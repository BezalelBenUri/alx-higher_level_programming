#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - Prints basic info about Python lists
 * @p: Pointer to a Python object
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, i;
	PyObject *obj;

	printf("[*] Python list info\n");
	size = PyList_Size(p);
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		obj = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(obj)->tp_name);
		if (PyBytes_Check(obj))
			print_python_bytes(obj);
		else if (PyFloat_Check(obj))
			print_python_float(obj);
	}
}

/**
 * print_python_bytes - Prints basic info about Python bytes objects
 * @p: Pointer to a Python object
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	char *str;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	str = PyBytes_AsString(p);

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", str);

	if (size > 10)
		size = 10;

	printf("  first %ld bytes:", size + 1);
	for (i = 0; i <= size; i++)
		printf(" %02x", (unsigned char)str[i]);
	printf("\n");
}

/**
 * print_python_float - Prints basic info about Python float objects
 * @p: Pointer to a Python object
 */
void print_python_float(PyObject *p)
{
	PyObject *repr;

	printf("[.] float object info\n");
	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	repr = PyObject_Repr(p);
	printf("  value: %s\n", PyUnicode_AsUTF8(repr));
	Py_XDECREF(repr);
}

