from gaze_guard import AttentionController

def on_start():
    print("AI STARTED 🔊")

def on_stop():
    print("AI STOPPED 🔇")

controller = AttentionController()

controller.on_attention_gain = on_start
controller.on_attention_loss = on_stop

try:
    while True:
        pass
except KeyboardInterrupt:
    controller.stop()