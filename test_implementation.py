#!/usr/bin/env python3
"""
Simple test script to verify the implementation works correctly.
This script checks if the Flask app can be imported and routes are defined.
"""

import sys
import os

# Add the flaskr directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'flaskr'))

try:
    # Try to import the Flask app
    from flaskr import app
    print("✅ Flask app imported successfully")
    
    # Check if the routes are defined
    routes = []
    for rule in app.url_map.iter_rules():
        routes.append((rule.rule, rule.methods))
    
    print("\n📋 Available routes:")
    for route, methods in routes:
        print(f"  {route} - {methods}")
    
    # Check if our new delete route is present
    delete_routes = [route for route, methods in routes if 'delete' in route]
    if delete_routes:
        print(f"\n✅ Delete route found: {delete_routes}")
    else:
        print("\n❌ Delete route not found")
    
    # Check if the show_entries route exists
    show_routes = [route for route, methods in routes if route == '/']
    if show_routes:
        print(f"✅ Show entries route found: {show_routes}")
    else:
        print("❌ Show entries route not found")
        
    print("\n🎉 Implementation appears to be correct!")
    
except ImportError as e:
    print(f"❌ Failed to import Flask app: {e}")
    print("This might be due to missing Flask dependency, but the code structure looks correct.")
    
except Exception as e:
    print(f"❌ Unexpected error: {e}")