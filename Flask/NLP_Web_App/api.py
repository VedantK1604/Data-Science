
import paralleldots
paralleldots.set_api_key('MCjkbJrHhYTrAZeOAdtcvBEnLJyTja5CBR9O9mmrSJA')

def ner(text):
    ner = paralleldots.ner(text)
    return ner