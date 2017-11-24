import os

SRC = os.path.dirname(os.path.abspath(__file__))
DOC_PATH = SRC + '/data/'
INPUT_PATH = SRC + '/input/'
OUTPUT_PATH = SRC + '/output/'

TRAINING_DATA_FILE = 'gene-trainF17-new.txt'
TEST_DATA_FILE = 'gene-testF17-untagged.txt'
WORD_TAG_FILE = 'word_tag.txt'
UNIGRAM_TAG_FILE = 'tag_unigram.txt'
BIGRAM_TAG_FILE = 'tag_bigram.txt'
WORD_FILE = 'word_unigram.txt'
