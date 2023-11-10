# Sentiment analysis

For this project, I use two different neural networks in Keras to try and classify 
a book review as either positive or negative, and report on which network type worked 
better.

This problem can be broken down into the following steps:
1. Get the dataset
2. Preprocessing the Data
3. Build the Model
4. Train the model
5. Test the Model
6. Predict Something

I will be using a small portion of the Multi-Domain Sentiment Dataset, which contains 
product reviews from Amazon. The full dataset contains reviews for products under the 
categories: kitchen, books, DVDs, and electronics, but I will only be looking at 
reviews for the book category.

Then I have craeted two files, positive.txt and negative.txt, containing the reviews. 
Each review is associated with a number of fields. The only field we are interested 
in is the “title” field, which contains the title of the review. I have used this title 
to predict the sentiment of the review. While some sentiments are easy to classify, 
like “don’t buy this horrible book”, others are less straightforward, like “'run don't 
walk to buy this book”. The latter is hard to classify because it contains the word
“don’t”, which might be seen as an indication that this is a negative review, whereas 
actually, it is a positive one. Thus, sentiment analysis is not always straightforward.

In order to feed this data into our network, all input reviews must have the same
length. Since the reviews differ heavily in terms of lengths, we either need to trim
or pad the reviews so that they are the same length. For this project, we will set the
length of reviews to the mean length, which is around 4 words. I then built a recurrent 
neural network to classify sentiment. The network will need to start with a special 
layer which will assist with text classification through a process called embedding.

Once all the above steps were completed we are now ready to train your model.
I have then compiled my model by specifying the loss function and optimizer we want
to use while training, as well as any evaluation metrics we’d like to measure. I set 
the optimizer to ‘adam’ and the loss function to ‘binary_crossentropy’.


