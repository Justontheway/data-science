import numpy as np
import scipy.weave as weave

# 使用scipy.weave可以调用C/C++的代码,从而提升性能
def my_sum(a):
    n = int(len(a))
    code = """
    int i;

    double counter;
    counter = 0;
    for(i = 0; i < n; i++) {
        counter += a(i);
    }
    return_val = counter;
    """

    err = weave.inline(
        code, ['a','n'],
        type_converters = weave.converters.blitz,
        compiler = "gcc"
    )
    return err

a = np.arange(0, 100000000, 1)

# 第一次调用weave会自动对C语言进行编译，此后则直接运行编译之后的代码
my_sum(a)

