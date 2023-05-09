
## 2to3

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 27.10% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 3.58% | `python` | `gc_collect_main` | gc |
| 3.38% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 2.51% | `python` | `_PyObject_Malloc (inlined)` | memory |
| 1.82% | `python` | `_PyObject_Free` | memory |
| 1.76% | `python` | `_Py_dict_lookup` | lookup |
| 1.73% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.68% | `python` | `sre_ucs1_match` | library |
| 1.62% | `python` | `tupledealloc` | memory |
| 1.46% | `python` | `_PyType_Lookup` | lookup |
| 1.34% | `python` | `visit_decref` | gc |
| 1.18% | `python` | `PyObject_GenericGetAttr` | dynamic |
| 1.18% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 0.97% | `python` | `visit_reachable` | gc |
| 0.77% | `python` | `_PyPegen_is_memoized` | unknown |
| 0.72% | `python` | `advance` | interpreter |
| 0.66% | `python` | `PyObject_GetAttr` | dynamic |
| 0.66% | `python` | `initialize_locals` | interpreter |
| 0.57% | `python` | `_PyObject_GetInstanceAttribute` | dynamic |
| 0.56% | `python` | `PyObject_RichCompare` | dynamic |
| 0.56% | `libc-2.31.so` | `pthread_attr_setschedparam` | libc |
| 0.55% | `python` | `tuple_alloc` | memory |
| 0.53% | `python` | `r_object` | unknown |
| 0.52% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.51% | `python` | `siphash13` | str |

## aiohttp

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 25.77% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 2.47% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 2.29% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 2.03% | `python` | `_PyObject_Malloc` | memory |
| 1.87% | `python` | `_PyObject_Free` | memory |
| 1.60% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.52% | `python` | `initialize_locals` | interpreter |
| 1.39% | `python` | `gc_collect_main` | gc |
| 1.16% | `python` | `_Py_dict_lookup` | lookup |
| 1.15% | `python` | `tupledealloc` | memory |
| 1.00% | `python` | `_PyType_Lookup` | lookup |
| 0.80% | `python` | `visit_decref` | gc |
| 0.76% | `libc-2.31.so` | `pthread_attr_setschedparam` | libc |
| 0.69% | `python` | `advance` | interpreter |
| 0.57% | `python` | `siphash13` | str |
| 0.55% | `python` | `PyObject_GenericGetAttr` | dynamic |
| 0.52% | `python` | `sre_ucs1_match` | library |
| 0.51% | `python` | `_PyFunction_Vectorcall` | unknown |

## async_generators

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 22.58% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 10.39% | `python` | `_PyErr_SetObject.part.0` | unknown |
| 3.11% | `python` | `_PyObject_Free` | memory |
| 3.01% | `python` | `async_gen_asend_iternext` | unknown |
| 2.58% | `python` | `_PyObject_Malloc` | memory |
| 2.54% | `python` | `PyType_GenericAlloc` | memory |
| 2.38% | `python` | `tupledealloc` | memory |
| 2.22% | `python` | `gc_collect_main` | gc |
| 2.01% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.91% | `python` | `async_gen_anext` | unknown |
| 1.85% | `python` | `PyErr_ExceptionMatches` | unknown |
| 1.64% | `python` | `_Py_NewReference` | memory |
| 1.55% | `python` | `_PyObject_MakeTpCall` | dynamic |
| 1.55% | `python` | `advance` | interpreter |
| 1.52% | `python` | `_PyTuple_FromArray` | tuple |
| 1.35% | `python` | `async_gen_asend_dealloc` | memory |
| 1.26% | `python` | `async_gen_wrapped_val_dealloc` | memory |
| 1.25% | `python` | `PyObject_GC_UnTrack` | gc |
| 1.23% | `python` | `_PyErr_Restore` | unknown |
| 1.22% | `python` | `_PyAsyncGenValueWrapperNew` | memory |
| 1.21% | `python` | `_PyGen_SetStopIterationValue` | unknown |
| 1.17% | `python` | `_PyGen_FetchStopIterationValue` | unknown |
| 1.09% | `python` | `PyObject_CallOneArg` | dynamic |
| 1.06% | `python` | `tuple_alloc` | memory |
| 1.04% | `python` | `type_call` | dynamic |
| 1.02% | `python` | `StopIteration_dealloc` | memory |
| 0.82% | `python` | `_PyTrash_begin` | gc |
| 0.82% | `python` | `PyObject_GC_Del` | gc |
| 0.76% | `python` | `StopIteration_init` | unknown |
| 0.76% | `python` | `_PyTrash_end` | gc |
| 0.75% | `python` | `visit_reachable` | gc |
| 0.73% | `python` | `initialize_locals` | interpreter |
| 0.71% | `python` | `BaseException_new` | memory |
| 0.70% | `python` | `visit_decref` | gc |
| 0.65% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 0.62% | `python` | `_PyErr_CreateException` | unknown |
| 0.61% | `python` | `PyType_IsSubtype` | dynamic |
| 0.53% | `python` | `_PyObject_GC_Link` | gc |
| 0.52% | `python` | `long_add` | int |

## async_tree

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 26.24% | `python` | `gc_collect_main` | gc |
| 18.06% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 6.94% | `python` | `visit_reachable` | gc |
| 6.63% | `python` | `visit_decref` | gc |
| 2.02% | `python` | `_PyObject_Malloc` | memory |
| 1.49% | `python` | `_PyObject_Free` | memory |
| 1.21% | `python` | `subtype_traverse` | gc |
| 1.04% | `python` | `initialize_locals` | interpreter |
| 0.94% | `python` | `_Py_dict_lookup` | lookup |
| 0.88% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 0.86% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.82% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.76% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 0.75% | `python` | `_PyType_Lookup` | lookup |
| 0.73% | `python` | `context_tp_dealloc` | memory |
| 0.68% | `python` | `_PyObject_GetMethod` | dynamic |
| 0.64% | `python` | `tupledealloc` | memory |
| 0.60% | `_asyncio.cpython-312-x86_64-linux-gnu.so` | `TaskObj_traverse` | library |
| 0.53% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.52% | `python` | `PyObject_GenericGetAttr` | dynamic |
| 0.51% | `python` | `subtype_dealloc` | memory |
| 0.50% | `python` | `_PyEval_Vector` | interpreter |

## async_tree_cpu_io_mixed

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 18.84% | `python` | `gc_collect_main` | gc |
| 16.08% | `python` | `k_mul` | int |
| 14.60% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 4.84% | `python` | `visit_reachable` | gc |
| 4.60% | `python` | `visit_decref` | gc |
| 2.79% | `python` | `_PyObject_Malloc` | memory |
| 2.22% | `python` | `_PyObject_Free` | memory |
| 1.31% | `python` | `PyErr_CheckSignals` | unknown |
| 1.22% | `math.cpython-312-x86_64-linux-gnu.so` | `factorial_partial_product` | library |
| 0.90% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 0.84% | `python` | `_Py_dict_lookup` | lookup |
| 0.83% | `python` | `subtype_traverse` | gc |
| 0.80% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 0.74% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.66% | `python` | `initialize_locals` | interpreter |
| 0.64% | `python` | `_PyObject_GetMethod` | dynamic |
| 0.64% | `python` | `PyThread_get_thread_ident` | unknown |
| 0.61% | `python` | `_PyType_Lookup` | lookup |
| 0.60% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.57% | `python` | `PyLong_FromUnsignedLong` | int |

## async_tree_io

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 33.95% | `python` | `gc_collect_main` | gc |
| 16.74% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 8.03% | `python` | `visit_reachable` | gc |
| 7.21% | `python` | `visit_decref` | gc |
| 1.66% | `python` | `_PyObject_Malloc` | memory |
| 1.29% | `python` | `subtype_traverse` | gc |
| 1.21% | `python` | `_PyObject_Free` | memory |
| 1.04% | `python` | `initialize_locals` | interpreter |
| 0.95% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 0.69% | `python` | `_PyEval_Vector` | interpreter |
| 0.69% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.66% | `python` | `_PyFrame_Traverse` | unknown |
| 0.61% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 0.60% | `python` | `_Py_dict_lookup` | lookup |
| 0.60% | `python` | `_PyType_Lookup` | lookup |
| 0.58% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.50% | `_heapq.cpython-312-x86_64-linux-gnu.so` | `siftup` | library |

## async_tree_memoization

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 25.84% | `python` | `gc_collect_main` | gc |
| 19.07% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 6.66% | `python` | `visit_reachable` | gc |
| 6.52% | `python` | `visit_decref` | gc |
| 2.00% | `python` | `_PyObject_Malloc` | memory |
| 1.58% | `python` | `_PyObject_Free` | memory |
| 1.17% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.11% | `python` | `subtype_traverse` | gc |
| 1.05% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.97% | `python` | `initialize_locals` | interpreter |
| 0.95% | `python` | `_Py_dict_lookup` | lookup |
| 0.89% | `python` | `_PyType_Lookup` | lookup |
| 0.88% | `python` | `_PyObject_GetMethod` | dynamic |
| 0.84% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 0.80% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.56% | `python` | `tupledealloc` | memory |
| 0.52% | `python` | `PyObject_GenericGetAttr` | dynamic |
| 0.51% | `python` | `context_tp_dealloc` | memory |

## asyncio_tcp

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 32.63% | `[kernel.kallsyms]` | `copy_user_enhanced_fast_string` | kernel |
| 16.73% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 9.28% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 8.16% | `[kernel.kallsyms]` | `clear_page_erms` | kernel |
| 0.86% | `python` | `_PyObject_Malloc` | memory |
| 0.55% | `[kernel.kallsyms]` | `tcp_sendmsg_locked` | kernel |

## chameleon

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 40.74% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 3.16% | `python` | `_PyObject_Malloc` | memory |
| 3.09% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 2.73% | `python` | `_PyObject_Free` | memory |
| 2.08% | `python` | `_Py_dict_lookup` | lookup |
| 2.04% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.93% | `python` | `sre_ucs2_charset.isra.0` | library |
| 1.66% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.65% | `python` | `_PyUnicode_JoinArray.part.0` | str |
| 1.44% | `python` | `gc_collect_main` | gc |
| 1.28% | `python` | `long_to_decimal_string_internal` | int |
| 1.22% | `python` | `PyUnicode_Format` | str |
| 1.12% | `python` | `_copy_characters.part.0.constprop.0` | str |
| 1.03% | `python` | `_sre_SRE_Pattern_search` | library |
| 0.91% | `python` | `list_append` | list |
| 0.89% | `python` | `insertdict` | dict |
| 0.81% | `python` | `resize_compact` | str |
| 0.80% | `python` | `dict_get` | dict |
| 0.76% | `python` | `visit_reachable` | gc |
| 0.65% | `python` | `PyObject_Vectorcall` | dynamic |
| 0.64% | `python` | `PyUnicode_New.part.0` | memory |
| 0.61% | `python` | `list_dealloc` | memory |
| 0.61% | `libc-2.31.so` | `malloc` | libc |
| 0.61% | `python` | `visit_decref` | gc |
| 0.57% | `python` | `method_vectorcall_FASTCALL` | unknown |
| 0.53% | `libc-2.31.so` | `pthread_attr_setschedparam` | libc |

## chaos

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 48.14% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 2.34% | `python` | `_PyLong_Subtract` | int |
| 1.98% | `python` | `_PyLong_Add` | int |
| 1.82% | `python` | `_PyObject_Free` | memory |
| 1.79% | `python` | `PyType_IsSubtype` | dynamic |
| 1.58% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.27% | `python` | `tupledealloc` | memory |
| 1.13% | `python` | `PyFloat_FromDouble` | float |
| 1.04% | `python` | `initialize_locals` | interpreter |
| 1.02% | `python` | `_PyObject_Malloc (inlined)` | memory |
| 1.00% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 0.95% | `python` | `float_dealloc` | memory |
| 0.94% | `libm-2.31.so` | `f64xsubf128` | library |
| 0.92% | `python` | `compute_range_length` | unknown |
| 0.91% | `python` | `PyLong_AsDouble` | int |
| 0.88% | `python` | `subtype_dealloc` | memory |
| 0.88% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.85% | `python` | `gc_collect_main` | gc |
| 0.85% | `python` | `PyLong_FromLong` | int |
| 0.83% | `python` | `float_div` | float |
| 0.81% | `python` | `range_iter` | unknown |
| 0.79% | `python` | `_PyType_Lookup` | lookup |
| 0.75% | `python` | `float_richcompare` | float |
| 0.72% | `python` | `_Py_NewReference` | memory |
| 0.65% | `python` | `tuple_alloc` | memory |
| 0.62% | `python` | `float_pow` | float |
| 0.60% | `python` | `float_sub` | float |
| 0.55% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.53% | `python` | `PyObject_Vectorcall` | dynamic |
| 0.51% | `python` | `PyNumber_TrueDivide` | dynamic |

## comprehensions

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 32.34% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 4.48% | `python` | `_Py_dict_lookup` | lookup |
| 3.68% | `python` | `_PyObject_Malloc` | memory |
| 2.57% | `python` | `_PyObject_Free` | memory |
| 2.25% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 2.17% | `python` | `advance` | interpreter |
| 1.68% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.58% | `python` | `PyFunction_NewWithQualName` | memory |
| 1.35% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.21% | `python` | `dict_get` | dict |
| 1.10% | `python` | `list_dealloc` | memory |
| 1.10% | `python` | `PyObject_RichCompare` | dynamic |
| 1.05% | `python` | `gc_collect_main` | gc |
| 1.00% | `python` | `_PyObject_Realloc` | memory |
| 0.97% | `python` | `_PyObject_GC_New` | gc |
| 0.93% | `python` | `_PyType_Lookup` | lookup |
| 0.90% | `python` | `tupledealloc` | memory |
| 0.87% | `python` | `PyObject_GenericGetAttr` | dynamic |
| 0.87% | `python` | `PyObject_GC_Del` | gc |
| 0.80% | `python` | `insertdict` | dict |
| 0.72% | `python` | `PyDict_GetItemWithError` | dict |
| 0.71% | `python` | `PyObject_IsTrue` | dynamic |
| 0.67% | `python` | `frame_dealloc` | memory |
| 0.67% | `python` | `PyCode_Addr2Line` | unknown |
| 0.65% | `python` | `_PyObject_GC_NewVar` | gc |
| 0.65% | `python` | `func_clear` | unknown |
| 0.65% | `python` | `_PyTrash_end` | gc |
| 0.63% | `python` | `long_richcompare` | int |
| 0.60% | `python` | `func_dealloc` | memory |
| 0.60% | `python` | `PyObject_RichCompareBool` | dynamic |
| 0.59% | `python` | `tuple_alloc` | memory |
| 0.59% | `python` | `visit_decref` | gc |
| 0.57% | `python` | `_Py_NewReference` | memory |
| 0.56% | `python` | `long_hash` | int |
| 0.55% | `python` | `PyObject_GetAttr` | dynamic |
| 0.55% | `python` | `unsafe_tuple_compare` | unknown |
| 0.53% | `python` | `_PyTuple_FromArraySteal` | tuple |
| 0.52% | `python` | `_PyObject_GetInstanceAttribute` | dynamic |
| 0.52% | `python` | `PyObject_Hash` | dynamic |
| 0.52% | `python` | `_Py_Dealloc` | memory |
| 0.51% | `python` | `visit_reachable` | gc |
| 0.51% | `python` | `_PyObject_GC_Link` | gc |

## concurrent_imap

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 14.02% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 9.82% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 2.77% | `python` | `_PyObject_Free` | memory |
| 2.38% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 1.76% | `python` | `gc_collect_main` | gc |
| 1.64% | `python` | `tupledealloc` | memory |
| 1.49% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.32% | `python` | `_PyObject_Malloc` | memory |
| 1.31% | `python` | `initialize_locals` | interpreter |
| 1.21% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.14% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 1.08% | `python` | `_Py_dict_lookup` | lookup |
| 1.03% | `python` | `visit_decref` | gc |
| 0.94% | `python` | `_PyType_Lookup` | lookup |
| 0.84% | `python` | `_PyObject_Malloc (inlined)` | memory |
| 0.77% | `python` | `visit_reachable` | gc |
| 0.73% | `python` | `_PyCode_Quicken` | interpreter |
| 0.72% | `python` | `map_next` | unknown |
| 0.67% | `python` | `_PyTrash_end` | gc |
| 0.65% | `[kernel.kallsyms]` | `copy_page` | kernel |
| 0.64% | `python` | `tuple_alloc` | memory |
| 0.62% | `python` | `r_object` | unknown |
| 0.59% | `python` | `_PyObject_GetMethod` | dynamic |
| 0.57% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.57% | `[kernel.kallsyms]` | `native_irq_return_iret` | kernel |
| 0.53% | `python` | `_PyThreadState_PushFrame` | unknown |
| 0.52% | `python` | `PyObject_GenericGetAttr` | dynamic |
| 0.52% | `python` | `subtype_dealloc` | memory |

## coroutines

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 45.05% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 5.99% | `python` | `gen_dealloc` | memory |
| 3.67% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 3.29% | `python` | `_PyObject_GC_NewVar` | gc |
| 3.20% | `python` | `make_gen` | unknown |
| 3.19% | `python` | `_PyLong_Subtract` | int |
| 2.69% | `python` | `_PyLong_Add` | int |
| 2.67% | `python` | `_PyObject_Free` | memory |
| 2.12% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.85% | `python` | `_PyObject_Malloc (inlined)` | memory |
| 1.79% | `python` | `PyObject_CallFinalizerFromDealloc` | memory |
| 1.40% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 1.34% | `python` | `gc_collect_main` | gc |
| 1.23% | `python` | `PyObject_GC_Del` | gc |
| 1.10% | `python` | `_Py_MakeCoro` | unknown |
| 0.74% | `python` | `_PyObject_GC_Link` | gc |
| 0.67% | `python` | `_PyFrame_Copy` | unknown |
| 0.66% | `python` | `_PyCoro_GetAwaitableIter` | unknown |
| 0.65% | `python` | `_PyThreadState_PopFrame` | interpreter |
| 0.62% | `python` | `visit_decref` | gc |

## coverage

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 25.34% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 5.74% | `tracer.cpython-312-x86_64-linux-gnu.so` | `CTracer_trace` | library |
| 5.70% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 3.52% | `python` | `call_trace.part.0` | unknown |
| 3.46% | `python` | `_Py_dict_lookup` | lookup |
| 2.91% | `python` | `_PyObject_Malloc` | memory |
| 2.29% | `python` | `_PyObject_Free` | memory |
| 2.26% | `python` | `siphash13` | str |
| 1.95% | `python` | `_PyType_Lookup` | lookup |
| 1.68% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.57% | `python` | `gc_collect_main` | gc |
| 1.35% | `python` | `PyDict_GetItem` | dict |
| 1.34% | `python` | `PyLong_FromLong` | int |
| 1.25% | `python` | `initialize_locals` | interpreter |
| 1.24% | `python` | `set_add_entry` | set |
| 1.13% | `python` | `long_richcompare` | int |
| 1.00% | `python` | `PyObject_GenericGetAttr` | dynamic |
| 0.96% | `python` | `unicode_decode_utf8` | str |
| 0.93% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 0.90% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.88% | `python` | `_PyObject_GC_NewVar` | gc |
| 0.86% | `python` | `PyUnicode_New.part.0` | memory |
| 0.78% | `python` | `long_sub` | int |
| 0.77% | `python` | `ascii_decode` | str |
| 0.71% | `python` | `find_name_in_mro` | lookup |
| 0.64% | `python` | `PySet_Add` | unknown |
| 0.62% | `python` | `PyObject_RichCompare` | dynamic |
| 0.60% | `python` | `trace_function_exit` | unknown |
| 0.59% | `python` | `PyObject_GetAttr` | dynamic |
| 0.54% | `python` | `r_object` | unknown |
| 0.54% | `python` | `frame_dealloc` | memory |
| 0.54% | `python` | `visit_reachable` | gc |
| 0.51% | `python` | `_PyDict_LoadGlobal` | dict |

