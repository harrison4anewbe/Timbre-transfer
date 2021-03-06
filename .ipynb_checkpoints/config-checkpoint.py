import os

IMG_DIM = (256,256,1)

DEFAULT_SAMPLING_RATE = 44100
LAMBDA = 100

NSYNTH_VELOCITIES = [25, 50, 100, 127]
NSYNTH_SAMPLE_RATE = 16000

hop_length = 512
bins_per_octave = 16 * 2
amin=1/(2**16)

TEST_AUDIOS_PATH = '..//data//audios//test'

OUTPUT_PATH = os.path.join('..','data', 'outputs')
CHECKPOINT_DIR = os.path.join('..', 'models')