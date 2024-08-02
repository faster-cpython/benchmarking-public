
## 2to3

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 27.23% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 3.50% | `python` | `gc_collect_region.isra.0` | gc |
| 3.14% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 2.99% | `python` | `_PyObject_Malloc` | memory |
| 2.28% | `python` | `_PyObject_Free` | memory |
| 2.18% | `python` | `_Py_dict_lookup` | lookup |
| 1.88% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.81% | `python` | `_PyType_LookupRef` | lookup |
| 1.44% | `python` | `sre_ucs1_match` | library |
| 1.42% | `python` | `tupledealloc` | memory |
| 1.39% | `python` | `visit_decref` | gc |
| 1.27% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 0.86% | `python` | `PyObject_GenericGetAttr` | dynamic |
| 0.82% | `python` | `_PyTuple_FromStackRefSteal` | tuple |
| 0.82% | `python` | `visit_reachable` | gc |
| 0.71% | `python` | `_PyPegen_is_memoized` | interpreter |
| 0.71% | `libc-2.31.so` | `pthread_attr_setschedparam` | libc |
| 0.68% | `python` | `r_object` | import |
| 0.66% | `python` | `siphash13` | str |
| 0.63% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.61% | `python` | `initialize_locals` | interpreter |
| 0.56% | `python` | `PyObject_RichCompareBool` | dynamic |
| 0.52% | `python` | `_PyObject_TryGetInstanceAttribute` | dynamic |
| 0.50% | `python` | `dict_dealloc` | memory |
| 0.50% | `python` | `PyObject_GetAttr` | dynamic |
| 0.50% | `python` | `find_name_in_mro` | lookup |
| 0.48% | `python` | `update_one_slot` | lookup |
| 0.48% | `python` | `_PyCode_Quicken` | interpreter |
| 0.47% | `python` | `PyDict_GetItemRef` | dict |
| 0.46% | `python` | `_Py_hashtable_get_entry_generic` | lookup |
| 0.43% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.42% | `python` | `_Py_Dealloc` | memory |
| 0.40% | `python` | `list_dealloc` | memory |
| 0.37% | `python` | `_PyPegen_expect_token` | interpreter |
| 0.35% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.34% | `python` | `gen_dealloc` | memory |
| 0.34% | `python` | `dict_traverse` | gc |
| 0.34% | `python` | `tok_get_normal_mode` | compiler |
| 0.33% | `python` | `PyObject_GC_Del` | gc |
| 0.32% | `python` | `insertdict` | dict |
| 0.31% | `python` | `insert_to_emptydict` | dict |
| 0.30% | `python` | `type_ready` | dynamic |
| 0.29% | `python` | `_PyPegen_update_memo` | interpreter |
| 0.29% | `python` | `_PyUnicode_FromUCS1.part.0` | str |
| 0.28% | `python` | `_Py_NewReference` | memory |
| 0.28% | `python` | `list_subscript` | list |
| 0.27% | `python` | `sre_ucs1_count` | library |
| 0.27% | `python` | `sre_ucs2_charset.isra.0` | library |
| 0.26% | `python` | `_PyCfg_OptimizeCodeUnit` | unknown |
| 0.26% | `libz.so.1.2.11` | `inflateBackEnd` | library |

## async_generators

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 22.88% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 8.60% | `python` | `_PyErr_SetObject.part.0` | exceptions |
| 3.99% | `python` | `_PyObject_Malloc` | memory |
| 3.83% | `python` | `_PyObject_Free` | memory |
| 2.69% | `python` | `async_gen_asend_iternext` | async |
| 2.47% | `python` | `PyType_GenericAlloc` | memory |
| 2.35% | `python` | `_PyTuple_FromArray.part.0` | tuple |
| 2.25% | `python` | `tupledealloc` | memory |
| 2.03% | `python` | `StopIteration_init` | dynamic |
| 1.87% | `python` | `_Py_Dealloc` | memory |
| 1.83% | `python` | `_PyAsyncGenValueWrapperNew` | memory |
| 1.65% | `python` | `async_gen_wrapped_val_dealloc` | memory |
| 1.52% | `python` | `PyErr_ExceptionMatches` | exceptions |
| 1.45% | `python` | `_PyErr_ExceptionMatches` | exceptions |
| 1.40% | `python` | `async_gen_anext` | async |
| 1.39% | `python` | `async_gen_asend_dealloc` | memory |
| 1.37% | `python` | `StopIteration_dealloc` | memory |
| 1.36% | `python` | `_PyGen_FetchStopIterationValue` | miscobj |
| 1.34% | `python` | `_PyObject_MakeTpCall` | dynamic |
| 1.27% | `python` | `PyObject_GC_UnTrack` | gc |
| 1.20% | `python` | `_PyErr_Restore` | exceptions |
| 1.17% | `python` | `type_call` | dynamic |
| 1.15% | `python` | `PyObject_GC_Del` | gc |
| 1.13% | `python` | `_Py_NewReference` | memory |
| 1.10% | `python` | `PyObject_CallOneArg` | dynamic |
| 0.94% | `python` | `gc_collect_region.isra.0` | gc |
| 0.89% | `python` | `PyObject_CallFinalizerFromDealloc` | memory |
| 0.87% | `python` | `_PyGen_SetStopIterationValue` | miscobj |
| 0.71% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 0.70% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 0.68% | `python` | `PyType_IsSubtype` | dynamic |
| 0.66% | `python` | `BaseException_new` | memory |
| 0.64% | `python` | `PyObject_RichCompareBool` | dynamic |
| 0.60% | `python` | `_PyErr_CreateException` | exceptions |
| 0.58% | `python` | `_PyObject_GC_Link` | gc |
| 0.55% | `python` | `PyErr_SetObject` | exceptions |
| 0.52% | `python` | `long_add` | int |
| 0.52% | `python` | `initialize_locals` | interpreter |
| 0.51% | `python` | `visit_decref` | gc |
| 0.46% | `python` | `visit_reachable` | gc |
| 0.40% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.37% | `python` | `range_subscript` | miscobj |
| 0.37% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.33% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.33% | `python` | `long_richcompare` | int |
| 0.32% | `python` | `_Py_CheckFunctionResult` | calls |
| 0.31% | `python` | `compute_range_length` | unknown |
| 0.30% | `python` | `PyNumber_Add` | dynamic |
| 0.30% | `python` | `visit_add_to_container` | gc |
| 0.28% | `python` | `PyObject_ClearWeakRefs` | dynamic |
| 0.26% | `python` | `_PySlice_GetLongIndices` | miscobj |
| 0.25% | `python` | `_PyBuildSlice_ConsumeRefs` | miscobj |

## async_tree

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 24.69% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 9.29% | `python` | `gc_collect_region.isra.0` | gc |
| 4.52% | `python` | `visit_decref` | gc |
| 4.49% | `python` | `visit_reachable` | gc |
| 4.31% | `python` | `visit_add_to_container` | gc |
| 3.73% | `python` | `_PyObject_Malloc` | memory |
| 2.28% | `python` | `_PyObject_Free` | memory |
| 1.61% | `python` | `_Py_dict_lookup` | lookup |
| 1.59% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.53% | `python` | `_PyType_LookupRef` | lookup |
| 1.40% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 1.25% | `python` | `initialize_locals` | interpreter |
| 1.13% | `python` | `subtype_traverse` | gc |
| 0.94% | `python` | `context_tp_dealloc` | memory |
| 0.94% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.80% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 0.76% | `python` | `tupledealloc` | memory |
| 0.68% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.64% | `python` | `subtype_dealloc` | memory |
| 0.64% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.61% | `python` | `_PyGC_Collect` | gc |
| 0.60% | `python` | `_PyEval_Vector` | interpreter |
| 0.59% | `_asyncio.cpython-314-x86_64-linux-gnu.so` | `TaskObj_traverse` | library |
| 0.58% | `python` | `dict_traverse` | gc |
| 0.57% | `python` | `_PyFrame_Traverse` | interpreter |
| 0.55% | `python` | `dict_dealloc` | memory |
| 0.55% | `python` | `_PyObject_GetMethod` | dynamic |
| 0.50% | `python` | `PyDict_GetItemRef` | dict |
| 0.49% | `python` | `PyObject_RichCompareBool` | dynamic |
| 0.49% | `python` | `_PyTuple_FromArray.part.0` | tuple |
| 0.48% | `python` | `PyObject_GC_Del` | gc |
| 0.47% | `python` | `PyObject_GenericGetAttr` | dynamic |
| 0.46% | `python` | `_PyObject_GC_New` | gc |
| 0.45% | `python` | `insertdict` | dict |
| 0.45% | `python` | `gen_dealloc` | memory |
| 0.44% | `python` | `_Py_Dealloc` | memory |
| 0.42% | `python` | `_PyArg_UnpackKeywords` | calls |
| 0.42% | `python` | `insert_to_emptydict` | dict |
| 0.40% | `python` | `_PyObject_MakeTpCall` | dynamic |
| 0.38% | `python` | `PyType_GenericAlloc` | memory |
| 0.36% | `python` | `_PyThreadState_PopFrame` | interpreter |
| 0.35% | `python` | `_PyObject_GC_Link` | gc |
| 0.34% | `python` | `list_dealloc` | memory |
| 0.32% | `python` | `_PyObject_Calloc` | memory |
| 0.31% | `python` | `_PyObject_Realloc` | memory |
| 0.31% | `python` | `PyUnicode_RichCompare` | str |
| 0.31% | `python` | `gen_traverse` | gc |
| 0.27% | `python` | `_Py_NewReference` | memory |
| 0.27% | `python` | `PyObject_GetAttr` | dynamic |
| 0.26% | `python` | `dict_setdefault_ref_lock_held` | dict |
| 0.26% | `_asyncio.cpython-314-x86_64-linux-gnu.so` | `TaskObj_clear` | library |
| 0.26% | `python` | `_PyDict_FromItems` | dict |
| 0.26% | `[kernel.kallsyms]` | `clear_page_erms` | kernel |
| 0.26% | `python` | `PyObject_Vectorcall` | dynamic |
| 0.25% | `[kernel.kallsyms]` | `native_irq_return_iret` | kernel |
| 0.25% | `python` | `PyObject_VectorcallMethod` | dynamic |

## async_tree_cpu_io_mixed

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 20.07% | `python` | `k_mul` | int |
| 17.20% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 6.09% | `python` | `gc_collect_region.isra.0` | gc |
| 4.24% | `python` | `_PyObject_Malloc` | memory |
| 3.68% | `python` | `_PyObject_Free` | memory |
| 3.24% | `python` | `visit_decref` | gc |
| 2.92% | `python` | `visit_reachable` | gc |
| 2.53% | `python` | `visit_add_to_container` | gc |
| 1.69% | `python` | `PyErr_CheckSignals` | exceptions |
| 1.19% | `math.cpython-314-x86_64-linux-gnu.so` | `factorial_partial_product` | library |
| 1.11% | `python` | `_Py_dict_lookup` | lookup |
| 1.11% | `python` | `_PyType_LookupRef` | lookup |
| 1.06% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 0.94% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.88% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 0.85% | `python` | `initialize_locals` | interpreter |
| 0.83% | `python` | `subtype_traverse` | gc |
| 0.80% | `python` | `PyThread_get_thread_ident` | unknown |
| 0.75% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.68% | `python` | `PyLong_FromUnsignedLong` | int |
| 0.66% | `python` | `context_tp_dealloc` | memory |
| 0.65% | `python` | `_Py_Dealloc` | memory |
| 0.55% | `python` | `long_mul` | int |
| 0.47% | `python` | `tupledealloc` | memory |
| 0.46% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.45% | `python` | `PyNumber_Multiply` | dynamic |
| 0.45% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.44% | `python` | `_PyGC_Collect` | gc |
| 0.42% | `python` | `_PyEval_Vector` | interpreter |
| 0.42% | `python` | `gen_dealloc` | memory |
| 0.40% | `python` | `long_lshift1` | int |
| 0.39% | `python` | `_Py_NewReference` | memory |
| 0.39% | `python` | `_PyObject_GetMethod` | dynamic |
| 0.39% | `python` | `subtype_dealloc` | memory |
| 0.38% | `python` | `PyObject_GenericGetAttr` | dynamic |
| 0.34% | `python` | `dict_traverse` | gc |
| 0.34% | `python` | `dict_dealloc` | memory |
| 0.34% | `python` | `_PyFrame_Traverse` | interpreter |
| 0.33% | `python` | `PyDict_GetItemRef` | dict |
| 0.33% | `_asyncio.cpython-314-x86_64-linux-gnu.so` | `TaskObj_traverse` | library |
| 0.32% | `python` | `PyObject_RichCompareBool` | dynamic |
| 0.32% | `python` | `PyObject_GC_Del` | gc |
| 0.31% | `python` | `_PyTuple_FromArray.part.0` | tuple |
| 0.31% | `libc-2.31.so` | `pthread_self` | libc |
| 0.29% | `python` | `_PyObject_GC_New` | gc |
| 0.27% | `python` | `_PyObject_MakeTpCall` | dynamic |

## async_tree_cpu_io_mixed_tg

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 21.13% | `python` | `k_mul` | int |
| 16.16% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 6.50% | `python` | `gc_collect_region.isra.0` | gc |
| 4.26% | `python` | `_PyObject_Malloc` | memory |
| 3.80% | `python` | `visit_decref` | gc |
| 3.67% | `python` | `_PyObject_Free` | memory |
| 3.62% | `python` | `visit_add_to_container` | gc |
| 3.35% | `python` | `visit_reachable` | gc |
| 1.65% | `python` | `PyErr_CheckSignals` | exceptions |
| 1.22% | `math.cpython-314-x86_64-linux-gnu.so` | `factorial_partial_product` | library |
| 0.95% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 0.92% | `python` | `_PyType_LookupRef` | lookup |
| 0.88% | `python` | `initialize_locals` | interpreter |
| 0.88% | `python` | `PyThread_get_thread_ident` | unknown |
| 0.87% | `python` | `subtype_traverse` | gc |
| 0.86% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 0.86% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.79% | `python` | `_Py_dict_lookup` | lookup |
| 0.72% | `python` | `PyLong_FromUnsignedLong` | int |
| 0.66% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.64% | `python` | `_Py_Dealloc` | memory |
| 0.55% | `python` | `long_mul` | int |
| 0.50% | `python` | `_PyEval_Vector` | interpreter |
| 0.48% | `python` | `_PyFrame_Traverse` | interpreter |
| 0.46% | `python` | `PyNumber_Multiply` | dynamic |
| 0.45% | `python` | `_PyGC_Collect` | gc |
| 0.44% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.44% | `python` | `tupledealloc` | memory |
| 0.44% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.39% | `python` | `subtype_dealloc` | memory |
| 0.37% | `python` | `_Py_NewReference` | memory |
| 0.37% | `python` | `long_lshift1` | int |
| 0.36% | `_asyncio.cpython-314-x86_64-linux-gnu.so` | `TaskObj_traverse` | library |
| 0.35% | `python` | `PyObject_GenericGetAttr` | dynamic |
| 0.33% | `python` | `_PyObject_GetMethod` | dynamic |
| 0.32% | `python` | `set_traverse` | gc |
| 0.32% | `python` | `PyDict_GetItemRef` | dict |
| 0.31% | `libc-2.31.so` | `pthread_self` | libc |
| 0.30% | `python` | `PyObject_RichCompareBool` | dynamic |
| 0.29% | `python` | `PyObject_GC_Del` | gc |
| 0.27% | `python` | `PyType_GenericAlloc` | memory |
| 0.26% | `python` | `_PyTuple_FromArray.part.0` | tuple |
| 0.25% | `python` | `long_dealloc` | memory |

## async_tree_io

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 21.61% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 14.30% | `python` | `gc_collect_region.isra.0` | gc |
| 7.34% | `python` | `visit_add_to_container` | gc |
| 6.94% | `python` | `visit_decref` | gc |
| 6.61% | `python` | `visit_reachable` | gc |
| 2.50% | `python` | `_PyObject_Malloc` | memory |
| 1.70% | `python` | `_PyObject_Free` | memory |
| 1.37% | `python` | `subtype_traverse` | gc |
| 1.31% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.29% | `python` | `_PyFrame_Traverse` | interpreter |
| 1.26% | `python` | `initialize_locals` | interpreter |
| 1.14% | `python` | `_PyType_LookupRef` | lookup |
| 1.09% | `python` | `_PyGC_Collect` | gc |
| 0.90% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.86% | `python` | `_Py_dict_lookup` | lookup |
| 0.80% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.73% | `python` | `_PyEval_Vector` | interpreter |
| 0.71% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.67% | `python` | `gen_traverse` | gc |
| 0.57% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.56% | `_asyncio.cpython-314-x86_64-linux-gnu.so` | `TaskObj_traverse` | library |
| 0.55% | `python` | `tupledealloc` | memory |
| 0.54% | `python` | `PyObject_RichCompareBool` | dynamic |
| 0.51% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 0.49% | `python` | `subtype_dealloc` | memory |
| 0.48% | `_heapq.cpython-314-x86_64-linux-gnu.so` | `siftup` | library |
| 0.45% | `python` | `dict_traverse` | gc |
| 0.44% | `python` | `gen_dealloc` | memory |
| 0.44% | `python` | `context_tp_dealloc` | memory |
| 0.36% | `python` | `slot_tp_richcompare` | dynamic |
| 0.34% | `python` | `PyObject_GenericGetAttr` | dynamic |
| 0.34% | `python` | `_PyThreadState_PopFrame` | interpreter |
| 0.32% | `python` | `PyObject_IS_GC` | gc |
| 0.32% | `python` | `_PyTuple_FromArray.part.0` | tuple |
| 0.32% | `python` | `PyObject_GC_Del` | gc |
| 0.32% | `python` | `PyDict_GetItemRef` | dict |
| 0.31% | `python` | `insert_to_emptydict` | dict |
| 0.31% | `python` | `dict_dealloc` | memory |
| 0.30% | `python` | `_PyObject_GC_New` | gc |
| 0.29% | `python` | `_PyObject_Realloc` | memory |
| 0.28% | `python` | `_Py_Dealloc` | memory |
| 0.28% | `python` | `_PyObject_GetMethod` | dynamic |
| 0.27% | `python` | `PyType_GenericAlloc` | memory |
| 0.27% | `python` | `_PyObject_MakeTpCall` | dynamic |
| 0.26% | `python` | `_PyThreadState_PushFrame` | interpreter |
| 0.26% | `python` | `context_run` | unknown |

## async_tree_io_tg

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 21.22% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 13.74% | `python` | `gc_collect_region.isra.0` | gc |
| 7.93% | `python` | `visit_add_to_container` | gc |
| 7.25% | `python` | `visit_decref` | gc |
| 6.84% | `python` | `visit_reachable` | gc |
| 2.44% | `python` | `_PyObject_Malloc` | memory |
| 1.69% | `python` | `_PyObject_Free` | memory |
| 1.43% | `python` | `subtype_traverse` | gc |
| 1.34% | `python` | `_PyFrame_Traverse` | interpreter |
| 1.31% | `python` | `initialize_locals` | interpreter |
| 1.30% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.11% | `python` | `_PyGC_Collect` | gc |
| 1.01% | `python` | `_PyType_LookupRef` | lookup |
| 1.00% | `python` | `_PyEval_Vector` | interpreter |
| 0.87% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.83% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.73% | `python` | `_Py_dict_lookup` | lookup |
| 0.71% | `python` | `gen_traverse` | gc |
| 0.69% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.58% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.57% | `python` | `PyObject_RichCompareBool` | dynamic |
| 0.57% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 0.53% | `_asyncio.cpython-314-x86_64-linux-gnu.so` | `TaskObj_traverse` | library |
| 0.52% | `_heapq.cpython-314-x86_64-linux-gnu.so` | `siftup` | library |
| 0.52% | `python` | `tupledealloc` | memory |
| 0.51% | `python` | `subtype_dealloc` | memory |
| 0.50% | `python` | `set_traverse` | gc |
| 0.39% | `python` | `gen_dealloc` | memory |
| 0.38% | `python` | `PyObject_GenericGetAttr` | dynamic |
| 0.36% | `python` | `slot_tp_richcompare` | dynamic |
| 0.34% | `python` | `PyObject_VisitManagedDict` | dynamic |
| 0.32% | `python` | `_PyTuple_FromArray.part.0` | tuple |
| 0.32% | `python` | `_PyThreadState_PopFrame` | interpreter |
| 0.32% | `python` | `PyType_GenericAlloc` | memory |
| 0.31% | `python` | `PyDict_GetItemRef` | dict |
| 0.31% | `python` | `PyObject_GC_Del` | gc |
| 0.30% | `python` | `insert_to_emptydict` | dict |
| 0.29% | `python` | `_Py_Dealloc` | memory |
| 0.28% | `[kernel.kallsyms]` | `clear_page_erms` | kernel |
| 0.27% | `python` | `_PyThreadState_PushFrame` | interpreter |
| 0.27% | `python` | `_PyObject_GC_New` | gc |
| 0.27% | `python` | `dict_traverse` | gc |
| 0.26% | `python` | `_PyObject_MakeTpCall` | dynamic |
| 0.26% | `python` | `_PyObject_Realloc` | memory |
| 0.25% | `python` | `_PyObject_Calloc` | memory |

## async_tree_memoization

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 25.29% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 10.03% | `python` | `gc_collect_region.isra.0` | gc |
| 5.10% | `python` | `visit_decref` | gc |
| 4.84% | `python` | `visit_reachable` | gc |
| 4.43% | `python` | `visit_add_to_container` | gc |
| 3.17% | `python` | `_PyObject_Malloc` | memory |
| 2.11% | `python` | `_PyObject_Free` | memory |
| 1.71% | `python` | `_PyType_LookupRef` | lookup |
| 1.55% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.54% | `python` | `_Py_dict_lookup` | lookup |
| 1.31% | `python` | `initialize_locals` | interpreter |
| 1.26% | `python` | `subtype_traverse` | gc |
| 1.25% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 1.06% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.86% | `python` | `context_tp_dealloc` | memory |
| 0.77% | `python` | `_PyGC_Collect` | gc |
| 0.72% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 0.69% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.67% | `python` | `tupledealloc` | memory |
| 0.66% | `python` | `_PyEval_Vector` | interpreter |
| 0.65% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.61% | `python` | `_PyObject_GetMethod` | dynamic |
| 0.56% | `python` | `subtype_dealloc` | memory |
| 0.53% | `_asyncio.cpython-314-x86_64-linux-gnu.so` | `TaskObj_traverse` | library |
| 0.52% | `python` | `_PyFrame_Traverse` | interpreter |
| 0.52% | `python` | `PyObject_GenericGetAttr` | dynamic |
| 0.52% | `python` | `dict_traverse` | gc |
| 0.49% | `python` | `PyDict_GetItemRef` | dict |
| 0.48% | `python` | `PyObject_RichCompareBool` | dynamic |
| 0.47% | `python` | `dict_dealloc` | memory |
| 0.45% | `python` | `gen_dealloc` | memory |
| 0.43% | `python` | `PyObject_GC_Del` | gc |
| 0.42% | `python` | `_PyObject_GC_New` | gc |
| 0.41% | `python` | `_PyTuple_FromArray.part.0` | tuple |
| 0.38% | `python` | `_Py_Dealloc` | memory |
| 0.38% | `python` | `gen_traverse` | gc |
| 0.35% | `python` | `_PyObject_MakeTpCall` | dynamic |
| 0.35% | `python` | `insert_to_emptydict` | dict |
| 0.34% | `python` | `insertdict` | dict |
| 0.34% | `python` | `PyType_GenericAlloc` | memory |
| 0.34% | `python` | `_PyThreadState_PopFrame` | interpreter |
| 0.33% | `python` | `_PyArg_UnpackKeywords` | calls |
| 0.31% | `python` | `PyObject_GetAttr` | dynamic |
| 0.31% | `python` | `list_dealloc` | memory |
| 0.31% | `python` | `_PyObject_Realloc` | memory |
| 0.29% | `python` | `PyObject_IS_GC` | gc |
| 0.29% | `python` | `_PyObject_GC_Link` | gc |
| 0.27% | `python` | `list_traverse` | gc |
| 0.27% | `python` | `PyIter_Send` | dynamic |
| 0.26% | `python` | `_PyObject_Calloc` | memory |
| 0.26% | `python` | `_Py_NewReference` | memory |
| 0.26% | `python` | `dict_setdefault_ref_lock_held` | dict |
| 0.26% | `python` | `PyUnicode_RichCompare` | str |

## async_tree_memoization_tg

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 24.92% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 9.97% | `python` | `gc_collect_region.isra.0` | gc |
| 5.57% | `python` | `visit_decref` | gc |
| 5.53% | `python` | `visit_add_to_container` | gc |
| 5.15% | `python` | `visit_reachable` | gc |
| 3.29% | `python` | `_PyObject_Malloc` | memory |
| 2.02% | `python` | `_PyObject_Free` | memory |
| 1.55% | `python` | `_PyType_LookupRef` | lookup |
| 1.47% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.39% | `python` | `initialize_locals` | interpreter |
| 1.27% | `python` | `subtype_traverse` | gc |
| 1.27% | `python` | `_Py_dict_lookup` | lookup |
| 1.22% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 1.04% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.76% | `python` | `_PyEval_Vector` | interpreter |
| 0.73% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 0.72% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.71% | `python` | `_PyGC_Collect` | gc |
| 0.66% | `python` | `_PyFrame_Traverse` | interpreter |
| 0.64% | `python` | `tupledealloc` | memory |
| 0.62% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.60% | `python` | `PyObject_GenericGetAttr` | dynamic |
| 0.59% | `python` | `subtype_dealloc` | memory |
| 0.56% | `_asyncio.cpython-314-x86_64-linux-gnu.so` | `TaskObj_traverse` | library |
| 0.53% | `python` | `_PyObject_GetMethod` | dynamic |
| 0.50% | `python` | `PyObject_RichCompareBool` | dynamic |
| 0.49% | `python` | `PyDict_GetItemRef` | dict |
| 0.45% | `python` | `set_traverse` | gc |
| 0.42% | `python` | `PyObject_GC_Del` | gc |
| 0.41% | `python` | `PyType_GenericAlloc` | memory |
| 0.40% | `python` | `gen_traverse` | gc |
| 0.39% | `python` | `_PyObject_GC_New` | gc |
| 0.38% | `python` | `context_tp_dealloc` | memory |
| 0.38% | `python` | `_PyTuple_FromArray.part.0` | tuple |
| 0.37% | `python` | `_Py_Dealloc` | memory |
| 0.36% | `python` | `_PyThreadState_PopFrame` | interpreter |
| 0.34% | `python` | `PyObject_VisitManagedDict` | dynamic |
| 0.34% | `python` | `PyObject_GetAttr` | dynamic |
| 0.34% | `python` | `_PyObject_MakeTpCall` | dynamic |
| 0.33% | `python` | `dict_traverse` | gc |
| 0.32% | `python` | `_PyObject_GC_Link` | gc |
| 0.31% | `python` | `gen_dealloc` | memory |
| 0.30% | `python` | `_PyArg_UnpackKeywords` | calls |
| 0.29% | `python` | `dict_setdefault_ref_lock_held` | dict |
| 0.28% | `python` | `dict_dealloc` | memory |
| 0.28% | `python` | `set_lookkey` | miscobj |
| 0.28% | `python` | `_PyObject_Calloc` | memory |
| 0.27% | `python` | `PyUnicode_RichCompare` | str |
| 0.27% | `python` | `insert_to_emptydict` | dict |
| 0.27% | `python` | `_Py_NewReference` | memory |
| 0.26% | `_asyncio.cpython-314-x86_64-linux-gnu.so` | `TaskStepMethWrapper_call` | library |
| 0.26% | `_asyncio.cpython-314-x86_64-linux-gnu.so` | `task_step_impl` | library |
| 0.26% | `python` | `PyIter_Send` | dynamic |
| 0.26% | `python` | `insertdict` | dict |

## async_tree_tg

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 23.55% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 9.18% | `python` | `gc_collect_region.isra.0` | gc |
| 5.47% | `python` | `visit_add_to_container` | gc |
| 5.17% | `python` | `visit_decref` | gc |
| 4.92% | `python` | `visit_reachable` | gc |
| 3.71% | `python` | `_PyObject_Malloc` | memory |
| 2.43% | `python` | `_PyObject_Free` | memory |
| 1.46% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.37% | `python` | `initialize_locals` | interpreter |
| 1.37% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 1.27% | `python` | `_Py_dict_lookup` | lookup |
| 1.21% | `python` | `_PyType_LookupRef` | lookup |
| 1.14% | `python` | `subtype_traverse` | gc |
| 0.86% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.86% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 0.83% | `python` | `subtype_dealloc` | memory |
| 0.71% | `python` | `_PyFrame_Traverse` | interpreter |
| 0.67% | `python` | `tupledealloc` | memory |
| 0.67% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.66% | `python` | `_PyEval_Vector` | interpreter |
| 0.64% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.63% | `python` | `_PyGC_Collect` | gc |
| 0.61% | `python` | `PyObject_GenericGetAttr` | dynamic |
| 0.61% | `_asyncio.cpython-314-x86_64-linux-gnu.so` | `TaskObj_traverse` | library |
| 0.55% | `python` | `PyObject_RichCompareBool` | dynamic |
| 0.54% | `python` | `set_traverse` | gc |
| 0.48% | `python` | `_PyTuple_FromArray.part.0` | tuple |
| 0.46% | `python` | `PyType_GenericAlloc` | memory |
| 0.46% | `python` | `PyDict_GetItemRef` | dict |
| 0.44% | `python` | `_Py_Dealloc` | memory |
| 0.43% | `python` | `PyObject_GC_Del` | gc |
| 0.41% | `python` | `dict_traverse` | gc |
| 0.41% | `python` | `_PyObject_MakeTpCall` | dynamic |
| 0.41% | `python` | `_PyObject_GetMethod` | dynamic |
| 0.40% | `python` | `_PyObject_GC_New` | gc |
| 0.39% | `[kernel.kallsyms]` | `clear_page_erms` | kernel |
| 0.38% | `[kernel.kallsyms]` | `native_irq_return_iret` | kernel |
| 0.37% | `python` | `_PyObject_GC_Link` | gc |
| 0.35% | `python` | `gen_traverse` | gc |
| 0.35% | `python` | `_PyArg_UnpackKeywords` | calls |
| 0.35% | `python` | `PyUnicode_RichCompare` | str |
| 0.35% | `python` | `_PyThreadState_PopFrame` | interpreter |
| 0.33% | `python` | `PyObject_VisitManagedDict` | dynamic |
| 0.32% | `python` | `dict_dealloc` | memory |
| 0.32% | `python` | `dict_setdefault_ref_lock_held` | dict |
| 0.30% | `python` | `_Py_NewReference` | memory |
| 0.30% | `python` | `insert_to_emptydict` | dict |
| 0.29% | `python` | `PyObject_GetAttr` | dynamic |
| 0.29% | `python` | `_PyObject_Calloc` | memory |
| 0.28% | `[kernel.kallsyms]` | `rmqueue` | kernel |
| 0.27% | `[kernel.kallsyms]` | `sync_regs` | kernel |
| 0.27% | `python` | `insertdict` | dict |
| 0.27% | `python` | `gen_dealloc` | memory |

## asyncio_tcp

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 32.42% | `[kernel.kallsyms]` | `copy_user_enhanced_fast_string` | kernel |
| 16.79% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 9.08% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 8.12% | `[kernel.kallsyms]` | `clear_page_erms` | kernel |
| 0.71% | `python` | `_PyObject_Malloc` | memory |
| 0.60% | `[kernel.kallsyms]` | `tcp_sendmsg_locked` | kernel |
| 0.59% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.56% | `[kernel.kallsyms]` | `native_irq_return_iret` | kernel |
| 0.52% | `python` | `_PyType_LookupRef` | lookup |
| 0.49% | `python` | `_PyObject_Free` | memory |
| 0.49% | `[kernel.kallsyms]` | `rmqueue` | kernel |
| 0.47% | `python` | `_Py_dict_lookup` | lookup |
| 0.37% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 0.36% | `[kernel.kallsyms]` | `prep_new_page` | kernel |
| 0.36% | `[kernel.kallsyms]` | `_raw_spin_lock` | kernel |
| 0.34% | `python` | `gc_collect_region.isra.0` | gc |
| 0.31% | `[kernel.kallsyms]` | `skb_release_data` | kernel |
| 0.31% | `[kernel.kallsyms]` | `sync_regs` | kernel |
| 0.30% | `[kernel.kallsyms]` | `__free_pages_ok` | kernel |
| 0.28% | `libc-2.31.so` | `pthread_attr_setschedparam` | libc |
| 0.26% | `python` | `PyObject_GetAttr` | dynamic |

## asyncio_tcp_ssl

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 39.83% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 25.82% | `libcrypto.so.1.1` | `CRYPTO_secure_actual_size` | libc |
| 10.49% | `[kernel.kallsyms]` | `copy_user_enhanced_fast_string` | kernel |
| 3.57% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 2.89% | `[kernel.kallsyms]` | `clear_page_erms` | kernel |
| 0.91% | `libssl.so.1.1` | `SSL_rstate_string` | library |
| 0.56% | `libc-2.31.so` | `pthread_attr_setschedparam` | libc |
| 0.44% | `libssl.so.1.1` | `DTLSv1_client_method` | library |
| 0.44% | `libcrypto.so.1.1` | `AES_unwrap_key` | libc |
| 0.31% | `python` | `_PyObject_Malloc` | memory |
| 0.27% | `libcrypto.so.1.1` | `CRYPTO_gcm128_release` | libc |
| 0.26% | `python` | `_PyType_LookupRef` | lookup |

