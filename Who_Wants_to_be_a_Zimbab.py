#Who Wants to be a Zimbab
from ast import While
from operator import index
import random
class Player:
    def __init__(self,question = " ",gindex= 234,answer = "", points = 0, live = 3):
        self.question= question
        self.gindex= gindex
        self.answer= answer
        self.points= points
        self.live = live
        
    def generate_gindex(self):
        self.gindex = random.randint(0,len(question_list)-1)

    def generate_question(self):
        self.question = question_list[self.gindex]
        print(self.question)
        question_list.remove(self.question)

    def point_nambah(self):
        self.points+= 36190
        print("Congrats, correct answer. You have accumulated "+str(self.points)+" ZWD On to the next one")
    
    def wrong_ans(self):
        self.live = self.live-1
        if self.live >0 :
            print("Aw darn it, lost a life. Don't worry you still have "+ str(self.live) +" left!")
        else :
            print("GAME OVER")
            exit()

print("################################")
print("# Who Wants To be a Zimbabwean #")
print("################################")
question_list = ["What is the height of the Eifell Tower? 200 m | 300 m | 250 m", "Who is the first President of Indonesia? Soekarno | B.J. Habiebie | Salman", "On what year did the bomb of Hiroshima was dropped ? 1944|1947|1945", "Table salt has the scientifical name of ... Magnesium Sulfide | Sodium Chloride | Sulfuric Acid"]
wrong_answer_list = ["200 m", "250 m", "b.j. habiebie", "salman","1944", "1947", "magnesium sulfide", "sulfuric acid"]
answer_list = ["300 m", "soekarno", "1945", "sodium chloride"]
player_one = Player()
while question_list !=[] :
    player_one.generate_gindex()
    player_one.generate_question()
    print("Input your answer")
    acts = input()
    acts = acts.lower()
    if acts in answer_list:
        player_one.point_nambah()
    elif acts in wrong_answer_list:
        player_one.wrong_ans()
    else:
        print("Whoops, it seems like your answer doesn't match up to any of the options")
        continue
print("CONGRATULATION !!! You've become the richest man in Zimbabwe")