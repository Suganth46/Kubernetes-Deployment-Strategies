import re
import os

js_path = "src/data/movies.js"
if os.path.exists(js_path):
    with open(js_path, "r", encoding="utf-8") as f:
        content = f.read()

    replacements = {
        'https://images.unsplash.com/photo-1505634524240-41dbd2449553?auto=format&fit=crop&q=80&w=400': 'https://image.tmdb.org/t/p/w500/tXxtAWX4Xogk1P1aC2vMOrL0uV7.jpg',
        'https://images.unsplash.com/photo-1605806616949-1e87b487cb2a?auto=format&fit=crop&q=80&w=400': 'https://image.tmdb.org/t/p/w500/nAU74GmpUk7t5iklEp3bufwDq4n.jpg',
        'https://images.unsplash.com/photo-1628045938222-26db129759db?auto=format&fit=crop&q=80&w=400': 'https://image.tmdb.org/t/p/w500/6yoghtyTpznpBik8EngEmJskVPh.jpg',
        'https://images.unsplash.com/photo-1509347528160-9a9e33742cdb?auto=format&fit=crop&q=80&w=400': 'https://image.tmdb.org/t/p/w500/oYuLEt3zVCKq57qu2F8dT7NIa6f.jpg',
        'https://images.unsplash.com/photo-1541818227606-d50d061c5f3e?auto=format&fit=crop&q=80&w=400': 'https://image.tmdb.org/t/p/w500/gfVQvO2Qz9n352rBsh0D4ZqL0Uo.jpg',
    }
    for old_str, new_str in replacements.items():
        content = content.replace(old_str, new_str)
        
    with open(js_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Updated src/data/movies.js")