## crypto_pyaes

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 37.06% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 6.90% | `python` | `long_bitwise` | int |
| 4.79% | `python` | `_PyObject_Free` | memory |
| 3.87% | `python` | `long_rshift1` | int |
| 3.83% | `python` | `_PyObject_Malloc` | memory |
| 2.69% | `python` | `PyObject_GenericGetAttr` | dynamic |
| 2.58% | `python` | `l_mod` | int |
| 2.51% | `python` | `long_and` | int |
| 2.35% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 1.72% | `python` | `PyLong_FromLong` | int |
| 1.53% | `python` | `_PyLong_Add` | int |
| 1.52% | `python` | `long_rshift` | int |
| 1.36% | `python` | `PyObject_GetAttr` | dynamic |
| 1.32% | `python` | `_PyType_Lookup` | lookup |
| 1.17% | `python` | `PyNumber_And` | dynamic |
| 1.14% | `python` | `long_xor` | int |
| 1.10% | `python` | `_PyObject_GetInstanceAttribute` | dynamic |
| 1.04% | `python` | `_Py_NewReference` | memory |
| 0.93% | `python` | `PyNumber_Xor` | dynamic |
| 0.87% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 0.82% | `python` | `gc_collect_main` | gc |
| 0.68% | `python` | `long_mod` | int |
| 0.66% | `python` | `PyNumber_Remainder` | dynamic |
| 0.64% | `python` | `PyNumber_Rshift` | dynamic |
| 0.57% | `python` | `list_dealloc` | memory |
| 0.50% | `python` | `range_iter` | unknown |

## dask

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 34.25% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 3.85% | `python` | `gc_collect_main` | gc |
| 2.46% | `python` | `_PyObject_Malloc` | memory |
| 2.17% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 2.12% | `python` | `_PyObject_Free` | memory |
| 1.96% | `python` | `visit_decref` | gc |
| 1.72% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.65% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.46% | `python` | `visit_reachable` | gc |
| 1.23% | `python` | `_Py_dict_lookup` | lookup |
| 1.20% | `python` | `tupledealloc` | memory |
| 0.99% | `python` | `initialize_locals` | interpreter |
| 0.76% | `python` | `_PyType_Lookup` | lookup |
| 0.58% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.52% | `python` | `_Py_NewReference` | memory |

## deepcopy

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 46.42% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 5.92% | `python` | `_Py_dict_lookup` | lookup |
| 3.04% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 2.89% | `python` | `_PyObject_Free` | memory |
| 2.37% | `python` | `_PyObject_Malloc` | memory |
| 2.03% | `python` | `dict_get` | dict |
| 1.50% | `python` | `PyLong_FromVoidPtr` | int |
| 1.23% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.99% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 0.98% | `python` | `sys_audit_tstate` | unknown |
| 0.94% | `python` | `initialize_locals` | interpreter |
| 0.92% | `python` | `list_append` | list |
| 0.86% | `python` | `long_hash` | int |
| 0.84% | `python` | `PySys_Audit` | unknown |
| 0.77% | `python` | `gc_collect_main` | gc |
| 0.69% | `python` | `insertdict` | dict |
| 0.67% | `python` | `PyObject_Hash` | dynamic |
| 0.65% | `python` | `_PyObject_Realloc` | memory |
| 0.63% | `python` | `long_richcompare` | int |
| 0.63% | `python` | `advance` | interpreter |
| 0.62% | `python` | `tupledealloc` | memory |
| 0.62% | `python` | `_PyType_Lookup` | lookup |
| 0.58% | `python` | `insert_to_emptydict` | dict |
| 0.56% | `python` | `_PyObject_GC_New` | gc |
| 0.56% | `python` | `list_dealloc` | memory |
| 0.52% | `python` | `_PyThreadState_PopFrame` | interpreter |

## deltablue

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 60.24% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 3.06% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 2.22% | `python` | `gc_collect_main` | gc |
| 1.93% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 1.77% | `python` | `_PyObject_Malloc` | memory |
| 1.68% | `python` | `_PyObject_GetMethod` | dynamic |
| 1.63% | `python` | `_PyObject_Free` | memory |
| 1.44% | `python` | `_PyType_Lookup` | lookup |
| 1.08% | `python` | `visit_decref` | gc |
| 1.06% | `python` | `_PyThreadState_PopFrame` | interpreter |
| 0.82% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 0.63% | `python` | `_PyObject_VisitManagedDict` | gc |

## django_template

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 33.98% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 3.33% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 2.82% | `python` | `_PyObject_Malloc (inlined)` | memory |
| 2.48% | `python` | `_PyObject_Free` | memory |
| 2.01% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.96% | `python` | `gc_collect_main` | gc |
| 1.68% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.52% | `python` | `_Py_dict_lookup` | lookup |
| 1.32% | `python` | `_PyType_Lookup` | lookup |
| 1.27% | `python` | `_PyObject_GenericGetAttrWithDict` | dynamic |
| 1.12% | `python` | `initialize_locals` | interpreter |
| 0.99% | `python` | `visit_decref` | gc |
| 0.91% | `python` | `tupledealloc` | memory |
| 0.76% | `python` | `replace` | str |
| 0.72% | `python` | `insertdict` | dict |
| 0.71% | `python` | `visit_reachable` | gc |
| 0.65% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.64% | `python` | `_PyObject_GC_New` | gc |
| 0.62% | `python` | `PyObject_GC_Del` | gc |
| 0.61% | `python` | `_Py_NewReference` | memory |
| 0.60% | `python` | `PyType_IsSubtype` | dynamic |
| 0.60% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.53% | `python` | `r_object` | unknown |
| 0.50% | `python` | `tuple_alloc` | memory |

## djangocms

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 17.57% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 5.74% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 4.91% | `python` | `gc_collect_main` | gc |
| 2.47% | `python` | `_PyObject_Malloc` | memory |
| 2.40% | `python` | `_Py_dict_lookup` | lookup |
| 2.05% | `python` | `visit_decref` | gc |
| 1.95% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.69% | `python` | `_PyType_Lookup` | lookup |
| 1.58% | `python` | `_PyObject_Free` | memory |
| 1.56% | `python` | `visit_reachable` | gc |
| 0.98% | `libc-2.31.so` | `pthread_attr_setschedparam` | libc |
| 0.91% | `python` | `PyObject_GenericGetAttr` | dynamic |
| 0.87% | `python` | `dict_traverse` | gc |
| 0.80% | `libsqlite3.so.0.8.6` | `sqlite3_exec` | library |
| 0.78% | `python` | `tupledealloc` | memory |
| 0.74% | `libz.so.1.2.11` | `inflateBackEnd` | library |
| 0.73% | `python` | `initialize_locals` | interpreter |
| 0.72% | `python` | `find_name_in_mro` | lookup |
| 0.72% | `python` | `_PyDict_GetItem_KnownHash` | dict |
| 0.66% | `python` | `advance` | interpreter |
| 0.62% | `python` | `update_one_slot` | unknown |
| 0.62% | `python` | `_PyPegen_is_memoized` | unknown |
| 0.55% | `python` | `insertdict` | dict |
| 0.52% | `python` | `_PyFrame_ClearExceptCode` | interpreter |

## docutils

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 25.23% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 7.00% | `python` | `sre_ucs1_match` | library |
| 6.46% | `python` | `gc_collect_main` | gc |
| 3.23% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 2.68% | `python` | `_PyObject_Malloc` | memory |
| 2.37% | `python` | `_PyObject_Free` | memory |
| 2.30% | `python` | `visit_decref` | gc |
| 2.26% | `python` | `_PyType_Lookup` | lookup |
| 2.04% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.69% | `python` | `sre_ucs2_charset.isra.0` | library |
| 1.48% | `python` | `visit_reachable` | gc |
| 1.46% | `python` | `PyObject_GenericGetAttr` | dynamic |
| 1.44% | `python` | `_Py_dict_lookup` | lookup |
| 1.30% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.00% | `python` | `advance` | interpreter |
| 0.83% | `python` | `list_dealloc` | memory |
| 0.80% | `python` | `PyObject_GetAttr` | dynamic |
| 0.78% | `python` | `_PyObject_GetInstanceAttribute` | dynamic |
| 0.76% | `python` | `dict_traverse` | gc |
| 0.74% | `python` | `tupledealloc` | memory |
| 0.70% | `python` | `_PyObject_GetMethod` | dynamic |
| 0.64% | `python` | `initialize_locals` | interpreter |
| 0.62% | `python` | `PyType_IsSubtype` | dynamic |
| 0.61% | `python` | `list_traverse` | gc |
| 0.61% | `libc-2.31.so` | `pthread_attr_setschedparam` | libc |
| 0.51% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.50% | `python` | `PyUnicode_Format` | str |

## dulwich_log

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 28.50% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 2.91% | `libz.so.1.2.11` | `inflateCodesUsed` | library |
| 2.76% | `python` | `_PyObject_Malloc` | memory |
| 2.43% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 2.20% | `python` | `_PyObject_Free` | memory |
| 1.80% | `libz.so.1.2.11` | `inflateBackEnd` | library |
| 1.57% | `libz.so.1.2.11` | `inflate` | library |
| 1.31% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 1.18% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.15% | `python` | `gc_collect_main` | gc |
| 0.93% | `python` | `tupledealloc` | memory |
| 0.82% | `python` | `visit_decref` | gc |
| 0.75% | `python` | `_PyType_Lookup` | lookup |
| 0.72% | `libc-2.31.so` | `pthread_attr_setschedparam` | libc |
| 0.69% | `[kernel.kallsyms]` | `__d_lookup_rcu` | kernel |
| 0.66% | `[kernel.kallsyms]` | `copy_user_enhanced_fast_string` | kernel |
| 0.63% | `python` | `advance` | interpreter |
| 0.62% | `python` | `initialize_locals` | interpreter |
| 0.60% | `python` | `_Py_dict_lookup` | lookup |
| 0.58% | `python` | `_Py_NewReference` | memory |
| 0.57% | `python` | `subtype_dealloc` | memory |
| 0.57% | `python` | `tuple_alloc` | memory |
| 0.55% | `python` | `vgetargs1_impl` | unknown |
| 0.54% | `python` | `PyObject_GC_UnTrack` | gc |

## fannkuch

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 37.68% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 8.34% | `python` | `PySlice_AdjustIndices` | slice |
| 5.61% | `python` | `list_subscript` | list |
| 5.19% | `python` | `list_ass_slice` | list |
| 4.58% | `python` | `_PyLong_Add` | int |
| 3.63% | `python` | `list_dealloc` | memory |
| 3.12% | `python` | `slice_dealloc` | memory |
| 2.45% | `python` | `PyNumber_AsSsize_t` | dynamic |
| 2.30% | `python` | `_PyEval_SliceIndex` | slice |
| 2.07% | `python` | `PySlice_Unpack` | slice |
| 1.60% | `python` | `PySlice_New` | memory |
| 1.58% | `python` | `list_ass_subscript` | list |
| 1.57% | `python` | `_PyBuildSlice_ConsumeRefs` | slice |
| 1.56% | `python` | `_PyObject_Free` | memory |
| 1.38% | `python` | `_PyObject_Malloc` | memory |
| 1.34% | `python` | `_Py_NewReference` | memory |
| 1.28% | `python` | `PyLong_AsSsize_t` | int |
| 1.11% | `python` | `list_insert` | list |
| 1.09% | `python` | `PyObject_IsTrue` | dynamic |
| 0.89% | `python` | `PyObject_GetItem` | dynamic |
| 0.88% | `python` | `_PyLong_Subtract` | int |
| 0.81% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 0.70% | `python` | `_PyTrash_end` | gc |
| 0.69% | `python` | `_PyTrash_begin` | gc |
| 0.61% | `python` | `PyObject_SetItem` | dynamic |
| 0.60% | `python` | `list_pop` | list |

## float

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 37.46% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 4.41% | `libm-2.31.so` | `f64xsubf128` | library |
| 3.86% | `python` | `gc_collect_main` | gc |
| 3.03% | `python` | `subtype_traverse` | gc |
| 2.88% | `python` | `visit_decref` | gc |
| 2.52% | `python` | `visit_reachable` | gc |
| 2.06% | `python` | `_PyObject_Free` | memory |
| 2.04% | `python` | `_PyObject_Malloc (inlined)` | memory |
| 2.03% | `python` | `PyFloat_FromDouble` | float |
| 1.98% | `python` | `float_div` | float |
| 1.82% | `python` | `subtype_dealloc` | memory |
| 1.62% | `python` | `float_dealloc` | memory |
| 1.25% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.00% | `python` | `PyType_IsSubtype` | dynamic |
| 1.00% | `python` | `_Py_NewReference` | memory |
| 0.95% | `python` | `initialize_locals` | interpreter |
| 0.94% | `python` | `tupledealloc` | memory |
| 0.93% | `python` | `PyNumber_InPlaceTrueDivide` | dynamic |
| 0.86% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.75% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 0.68% | `python` | `long_float` | int |
| 0.63% | `python` | `_PyObject_MakeTpCall` | dynamic |
| 0.62% | `python` | `PyType_GenericAlloc` | memory |
| 0.53% | `python` | `_PyType_Lookup` | lookup |
| 0.51% | `python` | `_PyObject_Call_Prepend` | dynamic |

## gc_collect

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 31.60% | `python` | `gc_collect_main` | gc |
| 14.78% | `python` | `visit_reachable` | gc |
| 14.17% | `python` | `visit_decref` | gc |
| 6.51% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 5.19% | `python` | `dict_traverse` | gc |
| 1.91% | `python` | `PyObject_IS_GC` | gc |
| 1.90% | `python` | `_PyDict_MaybeUntrack` | gc |
| 1.80% | `python` | `subtype_traverse` | gc |
| 1.74% | `python` | `func_traverse` | gc |
| 1.62% | `python` | `set_traverse` | gc |
| 1.47% | `python` | `_PyObject_VisitManagedDict` | gc |
| 1.32% | `python` | `type_is_gc` | gc |
| 0.90% | `python` | `_PyObject_Malloc` | memory |
| 0.84% | `python` | `type_traverse` | gc |
| 0.73% | `python` | `tupletraverse` | tuple |
| 0.54% | `python` | `list_traverse` | gc |
| 0.54% | `python` | `initialize_locals` | interpreter |
| 0.52% | `python` | `_PyObject_Free` | memory |

## gc_traversal

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 29.16% | `python` | `visit_reachable` | gc |
| 21.25% | `python` | `visit_decref` | gc |
| 15.38% | `python` | `list_traverse` | gc |
| 12.97% | `python` | `gc_collect_main` | gc |
| 3.73% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 2.24% | `python` | `dict_traverse` | gc |
| 0.94% | `python` | `PyObject_IS_GC` | gc |
| 0.79% | `python` | `_PyDict_MaybeUntrack` | gc |
| 0.78% | `python` | `func_traverse` | gc |
| 0.70% | `python` | `set_traverse` | gc |
| 0.62% | `python` | `unicodekeys_lookup_unicode` | lookup |

## generators

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 49.58% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 4.44% | `python` | `gc_collect_main` | gc |
| 2.35% | `python` | `_PyObject_Malloc` | memory |
| 1.94% | `python` | `_PyObject_Free` | memory |
| 1.51% | `python` | `visit_reachable` | gc |
| 1.45% | `python` | `initialize_locals` | interpreter |
| 1.44% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.42% | `python` | `gen_dealloc` | memory |
| 1.38% | `python` | `visit_decref` | gc |
| 1.24% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.18% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.97% | `python` | `long_add` | int |
| 0.91% | `python` | `_PyObject_VisitManagedDict` | gc |
| 0.86% | `python` | `PyObject_IsTrue` | dynamic |
| 0.82% | `python` | `_PyType_Lookup` | lookup |
| 0.81% | `python` | `subtype_traverse` | gc |
| 0.81% | `python` | `make_gen` | unknown |
| 0.81% | `python` | `compute_range_length` | unknown |
| 0.80% | `python` | `range_subscript` | unknown |
| 0.72% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.70% | `python` | `_PyObject_GC_NewVar` | gc |
| 0.62% | `python` | `_PySlice_GetLongIndices` | slice |
| 0.55% | `python` | `PyObject_RichCompare` | dynamic |
| 0.55% | `python` | `long_richcompare` | int |
| 0.52% | `python` | `tupledealloc` | memory |
| 0.51% | `python` | `PyObject_RichCompareBool` | dynamic |
| 0.50% | `python` | `long_mul` | int |

## genshi

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 46.09% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 2.96% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 2.49% | `python` | `_PyObject_Free` | memory |
| 2.40% | `python` | `_PyObject_Malloc` | memory |
| 2.35% | `python` | `_Py_dict_lookup` | lookup |
| 1.43% | `python` | `insertdict` | dict |
| 1.36% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.30% | `python` | `_PyType_Lookup` | lookup |
| 1.23% | `python` | `insert_to_emptydict` | dict |
| 1.13% | `python` | `tupledealloc` | memory |
| 1.05% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.00% | `python` | `PyObject_IsTrue` | dynamic |
| 0.87% | `python` | `gc_collect_main` | gc |
| 0.80% | `python` | `_PyTuple_FromArraySteal` | tuple |
| 0.75% | `python` | `_PyDict_FromItems` | dict |
| 0.65% | `python` | `_Py_type_getattro` | lookup |
| 0.62% | `python` | `_PyObject_GC_New` | gc |
| 0.61% | `python` | `free_keys_object` | dict |
| 0.61% | `python` | `tuple_alloc` | memory |
| 0.59% | `python` | `_PyTrash_end` | gc |
| 0.58% | `python` | `_PyObject_GetMethod` | dynamic |
| 0.55% | `python` | `PyObject_GC_Del` | gc |
| 0.54% | `python` | `dict_dealloc` | memory |
| 0.51% | `python` | `long_to_decimal_string_internal` | int |
| 0.51% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.50% | `libc-2.31.so` | `pthread_attr_setschedparam` | libc |

## go

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 65.16% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 2.17% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 2.00% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 1.54% | `python` | `_PyObject_GetMethod` | dynamic |
| 1.25% | `python` | `_PyObject_Free` | memory |
| 1.07% | `python` | `_Py_dict_lookup` | lookup |
| 1.05% | `python` | `_PyType_Lookup` | lookup |
| 1.04% | `python` | `_PyObject_Malloc (inlined)` | memory |
| 0.90% | `python` | `gc_collect_main` | gc |
| 0.88% | `python` | `long_bitwise` | int |
| 0.85% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 0.78% | `python` | `_PyLong_Add` | int |
| 0.61% | `python` | `initialize_locals` | interpreter |
| 0.61% | `python` | `_PyThreadState_PopFrame` | interpreter |
| 0.56% | `python` | `_PyLong_Subtract` | int |
| 0.53% | `python` | `PyDict_GetItemWithError` | dict |

