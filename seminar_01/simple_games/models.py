from django.db import models
from datetime import datetime as dt


class CoinPlay(models.Model):

    # throws = []

    side = models.CharField(max_length=10)
    time = models.DateTimeField(auto_now_add=True)

    # @staticmethod
    # def get_throws(amount):
    #     obverse_cnt = 0
    #     reverse_cnt = 0
    #     for item in CoinPlay.throws[-amount:]:
    #         if item[1] == 'obverse':
    #             obverse_cnt += 1
    #         else:
    #             reverse_cnt += 1
    #     return {'obverse': obverse_cnt, 'reverse': reverse_cnt, }

    @staticmethod
    def add_throw(value):
        sides = ('obverse', 'reverse')
        # CoinPlay.throws.append((dt.now(), sides[value]))
        return {'time': dt.now(), 'side': sides[value]}

    def __str__(self):
        return f'{self.side} {self.time}'
