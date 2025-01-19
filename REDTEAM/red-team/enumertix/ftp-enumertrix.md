---
description: The File Transfer Protocol Service is being Enumerated.
---

# FTP Enumertrix

## File Transfer Protocol

> Its most commonly used for file transfer in various devices on Client to Server based.&#x20;
>
> Where its used standard Port 21.



### Network Mapper

> NMAP

```
nmap -sV -n -Pn -p 21 -sS -sC ftp*.nse  #TARGETIP
```



### FTP Anonymous Login

> in FTP there is an feature where any login is allowed which is called ANONYMOUS LOGIN.

#### NSE FTP SCIRPT DIVE

```
--- Connects to the FTP server and checks if the server allows anonymous logins.
action = function(host, port)
  local max_list = stdnse.get_script_args("ftp-anon.maxlist")
  if not max_list then
    if nmap.verbosity() == 0 then
      max_list = 20
    else
      max_list = nil
    end
  else
    max_list = tonumber(max_list)
    if max_list < 0 then
      max_list = nil
    end
  end
  local socket, code, message, buffer = ftp.connect(host, port, {request_timeout=8000})
  if not socket then
    stdnse.debug1("Couldn't connect: %s", code or message)
    return nil
  end
  if code and code ~= 220 then
    stdnse.debug1("banner code %d %q.", code, message)
    return nil
  end
  local status, code, message = ftp.auth(socket, buffer, "anonymous", "IEUser@")  # It uses this Username and password it this work then it 
  if not status then                                                                                                                 # print the result as seems .
    if not code then
      stdnse.debug1("got socket error %q.", message)
    elseif code == 421 or code == 530 then
      -- Don't log known error codes.
      -- 421: Service not available, closing control connection.
      -- 530: Not logged in.
    else
      stdnse.debug1("got code %d %q.", code, message)
      return ("got code %d %q."):format(code, message)
    end
    return nil
  end

```

> Direclty WEB Access using any file manager on Any OS.

<figure><img src="../../.gitbook/assets/image (17).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (18).png" alt=""><figcaption></figcaption></figure>

### BruteForce FTP

#### Hydra

```
hydra -l "anonymous" -p "anonymous" ftp://TARGETIP
hydra -L username.txt -P "password.txt" ftp://TARGET_IP
```

