"""
urban university – python Junior grade course
implemented by gee3k (c) 2024-2025
"""

def start():
    if __name__ != "__main__":
        print( f"\n=* {__name__} *=")

    # non-mutable & mutable objects - tuples
    print( "Immutable & Mutable objects - Tuples\n" )
    #
    immutable_var = ([ "idx", 3, 7, 5 ], True, 0.5,
                     ( "item 1", "item 2", "item 3", "item 4", "item 5", "item 6", "item 7" ))
    print( "immutable_var",
           f"\n\tvalue : { immutable_var }",
           f"\n\tvar. type : { type( immutable_var ) }"
           )

    err_explain = """
# ! Attempt to run next code snippet raise the TypeError,
# ! and followed description explains what caused such error
# ! Code snippet causing the error : 'immutable_var[1] = False'
# ! Python's error description:
# immutable_var[1] = False
# ~~~~~~~~~~~~~^^^
# TypeError: 'tuple' object does not support item assignment
"""
    print( err_explain )

    mutable_list = immutable_var[0]
    print( "mutable_list\n( content linked 'mutable_list = immutable_var[0]', see above )",
           f"\n\tvalue : { mutable_list }",
           f"\n\tvar. type : { type( mutable_list ) }",
           )
    mutable_list.append( "modified" )
    print( "mutable_list ( changed appending str )",
           f"\n\tvalue : { mutable_list }",
           f"\n\tvar. type : { type( mutable_list ) }",
           )

    print( "checking mutable tuple content",
           f"\n\tvalue : { immutable_var }",
           f"\n\tvar. type : { type( immutable_var ) }"
           )

if __name__ == "__main__":
    start()