# MUSIC WITH PYTHON
import numpy as np
from pprint import pprint
from scipy.io.wavfile import write

# Code adapted from: https://github.com/weeping-angel/Mathematics-of-Music
# Emaj scale 

samplerate = 44100

def get_wave(freq, duration=0.5):
    #IN: frequecy time_duration for a wave 
    #OUT "numpy array" of values at all points in time
    
    amplitude = 4096
    t = np.linspace(0, duration, int(samplerate * duration))
    wave = amplitude * np.sin(2 * np.pi * freq * t)
    
    return wave

def get_piano_notes():
    #Returns a dict object for all the piano note freqs.

    # WHITE keys
    # black(sharp) keys
    octave = ['C', 'c', 'D', 'd', 'E', 'F', 'f', 'G', 'g', 'A', 'a', 'B', 'H','h','I','i','J','K','k','L','l','M','m','N'] 
    # added notes H through k to have all the numbers as in video
    
    base_freq = 261.63 #Frequency of Note C4
    base_freq2 = 523.25
    
    note_freqs1 = {octave[i]: base_freq * pow(2,(i/12)) for i in range(12)} #C4-B4 octave
    note_freqs2 = {octave[i+12]: base_freq2 * pow(2,(i/12)) for i in range(12)} #C5-B5 octave
    
    note_freqs = {**note_freqs1, **note_freqs2} #2 octave piano 
    note_freqs[''] = 0.0 # silent note

    # Emaj = {note_freqs}
    
    return note_freqs
  
def get_chords(progression):
    melody =''
    octave = ['C', 'c', 'D', 'd', 'E', 'F', 'f', 'G', 'g', 'A', 'a', 'B', 'H','h','I','i','J','K','k','L','l','M','m','N'] 
    major = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
    minor = ['Cm', 'Dm', 'Em', 'Fm', 'Gm', 'Am', 'Bm']
    # sharp = ['C#', 'D#', 'E#', 'F#', 'G#', 'A#', 'B#']
    # bemol = ['Cb', 'Db', 'Eb', 'Fb', 'Gb', 'Ab', 'Bb']

    chords_major1 = {major[i]: octave[2*i]+octave[2*i+4]+octave[2*i+7]for i in range(3)}
    chords_major2 = {major[i]: octave[2*i-1]+octave[2*i-1+4]+octave[2*i-1+7]for i in range(3,len(major))}
    chords_major ={**chords_major1, **chords_major2}

    chords_minor1 = {minor[i]: octave[2*i]+octave[2*i+4]+octave[2*i+7]for i in range(3)}
    chords_minor2 = {minor[i]: octave[2*i-1]+octave[2*i-1+3]+octave[2*i-1+7]for i in range(3,len(major))}
    chords_minor ={**chords_minor1, **chords_minor2}
    chords = {**chords_major, **chords_minor}

    #compose chord progression
    for name in progression.split('-'):
        melody += (str(chords[name])+'-') 

    return melody[:-1]

def get_song_data(music_notes):
    # Function to concatenate all the waves (notes)
    
    note_freqs = get_piano_notes() # Function that we made earlier
    song = [get_wave(note_freqs[note]) for note in music_notes.split('-')]
    song = np.concatenate(song)
    return song

def get_chord_data(chords):
    chords = chords.split('-')
    note_freqs = get_piano_notes()
    
    chord_data = []
    for chord in chords:
        data = sum([get_wave(note_freqs[note]) for note in list(chord)])
        chord_data.append(data)
    
    chord_data = np.concatenate(chord_data, axis=0)    
    return chord_data.astype(np.int16)

def get_song_from_seq(magic_number, c_flag):
    '''
    Return song data from number sequence from library.
    Inputs: 
        magic_number = the number of the sequence of choice from the library
        c_flag = 0 for the song to come out as single notes, 1 for the song to be made with chords
    
    Output:
        melody = a sequence of frequencies that can be played out

    '''
    Sequence ={
        0: '0-1-1-2-3-5-8-13-21-34-55-89-144-233-377-610-987-1597-2584-4181-6765-10946-17711-28657-46368-75025',
        #fibonacci
        1: '3.1415926535897932384626433832795028841971693993751',
        #pi
        2: '-A-B-A-C-A-B-A-D-A-B-A-C-A-B-A-E-A-B-A-C-A-B-A-D-A-B-A-C-A-B-A-F-A-B-A-C-A-B-A-D-A-B-A-C-A-B-A-E-A-B-A-C-A-B-A-D-A-B-A-C-A-B-A',
        #abacaba
        3: '1.80339887 4989484820 4586834365 6381177203 0917980576',
        #phi
        4: ''
        #recaman - tbd
    }
    music_notes=''

    #SELECT SEQUENCE
    if c_flag == 0: #get single note melody
        if magic_number != 2:    
            for nr in Sequence[magic_number]:
                if nr=='0':
                    music_notes+='-d'
                elif nr=='1':
                    music_notes+='-E'
                elif nr=='2':
                    music_notes+='-f'
                elif nr=='3':
                    music_notes+='-g'
                elif nr=='4':
                    music_notes+='-A'
                elif nr=='5':
                    music_notes+='-B'
                elif nr=='6':
                    music_notes+='-h'
                elif nr=='7':
                    music_notes+='-i'
                elif nr=='8':
                    music_notes+='-J'
                elif nr=='9':
                    music_notes+='-k'
        else:
            music_notes = Sequence[2]

        melody = get_song_data(music_notes)
        return melody

    else: #get chord melody
        if magic_number !=2:
            for nr in Sequence[magic_number]:
                if nr=='0':
                    music_notes+='-D' # D#
                elif nr=='1':
                    music_notes+='-E'
                elif nr=='2':
                    music_notes+='-F' # F#
                elif nr=='3':
                    music_notes+='-G' # G#
                elif nr=='4':
                    music_notes+='-A'
                elif nr=='5':
                    music_notes+='-B'
                elif nr=='6':
                    music_notes+='-B' # B# used to be H
                elif nr=='7':
                    music_notes+='-D' # D#
                elif nr=='8':
                    music_notes+='-E' # used to be J
                elif nr=='9':
                    music_notes+='-F' # F#+8
        else:
            music_notes = Sequence[2]

    chords = get_chords(music_notes[1:])
    melody = get_chord_data(chords)

    return melody

def main():
    x=2
    c_flag =1
    data = get_song_from_seq(x,c_flag)
    # data = get_song_data(music_notes)
    data = data * (16300/np.max(data)) # Adjusting the Amplitude (Optional)
    if c_flag  == 0:
        write(('music_'+str(x)+'.wav'), samplerate, data.astype(np.int16))
    else:
        write(('music_'+str(x)+'_chords.wav'), samplerate, data.astype(np.int16))

if __name__=='__main__':
    main()
