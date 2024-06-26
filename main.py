import time as t
import argparse
import sounddevice as sd
import numpy as np

from signal_chain import SignalChain
from effects.distortion import Distortion
from effects.chorus import Chorus

def int_or_str(text):
    """Helper function for argument parsing."""
    try:
        return int(text)
    except ValueError:
        return text


parser = argparse.ArgumentParser(add_help=False)
parser.add_argument(
    '-l', '--list-devices', action='store_true',
    help='show list of audio devices and exit')
args, remaining = parser.parse_known_args()
if args.list_devices:
    print(sd.query_devices())
    parser.exit(0)
parser = argparse.ArgumentParser(
    description=__doc__,
    formatter_class=argparse.RawDescriptionHelpFormatter,
    parents=[parser])
parser.add_argument(
    '-i', '--input-device', type=int_or_str,
    help='input device (numeric ID or substring)')
parser.add_argument(
    '-o', '--output-device', type=int_or_str,
    help='output device (numeric ID or substring)')
parser.add_argument(
    '-c', '--channels', type=int, default=2,
    help='number of channels')
args = parser.parse_args(remaining)


effects = SignalChain([
    Distortion(volume=-10, drive=16, normalize=False),
    Chorus()
], block_size=32, samplerate=48000)

def callback(indata, outdata, frames, time, status):
    if status:
        print(status)
    indata = effects.apply(indata)
    outdata[:] = indata


# The input device is a PreSonus Audiobox USB96
try:
    with sd.Stream(device=(args.input_device, args.output_device),
                   samplerate=48000, blocksize=32,  # Look into exactly what changing this entails
                   dtype='float32',  # Using int16 leaves it unnormalized. float32 normalizes the waveform
                   latency=0.01,
                   channels=1,  # Stereo for now, could be mono
                   callback=callback):
        print('#' * 80)
        print('press Return to quit')
        print('#' * 80)
        input()
except KeyboardInterrupt:
    parser.exit('')
except Exception as e:
    parser.exit(type(e).__name__ + ': ' + str(e))