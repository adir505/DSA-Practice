int maxArea(int* height, int heightSize){
    int i=0, j=heightSize-1;
    int max_area=0;
    while(i<j){
        int area = (j-i) * (height[i]<height[j] ? height[i++] : height[j--]);
        if(area > max_area) max_area = area;
    }
    return max_area;
}