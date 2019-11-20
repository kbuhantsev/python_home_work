
class MyDict(dict):

    def __setattr__(self, key, value):
        self[key] = value

    def __getattr__(self, item):
        return self[item]


md = MyDict()
md['test'] = 1
print(md.test)

md.attribute = 2
print(md['attribute'])
