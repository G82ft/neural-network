#include <iostream>
#include <vector>

using std::vector;


template <typename T>
T multiplyRows(vector<T> first, vector<T> second) {
  T res = 0;
  
  for (int i = 0; i < first.size(); i++) {
    res += first[i] * second[i];
  }
  
  return res;
}


template <typename T>
class Matrix {
  public:
    Matrix(vector<vector<T>> rows) {
      this->rows = rows;
    }

    vector<T>& operator[](int index) {
      return rows[index];
    }

    friend std::ostream& operator<<(std::ostream &stream, Matrix m) {
      for (int i = 0; i < m.height(); i++) {
        stream << "[ ";
        for (int j = 0; j < m.width(); j++) {
          stream << m.rows[i][j] << " ";
        }
        stream << "]\n";
      }

      return stream;
    }

    Matrix operator+(Matrix other) {
      Matrix matrix = other;

      for (int row = 0; row < matrix.height(); row++) {
        for (int col = 0; col < matrix.width(); col++) {
          matrix[row][col] = rows[row][col] + other[row][col];
        }
      }
      
      return matrix;
    }
    
    Matrix operator-(Matrix other) {
      Matrix matrix = other;

      for (int row = 0; row < matrix.height(); row++) {
        for (int col = 0; col < matrix.width(); col++) {
          matrix[row][col] = rows[row][col] - other[row][col];
        }
      }
      
      return matrix;
    }
    
    Matrix operator*(Matrix other) {
      Matrix otherRows = other.rows;
      Matrix matrix(otherRows);
      matrix.getTransposed();
      for (int row = 0; row < matrix.height(); row++) {
        for (int col = 0; col < matrix.width(); col++) {
          matrix[row][col] = multiplyRows<T>(
              this->rows[row], other.getTransposed()[col]
            );
        }
      }
      
      return matrix;
    }
    
    Matrix operator*(int other) {
      Matrix matrix(this->rows);
      
      for (int row = 0; row < matrix.height(); row++) {
        for (int col = 0; col < matrix.width(); col++) {
          matrix[row][col] *= other;
        }
      }
      
      return matrix;
    }
    
    Matrix getTransposed() {
      vector<vector<T>> transposedRows = rows;

      transposedRows.resize(width());
      for (int i = 0; i < width(); i++) {
        transposedRows[i].resize(height());
      }
      Matrix transposed(transposedRows);

      for (int i = 0; i < height(); i++) {
        for (int j = 0; j < width(); j++) {
          transposed[j][i] = rows[i][j];
        }
      }

      return transposed;
    }

    int height() {
      return rows.size();
    }
    
    int width() {
      return rows[0].size();
    }
    
    bool isSquare() {
      return height() == width();
    }
    

  private:
    vector<vector<T>> rows;
};