## gunicorn

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 27.12% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 2.84% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 2.22% | `python` | `_PyObject_Malloc` | memory |
| 2.20% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.92% | `python` | `_PyObject_Free` | memory |
| 1.65% | `python` | `gc_collect_main` | gc |
| 1.53% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.37% | `python` | `initialize_locals` | interpreter |
| 1.23% | `python` | `_Py_dict_lookup` | lookup |
| 1.20% | `python` | `tupledealloc` | memory |
| 0.98% | `python` | `_PyType_Lookup` | lookup |
| 0.92% | `python` | `advance` | interpreter |
| 0.75% | `python` | `visit_decref` | gc |
| 0.68% | `libc-2.31.so` | `pthread_attr_setschedparam` | libc |
| 0.57% | `python` | `PyObject_GenericGetAttr` | dynamic |
| 0.55% | `python` | `PyObject_IsTrue` | dynamic |
| 0.55% | `python` | `tuple_alloc` | memory |
| 0.52% | `python` | `sre_ucs1_match` | library |

## hexiom

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 56.30% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 2.38% | `python` | `long_richcompare` | int |
| 2.34% | `python` | `list_contains` | list |
| 2.32% | `python` | `PyObject_RichCompare` | dynamic |
| 2.17% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.56% | `python` | `PyObject_RichCompareBool` | dynamic |
| 1.54% | `python` | `_PyObject_Free` | memory |
| 1.36% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 1.33% | `python` | `PyLong_FromSsize_t` | int |
| 1.23% | `python` | `gen_iternext` | unknown |
| 1.23% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.22% | `python` | `_PyObject_Malloc` | memory |
| 1.11% | `python` | `gc_collect_main` | gc |
| 0.65% | `python` | `PyLong_FromLong` | int |
| 0.61% | `python` | `visit_decref` | gc |
| 0.57% | `python` | `_PyThreadState_PopFrame` | interpreter |
| 0.55% | `python` | `builtin_sum` | unknown |
| 0.53% | `python` | `tupledealloc` | memory |
| 0.52% | `python` | `_Py_dict_lookup` | lookup |
| 0.51% | `python` | `list_dealloc` | memory |

## html5lib

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 36.39% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 6.32% | `python` | `sre_ucs2_charset.isra.0` | library |
| 3.48% | `python` | `gc_collect_main` | gc |
| 2.34% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 1.98% | `python` | `_PyObject_Malloc` | memory |
| 1.77% | `python` | `_Py_dict_lookup` | lookup |
| 1.76% | `python` | `_PyObject_Free` | memory |
| 1.46% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.19% | `python` | `visit_decref` | gc |
| 1.12% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 0.89% | `python` | `visit_reachable` | gc |
| 0.78% | `python` | `sre_ucs1_count` | library |
| 0.74% | `python` | `initialize_locals` | interpreter |
| 0.69% | `python` | `PyObject_RichCompare` | dynamic |
| 0.63% | `python` | `PyObject_IsTrue` | dynamic |
| 0.62% | `python` | `PyObject_GenericGetAttr` | dynamic |
| 0.61% | `python` | `insertdict` | dict |
| 0.57% | `libc-2.31.so` | `pthread_attr_setschedparam` | libc |
| 0.52% | `python` | `PyObject_GetAttr` | dynamic |
| 0.51% | `python` | `tupledealloc` | memory |

## json

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 12.00% | `_json.cpython-312-x86_64-linux-gnu.so` | `scanstring_unicode` | library |
| 7.81% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 6.49% | `_json.cpython-312-x86_64-linux-gnu.so` | `scan_once_unicode` | library |
| 6.01% | `python` | `siphash13` | str |
| 5.14% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 5.06% | `python` | `_PyObject_Malloc` | memory |
| 3.73% | `python` | `PyDict_SetDefault` | dict |
| 3.63% | `python` | `_PyObject_Free` | memory |
| 3.03% | `python` | `PyLong_FromString` | int |
| 2.64% | `python` | `insertdict` | dict |
| 2.45% | `python` | `_Py_dict_lookup` | lookup |
| 2.43% | `libc-2.31.so` | `pthread_attr_setschedparam` | libc |
| 2.32% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 2.04% | `python` | `_PyUnicode_FromASCII (inlined)` | str |
| 1.84% | `python` | `free_keys_object` | dict |
| 1.61% | `python` | `find_empty_slot` | dict |
| 1.57% | `python` | `build_indices_unicode` | dict |
| 1.47% | `python` | `PyUnicode_Substring` | str |
| 0.91% | `python` | `PyObject_IS_GC` | gc |
| 0.80% | `python` | `insert_to_emptydict` | dict |
| 0.80% | `python` | `PyDict_SetItem` | dict |
| 0.79% | `python` | `gc_collect_main` | gc |
| 0.73% | `python` | `_sre_SRE_Pattern_match` | library |
| 0.65% | `python` | `tupledealloc` | memory |
| 0.64% | `python` | `_Py_NewReference` | memory |
| 0.61% | `python` | `dictresize` | unknown |
| 0.57% | `python` | `initialize_locals` | interpreter |
| 0.56% | `python` | `unicode_dealloc` | memory |
| 0.55% | `python` | `sre_ucs1_match` | library |
| 0.52% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 0.50% | `python` | `sre_ucs1_count` | library |
| 0.50% | `libc-2.31.so` | `malloc` | libc |

## json_dumps

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 13.07% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 8.34% | `_json.cpython-312-x86_64-linux-gnu.so` | `py_encode_basestring_ascii` | library |
| 4.86% | `python` | `_PyObject_Malloc` | memory |
| 4.67% | `python` | `_PyObject_Free` | memory |
| 4.36% | `python` | `_copy_characters.part.0.constprop.0` | str |
| 3.79% | `python` | `_PyUnicodeWriter_WriteStr` | str |
| 3.25% | `_json.cpython-312-x86_64-linux-gnu.so` | `encoder_listencode_obj` | library |
| 2.89% | `python` | `_Py_dict_lookup` | lookup |
| 2.86% | `python` | `resize_compact` | str |
| 2.86% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 2.57% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 2.52% | `python` | `PyUnicode_New` | memory |
| 2.47% | `_json.cpython-312-x86_64-linux-gnu.so` | `encoder_encode_key_value` | library |
| 1.65% | `python` | `PyDict_Next` | dict |
| 1.62% | `python` | `convertitem` | unknown |
| 1.56% | `python` | `vgetargskeywords` | unknown |
| 1.55% | `python` | `_PyObject_Realloc` | memory |
| 1.28% | `python` | `tupledealloc` | memory |
| 1.11% | `python` | `_PyUnicodeWriter_PrepareInternal` | str |
| 1.07% | `python` | `initialize_locals` | interpreter |
| 0.93% | `python` | `PyDict_GetItemWithError` | dict |
| 0.88% | `python` | `_PyType_Lookup` | lookup |
| 0.87% | `python` | `gc_collect_main` | gc |
| 0.86% | `python` | `unicode_dealloc` | memory |
| 0.82% | `python` | `long_to_decimal_string_internal` | int |
| 0.72% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 0.71% | `python` | `_Py_NewReference` | memory |
| 0.63% | `python` | `long_hash` | int |
| 0.61% | `python` | `PyType_IsSubtype` | dynamic |
| 0.58% | `python` | `PyObject_GenericGetAttr` | dynamic |
| 0.56% | `python` | `tuple_alloc` | memory |
| 0.53% | `python` | `insertdict` | dict |
| 0.52% | `python` | `_Py_Dealloc` | memory |

## json_loads

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 13.10% | `_json.cpython-312-x86_64-linux-gnu.so` | `scanstring_unicode` | library |
| 7.15% | `_json.cpython-312-x86_64-linux-gnu.so` | `scan_once_unicode` | library |
| 6.98% | `python` | `siphash13` | str |
| 6.74% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 5.60% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 4.95% | `python` | `_PyObject_Malloc` | memory |
| 3.58% | `python` | `_PyObject_Free` | memory |
| 3.40% | `python` | `_Py_dict_lookup` | lookup |
| 3.20% | `python` | `insertdict` | dict |
| 3.11% | `python` | `PyLong_FromString` | int |
| 3.06% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 3.04% | `python` | `_PyUnicode_FromASCII` | str |
| 2.81% | `python` | `PyDict_SetDefault` | dict |
| 2.30% | `python` | `PyUnicode_Substring` | str |
| 1.30% | `python` | `free_keys_object` | dict |
| 1.30% | `python` | `find_empty_slot` | dict |
| 1.05% | `libc-2.31.so` | `pthread_attr_setschedparam` | libc |
| 1.03% | `python` | `PyDict_SetItem` | dict |
| 1.02% | `python` | `build_indices_unicode` | dict |
| 0.92% | `python` | `PyObject_IS_GC` | gc |
| 0.91% | `python` | `unicode_dealloc` | memory |
| 0.81% | `python` | `gc_collect_main` | gc |
| 0.60% | `python` | `_Py_NewReference` | memory |

## logging

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 46.86% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 3.54% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 2.00% | `python` | `_Py_dict_lookup` | lookup |
| 1.93% | `python` | `initialize_locals` | interpreter |
| 1.78% | `python` | `dict_dealloc` | memory |
| 1.78% | `python` | `advance` | interpreter |
| 1.71% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.62% | `python` | `_PyObject_Malloc (inlined)` | memory |
| 1.56% | `python` | `_PyObject_Free` | memory |
| 1.30% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 1.18% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 1.17% | `python` | `PyObject_GenericGetAttr` | dynamic |
| 0.97% | `python` | `_PyType_Lookup` | lookup |
| 0.89% | `python` | `_Py_NewReference` | memory |
| 0.75% | `python` | `PyDict_New` | memory |
| 0.73% | `python` | `PyObject_GetAttr` | dynamic |
| 0.69% | `python` | `PyObject_IsTrue` | dynamic |
| 0.67% | `python` | `_PyThreadState_PopFrame` | interpreter |
| 0.66% | `python` | `_PyTrash_end` | gc |
| 0.65% | `python` | `PyDict_GetItemWithError` | dict |
| 0.65% | `python` | `PyUnicode_Contains` | str |
| 0.54% | `python` | `tupledealloc` | memory |
| 0.53% | `python` | `_PyTrash_begin` | gc |
| 0.52% | `python` | `vgetargs1_impl` | unknown |

## mako

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 37.34% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 8.02% | `python` | `replace` | str |
| 5.03% | `python` | `long_to_decimal_string_internal` | int |
| 3.93% | `python` | `_PyUnicode_JoinArray.part.0` | str |
| 3.28% | `python` | `_PyObject_Free` | memory |
| 2.82% | `python` | `deque_append` | unknown |
| 2.48% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.89% | `python` | `_PyObject_Malloc` | memory |
| 1.88% | `python` | `unicode_replace` | str |
| 1.83% | `python` | `dequeiter_next` | unknown |
| 1.41% | `python` | `list_extend` | list |
| 1.16% | `python` | `PyUnicode_New` | memory |
| 1.15% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.06% | `python` | `gc_collect_main` | gc |
| 1.00% | `python` | `sre_ucs2_charset.isra.0` | library |
| 0.99% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.96% | `python` | `list_dealloc` | memory |
| 0.92% | `python` | `PyObject_Str` | dynamic |
| 0.92% | `python` | `PyErr_CheckSignals` | unknown |
| 0.85% | `libc-2.31.so` | `pthread_attr_setschedparam` | libc |
| 0.73% | `python` | `deque_clear.part.0` | unknown |
| 0.71% | `python` | `PyLong_FromLong` | int |
| 0.52% | `python` | `PyThread_get_thread_ident` | unknown |
| 0.50% | `[kernel.kallsyms]` | `native_irq_return_iret` | kernel |

## mdp

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 28.11% | `python` | `tuplehash` | tuple |
| 15.59% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 13.94% | `python` | `PyObject_Hash` | dynamic |
| 11.14% | `python` | `long_hash` | int |
| 5.99% | `python` | `_Py_dict_lookup` | lookup |
| 2.04% | `python` | `tuplerichcompare` | tuple |
| 1.41% | `python` | `PyObject_RichCompareBool` | dynamic |
| 1.33% | `python` | `PyObject_RichCompare` | dynamic |
| 1.16% | `python` | `_PyObject_Free` | memory |
| 1.15% | `python` | `dict_subscript` | dict |
| 1.05% | `python` | `_PyObject_Malloc` | memory |
| 0.88% | `python` | `_PyLong_GCD` | int |
| 0.65% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 0.58% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.57% | `python` | `_PyFrame_ClearExceptCode` | interpreter |

## meteor_contest

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 21.41% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 8.21% | `python` | `set_issubset` | set |
| 7.68% | `python` | `set_lookkey` | set |
| 5.81% | `python` | `setiter_iternext` | set |
| 3.49% | `python` | `set_difference` | set |
| 3.26% | `python` | `set_dealloc` | memory |
| 2.37% | `python` | `PyObject_RichCompare` | dynamic |
| 2.07% | `python` | `_PyObject_Free` | memory |
| 1.92% | `python` | `set_add_entry` | set |
| 1.90% | `python` | `list_dealloc` | memory |
| 1.81% | `python` | `_PyObject_Malloc` | memory |
| 1.52% | `python` | `long_richcompare` | int |
| 1.44% | `python` | `min_max` | unknown |
| 1.43% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.37% | `python` | `list_slice.isra.0` | list |
| 1.34% | `python` | `gc_collect_main` | gc |
| 1.12% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 1.04% | `python` | `PyIter_Next` | unknown |
| 0.96% | `python` | `PyObject_RichCompareBool` | dynamic |
| 0.93% | `python` | `set_table_resize` | set |
| 0.92% | `python` | `set_intersection` | set |
| 0.74% | `python` | `set_update_internal` | set |
| 0.71% | `python` | `PyType_GenericAlloc` | memory |
| 0.71% | `python` | `visit_decref` | gc |
| 0.68% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 0.67% | `python` | `set_richcompare` | set |
| 0.65% | `python` | `PyObject_GC_Del` | gc |
| 0.55% | `python` | `visit_reachable` | gc |

## mypy2

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 29.20% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 13.85% | `python` | `gc_collect_main` | gc |
| 2.73% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 2.67% | `python` | `_PyObject_Malloc` | memory |
| 2.51% | `python` | `visit_decref` | gc |
| 1.98% | `python` | `_PyObject_Free` | memory |
| 1.92% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.57% | `python` | `_Py_dict_lookup` | lookup |
| 1.56% | `python` | `initialize_locals` | interpreter |
| 1.39% | `python` | `_PyType_Lookup` | lookup |
| 1.33% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.30% | `python` | `subtype_traverse` | gc |
| 1.20% | `python` | `subtype_dealloc` | memory |
| 1.13% | `python` | `visit_reachable` | gc |
| 0.87% | `python` | `siphash13` | str |
| 0.80% | `_json.cpython-312-x86_64-linux-gnu.so` | `scan_once_unicode` | library |
| 0.76% | `_json.cpython-312-x86_64-linux-gnu.so` | `scanstring_unicode` | library |
| 0.75% | `python` | `PyType_IsSubtype` | dynamic |
| 0.73% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.64% | `python` | `list_dealloc` | memory |
| 0.60% | `python` | `PyDict_GetItemWithError` | dict |
| 0.58% | `python` | `tupledealloc` | memory |
| 0.56% | `python` | `_PyObject_GetMethod` | dynamic |
| 0.50% | `python` | `_PyObject_GC_New` | gc |
| 0.50% | `python` | `insertdict` | dict |

## nbody

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 68.08% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 6.42% | `python` | `PyFloat_FromDouble` | float |
| 4.31% | `libm-2.31.so` | `f64xsubf128` | library |
| 2.40% | `python` | `float_dealloc` | memory |
| 2.26% | `python` | `_Py_NewReference` | memory |
| 1.30% | `python` | `float_pow` | float |
| 0.83% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.81% | `python` | `gc_collect_main` | gc |

## nqueens

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 37.32% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 4.69% | `python` | `_PyObject_Malloc (inlined)` | memory |
| 3.50% | `python` | `_PyObject_Free` | memory |
| 2.13% | `python` | `gen_iternext` | unknown |
| 2.11% | `python` | `set_add_entry` | set |
| 1.92% | `python` | `PySlice_AdjustIndices` | slice |
| 1.70% | `python` | `_PyLong_Add` | int |
| 1.62% | `python` | `list_dealloc` | memory |
| 1.49% | `python` | `tupledealloc` | memory |
| 1.34% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.33% | `python` | `set_dealloc` | memory |
| 1.31% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 1.11% | `python` | `PyLong_FromLong` | int |
| 0.99% | `python` | `_Py_NewReference` | memory |
| 0.98% | `python` | `PyFunction_NewWithQualName` | memory |
| 0.97% | `python` | `_PyBuildSlice_ConsumeRefs` | slice |
| 0.89% | `python` | `PyNumber_AsSsize_t` | dynamic |
| 0.85% | `python` | `gc_collect_main` | gc |
| 0.84% | `python` | `slice_dealloc` | memory |
| 0.82% | `python` | `set_table_resize` | set |
| 0.81% | `python` | `set_update_internal` | set |
| 0.81% | `python` | `_PyTrash_end` | gc |
| 0.79% | `python` | `_Py_dict_lookup` | lookup |
| 0.73% | `python` | `list_subscript` | list |
| 0.73% | `python` | `_PyLong_Subtract` | int |
| 0.72% | `python` | `_PyObject_LookupSpecial` | dynamic |
| 0.71% | `python` | `list_ass_slice` | list |
| 0.68% | `python` | `PyList_New.constprop.0` | memory |
| 0.64% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.61% | `python` | `_PyObject_GC_New` | gc |
| 0.56% | `python` | `_PyTrash_begin` | gc |
| 0.54% | `python` | `PySlice_Unpack` | slice |
| 0.54% | `python` | `list_slice.isra.0` | list |
| 0.52% | `python` | `PySequence_Tuple` | dynamic |
| 0.52% | `python` | `PyObject_GC_Del` | gc |
| 0.51% | `python` | `func_clear` | unknown |
| 0.50% | `python` | `range_iter` | unknown |
| 0.50% | `python` | `_PyObject_GC_Link` | gc |

