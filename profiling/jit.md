
## 2to3

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 15.89% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 13.12% | `[JIT]` | `jit` | jit |
| 2.18% | `python` | `deduce_unreachable` | gc |
| 2.11% | `python` | `type_new` | memory |
| 2.00% | `python` | `gc_collect_region.isra.0` | gc |
| 1.85% | `python` | `tuple_dealloc` | memory |
| 1.64% | `python` | `sre_ucs1_match` | library |
| 1.63% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.58% | `python` | `visit_decref` | gc |
| 1.41% | `python` | `intern_common.part.0` | str |
| 1.12% | `python` | `PyDict_GetItemRef` | dict |
| 1.08% | `python` | `_PyCode_New` | interpreter |
| 0.96% | `python` | `visit_reachable` | gc |
| 0.80% | `python` | `r_object` | import |
| 0.77% | `python` | `list_dealloc` | memory |
| 0.75% | `python` | `_PyTuple_FromStackRefSteal` | tuple |
| 0.73% | `libc-2.31.so` | `__memcpy_avx_unaligned_erms` | libc |
| 0.70% | `python` | `PyObject_GetAttr` | dynamic |
| 0.68% | `python` | `siphash13` | str |
| 0.66% | `python` | `_Py_MakeCoro` | unknown |
| 0.64% | `python` | `gen_dealloc` | memory |
| 0.63% | `python` | `uop_optimize` | compiler |
| 0.60% | `python` | `PyObject_SetAttr` | dynamic |
| 0.58% | `python` | `PyUnicode_FromKindAndData` | str |
| 0.54% | `python` | `dict_dealloc` | memory |
| 0.53% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.48% | `python` | `unicode_dealloc` | memory |
| 0.48% | `python` | `PyDict_Contains` | dict |
| 0.44% | `python` | `insertdict` | dict |
| 0.44% | `libc-2.31.so` | `_int_malloc` | libc |
| 0.42% | `python` | `tok_get_normal_mode` | compiler |
| 0.42% | `python` | `listiter_dealloc` | memory |
| 0.40% | `python` | `subtype_traverse` | gc |
| 0.39% | `python` | `_PyCfg_OptimizeCodeUnit.constprop.0` | unknown |
| 0.39% | `python` | `_PyFunction_Vectorcall` | calls |
| 0.38% | `python` | `_PyPegen_fill_token` | interpreter |
| 0.38% | `python` | `PyDict_SetItem` | dict |
| 0.38% | `python` | `PyMem_Free` | memory |
| 0.35% | `python` | `find_name_in_mro` | lookup |
| 0.34% | `python` | `dict_traverse` | gc |
| 0.34% | `python` | `sre_ucs1_count` | library |
| 0.34% | `python` | `list_iter` | list |
| 0.33% | `python` | `_sre_SRE_Pattern_match` | library |
| 0.32% | `python` | `insert_to_emptydict` | dict |
| 0.32% | `python` | `list_subscript` | list |
| 0.31% | `python` | `type_ready` | dynamic |
| 0.31% | `python` | `dictresize` | dict |
| 0.29% | `python` | `_PyLexer_update_fstring_expr` | unknown |
| 0.29% | `python` | `sre_ucs2_charset.isra.0` | library |
| 0.29% | `libc-2.31.so` | `__memcmp_avx2_movbe` | libc |
| 0.29% | `python` | `code_dealloc` | memory |
| 0.29% | `python` | `PyMem_Malloc` | memory |
| 0.27% | `python` | `_PyObject_MakeTpCall` | dynamic |
| 0.27% | `python` | `code_hash` | unknown |
| 0.26% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 0.26% | `python` | `slot_tp_richcompare` | dynamic |
| 0.25% | `python` | `_PyAssemble_MakeCodeObject` | unknown |
| 0.25% | `python` | `_PyEvalFramePushAndInit` | interpreter |

## async_generators

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 21.46% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 8.42% | `python` | `_PyErr_SetObject` | exceptions |
| 4.33% | `python` | `StopIteration_dealloc` | memory |
| 3.94% | `[JIT]` | `jit` | jit |
| 3.63% | `python` | `_PyObject_MakeTpCall` | dynamic |
| 3.60% | `python` | `BaseException_new` | memory |
| 2.55% | `python` | `StopIteration_init` | dynamic |
| 2.46% | `python` | `async_gen_asend_send` | async |
| 2.40% | `python` | `gen_send_ex` | unknown |
| 2.26% | `python` | `tuple_dealloc` | memory |
| 2.12% | `python` | `async_gen_asend_new` | memory |
| 2.10% | `python` | `gen_send_ex2` | unknown |
| 1.84% | `python` | `PyErr_ExceptionMatches` | exceptions |
| 1.80% | `python` | `async_gen_asend_dealloc` | memory |
| 1.62% | `python` | `PyErr_GivenExceptionMatches` | exceptions |
| 1.56% | `python` | `_PyAsyncGenValueWrapperNew` | memory |
| 1.52% | `python` | `async_gen_wrapped_val_dealloc` | memory |
| 1.31% | `python` | `async_gen_unwrap_value.isra.0` | async |
| 0.98% | `python` | `long_add` | int |
| 0.98% | `python` | `PyObject_CallFinalizerFromDealloc` | memory |
| 0.94% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.93% | `python` | `_PyGen_FetchStopIterationValue.cold` | miscobj |
| 0.86% | `python` | `type_call` | dynamic |
| 0.85% | `python` | `_PyGen_SetStopIterationValue` | miscobj |
| 0.79% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.78% | `python` | `_PyEval_EvalFrameDefault.cold` | interpreter |
| 0.71% | `python` | `PyType_GenericAlloc` | memory |
| 0.71% | `python` | `long_dealloc` | memory |
| 0.67% | `python` | `deduce_unreachable` | gc |
| 0.59% | `python` | `visit_decref` | gc |
| 0.59% | `python` | `subtype_dealloc` | memory |
| 0.56% | `python` | `range_subscript` | miscobj |
| 0.51% | `python` | `visit_reachable` | gc |
| 0.49% | `python` | `_Py_Dealloc` | memory |
| 0.48% | `python` | `_Py_NewReference` | memory |
| 0.48% | `python` | `subtype_traverse` | gc |
| 0.46% | `python` | `_PyFunction_Vectorcall` | calls |
| 0.42% | `python` | `type_new` | memory |
| 0.41% | `python` | `visit_add_to_container` | gc |
| 0.40% | `python` | `gc_collect_region.isra.0` | gc |
| 0.39% | `python` | `_PyEval_GetANext` | interpreter |
| 0.39% | `python` | `PyTraceBack_Here` | exceptions |
| 0.38% | `python` | `make_range_object` | unknown |
| 0.37% | `python` | `_PyGen_FetchStopIterationValue` | miscobj |
| 0.36% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.36% | `python` | `_PyObject_New` | memory |
| 0.36% | `python` | `gen_dealloc` | memory |
| 0.31% | `python` | `BaseException_vectorcall` | exceptions |
| 0.30% | `python` | `PyObject_CallOneArg` | dynamic |
| 0.29% | `python` | `weakref_dealloc` | memory |
| 0.28% | `python` | `_PyFrame_MakeAndSetFrameObject` | unknown |
| 0.28% | `python` | `BaseException_dealloc` | memory |
| 0.27% | `python` | `range_dealloc` | memory |
| 0.25% | `python` | `long_richcompare` | int |
| 0.25% | `python` | `async_gen_init_hooks` | async |

## async_tree

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 18.28% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 7.24% | `[JIT]` | `jit` | jit |
| 6.27% | `python` | `deduce_unreachable` | gc |
| 5.07% | `python` | `visit_decref` | gc |
| 5.06% | `python` | `visit_add_to_container` | gc |
| 4.87% | `python` | `visit_reachable` | gc |
| 4.25% | `python` | `gc_collect_region.isra.0` | gc |
| 2.27% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.31% | `python` | `_PyFunction_Vectorcall` | calls |
| 1.25% | `python` | `subtype_traverse` | gc |
| 1.23% | `python` | `_PyObject_GC_New` | gc |
| 1.13% | `python` | `tuple_dealloc` | memory |
| 1.05% | `python` | `PyObject_VectorcallMethod` | dynamic |
| 1.01% | `python` | `PyObject_GC_Del` | gc |
| 1.00% | `python` | `PyObject_GetAttr` | dynamic |
| 0.95% | `python` | `context_tp_dealloc` | memory |
| 0.89% | `python` | `slot_tp_init` | unknown |
| 0.88% | `python` | `_PyObject_MakeTpCall` | dynamic |
| 0.88% | `python` | `gen_traverse` | gc |
| 0.79% | `python` | `_PyObject_GC_NewVar` | gc |
| 0.78% | `python` | `gen_dealloc` | memory |
| 0.75% | `python` | `PyType_GenericNew` | memory |
| 0.73% | `python` | `meth_dealloc` | memory |
| 0.72% | `_asyncio.cpython-314-x86_64-linux-gnu.so` | `TaskObj_traverse` | library |
| 0.72% | `python` | `PyDict_GetItemRef` | dict |
| 0.69% | `python` | `list_dealloc` | memory |
| 0.66% | `python` | `_PyGC_Collect` | gc |
| 0.60% | `python` | `object_new` | memory |
| 0.57% | `python` | `subtype_dealloc` | memory |
| 0.56% | `python` | `type_new` | memory |
| 0.53% | `python` | `clear_slots` | unknown |
| 0.53% | `python` | `insertdict` | dict |
| 0.53% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.41% | `python` | `_PyArg_UnpackKeywords` | calls |
| 0.41% | `python` | `dict_dealloc` | memory |
| 0.40% | `python` | `dict_traverse` | gc |
| 0.40% | `python` | `method_get` | dynamic |
| 0.39% | `python` | `PyObject_RichCompareBool` | dynamic |
| 0.39% | `python` | `insert_to_emptydict` | dict |
| 0.39% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.35% | `python` | `PyLong_FromLong` | int |
| 0.34% | `python` | `list_resize` | list |
| 0.32% | `python` | `dict_setdefault_ref_lock_held` | dict |
| 0.32% | `python` | `func_traverse` | gc |
| 0.32% | `python` | `dictresize` | dict |
| 0.32% | `python` | `intern_common.part.0` | str |
| 0.30% | `python` | `PyObject_VisitManagedDict` | dynamic |
| 0.30% | `[kernel.kallsyms]` | `native_irq_return_iret` | kernel |
| 0.30% | `python` | `PyUnicode_RichCompare` | str |
| 0.28% | `_asyncio.cpython-314-x86_64-linux-gnu.so` | `TaskObj_clear` | library |
| 0.27% | `[kernel.kallsyms]` | `clear_page_erms` | kernel |
| 0.26% | `python` | `long_dealloc` | memory |
| 0.26% | `python` | `PyObject_SetAttr` | dynamic |
| 0.25% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.25% | `python` | `_Py_dict_lookup` | lookup |

## async_tree_cpu_io_mixed

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 20.73% | `python` | `k_mul` | int |
| 14.44% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 4.85% | `[JIT]` | `jit` | jit |
| 4.55% | `python` | `deduce_unreachable` | gc |
| 3.85% | `python` | `visit_decref` | gc |
| 3.42% | `python` | `visit_reachable` | gc |
| 3.41% | `python` | `visit_add_to_container` | gc |
| 2.97% | `python` | `gc_collect_region.isra.0` | gc |
| 2.67% | `python` | `long_dealloc` | memory |
| 1.56% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.40% | `python` | `_PyLong_New` | memory |
| 0.96% | `python` | `subtype_traverse` | gc |
| 0.90% | `python` | `_PyFunction_Vectorcall` | calls |
| 0.84% | `python` | `PyObject_GetAttr` | dynamic |
| 0.81% | `python` | `long_mul_method` | int |
| 0.79% | `python` | `tuple_dealloc` | memory |
| 0.78% | `python` | `context_tp_dealloc` | memory |
| 0.76% | `python` | `_PyObject_GC_New` | gc |
| 0.75% | `python` | `gen_dealloc` | memory |
| 0.72% | `math.cpython-314-x86_64-linux-gnu.so` | `factorial_partial_product` | library |
| 0.65% | `python` | `PyObject_VectorcallMethod` | dynamic |
| 0.58% | `python` | `gen_traverse` | gc |
| 0.58% | `python` | `meth_dealloc` | memory |
| 0.57% | `python` | `PyObject_GC_Del` | gc |
| 0.56% | `python` | `slot_tp_init` | unknown |
| 0.56% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.53% | `python` | `_PyObject_MakeTpCall` | dynamic |
| 0.53% | `python` | `_PyObject_GC_NewVar` | gc |
| 0.52% | `math.cpython-314-x86_64-linux-gnu.so` | `math_factorial` | library |
| 0.50% | `python` | `list_dealloc` | memory |
| 0.47% | `python` | `long_lshift_int64` | int |
| 0.47% | `python` | `_PyGC_Collect` | gc |
| 0.46% | `python` | `PyDict_GetItemRef` | dict |
| 0.45% | `_asyncio.cpython-314-x86_64-linux-gnu.so` | `TaskObj_traverse` | library |
| 0.45% | `python` | `PyType_GenericNew` | memory |
| 0.45% | `python` | `subtype_dealloc` | memory |
| 0.43% | `python` | `PyNumber_Multiply` | dynamic |
| 0.41% | `python` | `object_new` | memory |
| 0.36% | `python` | `clear_slots` | unknown |
| 0.35% | `python` | `type_new` | memory |
| 0.35% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.34% | `python` | `PyLong_FromUnsignedLong` | int |
| 0.32% | `python` | `insertdict` | dict |
| 0.29% | `python` | `PyObject_RichCompareBool` | dynamic |
| 0.28% | `python` | `_PyArg_UnpackKeywords` | calls |
| 0.27% | `python` | `method_get` | dynamic |
| 0.27% | `python` | `insert_to_emptydict` | dict |
| 0.26% | `python` | `PyObject_SetAttr` | dynamic |
| 0.25% | `python` | `_Py_Dealloc` | memory |

## async_tree_cpu_io_mixed_tg

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 21.11% | `python` | `k_mul` | int |
| 14.44% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 4.63% | `python` | `deduce_unreachable` | gc |
| 4.48% | `python` | `visit_add_to_container` | gc |
| 4.30% | `python` | `visit_decref` | gc |
| 3.86% | `python` | `visit_reachable` | gc |
| 3.07% | `[JIT]` | `jit` | jit |
| 3.02% | `python` | `gc_collect_region.isra.0` | gc |
| 2.81% | `python` | `long_dealloc` | memory |
| 1.52% | `python` | `_PyLong_New` | memory |
| 1.47% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.08% | `python` | `subtype_traverse` | gc |
| 0.97% | `python` | `PyObject_GetAttr` | dynamic |
| 0.80% | `python` | `_PyFunction_Vectorcall` | calls |
| 0.80% | `python` | `long_mul_method` | int |
| 0.79% | `python` | `gen_traverse` | gc |
| 0.76% | `math.cpython-314-x86_64-linux-gnu.so` | `factorial_partial_product` | library |
| 0.73% | `python` | `tuple_dealloc` | memory |
| 0.69% | `python` | `_PyObject_GC_NewVar` | gc |
| 0.68% | `python` | `PyObject_VectorcallMethod` | dynamic |
| 0.66% | `python` | `PyObject_GC_Del` | gc |
| 0.59% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.58% | `python` | `PyDict_GetItemRef` | dict |
| 0.58% | `python` | `gen_dealloc` | memory |
| 0.57% | `python` | `_PyObject_GC_New` | gc |
| 0.54% | `math.cpython-314-x86_64-linux-gnu.so` | `math_factorial` | library |
| 0.54% | `python` | `slot_tp_init` | unknown |
| 0.51% | `_asyncio.cpython-314-x86_64-linux-gnu.so` | `TaskObj_traverse` | library |
| 0.50% | `python` | `PyType_GenericNew` | memory |
| 0.49% | `python` | `_PyGC_Collect` | gc |
| 0.48% | `python` | `_PyObject_MakeTpCall` | dynamic |
| 0.46% | `python` | `object_new` | memory |
| 0.45% | `python` | `long_lshift_int64` | int |
| 0.45% | `python` | `meth_dealloc` | memory |
| 0.41% | `python` | `clear_slots` | unknown |
| 0.40% | `python` | `PyNumber_Multiply` | dynamic |
| 0.40% | `python` | `set_traverse` | gc |
| 0.39% | `python` | `subtype_dealloc` | memory |
| 0.36% | `python` | `type_new` | memory |
| 0.34% | `python` | `PyLong_FromUnsignedLong` | int |
| 0.34% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.32% | `python` | `list_dealloc` | memory |
| 0.31% | `python` | `PyObject_RichCompareBool` | dynamic |
| 0.30% | `python` | `dict_traverse` | gc |
| 0.26% | `python` | `insertdict` | dict |
| 0.25% | `python` | `method_get` | dynamic |

## async_tree_io

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 19.09% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 8.55% | `python` | `deduce_unreachable` | gc |
| 7.52% | `python` | `visit_add_to_container` | gc |
| 7.10% | `python` | `visit_decref` | gc |
| 6.58% | `python` | `visit_reachable` | gc |
| 6.00% | `python` | `gc_collect_region.isra.0` | gc |
| 4.65% | `[JIT]` | `jit` | jit |
| 2.07% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.49% | `python` | `gen_traverse` | gc |
| 1.45% | `python` | `subtype_traverse` | gc |
| 1.17% | `python` | `slot_tp_richcompare` | dynamic |
| 1.03% | `python` | `_PyGC_Collect` | gc |
| 0.94% | `python` | `_PyFunction_Vectorcall` | calls |
| 0.86% | `python` | `tuple_dealloc` | memory |
| 0.73% | `python` | `PyObject_GetAttr` | dynamic |
| 0.72% | `python` | `_PyObject_GC_New` | gc |
| 0.67% | `python` | `PyObject_GC_Del` | gc |
| 0.65% | `_heapq.cpython-314-x86_64-linux-gnu.so` | `_heapq_heappop` | library |
| 0.64% | `python` | `slot_tp_init` | unknown |
| 0.63% | `python` | `PyObject_VectorcallMethod` | dynamic |
| 0.62% | `_asyncio.cpython-314-x86_64-linux-gnu.so` | `TaskObj_traverse` | library |
| 0.57% | `python` | `PyObject_RichCompareBool` | dynamic |
| 0.56% | `python` | `_PyObject_GC_NewVar` | gc |
| 0.55% | `python` | `_PyObject_MakeTpCall` | dynamic |
| 0.53% | `python` | `object_new` | memory |
| 0.52% | `python` | `gen_dealloc` | memory |
| 0.51% | `python` | `list_dealloc` | memory |
| 0.50% | `python` | `PyType_GenericNew` | memory |
| 0.49% | `python` | `meth_dealloc` | memory |
| 0.45% | `python` | `clear_slots` | unknown |
| 0.42% | `python` | `context_tp_dealloc` | memory |
| 0.41% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.40% | `python` | `PyDict_GetItemRef` | dict |
| 0.36% | `python` | `insert_to_emptydict` | dict |
| 0.36% | `python` | `list_resize` | list |
| 0.34% | `python` | `_PySuper_Lookup` | dynamic |
| 0.33% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.32% | `python` | `_PyObject_Call` | dynamic |
| 0.32% | `_asyncio.cpython-314-x86_64-linux-gnu.so` | `FutureObj_traverse` | library |
| 0.31% | `python` | `PyObject_VisitManagedDict` | dynamic |
| 0.31% | `python` | `subtype_dealloc` | memory |
| 0.30% | `python` | `_PyArg_UnpackKeywords` | calls |
| 0.28% | `[kernel.kallsyms]` | `clear_page_erms` | kernel |
| 0.27% | `python` | `dict_traverse` | gc |
| 0.27% | `python` | `dict_dealloc` | memory |
| 0.27% | `python` | `tuple_traverse` | gc |
| 0.26% | `python` | `PyLong_FromLong` | int |
| 0.25% | `python` | `func_traverse` | gc |

## async_tree_io_tg

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 16.85% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 9.92% | `python` | `deduce_unreachable` | gc |
| 9.41% | `python` | `visit_add_to_container` | gc |
| 8.13% | `python` | `visit_decref` | gc |
| 7.57% | `python` | `visit_reachable` | gc |
| 7.07% | `python` | `gc_collect_region.isra.0` | gc |
| 2.98% | `[JIT]` | `jit` | jit |
| 2.13% | `python` | `gen_traverse` | gc |
| 1.72% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.64% | `python` | `subtype_traverse` | gc |
| 1.32% | `python` | `_PyGC_Collect` | gc |
| 1.04% | `python` | `slot_tp_richcompare` | dynamic |
| 1.03% | `python` | `_PyFunction_Vectorcall` | calls |
| 0.82% | `python` | `gen_dealloc` | memory |
| 0.81% | `python` | `tuple_dealloc` | memory |
| 0.80% | `python` | `PyObject_GetAttr` | dynamic |
| 0.74% | `_asyncio.cpython-314-x86_64-linux-gnu.so` | `TaskObj_traverse` | library |
| 0.60% | `_heapq.cpython-314-x86_64-linux-gnu.so` | `_heapq_heappop` | library |
| 0.57% | `python` | `_PyObject_GC_NewVar` | gc |
| 0.57% | `python` | `PyObject_VectorcallMethod` | dynamic |
| 0.56% | `python` | `_PyObject_GC_New` | gc |
| 0.56% | `python` | `PyObject_GC_Del` | gc |
| 0.54% | `python` | `set_traverse` | gc |
| 0.52% | `python` | `slot_tp_init` | unknown |
| 0.47% | `python` | `PyObject_RichCompareBool` | dynamic |
| 0.46% | `python` | `meth_dealloc` | memory |
| 0.46% | `python` | `_PyObject_MakeTpCall` | dynamic |
| 0.45% | `python` | `object_new` | memory |
| 0.42% | `python` | `PyType_GenericNew` | memory |
| 0.41% | `python` | `subtype_dealloc` | memory |
| 0.40% | `python` | `PyDict_GetItemRef` | dict |
| 0.39% | `python` | `clear_slots` | unknown |
| 0.38% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.33% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.33% | `_asyncio.cpython-314-x86_64-linux-gnu.so` | `FutureObj_traverse` | library |
| 0.32% | `python` | `list_dealloc` | memory |
| 0.29% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.29% | `[kernel.kallsyms]` | `clear_page_erms` | kernel |
| 0.28% | `python` | `PyObject_VisitManagedDict` | dynamic |
| 0.28% | `python` | `_PyObject_Call` | dynamic |

## async_tree_memoization

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 20.68% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 6.67% | `python` | `deduce_unreachable` | gc |
| 6.54% | `[JIT]` | `jit` | jit |
| 5.37% | `python` | `visit_decref` | gc |
| 4.92% | `python` | `visit_add_to_container` | gc |
| 4.92% | `python` | `visit_reachable` | gc |
| 4.21% | `python` | `gc_collect_region.isra.0` | gc |
| 2.30% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.38% | `python` | `subtype_traverse` | gc |
| 1.35% | `python` | `_PyFunction_Vectorcall` | calls |
| 1.20% | `python` | `PyObject_GetAttr` | dynamic |
| 1.11% | `python` | `tuple_dealloc` | memory |
| 1.02% | `python` | `_PyObject_GC_New` | gc |
| 1.00% | `python` | `context_tp_dealloc` | memory |
| 0.94% | `python` | `PyObject_VectorcallMethod` | dynamic |
| 0.83% | `python` | `slot_tp_init` | unknown |
| 0.79% | `python` | `gen_traverse` | gc |
| 0.77% | `python` | `PyObject_GC_Del` | gc |
| 0.77% | `python` | `gen_dealloc` | memory |
| 0.75% | `python` | `meth_dealloc` | memory |
| 0.74% | `python` | `_PyObject_MakeTpCall` | dynamic |
| 0.73% | `python` | `_PyGC_Collect` | gc |
| 0.67% | `python` | `PyDict_GetItemRef` | dict |
| 0.65% | `python` | `list_dealloc` | memory |
| 0.65% | `python` | `_PyObject_GC_NewVar` | gc |
| 0.63% | `_asyncio.cpython-314-x86_64-linux-gnu.so` | `TaskObj_traverse` | library |
| 0.62% | `python` | `PyType_GenericNew` | memory |
| 0.59% | `python` | `object_new` | memory |
| 0.52% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.51% | `python` | `subtype_dealloc` | memory |
| 0.51% | `python` | `clear_slots` | unknown |
| 0.47% | `python` | `type_new` | memory |
| 0.47% | `python` | `method_get` | dynamic |
| 0.45% | `python` | `insertdict` | dict |
| 0.41% | `python` | `PyObject_RichCompareBool` | dynamic |
| 0.40% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.39% | `python` | `PyObject_SetAttr` | dynamic |
| 0.38% | `python` | `_PyArg_UnpackKeywords` | calls |
| 0.38% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.36% | `python` | `insert_to_emptydict` | dict |
| 0.34% | `python` | `dict_traverse` | gc |
| 0.34% | `python` | `dict_dealloc` | memory |
| 0.33% | `python` | `PyIter_Send` | dynamic |
| 0.31% | `python` | `PyLong_FromLong` | int |
| 0.31% | `python` | `list_resize` | list |
| 0.31% | `python` | `dict_setdefault_ref_lock_held` | dict |
| 0.29% | `python` | `intern_common.part.0` | str |
| 0.27% | `python` | `PyObject_VisitManagedDict` | dynamic |
| 0.27% | `python` | `tuple_traverse` | gc |
| 0.27% | `python` | `PyUnicode_RichCompare` | str |
| 0.26% | `python` | `list_traverse` | gc |
| 0.26% | `python` | `dictresize` | dict |

## async_tree_memoization_tg

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 20.80% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 6.90% | `python` | `deduce_unreachable` | gc |
| 6.42% | `python` | `visit_add_to_container` | gc |
| 6.10% | `python` | `visit_decref` | gc |
| 5.45% | `python` | `visit_reachable` | gc |
| 4.62% | `python` | `gc_collect_region.isra.0` | gc |
| 4.14% | `[JIT]` | `jit` | jit |
| 2.21% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.52% | `python` | `subtype_traverse` | gc |
| 1.43% | `python` | `PyObject_GetAttr` | dynamic |
| 1.18% | `python` | `gen_traverse` | gc |
| 1.12% | `python` | `_PyFunction_Vectorcall` | calls |
| 0.98% | `python` | `tuple_dealloc` | memory |
| 0.94% | `python` | `PyObject_VectorcallMethod` | dynamic |
| 0.87% | `python` | `_PyObject_GC_NewVar` | gc |
| 0.87% | `python` | `PyObject_GC_Del` | gc |
| 0.79% | `python` | `_PyObject_GC_New` | gc |
| 0.76% | `python` | `PyDict_GetItemRef` | dict |
| 0.75% | `_asyncio.cpython-314-x86_64-linux-gnu.so` | `TaskObj_traverse` | library |
| 0.74% | `python` | `slot_tp_init` | unknown |
| 0.71% | `python` | `_PyGC_Collect` | gc |
| 0.69% | `python` | `gen_dealloc` | memory |
| 0.68% | `python` | `meth_dealloc` | memory |
| 0.67% | `python` | `_PyObject_MakeTpCall` | dynamic |
| 0.64% | `python` | `PyType_GenericNew` | memory |
| 0.61% | `python` | `object_new` | memory |
| 0.54% | `python` | `set_traverse` | gc |
| 0.52% | `python` | `subtype_dealloc` | memory |
| 0.51% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.50% | `python` | `type_new` | memory |
| 0.48% | `python` | `clear_slots` | unknown |
| 0.45% | `python` | `PyObject_RichCompareBool` | dynamic |
| 0.43% | `python` | `list_dealloc` | memory |
| 0.41% | `python` | `method_get` | dynamic |
| 0.40% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.39% | `python` | `context_tp_dealloc` | memory |
| 0.35% | `python` | `set_discard_entry` | miscobj |
| 0.35% | `python` | `insertdict` | dict |
| 0.33% | `python` | `_PyArg_UnpackKeywords` | calls |
| 0.32% | `python` | `dict_traverse` | gc |
| 0.32% | `python` | `dict_setdefault_ref_lock_held` | dict |
| 0.32% | `python` | `PyIter_Send` | dynamic |
| 0.31% | `python` | `intern_common.part.0` | str |
| 0.29% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.27% | `_asyncio.cpython-314-x86_64-linux-gnu.so` | `task_step_impl` | library |
| 0.26% | `python` | `PyLong_FromLong` | int |
| 0.26% | `python` | `_PyCode_New` | interpreter |
| 0.26% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.26% | `python` | `PyObject_VisitManagedDict` | dynamic |
| 0.25% | `[kernel.kallsyms]` | `clear_page_erms` | kernel |
| 0.25% | `python` | `_Py_dict_lookup` | lookup |
| 0.25% | `python` | `dict_dealloc` | memory |

## async_tree_tg

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 19.17% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 6.66% | `python` | `visit_add_to_container` | gc |
| 6.35% | `python` | `deduce_unreachable` | gc |
| 5.77% | `python` | `visit_decref` | gc |
| 5.41% | `python` | `visit_reachable` | gc |
| 4.44% | `python` | `gc_collect_region.isra.0` | gc |
| 4.39% | `[JIT]` | `jit` | jit |
| 2.13% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.42% | `python` | `subtype_traverse` | gc |
| 1.32% | `python` | `PyObject_GetAttr` | dynamic |
| 1.16% | `python` | `PyObject_GC_Del` | gc |
| 1.15% | `python` | `_PyFunction_Vectorcall` | calls |
| 1.12% | `python` | `gen_traverse` | gc |
| 1.09% | `python` | `PyObject_VectorcallMethod` | dynamic |
| 1.04% | `python` | `_PyObject_GC_NewVar` | gc |
| 1.01% | `python` | `tuple_dealloc` | memory |
| 0.94% | `python` | `_PyObject_GC_New` | gc |
| 0.88% | `python` | `PyDict_GetItemRef` | dict |
| 0.82% | `python` | `slot_tp_init` | unknown |
| 0.79% | `python` | `PyType_GenericNew` | memory |
| 0.73% | `python` | `_PyObject_MakeTpCall` | dynamic |
| 0.71% | `_asyncio.cpython-314-x86_64-linux-gnu.so` | `TaskObj_traverse` | library |
| 0.67% | `python` | `object_new` | memory |
| 0.65% | `python` | `meth_dealloc` | memory |
| 0.63% | `python` | `_PyGC_Collect` | gc |
| 0.60% | `python` | `gen_dealloc` | memory |
| 0.57% | `python` | `set_traverse` | gc |
| 0.56% | `python` | `type_new` | memory |
| 0.54% | `python` | `subtype_dealloc` | memory |
| 0.50% | `python` | `clear_slots` | unknown |
| 0.46% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.45% | `python` | `PyObject_RichCompareBool` | dynamic |
| 0.43% | `[kernel.kallsyms]` | `clear_page_erms` | kernel |
| 0.43% | `python` | `list_dealloc` | memory |
| 0.42% | `python` | `insertdict` | dict |
| 0.41% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.40% | `[kernel.kallsyms]` | `native_irq_return_iret` | kernel |
| 0.39% | `python` | `dict_setdefault_ref_lock_held` | dict |
| 0.37% | `python` | `dict_traverse` | gc |
| 0.37% | `python` | `_PyArg_UnpackKeywords` | calls |
| 0.34% | `python` | `PyLong_FromLong` | int |
| 0.32% | `python` | `intern_common.part.0` | str |
| 0.32% | `[kernel.kallsyms]` | `rmqueue` | kernel |
| 0.32% | `python` | `method_get` | dynamic |
| 0.31% | `python` | `PyUnicode_RichCompare` | str |
| 0.31% | `[kernel.kallsyms]` | `sync_regs` | kernel |
| 0.29% | `python` | `insert_to_emptydict` | dict |
| 0.29% | `python` | `long_dealloc` | memory |
| 0.29% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.28% | `python` | `_PyCode_New` | interpreter |
| 0.28% | `python` | `dict_dealloc` | memory |
| 0.28% | `python` | `_Py_dict_lookup` | lookup |
| 0.27% | `python` | `PyObject_VisitManagedDict` | dynamic |
| 0.26% | `python` | `PyLong_FromUnsignedLongLong` | int |
| 0.25% | `python` | `method_vectorcall` | calls |

## asyncio_websockets

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 64.65% | `libz.so.1.2.11` | `crc32_combine64` | library |
| 20.45% | `libz.so.1.2.11` | `inflateBackEnd` | library |
| 2.73% | `libc-2.31.so` | `__memcpy_avx_unaligned_erms` | libc |
| 1.42% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 0.42% | `libz.so.1.2.11` | `inflateCodesUsed` | library |
| 0.41% | `python` | `type_new` | memory |
| 0.27% | `python` | `deduce_unreachable` | gc |
| 0.27% | `[JIT]` | `jit` | jit |
| 0.26% | `python` | `intern_common.part.0` | str |

## bpe_tokeniser

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 25.47% | `[JIT]` | `jit` | jit |
| 6.84% | `python` | `tuple_dealloc` | memory |
| 5.94% | `python` | `list_dealloc` | memory |
| 3.96% | `python` | `dict_subscript` | dict |
| 2.80% | `python` | `zip_new` | memory |
| 2.56% | `python` | `_PyObject_MakeTpCall` | dynamic |
| 2.38% | `python` | `list_subscript` | list |
| 2.14% | `python` | `insertdict` | dict |
| 2.03% | `python` | `list_iter` | list |
| 1.98% | `python` | `listiter_dealloc` | memory |
| 1.70% | `python` | `listiter_next` | list |
| 1.55% | `python` | `deduce_unreachable` | gc |
| 1.54% | `python` | `zip_next` | unknown |
| 1.49% | `python` | `slot_mp_subscript` | unknown |
| 1.44% | `python` | `tuple_hash` | tuple |
| 1.44% | `python` | `tuple_richcompare` | tuple |
| 1.40% | `python` | `wrapperdescr_call` | unknown |
| 1.37% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 1.32% | `python` | `PyList_New` | memory |
| 1.30% | `python` | `visit_decref` | gc |
| 1.29% | `python` | `zip_dealloc` | memory |
| 1.27% | `python` | `list_traverse` | gc |
| 1.24% | `python` | `_PyLong_Add` | int |
| 1.22% | `python` | `visit_reachable` | gc |
| 1.14% | `python` | `slot_mp_ass_subscript` | unknown |
| 0.97% | `python` | `PyObject_Size` | dynamic |
| 0.97% | `python` | `_PyLong_Subtract` | int |
| 0.85% | `python` | `PyObject_GetItem` | dynamic |
| 0.83% | `python` | `_PyObject_GC_New` | gc |
| 0.82% | `python` | `PyObject_RichCompare` | dynamic |
| 0.80% | `python` | `gc_collect_region.isra.0` | gc |
| 0.72% | `python` | `_PyList_AppendTakeRefListResize` | list |
| 0.72% | `python` | `_PyTuple_FromStackRefSteal` | tuple |
| 0.71% | `python` | `wrap_objobjargproc` | unknown |
| 0.70% | `python` | `PyObject_GC_Del` | gc |
| 0.68% | `python` | `PyMem_Malloc` | memory |
| 0.66% | `python` | `visit_add_to_container` | gc |
| 0.63% | `python` | `_PyObject_Malloc` | memory |
| 0.53% | `python` | `method_vectorcall_O` | calls |
| 0.52% | `python` | `PyNumber_AsSsize_t` | dynamic |
| 0.50% | `python` | `method_dealloc` | memory |
| 0.50% | `python` | `PyTuple_New` | memory |
| 0.49% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.49% | `python` | `func_descr_get` | unknown |
| 0.47% | `python` | `PyLong_FromSsize_t` | int |
| 0.46% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.46% | `python` | `PyArg_UnpackTuple` | calls |
| 0.40% | `python` | `_Py_Dealloc` | memory |
| 0.40% | `python` | `PyObject_SetItem` | dynamic |
| 0.40% | `python` | `dictiter_iternextkey` | dict |
| 0.38% | `python` | `_PyType_LookupRef` | lookup |
| 0.37% | `python` | `PyObject_GetIter` | dynamic |
| 0.36% | `python` | `bytes_richcompare` | str |
| 0.36% | `python` | `_PyFunction_Vectorcall` | calls |
| 0.35% | `python` | `_PyList_FromStackRefSteal` | list |
| 0.30% | `python` | `method_vectorcall` | calls |
| 0.29% | `python` | `dict_traverse` | gc |
| 0.29% | `python` | `tuple_traverse` | gc |
| 0.29% | `python` | `type_call` | dynamic |
| 0.28% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.25% | `python` | `PyObject_Hash` | dynamic |
| 0.25% | `python` | `builtin_max` | unknown |

