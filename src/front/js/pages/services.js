import React, { useState } from "react";
import { Link } from "react-router-dom";
import "../../styles/services.css";

export const AllServices = () => {
    const [services] = useState([
        {
            id: 1,
            name: "Experiencia Mizu Mujer",
            image: "https://placehold.co/600x400",
            description: "Masajes capilares relajantes, técnicas japonesas AMMA-SHIATSU y productos naturales.",
            link: "/service/1"
        },
        {
            id: 2,
            name: "Placer Mizu",
            image: "https://placehold.co/600x400",
            description: "Tratamiento capilar premium que incluye masajes faciales y exfoliación capilar.",
            link: "/service/2"
        },
        {
            id: 3,
            name: "Migraña Mizu",
            image: "https://placehold.co/600x400",
            description: "Masajes específicos para aliviar migrañas, mejorando la circulación y el bienestar.",
            link: "/service/3"
        },
        {
            id: 4,
            name: "Bosque y Selva",
            image: "https://placehold.co/600x400",
            description: "Tratamiento de parejas con técnicas relajantes y un ambiente natural único.",
            link: "/service/4"
        },
        {
            id: 5,
            name: "Renovación Capilar",
            image: "https://placehold.co/600x400",
            description: "Tratamiento especial para revitalizar y renovar la salud del cuero cabelludo.",
            link: "/service/5"
        }
    ]);

    return (
        <div className="all-services-container">
            <h2>Todos los Servicios</h2>
            <div className="all-services-cards">
                {services.map((service, index) => (
                    <div className="card" key={index}>
                        <div className="bg-image hover-overlay" data-mdb-ripple-init data-mdb-ripple-color="light">
                            <img src={service.image} className="img-fluid" alt={service.name} />
                            <Link to={service.link}>
                                <div className="mask" style={{ backgroundColor: "rgba(251, 251, 251, 0.15)" }}></div>
                            </Link>
                        </div>
                        <div className="card-body">
                            <h5 className="card-title">{service.name}</h5>
                            <p className="card-text">{service.description}</p>
                            <Link to={service.link} className="btn btn-primary" data-mdb-ripple-init>Ver Servicio</Link>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    );
};
