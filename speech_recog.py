import io, os, datetime, queue, argparse

# Imports Google Cloud client libraries
from google.cloud import speech, storage
from google.cloud.speech import enums, types
from google.cloud.storage import Blob

blob_q = queue.Queue()
BUCKET_NAME = "directed-beacon-143800.appspot.com"
PROJECT_NAME = "directed-beacon-143800"

def upload(filename):
    client = storage.Client(project=PROJECT_NAME)
    bucket = client.get_bucket(BUCKET_NAME)
    blob_name = "{}_{}".format(str(datetime.datetime.now()), filename)
    blob = Blob(blob_name, bucket)
    with open(filename, 'rb') as my_file:
        blob.upload_from_file(my_file)
        blob_q.put("gs://{}/{}".format(BUCKET_NAME, blob_name))

def transcribe_gcs(gcs_uri, out_file_name):
    client = speech.SpeechClient()

    operation = client.long_running_recognize(
        audio=speech.types.RecognitionAudio(
            uri=gcs_uri,
        ),
        config=speech.types.RecognitionConfig(
            encoding='LINEAR16',
            language_code='en-US',
            enable_automatic_punctuation=True,
            profanity_filter=True,
            sample_rate_hertz=16000
        )
    )

    print('Waiting for operation to complete...')
    response = operation.result(timeout=90)

    of = open(out_file_name, "w")

    for result in response.results:
        of.write('{}'.format(result.alternatives[0].transcript))

    of.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Uses the Google Cloud Speech API and Storage to recognize speech in wav files.")
    parser.add_argument("-i","--input", help = "WAV file to use as input", required = True)
    parser.add_argument("-o","--output", help = "Text file to output transcription to", default="transcription.txt")
    args = parser.parse_args()

    upload(args.input)
    transcribe_gcs(blob_q.get(), args.output)