solution = lambda numbers, count=0: solution(
    numbers.replace(
        ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"][count], 
        str(count)), 
    count+1) if count<10 else int(numbers)