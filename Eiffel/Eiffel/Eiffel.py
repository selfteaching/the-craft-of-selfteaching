
#!/usr/bin/env python3

"""
Support Eiffel-style preconditions and postconditions for functions.
An example for Python metaclasses.
"""

import unittest
from types import FunctionType as function

class EiffelBaseMetaClass(type):

    def __new__(meta, name, bases, dict):
        meta.convert_methods(dict)
        return super(EiffelBaseMetaClass, meta).__new__(
            meta, name, bases, dict)

    @classmethod
    def convert_methods(cls, dict):
        """Replace functions in dict with EiffelMethod wrappers.
        The dict is modified in place.
        If a method ends in _pre or _post, it is removed from the dict
        regardless of whether there is a corresponding method.
        """
        # find methods with pre or post conditions
        methods = []
        for k, v in dict.items():
            if k.endswith('_pre') or k.endswith('_post'):
                assert isinstance(v, function)
            elif isinstance(v, function):
                methods.append(k)
        for m in methods:
            pre = dict.get("%s_pre" % m)
            post = dict.get("%s_post" % m)
            if pre or post:
                dict[m] = cls.make_eiffel_method(dict[m], pre, post)


class EiffelMetaClass1(EiffelBaseMetaClass):
    # an implementation of the "eiffel" meta class that uses nested functions

    @staticmethod
    def make_eiffel_method(func, pre, post):
        def method(self, *args, **kwargs):
            if pre:
                pre(self, *args, **kwargs)
            rv = func(self, *args, **kwargs)
            if post:
                post(self, rv, *args, **kwargs)
            return rv

        if func.__doc__:
            method.__doc__ = func.__doc__

        return method


class EiffelMethodWrapper:

    def __init__(self, inst, descr):
        self._inst = inst
        self._descr = descr

    def __call__(self, *args, **kwargs):
        return self._descr.callmethod(self._inst, args, kwargs)


class EiffelDescriptor:

    def __init__(self, func, pre, post):
        self._func = func
        self._pre = pre
        self._post = post

        self.__name__ = func.__name__
        self.__doc__ = func.__doc__

    def __get__(self, obj, cls=None):
        return EiffelMethodWrapper(obj, self)

    def callmethod(self, inst, args, kwargs):
        if self._pre:
            self._pre(inst, *args, **kwargs)
        x = self._func(inst, *args, **kwargs)
        if self._post:
            self._post(inst, x, *args, **kwargs)
        return x


class EiffelMetaClass2(EiffelBaseMetaClass):
    # an implementation of the "eiffel" meta class that uses descriptors

    make_eiffel_method = EiffelDescriptor

class Tests(unittest.TestCase):

    def testEiffelMetaClass1(self):
        self._test(EiffelMetaClass1)

    def testEiffelMetaClass2(self):
        self._test(EiffelMetaClass2)

    def _test(self, metaclass):
        class Eiffel(metaclass=metaclass):
            pass

        class Test(Eiffel):
            def m(self, arg):
                """Make it a little larger"""
                return arg + 1

            def m2(self, arg):
                """Make it a little larger"""
                return arg + 1

            def m2_pre(self, arg):
                assert arg > 0

            def m2_post(self, result, arg):
                assert result > arg

        class Sub(Test):
            def m2(self, arg):
                return arg**2

            def m2_post(self, Result, arg):
                super(Sub, self).m2_post(Result, arg)
                assert Result < 100

        t = Test()
        print('in test')
        self.assertEqual(t.m(1), 2)
        self.assertEqual(t.m2(1), 2)
        self.assertRaises(AssertionError, t.m2, 0)

        s = Sub()
        print('in subtest')
        self.assertRaises(AssertionError, s.m2, 1)
        self.assertRaises(AssertionError, s.m2, 10)
        self.assertEqual(s.m2(5), 25)


if __name__ == "__main__":
    unittest.main()

