# -*- coding: utf-8 -*-


from abc import ABC, abstractmethod
from typing import List


class FieldNameClassifier(ABC):
    @abstractmethod
    def predict_field_type(self, field_name: str) -> List[str]:
        pass

    @abstractmethod
    def load_knowledge_dict(self, knowledge_dict: dict) -> None:
        pass