## pathlib

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 18.07% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 3.76% | `python` | `_PyObject_Malloc` | memory |
| 3.35% | `python` | `_PyObject_Free` | memory |
| 1.65% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.58% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 1.50% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.46% | `[kernel.kallsyms]` | `__d_lookup_rcu` | kernel |
| 1.21% | `python` | `initialize_locals` | interpreter |
| 1.20% | `libpthread-2.31.so` | `__pthread_mutex_lock` | library |
| 1.14% | `[kernel.kallsyms]` | `__ext4fs_dirhash` | kernel |
| 1.13% | `[kernel.kallsyms]` | `memset_erms` | kernel |
| 1.08% | `python` | `gc_collect_main` | gc |
| 0.97% | `[kernel.kallsyms]` | `ext4_htree_store_dirent` | kernel |
| 0.97% | `python` | `_PyType_Lookup` | lookup |
| 0.97% | `libpthread-2.31.so` | `pthread_mutex_unlock` | library |
| 0.81% | `python` | `_Py_dict_lookup` | lookup |
| 0.80% | `python` | `tupledealloc` | memory |
| 0.80% | `python` | `_Py_NewReference` | memory |
| 0.79% | `python` | `PyDict_GetItemWithError` | dict |
| 0.78% | `python` | `sre_ucs1_match` | library |
| 0.75% | `[kernel.kallsyms]` | `filldir64` | kernel |
| 0.74% | `python` | `k_mul` | int |
| 0.73% | `libc-2.31.so` | `pthread_attr_setschedparam` | libc |
| 0.73% | `python` | `PyObject_IsTrue` | dynamic |
| 0.68% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.65% | `python` | `_PyObject_GetMethod` | dynamic |
| 0.62% | `python` | `take_gil` | unknown |
| 0.61% | `python` | `_Py_Dealloc` | memory |
| 0.60% | `python` | `_pystat_fromstructstat` | unknown |
| 0.58% | `python` | `tp_new_wrapper` | memory |
| 0.57% | `python` | `list_dealloc` | memory |
| 0.57% | `[kernel.kallsyms]` | `strncpy_from_user` | kernel |
| 0.56% | `python` | `_Py_type_getattro` | lookup |
| 0.55% | `python` | `subtype_dealloc` | memory |
| 0.53% | `python` | `_PyUnicode_JoinArray.part.0` | str |

## pickle

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 26.17% | `_pickle.cpython-312-x86_64-linux-gnu.so` | `save` | library |
| 9.04% | `_pickle.cpython-312-x86_64-linux-gnu.so` | `_Pickler_Write` | library |
| 7.60% | `_pickle.cpython-312-x86_64-linux-gnu.so` | `PyMemoTable_Set` | library |
| 4.32% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 4.32% | `_pickle.cpython-312-x86_64-linux-gnu.so` | `Pickler_clear` | library |
| 3.87% | `_pickle.cpython-312-x86_64-linux-gnu.so` | `memo_put.isra.0` | library |
| 3.75% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 3.14% | `python` | `PyDict_Next` | dict |
| 2.79% | `python` | `PyUnicode_AsUTF8AndSize` | str |
| 2.43% | `_pickle.cpython-312-x86_64-linux-gnu.so` | `_Pickler_Write.constprop.3` | library |
| 1.65% | `_pickle.cpython-312-x86_64-linux-gnu.so` | `memo_get.isra.0` | library |
| 1.61% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 1.54% | `libc-2.31.so` | `pthread_attr_setschedparam` | libc |
| 1.35% | `python` | `_PyObject_Free` | memory |
| 1.24% | `python` | `gc_collect_main` | gc |
| 1.14% | `python` | `_PyObject_Malloc` | memory |
| 0.97% | `python` | `_PyType_Lookup` | lookup |
| 0.66% | `python` | `_Py_dict_lookup` | lookup |
| 0.51% | `python` | `visit_decref` | gc |
| 0.51% | `python` | `PyLong_AsLongAndOverflow` | int |

## pickle_dict

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 45.53% | `_pickle.cpython-312-x86_64-linux-gnu.so` | `save` | library |
| 12.01% | `python` | `PyDict_Next` | dict |
| 7.67% | `_pickle.cpython-312-x86_64-linux-gnu.so` | `_Pickler_Write` | library |
| 6.92% | `_pickle.cpython-312-x86_64-linux-gnu.so` | `_Pickler_Write.constprop.3` | library |
| 4.16% | `python` | `PyLong_AsLongAndOverflow` | int |
| 3.12% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 2.07% | `_pickle.cpython-312-x86_64-linux-gnu.so` | `PyMemoTable_Set` | library |
| 1.44% | `_pickle.cpython-312-x86_64-linux-gnu.so` | `Pickler_clear` | library |
| 0.96% | `python` | `gc_collect_main` | gc |
| 0.91% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 0.82% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.76% | `_pickle.cpython-312-x86_64-linux-gnu.so` | `0x0000000000005cc4` | library |
| 0.65% | `_pickle.cpython-312-x86_64-linux-gnu.so` | `memo_put.isra.0` | library |
| 0.57% | `python` | `_PyObject_Malloc` | memory |

## pickle_list

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 49.69% | `_pickle.cpython-312-x86_64-linux-gnu.so` | `save` | library |
| 10.32% | `_pickle.cpython-312-x86_64-linux-gnu.so` | `_Pickler_Write` | library |
| 4.70% | `python` | `PyLong_AsLongAndOverflow` | int |
| 4.70% | `_pickle.cpython-312-x86_64-linux-gnu.so` | `_Pickler_Write.constprop.3` | library |
| 4.52% | `_pickle.cpython-312-x86_64-linux-gnu.so` | `PyMemoTable_Set` | library |
| 2.94% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 2.40% | `_pickle.cpython-312-x86_64-linux-gnu.so` | `Pickler_clear` | library |
| 1.69% | `_pickle.cpython-312-x86_64-linux-gnu.so` | `memo_put.isra.0` | library |
| 1.66% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.47% | `libc-2.31.so` | `pthread_attr_setschedparam` | libc |
| 1.03% | `_pickle.cpython-312-x86_64-linux-gnu.so` | `0x0000000000005cc4` | library |
| 0.75% | `python` | `_PyObject_Malloc` | memory |
| 0.70% | `python` | `gc_collect_main` | gc |
| 0.59% | `python` | `_PyObject_Free` | memory |
| 0.57% | `python` | `PyList_Size` | list |
| 0.55% | `python` | `unicodekeys_lookup_unicode` | lookup |

## pickle_pure_python

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 42.49% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 3.82% | `python` | `_Py_dict_lookup` | lookup |
| 2.72% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 2.69% | `python` | `_PyObject_Malloc` | memory |
| 2.42% | `python` | `_PyObject_Free` | memory |
| 2.30% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 1.70% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.19% | `python` | `initialize_locals` | interpreter |
| 1.13% | `python` | `gc_collect_main` | gc |
| 0.93% | `python` | `PyLong_FromSsize_t` | int |
| 0.92% | `python` | `PyObject_IsTrue` | dynamic |
| 0.92% | `python` | `_PyType_Lookup` | lookup |
| 0.91% | `python` | `tupledealloc` | memory |
| 0.87% | `python` | `PyBuffer_FillInfo` | unknown |
| 0.80% | `python` | `dict_get` | dict |
| 0.72% | `python` | `PyObject_GetAttr` | dynamic |
| 0.67% | `python` | `bytes_concat` | unknown |
| 0.66% | `python` | `PyObject_GenericGetAttr` | dynamic |
| 0.66% | `python` | `visit_decref` | gc |
| 0.66% | `python` | `PyType_GetModuleByDef` | unknown |
| 0.65% | `python` | `PyLong_FromVoidPtr` | int |
| 0.64% | `_struct.cpython-312-x86_64-linux-gnu.so` | `pack` | library |
| 0.64% | `python` | `PyBuffer_Release` | unknown |
| 0.60% | `python` | `_PyThreadState_PopFrame` | interpreter |
| 0.58% | `python` | `PyUnicode_AsEncodedString.part.0` | str |
| 0.57% | `python` | `PyDict_GetItemWithError` | dict |
| 0.57% | `libc-2.31.so` | `pthread_attr_setschedparam` | libc |
| 0.56% | `python` | `insertdict` | dict |
| 0.52% | `python` | `write_bytes` | unknown |

## pidigits

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 35.94% | `python` | `x_divrem` | int |
| 23.00% | `python` | `k_mul` | int |
| 11.49% | `python` | `x_add` | int |
| 7.46% | `python` | `x_sub` | int |
| 4.15% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 2.42% | `libc-2.31.so` | `pthread_attr_setschedparam` | libc |
| 1.64% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 0.79% | `python` | `gc_collect_main` | gc |
| 0.68% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.55% | `python` | `_PyObject_Free` | memory |
| 0.51% | `python` | `_PyObject_Malloc` | memory |

## pprint

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 43.67% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 3.51% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 3.05% | `python` | `_PyObject_Malloc` | memory |
| 3.02% | `python` | `_PyObject_Free` | memory |
| 2.31% | `python` | `_PyType_Lookup` | lookup |
| 1.85% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.84% | `python` | `tupledealloc` | memory |
| 1.42% | `python` | `_PyUnicode_JoinArray.part.0` | str |
| 1.38% | `python` | `_Py_dict_lookup` | lookup |
| 1.31% | `python` | `long_to_decimal_string_internal` | int |
| 1.22% | `python` | `PyUnicode_Format` | str |
| 1.16% | `python` | `_Py_type_getattro_impl` | unknown |
| 0.92% | `python` | `_PyTuple_FromArraySteal` | tuple |
| 0.86% | `python` | `set_lookkey` | set |
| 0.85% | `python` | `tuple_alloc` | memory |
| 0.78% | `python` | `resize_compact` | str |
| 0.76% | `python` | `_Py_type_getattro` | lookup |
| 0.71% | `python` | `_copy_characters.part.0.constprop.0` | str |
| 0.67% | `python` | `list_dealloc` | memory |
| 0.66% | `python` | `list_sort_impl` | list |
| 0.66% | `python` | `_PyTrash_begin` | gc |
| 0.66% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.64% | `python` | `_Py_NewReference` | memory |
| 0.63% | `python` | `_PyTrash_end` | gc |
| 0.60% | `python` | `subtype_dealloc` | memory |
| 0.60% | `python` | `initialize_locals` | interpreter |
| 0.53% | `python` | `PyObject_IsSubclass` | dynamic |
| 0.51% | `python` | `_PyObject_Realloc` | memory |
| 0.50% | `python` | `PyUnicode_New.part.0` | memory |

## pycparser

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 33.28% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 12.20% | `python` | `sre_ucs1_match` | library |
| 4.12% | `python` | `gc_collect_main` | gc |
| 2.40% | `libc-2.31.so` | `pthread_attr_setschedparam` | libc |
| 2.26% | `python` | `_PyObject_Malloc` | memory |
| 2.18% | `python` | `_Py_dict_lookup` | lookup |
| 1.90% | `python` | `_PyObject_Free` | memory |
| 1.75% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 1.17% | `python` | `visit_decref` | gc |
| 1.15% | `python` | `PySlice_AdjustIndices` | slice |
| 1.11% | `python` | `subtype_traverse` | gc |
| 1.08% | `python` | `visit_reachable` | gc |
| 1.01% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.00% | `python` | `initialize_locals` | interpreter |
| 0.96% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 0.90% | `python` | `_PyType_Lookup` | lookup |
| 0.90% | `python` | `sre_ucs1_count` | library |
| 0.89% | `python` | `pattern_new_match.isra.0.part.0` | memory |
| 0.84% | `python` | `subtype_dealloc` | memory |
| 0.82% | `python` | `_sre_SRE_Pattern_match` | library |
| 0.81% | `python` | `list_ass_slice` | list |
| 0.74% | `python` | `PyObject_IsTrue` | dynamic |
| 0.60% | `python` | `_PyObject_FreeInstanceAttributes` | dynamic |
| 0.60% | `python` | `PySlice_New` | memory |
| 0.58% | `python` | `list_dealloc` | memory |
| 0.58% | `python` | `long_neg` | int |
| 0.53% | `python` | `PyNumber_AsSsize_t` | dynamic |
| 0.52% | `python` | `_PyObject_GenericGetAttrWithDict` | dynamic |
| 0.51% | `python` | `_PyEvalFramePushAndInit` | interpreter |

## pyflate

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 45.53% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 4.36% | `python` | `list_dealloc` | memory |
| 4.13% | `python` | `list_ass_slice` | list |
| 2.86% | `python` | `_PyObject_Free` | memory |
| 2.82% | `libc-2.31.so` | `pthread_attr_setschedparam` | libc |
| 2.66% | `python` | `list_slice.isra.0` | list |
| 2.03% | `python` | `_PyObject_Malloc` | memory |
| 1.99% | `python` | `list_concat` | list |
| 1.62% | `python` | `_PyLong_Subtract` | int |
| 1.54% | `python` | `_PyLong_Add` | int |
| 1.44% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.33% | `python` | `PySlice_AdjustIndices` | slice |
| 1.21% | `python` | `bytes_subscript` | unknown |
| 1.15% | `python` | `PyNumber_AsSsize_t` | dynamic |
| 1.11% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.05% | `python` | `PyLong_AsSsize_t` | int |
| 0.99% | `python` | `long_lshift1` | int |
| 0.87% | `python` | `long_lshift` | int |
| 0.84% | `python` | `list_sort_impl` | list |
| 0.82% | `python` | `stringlib_bytes_join` | unknown |
| 0.76% | `python` | `_Py_NewReference` | memory |
| 0.74% | `python` | `PyLong_FromSsize_t` | int |
| 0.73% | `python` | `PyObject_GetItem` | dynamic |
| 0.73% | `python` | `_PyBuildSlice_ConsumeRefs` | slice |
| 0.62% | `python` | `unsafe_long_compare` | unknown |
| 0.61% | `python` | `slice_dealloc` | memory |

## python_startup

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 8.77% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 6.77% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 6.27% | `python` | `gc_collect_main` | gc |
| 3.96% | `python` | `visit_decref` | gc |
| 2.77% | `python` | `visit_reachable` | gc |
| 2.65% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 2.49% | `python` | `_Py_dict_lookup` | lookup |
| 2.33% | `python` | `_PyObject_Malloc` | memory |
| 1.47% | `python` | `update_one_slot` | unknown |
| 1.45% | `python` | `_PyObject_Free` | memory |
| 1.45% | `python` | `_PyStaticCode_Fini` | unknown |
| 1.12% | `python` | `dict_traverse` | gc |
| 1.02% | `python` | `_PyType_Lookup` | lookup |
| 0.99% | `python` | `find_name_in_mro` | lookup |
| 0.88% | `python` | `r_object` | unknown |
| 0.88% | `python` | `type_ready` | dynamic |
| 0.79% | `python` | `_PyCode_Quicken` | interpreter |
| 0.74% | `python` | `siphash13` | str |
| 0.67% | `libc-2.31.so` | `pthread_attr_setschedparam` | libc |
| 0.65% | `python` | `tupledealloc` | memory |
| 0.65% | `[kernel.kallsyms]` | `native_irq_return_iret` | kernel |
| 0.61% | `python` | `set_traverse` | gc |
| 0.59% | `ld-2.31.so` | `_dl_rtld_di_serinfo` | library |
| 0.53% | `python` | `insertdict` | dict |
| 0.53% | `[kernel.kallsyms]` | `zap_pte_range.isra.0` | kernel |
| 0.52% | `python` | `_PyDict_GetItem_KnownHash` | dict |
| 0.52% | `[kernel.kallsyms]` | `__ext4fs_dirhash` | kernel |

## python_startup_no_site

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 7.45% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 6.93% | `python` | `gc_collect_main` | gc |
| 5.95% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 3.51% | `python` | `visit_decref` | gc |
| 3.42% | `python` | `visit_reachable` | gc |
| 3.12% | `python` | `_PyStaticCode_Fini` | unknown |
| 2.44% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 2.03% | `python` | `_Py_dict_lookup` | lookup |
| 1.83% | `python` | `_PyObject_Malloc` | memory |
| 1.73% | `python` | `_PyObject_Free` | memory |
| 1.41% | `python` | `update_one_slot` | unknown |
| 1.37% | `python` | `dict_traverse` | gc |
| 1.23% | `python` | `insertdict` | dict |
| 1.00% | `python` | `free_keys_object` | dict |
| 0.97% | `python` | `_PyCode_Quicken` | interpreter |
| 0.97% | `python` | `siphash13` | str |
| 0.93% | `python` | `r_object` | unknown |
| 0.85% | `python` | `type_ready` | dynamic |
| 0.85% | `ld-2.31.so` | `_dl_rtld_di_serinfo` | library |
| 0.81% | `python` | `find_name_in_mro` | lookup |
| 0.79% | `[kernel.kallsyms]` | `zap_pte_range.isra.0` | kernel |
| 0.76% | `python` | `_PyType_Lookup` | lookup |
| 0.74% | `libc-2.31.so` | `pthread_attr_setschedparam` | libc |
| 0.70% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 0.68% | `python` | `_PyDict_GetItem_KnownHash` | dict |
| 0.57% | `python` | `tupledealloc` | memory |
| 0.56% | `libc-2.31.so` | `__gconv_get_alias_db` | libc |
| 0.54% | `python` | `advance` | interpreter |
| 0.51% | `python` | `ascii_decode` | str |
| 0.51% | `[kernel.kallsyms]` | `native_irq_return_iret` | kernel |

## raytrace

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 49.07% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 3.28% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 2.18% | `python` | `_PyObject_Free` | memory |
| 1.73% | `python` | `PyFloat_FromDouble` | float |
| 1.60% | `python` | `tupledealloc` | memory |
| 1.59% | `python` | `initialize_locals` | interpreter |
| 1.52% | `python` | `subtype_dealloc` | memory |
| 1.39% | `python` | `float_dealloc` | memory |
| 1.36% | `python` | `_PyObject_Malloc` | memory |
| 1.21% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 1.19% | `python` | `PyType_GenericAlloc` | memory |
| 1.16% | `python` | `_PyType_Lookup` | lookup |
| 1.10% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.03% | `python` | `PyType_IsSubtype` | dynamic |
| 1.01% | `python` | `_Py_NewReference` | memory |
| 0.95% | `python` | `_PyTuple_FromArray` | tuple |
| 0.89% | `python` | `_PyObject_MakeTpCall` | dynamic |
| 0.84% | `python` | `PyNumber_Subtract` | dynamic |
| 0.77% | `python` | `slot_tp_init` | unknown |
| 0.76% | `python` | `float_sub` | float |
| 0.73% | `python` | `_PyObject_Call_Prepend` | dynamic |
| 0.68% | `python` | `tuple_alloc` | memory |
| 0.67% | `python` | `_PyEval_Vector` | interpreter |
| 0.67% | `python` | `_PyTrash_end` | gc |
| 0.65% | `python` | `_PyObject_FreeInstanceAttributes` | dynamic |
| 0.65% | `python` | `_PyThreadState_PopFrame` | interpreter |
| 0.63% | `python` | `PyLong_AsDouble` | int |
| 0.61% | `python` | `type_call` | dynamic |
| 0.61% | `python` | `PyObject_Vectorcall` | dynamic |
| 0.58% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.57% | `python` | `_PyTrash_begin` | gc |
| 0.53% | `python` | `_PyObject_InitializeDict` | dynamic |
| 0.51% | `python` | `unicodekeys_lookup_unicode` | lookup |

