import socket
import threading
from datetime import datetime

def print_with_timestamp(message):
    timestamp = datetime.now().strftime("%y%m%d %H:%M:%S.%f:")[:-3]
    print(f"\n[{timestamp}] {message}")

def handle_client(client_socket, server_ip, server_port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server_socket.connect((server_ip, server_port))
        print_with_timestamp(f'Relay connected to remote host: {server_ip}:{server_port}')
    except socket.timeout:
        print_with_timestamp(f'Timeout occurred. Check your network connection. {server_ip}:{server_port}')
        # Additional error handling or cleanup code specific to timeout    

    def forward(src, dst):
        try:
            src_address = src.getpeername()
            dst_address = dst.getpeername()

            while True:
                data = src.recv(1024)
                if not data:
                    break
                # print(data)
                # decoded_data = data.decode(errors='ignore')
                # printable_data = ''.join(c for c in decoded_data if c.isprintable())
                # print(f"Received from {src_name}: {printable_data}")
                # print(printable_data)
                # print(f"From: "src {src_address[0]}:{src_address[1]}")
                # print(f"From: {src} To: {dst}")
                print_with_timestamp(f"From: {src_address[0]}:{src_address[1]} To: {dst_address[0]}:{dst_address[1]}")
                hex_data = ''.join(hex(c)[2:].zfill(2).upper() for c in data)
                spaced_hex_data = ' '.join(hex_data[i:i+2] for i in range(0, len(hex_data), 2))
                print(spaced_hex_data)
                dst.sendall(data)

        except ConnectionResetError:
            timestamp = datetime.now().strftime("%y%m%d %H:%M:%S.%f:")[:-3]
            print_with_timestamp("Client disconnected.")
            # Additional code for handling client disconnection
        except OSError:
            timestamp = datetime.now().strftime("%y%m%d %H:%M:%S.%f:")[:-3]
            print_with_timestamp("Bad file descriptor")
        except Exception as e:
            timestamp = datetime.now().strftime("%y%m%d %H:%M:%S.%f:")[:-3]
            print_with_timestamp(f"An error occurred: {str(e)}")

        finally:
            # Close the connection to the local host
            client_socket.close()

            # Print when disconnecting from the local host
            print_with_timestamp(f'Relay disconnected from local host: {server_ip}:{server_port}')

            # Close the connection to the remote host
            server_socket.close()
            
            # Print when disconnecting from the remote host
            print_with_timestamp(f'Relay disconnected from remote host: {server_ip}:{server_port}')
    
    threading.Thread(target=forward, args=(client_socket, server_socket)).start()
    threading.Thread(target=forward, args=(server_socket, client_socket)).start()

def tcp_relay(relay_ip, relay_port, server_ip, server_port):
    relay_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    relay_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    relay_socket.bind((relay_ip, relay_port))
    relay_socket.listen(1)
    print_with_timestamp(f"Relay listening on {relay_ip}:{relay_port}")

    while True:
        client_socket, client_address = relay_socket.accept()
        print_with_timestamp(f"Client connected: {client_address[0]}:{client_address[1]}")
        threading.Thread(target=handle_client, args=(client_socket, server_ip, server_port)).start()

# USUAL PED
# tcp_relay('192.168.101.173', 8001, '192.168.101.205', 16107)
# tcp_relay('192.168.101.173', 8001, '192.168.101.170', 16107)
# tcp_relay('192.168.101.173', 8001, '192.168.132.2', 16107)
# tcp_relay('192.168.137.1', 8001, '192.168.132.2', 16107)
# VAS
# tcp_relay('192.168.101.173', 8001, '192.168.102.98', 16108)
# The Works PED
tcp_relay('192.168.101.173', 8001, '192.168.102.43', 16107)
