#!/usr/bin/python3

#|###############################|#
#| Chronos Security | Marin Radu |#
#| https://chronossec.site       |#
#| https://github.com/ChronosPK  |#
#|###############################|#

import urllib.parse
from http.server import HTTPServer, BaseHTTPRequestHandler
import platform
from generate_flag import generate_flag

salt = "Custom Request 1"
port = 9999

with open("requests.log","w") as file:
	file.write(f"Expected command: \ncurl http://domain:port/flag?python={platform.python_version()}\n\n")

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

		elif self.path == "/flag" or "/flag?" in self.path or "/flag/?" in self.path:
			query_string = urllib.parse.urlparse(self.path).query
			params = urllib.parse.parse_qs(query_string)
			if "python" in params and params["python"][0] == platform.python_version():
				self.send_response(200)
				self.send_header("Content-Type", "text/plain")
				self.end_headers()
				flag = generate_flag(salt)
				self.wfile.write(flag.encode())
				self.wfile.write("\n".encode())

			else:
				# Wrong query
				self.send_response(400)
				self.send_header("Content-Type", "text/plain")
				self.end_headers()
				self.wfile.write("Wrong query!\n".encode())
		else:
			# Wrong location
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
