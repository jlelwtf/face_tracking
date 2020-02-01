import os

urls = [
    'http://documents.epfl.ch/groups/c/cv/cvlab-pom-video1/www/4p-c0.avi',
    'http://documents.epfl.ch/groups/c/cv/cvlab-pom-video1/www/4p-c1.avi',
    'http://documents.epfl.ch/groups/c/cv/cvlab-pom-video1/www/4p-c2.avi',
    'http://documents.epfl.ch/groups/c/cv/cvlab-pom-video1/www/4p-c3.avi',
    'http://documents.epfl.ch/groups/c/cv/cvlab-pom-video1/www/6p-c0.avi',
    'http://documents.epfl.ch/groups/c/cv/cvlab-pom-video1/www/6p-c1.avi',
    'http://documents.epfl.ch/groups/c/cv/cvlab-pom-video1/www/6p-c2.avi',
    'http://documents.epfl.ch/groups/c/cv/cvlab-pom-video1/www/6p-c3.avi',
    'https://documents.epfl.ch/groups/c/cv/cvlab-pom-video1/www/campus4-c0.avi',
    'https://documents.epfl.ch/groups/c/cv/cvlab-pom-video1/www/campus4-c1.avi',
    'https://documents.epfl.ch/groups/c/cv/cvlab-pom-video1/www/campus4-c2.avi',
    'https://documents.epfl.ch/groups/c/cv/cvlab-pom-video3/www/terrace1-c0.avi',
    'https://documents.epfl.ch/groups/c/cv/cvlab-pom-video3/www/terrace1-c1.avi',
    'https://documents.epfl.ch/groups/c/cv/cvlab-pom-video3/www/terrace1-c2.avi',
    'https://documents.epfl.ch/groups/c/cv/cvlab-pom-video3/www/terrace1-c3.avi',
    'https://documents.epfl.ch/groups/c/cv/cvlab-pom-video2/www/passageway1-c0.avi',
    'https://documents.epfl.ch/groups/c/cv/cvlab-pom-video2/www/passageway1-c1.avi',
    'https://documents.epfl.ch/groups/c/cv/cvlab-pom-video2/www/passageway1-c2.avi',
    'https://documents.epfl.ch/groups/c/cv/cvlab-pom-video3/www/passageway1-c3.avi',
    'https://documents.epfl.ch/groups/c/cv/cvlab-pom-video2/www/match5-c0.avi',
    'https://documents.epfl.ch/groups/c/cv/cvlab-pom-video2/www/match5-c1.avi',
    'https://documents.epfl.ch/groups/c/cv/cvlab-pom-video2/www/match5-c2.avi',
    'https://documents.epfl.ch/groups/c/cv/cvlab-pom-video2/www/match5-c3.avi'
]

download_dir = 'video'

if __name__ == '__main__':
    if not os.path.exists(download_dir):
        os.mkdir(download_dir)

    for url in urls:
        os.system(
            'wget '
            f'{url} '
            f'-P {download_dir}'
        )
