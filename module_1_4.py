"""
urban university – python Junior grade course
implemented by gee3k (c) 2024-2025
"""

def start():
    if __name__ != "__main__":
        print( f"\n=* {__name__} *=")

    # app organize & Str class methods
    print( "App organize & Str class methods\n" )
    #
    my_string = input( "please, type some/any text here and press an [enter] key when you've done\n>" )
    scnt = my_string.count('')-1
    print( f"You've just entered { scnt } chars long text",
           f"\n\tmy_string .upper case : { my_string.upper() }",
           f"\n\tmy_string .lower case : { my_string.lower() }",
           f"\n\tmy_string .replace (del spaces): { my_string.replace( ' ', '' ) }",
           f"\n\tmy_string 1st char : { my_string[0] }",
           f"\n\tmy_string last char : { my_string[-1] }",
           )

if __name__ == "__main__":
    start()