import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification


class SentimentAnalyzer:
    def __init__(self, model_path):
        self.__model_path = model_path
        self.labels = ['negative', 'neutral', 'positive']

    def load_model(self):
        self.tokenizer = AutoTokenizer.from_pretrained(self.__model_path)
        self.model = AutoModelForSequenceClassification.from_pretrained(
            self.__model_path)

    def get_sentiment(self, text):
        if not hasattr(self, 'model'):
            self.load_model()
        inputs = self.tokenizer(text, return_tensors="pt")
        outputs = self.model(**inputs)
        probs = torch.softmax(outputs.logits, dim=1).squeeze()
        return {
            'sentiment': self.labels[probs.argmax()],
            'score': probs.max().item(),
            'details': {self.labels[i]: prob.item() for i, prob in enumerate(probs)}
        }
