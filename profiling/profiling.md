
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
| 1.62% | `python` | `tupledealloc` | unknown |
| 1.46% | `python` | `_PyType_Lookup` | lookup |
| 1.34% | `python` | `visit_decref` | gc |
| 1.18% | `python` | `PyObject_GenericGetAttr` | dynamic |
| 1.18% | `python` | `_PyFrame_ClearExceptCode` | interpreter |

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
| 1.15% | `python` | `tupledealloc` | unknown |
| 1.00% | `python` | `_PyType_Lookup` | lookup |

## async_generators

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 22.58% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 10.39% | `python` | `_PyErr_SetObject.part.0` | unknown |
| 3.11% | `python` | `_PyObject_Free` | memory |
| 3.01% | `python` | `async_gen_asend_iternext` | unknown |
| 2.58% | `python` | `_PyObject_Malloc` | memory |
| 2.54% | `python` | `PyType_GenericAlloc` | memory |
| 2.38% | `python` | `tupledealloc` | unknown |
| 2.22% | `python` | `gc_collect_main` | gc |
| 2.01% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.91% | `python` | `async_gen_anext` | unknown |
| 1.85% | `python` | `PyErr_ExceptionMatches` | unknown |
| 1.64% | `python` | `_Py_NewReference` | unknown |
| 1.55% | `python` | `_PyObject_MakeTpCall` | dynamic |
| 1.55% | `python` | `advance` | unknown |
| 1.52% | `python` | `_PyTuple_FromArray` | unknown |
| 1.35% | `python` | `async_gen_asend_dealloc` | memory |
| 1.26% | `python` | `async_gen_wrapped_val_dealloc` | memory |
| 1.25% | `python` | `PyObject_GC_UnTrack` | dynamic |
| 1.23% | `python` | `_PyErr_Restore` | unknown |
| 1.22% | `python` | `_PyAsyncGenValueWrapperNew` | unknown |
| 1.21% | `python` | `_PyGen_SetStopIterationValue` | unknown |
| 1.17% | `python` | `_PyGen_FetchStopIterationValue` | unknown |
| 1.09% | `python` | `PyObject_CallOneArg` | dynamic |
| 1.06% | `python` | `tuple_alloc` | memory |
| 1.04% | `python` | `type_call` | dynamic |
| 1.02% | `python` | `StopIteration_dealloc` | memory |

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

## async_tree_cpu_io_mixed

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 18.84% | `python` | `gc_collect_main` | gc |
| 16.08% | `python` | `k_mul` | unknown |
| 14.60% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 4.84% | `python` | `visit_reachable` | gc |
| 4.60% | `python` | `visit_decref` | gc |
| 2.79% | `python` | `_PyObject_Malloc` | memory |
| 2.22% | `python` | `_PyObject_Free` | memory |
| 1.31% | `python` | `PyErr_CheckSignals` | unknown |
| 1.22% | `math.cpython-312-x86_64-linux-gnu.so` | `factorial_partial_product` | library |

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

## asyncio_tcp

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 32.63% | `[kernel.kallsyms]` | `copy_user_enhanced_fast_string` | kernel |
| 16.73% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 9.28% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 8.16% | `[kernel.kallsyms]` | `clear_page_erms` | kernel |

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
| 1.65% | `python` | `_PyUnicode_JoinArray.part.0` | unknown |
| 1.44% | `python` | `gc_collect_main` | gc |
| 1.28% | `python` | `long_to_decimal_string_internal` | unknown |
| 1.22% | `python` | `PyUnicode_Format` | unknown |
| 1.12% | `python` | `_copy_characters.part.0.constprop.0` | unknown |
| 1.03% | `python` | `_sre_SRE_Pattern_search` | library |

## chaos

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 48.14% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 2.34% | `python` | `_PyLong_Subtract` | unknown |
| 1.98% | `python` | `_PyLong_Add` | unknown |
| 1.82% | `python` | `_PyObject_Free` | memory |
| 1.79% | `python` | `PyType_IsSubtype` | unknown |
| 1.58% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.27% | `python` | `tupledealloc` | unknown |
| 1.13% | `python` | `PyFloat_FromDouble` | unknown |
| 1.04% | `python` | `initialize_locals` | interpreter |
| 1.02% | `python` | `_PyObject_Malloc (inlined)` | memory |
| 1.00% | `libc-2.31.so` | `__nss_database_lookup` | libc |

## comprehensions

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 32.34% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 4.48% | `python` | `_Py_dict_lookup` | lookup |
| 3.68% | `python` | `_PyObject_Malloc` | memory |
| 2.57% | `python` | `_PyObject_Free` | memory |
| 2.25% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 2.17% | `python` | `advance` | unknown |
| 1.68% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.58% | `python` | `PyFunction_NewWithQualName` | unknown |
| 1.35% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.21% | `python` | `dict_get` | unknown |
| 1.10% | `python` | `list_dealloc` | memory |
| 1.10% | `python` | `PyObject_RichCompare` | dynamic |
| 1.05% | `python` | `gc_collect_main` | gc |
| 1.00% | `python` | `_PyObject_Realloc` | dynamic |

## concurrent_imap

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 14.02% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 9.82% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 2.77% | `python` | `_PyObject_Free` | memory |
| 2.38% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 1.76% | `python` | `gc_collect_main` | gc |
| 1.64% | `python` | `tupledealloc` | unknown |
| 1.49% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.32% | `python` | `_PyObject_Malloc` | memory |
| 1.31% | `python` | `initialize_locals` | interpreter |
| 1.21% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.14% | `python` | `_PyEvalFramePushAndInit` | unknown |
| 1.08% | `python` | `_Py_dict_lookup` | lookup |
| 1.03% | `python` | `visit_decref` | gc |

