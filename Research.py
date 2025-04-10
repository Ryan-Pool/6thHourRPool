import numpy as np
import matplotlib.pyplot as plt
import torch
import torch.nn as nn


x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)


plt.plot(x, y)
plt.title("This is the wave we want to teach!")
plt.show()


class TinyBrain(nn.Module):
    def __init__(self):
        super().__init__()
        self.model = nn.Sequential(
            nn.Linear(1, 10),
            nn.Tanh(),
            nn.Linear(10, 1)
        )

    def forward(self, x):
        return self.modelf(x)

brain = TinyBrain()

x_train = torch.tensor(x.reshape(-1, 1), dtype=torch.float32)
y_train = torch.tensor(y.reshape(-1, 1), dtype=torch.float32)

loss_function = nn.MSELoss()

optimizer = torch.optim.Adam(brain.parameters(), lr=0.01)

for epoch in range(1000):
    prediction = brain(x_train)
    loss = loss_function(prediction, y_train)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if epoch % 100 == 0:
        print(f"Epoch {epoch} - Loss: {loss.item()}")


with torch.no_grad():
    y_pred = brain(x_train).numpy()

plt.figure(figsize=(10, 5))
plt.plot(x, y, label='True wave')
plt.plot(x, y_pred, label='Robots learned wave', linestyle='--')
plt.legend()
plt.title("Did the robot learn the wave?")
plt.xlabel("x")
plt.ylabel("wave height")
plt.grid(True)
plt.show()