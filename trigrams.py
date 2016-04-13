import sys
import os
import math


def usage_error(msg):
    print msg
    print 'usage: python ngram_freq_analyzer.py ngram_length slide_length input_file output_file'
    os._exit(1)


def process_inputs(argv):
    if len(argv) != 2:
        usage_error('Two arguments are required.')
    input_file = argv[0]
    output_file = argv[1]
    return input_file, output_file


def generate_ngram_dict(input_file, output_file):
    line_count = 0
    char_count = 0
    first_chars = {}
    trigram_dict = {}
    for x in xrange(0, 128):
        for y in xrange(0, 128):
            first_chars[(x, y)] = 0
    for x in xrange(0, 128):
        for y in xrange(0, 128):
            for z in xrange(0, 128):
                trigram_dict[(x, y, z)] = 0

    print "Generating ngram frequency dictionary"
    try:
        with open(input_file, 'rb') as input_data:
            for line in input_data:
                line_count += 1
                if len(line) > 2:
                    char_count += len(line) - 2
                key = (ord(line[0]), ord(line[1]))
                first_chars[key] += 1

                i = len(line) - 3
                for x in xrange(0, i):
                    bigram1 = ord(line[x])
                    bigram2 = ord(line[x + 1])
                    trigram = ord(line[x + 2])
                    key = (bigram1, bigram2, trigram)
                    trigram_dict[key] += 1
            for key in first_chars:
                if first_chars[key] != 0:
                    first_chars[key] = -10 * math.log(1.00 * first_chars[key] / line_count)
                else:
                    first_chars[key] = 1000

            for key in trigram_dict:
                if trigram_dict[key] != 0:
                    trigram_dict[key] = -10 * math.log(1.00 * trigram_dict[key] / char_count)
                    print key, trigram_dict[key]
                else:
                    trigram_dict[key] = 1000

        with open(output_file, 'wb') as output_data:
            print "outputting bigram leads"
            for key, value in trigram_dict.items():
                out_key = str(key[0])+','+str(key[1])
                str_out = str((int(value))) + "=" + str(out_key) + "\n"
                output_data.write(str_out)
            print "outputting trigram probabilities"
            for key, value in trigram_dict.items():
                out_key = str(key[0])+','+str(key[1])+','+str(key[2])
                str_out = str((int(value))) + "=" + str(out_key) + "\n"
                output_data.write(str_out)

    except IOError:
        print 'Unable to open input file. Does it exist? Do you have read permission?'
        os._exit(1)


def main(argv):
    input_file, output_file = process_inputs(argv)  # process command line args
    generate_ngram_dict(input_file, output_file)  # generate ngram dictionary with counts


if __name__ == "__main__":
    main(sys.argv[1:])
