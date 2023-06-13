public class largest{
    
    public static int large(int arr[],int n){
        int large=0;
        for(int i=0;i<n;i++){
            if(arr[i]>large){
                large=arr[i];
            }
        }
        return large;
    }
    public static void main(String args[]){
        int arr[]={7,8,9,1,3};
        int ans=large(arr, 5);
        System.out.println(ans);

    }
}