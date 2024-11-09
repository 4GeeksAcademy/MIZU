import React from "react";
import { useParams } from "react-router-dom";
import "../../styles/service-detail.css";

const exampleServices = [
    {
        id: 1,
        name: "Experiencia Mizu Mujer",
        image: "https://placehold.co/600x400",
        description: "Masajes capilares relajantes, técnicas japonesas AMMA-SHIATSU y productos naturales.",
        duration: 60,
        price: 66.99,
        link: "/service/1"
    },
    {
        id: 2,
        name: "Placer Mizu",
        image: "https://placehold.co/600x400",
        description: "Tratamiento capilar premium que incluye masajes faciales y exfoliación capilar.",
        duration: 90,
        price: 90.00,
        link: "/service/2"
    },
    {
        id: 3,
        name: "Migraña Mizu",
        image: "https://placehold.co/600x400",
        description: "Masajes específicos para aliviar migrañas, mejorando la circulación y el bienestar.",
        duration: 45,
        price: 50.00,
        link: "/service/3"
    },
    {
        id: 4,
        name: "Bosque y Selva",
        image: "https://placehold.co/600x400",
        description: "Tratamiento de parejas con técnicas relajantes y un ambiente natural único.",
        duration: 120,
        price: 120.00,
        link: "/service/4"
    }
];

export const ServiceDetail = () => {
    const { theid } = useParams();
    const service = exampleServices.find(s => s.id === parseInt(theid));

    if (!service) {
        return <div>Servicio no encontrado.</div>;
    }

    return (
        <div className="service-detail-container">
            {/* Service Detail Section */}
            <section id="service-detail" className="service-detail-section">
                <div className="service-detail-content">
                    <h1 className="text-black">{service.name}</h1>
                    <img src={service.image} alt={service.name} className="service-image" />
                    <p className="text-black">{service.description}</p>
                    <p className="text-black"><strong>Duración:</strong> {service.duration} minutos</p>
                    <p className="text-black"><strong>Precio:</strong> {service.price}€</p>
                </div>
                <div className="reservation-section">
                    <h2>Reserva tu sesión</h2>
                    <p>Selecciona la fecha y la hora para reservar tu tratamiento.</p>
                    <form className="reservation-form">
                        <label htmlFor="date">Fecha:</label>
                        <input type="date" id="date" name="date" required />

                        <label htmlFor="time">Hora:</label>
                        <input type="time" id="time" name="time" required />

                        <button type="submit" className="btn btn-primary">Reservar</button>
                    </form>
                </div>
            </section>
        </div>
    );
};
