import sys

def main():

    name = raw_input( str.decode( 'Iveskite savo vardą:\n', 'utf-8' ) )
    age = raw_input( str.decode( 'Iveskite savo amžių:\n', 'utf-8' ) )

    print( str.decode( "Sveiki " + name + ' jums yra ' + age + ' metų.', 'utf-8' ) )


main()
