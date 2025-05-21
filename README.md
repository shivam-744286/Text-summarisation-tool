# Text-summarisation-tool

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: SHIVAM KUMAR

*Intern id*: CT04DN1277

*DOMAIN*: Artificial Intelligence

*DURATION*: 4 weeks

*MENTOR*: NEELA SANTOSH

This project is done using Google colab. It is a online compiler which provide all the libraries available in python. it is a free, browser-based service that allows users to write and execute Python code in a cloud environment

*OUTPUT*:
![Image](https://github.com/user-attachments/assets/009f4c60-5a33-491c-b1b0-664b33e2aecc)
![Image](https://github.com/user-attachments/assets/a43ac82d-d173-40f1-b680-5454c2b8be7e)

The process making this tool is as follows:

At first, we import a special function called pipeline from a library named hugging face transformers these functions gives us an easy access to powerful ai models that can perform different language tasks including summarization. (in first line)

Next we create a summarizer by calling the pipeline and specifying that we want to do summarization. We also select a model called "facebook/bart-large-cnn" which is very good at generating summaries it's already trained. so, we don't need to train it ourselves. As 'BART' stands for 'Bidirectional and Auto-Regressive transformer'. it's a NLP which was trained on massive text data set to detect the main idea, remove unnecessary info and write shorter version in correct grammar.

Then we write or paste a long paragraph of text. This could be from news article, blog post, even an academic paper. For example I have written a paragraph which shows what is cryptocurrency and how does it work..

Next using a function split and len, We can know how much words are there in the entered paragraph which can help us to roughly estimate the number of words does the summary contain. After estimation a rough number of words is given to the summarize operator as an argument. Or value can be directly entered to min length and Max length by the coder. This step depends on the person as perspective may change from person to person.

Now we pass the input paragraph into the summarizer we tell it the maximum and minimum length of the summary we want. The AI will read the whole input understand its meaning and then generate a short meaningful summary.

Finally we print the summary which is shorter version of the original content we entered.
