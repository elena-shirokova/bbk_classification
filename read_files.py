from os import listdir

#All texts together
def read_file(filename):
    infile = open(filename,'r')

    contents = infile.read()
    infile.close()
    return contents


def list_textfiles(directory):
    textfiles = []

    for filename in listdir(directory):
        if filename.endswith(".txt"):
            textfiles.append(directory + "/" + filename)

    return textfiles

def list_textfiles_label(directory):
    textfiles = []

    for filename in listdir(directory):
        if filename.endswith(".mrc"):
            textfiles.append((directory + "/" + filename,filename))

    return textfiles

def list_textfiles_files(directory):
    textfiles = []
    for filename in listdir(directory):
        if filename.endswith(".txt"):
            textfiles.append((directory + "/" + filename,filename))
    return textfiles