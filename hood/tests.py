from django.test import TestCase
from .models import Posts, Profile, NeighbourHood, Businesses
from django.contrib.auth.models import User

# Create your tests here.

class ProfileTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.liz = Profile(id = 125, full_name = "niwiduhaye", profile_pic = "",userId = 1, user_email = "fionaniwe2020@gmail.com")

    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.liz,Profile))
    
    def test_initialization(self):
        self.assertEqual(self.liz.full_name,"niwiduhaye")
        self.assertEqual(self.liz.profile_pic,"")
        self.assertEqual(self.liz.userId, 1)
        self.assertEqual(self.liz.user_email, "fionaniwe2020@gmail.com")

    # Testing Save method
    def test_create_profile(self):
        self.liz.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles)>0)

    # Testing Delete method
    def test_delete_profile(self):
        self.liz.delete_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) == 0)



class NeighbourhoodTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.karen = NeighbourHood(id = 10, neighbourhood_name = "nyakabanda", neighbourhood_location = "nyarugenge",occupants_count = 200)

    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.karen,NeighbourHood))
    
    def test_initialization(self):
        self.assertEqual(self.karen.neighbourhood_name,"nyakabanda")
        self.assertEqual(self.karen.neighbourhood_location,"nyarugenge")
        self.assertEqual(self.karen.occupants_count, 200)
     

    # Testing Save method
    def test_create_neigborhood(self):
        self.karen.save_neighborhood()
        neighborhoods = NeighbourHood.objects.all()
        self.assertTrue(len(neighborhoods)>0)

    # Testing Delete method
    def test_delete_neigborhood(self):
        self.karen.delete_neighborhood()
        neighborhoods = NeighbourHood.objects.all()
        self.assertTrue(len(neighborhoods) == 0)


    
class PostsTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.liz = Profile(full_name = "niwiduhaye", profile_pic = "",userId = 1, user_email = "fionaniwe2020@gmail.com")
        
        self.karen = NeighbourHood(neighbourhood_name = "nyakabanda", neighbourhood_location = "nyarugenge",occupants_count = 200)
       
        self.posts = Posts(id = 125, title = "New Post", post = "very good",pub_date = 8/1/2021, poster_id = 4)
    

        self.user = User(username="Moringa")

    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.posts,Posts))

    def test_initialization(self):
        self.assertEqual(self.posts.title,"New Post")
        self.assertEqual(self.posts.post,"very good")
        self.assertEqual(self.posts.pub_date, 8/1/2021)
        self.assertEqual(self.posts.poster_id,4)


    # Testing Delete method
    def test_delete_post(self):
        self.posts.delete_post()
        posts = Posts.objects.all()
        self.assertTrue(len(posts) == 0)


class BusinessesTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.florist = Businesses(id = 125, business_name = "sm", business_description = "nike shop",contact_person ="ange", business_email = "ange@gmail.com")

    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.florist,Businesses))
    
    def test_initialization(self):
        self.assertEqual(self.florist.business_name,"sm")
        self.assertEqual(self.florist.business_description,"nike shop")
        self.assertEqual(self.florist.contact_person, "ange")
        self.assertEqual(self.florist.business_email, "ange@gmail.com")

    # Testing Save method
    def test_create_business(self):
        self.florist.save_business()
        businesses = Businesses.objects.all()
        self.assertTrue(len(businesses)>0)

    # Testing Delete method
    def test_delete_business(self):
        self.florist.delete_business()
        businesses = Businesses.objects.all()
        self.assertTrue(len(businesses) == 0)