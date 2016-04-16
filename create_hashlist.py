"""
This program is just to create a list of MD5 hashed passwords.

It can be used to generate any list of hashes, either a list of hashes of the most common passwords, or
a list of hashes to crack.

"""

import sys
import os
import math
import hashlib

def usage_error(msg):
    print msg
    print 'usage: python create_hashlist.py input_file output_file'
    os._exit(1)


def process_inputs(argv):
    if len(argv) != 2:
        usage_error('Two arguments are required.')
    input_file = argv[0]
    output_file = argv[1]
    return input_file, output_file


def hash_inputs(input_file, output_file):
    print "hashing the inputs"
    passwords_to_hash = []

    try:
        print "Opening file of passwords to hash"
        with open(input_file, 'rb') as input_data:
            print "Generating list of passwords to crack"
            for password in input_data:
                passwords_to_hash.append(str(password).replace('\n', ''))

        print passwords_to_hash

        print "Opening output file"
        with open(output_file, 'wb') as output_data:
            print "writing hashed passwords to output file"
            for pwd in passwords_to_hash:
                pwd_hash = hashlib.md5(pwd).hexdigest()
                str_out = str(pwd_hash) + "\n"
                output_data.write(str_out)

    except IOError:
        print 'Unable to open file. Does it exist? Do you have read permission?'
        os._exit(1)


def main(argv):
    input_file, output_file = process_inputs(argv)  # process command line args
    hash_inputs(input_file, output_file)  # hash the inputs


if __name__ == "__main__":
    main(sys.argv[1:])
