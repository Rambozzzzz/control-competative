n = int(input("How many employee IDs? "))
ids = list(map(int, input("Enter the IDs: ").split()))

if len(ids) != n:
    print("Error.")
else:
    evens = [str(i) for i in ids if i % 2 == 0]
    if evens:
        for e in evens:
            print(e, end=' ')
        print()
    else:
        print(-1)
