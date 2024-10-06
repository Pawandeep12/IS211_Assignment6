class ConversionNotPossible(Exception):
    pass


conversion_factors = {
    'celsius': {
        'kelvin': lambda c: c + 273.15,
        'fahrenheit': lambda c: (c * 9 / 5) + 32,
    },
    'fahrenheit': {
        'celsius': lambda f: (f - 32) * 5 / 9,
        'kelvin': lambda f: (f + 459.67) * 5 / 9,
    },
    'kelvin': {
        'celsius': lambda k: k - 273.15,
        'fahrenheit': lambda k: (k * 9 / 5) - 459.67,
    },
    'miles': {
        'yards': lambda m: m * 1760,
        'meters': lambda m: m * 1609.34,
    },
    'yards': {
        'miles': lambda y: y / 1760,
        'meters': lambda y: y * 0.9144,
    },
    'meters': {
        'miles': lambda m: m / 1609.34,
        'yards': lambda m: m / 0.9144,
    }
}


def convert(fromUnit, toUnit, value):
    fromUnit = fromUnit.lower()
    toUnit = toUnit.lower()

    if fromUnit == toUnit:
        return value

    if fromUnit in conversion_factors and toUnit in conversion_factors[fromUnit]:
        return conversion_factors[fromUnit][toUnit](value)

    raise ConversionNotPossible(f"Cannot convert from {fromUnit} to {toUnit}.")
