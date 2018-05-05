//Author: Yosiyoshi, code in development

import java.util.Random;

public class AutOthello{
	public static void main(String[] args) {
	int m[][] = {{0,0,0,0},{0,1,-1,0},{0,-1,1,0},{0,0,0,0}};
	int t = 0;
	while (t <= 2) {
		Random rand = new Random();
		int w = rand.nextInt(3);
		int h = rand.nextInt(3);
		while (h <= 1) {
    		if (m[w-1][h]+m[w][h]>=-1) {
             m[w][h] = 0;
             w = w + 1;
             if (1 <= w && w <= 2); {
                 m[w-1][h] = 1;
                 m[w+1][h] = 1;
            } else if (w <= 1) {
                 if (m[w][h] == m[w+2][h]) {
                 m[w+1][h] = 1;
                 m[w+2][h] = 1;
                     }
            } else if (w >= 2) {
            		if (m[w][h] == m[w-2][h]); {
                	m[w-1][h] = 1;
                	m[w-1][h] = 1;
                    	}
                }
// Uncompleted coding.
            }
    	       System.out.println(m);
    	       t = t + 1; 
        	}
	}
    }
}
