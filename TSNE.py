import numpy as np
import pandas as pd
import numpy as np
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import seaborn as sns
# get the features from the file features.txt
def tsne(path):
    features = list()
    with open(path+'features.txt') as f:
        features = [line.split()[1] for line in f.readlines()]
    print('No of Features: {}'.format(len(features)))
    # get the data from txt files to pandas dataffame
    X_train = pd.read_csv(path+'train\X_train.txt', delim_whitespace=True, header=None)

    # add subject column to the dataframe
    X_train['subject'] = pd.read_csv(path+'train\subject_train.txt', header=None, squeeze=True)

    y_train = pd.read_csv(path+'train\y_train.txt', names=['Activity'], squeeze=True)
    y_train_labels = y_train.map({1: 'WALKING', 2:'WALKING_UPSTAIRS',3:'WALKING_DOWNSTAIRS',\
                           4:'SITTING', 5:'STANDING',6:'LAYING'})

    # put all columns in a single dataframe
    train = X_train
    train['Activity'] = y_train
    train['ActivityName'] = y_train_labels
    train.sample()
    train.shape
    # get the data from txt files to pandas dataffame
    X_test = pd.read_csv(path+'test\X_test.txt', delim_whitespace=True, header=None)

    # add subject column to the dataframe
    X_test['subject'] = pd.read_csv(path+'test\subject_test.txt', header=None, squeeze=True)

    # get y labels from the txt file
    y_test = pd.read_csv(path+'test\y_test.txt', names=['Activity'], squeeze=True)
    y_test_labels = y_test.map({1: 'WALKING', 2:'WALKING_UPSTAIRS',3:'WALKING_DOWNSTAIRS',\
                           4:'SITTING', 5:'STANDING',6:'LAYING'})


    # put all columns in a single dataframe
    test = X_test
    test['Activity'] = y_test
    test['ActivityName'] = y_test_labels
    test.sample()
    test.shape
    print('No of duplicates in train: {}'.format(sum(train.duplicated())))
    print('No of duplicates in test : {}'.format(sum(test.duplicated())))
    print('We have {} NaN/Null values in train'.format(train.isnull().values.sum()))
    print('We have {} NaN/Null values in test'.format(test.isnull().values.sum()))
    columns = train.columns

    # Removing '()' from column names
    columns = columns.str.replace('[()]','')
    columns = columns.str.replace('[-]', '')
    columns = columns.str.replace('[,]','')

    train.columns = columns
    test.columns = columns

    test.columns
    train.to_csv('train.csv', index=False)
    test.to_csv('test.csv', index=False)
    X_pre_tsne = train.drop(['subject', 'Activity', 'ActivityName'], axis=1)
    y_pre_tsne = train['ActivityName']
    perform_tsne(X_data=X_pre_tsne, y_data=y_pre_tsne, perplexities=[50])

def perform_tsne(X_data, y_data, perplexities, n_iter=1000, img_name_prefix='t-sne'):
    for index, perplexity in enumerate(perplexities):
        # perform t-sne
        print('\nperforming tsne with perplexity {} and with {} iterations at max'.format(perplexity, n_iter))
        X_reduced = TSNE(verbose=2, perplexity=perplexity).fit_transform(X_data)
        print('Done..')

        # prepare the data for seaborn
        print('Creating plot for this t-sne visualization..')
        df = pd.DataFrame({'x': X_reduced[:, 0], 'y': X_reduced[:, 1], 'label': y_data})

        # draw the plot in appropriate place in the grid
        sns.lmplot(data=df, x='x', y='y', hue='label', fit_reg=False, size=8, \
                   palette="Set1", markers=['^', 'v', 's', 'o', '1', '2'])
        plt.title("perplexity : {} and max_iter : {}".format(perplexity, n_iter))
        img_name = img_name_prefix + '_perp_{}_iter_{}.png'.format(perplexity, n_iter)
        print('saving this plot as image in present working directory...')
        plt.savefig(img_name)
        plt.show()
        img = mpimg.imread(img_name)
        plt.imshow(img)
        print('Done')
if __name__ == '__main__':
    path = r'F:\HARDataset\UCI HAR Dataset\UCI HAR Dataset\\'
    tsne(path)