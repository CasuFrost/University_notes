'''
Funzioni di utilita' per leggere e salvare una immagine nella nostra codifica.
Utilities to load/save a PNG file to our encoding.
'''
import png

def load(filename):
    """ Carica la immagine PNG dal file 'filename'.  Torna una lista di liste di pixel.
        Ogni pixel è una tupla (R, G, B) dei 3 colori con valori tra 0 e 255.
        Load a PNG image from file 'filename'. Return a list of lists of pixel.
        Each pixel is a tuple (R, G, B) of its 3 colors with values in 0..255.
    """
    with open(filename, mode='rb') as f:
        reader = png.Reader(file=f)
        w, h, png_img, _ = reader.asRGB8()
        img = [0]*h
        for y,line in enumerate(png_img):
            l = [0]*w
            for x in range(w):
                j=x*3
                l[x]=(line[j], line[j+1], line[j+2])
            img[y]=l
        return img

def save(img, filename):
    """ Salva l'immagine 'img' nel file PNG 'filename'. img è una lista di liste di pixel. 
        Ogni pixel è una tupla (R, G, B) dei 3 colori con valori tra 0 e 255.
        Save the 'img' image in a 'filename' PNG file. img is a list of lists of pixel.
        Each pixel is a tuple (R, G, B) of its 3 colors with values in 0..255.
    """
    pngimg = png.from_array(img,'RGB')
    pngimg.save(filename)

