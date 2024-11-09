const getState = ({ getStore, getActions, setStore }) => {
    return {
        store: {
            clientes: [],
            servicios: [],
            reservas: [],
            transacciones: [],
            historialVisitas: [],
        },
        actions: {
            // Fetch Clientes from the API
            fetchClientes: async () => {
                try {
                    const response = await fetch(process.env.BACKEND_URL + "/api/clientes");
                    if (response.ok) {
                        const data = await response.json();
                        setStore({ clientes: data });
                    }
                } catch (error) {
                    console.error("Error fetching clientes:", error);
                }
            },

            // Fetch Servicios from the API
            fetchServicios: async () => {
                try {
                    const response = await fetch(process.env.BACKEND_URL + "/api/servicios");
                    if (response.ok) {
                        const data = await response.json();
                        setStore({ servicios: data });
                    }
                } catch (error) {
                    console.error("Error fetching servicios:", error);
                }
            },

            // Create Reserva
            createReserva: async (reserva) => {
                try {
                    const response = await fetch(process.env.BACKEND_URL + "/api/reservas", {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json",
                        },
                        body: JSON.stringify(reserva),
                    });
                    if (response.ok) {
                        const newReserva = await response.json();
                        setStore({ reservas: [...getStore().reservas, newReserva] });
                    }
                } catch (error) {
                    console.error("Error creating reserva:", error);
                }
            },

            // Fetch Reservas from the API
            fetchReservas: async () => {
                try {
                    const response = await fetch(process.env.BACKEND_URL + "/api/reservas");
                    if (response.ok) {
                        const data = await response.json();
                        setStore({ reservas: data });
                    }
                } catch (error) {
                    console.error("Error fetching reservas:", error);
                }
            },

            // Fetch Historial de Visitas
            fetchHistorialVisitas: async () => {
                try {
                    const response = await fetch(process.env.BACKEND_URL + "/api/historial_visitas");
                    if (response.ok) {
                        const data = await response.json();
                        setStore({ historialVisitas: data });
                    }
                } catch (error) {
                    console.error("Error fetching historial visitas:", error);
                }
            },
        },
    };
};

export default getState;
