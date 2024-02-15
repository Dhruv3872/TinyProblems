# Problem-12: Write a program to Find prime and non-prime numbers in the array:
import math  # For using sqrt & ceil.


def find_prime_non_prime(input_array: list):
    # We are not checking for uniqueness of the array, but we will use sets to store prime
    # and non-prime numbers to avoid duplication in the output.
    output: dict[str, set] = {'prime': set(), 'non-prime': set()}
    primes: list = [2, 3]  # Initialised a list of prime numbers
    max_non_prime: int = 4  # Maximum non-prime evaluated so far. Initialised with the first non-prime.
    knowledge: dict = {'int': input_array[0], 'prime_list': primes, 'max_non_prime': max_non_prime}
    for x in input_array:
        knowledge['int'] = x
        output_knowledge = check_prime(knowledge)
        knowledge['prime_list'] = output_knowledge['prime_list']
        knowledge['max_non_prime'] = output_knowledge['max_non_prime']
        if output_knowledge['is_prime']:
            output['prime'].add(x)
        else:
            output['non-prime'].add(x)
    return output


def check_prime(input_knowledge: dict):
    input_int: int = input_knowledge['int']
    prime_list: list = input_knowledge['prime_list']
    max_non_prime: int = input_knowledge['max_non_prime']
    is_prime: bool | None = None  # Two types so that we can initialise it
    # with None value, and then evaluate whether it is prime or not within
    # the function, and then assign that bool to this variable.
    output: dict = {'is_prime': is_prime, 'prime_list': prime_list, 'max_non_prime': max_non_prime}
    # print(input_int in prime_list)
    if input_int in prime_list:
        # print(input)
        is_prime = True
        # print(is_prime)
    # No need to append it to the list as it's already in there.
    elif input_int == max_non_prime:
        is_prime = False
    elif type(math.sqrt(input_int)) == int:
        is_prime = False
        if input_int == max_non_prime + 1:
            max_non_prime = input_int
            input_knowledge['max_non_prime'] = max_non_prime
        else:
            for prime in prime_list:
                if input_int == prime + 1:
                    max_non_prime = input_int
                    input_knowledge['max_non_prime'] = max_non_prime
                    break
    elif math.ceil(math.sqrt(input_int)) <= max_non_prime:
        for prime in prime_list:
            remainder: int = input_int % prime
            if remainder == 0:
                is_prime = False
                if input_int == max_non_prime + 1:
                    max_non_prime = input_int
                    input_knowledge['max_non_prime'] = max_non_prime
                else:
                    for prime_int in prime_list:
                        if input_int == prime_int + 1:
                            max_non_prime = input_int
                            input_knowledge['max_non_prime'] = max_non_prime
                            break
                break
        if is_prime is None:  # If it is still None, that means that the
            # entire for loop completed without changing its value. Hence, it
            # is indeed a prime integer.
            is_prime = True
            prime_list.append(input_int)
            input_knowledge['prime_list'] = prime_list
    else:
        for x in range(max_non_prime + 1, math.ceil(math.sqrt(input_int)) + 1):
            input_knowledge['int'] = x
            output = check_prime(input_knowledge)
            input_knowledge['prime_list'] = output['prime_list']
            input_knowledge['max_non_prime'] = output['max_non_prime']
        input_knowledge['int'] = input_int  # Rewrite the value of input_int into
        # the input_knowledge.
        output = check_prime(input_knowledge)  # Run this function one last time to find
        # if the originally given integer is prime or not.
        is_prime = output['is_prime']
        prime_list = output['prime_list']
        input_knowledge['prime_list'] = output['prime_list']
        max_non_prime = output['max_non_prime']
        input_knowledge['max_non_prime'] = output['max_non_prime']

        max_non_prime = output['max_non_prime']
    output['is_prime'] = is_prime
    output['prime_list'] = input_knowledge['prime_list']
    output['max_non_prime'] = input_knowledge['max_non_prime']
    return output


print(find_prime_non_prime([2, 1143, 53, 71, 85, 96, 23, 462, 78, 153]))
