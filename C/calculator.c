// Create a calculator that can add, subtract, multiply, and divide

#include <stdio.h>
int main()
{
    int a, b, sum, sub, mul, div;
    printf("Enter the first number: ");
    scanf("%d", &a);
    printf("Enter the second number: ");
    scanf("%d", &b);
    sum = a + b;
    sub = a - b;
    mul = a * b;
    div = a / b;
    printf("%d + %d = %d\n", a, b, sum);
    printf("%d - %d = %d\n", a, b, sub);
    printf("%d * %d = %d\n", a, b, mul);
    printf("%d / %d = %d\n", a, b, div);
    return 0;
}