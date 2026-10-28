"""Refresh the rounded activity numbers on the Ace organization profile.

Modeled on simonw/simonw's build_readme.py: count from the live GitHub API,
then rewrite only the text between the stats markers in profile/README.md.
Numbers are rounded down so the public page never overstates them.
"""

import datetime
import json
import os
import pathlib
import re
import sys
import urllib.parse
import urllib.request

ORG = "acemarketingservices"
SINCE = "2026-04-01"
README = pathlib.Path(__file__).resolve().parent.parent / "profile" / "README.md"
MARKER = re.compile(
    r"(<!-- stats starts -->).*(<!-- stats ends -->)", re.DOTALL
)


def merged_count(token, since):
    query = f"org:{ORG} is:pr is:merged merged:>={since}"
    url = "https://api.github.com/search/issues?" + urllib.parse.urlencode(
        {"q": query, "per_page": 1}
    )
    request = urllib.request.Request(
        url,
        headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
        },
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.load(response)["total_count"]


def round_down(number, step):
    return f"{number // step * step:,}+"


def main():
    token = os.environ.get("ORG_STATS_TOKEN")
    if not token:
        print("ORG_STATS_TOKEN is not set; leaving the profile unchanged.")
        return 0
    today = datetime.date.today()
    last_30 = (today - datetime.timedelta(days=30)).isoformat()
    total = merged_count(token, SINCE)
    month = merged_count(token, last_30)
    block = (
        "\n```yaml\n"
        f"changes shipped:  {round_down(total, 100)} since April 2026\n"
        f"last 30 days:     {round_down(month, 100)}\n"
        f"updated:          {today:%B %-d, %Y}, automatically every day\n"
        "```\n"
    )
    text = README.read_text()
    if not MARKER.search(text):
        print("Stats markers not found in profile/README.md", file=sys.stderr)
        return 1
    README.write_text(MARKER.sub(lambda m: m.group(1) + block + m.group(2), text))
    return 0


if __name__ == "__main__":
    sys.exit(main())
