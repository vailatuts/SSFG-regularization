# SSFG: Stochastically Scaling Features and Gradients for Regularizing Graph Convolutional Networks
<br>

In this repository,  we implement the SSFG (stochastic ReLU) regularization method for regularizing graph convoultional networks. Our paper "SSFG: Stochastically Scaling Features and Gradients for Regularizing Graph Convolutional Networks" was accepted for publication in IEEE Transactions on Neural Networks and Learning Systems. The paper can be accessed [through this link](https://arxiv.org/abs/2102.10338).

```
@article{zhang2021ssfg,
  title={SSFG: Stochastically Scaling Features and Gradients for Regularizing Graph Convolutional Networks},
  author={Haimin Zhang, Min Xu, Guoqiang Zhang, and Kenta Niwa},
  journal={IEEE Transactions on Neural Networks and Learning Systems},
  year={2022}
}
```

### Preparation

Install PyTorch and the benchmark datasets following the official [Benchmarking Graph Neural Networks](https://github.com/graphdeeplearning/benchmarking-gnns).

Run the following command to reproduce our results on CIFAR10 using GatedGCN for superpixel graph classification:

```
python main_superpixels_graph_classification.py --dataset CIFAR10 --seed 95 --gpu_id 0 --config configs/superpixels_graph_classification_GatedGCN_CIFAR10_100k.json
```

For [graph attention networks (GATs)](https://arxiv.org/abs/1710.10903), the SSFG regularization is applied to the output of each of the multi-attention heads. This can be done by making the following change in  [layers/myreg.py](layers/myreg.py):

```
lam = bt.sample(grad_output.shape[:2]) + .5  # change grad_output.shape[:1] to grad_output.shape[:2]
```

### License

This project is currently under the CC-BY-NC 4.0 license. See [LICENSE](LICENSE) for details.
