# MUSIC WITH PYTHON
import numpy as np
from pprint import pprint
from scipy.io.wavfile import write

# Code adapted from: https://github.com/weeping-angel/Mathematics-of-Music
# Emaj scale 

samplerate = 44100

def get_wave(freq, duration=0.5):
    '''
    Input: frequecy time_duration for a wave 
    Output: array of values describing the sine function of the wave 
            (which can be reproduced as sound)
    '''
    
    amplitude = 4096
    t = np.linspace(0, duration, int(samplerate * duration))
    wave = amplitude * np.sin(2 * np.pi * freq * t)
    
    return wave

def get_piano_notes():
    '''
    Returns a dict object for all the piano note freqs for 2 octaves.
        White keys - X, Black keys - x, C = C4, 261.63 Hz
        Standard notation of notes in English for the first octave, 
        after the first octave, the note symbols go alphabetically from H to N
    '''
    octave = ['C', 'c', 'D', 'd', 'E', 'F', 'f', 'G', 'g', 'A', 'a', 'B', 'H','h','I','i','J','K','k','L','l','M','m','N'] 
    
    base_freq = 261.63 #Frequency of Note C4
    note_freqs = {octave[i]: base_freq*pow(4,(i/24)) for i in range(len(octave))}
    note_freqs[''] = 0.0 # silent note
    
    return note_freqs
  
def get_chords():
    '''
    Returns a dict object for all the major and minor chords in Emaj (the scale chosen for this project).
        Each chord is composed of the primary, third and fifth notes (as described in get_piano_notes())
    '''
    octave = ['C', 'c', 'D', 'd', 'E', 'F', 'f', 'G', 'g', 'A', 'a', 'B', 'H','h','I','i','J','K','k','L','l','M','m','N'] 
    major = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'B#']
    minor = ['Cm', 'C#m', 'Dm', 'D#m', 'Em', 'Fm', 'F#m', 'Gm', 'G#m', 'Am', 'A#m', 'Bm', 'B#m']

    chords_major = {major[i]: octave[i]+octave[i+4]+octave[i+7]for i in range(len(major))}
    chords_minor = {minor[i]: octave[i]+octave[i+3]+octave[i+7]for i in range(len(minor))}
    chords = {**chords_major, **chords_minor}

    return chords

def get_song_data(music_notes):
    '''
    Function to concatenate all the waves (notes)
    
    Inputs: The progression of music notes (with the symbols as defined in get_piano_notes())
            as a string with elements separated by '-'
    Outputs: The concatenated waves as an array
    '''
    print(music_notes)
    note_freqs = get_piano_notes() 
    song = [get_wave(note_freqs[note]) for note in music_notes.split('-')]
    song = np.concatenate(song)
    # print(song)
    return song

def get_chord_data(music_notes):
    '''
    Function to concatenate all the waves into chords
    
    Inputs: The progression of chords (with the standard notation of chords in English) 
            as a string with elements separated by '-'
    Outputs: The concatenated and superimposed waves as an array
    '''
    # print(music_notes)
    chords = get_chords()
    chords_pr = str(chords[music_notes])
    # print(chords_pr)
    # Getting from chords to the notes they are made up of
    # for name in music_notes.split('-'):
    #     chords_pr += (str(chords[name])+'-') 

    # chords_pr = chords_pr.split('-')
    # chords_pr = chords_pr [:-1]
    

    # Using the chords expanded into notes to obtain the wave data
    note_freqs = get_piano_notes()
    chord_data = []
    data = sum([get_wave(note_freqs[note]) for note in chords_pr])
    chord_data.append(data)
    # print(chord_data)

    # Concatenation step
    chord_data = np.concatenate(chord_data, axis=0) 
    # print(chord_data)   
    return chord_data.astype(np.int16)

def get_song_from_seq(number_sequence):
    '''
    Return song data from number sequence.
    Inputs: 
        number_sequence = the number of the sequence of choice as a string
        c_flag = 0 for the song to come out as single notes
               = 1 for the song to be made with chords
    Output:
        melody = a sequence of frequencies that can be played out (array with wave data)
    '''

    music_notes=''
    song=[]
    counter =0
    c_flag=1
    for nr in number_sequence:
        # reset counter
        if counter == 3:
            c_flag=1
            counter=0

        if c_flag == 0: #get single note melody   
            if nr=='0':
                music_notes='d'
            elif nr=='1':
                music_notes='E'
            elif nr=='2':
                music_notes='f'
            elif nr=='3':
                music_notes='g'
            elif nr=='4':
                music_notes='A'
            elif nr=='5':
                music_notes='B'
            elif nr=='6':
                music_notes='h'
            elif nr=='7':
                music_notes='i'
            elif nr=='8':
                music_notes='J'
            elif nr=='9':
                music_notes='k'
            song.append(get_song_data(music_notes))

        elif c_flag==1: #get chord melody
            if nr=='0':
                music_notes='D#m'
            elif nr=='1':
                music_notes='E'
            elif nr=='2':
                music_notes='F#m'
            elif nr=='3':
                music_notes='G#' 
            elif nr=='4':
                music_notes='A'
            elif nr=='5':
                music_notes='Bm'
            elif nr=='6':
                music_notes='C#' 
            elif nr=='7':
                music_notes='D#m'
            elif nr=='8':
                music_notes='E'
            elif nr=='9':
                music_notes='F#m' 
            song.append(get_chord_data(music_notes))
            c_flag=0
    counter += 1

    print(song)
    song=np.concatenate(song, axis=0)
    song = song * (16300/np.max(song)) # Adjusting the Amplitude
    return song


def main():
    Sequence ={
        'fibonacci': '0-1-1-2-3-5-8-13-21-34-55-89-144-233-377-610-987-1597-2584-4181-6765-10946-17711-28657-46368-75025',
        'pi': '3.1415926535897932384626433832795028841971693993751',
        # 2: '-A-B-A-C-A-B-A-D-A-B-A-C-A-B-A-E-A-B-A-C-A-B-A-D-A-B-A-C-A-B-A-F-A-B-A-C-A-B-A-D-A-B-A-C-A-B-A-E-A-B-A-C-A-B-A-D-A-B-A-C-A-B-A',
        # #abacaba !WON'T WORK ANYMORE
        'phi': '1.80339887 4989484820 4586834365 6381177203 0917980576',
        'recaman': '0 1 3 6 2 7 13 20 12 21 11 22 10 23 9'
    }

    x = 'fibonacci'
    nr_seq=Sequence[x]
    # c_flag=0
    data = get_song_from_seq(nr_seq)
    
    write(('music_'+str(x)+'_complex.wav'), samplerate, data.astype(np.int16))


if __name__=='__main__':
    main()
