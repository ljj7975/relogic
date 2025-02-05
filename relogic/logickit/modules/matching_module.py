import torch
import torch.nn as nn

class MatchingModule(nn.Module):
  def __init__(self, config, task_name, n_classes):
    super(MatchingModule, self).__init__()
    self.config = config
    self.task_name = task_name
    self.n_classes = n_classes
    self.to_logits = nn.Linear(config.hidden_size, self.n_classes)

  # def forward(self, input, input_mask=None, segment_ids=None, extra_args=None, **kwargs):
  def forward(self, *inputs, **kwargs):
    features = kwargs.pop("features")
    logits = self.to_logits(features[:,0])
    return logits