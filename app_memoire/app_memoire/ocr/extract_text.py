#import keras_ocr
import easyocr
import pandas as pd
import time

def extract_text (img_path) :

    """ #recognizer = keras_ocr.recognition.Recognizer()
    #recognizer.model.load_weights('/home/app_memoire/app_memoire/ocr/recognizer_composer.h5')

    #pipeline = keras_ocr.pipeline.Pipeline(recognizer=recognizer, text_threshold=0.4)
    #pipeline = keras_ocr.pipeline.Pipeline()
    prediction_groups = pipeline.recognize([img_path])

    arr_terms = []
    tuple_list = prediction_groups[0]

    for item in tuple_list:
        arr_terms.append((item[0], 0.9))

    print(arr_terms) """
    """ fig, axs = plt.subplots(nrows = (len(images)), figsize=(20,20))
    for ax, image, predictions in zip(axs, images, prediction_groups):
        keras_ocr.tools.drawAnnotations(image=image, predictions=predictions, ax=ax)
        print(predictions) """
    start_time = time.time()

    reader = easyocr.Reader(['fr', 'en', 'de'], gpu = True)
    result = reader.readtext(img_path)
    df = pd.DataFrame(result, columns=['bbox','text','conf'])
    df = df.drop(['bbox'], axis=1)
    arr_terms = list(df.itertuples(index=False, name=None))
    arr_terms = list(filter(lambda n: n[1] > 0.1, arr_terms))
    print(arr_terms)
    print("--- OCR : %s seconds ---" % (time.time() - start_time))

    return arr_terms