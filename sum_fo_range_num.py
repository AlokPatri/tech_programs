while True:
    try:
        while True:
            try:
                start_range=int(input("initial point\n"))
                break
            except ValueError:
                print("please enter valid start point!")
        while True:
            try:
                end_range=int(input("end point\n"))
                break
            except ValueError:
                print("please enter valid end point!")
        # caculating the sum of number of given range
        sum=0
        for i in range(start_range,end_range+1):
            sum+=i
        print(f"the sum of numbers in given range {start_range}-{end_range}is ", sum)
        break
    except ValueError:
        print("invalid input! please enter a valid range")
