"""A densely connected neural netowrk"""

import torch
from torch import nn
from torch.nn import Parameter
from torch import Tensor


class DenseLayer(nn.Module):
    """A densely connected neural netowrk
    Equavilant to torch.nn.Linear(in_features=m, out_features=2)
    Args:
        input_dim: #inputs
        output_dim: #out_puts
    """

    def __init__(self, input_dim: int, output_dim: int):
        """Init method

        Args:
            input_dim (int): _description_
            output_dim (int): _description_
        """
        super().__init__()

        # initialize weight and bias
        self.weights: Parameter = Parameter(
            torch.randn(input_dim, output_dim, requires_grad=True)
        )
        self.b = Parameter(torch.randn(1, output_dim, requires_grad=True))

    def forward(self, inputs: Tensor) -> Tensor:
        """The Forward path of the network

        Args:
            inputs (Tensor): _description_

        Returns:
            Tensor: result of the transform
        """
        # Forward propagate the inputs
        z: Tensor = torch.matmul(inputs, self.weights) + self.b

        output: Tensor = torch.sigmoid(z)
        return output
