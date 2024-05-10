#include <iostream>
using namespace std;

int totalMoves = 0; // Global variable to keep track of total moves

void moveDisk(int disk, char source, char destination) {
    cout << "Move disk " << disk << " from rod " << source << " to rod " << destination << endl;
    totalMoves++; // Increment total moves
}

void towerOfHanoi4Pegs(int n, char source, char destination, char auxiliary1, char auxiliary2) {
    if (n <= 0) {
        return;
    } else if (n == 1) {
        moveDisk(1, source, destination);
        return;
    }

    // Move top n-2 disks to auxiliary1 using auxiliary2 and destination
    towerOfHanoi4Pegs(n - 2, source, auxiliary1, auxiliary2, destination);

    // Move remaining 2 disks to destination using auxiliary2
    moveDisk(n - 1, source, auxiliary2);
    moveDisk(n, source, destination);
    moveDisk(n - 1, auxiliary2, destination);

    // Move top n-2 disks to destination using auxiliary1 and source
    towerOfHanoi4Pegs(n - 2, auxiliary1, destination, source, auxiliary2);
}

int main() {
    int N = 8; // Number of disks
    char A = 'A', B = 'B', C = 'C', D = 'D'; // Pegs
    towerOfHanoi4Pegs(N, A, D, B, C); // A: source, D: destination, B, C: auxiliary
    cout << "\nTotal moves: " << totalMoves << endl; // Output total moves
    return 0;
}

