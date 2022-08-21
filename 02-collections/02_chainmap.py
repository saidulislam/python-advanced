import argparse
import os

from collections import ChainMap

def main():
    app_defaults = {'username':'admin', 'password':'admin'}
    
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--username')
    parser.add_argument('-p', '--password')
    args = parser.parse_args()
    
    # vars function is basically a dictionary maker
    command_line_arguments = {key:value for key, value 
                              in vars(args).items() if value}
    
    # chain = ChainMap(command_line_arguments, os.environ, 
    #                  app_defaults)
    chain = ChainMap(command_line_arguments, app_defaults)
    
    print(chain['username'])

if __name__ == '__main__':
    # it will use either the default value or the user provided in arg
    main()
