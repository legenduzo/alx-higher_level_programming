#include <Python.h>
#include <stdio.h>
#include <listobject.h>

/**
 * print_python_list_info - prints information about a python list object
 * @p: list object to print about
 */

void print_python_list_info(PyObject *p)
{
	int i;
	PyObject *item;
	int size = PyList_Size(p);
	int alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %d: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
