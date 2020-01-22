import requests

while True:
    data = requests.get("https://api.lyrics.ovh/v1/%s/%s" % (input("Please, Enter the artist name: ").strip(), input("Please, Enter the song name: ").strip())).json()
    print("\n")
    if "lyrics" in data and data["lyrics"] is not "":
        for i in data["lyrics"].split("\n"):
            print(i)
    else:
        print("No lyrics found")
    print("\n")
