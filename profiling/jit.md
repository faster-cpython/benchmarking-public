
## 2to3

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 15.17% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 10.32% | `[JIT]` | `jit` | jit |
| 3.39% | `python` | `gc_collect_region.isra.0` | gc |
| 3.13% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 3.03% | `python` | `_PyObject_Malloc` | memory |
| 2.28% | `python` | `_PyObject_Free` | memory |
| 2.28% | `python` | `_Py_dict_lookup` | lookup |
| 1.90% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.79% | `python` | `_PyType_LookupRef` | lookup |
| 1.48% | `python` | `tupledealloc` | memory |
| 1.40% | `python` | `sre_ucs1_match` | library |
| 1.39% | `python` | `visit_decref` | gc |
| 1.26% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 0.85% | `python` | `_PyTuple_FromStackRefSteal` | tuple |
| 0.84% | `python` | `PyObject_GenericGetAttr` | dynamic |
| 0.80% | `python` | `visit_reachable` | gc |
| 0.74% | `libc-2.31.so` | `pthread_attr_setschedparam` | libc |
| 0.70% | `python` | `_PyPegen_is_memoized` | interpreter |
| 0.64% | `python` | `r_object` | import |
| 0.60% | `python` | `_Py_Dealloc` | memory |
| 0.60% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.60% | `python` | `_PyObject_TryGetInstanceAttribute` | dynamic |
| 0.56% | `python` | `siphash13` | str |
| 0.56% | `python` | `PyObject_GetAttr` | dynamic |
| 0.55% | `python` | `PyObject_RichCompareBool` | dynamic |
| 0.52% | `python` | `update_one_slot` | lookup |
| 0.52% | `python` | `initialize_locals` | interpreter |
| 0.48% | `python` | `PyDict_GetItemRef` | dict |
| 0.46% | `python` | `dict_dealloc` | memory |
| 0.46% | `python` | `_Py_hashtable_get_entry_generic` | lookup |
| 0.42% | `python` | `_PyCode_Quicken` | interpreter |
| 0.42% | `python` | `find_name_in_mro` | lookup |
| 0.42% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.37% | `python` | `list_dealloc` | memory |
| 0.34% | `python` | `PyObject_GC_Del` | gc |
| 0.33% | `python` | `_PyPegen_expect_token` | interpreter |
| 0.31% | `python` | `insertdict` | dict |
| 0.31% | `python` | `gen_dealloc` | memory |
| 0.30% | `python` | `insert_to_emptydict` | dict |
| 0.30% | `python` | `_PyUnicode_FromUCS1.part.0` | str |
| 0.29% | `python` | `tok_get_normal_mode` | compiler |
| 0.29% | `python` | `PyList_New` | memory |
| 0.28% | `python` | `type_ready` | dynamic |
| 0.28% | `python` | `dict_traverse` | gc |
| 0.28% | `python` | `_PyCfg_OptimizeCodeUnit` | unknown |
| 0.27% | `python` | `intern_constants` | str |
| 0.27% | `python` | `_PyPegen_update_memo` | interpreter |
| 0.26% | `python` | `sre_ucs2_charset.isra.0` | library |
| 0.26% | `python` | `sre_ucs1_count` | library |
| 0.25% | `python` | `uop_optimize` | compiler |

## async_generators

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 22.71% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 7.98% | `python` | `_PyErr_SetObject.part.0` | exceptions |
| 4.03% | `python` | `_PyObject_Malloc` | memory |
| 3.80% | `python` | `_PyObject_Free` | memory |
| 3.53% | `[JIT]` | `jit` | jit |
| 2.66% | `python` | `async_gen_asend_iternext` | async |
| 2.43% | `python` | `PyType_GenericAlloc` | memory |
| 2.34% | `python` | `_PyTuple_FromArray.part.0` | tuple |
| 2.23% | `python` | `tupledealloc` | memory |
| 1.99% | `python` | `StopIteration_init` | dynamic |
| 1.82% | `python` | `async_gen_anext` | async |
| 1.69% | `python` | `_PyAsyncGenValueWrapperNew` | memory |
| 1.60% | `python` | `PyErr_ExceptionMatches` | exceptions |
| 1.56% | `python` | `_Py_Dealloc` | memory |
| 1.55% | `python` | `async_gen_wrapped_val_dealloc` | memory |
| 1.36% | `python` | `StopIteration_dealloc` | memory |
| 1.34% | `python` | `_PyGen_FetchStopIterationValue` | miscobj |
| 1.28% | `python` | `_PyObject_MakeTpCall` | dynamic |
| 1.25% | `python` | `async_gen_asend_dealloc` | memory |
| 1.16% | `python` | `_PyErr_ExceptionMatches` | exceptions |
| 1.15% | `python` | `PyObject_GC_UnTrack` | gc |
| 1.10% | `python` | `PyObject_GC_Del` | gc |
| 1.06% | `python` | `PyObject_CallOneArg` | dynamic |
| 1.05% | `python` | `_PyErr_Restore` | exceptions |
| 1.00% | `python` | `type_call` | dynamic |
| 0.93% | `python` | `_Py_NewReference` | memory |
| 0.91% | `python` | `gc_collect_region.isra.0` | gc |
| 0.88% | `python` | `_PyGen_SetStopIterationValue` | miscobj |
| 0.85% | `python` | `PyObject_CallFinalizerFromDealloc` | memory |
| 0.77% | `python` | `PyType_IsSubtype` | dynamic |
| 0.71% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 0.65% | `python` | `BaseException_new` | memory |
| 0.64% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 0.55% | `python` | `_PyErr_CreateException` | exceptions |
| 0.53% | `python` | `_PyObject_GC_Link` | gc |
| 0.52% | `python` | `PyObject_RichCompareBool` | dynamic |
| 0.51% | `python` | `initialize_locals` | interpreter |
| 0.49% | `python` | `visit_decref` | gc |
| 0.46% | `python` | `long_add` | int |
| 0.44% | `python` | `visit_reachable` | gc |
| 0.42% | `python` | `PyErr_SetObject` | exceptions |
| 0.41% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.37% | `python` | `_Py_CheckFunctionResult` | calls |
| 0.37% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.36% | `python` | `long_richcompare` | int |
| 0.34% | `python` | `range_subscript` | miscobj |
| 0.33% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.31% | `python` | `visit_add_to_container` | gc |
| 0.29% | `python` | `compute_range_length` | unknown |
| 0.26% | `python` | `PyNumber_Add` | dynamic |

## async_tree

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 20.40% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 9.00% | `python` | `gc_collect_region.isra.0` | gc |
| 4.42% | `python` | `visit_decref` | gc |
| 4.37% | `python` | `visit_reachable` | gc |
| 4.18% | `[JIT]` | `jit` | jit |
| 4.02% | `python` | `visit_add_to_container` | gc |
| 3.77% | `python` | `_PyObject_Malloc` | memory |
| 2.42% | `python` | `_PyObject_Free` | memory |
| 1.66% | `python` | `_Py_dict_lookup` | lookup |
| 1.56% | `python` | `_PyType_LookupRef` | lookup |
| 1.52% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.46% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 1.35% | `python` | `initialize_locals` | interpreter |
| 1.08% | `python` | `subtype_traverse` | gc |
| 0.89% | `python` | `context_tp_dealloc` | memory |
| 0.82% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.79% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 0.77% | `python` | `tupledealloc` | memory |
| 0.67% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.64% | `python` | `subtype_dealloc` | memory |
| 0.64% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.62% | `python` | `_PyGC_Collect` | gc |
| 0.59% | `python` | `_Py_Dealloc` | memory |
| 0.57% | `python` | `dict_traverse` | gc |
| 0.56% | `python` | `_PyFrame_Traverse` | interpreter |
| 0.54% | `python` | `PyDict_GetItemRef` | dict |
| 0.52% | `_asyncio.cpython-314-x86_64-linux-gnu.so` | `TaskObj_traverse` | library |
| 0.51% | `python` | `_PyEval_Vector` | interpreter |
| 0.51% | `python` | `insertdict` | dict |
| 0.50% | `python` | `_PyObject_GetMethod` | dynamic |
| 0.50% | `python` | `dict_dealloc` | memory |
| 0.49% | `python` | `PyObject_RichCompareBool` | dynamic |
| 0.47% | `python` | `_PyObject_GC_New` | gc |
| 0.44% | `python` | `_PyTuple_FromArray.part.0` | tuple |
| 0.44% | `python` | `gen_dealloc` | memory |
| 0.43% | `python` | `PyObject_GC_Del` | gc |
| 0.43% | `python` | `_PyObject_MakeTpCall` | dynamic |
| 0.40% | `python` | `PyObject_GenericGetAttr` | dynamic |
| 0.40% | `python` | `insert_to_emptydict` | dict |
| 0.38% | `python` | `_PyArg_UnpackKeywords` | calls |
| 0.35% | `python` | `PyType_GenericAlloc` | memory |
| 0.34% | `python` | `_PyThreadState_PopFrame` | interpreter |
| 0.32% | `python` | `gen_traverse` | gc |
| 0.32% | `python` | `list_dealloc` | memory |
| 0.31% | `python` | `_Py_NewReference` | memory |
| 0.30% | `python` | `_PyObject_Realloc` | memory |
| 0.29% | `python` | `dict_setdefault_ref_lock_held` | dict |
| 0.28% | `python` | `_PyObject_GC_Link` | gc |
| 0.28% | `python` | `PyObject_GetAttr` | dynamic |
| 0.27% | `[kernel.kallsyms]` | `clear_page_erms` | kernel |
| 0.27% | `_asyncio.cpython-314-x86_64-linux-gnu.so` | `TaskObj_clear` | library |
| 0.26% | `python` | `PyUnicode_RichCompare` | str |
| 0.26% | `python` | `_PyObject_Calloc` | memory |
| 0.26% | `[kernel.kallsyms]` | `native_irq_return_iret` | kernel |
| 0.25% | `python` | `PyObject_Vectorcall` | dynamic |

## async_tree_cpu_io_mixed

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 23.52% | `python` | `k_mul` | int |
| 14.45% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 5.77% | `python` | `gc_collect_region.isra.0` | gc |
| 4.09% | `python` | `_PyObject_Malloc` | memory |
| 3.49% | `python` | `_PyObject_Free` | memory |
| 3.13% | `python` | `visit_decref` | gc |
| 2.77% | `python` | `visit_reachable` | gc |
| 2.50% | `[JIT]` | `jit` | jit |
| 2.40% | `python` | `visit_add_to_container` | gc |
| 1.56% | `python` | `PyErr_CheckSignals` | exceptions |
| 1.15% | `python` | `_PyType_LookupRef` | lookup |
| 1.08% | `math.cpython-314-x86_64-linux-gnu.so` | `factorial_partial_product` | library |
| 1.03% | `python` | `_Py_dict_lookup` | lookup |
| 0.97% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 0.87% | `python` | `initialize_locals` | interpreter |
| 0.84% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.77% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 0.77% | `python` | `subtype_traverse` | gc |
| 0.71% | `python` | `PyThread_get_thread_ident` | unknown |
| 0.70% | `python` | `_Py_Dealloc` | memory |
| 0.66% | `python` | `PyLong_FromUnsignedLong` | int |
| 0.65% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.64% | `python` | `context_tp_dealloc` | memory |
| 0.50% | `python` | `long_mul` | int |
| 0.47% | `python` | `PyNumber_Multiply` | dynamic |
| 0.45% | `python` | `tupledealloc` | memory |
| 0.42% | `python` | `gen_dealloc` | memory |
| 0.41% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.41% | `python` | `_PyObject_GetMethod` | dynamic |
| 0.40% | `python` | `_PyEval_Vector` | interpreter |
| 0.40% | `python` | `_PyGC_Collect` | gc |
| 0.40% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.39% | `python` | `long_lshift1` | int |
| 0.37% | `python` | `subtype_dealloc` | memory |
| 0.36% | `python` | `_Py_NewReference` | memory |
| 0.34% | `python` | `PyObject_GenericGetAttr` | dynamic |
| 0.34% | `python` | `dict_traverse` | gc |
| 0.32% | `python` | `_PyFrame_Traverse` | interpreter |
| 0.32% | `python` | `dict_dealloc` | memory |
| 0.32% | `_asyncio.cpython-314-x86_64-linux-gnu.so` | `TaskObj_traverse` | library |
| 0.31% | `python` | `PyDict_GetItemRef` | dict |
| 0.29% | `python` | `_PyTuple_FromArray.part.0` | tuple |
| 0.28% | `python` | `PyObject_GC_Del` | gc |
| 0.28% | `python` | `_PyObject_GC_New` | gc |
| 0.28% | `python` | `PyObject_RichCompareBool` | dynamic |
| 0.27% | `libc-2.31.so` | `pthread_self` | libc |

## async_tree_cpu_io_mixed_tg

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 24.04% | `python` | `k_mul` | int |
| 13.52% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 6.32% | `python` | `gc_collect_region.isra.0` | gc |
| 4.11% | `python` | `_PyObject_Malloc` | memory |
| 3.69% | `python` | `visit_decref` | gc |
| 3.58% | `python` | `_PyObject_Free` | memory |
| 3.35% | `python` | `visit_add_to_container` | gc |
| 3.20% | `python` | `visit_reachable` | gc |
| 2.36% | `[JIT]` | `jit` | jit |
| 1.65% | `python` | `PyErr_CheckSignals` | exceptions |
| 1.12% | `math.cpython-314-x86_64-linux-gnu.so` | `factorial_partial_product` | library |
| 0.91% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 0.85% | `python` | `_PyType_LookupRef` | lookup |
| 0.83% | `python` | `initialize_locals` | interpreter |
| 0.82% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.81% | `python` | `subtype_traverse` | gc |
| 0.78% | `python` | `_Py_dict_lookup` | lookup |
| 0.78% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 0.72% | `python` | `PyThread_get_thread_ident` | unknown |
| 0.71% | `python` | `_Py_Dealloc` | memory |
| 0.67% | `python` | `PyLong_FromUnsignedLong` | int |
| 0.62% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.53% | `python` | `long_mul` | int |
| 0.47% | `python` | `_PyGC_Collect` | gc |
| 0.47% | `python` | `_PyFrame_Traverse` | interpreter |
| 0.46% | `python` | `PyNumber_Multiply` | dynamic |
| 0.45% | `python` | `_PyEval_Vector` | interpreter |
| 0.42% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.40% | `python` | `long_lshift1` | int |
| 0.39% | `python` | `subtype_dealloc` | memory |
| 0.39% | `python` | `tupledealloc` | memory |
| 0.39% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.38% | `python` | `PyObject_GenericGetAttr` | dynamic |
| 0.36% | `python` | `_Py_NewReference` | memory |
| 0.32% | `_asyncio.cpython-314-x86_64-linux-gnu.so` | `TaskObj_traverse` | library |
| 0.30% | `python` | `PyObject_RichCompareBool` | dynamic |
| 0.30% | `python` | `_PyObject_GetMethod` | dynamic |
| 0.29% | `python` | `set_traverse` | gc |
| 0.29% | `libc-2.31.so` | `pthread_self` | libc |
| 0.28% | `python` | `PyType_GenericAlloc` | memory |
| 0.28% | `python` | `PyObject_GC_Del` | gc |
| 0.27% | `python` | `PyDict_GetItemRef` | dict |
| 0.26% | `python` | `_PyObject_GC_New` | gc |
| 0.26% | `python` | `_PyObject_MakeTpCall` | dynamic |
| 0.25% | `python` | `_PyTuple_FromArray.part.0` | tuple |
| 0.25% | `python` | `long_dealloc` | memory |

## async_tree_io

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 19.05% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 14.13% | `python` | `gc_collect_region.isra.0` | gc |
| 7.12% | `python` | `visit_add_to_container` | gc |
| 6.99% | `python` | `visit_decref` | gc |
| 6.55% | `python` | `visit_reachable` | gc |
| 2.87% | `[JIT]` | `jit` | jit |
| 2.69% | `python` | `_PyObject_Malloc` | memory |
| 1.68% | `python` | `_PyObject_Free` | memory |
| 1.36% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.30% | `python` | `subtype_traverse` | gc |
| 1.28% | `python` | `initialize_locals` | interpreter |
| 1.20% | `python` | `_PyFrame_Traverse` | interpreter |
| 1.20% | `python` | `_PyType_LookupRef` | lookup |
| 1.12% | `python` | `_PyGC_Collect` | gc |
| 0.85% | `python` | `_Py_dict_lookup` | lookup |
| 0.80% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.75% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.74% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.71% | `python` | `_PyEval_Vector` | interpreter |
| 0.66% | `python` | `gen_traverse` | gc |
| 0.60% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.54% | `python` | `tupledealloc` | memory |
| 0.54% | `python` | `PyObject_RichCompareBool` | dynamic |
| 0.52% | `_asyncio.cpython-314-x86_64-linux-gnu.so` | `TaskObj_traverse` | library |
| 0.52% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 0.48% | `python` | `dict_traverse` | gc |
| 0.48% | `_heapq.cpython-314-x86_64-linux-gnu.so` | `siftup` | library |
| 0.48% | `python` | `subtype_dealloc` | memory |
| 0.40% | `python` | `context_tp_dealloc` | memory |
| 0.39% | `python` | `gen_dealloc` | memory |
| 0.37% | `python` | `slot_tp_richcompare` | dynamic |
| 0.36% | `python` | `_Py_Dealloc` | memory |
| 0.35% | `python` | `PyObject_GenericGetAttr` | dynamic |
| 0.34% | `python` | `PyObject_IS_GC` | gc |
| 0.33% | `python` | `_PyThreadState_PopFrame` | interpreter |
| 0.32% | `python` | `_PyTuple_FromArray.part.0` | tuple |
| 0.32% | `python` | `PyDict_GetItemRef` | dict |
| 0.32% | `python` | `dict_dealloc` | memory |
| 0.31% | `python` | `PyObject_GC_Del` | gc |
| 0.30% | `python` | `insert_to_emptydict` | dict |
| 0.29% | `python` | `_PyObject_MakeTpCall` | dynamic |
| 0.29% | `python` | `_PyObject_GC_New` | gc |
| 0.28% | `python` | `PyType_GenericAlloc` | memory |
| 0.27% | `python` | `PyObject_Call` | dynamic |
| 0.27% | `python` | `_PyObject_GetMethod` | dynamic |
| 0.26% | `python` | `_PyThreadState_PushFrame` | interpreter |
| 0.26% | `python` | `_PyArg_UnpackKeywords` | calls |
| 0.26% | `python` | `_PyObject_Realloc` | memory |
| 0.25% | `[kernel.kallsyms]` | `clear_page_erms` | kernel |

## async_tree_io_tg

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 18.52% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 13.80% | `python` | `gc_collect_region.isra.0` | gc |
| 7.64% | `python` | `visit_add_to_container` | gc |
| 7.30% | `python` | `visit_decref` | gc |
| 6.77% | `python` | `visit_reachable` | gc |
| 2.79% | `[JIT]` | `jit` | jit |
| 2.68% | `python` | `_PyObject_Malloc` | memory |
| 1.67% | `python` | `_PyObject_Free` | memory |
| 1.35% | `python` | `_PyFrame_Traverse` | interpreter |
| 1.34% | `python` | `initialize_locals` | interpreter |
| 1.31% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.31% | `python` | `subtype_traverse` | gc |
| 1.17% | `python` | `_PyGC_Collect` | gc |
| 1.03% | `python` | `_PyType_LookupRef` | lookup |
| 1.00% | `python` | `_PyEval_Vector` | interpreter |
| 0.82% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.78% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.75% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.71% | `python` | `gen_traverse` | gc |
| 0.71% | `python` | `_Py_dict_lookup` | lookup |
| 0.57% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.54% | `python` | `PyObject_RichCompareBool` | dynamic |
| 0.54% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 0.53% | `_asyncio.cpython-314-x86_64-linux-gnu.so` | `TaskObj_traverse` | library |
| 0.52% | `python` | `tupledealloc` | memory |
| 0.50% | `python` | `set_traverse` | gc |
| 0.49% | `_heapq.cpython-314-x86_64-linux-gnu.so` | `siftup` | library |
| 0.48% | `python` | `subtype_dealloc` | memory |
| 0.42% | `python` | `slot_tp_richcompare` | dynamic |
| 0.39% | `python` | `gen_dealloc` | memory |
| 0.39% | `python` | `PyObject_GenericGetAttr` | dynamic |
| 0.36% | `python` | `PyObject_VisitManagedDict` | dynamic |
| 0.35% | `python` | `_Py_Dealloc` | memory |
| 0.32% | `python` | `_PyThreadState_PopFrame` | interpreter |
| 0.32% | `python` | `PyDict_GetItemRef` | dict |
| 0.31% | `python` | `PyObject_GC_Del` | gc |
| 0.30% | `python` | `insert_to_emptydict` | dict |
| 0.30% | `[kernel.kallsyms]` | `clear_page_erms` | kernel |
| 0.30% | `python` | `PyType_GenericAlloc` | memory |
| 0.30% | `python` | `_PyTuple_FromArray.part.0` | tuple |
| 0.28% | `python` | `_PyObject_GC_New` | gc |
| 0.28% | `[kernel.kallsyms]` | `native_irq_return_iret` | kernel |
| 0.27% | `python` | `_PyThreadState_PushFrame` | interpreter |
| 0.27% | `python` | `PyObject_Call` | dynamic |
| 0.26% | `python` | `_PyObject_MakeTpCall` | dynamic |
| 0.26% | `python` | `dict_traverse` | gc |
| 0.26% | `python` | `_PyObject_Calloc` | memory |
| 0.25% | `python` | `PyObject_IS_GC` | gc |
| 0.25% | `python` | `_PyObject_GetMethod` | dynamic |
| 0.25% | `python` | `PyObject_GetAttr` | dynamic |

## async_tree_memoization

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 21.76% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 9.81% | `python` | `gc_collect_region.isra.0` | gc |
| 5.11% | `python` | `visit_decref` | gc |
| 4.64% | `python` | `visit_reachable` | gc |
| 4.29% | `python` | `visit_add_to_container` | gc |
| 3.74% | `[JIT]` | `jit` | jit |
| 3.32% | `python` | `_PyObject_Malloc` | memory |
| 2.12% | `python` | `_PyObject_Free` | memory |
| 1.77% | `python` | `_PyType_LookupRef` | lookup |
| 1.52% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.51% | `python` | `_Py_dict_lookup` | lookup |
| 1.39% | `python` | `initialize_locals` | interpreter |
| 1.26% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 1.18% | `python` | `subtype_traverse` | gc |
| 1.05% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.87% | `python` | `context_tp_dealloc` | memory |
| 0.75% | `python` | `_PyGC_Collect` | gc |
| 0.67% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.67% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 0.64% | `python` | `tupledealloc` | memory |
| 0.63% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.62% | `python` | `_PyEval_Vector` | interpreter |
| 0.61% | `python` | `_PyObject_GetMethod` | dynamic |
| 0.56% | `python` | `subtype_dealloc` | memory |
| 0.54% | `_asyncio.cpython-314-x86_64-linux-gnu.so` | `TaskObj_traverse` | library |
| 0.52% | `python` | `PyDict_GetItemRef` | dict |
| 0.52% | `python` | `dict_traverse` | gc |
| 0.50% | `python` | `_Py_Dealloc` | memory |
| 0.49% | `python` | `_PyFrame_Traverse` | interpreter |
| 0.49% | `python` | `PyObject_GenericGetAttr` | dynamic |
| 0.47% | `python` | `gen_dealloc` | memory |
| 0.46% | `python` | `PyObject_RichCompareBool` | dynamic |
| 0.43% | `python` | `_PyObject_GC_New` | gc |
| 0.42% | `python` | `dict_dealloc` | memory |
| 0.40% | `python` | `PyObject_GC_Del` | gc |
| 0.39% | `python` | `_PyTuple_FromArray.part.0` | tuple |
| 0.38% | `python` | `insert_to_emptydict` | dict |
| 0.35% | `python` | `gen_traverse` | gc |
| 0.34% | `python` | `insertdict` | dict |
| 0.34% | `python` | `_PyArg_UnpackKeywords` | calls |
| 0.34% | `python` | `PyType_GenericAlloc` | memory |
| 0.34% | `python` | `list_dealloc` | memory |
| 0.33% | `python` | `_PyThreadState_PopFrame` | interpreter |
| 0.31% | `python` | `_PyObject_MakeTpCall` | dynamic |
| 0.29% | `python` | `_PyObject_Realloc` | memory |
| 0.29% | `python` | `PyObject_IS_GC` | gc |
| 0.27% | `python` | `list_traverse` | gc |
| 0.27% | `python` | `PyObject_GetAttr` | dynamic |

## async_tree_memoization_tg

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 21.42% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 9.95% | `python` | `gc_collect_region.isra.0` | gc |
| 5.54% | `python` | `visit_decref` | gc |
| 5.27% | `python` | `visit_add_to_container` | gc |
| 4.99% | `python` | `visit_reachable` | gc |
| 3.53% | `[JIT]` | `jit` | jit |
| 3.43% | `python` | `_PyObject_Malloc` | memory |
| 2.14% | `python` | `_PyObject_Free` | memory |
| 1.54% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.50% | `python` | `_PyType_LookupRef` | lookup |
| 1.47% | `python` | `initialize_locals` | interpreter |
| 1.36% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 1.33% | `python` | `_Py_dict_lookup` | lookup |
| 1.21% | `python` | `subtype_traverse` | gc |
| 0.98% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.75% | `python` | `_PyEval_Vector` | interpreter |
| 0.71% | `python` | `_PyGC_Collect` | gc |
| 0.71% | `python` | `_PyFrame_Traverse` | interpreter |
| 0.69% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 0.69% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.68% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.64% | `python` | `subtype_dealloc` | memory |
| 0.62% | `python` | `tupledealloc` | memory |
| 0.62% | `python` | `PyObject_GenericGetAttr` | dynamic |
| 0.51% | `python` | `PyObject_RichCompareBool` | dynamic |
| 0.51% | `python` | `_Py_Dealloc` | memory |
| 0.51% | `python` | `PyDict_GetItemRef` | dict |
| 0.49% | `_asyncio.cpython-314-x86_64-linux-gnu.so` | `TaskObj_traverse` | library |
| 0.48% | `python` | `_PyObject_GetMethod` | dynamic |
| 0.45% | `python` | `set_traverse` | gc |
| 0.42% | `python` | `gen_traverse` | gc |
| 0.39% | `python` | `_PyTuple_FromArray.part.0` | tuple |
| 0.38% | `python` | `_PyObject_MakeTpCall` | dynamic |
| 0.38% | `python` | `PyType_GenericAlloc` | memory |
| 0.38% | `python` | `PyObject_GC_Del` | gc |
| 0.37% | `python` | `_PyObject_GC_New` | gc |
| 0.36% | `python` | `context_tp_dealloc` | memory |
| 0.36% | `python` | `gen_dealloc` | memory |
| 0.35% | `python` | `_PyThreadState_PopFrame` | interpreter |
| 0.33% | `python` | `PyObject_GetAttr` | dynamic |
| 0.32% | `python` | `dict_traverse` | gc |
| 0.31% | `python` | `insert_to_emptydict` | dict |
| 0.30% | `python` | `PyObject_VisitManagedDict` | dynamic |
| 0.29% | `python` | `set_lookkey` | miscobj |
| 0.28% | `python` | `_PyArg_UnpackKeywords` | calls |
| 0.28% | `python` | `dict_dealloc` | memory |
| 0.26% | `python` | `PyUnicode_RichCompare` | str |
| 0.26% | `python` | `dict_setdefault_ref_lock_held` | dict |

## async_tree_tg

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 20.13% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 9.00% | `python` | `gc_collect_region.isra.0` | gc |
| 5.16% | `python` | `visit_add_to_container` | gc |
| 5.00% | `python` | `visit_decref` | gc |
| 4.78% | `python` | `visit_reachable` | gc |
| 3.91% | `[JIT]` | `jit` | jit |
| 3.83% | `python` | `_PyObject_Malloc` | memory |
| 2.36% | `python` | `_PyObject_Free` | memory |
| 1.51% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.50% | `python` | `initialize_locals` | interpreter |
| 1.38% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 1.30% | `python` | `_Py_dict_lookup` | lookup |
| 1.22% | `python` | `_PyType_LookupRef` | lookup |
| 1.04% | `python` | `subtype_traverse` | gc |
| 0.81% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.76% | `python` | `tupledealloc` | memory |
| 0.75% | `python` | `_PyFrame_Traverse` | interpreter |
| 0.74% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 0.68% | `python` | `subtype_dealloc` | memory |
| 0.65% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.65% | `python` | `_PyEval_Vector` | interpreter |
| 0.63% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.62% | `_asyncio.cpython-314-x86_64-linux-gnu.so` | `TaskObj_traverse` | library |
| 0.60% | `python` | `PyObject_GenericGetAttr` | dynamic |
| 0.58% | `python` | `_PyGC_Collect` | gc |
| 0.56% | `python` | `_Py_Dealloc` | memory |
| 0.52% | `python` | `PyObject_RichCompareBool` | dynamic |
| 0.52% | `python` | `set_traverse` | gc |
| 0.48% | `python` | `_PyTuple_FromArray.part.0` | tuple |
| 0.48% | `python` | `PyObject_GC_Del` | gc |
| 0.46% | `python` | `PyDict_GetItemRef` | dict |
| 0.44% | `python` | `_PyObject_GC_New` | gc |
| 0.43% | `python` | `PyType_GenericAlloc` | memory |
| 0.41% | `python` | `_PyObject_GetMethod` | dynamic |
| 0.40% | `python` | `dict_traverse` | gc |
| 0.39% | `python` | `_PyObject_MakeTpCall` | dynamic |
| 0.39% | `[kernel.kallsyms]` | `clear_page_erms` | kernel |
| 0.36% | `python` | `insert_to_emptydict` | dict |
| 0.35% | `python` | `gen_traverse` | gc |
| 0.35% | `[kernel.kallsyms]` | `native_irq_return_iret` | kernel |
| 0.35% | `python` | `dict_dealloc` | memory |
| 0.34% | `python` | `_PyArg_UnpackKeywords` | calls |
| 0.33% | `python` | `PyObject_GetAttr` | dynamic |
| 0.32% | `python` | `_PyThreadState_PopFrame` | interpreter |
| 0.32% | `python` | `insertdict` | dict |
| 0.32% | `python` | `dict_setdefault_ref_lock_held` | dict |
| 0.31% | `python` | `PyObject_VisitManagedDict` | dynamic |
| 0.30% | `python` | `gen_dealloc` | memory |
| 0.29% | `python` | `PyUnicode_RichCompare` | str |
| 0.28% | `python` | `_PyObject_Calloc` | memory |
| 0.27% | `[kernel.kallsyms]` | `sync_regs` | kernel |
| 0.26% | `[kernel.kallsyms]` | `rmqueue` | kernel |
| 0.26% | `python` | `_Py_NewReference` | memory |
| 0.26% | `python` | `_PyObject_GC_Link` | gc |

## asyncio_tcp

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 30.09% | `[kernel.kallsyms]` | `copy_user_enhanced_fast_string` | kernel |
| 17.59% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 8.39% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 7.82% | `[kernel.kallsyms]` | `clear_page_erms` | kernel |
| 2.07% | `[JIT]` | `jit` | jit |
| 0.73% | `python` | `_PyObject_Malloc` | memory |
| 0.61% | `[kernel.kallsyms]` | `tcp_sendmsg_locked` | kernel |
| 0.58% | `python` | `_PyType_LookupRef` | lookup |
| 0.56% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.53% | `[kernel.kallsyms]` | `native_irq_return_iret` | kernel |
| 0.49% | `python` | `_PyObject_Free` | memory |
| 0.46% | `python` | `_Py_dict_lookup` | lookup |
| 0.43% | `[kernel.kallsyms]` | `rmqueue` | kernel |
| 0.39% | `[kernel.kallsyms]` | `_raw_spin_lock` | kernel |
| 0.38% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 0.34% | `[kernel.kallsyms]` | `prep_new_page` | kernel |
| 0.32% | `python` | `gc_collect_region.isra.0` | gc |
| 0.30% | `[kernel.kallsyms]` | `sync_regs` | kernel |
| 0.29% | `[kernel.kallsyms]` | `__free_pages_ok` | kernel |
| 0.29% | `libc-2.31.so` | `pthread_attr_setschedparam` | libc |
| 0.25% | `python` | `PyObject_GetAttr` | dynamic |

## asyncio_tcp_ssl

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 38.80% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 26.41% | `libcrypto.so.1.1` | `CRYPTO_secure_actual_size` | libc |
| 11.10% | `[kernel.kallsyms]` | `copy_user_enhanced_fast_string` | kernel |
| 3.02% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 2.85% | `[kernel.kallsyms]` | `clear_page_erms` | kernel |
| 0.91% | `[JIT]` | `jit` | jit |
| 0.87% | `libssl.so.1.1` | `SSL_rstate_string` | library |
| 0.58% | `libc-2.31.so` | `pthread_attr_setschedparam` | libc |
| 0.48% | `libssl.so.1.1` | `DTLSv1_client_method` | library |
| 0.44% | `libcrypto.so.1.1` | `AES_unwrap_key` | libc |
| 0.30% | `python` | `_PyObject_Malloc` | memory |
| 0.28% | `libcrypto.so.1.1` | `CRYPTO_gcm128_release` | libc |
| 0.28% | `libpthread-2.31.so` | `__pthread_mutex_lock` | library |

## asyncio_websockets

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 64.32% | `libz.so.1.2.11` | `crc32_combine64` | library |
| 20.40% | `libz.so.1.2.11` | `inflateBackEnd` | library |
| 2.93% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.41% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 0.48% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.43% | `python` | `gc_collect_region.isra.0` | gc |
| 0.41% | `libz.so.1.2.11` | `inflateCodesUsed` | library |
| 0.29% | `python` | `_PyObject_Malloc` | memory |
| 0.26% | `python` | `_Py_dict_lookup` | lookup |

