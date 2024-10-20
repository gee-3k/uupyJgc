"""
urban university – python Junior grade course
implemented by gee3k (c) 2024-2025
"""

def start():
    if __name__ != "__main__":
        print( f"\n=* {__name__} *=")

    # dictionaries and sets
    print( ":: Dictionaries\n" )
    #
    my_dict = { "name-01": 1987, "name-02": 1994, "name-03": 2002 }
    print( f"my_dict : { my_dict }",
           f"\n\tvalue by existing key [ 'name-02' ] : { my_dict[ "name-02" ] }"
           f"\n\tvalue by non-exist key get( 'nm-02' ) : { my_dict.get( "nm-02" ) }"
           )
    my_dict.update( { "name-04": 1965, "name-05": 1971 } )
    print( f"my_dict updated adding new dict pairs",
           f"\n\t{ my_dict }"
           )

    print( f"my_dict deleting pair w/ pop( 'name-03' )",
           f"\n\tdeleted pair's value : { my_dict.pop( 'name-03' ) }"
           )
    print( f"my_dict now : { my_dict }\n\n" )

    # # # # # # #

    print( ":: Sets\n" )
    #
    print( "creating variable with assigned data :\n"+
           "\tmy_set = { 4, 2, 7, 5, 'str', True, 5, 3, 7, 6, 2, 4, 0, 8, 6, 'str', True }"
           )
    my_set = { 4, 2, 7, 5, 'str', True, 5, 3, 7, 6, 2, 4, 0, 8, 6, 'str', True }
    print( "\tcreated 'my_set' looks like :", my_set )
    #
    print( "adding multiple values at once w/ update( [ 9, 11 ] ) " )
    my_set.update( [ 9, 11 ] )
    print( "\tupdated 'my_set' looks like :", my_set )
    #
    print( "deleting element of the set w/ discard( True )" )
    my_set.discard( True )
    print( "\tchanged 'my_set' looks like :", my_set )

if __name__ == "__main__":
    start()