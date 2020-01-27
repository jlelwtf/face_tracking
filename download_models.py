import os

urls = [
    'https://github.com/davisking/dlib-models/raw/master/shape_predictor_68_face_landmarks.dat.bz2',
    'https://github.com/davisking/dlib-models/raw/master/dlib_face_recognition_resnet_model_v1.dat.bz2',
]

download_dir = 'descriptor_calculator'

if __name__ == '__main__':
    for url in urls:
        os.system(
            f'wget {url} -P {download_dir}'
        )

        file_name = os.path.join(download_dir, url.split('/')[-1])

        os.system(
            f'bzip2 -d {file_name} '
        )

