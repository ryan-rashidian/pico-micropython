import tkinter as tk
import socket

server_ip = 'IP'
server_port = 12345

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def power_on():
    sock.sendto(b'ON', (server_ip, server_port))

def power_off():
    sock.sendto(b'OFF', (server_ip, server_port))

root = tk.Tk()
root.title('Motion Sensor')
label = tk.Label(
    root,
    text='Motion Sensor Controller',
    fg='white',
    bg='blue',
    font=('Arial', 18, 'bold')
)
label.pack(fill="x")

button1 = tk.Button(
    root,
    text="ON",
    font=('Arial', 36),
    command=power_on
)
button1.pack(expand=1, fill='both', side='left')
button2 = tk.Button(
    root,
    text="OFF",
    font=('Arial', 36),
    command=power_off
)
button2.pack(expand=1, fill='both', side='right')

if __name__ == '__main__':
    root.mainloop()