## coroutines

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 45.05% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 5.99% | `python` | `gen_dealloc` | memory |
| 3.67% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 3.29% | `python` | `_PyObject_GC_NewVar` | dynamic |
| 3.20% | `python` | `make_gen` | unknown |
| 3.19% | `python` | `_PyLong_Subtract` | unknown |
| 2.69% | `python` | `_PyLong_Add` | unknown |
| 2.67% | `python` | `_PyObject_Free` | memory |
| 2.12% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.85% | `python` | `_PyObject_Malloc (inlined)` | memory |
| 1.79% | `python` | `PyObject_CallFinalizerFromDealloc` | memory |
| 1.40% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 1.34% | `python` | `gc_collect_main` | gc |
| 1.23% | `python` | `PyObject_GC_Del` | dynamic |
| 1.10% | `python` | `_Py_MakeCoro` | unknown |

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
| 2.26% | `python` | `siphash13` | unknown |
| 1.95% | `python` | `_PyType_Lookup` | lookup |
| 1.68% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.57% | `python` | `gc_collect_main` | gc |
| 1.35% | `python` | `PyDict_GetItem` | unknown |
| 1.34% | `python` | `PyLong_FromLong` | unknown |
| 1.25% | `python` | `initialize_locals` | interpreter |
| 1.24% | `python` | `set_add_entry` | unknown |
| 1.13% | `python` | `long_richcompare` | unknown |
| 1.00% | `python` | `PyObject_GenericGetAttr` | dynamic |

## crypto_pyaes

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 37.06% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 6.90% | `python` | `long_bitwise` | unknown |
| 4.79% | `python` | `_PyObject_Free` | memory |
| 3.87% | `python` | `long_rshift1` | unknown |
| 3.83% | `python` | `_PyObject_Malloc` | memory |
| 2.69% | `python` | `PyObject_GenericGetAttr` | dynamic |
| 2.58% | `python` | `l_mod` | unknown |
| 2.51% | `python` | `long_and` | unknown |
| 2.35% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 1.72% | `python` | `PyLong_FromLong` | unknown |
| 1.53% | `python` | `_PyLong_Add` | unknown |
| 1.52% | `python` | `long_rshift` | unknown |
| 1.36% | `python` | `PyObject_GetAttr` | dynamic |
| 1.32% | `python` | `_PyType_Lookup` | lookup |
| 1.17% | `python` | `PyNumber_And` | dynamic |
| 1.14% | `python` | `long_xor` | unknown |
| 1.10% | `python` | `_PyObject_GetInstanceAttribute` | dynamic |
| 1.04% | `python` | `_Py_NewReference` | unknown |

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
| 1.20% | `python` | `tupledealloc` | unknown |

## deepcopy

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 46.42% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 5.92% | `python` | `_Py_dict_lookup` | lookup |
| 3.04% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 2.89% | `python` | `_PyObject_Free` | memory |
| 2.37% | `python` | `_PyObject_Malloc` | memory |
| 2.03% | `python` | `dict_get` | unknown |
| 1.50% | `python` | `PyLong_FromVoidPtr` | unknown |
| 1.23% | `python` | `unicodekeys_lookup_unicode` | lookup |

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
| 1.00% | `python` | `advance` | unknown |

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

## fannkuch

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 37.68% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 8.34% | `python` | `PySlice_AdjustIndices` | unknown |
| 5.61% | `python` | `list_subscript` | unknown |
| 5.19% | `python` | `list_ass_slice` | unknown |
| 4.58% | `python` | `_PyLong_Add` | unknown |
| 3.63% | `python` | `list_dealloc` | memory |
| 3.12% | `python` | `slice_dealloc` | memory |
| 2.45% | `python` | `PyNumber_AsSsize_t` | dynamic |
| 2.30% | `python` | `_PyEval_SliceIndex` | unknown |
| 2.07% | `python` | `PySlice_Unpack` | unknown |
| 1.60% | `python` | `PySlice_New` | unknown |
| 1.58% | `python` | `list_ass_subscript` | unknown |
| 1.57% | `python` | `_PyBuildSlice_ConsumeRefs` | unknown |
| 1.56% | `python` | `_PyObject_Free` | memory |
| 1.38% | `python` | `_PyObject_Malloc` | memory |
| 1.34% | `python` | `_Py_NewReference` | unknown |
| 1.28% | `python` | `PyLong_AsSsize_t` | unknown |
| 1.11% | `python` | `list_insert` | unknown |
| 1.09% | `python` | `PyObject_IsTrue` | dynamic |

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
| 2.03% | `python` | `PyFloat_FromDouble` | unknown |
| 1.98% | `python` | `float_div` | unknown |
| 1.82% | `python` | `subtype_dealloc` | memory |
| 1.62% | `python` | `float_dealloc` | memory |
| 1.25% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.00% | `python` | `PyType_IsSubtype` | unknown |
| 1.00% | `python` | `_Py_NewReference` | unknown |

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

## gc_traversal

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 29.16% | `python` | `visit_reachable` | gc |
| 21.25% | `python` | `visit_decref` | gc |
| 15.38% | `python` | `list_traverse` | gc |
| 12.97% | `python` | `gc_collect_main` | gc |
| 3.73% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 2.24% | `python` | `dict_traverse` | gc |

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
| 1.18% | `python` | `_PyEvalFramePushAndInit` | unknown |

## genshi

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 46.09% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 2.96% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 2.49% | `python` | `_PyObject_Free` | memory |
| 2.40% | `python` | `_PyObject_Malloc` | memory |
| 2.35% | `python` | `_Py_dict_lookup` | lookup |
| 1.43% | `python` | `insertdict` | unknown |
| 1.36% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.30% | `python` | `_PyType_Lookup` | lookup |
| 1.23% | `python` | `insert_to_emptydict` | unknown |
| 1.13% | `python` | `tupledealloc` | unknown |
| 1.05% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.00% | `python` | `PyObject_IsTrue` | dynamic |

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
| 1.20% | `python` | `tupledealloc` | unknown |

## hexiom

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 56.30% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 2.38% | `python` | `long_richcompare` | unknown |
| 2.34% | `python` | `list_contains` | unknown |
| 2.32% | `python` | `PyObject_RichCompare` | dynamic |
| 2.17% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.56% | `python` | `PyObject_RichCompareBool` | dynamic |
| 1.54% | `python` | `_PyObject_Free` | memory |
| 1.36% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 1.33% | `python` | `PyLong_FromSsize_t` | unknown |
| 1.23% | `python` | `gen_iternext` | unknown |
| 1.23% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.22% | `python` | `_PyObject_Malloc` | memory |
| 1.11% | `python` | `gc_collect_main` | gc |

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

