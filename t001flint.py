"""
urban university – python Junior grade course
implemented by gee3k (c) 2024-2025
"""

def start():
    if __name__ != "__main__":
        print( f"\n=* {__name__} *=")

    # 1st program
    print( "1st program :", 9 ** 0.5 * 5 )

    # 2nd program
    print( "2nd program :", 9.99 > 9.98 and 1000 != 1001 )

    # 3rd program
    npr = 2 * 2 + 2
    wpr = 2 * ( 2 + 2 )
    print( "3rd program :", npr == wpr,
           f"\n\t  no priority : { npr }",
           f"\n\twith priority : { wpr }"
           )

    # 4th program
    s = '123.456'
    print( "4th program :",
           f"\n\tby str.split : { s.split('.')[1][0] }",
           f"\n\tby tech.spec.: { int( float(s) * 10 % 123 ) }"
           )
