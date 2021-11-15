import wikipedia
from Commands.Speaker import mainspeak

def wikisearch(cmmd):
        mainspeak("Searching wikipedia")
        query = cmmd.replace("search for","")
        query = query.replace("in wikipedia","")

        try:
            results = wikipedia.summary(query,2)
            mainspeak("Here is what I found,  "+ results)
        except Exception as e :
            mainspeak("could not find anything relevant in wikipedia Sir")