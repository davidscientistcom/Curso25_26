/**
 * Representa un recurso de Usuario en el sistema.
 * POJO (Plain Old Java Object) simple.
 */
public class User {
    public int id;
    public String name;
    public String email;

    // Constructor vacío requerido por GSON para reflexión
    public User() { }

    public User(int id, String name, String email) {
        this.id = id;
        this.name = name;
        this.email = email;
    }
}
