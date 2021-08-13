import requests

class DictionarySearch:
    word = ""
    meaning = ""
    verbe = ""
    url = ""

    def __init__(self):
        self.word = ""
        self.meaning = ""
        self.verbe = ""
        self.url = "https://api.dictionaryapi.dev/api/v2/entries/en/"

    def get_meaning(self, q):
        self.word = q

        res = requests.get(self.url + q)
        data = res.json()
        meaning = data[0]["meanings"][0]
        self.meaning = meaning["definitions"][0]["definition"]
        self.verbe = meaning["partOfSpeech"].capitalize()
        return q + ". " + self.verbe + ". " + self.meaning




ds = DictionarySearch()
word = input("Word? ")
print("Output: " + ds.get_meaning(word))
