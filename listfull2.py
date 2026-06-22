listPrime = []
for x in range(2,51):
    print("x=============----------------",x)
    checkPrime = True
    for k in range(2,int(x**0.5)+1):
        print("k======",k)
        if x%k==0:
            checkPrime = False
            break
        else:
            checkPrime = True
    if checkPrime :
        # print("x====",x)
        listPrime.append(x)
print(listPrime)
    
# n = int(input("Nhập vào một số: "))
# if n <= 1:
#     print(f"Số {n} không là số nguyên tố")
# elif n == 2:
#     print("2 là số nguyên tố")
# else:
#     checkPrime = True
#     for x in range(2,int(n**0.5)+1):
#             if n%x==0:
#                 checkPrime = False
#                 break
#             else:
#                 checkPrime = True
#     if checkPrime:
#         print("Đây là số nguyên tố") 
#     else:
#         print("Đây không là số nguyên tố")