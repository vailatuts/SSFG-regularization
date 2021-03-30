# SSFG: Stochastically Scaling Features and Gradients for Regularizing Graph Convolutional Networks
<br>

In this repository,  we implement the SSFG (stochastic ReLU) regularization method for regularizing graph convoultional networks. Our paper "SSFG: Stochastically Scaling Features and Gradients for Regularizing Graph Convolutional Networks" is available on Arxiv at [https://arxiv.org/abs/2102.10338](https://arxiv.org/abs/2102.10338).

```
@article{zhang2021ssfg,
  title={SSFG: Stochastically Scaling Features and Gradients for Regularizing Graph Convolution Networks},
  author={Zhang, Haimin and Xu, Min},
  journal={arXiv preprint arXiv:2102.10338},
  year={2021}
}
```

### Preparation

Install PyTorch and the benchmark datasets following the official [Benchmarking Graph Neural Networks](https://github.com/graphdeeplearning/benchmarking-gnns).

Run the following command to reproduce our results on CIFAR10 using GatedGCN for superpixel graph classification:

```
python main_superpixels_graph_classification.py --dataset CIFAR10 --seed 95 --gpu_id 0 --config configs/superpixels_graph_classification_GatedGCN_CIFAR10_100k.json
```


