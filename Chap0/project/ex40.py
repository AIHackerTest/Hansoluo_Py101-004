# coding:utf-8

# ת����py3�����ϰLPTHW�е�ex40.py
# �����py2��Ҫ��print�Ĳ�ͬ

class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics
		
    def  sing_me_a_song(self):
        for line in self.lyrics:
            print (line)

little_star = Song(["һ��һ��������","���϶���С����"])
two_tigers = Song(["��ֻ�ϻ�","��ֻ�ϻ��ܵÿ�","һֻû�ж���","һֻû��β��"]) 

little_star.sing_me_a_song()
two_tigers.sing_me_a_song()