## bpe_tokeniser

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 16.50% | `[JIT]` | `jit` | jit |
| 5.32% | `python` | `tupledealloc` | memory |
| 5.29% | `python` | `_Py_dict_lookup` | lookup |
| 4.85% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 4.11% | `python` | `_PyObject_Free` | memory |
| 3.70% | `python` | `_PyObject_Malloc` | memory |
| 2.86% | `python` | `list_dealloc` | memory |
| 2.49% | `python` | `_PyTuple_FromArray.part.0` | tuple |
| 1.97% | `python` | `listiter_next` | list |
| 1.87% | `python` | `PyObject_GC_UnTrack` | gc |
| 1.82% | `python` | `PyTuple_New` | memory |
| 1.78% | `python` | `gc_collect_region.isra.0` | gc |
| 1.74% | `python` | `_Py_Dealloc` | memory |
| 1.69% | `python` | `PyObject_RichCompareBool` | dynamic |
| 1.62% | `python` | `PyList_New` | memory |
| 1.57% | `python` | `zip_next` | unknown |
| 1.52% | `python` | `_PyType_LookupRef` | lookup |
| 1.29% | `python` | `PySlice_AdjustIndices` | miscobj |
| 1.12% | `python` | `tuplerichcompare` | tuple |
| 1.06% | `python` | `tuplehash` | tuple |
| 1.01% | `python` | `visit_reachable` | gc |
| 0.99% | `python` | `visit_decref` | gc |
| 0.99% | `python` | `_PyObject_GC_New` | gc |
| 0.98% | `python` | `_PyObject_MakeTpCall` | dynamic |
| 0.94% | `python` | `list_slice_lock_held.isra.0` | list |
| 0.91% | `python` | `_PyLong_Add` | int |
| 0.91% | `python` | `PyObject_GC_Del` | gc |
| 0.90% | `python` | `PyObject_Hash` | dynamic |
| 0.89% | `python` | `_Py_NewReference` | memory |
| 0.88% | `python` | `list_subscript` | list |
| 0.88% | `python` | `_PyBuildSlice_ConsumeRefs` | miscobj |
| 0.87% | `python` | `insertdict` | dict |
| 0.87% | `python` | `list_traverse` | gc |
| 0.84% | `python` | `_PyLong_Subtract` | int |
| 0.77% | `python` | `_PyTuple_FromStackRefSteal` | tuple |
| 0.74% | `python` | `slice_dealloc` | memory |
| 0.72% | `python` | `slot_mp_subscript` | unknown |
| 0.67% | `python` | `PyType_GenericAlloc` | memory |
| 0.66% | `python` | `PyObject_GetItem` | dynamic |
| 0.65% | `python` | `PyObject_Size` | dynamic |
| 0.61% | `python` | `dict_subscript` | dict |
| 0.61% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 0.59% | `python` | `zip_new` | memory |
| 0.56% | `python` | `_PyObject_LookupSpecial` | dynamic |
| 0.51% | `python` | `list_iter` | list |
| 0.51% | `python` | `_PyObject_GC_Link` | gc |
| 0.49% | `python` | `method_vectorcall_O` | calls |
| 0.47% | `python` | `PySlice_Unpack` | miscobj |
| 0.47% | `python` | `PyObject_GetIter` | dynamic |
| 0.43% | `python` | `PyNumber_AsSsize_t` | dynamic |
| 0.42% | `python` | `vectorcall_method` | calls |
| 0.41% | `python` | `listiter_dealloc` | memory |
| 0.41% | `python` | `PyLong_FromSsize_t` | int |
| 0.41% | `python` | `_PyEval_SliceIndex` | interpreter |
| 0.41% | `python` | `wrapperdescr_call` | unknown |
| 0.38% | `python` | `PyObject_RichCompare` | dynamic |
| 0.38% | `python` | `visit_add_to_container` | gc |
| 0.38% | `python` | `PyArg_UnpackTuple` | calls |
| 0.36% | `python` | `initialize_locals` | interpreter |
| 0.35% | `python` | `dictiter_iternextkey` | dict |
| 0.34% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.34% | `python` | `_PyObject_Realloc` | memory |
| 0.33% | `python` | `PyObject_SetItem` | dynamic |
| 0.31% | `python` | `PyObject_Vectorcall` | dynamic |
| 0.31% | `python` | `dict_ass_sub` | dict |
| 0.31% | `python` | `_PyList_AppendTakeRefListResize` | list |
| 0.29% | `python` | `bytes_richcompare` | str |
| 0.29% | `python` | `type_call` | dynamic |
| 0.28% | `python` | `PyThreadState_Get` | unknown |
| 0.28% | `python` | `PyType_IsSubtype` | dynamic |
| 0.26% | `python` | `_Py_CheckFunctionResult` | calls |
| 0.26% | `python` | `wrap_objobjargproc` | unknown |
| 0.26% | `python` | `_PyFrame_ClearExceptCode` | interpreter |

## chaos

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 21.97% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 21.50% | `[JIT]` | `jit` | jit |
| 2.90% | `python` | `_PyObject_Malloc` | memory |
| 2.83% | `python` | `_PyObject_Free` | memory |
| 2.28% | `python` | `_PyLong_Subtract` | int |
| 1.93% | `python` | `PyType_IsSubtype` | dynamic |
| 1.92% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.52% | `python` | `_PyLong_Add` | int |
| 1.46% | `python` | `float_dealloc` | memory |
| 1.29% | `python` | `PyLong_AsDouble` | int |
| 1.20% | `python` | `_Py_Dealloc` | memory |
| 1.20% | `python` | `float_div` | float |
| 1.06% | `python` | `compute_range_length` | unknown |
| 1.05% | `python` | `float_richcompare` | float |
| 1.02% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.96% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.96% | `python` | `range_iter` | miscobj |
| 0.95% | `libm-2.31.so` | `f64xsubf128` | library |
| 0.90% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 0.86% | `python` | `float_sub` | float |
| 0.80% | `python` | `gc_collect_region.isra.0` | gc |
| 0.78% | `python` | `subtype_dealloc` | memory |
| 0.75% | `python` | `PyFloat_FromDouble` | float |
| 0.73% | `python` | `PyNumber_TrueDivide` | dynamic |
| 0.71% | `python` | `_Py_NewReference` | memory |
| 0.71% | `python` | `_PyType_NewManagedObject` | memory |
| 0.71% | `python` | `PyNumber_Subtract` | dynamic |
| 0.67% | `python` | `float_pow` | float |
| 0.64% | `python` | `_PyType_LookupRef` | lookup |
| 0.62% | `python` | `PyLong_FromLong` | int |
| 0.60% | `python` | `_Py_dict_lookup` | lookup |
| 0.53% | `python` | `PyObject_ClearManagedDict` | dynamic |
| 0.49% | `python` | `PyObject_RichCompare` | dynamic |
| 0.48% | `python` | `PyLong_AsLongAndOverflow` | int |
| 0.46% | `python` | `initialize_locals` | interpreter |
| 0.45% | `python` | `tupledealloc` | memory |
| 0.43% | `python` | `PyObject_GC_Del` | gc |
| 0.39% | `python` | `visit_decref` | gc |
| 0.38% | `python` | `range_vectorcall` | miscobj |
| 0.37% | `python` | `PyLong_AsLong` | int |
| 0.36% | `python` | `_PyThreadState_PopFrame` | interpreter |
| 0.35% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.35% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.32% | `python` | `r_object` | import |
| 0.31% | `python` | `visit_reachable` | gc |
| 0.29% | `python` | `PyNumber_Index` | dynamic |
| 0.28% | `python` | `_PyFloat_ExactDealloc` | memory |
| 0.26% | `python` | `_PyTuple_FromStackRefSteal` | tuple |
| 0.26% | `python` | `float_mul` | float |
| 0.26% | `python` | `list_dealloc` | memory |
| 0.25% | `python` | `_PyObject_GC_Link` | gc |
| 0.25% | `python` | `PyObject_ClearWeakRefs` | dynamic |

## comprehensions

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 29.53% | `[JIT]` | `jit` | jit |
| 7.30% | `python` | `_Py_dict_lookup` | lookup |
| 7.09% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 4.25% | `python` | `_PyObject_Malloc` | memory |
| 3.60% | `python` | `_PyObject_Free` | memory |
| 2.15% | `python` | `dict_get` | dict |
| 1.73% | `python` | `PyObject_RichCompareBool` | dynamic |
| 1.72% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 1.55% | `python` | `_PyObject_Realloc` | memory |
| 1.30% | `python` | `PyDict_GetItemRef` | dict |
| 1.20% | `python` | `long_richcompare` | int |
| 1.13% | `python` | `insertdict` | dict |
| 1.06% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 0.99% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 0.98% | `python` | `PyFunction_NewWithQualName` | memory |
| 0.96% | `python` | `PyObject_GC_Del` | gc |
| 0.93% | `python` | `_PyType_LookupRef` | lookup |
| 0.90% | `python` | `list_dealloc` | memory |
| 0.83% | `python` | `tupledealloc` | memory |
| 0.83% | `python` | `gc_collect_region.isra.0` | gc |
| 0.83% | `python` | `PyObject_Hash` | dynamic |
| 0.80% | `python` | `unsafe_tuple_compare` | unknown |
| 0.79% | `python` | `long_hash` | int |
| 0.79% | `python` | `_PyObject_GC_New` | gc |
| 0.79% | `python` | `_PyList_AppendTakeRefListResize` | list |
| 0.74% | `python` | `_Py_Dealloc` | memory |
| 0.72% | `python` | `gen_dealloc` | memory |
| 0.67% | `python` | `PyObject_IsTrue` | dynamic |
| 0.65% | `python` | `_PyTuple_FromStackRefSteal` | tuple |
| 0.65% | `python` | `list_sort_impl` | list |
| 0.57% | `python` | `func_dealloc` | memory |
| 0.56% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.44% | `python` | `list_iter` | list |
| 0.43% | `python` | `gen_iternext` | miscobj |
| 0.42% | `python` | `func_clear` | unknown |
| 0.42% | `python` | `listiter_dealloc` | memory |
| 0.40% | `python` | `visit_decref` | gc |
| 0.39% | `python` | `PyObject_GetIter` | dynamic |
| 0.38% | `python` | `PyObject_RichCompare` | dynamic |
| 0.38% | `python` | `_PyObject_GC_Link` | gc |
| 0.37% | `python` | `_Py_type_getattro` | lookup |
| 0.36% | `python` | `PyList_New` | memory |
| 0.34% | `python` | `dict_dealloc` | memory |
| 0.34% | `python` | `_PyObject_GC_NewVar` | gc |
| 0.33% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.32% | `python` | `builtin_any` | unknown |
| 0.31% | `python` | `_Py_NewReference` | memory |
| 0.31% | `python` | `visit_reachable` | gc |
| 0.30% | `python` | `r_object` | import |
| 0.28% | `python` | `update_one_slot` | lookup |
| 0.28% | `python` | `make_gen` | miscobj |
| 0.27% | `python` | `PyObject_GetAttr` | dynamic |
| 0.27% | `python` | `_PyThreadState_PopFrame` | interpreter |
| 0.27% | `python` | `_PyFrame_ClearLocals` | unknown |
| 0.26% | `python` | `_PyDict_SetItem_Take2` | dict |
| 0.26% | `python` | `tuplesubscript` | tuple |

## concurrent_imap

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 18.48% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 4.71% | `[JIT]` | `jit` | jit |
| 3.06% | `python` | `_PyObject_Free` | memory |
| 1.94% | `python` | `_PyObject_Malloc` | memory |
| 1.72% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.52% | `[kernel.kallsyms]` | `memset_erms` | kernel |
| 1.50% | `[kernel.kallsyms]` | `perf_event_alloc` | kernel |
| 1.34% | `python` | `_PyType_LookupRef` | lookup |
| 1.23% | `python` | `tupledealloc` | memory |
| 1.03% | `python` | `initialize_locals` | interpreter |
| 0.95% | `python` | `PyObject_ClearManagedDict` | dynamic |
| 0.92% | `python` | `subtype_dealloc` | memory |
| 0.90% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.89% | `python` | `_Py_Dealloc` | memory |
| 0.88% | `[kernel.kallsyms]` | `clear_page_erms` | kernel |
| 0.87% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 0.85% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.73% | `python` | `_Py_dict_lookup` | lookup |
| 0.70% | `libc-2.31.so` | `pthread_attr_setschedparam` | libc |
| 0.68% | `python` | `dict_dealloc` | memory |
| 0.63% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.60% | `python` | `PyObject_GC_Del` | gc |
| 0.60% | `python` | `PyObject_GetAttr` | dynamic |
| 0.59% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.58% | `python` | `PyObject_GenericGetAttr` | dynamic |
| 0.54% | `[kernel.kallsyms]` | `mutex_unlock` | kernel |
| 0.48% | `[kernel.kallsyms]` | `copy_page` | kernel |
| 0.47% | `[kernel.kallsyms]` | `mutex_lock` | kernel |
| 0.47% | `[kernel.kallsyms]` | `inherit_event.isra.0` | kernel |
| 0.45% | `python` | `PyObject_Vectorcall` | dynamic |
| 0.44% | `[vdso]` | `__vdso_clock_gettime` | unknown |
| 0.41% | `python` | `_PyObject_LookupSpecialMethod` | dynamic |
| 0.41% | `[kernel.kallsyms]` | `_raw_spin_lock_irqsave` | kernel |
| 0.41% | `python` | `gc_collect_region.isra.0` | gc |
| 0.40% | `[kernel.kallsyms]` | `_raw_spin_lock` | kernel |
| 0.40% | `[kernel.kallsyms]` | `native_flush_tlb_one_user` | kernel |
| 0.39% | `libpthread-2.31.so` | `__pthread_mutex_lock` | library |
| 0.38% | `[kernel.kallsyms]` | `find_vma` | kernel |
| 0.38% | `python` | `_PyTuple_FromArray.part.0` | tuple |
| 0.37% | `[kernel.kallsyms]` | `page_counter_cancel` | kernel |
| 0.37% | `python` | `PyType_GenericAlloc` | memory |
| 0.36% | `libpthread-2.31.so` | `pthread_mutex_unlock` | library |
| 0.35% | `libc-2.31.so` | `free` | libc |
| 0.35% | `python` | `list_dealloc` | memory |
| 0.34% | `[kernel.kallsyms]` | `nmi_restore` | kernel |
| 0.34% | `[kernel.kallsyms]` | `__vma_adjust` | kernel |
| 0.34% | `[kernel.kallsyms]` | `kfree` | kernel |
| 0.33% | `python` | `_PyTuple_FromStackRefSteal` | tuple |
| 0.33% | `[kernel.kallsyms]` | `syscall_return_via_sysret` | kernel |
| 0.32% | `[kernel.kallsyms]` | `memcg_kmem_get_cache` | kernel |
| 0.31% | `[kernel.kallsyms]` | `kmem_cache_alloc_trace` | kernel |
| 0.31% | `[kernel.kallsyms]` | `zap_pte_range.isra.0` | kernel |
| 0.30% | `[kernel.kallsyms]` | `native_irq_return_iret` | kernel |
| 0.29% | `[kernel.kallsyms]` | `psi_task_change` | kernel |
| 0.29% | `[kernel.kallsyms]` | `do_sys_poll` | kernel |
| 0.28% | `python` | `PyObject_ClearWeakRefs` | dynamic |
| 0.26% | `[kernel.kallsyms]` | `account_kernel_stack` | kernel |
| 0.26% | `[kernel.kallsyms]` | `__fget_light` | kernel |
| 0.26% | `[kernel.kallsyms]` | `native_sched_clock` | kernel |
| 0.25% | `python` | `long_dealloc` | memory |

## coroutines

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 44.12% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 6.36% | `python` | `gen_dealloc` | memory |
| 5.33% | `python` | `_PyObject_Malloc` | memory |
| 4.43% | `python` | `_PyObject_Free` | memory |
| 2.80% | `python` | `_PyObject_GC_NewVar` | gc |
| 2.50% | `python` | `make_gen` | miscobj |
| 2.41% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 2.23% | `python` | `_PyLong_Subtract` | int |
| 1.92% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.56% | `python` | `PyObject_CallFinalizerFromDealloc` | memory |
| 1.56% | `python` | `_PyLong_Add` | int |
| 1.43% | `python` | `PyObject_GC_Del` | gc |
| 1.19% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 1.09% | `python` | `_Py_MakeCoro` | unknown |
| 0.96% | `python` | `gc_collect_region.isra.0` | gc |
| 0.92% | `python` | `_PyObject_GC_Link` | gc |
| 0.78% | `python` | `_PyThreadState_PopFrame` | interpreter |
| 0.74% | `python` | `_PyCoro_GetAwaitableIter` | unknown |
| 0.67% | `python` | `_Py_dict_lookup` | lookup |
| 0.61% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 0.57% | `python` | `visit_decref` | gc |
| 0.52% | `[JIT]` | `jit` | jit |
| 0.44% | `python` | `r_object` | import |
| 0.41% | `python` | `_Py_NewReference` | memory |
| 0.40% | `python` | `visit_reachable` | gc |
| 0.38% | `python` | `_PyGen_Finalize` | miscobj |
| 0.30% | `python` | `update_one_slot` | lookup |
| 0.28% | `python` | `_PyCode_Quicken` | interpreter |
| 0.28% | `python` | `_Py_hashtable_get_entry_generic` | lookup |
| 0.27% | `python` | `siphash13` | str |

## coverage

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 14.25% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 6.79% | `python` | `call_instrumentation_vector.part.0` | interpreter |
| 6.01% | `tracer.cpython-314-x86_64-linux-gnu.so` | `CTracer_trace` | library |
| 5.66% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 3.64% | `python` | `_Py_dict_lookup` | lookup |
| 3.33% | `python` | `_Py_call_instrumentation_line` | interpreter |
| 3.31% | `python` | `_PyObject_Malloc` | memory |
| 3.10% | `python` | `_PyObject_Free` | memory |
| 2.74% | `python` | `siphash13` | str |
| 1.87% | `python` | `PyDict_GetItem` | dict |
| 1.56% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.40% | `python` | `gc_collect_region.isra.0` | gc |
| 1.31% | `python` | `_Py_hashtable_get_entry_generic` | lookup |
| 1.30% | `python` | `set_add_entry` | miscobj |
| 1.11% | `python` | `PyLong_FromLong` | int |
| 0.96% | `python` | `_PyType_LookupRef` | lookup |
| 0.92% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 0.92% | `python` | `PyObject_GenericSetAttr` | dynamic |
| 0.85% | `python` | `dict_setdefault_ref_lock_held` | dict |
| 0.84% | `python` | `PySet_Add` | miscobj |
| 0.81% | `[JIT]` | `jit` | jit |
| 0.78% | `python` | `visit_decref` | gc |
| 0.75% | `python` | `_PyObject_GC_NewVar` | gc |
| 0.75% | `python` | `PyObject_GC_Del` | gc |
| 0.70% | `python` | `ascii_decode` | str |
| 0.66% | `python` | `intern_common.part.0` | str |
| 0.64% | `python` | `unicode_decode_utf8.part.0` | str |
| 0.64% | `python` | `frame_dealloc` | memory |
| 0.61% | `python` | `_PyCode_GetCode` | interpreter |
| 0.61% | `python` | `visit_reachable` | gc |
| 0.60% | `python` | `PyUnicode_New.part.0` | memory |
| 0.55% | `python` | `sys_trace_return` | library |
| 0.54% | `python` | `_PyDict_LoadGlobal` | dict |
| 0.53% | `python` | `sys_trace_start` | library |
| 0.52% | `python` | `_Py_Dealloc` | memory |
| 0.51% | `python` | `r_object` | import |
| 0.49% | `python` | `_PyLong_Subtract` | int |
| 0.47% | `python` | `PyEval_GetFrame` | interpreter |
| 0.44% | `python` | `PyObject_SetAttr` | dynamic |
| 0.42% | `python` | `PyObject_Hash` | dynamic |
| 0.42% | `python` | `PyFrame_GetCode` | exceptions |
| 0.41% | `tracer.cpython-314-x86_64-linux-gnu.so` | `CTracer_set_pdata_stack` | library |
| 0.41% | `python` | `_Py_call_instrumentation_arg` | unknown |
| 0.40% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.40% | `python` | `_PyLong_Add` | int |
| 0.39% | `python` | `unicode_dealloc` | memory |
| 0.39% | `python` | `update_one_slot` | lookup |
| 0.36% | `python` | `_Py_CheckFunctionResult` | calls |
| 0.36% | `python` | `PyObject_SetAttrString` | dynamic |
| 0.36% | `python` | `PyUnicode_InternFromString` | str |
| 0.35% | `python` | `find_name_in_mro` | lookup |
| 0.34% | `python` | `long_hash` | int |
| 0.31% | `python` | `tupledealloc` | memory |
| 0.30% | `python` | `_PyType_GetDict` | dynamic |
| 0.30% | `python` | `_PyCode_Quicken` | interpreter |
| 0.29% | `python` | `PyFrame_GetLineNumber` | exceptions |

## crypto_pyaes

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 24.95% | `[JIT]` | `jit` | jit |
| 10.45% | `python` | `_PyObject_Free` | memory |
| 8.10% | `python` | `long_bitwise` | int |
| 7.81% | `python` | `_PyObject_Malloc` | memory |
| 3.80% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 3.75% | `python` | `long_rshift1` | int |
| 3.02% | `python` | `l_mod` | int |
| 1.89% | `python` | `long_and` | int |
| 1.68% | `python` | `_Py_Dealloc` | memory |
| 1.67% | `python` | `long_rshift` | int |
| 1.33% | `python` | `long_dealloc` | memory |
| 1.32% | `python` | `PyNumber_And` | dynamic |
| 1.21% | `python` | `long_xor` | int |
| 1.20% | `python` | `PyNumber_Xor` | dynamic |
| 1.14% | `python` | `PyLong_FromLong` | int |
| 1.11% | `python` | `_PyLong_Add` | int |
| 1.02% | `python` | `_Py_dict_lookup` | lookup |
| 0.89% | `python` | `PyNumber_Remainder` | dynamic |
| 0.85% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.84% | `python` | `PyNumber_Rshift` | dynamic |
| 0.73% | `python` | `_Py_NewReference` | memory |
| 0.72% | `python` | `gc_collect_region.isra.0` | gc |
| 0.67% | `python` | `long_mod` | int |
| 0.66% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 0.64% | `python` | `compute_range_length` | unknown |
| 0.60% | `python` | `PyLong_AsSsize_t` | int |
| 0.59% | `python` | `range_iter` | miscobj |
| 0.55% | `python` | `PyObject_Malloc` | dynamic |
| 0.54% | `python` | `list_dealloc` | memory |
| 0.45% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 0.36% | `python` | `PyObject_Free` | dynamic |
| 0.36% | `python` | `visit_decref` | gc |
| 0.33% | `python` | `PyList_New` | memory |
| 0.29% | `python` | `r_object` | import |
| 0.26% | `python` | `visit_reachable` | gc |
| 0.25% | `python` | `PyLong_AsLongAndOverflow` | int |

## dask

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 21.36% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 3.84% | `python` | `gc_collect_region.isra.0` | gc |
| 3.30% | `[JIT]` | `jit` | jit |
| 3.25% | `python` | `_PyObject_Malloc` | memory |
| 2.55% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 2.45% | `python` | `_PyObject_Free` | memory |
| 2.36% | `python` | `visit_decref` | gc |
| 1.97% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.75% | `python` | `visit_reachable` | gc |
| 1.71% | `python` | `_Py_dict_lookup` | lookup |
| 1.42% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.38% | `python` | `visit_add_to_container` | gc |
| 1.29% | `python` | `tupledealloc` | memory |
| 1.10% | `python` | `initialize_locals` | interpreter |
| 1.07% | `python` | `_PyType_LookupRef` | lookup |
| 0.92% | `python` | `dict_dealloc` | memory |
| 0.91% | `python` | `PyBytes_Repr` | str |
| 0.72% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.67% | `python` | `_Py_Dealloc` | memory |
| 0.56% | `python` | `insertdict` | dict |
| 0.55% | `libc-2.31.so` | `pthread_attr_setschedparam` | libc |
| 0.50% | `python` | `PyDict_GetItemRef` | dict |
| 0.49% | `python` | `siphash13` | str |
| 0.44% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.42% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.42% | `python` | `PyObject_RichCompareBool` | dynamic |
| 0.42% | `python` | `PyObject_GC_Del` | gc |
| 0.41% | `python` | `_PyTuple_FromArray.part.0` | tuple |
| 0.40% | `python` | `set_traverse` | gc |
| 0.39% | `python` | `_PyTuple_FromStackRefSteal` | tuple |
| 0.39% | `python` | `PyObject_IS_GC` | gc |
| 0.38% | `python` | `dict_traverse` | gc |
| 0.38% | `python` | `_PyObject_GC_New` | gc |
| 0.34% | `python` | `list_dealloc` | memory |
| 0.34% | `python` | `_PyDict_FromItems` | dict |
| 0.33% | `python` | `dict_merge` | dict |
| 0.32% | `_cmsgpack.cpython-314-x86_64-linux-gnu.so` | `__pyx_f_7msgpack_9_cmsgpack_6Packer__pack` | library |
| 0.31% | `python` | `PyType_GenericAlloc` | memory |
| 0.31% | `libcrypto.so.1.1` | `MD4` | libc |
| 0.30% | `python` | `insert_to_emptydict` | dict |
| 0.30% | `python` | `tupletraverse` | tuple |
| 0.30% | `python` | `r_object` | import |
| 0.30% | `python` | `_PyPegen_is_memoized` | interpreter |
| 0.29% | `python` | `_Py_hashtable_get_entry_generic` | lookup |
| 0.28% | `python` | `PyType_IsSubtype` | dynamic |
| 0.28% | `python` | `setiter_iternext` | miscobj |
| 0.27% | `python` | `PyObject_Vectorcall` | dynamic |
| 0.27% | `python` | `_PyObject_Calloc` | memory |
| 0.26% | `python` | `_Py_NewReference` | memory |
| 0.25% | `python` | `_PyObject_GetMethod` | dynamic |

## deepcopy

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 17.33% | `[JIT]` | `jit` | jit |
| 15.27% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 4.80% | `python` | `_Py_dict_lookup` | lookup |
| 4.53% | `python` | `_PyObject_Malloc` | memory |
| 4.25% | `python` | `_PyObject_Free` | memory |
| 4.06% | `python` | `initialize_locals` | interpreter |
| 2.90% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 2.71% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 1.75% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 1.33% | `python` | `set_lookkey` | miscobj |
| 1.21% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.09% | `python` | `_PyType_LookupRef` | lookup |
| 1.05% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 0.94% | `python` | `insertdict` | dict |
| 0.89% | `python` | `PyLong_FromVoidPtr` | int |
| 0.83% | `python` | `_PyDict_LoadGlobal` | dict |
| 0.81% | `python` | `tupledealloc` | memory |
| 0.79% | `python` | `dict_get` | dict |
| 0.78% | `python` | `_Py_Dealloc` | memory |
| 0.73% | `python` | `_PyObject_Realloc` | memory |
| 0.65% | `python` | `insert_to_emptydict` | dict |
| 0.64% | `python` | `list_append` | list |
| 0.64% | `python` | `PyObject_Hash` | dynamic |
| 0.63% | `python` | `gc_collect_region.isra.0` | gc |
| 0.60% | `python` | `PyObject_GC_Del` | gc |
| 0.60% | `python` | `long_hash` | int |
| 0.59% | `python` | `sys_audit_tstate` | unknown |
| 0.59% | `python` | `long_richcompare` | int |
| 0.59% | `python` | `PyObject_RichCompareBool` | dynamic |
| 0.58% | `python` | `dict_dealloc` | memory |
| 0.58% | `python` | `_PyThreadState_PushFrame` | interpreter |
| 0.55% | `python` | `_PyObject_GC_New` | gc |
| 0.54% | `python` | `list_dealloc` | memory |
| 0.53% | `python` | `_PySet_Contains` | miscobj |
| 0.52% | `python` | `dictiter_iternextitem` | dict |
| 0.51% | `python` | `PyDict_GetItemRef` | dict |
| 0.49% | `python` | `_PyObject_GenericGetAttrWithDict` | dynamic |
| 0.48% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.46% | `python` | `PySys_Audit` | unknown |
| 0.43% | `python` | `_PyThreadState_PopFrame` | interpreter |
| 0.39% | `python` | `_PyObject_Calloc` | memory |
| 0.39% | `python` | `_Py_NewReference` | memory |
| 0.38% | `python` | `PyObject_GetAttr` | dynamic |
| 0.35% | `python` | `_PyTuple_FromArray.part.0` | tuple |
| 0.34% | `libc-2.31.so` | `pthread_attr_setschedparam` | libc |
| 0.31% | `python` | `PyType_GenericAlloc` | memory |
| 0.30% | `python` | `visit_decref` | gc |
| 0.30% | `python` | `PyObject_GenericGetAttr` | dynamic |
| 0.29% | `python` | `_PyDict_SetItem_Take2` | dict |
| 0.27% | `python` | `r_object` | import |
| 0.27% | `python` | `dict_merge` | dict |
| 0.26% | `python` | `PyList_New` | memory |
| 0.25% | `python` | `_PyObject_GC_Link` | gc |

## deltablue

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 47.49% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 10.58% | `[JIT]` | `jit` | jit |
| 3.44% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 2.20% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 2.18% | `python` | `_PyObject_Malloc` | memory |
| 2.13% | `python` | `_PyType_LookupRef` | lookup |
| 2.07% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 2.04% | `python` | `gc_collect_region.isra.0` | gc |
| 1.89% | `python` | `_PyObject_GetMethod` | dynamic |
| 1.72% | `python` | `_PyObject_Free` | memory |
| 1.01% | `python` | `_PyThreadState_PopFrame` | interpreter |
| 0.81% | `python` | `visit_decref` | gc |
| 0.81% | `python` | `_PyObject_TryGetInstanceAttribute` | dynamic |
| 0.77% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 0.57% | `python` | `_Py_dict_lookup` | lookup |
| 0.41% | `python` | `visit_reachable` | gc |
| 0.36% | `python` | `_Py_type_getattro` | lookup |
| 0.33% | `python` | `PyDict_GetItemRef` | dict |
| 0.32% | `python` | `_PyObject_GC_New` | gc |
| 0.30% | `python` | `_PyType_GetDict` | dynamic |
| 0.30% | `python` | `subtype_dealloc` | memory |
| 0.29% | `python` | `PyObject_GC_Del` | gc |
| 0.27% | `python` | `PyType_IsSubtype` | dynamic |
| 0.25% | `libc-2.31.so` | `pthread_attr_setschedparam` | libc |
| 0.25% | `python` | `_PyLong_Add` | int |

## django_template

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 24.58% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 8.82% | `[JIT]` | `jit` | jit |
| 3.45% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 3.21% | `python` | `_PyObject_Malloc` | memory |
| 2.90% | `python` | `_PyObject_Free` | memory |
| 2.30% | `python` | `_PyType_LookupRef` | lookup |
| 1.92% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.86% | `python` | `_Py_dict_lookup` | lookup |
| 1.72% | `python` | `gc_collect_region.isra.0` | gc |
| 1.28% | `python` | `_PyObject_GenericGetAttrWithDict` | dynamic |
| 1.27% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.23% | `python` | `initialize_locals` | interpreter |
| 1.01% | `python` | `replace` | str |
| 0.91% | `python` | `tupledealloc` | memory |
| 0.86% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.86% | `python` | `visit_decref` | gc |
| 0.79% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.74% | `python` | `insertdict` | dict |
| 0.68% | `python` | `PyObject_GC_Del` | gc |
| 0.68% | `python` | `PyType_IsSubtype` | dynamic |
| 0.60% | `python` | `visit_reachable` | gc |
| 0.58% | `python` | `_PyObject_GC_New` | gc |
| 0.57% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.57% | `python` | `_Py_Dealloc` | memory |
| 0.54% | `python` | `dict_dealloc` | memory |
| 0.54% | `python` | `r_object` | import |
| 0.51% | `python` | `PyObject_GetOptionalAttr` | dynamic |
| 0.50% | `python` | `update_one_slot` | lookup |
| 0.47% | `python` | `list_dealloc` | memory |
| 0.44% | `python` | `_PyObject_GetMethod` | dynamic |
| 0.44% | `python` | `PyDict_GetItemRef` | dict |
| 0.43% | `libc-2.31.so` | `pthread_attr_setschedparam` | libc |
| 0.40% | `python` | `find_name_in_mro` | lookup |
| 0.40% | `python` | `_PyTuple_FromArray.part.0` | tuple |
| 0.39% | `python` | `_PyThreadState_PopFrame` | interpreter |
| 0.39% | `python` | `PyType_GenericAlloc` | memory |
| 0.38% | `python` | `_PyObject_GC_Link` | gc |
| 0.36% | `python` | `long_to_decimal_string_internal` | int |
| 0.35% | `python` | `_Py_hashtable_get_entry_generic` | lookup |
| 0.35% | `python` | `PyObject_GetIter` | dynamic |
| 0.33% | `python` | `object_isinstance` | dynamic |
| 0.33% | `libz.so.1.2.11` | `inflateBackEnd` | library |
| 0.32% | `python` | `_PyCode_Quicken` | interpreter |
| 0.32% | `python` | `siphash13` | str |
| 0.31% | `python` | `_Py_NewReference` | memory |
| 0.31% | `python` | `PyFunction_NewWithQualName` | memory |
| 0.30% | `python` | `_PyType_GetDict` | dynamic |
| 0.29% | `python` | `_PyObject_Calloc` | memory |
| 0.27% | `python` | `_PyPegen_is_memoized` | interpreter |
| 0.27% | `python` | `_PyTuple_FromStackRefSteal` | tuple |
| 0.26% | `python` | `unicode_replace` | str |
| 0.26% | `python` | `_PyThreadState_PushFrame` | interpreter |
| 0.26% | `python` | `_PyUnicode_FromUCS1.part.0` | str |

