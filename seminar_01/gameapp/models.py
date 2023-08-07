from django.db import models
from datetime import datetime as dt


class Coin(models.Model):
    # trows = {"орел": [], "решка": []}
    trows = []

    side = models.CharField(max_length=20)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Coin: {self.side}, time: {self.time}'

    @staticmethod
    def get_trows(amount):
        obverse_cnt = 0
        reverse_cnt = 0
        for item in Coin.trows[-amount:]:
            if item[1] == "obverse":
                obverse_cnt += 1
            else:
                reverse_cnt += 1
        return f'Obverse: {obverse_cnt}, Reverse: {reverse_cnt}'

    @staticmethod
    def add_trow(side):
        Coin.trows.append((dt.now(), side))


class Author(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    biography = models.TextField()
    birthday = models.DateField()

    def __str__(self):
        return f'Author: {self.name} {self.surname}, email: {self.email}, biography: {self.biography}, birthday: {self.birthday}'

    def get_fullname(self):
        return f'{self.name} {self.surname}'


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    public_date = models.DateField(auto_now=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    views = models.IntegerField(default=0)
    published = models.BooleanField(default=False)

    def __str__(self):
        return f'Title is {self.title}.\nContent is: {self.content}.\nPublished date: {self.public_date}. Author is {Author.get_fullname(self.author)}' \
               f'Is category: {self.category}. Count of views: {self.views}.\nStatus: {self.published}.'
