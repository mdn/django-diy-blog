from django.test import TestCase

# Create your tests here.

from django.contrib.auth.models import User #Blog author or commenter
from blog.models import BlogAuthor, Blog, BlogComment

class BlogAuthorModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        test_user1 = User.objects.create_user(username='testuser1', password='12345') 
        test_user1.save()
        cls.author = BlogAuthor.objects.create(user=test_user1, bio='This is a bio')
        
    def test_get_absolute_url(self):
        author=self.author       
        self.assertEqual(author.get_absolute_url(),f'/blog/blogger/{author.id}')
           
    def test_user_label(self):
        author=self.author
        field_label = author._meta.get_field('user').verbose_name
        self.assertEqual(field_label,'user')
        
    def test_bio_label(self):
        author=self.author
        field_label = author._meta.get_field('bio').verbose_name
        self.assertEqual(field_label,'bio')

    def test_bio_max_length(self):
        author=self.author
        max_length = author._meta.get_field('bio').max_length
        self.assertEqual(max_length,400)
        
    def test_object_name(self):
        author=self.author
        expected_object_name = author.user.username
        self.assertEqual(expected_object_name,str(author))
        
        

import datetime

class BlogModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        test_user1 = User.objects.create_user(username='testuser1', password='12345') 
        test_user1.save()
        blog_author = BlogAuthor.objects.create(user=test_user1, bio='This is a bio')
        cls.blog = Blog.objects.create(name='Test Blog 1',author=blog_author,description='Test Blog 1 Description')
        
    def test_get_absolute_url(self):
        blog=self.blog       
        self.assertEqual(blog.get_absolute_url(),f'/blog/blog/{blog.id}')
           
    def test_name_label(self):
        blog=self.blog
        field_label = blog._meta.get_field('name').verbose_name
        self.assertEqual(field_label,'name')
        
    def test_name_max_length(self):
        blog=self.blog
        max_length = blog._meta.get_field('name').max_length
        self.assertEqual(max_length,200)
        
    def test_description_label(self):
        blog=self.blog
        field_label = blog._meta.get_field('description').verbose_name
        self.assertEqual(field_label,'description')
        
    def test_description_max_length(self):
        blog=self.blog
        max_length = blog._meta.get_field('description').max_length
        self.assertEqual(max_length,2000)

    def test_date_label(self):
        blog=self.blog
        field_label = blog._meta.get_field('post_date').verbose_name
        self.assertEqual(field_label,'post date')
        
    def test_date(self):
        blog=self.blog
        the_date = blog.post_date
        self.assertEqual(the_date,datetime.date.today())

    def test_object_name(self):
        blog=self.blog
        expected_object_name = blog.name
        self.assertEqual(expected_object_name,str(blog))


class BlogCommentModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        test_user1 = User.objects.create_user(username='testuser1', password='12345') 
        test_user1.save()
        test_user2 = User.objects.create_user(username='testuser2', password='12345') 
        test_user2.save()
        blog_author = BlogAuthor.objects.create(user=test_user1, bio='This is a bio')
        blog_test = Blog.objects.create(name='Test Blog 1',author=blog_author,description='Test Blog 1 Description')
        cls.blog_comment=BlogComment.objects.create(description='Test Blog 1 Comment 1 Description', author=test_user2,blog=blog_test)

        
    def test_description_label(self):
        blogcomment=self.blog_comment
        field_label = blogcomment._meta.get_field('description').verbose_name
        self.assertEqual(field_label,'description')
        
    def test_description_max_length(self):
        blogcomment=self.blog_comment
        max_length = blogcomment._meta.get_field('description').max_length
        self.assertEqual(max_length,1000)
           
    def test_author_label(self):
        blogcomment=self.blog_comment
        field_label = blogcomment._meta.get_field('author').verbose_name
        self.assertEqual(field_label,'author')
        
    def test_date_label(self):
        blogcomment=self.blog_comment
        field_label = blogcomment._meta.get_field('post_date').verbose_name
        self.assertEqual(field_label,'post date')
        
    def test_blog_label(self):
        blogcomment=self.blog_comment
        field_label = blogcomment._meta.get_field('blog').verbose_name
        self.assertEqual(field_label,'blog')

    def test_object_name(self):
        blogcomment=self.blog_comment
        expected_object_name = ''
        len_title=75
        if len(blogcomment.description)>len_title:
            expected_object_name=blogcomment.description[:len_title] + '...'
        else:
            expected_object_name=blogcomment.description
            
        self.assertEqual(expected_object_name,str(blogcomment))

