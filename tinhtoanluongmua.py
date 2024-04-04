from datetime import datetime

class Tram_d0():
    def __init__(self, tentram, thoigianbatdau, thoigianketthuc, luongmua):
        self.tentram = tentram
        self.thoigianbatdau = datetime.strptime(thoigianbatdau, "%H:%M")
        self.thoigianketthuc = datetime.strptime(thoigianketthuc, "%H:%M")
        self.tongthoigian = (self.thoigianketthuc - self.thoigianbatdau).seconds / 3600  # convert to hours
        self.luongmua = luongmua

tram_dict = {}
n = int(input())
for i in range(n):
    tentram = input()
    thoigianbatdau = input()
    thoigianketthuc = input()
    luongmua = float(input())
    tram = Tram_d0(tentram, thoigianbatdau, thoigianketthuc, luongmua)
    if tentram not in tram_dict:
        tram_dict[tentram] = [tram.tongthoigian, tram.luongmua]
    else:
        tram_dict[tentram][0] += tram.tongthoigian
        tram_dict[tentram][1] += tram.luongmua

for idx, (tentram, (tongthoigian, tongluongmua)) in enumerate(tram_dict.items(), start=1):
    print(f"T{idx:02d} {tentram} {tongluongmua / tongthoigian:.2f}")