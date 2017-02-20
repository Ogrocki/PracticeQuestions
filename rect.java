//write a fuction that takes in two sets of x,y points which are
// the bottom left and top right points of a rectangle.

//Then find if those two rectangles are overlapping
//return true on overlap
//return false on not overlap

public class rect{
	public static void main(String[] args){
		System.out.println(isOverlap(0,0,5,5,6,6,7,7));
	}
public static boolean isOverlap(int bl1x, int bl1y, int tr1x, int tr1y, int bl2x, int bl2y, int tr2x, int tr2y){
	if(bl1x>tr2x) return false;
	if(bl1y>tr2y) return false;
	if(tr1x<bl2x) return false;
	if(tr1y<bl2y) return false;

	return true;
}
}