## chaos

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 24.60% | `[JIT]` | `jit` | jit |
| 21.69% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 3.47% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 3.32% | `python` | `_PyFloat_FromDouble_ConsumeInputs` | float |
| 2.10% | `python` | `_PyLong_Subtract` | int |
| 1.63% | `python` | `subtype_dealloc` | memory |
| 1.50% | `python` | `_PyLong_Add` | int |
| 1.37% | `python` | `range_vectorcall` | miscobj |
| 1.34% | `python` | `float_div` | float |
| 1.24% | `python` | `PyType_GenericAlloc` | memory |
| 1.18% | `python` | `type_new` | memory |
| 1.14% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 1.09% | `python` | `float_sub` | float |
| 1.04% | `libm-2.31.so` | `__ieee754_pow_fma` | library |
| 0.99% | `python` | `range_iter` | miscobj |
| 0.88% | `python` | `float_dealloc` | memory |
| 0.86% | `python` | `PyNumber_TrueDivide` | dynamic |
| 0.81% | `python` | `PyObject_GC_Del` | gc |
| 0.81% | `python` | `PyNumber_Subtract` | dynamic |
| 0.79% | `python` | `PyLong_AsDouble` | int |
| 0.72% | `python` | `float_richcompare` | float |
| 0.68% | `python` | `tuple_dealloc` | memory |
| 0.68% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.65% | `python` | `float_pow` | float |
| 0.64% | `python` | `PyObject_RichCompare` | dynamic |
| 0.64% | `python` | `convert_to_double` | unknown |
| 0.63% | `python` | `intern_common.part.0` | str |
| 0.63% | `python` | `_PyCode_New` | interpreter |
| 0.62% | `python` | `PyLong_FromLong` | int |
| 0.57% | `python` | `visit_decref` | gc |
| 0.55% | `python` | `deduce_unreachable` | gc |
| 0.53% | `python` | `PyObject_Free` | dynamic |
| 0.53% | `python` | `vectorcall_maybe.constprop.0` | unknown |
| 0.51% | `python` | `range_dealloc` | memory |
| 0.50% | `python` | `gc_collect_region.isra.0` | gc |
| 0.44% | `python` | `PyType_IsSubtype` | dynamic |
| 0.42% | `python` | `PyObject_GetAttr` | dynamic |
| 0.42% | `python` | `list_dealloc` | memory |
| 0.38% | `python` | `r_object` | import |
| 0.37% | `python` | `long_sub` | int |
| 0.35% | `python` | `visit_reachable` | gc |
| 0.34% | `python` | `PyObject_GetIter` | dynamic |
| 0.33% | `python` | `PyUnicode_FromKindAndData` | str |
| 0.30% | `python` | `_Py_Dealloc` | memory |
| 0.28% | `libc-2.31.so` | `__memcpy_avx_unaligned_erms` | libc |
| 0.25% | `python` | `siphash13` | str |

## comprehensions

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 37.06% | `[JIT]` | `jit` | jit |
| 7.50% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 4.10% | `python` | `dict_get` | dict |
| 2.91% | `python` | `PyFunction_NewWithQualName` | memory |
| 2.28% | `python` | `_PyList_AppendTakeRefListResize` | list |
| 2.19% | `python` | `listiter_dealloc` | memory |
| 2.03% | `python` | `list_dealloc` | memory |
| 2.01% | `python` | `PyDict_GetItemRef` | dict |
| 1.65% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.64% | `python` | `unsafe_tuple_compare` | unknown |
| 1.56% | `python` | `list_iter` | list |
| 1.54% | `python` | `func_dealloc` | memory |
| 1.50% | `python` | `gen_dealloc` | memory |
| 1.49% | `python` | `insertdict` | dict |
| 1.05% | `python` | `type_new` | memory |
| 1.00% | `python` | `_Py_MakeCoro` | unknown |
| 0.98% | `python` | `long_hash` | int |
| 0.88% | `python` | `tuple_dealloc` | memory |
| 0.83% | `python` | `long_richcompare` | int |
| 0.75% | `libc-2.31.so` | `__memcpy_avx_unaligned_erms` | libc |
| 0.67% | `python` | `PyObject_RichCompare` | dynamic |
| 0.65% | `python` | `_Py_type_getattro` | lookup |
| 0.62% | `python` | `_PyObject_Malloc` | memory |
| 0.60% | `python` | `dictresize` | dict |
| 0.59% | `python` | `list_sort_impl` | list |
| 0.58% | `python` | `intern_common.part.0` | str |
| 0.57% | `python` | `PyObject_GetIter` | dynamic |
| 0.55% | `python` | `deduce_unreachable` | gc |
| 0.53% | `python` | `_PyCode_New` | interpreter |
| 0.50% | `python` | `_PyTuple_FromStackRefSteal` | tuple |
| 0.49% | `python` | `builtin_any` | unknown |
| 0.49% | `python` | `gc_collect_region.isra.0` | gc |
| 0.47% | `python` | `PyObject_GetAttr` | dynamic |
| 0.45% | `python` | `gen_close` | unknown |
| 0.45% | `python` | `visit_decref` | gc |
| 0.44% | `python` | `dict_dealloc` | memory |
| 0.39% | `python` | `list_resize` | list |
| 0.39% | `python` | `PyObject_Hash` | dynamic |
| 0.39% | `python` | `r_object` | import |
| 0.35% | `python` | `_PyList_FromStackRefSteal` | list |
| 0.34% | `python` | `_PyDict_SetItem_Take2` | dict |
| 0.32% | `python` | `gen_iternext` | miscobj |
| 0.32% | `python` | `tuple_subscript` | tuple |
| 0.31% | `python` | `visit_reachable` | gc |
| 0.31% | `python` | `_Py_Dealloc` | memory |
| 0.30% | `python` | `PyUnicode_FromKindAndData` | str |
| 0.28% | `python` | `insert_to_emptydict` | dict |
| 0.28% | `python` | `unsafe_object_compare` | unknown |

## concurrent_imap

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 14.49% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 4.09% | `[JIT]` | `jit` | jit |
| 2.68% | `python` | `type_new` | memory |
| 2.17% | `[kernel.kallsyms]` | `memset_erms` | kernel |
| 1.72% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.69% | `python` | `intern_common.part.0` | str |
| 1.39% | `python` | `_PyCode_New` | interpreter |
| 1.18% | `python` | `tuple_dealloc` | memory |
| 0.95% | `python` | `r_object` | import |
| 0.84% | `python` | `do_string_format` | unknown |
| 0.77% | `python` | `PyUnicode_FromKindAndData` | str |
| 0.77% | `[kernel.kallsyms]` | `zap_pte_range.isra.0` | kernel |
| 0.76% | `python` | `deduce_unreachable` | gc |
| 0.76% | `libc-2.31.so` | `__memcpy_avx_unaligned_erms` | libc |
| 0.72% | `[kernel.kallsyms]` | `perf_event_alloc` | kernel |
| 0.67% | `python` | `long_dealloc` | memory |
| 0.66% | `python` | `visit_decref` | gc |
| 0.61% | `python` | `list_dealloc` | memory |
| 0.59% | `python` | `subtype_dealloc` | memory |
| 0.57% | `python` | `PyDict_GetItemRef` | dict |
| 0.54% | `[kernel.kallsyms]` | `page_counter_cancel` | kernel |
| 0.52% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.52% | `python` | `siphash13` | str |
| 0.51% | `python` | `PyObject_GetAttr` | dynamic |
| 0.46% | `[kernel.kallsyms]` | `psi_task_change` | kernel |
| 0.45% | `python` | `visit_reachable` | gc |
| 0.45% | `python` | `gc_collect_region.isra.0` | gc |
| 0.45% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.45% | `[kernel.kallsyms]` | `_raw_spin_lock` | kernel |
| 0.41% | `[kernel.kallsyms]` | `clear_page_erms` | kernel |
| 0.40% | `python` | `insertdict` | dict |
| 0.39% | `[kernel.kallsyms]` | `memcpy_erms` | kernel |
| 0.39% | `[kernel.kallsyms]` | `clear_bhb_loop` | kernel |
| 0.39% | `python` | `find_name_in_mro` | lookup |
| 0.38% | `[kernel.kallsyms]` | `mutex_lock` | kernel |
| 0.38% | `python` | `_PyUnicode_ToDecimalDigit` | str |
| 0.38% | `python` | `dict_dealloc` | memory |
| 0.37% | `[kernel.kallsyms]` | `copy_page` | kernel |
| 0.37% | `python` | `unicode_dealloc` | memory |
| 0.36% | `[kernel.kallsyms]` | `find_vma` | kernel |
| 0.35% | `python` | `type_ready` | dynamic |
| 0.34% | `libc-2.31.so` | `_int_malloc` | libc |
| 0.34% | `python` | `PyBytes_FromStringAndSize` | str |
| 0.34% | `python` | `uop_optimize` | compiler |
| 0.32% | `python` | `PyObject_GC_Del` | gc |
| 0.31% | `libpthread-2.31.so` | `__pthread_mutex_lock` | library |
| 0.31% | `python` | `PyDict_SetItem` | dict |
| 0.31% | `[kernel.kallsyms]` | `native_irq_return_iret` | kernel |
| 0.31% | `[kernel.kallsyms]` | `native_flush_tlb_one_user` | kernel |
| 0.30% | `python` | `unicode_encode` | str |
| 0.30% | `python` | `PyObject_SetAttr` | dynamic |
| 0.29% | `[kernel.kallsyms]` | `do_syscall_64` | kernel |
| 0.29% | `python` | `dictresize` | dict |
| 0.29% | `[kernel.kallsyms]` | `kmem_cache_alloc_trace` | kernel |
| 0.28% | `python` | `_PyFunction_Vectorcall` | calls |
| 0.28% | `[kernel.kallsyms]` | `copy_user_enhanced_fast_string` | kernel |
| 0.28% | `python` | `_Py_dict_lookup` | lookup |
| 0.28% | `libc-2.31.so` | `_int_free` | libc |
| 0.28% | `[kernel.kallsyms]` | `copy_process` | kernel |
| 0.28% | `[kernel.kallsyms]` | `native_sched_clock` | kernel |
| 0.28% | `python` | `_PyObject_LookupSpecialMethod` | dynamic |
| 0.27% | `[kernel.kallsyms]` | `mutex_unlock` | kernel |
| 0.27% | `[kernel.kallsyms]` | `_raw_spin_lock_irqsave` | kernel |
| 0.27% | `python` | `meth_dealloc` | memory |
| 0.26% | `python` | `PyObject_Vectorcall` | dynamic |
| 0.26% | `[kernel.kallsyms]` | `memcg_kmem_get_cache` | kernel |
| 0.25% | `python` | `take_gil` | gil |
| 0.25% | `[kernel.kallsyms]` | `kmem_cache_alloc` | kernel |

## coroutines

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 44.94% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 13.75% | `python` | `gen_dealloc` | memory |
| 6.77% | `python` | `_PyObject_GC_NewVar` | gc |
| 5.16% | `python` | `_PyEval_EvalFrameDefault.cold` | interpreter |
| 3.90% | `python` | `make_gen` | miscobj |
| 2.74% | `python` | `long_sub` | int |
| 2.65% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 2.52% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 2.05% | `python` | `_Py_MakeCoro` | unknown |
| 1.63% | `python` | `long_add` | int |
| 1.52% | `python` | `_PyEval_GetAwaitable` | interpreter |
| 1.09% | `python` | `_PyCoro_GetAwaitableIter` | unknown |
| 0.71% | `python` | `type_new` | memory |
| 0.55% | `python` | `_PyGen_yf` | miscobj |
| 0.37% | `python` | `_PyCode_New` | interpreter |
| 0.37% | `python` | `intern_common.part.0` | str |
| 0.36% | `python` | `visit_decref` | gc |
| 0.33% | `python` | `deduce_unreachable` | gc |
| 0.31% | `python` | `gc_collect_region.isra.0` | gc |
| 0.30% | `[JIT]` | `jit` | jit |
| 0.26% | `python` | `r_object` | import |

## coverage

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 20.19% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 8.22% | `tracer.cpython-314-x86_64-linux-gnu.so` | `CTracer_trace` | library |
| 4.70% | `python` | `intern_common.part.0` | str |
| 3.96% | `python` | `call_instrumentation_vector` | interpreter |
| 3.62% | `python` | `siphash13` | str |
| 3.05% | `python` | `PyUnicode_InternFromString` | str |
| 2.86% | `python` | `frame_dealloc` | memory |
| 2.74% | `python` | `PySet_Add` | miscobj |
| 2.46% | `python` | `_Py_dict_lookup` | lookup |
| 2.43% | `python` | `PyObject_SetAttr` | dynamic |
| 2.35% | `python` | `_PyObject_VectorcallTstate.lto_priv.1` | dynamic |
| 2.19% | `python` | `_PyFrame_MakeAndSetFrameObject` | unknown |
| 1.94% | `python` | `call_one_instrument` | unknown |
| 1.90% | `python` | `PyLong_FromLong` | int |
| 1.85% | `python` | `unicode_dealloc` | memory |
| 1.71% | `python` | `_PyEval_LoadGlobalStackRef` | interpreter |
| 1.64% | `python` | `dict_getitem` | dict |
| 1.63% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.21% | `python` | `call_trace_func.isra.0` | unknown |
| 1.04% | `python` | `type_new` | memory |
| 0.73% | `python` | `_PyCode_GetCode` | interpreter |
| 0.67% | `[JIT]` | `jit` | jit |
| 0.64% | `python` | `long_sub` | int |
| 0.64% | `python` | `PyEval_GetFrame` | interpreter |
| 0.62% | `python` | `deduce_unreachable` | gc |
| 0.62% | `python` | `visit_decref` | gc |
| 0.60% | `python` | `long_hash` | int |
| 0.57% | `python` | `PyFrame_GetCode` | exceptions |
| 0.56% | `python` | `_PyCode_New` | interpreter |
| 0.54% | `tracer.cpython-314-x86_64-linux-gnu.so` | `CTracer_set_pdata_stack` | library |
| 0.53% | `python` | `long_add` | int |
| 0.53% | `python` | `_Py_CheckFunctionResult` | calls |
| 0.53% | `python` | `gc_collect_region.isra.0` | gc |
| 0.49% | `libc-2.31.so` | `__memcmp_avx2_movbe` | libc |
| 0.48% | `python` | `frame_settrace` | unknown |
| 0.46% | `python` | `PyObject_SetAttrString` | dynamic |
| 0.45% | `python` | `visit_reachable` | gc |
| 0.43% | `python` | `hashtable_unicode_hash` | unknown |
| 0.43% | `python` | `compute_line` | unknown |
| 0.42% | `python` | `_Py_call_instrumentation_arg` | unknown |
| 0.40% | `python` | `_PyEval_GetFrame` | interpreter |
| 0.39% | `libc-2.31.so` | `__strlen_avx2` | libc |
| 0.39% | `python` | `PyFrame_GetLineNumber` | exceptions |
| 0.39% | `libc-2.31.so` | `__memcpy_avx_unaligned_erms` | libc |
| 0.37% | `python` | `r_object` | import |
| 0.34% | `python` | `getset_set` | unknown |
| 0.29% | `python` | `PyUnicode_FromKindAndData` | str |
| 0.26% | `python` | `tuple_dealloc` | memory |

## crypto_pyaes

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 28.57% | `[JIT]` | `jit` | jit |
| 8.93% | `python` | `long_dealloc` | memory |
| 8.03% | `python` | `long_bitwise` | int |
| 4.56% | `python` | `long_rshift` | int |
| 4.15% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 4.01% | `python` | `long_and` | int |
| 3.66% | `python` | `long_mod` | int |
| 3.03% | `python` | `_PyLong_New` | memory |
| 1.62% | `python` | `binary_op` | unknown |
| 1.41% | `python` | `PyNumber_And` | dynamic |
| 1.15% | `python` | `_PyLong_Add` | int |
| 1.08% | `python` | `list_dealloc` | memory |
| 1.06% | `python` | `type_new` | memory |
| 0.97% | `python` | `long_xor` | int |
| 0.96% | `python` | `_PyObject_Free` | memory |
| 0.84% | `python` | `PyNumber_Rshift` | dynamic |
| 0.79% | `python` | `PyNumber_Remainder` | dynamic |
| 0.76% | `python` | `_PyObject_Malloc` | memory |
| 0.75% | `python` | `range_vectorcall` | miscobj |
| 0.75% | `python` | `_PyLong_FromSTwoDigits` | int |
| 0.66% | `python` | `_Py_Dealloc` | memory |
| 0.65% | `python` | `intern_common.part.0` | str |
| 0.63% | `python` | `deduce_unreachable` | gc |
| 0.63% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.58% | `python` | `PyLong_FromLong` | int |
| 0.58% | `python` | `maybe_small_long` | unknown |
| 0.57% | `python` | `dict_get` | dict |
| 0.56% | `python` | `range_iter` | miscobj |
| 0.55% | `python` | `_PyCode_New` | interpreter |
| 0.52% | `python` | `visit_decref` | gc |
| 0.50% | `libc-2.31.so` | `__memcpy_avx_unaligned_erms` | libc |
| 0.45% | `python` | `r_object` | import |
| 0.45% | `python` | `gc_collect_region.isra.0` | gc |
| 0.32% | `python` | `visit_reachable` | gc |
| 0.29% | `python` | `PyObject_Free` | dynamic |
| 0.27% | `python` | `tuple_dealloc` | memory |
| 0.27% | `python` | `PyUnicode_FromKindAndData` | str |
| 0.26% | `python` | `range_dealloc` | memory |

## deepcopy

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 21.83% | `[JIT]` | `jit` | jit |
| 19.07% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 4.45% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 4.14% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 1.96% | `python` | `dict_get` | dict |
| 1.86% | `python` | `long_dealloc` | memory |
| 1.86% | `python` | `insertdict` | dict |
| 1.50% | `python` | `_PyLong_New` | memory |
| 1.36% | `python` | `_PySet_Contains` | miscobj |
| 1.27% | `python` | `PyDict_GetItemRef` | dict |
| 1.16% | `python` | `tuple_dealloc` | memory |
| 1.00% | `python` | `list_dealloc` | memory |
| 1.00% | `python` | `long_hash` | int |
| 0.96% | `python` | `PyObject_GetAttr` | dynamic |
| 0.91% | `python` | `insert_to_emptydict` | dict |
| 0.85% | `python` | `PySys_Audit` | unknown |
| 0.83% | `python` | `type_new` | memory |
| 0.75% | `python` | `dict_dealloc` | memory |
| 0.73% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.70% | `python` | `PyObject_GetOptionalAttr` | dynamic |
| 0.67% | `python` | `dictiter_iternextitem` | dict |
| 0.61% | `python` | `builtin_id` | unknown |
| 0.60% | `python` | `long_richcompare` | int |
| 0.57% | `python` | `list_resize` | list |
| 0.56% | `python` | `method_get` | dynamic |
| 0.55% | `python` | `list_append` | list |
| 0.54% | `python` | `BaseException_vectorcall` | exceptions |
| 0.52% | `python` | `PyMem_Realloc` | memory |
| 0.52% | `python` | `PyTraceBack_Here` | exceptions |
| 0.52% | `python` | `PyObject_RichCompareBool` | dynamic |
| 0.50% | `python` | `_PyObject_GenericGetAttrWithDict` | dynamic |
| 0.48% | `python` | `object_new` | memory |
| 0.47% | `python` | `PyObject_Hash` | dynamic |
| 0.46% | `python` | `meth_dealloc` | memory |
| 0.42% | `python` | `intern_common.part.0` | str |
| 0.41% | `python` | `object_isinstance` | dynamic |
| 0.40% | `python` | `deduce_unreachable` | gc |
| 0.40% | `python` | `_PyObject_GC_New` | gc |
| 0.39% | `python` | `_PyFrame_MakeAndSetFrameObject` | unknown |
| 0.39% | `python` | `_PyCode_New` | interpreter |
| 0.38% | `python` | `slot_tp_init` | unknown |
| 0.37% | `python` | `dict_items` | dict |
| 0.34% | `python` | `visit_decref` | gc |
| 0.34% | `python` | `gc_collect_region.isra.0` | gc |
| 0.34% | `python` | `BaseException_dealloc` | memory |
| 0.33% | `python` | `_Py_type_getattro` | lookup |
| 0.33% | `python` | `dict_merge` | dict |
| 0.31% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.31% | `python` | `cell_dealloc` | memory |
| 0.31% | `python` | `r_object` | import |
| 0.31% | `python` | `PyObject_GC_Del` | gc |
| 0.30% | `python` | `_PyObject_Calloc` | memory |
| 0.29% | `python` | `dictitems_iter` | unknown |
| 0.29% | `python` | `dictiter_dealloc` | memory |
| 0.28% | `libc-2.31.so` | `__memcpy_avx_unaligned_erms` | libc |
| 0.26% | `python` | `subtype_dealloc` | memory |
| 0.26% | `python` | `PyMem_Free` | memory |
| 0.26% | `python` | `PyList_New` | memory |
| 0.26% | `python` | `method_dealloc` | memory |
| 0.25% | `python` | `func_descr_get` | unknown |

## deltablue

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 35.11% | `[JIT]` | `jit` | jit |
| 22.07% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 6.04% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.64% | `python` | `deduce_unreachable` | gc |
| 1.44% | `python` | `gc_collect_region.isra.0` | gc |
| 1.24% | `python` | `type_new` | memory |
| 1.21% | `python` | `visit_decref` | gc |
| 1.15% | `python` | `_PySuper_Lookup` | dynamic |
| 1.07% | `python` | `_PyObject_GetMethod` | dynamic |
| 0.77% | `python` | `_Py_type_getattro` | lookup |
| 0.75% | `python` | `PyObject_GetAttr` | dynamic |
| 0.72% | `python` | `method_dealloc` | memory |
| 0.70% | `python` | `intern_common.part.0` | str |
| 0.67% | `python` | `cm_descr_get` | unknown |
| 0.63% | `python` | `subtype_traverse` | gc |
| 0.60% | `python` | `visit_reachable` | gc |
| 0.58% | `python` | `_PyCode_New` | interpreter |
| 0.51% | `python` | `subtype_dealloc` | memory |
| 0.47% | `python` | `list_iter` | list |
| 0.46% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.44% | `python` | `PyType_GenericNew` | memory |
| 0.42% | `python` | `listiter_dealloc` | memory |
| 0.41% | `python` | `r_object` | import |
| 0.40% | `libc-2.31.so` | `__memcpy_avx_unaligned_erms` | libc |
| 0.37% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.34% | `python` | `PyUnicode_FromKindAndData` | str |
| 0.33% | `python` | `tuple_dealloc` | memory |
| 0.33% | `python` | `_PyLong_Add` | int |
| 0.32% | `python` | `list_dealloc` | memory |
| 0.31% | `python` | `_PyObject_Malloc` | memory |
| 0.30% | `python` | `long_dealloc` | memory |
| 0.29% | `python` | `PyType_GenericAlloc` | memory |
| 0.29% | `python` | `PyObject_GC_Del` | gc |
| 0.28% | `python` | `visit_add_to_container` | gc |
| 0.28% | `python` | `PyObject_SetAttr` | dynamic |
| 0.27% | `python` | `uop_optimize` | compiler |
| 0.26% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.26% | `python` | `PyUnicode_Format` | str |

## django_template

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 25.03% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 11.49% | `[JIT]` | `jit` | jit |
| 3.22% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 2.16% | `python` | `type_new` | memory |
| 1.60% | `python` | `object_isinstance` | dynamic |
| 1.44% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 1.35% | `python` | `tuple_dealloc` | memory |
| 1.22% | `python` | `deduce_unreachable` | gc |
| 1.21% | `python` | `insertdict` | dict |
| 1.21% | `python` | `intern_common.part.0` | str |
| 1.05% | `python` | `gc_collect_region.isra.0` | gc |
| 0.99% | `python` | `PyDict_GetItemRef` | dict |
| 0.99% | `python` | `visit_decref` | gc |
| 0.89% | `python` | `_PyCode_New` | interpreter |
| 0.88% | `python` | `unicode_replace` | str |
| 0.79% | `python` | `PyType_GenericAlloc` | memory |
| 0.79% | `python` | `PyObject_GetOptionalAttr` | dynamic |
| 0.79% | `python` | `PyFunction_NewWithQualName` | memory |
| 0.75% | `python` | `PyObject_GC_Del` | gc |
| 0.75% | `python` | `list_dealloc` | memory |
| 0.73% | `python` | `visit_reachable` | gc |
| 0.66% | `python` | `r_object` | import |
| 0.65% | `python` | `tupleiter_dealloc` | memory |
| 0.63% | `python` | `long_to_decimal_string_internal` | int |
| 0.60% | `libc-2.31.so` | `__memcpy_avx_unaligned_erms` | libc |
| 0.59% | `python` | `dict_dealloc` | memory |
| 0.58% | `python` | `_PyObject_GC_New` | gc |
| 0.58% | `python` | `_PyObject_GenericGetAttrWithDict` | dynamic |
| 0.56% | `python` | `PyUnicode_FromKindAndData` | str |
| 0.53% | `python` | `listiter_dealloc` | memory |
| 0.51% | `python` | `unicode_dealloc` | memory |
| 0.46% | `python` | `_Py_MakeCoro` | unknown |
| 0.44% | `python` | `tuple_iter` | tuple |
| 0.43% | `python` | `list_iter` | list |
| 0.43% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.42% | `python` | `slot_sq_contains` | unknown |
| 0.42% | `python` | `siphash13` | str |
| 0.42% | `python` | `func_dealloc` | memory |
| 0.41% | `python` | `list_vectorcall` | list |
| 0.38% | `libz.so.1.2.11` | `inflateBackEnd` | library |
| 0.37% | `python` | `slot_mp_ass_subscript` | unknown |
| 0.36% | `python` | `_PyObject_Calloc` | memory |
| 0.34% | `python` | `PyObject_GetIter` | dynamic |
| 0.34% | `python` | `builtin_getattr` | lookup |
| 0.34% | `python` | `code_dealloc` | memory |
| 0.33% | `python` | `_PyUnicode_JoinArray` | str |
| 0.33% | `python` | `func_descr_get` | unknown |
| 0.32% | `python` | `gen_dealloc` | memory |
| 0.29% | `python` | `_PyObject_MakeTpCall` | dynamic |
| 0.28% | `python` | `list_subscript` | list |
| 0.28% | `python` | `meth_dealloc` | memory |
| 0.28% | `python` | `method_get` | dynamic |
| 0.27% | `libc-2.31.so` | `_int_malloc` | libc |
| 0.27% | `python` | `_Py_dict_lookup` | lookup |
| 0.26% | `python` | `chain_next` | unknown |
| 0.26% | `python` | `type_ready` | dynamic |
| 0.26% | `python` | `subtype_dealloc` | memory |
| 0.25% | `python` | `find_name_in_mro` | lookup |

## docutils

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 19.45% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 8.93% | `[JIT]` | `jit` | jit |
| 7.09% | `python` | `sre_ucs1_match` | library |
| 3.47% | `python` | `deduce_unreachable` | gc |
| 2.77% | `python` | `sre_ucs2_charset.isra.0` | library |
| 2.69% | `python` | `PyObject_GetAttr` | dynamic |
| 2.67% | `python` | `gc_collect_region.isra.0` | gc |
| 2.07% | `python` | `find_name_in_mro` | lookup |
| 1.93% | `python` | `visit_add_to_container` | gc |
| 1.89% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.78% | `python` | `visit_decref` | gc |
| 1.76% | `python` | `list_dealloc` | memory |
| 1.21% | `libc-2.31.so` | `__memcpy_avx_unaligned_erms` | libc |
| 1.06% | `python` | `PyObject_SetAttr` | dynamic |
| 0.98% | `python` | `PyDict_GetItemRef` | dict |
| 0.97% | `python` | `_PyObject_GetMethod` | dynamic |
| 0.84% | `python` | `_PyUnicode_JoinArray` | str |
| 0.81% | `python` | `visit_reachable` | gc |
| 0.77% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.76% | `python` | `object_isinstance` | dynamic |
| 0.73% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.72% | `python` | `tuple_dealloc` | memory |
| 0.70% | `python` | `dict_traverse` | gc |
| 0.70% | `python` | `list_subscript` | list |
| 0.69% | `python` | `PyMem_Free` | memory |
| 0.68% | `python` | `subtype_traverse` | gc |
| 0.66% | `python` | `list_traverse` | gc |
| 0.58% | `python` | `PyUnicode_Format` | str |
| 0.58% | `python` | `PyMem_Malloc` | memory |
| 0.58% | `python` | `insertdict` | dict |
| 0.57% | `python` | `_PyObject_GenericGetAttrWithDict` | dynamic |
| 0.56% | `python` | `unicode_dealloc` | memory |
| 0.55% | `python` | `dict_dealloc` | memory |
| 0.49% | `python` | `_sre_SRE_Pattern_match` | library |
| 0.49% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.46% | `python` | `sre_ucs1_count` | library |
| 0.46% | `python` | `func_descr_get` | unknown |
| 0.45% | `python` | `_PyObject_GC_New` | gc |
| 0.42% | `python` | `_Py_dict_lookup` | lookup |
| 0.40% | `python` | `_PyTuple_FromStackRefSteal` | tuple |
| 0.39% | `python` | `PyDict_Contains` | dict |
| 0.39% | `libc-2.31.so` | `_int_malloc` | libc |
| 0.37% | `python` | `uop_optimize` | compiler |
| 0.37% | `python` | `listiter_dealloc` | memory |
| 0.36% | `python` | `method_dealloc` | memory |
| 0.35% | `python` | `list_vectorcall` | list |
| 0.34% | `python` | `_Py_type_getattro` | lookup |
| 0.33% | `python` | `_PyGC_Collect` | gc |
| 0.33% | `python` | `list_iter` | list |
| 0.31% | `python` | `PyList_New` | memory |
| 0.30% | `python` | `getset_get` | dynamic |
| 0.29% | `python` | `gen_dealloc` | memory |
| 0.26% | `python` | `_Py_MakeCoro` | unknown |

## dulwich_log

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 23.43% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 5.68% | `[JIT]` | `jit` | jit |
| 3.00% | `libz.so.1.2.11` | `inflateCodesUsed` | library |
| 1.87% | `libz.so.1.2.11` | `inflateBackEnd` | library |
| 1.70% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.66% | `libz.so.1.2.11` | `inflate` | library |
| 1.33% | `python` | `PyBytes_FromStringAndSize` | str |
| 1.21% | `python` | `type_new` | memory |
| 0.93% | `python` | `tuple_dealloc` | memory |
| 0.92% | `python` | `object_dealloc` | memory |
| 0.79% | `python` | `visit_decref` | gc |
| 0.76% | `python` | `long_dealloc` | memory |
| 0.74% | `python` | `intern_common.part.0` | str |
| 0.73% | `libc-2.31.so` | `__memcpy_avx_unaligned_erms` | libc |
| 0.73% | `python` | `deduce_unreachable` | gc |
| 0.67% | `python` | `list_dealloc` | memory |
| 0.66% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.62% | `python` | `_PyCode_New` | interpreter |
| 0.60% | `python` | `siphash13` | str |
| 0.60% | `python` | `gc_collect_region.isra.0` | gc |
| 0.59% | `[kernel.kallsyms]` | `copy_user_enhanced_fast_string` | kernel |
| 0.57% | `[kernel.kallsyms]` | `__d_lookup_rcu` | kernel |
| 0.51% | `python` | `r_object` | import |
| 0.49% | `python` | `unicode_dealloc` | memory |
| 0.47% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.47% | `python` | `PyDict_GetItemRef` | dict |
| 0.45% | `python` | `visit_reachable` | gc |
| 0.44% | `python` | `_PyTuple_FromStackRefSteal` | tuple |
| 0.42% | `python` | `PyUnicode_FSConverter` | str |
| 0.40% | `python` | `PyList_New` | memory |
| 0.39% | `python` | `slot_tp_init` | unknown |
| 0.39% | `libc-2.31.so` | `_int_malloc` | libc |
| 0.39% | `python` | `unicode_encode` | str |
| 0.36% | `libc-2.31.so` | `__memcmp_avx2_movbe` | libc |
| 0.35% | `python` | `_Py_Dealloc` | memory |
| 0.34% | `python` | `find_name_in_mro` | lookup |
| 0.34% | `python` | `_PyLong_FromBytes` | int |
| 0.34% | `python` | `PyUnicode_FromKindAndData` | str |
| 0.33% | `python` | `_PyLong_Add` | int |
| 0.33% | `[kernel.kallsyms]` | `link_path_walk.part.0` | kernel |
| 0.33% | `python` | `PyType_GenericAlloc` | memory |
| 0.32% | `python` | `PyObject_GC_Del` | gc |
| 0.32% | `python` | `PyUnicode_New` | memory |
| 0.32% | `python` | `bytes_richcompare` | str |
| 0.31% | `python` | `clear_slots` | unknown |
| 0.31% | `python` | `subtype_dealloc` | memory |
| 0.30% | `python` | `PySlice_Unpack` | miscobj |
| 0.30% | `python` | `_PyObject_GC_New` | gc |
| 0.29% | `python` | `PyObject_RichCompare` | dynamic |
| 0.28% | `python` | `_PyObject_MakeTpCall` | dynamic |
| 0.27% | `python` | `_PyObject_Malloc` | memory |
| 0.27% | `libpthread-2.31.so` | `__pthread_mutex_lock` | library |
| 0.27% | `python` | `object_new` | memory |
| 0.26% | `libc-2.31.so` | `__libc_malloc` | libc |
| 0.26% | `python` | `PyFunction_NewWithQualName` | memory |
| 0.26% | `python` | `PyTraceBack_Here` | exceptions |

## fannkuch

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 32.56% | `[JIT]` | `jit` | jit |
| 10.75% | `python` | `list_subscript` | list |
| 8.33% | `python` | `list_ass_slice_lock_held` | list |
| 8.06% | `python` | `list_dealloc` | memory |
| 3.94% | `python` | `slice_dealloc` | memory |
| 3.62% | `python` | `list_new_prealloc` | memory |
| 3.27% | `python` | `_PyLong_Add` | int |
| 2.61% | `python` | `PySlice_New` | memory |
| 2.52% | `python` | `list_ass_subscript` | list |
| 1.80% | `python` | `PySlice_Unpack` | miscobj |
| 1.56% | `python` | `_PyEval_SliceIndex` | interpreter |
| 1.56% | `python` | `_PyBuildSlice_ConsumeRefs` | miscobj |
| 1.20% | `libc-2.31.so` | `__memcpy_avx_unaligned_erms` | libc |
| 1.14% | `python` | `ins1` | unknown |
| 1.06% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 1.03% | `python` | `PyObject_GetItem` | dynamic |
| 0.89% | `python` | `PyNumber_AsSsize_t` | dynamic |
| 0.86% | `python` | `_PyLong_Subtract` | int |
| 0.82% | `python` | `list_pop` | list |
| 0.71% | `python` | `PyMem_Malloc` | memory |
| 0.70% | `python` | `PyObject_SetItem` | dynamic |
| 0.60% | `python` | `PySequence_Fast` | dynamic |
| 0.56% | `python` | `_Py_Dealloc` | memory |
| 0.49% | `python` | `PySlice_AdjustIndices` | miscobj |
| 0.45% | `python` | `type_new` | memory |
| 0.42% | `python` | `PyMem_Free` | memory |
| 0.40% | `python` | `list_insert` | list |
| 0.37% | `python` | `PyList_New` | memory |
| 0.35% | `python` | `PyLong_AsSsize_t` | int |
| 0.35% | `python` | `_PyNumber_Index` | dynamic |
| 0.30% | `python` | `list_resize` | list |
| 0.26% | `python` | `intern_common.part.0` | str |

## float

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 23.93% | `[JIT]` | `jit` | jit |
| 11.00% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 2.59% | `libm-2.31.so` | `__sin_fma` | library |
| 2.43% | `python` | `_PyFloat_FromDouble_ConsumeInputs` | float |
| 2.33% | `libm-2.31.so` | `__cos_fma` | library |
| 2.31% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 2.14% | `python` | `subtype_traverse` | gc |
| 2.14% | `python` | `visit_decref` | gc |
| 1.87% | `python` | `slot_tp_init` | unknown |
| 1.83% | `python` | `float_div` | float |
| 1.80% | `python` | `deduce_unreachable` | gc |
| 1.74% | `python` | `_PyObject_Malloc` | memory |
| 1.63% | `python` | `object_new` | memory |
| 1.55% | `python` | `visit_reachable` | gc |
| 1.55% | `python` | `visit_add_to_container` | gc |
| 1.46% | `python` | `clear_slots` | unknown |
| 1.46% | `python` | `PyFloat_AsDouble` | float |
| 1.15% | `python` | `subtype_dealloc` | memory |
| 1.11% | `python` | `_PyObject_MakeTpCall` | dynamic |
| 1.10% | `python` | `PyFloat_FromDouble` | float |
| 1.10% | `python` | `float_dealloc` | memory |
| 1.04% | `python` | `gc_collect_region.isra.0` | gc |
| 1.02% | `python` | `_PyObject_Free` | memory |
| 1.00% | `python` | `type_new` | memory |
| 0.98% | `python` | `PyLong_FromLong` | int |
| 0.96% | `python` | `tuple_dealloc` | memory |
| 0.79% | `python` | `long_dealloc` | memory |
| 0.71% | `python` | `PyLong_AsDouble` | int |
| 0.69% | `python` | `float_mul` | float |
| 0.65% | `python` | `PyObject_GC_Del` | gc |
| 0.58% | `python` | `list_dealloc` | memory |
| 0.58% | `python` | `intern_common.part.0` | str |
| 0.57% | `python` | `_PyCode_New` | interpreter |
| 0.53% | `python` | `binary_op1` | unknown |
| 0.48% | `python` | `binary_iop1` | unknown |
| 0.46% | `python` | `PyNumber_Multiply` | dynamic |
| 0.45% | `[kernel.kallsyms]` | `native_irq_return_iret` | kernel |
| 0.44% | `python` | `PyNumber_TrueDivide` | dynamic |
| 0.42% | `python` | `list_subscript` | list |
| 0.42% | `[kernel.kallsyms]` | `clear_page_erms` | kernel |
| 0.38% | `python` | `dict_traverse` | gc |
| 0.38% | `python` | `r_object` | import |
| 0.32% | `python` | `binary_iop` | unknown |
| 0.31% | `python` | `list_traverse` | gc |
| 0.30% | `[kernel.kallsyms]` | `sync_regs` | kernel |
| 0.30% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.30% | `python` | `type_call` | dynamic |
| 0.29% | `python` | `PyUnicode_FromKindAndData` | str |
| 0.29% | `[kernel.kallsyms]` | `free_pcppages_bulk` | kernel |
| 0.28% | `math.cpython-314-x86_64-linux-gnu.so` | `math_cos` | library |
| 0.27% | `libc-2.31.so` | `__memcpy_avx_unaligned_erms` | libc |
| 0.27% | `math.cpython-314-x86_64-linux-gnu.so` | `math_sin` | library |

