class nhanvien:
    count = 0

    def __init__(self, hoten, lithuyet, thuchanh):
        self.hoten = hoten
        self.lithuyet = self.convert_score(lithuyet)
        self.thuchanh = self.convert_score(thuchanh)
        self.trungbinh = round((self.lithuyet + self.thuchanh) / 2, 2)
        nhanvien.count += 1
        self.id = f"TS{self.count:02}"

    def convert_score(self, score):
        if '.' not in score and len(score) > 1:
            score = score[:1] + '.' + score[1:]
        return float(score)

    def xeploai(self):
        if self.trungbinh < 5:
            return "TRUOT"
        elif 5 <= self.trungbinh < 8:
            return "CAN NHAC"
        elif 8 <= self.trungbinh <= 9.5:
            return "DAT"
        else:
            return "XUAT SAC"

t = int(input())
list_nv = []
for i in range(t):
    NV = nhanvien(input(), input(), input())
    list_nv.append(NV)

list_nv.sort(key=lambda x: x.trungbinh, reverse=True)

for nv in list_nv:
    print(f"{nv.id} {nv.hoten} {nv.trungbinh:.2f} {nv.xeploai()}")