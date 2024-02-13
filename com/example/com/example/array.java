package com.example;

// class student{
//     int id;
//     String name;
//     student(int id ,String name){
//         this.id=id;
//         this.name=name;
//     }
//     void display(){
//     System.out.println(id+" "+name);
//     }
//     public static void main(String args[])
//     {
//         student student = new student(1,"Varun");
//         student.display();
//     }
// }
class student{
    int id;
    String name;
    student(int id ,String name){
        this.id=id;
        this.name=name;
    }
    void display(){
    System.out.println(id+" "+name);
    }
public static void main(String args[])
{
    student s1=new student(1,"Varun");
    student s2=new student(2,"samay");
    student s3=new student(3,"vishal");
    student s4=new student(4,"rohan");
    student s5=new student(5,"abhishek");
    s1.display();
    s2.display();
    s3.display();
    s4.display();
    s5.display();
}
}