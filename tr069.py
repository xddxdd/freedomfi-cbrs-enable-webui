from http.server import SimpleHTTPRequestHandler, HTTPServer


xml_data = """
<?xml version='1.0' encoding='UTF-8'?>
<soap11env:Envelope xmlns:soap11enc="http://schemas.xmlsoap.org/soap/encoding/"
    xmlns:soap11env="http://schemas.xmlsoap.org/soap/envelope/"
    xmlns:cwmp="urn:dslforum-org:cwmp-1-0"
    xmlns:xsd="http://www.w3.org/2001/XMLSchema">
    <soap11env:Header>
        <cwmp:ID soap11env:mustUnderstand="1">null</cwmp:ID>
    </soap11env:Header>
    <soap11env:Body>
        <cwmp:SetParameterValues>
            <ParameterList>
                <ParameterValueStruct>
                    <Name xsi:type="xsd:string">Device.X_000E8F_DeviceFeature.X_000E8F_WebServerEnable</Name>
                    <Value xsi:type="xsd:boolean">1</Value>
                </ParameterValueStruct>
            </ParameterList>
            <ParameterKey xsi:type="xsd:string">SetPValues1234</ParameterKey>
        </cwmp:SetParameterValues>
    </soap11env:Body>
</soap11env:Envelope>
"""


class HTTPRequestHandler(SimpleHTTPRequestHandler):
    """This handler uses server.base_path instead of always using os.getcwd()"""

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/xml")
        self.end_headers()
        self.wfile.write(xml_data.strip().encode("utf-8"))

    def do_POST(self):
        content_len = int(self.headers.get("Content-Length", 0))
        post_body = self.rfile.read(content_len).decode("utf-8")
        print(post_body)

        self.send_response(200)
        self.send_header("Content-type", "text/xml")
        self.end_headers()

        if "cwmp:SetParameterValuesResponse" in post_body or "cwmp:Fault" in post_body:
            return
        self.wfile.write(xml_data.strip().encode("utf-8"))


httpd = HTTPServer(("", 8443), HTTPRequestHandler)
httpd.serve_forever()
