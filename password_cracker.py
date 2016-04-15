import sys
import os
import math
import hashlib

def usage_error(msg):
    print msg
    print 'usage: python password_cracker.py ngram_length password_dictionary input_file output_file'
    os._exit(1)


def process_inputs(argv):
    if len(argv) != 4:
        usage_error('Four arguments are required.')
    try:
        ngram_size = int(argv[0])
    except:
        usage_error("first param must be integer between 1-3")
    if ngram_size > 3 or ngram_size < 1:
        usage_error("first param must be integer between 1-3")
    pwd_dictionary = argv[1]
    input_file = argv[2]
    output_file = argv[3]
    return ngram_size, pwd_dictionary, input_file, output_file


def dictionary_crack(common_passwords, input_file, output_file):
    print "Attempting to read password dictionary"
    passwords_to_crack = []
    cracked_passwords = {}

    try:
        print "Opening file of passwords to crack"
        with open(input_file, 'rb') as input_data:
            print "Generating list of passwords to crack"
            for hashed_password in input_data:
                passwords_to_crack.append(str(hashed_password).replace('\n',''))

        print passwords_to_crack

        print "Opening output file"
        with open(common_passwords, 'rb') as password_data:
            print "checking common passwords against the password list"
            for password in password_data:
                pwd_hash = hashlib.md5(str(password).replace('\n','')).hexdigest()
                if pwd_hash in passwords_to_crack:
                    passwords_to_crack.remove(pwd_hash)
                    cracked_passwords[pwd_hash] = password

        with open(output_file, 'wb') as output_data:
            print "writing cracked passwords to output file"
            for key, value in cracked_passwords.items():
                str_out = str(key) + "," + str(value)
                output_data.write(str_out)

    except IOError:
        print 'Unable to open file. Does it exist? Do you have read permission?'
        os._exit(1)


def main(argv):
    ngram_size, common_passwords, input_file, output_file = process_inputs(argv)  # process command line args
    dictionary_crack(common_passwords, input_file, output_file)  # perform a dictionary attack


if __name__ == "__main__":
    main(sys.argv[1:])