## docutils

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 16.00% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 9.10% | `[JIT]` | `jit` | jit |
| 6.11% | `python` | `sre_ucs1_match` | library |
| 5.72% | `python` | `gc_collect_region.isra.0` | gc |
| 3.88% | `python` | `_PyObject_Malloc` | memory |
| 3.03% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 3.03% | `python` | `_PyType_LookupRef` | lookup |
| 2.96% | `python` | `_PyObject_Free` | memory |
| 1.93% | `python` | `_Py_dict_lookup` | lookup |
| 1.87% | `python` | `visit_add_to_container` | gc |
| 1.76% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.70% | `python` | `visit_decref` | gc |
| 1.70% | `python` | `sre_ucs2_charset.isra.0` | library |
| 1.33% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.18% | `python` | `list_dealloc` | memory |
| 1.18% | `python` | `PyObject_GenericGetAttr` | dynamic |
| 0.89% | `python` | `dict_traverse` | gc |
| 0.83% | `python` | `visit_reachable` | gc |
| 0.80% | `python` | `PyObject_GetAttr` | dynamic |
| 0.77% | `python` | `initialize_locals` | interpreter |
| 0.76% | `python` | `_PyObject_TryGetInstanceAttribute` | dynamic |
| 0.69% | `python` | `tupledealloc` | memory |
| 0.67% | `python` | `_PyObject_GetMethod` | dynamic |
| 0.61% | `libc-2.31.so` | `pthread_attr_setschedparam` | libc |
| 0.60% | `python` | `_Py_Dealloc` | memory |
| 0.58% | `python` | `PyType_IsSubtype` | dynamic |
| 0.57% | `python` | `list_traverse` | gc |
| 0.55% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.52% | `python` | `list_slice_lock_held.isra.0` | list |
| 0.50% | `python` | `dict_dealloc` | memory |
| 0.46% | `python` | `PyObject_GC_Del` | gc |
| 0.44% | `python` | `_PyUnicode_JoinArray.part.0` | str |
| 0.43% | `python` | `_PyObject_GC_New` | gc |
| 0.43% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.42% | `python` | `PyDict_GetItemRef` | dict |
| 0.41% | `python` | `PyList_New` | memory |
| 0.40% | `python` | `PyUnicode_Format` | str |
| 0.40% | `python` | `sre_ucs1_count` | library |
| 0.39% | `python` | `_PyTuple_FromStackRefSteal` | tuple |
| 0.38% | `python` | `_PyObject_GenericGetAttrWithDict` | dynamic |
| 0.36% | `python` | `find_name_in_mro` | lookup |
| 0.35% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.35% | `python` | `_copy_characters.part.0.constprop.0` | str |
| 0.35% | `python` | `PyType_GenericAlloc` | memory |
| 0.34% | `python` | `list_extend_lock_held` | list |
| 0.31% | `python` | `insertdict` | dict |
| 0.30% | `python` | `_PyTuple_FromArray.part.0` | tuple |
| 0.30% | `python` | `_PyObject_Realloc` | memory |
| 0.30% | `python` | `split` | str |
| 0.28% | `python` | `_PyGC_Collect` | gc |
| 0.28% | `python` | `PyObject_VisitManagedDict` | dynamic |
| 0.28% | `python` | `subtype_traverse` | gc |
| 0.28% | `python` | `sre_search` | library |
| 0.26% | `python` | `listiter_next` | list |
| 0.25% | `python` | `PyObject_SetAttr` | dynamic |

## fannkuch

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 25.18% | `[JIT]` | `jit` | jit |
| 10.10% | `python` | `PySlice_AdjustIndices` | miscobj |
| 5.88% | `python` | `list_ass_slice_lock_held` | list |
| 5.36% | `python` | `list_subscript` | list |
| 4.05% | `python` | `_PyObject_Free` | memory |
| 3.81% | `python` | `slice_dealloc` | memory |
| 3.61% | `python` | `_PyObject_Malloc` | memory |
| 3.56% | `python` | `_PyEval_SliceIndex` | interpreter |
| 3.10% | `python` | `list_dealloc` | memory |
| 2.73% | `python` | `_PyBuildSlice_ConsumeRefs` | miscobj |
| 2.60% | `python` | `PyNumber_AsSsize_t` | dynamic |
| 2.58% | `python` | `_PyLong_Add` | int |
| 2.50% | `python` | `PySlice_New` | memory |
| 2.42% | `python` | `list_ass_subscript` | list |
| 2.23% | `python` | `PySlice_Unpack` | miscobj |
| 2.11% | `python` | `PyList_New` | memory |
| 1.60% | `python` | `_Py_Dealloc` | memory |
| 1.53% | `python` | `PyLong_AsSsize_t` | int |
| 1.20% | `python` | `list_insert` | list |
| 1.19% | `python` | `PySequence_Fast` | dynamic |
| 1.00% | `python` | `PyObject_GetItem` | dynamic |
| 0.86% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 0.82% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 0.74% | `python` | `_Py_NewReference` | memory |
| 0.69% | `python` | `_PyLong_Subtract` | int |
| 0.65% | `python` | `list_pop` | list |
| 0.65% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.63% | `python` | `PyObject_SetItem` | dynamic |
| 0.44% | `python` | `list_slice_lock_held.isra.0` | list |
| 0.37% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.29% | `python` | `_PyNumber_Index` | dynamic |
| 0.27% | `python` | `gc_collect_region.isra.0` | gc |

## float

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 23.73% | `[JIT]` | `jit` | jit |
| 9.89% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 5.08% | `libm-2.31.so` | `f64xsubf128` | library |
| 4.75% | `python` | `_PyObject_Malloc` | memory |
| 2.73% | `python` | `_PyObject_Free` | memory |
| 2.27% | `python` | `gc_collect_region.isra.0` | gc |
| 1.93% | `python` | `subtype_traverse` | gc |
| 1.90% | `python` | `_Py_Dealloc` | memory |
| 1.85% | `python` | `visit_decref` | gc |
| 1.81% | `python` | `subtype_dealloc` | memory |
| 1.66% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.66% | `python` | `float_div` | float |
| 1.57% | `python` | `PyFloat_FromDouble` | float |
| 1.54% | `python` | `visit_reachable` | gc |
| 1.27% | `python` | `float_dealloc` | memory |
| 1.26% | `python` | `visit_add_to_container` | gc |
| 1.13% | `python` | `PyType_IsSubtype` | dynamic |
| 1.08% | `python` | `_Py_NewReference` | memory |
| 0.91% | `python` | `tupledealloc` | memory |
| 0.85% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.82% | `python` | `PyType_GenericAlloc` | memory |
| 0.80% | `python` | `PyNumber_InPlaceTrueDivide` | dynamic |
| 0.80% | `python` | `initialize_locals` | interpreter |
| 0.75% | `python` | `_PyType_LookupRef` | lookup |
| 0.72% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.71% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.67% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 0.67% | `python` | `_PyObject_MakeTpCall` | dynamic |
| 0.64% | `python` | `long_float` | int |
| 0.56% | `python` | `float_mul` | float |
| 0.55% | `python` | `_PyTuple_FromArray.part.0` | tuple |
| 0.55% | `python` | `PyFloat_AsDouble.part.0` | float |
| 0.54% | `python` | `_PyObject_Call_Prepend` | dynamic |
| 0.51% | `python` | `PyLong_AsDouble` | int |
| 0.49% | `python` | `list_dealloc` | memory |
| 0.45% | `python` | `_Py_dict_lookup` | lookup |
| 0.45% | `python` | `_PyEval_Vector` | interpreter |
| 0.42% | `python` | `list_slice_lock_held.isra.0` | list |
| 0.41% | `[kernel.kallsyms]` | `native_irq_return_iret` | kernel |
| 0.40% | `python` | `type_call` | dynamic |
| 0.38% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.38% | `python` | `_PyThreadState_PopFrame` | interpreter |
| 0.37% | `[kernel.kallsyms]` | `clear_page_erms` | kernel |
| 0.36% | `python` | `list_traverse` | gc |
| 0.36% | `math.cpython-314-x86_64-linux-gnu.so` | `math_sin` | library |
| 0.35% | `python` | `PyNumber_Multiply` | dynamic |
| 0.33% | `[kernel.kallsyms]` | `sync_regs` | kernel |
| 0.32% | `python` | `slot_tp_init` | unknown |
| 0.32% | `math.cpython-314-x86_64-linux-gnu.so` | `math_sqrt` | library |
| 0.31% | `python` | `PyNumber_TrueDivide` | dynamic |
| 0.31% | `python` | `dict_traverse` | gc |
| 0.30% | `python` | `PyLong_FromLong` | int |
| 0.28% | `python` | `r_object` | import |
| 0.27% | `[kernel.kallsyms]` | `free_pcppages_bulk` | kernel |
| 0.26% | `python` | `PyObject_Vectorcall` | dynamic |
| 0.26% | `python` | `object_new` | memory |
| 0.25% | `[kernel.kallsyms]` | `rmqueue` | kernel |

## gc_collect

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 28.71% | `python` | `gc_collect_region.isra.0` | gc |
| 13.81% | `python` | `visit_reachable` | gc |
| 13.80% | `python` | `visit_decref` | gc |
| 5.66% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 4.74% | `python` | `_PyGC_Collect` | gc |
| 4.28% | `python` | `dict_traverse` | gc |
| 1.83% | `python` | `func_traverse` | gc |
| 1.63% | `python` | `PyObject_IS_GC` | gc |
| 1.47% | `python` | `subtype_traverse` | gc |
| 1.33% | `python` | `PyObject_VisitManagedDict` | dynamic |
| 1.32% | `python` | `_PyDict_MaybeUntrack` | gc |
| 1.32% | `python` | `set_traverse` | gc |
| 1.12% | `python` | `type_is_gc` | gc |
| 0.99% | `[JIT]` | `jit` | jit |
| 0.99% | `python` | `_PyObject_Malloc` | memory |
| 0.74% | `python` | `tupletraverse` | tuple |
| 0.69% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.66% | `python` | `type_traverse` | gc |
| 0.63% | `python` | `_PyObject_Free` | memory |
| 0.52% | `python` | `list_traverse` | gc |
| 0.52% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 0.50% | `python` | `meth_traverse` | gc |
| 0.44% | `python` | `subtype_dealloc` | memory |
| 0.44% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 0.40% | `python` | `_PyType_NewManagedObject` | memory |
| 0.36% | `python` | `PyObject_ClearManagedDict` | dynamic |
| 0.34% | `python` | `_Py_dict_lookup` | lookup |
| 0.33% | `python` | `_PyEval_FrameClearAndPop` | interpreter |

## gc_traversal

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 32.13% | `python` | `visit_reachable` | gc |
| 20.85% | `python` | `visit_decref` | gc |
| 16.47% | `python` | `list_traverse` | gc |
| 11.95% | `python` | `gc_collect_region.isra.0` | gc |
| 1.89% | `[JIT]` | `jit` | jit |
| 1.87% | `python` | `dict_traverse` | gc |
| 0.99% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 0.80% | `python` | `func_traverse` | gc |
| 0.79% | `python` | `PyObject_IS_GC` | gc |
| 0.61% | `python` | `_PyDict_MaybeUntrack` | gc |
| 0.57% | `python` | `set_traverse` | gc |
| 0.52% | `python` | `_PyObject_Free` | memory |
| 0.51% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.49% | `python` | `type_is_gc` | gc |
| 0.45% | `python` | `PyLong_FromLong` | int |
| 0.45% | `python` | `_PyObject_Malloc` | memory |
| 0.31% | `python` | `list_dealloc` | memory |
| 0.31% | `python` | `type_traverse` | gc |
| 0.31% | `python` | `subtype_traverse` | gc |
| 0.31% | `python` | `tupletraverse` | tuple |
| 0.26% | `libc-2.31.so` | `__nss_database_lookup` | libc |

## generators

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 31.35% | `[JIT]` | `jit` | jit |
| 23.00% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 4.13% | `python` | `_PyObject_Malloc` | memory |
| 3.11% | `python` | `_PyObject_Free` | memory |
| 1.67% | `python` | `gc_collect_region.isra.0` | gc |
| 1.45% | `python` | `gen_dealloc` | memory |
| 1.18% | `python` | `PyObject_RichCompareBool` | dynamic |
| 1.15% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.04% | `python` | `long_add` | int |
| 1.02% | `python` | `initialize_locals` | interpreter |
| 0.85% | `python` | `visit_decref` | gc |
| 0.83% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.81% | `python` | `_PyType_LookupRef` | lookup |
| 0.77% | `python` | `range_subscript` | miscobj |
| 0.75% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.73% | `python` | `visit_reachable` | gc |
| 0.73% | `python` | `long_richcompare` | int |
| 0.70% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.69% | `python` | `_PyObject_GC_NewVar` | gc |
| 0.65% | `python` | `compute_range_length` | unknown |
| 0.62% | `python` | `PyNumber_Add` | dynamic |
| 0.61% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 0.59% | `python` | `make_gen` | miscobj |
| 0.53% | `python` | `_PyEval_Vector` | interpreter |
| 0.51% | `python` | `_Py_Dealloc` | memory |
| 0.51% | `python` | `_PyBuildSlice_ConsumeRefs` | miscobj |
| 0.47% | `python` | `PyObject_GC_Del` | gc |
| 0.46% | `python` | `_PySlice_GetLongIndices` | miscobj |
| 0.44% | `python` | `PyObject_VisitManagedDict` | dynamic |
| 0.43% | `python` | `slot_tp_iter` | unknown |
| 0.42% | `python` | `subtype_traverse` | gc |
| 0.41% | `python` | `PyObject_CallOneArg` | dynamic |
| 0.40% | `python` | `visit_add_to_container` | gc |
| 0.39% | `python` | `long_mul` | int |
| 0.38% | `python` | `PyLong_AsLongAndOverflow` | int |
| 0.37% | `python` | `subtype_dealloc` | memory |
| 0.36% | `python` | `long_div` | int |
| 0.36% | `python` | `_Py_dict_lookup` | lookup |
| 0.35% | `python` | `PyObject_CallFinalizerFromDealloc` | memory |
| 0.33% | `python` | `_PyThreadState_PopFrame` | interpreter |
| 0.32% | `python` | `_Py_NewReference` | memory |
| 0.32% | `python` | `_PyType_NewManagedObject` | memory |
| 0.31% | `python` | `PyObject_ClearManagedDict` | dynamic |
| 0.30% | `python` | `long_dealloc` | memory |
| 0.28% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.27% | `python` | `PyNumber_Multiply` | dynamic |
| 0.25% | `python` | `range_dealloc` | memory |

## genshi

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 32.04% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 11.15% | `[JIT]` | `jit` | jit |
| 3.77% | `python` | `_PyObject_Malloc` | memory |
| 2.94% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 2.87% | `python` | `_PyObject_Free` | memory |
| 2.82% | `python` | `_Py_dict_lookup` | lookup |
| 1.48% | `python` | `_PyType_LookupRef` | lookup |
| 1.27% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.22% | `python` | `tupledealloc` | memory |
| 1.16% | `python` | `insertdict` | dict |
| 0.98% | `python` | `_PyTuple_FromStackRefSteal` | tuple |
| 0.95% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 0.91% | `python` | `gc_collect_region.isra.0` | gc |
| 0.87% | `python` | `insert_to_emptydict` | dict |
| 0.76% | `python` | `dict_dealloc` | memory |
| 0.68% | `python` | `_PyObject_GC_New` | gc |
| 0.66% | `python` | `initialize_locals` | interpreter |
| 0.65% | `python` | `PyDict_GetItemRef` | dict |
| 0.64% | `python` | `_PyDict_FromItems` | dict |
| 0.60% | `libc-2.31.so` | `pthread_attr_setschedparam` | libc |
| 0.59% | `python` | `pattern_subx` | library |
| 0.56% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.52% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.50% | `python` | `_Py_Dealloc` | memory |
| 0.48% | `python` | `visit_decref` | gc |
| 0.46% | `python` | `PyObject_GC_Del` | gc |
| 0.45% | `python` | `_PyObject_GetMethod` | dynamic |
| 0.44% | `python` | `PyType_IsSubtype` | dynamic |
| 0.41% | `python` | `PyObject_IsTrue` | dynamic |
| 0.40% | `python` | `long_to_decimal_string_internal` | int |
| 0.39% | `python` | `build_indices_unicode` | dict |
| 0.36% | `python` | `_Py_type_getattro` | lookup |
| 0.36% | `python` | `visit_reachable` | gc |
| 0.35% | `python` | `_PyUnicode_JoinArray.part.0` | str |
| 0.35% | `python` | `dictiter_iternextvalue` | dict |
| 0.34% | `python` | `_PyObject_GenericGetAttrWithDict` | dynamic |
| 0.34% | `python` | `r_object` | import |
| 0.33% | `python` | `gen_iternext` | miscobj |
| 0.33% | `libc-2.31.so` | `malloc` | libc |
| 0.31% | `python` | `tuplehash` | tuple |
| 0.30% | `python` | `_Py_NewReference` | memory |
| 0.28% | `python` | `update_one_slot` | lookup |
| 0.28% | `python` | `find_name_in_mro` | lookup |
| 0.28% | `python` | `list_dealloc` | memory |
| 0.27% | `python` | `PyObject_IS_GC` | gc |
| 0.27% | `python` | `find_empty_slot` | dict |
| 0.26% | `python` | `PyObject_Vectorcall` | dynamic |
| 0.25% | `python` | `PyObject_GetAttr` | dynamic |

## go

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 43.51% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 17.31% | `[JIT]` | `jit` | jit |
| 2.60% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 2.50% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 2.02% | `python` | `_PyObject_Free` | memory |
| 1.83% | `python` | `_PyObject_GetMethod` | dynamic |
| 1.71% | `python` | `_PyObject_Malloc` | memory |
| 1.66% | `python` | `_PyType_LookupRef` | lookup |
| 1.64% | `python` | `_Py_dict_lookup` | lookup |
| 1.16% | `python` | `initialize_locals` | interpreter |
| 1.15% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.93% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 0.93% | `python` | `long_bitwise` | int |
| 0.86% | `python` | `PyDict_GetItemRef` | dict |
| 0.75% | `python` | `gc_collect_region.isra.0` | gc |
| 0.55% | `python` | `_PyLong_Add` | int |
| 0.52% | `python` | `_PyThreadState_PopFrame` | interpreter |
| 0.51% | `python` | `insertdict` | dict |
| 0.45% | `python` | `visit_decref` | gc |
| 0.43% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.39% | `python` | `_Py_Dealloc` | memory |
| 0.33% | `python` | `_PyLong_Subtract` | int |
| 0.29% | `libc-2.31.so` | `pthread_attr_setschedparam` | libc |
| 0.26% | `python` | `visit_reachable` | gc |

## hexiom

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 37.99% | `[JIT]` | `jit` | jit |
| 12.70% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 3.38% | `python` | `PyObject_RichCompareBool` | dynamic |
| 2.24% | `python` | `list_contains` | list |
| 2.14% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 2.08% | `python` | `long_richcompare` | int |
| 2.02% | `python` | `_PyObject_Malloc` | memory |
| 1.97% | `python` | `_PyObject_Free` | memory |
| 1.59% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.25% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 1.17% | `python` | `gen_iternext` | miscobj |
| 0.84% | `python` | `PyLong_FromSsize_t` | int |
| 0.84% | `python` | `gc_collect_region.isra.0` | gc |
| 0.81% | `python` | `builtin_sum` | unknown |
| 0.80% | `python` | `_Py_dict_lookup` | lookup |
| 0.78% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 0.76% | `python` | `PyObject_Size` | dynamic |
| 0.68% | `python` | `_PyType_LookupRef` | lookup |
| 0.66% | `python` | `PyLong_FromLong` | int |
| 0.59% | `python` | `initialize_locals` | interpreter |
| 0.56% | `python` | `_Py_Dealloc` | memory |
| 0.55% | `python` | `PySequence_Contains` | dynamic |
| 0.55% | `python` | `_PyThreadState_PopFrame` | interpreter |
| 0.48% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.46% | `python` | `PyIter_Next` | dynamic |
| 0.43% | `python` | `slot_mp_subscript` | unknown |
| 0.42% | `python` | `range_iter` | miscobj |
| 0.39% | `python` | `visit_decref` | gc |
| 0.38% | `python` | `_PyLong_Add` | int |
| 0.37% | `python` | `list_dealloc` | memory |
| 0.35% | `python` | `tupledealloc` | memory |
| 0.32% | `python` | `PyObject_GetItem` | dynamic |
| 0.32% | `python` | `visit_reachable` | gc |
| 0.30% | `python` | `r_object` | import |
| 0.30% | `python` | `PyList_New` | memory |
| 0.30% | `python` | `PySlice_AdjustIndices` | miscobj |
| 0.29% | `python` | `PyObject_GC_Del` | gc |
| 0.29% | `python` | `PyFunction_NewWithQualName` | memory |
| 0.29% | `python` | `_PyEval_Vector` | interpreter |
| 0.28% | `python` | `update_one_slot` | lookup |
| 0.28% | `python` | `_PyObject_GC_New` | gc |
| 0.27% | `python` | `compute_range_length` | unknown |

## html5lib

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 30.05% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 7.42% | `python` | `sre_ucs2_charset.isra.0` | library |
| 6.31% | `[JIT]` | `jit` | jit |
| 2.94% | `python` | `gc_collect_region.isra.0` | gc |
| 2.87% | `python` | `_PyObject_Malloc` | memory |
| 2.25% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 2.22% | `python` | `_PyObject_Free` | memory |
| 2.00% | `python` | `_Py_dict_lookup` | lookup |
| 1.35% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.22% | `python` | `visit_decref` | gc |
| 1.15% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 0.94% | `python` | `PyDict_GetItemRef` | dict |
| 0.81% | `python` | `_PyType_LookupRef` | lookup |
| 0.72% | `python` | `PyObject_RichCompareBool` | dynamic |
| 0.68% | `python` | `sre_ucs1_count` | library |
| 0.61% | `libc-2.31.so` | `pthread_attr_setschedparam` | libc |
| 0.59% | `python` | `visit_reachable` | gc |
| 0.58% | `python` | `initialize_locals` | interpreter |
| 0.57% | `python` | `tupledealloc` | memory |
| 0.56% | `python` | `set_lookkey` | miscobj |
| 0.51% | `python` | `dict_dealloc` | memory |
| 0.50% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.48% | `python` | `visit_add_to_container` | gc |
| 0.46% | `python` | `_Py_Dealloc` | memory |
| 0.45% | `python` | `insertdict` | dict |
| 0.45% | `python` | `PyObject_GenericGetAttr` | dynamic |
| 0.42% | `python` | `PyObject_GetAttr` | dynamic |
| 0.39% | `python` | `PyNumber_AsSsize_t` | dynamic |
| 0.37% | `python` | `list_subscript` | list |
| 0.36% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.36% | `python` | `PyObject_GetItem` | dynamic |
| 0.36% | `python` | `r_object` | import |
| 0.35% | `python` | `list_dealloc` | memory |
| 0.34% | `python` | `_PyUnicode_TranslateCharmap` | str |
| 0.33% | `python` | `_PyUnicode_Equal` | str |
| 0.33% | `python` | `PyObject_GC_Del` | gc |
| 0.33% | `python` | `insert_to_emptydict` | dict |
| 0.32% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.32% | `python` | `PyList_New` | memory |
| 0.31% | `python` | `siphash13` | str |
| 0.30% | `python` | `PyObject_IsTrue` | dynamic |
| 0.30% | `python` | `update_one_slot` | lookup |
| 0.30% | `libc-2.31.so` | `malloc` | libc |
| 0.30% | `python` | `list_contains` | list |
| 0.30% | `python` | `PyType_GenericAlloc` | memory |
| 0.27% | `python` | `PyType_IsSubtype` | dynamic |
| 0.27% | `python` | `_PyObject_GC_New` | gc |
| 0.26% | `python` | `find_name_in_mro` | lookup |
| 0.26% | `python` | `sre_ucs1_match` | library |
| 0.25% | `python` | `_PyLong_Add` | int |

## json

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 11.20% | `_json.cpython-314-x86_64-linux-gnu.so` | `scanstring_unicode` | library |
| 7.07% | `python` | `_PyObject_Malloc` | memory |
| 5.46% | `_json.cpython-314-x86_64-linux-gnu.so` | `scan_once_unicode` | library |
| 5.43% | `python` | `_PyObject_Free` | memory |
| 4.87% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 4.79% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 4.70% | `python` | `siphash13` | str |
| 3.53% | `python` | `_Py_dict_lookup` | lookup |
| 3.03% | `python` | `dict_setdefault_ref_lock_held` | dict |
| 2.46% | `[JIT]` | `jit` | jit |
| 2.20% | `python` | `insertdict` | dict |
| 2.16% | `python` | `PyLong_FromString` | int |
| 2.01% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.89% | `python` | `PyUnicode_Substring` | str |
| 1.74% | `libc-2.31.so` | `pthread_attr_setschedparam` | libc |
| 1.66% | `python` | `dict_dealloc` | memory |
| 1.37% | `python` | `PyUnicode_New.part.0` | memory |
| 1.25% | `python` | `build_indices_unicode` | dict |
| 1.12% | `python` | `gc_collect_region.isra.0` | gc |
| 0.99% | `python` | `find_empty_slot` | dict |
| 0.95% | `python` | `unicode_dealloc` | memory |
| 0.90% | `python` | `PyObject_IS_GC` | gc |
| 0.84% | `python` | `_Py_Dealloc` | memory |
| 0.73% | `python` | `PyDict_SetItem` | dict |
| 0.70% | `python` | `initialize_locals` | interpreter |
| 0.70% | `python` | `_sre_SRE_Pattern_match` | library |
| 0.57% | `python` | `insert_to_emptydict` | dict |
| 0.56% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 0.53% | `python` | `visit_decref` | gc |
| 0.51% | `python` | `PyDict_GetItemRef` | dict |
| 0.49% | `python` | `tupledealloc` | memory |
| 0.45% | `python` | `sre_ucs1_match` | library |
| 0.42% | `python` | `dictresize` | dict |
| 0.41% | `python` | `r_object` | import |
| 0.41% | `python` | `_Py_NewReference` | memory |
| 0.41% | `libc-2.31.so` | `malloc` | libc |
| 0.38% | `python` | `PyUnicode_Splitlines` | str |
| 0.38% | `python` | `vgetargskeywords.constprop.0` | calls |
| 0.37% | `python` | `pattern_new_match.isra.0.part.0` | memory |
| 0.34% | `python` | `visit_reachable` | gc |
| 0.34% | `python` | `unicode_hash` | str |
| 0.33% | `python` | `_PyObject_Realloc` | memory |
| 0.32% | `python` | `resize_compact` | str |
| 0.31% | `python` | `update_one_slot` | lookup |
| 0.29% | `python` | `PyObject_Malloc` | dynamic |
| 0.28% | `python` | `new_keys_object.constprop.0` | unknown |
| 0.27% | `python` | `find_name_in_mro` | lookup |
| 0.27% | `python` | `_PyType_LookupRef` | lookup |
| 0.27% | `python` | `PyBytes_FromStringAndSize` | str |
| 0.25% | `python` | `_PyCode_Quicken` | interpreter |

## json_dumps

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 8.76% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 8.22% | `python` | `_PyObject_Malloc` | memory |
| 6.54% | `_json.cpython-314-x86_64-linux-gnu.so` | `py_encode_basestring_ascii` | library |
| 6.45% | `python` | `_PyObject_Free` | memory |
| 3.49% | `python` | `_copy_characters.part.0.constprop.0` | str |
| 3.35% | `python` | `_Py_dict_lookup` | lookup |
| 2.76% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 2.75% | `_json.cpython-314-x86_64-linux-gnu.so` | `encoder_listencode_obj` | library |
| 2.66% | `python` | `_PyUnicodeWriter_WriteStr` | str |
| 2.47% | `[JIT]` | `jit` | jit |
| 2.44% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 2.33% | `python` | `resize_compact` | str |
| 1.97% | `python` | `vgetargskeywords.constprop.0` | calls |
| 1.92% | `_json.cpython-314-x86_64-linux-gnu.so` | `encoder_encode_key_value` | library |
| 1.82% | `python` | `PyUnicode_New.part.0` | memory |
| 1.40% | `python` | `convertitem.constprop.0` | library |
| 1.22% | `python` | `_PyObject_Realloc` | memory |
| 1.21% | `python` | `_Py_Dealloc` | memory |
| 1.17% | `python` | `PyDict_GetItemRef` | dict |
| 1.09% | `python` | `gc_collect_region.isra.0` | gc |
| 1.09% | `python` | `tupledealloc` | memory |
| 1.05% | `python` | `unicode_dealloc` | memory |
| 1.05% | `python` | `_PyType_LookupRef` | lookup |
| 1.04% | `python` | `PyDict_Next` | dict |
| 1.04% | `python` | `initialize_locals` | interpreter |
| 0.92% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 0.91% | `python` | `_PyUnicodeWriter_PrepareInternal` | str |
| 0.69% | `python` | `long_to_decimal_string_internal` | int |
| 0.57% | `python` | `PyType_IsSubtype` | dynamic |
| 0.50% | `python` | `_Py_NewReference` | memory |
| 0.49% | `python` | `insertdict` | dict |
| 0.47% | `python` | `visit_decref` | gc |
| 0.45% | `python` | `long_hash` | int |
| 0.42% | `python` | `dict_dealloc` | memory |
| 0.41% | `python` | `r_object` | import |
| 0.40% | `python` | `_PyObject_GenericGetAttrWithDict` | dynamic |
| 0.40% | `python` | `_PyTuple_FromArray.part.0` | tuple |
| 0.39% | `python` | `memcpy@plt` | memory |
| 0.34% | `python` | `_Py_type_getattro` | lookup |
| 0.32% | `python` | `_PyTuple_FromStackRefSteal` | tuple |
| 0.32% | `python` | `PyFunction_NewWithQualName` | memory |
| 0.32% | `python` | `PyObject_GenericGetAttr` | dynamic |
| 0.31% | `python` | `PyObject_Malloc` | dynamic |
| 0.31% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.30% | `python` | `update_one_slot` | lookup |
| 0.30% | `python` | `visit_reachable` | gc |
| 0.29% | `python` | `PyObject_Free` | dynamic |
| 0.27% | `python` | `_PyObject_MakeTpCall` | dynamic |
| 0.27% | `python` | `_PyCode_Quicken` | interpreter |
| 0.27% | `python` | `find_name_in_mro` | lookup |
| 0.26% | `python` | `PyObject_GetAttr` | dynamic |
| 0.26% | `python` | `delitem_common` | dynamic |
| 0.26% | `python` | `_PyUnicodeWriter_WriteASCIIString` | str |
| 0.25% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.25% | `python` | `func_dealloc` | memory |

## json_loads

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 14.22% | `_json.cpython-314-x86_64-linux-gnu.so` | `scanstring_unicode` | library |
| 8.18% | `python` | `_PyObject_Malloc` | memory |
| 7.32% | `_json.cpython-314-x86_64-linux-gnu.so` | `scan_once_unicode` | library |
| 6.58% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 6.08% | `python` | `siphash13` | str |
| 5.78% | `python` | `_PyObject_Free` | memory |
| 4.10% | `python` | `_Py_dict_lookup` | lookup |
| 3.91% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 3.29% | `python` | `PyUnicode_Substring` | str |
| 2.85% | `python` | `insertdict` | dict |
| 2.73% | `python` | `PyLong_FromString` | int |
| 2.69% | `python` | `dict_setdefault_ref_lock_held` | dict |
| 2.39% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 2.35% | `python` | `PyUnicode_New.part.0` | memory |
| 1.22% | `python` | `unicode_dealloc` | memory |
| 1.05% | `python` | `dict_dealloc` | memory |
| 0.98% | `python` | `find_empty_slot` | dict |
| 0.97% | `python` | `_Py_Dealloc` | memory |
| 0.90% | `python` | `PyDict_SetItem` | dict |
| 0.87% | `python` | `PyObject_IS_GC` | gc |
| 0.86% | `python` | `build_indices_unicode` | dict |
| 0.75% | `libc-2.31.so` | `pthread_attr_setschedparam` | libc |
| 0.58% | `python` | `gc_collect_region.isra.0` | gc |
| 0.52% | `python` | `_Py_NewReference` | memory |
| 0.51% | `python` | `_PyUnicodeWriter_Init` | str |
| 0.47% | `[JIT]` | `jit` | jit |
| 0.47% | `python` | `unicode_hash` | str |
| 0.38% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 0.37% | `python` | `PyObject_Malloc` | dynamic |
| 0.36% | `libc-2.31.so` | `malloc` | libc |
| 0.34% | `python` | `dictresize` | dict |
| 0.34% | `python` | `PyList_Append` | list |
| 0.32% | `python` | `initialize_locals` | interpreter |
| 0.32% | `python` | `_sre_SRE_Pattern_match` | library |
| 0.31% | `python` | `PyObject_Free` | dynamic |
| 0.30% | `python` | `tupledealloc` | memory |
| 0.30% | `python` | `insert_to_emptydict` | dict |
| 0.30% | `python` | `sre_ucs1_match` | library |
| 0.30% | `python` | `PyObject_Hash` | dynamic |
| 0.28% | `python` | `_Py_HashBytes` | unknown |
| 0.28% | `python` | `PyDict_GetItemRef` | dict |
| 0.27% | `python` | `PyBytes_FromStringAndSize` | str |
| 0.26% | `python` | `visit_decref` | gc |
| 0.25% | `python` | `new_keys_object.constprop.0` | unknown |
| 0.25% | `python` | `_PyObject_Realloc` | memory |

## logging

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 30.68% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 11.93% | `[JIT]` | `jit` | jit |
| 3.91% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 2.66% | `python` | `_PyObject_Malloc` | memory |
| 2.65% | `python` | `_Py_dict_lookup` | lookup |
| 2.23% | `python` | `_PyObject_Free` | memory |
| 2.15% | `python` | `initialize_locals` | interpreter |
| 2.15% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.80% | `python` | `PyCode_Addr2Line` | exceptions |
| 1.78% | `python` | `dict_dealloc` | memory |
| 1.40% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 1.38% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.16% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 1.16% | `python` | `PyDict_GetItemRef` | dict |
| 1.06% | `python` | `PyDict_New` | memory |
| 1.00% | `python` | `_PyType_LookupRef` | lookup |
| 0.85% | `python` | `_PyThreadState_PopFrame` | interpreter |
| 0.73% | `python` | `_Py_Dealloc` | memory |
| 0.72% | `python` | `PyUnicode_Contains` | str |
| 0.65% | `python` | `PyObject_GenericGetAttr` | dynamic |
| 0.62% | `python` | `PyObject_GetAttr` | dynamic |
| 0.55% | `python` | `gc_collect_region.isra.0` | gc |
| 0.47% | `python` | `_PyObject_LookupSpecialMethod` | dynamic |
| 0.47% | `python` | `tupledealloc` | memory |
| 0.45% | `python` | `_PyThreadState_PushFrame` | interpreter |
| 0.43% | `python` | `_Py_NewReference` | memory |
| 0.42% | `python` | `PyUnicode_Format` | str |
| 0.40% | `python` | `PySlice_AdjustIndices` | miscobj |
| 0.32% | `python` | `_PyTuple_FromArray.part.0` | tuple |
| 0.32% | `python` | `long_hash` | int |
| 0.32% | `python` | `any_find_slice` | unknown |
| 0.31% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.30% | `python` | `_PyObject_GenericGetAttrWithDict` | dynamic |
| 0.29% | `python` | `PyObject_Hash` | dynamic |
| 0.28% | `python` | `make_dict_from_instance_attributes` | unknown |
| 0.28% | `python` | `PyUnicode_Splitlines` | str |
| 0.27% | `python` | `PyObject_IS_GC` | gc |
| 0.27% | `python` | `PyObject_Vectorcall` | dynamic |
| 0.26% | `python` | `l_mod` | int |
| 0.26% | `python` | `visit_decref` | gc |
| 0.26% | `python` | `siphash13` | str |
| 0.25% | `python` | `PyLong_FromLong` | int |

