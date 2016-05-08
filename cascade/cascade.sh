VAR1=$1

echo 'dictionary crack'
    python dictionary_cracker.py ../password_lists/top_10000_pwd.txt $1 cracked_by_dictionary.txt uncracked_by_dictionary.txt
echo 'target 50, exists'
    python markov_crack_bfs_cascade.py ../markov_models/hmm_top10000_bi_exist.txt uncracked_by_dictionary.txt 16 cracked_by_50_exists.txt uncracked_by_50_exists.txt 50
echo 'target 100, exists'
    python markov_crack_bfs_cascade.py ../markov_models/hmm_top10000_bi_exist.txt uncracked_by_50_exists.txt 16 cracked_by_100_exists.txt uncracked_by_100_exists.txt 100
echo 'target 500, exists'
    python markov_crack_bfs_cascade.py ../markov_models/hmm_top10000_bi_exist.txt uncracked_by_100_exists.txt 16 cracked_by_500_exists.txt uncracked_by_500_exists.txt 500

