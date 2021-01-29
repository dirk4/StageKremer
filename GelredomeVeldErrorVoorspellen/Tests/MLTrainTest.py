import unittest
import Controller.TensorFlow.MLTrain as mlt

class MyTestCase(unittest.TestCase):

    def test_avarage_accuracy(self):
        tl = mlt.MLTrain()
        tl.train_model()
        accuracy = tl.evaluate_dataset()
        assert (accuracy, 0.9)

if __name__ == '__main__':
    unittest.main()
