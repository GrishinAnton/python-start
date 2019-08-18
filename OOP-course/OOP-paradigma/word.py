class Word:

    def __init__(self, text):
        self.text=text

class Sentence:

    def show(self, list):
        str=''

        for index in self.content:
            if index <= len(list):
                str += list[index].text + ' '

        print(str)

    def show_parts(self, list):
        arr=[]
        for index in self.content:
            if index <= len(list):
                arr.append(list[index].part())

        print(set(arr))

    def __init__(self,  content):
        self.content=content

class Noun(Word):
    __grammar='сущ'

    def part(self):
        return 'существительное'


class Verb(Word):
    __grammar='гл'

    def part(self):
        return 'глагол'

words=[]
words.append(Noun('собака'))
words.append(Verb('ела'))
words.append(Noun('колбасу'))
words.append(Noun('кот'))


dog = Sentence([0,2,6,1])
dog.show(words)
dog.show_parts(words)
