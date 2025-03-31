# Enable Web UI on FreedomFi Indoor CBRS Radio

This script implements a minimal TR-069 remote management server to enable Web UI on the FreedomFi Indoor CBRS Radio (Sercomm SCE4255W).

## Usage

1. Install Python 3 on your local computer.
2. Start script with `python3 tr069.py`
3. Update the DNS settings of your router, so that it can hijack `acs.freedomfi.com` to the IP address of your computer.
4. Turn on the FreedomFi Indoor CBRS Radio, and plug it into your LAN.
5. Once the radio starts connecting to remote management, you should see the script start printing some XML messages. These are the messages sent by the radio.

```bash
<soap-env:Envelope xmlns:soap-env="http://schemas.xmlsoap.org/soap/envelope/" xmlns:soap-enc="http://schemas.xmlsoap.org/soap/encoding/" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:cwmp="urn:dslforum-org:cwmp-1-0">
  <soap-env:Header>
    <cwmp:ID soap-env:mustUnderstand="1">null</cwmp:ID>
  </soap-env:Header>
  <soap-env:Body>
    <cwmp:SetParameterValuesResponse>
      <Status xsi:type="xsd:int">0</Status>
    </cwmp:SetParameterValuesResponse>
  </soap-env:Body>
</soap-env:Envelope>

192.168.0.209 - - [30/Mar/2025 17:15:50] "POST / HTTP/1.1" 200 -
```

If you do not see any requests, make sure you set up the DNS hijacking correctly. Try visiting `http://acs.freedomfi.com:8443` with your browser, and it should show an XML response.

6. Once you see `cwmp:SetParameterValuesResponse` in the response, the Web UI should be enabled.
7. Log in to the Web UI at the radio's IP address. The web UI is on port 443 with HTTPS enabled. E.g. `https://192.168.1.123/`
8. The default username and password are `sc_femto` and `tsFid2wz` ([source](https://discord.com/channels/404106811252408320/836735476659912754/1355330850232995861)).
9. Stop the script and remove the DNS hijacking, so that the radio doesn't try to connect to remote management infinitely.
