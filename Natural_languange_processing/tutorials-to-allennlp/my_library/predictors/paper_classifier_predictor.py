# _*_ encoding: utf-8 _*_
"""
@file: paper_classifier_predictor.py
@author: kebo
@contact: itachi971009@gmail.com
@time: 2019-03-19 17:54
@desc:
"""
from overrides import overrides

from allennlp.common.util import JsonDict
from allennlp.data import Instance
from allennlp.predictors.predictor import Predictor

@Predictor.register("paper-classifier")
class PaperClassifierPredictor(Predictor):
    """Predictor wrapper for the AcademicPaperClassifier"""
    def predict_json(self, inputs: JsonDict) -> JsonDict:
        instance = self._json_to_instance(inputs)
        output_dict = self.predict_instance(instance)
        label_dict = self._model.vocab.get_index_to_token_vocabulary('labels')
        all_labels = [label_dict[i] for i in range(len(label_dict))]
        output_dict["all_labels"] = all_labels
        return output_dict

    @overrides
    def _json_to_instance(self, json_dict: JsonDict) -> Instance:
        title = json_dict['title']
        abstract = json_dict['paperAbstract']
        return self._dataset_reader.text_to_instance(title=title,abstract=abstract)