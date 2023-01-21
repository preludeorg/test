# What is my IP address?

> Modeled after Operator TTP #4d2c97ed-5464-4a27-9cc4-f76237526aea

After compromising a device adversaries often programmatically look up the public IP address. This information provides details about the physical location of the device, including it's specific longitude/lattitude.

Example output: 
```
{
  "ip": "210.79.76.134",
  "hostname": "pool-210.79.76.134.washdc.fios.verizon.net",
  "city": "Rockville",
  "region": "Maryland",
  "country": "US",
  "loc": "32.9876,-71.1234",
  "org": "AS701 Comcast Business",
  "postal": "34510",
  "timezone": "America/New_York",
  "readme": "https://ipinfo.io/missingauth"
}   
```

While looking up this information from a browser may be normal, looking it up programmatically should be flagged as suspicious.

## How

This test uses a free service hosted at http://ipinfo.io which displays the IP information of the caller. It exits successfully if the lookup is allowed to complete.