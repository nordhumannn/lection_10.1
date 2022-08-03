import abc


class AbcClass(abc.ABC):

    @abc.abstractmethod
    def prime_number(self, number):
        for i in range(2, number):
            if not number % i:
                return False
        return True


class Validator(AbcClass):
    def prime_number(self, number):
        return super().prime_number(number)


x = Validator()
print(x.prime_number(3))