## json

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 12.00% | `_json.cpython-312-x86_64-linux-gnu.so` | `scanstring_unicode` | library |
| 7.81% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 6.49% | `_json.cpython-312-x86_64-linux-gnu.so` | `scan_once_unicode` | library |
| 6.01% | `python` | `siphash13` | unknown |
| 5.14% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 5.06% | `python` | `_PyObject_Malloc` | memory |
| 3.73% | `python` | `PyDict_SetDefault` | unknown |
| 3.63% | `python` | `_PyObject_Free` | memory |
| 3.03% | `python` | `PyLong_FromString` | unknown |
| 2.64% | `python` | `insertdict` | unknown |
| 2.45% | `python` | `_Py_dict_lookup` | lookup |
| 2.43% | `libc-2.31.so` | `pthread_attr_setschedparam` | libc |
| 2.32% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 2.04% | `python` | `_PyUnicode_FromASCII (inlined)` | unknown |
| 1.84% | `python` | `free_keys_object` | unknown |
| 1.61% | `python` | `find_empty_slot` | unknown |
| 1.57% | `python` | `build_indices_unicode` | unknown |
| 1.47% | `python` | `PyUnicode_Substring` | unknown |

## json_dumps

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 13.07% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 8.34% | `_json.cpython-312-x86_64-linux-gnu.so` | `py_encode_basestring_ascii` | library |
| 4.86% | `python` | `_PyObject_Malloc` | memory |
| 4.67% | `python` | `_PyObject_Free` | memory |
| 4.36% | `python` | `_copy_characters.part.0.constprop.0` | unknown |
| 3.79% | `python` | `_PyUnicodeWriter_WriteStr` | unknown |
| 3.25% | `_json.cpython-312-x86_64-linux-gnu.so` | `encoder_listencode_obj` | library |
| 2.89% | `python` | `_Py_dict_lookup` | lookup |
| 2.86% | `python` | `resize_compact` | unknown |
| 2.86% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 2.57% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 2.52% | `python` | `PyUnicode_New` | unknown |
| 2.47% | `_json.cpython-312-x86_64-linux-gnu.so` | `encoder_encode_key_value` | library |
| 1.65% | `python` | `PyDict_Next` | unknown |
| 1.62% | `python` | `convertitem` | unknown |
| 1.56% | `python` | `vgetargskeywords` | unknown |
| 1.55% | `python` | `_PyObject_Realloc` | dynamic |
| 1.28% | `python` | `tupledealloc` | unknown |
| 1.11% | `python` | `_PyUnicodeWriter_PrepareInternal` | unknown |
| 1.07% | `python` | `initialize_locals` | interpreter |

## json_loads

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 13.10% | `_json.cpython-312-x86_64-linux-gnu.so` | `scanstring_unicode` | library |
| 7.15% | `_json.cpython-312-x86_64-linux-gnu.so` | `scan_once_unicode` | library |
| 6.98% | `python` | `siphash13` | unknown |
| 6.74% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 5.60% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 4.95% | `python` | `_PyObject_Malloc` | memory |
| 3.58% | `python` | `_PyObject_Free` | memory |
| 3.40% | `python` | `_Py_dict_lookup` | lookup |
| 3.20% | `python` | `insertdict` | unknown |
| 3.11% | `python` | `PyLong_FromString` | unknown |
| 3.06% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 3.04% | `python` | `_PyUnicode_FromASCII` | unknown |
| 2.81% | `python` | `PyDict_SetDefault` | unknown |
| 2.30% | `python` | `PyUnicode_Substring` | unknown |
| 1.30% | `python` | `free_keys_object` | unknown |
| 1.30% | `python` | `find_empty_slot` | unknown |
| 1.05% | `libc-2.31.so` | `pthread_attr_setschedparam` | libc |
| 1.03% | `python` | `PyDict_SetItem` | unknown |
| 1.02% | `python` | `build_indices_unicode` | unknown |

## logging

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 46.86% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 3.54% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 2.00% | `python` | `_Py_dict_lookup` | lookup |
| 1.93% | `python` | `initialize_locals` | interpreter |
| 1.78% | `python` | `dict_dealloc` | memory |
| 1.78% | `python` | `advance` | unknown |
| 1.71% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.62% | `python` | `_PyObject_Malloc (inlined)` | memory |
| 1.56% | `python` | `_PyObject_Free` | memory |
| 1.30% | `python` | `_PyEvalFramePushAndInit` | unknown |
| 1.18% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 1.17% | `python` | `PyObject_GenericGetAttr` | dynamic |

## mako

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 37.34% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 8.02% | `python` | `replace` | unknown |
| 5.03% | `python` | `long_to_decimal_string_internal` | unknown |
| 3.93% | `python` | `_PyUnicode_JoinArray.part.0` | unknown |
| 3.28% | `python` | `_PyObject_Free` | memory |
| 2.82% | `python` | `deque_append` | unknown |
| 2.48% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.89% | `python` | `_PyObject_Malloc` | memory |
| 1.88% | `python` | `unicode_replace` | unknown |
| 1.83% | `python` | `dequeiter_next` | unknown |
| 1.41% | `python` | `list_extend` | unknown |
| 1.16% | `python` | `PyUnicode_New` | unknown |
| 1.15% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.06% | `python` | `gc_collect_main` | gc |
| 1.00% | `python` | `sre_ucs2_charset.isra.0` | library |

## mdp

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 28.11% | `python` | `tuplehash` | unknown |
| 15.59% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 13.94% | `python` | `PyObject_Hash` | dynamic |
| 11.14% | `python` | `long_hash` | unknown |
| 5.99% | `python` | `_Py_dict_lookup` | lookup |
| 2.04% | `python` | `tuplerichcompare` | unknown |
| 1.41% | `python` | `PyObject_RichCompareBool` | dynamic |
| 1.33% | `python` | `PyObject_RichCompare` | dynamic |
| 1.16% | `python` | `_PyObject_Free` | memory |
| 1.15% | `python` | `dict_subscript` | unknown |
| 1.05% | `python` | `_PyObject_Malloc` | memory |

## meteor_contest

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 21.41% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 8.21% | `python` | `set_issubset` | unknown |
| 7.68% | `python` | `set_lookkey` | unknown |
| 5.81% | `python` | `setiter_iternext` | unknown |
| 3.49% | `python` | `set_difference` | unknown |
| 3.26% | `python` | `set_dealloc` | memory |
| 2.37% | `python` | `PyObject_RichCompare` | dynamic |
| 2.07% | `python` | `_PyObject_Free` | memory |
| 1.92% | `python` | `set_add_entry` | unknown |
| 1.90% | `python` | `list_dealloc` | memory |
| 1.81% | `python` | `_PyObject_Malloc` | memory |
| 1.52% | `python` | `long_richcompare` | unknown |
| 1.44% | `python` | `min_max` | unknown |
| 1.43% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.37% | `python` | `list_slice.isra.0` | unknown |
| 1.34% | `python` | `gc_collect_main` | gc |
| 1.12% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 1.04% | `python` | `PyIter_Next` | unknown |

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

