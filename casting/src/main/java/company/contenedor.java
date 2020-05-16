package company;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class contenedor {
    List<employee> list = new ArrayList();

    public contenedor() {

    }

    public void addEmployee(employee e) {
        list.add(e);
    }

    public void deleteEmployee(int id) {
        if (list.isEmpty()) {
            System.out.println("No hay empleados");
            return;
        } else {
            Iterator<employee> it = list.iterator();
            while (it.hasNext()) {
                employee p = it.next();
                if (p.getIdEmployee() == id) {
                    it.remove();
                }
            }
/*
            for(employee p : list)
            {
                if (p.getIdEmployee() == id)
                {
                    list.remove(p);
                    break;
                }
            }*/
        }

    }

    public void show() {
        for (employee p : list) {
            p.Imprimir();
        }
    }

    public void show_manager() {
        for (employee p : list) {
            if (p instanceof manager) {
                p.Imprimir();
            }
        }
    }

    public void show_writter() {
        for (employee p : list) {
            if (p instanceof writter) {
                p.Imprimir();
            }
        }
    }

    public void set_Manager(int id, String department) {
        for (employee p : list) {
            if (p.getIdEmployee() == id) {
                manager m = (manager) p;
                m.setDepartment(department);
            }
        }
    }

    public void set_Writter(int id, String editor) {
        for (employee p : list) {
            if (p.getIdEmployee() == id) {
                writter w = (writter) p;
                w.setEditor(editor);
            }
        }
    }
}
