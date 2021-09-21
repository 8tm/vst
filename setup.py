import datetime
import setuptools

version = datetime.datetime.now().strftime('%y.%-m.%-d')
setuptools.setup(
    name='mts',
    version=version,
    author='Tadeusz Miszczyk',
    author_email='tadeusz.miszczyk@gmail.com',
    description=('Useful scripts for Mekatron project',),
    url='https://github.com/8tm/mts',
    package_dir={'': 'src'},
    packages=setuptools.find_namespace_packages(where='src'),
    include_package_data=True,
    install_requires=[
        'pydub==0.25.1',
        'SpeechRecognition==3.8.1',
        'ffmpeg-python==0.2.0',
    ],
    extras_require={
        'tests': [
            'flake8==3.8.3',
            'flake8-commas==2.0.0',
            'flake8-import-order==0.18.1',
            'flake8-quotes==3.2.0',
            'pytest==6.0.1',
            'pytest-cov==2.10.0',
            'pytest-mock==3.2.0',
            'pytest-random-order==1.0.4',
            'pytest-xdist==1.29.0',
            'pytest-parallel',
            'mypy==0.812',
        ],
        'dev-tools': [
            'pip-search==0.0.7',
        ],
    },
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
    ],
    python_requires='>=3.7.4',
    entry_points={
        'console_scripts': [
            'mts_wav_to_text = mts.wav_to_text:main',
            'mts_audio_to_wav = mts.audio_to_wav:main',
        ],
    },
)
