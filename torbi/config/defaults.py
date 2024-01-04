###############################################################################
# Metadata
###############################################################################


# Configuration name
CONFIG = 'torbi'


###############################################################################
# Decoding
###############################################################################





###############################################################################
# Directories
###############################################################################


# Root location for saving outputs
ROOT_DIR = Path(__file__).parent.parent.parent

# Location of preprocessed features
CACHE_DIR = ROOT_DIR / 'data' / 'cache'

# Location of datasets on disk
DATA_DIR = ROOT_DIR / 'data' / 'datasets'

# Location to save evaluation artifacts
EVAL_DIR = ROOT_DIR / 'eval'


###############################################################################
# Evaluation
###############################################################################


# Names of all datasets
DATASETS = ['daps']

# Number of randomly-selected samples to evaluate
EVALUATION_SAMPLES = 100

# Thresholds (in number of 5 cent bins) for raw pitch accuracy evaluation
PITCH_ERROR_THRESHOLDS = [0, 1, 2]

# Seed for all random number generators
RANDOM_SEED = 1234