## asyncio_websockets

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 65.85% | `libz.so.1.2.11` | `crc32_combine64` | library |
| 20.82% | `libz.so.1.2.11` | `inflateBackEnd` | library |
| 2.80% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.35% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 0.43% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.41% | `libz.so.1.2.11` | `inflateCodesUsed` | library |
| 0.35% | `python` | `gc_collect_region.isra.0` | gc |
| 0.27% | `python` | `_PyObject_Malloc` | memory |

## bpe_tokeniser

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 26.14% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 5.05% | `python` | `_Py_dict_lookup` | lookup |
| 4.70% | `python` | `tupledealloc` | memory |
| 3.99% | `python` | `_PyObject_Free` | memory |
| 3.08% | `python` | `_PyObject_Malloc` | memory |
| 2.83% | `python` | `list_dealloc` | memory |
| 2.34% | `python` | `_PyTuple_FromArray.part.0` | tuple |
| 1.88% | `python` | `PyTuple_New` | memory |
| 1.87% | `python` | `listiter_next` | list |
| 1.83% | `python` | `PyObject_GC_UnTrack` | gc |
| 1.74% | `python` | `_PyType_LookupRef` | lookup |
| 1.66% | `python` | `gc_collect_region.isra.0` | gc |
| 1.64% | `python` | `PyObject_RichCompareBool` | dynamic |
| 1.58% | `python` | `zip_next` | unknown |
| 1.45% | `python` | `PyList_New` | memory |
| 1.24% | `python` | `PySlice_AdjustIndices` | miscobj |
| 1.18% | `python` | `_Py_Dealloc` | memory |
| 1.07% | `python` | `tuplerichcompare` | tuple |
| 1.05% | `python` | `tuplehash` | tuple |
| 0.98% | `python` | `visit_reachable` | gc |
| 0.94% | `python` | `_PyObject_GC_New` | gc |
| 0.93% | `python` | `_PyObject_MakeTpCall` | dynamic |
| 0.88% | `python` | `visit_decref` | gc |
| 0.87% | `python` | `_Py_NewReference` | memory |
| 0.86% | `python` | `list_slice_lock_held.isra.0` | list |
| 0.86% | `python` | `PyObject_GC_Del` | gc |
| 0.85% | `python` | `PyObject_Hash` | dynamic |
| 0.85% | `python` | `_PyLong_Add` | int |
| 0.85% | `python` | `insertdict` | dict |
| 0.85% | `python` | `_PyBuildSlice_ConsumeRefs` | miscobj |
| 0.83% | `python` | `list_subscript` | list |
| 0.82% | `python` | `list_traverse` | gc |
| 0.82% | `python` | `PyObject_GetItem` | dynamic |
| 0.77% | `python` | `_PyLong_Subtract` | int |
| 0.74% | `python` | `_PyTuple_FromStackRefSteal` | tuple |
| 0.66% | `python` | `slot_mp_subscript` | unknown |
| 0.64% | `python` | `slice_dealloc` | memory |
| 0.60% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 0.59% | `python` | `PyType_GenericAlloc` | memory |
| 0.58% | `python` | `zip_new` | memory |
| 0.55% | `python` | `dict_subscript` | dict |
| 0.50% | `python` | `_PyObject_LookupSpecial` | dynamic |
| 0.47% | `python` | `method_vectorcall_O` | calls |
| 0.47% | `python` | `list_iter` | list |
| 0.46% | `python` | `_PyObject_GC_Link` | gc |
| 0.46% | `python` | `PySlice_Unpack` | miscobj |
| 0.45% | `python` | `PyObject_GetIter` | dynamic |
| 0.43% | `python` | `PyLong_FromSsize_t` | int |
| 0.40% | `python` | `PyNumber_AsSsize_t` | dynamic |
| 0.39% | `python` | `vectorcall_method` | calls |
| 0.39% | `python` | `listiter_dealloc` | memory |
| 0.39% | `python` | `wrapperdescr_call` | unknown |
| 0.38% | `python` | `_PyEval_SliceIndex` | interpreter |
| 0.37% | `python` | `initialize_locals` | interpreter |
| 0.36% | `python` | `visit_add_to_container` | gc |
| 0.35% | `python` | `PyArg_UnpackTuple` | calls |
| 0.34% | `python` | `dictiter_iternextkey` | dict |
| 0.33% | `python` | `PyObject_RichCompare` | dynamic |
| 0.33% | `python` | `_PyObject_Realloc` | memory |
| 0.32% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.31% | `python` | `dict_ass_sub` | dict |
| 0.30% | `python` | `_PyList_AppendTakeRefListResize` | list |
| 0.29% | `python` | `PyObject_SetItem` | dynamic |
| 0.28% | `python` | `type_call` | dynamic |
| 0.27% | `python` | `bytes_richcompare` | str |
| 0.27% | `python` | `PyThreadState_Get` | unknown |
| 0.27% | `python` | `PyObject_Size` | dynamic |
| 0.27% | `python` | `PyObject_Vectorcall` | dynamic |
| 0.25% | `python` | `_Py_CheckFunctionResult` | calls |
| 0.25% | `python` | `PyType_IsSubtype` | dynamic |

## chaos

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 46.27% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 2.68% | `python` | `_PyObject_Malloc` | memory |
| 2.55% | `python` | `_PyObject_Free` | memory |
| 2.15% | `python` | `_PyLong_Subtract` | int |
| 2.05% | `python` | `PyType_IsSubtype` | dynamic |
| 1.88% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.52% | `python` | `_PyLong_Add` | int |
| 1.32% | `python` | `float_div` | float |
| 1.30% | `python` | `float_dealloc` | memory |
| 1.23% | `python` | `float_richcompare` | float |
| 1.21% | `python` | `PyLong_AsDouble` | int |
| 1.09% | `python` | `compute_range_length` | unknown |
| 1.02% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.95% | `python` | `float_sub` | float |
| 0.95% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 0.92% | `libm-2.31.so` | `f64xsubf128` | library |
| 0.89% | `python` | `range_iter` | miscobj |
| 0.84% | `python` | `_PyType_NewManagedObject` | memory |
| 0.78% | `python` | `PyFloat_FromDouble` | float |
| 0.78% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.77% | `python` | `_Py_NewReference` | memory |
| 0.72% | `python` | `subtype_dealloc` | memory |
| 0.70% | `python` | `gc_collect_region.isra.0` | gc |
| 0.69% | `python` | `float_pow` | float |
| 0.65% | `python` | `PyNumber_Subtract` | dynamic |
| 0.64% | `python` | `PyObject_ClearManagedDict` | dynamic |
| 0.60% | `python` | `_Py_Dealloc` | memory |
| 0.58% | `python` | `_PyType_LookupRef` | lookup |
| 0.58% | `python` | `PyNumber_TrueDivide` | dynamic |
| 0.55% | `python` | `_Py_dict_lookup` | lookup |
| 0.52% | `python` | `PyLong_FromLong` | int |
| 0.52% | `python` | `PyLong_AsLongAndOverflow` | int |
| 0.47% | `python` | `initialize_locals` | interpreter |
| 0.47% | `python` | `tupledealloc` | memory |
| 0.43% | `python` | `PyObject_GC_Del` | gc |
| 0.42% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.41% | `python` | `_PyThreadState_PopFrame` | interpreter |
| 0.41% | `python` | `PyObject_RichCompare` | dynamic |
| 0.41% | `python` | `visit_decref` | gc |
| 0.37% | `python` | `PyLong_AsLong` | int |
| 0.36% | `python` | `range_vectorcall` | miscobj |
| 0.33% | `python` | `_PyTuple_FromStackRefSteal` | tuple |
| 0.31% | `python` | `PyObject_ClearWeakRefs` | dynamic |
| 0.30% | `python` | `_PyObject_GC_Link` | gc |
| 0.29% | `python` | `r_object` | import |
| 0.28% | `python` | `_PyObject_New` | memory |
| 0.28% | `python` | `list_dealloc` | memory |
| 0.27% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.27% | `python` | `PyNumber_Index` | dynamic |
| 0.27% | `python` | `visit_reachable` | gc |
| 0.26% | `python` | `_PyFloat_ExactDealloc` | memory |
| 0.25% | `python` | `float_mul` | float |

## comprehensions

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 38.24% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 6.87% | `python` | `_Py_dict_lookup` | lookup |
| 3.69% | `python` | `_PyObject_Free` | memory |
| 3.68% | `python` | `_PyObject_Malloc` | memory |
| 2.22% | `python` | `dict_get` | dict |
| 1.87% | `python` | `PyObject_RichCompareBool` | dynamic |
| 1.72% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 1.46% | `python` | `PyDict_GetItemRef` | dict |
| 1.36% | `python` | `_PyObject_Realloc` | memory |
| 1.14% | `python` | `insertdict` | dict |
| 1.08% | `python` | `long_richcompare` | int |
| 1.04% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.00% | `python` | `PyFunction_NewWithQualName` | memory |
| 1.00% | `python` | `PyObject_GC_Del` | gc |
| 0.98% | `python` | `list_dealloc` | memory |
| 0.96% | `python` | `_PyType_LookupRef` | lookup |
| 0.96% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 0.91% | `python` | `PyObject_Hash` | dynamic |
| 0.85% | `python` | `_PyObject_GC_New` | gc |
| 0.82% | `python` | `tupledealloc` | memory |
| 0.79% | `python` | `unsafe_tuple_compare` | unknown |
| 0.78% | `python` | `gc_collect_region.isra.0` | gc |
| 0.76% | `python` | `_PyList_AppendTakeRefListResize` | list |
| 0.73% | `python` | `long_hash` | int |
| 0.61% | `python` | `list_sort_impl` | list |
| 0.60% | `python` | `gen_dealloc` | memory |
| 0.60% | `python` | `func_dealloc` | memory |
| 0.58% | `python` | `_PyTuple_FromStackRefSteal` | tuple |
| 0.49% | `python` | `PyObject_RichCompare` | dynamic |
| 0.49% | `python` | `list_iter` | list |
| 0.46% | `python` | `_Py_Dealloc` | memory |
| 0.45% | `python` | `dict_dealloc` | memory |
| 0.42% | `python` | `listiter_dealloc` | memory |
| 0.42% | `python` | `visit_decref` | gc |
| 0.42% | `python` | `func_clear` | unknown |
| 0.41% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.39% | `python` | `gen_iternext` | miscobj |
| 0.39% | `python` | `PyList_New` | memory |
| 0.38% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.38% | `python` | `_PyObject_GC_Link` | gc |
| 0.35% | `python` | `r_object` | import |
| 0.34% | `python` | `builtin_any` | unknown |
| 0.34% | `python` | `visit_reachable` | gc |
| 0.33% | `python` | `_Py_type_getattro` | lookup |
| 0.33% | `python` | `PyObject_GetIter` | dynamic |
| 0.33% | `python` | `_PyDict_SetItem_Take2` | dict |
| 0.32% | `python` | `PyObject_IsTrue` | dynamic |
| 0.31% | `python` | `_Py_NewReference` | memory |
| 0.30% | `python` | `_PyThreadState_PopFrame` | interpreter |
| 0.30% | `python` | `_PyObject_GC_NewVar` | gc |
| 0.29% | `python` | `find_name_in_mro` | lookup |
| 0.28% | `python` | `tuplesubscript` | tuple |
| 0.28% | `python` | `unsafe_object_compare` | unknown |
| 0.25% | `python` | `PyObject_GetAttr` | dynamic |

## concurrent_imap

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 20.52% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 2.90% | `python` | `_PyObject_Free` | memory |
| 1.86% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.68% | `python` | `_PyObject_Malloc` | memory |
| 1.54% | `[kernel.kallsyms]` | `perf_event_alloc` | kernel |
| 1.36% | `python` | `_PyType_LookupRef` | lookup |
| 1.33% | `[kernel.kallsyms]` | `memset_erms` | kernel |
| 1.16% | `libc-2.31.so` | `pthread_attr_setschedparam` | libc |
| 1.15% | `python` | `tupledealloc` | memory |
| 1.02% | `python` | `subtype_dealloc` | memory |
| 1.01% | `python` | `initialize_locals` | interpreter |
| 0.96% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.94% | `[kernel.kallsyms]` | `clear_page_erms` | kernel |
| 0.88% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 0.83% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.81% | `[kernel.kallsyms]` | `psi_task_change` | kernel |
| 0.80% | `python` | `PyObject_ClearManagedDict` | dynamic |
| 0.77% | `python` | `_Py_Dealloc` | memory |
| 0.75% | `python` | `_Py_dict_lookup` | lookup |
| 0.72% | `[kernel.kallsyms]` | `mutex_unlock` | kernel |
| 0.70% | `[kernel.kallsyms]` | `update_load_avg` | kernel |
| 0.65% | `libc-2.31.so` | `free` | libc |
| 0.62% | `[kernel.kallsyms]` | `mutex_lock` | kernel |
| 0.58% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.56% | `[kernel.kallsyms]` | `inherit_event.isra.0` | kernel |
| 0.55% | `python` | `PyObject_GC_Del` | gc |
| 0.54% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.51% | `python` | `PyObject_GetAttr` | dynamic |
| 0.50% | `python` | `PyObject_GenericGetAttr` | dynamic |
| 0.49% | `python` | `dict_dealloc` | memory |
| 0.47% | `[kernel.kallsyms]` | `_raw_spin_lock_irqsave` | kernel |
| 0.47% | `[kernel.kallsyms]` | `_raw_spin_lock` | kernel |
| 0.44% | `python` | `list_dealloc` | memory |
| 0.43% | `[kernel.kallsyms]` | `kfree` | kernel |
| 0.43% | `[kernel.kallsyms]` | `copy_page` | kernel |
| 0.41% | `[kernel.kallsyms]` | `syscall_return_via_sysret` | kernel |
| 0.41% | `[kernel.kallsyms]` | `page_counter_cancel` | kernel |
| 0.38% | `[kernel.kallsyms]` | `find_vma` | kernel |
| 0.37% | `[kernel.kallsyms]` | `update_cfs_group` | kernel |
| 0.37% | `python` | `PyObject_Vectorcall` | dynamic |
| 0.35% | `[kernel.kallsyms]` | `native_sched_clock` | kernel |
| 0.35% | `[kernel.kallsyms]` | `enqueue_task_fair` | kernel |
| 0.35% | `libpthread-2.31.so` | `__pthread_mutex_lock` | library |
| 0.35% | `python` | `gc_collect_region.isra.0` | gc |
| 0.35% | `python` | `_PyTuple_FromArray.part.0` | tuple |
| 0.34% | `python` | `PyType_GenericAlloc` | memory |
| 0.32% | `[kernel.kallsyms]` | `zap_pte_range.isra.0` | kernel |
| 0.32% | `python` | `_PyObject_LookupSpecialMethod` | dynamic |
| 0.32% | `libpthread-2.31.so` | `pthread_mutex_unlock` | library |
| 0.31% | `[vdso]` | `__vdso_clock_gettime` | unknown |
| 0.31% | `python` | `_PyTuple_FromStackRefSteal` | tuple |
| 0.30% | `python` | `_PyParkingLot_Unpark` | unknown |
| 0.30% | `libpthread-2.31.so` | `__nptl_deallocate_tsd.part.0` | library |
| 0.30% | `[kernel.kallsyms]` | `rb_insert_color` | kernel |
| 0.30% | `[kernel.kallsyms]` | `account_kernel_stack` | kernel |
| 0.29% | `[kernel.kallsyms]` | `reweight_entity` | kernel |
| 0.28% | `[kernel.kallsyms]` | `__lock_text_start` | kernel |
| 0.27% | `[kernel.kallsyms]` | `native_flush_tlb_one_user` | kernel |
| 0.26% | `python` | `_PyThreadState_PopFrame` | interpreter |
| 0.26% | `python` | `PyObject_IsTrue` | dynamic |
| 0.26% | `[kernel.kallsyms]` | `__fget_light` | kernel |
| 0.25% | `python` | `PyObject_ClearWeakRefs` | dynamic |
| 0.25% | `python` | `PyDict_GetItemRef` | dict |

## coroutines

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 47.17% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 6.21% | `python` | `gen_dealloc` | memory |
| 4.76% | `python` | `_PyObject_Malloc` | memory |
| 4.48% | `python` | `_PyObject_Free` | memory |
| 3.32% | `python` | `_PyObject_GC_NewVar` | gc |
| 2.76% | `python` | `make_gen` | miscobj |
| 2.33% | `python` | `_PyLong_Subtract` | int |
| 2.29% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.85% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.83% | `python` | `PyObject_CallFinalizerFromDealloc` | memory |
| 1.73% | `python` | `_PyLong_Add` | int |
| 1.49% | `python` | `PyObject_GC_Del` | gc |
| 1.33% | `python` | `_Py_MakeCoro` | unknown |
| 0.95% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.89% | `python` | `_PyObject_GC_Link` | gc |
| 0.89% | `python` | `_PyCoro_GetAwaitableIter` | unknown |
| 0.84% | `python` | `_PyThreadState_PopFrame` | interpreter |
| 0.79% | `python` | `gc_collect_region.isra.0` | gc |
| 0.51% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 0.50% | `python` | `_Py_NewReference` | memory |
| 0.42% | `python` | `_Py_dict_lookup` | lookup |
| 0.39% | `python` | `_PyGen_Finalize` | miscobj |
| 0.38% | `python` | `PyObject_Malloc` | dynamic |
| 0.36% | `python` | `r_object` | import |
| 0.36% | `python` | `visit_decref` | gc |
| 0.32% | `python` | `visit_reachable` | gc |
| 0.28% | `python` | `find_name_in_mro` | lookup |

## coverage

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 14.96% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 6.29% | `tracer.cpython-314-x86_64-linux-gnu.so` | `CTracer_trace` | library |
| 6.22% | `python` | `call_instrumentation_vector.part.0` | interpreter |
| 5.69% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 4.06% | `python` | `_Py_dict_lookup` | lookup |
| 3.37% | `python` | `_Py_call_instrumentation_line` | interpreter |
| 2.95% | `python` | `_PyObject_Free` | memory |
| 2.90% | `python` | `_PyObject_Malloc` | memory |
| 2.78% | `python` | `siphash13` | str |
| 1.72% | `python` | `PyDict_GetItem` | dict |
| 1.47% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.47% | `python` | `gc_collect_region.isra.0` | gc |
| 1.42% | `python` | `set_add_entry` | miscobj |
| 1.34% | `python` | `PyLong_FromLong` | int |
| 1.14% | `python` | `_Py_hashtable_get_entry_generic` | lookup |
| 1.10% | `python` | `_PyType_LookupRef` | lookup |
| 0.94% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 0.86% | `python` | `ascii_decode` | str |
| 0.83% | `python` | `PyObject_GenericSetAttr` | dynamic |
| 0.82% | `python` | `PyObject_GC_Del` | gc |
| 0.81% | `python` | `visit_decref` | gc |
| 0.78% | `python` | `dict_setdefault_ref_lock_held` | dict |
| 0.72% | `python` | `intern_common.part.0` | str |
| 0.72% | `python` | `_PyObject_GC_NewVar` | gc |
| 0.71% | `python` | `visit_reachable` | gc |
| 0.69% | `python` | `frame_dealloc` | memory |
| 0.69% | `python` | `PySet_Add` | miscobj |
| 0.63% | `python` | `_PyCode_GetCode` | interpreter |
| 0.62% | `python` | `unicode_decode_utf8.part.0` | str |
| 0.62% | `python` | `PyUnicode_New.part.0` | memory |
| 0.61% | `python` | `sys_trace_return` | library |
| 0.57% | `python` | `sys_trace_start` | library |
| 0.57% | `python` | `_Py_Dealloc` | memory |
| 0.55% | `python` | `r_object` | import |
| 0.54% | `python` | `_PyDict_LoadGlobal` | dict |
| 0.52% | `python` | `PyObject_Hash` | dynamic |
| 0.45% | `python` | `PyEval_GetFrame` | interpreter |
| 0.42% | `tracer.cpython-314-x86_64-linux-gnu.so` | `CTracer_set_pdata_stack` | library |
| 0.42% | `python` | `PyObject_SetAttr` | dynamic |
| 0.42% | `python` | `PyFrame_GetCode` | exceptions |
| 0.41% | `python` | `_PyLong_Subtract` | int |
| 0.40% | `python` | `unicode_dealloc` | memory |
| 0.40% | `python` | `_Py_call_instrumentation_arg` | unknown |
| 0.40% | `python` | `PyObject_SetAttrString` | dynamic |
| 0.39% | `python` | `PyUnicode_InternFromString` | str |
| 0.38% | `python` | `find_name_in_mro` | lookup |
| 0.38% | `python` | `update_one_slot` | lookup |
| 0.35% | `python` | `_PyLong_Add` | int |
| 0.34% | `python` | `_Py_CheckFunctionResult` | calls |
| 0.34% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.32% | `python` | `_PyCode_Quicken` | interpreter |
| 0.30% | `python` | `long_hash` | int |
| 0.30% | `python` | `tupledealloc` | memory |
| 0.29% | `python` | `_PyType_GetDict` | dynamic |
| 0.28% | `python` | `dict_traverse` | gc |
| 0.28% | `libc-2.31.so` | `pthread_attr_setschedparam` | libc |
| 0.28% | `python` | `_Py_hashtable_get` | lookup |
| 0.27% | `python` | `_PyObject_GC_Link` | gc |
| 0.27% | `python` | `PyFrame_GetLineNumber` | exceptions |

## crypto_pyaes

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 34.01% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 9.00% | `python` | `_PyObject_Free` | memory |
| 7.99% | `python` | `long_bitwise` | int |
| 7.81% | `python` | `_PyObject_Malloc` | memory |
| 3.49% | `python` | `long_rshift1` | int |
| 3.26% | `python` | `l_mod` | int |
| 1.71% | `python` | `long_rshift` | int |
| 1.67% | `python` | `long_and` | int |
| 1.38% | `python` | `PyNumber_And` | dynamic |
| 1.15% | `python` | `PyLong_FromLong` | int |
| 1.15% | `python` | `_PyLong_Add` | int |
| 1.15% | `python` | `long_xor` | int |
| 1.15% | `python` | `PyNumber_Xor` | dynamic |
| 1.11% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 0.97% | `python` | `long_dealloc` | memory |
| 0.95% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.87% | `python` | `PyNumber_Rshift` | dynamic |
| 0.75% | `python` | `_Py_NewReference` | memory |
| 0.71% | `python` | `gc_collect_region.isra.0` | gc |
| 0.71% | `python` | `long_mod` | int |
| 0.71% | `python` | `_Py_dict_lookup` | lookup |
| 0.63% | `python` | `PyNumber_Remainder` | dynamic |
| 0.62% | `python` | `PyObject_Malloc` | dynamic |
| 0.58% | `python` | `compute_range_length` | unknown |
| 0.57% | `python` | `list_dealloc` | memory |
| 0.52% | `python` | `PyLong_AsSsize_t` | int |
| 0.46% | `python` | `_Py_Dealloc` | memory |
| 0.45% | `python` | `range_iter` | miscobj |
| 0.41% | `python` | `PyObject_Free` | dynamic |
| 0.39% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 0.37% | `python` | `visit_decref` | gc |
| 0.32% | `python` | `r_object` | import |
| 0.27% | `python` | `PyList_New` | memory |
| 0.27% | `python` | `PyLong_AsLongAndOverflow` | int |
| 0.27% | `python` | `visit_reachable` | gc |

## dask

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 24.13% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 3.90% | `python` | `gc_collect_region.isra.0` | gc |
| 3.13% | `python` | `_PyObject_Malloc` | memory |
| 2.60% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 2.48% | `python` | `visit_decref` | gc |
| 2.43% | `python` | `_PyObject_Free` | memory |
| 1.90% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.83% | `python` | `visit_reachable` | gc |
| 1.78% | `python` | `_Py_dict_lookup` | lookup |
| 1.41% | `python` | `visit_add_to_container` | gc |
| 1.40% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.30% | `python` | `tupledealloc` | memory |
| 1.14% | `python` | `_PyType_LookupRef` | lookup |
| 1.13% | `python` | `initialize_locals` | interpreter |
| 0.97% | `python` | `dict_dealloc` | memory |
| 0.90% | `python` | `PyBytes_Repr` | str |
| 0.73% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.55% | `libc-2.31.so` | `pthread_attr_setschedparam` | libc |
| 0.54% | `python` | `insertdict` | dict |
| 0.53% | `python` | `_Py_Dealloc` | memory |
| 0.51% | `python` | `PyDict_GetItemRef` | dict |
| 0.51% | `python` | `siphash13` | str |
| 0.46% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.45% | `python` | `dict_traverse` | gc |
| 0.44% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.44% | `python` | `PyObject_RichCompareBool` | dynamic |
| 0.42% | `python` | `PyObject_GC_Del` | gc |
| 0.42% | `python` | `set_traverse` | gc |
| 0.39% | `python` | `_PyObject_GC_New` | gc |
| 0.38% | `python` | `_PyTuple_FromArray.part.0` | tuple |
| 0.38% | `python` | `PyObject_IS_GC` | gc |
| 0.37% | `python` | `_PyTuple_FromStackRefSteal` | tuple |
| 0.35% | `python` | `r_object` | import |
| 0.35% | `python` | `_PyDict_FromItems` | dict |
| 0.34% | `python` | `list_dealloc` | memory |
| 0.34% | `libcrypto.so.1.1` | `MD4` | libc |
| 0.33% | `_cmsgpack.cpython-314-x86_64-linux-gnu.so` | `__pyx_f_7msgpack_9_cmsgpack_6Packer__pack` | library |
| 0.33% | `python` | `_PyPegen_is_memoized` | interpreter |
| 0.32% | `python` | `_Py_hashtable_get_entry_generic` | lookup |
| 0.32% | `python` | `PyType_IsSubtype` | dynamic |
| 0.32% | `python` | `PyType_GenericAlloc` | memory |
| 0.32% | `python` | `dict_merge` | dict |
| 0.31% | `python` | `insert_to_emptydict` | dict |
| 0.31% | `python` | `tupletraverse` | tuple |
| 0.29% | `python` | `_PyObject_Calloc` | memory |
| 0.27% | `python` | `_Py_NewReference` | memory |
| 0.27% | `python` | `PyObject_Vectorcall` | dynamic |
| 0.27% | `python` | `setiter_iternext` | miscobj |

## deepcopy

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 37.04% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 4.22% | `python` | `_PyObject_Malloc` | memory |
| 3.97% | `python` | `initialize_locals` | interpreter |
| 3.93% | `python` | `_Py_dict_lookup` | lookup |
| 3.83% | `python` | `_PyObject_Free` | memory |
| 2.97% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.79% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 1.44% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 1.30% | `python` | `set_lookkey` | miscobj |
| 1.08% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.08% | `python` | `_PyType_LookupRef` | lookup |
| 0.94% | `python` | `insertdict` | dict |
| 0.92% | `python` | `PyLong_FromVoidPtr` | int |
| 0.90% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.83% | `python` | `tupledealloc` | memory |
| 0.78% | `python` | `_PyObject_Realloc` | memory |
| 0.77% | `python` | `dict_get` | dict |
| 0.74% | `python` | `insert_to_emptydict` | dict |
| 0.70% | `python` | `_Py_Dealloc` | memory |
| 0.66% | `python` | `_PyThreadState_PushFrame` | interpreter |
| 0.64% | `python` | `list_append` | list |
| 0.62% | `python` | `PyObject_Hash` | dynamic |
| 0.60% | `python` | `long_hash` | int |
| 0.60% | `python` | `gc_collect_region.isra.0` | gc |
| 0.59% | `python` | `dict_dealloc` | memory |
| 0.58% | `python` | `PyObject_GC_Del` | gc |
| 0.58% | `python` | `PyObject_RichCompareBool` | dynamic |
| 0.57% | `python` | `long_richcompare` | int |
| 0.56% | `python` | `dictiter_iternextitem` | dict |
| 0.56% | `python` | `sys_audit_tstate` | unknown |
| 0.55% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.55% | `python` | `_PyObject_GC_New` | gc |
| 0.53% | `python` | `list_dealloc` | memory |
| 0.52% | `python` | `_PySet_Contains` | miscobj |
| 0.51% | `python` | `_PyObject_GenericGetAttrWithDict` | dynamic |
| 0.48% | `python` | `PyDict_GetItemRef` | dict |
| 0.48% | `python` | `PySys_Audit` | unknown |
| 0.43% | `python` | `_PyThreadState_PopFrame` | interpreter |
| 0.41% | `python` | `_PyDict_SetItem_Take2` | dict |
| 0.41% | `python` | `_Py_NewReference` | memory |
| 0.35% | `python` | `_PyTuple_FromArray.part.0` | tuple |
| 0.35% | `python` | `visit_decref` | gc |
| 0.33% | `python` | `_PyObject_Calloc` | memory |
| 0.32% | `libc-2.31.so` | `pthread_attr_setschedparam` | libc |
| 0.32% | `python` | `PyType_GenericAlloc` | memory |
| 0.30% | `python` | `dict_merge` | dict |
| 0.29% | `python` | `PyObject_GenericGetAttr` | dynamic |
| 0.29% | `python` | `_PyObject_GC_Link` | gc |
| 0.27% | `python` | `builtin_id` | unknown |
| 0.27% | `python` | `PyObject_GetAttr` | dynamic |
| 0.27% | `python` | `r_object` | import |
| 0.26% | `python` | `visit_reachable` | gc |

## deltablue

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 57.43% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 3.74% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 2.36% | `python` | `_PyObject_Malloc` | memory |
| 2.30% | `python` | `gc_collect_region.isra.0` | gc |
| 2.13% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.92% | `python` | `_PyObject_Free` | memory |
| 1.78% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 1.57% | `python` | `_PyType_LookupRef` | lookup |
| 1.21% | `python` | `_PyThreadState_PopFrame` | interpreter |
| 0.96% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 0.90% | `python` | `visit_decref` | gc |
| 0.68% | `python` | `_Py_dict_lookup` | lookup |
| 0.66% | `python` | `_PyObject_GetMethod` | dynamic |
| 0.48% | `python` | `visit_reachable` | gc |
| 0.38% | `python` | `r_object` | import |
| 0.37% | `python` | `_Py_type_getattro` | lookup |
| 0.36% | `python` | `PyDict_GetItemRef` | dict |
| 0.35% | `python` | `_PyObject_GC_New` | gc |
| 0.34% | `python` | `subtype_dealloc` | memory |
| 0.32% | `python` | `tupledealloc` | memory |
| 0.31% | `python` | `initialize_locals` | interpreter |
| 0.29% | `python` | `method_dealloc` | memory |
| 0.27% | `libc-2.31.so` | `pthread_attr_setschedparam` | libc |
| 0.27% | `python` | `PyObject_GC_Del` | gc |
| 0.27% | `python` | `_PyLong_Add` | int |
| 0.26% | `python` | `_PyObject_TryGetInstanceAttribute` | dynamic |

## django_template

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 33.27% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 3.33% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 3.19% | `python` | `_PyObject_Malloc` | memory |
| 3.16% | `python` | `_PyObject_Free` | memory |
| 2.31% | `python` | `_PyType_LookupRef` | lookup |
| 1.95% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.90% | `python` | `_Py_dict_lookup` | lookup |
| 1.65% | `python` | `gc_collect_region.isra.0` | gc |
| 1.41% | `python` | `initialize_locals` | interpreter |
| 1.33% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.25% | `python` | `_PyObject_GenericGetAttrWithDict` | dynamic |
| 1.16% | `python` | `replace` | str |
| 0.91% | `python` | `tupledealloc` | memory |
| 0.89% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.84% | `python` | `visit_decref` | gc |
| 0.83% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.77% | `python` | `insertdict` | dict |
| 0.72% | `python` | `PyObject_GC_Del` | gc |
| 0.70% | `python` | `PyType_IsSubtype` | dynamic |
| 0.67% | `python` | `_PyObject_GC_New` | gc |
| 0.64% | `python` | `visit_reachable` | gc |
| 0.59% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.57% | `python` | `_Py_Dealloc` | memory |
| 0.56% | `python` | `r_object` | import |
| 0.52% | `python` | `PyObject_GetOptionalAttr` | dynamic |
| 0.49% | `python` | `find_name_in_mro` | lookup |
| 0.49% | `python` | `list_dealloc` | memory |
| 0.47% | `python` | `dict_dealloc` | memory |
| 0.46% | `python` | `long_to_decimal_string_internal` | int |
| 0.44% | `python` | `PyDict_GetItemRef` | dict |
| 0.43% | `libc-2.31.so` | `pthread_attr_setschedparam` | libc |
| 0.42% | `python` | `_PyTuple_FromArray.part.0` | tuple |
| 0.41% | `python` | `_PyObject_GC_Link` | gc |
| 0.41% | `python` | `update_one_slot` | lookup |
| 0.41% | `python` | `_PyThreadState_PopFrame` | interpreter |
| 0.36% | `python` | `_Py_NewReference` | memory |
| 0.35% | `python` | `PyType_GenericAlloc` | memory |
| 0.35% | `python` | `PyFunction_NewWithQualName` | memory |
| 0.35% | `python` | `object_isinstance` | dynamic |
| 0.34% | `libz.so.1.2.11` | `inflateBackEnd` | library |
| 0.34% | `python` | `siphash13` | str |
| 0.33% | `python` | `_PyObject_GetMethod` | dynamic |
| 0.33% | `python` | `_PyCode_Quicken` | interpreter |
| 0.32% | `python` | `_PyType_GetDict` | dynamic |
| 0.31% | `python` | `_Py_hashtable_get_entry_generic` | lookup |
| 0.30% | `python` | `_PyObject_Calloc` | memory |
| 0.30% | `python` | `_PyTuple_FromStackRefSteal` | tuple |
| 0.28% | `python` | `_PyThreadState_PushFrame` | interpreter |
| 0.27% | `python` | `_PyPegen_is_memoized` | interpreter |
| 0.26% | `python` | `PyObject_GetIter` | dynamic |
| 0.26% | `python` | `unicode_replace` | str |
| 0.26% | `python` | `_PyUnicode_FromUCS1.part.0` | str |
| 0.25% | `python` | `getset_get` | dynamic |

