#include <Python.h>
#include <stdio.h>

void print_python_bytes(PyObject *p)
{
	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	Py_ssize_t size = PyBytes_Size(p);
	printf("  size: %ld\n", size);

	char *str = PyBytes_AsString(p);
	printf("  trying string: %s\n", str);

	printf("  first 10 bytes: ");
	for (Py_ssize_t i = 0; i < size && i < 10; i++)
	{
		printf("%02x", (unsigned char)str[i]);
		if (i < size - 1 && i < 9)
			printf(" ");
	}
	printf("\n");
}

void print_python_list(PyObject *p)
{
	printf("[*] Python list info\n");
	Py_ssize_t size = PyList_Size(p);
	printf("[*] Size of the Python List = %ld\n", size);

	Py_ssize_t allocated = ((PyListObject *)p)->allocated;
	printf("[*] Allocated = %ld\n", allocated);
	for (Py_ssize_t i = 0; i < size; i++)
	{
		PyObject *item = PyList_GetItem(p, i);
		const char *type = item->ob_type->tp_name;
		printf("Element %ld: %s\n", i, type);
		if (PyBytes_Check(item))
		       	print_python_bytes(item);
	}
}
