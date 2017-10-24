import subprocess
import argparse
import sys

parser = argparse.ArgumentParser(description='''
ACS Programming Challenge |
Author: Mahdi Davari |
Last updated: August, 2017''')


parser.add_argument('-f', metavar='files', type=str, nargs=1,
                    help='Input file for files, e.g. -f files.txt. Required')
parser.add_argument('-n', metavar='nodes', type=str, nargs=1,
                    help='Input file for nodes, e.g. -n nodes.txt. Required')

args = parser.parse_args()
if args.f and args.n:
    file_key = args.f[0]
    file_extract = args.n[0]
else:
    sys.stderr.write('You should provide input files for file_name and node_names, i.e., -f and -n. For more information, use -h')
    sys.exit(1)



def msg(file_key,file_extract):
    a = 0
    with open(file_key) as file:
        for lines in file:
            lines = lines.split()
            a=int(lines[2])+int(lines[3])+int(7.0)
            keyword = 'EA'+str(lines[0])
            subprocess.call(["/usr/bin/grep","-A",str(a), str(keyword),file_extract])
            return TRUE

msg('extended_convex_hull', 'GPa')
