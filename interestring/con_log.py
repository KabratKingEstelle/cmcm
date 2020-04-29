import socket,sys,struct
def main():
    with open(sys.argv[1],'rb') as f:
        data_to_send = f.read()

    HOST ='localhost'
    PORT = 9527
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('connecting....')
    s.connect((HOST,PORT))
    print('sending config....')
    s.send(struct.pack('>L'),len(data_to_send))
    s.send(data_to_send)
    s.close()
    print('complete')
if __name__ =='__main__':
    main()