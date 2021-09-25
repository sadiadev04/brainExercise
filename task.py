def process_amount(amount):
    month = ['January','February','March','April','May','JUne','July','August','September','October','November','December']
    for i in range(12):
        monthly_amount = amount/12
        amount = amount - monthly_amount
        print(f'{month[i]} Payment : {format(monthly_amount,".2f")}')
    return amount
    

amount = int(input("Enter total amount : "))
address = input("Please enter address : ")

data = process_amount(amount)

print(f'Remaining amount after the completion of contract : {format(data, ".2f")} sent to given address {address}')