## docutils

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 23.85% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 6.51% | `python` | `sre_ucs1_match` | library |
| 6.17% | `python` | `gc_collect_region.isra.0` | gc |
| 3.72% | `python` | `_PyObject_Malloc` | memory |
| 3.12% | `python` | `_PyObject_Free` | memory |
| 3.03% | `python` | `_PyType_LookupRef` | lookup |
| 3.02% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 1.97% | `python` | `visit_add_to_container` | gc |
| 1.89% | `python` | `_Py_dict_lookup` | lookup |
| 1.86% | `python` | `visit_decref` | gc |
| 1.86% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.81% | `python` | `sre_ucs2_charset.isra.0` | library |
| 1.33% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.32% | `python` | `list_dealloc` | memory |
| 1.18% | `python` | `PyObject_GenericGetAttr` | dynamic |
| 0.95% | `python` | `dict_traverse` | gc |
| 0.94% | `python` | `visit_reachable` | gc |
| 0.82% | `python` | `initialize_locals` | interpreter |
| 0.71% | `python` | `_PyObject_TryGetInstanceAttribute` | dynamic |
| 0.71% | `python` | `tupledealloc` | memory |
| 0.62% | `python` | `list_traverse` | gc |
| 0.62% | `python` | `PyObject_GetAttr` | dynamic |
| 0.61% | `libc-2.31.so` | `pthread_attr_setschedparam` | libc |
| 0.59% | `python` | `_PyObject_GetMethod` | dynamic |
| 0.57% | `python` | `PyType_IsSubtype` | dynamic |
| 0.57% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.54% | `python` | `dict_dealloc` | memory |
| 0.51% | `python` | `list_slice_lock_held.isra.0` | list |
| 0.49% | `python` | `PyObject_GC_Del` | gc |
| 0.48% | `python` | `PyUnicode_Format` | str |
| 0.47% | `python` | `_PyUnicode_JoinArray.part.0` | str |
| 0.45% | `python` | `_Py_Dealloc` | memory |
| 0.45% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.44% | `python` | `_PyObject_GC_New` | gc |
| 0.44% | `python` | `sre_ucs1_count` | library |
| 0.43% | `python` | `PyDict_GetItemRef` | dict |
| 0.41% | `python` | `PyList_New` | memory |
| 0.39% | `python` | `_PyTuple_FromStackRefSteal` | tuple |
| 0.39% | `python` | `_PyObject_GenericGetAttrWithDict` | dynamic |
| 0.38% | `python` | `find_name_in_mro` | lookup |
| 0.36% | `python` | `list_extend_lock_held` | list |
| 0.36% | `python` | `PyType_GenericAlloc` | memory |
| 0.35% | `python` | `_copy_characters.part.0.constprop.0` | str |
| 0.35% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.33% | `python` | `insertdict` | dict |
| 0.31% | `python` | `_PyObject_Realloc` | memory |
| 0.31% | `python` | `_PyTuple_FromArray.part.0` | tuple |
| 0.30% | `python` | `_PyGC_Collect` | gc |
| 0.30% | `python` | `split` | str |
| 0.29% | `python` | `subtype_traverse` | gc |
| 0.29% | `python` | `PyObject_VisitManagedDict` | dynamic |
| 0.29% | `python` | `sre_search` | library |
| 0.26% | `python` | `_PyObject_GC_Link` | gc |

## fannkuch

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 35.80% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 9.00% | `python` | `PySlice_AdjustIndices` | miscobj |
| 5.48% | `python` | `list_ass_slice_lock_held` | list |
| 5.02% | `python` | `list_subscript` | list |
| 3.98% | `python` | `_PyObject_Free` | memory |
| 3.84% | `python` | `_PyObject_Malloc` | memory |
| 3.54% | `python` | `_PyEval_SliceIndex` | interpreter |
| 3.42% | `python` | `slice_dealloc` | memory |
| 2.59% | `python` | `list_dealloc` | memory |
| 2.29% | `python` | `PyNumber_AsSsize_t` | dynamic |
| 2.22% | `python` | `_PyLong_Add` | int |
| 2.17% | `python` | `_PyBuildSlice_ConsumeRefs` | miscobj |
| 2.12% | `python` | `list_ass_subscript` | list |
| 1.94% | `python` | `PySlice_Unpack` | miscobj |
| 1.59% | `python` | `PyList_New` | memory |
| 1.54% | `python` | `PySlice_New` | memory |
| 1.44% | `python` | `PyLong_AsSsize_t` | int |
| 1.28% | `python` | `PyObject_GetItem` | dynamic |
| 1.00% | `python` | `PySequence_Fast` | dynamic |
| 0.89% | `python` | `list_insert` | list |
| 0.66% | `python` | `_Py_NewReference` | memory |
| 0.64% | `python` | `_PyLong_Subtract` | int |
| 0.63% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 0.55% | `python` | `list_pop` | list |
| 0.55% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.54% | `python` | `PyObject_SetItem` | dynamic |
| 0.38% | `python` | `list_slice_lock_held.isra.0` | list |
| 0.30% | `python` | `unicodekeys_lookup_unicode` | lookup |

## float

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 38.48% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 4.73% | `libm-2.31.so` | `f64xsubf128` | library |
| 3.68% | `python` | `_PyObject_Malloc` | memory |
| 2.70% | `python` | `_PyObject_Free` | memory |
| 2.04% | `python` | `gc_collect_region.isra.0` | gc |
| 1.95% | `python` | `float_dealloc` | memory |
| 1.88% | `python` | `visit_decref` | gc |
| 1.87% | `python` | `subtype_traverse` | gc |
| 1.66% | `python` | `subtype_dealloc` | memory |
| 1.63% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.63% | `python` | `float_div` | float |
| 1.58% | `python` | `visit_reachable` | gc |
| 1.52% | `python` | `PyFloat_FromDouble` | float |
| 1.43% | `python` | `_Py_Dealloc` | memory |
| 1.19% | `python` | `visit_add_to_container` | gc |
| 0.99% | `python` | `_Py_NewReference` | memory |
| 0.96% | `python` | `PyType_IsSubtype` | dynamic |
| 0.79% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.76% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 0.74% | `python` | `_PyType_LookupRef` | lookup |
| 0.73% | `python` | `tupledealloc` | memory |
| 0.72% | `python` | `initialize_locals` | interpreter |
| 0.72% | `python` | `PyType_GenericAlloc` | memory |
| 0.66% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.64% | `python` | `PyNumber_InPlaceTrueDivide` | dynamic |
| 0.63% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.60% | `python` | `long_float` | int |
| 0.58% | `python` | `_PyObject_MakeTpCall` | dynamic |
| 0.47% | `python` | `PyFloat_AsDouble.part.0` | float |
| 0.46% | `python` | `_PyTuple_FromArray.part.0` | tuple |
| 0.46% | `python` | `list_dealloc` | memory |
| 0.45% | `python` | `_PyObject_Call_Prepend` | dynamic |
| 0.45% | `python` | `_PyEval_Vector` | interpreter |
| 0.43% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.43% | `python` | `float_mul` | float |
| 0.41% | `python` | `PyLong_AsDouble` | int |
| 0.39% | `python` | `list_slice_lock_held.isra.0` | list |
| 0.38% | `python` | `_Py_dict_lookup` | lookup |
| 0.38% | `python` | `type_call` | dynamic |
| 0.37% | `[kernel.kallsyms]` | `native_irq_return_iret` | kernel |
| 0.34% | `python` | `_PyThreadState_PopFrame` | interpreter |
| 0.32% | `python` | `slot_tp_init` | unknown |
| 0.31% | `[kernel.kallsyms]` | `clear_page_erms` | kernel |
| 0.31% | `python` | `PyNumber_Multiply` | dynamic |
| 0.30% | `python` | `list_traverse` | gc |
| 0.30% | `python` | `PyLong_FromLong` | int |
| 0.29% | `math.cpython-314-x86_64-linux-gnu.so` | `math_sin` | library |
| 0.28% | `[kernel.kallsyms]` | `sync_regs` | kernel |
| 0.28% | `python` | `r_object` | import |
| 0.26% | `python` | `_PyObject_GC_Link` | gc |
| 0.26% | `python` | `PyNumber_TrueDivide` | dynamic |
| 0.26% | `math.cpython-314-x86_64-linux-gnu.so` | `math_sqrt` | library |
| 0.26% | `python` | `dict_traverse` | gc |

## gc_collect

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 28.75% | `python` | `gc_collect_region.isra.0` | gc |
| 14.52% | `python` | `visit_reachable` | gc |
| 13.58% | `python` | `visit_decref` | gc |
| 6.26% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 4.70% | `python` | `_PyGC_Collect` | gc |
| 4.60% | `python` | `dict_traverse` | gc |
| 1.85% | `python` | `func_traverse` | gc |
| 1.64% | `python` | `PyObject_IS_GC` | gc |
| 1.51% | `python` | `subtype_traverse` | gc |
| 1.38% | `python` | `PyObject_VisitManagedDict` | dynamic |
| 1.38% | `python` | `_PyDict_MaybeUntrack` | gc |
| 1.27% | `python` | `set_traverse` | gc |
| 1.13% | `python` | `type_is_gc` | gc |
| 0.90% | `python` | `_PyObject_Malloc` | memory |
| 0.78% | `python` | `tupletraverse` | tuple |
| 0.66% | `python` | `type_traverse` | gc |
| 0.66% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.59% | `python` | `_PyObject_Free` | memory |
| 0.56% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 0.50% | `python` | `list_traverse` | gc |
| 0.46% | `python` | `meth_traverse` | gc |
| 0.45% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 0.42% | `python` | `subtype_dealloc` | memory |
| 0.42% | `python` | `PyObject_ClearManagedDict` | dynamic |
| 0.38% | `python` | `_PyType_NewManagedObject` | memory |
| 0.32% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.30% | `python` | `_Py_dict_lookup` | lookup |

## gc_traversal

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 30.79% | `python` | `visit_reachable` | gc |
| 20.97% | `python` | `visit_decref` | gc |
| 16.65% | `python` | `list_traverse` | gc |
| 11.24% | `python` | `gc_collect_region.isra.0` | gc |
| 3.65% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 2.01% | `python` | `dict_traverse` | gc |
| 0.84% | `python` | `func_traverse` | gc |
| 0.74% | `python` | `PyObject_IS_GC` | gc |
| 0.61% | `python` | `_PyDict_MaybeUntrack` | gc |
| 0.59% | `python` | `set_traverse` | gc |
| 0.54% | `python` | `_PyObject_Malloc` | memory |
| 0.52% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.47% | `python` | `type_is_gc` | gc |
| 0.46% | `python` | `PyLong_FromLong` | int |
| 0.44% | `python` | `_PyObject_Free` | memory |
| 0.32% | `python` | `tupletraverse` | tuple |
| 0.31% | `python` | `subtype_traverse` | gc |
| 0.31% | `python` | `type_traverse` | gc |
| 0.29% | `python` | `list_dealloc` | memory |
| 0.28% | `python` | `_Py_dict_lookup` | lookup |
| 0.26% | `python` | `PyObject_VisitManagedDict` | dynamic |
| 0.25% | `libc-2.31.so` | `__nss_database_lookup` | libc |

## generators

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 49.96% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 4.42% | `python` | `_PyObject_Malloc` | memory |
| 3.22% | `python` | `_PyObject_Free` | memory |
| 1.76% | `python` | `gc_collect_region.isra.0` | gc |
| 1.64% | `python` | `gen_dealloc` | memory |
| 1.34% | `python` | `PyObject_RichCompareBool` | dynamic |
| 1.31% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.24% | `python` | `long_add` | int |
| 1.02% | `python` | `initialize_locals` | interpreter |
| 0.93% | `python` | `visit_decref` | gc |
| 0.90% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.86% | `python` | `range_subscript` | miscobj |
| 0.82% | `python` | `visit_reachable` | gc |
| 0.80% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.79% | `python` | `make_gen` | miscobj |
| 0.73% | `python` | `_PyObject_GC_NewVar` | gc |
| 0.73% | `python` | `compute_range_length` | unknown |
| 0.72% | `python` | `_PyType_LookupRef` | lookup |
| 0.71% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.70% | `python` | `PyNumber_Add` | dynamic |
| 0.68% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 0.67% | `python` | `long_richcompare` | int |
| 0.60% | `python` | `_Py_Dealloc` | memory |
| 0.58% | `python` | `_PySlice_GetLongIndices` | miscobj |
| 0.57% | `python` | `PyObject_GC_Del` | gc |
| 0.54% | `python` | `_PyBuildSlice_ConsumeRefs` | miscobj |
| 0.53% | `python` | `PyObject_CallOneArg` | dynamic |
| 0.49% | `python` | `subtype_traverse` | gc |
| 0.49% | `python` | `PyObject_VisitManagedDict` | dynamic |
| 0.48% | `python` | `_PyEval_Vector` | interpreter |
| 0.48% | `python` | `PyLong_AsLongAndOverflow` | int |
| 0.47% | `python` | `slot_tp_iter` | unknown |
| 0.46% | `python` | `_PyObject_GC_Link` | gc |
| 0.44% | `python` | `long_mul` | int |
| 0.43% | `python` | `visit_add_to_container` | gc |
| 0.41% | `python` | `long_div` | int |
| 0.39% | `python` | `PyObject_CallFinalizerFromDealloc` | memory |
| 0.38% | `python` | `_Py_NewReference` | memory |
| 0.37% | `python` | `_Py_dict_lookup` | lookup |
| 0.37% | `python` | `_PyThreadState_PopFrame` | interpreter |
| 0.36% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.35% | `python` | `subtype_dealloc` | memory |
| 0.34% | `python` | `PyObject_GetItem` | dynamic |
| 0.34% | `python` | `long_dealloc` | memory |
| 0.34% | `python` | `_PyType_NewManagedObject` | memory |
| 0.33% | `python` | `PyObject_ClearManagedDict` | dynamic |
| 0.31% | `python` | `range_dealloc` | memory |
| 0.31% | `python` | `PyNumber_Multiply` | dynamic |
| 0.29% | `python` | `slice_dealloc` | memory |
| 0.26% | `python` | `_PyThreadState_PushFrame` | interpreter |
| 0.26% | `python` | `PyLong_FromLong` | int |
| 0.25% | `python` | `PyObject_IsTrue` | dynamic |

## genshi

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 42.41% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 3.68% | `python` | `_PyObject_Malloc` | memory |
| 3.02% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 2.95% | `python` | `_PyObject_Free` | memory |
| 2.76% | `python` | `_Py_dict_lookup` | lookup |
| 1.57% | `python` | `_PyType_LookupRef` | lookup |
| 1.31% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.28% | `python` | `tupledealloc` | memory |
| 1.26% | `python` | `insertdict` | dict |
| 1.06% | `python` | `dict_dealloc` | memory |
| 1.05% | `python` | `_PyTuple_FromStackRefSteal` | tuple |
| 1.05% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 0.87% | `python` | `gc_collect_region.isra.0` | gc |
| 0.84% | `python` | `insert_to_emptydict` | dict |
| 0.75% | `python` | `_PyObject_GC_New` | gc |
| 0.73% | `python` | `initialize_locals` | interpreter |
| 0.68% | `python` | `_PyDict_FromItems` | dict |
| 0.63% | `python` | `PyDict_GetItemRef` | dict |
| 0.60% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.58% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.58% | `python` | `pattern_subx` | library |
| 0.55% | `libc-2.31.so` | `pthread_attr_setschedparam` | libc |
| 0.50% | `python` | `PyObject_GC_Del` | gc |
| 0.50% | `python` | `PyType_IsSubtype` | dynamic |
| 0.49% | `python` | `long_to_decimal_string_internal` | int |
| 0.48% | `python` | `PyObject_IsTrue` | dynamic |
| 0.45% | `python` | `visit_decref` | gc |
| 0.44% | `python` | `_PyObject_GetMethod` | dynamic |
| 0.40% | `python` | `_Py_type_getattro` | lookup |
| 0.39% | `python` | `gen_iternext` | miscobj |
| 0.39% | `python` | `_Py_Dealloc` | memory |
| 0.38% | `python` | `_PyUnicode_JoinArray.part.0` | str |
| 0.38% | `python` | `visit_reachable` | gc |
| 0.35% | `python` | `_PyFunction_FromConstructor` | unknown |
| 0.35% | `python` | `_PyObject_GenericGetAttrWithDict` | dynamic |
| 0.34% | `python` | `r_object` | import |
| 0.33% | `python` | `_Py_NewReference` | memory |
| 0.33% | `python` | `build_indices_unicode` | dict |
| 0.31% | `python` | `find_empty_slot` | dict |
| 0.31% | `libc-2.31.so` | `malloc` | libc |
| 0.30% | `python` | `PyObject_RichCompareBool` | dynamic |
| 0.30% | `python` | `dictiter_iternextvalue` | dict |
| 0.30% | `python` | `tuplehash` | tuple |
| 0.29% | `python` | `_PyObject_GC_Link` | gc |
| 0.28% | `python` | `update_one_slot` | lookup |
| 0.27% | `python` | `method_dealloc` | memory |
| 0.27% | `python` | `find_name_in_mro` | lookup |
| 0.27% | `python` | `PyObject_Vectorcall` | dynamic |
| 0.27% | `python` | `list_dealloc` | memory |
| 0.26% | `python` | `_PyThreadState_PopFrame` | interpreter |
| 0.26% | `python` | `sre_ucs1_match` | library |

## go

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 61.82% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 2.60% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 2.35% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 1.90% | `python` | `_PyObject_Free` | memory |
| 1.76% | `python` | `_PyObject_GetMethod` | dynamic |
| 1.73% | `python` | `_PyObject_Malloc` | memory |
| 1.64% | `python` | `_PyType_LookupRef` | lookup |
| 1.53% | `python` | `_Py_dict_lookup` | lookup |
| 1.09% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.07% | `python` | `initialize_locals` | interpreter |
| 0.93% | `python` | `long_bitwise` | int |
| 0.91% | `python` | `PyDict_GetItemRef` | dict |
| 0.90% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 0.70% | `python` | `gc_collect_region.isra.0` | gc |
| 0.61% | `python` | `_PyLong_Add` | int |
| 0.58% | `python` | `_PyThreadState_PopFrame` | interpreter |
| 0.50% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.46% | `python` | `visit_decref` | gc |
| 0.45% | `python` | `insertdict` | dict |
| 0.37% | `python` | `_PyLong_Subtract` | int |
| 0.32% | `python` | `r_object` | import |
| 0.31% | `python` | `visit_reachable` | gc |
| 0.29% | `libc-2.31.so` | `pthread_attr_setschedparam` | libc |

## hexiom

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 54.70% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 3.73% | `python` | `PyObject_RichCompareBool` | dynamic |
| 2.40% | `python` | `list_contains` | list |
| 2.37% | `python` | `long_richcompare` | int |
| 2.00% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.93% | `python` | `_PyObject_Malloc` | memory |
| 1.80% | `python` | `_PyObject_Free` | memory |
| 1.39% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 1.16% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.10% | `python` | `gen_iternext` | miscobj |
| 0.96% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.93% | `python` | `gc_collect_region.isra.0` | gc |
| 0.73% | `python` | `PyLong_FromSsize_t` | int |
| 0.73% | `python` | `_Py_dict_lookup` | lookup |
| 0.72% | `python` | `builtin_sum` | unknown |
| 0.58% | `python` | `PyLong_FromLong` | int |
| 0.50% | `python` | `visit_decref` | gc |
| 0.49% | `python` | `_PyThreadState_PopFrame` | interpreter |
| 0.44% | `python` | `PyObject_Size` | dynamic |
| 0.41% | `python` | `r_object` | import |
| 0.39% | `python` | `visit_reachable` | gc |
| 0.38% | `python` | `list_dealloc` | memory |
| 0.37% | `python` | `PyIter_Next` | dynamic |
| 0.36% | `python` | `PyObject_GC_Del` | gc |
| 0.34% | `python` | `tupledealloc` | memory |
| 0.33% | `python` | `range_iter` | miscobj |
| 0.31% | `python` | `find_name_in_mro` | lookup |
| 0.30% | `python` | `_PyLong_Add` | int |
| 0.30% | `python` | `compute_range_length` | unknown |
| 0.29% | `python` | `PyFunction_NewWithQualName` | memory |
| 0.29% | `python` | `PySequence_Contains` | dynamic |
| 0.27% | `python` | `PyList_New` | memory |
| 0.27% | `python` | `_PyCode_Quicken` | interpreter |
| 0.26% | `python` | `siphash13` | str |
| 0.25% | `python` | `update_one_slot` | lookup |

## html5lib

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 36.44% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 7.68% | `python` | `sre_ucs2_charset.isra.0` | library |
| 2.96% | `python` | `gc_collect_region.isra.0` | gc |
| 2.67% | `python` | `_PyObject_Malloc` | memory |
| 2.34% | `python` | `_PyObject_Free` | memory |
| 2.26% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 1.93% | `python` | `_Py_dict_lookup` | lookup |
| 1.47% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.28% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.24% | `python` | `visit_decref` | gc |
| 0.95% | `python` | `PyDict_GetItemRef` | dict |
| 0.82% | `python` | `_PyType_LookupRef` | lookup |
| 0.76% | `python` | `sre_ucs1_count` | library |
| 0.75% | `python` | `PyObject_RichCompareBool` | dynamic |
| 0.65% | `libc-2.31.so` | `pthread_attr_setschedparam` | libc |
| 0.62% | `python` | `initialize_locals` | interpreter |
| 0.62% | `python` | `visit_reachable` | gc |
| 0.58% | `python` | `tupledealloc` | memory |
| 0.52% | `python` | `insertdict` | dict |
| 0.51% | `python` | `set_lookkey` | miscobj |
| 0.48% | `python` | `dict_dealloc` | memory |
| 0.48% | `python` | `visit_add_to_container` | gc |
| 0.48% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.43% | `python` | `siphash13` | str |
| 0.43% | `python` | `PyObject_GetAttr` | dynamic |
| 0.41% | `python` | `_Py_Dealloc` | memory |
| 0.40% | `python` | `list_subscript` | list |
| 0.39% | `python` | `PyObject_GenericGetAttr` | dynamic |
| 0.38% | `python` | `_PyUnicode_TranslateCharmap` | str |
| 0.37% | `python` | `list_dealloc` | memory |
| 0.36% | `python` | `r_object` | import |
| 0.36% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.35% | `python` | `PyObject_GC_Del` | gc |
| 0.35% | `python` | `PyObject_GetItem` | dynamic |
| 0.35% | `python` | `insert_to_emptydict` | dict |
| 0.35% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.35% | `python` | `_PyUnicode_Equal` | str |
| 0.34% | `python` | `list_contains` | list |
| 0.33% | `python` | `PyList_New` | memory |
| 0.33% | `python` | `PyObject_IsTrue` | dynamic |
| 0.31% | `python` | `PyNumber_AsSsize_t` | dynamic |
| 0.30% | `python` | `PyType_GenericAlloc` | memory |
| 0.29% | `python` | `_PyObject_GC_New` | gc |
| 0.29% | `python` | `find_name_in_mro` | lookup |
| 0.27% | `python` | `_PyThreadState_PopFrame` | interpreter |
| 0.26% | `python` | `sre_ucs1_match` | library |
| 0.26% | `python` | `update_one_slot` | lookup |

## json

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 11.07% | `_json.cpython-314-x86_64-linux-gnu.so` | `scanstring_unicode` | library |
| 7.46% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 6.91% | `python` | `_PyObject_Malloc` | memory |
| 5.78% | `_json.cpython-314-x86_64-linux-gnu.so` | `scan_once_unicode` | library |
| 5.28% | `python` | `_PyObject_Free` | memory |
| 5.11% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 4.62% | `python` | `siphash13` | str |
| 3.34% | `python` | `_Py_dict_lookup` | lookup |
| 3.13% | `python` | `dict_setdefault_ref_lock_held` | dict |
| 2.22% | `python` | `PyLong_FromString` | int |
| 2.16% | `python` | `insertdict` | dict |
| 2.12% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.92% | `libc-2.31.so` | `pthread_attr_setschedparam` | libc |
| 1.82% | `python` | `PyUnicode_Substring` | str |
| 1.81% | `python` | `dict_dealloc` | memory |
| 1.42% | `python` | `PyUnicode_New.part.0` | memory |
| 1.20% | `python` | `build_indices_unicode` | dict |
| 1.19% | `python` | `gc_collect_region.isra.0` | gc |
| 1.10% | `python` | `find_empty_slot` | dict |
| 0.81% | `python` | `PyObject_IS_GC` | gc |
| 0.80% | `python` | `unicode_dealloc` | memory |
| 0.78% | `python` | `_Py_Dealloc` | memory |
| 0.73% | `python` | `PyDict_SetItem` | dict |
| 0.68% | `python` | `_sre_SRE_Pattern_match` | library |
| 0.63% | `python` | `initialize_locals` | interpreter |
| 0.57% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 0.55% | `python` | `insert_to_emptydict` | dict |
| 0.54% | `python` | `tupledealloc` | memory |
| 0.51% | `python` | `sre_ucs1_match` | library |
| 0.47% | `python` | `PyDict_GetItemRef` | dict |
| 0.46% | `libc-2.31.so` | `malloc` | libc |
| 0.45% | `python` | `dictresize` | dict |
| 0.42% | `python` | `visit_decref` | gc |
| 0.42% | `python` | `r_object` | import |
| 0.41% | `python` | `_Py_NewReference` | memory |
| 0.40% | `python` | `visit_reachable` | gc |
| 0.36% | `python` | `_PyObject_Realloc` | memory |
| 0.35% | `python` | `unicode_hash` | str |
| 0.32% | `python` | `new_keys_object.constprop.0` | unknown |
| 0.31% | `python` | `resize_compact` | str |
| 0.31% | `python` | `pattern_new_match.isra.0.part.0` | memory |
| 0.31% | `python` | `PyObject_Malloc` | dynamic |
| 0.31% | `python` | `PyBytes_FromStringAndSize` | str |
| 0.29% | `python` | `PyUnicode_Splitlines` | str |
| 0.29% | `python` | `_PyType_LookupRef` | lookup |
| 0.29% | `python` | `update_one_slot` | lookup |
| 0.29% | `python` | `_PyCode_Quicken` | interpreter |
| 0.28% | `python` | `_PyUnicodeWriter_Init` | str |
| 0.28% | `python` | `find_name_in_mro` | lookup |
| 0.26% | `python` | `vgetargskeywords.constprop.0` | calls |

## json_dumps

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 12.79% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 7.79% | `python` | `_PyObject_Malloc` | memory |
| 6.78% | `_json.cpython-314-x86_64-linux-gnu.so` | `py_encode_basestring_ascii` | library |
| 6.59% | `python` | `_PyObject_Free` | memory |
| 3.39% | `python` | `_copy_characters.part.0.constprop.0` | str |
| 3.02% | `python` | `_Py_dict_lookup` | lookup |
| 2.58% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 2.56% | `_json.cpython-314-x86_64-linux-gnu.so` | `encoder_listencode_obj` | library |
| 2.48% | `python` | `_PyUnicodeWriter_WriteStr` | str |
| 2.38% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 2.20% | `python` | `resize_compact` | str |
| 1.96% | `python` | `vgetargskeywords.constprop.0` | calls |
| 1.82% | `_json.cpython-314-x86_64-linux-gnu.so` | `encoder_encode_key_value` | library |
| 1.82% | `python` | `PyUnicode_New.part.0` | memory |
| 1.37% | `python` | `_PyObject_Realloc` | memory |
| 1.25% | `python` | `convertitem.constprop.0` | library |
| 1.24% | `python` | `_Py_Dealloc` | memory |
| 1.20% | `python` | `tupledealloc` | memory |
| 1.16% | `python` | `unicode_dealloc` | memory |
| 1.14% | `python` | `PyDict_GetItemRef` | dict |
| 1.12% | `python` | `PyDict_Next` | dict |
| 1.02% | `python` | `gc_collect_region.isra.0` | gc |
| 1.00% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 0.91% | `python` | `_PyType_LookupRef` | lookup |
| 0.89% | `python` | `initialize_locals` | interpreter |
| 0.84% | `python` | `_PyUnicodeWriter_PrepareInternal` | str |
| 0.77% | `python` | `long_to_decimal_string_internal` | int |
| 0.63% | `python` | `_Py_NewReference` | memory |
| 0.52% | `python` | `PyType_IsSubtype` | dynamic |
| 0.46% | `python` | `r_object` | import |
| 0.42% | `python` | `_PyTuple_FromArray.part.0` | tuple |
| 0.41% | `python` | `visit_decref` | gc |
| 0.41% | `python` | `dict_dealloc` | memory |
| 0.41% | `python` | `visit_reachable` | gc |
| 0.41% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.40% | `python` | `long_hash` | int |
| 0.36% | `python` | `_PyTuple_FromStackRefSteal` | tuple |
| 0.35% | `python` | `delitem_common` | dynamic |
| 0.34% | `python` | `PyObject_Malloc` | dynamic |
| 0.34% | `python` | `_PyObject_GenericGetAttrWithDict` | dynamic |
| 0.34% | `python` | `insertdict` | dict |
| 0.31% | `python` | `update_one_slot` | lookup |
| 0.30% | `python` | `PyType_GenericAlloc` | memory |
| 0.30% | `python` | `_Py_type_getattro` | lookup |
| 0.29% | `python` | `memcpy@plt` | memory |
| 0.29% | `python` | `PyTuple_New` | memory |
| 0.28% | `python` | `PyObject_GenericGetAttr` | dynamic |
| 0.28% | `python` | `insert_to_emptydict` | dict |
| 0.27% | `python` | `find_name_in_mro` | lookup |
| 0.27% | `python` | `_PyCode_Quicken` | interpreter |
| 0.27% | `python` | `PyObject_IsTrue` | dynamic |
| 0.26% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.26% | `python` | `PyDict_DelItem` | dict |
| 0.26% | `python` | `siphash13` | str |
| 0.25% | `python` | `PyObject_GC_Del` | gc |

## json_loads

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 14.32% | `_json.cpython-314-x86_64-linux-gnu.so` | `scanstring_unicode` | library |
| 8.49% | `python` | `_PyObject_Malloc` | memory |
| 7.44% | `_json.cpython-314-x86_64-linux-gnu.so` | `scan_once_unicode` | library |
| 6.80% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 6.42% | `python` | `siphash13` | str |
| 5.40% | `python` | `_PyObject_Free` | memory |
| 4.27% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 3.77% | `python` | `_Py_dict_lookup` | lookup |
| 3.54% | `python` | `PyUnicode_Substring` | str |
| 2.84% | `python` | `dict_setdefault_ref_lock_held` | dict |
| 2.72% | `python` | `insertdict` | dict |
| 2.72% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 2.65% | `python` | `PyLong_FromString` | int |
| 2.32% | `python` | `PyUnicode_New.part.0` | memory |
| 1.27% | `python` | `unicode_dealloc` | memory |
| 1.19% | `python` | `find_empty_slot` | dict |
| 1.19% | `python` | `dict_dealloc` | memory |
| 1.03% | `python` | `_Py_Dealloc` | memory |
| 1.01% | `libc-2.31.so` | `pthread_attr_setschedparam` | libc |
| 0.92% | `python` | `build_indices_unicode` | dict |
| 0.77% | `python` | `PyDict_SetItem` | dict |
| 0.74% | `python` | `PyObject_IS_GC` | gc |
| 0.67% | `python` | `gc_collect_region.isra.0` | gc |
| 0.52% | `python` | `_Py_NewReference` | memory |
| 0.42% | `python` | `_PyUnicodeWriter_Init` | str |
| 0.42% | `python` | `unicode_hash` | str |
| 0.41% | `python` | `_sre_SRE_Pattern_match` | library |
| 0.36% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 0.34% | `python` | `dictresize` | dict |
| 0.34% | `python` | `PyObject_Malloc` | dynamic |
| 0.33% | `python` | `initialize_locals` | interpreter |
| 0.32% | `python` | `insert_to_emptydict` | dict |
| 0.32% | `python` | `PyList_Append` | list |
| 0.32% | `libc-2.31.so` | `malloc` | libc |
| 0.29% | `python` | `r_object` | import |
| 0.28% | `python` | `tupledealloc` | memory |
| 0.28% | `python` | `PyDict_GetItemRef` | dict |
| 0.27% | `python` | `_Py_HashBytes` | unknown |
| 0.26% | `python` | `new_keys_object.constprop.0` | unknown |
| 0.26% | `python` | `PyObject_Hash` | dynamic |
| 0.26% | `python` | `_PyObject_Realloc` | memory |
| 0.25% | `python` | `visit_reachable` | gc |

