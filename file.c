#include <stdio.h>

int main() {  
  FILE *fptr;
  int c, stock;
  char buffer[200], item[10];
  float price;

  
  fptr = fopen("myfile.txt", "r");

  fgets(buffer, 20, fptr);    
  printf("%s\n", buffer);

  fscanf(fptr, "%d%s%f", &stock, item, &price); 
  printf("%d  %s  %4.2f\n", stock, item, price);

  while ((c = getc(fptr)) != EOF)
    printf("%c", c);

  fclose(fptr);
  return 0;
}