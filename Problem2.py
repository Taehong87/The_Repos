def fib_list(start_val, max_val):
    fib_list = []
    while True:
        if not fib_list:
            fib_list.append(start_val)
            fib_list.append(start_val * 2)
        else:
            new_val = fib_list[-2] + fib_list[-1]
            if new_val > max_val:
                break
            else:
                fib_list.append(new_val)
    return fib_list

def even_sums(num_list):
    even_sum = 0
    for num in num_list:
        if num % 2 == 0:
            even_sum += num
    return even_sum

print even_sums(fib_list(1, 4000000))
    