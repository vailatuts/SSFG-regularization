import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
import pdb

class ssfg(torch.autograd.Function):

    @staticmethod
    def forward(ctx, x, training):
        if training:
            myparam = 1.5 
            bt = torch.distributions.beta.Beta(torch.tensor([myparam], device="cuda"), torch.tensor([myparam], device="cuda"))
            lam = bt.sample(x.shape[:1]) + .5
            lam[lam > 1] = 1./(2-lam[lam > 1])
            x = lam * x
        else:
            pass
        
        return x

    @staticmethod
    def backward(ctx, grad_output):

        myparam = 1.5
        bt = torch.distributions.beta.Beta(torch.tensor([myparam], device="cuda"), torch.tensor([myparam], device="cuda"))
        lam = bt.sample(grad_output.shape[:1]) + .5
        lam[lam > 1] = 1./(2-lam[lam > 1])

        return lam * grad_output, None


