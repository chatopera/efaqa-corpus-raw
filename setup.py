# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
LONGDOC = """
Emotional First Aid Raw Dataset
===============================

心理咨询问答原始语料库，仅限研究用途。心理咨询问答原始语料库（以下也称为“本数据集”，“本语料库”）是为应用人工智能技术于心理咨询领域制作的高品质语料，语料是爬取心理咨询领域公开的网站的数据，经过整理和脱敏制作而成。消息总文本字符数四千四百多万，具体说明见下。

https://github.com/chatopera/efaqa-corpus-raw

"""

setup(
    name='efaqa-corpus-raw',
    version='1.0.3',
    description='心理咨询问答原始语料库（以下也称为“本数据集”，“本语料库”）是为应用人工智能技术于心理咨询领域制作的高品质语料，语料是爬取心理咨询领域公开的网站的数据，经过整理和脱敏制作而成。消息总文本字符数四千四百多万。',
    long_description=LONGDOC,
    author='Hai Liang Wang',
    author_email='hain@chatopera.com',
    url='https://github.com/chatopera/efaqa-corpus-raw',
    license="Chunsong Public License, version 1.0",
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Natural Language :: Chinese (Simplified)',
        'Natural Language :: Chinese (Traditional)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Text Processing',
        'Topic :: Text Processing :: Indexing',
        'Topic :: Text Processing :: Linguistic'],
    keywords='corpus,machine-learning,NLU,NLP,chatbot',
    packages=find_packages(),
    install_requires=[
        'chatoperastore>=1.2.0'
    ],
    package_data={
        'efaqa_corpus_raw': [
            '**/**/.gitignore',
            'LICENSE']})
