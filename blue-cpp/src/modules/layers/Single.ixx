// Copyright 2025 by Amir Nourinia

module;
#include <torch/torch.h>
export module Layer:Single;

export namespace blue {
class Single final: public torch::nn::Module {
 public:
  Single(size_t const input_count, size_t const hidden_count, size_t const output_count) {
    // Construct and register two Linear submodules.
    fc1 = register_module("fc1", torch::nn::Linear(input_count, hidden_count));
    fc2 = register_module("fc2", torch::nn::Linear(hidden_count, output_count));
  }
  // Implement the Net's algorithm.
  torch::Tensor forward(torch::Tensor x) {
    // Use one of many tensor manipulation functions.
    x = torch::sigmoid(fc1->forward(x.reshape({x.size(0), 784})));
    x = torch::dropout(x, /*p=*/0.5, /*train=*/is_training());
    // x = torch::sigmoid(fc2->forward(x), );
    // x = torch::log_softmax(fc3->forward(x), /*dim=*/1);
    return x;
  }

  // Use one of many "standard library" modules.
  torch::nn::Linear fc1{nullptr};
  torch::nn::Linear fc2{nullptr};
};
}  // namespace blue