class Game_Thu():
    def __init__(self,id,name,timein,timeout):
        self.id = id
        self.name = name
        self.timein = self.convert_time(timein)
        self.timeout = self.convert_time(timeout)
        self.time = self.timeout - self.timein
    def convert_time(self,time):
        time = time.split(':')
        return int(time[0])*60 + int(time[1])
    def __str__(self):
        return f"{self.id} {self.name} {self.time//60} gio {self.time%60} phut"   
t = int(input())
players=[]
for i in range(t):
    nguoichoi=Game_Thu(input(),input(),input(),input())
    players.append(nguoichoi)
players.sort(key=lambda x:x.time,reverse=True)
for i in players:
    print(i)
        