## gc_collect

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 19.89% | `python` | `gc_collect_region.isra.0` | gc |
| 15.59% | `python` | `deduce_unreachable` | gc |
| 14.94% | `python` | `visit_reachable` | gc |
| 14.86% | `python` | `visit_decref` | gc |
| 5.21% | `python` | `_PyGC_Collect` | gc |
| 4.17% | `python` | `dict_traverse` | gc |
| 3.29% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 2.60% | `python` | `subtype_traverse` | gc |
| 2.11% | `python` | `func_traverse` | gc |
| 1.97% | `[JIT]` | `jit` | jit |
| 1.22% | `python` | `set_traverse` | gc |
| 1.08% | `python` | `tuple_traverse` | gc |
| 0.76% | `python` | `type_traverse` | gc |
| 0.73% | `python` | `list_traverse` | gc |
| 0.71% | `python` | `PyType_GenericAlloc` | memory |
| 0.59% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.51% | `python` | `type_new` | memory |
| 0.43% | `python` | `meth_traverse` | gc |
| 0.38% | `python` | `subtype_dealloc` | memory |
| 0.33% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.30% | `python` | `PyObject_GC_Del` | gc |
| 0.30% | `python` | `intern_common.part.0` | str |
| 0.27% | `python` | `PyObject_ClearManagedDict` | dynamic |

## gc_traversal

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 25.85% | `python` | `visit_reachable` | gc |
| 22.38% | `python` | `visit_decref` | gc |
| 13.46% | `python` | `list_traverse` | gc |
| 10.79% | `python` | `gc_collect_region.isra.0` | gc |
| 8.29% | `python` | `deduce_unreachable` | gc |
| 2.33% | `python` | `dict_traverse` | gc |
| 1.96% | `[JIT]` | `jit` | jit |
| 1.25% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 1.20% | `python` | `func_traverse` | gc |
| 0.93% | `python` | `subtype_traverse` | gc |
| 0.74% | `python` | `set_traverse` | gc |
| 0.62% | `python` | `tuple_traverse` | gc |
| 0.54% | `python` | `type_new` | memory |
| 0.53% | `python` | `PyLong_FromLong` | int |
| 0.48% | `python` | `type_traverse` | gc |
| 0.35% | `python` | `long_dealloc` | memory |
| 0.31% | `python` | `intern_common.part.0` | str |
| 0.30% | `python` | `list_dealloc` | memory |
| 0.29% | `python` | `_PyCode_New` | interpreter |
| 0.25% | `python` | `meth_traverse` | gc |

## generators

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 36.20% | `[JIT]` | `jit` | jit |
| 22.12% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 2.77% | `python` | `gen_dealloc` | memory |
| 2.05% | `python` | `long_add` | int |
| 1.84% | `python` | `_Py_MakeCoro` | unknown |
| 1.56% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.52% | `python` | `long_dealloc` | memory |
| 1.41% | `python` | `_PyFunction_Vectorcall` | calls |
| 1.24% | `python` | `range_subscript` | miscobj |
| 1.18% | `python` | `deduce_unreachable` | gc |
| 1.08% | `python` | `visit_decref` | gc |
| 0.97% | `python` | `lookup_maybe_method` | unknown |
| 0.96% | `python` | `visit_reachable` | gc |
| 0.95% | `python` | `subtype_dealloc` | memory |
| 0.90% | `python` | `subtype_traverse` | gc |
| 0.87% | `python` | `PyType_GenericAlloc` | memory |
| 0.81% | `python` | `make_range_object` | unknown |
| 0.76% | `python` | `_PyObject_New` | memory |
| 0.71% | `python` | `type_new` | memory |
| 0.69% | `python` | `gc_collect_region.isra.0` | gc |
| 0.61% | `python` | `visit_add_to_container` | gc |
| 0.60% | `python` | `range_dealloc` | memory |
| 0.55% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 0.51% | `python` | `long_richcompare` | int |
| 0.48% | `python` | `PyNumber_Add` | dynamic |
| 0.47% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.46% | `python` | `long_mul_method` | int |
| 0.42% | `python` | `_PySlice_GetLongIndices` | miscobj |
| 0.42% | `python` | `PyObject_CallOneArg` | dynamic |
| 0.41% | `python` | `intern_common.part.0` | str |
| 0.41% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.41% | `python` | `slot_tp_iter` | unknown |
| 0.35% | `python` | `_PyCode_New` | interpreter |
| 0.33% | `python` | `long_div` | int |
| 0.33% | `python` | `PyObject_RichCompareBool` | dynamic |
| 0.33% | `python` | `PyObject_GetItem` | dynamic |
| 0.32% | `python` | `PyLong_AsLongAndOverflow` | int |
| 0.28% | `python` | `r_object` | import |
| 0.27% | `python` | `PyObject_GC_Del` | gc |
| 0.27% | `python` | `slice_dealloc` | memory |

## genshi

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 33.68% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 17.12% | `[JIT]` | `jit` | jit |
| 2.01% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.46% | `python` | `tuple_dealloc` | memory |
| 1.45% | `python` | `insertdict` | dict |
| 1.28% | `python` | `dictresize` | dict |
| 1.14% | `python` | `_PyObject_GC_New` | gc |
| 1.12% | `python` | `dict_dealloc` | memory |
| 1.03% | `python` | `insert_to_emptydict` | dict |
| 1.01% | `python` | `_PyTuple_FromStackRefSteal` | tuple |
| 0.90% | `python` | `PyDict_GetItemRef` | dict |
| 0.89% | `python` | `type_new` | memory |
| 0.84% | `python` | `method_dealloc` | memory |
| 0.80% | `python` | `long_to_decimal_string_internal` | int |
| 0.80% | `python` | `_Py_type_getattro` | lookup |
| 0.78% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.77% | `python` | `cm_descr_get` | unknown |
| 0.69% | `python` | `dict_get` | dict |
| 0.65% | `python` | `PyObject_IsTrue` | dynamic |
| 0.61% | `python` | `PyDict_Contains` | dict |
| 0.61% | `python` | `PyDict_SetItem` | dict |
| 0.57% | `python` | `listiter_dealloc` | memory |
| 0.57% | `python` | `deduce_unreachable` | gc |
| 0.56% | `python` | `object_isinstance` | dynamic |
| 0.53% | `python` | `_PyEval_LoadName` | interpreter |
| 0.52% | `python` | `func_dealloc` | memory |
| 0.51% | `python` | `intern_common.part.0` | str |
| 0.50% | `python` | `_PyDict_LoadBuiltinsFromGlobals` | dict |
| 0.50% | `python` | `PyUnicode_New` | memory |
| 0.49% | `python` | `visit_decref` | gc |
| 0.49% | `python` | `PyObject_GetAttr` | dynamic |
| 0.49% | `python` | `_PyUnicode_JoinArray` | str |
| 0.49% | `python` | `gc_collect_region.isra.0` | gc |
| 0.47% | `python` | `PyObject_GC_Del` | gc |
| 0.47% | `python` | `_PyCode_New` | interpreter |
| 0.44% | `python` | `dictiter_iternextvalue` | dict |
| 0.43% | `python` | `PyMem_Free` | memory |
| 0.43% | `python` | `PyObject_Str` | dynamic |
| 0.43% | `python` | `unicode_dealloc` | memory |
| 0.41% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.41% | `libc-2.31.so` | `__memcpy_avx_unaligned_erms` | libc |
| 0.40% | `python` | `list_dealloc` | memory |
| 0.35% | `python` | `list_iter` | list |
| 0.34% | `python` | `r_object` | import |
| 0.34% | `python` | `visit_reachable` | gc |
| 0.33% | `libc-2.31.so` | `_int_malloc` | libc |
| 0.32% | `python` | `deque_iter` | miscobj |
| 0.29% | `python` | `PyType_GenericAlloc` | memory |
| 0.28% | `python` | `PyObject_Vectorcall` | dynamic |
| 0.27% | `python` | `tuple_hash` | tuple |
| 0.27% | `python` | `list_vectorcall` | list |
| 0.26% | `python` | `gen_iternext` | miscobj |
| 0.25% | `python` | `PyObject_IsInstance` | dynamic |
| 0.25% | `python` | `PyType_GetModuleByDef` | dynamic |

## go

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 35.29% | `[JIT]` | `jit` | jit |
| 30.35% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 4.28% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.45% | `python` | `long_bitwise` | int |
| 1.25% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 1.19% | `python` | `long_dealloc` | memory |
| 1.09% | `python` | `type_new` | memory |
| 0.86% | `python` | `PyDict_SetItem` | dict |
| 0.81% | `python` | `listiter_dealloc` | memory |
| 0.70% | `python` | `_PyLong_Add` | int |
| 0.65% | `python` | `list_iter` | list |
| 0.60% | `python` | `visit_decref` | gc |
| 0.59% | `python` | `intern_common.part.0` | str |
| 0.57% | `python` | `_PyCode_New` | interpreter |
| 0.56% | `python` | `deduce_unreachable` | gc |
| 0.51% | `python` | `gc_collect_region.isra.0` | gc |
| 0.43% | `python` | `r_object` | import |
| 0.41% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.40% | `python` | `long_add` | int |
| 0.33% | `python` | `visit_reachable` | gc |
| 0.32% | `_random.cpython-314-x86_64-linux-gnu.so` | `_random_Random_random` | library |
| 0.30% | `python` | `PyUnicode_FromKindAndData` | str |
| 0.30% | `python` | `long_sub` | int |
| 0.28% | `libc-2.31.so` | `__memcpy_avx_unaligned_erms` | libc |
| 0.26% | `python` | `binary_op1` | unknown |
| 0.26% | `python` | `_PySet_Contains` | miscobj |

## hexiom

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 39.78% | `[JIT]` | `jit` | jit |
| 16.21% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 4.08% | `python` | `list_contains` | list |
| 3.54% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 2.06% | `python` | `long_richcompare` | int |
| 1.95% | `python` | `builtin_sum` | unknown |
| 1.23% | `python` | `type_new` | memory |
| 0.83% | `python` | `PyLong_FromLong` | int |
| 0.79% | `python` | `gen_iternext` | miscobj |
| 0.76% | `python` | `list_dealloc` | memory |
| 0.71% | `python` | `PyFunction_NewWithQualName` | memory |
| 0.67% | `python` | `_PyCode_New` | interpreter |
| 0.67% | `python` | `listiter_dealloc` | memory |
| 0.66% | `python` | `intern_common.part.0` | str |
| 0.64% | `python` | `deduce_unreachable` | gc |
| 0.60% | `python` | `visit_decref` | gc |
| 0.59% | `python` | `PyLong_FromSsize_t` | int |
| 0.57% | `python` | `gc_collect_region.isra.0` | gc |
| 0.57% | `python` | `PySequence_Contains` | dynamic |
| 0.54% | `python` | `PyObject_Size` | dynamic |
| 0.51% | `python` | `list_iter` | list |
| 0.47% | `python` | `r_object` | import |
| 0.43% | `python` | `visit_reachable` | gc |
| 0.42% | `python` | `tuple_dealloc` | memory |
| 0.35% | `python` | `gen_dealloc` | memory |
| 0.34% | `libc-2.31.so` | `__memcpy_avx_unaligned_erms` | libc |
| 0.34% | `python` | `func_dealloc` | memory |
| 0.33% | `python` | `range_iter` | miscobj |
| 0.32% | `python` | `PyUnicode_FromKindAndData` | str |
| 0.31% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.31% | `python` | `_Py_MakeCoro` | unknown |
| 0.30% | `python` | `range_vectorcall` | miscobj |
| 0.30% | `python` | `PyObject_Free` | dynamic |
| 0.28% | `python` | `siphash13` | str |
| 0.28% | `python` | `PyList_New` | memory |
| 0.27% | `python` | `_Py_Dealloc` | memory |
| 0.26% | `python` | `_PyTuple_FromStackRefSteal` | tuple |
| 0.25% | `python` | `range_dealloc` | memory |

## html5lib

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 32.57% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 8.97% | `python` | `sre_ucs2_charset.isra.0` | library |
| 7.55% | `[JIT]` | `jit` | jit |
| 2.35% | `python` | `PyDict_GetItemRef` | dict |
| 2.10% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.86% | `python` | `deduce_unreachable` | gc |
| 1.61% | `python` | `gc_collect_region.isra.0` | gc |
| 1.38% | `python` | `visit_decref` | gc |
| 1.19% | `python` | `PyObject_GetAttr` | dynamic |
| 1.19% | `python` | `type_new` | memory |
| 0.85% | `python` | `sre_ucs1_count` | library |
| 0.73% | `python` | `insertdict` | dict |
| 0.70% | `python` | `_sre_SRE_Pattern_match` | library |
| 0.68% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.66% | `python` | `unicode_dealloc` | memory |
| 0.65% | `python` | `dict_dealloc` | memory |
| 0.65% | `python` | `visit_reachable` | gc |
| 0.63% | `python` | `intern_common.part.0` | str |
| 0.59% | `python` | `visit_add_to_container` | gc |
| 0.59% | `python` | `list_dealloc` | memory |
| 0.56% | `python` | `_PyCode_New` | interpreter |
| 0.54% | `python` | `list_subscript` | list |
| 0.53% | `python` | `PyUnicode_Concat` | str |
| 0.53% | `python` | `set_contains_lock_held` | miscobj |
| 0.52% | `python` | `long_dealloc` | memory |
| 0.52% | `python` | `list_contains` | list |
| 0.47% | `python` | `tuple_dealloc` | memory |
| 0.47% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.46% | `libc-2.31.so` | `__memcpy_avx_unaligned_erms` | libc |
| 0.44% | `python` | `PyObject_IsTrue` | dynamic |
| 0.43% | `python` | `siphash13` | str |
| 0.40% | `python` | `r_object` | import |
| 0.37% | `libc-2.31.so` | `__memcmp_avx2_movbe` | libc |
| 0.36% | `python` | `method_dealloc` | memory |
| 0.34% | `python` | `func_descr_get` | unknown |
| 0.34% | `python` | `PyUnicode_FromKindAndData` | str |
| 0.32% | `python` | `tuple_richcompare` | tuple |
| 0.32% | `python` | `_PyLong_Add` | int |
| 0.30% | `python` | `frozenset_vectorcall` | unknown |
| 0.30% | `libc-2.31.so` | `_int_malloc` | libc |
| 0.30% | `python` | `slot_mp_subscript` | unknown |
| 0.28% | `python` | `sre_ucs1_match` | library |
| 0.28% | `python` | `PyObject_SetAttr` | dynamic |
| 0.28% | `python` | `insert_to_emptydict` | dict |
| 0.27% | `python` | `object_richcompare` | dynamic |
| 0.27% | `python` | `_PyUnicode_TranslateCharmap` | str |
| 0.27% | `python` | `PyList_New` | memory |
| 0.26% | `python` | `PyObject_GC_Del` | gc |
| 0.26% | `python` | `subtype_traverse` | gc |
| 0.26% | `python` | `_PyUnicode_JoinArray` | str |
| 0.25% | `python` | `_Py_dict_lookup` | lookup |

## json

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 18.09% | `_json.cpython-314-x86_64-linux-gnu.so` | `_parse_object_unicode` | library |
| 7.22% | `python` | `PyUnicode_Substring` | str |
| 5.41% | `python` | `dict_setdefault_ref_lock_held` | dict |
| 5.28% | `python` | `siphash13` | str |
| 5.08% | `python` | `PyDict_SetItem` | dict |
| 4.91% | `python` | `unicode_dealloc` | memory |
| 3.92% | `[JIT]` | `jit` | jit |
| 3.80% | `python` | `dictresize` | dict |
| 3.80% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 3.12% | `python` | `PyLong_FromString` | int |
| 2.65% | `python` | `dict_dealloc` | memory |
| 2.04% | `python` | `_sre_SRE_Pattern_match` | library |
| 1.37% | `_json.cpython-314-x86_64-linux-gnu.so` | `_match_number_unicode.isra.0` | library |
| 1.27% | `python` | `PyBytes_FromStringAndSize` | str |
| 1.26% | `libc-2.31.so` | `__memcpy_avx_unaligned_erms` | libc |
| 1.18% | `libc-2.31.so` | `_int_malloc` | libc |
| 0.94% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.93% | `python` | `PyDict_GetItemRef` | dict |
| 0.86% | `python` | `type_new` | memory |
| 0.71% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.70% | `python` | `object_dealloc` | memory |
| 0.66% | `python` | `unicode_hash` | str |
| 0.66% | `python` | `tuple_dealloc` | memory |
| 0.62% | `python` | `insert_to_emptydict` | dict |
| 0.61% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.61% | `libc-2.31.so` | `_int_free` | libc |
| 0.57% | `python` | `sre_ucs1_match` | library |
| 0.57% | `libc-2.31.so` | `__libc_malloc` | libc |
| 0.54% | `python` | `long_dealloc` | memory |
| 0.54% | `python` | `_PyUnicodeWriter_PrepareInternal` | str |
| 0.51% | `python` | `intern_common.part.0` | str |
| 0.49% | `python` | `resize_compact` | str |
| 0.48% | `python` | `match_dealloc` | memory |
| 0.46% | `python` | `deduce_unreachable` | gc |
| 0.44% | `python` | `gc_collect_region.isra.0` | gc |
| 0.41% | `python` | `_PyCode_New` | interpreter |
| 0.41% | `python` | `visit_decref` | gc |
| 0.40% | `python` | `_PyObject_Free` | memory |
| 0.40% | `python` | `vgetargskeywords.constprop.0` | calls |
| 0.39% | `python` | `PyMem_Free` | memory |
| 0.33% | `python` | `r_object` | import |
| 0.33% | `python` | `_PyLong_New` | memory |
| 0.31% | `python` | `_PyUnicodeWriter_Init` | str |
| 0.27% | `python` | `_PyUnicodeWriter_WriteSubstring` | str |
| 0.27% | `python` | `visit_reachable` | gc |
| 0.27% | `python` | `PyObject_Hash` | dynamic |
| 0.26% | `python` | `PyUnicode_FromKindAndData` | str |

## json_dumps

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 9.17% | `_json.cpython-314-x86_64-linux-gnu.so` | `encoder_listencode_dict` | library |
| 6.55% | `python` | `PyUnicode_New` | memory |
| 6.39% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 5.22% | `[JIT]` | `jit` | jit |
| 5.19% | `python` | `_PyUnicodeWriter_WriteStr` | str |
| 4.92% | `python` | `PyUnicodeWriter_WriteStr` | str |
| 4.68% | `python` | `unicode_dealloc` | memory |
| 3.30% | `python` | `_PyUnicodeWriter_PrepareInternal` | str |
| 3.00% | `_json.cpython-314-x86_64-linux-gnu.so` | `py_encode_basestring_ascii` | library |
| 2.88% | `python` | `resize_compact` | str |
| 2.36% | `libc-2.31.so` | `__memcpy_avx_unaligned_erms` | libc |
| 2.36% | `python` | `PyDict_GetItemRef` | dict |
| 2.28% | `python` | `vgetargskeywords.constprop.0` | calls |
| 1.47% | `python` | `long_to_decimal_string_internal` | int |
| 1.43% | `python` | `PyDict_Next` | dict |
| 1.37% | `python` | `tuple_dealloc` | memory |
| 1.32% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 1.25% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.13% | `python` | `PyDict_SetItem` | dict |
| 1.04% | `python` | `PyObject_GetAttr` | dynamic |
| 1.03% | `python` | `object_isinstance` | dynamic |
| 1.01% | `python` | `PyFunction_NewWithQualName` | memory |
| 0.84% | `python` | `_PyLong_New` | memory |
| 0.81% | `python` | `type_new` | memory |
| 0.78% | `python` | `long_hash` | int |
| 0.78% | `python` | `_PyObject_MakeTpCall` | dynamic |
| 0.75% | `python` | `func_dealloc` | memory |
| 0.70% | `python` | `long_dealloc` | memory |
| 0.70% | `python` | `PyDict_DelItem` | dict |
| 0.60% | `python` | `PyDict_Contains` | dict |
| 0.56% | `python` | `_Py_dict_lookup` | lookup |
| 0.53% | `python` | `unicode_decode_utf8_writer` | str |
| 0.51% | `python` | `PyMem_Free` | memory |
| 0.50% | `python` | `PyType_GenericAlloc` | memory |
| 0.48% | `python` | `intern_common.part.0` | str |
| 0.45% | `python` | `deduce_unreachable` | gc |
| 0.44% | `python` | `method_dealloc` | memory |
| 0.43% | `python` | `dict_dealloc` | memory |
| 0.43% | `python` | `memcpy@plt` | memory |
| 0.42% | `python` | `insert_to_emptydict` | dict |
| 0.42% | `python` | `PyUnicodeWriter_Create` | str |
| 0.41% | `python` | `_PyCode_New` | interpreter |
| 0.40% | `python` | `PyTuple_Pack` | tuple |
| 0.39% | `python` | `func_descr_get` | unknown |
| 0.38% | `python` | `PyLong_FromLong` | int |
| 0.38% | `python` | `gc_collect_region.isra.0` | gc |
| 0.37% | `python` | `visit_decref` | gc |
| 0.35% | `python` | `PyMem_Malloc` | memory |
| 0.35% | `python` | `pthread_self@plt` | unknown |
| 0.35% | `python` | `_PyTuple_FromStackRefSteal` | tuple |
| 0.35% | `libc-2.31.so` | `pthread_self` | libc |
| 0.33% | `python` | `_Py_Dealloc` | memory |
| 0.32% | `python` | `r_object` | import |
| 0.30% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.30% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.29% | `_json.cpython-314-x86_64-linux-gnu.so` | `0x0000000000002664` | library |
| 0.29% | `python` | `visit_reachable` | gc |
| 0.28% | `_json.cpython-314-x86_64-linux-gnu.so` | `encoder_listencode_obj` | library |
| 0.27% | `python` | `PyType_IsSubtype` | dynamic |
| 0.27% | `libc-2.31.so` | `__strchr_avx2` | libc |
| 0.26% | `python` | `_PyUnicodeWriter_Finish` | str |

## json_loads

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 19.39% | `_json.cpython-314-x86_64-linux-gnu.so` | `_parse_object_unicode` | library |
| 10.84% | `python` | `PyUnicode_Substring` | str |
| 6.54% | `python` | `siphash13` | str |
| 6.15% | `python` | `dict_setdefault_ref_lock_held` | dict |
| 5.21% | `python` | `PyDict_SetItem` | dict |
| 4.94% | `python` | `unicode_dealloc` | memory |
| 4.04% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 3.26% | `python` | `PyLong_FromString` | int |
| 2.29% | `python` | `dictresize` | dict |
| 2.00% | `[JIT]` | `jit` | jit |
| 1.71% | `python` | `dict_dealloc` | memory |
| 1.29% | `python` | `PyBytes_FromStringAndSize` | str |
| 1.21% | `_json.cpython-314-x86_64-linux-gnu.so` | `_match_number_unicode.isra.0` | library |
| 1.12% | `python` | `type_new` | memory |
| 1.11% | `python` | `_sre_SRE_Pattern_match` | library |
| 1.02% | `libc-2.31.so` | `__memcpy_avx_unaligned_erms` | libc |
| 0.90% | `_json.cpython-314-x86_64-linux-gnu.so` | `_parse_array_unicode` | library |
| 0.84% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.81% | `python` | `object_dealloc` | memory |
| 0.78% | `python` | `unicode_hash` | str |
| 0.65% | `python` | `deduce_unreachable` | gc |
| 0.64% | `python` | `intern_common.part.0` | str |
| 0.59% | `python` | `long_dealloc` | memory |
| 0.58% | `libc-2.31.so` | `__memcmp_avx2_movbe` | libc |
| 0.55% | `python` | `PyDict_GetItemRef` | dict |
| 0.53% | `python` | `gc_collect_region.isra.0` | gc |
| 0.52% | `python` | `_PyCode_New` | interpreter |
| 0.48% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.47% | `python` | `_PyUnicodeWriter_Init` | str |
| 0.47% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.47% | `python` | `visit_decref` | gc |
| 0.46% | `python` | `tuple_dealloc` | memory |
| 0.40% | `libc-2.31.so` | `__libc_malloc` | libc |
| 0.39% | `libc-2.31.so` | `_int_malloc` | libc |
| 0.38% | `python` | `r_object` | import |
| 0.37% | `python` | `insert_to_emptydict` | dict |
| 0.37% | `python` | `list_dealloc` | memory |
| 0.36% | `python` | `visit_reachable` | gc |
| 0.36% | `python` | `PyObject_Hash` | dynamic |
| 0.34% | `python` | `PyList_Append` | list |
| 0.33% | `libc-2.31.so` | `_int_free` | libc |
| 0.31% | `python` | `PyUnicode_FromKindAndData` | str |
| 0.30% | `python` | `sre_ucs1_match` | library |
| 0.26% | `python` | `PyMem_Realloc` | memory |

## logging

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 32.00% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 15.16% | `[JIT]` | `jit` | jit |
| 6.16% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 2.80% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 2.24% | `python` | `PyDict_GetItemRef` | dict |
| 1.74% | `python` | `PyCode_Addr2Line` | exceptions |
| 1.66% | `python` | `dict_dealloc` | memory |
| 1.54% | `python` | `PyObject_GetAttr` | dynamic |
| 0.96% | `python` | `PyDict_New` | memory |
| 0.94% | `python` | `type_new` | memory |
| 0.76% | `python` | `tuple_dealloc` | memory |
| 0.74% | `python` | `unicode_dealloc` | memory |
| 0.69% | `python` | `PyLong_FromLong` | int |
| 0.69% | `python` | `long_dealloc` | memory |
| 0.63% | `python` | `PyUnicode_Substring` | str |
| 0.62% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.54% | `python` | `intern_common.part.0` | str |
| 0.52% | `python` | `deduce_unreachable` | gc |
| 0.50% | `python` | `PyUnicode_Format` | str |
| 0.46% | `python` | `_PyCode_New` | interpreter |
| 0.43% | `python` | `visit_decref` | gc |
| 0.42% | `python` | `_PyObject_LookupSpecialMethod` | dynamic |
| 0.39% | `python` | `unicode_splitlines` | str |
| 0.39% | `python` | `siphash13` | str |
| 0.38% | `python` | `dict_get` | dict |
| 0.38% | `python` | `PyObject_GetOptionalAttr` | dynamic |
| 0.38% | `python` | `gc_collect_region.isra.0` | gc |
| 0.37% | `python` | `frame_dealloc` | memory |
| 0.37% | `python` | `slot_tp_init` | unknown |
| 0.34% | `python` | `PyUnicode_Contains` | str |
| 0.34% | `python` | `r_object` | import |
| 0.33% | `python` | `_PyFrame_MakeAndSetFrameObject` | unknown |
| 0.31% | `[kernel.kallsyms]` | `clear_bhb_loop` | kernel |
| 0.31% | `python` | `long_hash` | int |
| 0.30% | `python` | `make_dict_from_instance_attributes` | unknown |
| 0.30% | `python` | `float_div` | float |
| 0.30% | `libc-2.31.so` | `__memcpy_avx_unaligned_erms` | libc |
| 0.29% | `python` | `method_vectorcall` | calls |
| 0.29% | `python` | `PyObject_Vectorcall` | dynamic |
| 0.28% | `python` | `PyObject_Hash` | dynamic |
| 0.28% | `python` | `object_new` | memory |
| 0.28% | `python` | `visit_reachable` | gc |
| 0.28% | `python` | `_PyTuple_FromStackRefSteal` | tuple |
| 0.28% | `python` | `PyUnicode_FromKindAndData` | str |
| 0.26% | `python` | `method_dealloc` | memory |
| 0.26% | `python` | `getset_get` | dynamic |
| 0.26% | `python` | `long_mod` | int |

## mako

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 30.47% | `[JIT]` | `jit` | jit |
| 8.89% | `python` | `unicode_replace` | str |
| 8.35% | `python` | `long_to_decimal_string_internal` | int |
| 4.62% | `python` | `_PyUnicode_JoinArray` | str |
| 3.07% | `python` | `PyUnicode_New` | memory |
| 2.91% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 2.72% | `python` | `unicode_dealloc` | memory |
| 2.43% | `python` | `dequeiter_next_lock_held.isra.0` | miscobj |
| 2.32% | `libc-2.31.so` | `__memcpy_avx_unaligned_erms` | libc |
| 1.83% | `python` | `PyObject_Str` | dynamic |
| 1.47% | `python` | `deque_append_lock_held` | miscobj |
| 1.43% | `python` | `_list_extend` | list |
| 1.39% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.38% | `python` | `list_dealloc` | memory |
| 1.20% | `python` | `deque_append_impl` | miscobj |
| 1.02% | `python` | `sre_ucs2_charset.isra.0` | library |
| 0.92% | `python` | `deque_clear` | miscobj |
| 0.90% | `python` | `type_new` | memory |
| 0.66% | `python` | `PyLong_FromLong` | int |
| 0.53% | `[kernel.kallsyms]` | `native_irq_return_iret` | kernel |
| 0.52% | `python` | `intern_common.part.0` | str |
| 0.52% | `python` | `visit_decref` | gc |
| 0.51% | `libc-2.31.so` | `_int_malloc` | libc |
| 0.50% | `python` | `deduce_unreachable` | gc |
| 0.46% | `python` | `_PyCode_New` | interpreter |
| 0.45% | `python` | `gc_collect_region.isra.0` | gc |
| 0.42% | `[kernel.kallsyms]` | `clear_page_erms` | kernel |
| 0.38% | `[kernel.kallsyms]` | `sync_regs` | kernel |
| 0.37% | `python` | `visit_reachable` | gc |
| 0.32% | `python` | `r_object` | import |
| 0.30% | `python` | `memcpy@plt` | memory |
| 0.30% | `python` | `deque_append` | miscobj |
| 0.28% | `python` | `dequeiter_next` | miscobj |
| 0.25% | `python` | `PyUnicode_FromKindAndData` | str |

## mdp

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 33.41% | `python` | `tuple_hash` | tuple |
| 12.77% | `python` | `long_hash` | int |
| 10.61% | `[JIT]` | `jit` | jit |
| 9.52% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 5.93% | `python` | `dict_subscript` | dict |
| 3.22% | `python` | `tuple_richcompare` | tuple |
| 1.47% | `python` | `insertdict` | dict |
| 1.34% | `python` | `_PyLong_GCD` | int |
| 1.25% | `python` | `_PySuper_Lookup` | dynamic |
| 1.20% | `python` | `PyDict_GetItemRef` | dict |
| 1.01% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.00% | `python` | `PyFunction_NewWithQualName` | memory |
| 0.98% | `python` | `builtin_sum` | unknown |
| 0.66% | `python` | `_PyFloat_FromDouble_ConsumeInputs` | float |
| 0.60% | `python` | `_PySet_Contains` | miscobj |
| 0.53% | `python` | `listiter_dealloc` | memory |
| 0.53% | `python` | `gen_dealloc` | memory |
| 0.52% | `python` | `_Py_MakeCoro` | unknown |
| 0.50% | `python` | `tuple_dealloc` | memory |
| 0.47% | `python` | `gen_iternext` | miscobj |
| 0.47% | `python` | `PyObject_GetItem` | dynamic |
| 0.44% | `python` | `func_dealloc` | memory |
| 0.41% | `python` | `long_div` | int |
| 0.40% | `python` | `subtype_dealloc` | memory |
| 0.36% | `python` | `tp_new_wrapper` | memory |
| 0.35% | `python` | `long_dealloc` | memory |
| 0.34% | `python` | `PyObject_GetAttr` | dynamic |
| 0.34% | `python` | `list_iter` | list |
| 0.33% | `python` | `vectorcall_maybe.constprop.0` | unknown |
| 0.31% | `python` | `PyObject_RichCompare` | dynamic |
| 0.27% | `python` | `PyObject_Hash` | dynamic |

## meteor_contest

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 20.58% | `[JIT]` | `jit` | jit |
| 9.17% | `python` | `set_issubset_impl` | miscobj |
| 6.49% | `python` | `setiter_iternext` | miscobj |
| 5.64% | `python` | `set_lookkey` | miscobj |
| 5.63% | `python` | `set_difference` | miscobj |
| 4.89% | `python` | `set_dealloc` | memory |
| 3.70% | `python` | `builtin_min` | unknown |
| 2.87% | `python` | `list_dealloc` | memory |
| 2.67% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 2.24% | `python` | `set_add_entry` | miscobj |
| 1.84% | `python` | `list_subscript` | list |
| 1.56% | `python` | `set_table_resize` | miscobj |
| 1.50% | `python` | `long_richcompare` | int |
| 1.27% | `python` | `make_new_set` | memory |
| 1.18% | `python` | `PyObject_RichCompare` | dynamic |
| 1.06% | `python` | `type_new` | memory |
| 1.03% | `python` | `set_iter` | miscobj |
| 0.98% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.97% | `python` | `set_intersection` | miscobj |
| 0.88% | `python` | `listiter_dealloc` | memory |
| 0.78% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.76% | `python` | `setiter_dealloc` | memory |
| 0.70% | `python` | `set_merge_lock_held.part.0` | miscobj |
| 0.67% | `python` | `list_iter` | list |
| 0.64% | `python` | `intern_common.part.0` | str |
| 0.62% | `python` | `PyMem_Malloc` | memory |
| 0.60% | `python` | `deduce_unreachable` | gc |
| 0.56% | `python` | `_PyCode_New` | interpreter |
| 0.55% | `python` | `set_difference_update_internal` | miscobj |
| 0.47% | `python` | `set_richcompare` | miscobj |
| 0.46% | `python` | `visit_decref` | gc |
| 0.46% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.42% | `python` | `gc_collect_region.isra.0` | gc |
| 0.35% | `python` | `r_object` | import |
| 0.35% | `python` | `PyUnicode_FromKindAndData` | str |
| 0.34% | `python` | `PyList_New` | memory |
| 0.33% | `python` | `PyObject_Size` | dynamic |
| 0.30% | `libc-2.31.so` | `__memcpy_avx_unaligned_erms` | libc |
| 0.30% | `python` | `visit_reachable` | gc |
| 0.27% | `python` | `list_ass_slice_lock_held` | list |
| 0.26% | `python` | `PyObject_IsTrue` | dynamic |
| 0.26% | `python` | `tuple_dealloc` | memory |

## nbody

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 48.69% | `[JIT]` | `jit` | jit |
| 20.16% | `python` | `_PyFloat_FromDouble_ConsumeInputs` | float |
| 4.56% | `libm-2.31.so` | `__ieee754_pow_fma` | library |
| 2.75% | `python` | `float_dealloc` | memory |
| 2.48% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 1.86% | `python` | `_Py_Dealloc` | memory |
| 1.35% | `python` | `float_pow` | float |
| 0.96% | `python` | `type_new` | memory |
| 0.55% | `python` | `intern_common.part.0` | str |
| 0.51% | `python` | `listiter_dealloc` | memory |
| 0.51% | `python` | `deduce_unreachable` | gc |
| 0.49% | `libm-2.31.so` | `powf64` | library |
| 0.47% | `python` | `gc_collect_region.isra.0` | gc |
| 0.46% | `python` | `visit_decref` | gc |
| 0.44% | `python` | `_PyCode_New` | interpreter |
| 0.40% | `python` | `list_iter` | list |
| 0.39% | `python` | `_PyNumber_PowerNoMod` | dynamic |
| 0.38% | `python` | `r_object` | import |
| 0.31% | `python` | `PyUnicode_FromKindAndData` | str |
| 0.30% | `python` | `visit_reachable` | gc |
| 0.27% | `python` | `_PyFloat_ExactDealloc` | memory |

## networkx

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 8.63% | `python` | `visit_decref` | gc |
| 8.47% | `python` | `visit_add_to_container` | gc |
| 7.73% | `python` | `dict_traverse` | gc |
| 7.30% | `python` | `PyDict_GetItemRef` | dict |
| 6.98% | `python` | `visit_reachable` | gc |
| 6.77% | `[JIT]` | `jit` | jit |
| 5.79% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 4.77% | `python` | `_PySet_Contains` | miscobj |
| 4.53% | `python` | `dictiter_iternextkey` | dict |
| 4.25% | `python` | `PyDict_Contains` | dict |
| 3.44% | `python` | `deduce_unreachable` | gc |
| 3.43% | `python` | `insertdict` | dict |
| 2.87% | `python` | `gc_collect_region.isra.0` | gc |
| 1.93% | `python` | `dict_dealloc` | memory |
| 1.87% | `python` | `PyObject_GetAttr` | dynamic |
| 1.80% | `python` | `dictresize` | dict |
| 0.72% | `python` | `dict_get` | dict |
| 0.67% | `libz.so.1.2.11` | `inflateBackEnd` | library |
| 0.66% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.59% | `python` | `list_dealloc` | memory |
| 0.58% | `python` | `unicode_eq.lto_priv.1` | str |
| 0.55% | `python` | `unicode_dealloc` | memory |
| 0.49% | `python` | `tuple_dealloc` | memory |
| 0.49% | `python` | `split` | str |
| 0.48% | `python` | `siphash13` | str |
| 0.48% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.44% | `python` | `_PyObject_GetMethod` | dynamic |
| 0.40% | `python` | `_PyGC_Collect` | gc |
| 0.39% | `python` | `method_vectorcall_VARARGS_KEYWORDS` | calls |
| 0.38% | `libc-2.31.so` | `__memcmp_avx2_movbe` | libc |
| 0.33% | `python` | `unicode_decode_utf8` | str |
| 0.31% | `python` | `PyUnicode_New` | memory |
| 0.29% | `python` | `PyObject_VectorcallMethod` | dynamic |
| 0.29% | `python` | `list_iter` | list |
| 0.27% | `python` | `_PyObject_Malloc` | memory |
| 0.26% | `python` | `listiter_dealloc` | memory |
| 0.25% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.25% | `python` | `_PyObject_GenericGetAttrWithDict` | dynamic |

