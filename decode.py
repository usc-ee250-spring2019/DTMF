""" EE 250L
List team members here.
Insert Github repository link here.
"""

import matplotlib.pyplot as plt
import numpy as np
from pydub import AudioSegment
import os
import sys

MAX_FRQ = 2000
SLICE_SIZE = 0.15 #seconds
WINDOW_SIZE = 0.25 #seconds
NUMBER_DIC = {}

LOWER_FRQS = [697, 770, 852, 941]
HIGHER_FRQS = [1209, 1336, 1477, 1633]
FRQ_THRES = 20

def get_peak_frqs(frq, fft):
    #TODO: implement an algorithm to find the two maximum values in a given array
    upper_frq = 0
    lower_frq = 0
    return (lower_frq, upper_frq)

def get_number_from_frqs(lower_frq, higher_frq):
    #TODO: given a lower frequency and higher frequency pair
    #      return the corresponding key otherwise return '?' if no match is found
    return '?'

def main(file):
    print("Importing {}".format(file))
    audio = AudioSegment.from_mp3(file)

    sample_count = audio.frame_count()
    sample_rate = audio.frame_rate
    samples = audio.get_array_of_samples()

    print("Number of channels: " + str(audio.channels))
    print("Sample count: " + str(sample_count))
    print("Sample rate: " + str(sample_rate))
    print("Sample width: " + str(audio.sample_width))

    period = 1/sample_rate                     #the period of each sample
    duration = sample_count/sample_rate         #length of full audio in seconds

    slice_sample_size = int(SLICE_SIZE*sample_rate)   #get the number of elements expected for [SLICE_SIZE] seconds

    n = slice_sample_size                            #n is the number of elements in the slice

    #generating the frequency spectrum
    k = np.arange(n)                                #k is an array from 0 to [n] with a step of 1
    slice_duration = n/sample_rate                   #slice_duration is the length of time the sample slice is (seconds)
    frq = k/slice_duration                          #generate the frequencies by dividing every element of k by slice_duration

    max_frq_idx = int(MAX_FRQ*slice_duration)       #get the index of the maximum frequency (2000)
    frq = frq[range(max_frq_idx)]                   #truncate the frequency array so it goes from 0 to 2000 Hz

    start_index = 0                                 #set the starting index at 0
    end_index = start_index + slice_sample_size      #find the ending index for the slice
    output = ''

    print()
    i = 1
    while end_index < len(samples):
        print("Sample {}:".format(i))
        i += 1

        #TODO: grab the sample slice and perform FFT on it
        #hint: you will need to use the samples variable
        #sample_slice = samples[?]


        #TODO: truncate the FFT to 0 to 2000 Hz
        #hint: you will need to make use of max_frq_idx


        #TODO: calculate the locations of the upper and lower FFT peak using get_peak_frqs()


        #TODO: print the values and find the number that corresponds to the numbers using get_number_from_frqs()


        #Incrementing the start and end window for FFT analysis
        start_index += int(WINDOW_SIZE*sample_rate)
        end_index = start_index + slice_sample_size

    print("Program completed")
    print("User typed: " + str(output))

if __name__ == '__main__':
    if len(sys.argv) != 2 or not os.path.isfile(sys.argv[1]):
        print("Usage: decode.py [file]")
        exit(1)
    main(sys.argv[1])
