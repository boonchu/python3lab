import argparse

def main():
    ''' Example of taking inputs for megazord bin'''
    parser = argparse.ArgumentParser(prog='my_megazord_program')
    parser.add_argument('-i', nargs='?', help='help for -i blah')
    parser.add_argument('-d', nargs='?', help='help for -d blah')
    parser.add_argument('-v', nargs='?', help='help for -v blah')
    parser.add_argument('-w', nargs='?', help='help for -w blah')

    args = parser.parse_args()

    collected_inputs = {'i': args.i,
                    'd': args.d,
                    'v': args.v,
                    'w': args.w}
    print 'got input: ', collected_inputs 

if __name__ == "__main__":
    main()
