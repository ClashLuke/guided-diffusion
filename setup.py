import setuptools

setuptools.setup(
    name="guided_diffusion",
    packages=setuptools.find_packages(),
    install_requires=["blobfile>=1.0.5", "torch", "tqdm"],
)
