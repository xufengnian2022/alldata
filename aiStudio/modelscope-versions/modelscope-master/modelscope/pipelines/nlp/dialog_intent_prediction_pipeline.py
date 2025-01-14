# Copyright (c) Alibaba, Inc. and its affiliates.

from typing import Any, Dict, Union

from modelscope.metainfo import Pipelines
from modelscope.models import Model
from modelscope.models.nlp import SpaceForDialogIntent
from modelscope.outputs import OutputKeys
from modelscope.pipelines.base import Pipeline
from modelscope.pipelines.builder import PIPELINES
from modelscope.preprocessors import DialogIntentPredictionPreprocessor
from modelscope.utils.constant import Tasks

__all__ = ['DialogIntentPredictionPipeline']


@PIPELINES.register_module(
    Tasks.task_oriented_conversation,
    module_name=Pipelines.dialog_intent_prediction)
class DialogIntentPredictionPipeline(Pipeline):

    def __init__(self,
                 model: Union[SpaceForDialogIntent, str],
                 preprocessor: DialogIntentPredictionPreprocessor = None,
                 **kwargs):
        """Use `model` and `preprocessor` to create a dialog intent prediction pipeline

        Args:
            model (str or SpaceForDialogIntent): Supply either a local model dir or a model id from the model hub,
            or a SpaceForDialogIntent instance.
            preprocessor (DialogIntentPredictionPreprocessor): An optional preprocessor instance.
        """
        model = model if isinstance(
            model, SpaceForDialogIntent) else Model.from_pretrained(model)
        if preprocessor is None:
            preprocessor = DialogIntentPredictionPreprocessor(model.model_dir)
        self.model = model
        super().__init__(model=model, preprocessor=preprocessor, **kwargs)
        self.categories = preprocessor.categories

    def postprocess(self, inputs: Dict[str, Any]) -> Dict[str, str]:
        """process the prediction results

        Args:
            inputs (Dict[str, Any]): _description_

        Returns:
            Dict[str, str]: the prediction results
        """
        import numpy as np
        pred = inputs['pred']
        pos = np.where(pred == np.max(pred))

        return {
            OutputKeys.OUTPUT: {
                OutputKeys.PREDICTION: pred,
                OutputKeys.LABEL_POS: pos[0],
                OutputKeys.LABEL: self.categories[pos[0][0]]
            }
        }
