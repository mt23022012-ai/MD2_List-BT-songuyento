n = int(input("Nhập vào một số: "))
if n <= 1:
    print(f"Số {n} không là số nguyên tố")
elif n == 2:
    print("2 là số nguyên tố")
else:
    checkPrime = True
    for x in range(2,int(n**0.5)+1):
            if n%x==0:
                checkPrime = False
                break
            else:
                checkPrime = True
    if checkPrime:
        print("Đây là số nguyên tố") 
    else:
        print("Đây không là số nguyên tố")