## logging

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 44.05% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 3.76% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 2.63% | `python` | `_PyObject_Malloc` | memory |
| 2.30% | `python` | `_Py_dict_lookup` | lookup |
| 2.21% | `python` | `_PyObject_Free` | memory |
| 2.10% | `python` | `initialize_locals` | interpreter |
| 1.81% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.71% | `python` | `dict_dealloc` | memory |
| 1.66% | `python` | `PyCode_Addr2Line` | exceptions |
| 1.55% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.42% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 1.14% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 1.12% | `python` | `PyDict_New` | memory |
| 1.09% | `python` | `PyDict_GetItemRef` | dict |
| 1.00% | `python` | `_PyType_LookupRef` | lookup |
| 0.81% | `python` | `_PyThreadState_PopFrame` | interpreter |
| 0.68% | `python` | `_Py_Dealloc` | memory |
| 0.66% | `python` | `PyObject_GenericGetAttr` | dynamic |
| 0.64% | `python` | `PyUnicode_Contains` | str |
| 0.55% | `python` | `tupledealloc` | memory |
| 0.53% | `python` | `PyObject_GetAttr` | dynamic |
| 0.52% | `python` | `gc_collect_region.isra.0` | gc |
| 0.48% | `python` | `_PyThreadState_PushFrame` | interpreter |
| 0.46% | `python` | `_Py_NewReference` | memory |
| 0.44% | `python` | `_PyObject_LookupSpecialMethod` | dynamic |
| 0.38% | `python` | `PyObject_Hash` | dynamic |
| 0.37% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.34% | `python` | `PyUnicode_Format` | str |
| 0.34% | `python` | `PySlice_AdjustIndices` | miscobj |
| 0.33% | `python` | `any_find_slice` | unknown |
| 0.33% | `python` | `PyObject_Vectorcall` | dynamic |
| 0.31% | `python` | `_PyObject_GenericGetAttrWithDict` | dynamic |
| 0.30% | `python` | `visit_decref` | gc |
| 0.30% | `python` | `PyUnicode_Splitlines` | str |
| 0.28% | `python` | `siphash13` | str |
| 0.28% | `python` | `_PyTuple_FromStackRefSteal` | tuple |
| 0.27% | `python` | `_PyTuple_FromArray.part.0` | tuple |
| 0.26% | `python` | `long_hash` | int |
| 0.25% | `python` | `make_dict_from_instance_attributes` | unknown |
| 0.25% | `python` | `_PyBuildSlice_ConsumeRefs` | miscobj |

## mako

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 32.96% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 7.35% | `python` | `replace` | str |
| 4.16% | `python` | `_PyObject_Free` | memory |
| 3.82% | `python` | `long_to_decimal_string_internal` | int |
| 3.79% | `python` | `_PyObject_Malloc` | memory |
| 3.17% | `python` | `_PyUnicode_JoinArray.part.0` | str |
| 2.23% | `python` | `unicode_replace` | str |
| 2.13% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 2.01% | `python` | `deque_append` | miscobj |
| 1.71% | `python` | `dequeiter_next` | miscobj |
| 1.48% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 1.35% | `python` | `gc_collect_region.isra.0` | gc |
| 1.01% | `python` | `list_dealloc` | memory |
| 0.96% | `python` | `_list_extend` | list |
| 0.92% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 0.88% | `python` | `PyUnicode_New.part.0` | memory |
| 0.79% | `python` | `_Py_dict_lookup` | lookup |
| 0.78% | `libc-2.31.so` | `pthread_attr_setschedparam` | libc |
| 0.77% | `python` | `PyErr_CheckSignals` | exceptions |
| 0.70% | `python` | `visit_decref` | gc |
| 0.67% | `python` | `deque_clear.part.0` | miscobj |
| 0.66% | `python` | `sre_ucs2_charset.isra.0` | library |
| 0.63% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.56% | `python` | `PyObject_Str` | dynamic |
| 0.55% | `python` | `unicode_dealloc` | memory |
| 0.49% | `python` | `_Py_Dealloc` | memory |
| 0.44% | `[kernel.kallsyms]` | `native_irq_return_iret` | kernel |
| 0.42% | `python` | `visit_reachable` | gc |
| 0.41% | `python` | `r_object` | import |
| 0.39% | `python` | `PyThread_get_thread_ident` | unknown |
| 0.39% | `python` | `_PyType_LookupRef` | lookup |
| 0.38% | `python` | `update_one_slot` | lookup |
| 0.37% | `python` | `PyLong_FromLong` | int |
| 0.37% | `python` | `find_name_in_mro` | lookup |
| 0.36% | `[kernel.kallsyms]` | `clear_page_erms` | kernel |
| 0.35% | `python` | `_Py_NewReference` | memory |
| 0.34% | `python` | `siphash13` | str |
| 0.33% | `python` | `_PyCode_Quicken` | interpreter |
| 0.31% | `python` | `long_to_decimal_string` | int |
| 0.30% | `[kernel.kallsyms]` | `sync_regs` | kernel |
| 0.30% | `python` | `tupledealloc` | memory |
| 0.29% | `python` | `_Py_hashtable_get_entry_generic` | lookup |

## mdp

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 28.64% | `python` | `tuplehash` | tuple |
| 14.75% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 13.25% | `python` | `PyObject_Hash` | dynamic |
| 11.42% | `python` | `long_hash` | int |
| 6.40% | `python` | `_Py_dict_lookup` | lookup |
| 3.05% | `python` | `PyObject_RichCompareBool` | dynamic |
| 1.88% | `python` | `tuplerichcompare` | tuple |
| 1.44% | `python` | `_PyObject_Free` | memory |
| 1.27% | `python` | `_PyObject_Malloc` | memory |
| 1.13% | `python` | `dict_subscript` | dict |
| 0.96% | `python` | `_PyLong_GCD` | int |
| 0.71% | `python` | `PyDict_GetItemRef` | dict |
| 0.66% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.64% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 0.52% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 0.46% | `python` | `builtin_sum` | unknown |
| 0.45% | `python` | `gen_iternext` | miscobj |
| 0.44% | `python` | `set_lookkey` | miscobj |
| 0.38% | `python` | `PyObject_GetItem` | dynamic |
| 0.37% | `python` | `insertdict` | dict |
| 0.34% | `python` | `_PyType_LookupRef` | lookup |
| 0.33% | `python` | `subtype_dealloc` | memory |
| 0.33% | `python` | `tupledealloc` | memory |
| 0.31% | `python` | `_Py_Dealloc` | memory |
| 0.30% | `python` | `PyFunction_NewWithQualName` | memory |
| 0.26% | `python` | `PyObject_GC_Del` | gc |

## meteor_contest

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 21.39% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 8.11% | `python` | `set_issubset_impl` | miscobj |
| 7.25% | `python` | `set_lookkey` | miscobj |
| 6.28% | `python` | `setiter_iternext` | miscobj |
| 3.41% | `python` | `set_difference` | miscobj |
| 3.18% | `python` | `set_dealloc` | memory |
| 2.99% | `python` | `_PyObject_Malloc` | memory |
| 2.86% | `python` | `_PyObject_Free` | memory |
| 2.73% | `python` | `PyObject_RichCompareBool` | dynamic |
| 2.20% | `python` | `list_dealloc` | memory |
| 1.96% | `python` | `set_add_entry` | miscobj |
| 1.67% | `python` | `long_richcompare` | int |
| 1.54% | `python` | `min_max` | unknown |
| 1.38% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.25% | `python` | `list_slice_lock_held.isra.0` | list |
| 1.19% | `python` | `PyIter_Next` | dynamic |
| 1.13% | `python` | `PyObject_RichCompare` | dynamic |
| 1.10% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.94% | `python` | `gc_collect_region.isra.0` | gc |
| 0.87% | `python` | `set_intersection` | miscobj |
| 0.85% | `python` | `set_table_resize` | miscobj |
| 0.81% | `python` | `PyObject_GC_Del` | gc |
| 0.77% | `python` | `PyType_GenericAlloc` | memory |
| 0.69% | `python` | `_Py_dict_lookup` | lookup |
| 0.69% | `python` | `set_merge_lock_held.part.0` | miscobj |
| 0.56% | `python` | `set_richcompare` | miscobj |
| 0.53% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 0.51% | `python` | `_PyObject_GC_New` | gc |
| 0.50% | `python` | `initialize_locals` | interpreter |
| 0.48% | `python` | `PySlice_AdjustIndices` | miscobj |
| 0.47% | `python` | `visit_decref` | gc |
| 0.43% | `python` | `set_difference_update_internal` | miscobj |
| 0.39% | `python` | `r_object` | import |
| 0.38% | `python` | `visit_reachable` | gc |
| 0.37% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.33% | `python` | `PyObject_IsTrue` | dynamic |
| 0.32% | `python` | `slice_dealloc` | memory |
| 0.30% | `libc-2.31.so` | `pthread_attr_setschedparam` | libc |
| 0.30% | `python` | `_PyObject_GC_Link` | gc |
| 0.29% | `python` | `_PyCode_Quicken` | interpreter |
| 0.29% | `python` | `list_subscript` | list |
| 0.28% | `python` | `PyList_New` | memory |
| 0.27% | `python` | `_Py_NewReference` | memory |
| 0.27% | `python` | `find_name_in_mro` | lookup |
| 0.27% | `python` | `list_ass_slice_lock_held` | list |
| 0.26% | `python` | `PyObject_GetIter` | dynamic |
| 0.26% | `python` | `_PyBuildSlice_ConsumeRefs` | miscobj |
| 0.26% | `python` | `_PyType_LookupRef` | lookup |
| 0.25% | `python` | `siphash13` | str |

## nbody

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 69.38% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 4.47% | `libm-2.31.so` | `f64xsubf128` | library |
| 4.37% | `python` | `PyFloat_FromDouble` | float |
| 2.90% | `python` | `float_dealloc` | memory |
| 1.83% | `python` | `_Py_NewReference` | memory |
| 1.61% | `python` | `float_pow` | float |
| 0.82% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.73% | `python` | `_PyObject_Free` | memory |
| 0.67% | `python` | `_PyObject_Malloc` | memory |
| 0.63% | `python` | `gc_collect_region.isra.0` | gc |
| 0.46% | `libm-2.31.so` | `pow` | library |
| 0.41% | `python` | `_PyNumber_PowerNoMod` | dynamic |
| 0.40% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 0.35% | `python` | `visit_decref` | gc |
| 0.35% | `python` | `_Py_dict_lookup` | lookup |
| 0.33% | `python` | `_PyFloat_ExactDealloc` | memory |
| 0.28% | `python` | `r_object` | import |

## nqueens

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 34.90% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 5.25% | `python` | `_PyObject_Free` | memory |
| 5.09% | `python` | `_PyObject_Malloc` | memory |
| 3.17% | `python` | `gen_iternext` | miscobj |
| 2.88% | `python` | `set_add_entry` | miscobj |
| 2.43% | `python` | `PySlice_AdjustIndices` | miscobj |
| 1.60% | `python` | `PyList_New` | memory |
| 1.32% | `python` | `_PyBuildSlice_ConsumeRefs` | miscobj |
| 1.28% | `python` | `_PyLong_Add` | int |
| 1.27% | `python` | `list_dealloc` | memory |
| 1.26% | `python` | `set_dealloc` | memory |
| 1.25% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 1.16% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.02% | `python` | `list_subscript` | list |
| 1.02% | `python` | `slice_dealloc` | memory |
| 0.99% | `python` | `tupledealloc` | memory |
| 0.96% | `python` | `PyFunction_NewWithQualName` | memory |
| 0.92% | `python` | `set_table_resize` | miscobj |
| 0.91% | `python` | `PyNumber_AsSsize_t` | dynamic |
| 0.90% | `python` | `_Py_dict_lookup` | lookup |
| 0.81% | `python` | `_PyEval_SliceIndex` | interpreter |
| 0.80% | `python` | `_PyObject_LookupSpecial` | dynamic |
| 0.78% | `python` | `PyObject_GC_Del` | gc |
| 0.75% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.66% | `python` | `PyIter_Next` | dynamic |
| 0.65% | `python` | `list_ass_slice_lock_held` | list |
| 0.63% | `python` | `PyLong_FromLong` | int |
| 0.62% | `python` | `PySequence_Tuple` | dynamic |
| 0.61% | `python` | `PySlice_Unpack` | miscobj |
| 0.58% | `python` | `list_ass_subscript` | list |
| 0.57% | `python` | `gen_dealloc` | memory |
| 0.56% | `python` | `_Py_NewReference` | memory |
| 0.56% | `python` | `func_clear` | unknown |
| 0.56% | `python` | `list_slice_lock_held.isra.0` | list |
| 0.56% | `python` | `func_dealloc` | memory |
| 0.55% | `python` | `range_iter` | miscobj |
| 0.55% | `python` | `set_update_iterable_lock_held` | miscobj |
| 0.52% | `python` | `PyType_GenericAlloc` | memory |
| 0.51% | `python` | `_PyTuple_FromStackRefSteal` | tuple |
| 0.50% | `python` | `_PyObject_GC_New` | gc |
| 0.50% | `python` | `PyObject_GetItem` | dynamic |
| 0.49% | `python` | `_PyObject_GC_NewVar` | gc |
| 0.49% | `python` | `_PyLong_Subtract` | int |
| 0.47% | `python` | `PyLong_AsSsize_t` | int |
| 0.42% | `python` | `range_reverse` | miscobj |
| 0.42% | `python` | `compute_range_length` | unknown |
| 0.41% | `python` | `PyObject_GetIter` | dynamic |
| 0.40% | `python` | `PyObject_Hash` | dynamic |
| 0.39% | `python` | `_Py_Dealloc` | memory |
| 0.39% | `python` | `PyLong_AsLong` | int |
| 0.39% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 0.34% | `python` | `gc_collect_region.isra.0` | gc |
| 0.32% | `python` | `_PyObject_GC_Link` | gc |
| 0.31% | `python` | `_PyTuple_Resize` | tuple |
| 0.31% | `python` | `list_concat` | list |
| 0.29% | `python` | `PyTuple_New` | memory |
| 0.29% | `python` | `PyDict_GetItemWithError` | dict |
| 0.29% | `python` | `long_hash` | int |
| 0.25% | `python` | `PyDict_GetItemRef` | dict |

## pathlib

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 12.83% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 5.28% | `python` | `_PyObject_Malloc` | memory |
| 4.80% | `python` | `_PyObject_Free` | memory |
| 1.74% | `[kernel.kallsyms]` | `__d_lookup_rcu` | kernel |
| 1.56% | `python` | `_PyType_LookupRef` | lookup |
| 1.56% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.55% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 1.37% | `libpthread-2.31.so` | `__pthread_mutex_lock` | library |
| 1.29% | `[kernel.kallsyms]` | `ext4_htree_store_dirent` | kernel |
| 1.27% | `libpthread-2.31.so` | `pthread_mutex_unlock` | library |
| 1.25% | `[kernel.kallsyms]` | `__ext4fs_dirhash` | kernel |
| 1.18% | `[kernel.kallsyms]` | `memset_erms` | kernel |
| 1.08% | `python` | `_Py_Dealloc` | memory |
| 1.06% | `python` | `initialize_locals` | interpreter |
| 0.93% | `python` | `take_gil` | gil |
| 0.90% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 0.89% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.86% | `python` | `_Py_dict_lookup` | lookup |
| 0.81% | `[kernel.kallsyms]` | `filldir64` | kernel |
| 0.81% | `python` | `k_mul` | int |
| 0.80% | `python` | `gc_collect_region.isra.0` | gc |
| 0.76% | `libc-2.31.so` | `pthread_attr_setschedparam` | libc |
| 0.73% | `python` | `subtype_dealloc` | memory |
| 0.72% | `python` | `tupledealloc` | memory |
| 0.66% | `[kernel.kallsyms]` | `link_path_walk.part.0` | kernel |
| 0.65% | `[kernel.kallsyms]` | `strncpy_from_user` | kernel |
| 0.64% | `python` | `sre_ucs1_match` | library |
| 0.60% | `[kernel.kallsyms]` | `copy_user_enhanced_fast_string` | kernel |
| 0.54% | `python` | `fill_time` | unknown |
| 0.52% | `python` | `ascii_decode` | str |
| 0.52% | `[kernel.kallsyms]` | `__slab_free` | kernel |
| 0.51% | `python` | `_PyObject_LookupSpecial` | dynamic |
| 0.50% | `python` | `_Py_NewReference` | memory |
| 0.49% | `[kernel.kallsyms]` | `str2hashbuf_signed` | kernel |
| 0.48% | `[kernel.kallsyms]` | `security_inode_getattr` | kernel |
| 0.47% | `[kernel.kallsyms]` | `syscall_return_via_sysret` | kernel |
| 0.46% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.46% | `python` | `_PyTuple_FromStackRefSteal` | tuple |
| 0.45% | `python` | `ScandirIterator_iternext` | unknown |
| 0.45% | `python` | `x_add` | int |
| 0.45% | `[kernel.kallsyms]` | `rb_insert_color` | kernel |
| 0.44% | `python` | `_PyArg_UnpackKeywords` | calls |
| 0.44% | `[kernel.kallsyms]` | `__ext4_check_dir_entry` | kernel |
| 0.44% | `python` | `_Py_type_getattro` | lookup |
| 0.43% | `[kernel.kallsyms]` | `ext4_getattr` | kernel |
| 0.43% | `python` | `map_next` | unknown |
| 0.42% | `[kernel.kallsyms]` | `rb_next` | kernel |
| 0.42% | `[kernel.kallsyms]` | `__virt_addr_valid` | kernel |
| 0.42% | `python` | `os_stat` | unknown |
| 0.41% | `python` | `_sre_SRE_Pattern_match` | library |
| 0.41% | `python` | `structseq_dealloc` | memory |
| 0.40% | `[kernel.kallsyms]` | `kmem_cache_alloc` | kernel |
| 0.40% | `python` | `PyLong_FromUnsignedLong` | int |
| 0.39% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.39% | `python` | `visit_decref` | gc |
| 0.39% | `libc-2.31.so` | `__xstat` | libc |
| 0.38% | `python` | `PyLong_FromLongLong` | int |
| 0.38% | `[kernel.kallsyms]` | `entry_SYSCALL_64` | kernel |
| 0.38% | `python` | `long_dealloc` | memory |
| 0.36% | `python` | `PyDict_GetItemWithError` | dict |
| 0.35% | `[kernel.kallsyms]` | `__kmalloc` | kernel |
| 0.35% | `python` | `unicode_decode_utf8.part.0` | str |
| 0.33% | `[kernel.kallsyms]` | `lookup_fast` | kernel |
| 0.33% | `python` | `_PyEval_Vector` | interpreter |
| 0.32% | `python` | `listiter_next` | list |
| 0.32% | `python` | `path_converter` | unknown |
| 0.31% | `[kernel.kallsyms]` | `kfree` | kernel |
| 0.30% | `python` | `PyLong_AsSsize_t` | int |
| 0.30% | `[kernel.kallsyms]` | `kmem_cache_free` | kernel |
| 0.29% | `[kernel.kallsyms]` | `walk_component` | kernel |
| 0.29% | `python` | `_pystat_fromstructstat` | unknown |
| 0.29% | `python` | `PyObject_Malloc` | dynamic |
| 0.28% | `python` | `_PyObject_GenericGetAttrWithDict` | dynamic |
| 0.28% | `[kernel.kallsyms]` | `set_root` | kernel |
| 0.28% | `python` | `drop_gil` | gil |
| 0.28% | `python` | `PyUnicode_New.part.0` | memory |
| 0.28% | `python` | `visit_reachable` | gc |
| 0.28% | `python` | `PyObject_GC_Del` | gc |
| 0.27% | `python` | `tp_new_wrapper` | memory |
| 0.27% | `[kernel.kallsyms]` | `call_filldir` | kernel |
| 0.27% | `python` | `_PyThreadState_PushFrame` | interpreter |
| 0.27% | `[kernel.kallsyms]` | `memchr` | kernel |
| 0.27% | `python` | `type_call` | dynamic |
| 0.27% | `python` | `PyFloat_FromDouble` | float |
| 0.26% | `[kernel.kallsyms]` | `ext4_search_dir` | kernel |
| 0.26% | `python` | `r_object` | import |
| 0.26% | `libc-2.31.so` | `malloc` | libc |
| 0.26% | `python` | `PyLong_FromLong` | int |
| 0.26% | `python` | `PyDict_GetItemRef` | dict |
| 0.25% | `[kernel.kallsyms]` | `vfs_getattr_nosec` | kernel |

## pickle_pure_python

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 43.29% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 4.17% | `python` | `_Py_dict_lookup` | lookup |
| 4.09% | `python` | `_PyObject_Free` | memory |
| 3.83% | `python` | `_PyObject_Malloc` | memory |
| 2.63% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.73% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 1.67% | `python` | `initialize_locals` | interpreter |
| 1.65% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.18% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.88% | `python` | `gc_collect_region.isra.0` | gc |
| 0.84% | `python` | `PyBuffer_FillInfo` | miscobj |
| 0.82% | `python` | `tupledealloc` | memory |
| 0.81% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.74% | `python` | `dict_get` | dict |
| 0.70% | `python` | `PyBuffer_Release` | miscobj |
| 0.70% | `python` | `PyLong_FromSsize_t` | int |
| 0.68% | `python` | `PyDict_GetItemRef` | dict |
| 0.67% | `python` | `PyLong_FromVoidPtr` | int |
| 0.66% | `python` | `_PyType_LookupRef` | lookup |
| 0.64% | `python` | `bytes_concat` | str |
| 0.53% | `python` | `insertdict` | dict |
| 0.52% | `python` | `write_bytes` | unknown |
| 0.50% | `python` | `_PyThreadState_PopFrame` | interpreter |
| 0.49% | `python` | `_PyTuple_FromStackRefSteal` | tuple |
| 0.46% | `libc-2.31.so` | `pthread_attr_setschedparam` | libc |
| 0.45% | `python` | `PyNumber_Add` | dynamic |
| 0.45% | `python` | `sys_audit_tstate` | unknown |
| 0.43% | `python` | `visit_decref` | gc |
| 0.43% | `python` | `PyObject_GetBuffer` | dynamic |
| 0.42% | `python` | `_Py_Dealloc` | memory |
| 0.41% | `python` | `_PyObject_GenericGetAttrWithDict` | dynamic |
| 0.40% | `python` | `r_object` | import |
| 0.36% | `python` | `long_hash` | int |
| 0.35% | `_struct.cpython-314-x86_64-linux-gnu.so` | `s_pack_internal.isra.0` | library |
| 0.35% | `python` | `PySys_Audit` | unknown |
| 0.35% | `python` | `PyUnicode_AsEncodedString.part.0` | str |
| 0.33% | `python` | `visit_reachable` | gc |
| 0.33% | `python` | `_PyObject_Realloc` | memory |
| 0.31% | `_struct.cpython-314-x86_64-linux-gnu.so` | `s_pack` | library |
| 0.31% | `python` | `PyBytes_FromStringAndSize.constprop.0` | str |
| 0.30% | `python` | `_Py_NewReference` | memory |
| 0.30% | `python` | `siphash13` | str |
| 0.29% | `python` | `dictiter_iternextitem` | dict |
| 0.29% | `python` | `_PyThreadState_PushFrame` | interpreter |
| 0.28% | `python` | `update_one_slot` | lookup |
| 0.26% | `_struct.cpython-314-x86_64-linux-gnu.so` | `pack` | library |
| 0.26% | `python` | `_Py_hashtable_get_entry_generic` | lookup |
| 0.26% | `python` | `PyObject_Malloc` | dynamic |
| 0.26% | `python` | `find_name_in_mro` | lookup |

## pidigits

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 34.78% | `python` | `x_divrem` | int |
| 23.24% | `python` | `k_mul` | int |
| 12.40% | `python` | `x_add` | int |
| 7.87% | `python` | `x_sub` | int |
| 3.80% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 2.38% | `libc-2.31.so` | `pthread_attr_setschedparam` | libc |
| 1.68% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 0.93% | `python` | `_PyObject_Malloc` | memory |
| 0.89% | `python` | `_PyObject_Free` | memory |
| 0.70% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.57% | `python` | `gc_collect_region.isra.0` | gc |
| 0.37% | `python` | `_Py_dict_lookup` | lookup |
| 0.29% | `python` | `visit_decref` | gc |
| 0.28% | `python` | `r_object` | import |

## pprint

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 40.33% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 5.11% | `python` | `_PyObject_Malloc` | memory |
| 3.91% | `python` | `_PyObject_Free` | memory |
| 3.71% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 3.67% | `python` | `_PyType_LookupRef` | lookup |
| 2.21% | `python` | `tupledealloc` | memory |
| 1.59% | `python` | `_Py_type_getattro` | lookup |
| 1.52% | `python` | `_Py_dict_lookup` | lookup |
| 1.51% | `python` | `_PyTuple_FromStackRefSteal` | tuple |
| 1.42% | `python` | `_Py_type_getattro_impl` | dynamic |
| 1.40% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.31% | `python` | `_PyUnicode_JoinArray.part.0` | str |
| 1.30% | `python` | `long_to_decimal_string_internal` | int |
| 1.06% | `python` | `PyUnicode_Format` | str |
| 1.02% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.88% | `python` | `resize_compact` | str |
| 0.74% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.73% | `python` | `set_lookkey` | miscobj |
| 0.67% | `python` | `PyUnicode_New.part.0` | memory |
| 0.63% | `python` | `_copy_characters.part.0.constprop.0` | str |
| 0.61% | `python` | `_Py_Dealloc` | memory |
| 0.58% | `python` | `_PyTuple_FromArray.part.0` | tuple |
| 0.55% | `python` | `_PyObject_Realloc` | memory |
| 0.53% | `python` | `PyObject_GC_Del` | gc |
| 0.52% | `python` | `_PyUnicodeWriter_WriteSubstring` | str |
| 0.51% | `python` | `unicode_dealloc` | memory |
| 0.49% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.49% | `python` | `_Py_NewReference` | memory |
| 0.49% | `python` | `initialize_locals` | interpreter |
| 0.48% | `python` | `PyObject_IsSubclass` | dynamic |
| 0.46% | `python` | `list_append` | list |
| 0.45% | `python` | `subtype_dealloc` | memory |
| 0.44% | `python` | `insertdict` | dict |
| 0.43% | `python` | `PyObject_GetAttr` | dynamic |
| 0.42% | `python` | `PyErr_CheckSignals` | exceptions |
| 0.41% | `python` | `list_sort_impl` | list |
| 0.41% | `python` | `PyList_New` | memory |
| 0.40% | `python` | `_PyThreadState_PopFrame` | interpreter |
| 0.39% | `python` | `_PyObject_GC_New` | gc |
| 0.39% | `python` | `long_hash` | int |
| 0.38% | `python` | `_PyObject_GC_Link` | gc |
| 0.37% | `python` | `PyObject_GenericGetAttr` | dynamic |
| 0.36% | `python` | `PyObject_GetOptionalAttr` | dynamic |
| 0.36% | `python` | `_PyObject_MakeTpCall` | dynamic |
| 0.36% | `python` | `list_dealloc` | memory |
| 0.33% | `python` | `_PyUnicodeWriter_PrepareInternal` | str |
| 0.32% | `python` | `PyType_IsSubtype` | dynamic |
| 0.32% | `python` | `_PyEval_Vector` | interpreter |
| 0.28% | `python` | `PyObject_Hash` | dynamic |
| 0.28% | `python` | `PyType_GenericAlloc` | memory |
| 0.28% | `python` | `wrapperdescr_get` | unknown |
| 0.27% | `python` | `_PySet_Contains` | miscobj |
| 0.27% | `python` | `PyObject_Repr` | dynamic |
| 0.26% | `python` | `builtin_getattr` | lookup |
| 0.26% | `python` | `PyCMethod_New` | memory |

## pycparser

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 33.77% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 13.85% | `python` | `sre_ucs1_match` | library |
| 3.77% | `python` | `gc_collect_region.isra.0` | gc |
| 2.59% | `python` | `_Py_dict_lookup` | lookup |
| 2.52% | `python` | `_PyObject_Malloc` | memory |
| 2.28% | `python` | `_PyObject_Free` | memory |
| 2.20% | `libc-2.31.so` | `pthread_attr_setschedparam` | libc |
| 1.62% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 1.41% | `python` | `_PyType_LookupRef` | lookup |
| 1.31% | `python` | `PySlice_AdjustIndices` | miscobj |
| 1.16% | `python` | `PyDict_GetItemRef` | dict |
| 1.08% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.03% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 0.97% | `python` | `_sre_SRE_Pattern_match` | library |
| 0.94% | `python` | `visit_decref` | gc |
| 0.87% | `python` | `initialize_locals` | interpreter |
| 0.87% | `python` | `subtype_traverse` | gc |
| 0.84% | `python` | `list_ass_slice_lock_held` | list |
| 0.82% | `python` | `pattern_new_match.isra.0.part.0` | memory |
| 0.77% | `python` | `visit_add_to_container` | gc |
| 0.72% | `python` | `subtype_dealloc` | memory |
| 0.70% | `python` | `sre_ucs1_count` | library |
| 0.55% | `python` | `visit_reachable` | gc |
| 0.53% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.48% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.48% | `python` | `PyNumber_AsSsize_t` | dynamic |
| 0.47% | `python` | `dict_get` | dict |
| 0.47% | `python` | `PyType_GenericAlloc` | memory |
| 0.46% | `python` | `PySlice_New` | memory |
| 0.46% | `python` | `list_subscript` | list |
| 0.45% | `python` | `sre_ucs2_charset.isra.0` | library |
| 0.45% | `python` | `slice_dealloc` | memory |
| 0.44% | `python` | `_PyObject_GenericGetAttrWithDict` | dynamic |
| 0.43% | `python` | `long_neg` | int |
| 0.42% | `python` | `PyObject_Vectorcall` | dynamic |
| 0.41% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.40% | `python` | `PyObject_ClearManagedDict` | dynamic |
| 0.38% | `libc-2.31.so` | `malloc` | libc |
| 0.37% | `python` | `list_dealloc` | memory |
| 0.35% | `python` | `list_ass_subscript` | list |
| 0.33% | `python` | `vectorcall_method` | calls |
| 0.31% | `python` | `PyList_New` | memory |
| 0.30% | `python` | `_PyEval_SliceIndex` | interpreter |
| 0.29% | `python` | `PyObject_GC_Del` | gc |
| 0.29% | `python` | `PyType_IsSubtype` | dynamic |
| 0.27% | `python` | `_Py_Dealloc` | memory |
| 0.27% | `python` | `_PyObject_MakeTpCall` | dynamic |
| 0.26% | `python` | `PySlice_Unpack` | miscobj |
| 0.26% | `python` | `_PyBuildSlice_ConsumeRefs` | miscobj |
| 0.25% | `python` | `PyObject_GetOptionalAttr` | dynamic |

## pyflate

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 43.68% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 6.09% | `python` | `list_dealloc` | memory |
| 4.42% | `python` | `_PyObject_Free` | memory |
| 3.73% | `python` | `list_ass_slice_lock_held` | list |
| 3.31% | `python` | `_PyObject_Malloc` | memory |
| 2.35% | `libc-2.31.so` | `pthread_attr_setschedparam` | libc |
| 2.28% | `python` | `PyNumber_AsSsize_t` | dynamic |
| 1.87% | `python` | `list_concat` | list |
| 1.72% | `python` | `list_slice_lock_held.isra.0` | list |
| 1.42% | `python` | `_PyLong_Add` | int |
| 1.34% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.22% | `python` | `_PyLong_Subtract` | int |
| 1.18% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.10% | `python` | `PySlice_AdjustIndices` | miscobj |
| 1.04% | `python` | `PyLong_AsSsize_t` | int |
| 0.94% | `python` | `long_lshift` | int |
| 0.84% | `python` | `stringlib_bytes_join` | str |
| 0.80% | `python` | `list_sort_impl` | list |
| 0.79% | `python` | `bytes_subscript` | str |
| 0.75% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.74% | `python` | `PyLong_FromSsize_t` | int |
| 0.64% | `python` | `_PyBuildSlice_ConsumeRefs` | miscobj |
| 0.63% | `python` | `long_lshift1` | int |
| 0.61% | `python` | `unsafe_long_compare` | unknown |
| 0.56% | `python` | `slice_dealloc` | memory |
| 0.54% | `python` | `PyObject_GetItem` | dynamic |
| 0.54% | `python` | `long_dealloc` | memory |
| 0.54% | `python` | `_Py_NewReference` | memory |
| 0.52% | `python` | `PyList_New` | memory |
| 0.44% | `python` | `long_and` | int |
| 0.43% | `python` | `_PyEval_SliceIndex` | interpreter |
| 0.41% | `python` | `PyBuffer_Release` | miscobj |
| 0.36% | `python` | `long_rshift` | int |
| 0.35% | `python` | `_PyThreadState_PopFrame` | interpreter |
| 0.34% | `python` | `PyNumber_Lshift` | dynamic |
| 0.32% | `python` | `_PyBytes_FromList` | unknown |
| 0.32% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.30% | `python` | `long_rshift1` | int |
| 0.28% | `python` | `PySlice_Unpack` | miscobj |
| 0.26% | `python` | `list_subscript` | list |

## pylint

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 22.68% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 15.34% | `python` | `gc_collect_region.isra.0` | gc |
| 4.08% | `python` | `visit_decref` | gc |
| 3.35% | `python` | `visit_reachable` | gc |
| 2.54% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 2.44% | `python` | `_PyObject_Malloc` | memory |
| 2.19% | `python` | `_PyType_LookupRef` | lookup |
| 2.14% | `python` | `visit_add_to_container` | gc |
| 2.04% | `python` | `_PyObject_Free` | memory |
| 1.69% | `python` | `_Py_dict_lookup` | lookup |
| 1.36% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.21% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.14% | `python` | `initialize_locals` | interpreter |
| 1.01% | `python` | `dict_traverse` | gc |
| 0.94% | `python` | `PyObject_VisitManagedDict` | dynamic |
| 0.88% | `python` | `list_traverse` | gc |
| 0.80% | `python` | `PyDict_GetItemRef` | dict |
| 0.64% | `python` | `PyObject_GenericGetAttr` | dynamic |
| 0.63% | `python` | `subtype_traverse` | gc |
| 0.62% | `python` | `dict_dealloc` | memory |
| 0.61% | `python` | `tupledealloc` | memory |
| 0.57% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.54% | `python` | `PyType_IsSubtype` | dynamic |
| 0.52% | `python` | `_PyGC_Collect` | gc |
| 0.48% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.44% | `python` | `insertdict` | dict |
| 0.44% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.43% | `python` | `_PyPegen_is_memoized` | interpreter |
| 0.40% | `python` | `PyObject_GetAttr` | dynamic |
| 0.39% | `python` | `list_dealloc` | memory |
| 0.38% | `python` | `_PyObject_GetMethod` | dynamic |
| 0.38% | `python` | `PyObject_GC_Del` | gc |
| 0.37% | `python` | `_Py_Dealloc` | memory |
| 0.37% | `python` | `_PyObject_GenericGetAttrWithDict` | dynamic |
| 0.36% | `python` | `islice_next` | unknown |
| 0.32% | `python` | `PyObject_ClearManagedDict` | dynamic |
| 0.31% | `python` | `_PyObject_GC_New` | gc |
| 0.30% | `python` | `PyObject_IS_GC` | gc |
| 0.30% | `python` | `find_name_in_mro` | lookup |
| 0.29% | `python` | `_PyObject_TryGetInstanceAttribute` | dynamic |
| 0.27% | `python` | `PyType_GenericAlloc` | memory |
| 0.26% | `libc-2.31.so` | `pthread_attr_setschedparam` | libc |
| 0.26% | `python` | `subtype_dealloc` | memory |
| 0.25% | `python` | `siphash13` | str |

