import re
import os
import urllib.parse

def patch_file(filepath):
    if not os.path.exists(filepath):
        return
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Dictionary of 404 urls to replace with text placeholders
    bad_urls = {
        'https://image.tmdb.org/t/p/w500/tXxtAWX4Xogk1P1aC2vMOrL0uV7.jpg': 'Get Out',
        'https://image.tmdb.org/t/p/w500/nAU74GmpUk7t5iklEp3bufwDq4n.jpg': 'A Quiet Place',
        'https://image.tmdb.org/t/p/w500/6yoghtyTpznpBik8EngEmJskVPh.jpg': 'Se7en',
        'https://image.tmdb.org/t/p/w500/oYuLEt3zVCKq57qu2F8dT7NIa6f.jpg': 'Inception',
        'https://image.tmdb.org/t/p/w500/gfVQvO2Qz9n352rBsh0D4ZqL0Uo.jpg': 'Step Brothers',
        # One last unsplash URL that was not caught maybe?
        'https://images.unsplash.com/photo-1518199266791-5375a83190b7?auto=format&fit=crop&q=80&w=400': 'The Notebook',
    }
    
    for bad_url, title in bad_urls.items():
        encoded = urllib.parse.quote(title)
        placeholder = f"https://placehold.co/500x750/1e293b/ffffff?text={encoded}"
        content = content.replace(bad_url, placeholder)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

patch_file("static/index.html")
patch_file("src/data/movies.js")
print("Fixed invalid images")
