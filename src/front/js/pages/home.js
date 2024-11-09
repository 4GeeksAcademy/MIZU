import React, { useState } from "react";
import { Link } from "react-router-dom";
import "../../styles/home.css";

export const Home = () => {
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
        }
    ]);

    return (
        <div>
            {/* Jumbotron Section */}
            <section id="home" className="jumbotron">
                <div className="jumbotron-content">
                    <h1>Relaja tu mente, cuida tu cabello</h1>
                    <p className="description">En Mizu Head Spa, nos dedicamos a brindarte una experiencia única de head spa que fusiona el autocuidado con el cuidado capilar, utilizando tratamientos naturales y técnicas japonesas AMMA-SHIATSU.</p>
                </div>
            </section>

            {/* Services Cards Section */}
            <section id="services-cards" className="services-cards-section">
                <h2>Servicios Principales</h2>
                <div className="services-cards">
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
                <div className="view-all-services">
                    <Link to="/services">
                        <button className="btn">Ver todos los servicios</button>
                    </Link>
                </div>
            </section>

            {/* Pre-Footer Section */}
            <section id="prefooter" className="prefooter-section">
                <div className="prefooter-content">
                    <h2>Visítanos</h2>
                    <p>Nos encontramos en: Av. Reina Victoria 51, BB Work Space, Cabina #3, Madrid.</p>
                    <p>Para cualquier duda, contáctanos en <a href="mailto:Supgou@mizumadrid.com">Supgou@mizumadrid.com</a></p>
                </div>
            </section>
        </div>
    );
};