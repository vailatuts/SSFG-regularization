import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
import pdb

class myshake(torch.autograd.Function):

    @staticmethod
    def forward(ctx, x, training):
        #return x
        if training:
            #bt = torch.distributions.beta.Beta(torch.tensor([2.]), torch.tensor([2.]))
            myparam = 10. 
            bt = torch.distributions.beta.Beta(torch.tensor([myparam], device="cuda"), torch.tensor([myparam], device="cuda"))
            lam = bt.sample(x.shape[:1]) + .5
            #lam = lam.type_as(x)
            #idx,_ = lam > 1
            #pdb.set_trace()
            lam[lam > 1] = 1./(2-lam[lam > 1])
            #pdb.set_trace()
            x = lam * x
            #pdb.set_trace()
        else:
            pass
        
        return x

    @staticmethod
    def backward(ctx, grad_output):


        #return grad_output, None

        myparam = 10.
        bt = torch.distributions.beta.Beta(torch.tensor([myparam], device="cuda"), torch.tensor([myparam], device="cuda"))
        #print('grad', grad_output[0].shape)
        #lam = bt.sample(grad_output[0].shape) + .5
        lam = bt.sample(grad_output.shape[:1]) + .5
        lam[lam > 1] = 1./(2-lam[lam > 1])
        #lam = lam.unsqueeze(0).squeeze(-1)
        #pdb.set_trace()
        #lam = lam.unsqueeze(-1)
        #lam = lam.type_as(grad_output)

        #print('lam', lam.shape, grad_output.shape)


        return lam * grad_output, None