## networkx_connected_components

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 8.72% | `python` | `visit_decref` | gc |
| 8.57% | `python` | `visit_add_to_container` | gc |
| 7.93% | `python` | `dict_traverse` | gc |
| 7.55% | `python` | `PyDict_GetItemRef` | dict |
| 7.03% | `python` | `visit_reachable` | gc |
| 7.02% | `[JIT]` | `jit` | jit |
| 6.22% | `python` | `_PySet_Contains` | miscobj |
| 5.69% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 4.55% | `python` | `dictiter_iternextkey` | dict |
| 4.30% | `python` | `PyDict_Contains` | dict |
| 3.50% | `python` | `deduce_unreachable` | gc |
| 2.92% | `python` | `gc_collect_region.isra.0` | gc |
| 2.22% | `python` | `insertdict` | dict |
| 1.96% | `python` | `PyObject_GetAttr` | dynamic |
| 1.82% | `python` | `dict_dealloc` | memory |
| 0.72% | `python` | `dict_get` | dict |
| 0.71% | `python` | `unicode_eq.lto_priv.1` | str |
| 0.68% | `python` | `dictresize` | dict |
| 0.68% | `libz.so.1.2.11` | `inflateBackEnd` | library |
| 0.67% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.59% | `python` | `list_dealloc` | memory |
| 0.55% | `python` | `unicode_dealloc` | memory |
| 0.52% | `python` | `siphash13` | str |
| 0.46% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.46% | `python` | `split` | str |
| 0.45% | `python` | `_PyObject_GetMethod` | dynamic |
| 0.43% | `python` | `tuple_dealloc` | memory |
| 0.42% | `libc-2.31.so` | `__memcmp_avx2_movbe` | libc |
| 0.42% | `python` | `set_dealloc` | memory |
| 0.40% | `python` | `_PyGC_Collect` | gc |
| 0.38% | `python` | `method_vectorcall_VARARGS_KEYWORDS` | calls |
| 0.35% | `python` | `unicode_decode_utf8` | str |
| 0.31% | `python` | `PyObject_VectorcallMethod` | dynamic |
| 0.29% | `python` | `PyUnicode_New` | memory |
| 0.29% | `python` | `list_iter` | list |
| 0.28% | `python` | `_PyObject_Malloc` | memory |
| 0.27% | `python` | `set_merge_lock_held.part.0` | miscobj |
| 0.27% | `python` | `listiter_dealloc` | memory |

## networkx_k_core

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 15.17% | `python` | `PyDict_GetItemRef` | dict |
| 10.28% | `python` | `visit_add_to_container` | gc |
| 9.98% | `python` | `visit_decref` | gc |
| 8.81% | `python` | `visit_reachable` | gc |
| 8.35% | `[JIT]` | `jit` | jit |
| 7.65% | `python` | `dict_traverse` | gc |
| 4.39% | `python` | `insertdict` | dict |
| 3.80% | `python` | `PyDict_Contains` | dict |
| 3.59% | `python` | `list_remove` | list |
| 3.21% | `python` | `deduce_unreachable` | gc |
| 2.93% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 2.51% | `python` | `gc_collect_region.isra.0` | gc |
| 2.26% | `python` | `dictiter_iternextkey` | dict |
| 1.01% | `python` | `dict_dealloc` | memory |
| 0.96% | `python` | `list_dealloc` | memory |
| 0.94% | `python` | `dictresize` | dict |
| 0.87% | `python` | `PyObject_GetAttr` | dynamic |
| 0.69% | `python` | `PyUnicode_RichCompare` | str |
| 0.65% | `python` | `dict_get` | dict |
| 0.52% | `python` | `list_traverse` | gc |
| 0.46% | `python` | `long_dealloc` | memory |
| 0.45% | `python` | `listiter_next` | list |
| 0.43% | `libc-2.31.so` | `__memcmp_avx2_movbe` | libc |
| 0.43% | `python` | `_PyGC_Collect` | gc |
| 0.41% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.38% | `python` | `PyObject_RichCompareBool` | dynamic |
| 0.38% | `libc-2.31.so` | `__memcpy_avx_unaligned_erms` | libc |
| 0.29% | `libz.so.1.2.11` | `inflateBackEnd` | library |

## nqueens

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 25.20% | `[JIT]` | `jit` | jit |
| 18.49% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 4.88% | `python` | `set_vectorcall` | miscobj |
| 2.94% | `python` | `list_dealloc` | memory |
| 2.63% | `python` | `PyFunction_NewWithQualName` | memory |
| 2.04% | `python` | `set_dealloc` | memory |
| 1.97% | `python` | `gen_iternext` | miscobj |
| 1.80% | `python` | `list_subscript` | list |
| 1.33% | `python` | `_PyLong_Add` | int |
| 1.29% | `python` | `func_dealloc` | memory |
| 1.23% | `python` | `tuple_dealloc` | memory |
| 1.23% | `python` | `_Py_MakeCoro` | unknown |
| 1.21% | `python` | `gen_dealloc` | memory |
| 1.18% | `python` | `PyMem_Malloc` | memory |
| 1.15% | `python` | `_PyBuildSlice_ConsumeRefs` | miscobj |
| 1.08% | `python` | `list_ass_slice_lock_held` | list |
| 0.90% | `python` | `PyList_New` | memory |
| 0.88% | `python` | `slice_dealloc` | memory |
| 0.82% | `python` | `type_new` | memory |
| 0.78% | `python` | `PyLong_FromLong` | int |
| 0.69% | `python` | `list_ass_subscript` | list |
| 0.66% | `python` | `PyNumber_AsSsize_t` | dynamic |
| 0.62% | `python` | `PyObject_Free` | dynamic |
| 0.60% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.57% | `python` | `_PyLong_Subtract` | int |
| 0.52% | `python` | `range_iter` | miscobj |
| 0.52% | `python` | `_PyTuple_FromStackRefSteal` | tuple |
| 0.50% | `python` | `PySequence_Tuple` | dynamic |
| 0.49% | `python` | `_PyObject_LookupSpecial` | dynamic |
| 0.49% | `python` | `intern_common.part.0` | str |
| 0.47% | `python` | `PyObject_GetIter` | dynamic |
| 0.46% | `python` | `range_vectorcall` | miscobj |
| 0.45% | `python` | `deduce_unreachable` | gc |
| 0.44% | `python` | `_PyCode_New` | interpreter |
| 0.43% | `python` | `list_new_prealloc` | memory |
| 0.43% | `python` | `visit_decref` | gc |
| 0.42% | `python` | `meth_dealloc` | memory |
| 0.42% | `python` | `list_iter` | list |
| 0.42% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.42% | `python` | `method_get` | dynamic |
| 0.41% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 0.40% | `python` | `PyObject_GetItem` | dynamic |
| 0.38% | `python` | `gc_collect_region.isra.0` | gc |
| 0.38% | `python` | `_PyObject_GC_NewVar` | gc |
| 0.32% | `python` | `listiter_dealloc` | memory |
| 0.32% | `python` | `range_reverse` | miscobj |
| 0.32% | `python` | `_PyObject_Realloc` | memory |
| 0.32% | `python` | `_Py_Dealloc` | memory |
| 0.32% | `python` | `r_object` | import |
| 0.30% | `python` | `long_hash` | int |
| 0.30% | `libc-2.31.so` | `__memcpy_avx_unaligned_erms` | libc |
| 0.28% | `python` | `PySlice_Unpack` | miscobj |
| 0.28% | `python` | `PyUnicode_FromKindAndData` | str |
| 0.27% | `python` | `_PyTuple_Resize` | tuple |

## pathlib

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 9.58% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 3.38% | `[JIT]` | `jit` | jit |
| 2.32% | `python` | `long_dealloc` | memory |
| 2.17% | `python` | `ScandirIterator_iternext` | unknown |
| 1.52% | `[kernel.kallsyms]` | `__d_lookup_rcu` | kernel |
| 1.48% | `libpthread-2.31.so` | `__pthread_mutex_lock` | library |
| 1.39% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.36% | `python` | `PyUnicode_DecodeFSDefault` | str |
| 1.33% | `python` | `unicode_decode_utf8` | str |
| 1.30% | `[kernel.kallsyms]` | `ext4_htree_store_dirent` | kernel |
| 1.30% | `[kernel.kallsyms]` | `memset_erms` | kernel |
| 1.24% | `python` | `_PyLong_New` | memory |
| 1.23% | `libpthread-2.31.so` | `pthread_mutex_unlock` | library |
| 1.20% | `python` | `fill_time` | unknown |
| 1.17% | `python` | `k_mul` | int |
| 1.17% | `[kernel.kallsyms]` | `__ext4fs_dirhash` | kernel |
| 1.11% | `python` | `path_converter` | unknown |
| 1.07% | `python` | `take_gil` | gil |
| 1.03% | `python` | `type_new` | memory |
| 0.84% | `python` | `x_add` | int |
| 0.81% | `python` | `tuple_dealloc` | memory |
| 0.80% | `[kernel.kallsyms]` | `filldir64` | kernel |
| 0.79% | `python` | `unicode_dealloc` | memory |
| 0.77% | `python` | `_sre_SRE_Pattern_match` | library |
| 0.77% | `[kernel.kallsyms]` | `strncpy_from_user` | kernel |
| 0.72% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.69% | `python` | `sre_ucs1_match` | library |
| 0.66% | `python` | `tp_new_wrapper` | memory |
| 0.66% | `python` | `clear_slots` | unknown |
| 0.65% | `python` | `deduce_unreachable` | gc |
| 0.64% | `[kernel.kallsyms]` | `link_path_walk.part.0` | kernel |
| 0.62% | `[kernel.kallsyms]` | `kmem_cache_alloc` | kernel |
| 0.60% | `python` | `slot_tp_init` | unknown |
| 0.60% | `python` | `intern_common.part.0` | str |
| 0.58% | `[kernel.kallsyms]` | `clear_bhb_loop` | kernel |
| 0.58% | `[kernel.kallsyms]` | `copy_user_enhanced_fast_string` | kernel |
| 0.58% | `python` | `visit_decref` | gc |
| 0.58% | `python` | `PyLong_FromLong` | int |
| 0.57% | `python` | `gc_collect_region.isra.0` | gc |
| 0.56% | `python` | `PyDict_GetItemRef` | dict |
| 0.53% | `python` | `object_isinstance` | dynamic |
| 0.53% | `python` | `vectorcall_method` | calls |
| 0.52% | `[kernel.kallsyms]` | `rb_insert_color` | kernel |
| 0.51% | `python` | `_PyCode_New` | interpreter |
| 0.51% | `python` | `_PyObject_GC_NewVar` | gc |
| 0.51% | `python` | `PyObject_GC_Del` | gc |
| 0.51% | `[kernel.kallsyms]` | `str2hashbuf_signed` | kernel |
| 0.50% | `python` | `structseq_dealloc` | memory |
| 0.49% | `libc-2.31.so` | `_int_malloc` | libc |
| 0.49% | `[kernel.kallsyms]` | `__slab_free` | kernel |
| 0.49% | `[kernel.kallsyms]` | `syscall_return_via_sysret` | kernel |
| 0.48% | `python` | `get_type_attr_as_size` | unknown |
| 0.46% | `[kernel.kallsyms]` | `rb_next` | kernel |
| 0.45% | `[kernel.kallsyms]` | `security_inode_getattr` | kernel |
| 0.45% | `python` | `method_vectorcall` | calls |
| 0.44% | `[kernel.kallsyms]` | `__ext4_check_dir_entry` | kernel |
| 0.44% | `python` | `_Py_type_getattro` | lookup |
| 0.43% | `[kernel.kallsyms]` | `ext4_getattr` | kernel |
| 0.42% | `[kernel.kallsyms]` | `do_syscall_64` | kernel |
| 0.42% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.42% | `python` | `subtype_dealloc` | memory |
| 0.42% | `python` | `visit_reachable` | gc |
| 0.41% | `[kernel.kallsyms]` | `kfree` | kernel |
| 0.41% | `python` | `_Py_dict_lookup` | lookup |
| 0.41% | `python` | `r_object` | import |
| 0.41% | `python` | `_PyObject_LookupSpecial` | dynamic |
| 0.41% | `libc-2.31.so` | `__xstat64` | libc |
| 0.40% | `python` | `list_dealloc` | memory |
| 0.40% | `python` | `_PyTuple_FromStackRefSteal` | tuple |
| 0.39% | `[kernel.kallsyms]` | `__virt_addr_valid` | kernel |
| 0.39% | `python` | `_PyArg_UnpackKeywords` | calls |
| 0.38% | `python` | `object_dealloc` | memory |
| 0.38% | `python` | `_PyObject_New` | memory |
| 0.37% | `[kernel.kallsyms]` | `kmem_cache_free` | kernel |
| 0.37% | `libc-2.31.so` | `__memcpy_avx_unaligned_erms` | libc |
| 0.37% | `libc-2.31.so` | `__strcpy_avx2` | libc |
| 0.36% | `python` | `func_descr_get` | unknown |
| 0.36% | `[kernel.kallsyms]` | `entry_SYSCALL_64` | kernel |
| 0.36% | `[kernel.kallsyms]` | `__kmalloc` | kernel |
| 0.34% | `[kernel.kallsyms]` | `generic_permission` | kernel |
| 0.33% | `[kernel.kallsyms]` | `lookup_fast` | kernel |
| 0.33% | `python` | `slot_tp_new` | memory |
| 0.33% | `[kernel.kallsyms]` | `in_group_p` | kernel |
| 0.32% | `libc-2.31.so` | `_int_free` | libc |
| 0.32% | `python` | `PyMem_Malloc` | memory |
| 0.31% | `python` | `PyEval_SaveThread` | interpreter |
| 0.31% | `python` | `tuple_iter` | tuple |
| 0.30% | `[kernel.kallsyms]` | `__check_heap_object` | kernel |
| 0.30% | `python` | `PyUnicode_FromKindAndData` | str |
| 0.29% | `[kernel.kallsyms]` | `call_filldir` | kernel |
| 0.29% | `python` | `PyObject_Free` | dynamic |
| 0.29% | `python` | `map_next` | unknown |
| 0.28% | `[kernel.kallsyms]` | `memcpy_erms` | kernel |
| 0.28% | `python` | `_PyObject_Malloc` | memory |
| 0.28% | `python` | `method_dealloc` | memory |
| 0.28% | `python` | `PyUnicode_DecodeFSDefaultAndSize` | str |
| 0.28% | `libc-2.31.so` | `__libc_malloc` | libc |
| 0.27% | `[kernel.kallsyms]` | `walk_component` | kernel |
| 0.26% | `python` | `long_mul_method` | int |
| 0.25% | `python` | `tupleiter_dealloc` | memory |
| 0.25% | `python` | `listiter_next` | list |

## pickle_pure_python

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 26.88% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 14.37% | `[JIT]` | `jit` | jit |
| 3.68% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 2.78% | `python` | `tuple_dealloc` | memory |
| 2.23% | `python` | `bytes_concat` | str |
| 2.01% | `python` | `dict_get` | dict |
| 1.92% | `python` | `unicode_encode` | str |
| 1.61% | `python` | `_PyLong_New` | memory |
| 1.53% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 1.41% | `python` | `PyDict_GetItemRef` | dict |
| 1.39% | `python` | `object_dealloc` | memory |
| 1.35% | `python` | `type_new` | memory |
| 1.32% | `python` | `insertdict` | dict |
| 1.22% | `python` | `long_dealloc` | memory |
| 0.93% | `python` | `write_bytes` | unknown |
| 0.92% | `libc-2.31.so` | `__memcpy_avx_unaligned_erms` | libc |
| 0.85% | `python` | `unicode_encode_utf8` | str |
| 0.80% | `python` | `intern_common.part.0` | str |
| 0.78% | `python` | `deduce_unreachable` | gc |
| 0.68% | `python` | `_PyCode_New` | interpreter |
| 0.66% | `python` | `visit_decref` | gc |
| 0.65% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.63% | `python` | `gc_collect_region.isra.0` | gc |
| 0.62% | `python` | `PyDict_Contains` | dict |
| 0.58% | `python` | `PySys_Audit` | unknown |
| 0.56% | `python` | `_PyTuple_Resize` | tuple |
| 0.56% | `_struct.cpython-314-x86_64-linux-gnu.so` | `s_pack` | library |
| 0.55% | `python` | `_PyTuple_FromStackRefSteal` | tuple |
| 0.54% | `python` | `r_object` | import |
| 0.53% | `python` | `long_hash` | int |
| 0.52% | `python` | `_PyObject_GenericGetAttrWithDict` | dynamic |
| 0.47% | `python` | `PyUnicode_FromKindAndData` | str |
| 0.45% | `libc-2.31.so` | `_int_malloc` | libc |
| 0.43% | `python` | `visit_reachable` | gc |
| 0.40% | `python` | `builtin_id` | unknown |
| 0.36% | `python` | `builtin_getattr` | lookup |
| 0.35% | `libc-2.31.so` | `__memset_avx2_erms` | libc |
| 0.33% | `python` | `dict_dealloc` | memory |
| 0.32% | `python` | `siphash13` | str |
| 0.32% | `python` | `dictiter_iternextitem` | dict |
| 0.31% | `python` | `PyType_GetModuleByDef` | dynamic |
| 0.29% | `python` | `_PyBytesWriter_Finish` | unknown |
| 0.28% | `_struct.cpython-314-x86_64-linux-gnu.so` | `pack` | library |
| 0.28% | `python` | `PyObject_GetAttr` | dynamic |
| 0.27% | `python` | `PyNumber_Add` | dynamic |
| 0.26% | `python` | `_PyBytes_Resize` | unknown |

## pidigits

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 34.63% | `python` | `x_divrem` | int |
| 21.00% | `python` | `k_mul` | int |
| 13.03% | `python` | `x_add` | int |
| 8.17% | `python` | `x_sub` | int |
| 3.21% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 1.69% | `libc-2.31.so` | `_int_malloc` | libc |
| 1.05% | `libc-2.31.so` | `__memset_avx2_erms` | libc |
| 0.97% | `[JIT]` | `jit` | jit |
| 0.83% | `python` | `type_new` | memory |
| 0.62% | `libc-2.31.so` | `_int_free` | libc |
| 0.46% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.45% | `python` | `intern_common.part.0` | str |
| 0.43% | `python` | `_PyCode_New` | interpreter |
| 0.43% | `python` | `deduce_unreachable` | gc |
| 0.39% | `python` | `visit_decref` | gc |
| 0.39% | `python` | `gc_collect_region.isra.0` | gc |
| 0.38% | `python` | `long_dealloc` | memory |
| 0.36% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.32% | `python` | `tuple_dealloc` | memory |
| 0.28% | `python` | `r_object` | import |
| 0.27% | `libc-2.31.so` | `unlink_chunk.isra.0` | libc |
| 0.26% | `python` | `PyObject_Free` | dynamic |
| 0.25% | `python` | `visit_reachable` | gc |

## pprint

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 35.01% | `[JIT]` | `jit` | jit |
| 7.79% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 6.21% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 3.18% | `python` | `_Py_type_getattro_impl` | dynamic |
| 2.75% | `python` | `PyUnicode_Format` | str |
| 2.66% | `python` | `long_to_decimal_string_internal` | int |
| 2.45% | `python` | `tuple_dealloc` | memory |
| 2.41% | `python` | `_PyUnicode_JoinArray` | str |
| 1.78% | `python` | `unicode_dealloc` | memory |
| 1.70% | `python` | `_PyTuple_FromStackRefSteal` | tuple |
| 1.56% | `libc-2.31.so` | `__memcpy_avx_unaligned_erms` | libc |
| 1.24% | `python` | `_PyUnicodeWriter_PrepareInternal` | str |
| 1.18% | `python` | `_PySet_Contains` | miscobj |
| 1.07% | `python` | `slot_tp_init` | unknown |
| 1.03% | `python` | `PyObject_GetAttr` | dynamic |
| 0.97% | `python` | `list_dealloc` | memory |
| 0.97% | `python` | `meth_dealloc` | memory |
| 0.94% | `python` | `PyUnicode_New` | memory |
| 0.93% | `python` | `insertdict` | dict |
| 0.91% | `python` | `PyDict_Contains` | dict |
| 0.87% | `python` | `slot_tp_richcompare` | dynamic |
| 0.78% | `python` | `_PyObject_MakeTpCall` | dynamic |
| 0.76% | `python` | `builtin_issubclass` | unknown |
| 0.76% | `python` | `method_get` | dynamic |
| 0.74% | `python` | `object_new` | memory |
| 0.70% | `python` | `builtin_getattr` | lookup |
| 0.67% | `python` | `builtin_sorted` | unknown |
| 0.63% | `python` | `list_sort_impl` | list |
| 0.62% | `python` | `builtin_repr` | unknown |
| 0.61% | `python` | `long_hash` | int |
| 0.60% | `python` | `_PyLong_New` | memory |
| 0.55% | `python` | `_PyObject_Malloc` | memory |
| 0.52% | `python` | `_Py_dict_lookup` | lookup |
| 0.52% | `python` | `_PyList_FromStackRefSteal` | list |
| 0.48% | `python` | `subtype_dealloc` | memory |
| 0.45% | `python` | `unicode_repr` | str |
| 0.45% | `python` | `list_append` | list |
| 0.45% | `python` | `PyDict_DelItem` | dict |
| 0.44% | `python` | `PyObject_GC_Del` | gc |
| 0.36% | `python` | `listiter_dealloc` | memory |
| 0.33% | `python` | `_PyFunction_Vectorcall` | calls |
| 0.33% | `python` | `clear_slots` | unknown |
| 0.33% | `python` | `long_dealloc` | memory |
| 0.32% | `python` | `list_iter` | list |
| 0.30% | `python` | `PyObject_Hash` | dynamic |
| 0.30% | `python` | `tuple_iter` | tuple |
| 0.28% | `python` | `_PyArg_UnpackKeywords` | calls |
| 0.28% | `python` | `tupleiter_dealloc` | memory |
| 0.27% | `python` | `PyTuple_Pack` | tuple |
| 0.26% | `python` | `wrapperdescr_call` | unknown |
| 0.25% | `python` | `dictresize` | dict |

## pycparser

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 17.36% | `[JIT]` | `jit` | jit |
| 17.32% | `python` | `sre_ucs1_match` | library |
| 17.13% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 2.72% | `python` | `_sre_SRE_Pattern_match` | library |
| 2.61% | `python` | `PyDict_GetItemRef` | dict |
| 2.04% | `python` | `deduce_unreachable` | gc |
| 1.90% | `python` | `gc_collect_region.isra.0` | gc |
| 1.59% | `python` | `dict_get` | dict |
| 1.59% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.41% | `python` | `object_new` | memory |
| 1.27% | `libc-2.31.so` | `_int_malloc` | libc |
| 1.18% | `python` | `subtype_dealloc` | memory |
| 1.03% | `python` | `list_ass_slice_lock_held` | list |
| 1.02% | `python` | `visit_decref` | gc |
| 0.96% | `python` | `subtype_traverse` | gc |
| 0.95% | `python` | `object_isinstance` | dynamic |
| 0.84% | `python` | `visit_add_to_container` | gc |
| 0.76% | `python` | `list_dealloc` | memory |
| 0.69% | `python` | `sre_ucs1_count` | library |
| 0.66% | `python` | `PyDict_Contains` | dict |
| 0.65% | `python` | `PyObject_GC_Del` | gc |
| 0.64% | `python` | `list_subscript` | list |
| 0.63% | `libc-2.31.so` | `__memcpy_avx_unaligned_erms` | libc |
| 0.61% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.60% | `python` | `slot_mp_ass_subscript` | unknown |
| 0.58% | `libc-2.31.so` | `_int_free` | libc |
| 0.56% | `python` | `visit_reachable` | gc |
| 0.52% | `python` | `slice_dealloc` | memory |
| 0.50% | `python` | `_PyObject_MakeTpCall` | dynamic |
| 0.47% | `python` | `slot_tp_init` | unknown |
| 0.47% | `python` | `PyNumber_Negative` | dynamic |
| 0.46% | `python` | `PySlice_Unpack` | miscobj |
| 0.46% | `python` | `sre_ucs2_charset.isra.0` | library |
| 0.44% | `python` | `_PyFunction_Vectorcall` | calls |
| 0.44% | `python` | `PyObject_GetAttr` | dynamic |
| 0.42% | `libc-2.31.so` | `__libc_malloc` | libc |
| 0.42% | `python` | `PySlice_New` | memory |
| 0.39% | `python` | `PyMem_Malloc` | memory |
| 0.38% | `python` | `PyObject_Vectorcall` | dynamic |
| 0.37% | `python` | `list_ass_subscript` | list |
| 0.37% | `python` | `long_dealloc` | memory |
| 0.34% | `python` | `_PyObject_Malloc` | memory |
| 0.34% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.32% | `python` | `PyList_New` | memory |
| 0.32% | `python` | `insertdict` | dict |
| 0.32% | `libc-2.31.so` | `unlink_chunk.isra.0` | libc |
| 0.30% | `python` | `listiter_dealloc` | memory |
| 0.29% | `python` | `list_iter` | list |
| 0.28% | `python` | `PyObject_SetAttr` | dynamic |
| 0.27% | `python` | `_PyLong_New` | memory |
| 0.26% | `python` | `vectorcall_method` | calls |
| 0.25% | `python` | `_PyGC_Collect` | gc |

## pyflate

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 31.41% | `[JIT]` | `jit` | jit |
| 8.11% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 7.92% | `python` | `list_dealloc` | memory |
| 5.65% | `python` | `list_ass_slice_lock_held` | list |
| 2.81% | `python` | `long_dealloc` | memory |
| 2.67% | `python` | `list_subscript` | list |
| 2.49% | `python` | `list_concat` | list |
| 2.41% | `python` | `bytes_subscript` | str |
| 2.11% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 2.05% | `python` | `_PyLong_Add` | int |
| 1.70% | `libc-2.31.so` | `_int_malloc` | libc |
| 1.32% | `python` | `stringlib_bytes_join.lto_priv.1` | str |
| 1.31% | `python` | `long_lshift_method` | int |
| 1.29% | `python` | `_PyLong_Subtract` | int |
| 1.28% | `libc-2.31.so` | `__memcpy_avx_unaligned_erms` | libc |
| 1.08% | `python` | `_PyLong_New` | memory |
| 1.06% | `python` | `PyObject_Free` | dynamic |
| 1.00% | `python` | `PySlice_Unpack` | miscobj |
| 0.84% | `python` | `list_sort_impl` | list |
| 0.69% | `libc-2.31.so` | `_int_free` | libc |
| 0.67% | `python` | `unsafe_long_compare` | unknown |
| 0.62% | `python` | `PyObject_GetItem` | dynamic |
| 0.59% | `python` | `long_rshift` | int |
| 0.55% | `python` | `PyNumber_Lshift` | dynamic |
| 0.55% | `python` | `long_and` | int |
| 0.50% | `python` | `slice_dealloc` | memory |
| 0.45% | `python` | `PyMem_Malloc` | memory |
| 0.44% | `python` | `_PyBytes_FromList` | unknown |
| 0.43% | `python` | `enum_next` | miscobj |
| 0.41% | `python` | `list_new_prealloc` | memory |
| 0.38% | `python` | `PyLong_FromLong` | int |
| 0.37% | `python` | `PyList_New` | memory |
| 0.36% | `python` | `_PyLong_FromSTwoDigits` | int |
| 0.36% | `python` | `PyLong_FromSsize_t` | int |
| 0.35% | `python` | `type_new` | memory |
| 0.35% | `python` | `PyNumber_And` | dynamic |
| 0.30% | `libc-2.31.so` | `__libc_malloc` | libc |
| 0.30% | `python` | `list_iter` | list |
| 0.29% | `python` | `PyObject_Size` | dynamic |
| 0.29% | `python` | `listiter_dealloc` | memory |
| 0.28% | `python` | `_PyBuildSlice_ConsumeRefs` | miscobj |
| 0.27% | `python` | `long_sub` | int |
| 0.26% | `libc-2.31.so` | `unlink_chunk.isra.0` | libc |
| 0.25% | `python` | `_Py_Dealloc` | memory |

## pylint

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 18.90% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 8.50% | `python` | `deduce_unreachable` | gc |
| 8.08% | `[JIT]` | `jit` | jit |
| 6.98% | `python` | `gc_collect_region.isra.0` | gc |
| 4.09% | `python` | `visit_decref` | gc |
| 3.28% | `python` | `visit_reachable` | gc |
| 2.12% | `python` | `visit_add_to_container` | gc |
| 1.65% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.63% | `python` | `subtype_traverse` | gc |
| 1.58% | `python` | `PyDict_GetItemRef` | dict |
| 1.43% | `python` | `PyObject_GetAttr` | dynamic |
| 0.95% | `python` | `dict_traverse` | gc |
| 0.93% | `python` | `list_traverse` | gc |
| 0.86% | `python` | `object_isinstance` | dynamic |
| 0.82% | `python` | `_PyObject_GetMethod` | dynamic |
| 0.82% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.76% | `python` | `tuple_dealloc` | memory |
| 0.74% | `python` | `find_name_in_mro` | lookup |
| 0.71% | `python` | `PyObject_SetAttr` | dynamic |
| 0.68% | `python` | `_PyFunction_Vectorcall` | calls |
| 0.67% | `python` | `dict_dealloc` | memory |
| 0.62% | `python` | `insertdict` | dict |
| 0.61% | `python` | `list_dealloc` | memory |
| 0.55% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.51% | `python` | `_PyGC_Collect` | gc |
| 0.47% | `python` | `intern_common.part.0` | str |
| 0.46% | `python` | `subtype_dealloc` | memory |
| 0.46% | `python` | `_Py_MakeCoro` | unknown |
| 0.41% | `libc-2.31.so` | `__memcpy_avx_unaligned_erms` | libc |
| 0.40% | `python` | `gen_dealloc` | memory |
| 0.40% | `python` | `type_new` | memory |
| 0.40% | `python` | `uop_optimize` | compiler |
| 0.36% | `python` | `islice_next` | unknown |
| 0.34% | `python` | `_PySuper_Lookup` | dynamic |
| 0.32% | `python` | `PyMem_Free` | memory |
| 0.32% | `python` | `_PyObject_MakeTpCall` | dynamic |
| 0.31% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.31% | `python` | `listiter_dealloc` | memory |
| 0.30% | `python` | `list_iter` | list |
| 0.30% | `python` | `unicode_dealloc` | memory |
| 0.29% | `python` | `_Py_slot_tp_getattr_hook` | unknown |
| 0.26% | `python` | `siphash13` | str |
| 0.25% | `python` | `_PyStack_UnpackDict` | unknown |

## python_startup

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 8.78% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 5.94% | `python` | `type_new` | memory |
| 3.17% | `python` | `intern_common.part.0` | str |
| 2.93% | `python` | `_PyCode_New` | interpreter |
| 2.83% | `python` | `visit_decref` | gc |
| 2.73% | `python` | `deduce_unreachable` | gc |
| 2.49% | `python` | `r_object` | import |
| 1.88% | `python` | `gc_collect_region.isra.0` | gc |
| 1.82% | `python` | `PyUnicode_FromKindAndData` | str |
| 1.69% | `python` | `visit_reachable` | gc |
| 1.47% | `python` | `siphash13` | str |
| 1.18% | `libc-2.31.so` | `__memcpy_avx_unaligned_erms` | libc |
| 1.14% | `python` | `tuple_dealloc` | memory |
| 0.98% | `python` | `type_ready` | dynamic |
| 0.92% | `python` | `unicode_dealloc` | memory |
| 0.92% | `python` | `insertdict` | dict |
| 0.87% | `python` | `PyDict_GetItemRef` | dict |
| 0.84% | `python` | `find_name_in_mro` | lookup |
| 0.76% | `python` | `dict_traverse` | gc |
| 0.72% | `python` | `PyDict_SetItem` | dict |
| 0.71% | `[kernel.kallsyms]` | `native_irq_return_iret` | kernel |
| 0.71% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.69% | `[kernel.kallsyms]` | `filemap_map_pages` | kernel |
| 0.67% | `python` | `dictresize` | dict |
| 0.59% | `ld-2.31.so` | `do_lookup_x` | library |
| 0.58% | `libc-2.31.so` | `_int_malloc` | libc |
| 0.55% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.52% | `python` | `_PyEval_LoadGlobalStackRef` | interpreter |
| 0.51% | `python` | `_Py_dict_lookup` | lookup |
| 0.51% | `libc-2.31.so` | `__strlen_avx2` | libc |
| 0.51% | `python` | `PyBytes_FromStringAndSize` | str |
| 0.51% | `python` | `dict_dealloc` | memory |
| 0.46% | `python` | `code_dealloc` | memory |
| 0.44% | `[kernel.kallsyms]` | `sync_regs` | kernel |
| 0.44% | `python` | `list_dealloc` | memory |
| 0.43% | `python` | `PyFunction_NewWithQualName` | memory |
| 0.42% | `[kernel.kallsyms]` | `clear_page_erms` | kernel |
| 0.39% | `python` | `PyType_GenericAlloc` | memory |
| 0.39% | `ld-2.31.so` | `strcmp` | library |
| 0.39% | `[JIT]` | `jit` | jit |
| 0.39% | `libc-2.31.so` | `wcsrtombs` | libc |
| 0.38% | `libc-2.31.so` | `__memcmp_avx2_movbe` | libc |
| 0.37% | `python` | `tuple_traverse` | gc |
| 0.35% | `python` | `_PyObject_GC_NewVar` | gc |
| 0.34% | `python` | `_add_methods_to_object` | unknown |
| 0.34% | `ld-2.31.so` | `_dl_relocate_object` | library |
| 0.32% | `python` | `PyUnicode_FromString` | str |
| 0.31% | `[kernel.kallsyms]` | `zap_pte_range.isra.0` | kernel |
| 0.31% | `python` | `func_dealloc` | memory |
| 0.30% | `ld-2.31.so` | `_dl_lookup_symbol_x` | library |
| 0.29% | `libc-2.31.so` | `__gconv_transform_internal_utf8` | libc |
| 0.29% | `python` | `PyObject_GetAttr` | dynamic |
| 0.28% | `[kernel.kallsyms]` | `__d_lookup_rcu` | kernel |
| 0.28% | `python` | `func_traverse` | gc |
| 0.27% | `python` | `set_traverse` | gc |
| 0.27% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.26% | `[kernel.kallsyms]` | `rmqueue` | kernel |
| 0.26% | `python` | `PyTuple_New` | memory |
| 0.26% | `libc-2.31.so` | `__libc_malloc` | libc |
| 0.25% | `python` | `PyObject_SetAttr` | dynamic |
| 0.25% | `python` | `subtype_dealloc` | memory |

## python_startup_no_site

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 7.90% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 5.77% | `python` | `type_new` | memory |
| 3.48% | `python` | `intern_common.part.0` | str |
| 2.83% | `python` | `deduce_unreachable` | gc |
| 2.83% | `python` | `visit_decref` | gc |
| 2.70% | `python` | `_PyCode_New` | interpreter |
| 2.17% | `python` | `r_object` | import |
| 2.17% | `python` | `gc_collect_region.isra.0` | gc |
| 1.74% | `python` | `visit_reachable` | gc |
| 1.67% | `python` | `siphash13` | str |
| 1.65% | `python` | `PyUnicode_FromKindAndData` | str |
| 1.16% | `libc-2.31.so` | `__memcpy_avx_unaligned_erms` | libc |
| 1.15% | `ld-2.31.so` | `_dl_relocate_object` | library |
| 1.09% | `python` | `insertdict` | dict |
| 1.07% | `python` | `type_ready` | dynamic |
| 1.05% | `python` | `tuple_dealloc` | memory |
| 1.00% | `[kernel.kallsyms]` | `native_irq_return_iret` | kernel |
| 0.96% | `ld-2.31.so` | `do_lookup_x` | library |
| 0.94% | `[kernel.kallsyms]` | `filemap_map_pages` | kernel |
| 0.89% | `python` | `unicode_dealloc` | memory |
| 0.81% | `python` | `dict_traverse` | gc |
| 0.76% | `python` | `find_name_in_mro` | lookup |
| 0.73% | `python` | `PyDict_GetItemRef` | dict |
| 0.71% | `[kernel.kallsyms]` | `sync_regs` | kernel |
| 0.70% | `libc-2.31.so` | `wcsrtombs` | libc |
| 0.68% | `python` | `dictresize` | dict |
| 0.61% | `python` | `PyDict_SetItem` | dict |
| 0.58% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.57% | `python` | `_Py_dict_lookup` | lookup |
| 0.56% | `libc-2.31.so` | `__strlen_avx2` | libc |
| 0.56% | `libc-2.31.so` | `_int_malloc` | libc |
| 0.55% | `python` | `dict_dealloc` | memory |
| 0.55% | `[kernel.kallsyms]` | `copy_page` | kernel |
| 0.54% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.52% | `libc-2.31.so` | `__gconv_transform_internal_utf8` | libc |
| 0.50% | `[kernel.kallsyms]` | `clear_page_erms` | kernel |
| 0.47% | `python` | `_add_methods_to_object` | unknown |
| 0.46% | `ld-2.31.so` | `strcmp` | library |
| 0.44% | `ld-2.31.so` | `_dl_lookup_symbol_x` | library |
| 0.43% | `python` | `PyBytes_FromStringAndSize` | str |
| 0.42% | `[kernel.kallsyms]` | `zap_pte_range.isra.0` | kernel |
| 0.40% | `python` | `PyUnicode_FromString` | str |
| 0.39% | `[JIT]` | `jit` | jit |
| 0.38% | `python` | `_PyObject_GC_NewVar` | gc |
| 0.38% | `python` | `code_dealloc` | memory |
| 0.36% | `python` | `PyType_GenericAlloc` | memory |
| 0.35% | `python` | `list_dealloc` | memory |
| 0.34% | `python` | `PyFunction_NewWithQualName` | memory |
| 0.34% | `ld-2.31.so` | `check_match` | library |
| 0.33% | `python` | `PyDict_SetItemString` | dict |
| 0.33% | `python` | `_PyEval_LoadGlobalStackRef` | interpreter |
| 0.33% | `python` | `tuple_traverse` | gc |
| 0.30% | `[kernel.kallsyms]` | `release_pages` | kernel |
| 0.30% | `[kernel.kallsyms]` | `__handle_mm_fault` | kernel |
| 0.28% | `[kernel.kallsyms]` | `_raw_spin_lock` | kernel |
| 0.28% | `python` | `func_dealloc` | memory |
| 0.27% | `libc-2.31.so` | `_int_free` | libc |
| 0.26% | `libc-2.31.so` | `__memcmp_avx2_movbe` | libc |
| 0.26% | `[kernel.kallsyms]` | `rmqueue` | kernel |
| 0.25% | `python` | `_PyEvalFramePushAndInit` | interpreter |

