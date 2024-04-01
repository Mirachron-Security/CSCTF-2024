#!/usr/bin/python3

#|###############################|#
#| Chronos Security | Marin Radu |#
#| https://chronossec.site       |#
#| https://github.com/ChronosPK  |#
#|###############################|#

import urllib.parse
from http.server import HTTPServer, BaseHTTPRequestHandler
import hashlib
from generate_flag import generate_flag

salt = "Custom Request 2"
port = 9999

with open("requests.log","w") as file:
	file.write(f"Expected command: \n/usr/bin/curl -s http://domain:port/c2VjcmV0?flag=please -H 'CSCTF: dc23933049d8b06808e15916d9cc735bd5c82fc87e5f3a970442f6fc04f5a275'\n\n")

class FlagHandler(BaseHTTPRequestHandler):
	def log_request(self, code='-', size='-'):
		G = "\033[0;32m"
		NO = "\033[0m"
		client_ip = self.client_address[0]
		with open("requests.log", "a") as f:
			f.write(f"AT {G}{self.log_date_time_string()}{NO} FROM {G}{client_ip}{NO}\n")
			f.write(f"{self.requestline}\n\n")
	
	def do_GET(self):
		if self.path == "" or self.path == "/":
			message = open("message.txt","r").read()
			self.send_response(200)
			self.send_header("Content-Type", "text/plain")
			self.end_headers()
			self.wfile.write(message.encode())

		elif self.path == "/c2VjcmV0" or self.path == "/c2VjcmV0/" or "/c2VjcmV0?" in self.path or "/c2VjcmV0/?" in self.path:

			query_string = urllib.parse.urlparse(self.path).query
			params = urllib.parse.parse_qs(query_string)

			# Check the custom header
			if "CSCTF" in self.headers:
				header_value = self.headers["CSCTF"]
				winner_hash = hashlib.sha256((b"text/plain")).hexdigest()
				# print(f"winner_hash: {winner_hash}") # debug
				if header_value == winner_hash:

					# Check the custom query
					if "flag" in params and params["flag"][0] == "please":
						self.send_response(200)
						self.send_header("Content-Type", "text/plain")
						self.end_headers()
						flag = generate_flag(salt)
						self.wfile.write(flag.encode())
						self.wfile.write("\n".encode())

					else: # if query is wrong, display message
						self.send_response(400)
						self.send_header("Content-Type", "text/plain")
						self.end_headers()
						self.wfile.write("Check your query!\n".encode())

				else: # if the value of the header is wrong, display message
					self.send_response(400)
					self.send_header("Content-Type", "text/plain")
					self.end_headers()
					self.wfile.write("Wrong value for custom header".encode())
					self.wfile.write("\n".encode())

			else: # if the header is wrong or doesn't exist, display message
				self.send_response(400)
				self.send_header("Content-Type", "text/plain")
				self.end_headers()
				self.wfile.write("Check your Header.".encode())
				self.wfile.write("\n".encode())
		
		else:
			# If the location is not "/second/flag", send a 404 error
			self.send_response(404)
			self.send_header("Content-Type", "text/plain")
			self.end_headers()
			self.wfile.write("Not found. Are you lost?\n".encode())

try:
	httpd = HTTPServer(("0.0.0.0", port), FlagHandler)
	print(f"Server started on port {port}")
	httpd.serve_forever()
except KeyboardInterrupt:
	httpd.server_close()