## regex_compile

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 41.94% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 3.24% | `python` | `sre_ucs1_match` | library |
| 2.69% | `python` | `_PyObject_Malloc` | memory |
| 2.57% | `python` | `_PyObject_Free` | memory |
| 1.94% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.28% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 1.14% | `python` | `tupledealloc` | memory |
| 1.14% | `python` | `_PyType_Lookup` | lookup |
| 1.08% | `python` | `advance` | interpreter |
| 1.07% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 0.93% | `python` | `gc_collect_main` | gc |
| 0.88% | `python` | `bytearray_ass_subscript` | unknown |
| 0.75% | `python` | `PyLong_FromLong` | int |
| 0.75% | `python` | `initialize_locals` | interpreter |
| 0.62% | `python` | `PyObject_IsTrue` | dynamic |
| 0.60% | `python` | `PyObject_GenericGetAttr` | dynamic |
| 0.58% | `python` | `sre_ucs2_charset.isra.0` | library |
| 0.56% | `python` | `_Py_dict_lookup` | lookup |
| 0.53% | `python` | `_PyLong_Add` | int |
| 0.52% | `python` | `sre_search` | library |
| 0.50% | `python` | `PyNumber_AsSsize_t` | dynamic |
| 0.50% | `python` | `_Py_NewReference` | memory |

## regex_dna

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 33.77% | `python` | `sre_ucs1_match` | library |
| 30.78% | `python` | `sre_ucs2_charset.isra.0` | library |
| 6.96% | `python` | `sre_search` | library |
| 6.17% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 2.75% | `libm-2.31.so` | `__fmod_finite` | library |
| 1.19% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.04% | `_bisect.cpython-312-x86_64-linux-gnu.so` | `_bisect_bisect_right` | library |
| 0.91% | `python` | `pattern_subx` | library |
| 0.68% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.67% | `python` | `float_rem` | float |
| 0.61% | `python` | `gc_collect_main` | gc |
| 0.55% | `python` | `_PyObject_Malloc` | memory |
| 0.53% | `python` | `float_richcompare` | float |

## regex_effbot

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 40.91% | `python` | `sre_ucs1_match` | library |
| 16.04% | `python` | `sre_ucs2_charset.isra.0` | library |
| 6.86% | `python` | `sre_search` | library |
| 6.37% | `python` | `_PyObject_Free` | memory |
| 4.52% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 3.12% | `python` | `_PyObject_Malloc` | memory |
| 1.86% | `python` | `sre_ucs1_count` | library |
| 1.13% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 1.09% | `python` | `gc_collect_main` | gc |
| 0.85% | `python` | `PyObject_Malloc` | dynamic |
| 0.57% | `python` | `advance` | interpreter |
| 0.51% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 0.51% | `python` | `siphash13` | str |

## regex_v8

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 44.44% | `python` | `sre_ucs1_match` | library |
| 7.62% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 5.58% | `python` | `sre_search` | library |
| 5.57% | `python` | `sre_ucs1_count` | library |
| 4.31% | `libc-2.31.so` | `pthread_attr_setschedparam` | libc |
| 2.15% | `python` | `pattern_subx` | library |
| 1.86% | `python` | `_PyObject_Free` | memory |
| 1.78% | `python` | `_PyObject_Malloc` | memory |
| 1.63% | `python` | `_sre_SRE_Pattern_search` | library |
| 1.36% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.32% | `python` | `pattern_new_match.isra.0.part.0` | memory |
| 0.92% | `python` | `gc_collect_main` | gc |
| 0.79% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.72% | `libc-2.31.so` | `malloc` | libc |
| 0.65% | `python` | `_PyUnicode_IsAlpha` | str |
| 0.65% | `python` | `_PyUnicode_JoinArray.part.0` | str |

## richards

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 51.99% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 6.22% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 3.76% | `python` | `_PyType_Lookup` | lookup |
| 2.72% | `python` | `PyObject_GenericGetAttr` | dynamic |
| 2.48% | `python` | `_PyObject_GetInstanceAttribute` | dynamic |
| 2.35% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 2.05% | `python` | `_PyObject_GetMethod` | dynamic |
| 1.46% | `python` | `PyObject_GetAttr` | dynamic |
| 1.23% | `python` | `gc_collect_main` | gc |
| 1.21% | `python` | `_Py_dict_lookup` | lookup |
| 0.94% | `python` | `_PyObject_Free` | memory |
| 0.92% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 0.79% | `python` | `find_name_in_mro` | lookup |
| 0.71% | `python` | `_PyThreadState_PopFrame` | interpreter |
| 0.62% | `python` | `_PyObject_Malloc` | memory |
| 0.56% | `python` | `initialize_locals` | interpreter |
| 0.55% | `python` | `_PyDict_GetItem_KnownHash` | dict |
| 0.53% | `python` | `PyObject_GenericSetAttr` | dynamic |
| 0.52% | `python` | `advance` | interpreter |

## scimark

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 44.25% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 3.66% | `array.cpython-312-x86_64-linux-gnu.so` | `array_subscr` | library |
| 3.60% | `python` | `PyFloat_FromDouble` | float |
| 3.51% | `python` | `PyType_GetModuleByDef` | unknown |
| 2.78% | `python` | `PyNumber_AsSsize_t` | dynamic |
| 2.72% | `python` | `_PyObject_Free` | memory |
| 2.60% | `python` | `vgetargs1_impl` | unknown |
| 2.49% | `python` | `PyObject_GetItem` | dynamic |
| 2.13% | `python` | `_PyLong_Add` | int |
| 1.83% | `python` | `_PyObject_Malloc` | memory |
| 1.56% | `python` | `convertitem` | unknown |
| 1.56% | `python` | `PyLong_AsSsize_t` | int |
| 1.40% | `python` | `PyLong_FromLong` | int |
| 1.34% | `array.cpython-312-x86_64-linux-gnu.so` | `array_ass_subscr` | library |
| 1.34% | `python` | `_Py_NewReference` | memory |
| 1.17% | `python` | `float_dealloc` | memory |
| 1.11% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 0.85% | `array.cpython-312-x86_64-linux-gnu.so` | `d_setitem` | library |
| 0.78% | `python` | `_PyLong_Multiply` | int |
| 0.77% | `python` | `_PyArg_Parse_SizeT` | unknown |
| 0.75% | `python` | `_PyFloat_ExactDealloc` | memory |
| 0.74% | `python` | `PyIndex_Check` | unknown |
| 0.70% | `python` | `PyObject_SetItem` | dynamic |
| 0.62% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.58% | `python` | `_PyType_Lookup` | lookup |
| 0.51% | `python` | `_PyLong_Subtract` | int |
| 0.51% | `array.cpython-312-x86_64-linux-gnu.so` | `d_getitem` | library |

## spectral_norm

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 37.76% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 9.53% | `python` | `_PyLong_Add` | int |
| 5.06% | `python` | `_PyObject_Free` | memory |
| 3.51% | `python` | `float_div` | float |
| 3.49% | `python` | `_PyObject_Malloc (inlined)` | memory |
| 2.56% | `python` | `long_div` | int |
| 1.98% | `python` | `_PyLong_Multiply` | int |
| 1.91% | `python` | `PyType_IsSubtype` | dynamic |
| 1.90% | `python` | `enum_next` | unknown |
| 1.78% | `python` | `listiter_next` | list |
| 1.75% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.59% | `python` | `PyLong_FromLong` | int |
| 1.38% | `python` | `_Py_NewReference` | memory |
| 1.32% | `python` | `gc_collect_main` | gc |
| 1.30% | `python` | `PyNumber_TrueDivide` | dynamic |
| 1.17% | `python` | `PyNumber_FloorDivide` | dynamic |
| 1.04% | `python` | `PyLong_AsDouble` | int |
| 1.02% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.67% | `python` | `PyLong_FromSsize_t` | int |
| 0.67% | `python` | `PyObject_Free` | dynamic |
| 0.62% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 0.58% | `python` | `visit_decref` | gc |
| 0.53% | `python` | `PyObject_Malloc` | dynamic |

## sqlalchemy_declarative

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 23.87% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 4.81% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 3.18% | `python` | `gc_collect_main` | gc |
| 2.76% | `python` | `_Py_dict_lookup` | lookup |
| 2.35% | `python` | `_PyObject_Malloc` | memory |
| 2.07% | `python` | `_PyType_Lookup` | lookup |
| 2.02% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.86% | `python` | `visit_decref` | gc |
| 1.84% | `python` | `_PyObject_Free` | memory |
| 1.57% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.50% | `python` | `visit_reachable` | gc |
| 1.36% | `python` | `tupledealloc` | memory |
| 1.32% | `python` | `PyObject_GenericGetAttr` | dynamic |
| 0.86% | `python` | `PyObject_GetAttr` | dynamic |
| 0.84% | `python` | `initialize_locals` | interpreter |
| 0.82% | `python` | `_PyDict_GetItem_KnownHash` | dict |
| 0.73% | `libpthread-2.31.so` | `__pthread_mutex_lock` | library |
| 0.68% | `libpthread-2.31.so` | `pthread_mutex_unlock` | library |
| 0.60% | `python` | `PyObject_IsTrue` | dynamic |
| 0.56% | `python` | `find_name_in_mro` | lookup |
| 0.54% | `python` | `_PyObject_GetMethod` | dynamic |
| 0.54% | `python` | `sre_ucs1_match` | library |
| 0.53% | `python` | `_PyObject_GC_New` | gc |
| 0.52% | `python` | `insertdict` | dict |
| 0.51% | `python` | `dict_traverse` | gc |

## sqlalchemy_imperative

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 28.24% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 4.85% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 2.56% | `python` | `gc_collect_main` | gc |
| 2.33% | `python` | `_Py_dict_lookup` | lookup |
| 2.31% | `python` | `_PyObject_Malloc` | memory |
| 2.26% | `python` | `_PyType_Lookup` | lookup |
| 2.15% | `python` | `PyObject_GenericGetAttr` | dynamic |
| 1.72% | `python` | `_PyObject_Free` | memory |
| 1.68% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.34% | `python` | `tupledealloc` | memory |
| 1.25% | `python` | `PyObject_GetAttr` | dynamic |
| 1.16% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.12% | `python` | `visit_decref` | gc |
| 0.92% | `python` | `initialize_locals` | interpreter |
| 0.77% | `python` | `visit_reachable` | gc |
| 0.64% | `libpthread-2.31.so` | `__pthread_mutex_lock` | library |
| 0.62% | `python` | `PyDict_GetItemWithError` | dict |
| 0.61% | `python` | `_PyObject_GetMethod` | dynamic |
| 0.60% | `python` | `PyObject_IsTrue` | dynamic |
| 0.58% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.57% | `python` | `subtype_dealloc` | memory |
| 0.56% | `python` | `sre_ucs1_match` | library |
| 0.54% | `python` | `_PyObject_GC_New` | gc |
| 0.54% | `python` | `tuple_alloc` | memory |
| 0.50% | `python` | `insertdict` | dict |

## sqlglot

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 36.89% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 2.93% | `python` | `_PyObject_Free` | memory |
| 2.78% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 2.36% | `python` | `_PyType_Lookup` | lookup |
| 2.36% | `python` | `_PyObject_Malloc` | memory |
| 2.01% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.63% | `python` | `PyObject_GenericGetAttr` | dynamic |
| 1.48% | `python` | `PyType_IsSubtype` | dynamic |
| 1.39% | `python` | `gc_collect_main` | gc |
| 1.26% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.25% | `python` | `tupledealloc` | memory |
| 1.21% | `python` | `_Py_dict_lookup` | lookup |
| 1.21% | `python` | `_PyObject_GenericGetAttrWithDict` | dynamic |
| 1.13% | `python` | `initialize_locals` | interpreter |
| 1.05% | `python` | `PyObject_GetAttr` | dynamic |
| 0.94% | `python` | `dictiter_iternextitem` | unknown |
| 0.83% | `python` | `_PyObject_LookupSpecial` | dynamic |
| 0.82% | `python` | `PyObject_IsTrue` | dynamic |
| 0.79% | `python` | `_PyObject_GC_New` | gc |
| 0.75% | `python` | `visit_decref` | gc |
| 0.63% | `python` | `PyObject_IsInstance` | dynamic |
| 0.63% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.59% | `python` | `_Py_NewReference` | memory |
| 0.58% | `python` | `_PyTrash_end` | gc |
| 0.55% | `python` | `_PyObject_LookupAttr` | dynamic |
| 0.54% | `python` | `_PyTrash_begin` | gc |
| 0.53% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.52% | `python` | `object_isinstance` | unknown |
| 0.52% | `python` | `PyObject_GC_Del` | gc |
| 0.50% | `python` | `_PyObject_GetInstanceAttribute` | dynamic |

## sqlite_synth

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 11.83% | `libpthread-2.31.so` | `pthread_mutex_unlock` | library |
| 11.81% | `libpthread-2.31.so` | `__pthread_mutex_lock` | library |
| 8.98% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 4.36% | `libsqlite3.so.0.8.6` | `sqlite3_reset` | library |
| 2.83% | `python` | `take_gil` | unknown |
| 2.29% | `python` | `_PyObject_Malloc` | memory |
| 2.23% | `python` | `_PyObject_Free` | memory |
| 2.07% | `libm-2.31.so` | `f64xsubf128` | library |
| 1.29% | `libsqlite3.so.0.8.6` | `sqlite3_randomness` | library |
| 1.14% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 1.10% | `libpthread-2.31.so` | `pthread_cond_signal@@GLIBC_2.3.2` | library |
| 1.04% | `python` | `_PyThreadState_Swap` | unknown |
| 1.02% | `python` | `drop_gil` | unknown |
| 0.97% | `python` | `tupledealloc` | memory |
| 0.92% | `libsqlite3.so.0.8.6` | `sqlite3_value_double` | library |
| 0.92% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 0.88% | `python` | `gc_collect_main` | gc |
| 0.86% | `libc-2.31.so` | `pthread_attr_setschedparam` | libc |
| 0.85% | `_sqlite3.cpython-312-x86_64-linux-gnu.so` | `_pysqlite_query_execute` | library |
| 0.78% | `libsqlite3.so.0.8.6` | `sqlite3_value_int64` | library |
| 0.72% | `libsqlite3.so.0.8.6` | `sqlite3_wal_checkpoint` | library |
| 0.72% | `python` | `long_to_decimal_string_internal` | int |
| 0.71% | `libsqlite3.so.0.8.6` | `sqlite3_extended_errcode` | library |
| 0.71% | `libsqlite3.so.0.8.6` | `sqlite3_preupdate_old` | library |
| 0.69% | `libsqlite3.so.0.8.6` | `sqlite3_vtab_config` | library |
| 0.65% | `python` | `PyFloat_FromDouble` | float |
| 0.59% | `python` | `PyList_New` | memory |
| 0.59% | `python` | `_Py_NewReference` | memory |
| 0.55% | `python` | `list_dealloc` | memory |
| 0.51% | `libsqlite3.so.0.8.6` | `sqlite3_step` | library |
| 0.50% | `libsqlite3.so.0.8.6` | `sqlite3_str_value` | library |

## sympy

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 25.90% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 3.83% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 2.80% | `python` | `_PyObject_Malloc` | memory |
| 2.38% | `python` | `_PyObject_Free` | memory |
| 2.37% | `python` | `_PyType_Lookup` | lookup |
| 1.80% | `python` | `tupledealloc` | memory |
| 1.78% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.46% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.38% | `python` | `gc_collect_main` | gc |
| 1.36% | `python` | `initialize_locals` | interpreter |
| 1.26% | `python` | `_Py_dict_lookup` | lookup |
| 1.06% | `python` | `PyObject_GenericGetAttr` | dynamic |
| 1.03% | `python` | `PyType_IsSubtype` | dynamic |
| 0.95% | `python` | `PyObject_RichCompare` | dynamic |
| 0.81% | `python` | `PyObject_GetAttr` | dynamic |
| 0.76% | `python` | `tuple_alloc` | memory |
| 0.74% | `python` | `_PyObject_GC_New` | gc |
| 0.74% | `python` | `_Py_dict_lookup` | lookup |
| 0.72% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.68% | `python` | `visit_decref` | gc |
| 0.66% | `python` | `insertdict` | dict |
| 0.61% | `python` | `_PyTrash_end` | gc |
| 0.61% | `python` | `_PyTrash_begin` | gc |
| 0.60% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.56% | `python` | `_Py_type_getattro` | lookup |
| 0.55% | `python` | `advance` | interpreter |
| 0.54% | `python` | `PyObject_GC_Del` | gc |
| 0.53% | `python` | `_PyCode_Quicken` | interpreter |
| 0.50% | `python` | `visit_reachable` | gc |

## telco

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 17.31% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 5.05% | `python` | `_PyObject_Malloc` | memory |
| 4.26% | `python` | `_PyObject_Free` | memory |
| 2.20% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 2.00% | `_decimal.cpython-312-x86_64-linux-gnu.so` | `_mpd_qaddsub` | library |
| 1.93% | `_decimal.cpython-312-x86_64-linux-gnu.so` | `_mpd_check_exp` | library |
| 1.67% | `python` | `PyContextVar_Get` | unknown |
| 1.63% | `_decimal.cpython-312-x86_64-linux-gnu.so` | `_mpd_qmul` | library |
| 1.62% | `_decimal.cpython-312-x86_64-linux-gnu.so` | `mpd_setdigits` | library |
| 1.55% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 1.44% | `_decimal.cpython-312-x86_64-linux-gnu.so` | `nm_mpd_qadd` | library |
| 1.43% | `_decimal.cpython-312-x86_64-linux-gnu.so` | `_mpd_baseshiftr` | library |
| 1.38% | `python` | `tupledealloc` | memory |
| 1.34% | `python` | `PyObject_GenericGetAttr` | dynamic |
| 1.32% | `python` | `convertitem` | unknown |
| 1.28% | `python` | `gc_collect_main` | gc |
| 1.24% | `_decimal.cpython-312-x86_64-linux-gnu.so` | `mpd_qquantize` | library |
| 1.20% | `python` | `_PyArg_UnpackKeywordsWithVararg` | unknown |
| 1.14% | `python` | `vgetargskeywords` | unknown |
| 1.04% | `_decimal.cpython-312-x86_64-linux-gnu.so` | `nm_mpd_qmul` | library |
| 0.98% | `python` | `PyUnicode_AsUCS4` | str |
| 0.92% | `_decimal.cpython-312-x86_64-linux-gnu.so` | `mpd_qshiftr` | library |
| 0.92% | `python` | `_PyType_Lookup` | lookup |
| 0.85% | `python` | `_PyObject_New` | memory |
| 0.84% | `python` | `meth_dealloc` | memory |
| 0.84% | `python` | `_PyTrash_begin` | gc |
| 0.83% | `python` | `vgetargs1_impl` | unknown |
| 0.79% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.77% | `python` | `tuple_alloc` | memory |
| 0.77% | `_decimal.cpython-312-x86_64-linux-gnu.so` | `dec_addstatus` | library |
| 0.75% | `python` | `_PyTrash_end` | gc |
| 0.70% | `_decimal.cpython-312-x86_64-linux-gnu.so` | `dec_mpd_qquantize` | library |
| 0.69% | `_decimal.cpython-312-x86_64-linux-gnu.so` | `mpd_qfinalize.part.0` | library |
| 0.63% | `python` | `PyNumber_InPlaceAdd` | dynamic |
| 0.62% | `python` | `PyObject_GetAttr` | dynamic |
| 0.59% | `python` | `visit_decref` | gc |
| 0.55% | `python` | `_PyTuple_FromArray` | tuple |
| 0.54% | `python` | `_Py_dict_lookup` | lookup |
| 0.52% | `python` | `PyCMethod_New` | memory |
| 0.50% | `python` | `PyNumber_Multiply` | dynamic |

