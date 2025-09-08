file = open("score.txt","w")

while True:

    name,kor,eng,math = eval(input("이름,국어,영어,수학 입력:"))

    if name=="":
        break

    file.write(f"{name} {kor:>4d} {eng:>4d} {math:>4d}")



file.close()
