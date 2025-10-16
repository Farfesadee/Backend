from http.server import BaseHTTPRequestHandler, HTTPServer
import json
data = [
    {
        "name": "John Doe",
        "track": "AI Developer"
    }
]
class BasicAPI(BaseHTTPRequestHandler):
    def send_data(self, data, status=200):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

    def do_DELETE(self):
        content_size = int(self.headers.get('Content-Length'))
        parsed_data = self.rfile.read(content_size)
        delete_data = json.loads(parsed_data)

        global data
        data = [item for item in data if item != delete_data]

        self.send_data({
            "Message": "Data Deleted",
            "data": delete_data
        })

def run():
        HTTPServer(('localhost', 4000), BasicAPI).serve_forever()
print("Application is running")
run()