## nbody

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 68.08% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 6.42% | `python` | `PyFloat_FromDouble` | unknown |
| 4.31% | `libm-2.31.so` | `f64xsubf128` | library |
| 2.40% | `python` | `float_dealloc` | memory |
| 2.26% | `python` | `_Py_NewReference` | unknown |
| 1.30% | `python` | `float_pow` | unknown |

## nqueens

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 37.32% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 4.69% | `python` | `_PyObject_Malloc (inlined)` | memory |
| 3.50% | `python` | `_PyObject_Free` | memory |
| 2.13% | `python` | `gen_iternext` | unknown |
| 2.11% | `python` | `set_add_entry` | unknown |
| 1.92% | `python` | `PySlice_AdjustIndices` | unknown |
| 1.70% | `python` | `_PyLong_Add` | unknown |
| 1.62% | `python` | `list_dealloc` | memory |
| 1.49% | `python` | `tupledealloc` | unknown |
| 1.34% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.33% | `python` | `set_dealloc` | memory |
| 1.31% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 1.11% | `python` | `PyLong_FromLong` | unknown |

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
| 3.14% | `python` | `PyDict_Next` | unknown |
| 2.79% | `python` | `PyUnicode_AsUTF8AndSize` | unknown |
| 2.43% | `_pickle.cpython-312-x86_64-linux-gnu.so` | `_Pickler_Write.constprop.3` | library |
| 1.65% | `_pickle.cpython-312-x86_64-linux-gnu.so` | `memo_get.isra.0` | library |
| 1.61% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 1.54% | `libc-2.31.so` | `pthread_attr_setschedparam` | libc |
| 1.35% | `python` | `_PyObject_Free` | memory |
| 1.24% | `python` | `gc_collect_main` | gc |
| 1.14% | `python` | `_PyObject_Malloc` | memory |

## pickle_dict

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 45.53% | `_pickle.cpython-312-x86_64-linux-gnu.so` | `save` | library |
| 12.01% | `python` | `PyDict_Next` | unknown |
| 7.67% | `_pickle.cpython-312-x86_64-linux-gnu.so` | `_Pickler_Write` | library |
| 6.92% | `_pickle.cpython-312-x86_64-linux-gnu.so` | `_Pickler_Write.constprop.3` | library |
| 4.16% | `python` | `PyLong_AsLongAndOverflow` | unknown |
| 3.12% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 2.07% | `_pickle.cpython-312-x86_64-linux-gnu.so` | `PyMemoTable_Set` | library |
| 1.44% | `_pickle.cpython-312-x86_64-linux-gnu.so` | `Pickler_clear` | library |

## pickle_list

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 49.69% | `_pickle.cpython-312-x86_64-linux-gnu.so` | `save` | library |
| 10.32% | `_pickle.cpython-312-x86_64-linux-gnu.so` | `_Pickler_Write` | library |
| 4.70% | `python` | `PyLong_AsLongAndOverflow` | unknown |
| 4.70% | `_pickle.cpython-312-x86_64-linux-gnu.so` | `_Pickler_Write.constprop.3` | library |
| 4.52% | `_pickle.cpython-312-x86_64-linux-gnu.so` | `PyMemoTable_Set` | library |
| 2.94% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 2.40% | `_pickle.cpython-312-x86_64-linux-gnu.so` | `Pickler_clear` | library |
| 1.69% | `_pickle.cpython-312-x86_64-linux-gnu.so` | `memo_put.isra.0` | library |
| 1.66% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.47% | `libc-2.31.so` | `pthread_attr_setschedparam` | libc |
| 1.03% | `_pickle.cpython-312-x86_64-linux-gnu.so` | `0x0000000000005cc4` | library |

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

## pidigits

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 35.94% | `python` | `x_divrem` | unknown |
| 23.00% | `python` | `k_mul` | unknown |
| 11.49% | `python` | `x_add` | unknown |
| 7.46% | `python` | `x_sub` | unknown |
| 4.15% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 2.42% | `libc-2.31.so` | `pthread_attr_setschedparam` | libc |
| 1.64% | `libc-2.31.so` | `__nss_database_lookup` | libc |

## pprint

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 43.67% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 3.51% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 3.05% | `python` | `_PyObject_Malloc` | memory |
| 3.02% | `python` | `_PyObject_Free` | memory |
| 2.31% | `python` | `_PyType_Lookup` | lookup |
| 1.85% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.84% | `python` | `tupledealloc` | unknown |
| 1.42% | `python` | `_PyUnicode_JoinArray.part.0` | unknown |
| 1.38% | `python` | `_Py_dict_lookup` | lookup |
| 1.31% | `python` | `long_to_decimal_string_internal` | unknown |
| 1.22% | `python` | `PyUnicode_Format` | unknown |
| 1.16% | `python` | `_Py_type_getattro_impl` | unknown |

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
| 1.15% | `python` | `PySlice_AdjustIndices` | unknown |
| 1.11% | `python` | `subtype_traverse` | gc |
| 1.08% | `python` | `visit_reachable` | gc |
| 1.01% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.00% | `python` | `initialize_locals` | interpreter |

## pyflate

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 45.53% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 4.36% | `python` | `list_dealloc` | memory |
| 4.13% | `python` | `list_ass_slice` | unknown |
| 2.86% | `python` | `_PyObject_Free` | memory |
| 2.82% | `libc-2.31.so` | `pthread_attr_setschedparam` | libc |
| 2.66% | `python` | `list_slice.isra.0` | unknown |
| 2.03% | `python` | `_PyObject_Malloc` | memory |
| 1.99% | `python` | `list_concat` | unknown |
| 1.62% | `python` | `_PyLong_Subtract` | unknown |
| 1.54% | `python` | `_PyLong_Add` | unknown |
| 1.44% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.33% | `python` | `PySlice_AdjustIndices` | unknown |
| 1.21% | `python` | `bytes_subscript` | unknown |
| 1.15% | `python` | `PyNumber_AsSsize_t` | dynamic |
| 1.11% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.05% | `python` | `PyLong_AsSsize_t` | unknown |

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
| 1.23% | `python` | `insertdict` | unknown |
| 1.00% | `python` | `free_keys_object` | unknown |

