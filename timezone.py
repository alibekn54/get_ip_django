from timezonefinder import TimezoneFinder

tf = TimezoneFinder()
tz = tf.timezone_at(lng=52.5061, lat=13.358)  # 'Europe/Berlin'
ee = tf.timezone_at(lng=1.0, lat=50.5)  # 'Etc/GMT'

print(ee)