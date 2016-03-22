//
//  main.c
//  hw5
//
//  Created by Zachary King on 2/8/16.
//  Copyright © 2016 Zachary King. All rights reserved.
//

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>


int frobcmp(const char* a,const char* b)
{
    //initializations
    int len1 = 0;
    int len2 = 0;
    
    //find the length of the first char string
    for(int i = 0; a[i] != ' ';i++)
    {
        len1++;
    }
    
    //find the length of the second char string
    for(int i = 0; b[i] != ' ';i++)
    {
        len2++;
    }
    
    //unfrob print for debugging purposes
    /*
    printf("First Input String(uf): ");
    for(int i = 0; i < len1; i++)
    {
        printf("%c",(a[i]^42));
    }
    printf("\nSecond Input String:(uf): ");
    for(int i = 0; i < len2; i++)
    {
        printf("%c",(b[i]^42));
    }
    printf("\nLength of a: %d\n",len1);
    printf("Length of b: %d\n",len2);
    */

    //find the minimum of the two lengths
    int lenmin = 0;
    if (len1 > len2)
    {
        lenmin = len2;
    }
    else
    {
        lenmin = len1;
    }
    //printf("minlength = %d\n",lenmin);
    
    
    //compare loop
    for(int i = 0; i < lenmin; i++)
    {
        char cha = a[i]^42;
        char chb = b[i]^42;
        if(cha > chb)
        {
            return 1;
        }
        else if (cha < chb)
        {
            return -1;
        }
        else
        {
            continue;
        }
    }
    if (lenmin == len1 && lenmin == len2)
    {
        return 0;
    }
    else if (len1 > lenmin)
    {
        return 1;
    }
    else
    {
        return -1;
    }
    
    return 0;
}

int wrapper(const void* v1,const void* v2)
{
    const char* aa = *(const char**)v1;
    const char* bb = *(const char**)v2;
    return frobcmp(aa,bb);
}

int main()
{
    //initialize
    char* input = malloc(1);
    long ccount = 0;
    long wcount = 0;
    
    //initialize file read
    char ch = getchar();
    if (ch == EOF)
        exit(1);
    while (ch != EOF)
    {

        ccount++;
        input = realloc(input,sizeof(char) * ccount);
        if (input == 0)
        {
            fputs("Error Allocating Memory", stderr);
            exit(1);
        }
        input[ccount-1] = ch;
        if (ch == ' ')
        {
            
            wcount++;
        }
        ch = getchar();
    }

    if (input[ccount-1] != ' ')
    {
        ccount++;
        wcount++;
        input = realloc(input,sizeof(char) * ccount);
        if (input == 0)
        {
            fputs("Error Allocating Memory", stderr);
            exit(1);
        }
        input[ccount-1] = ' ';
    }
    /*
    printf("wordcount = %d \n",(int)wcount);
    for (int i = 0; i < ccount; i++)
    {
        printf("%c",input[i]);
    }
    printf("\n");
    */
    
    char** words = 0;
    words = (char**) malloc(sizeof(char*) * wcount);
    if (words == 0)
    {
        fputs("Error Allocating Memory", stderr);
        exit(1);
    }
    long wloc = 0;
    long cword = 0;
    
    for(int i = 0; i < ccount; i++)
    {
        if (wloc == 0)
        {
            words[cword] = malloc(sizeof(char));
            if (words[cword] == 0)
            {
                fputs("Error Allocating Memory", stderr);
                exit(1);
            }
        }
        else
        {
            words[cword] = realloc(words[cword],sizeof(char) * (wloc + 1));
            if (words[cword] == 0)
            {
                fputs("Error Allocating Memory", stderr);
                exit(1);
            }
        }
        
        words[cword][wloc] = input[i];
        wloc++;
        if(input[i] == ' ')
        {
            cword++;
            wloc = 0;
        }
    }
    
    qsort(words, wcount,sizeof(char*),wrapper);
    /*
    for(int i=0; i< wcount; i++)
    {
        printf("word #%d at address%p: ",i,words[i]);
        int j = 0;
        while (words[i][j] != ' ')
        {
            printf("%c",words[i][j]^42);
            j++;
        }
        printf(" (done)\n");
    }
    */
    for (int i = 0; i < wcount; i++)
    {
        int j = 0;
        while(words[i][j] != ' ')
        {
            putchar(words[i][j]);
            j++;
        }
        putchar(words[i][j]);
    }
    for (int i = 0; i < wcount; i++)
    {
        free(words[i]);
    }
    free(words);
    exit(0);
}

