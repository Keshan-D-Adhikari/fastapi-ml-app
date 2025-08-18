#!/usr/bin/env python3
"""
Start the FastAPI server
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.main import app

if __name__ == "__main__":
    print("Starting FastAPI server...")
    print("Visit http://localhost:8000/docs for API documentation")
    try:
        import uvicorn
        uvicorn.run(app, host="0.0.0.0", port=8000)
    except ImportError:
        print("uvicorn not installed. Starting with basic server...")
        import http.server
        import socketserver
        from urllib.parse import parse_qs
        
        PORT = 8000
        
        class APIHandler(http.server.SimpleHTTPRequestHandler):
            def do_GET(self):
                if self.path == '/':
                    self.send_response(200)
                    self.send_header('Content-type', 'application/json')
                    self.end_headers()
                    self.wfile.write(b'{"message": "Iris API is running", "docs": "Visit /docs for API documentation"}')
                else:
                    self.send_response(404)
                    self.end_headers()
        
        with socketserver.TCPServer(("", PORT), APIHandler) as httpd:
            print(f"Server running at http://localhost:{PORT}")
            httpd.serve_forever()