## raytrace

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 49.07% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 3.28% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 2.18% | `python` | `_PyObject_Free` | memory |
| 1.73% | `python` | `PyFloat_FromDouble` | unknown |
| 1.60% | `python` | `tupledealloc` | unknown |
| 1.59% | `python` | `initialize_locals` | interpreter |
| 1.52% | `python` | `subtype_dealloc` | memory |
| 1.39% | `python` | `float_dealloc` | memory |
| 1.36% | `python` | `_PyObject_Malloc` | memory |
| 1.21% | `python` | `_PyEvalFramePushAndInit` | unknown |
| 1.19% | `python` | `PyType_GenericAlloc` | memory |
| 1.16% | `python` | `_PyType_Lookup` | lookup |
| 1.10% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.03% | `python` | `PyType_IsSubtype` | unknown |
| 1.01% | `python` | `_Py_NewReference` | unknown |

## regex_compile

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 41.94% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 3.24% | `python` | `sre_ucs1_match` | library |
| 2.69% | `python` | `_PyObject_Malloc` | memory |
| 2.57% | `python` | `_PyObject_Free` | memory |
| 1.94% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.28% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 1.14% | `python` | `tupledealloc` | unknown |
| 1.14% | `python` | `_PyType_Lookup` | lookup |
| 1.08% | `python` | `advance` | unknown |
| 1.07% | `libc-2.31.so` | `__nss_database_lookup` | libc |

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
| 1.32% | `python` | `pattern_new_match.isra.0.part.0` | library |

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

## scimark

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 44.25% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 3.66% | `array.cpython-312-x86_64-linux-gnu.so` | `array_subscr` | library |
| 3.60% | `python` | `PyFloat_FromDouble` | unknown |
| 3.51% | `python` | `PyType_GetModuleByDef` | unknown |
| 2.78% | `python` | `PyNumber_AsSsize_t` | dynamic |
| 2.72% | `python` | `_PyObject_Free` | memory |
| 2.60% | `python` | `vgetargs1_impl` | unknown |
| 2.49% | `python` | `PyObject_GetItem` | dynamic |
| 2.13% | `python` | `_PyLong_Add` | unknown |
| 1.83% | `python` | `_PyObject_Malloc` | memory |
| 1.56% | `python` | `convertitem` | unknown |
| 1.56% | `python` | `PyLong_AsSsize_t` | unknown |
| 1.40% | `python` | `PyLong_FromLong` | unknown |
| 1.34% | `array.cpython-312-x86_64-linux-gnu.so` | `array_ass_subscr` | library |
| 1.34% | `python` | `_Py_NewReference` | unknown |
| 1.17% | `python` | `float_dealloc` | memory |
| 1.11% | `python` | `_PyFrame_ClearExceptCode` | interpreter |

## spectral_norm

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 37.76% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 9.53% | `python` | `_PyLong_Add` | unknown |
| 5.06% | `python` | `_PyObject_Free` | memory |
| 3.51% | `python` | `float_div` | unknown |
| 3.49% | `python` | `_PyObject_Malloc (inlined)` | memory |
| 2.56% | `python` | `long_div` | unknown |
| 1.98% | `python` | `_PyLong_Multiply` | unknown |
| 1.91% | `python` | `PyType_IsSubtype` | unknown |
| 1.90% | `python` | `enum_next` | unknown |
| 1.78% | `python` | `listiter_next` | unknown |
| 1.75% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.59% | `python` | `PyLong_FromLong` | unknown |
| 1.38% | `python` | `_Py_NewReference` | unknown |
| 1.32% | `python` | `gc_collect_main` | gc |
| 1.30% | `python` | `PyNumber_TrueDivide` | dynamic |
| 1.17% | `python` | `PyNumber_FloorDivide` | dynamic |
| 1.04% | `python` | `PyLong_AsDouble` | unknown |
| 1.02% | `python` | `unicodekeys_lookup_unicode` | lookup |

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
| 1.36% | `python` | `tupledealloc` | unknown |
| 1.32% | `python` | `PyObject_GenericGetAttr` | dynamic |

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
| 1.34% | `python` | `tupledealloc` | unknown |
| 1.25% | `python` | `PyObject_GetAttr` | dynamic |
| 1.16% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.12% | `python` | `visit_decref` | gc |

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
| 1.48% | `python` | `PyType_IsSubtype` | unknown |
| 1.39% | `python` | `gc_collect_main` | gc |
| 1.26% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.25% | `python` | `tupledealloc` | unknown |
| 1.21% | `python` | `_Py_dict_lookup` | lookup |
| 1.21% | `python` | `_PyObject_GenericGetAttrWithDict` | dynamic |
| 1.13% | `python` | `initialize_locals` | interpreter |
| 1.05% | `python` | `PyObject_GetAttr` | dynamic |

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

## sympy

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 25.90% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 3.83% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 2.80% | `python` | `_PyObject_Malloc` | memory |
| 2.38% | `python` | `_PyObject_Free` | memory |
| 2.37% | `python` | `_PyType_Lookup` | lookup |
| 1.80% | `python` | `tupledealloc` | unknown |
| 1.78% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.46% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.38% | `python` | `gc_collect_main` | gc |
| 1.36% | `python` | `initialize_locals` | interpreter |
| 1.26% | `python` | `_Py_dict_lookup` | lookup |
| 1.06% | `python` | `PyObject_GenericGetAttr` | dynamic |
| 1.03% | `python` | `PyType_IsSubtype` | unknown |

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
| 1.38% | `python` | `tupledealloc` | unknown |
| 1.34% | `python` | `PyObject_GenericGetAttr` | dynamic |
| 1.32% | `python` | `convertitem` | unknown |
| 1.28% | `python` | `gc_collect_main` | gc |
| 1.24% | `_decimal.cpython-312-x86_64-linux-gnu.so` | `mpd_qquantize` | library |
| 1.20% | `python` | `_PyArg_UnpackKeywordsWithVararg` | unknown |
| 1.14% | `python` | `vgetargskeywords` | unknown |
| 1.04% | `_decimal.cpython-312-x86_64-linux-gnu.so` | `nm_mpd_qmul` | library |

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
| 1.62% | `python` | `insert_to_emptydict` | unknown |
| 1.56% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.46% | `python` | `_Py_dict_lookup` | lookup |
| 1.41% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.32% | `python` | `insertdict` | unknown |
| 1.15% | `python` | `subtype_dealloc` | memory |
| 1.13% | `python` | `gc_collect_main` | gc |
| 1.12% | `python` | `tupledealloc` | unknown |

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

