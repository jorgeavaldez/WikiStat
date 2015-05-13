import requests

requestSchema = "/w/api.php?action=query&prop=extracts&format=json&explaintext=&exsectionformat=plain&titles={0}"

class WikiRequests:

    def queryPage(self, query):
        self.url = "http://en.wikipedia.org" + requestSchema.format(query.replace(" ", "%20"))
        self.jsonDump = requests.get(self.url).json()
        return self.jsonDump

    def getJsonDump(self):
        return self.jsonDump if self.jsonDump else null

    def getUrl(self):
        return self.url

wr = WikiRequests()
json = wr.queryPage("John Carmack")
print((json["query"]["pages"].itervalues().next()["extract"]).encode("utf-8"))
