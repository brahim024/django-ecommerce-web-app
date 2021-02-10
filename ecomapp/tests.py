from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User=get_user_model()
# Create your tests here.
class UserTestCase(TestCase):
    def setUp(self):
        user_a=User(username='brahim024',email='boughanm6@gmail.com')
        user_a.is_staff=True
        user_a.is_superuser=True
        user_a_pw='admin000'
        self.user_a_pw=user_a_pw
        
        user_a.save()
        user_a.set_password(user_a_pw)
        self.user_a=user_a
        
    
    def test_user_count(self):
        
        user_count=User.objects.all().count()
        self.assertEqual(user_count,1)
        self.assertNotEqual(user_count,0)
        
    def test_user_password(self):
        '''user_qs=User.objects.filter(username__iexact='brahim024')
        user_exists=user_qs.exists() and user_qs.count() == 1
        self.assertTrue(user_exists)
        user_a=user_qs.first()'''
        self.assertTrue(self.user_a.check_password('admin000'))
        print(self.user_a_pw)