## thrift

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 21.65% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 3.61% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 3.32% | `python` | `_PyObject_Malloc` | memory |
| 2.94% | `python` | `initialize_locals` | interpreter |
| 2.77% | `python` | `_PyObject_Free` | memory |
| 1.89% | `python` | `PyObject_GenericGetAttr` | dynamic |
| 1.83% | `python` | `_PyType_Lookup` | lookup |
| 1.71% | `fastbinary.cpython-312-x86_64-linux-gnu.so` | `apache::thrift::py::ProtocolBase<apache::thrift::py::BinaryProtocol>::encodeValue` | library |
| 1.62% | `python` | `insert_to_emptydict` | dict |
| 1.56% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.46% | `python` | `_Py_dict_lookup` | lookup |
| 1.41% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.32% | `python` | `insertdict` | dict |
| 1.15% | `python` | `subtype_dealloc` | memory |
| 1.13% | `python` | `gc_collect_main` | gc |
| 1.12% | `python` | `tupledealloc` | memory |
| 0.98% | `python` | `PyType_GenericAlloc` | memory |
| 0.89% | `python` | `dict_dealloc` | memory |
| 0.88% | `python` | `_PyObject_Call_Prepend` | dynamic |
| 0.86% | `python` | `_PyStack_UnpackDict` | unknown |
| 0.81% | `python` | `PyObject_GetAttr` | dynamic |
| 0.80% | `python` | `slot_tp_init` | unknown |
| 0.80% | `python` | `PyUnicode_FromFormatV` | str |
| 0.75% | `python` | `_PyTrash_begin` | gc |
| 0.74% | `python` | `_PyObject_MakeTpCall` | dynamic |
| 0.70% | `python` | `free_keys_object` | dict |
| 0.67% | `python` | `PyObject_RichCompare` | dynamic |
| 0.67% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.66% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.65% | `python` | `_Py_NewReference` | memory |
| 0.64% | `python` | `_PyTrash_end` | gc |
| 0.62% | `python` | `PyLong_AsLong` | int |
| 0.61% | `fastbinary.cpython-312-x86_64-linux-gnu.so` | `apache::thrift::py::ProtocolBase<apache::thrift::py::BinaryProtocol>::decodeValue` | library |
| 0.58% | `python` | `list_dealloc` | memory |
| 0.57% | `python` | `PyTuple_Size` | tuple |
| 0.56% | `python` | `_PyObject_InitializeDict` | dynamic |
| 0.54% | `python` | `PyDict_GetItemWithError` | dict |
| 0.54% | `python` | `PyDict_SetItem` | dict |
| 0.51% | `python` | `_Py_Dealloc` | memory |

## tornado_http

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 26.87% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 3.98% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 2.54% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 2.49% | `python` | `_PyObject_Malloc` | memory |
| 2.14% | `python` | `gc_collect_main` | gc |
| 1.87% | `python` | `_PyObject_Free` | memory |
| 1.29% | `python` | `_PyType_Lookup` | lookup |
| 1.19% | `python` | `visit_decref` | gc |
| 1.06% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.02% | `python` | `_Py_dict_lookup` | lookup |
| 0.96% | `python` | `visit_reachable` | gc |
| 0.88% | `python` | `advance` | interpreter |
| 0.86% | `python` | `initialize_locals` | interpreter |
| 0.78% | `python` | `tupledealloc` | memory |
| 0.65% | `[kernel.kallsyms]` | `copy_user_enhanced_fast_string` | kernel |
| 0.64% | `libc-2.31.so` | `pthread_attr_setschedparam` | libc |
| 0.59% | `python` | `PyObject_GenericGetAttr` | dynamic |
| 0.54% | `python` | `PyObject_GC_UnTrack` | gc |

## unpack_sequence

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 80.90% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 1.21% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.93% | `python` | `gc_collect_main` | gc |
| 0.72% | `python` | `_PyObject_Free` | memory |
| 0.72% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 0.52% | `python` | `visit_reachable` | gc |
| 0.50% | `python` | `_PyObject_Malloc` | memory |

## unpickle

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 7.65% | `_pickle.cpython-312-x86_64-linux-gnu.so` | `load` | library |
| 6.58% | `_pickle.cpython-312-x86_64-linux-gnu.so` | `load_counted_binunicode` | library |
| 6.02% | `python` | `siphash13` | str |
| 5.25% | `python` | `insertdict` | dict |
| 5.12% | `python` | `_PyObject_Free` | memory |
| 5.10% | `python` | `ascii_decode` | str |
| 4.90% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 4.63% | `python` | `unicode_decode_utf8` | str |
| 4.51% | `python` | `_PyObject_Malloc` | memory |
| 3.36% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 2.95% | `python` | `PyUnicode_New.part.0` | memory |
| 2.60% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 2.22% | `python` | `_Py_dict_lookup` | lookup |
| 1.96% | `_pickle.cpython-312-x86_64-linux-gnu.so` | `do_setitems.isra.0` | library |
| 1.84% | `_pickle.cpython-312-x86_64-linux-gnu.so` | `_Unpickler_MemoPut` | library |
| 1.81% | `python` | `free_keys_object` | dict |
| 1.68% | `python` | `dict_ass_sub` | dict |
| 1.40% | `python` | `_PyObject_Realloc` | memory |
| 1.26% | `python` | `find_empty_slot` | dict |
| 1.23% | `python` | `build_indices_unicode` | dict |
| 1.08% | `python` | `PyObject_SetItem` | dynamic |
| 0.89% | `python` | `unicode_dealloc` | memory |
| 0.86% | `python` | `PyObject_IS_GC` | gc |
| 0.84% | `_pickle.cpython-312-x86_64-linux-gnu.so` | `Unpickler_clear` | library |
| 0.81% | `python` | `_Py_NewReference` | memory |
| 0.77% | `python` | `gc_collect_main` | gc |
| 0.67% | `python` | `list_dealloc` | memory |
| 0.63% | `_pickle.cpython-312-x86_64-linux-gnu.so` | `Pdata_push` | library |
| 0.63% | `python` | `PyLong_FromLong` | int |
| 0.62% | `libc-2.31.so` | `pthread_attr_setschedparam` | libc |
| 0.60% | `python` | `_Py_Dealloc` | memory |
| 0.54% | `python` | `dictresize` | unknown |
| 0.50% | `python` | `unicode_hash` | str |

## unpickle_list

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 17.37% | `_pickle.cpython-312-x86_64-linux-gnu.so` | `load` | library |
| 7.67% | `python` | `list_dealloc` | memory |
| 5.75% | `python` | `list_ass_slice` | list |
| 5.36% | `python` | `PyList_New` | memory |
| 5.16% | `python` | `PyLong_FromLong` | int |
| 4.93% | `python` | `_PyObject_Free` | memory |
| 4.45% | `_pickle.cpython-312-x86_64-linux-gnu.so` | `Pdata_push` | library |
| 3.84% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 3.62% | `_pickle.cpython-312-x86_64-linux-gnu.so` | `do_append.isra.0` | library |
| 3.07% | `python` | `_PyObject_Malloc` | memory |
| 2.42% | `python` | `_PyObject_Calloc` | memory |
| 2.16% | `python` | `PyMem_Calloc` | memory |
| 1.88% | `python` | `_Py_NewReference` | memory |
| 1.65% | `python` | `PyObject_GC_UnTrack` | gc |
| 1.48% | `python` | `_PyObject_Realloc` | memory |
| 1.47% | `python` | `_PyTrash_begin` | gc |
| 1.39% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.34% | `_pickle.cpython-312-x86_64-linux-gnu.so` | `marker.isra.0` | library |
| 1.32% | `python` | `gc_collect_main` | gc |
| 1.19% | `python` | `_PyTrash_end` | gc |
| 1.08% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.90% | `_pickle.cpython-312-x86_64-linux-gnu.so` | `_Unpickler_MemoPut` | library |
| 0.70% | `_pickle.cpython-312-x86_64-linux-gnu.so` | `0x0000000000005ba4` | library |
| 0.68% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 0.53% | `python` | `visit_decref` | gc |
| 0.53% | `python` | `_Py_Dealloc` | memory |
| 0.51% | `python` | `advance` | interpreter |

## unpickle_pure_python

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 49.53% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 2.48% | `python` | `_Py_dict_lookup` | lookup |
| 2.46% | `python` | `PyObject_IsTrue` | dynamic |
| 2.01% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.68% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.65% | `python` | `_PyObject_Free` | memory |
| 1.63% | `python` | `bytes_subscript` | unknown |
| 1.52% | `python` | `_PyObject_Malloc` | memory |
| 1.35% | `python` | `PyNumber_AsSsize_t` | dynamic |
| 1.10% | `python` | `insertdict` | dict |
| 1.10% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 1.09% | `python` | `PyBytes_FromStringAndSize` | unknown |
| 1.00% | `python` | `initialize_locals` | interpreter |
| 0.93% | `python` | `_io_BytesIO_read` | unknown |
| 0.93% | `python` | `advance` | interpreter |
| 0.85% | `python` | `gc_collect_main` | gc |
| 0.71% | `python` | `PyUnicode_Decode.part.0` | str |
| 0.69% | `python` | `PyLong_FromSsize_t` | int |
| 0.67% | `python` | `tupledealloc` | memory |
| 0.65% | `python` | `PyLong_AsSsize_t` | int |
| 0.62% | `python` | `PyObject_GetItem` | dynamic |
| 0.62% | `python` | `PyDict_GetItemWithError` | dict |
| 0.61% | `python` | `_PyThreadState_PopFrame` | interpreter |
| 0.55% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.53% | `python` | `_Py_convert_optional_to_ssize_t` | unknown |
| 0.53% | `python` | `PyObject_IsInstance` | dynamic |
| 0.53% | `python` | `siphash13` | str |
| 0.51% | `python` | `ascii_decode` | str |

## xml_etree

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 19.90% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 3.31% | `python` | `_PyObject_Malloc` | memory |
| 3.09% | `python` | `gc_collect_main` | gc |
| 2.62% | `pyexpat.cpython-312-x86_64-linux-gnu.so` | `normal_contentTok` | library |
| 2.58% | `pyexpat.cpython-312-x86_64-linux-gnu.so` | `normal_updatePosition` | library |
| 2.30% | `python` | `_PyObject_Free` | memory |
| 1.89% | `python` | `_PyType_Lookup` | lookup |
| 1.87% | `python` | `PyObject_GenericGetAttr` | dynamic |
| 1.87% | `python` | `visit_reachable` | gc |
| 1.77% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.67% | `python` | `visit_decref` | gc |
| 1.58% | `pyexpat.cpython-312-x86_64-linux-gnu.so` | `accountingDiffTolerated.part.0` | library |
| 1.56% | `python` | `_Py_dict_lookup` | lookup |
| 1.43% | `pyexpat.cpython-312-x86_64-linux-gnu.so` | `sip24_update` | library |
| 1.35% | `python` | `_io_TextIOWrapper_write` | unknown |
| 1.28% | `pyexpat.cpython-312-x86_64-linux-gnu.so` | `doContent` | library |
| 1.23% | `pyexpat.cpython-312-x86_64-linux-gnu.so` | `normal_nameLength` | library |
| 1.04% | `python` | `initialize_locals` | interpreter |
| 0.89% | `_elementtree.cpython-312-x86_64-linux-gnu.so` | `element_gc_traverse` | library |
| 0.89% | `pyexpat.cpython-312-x86_64-linux-gnu.so` | `lookup.constprop.0` | library |
| 0.84% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.81% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 0.81% | `python` | `tupledealloc` | memory |
| 0.79% | `python` | `PyObject_GetAttr` | dynamic |
| 0.76% | `python` | `PyUnicode_Contains` | str |
| 0.75% | `python` | `ascii_decode` | str |
| 0.75% | `python` | `PyObject_IsTrue` | dynamic |
| 0.75% | `python` | `PyUnicode_New.part.0` | memory |
| 0.74% | `python` | `siphash13` | str |
| 0.74% | `python` | `_copy_characters.part.0.constprop.0` | str |
| 0.73% | `pyexpat.cpython-312-x86_64-linux-gnu.so` | `normal_getAtts` | library |
| 0.72% | `python` | `_PyObject_GetMethod` | dynamic |
| 0.72% | `_elementtree.cpython-312-x86_64-linux-gnu.so` | `elementiter_next` | library |
| 0.72% | `pyexpat.cpython-312-x86_64-linux-gnu.so` | `sip24_final` | library |
| 0.68% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.68% | `_elementtree.cpython-312-x86_64-linux-gnu.so` | `expat_end_handler` | library |
| 0.62% | `python` | `list_dealloc` | memory |
| 0.61% | `python` | `_PyObject_GC_New` | gc |
| 0.59% | `python` | `_PyObject_GenericGetAttrWithDict` | dynamic |
| 0.59% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.57% | `python` | `getset_get` | unknown |
| 0.55% | `_elementtree.cpython-312-x86_64-linux-gnu.so` | `treebuilder_handle_start` | library |
| 0.55% | `python` | `unicode_decode_utf8` | str |
| 0.52% | `python` | `_PyTrash_end` | gc |
| 0.52% | `python` | `_Py_NewReference` | memory |
| 0.50% | `pyexpat.cpython-312-x86_64-linux-gnu.so` | `storeAtts` | library |


## Categories

### interpreter

31.61% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 28.45% | python | _PyEval_EvalFrameDefault |
| 1.18% | python | _PyFrame_ClearExceptCode |
| 0.66% | python | initialize_locals |
| 0.40% | python | advance |
| 0.33% | python | _PyEvalFramePushAndInit |
| 0.23% | python | _PyCode_Quicken |
| 0.22% | python | _PyThreadState_PopFrame |
| 0.13% | python | _PyEval_Vector |
| 0.01% | python | _PyFrame_New_NoTrack |

### memory

10.75% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 2.25% | python | _PyObject_Free |
| 2.01% | python | _PyObject_Malloc |
| 0.71% | python | tupledealloc |
| 0.55% | python | list_dealloc |
| 0.51% | python | _Py_NewReference |
| 0.30% | python | _PyObject_Malloc (inlined) |
| 0.29% | python | tuple_alloc |
| 0.26% | python | subtype_dealloc |
| 0.26% | python | PyType_GenericAlloc |
| 0.23% | python | _Py_Dealloc |
| 0.23% | python | _PyObject_Realloc |
| 0.18% | python | PyUnicode_New.part.0 |
| 0.17% | python | dict_dealloc |
| 0.16% | python | unicode_dealloc |
| 0.15% | python | gen_dealloc |
| 0.14% | python | PyList_New |
| 0.13% | python | float_dealloc |
| 0.12% | python | PyFunction_NewWithQualName |
| 0.11% | python | code_dealloc |
| 0.10% | python | set_dealloc |
| 0.09% | python | slice_dealloc |
| 0.09% | python | _PyObject_Calloc |
| 0.08% | python | PyList_New.constprop.0 |
| 0.07% | python | object_dealloc |
| 0.07% | python | meth_dealloc |
| 0.07% | python | PyDict_New |
| 0.07% | python | PyUnicode_New |
| 0.07% | python | func_dealloc |
| 0.06% | python | PyMem_Calloc |
| 0.06% | python | PyCMethod_New |
| 0.06% | python | frame_dealloc |
| 0.06% | python | PyTuple_New |
| 0.06% | python | pattern_new_match.isra.0.part.0 |
| 0.05% | python | PyObject_CallFinalizerFromDealloc |
| 0.04% | python | object_new |
| 0.04% | python | allocate_from_new_pool |
| 0.04% | python | method_dealloc |
| 0.04% | python | PyMethod_New |
| 0.04% | python | listiter_dealloc |
| 0.03% | python | PySlice_New |
| 0.03% | python | _PyCode_New |
| 0.03% | python | PyMem_Free |
| 0.03% | python | _PyFloat_ExactDealloc |
| 0.03% | python | _PyObject_New |
| 0.03% | python | context_tp_dealloc |
| 0.02% | python | BaseException_new |
| 0.02% | python | tp_new_wrapper |
| 0.02% | python | type_new |
| 0.02% | python | cell_dealloc |
| 0.02% | python | tb_dealloc |
| 0.02% | python | PyMem_Malloc |
| 0.02% | python | async_gen_asend_dealloc |
| 0.02% | python | PyMem_Realloc |
| 0.02% | python | async_gen_wrapped_val_dealloc |
| 0.02% | python | range_dealloc |
| 0.02% | python | _PyAsyncGenValueWrapperNew |
| 0.02% | python | StopIteration_dealloc |
| 0.01% | python | PyCell_New |
| 0.01% | python | structseq_dealloc |
| 0.01% | python | tupleiter_dealloc |
| 0.01% | python | BaseException_dealloc |
| 0.01% | python | PyWeakref_NewRef |
| 0.01% | python | weakref___new__ |
| 0.01% | python | unicode_new |
| 0.01% | python | _PyUnicode_ExactDealloc |
| 0.01% | python | AttributeError_dealloc |
| 0.01% | python | weakref_dealloc |
| 0.01% | python | dictiter_dealloc |
| 0.01% | python | super_dealloc |
| 0.01% | python | _PyMem_RawMalloc |
| 0.01% | python | _Py_NewReferenceNoTotal |
| 0.01% | python | reversed_new_impl |
| 0.01% | python | dictitems_new |
| 0.01% | python | long_new |

### gc

10.49% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 3.73% | python | gc_collect_main |
| 1.57% | python | visit_decref |
| 1.53% | python | visit_reachable |
| 0.38% | python | PyObject_GC_UnTrack |
| 0.30% | python | _PyTrash_end |
| 0.30% | python | dict_traverse |
| 0.29% | python | _PyTrash_begin |
| 0.29% | python | PyObject_GC_Del |
| 0.28% | python | list_traverse |
| 0.26% | python | _PyObject_GC_New |
| 0.24% | python | subtype_traverse |
| 0.22% | python | PyObject_IS_GC |
| 0.16% | python | _PyObject_GC_Link |
| 0.15% | python | _PyObject_GC_NewVar |
| 0.10% | python | _PyObject_VisitManagedDict |
| 0.10% | python | set_traverse |
| 0.10% | python | func_traverse |
| 0.09% | python | _PyTrash_cond |
| 0.07% | python | _PyDict_MaybeUntrack |
| 0.07% | python | type_is_gc |
| 0.05% | python | type_traverse |
| 0.05% | python | _PyTuple_MaybeUntrack |
| 0.03% | python | PyObject_GC_Track |
| 0.02% | python | meth_traverse |
| 0.02% | python | gc_traverse |
| 0.02% | python | gen_traverse |
| 0.01% | python | context_tp_traverse |
| 0.01% | python | descr_traverse |
| 0.01% | python | cell_traverse |
| 0.01% | python | module_traverse |

### library

