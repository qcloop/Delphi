import time

out_dir = 'smb_delphi'
eval_interval = 500
eval_iters = 100
log_interval = 100
always_save_checkpoint = False

wandb_log = False
wandb_project = 'delphi_smb'
wandb_run_name = 'smb_' + str(time.time())

dataset = 'smb'

vocab_size = 78

ignore_tokens = [0, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77]

# Model size (Delphi-2M-like)
n_layer = 12
n_head = 12
n_embd = 120
dropout = 0.1

# Optimizer / LR schedule
learning_rate = 3e-4
max_iters = 200_000
lr_decay_iters = 200_000
min_lr = 3e-5
warmup_iters = 5_000
weight_decay = 2e-1
beta2 = 0.99

# Delphi time-to-event stability + regularization
t_min = 0.1
token_dropout = 0.0

# Recommended for SMB (prevents same-timestamp leakage)
mask_ties = True

# Kept for compatibility with Delphi scripts
no_event_token_rate = 5
