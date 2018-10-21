import speech_recog as sr
import summary as sum
import argparse

def run_me(filename):
    print("Begin upload:")
    sr.upload(filename)
    print("Upload finished. Begin transcription:")
    sr.transcribe_gcs(sr.blob_q.get(), "transcription.txt")
    print("Transcription finished. Begin summary:")
    sum.summary("transcription.txt")
    print("Summary finished. Begin keywords:")
    sum.get_keywords()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Recognizes speech in a WAV file, then summarizes the generated text and extracts keywords.")
    parser.add_argument("-i","--input", help = "WAV file to use as input", required = True)
    args = parser.parse_args()
    run_me(args.input)