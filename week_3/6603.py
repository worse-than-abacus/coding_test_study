while True:
    x,*arr = map(int,input().split())
    if x == 0: break
    num=x+1
    for a in range(1,num):                                      # 1번째 리스트 1번부터
        for b in range(a+1,num):                                # 2번째 리스트 2번부터
            for c in range(b+1,num):                            # 3번째 리스트 3번부터
                for d in range(c+1,num):                        # 4번째 리스트 4번부터
                    for e in range(d+1,num):                    # 5번째 리스트 5번부터
                        for f in range(e+1,num):                # 6번째 리스트 6번부터
                            print(f'{arr[a-1]} {arr[b-1]} {arr[c-1]} {arr[d-1]} {arr[e-1]} {arr[f-1]}')
    print()