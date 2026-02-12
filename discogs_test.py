import discogs_client

# 1. Authenticate
d = discogs_client.Client('VinylScout/1.0', user_token='FBBAkTDidzFPdBfoImejnBMSoHNaNYkgAirtlhek')

# 2. Search for an artist (Example: Frank Ocean)
print("Searching for Frank Ocean...")
results = d.search('Frank Ocean', type='artist')
artist = results[0]
print(f"Found Artist: {artist.name}")

# 3. Get their releases
print(f"Fetching releases for {artist.name}...")
releases = artist.releases.page(1) # Get first page

for release in releases[:5]: # Just show first 5
    print(f"- {release.title} ({release.year})")