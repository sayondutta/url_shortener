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
        cur_id = 'moriarty'+self.encode(self.id)
        self.book[url] = cur_id
        self.revbook[cur_id] = url
        self.id += 1