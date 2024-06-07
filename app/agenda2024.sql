-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 07-06-2024 a las 16:10:12
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `agenda2024`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `canciones`
--

CREATE TABLE `canciones` (
  `IdCancion` int(11) NOT NULL,
  `TituloCancion` varchar(100) DEFAULT NULL,
  `NombreArtistaCancion` varchar(100) DEFAULT NULL,
  `Genero` varchar(50) DEFAULT NULL,
  `Duracion` time DEFAULT NULL,
  `Precio` decimal(10,2) DEFAULT NULL,
  `Lanzamiento` date DEFAULT NULL,
  `Img` blob DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `canciones`
--

INSERT INTO `canciones` (`IdCancion`, `TituloCancion`, `NombreArtistaCancion`, `Genero`, `Duracion`, `Precio`, `Lanzamiento`, `Img`) VALUES
(8, 'MARIA SE FUE ', 'SHAKIRA', 'Balada', '00:50:00', 3000.00, '2024-05-05', 

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `compras`
--

CREATE TABLE `compras` (
  `idcompra` int(11) NOT NULL,
  `fechaCompra` date NOT NULL,
  `Precio` decimal(10,2) NOT NULL,
  `userid` int(11) NOT NULL,
  `idcancion` int(11) NOT NULL,
  `mpago` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `persona`
--

CREATE TABLE `persona` (
  `IdPersona` int(11) NOT NULL,
  `NombrePerso` varchar(50) DEFAULT NULL,
  `ApellidoPerso` varchar(50) DEFAULT NULL,
  `EmailPerso` varchar(100) DEFAULT NULL,
  `DireccionPerso` varchar(100) DEFAULT NULL,
  `TelefonoPerso` varchar(15) DEFAULT NULL,
  `UsuarioPerso` varchar(50) DEFAULT NULL,
  `ContraseñaPerso` varchar(50) DEFAULT NULL,
  `Rol` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `persona`
--

INSERT INTO `persona` (`IdPersona`, `NombrePerso`, `ApellidoPerso`, `EmailPerso`, `DireccionPerso`, `TelefonoPerso`, `UsuarioPerso`, `ContraseñaPerso`, `Rol`) VALUES
(1, 'juan', 'MORA', 'esteban14juan@gmail.com', 'sena', '11111111111', 'juan', 'scrypt:32768:8:1$dDFIrbMXstL1YHiY$81307cbaddda88be', 'Comprador'),
(3, 'MARIA', 'MORA', 'nai@gmail.com', 'sena', '111111111111', 'DANI', 'scrypt:32768:8:1$BpSoI37SGXhNGgka$b8c3b67343925a79', 'Administrador'),
(4, 'felipe', 'castaño', 'feli@gmail.com', 'sena', '1234567890', 'felipe', 'scrypt:32768:8:1$aZB9IJO5G7vtUDgK$eb0ace7c89b9f0f6', 'Administrador'),
(6, '2222222', '222222222', '222222222@222', '22222222', '22222222', '2222', 'juan123', 'Administrador');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `canciones`
--
ALTER TABLE `canciones`
  ADD PRIMARY KEY (`IdCancion`);

--
-- Indices de la tabla `compras`
--
ALTER TABLE `compras`
  ADD PRIMARY KEY (`idcompra`);

--
-- Indices de la tabla `persona`
--
ALTER TABLE `persona`
  ADD PRIMARY KEY (`IdPersona`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `canciones`
--
ALTER TABLE `canciones`
  MODIFY `IdCancion` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT de la tabla `compras`
--
ALTER TABLE `compras`
  MODIFY `idcompra` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `persona`
--
ALTER TABLE `persona`
  MODIFY `IdPersona` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
