
"""IP addess scope verification

This script allows the user to enter a public IP Address to verify ownership
and geolocation of the address.

This tool accepts only a single IP address (xxx.xxx.xxx.xxx)

This script requires that 'ipwhois' be installed within the Python 
environment you are running this script in.

This file can also be importate as a module and contains the following functions:

        *main(ip_address) - the main function of the script
        *get_ip_info(ip_address) - returns a data as a list about the ip address through 'IPWhois'
        *print_results(ip_address, ownership, country, state, city, postal_code) - 
            displays results of a successful ip request from get_ip_info

ip_scope_file_read script is meant to be used with this script for multiple single
ip addresses read in from a file
"""

#!/usr/bin/env python3
import sys
from ipwhois import IPWhois

def main(ip_address):

    try:
        ownership, country, state, city, postal_code = get_ip_info(ip_address)
    except:
        sys.exit("You entered an invalid or non public IP address")
    else:
        print_results(ip_address, ownership, country, state, city, postal_code)
    
    #ip_info = get_ip_info(ip_address)
    #print_results(ip_address, ip_info[0], ip_info[1], ip_info[2], ip_info[3], ip_info[4])

def get_ip_info(ip_address):
    """Gets ownership and geolocation data from ip_address

    Parameters
    ----------
    ip_address : str
        a single ip address (xxx.xxx.xxx.xxx)

    Returns
    -------
    list
        a list of strings containing the requested data:
            ownership, country, state, city, postal_code
    """
    obj = IPWhois(ip_address)
    results = obj.lookup_whois()
    
    return results['nets'][0]['description'], results['asn_country_code'], results['nets'][0]['state'], results['nets'][0]['city'], results['nets'][0]['postal_code']

    # ownership = results['nets'][0]['description']
    # country = results['asn_country_code']
    # state = results['nets'][0]['state']
    # city = results['nets'][0]['city']
    # postal_code = results['nets'][0]['postal_code']

    # return ownership, country, state, city, postal_code


def print_results(ip_address, ownership, country, state, city, postal_code):
    print(f'''
    IP address: {ip_address}
    Ownership: {ownership}

    Geolocation data:
        Country:  {country}
        State:    {state}
        City:     {city}
        Zip Code: {postal_code}
    ''')


if __name__ == '__main__':
    num_args = len(sys.argv)
    if num_args == 2:
        main(sys.argv[1])
    elif num_args == 1:
        sys.exit("Failed to provide IP address as argument")
    else:
        sys.exit("Too many arguments")
        