import matplotlib.pyplot as plt

paragraph = """Figure 2 allows us to semi-quantitively make comparisons between the electron transfer kinetics of the two proteins. At 12 Hz any signals from cytochrome C6 have completely disappeared whereas signals from plastocyanin remain obvious. The rapid attenuation of signals from cyt C6 shows it’s inability transfer electrons quickly enough to keep up with oscillations of the applied sinusoidal potential at higher frequencies and therefore its comparative slowness when compared to plastocyanin which continues to show strong signals even at 24 Hz. This is supported by the asymmetry obvious in many of the harmonics of cyt C6 shown in figure 1 which is absent even at the highest frequencies of Pc.

Gold working Electrodes
In order to offset the satellite signals obscuring the cyt C6 harmonics present when FTacV is conducted on PGE electrodes, it was decided to try stabilising cyt C6 on a SAM, adsorbed onto a gold surface. Originally the SAM chosen was 3-mercapto-propionic acid (SHCH2CH2COOH) as this would provide a uniform negative charge to allow consistent orientation of the protein on the electrode. However, this system also caused obscuring signals of unknown origin to appear on the electrode, so it was decided to try making SAMs with cystamine (SHCH2CH2NH2) to provide a uniform positive charge on the electrode. It is theorised however, that this repels the mostly positively charged heme binding pocket in cyt C6 and therefore holds the heme centre beyond the distance possible for electron transfer. 
"""

normalised = paragraph.lower()

punctuation = ".!?,"


removed = str.maketrans({char: None for char in punctuation})

cleaned_txt = normalised.translate(removed)

print (cleaned_txt)

words = cleaned_txt.split()

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
   
sorted_words = sorted(word_count.items(), key = lambda x: (-x[1], x[0]))

for word, count in sorted_words:
    print(word + ":", count)
    
    
words_counted = [word for word, count in sorted_words]
count = [count for word, count in sorted_words]

plt.figure()
plt.xticks(rotation=45)
plt.bar(words_counted, count)

        