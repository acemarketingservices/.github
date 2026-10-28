"""Draw the rounded activity card shown on the Ace organization profile.

Modeled on simonw/simonw's build_readme.py (count from the live GitHub API)
and lowlighter/metrics (write an SVG card to its own branch, because the
profile's main branch only accepts reviewed pull requests). Numbers are
rounded down so the public page never overstates them.
"""

import datetime
import json
import os
import sys
import urllib.parse
import urllib.request

ORG = "acemarketingservices"
SINCE = "2026-04-01"

CARD = """<svg xmlns="http://www.w3.org/2000/svg" width="560" height="132" viewBox="0 0 560 132" role="img" aria-label="{label}">
  <style>
    .bg {{ fill: #ffffff; stroke: #d0d7de; }}
    .big {{ font: 700 30px -apple-system, Segoe UI, Helvetica, Arial, sans-serif; fill: #1f2328; }}
    .small {{ font: 400 13px -apple-system, Segoe UI, Helvetica, Arial, sans-serif; fill: #59636e; }}
    @media (prefers-color-scheme: dark) {{
      .bg {{ fill: #0d1117; stroke: #30363d; }}
      .big {{ fill: #f0f6fc; }}
      .small {{ fill: #9198a1; }}
    }}
  </style>
  <rect class="bg" x="0.5" y="0.5" width="559" height="131" rx="10"/>
  <text class="big" x="28" y="58">{total}</text>
  <text class="small" x="28" y="82">changes shipped since April 2026</text>
  <text class="big" x="300" y="58">{month}</text>
  <text class="small" x="300" y="82">in the last 30 days</text>
  <text class="small" x="28" y="114">Updated {today}, automatically every day</text>
</svg>
"""


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
    if len(sys.argv) != 2:
        print("usage: update_profile_stats.py OUTPUT.svg", file=sys.stderr)
        return 2
    token = os.environ.get("ORG_STATS_TOKEN")
    if not token:
        print("ORG_STATS_TOKEN is not set; leaving the card unchanged.")
        return 0
    today = datetime.date.today()
    last_30 = (today - datetime.timedelta(days=30)).isoformat()
    total = round_down(merged_count(token, SINCE), 100)
    month = round_down(merged_count(token, last_30), 100)
    label = f"{total} changes shipped since April 2026, {month} in the last 30 days"
    with open(sys.argv[1], "w") as out:
        out.write(
            CARD.format(
                label=label, total=total, month=month, today=f"{today:%B %-d, %Y}"
            )
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
