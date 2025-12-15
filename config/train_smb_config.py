# config/smb.py
# Delphi-compatible configuration for SMB event modeling

import time

# --------------------
# Logging & output
# --------------------

out_dir = 'SMB_Delphi'
eval_interval = 500
eval_iters = 100
log_interval = 100

always_save_checkpoint = False

wandb_log = False
wandb_project = 'delphi_smb'
wandb_run_name = 'smb_' + str(time.time())

# --------------------
# Dataset
# --------------------

dataset = 'smb'

# Vocabulary
vocab_size = 78

# Ignore input-only tokens (sector, size, form, region) + PAD
ignore_tokens = [
    # Sector
    58, 59, 60, 61, 62, 63, 64, 65, 66,
    # Size
    67, 68, 69,
    # Legal form
    70, 71, 72, 73,
    # Region
    74, 75, 76,
    # PAD
    77,
]

# --------------------
# Model size
# --------------------

n_layer = 12
n_head = 12
n_embd = 120
dropout = 0.1

# --------------------
# Optimization
# --------------------

learning_rate = 3e-4
max_iters = 200_000
lr_decay_iters = 200_000
min_lr = 3e-5

beta2 = 0.99
weight_decay = 2e-1
warmup_iters = 5_000

# --------------------
# Time-to-event specifics (CRITICAL)
# --------------------

# Minimum allowed time gap (prevents numerical instability)
t_min = 0.1

# Matches Delphi “no-event” logic
# ~1 no-event token every 5 time units (years in paper; here handled by data)
no_event_token_rate = 5

# Regularization
token_dropout = 0.0

# --------------------
# Reproducibility
# --------------------

seed = 42