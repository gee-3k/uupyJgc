"""
urban university – python Junior grade course
implemented by gee3k (c) 2024-2025
"""

# program flow if/elif/else
def run_02():
    if __name__ != "__main__":
        print( f"\n=* {__name__} *=")

    # module 02 run lesson 02
    print( ":: Module 02 ( basic operators and program flow )" )
    print( "\tThe goal to understand and apply conditional constructions of an application or program flow\n" )

    #
    first = input( "enter 'first' number:\n1st > " )
    second = input( "enter 'second' number:\n2nd > " )
    third = input( "enter 'third' number:\n3rd > " )

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