import sys
import os
import time
import hashlib
import copy

def usage_error(msg):
    print msg
    print 'usage: python markov_crack.py markov_model_file password_input_file pwd_length output_file'
    os._exit(1)


def process_inputs(argv):
    if len(argv) != 4:
        usage_error('Four arguments are required.')
    markov_file = argv[0]
    password_file = argv[1]
    password_length = argv[2]
    output_file = argv[3]
    return markov_file, password_file, password_length, output_file

def check_for_hash(password_chars, hashed_passwords, output_file):
    password = ''
    for num in password_chars:
        password+=(chr(int(num)))
    new_hash = hashlib.md5(password).hexdigest()
    sys.stdout.write('%s\r' % password)
    sys.stdout.flush()
    while new_hash in hashed_passwords:
        print "password found:" + password + "," + new_hash
	with open(output_file,'ab') as output_data:
	    output_data.write(password+'::::'+new_hash+'\n')
	hashed_passwords.remove(new_hash)


def markov_crack(markov_file, password_file, password_length, output_file):
    with open(password_file, 'rb') as password_data:
        hashed_pwd = []
        for line in password_data:
            hashed_pwd.append(line.strip())

    with open(markov_file, 'rb') as markov_data:
        # initialize leading characters list
        leading_chars = []
        for line in markov_data:
            if line[0] == "2":
                break
            leading_chars.append((line.split("=")[1].rstrip(",").rstrip()).split(","))
        # init probable ngrams list
        ngrams = []
        for line in markov_data:
            if line[0] == "1":
                pass
            ngrams.append((line.split("=")[1].rstrip().rstrip(",")).split(","))
        # init loop variables
        ngram_len = len(leading_chars[0])

        # markov loop
        print "entering markov loop"
        start = time.time()

        #step 1: we loop through a number of times equal to the length - r
        for i in range(ngram_len, int(password_length)+1):
            for chars in leading_chars:
                stack = [(chars, 0)]
                check_for_hash(chars, hashed_pwd, output_file)
                while len(stack) > 0:
                    # get current password to construct
                    curr = stack.pop()
                    curr_pass = curr[0]
                    curr_index = curr[1]
                    if curr_index == len(ngrams):
                        continue  # if we've reached end of prob_ngrams list, continue
                    if len(curr_pass) >= i:
                        continue  # if curr password is max length, continue
                    for x in xrange(curr_index, len(ngrams)):
                        # look for matching ngram
                        if curr_pass[-ngram_len:] == ngrams[x][:ngram_len]:
                            # add old password with new index to stack
                            stack.append((curr_pass, x + 1))
                            new_curr = copy.deepcopy(curr_pass)
                            new_curr.extend(ngrams[x][-1:])
                            # add new password to stack
                            stack.append((new_curr, 0))
                            # try cracking password, if it works, terminate loop
                            check_for_hash(new_curr, hashed_pwd, output_file)
                            if len(hashed_pwd) == 0:
                                end = time.time()
                                print end-start
                                return 0
                            break


def main(argv):
    markov_file, password_file, password_length, output_file = process_inputs(argv)
    markov_crack(markov_file, password_file, password_length, output_file)
if __name__ == "__main__":
    main(sys.argv[1:])
