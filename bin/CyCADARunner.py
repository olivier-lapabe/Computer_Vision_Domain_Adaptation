import torch
import os
import time
import matplotlib.pyplot as plt
from src.solvers.CyCADASolver import CyCADASolver
from src.Common.utils import svhn_loader, mnist_loader

# Hyperparameters
batch_size_stepA = 128
batch_size_stepB = 128
num_epochs_stepA = 100
num_epochs_stepB = 100
lr_stepA = 0.0001
lr_stepB = 0.00001

# Training and saving parameters
stepA = True
stepB = True
path = "savedmodels/CyCADA_MNIST-to-SVHN/"
data_augment_source = False


# -----------------------------------------------------------------------------
# stepA_runner
# -----------------------------------------------------------------------------
def stepA_runner(CyCADAClassifier, batch_size_stepA, num_epochs_stepA, path=False):
    # Load SVHN dataset
    dataloader_S_train, dataloader_S_test = mnist_loader(batch_size_stepA)

    # Train and Test over epochs
    for epoch in range(num_epochs_stepA):
        CyCADAClassifier.train_stepA(epoch, dataloader_S_train)
        CyCADAClassifier.test_stepA(epoch, dataloader_S_test)
    
    # Save CyCADAClassifier.F_S model
    if path != False:
        os.makedirs(path, exist_ok=True)
        torch.save(CyCADAClassifier.F_S.state_dict(), os.path.join(path, 'F_S_model.pth'))


# -----------------------------------------------------------------------------
# stepB_runner
# -----------------------------------------------------------------------------
def stepB_runner(CyCADAClassifier, batch_size_stepB, num_epochs_stepB, path=False):
    # Load SVHN and MNIST datasets
    dataloader_S_train, _ = mnist_loader(batch_size_stepB)
    dataloader_T_train, dataloader_T_test = svhn_loader(batch_size_stepB)

    # Train and Test over epochs
    for epoch in range(num_epochs_stepB):
        CyCADAClassifier.train_stepB(epoch, dataloader_S_train, dataloader_T_train)
        CyCADAClassifier.test_stepB(epoch, dataloader_T_test)
    
    # save CyCADAClassifier.F_T and CyCADAClassifier.G_ST models
    if path != False:
        os.makedirs(path, exist_ok=True)
        torch.save(CyCADAClassifier.F_T.state_dict(), os.path.join(path, 'F_T_model.pth'))
        torch.save(CyCADAClassifier.G_ST.state_dict(), os.path.join(path, 'G_ST_model.pth'))


# -----------------------------------------------------------------------------
# main
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    start_time = time.time()

    CyCADAClassifier = CyCADASolver(lr_stepA=lr_stepA,lr_stepB=lr_stepB, path=path, data_augment_source=data_augment_source)
    print(f"Using device {CyCADAClassifier.device}")
    CyCADAClassifier = CyCADAClassifier.to(CyCADAClassifier.device)

    # Step A - Train F_S
    if stepA:
        stepA_runner(CyCADAClassifier, batch_size_stepA, num_epochs_stepA, path)

    # Step B - Train G_ST, G_TS, D_S, D_T, D_feat, F_T (F_S fix)
    if stepB:
        CyCADAClassifier.F_S.load_state_dict(torch.load(os.path.join(path, 'F_S_model.pth'), map_location=CyCADAClassifier.device))
        stepB_runner(CyCADAClassifier, batch_size_stepB, num_epochs_stepB, path)

    end_time = time.time()
    duration = end_time - start_time
    print(f"The process took {duration/60} minutes to complete.")
