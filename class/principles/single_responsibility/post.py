class BlogPost:
    def __init__(self, title:str,content:str, author:str):
        self.title = title
        self.content = content
        self.author = author
        self.published = False

    def publish(self):
        self.published = True
        print(f"Blog post {self.title} has been published")

    def unpublish(self):
        self.published = False
        print(f"Blog post {self.title} has been unpublished")

    def print_post_info(self):
        print(f"Title: {self.title}")
        print(f"Content: {self.content}")
        print(f"Author: {self.author}")
        print(f"Published: {self.published}")

# Instantiate the class
post = BlogPost("My First Blog Post", "This is the content of my first blog post.", "John Doe")
post.print_post_info()
post.publish()
post.print_post_info()
post.unpublish()
post.print_post_info()

# with SRP
class BlogPost2:
    def __init__(self, title:str,content:str, author:str):
        self.title = title
        self.content = content
        self.author = author
        self.published = False

class BlogPostManager:
    @staticmethod
    def publish(post:BlogPost2):
        post.published = True
        print(f"Blog post {post.title} has been published")
    @staticmethod
    def unpublish(post:BlogPost2):
        post.published = False
        print(f"Blog post {post.title} has been unpublished")
class BlogPostPrinter:
    @staticmethod
    def print_post_info(post:BlogPost2):
        print(f"Title: {post.title}")
        print(f"Content: {post.content}")
        print(f"Author: {post.author}")
        print(f"Published: {post.published}")

# Instantiate the class
post2 = BlogPost2("My First Blog Post", "This is the content of my first blog post.", "John Doe")
BlogPostPrinter.print_post_info(post2)
BlogPostManager.publish(post2)
BlogPostPrinter.print_post_info(post2)
BlogPostManager.unpublish(post2)
BlogPostPrinter.print_post_info(post2)

    
