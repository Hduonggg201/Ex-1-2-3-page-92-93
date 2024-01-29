import math

def gptb1():

    a = float(input("Nhập hệ số a: "))

    b = float(input("Nhập hệ số b: "))

    if a == 0:

        if b == 0:

            print("Vô số nghiệm")

        else:

            print("Vô nghiệm")

    else:

        print("Phương trình có nghiệm x =", -b / a)

def gptb2():

    # Nhập các hệ số

    a = float(input("Nhập hệ số bậc 2, a = "));

    b = float(input("Nhập hệ số bậc 1, b = "));

    c = float(input("Nhập hằng số tự do, c = "));

    # kiểm tra các hệ số

    if (a == 0):

        if (b == 0):

            print ("Phương trình vô nghiệm!");

    else:

        print ("Phương trình có một nghiệm: x = ", + (-c / b));

    return;

    # tính delta

    delta = b * b - 4 * a * c;

    # tính nghiệm

    if (delta > 0):

        x1 = (float)((-b + math.sqrt(delta)) / (2 * a));

        x2 = (float)((-b - math.sqrt(delta)) / (2 * a));

        print ("Phương trình có 2 nghiệm là: x1 = ", x1, " và x2 = ", x2);

    elif (delta == 0):

        x1 = (-b / (2 * a));

        print("Phương trình có nghiệm kép: x1 = x2 = ", x1);

    else:

        print("Phương trình vô nghiệm!");

#Khai báo hàm Giải pt bậc nhất GPTBN1

#Khai báo hàm Giải pt bậc hai GPTB2

#Tạo bảng chọn việc

while True:

    print("*********************************************")

    print("BẢNG CHỌN VIỆC")

    print("1. Giải phương trình bậc nhất ")

    print("2. Giải phương trình bậc hai ")

    print("3. Thoát khỏi công việc")

    print("*********************************************")

    chon = input("Hãy chọn (1 hay 2 hay 3): ")

    if chon == '1':

        print("Giải phương trình bậc nhất ")

        gptb1()

    elif chon == '2':

        print("Giải phương trình bậc hai")

        gptb2()

    else:

        print("Tạm biệt")

        break

