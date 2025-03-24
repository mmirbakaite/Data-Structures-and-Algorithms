#include <iostream>

using namespace std;

// suranda max sk
int getMax(int arr[], int n) {
    int max = arr[0];
    for (int i = 1; i < n; i++)
        if (arr[i] > max)
            max = arr[i];
    return max;
}

// lygina skaiciu skaitmenis
void countingSort(int arr[], int dydis, int vieta) {
    
    // max elem sk., rezulatatu saugojimas, skaiciu paasikartojimu saugojimas
    const int max = 10;
    int* output = new int[dydis];
    int* kiekis = new int[max];

    // pradzioje visi skaièiø pasikartojimø kiekiai nuliniai
    for (int i = 0; i < max; ++i)
        kiekis[i] = 0;

    // suskaiciuojam skaitmenu pasikartojima
    for (int i = 0; i < dydis; i++)
        kiekis[(arr[i] / vieta) % 10]++;

    //susumuojame kieki
    for (int i = 1; i < max; i++)
        kiekis[i] += kiekis[i - 1];

    // perstumia á rezultatø masyvà pagal jø skaitmenis
    for (int i = dydis - 1; i >= 0; i--) {
        output[kiekis[(arr[i] / vieta) % 10] - 1] = arr[i];
        kiekis[(arr[i] / vieta) % 10]--;
    }

    // kopijuoja rûðiuotus elementus ið output masyvo atgal á pradiná arr masyvà
    for (int i = 0; i < dydis; i++)
        arr[i] = output[i];

    // atlaisvinam atminti
    delete[] output;
    delete[] kiekis;
}

// lygina skaicius pasinaudojant skaiciu skaitmenu lyginimu
void radixSort(int arr[], int dydis) {

    // max sk kiekvienoje iteracijoje
    int max = getMax(arr, dydis);

    for (int vieta = 1; max / vieta > 0; vieta *= 10)
        countingSort(arr, dydis, vieta);
}

// isspausdinamas masyvas
void printArray(int arr[], int dydis) {
    for (int i = 0; i < dydis; i++)
        cout << arr[i] << " ";
    cout << endl;
}

int main() {
    int n;
    cout << "Iveskite masyvo dydi: ";
    cin >> n;

    int* arr = new int[n];
    cout << "Iveskite masyvo elementus: ";
    for (int i = 0; i < n; i++)
        cin >> arr[i];

    radixSort(arr, n);
    printArray(arr, n);

    delete[] arr;

    return 0;
}

