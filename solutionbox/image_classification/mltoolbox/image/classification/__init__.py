# Copyright 2017 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except
# in compliance with the License. You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License
# is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
# or implied. See the License for the specific language governing permissions and limitations under
# the License.

"""
Single label image classification solution. Typical usage is:

Run preprocess() or preprocess_async() to preprocess data for training.
Run train() or train_async() to train models.
Run predict(), batch_predict(), batch_predict_async() to perform predictions.

The trained model can also be deployed online with google.datalab.ml.ModelVersions.deploy() call.
"""

from ._api import preprocess, preprocess_async, train, train_async, predict, batch_predict, \
    batch_predict_async

__all__ = ['preprocess', 'preprocess_async', 'train', 'train_async', 'predict', 'batch_predict',
           'batch_predict_async']