10.22% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 2.05% | python | sre_ucs1_match |
| 1.64% | _pickle.cpython-312-x86_64-linux-gnu.so | save |
| 0.81% | python | sre_ucs2_charset.isra.0 |
| 0.37% | _pickle.cpython-312-x86_64-linux-gnu.so | _Pickler_Write |
| 0.35% | _json.cpython-312-x86_64-linux-gnu.so | scanstring_unicode |
| 0.34% | _pickle.cpython-312-x86_64-linux-gnu.so | load |
| 0.29% | python | sre_search |
| 0.24% | libpthread-2.31.so | __pthread_mutex_lock |
| 0.22% | libpthread-2.31.so | pthread_mutex_unlock |
| 0.20% | _json.cpython-312-x86_64-linux-gnu.so | scan_once_unicode |
| 0.19% | _pickle.cpython-312-x86_64-linux-gnu.so | PyMemoTable_Set |
| 0.19% | _pickle.cpython-312-x86_64-linux-gnu.so | _Pickler_Write.constprop.3 |
| 0.18% | python | sre_ucs1_count |
| 0.16% | libm-2.31.so | f64xsubf128 |
| 0.11% | _json.cpython-312-x86_64-linux-gnu.so | py_encode_basestring_ascii |
| 0.11% | _pickle.cpython-312-x86_64-linux-gnu.so | Pickler_clear |
| 0.09% | _pickle.cpython-312-x86_64-linux-gnu.so | load_counted_binunicode |
| 0.08% | _pickle.cpython-312-x86_64-linux-gnu.so | memo_put.isra.0 |
| 0.08% | tracer.cpython-312-x86_64-linux-gnu.so | CTracer_trace |
| 0.07% | ld-2.31.so | _dl_rtld_di_serinfo |
| 0.07% | libsqlite3.so.0.8.6 | sqlite3_reset |
| 0.07% | _pickle.cpython-312-x86_64-linux-gnu.so | Pdata_push |
| 0.05% | python | pattern_subx |
| 0.05% | _pickle.cpython-312-x86_64-linux-gnu.so | do_append.isra.0 |
| 0.05% | libz.so.1.2.11 | inflateBackEnd |
| 0.05% | array.cpython-312-x86_64-linux-gnu.so | array_subscr |
| 0.04% | python | _sre_SRE_Pattern_match |
| 0.04% | _json.cpython-312-x86_64-linux-gnu.so | encoder_listencode_obj |
| 0.04% | libz.so.1.2.11 | inflateCodesUsed |
| 0.04% | python | _sre_SRE_Pattern_search |
| 0.04% | libm-2.31.so | __fmod_finite |
| 0.04% | _pickle.cpython-312-x86_64-linux-gnu.so | _Unpickler_MemoPut |
| 0.04% | pyexpat.cpython-312-x86_64-linux-gnu.so | normal_contentTok |
| 0.03% | pyexpat.cpython-312-x86_64-linux-gnu.so | normal_updatePosition |
| 0.03% | _json.cpython-312-x86_64-linux-gnu.so | encoder_encode_key_value |
| 0.03% | _decimal.cpython-312-x86_64-linux-gnu.so | _mpd_qaddsub |
| 0.03% | _pickle.cpython-312-x86_64-linux-gnu.so | do_setitems.isra.0 |
| 0.03% | libpthread-2.31.so | pthread_cond_signal@@GLIBC_2.3.2 |
| 0.03% | _decimal.cpython-312-x86_64-linux-gnu.so | _mpd_check_exp |
| 0.03% | _pickle.cpython-312-x86_64-linux-gnu.so | 0x0000000000005cc4 |
| 0.02% | _asyncio.cpython-312-x86_64-linux-gnu.so | TaskObj_traverse |
| 0.02% | ld-2.31.so | _dl_catch_error |
| 0.02% | libsqlite3.so.0.8.6 | sqlite3_randomness |
| 0.02% | fastbinary.cpython-312-x86_64-linux-gnu.so | apache::thrift::py::ProtocolBase<apache::thrift::py::BinaryProtocol>::encodeValue |
| 0.02% | libz.so.1.2.11 | inflate |
| 0.02% | _pickle.cpython-312-x86_64-linux-gnu.so | memo_get.isra.0 |
| 0.02% | _decimal.cpython-312-x86_64-linux-gnu.so | _mpd_qmul |
| 0.02% | _decimal.cpython-312-x86_64-linux-gnu.so | mpd_setdigits |
| 0.02% | pyexpat.cpython-312-x86_64-linux-gnu.so | accountingDiffTolerated.part.0 |
| 0.02% | _pickle.cpython-312-x86_64-linux-gnu.so | marker.isra.0 |
| 0.02% | _decimal.cpython-312-x86_64-linux-gnu.so | nm_mpd_qadd |
| 0.02% | _decimal.cpython-312-x86_64-linux-gnu.so | _mpd_baseshiftr |
| 0.02% | pyexpat.cpython-312-x86_64-linux-gnu.so | sip24_update |
| 0.02% | _asyncio.cpython-312-x86_64-linux-gnu.so | task_step |
| 0.02% | array.cpython-312-x86_64-linux-gnu.so | array_ass_subscr |
| 0.02% | pyexpat.cpython-312-x86_64-linux-gnu.so | doContent |
| 0.02% | libpthread-2.31.so | __errno_location |
| 0.02% | _pickle.cpython-312-x86_64-linux-gnu.so | Unpickler_clear |
| 0.02% | _decimal.cpython-312-x86_64-linux-gnu.so | mpd_qquantize |
| 0.02% | pyexpat.cpython-312-x86_64-linux-gnu.so | normal_nameLength |
| 0.02% | math.cpython-312-x86_64-linux-gnu.so | factorial_partial_product |
| 0.02% | libsqlite3.so.0.8.6 | sqlite3_exec |
| 0.01% | libsqlite3.so.0.8.6 | sqlite3_value_double |
| 0.01% | _elementtree.cpython-312-x86_64-linux-gnu.so | element_gc_traverse |
| 0.01% | _bisect.cpython-312-x86_64-linux-gnu.so | _bisect_bisect_right |
| 0.01% | _decimal.cpython-312-x86_64-linux-gnu.so | nm_mpd_qmul |
| 0.01% | libsqlite3.so.0.8.6 | sqlite3_value_int64 |
| 0.01% | _decimal.cpython-312-x86_64-linux-gnu.so | mpd_qshiftr |
| 0.01% | _sqlite3.cpython-312-x86_64-linux-gnu.so | _pysqlite_query_execute |
| 0.01% | pyexpat.cpython-312-x86_64-linux-gnu.so | lookup.constprop.0 |
| 0.01% | libpthread-2.31.so | sem_post@@GLIBC_2.2.5 |
| 0.01% | array.cpython-312-x86_64-linux-gnu.so | d_setitem |
| 0.01% | libpthread-2.31.so | sem_trywait@@GLIBC_2.2.5 |
| 0.01% | libsqlite3.so.0.8.6 | sqlite3_wal_checkpoint |
| 0.01% | libsqlite3.so.0.8.6 | sqlite3_str_value |
| 0.01% | libsqlite3.so.0.8.6 | sqlite3_vtab_config |
| 0.01% | libsqlite3.so.0.8.6 | sqlite3_extended_errcode |
| 0.01% | libsqlite3.so.0.8.6 | sqlite3_preupdate_old |
| 0.01% | _decimal.cpython-312-x86_64-linux-gnu.so | dec_addstatus |
| 0.01% | math.cpython-312-x86_64-linux-gnu.so | math_sqrt |
| 0.01% | _pickle.cpython-312-x86_64-linux-gnu.so | 0x0000000000005ba4 |
| 0.01% | _asyncio.cpython-312-x86_64-linux-gnu.so | TaskObj_clear |
| 0.01% | pyexpat.cpython-312-x86_64-linux-gnu.so | sip24_final |
| 0.01% | pyexpat.cpython-312-x86_64-linux-gnu.so | normal_getAtts |
| 0.01% | _struct.cpython-312-x86_64-linux-gnu.so | pack |
| 0.01% | math.cpython-312-x86_64-linux-gnu.so | math_cos |
| 0.01% | _elementtree.cpython-312-x86_64-linux-gnu.so | elementiter_next |
| 0.01% | _decimal.cpython-312-x86_64-linux-gnu.so | dec_mpd_qquantize |
| 0.01% | _decimal.cpython-312-x86_64-linux-gnu.so | mpd_qfinalize.part.0 |
| 0.01% | libmagic.so.1.0.0 | 0x000000000000f936 |
| 0.01% | _elementtree.cpython-312-x86_64-linux-gnu.so | expat_end_handler |
| 0.01% | _pickle.cpython-312-x86_64-linux-gnu.so | 0x0000000000005e50 |
| 0.01% | fastbinary.cpython-312-x86_64-linux-gnu.so | apache::thrift::py::ProtocolBase<apache::thrift::py::BinaryProtocol>::decodeValue |
| 0.01% | _heapq.cpython-312-x86_64-linux-gnu.so | siftup |
| 0.01% | _pickle.cpython-312-x86_64-linux-gnu.so | _Unpickler_New |
| 0.01% | libsqlite3.so.0.8.6 | sqlite3_step |
| 0.01% | _elementtree.cpython-312-x86_64-linux-gnu.so | treebuilder_handle_start |
| 0.01% | libsqlite3.so.0.8.6 | sqlite3_enable_shared_cache |
| 0.01% | _pickle.cpython-312-x86_64-linux-gnu.so | _Pickler_New.isra.0 |
| 0.01% | array.cpython-312-x86_64-linux-gnu.so | d_getitem |
| 0.01% | pyexpat.cpython-312-x86_64-linux-gnu.so | storeAtts |

### unknown

7.17% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 0.23% | python | r_object |
| 0.20% | python | update_one_slot |
| 0.18% | python | _PyErr_SetObject.part.0 |
| 0.13% | python | vgetargs1_impl |
| 0.12% | python | convertitem |
| 0.12% | python | PyCode_Addr2Line |
| 0.11% | python | _PyThreadState_PushFrame |
| 0.09% | python | _PyFunction_Vectorcall |
| 0.09% | python | intern_string_constants |
| 0.09% | python | PyType_GetModuleByDef |
| 0.09% | python | slot_tp_init |
| 0.09% | python | vgetargskeywords |
| 0.09% | python | _PyStaticCode_Fini |
| 0.08% | python | _PyPegen_is_memoized |
| 0.08% | python | _Py_CheckFunctionResult |
| 0.08% | python | gen_iternext |
| 0.08% | python | PyErr_Occurred |
| 0.08% | python | make_gen |
| 0.07% | python | take_gil |
| 0.06% | python | _PyThreadState_UncheckedGet |
| 0.06% | python | PyBytes_FromStringAndSize |
| 0.06% | python | func_clear |
| 0.06% | python | _PyIO_find_line_ending |
| 0.06% | python | memset@plt |
| 0.06% | python | PyErr_CheckSignals |
| 0.06% | python | getset_get |
| 0.06% | python | memcpy@plt |
| 0.06% | python | object_isinstance |
| 0.05% | python | PyBool_FromLong |
| 0.05% | python | compute_range_length |
| 0.05% | python | dictresize |
| 0.05% | python | deque_append |
| 0.05% | python | call_trace.part.0 |
| 0.05% | python | PyIter_Next |
| 0.05% | python | dictiter_iternextitem |
| 0.04% | python | bytes_subscript |
| 0.04% | python | PyErr_ExceptionMatches |
| 0.04% | python | _PyPegen_expect_token |
| 0.04% | python | super_getattro |
| 0.04% | python | PyDescr_IsData |
| 0.04% | python | async_gen_asend_iternext |
| 0.04% | python | min_max |
| 0.04% | python | _PyStack_UnpackDict |
| 0.04% | python | range_iter |
| 0.04% | python | method_vectorcall |
| 0.04% | python | enum_next |
| 0.04% | python | _PyErr_Restore |
| 0.04% | python | PyThread_get_thread_ident |
| 0.03% | python | delitem_common |
| 0.03% | python | tok_get |
| 0.03% | python | tok_nextc |
| 0.03% | python | _Py_HashBytes |
| 0.03% | python | split |
| 0.03% | python | sys_audit_tstate |
| 0.03% | python | _PyCfg_OptimizeCodeUnit |
| 0.03% | python | _PyFrame_Traverse |
| 0.03% | python | method_get |
| 0.03% | python | PyBuffer_Release |
| 0.03% | python | _PyPegen_update_memo |
| 0.03% | python | dequeiter_next |
| 0.03% | python | new_keys_object |
| 0.03% | python | method_vectorcall_VARARGS |
| 0.03% | python | async_gen_anext |
| 0.03% | python | _Py_MakeCoro |
| 0.02% | python | do_mkvalue |
| 0.02% | python | pysiphash |
| 0.02% | python | drop_gil |
| 0.02% | python | _Py_type_getattro_impl |
| 0.02% | python | PySys_Audit |
| 0.02% | python | _PyThreadState_Swap |
| 0.02% | python | PyContextVar_Get |
| 0.02% | python | vectorcall_method |
| 0.02% | python | cfunction_call |
| 0.02% | python | assemble |
| 0.02% | python | super_vectorcall |
| 0.02% | python | code_hash |
| 0.02% | python | tailmatch |
| 0.02% | python | slot_tp_richcompare |
| 0.02% | python | BaseException_clear |
| 0.02% | python | PyMember_GetOne |
| 0.02% | python | _PyEval_BuiltinsFromGlobals |
| 0.02% | python | _PyArg_UnpackKeywords |
| 0.02% | python | stringlib_bytes_join |
| 0.02% | python | range_subscript |
| 0.02% | python | method_vectorcall_FASTCALL_KEYWORDS_METHOD |
| 0.02% | python | primary_rule |
| 0.02% | python | bytearray_ass_subscript |
| 0.02% | python | _PyFrame_Copy |
| 0.02% | python | _PyGen_Finalize |
| 0.02% | python | builtin_getattr |
| 0.02% | python | _io_TextIOWrapper_write |
| 0.02% | python | term_rule |
| 0.02% | python | _PyErr_CreateException |
| 0.02% | python | map_next |
| 0.02% | python | PyBuffer_FillInfo |
| 0.02% | python | cfunction_vectorcall_O |
| 0.02% | python | _PyGen_SetStopIterationValue |
| 0.02% | python | clone_combined_dict_keys.isra.0 |
| 0.02% | python | PyArg_UnpackTuple |
| 0.02% | python | _PyGen_FetchStopIterationValue |
| 0.02% | python | cfunction_vectorcall_NOARGS |
| 0.02% | python | _PyArg_UnpackKeywordsWithVararg |
| 0.02% | python | _pystat_fromstructstat |
| 0.02% | python | object_richcompare |
| 0.02% | python | PyImport_ImportModuleLevelObject |
| 0.02% | python | _io_BytesIO_read |
| 0.02% | python | _PyTraceBack_FromFrame |
| 0.02% | python | context_run |
| 0.02% | python | PyArg_ParseTupleAndKeywords |
| 0.02% | python | _PyArena_Malloc |
| 0.02% | python | _PyArg_ParseTuple_SizeT |
| 0.02% | python | countformat |
| 0.02% | python | build_string |
| 0.02% | python | r_string (inlined) |
| 0.02% | python | supercheck |
| 0.01% | python | builtin_sum |
| 0.01% | python | super_init_without_args |
| 0.01% | python | dictiter_iternextvalue |
| 0.01% | python | cfunction_vectorcall_FASTCALL_KEYWORDS |
| 0.01% | python | PyIndex_Check |
| 0.01% | python | PyErr_GetRaisedException |
| 0.01% | [vdso] | 0x00000000000006c8 |
| 0.01% | python | range_vectorcall |
| 0.01% | python | module_getattro |
| 0.01% | python | build_indices_generic |
| 0.01% | python | _PyPegen_fill_token |
| 0.01% | python | PyErr_SetRaisedException |
| 0.01% | python | PyEval_SaveThread |
| 0.01% | python | PyIter_Send |
| 0.01% | python | member_get |
| 0.01% | python | method_vectorcall_VARARGS_KEYWORDS |
| 0.01% | python | slot_tp_descr_get |
| 0.01% | python | method_vectorcall_FASTCALL |
| 0.01% | python | _PyModule_ClearDict |
| 0.01% | python | pthread_self@plt |
| 0.01% | python | slot_tp_iternext |
| 0.01% | python | _Py_bytes_lower |
| 0.01% | python | slot_tp_hash |
| 0.01% | python | StopIteration_init |
| 0.01% | python | bounded_lru_cache_wrapper |
| 0.01% | python | vectorcall_maybe.constprop.0 |
| 0.01% | python | _PyPegen_insert_memo |
| 0.01% | python | _PyCode_Validate |
| 0.01% | python | builtin_id |
| 0.01% | python | analyze_descriptor |
| 0.01% | python | deque_popleft |
| 0.01% | python | object_recursive_isinstance |
| 0.01% | python | _PyCoro_GetAwaitableIter |
| 0.01% | python | builtin_hasattr |
| 0.01% | python | PyMember_SetOne |
| 0.01% | python | memcmp@plt |
| 0.01% | python | _PyArg_Parse_SizeT |
| 0.01% | python | PyErr_GivenExceptionMatches |
| 0.01% | python | _PyFrame_MakeAndSetFrameObject |
| 0.01% | python | any_find_slice |
| 0.01% | python | make_dict_from_instance_attributes |
| 0.01% | python | slot_mp_subscript |
| 0.01% | python | deque_clear.part.0 |
| 0.01% | python | method_vectorcall_NOARGS |
| 0.01% | python | pthread_mutex_unlock@plt |
| 0.01% | python | object_vacall |
| 0.01% | python | _io_open |
| 0.01% | python | _Py_convert_optional_to_ssize_t |
| 0.01% | python | _PyObjectDict_SetItem |
| 0.01% | python | bytes_concat |
| 0.01% | python | PyErr_Format |
| 0.01% | python | subtype_clear |
| 0.01% | python | PyIter_Check |
| 0.01% | python | object_init |
| 0.01% | python | cm_descr_get |
| 0.01% | python | shift_expr_rule |
| 0.01% | python | bytes_richcompare |
| 0.01% | python | PyTraceBack_Here |
| 0.01% | python | PySet_Add |
| 0.01% | python | strlen@plt |
| 0.01% | python | _Py_Specialize_LoadAttr |
| 0.01% | python | BaseException_init |
| 0.01% | python | write_bytes |
| 0.01% | python | inversion_rule |
| 0.01% | python | import_get_module |
| 0.01% | python | func_descr_get |
| 0.01% | python | _Py_Specialize_Call |
| 0.01% | python | sum_rule |
| 0.01% | python | unsafe_tuple_compare |
| 0.01% | python | cfunction_vectorcall_FASTCALL_KEYWORDS_METHOD |
| 0.01% | python | unsafe_long_compare |
| 0.01% | python | _PyBytes_Resize |
| 0.01% | python | slot_tp_iter |
| 0.01% | python | compiler_visit_expr1 |
| 0.01% | python | unsafe_latin_compare |
| 0.01% | python | trace_function_exit |
| 0.01% | python | stringio_iternext |
| 0.01% | python | _Py_slot_tp_getattr_hook |
| 0.01% | python | binary_op1 |
| 0.01% | python | dictiter_iternextkey |
| 0.01% | python | PyEval_RestoreThread |
| 0.01% | [vdso] | __vdso_clock_gettime |
| 0.01% | python | bitwise_xor_rule |
| 0.01% | python | PyException_GetTraceback |
| 0.01% | python | slot_sq_contains |
| 0.01% | python | PyGen_am_send |
| 0.01% | python | method_vectorcall_O |
| 0.01% | python | findchar |
| 0.01% | python | _Py_HashPointer |
| 0.01% | python | _io_FileIO___init__ |
| 0.01% | python | bytes_length |
| 0.01% | python | astfold_expr |
| 0.01% | python | remove_all_subclasses |
| 0.01% | python | update_slot |
| 0.01% | python | _PyTypes_Fini |
| 0.01% | python | os_stat |
| 0.01% | python | write_str |

