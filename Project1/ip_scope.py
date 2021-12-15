"""IP addess scope verification

This script allows the user to enter a public IP Address to verify ownership
and geolocation of the address.

This tool accepts only a single IP address (xxx.xxx.xxx.xxx)

This file can also be imported as a module and contains the following functions:

        *main(ip_address) - the main function of the script
        *get_ip_info(ip_address) - returns requested data as a dictionary about the ip address through 'IPWhois' api
        *print_results() - 
            displays results of a successful ip request from get_ip_info

ip_scope_file_read script is meant to be used with this script for multiple single
ip addresses read in from a file
"""

#!/usr/bin/env python3
import sys, traceback
import requests
import json
import ipaddress

def main(ip):
    #IP conversion and check
    geo_data = get_ip_info(ip)
    print_results(geo_data)

def validate_ip_address(address):
    """Takes in a value and checks for valid ipaddress type

    Parameters
    ----------
    address : str or int
        accepts a single ip address as a base 2 int or a str in IPv4/6, binary (packet), and IPv4/6 CIDR format
        
    Returns
    -------
    IP object
       Will return an object of type ipaddress.IPv(4/6)Address or ipaddress.IPv(4/6)Network or ValueError
    """
    try:
        ip = ipaddress.ip_address(address)
        print(f"IP address {address} is a valid {type(ip)} address")
        return ip 
    except:
        print(f"IP address {address} is not a valid IPv4 or IPv6 address.")
    
    try:
        ip = ipaddress.ip_network(address)
        print(f"IP address {address} is a valid {type(ip)} address")
        return ip
    except:
        print(f"IP address {address} is not a valid IPv4Network or IPv6Network CIDR address.")

    # If address is neither type function will return ValueError but not raise the exception so that the program can output invalid address
    return ValueError(f"ValueError '{address}' does not appear to be an IPv4 or IPv6 address or network")

# def check_ip_for_public(ip):
#     return "Private" if (ipaddress.ip_address(ip).is_private) else "Public"
   
def get_ip_info(ipv4):
    """Gets ownership and geolocation data from ip_address

    Parameters
    ----------
    ip_address : str
        a single ip address (xxx.xxx.xxx.xxx)

    Returns
    -------
    Dictionary
        a dictionary of strings containing the requested data from the geo_data_keys list:
            ip, ownership(org), continent, continent_code, country, country_code, region, city, timezone
    """
    
    #geo_data_keys is a list of data to return from json object, add/remove keys as needed
    geo_data_keys = ['ip','org','continent','continent_code','country','country_code','region','city','timezone'] 

    try:
        address = "http://ipwhois.app/json/" + ipv4
        r = requests.get(address)
        data = json.loads(r.text)
        
        # Checking json success value
        if data['success']:
            
            #### Uncomment if you want the entire json object ####
            # return data
            #### Uncomment if you want to print out json object ####
            # print(json.dumps(data, indent=4, sort_keys=True))

            return {key:data[key] for key in geo_data_keys if key in data}
        else:
            print(f"Request failed with {ipv4}")
            print(f"Message: {data['message']}")

            # sys.exit()

    except requests.exceptions.HTTPError as e:
        print("An HTTP Error occured: ", e)
    except requests.exceptions.ConnectionError as e:
        print("An Error Connecting to IPWHOIS occured: ", e)
    except requests.exceptions.Timeout as e:
        print("Timeout Error: ", e)
    except requests.exceptions.TooManyRedirects as e:
        print("Too many redirects: ", e)
    except requests.exceptions.RequestException as e:
        print(e)
    except Exception:
        #For any other unexpected error
        str = traceback.format_exc()
        print(str)

def print_results(geo_dict):
    """Prints ownership and geolocation data requested

    Parameters
    ----------
    geo_dict : dictionary
        a dictionary with key value pairs of geolocation/ownership data

    Returns
    -------
    NULL
        prints data as requested under the geo_data_keys list
            ip, ownership(org), continent, continent_code, country, country_code, region, city, timezone
    """

    print(f'''
    IP address: {geo_dict['ip']}
    Ownership:  {geo_dict['org']}

    Geolocation data:
        Continent:    {geo_dict['continent']} ({geo_dict['continent_code']})
        Country:      {geo_dict['country']} ({geo_dict['country_code']})
        State/Region: {geo_dict['region']}
        City:         {geo_dict['city']}
        Timezone:     {geo_dict['timezone']}
    ''')


if __name__ == '__main__':
    num_args = len(sys.argv)
    if num_args == 2:
        main(sys.argv[1])
    elif num_args == 1:
        sys.exit("Failed to provide IP address as argument")
    else:
        sys.exit("Too many arguments")
        