## python_startup

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 7.27% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 5.48% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 4.38% | `python` | `gc_collect_region.isra.0` | gc |
| 3.31% | `python` | `_PyObject_Malloc` | memory |
| 3.16% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 2.79% | `python` | `_Py_dict_lookup` | lookup |
| 2.53% | `python` | `visit_decref` | gc |
| 2.18% | `python` | `visit_reachable` | gc |
| 1.82% | `ld-2.31.so` | `_dl_rtld_di_serinfo` | library |
| 1.77% | `python` | `_PyObject_Free` | memory |
| 1.61% | `python` | `r_object` | import |
| 1.46% | `python` | `find_name_in_mro` | lookup |
| 1.43% | `python` | `type_ready` | dynamic |
| 1.42% | `python` | `siphash13` | str |
| 1.36% | `python` | `_Py_hashtable_get_entry_generic` | lookup |
| 1.28% | `python` | `update_one_slot` | lookup |
| 1.06% | `python` | `_PyCode_Quicken` | interpreter |
| 0.94% | `python` | `_PyType_LookupRef` | lookup |
| 0.93% | `libc-2.31.so` | `pthread_attr_setschedparam` | libc |
| 0.91% | `python` | `ascii_decode` | str |
| 0.89% | `python` | `tupledealloc` | memory |
| 0.87% | `python` | `dict_traverse` | gc |
| 0.76% | `python` | `_PyUnicode_FromUCS1.part.0` | str |
| 0.75% | `python` | `insertdict` | dict |
| 0.73% | `[kernel.kallsyms]` | `native_irq_return_iret` | kernel |
| 0.68% | `[kernel.kallsyms]` | `filemap_map_pages` | kernel |
| 0.60% | `python` | `dict_setdefault_ref_lock_held` | dict |
| 0.60% | `python` | `_PyDict_GetItemRef_KnownHash` | dict |
| 0.55% | `python` | `build_indices_unicode` | dict |
| 0.54% | `python` | `intern_constants` | str |
| 0.53% | `[kernel.kallsyms]` | `sync_regs` | kernel |
| 0.51% | `libc-2.31.so` | `__gconv_get_alias_db` | libc |
| 0.48% | `libc-2.31.so` | `wcsrtombs` | libc |
| 0.47% | `python` | `intern_common.part.0` | str |
| 0.46% | `python` | `_Py_Dealloc` | memory |
| 0.43% | `python` | `dict_dealloc` | memory |
| 0.43% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 0.42% | `python` | `PyDict_GetItemRef` | dict |
| 0.41% | `[kernel.kallsyms]` | `clear_page_erms` | kernel |
| 0.41% | `python` | `PyObject_IS_GC` | gc |
| 0.39% | `python` | `_Py_GetBaseOpcode` | interpreter |
| 0.36% | `python` | `list_dealloc` | memory |
| 0.36% | `python` | `initialize_locals` | interpreter |
| 0.35% | `ld-2.31.so` | `_dl_catch_error` | library |
| 0.35% | `python` | `PyType_GenericAlloc` | memory |
| 0.35% | `python` | `find_empty_slot` | dict |
| 0.34% | `python` | `code_dealloc` | memory |
| 0.34% | `python` | `PyUnicode_New.part.0` | memory |
| 0.34% | `python` | `_PyCode_New` | interpreter |
| 0.31% | `[kernel.kallsyms]` | `zap_pte_range.isra.0` | kernel |
| 0.29% | `python` | `unicode_decode_utf8.part.0` | str |
| 0.29% | `python` | `tupletraverse` | tuple |
| 0.28% | `[kernel.kallsyms]` | `__handle_mm_fault` | kernel |
| 0.28% | `python` | `PyObject_GC_Del` | gc |
| 0.28% | `python` | `set_traverse` | gc |
| 0.26% | `python` | `PyTuple_New` | memory |
| 0.26% | `python` | `_PyUnicode_InternImmortal` | str |
| 0.25% | `[kernel.kallsyms]` | `_raw_spin_lock` | kernel |

## python_startup_no_site

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 7.13% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 5.06% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 4.47% | `python` | `gc_collect_region.isra.0` | gc |
| 3.29% | `python` | `_PyObject_Malloc` | memory |
| 3.15% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 2.83% | `ld-2.31.so` | `_dl_rtld_di_serinfo` | library |
| 2.54% | `python` | `_Py_dict_lookup` | lookup |
| 2.42% | `python` | `visit_decref` | gc |
| 2.07% | `python` | `visit_reachable` | gc |
| 1.79% | `python` | `type_ready` | dynamic |
| 1.74% | `python` | `_PyObject_Free` | memory |
| 1.60% | `python` | `siphash13` | str |
| 1.25% | `python` | `_Py_hashtable_get_entry_generic` | lookup |
| 1.25% | `python` | `find_name_in_mro` | lookup |
| 1.22% | `python` | `r_object` | import |
| 1.06% | `python` | `ascii_decode` | str |
| 1.06% | `python` | `update_one_slot` | lookup |
| 0.99% | `[kernel.kallsyms]` | `native_irq_return_iret` | kernel |
| 0.93% | `python` | `_PyType_LookupRef` | lookup |
| 0.89% | `libc-2.31.so` | `pthread_attr_setschedparam` | libc |
| 0.86% | `python` | `dict_traverse` | gc |
| 0.77% | `python` | `_PyCode_Quicken` | interpreter |
| 0.76% | `python` | `tupledealloc` | memory |
| 0.73% | `[kernel.kallsyms]` | `filemap_map_pages` | kernel |
| 0.70% | `python` | `insertdict` | dict |
| 0.69% | `libc-2.31.so` | `__gconv_get_alias_db` | libc |
| 0.68% | `libc-2.31.so` | `wcsrtombs` | libc |
| 0.66% | `[kernel.kallsyms]` | `sync_regs` | kernel |
| 0.65% | `python` | `dict_setdefault_ref_lock_held` | dict |
| 0.53% | `python` | `_PyUnicode_FromUCS1.part.0` | str |
| 0.53% | `python` | `build_indices_unicode` | dict |
| 0.52% | `ld-2.31.so` | `_dl_catch_error` | library |
| 0.48% | `[kernel.kallsyms]` | `clear_page_erms` | kernel |
| 0.48% | `python` | `_PyDict_GetItemRef_KnownHash` | dict |
| 0.47% | `python` | `intern_constants` | str |
| 0.46% | `python` | `intern_common.part.0` | str |
| 0.45% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 0.44% | `[kernel.kallsyms]` | `copy_page` | kernel |
| 0.44% | `python` | `initialize_locals` | interpreter |
| 0.42% | `python` | `dict_dealloc` | memory |
| 0.41% | `[kernel.kallsyms]` | `zap_pte_range.isra.0` | kernel |
| 0.40% | `python` | `_Py_Dealloc` | memory |
| 0.40% | `python` | `unicode_decode_utf8.part.0` | str |
| 0.40% | `python` | `PyUnicode_New.part.0` | memory |
| 0.37% | `[kernel.kallsyms]` | `__handle_mm_fault` | kernel |
| 0.37% | `python` | `PyDict_GetItemRef` | dict |
| 0.36% | `python` | `find_empty_slot` | dict |
| 0.36% | `python` | `_Py_GetBaseOpcode` | interpreter |
| 0.36% | `python` | `PyType_GenericAlloc` | memory |
| 0.33% | `python` | `PyObject_IS_GC` | gc |
| 0.30% | `python` | `code_dealloc` | memory |
| 0.29% | `[kernel.kallsyms]` | `release_pages` | kernel |
| 0.26% | `[kernel.kallsyms]` | `_raw_spin_lock` | kernel |
| 0.26% | `python` | `PyObject_GC_Del` | gc |
| 0.26% | `python` | `tupletraverse` | tuple |
| 0.25% | `python` | `list_dealloc` | memory |

## raytrace

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 52.75% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 4.29% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 2.36% | `python` | `_PyObject_Free` | memory |
| 2.17% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.81% | `python` | `_PyObject_Malloc` | memory |
| 1.60% | `python` | `float_dealloc` | memory |
| 1.44% | `python` | `subtype_dealloc` | memory |
| 1.30% | `python` | `_PyType_NewManagedObject` | memory |
| 1.27% | `python` | `PyType_IsSubtype` | dynamic |
| 1.22% | `python` | `PyFloat_FromDouble` | float |
| 1.20% | `python` | `PyObject_ClearManagedDict` | dynamic |
| 1.19% | `python` | `_PyThreadState_PopFrame` | interpreter |
| 1.16% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.10% | `python` | `_Py_Dealloc` | memory |
| 1.02% | `python` | `float_sub` | float |
| 1.01% | `python` | `PyNumber_Subtract` | dynamic |
| 0.91% | `python` | `_Py_NewReference` | memory |
| 0.90% | `python` | `_PyType_LookupRef` | lookup |
| 0.78% | `python` | `PyLong_AsDouble` | int |
| 0.70% | `python` | `initialize_locals` | interpreter |
| 0.65% | `python` | `PyObject_GC_Del` | gc |
| 0.61% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.60% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.58% | `python` | `float_richcompare` | float |
| 0.51% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.51% | `python` | `tupledealloc` | memory |
| 0.49% | `python` | `PyObject_ClearWeakRefs` | dynamic |
| 0.47% | `python` | `vectorcall_maybe.constprop.0` | unknown |
| 0.46% | `python` | `float_mul` | float |
| 0.46% | `python` | `_PyFloat_ExactDealloc` | memory |
| 0.43% | `python` | `PyNumber_Multiply` | dynamic |
| 0.41% | `python` | `_PyTuple_FromStackRefSteal` | tuple |
| 0.39% | `python` | `_PyEval_Vector` | interpreter |
| 0.39% | `python` | `gc_collect_region.isra.0` | gc |
| 0.34% | `python` | `_PyObject_GC_Link` | gc |
| 0.32% | `python` | `slot_nb_subtract` | unknown |
| 0.27% | `python` | `_PyObject_InitInlineValues` | dynamic |
| 0.27% | `python` | `PyObject_RichCompare` | dynamic |
| 0.27% | `python` | `float_div` | float |
| 0.26% | `python` | `long_sub` | int |

## regex_compile

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 42.49% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 4.23% | `python` | `_PyObject_Malloc` | memory |
| 3.93% | `python` | `sre_ucs1_match` | library |
| 3.20% | `python` | `_PyObject_Free` | memory |
| 1.96% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.48% | `python` | `_PyType_LookupRef` | lookup |
| 1.41% | `python` | `PyNumber_AsSsize_t` | dynamic |
| 1.26% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.04% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.87% | `python` | `bytearray_ass_subscript` | miscobj |
| 0.79% | `python` | `tupledealloc` | memory |
| 0.77% | `python` | `sre_ucs2_charset.isra.0` | library |
| 0.76% | `python` | `_Py_dict_lookup` | lookup |
| 0.71% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.69% | `python` | `PyLong_FromLong` | int |
| 0.63% | `python` | `gc_collect_region.isra.0` | gc |
| 0.59% | `python` | `sre_search` | library |
| 0.58% | `python` | `initialize_locals` | interpreter |
| 0.58% | `python` | `_PyTuple_FromStackRefSteal` | tuple |
| 0.56% | `python` | `list_dealloc` | memory |
| 0.50% | `python` | `PyUnicode_Contains` | str |
| 0.49% | `python` | `PyObject_GC_Del` | gc |
| 0.46% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.44% | `python` | `PyObject_GenericGetAttr` | dynamic |
| 0.42% | `python` | `_PyObject_GenericGetAttrWithDict` | dynamic |
| 0.41% | `python` | `_Py_Dealloc` | memory |
| 0.41% | `libc-2.31.so` | `pthread_attr_setschedparam` | libc |
| 0.40% | `python` | `_PyObject_GC_New` | gc |
| 0.40% | `python` | `PyObject_SetItem` | dynamic |
| 0.40% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.38% | `python` | `list_append` | list |
| 0.37% | `python` | `PyType_IsSubtype` | dynamic |
| 0.37% | `python` | `PyLong_AsLongAndOverflow` | int |
| 0.37% | `python` | `PyObject_GetAttr` | dynamic |
| 0.37% | `python` | `_PyObject_Realloc` | memory |
| 0.37% | `python` | `siphash13` | str |
| 0.35% | `python` | `visit_decref` | gc |
| 0.35% | `python` | `PyLong_AsSsize_t` | int |
| 0.33% | `python` | `set_lookkey` | miscobj |
| 0.33% | `python` | `min_max` | unknown |
| 0.32% | `python` | `sre_ucs1_count` | library |
| 0.32% | `python` | `_PyThreadState_PopFrame` | interpreter |
| 0.30% | `python` | `_Py_NewReference` | memory |
| 0.29% | `python` | `_PyLong_Add` | int |
| 0.29% | `python` | `PyList_New` | memory |
| 0.29% | `python` | `PyDict_GetItemRef` | dict |
| 0.27% | `python` | `visit_reachable` | gc |
| 0.26% | `python` | `r_object` | import |
| 0.25% | `python` | `compute_range_length` | unknown |

## regex_dna

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 34.97% | `python` | `sre_ucs1_match` | library |
| 26.37% | `python` | `sre_ucs2_charset.isra.0` | library |
| 8.42% | `python` | `sre_search` | library |
| 6.60% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 3.53% | `libm-2.31.so` | `__fmod_finite` | library |
| 1.39% | `_bisect.cpython-314-x86_64-linux-gnu.so` | `_bisect_bisect_right` | library |
| 1.20% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.02% | `python` | `pattern_subx` | library |
| 0.71% | `python` | `_PyObject_Malloc` | memory |
| 0.67% | `python` | `float_richcompare` | float |
| 0.66% | `python` | `float_rem` | float |
| 0.58% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.47% | `python` | `stringlib_bytes_join` | str |
| 0.46% | `python` | `float_div` | float |
| 0.45% | `python` | `float_dealloc` | memory |
| 0.42% | `python` | `_PyObject_Free` | memory |
| 0.40% | `python` | `gc_collect_region.isra.0` | gc |
| 0.40% | `python` | `list_item` | list |
| 0.37% | `python` | `bytearray_ass_subscript` | miscobj |
| 0.33% | `libc-2.31.so` | `pthread_attr_setschedparam` | libc |
| 0.28% | `python` | `PyBuffer_Release` | miscobj |
| 0.27% | `python` | `_Py_dict_lookup` | lookup |
| 0.25% | `python` | `visit_decref` | gc |

## regex_effbot

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 40.67% | `python` | `sre_ucs1_match` | library |
| 14.13% | `python` | `sre_ucs2_charset.isra.0` | library |
| 7.76% | `python` | `_PyObject_Free` | memory |
| 6.76% | `python` | `sre_search` | library |
| 5.90% | `python` | `_PyObject_Malloc` | memory |
| 3.80% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 2.29% | `python` | `sre_ucs1_count` | library |
| 1.04% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.78% | `python` | `gc_collect_region.isra.0` | gc |
| 0.75% | `python` | `PyMem_Malloc` | memory |
| 0.58% | `python` | `_Py_dict_lookup` | lookup |
| 0.53% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 0.46% | `python` | `siphash13` | str |
| 0.44% | `libc-2.31.so` | `pthread_attr_setschedparam` | libc |
| 0.42% | `python` | `PyMem_Free` | memory |
| 0.41% | `python` | `visit_decref` | gc |
| 0.34% | `python` | `visit_reachable` | gc |
| 0.30% | `python` | `r_object` | import |
| 0.28% | `python` | `tupledealloc` | memory |

## regex_v8

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 35.56% | `python` | `sre_ucs1_match` | library |
| 8.16% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 4.16% | `python` | `sre_ucs1_count` | library |
| 4.10% | `python` | `sre_search` | library |
| 3.80% | `python` | `PyCode_Addr2Line` | exceptions |
| 3.20% | `python` | `_PyObject_Malloc` | memory |
| 2.94% | `python` | `_PyObject_Free` | memory |
| 2.03% | `libc-2.31.so` | `pthread_attr_setschedparam` | libc |
| 1.72% | `python` | `pattern_subx` | library |
| 1.33% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 1.31% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.14% | `python` | `pattern_new_match.isra.0.part.0` | memory |
| 1.06% | `python` | `_sre_SRE_Pattern_search` | library |
| 1.01% | `python` | `_Py_dict_lookup` | lookup |
| 0.82% | `python` | `gc_collect_region.isra.0` | gc |
| 0.61% | `libc-2.31.so` | `malloc` | libc |
| 0.50% | `python` | `_PyUnicode_JoinArray.part.0` | str |
| 0.49% | `python` | `visit_decref` | gc |
| 0.46% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 0.46% | `python` | `_PyUnicode_IsAlpha` | str |
| 0.44% | `python` | `_PyUnicode_ToLowercase` | str |
| 0.41% | `python` | `_PyType_LookupRef` | lookup |
| 0.39% | `python` | `PyUnicode_Contains` | str |
| 0.37% | `python` | `visit_reachable` | gc |
| 0.36% | `python` | `PyNumber_AsSsize_t` | dynamic |
| 0.35% | `python` | `siphash13` | str |
| 0.35% | `python` | `PyDict_GetItemRef` | dict |
| 0.34% | `python` | `_PyPegen_is_memoized` | interpreter |
| 0.33% | `python` | `PyList_Append` | list |
| 0.32% | `python` | `PyUnicode_Substring` | str |
| 0.31% | `python` | `_PyObject_Realloc` | memory |
| 0.31% | `python` | `list_dealloc` | memory |
| 0.30% | `python` | `tupledealloc` | memory |
| 0.30% | `python` | `r_object` | import |
| 0.27% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.26% | `python` | `bytearray_ass_subscript` | miscobj |
| 0.26% | `python` | `sre_ucs2_charset.isra.0` | library |

## richards

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 54.34% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 4.64% | `python` | `_PyType_LookupRef` | lookup |
| 4.60% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 3.19% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 2.65% | `python` | `PyObject_GenericGetAttr` | dynamic |
| 2.22% | `python` | `_PyObject_TryGetInstanceAttribute` | dynamic |
| 1.85% | `python` | `_PyObject_GetMethod` | dynamic |
| 1.69% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.28% | `python` | `_PyObject_Free` | memory |
| 1.10% | `python` | `_PyObject_Malloc` | memory |
| 1.02% | `python` | `PyObject_GetAttr` | dynamic |
| 0.93% | `python` | `gc_collect_region.isra.0` | gc |
| 0.91% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 0.72% | `python` | `_PyThreadState_PopFrame` | interpreter |
| 0.58% | `python` | `_Py_dict_lookup` | lookup |
| 0.57% | `python` | `initialize_locals` | interpreter |
| 0.54% | `python` | `visit_decref` | gc |
| 0.41% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.40% | `python` | `r_object` | import |
| 0.36% | `python` | `visit_reachable` | gc |
| 0.35% | `python` | `_PyType_GetDict` | dynamic |
| 0.31% | `python` | `PyObject_GenericSetAttr` | dynamic |
| 0.31% | `python` | `update_one_slot` | lookup |
| 0.30% | `python` | `_PyLong_Add` | int |
| 0.28% | `python` | `find_name_in_mro` | lookup |
| 0.27% | `python` | `_PyCode_Quicken` | interpreter |
| 0.26% | `python` | `PyObject_SetAttr` | dynamic |
| 0.26% | `python` | `store_instance_attr_lock_held` | unknown |

## richards_super

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 57.37% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 4.78% | `python` | `_PyType_LookupRef` | lookup |
| 4.73% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 3.45% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 2.41% | `python` | `PyObject_GenericGetAttr` | dynamic |
| 2.30% | `python` | `_PyObject_TryGetInstanceAttribute` | dynamic |
| 2.03% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.71% | `python` | `_PyObject_GetMethod` | dynamic |
| 1.18% | `python` | `_PyObject_Free` | memory |
| 1.17% | `python` | `PyObject_GetAttr` | dynamic |
| 0.82% | `python` | `_PyObject_Malloc` | memory |
| 0.78% | `python` | `_PyThreadState_PopFrame` | interpreter |
| 0.75% | `python` | `_Py_dict_lookup` | lookup |
| 0.66% | `python` | `PyDict_GetItemRef` | dict |
| 0.65% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 0.61% | `python` | `PyObject_GenericSetAttr` | dynamic |
| 0.58% | `python` | `PyObject_SetAttr` | dynamic |
| 0.57% | `python` | `do_super_lookup` | dynamic |
| 0.56% | `python` | `gc_collect_region.isra.0` | gc |
| 0.56% | `python` | `store_instance_attr_lock_held` | unknown |
| 0.46% | `python` | `_PySuper_Lookup` | dynamic |
| 0.42% | `python` | `initialize_locals` | interpreter |
| 0.38% | `python` | `_PyType_GetDict` | dynamic |
| 0.36% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.29% | `python` | `_PyLong_Add` | int |
| 0.27% | `python` | `r_object` | import |
| 0.27% | `python` | `visit_decref` | gc |
| 0.26% | `python` | `_PyUnicode_InternMortal` | str |

## scimark

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 40.61% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 5.65% | `python` | `PyNumber_AsSsize_t` | dynamic |
| 4.45% | `python` | `_PyObject_Free` | memory |
| 3.81% | `array.cpython-314-x86_64-linux-gnu.so` | `array_subscr` | library |
| 3.74% | `python` | `_PyObject_Malloc` | memory |
| 2.90% | `python` | `PyFloat_FromDouble` | float |
| 2.59% | `python` | `PyObject_GetItem` | dynamic |
| 2.36% | `python` | `vgetargs1_impl` | calls |
| 1.93% | `python` | `_PyLong_Add` | int |
| 1.67% | `python` | `convertitem.constprop.0` | library |
| 1.66% | `python` | `PyLong_AsSsize_t` | int |
| 1.33% | `array.cpython-314-x86_64-linux-gnu.so` | `array_ass_subscr` | library |
| 1.30% | `python` | `_Py_NewReference` | memory |
| 1.24% | `python` | `float_dealloc` | memory |
| 1.14% | `python` | `PyLong_FromLong` | int |
| 1.03% | `python` | `PyIndex_Check` | unknown |
| 1.00% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 0.89% | `python` | `PyType_GetModuleByDef` | dynamic |
| 0.79% | `python` | `PyArg_Parse` | calls |
| 0.79% | `array.cpython-314-x86_64-linux-gnu.so` | `d_setitem` | library |
| 0.75% | `python` | `_PyLong_Multiply` | int |
| 0.74% | `python` | `long_dealloc` | memory |
| 0.71% | `python` | `PyObject_SetItem` | dynamic |
| 0.66% | `python` | `_PyFloat_ExactDealloc` | memory |
| 0.57% | `python` | `_PyType_LookupRef` | lookup |
| 0.54% | `python` | `PyType_IsSubtype` | dynamic |
| 0.52% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.45% | `python` | `_PyObject_GenericGetAttrWithDict` | dynamic |
| 0.44% | `python` | `_PyTuple_FromStackRefSteal` | tuple |
| 0.44% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.38% | `array.cpython-314-x86_64-linux-gnu.so` | `d_getitem` | library |
| 0.37% | `python` | `_PyLong_Frexp` | int |
| 0.36% | `python` | `tupledealloc` | memory |
| 0.34% | `array.cpython-314-x86_64-linux-gnu.so` | `0x0000000000004644` | library |
| 0.34% | `array.cpython-314-x86_64-linux-gnu.so` | `0x00000000000047e4` | library |
| 0.32% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 0.32% | `python` | `_PyLong_Subtract` | int |
| 0.31% | `array.cpython-314-x86_64-linux-gnu.so` | `0x00000000000049c4` | library |
| 0.30% | `python` | `float_richcompare` | float |
| 0.28% | `python` | `gc_collect_region.isra.0` | gc |
| 0.25% | `python` | `PyObject_Malloc` | dynamic |

## spectral_norm

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 34.34% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 9.36% | `python` | `_PyObject_Free` | memory |
| 8.31% | `python` | `_PyLong_Add` | int |
| 7.33% | `python` | `_PyObject_Malloc` | memory |
| 3.03% | `python` | `float_div` | float |
| 3.01% | `python` | `long_div` | int |
| 2.38% | `python` | `_PyLong_Multiply` | int |
| 2.16% | `python` | `listiter_next` | list |
| 2.15% | `python` | `enum_next` | miscobj |
| 1.74% | `python` | `PyType_IsSubtype` | dynamic |
| 1.67% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.38% | `python` | `_Py_NewReference` | memory |
| 1.37% | `python` | `PyLong_FromLong` | int |
| 1.10% | `python` | `PyNumber_TrueDivide` | dynamic |
| 0.98% | `python` | `long_dealloc` | memory |
| 0.97% | `python` | `PyLong_AsDouble` | int |
| 0.97% | `python` | `PyNumber_FloorDivide` | dynamic |
| 0.96% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.93% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.79% | `python` | `PyLong_FromSsize_t` | int |
| 0.65% | `python` | `PyObject_Malloc` | dynamic |
| 0.58% | `python` | `gc_collect_region.isra.0` | gc |
| 0.57% | `python` | `float_dealloc` | memory |
| 0.55% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 0.53% | `python` | `_PyThreadState_PopFrame` | interpreter |
| 0.48% | `python` | `PyObject_Free` | dynamic |
| 0.45% | `python` | `_Py_dict_lookup` | lookup |
| 0.37% | `python` | `visit_decref` | gc |
| 0.32% | `python` | `r_object` | import |
| 0.28% | `python` | `visit_reachable` | gc |

## sqlglot

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 31.16% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 4.63% | `python` | `_PyObject_Free` | memory |
| 4.11% | `python` | `_PyObject_Malloc` | memory |
| 2.92% | `python` | `_PyType_LookupRef` | lookup |
| 1.98% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 1.94% | `python` | `PyType_IsSubtype` | dynamic |
| 1.76% | `python` | `tupledealloc` | memory |
| 1.56% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.37% | `python` | `_PyObject_GenericGetAttrWithDict` | dynamic |
| 1.32% | `python` | `dictiter_iternextitem` | dict |
| 1.23% | `python` | `_Py_dict_lookup` | lookup |
| 1.17% | `python` | `gc_collect_region.isra.0` | gc |
| 1.16% | `python` | `PyObject_GC_Del` | gc |
| 1.14% | `python` | `_PyTuple_FromStackRefSteal` | tuple |
| 1.11% | `python` | `_PyObject_LookupSpecial` | dynamic |
| 1.05% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.05% | `python` | `_PyObject_GC_New` | gc |
| 0.90% | `python` | `PyObject_IsInstance` | dynamic |
| 0.83% | `python` | `object_isinstance` | dynamic |
| 0.83% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.81% | `python` | `PyObject_GetOptionalAttr` | dynamic |
| 0.78% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.72% | `python` | `initialize_locals` | interpreter |
| 0.70% | `python` | `_Py_Dealloc` | memory |
| 0.62% | `python` | `insert_to_emptydict` | dict |
| 0.57% | `python` | `visit_decref` | gc |
| 0.54% | `python` | `_PyObject_GC_Link` | gc |
| 0.54% | `python` | `visit_reachable` | gc |
| 0.53% | `python` | `_PyObject_RealIsInstance` | dynamic |
| 0.52% | `python` | `siphash13` | str |
| 0.52% | `python` | `PyCMethod_New` | memory |
| 0.49% | `python` | `PyTuple_Pack` | tuple |
| 0.49% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.46% | `python` | `PyObject_CallOneArg` | dynamic |
| 0.46% | `python` | `dict_dealloc` | memory |
| 0.45% | `python` | `_PyObject_Calloc` | memory |
| 0.45% | `python` | `getset_get` | dynamic |
| 0.43% | `python` | `_Py_NewReference` | memory |
| 0.42% | `python` | `meth_dealloc` | memory |
| 0.42% | `python` | `gen_dealloc` | memory |
| 0.41% | `python` | `r_object` | import |
| 0.38% | `python` | `_PyObject_GC_NewVar` | gc |
| 0.38% | `python` | `find_name_in_mro` | lookup |
| 0.37% | `python` | `PyObject_GenericGetAttr` | dynamic |
| 0.36% | `python` | `PyFunction_NewWithQualName` | memory |
| 0.35% | `python` | `cfunction_vectorcall_O` | calls |
| 0.35% | `python` | `_PyThreadState_PopFrame` | interpreter |
| 0.35% | `python` | `_PyObject_Realloc` | memory |
| 0.34% | `python` | `list_dealloc` | memory |
| 0.34% | `python` | `update_one_slot` | lookup |
| 0.33% | `python` | `PyObject_GetAttr` | dynamic |
| 0.31% | `python` | `_Py_hashtable_get_entry_generic` | lookup |
| 0.29% | `python` | `PyList_New` | memory |
| 0.29% | `libc-2.31.so` | `pthread_attr_setschedparam` | libc |
| 0.27% | `python` | `gen_iternext` | miscobj |
| 0.27% | `python` | `PyObject_IsTrue` | dynamic |
| 0.26% | `python` | `tuplehash` | tuple |
| 0.25% | `python` | `dictitems_iter` | unknown |

## sqlglot_optimize

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 30.26% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 4.26% | `python` | `_PyObject_Free` | memory |
| 3.85% | `python` | `_PyObject_Malloc` | memory |
| 3.23% | `python` | `_PyType_LookupRef` | lookup |
| 2.39% | `python` | `PyType_IsSubtype` | dynamic |
| 2.09% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 1.63% | `python` | `tupledealloc` | memory |
| 1.62% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.61% | `python` | `_PyObject_GenericGetAttrWithDict` | dynamic |
| 1.49% | `python` | `dictiter_iternextitem` | dict |
| 1.39% | `python` | `_Py_dict_lookup` | lookup |
| 1.26% | `python` | `gc_collect_region.isra.0` | gc |
| 1.25% | `python` | `PyObject_GC_Del` | gc |
| 1.16% | `python` | `_PyObject_LookupSpecial` | dynamic |
| 1.06% | `python` | `_PyTuple_FromStackRefSteal` | tuple |
| 1.06% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.01% | `python` | `_PyObject_GC_New` | gc |
| 0.96% | `python` | `PyObject_GetOptionalAttr` | dynamic |
| 0.95% | `python` | `PyObject_IsInstance` | dynamic |
| 0.89% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.83% | `python` | `object_isinstance` | dynamic |
| 0.67% | `python` | `_Py_Dealloc` | memory |
| 0.67% | `python` | `visit_decref` | gc |
| 0.66% | `python` | `initialize_locals` | interpreter |
| 0.62% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.61% | `python` | `PyCMethod_New` | memory |
| 0.56% | `python` | `PyObject_CallOneArg` | dynamic |
| 0.55% | `python` | `siphash13` | str |
| 0.55% | `python` | `_PyObject_RealIsInstance` | dynamic |
| 0.53% | `python` | `getset_get` | dynamic |
| 0.50% | `python` | `PyObject_GenericGetAttr` | dynamic |
| 0.50% | `python` | `visit_reachable` | gc |
| 0.50% | `python` | `_PyObject_Calloc` | memory |
| 0.50% | `python` | `dict_dealloc` | memory |
| 0.50% | `python` | `_PyObject_GC_Link` | gc |
| 0.46% | `python` | `_Py_NewReference` | memory |
| 0.46% | `python` | `insert_to_emptydict` | dict |
| 0.46% | `python` | `list_dealloc` | memory |
| 0.45% | `python` | `meth_dealloc` | memory |
| 0.43% | `python` | `PyObject_GetAttr` | dynamic |
| 0.42% | `python` | `r_object` | import |
| 0.40% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.37% | `python` | `cfunction_vectorcall_O` | calls |
| 0.37% | `python` | `tuplehash` | tuple |
| 0.36% | `python` | `find_name_in_mro` | lookup |
| 0.35% | `python` | `insertdict` | dict |
| 0.35% | `python` | `PyList_New` | memory |
| 0.34% | `python` | `PyTuple_Pack` | tuple |
| 0.30% | `python` | `update_one_slot` | lookup |
| 0.30% | `python` | `_PyCode_Quicken` | interpreter |
| 0.29% | `python` | `PyMember_GetOne` | lookup |
| 0.29% | `python` | `_PyType_GetDict` | dynamic |
| 0.28% | `python` | `_PyThreadState_PopFrame` | interpreter |
| 0.28% | `python` | `dict_get` | dict |
| 0.28% | `python` | `PyFunction_NewWithQualName` | memory |
| 0.28% | `python` | `PyObject_IsTrue` | dynamic |
| 0.27% | `python` | `PyObject_Hash` | dynamic |
| 0.27% | `python` | `_Py_hashtable_get_entry_generic` | lookup |
| 0.27% | `python` | `PyObject_Malloc` | dynamic |
| 0.26% | `libc-2.31.so` | `pthread_attr_setschedparam` | libc |
| 0.26% | `python` | `_PyObject_Realloc` | memory |

