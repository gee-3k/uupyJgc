"""
urban university – python Junior grade course
implemented by gee3k (c) 2024-2025
"""

# vart - variable with text templates
vart = [ [ "first", "1st" ], [ "second", "2nd" ], [ "third", "3rd" ] ]
# input helper with type check
def inp( vart_idx ):
    if vart_idx.is_integer() and vart_idx < 1 or vart_idx >= 4:
        print( "ERRor: index is out of boundary!" )
        return -1
    tmp: str = ""
    res: int = 0
    while not tmp.isnumeric():
        tmp = input( f"pls. enter the '{ vart[ vart_idx-1 ][0] }' integer number:\n{ vart[ vart_idx-1 ][1] } > " )
        if not tmp.isnumeric():
            print( "Pay your attention - you have to enter A NUMBER! pls. try again." )
        else:
            res = int( tmp )
    return res

# program flow if/elif/else
def run_02():
    if __name__ != "__main__":
        print( f"\n=* { __name__ } *=" )

    # module 02 run lesson 02
    print( ":: Module 02 ( basic operators and program flow )" )
    print( "\tThe goal to understand and apply conditional constructions of an application or program flow\n" )

    first = inp( 1 )
    second = inp( 2 )
    third = inp( 3 )

    if first == second and second == third and third == first:
        print( 3 )
    elif first == second and first != third \
        or first == third and first != second \
        or second == third and second != first:
        print( 2 )
    elif first != second and second != third and third != first:
        print( 0 )

if __name__ == "__main__":
    run_02()