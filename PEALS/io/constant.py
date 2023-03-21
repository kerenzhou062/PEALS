# CONSTANT VALUE
VERSION = '1.2'
BUFFER_SIZE = 10000000
THREAD = 10
THREAD_START_METHOD="fork"
MATH_RELTOL = 0.05
MOVE_METHOD = "move"
SMOOTH_LOOP = 1
SMOOTH_SPAN = 25
PEAK_SIZE = 35
EXT_SIZE = 0
LOOK_AHEAD = 25
CSAPS_SMOOTH = 0.005
IP_RATIO = 1.25
CENTER = 0.1
COMPLEXITY_RATE = 0.05
TX_SPLIT_MAX_SIZE=50000
TX_SPLIT_OPT_SIZE=int(TX_SPLIT_MAX_SIZE * 0.3)
THIRD_PARTY_SOFTWARE = {'bedtools':'bash', 'featureCounts':'bash', 'samtools':'bash', 'DESeq2':'R'}
#identifier
ID_SEP_DICT={'labeltxid':'#=', 'txinfo':':=', 'genetx':'::', 'peakid':'|=', 'bedutils':'==', 'peakid_out':'|'}
REF_PEAK_LABEL = 'POOL_REF'
BINARY_APPENDIX = '.mbb'
# CONSTANT TEMP NAME
TEMP_PREFIX = "peals_tmp"
# CONSTANT HELP
EPILOG_CALL_PEAK = """
Examples:
Peak calling for regular MeRIP-seq:
    $ peals callpeak -i <bam directory> -m <sample matrix> -P <prefix> -o <output directory>
"""

EPILOG_DIFF_PEAK = """
Examples:
Differential peak calling for regular MeRIP-seq:
    $ peals diffpeak -i <bam directory> -m <sample matrix> -P <prefix> -o <output directory>
"""

# CONSTANT LOGGING MESSAGE
RUNNING_TIME = "Total execution time for the whole analysis was: {}."
GET_GENE_EXP_LOG = "Obtaining gene expression..."
GET_TX_EXP_LOG = "Obtaining trascript expression..."
SUBSAMPLE_BAM_LOG = "Subsampling input bams with seed {}..."
BAM_TO_COVERAGE_LOG = "Preparing genome-wide reads coverage..."
DECODE_ANNO_LOG = "Decoding and building annotation information from {}..."
CALL_PEAK_LOG = "Calling peak candidates on ip ({}) and input ({})..."
CALL_PEAK_DONE_LOG = "Calling peak candidates on ip ({}) and input ({}) done."
READ_BINARY_LOG = "Reading binary files from specified input ({})..."