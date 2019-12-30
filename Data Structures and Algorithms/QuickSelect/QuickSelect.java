package lab3;

import java.util.ArrayList;
import java.util.Random;
import java.util.Scanner;

/*
         This class uses the QuickSelect Algorithm to solve the following:
         i) Find the k least integer in an unordered array
         ii) Find the mak k integers in an unordered array
 */
public class QuickSelect {

    /**
     * Generates an integer array
     *
     * @param size the size of the array
     * @param max  the maximum value in the array
     * @param min  the minimum value in the array
     * @return an integer array
     */

    public static int[] generateArray(int size, int max, int min) {
        int[] array = new int[size];
        Random r = new Random();
        int randomNum;
        for (int i = 0; i < array.length; i++) {
            randomNum = r.nextInt((max - min) + 1) + min; //generating a random integer not exceeding max
            array[i] = randomNum;
        }
        return array;
    }

    /**
     * This method is used to partition the array.
     * Works by taking the last element, and taking elements that are greater than it and shift the values
     * @param array
     * @return
     */
    public static int partition(int[] array, int startIndex, int endIndex) {
        if(startIndex==endIndex){
            return endIndex;
        }else {
            int pivot = array[endIndex];
            ArrayList<Integer> lowerArray = new ArrayList<Integer>();
            ArrayList<Integer> upperArray = new ArrayList<Integer>();
            for (int i = startIndex; i <= endIndex - 1; i++) {
                if (array[i] >= pivot) {
                    upperArray.add(array[i]);
                } else {
                    lowerArray.add(array[i]);
                }
            }
            int count = startIndex;
            for (Integer intg : lowerArray) {
                array[count] = intg;
                count++;
            }
            int pivotIndex = count;
            array[count] = pivot;
            count++;
            for (Integer intg : upperArray) {
                array[count] = intg;
                count++;
            }

            return pivotIndex;
        }
    }



    /**
     * This method uses the QuickSelect algorithm to find the kth integer in the array
     * @param k - the position of the integer to find
     * @param array - the array to find the integer in
     * @param startIndex - the index at which to start at
     * @param endIndex - the index at which to end at
     * @return the index of the kth integer
     */

    public static int Quick_select(int k, int[] array,int startIndex, int endIndex) {
        if (k > array.length) {
            System.out.println("Sorry, k is greater than the number of element in the list");
        } else {
            int index = partition(array,startIndex,endIndex);
            if (index+1 == k) {
                return index;
            } else if (index+1> k) {
                return Quick_select(k, array, 0, index-1);
            } else if (index+1 < k) {
                return Quick_select(k ,array, index + 1, array.length-1);
            }

        }
        return -1;
    }

    /**
     * This method uses the QuickSelect Algorithm to find the maximum k integers in the array
     * @param k - index of the element to find
     * @param array - the array to find the integer in
     * @return
     */

    public static int printKMaxIntegers(int k, int[] array){
        if (k > array.length) {
            System.out.println("Sorry, k is greater than the number of element in the list");
        } else {
            k=array.length-(k-1);
            int index=Quick_select(k,array,0,array.length-1);
            for(int i=index;i<array.length;i++){
                System.out.print(array[i]+" ");
            }
        }
        return 0;
    }


    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.println("Enter a number: ");
        int n = in.nextInt();
        int[] array = generateArray(n, 100, -100);
        for (int a : array) {
            System.out.print(a + " ");
        }
        System.out.println();
        System.out.println("Enter a number between 1 and " + n + ": ");
        int k = in.nextInt();
        int index=Quick_select(k,array,0,array.length-1);
        System.out.println("Element: "+array[index]);
        System.out.println();
        System.out.println("Enter a number: ");
        n = in.nextInt();
        array = generateArray(n, 100, -100);
        for (int a : array) {
            System.out.print(a + " ");
        }
        System.out.println();
        System.out.println("Enter a number between 1 and " + n + ": ");
        k = in.nextInt();
        printKMaxIntegers(k,array);
    }
}
