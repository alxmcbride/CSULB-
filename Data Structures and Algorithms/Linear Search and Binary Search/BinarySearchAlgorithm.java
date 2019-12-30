package lab1;

import java.util.Random;

/**
 * This class tests the binary search algorithm and determines the average case and
 * the worst case running time
 */

public class BinarySearchAlgorithm {

    /**
     * Performs the binary search
     * @param key an integer value to be searched for
     * @param a an integer array
     * @return true if the value was found, otherwise false
     */

    public static boolean search(int key, int [] a){

        //setting the start and end index
          int startIndex=0;
          int endIndex=(a.length)-1;

        //performing the search
          while(endIndex >= startIndex){
              int midIndex=(startIndex + endIndex)/2;
              int aMid=a[midIndex];
              if(aMid==key){
                  return true;
              }else if(aMid < key){
                  startIndex=midIndex+1;
              }else if(aMid > key){
                  endIndex=midIndex-1;
              }
          }
          return false;  //if element is not found

    }

    /**
     * Calculates the average case running time for the binary search
     * @param array an integer array
     * @return the elapsed time
     */

    public static double avgCaseTimer(int [] array) {
        //Initializing new stopwatch
        Stopwatch stopwatch = new Stopwatch();

        //Used to generate a random index in the array
        Random r = new Random();

        //Measuring the runtime
        double totalRuntimeAvgCase = 0.0;
        for (int i = 0; i < 100; i++) {
            int index = r.nextInt(array.length-1);
            int key=array[index];
            stopwatch.start();
            search(key, array);
            stopwatch.stop();
            totalRuntimeAvgCase += stopwatch.elapsedTime();
        }

        return totalRuntimeAvgCase / 100;
    }

    /**
     * Calculates the worst case running time for the binary search
     * @param array an integer array
     * @return the elapsed time
     */
    public static double worstCaseTimer(int[] array) {

        //Initializing new stopwatch
        Stopwatch stopwatch = new Stopwatch();

        //Measuring runtime
        stopwatch.start();
        search(5000, array);
        stopwatch.stop();
        return stopwatch.elapsedTime();

    }


}
