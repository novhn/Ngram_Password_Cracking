import sys
import os
import math


def usage_error(msg):
    print msg
    print 'usage: python ngram_freq_analyzer.py ngram_length input_file output_file all-flag'
    os._exit(1)


def process_inputs(argv):
    if len(argv) != 3:
        usage_error('Three arguments are required.')
    try:
        ngram_size = int(argv[0])
    except:
        usage_error("first param must be integer between 1-3")
    if ngram_size > 3 or ngram_size < 1:
        usage_error("first param must be integer between 1-3")
    input_file = argv[1]
    output_file = argv[2]
    all_flag = False
    if argv[3]:
        all_flag = True
    return ngram_size, input_file, output_file, all_flag


def generate_ngram_dict(ngram_size, input_file, output_file, all_flag):
    print "Initializing variables"
    line_count = 0
    char_count = 0
    first_chars = {}
    ngram_dict = {}
    if ngram_size == 1:
        for x in xrange(32, 128):
            first_chars[x] = 0
            ngram_dict[x] = 0
    if ngram_size == 2:
        for x in xrange(32, 128):
            first_chars[x] = 0
        for x in xrange(32, 128):
            for y in xrange(32, 128):
                ngram_dict[(x, y)] = 0
    if ngram_size == 3:
        for x in xrange(32, 128):
            for y in xrange(32, 128):
                first_chars[(x, y)] = 0
        for x in xrange(32, 128):
            for y in xrange(32, 128):
                for z in xrange(32, 128):
                    ngram_dict[(x, y, z)] = 0

    try:
        print "Opening input file"
        with open(input_file, 'rb') as input_data:
            print "Generating frequency map of leading characters and ngrams"
            for line in input_data:
                line = line.strip()
                multiplier = 1
                is_invalid = 0

                parts = line.split()
                if len(parts) > 1:
                    multiplier = int(parts[0])
                    line = parts[1]

                line_count += 1 * multiplier
                if len(line) > ngram_size - 1:
                    char_count += (len(line) - ngram_size + 1) * multiplier

                for char in line:
                    if ord(char) > 128 or ord(char) < 32:
                        is_invalid = 1

                if is_invalid:
                    continue

                if ngram_size == 3:
                    key = (ord(line[0]), ord(line[1]))
                else:
                    key = ord(line[0])
                first_chars[key] += 1

                i = len(line) - ngram_size
                for x in xrange(0, i+1):
                    unigram = ord(line[x])
                    if ngram_size == 3:
                        bigram = ord(line[x + 1])
                        trigram = ord(line[x + 2])
                        key = (unigram, bigram, trigram)
                    if ngram_size == 2:
                        bigram = ord(line[x + 1])
                        key = (unigram, bigram)
                    if ngram_size == 1:
                        key = unigram
                    ngram_dict[key] += 1 * multiplier


            for key in first_chars:
                if first_chars[key] != 0:
                    first_chars[key] = -10 * math.log(1.00 * first_chars[key] / line_count)
                else:
                    first_chars[key] = 1000

            for key in ngram_dict:
                if ngram_dict[key] != 0:
                    ngram_dict[key] = -10 * math.log(1.00 * ngram_dict[key] / char_count)
                else:
                    if all_flag:
                        ngram_dict[key] = 1000

        print "Opening output file"
        with open(output_file, 'wb') as output_data:
            print "outputting lead char probabilities"
            for key, value in first_chars.items():
                out_key = ''
                if isinstance(key, tuple):
                    for item in key:
                        out_key += str(item) + ','
                else:
                    out_key = key
                str_out = "1:"+str((int(value))).zfill(4) + "=" + str(out_key) + "\n"
                output_data.write(str_out)
            print "outputting ngram probabilities"
            for key, value in ngram_dict.items():
                out_key = ''
                if isinstance(key, tuple):
                    for item in key:
                        out_key += str(item) + ','
                else:
                    out_key = key
                str_out = "2:"+str((int(value))).zfill(4) + "=" + str(out_key) + "\n"
                output_data.write(str_out)
        with open(output_file, 'rb') as output_data:
            print "sorting lines"
            lines = output_data.readlines()
            lines.sort()
            print "lines sorted"
        with open(output_file, 'wb') as output_data:
            for line in lines:
                output_data.write(line)

    except IOError:
        print 'Unable to open file. Does it exist? Do you have read permission?'
        os._exit(1)


def main(argv):
    ngram_size, input_file, output_file, all_flag = process_inputs(argv)  # process command line args
    generate_ngram_dict(ngram_size, input_file, output_file, all_flag)  # generate ngram dictionary with counts


if __name__ == "__main__":
    main(sys.argv[1:])
