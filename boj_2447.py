
def star(N):
    if N == 1:
        star(N//3)
i = 0

while i != 3:
   i = int(input("1.게임시작 2.랭킹보기 3.게임종료 >>> "))
   if i == 1:
       print("게임을 시작합니다")
   elif i == 2:
        print("실시간 랭킹")
   elif i == 3:
        print("게임을 종료합니다.")