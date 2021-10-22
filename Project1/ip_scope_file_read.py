
"""IP addess scope verification add-on 

This script reads in IP addresses from a file and uses the ip_scope script
to request ownership and geolocation data. 

This tool accepts a single text (.txt) files. 
(Support for comma separated files planned for future releases)

This script requires that 'ipwhois' be installed within the Python 
environment you are running this script in as the script ip_scope
requires it.

This file can also be imported as a module and contains the following functions:

        *main(ip_address) - the main function of the script
"""

#!/usr/bin/env python3

import sys, traceback
from os import strerror
import ip_scope

def main(file_name):
    
    try:
        file = open(file_name, 'r')
        IPs = file.readlines()
    
        for IP in IPs:
            ip_scope.main(IP.rstrip()) #strip the newline character from each ip

        file.close()
    except IOError as e:
        print("I/O error occurred: ", strerror(e.errno))
    except Exception:
        #For any other unexpected error
        str = traceback.format_exc()
        print(str)
       
if __name__ == '__main__':
    num_args = len(sys.argv)
    if num_args == 2:
        main(sys.argv[1])
    elif num_args == 1:
        sys.exit("Failed to provide file name as argument")
    else:
        sys.exit("Too many arguments")