## mako

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 28.14% | `[JIT]` | `jit` | jit |
| 8.62% | `python` | `replace` | str |
| 5.05% | `python` | `long_to_decimal_string_internal` | int |
| 4.93% | `python` | `_PyObject_Malloc` | memory |
| 4.36% | `python` | `_PyObject_Free` | memory |
| 4.04% | `python` | `_PyUnicode_JoinArray.part.0` | str |
| 2.78% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 2.63% | `python` | `unicode_replace` | str |
| 2.54% | `python` | `deque_append` | miscobj |
| 2.28% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.85% | `python` | `dequeiter_next` | miscobj |
| 1.30% | `python` | `_list_extend` | list |
| 1.21% | `python` | `PyErr_CheckSignals` | exceptions |
| 1.07% | `python` | `list_dealloc` | memory |
| 1.03% | `python` | `PyUnicode_New.part.0` | memory |
| 0.96% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.91% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 0.90% | `python` | `deque_clear.part.0` | miscobj |
| 0.88% | `python` | `sre_ucs2_charset.isra.0` | library |
| 0.81% | `python` | `gc_collect_region.isra.0` | gc |
| 0.80% | `python` | `PyObject_Str` | dynamic |
| 0.71% | `libc-2.31.so` | `pthread_attr_setschedparam` | libc |
| 0.71% | `python` | `unicode_dealloc` | memory |
| 0.62% | `python` | `_Py_dict_lookup` | lookup |
| 0.56% | `python` | `PyThread_get_thread_ident` | unknown |
| 0.55% | `python` | `PyLong_FromLong` | int |
| 0.49% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.46% | `python` | `_Py_Dealloc` | memory |
| 0.44% | `python` | `_Py_NewReference` | memory |
| 0.40% | `[kernel.kallsyms]` | `native_irq_return_iret` | kernel |
| 0.39% | `python` | `visit_decref` | gc |
| 0.37% | `python` | `long_to_decimal_string` | int |
| 0.36% | `[kernel.kallsyms]` | `clear_page_erms` | kernel |
| 0.33% | `[kernel.kallsyms]` | `sync_regs` | kernel |
| 0.32% | `python` | `visit_reachable` | gc |
| 0.31% | `python` | `r_object` | import |
| 0.31% | `python` | `memcpy@plt` | memory |
| 0.30% | `python` | `PyObject_Malloc` | dynamic |
| 0.28% | `python` | `update_one_slot` | lookup |
| 0.26% | `python` | `PyObject_Free` | dynamic |
| 0.25% | `python` | `_PyType_LookupRef` | lookup |

## mdp

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 28.34% | `python` | `tuplehash` | tuple |
| 13.75% | `python` | `PyObject_Hash` | dynamic |
| 10.45% | `python` | `long_hash` | int |
| 7.89% | `[JIT]` | `jit` | jit |
| 7.64% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 6.52% | `python` | `_Py_dict_lookup` | lookup |
| 2.97% | `python` | `PyObject_RichCompareBool` | dynamic |
| 1.85% | `python` | `tuplerichcompare` | tuple |
| 1.52% | `python` | `_PyObject_Malloc` | memory |
| 1.37% | `python` | `_PyObject_Free` | memory |
| 1.18% | `python` | `dict_subscript` | dict |
| 0.96% | `python` | `_PyLong_GCD` | int |
| 0.73% | `python` | `PyDict_GetItemRef` | dict |
| 0.73% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.62% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 0.49% | `python` | `builtin_sum` | unknown |
| 0.46% | `python` | `gen_iternext` | miscobj |
| 0.42% | `python` | `set_lookkey` | miscobj |
| 0.37% | `python` | `_Py_Dealloc` | memory |
| 0.36% | `python` | `insertdict` | dict |
| 0.36% | `python` | `PyObject_GetItem` | dynamic |
| 0.34% | `python` | `_PyType_LookupRef` | lookup |
| 0.32% | `python` | `subtype_dealloc` | memory |
| 0.31% | `python` | `tupledealloc` | memory |
| 0.28% | `python` | `PyFunction_NewWithQualName` | memory |

## meteor_contest

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 16.53% | `[JIT]` | `jit` | jit |
| 8.56% | `python` | `set_issubset_impl` | miscobj |
| 8.28% | `python` | `set_lookkey` | miscobj |
| 5.66% | `python` | `setiter_iternext` | miscobj |
| 3.60% | `python` | `set_difference` | miscobj |
| 3.37% | `python` | `_PyObject_Free` | memory |
| 3.21% | `python` | `set_dealloc` | memory |
| 3.05% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 3.05% | `python` | `_PyObject_Malloc` | memory |
| 2.65% | `python` | `PyObject_RichCompareBool` | dynamic |
| 2.22% | `python` | `set_add_entry` | miscobj |
| 1.81% | `python` | `long_richcompare` | int |
| 1.64% | `python` | `list_dealloc` | memory |
| 1.50% | `python` | `min_max` | unknown |
| 1.26% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.22% | `python` | `list_slice_lock_held.isra.0` | list |
| 1.12% | `python` | `PyObject_RichCompare` | dynamic |
| 1.12% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 1.03% | `python` | `gc_collect_region.isra.0` | gc |
| 0.99% | `python` | `set_intersection` | miscobj |
| 0.95% | `python` | `set_table_resize` | miscobj |
| 0.89% | `python` | `PyIter_Next` | dynamic |
| 0.80% | `python` | `set_merge_lock_held.part.0` | miscobj |
| 0.75% | `python` | `PyObject_GC_Del` | gc |
| 0.72% | `python` | `PyType_GenericAlloc` | memory |
| 0.66% | `python` | `_Py_dict_lookup` | lookup |
| 0.65% | `python` | `_Py_Dealloc` | memory |
| 0.58% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 0.57% | `python` | `PySlice_AdjustIndices` | miscobj |
| 0.51% | `python` | `_PyObject_GC_New` | gc |
| 0.50% | `python` | `initialize_locals` | interpreter |
| 0.47% | `python` | `set_richcompare` | miscobj |
| 0.45% | `python` | `visit_decref` | gc |
| 0.45% | `python` | `set_difference_update_internal` | miscobj |
| 0.37% | `python` | `PyList_New` | memory |
| 0.37% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.34% | `python` | `visit_reachable` | gc |
| 0.34% | `python` | `r_object` | import |
| 0.32% | `python` | `_PyBuildSlice_ConsumeRefs` | miscobj |
| 0.32% | `python` | `_PyObject_GC_Link` | gc |
| 0.31% | `python` | `PyObject_Size` | dynamic |
| 0.28% | `python` | `list_ass_slice_lock_held` | list |
| 0.27% | `python` | `slice_dealloc` | memory |
| 0.26% | `python` | `PyObject_IsTrue` | dynamic |
| 0.26% | `python` | `_PyCode_Quicken` | interpreter |
| 0.26% | `python` | `update_one_slot` | lookup |

## nbody

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 63.46% | `[JIT]` | `jit` | jit |
| 4.43% | `libm-2.31.so` | `f64xsubf128` | library |
| 4.01% | `python` | `PyFloat_FromDouble` | float |
| 3.34% | `python` | `_Py_Dealloc` | memory |
| 3.29% | `python` | `float_dealloc` | memory |
| 1.89% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 1.82% | `python` | `_Py_NewReference` | memory |
| 1.50% | `python` | `float_pow` | float |
| 0.84% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.81% | `python` | `_PyObject_Free` | memory |
| 0.70% | `python` | `_PyObject_Malloc` | memory |
| 0.63% | `python` | `gc_collect_region.isra.0` | gc |
| 0.43% | `libm-2.31.so` | `pow` | library |
| 0.42% | `python` | `_PyNumber_PowerNoMod` | dynamic |
| 0.41% | `python` | `_Py_dict_lookup` | lookup |
| 0.37% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 0.35% | `python` | `visit_decref` | gc |
| 0.34% | `python` | `_PyFloat_ExactDealloc` | memory |
| 0.28% | `python` | `r_object` | import |

## nqueens

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 18.38% | `[JIT]` | `jit` | jit |
| 16.01% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 4.65% | `python` | `_PyObject_Malloc` | memory |
| 4.55% | `python` | `_PyObject_Free` | memory |
| 2.19% | `python` | `set_add_entry` | miscobj |
| 1.99% | `python` | `gen_iternext` | miscobj |
| 1.98% | `python` | `PySlice_AdjustIndices` | miscobj |
| 1.93% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 1.24% | `python` | `_Py_dict_lookup` | lookup |
| 1.22% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.17% | `python` | `_PyLong_Add` | int |
| 1.09% | `python` | `_PyBuildSlice_ConsumeRefs` | miscobj |
| 1.08% | `python` | `list_dealloc` | memory |
| 1.06% | `python` | `tupledealloc` | memory |
| 1.01% | `python` | `_Py_Dealloc` | memory |
| 1.01% | `python` | `gc_collect_region.isra.0` | gc |
| 1.00% | `python` | `set_dealloc` | memory |
| 0.97% | `python` | `PyList_New` | memory |
| 0.82% | `python` | `PyFunction_NewWithQualName` | memory |
| 0.73% | `python` | `PyNumber_AsSsize_t` | dynamic |
| 0.70% | `python` | `PyObject_GC_Del` | gc |
| 0.70% | `python` | `list_subscript` | list |
| 0.64% | `python` | `_PyEval_SliceIndex` | interpreter |
| 0.64% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.63% | `python` | `slice_dealloc` | memory |
| 0.57% | `python` | `set_table_resize` | miscobj |
| 0.55% | `python` | `PyIter_Next` | dynamic |
| 0.54% | `python` | `visit_decref` | gc |
| 0.53% | `python` | `list_ass_slice_lock_held` | list |
| 0.52% | `python` | `PySlice_Unpack` | miscobj |
| 0.51% | `python` | `gen_dealloc` | memory |
| 0.50% | `python` | `list_ass_subscript` | list |
| 0.48% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 0.48% | `python` | `_PyObject_LookupSpecial` | dynamic |
| 0.48% | `python` | `PySequence_Tuple` | dynamic |
| 0.47% | `python` | `_PyObject_GC_NewVar` | gc |
| 0.47% | `python` | `PyLong_FromLong` | int |
| 0.45% | `python` | `set_update_iterable_lock_held` | miscobj |
| 0.45% | `python` | `_Py_NewReference` | memory |
| 0.44% | `python` | `_PyLong_Subtract` | int |
| 0.41% | `python` | `list_slice_lock_held.isra.0` | list |
| 0.41% | `python` | `_PyTuple_FromStackRefSteal` | tuple |
| 0.40% | `python` | `func_dealloc` | memory |
| 0.40% | `python` | `_PyObject_GC_New` | gc |
| 0.40% | `python` | `r_object` | import |
| 0.38% | `python` | `func_clear` | unknown |
| 0.37% | `python` | `visit_reachable` | gc |
| 0.34% | `python` | `compute_range_length` | unknown |
| 0.34% | `python` | `update_one_slot` | lookup |
| 0.34% | `python` | `range_iter` | miscobj |
| 0.33% | `python` | `PyObject_GetItem` | dynamic |
| 0.33% | `python` | `PyLong_AsSsize_t` | int |
| 0.32% | `python` | `PyDict_GetItemRef` | dict |
| 0.31% | `python` | `_PyObject_Realloc` | memory |
| 0.30% | `python` | `_PyType_LookupRef` | lookup |
| 0.29% | `python` | `find_name_in_mro` | lookup |
| 0.28% | `python` | `PyLong_AsLong` | int |
| 0.28% | `python` | `_PyObject_GC_Link` | gc |
| 0.28% | `python` | `_PyCode_Quicken` | interpreter |
| 0.28% | `python` | `siphash13` | str |
| 0.27% | `python` | `_Py_hashtable_get_entry_generic` | lookup |
| 0.27% | `python` | `PyTuple_New` | memory |
| 0.27% | `libc-2.31.so` | `pthread_attr_setschedparam` | libc |
| 0.27% | `python` | `PyObject_GetIter` | dynamic |
| 0.26% | `python` | `_PyTuple_Resize` | tuple |
| 0.26% | `python` | `range_reverse` | miscobj |
| 0.26% | `python` | `PyType_GenericAlloc` | memory |

## pathlib

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 9.81% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 5.50% | `python` | `_PyObject_Malloc` | memory |
| 4.90% | `python` | `_PyObject_Free` | memory |
| 3.22% | `[JIT]` | `jit` | jit |
| 1.62% | `[kernel.kallsyms]` | `__d_lookup_rcu` | kernel |
| 1.56% | `python` | `_PyType_LookupRef` | lookup |
| 1.52% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.41% | `libpthread-2.31.so` | `__pthread_mutex_lock` | library |
| 1.38% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 1.28% | `libpthread-2.31.so` | `pthread_mutex_unlock` | library |
| 1.24% | `[kernel.kallsyms]` | `ext4_htree_store_dirent` | kernel |
| 1.22% | `[kernel.kallsyms]` | `__ext4fs_dirhash` | kernel |
| 1.21% | `[kernel.kallsyms]` | `memset_erms` | kernel |
| 1.18% | `python` | `_Py_Dealloc` | memory |
| 1.07% | `python` | `initialize_locals` | interpreter |
| 1.00% | `libc-2.31.so` | `pthread_attr_setschedparam` | libc |
| 0.87% | `python` | `take_gil` | gil |
| 0.83% | `python` | `k_mul` | int |
| 0.83% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 0.82% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.80% | `[kernel.kallsyms]` | `filldir64` | kernel |
| 0.74% | `python` | `subtype_dealloc` | memory |
| 0.73% | `python` | `_Py_dict_lookup` | lookup |
| 0.71% | `python` | `sre_ucs1_match` | library |
| 0.68% | `python` | `tupledealloc` | memory |
| 0.65% | `[kernel.kallsyms]` | `strncpy_from_user` | kernel |
| 0.65% | `python` | `gc_collect_region.isra.0` | gc |
| 0.63% | `python` | `fill_time` | unknown |
| 0.60% | `python` | `_PyObject_LookupSpecial` | dynamic |
| 0.58% | `python` | `_Py_NewReference` | memory |
| 0.56% | `[kernel.kallsyms]` | `copy_user_enhanced_fast_string` | kernel |
| 0.55% | `python` | `x_add` | int |
| 0.55% | `[kernel.kallsyms]` | `__slab_free` | kernel |
| 0.53% | `[kernel.kallsyms]` | `link_path_walk.part.0` | kernel |
| 0.50% | `python` | `_PyArg_UnpackKeywords` | calls |
| 0.50% | `[kernel.kallsyms]` | `__virt_addr_valid` | kernel |
| 0.49% | `[kernel.kallsyms]` | `syscall_return_via_sysret` | kernel |
| 0.48% | `[kernel.kallsyms]` | `rb_insert_color` | kernel |
| 0.47% | `python` | `_PyTuple_FromStackRefSteal` | tuple |
| 0.47% | `[kernel.kallsyms]` | `str2hashbuf_signed` | kernel |
| 0.46% | `python` | `map_next` | unknown |
| 0.46% | `python` | `long_dealloc` | memory |
| 0.45% | `python` | `ascii_decode` | str |
| 0.45% | `[kernel.kallsyms]` | `rb_next` | kernel |
| 0.44% | `[kernel.kallsyms]` | `ext4_getattr` | kernel |
| 0.44% | `[kernel.kallsyms]` | `__ext4_check_dir_entry` | kernel |
| 0.44% | `python` | `ScandirIterator_iternext` | unknown |
| 0.43% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.43% | `[kernel.kallsyms]` | `security_inode_getattr` | kernel |
| 0.41% | `python` | `structseq_dealloc` | memory |
| 0.41% | `python` | `_PyFunction_Vectorcall` | calls |
| 0.40% | `python` | `method_vectorcall` | calls |
| 0.40% | `[kernel.kallsyms]` | `kmem_cache_alloc` | kernel |
| 0.38% | `python` | `PyFloat_FromDouble` | float |
| 0.37% | `python` | `PyLong_FromUnsignedLong` | int |
| 0.37% | `python` | `_sre_SRE_Pattern_match` | library |
| 0.36% | `python` | `_PyEval_Vector` | interpreter |
| 0.36% | `python` | `_Py_type_getattro` | lookup |
| 0.35% | `python` | `_PyType_GetDict` | dynamic |
| 0.35% | `libc-2.31.so` | `__xstat` | libc |
| 0.35% | `python` | `PyLong_FromLongLong` | int |
| 0.34% | `python` | `visit_decref` | gc |
| 0.34% | `[kernel.kallsyms]` | `__kmalloc` | kernel |
| 0.34% | `python` | `PyDict_GetItemWithError` | dict |
| 0.34% | `[kernel.kallsyms]` | `lookup_fast` | kernel |
| 0.34% | `python` | `listiter_next` | list |
| 0.33% | `python` | `unicode_decode_utf8.part.0` | str |
| 0.33% | `python` | `PyObject_GC_Del` | gc |
| 0.32% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.32% | `[kernel.kallsyms]` | `set_root` | kernel |
| 0.31% | `python` | `tp_new_wrapper` | memory |
| 0.31% | `python` | `PyDict_GetItemRef` | dict |
| 0.31% | `[kernel.kallsyms]` | `entry_SYSCALL_64` | kernel |
| 0.30% | `python` | `PyLong_AsSsize_t` | int |
| 0.29% | `[kernel.kallsyms]` | `kfree` | kernel |
| 0.28% | `python` | `_PyThreadState_PushFrame` | interpreter |
| 0.28% | `python` | `PyObject_Malloc` | dynamic |
| 0.28% | `python` | `path_converter` | unknown |
| 0.27% | `python` | `_PyObject_GenericGetAttrWithDict` | dynamic |
| 0.27% | `[kernel.kallsyms]` | `in_group_p` | kernel |
| 0.27% | `[kernel.kallsyms]` | `call_filldir` | kernel |
| 0.27% | `[kernel.kallsyms]` | `memchr` | kernel |
| 0.27% | `[kernel.kallsyms]` | `ext4_find_dest_de` | kernel |
| 0.26% | `python` | `float_dealloc` | memory |
| 0.26% | `python` | `_pystat_fromstructstat` | unknown |
| 0.26% | `python` | `list_dealloc` | memory |
| 0.26% | `python` | `os_stat` | unknown |
| 0.26% | `python` | `PyUnicode_New.part.0` | memory |
| 0.25% | `python` | `PyLong_FromLong` | int |

## pickle_pure_python

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 20.83% | `[JIT]` | `jit` | jit |
| 19.19% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 4.49% | `python` | `_PyObject_Malloc` | memory |
| 4.37% | `python` | `_Py_dict_lookup` | lookup |
| 3.89% | `python` | `_PyObject_Free` | memory |
| 2.53% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.69% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.61% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 1.51% | `python` | `initialize_locals` | interpreter |
| 1.28% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.99% | `python` | `gc_collect_region.isra.0` | gc |
| 0.84% | `python` | `tupledealloc` | memory |
| 0.83% | `python` | `PyBuffer_FillInfo` | miscobj |
| 0.79% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.75% | `python` | `dict_get` | dict |
| 0.68% | `python` | `PyDict_GetItemRef` | dict |
| 0.67% | `python` | `bytes_concat` | str |
| 0.66% | `python` | `_Py_Dealloc` | memory |
| 0.65% | `python` | `PyLong_FromVoidPtr` | int |
| 0.65% | `python` | `PyBuffer_Release` | miscobj |
| 0.61% | `python` | `PyLong_FromSsize_t` | int |
| 0.58% | `python` | `_PyType_LookupRef` | lookup |
| 0.57% | `python` | `_PyTuple_FromStackRefSteal` | tuple |
| 0.56% | `libc-2.31.so` | `pthread_attr_setschedparam` | libc |
| 0.55% | `python` | `insertdict` | dict |
| 0.53% | `python` | `_PyThreadState_PopFrame` | interpreter |
| 0.51% | `python` | `visit_decref` | gc |
| 0.44% | `python` | `write_bytes` | unknown |
| 0.44% | `python` | `long_hash` | int |
| 0.43% | `python` | `sys_audit_tstate` | unknown |
| 0.41% | `python` | `_PyObject_GenericGetAttrWithDict` | dynamic |
| 0.41% | `python` | `PyUnicode_AsEncodedString.part.0` | str |
| 0.41% | `python` | `PyNumber_Add` | dynamic |
| 0.40% | `python` | `r_object` | import |
| 0.36% | `python` | `PySys_Audit` | unknown |
| 0.36% | `_struct.cpython-314-x86_64-linux-gnu.so` | `s_pack_internal.isra.0` | library |
| 0.36% | `python` | `unicode_encode` | str |
| 0.35% | `python` | `_PyObject_Realloc` | memory |
| 0.35% | `python` | `visit_reachable` | gc |
| 0.32% | `python` | `PyObject_GetBuffer` | dynamic |
| 0.32% | `python` | `_Py_NewReference` | memory |
| 0.31% | `python` | `update_one_slot` | lookup |
| 0.31% | `python` | `PyBytes_FromStringAndSize.constprop.0` | str |
| 0.31% | `python` | `PyObject_Size` | dynamic |
| 0.28% | `python` | `PyObject_Malloc` | dynamic |
| 0.28% | `python` | `_PyCode_Quicken` | interpreter |
| 0.28% | `python` | `dictiter_iternextitem` | dict |
| 0.27% | `python` | `find_name_in_mro` | lookup |
| 0.26% | `_struct.cpython-314-x86_64-linux-gnu.so` | `pack` | library |
| 0.26% | `python` | `PyObject_Hash` | dynamic |
| 0.26% | `python` | `PyType_GetModuleByDef` | dynamic |
| 0.26% | `python` | `PyBytes_FromStringAndSize` | str |
| 0.25% | `python` | `_Py_hashtable_get_entry_generic` | lookup |
| 0.25% | `_struct.cpython-314-x86_64-linux-gnu.so` | `s_pack` | library |
| 0.25% | `python` | `bytes_buffer_getbuffer` | str |

## pidigits

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 32.10% | `python` | `x_divrem` | int |
| 28.41% | `python` | `k_mul` | int |
| 12.86% | `python` | `x_add` | int |
| 7.15% | `python` | `x_sub` | int |
| 2.27% | `libc-2.31.so` | `pthread_attr_setschedparam` | libc |
| 1.71% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.62% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 1.21% | `[JIT]` | `jit` | jit |
| 0.85% | `python` | `_PyObject_Free` | memory |
| 0.76% | `python` | `_PyObject_Malloc` | memory |
| 0.66% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.49% | `python` | `gc_collect_region.isra.0` | gc |
| 0.34% | `python` | `_Py_dict_lookup` | lookup |
| 0.26% | `python` | `visit_decref` | gc |

## pprint

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 22.15% | `[JIT]` | `jit` | jit |
| 12.80% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 5.72% | `python` | `_PyObject_Malloc` | memory |
| 3.99% | `python` | `_PyObject_Free` | memory |
| 3.64% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 3.46% | `python` | `_PyType_LookupRef` | lookup |
| 2.25% | `python` | `_Py_dict_lookup` | lookup |
| 2.04% | `python` | `tupledealloc` | memory |
| 1.69% | `python` | `_Py_type_getattro_impl` | dynamic |
| 1.66% | `python` | `_Py_type_getattro` | lookup |
| 1.66% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.43% | `python` | `_PyTuple_FromStackRefSteal` | tuple |
| 1.42% | `python` | `long_to_decimal_string_internal` | int |
| 1.26% | `python` | `_PyUnicode_JoinArray.part.0` | str |
| 1.18% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.01% | `python` | `PyUnicode_Format` | str |
| 1.01% | `python` | `set_lookkey` | miscobj |
| 0.93% | `python` | `_Py_Dealloc` | memory |
| 0.89% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.76% | `python` | `resize_compact` | str |
| 0.76% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.73% | `python` | `PyObject_GetAttr` | dynamic |
| 0.69% | `python` | `PyUnicode_New.part.0` | memory |
| 0.68% | `python` | `_PyObject_Realloc` | memory |
| 0.65% | `python` | `_PyTuple_FromArray.part.0` | tuple |
| 0.64% | `python` | `_copy_characters.part.0.constprop.0` | str |
| 0.57% | `python` | `PyObject_IsSubclass` | dynamic |
| 0.55% | `python` | `list_sort_impl` | list |
| 0.53% | `python` | `unicode_dealloc` | memory |
| 0.52% | `python` | `initialize_locals` | interpreter |
| 0.50% | `python` | `_PyUnicodeWriter_WriteSubstring` | str |
| 0.50% | `python` | `PyObject_GC_Del` | gc |
| 0.50% | `python` | `PyObject_GetOptionalAttr` | dynamic |
| 0.50% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.49% | `python` | `_Py_NewReference` | memory |
| 0.48% | `python` | `subtype_dealloc` | memory |
| 0.47% | `python` | `insertdict` | dict |
| 0.46% | `python` | `list_append` | list |
| 0.44% | `python` | `PyList_New` | memory |
| 0.43% | `python` | `PyErr_CheckSignals` | exceptions |
| 0.39% | `python` | `list_dealloc` | memory |
| 0.39% | `python` | `_PyThreadState_PopFrame` | interpreter |
| 0.39% | `python` | `long_hash` | int |
| 0.38% | `python` | `PyType_GenericAlloc` | memory |
| 0.37% | `python` | `_PyObject_GC_New` | gc |
| 0.36% | `python` | `PyObject_GenericGetAttr` | dynamic |
| 0.35% | `python` | `_PyObject_MakeTpCall` | dynamic |
| 0.34% | `python` | `PyObject_Hash` | dynamic |
| 0.34% | `python` | `_PySet_Contains` | miscobj |
| 0.34% | `python` | `builtin_getattr` | lookup |
| 0.32% | `python` | `_PyEval_Vector` | interpreter |
| 0.32% | `python` | `_PyUnicodeWriter_PrepareInternal` | str |
| 0.31% | `python` | `_PyObject_GC_Link` | gc |
| 0.30% | `python` | `_PyDict_LoadGlobal` | dict |
| 0.30% | `python` | `wrapperdescr_get` | unknown |
| 0.30% | `python` | `PyObject_Repr` | dynamic |
| 0.29% | `python` | `PyType_IsSubtype` | dynamic |
| 0.28% | `python` | `builtin_issubclass` | unknown |
| 0.28% | `python` | `slot_tp_richcompare` | dynamic |
| 0.27% | `python` | `recursive_issubclass` | unknown |
| 0.25% | `python` | `delitem_common` | dynamic |

## pycparser

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 16.59% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 14.57% | `[JIT]` | `jit` | jit |
| 13.91% | `python` | `sre_ucs1_match` | library |
| 3.77% | `python` | `gc_collect_region.isra.0` | gc |
| 2.86% | `python` | `_PyObject_Malloc` | memory |
| 2.86% | `python` | `_Py_dict_lookup` | lookup |
| 2.32% | `python` | `_PyObject_Free` | memory |
| 2.15% | `libc-2.31.so` | `pthread_attr_setschedparam` | libc |
| 1.94% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 1.44% | `python` | `_PyType_LookupRef` | lookup |
| 1.35% | `python` | `PySlice_AdjustIndices` | miscobj |
| 1.19% | `python` | `PyDict_GetItemRef` | dict |
| 1.10% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 0.98% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 0.96% | `python` | `visit_decref` | gc |
| 0.96% | `python` | `_sre_SRE_Pattern_match` | library |
| 0.84% | `python` | `pattern_new_match.isra.0.part.0` | memory |
| 0.84% | `python` | `list_ass_slice_lock_held` | list |
| 0.83% | `python` | `subtype_traverse` | gc |
| 0.83% | `python` | `initialize_locals` | interpreter |
| 0.78% | `python` | `visit_add_to_container` | gc |
| 0.68% | `python` | `subtype_dealloc` | memory |
| 0.64% | `python` | `sre_ucs1_count` | library |
| 0.55% | `python` | `visit_reachable` | gc |
| 0.54% | `python` | `_Py_Dealloc` | memory |
| 0.52% | `python` | `list_subscript` | list |
| 0.52% | `python` | `dict_get` | dict |
| 0.52% | `python` | `PyType_GenericAlloc` | memory |
| 0.51% | `python` | `slice_dealloc` | memory |
| 0.51% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.50% | `python` | `PyNumber_AsSsize_t` | dynamic |
| 0.49% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.47% | `python` | `_PyObject_GenericGetAttrWithDict` | dynamic |
| 0.46% | `python` | `sre_ucs2_charset.isra.0` | library |
| 0.44% | `python` | `PySlice_New` | memory |
| 0.43% | `python` | `PyObject_ClearManagedDict` | dynamic |
| 0.41% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.41% | `libc-2.31.so` | `malloc` | libc |
| 0.40% | `python` | `PyObject_Vectorcall` | dynamic |
| 0.39% | `python` | `long_neg` | int |
| 0.38% | `python` | `list_dealloc` | memory |
| 0.35% | `python` | `list_ass_subscript` | list |
| 0.35% | `python` | `vectorcall_method` | calls |
| 0.33% | `python` | `PyList_New` | memory |
| 0.33% | `python` | `_PyEval_SliceIndex` | interpreter |
| 0.32% | `python` | `PyObject_IsTrue` | dynamic |
| 0.32% | `python` | `PyType_IsSubtype` | dynamic |
| 0.29% | `python` | `_PyObject_MakeTpCall` | dynamic |
| 0.29% | `python` | `_PyBuildSlice_ConsumeRefs` | miscobj |
| 0.29% | `python` | `PySlice_Unpack` | miscobj |
| 0.29% | `python` | `PyObject_GC_Del` | gc |
| 0.25% | `python` | `dict_dealloc` | memory |

## pyflate

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 29.40% | `[JIT]` | `jit` | jit |
| 7.33% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 6.04% | `python` | `list_ass_slice_lock_held` | list |
| 5.01% | `python` | `_PyObject_Free` | memory |
| 4.00% | `python` | `list_dealloc` | memory |
| 3.96% | `python` | `_PyObject_Malloc` | memory |
| 2.84% | `libc-2.31.so` | `pthread_attr_setschedparam` | libc |
| 2.63% | `python` | `PyNumber_AsSsize_t` | dynamic |
| 1.93% | `python` | `list_concat` | list |
| 1.81% | `python` | `list_slice_lock_held.isra.0` | list |
| 1.59% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.53% | `python` | `_PyLong_Add` | int |
| 1.47% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.44% | `python` | `PySlice_AdjustIndices` | miscobj |
| 1.31% | `python` | `_PyLong_Subtract` | int |
| 1.20% | `python` | `PyLong_AsSsize_t` | int |
| 0.97% | `python` | `list_sort_impl` | list |
| 0.95% | `python` | `long_lshift` | int |
| 0.88% | `python` | `stringlib_bytes_join` | str |
| 0.84% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.80% | `python` | `PyLong_FromSsize_t` | int |
| 0.79% | `python` | `bytes_subscript` | str |
| 0.71% | `python` | `_Py_Dealloc` | memory |
| 0.70% | `python` | `_PyBuildSlice_ConsumeRefs` | miscobj |
| 0.65% | `python` | `PyList_New` | memory |
| 0.63% | `python` | `long_lshift1` | int |
| 0.63% | `python` | `unsafe_long_compare` | unknown |
| 0.59% | `python` | `long_dealloc` | memory |
| 0.57% | `python` | `PyObject_GetItem` | dynamic |
| 0.56% | `python` | `_Py_NewReference` | memory |
| 0.56% | `python` | `slice_dealloc` | memory |
| 0.50% | `python` | `_PyEval_SliceIndex` | interpreter |
| 0.50% | `python` | `long_and` | int |
| 0.46% | `python` | `long_rshift` | int |
| 0.46% | `python` | `PyBuffer_Release` | miscobj |
| 0.44% | `python` | `PyNumber_Lshift` | dynamic |
| 0.42% | `python` | `_PyBytes_FromList` | unknown |
| 0.39% | `python` | `_PyThreadState_PopFrame` | interpreter |
| 0.38% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.35% | `python` | `PyNumber_And` | dynamic |
| 0.32% | `python` | `PySlice_Unpack` | miscobj |
| 0.29% | `python` | `gc_collect_region.isra.0` | gc |
| 0.28% | `python` | `list_subscript` | list |
| 0.28% | `python` | `PyObject_Malloc` | dynamic |
| 0.27% | `libc-2.31.so` | `malloc` | libc |
| 0.27% | `python` | `gallop_right` | unknown |

## pylint

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 17.43% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 14.43% | `python` | `gc_collect_region.isra.0` | gc |
| 6.67% | `[JIT]` | `jit` | jit |
| 3.92% | `python` | `visit_decref` | gc |
| 3.16% | `python` | `visit_reachable` | gc |
| 2.61% | `python` | `_PyObject_Malloc` | memory |
| 2.57% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 2.19% | `python` | `_PyType_LookupRef` | lookup |
| 2.02% | `python` | `visit_add_to_container` | gc |
| 2.01% | `python` | `_PyObject_Free` | memory |
| 1.72% | `python` | `_Py_dict_lookup` | lookup |
| 1.33% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.23% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.10% | `python` | `initialize_locals` | interpreter |
| 0.93% | `python` | `dict_traverse` | gc |
| 0.86% | `python` | `PyObject_VisitManagedDict` | dynamic |
| 0.81% | `python` | `list_traverse` | gc |
| 0.80% | `python` | `PyDict_GetItemRef` | dict |
| 0.66% | `python` | `PyObject_GenericGetAttr` | dynamic |
| 0.64% | `python` | `tupledealloc` | memory |
| 0.61% | `python` | `dict_dealloc` | memory |
| 0.57% | `python` | `subtype_traverse` | gc |
| 0.57% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.55% | `python` | `PyType_IsSubtype` | dynamic |
| 0.47% | `python` | `PyObject_GetAttr` | dynamic |
| 0.45% | `python` | `_PyGC_Collect` | gc |
| 0.44% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.43% | `python` | `insertdict` | dict |
| 0.42% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.41% | `python` | `_PyObject_GetMethod` | dynamic |
| 0.41% | `python` | `_PyPegen_is_memoized` | interpreter |
| 0.41% | `python` | `_Py_Dealloc` | memory |
| 0.39% | `python` | `_PyObject_GenericGetAttrWithDict` | dynamic |
| 0.36% | `python` | `PyObject_GC_Del` | gc |
| 0.35% | `python` | `islice_next` | unknown |
| 0.35% | `python` | `list_dealloc` | memory |
| 0.31% | `python` | `PyObject_IS_GC` | gc |
| 0.30% | `python` | `_PyObject_TryGetInstanceAttribute` | dynamic |
| 0.30% | `python` | `PyObject_ClearManagedDict` | dynamic |
| 0.28% | `python` | `_PyObject_GC_New` | gc |
| 0.27% | `python` | `PyType_GenericAlloc` | memory |
| 0.27% | `libc-2.31.so` | `pthread_attr_setschedparam` | libc |
| 0.26% | `python` | `find_name_in_mro` | lookup |

