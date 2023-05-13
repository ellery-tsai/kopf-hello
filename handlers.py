import kopf


@kopf.timer('kopfexamples', interval=1)
def my_timer(spec, **kwargs):
    print(f"Object's spec: {spec}")
