import urllib.request
import urllib.parse
import json

movies = ["Get Out (film)", "A Quiet Place", "Se7en", "Inception", "Step Brothers (film)", "The Notebook"]

images = {}
for title in movies:
    encoded_title = urllib.parse.quote(title)
    url = f"https://en.wikipedia.org/w/api.php?action=query&titles={encoded_title}&prop=pageimages&format=json&pithumbsize=500"
    
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        response = urllib.request.urlopen(req)
        data = json.loads(response.read().decode('utf-8'))
        pages = data['query']['pages']
        for page_id, page_info in pages.items():
            if 'thumbnail' in page_info:
                images[title] = page_info['thumbnail']['source']
    except Exception as e:
        print(f"Error for {title}: {e}")

print(images)
