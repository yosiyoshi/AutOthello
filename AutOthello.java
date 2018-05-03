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
    		if (m[w-1][h]+m[w][h]==0); {
//Here is the detail of algorithm! 
        		}
    		}
		}
	}
}
