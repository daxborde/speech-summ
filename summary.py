from gensim.summarization.summarizer import summarize
from gensim.summarization import keywords
import argparse

def summary(text_file):
    try:
        file = open(text_file, "r")
        text = file.read()
        text = text.replace('\n', ' ').replace('\r', ' ')
        output = open("output.txt", "w")
        output.write("summary:\n"+text)
        print(text)
        file.close()
        output.close()
    except (IOError, FileNotFoundError):
        print("Error in reading input file.")
        pass

def get_keywords():
    try:
        summary_file = open("output.txt", "r")
        kw = keywords(summary_file.read())
        output = open("keywords.txt", "w")
        output.write(kw)
        print("keywords:\n"+kw)
        summary_file.close()
        output.close()
    except (IOError, FileNotFoundError):
        print("Error in reading input file.")
        pass

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Uses gensim to summarize a given text file.")
    parser.add_argument("-i","--input", help = "Name of plain text file containing our corpus.", required = True)
    args = parser.parse_args()
    summary(args.input)
    get_keywords()