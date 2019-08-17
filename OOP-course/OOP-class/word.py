class Word:

    def __init__(self, text, part):
        self.text=text
        self.part=part

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
                arr.append(list[index].part)

        print(set(arr))

    def __init__(self,  content):
        self.content=content

words = [["собака", "сущ"],["ела", "глагол"], ["колбасу", "сущ"], ["вечером", "наречие"]]
list=[]
for item in words:
    list.append(Word(item[0], item[1]))


dog = Sentence([0,2,6,1])
dog.show(list)
dog.show_parts(list)