import sys

T = int(sys.stdin.readline())
Test_case = []

for i in range(T):
    Test_case.append(list(map(int, sys.stdin.readline().split())))

for i in range(len(Test_case)):
    H = Test_case[i][0]
    W = Test_case[i][1]
    N = Test_case[i][2]

    spare = N % H
    qt = N // H

    # W 한 자릿수 / H 한 자릿수
    if W < 10 and H < 10:
    # N/H의 나머지가 0일 때
        if spare:
            print(str(spare) + '0' + str(qt + 1))
    # N/H의 나머지가 0이 아닐 때
        else:
            print(str(H) + '0' + str(qt))
    # W 한 자릿수 / H 두 자릿수
    elif W < 10 and H >= 10:
        if spare:
            print(str(spare)+'0'+str(qt+1))
        else:
            print(str(H)+'0'+str(qt))


    # W 두 자릿수 / H 한 자릿수
    elif W >= 10 and H < 10:
        if spare and qt >= 9:
            print(str(spare)+str(qt+1))
        elif spare and qt < 9:
            print(str(spare)+'0'+str(qt+1))
        elif not spare and qt > 9:
            print(str(H)+str(qt))
        elif not spare and qt <= 9:
            print(str(H)+'0'+str(qt))


    # W 두 자릿수 / H 두 자릿수
    elif W >= 10 and H >= 10:
        if spare >= 10 and qt >= 9:
            print(str(spare)+str(qt+1))
        elif spare >= 10 and qt < 9:
            print(str(spare)+'0'+str(qt+1))
        elif 0 < spare < 10 and qt >= 9:
            print(str(spare)+str(qt+1))
        elif 0 < spare < 10 and qt < 9:
            print(str(spare)+'0'+str(qt+1))
        elif not spare and qt >= 10 :
            print(str(H)+str(qt))
        elif not spare and qt < 10:
            print(str(H)+'0'+str(qt))





















    # # XX0Y인 case
    # if W < 10 and N % H == 0:
    #     print(str(H) + '0' + str(int(N / H)))
    # elif W < 10 and N % H != 0:
    #     print(str(N % H) + '0' + str((N // H) + 1))
    # elif W >= 10 and (N / H) < 10 and (N % H) == 0:
    #     print(str(H) + '0' + str(int(N / H)))
    # elif W >= 10 and (N / H) < 10 and (N % H) != 0:
    #     print(str(N % H) + '0' + str((N // H) + 1))
    #
    # # XXYY인 case
    # elif W >= 10 and (N / H) >= 10 and (N % H) != 0:
    #     print(str(N % H) + str((N // H) + 1))
    # elif W >= 10 and (N / H) >= 10 and (N % H) == 0:
    #     print(str(H) + str(int(N / H)))
