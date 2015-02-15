from read_file_bbk import *

def write_to_file(bbk_final, filename):

        with open(filename,'w') as f:
            for sentence in bbk_final:
                f.write(sentence + '\n')
        f.close()


for i in xrange(0,len(texts)):
    filename = 'bbk' + str(i)
    write_to_file(get_words_bbk(split_text(texts[i])),filename)