## unpack_sequence

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 80.90% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 1.21% | `python` | `unicodekeys_lookup_unicode` | lookup |

## unpickle

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 7.65% | `_pickle.cpython-312-x86_64-linux-gnu.so` | `load` | library |
| 6.58% | `_pickle.cpython-312-x86_64-linux-gnu.so` | `load_counted_binunicode` | library |
| 6.02% | `python` | `siphash13` | unknown |
| 5.25% | `python` | `insertdict` | unknown |
| 5.12% | `python` | `_PyObject_Free` | memory |
| 5.10% | `python` | `ascii_decode` | unknown |
| 4.90% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 4.63% | `python` | `unicode_decode_utf8` | unknown |
| 4.51% | `python` | `_PyObject_Malloc` | memory |
| 3.36% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 2.95% | `python` | `PyUnicode_New.part.0` | unknown |
| 2.60% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 2.22% | `python` | `_Py_dict_lookup` | lookup |
| 1.96% | `_pickle.cpython-312-x86_64-linux-gnu.so` | `do_setitems.isra.0` | library |
| 1.84% | `_pickle.cpython-312-x86_64-linux-gnu.so` | `_Unpickler_MemoPut` | library |
| 1.81% | `python` | `free_keys_object` | unknown |
| 1.68% | `python` | `dict_ass_sub` | unknown |
| 1.40% | `python` | `_PyObject_Realloc` | dynamic |
| 1.26% | `python` | `find_empty_slot` | unknown |
| 1.23% | `python` | `build_indices_unicode` | unknown |
| 1.08% | `python` | `PyObject_SetItem` | dynamic |

## unpickle_list

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 17.37% | `_pickle.cpython-312-x86_64-linux-gnu.so` | `load` | library |
| 7.67% | `python` | `list_dealloc` | memory |
| 5.75% | `python` | `list_ass_slice` | unknown |
| 5.36% | `python` | `PyList_New` | unknown |
| 5.16% | `python` | `PyLong_FromLong` | unknown |
| 4.93% | `python` | `_PyObject_Free` | memory |
| 4.45% | `_pickle.cpython-312-x86_64-linux-gnu.so` | `Pdata_push` | library |
| 3.84% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 3.62% | `_pickle.cpython-312-x86_64-linux-gnu.so` | `do_append.isra.0` | library |
| 3.07% | `python` | `_PyObject_Malloc` | memory |
| 2.42% | `python` | `_PyObject_Calloc` | dynamic |
| 2.16% | `python` | `PyMem_Calloc` | memory |
| 1.88% | `python` | `_Py_NewReference` | unknown |
| 1.65% | `python` | `PyObject_GC_UnTrack` | dynamic |
| 1.48% | `python` | `_PyObject_Realloc` | dynamic |
| 1.47% | `python` | `_PyTrash_begin` | gc |
| 1.39% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.34% | `_pickle.cpython-312-x86_64-linux-gnu.so` | `marker.isra.0` | library |
| 1.32% | `python` | `gc_collect_main` | gc |
| 1.19% | `python` | `_PyTrash_end` | gc |
| 1.08% | `python` | `unicodekeys_lookup_unicode` | lookup |

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
| 1.10% | `python` | `insertdict` | unknown |
| 1.10% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 1.09% | `python` | `PyBytes_FromStringAndSize` | unknown |
| 1.00% | `python` | `initialize_locals` | interpreter |

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


## Categories

### interpreter

29.82% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 28.44% | python | _PyEval_EvalFrameDefault |
| 0.98% | python | _PyFrame_ClearExceptCode |
| 0.38% | python | initialize_locals |
| 0.01% | python | _PyThreadState_PopFrame |

### unknown

