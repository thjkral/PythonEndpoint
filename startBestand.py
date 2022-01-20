#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 15:18:08 2022

@author: tom
"""


from http.server import HTTPServer, BaseHTTPRequestHandler

class defgh():
    def hoi(self):
        return 'Probeersel'

class abc(BaseHTTPRequestHandler): 
    
    def do_GET(self):
        
        q = defgh()
        
        self.send_response(200)
        self.send_header("content-type", "text/html")
        self.end_headers()
        self.wfile.write(q.hoi().encode())
    

def main(): #Bepaald dat de server de lucht in gaat
    PORT = 8000
    server = HTTPServer(('',PORT), abc)
    print('Server running 8000')
    server.serve_forever()


if __name__ == '__main__': #als main running script is, doe de lucht in
    main()
    
    
    
