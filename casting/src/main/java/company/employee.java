package company;

public class employee {
    protected int idEmployee;
    protected String name;
    protected String surname;
    protected double salary;
    protected static int countEmployee;


    public employee(String name, String surname, double salary) {
        this.idEmployee = ++countEmployee;
        this.name = name;
        this.surname = surname;
        this.salary = salary;
    }

    public int getIdEmployee() {
        return idEmployee;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getSurname() {
        return surname;
    }

    public void setSurname(String surname) {
        this.surname = surname;
    }

    public double getSalary() {
        return salary;
    }

    public void setSalary(double salary) {
        this.salary = salary;
    }

    public void Imprimir() {
        System.out.println("El id del empleado es : " + idEmployee);
        System.out.println("El nombre es : " + name);
        System.out.println("El apellido es : " + surname);
        System.out.println("El salario es : " + salary);
    }
}
