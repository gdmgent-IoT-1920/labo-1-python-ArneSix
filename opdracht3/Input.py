# class for validating user input
class InputManager:

    @staticmethod
    def isInt(input_value: str) -> bool:
        if (input_value.isnumeric()):
            return input_value.isnumeric()
        else:
            print("Please enter a valid 4 digit number")
            return False

    @staticmethod
    def isFourDigit(input_value: str) -> bool:
        if (input_value.__len__() == 4):
            return input_value.__len__() == 4
        else:
            print("Oi!! I said a 4 digit number")
            return False