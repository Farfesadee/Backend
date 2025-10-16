from http.server import BaseHTTPRequestHandler, HTTPServer
import json
data = [
    {
        "id": 1, "name": "John Doe", "track": "AI Developer"
    }
]
class BasicAPI(BaseHTTPRequestHandler):
    def send_data(self, data, status=200):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

    def do_PUT(self):
        content_size = int(self.headers.get('Content-Length'))
        parsed_data = self.rfile.read(content_size)
        update_data = json.loads(parsed_data)


        # Expecting JSON with an 'id' field to identify the record to update

        record_id = update_data.get("id")
        if record_id is None:
            self.send_data({"Error": "ID is required for update"}, status=400)
            return
        
        # Find and update the record
        for record in data:
            if record["id"] == record_id:
                record.update(update_data)
                self.send_data({
                    "Message": "Data Updated Successfully",
                    "update data": record
                })
                return
            
            # If not found, return an error
        self.send_data({"Error": f"Record with id {record_id} not found"}, status=404)

def run():
    print("Application is running")
    server = HTTPServer(('localhost', 7000), BasicAPI)
    server.serve_forever()

if __name__ == "__main__":
    run()