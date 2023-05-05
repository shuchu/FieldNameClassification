# -*- coding: utf-8 -*-


from typing import List

import fasttext

from field_name_classifier import FieldNameClassifier
from tokenizer import Tokenizer


class FTClassifier(FieldNameClassifier):
    def __init__(self, prob_threshold=0.0):
        self._model = None
        self._tokenizer = Tokenizer()
        self._prob_th = 0.0  # Threshold of prediction probability

    def predict_field_type(self, field_name: str) -> List[str]:
        if not field_name:
            return []

        tokens = self._tokenizer.extract_tokens(field_name)
        pred, prob = self._model.predict(" ".join(tokens))

        label = ""
        p = prob[0]
        if pred:
            label = pred[0][9:]  # fasttext's label property

        if p >= self._prob_th:
            return [label]
        else:
            return []

    def load_knowledge_dict(self, knowledge_dict: dict) -> None:
        pass

    def load_model(self, model_path: str) -> None:
        self._model = fasttext.FastText.load_model(model_path)

    def save_model(self, model_path: str) -> None:
        self._model.save_model(model_path)

    def train(self, tr_data_fname: str) -> None:
        self._model = fasttext.train_supervised(
            input=tr_data_fname, lr=1.0, epoch=25, wordNgrams=2
        )
