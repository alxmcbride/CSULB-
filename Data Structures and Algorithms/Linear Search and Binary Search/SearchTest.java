import lab1.BinarySearchAlgorithm;
import lab1.LinearSearchAlgorithm;
import lab1.SearchUtilities;

import java.util.Scanner;

/**
 * This class is a tester class for the linear and binary search algorithms
 */
public class SearchTest {

    /**
     * Finds the linear and binary search algorithms' running time for the average case
     * and the worst case
     * @param args
     */

    public static void main(String[] args){

        Scanner in = new Scanner(System.in);
        System.out.println("Enter a positive integer: ");
        int n = in.nextInt();

        //Generating the array
        SearchUtilities su = new SearchUtilities();
        int[] array = su.generateArray(n, 1000, -1000);

        //Sorting the array
        int[] sortedArray = su.sort(array);

        // Average Case
        //--Linear Search
        double linAvgRuntime=LinearSearchAlgorithm.avgCaseTimer(sortedArray);
        System.out.printf("Linear Search Average Case Runtime: %f seconds\n",linAvgRuntime);

        //--Binary Search
        double binAvgRuntime= BinarySearchAlgorithm.avgCaseTimer(sortedArray);
        System.out.printf("Binary Search Average Case Runtime: %f seconds\n",binAvgRuntime);

        //Worst Case
        array = su.generateArray(n, 1000, -1000);
        //--Linear Search
        double linWorstRuntime=LinearSearchAlgorithm.worstCaseTimer(sortedArray);
        System.out.printf("Linear Search Worst Case Runtime: %f seconds\n",linWorstRuntime);

        //--Binary Search
        double binWorstRuntime= BinarySearchAlgorithm.worstCaseTimer(sortedArray);
        System.out.printf("Binary Search Worst Case Runtime: %f seconds\n",binWorstRuntime);

        //Time per line in binary search
        double k=Math.log10(n)/Math.log10(2);
        double timePerLine=binWorstRuntime/(5*k)+3;
        System.out.printf("Time per line: %.12f seconds\n",timePerLine);

        //Estimated time for linear search and binary search when n=10^9
        System.out.printf("Estimated time for n = 10e9 using Linear Search: %f seconds\n",(10e9+1)*timePerLine);

        System.out.printf("Estimated time for n = 10e9 using Binary Search: %f seconds",((5*Math.log10(10e9)/Math.log10(2)+3)*timePerLine));

    }
}