## python_startup

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 7.42% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 5.47% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 4.34% | `python` | `gc_collect_region.isra.0` | gc |
| 3.47% | `python` | `_PyObject_Malloc` | memory |
| 3.10% | `python` | `_Py_dict_lookup` | lookup |
| 3.08% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 2.60% | `python` | `visit_decref` | gc |
| 2.01% | `ld-2.31.so` | `_dl_rtld_di_serinfo` | library |
| 1.97% | `python` | `visit_reachable` | gc |
| 1.73% | `python` | `_PyObject_Free` | memory |
| 1.63% | `python` | `r_object` | import |
| 1.47% | `python` | `type_ready` | dynamic |
| 1.44% | `python` | `siphash13` | str |
| 1.43% | `python` | `update_one_slot` | lookup |
| 1.34% | `python` | `find_name_in_mro` | lookup |
| 1.26% | `python` | `_Py_hashtable_get_entry_generic` | lookup |
| 0.96% | `python` | `_PyType_LookupRef` | lookup |
| 0.94% | `python` | `_PyCode_Quicken` | interpreter |
| 0.90% | `libc-2.31.so` | `pthread_attr_setschedparam` | libc |
| 0.87% | `python` | `tupledealloc` | memory |
| 0.86% | `python` | `ascii_decode` | str |
| 0.76% | `python` | `dict_traverse` | gc |
| 0.74% | `python` | `_PyUnicode_FromUCS1.part.0` | str |
| 0.74% | `python` | `insertdict` | dict |
| 0.68% | `[kernel.kallsyms]` | `native_irq_return_iret` | kernel |
| 0.63% | `[kernel.kallsyms]` | `filemap_map_pages` | kernel |
| 0.59% | `python` | `_PyDict_GetItemRef_KnownHash` | dict |
| 0.57% | `python` | `intern_constants` | str |
| 0.56% | `[kernel.kallsyms]` | `sync_regs` | kernel |
| 0.55% | `python` | `dict_setdefault_ref_lock_held` | dict |
| 0.51% | `libc-2.31.so` | `wcsrtombs` | libc |
| 0.50% | `libc-2.31.so` | `__gconv_get_alias_db` | libc |
| 0.49% | `python` | `build_indices_unicode` | dict |
| 0.45% | `python` | `dict_dealloc` | memory |
| 0.45% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 0.44% | `python` | `_Py_GetBaseOpcode` | interpreter |
| 0.43% | `python` | `intern_common.part.0` | str |
| 0.43% | `[kernel.kallsyms]` | `clear_page_erms` | kernel |
| 0.43% | `ld-2.31.so` | `_dl_catch_error` | library |
| 0.42% | `python` | `PyObject_IS_GC` | gc |
| 0.42% | `python` | `_Py_Dealloc` | memory |
| 0.40% | `python` | `PyDict_GetItemRef` | dict |
| 0.38% | `python` | `PyUnicode_New.part.0` | memory |
| 0.38% | `python` | `find_empty_slot` | dict |
| 0.35% | `python` | `initialize_locals` | interpreter |
| 0.34% | `[kernel.kallsyms]` | `zap_pte_range.isra.0` | kernel |
| 0.33% | `python` | `_PyCode_New` | interpreter |
| 0.32% | `python` | `list_dealloc` | memory |
| 0.31% | `python` | `PyType_GenericAlloc` | memory |
| 0.31% | `[kernel.kallsyms]` | `__handle_mm_fault` | kernel |
| 0.30% | `python` | `code_dealloc` | memory |
| 0.27% | `python` | `tupletraverse` | tuple |
| 0.27% | `python` | `_PyUnicode_InternImmortal` | str |
| 0.27% | `python` | `func_traverse` | gc |
| 0.27% | `python` | `unicode_decode_utf8.part.0` | str |
| 0.26% | `[kernel.kallsyms]` | `rmqueue` | kernel |
| 0.26% | `python` | `PyObject_GC_Del` | gc |
| 0.26% | `python` | `set_traverse` | gc |

## python_startup_no_site

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 6.85% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 4.83% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 4.46% | `python` | `gc_collect_region.isra.0` | gc |
| 3.37% | `python` | `_PyObject_Malloc` | memory |
| 3.09% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 2.84% | `ld-2.31.so` | `_dl_rtld_di_serinfo` | library |
| 2.70% | `python` | `_Py_dict_lookup` | lookup |
| 2.44% | `python` | `visit_decref` | gc |
| 1.92% | `python` | `visit_reachable` | gc |
| 1.86% | `python` | `type_ready` | dynamic |
| 1.73% | `python` | `_PyObject_Free` | memory |
| 1.49% | `python` | `siphash13` | str |
| 1.38% | `python` | `_Py_hashtable_get_entry_generic` | lookup |
| 1.24% | `python` | `update_one_slot` | lookup |
| 1.21% | `python` | `r_object` | import |
| 1.13% | `python` | `find_name_in_mro` | lookup |
| 1.06% | `python` | `ascii_decode` | str |
| 0.88% | `[kernel.kallsyms]` | `native_irq_return_iret` | kernel |
| 0.87% | `python` | `_PyType_LookupRef` | lookup |
| 0.83% | `libc-2.31.so` | `pthread_attr_setschedparam` | libc |
| 0.82% | `python` | `dict_traverse` | gc |
| 0.81% | `python` | `_PyCode_Quicken` | interpreter |
| 0.78% | `python` | `tupledealloc` | memory |
| 0.72% | `python` | `insertdict` | dict |
| 0.70% | `[kernel.kallsyms]` | `filemap_map_pages` | kernel |
| 0.69% | `libc-2.31.so` | `__gconv_get_alias_db` | libc |
| 0.62% | `[kernel.kallsyms]` | `sync_regs` | kernel |
| 0.61% | `libc-2.31.so` | `wcsrtombs` | libc |
| 0.59% | `python` | `_PyUnicode_FromUCS1.part.0` | str |
| 0.59% | `ld-2.31.so` | `_dl_catch_error` | library |
| 0.58% | `python` | `dict_setdefault_ref_lock_held` | dict |
| 0.52% | `python` | `intern_constants` | str |
| 0.51% | `[kernel.kallsyms]` | `clear_page_erms` | kernel |
| 0.48% | `python` | `_PyDict_GetItemRef_KnownHash` | dict |
| 0.48% | `python` | `intern_common.part.0` | str |
| 0.45% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 0.45% | `python` | `build_indices_unicode` | dict |
| 0.44% | `python` | `_Py_Dealloc` | memory |
| 0.44% | `[kernel.kallsyms]` | `copy_page` | kernel |
| 0.43% | `python` | `dict_dealloc` | memory |
| 0.40% | `python` | `initialize_locals` | interpreter |
| 0.40% | `python` | `PyType_GenericAlloc` | memory |
| 0.39% | `python` | `PyObject_IS_GC` | gc |
| 0.39% | `[kernel.kallsyms]` | `zap_pte_range.isra.0` | kernel |
| 0.37% | `python` | `PyUnicode_New.part.0` | memory |
| 0.37% | `python` | `find_empty_slot` | dict |
| 0.36% | `python` | `PyDict_GetItemRef` | dict |
| 0.35% | `[kernel.kallsyms]` | `__handle_mm_fault` | kernel |
| 0.35% | `python` | `_Py_GetBaseOpcode` | interpreter |
| 0.34% | `[JIT]` | `jit` | jit |
| 0.33% | `[kernel.kallsyms]` | `rmqueue` | kernel |
| 0.31% | `python` | `unicode_decode_utf8.part.0` | str |
| 0.28% | `[kernel.kallsyms]` | `release_pages` | kernel |
| 0.28% | `python` | `PyObject_GC_Del` | gc |
| 0.26% | `python` | `func_traverse` | gc |
| 0.26% | `python` | `unicode_dealloc` | memory |
| 0.26% | `python` | `code_dealloc` | memory |

## raytrace

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 41.63% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 11.09% | `[JIT]` | `jit` | jit |
| 4.17% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 2.50% | `python` | `_PyObject_Free` | memory |
| 2.25% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.87% | `python` | `_PyObject_Malloc` | memory |
| 1.61% | `python` | `float_dealloc` | memory |
| 1.44% | `python` | `subtype_dealloc` | memory |
| 1.36% | `python` | `PyType_IsSubtype` | dynamic |
| 1.31% | `python` | `_Py_Dealloc` | memory |
| 1.12% | `python` | `_PyType_NewManagedObject` | memory |
| 1.08% | `python` | `PyObject_ClearManagedDict` | dynamic |
| 1.06% | `python` | `PyFloat_FromDouble` | float |
| 1.05% | `python` | `_PyThreadState_PopFrame` | interpreter |
| 1.03% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 0.95% | `python` | `PyNumber_Subtract` | dynamic |
| 0.90% | `python` | `_PyType_LookupRef` | lookup |
| 0.89% | `python` | `float_sub` | float |
| 0.84% | `python` | `_Py_NewReference` | memory |
| 0.71% | `python` | `PyLong_AsDouble` | int |
| 0.71% | `python` | `float_mul` | float |
| 0.66% | `python` | `initialize_locals` | interpreter |
| 0.63% | `python` | `PyObject_GC_Del` | gc |
| 0.57% | `python` | `PyNumber_Multiply` | dynamic |
| 0.57% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.56% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.51% | `python` | `tupledealloc` | memory |
| 0.48% | `python` | `_PyFloat_ExactDealloc` | memory |
| 0.46% | `python` | `float_richcompare` | float |
| 0.46% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.46% | `python` | `PyObject_ClearWeakRefs` | dynamic |
| 0.44% | `python` | `gc_collect_region.isra.0` | gc |
| 0.44% | `python` | `vectorcall_maybe.constprop.0` | unknown |
| 0.36% | `python` | `_PyTuple_FromStackRefSteal` | tuple |
| 0.33% | `python` | `slot_nb_subtract` | unknown |
| 0.31% | `python` | `_PyEval_Vector` | interpreter |
| 0.29% | `python` | `_Py_dict_lookup` | lookup |
| 0.27% | `python` | `float_add` | float |
| 0.26% | `python` | `PyNumber_Add` | dynamic |

## regex_compile

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 19.28% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 18.82% | `[JIT]` | `jit` | jit |
| 3.74% | `python` | `_PyObject_Malloc` | memory |
| 3.63% | `python` | `sre_ucs1_match` | library |
| 3.38% | `python` | `_PyObject_Free` | memory |
| 2.03% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.61% | `python` | `_PyType_LookupRef` | lookup |
| 1.33% | `python` | `PyNumber_AsSsize_t` | dynamic |
| 1.29% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.18% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.92% | `python` | `_Py_Dealloc` | memory |
| 0.87% | `python` | `bytearray_ass_subscript` | miscobj |
| 0.85% | `python` | `_Py_dict_lookup` | lookup |
| 0.78% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.75% | `python` | `PyLong_FromLong` | int |
| 0.75% | `python` | `tupledealloc` | memory |
| 0.73% | `python` | `gc_collect_region.isra.0` | gc |
| 0.72% | `python` | `sre_ucs2_charset.isra.0` | library |
| 0.72% | `python` | `initialize_locals` | interpreter |
| 0.67% | `python` | `_PyTuple_FromStackRefSteal` | tuple |
| 0.55% | `python` | `PyUnicode_Contains` | str |
| 0.52% | `python` | `sre_search` | library |
| 0.52% | `python` | `list_dealloc` | memory |
| 0.49% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.47% | `python` | `PyObject_GC_Del` | gc |
| 0.46% | `python` | `PyObject_GetAttr` | dynamic |
| 0.45% | `python` | `PyObject_GenericGetAttr` | dynamic |
| 0.44% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.42% | `python` | `_PyObject_GenericGetAttrWithDict` | dynamic |
| 0.42% | `libc-2.31.so` | `pthread_attr_setschedparam` | libc |
| 0.42% | `python` | `_PyObject_Realloc` | memory |
| 0.41% | `python` | `_PyLong_Add` | int |
| 0.40% | `python` | `list_append` | list |
| 0.40% | `python` | `_PyObject_GC_New` | gc |
| 0.39% | `python` | `PyObject_SetItem` | dynamic |
| 0.38% | `python` | `PyType_IsSubtype` | dynamic |
| 0.35% | `python` | `PyLong_AsLongAndOverflow` | int |
| 0.35% | `python` | `visit_decref` | gc |
| 0.34% | `python` | `siphash13` | str |
| 0.34% | `python` | `_PyUnicode_Equal` | str |
| 0.34% | `python` | `set_lookkey` | miscobj |
| 0.33% | `python` | `PyObject_GetItem` | dynamic |
| 0.32% | `python` | `PyLong_AsSsize_t` | int |
| 0.32% | `python` | `_Py_NewReference` | memory |
| 0.32% | `python` | `min_max` | unknown |
| 0.31% | `python` | `sre_ucs1_count` | library |
| 0.31% | `python` | `PyList_New` | memory |
| 0.30% | `python` | `_PyEval_Vector` | interpreter |
| 0.30% | `python` | `PyObject_IsTrue` | dynamic |
| 0.28% | `python` | `_PyType_GetDict` | dynamic |
| 0.28% | `python` | `PyDict_GetItemRef` | dict |
| 0.27% | `python` | `visit_reachable` | gc |
| 0.27% | `python` | `r_object` | import |
| 0.26% | `python` | `_PyThreadState_PopFrame` | interpreter |
| 0.25% | `python` | `PyObject_GetOptionalAttr` | dynamic |

## regex_dna

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 34.84% | `python` | `sre_ucs1_match` | library |
| 26.60% | `python` | `sre_ucs2_charset.isra.0` | library |
| 8.28% | `python` | `sre_search` | library |
| 3.98% | `[JIT]` | `jit` | jit |
| 3.35% | `libm-2.31.so` | `__fmod_finite` | library |
| 1.48% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 1.45% | `_bisect.cpython-314-x86_64-linux-gnu.so` | `_bisect_bisect_right` | library |
| 1.21% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.09% | `python` | `pattern_subx` | library |
| 0.73% | `python` | `float_rem` | float |
| 0.69% | `python` | `float_richcompare` | float |
| 0.68% | `python` | `_PyObject_Malloc` | memory |
| 0.60% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.56% | `python` | `float_dealloc` | memory |
| 0.50% | `python` | `gc_collect_region.isra.0` | gc |
| 0.45% | `python` | `_PyObject_Free` | memory |
| 0.45% | `python` | `stringlib_bytes_join` | str |
| 0.38% | `python` | `list_item` | list |
| 0.36% | `python` | `_Py_Dealloc` | memory |
| 0.34% | `python` | `bytearray_ass_subscript` | miscobj |
| 0.33% | `python` | `float_div` | float |
| 0.32% | `python` | `_Py_dict_lookup` | lookup |
| 0.31% | `libc-2.31.so` | `pthread_attr_setschedparam` | libc |
| 0.27% | `python` | `visit_decref` | gc |
| 0.25% | `python` | `PyBuffer_Release` | miscobj |

## regex_effbot

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 40.12% | `python` | `sre_ucs1_match` | library |
| 14.40% | `python` | `sre_ucs2_charset.isra.0` | library |
| 7.46% | `python` | `_PyObject_Free` | memory |
| 6.91% | `python` | `sre_search` | library |
| 5.05% | `python` | `_PyObject_Malloc` | memory |
| 3.21% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 2.19% | `python` | `sre_ucs1_count` | library |
| 1.05% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.88% | `python` | `PyMem_Malloc` | memory |
| 0.84% | `python` | `gc_collect_region.isra.0` | gc |
| 0.71% | `python` | `_Py_dict_lookup` | lookup |
| 0.69% | `[JIT]` | `jit` | jit |
| 0.56% | `python` | `siphash13` | str |
| 0.55% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 0.47% | `python` | `PyMem_Free` | memory |
| 0.47% | `python` | `visit_decref` | gc |
| 0.39% | `libc-2.31.so` | `pthread_attr_setschedparam` | libc |
| 0.37% | `python` | `r_object` | import |
| 0.36% | `python` | `visit_reachable` | gc |
| 0.33% | `python` | `_PyType_LookupRef` | lookup |

## regex_v8

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 35.18% | `python` | `sre_ucs1_match` | library |
| 4.97% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 4.09% | `python` | `PyCode_Addr2Line` | exceptions |
| 4.07% | `python` | `sre_ucs1_count` | library |
| 3.98% | `python` | `sre_search` | library |
| 2.99% | `python` | `_PyObject_Malloc` | memory |
| 2.79% | `python` | `_PyObject_Free` | memory |
| 2.78% | `[JIT]` | `jit` | jit |
| 1.78% | `libc-2.31.so` | `pthread_attr_setschedparam` | libc |
| 1.67% | `python` | `pattern_subx` | library |
| 1.32% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 1.32% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.10% | `python` | `pattern_new_match.isra.0.part.0` | memory |
| 1.01% | `python` | `_sre_SRE_Pattern_search` | library |
| 1.00% | `python` | `_Py_dict_lookup` | lookup |
| 0.87% | `python` | `gc_collect_region.isra.0` | gc |
| 0.62% | `libc-2.31.so` | `malloc` | libc |
| 0.50% | `python` | `visit_decref` | gc |
| 0.48% | `python` | `_PyUnicode_IsAlpha` | str |
| 0.47% | `python` | `_PyUnicode_JoinArray.part.0` | str |
| 0.45% | `python` | `_PyUnicode_ToLowercase` | str |
| 0.43% | `python` | `r_object` | import |
| 0.42% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 0.41% | `python` | `_PyType_LookupRef` | lookup |
| 0.40% | `python` | `PyNumber_AsSsize_t` | dynamic |
| 0.39% | `python` | `_Py_Dealloc` | memory |
| 0.37% | `python` | `visit_reachable` | gc |
| 0.36% | `python` | `PyDict_GetItemRef` | dict |
| 0.34% | `python` | `PyLong_FromLong` | int |
| 0.34% | `python` | `PyUnicode_Contains` | str |
| 0.34% | `python` | `_PyPegen_is_memoized` | interpreter |
| 0.33% | `python` | `PyList_Append` | list |
| 0.33% | `python` | `_PyObject_Realloc` | memory |
| 0.31% | `python` | `list_dealloc` | memory |
| 0.29% | `python` | `find_name_in_mro` | lookup |
| 0.28% | `python` | `PyUnicode_Substring` | str |
| 0.28% | `python` | `tupledealloc` | memory |
| 0.27% | `python` | `siphash13` | str |
| 0.26% | `python` | `sre_ucs2_charset.isra.0` | library |

## richards

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 37.79% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 22.67% | `[JIT]` | `jit` | jit |
| 4.47% | `python` | `_PyType_LookupRef` | lookup |
| 3.88% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 3.76% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 2.14% | `python` | `_PyObject_TryGetInstanceAttribute` | dynamic |
| 1.96% | `python` | `_PyObject_GetMethod` | dynamic |
| 1.90% | `python` | `PyObject_GenericGetAttr` | dynamic |
| 1.87% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.58% | `python` | `PyObject_GetAttr` | dynamic |
| 1.14% | `python` | `_PyObject_Free` | memory |
| 0.98% | `python` | `_PyObject_Malloc` | memory |
| 0.93% | `python` | `_PyThreadState_PopFrame` | interpreter |
| 0.67% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 0.57% | `python` | `initialize_locals` | interpreter |
| 0.53% | `python` | `gc_collect_region.isra.0` | gc |
| 0.49% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.48% | `python` | `PyObject_GenericSetAttr` | dynamic |
| 0.42% | `python` | `_PyLong_Add` | int |
| 0.41% | `python` | `PyObject_SetAttr` | dynamic |
| 0.39% | `python` | `_Py_dict_lookup` | lookup |
| 0.33% | `python` | `store_instance_attr_lock_held` | unknown |
| 0.33% | `python` | `_PyType_GetDict` | dynamic |
| 0.28% | `python` | `visit_decref` | gc |

## richards_super

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 35.31% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 17.54% | `[JIT]` | `jit` | jit |
| 4.19% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 4.08% | `python` | `_PyType_LookupRef` | lookup |
| 3.31% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.79% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.59% | `python` | `_PyObject_TryGetInstanceAttribute` | dynamic |
| 1.58% | `python` | `_PyObject_GetMethod` | dynamic |
| 1.47% | `python` | `PyObject_GenericGetAttr` | dynamic |
| 1.36% | `python` | `PyObject_GetAttr` | dynamic |
| 1.19% | `python` | `_PyObject_Malloc` | memory |
| 1.18% | `python` | `_PyObject_Free` | memory |
| 0.99% | `python` | `_Py_dict_lookup` | lookup |
| 0.96% | `python` | `PyDict_GetItemRef` | dict |
| 0.94% | `python` | `gc_collect_region.isra.0` | gc |
| 0.93% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 0.84% | `python` | `_PyThreadState_PopFrame` | interpreter |
| 0.69% | `python` | `PyObject_SetAttr` | dynamic |
| 0.64% | `python` | `PyObject_GenericSetAttr` | dynamic |
| 0.62% | `python` | `store_instance_attr_lock_held` | unknown |
| 0.59% | `python` | `do_super_lookup` | dynamic |
| 0.59% | `python` | `visit_decref` | gc |
| 0.52% | `python` | `initialize_locals` | interpreter |
| 0.43% | `python` | `visit_reachable` | gc |
| 0.39% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.39% | `python` | `_PySuper_Lookup` | dynamic |
| 0.35% | `python` | `r_object` | import |
| 0.29% | `python` | `_PyType_GetDict` | dynamic |
| 0.28% | `python` | `_PyLong_Add` | int |
| 0.27% | `python` | `_Py_hashtable_get_entry_generic` | lookup |
| 0.26% | `libc-2.31.so` | `pthread_attr_setschedparam` | libc |

## scimark

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 18.12% | `[JIT]` | `jit` | jit |
| 14.72% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 5.44% | `python` | `PyNumber_AsSsize_t` | dynamic |
| 5.10% | `python` | `_PyObject_Free` | memory |
| 4.04% | `python` | `_PyObject_Malloc` | memory |
| 3.77% | `array.cpython-314-x86_64-linux-gnu.so` | `array_subscr` | library |
| 2.89% | `python` | `PyFloat_FromDouble` | float |
| 2.45% | `python` | `vgetargs1_impl` | calls |
| 2.44% | `python` | `PyObject_GetItem` | dynamic |
| 1.91% | `python` | `_PyLong_Add` | int |
| 1.88% | `python` | `PyLong_AsSsize_t` | int |
| 1.87% | `python` | `_Py_Dealloc` | memory |
| 1.73% | `python` | `convertitem.constprop.0` | library |
| 1.42% | `python` | `_PyType_LookupRef` | lookup |
| 1.30% | `array.cpython-314-x86_64-linux-gnu.so` | `array_ass_subscr` | library |
| 1.29% | `python` | `float_dealloc` | memory |
| 1.16% | `python` | `PyLong_FromLong` | int |
| 1.12% | `python` | `_Py_NewReference` | memory |
| 1.04% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 0.90% | `python` | `PyType_GetModuleByDef` | dynamic |
| 0.88% | `python` | `PyIndex_Check` | unknown |
| 0.85% | `python` | `initialize_locals` | interpreter |
| 0.84% | `array.cpython-314-x86_64-linux-gnu.so` | `d_setitem` | library |
| 0.78% | `python` | `_PyLong_Multiply` | int |
| 0.77% | `python` | `PyArg_Parse` | calls |
| 0.75% | `python` | `long_dealloc` | memory |
| 0.73% | `python` | `slot_mp_subscript` | unknown |
| 0.72% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.69% | `python` | `PyObject_SetItem` | dynamic |
| 0.66% | `python` | `_PyFloat_ExactDealloc` | memory |
| 0.59% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.58% | `python` | `_PyEval_Vector` | interpreter |
| 0.54% | `python` | `PyType_IsSubtype` | dynamic |
| 0.51% | `array.cpython-314-x86_64-linux-gnu.so` | `d_getitem` | library |
| 0.51% | `python` | `_PyObject_GenericGetAttrWithDict` | dynamic |
| 0.47% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 0.45% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.44% | `python` | `_PyTuple_FromStackRefSteal` | tuple |
| 0.44% | `python` | `tupledealloc` | memory |
| 0.40% | `python` | `_PyLong_Frexp` | int |
| 0.37% | `python` | `_PyLong_Subtract` | int |
| 0.34% | `array.cpython-314-x86_64-linux-gnu.so` | `0x0000000000004644` | library |
| 0.33% | `array.cpython-314-x86_64-linux-gnu.so` | `0x00000000000047e4` | library |
| 0.33% | `python` | `float_richcompare` | float |
| 0.32% | `array.cpython-314-x86_64-linux-gnu.so` | `0x00000000000049c4` | library |
| 0.31% | `python` | `gc_collect_region.isra.0` | gc |
| 0.28% | `python` | `PyObject_Malloc` | dynamic |
| 0.27% | `python` | `object_isinstance` | dynamic |
| 0.26% | `python` | `_PyThreadState_PopFrame` | interpreter |

## spectral_norm

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 23.04% | `[JIT]` | `jit` | jit |
| 10.26% | `python` | `_PyObject_Free` | memory |
| 9.09% | `python` | `_PyLong_Add` | int |
| 7.17% | `python` | `_PyObject_Malloc` | memory |
| 3.21% | `python` | `_PyLong_Multiply` | int |
| 2.95% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 2.83% | `python` | `float_div` | float |
| 2.32% | `python` | `long_div` | int |
| 2.00% | `python` | `listiter_next` | list |
| 1.94% | `python` | `_Py_Dealloc` | memory |
| 1.87% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.66% | `python` | `PyType_IsSubtype` | dynamic |
| 1.62% | `python` | `enum_next` | miscobj |
| 1.48% | `python` | `_Py_NewReference` | memory |
| 1.43% | `python` | `PyLong_FromLong` | int |
| 1.36% | `python` | `PyNumber_TrueDivide` | dynamic |
| 1.18% | `python` | `float_dealloc` | memory |
| 1.11% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.99% | `python` | `long_dealloc` | memory |
| 0.92% | `python` | `PyNumber_FloorDivide` | dynamic |
| 0.91% | `python` | `PyLong_AsDouble` | int |
| 0.89% | `python` | `float_mul` | float |
| 0.86% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.78% | `python` | `PyLong_FromSsize_t` | int |
| 0.75% | `python` | `gc_collect_region.isra.0` | gc |
| 0.64% | `python` | `PyObject_Malloc` | dynamic |
| 0.62% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 0.58% | `python` | `PyNumber_Multiply` | dynamic |
| 0.54% | `python` | `_Py_dict_lookup` | lookup |
| 0.52% | `python` | `PyObject_Free` | dynamic |
| 0.50% | `python` | `_PyThreadState_PopFrame` | interpreter |
| 0.45% | `python` | `visit_decref` | gc |
| 0.39% | `python` | `visit_reachable` | gc |
| 0.34% | `python` | `r_object` | import |
| 0.26% | `libc-2.31.so` | `pthread_attr_setschedparam` | libc |
| 0.25% | `python` | `tupledealloc` | memory |
| 0.25% | `python` | `_PyCode_Quicken` | interpreter |

## sqlglot

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 20.09% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 11.14% | `[JIT]` | `jit` | jit |
| 4.29% | `python` | `_PyObject_Free` | memory |
| 4.24% | `python` | `_PyObject_Malloc` | memory |
| 2.54% | `python` | `_PyType_LookupRef` | lookup |
| 1.99% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 1.82% | `python` | `PyType_IsSubtype` | dynamic |
| 1.73% | `python` | `tupledealloc` | memory |
| 1.58% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.36% | `python` | `_PyObject_GenericGetAttrWithDict` | dynamic |
| 1.33% | `python` | `_Py_dict_lookup` | lookup |
| 1.31% | `python` | `dictiter_iternextitem` | dict |
| 1.21% | `python` | `_PyObject_LookupSpecial` | dynamic |
| 1.16% | `python` | `PyObject_GC_Del` | gc |
| 1.16% | `python` | `gc_collect_region.isra.0` | gc |
| 1.15% | `python` | `_PyTuple_FromStackRefSteal` | tuple |
| 1.10% | `python` | `PyObject_IsInstance` | dynamic |
| 1.02% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 0.94% | `python` | `_PyObject_GC_New` | gc |
| 0.87% | `python` | `object_isinstance` | dynamic |
| 0.86% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.85% | `python` | `_Py_Dealloc` | memory |
| 0.76% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.70% | `python` | `PyObject_GetOptionalAttr` | dynamic |
| 0.66% | `python` | `initialize_locals` | interpreter |
| 0.62% | `python` | `visit_decref` | gc |
| 0.56% | `python` | `PyObject_GetAttr` | dynamic |
| 0.55% | `python` | `insert_to_emptydict` | dict |
| 0.54% | `python` | `_PyObject_GC_Link` | gc |
| 0.53% | `python` | `PyCMethod_New` | memory |
| 0.50% | `python` | `PyObject_GenericGetAttr` | dynamic |
| 0.49% | `python` | `_PyObject_RealIsInstance` | dynamic |
| 0.49% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.49% | `python` | `_PyObject_Calloc` | memory |
| 0.47% | `python` | `getset_get` | dynamic |
| 0.47% | `python` | `visit_reachable` | gc |
| 0.47% | `python` | `siphash13` | str |
| 0.45% | `python` | `_Py_NewReference` | memory |
| 0.43% | `python` | `PyFunction_NewWithQualName` | memory |
| 0.43% | `python` | `PyTuple_Pack` | tuple |
| 0.41% | `python` | `dict_dealloc` | memory |
| 0.40% | `python` | `PyObject_CallOneArg` | dynamic |
| 0.37% | `python` | `r_object` | import |
| 0.37% | `python` | `meth_dealloc` | memory |
| 0.35% | `python` | `list_dealloc` | memory |
| 0.35% | `python` | `gen_dealloc` | memory |
| 0.34% | `python` | `PyList_New` | memory |
| 0.34% | `python` | `find_name_in_mro` | lookup |
| 0.33% | `python` | `update_one_slot` | lookup |
| 0.32% | `python` | `cfunction_vectorcall_O` | calls |
| 0.32% | `python` | `_PyThreadState_PopFrame` | interpreter |
| 0.31% | `python` | `_PyObject_GC_NewVar` | gc |
| 0.30% | `python` | `_PyObject_Realloc` | memory |
| 0.30% | `python` | `PyObject_IsTrue` | dynamic |
| 0.27% | `libc-2.31.so` | `pthread_attr_setschedparam` | libc |
| 0.26% | `python` | `gen_iternext` | miscobj |
| 0.26% | `python` | `_PyCode_Quicken` | interpreter |

## sqlglot_optimize

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 18.56% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 11.31% | `[JIT]` | `jit` | jit |
| 4.19% | `python` | `_PyObject_Free` | memory |
| 4.00% | `python` | `_PyObject_Malloc` | memory |
| 3.10% | `python` | `_PyType_LookupRef` | lookup |
| 2.25% | `python` | `PyType_IsSubtype` | dynamic |
| 2.13% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 1.68% | `python` | `tupledealloc` | memory |
| 1.65% | `python` | `_PyObject_GenericGetAttrWithDict` | dynamic |
| 1.57% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.46% | `python` | `_Py_dict_lookup` | lookup |
| 1.43% | `python` | `dictiter_iternextitem` | dict |
| 1.34% | `python` | `_PyObject_LookupSpecial` | dynamic |
| 1.30% | `python` | `gc_collect_region.isra.0` | gc |
| 1.12% | `python` | `PyObject_IsInstance` | dynamic |
| 1.11% | `python` | `_PyObject_GC_New` | gc |
| 1.09% | `python` | `PyObject_GC_Del` | gc |
| 1.04% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.00% | `python` | `_PyTuple_FromStackRefSteal` | tuple |
| 0.87% | `python` | `_Py_Dealloc` | memory |
| 0.86% | `python` | `object_isinstance` | dynamic |
| 0.85% | `python` | `PyObject_GetOptionalAttr` | dynamic |
| 0.81% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.70% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.64% | `python` | `_PyObject_RealIsInstance` | dynamic |
| 0.63% | `python` | `visit_decref` | gc |
| 0.62% | `python` | `PyObject_GenericGetAttr` | dynamic |
| 0.60% | `python` | `PyObject_GetAttr` | dynamic |
| 0.58% | `python` | `initialize_locals` | interpreter |
| 0.57% | `python` | `PyCMethod_New` | memory |
| 0.54% | `python` | `PyObject_CallOneArg` | dynamic |
| 0.51% | `python` | `_PyObject_Calloc` | memory |
| 0.49% | `python` | `getset_get` | dynamic |
| 0.48% | `python` | `_PyObject_GC_Link` | gc |
| 0.45% | `python` | `siphash13` | str |
| 0.44% | `python` | `visit_reachable` | gc |
| 0.44% | `python` | `meth_dealloc` | memory |
| 0.43% | `python` | `PyList_New` | memory |
| 0.40% | `python` | `insert_to_emptydict` | dict |
| 0.39% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.39% | `python` | `list_dealloc` | memory |
| 0.39% | `python` | `dict_dealloc` | memory |
| 0.39% | `python` | `_Py_NewReference` | memory |
| 0.38% | `python` | `tuplehash` | tuple |
| 0.37% | `python` | `update_one_slot` | lookup |
| 0.36% | `python` | `PyTuple_Pack` | tuple |
| 0.35% | `python` | `insertdict` | dict |
| 0.35% | `python` | `r_object` | import |
| 0.34% | `python` | `find_name_in_mro` | lookup |
| 0.34% | `python` | `cfunction_vectorcall_O` | calls |
| 0.32% | `python` | `PyFunction_NewWithQualName` | memory |
| 0.31% | `python` | `PyMember_GetOne` | lookup |
| 0.31% | `python` | `_PyType_GetDict` | dynamic |
| 0.29% | `python` | `object_recursive_isinstance` | dynamic |
| 0.29% | `python` | `_PyThreadState_PopFrame` | interpreter |
| 0.28% | `python` | `PyObject_IsTrue` | dynamic |
| 0.28% | `python` | `PyObject_Hash` | dynamic |
| 0.27% | `python` | `PyDescr_IsData` | dynamic |
| 0.27% | `python` | `method_get` | dynamic |
| 0.26% | `python` | `dict_get` | dict |

