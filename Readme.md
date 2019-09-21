The issue:
Internet stops working on windows machines with certain intel/broadcom WiFi chips after the newest windows 10 update
It is not easy to figure this problem out just by looking at the WiFi signal bar at the bottom right of taskbar as it shows
full network connectivity, even though pages wont load and downloads (if any) will stop

The fix:
I have noticed that

turning WiFi on and off on my laptop
Or
disconnecting and reconnecting to the WiFi network
Or
rebooting the WiFi router fixes the issue, atleast for a little while, until the problem occurs again and fix needs to be re-applied

However, I might not always be available on the system to perform these temporary fixes, for instance-during overnight downloads
Hence this python script



The python file wifi_reset.py checks whether internet is working 
(by pinging Google.com in this case, change as you see fit)
and resets wifi on your PC if its not. 
This fixes the weird internet connectivity 
issue 
The python code requires elevated (admin) rights, hence the easiest solution 
would be to run it through a batch (.bat) file (also provided)


