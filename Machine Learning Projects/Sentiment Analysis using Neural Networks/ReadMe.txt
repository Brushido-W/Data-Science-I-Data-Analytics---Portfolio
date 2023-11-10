## Sentiment Analysis using Neural Networks

This Capstone Project focuses on implementing a basic form of Natural Language Processing (NLP) known as Sentiment Analysis. The objective is to develop two distinct neural networks using Keras to classify book reviews as either positive or negative, and subsequently determine which network performs better.

The challenge lies in accurately identifying the sentiment of a review, even when the sentiment is negated or nuanced. For instance, consider the example review: "This book is not very good." Although the phrase "very good" appears at the end, indicating a positive sentiment, the presence of the negation term "not" reverses the sentiment, making it negative. Our task is to train the neural networks to recognize and classify such nuanced distinctions effectively.

To accomplish this, the project can be divided into the following key steps:

1. **Get the dataset**: Obtain a suitable dataset consisting of book reviews for training and evaluation purposes.
2. **Preprocess the Data**: Prepare the dataset by applying necessary preprocessing techniques such as tokenization, normalization, and removing stopwords.
3. **Build the Model**: Construct two different neural network architectures using the Keras framework, each with its unique configuration.
4. **Train the Model**: Train the neural networks using the preprocessed dataset to learn the patterns and sentiments associated with the book reviews.
5. **Test the Model**: Evaluate the performance of the trained models by testing them on a separate set of book reviews.
6. **Make Predictions**: Utilize the trained models to predict sentiments for new, unseen book reviews and assess their accuracy.

By following these steps, we aim to develop a robust sentiment analysis system capable of accurately classifying book reviews as positive or negative. The project allows for a comparative analysis of the two neural network models, providing insights into their respective performances.

Please refer to the project documentation and code for detailed instructions on dataset acquisition, data preprocessing, model building, training, testing, and making predictions.