## sqlglot_parse

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 23.98% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 19.61% | `[JIT]` | `jit` | jit |
| 2.96% | `python` | `_PyObject_Malloc` | memory |
| 2.92% | `python` | `_PyType_LookupRef` | lookup |
| 2.72% | `python` | `_PyObject_Free` | memory |
| 2.47% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 2.20% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 2.08% | `python` | `_Py_dict_lookup` | lookup |
| 1.96% | `python` | `gc_collect_region.isra.0` | gc |
| 1.84% | `python` | `initialize_locals` | interpreter |
| 1.04% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.01% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 0.92% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.83% | `python` | `visit_decref` | gc |
| 0.79% | `python` | `PyObject_GetAttr` | dynamic |
| 0.70% | `python` | `_PyLong_Add` | int |
| 0.69% | `python` | `PyObject_RichCompare` | dynamic |
| 0.63% | `python` | `_Py_Dealloc` | memory |
| 0.61% | `python` | `PyType_IsSubtype` | dynamic |
| 0.55% | `python` | `dict_dealloc` | memory |
| 0.52% | `python` | `tupledealloc` | memory |
| 0.48% | `python` | `_Py_type_getattro` | lookup |
| 0.44% | `python` | `_PyThreadState_PopFrame` | interpreter |
| 0.42% | `python` | `visit_reachable` | gc |
| 0.42% | `python` | `dictiter_iternextitem` | dict |
| 0.41% | `python` | `_PyObject_GC_New` | gc |
| 0.38% | `python` | `subtype_dealloc` | memory |
| 0.37% | `python` | `insert_to_emptydict` | dict |
| 0.37% | `python` | `_PyLong_Subtract` | int |
| 0.37% | `python` | `PyObject_GC_Del` | gc |
| 0.35% | `python` | `find_name_in_mro` | lookup |
| 0.33% | `python` | `dict_get` | dict |
| 0.32% | `python` | `dict_traverse` | gc |
| 0.32% | `python` | `PyObject_GenericGetAttr` | dynamic |
| 0.31% | `python` | `_PyObject_LookupSpecial` | dynamic |
| 0.31% | `python` | `PyObject_IsTrue` | dynamic |
| 0.30% | `python` | `_Py_NewReference` | memory |
| 0.30% | `python` | `subtype_traverse` | gc |
| 0.30% | `python` | `PyLong_FromSsize_t` | int |
| 0.30% | `python` | `r_object` | import |
| 0.29% | `python` | `insertdict` | dict |
| 0.29% | `python` | `siphash13` | str |
| 0.28% | `python` | `_PyThreadState_PushFrame` | interpreter |
| 0.28% | `python` | `PyNumber_AsSsize_t` | dynamic |
| 0.28% | `python` | `update_one_slot` | lookup |
| 0.28% | `python` | `PyObject_RichCompareBool` | dynamic |
| 0.27% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.26% | `python` | `PyObject_SetAttr` | dynamic |
| 0.26% | `python` | `PyDict_Contains` | dict |
| 0.26% | `python` | `_PyEval_Vector` | interpreter |

## sqlglot_transpile

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 21.69% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 16.88% | `[JIT]` | `jit` | jit |
| 3.26% | `python` | `_PyObject_Malloc` | memory |
| 3.04% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 2.82% | `python` | `_PyObject_Free` | memory |
| 2.75% | `python` | `_PyType_LookupRef` | lookup |
| 2.28% | `python` | `_Py_dict_lookup` | lookup |
| 2.16% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 2.08% | `python` | `gc_collect_region.isra.0` | gc |
| 1.72% | `python` | `initialize_locals` | interpreter |
| 1.35% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 0.93% | `python` | `visit_decref` | gc |
| 0.89% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.88% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.81% | `python` | `PyObject_GetAttr` | dynamic |
| 0.65% | `python` | `PyType_IsSubtype` | dynamic |
| 0.65% | `python` | `tupledealloc` | memory |
| 0.60% | `python` | `_Py_Dealloc` | memory |
| 0.52% | `python` | `visit_reachable` | gc |
| 0.52% | `python` | `_PyLong_Add` | int |
| 0.49% | `python` | `dict_dealloc` | memory |
| 0.49% | `python` | `PyObject_GenericGetAttr` | dynamic |
| 0.47% | `python` | `PyObject_RichCompare` | dynamic |
| 0.47% | `python` | `dict_get` | dict |
| 0.46% | `python` | `siphash13` | str |
| 0.45% | `python` | `r_object` | import |
| 0.44% | `python` | `find_name_in_mro` | lookup |
| 0.43% | `python` | `PyObject_GC_Del` | gc |
| 0.42% | `python` | `update_one_slot` | lookup |
| 0.39% | `python` | `_Py_type_getattro` | lookup |
| 0.39% | `python` | `_PyObject_GC_New` | gc |
| 0.38% | `python` | `_PyThreadState_PopFrame` | interpreter |
| 0.35% | `python` | `dictiter_iternextitem` | dict |
| 0.34% | `libc-2.31.so` | `pthread_attr_setschedparam` | libc |
| 0.34% | `python` | `PyObject_IsTrue` | dynamic |
| 0.33% | `python` | `insertdict` | dict |
| 0.33% | `python` | `insert_to_emptydict` | dict |
| 0.32% | `python` | `_PyObject_LookupSpecial` | dynamic |
| 0.32% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.31% | `python` | `_PyObject_GenericGetAttrWithDict` | dynamic |
| 0.30% | `python` | `dict_traverse` | gc |
| 0.28% | `python` | `PyObject_IsInstance` | dynamic |
| 0.28% | `python` | `_Py_hashtable_get_entry_generic` | lookup |
| 0.28% | `python` | `subtype_dealloc` | memory |
| 0.28% | `python` | `_PyUnicode_JoinArray.part.0` | str |
| 0.27% | `python` | `_PyDict_GetItemRef_KnownHash` | dict |
| 0.27% | `python` | `PyDict_GetItemRef` | dict |
| 0.26% | `python` | `list_dealloc` | memory |
| 0.26% | `python` | `_PyCode_Quicken` | interpreter |
| 0.25% | `python` | `_PyLong_Subtract` | int |

## sympy

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 17.95% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 8.40% | `[JIT]` | `jit` | jit |
| 3.54% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 3.46% | `python` | `_PyType_LookupRef` | lookup |
| 3.20% | `python` | `_PyObject_Malloc` | memory |
| 2.65% | `python` | `_Py_dict_lookup` | lookup |
| 2.63% | `python` | `_PyObject_Free` | memory |
| 1.86% | `python` | `gc_collect_region.isra.0` | gc |
| 1.75% | `python` | `tupledealloc` | memory |
| 1.55% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.48% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.31% | `python` | `initialize_locals` | interpreter |
| 1.08% | `python` | `PyObject_RichCompareBool` | dynamic |
| 0.99% | `python` | `visit_decref` | gc |
| 0.95% | `python` | `PyType_IsSubtype` | dynamic |
| 0.79% | `python` | `_Py_Dealloc` | memory |
| 0.78% | `python` | `PyObject_GetAttr` | dynamic |
| 0.73% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.71% | `python` | `_PyObject_GenericGetAttrWithDict` | dynamic |
| 0.70% | `python` | `PyDict_GetItemRef` | dict |
| 0.69% | `python` | `visit_reachable` | gc |
| 0.63% | `python` | `_PyTuple_FromArray.part.0` | tuple |
| 0.63% | `python` | `dict_dealloc` | memory |
| 0.62% | `python` | `insertdict` | dict |
| 0.61% | `python` | `PyObject_GC_Del` | gc |
| 0.55% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.54% | `python` | `_PyObject_GC_New` | gc |
| 0.51% | `python` | `PyObject_GenericGetAttr` | dynamic |
| 0.50% | `python` | `_PyTuple_FromStackRefSteal` | tuple |
| 0.50% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.47% | `python` | `_Py_type_getattro` | lookup |
| 0.44% | `python` | `r_object` | import |
| 0.41% | `python` | `_PyPegen_is_memoized` | interpreter |
| 0.41% | `python` | `dictiter_iternextitem` | dict |
| 0.39% | `python` | `PyUnicode_RichCompare` | str |
| 0.38% | `python` | `_PyObject_LookupSpecial` | dynamic |
| 0.38% | `python` | `setiter_iternext` | miscobj |
| 0.36% | `python` | `find_name_in_mro` | lookup |
| 0.36% | `python` | `list_dealloc` | memory |
| 0.35% | `python` | `_PyCode_Quicken` | interpreter |
| 0.35% | `python` | `_PyObject_GetMethod` | dynamic |
| 0.33% | `python` | `PyObject_CallOneArg` | dynamic |
| 0.32% | `python` | `siphash13` | str |
| 0.32% | `python` | `PyTuple_New` | memory |
| 0.31% | `python` | `insert_to_emptydict` | dict |
| 0.31% | `libc-2.31.so` | `pthread_attr_setschedparam` | libc |
| 0.31% | `python` | `PyObject_GetOptionalAttr` | dynamic |
| 0.30% | `python` | `_Py_NewReference` | memory |
| 0.29% | `python` | `dict_traverse` | gc |
| 0.28% | `python` | `_PyObject_GC_Link` | gc |
| 0.26% | `python` | `_PyObject_MakeTpCall` | dynamic |

## telco

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 8.05% | `[JIT]` | `jit` | jit |
| 7.14% | `python` | `_PyObject_Malloc` | memory |
| 6.32% | `python` | `_PyObject_Free` | memory |
| 3.47% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 2.28% | `python` | `PyType_GetModuleByDef` | dynamic |
| 2.24% | `python` | `PyObject_GC_Del` | gc |
| 1.96% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.90% | `python` | `_PyObject_GC_New` | gc |
| 1.88% | `_decimal.cpython-314-x86_64-linux-gnu.so` | `nm_mpd_qadd` | library |
| 1.61% | `_decimal.cpython-314-x86_64-linux-gnu.so` | `_mpd_qaddsub` | library |
| 1.53% | `python` | `tupledealloc` | memory |
| 1.51% | `_decimal.cpython-314-x86_64-linux-gnu.so` | `_mpd_check_exp` | library |
| 1.48% | `_decimal.cpython-314-x86_64-linux-gnu.so` | `_mpd_qmul` | library |
| 1.47% | `python` | `_PyType_LookupRef` | lookup |
| 1.44% | `python` | `PyContextVar_Get` | unknown |
| 1.41% | `_decimal.cpython-314-x86_64-linux-gnu.so` | `nm_mpd_qmul` | library |
| 1.40% | `python` | `_PyArg_UnpackKeywordsWithVararg` | calls |
| 1.39% | `python` | `_Py_Dealloc` | memory |
| 1.30% | `_decimal.cpython-314-x86_64-linux-gnu.so` | `mpd_setdigits` | library |
| 1.21% | `python` | `vgetargskeywords.constprop.0` | calls |
| 1.15% | `python` | `convertitem.constprop.0` | library |
| 1.11% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 1.09% | `python` | `PyObject_GC_UnTrack` | gc |
| 1.04% | `_decimal.cpython-314-x86_64-linux-gnu.so` | `_mpd_baseshiftr` | library |
| 1.00% | `python` | `PyObject_GenericGetAttr` | dynamic |
| 0.97% | `_decimal.cpython-314-x86_64-linux-gnu.so` | `dec_addstatus` | library |
| 0.92% | `python` | `_PyTuple_FromArray.part.0` | tuple |
| 0.90% | `_decimal.cpython-314-x86_64-linux-gnu.so` | `mpd_qquantize` | library |
| 0.88% | `_decimal.cpython-314-x86_64-linux-gnu.so` | `dec_mpd_qquantize` | library |
| 0.82% | `_decimal.cpython-314-x86_64-linux-gnu.so` | `PyDecType_New` | library |
| 0.78% | `python` | `vgetargs1_impl` | calls |
| 0.77% | `_decimal.cpython-314-x86_64-linux-gnu.so` | `dec_dealloc` | library |
| 0.77% | `python` | `PyTuple_New` | memory |
| 0.77% | `_decimal.cpython-314-x86_64-linux-gnu.so` | `mpd_qshiftr` | library |
| 0.74% | `python` | `_PyObject_GC_Link` | gc |
| 0.72% | `python` | `gc_collect_region.isra.0` | gc |
| 0.71% | `python` | `_Py_dict_lookup` | lookup |
| 0.68% | `python` | `_Py_NewReference` | memory |
| 0.64% | `python` | `PyDict_GetItemRef` | dict |
| 0.61% | `python` | `PyCMethod_New` | memory |
| 0.59% | `_decimal.cpython-314-x86_64-linux-gnu.so` | `mpd_qfinalize.part.0` | library |
| 0.57% | `python` | `PyType_IsSubtype` | dynamic |
| 0.57% | `python` | `PyUnicode_AsUCS4` | str |
| 0.50% | `_decimal.cpython-314-x86_64-linux-gnu.so` | `dec_str` | library |
| 0.48% | `_decimal.cpython-314-x86_64-linux-gnu.so` | `_mpd_baseadd` | library |
| 0.47% | `python` | `write_str` | unknown |
| 0.45% | `python` | `PyObject_Vectorcall` | dynamic |
| 0.44% | `_decimal.cpython-314-x86_64-linux-gnu.so` | `ctx_mpd_qquantize` | library |
| 0.44% | `python` | `visit_decref` | gc |
| 0.42% | `python` | `method_vectorcall_VARARGS_KEYWORDS` | calls |
| 0.42% | `python` | `meth_dealloc` | memory |
| 0.41% | `_decimal.cpython-314-x86_64-linux-gnu.so` | `mpd_del` | library |
| 0.41% | `python` | `PyObject_Malloc` | dynamic |
| 0.41% | `_decimal.cpython-314-x86_64-linux-gnu.so` | `_mpd_to_string` | library |
| 0.40% | `_decimal.cpython-314-x86_64-linux-gnu.so` | `current_context` | library |
| 0.39% | `python` | `binary_op1` | unknown |
| 0.37% | `python` | `PyObject_RichCompare` | dynamic |
| 0.37% | `_decimal.cpython-314-x86_64-linux-gnu.so` | `PyDecType_FromLongExact` | library |
| 0.36% | `python` | `_PyObject_MakeTpCall` | dynamic |
| 0.35% | `python` | `PyFile_WriteObject` | unknown |
| 0.35% | `python` | `PyObject_GetAttr` | dynamic |
| 0.35% | `_decimal.cpython-314-x86_64-linux-gnu.so` | `0x0000000000007bc4` | library |
| 0.34% | `python` | `_PyObject_GetMethod` | dynamic |
| 0.33% | `python` | `PyNumber_Multiply` | dynamic |
| 0.33% | `python` | `builtin_print` | unknown |
| 0.32% | `_decimal.cpython-314-x86_64-linux-gnu.so` | `mpd_qmul` | library |
| 0.31% | `python` | `PyObject_CallOneArg` | dynamic |
| 0.30% | `python` | `r_object` | import |
| 0.30% | `python` | `PyNumber_InPlaceAdd` | dynamic |
| 0.30% | `python` | `visit_reachable` | gc |
| 0.29% | `python` | `PyUnicode_CompareWithASCIIString` | str |
| 0.29% | `python` | `cfunction_vectorcall_O` | calls |
| 0.27% | `_decimal.cpython-314-x86_64-linux-gnu.so` | `mpd_qadd` | library |
| 0.25% | `python` | `PyUnicode_New.part.0` | memory |
| 0.25% | `_decimal.cpython-314-x86_64-linux-gnu.so` | `word_to_string` | library |

## thrift

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 20.21% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 4.52% | `python` | `_PyObject_Malloc` | memory |
| 3.71% | `python` | `_PyObject_Free` | memory |
| 3.55% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 2.46% | `python` | `_PyType_LookupRef` | lookup |
| 2.32% | `python` | `initialize_locals` | interpreter |
| 2.14% | `python` | `_Py_dict_lookup` | lookup |
| 2.08% | `fastbinary.cpython-314-x86_64-linux-gnu.so` | `apache::thrift::py::ProtocolBase<apache::thrift::py::BinaryProtocol>::encodeValue` | library |
| 1.80% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.70% | `python` | `insert_to_emptydict` | dict |
| 1.39% | `python` | `insertdict` | dict |
| 1.31% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.26% | `python` | `PyType_GenericAlloc` | memory |
| 1.24% | `python` | `dict_dealloc` | memory |
| 1.18% | `python` | `PyDict_GetItemRef` | dict |
| 1.12% | `python` | `subtype_dealloc` | memory |
| 1.05% | `[JIT]` | `jit` | jit |
| 0.96% | `python` | `_Py_Dealloc` | memory |
| 0.94% | `python` | `PyObject_RichCompareBool` | dynamic |
| 0.88% | `python` | `tupledealloc` | memory |
| 0.80% | `fastbinary.cpython-314-x86_64-linux-gnu.so` | `apache::thrift::py::ProtocolBase<apache::thrift::py::BinaryProtocol>::decodeValue` | library |
| 0.78% | `python` | `_PyObject_Call_Prepend` | dynamic |
| 0.77% | `python` | `PyDict_SetItem` | dict |
| 0.74% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.73% | `python` | `gc_collect_region.isra.0` | gc |
| 0.69% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.68% | `python` | `_PyObject_GenericGetAttrWithDict` | dynamic |
| 0.66% | `python` | `PyLong_AsLong` | int |
| 0.66% | `python` | `_PyStack_UnpackDict` | unknown |
| 0.64% | `fastbinary.cpython-314-x86_64-linux-gnu.so` | `apache::thrift::py::ProtocolBase<apache::thrift::py::BinaryProtocol>::readStruct` | library |
| 0.63% | `python` | `_PyObject_MakeTpCall` | dynamic |
| 0.62% | `python` | `PyObject_GenericGetAttr` | dynamic |
| 0.59% | `python` | `PyObject_IS_GC` | gc |
| 0.58% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.56% | `python` | `PyObject_GC_Del` | gc |
| 0.55% | `fastbinary.cpython-314-x86_64-linux-gnu.so` | `apache::thrift::py::ProtocolBase<apache::thrift::py::BinaryProtocol>::readBytes` | library |
| 0.55% | `python` | `PyTuple_Size` | tuple |
| 0.54% | `python` | `PyObject_GetAttr` | dynamic |
| 0.50% | `python` | `PyDict_Next` | dict |
| 0.49% | `python` | `type_call` | dynamic |
| 0.48% | `python` | `_PyEval_Vector` | interpreter |
| 0.47% | `python` | `PyObject_ClearManagedDict` | dynamic |
| 0.46% | `python` | `PyObject_Call` | dynamic |
| 0.44% | `python` | `_PyDict_FromItems` | dict |
| 0.42% | `python` | `slot_tp_init` | unknown |
| 0.42% | `fastbinary.cpython-314-x86_64-linux-gnu.so` | `apache::thrift::py::BinaryProtocol::readFieldBegin` | library |
| 0.41% | `python` | `PyUnicode_RichCompare` | str |
| 0.40% | `python` | `dict_merge` | dict |
| 0.40% | `python` | `unicode_from_format` | str |
| 0.40% | `python` | `_Py_NewReference` | memory |
| 0.40% | `python` | `_PyObject_Calloc` | memory |
| 0.39% | `python` | `_PyObject_TryGetInstanceAttribute` | dynamic |
| 0.38% | `python` | `_Py_type_getattro` | lookup |
| 0.37% | `python` | `_PyTuple_FromArray.part.0` | tuple |
| 0.35% | `python` | `ascii_decode` | str |
| 0.35% | `python` | `visit_decref` | gc |
| 0.35% | `python` | `PyTuple_New` | memory |
| 0.34% | `python` | `_PyFunction_Vectorcall` | calls |
| 0.33% | `python` | `siphash13` | str |
| 0.32% | `python` | `resize_compact` | str |
| 0.30% | `python` | `vgetargs1_impl` | calls |
| 0.30% | `python` | `_PyThreadState_PopFrame` | interpreter |
| 0.30% | `fastbinary.cpython-314-x86_64-linux-gnu.so` | `apache::thrift::py::parse_struct_item_spec` | library |
| 0.29% | `python` | `_PyObject_GC_Link` | gc |
| 0.29% | `python` | `r_object` | import |
| 0.29% | `python` | `PyDict_New` | memory |
| 0.28% | `libc-2.31.so` | `malloc` | libc |
| 0.28% | `python` | `object_new` | memory |
| 0.27% | `python` | `visit_reachable` | gc |
| 0.27% | `python` | `_PyObject_Realloc` | memory |
| 0.27% | `python` | `listiter_next` | list |
| 0.26% | `python` | `list_dealloc` | memory |
| 0.26% | `python` | `PyObject_ClearWeakRefs` | dynamic |
| 0.26% | `libc-2.31.so` | `pthread_attr_setschedparam` | libc |
| 0.26% | `python` | `PyUnicode_New.part.0` | memory |
| 0.25% | `python` | `_PyType_GetDict` | dynamic |

## tomli_loads

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 19.28% | `[JIT]` | `jit` | jit |
| 19.14% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 6.17% | `python` | `_PyObject_Malloc` | memory |
| 5.41% | `python` | `_PyObject_Free` | memory |
| 5.03% | `python` | `set_lookkey` | miscobj |
| 3.83% | `python` | `_PyLong_Add` | int |
| 3.25% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 2.48% | `python` | `_PyUnicode_Equal` | str |
| 2.28% | `python` | `_Py_dict_lookup` | lookup |
| 2.11% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.67% | `python` | `_PySet_Contains` | miscobj |
| 1.53% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.25% | `python` | `PyDict_GetItemRef` | dict |
| 1.04% | `python` | `_Py_Dealloc` | memory |
| 0.91% | `python` | `tupledealloc` | memory |
| 0.88% | `python` | `_PyTuple_FromStackRefSteal` | tuple |
| 0.84% | `python` | `_PyIncrementalNewlineDecoder_decode` | memory |
| 0.82% | `python` | `long_dealloc` | memory |
| 0.78% | `python` | `replace` | str |
| 0.74% | `python` | `_PyUnicode_FromUCS4.part.0` | str |
| 0.66% | `python` | `PyNumber_AsSsize_t` | dynamic |
| 0.62% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.57% | `python` | `_Py_NewReference` | memory |
| 0.54% | `python` | `sre_ucs4_match` | library |
| 0.52% | `python` | `_PyType_LookupRef` | lookup |
| 0.44% | `python` | `tuplesubscript` | tuple |
| 0.39% | `python` | `siphash13` | str |
| 0.38% | `python` | `PySlice_AdjustIndices` | miscobj |
| 0.38% | `python` | `PyType_IsSubtype` | dynamic |
| 0.38% | `python` | `unicode_decode_utf8_impl` | str |
| 0.37% | `python` | `initialize_locals` | interpreter |
| 0.35% | `python` | `_PyObject_GenericGetAttrWithDict` | dynamic |
| 0.34% | `python` | `_PyBuildSlice_ConsumeRefs` | miscobj |
| 0.32% | `python` | `PyObject_GetItem` | dynamic |
| 0.32% | `python` | `PyObject_GetAttr` | dynamic |
| 0.31% | `python` | `slice_dealloc` | memory |
| 0.30% | `python` | `memcmp@plt` | unknown |
| 0.30% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.29% | `python` | `PyDict_Contains` | dict |
| 0.27% | `python` | `_PyObject_GC_New` | gc |
| 0.26% | `python` | `PyObject_GenericGetAttr` | dynamic |
| 0.25% | `python` | `PyObject_GC_Del` | gc |

## tornado_http

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 24.93% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 3.78% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 2.88% | `python` | `_PyObject_Malloc` | memory |
| 2.87% | `[JIT]` | `jit` | jit |
| 2.43% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 1.94% | `python` | `_PyObject_Free` | memory |
| 1.76% | `python` | `gc_collect_region.isra.0` | gc |
| 1.65% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.57% | `python` | `_Py_dict_lookup` | lookup |
| 1.48% | `python` | `_PyType_LookupRef` | lookup |
| 0.97% | `python` | `tupledealloc` | memory |
| 0.96% | `python` | `visit_decref` | gc |
| 0.83% | `python` | `initialize_locals` | interpreter |
| 0.78% | `libc-2.31.so` | `pthread_attr_setschedparam` | libc |
| 0.75% | `[kernel.kallsyms]` | `copy_user_enhanced_fast_string` | kernel |
| 0.69% | `python` | `visit_reachable` | gc |
| 0.59% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.57% | `python` | `r_object` | import |
| 0.54% | `python` | `_Py_Dealloc` | memory |
| 0.52% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.47% | `python` | `find_name_in_mro` | lookup |
| 0.45% | `python` | `PyDict_GetItemRef` | dict |
| 0.43% | `python` | `sre_ucs1_match` | library |
| 0.43% | `python` | `update_one_slot` | lookup |
| 0.42% | `python` | `dict_dealloc` | memory |
| 0.42% | `python` | `siphash13` | str |
| 0.41% | `python` | `PyObject_GC_Del` | gc |
| 0.41% | `python` | `_PyTuple_FromArray.part.0` | tuple |
| 0.39% | `[kernel.kallsyms]` | `clear_page_erms` | kernel |
| 0.37% | `python` | `PyObject_GenericGetAttr` | dynamic |
| 0.37% | `python` | `_PyCode_Quicken` | interpreter |
| 0.37% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.36% | `python` | `PyObject_Vectorcall` | dynamic |
| 0.34% | `python` | `subtype_dealloc` | memory |
| 0.33% | `python` | `_PyTuple_FromStackRefSteal` | tuple |
| 0.32% | `python` | `PyObject_GetAttr` | dynamic |
| 0.32% | `python` | `PyType_IsSubtype` | dynamic |
| 0.31% | `python` | `insertdict` | dict |
| 0.31% | `python` | `PyType_GenericAlloc` | memory |
| 0.29% | `python` | `_PyObject_GC_New` | gc |
| 0.29% | `python` | `_Py_hashtable_get_entry_generic` | lookup |
| 0.28% | `python` | `list_dealloc` | memory |
| 0.28% | `libc-2.31.so` | `malloc` | libc |
| 0.28% | `python` | `_PyUnicode_FromUCS1.part.0` | str |
| 0.25% | `[kernel.kallsyms]` | `native_irq_return_iret` | kernel |

## typing_runtime_protocols

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 22.68% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 6.14% | `[JIT]` | `jit` | jit |
| 4.77% | `python` | `_PyObject_Malloc` | memory |
| 3.44% | `python` | `_PyObject_Free` | memory |
| 2.91% | `python` | `_PyTuple_FromArray.part.0` | tuple |
| 2.72% | `python` | `tupledealloc` | memory |
| 2.58% | `python` | `_Py_dict_lookup` | lookup |
| 2.47% | `python` | `weakref___new__` | memory |
| 2.13% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 1.96% | `python` | `_PyType_LookupRef` | lookup |
| 1.77% | `python` | `_PyObject_MakeTpCall` | dynamic |
| 1.66% | `python` | `PyArg_UnpackTuple` | calls |
| 1.21% | `python` | `PyObject_RichCompareBool` | dynamic |
| 1.16% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.03% | `python` | `gc_collect_region.isra.0` | gc |
| 1.02% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 0.88% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.88% | `python` | `bounded_lru_cache_wrapper` | unknown |
| 0.87% | `python` | `PyObject_Vectorcall` | dynamic |
| 0.78% | `python` | `_PyObject_GC_New` | gc |
| 0.76% | `python` | `_Py_type_getattro` | lookup |
| 0.76% | `python` | `PyObject_GC_Del` | gc |
| 0.71% | `python` | `_PyDict_GetItem_KnownHash` | dict |
| 0.70% | `python` | `_Py_Dealloc` | memory |
| 0.70% | `python` | `type_call` | dynamic |
| 0.62% | `python` | `initialize_locals` | interpreter |
| 0.60% | `python` | `PyObject_GetAttr` | dynamic |
| 0.59% | `python` | `_Py_NewReference` | memory |
| 0.52% | `python` | `visit_decref` | gc |
| 0.50% | `python` | `set_lookkey` | miscobj |
| 0.48% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.46% | `python` | `getset_get` | dynamic |
| 0.46% | `python` | `list_dealloc` | memory |
| 0.44% | `python` | `PyObject_Hash` | dynamic |
| 0.44% | `python` | `PyTraceBack_Here` | exceptions |
| 0.43% | `python` | `frame_dealloc` | memory |
| 0.43% | `python` | `tuplerichcompare` | tuple |
| 0.42% | `python` | `PyType_IsSubtype` | dynamic |
| 0.40% | `python` | `wrap_descr_get` | unknown |
| 0.39% | `python` | `visit_reachable` | gc |
| 0.37% | `python` | `find_name_in_mro` | lookup |
| 0.37% | `python` | `PyList_New` | memory |
| 0.37% | `python` | `_PyObject_LookupSpecial` | dynamic |
| 0.37% | `python` | `r_object` | import |
| 0.35% | `python` | `_PyObject_GC_Link` | gc |
| 0.35% | `python` | `_Py_CheckFunctionResult` | calls |
| 0.35% | `python` | `weakref___init__` | unknown |
| 0.35% | `python` | `_PyObject_Realloc` | memory |
| 0.34% | `python` | `tuplehash` | tuple |
| 0.33% | `python` | `PyObject_Call` | dynamic |
| 0.32% | `python` | `update_one_slot` | lookup |
| 0.32% | `python` | `tuple_iter` | tuple |
| 0.32% | `python` | `_PyStaticType_GetState` | unknown |
| 0.30% | `python` | `tupleiter_dealloc` | memory |
| 0.29% | `python` | `_PyCode_Quicken` | interpreter |
| 0.29% | `python` | `_PyList_AppendTakeRefListResize` | list |
| 0.29% | `python` | `wrapper_call` | unknown |
| 0.29% | `libc-2.31.so` | `pthread_attr_setschedparam` | libc |
| 0.28% | `python` | `_PyTuple_FromArray` | tuple |
| 0.28% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.27% | `python` | `weakref_richcompare` | unknown |

## unpickle_pure_python

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 29.32% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 18.45% | `[JIT]` | `jit` | jit |
| 3.35% | `python` | `_Py_dict_lookup` | lookup |
| 2.96% | `python` | `_PyObject_Malloc` | memory |
| 2.79% | `python` | `PyObject_IsTrue` | dynamic |
| 2.19% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 1.80% | `python` | `_PyObject_Free` | memory |
| 1.56% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.49% | `python` | `PyDict_GetItemRef` | dict |
| 1.48% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.47% | `python` | `PyNumber_AsSsize_t` | dynamic |
| 1.26% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 1.00% | `python` | `_io_BytesIO_read` | unknown |
| 0.99% | `python` | `insertdict` | dict |
| 0.86% | `python` | `PyObject_GetItem` | dynamic |
| 0.83% | `python` | `bytes_subscript` | str |
| 0.82% | `python` | `initialize_locals` | interpreter |
| 0.78% | `python` | `PyObject_Size` | dynamic |
| 0.74% | `python` | `PyLong_AsSsize_t` | int |
| 0.73% | `python` | `_Py_convert_optional_to_ssize_t` | unknown |
| 0.71% | `python` | `PyBytes_FromStringAndSize` | str |
| 0.69% | `python` | `PyUnicode_Decode.part.0` | str |
| 0.67% | `python` | `gc_collect_region.isra.0` | gc |
| 0.66% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.61% | `python` | `siphash13` | str |
| 0.59% | `python` | `_PyThreadState_PopFrame` | interpreter |
| 0.53% | `python` | `PyObject_IsInstance` | dynamic |
| 0.52% | `python` | `ascii_decode` | str |
| 0.51% | `python` | `list_subscript` | list |
| 0.50% | `python` | `PyLong_FromSsize_t` | int |
| 0.44% | `python` | `unicode_decode_utf8` | str |
| 0.41% | `python` | `visit_decref` | gc |
| 0.37% | `python` | `PyUnicode_FromEncodedObject` | str |
| 0.34% | `python` | `list_append` | list |
| 0.34% | `python` | `unicode_vectorcall` | str |
| 0.34% | `python` | `_PyType_LookupRef` | lookup |
| 0.33% | `python` | `PyObject_Hash` | dynamic |
| 0.33% | `python` | `_PyObject_Realloc` | memory |
| 0.33% | `libc-2.31.so` | `pthread_attr_setschedparam` | libc |
| 0.30% | `python` | `r_object` | import |
| 0.30% | `python` | `tupledealloc` | memory |
| 0.28% | `python` | `PyUnicode_AsUTF8AndSize` | str |
| 0.28% | `python` | `dict_dealloc` | memory |
| 0.27% | `python` | `long_hash` | int |
| 0.26% | `python` | `_Py_Dealloc` | memory |
| 0.26% | `python` | `visit_reachable` | gc |
| 0.26% | `python` | `PyUnicode_New.part.0` | memory |

