def make_album(name, title, num_songs=None):
    if num_songs:
        return {"artist_name": name, "album_title": title, "num_songs": num_songs}
    else:
        return {"artist_name": name, "album_title": title}

print(make_album("Imagine Dragons", "Night Visions", 14))
print(make_album("Linkin Park", "Hybrid Theory"))
print(make_album("Hiroyuki Sawano", "JEOPARDY"))
