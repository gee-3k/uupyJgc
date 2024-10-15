"""
urban university – python Junior grade course
implemented by gee3k (c) 2024-2025
"""

def start():
    if __name__ != "__main__":
        print( f"\n=* {__name__} *=")

    # variables
    print( "Strings & Indexes" )
    #
    example = "Some String"
    print( f"\ngiven string : '{ example }'",
           f"\n\t1st char str[0]: '{ example[0] }'",
           f"\n\tlast char str[-1]: '{example[-1]}'",
           f"\n\t2nd half part w/ odd amount of chars str[-5:]: '{example[-5:]}'",
           f"\n\treverse str[::-1]: '{example[::-1]}'",
           f"\n\tevery 2nd char str[::2]: '{example[::2]}'",
           )

if __name__ == "__main__":
    start()