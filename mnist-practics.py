from sklearn import datasets, svm
from sklearn.model_selection import train_test_split

# サンプル画像データのロード
mnist = datasets.fetch_mldata('MNIST original', data_home='image/')
X = mnist.data / 255
y = mnist.target

# 訓練用データとテスト用データに分ける
X_train, X_test, y_train, y_test = train_test_split(
    X, y, train_size=1000, test_size=300
)

# 訓練用データで学習
clf = svm.SVC()
clf.fit(X_train, y_train)

# テスト用データで実際に試す
score = clf.score(X_test, y_test)
print(score)
