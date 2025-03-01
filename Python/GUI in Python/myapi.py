import paralleldots

class API:
    
    def __init__(self):
        paralleldots.set_api_key('API key')
        
    def sentiment_analysis(self,text):
        result = paralleldots.sentiment(text)
        return result
    
    def ner_analysis(self,text):
        result = paralleldots.ner(text)
        return result
    
    def emotion_analysis(self,text):
        result = paralleldots.emotion(text)
        return result
    