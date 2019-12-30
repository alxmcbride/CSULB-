package lab1;

import java.util.Random;

/**
 * This class tests the linear search algorithm and determines the average case and
 * the worst case running time
 */

public class LinearSearchAlgorithm {

    /**
     * Performs the linear search
     * @param key an integer value to be searched for
     * @param a an integer array
     * @return true if the value was found, otherwise false
     */
    public static boolean search(int key, int[] a) {
        for (int num : a) {
            if (num == key) {
                return true;
            }
        }
        return false;
    }

    /**
     * Calculates the average case running time for the linear search
     * @param array an integer array
     * @return the elapsed time
     */

    public static double avgCaseTimer(int[] array) {
        //Initializing new stopwatch
        Stopwatch stopwatch = new Stopwatch();

        //Used to generate a random index in the array
        Random r = new Random();

        // Measuring the running time
        double totalRuntimeAvgCase = 0.0;
        for (int i = 0; i < 100; i++) {
            //random value from array
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
     * Calculates the worst case running time for the linear search
     * @param array an integer array
     * @return the elapsed time
     */
    public static double worstCaseTimer(int [] array){
        //Initializing new stopwatch
        Stopwatch stopwatch = new Stopwatch();

        //Measuring running time
        stopwatch.start();
        search(5000, array);
        stopwatch.stop();
        return stopwatch.elapsedTime();

    }
}
