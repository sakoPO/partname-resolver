from enum import Enum


class Type(Enum):
    MLCC = "Multi layer ceramic capacitor"
    ElectrolyticAluminium = "Aluminium Electrolytic Capacitor"
    ThinFilmResistor = "Thin Film Resistor"
    ThickFilmResistor = "Thick Film Resistor"
    ThinFilmResistorArray = "Thin Film Resistor Array"
    ThickFilmResistorArray = "Thick Film Resistor Array"
