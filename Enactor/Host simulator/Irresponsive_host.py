import socket
import argparse

def main(port):
    # Create a TCP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # Allow port reuse to avoid "Address already in use" errors
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        try:
            # Bind to all interfaces on the specified port
            sock.bind(('', port))
            sock.listen(1)
            print(f"Listening on port {port}. Press Ctrl+C to exit...")
            
            # Accept a connection
            conn, addr = sock.accept()
            print(f"Connected to {addr}. No response will be sent.")
            
            # Wait indefinitely (until user presses Enter)
            input("Press Enter to close the connection and exit...")
            
        except KeyboardInterrupt:
            print("\nServer terminated by user.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simulate a hanging server.")
    parser.add_argument("port", type=int, help="Port to listen on (e.g., 8080)")
    args = parser.parse_args()
    
    main(args.port)