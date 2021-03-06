"""
  NaoSay , Nao voicing functions
"""
import time
import sys
import argparse

import naosay

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="127.0.0.1",
                        help="Robot ip address")
    parser.add_argument("--port", type=int, default=9559,
                        help="Robot port number")
    parser.add_argument("--text", type=str,
                        default="../resources/say_intro.txt",
                        help="text file to be said")
    args = parser.parse_args()
    print args
    #naosay.sayTxt(args.ip, args.port,args.text)
    naosay.sayHello(args.ip, args.port)