### dynamic

5.49% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 0.50% | python | PyObject_GenericGetAttr |
| 0.31% | python | PyObject_IsTrue |
| 0.31% | python | PyObject_Hash |
| 0.30% | python | PyType_IsSubtype |
| 0.30% | python | PyObject_GetAttr |
| 0.25% | python | PyObject_RichCompare |
| 0.25% | python | _PyObject_GetMethod |
| 0.20% | python | _PyObject_MakeTpCall |
| 0.18% | python | PyObject_Vectorcall |
| 0.17% | python | PyNumber_AsSsize_t |
| 0.17% | python | PyObject_Malloc |
| 0.15% | python | _PyObject_GenericGetAttrWithDict |
| 0.15% | python | _PyObject_GetInstanceAttribute |
| 0.14% | python | PyObject_Free |
| 0.13% | python | PyObject_GetItem |
| 0.13% | python | PyObject_RichCompareBool |
| 0.11% | python | type_call |
| 0.10% | python | type_ready |
| 0.09% | python | _PyObject_Call_Prepend |
| 0.09% | python | _PyObject_LookupSpecial |
| 0.09% | python | _PyObject_LookupAttr |
| 0.08% | python | PyObject_GetIter |
| 0.07% | python | PySequence_Contains |
| 0.07% | python | _PyObject_FreeInstanceAttributes |
| 0.07% | python | PyObject_GenericSetAttr |
| 0.06% | python | PyObject_CallOneArg |
| 0.06% | python | PyObject_SetAttr |
| 0.06% | python | PyObject_IsInstance |
| 0.06% | python | PyObject_Call |
| 0.06% | python | _PyObject_InitializeDict |
| 0.05% | python | PyObject_SetItem |
| 0.05% | python | PyObject_Size |
| 0.05% | python | PyObject_ClearWeakRefs |
| 0.04% | python | PyNumber_Add |
| 0.04% | python | PyNumber_Multiply |
| 0.03% | python | PyObject_Str |
| 0.03% | python | PyNumber_And |
| 0.03% | python | PyNumber_TrueDivide |
| 0.03% | python | PyObject_VectorcallMethod |
| 0.02% | python | PyNumber_Subtract |
| 0.02% | python | PySequence_Fast |
| 0.02% | python | PyNumber_Remainder |
| 0.02% | python | PyNumber_FloorDivide |
| 0.02% | python | _PyObject_StoreInstanceAttribute |
| 0.02% | python | PySequence_Tuple |
| 0.02% | python | PyNumber_InPlaceAdd |
| 0.01% | python | _PyNumber_Index |
| 0.01% | python | PyNumber_Xor |
| 0.01% | python | _PyObject_CallFunctionVa |
| 0.01% | python | PyNumber_InPlaceTrueDivide |
| 0.01% | python | PyNumber_Rshift |
| 0.01% | python | PyNumber_Index |
| 0.01% | python | PyObject_IsSubclass |
| 0.01% | python | _PyObject_ClearManagedDict |
| 0.01% | python | PyObject_DelItem |
| 0.01% | python | PyObject_LengthHint |
| 0.01% | python | PyObject_GetBuffer |
| 0.01% | python | PyNumber_Negative |
| 0.01% | python | _PyObject_GenericTryGetAttr |
| 0.01% | python | type_mro_modified |
| 0.01% | python | _PyNumber_PowerNoMod |
| 0.01% | python | PyNumber_Long |

### lookup

4.53% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 2.07% | python | unicodekeys_lookup_unicode |
| 1.31% | python | _Py_dict_lookup |
| 0.87% | python | _PyType_Lookup |
| 0.17% | python | find_name_in_mro |
| 0.11% | python | _Py_type_getattro |

### int

4.07% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 0.55% | python | k_mul |
| 0.49% | python | x_divrem |
| 0.44% | python | _PyLong_Add |
| 0.31% | python | PyLong_FromLong |
| 0.23% | python | long_hash |
| 0.17% | python | x_add |
| 0.16% | python | _PyLong_Subtract |
| 0.16% | python | PyLong_AsLongAndOverflow |
| 0.15% | python | long_to_decimal_string_internal |
| 0.15% | python | PyLong_FromSsize_t |
| 0.13% | python | PyLong_AsSsize_t |
| 0.12% | python | long_richcompare |
| 0.11% | python | long_bitwise |
| 0.11% | python | PyLong_FromString |
| 0.10% | python | x_sub |
| 0.06% | python | long_rshift1 |
| 0.06% | python | long_and |
| 0.06% | python | _PyLong_Multiply |
| 0.05% | python | long_div |
| 0.04% | python | PyLong_AsDouble |
| 0.04% | python | PyLong_FromVoidPtr |
| 0.04% | python | PyLong_AsLong |
| 0.04% | python | l_mod |
| 0.03% | python | long_add |
| 0.03% | python | long_mul |
| 0.03% | python | long_rshift |
| 0.02% | python | PyLong_FromUnsignedLong |
| 0.02% | python | long_lshift1 |
| 0.02% | python | long_xor |
| 0.01% | python | long_sub |
| 0.01% | python | long_lshift |
| 0.01% | python | long_neg |
| 0.01% | python | PyLong_FromLongLong |
| 0.01% | python | long_float |
| 0.01% | python | long_to_decimal_string |
| 0.01% | python | _PyLong_GCD |
| 0.01% | python | _PyLong_AsInt |
| 0.01% | python | long_mod |
| 0.01% | python | long_bool |
| 0.01% | python | _PyLong_Frexp |

### kernel

3.74% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 0.54% | [kernel.kallsyms] | copy_user_enhanced_fast_string |
| 0.22% | [kernel.kallsyms] | clear_page_erms |
| 0.11% | [kernel.kallsyms] | native_irq_return_iret |
| 0.10% | [kernel.kallsyms] | __d_lookup_rcu |
| 0.09% | [kernel.kallsyms] | rmqueue |
| 0.08% | [kernel.kallsyms] | sync_regs |
| 0.08% | [kernel.kallsyms] | zap_pte_range.isra.0 |
| 0.06% | [kernel.kallsyms] | _raw_spin_lock |
| 0.05% | [kernel.kallsyms] | copy_pte_range.isra.0 |
| 0.05% | [kernel.kallsyms] | free_pcppages_bulk |
| 0.04% | [kernel.kallsyms] | __handle_mm_fault |
| 0.04% | [kernel.kallsyms] | memset_erms |
| 0.04% | [kernel.kallsyms] | release_pages |
| 0.03% | [kernel.kallsyms] | __ext4fs_dirhash |
| 0.03% | [kernel.kallsyms] | link_path_walk.part.0 |
| 0.03% | [kernel.kallsyms] | page_remove_rmap |
| 0.03% | [kernel.kallsyms] | kmem_cache_alloc |
| 0.03% | [kernel.kallsyms] | try_charge |
| 0.03% | [kernel.kallsyms] | copy_page |
| 0.03% | [kernel.kallsyms] | ext4_htree_store_dirent |
| 0.03% | [kernel.kallsyms] | syscall_return_via_sysret |
| 0.03% | [kernel.kallsyms] | __pagevec_lru_add_fn |
| 0.02% | [kernel.kallsyms] | entry_SYSCALL_64 |
| 0.02% | [kernel.kallsyms] | get_mem_cgroup_from_mm |
| 0.02% | [kernel.kallsyms] | find_get_entry |
| 0.02% | [kernel.kallsyms] | mem_cgroup_throttle_swaprate |
| 0.02% | [kernel.kallsyms] | strncpy_from_user |
| 0.02% | [kernel.kallsyms] | filemap_map_pages |
| 0.02% | [kernel.kallsyms] | handle_mm_fault |
| 0.02% | [kernel.kallsyms] | filldir64 |
| 0.02% | [kernel.kallsyms] | lookup_fast |
| 0.02% | [kernel.kallsyms] | kmem_cache_free |
| 0.02% | [kernel.kallsyms] | do_syscall_64 |
| 0.02% | [kernel.kallsyms] | mem_cgroup_try_charge |
| 0.02% | [kernel.kallsyms] | __alloc_pages_nodemask |
| 0.02% | [kernel.kallsyms] | memcg_kmem_get_cache |
| 0.02% | [kernel.kallsyms] | __virt_addr_valid |
| 0.02% | [kernel.kallsyms] | __slab_free |
| 0.02% | [kernel.kallsyms] | inode_permission |
| 0.02% | [kernel.kallsyms] | find_vma |
| 0.02% | [kernel.kallsyms] | do_user_addr_fault |
| 0.01% | [kernel.kallsyms] | str2hashbuf_signed |
| 0.01% | [kernel.kallsyms] | generic_permission |
| 0.01% | [kernel.kallsyms] | do_wp_page |
| 0.01% | [kernel.kallsyms] | __fget_light |
| 0.01% | [kernel.kallsyms] | kfree |
| 0.01% | [kernel.kallsyms] | page_fault |
| 0.01% | [kernel.kallsyms] | prep_new_page |
| 0.01% | [kernel.kallsyms] | walk_component |
| 0.01% | [kernel.kallsyms] | ext4_getattr |
| 0.01% | [kernel.kallsyms] | vmacache_find |
| 0.01% | [kernel.kallsyms] | perf_iterate_ctx |
| 0.01% | [kernel.kallsyms] | __count_memcg_events |
| 0.01% | [kernel.kallsyms] | security_inode_getattr |
| 0.01% | [kernel.kallsyms] | rb_insert_color |
| 0.01% | [kernel.kallsyms] | __mod_lruvec_state |
| 0.01% | [kernel.kallsyms] | _raw_spin_lock_irqsave |
| 0.01% | [kernel.kallsyms] | do_anonymous_page |
| 0.01% | [kernel.kallsyms] | memcpy_erms |
| 0.01% | [kernel.kallsyms] | rb_next |
| 0.01% | [kernel.kallsyms] | free_pages_and_swap_cache |
| 0.01% | [kernel.kallsyms] | get_page_from_freelist |
| 0.01% | [kernel.kallsyms] | error_entry |
| 0.01% | [kernel.kallsyms] | __mod_memcg_state |
| 0.01% | [kernel.kallsyms] | ___slab_alloc |
| 0.01% | [kernel.kallsyms] | set_root |
| 0.01% | [kernel.kallsyms] | free_unref_page_prepare.part.0 |
| 0.01% | [kernel.kallsyms] | _cond_resched |
| 0.01% | [kernel.kallsyms] | entry_SYSCALL_64_after_hwframe |
| 0.01% | [kernel.kallsyms] | tcp_sendmsg_locked |
| 0.01% | [kernel.kallsyms] | xas_load |
| 0.01% | [kernel.kallsyms] | __kmalloc |
| 0.01% | [kernel.kallsyms] | __check_object_size |
| 0.01% | [kernel.kallsyms] | up_read |
| 0.01% | [kernel.kallsyms] | vm_normal_page |
| 0.01% | [kernel.kallsyms] | generic_file_buffered_read |
| 0.01% | [kernel.kallsyms] | free_unref_page_commit |
| 0.01% | [kernel.kallsyms] | memchr |
| 0.01% | [kernel.kallsyms] | __follow_mount_rcu.isra.0 |
| 0.01% | [kernel.kallsyms] | pagevec_lru_move_fn |
| 0.01% | [kernel.kallsyms] | down_read_trylock |
| 0.01% | [kernel.kallsyms] | fpregs_assert_state_consistent |
| 0.01% | [kernel.kallsyms] | swapgs_restore_regs_and_return_to_usermode |
| 0.01% | [kernel.kallsyms] | security_inode_permission |
| 0.01% | [kernel.kallsyms] | __vma_adjust |
| 0.01% | [kernel.kallsyms] | fsnotify |
| 0.01% | [kernel.kallsyms] | __lru_cache_add |

### str

2.76% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 0.49% | python | siphash13 |
| 0.16% | python | _PyUnicode_JoinArray.part.0 |
| 0.16% | python | ascii_decode |
| 0.15% | python | unicode_decode_utf8 |
| 0.14% | python | _copy_characters.part.0.constprop.0 |
| 0.13% | python | replace |
| 0.10% | python | resize_compact |
| 0.10% | python | _PyUnicode_FromUCS1.part.0 |
| 0.09% | python | PyUnicode_InternInPlace |
| 0.08% | python | PyUnicode_FromFormatV |
| 0.07% | python | PyUnicode_Substring |
| 0.07% | python | _PyUnicode_FromASCII |
| 0.07% | python | _PyUnicodeWriter_WriteStr |
| 0.06% | python | PyUnicode_Format |
| 0.05% | python | PyUnicode_AsUTF8AndSize |
| 0.05% | python | _PyUnicode_FromUCS4.part.0 |
| 0.05% | python | unicode_hash |
| 0.05% | python | PyUnicode_Contains |
| 0.04% | python | PyUnicode_RichCompare |
| 0.04% | python | _PyUnicodeWriter_PrepareInternal |
| 0.03% | python | _PyUnicode_FromASCII (inlined) |
| 0.03% | python | PyUnicode_AsUCS4 |
| 0.03% | python | unicode_replace |
| 0.03% | python | _PyUnicode_Equal |
| 0.02% | python | unicode_subscript |
| 0.02% | python | PyUnicode_Concat |
| 0.02% | python | unicode_getitem |
| 0.02% | python | _PyUnicodeWriter_WriteASCIIString |
| 0.02% | python | unicode_rstrip |
| 0.02% | python | _PyUnicodeWriter_Finish |
| 0.02% | python | PyUnicode_Decode.part.0 |
| 0.02% | python | PyUnicode_AsEncodedString.part.0 |
| 0.02% | python | unicode_startswith |
| 0.01% | python | _PyUnicodeWriter_WriteSubstring.part.0 |
| 0.01% | python | unicode_lower |
| 0.01% | python | PyUnicode_FromWideChar |
| 0.01% | python | unicode_encode_utf8 |
| 0.01% | python | PyUnicode_FromKindAndData |
| 0.01% | python | _PyUnicode_IsAlpha |
| 0.01% | python | unicode_join |
| 0.01% | python | _PyUnicodeWriter_Init |
| 0.01% | python | unicode_length |
| 0.01% | python | _PyUnicode_ToLowercase |
| 0.01% | python | _PyUnicode_TranslateCharmap |
| 0.01% | python | PyUnicode_Splitlines |
| 0.01% | python | PyUnicode_FromEncodedObject |
| 0.01% | python | unicode_encode |
| 0.01% | python | unicode_endswith |

### libc

2.69% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 1.75% | libc-2.31.so | __nss_database_lookup |
| 0.54% | libc-2.31.so | pthread_attr_setschedparam |
| 0.13% | libc-2.31.so | malloc |
| 0.05% | libc-2.31.so | free |
| 0.02% | libc-2.31.so | pthread_self |
| 0.02% | libc-2.31.so | __gconv_get_alias_db |
| 0.02% | libc-2.31.so | psiginfo |
| 0.02% | libc-2.31.so | __libc_realloc |
| 0.01% | libc-2.31.so | wcsrtombs |
| 0.01% | libc-2.31.so | clock_gettime |

### dict

2.48% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 0.44% | python | insertdict |
| 0.28% | python | PyDict_Next |
| 0.24% | python | PyDict_GetItemWithError |
| 0.23% | python | free_keys_object |
| 0.16% | python | insert_to_emptydict |
| 0.15% | python | _PyDict_GetItem_KnownHash |
| 0.15% | python | PyDict_SetDefault |
| 0.14% | python | find_empty_slot |
| 0.11% | python | build_indices_unicode |
| 0.10% | python | dict_get |
| 0.07% | python | PyDict_SetItem |
| 0.07% | python | _PyDict_FromItems |
| 0.03% | python | dict_ass_sub |
| 0.03% | python | dict_merge |
| 0.03% | python | dict_subscript |
| 0.03% | python | _PyDict_SetItem_Take2 |
| 0.03% | python | PyDict_Contains |
| 0.02% | python | PyDict_DelItem |
| 0.02% | python | _PyDict_Next.part.0 |
| 0.02% | python | PyDict_GetItem |
| 0.02% | python | _PyDict_LoadGlobal |
| 0.01% | python | _PyDict_DelItem_KnownHash |
| 0.01% | python | dict_pop |

### list

1.04% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 0.24% | python | list_ass_slice |
| 0.13% | python | list_subscript |
| 0.08% | python | list_slice.isra.0 |
| 0.07% | python | list_extend |
| 0.06% | python | listiter_next |
| 0.05% | python | PyList_Append |
| 0.05% | python | list_sort_impl |
| 0.05% | python | list_iter |
| 0.05% | python | list_append |
| 0.04% | python | list_contains |
| 0.04% | python | list_concat |
| 0.03% | python | list_ass_subscript |
| 0.02% | python | _PyList_AppendTakeRefListResize |
| 0.02% | python | list_pop |
| 0.02% | python | _PyList_FromArraySteal |
| 0.02% | python | list_insert |
| 0.01% | python | list_length |
| 0.01% | python | PyList_Size |
| 0.01% | python | list_item |

### tuple

1.02% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 0.41% | python | tuplehash |
| 0.17% | python | _PyTuple_FromArray |
| 0.14% | python | _PyTuple_FromArraySteal |
| 0.10% | python | tupletraverse |
| 0.04% | python | tuplerichcompare |
| 0.03% | python | PyTuple_Pack |
| 0.02% | python | tuple_iter |
| 0.02% | python | tupleiter_next |
| 0.02% | python | _PyTuple_ClearFreeList |
| 0.02% | python | PyTuple_Size |
| 0.01% | python | PyTuple_GetSlice |
| 0.01% | python | tuplesubscript |

### set

0.71% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 0.20% | python | set_lookkey |
| 0.11% | python | set_issubset |
| 0.11% | python | set_add_entry |
| 0.10% | python | setiter_iternext |
| 0.05% | python | set_difference |
| 0.03% | python | set_table_resize |
| 0.03% | python | set_update_internal |
| 0.02% | python | set_contains |
| 0.01% | python | set_intersection |
| 0.01% | python | set_richcompare |

### float

0.45% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 0.23% | python | PyFloat_FromDouble |
| 0.09% | python | float_div |
| 0.03% | python | float_richcompare |
| 0.03% | python | float_pow |
| 0.02% | python | float_sub |
| 0.02% | python | float_mul |
| 0.01% | python | PyFloat_AsDouble.part.0 |
| 0.01% | python | PyFloat_AsDouble |
| 0.01% | python | float_rem |

### slice

0.44% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 0.22% | python | PySlice_AdjustIndices |
| 0.08% | python | _PyBuildSlice_ConsumeRefs |
| 0.07% | python | _PyEval_SliceIndex |
| 0.06% | python | PySlice_Unpack |
| 0.02% | python | _PySlice_GetLongIndices |
