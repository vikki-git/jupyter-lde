import IPython as IPython
from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument("-p",
                    "--password", 
                     dest="password",
                     help="Password for authentication.",
                     required=True)
    
args = parser.parse_args()

hash = IPython.lib.passwd(args.password)

print("ACCESS_TOKEN=" + hash)
