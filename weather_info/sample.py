x={
    "type": "Feature",
    "geometry": {
        "type": "Point",
        "coordinates": [-0.25, 51.5, 9]
    },
    "properties": {
        "meta": {
            "updated_at": "2022-06-29T13:37:42Z",
            "units": {
                "air_pressure_at_sea_level": "hPa",
            }
        },
        "timeseries": [{
                "time": "2022-06-29T16:00:00Z",
                "data": {
                    "instant": {
                        "details": {
                            "air_pressure_at_sea_level": 1010.8,
                            "air_temperature": 19.5,
                            "wind_speed": 5.8
                        }
                    },
                    "next_12_hours": {
                        "summary": {
                            "symbol_code": "lightrain"
                        }
                    },
                    "next_1_hours": {
                        "summary": {
                            "symbol_code": "cloudy"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    },
                    "next_6_hours": {
                        "summary": {
                            "symbol_code": "cloudy"
                        },
                        "details": {
                            "precipitation_amount": 0.0
                        }
                    }
                }
            }
            ]
    }
}

air_pressure_at_sea_level=x['properties']["timeseries"][0]["data"]["instant"]["details"]["air_pressure_at_sea_level"]
air_temperature=x['properties']["timeseries"][0]["data"]["instant"]["details"]["air_temperature"]
wind_speed=x['properties']["timeseries"][0]["data"]["instant"]["details"]["wind_speed"]
print(air_pressure_at_sea_level,air_temperature,wind_speed)