8.66% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 0.53% | python | k_mul |
| 0.49% | python | x_divrem |
| 0.38% | python | tuplehash |
| 0.37% | python | tupledealloc |
| 0.35% | python | _PyLong_Add |
| 0.29% | python | siphash13 |
| 0.23% | python | PyDict_Next |
| 0.22% | python | insertdict |
| 0.20% | python | list_ass_slice |
| 0.20% | python | PyFloat_FromDouble |
| 0.17% | python | _Py_NewReference |
| 0.17% | python | PySlice_AdjustIndices |
| 0.17% | python | PyLong_FromLong |
| 0.16% | python | x_add |
| 0.15% | python | long_hash |
| 0.14% | python | _PyErr_SetObject.part.0 |
| 0.12% | python | PyLong_AsLongAndOverflow |
| 0.11% | python | PyType_IsSubtype |
| 0.11% | python | set_issubset |
| 0.11% | python | replace |
| 0.10% | python | set_lookkey |
| 0.10% | python | long_to_decimal_string_internal |
| 0.10% | python | advance |
| 0.10% | python | x_sub |
| 0.10% | python | _PyLong_Subtract |
| 0.09% | python | _PyUnicode_JoinArray.part.0 |
| 0.09% | python | long_bitwise |
| 0.09% | python | PyDict_SetDefault |
| 0.08% | python | PyLong_FromString |
| 0.08% | python | free_keys_object |
| 0.08% | python | setiter_iternext |
| 0.08% | python | list_subscript |
| 0.07% | python | float_div |
| 0.07% | python | _copy_characters.part.0.constprop.0 |
| 0.07% | python | PyList_New |
| 0.07% | python | set_add_entry |
| 0.07% | python | ascii_decode |
| 0.07% | python | long_richcompare |
| 0.07% | python | _PyEvalFramePushAndInit |
| 0.06% | python | unicode_decode_utf8 |
| 0.06% | python | _PyStaticCode_Fini |
| 0.06% | python | convertitem |
| 0.06% | python | find_empty_slot |
| 0.05% | python | list_slice.isra.0 |
| 0.05% | python | PyLong_AsSsize_t |
| 0.05% | python | long_rshift1 |
| 0.05% | python | build_indices_unicode |
| 0.05% | python | _PyUnicodeWriter_WriteStr |
| 0.05% | python | PyUnicode_Substring |
| 0.05% | python | PyUnicode_New |
| 0.05% | python | call_trace.part.0 |
| 0.05% | python | PyType_GetModuleByDef |
| 0.05% | python | set_difference |
| 0.05% | python | gen_iternext |
| 0.04% | python | dict_get |
| 0.04% | python | make_gen |
| 0.04% | python | _PyUnicode_FromASCII |
| 0.04% | python | async_gen_asend_iternext |
| 0.04% | python | PyUnicode_New.part.0 |
| 0.04% | python | update_one_slot |
| 0.04% | python | resize_compact |
| 0.04% | python | insert_to_emptydict |
| 0.04% | python | bytes_subscript |
| 0.04% | python | take_gil |
| 0.04% | python | deque_append |
| 0.04% | python | PyUnicode_AsUTF8AndSize |
| 0.04% | python | vgetargskeywords |
| 0.04% | python | vgetargs1_impl |
| 0.03% | python | l_mod |
| 0.03% | python | long_div |
| 0.03% | python | long_and |
| 0.03% | python | PyUnicode_Format |
| 0.03% | python | list_contains |
| 0.03% | python | _PyEval_SliceIndex |
| 0.03% | python | PySlice_Unpack |
| 0.03% | python | _PyUnicode_FromASCII (inlined) |
| 0.03% | python | tuplerichcompare |
| 0.03% | python | list_concat |
| 0.03% | python | _PyLong_Multiply |
| 0.03% | python | async_gen_anext |
| 0.03% | python | enum_next |
| 0.03% | python | unicode_replace |
| 0.03% | python | PyErr_ExceptionMatches |
| 0.02% | python | dequeiter_next |
| 0.02% | python | listiter_next |
| 0.02% | python | dict_ass_sub |
| 0.02% | python | PyContextVar_Get |
| 0.02% | python | PySlice_New |
| 0.02% | python | PyFunction_NewWithQualName |
| 0.02% | python | list_ass_subscript |
| 0.02% | python | _PyBuildSlice_ConsumeRefs |
| 0.02% | python | _PyTuple_FromArray |
| 0.02% | python | long_rshift |
| 0.02% | python | PyLong_FromVoidPtr |
| 0.02% | python | min_max |
| 0.02% | python | list_extend |
| 0.02% | python | PyDict_GetItem |
| 0.02% | python | _io_TextIOWrapper_write |
| 0.02% | python | PyLong_FromSsize_t |
| 0.02% | python | PyErr_CheckSignals |
| 0.02% | python | float_pow |
| 0.02% | python | _PyErr_Restore |
| 0.02% | python | _PyAsyncGenValueWrapperNew |
| 0.02% | python | _PyGen_SetStopIterationValue |
| 0.02% | python | _PyArg_UnpackKeywordsWithVararg |
| 0.02% | python | _PyGen_FetchStopIterationValue |
| 0.02% | python | _Py_type_getattro_impl |
| 0.02% | python | dict_subscript |
| 0.02% | python | long_xor |
| 0.02% | python | list_insert |
| 0.02% | python | _PyUnicodeWriter_PrepareInternal |
| 0.01% | python | _Py_MakeCoro |
| 0.01% | python | PyBytes_FromStringAndSize |
| 0.01% | python | PyIter_Next |
| 0.01% | python | PyLong_AsDouble |
| 0.01% | python | _PyThreadState_Swap |
| 0.01% | python | PyDict_SetItem |
| 0.01% | python | drop_gil |

### library

