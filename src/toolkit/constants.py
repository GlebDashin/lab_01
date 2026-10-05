SAMPLE_CONSTANT: int = 10
CONVERSION: dict[str, tuple[str, float]] = {
    "mm": ("length", 0.001),
    "m": ("length", 1.0),
    "km": ("length", 1000.0),
    "cm": ("length", 0.01),
    "kg": ("mass", 1.0),
    "g": ("mass", 0.001),
    "c": ("temperature", 1.0),
    "f": ("temperature", 1.0),
    "k": ("temperature", 1.0),
}
