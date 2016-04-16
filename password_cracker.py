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


def dictionary_crack(common_passwords_file, input_file, output_file):
    print "Attempting to perform a dictionary attack"
    passwords_to_crack = []
    cracked_passwords = {}
    common_passwords_dict = {}

    try:
        print "Opening file of hashed common passwords"
        with open(common_passwords_file, 'rb') as password_data:
            print "Generating dictionary of common hashed passwords"
            for password in password_data:
                pwd = str(password).replace('\n','')
                pwd_hash = hashlib.md5(pwd).hexdigest()
                common_passwords_dict[pwd_hash] = pwd

        print "Opening file of passwords to crack"
        with open(input_file, 'rb') as input_data:
            print "Generating list of passwords to crack"
            for hashed_password in input_data:
                hashed_pwd = str(hashed_password).replace('\n','')
                if hashed_pwd in common_passwords_dict:
                    cracked_passwords[hashed_pwd] = common_passwords_dict[hashed_pwd]
                else:
                    passwords_to_crack.append(hashed_pwd)

        print passwords_to_crack, cracked_passwords

        with open(output_file, 'wb') as output_data:
            print "writing cracked passwords to output file"
            for key, value in cracked_passwords.items():
                str_out = str(key) + "," + str(value) + "\n"
                output_data.write(str_out)

    except IOError:
        print 'Unable to open file. Does it exist? Do you have read permission?'
        os._exit(1)


def main(argv):
    ngram_size, common_passwords, input_file, output_file = process_inputs(argv)  # process command line args
    dictionary_crack(common_passwords, input_file, output_file)  # perform a dictionary attack


if __name__ == "__main__":
    main(sys.argv[1:])
