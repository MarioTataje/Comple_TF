package company;

public enum typewrite {
    CLASICO("Escritura a mano"),
    MODERNO("Escritura digital");

    private final String description;

    typewrite(String description) {
        this.description = description;
    }

    public String getDescription() {
        return description;
    }
}
