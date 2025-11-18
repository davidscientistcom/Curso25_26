import com.google.gson.Gson;
import io.javalin.Javalin;
import io.javalin.http.Context;
import io.javalin.http.HttpStatus; // Enumerado para códigos HTTP

import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.Optional;
import java.util.concurrent.ThreadLocalRandom;

public class Main {

    // Singleton de Gson para manejo de JSON
    private static final Gson gson = new Gson();
    
    // Base de datos en memoria (Volátil) para simulación
    private static final List<User> users = new ArrayList<>();

    public static void main(String[] args) {
        // Inicialización de datos mock
        users.add(new User(1, "Alice", "alice@university.edu"));
        users.add(new User(2, "Bob", "bob@university.edu"));

        // 1. Configuración e inicio del servidor Javalin
        // Usamos .create(config -> {}) que es la convención moderna en v6.x
        Javalin app = Javalin.create(config -> {
            config.router.contextPath = "/"; // Raíz
        }).start(7001);

        System.out.println("Servidor corriendo en http://localhost:7001");

        // 2. Definición de Rutas (Endpoints)
        // Mapeamos verbos HTTP a métodos de Java (Method References)
        app.post("/users", Main::createUser);
        app.get("/users", Main::getAllUsers);
        app.get("/users/{id}", Main::getUserById);
        app.put("/users/{id}", Main::updateUser);
        app.delete("/users/{id}", Main::deleteUser);
    }

    // --- CONTROLADORES (HANDLERS) ---

    /**
     * POST /users
     * Crea un nuevo recurso.
     */
    private static void createUser(Context ctx) {
        // Deserialización: JSON Body -> Java Object
        User newUser = gson.fromJson(ctx.body(), User.class);
        
        // Lógica de negocio simulada
        newUser.id = ThreadLocalRandom.current().nextInt(100, 999);
        users.add(newUser);

        // Respuesta: 201 Created
        ctx.status(HttpStatus.CREATED);
        ctx.json(Map.of(
            "message", "Usuario creado exitosamente",
            "id", newUser.id
        ));
    }

    /**
     * GET /users
     * Recupera la colección completa.
     */
    private static void getAllUsers(Context ctx) {
        // Serialización automática a JSON
        ctx.status(HttpStatus.OK);
        ctx.json(users);
    }

    /**
     * GET /users/{id}
     * Recupera un recurso específico.
     */
    private static void getUserById(Context ctx) {
        int id = Integer.parseInt(ctx.pathParam("id"));

        // Búsqueda funcional (Java Stream API)
        Optional<User> match = users.stream()
                .filter(u -> u.id == id)
                .findFirst();

        if (match.isPresent()) {
            ctx.status(HttpStatus.OK);
            ctx.json(match.get());
        } else {
            ctx.status(HttpStatus.NOT_FOUND);
            ctx.json(Map.of("error", "Usuario no encontrado"));
        }
    }

    /**
     * PUT /users/{id}
     * Actualiza un recurso existente.
     */
    private static void updateUser(Context ctx) {
        int id = Integer.parseInt(ctx.pathParam("id"));
        User incomeData = gson.fromJson(ctx.body(), User.class);

        Optional<User> match = users.stream()
                .filter(u -> u.id == id)
                .findFirst();

        if (match.isPresent()) {
            User user = match.get();
            user.name = incomeData.name;
            user.email = incomeData.email;
            
            ctx.status(HttpStatus.OK);
            ctx.json(user);
        } else {
            ctx.status(HttpStatus.NOT_FOUND);
            ctx.json(Map.of("error", "Usuario no encontrado para actualizar"));
        }
    }

    /**
     * DELETE /users/{id}
     * Elimina un recurso.
     */
    private static void deleteUser(Context ctx) {
        int id = Integer.parseInt(ctx.pathParam("id"));
        
        boolean removed = users.removeIf(u -> u.id == id);

        if (removed) {
            ctx.status(HttpStatus.OK); // O HttpStatus.NO_CONTENT (204)
            ctx.json(Map.of("message", "Usuario eliminado"));
        } else {
            ctx.status(HttpStatus.NOT_FOUND);
            ctx.json(Map.of("error", "Usuario no existe"));
        }
    }
}
