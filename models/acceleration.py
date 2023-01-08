# This file implements acceleration/velocity calculation

import torch
import torch.nn as nn


class AcFusionLayer(nn.Module):
	"""docstring for AcFusionLayer"""
	def __init__(self, ):
		super(AcFusionLayer, self).__init__()
	
	def forward(self, flo10, flo01, flo12, flo21, flo32, flo23, t=0.5):
		"""
			-- input: four flows
			-- output: center shift
		"""

		return (t/4 - t**2/4 + t**3/6) * flo01 + (t/2 + t**3/3)*flo12 + (t/4 + t**2/4 + t**3/6)*flo23, ((1-t)/4 - (1-t)**2/4 + (1-t)**3/6) * flo10 + ((1-t)/2 + (1-t)**3/3)*flo21 + ((1-t)/4 + (1-t)**2/4 + (1-t)**3/6)*flo32
		
