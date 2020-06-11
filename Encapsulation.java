public class Student
{
int rollNo=43;
double marks=95;
String name= new String("Lavanya");

void display()
{
    System.out.println("Roll no:"+ rollNo);
    System.out.println("Marks:" + marks);
    System.out.println("Name : "+name);
    
    
}
    public static void main(String[] args) {
        
System.out.println("Student info");
Student st=new Student();
st.display();
    }
}

