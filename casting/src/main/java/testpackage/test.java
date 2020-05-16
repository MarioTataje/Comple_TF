package testpackage;

import company.*;
import org.jetbrains.annotations.NotNull;

import java.util.Scanner;

public class test {

    public static void main(String[] arg) {
        Scanner sc = new Scanner(System.in);
        contenedor obj = new contenedor();
        while (true) {
            int opcion = menu();
            if (opcion == 1) {
                addManager(obj);
            } else {
                if (opcion == 2) {
                    addWritter(obj);
                } else {
                    if (opcion == 3) {
                        deleteEmployee(obj);
                    } else {
                        if (opcion == 4) {
                            obj.show();
                        } else {
                            if (opcion == 5) {
                                obj.show_manager();
                            } else {
                                if (opcion == 6) {
                                    obj.show_writter();
                                } else {
                                    if (opcion == 7) {
                                        setManager(obj);
                                    } else {
                                        if (opcion == 8) {
                                            setWritter(obj);
                                        } else {
                                            if (opcion == 9) {
                                                System.exit(0);
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    public static int menu() {
        int opt;
        Scanner scopt = new Scanner(System.in);
        System.out.println("1.- Agregar gerente");
        System.out.println("2.- Agregar escritor");
        System.out.println("3.- Eliminar un empleado");
        System.out.println("4.- Mostrar empleados");
        System.out.println("5.- Mostrar gerentes");
        System.out.println("6.- Mostrar escritores");
        System.out.println("7.- Actualizar departamento de gerente");
        System.out.println("8.- Actualizar editora de escritor");
        System.out.println("9.- Salir");
        System.out.println("Ingrese opcion");
        opt = scopt.nextInt();
        return opt;
    }

    public static void addManager(@NotNull contenedor obj) {
        String name;
        String surname;
        double salary;
        String department;
        Scanner sc2 = new Scanner(System.in);
        Scanner sc3 = new Scanner(System.in);
        System.out.println("El nombre del gerente es : ");
        name = sc2.nextLine();
        System.out.println("El apellido del gerente es : ");
        surname = sc2.nextLine();
        System.out.println("El salario del gerente es : ");
        salary = sc2.nextDouble();
        System.out.println("El departamento del gerente es : ");
        department = sc3.nextLine();
        employee e = new manager(name, surname, salary, department);
        obj.addEmployee(e);
    }

    public static void addWritter(@NotNull contenedor obj) {
        String name;
        String surname;
        double salary;
        String type;
        String editor;
        Scanner sc4 = new Scanner(System.in);
        Scanner sc5 = new Scanner(System.in);
        System.out.println("El nombre del escritor es : ");
        name = sc4.nextLine();
        System.out.println("El apellido del escritor es : ");
        surname = sc4.nextLine();
        System.out.println("El salario del escritor es : ");
        salary = sc4.nextDouble();
        System.out.println("El tipo de escritor es : ");
        type = sc5.nextLine();
        System.out.println("Su editora es :");
        editor = sc5.nextLine();
        employee e = new writter(name, surname, salary, type, editor);
        obj.addEmployee(e);
    }

    public static void deleteEmployee(@NotNull contenedor obj) {
        Scanner sc6 = new Scanner(System.in);
        int id;
        System.out.println("Ingrese el id del empleado a eliminar");
        id = sc6.nextInt();
        obj.deleteEmployee(id);
    }

    public static void setManager(@NotNull contenedor obj) {
        Scanner sc7 = new Scanner(System.in);
        Scanner sc8 = new Scanner(System.in);
        int id;
        String department;
        System.out.println("Seleccione el gerente a modificar su departamento : ");
        id = sc7.nextInt();
        System.out.println("Ingrese el nuevo departamento");
        department = sc8.nextLine();
        obj.set_Manager(id, department);
    }

    public static void setWritter(@NotNull contenedor obj) {
        Scanner sc9 = new Scanner(System.in);
        Scanner sc10 = new Scanner(System.in);
        int id;
        String editor;
        System.out.println("Seleccione el escritor a modificar su departamento : ");
        id = sc9.nextInt();
        System.out.println("Ingrese la nueva editora");
        editor = sc10.nextLine();
        obj.set_Writter(id, editor);
    }
}
