<div align="center">
    <hi>Project 1 - The Scope!</h1>
    <h2>A Python script for finding geolocation and owndership of an IP Addess/list of IP Addresses/CIDR</h2>
</div>

<div>
<p>
<b>Scenario:</b> Congrats, your Penetration testing company Red Planet has landed an external assessment for Microsoft! Your point of contact has give you a few IP addresses for you to test. Like with any test you should always verify the scope given to you to make sure there wasn't a mistake.

<b>Beginner Task:</b> Write a script that will have the user input an IP address. The script should output the ownership and geolocation of the IP. The output should be presented in a way that is clean and organized in order to be added to your report.

<b>Intermediate Task:</b>  Have the script read multiple IP addresses from a text file and process them all at once.

<b>Expert Task:</b> Have the script read from a file containing both single IP addresses and CIDR notation, having it process it both types.

Here are your IP addresses to check:
<br>131.253.12.5
<br>131.91.4.55
<br>192.224.113.15
<br>199.60.28.111

For the Expert Task here are two networks in CIDR notation:
<br>20.128.0.0/16
<br>208.76.44.0/22
</p>

</div>

<h2>Usage</h2>

```

python3 ip_scope.py -h
Usage: ip_scope_.py [-h] ip_addr

Geolocate an IP address

positional arguments:
  ip_addr     Look up a single IP Address (IPv4 or IPv6)

optional arguments:
  -h, --help  show this help message and exit
```

<h2>Example Output</h2>

![](example.png)