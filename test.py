from gaze_guard import AttentionController

controller = AttentionController()

while True:
    if controller.is_user_attentive():
        print("Looking at AI")
    else:
        print("Not looking")