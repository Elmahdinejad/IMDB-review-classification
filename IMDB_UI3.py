import tkinter as tk  
from tkinter import messagebox, scrolledtext  
import numpy as np  
from tensorflow.keras.models import load_model  
from tensorflow.keras.preprocessing.sequence import pad_sequences  
from tensorflow.keras.datasets import imdb  
import re  

# Load the Keras model  
model = load_model('IMDB_model.keras')  

# Load the IMDB word index to translate integers to words  
word_index = imdb.get_word_index()  
reverse_word_index = {value: key for key, value in word_index.items()}  
reverse_word_index[0] = '[PAD]'  # For padding  

def preprocess_review(review):  
    # Clean and tokenize the text  
    review = re.sub(r'\W', ' ', review)  # Remove non-word characters  
    review = review.lower().split()  
    # Convert words to integers  
    encoded_review = [word_index.get(word, 0) for word in review]  # Default to 0 for unknown words  
    # Create a one-hot encoded vector (size 10000)  
    one_hot_review = np.zeros(10000)  # Assuming a vocabulary size of 10,000  
    for index in encoded_review:  
        if index < 10000:  # Ensure we only fill valid indices  
            one_hot_review[index] = 1  
    return one_hot_review.reshape(1, -1)  # Reshape to (1, 10000)  

def predict_sentiment():  
    review = review_text.get("1.0", tk.END).strip()  # Get review from text area  
    if not review:  
        messagebox.showwarning("Input Error", "Please enter a review.")  
        return  

    # Preprocess and predict sentiment  
    processed_review = preprocess_review(review)  
    prediction = model.predict(processed_review)  # Predict sentiment  
    sentiment = "Positive" if prediction[0][0] >= 0.5 else "Negative"  

    # Show the result in message box  
    messagebox.showinfo("Prediction Result", f"The review is: {sentiment}")  

# Create the main application window  
app = tk.Tk()  
app.title("Movie Review Sentiment Analysis")  
app.geometry("600x500")  
app.configure(bg="#2E2E2E")  # Dark gray background  

# Header Frame  
header_frame = tk.Frame(app, bg="#3C3C3C")  
header_frame.pack(side=tk.TOP, fill=tk.X)  

# Create a title label  
title_label = tk.Label(header_frame, text="Movie Review Sentiment Analysis", font=("Helvetica", 18, "bold"), bg="#3C3C3C", fg="white")  
title_label.pack(pady=15)  

# Create input text area for review  
tk.Label(app, text="Enter your movie review:", font=("Helvetica", 12), bg="#2E2E2E", fg="white").pack(pady=10)  

review_text = scrolledtext.ScrolledText(app, height=10, width=70, font=("Helvetica", 12), wrap=tk.WORD, bg="#444444", fg="white", bd=2, relief=tk.GROOVE)  
review_text.pack(pady=10)  

# Create a button to predict sentiment  
predict_button = tk.Button(app, text="Predict Sentiment", command=predict_sentiment,  
                            font=("Helvetica", 12), bg="#4CAF50", fg="white", padx=15, pady=8, relief=tk.RAISED)  
predict_button.pack(pady=20)  

# Status Bar Frame  
status_frame = tk.Frame(app, bg="#2E2E2E")  
status_frame.pack(side=tk.BOTTOM, fill=tk.X)  

status_label = tk.Label(status_frame, text="Enter a movie review and click 'Predict Sentiment'.", font=("Helvetica", 10), bg="#2E2E2E", fg="#CCCCCC")  
status_label.pack(pady=5)  

# Create a footer label  
footer_label = tk.Label(app, text="❤️ Made as my first sentiment prediction using Tkinter and TensorFlow ❤️", font=("Helvetica", 10), bg="#2E2E2E", fg="#CCCCCC")  
footer_label.pack(side=tk.BOTTOM, pady=10)  

# Run the application  
app.mainloop()