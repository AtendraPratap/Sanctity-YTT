
	import urllib # Python URL functions

        import urllib2 # Python URL functions

        user = "username" # Your authentication key.

        key = "API Key" # Your authentication key.

        mobile = "XXXXXXXXXX" # Multiple mobiles numbers separated by comma.

        message = "Test message" # Your message to send.

        senderid = "XXXXXX" # Sender ID,While using route4 sender id should be 6 characters long.

        accusage = "default" # Define route

        # Prepare you post parameters

        values = {

                    'user' : user,

                    'password' : key,

                    'mobiles' : mobile,

                    'message' : message,

                    'senderid' : senderid,               

                    'accusage' : accusage

                    }

        url = "https://domain/sendsms.jsp?" # API URL

        postdata = urllib.urlencode(values) # URL encoding the data here.

        req = urllib2.Request(url, postdata)

        response = urllib2.urlopen(req)

        output = response.read() # Get Response

        print output # Print Response