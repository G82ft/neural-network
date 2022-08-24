#include <iostream>
#include <vector>

#include "matrix.cpp"

using std::vector;

template <typename T>
Matrix<T> ReLU(Matrix<T> matrix) {
  Matrix<T> activated = matrix;

  for (int i = 0; i < activated.height(); i++) {
    for (int j = 0; j < activated.width(); j++) {
      if (activated[i][j] < 0) {
        activated[i][j] = 0;
      }
    }
  }

  return activated;
}


class NeuralNetwork {
  public:
    NeuralNetwork(vector<Matrix<float>> layers, vector<Matrix<float>> biases) {
      this->layers = layers;
      this->biases = biases;
    }

    Matrix<float> getOutput(Matrix<float> input) {
      Matrix<float> layer = input;

      for (int L = 0; L < layers.size(); L++) {
        layer = ReLU<float>(layers[L] * layer + biases[L]);
      }

      return layer;
    }

  private:
    vector<Matrix<float>> layers;
    vector<Matrix<float>> biases;
};
