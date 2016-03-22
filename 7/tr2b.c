#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

int main(int argc, char** argv)
{
  //Check for correct number of arguments
  if (argc != 3)
  {
    printf("This program requires 3 arguments \n");
    exit(1);
  }
  char* a1 = argv[1];
  char* a2 = argv[2];
  //Check for Same Length
  if (strlen(a2) != strlen(a1))
  {
    printf("The two arguments are not the same length \n");
    exit(2);
  }
  //Check for duplicates
  int i,j;
  long arglen = strlen(a1);
  for(i = 0; i < arglen; i++)
  {
    for(j = 0; j < arglen; j++)
    {
      if (j == i)
	continue;
      else if (a1[i] == a1[j])
      {
	printf("There cannot be duplicates in the first argument");
	exit(3);
      }
	  
    }
  }
  //Run the Translation
  char c = getchar();
  while (c != EOF)
  {
    int found = 0;
    for(i = 0; i < arglen; i++)
    {
      if (a1[i] == c)
      {
	putchar(a2[i]);
	found = 1;
	break;
      }
 
    }
    if (found == 0)
    {
      putchar(c);
    }
    c = getchar();
  }
  
}
