# Copyright 2019 Yahoo Inc / Verizon Media
# Licensed under the terms of the Apache 2.0 license.
# Please see LICENSE file in the project root for terms.
"""Helper functions to abstract API changes between TensorFlow versions."""

import tensorflow as tf

TF_VERSION = tf.__version__


def export_saved_model(model, export_dir, is_chief=False):
  if TF_VERSION == '2.0.0':
    if is_chief:
      tf.keras.experimental.export_saved_model(model, export_dir)
  else:
    model.save(export_dir, save_format='tf')


def disable_auto_shard(options):
  if TF_VERSION == '2.0.0':
    options.experimental_distribute.auto_shard = False
  else:
    options.experimental_distribute.auto_shard_policy = tf.data.experimental.AutoShardPolicy.OFF
