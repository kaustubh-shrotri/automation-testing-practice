from unittest import TestCase
from blog import Blog
class BlogTest(TestCase):
    def test_create_post_in_blog(self):
        b = Blog('test', 'author')
        b.create_post('test post','test content')

        self.assertEqual(len(b.posts),1)
        self.assertEqual(b.posts[0].title, 'test post')
        self.assertEqual(b.posts[0].content, 'test content')

    def test_json_no_posts(self):
        b = Blog('test', 'author')
        expected = {'Title': 'test',
                    'Author': 'author',
                    'Posts': []}
        self.assertEqual(b.json(), expected)

    def test_json(self):
        b = Blog('test', 'author')
        b.create_post('test post', 'test content')

        expected = {'Title': 'test',
                    'Author': 'author',
                    'Posts': [{'title': 'test post',
                               'content': 'test content'}]}

        self.assertEqual(b.json(), expected)
