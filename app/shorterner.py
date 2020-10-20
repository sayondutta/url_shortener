import random
class shortener(object):
    def __init__(self):
        self.book = {}
        self.revbook = {}
        self.base = 62
        self.chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.id = 1

    def redirect(self,url):
        if url in self.book:
            return self.read(url)
        else:
            self.write(url)
            return self.read(url)

    def read(self,url):
        return self.book[url]

    def encode(self,id):
        cur_id = ''
        while id:
            r = id%self.base
            cur_id += self.chars[r]
            id //= self.base
        return cur_id

    def write(self,url):
        s = [self.chars[random.randint(0,61)] for i in range(6)]
        s = ''.join(s)
        cur_id = s+self.encode(self.id)
        self.book[url] = cur_id
        self.revbook[cur_id] = url
        self.id += 1