## raytrace

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 31.98% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 24.13% | `[JIT]` | `jit` | jit |
| 7.15% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 3.37% | `python` | `_PyFloat_FromDouble_ConsumeInputs` | float |
| 2.70% | `python` | `subtype_dealloc` | memory |
| 2.55% | `python` | `PyType_GenericAlloc` | memory |
| 1.60% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 1.55% | `python` | `vectorcall_maybe.constprop.0` | unknown |
| 1.44% | `python` | `PyObject_GC_Del` | gc |
| 1.31% | `python` | `float_dealloc` | memory |
| 1.07% | `python` | `PyNumber_Subtract` | dynamic |
| 0.92% | `python` | `float_sub` | float |
| 0.90% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.61% | `python` | `tuple_dealloc` | memory |
| 0.58% | `python` | `float_richcompare` | float |
| 0.54% | `python` | `type_new` | memory |
| 0.51% | `python` | `PyObject_RichCompare` | dynamic |
| 0.45% | `python` | `long_dealloc` | memory |
| 0.41% | `python` | `float_mul` | float |
| 0.39% | `python` | `PyLong_AsDouble` | int |
| 0.39% | `python` | `PyNumber_Multiply` | dynamic |
| 0.38% | `python` | `convert_to_double` | unknown |
| 0.36% | `python` | `_PyTuple_FromStackRefSteal` | tuple |
| 0.33% | `python` | `list_dealloc` | memory |
| 0.31% | `python` | `_PyFloat_ExactDealloc` | memory |
| 0.31% | `python` | `intern_common.part.0` | str |
| 0.30% | `python` | `slot_nb_subtract` | unknown |
| 0.28% | `python` | `PyType_IsSubtype` | dynamic |
| 0.28% | `python` | `PyNumber_Add` | dynamic |
| 0.26% | `python` | `visit_decref` | gc |
| 0.26% | `python` | `float_add` | float |
| 0.26% | `python` | `deduce_unreachable` | gc |
| 0.25% | `python` | `_PyCode_New` | interpreter |
| 0.25% | `python` | `float_div` | float |

## regex_compile

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 26.34% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 17.54% | `[JIT]` | `jit` | jit |
| 4.03% | `python` | `sre_ucs1_match` | library |
| 3.05% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.96% | `python` | `bytearray_ass_subscript` | miscobj |
| 1.14% | `python` | `long_dealloc` | memory |
| 1.12% | `python` | `PyLong_FromLong` | int |
| 1.09% | `python` | `object_isinstance` | dynamic |
| 1.09% | `python` | `PyObject_GetAttr` | dynamic |
| 0.98% | `python` | `tuple_dealloc` | memory |
| 0.96% | `python` | `sre_ucs2_charset.isra.0` | library |
| 0.93% | `python` | `list_dealloc` | memory |
| 0.86% | `python` | `type_new` | memory |
| 0.69% | `python` | `PyMem_Free` | memory |
| 0.58% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.55% | `python` | `_PyTuple_FromStackRefSteal` | tuple |
| 0.55% | `python` | `deduce_unreachable` | gc |
| 0.53% | `python` | `slot_sq_item` | unknown |
| 0.53% | `python` | `PyDict_GetItemRef` | dict |
| 0.52% | `python` | `intern_common.part.0` | str |
| 0.51% | `python` | `vectorcall_method` | calls |
| 0.50% | `python` | `sre_search` | library |
| 0.50% | `python` | `_PyCode_New` | interpreter |
| 0.49% | `libc-2.31.so` | `__memcpy_avx_unaligned_erms` | libc |
| 0.48% | `python` | `visit_decref` | gc |
| 0.45% | `python` | `gc_collect_region.isra.0` | gc |
| 0.44% | `python` | `PyUnicode_Contains` | str |
| 0.42% | `python` | `meth_dealloc` | memory |
| 0.42% | `python` | `method_dealloc` | memory |
| 0.41% | `python` | `PyMem_Malloc` | memory |
| 0.40% | `python` | `list_append` | list |
| 0.39% | `python` | `uop_optimize` | compiler |
| 0.39% | `python` | `subtype_dealloc` | memory |
| 0.38% | `python` | `siphash13` | str |
| 0.37% | `python` | `PyMem_Realloc` | memory |
| 0.37% | `python` | `frame_dealloc` | memory |
| 0.35% | `python` | `_PyFrame_MakeAndSetFrameObject` | unknown |
| 0.35% | `python` | `BaseException_vectorcall` | exceptions |
| 0.34% | `python` | `PyTraceBack_Here` | exceptions |
| 0.34% | `python` | `sre_ucs1_count` | library |
| 0.33% | `python` | `_PyObject_Malloc` | memory |
| 0.33% | `python` | `r_object` | import |
| 0.33% | `python` | `list_iter` | list |
| 0.32% | `python` | `listiter_dealloc` | memory |
| 0.32% | `python` | `builtin_min` | unknown |
| 0.32% | `python` | `PyType_GenericAlloc` | memory |
| 0.31% | `python` | `_PyLong_Add` | int |
| 0.31% | `python` | `PyObject_SetItem` | dynamic |
| 0.31% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.31% | `python` | `PyObject_GC_Del` | gc |
| 0.30% | `python` | `visit_reachable` | gc |
| 0.30% | `python` | `_PySet_Contains` | miscobj |
| 0.29% | `libc-2.31.so` | `_int_malloc` | libc |
| 0.29% | `python` | `func_descr_get` | unknown |
| 0.28% | `python` | `_Py_Dealloc` | memory |
| 0.27% | `python` | `unicode_dealloc` | memory |
| 0.27% | `python` | `method_get` | dynamic |
| 0.26% | `python` | `PyNumber_And` | dynamic |
| 0.26% | `python` | `PyUnicode_FromKindAndData` | str |

## regex_dna

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 36.07% | `python` | `sre_ucs1_match` | library |
| 29.41% | `python` | `sre_ucs2_charset.isra.0` | library |
| 5.98% | `python` | `sre_search` | library |
| 3.30% | `[JIT]` | `jit` | jit |
| 3.13% | `libm-2.31.so` | `__fmod_finite@GLIBC_2.15` | library |
| 1.66% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 1.18% | `_bisect.cpython-314-x86_64-linux-gnu.so` | `_bisect_bisect_right` | library |
| 1.00% | `python` | `pattern_subx` | library |
| 0.97% | `libc-2.31.so` | `__memcpy_avx_unaligned_erms` | libc |
| 0.79% | `python` | `float_richcompare` | float |
| 0.72% | `python` | `_PyFloat_FromDouble_ConsumeInputs` | float |
| 0.63% | `python` | `type_new` | memory |
| 0.62% | `python` | `stringlib_bytes_join.lto_priv.1` | str |
| 0.41% | `python` | `float_rem` | float |
| 0.40% | `python` | `PyFloat_FromDouble` | float |
| 0.38% | `python` | `float_dealloc` | memory |
| 0.37% | `python` | `bytearray_ass_subscript` | miscobj |
| 0.34% | `python` | `intern_common.part.0` | str |
| 0.33% | `python` | `visit_decref` | gc |
| 0.33% | `python` | `_PyCode_New` | interpreter |
| 0.32% | `python` | `PyBytes_FromStringAndSize` | str |
| 0.31% | `python` | `gc_collect_region.isra.0` | gc |
| 0.31% | `python` | `deduce_unreachable` | gc |
| 0.30% | `python` | `list_item` | list |
| 0.27% | `python` | `float_div` | float |

## regex_effbot

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 38.83% | `python` | `sre_ucs1_match` | library |
| 16.91% | `python` | `sre_ucs2_charset.isra.0` | library |
| 9.06% | `python` | `PyMem_Free` | memory |
| 5.95% | `python` | `PyMem_Malloc` | memory |
| 5.83% | `python` | `sre_search` | library |
| 2.94% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 2.23% | `python` | `sre_ucs1_count` | library |
| 0.94% | `python` | `type_new` | memory |
| 0.74% | `[JIT]` | `jit` | jit |
| 0.55% | `python` | `deduce_unreachable` | gc |
| 0.50% | `python` | `intern_common.part.0` | str |
| 0.47% | `python` | `siphash13` | str |
| 0.44% | `python` | `_PyCode_New` | interpreter |
| 0.43% | `python` | `gc_collect_region.isra.0` | gc |
| 0.43% | `python` | `visit_decref` | gc |
| 0.36% | `python` | `r_object` | import |
| 0.34% | `python` | `visit_reachable` | gc |
| 0.29% | `python` | `tuple_dealloc` | memory |
| 0.27% | `python` | `PyUnicode_FromKindAndData` | str |
| 0.25% | `python` | `_PyEval_FrameClearAndPop` | interpreter |

## regex_v8

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 35.34% | `python` | `sre_ucs1_match` | library |
| 5.54% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 4.43% | `python` | `sre_ucs1_count` | library |
| 3.48% | `python` | `PyCode_Addr2Line` | exceptions |
| 3.37% | `python` | `sre_search` | library |
| 3.23% | `[JIT]` | `jit` | jit |
| 1.27% | `libc-2.31.so` | `_int_malloc` | libc |
| 1.22% | `python` | `type_new` | memory |
| 1.22% | `python` | `pattern_subx` | library |
| 1.13% | `python` | `state_init` | unknown |
| 1.03% | `python` | `PyMem_Free` | memory |
| 0.86% | `python` | `sre_ucs1_match.cold` | library |
| 0.81% | `python` | `deduce_unreachable` | gc |
| 0.80% | `python` | `intern_common.part.0` | str |
| 0.78% | `libc-2.31.so` | `__memcpy_avx_unaligned_erms` | libc |
| 0.78% | `libc-2.31.so` | `_int_free` | libc |
| 0.77% | `python` | `PyDict_GetItemRef` | dict |
| 0.71% | `python` | `_PyCode_New` | interpreter |
| 0.68% | `python` | `PyMem_Malloc` | memory |
| 0.66% | `libc-2.31.so` | `__libc_malloc` | libc |
| 0.65% | `python` | `visit_decref` | gc |
| 0.63% | `python` | `list_dealloc` | memory |
| 0.60% | `python` | `gc_collect_region.isra.0` | gc |
| 0.58% | `python` | `PyUnicode_Substring` | str |
| 0.55% | `python` | `unicode_dealloc` | memory |
| 0.55% | `python` | `_PyUnicode_IsAlpha` | str |
| 0.53% | `python` | `_PyUnicode_JoinArray` | str |
| 0.52% | `python` | `PyLong_FromLong` | int |
| 0.52% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.51% | `python` | `bytearray_ass_subscript` | miscobj |
| 0.50% | `python` | `r_object` | import |
| 0.47% | `python` | `long_dealloc` | memory |
| 0.44% | `python` | `Py_UNICODE_ISALNUM.lto_priv.1` | unknown |
| 0.44% | `python` | `tuple_dealloc` | memory |
| 0.44% | `python` | `_PyObject_Malloc` | memory |
| 0.40% | `python` | `visit_reachable` | gc |
| 0.39% | `python` | `siphash13` | str |
| 0.39% | `python` | `_PyObject_GC_NewVar` | gc |
| 0.38% | `python` | `PyUnicode_FromKindAndData` | str |
| 0.32% | `python` | `PyMem_Realloc` | memory |
| 0.30% | `python` | `PyList_Append` | list |
| 0.30% | `python` | `sre_ucs2_charset.isra.0` | library |
| 0.28% | `python` | `pattern_new_match.isra.0` | memory |
| 0.28% | `python` | `object_isinstance` | dynamic |
| 0.27% | `python` | `uop_optimize` | compiler |

## richards

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 49.68% | `[JIT]` | `jit` | jit |
| 18.38% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 5.60% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 3.90% | `python` | `_PyObject_GetMethod` | dynamic |
| 1.61% | `python` | `PyObject_GetAttr` | dynamic |
| 1.42% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 1.01% | `python` | `PyObject_SetAttr` | dynamic |
| 0.98% | `python` | `long_dealloc` | memory |
| 0.89% | `python` | `type_new` | memory |
| 0.56% | `python` | `_PyLong_Add` | int |
| 0.50% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.47% | `python` | `intern_common.part.0` | str |
| 0.47% | `python` | `deduce_unreachable` | gc |
| 0.46% | `python` | `_PyCode_New` | interpreter |
| 0.44% | `python` | `gc_collect_region.isra.0` | gc |
| 0.42% | `python` | `visit_decref` | gc |
| 0.40% | `python` | `_PyLong_Subtract` | int |
| 0.30% | `python` | `r_object` | import |
| 0.28% | `python` | `visit_reachable` | gc |
| 0.25% | `python` | `PyUnicode_FromKindAndData` | str |

## richards_super

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 33.08% | `[JIT]` | `jit` | jit |
| 31.56% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 5.94% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 4.34% | `python` | `_PyObject_GetMethod` | dynamic |
| 2.99% | `python` | `_PySuper_Lookup` | dynamic |
| 2.79% | `python` | `PyObject_SetAttr` | dynamic |
| 1.48% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 1.47% | `python` | `PyObject_GetAttr` | dynamic |
| 0.81% | `python` | `type_new` | memory |
| 0.77% | `python` | `long_dealloc` | memory |
| 0.56% | `python` | `long_add` | int |
| 0.56% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.49% | `python` | `intern_common.part.0` | str |
| 0.45% | `python` | `deduce_unreachable` | gc |
| 0.39% | `python` | `_PyCode_New` | interpreter |
| 0.38% | `python` | `visit_decref` | gc |
| 0.38% | `python` | `gc_collect_region.isra.0` | gc |
| 0.32% | `python` | `r_object` | import |
| 0.26% | `python` | `visit_reachable` | gc |
| 0.25% | `python` | `long_sub` | int |

## scimark

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 22.85% | `[JIT]` | `jit` | jit |
| 10.93% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 7.16% | `python` | `PyNumber_AsSsize_t` | dynamic |
| 4.59% | `python` | `long_dealloc` | memory |
| 3.99% | `array.cpython-314-x86_64-linux-gnu.so` | `array_subscr` | library |
| 3.44% | `python` | `_PyFloat_FromDouble_ConsumeInputs` | float |
| 2.89% | `python` | `_PyLong_Add` | int |
| 2.52% | `python` | `vgetargs1_impl` | calls |
| 2.49% | `python` | `PyLong_FromLong` | int |
| 2.36% | `python` | `PyObject_GetItem` | dynamic |
| 1.98% | `python` | `convertitem` | unknown |
| 1.96% | `python` | `PyFloat_FromDouble` | float |
| 1.88% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.46% | `array.cpython-314-x86_64-linux-gnu.so` | `array_ass_subscr` | library |
| 1.28% | `python` | `object_isinstance` | dynamic |
| 1.24% | `python` | `float_dealloc` | memory |
| 1.17% | `python` | `_PyLong_Multiply` | int |
| 1.02% | `python` | `PyIndex_Check` | unknown |
| 0.96% | `python` | `PyObject_Free` | dynamic |
| 0.92% | `python` | `PyType_GetModuleByDef` | dynamic |
| 0.85% | `array.cpython-314-x86_64-linux-gnu.so` | `d_setitem` | library |
| 0.82% | `python` | `PyArg_Parse` | calls |
| 0.80% | `python` | `_Py_Dealloc` | memory |
| 0.77% | `python` | `PyObject_SetItem` | dynamic |
| 0.69% | `python` | `type_new` | memory |
| 0.63% | `python` | `_PyFloat_ExactDealloc` | memory |
| 0.57% | `python` | `tuple_dealloc` | memory |
| 0.52% | `python` | `PyFloat_AsDouble` | float |
| 0.44% | `array.cpython-314-x86_64-linux-gnu.so` | `d_getitem` | library |
| 0.42% | `python` | `_PyTuple_FromStackRefSteal` | tuple |
| 0.42% | `python` | `_PyLong_Frexp` | int |
| 0.39% | `python` | `float_richcompare` | float |
| 0.36% | `python` | `intern_common.part.0` | str |
| 0.35% | `python` | `_PyCode_New` | interpreter |
| 0.32% | `python` | `range_vectorcall` | miscobj |
| 0.31% | `python` | `visit_decref` | gc |
| 0.30% | `python` | `deduce_unreachable` | gc |
| 0.30% | `python` | `_PyFrame_PushUnchecked.isra.0` | unknown |
| 0.30% | `array.cpython-314-x86_64-linux-gnu.so` | `0x00000000000049c4` | library |
| 0.30% | `python` | `_PyLong_Subtract` | int |
| 0.30% | `python` | `gc_collect_region.isra.0` | gc |
| 0.29% | `array.cpython-314-x86_64-linux-gnu.so` | `0x00000000000047e4` | library |
| 0.27% | `python` | `PyObject_RichCompare` | dynamic |
| 0.26% | `array.cpython-314-x86_64-linux-gnu.so` | `0x0000000000004854` | library |
| 0.26% | `python` | `range_iter` | miscobj |
| 0.25% | `python` | `r_object` | import |

## spectral_norm

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 22.39% | `[JIT]` | `jit` | jit |
| 11.22% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 9.38% | `python` | `_PyLong_Add` | int |
| 5.49% | `python` | `long_dealloc` | memory |
| 4.25% | `python` | `long_div` | int |
| 4.19% | `python` | `PyObject_Free` | dynamic |
| 3.79% | `python` | `_PyLong_Multiply` | int |
| 3.10% | `python` | `float_div` | float |
| 2.68% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 2.20% | `python` | `enum_next` | miscobj |
| 1.98% | `python` | `_PyFloat_FromDouble_ConsumeInputs` | float |
| 1.82% | `python` | `listiter_next` | list |
| 1.53% | `python` | `PyNumber_TrueDivide` | dynamic |
| 1.16% | `python` | `convert_to_double` | unknown |
| 1.15% | `python` | `type_new` | memory |
| 1.04% | `python` | `PyLong_AsDouble` | int |
| 1.01% | `python` | `PyType_IsSubtype` | dynamic |
| 0.98% | `python` | `PyNumber_FloorDivide` | dynamic |
| 0.68% | `python` | `intern_common.part.0` | str |
| 0.64% | `python` | `_PyCode_New` | interpreter |
| 0.63% | `python` | `deduce_unreachable` | gc |
| 0.57% | `python` | `visit_decref` | gc |
| 0.56% | `python` | `gc_collect_region.isra.0` | gc |
| 0.47% | `python` | `r_object` | import |
| 0.47% | `python` | `_Py_Dealloc` | memory |
| 0.43% | `python` | `float_dealloc` | memory |
| 0.43% | `python` | `visit_reachable` | gc |
| 0.41% | `python` | `_Py_NewReference` | memory |
| 0.37% | `python` | `tuple_dealloc` | memory |
| 0.36% | `python` | `PyUnicode_FromKindAndData` | str |
| 0.29% | `python` | `siphash13` | str |
| 0.29% | `libc-2.31.so` | `__memcpy_avx_unaligned_erms` | libc |

## sphinx

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 18.24% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 8.69% | `[JIT]` | `jit` | jit |
| 6.40% | `python` | `sre_ucs1_match` | library |
| 3.05% | `python` | `deduce_unreachable` | gc |
| 3.03% | `python` | `sre_ucs2_charset.isra.0` | library |
| 2.38% | `python` | `PyObject_GetAttr` | dynamic |
| 2.31% | `python` | `gc_collect_region.isra.0` | gc |
| 1.94% | `python` | `visit_decref` | gc |
| 1.70% | `python` | `object_isinstance` | dynamic |
| 1.58% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.45% | `_pickle.cpython-314-x86_64-linux-gnu.so` | `save` | library |
| 1.39% | `python` | `visit_add_to_container` | gc |
| 1.31% | `python` | `PyDict_GetItemRef` | dict |
| 1.29% | `python` | `visit_reachable` | gc |
| 1.08% | `libc-2.31.so` | `__memcpy_avx_unaligned_erms` | libc |
| 1.04% | `python` | `find_name_in_mro` | lookup |
| 0.89% | `python` | `_PyObject_GetMethod` | dynamic |
| 0.84% | `python` | `PyUnicode_Format` | str |
| 0.82% | `python` | `siphash13` | str |
| 0.76% | `python` | `dict_traverse` | gc |
| 0.75% | `python` | `list_dealloc` | memory |
| 0.74% | `python` | `tuple_dealloc` | memory |
| 0.68% | `python` | `gen_dealloc` | memory |
| 0.65% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.64% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.62% | `python` | `_Py_MakeCoro` | unknown |
| 0.61% | `python` | `PyObject_SetAttr` | dynamic |
| 0.52% | `python` | `PyMem_Free` | memory |
| 0.51% | `python` | `subtype_traverse` | gc |
| 0.50% | `python` | `unicode_dealloc` | memory |
| 0.48% | `python` | `type_new` | memory |
| 0.44% | `python` | `dict_dealloc` | memory |
| 0.43% | `python` | `PyMem_Malloc` | memory |
| 0.43% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.43% | `python` | `uop_optimize` | compiler |
| 0.40% | `python` | `_PyFunction_Vectorcall` | calls |
| 0.39% | `python` | `list_traverse` | gc |
| 0.38% | `python` | `getset_get` | dynamic |
| 0.37% | `_pickle.cpython-314-x86_64-linux-gnu.so` | `memo_put.isra.0` | library |
| 0.36% | `python` | `_PyGC_Collect` | gc |
| 0.36% | `python` | `insertdict` | dict |
| 0.35% | `python` | `listiter_dealloc` | memory |
| 0.34% | `python` | `sre_search` | library |
| 0.34% | `libc-2.31.so` | `_int_malloc` | libc |
| 0.33% | `python` | `list_iter` | list |
| 0.33% | `python` | `intern_common.part.0` | str |
| 0.32% | `python` | `tupleiter_dealloc` | memory |
| 0.31% | `python` | `tuple_iter` | tuple |
| 0.31% | `python` | `PyObject_GetOptionalAttr` | dynamic |
| 0.30% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 0.28% | `python` | `_PyObject_GC_New` | gc |
| 0.27% | `python` | `_PyObject_GenericGetAttrWithDict` | dynamic |
| 0.26% | `python` | `sre_ucs1_count` | library |
| 0.26% | `python` | `_PyTuple_FromStackRefSteal` | tuple |
| 0.26% | `python` | `method_get` | dynamic |
| 0.25% | `python` | `sre_ucs2_match` | library |

## sqlalchemy_declarative

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 21.90% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 7.39% | `[JIT]` | `jit` | jit |
| 2.52% | `python` | `type_new` | memory |
| 2.22% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.88% | `python` | `PyObject_GetAttr` | dynamic |
| 1.83% | `python` | `tuple_dealloc` | memory |
| 1.61% | `python` | `PyObject_SetAttr` | dynamic |
| 1.37% | `python` | `find_name_in_mro` | lookup |
| 1.29% | `python` | `deduce_unreachable` | gc |
| 1.20% | `python` | `PyDict_GetItemRef` | dict |
| 1.06% | `python` | `gc_collect_region.isra.0` | gc |
| 1.04% | `python` | `intern_common.part.0` | str |
| 1.02% | `python` | `visit_decref` | gc |
| 1.00% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.81% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.79% | `python` | `dict_dealloc` | memory |
| 0.77% | `python` | `_PyCode_New` | interpreter |
| 0.72% | `python` | `visit_reachable` | gc |
| 0.72% | `python` | `subtype_dealloc` | memory |
| 0.70% | `libpthread-2.31.so` | `__pthread_mutex_lock` | library |
| 0.64% | `libc-2.31.so` | `__memcpy_avx_unaligned_erms` | libc |
| 0.60% | `libpthread-2.31.so` | `pthread_mutex_unlock` | library |
| 0.59% | `python` | `list_dealloc` | memory |
| 0.57% | `python` | `r_object` | import |
| 0.55% | `python` | `insertdict` | dict |
| 0.48% | `python` | `PyUnicode_FromKindAndData` | str |
| 0.47% | `python` | `_PyObject_GetMethod` | dynamic |
| 0.46% | `python` | `list_iter` | list |
| 0.44% | `python` | `siphash13` | str |
| 0.44% | `python` | `PyType_GenericAlloc` | memory |
| 0.42% | `python` | `listiter_dealloc` | memory |
| 0.41% | `python` | `sre_ucs1_match` | library |
| 0.40% | `python` | `_PyObject_MakeTpCall` | dynamic |
| 0.40% | `python` | `PyObject_Vectorcall` | dynamic |
| 0.39% | `python` | `_Py_type_getattro` | lookup |
| 0.39% | `python` | `set_dealloc` | memory |
| 0.39% | `python` | `PyFunction_NewWithQualName` | memory |
| 0.39% | `python` | `tuple_hash` | tuple |
| 0.39% | `python` | `unicode_dealloc` | memory |
| 0.36% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.36% | `python` | `PyObject_GC_Del` | gc |
| 0.35% | `python` | `_Py_slot_tp_getattr_hook` | unknown |
| 0.35% | `libsqlite3.so.0.8.6` | `sqlite3_reset` | library |
| 0.34% | `python` | `_PyTuple_FromStackRefSteal` | tuple |
| 0.33% | `libc-2.31.so` | `_int_malloc` | libc |
| 0.33% | `python` | `slot_tp_init` | unknown |
| 0.32% | `python` | `_PyFunction_Vectorcall` | calls |
| 0.32% | `python` | `uop_optimize` | compiler |
| 0.31% | `python` | `code_dealloc` | memory |
| 0.31% | `python` | `PyObject_IsTrue` | dynamic |
| 0.30% | `python` | `slot_mp_subscript` | unknown |
| 0.30% | `python` | `type_ready` | dynamic |
| 0.29% | `python` | `func_dealloc` | memory |
| 0.28% | `python` | `PyDict_Contains` | dict |
| 0.28% | `python` | `PyMem_Free` | memory |
| 0.27% | `python` | `take_gil` | gil |
| 0.27% | `python` | `tp_new_wrapper` | memory |
| 0.27% | `python` | `PyDict_SetItem` | dict |
| 0.26% | `python` | `_PyObject_GC_New` | gc |
| 0.26% | `python` | `dictresize` | dict |
| 0.26% | `python` | `dict_traverse` | gc |
| 0.25% | `python` | `method_dealloc` | memory |

## sqlalchemy_imperative

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 27.79% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 3.91% | `[JIT]` | `jit` | jit |
| 2.66% | `python` | `type_new` | memory |
| 2.53% | `python` | `PyObject_GetAttr` | dynamic |
| 1.85% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.69% | `python` | `tuple_dealloc` | memory |
| 1.57% | `python` | `deduce_unreachable` | gc |
| 1.37% | `python` | `gc_collect_region.isra.0` | gc |
| 1.25% | `python` | `visit_decref` | gc |
| 1.16% | `python` | `PyDict_GetItemRef` | dict |
| 1.15% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 1.12% | `python` | `PyObject_SetAttr` | dynamic |
| 1.06% | `python` | `intern_common.part.0` | str |
| 0.91% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.89% | `python` | `dict_dealloc` | memory |
| 0.79% | `python` | `visit_reachable` | gc |
| 0.78% | `python` | `_PyCode_New` | interpreter |
| 0.69% | `python` | `list_dealloc` | memory |
| 0.67% | `python` | `r_object` | import |
| 0.64% | `libc-2.31.so` | `__memcpy_avx_unaligned_erms` | libc |
| 0.63% | `python` | `find_name_in_mro` | lookup |
| 0.61% | `python` | `insertdict` | dict |
| 0.61% | `libpthread-2.31.so` | `__pthread_mutex_lock` | library |
| 0.52% | `libpthread-2.31.so` | `pthread_mutex_unlock` | library |
| 0.52% | `python` | `PyType_GenericAlloc` | memory |
| 0.51% | `python` | `subtype_dealloc` | memory |
| 0.48% | `libsqlite3.so.0.8.6` | `sqlite3_reset` | library |
| 0.47% | `python` | `sre_ucs1_match` | library |
| 0.44% | `python` | `visit_add_to_container` | gc |
| 0.44% | `python` | `siphash13` | str |
| 0.44% | `python` | `_Py_type_getattro` | lookup |
| 0.43% | `python` | `PyUnicode_FromKindAndData` | str |
| 0.42% | `python` | `unicode_dealloc` | memory |
| 0.41% | `python` | `_PyObject_GetMethod` | dynamic |
| 0.41% | `python` | `_PyTuple_FromStackRefSteal` | tuple |
| 0.40% | `python` | `_PyFunction_Vectorcall` | calls |
| 0.40% | `python` | `method_dealloc` | memory |
| 0.39% | `python` | `slot_tp_init` | unknown |
| 0.39% | `python` | `PyDict_SetItem` | dict |
| 0.39% | `python` | `dictresize` | dict |
| 0.38% | `python` | `PyFunction_NewWithQualName` | memory |
| 0.35% | `python` | `insert_to_emptydict` | dict |
| 0.34% | `libsqlite3.so.0.8.6` | `sqlite3_exec` | library |
| 0.33% | `python` | `_PyObject_MakeTpCall` | dynamic |
| 0.33% | `python` | `PyObject_Vectorcall` | dynamic |
| 0.32% | `python` | `PyObject_IsTrue` | dynamic |
| 0.32% | `python` | `PyMem_Free` | memory |
| 0.32% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.30% | `libsqlite3.so.0.8.6` | `sqlite3_randomness` | library |
| 0.30% | `python` | `PyObject_GC_Del` | gc |
| 0.30% | `python` | `dict_traverse` | gc |
| 0.30% | `python` | `code_dealloc` | memory |
| 0.30% | `libc-2.31.so` | `__libc_malloc` | libc |
| 0.29% | `python` | `type_ready` | dynamic |
| 0.28% | `python` | `dict_merge` | dict |
| 0.26% | `python` | `object_new` | memory |
| 0.25% | `python` | `list_iter` | list |

## sqlglot

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 22.69% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 12.74% | `[JIT]` | `jit` | jit |
| 4.68% | `python` | `object_isinstance` | dynamic |
| 2.49% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 2.42% | `python` | `tuple_dealloc` | memory |
| 1.52% | `python` | `method_get` | dynamic |
| 1.45% | `python` | `type_new` | memory |
| 1.34% | `python` | `dictiter_iternextitem` | dict |
| 1.31% | `python` | `meth_dealloc` | memory |
| 1.23% | `python` | `PyObject_IsInstance` | dynamic |
| 1.07% | `python` | `PyFunction_NewWithQualName` | memory |
| 1.04% | `python` | `_Py_MakeCoro` | unknown |
| 1.00% | `python` | `_PyTuple_FromStackRefSteal` | tuple |
| 0.87% | `python` | `_PyType_LookupRef` | lookup |
| 0.84% | `python` | `gen_dealloc` | memory |
| 0.82% | `python` | `dictiter_dealloc` | memory |
| 0.81% | `python` | `deduce_unreachable` | gc |
| 0.79% | `python` | `dict_items` | dict |
| 0.78% | `python` | `visit_decref` | gc |
| 0.76% | `python` | `intern_common.part.0` | str |
| 0.75% | `python` | `slot_tp_hash` | unknown |
| 0.74% | `python` | `list_dealloc` | memory |
| 0.72% | `python` | `gc_collect_region.isra.0` | gc |
| 0.68% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.66% | `python` | `_PyCode_New` | interpreter |
| 0.65% | `python` | `getset_get` | dynamic |
| 0.63% | `python` | `siphash13` | str |
| 0.61% | `python` | `dictview_dealloc` | memory |
| 0.60% | `python` | `insert_to_emptydict` | dict |
| 0.55% | `python` | `dictitems_iter` | unknown |
| 0.53% | `python` | `dict_get` | dict |
| 0.53% | `python` | `func_dealloc` | memory |
| 0.50% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.50% | `python` | `PyTuple_Pack` | tuple |
| 0.49% | `python` | `dict_dealloc` | memory |
| 0.49% | `python` | `r_object` | import |
| 0.48% | `python` | `unicode_dealloc` | memory |
| 0.46% | `python` | `listiter_dealloc` | memory |
| 0.44% | `libc-2.31.so` | `__memcpy_avx_unaligned_erms` | libc |
| 0.43% | `python` | `PyObject_GetAttr` | dynamic |
| 0.43% | `python` | `list_iter` | list |
| 0.43% | `python` | `_PyObject_Calloc` | memory |
| 0.43% | `python` | `uop_optimize` | compiler |
| 0.42% | `python` | `visit_reachable` | gc |
| 0.41% | `python` | `find_name_in_mro` | lookup |
| 0.40% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 0.39% | `python` | `slot_tp_richcompare` | dynamic |
| 0.38% | `python` | `PyObject_CallOneArg` | dynamic |
| 0.37% | `python` | `_PyLong_New` | memory |
| 0.35% | `python` | `_PyFunction_Vectorcall` | calls |
| 0.35% | `python` | `insertdict` | dict |
| 0.35% | `python` | `cfunction_vectorcall_O` | calls |
| 0.34% | `python` | `tuple_hash` | tuple |
| 0.34% | `python` | `PyUnicode_FromKindAndData` | str |
| 0.33% | `python` | `_PyObject_GC_NewVar` | gc |
| 0.32% | `python` | `PyUnicode_New` | memory |
| 0.31% | `python` | `PyObject_IsTrue` | dynamic |
| 0.31% | `python` | `_PyObject_GetMethod` | dynamic |
| 0.31% | `python` | `PyObject_GetIter` | dynamic |
| 0.30% | `python` | `_PyUnicode_JoinArray` | str |
| 0.28% | `python` | `_PyObject_Malloc` | memory |
| 0.27% | `python` | `long_dealloc` | memory |
| 0.27% | `python` | `set_vectorcall` | miscobj |
| 0.26% | `python` | `_Py_Dealloc` | memory |
| 0.26% | `python` | `PyDict_GetItemRef` | dict |

## sqlglot_optimize

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 19.98% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 13.75% | `[JIT]` | `jit` | jit |
| 5.24% | `python` | `object_isinstance` | dynamic |
| 2.28% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 2.13% | `python` | `tuple_dealloc` | memory |
| 1.47% | `python` | `method_get` | dynamic |
| 1.46% | `python` | `dictiter_iternextitem` | dict |
| 1.45% | `python` | `type_new` | memory |
| 1.45% | `python` | `meth_dealloc` | memory |
| 1.20% | `python` | `PyObject_IsInstance` | dynamic |
| 1.06% | `python` | `deduce_unreachable` | gc |
| 1.03% | `python` | `PyObject_GetAttr` | dynamic |
| 1.00% | `python` | `list_dealloc` | memory |
| 0.91% | `python` | `_PyTuple_FromStackRefSteal` | tuple |
| 0.83% | `python` | `gc_collect_region.isra.0` | gc |
| 0.81% | `python` | `_PyType_LookupRef` | lookup |
| 0.80% | `python` | `PyFunction_NewWithQualName` | memory |
| 0.79% | `python` | `visit_decref` | gc |
| 0.76% | `python` | `intern_common.part.0` | str |
| 0.70% | `python` | `getset_get` | dynamic |
| 0.69% | `python` | `_PyCode_New` | interpreter |
| 0.65% | `python` | `dict_get` | dict |
| 0.65% | `python` | `uop_optimize` | compiler |
| 0.60% | `python` | `dictiter_dealloc` | memory |
| 0.60% | `python` | `dict_items` | dict |
| 0.58% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.57% | `python` | `slot_tp_hash` | unknown |
| 0.56% | `python` | `r_object` | import |
| 0.55% | `python` | `visit_reachable` | gc |
| 0.55% | `python` | `siphash13` | str |
| 0.53% | `python` | `listiter_dealloc` | memory |
| 0.51% | `python` | `dict_dealloc` | memory |
| 0.51% | `python` | `member_get` | unknown |
| 0.51% | `python` | `insertdict` | dict |
| 0.50% | `python` | `list_iter` | list |
| 0.49% | `python` | `tuple_hash` | tuple |
| 0.49% | `python` | `dictview_dealloc` | memory |
| 0.49% | `python` | `_Py_MakeCoro` | unknown |
| 0.48% | `python` | `insert_to_emptydict` | dict |
| 0.48% | `python` | `unicode_dealloc` | memory |
| 0.47% | `python` | `find_name_in_mro` | lookup |
| 0.46% | `libc-2.31.so` | `__memcpy_avx_unaligned_erms` | libc |
| 0.45% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.45% | `python` | `func_dealloc` | memory |
| 0.44% | `python` | `dictitems_iter` | unknown |
| 0.41% | `python` | `gen_dealloc` | memory |
| 0.41% | `python` | `_PyObject_Calloc` | memory |
| 0.39% | `python` | `_PyFunction_Vectorcall` | calls |
| 0.38% | `python` | `_PyUnicode_JoinArray` | str |
| 0.38% | `python` | `PyObject_CallOneArg` | dynamic |
| 0.36% | `python` | `PyUnicode_FromKindAndData` | str |
| 0.36% | `python` | `_PyLong_New` | memory |
| 0.36% | `python` | `PyTuple_Pack` | tuple |
| 0.35% | `python` | `long_dealloc` | memory |
| 0.33% | `python` | `_PyObject_Malloc` | memory |
| 0.33% | `python` | `PyDict_GetItemRef` | dict |
| 0.32% | `python` | `PyList_New` | memory |
| 0.32% | `python` | `PyObject_IsTrue` | dynamic |
| 0.30% | `python` | `cfunction_vectorcall_O` | calls |
| 0.29% | `python` | `PyObject_SetAttr` | dynamic |
| 0.27% | `python` | `PyObject_GetIter` | dynamic |
| 0.26% | `python` | `PyObject_GC_Del` | gc |
| 0.25% | `python` | `_PyObject_GC_New` | gc |
| 0.25% | `python` | `object_recursive_isinstance.part.0` | dynamic |

