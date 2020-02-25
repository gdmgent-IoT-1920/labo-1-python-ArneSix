def reverse_str(input_str: str):
    split_str = input_str.split(' ')
    split_str.reverse()
    joined_str = ' '.join(split_str)

    return joined_str

user_input = input("Enter a sentence ")
to_print_str = reverse_str(user_input)

print(to_print_str)