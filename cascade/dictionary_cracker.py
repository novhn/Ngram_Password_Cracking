import sys
import os
import math
import hashlib

def usage_error(msg):
    print msg
    print 'usage: python dictionary_cracker.py password_dictionary input_file output_file_cracked output_file_uncracked'
    os._exit(1)


def process_inputs(argv):
    if len(argv) != 4:
        usage_error('Four arguments are required.')
    pwd_dictionary = argv[0]
    input_file = argv[1]
    output_file = argv[2]
    uncracked_hashes = argv[3]
    return pwd_dictionary, input_file, output_file, uncracked_hashes


def dictionary_crack(common_passwords_file, input_file, output_file, uncracked_hashes):
    print "Attempting to perform a dictionary attack"
    passwords_to_crack = []
    cracked_passwords = {}
    common_passwords_dict = {}
    pwd_counter = 0
    cracked_counter = 0

    try:
        print "Opening file of common passwords"
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
                pwd_counter += 1
                hashed_pwd = str(hashed_password).replace('\n','')
                if hashed_pwd in common_passwords_dict:
                    cracked_passwords[hashed_pwd] = common_passwords_dict[hashed_pwd]
                    cracked_counter += 1
                else:
                    passwords_to_crack.append(hashed_pwd)

        print pwd_counter, cracked_counter
        print "cracked " + str(cracked_counter) + " out of " + str(pwd_counter) + " passwords."

        with open(output_file, 'wb') as output_data:
            print "writing cracked passwords to output file"
            for key, value in cracked_passwords.items():
                str_out = str(key) + "," + str(value) + "\n"
                output_data.write(str_out)

        with open(uncracked_hashes, 'wb') as hash_data:
            print "writing cracked passwords to output file"
            for elem in passwords_to_crack:
                str_out = str(elem) + "\n"
                hash_data.write(str_out)

    except IOError:
        print 'Unable to open file. Does it exist? Do you have read permission?'
        os._exit(1)


def main(argv):
    common_passwords, input_file, output_file, uncracked_hashes = process_inputs(argv)  # process command line args
    dictionary_crack(common_passwords, input_file, output_file, uncracked_hashes)  # perform a dictionary attack


if __name__ == "__main__":
    main(sys.argv[1:])