## sqlglot_parse

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 25.55% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 22.27% | `[JIT]` | `jit` | jit |
| 3.34% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.59% | `python` | `PyObject_GetAttr` | dynamic |
| 1.55% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 1.50% | `python` | `PyDict_Contains` | dict |
| 1.35% | `python` | `deduce_unreachable` | gc |
| 1.31% | `python` | `_Py_type_getattro` | lookup |
| 1.21% | `python` | `gc_collect_region.isra.0` | gc |
| 1.05% | `python` | `type_new` | memory |
| 0.96% | `python` | `visit_decref` | gc |
| 0.78% | `python` | `dict_get` | dict |
| 0.76% | `python` | `long_dealloc` | memory |
| 0.73% | `python` | `_PyFunction_Vectorcall` | calls |
| 0.72% | `python` | `_PyLong_Add` | int |
| 0.72% | `python` | `slot_tp_hash` | unknown |
| 0.71% | `python` | `object_isinstance` | dynamic |
| 0.70% | `python` | `PyObject_SetAttr` | dynamic |
| 0.69% | `python` | `tuple_dealloc` | memory |
| 0.68% | `python` | `PyObject_RichCompare` | dynamic |
| 0.68% | `python` | `dict_dealloc` | memory |
| 0.59% | `python` | `intern_common.part.0` | str |
| 0.56% | `python` | `find_name_in_mro` | lookup |
| 0.53% | `python` | `object_new` | memory |
| 0.51% | `python` | `slot_tp_init` | unknown |
| 0.51% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.49% | `python` | `dictiter_iternextitem` | dict |
| 0.49% | `python` | `insert_to_emptydict` | dict |
| 0.49% | `python` | `unicode_dealloc` | memory |
| 0.47% | `python` | `visit_reachable` | gc |
| 0.45% | `python` | `_PyCode_New` | interpreter |
| 0.45% | `python` | `PyDict_SetItem` | dict |
| 0.43% | `python` | `_PyLong_New` | memory |
| 0.42% | `python` | `_PyObject_GC_New` | gc |
| 0.40% | `python` | `subtype_traverse` | gc |
| 0.38% | `python` | `PyObject_GC_Del` | gc |
| 0.38% | `libc-2.31.so` | `__memcpy_avx_unaligned_erms` | libc |
| 0.37% | `python` | `siphash13` | str |
| 0.37% | `python` | `r_object` | import |
| 0.35% | `python` | `_PyLong_Subtract` | int |
| 0.33% | `python` | `dict_traverse` | gc |
| 0.32% | `python` | `clear_slots` | unknown |
| 0.32% | `python` | `dictiter_dealloc` | memory |
| 0.31% | `python` | `meth_dealloc` | memory |
| 0.31% | `python` | `PyDict_GetItemRef` | dict |
| 0.31% | `python` | `PyUnicode_FromKindAndData` | str |
| 0.30% | `python` | `PyUnicode_New` | memory |
| 0.29% | `python` | `method_get` | dynamic |
| 0.29% | `python` | `PySlice_Unpack` | miscobj |
| 0.28% | `python` | `object_richcompare` | dynamic |
| 0.27% | `python` | `subtype_dealloc` | memory |
| 0.26% | `python` | `dict_merge` | dict |
| 0.25% | `python` | `list_dealloc` | memory |

## sqlglot_transpile

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 24.22% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 19.11% | `[JIT]` | `jit` | jit |
| 3.26% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.61% | `python` | `PyObject_GetAttr` | dynamic |
| 1.55% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 1.54% | `python` | `type_new` | memory |
| 1.26% | `python` | `deduce_unreachable` | gc |
| 1.22% | `python` | `gc_collect_region.isra.0` | gc |
| 1.12% | `python` | `visit_decref` | gc |
| 1.08% | `python` | `dict_get` | dict |
| 1.05% | `python` | `object_isinstance` | dynamic |
| 1.02% | `python` | `find_name_in_mro` | lookup |
| 1.01% | `python` | `PyDict_Contains` | dict |
| 0.96% | `python` | `_Py_type_getattro` | lookup |
| 0.84% | `python` | `intern_common.part.0` | str |
| 0.76% | `python` | `tuple_dealloc` | memory |
| 0.66% | `python` | `_PyCode_New` | interpreter |
| 0.65% | `python` | `_PyFunction_Vectorcall` | calls |
| 0.65% | `python` | `dict_dealloc` | memory |
| 0.60% | `python` | `unicode_dealloc` | memory |
| 0.58% | `python` | `long_dealloc` | memory |
| 0.58% | `python` | `visit_reachable` | gc |
| 0.54% | `python` | `siphash13` | str |
| 0.54% | `libc-2.31.so` | `__memcpy_avx_unaligned_erms` | libc |
| 0.52% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.52% | `python` | `slot_tp_hash` | unknown |
| 0.51% | `python` | `PyObject_SetAttr` | dynamic |
| 0.51% | `python` | `PyObject_RichCompare` | dynamic |
| 0.48% | `python` | `_PyLong_Add` | int |
| 0.48% | `python` | `r_object` | import |
| 0.46% | `python` | `PyDict_SetItem` | dict |
| 0.43% | `python` | `PyDict_GetItemRef` | dict |
| 0.42% | `python` | `_PyUnicode_JoinArray` | str |
| 0.42% | `python` | `list_dealloc` | memory |
| 0.40% | `python` | `object_new` | memory |
| 0.40% | `python` | `insert_to_emptydict` | dict |
| 0.38% | `python` | `meth_dealloc` | memory |
| 0.37% | `python` | `dictiter_iternextitem` | dict |
| 0.37% | `python` | `_PyObject_GC_New` | gc |
| 0.35% | `python` | `PyUnicode_FromKindAndData` | str |
| 0.35% | `python` | `method_get` | dynamic |
| 0.33% | `python` | `slot_tp_init` | unknown |
| 0.33% | `python` | `method_dealloc` | memory |
| 0.32% | `python` | `subtype_traverse` | gc |
| 0.32% | `python` | `func_descr_get` | unknown |
| 0.32% | `python` | `PyObject_GC_Del` | gc |
| 0.31% | `python` | `insertdict` | dict |
| 0.31% | `python` | `subtype_dealloc` | memory |
| 0.31% | `python` | `dict_traverse` | gc |
| 0.30% | `python` | `uop_optimize` | compiler |
| 0.29% | `python` | `PyObject_IsInstance` | dynamic |
| 0.29% | `python` | `_PyLong_New` | memory |
| 0.29% | `python` | `PyObject_IsTrue` | dynamic |
| 0.26% | `python` | `PyObject_GetOptionalAttr` | dynamic |
| 0.26% | `python` | `_PyType_LookupRef` | lookup |

## sqlite_synth

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 12.55% | `libpthread-2.31.so` | `pthread_mutex_unlock` | library |
| 12.38% | `libpthread-2.31.so` | `__pthread_mutex_lock` | library |
| 5.99% | `python` | `take_gil` | gil |
| 4.98% | `libsqlite3.so.0.8.6` | `sqlite3_reset` | library |
| 4.03% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 2.72% | `[JIT]` | `jit` | jit |
| 2.44% | `libm-2.31.so` | `__cos_fma` | library |
| 1.54% | `libsqlite3.so.0.8.6` | `sqlite3_randomness` | library |
| 1.44% | `python` | `PyEval_SaveThread` | interpreter |
| 1.29% | `python` | `long_dealloc` | memory |
| 1.16% | `libpthread-2.31.so` | `pthread_cond_signal@@GLIBC_2.3.2` | library |
| 1.13% | `python` | `tuple_dealloc` | memory |
| 1.07% | `_sqlite3.cpython-314-x86_64-linux-gnu.so` | `_pysqlite_query_execute` | library |
| 1.01% | `libsqlite3.so.0.8.6` | `sqlite3_value_double` | library |
| 0.89% | `python` | `long_to_decimal_string_internal` | int |
| 0.80% | `libsqlite3.so.0.8.6` | `sqlite3_value_int64` | library |
| 0.80% | `libsqlite3.so.0.8.6` | `sqlite3_preupdate_old` | library |
| 0.79% | `python` | `type_new` | memory |
| 0.78% | `python` | `PyFloat_AsDouble` | float |
| 0.76% | `libsqlite3.so.0.8.6` | `sqlite3_wal_checkpoint` | library |
| 0.70% | `python` | `list_dealloc` | memory |
| 0.70% | `python` | `PyType_GenericAlloc` | memory |
| 0.67% | `libsqlite3.so.0.8.6` | `sqlite3_extended_errcode` | library |
| 0.64% | `libsqlite3.so.0.8.6` | `sqlite3_vtab_config` | library |
| 0.63% | `libc-2.31.so` | `pthread_mutex_lock` | libc |
| 0.59% | `libc-2.31.so` | `_int_free` | libc |
| 0.58% | `python` | `PyFloat_FromDouble` | float |
| 0.58% | `libsqlite3.so.0.8.6` | `sqlite3_enable_shared_cache` | library |
| 0.57% | `python` | `unicode_dealloc` | memory |
| 0.54% | `python` | `_PyObject_MakeTpCall` | dynamic |
| 0.52% | `python` | `PyEval_RestoreThread` | interpreter |
| 0.50% | `libsqlite3.so.0.8.6` | `sqlite3_step` | library |
| 0.48% | `_sqlite3.cpython-314-x86_64-linux-gnu.so` | `pysqlite_cursor_iternext` | library |
| 0.47% | `libc-2.31.so` | `pthread_mutex_unlock` | libc |
| 0.47% | `python` | `PyUnicode_New` | memory |
| 0.47% | `python` | `PyObject_GetAttr` | dynamic |
| 0.46% | `python` | `_PyObject_Malloc` | memory |
| 0.45% | `python` | `object_new` | memory |
| 0.45% | `python` | `bounded_lru_cache_wrapper` | unknown |
| 0.44% | `python` | `unicode_decode_utf8` | str |
| 0.44% | `python` | `intern_common.part.0` | str |
| 0.42% | `python` | `method_vectorcall` | calls |
| 0.42% | `_sqlite3.cpython-314-x86_64-linux-gnu.so` | `pysqlite_cursor_init` | library |
| 0.41% | `libsqlite3.so.0.8.6` | `sqlite3_str_value` | library |
| 0.40% | `python` | `_PyCode_New` | interpreter |
| 0.38% | `python` | `deduce_unreachable` | gc |
| 0.38% | `libsqlite3.so.0.8.6` | `sqlite3_mutex_try` | library |
| 0.37% | `python` | `visit_decref` | gc |
| 0.37% | `python` | `PyTuple_New` | memory |
| 0.37% | `libc-2.31.so` | `__memcpy_avx_unaligned_erms` | libc |
| 0.36% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.36% | `libc-2.31.so` | `__libc_malloc` | libc |
| 0.35% | `python` | `PyList_New` | memory |
| 0.35% | `libsqlite3.so.0.8.6` | `sqlite3_value_pointer` | library |
| 0.34% | `python` | `long_add` | int |
| 0.34% | `python` | `pthread_mutex_lock@plt` | unknown |
| 0.34% | `libsqlite3.so.0.8.6` | `sqlite3_close_v2` | library |
| 0.33% | `python` | `gc_collect_region.isra.0` | gc |
| 0.33% | `python` | `float_dealloc` | memory |
| 0.33% | `python` | `list_iter` | list |
| 0.32% | `python` | `method_dealloc` | memory |
| 0.31% | `libsqlite3.so.0.8.6` | `sqlite3_free` | library |
| 0.30% | `python` | `PyLong_FromLongLong` | int |
| 0.30% | `python` | `listiter_dealloc` | memory |
| 0.30% | `python` | `_Py_dict_lookup` | lookup |
| 0.30% | `python` | `pthread_mutex_unlock@plt` | unknown |
| 0.29% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.29% | `_sqlite3.cpython-314-x86_64-linux-gnu.so` | `pysqlite_connection_execute` | library |
| 0.28% | `libsqlite3.so.0.8.6` | `sqlite3_realloc64` | library |
| 0.28% | `math.cpython-314-x86_64-linux-gnu.so` | `math_cos` | library |
| 0.28% | `python` | `PyLong_FromLong` | int |
| 0.28% | `_sqlite3.cpython-314-x86_64-linux-gnu.so` | `bind_param.isra.0` | library |
| 0.27% | `python` | `r_object` | import |
| 0.27% | `python` | `PyObject_CallOneArg` | dynamic |
| 0.27% | `python` | `func_descr_get` | unknown |
| 0.27% | `_sqlite3.cpython-314-x86_64-linux-gnu.so` | `func_callback` | library |
| 0.26% | `libsqlite3.so.0.8.6` | `sqlite3_db_config` | library |
| 0.25% | `python` | `_Py_Dealloc` | memory |

## sympy

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 20.52% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 10.45% | `[JIT]` | `jit` | jit |
| 2.20% | `python` | `tuple_dealloc` | memory |
| 2.17% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.27% | `python` | `PyDict_GetItemRef` | dict |
| 1.22% | `python` | `PyObject_GetAttr` | dynamic |
| 1.21% | `python` | `deduce_unreachable` | gc |
| 1.16% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 1.14% | `python` | `type_new` | memory |
| 1.10% | `python` | `visit_decref` | gc |
| 1.04% | `python` | `gc_collect_region.isra.0` | gc |
| 0.95% | `python` | `PyDict_SetItem` | dict |
| 0.93% | `python` | `intern_common.part.0` | str |
| 0.92% | `python` | `find_name_in_mro` | lookup |
| 0.92% | `python` | `_Py_type_getattro` | lookup |
| 0.88% | `python` | `PyObject_RichCompareBool` | dynamic |
| 0.82% | `python` | `object_isinstance` | dynamic |
| 0.80% | `python` | `_Py_dict_lookup` | lookup |
| 0.78% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.76% | `python` | `_PyCode_New` | interpreter |
| 0.76% | `python` | `visit_reachable` | gc |
| 0.73% | `python` | `slot_tp_richcompare` | dynamic |
| 0.70% | `python` | `dict_dealloc` | memory |
| 0.68% | `python` | `method_get` | dynamic |
| 0.68% | `python` | `_PyFunction_Vectorcall` | calls |
| 0.65% | `python` | `list_dealloc` | memory |
| 0.64% | `python` | `meth_dealloc` | memory |
| 0.62% | `python` | `_PyObject_GenericGetAttrWithDict` | dynamic |
| 0.56% | `python` | `PyFunction_NewWithQualName` | memory |
| 0.54% | `python` | `_PyObject_MakeTpCall` | dynamic |
| 0.53% | `libc-2.31.so` | `__memcpy_avx_unaligned_erms` | libc |
| 0.53% | `python` | `r_object` | import |
| 0.49% | `python` | `dict_merge` | dict |
| 0.49% | `python` | `_PyTuple_FromStackRefSteal` | tuple |
| 0.48% | `python` | `dictresize` | dict |
| 0.48% | `python` | `PyUnicode_RichCompare` | str |
| 0.47% | `python` | `setiter_iternext` | miscobj |
| 0.47% | `python` | `PyObject_GetOptionalAttr` | dynamic |
| 0.46% | `python` | `dictiter_iternextitem` | dict |
| 0.41% | `python` | `dict_subscript` | dict |
| 0.39% | `python` | `func_dealloc` | memory |
| 0.38% | `python` | `slot_tp_hash` | unknown |
| 0.38% | `python` | `tuple_iter` | tuple |
| 0.37% | `python` | `_Py_slot_tp_getattr_hook` | unknown |
| 0.37% | `python` | `siphash13` | str |
| 0.37% | `python` | `PyUnicode_FromKindAndData` | str |
| 0.36% | `python` | `insertdict` | dict |
| 0.36% | `python` | `wrapperdescr_call` | unknown |
| 0.35% | `python` | `tupleiter_dealloc` | memory |
| 0.34% | `python` | `insert_to_emptydict` | dict |
| 0.33% | `python` | `PyMem_Free` | memory |
| 0.32% | `python` | `_PyStack_UnpackDict` | unknown |
| 0.32% | `libc-2.31.so` | `__memcmp_avx2_movbe` | libc |
| 0.30% | `python` | `PyObject_IsInstance` | dynamic |
| 0.30% | `python` | `dict_get` | dict |
| 0.28% | `python` | `dict_traverse` | gc |
| 0.28% | `python` | `PyDict_Contains` | dict |
| 0.28% | `python` | `unicode_dealloc` | memory |
| 0.28% | `python` | `_Py_Dealloc` | memory |
| 0.28% | `python` | `_PyType_LookupRef` | lookup |
| 0.26% | `python` | `code_dealloc` | memory |
| 0.26% | `python` | `PyObject_CallOneArg` | dynamic |
| 0.26% | `python` | `tuple_hash` | tuple |
| 0.25% | `python` | `visit_add_to_container` | gc |
| 0.25% | `python` | `_PyObject_Malloc` | memory |

## telco

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 9.64% | `[JIT]` | `jit` | jit |
| 4.39% | `python` | `PyObject_GC_Del` | gc |
| 4.24% | `python` | `_PyObject_GC_New` | gc |
| 2.67% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 2.50% | `_decimal.cpython-314-x86_64-linux-gnu.so` | `nm_mpd_qadd` | library |
| 2.28% | `_decimal.cpython-314-x86_64-linux-gnu.so` | `nm_mpd_qmul` | library |
| 2.21% | `_decimal.cpython-314-x86_64-linux-gnu.so` | `_mpd_qaddsub` | library |
| 1.95% | `_decimal.cpython-314-x86_64-linux-gnu.so` | `_mpd_baseshiftr` | library |
| 1.85% | `python` | `method_get` | dynamic |
| 1.83% | `python` | `tuple_dealloc` | memory |
| 1.78% | `python` | `PyObject_GetAttr` | dynamic |
| 1.74% | `python` | `meth_dealloc` | memory |
| 1.50% | `_decimal.cpython-314-x86_64-linux-gnu.so` | `dec_mpd_qquantize` | library |
| 1.47% | `python` | `PyObject_GC_Track` | gc |
| 1.45% | `_decimal.cpython-314-x86_64-linux-gnu.so` | `mpd_qshiftr` | library |
| 1.44% | `_decimal.cpython-314-x86_64-linux-gnu.so` | `_mpd_qmul` | library |
| 1.41% | `_decimal.cpython-314-x86_64-linux-gnu.so` | `find_state_left_or_right` | library |
| 1.39% | `python` | `vgetargskeywords.constprop.0` | calls |
| 1.39% | `python` | `PyContextVar_Get` | unknown |
| 1.34% | `_decimal.cpython-314-x86_64-linux-gnu.so` | `mpd_qfinalize` | library |
| 1.30% | `_decimal.cpython-314-x86_64-linux-gnu.so` | `convert_op` | library |
| 1.19% | `python` | `PyDict_GetItemRef` | dict |
| 1.10% | `python` | `vgetargs1_impl` | calls |
| 1.08% | `python` | `type_new` | memory |
| 1.08% | `python` | `_PyArg_UnpackKeywordsWithVararg` | calls |
| 1.01% | `python` | `PyObject_GC_UnTrack` | gc |
| 1.01% | `python` | `PyUnicode_New` | memory |
| 0.90% | `python` | `PyObject_GenericGetAttr` | dynamic |
| 0.87% | `_decimal.cpython-314-x86_64-linux-gnu.so` | `dec_dealloc` | library |
| 0.86% | `_decimal.cpython-314-x86_64-linux-gnu.so` | `mpd_qquantize` | library |
| 0.82% | `python` | `_PyObject_MakeTpCall` | dynamic |
| 0.82% | `python` | `_io_BytesIO_read` | unknown |
| 0.72% | `python` | `method_vectorcall_VARARGS_KEYWORDS` | calls |
| 0.69% | `_decimal.cpython-314-x86_64-linux-gnu.so` | `PyDecType_FromLongExact` | library |
| 0.68% | `python` | `find_keyword` | unknown |
| 0.68% | `python` | `PyTuple_New` | memory |
| 0.64% | `python` | `_Py_Dealloc` | memory |
| 0.64% | `python` | `deduce_unreachable` | gc |
| 0.63% | `libc-2.31.so` | `__strlen_avx2` | libc |
| 0.63% | `python` | `as_ucs4` | unknown |
| 0.63% | `_decimal.cpython-314-x86_64-linux-gnu.so` | `dec_addstatus` | library |
| 0.61% | `python` | `intern_common.part.0` | str |
| 0.59% | `python` | `unicode_dealloc` | memory |
| 0.56% | `_decimal.cpython-314-x86_64-linux-gnu.so` | `PyDecType_New.isra.0` | library |
| 0.53% | `python` | `_PyCode_New` | interpreter |
| 0.53% | `python` | `gc_collect_region.isra.0` | gc |
| 0.53% | `python` | `PyNumber_Multiply` | dynamic |
| 0.53% | `python` | `PyType_GetBaseByToken` | unknown |
| 0.53% | `python` | `PyObject_Vectorcall` | dynamic |
| 0.52% | `python` | `long_dealloc` | memory |
| 0.52% | `_decimal.cpython-314-x86_64-linux-gnu.so` | `dec_str` | library |
| 0.52% | `libc-2.31.so` | `__strchr_avx2` | libc |
| 0.52% | `python` | `visit_decref` | gc |
| 0.51% | `python` | `PyMem_Malloc` | memory |
| 0.50% | `_struct.cpython-314-x86_64-linux-gnu.so` | `unpack` | library |
| 0.50% | `python` | `PyMem_Free` | memory |
| 0.45% | `_decimal.cpython-314-x86_64-linux-gnu.so` | `current_context` | library |
| 0.43% | `_decimal.cpython-314-x86_64-linux-gnu.so` | `word_to_string` | library |
| 0.43% | `python` | `binary_op1` | unknown |
| 0.43% | `python` | `object_dealloc` | memory |
| 0.43% | `python` | `write_str` | unknown |
| 0.42% | `python` | `PyLong_FromLong` | int |
| 0.42% | `python` | `PyObject_Str` | dynamic |
| 0.40% | `python` | `r_object` | import |
| 0.38% | `libc-2.31.so` | `__memcmp_avx2_movbe` | libc |
| 0.36% | `python` | `PyFile_WriteObject` | unknown |
| 0.35% | `_decimal.cpython-314-x86_64-linux-gnu.so` | `ctx_mpd_qquantize` | library |
| 0.34% | `python` | `PyObject_RichCompare` | dynamic |
| 0.34% | `_decimal.cpython-314-x86_64-linux-gnu.so` | `mpd_qadd` | library |
| 0.33% | `_decimal.cpython-314-x86_64-linux-gnu.so` | `_mpd_to_string` | library |
| 0.33% | `python` | `cfunction_vectorcall_O` | calls |
| 0.33% | `libc-2.31.so` | `__memcpy_avx_unaligned_erms` | libc |
| 0.32% | `python` | `visit_reachable` | gc |
| 0.32% | `python` | `PyUnicode_CompareWithASCIIString` | str |
| 0.31% | `python` | `PyLong_FromUnsignedLongLong` | int |
| 0.30% | `python` | `PyUnicode_FromKindAndData` | str |
| 0.30% | `python` | `builtin_print` | unknown |
| 0.30% | `python` | `PyObject_CallOneArg` | dynamic |
| 0.29% | `python` | `PyNumber_InPlaceAdd` | dynamic |
| 0.28% | `python` | `PyType_GetModuleByDef` | dynamic |
| 0.28% | `_decimal.cpython-314-x86_64-linux-gnu.so` | `_mpd_rnd_incr.isra.0` | library |
| 0.26% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.26% | `python` | `siphash13` | str |

## thrift

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 23.19% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 2.64% | `python` | `PyDict_GetItemRef` | dict |
| 2.56% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 2.55% | `fastbinary.cpython-314-x86_64-linux-gnu.so` | `apache::thrift::py::ProtocolBase<apache::thrift::py::BinaryProtocol>::encodeValue` | library |
| 2.38% | `python` | `subtype_dealloc` | memory |
| 2.20% | `[JIT]` | `jit` | jit |
| 2.04% | `python` | `PyDict_SetItem` | dict |
| 1.96% | `python` | `PyObject_GetAttr` | dynamic |
| 1.91% | `python` | `insert_to_emptydict` | dict |
| 1.88% | `python` | `_PyFunction_Vectorcall` | calls |
| 1.79% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 1.66% | `python` | `dict_dealloc` | memory |
| 1.46% | `python` | `_PyStack_UnpackDict` | unknown |
| 1.43% | `python` | `tuple_dealloc` | memory |
| 1.42% | `python` | `object_new` | memory |
| 1.20% | `python` | `slot_tp_init` | unknown |
| 1.15% | `python` | `PyObject_RichCompareBool` | dynamic |
| 1.01% | `python` | `insertdict` | dict |
| 1.00% | `fastbinary.cpython-314-x86_64-linux-gnu.so` | `apache::thrift::py::ProtocolBase<apache::thrift::py::BinaryProtocol>::decodeValue` | library |
| 0.98% | `python` | `PyType_GenericAlloc` | memory |
| 0.97% | `python` | `PyObject_GC_Del` | gc |
| 0.90% | `python` | `unicode_from_format` | str |
| 0.90% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.86% | `python` | `PyMem_Free` | memory |
| 0.86% | `python` | `_PySuper_Lookup` | dynamic |
| 0.85% | `python` | `PyLong_AsLong` | int |
| 0.83% | `python` | `PyUnicode_DecodeUTF8` | str |
| 0.83% | `python` | `_PyObject_MakeTpCall` | dynamic |
| 0.80% | `python` | `PyErr_Format` | exceptions |
| 0.78% | `fastbinary.cpython-314-x86_64-linux-gnu.so` | `apache::thrift::py::ProtocolBase<apache::thrift::py::BinaryProtocol>::readStruct` | library |
| 0.78% | `python` | `PyTuple_Size` | tuple |
| 0.77% | `python` | `_PyObject_GenericGetAttrWithDict` | dynamic |
| 0.75% | `python` | `type_new` | memory |
| 0.72% | `fastbinary.cpython-314-x86_64-linux-gnu.so` | `apache::thrift::py::ProtocolBase<apache::thrift::py::BinaryProtocol>::readBytes` | library |
| 0.72% | `python` | `PyObject_GetOptionalAttr` | dynamic |
| 0.68% | `python` | `list_dealloc` | memory |
| 0.67% | `python` | `dictresize` | dict |
| 0.60% | `python` | `unicode_dealloc` | memory |
| 0.60% | `python` | `PyUnicode_RichCompare` | str |
| 0.58% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.55% | `fastbinary.cpython-314-x86_64-linux-gnu.so` | `apache::thrift::py::BinaryProtocol::readFieldBegin` | library |
| 0.52% | `python` | `dict_merge` | dict |
| 0.51% | `libc-2.31.so` | `__memcpy_avx_unaligned_erms` | libc |
| 0.50% | `python` | `unicode_encode_utf8` | str |
| 0.49% | `python` | `method_dealloc` | memory |
| 0.49% | `python` | `deduce_unreachable` | gc |
| 0.45% | `python` | `object_dealloc` | memory |
| 0.44% | `python` | `intern_common.part.0` | str |
| 0.43% | `python` | `siphash13` | str |
| 0.43% | `python` | `tuple_iter` | tuple |
| 0.42% | `python` | `vgetargs1_impl` | calls |
| 0.38% | `python` | `visit_decref` | gc |
| 0.38% | `python` | `PyBytes_FromStringAndSize` | str |
| 0.38% | `python` | `_PyCode_New` | interpreter |
| 0.37% | `fastbinary.cpython-314-x86_64-linux-gnu.so` | `apache::thrift::py::parse_struct_item_spec` | library |
| 0.37% | `python` | `PyObject_SetAttr` | dynamic |
| 0.36% | `python` | `func_descr_get` | unknown |
| 0.35% | `python` | `BaseException_vectorcall` | exceptions |
| 0.35% | `python` | `gc_collect_region.isra.0` | gc |
| 0.34% | `python` | `_Py_dict_lookup` | lookup |
| 0.33% | `python` | `tupleiter_dealloc` | memory |
| 0.33% | `libc-2.31.so` | `__libc_malloc` | libc |
| 0.32% | `python` | `_PyObject_Calloc` | memory |
| 0.32% | `python` | `PyDict_New` | memory |
| 0.29% | `python` | `PyObject_Call` | dynamic |
| 0.29% | `python` | `unicode_fromformat_write_utf8` | str |
| 0.29% | `libc-2.31.so` | `__strlen_avx2` | libc |
| 0.27% | `python` | `r_object` | import |
| 0.27% | `python` | `type_call` | dynamic |
| 0.27% | `python` | `_Py_module_getattro` | unknown |
| 0.27% | `python` | `_PyEval_ImportName` | interpreter |
| 0.26% | `python` | `dict_get` | dict |
| 0.26% | `python` | `BaseException_dealloc` | memory |
| 0.26% | `python` | `PyImport_ImportModuleLevelObject` | import |
| 0.25% | `fastbinary.cpython-314-x86_64-linux-gnu.so` | `apache::thrift::py::parse_struct_args` | library |
| 0.25% | `python` | `visit_reachable` | gc |

## tomli_loads

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 22.03% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 21.60% | `[JIT]` | `jit` | jit |
| 6.20% | `python` | `_PyLong_Add` | int |
| 5.62% | `python` | `long_dealloc` | memory |
| 5.41% | `python` | `_PySet_Contains` | miscobj |
| 2.42% | `python` | `PyDict_GetItemRef` | dict |
| 2.29% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 2.23% | `python` | `PyDict_Contains` | dict |
| 2.12% | `python` | `_PyUnicode_Equal` | str |
| 1.21% | `libc-2.31.so` | `__memcmp_avx2_movbe` | libc |
| 1.15% | `python` | `_PyIncrementalNewlineDecoder_decode.cold` | memory |
| 1.03% | `python` | `tuple_dealloc` | memory |
| 0.93% | `python` | `object_isinstance` | dynamic |
| 0.89% | `python` | `PyObject_GetAttr` | dynamic |
| 0.89% | `python` | `long_add` | int |
| 0.86% | `libc-2.31.so` | `__memcpy_avx_unaligned_erms` | libc |
| 0.82% | `python` | `set_contains_lock_held` | miscobj |
| 0.82% | `python` | `_PyTuple_FromStackRefSteal` | tuple |
| 0.71% | `python` | `PyUnicode_New` | memory |
| 0.71% | `python` | `PySlice_Unpack` | miscobj |
| 0.67% | `python` | `_PyIncrementalNewlineDecoder_decode` | memory |
| 0.63% | `python` | `PyFunction_NewWithQualName` | memory |
| 0.59% | `python` | `sre_ucs4_match` | library |
| 0.53% | `python` | `siphash13` | str |
| 0.46% | `python` | `cell_dealloc` | memory |
| 0.46% | `python` | `tupleiter_dealloc` | memory |
| 0.44% | `python` | `_PyUnicode_FromUCS4` | str |
| 0.43% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.42% | `python` | `ucs4lib_fastsearch` | unknown |
| 0.41% | `python` | `ucs4lib_utf8_decode` | unknown |
| 0.40% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.37% | `python` | `_PyObject_GC_New` | gc |
| 0.36% | `python` | `tuple_iter` | tuple |
| 0.35% | `python` | `_sre_SRE_Pattern_match` | library |
| 0.35% | `python` | `func_dealloc` | memory |
| 0.34% | `python` | `_Py_MakeCoro` | unknown |
| 0.34% | `python` | `memcmp@plt` | unknown |
| 0.34% | `python` | `unicode_dealloc` | memory |
| 0.33% | `python` | `insertdict` | dict |
| 0.32% | `python` | `ucs4lib_find_max_char` | unknown |
| 0.32% | `python` | `tuple_subscript` | tuple |
| 0.31% | `[kernel.kallsyms]` | `clear_page_erms` | kernel |
| 0.30% | `python` | `_Py_Dealloc` | memory |
| 0.30% | `[kernel.kallsyms]` | `native_irq_return_iret` | kernel |
| 0.28% | `python` | `PyObject_GetItem` | dynamic |
| 0.27% | `python` | `dict_dealloc` | memory |
| 0.26% | `python` | `range_vectorcall` | miscobj |

## typing_runtime_protocols

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 23.24% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 9.61% | `[JIT]` | `jit` | jit |
| 4.15% | `python` | `tuple_dealloc` | memory |
| 3.99% | `python` | `_PyObject_MakeTpCall` | dynamic |
| 3.22% | `python` | `get_or_create_weakref` | unknown |
| 2.08% | `python` | `PyArg_UnpackTuple` | calls |
| 1.96% | `python` | `_Py_dict_lookup` | lookup |
| 1.86% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.69% | `python` | `tuple_iter` | tuple |
| 1.49% | `python` | `tupleiter_dealloc` | memory |
| 1.42% | `python` | `list_dealloc` | memory |
| 1.24% | `python` | `_Py_type_getattro` | lookup |
| 1.22% | `python` | `_PyObject_Malloc` | memory |
| 1.20% | `python` | `PyDict_Contains` | dict |
| 1.07% | `python` | `PyTraceBack_Here` | exceptions |
| 1.07% | `python` | `PySequence_Tuple` | dynamic |
| 0.97% | `python` | `PyObject_GetAttr` | dynamic |
| 0.96% | `python` | `PyObject_Vectorcall` | dynamic |
| 0.88% | `python` | `bounded_lru_cache_wrapper` | unknown |
| 0.86% | `python` | `type_new` | memory |
| 0.84% | `python` | `wrap_descr_get` | unknown |
| 0.83% | `python` | `frame_dealloc` | memory |
| 0.80% | `python` | `_PyFrame_MakeAndSetFrameObject` | unknown |
| 0.74% | `python` | `type_dict` | dynamic |
| 0.73% | `python` | `type_call` | dynamic |
| 0.71% | `python` | `PySet_Contains` | miscobj |
| 0.70% | `python` | `tuple_hash` | tuple |
| 0.68% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.66% | `python` | `weakref___new__` | memory |
| 0.63% | `python` | `mappingproxy_dealloc` | memory |
| 0.60% | `python` | `method_dealloc` | memory |
| 0.60% | `python` | `_PyDict_GetItem_KnownHash` | dict |
| 0.58% | `python` | `tuple_contains` | tuple |
| 0.56% | `python` | `weakref_richcompare` | unknown |
| 0.56% | `python` | `_PyObject_Call` | dynamic |
| 0.50% | `python` | `_Py_type_getattro_impl` | dynamic |
| 0.50% | `python` | `PyObject_GetIter` | dynamic |
| 0.47% | `python` | `intern_common.part.0` | str |
| 0.46% | `python` | `deduce_unreachable` | gc |
| 0.45% | `python` | `weakref___init__` | unknown |
| 0.45% | `python` | `tuple_richcompare` | tuple |
| 0.44% | `python` | `visit_decref` | gc |
| 0.44% | `python` | `_PyCode_New` | interpreter |
| 0.43% | `python` | `PyObject_GenericGetAttr` | dynamic |
| 0.41% | `python` | `gc_collect_region.isra.0` | gc |
| 0.41% | `python` | `PyObject_IsInstance` | dynamic |
| 0.40% | `python` | `tb_dealloc` | memory |
| 0.40% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.39% | `python` | `setiter_dealloc` | memory |
| 0.37% | `python` | `PyList_New` | memory |
| 0.37% | `python` | `getset_get` | dynamic |
| 0.36% | `python` | `_PyList_AppendTakeRefListResize` | list |
| 0.36% | `python` | `setiter_iternext` | miscobj |
| 0.35% | `python` | `dict_get` | dict |
| 0.34% | `python` | `lru_cache_make_key` | unknown |
| 0.33% | `python` | `BaseException_new` | memory |
| 0.33% | `python` | `r_object` | import |
| 0.32% | `libc-2.31.so` | `__memcpy_avx_unaligned_erms` | libc |
| 0.31% | `python` | `func_descr_get` | unknown |
| 0.30% | `python` | `wrapperdescr_call` | unknown |
| 0.30% | `python` | `_PyList_FromStackRefSteal` | list |
| 0.29% | `python` | `dict_dealloc` | memory |
| 0.28% | `python` | `visit_reachable` | gc |
| 0.28% | `python` | `AttributeError_init` | exceptions |
| 0.27% | `python` | `set_iter` | miscobj |
| 0.26% | `python` | `PyUnicode_FromKindAndData` | str |
| 0.26% | `python` | `_abc__abc_instancecheck` | unknown |
| 0.26% | `python` | `PyObject_RichCompare` | dynamic |

## unpickle_pure_python

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 39.54% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 14.62% | `[JIT]` | `jit` | jit |
| 3.88% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 2.84% | `python` | `PyDict_GetItemRef` | dict |
| 2.59% | `python` | `_io_BytesIO_read` | unknown |
| 1.87% | `python` | `PyObject_IsTrue` | dynamic |
| 1.49% | `python` | `insertdict` | dict |
| 1.35% | `python` | `unicode_decode_utf8` | str |
| 1.17% | `python` | `bytes_subscript` | str |
| 1.10% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 1.04% | `python` | `unicode_vectorcall` | str |
| 0.99% | `python` | `type_new` | memory |
| 0.87% | `python` | `object_dealloc` | memory |
| 0.73% | `python` | `PyObject_GetItem` | dynamic |
| 0.69% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.67% | `python` | `unicode_dealloc` | memory |
| 0.62% | `python` | `siphash13` | str |
| 0.57% | `python` | `intern_common.part.0` | str |
| 0.55% | `python` | `PyObject_IsInstance` | dynamic |
| 0.54% | `libc-2.31.so` | `__memcpy_avx_unaligned_erms` | libc |
| 0.53% | `python` | `visit_decref` | gc |
| 0.51% | `python` | `_PyCode_New` | interpreter |
| 0.51% | `python` | `deduce_unreachable` | gc |
| 0.49% | `python` | `gc_collect_region.isra.0` | gc |
| 0.46% | `python` | `dictresize` | dict |
| 0.45% | `python` | `list_subscript` | list |
| 0.43% | `python` | `PyMem_Realloc` | memory |
| 0.43% | `python` | `PyObject_Size` | dynamic |
| 0.43% | `python` | `tuple_dealloc` | memory |
| 0.40% | `python` | `PyObject_Hash` | dynamic |
| 0.38% | `python` | `dict_dealloc` | memory |
| 0.37% | `python` | `r_object` | import |
| 0.37% | `python` | `list_dealloc` | memory |
| 0.36% | `python` | `long_hash` | int |
| 0.33% | `python` | `PyObject_GetAttr` | dynamic |
| 0.33% | `python` | `PyUnicode_FromKindAndData` | str |
| 0.32% | `python` | `list_append` | list |
| 0.29% | `python` | `visit_reachable` | gc |
| 0.27% | `python` | `PyLong_FromSsize_t` | int |
| 0.26% | `libc-2.31.so` | `__strlen_avx2` | libc |

