    # target:50
echo 'target 50, exists'
    python markov_crack_bfs.py ./markov_models/hmm_top10000_bi_exist.txt ./password_lists/singles.org_md5.txt 16 ./results/bfs_hmm_top10000_bi_exist_50.txt 50
    python markov_crack_bfs.py ./markov_models/hmm_top10000_tri_exist.txt ./password_lists/singles.org_md5.txt 16 ./results/bfs_hmm_top10000_tri_exist_50.txt 50
    # target: 100
echo 'target 100, exists'
    python markov_crack_bfs.py ./markov_models/hmm_top10000_bi_exist.txt ./password_lists/singles.org_md5.txt 16 ./results/bfs_hmm_top10000_bi_exist_100.txt 100
    python markov_crack_bfs.py ./markov_models/hmm_top10000_tri_exist.txt ./password_lists/singles.org_md5.txt 16 ./results/bfs_hmm_top10000_tri_exist_100.txt 100
    #target: 50
echo 'target 50, all'
    python markov_crack_bfs.py ./markov_models/hmm_top10000_bi_all.txt ./password_lists/singles.org_md5.txt 16 ./results/bfs_hmm_top10000_bi_all_50.txt 50
    python markov_crack_bfs.py ./markov_models/hmm_top10000_tri_all.txt ./password_lists/singles.org_md5.txt 16 ./results/bfs_hmm_top10000_tri_all_50.txt 50
    #target: 100
echo 'target 100, all'
    python markov_crack_bfs.py ./markov_models/hmm_top10000_bi_all.txt ./password_lists/singles.org_md5.txt 16 ./results/bfs_hmm_top10000_bi_all_100.txt 100
    python markov_crack_bfs.py ./markov_models/hmm_top10000_tri_all.txt ./password_lists/singles.org_md5.txt 16 ./results/bfs_hmm_top10000_tri_all_100.txt 100
    # target: 500
echo 'target 500, exists'
    python markov_crack_bfs.py ./markov_models/hmm_top10000_bi_exist.txt ./password_lists/singles.org_md5.txt 16 ./results/bfs_hmm_top10000_bi_exist_500.txt 500
    python markov_crack_bfs.py ./markov_models/hmm_top10000_tri_exist.txt ./password_lists/singles.org_md5.txt 16 ./results/bfs_hmm_top10000_tri_exist_500.txt 500
echo 'target 500, all'
    #target: 500
    python markov_crack_bfs.py ./markov_models/hmm_top10000_bi_all.txt ./password_lists/singles.org_md5.txt 16 ./results/bfs_hmm_top10000_bi_all_500.txt 500
    python markov_crack_bfs.py ./markov_models/hmm_top10000_tri_all.txt ./password_lists/singles.org_md5.txt 16 ./results/bfs_hmm_top10000_tri_all_500.txt 500
