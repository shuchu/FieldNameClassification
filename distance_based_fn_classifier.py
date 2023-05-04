# -*- codint: utf-8 -*-


from collections import defaultdict
from typing import List, Dict, Set, DefaultDict

from textdistance import DamerauLevenshtein

from field_name_classifier import FieldNameClassifier


class DistanceFieldNameClassifier(FieldNameClassifier):
    def __init__(self, distance_tr: float = 1.0):
        # the default knowledge dictionary
        self._kd = {}  # type: Dict[str, List[str]]
        # Use set() to avoid duplication in the value list of a key in knowledge dictionary.
        self._lookup_tbl = defaultdict(set)  # type: DefaultDict[str, Set]
        self._dl_dist = DamerauLevenshtein() 
        self._distance_tr = distance_tr  # distance threshold

    def predict_field_type(self, field_name: str) -> List[str]:
        """Predict the field type of a given field name.

        Args:
            field_name: the querying field name.

        Returns:
            List of associated field types.

        """
        if field_name in self._lookup_tbl:
            return list(self._lookup_tbl[field_name])
        else:
            # do similarity search
            top_fn = self._search_similar_field_names(field_name)
            res = set()
            for fn in top_fn:
                for ft in self._lookup_tbl[fn]:
                    res.add(ft)
            return list(res)

    def _search_similar_field_names(self, field_name: str) -> List[str]:
        # Search the most similar field names in knowledge dictionary.
        top_fn = []
        min_dist_nm = self._distance_tr
        for key in self._lookup_tbl:
            d = self._dl_dist(field_name, key)
            d_nm = d / max(len(field_name), len(key))
            if d_nm < min_dist_nm:
                min_dist_nm = d_nm
                top_fn = [key]
            elif d_nm == min_dist_nm:
                top_fn.append(key)
        return top_fn

    def load_knowledge_dict(self, knowledge_dict: dict) -> None:
        """Load the (field type, field names) mapping. Create an inverse map from field name to field types."""
        self._kd = knowledge_dict

        # Update the lookup table
        for key in self._kd:
            if isinstance(self._kd[key], list):
                for val in self._kd[key]:
                    self._lookup_tbl[val].add(key)
