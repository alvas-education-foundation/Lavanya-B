public class Vehicle {
    private String color;
    
    Vehicle() {
        this.setColor("Red");
    }
    Vehicle(String c) {
        this.setColor(c);
    }
    
    public void setColor(String c) {
        this.color = c;
    }
    

    public String getColor() {
        return color;
    }
}

public class Program {
    public static void main(String[] args) {        
     
        Vehicle v1 = new Vehicle();
        
   
        Vehicle v2 = new Vehicle("Green"); 
        
        System.out.println(v2.getColor());
    }
}