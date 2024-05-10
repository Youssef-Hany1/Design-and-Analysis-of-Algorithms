#include <iostream>
#include <cmath>
using namespace std;

int totalMoves = 0; // Global variable to keep track of total moves

void towerOfHanoi3Rods(int m, char fromRod, char toRod, char auxRod) {
    if (m == 1) {
        cout << "Move disk 1 from rod " << fromRod << " to rod " << toRod << endl;
        totalMoves++;
        return;
    }
    towerOfHanoi3Rods(m - 1, fromRod, auxRod, toRod);
    cout << "Move disk " << m << " from rod " << fromRod << " to rod " << toRod << endl;
    totalMoves++;
    towerOfHanoi3Rods(m - 1, auxRod, toRod, fromRod);
}

void towerOfHanoi4Rods(int n, char rod1, char rod2, char rod3, char rod4) {
    if (n == 0)
        return;
    if (n == 1) {
        cout << "Move disk 1 from rod " << rod1 << " to rod " << rod2 << endl;
        totalMoves++;
        return;
    }

    towerOfHanoi4Rods(n - 2, rod1, rod3, rod4, rod2);

    cout << "Move disk " << n << " from rod " << rod1 << " to rod " << rod4 << endl;
    cout << "Move disk " << n << " from rod " << rod1 << " to rod " << rod2 << endl;
    cout << "Move disk " << n << " from rod " << rod4 << " to rod " << rod2 << endl;
    totalMoves += 3;

    towerOfHanoi4Rods(n - 2, rod3, rod2, rod1, rod4);
}

void towerOfHanoiThirdMethod(int start, int end, char rodA, char rodB, char rodC, char rodD) {
    int disks = end - start + 1;
    int k = sqrt(2 * disks); // Calculating k
    towerOfHanoi4Rods(disks - k, rodA, rodD, rodB, rodC);
    towerOfHanoi3Rods(k, rodA, rodB, rodC);
    towerOfHanoi4Rods(disks - k, rodD, rodB, rodA, rodC);
}

int main() {
    int n = 8;

    cout << "\n---------------Tower of Hanoi in 33 moves --------------\n" << endl;
    towerOfHanoiThirdMethod(1, n, 'A', 'B', 'C', 'D');
    cout << "\nTotal moves: " << totalMoves << endl;
    return 0;
}



