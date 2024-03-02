import threading
from multiprocessing import Pool
import socket


class myscan:
    # можно понизить число для роста скорости или повысить для гарантии работы с большим пингом
    socket.setdefaulttimeout(0.25)
    print_lock = threading.Lock()
    def __init__(self, t_IP, startPort, endPort):
        self.t_IP = t_IP
        self.startPort = startPort
        self.endPort = endPort

    def portscan(self, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            con = s.connect((self.t_IP, port))
            with self.print_lock:
                print(port, 'is open')
            con.close()
        except:
            pass

    def sum_square_with_mp(self, num):
        p = Pool()
        p.map(self.portscan, num)

    def mainScan(self):
        numbers = range(self.startPort, self.endPort)
        self.sum_square_with_mp(numbers)

