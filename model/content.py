
class Sentences():
    def __init__(self,text="",keywords = [],imageUrls = []):
        self.text= text
        self.keywords = keywords
        self.imageUrls = imageUrls
        
    def toString(self):
        return "Text: {}, Keywords: {}, imageUrls: {}".format(self.text,self.keywords,self.imageUrls)
        
# =========================================================   
        
class Content():
    def __init__(self,searchTerm,
                 prefix,
                 sourceContentOriginal=None,
                 sourceContentSanitized=None):
        self.searchTerm = searchTerm
        self.prefix = prefix
        self.sourceContentOriginal = sourceContentOriginal
        self.sourceContentSanitized = sourceContentSanitized
        self.setences = []
        
    def toString(self):
        return """ 
        SearchTerm: {},
        Prefix: {}
        """.format(self.searchTerm,self.prefix)