with open('ScaleModel_SingleAPI_New.csv', 'w') as fw:
    with open('ScaleModel_SingleAPI_New.txt', 'r') as f:
        for line in f.readlines():
            # print(line)
            #type(line)
            ptn=r'<TestProfile Name="(\w*)".*Percentage="(.*)" Type=.*'
            result = re.findall(ptn,line)
            if (len(result) != 0):
                fw.write(str(result).replace("[","").replace("]","").replace("(","").replace(")","").replace("'",""))
                fw.write("\n")

# props.put("RPSTimes", "1");
# double rpmPerThreads = 60.0 / (3 * ${apiCount});

# int {name}_Threads = (int)Math.ceil(${{name}_baselineTPS} * ${devicesCount} / ${agentCount} /rpmPerThreads);
# double {name}_TPS = ${{name}_baselineTPS} * ${devicesCount} / ${agentCount};
# props.put("TC201800001_Napa_DVR_WatchAndTricks_TPS", String.valueOf(TC201800001_Napa_DVR_WatchAndTricks_TPS));
# int totalThreads = TC201800001_Napa_DVR_WatchAndTricks_Threads + ...
# props.put("totalThreads", String.valueOf(totalThreads));

with open('TestTPMCalculateCode.txt', 'w') as fw:
    fw.write(f'props.put("RPSTimes", "1");\n')
    fw.write(f'double rpmPerThreads = 60.0 / (3 * ${{apiCount}});\n')
    totalThreadsStr = 'int totalThreads = '
    with open('TestName.txt', 'r') as f:
        for name in f.readlines():
            if (len(name)) :
                name = name.replace('\n', '')
                totalThreadsStr += name+'_Threads'
                totalThreadsStr += ' + '
                fw.write(f'int {name}_Threads = (int)Math.ceil(${{{name}_baselineTPM}} * ${{devicesCount}} / ${{agentCount}} /rpmPerThreads);')
                fw.write('\n')
                fw.write(f'double {name}_TPM = ${{{name}_baselineTPM}} * ${{devicesCount}} / ${{agentCount}};')
                fw.write('\n')
                fw.write(f'props.put("{name}_TPM", String.valueOf({name}_TPM));')
                fw.write('\n')
    print(totalThreadsStr)
    fw.write(totalThreadsStr[:-3]+';\n')
    fw.write(f'props.put("totalThreads", String.valueOf(totalThreads));')


# props.put("RPSTimes", "1");
# Double rpsTime = 0.1;
# int rampUpTime = Integer.parseInt(vars.get("Rampup"));
# if(rampUpTime > 100)
# {	
# 	//rpsTime=0.01*rpsTime;
# Double TC201800001_Napa_DVR_WatchAndTricks_TPS = Double.parseDouble(props.get("TC201800001_Napa_DVR_WatchAndTricks_TPS")) * rpsTime;
# props.put("TC201800001_Napa_DVR_WatchAndTricks_TPS", String.valueOf(TC201800001_Napa_DVR_WatchAndTricks_TPS));
with open('TestTPMRampupCode.txt', 'w') as fw:
    fw.write(f'props.put("RPSTimes", "1");\n')
    fw.write(f'Double rpsTime = 0.1;\n')
    fw.write(f'int rampUpTime = Integer.parseInt(vars.get("Rampup"));\n')
    fw.write(f'if(rampUpTime > 100)\n')
    fw.write(f'{{\n')
    with open('TestName.txt', 'r') as f:
        for name in f.readlines():
            if (len(name)) :
                name = name.replace('\n', '')
                # fw.write(f'int {name}_Threads = (int)Math.ceil(${{{name}_baselineTPM}} * ${{devicesCount}} / ${{agentCount}} /rpmPerThreads);')
                fw.write(f'Double {name}_TPM = Double.parseDouble(props.get("{name}_TPM")) * rpsTime;\n')
                fw.write(f'props.put("{name}_TPM", String.valueOf({name}_TPM));\n')
    fw.write(f'}}\n')
