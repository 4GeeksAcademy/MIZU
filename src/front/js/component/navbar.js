import React from "react";
import { Link } from "react-router-dom";
import "../../styles/navbar.css";

export const Navbar = () => {
    return (
        <nav className="navbar navbar-expand-lg navbar-light" style={{ backgroundColor: "#073642" }}>
            <div className="container-fluid justify-content-between">
                {/* Left elements */}
                <div className="d-flex">
                    {/* Brand */}
                    <Link to="/" className="navbar-brand me-2 mb-1 d-flex align-items-center">
                        <img
                            src="https://mdbcdn.b-cdn.net/img/logo/mdb-transaprent-noshadows.webp"
                            height="20"
                            alt="Mizu Logo"
                            loading="lazy"
                            style={{ marginTop: "2px" }}
                        />
                        <span className="ms-2 text-white">MIZU</span>
                    </Link>
                </div>
                {/* Left elements */}

                {/* Center elements */}
                <ul className="navbar-nav flex-row d-none d-md-flex">
                    <li className="nav-item me-3 me-lg-1">
                        <Link className="nav-link text-white" to="#home">Inicio</Link>
                    </li>
                    <li className="nav-item me-3 me-lg-1">
                        <Link className="nav-link text-white" to="#about">Sobre Nosotros</Link>
                    </li>
                    <li className="nav-item me-3 me-lg-1">
                        <Link className="nav-link text-white" to="#services">Servicios</Link>
                    </li>
                    <li className="nav-item me-3 me-lg-1">
                        <Link className="nav-link text-white" to="#contact">Contacto</Link>
                    </li>
                </ul>
                {/* Center elements */}

                {/* Right elements */}
                <ul className="navbar-nav flex-row">
                    <li className="nav-item me-3 me-lg-1">
                        <a className="nav-link" href="#">
                            <span><i className="fab fa-facebook-f text-white"></i></span>
                        </a>
                    </li>
                    <li className="nav-item me-3 me-lg-1">
                        <a className="nav-link" href="#">
                            <span><i className="fab fa-instagram text-white"></i></span>
                        </a>
                    </li>
                    <li className="nav-item me-3 me-lg-1">
                        <a className="nav-link" href="#">
                            <span><i className="fab fa-tiktok text-white"></i></span>
                        </a>
                    </li>
                </ul>
                {/* Right elements */}
            </div>
        </nav>
    );
};