from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

input_text = input ("Enter content to be summarised:\n")

print ("Number of words in Entered content: ",len(input_text.split()))

a=int(input("Enter maximum number of word needed in summary accordingly"))

summary = summarizer(input_text, max_length=a, min_length=25, do_sample=False)


print("\nSummary:\n", summary[0]['summary_text'])
