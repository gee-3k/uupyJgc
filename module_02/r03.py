"""
urban university – python Junior grade course
implemented by gee3k (c) 2024-2025
"""

# program flow while loop
def run_03():
    if __name__ != "__main__":
        print( f"\n=* {__name__} *=")

    # module 02 run lesson 03
    print( ":: Module 02 run 03 ( basic operators and program flow )" )
    print( "\tThe goal to understand and apply while loop and its break/continue\n" )

    my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

    list_len = len( my_list )
    idx = 0
    while idx < list_len:
        if my_list[idx] == 0:
            idx += 1
            continue
        if my_list[idx] < 0:
            break
        print( f"found positive : { my_list[idx]  }")
        idx += 1

if __name__ == "__main__":
    run_03()