from gensim.summarization.summarizer import summarize
from gensim.summarization import keywords

def summary(text_file):
    try:
        file = open(text_file, "r")
        text = file.read()
        text = text.replace('\n', ' ').replace('\r', ' ')
        output = open("output.txt", "w")
        output.write(text)
        print(text)
        file.close()
        output.close()
    except (IOError, FileNotFoundError) as e:
        print("Error in reading input file.")
        pass

def get_keywords():
    try:
        summmary_file = open("output.txt", "r").read()
        kw = keywords(summary_file)
        output = open("keywords.txt", "w")
        output.write(kw)
        print(output)
        summary_file.close()
        output.close()
    except (IOError, FileNotFoundError) as e:
        print("Error in reading input file.")
        pass

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Uses gensim to summarize a given text file.")
    parser.add_argument("-i","--input", help = "Name of plain text file containing our corpus.", required = True)
    args = parser.parse_args()
    summary(args.input)
