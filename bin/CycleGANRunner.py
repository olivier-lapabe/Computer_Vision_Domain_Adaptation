import torch
import time
import os
from src.solvers.CycleGANSolver import CycleGANSolver
from src.Common.utils import mnist_loader, svhn_loader


# Define parameters
batch_size = 50 # Batchs size of Dataloader for gradient descent
num_epochs = 100
loss_cycle_weight = 10
num_gen_training = 2
path = f"savedmodels/CycleGAN/newsolver/epochs_{num_epochs}_weight_{loss_cycle_weight}_gen_{num_gen_training}"

if __name__ == "__main__":
    start_time = time.time()

    # Ensure the save directory exists
    os.makedirs(path, exist_ok=True)

    # Load SVHN and MNIST datasets
    dataloader_S_train, dataloader_S_test = svhn_loader(batch_size)
    dataloader_M_train, dataloader_M_test = mnist_loader(batch_size)

   # Initialize CycleGAN model
    cycleGAN = CycleGANSolver(loss_cycle_weight=loss_cycle_weight)
    print(f"Using device {cycleGAN.device}")
    cycleGAN = cycleGAN.to(cycleGAN.device)
    
    # Train
    print('Training starts')
    cycleGAN_trained = cycleGAN.train_cycle_GAN(dataloader_S_train, dataloader_M_train, dataloader_S_test, num_epochs, num_gen_training, path)

    # Save trained model
    torch.save(cycleGAN.G_SM.state_dict(), os.path.join(path, 'G_SM_model.pth'))
    torch.save(cycleGAN.G_MS.state_dict(), os.path.join(path, 'G_MS_model.pth'))

    end_time = time.time()
    duration = end_time - start_time
    print(f"The process took {duration/60} minutes to complete.")