## sqlglot_parse

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 45.43% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 2.85% | `python` | `_PyType_LookupRef` | lookup |
| 2.81% | `python` | `_PyObject_Free` | memory |
| 2.81% | `python` | `_PyObject_Malloc` | memory |
| 2.33% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 2.32% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 2.09% | `python` | `gc_collect_region.isra.0` | gc |
| 1.89% | `python` | `_Py_dict_lookup` | lookup |
| 1.74% | `python` | `initialize_locals` | interpreter |
| 1.04% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.02% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.99% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.85% | `python` | `visit_decref` | gc |
| 0.76% | `python` | `PyObject_GetAttr` | dynamic |
| 0.70% | `python` | `PyObject_RichCompare` | dynamic |
| 0.66% | `python` | `_PyLong_Add` | int |
| 0.54% | `python` | `dict_dealloc` | memory |
| 0.52% | `python` | `tupledealloc` | memory |
| 0.49% | `python` | `PyType_IsSubtype` | dynamic |
| 0.48% | `python` | `_Py_type_getattro` | lookup |
| 0.48% | `python` | `_PyThreadState_PopFrame` | interpreter |
| 0.46% | `python` | `_Py_Dealloc` | memory |
| 0.45% | `python` | `visit_reachable` | gc |
| 0.38% | `python` | `subtype_dealloc` | memory |
| 0.37% | `python` | `insert_to_emptydict` | dict |
| 0.37% | `python` | `dictiter_iternextitem` | dict |
| 0.36% | `python` | `r_object` | import |
| 0.35% | `python` | `_PyLong_Subtract` | int |
| 0.35% | `python` | `find_name_in_mro` | lookup |
| 0.34% | `python` | `_PyObject_GC_New` | gc |
| 0.34% | `python` | `PyObject_GC_Del` | gc |
| 0.33% | `python` | `dict_traverse` | gc |
| 0.33% | `python` | `PyObject_GenericGetAttr` | dynamic |
| 0.31% | `python` | `_PyThreadState_PushFrame` | interpreter |
| 0.31% | `python` | `subtype_traverse` | gc |
| 0.30% | `python` | `insertdict` | dict |
| 0.29% | `python` | `dict_get` | dict |
| 0.29% | `python` | `update_one_slot` | lookup |
| 0.28% | `python` | `_Py_NewReference` | memory |
| 0.27% | `python` | `siphash13` | str |
| 0.26% | `python` | `_PyObject_LookupSpecial` | dynamic |
| 0.26% | `python` | `PyObject_RichCompareBool` | dynamic |
| 0.26% | `python` | `_PyCode_Quicken` | interpreter |
| 0.26% | `python` | `PyObject_GC_UnTrack` | gc |

## sqlglot_transpile

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 40.33% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 2.98% | `python` | `_PyObject_Free` | memory |
| 2.98% | `python` | `_PyObject_Malloc` | memory |
| 2.92% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 2.79% | `python` | `_PyType_LookupRef` | lookup |
| 2.22% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 2.15% | `python` | `_Py_dict_lookup` | lookup |
| 2.03% | `python` | `gc_collect_region.isra.0` | gc |
| 1.68% | `python` | `initialize_locals` | interpreter |
| 1.34% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 0.90% | `python` | `visit_decref` | gc |
| 0.88% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.80% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.70% | `python` | `PyType_IsSubtype` | dynamic |
| 0.67% | `python` | `PyObject_GetAttr` | dynamic |
| 0.61% | `python` | `tupledealloc` | memory |
| 0.54% | `python` | `visit_reachable` | gc |
| 0.53% | `python` | `find_name_in_mro` | lookup |
| 0.51% | `python` | `siphash13` | str |
| 0.51% | `python` | `_Py_Dealloc` | memory |
| 0.50% | `python` | `dict_dealloc` | memory |
| 0.49% | `python` | `PyObject_RichCompare` | dynamic |
| 0.49% | `python` | `r_object` | import |
| 0.49% | `python` | `PyObject_GenericGetAttr` | dynamic |
| 0.46% | `python` | `_PyLong_Add` | int |
| 0.41% | `python` | `_PyObject_GC_New` | gc |
| 0.40% | `python` | `PyObject_GC_Del` | gc |
| 0.38% | `python` | `_Py_type_getattro` | lookup |
| 0.38% | `python` | `_PyThreadState_PopFrame` | interpreter |
| 0.37% | `python` | `_PyObject_GenericGetAttrWithDict` | dynamic |
| 0.36% | `python` | `update_one_slot` | lookup |
| 0.35% | `python` | `subtype_dealloc` | memory |
| 0.35% | `python` | `dict_get` | dict |
| 0.34% | `python` | `dictiter_iternextitem` | dict |
| 0.33% | `python` | `insertdict` | dict |
| 0.32% | `python` | `_PyCode_Quicken` | interpreter |
| 0.32% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.32% | `python` | `insert_to_emptydict` | dict |
| 0.31% | `python` | `_PyObject_LookupSpecial` | dynamic |
| 0.30% | `python` | `_Py_NewReference` | memory |
| 0.29% | `python` | `dict_traverse` | gc |
| 0.28% | `libc-2.31.so` | `pthread_attr_setschedparam` | libc |
| 0.28% | `python` | `PyObject_IsTrue` | dynamic |
| 0.28% | `python` | `_PyDict_GetItemRef_KnownHash` | dict |
| 0.28% | `python` | `_PyUnicode_JoinArray.part.0` | str |
| 0.27% | `python` | `_Py_hashtable_get_entry_generic` | lookup |
| 0.25% | `python` | `_PyObject_GC_Link` | gc |
| 0.25% | `python` | `subtype_traverse` | gc |

## sympy

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 27.48% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 3.81% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 3.65% | `python` | `_PyType_LookupRef` | lookup |
| 3.22% | `python` | `_PyObject_Malloc` | memory |
| 2.78% | `python` | `_PyObject_Free` | memory |
| 2.66% | `python` | `_Py_dict_lookup` | lookup |
| 2.06% | `python` | `gc_collect_region.isra.0` | gc |
| 1.92% | `python` | `tupledealloc` | memory |
| 1.56% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.49% | `python` | `initialize_locals` | interpreter |
| 1.41% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.27% | `python` | `PyObject_RichCompareBool` | dynamic |
| 1.12% | `python` | `visit_decref` | gc |
| 1.03% | `python` | `PyType_IsSubtype` | dynamic |
| 0.79% | `python` | `_PyObject_GenericGetAttrWithDict` | dynamic |
| 0.79% | `python` | `visit_reachable` | gc |
| 0.78% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.75% | `python` | `PyDict_GetItemRef` | dict |
| 0.72% | `python` | `PyObject_GetAttr` | dynamic |
| 0.71% | `python` | `dict_dealloc` | memory |
| 0.67% | `python` | `_PyTuple_FromArray.part.0` | tuple |
| 0.64% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.63% | `python` | `insertdict` | dict |
| 0.62% | `python` | `_Py_Dealloc` | memory |
| 0.61% | `python` | `PyObject_GC_Del` | gc |
| 0.60% | `python` | `_PyObject_GC_New` | gc |
| 0.53% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.52% | `python` | `r_object` | import |
| 0.52% | `python` | `_PyTuple_FromStackRefSteal` | tuple |
| 0.51% | `python` | `_Py_type_getattro` | lookup |
| 0.47% | `python` | `find_name_in_mro` | lookup |
| 0.47% | `python` | `PyObject_GenericGetAttr` | dynamic |
| 0.42% | `python` | `setiter_iternext` | miscobj |
| 0.41% | `python` | `_PyCode_Quicken` | interpreter |
| 0.40% | `python` | `_PyObject_LookupSpecial` | dynamic |
| 0.38% | `python` | `PyUnicode_RichCompare` | str |
| 0.37% | `python` | `list_dealloc` | memory |
| 0.36% | `python` | `dictiter_iternextitem` | dict |
| 0.36% | `python` | `_Py_NewReference` | memory |
| 0.35% | `python` | `PyObject_CallOneArg` | dynamic |
| 0.35% | `python` | `insert_to_emptydict` | dict |
| 0.34% | `python` | `PyTuple_New` | memory |
| 0.33% | `python` | `_PyObject_GetMethod` | dynamic |
| 0.33% | `python` | `dict_traverse` | gc |
| 0.32% | `python` | `_PyObject_GC_Link` | gc |
| 0.31% | `python` | `siphash13` | str |
| 0.31% | `python` | `PyObject_GetOptionalAttr` | dynamic |
| 0.29% | `python` | `slot_tp_richcompare` | dynamic |
| 0.28% | `python` | `_PyObject_MakeTpCall` | dynamic |
| 0.28% | `python` | `PyDict_SetItem` | dict |
| 0.27% | `python` | `_PyEval_Vector` | interpreter |
| 0.26% | `libc-2.31.so` | `pthread_attr_setschedparam` | libc |
| 0.26% | `python` | `PyList_New` | memory |
| 0.25% | `python` | `PyCMethod_New` | memory |

## telco

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 13.74% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 6.87% | `python` | `_PyObject_Malloc` | memory |
| 5.96% | `python` | `_PyObject_Free` | memory |
| 2.25% | `python` | `PyType_GetModuleByDef` | dynamic |
| 2.21% | `python` | `PyObject_GC_Del` | gc |
| 2.02% | `_decimal.cpython-314-x86_64-linux-gnu.so` | `nm_mpd_qadd` | library |
| 1.99% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.87% | `python` | `PyContextVar_Get` | unknown |
| 1.71% | `python` | `_PyObject_GC_New` | gc |
| 1.70% | `_decimal.cpython-314-x86_64-linux-gnu.so` | `mpd_setdigits` | library |
| 1.56% | `python` | `tupledealloc` | memory |
| 1.54% | `_decimal.cpython-314-x86_64-linux-gnu.so` | `_mpd_qaddsub` | library |
| 1.50% | `_decimal.cpython-314-x86_64-linux-gnu.so` | `_mpd_check_exp` | library |
| 1.48% | `python` | `vgetargskeywords.constprop.0` | calls |
| 1.39% | `_decimal.cpython-314-x86_64-linux-gnu.so` | `nm_mpd_qmul` | library |
| 1.37% | `_decimal.cpython-314-x86_64-linux-gnu.so` | `_mpd_qmul` | library |
| 1.31% | `python` | `_PyArg_UnpackKeywordsWithVararg` | calls |
| 1.26% | `python` | `_PyType_LookupRef` | lookup |
| 1.18% | `python` | `convertitem.constprop.0` | library |
| 1.17% | `_decimal.cpython-314-x86_64-linux-gnu.so` | `_mpd_baseshiftr` | library |
| 1.09% | `python` | `PyObject_GC_UnTrack` | gc |
| 1.00% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.97% | `python` | `PyObject_GenericGetAttr` | dynamic |
| 0.94% | `_decimal.cpython-314-x86_64-linux-gnu.so` | `mpd_qquantize` | library |
| 0.87% | `_decimal.cpython-314-x86_64-linux-gnu.so` | `dec_addstatus` | library |
| 0.87% | `_decimal.cpython-314-x86_64-linux-gnu.so` | `dec_mpd_qquantize` | library |
| 0.83% | `python` | `_PyTuple_FromArray.part.0` | tuple |
| 0.81% | `_decimal.cpython-314-x86_64-linux-gnu.so` | `PyDecType_New` | library |
| 0.80% | `python` | `PyUnicode_AsUCS4` | str |
| 0.80% | `python` | `_PyObject_GC_Link` | gc |
| 0.74% | `python` | `vgetargs1_impl` | calls |
| 0.73% | `python` | `PyCMethod_New` | memory |
| 0.72% | `_decimal.cpython-314-x86_64-linux-gnu.so` | `dec_dealloc` | library |
| 0.70% | `python` | `gc_collect_region.isra.0` | gc |
| 0.68% | `_decimal.cpython-314-x86_64-linux-gnu.so` | `mpd_qshiftr` | library |
| 0.62% | `python` | `_Py_NewReference` | memory |
| 0.60% | `python` | `PyTuple_New` | memory |
| 0.57% | `_decimal.cpython-314-x86_64-linux-gnu.so` | `dec_str` | library |
| 0.57% | `python` | `PyNumber_Multiply` | dynamic |
| 0.56% | `_decimal.cpython-314-x86_64-linux-gnu.so` | `mpd_qfinalize.part.0` | library |
| 0.55% | `python` | `_Py_Dealloc` | memory |
| 0.55% | `python` | `_Py_dict_lookup` | lookup |
| 0.52% | `python` | `PyNumber_InPlaceAdd` | dynamic |
| 0.52% | `_decimal.cpython-314-x86_64-linux-gnu.so` | `_mpd_baseadd` | library |
| 0.51% | `python` | `PyDict_GetItemRef` | dict |
| 0.49% | `python` | `write_str` | unknown |
| 0.47% | `python` | `PyType_IsSubtype` | dynamic |
| 0.46% | `_decimal.cpython-314-x86_64-linux-gnu.so` | `ctx_mpd_qquantize` | library |
| 0.44% | `python` | `meth_dealloc` | memory |
| 0.41% | `python` | `_io_BytesIO_read` | unknown |
| 0.40% | `_decimal.cpython-314-x86_64-linux-gnu.so` | `_mpd_to_string` | library |
| 0.40% | `python` | `PyObject_RichCompare` | dynamic |
| 0.40% | `python` | `PyObject_Malloc` | dynamic |
| 0.40% | `python` | `binary_op1` | unknown |
| 0.39% | `python` | `method_vectorcall_VARARGS_KEYWORDS` | calls |
| 0.38% | `_decimal.cpython-314-x86_64-linux-gnu.so` | `mpd_del` | library |
| 0.37% | `_decimal.cpython-314-x86_64-linux-gnu.so` | `0x0000000000007bc4` | library |
| 0.36% | `_decimal.cpython-314-x86_64-linux-gnu.so` | `mpd_qmul` | library |
| 0.36% | `_decimal.cpython-314-x86_64-linux-gnu.so` | `current_context` | library |
| 0.35% | `python` | `builtin_print` | unknown |
| 0.35% | `python` | `_PyType_GetModuleByDef2` | unknown |
| 0.34% | `python` | `PyFile_WriteObject` | unknown |
| 0.34% | `python` | `PyNumber_Add` | dynamic |
| 0.34% | `python` | `PyObject_Vectorcall` | dynamic |
| 0.34% | `python` | `PyErr_CheckSignals` | exceptions |
| 0.34% | `python` | `PyObject_GetAttr` | dynamic |
| 0.33% | `python` | `PyObject_CallOneArg` | dynamic |
| 0.32% | `python` | `visit_decref` | gc |
| 0.31% | `_decimal.cpython-314-x86_64-linux-gnu.so` | `PyDecType_FromLongExact` | library |
| 0.31% | `python` | `PyObject_Str` | dynamic |
| 0.29% | `python` | `cfunction_vectorcall_O` | calls |
| 0.29% | `python` | `_PyObject_MakeTpCall` | dynamic |
| 0.28% | `python` | `r_object` | import |
| 0.26% | `python` | `PyUnicode_CompareWithASCIIString` | str |

## thrift

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 20.21% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 3.92% | `python` | `_PyObject_Malloc` | memory |
| 3.67% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 3.65% | `python` | `_PyObject_Free` | memory |
| 2.71% | `python` | `_PyType_LookupRef` | lookup |
| 2.16% | `python` | `initialize_locals` | interpreter |
| 2.15% | `python` | `_Py_dict_lookup` | lookup |
| 2.01% | `fastbinary.cpython-314-x86_64-linux-gnu.so` | `apache::thrift::py::ProtocolBase<apache::thrift::py::BinaryProtocol>::encodeValue` | library |
| 1.92% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.55% | `python` | `insert_to_emptydict` | dict |
| 1.46% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.41% | `python` | `insertdict` | dict |
| 1.36% | `python` | `dict_dealloc` | memory |
| 1.18% | `python` | `PyType_GenericAlloc` | memory |
| 1.10% | `python` | `subtype_dealloc` | memory |
| 1.09% | `python` | `PyDict_GetItemRef` | dict |
| 0.97% | `python` | `tupledealloc` | memory |
| 0.94% | `python` | `PyObject_RichCompareBool` | dynamic |
| 0.94% | `python` | `gc_collect_region.isra.0` | gc |
| 0.91% | `python` | `_Py_Dealloc` | memory |
| 0.81% | `fastbinary.cpython-314-x86_64-linux-gnu.so` | `apache::thrift::py::ProtocolBase<apache::thrift::py::BinaryProtocol>::decodeValue` | library |
| 0.76% | `python` | `_PyObject_GenericGetAttrWithDict` | dynamic |
| 0.73% | `python` | `_PyObject_Call_Prepend` | dynamic |
| 0.70% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.69% | `python` | `PyDict_SetItem` | dict |
| 0.67% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.66% | `python` | `_PyStack_UnpackDict` | unknown |
| 0.61% | `python` | `PyObject_GenericGetAttr` | dynamic |
| 0.59% | `python` | `PyObject_IS_GC` | gc |
| 0.58% | `python` | `_PyObject_MakeTpCall` | dynamic |
| 0.58% | `python` | `PyTuple_Size` | tuple |
| 0.57% | `fastbinary.cpython-314-x86_64-linux-gnu.so` | `apache::thrift::py::ProtocolBase<apache::thrift::py::BinaryProtocol>::readBytes` | library |
| 0.56% | `fastbinary.cpython-314-x86_64-linux-gnu.so` | `apache::thrift::py::ProtocolBase<apache::thrift::py::BinaryProtocol>::readStruct` | library |
| 0.55% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.54% | `python` | `PyObject_GC_Del` | gc |
| 0.53% | `python` | `PyDict_Next` | dict |
| 0.53% | `python` | `PyLong_AsLong` | int |
| 0.51% | `python` | `PyObject_ClearManagedDict` | dynamic |
| 0.47% | `python` | `PyObject_GetAttr` | dynamic |
| 0.46% | `python` | `type_call` | dynamic |
| 0.46% | `fastbinary.cpython-314-x86_64-linux-gnu.so` | `apache::thrift::py::BinaryProtocol::readFieldBegin` | library |
| 0.45% | `python` | `dict_merge` | dict |
| 0.44% | `python` | `PyObject_Call` | dynamic |
| 0.44% | `python` | `unicode_from_format` | str |
| 0.41% | `python` | `_PyEval_Vector` | interpreter |
| 0.40% | `python` | `PyUnicode_RichCompare` | str |
| 0.39% | `libc-2.31.so` | `pthread_attr_setschedparam` | libc |
| 0.39% | `python` | `_PyDict_FromItems` | dict |
| 0.39% | `python` | `r_object` | import |
| 0.39% | `python` | `slot_tp_init` | unknown |
| 0.38% | `python` | `siphash13` | str |
| 0.38% | `python` | `PyTuple_New` | memory |
| 0.37% | `python` | `ascii_decode` | str |
| 0.37% | `python` | `visit_decref` | gc |
| 0.35% | `python` | `vgetargs1_impl` | calls |
| 0.35% | `python` | `_PyFunction_Vectorcall` | calls |
| 0.34% | `python` | `_PyTuple_FromArray.part.0` | tuple |
| 0.34% | `python` | `_PyObject_Realloc` | memory |
| 0.33% | `python` | `find_empty_slot` | dict |
| 0.33% | `python` | `PyDict_New` | memory |
| 0.33% | `python` | `_Py_NewReference` | memory |
| 0.33% | `python` | `_PyObject_Calloc` | memory |
| 0.32% | `python` | `_PyObject_GC_Link` | gc |
| 0.32% | `python` | `visit_reachable` | gc |
| 0.30% | `python` | `_PyUnicodeWriter_WriteASCIIString` | str |
| 0.30% | `python` | `_PyObject_TryGetInstanceAttribute` | dynamic |
| 0.30% | `fastbinary.cpython-314-x86_64-linux-gnu.so` | `apache::thrift::py::parse_struct_item_spec` | library |
| 0.30% | `python` | `convertitem.constprop.0` | library |
| 0.29% | `python` | `_Py_type_getattro` | lookup |
| 0.29% | `python` | `list_dealloc` | memory |
| 0.28% | `python` | `PyList_New` | memory |
| 0.28% | `libc-2.31.so` | `malloc` | libc |
| 0.28% | `python` | `resize_compact` | str |
| 0.27% | `python` | `object_new` | memory |
| 0.27% | `python` | `PyObject_ClearWeakRefs` | dynamic |
| 0.26% | `python` | `PyUnicode_New.part.0` | memory |
| 0.26% | `python` | `_PyThreadState_PopFrame` | interpreter |

## tomli_loads

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 48.73% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 4.62% | `python` | `set_lookkey` | miscobj |
| 4.02% | `python` | `_PyObject_Free` | memory |
| 3.38% | `python` | `_PyObject_Malloc` | memory |
| 3.05% | `python` | `_PyLong_Add` | int |
| 2.59% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 2.55% | `python` | `_PyUnicode_Equal` | str |
| 2.03% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.77% | `python` | `_Py_dict_lookup` | lookup |
| 1.72% | `python` | `_PySet_Contains` | miscobj |
| 1.41% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.15% | `python` | `PyDict_GetItemRef` | dict |
| 0.83% | `python` | `_PyTuple_FromStackRefSteal` | tuple |
| 0.80% | `python` | `_PyIncrementalNewlineDecoder_decode` | memory |
| 0.80% | `python` | `tupledealloc` | memory |
| 0.75% | `python` | `long_dealloc` | memory |
| 0.73% | `python` | `replace` | str |
| 0.65% | `python` | `_PyUnicode_FromUCS4.part.0` | str |
| 0.62% | `python` | `PyNumber_AsSsize_t` | dynamic |
| 0.58% | `python` | `_Py_NewReference` | memory |
| 0.49% | `python` | `sre_ucs4_match` | library |
| 0.48% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.46% | `python` | `_PyType_LookupRef` | lookup |
| 0.38% | `python` | `tuplesubscript` | tuple |
| 0.38% | `python` | `_PyBuildSlice_ConsumeRefs` | miscobj |
| 0.36% | `python` | `siphash13` | str |
| 0.35% | `python` | `unicode_decode_utf8_impl` | str |
| 0.32% | `python` | `PyObject_GetAttr` | dynamic |
| 0.31% | `python` | `PyType_IsSubtype` | dynamic |
| 0.31% | `python` | `initialize_locals` | interpreter |
| 0.30% | `python` | `_PyObject_GenericGetAttrWithDict` | dynamic |
| 0.29% | `python` | `PySlice_AdjustIndices` | miscobj |
| 0.27% | `python` | `memcmp@plt` | unknown |
| 0.26% | `python` | `PyDict_Contains` | dict |
| 0.26% | `python` | `PyObject_GenericGetAttr` | dynamic |
| 0.25% | `python` | `PyObject_Malloc` | dynamic |

## tornado_http

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 27.23% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 3.68% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 2.77% | `python` | `_PyObject_Malloc` | memory |
| 2.43% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 2.08% | `python` | `_PyObject_Free` | memory |
| 1.89% | `python` | `gc_collect_region.isra.0` | gc |
| 1.58% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.49% | `python` | `_Py_dict_lookup` | lookup |
| 1.46% | `python` | `_PyType_LookupRef` | lookup |
| 0.98% | `python` | `tupledealloc` | memory |
| 0.97% | `python` | `visit_decref` | gc |
| 0.88% | `python` | `initialize_locals` | interpreter |
| 0.78% | `libc-2.31.so` | `pthread_attr_setschedparam` | libc |
| 0.73% | `[kernel.kallsyms]` | `copy_user_enhanced_fast_string` | kernel |
| 0.69% | `python` | `visit_reachable` | gc |
| 0.63% | `python` | `r_object` | import |
| 0.57% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.53% | `python` | `find_name_in_mro` | lookup |
| 0.52% | `python` | `_Py_Dealloc` | memory |
| 0.49% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.48% | `[kernel.kallsyms]` | `clear_page_erms` | kernel |
| 0.45% | `python` | `sre_ucs1_match` | library |
| 0.45% | `python` | `update_one_slot` | lookup |
| 0.44% | `python` | `PyDict_GetItemRef` | dict |
| 0.43% | `python` | `PyObject_GC_Del` | gc |
| 0.40% | `python` | `dict_dealloc` | memory |
| 0.40% | `python` | `_PyCode_Quicken` | interpreter |
| 0.40% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.38% | `python` | `siphash13` | str |
| 0.37% | `python` | `PyObject_GenericGetAttr` | dynamic |
| 0.37% | `python` | `_PyTuple_FromArray.part.0` | tuple |
| 0.35% | `python` | `_Py_hashtable_get_entry_generic` | lookup |
| 0.35% | `python` | `PyObject_Vectorcall` | dynamic |
| 0.32% | `python` | `_PyTuple_FromStackRefSteal` | tuple |
| 0.32% | `python` | `list_dealloc` | memory |
| 0.31% | `python` | `PyObject_GetAttr` | dynamic |
| 0.30% | `python` | `PyType_GenericAlloc` | memory |
| 0.30% | `python` | `_PyObject_GC_New` | gc |
| 0.28% | `python` | `_PyDict_GetItemRef_KnownHash` | dict |
| 0.28% | `python` | `_PyUnicode_FromUCS1.part.0` | str |
| 0.28% | `python` | `PyType_IsSubtype` | dynamic |
| 0.27% | `python` | `dict_traverse` | gc |
| 0.27% | `python` | `code_dealloc` | memory |
| 0.27% | `python` | `subtype_dealloc` | memory |
| 0.26% | `python` | `insertdict` | dict |
| 0.26% | `python` | `type_ready` | dynamic |

## typing_runtime_protocols

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 28.52% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 4.45% | `python` | `_PyObject_Malloc` | memory |
| 3.76% | `python` | `_PyObject_Free` | memory |
| 3.43% | `python` | `_PyTuple_FromArray.part.0` | tuple |
| 3.06% | `python` | `tupledealloc` | memory |
| 2.78% | `python` | `weakref___new__` | memory |
| 2.64% | `python` | `_Py_dict_lookup` | lookup |
| 2.29% | `python` | `_PyObject_MakeTpCall` | dynamic |
| 2.27% | `python` | `_PyType_LookupRef` | lookup |
| 1.96% | `python` | `PyArg_UnpackTuple` | calls |
| 1.86% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 1.50% | `python` | `PyObject_RichCompareBool` | dynamic |
| 1.20% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.06% | `python` | `PyObject_GC_UnTrack` | gc |
| 1.01% | `python` | `_Py_type_getattro` | lookup |
| 0.98% | `python` | `bounded_lru_cache_wrapper` | unknown |
| 0.95% | `python` | `_PyObject_GC_New` | gc |
| 0.81% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 0.81% | `python` | `PyObject_Vectorcall` | dynamic |
| 0.80% | `python` | `type_call` | dynamic |
| 0.78% | `python` | `PyObject_GC_Del` | gc |
| 0.73% | `python` | `_Py_Dealloc` | memory |
| 0.70% | `python` | `_PyDict_GetItem_KnownHash` | dict |
| 0.66% | `python` | `gc_collect_region.isra.0` | gc |
| 0.62% | `python` | `set_lookkey` | miscobj |
| 0.62% | `python` | `_Py_NewReference` | memory |
| 0.62% | `python` | `initialize_locals` | interpreter |
| 0.60% | `python` | `getset_get` | dynamic |
| 0.57% | `python` | `PyObject_GetAttr` | dynamic |
| 0.52% | `python` | `list_dealloc` | memory |
| 0.50% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.50% | `python` | `weakref___init__` | unknown |
| 0.49% | `python` | `tuplehash` | tuple |
| 0.49% | `python` | `PyList_New` | memory |
| 0.49% | `python` | `wrap_descr_get` | unknown |
| 0.47% | `python` | `frame_dealloc` | memory |
| 0.46% | `python` | `tuplerichcompare` | tuple |
| 0.46% | `python` | `PyTraceBack_Here` | exceptions |
| 0.45% | `python` | `PyObject_Call` | dynamic |
| 0.44% | `python` | `PyObject_Hash` | dynamic |
| 0.40% | `python` | `_Py_CheckFunctionResult` | calls |
| 0.40% | `python` | `weakref_richcompare` | unknown |
| 0.39% | `python` | `_PyObject_GC_Link` | gc |
| 0.39% | `python` | `_PyList_AppendTakeRefListResize` | list |
| 0.39% | `python` | `_PyObject_LookupSpecial` | dynamic |
| 0.37% | `python` | `PyObject_GenericGetAttr` | dynamic |
| 0.36% | `python` | `visit_decref` | gc |
| 0.35% | `python` | `tuple_iter` | tuple |
| 0.35% | `python` | `PyType_IsSubtype` | dynamic |
| 0.32% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.32% | `python` | `_PyStaticType_GetState` | unknown |
| 0.31% | `python` | `_PyTuple_FromArray` | tuple |
| 0.30% | `python` | `r_object` | import |
| 0.30% | `python` | `lru_cache_make_key` | unknown |
| 0.28% | `python` | `visit_reachable` | gc |
| 0.28% | `python` | `_PyObject_Realloc` | memory |
| 0.28% | `python` | `find_name_in_mro` | lookup |
| 0.28% | `python` | `_abc__abc_instancecheck` | unknown |
| 0.27% | `python` | `AttributeError_init` | exceptions |
| 0.26% | `python` | `_PyThreadState_PopFrame` | interpreter |
| 0.26% | `python` | `PyObject_GetIter` | dynamic |
| 0.26% | `python` | `PySequence_Tuple` | dynamic |
| 0.25% | `python` | `dict_dealloc` | memory |

## unpickle_pure_python

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 50.55% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 3.27% | `python` | `_Py_dict_lookup` | lookup |
| 2.56% | `python` | `_PyObject_Malloc` | memory |
| 2.40% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 2.02% | `python` | `PyObject_IsTrue` | dynamic |
| 2.00% | `python` | `_PyObject_Free` | memory |
| 1.66% | `python` | `PyDict_GetItemRef` | dict |
| 1.58% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.50% | `python` | `PyNumber_AsSsize_t` | dynamic |
| 1.19% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 1.03% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.02% | `python` | `_io_BytesIO_read` | unknown |
| 0.98% | `python` | `insertdict` | dict |
| 0.90% | `python` | `bytes_subscript` | str |
| 0.89% | `python` | `PyObject_GetItem` | dynamic |
| 0.87% | `python` | `initialize_locals` | interpreter |
| 0.73% | `python` | `PyLong_AsSsize_t` | int |
| 0.69% | `python` | `PyUnicode_Decode.part.0` | str |
| 0.66% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.61% | `python` | `PyLong_FromSsize_t` | int |
| 0.60% | `python` | `siphash13` | str |
| 0.58% | `python` | `gc_collect_region.isra.0` | gc |
| 0.57% | `python` | `PyObject_IsInstance` | dynamic |
| 0.55% | `python` | `_PyThreadState_PopFrame` | interpreter |
| 0.55% | `python` | `PyBytes_FromStringAndSize` | str |
| 0.54% | `python` | `ascii_decode` | str |
| 0.49% | `python` | `_Py_convert_optional_to_ssize_t` | unknown |
| 0.44% | `python` | `list_subscript` | list |
| 0.41% | `python` | `PyObject_Size` | dynamic |
| 0.41% | `python` | `unicode_decode_utf8` | str |
| 0.39% | `python` | `visit_decref` | gc |
| 0.38% | `python` | `unicode_vectorcall` | str |
| 0.37% | `python` | `dict_dealloc` | memory |
| 0.36% | `python` | `PyObject_Hash` | dynamic |
| 0.33% | `python` | `r_object` | import |
| 0.32% | `libc-2.31.so` | `pthread_attr_setschedparam` | libc |
| 0.32% | `python` | `_PyType_LookupRef` | lookup |
| 0.32% | `python` | `long_hash` | int |
| 0.31% | `python` | `list_append` | list |
| 0.31% | `python` | `PyUnicode_FromEncodedObject` | str |
| 0.28% | `python` | `_PyObject_Realloc` | memory |
| 0.28% | `python` | `PyUnicode_AsUTF8AndSize` | str |
| 0.27% | `python` | `bytes_length` | str |
| 0.26% | `python` | `tupledealloc` | memory |

