# BIA_Project
This is a project on Stellar Object Classification


🚀 Project Overview


Classifying stellar objects, such as stars, galaxies, and quasars, is crucial in astronomical studies. This project applies multiple supervised learning algorithms to detect and classify stellar objects efficiently. The best-performing model, XGBoost, was deployed on Streamlit to provide real-time predictions.
![galaxy](https://github.com/user-attachments/assets/3ad541a8-3013-497f-be75-6b9464bbc8b7)

Stellar Object Classification 🌌🔭
1. Introduction 🌟
Astronomy is the study of everything in the universe beyond Earth’s atmosphere. Astronomers classify stars based on their spectral characteristics, helping to extract valuable information about the stars, such as their elements, temperature, density, and magnetic field. The classification of celestial objects, including stars, galaxies, and quasars, is a fundamental task in astronomy.

This project aims to classify stars, galaxies, and quasars (luminous supermassive black holes) based on their spectral characteristics. The classification scheme plays a critical role in understanding the structure and evolution of the universe.

2. Dataset Overview 📊
The dataset used in this project contains 100,000 observations of space captured by the Sloan Digital Sky Survey (SDSS). Each data point consists of 17 feature columns and 1 class column, which identifies the object as either a star, galaxy, or quasar.

Note: The SDSS data is publicly available. Please refer to the citation at the end for more information.

2.1 Features in the Dataset 🧑‍💻
obj_ID = Object Identifier: A unique value identifying the object in the image catalog used by the CAS.
alpha = Right Ascension angle (at J2000 epoch).
delta = Declination angle (at J2000 epoch).
u = Ultraviolet filter in the photometric system.
g = Green filter in the photometric system.
r = Red filter in the photometric system.
i = Near Infrared filter in the photometric system.
z = Infrared filter in the photometric system.
run_ID = Run Number, identifying the specific scan.
rereun_ID = Rerun Number, specifying how the image was processed.
cam_col = Camera column to identify the scanline within the run.
field_ID = Field number identifying each field.
spec_obj_ID = Unique ID used for optical spectroscopic objects. Two different observations with the same spec_obj_ID must share the output class.
class = Object class: Identifies the object as a galaxy, star, or quasar.
redshift = Redshift value, indicating the increase in wavelength.
plate = Plate ID, identifying each plate in SDSS.
MJD = Modified Julian Date, indicating when the SDSS data was taken.
fiber_ID = Fiber ID, identifying the fiber that pointed the light at the focal plane in each observation.
2.2 Background Information Useful to Understand the Data 🔭🌠
2.2.1 Celestial Sphere: An imaginary sphere surrounding Earth, where celestial objects can be projected onto its inner surface. It serves as a reference for observing the positions of stars and galaxies.

2.2.2 Celestial Equator: The great circle of the celestial sphere that lies in the same plane as Earth’s equator.

2.2.3 Ascension and Declination: These coordinates are used in astronomy to specify the position of celestial objects. Right Ascension (RA) indicates the horizontal position, while Declination (Dec) indicates the vertical position in the celestial sphere.

2.2.4 Photometric System: A method for measuring the brightness of light visible to the human eye. The UBV system, which includes ultraviolet, blue, and visual filters, was one of the first standardized systems for classifying stars based on their colors.

2.2.5 Redshift: Redshift occurs when the wavelength of light from an object stretches, shifting it towards the red part of the spectrum. It helps astronomers measure the velocity and distance of objects, especially distant galaxies and stars.

2.3 Useful Features ⚙️
Key features in the dataset that are particularly useful for the classification task include:

Navigation angles: Right Ascension (alpha) and Declination (delta).
Photometric system filters: u, g, r, i, z, which correspond to various wavelengths of light.
Redshift: Important for determining the distance and velocity of the object.
The remaining columns in the dataset, such as the object and image identifiers (e.g., obj_ID, spec_obj_ID), serve more as metadata and are less relevant for the learning stage of this classification task.