## xml_etree

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 10.51% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 6.81% | `[JIT]` | `jit` | jit |
| 5.01% | `python` | `_PyObject_Malloc` | memory |
| 3.28% | `python` | `_PyObject_Free` | memory |
| 2.66% | `python` | `_PyType_LookupRef` | lookup |
| 2.57% | `pyexpat.cpython-314-x86_64-linux-gnu.so` | `normal_updatePosition` | library |
| 2.56% | `python` | `gc_collect_region.isra.0` | gc |
| 2.17% | `pyexpat.cpython-314-x86_64-linux-gnu.so` | `normal_contentTok` | library |
| 1.82% | `libc-2.31.so` | `__nss_database_lookup` | libc |
| 1.73% | `python` | `_Py_dict_lookup` | lookup |
| 1.64% | `python` | `_io_TextIOWrapper_write` | unknown |
| 1.42% | `pyexpat.cpython-314-x86_64-linux-gnu.so` | `sip24_update` | library |
| 1.40% | `python` | `visit_decref` | gc |
| 1.39% | `python` | `visit_reachable` | gc |
| 1.37% | `python` | `PyObject_GenericGetAttr` | dynamic |
| 1.34% | `pyexpat.cpython-314-x86_64-linux-gnu.so` | `accountingDiffTolerated.part.0` | library |
| 1.16% | `pyexpat.cpython-314-x86_64-linux-gnu.so` | `normal_nameLength` | library |
| 1.07% | `_elementtree.cpython-314-x86_64-linux-gnu.so` | `expat_end_handler` | library |
| 1.06% | `pyexpat.cpython-314-x86_64-linux-gnu.so` | `doContent` | library |
| 1.03% | `pyexpat.cpython-314-x86_64-linux-gnu.so` | `lookup.constprop.0` | library |
| 0.99% | `python` | `initialize_locals` | interpreter |
| 0.97% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.94% | `_elementtree.cpython-314-x86_64-linux-gnu.so` | `treebuilder_handle_start` | library |
| 0.88% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 0.86% | `python` | `PyUnicode_Contains` | str |
| 0.85% | `python` | `PyObject_GetAttr` | dynamic |
| 0.79% | `python` | `_Py_Dealloc` | memory |
| 0.78% | `python` | `tupledealloc` | memory |
| 0.71% | `pyexpat.cpython-314-x86_64-linux-gnu.so` | `normal_getAtts` | library |
| 0.69% | `python` | `siphash13` | str |
| 0.66% | `python` | `ascii_decode` | str |
| 0.65% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.64% | `_elementtree.cpython-314-x86_64-linux-gnu.so` | `element_gc_traverse` | library |
| 0.62% | `_elementtree.cpython-314-x86_64-linux-gnu.so` | `elementiter_next` | library |
| 0.62% | `pyexpat.cpython-314-x86_64-linux-gnu.so` | `sip24_final` | library |
| 0.62% | `python` | `getset_get` | dynamic |
| 0.62% | `python` | `_copy_characters.part.0.constprop.0` | str |
| 0.61% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.53% | `python` | `list_dealloc` | memory |
| 0.53% | `python` | `PyUnicode_New.part.0` | memory |
| 0.52% | `python` | `_PyObject_GenericGetAttrWithDict` | dynamic |
| 0.52% | `pyexpat.cpython-314-x86_64-linux-gnu.so` | `storeAtts` | library |
| 0.51% | `_elementtree.cpython-314-x86_64-linux-gnu.so` | `expat_data_handler` | library |
| 0.50% | `python` | `_PyObject_GC_New` | gc |
| 0.49% | `python` | `_PyObject_GetMethod` | dynamic |
| 0.45% | `python` | `PyObject_VectorcallMethod` | dynamic |
| 0.43% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.42% | `python` | `PyObject_GC_Del` | gc |
| 0.42% | `python` | `_Py_NewReference` | memory |
| 0.41% | `python` | `PyType_IsSubtype` | dynamic |
| 0.39% | `_elementtree.cpython-314-x86_64-linux-gnu.so` | `element_gc_clear` | library |
| 0.39% | `python` | `visit_add_to_container` | gc |
| 0.38% | `libc-2.31.so` | `pthread_attr_setschedparam` | libc |
| 0.38% | `python` | `PyUnicode_Concat` | str |
| 0.38% | `python` | `unicode_dealloc` | memory |
| 0.37% | `_elementtree.cpython-314-x86_64-linux-gnu.so` | `expat_start_handler` | library |
| 0.37% | `python` | `_PyType_GetDict` | dynamic |
| 0.36% | `python` | `long_to_decimal_string_internal` | int |
| 0.35% | `python` | `PyType_GenericAlloc` | memory |
| 0.34% | `python` | `vgetargs1_impl` | calls |
| 0.34% | `python` | `PyObject_RichCompareBool` | dynamic |
| 0.33% | `python` | `_PyEval_Vector` | interpreter |
| 0.32% | `python` | `_PyObject_GC_Link` | gc |
| 0.31% | `python` | `PyUnicode_Format` | str |
| 0.30% | `python` | `dict_dealloc` | memory |
| 0.29% | `python` | `_PyObject_Realloc` | memory |
| 0.29% | `python` | `_PyTuple_FromStackRefSteal` | tuple |
| 0.29% | `python` | `PyList_Append` | list |
| 0.28% | `python` | `stringlib__two_way` | str |
| 0.28% | `python` | `_PyTuple_FromArray.part.0` | tuple |
| 0.27% | `_elementtree.cpython-314-x86_64-linux-gnu.so` | `makeuniversal.isra.0` | library |
| 0.27% | `_elementtree.cpython-314-x86_64-linux-gnu.so` | `element_getitem` | library |
| 0.26% | `python` | `tupletraverse` | tuple |
| 0.26% | `python` | `PyList_New` | memory |
| 0.26% | `python` | `PyObject_GetOptionalAttr` | dynamic |
| 0.26% | `python` | `PyDescr_IsData` | dynamic |
| 0.26% | `python` | `object_isinstance` | dynamic |
| 0.25% | `python` | `PyObject_IsTrue` | dynamic |


## Categories

### interpreter

20.64% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 16.03% | python | _PyEval_EvalFrameDefault |
| 1.36% | python | _PyFrame_ClearExceptCode |
| 0.73% | python | initialize_locals |
| 0.63% | python | _PyEval_FrameClearAndPop |
| 0.39% | python | _PyEvalFramePushAndInit |
| 0.27% | python | _PyThreadState_PopFrame |
| 0.19% | python | _PyCode_Quicken |
| 0.17% | python | _PyEval_Vector |
| 0.12% | python | _PyThreadState_PushFrame |
| 0.10% | python | _PyEval_SliceIndex |
| 0.09% | python | call_instrumentation_vector.part.0 |
| 0.08% | python | _Py_GetBaseOpcode |
| 0.08% | python | _PyFrame_Traverse |
| 0.07% | python | _PyPegen_is_memoized |
| 0.06% | python | _PyCode_New |
| 0.05% | python | _Py_call_instrumentation_line |
| 0.04% | python | _PyPegen_expect_token |
| 0.03% | python | _PyPegen_update_memo |
| 0.02% | python | _PyCode_Validate |
| 0.01% | python | _PyPegen_fill_token |
| 0.01% | python | _PyEval_BuiltinsFromGlobals |
| 0.01% | python | _PyFrame_New_NoTrack |
| 0.01% | python | _PyPegen_insert_memo |
| 0.01% | python | _PyCode_GetCode |
| 0.01% | python | _PyPegen_name_token |
| 0.01% | python | _PyThreadState_Attach |
| 0.01% | python | PyEval_GetFrame |
| 0.01% | python | _PyEval_ImportName |
| 0.01% | python | _PyPegen_new_identifier |
| 0.00% | python | _PyThreadState_MustExit |
| 0.00% | python | _PyThreadState_Detach |
| 0.00% | python | _PyCode_ConstantKey |
| 0.00% | python | PyEval_EvalCode |
| 0.00% | python | PyEval_SaveThread |

### memory

13.14% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 3.55% | python | _PyObject_Malloc |
| 3.15% | python | _PyObject_Free |
| 0.74% | python | _Py_Dealloc |
| 0.72% | python | tupledealloc |
| 0.42% | python | list_dealloc |
| 0.39% | python | _Py_NewReference |
| 0.31% | python | dict_dealloc |
| 0.24% | python | subtype_dealloc |
| 0.24% | python | PyType_GenericAlloc |
| 0.21% | python | PyList_New |
| 0.21% | python | PyUnicode_New.part.0 |
| 0.20% | python | gen_dealloc |
| 0.20% | python | _PyObject_Realloc |
| 0.16% | python | float_dealloc |
| 0.15% | python | unicode_dealloc |
| 0.14% | python | long_dealloc |
| 0.12% | python | slice_dealloc |
| 0.12% | python | PyTuple_New |
| 0.09% | python | PyFunction_NewWithQualName |
| 0.09% | python | _PyObject_Calloc |
| 0.08% | python | code_dealloc |
| 0.08% | python | PyCMethod_New |
| 0.08% | python | set_dealloc |
| 0.07% | python | func_dealloc |
| 0.06% | python | PyObject_CallFinalizerFromDealloc |
| 0.06% | python | meth_dealloc |
| 0.06% | python | memset@plt |
| 0.05% | python | context_tp_dealloc |
| 0.05% | python | memcpy@plt |
| 0.05% | python | allocate_from_new_pool |
| 0.05% | python | listiter_dealloc |
| 0.05% | python | pattern_new_match.isra.0.part.0 |
| 0.05% | python | _PyType_NewManagedObject |
| 0.04% | python | PySlice_New |
| 0.04% | python | PyDict_New |
| 0.04% | python | method_dealloc |
| 0.04% | python | weakref___new__ |
| 0.04% | python | PyMethod_New |
| 0.03% | python | PyMem_Calloc |
| 0.03% | python | frame_dealloc |
| 0.03% | python | object_new |
| 0.03% | python | PyMem_Malloc |
| 0.03% | python | PyMem_Free |
| 0.03% | python | _PyFloat_ExactDealloc |
| 0.02% | python | _PyAsyncGenValueWrapperNew |
| 0.02% | python | type_new |
| 0.02% | python | StopIteration_dealloc |
| 0.02% | python | async_gen_wrapped_val_dealloc |
| 0.02% | python | object_dealloc |
| 0.02% | python | _PyObject_New |
| 0.02% | python | tupleiter_dealloc |
| 0.02% | python | async_gen_asend_dealloc |
| 0.02% | python | cell_dealloc |
| 0.01% | python | PyMem_Realloc |
| 0.01% | python | range_dealloc |
| 0.01% | python | structseq_dealloc |
| 0.01% | python | tp_new_wrapper |
| 0.01% | python | BaseException_new |
| 0.01% | python | _PyIncrementalNewlineDecoder_decode |
| 0.01% | python | dictiter_dealloc |
| 0.01% | python | tb_dealloc |
| 0.01% | python | zip_new |
| 0.01% | python | dictview_dealloc |
| 0.01% | python | PyWeakref_NewRef |
| 0.01% | python | BaseException_dealloc |
| 0.01% | python | _PyMem_RawMalloc |
| 0.01% | python | PyUnicode_New |
| 0.01% | python | PyCell_New |
| 0.01% | python | match_dealloc |
| 0.01% | python | _PyUnicode_ExactDealloc |
| 0.01% | python | type_dealloc |
| 0.01% | python | reversed_new_impl |
| 0.00% | python | unicode_new |
| 0.00% | python | setiter_dealloc |
| 0.00% | python | slot_tp_new |
| 0.00% | python | _PyMem_RawFree |
| 0.00% | python | memory_dealloc |
| 0.00% | python | descr_dealloc |
| 0.00% | python | zip_dealloc |
| 0.00% | python | _Py_NewReferenceNoTotal |
| 0.00% | python | _PyObject_NewVar |

### jit

11.58% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 11.58% | [JIT] | jit |

### gc

10.08% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 2.91% | python | gc_collect_region.isra.0 |
| 1.63% | python | visit_decref |
| 1.58% | python | visit_reachable |
| 0.70% | python | visit_add_to_container |
| 0.43% | python | PyObject_GC_UnTrack |
| 0.40% | python | PyObject_GC_Del |
| 0.30% | python | list_traverse |
| 0.29% | python | _PyObject_GC_New |
| 0.27% | python | dict_traverse |
| 0.23% | python | subtype_traverse |
| 0.20% | python | _PyObject_GC_Link |
| 0.18% | python | PyObject_IS_GC |
| 0.17% | python | _PyGC_Collect |
| 0.15% | python | _PyObject_GC_NewVar |
| 0.11% | python | func_traverse |
| 0.09% | python | set_traverse |
| 0.07% | python | type_is_gc |
| 0.05% | python | type_traverse |
| 0.05% | python | _PyTuple_MaybeUntrack |
| 0.05% | python | _PyDict_MaybeUntrack |
| 0.04% | python | gen_traverse |
| 0.03% | python | meth_traverse |
| 0.02% | python | context_tp_traverse |
| 0.02% | python | PyGC_Collect |
| 0.02% | python | PyObject_GC_Track |
| 0.01% | python | descr_traverse |
| 0.01% | python | gc_traverse |
| 0.01% | python | executor_traverse |
| 0.01% | python | module_traverse |
| 0.01% | python | method_traverse |
| 0.01% | python | cell_traverse |
| 0.00% | python | _PyObject_GC_Resize |
| 0.00% | python | deque_traverse |

### library

7.15% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 1.90% | python | sre_ucs1_match |
| 0.88% | libz.so.1.2.11 | crc32_combine64 |
| 0.73% | python | sre_ucs2_charset.isra.0 |
| 0.35% | _json.cpython-314-x86_64-linux-gnu.so | scanstring_unicode |
| 0.29% | libz.so.1.2.11 | inflateBackEnd |
| 0.28% | python | sre_search |
| 0.18% | _json.cpython-314-x86_64-linux-gnu.so | scan_once_unicode |
| 0.14% | libm-2.31.so | f64xsubf128 |
| 0.14% | python | sre_ucs1_count |
| 0.13% | ld-2.31.so | _dl_rtld_di_serinfo |
| 0.09% | _json.cpython-314-x86_64-linux-gnu.so | py_encode_basestring_ascii |
| 0.08% | tracer.cpython-314-x86_64-linux-gnu.so | CTracer_trace |
| 0.08% | python | convertitem.constprop.0 |
| 0.05% | _asyncio.cpython-314-x86_64-linux-gnu.so | TaskObj_traverse |
| 0.05% | libpthread-2.31.so | __pthread_mutex_lock |
| 0.05% | array.cpython-314-x86_64-linux-gnu.so | array_subscr |
| 0.05% | python | pattern_subx |
| 0.05% | libm-2.31.so | __fmod_finite |
| 0.05% | python | _sre_SRE_Pattern_match |
| 0.04% | libpthread-2.31.so | pthread_mutex_unlock |
| 0.04% | ld-2.31.so | _dl_catch_error |
| 0.04% | _json.cpython-314-x86_64-linux-gnu.so | encoder_listencode_obj |
| 0.04% | pyexpat.cpython-314-x86_64-linux-gnu.so | normal_updatePosition |
| 0.03% | math.cpython-314-x86_64-linux-gnu.so | factorial_partial_product |
| 0.03% | pyexpat.cpython-314-x86_64-linux-gnu.so | normal_contentTok |
| 0.03% | fastbinary.cpython-314-x86_64-linux-gnu.so | apache::thrift::py::ProtocolBase<apache::thrift::py::BinaryProtocol>::encodeValue |
| 0.03% | _json.cpython-314-x86_64-linux-gnu.so | encoder_encode_key_value |
| 0.03% | _decimal.cpython-314-x86_64-linux-gnu.so | nm_mpd_qadd |
| 0.03% | _asyncio.cpython-314-x86_64-linux-gnu.so | task_step_impl |
| 0.02% | _decimal.cpython-314-x86_64-linux-gnu.so | _mpd_qaddsub |
| 0.02% | _decimal.cpython-314-x86_64-linux-gnu.so | _mpd_check_exp |
| 0.02% | _decimal.cpython-314-x86_64-linux-gnu.so | _mpd_qmul |
| 0.02% | _asyncio.cpython-314-x86_64-linux-gnu.so | TaskStepMethWrapper_call |
| 0.02% | _bisect.cpython-314-x86_64-linux-gnu.so | _bisect_bisect_right |
| 0.02% | pyexpat.cpython-314-x86_64-linux-gnu.so | sip24_update |
| 0.02% | _decimal.cpython-314-x86_64-linux-gnu.so | nm_mpd_qmul |
| 0.02% | array.cpython-314-x86_64-linux-gnu.so | array_ass_subscr |
| 0.02% | pyexpat.cpython-314-x86_64-linux-gnu.so | accountingDiffTolerated.part.0 |
| 0.02% | _decimal.cpython-314-x86_64-linux-gnu.so | mpd_setdigits |
| 0.02% | python | _sre_SRE_Pattern_search |
| 0.02% | _asyncio.cpython-314-x86_64-linux-gnu.so | TaskObj_clear |
| 0.02% | _heapq.cpython-314-x86_64-linux-gnu.so | siftup |
| 0.02% | pyexpat.cpython-314-x86_64-linux-gnu.so | normal_nameLength |
| 0.01% | _elementtree.cpython-314-x86_64-linux-gnu.so | expat_end_handler |
| 0.01% | pyexpat.cpython-314-x86_64-linux-gnu.so | doContent |
| 0.01% | _decimal.cpython-314-x86_64-linux-gnu.so | _mpd_baseshiftr |
| 0.01% | _asyncio.cpython-314-x86_64-linux-gnu.so | future_init |
| 0.01% | pyexpat.cpython-314-x86_64-linux-gnu.so | lookup.constprop.0 |
| 0.01% | _asyncio.cpython-314-x86_64-linux-gnu.so | _asyncio_Task___init__ |
| 0.01% | _decimal.cpython-314-x86_64-linux-gnu.so | dec_addstatus |
| 0.01% | _elementtree.cpython-314-x86_64-linux-gnu.so | treebuilder_handle_start |
| 0.01% | _decimal.cpython-314-x86_64-linux-gnu.so | mpd_qquantize |
| 0.01% | _asyncio.cpython-314-x86_64-linux-gnu.so | _asyncio_Future_add_done_callback |
| 0.01% | _decimal.cpython-314-x86_64-linux-gnu.so | dec_mpd_qquantize |
| 0.01% | libssl.so.1.1 | SSL_rstate_string |
| 0.01% | array.cpython-314-x86_64-linux-gnu.so | d_setitem |
| 0.01% | _asyncio.cpython-314-x86_64-linux-gnu.so | TaskStepMethWrapper_traverse |
| 0.01% | _asyncio.cpython-314-x86_64-linux-gnu.so | future_schedule_callbacks |
| 0.01% | _decimal.cpython-314-x86_64-linux-gnu.so | PyDecType_New |
| 0.01% | libpthread-2.31.so | __errno_location |
| 0.01% | fastbinary.cpython-314-x86_64-linux-gnu.so | apache::thrift::py::ProtocolBase<apache::thrift::py::BinaryProtocol>::decodeValue |
| 0.01% | _decimal.cpython-314-x86_64-linux-gnu.so | dec_dealloc |
| 0.01% | _decimal.cpython-314-x86_64-linux-gnu.so | mpd_qshiftr |
| 0.01% | _asyncio.cpython-314-x86_64-linux-gnu.so | FutureObj_traverse |
| 0.01% | _elementtree.cpython-314-x86_64-linux-gnu.so | element_gc_traverse |
| 0.01% | pyexpat.cpython-314-x86_64-linux-gnu.so | normal_getAtts |
| 0.01% | libpthread-2.31.so | pthread_cond_signal@@GLIBC_2.3.2 |
| 0.01% | fastbinary.cpython-314-x86_64-linux-gnu.so | apache::thrift::py::ProtocolBase<apache::thrift::py::BinaryProtocol>::readStruct |
| 0.01% | pyexpat.cpython-314-x86_64-linux-gnu.so | sip24_final |
| 0.01% | math.cpython-314-x86_64-linux-gnu.so | math_sqrt |
| 0.01% | _elementtree.cpython-314-x86_64-linux-gnu.so | elementiter_next |
| 0.01% | libpthread-2.31.so | sem_trywait@@GLIBC_2.2.5 |
| 0.01% | _decimal.cpython-314-x86_64-linux-gnu.so | mpd_qfinalize.part.0 |
| 0.01% | python | sys_trace_return |
| 0.01% | _asyncio.cpython-314-x86_64-linux-gnu.so | task_wakeup |
| 0.01% | fastbinary.cpython-314-x86_64-linux-gnu.so | apache::thrift::py::ProtocolBase<apache::thrift::py::BinaryProtocol>::readBytes |
| 0.01% | python | sre_ucs4_match |
| 0.01% | python | sys_trace_start |
| 0.01% | libz.so.1.2.11 | inflateCodesUsed |
| 0.01% | pyexpat.cpython-314-x86_64-linux-gnu.so | storeAtts |
| 0.01% | _asyncio.cpython-314-x86_64-linux-gnu.so | task_call_step_soon |
| 0.01% | _elementtree.cpython-314-x86_64-linux-gnu.so | expat_data_handler |
| 0.01% | _random.cpython-314-x86_64-linux-gnu.so | genrand_uint32 |
| 0.01% | _asyncio.cpython-314-x86_64-linux-gnu.so | FutureObj_clear |
| 0.01% | array.cpython-314-x86_64-linux-gnu.so | d_getitem |
| 0.01% | libm-2.31.so | pow |
| 0.01% | _decimal.cpython-314-x86_64-linux-gnu.so | dec_str |
| 0.01% | _decimal.cpython-314-x86_64-linux-gnu.so | _mpd_baseadd |
| 0.01% | libpthread-2.31.so | sem_post@@GLIBC_2.2.5 |
| 0.01% | libssl.so.1.1 | DTLSv1_client_method |
| 0.01% | _decimal.cpython-314-x86_64-linux-gnu.so | ctx_mpd_qquantize |
| 0.01% | _asyncio.cpython-314-x86_64-linux-gnu.so | FutureIter_traverse |
| 0.01% | _elementtree.cpython-314-x86_64-linux-gnu.so | element_gc_clear |
| 0.01% | _asyncio.cpython-314-x86_64-linux-gnu.so | TaskObj_finalize |
| 0.01% | fastbinary.cpython-314-x86_64-linux-gnu.so | apache::thrift::py::BinaryProtocol::readFieldBegin |
| 0.01% | _decimal.cpython-314-x86_64-linux-gnu.so | mpd_del |
| 0.01% | _decimal.cpython-314-x86_64-linux-gnu.so | _mpd_to_string |
| 0.01% | tracer.cpython-314-x86_64-linux-gnu.so | CTracer_set_pdata_stack |
| 0.01% | _decimal.cpython-314-x86_64-linux-gnu.so | current_context |
| 0.01% | _struct.cpython-314-x86_64-linux-gnu.so | s_pack_internal.isra.0 |
| 0.01% | _elementtree.cpython-314-x86_64-linux-gnu.so | expat_start_handler |
| 0.01% | _decimal.cpython-314-x86_64-linux-gnu.so | PyDecType_FromLongExact |
| 0.00% | _asyncio.cpython-314-x86_64-linux-gnu.so | future_add_done_callback |
| 0.00% | math.cpython-314-x86_64-linux-gnu.so | math_sin |
| 0.00% | _decimal.cpython-314-x86_64-linux-gnu.so | 0x0000000000007bc4 |
| 0.00% | array.cpython-314-x86_64-linux-gnu.so | 0x0000000000004644 |
| 0.00% | array.cpython-314-x86_64-linux-gnu.so | 0x00000000000047e4 |
| 0.00% | ld-2.31.so | _dl_debug_state |
| 0.00% | array.cpython-314-x86_64-linux-gnu.so | 0x00000000000049c4 |
| 0.00% | _cmsgpack.cpython-314-x86_64-linux-gnu.so | __pyx_f_7msgpack_9_cmsgpack_6Packer__pack |
| 0.00% | _decimal.cpython-314-x86_64-linux-gnu.so | mpd_qmul |
| 0.00% | _struct.cpython-314-x86_64-linux-gnu.so | unpack |
| 0.00% | math.cpython-314-x86_64-linux-gnu.so | math_factorial |
| 0.00% | _json.cpython-314-x86_64-linux-gnu.so | 0x00000000000024c4 |
| 0.00% | fastbinary.cpython-314-x86_64-linux-gnu.so | apache::thrift::py::parse_struct_item_spec |
| 0.00% | _asyncio.cpython-314-x86_64-linux-gnu.so | task_step |
| 0.00% | _decimal.cpython-314-x86_64-linux-gnu.so | mpd_qadd |
| 0.00% | _elementtree.cpython-314-x86_64-linux-gnu.so | makeuniversal.isra.0 |
| 0.00% | _elementtree.cpython-314-x86_64-linux-gnu.so | element_getitem |
| 0.00% | _struct.cpython-314-x86_64-linux-gnu.so | pack |
| 0.00% | _json.cpython-314-x86_64-linux-gnu.so | 0x0000000000002464 |
| 0.00% | _json.cpython-314-x86_64-linux-gnu.so | 0x0000000000002714 |
| 0.00% | _heapq.cpython-314-x86_64-linux-gnu.so | siftdown |
| 0.00% | _struct.cpython-314-x86_64-linux-gnu.so | s_pack |
| 0.00% | _decimal.cpython-314-x86_64-linux-gnu.so | word_to_string |

### dynamic

6.18% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 0.37% | python | PyObject_RichCompareBool |
| 0.34% | python | PyType_IsSubtype |
| 0.32% | python | PyObject_Hash |
| 0.29% | python | PyObject_GenericGetAttr |
| 0.27% | python | PyObject_GetAttr |
| 0.26% | python | PyNumber_AsSsize_t |
| 0.23% | python | _PyObject_GetMethod |
| 0.20% | python | _PyObject_GenericGetAttrWithDict |
| 0.18% | python | _PyObject_MakeTpCall |
| 0.16% | python | PyObject_Malloc |
| 0.16% | python | PyObject_IsTrue |
| 0.15% | python | type_ready |
| 0.14% | python | PyObject_GetItem |
| 0.14% | python | PyObject_Vectorcall |
| 0.13% | python | _PyObject_TryGetInstanceAttribute |
| 0.13% | python | _PyType_GetDict |
| 0.12% | python | PyObject_Free |
| 0.10% | python | _PyObject_LookupSpecial |
| 0.10% | python | PyObject_ClearManagedDict |
| 0.10% | python | PyObject_GetOptionalAttr |
| 0.10% | python | PyObject_VisitManagedDict |
| 0.10% | python | type_call |
| 0.09% | python | PyObject_GetIter |
| 0.08% | python | PyObject_RichCompare |
| 0.08% | python | PyObject_IsInstance |
| 0.07% | python | PyObject_CallOneArg |
| 0.07% | python | PyType_GetModuleByDef |
| 0.07% | python | PyObject_Size |
| 0.07% | python | PyObject_GenericSetAttr |
| 0.07% | python | _PyObject_Call_Prepend |
| 0.06% | python | getset_get |
| 0.06% | python | object_isinstance |
| 0.06% | python | PyObject_SetAttr |
| 0.06% | python | PyObject_ClearWeakRefs |
| 0.06% | python | PyObject_Call |
| 0.06% | python | PyNumber_Multiply |
| 0.05% | python | PyDescr_IsData |
| 0.04% | python | PyObject_SetItem |
| 0.04% | python | PyNumber_TrueDivide |
| 0.04% | python | PyNumber_Add |
| 0.04% | python | PyIter_Next |
| 0.04% | python | PyNumber_And |
| 0.04% | python | PyObject_VectorcallMethod |
| 0.04% | python | PySequence_Fast |
| 0.03% | python | delitem_common |
| 0.03% | python | _Py_type_getattro_impl |
| 0.03% | python | method_get |
| 0.03% | python | do_super_lookup |
| 0.03% | python | _PyObject_LookupSpecialMethod |
| 0.03% | python | StopIteration_init |
| 0.03% | python | PySequence_Contains |
| 0.03% | python | slot_tp_richcompare |
| 0.02% | python | PyNumber_Subtract |
| 0.02% | python | _PyObject_ClearFreeLists |
| 0.02% | python | PyObject_Str |
| 0.02% | python | PyIter_Send |
| 0.02% | python | _PyObject_RealIsInstance |
| 0.02% | python | PyNumber_Remainder |
| 0.02% | python | PySequence_Tuple |
| 0.02% | python | PyNumber_Index |
| 0.02% | python | object_richcompare |
| 0.02% | python | PyNumber_FloorDivide |
| 0.02% | python | PyNumber_Xor |
| 0.02% | python | _PySuper_Lookup |
| 0.02% | python | _PyObject_InitInlineValues |
| 0.01% | python | object_get_class |
| 0.01% | python | _PyNumber_Index |
| 0.01% | python | PyNumber_Rshift |
| 0.01% | python | object_recursive_isinstance |
| 0.01% | python | PyObject_IsSubclass |
| 0.01% | python | PyNumber_InPlaceTrueDivide |
| 0.01% | python | _PyObject_CallFunctionVa |
| 0.01% | python | _PyObject_StoreInstanceAttribute |
| 0.01% | python | PyMapping_GetOptionalItem |
| 0.01% | python | PyNumber_InPlaceAdd |
| 0.01% | python | object_vacall |
| 0.01% | python | PyObject_GenericHash |
| 0.01% | python | _PyNumber_PowerNoMod |
| 0.01% | python | PyNumber_Lshift |
| 0.01% | python | object_init |
| 0.01% | python | PyObject_GetBuffer |
| 0.01% | python | _PyObject_RealIsSubclass |
| 0.01% | python | PyObject_SelfIter |
| 0.01% | python | type_mro_modified |
| 0.01% | python | PyObject_LengthHint |
| 0.01% | python | PyObject_SetAttrString |
| 0.01% | python | PyNumber_Negative |
| 0.01% | python | PyObject_DelItem |
| 0.01% | python | PyMapping_Check |
| 0.01% | python | PyObject_HasAttrWithError |
| 0.01% | python | PyNumber_Long |
| 0.00% | python | PyIter_Check |
| 0.00% | python | PyNumber_Or |
| 0.00% | python | type___instancecheck__ |
| 0.00% | python | PyObject_Repr |
| 0.00% | python | PySequence_GetItem |
| 0.00% | python | object_str |
| 0.00% | python | PyObject_CallMethodObjArgs |

### lookup

5.59% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 1.83% | python | unicodekeys_lookup_unicode |
| 1.67% | python | _Py_dict_lookup |
| 1.22% | python | _PyType_LookupRef |
| 0.23% | python | update_one_slot |
| 0.22% | python | find_name_in_mro |
| 0.21% | python | _Py_hashtable_get_entry_generic |
| 0.11% | python | _Py_type_getattro |
| 0.02% | python | PyMember_GetOne |
| 0.02% | python | builtin_getattr |
| 0.02% | python | _PyType_Lookup |
| 0.02% | python | _Py_hashtable_get |
| 0.01% | python | PyMember_SetOne |
| 0.01% | python | _Py_hashtable_destroy |

### kernel

