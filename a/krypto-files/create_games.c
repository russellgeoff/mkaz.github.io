/*

create_games.c

    Marcus Kazmierczak, marcus@mkaz.com
    March 11, 2002
    http://mkaz.com/math/krypto/

Generate all possible krypto games
and writes them out to a test file

There's a total of 2,968,875 possible games
You end up with a 45mb text file

$Date: 2002/03/13 07:03:33 $
$Revision: 1.1 $

*/

#include <stdio.h>

int main(void)
{
    static int max = 25;
    static int smax = 25;
    int i = 0;

    int n1,n2,n3,n4,n5,s1;
    
    for (n1=1; n1 <= max; n1++)
    {
    	for (n2=n1; n2 <= max; n2++)
    	{
            for (n3=n2; n3 <= max; n3++)
            {
            	for (n4=n3; n4 <= max; n4++)
            	{
                    for (n5=n4; n5 <= max; n5++)
                    {
                        for (s1=1; s1 <= smax; s1++)
                        {
                            printf("%d %d %d %d %d %d\n", n1, n2, n3, n4, n5, s1);
                        }
                    }
            	}
            }
    	}
    }
            	

}
