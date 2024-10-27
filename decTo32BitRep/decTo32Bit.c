#include <stdint.h>  // Include the header for fixed-width integer types
#include <string.h>  // Include the header for memcpy
#include <stdio.h>   // Include the header for printf
// https://cs.stackexchange.com/questions/21312/problem-in-finding-the-floating-point-representation
// Day 1: Working on C tutorial on Geek For Geeks [26th - 27th October]
uint32_t float_to_binary(float num) {
    uint32_t result;
    memcpy(&result, &num, sizeof(result));  // Copy the raw bytes of the float 'num' into 'result'
    return result;
}

int main() {
    float num = 10.75;
    uint32_t binary_rep = float_to_binary(num);
    printf("Binary representation: 0x%X\n", binary_rep);  // Print the binary representation of 'num' in hexadecimal format
    return 0;
}
