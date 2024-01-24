from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from users.models import CustomUser
# Create your models here.

class BooksModel(models.Model):
    book_name = models.CharField(max_length=25)
    short_description = models.TextField()
    publisher = models.CharField(max_length=25)
    book_image = models.ImageField(default='default_book_image.jpg',upload_to='media/')
    book_price = models.DecimalField(max_digits=6,decimal_places=2)
    isbn = models.IntegerField(unique=True,primary_key=True)
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.book_name
    

class AuthorModel(models.Model):
    author_name = models.CharField(max_length=25)
    author_f_name = models.CharField(max_length=25)
    email = models.EmailField()
    author_prof = models.CharField(max_length=25)

    def __str__(self):
        return self.author_name
    

class BookAuthorModel(models.Model):
    book = models.ForeignKey(BooksModel,blank=True,null=True, on_delete=models.CASCADE)
    author = models.ForeignKey(AuthorModel,blank=True,null=True,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author} {self.book}"
    
    def get_info(self):
        return f"{self.author} {self.book}"
    

class ReviewBookModel(models.Model):
    user = models.ForeignKey(CustomUser,blank=True,null=True,on_delete=models.CASCADE)
    book = models.ForeignKey(BooksModel,blank=True,null=True,on_delete=models.CASCADE)
    comment_body = models.TextField()
    star_given = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(limit_value=1),
            MaxValueValidator(limit_value=5),
        ]
    )
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.user.username