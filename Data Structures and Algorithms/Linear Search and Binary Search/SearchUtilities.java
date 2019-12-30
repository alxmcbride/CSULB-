package lab1;

        import java.util.Random;

/**
 * This class is used for the following utilities:
 * - Generating an array
 * - Sorting the array
 */

public class SearchUtilities {

    /**
     * Generates an integer array
     * @param size the size of the array
     * @param max the maximum value in the array
     * @param min the minimum value in the array
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
     * Sorts the array using Bubble Sort Algorithm
     * @param array an integer array
     */
    public static int[] sort(int[] array){
        for (int i = 0; i < array.length - 1; i++) {
            for (int j = 0; j < array.length - i - 1; j++) {
                if (array[j] > array[j + 1]) {
                    //swaps the element
                    int temp = array[j];
                    array[j] = array[j + 1];
                    array[j + 1] = temp;
                }
            }
        }
        return array;
    }


}

