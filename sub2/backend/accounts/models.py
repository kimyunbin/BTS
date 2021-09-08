from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager



class CustomUserManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            name=name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password=None):
        user = self.create_user(
            email,
            password=password,
            name=name
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
        
class User(AbstractBaseUser):
    # default id / password / last_login 
    username = models.EmailField(max_length=255, unique=True)
    nickname =  models.CharField(max_length=50)
    created_on = models.DateTimeField(auto_now_add=True)
    
    # info1 = models.charFIeld()
    # info2 = 
    # .....
    
    class Meta:
        db_table = 'user'

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    # REQUIRED_FIELDS = ['username'] createsuper user용 

