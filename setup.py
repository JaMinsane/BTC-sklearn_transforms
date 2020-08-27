from setuptools import setup
from impyute.imputation.cs import mice

setup(
      name='my_custom_sklearn_transforms',
      version='1.0',
      description='''
            This is a sample python package for encapsulating custom
            tranforms from scikit-learn into Watson Machine Learning
      ''',
      url='https://github.com/JaMinsane/sklearn_transforms/',
      author='James Jaramillo',
      author_email='james.jh03@gmail.com',
      license='BSD',
      packages=[
            'my_custom_sklearn_transforms',
            mice
      ],
      zip_safe=False
)
