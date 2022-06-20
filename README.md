# Detectree 

Nowadays, earth systems are altered to the needs of humankind, as our planet is dominated by human influence. At the same time, however, while the world seeks to slow down the pace of climate change, tree cover in cities is shrinking rapidly, leading to an increase in urban temperatures and air pollution. Because air pollution is linked to a variety of diseases in humans and the majority of the world’s population lives in cities, trees are essential for healthy communities. In addition, trees encourage physical activity, promote social ties and are believed to reduce stress among people. In this study, we aim to assess the benefits of trees in cities on people's health and social well-being.

# Download Aerial Images

The Mapbox API allows for programmatic access of satellite data [4]. Mapbox tiles are returned as raster tiles, containing the pixel-based data stored as a grid structure in jpg format with 90% quality maximum. Although not ideal in terms of georeferencing and resolution, in this study, the Mapbox Raster Tiles API was used for further analysis. With the ['convert_coordinates.py'](https://git.uibk.ac.at/csaw6507/detectree/-/blob/main/convert_coordinates.py) programm one obtains the relevant tile depending on the latitude and longitude as well as the zoom factor. With the given geographical boundaries the tiles are downloaded with the [' mapbox_city.py'](https://git.uibk.ac.at/csaw6507/detectree/-/blob/main/mapbox_athens.py) program and stored in the folder for the raw tiles of each city.

# Classify Pixels 
A schematic way to classify IBK tiles. For a detailed explanation we refer to the report or to the explanations of the Jupyter notebook [Ibk_detectree.ipynb](https://git.uibk.ac.at/csaw6507/detectree/-/blob/main/Ibk_detectree.ipynb).

To classify trees of the loaded satellite images, it is not sufficient to read out the respective pixel value, i.e.the color, to solve the binary classification problem. Instead, one must refer to a 27-dimensional feature vector [2]. The binary classification at the pixel level between tree-like and non-tree-like pixels is taken by the Detectree module with the `pixel_features.PixelFeaturesBuilder()` function. The output of the function is a matrix in which each row represents a pixel of the original RGB image, with the respective features of the pixel added as a column.
The task of classifying tree/non-tree pixels becomes a supervised learning problem, where a classifier that maps the pixel features to the tree/non-tree responses is trained and later used to classify the values for the remaining pixels [1]. The tranied AdaBoost classifier are then stored in the folder [models](https://git.uibk.ac.at/csaw6507/detectree/-/tree/main/models).

> Bulding the PixelFeaturesBuilder:

`pfb = pixel_features.PixelFeaturesBuilder()`

`X = pfb.build_features_from_filepath(img_filepath)`

> classify the ibk tile:

`y_nonrefined = dtr.Classifier(refine=False).classify_img(ibk_img_filepath, clf)`

`c = dtr.Classifier()`

`y = c.classify_img(ibk_img_filepath, clf)`

> open ibk classifiaction:

`with rio.open(ibk_img_filepath) as src:
    plot.show(src.read())`
    
`plt.imshow(y_nonrefined)`

`plt.figure()`

`plt.imshow(y)`

`picture = plt.imshow(y)`

The "[train_classifier.py](https://git.uibk.ac.at/csaw6507/detectree/-/blob/main/train_classifier.py)" program can be used to train the classifier using predefined train and test data and a ground truth mask. The information about the train/test split ratio is contained in the split.csv table.

# Analysis and validation of the predicted tiles

We can determine the proportion of predicted tree-like and non-tree-like pixels of each image using our program [pixel_color.py](https://git.uibk.ac.at/csaw6507/detectree/-/blob/main/pixel-color.py). A list of the "predicted_tiles" from the corresponding directory is created and in the next step the proportion of tree-like pixels is determined. After running the classification function, the image is further refined to neglect weakly detected tree-like pixels. The tree-like pixels are then stored as white pixels, while the non-tree-like pixels are stored as black ones. Using an analysis of the colors for each pixel in the image with the `pixel_color(path1)` function, the proportion of classified pixels can be determined. 
To provide an accuracy of the algorithm, we divided the "predicted_tiles" in the program according to high and low tree coverage, respectively, and later randomly selected two tiles from each group. These tiles were then compared to the tree coverage we manually determined to maintain the accuracy of the classification. 


# Data Analysis

Data analysis was performed using the two Jupyter notebooks [Analysis_data_lab_1.ipynb](https://git.uibk.ac.at/csaw6507/detectree/-/blob/main/Analysis_data_lab_1.ipynb) and [Analysis_data_lab_2.ipynb](https://git.uibk.ac.at/csaw6507/detectree/-/blob/main/Analysis_data_lab_2.ipynb) . Further explanations can be taken from the description.

# References
1. Tree detection from aerial imagery in Python, https://github.com/martibosch/detectree
2.	Yang, L., Wu, X., Praun, E., & Ma, X. (2009). Tree detection from aerial imagery. In Proceedings of the 17th ACM SIGSPATIAL International Conference on Advances in Geographic Information Systems (pp. 131-137). ACM.
3.	Oliva, A., & Torralba, A. (2001). Modeling the shape of the scene: A holistic representation of the spatial envelope. International journal of computer vision, 42(3), 145-175.
4. https://docs.mapbox.com/data/tilesets/guides/imagery/, 01.06.2022

