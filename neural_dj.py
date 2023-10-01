import os
from metaphor_python import Metaphor
#from datetime import datetime, timedelta
metaphor = Metaphor(os.getenv("METAPHOR_API_KEY"))


#cutoff = (datetime.today() - timedelta(days=50)).strftime('%Y-%m-%d')

starting_point = input(
    "Name a song to base the search on (default= \"storken - lille vals\"): "
)

# "storken - lille vals" is an electronic 80s inspired synth track
if starting_point == "":
    starting_point = "storken - lille vals"

print(f"\nConstructing playlist starting from: \"{starting_point}\" ...\n")

# ideally would be ["youtube.com","soundcloud.com","bandcamp.com"] etc, causes errors
domains = ["youtube.com"]

starting_point_url = metaphor.search(
  f"{starting_point}",
  num_results=1,
  include_domains=domains,
  use_autoprompt=True,
  type="keyword",
).results[0].url

url = starting_point_url
for i in range(5):
    response = metaphor.find_similar(
            f"{url}",
            num_results=3,
            include_domains=domains,
        ).results[2]
    url = response.url

    print(f"Track {i+1}\n\tTitle: {response.title}\n\turl: {url}\n")
