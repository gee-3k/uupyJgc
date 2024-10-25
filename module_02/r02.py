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

    # refactored to in-loop checking w/ possibly `out of range` at calling inp()
    tl = list()
    for i in range( len( vart ) ):
        inp_data = inp( i+1 )
        if inp_data != -1:
            tl.append( inp_data )
        else:
            print( "ERRor: in range" )

    if tl[ 0 ] == tl[ 1 ] and tl[ 1 ] == tl[ 2 ] and tl[ 2 ] == tl[ 0 ]:
        print( 3 )
    elif tl[ 0 ] == tl[ 1 ] and tl[ 0 ] != tl[ 2 ] \
        or tl[ 0 ] == tl[ 2 ] and tl[ 0 ] != tl[ 1 ] \
        or tl[ 1 ] == tl[ 2 ] and tl[ 1 ] != tl[ 0 ]:
        print( 2 )
    elif tl[ 0 ] != tl[ 1 ] and tl[ 1 ] != tl[ 2 ] and tl[ 2 ] != tl[ 0 ]:
        print( 0 )

"""
    # before refactoring:
    # have to check returned result from inp() for -1 each time
    # to ensure returned data, but not 'out of range' error
    
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
"""

if __name__ == "__main__":
    run_02()