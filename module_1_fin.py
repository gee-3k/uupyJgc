"""
urban university – python Junior grade course
implemented by gee3k (c) 2024-2025
"""

def start():
    if __name__ != "__main__":
        print( f"\n=* {__name__} *=")

    # module 1 final practise
    print( ":: Module 001 ( basic data structs ) - final practise" )
    print( "\tThe goal to write an app, that collects dictionary from given source data.\n" )

    grades = [ [5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5] ]
    students = { 'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron' }
    sorted_studs = sorted( students ) # sorted list
    print( f"Given variables & data :\n\t'grades' type : { type( grades ) }\n\tvalue : { grades } # sorted &",
           f"\n\t'students' type : { type( students ) }\n\tvalue : { students } # unsorted by design" )

    print( "\nAt first let's sure given data elements count are equal at both variables" )
    grade_el_max = len( grades ) # max available elements to process
    if grade_el_max != len( students ):
        print( "! ERROR: count of elements mismatch." )
        return -1

    print( "\nPreparing data 'sorted_studs = sorted( students )' :"+
           f"\n\t'sorted_studs' type : { type( sorted_studs ) }\n\tvalue : { sorted_studs }"
           )

    dict_average_result = dict()
    idx = 0
    print( "\nCalculating average grades of sorted students inside a while loop,\nto store each grades element into dict_average_result.." )
    while idx < grade_el_max:
        # `el` has a grade's statistics list w/ variable count
        grade_el = grades[ idx ]
        # calc average
        average_el = sum( grade_el ) / float( len( grade_el ) )
        # store in dict_result
        dict_average_result.update( { sorted_studs[ idx ]: average_el } )
        # increment idx
        idx += 1

    print( f"\ndict_result :\n\ttype { type( dict_average_result ) }\n\tvalue : { dict_average_result }" )

if __name__ == "__main__":
    start()