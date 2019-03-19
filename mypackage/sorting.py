def sum_array(array):

    """
    Calculate the sum of a list of arrays

    Args:
        (array): Numbers in a list to be added together

    Returns:
        int: sum of all numbers in a array added together

    Examples:
        >>> sum_array([1,2,3,4,5])
        15
        >> sum_array([1,5,7,3,4])
        20
        >> sum_array([10,10,20,10])
        50
    """


    if len(array)==0:
        return 0
    else:
        return array[0] + sum_array(array[1:])


def fibonacci(n):

    """
    Calculate nth term in fibonacci sequence

    Args:
        n (int): nth term in fibonacci sequence to calculate

    Returns:
        int: nth term of fibonacci sequence,
             equal to sum of previous two terms

    Examples:
        >>> fibonacci(1)
        1
        >> fibonacci(2)
        1
        >> fibonacci(3)
        2
    """

    if n <= 1:
        return n

    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def factorial(n):

    """
    Calculate the factorial of a given number

    Args:
        n (int): the input number

    Returns:
        int: the factorial of a number e.g 5! = 5*4*3*2*1 = 120

    Examples:
        >>> factorial(6)
        720
        >> factorial(4)
        24
    """
    if n < 1:
        return 1
    else:
        fac = n * factorial( n - 1 )
        return fac


def reverse(word):

    """
    Output a string in reverse

    Args:
        word: string that you would input

    Returns: a string in reverse order

    Examples:
        >>> reverse('apple')
        'elppa'
        >> reverse('friend')
        'dneirf'

    """

    if word == "":
        return word
    else:
        return word[-1] + reverse(word[:-1])
