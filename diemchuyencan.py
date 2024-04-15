class SinhVien():
    def __init__(self, id, name, class_name):
        self.id = id
        self.name = name
        self.class_name = class_name
        self.diemdanh = ""
        self.diemcc = 10
        self.ghichu = ""

    def xulydiemcc(self, diemdanh):
        for i in range(len(diemdanh)):
            if diemdanh[i] == "x":
                continue
            elif diemdanh[i] == "m":
                self.diemcc -= 1
            else:
                self.diemcc -= 2
        if self.diemcc < 0:
            self.diemcc = 0
        if self.diemcc == 0:
            self.ghichu = "KDDK"

    def __str__(self):
        return f"{self.id} {self.name} {self.class_name} {self.diemcc} {self.ghichu}"

n = int(input())
list_sinhvien = []
for i in range(n):
    sinh_vien = SinhVien(input(), input(), input())
    list_sinhvien.append(sinh_vien)

for i in range(n):
    id, diemdanh = input().split()
    for sinh_vien in list_sinhvien:
        if sinh_vien.id == id:
            sinh_vien.xulydiemcc(diemdanh)
            break

for sinh_vien in list_sinhvien:
    print(sinh_vien)