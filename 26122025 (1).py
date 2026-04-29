from picamera2 import Picamera2
import cv2
import numpy as np
import tflite_runtime.interpreter as tflite
import time

IMG_SIZE = 224

interpreter = tflite.Interpreter(model_path="/home/raspi/cat_dog/ta/cats_dogs_model.tflite")
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration(main={"size": (640, 480)}))
picam2.start()

time.sleep(2)

print("Running... Press q to exit")

while True:
    frame = picam2.capture_array()

    frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)

    img = cv2.resize(frame, (IMG_SIZE, IMG_SIZE))
    img = img / 255.0
    img = np.expand_dims(img, axis=0).astype(np.float32)

    interpreter.set_tensor(input_details[0]['index'], img)
    interpreter.invoke()

    output = interpreter.get_tensor(output_details[0]['index'])[0][0]

    label = "Dog" if output > 0.5 else "Cat"
    confidence = output if output > 0.5 else (1 - output)

    text = f"{label}: {confidence:.2f}"

    cv2.putText(frame, text, (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1,
                (0, 255, 0), 2)

    cv2.imshow("Live Prediction", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
picam2.stop()
