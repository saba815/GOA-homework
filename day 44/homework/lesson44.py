def hello_world():
    print("Hello, world!")

# ფუნქციის გამოძახება
hello_world()

def greet(name):
    print(f"Hello, {name}!")

# მაგალითი გამოყენების
greet("საბუნა")

def sum_two_numbers(a, b):
    return a + b

# გამოყენების მაგალითი
result = sum_two_numbers(5, 7)
print(result)  # დააბეჭდებს: 12

def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# გამოყენების მაგალითი
print(even_or_odd(10))  # გამოიტანს: Even
print(even_or_odd(7))   # გამოიტანს: Odd


def average(numbers):
    if not numbers:
        return 0  # თუ სიაში ელემენტები არ არის, აბრუნებს 0
    return sum(numbers) / len(numbers)

# გამოყენების მაგალითი
nums = [2, 4, 6, 8, 10]
print(average(nums))  # გამოიტანს: 6.0

def string_length(s):
    return len(s)

# გამოყენების მაგალითი
print(string_length("გამარჯობა"))  # გამოიტანს: 8

def reverse_list(lst):
    return lst[::-1]

# გამოყენების მაგალითი
numbers = [1, 2, 3, 4, 5]
print(reverse_list(numbers))  # გამოიტანს: [5, 4, 3, 2, 1]

def to_uppercase(s):
    return s.upper()

# გამოყენების მაგალითი
print(to_uppercase("გამარჯობა"))  # გამოიტანს: გამარჯობა -> გამარჯობა (დიდი ასოები ქართულად არ ცვალება, მაგრამ ინგლისურად იქნება)
print(to_uppercase("hello world"))  # გამოიტანს: HELLO WORLD

def max_of_two(a, b):
    if a > b:
        return a
    else:
        return b

# ან უფრო მოკლე ფორმით:
# def max_of_two(a, b):
#     return a if a > b else b

# გამოყენების მაგალითი
print(max_of_two(10, 20))  # გამოიტანს: 20
print(max_of_two(30, 15))  # გამოიტანს: 30

def is_negative(number):
    return number < 0

# გამოყენების მაგალითი
print(is_negative(-5))  # გამოიტანს: True
print(is_negative(0))   # გამოიტანს: False
print(is_negative(10))  # გამოიტანს: False

def longest_word(words):
    if not words:
        return None  # თუ სიაში სიტყვები არაა, აბრუნებს None
    
    longest = words[0]
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest

# გამოყენების მაგალითი
words_list = ["თბილისი", "გიორგი", "ქუჩა", "მოსწავლე"]
print(longest_word(words_list))  # გამოიტანს: მოსწავლე
