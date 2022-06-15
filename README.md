# Detectree 

Nowadays, earth systems are altered to the needs of humankind, as our planet is dominated by human influence. At the same time, however, while the world seeks to slow down the pace of climate change, tree cover in cities is shrinking rapidly, leading to an increase in urban temperatures and air pollution. Because air pollution is linked to a variety of diseases in humans and the majority of the world’s population lives in cities, trees are essential for healthy communities. In addition, trees encourage physical activity, promote social ties and are believed to reduce stress among people. In this study, we aim to assess the benefits of trees in cities on people's health and social well-being.

# Download Aerial Images

TEXT

# Classify Pixels 


> Bulding the PixelFeaturesBuilder
`pfb = pixel_features.PixelFeaturesBuilder()`
`X = pfb.build_features_from_filepath(img_filepath)`

> classify the ibk tile
`y_nonrefined = dtr.Classifier(refine=False).classify_img(ibk_img_filepath, clf)`
`c = dtr.Classifier()`
`y = c.classify_img(ibk_img_filepath, clf)`

> open ibk classifiaction 
`with rio.open(ibk_img_filepath) as src:
    plot.show(src.read())

plt.imshow(y_nonrefined)
plt.figure()
plt.imshow(y)
picture = plt.imshow(y)
`
