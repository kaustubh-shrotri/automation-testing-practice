from post import Post


class Blog:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.posts = []

    def __repr__(self):
        if len(self.posts) != 1:
            self.print_s = 's'
        else:
            self.print_s = ''
        return f'{self.title} by {self.author} ({len(self.posts)} post{self.print_s})'

    def create_post(self, title, content):
        self.posts.append(Post(title, content))

    def json(self):
        return {'Title': self.title,
                'Author': self.author,
                'Posts': [post.json() for post in self.posts]}
