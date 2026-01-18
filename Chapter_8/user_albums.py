def make_album(name, title, num_songs=None):
    if num_songs:
        return {"artist_name": name, "album_title": title, "num_songs": num_songs}
    else:
        return {"artist_name": name, "album_title": title}

while True:
    print("Enter 'q' either in the field requesting artist name or album name to exit the loop.")
    artist_n = input("Please enter the artist name: ")
    album_n = input("Please enter the album name: ")
    if artist_n == "q" or album_n == "q":
        break
    else:
        print(make_album(artist_n, album_n))