'''
Function for training the classifier to do subsequent analysis.
- data needs to be already split into train- and testdata and information has to be stored in split.csv
- Models need to be already established
- ground truth-data needs to be downloaded and provided for the corresponding files in split.csv

Data Processing

'''

# -----------------------------------
# Step 0: Import all needed libraries
# -----------------------------------

import pandas as pd
import random
from os import path
import glob

import detectree as dtr
from detectree import filters, image_descriptor, pixel_features

from joblib import load


def train_classifier(directory, split_df_filepath, response_dir, models_dir):
    img_filepath = random.choice(glob.glob(f'{directory}*.tif'))
    pfb = pixel_features.PixelFeaturesBuilder()
    X = pfb.build_features_from_filepath(img_filepath)
    kernels = filters.get_gabor_filter_bank(frequencies=(.1, .25, .4),
                                            num_orientations=(4, 8, 8))
    response_bins_per_axis = 4
    num_color_bins = 8

    img_descr = image_descriptor.compute_image_descriptor_from_filepath(
        img_filepath,
        kernels=kernels,
        response_bins_per_axis=response_bins_per_axis,
        num_color_bins=num_color_bins)

    ts = dtr.TrainingSelector(img_dir=directory)
    split_df = pd.read_csv(split_df_filepath)
    evr = 0.922583197079706

    img_filepath = split_df[split_df['train']]['img_filepath'].sample(1).iloc[0]
    response_filepath = path.join(response_dir, path.basename(img_filepath))

    # load models
    img_cluster_0 = load(f'{models_dir}/0.joblib')
    img_cluster_1 = load(f'{models_dir}/1.joblib')
    img_cluster_2 = load(f'{models_dir}2.joblib')
    img_cluster_3 = load(f'{models_dir}/3.joblib')

    clf_dict = {0: img_cluster_0, 1: img_cluster_1, 2: img_cluster_2, 3: img_cluster_3}
    # load a non-training tile
    img_row = split_df[~split_df['train']].iloc[0]
    img_filepath = img_row['img_filepath']
    img_cluster = img_row['img_cluster']

    # get the classifier of the tile's corresponding first-level cluster
    clf = clf_dict[img_cluster]

    # classify the tile
    y_nonrefined = dtr.Classifier(refine=False).classify_img(img_filepath, clf)
    # `refine=True` by default in `Classifier`
    c = dtr.Classifier()
    y = c.classify_img(img_filepath, clf)

if __name__ == "__main__":
    directory_1 = '/content/drive/MyDrive/data/interim/tiles/'
    split_df_filepath_1 = '/content/drive/MyDrive/data/interim/tiles/split.csv'
    response_dir_1 = '/content/drive/MyDrive/data/interim/response_tiles'
    models_dir_1 = '/content/drive/MyDrive/data/models'

    train_classifier(directory_1, split_df_filepath_1, response_dir_1, models_dir_1)
