"""fit (learn) vs transform (apply learned params)."""
import numpy as np
from sklearn.preprocessing import StandardScaler

def main():
    train = np.array([[1.0], [2.0], [3.0]])
    test = np.array([[4.0], [5.0]])

    scaler = StandardScaler().fit(train)
    print("train mean/std:", scaler.mean_, scaler.scale_)
    print("train scaled:\n", scaler.transform(train))
    print("test scaled with train params:\n", scaler.transform(test))

if __name__ == "__main__":
    main()