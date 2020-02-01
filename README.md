Face tracking demo.
Tested on ubuntu 18.04.

####Requirements
- python 3.6
- pip
- bzip2

####Download data
To download videos:
```bash
python download_video.py
```

To download models:
```bash
python download_models.py
```

####Install libraries
```bash
pip install -r requiremets.txt
```

####Run project
run with custom arguments:
```bash
python run.py --video_path=<path to tracked video> --scale_view=<video zoom ratio> 
```
or run with default arguments (video_path='video/4p-c0.avi', scale_view=3.0)
```bash
python run.py
```
