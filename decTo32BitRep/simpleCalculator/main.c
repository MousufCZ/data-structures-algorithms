#include <stdio.h>
#include "calculator.h"

int main(){
    char operator;
    double num1, num2, result;

    printf("Enter an operator (+, -, *, /): ");
    scanf(" %c", &operator);
    // printf("Selected: ", &operator);

    printf("Enter two operands: ");
    scanf("%lf %lf", &num1, &num2);

    return 0;
}