# class creation
class Developer:
 
    def code(self, lang):
        self.languages = ['PYTHON', 'JAVA', 'C++']
        # print(lang)
        for i in self.languages:
            if i == lang.upper():
                print(lang, " language in the list")

    def resume(self):
        #self.language = ['TAMIL', 'ENGLISH', 'HINDI']
        # print(lang)
        print("======Developer languages list=======")
        for i in self.languages:
            # if i == lang.upper():
            print(i)

    def __init__(self):
        self.languages = ['TAMIL', 'ENGLISH', 'HINDI']

dev = Developer()
lang = input("Enter language: ")
dev.code(lang)
dev.resume()

class SrDeveloper(Developer):
   def __init__(self):
        self.reviews = []
        Developer.__init__(self)
   def review(self,review):
       self.reviews
       self.languages
            
        
class TechLead(SrDeveloper):
      def design(self):
         self.x=5






