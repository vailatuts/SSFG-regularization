
import numpy as np

### ZINK

sgZink10 = np.array([0.4470, 0.4483, 0.4369, 0.4319])
sgZink10t = np.array([0.1977, 0.1830, 0.1913, 0.1935])

print('Graphsagetest', np.mean(sgZink10), np.std(sgZink10))
print('train', np.mean(sgZink10t), np.std(sgZink10t))
print('')

sgZink10 = np.array([0.4651, 0.4652, 0.4662, 0.4678])
sgZink10t = np.array([0.3169, .3457, .3234, .3303])
print('GATtest', np.mean(sgZink10), np.std(sgZink10))
print('GATtrain', np.mean(sgZink10t), np.std(sgZink10t))
print("")

gatedgcnZink10 = np.array([0.4122, 0.4067, 0.4161, 0.4260])
gatedgcnZink10t = np.array([0.3054, .3152, .3129, .3286])
print('gatedgcntest4', np.mean(gatedgcnZink10), np.std(gatedgcnZink10))
print('gatedgcntrain4', np.mean(gatedgcnZink10t), np.std(gatedgcnZink10t))
print("")

gatedgcnZink10 = np.array([0.4151, 0.4193, 0.4042, 0.4157])
gatedgcnZink10t = np.array([0.3168, .3230, .3025, .3188])
print('gatedgcntest5', np.mean(gatedgcnZink10), np.std(gatedgcnZink10))
print('gatedgcntrain5', np.mean(gatedgcnZink10t), np.std(gatedgcnZink10t))
print("")

gatedgcnZink10 = np.array([0.4040, 0.4036, 0.4044, 0.4035])
gatedgcnZink10t = np.array([0.2945, .2983, .3015, .2880])
print('gatedgcntest6', np.mean(gatedgcnZink10), np.std(gatedgcnZink10))
print('gatedgcntrain6', np.mean(gatedgcnZink10t), np.std(gatedgcnZink10t))
print("")

gatedgcnZink10 = np.array([0.3996, 0.3997, 0.3979, 0.3961])
gatedgcnZink10t = np.array([0.2849, .2797, .2990, .2806])
print('gatedgcntest7', np.mean(gatedgcnZink10), np.std(gatedgcnZink10))
print('gatedgcntrain7', np.mean(gatedgcnZink10t), np.std(gatedgcnZink10t))
print("")

tcifar10 = np.array([68.22, 68.46, 69.21, 69.32])
tcifar10t = np.array([89.97, 89.57, 89.86, 89.98])
print('gatedgcncf4', np.mean(tcifar10), np.std(tcifar10))
print('gatedgcncf4', np.mean(tcifar10t), np.std(tcifar10t))
print("")

tcifar10 = np.array([66.23, 65.89, 65.76, 65.98])
tcifar10t = np.array([83.88, 83.78, 86.09, 83.78])
print('gatncf4', np.mean(tcifar10), np.std(tcifar10))
print('gatncf4', np.mean(tcifar10t), np.std(tcifar10t))
print("")


tcifar10 = np.array([72.2, 71.31, 71.35, 71.48])
tcifar10t = np.array([85.45, 84.39, 82.42, 83.25])
print('gatedgcncf1', np.mean(tcifar10), np.std(tcifar10))
print('gatedgcncf1', np.mean(tcifar10t), np.std(tcifar10t))
print("")



tcifar10 = np.array([71.72, 71.86, 72.24, 71.93])
tcifar10t = np.array([87.63, 87.30, 87.10, 87.86])
print('gatedgcncf1', np.mean(tcifar10), np.std(tcifar10))
print('gatedgcncf1', np.mean(tcifar10t), np.std(tcifar10t))
print("")

tcifar10 = np.array([70.82, 71.26, 72.01, 71.44])
tcifar10t = np.array([88.78, 85.30, 88.10, 86.40])
print('gatedgcncf2', np.mean(tcifar10), np.std(tcifar10))
print('gatedgcncf2', np.mean(tcifar10t), np.std(tcifar10t))
print("")

tcifar10 = np.array([71.39, 70.55, 70.79, 70.92])
tcifar10t = np.array([90.06, 86.58, 90.67, 87.27])
print('gatedgcncf2', np.mean(tcifar10), np.std(tcifar10))
print('gatedgcncf2', np.mean(tcifar10t), np.std(tcifar10t))
print("")


tmnist = np.array([97.75, 97.85, 98.07, 98.10])
tmnistt = np.array([99.998, 99.998, 99.994, 99.995])
print('gatedgcnmnist5', np.mean(tmnist), np.std(tmnist))
print('gatedgcnmnist5', np.mean(tmnistt), np.std(tmnistt))
print("")

tmnist = np.array([98.03, 97.94, 97.82, 97.96])
tmnistt = np.array([99.994, 99.998, 99.995, 99.996])
print('gatedgcnmnist5', np.mean(tmnist), np.std(tmnist))
print('gatedgcnmnist5', np.mean(tmnistt), np.std(tmnistt))
print("")


tmnist = np.array([97.71, 97.79, 97.99, 97.90])
tmnistt = np.array([99.904, 99.833, 99.927, 99.893])
print('gatedgcnmnist5', np.mean(tmnist), np.std(tmnist))
print('gatedgcnmnist5', np.mean(tmnistt), np.std(tmnistt))
print("")


tmnist = np.array([97.67, 97.64, 97.93, 97.68])
tmnistt = np.array([99.982, 99.973, 99.973, 99.973])
print('gatedgcnmnist5', np.mean(tmnist), np.std(tmnist))
print('gatedgcnmnist5', np.mean(tmnistt), np.std(tmnistt))
print("")


tmnist = np.array([98.03, 97.98, 97.94, 97.99])
tmnistt = np.array([99.998, 99.994, 99.996, 99.995])
print('gatedgcnmnist5', np.mean(tmnist), np.std(tmnist))
print('gatedgcnmnist5', np.mean(tmnistt), np.std(tmnistt))
print("")


tmnist = np.array([97.73, 97.61, 97.75, 97.72])
tmnistt = np.array([99.993, 99.996, 99.998, 99.998])
print('gatedgcnmnist5', np.mean(tmnist), np.std(tmnist))
print('gatedgcnmnist5', np.mean(tmnistt), np.std(tmnistt))
print("")
