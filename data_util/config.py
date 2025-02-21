
import os

root_dir = os.path.expanduser("~")

train_data_path = "/home/lpc/PycharmProjects/split_encoder_pointer_summarizer-master/data/merge/ht_in_citation/masking/abstract2triple/chunked/train_*"
eval_data_path = "/home/lpc/PycharmProjects/split_encoder_pointer_summarizer-master/data/merge/ht_in_citation/masking/abstract2triple/val.bin"
decode_data_path = "/home/lpc/PycharmProjects/split_encoder_pointer_summarizer-master/data/merge/ht_in_citation/masking/abstract2triple/test.bin"
vocab_path = "/home/lpc/PycharmProjects/split_encoder_pointer_summarizer-master/data/merge/ht_in_citation/masking/abstract2triple/vocab"
log_root = "/home/lpc/PycharmProjects/split_encoder_pointer_summarizer-master/log/merge/ht_in_citation/masking/abstract2triple"


# Hyperparameters
hidden_dim= 256
emb_dim= 128
batch_size= 32
max_enc_steps=400
max_dec_steps=100
beam_size=4
min_dec_steps=35
vocab_size=50000

lr=0.001
adagrad_init_acc=0.1
rand_unif_init_mag=0.02
trunc_norm_init_std=1e-4
max_grad_norm=2.0

pointer_gen = True
is_coverage = False
cov_loss_wt = 1.0

eps = 1e-12
max_iterations = 10000

use_gpu=True

lr_coverage=0.15
