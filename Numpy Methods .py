{"cells":[{"cell_type":"code","execution_count":1,"metadata":{},"outputs":[],"source":["import numpy as np\n","\n","x = np.zeros((4,4))"]},{"cell_type":"code","execution_count":2,"metadata":{},"outputs":[{"data":{"text/plain":["array([[0., 0., 0., 0.],\n","       [0., 0., 0., 0.],\n","       [0., 0., 0., 0.],\n","       [0., 0., 0., 0.]])"]},"execution_count":2,"metadata":{},"output_type":"execute_result"}],"source":["x"]},{"cell_type":"code","execution_count":3,"metadata":{},"outputs":[{"data":{"text/plain":["array([[1., 1., 1., 1., 1.],\n","       [1., 1., 1., 1., 1.],\n","       [1., 1., 1., 1., 1.],\n","       [1., 1., 1., 1., 1.],\n","       [1., 1., 1., 1., 1.]])"]},"execution_count":3,"metadata":{},"output_type":"execute_result"}],"source":["np.ones((5,5))"]},{"cell_type":"code","execution_count":4,"metadata":{},"outputs":[{"data":{"text/plain":["array([[1.09576765e-311, 1.09576677e-311, 0.00000000e+000,\n","        0.00000000e+000, 0.00000000e+000, 0.00000000e+000,\n","        0.00000000e+000],\n","       [0.00000000e+000, 0.00000000e+000, 0.00000000e+000,\n","        0.00000000e+000, 0.00000000e+000, 0.00000000e+000,\n","        0.00000000e+000],\n","       [0.00000000e+000, 0.00000000e+000, 0.00000000e+000,\n","        0.00000000e+000, 0.00000000e+000, 0.00000000e+000,\n","        0.00000000e+000],\n","       [0.00000000e+000, 0.00000000e+000, 0.00000000e+000,\n","        0.00000000e+000, 0.00000000e+000, 0.00000000e+000,\n","        0.00000000e+000],\n","       [0.00000000e+000, 0.00000000e+000, 0.00000000e+000,\n","        0.00000000e+000, 0.00000000e+000, 0.00000000e+000,\n","        0.00000000e+000],\n","       [0.00000000e+000, 0.00000000e+000, 0.00000000e+000,\n","        0.00000000e+000, 0.00000000e+000, 0.00000000e+000,\n","        0.00000000e+000],\n","       [0.00000000e+000, 0.00000000e+000, 0.00000000e+000,\n","        0.00000000e+000, 0.00000000e+000, 0.00000000e+000,\n","        0.00000000e+000]])"]},"execution_count":4,"metadata":{},"output_type":"execute_result"}],"source":["np.empty((7,7))"]},{"cell_type":"code","execution_count":5,"metadata":{},"outputs":[],"source":["# np.empty() creates desired shape of array as shown in above result with random data"]},{"cell_type":"code","execution_count":6,"metadata":{},"outputs":[{"data":{"text/plain":["array([1, 4, 5, 7])"]},"execution_count":6,"metadata":{},"output_type":"execute_result"}],"source":["# converting python list to numpy array:\n","\n","l = [1, 4, 5, 7]\n","\n","np.array(l)"]}],"metadata":{"language_info":{"codemirror_mode":{"name":"ipython","version":3},"file_extension":".py","mimetype":"text/x-python","name":"python","nbconvert_exporter":"python","pygments_lexer":"ipython3","version":3},"orig_nbformat":4},"nbformat":4,"nbformat_minor":2}
