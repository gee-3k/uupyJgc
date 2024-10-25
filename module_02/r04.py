"""
urban university – python Junior grade course
implemented by gee3k (c) 2024-2025
"""

# program flow
def run_04():
    if __name__ != "__main__":
        print( f"\n=* { __name__ } *=" )

    # module 02 run lesson 04
    print( ":: Module 02 run 04 ( basic operators and program flow )" )
    print( "\tThe goal to consolidate the skills to solving tasks by applying for loop and basic data types.\n" )

    numbers = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 ]
    primes = []
    not_primes = []
    is_prime = False
    ln = len( numbers )
    print( "range :", ln )

    for idx in range( 1, ln ):
        n = numbers[ idx ]
    #    print( "n :", n )
        if n == 2:
            is_prime = True
        elif not n % 2:
            is_prime = False
        else:
            is_prime = True
            for i in range( 2, n - 1 ):
                if n % i == 0:
                    is_prime = False
    #    print( is_prime )
        if is_prime:
            primes.append( n )
        else:
            not_primes.append( n )

    print( "numbers :", numbers )
    print( "primes :", primes )
    print( "not_primes :", not_primes )

if __name__ == "__main__":
    run_04()