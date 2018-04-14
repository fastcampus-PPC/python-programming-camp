from pretrained.loader.pkl_loader import Vectorizer, Classifier

if __name__ == "__main__":
    review = input("Please enter your review: ")
    input_features = Vectorizer.instance().get_vector(review)
    result = Classifier.instance().get_prediction(input_features)

    print("당신은 " + str(result))