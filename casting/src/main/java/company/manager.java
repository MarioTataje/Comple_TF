package company;

public class manager extends employee {

    private int idManager;
    private String department;
    private static int countManager;

    public manager(String name, String surname, double salary, String department) {
        super(name, surname, salary);
        idManager = ++countManager;
        this.department = department;
    }

    public String getDepartment() {
        return department;
    }

    public void setDepartment(String department) {
        this.department = department;
    }

    @Override
    public void Imprimir() {
        System.out.println("El id del gerente es : " + idManager);
        super.Imprimir();
        System.out.println("Su departamento es : " + department);
    }
}
