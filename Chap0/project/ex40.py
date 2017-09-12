# coding:utf-8

# 转换成py3后的练习LPTHW中的ex40.py
# 相比于py2主要是print的不同

class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics
		
    def  sing_me_a_song(self):
        for line in self.lyrics:
            print (line)

little_star = Song(["一闪一闪亮晶晶","天上都是小星星"])
two_tigers = Song(["两只老虎","两只老虎跑得快","一只没有耳朵","一只没有尾巴"]) 

little_star.sing_me_a_song()
two_tigers.sing_me_a_song()

