/*

 #-----------------------------------------------------------------------------
 # Krypto Solver 
 # $Revision: 1.8 $
 # $Date: 2002/03/15 06:45:01 $
 #-----------------------------------------------------------------------------

 * Marcus Kazmierczak, marcus@mkaz.com
 * http://mkaz.com/math/krypto/
 * Created On: March 12, 2002
 
 * Permutation Routine unknowingly supplied by Terry R. McConnell 
 * from the site: http://barnyard.syr.edu/quickies/perms.c 

*/

#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>
#include <math.h>


/* ----------------------------------------------------------------------------- */

int operate(int a, int b, char o);

#define GS  5           /* Game Size */
#define GSF 120         /* Total Game Permutations: GS! */
#define NOPS 4          /* Number of operator types [+,-,*,/] */
#define CH 4            /* How many operators we need: GS-1 */
#define OPLOOP 256      /* pow(NOPS,CH) */
#define NAS 14          /* Number of Answers in Array (Parentheses) */

/* ----------------------------------------------------------------------------- */

static int p[GS];       /* global array to hold generated permutation */
static int lvl = -1;    /* The level of recursion */
static int poa[GSF][GS];   /* multiple array to hold game permutations */
char ops[OPLOOP][GS];      /* multiple array to hold operation permuations */
int row = 0;

/* ----------------------------------------------------------------------------- */

