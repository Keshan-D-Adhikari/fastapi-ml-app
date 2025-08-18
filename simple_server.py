import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Simple test to see if imports work
try:
    from app.main import app
    print("SUCCESS: FastAPI app imported successfully")
except Exception as e:
    print(f"ERROR: Import error: {e}")
    sys.exit(1)

# Test model loading
try:
    import pickle
    with open('models/iris_classifier.pkl', 'rb') as f:
        model = pickle.load(f)
    print("SUCCESS: Model loaded successfully")
except Exception as e:
    print(f"ERROR: Model loading error: {e}")

# Start server
print("STARTING: Server on http://127.0.0.1:8000")
print("DOCS: Visit http://127.0.0.1:8000/docs for API documentation")

if __name__ == "__main__":
    try:
        import uvicorn
        uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")
    except ImportError:
        print("ERROR: uvicorn not available, using basic server")
        import http.server
        import socketserver
        from urllib.parse import urlparse, parse_qs
        import json
        
        class APIHandler(http.server.SimpleHTTPRequestHandler):
            def do_GET(self):
                if self.path == '/':
                    self.send_response(200)
                    self.send_header('Content-type', 'application/json')
                    self.send_header('Access-Control-Allow-Origin', '*')
                    self.end_headers()
                    response = {"message": "Iris Classification API", "status": "running", "docs": "/docs"}
                    self.wfile.write(json.dumps(response).encode())
                elif self.path == '/health':
                    self.send_response(200)
                    self.send_header('Content-type', 'application/json')
                    self.send_header('Access-Control-Allow-Origin', '*')
                    self.end_headers()
                    response = {"status": "healthy", "model_loaded": True}
                    self.wfile.write(json.dumps(response).encode())
                else:
                    self.send_response(404)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    self.wfile.write(b"<h1>404 - Not Found</h1><p>Try <a href='/'>homepage</a> or <a href='/health'>health check</a></p>")
        
        PORT = 8000
        with socketserver.TCPServer(("127.0.0.1", PORT), APIHandler) as httpd:
            print(f"RUNNING: Basic server at http://127.0.0.1:{PORT}")
            print("Press Ctrl+C to stop")
            try:
                httpd.serve_forever()
            except KeyboardInterrupt:
                print("SERVER STOPPED")
