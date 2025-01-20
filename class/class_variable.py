from pprint import pprint
class HtmlDocument:
    # class variable
    extension = 'html'
    version = '5'


    # callable class attribute
    def render():
        print('Rendering html document')

    def greet(self):
        print(f'Hello {self.extension}')

print(HtmlDocument.__name__)
print(type(HtmlDocument))

# check instance
print(isinstance(HtmlDocument,type))

# print class variable
print(HtmlDocument.extension)   
print(HtmlDocument.version)
media_tpye = getattr(HtmlDocument,'media_type','text/html')
print(media_tpye)

# set values of class variable
HtmlDocument.version=10
print(HtmlDocument.version)
setattr(HtmlDocument,'version',20)
print(HtmlDocument.version)

# delete class variable
# del HtmlDocument.version
# delattr(HtmlDocument,'version')
# print(HtmlDocument.version)

# class variable storage
pprint(HtmlDocument.__dict__)
HtmlDocument.render()
print(HtmlDocument.render)
print(type(HtmlDocument.render))
print(type(HtmlDocument.greet))

http_render = HtmlDocument()
print(http_render.render)
print(type(http_render.render) is type(HtmlDocument.render))
print(type(http_render.render))
print(type(HtmlDocument.render))
http_render.render()