def average_of_prime():
    sum_of_prime = 0
    counter = 0
    num = int(input("Enter range limit: "))
    for numbers in range(2, num):
        for new_numbers in range(2, numbers):
            if numbers % new_numbers == 0:
                break
        else:

            sum_of_prime += numbers
            counter += 1
    print(f"sum_of_prime ={sum_of_prime}")
    average=sum_of_prime/counter
    print(f"number_of_prime_numbers = {counter}\n"f"Average = {average}\n")
average_of_prime()


