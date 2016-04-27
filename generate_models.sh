python ngram_freq_analyzer.py 2 ./password_lists/top_10000_pwd.txt ./markov_models/hmm_top10000_bi_exist.txt existing
python ngram_freq_analyzer.py 3 ./password_lists/top_10000_pwd.txt ./markov_models/hmm_top10000_tri_exist.txt existing
python ngram_freq_analyzer.py 2 ./password_lists/top_10000_pwd.txt ./markov_models/hmm_top10000_bi_all.txt all
python ngram_freq_analyzer.py 3 ./password_lists/top_10000_pwd.txt ./markov_models/hmm_top10000_tri_all.txt all