8.29% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 1.94% | python | sre_ucs1_match |
| 1.64% | _pickle.cpython-312-x86_64-linux-gnu.so | save |
| 0.78% | python | sre_ucs2_charset.isra.0 |
| 0.37% | _pickle.cpython-312-x86_64-linux-gnu.so | _Pickler_Write |
| 0.34% | _json.cpython-312-x86_64-linux-gnu.so | scanstring_unicode |
| 0.34% | _pickle.cpython-312-x86_64-linux-gnu.so | load |
| 0.26% | python | sre_search |
| 0.19% | _pickle.cpython-312-x86_64-linux-gnu.so | PyMemoTable_Set |
| 0.19% | _pickle.cpython-312-x86_64-linux-gnu.so | _Pickler_Write.constprop.3 |
| 0.18% | _json.cpython-312-x86_64-linux-gnu.so | scan_once_unicode |
| 0.18% | libpthread-2.31.so | __pthread_mutex_lock |
| 0.16% | libpthread-2.31.so | pthread_mutex_unlock |
| 0.15% | libm-2.31.so | f64xsubf128 |
| 0.11% | _json.cpython-312-x86_64-linux-gnu.so | py_encode_basestring_ascii |
| 0.11% | _pickle.cpython-312-x86_64-linux-gnu.so | Pickler_clear |
| 0.10% | python | sre_ucs1_count |
| 0.09% | _pickle.cpython-312-x86_64-linux-gnu.so | load_counted_binunicode |
| 0.08% | tracer.cpython-312-x86_64-linux-gnu.so | CTracer_trace |
| 0.08% | _pickle.cpython-312-x86_64-linux-gnu.so | memo_put.isra.0 |
| 0.06% | _pickle.cpython-312-x86_64-linux-gnu.so | Pdata_push |
| 0.06% | libsqlite3.so.0.8.6 | sqlite3_reset |
| 0.05% | array.cpython-312-x86_64-linux-gnu.so | array_subscr |
| 0.05% | _pickle.cpython-312-x86_64-linux-gnu.so | do_append.isra.0 |
| 0.04% | _json.cpython-312-x86_64-linux-gnu.so | encoder_listencode_obj |
| 0.04% | libz.so.1.2.11 | inflateCodesUsed |
| 0.04% | libm-2.31.so | __fmod_finite |
| 0.04% | python | _sre_SRE_Pattern_search |
| 0.04% | pyexpat.cpython-312-x86_64-linux-gnu.so | normal_contentTok |
| 0.03% | pyexpat.cpython-312-x86_64-linux-gnu.so | normal_updatePosition |
| 0.03% | _json.cpython-312-x86_64-linux-gnu.so | encoder_encode_key_value |
| 0.03% | python | pattern_subx |
| 0.03% | _decimal.cpython-312-x86_64-linux-gnu.so | _mpd_qaddsub |
| 0.03% | _pickle.cpython-312-x86_64-linux-gnu.so | do_setitems.isra.0 |
| 0.03% | _decimal.cpython-312-x86_64-linux-gnu.so | _mpd_check_exp |
| 0.02% | _pickle.cpython-312-x86_64-linux-gnu.so | _Unpickler_MemoPut |
| 0.02% | libz.so.1.2.11 | inflateBackEnd |
| 0.02% | fastbinary.cpython-312-x86_64-linux-gnu.so | apache::thrift::py::ProtocolBase<apache::thrift::py::BinaryProtocol>::encodeValue |
| 0.02% | _pickle.cpython-312-x86_64-linux-gnu.so | memo_get.isra.0 |
| 0.02% | _decimal.cpython-312-x86_64-linux-gnu.so | _mpd_qmul |
| 0.02% | _decimal.cpython-312-x86_64-linux-gnu.so | mpd_setdigits |
| 0.02% | pyexpat.cpython-312-x86_64-linux-gnu.so | accountingDiffTolerated.part.0 |
| 0.02% | libz.so.1.2.11 | inflate |
| 0.02% | _decimal.cpython-312-x86_64-linux-gnu.so | nm_mpd_qadd |
| 0.02% | _decimal.cpython-312-x86_64-linux-gnu.so | _mpd_baseshiftr |
| 0.02% | pyexpat.cpython-312-x86_64-linux-gnu.so | sip24_update |
| 0.02% | array.cpython-312-x86_64-linux-gnu.so | array_ass_subscr |
| 0.02% | _pickle.cpython-312-x86_64-linux-gnu.so | marker.isra.0 |
| 0.02% | python | pattern_new_match.isra.0.part.0 |
| 0.02% | libsqlite3.so.0.8.6 | sqlite3_randomness |
| 0.02% | pyexpat.cpython-312-x86_64-linux-gnu.so | doContent |
| 0.02% | _decimal.cpython-312-x86_64-linux-gnu.so | mpd_qquantize |
| 0.02% | pyexpat.cpython-312-x86_64-linux-gnu.so | normal_nameLength |
| 0.02% | math.cpython-312-x86_64-linux-gnu.so | factorial_partial_product |
| 0.01% | libpthread-2.31.so | pthread_cond_signal@@GLIBC_2.3.2 |
| 0.01% | _bisect.cpython-312-x86_64-linux-gnu.so | _bisect_bisect_right |
| 0.01% | _decimal.cpython-312-x86_64-linux-gnu.so | nm_mpd_qmul |
| 0.01% | _pickle.cpython-312-x86_64-linux-gnu.so | 0x0000000000005cc4 |

### gc

6.61% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 3.47% | python | gc_collect_main |
| 1.25% | python | visit_decref |
| 1.23% | python | visit_reachable |
| 0.21% | python | list_traverse |
| 0.15% | python | subtype_traverse |
| 0.13% | python | dict_traverse |
| 0.03% | python | PyObject_IS_GC |
| 0.03% | python | _PyDict_MaybeUntrack |
| 0.02% | python | func_traverse |
| 0.02% | python | set_traverse |
| 0.02% | python | _PyObject_VisitManagedDict |
| 0.02% | python | _PyTrash_begin |
| 0.02% | python | type_is_gc |
| 0.02% | python | _PyTrash_end |

### memory

5.21% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 2.18% | python | _PyObject_Free |
| 1.91% | python | _PyObject_Malloc |
| 0.28% | python | _PyObject_Malloc (inlined) |
| 0.27% | python | list_dealloc |
| 0.10% | python | gen_dealloc |
| 0.09% | python | float_dealloc |
| 0.08% | python | subtype_dealloc |
| 0.06% | python | set_dealloc |
| 0.05% | python | PyType_GenericAlloc |
| 0.04% | python | slice_dealloc |
| 0.03% | python | PyMem_Calloc |
| 0.02% | python | PyObject_CallFinalizerFromDealloc |
| 0.02% | python | dict_dealloc |
| 0.02% | python | async_gen_asend_dealloc |
| 0.02% | python | async_gen_wrapped_val_dealloc |
| 0.01% | python | tuple_alloc |
| 0.01% | python | StopIteration_dealloc |

### lookup

3.49% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 1.87% | python | unicodekeys_lookup_unicode |
| 1.09% | python | _Py_dict_lookup |
| 0.54% | python | _PyType_Lookup |

### libc

1.78% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 1.53% | libc-2.31.so | __nss_database_lookup |
| 0.25% | libc-2.31.so | pthread_attr_setschedparam |

### dynamic

1.36% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 0.29% | python | PyObject_GenericGetAttr |
| 0.19% | python | PyObject_Hash |
| 0.10% | python | PyNumber_AsSsize_t |
| 0.10% | python | PyObject_RichCompare |
| 0.07% | python | _PyObject_Realloc |
| 0.07% | python | _PyObject_GetMethod |
| 0.07% | python | PyObject_GetAttr |
| 0.06% | python | PyObject_IsTrue |
| 0.05% | python | _PyObject_GetInstanceAttribute |
| 0.04% | python | _PyObject_GC_NewVar |
| 0.04% | python | PyObject_RichCompareBool |
| 0.04% | python | PyObject_GC_UnTrack |
| 0.03% | python | PyObject_GetItem |
| 0.03% | python | _PyObject_GenericGetAttrWithDict |
| 0.03% | python | _PyObject_Calloc |
| 0.02% | python | _PyObject_MakeTpCall |
| 0.02% | python | PyNumber_TrueDivide |
| 0.02% | python | PyObject_GC_Del |
| 0.02% | python | PyNumber_And |
| 0.02% | python | PyNumber_FloorDivide |
| 0.01% | python | PyObject_CallOneArg |
| 0.01% | python | PyObject_SetItem |
| 0.01% | python | type_call |

### kernel

0.60% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 0.44% | [kernel.kallsyms] | copy_user_enhanced_fast_string |
| 0.11% | [kernel.kallsyms] | clear_page_erms |
| 0.02% | [kernel.kallsyms] | __d_lookup_rcu |
| 0.02% | [kernel.kallsyms] | __ext4fs_dirhash |
| 0.02% | [kernel.kallsyms] | memset_erms |