int main(int argc, char *argv[])
{
    int g[GS], x[GS];
    int i,j,oi,oj;
    char aops[NOPS];

    int ans[NAS];
    int reg1, reg2, reg3;
    int s, count=0;
    
    printf("Krypto Solver\n");
    printf("by Marcus Kazmierczak\n\n");
    
    aops[0] = '+'; aops[1] = '-'; aops[2] = '*'; aops[3] = '/';

/*== GET INPUT ==*/        
    /*= verify valid input =*/
    if (argc != 7) { printf("USAGE: solver x1 x2 x3 x4 x5 s1\n"); exit(1); }
    
    for (i=0; i < GS; i++) { g[i] = atoi(argv[i+1]);  }
    s = atoi(argv[6]);
    

    
    /*= generate order arrays =*/   
    permute(1);
    choose(aops);
    
    /*= loop through all game permutations =*/
    for (i=0; i < GSF; i++) 
    {
    	/*== zero out answers ==*/
    	for(j=0; j < NAS; j++) ans[j] = 0;
    	
        /*= loop through order operations =*/
    	for (oi=0; oi < OPLOOP; oi++)
    	{
    		for(j=0; j < GS; j++) { x[j] = g[poa[i][j]-1]; }
    		
            /*== Paren Case  0: (((x0 @ x1) @ x2 ) @ x3) @ x4 =*/
            reg1 = operate(x[0], x[1], ops[oi][1]);
            reg2 = operate(reg1, x[2], ops[oi][2]);
            reg3 = operate(reg2, x[3], ops[oi][3]);
            if ((reg1 == -99999) || (reg2 == -99999) || (reg3 == -99999)) { ans[0] = -99999; }
            else { ans[0] = operate(reg3, x[4], ops[oi][4]); }

            /*== Paren Case  1: ((x0 @ x1) @ x2) @ (x3 @ x4) =*/
            reg1 = operate(x[0], x[1], ops[oi][1]);
            reg2 = operate(reg1, x[2], ops[oi][2]);
            reg3 = operate(x[3], x[4], ops[oi][4]);
            if ((reg1 == -99999) || (reg2 == -99999) || (reg3 == -99999)) { ans[1] = -99999;  }
            else { ans[1] = operate(reg2, reg3, ops[oi][3]); }

            /*== Paren Case  2: ((x0 @ x1) @ (x2 @ x3)) @ x4 =*/
            reg1 = operate(x[0], x[1], ops[oi][1]);
            reg2 = operate(x[2], x[3], ops[oi][3]);
            reg3 = operate(reg1, reg2, ops[oi][2]);
            if ((reg1 == -99999) || (reg2 == -99999) || (reg3 == -99999)) { ans[2] == -99999;  }
            else { ans[2] = operate(reg3, x[4], ops[oi][4]); }

            /*== Paren Case  3: (x0 @ x1) @ (x2 @ (x3 @ x4)) =*/
            reg1 = operate(x[0], x[1], ops[oi][1]);
            reg2 = operate(x[3], x[4], ops[oi][4]);
            reg3 = operate(x[2], reg2, ops[oi][3]);
            if ((reg1 == -99999) || (reg2 == -99999) || (reg3 == -99999)) { ans[3] = -99999; }
            else { ans[3] = operate(reg1, reg3, ops[oi][2]); }
            
            /*= Paren Case  4:  x0 @ ( x1 @ ( x2 @ ( x3 @ x4 ))) =*/
            reg1 = operate(x[3], x[4], ops[oi][4]);
            reg2 = operate(x[2], reg1, ops[oi][3]);
            reg3 = operate(x[1], reg2, ops[oi][2]);
            if ((reg1 == -99999) || (reg2 == -99999) || (reg3 == -99999)) { ans[4] = -99999; }
            else { ans[4] = operate(x[0], reg3, ops[oi][1]); }
            
            /*= Paren Case  5:  x0 @ ( x1 @ (( x2 @ x3 ) @ x4 )) =*/
            reg1 = operate(x[2], x[3], ops[oi][3]);
            reg2 = operate(reg1, x[4], ops[oi][4]);
            reg3 = operate(x[1], reg2, ops[oi][2]);
            if ((reg1 == -99999) || (reg2 == -99999) || (reg3 == -99999)) { ans[5] = -99999; }
            else { ans[5] = operate(x[0], reg3, ops[oi][1]); }
            
            /*= Paren Case  6:  x0 @ (( x1 @ x2 ) @ ( x3 @ x4 )) =*/
            reg1 = operate(x[1], x[2], ops[oi][2]);
            reg2 = operate(x[3], x[4], ops[oi][4]);
            reg3 = operate(reg1, reg2, ops[oi][3]);
            if ((reg1 == -99999) || (reg2 == -99999) || (reg3 == -99999)) { ans[6] = -99999;  }
            else { ans[6] = operate(x[0], reg3, ops[oi][1]); }
            
            /*= Paren Case  7:  x0 @ (( x1 @ ( x2 @ x3 )) @ x4 ) =*/
            reg1 = operate(x[2], x[3], ops[oi][3]);
            reg2 = operate(x[1], reg1, ops[oi][2]);
            reg3 = operate(reg2, x[4], ops[oi][4]);
            if ((reg1 == -99999) || (reg2 == -99999) || (reg3 == -99999)) { ans[7] = -99999; }
            else { ans[7] = operate(x[0], reg3, ops[oi][1]); }
            
            /*= Paren Case  8:  x0 @ ((( x1 @ x2 ) @ x3 ) @ x4 ) =*/
            reg1 = operate(x[1], x[2], ops[oi][2]);
            reg2 = operate(reg1, x[3], ops[oi][3]);
            reg3 = operate(reg2, x[4], ops[oi][4]);
            if ((reg1 == -99999) || (reg2 == -99999) || (reg3 == -99999)) { ans[8] = -99999; }
            else { ans[8] = operate(x[0], reg3, ops[oi][1]); }
            
            /*= Paren Case  9:  ( x0 @ x1 ) @ (( x2 @ x3 ) @ x4 ) =*/
            reg1 = operate(x[0], x[1], ops[oi][1]);
            reg2 = operate(x[2], x[3], ops[oi][3]);
            reg3 = operate(reg2, x[4], ops[oi][4]);
            if ((reg1 == -99999) || (reg2 == -99999) || (reg3 == -99999)) { ans[9] = -99999; }
            else { ans[9] = operate(reg1, reg3, ops[oi][2]); }
            
            /*= Paren Case 10:  ( x0 @ ( x1 @ x2 )) @ ( x3 @ x4 ) =*/
            reg1 = operate(x[1], x[2], ops[oi][2]);
            reg2 = operate(x[0], reg1, ops[oi][1]);
            reg3 = operate(x[3], x[4], ops[oi][4]);
            if ((reg1 == -99999) || (reg2 == -99999) || (reg3 == -99999)) { ans[10] = -99999; }
            else { ans[10] = operate(reg2, reg3, ops[oi][3]); }
            
            /*= Paren Case 11:  ( x0 @ ( x1 @ ( x2 @ x3 ))) @ x4  =*/
            reg1 = operate(x[2], x[3], ops[oi][3]);
            reg2 = operate(x[1], reg1, ops[oi][2]);
            reg3 = operate(x[0], reg2, ops[oi][1]);
            if ((reg1 == -99999) || (reg2 == -99999) || (reg3 == -99999)) { ans[11] = -99999; }
            else { ans[11] = operate(reg3, x[4], ops[oi][4]); }
            
            /*= Paren Case 12:  ( x0 @ (( x1 @ x2 ) @ x3 )) @ x4  =*/
            reg1 = operate(x[1], x[2], ops[oi][2]);
            reg2 = operate(reg1, x[3], ops[oi][3]);
            reg3 = operate(x[0], reg2, ops[oi][1]);
            if ((reg1 == -99999) || (reg2 == -99999) || (reg3 == -99999)) { ans[12] = -99999; }
            else { ans[12] = operate(reg3, x[4], ops[oi][4]); }
            
            /*= Paren Case 13:  (( x0 @ ( x1 @ x2 )) @ x3 ) @ x4  =*/
            reg1 = operate(x[1], x[2], ops[oi][2]);
            reg2 = operate(x[0], reg1, ops[oi][1]);
            reg3 = operate(reg2, x[3], ops[oi][3]);
            if ((reg1 == -99999) || (reg2 == -99999) || (reg3 == -99999)) { ans[13] = -99999; }
            else { ans[13] = operate(reg3, x[4], ops[oi][4]); }
            
    
            for ( j=0; j < NAS; j++)
            {
                if (s == ans[j]) 
                {
                	count++;
                    //printf("Perm: %d, Op: %d, Paren: %d\n",i,oi,j);
                }
            }
    	}
    }
    
    printf("Krypto: %d %d %d %d %d : %d\n",g[0],g[1],g[2],g[3],g[4],s);
    printf("Total Answers Found: %d\n",count);
    
    
    printf("\n");
    return 0;
}

