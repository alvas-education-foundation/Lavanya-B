import java.util.HashMap;

public class MyClass {
    public static void main(String[ ] args) {
        HashMap<String, Integer> points = new HashMap<String, Integer>();
        points.put("Abc", 154);
        points.put("Def", 42);
        points.put("Ghi", 733);
        System.out.println(points.get("Def")); 
    }
}

