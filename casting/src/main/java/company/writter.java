package company;

public class writter extends employee {

    private int idWritter;
    final typewrite tw;
    private String type;
    private String editor;
    private static int countWritter;

    public writter(String name, String surname, double salary, String type, String editor) {
        super(name, surname, salary);
        this.idWritter = ++countWritter;
        this.type = type;
        this.editor = editor;
        tw = typewrite.valueOf(this.type);
    }

    @Override
    public void Imprimir() {
        System.out.println("El id del escritor es : " + idWritter);
        super.Imprimir();
        switch (tw) {
            case CLASICO:
                System.out.println("El tipo de escritura es : " + typewrite.CLASICO);
                System.out.println("Su descripcion es : " + tw.getDescription());
                break;
            case MODERNO:
                System.out.println("El tipo de escritura es : " + typewrite.MODERNO);
                System.out.println("Su descripcion es : " + tw.getDescription());
                break;
        }
        System.out.println("Su editora es : " + editor);
    }

    public String getDescription() {
        return tw.getDescription();
    }

    public void setEditor(String editor) {
        this.editor = editor;
    }
}