## xml_etree

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 20.10% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 4.46% | `python` | `_PyObject_Malloc` | memory |
| 3.54% | `python` | `_PyObject_Free` | memory |
| 2.65% | `python` | `_PyType_LookupRef` | lookup |
| 2.54% | `pyexpat.cpython-314-x86_64-linux-gnu.so` | `normal_updatePosition` | library |
| 2.42% | `python` | `gc_collect_region.isra.0` | gc |
| 2.21% | `pyexpat.cpython-314-x86_64-linux-gnu.so` | `normal_contentTok` | library |
| 1.76% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.74% | `python` | `_Py_dict_lookup` | lookup |
| 1.67% | `python` | `_io_TextIOWrapper_write` | unknown |
| 1.48% | `python` | `PyObject_GenericGetAttr` | dynamic |
| 1.36% | `python` | `visit_reachable` | gc |
| 1.35% | `python` | `visit_decref` | gc |
| 1.32% | `pyexpat.cpython-314-x86_64-linux-gnu.so` | `sip24_update` | library |
| 1.28% | `pyexpat.cpython-314-x86_64-linux-gnu.so` | `accountingDiffTolerated.part.0` | library |
| 1.14% | `pyexpat.cpython-314-x86_64-linux-gnu.so` | `normal_nameLength` | library |
| 1.06% | `pyexpat.cpython-314-x86_64-linux-gnu.so` | `doContent` | library |
| 1.03% | `_elementtree.cpython-314-x86_64-linux-gnu.so` | `expat_end_handler` | library |
| 0.99% | `pyexpat.cpython-314-x86_64-linux-gnu.so` | `lookup.constprop.0` | library |
| 0.95% | `python` | `initialize_locals` | interpreter |
| 0.93% | `_elementtree.cpython-314-x86_64-linux-gnu.so` | `treebuilder_handle_start` | library |
| 0.87% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.83% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 0.81% | `python` | `PyUnicode_Contains` | str |
| 0.80% | `python` | `ascii_decode` | str |
| 0.77% | `python` | `PyObject_GetAttr` | dynamic |
| 0.74% | `pyexpat.cpython-314-x86_64-linux-gnu.so` | `normal_getAtts` | library |
| 0.71% | `python` | `tupledealloc` | memory |
| 0.69% | `python` | `siphash13` | str |
| 0.67% | `_elementtree.cpython-314-x86_64-linux-gnu.so` | `elementiter_next` | library |
| 0.67% | `python` | `_Py_Dealloc` | memory |
| 0.66% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.63% | `_elementtree.cpython-314-x86_64-linux-gnu.so` | `element_gc_traverse` | library |
| 0.62% | `pyexpat.cpython-314-x86_64-linux-gnu.so` | `sip24_final` | library |
| 0.61% | `python` | `_copy_characters.part.0.constprop.0` | str |
| 0.58% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.55% | `python` | `getset_get` | dynamic |
| 0.52% | `_elementtree.cpython-314-x86_64-linux-gnu.so` | `expat_data_handler` | library |
| 0.52% | `pyexpat.cpython-314-x86_64-linux-gnu.so` | `storeAtts` | library |
| 0.51% | `python` | `list_dealloc` | memory |
| 0.51% | `python` | `PyUnicode_New.part.0` | memory |
| 0.48% | `python` | `_PyObject_GenericGetAttrWithDict` | dynamic |
| 0.46% | `python` | `_PyObject_GC_New` | gc |
| 0.45% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.45% | `python` | `_PyObject_GetMethod` | dynamic |
| 0.43% | `python` | `_Py_NewReference` | memory |
| 0.43% | `python` | `PyObject_VectorcallMethod` | dynamic |
| 0.41% | `python` | `vgetargs1_impl` | calls |
| 0.40% | `python` | `PyObject_GC_Del` | gc |
| 0.39% | `python` | `visit_add_to_container` | gc |
| 0.39% | `python` | `unicode_dealloc` | memory |
| 0.39% | `libc-2.31.so` | `pthread_attr_setschedparam` | libc |
| 0.39% | `python` | `PyType_GenericAlloc` | memory |
| 0.37% | `python` | `PyType_IsSubtype` | dynamic |
| 0.36% | `_elementtree.cpython-314-x86_64-linux-gnu.so` | `element_gc_clear` | library |
| 0.36% | `_elementtree.cpython-314-x86_64-linux-gnu.so` | `expat_start_handler` | library |
| 0.35% | `python` | `PyUnicode_Concat` | str |
| 0.34% | `python` | `_PyType_GetDict` | dynamic |
| 0.33% | `python` | `PyUnicode_Format` | str |
| 0.33% | `python` | `_PyEval_Vector` | interpreter |
| 0.33% | `python` | `long_to_decimal_string_internal` | int |
| 0.32% | `python` | `_PyObject_GC_Link` | gc |
| 0.31% | `python` | `PyObject_RichCompareBool` | dynamic |
| 0.30% | `python` | `tupletraverse` | tuple |
| 0.30% | `_elementtree.cpython-314-x86_64-linux-gnu.so` | `makeuniversal.isra.0` | library |
| 0.29% | `python` | `_PyTuple_FromStackRefSteal` | tuple |
| 0.29% | `_elementtree.cpython-314-x86_64-linux-gnu.so` | `element_getitem` | library |
| 0.29% | `python` | `dict_dealloc` | memory |
| 0.29% | `python` | `_PyObject_Realloc` | memory |
| 0.28% | `python` | `stringlib__two_way` | str |
| 0.28% | `python` | `object_isinstance` | dynamic |
| 0.27% | `python` | `_PyTuple_FromArray.part.0` | tuple |
| 0.27% | `python` | `PyList_Append` | list |
| 0.26% | `python` | `PyDescr_IsData` | dynamic |
| 0.26% | `python` | `PyUnicode_DecodeUTF8` | str |


## Categories

### interpreter

33.47% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 28.93% | python | _PyEval_EvalFrameDefault |
| 1.36% | python | _PyFrame_ClearExceptCode |
| 0.71% | python | initialize_locals |
| 0.59% | python | _PyEval_FrameClearAndPop |
| 0.38% | python | _PyEvalFramePushAndInit |
| 0.28% | python | _PyThreadState_PopFrame |
| 0.20% | python | _PyCode_Quicken |
| 0.17% | python | _PyEval_Vector |
| 0.12% | python | _PyThreadState_PushFrame |
| 0.09% | python | _PyEval_SliceIndex |
| 0.09% | python | call_instrumentation_vector.part.0 |
| 0.08% | python | _PyFrame_Traverse |
| 0.08% | python | _Py_GetBaseOpcode |
| 0.07% | python | _PyPegen_is_memoized |
| 0.06% | python | _PyCode_New |
| 0.05% | python | _Py_call_instrumentation_line |
| 0.03% | python | _PyPegen_expect_token |
| 0.03% | python | _PyPegen_update_memo |
| 0.02% | python | _PyCode_Validate |
| 0.01% | python | _PyPegen_fill_token |
| 0.01% | python | _PyEval_BuiltinsFromGlobals |
| 0.01% | python | _PyCode_GetCode |
| 0.01% | python | _PyPegen_insert_memo |
| 0.01% | python | _PyFrame_New_NoTrack |
| 0.01% | python | _PyPegen_name_token |
| 0.01% | python | _PyThreadState_Attach |
| 0.01% | python | PyEval_GetFrame |
| 0.01% | python | _PyThreadState_MustExit |
| 0.01% | python | PyEval_EvalCode |
| 0.00% | python | _PyPegen_new_identifier |
| 0.00% | python | _PyThreadState_Detach |
| 0.00% | python | _PyEval_ImportName |
| 0.00% | python | _PyCode_ConstantKey |

### memory

12.69% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 3.37% | python | _PyObject_Malloc |
| 3.09% | python | _PyObject_Free |
| 0.72% | python | tupledealloc |
| 0.47% | python | _Py_Dealloc |
| 0.46% | python | list_dealloc |
| 0.40% | python | _Py_NewReference |
| 0.33% | python | dict_dealloc |
| 0.25% | python | subtype_dealloc |
| 0.24% | python | PyType_GenericAlloc |
| 0.20% | python | PyList_New |
| 0.20% | python | gen_dealloc |
| 0.20% | python | _PyObject_Realloc |
| 0.20% | python | PyUnicode_New.part.0 |
| 0.15% | python | float_dealloc |
| 0.14% | python | unicode_dealloc |
| 0.13% | python | long_dealloc |
| 0.12% | python | PyTuple_New |
| 0.12% | python | slice_dealloc |
| 0.09% | python | PyFunction_NewWithQualName |
| 0.09% | python | code_dealloc |
| 0.09% | python | _PyObject_Calloc |
| 0.08% | python | PyCMethod_New |
| 0.08% | python | set_dealloc |
| 0.07% | python | func_dealloc |
| 0.07% | python | PyObject_CallFinalizerFromDealloc |
| 0.06% | python | meth_dealloc |
| 0.06% | python | memset@plt |
| 0.06% | python | allocate_from_new_pool |
| 0.05% | python | context_tp_dealloc |
| 0.05% | python | _PyType_NewManagedObject |
| 0.05% | python | PyDict_New |
| 0.05% | python | listiter_dealloc |
| 0.05% | python | pattern_new_match.isra.0.part.0 |
| 0.04% | python | memcpy@plt |
| 0.04% | python | weakref___new__ |
| 0.04% | python | method_dealloc |
| 0.04% | python | PyMethod_New |
| 0.04% | python | PyMem_Calloc |
| 0.03% | python | frame_dealloc |
| 0.03% | python | PyMem_Free |
| 0.03% | python | PySlice_New |
| 0.03% | python | PyMem_Malloc |
| 0.03% | python | object_new |
| 0.03% | python | _PyFloat_ExactDealloc |
| 0.03% | python | _PyAsyncGenValueWrapperNew |
| 0.02% | python | async_gen_wrapped_val_dealloc |
| 0.02% | python | StopIteration_dealloc |
| 0.02% | python | type_new |
| 0.02% | python | object_dealloc |
| 0.02% | python | async_gen_asend_dealloc |
| 0.02% | python | _PyObject_New |
| 0.02% | python | cell_dealloc |
| 0.01% | python | tupleiter_dealloc |
| 0.01% | python | range_dealloc |
| 0.01% | python | structseq_dealloc |
| 0.01% | python | BaseException_new |
| 0.01% | python | tp_new_wrapper |
| 0.01% | python | PyMem_Realloc |
| 0.01% | python | dictiter_dealloc |
| 0.01% | python | _PyIncrementalNewlineDecoder_decode |
| 0.01% | python | tb_dealloc |
| 0.01% | python | BaseException_dealloc |
| 0.01% | python | zip_new |
| 0.01% | python | dictview_dealloc |
| 0.01% | python | PyCell_New |
| 0.01% | python | PyWeakref_NewRef |
| 0.01% | python | _PyMem_RawMalloc |
| 0.01% | python | match_dealloc |
| 0.01% | python | _PyTokenizer_translate_newlines |
| 0.01% | python | type_dealloc |
| 0.01% | python | reversed_new_impl |
| 0.01% | python | setiter_dealloc |
| 0.01% | python | PyUnicode_New |
| 0.00% | python | _PyUnicode_ExactDealloc |
| 0.00% | python | slot_tp_new |
| 0.00% | python | descr_dealloc |
| 0.00% | python | _PyMem_RawFree |
| 0.00% | python | _Py_NewReferenceNoTotal |
| 0.00% | python | unicode_new |
| 0.00% | python | PyDictProxy_New |
| 0.00% | python | memory_dealloc |
| 0.00% | python | PyObject_Realloc |
| 0.00% | python | AttributeError_dealloc |
| 0.00% | python | _PyObject_NewVar |
| 0.00% | python | zip_dealloc |

### gc

10.22% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 2.92% | python | gc_collect_region.isra.0 |
| 1.63% | python | visit_decref |
| 1.61% | python | visit_reachable |
| 0.73% | python | visit_add_to_container |
| 0.45% | python | PyObject_GC_UnTrack |
| 0.41% | python | PyObject_GC_Del |
| 0.31% | python | list_traverse |
| 0.29% | python | dict_traverse |
| 0.29% | python | _PyObject_GC_New |
| 0.25% | python | subtype_traverse |
| 0.22% | python | _PyObject_GC_Link |
| 0.17% | python | PyObject_IS_GC |
| 0.17% | python | _PyGC_Collect |
| 0.16% | python | _PyObject_GC_NewVar |
| 0.11% | python | func_traverse |
| 0.09% | python | set_traverse |
| 0.07% | python | type_is_gc |
| 0.05% | python | _PyDict_MaybeUntrack |
| 0.05% | python | _PyTuple_MaybeUntrack |
| 0.05% | python | type_traverse |
| 0.04% | python | gen_traverse |
| 0.03% | python | meth_traverse |
| 0.02% | python | context_tp_traverse |
| 0.02% | python | PyObject_GC_Track |
| 0.02% | python | PyGC_Collect |
| 0.01% | python | descr_traverse |
| 0.01% | python | gc_traverse |
| 0.01% | python | module_traverse |
| 0.01% | python | method_traverse |
| 0.01% | python | cell_traverse |
| 0.00% | python | _PyObject_GC_Resize |
| 0.00% | python | deque_traverse |

### library

7.22% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 1.93% | python | sre_ucs1_match |
| 0.90% | libz.so.1.2.11 | crc32_combine64 |
| 0.72% | python | sre_ucs2_charset.isra.0 |
| 0.35% | _json.cpython-314-x86_64-linux-gnu.so | scanstring_unicode |
| 0.30% | libz.so.1.2.11 | inflateBackEnd |
| 0.28% | python | sre_search |
| 0.18% | _json.cpython-314-x86_64-linux-gnu.so | scan_once_unicode |
| 0.14% | python | sre_ucs1_count |
| 0.14% | libm-2.31.so | f64xsubf128 |
| 0.13% | ld-2.31.so | _dl_rtld_di_serinfo |
| 0.09% | _json.cpython-314-x86_64-linux-gnu.so | py_encode_basestring_ascii |
| 0.09% | tracer.cpython-314-x86_64-linux-gnu.so | CTracer_trace |
| 0.08% | python | convertitem.constprop.0 |
| 0.06% | _asyncio.cpython-314-x86_64-linux-gnu.so | TaskObj_traverse |
| 0.05% | array.cpython-314-x86_64-linux-gnu.so | array_subscr |
| 0.05% | libpthread-2.31.so | __pthread_mutex_lock |
| 0.05% | python | pattern_subx |
| 0.05% | libm-2.31.so | __fmod_finite |
| 0.05% | python | _sre_SRE_Pattern_match |
| 0.04% | libpthread-2.31.so | pthread_mutex_unlock |
| 0.04% | ld-2.31.so | _dl_catch_error |
| 0.04% | _json.cpython-314-x86_64-linux-gnu.so | encoder_listencode_obj |
| 0.03% | pyexpat.cpython-314-x86_64-linux-gnu.so | normal_updatePosition |
| 0.03% | math.cpython-314-x86_64-linux-gnu.so | factorial_partial_product |
| 0.03% | pyexpat.cpython-314-x86_64-linux-gnu.so | normal_contentTok |
| 0.03% | _decimal.cpython-314-x86_64-linux-gnu.so | nm_mpd_qadd |
| 0.03% | fastbinary.cpython-314-x86_64-linux-gnu.so | apache::thrift::py::ProtocolBase<apache::thrift::py::BinaryProtocol>::encodeValue |
| 0.03% | _asyncio.cpython-314-x86_64-linux-gnu.so | task_step_impl |
| 0.02% | _json.cpython-314-x86_64-linux-gnu.so | encoder_encode_key_value |
| 0.02% | _decimal.cpython-314-x86_64-linux-gnu.so | mpd_setdigits |
| 0.02% | _asyncio.cpython-314-x86_64-linux-gnu.so | TaskStepMethWrapper_call |
| 0.02% | _decimal.cpython-314-x86_64-linux-gnu.so | _mpd_qaddsub |
| 0.02% | _decimal.cpython-314-x86_64-linux-gnu.so | _mpd_check_exp |
| 0.02% | _bisect.cpython-314-x86_64-linux-gnu.so | _bisect_bisect_right |
| 0.02% | array.cpython-314-x86_64-linux-gnu.so | array_ass_subscr |
| 0.02% | _decimal.cpython-314-x86_64-linux-gnu.so | nm_mpd_qmul |
| 0.02% | _decimal.cpython-314-x86_64-linux-gnu.so | _mpd_qmul |
| 0.02% | pyexpat.cpython-314-x86_64-linux-gnu.so | sip24_update |
| 0.02% | python | _sre_SRE_Pattern_search |
| 0.02% | pyexpat.cpython-314-x86_64-linux-gnu.so | accountingDiffTolerated.part.0 |
| 0.02% | _asyncio.cpython-314-x86_64-linux-gnu.so | TaskObj_clear |
| 0.02% | _heapq.cpython-314-x86_64-linux-gnu.so | siftup |
| 0.02% | _decimal.cpython-314-x86_64-linux-gnu.so | _mpd_baseshiftr |
| 0.02% | pyexpat.cpython-314-x86_64-linux-gnu.so | normal_nameLength |
| 0.01% | pyexpat.cpython-314-x86_64-linux-gnu.so | doContent |
| 0.01% | _elementtree.cpython-314-x86_64-linux-gnu.so | expat_end_handler |
| 0.01% | _asyncio.cpython-314-x86_64-linux-gnu.so | future_init |
| 0.01% | _asyncio.cpython-314-x86_64-linux-gnu.so | _asyncio_Task___init__ |
| 0.01% | pyexpat.cpython-314-x86_64-linux-gnu.so | lookup.constprop.0 |
| 0.01% | _decimal.cpython-314-x86_64-linux-gnu.so | mpd_qquantize |
| 0.01% | _elementtree.cpython-314-x86_64-linux-gnu.so | treebuilder_handle_start |
| 0.01% | libssl.so.1.1 | SSL_rstate_string |
| 0.01% | _asyncio.cpython-314-x86_64-linux-gnu.so | _asyncio_Future_add_done_callback |
| 0.01% | _decimal.cpython-314-x86_64-linux-gnu.so | dec_addstatus |
| 0.01% | _decimal.cpython-314-x86_64-linux-gnu.so | dec_mpd_qquantize |
| 0.01% | _asyncio.cpython-314-x86_64-linux-gnu.so | TaskStepMethWrapper_traverse |
| 0.01% | _asyncio.cpython-314-x86_64-linux-gnu.so | FutureObj_traverse |
| 0.01% | _decimal.cpython-314-x86_64-linux-gnu.so | PyDecType_New |
| 0.01% | fastbinary.cpython-314-x86_64-linux-gnu.so | apache::thrift::py::ProtocolBase<apache::thrift::py::BinaryProtocol>::decodeValue |
| 0.01% | libpthread-2.31.so | __errno_location |
| 0.01% | array.cpython-314-x86_64-linux-gnu.so | d_setitem |
| 0.01% | _asyncio.cpython-314-x86_64-linux-gnu.so | future_schedule_callbacks |
| 0.01% | _elementtree.cpython-314-x86_64-linux-gnu.so | element_gc_traverse |
| 0.01% | pyexpat.cpython-314-x86_64-linux-gnu.so | normal_getAtts |
| 0.01% | libpthread-2.31.so | pthread_cond_signal@@GLIBC_2.3.2 |
| 0.01% | _decimal.cpython-314-x86_64-linux-gnu.so | dec_dealloc |
| 0.01% | _decimal.cpython-314-x86_64-linux-gnu.so | mpd_qshiftr |
| 0.01% | _elementtree.cpython-314-x86_64-linux-gnu.so | elementiter_next |
| 0.01% | pyexpat.cpython-314-x86_64-linux-gnu.so | sip24_final |
| 0.01% | math.cpython-314-x86_64-linux-gnu.so | math_sqrt |
| 0.01% | python | sys_trace_return |
| 0.01% | _asyncio.cpython-314-x86_64-linux-gnu.so | task_wakeup |
| 0.01% | fastbinary.cpython-314-x86_64-linux-gnu.so | apache::thrift::py::ProtocolBase<apache::thrift::py::BinaryProtocol>::readBytes |
| 0.01% | python | sys_trace_start |
| 0.01% | _decimal.cpython-314-x86_64-linux-gnu.so | dec_str |
| 0.01% | _random.cpython-314-x86_64-linux-gnu.so | genrand_uint32 |
| 0.01% | libm-2.31.so | pow |
| 0.01% | libpthread-2.31.so | sem_post@@GLIBC_2.2.5 |
| 0.01% | fastbinary.cpython-314-x86_64-linux-gnu.so | apache::thrift::py::ProtocolBase<apache::thrift::py::BinaryProtocol>::readStruct |
| 0.01% | _decimal.cpython-314-x86_64-linux-gnu.so | mpd_qfinalize.part.0 |
| 0.01% | libpthread-2.31.so | sem_trywait@@GLIBC_2.2.5 |
| 0.01% | libz.so.1.2.11 | inflateCodesUsed |
| 0.01% | _elementtree.cpython-314-x86_64-linux-gnu.so | expat_data_handler |
| 0.01% | _decimal.cpython-314-x86_64-linux-gnu.so | _mpd_baseadd |
| 0.01% | pyexpat.cpython-314-x86_64-linux-gnu.so | storeAtts |
| 0.01% | _asyncio.cpython-314-x86_64-linux-gnu.so | FutureObj_clear |
| 0.01% | python | sre_ucs4_match |
| 0.01% | _asyncio.cpython-314-x86_64-linux-gnu.so | task_call_step_soon |
| 0.01% | _decimal.cpython-314-x86_64-linux-gnu.so | ctx_mpd_qquantize |
| 0.01% | fastbinary.cpython-314-x86_64-linux-gnu.so | apache::thrift::py::BinaryProtocol::readFieldBegin |
| 0.01% | _asyncio.cpython-314-x86_64-linux-gnu.so | FutureIter_traverse |
| 0.01% | _asyncio.cpython-314-x86_64-linux-gnu.so | TaskObj_finalize |
| 0.01% | libssl.so.1.1 | DTLSv1_client_method |
| 0.01% | tracer.cpython-314-x86_64-linux-gnu.so | CTracer_set_pdata_stack |
| 0.01% | _elementtree.cpython-314-x86_64-linux-gnu.so | element_gc_clear |
| 0.01% | _decimal.cpython-314-x86_64-linux-gnu.so | _mpd_to_string |
| 0.01% | array.cpython-314-x86_64-linux-gnu.so | d_getitem |
| 0.01% | _struct.cpython-314-x86_64-linux-gnu.so | s_pack_internal.isra.0 |
| 0.01% | _decimal.cpython-314-x86_64-linux-gnu.so | mpd_del |
| 0.01% | _asyncio.cpython-314-x86_64-linux-gnu.so | future_add_done_callback |
| 0.01% | _decimal.cpython-314-x86_64-linux-gnu.so | 0x0000000000007bc4 |
| 0.00% | _elementtree.cpython-314-x86_64-linux-gnu.so | expat_start_handler |
| 0.00% | _decimal.cpython-314-x86_64-linux-gnu.so | mpd_qmul |
| 0.00% | _decimal.cpython-314-x86_64-linux-gnu.so | current_context |
| 0.00% | array.cpython-314-x86_64-linux-gnu.so | 0x00000000000047e4 |
| 0.00% | array.cpython-314-x86_64-linux-gnu.so | 0x0000000000004644 |
| 0.00% | ld-2.31.so | _dl_debug_state |
| 0.00% | _cmsgpack.cpython-314-x86_64-linux-gnu.so | __pyx_f_7msgpack_9_cmsgpack_6Packer__pack |
| 0.00% | array.cpython-314-x86_64-linux-gnu.so | 0x00000000000049c4 |
| 0.00% | _struct.cpython-314-x86_64-linux-gnu.so | s_pack |
| 0.00% | math.cpython-314-x86_64-linux-gnu.so | math_factorial |
| 0.00% | _decimal.cpython-314-x86_64-linux-gnu.so | PyDecType_FromLongExact |
| 0.00% | _json.cpython-314-x86_64-linux-gnu.so | 0x0000000000002714 |
| 0.00% | fastbinary.cpython-314-x86_64-linux-gnu.so | apache::thrift::py::parse_struct_item_spec |
| 0.00% | libpthread-2.31.so | __nptl_deallocate_tsd.part.0 |
| 0.00% | _struct.cpython-314-x86_64-linux-gnu.so | s_unpack_internal.isra.0 |
| 0.00% | _elementtree.cpython-314-x86_64-linux-gnu.so | makeuniversal.isra.0 |
| 0.00% | _json.cpython-314-x86_64-linux-gnu.so | 0x00000000000024c4 |
| 0.00% | _elementtree.cpython-314-x86_64-linux-gnu.so | element_getitem |
| 0.00% | _asyncio.cpython-314-x86_64-linux-gnu.so | task_step |
| 0.00% | _struct.cpython-314-x86_64-linux-gnu.so | unpack |
| 0.00% | math.cpython-314-x86_64-linux-gnu.so | math_sin |
| 0.00% | _struct.cpython-314-x86_64-linux-gnu.so | pack |
| 0.00% | _asyncio.cpython-314-x86_64-linux-gnu.so | future_new_iter |
| 0.00% | _json.cpython-314-x86_64-linux-gnu.so | 0x0000000000002464 |
| 0.00% | python | _sre_SRE_Pattern_sub |
| 0.00% | _heapq.cpython-314-x86_64-linux-gnu.so | siftdown |

### dynamic

6.03% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 0.39% | python | PyObject_RichCompareBool |
| 0.33% | python | PyType_IsSubtype |
| 0.31% | python | PyObject_Hash |
| 0.31% | python | PyObject_GenericGetAttr |
| 0.26% | python | PyNumber_AsSsize_t |
| 0.23% | python | PyObject_GetAttr |
| 0.21% | python | _PyObject_GetMethod |
| 0.19% | python | _PyObject_GenericGetAttrWithDict |
| 0.18% | python | _PyObject_MakeTpCall |
| 0.16% | python | PyObject_Malloc |
| 0.15% | python | type_ready |
| 0.14% | python | PyObject_GetItem |
| 0.13% | python | _PyObject_TryGetInstanceAttribute |
| 0.13% | python | PyObject_IsTrue |
| 0.13% | python | PyObject_Vectorcall |
| 0.12% | python | _PyType_GetDict |
| 0.12% | python | PyObject_Free |
| 0.10% | python | PyObject_ClearManagedDict |
| 0.10% | python | type_call |
| 0.10% | python | _PyObject_LookupSpecial |
| 0.10% | python | PyObject_GetOptionalAttr |
| 0.10% | python | PyObject_VisitManagedDict |
| 0.08% | python | PyObject_RichCompare |
| 0.08% | python | PyObject_GetIter |
| 0.08% | python | PyObject_CallOneArg |
| 0.07% | python | PyObject_IsInstance |
| 0.07% | python | PyType_GetModuleByDef |
| 0.07% | python | getset_get |
| 0.06% | python | _PyObject_Call_Prepend |
| 0.06% | python | object_isinstance |
| 0.06% | python | PyObject_GenericSetAttr |
| 0.06% | python | PyObject_ClearWeakRefs |
| 0.05% | python | PyObject_SetAttr |
| 0.05% | python | PyObject_Call |
| 0.05% | python | PyNumber_Multiply |
| 0.05% | python | PyDescr_IsData |
| 0.04% | python | PyNumber_Add |
| 0.04% | python | PyObject_SetItem |
| 0.04% | python | PyIter_Next |
| 0.04% | python | PyObject_Size |
| 0.03% | python | PyNumber_TrueDivide |
| 0.03% | python | PyObject_VectorcallMethod |
| 0.03% | python | PyNumber_And |
| 0.03% | python | do_super_lookup |
| 0.03% | python | PySequence_Fast |
| 0.03% | python | method_get |
| 0.03% | python | StopIteration_init |
| 0.03% | python | _Py_type_getattro_impl |
| 0.03% | python | delitem_common |
| 0.03% | python | _PyObject_LookupSpecialMethod |
| 0.03% | python | slot_tp_richcompare |
| 0.03% | python | PyNumber_Subtract |
| 0.02% | python | _PyObject_ClearFreeLists |
| 0.02% | python | PySequence_Tuple |
| 0.02% | python | PyIter_Send |
| 0.02% | python | PyObject_Str |
| 0.02% | python | _PyObject_RealIsInstance |
| 0.02% | python | object_richcompare |
| 0.02% | python | PyNumber_FloorDivide |
| 0.02% | python | PySequence_Contains |
| 0.02% | python | PyNumber_Index |
| 0.02% | python | PyNumber_Xor |
| 0.02% | python | _PySuper_Lookup |
| 0.02% | python | _PyObject_InitInlineValues |
| 0.02% | python | object_get_class |
| 0.02% | python | PyNumber_Remainder |
| 0.01% | python | PyNumber_Rshift |
| 0.01% | python | _PyNumber_Index |
| 0.01% | python | PyObject_IsSubclass |
| 0.01% | python | PyNumber_InPlaceAdd |
| 0.01% | python | PyObject_GetBuffer |
| 0.01% | python | object_recursive_isinstance |
| 0.01% | python | PyObject_GenericHash |
| 0.01% | python | _PyObject_CallFunctionVa |
| 0.01% | python | PyMapping_GetOptionalItem |
| 0.01% | python | object_init |
| 0.01% | python | PyNumber_InPlaceTrueDivide |
| 0.01% | python | _PyObject_StoreInstanceAttribute |
| 0.01% | python | _PyObject_RealIsSubclass |
| 0.01% | python | _PyNumber_PowerNoMod |
| 0.01% | python | object_vacall |
| 0.01% | python | type_mro_modified |
| 0.01% | python | PyNumber_Negative |
| 0.01% | python | PyObject_SelfIter |
| 0.01% | python | PyObject_LengthHint |
| 0.01% | python | PyObject_SetAttrString |
| 0.01% | python | PyNumber_Lshift |
| 0.01% | python | PyObject_DelItem |
| 0.01% | python | PyIter_Check |
| 0.01% | python | PyMapping_Check |
| 0.01% | python | PyObject_HasAttrWithError |
| 0.01% | python | PySequence_GetItem |
| 0.00% | python | type___instancecheck__ |
| 0.00% | python | PyNumber_Long |
| 0.00% | python | PyObject_Repr |
| 0.00% | python | PyNumber_Or |
| 0.00% | python | type_clear |

### lookup

5.45% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 1.79% | python | unicodekeys_lookup_unicode |
| 1.58% | python | _Py_dict_lookup |
| 1.22% | python | _PyType_LookupRef |
| 0.24% | python | find_name_in_mro |
| 0.21% | python | update_one_slot |
| 0.20% | python | _Py_hashtable_get_entry_generic |
| 0.11% | python | _Py_type_getattro |
| 0.02% | python | _PyType_Lookup |
| 0.02% | python | _Py_hashtable_get |
| 0.02% | python | builtin_getattr |
| 0.02% | python | PyMember_GetOne |
| 0.01% | python | PyMember_SetOne |
| 0.01% | python | _Py_hashtable_destroy |

### kernel

