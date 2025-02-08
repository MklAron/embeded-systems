from sense_hat import SenseHat
from time import sleep
sense = SenseHat()
def calculate_sea_level_pressure(P, T, h=125):
    P0 = P * (1 - (0.0065 * h) / (T + 0.0065 * h + 273.15)) ** -5.257
    return P0
def get_forecast(P0, tendency):
    Z = None
    forecast = None

    if tendency == 'falling' and 985 <= P0 <= 1050:
        Z = 127 - 0.12 * P0
        forecast_table = {
            1: "Settled Fine",
            2: "Fine Weather",
            3: "Fine, Becoming Less Settled",
            4: "Fairly Fine, Showery Later",
            5: "Showery, Becoming More Unsettled",
            6: "Unsettled, Rain Later",
            7: "Rain at Times, Worse Later",
            8: "Rain at Times, Becoming Very Unsettled",
            9: "Very Unsettled, Rain"
        }
    elif tendency == 'steady' and 960 <= P0 <= 1033:
        Z = 144 - 0.13 * P0
        forecast_table = {
            10: "Settled Fine",
            11: "Fine Weather",
            12: "Fine, Possibly Showers",
            13: "Fairly Fine, Showers Likely",
            14: "Showery, Bright Intervals",
            15: "Changeable, Some Rain",
            16: "Unsettled, Rain at Times",
            17: "Rain at Frequent Intervals",
            18: "Very Unsettled, Rain"
        }
    elif tendency == 'rising' and 947 <= P0 <= 1030:
        Z = 185 - 0.16 * P0
        forecast_table = {
            20: "Settled Fine",
            21: "Fine Weather",
            22: "Becoming Fine",
            23: "Fairly Fine, Improving",
            24: "Fairly Fine, Possibly Showers Early",
            25: "Showery Early, Improving",
            26: "Changeable, Mending",
            27: "Rather Unsettled, Clearing Later",
            28: "Unsettled, Probably Improving",
            29: "Unsettled, Short Fine Intervals",
            30: "Very Unsettled, Finer at Times",
            31: "Stormy, Possibly Improving",
            32: "Stormy, Much Rain"
        }

    if Z is not None:
        Z_rounded = round(Z)
        forecast = forecast_table.get(Z_rounded, "Unknown Forecast")

    return Z, forecast
previous_pressure = None
while True:
    t = sense.get_temperature()
    p = sense.get_pressure()
    h = sense.get_humidity()
    t = round(t, 1)
    p = round(p, 1)
    h = round(h, 1)
    P0 = calculate_sea_level_pressure(p, t)
    if previous_pressure is None:
        tendency = "steady"
    else:
        if P0 - previous_pressure > 1.6:
            tendency = "rising"
        elif previous_pressure - P0 > 1.6:
            tendency = "falling"
        else:
            tendency = "steady"
    Z, forecast = get_forecast(P0, tendency)
    message = f"Temperature: {t}C, Pressure: {p}hPa, Humidity: {h}%, Sea-Level Pressure: {round(P0, 1)}hPa"
    print(message)
    if Z is not None:
        print(f"Forecast: {forecast} (Z = {Z:.2f}, Tendency: {tendency})")
    else:
        print(f"Forecast: Not Available (Tendency: {tendency})")
    previous_pressure = P0
    sleep(1)
