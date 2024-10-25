"""
urban university – python Junior grade course
implemented by gee3k (c) 2024-2025
"""
from inspect import stack
from os.path import sep


#
def get_matrix( n, m, val ):
    matrix = []
    for row in range( n ):
        c = []
        matrix.append( c )
        for col in range( m ):
            c.append( val )
    return matrix

# program flow
def run_05():
    if __name__ != "__main__":
        print( f"\n=* { __name__ } *=" )

    nm_func = stack()[ 0 ][ 3 ]
    nm_file = str( stack()[ 0 ][ 1 ] ).split( sep )[ -2: ]
    # module 02 run lesson 05
    print( f":: { nm_file[0] }{ sep }{ nm_file[ 1 ] } { sep } func: { nm_func } —",
           "basic operators, data types and program flow" )
    print( "\tThe goal to learn defining function and to call.\n" )

    r1 = get_matrix( 2, 2, 10 )
    r2 = get_matrix( 3, 5, 42 )
    r3 = get_matrix( 4, 2, 13 )
    print( r1 )
    print( r2 )
    print( r3 )

if __name__ == "__main__":
    run_05()