def ngram_freq(text,n,intersect):
    if not intersect and n > 1:
        step = 2
    else:
        step = 1
    bigram_dict = {}
    text_len = len(text)
    bigram_counter = 0
    for i in range(0,len(text)-(n-1),step):
        if text[i:i+n] not in bigram_dict:
            bigram_dict[text[i:i+n]] = 1
            bigram_counter += 1
        else:
            bigram_dict[text[i:i + n]] += 1
            bigram_counter += 1

    to_sort = [(key,bigram_dict[key]) for key in bigram_dict]
    to_sort.sort(key=lambda x:x[1],reverse=True)
    bigram_dict = {key:value for key,value in to_sort}
    return list(bigram_dict.keys())