
if __name__ == '__main__':
    notesDur = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    notesMol = ['c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g', 'g#', 'a', 'a#', 'b']

    #notesDurPL = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'B', 'H']
    #notesMolPL = ['c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g', 'g#', 'a', 'b', 'h']

    givenInput = input("Notes/chords to transpose: ")
    givenNotes = givenInput.split()
    print(givenNotes)
    transposed = givenNotes
    x = int(input("How many halftones? "))
    for i in range(len(givenNotes)):
        for j in range(12):
            if givenNotes[i] == notesDur[j]:
                if j+x<12: transposed[i] = notesDur[j+x]
                else:
                    y = -12+j+x
                    transposed[i] = notesDur[y]
                break
            if givenNotes[i] == notesMol[j]:
                if j+x<12: transposed[i] = notesMol[j+x]
                else:
                    y = -12+j+x
                    transposed[i] = notesMol[y]
                break

    print(transposed)