## xml_etree

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 12.12% | `[JIT]` | `jit` | jit |
| 6.10% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 3.97% | `python` | `PyObject_GetAttr` | dynamic |
| 3.16% | `pyexpat.cpython-314-x86_64-linux-gnu.so` | `doContent` | library |
| 2.42% | `pyexpat.cpython-314-x86_64-linux-gnu.so` | `PyExpat_XML_Parse` | library |
| 2.03% | `pyexpat.cpython-314-x86_64-linux-gnu.so` | `normal_contentTok` | library |
| 2.01% | `python` | `_io_TextIOWrapper_write` | unknown |
| 1.95% | `python` | `deduce_unreachable` | gc |
| 1.73% | `pyexpat.cpython-314-x86_64-linux-gnu.so` | `hash` | library |
| 1.62% | `python` | `visit_decref` | gc |
| 1.62% | `python` | `unicode_dealloc` | memory |
| 1.59% | `pyexpat.cpython-314-x86_64-linux-gnu.so` | `storeAtts` | library |
| 1.59% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.45% | `python` | `visit_reachable` | gc |
| 1.40% | `python` | `_PyObject_GC_New` | gc |
| 1.40% | `python` | `PyUnicode_Concat` | str |
| 1.37% | `python` | `PyObject_VectorcallMethod` | dynamic |
| 1.24% | `python` | `PyUnicode_DecodeUTF8` | str |
| 1.22% | `libc-2.31.so` | `__memcpy_avx_unaligned_erms` | libc |
| 1.18% | `python` | `object_isinstance` | dynamic |
| 1.11% | `python` | `gc_collect_region.isra.0` | gc |
| 1.10% | `python` | `tuple_dealloc` | memory |
| 1.04% | `python` | `_PyFunction_Vectorcall` | calls |
| 1.02% | `python` | `long_to_decimal_string_internal` | int |
| 1.02% | `python` | `PyUnicode_Format` | str |
| 0.99% | `python` | `list_dealloc` | memory |
| 0.96% | `python` | `PyObject_GC_Del` | gc |
| 0.96% | `python` | `PyUnicode_Contains` | str |
| 0.91% | `python` | `type_new` | memory |
| 0.87% | `_elementtree.cpython-314-x86_64-linux-gnu.so` | `elementiter_next` | library |
| 0.80% | `_elementtree.cpython-314-x86_64-linux-gnu.so` | `treebuilder_handle_start` | library |
| 0.79% | `python` | `siphash13` | str |
| 0.76% | `_elementtree.cpython-314-x86_64-linux-gnu.so` | `element_dealloc` | library |
| 0.75% | `python` | `PyDict_GetItemWithError` | dict |
| 0.75% | `python` | `BaseException_vectorcall` | exceptions |
| 0.72% | `python` | `PyBytes_FromStringAndSize` | str |
| 0.71% | `python` | `getset_get` | dynamic |
| 0.71% | `python` | `vgetargs1_impl` | calls |
| 0.70% | `python` | `object_dealloc` | memory |
| 0.65% | `_elementtree.cpython-314-x86_64-linux-gnu.so` | `element_gc_traverse` | library |
| 0.62% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.61% | `_elementtree.cpython-314-x86_64-linux-gnu.so` | `treebuilder_handle_end.isra.0` | library |
| 0.61% | `python` | `visit_add_to_container` | gc |
| 0.58% | `python` | `list_vectorcall` | list |
| 0.50% | `python` | `unicode_decode_utf8` | str |
| 0.48% | `python` | `intern_common.part.0` | str |
| 0.47% | `_elementtree.cpython-314-x86_64-linux-gnu.so` | `expat_data_handler` | library |
| 0.44% | `python` | `_PyObject_MakeTpCall` | dynamic |
| 0.43% | `python` | `_PyCode_New` | interpreter |
| 0.42% | `python` | `stringlib__two_way.lto_priv.1` | str |
| 0.41% | `_elementtree.cpython-314-x86_64-linux-gnu.so` | `Py_XDECREF` | library |
| 0.40% | `python` | `_PyObject_GC_NewVar` | gc |
| 0.40% | `python` | `listiter_dealloc` | memory |
| 0.36% | `python` | `PyDict_GetItemRef` | dict |
| 0.36% | `python` | `PyDict_Contains` | dict |
| 0.35% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.35% | `python` | `tuple_traverse` | gc |
| 0.34% | `python` | `list_iter` | list |
| 0.34% | `python` | `PyList_New` | memory |
| 0.34% | `libc-2.31.so` | `__memcmp_avx2_movbe` | libc |
| 0.33% | `python` | `PySequence_Contains` | dynamic |
| 0.33% | `python` | `PyObject_SetAttr` | dynamic |
| 0.32% | `python` | `_PyErr_SetObject` | exceptions |
| 0.32% | `_elementtree.cpython-314-x86_64-linux-gnu.so` | `element_getitem` | library |
| 0.32% | `python` | `PyList_Append` | list |
| 0.31% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.30% | `python` | `_PyUnicodeWriter_PrepareInternal` | str |
| 0.29% | `python` | `dict_dealloc` | memory |
| 0.29% | `python` | `r_object` | import |
| 0.29% | `python` | `vectorcall_method` | calls |
| 0.28% | `python` | `iter_iternext` | unknown |
| 0.28% | `python` | `PyMem_Realloc` | memory |
| 0.27% | `python` | `_textiowrapper_writeflush` | unknown |
| 0.27% | `python` | `BaseException_dealloc` | memory |
| 0.27% | `libc-2.31.so` | `__strlen_avx2` | libc |
| 0.27% | `python` | `PyTuple_Pack` | tuple |
| 0.27% | `python` | `dict_traverse` | gc |
| 0.26% | `python` | `_Py_Dealloc` | memory |
| 0.25% | `python` | `PyUnicode_FromKindAndData` | str |


## Categories

### interpreter

19.37% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 15.65% | python | _PyEval_EvalFrameDefault |
| 2.03% | python | _PyEval_FrameClearAndPop |
| 0.58% | python | _PyEvalFramePushAndInit |
| 0.48% | python | _PyCode_New |
| 0.10% | python | _PyEval_LoadGlobalStackRef |
| 0.09% | python | _PyFrame_ClearExceptCode |
| 0.09% | python | _PyEval_EvalFrameDefault.cold |
| 0.05% | python | call_instrumentation_vector |
| 0.05% | python | _PyPegen_fill_token |
| 0.03% | python | _PyEval_LoadName |
| 0.03% | python | PyEval_SaveThread |
| 0.02% | python | _PyEval_GetAwaitable |
| 0.02% | python | _PyEval_SliceIndex |
| 0.02% | python | _PyCode_Validate |
| 0.02% | python | _PyPegen_name_token |
| 0.01% | python | PyEval_RestoreThread |
| 0.01% | python | _PyCode_GetCode |
| 0.01% | python | PyEval_GetFrame |
| 0.01% | python | _PyPegen_Parser_Free |
| 0.01% | python | _PyEval_ImportName |
| 0.01% | python | _PyEval_GetFrame |
| 0.01% | python | _PyEval_GetANext |
| 0.00% | python | _PyEval_CheckExceptTypeValid |
| 0.00% | python | _PyPegen_expect_token |
| 0.00% | python | PyEval_EvalCode |

### jit

14.27% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 14.27% | [JIT] | jit |

### gc

11.78% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 2.10% | python | visit_decref |
| 1.99% | python | deduce_unreachable |
| 1.82% | python | visit_reachable |
| 1.66% | python | gc_collect_region.isra.0 |
| 1.17% | python | visit_add_to_container |
| 0.58% | python | dict_traverse |
| 0.36% | python | PyObject_GC_Del |
| 0.35% | python | subtype_traverse |
| 0.28% | python | list_traverse |
| 0.27% | python | _PyObject_GC_New |
| 0.26% | python | _PyObject_GC_NewVar |
| 0.21% | python | _PyGC_Collect |
| 0.13% | python | func_traverse |
| 0.12% | python | tuple_traverse |
| 0.12% | python | gen_traverse |
| 0.09% | python | set_traverse |
| 0.06% | python | type_traverse |
| 0.05% | python | PyObject_GC_UnTrack |
| 0.03% | python | PyObject_GC_Track |
| 0.03% | python | meth_traverse |
| 0.02% | python | context_tp_traverse |
| 0.01% | python | descr_traverse |
| 0.01% | python | gc_traverse |
| 0.01% | python | module_traverse |
| 0.01% | python | PyObject_IS_GC |
| 0.01% | python | method_traverse |
| 0.01% | python | cell_traverse |
| 0.01% | python | executor_traverse |
| 0.00% | python | _PyObject_GC_Resize |
| 0.00% | python | property_traverse |

### memory

10.68% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 0.99% | python | type_new |
| 0.97% | python | tuple_dealloc |
| 0.84% | python | list_dealloc |
| 0.79% | python | long_dealloc |
| 0.56% | python | unicode_dealloc |
| 0.42% | python | dict_dealloc |
| 0.40% | python | gen_dealloc |
| 0.32% | python | subtype_dealloc |
| 0.28% | python | PyMem_Free |
| 0.25% | python | PyFunction_NewWithQualName |
| 0.23% | python | PyUnicode_New |
| 0.23% | python | listiter_dealloc |
| 0.23% | python | _PyLong_New |
| 0.22% | python | PyMem_Malloc |
| 0.22% | python | _Py_Dealloc |
| 0.22% | python | meth_dealloc |
| 0.21% | python | PyType_GenericAlloc |
| 0.19% | python | object_new |
| 0.19% | python | _PyObject_Malloc |
| 0.16% | python | func_dealloc |
| 0.15% | python | PyList_New |
| 0.15% | python | set_dealloc |
| 0.13% | python | object_dealloc |
| 0.13% | python | method_dealloc |
| 0.12% | python | float_dealloc |
| 0.12% | python | code_dealloc |
| 0.09% | python | slice_dealloc |
| 0.09% | python | frame_dealloc |
| 0.09% | python | tupleiter_dealloc |
| 0.08% | python | PyTuple_New |
| 0.07% | python | PyType_GenericNew |
| 0.07% | python | PyMem_Realloc |
| 0.07% | python | BaseException_new |
| 0.06% | python | StopIteration_dealloc |
| 0.06% | python | _PyObject_Calloc |
| 0.06% | python | list_new_prealloc |
| 0.06% | python | memset@plt |
| 0.06% | python | allocate_from_new_pool |
| 0.06% | python | _PyObject_Free |
| 0.05% | python | context_tp_dealloc |
| 0.05% | python | memcpy@plt |
| 0.05% | python | dictiter_dealloc |
| 0.04% | python | zip_new |
| 0.04% | python | PyDict_New |
| 0.04% | python | PySlice_New |
| 0.04% | python | range_dealloc |
| 0.04% | python | cell_dealloc |
| 0.03% | python | tp_new_wrapper |
| 0.03% | python | dictview_dealloc |
| 0.03% | python | BaseException_dealloc |
| 0.03% | python | make_new_set |
| 0.03% | python | tb_dealloc |
| 0.03% | python | async_gen_asend_new |
| 0.03% | python | _PyObject_New |
| 0.03% | python | _Py_NewReference |
| 0.02% | python | async_gen_asend_dealloc |
| 0.02% | python | slot_tp_new |
| 0.02% | python | match_dealloc |
| 0.02% | python | _PyFloat_ExactDealloc |
| 0.02% | python | setiter_dealloc |
| 0.02% | python | zip_dealloc |
| 0.02% | python | _PyAsyncGenValueWrapperNew |
| 0.02% | python | async_gen_wrapped_val_dealloc |
| 0.02% | python | weakref_dealloc |
| 0.02% | python | PyObject_CallFinalizerFromDealloc |
| 0.02% | python | structseq_dealloc |
| 0.02% | python | _PyIncrementalNewlineDecoder_decode.cold |
| 0.01% | python | PySet_New |
| 0.01% | python | mappingproxy_dealloc |
| 0.01% | python | weakref___new__ |
| 0.01% | python | _PyObject_Realloc |
| 0.01% | python | descr_dealloc |
| 0.01% | python | _PyIncrementalNewlineDecoder_decode |
| 0.01% | python | _PyTokenizer_translate_newlines.constprop.0 |
| 0.01% | python | PyCMethod_New |
| 0.01% | python | unicode_new |
| 0.01% | python | pattern_new_match.isra.0 |
| 0.01% | python | context_new_from_vars |
| 0.01% | python | AttributeError_dealloc |
| 0.00% | python | bytesio_dealloc |
| 0.00% | python | bytesio_new |
| 0.00% | python | type_dealloc |
| 0.00% | python | PyMem_Calloc |
| 0.00% | python | _Py_uop_frame_new |
| 0.00% | python | PyCell_New |
| 0.00% | python | _PyMem_RawMalloc |
| 0.00% | python | _context_alloc |
| 0.00% | python | iter_dealloc |
| 0.00% | python | enum_dealloc |

### library

8.05% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 1.96% | python | sre_ucs1_match |
| 0.84% | libz.so.1.2.11 | crc32_combine64 |
| 0.84% | python | sre_ucs2_charset.isra.0 |
| 0.49% | _json.cpython-314-x86_64-linux-gnu.so | _parse_object_unicode |
| 0.32% | libz.so.1.2.11 | inflateBackEnd |
| 0.22% | libpthread-2.31.so | __pthread_mutex_lock |
| 0.22% | python | sre_search |
| 0.21% | libpthread-2.31.so | pthread_mutex_unlock |
| 0.14% | python | sre_ucs1_count |
| 0.12% | python | _sre_SRE_Pattern_match |
| 0.12% | _json.cpython-314-x86_64-linux-gnu.so | encoder_listencode_dict |
| 0.11% | tracer.cpython-314-x86_64-linux-gnu.so | CTracer_trace |
| 0.08% | libsqlite3.so.0.8.6 | sqlite3_reset |
| 0.07% | libm-2.31.so | __ieee754_pow_fma |
| 0.07% | _asyncio.cpython-314-x86_64-linux-gnu.so | TaskObj_traverse |
| 0.06% | libm-2.31.so | __cos_fma |
| 0.05% | array.cpython-314-x86_64-linux-gnu.so | array_subscr |
| 0.05% | libz.so.1.2.11 | inflateCodesUsed |
| 0.04% | ld-2.31.so | do_lookup_x |
| 0.04% | libm-2.31.so | __fmod_finite@GLIBC_2.15 |
| 0.04% | pyexpat.cpython-314-x86_64-linux-gnu.so | doContent |
| 0.04% | _json.cpython-314-x86_64-linux-gnu.so | py_encode_basestring_ascii |
| 0.04% | python | pattern_subx |
| 0.04% | ld-2.31.so | _dl_relocate_object |
| 0.03% | libm-2.31.so | __sin_fma |
| 0.03% | _json.cpython-314-x86_64-linux-gnu.so | _match_number_unicode.isra.0 |
| 0.03% | fastbinary.cpython-314-x86_64-linux-gnu.so | apache::thrift::py::ProtocolBase<apache::thrift::py::BinaryProtocol>::encodeValue |
| 0.03% | _decimal.cpython-314-x86_64-linux-gnu.so | nm_mpd_qadd |
| 0.03% | pyexpat.cpython-314-x86_64-linux-gnu.so | PyExpat_XML_Parse |
| 0.03% | ld-2.31.so | strcmp |
| 0.03% | _decimal.cpython-314-x86_64-linux-gnu.so | nm_mpd_qmul |
| 0.03% | _decimal.cpython-314-x86_64-linux-gnu.so | _mpd_qaddsub |
| 0.03% | pyexpat.cpython-314-x86_64-linux-gnu.so | normal_contentTok |
| 0.03% | libsqlite3.so.0.8.6 | sqlite3_randomness |
| 0.03% | _decimal.cpython-314-x86_64-linux-gnu.so | _mpd_baseshiftr |
| 0.03% | libpthread-2.31.so | pthread_cond_signal@@GLIBC_2.3.2 |
| 0.02% | libz.so.1.2.11 | inflate |
| 0.02% | pyexpat.cpython-314-x86_64-linux-gnu.so | hash |
| 0.02% | _asyncio.cpython-314-x86_64-linux-gnu.so | task_step_impl |
| 0.02% | pyexpat.cpython-314-x86_64-linux-gnu.so | storeAtts |
| 0.02% | array.cpython-314-x86_64-linux-gnu.so | array_ass_subscr |
| 0.02% | _pickle.cpython-314-x86_64-linux-gnu.so | save |
| 0.02% | ld-2.31.so | _dl_lookup_symbol_x |
| 0.02% | _decimal.cpython-314-x86_64-linux-gnu.so | dec_mpd_qquantize |
| 0.02% | math.cpython-314-x86_64-linux-gnu.so | factorial_partial_product |
| 0.02% | _heapq.cpython-314-x86_64-linux-gnu.so | _heapq_heappop |
| 0.02% | _decimal.cpython-314-x86_64-linux-gnu.so | mpd_qshiftr |
| 0.02% | _decimal.cpython-314-x86_64-linux-gnu.so | _mpd_qmul |
| 0.02% | _decimal.cpython-314-x86_64-linux-gnu.so | find_state_left_or_right |
| 0.02% | _decimal.cpython-314-x86_64-linux-gnu.so | mpd_qfinalize |
| 0.02% | ld-2.31.so | check_match |
| 0.02% | _decimal.cpython-314-x86_64-linux-gnu.so | convert_op |
| 0.02% | _asyncio.cpython-314-x86_64-linux-gnu.so | TaskObj_clear |
| 0.02% | _bisect.cpython-314-x86_64-linux-gnu.so | _bisect_bisect_right |
| 0.02% | _asyncio.cpython-314-x86_64-linux-gnu.so | FutureObj_traverse |
| 0.02% | _asyncio.cpython-314-x86_64-linux-gnu.so | TaskStepMethWrapper_traverse |
| 0.02% | libsqlite3.so.0.8.6 | sqlite3_value_double |
| 0.01% | _asyncio.cpython-314-x86_64-linux-gnu.so | _asyncio_Task___init__ |
| 0.01% | _asyncio.cpython-314-x86_64-linux-gnu.so | task_step |
| 0.01% | _sqlite3.cpython-314-x86_64-linux-gnu.so | _pysqlite_query_execute |
| 0.01% | math.cpython-314-x86_64-linux-gnu.so | math_factorial |
| 0.01% | _asyncio.cpython-314-x86_64-linux-gnu.so | _asyncio_Future_add_done_callback |
| 0.01% | libsqlite3.so.0.8.6 | sqlite3_wal_checkpoint |
| 0.01% | fastbinary.cpython-314-x86_64-linux-gnu.so | apache::thrift::py::ProtocolBase<apache::thrift::py::BinaryProtocol>::decodeValue |
| 0.01% | libsqlite3.so.0.8.6 | sqlite3_value_int64 |
| 0.01% | _asyncio.cpython-314-x86_64-linux-gnu.so | future_init |
| 0.01% | _json.cpython-314-x86_64-linux-gnu.so | _parse_array_unicode |
| 0.01% | libsqlite3.so.0.8.6 | sqlite3_preupdate_old |
| 0.01% | python | sre_ucs1_match.cold |
| 0.01% | _decimal.cpython-314-x86_64-linux-gnu.so | dec_dealloc |
| 0.01% | _elementtree.cpython-314-x86_64-linux-gnu.so | elementiter_next |
| 0.01% | _decimal.cpython-314-x86_64-linux-gnu.so | mpd_qquantize |
| 0.01% | array.cpython-314-x86_64-linux-gnu.so | d_setitem |
| 0.01% | _elementtree.cpython-314-x86_64-linux-gnu.so | element_dealloc |
| 0.01% | _asyncio.cpython-314-x86_64-linux-gnu.so | enter_task.isra.0 |
| 0.01% | _elementtree.cpython-314-x86_64-linux-gnu.so | treebuilder_handle_start |
| 0.01% | _elementtree.cpython-314-x86_64-linux-gnu.so | element_gc_traverse |
| 0.01% | fastbinary.cpython-314-x86_64-linux-gnu.so | apache::thrift::py::ProtocolBase<apache::thrift::py::BinaryProtocol>::readStruct |
| 0.01% | libsqlite3.so.0.8.6 | sqlite3_extended_errcode |
| 0.01% | fastbinary.cpython-314-x86_64-linux-gnu.so | apache::thrift::py::ProtocolBase<apache::thrift::py::BinaryProtocol>::readBytes |
| 0.01% | _asyncio.cpython-314-x86_64-linux-gnu.so | task_wakeup |
| 0.01% | libsqlite3.so.0.8.6 | sqlite3_vtab_config |
| 0.01% | _decimal.cpython-314-x86_64-linux-gnu.so | PyDecType_FromLongExact |
| 0.01% | _struct.cpython-314-x86_64-linux-gnu.so | unpack |
| 0.01% | libsqlite3.so.0.8.6 | sqlite3_step |
| 0.01% | _decimal.cpython-314-x86_64-linux-gnu.so | dec_addstatus |
| 0.01% | libsqlite3.so.0.8.6 | sqlite3_enable_shared_cache |
| 0.01% | libz.so.1.2.11 | adler32_combine64 |
| 0.01% | _elementtree.cpython-314-x86_64-linux-gnu.so | treebuilder_handle_end.isra.0 |
| 0.01% | _asyncio.cpython-314-x86_64-linux-gnu.so | call_soon.isra.0 |
| 0.01% | _asyncio.cpython-314-x86_64-linux-gnu.so | FutureObj_clear |
| 0.01% | python | sre_ucs4_match |
| 0.01% | _struct.cpython-314-x86_64-linux-gnu.so | s_pack |
| 0.01% | libm-2.31.so | powf64 |
| 0.01% | _decimal.cpython-314-x86_64-linux-gnu.so | PyDecType_New.isra.0 |
| 0.01% | math.cpython-314-x86_64-linux-gnu.so | math_cos |
| 0.01% | fastbinary.cpython-314-x86_64-linux-gnu.so | apache::thrift::py::BinaryProtocol::readFieldBegin |
| 0.01% | tracer.cpython-314-x86_64-linux-gnu.so | CTracer_set_pdata_stack |
| 0.01% | math.cpython-314-x86_64-linux-gnu.so | math_sqrt |
| 0.01% | _decimal.cpython-314-x86_64-linux-gnu.so | dec_str |
| 0.01% | _asyncio.cpython-314-x86_64-linux-gnu.so | TaskObj_finalize |
| 0.01% | libsqlite3.so.0.8.6 | sqlite3_str_value |
| 0.01% | _sqlite3.cpython-314-x86_64-linux-gnu.so | pysqlite_cursor_iternext |
| 0.01% | _elementtree.cpython-314-x86_64-linux-gnu.so | expat_data_handler |
| 0.01% | libsqlite3.so.0.8.6 | sqlite3_exec |
| 0.01% | _random.cpython-314-x86_64-linux-gnu.so | _random_Random_random |
| 0.01% | _sqlite3.cpython-314-x86_64-linux-gnu.so | pysqlite_cursor_init |
| 0.01% | _asyncio.cpython-314-x86_64-linux-gnu.so | FutureIter_traverse |
| 0.01% | libsqlite3.so.0.8.6 | sqlite3_mutex_try |
| 0.01% | _decimal.cpython-314-x86_64-linux-gnu.so | current_context |
| 0.01% | array.cpython-314-x86_64-linux-gnu.so | d_getitem |
| 0.01% | _decimal.cpython-314-x86_64-linux-gnu.so | word_to_string |
| 0.01% | python | _sre_compile |
| 0.01% | ld-2.31.so | _dl_map_object_from_fd |
| 0.01% | _elementtree.cpython-314-x86_64-linux-gnu.so | Py_XDECREF |
| 0.01% | libsqlite3.so.0.8.6 | sqlite3_free |
| 0.01% | libsqlite3.so.0.8.6 | sqlite3_value_pointer |
| 0.01% | _asyncio.cpython-314-x86_64-linux-gnu.so | task_call_step_soon |
| 0.01% | libsqlite3.so.0.8.6 | sqlite3_close_v2 |
| 0.00% | _pickle.cpython-314-x86_64-linux-gnu.so | memo_put.isra.0 |
| 0.00% | fastbinary.cpython-314-x86_64-linux-gnu.so | apache::thrift::py::parse_struct_item_spec |
| 0.00% | _random.cpython-314-x86_64-linux-gnu.so | _random_Random_getrandbits |
| 0.00% | _decimal.cpython-314-x86_64-linux-gnu.so | ctx_mpd_qquantize |
| 0.00% | _elementtree.cpython-314-x86_64-linux-gnu.so | element_getitem |
| 0.00% | _decimal.cpython-314-x86_64-linux-gnu.so | mpd_qadd |
| 0.00% | _asyncio.cpython-314-x86_64-linux-gnu.so | future_schedule_callbacks |
| 0.00% | _json.cpython-314-x86_64-linux-gnu.so | 0x0000000000002794 |
| 0.00% | libsqlite3.so.0.8.6 | sqlite3_realloc64 |
| 0.00% | _decimal.cpython-314-x86_64-linux-gnu.so | _mpd_to_string |
| 0.00% | _json.cpython-314-x86_64-linux-gnu.so | 0x0000000000002534 |
| 0.00% | python | _sre_SRE_Pattern_search |
| 0.00% | libsqlite3.so.0.8.6 | sqlite3_db_config |
| 0.00% | array.cpython-314-x86_64-linux-gnu.so | 0x00000000000049c4 |
| 0.00% | _json.cpython-314-x86_64-linux-gnu.so | scanner_call |
| 0.00% | _struct.cpython-314-x86_64-linux-gnu.so | pack |
| 0.00% | python | _sre_SRE_Pattern_sub |
| 0.00% | _json.cpython-314-x86_64-linux-gnu.so | 0x0000000000002664 |
| 0.00% | python | sre_ucs2_match |
| 0.00% | _asyncio.cpython-314-x86_64-linux-gnu.so | future_add_done_callback |
| 0.00% | _sqlite3.cpython-314-x86_64-linux-gnu.so | pysqlite_connection_execute |
| 0.00% | array.cpython-314-x86_64-linux-gnu.so | 0x00000000000047e4 |
| 0.00% | _sqlite3.cpython-314-x86_64-linux-gnu.so | bind_param.isra.0 |
| 0.00% | _json.cpython-314-x86_64-linux-gnu.so | encoder_listencode_obj |
| 0.00% | _decimal.cpython-314-x86_64-linux-gnu.so | _mpd_rnd_incr.isra.0 |
| 0.00% | python | _sre_SRE_Match_end |
| 0.00% | libpthread-2.31.so | sem_post@@GLIBC_2.2.5 |
| 0.00% | math.cpython-314-x86_64-linux-gnu.so | math_sin |
| 0.00% | _sqlite3.cpython-314-x86_64-linux-gnu.so | func_callback |
| 0.00% | array.cpython-314-x86_64-linux-gnu.so | 0x0000000000004854 |
| 0.00% | libsqlite3.so.0.8.6 | sqlite3_sourceid |
| 0.00% | fastbinary.cpython-314-x86_64-linux-gnu.so | apache::thrift::py::parse_struct_args |

### dynamic

5.54% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 0.75% | python | PyObject_GetAttr |
| 0.36% | python | object_isinstance |
| 0.36% | python | _PyObject_MakeTpCall |
| 0.25% | python | PyObject_SetAttr |
| 0.23% | python | _PyObject_GetMethod |
| 0.18% | python | method_get |
| 0.15% | python | PyNumber_AsSsize_t |
| 0.14% | python | PyObject_Free |
| 0.14% | python | PyObject_VectorcallMethod |
| 0.14% | python | type_ready |
| 0.14% | python | PyObject_Vectorcall |
| 0.13% | python | PyObject_GetItem |
| 0.13% | python | _PySuper_Lookup |
| 0.12% | python | PyObject_IsTrue |
| 0.12% | python | PyObject_RichCompareBool |
| 0.11% | python | PyObject_RichCompare |
| 0.11% | python | PyObject_GetIter |
| 0.11% | python | PyObject_GetOptionalAttr |
| 0.10% | python | _PyObject_GenericGetAttrWithDict |
| 0.10% | python | PyObject_IsInstance |
| 0.09% | python | getset_get |
| 0.08% | python | PyObject_Hash |
| 0.08% | python | type_call |
| 0.07% | python | slot_tp_richcompare |
| 0.07% | python | _Py_type_getattro_impl |
| 0.06% | python | PyObject_CallOneArg |
| 0.06% | python | _PyObject_Call |
| 0.06% | python | _PyObject_ClearFreeLists |
| 0.05% | python | PyObject_Str |
| 0.05% | python | _PyObject_VectorcallTstate.lto_priv.1 |
| 0.05% | python | PyObject_Size |
| 0.05% | python | PyType_GetModuleByDef |
| 0.05% | python | PyNumber_TrueDivide |
| 0.04% | python | PyObject_SetItem |
| 0.04% | python | PyNumber_Multiply |
| 0.04% | python | PySequence_Tuple |
| 0.04% | python | PyNumber_And |
| 0.04% | python | StopIteration_init |
| 0.04% | python | PyType_IsSubtype |
| 0.03% | python | PyNumber_Add |
| 0.03% | python | PyObject_VisitManagedDict |
| 0.03% | python | PyNumber_Subtract |
| 0.03% | python | _PyObject_LookupSpecialMethod |
| 0.02% | python | _PyObject_LookupSpecial |
| 0.02% | python | PyIter_Send |
| 0.02% | python | object_richcompare |
| 0.02% | python | PyNumber_Remainder |
| 0.02% | python | PySequence_Contains |
| 0.02% | python | PyNumber_FloorDivide |
| 0.02% | python | PyObject_GenericGetAttr |
| 0.02% | python | type_dict |
| 0.02% | python | PyObject_SelfIter |
| 0.01% | python | PyObject_ClearWeakRefs |
| 0.01% | python | PyObject_LengthHint |
| 0.01% | python | PySequence_Fast |
| 0.01% | python | PyObject_ClearManagedDict |
| 0.01% | python | PyNumber_Rshift |
| 0.01% | python | object_get_class |
| 0.01% | python | _PyNumber_Index |
| 0.01% | python | delitem_common |
| 0.01% | python | PyNumber_Negative |
| 0.01% | python | PyMapping_GetOptionalItem |
| 0.01% | python | PyObject_CallFunction |
| 0.01% | python | object_vacall |
| 0.01% | python | PyObject_GenericHash |
| 0.01% | python | PyNumber_Index |
| 0.01% | python | object_recursive_isinstance.part.0 |
| 0.01% | python | _PyObject_GenericSetAttrWithDict |
| 0.01% | python | PyNumber_Lshift |
| 0.01% | python | PyNumber_InPlaceAdd |
| 0.01% | python | type_dealloc_common |
| 0.01% | python | PyObject_GetBuffer |
| 0.01% | python | _PyNumber_PowerNoMod |
| 0.01% | python | object_init |
| 0.01% | python | type___instancecheck__ |
| 0.01% | python | PyObject_SetAttrString |
| 0.01% | python | PyObject_DelItem |
| 0.00% | python | PyObject_GenericGetDict |
| 0.00% | python | type_get_mro |
| 0.00% | python | PyIter_Next |
| 0.00% | python | type_clear |
| 0.00% | python | PyObject_CallMethodObjArgs |
| 0.00% | python | PyObject_Call |
| 0.00% | python | PyObject_HasAttrWithError |
| 0.00% | python | PyNumber_Or |
| 0.00% | python | type_setattro |
| 0.00% | python | PyObject_VectorcallDict |
| 0.00% | python | object_issubclass |

### unknown

