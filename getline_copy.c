/*
 * ===========================================================================
 *
 *         Author:  Ming Chen, v.mingchen@gmail.com
 *        Created:  05/02/2014 08:30:49 PM
 *
 *    Description:  
 *
 * ===========================================================================
 */

#include <stdio.h>
#define MAXLINE 1000

int getLine(char s[], int lim);
void copy(char from[], char to[]);

int main(){
	char line[MAXLINE];
	char maxline[MAXLINE];
	int maxlen = 0;
	int len;
	while((len = getLine(line, MAXLINE)) > 0){
			if(len > maxlen){
				maxlen = len;
				copy(line,maxline); 
			}
	}
	printf("max length is %d.", maxlen);
	printf("%s", maxline);
	return 0;
}

//getline() is used to read and save a line to s[] and return its length
int getLine(char s[], int lim){
/*int getLine(char *s, int lim){*/
	int i;
	char c;
	for(i=0; (i<lim-1) && (c=getchar() != EOF) && (c!='\n'); i++){ 
		s[i] = c;//s[] can be changed  why?
	}
	if(c == '\n'){
		s[i] = c;
		i++;
	}
	s[i] = '\0';
	return i;
}

void copy(char from[], char to[]){
	int i;
	for(i=0; from[i] != '\0'; i++){
		to[i] = from[i];
	}
	to[i] = '\0';
}

	
