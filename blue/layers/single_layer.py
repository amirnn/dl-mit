"""A single (hiddn) layer NN"""

from torch.nn import Module
from torch import Tensor
from blue.layers.dense_layer import DenseLayer


class SingleLayer(Module):
    """A single (hiddn) layer NN
    equavilant to:
    model = nn.Sequential(
        nn.Linear(m,n),
        nn.ReLU(),
        nn.linear(n,2)
    )
    """

    def __init__(self, input_dim: int, hidden_dim: int, output_dim: int):
        super().__init__()
        self.hidden_layer = DenseLayer(input_dim=input_dim, output_dim=hidden_dim)
        self.out_layer = DenseLayer(input_dim=hidden_dim, output_dim=output_dim)

    def forward(self, inputs: Tensor) -> Tensor:
        """forward path of the single (hidden) layer NN
        Args:
            inputs (Tensor): inputs
        Returns:
            Tensor: result of transform
        """
        z = self.hidden_layer.forward(inputs=inputs)
        return self.out_layer.forward(z)
