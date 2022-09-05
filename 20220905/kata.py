def fizzbuzz(num):
    """
    fizzbuzzを返す関数
    numが3の倍数 -> Fizz
    numが5の倍数 -> Buzz
    numが15の倍数 -> FizzBuzz
    その他 -> 引数num
    """
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    if num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    return str(num)