4.39% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 0.66% | [kernel.kallsyms] | copy_user_enhanced_fast_string |
| 0.26% | [kernel.kallsyms] | clear_page_erms |
| 0.14% | [kernel.kallsyms] | native_irq_return_iret |
| 0.10% | [kernel.kallsyms] | sync_regs |
| 0.08% | [kernel.kallsyms] | rmqueue |
| 0.08% | [kernel.kallsyms] | __d_lookup_rcu |
| 0.07% | [kernel.kallsyms] | _raw_spin_lock |
| 0.07% | [kernel.kallsyms] | zap_pte_range.isra.0 |
| 0.06% | [kernel.kallsyms] | free_pcppages_bulk |
| 0.06% | [kernel.kallsyms] | memset_erms |
| 0.05% | [kernel.kallsyms] | __handle_mm_fault |
| 0.04% | [kernel.kallsyms] | try_charge |
| 0.04% | [kernel.kallsyms] | release_pages |
| 0.04% | [kernel.kallsyms] | get_mem_cgroup_from_mm |
| 0.04% | [kernel.kallsyms] | __pagevec_lru_add_fn |
| 0.04% | [kernel.kallsyms] | mem_cgroup_throttle_swaprate |
| 0.03% | [kernel.kallsyms] | smp_call_function_single |
| 0.03% | [kernel.kallsyms] | filemap_map_pages |
| 0.03% | [kernel.kallsyms] | handle_mm_fault |
| 0.03% | [kernel.kallsyms] | mem_cgroup_try_charge |
| 0.03% | [kernel.kallsyms] | ext4_htree_store_dirent |
| 0.03% | [kernel.kallsyms] | syscall_return_via_sysret |
| 0.03% | [kernel.kallsyms] | link_path_walk.part.0 |
| 0.03% | [kernel.kallsyms] | __ext4fs_dirhash |
| 0.03% | [kernel.kallsyms] | __alloc_pages_nodemask |
| 0.03% | [kernel.kallsyms] | find_vma |
| 0.03% | [kernel.kallsyms] | kmem_cache_alloc |
| 0.03% | [kernel.kallsyms] | memcg_kmem_get_cache |
| 0.03% | [kernel.kallsyms] | page_remove_rmap |
| 0.02% | [kernel.kallsyms] | copy_page |
| 0.02% | [kernel.kallsyms] | perf_iterate_ctx |
| 0.02% | [kernel.kallsyms] | perf_event_alloc |
| 0.02% | [kernel.kallsyms] | kmem_cache_free |
| 0.02% | [kernel.kallsyms] | do_user_addr_fault |
| 0.02% | [kernel.kallsyms] | filldir64 |
| 0.02% | [kernel.kallsyms] | strncpy_from_user |
| 0.02% | [kernel.kallsyms] | native_flush_tlb_one_user |
| 0.02% | [kernel.kallsyms] | entry_SYSCALL_64 |
| 0.02% | [kernel.kallsyms] | do_anonymous_page |
| 0.02% | [kernel.kallsyms] | prep_new_page |
| 0.02% | [kernel.kallsyms] | do_syscall_64 |
| 0.02% | [kernel.kallsyms] | find_get_entry |
| 0.02% | [kernel.kallsyms] | get_page_from_freelist |
| 0.02% | [kernel.kallsyms] | inode_permission |
| 0.02% | [kernel.kallsyms] | __virt_addr_valid |
| 0.02% | [kernel.kallsyms] | lookup_fast |
| 0.02% | [kernel.kallsyms] | kfree |
| 0.02% | [kernel.kallsyms] | vmacache_find |
| 0.02% | [kernel.kallsyms] | __vma_adjust |
| 0.02% | [kernel.kallsyms] | rb_insert_color |
| 0.01% | [kernel.kallsyms] | __slab_free |
| 0.01% | [kernel.kallsyms] | error_entry |
| 0.01% | [kernel.kallsyms] | __mod_memcg_state |
| 0.01% | [kernel.kallsyms] | memcpy_erms |
| 0.01% | [kernel.kallsyms] | __count_memcg_events |
| 0.01% | [kernel.kallsyms] | unmapped_area_topdown |
| 0.01% | [kernel.kallsyms] | str2hashbuf_signed |
| 0.01% | [kernel.kallsyms] | _raw_spin_lock_irqsave |
| 0.01% | [kernel.kallsyms] | page_fault |
| 0.01% | [kernel.kallsyms] | ext4_getattr |
| 0.01% | [kernel.kallsyms] | rb_next |
| 0.01% | [kernel.kallsyms] | __mod_lruvec_state |
| 0.01% | [kernel.kallsyms] | tcp_sendmsg_locked |
| 0.01% | [kernel.kallsyms] | __fget_light |
| 0.01% | [kernel.kallsyms] | walk_component |
| 0.01% | [kernel.kallsyms] | generic_permission |
| 0.01% | [kernel.kallsyms] | up_read |
| 0.01% | [kernel.kallsyms] | entry_SYSCALL_64_after_hwframe |
| 0.01% | [kernel.kallsyms] | security_inode_getattr |
| 0.01% | [kernel.kallsyms] | down_read_trylock |
| 0.01% | [kernel.kallsyms] | __check_object_size |
| 0.01% | [kernel.kallsyms] | _cond_resched |
| 0.01% | [kernel.kallsyms] | lru_cache_add_active_or_unevictable |
| 0.01% | [kernel.kallsyms] | __lru_cache_add |
| 0.01% | [kernel.kallsyms] | __kmalloc |
| 0.01% | [kernel.kallsyms] | set_root |
| 0.01% | [kernel.kallsyms] | rcu_all_qs |
| 0.01% | [kernel.kallsyms] | alloc_pages_vma |
| 0.01% | [kernel.kallsyms] | page_add_file_rmap |
| 0.01% | [kernel.kallsyms] | free_unref_page_list |
| 0.01% | [kernel.kallsyms] | swapgs_restore_regs_and_return_to_usermode |
| 0.01% | [kernel.kallsyms] | fpregs_assert_state_consistent |
| 0.01% | [kernel.kallsyms] | mem_cgroup_from_task |
| 0.01% | [kernel.kallsyms] | mutex_lock |
| 0.01% | [kernel.kallsyms] | mutex_unlock |
| 0.01% | [kernel.kallsyms] | xas_load |
| 0.01% | [kernel.kallsyms] | pagevec_lru_move_fn |
| 0.01% | [kernel.kallsyms] | __ext4_check_dir_entry |
| 0.01% | [kernel.kallsyms] | show_cpuinfo |
| 0.01% | [kernel.kallsyms] | __mod_node_page_state |
| 0.01% | [kernel.kallsyms] | free_pages_and_swap_cache |
| 0.01% | [kernel.kallsyms] | __mod_zone_page_state |
| 0.01% | [kernel.kallsyms] | mem_cgroup_commit_charge |
| 0.01% | [kernel.kallsyms] | alloc_set_pte |
| 0.01% | [kernel.kallsyms] | __lock_text_start |
| 0.01% | [kernel.kallsyms] | in_group_p |
| 0.01% | [kernel.kallsyms] | format_decode |
| 0.01% | [kernel.kallsyms] | vsnprintf |
| 0.01% | [kernel.kallsyms] | generic_file_buffered_read |
| 0.01% | [kernel.kallsyms] | memchr |
| 0.01% | [kernel.kallsyms] | page_counter_cancel |
| 0.01% | [kernel.kallsyms] | ___slab_alloc |
| 0.01% | [kernel.kallsyms] | unlock_page |
| 0.01% | [kernel.kallsyms] | __follow_mount_rcu.isra.0 |
| 0.01% | [kernel.kallsyms] | __legitimize_mnt |
| 0.01% | [kernel.kallsyms] | __vma_link_rb |
| 0.01% | [kernel.kallsyms] | kmem_cache_alloc_trace |
| 0.01% | [kernel.kallsyms] | memcg_kmem_put_cache |
| 0.01% | [kernel.kallsyms] | free_unref_page_prepare.part.0 |
| 0.01% | [kernel.kallsyms] | inherit_event.isra.0 |
| 0.01% | [kernel.kallsyms] | free_unref_page_commit |
| 0.01% | [kernel.kallsyms] | psi_task_change |
| 0.01% | [kernel.kallsyms] | perf_event_mmap |
| 0.01% | [kernel.kallsyms] | __free_pages_ok |
| 0.01% | [kernel.kallsyms] | anon_vma_interval_tree_insert |
| 0.01% | [kernel.kallsyms] | lockref_put_return |
| 0.01% | [kernel.kallsyms] | call_filldir |
| 0.01% | [kernel.kallsyms] | native_sched_clock |
| 0.01% | [kernel.kallsyms] | kthread_blkcg |
| 0.01% | [kernel.kallsyms] | nmi_restore |
| 0.01% | [kernel.kallsyms] | fsnotify |
| 0.01% | [kernel.kallsyms] | __rb_insert_augmented |
| 0.01% | [kernel.kallsyms] | __check_heap_object |
| 0.01% | [kernel.kallsyms] | skb_release_data |
| 0.01% | [kernel.kallsyms] | page_counter_try_charge |
| 0.01% | [kernel.kallsyms] | mem_cgroup_try_charge_delay |
| 0.01% | [kernel.kallsyms] | __do_munmap |
| 0.01% | [kernel.kallsyms] | native_write_msr |
| 0.01% | [kernel.kallsyms] | __lookup_mnt |
| 0.01% | [kernel.kallsyms] | perf_iterate_sb |
| 0.01% | [kernel.kallsyms] | __fput |
| 0.01% | [kernel.kallsyms] | update_curr |
| 0.01% | [kernel.kallsyms] | vfs_getattr_nosec |
| 0.01% | [kernel.kallsyms] | string_nocheck |
| 0.01% | [kernel.kallsyms] | __tcp_transmit_skb |
| 0.01% | [kernel.kallsyms] | page_add_new_anon_rmap |
| 0.01% | [kernel.kallsyms] | mem_cgroup_page_lruvec |
| 0.00% | [kernel.kallsyms] | vma_interval_tree_insert |
| 0.00% | [kernel.kallsyms] | down_write |
| 0.00% | [kernel.kallsyms] | pmd_devmap_trans_unstable |
| 0.00% | [kernel.kallsyms] | security_inode_permission |
| 0.00% | [kernel.kallsyms] | anon_vma_interval_tree_remove |
| 0.00% | [kernel.kallsyms] | uncharge_page |
| 0.00% | [kernel.kallsyms] | __do_page_fault |
| 0.00% | [kernel.kallsyms] | update_cfs_group |
| 0.00% | [kernel.kallsyms] | cp_new_stat |
| 0.00% | [kernel.kallsyms] | getname_flags |
| 0.00% | [kernel.kallsyms] | common_perm |
| 0.00% | [kernel.kallsyms] | xas_start |
| 0.00% | [kernel.kallsyms] | mem_cgroup_update_lru_size |
| 0.00% | [kernel.kallsyms] | vm_normal_page |
| 0.00% | [kernel.kallsyms] | fput_many |
| 0.00% | [kernel.kallsyms] | filename_lookup |
| 0.00% | [kernel.kallsyms] | mem_cgroup_charge_statistics |
| 0.00% | [kernel.kallsyms] | __vma_rb_erase |
| 0.00% | [kernel.kallsyms] | unmap_page_range |
| 0.00% | [kernel.kallsyms] | do_dentry_open |
| 0.00% | [kernel.kallsyms] | mmap_region |
| 0.00% | [kernel.kallsyms] | update_load_avg |
| 0.00% | [kernel.kallsyms] | read_tsc |
| 0.00% | [kernel.kallsyms] | up_write |
| 0.00% | [kernel.kallsyms] | mark_page_accessed |
| 0.00% | [kernel.kallsyms] | __perf_addr_filters_adjust |
| 0.00% | [kernel.kallsyms] | htree_dirblock_to_tree |
| 0.00% | [kernel.kallsyms] | map_id_up |
| 0.00% | [kernel.kallsyms] | rcu_segcblist_enqueue |
| 0.00% | [kernel.kallsyms] | rb_next_postorder |
| 0.00% | [kernel.kallsyms] | account_kernel_stack |
| 0.00% | [kernel.kallsyms] | switch_fpu_return |
| 0.00% | [kernel.kallsyms] | do_sys_poll |
| 0.00% | [kernel.kallsyms] | page_mapping |
| 0.00% | [kernel.kallsyms] | __call_rcu |
| 0.00% | [kernel.kallsyms] | kernel_poison_pages |
| 0.00% | [kernel.kallsyms] | get_task_policy.part.0 |
| 0.00% | [kernel.kallsyms] | ext4_find_dest_de |
| 0.00% | [kernel.kallsyms] | kmem_cache_alloc_node |
| 0.00% | [kernel.kallsyms] | __skb_datagram_iter |
| 0.00% | [kernel.kallsyms] | tcp_ack |
| 0.00% | [kernel.kallsyms] | ip_finish_output2 |
| 0.00% | [kernel.kallsyms] | __dev_queue_xmit |
| 0.00% | [kernel.kallsyms] | __update_load_avg_se |
| 0.00% | [kernel.kallsyms] | do_sys_open |
| 0.00% | [kernel.kallsyms] | __task_pid_nr_ns |
| 0.00% | [kernel.kallsyms] | __d_lookup |
| 0.00% | [kernel.kallsyms] | change_protection_range |
| 0.00% | [kernel.kallsyms] | prepare_exit_to_usermode |
| 0.00% | [kernel.kallsyms] | free_one_page |
| 0.00% | [kernel.kallsyms] | path_init |
| 0.00% | [kernel.kallsyms] | __x86_indirect_thunk_rax |
| 0.00% | [kernel.kallsyms] | vma_interval_tree_remove |
| 0.00% | [kernel.kallsyms] | may_open.isra.0 |
| 0.00% | [kernel.kallsyms] | ext4_search_dir |
| 0.00% | [kernel.kallsyms] | __inc_numa_state |
| 0.00% | [kernel.kallsyms] | errseq_sample |
| 0.00% | [kernel.kallsyms] | ext4_dx_readdir |

### int

4.19% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 1.06% | python | k_mul |
| 0.44% | python | x_divrem |
| 0.43% | python | _PyLong_Add |
| 0.21% | python | long_hash |
| 0.19% | python | x_add |
| 0.18% | python | PyLong_FromLong |
| 0.16% | python | _PyLong_Subtract |
| 0.13% | python | PyLong_AsSsize_t |
| 0.13% | python | long_bitwise |
| 0.12% | python | long_to_decimal_string_internal |
| 0.12% | python | long_richcompare |
| 0.11% | python | PyLong_FromSsize_t |
| 0.10% | python | x_sub |
| 0.08% | python | PyLong_FromString |
| 0.07% | python | _PyLong_Multiply |
| 0.06% | python | long_rshift1 |
| 0.05% | python | PyLong_AsDouble |
| 0.05% | python | long_div |
| 0.05% | python | l_mod |
| 0.04% | python | long_and |
| 0.04% | python | PyLong_AsLongAndOverflow |
| 0.03% | python | PyLong_AsLong |
| 0.03% | python | long_mul |
| 0.03% | python | PyLong_FromVoidPtr |
| 0.03% | python | long_rshift |
| 0.03% | python | long_add |
| 0.03% | python | PyLong_FromUnsignedLong |
| 0.02% | python | long_lshift1 |
| 0.02% | python | long_xor |
| 0.02% | python | long_lshift |
| 0.01% | python | _PyLong_GCD |
| 0.01% | python | PyLong_FromUnsignedLongLong |
| 0.01% | python | long_to_decimal_string |
| 0.01% | python | PyLong_FromLongLong |
| 0.01% | python | long_mod |
| 0.01% | python | long_float |
| 0.01% | python | long_neg |
| 0.01% | python | PyLong_AsInt |
| 0.01% | python | _PyLong_Frexp |
| 0.01% | python | _PyLong_FromByteArray |
| 0.01% | python | PyLong_AsUnsignedLong |
| 0.00% | python | long_or |
| 0.00% | python | long_sub |
| 0.00% | python | long_vectorcall |
| 0.00% | python | long_invert |

### libc

3.20% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 1.99% | libc-2.31.so | __nss_database_lookup |
| 0.43% | libc-2.31.so | pthread_attr_setschedparam |
| 0.36% | libcrypto.so.1.1 | CRYPTO_secure_actual_size |
| 0.11% | libc-2.31.so | malloc |
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
| 0.00% | libc-2.31.so | wcstombs |

### unknown

2.61% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 0.06% | python | compute_range_length |
| 0.06% | python | PyThreadState_Get |
| 0.05% | python | func_clear |
| 0.05% | python | slot_tp_init |
| 0.04% | python | PyThread_get_thread_ident |
| 0.04% | python | min_max |
| 0.04% | python | slot_mp_subscript |
| 0.03% | python | _Py_uop_analyze_and_optimize |
| 0.03% | python | _PyStack_UnpackDict |
| 0.03% | python | _Py_MakeCoro |
| 0.03% | python | context_run |
| 0.03% | python | _Py_HashBytes |
| 0.03% | python | zip_next |
| 0.03% | python | store_instance_attr_lock_held |
| 0.03% | [vdso] | __vdso_clock_gettime |
| 0.02% | python | _PyCfg_OptimizeCodeUnit |
| 0.02% | python | sys_audit_tstate |
| 0.02% | python | _PyIO_find_line_ending |
| 0.02% | python | _io_TextIOWrapper_write |
| 0.02% | python | new_keys_object.constprop.0 |
| 0.02% | python | hashtable_unicode_compare |
| 0.02% | python | PyContextVar_Get |
| 0.02% | python | builtin_sum |
| 0.02% | python | _PyAssemble_MakeCodeObject |
| 0.02% | python | PyIndex_Check |
| 0.02% | python | PySys_Audit |
| 0.02% | python | do_mkvalue |
| 0.02% | python | code_hash |
| 0.02% | python | bounded_lru_cache_wrapper |
| 0.02% | python | memcmp@plt |
| 0.02% | python | hashtable_unicode_hash |
| 0.02% | python | _io_BytesIO_read |
| 0.02% | python | primary_rule |
| 0.02% | python | _PyCoro_GetAwaitableIter |
| 0.02% | python | pthread_self@plt |
| 0.01% | python | _PyArena_Malloc |
| 0.01% | python | term_rule |
| 0.01% | python | pysiphash |
| 0.01% | python | PyContext_CopyCurrent |
| 0.01% | python | map_next |
| 0.01% | python | fill_time |
| 0.01% | python | build_indices_generic |
| 0.01% | python | wrapperdescr_call |
| 0.01% | python | unsafe_tuple_compare |
| 0.01% | python | _PyFunction_SetVersion |
| 0.01% | python | _PyFunction_ClearCodeByVersion |
| 0.01% | python | _PyCfg_OptimizedCfgToInstructionSequence |
| 0.01% | python | tailmatch |
| 0.01% | python | _Py_convert_optional_to_ssize_t |
| 0.01% | python | _PyModule_ClearDict |
| 0.01% | python | builtin_hasattr |
| 0.01% | python | dictitems_iter |
| 0.01% | python | emit_trampoline |
| 0.01% | python | vectorcall_maybe.constprop.0 |
| 0.01% | python | _Py_Specialize_LoadAttr |
| 0.01% | python | slot_tp_hash |
| 0.01% | python | 0x0000000000084750 |
| 0.01% | python | _PyType_FromMetaclass_impl |
| 0.01% | python | member_get |
| 0.01% | python | emit__EXIT_TRACE |
| 0.01% | python | unsafe_long_compare |
| 0.01% | python | _Py_Specialize_Call |
| 0.01% | python | _io_open |
| 0.01% | python | strlen@plt |
| 0.01% | python | mro_implementation_unlocked |
| 0.01% | python | any_find_slice |
| 0.01% | python | compiler_visit_expr |
| 0.01% | python | inversion_rule |
| 0.01% | python | write_str |
| 0.01% | python | shift_expr_rule |
| 0.01% | python | binary_op1 |
| 0.01% | python | _PyBytes_FromList |
| 0.01% | python | subtype_clear |
| 0.01% | python | path_converter |
| 0.01% | python | setitem_take2_lock_held |
| 0.01% | python | sum_rule |
| 0.01% | python | _PyObjectDict_SetItem |
| 0.01% | python | insert_split_key |
| 0.01% | python | builtin_id |
| 0.01% | python | insert_split_value |
| 0.01% | python | islice_next |
| 0.01% | python | patch_x86_64_32rx |
| 0.01% | python | basicblock_remove_redundant_nops |
| 0.01% | python | _PyFrame_MakeAndSetFrameObject |
| 0.01% | python | build_string |
| 0.01% | python | symtable_visit_expr |
| 0.01% | python | write_bytes |
| 0.01% | python | os_stat |
| 0.01% | python | countformat |
| 0.01% | python | bitwise_or_rule |
| 0.01% | python | _pystat_fromstructstat |
| 0.01% | python | unsafe_latin_compare |
| 0.01% | python | ScandirIterator_iternext |
| 0.01% | python | astfold_expr |
| 0.01% | python | weakref___init__ |
| 0.01% | python | copy_lock_held |
| 0.01% | python | slot_sq_contains |
| 0.01% | python | mro_internal_unlocked.isra.0 |
| 0.01% | python | posix_do_stat.isra.0 |
| 0.01% | python | slot_tp_iter |
| 0.01% | python | slot_mp_ass_subscript |
| 0.01% | python | make_dict_from_instance_attributes |
| 0.01% | python | 0x0000000000084758 |
| 0.01% | python | bitwise_xor_rule |
| 0.01% | python | PyTime_AsSecondsDouble |
| 0.01% | python | builtin_any |
| 0.01% | python | slot_tp_call |
| 0.01% | python | assign_version_tag |
| 0.01% | python | analyze_descriptor |
| 0.01% | python | bitwise_and_rule |
| 0.01% | python | wrapperdescr_get |
| 0.01% | python | _PyStaticType_InitBuiltin |
| 0.01% | python | _PyInstructionSequence_Addop |
| 0.01% | python | _validate_inner |
| 0.01% | python | _Py_bytes_lower |
| 0.01% | python | builtin___build_class__ |
| 0.01% | python | scan_block_for_locals |
| 0.01% | python | slot_tp_iternext |
| 0.01% | python | lru_cache_make_key |
| 0.01% | python | rlock_acquire |
| 0.01% | python | _Py_call_instrumentation_arg |
| 0.01% | python | va_build_value |
| 0.01% | python | chain_next |
| 0.01% | python | wrap_descr_get |
| 0.01% | python | wrapper_call |
| 0.01% | python | func_descr_get |
| 0.01% | python | disjunction_rule |
| 0.01% | python | PyThread_acquire_lock_timed_with_retries |
| 0.01% | python | getset_set |
| 0.01% | python | _PyStaticType_GetState |
| 0.01% | python | do_strip |
| 0.01% | python | update_slot |
| 0.01% | python | sm_descr_get |
| 0.01% | python | _Py_module_getattro_impl |
| 0.01% | python | _abc__abc_instancecheck |
| 0.01% | python | _PyCfg_FromInstructionSequence |
| 0.01% | python | _io_FileIO___init__ |
| 0.01% | python | write_location_info_entry |
| 0.01% | python | best_base |
| 0.01% | python | weakref_richcompare |
| 0.01% | python | slot_nb_subtract |
| 0.01% | python | _Py_slot_tp_getattr_hook |
| 0.00% | python | PyFile_WriteObject |
| 0.00% | python | _PyCompile_EnsureArrayLargeEnough |
| 0.00% | python | atom_rule |
| 0.00% | python | recursive_issubclass |
| 0.00% | python | analyze_block |
| 0.00% | python | slot_sq_length |
| 0.00% | python | findchar |
| 0.00% | python | _Py_Executors_InvalidateDependency |
| 0.00% | python | merge_at |
| 0.00% | python | _PyArena_AddPyObject |
| 0.00% | python | builtin_print |
| 0.00% | python | builtin_issubclass |
| 0.00% | python | _PyFrame_ClearLocals |
| 0.00% | python | gen_close |
| 0.00% | python | PyStructSequence_SetItem |
| 0.00% | python | _PyFunction_FromConstructor |
| 0.00% | python | t_primary_rule |
| 0.00% | python | memmove@plt |
| 0.00% | python | remove_unreachable |
| 0.00% | python | os_fspath |
| 0.00% | python | _io__Buffered_read |
| 0.00% | python | PyThread_get_thread_ident_ex |
| 0.00% | python | delitem_knownhash_lock_held |
| 0.00% | python | partial_vectorcall |
| 0.00% | python | _PyTokenizer_Get |
| 0.00% | python | _textiowrapper_writeflush |
| 0.00% | python | remove_all_subclasses |
| 0.00% | python | unsafe_object_compare |
| 0.00% | python | classmethod_get |
| 0.00% | python | gallop_right |
| 0.00% | python | iter_iternext |
| 0.00% | python | stringio_iternext |
| 0.00% | python | expression_rule |
| 0.00% | python | _PyTypes_Fini |
| 0.00% | python | gallop_left |
| 0.00% | python | await_primary_rule |
| 0.00% | python | conjunction_rule |
| 0.00% | python | wrap_objobjargproc |
| 0.00% | python | strchr@plt |
| 0.00% | python | _Py_GetConfig |
| 0.00% | python | PyTime_MonotonicRaw |
| 0.00% | python | propagate_line_numbers |
| 0.00% | python | _PyDictKeys_StringLookup |
| 0.00% | python | factor_rule |
| 0.00% | python | __errno_location@plt |
| 0.00% | python | PyType_GetModule |
| 0.00% | python | find_frozen.part.0 |
| 0.00% | python | slot_tp_str |
| 0.00% | python | _Py_Specialize_LoadGlobal |
| 0.00% | python | duplicate_exits_without_lineno |
| 0.00% | python | _Py_VaBuildStack |

### str

2.54% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 0.43% | python | siphash13 |
| 0.15% | python | replace |
| 0.14% | python | _PyUnicode_FromUCS1.part.0 |
| 0.13% | python | _PyUnicode_JoinArray.part.0 |
| 0.11% | python | intern_constants |
| 0.10% | python | ascii_decode |
| 0.09% | python | PyUnicode_Substring |
| 0.09% | python | _copy_characters.part.0.constprop.0 |
| 0.07% | python | resize_compact |
| 0.07% | python | intern_common.part.0 |
| 0.06% | python | _PyUnicode_Equal |
| 0.05% | python | PyUnicode_Contains |
| 0.05% | python | PyUnicode_RichCompare |
| 0.05% | python | PyBytes_FromStringAndSize |
| 0.05% | python | _PyUnicode_InternImmortal |
| 0.04% | python | _PyUnicodeWriter_WriteStr |
| 0.04% | python | unicode_replace |
| 0.04% | python | PyUnicode_Format |
| 0.03% | python | _PyUnicode_FromUCS4.part.0 |
| 0.03% | python | _PyUnicode_InternMortal |
| 0.03% | python | unicode_decode_utf8.part.0 |
| 0.03% | python | _PyUnicodeWriter_PrepareInternal |
| 0.03% | python | unicode_hash |
| 0.02% | python | unicode_from_format |
| 0.02% | python | bytes_subscript |
| 0.02% | python | stringlib_bytes_join |
| 0.02% | python | PyUnicode_AsUCS4 |
| 0.02% | python | unicode_subscript |
| 0.02% | python | PyUnicode_FromWideChar |
| 0.02% | python | PyUnicode_Concat |
| 0.01% | python | split |
| 0.01% | python | _PyUnicode_ClearInterned |
| 0.01% | python | _PyUnicodeWriter_WriteSubstring |
| 0.01% | python | PyUnicode_DecodeUTF8 |
| 0.01% | python | PyBytes_Repr |
| 0.01% | python | PyUnicode_AsUTF8AndSize |
| 0.01% | python | unicode_rstrip |
| 0.01% | python | PyUnicode_Decode.part.0 |
| 0.01% | python | _PyUnicodeWriter_Init |
| 0.01% | python | unicode_decode_utf8_impl |
| 0.01% | python | _PyUnicodeWriter_WriteASCIIString |
| 0.01% | python | bytes_richcompare |
| 0.01% | python | PyUnicode_Splitlines |
| 0.01% | python | bytes_concat |
| 0.01% | python | _PyUnicode_IsAlpha |
| 0.01% | python | PyUnicode_InternFromString |
| 0.01% | python | PyUnicode_FromKindAndData |
| 0.01% | python | _PyUnicode_TranslateCharmap |
| 0.01% | python | unicode_rpartition |
| 0.01% | python | _PyUnicode_ToLowercase |
| 0.01% | python | PyUnicode_AsEncodedString.part.0 |
| 0.01% | python | unicode_join |
| 0.01% | python | unicode_startswith |
| 0.01% | python | unicode_encode_utf8 |
| 0.01% | python | unicode_repr |
| 0.01% | python | unicode_lower |
| 0.01% | python | _PyUnicodeWriter_Finish |
| 0.01% | python | PyUnicode_EncodeFSDefault |
| 0.01% | python | unicode_fromformat_write_utf8 |
| 0.01% | python | unicode_encode |
| 0.01% | python | unicode_decode_utf8 |
| 0.01% | python | PyUnicode_FromEncodedObject |
| 0.01% | python | bytes_length |
| 0.01% | python | PyUnicode_Append |
| 0.01% | python | _PyUnicode_IsLowercase |
| 0.01% | python | PyUnicode_FindChar |
| 0.01% | python | _PyUnicode_IsDigit |
| 0.01% | python | bytes_buffer_getbuffer |
| 0.01% | python | _PyUnicode_EqualToASCIIString |
| 0.01% | python | unicode_vectorcall |
| 0.00% | python | PyUnicode_FromString |
| 0.00% | python | PyBytes_FromStringAndSize.constprop.0 |
| 0.00% | python | unicode_endswith |
| 0.00% | python | _PyUnicode_IsDecimalDigit |
| 0.00% | python | PyUnicode_CompareWithASCIIString |
| 0.00% | python | _PyUnicodeWriter_WriteChar |
| 0.00% | python | _PyUnicode_EQ |
| 0.00% | python | stringlib__two_way |
| 0.00% | python | _PyUnicode_IsTitlecase |
| 0.00% | python | bytes_hash |
| 0.00% | python | unicode_length |
| 0.00% | python | _PyUnicode_IsPrintable |
| 0.00% | python | unicode_isupper |

### dict

2.32% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 0.39% | python | PyDict_GetItemRef |
| 0.36% | python | insertdict |
| 0.19% | python | dict_setdefault_ref_lock_held |
| 0.17% | python | insert_to_emptydict |
| 0.11% | python | _PyDict_GetItemRef_KnownHash |
| 0.10% | python | find_empty_slot |
| 0.10% | python | dict_get |
| 0.10% | python | build_indices_unicode |
| 0.09% | python | _PyDict_FromItems |
| 0.08% | python | dictiter_iternextitem |
| 0.08% | python | PyDict_SetItem |
| 0.06% | python | PyDict_Next |
| 0.06% | python | _PyDict_LoadGlobal |
| 0.04% | python | dictresize |
| 0.04% | python | PyDict_Contains |
| 0.04% | python | dict_merge |
| 0.04% | python | dict_subscript |
| 0.04% | python | PyDict_GetItemWithError |
| 0.03% | python | _PyDict_SetItem_Take2 |
| 0.03% | python | clone_combined_dict_keys.isra.0 |
| 0.03% | python | PyDict_GetItem |
| 0.03% | python | PyDict_Clear |
| 0.01% | python | dictiter_iternextkey |
| 0.01% | python | _PyDict_GetItem_KnownHash |
| 0.01% | python | _PyDict_DelItemIf |
| 0.01% | python | dict_ass_sub |
| 0.01% | python | dictiter_iternextvalue |
| 0.01% | python | dict_items |
| 0.01% | python | dict_tp_clear |
| 0.01% | python | PyDict_DelItem |
| 0.01% | python | PyDict_SetDefaultRef |
| 0.01% | python | PyDict_SetItemString |
| 0.00% | python | dict_pop |
| 0.00% | python | _PyDict_Next.part.0 |
| 0.00% | python | _PyDict_Next |
| 0.00% | python | _PyDict_Pop_KnownHash.part.0 |
| 0.00% | python | dict_update |

### miscobj

1.86% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 0.28% | python | set_lookkey |
| 0.27% | python | PySlice_AdjustIndices |
| 0.12% | python | _PyBuildSlice_ConsumeRefs |
| 0.12% | python | set_issubset_impl |
| 0.11% | python | set_add_entry |
| 0.09% | python | setiter_iternext |
| 0.08% | python | gen_iternext |
| 0.07% | python | make_gen |
| 0.07% | python | PySlice_Unpack |
| 0.05% | python | set_difference |
| 0.05% | python | _PySet_Contains |
| 0.05% | python | deque_append |
| 0.04% | python | range_iter |
| 0.03% | python | set_table_resize |
| 0.03% | python | enum_next |
| 0.03% | python | dequeiter_next |
| 0.03% | python | PyBuffer_Release |
| 0.02% | python | bytearray_ass_subscript |
| 0.02% | python | _PyGen_Finalize |
| 0.02% | python | PyBool_FromLong |
| 0.02% | python | _PyGen_FetchStopIterationValue |
| 0.02% | python | set_merge_lock_held.part.0 |
| 0.02% | python | range_subscript |
| 0.02% | python | deque_popleft |
| 0.02% | python | PyBuffer_FillInfo |
| 0.02% | python | range_vectorcall |
| 0.01% | python | set_intersection |
| 0.01% | python | _PyGen_SetStopIterationValue |
| 0.01% | python | PySet_Add |
| 0.01% | python | deque_clear.part.0 |
| 0.01% | python | _PySlice_GetLongIndices |
| 0.01% | python | PyGen_am_send |
| 0.01% | python | set_update_iterable_lock_held |
| 0.01% | python | set_richcompare |
| 0.01% | python | set_difference_update_internal |
| 0.01% | python | set_iter |
| 0.00% | python | set_vectorcall |
| 0.00% | python | set_add |
| 0.00% | python | range_reverse |
| 0.00% | python | set_discard |

### tuple

1.30% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 0.44% | python | tuplehash |
| 0.29% | python | _PyTuple_FromArray.part.0 |
| 0.25% | python | _PyTuple_FromStackRefSteal |
| 0.09% | python | tupletraverse |
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
| 0.00% | python | tuplegetter_descr_get |
| 0.00% | python | tupleconcat |
| 0.00% | python | PyTuple_GetItem |
| 0.00% | python | tuplelength |

### list

1.05% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 0.19% | python | list_ass_slice_lock_held |
| 0.14% | python | list_subscript |
| 0.09% | python | listiter_next |
| 0.08% | python | list_slice_lock_held.isra.0 |
| 0.05% | python | list_iter |
| 0.05% | python | PyList_Append |
| 0.05% | python | list_sort_impl |
| 0.05% | python | _list_extend |
| 0.05% | python | list_ass_subscript |
| 0.04% | python | list_extend_lock_held |
| 0.04% | python | list_contains |
| 0.04% | python | _PyList_AppendTakeRefListResize |
| 0.03% | python | list_concat |
| 0.03% | python | list_append |
| 0.02% | python | _PyList_FromArraySteal |
| 0.02% | python | list_pop |
| 0.02% | python | list_insert |
| 0.01% | python | list_length |
| 0.01% | python | list_richcompare |
| 0.01% | python | list_item |
| 0.00% | python | _PyList_Extend |
| 0.00% | python | list_remove |
| 0.00% | python | list_vectorcall |
| 0.00% | python | list_to_tuple |

### calls

0.64% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 0.09% | python | _PyFunction_Vectorcall |
| 0.07% | python | _Py_CheckFunctionResult |
| 0.07% | python | vgetargs1_impl |
| 0.07% | python | vgetargskeywords.constprop.0 |
| 0.05% | python | _PyArg_UnpackKeywords |
| 0.04% | python | PyArg_UnpackTuple |
| 0.03% | python | method_vectorcall |
| 0.03% | python | cfunction_vectorcall_FASTCALL_KEYWORDS |
| 0.02% | python | cfunction_vectorcall_O |
| 0.02% | python | method_vectorcall_FASTCALL_KEYWORDS_METHOD |
| 0.02% | python | _PyArg_UnpackKeywordsWithVararg |
| 0.02% | python | vectorcall_method |
| 0.02% | python | cfunction_vectorcall_NOARGS |
| 0.01% | python | method_vectorcall_VARARGS_KEYWORDS |
| 0.01% | python | method_vectorcall_O |
| 0.01% | python | PyArg_ParseTupleAndKeywords |
| 0.01% | python | PyArg_Parse |
| 0.01% | python | method_vectorcall_NOARGS |
| 0.01% | python | cfunction_call |
| 0.01% | python | method_vectorcall_VARARGS |
| 0.01% | python | PyArg_ParseTuple |
| 0.00% | python | cfunction_vectorcall_FASTCALL_KEYWORDS_METHOD |
| 0.00% | python | method_vectorcall_FASTCALL |

### exceptions

0.56% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 0.14% | python | _PyErr_SetObject.part.0 |
| 0.09% | python | PyErr_CheckSignals |
| 0.08% | python | PyCode_Addr2Line |
| 0.03% | python | PyErr_Occurred |
| 0.03% | python | PyErr_ExceptionMatches |
| 0.03% | python | _PyErr_Restore |
| 0.02% | python | PyTraceBack_Here |
| 0.02% | python | _PyErr_ExceptionMatches |
| 0.01% | python | BaseException_clear |
| 0.01% | python | PyErr_GetRaisedException |
| 0.01% | python | _PyErr_CreateException |
| 0.01% | python | BaseException_vectorcall |
| 0.01% | python | PyException_GetTraceback |
| 0.01% | python | PyErr_SetObject |
| 0.01% | python | PyErr_SetRaisedException |
| 0.01% | python | _PyErr_SetKeyError |
| 0.01% | python | AttributeError_init |
| 0.01% | python | PyFrame_GetCode |
| 0.01% | python | PyErr_GivenExceptionMatches |
| 0.00% | python | PyFrame_GetLineNumber |
| 0.00% | python | PyErr_Clear |

### float

0.42% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 0.16% | python | PyFloat_FromDouble |
| 0.09% | python | float_div |
| 0.04% | python | float_richcompare |
| 0.04% | python | float_mul |
| 0.03% | python | float_pow |
| 0.02% | python | float_sub |
| 0.01% | python | float_rem |
| 0.01% | python | float_add |
| 0.01% | python | PyFloat_AsDouble.part.0 |
| 0.01% | python | PyFloat_AsDouble |

### import

0.34% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 0.29% | python | r_object |
| 0.03% | python | r_string |
| 0.01% | python | PyImport_ImportModuleLevelObject |
| 0.01% | python | r_byte |

### compiler

0.15% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 0.06% | python | uop_optimize |
| 0.03% | python | tok_get_normal_mode |
| 0.03% | python | optimize_uops |
| 0.02% | python | tok_nextc |
| 0.01% | python | _PyJIT_Compile |

### async

0.06% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 0.04% | python | async_gen_asend_iternext |
| 0.02% | python | async_gen_anext |

### gil

0.04% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 0.03% | python | take_gil |
| 0.01% | python | drop_gil |