4.32% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 0.21% | python | slot_tp_init |
| 0.17% | python | _Py_MakeCoro |
| 0.10% | python | clear_slots |
| 0.09% | python | func_descr_get |
| 0.08% | python | _PyFrame_MakeAndSetFrameObject |
| 0.06% | python | builtin_min |
| 0.06% | python | _PyStack_UnpackDict |
| 0.05% | python | get_or_create_weakref |
| 0.05% | python | _io_BytesIO_read |
| 0.04% | python | gen_send_ex2 |
| 0.04% | python | builtin_sum |
| 0.04% | python | _PyCfg_OptimizeCodeUnit.constprop.0 |
| 0.04% | python | path_converter |
| 0.04% | python | slot_tp_hash |
| 0.04% | python | _Py_module_getattro |
| 0.04% | python | dictkeys_decref.part.0 |
| 0.04% | python | wrapperdescr_call |
| 0.04% | python | slot_mp_subscript |
| 0.04% | python | vectorcall_maybe.constprop.0 |
| 0.03% | python | ScandirIterator_iternext |
| 0.03% | python | cm_descr_get |
| 0.03% | python | slot_mp_ass_subscript |
| 0.03% | python | PySys_Audit |
| 0.03% | python | convert_to_double |
| 0.03% | python | gen_send_ex |
| 0.03% | python | dictitems_iter |
| 0.03% | python | _PyAssemble_MakeCodeObject |
| 0.03% | python | zip_next |
| 0.03% | python | member_get |
| 0.03% | python | convertitem |
| 0.03% | python | fill_time |
| 0.03% | python | _io_TextIOWrapper_write |
| 0.03% | python | unsafe_tuple_compare |
| 0.03% | python | call_one_instrument |
| 0.02% | python | hashtable_unicode_hash |
| 0.02% | python | lookup_maybe_method |
| 0.02% | python | finalize_interp_clear |
| 0.02% | python | _Py_VaBuildStack.constprop.0 |
| 0.02% | python | hashtable_unicode_compare |
| 0.02% | python | bitwise_xor_rule |
| 0.02% | python | state_init |
| 0.02% | python | code_hash |
| 0.02% | python | binary_op |
| 0.02% | python | Py_XDECREF.lto_priv.1 |
| 0.02% | python | bounded_lru_cache_wrapper |
| 0.02% | python | _add_methods_to_object |
| 0.02% | python | binary_op1 |
| 0.02% | python | emit_trampoline |
| 0.02% | python | _PyCfg_OptimizedCfgToInstructionSequence |
| 0.02% | python | atom_rule |
| 0.02% | python | emit__EXIT_TRACE |
| 0.02% | python | do_string_format |
| 0.02% | python | _PyCoro_GetAwaitableIter |
| 0.02% | python | shift_expr_rule |
| 0.02% | python | make_range_object |
| 0.02% | python | sum_rule |
| 0.02% | python | PyContextVar_Get |
| 0.02% | python | _Py_slot_tp_getattr_hook |
| 0.02% | python | memcmp@plt |
| 0.02% | python | patch_x86_64_32rx |
| 0.02% | python | build_indices_generic |
| 0.02% | python | pthread_self@plt |
| 0.02% | python | builtin_sorted |
| 0.02% | python | term_raw |
| 0.02% | python | PyIndex_Check |
| 0.02% | python | _PyModule_ClearDict |
| 0.02% | python | call_trace_func.isra.0 |
| 0.02% | python | builtin_id |
| 0.02% | [vdso] | __vdso_clock_gettime |
| 0.02% | python | classmethod_get |
| 0.02% | python | make_executor_from_uops |
| 0.02% | python | ins1 |
| 0.02% | python | context_run |
| 0.02% | python | as_ucs4 |
| 0.02% | python | Py_XDECREF.lto_priv.7 |
| 0.01% | python | inversion_rule |
| 0.01% | python | uop_optimize.cold |
| 0.01% | python | builtin_issubclass |
| 0.01% | python | builtin_max |
| 0.01% | python | primary_raw |
| 0.01% | python | _PyDictKeys_StringLookup |
| 0.01% | python | expression_rule |
| 0.01% | python | os_listdir |
| 0.01% | python | slot_sq_item |
| 0.01% | python | write_bytes |
| 0.01% | python | get_type_attr_as_size |
| 0.01% | python | mro_implementation_unlocked |
| 0.01% | python | slot_sq_contains |
| 0.01% | python | factor_rule |
| 0.01% | python | _PyCompile_ConstCacheMergeOne |
| 0.01% | python | _io_open |
| 0.01% | python | builtin_hasattr |
| 0.01% | python | wrap_descr_get |
| 0.01% | python | _PyContext_Exit |
| 0.01% | python | symtable_add_def_ctx |
| 0.01% | python | PyType_FromMetaclass |
| 0.01% | python | map_next |
| 0.01% | python | gc_list_move |
| 0.01% | python | notify_context_watchers.isra.0.constprop.0 |
| 0.01% | python | builtin_any |
| 0.01% | python | int_bit_length |
| 0.01% | python | unsafe_long_compare |
| 0.01% | python | _PyLexer_update_fstring_expr |
| 0.01% | python | frozenset_vectorcall |
| 0.01% | python | _PyCfg_FromInstructionSequence |
| 0.01% | python | wrap_objobjargproc |
| 0.01% | python | builtin_hash |
| 0.01% | python | binary_iop1 |
| 0.01% | python | analyze_block |
| 0.01% | python | weakref_richcompare |
| 0.01% | python | codegen_nameop |
| 0.01% | python | find_keyword |
| 0.01% | python | term_rule |
| 0.01% | python | PyModule_AddObjectRef |
| 0.01% | python | make_dict_from_instance_attributes |
| 0.01% | python | codegen_addop_load_const |
| 0.01% | python | astfold_expr |
| 0.01% | python | _PyFrame_PushUnchecked.isra.0 |
| 0.01% | python | lru_cache_make_key |
| 0.01% | python | _PyBytes_FromList |
| 0.01% | python | _PyBytes_Resize |
| 0.01% | python | symtable_visit_expr |
| 0.01% | python | builtin_repr |
| 0.01% | python | primary_rule |
| 0.01% | python | bitwise_or_rule |
| 0.01% | python | codegen_visit_expr |
| 0.01% | python | _copy_characters |
| 0.01% | python | Py_UNICODE_ISALNUM.lto_priv.1 |
| 0.01% | python | ucs4lib_find_max_char |
| 0.01% | python | maybe_small_long |
| 0.01% | python | getset_set |
| 0.01% | python | gen_close |
| 0.01% | python | weakref___init__ |
| 0.01% | python | iter_iternext |
| 0.01% | python | copy_values |
| 0.01% | python | chain_next |
| 0.01% | python | delitemif_lock_held |
| 0.01% | python | pthread_mutex_unlock@plt |
| 0.01% | python | sm_descr_get |
| 0.01% | python | 0x0000000000084740 |
| 0.01% | python | dictbytype |
| 0.01% | python | update_slots_callback |
| 0.01% | python | PyType_GetBaseByToken |
| 0.01% | python | new_dict |
| 0.01% | python | do_mktuple |
| 0.01% | python | unsafe_latin_compare |
| 0.01% | python | _PyType_AllocNoTrack |
| 0.01% | python | strlen@plt |
| 0.01% | python | emit__ERROR_POP_N |
| 0.01% | python | simple_stmt_rule |
| 0.01% | python | write_str |
| 0.01% | python | _Py_SourceAsString |
| 0.01% | python | _PyFunction_SetVersion |
| 0.01% | python | add_subclass |
| 0.01% | python | pthread_mutex_lock@plt |
| 0.01% | python | frame_settrace |
| 0.01% | python | _PyArena_Malloc |
| 0.01% | python | _PyCfg_ToInstructionSequence |
| 0.01% | python | named_expression_rule |
| 0.01% | python | subtype_dict |
| 0.01% | python | pop_lock_held |
| 0.01% | python | ucs4lib_utf8_decode |
| 0.01% | python | _io_FileIO___init__ |
| 0.01% | python | binary_iop |
| 0.01% | python | descr_setcheck.isra.0 |
| 0.01% | python | va_build_value |
| 0.01% | python | super_getattro |
| 0.01% | python | remove_unreachable |
| 0.01% | python | slot_tp_iter |
| 0.01% | python | _validate_inner |
| 0.01% | python | builtin___build_class__ |
| 0.01% | python | _PyRecursiveMutex_TryUnlock |
| 0.01% | python | compute_line |
| 0.01% | python | ucs4lib_fastsearch |
| 0.01% | python | update_slot |
| 0.01% | python | _PyOptimizer_Optimize |
| 0.01% | python | PyTime_AsSecondsDouble |
| 0.01% | python | _Py_call_instrumentation_arg |
| 0.01% | python | _PyContext_Enter |
| 0.01% | python | os_stat |
| 0.01% | python | PyThread_get_thread_ident_ex |
| 0.01% | python | update_symbols |
| 0.01% | python | find_frozen |
| 0.01% | python | __errno_location@plt |
| 0.01% | python | remove_redundant_nops_and_jumps |
| 0.01% | python | _pystat_fromstructstat |
| 0.01% | python | memmove@plt |
| 0.01% | python | subtype_clear |
| 0.01% | python | target_with_star_atom_rule |
| 0.01% | python | duplicate_exits_without_lineno |
| 0.00% | python | os_fspath |
| 0.00% | python | ascii_upper_or_lower |
| 0.00% | python | _io__Buffered_read |
| 0.00% | python | 0x0000000000084750 |
| 0.00% | python | islice_next |
| 0.00% | python | propagate_line_numbers |
| 0.00% | python | map_vectorcall |
| 0.00% | python | PyFile_WriteObject |
| 0.00% | python | unsafe_object_compare |
| 0.00% | python | _Py_Executors_InvalidateCold |
| 0.00% | python | pthread_cond_signal@plt |
| 0.00% | python | _abc__abc_instancecheck |
| 0.00% | python | PyOS_FSPath |
| 0.00% | python | _loop1_30_rule |
| 0.00% | python | assign_version_tag |
| 0.00% | python | _PyFunction_FromConstructor |
| 0.00% | python | match_getslice_by_index |
| 0.00% | python | solid_base |
| 0.00% | python | slot_nb_bool |
| 0.00% | python | listreviter_next |
| 0.00% | python | _stringio_readline.cold |
| 0.00% | python | slot_nb_subtract |
| 0.00% | python | clear_weakref_lock_held |
| 0.00% | python | _textiowrapper_writeflush |
| 0.00% | python | weakref_hash |
| 0.00% | python | _PyMutex_LockTimed |
| 0.00% | python | clear_lock_held |
| 0.00% | python | _PyStack_UnpackDict_Free |
| 0.00% | python | wrapper_call |
| 0.00% | python | posix_do_stat.isra.0 |
| 0.00% | python | builtin_print |
| 0.00% | python | _PyBytesWriter_Finish |
| 0.00% | python | _io_BytesIO___init__ |
| 0.00% | python | merge_at |
| 0.00% | python | _Py_uop_abstractcontext_fini |
| 0.00% | python | _Py_bytes_lower |
| 0.00% | python | gallop_right |
| 0.00% | python | gallop_left |
| 0.00% | python | label_exception_targets |
| 0.00% | python | _imp_is_builtin |
| 0.00% | python | slot_sq_length |
| 0.00% | python | import_star |
| 0.00% | python | args_rule |
| 0.00% | python | strchr@plt |
| 0.00% | python | insert_split_value.isra.0 |
| 0.00% | python | specialize_py_call |
| 0.00% | python | assignment_expression_rule |
| 0.00% | python | emit__CHECK_VALIDITY |
| 0.00% | python | new_keys_object.constprop.0 |
| 0.00% | python | bitwise_and_rule |
| 0.00% | python | strings_rule |
| 0.00% | python | merge_from_seq2_lock_held |
| 0.00% | python | emit__DEOPT |
| 0.00% | python | emit__FATAL_ERROR |
| 0.00% | python | analyze_descriptor |
| 0.00% | python | member_set |
| 0.00% | python | builtin_ord |
| 0.00% | python | t_primary_raw |

### int

4.10% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 0.84% | python | k_mul |
| 0.45% | python | x_divrem |
| 0.44% | python | _PyLong_Add |
| 0.26% | python | long_hash |
| 0.24% | python | PyLong_FromLong |
| 0.22% | python | long_to_decimal_string_internal |
| 0.19% | python | x_add |
| 0.14% | python | long_add |
| 0.12% | python | long_bitwise |
| 0.11% | python | x_sub |
| 0.11% | python | _PyLong_Subtract |
| 0.10% | python | long_richcompare |
| 0.08% | python | PyLong_FromString |
| 0.08% | python | long_and |
| 0.08% | python | long_div |
| 0.08% | python | long_sub |
| 0.07% | python | _PyLong_Multiply |
| 0.07% | python | long_rshift |
| 0.05% | python | long_mod |
| 0.05% | python | PyLong_FromSsize_t |
| 0.04% | python | PyLong_AsDouble |
| 0.04% | python | long_mul_method |
| 0.03% | python | PyLong_FromUnsignedLongLong |
| 0.02% | python | long_lshift_method |
| 0.02% | python | _PyLong_GCD |
| 0.02% | python | PyLong_AsLong |
| 0.02% | python | _PyLong_FromSTwoDigits |
| 0.01% | python | PyLong_FromUnsignedLong |
| 0.01% | python | long_xor |
| 0.01% | python | _PyLong_FromBytes |
| 0.01% | python | long_lshift_int64 |
| 0.01% | python | PyLong_AsSsize_t |
| 0.01% | python | long_mul |
| 0.01% | python | _PyLong_Frexp |
| 0.01% | python | PyLong_AsLongAndOverflow |
| 0.01% | python | PyLong_AsInt |
| 0.01% | python | long_vectorcall |
| 0.01% | python | long_add_method |
| 0.00% | python | _PyLong_FromByteArray |
| 0.00% | python | long_true_divide |
| 0.00% | python | PyLong_FromLongLong |
| 0.00% | python | long_sub_method |
| 0.00% | python | long_or |
| 0.00% | python | PyLong_FromUnicodeObject |

### dict

3.99% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 1.06% | python | PyDict_GetItemRef |
| 0.53% | python | insertdict |
| 0.34% | python | PyDict_Contains |
| 0.32% | python | PyDict_SetItem |
| 0.29% | python | dictresize |
| 0.25% | python | dict_get |
| 0.20% | python | dict_setdefault_ref_lock_held |
| 0.19% | python | insert_to_emptydict |
| 0.17% | python | dictiter_iternextkey |
| 0.15% | python | dict_subscript |
| 0.08% | python | dictiter_iternextitem |
| 0.06% | python | dict_merge |
| 0.04% | python | dict_items |
| 0.03% | python | PyDict_Copy |
| 0.03% | python | PyDict_GetItemWithError |
| 0.02% | python | PyDict_Next |
| 0.02% | python | dict_getitem |
| 0.02% | python | PyDict_DelItem |
| 0.02% | python | _PyDict_SetItem_Take2 |
| 0.02% | python | _PyDict_Next |
| 0.01% | python | _PyDict_FromItems |
| 0.01% | python | dictiter_iternextvalue |
| 0.01% | python | _PyDict_GetItem_KnownHash |
| 0.01% | python | PyDict_SetItemString |
| 0.01% | python | PyDict_GetItemStringRef |
| 0.01% | python | _PyDict_LoadBuiltinsFromGlobals |
| 0.01% | python | dict_iter |
| 0.01% | python | dict_update_common |
| 0.01% | python | dict_ass_sub |
| 0.00% | python | dict_richcompare |
| 0.00% | python | PyDict_SetDefaultRef |
| 0.00% | python | _PyDict_DetachFromObject |

### str

3.67% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 0.62% | python | intern_common.part.0 |
| 0.50% | python | siphash13 |
| 0.28% | python | PyUnicode_Substring |
| 0.28% | python | PyUnicode_FromKindAndData |
| 0.18% | python | _PyUnicode_JoinArray |
| 0.15% | python | PyBytes_FromStringAndSize |
| 0.14% | python | unicode_replace |
| 0.09% | python | _PyUnicodeWriter_PrepareInternal |
| 0.09% | python | PyUnicode_Format |
| 0.08% | python | unicode_decode_utf8 |
| 0.07% | python | _PyUnicodeWriter_WriteStr |
| 0.07% | python | PyUnicode_RichCompare |
| 0.06% | python | PyUnicodeWriter_WriteStr |
| 0.06% | python | PyUnicode_InternFromString |
| 0.05% | python | PyUnicode_Concat |
| 0.05% | python | bytes_subscript |
| 0.05% | python | resize_compact |
| 0.04% | python | unicode_hash |
| 0.04% | python | unicode_from_format |
| 0.04% | python | PyUnicode_Contains |
| 0.04% | python | unicode_encode |
| 0.04% | python | _PyUnicode_Equal |
| 0.03% | python | intern_constants |
| 0.03% | python | PyUnicode_FromString |
| 0.03% | python | bytes_concat |
| 0.03% | python | PyUnicode_DecodeUTF8 |
| 0.03% | python | stringlib_bytes_join.lto_priv.1 |
| 0.03% | python | unicode_encode_utf8 |
| 0.02% | python | PyUnicode_DecodeFSDefault |
| 0.02% | python | unicode_eq.lto_priv.1 |
| 0.02% | python | split |
| 0.02% | python | unicode_split |
| 0.02% | python | unicode_subscript |
| 0.02% | python | unicode_startswith |
| 0.02% | python | unicode_vectorcall |
| 0.01% | python | bytes_richcompare |
| 0.01% | python | unicode_repr |
| 0.01% | python | PyUnicode_FSConverter |
| 0.01% | python | unicode_splitlines |
| 0.01% | python | unicode_fromformat_write_utf8 |
| 0.01% | python | PyUnicode_FromWideChar |
| 0.01% | python | _PyUnicode_FromUCS4 |
| 0.01% | python | unicode_join |
| 0.01% | python | _PyUnicode_IsAlpha |
| 0.01% | python | bytes_decode |
| 0.01% | python | _PyUnicodeWriter_Init |
| 0.01% | python | unicode_rstrip |
| 0.01% | python | _PyUnicodeWriter_Finish |
| 0.01% | python | unicode_rfind |
| 0.01% | python | unicode_strip |
| 0.01% | python | unicode_find |
| 0.01% | python | unicode_decode_utf8_writer |
| 0.01% | python | _PyUnicode_TranslateCharmap |
| 0.01% | python | _PyUnicode_ToDecimalDigit |
| 0.01% | python | PyUnicode_RPartition |
| 0.01% | python | bytes_hash |
| 0.01% | python | PyUnicodeWriter_Create |
| 0.01% | python | PyUnicode_CompareWithASCIIString |
| 0.01% | python | stringlib__two_way.lto_priv.1 |
| 0.01% | python | unicode_isupper |
| 0.01% | python | _PyUnicode_IsDigit |
| 0.00% | python | PyUnicode_AsUTF8AndSize |
| 0.00% | python | PyUnicode_FindChar |
| 0.00% | python | unicode_endswith |
| 0.00% | python | PyUnicode_Append |
| 0.00% | python | PyUnicode_DecodeFSDefaultAndSize |
| 0.00% | python | _PyUnicodeWriter_WriteCharInline |
| 0.00% | python | _PyUnicode_FromASCII |
| 0.00% | python | PyUnicode_FromFormat |
| 0.00% | python | _PyUnicodeWriter_WriteSubstring |
| 0.00% | python | _PyUnicode_ScanIdentifier |
| 0.00% | python | PyUnicode_DecodeLocale |

### kernel

3.61% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 0.14% | [kernel.kallsyms] | native_irq_return_iret |
| 0.12% | [kernel.kallsyms] | clear_page_erms |
| 0.10% | [kernel.kallsyms] | copy_user_enhanced_fast_string |
| 0.10% | [kernel.kallsyms] | sync_regs |
| 0.09% | [kernel.kallsyms] | __d_lookup_rcu |
| 0.08% | [kernel.kallsyms] | rmqueue |
| 0.08% | [kernel.kallsyms] | zap_pte_range.isra.0 |
| 0.07% | [kernel.kallsyms] | _raw_spin_lock |
| 0.07% | [kernel.kallsyms] | free_pcppages_bulk |
| 0.07% | [kernel.kallsyms] | memset_erms |
| 0.05% | [kernel.kallsyms] | __handle_mm_fault |
| 0.05% | [kernel.kallsyms] | clear_bhb_loop |
| 0.04% | [kernel.kallsyms] | try_charge |
| 0.04% | [kernel.kallsyms] | get_mem_cgroup_from_mm |
| 0.04% | [kernel.kallsyms] | release_pages |
| 0.04% | [kernel.kallsyms] | __pagevec_lru_add_fn |
| 0.04% | [kernel.kallsyms] | filemap_map_pages |
| 0.04% | [kernel.kallsyms] | link_path_walk.part.0 |
| 0.04% | [kernel.kallsyms] | mem_cgroup_throttle_swaprate |
| 0.03% | [kernel.kallsyms] | kmem_cache_alloc |
| 0.03% | [kernel.kallsyms] | perf_iterate_ctx |
| 0.03% | [kernel.kallsyms] | mem_cgroup_try_charge |
| 0.03% | [kernel.kallsyms] | ext4_htree_store_dirent |
| 0.03% | [kernel.kallsyms] | handle_mm_fault |
| 0.03% | [kernel.kallsyms] | syscall_return_via_sysret |
| 0.03% | [kernel.kallsyms] | do_syscall_64 |
| 0.03% | [kernel.kallsyms] | find_vma |
| 0.03% | [kernel.kallsyms] | __ext4fs_dirhash |
| 0.03% | [kernel.kallsyms] | __alloc_pages_nodemask |
| 0.02% | [kernel.kallsyms] | page_remove_rmap |
| 0.02% | [kernel.kallsyms] | kmem_cache_free |
| 0.02% | [kernel.kallsyms] | strncpy_from_user |
| 0.02% | [kernel.kallsyms] | memcg_kmem_get_cache |
| 0.02% | [kernel.kallsyms] | copy_page |
| 0.02% | [kernel.kallsyms] | native_flush_tlb_one_user |
| 0.02% | [kernel.kallsyms] | filldir64 |
| 0.02% | [kernel.kallsyms] | memcpy_erms |
| 0.02% | [kernel.kallsyms] | unmapped_area_topdown |
| 0.02% | [kernel.kallsyms] | find_get_entry |
| 0.02% | [kernel.kallsyms] | smp_call_function_single |
| 0.02% | [kernel.kallsyms] | lookup_fast |
| 0.02% | [kernel.kallsyms] | inode_permission |
| 0.02% | [kernel.kallsyms] | do_anonymous_page |
| 0.02% | [kernel.kallsyms] | do_user_addr_fault |
| 0.02% | [kernel.kallsyms] | entry_SYSCALL_64 |
| 0.02% | [kernel.kallsyms] | __count_memcg_events |
| 0.02% | [kernel.kallsyms] | generic_permission |
| 0.02% | [kernel.kallsyms] | vmacache_find |
| 0.02% | [kernel.kallsyms] | walk_component |
| 0.02% | [kernel.kallsyms] | kfree |
| 0.02% | [kernel.kallsyms] | str2hashbuf_signed |
| 0.02% | [kernel.kallsyms] | error_entry |
| 0.01% | [kernel.kallsyms] | __mod_memcg_state |
| 0.01% | [kernel.kallsyms] | __vma_adjust |
| 0.01% | [kernel.kallsyms] | get_page_from_freelist |
| 0.01% | [kernel.kallsyms] | __mod_lruvec_state |
| 0.01% | [kernel.kallsyms] | page_fault |
| 0.01% | [kernel.kallsyms] | __virt_addr_valid |
| 0.01% | [kernel.kallsyms] | rb_insert_color |
| 0.01% | [kernel.kallsyms] | ext4_getattr |
| 0.01% | [kernel.kallsyms] | prep_new_page |
| 0.01% | [kernel.kallsyms] | rb_next |
| 0.01% | [kernel.kallsyms] | __slab_free |
| 0.01% | [kernel.kallsyms] | _cond_resched |
| 0.01% | [kernel.kallsyms] | up_read |
| 0.01% | [kernel.kallsyms] | __lru_cache_add |
| 0.01% | [kernel.kallsyms] | security_inode_getattr |
| 0.01% | [kernel.kallsyms] | swapgs_restore_regs_and_return_to_usermode |
| 0.01% | [kernel.kallsyms] | perf_event_alloc |
| 0.01% | [kernel.kallsyms] | entry_SYSCALL_64_after_hwframe |
| 0.01% | [kernel.kallsyms] | xas_load |
| 0.01% | [kernel.kallsyms] | perf_event_mmap |
| 0.01% | [kernel.kallsyms] | pagevec_lru_move_fn |
| 0.01% | [kernel.kallsyms] | mem_cgroup_from_task |
| 0.01% | [kernel.kallsyms] | page_counter_cancel |
| 0.01% | [kernel.kallsyms] | lru_cache_add_active_or_unevictable |
| 0.01% | [kernel.kallsyms] | __follow_mount_rcu.isra.0 |
| 0.01% | [kernel.kallsyms] | down_read_trylock |
| 0.01% | [kernel.kallsyms] | generic_file_buffered_read |
| 0.01% | [kernel.kallsyms] | __kmalloc |
| 0.01% | [kernel.kallsyms] | alloc_pages_vma |
| 0.01% | [kernel.kallsyms] | _raw_spin_lock_irqsave |
| 0.01% | [kernel.kallsyms] | ___slab_alloc |
| 0.01% | [kernel.kallsyms] | free_unref_page_list |
| 0.01% | [kernel.kallsyms] | free_unref_page_prepare.part.0 |
| 0.01% | [kernel.kallsyms] | format_decode |
| 0.01% | [kernel.kallsyms] | __ext4_check_dir_entry |
| 0.01% | [kernel.kallsyms] | vsnprintf |
| 0.01% | [kernel.kallsyms] | set_root |
| 0.01% | [kernel.kallsyms] | show_cpuinfo |
| 0.01% | [kernel.kallsyms] | page_add_file_rmap |
| 0.01% | [kernel.kallsyms] | rcu_all_qs |
| 0.01% | [kernel.kallsyms] | __mod_node_page_state |
| 0.01% | [kernel.kallsyms] | in_group_p |
| 0.01% | [kernel.kallsyms] | __legitimize_mnt |
| 0.01% | [kernel.kallsyms] | page_counter_try_charge |
| 0.01% | [kernel.kallsyms] | string_nocheck |
| 0.01% | [kernel.kallsyms] | fpregs_assert_state_consistent |
| 0.01% | [kernel.kallsyms] | __perf_addr_filters_adjust |
| 0.01% | [kernel.kallsyms] | fsnotify |
| 0.01% | [kernel.kallsyms] | mem_cgroup_commit_charge |
| 0.01% | [kernel.kallsyms] | __vma_link_rb |
| 0.01% | [kernel.kallsyms] | mmap_region |
| 0.01% | [kernel.kallsyms] | free_pages_and_swap_cache |
| 0.01% | [kernel.kallsyms] | psi_task_change |
| 0.01% | [kernel.kallsyms] | __check_heap_object |
| 0.01% | [kernel.kallsyms] | free_unref_page_commit |
| 0.01% | [kernel.kallsyms] | unlock_page |
| 0.01% | [kernel.kallsyms] | __mod_zone_page_state |
| 0.01% | [kernel.kallsyms] | __fget_light |
| 0.01% | [kernel.kallsyms] | security_inode_permission |
| 0.01% | [kernel.kallsyms] | memchr |
| 0.01% | [kernel.kallsyms] | alloc_set_pte |
| 0.01% | [kernel.kallsyms] | kmem_cache_alloc_trace |
| 0.01% | [kernel.kallsyms] | call_filldir |
| 0.01% | [kernel.kallsyms] | memcg_kmem_put_cache |
| 0.01% | [kernel.kallsyms] | mutex_lock |
| 0.01% | [kernel.kallsyms] | __check_object_size |
| 0.01% | [kernel.kallsyms] | mem_cgroup_try_charge_delay |
| 0.01% | [kernel.kallsyms] | perf_iterate_sb |
| 0.01% | [kernel.kallsyms] | change_protection_range |
| 0.01% | [kernel.kallsyms] | kthread_blkcg |
| 0.01% | [kernel.kallsyms] | getname_flags |
| 0.01% | [kernel.kallsyms] | native_sched_clock |
| 0.01% | [kernel.kallsyms] | __do_munmap |
| 0.01% | [kernel.kallsyms] | __vma_rb_erase |
| 0.01% | [kernel.kallsyms] | pmd_devmap_trans_unstable |
| 0.01% | [kernel.kallsyms] | unmap_page_range |
| 0.01% | [kernel.kallsyms] | anon_vma_interval_tree_insert |
| 0.01% | [kernel.kallsyms] | down_write |
| 0.01% | [kernel.kallsyms] | lockref_put_return |
| 0.01% | [kernel.kallsyms] | up_write |
| 0.01% | [kernel.kallsyms] | page_add_new_anon_rmap |
| 0.01% | [kernel.kallsyms] | vfs_getattr_nosec |
| 0.01% | [kernel.kallsyms] | _raw_spin_lock_irq |
| 0.01% | [kernel.kallsyms] | anon_vma_interval_tree_remove |
| 0.01% | [kernel.kallsyms] | __alloc_file |
| 0.01% | [kernel.kallsyms] | uncharge_page |
| 0.01% | [kernel.kallsyms] | __rb_insert_augmented |
| 0.00% | [kernel.kallsyms] | __do_page_fault |
| 0.00% | [kernel.kallsyms] | vma_interval_tree_insert |
| 0.00% | [kernel.kallsyms] | __lock_text_start |
| 0.00% | [kernel.kallsyms] | mem_cgroup_page_lruvec |
| 0.00% | [kernel.kallsyms] | mem_cgroup_update_lru_size |
| 0.00% | [kernel.kallsyms] | update_load_avg |
| 0.00% | [kernel.kallsyms] | mem_cgroup_charge_statistics |
| 0.00% | [kernel.kallsyms] | common_file_perm |
| 0.00% | [kernel.kallsyms] | do_dentry_open |
| 0.00% | [kernel.kallsyms] | vma_merge |
| 0.00% | [kernel.kallsyms] | cp_new_stat |
| 0.00% | [kernel.kallsyms] | common_perm |
| 0.00% | [kernel.kallsyms] | update_cfs_group |
| 0.00% | [kernel.kallsyms] | vm_normal_page |
| 0.00% | [kernel.kallsyms] | rb_next_postorder |
| 0.00% | [kernel.kallsyms] | get_task_policy.part.0 |
| 0.00% | [kernel.kallsyms] | htree_dirblock_to_tree |
| 0.00% | [kernel.kallsyms] | vma_interval_tree_remove |
| 0.00% | [kernel.kallsyms] | __lookup_mnt |
| 0.00% | [kernel.kallsyms] | path_init |
| 0.00% | [kernel.kallsyms] | may_open.isra.0 |
| 0.00% | [kernel.kallsyms] | mutex_unlock |
| 0.00% | [kernel.kallsyms] | ext4_dx_readdir |
| 0.00% | [kernel.kallsyms] | xas_start |
| 0.00% | [kernel.kallsyms] | __task_pid_nr_ns |
| 0.00% | [kernel.kallsyms] | update_curr |
| 0.00% | [kernel.kallsyms] | map_id_up |
| 0.00% | [kernel.kallsyms] | page_mapping |
| 0.00% | [kernel.kallsyms] | exit_to_usermode_loop |
| 0.00% | [kernel.kallsyms] | do_sys_open |
| 0.00% | [kernel.kallsyms] | mark_page_accessed |
| 0.00% | [kernel.kallsyms] | copy_process |
| 0.00% | [kernel.kallsyms] | prepare_exit_to_usermode |
| 0.00% | [kernel.kallsyms] | __find_get_block |
| 0.00% | [kernel.kallsyms] | __fput |
| 0.00% | [kernel.kallsyms] | flush_tlb_mm_range |
| 0.00% | [kernel.kallsyms] | filename_lookup |
| 0.00% | [kernel.kallsyms] | apparmor_file_alloc_security |
| 0.00% | [kernel.kallsyms] | do_page_fault |
| 0.00% | [kernel.kallsyms] | native_write_msr |
| 0.00% | [kernel.kallsyms] | errseq_sample |
| 0.00% | [kernel.kallsyms] | flush_tlb_func_common.constprop.0 |
| 0.00% | [kernel.kallsyms] | change_pte_range |
| 0.00% | [kernel.kallsyms] | get_vma_policy.part.0 |
| 0.00% | [kernel.kallsyms] | fput_many |
| 0.00% | [kernel.kallsyms] | nmi_restore |
| 0.00% | [kernel.kallsyms] | __fsnotify_parent |
| 0.00% | [kernel.kallsyms] | __update_load_avg_se |
| 0.00% | [kernel.kallsyms] | inherit_event.isra.0 |

### libc

2.38% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 0.56% | libc-2.31.so | __memcpy_avx_unaligned_erms |
| 0.42% | libc-2.31.so | __memset_avx2_unaligned_erms |
| 0.25% | libc-2.31.so | _int_malloc |
| 0.15% | libc-2.31.so | __memcmp_avx2_movbe |
| 0.14% | libc-2.31.so | _int_free |
| 0.12% | libc-2.31.so | __libc_malloc |
| 0.09% | libc-2.31.so | __strlen_avx2 |
| 0.06% | libc-2.31.so | __memset_avx2_erms |
| 0.05% | libc-2.31.so | unlink_chunk.isra.0 |
| 0.04% | libc-2.31.so | cfree@GLIBC_2.2.5 |
| 0.03% | libc-2.31.so | __strchr_avx2 |
| 0.02% | libc-2.31.so | pthread_self |
| 0.02% | libc-2.31.so | wcsrtombs |
| 0.02% | libc-2.31.so | __strncmp_avx2 |
| 0.02% | libc-2.31.so | __strcmp_avx2 |
| 0.02% | libc-2.31.so | __errno_location |
| 0.02% | libc-2.31.so | pthread_mutex_lock |
| 0.02% | libc-2.31.so | __memchr_avx2 |
| 0.02% | libc-2.31.so | __gconv_transform_internal_utf8 |
| 0.01% | libc-2.31.so | __libc_realloc |
| 0.01% | libc-2.31.so | __gconv_transform_utf8_internal |
| 0.01% | libc-2.31.so | pthread_mutex_unlock |
| 0.01% | libc-2.31.so | malloc_consolidate |
| 0.01% | libc-2.31.so | _int_realloc |
| 0.01% | libc-2.31.so | __xstat64 |
| 0.01% | libcrypto.so.1.1 | EVP_DecodeUpdate |
| 0.01% | libc-2.31.so | clock_gettime@@GLIBC_2.17 |
| 0.01% | libc-2.31.so | pthread_cond_signal@@GLIBC_2.3.2 |
| 0.01% | libc-2.31.so | __mbsrtowcs_l |
| 0.01% | libcrypto.so.1.1 | ASN1_tag2bit |
| 0.01% | libc-2.31.so | __strcpy_avx2 |
| 0.00% | libc-2.31.so | getenv |
| 0.00% | libc-2.31.so | __memrchr_avx2 |
| 0.00% | libcrypto.so.1.1 | EVP_desx_cbc |
| 0.00% | libc-2.31.so | __strrchr_avx2 |
| 0.00% | libc-2.31.so | calloc |
| 0.00% | libcrypto.so.1.1 | ASN1_item_i2d |
| 0.00% | libc-2.31.so | readdir64 |
| 0.00% | libc-2.31.so | __dcigettext |
| 0.00% | libcrypto.so.1.1 | ASN1_ENUMERATED_to_BN |
| 0.00% | libcrypto.so.1.1 | NETSCAPE_SPKI_print |
| 0.00% | libcrypto.so.1.1 | ASN1_item_ex_free |
| 0.00% | libc-2.31.so | __wcslen_avx2 |
| 0.00% | libc-2.31.so | read |

### miscobj

1.73% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 0.27% | python | _PySet_Contains |
| 0.12% | python | set_issubset_impl |
| 0.11% | python | setiter_iternext |
| 0.08% | python | PySlice_Unpack |
| 0.08% | python | set_vectorcall |
| 0.08% | python | set_lookkey |
| 0.07% | python | set_difference |
| 0.07% | python | make_gen |
| 0.06% | python | gen_iternext |
| 0.06% | python | range_vectorcall |
| 0.05% | python | range_iter |
| 0.05% | python | _PyBuildSlice_ConsumeRefs |
| 0.04% | python | enum_next |
| 0.04% | python | set_contains_lock_held |
| 0.04% | python | PySet_Add |
| 0.04% | python | bytearray_ass_subscript |
| 0.04% | python | set_table_resize |
| 0.03% | python | dequeiter_next_lock_held.isra.0 |
| 0.03% | python | set_add_entry |
| 0.03% | python | range_subscript |
| 0.02% | python | deque_append_lock_held |
| 0.02% | python | set_iter |
| 0.02% | python | PySlice_AdjustIndices |
| 0.02% | python | set_merge_lock_held.part.0 |
| 0.02% | python | deque_append_impl |
| 0.02% | python | set_add |
| 0.02% | python | set_discard_entry |
| 0.01% | python | deque_clear |
| 0.01% | python | set_intersection |
| 0.01% | python | deque_popleft_impl |
| 0.01% | python | _PyGen_FetchStopIterationValue.cold |
| 0.01% | python | _PyGen_SetStopIterationValue |
| 0.01% | python | PySet_Contains |
| 0.01% | python | _PySlice_GetLongIndices |
| 0.01% | python | _PyGen_yf |
| 0.01% | python | set_difference_update_internal |
| 0.01% | python | set_richcompare |
| 0.01% | python | PyBuffer_Release |
| 0.01% | python | deque_append |
| 0.01% | python | _PyGen_FetchStopIterationValue |
| 0.00% | python | deque_iter |
| 0.00% | python | range_reverse |
| 0.00% | python | dequeiter_next |

### list

1.54% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 0.32% | python | list_subscript |
| 0.22% | python | list_ass_slice_lock_held |
| 0.21% | python | list_iter |
| 0.09% | python | list_resize |
| 0.08% | python | listiter_next |
| 0.07% | python | list_contains |
| 0.06% | python | _PyList_AppendTakeRefListResize |
| 0.06% | python | _list_extend |
| 0.05% | python | list_ass_subscript |
| 0.05% | python | list_remove |
| 0.05% | python | PyList_Append |
| 0.05% | python | list_sort_impl |
| 0.04% | python | _PyList_FromStackRefSteal |
| 0.04% | python | list_concat |
| 0.04% | python | list_vectorcall |
| 0.03% | python | list_append |
| 0.03% | python | list_pop |
| 0.01% | python | list_clear_impl.constprop.0 |
| 0.01% | python | list_richcompare |
| 0.01% | python | list_length |
| 0.01% | python | list_insert |
| 0.01% | python | list_item |
| 0.00% | python | list_index |
| 0.00% | python | _PyList_Extend |
| 0.00% | python | list_extend_dict |

### tuple

1.09% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 0.51% | python | tuple_hash |
| 0.24% | python | _PyTuple_FromStackRefSteal |
| 0.09% | python | tuple_richcompare |
| 0.09% | python | tuple_iter |
| 0.05% | python | PyTuple_Pack |
| 0.03% | python | _PyTuple_FromArray |
| 0.02% | python | tuple_contains |
| 0.02% | python | _PyTuple_Resize |
| 0.01% | python | tuple_subscript |
| 0.01% | python | PyTuple_Size |
| 0.01% | python | tupleiter_next |
| 0.01% | python | tuple_concat |
| 0.00% | python | tuple_length |
| 0.00% | python | tuple_item |

### lookup

0.90% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 0.25% | python | find_name_in_mro |
| 0.21% | python | _Py_dict_lookup |
| 0.17% | python | _Py_type_getattro |
| 0.16% | python | unicodekeys_lookup_unicode |
| 0.06% | python | _PyType_LookupRef |
| 0.04% | python | builtin_getattr |
| 0.01% | python | PyMember_SetOne |
| 0.00% | python | _Py_hashtable_destroy |

### calls

0.89% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 0.30% | python | _PyFunction_Vectorcall |
| 0.08% | python | vgetargs1_impl |
| 0.07% | python | vgetargskeywords.constprop.0 |
| 0.06% | python | method_vectorcall |
| 0.05% | python | PyArg_UnpackTuple |
| 0.05% | python | _PyArg_UnpackKeywords |
| 0.04% | python | vectorcall_method |
| 0.03% | python | method_vectorcall_VARARGS_KEYWORDS |
| 0.03% | python | cfunction_vectorcall_FASTCALL_KEYWORDS |
| 0.02% | python | cfunction_vectorcall_O |
| 0.02% | python | method_vectorcall_FASTCALL_KEYWORDS_METHOD |
| 0.02% | python | cfunction_vectorcall_NOARGS |
| 0.02% | python | _Py_CheckFunctionResult |
| 0.02% | python | method_vectorcall_O |
| 0.01% | python | _PyArg_UnpackKeywordsWithVararg |
| 0.01% | python | method_vectorcall_VARARGS |
| 0.01% | python | method_vectorcall_NOARGS |
| 0.01% | python | PyArg_Parse |
| 0.01% | python | PyArg_ParseTupleAndKeywords |
| 0.01% | python | cfunction_call |
| 0.01% | python | PyArg_ParseTuple |
| 0.01% | python | method_vectorcall_FASTCALL |
| 0.00% | python | cfunction_vectorcall_FASTCALL_KEYWORDS_METHOD |
| 0.00% | python | cfunction_vectorcall_FASTCALL |

### float

0.79% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 0.47% | python | _PyFloat_FromDouble_ConsumeInputs |
| 0.09% | python | float_div |
| 0.06% | python | PyFloat_FromDouble |
| 0.04% | python | PyFloat_AsDouble |
| 0.04% | python | float_richcompare |
| 0.03% | python | float_sub |
| 0.03% | python | float_pow |
| 0.02% | python | float_mul |
| 0.01% | python | float_add |
| 0.01% | python | float_rem |

### exceptions

0.46% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 0.13% | python | _PyErr_SetObject |
| 0.07% | python | PyCode_Addr2Line |
| 0.06% | python | PyTraceBack_Here |
| 0.05% | python | BaseException_vectorcall |
| 0.03% | python | PyErr_GivenExceptionMatches |
| 0.03% | python | PyErr_ExceptionMatches |
| 0.02% | python | PyErr_Format |
| 0.01% | python | PyErr_Occurred |
| 0.01% | python | PyFrame_GetCode |
| 0.01% | python | AttributeError_init |
| 0.01% | python | PyFrame_GetLineNumber |
| 0.01% | python | _PyErr_SetKeyError |
| 0.00% | python | PyErr_GetRaisedException |

### import

0.39% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 0.36% | python | r_object |
| 0.02% | python | PyImport_ImportModuleLevelObject |

### compiler

0.28% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 0.15% | python | uop_optimize |
| 0.05% | python | tok_get_normal_mode |
| 0.04% | python | optimize_uops |
| 0.03% | python | _PyJIT_Compile |

### gil

0.12% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 0.11% | python | take_gil |

### async

0.06% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 0.03% | python | async_gen_asend_send |
| 0.02% | python | async_gen_unwrap_value.isra.0 |
| 0.00% | python | async_gen_init_hooks |
