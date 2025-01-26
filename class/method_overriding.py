import re
class Parser:
    phone_pattern = r'\d{3}-\d{3}-\d{4}'
    def __init__(self,text):
        self.text = text

    def email(self):
        match = re.search(r'[a-z0-9\.\-+_]+a[a-z0-9\.\-+_]+\.[a-z]+',self.text)
        if match:
            return match.group(0)
        return None
    def phone(self):
        match = re.search(self.phone_pattern,self.text)
        if match:
            return match.group(0)
        return None
    
    def parse(self):
        return {
            'email':self.email(),
            'phone':self.phone()
        }
    
class UKParser(Parser):
    phone_pattern = r'\+\d{1}-\d{3}-\d{3}-\d{4}'
    
    # def phone(self):
    #     match = re.search(r'\+\d{1}-\d{3}-\d{3}-\d{4}',self.text)
    #     if match:
    #         return match.group(0)
    #     return None

if __name__ == '__main__':
    print(__name__)
    s = 'Contact us via email at 1Hd8t@example.com or phone at 123-456-7890'
    parser = Parser(s)
    print(parser.parse())

    s2 = 'Contact us via email at 1Hd8t@example.com or phone at +1-123-456-7890'
    parser = UKParser(s2)
    print(parser.parse())