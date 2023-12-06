from amplitude import Amplitude, Identify, EventOptions, BaseEvent

def callback_func(event, code, message=None):
  # callback function that takes three input parameters
  # event: the event that triggered this callback
  # code: status code of request response
  # message: a optional string message for more detailed information
  print(f"Disparado evento {event} con codigo {code} y mensaje {message}")

amplitude = Amplitude("b4089e52afe753cb2348cdf4e9738848")
#amplitude.configuration.server_zone = "EU"
amplitude.configuration.callback = callback_func
amplitude.configuration.min_id_length = 1

identify_obj=Identify()
identify_obj.set("user-subscription-type", "PRO_5")
amplitude.identify(identify_obj, EventOptions(user_id="628"))

# Track a basic event
# One of user_id and device_id is required
#event = BaseEvent(event_type="Posti - Scheduled", user_id="628")
#amplitude.track(event)