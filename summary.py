from gensim.summarization.summarizer import summarize

def summary(text_file):
    try:
        file = open(text_file, "r")
        text = file.read().replace('\n', ' ').replace('\r', ' ')
        summary.summarized_text = summarize(text)
        print(summary.summarized_text)
    except (FileNotFoundError, IOError) as e:
        pass
