import tkinter as tk
import socket

server_ip = 'IP'
server_port = 12345

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def servo_left():
    sock.sendto(b'LEFT', (server_ip, server_port))

def servo_right():
    sock.sendto(b'RIGHT', (server_ip, server_port))

root = tk.Tk()
root.title('Servo Controller')
label = tk.Label(
    root,
    text='Servo Controller',
    fg='white',
    bg='blue',
    font=('Arial', 18, 'bold')
)
label.pack(fill="x")

button1 = tk.Button(
    root,
    text="Move Left",
    font=('Arial', 36),
    command=servo_left
)
button1.pack(expand=1, fill='both', side='left')
button2 = tk.Button(
    root,
    text="Move Right",
    font=('Arial', 36),
    command=servo_right
)
button2.pack(expand=1, fill='both', side='right')

if __name__ == '__main__':
    root.mainloop()

