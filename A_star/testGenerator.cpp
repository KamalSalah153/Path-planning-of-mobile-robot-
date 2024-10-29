/*#include <bits/stdc++.h>
using namespace std;
int main() {
    const int rows = 25;
    const int cols = 50;

    // Create a random number generator
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_real_distribution<> dis(0.0, 1.0);

    // Create a 2D array and initialize it
    char array2D[rows][cols];
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j) {
            if (dis(gen) <= 0.7)
                array2D[i][j] = '.';
            else
                array2D[i][j] = '#';
        }
    }

    // Save the array to a text file
    string name = "";
    name += to_string(rows);
    name += "x";
    name += to_string(cols);
    name += ".txt";
    std::ofstream outputFile(name);
    if (!outputFile.is_open()) {
        std::cout << "Failed to open the output file." << std::endl;
        return 0;
    }
    outputFile << rows << " " << cols << endl;
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j) {
            if (i == 0 && j == 0)outputFile << 'S';
            else if (i == rows - 1 && j == cols - 1)outputFile << 'E';
            else outputFile << array2D[i][j];
        }
        outputFile << std::endl;
    }

    outputFile.close();
    std::cout << "Output file created successfully." << std::endl;

    return 0;
}
*/