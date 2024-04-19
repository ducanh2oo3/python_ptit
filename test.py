n, m = map(int, input().split())
tong = 0
matran = []  # Khởi tạo matran như một danh sách rỗng
huongdichuyen = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
queue = []

for i in range(n):
    row = list(map(int, input().split()))  # Đọc một hàng từ input
    matran.append(row)  # Thêm hàng vào matran
    for j in range(m):
        if matran[i][j] == -1:
            queue.append((i, j))
while len(queue) > 0:
    u = queue[0]
    queue.pop(0)
    for i in huongdichuyen:
        x= i[0] + u[0]#tính toán vị trị mới tính từ chỗ bị bệnh xem là có thuộc ma trận kh ?
        y= i[1] + u[1]#tính toán vị trị mới tính từ chỗ bị bệnh xem là có thuộc ma trận kh ?
        if x >= 0 and x < n and y >= 0 and y < m:#kiểm tra xem vị trí mới có thuộc ma trận không
            if matran[x][y] != 0:#nếu mà thuộc ma trận và khác 0 thì cộng giá trị vào tổng
                tong += matran[x][y]
                matran[x][y] = 0#đánh dấu đã xét qua,gán bằng 0 để không xét lại
print(tong)