4.20% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 0.68% | [kernel.kallsyms] | copy_user_enhanced_fast_string |
| 0.27% | [kernel.kallsyms] | clear_page_erms |
| 0.13% | [kernel.kallsyms] | native_irq_return_iret |
| 0.09% | [kernel.kallsyms] | sync_regs |
| 0.08% | [kernel.kallsyms] | rmqueue |
| 0.08% | [kernel.kallsyms] | __d_lookup_rcu |
| 0.07% | [kernel.kallsyms] | _raw_spin_lock |
| 0.07% | [kernel.kallsyms] | zap_pte_range.isra.0 |
| 0.05% | [kernel.kallsyms] | free_pcppages_bulk |
| 0.05% | [kernel.kallsyms] | memset_erms |
| 0.05% | [kernel.kallsyms] | __handle_mm_fault |
| 0.04% | [kernel.kallsyms] | try_charge |
| 0.04% | [kernel.kallsyms] | get_mem_cgroup_from_mm |
| 0.04% | [kernel.kallsyms] | release_pages |
| 0.04% | [kernel.kallsyms] | __pagevec_lru_add_fn |
| 0.03% | [kernel.kallsyms] | filemap_map_pages |
| 0.03% | [kernel.kallsyms] | link_path_walk.part.0 |
| 0.03% | [kernel.kallsyms] | ext4_htree_store_dirent |
| 0.03% | [kernel.kallsyms] | mem_cgroup_throttle_swaprate |
| 0.03% | [kernel.kallsyms] | __ext4fs_dirhash |
| 0.03% | [kernel.kallsyms] | mem_cgroup_try_charge |
| 0.03% | [kernel.kallsyms] | syscall_return_via_sysret |
| 0.03% | [kernel.kallsyms] | handle_mm_fault |
| 0.03% | [kernel.kallsyms] | __alloc_pages_nodemask |
| 0.02% | [kernel.kallsyms] | page_remove_rmap |
| 0.02% | [kernel.kallsyms] | kmem_cache_alloc |
| 0.02% | [kernel.kallsyms] | copy_page |
| 0.02% | [kernel.kallsyms] | perf_event_alloc |
| 0.02% | [kernel.kallsyms] | smp_call_function_single |
| 0.02% | [kernel.kallsyms] | filldir64 |
| 0.02% | [kernel.kallsyms] | kmem_cache_free |
| 0.02% | [kernel.kallsyms] | strncpy_from_user |
| 0.02% | [kernel.kallsyms] | entry_SYSCALL_64 |
| 0.02% | [kernel.kallsyms] | find_vma |
| 0.02% | [kernel.kallsyms] | kfree |
| 0.02% | [kernel.kallsyms] | do_user_addr_fault |
| 0.02% | [kernel.kallsyms] | find_get_entry |
| 0.02% | [kernel.kallsyms] | prep_new_page |
| 0.02% | [kernel.kallsyms] | memcg_kmem_get_cache |
| 0.02% | [kernel.kallsyms] | do_anonymous_page |
| 0.02% | [kernel.kallsyms] | do_syscall_64 |
| 0.02% | [kernel.kallsyms] | rb_insert_color |
| 0.02% | [kernel.kallsyms] | lookup_fast |
| 0.02% | [kernel.kallsyms] | vmacache_find |
| 0.02% | [kernel.kallsyms] | __virt_addr_valid |
| 0.02% | [kernel.kallsyms] | get_page_from_freelist |
| 0.01% | [kernel.kallsyms] | inode_permission |
| 0.01% | [kernel.kallsyms] | __slab_free |
| 0.01% | [kernel.kallsyms] | __count_memcg_events |
| 0.01% | [kernel.kallsyms] | error_entry |
| 0.01% | [kernel.kallsyms] | psi_task_change |
| 0.01% | [kernel.kallsyms] | _raw_spin_lock_irqsave |
| 0.01% | [kernel.kallsyms] | page_fault |
| 0.01% | [kernel.kallsyms] | str2hashbuf_signed |
| 0.01% | [kernel.kallsyms] | __mod_memcg_state |
| 0.01% | [kernel.kallsyms] | walk_component |
| 0.01% | [kernel.kallsyms] | ext4_getattr |
| 0.01% | [kernel.kallsyms] | rb_next |
| 0.01% | [kernel.kallsyms] | __mod_lruvec_state |
| 0.01% | [kernel.kallsyms] | update_load_avg |
| 0.01% | [kernel.kallsyms] | tcp_sendmsg_locked |
| 0.01% | [kernel.kallsyms] | generic_permission |
| 0.01% | [kernel.kallsyms] | memcpy_erms |
| 0.01% | [kernel.kallsyms] | perf_iterate_ctx |
| 0.01% | [kernel.kallsyms] | __fget_light |
| 0.01% | [kernel.kallsyms] | mutex_unlock |
| 0.01% | [kernel.kallsyms] | _cond_resched |
| 0.01% | [kernel.kallsyms] | security_inode_getattr |
| 0.01% | [kernel.kallsyms] | mutex_lock |
| 0.01% | [kernel.kallsyms] | up_read |
| 0.01% | [kernel.kallsyms] | entry_SYSCALL_64_after_hwframe |
| 0.01% | [kernel.kallsyms] | show_cpuinfo |
| 0.01% | [kernel.kallsyms] | lru_cache_add_active_or_unevictable |
| 0.01% | [kernel.kallsyms] | native_flush_tlb_one_user |
| 0.01% | [kernel.kallsyms] | down_read_trylock |
| 0.01% | [kernel.kallsyms] | __lru_cache_add |
| 0.01% | [kernel.kallsyms] | xas_load |
| 0.01% | [kernel.kallsyms] | vsnprintf |
| 0.01% | [kernel.kallsyms] | __check_object_size |
| 0.01% | [kernel.kallsyms] | __kmalloc |
| 0.01% | [kernel.kallsyms] | __ext4_check_dir_entry |
| 0.01% | [kernel.kallsyms] | page_add_file_rmap |
| 0.01% | [kernel.kallsyms] | set_root |
| 0.01% | [kernel.kallsyms] | rcu_all_qs |
| 0.01% | [kernel.kallsyms] | alloc_pages_vma |
| 0.01% | [kernel.kallsyms] | __mod_node_page_state |
| 0.01% | [kernel.kallsyms] | update_cfs_group |
| 0.01% | [kernel.kallsyms] | inherit_event.isra.0 |
| 0.01% | [kernel.kallsyms] | free_unref_page_list |
| 0.01% | [kernel.kallsyms] | __mod_zone_page_state |
| 0.01% | [kernel.kallsyms] | __legitimize_mnt |
| 0.01% | [kernel.kallsyms] | ___slab_alloc |
| 0.01% | [kernel.kallsyms] | __follow_mount_rcu.isra.0 |
| 0.01% | [kernel.kallsyms] | unlock_page |
| 0.01% | [kernel.kallsyms] | format_decode |
| 0.01% | [kernel.kallsyms] | alloc_set_pte |
| 0.01% | [kernel.kallsyms] | mem_cgroup_from_task |
| 0.01% | [kernel.kallsyms] | page_counter_cancel |
| 0.01% | [kernel.kallsyms] | in_group_p |
| 0.01% | [kernel.kallsyms] | swapgs_restore_regs_and_return_to_usermode |
| 0.01% | [kernel.kallsyms] | memchr |
| 0.01% | [kernel.kallsyms] | free_pages_and_swap_cache |
| 0.01% | [kernel.kallsyms] | __lock_text_start |
| 0.01% | [kernel.kallsyms] | pagevec_lru_move_fn |
| 0.01% | [kernel.kallsyms] | skb_release_data |
| 0.01% | [kernel.kallsyms] | __vma_adjust |
| 0.01% | [kernel.kallsyms] | mem_cgroup_commit_charge |
| 0.01% | [kernel.kallsyms] | free_unref_page_prepare.part.0 |
| 0.01% | [kernel.kallsyms] | security_inode_permission |
| 0.01% | [kernel.kallsyms] | fpregs_assert_state_consistent |
| 0.01% | [kernel.kallsyms] | lockref_put_return |
| 0.01% | [kernel.kallsyms] | native_sched_clock |
| 0.01% | [kernel.kallsyms] | call_filldir |
| 0.01% | [kernel.kallsyms] | __free_pages_ok |
| 0.01% | [kernel.kallsyms] | memcg_kmem_put_cache |
| 0.01% | [kernel.kallsyms] | generic_file_buffered_read |
| 0.01% | [kernel.kallsyms] | string_nocheck |
| 0.01% | [kernel.kallsyms] | free_unref_page_commit |
| 0.01% | [kernel.kallsyms] | update_curr |
| 0.01% | [kernel.kallsyms] | vfs_getattr_nosec |
| 0.01% | [kernel.kallsyms] | kmem_cache_alloc_trace |
| 0.01% | [kernel.kallsyms] | fsnotify |
| 0.01% | [kernel.kallsyms] | __check_heap_object |
| 0.01% | [kernel.kallsyms] | enqueue_task_fair |
| 0.01% | [kernel.kallsyms] | getname_flags |
| 0.01% | [kernel.kallsyms] | __update_load_avg_se |
| 0.01% | [kernel.kallsyms] | reweight_entity |
| 0.01% | [kernel.kallsyms] | mem_cgroup_try_charge_delay |
| 0.01% | [kernel.kallsyms] | __lookup_mnt |
| 0.01% | [kernel.kallsyms] | kthread_blkcg |
| 0.01% | [kernel.kallsyms] | vma_interval_tree_insert |
| 0.00% | [kernel.kallsyms] | page_counter_try_charge |
| 0.00% | [kernel.kallsyms] | native_write_msr |
| 0.00% | [kernel.kallsyms] | switch_fpu_return |
| 0.00% | [kernel.kallsyms] | __do_page_fault |
| 0.00% | [kernel.kallsyms] | pmd_devmap_trans_unstable |
| 0.00% | [kernel.kallsyms] | nmi_restore |
| 0.00% | [kernel.kallsyms] | read_tsc |
| 0.00% | [kernel.kallsyms] | cp_new_stat |
| 0.00% | [kernel.kallsyms] | do_dentry_open |
| 0.00% | [kernel.kallsyms] | page_add_new_anon_rmap |
| 0.00% | [kernel.kallsyms] | tcp_ack |
| 0.00% | [kernel.kallsyms] | __tcp_transmit_skb |
| 0.00% | [kernel.kallsyms] | xas_start |
| 0.00% | [kernel.kallsyms] | htree_dirblock_to_tree |
| 0.00% | [kernel.kallsyms] | fput_many |
| 0.00% | [kernel.kallsyms] | mem_cgroup_page_lruvec |
| 0.00% | [kernel.kallsyms] | account_kernel_stack |
| 0.00% | [kernel.kallsyms] | uncharge_page |
| 0.00% | [kernel.kallsyms] | mem_cgroup_charge_statistics |
| 0.00% | [kernel.kallsyms] | rb_next_postorder |
| 0.00% | [kernel.kallsyms] | vm_normal_page |
| 0.00% | [kernel.kallsyms] | mem_cgroup_update_lru_size |
| 0.00% | [kernel.kallsyms] | __update_load_avg_cfs_rq |
| 0.00% | [kernel.kallsyms] | common_perm |
| 0.00% | [kernel.kallsyms] | unmap_page_range |
| 0.00% | [kernel.kallsyms] | futex_wake |
| 0.00% | [kernel.kallsyms] | map_id_up |
| 0.00% | [kernel.kallsyms] | __fput |
| 0.00% | [kernel.kallsyms] | unmapped_area_topdown |
| 0.00% | [kernel.kallsyms] | free_one_page |
| 0.00% | [kernel.kallsyms] | __x86_indirect_thunk_rax |
| 0.00% | [kernel.kallsyms] | mark_page_accessed |
| 0.00% | [kernel.kallsyms] | prepare_exit_to_usermode |
| 0.00% | [kernel.kallsyms] | tcp_write_xmit |
| 0.00% | [kernel.kallsyms] | cpuacct_charge |
| 0.00% | [kernel.kallsyms] | lockref_get_not_dead |
| 0.00% | [kernel.kallsyms] | ext4_search_dir |
| 0.00% | [kernel.kallsyms] | __skb_datagram_iter |
| 0.00% | [kernel.kallsyms] | try_to_wake_up |
| 0.00% | [kernel.kallsyms] | do_page_fault |
| 0.00% | [kernel.kallsyms] | may_open.isra.0 |
| 0.00% | [kernel.kallsyms] | vma_interval_tree_remove |
| 0.00% | [kernel.kallsyms] | path_init |
| 0.00% | [kernel.kallsyms] | ip_finish_output2 |
| 0.00% | [kernel.kallsyms] | __dev_queue_xmit |
| 0.00% | [kernel.kallsyms] | page_mapping |
| 0.00% | [kernel.kallsyms] | __inc_numa_state |
| 0.00% | [kernel.kallsyms] | down_write |

### int

4.01% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 0.90% | python | k_mul |
| 0.48% | python | x_divrem |
| 0.40% | python | _PyLong_Add |
| 0.22% | python | long_hash |
| 0.18% | python | x_add |
| 0.18% | python | PyLong_FromLong |
| 0.15% | python | _PyLong_Subtract |
| 0.13% | python | PyLong_AsSsize_t |
| 0.12% | python | long_bitwise |
| 0.12% | python | long_richcompare |
| 0.11% | python | PyLong_FromSsize_t |
| 0.11% | python | x_sub |
| 0.11% | python | long_to_decimal_string_internal |
| 0.08% | python | PyLong_FromString |
| 0.06% | python | long_div |
| 0.06% | python | _PyLong_Multiply |
| 0.05% | python | long_rshift1 |
| 0.05% | python | PyLong_AsDouble |
| 0.05% | python | l_mod |
| 0.04% | python | long_and |
| 0.04% | python | PyLong_AsLongAndOverflow |
| 0.03% | python | PyLong_AsLong |
| 0.03% | python | long_add |
| 0.03% | python | long_mul |
| 0.03% | python | PyLong_FromVoidPtr |
| 0.03% | python | long_rshift |
| 0.03% | python | PyLong_FromUnsignedLong |
| 0.02% | python | long_lshift1 |
| 0.02% | python | long_xor |
| 0.02% | python | long_lshift |
| 0.01% | python | _PyLong_GCD |
| 0.01% | python | PyLong_FromUnsignedLongLong |
| 0.01% | python | long_mod |
| 0.01% | python | PyLong_FromLongLong |
| 0.01% | python | long_to_decimal_string |
| 0.01% | python | long_neg |
| 0.01% | python | long_float |
| 0.01% | python | PyLong_AsInt |
| 0.01% | python | _PyLong_Frexp |
| 0.01% | python | _PyLong_FromByteArray |
| 0.01% | python | long_sub |
| 0.00% | python | long_or |
| 0.00% | python | PyLong_AsUnsignedLong |

### libc

3.21% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 2.01% | libc-2.31.so | __nss_database_lookup |
| 0.44% | libc-2.31.so | pthread_attr_setschedparam |
| 0.35% | libcrypto.so.1.1 | CRYPTO_secure_actual_size |
| 0.10% | libc-2.31.so | malloc |
| 0.04% | libc-2.31.so | free |
| 0.03% | libc-2.31.so | __gconv_get_alias_db |
| 0.02% | libc-2.31.so | pthread_self |
| 0.02% | libc-2.31.so | wcsrtombs |
| 0.01% | libc-2.31.so | clock_gettime |
| 0.01% | libc-2.31.so | __libc_realloc |
| 0.01% | libc-2.31.so | __xstat |
| 0.01% | libcrypto.so.1.1 | AES_unwrap_key |
| 0.01% | libcrypto.so.1.1 | MD4 |
| 0.00% | libc-2.31.so | __wcsncasecmp_l |
| 0.00% | libcrypto.so.1.1 | OPENSSL_LH_node_usage_stats |
| 0.00% | libcrypto.so.1.1 | CRYPTO_gcm128_release |
| 0.00% | libc-2.31.so | psiginfo |
| 0.00% | libc-2.31.so | wcstombs |

### str

2.51% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 0.44% | python | siphash13 |
| 0.13% | python | _PyUnicode_FromUCS1.part.0 |
| 0.13% | python | replace |
| 0.12% | python | _PyUnicode_JoinArray.part.0 |
| 0.11% | python | intern_constants |
| 0.11% | python | ascii_decode |
| 0.10% | python | PyUnicode_Substring |
| 0.09% | python | _copy_characters.part.0.constprop.0 |
| 0.07% | python | intern_common.part.0 |
| 0.07% | python | resize_compact |
| 0.06% | python | _PyUnicode_Equal |
| 0.05% | python | PyUnicode_RichCompare |
| 0.05% | python | PyUnicode_Contains |
| 0.05% | python | _PyUnicode_InternImmortal |
| 0.04% | python | PyBytes_FromStringAndSize |
| 0.04% | python | _PyUnicodeWriter_WriteStr |
| 0.04% | python | unicode_decode_utf8.part.0 |
| 0.04% | python | PyUnicode_Format |
| 0.04% | python | _PyUnicode_InternMortal |
| 0.04% | python | unicode_replace |
| 0.03% | python | _PyUnicode_FromUCS4.part.0 |
| 0.03% | python | _PyUnicodeWriter_PrepareInternal |
| 0.03% | python | unicode_hash |
| 0.03% | python | unicode_from_format |
| 0.03% | python | bytes_subscript |
| 0.02% | python | PyUnicode_AsUCS4 |
| 0.02% | python | stringlib_bytes_join |
| 0.02% | python | PyUnicode_Concat |
| 0.02% | python | split |
| 0.01% | python | _PyUnicode_ClearInterned |
| 0.01% | python | unicode_subscript |
| 0.01% | python | _PyUnicodeWriter_WriteSubstring |
| 0.01% | python | PyUnicode_FromWideChar |
| 0.01% | python | PyUnicode_DecodeUTF8 |
| 0.01% | python | PyBytes_Repr |
| 0.01% | python | _PyUnicodeWriter_WriteASCIIString |
| 0.01% | python | PyUnicode_AsUTF8AndSize |
| 0.01% | python | PyUnicode_Decode.part.0 |
| 0.01% | python | unicode_rstrip |
| 0.01% | python | _PyUnicodeWriter_Init |
| 0.01% | python | bytes_richcompare |
| 0.01% | python | unicode_lower |
| 0.01% | python | PyUnicode_InternFromString |
| 0.01% | python | _PyUnicode_IsAlpha |
| 0.01% | python | bytes_concat |
| 0.01% | python | unicode_decode_utf8_impl |
| 0.01% | python | PyUnicode_Splitlines |
| 0.01% | python | _PyUnicode_TranslateCharmap |
| 0.01% | python | PyUnicode_FromKindAndData |
| 0.01% | python | unicode_join |
| 0.01% | python | unicode_startswith |
| 0.01% | python | unicode_rpartition |
| 0.01% | python | _PyUnicode_ToLowercase |
| 0.01% | python | PyUnicode_AsEncodedString.part.0 |
| 0.01% | python | unicode_repr |
| 0.01% | python | unicode_encode_utf8 |
| 0.01% | python | unicode_vectorcall |
| 0.01% | python | unicode_fromformat_write_utf8 |
| 0.01% | python | _PyUnicodeWriter_Finish |
| 0.01% | python | unicode_decode_utf8 |
| 0.01% | python | bytes_length |
| 0.01% | python | PyUnicode_FromEncodedObject |
| 0.01% | python | PyUnicode_EncodeFSDefault |
| 0.01% | python | _PyUnicode_IsLowercase |
| 0.01% | python | _PyUnicode_EqualToASCIIString |
| 0.01% | python | _PyUnicode_EQ |
| 0.01% | python | PyUnicode_FindChar |
| 0.00% | python | bytes_buffer_getbuffer |
| 0.00% | python | PyUnicode_Append |
| 0.00% | python | _PyUnicodeWriter_WriteChar |
| 0.00% | python | unicode_endswith |
| 0.00% | python | _PyUnicode_IsDigit |
| 0.00% | python | PyUnicode_FromString |
| 0.00% | python | unicode_length |
| 0.00% | python | PyBytes_FromStringAndSize.constprop.0 |
| 0.00% | python | unicode_encode |
| 0.00% | python | _PyUnicode_IsDecimalDigit |
| 0.00% | python | PyUnicode_CompareWithASCIIString |
| 0.00% | python | PyUnicode_DecodeFSDefaultAndSize |
| 0.00% | python | stringlib__two_way |
| 0.00% | python | unicode_rfind |
| 0.00% | python | _PyUnicode_IsTitlecase |
| 0.00% | python | bytes_hash |

### unknown

2.50% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 0.06% | python | PyThreadState_Get |
| 0.06% | python | compute_range_length |
| 0.05% | python | func_clear |
| 0.04% | python | slot_tp_init |
| 0.04% | python | PyThread_get_thread_ident |
| 0.04% | python | min_max |
| 0.03% | python | _Py_MakeCoro |
| 0.03% | python | _Py_HashBytes |
| 0.03% | python | _PyStack_UnpackDict |
| 0.03% | python | context_run |
| 0.03% | python | zip_next |
| 0.03% | python | new_keys_object.constprop.0 |
| 0.03% | python | PyContextVar_Get |
| 0.02% | python | sys_audit_tstate |
| 0.02% | python | _PyIO_find_line_ending |
| 0.02% | [vdso] | __vdso_clock_gettime |
| 0.02% | python | _io_TextIOWrapper_write |
| 0.02% | python | store_instance_attr_lock_held |
| 0.02% | python | _PyCfg_OptimizeCodeUnit |
| 0.02% | python | hashtable_unicode_compare |
| 0.02% | python | _io_BytesIO_read |
| 0.02% | python | PySys_Audit |
| 0.02% | python | PyIndex_Check |
| 0.02% | python | builtin_sum |
| 0.02% | python | bounded_lru_cache_wrapper |
| 0.02% | python | pysiphash |
| 0.02% | python | code_hash |
| 0.02% | python | _PyCoro_GetAwaitableIter |
| 0.02% | python | _PyAssemble_MakeCodeObject |
| 0.02% | python | hashtable_unicode_hash |
| 0.02% | python | do_mkvalue |
| 0.02% | python | PyContext_CopyCurrent |
| 0.01% | python | slot_mp_subscript |
| 0.01% | python | memcmp@plt |
| 0.01% | python | _PyArena_Malloc |
| 0.01% | python | primary_rule |
| 0.01% | python | build_indices_generic |
| 0.01% | python | wrapperdescr_call |
| 0.01% | python | pthread_self@plt |
| 0.01% | python | _PyFunction_ClearCodeByVersion |
| 0.01% | python | map_next |
| 0.01% | python | term_rule |
| 0.01% | python | unsafe_tuple_compare |
| 0.01% | python | slot_tp_hash |
| 0.01% | python | _PyFunction_SetVersion |
| 0.01% | python | _PyModule_ClearDict |
| 0.01% | python | _Py_Specialize_LoadAttr |
| 0.01% | python | fill_time |
| 0.01% | python | _PyCfg_OptimizedCfgToInstructionSequence |
| 0.01% | python | dictitems_iter |
| 0.01% | python | builtin_hasattr |
| 0.01% | python | tailmatch |
| 0.01% | python | _PyType_FromMetaclass_impl |
| 0.01% | python | _Py_convert_optional_to_ssize_t |
| 0.01% | python | os_stat |
| 0.01% | python | vectorcall_maybe.constprop.0 |
| 0.01% | python | weakref___init__ |
| 0.01% | python | write_bytes |
| 0.01% | python | _PyObjectDict_SetItem |
| 0.01% | python | path_converter |
| 0.01% | python | member_get |
| 0.01% | python | unsafe_long_compare |
| 0.01% | python | subtype_clear |
| 0.01% | python | any_find_slice |
| 0.01% | python | mro_implementation_unlocked |
| 0.01% | python | analyze_descriptor |
| 0.01% | python | binary_op1 |
| 0.01% | python | inversion_rule |
| 0.01% | python | _Py_Specialize_Call |
| 0.01% | python | write_str |
| 0.01% | python | _io_open |
| 0.01% | python | builtin_id |
| 0.01% | python | strlen@plt |
| 0.01% | python | compiler_visit_expr |
| 0.01% | python | sum_rule |
| 0.01% | python | insert_split_value |
| 0.01% | python | copy_lock_held |
| 0.01% | python | _pystat_fromstructstat |
| 0.01% | python | setitem_take2_lock_held |
| 0.01% | python | islice_next |
| 0.01% | python | ScandirIterator_iternext |
| 0.01% | python | wrap_descr_get |
| 0.01% | python | slot_tp_iter |
| 0.01% | python | insert_split_key |
| 0.01% | python | unsafe_latin_compare |
| 0.01% | python | builtin_any |
| 0.01% | python | countformat |
| 0.01% | python | bitwise_or_rule |
| 0.01% | python | weakref_richcompare |
| 0.01% | python | _PyFrame_MakeAndSetFrameObject |
| 0.01% | python | mro_internal_unlocked.isra.0 |
| 0.01% | python | lru_cache_make_key |
| 0.01% | python | build_string |
| 0.01% | python | shift_expr_rule |
| 0.01% | python | _PyBytes_FromList |
| 0.01% | python | 0x0000000000080750 |
| 0.01% | python | _Py_bytes_lower |
| 0.01% | python | basicblock_remove_redundant_nops |
| 0.01% | python | _PyStaticType_InitBuiltin |
| 0.01% | python | bitwise_xor_rule |
| 0.01% | python | slot_sq_contains |
| 0.01% | python | slot_mp_ass_subscript |
| 0.01% | python | getset_set |
| 0.01% | python | _PyFunction_FromConstructor |
| 0.01% | python | builtin___build_class__ |
| 0.01% | python | chain_next |
| 0.01% | python | wrapperdescr_get |
| 0.01% | python | PyTime_AsSecondsDouble |
| 0.01% | python | bitwise_and_rule |
| 0.01% | python | scan_block_for_locals |
| 0.01% | python | slot_tp_call |
| 0.01% | python | slot_tp_iternext |
| 0.01% | python | func_descr_get |
| 0.01% | python | make_dict_from_instance_attributes |
| 0.01% | python | _PyInstructionSequence_Addop |
| 0.01% | python | posix_do_stat.isra.0 |
| 0.01% | python | symtable_visit_expr |
| 0.01% | python | _Py_call_instrumentation_arg |
| 0.01% | python | 0x0000000000080758 |
| 0.01% | python | do_strip |
| 0.01% | python | _validate_inner |
| 0.01% | python | _abc__abc_instancecheck |
| 0.01% | python | assign_version_tag |
| 0.01% | python | va_build_value |
| 0.01% | python | astfold_expr |
| 0.01% | python | sm_descr_get |
| 0.01% | python | _PyStaticType_GetState |
| 0.01% | python | _PyCfg_FromInstructionSequence |
| 0.01% | python | partial_vectorcall |
| 0.00% | python | write_location_info_entry |
| 0.00% | python | remove_unreachable |
| 0.00% | python | builtin_print |
| 0.00% | python | PyThread_acquire_lock_timed_with_retries |
| 0.00% | python | disjunction_rule |
| 0.00% | python | _PyType_GetModuleByDef2 |
| 0.00% | python | PyFile_WriteObject |
| 0.00% | python | slot_nb_subtract |
| 0.00% | python | slot_sq_length |
| 0.00% | python | builtin_issubclass |
| 0.00% | python | _PyDictKeys_StringLookup |
| 0.00% | python | memmove@plt |
| 0.00% | python | _Py_module_getattro_impl |
| 0.00% | python | analyze_block |
| 0.00% | python | expression_rule |
| 0.00% | python | t_primary_rule |
| 0.00% | python | _Py_slot_tp_getattr_hook |
| 0.00% | python | atom_rule |
| 0.00% | python | _PyFrame_ClearLocals |
| 0.00% | python | _PyTokenizer_Get |
| 0.00% | python | unsafe_object_compare |
| 0.00% | python | update_slot |
| 0.00% | python | _PyCompile_EnsureArrayLargeEnough |
| 0.00% | python | _PyParkingLot_Unpark |
| 0.00% | python | recursive_issubclass |
| 0.00% | python | PyStructSequence_SetItem |
| 0.00% | python | delitem_knownhash_lock_held |
| 0.00% | python | merge_at |
| 0.00% | python | _PyArena_AddPyObject |
| 0.00% | python | rlock_acquire |
| 0.00% | python | gen_close |
| 0.00% | python | _Py_VaBuildStack |
| 0.00% | python | find_frozen.part.0 |
| 0.00% | python | specialize_py_call |
| 0.00% | python | _PyAST_Name |
| 0.00% | python | conjunction_rule |
| 0.00% | python | best_base |
| 0.00% | python | _io_FileIO___init__ |
| 0.00% | python | __errno_location@plt |
| 0.00% | python | wrapper_call |
| 0.00% | python | os_fspath |
| 0.00% | python | factor_rule |
| 0.00% | python | slot_sq_item |
| 0.00% | python | propagate_line_numbers |
| 0.00% | python | _PyBytes_Resize |
| 0.00% | python | findchar |
| 0.00% | python | remove_all_subclasses |
| 0.00% | python | classmethod_get |
| 0.00% | python | duplicate_exits_without_lineno |
| 0.00% | python | PyThread_get_thread_ident_ex |
| 0.00% | python | _io__Buffered_read |
| 0.00% | python | gallop_left |
| 0.00% | python | stringio_iternext |
| 0.00% | python | _PyWeakref_ClearRef |
| 0.00% | python | _textiowrapper_writeflush |
| 0.00% | python | compute_range_item |
| 0.00% | python | wrap_objobjargproc |
| 0.00% | python | await_primary_rule |
| 0.00% | python | gallop_right |
| 0.00% | python | _Py_dg_dtoa |

### dict

2.29% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 0.38% | python | PyDict_GetItemRef |
| 0.35% | python | insertdict |
| 0.19% | python | dict_setdefault_ref_lock_held |
| 0.17% | python | insert_to_emptydict |
| 0.11% | python | find_empty_slot |
| 0.11% | python | _PyDict_GetItemRef_KnownHash |
| 0.10% | python | build_indices_unicode |
| 0.10% | python | dict_get |
| 0.09% | python | _PyDict_FromItems |
| 0.08% | python | dictiter_iternextitem |
| 0.07% | python | PyDict_SetItem |
| 0.06% | python | PyDict_Next |
| 0.04% | python | dictresize |
| 0.04% | python | dict_merge |
| 0.04% | python | PyDict_Contains |
| 0.04% | python | PyDict_GetItemWithError |
| 0.03% | python | _PyDict_LoadGlobal |
| 0.03% | python | dict_subscript |
| 0.03% | python | _PyDict_SetItem_Take2 |
| 0.02% | python | clone_combined_dict_keys.isra.0 |
| 0.02% | python | PyDict_Clear |
| 0.02% | python | PyDict_GetItem |
| 0.01% | python | dictiter_iternextkey |
| 0.01% | python | _PyDict_GetItem_KnownHash |
| 0.01% | python | dict_ass_sub |
| 0.01% | python | dictiter_iternextvalue |
| 0.01% | python | _PyDict_DelItemIf |
| 0.01% | python | dict_items |
| 0.01% | python | PyDict_DelItem |
| 0.01% | python | dict_tp_clear |
| 0.01% | python | PyDict_SetDefaultRef |
| 0.01% | python | dict_pop |
| 0.01% | python | _PyDict_Next.part.0 |
| 0.00% | python | PyDict_SetItemString |
| 0.00% | python | _PyDict_Pop_KnownHash.part.0 |
| 0.00% | python | _PyDict_Next |
| 0.00% | python | dict_update |

### miscobj

1.83% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 0.26% | python | set_lookkey |
| 0.25% | python | PySlice_AdjustIndices |
| 0.12% | python | _PyBuildSlice_ConsumeRefs |
| 0.11% | python | set_add_entry |
| 0.11% | python | set_issubset_impl |
| 0.10% | python | setiter_iternext |
| 0.09% | python | gen_iternext |
| 0.08% | python | make_gen |
| 0.06% | python | PySlice_Unpack |
| 0.05% | python | set_difference |
| 0.05% | python | _PySet_Contains |
| 0.04% | python | deque_append |
| 0.04% | python | range_iter |
| 0.04% | python | enum_next |
| 0.03% | python | set_table_resize |
| 0.03% | python | PyBuffer_Release |
| 0.03% | python | bytearray_ass_subscript |
| 0.03% | python | dequeiter_next |
| 0.02% | python | PyBool_FromLong |
| 0.02% | python | _PyGen_FetchStopIterationValue |
| 0.02% | python | _PyGen_Finalize |
| 0.02% | python | range_subscript |
| 0.02% | python | set_merge_lock_held.part.0 |
| 0.02% | python | PyBuffer_FillInfo |
| 0.02% | python | range_vectorcall |
| 0.01% | python | deque_popleft |
| 0.01% | python | PyGen_am_send |
| 0.01% | python | _PyGen_SetStopIterationValue |
| 0.01% | python | _PySlice_GetLongIndices |
| 0.01% | python | set_intersection |
| 0.01% | python | set_update_iterable_lock_held |
| 0.01% | python | PySet_Add |
| 0.01% | python | deque_clear.part.0 |
| 0.01% | python | set_richcompare |
| 0.01% | python | range_reverse |
| 0.01% | python | set_difference_update_internal |
| 0.01% | python | set_iter |
| 0.00% | python | set_vectorcall |
| 0.00% | python | set_add |
| 0.00% | python | _PyGen_yf |

### tuple

1.30% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 0.44% | python | tuplehash |
| 0.28% | python | _PyTuple_FromArray.part.0 |
| 0.25% | python | _PyTuple_FromStackRefSteal |
| 0.10% | python | tupletraverse |
| 0.06% | python | tuplerichcompare |
| 0.04% | python | PyTuple_Pack |
| 0.02% | python | _PyTuple_FromArray |
| 0.02% | python | tuple_iter |
| 0.02% | python | PyTuple_Size |
| 0.01% | python | tuplesubscript |
| 0.01% | python | tupleiter_next |
| 0.01% | python | _PyTuple_Resize |
| 0.01% | python | PyTuple_GetSlice |
| 0.00% | python | tuplecontains |
| 0.00% | python | PyTuple_GetItem |
| 0.00% | python | tuplegetter_descr_get |

### list

0.99% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 0.16% | python | list_ass_slice_lock_held |
| 0.14% | python | list_subscript |
| 0.08% | python | listiter_next |
| 0.08% | python | list_slice_lock_held.isra.0 |
| 0.05% | python | list_iter |
| 0.05% | python | PyList_Append |
| 0.05% | python | _list_extend |
| 0.05% | python | list_sort_impl |
| 0.05% | python | list_ass_subscript |
| 0.04% | python | list_contains |
| 0.04% | python | list_extend_lock_held |
| 0.04% | python | _PyList_AppendTakeRefListResize |
| 0.03% | python | list_concat |
| 0.03% | python | list_append |
| 0.02% | python | _PyList_FromArraySteal |
| 0.02% | python | list_pop |
| 0.01% | python | list_insert |
| 0.01% | python | list_length |
| 0.01% | python | list_item |
| 0.01% | python | list_richcompare |
| 0.00% | python | list_remove |
| 0.00% | python | _PyList_Extend |
| 0.00% | python | list_vectorcall |

### calls

0.62% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 0.07% | python | vgetargskeywords.constprop.0 |
| 0.07% | python | _PyFunction_Vectorcall |
| 0.07% | python | _Py_CheckFunctionResult |
| 0.07% | python | vgetargs1_impl |
| 0.05% | python | _PyArg_UnpackKeywords |
| 0.04% | python | PyArg_UnpackTuple |
| 0.03% | python | method_vectorcall |
| 0.02% | python | cfunction_vectorcall_O |
| 0.02% | python | cfunction_vectorcall_FASTCALL_KEYWORDS |
| 0.02% | python | method_vectorcall_FASTCALL_KEYWORDS_METHOD |
| 0.02% | python | vectorcall_method |
| 0.02% | python | _PyArg_UnpackKeywordsWithVararg |
| 0.02% | python | cfunction_vectorcall_NOARGS |
| 0.02% | python | method_vectorcall_O |
| 0.02% | python | method_vectorcall_VARARGS_KEYWORDS |
| 0.01% | python | PyArg_ParseTupleAndKeywords |
| 0.01% | python | PyArg_Parse |
| 0.01% | python | method_vectorcall_NOARGS |
| 0.01% | python | method_vectorcall_VARARGS |
| 0.01% | python | cfunction_call |
| 0.01% | python | PyArg_ParseTuple |
| 0.01% | python | cfunction_vectorcall_FASTCALL_KEYWORDS_METHOD |
| 0.00% | python | method_vectorcall_FASTCALL |

### exceptions

0.56% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 0.15% | python | _PyErr_SetObject.part.0 |
| 0.08% | python | PyErr_CheckSignals |
| 0.08% | python | PyCode_Addr2Line |
| 0.03% | python | PyErr_Occurred |
| 0.03% | python | PyErr_ExceptionMatches |
| 0.03% | python | _PyErr_Restore |
| 0.02% | python | _PyErr_ExceptionMatches |
| 0.02% | python | PyTraceBack_Here |
| 0.01% | python | PyErr_GetRaisedException |
| 0.01% | python | _PyErr_CreateException |
| 0.01% | python | BaseException_clear |
| 0.01% | python | PyErr_SetObject |
| 0.01% | python | PyException_GetTraceback |
| 0.01% | python | BaseException_vectorcall |
| 0.01% | python | PyErr_SetRaisedException |
| 0.01% | python | _PyErr_SetKeyError |
| 0.01% | python | PyFrame_GetCode |
| 0.01% | python | AttributeError_init |
| 0.00% | python | PyErr_GivenExceptionMatches |
| 0.00% | python | PyFrame_GetLineNumber |

### float

0.42% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 0.16% | python | PyFloat_FromDouble |
| 0.10% | python | float_div |
| 0.04% | python | float_richcompare |
| 0.03% | python | float_pow |
| 0.03% | python | float_sub |
| 0.02% | python | float_mul |
| 0.01% | python | float_rem |
| 0.01% | python | float_add |
| 0.01% | python | PyFloat_AsDouble |
| 0.01% | python | PyFloat_AsDouble.part.0 |

### import

0.35% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 0.30% | python | r_object |
| 0.03% | python | r_string |
| 0.01% | python | PyImport_ImportModuleLevelObject |
| 0.01% | python | r_byte |

### async

0.06% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 0.04% | python | async_gen_asend_iternext |
| 0.02% | python | async_gen_anext |

### compiler

0.05% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 0.03% | python | tok_get_normal_mode |
| 0.02% | python | tok_nextc |

### gil

0.04% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 0.03% | python | take_gil |
| 0.01% | python | drop_gil |