/* ----------------------------------------------------------------------------- 
   FUN...FUN...FUN...FUNCTIONS                                                   
 ----------------------------------------------------------------------------- */

/*== apply operation "op" to r1 and r2 return answer ==*/
int operate(int r1, int r2, char op)
{
    switch(op)
    {
        case '+':
            return add(r1, r2);

        case '-':
            return subt(r1, r2);

        case '*':
            return mult(r1, r2);
            
        case '/':
            return divide(r1, r2);

        default:
            printf("ERROR: Operation Not Found");
            exit(1);
     }
}

/*== addition operator ==*/
int add(int a, int b) { return a + b; }

/*== subtraction operator ==*/
int subt(int a, int b) { return a - b; }

/*== multiplication operator ==*/
int mult(int a, int b) { return a * b; }

/*== division operator ==*/
int divide(int a, int b)
{
    div_t qr;
    if (b != 0) { qr = div(a, b); }
    else { return -99999; }
    
    if (qr.rem != 0) { return -99999; }
    else { return qr.quot; }
    
}


/* this generates the permutation order array
   which determines the order we pull stuff out
   of the game array to give us our permutation */
int permute(int i)
{
	int q;

	lvl++;
	p[i-1] = lvl;

	if(lvl == GS)
    { 
        /* Generate Permutation Order Array */  	
		for(q=0; q < GS; q++) 
		    poa[row][q] = p[q];
		row++;	
	}
	for(q=1; q <= GS; q++)
		if(!p[q-1]) permute(q);  /* fill next unfilled slot */

	/* clean up for return to higher level */
	lvl--; p[i-1] = 0;
	return 0;
}

/* ----------------------------------------------------------------------------- */
/* choose function generates the set of different
   permuations of the operations.  
   For example: (for just +,- choose 4)  
        + + + +
        + + + -
        + + - +
        + + - -
        ...
 */                

int choose(char list[NOPS])
{
    int i,j,period,a;
    div_t qr;

    for (i=0; i < OPLOOP; i++)
    {
        for (j=1; j <= CH; j++)
        {
            period = pow(NOPS, CH-j);
            qr = div(i, period);
            a = qr.quot % NOPS;
            ops[i][j] = list[a];
        }
     }

    return 0;
}


