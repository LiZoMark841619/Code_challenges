def fib_finder(n, fib_list):
  fib_list.extend(fib_list[i] + fib_list[i+1] for i in range(n-2))
  return fib_list

if __name__ == '__main__':
    num = int(input('Please enter the length of the requested Fibonacci list:'))
    fib_list = [int(input(f'Please enter the number at index {i}:')) for i in range(2)]
    str1, str2 = 'The Fibonacci list from', 'numbers if the counter is'
    print(f'{str1} {fib_list[0]} including {num} number is below: {fib_finder(num, fib_list)}')