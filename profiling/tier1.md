
## 2to3

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 29.92% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 2.30% | `python` | `type_new` | memory |
| 2.22% | `python` | `deduce_unreachable` | gc |
| 2.16% | `python` | `gc_collect_region.isra.0` | gc |
| 1.89% | `python` | `tuple_dealloc` | memory |
| 1.75% | `python` | `sre_ucs1_match` | library |
| 1.63% | `python` | `visit_decref` | gc |
| 1.59% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.48% | `python` | `intern_common.part.0` | str |
| 1.25% | `python` | `_PyCode_New` | interpreter |
| 1.09% | `python` | `PyDict_GetItemRef` | dict |
| 1.00% | `python` | `visit_reachable` | gc |
| 0.85% | `python` | `PyObject_GetAttr` | dynamic |
| 0.84% | `python` | `r_object` | import |
| 0.82% | `python` | `list_dealloc` | memory |
| 0.79% | `libc-2.31.so` | `__memcpy_avx_unaligned_erms` | libc |
| 0.77% | `python` | `_PyTuple_FromStackRefSteal` | tuple |
| 0.75% | `python` | `siphash13` | str |
| 0.64% | `python` | `PyObject_SetAttr` | dynamic |
| 0.63% | `python` | `gen_dealloc` | memory |
| 0.63% | `python` | `PyUnicode_FromKindAndData` | str |
| 0.62% | `python` | `dict_dealloc` | memory |
| 0.60% | `python` | `_Py_MakeCoro` | unknown |
| 0.60% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.49% | `python` | `unicode_dealloc` | memory |
| 0.45% | `python` | `subtype_traverse` | gc |
| 0.45% | `libc-2.31.so` | `_int_malloc` | libc |
| 0.45% | `python` | `insertdict` | dict |
| 0.43% | `python` | `PyDict_Contains` | dict |
| 0.43% | `python` | `tok_get_normal_mode` | compiler |
| 0.42% | `python` | `PyMem_Free` | memory |
| 0.42% | `python` | `find_name_in_mro` | lookup |
| 0.42% | `python` | `PyObject_GC_Del` | gc |
| 0.42% | `python` | `_PyObject_GetMethod` | dynamic |
| 0.42% | `python` | `_PyCfg_OptimizeCodeUnit.constprop.0` | unknown |
| 0.39% | `python` | `sre_ucs1_count` | library |
| 0.39% | `python` | `list_iter` | list |
| 0.38% | `python` | `_PyFunction_Vectorcall` | calls |
| 0.38% | `python` | `_PyPegen_fill_token` | interpreter |
| 0.36% | `python` | `dict_traverse` | gc |
| 0.35% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.35% | `python` | `sre_ucs2_charset.isra.0` | library |
| 0.34% | `python` | `dictresize` | dict |
| 0.34% | `python` | `list_subscript` | list |
| 0.34% | `python` | `type_ready` | dynamic |
| 0.33% | `python` | `insert_to_emptydict` | dict |
| 0.33% | `python` | `PyDict_SetItem` | dict |
| 0.32% | `python` | `_sre_SRE_Pattern_match` | library |
| 0.32% | `python` | `_PyLexer_update_fstring_expr` | unknown |
| 0.31% | `python` | `code_dealloc` | memory |
| 0.30% | `libc-2.31.so` | `__memcmp_avx2_movbe` | libc |
| 0.30% | `python` | `tuple_richcompare` | tuple |
| 0.29% | `python` | `PyMem_Malloc` | memory |
| 0.29% | `python` | `code_hash` | unknown |
| 0.28% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 0.27% | `python` | `_PyAssemble_MakeCodeObject` | unknown |
| 0.27% | `python` | `_PyObject_MakeTpCall` | dynamic |
| 0.27% | `python` | `subtype_dealloc` | memory |
| 0.25% | `libz.so.1.2.11` | `inflateBackEnd` | library |

## async_generators

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 21.20% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 8.73% | `python` | `_PyErr_SetObject` | exceptions |
| 4.49% | `python` | `StopIteration_dealloc` | memory |
| 3.89% | `python` | `BaseException_new` | memory |
| 3.62% | `python` | `_PyObject_MakeTpCall` | dynamic |
| 2.99% | `python` | `async_gen_asend_send` | async |
| 2.78% | `python` | `gen_send_ex` | unknown |
| 2.62% | `python` | `StopIteration_init` | dynamic |
| 2.29% | `python` | `async_gen_asend_dealloc` | memory |
| 2.21% | `python` | `async_gen_asend_new` | memory |
| 2.17% | `python` | `tuple_dealloc` | memory |
| 2.08% | `python` | `gen_send_ex2` | unknown |
| 1.91% | `python` | `PyErr_GivenExceptionMatches` | exceptions |
| 1.72% | `python` | `PyErr_ExceptionMatches` | exceptions |
| 1.62% | `python` | `_PyAsyncGenValueWrapperNew` | memory |
| 1.52% | `python` | `async_gen_wrapped_val_dealloc` | memory |
| 1.40% | `python` | `_PyEval_EvalFrameDefault.cold` | interpreter |
| 1.38% | `python` | `async_gen_unwrap_value.isra.0` | async |
| 1.08% | `python` | `long_add` | int |
| 1.07% | `python` | `_PyGen_FetchStopIterationValue.cold` | miscobj |
| 1.02% | `python` | `PyObject_CallFinalizerFromDealloc` | memory |
| 0.93% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.91% | `python` | `_PyGen_SetStopIterationValue` | miscobj |
| 0.87% | `python` | `type_call` | dynamic |
| 0.79% | `python` | `long_dealloc` | memory |
| 0.79% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.69% | `python` | `PyType_GenericAlloc` | memory |
| 0.69% | `python` | `deduce_unreachable` | gc |
| 0.62% | `python` | `visit_decref` | gc |
| 0.58% | `python` | `range_subscript` | miscobj |
| 0.56% | `python` | `visit_reachable` | gc |
| 0.55% | `python` | `subtype_dealloc` | memory |
| 0.48% | `python` | `_Py_Dealloc` | memory |
| 0.48% | `python` | `_PyFunction_Vectorcall` | calls |
| 0.46% | `python` | `subtype_traverse` | gc |
| 0.45% | `python` | `type_new` | memory |
| 0.43% | `python` | `gc_collect_region.isra.0` | gc |
| 0.42% | `python` | `PyTraceBack_Here` | exceptions |
| 0.41% | `python` | `visit_add_to_container` | gc |
| 0.40% | `python` | `_PyGen_FetchStopIterationValue` | miscobj |
| 0.38% | `python` | `make_range_object` | unknown |
| 0.38% | `python` | `gen_dealloc` | memory |
| 0.38% | `python` | `_Py_NewReference` | memory |
| 0.38% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.36% | `python` | `PyObject_CallOneArg` | dynamic |
| 0.36% | `python` | `_PyObject_New` | memory |
| 0.35% | `python` | `PyObject_ClearWeakRefs` | dynamic |
| 0.30% | `python` | `_PyFrame_MakeAndSetFrameObject` | unknown |
| 0.30% | `python` | `BaseException_dealloc` | memory |
| 0.30% | `python` | `BaseException_vectorcall` | exceptions |
| 0.28% | `python` | `weakref_dealloc` | memory |
| 0.27% | `python` | `async_gen_init_hooks` | async |
| 0.26% | `python` | `intern_common.part.0` | str |
| 0.25% | `python` | `_PyBuildSlice_Consume2` | unknown |
| 0.25% | `python` | `PyNumber_Add` | dynamic |

## async_tree

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 25.82% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 6.25% | `python` | `deduce_unreachable` | gc |
| 5.11% | `python` | `visit_add_to_container` | gc |
| 5.09% | `python` | `visit_decref` | gc |
| 5.08% | `python` | `visit_reachable` | gc |
| 4.26% | `python` | `gc_collect_region.isra.0` | gc |
| 2.28% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.42% | `python` | `_PyFunction_Vectorcall` | calls |
| 1.30% | `python` | `subtype_traverse` | gc |
| 1.17% | `python` | `_PyObject_GC_New` | gc |
| 1.15% | `python` | `tuple_dealloc` | memory |
| 1.08% | `python` | `PyObject_GC_Del` | gc |
| 1.04% | `python` | `PyObject_GetAttr` | dynamic |
| 1.04% | `python` | `PyObject_VectorcallMethod` | dynamic |
| 0.98% | `python` | `context_tp_dealloc` | memory |
| 0.86% | `python` | `gen_traverse` | gc |
| 0.81% | `python` | `_PyObject_MakeTpCall` | dynamic |
| 0.80% | `python` | `slot_tp_init` | unknown |
| 0.79% | `python` | `gen_dealloc` | memory |
| 0.74% | `python` | `list_dealloc` | memory |
| 0.74% | `python` | `PyType_GenericNew` | memory |
| 0.72% | `_asyncio.cpython-314-x86_64-linux-gnu.so` | `TaskObj_traverse` | library |
| 0.71% | `python` | `meth_dealloc` | memory |
| 0.70% | `python` | `PyDict_GetItemRef` | dict |
| 0.67% | `python` | `_PyObject_GC_NewVar` | gc |
| 0.63% | `python` | `_PyGC_Collect` | gc |
| 0.63% | `python` | `object_new` | memory |
| 0.61% | `python` | `type_new` | memory |
| 0.55% | `python` | `subtype_dealloc` | memory |
| 0.54% | `python` | `clear_slots` | unknown |
| 0.51% | `python` | `insertdict` | dict |
| 0.46% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.45% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.43% | `python` | `_PyArg_UnpackKeywords` | calls |
| 0.40% | `python` | `dict_traverse` | gc |
| 0.39% | `python` | `insert_to_emptydict` | dict |
| 0.38% | `python` | `PyObject_RichCompareBool` | dynamic |
| 0.37% | `python` | `list_resize` | list |
| 0.37% | `python` | `dict_dealloc` | memory |
| 0.37% | `python` | `PyLong_FromLong` | int |
| 0.36% | `python` | `method_get` | dynamic |
| 0.35% | `python` | `dict_setdefault_ref_lock_held` | dict |
| 0.33% | `python` | `intern_common.part.0` | str |
| 0.32% | `[kernel.kallsyms]` | `clear_page_erms` | kernel |
| 0.31% | `python` | `_PyCode_New` | interpreter |
| 0.31% | `python` | `PyObject_VisitManagedDict` | dynamic |
| 0.29% | `python` | `func_traverse` | gc |
| 0.27% | `[kernel.kallsyms]` | `native_irq_return_iret` | kernel |
| 0.27% | `python` | `dictresize` | dict |
| 0.27% | `python` | `PyObject_Vectorcall` | dynamic |
| 0.27% | `python` | `PyUnicode_RichCompare` | str |
| 0.26% | `_asyncio.cpython-314-x86_64-linux-gnu.so` | `TaskObj_clear` | library |
| 0.26% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.26% | `python` | `PyObject_SetAttr` | dynamic |
| 0.25% | `python` | `_Py_dict_lookup` | lookup |

## async_tree_cpu_io_mixed

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 21.53% | `python` | `k_mul` | int |
| 19.04% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 4.46% | `python` | `deduce_unreachable` | gc |
| 3.85% | `python` | `visit_decref` | gc |
| 3.44% | `python` | `visit_reachable` | gc |
| 3.34% | `python` | `visit_add_to_container` | gc |
| 2.99% | `python` | `long_dealloc` | memory |
| 2.89% | `python` | `gc_collect_region.isra.0` | gc |
| 1.54% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.39% | `python` | `_PyLong_New` | memory |
| 0.93% | `python` | `_PyFunction_Vectorcall` | calls |
| 0.92% | `python` | `subtype_traverse` | gc |
| 0.89% | `python` | `long_mul_method` | int |
| 0.77% | `python` | `PyObject_GetAttr` | dynamic |
| 0.77% | `python` | `context_tp_dealloc` | memory |
| 0.76% | `python` | `tuple_dealloc` | memory |
| 0.75% | `python` | `_PyObject_GC_New` | gc |
| 0.74% | `math.cpython-314-x86_64-linux-gnu.so` | `factorial_partial_product` | library |
| 0.69% | `python` | `PyObject_VectorcallMethod` | dynamic |
| 0.66% | `python` | `gen_dealloc` | memory |
| 0.58% | `python` | `PyObject_GC_Del` | gc |
| 0.58% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.55% | `python` | `gen_traverse` | gc |
| 0.54% | `python` | `meth_dealloc` | memory |
| 0.52% | `python` | `slot_tp_init` | unknown |
| 0.52% | `python` | `_PyObject_MakeTpCall` | dynamic |
| 0.51% | `python` | `list_dealloc` | memory |
| 0.50% | `math.cpython-314-x86_64-linux-gnu.so` | `math_factorial` | library |
| 0.49% | `python` | `_PyObject_GC_NewVar` | gc |
| 0.49% | `_asyncio.cpython-314-x86_64-linux-gnu.so` | `TaskObj_traverse` | library |
| 0.49% | `python` | `_PyGC_Collect` | gc |
| 0.46% | `python` | `PyDict_GetItemRef` | dict |
| 0.45% | `python` | `PyType_GenericNew` | memory |
| 0.44% | `python` | `object_new` | memory |
| 0.44% | `python` | `long_lshift_int64` | int |
| 0.43% | `python` | `subtype_dealloc` | memory |
| 0.38% | `python` | `clear_slots` | unknown |
| 0.37% | `python` | `type_new` | memory |
| 0.35% | `python` | `PyNumber_Multiply` | dynamic |
| 0.34% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.33% | `python` | `insertdict` | dict |
| 0.33% | `python` | `PyLong_FromUnsignedLong` | int |
| 0.28% | `python` | `PyObject_RichCompareBool` | dynamic |
| 0.27% | `python` | `insert_to_emptydict` | dict |
| 0.26% | `python` | `method_get` | dynamic |
| 0.26% | `python` | `list_resize` | list |
| 0.25% | `python` | `_PyArg_UnpackKeywords` | calls |

## async_tree_cpu_io_mixed_tg

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 21.94% | `python` | `k_mul` | int |
| 17.55% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 4.64% | `python` | `deduce_unreachable` | gc |
| 4.45% | `python` | `visit_add_to_container` | gc |
| 4.17% | `python` | `visit_decref` | gc |
| 3.82% | `python` | `visit_reachable` | gc |
| 3.15% | `python` | `long_dealloc` | memory |
| 3.00% | `python` | `gc_collect_region.isra.0` | gc |
| 1.50% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.41% | `python` | `_PyLong_New` | memory |
| 1.13% | `python` | `subtype_traverse` | gc |
| 0.91% | `python` | `PyObject_GetAttr` | dynamic |
| 0.89% | `python` | `long_mul_method` | int |
| 0.87% | `python` | `_PyFunction_Vectorcall` | calls |
| 0.78% | `python` | `gen_traverse` | gc |
| 0.74% | `math.cpython-314-x86_64-linux-gnu.so` | `factorial_partial_product` | library |
| 0.69% | `python` | `PyObject_VectorcallMethod` | dynamic |
| 0.68% | `python` | `PyObject_GC_Del` | gc |
| 0.68% | `python` | `tuple_dealloc` | memory |
| 0.63% | `python` | `_PyObject_GC_NewVar` | gc |
| 0.62% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.59% | `python` | `_PyObject_GC_New` | gc |
| 0.56% | `math.cpython-314-x86_64-linux-gnu.so` | `math_factorial` | library |
| 0.54% | `python` | `PyDict_GetItemRef` | dict |
| 0.52% | `python` | `gen_dealloc` | memory |
| 0.51% | `_asyncio.cpython-314-x86_64-linux-gnu.so` | `TaskObj_traverse` | library |
| 0.50% | `python` | `slot_tp_init` | unknown |
| 0.49% | `python` | `_PyGC_Collect` | gc |
| 0.48% | `python` | `long_lshift_int64` | int |
| 0.48% | `python` | `_PyObject_MakeTpCall` | dynamic |
| 0.46% | `python` | `meth_dealloc` | memory |
| 0.43% | `python` | `PyType_GenericNew` | memory |
| 0.42% | `python` | `object_new` | memory |
| 0.40% | `python` | `clear_slots` | unknown |
| 0.40% | `python` | `PyNumber_Multiply` | dynamic |
| 0.40% | `python` | `set_traverse` | gc |
| 0.37% | `python` | `subtype_dealloc` | memory |
| 0.35% | `python` | `PyLong_FromUnsignedLong` | int |
| 0.34% | `python` | `type_new` | memory |
| 0.34% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.33% | `python` | `list_dealloc` | memory |
| 0.29% | `python` | `dict_traverse` | gc |
| 0.29% | `python` | `PyObject_RichCompareBool` | dynamic |
| 0.26% | `python` | `_PyArg_UnpackKeywords` | calls |

## async_tree_io

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 23.74% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 8.57% | `python` | `deduce_unreachable` | gc |
| 7.63% | `python` | `visit_add_to_container` | gc |
| 7.10% | `python` | `visit_decref` | gc |
| 6.71% | `python` | `visit_reachable` | gc |
| 5.99% | `python` | `gc_collect_region.isra.0` | gc |
| 2.12% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.55% | `python` | `subtype_traverse` | gc |
| 1.48% | `python` | `gen_traverse` | gc |
| 1.15% | `python` | `slot_tp_richcompare` | dynamic |
| 0.97% | `python` | `_PyGC_Collect` | gc |
| 0.94% | `python` | `_PyFunction_Vectorcall` | calls |
| 0.87% | `python` | `tuple_dealloc` | memory |
| 0.80% | `python` | `PyObject_GetAttr` | dynamic |
| 0.75% | `python` | `_PyObject_GC_New` | gc |
| 0.69% | `python` | `PyObject_GC_Del` | gc |
| 0.63% | `python` | `PyObject_VectorcallMethod` | dynamic |
| 0.62% | `_heapq.cpython-314-x86_64-linux-gnu.so` | `_heapq_heappop` | library |
| 0.62% | `python` | `slot_tp_init` | unknown |
| 0.60% | `_asyncio.cpython-314-x86_64-linux-gnu.so` | `TaskObj_traverse` | library |
| 0.59% | `python` | `_PyObject_MakeTpCall` | dynamic |
| 0.53% | `python` | `PyObject_RichCompareBool` | dynamic |
| 0.52% | `python` | `gen_dealloc` | memory |
| 0.52% | `python` | `_PyObject_GC_NewVar` | gc |
| 0.51% | `python` | `PyType_GenericNew` | memory |
| 0.50% | `python` | `meth_dealloc` | memory |
| 0.49% | `python` | `object_new` | memory |
| 0.47% | `python` | `list_dealloc` | memory |
| 0.43% | `python` | `clear_slots` | unknown |
| 0.40% | `python` | `list_resize` | list |
| 0.39% | `python` | `context_tp_dealloc` | memory |
| 0.39% | `python` | `PyDict_GetItemRef` | dict |
| 0.39% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.36% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.36% | `python` | `subtype_dealloc` | memory |
| 0.34% | `python` | `_PyObject_Call` | dynamic |
| 0.33% | `python` | `_PySuper_Lookup` | dynamic |
| 0.32% | `python` | `insert_to_emptydict` | dict |
| 0.32% | `_asyncio.cpython-314-x86_64-linux-gnu.so` | `FutureObj_traverse` | library |
| 0.31% | `python` | `PyObject_VisitManagedDict` | dynamic |
| 0.30% | `[kernel.kallsyms]` | `clear_page_erms` | kernel |
| 0.28% | `python` | `dict_traverse` | gc |
| 0.27% | `python` | `tuple_traverse` | gc |
| 0.26% | `python` | `method_get` | dynamic |
| 0.26% | `python` | `PyLong_FromLong` | int |
| 0.25% | `python` | `_PyArg_UnpackKeywords` | calls |
| 0.25% | `python` | `dict_dealloc` | memory |

## async_tree_io_tg

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 20.84% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 9.61% | `python` | `deduce_unreachable` | gc |
| 9.25% | `python` | `visit_add_to_container` | gc |
| 7.80% | `python` | `visit_decref` | gc |
| 7.55% | `python` | `visit_reachable` | gc |
| 6.81% | `python` | `gc_collect_region.isra.0` | gc |
| 2.06% | `python` | `gen_traverse` | gc |
| 1.77% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.65% | `python` | `subtype_traverse` | gc |
| 1.21% | `python` | `_PyGC_Collect` | gc |
| 1.10% | `python` | `_PyFunction_Vectorcall` | calls |
| 1.04% | `python` | `slot_tp_richcompare` | dynamic |
| 0.84% | `python` | `PyObject_GetAttr` | dynamic |
| 0.79% | `python` | `tuple_dealloc` | memory |
| 0.76% | `python` | `gen_dealloc` | memory |
| 0.70% | `_asyncio.cpython-314-x86_64-linux-gnu.so` | `TaskObj_traverse` | library |
| 0.61% | `_heapq.cpython-314-x86_64-linux-gnu.so` | `_heapq_heappop` | library |
| 0.59% | `python` | `PyObject_GC_Del` | gc |
| 0.56% | `python` | `PyObject_VectorcallMethod` | dynamic |
| 0.54% | `python` | `_PyObject_GC_New` | gc |
| 0.54% | `python` | `_PyObject_GC_NewVar` | gc |
| 0.52% | `python` | `slot_tp_init` | unknown |
| 0.52% | `python` | `set_traverse` | gc |
| 0.48% | `python` | `_PyObject_MakeTpCall` | dynamic |
| 0.47% | `python` | `PyObject_RichCompareBool` | dynamic |
| 0.47% | `python` | `object_new` | memory |
| 0.46% | `python` | `meth_dealloc` | memory |
| 0.44% | `python` | `subtype_dealloc` | memory |
| 0.43% | `python` | `PyType_GenericNew` | memory |
| 0.41% | `python` | `PyDict_GetItemRef` | dict |
| 0.40% | `python` | `clear_slots` | unknown |
| 0.36% | `python` | `list_dealloc` | memory |
| 0.35% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.34% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.34% | `_asyncio.cpython-314-x86_64-linux-gnu.so` | `FutureObj_traverse` | library |
| 0.32% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.31% | `[kernel.kallsyms]` | `clear_page_erms` | kernel |
| 0.30% | `python` | `_PyObject_Call` | dynamic |
| 0.27% | `python` | `PyObject_VisitManagedDict` | dynamic |
| 0.27% | `python` | `list_resize` | list |
| 0.27% | `[kernel.kallsyms]` | `native_irq_return_iret` | kernel |
| 0.26% | `python` | `insert_to_emptydict` | dict |
| 0.26% | `python` | `PyLong_FromLong` | int |
| 0.26% | `python` | `_PySuper_Lookup` | dynamic |

## async_tree_memoization

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 27.52% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 6.69% | `python` | `deduce_unreachable` | gc |
| 5.46% | `python` | `visit_decref` | gc |
| 5.00% | `python` | `visit_reachable` | gc |
| 4.98% | `python` | `visit_add_to_container` | gc |
| 4.20% | `python` | `gc_collect_region.isra.0` | gc |
| 2.40% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.38% | `python` | `subtype_traverse` | gc |
| 1.30% | `python` | `_PyFunction_Vectorcall` | calls |
| 1.24% | `python` | `PyObject_GetAttr` | dynamic |
| 1.06% | `python` | `tuple_dealloc` | memory |
| 1.04% | `python` | `_PyObject_GC_New` | gc |
| 0.95% | `python` | `context_tp_dealloc` | memory |
| 0.91% | `python` | `PyObject_VectorcallMethod` | dynamic |
| 0.86% | `python` | `gen_traverse` | gc |
| 0.85% | `python` | `PyObject_GC_Del` | gc |
| 0.79% | `python` | `gen_dealloc` | memory |
| 0.74% | `python` | `meth_dealloc` | memory |
| 0.73% | `python` | `slot_tp_init` | unknown |
| 0.72% | `python` | `list_dealloc` | memory |
| 0.72% | `python` | `_PyObject_MakeTpCall` | dynamic |
| 0.70% | `python` | `_PyGC_Collect` | gc |
| 0.66% | `_asyncio.cpython-314-x86_64-linux-gnu.so` | `TaskObj_traverse` | library |
| 0.63% | `python` | `_PyObject_GC_NewVar` | gc |
| 0.62% | `python` | `PyDict_GetItemRef` | dict |
| 0.61% | `python` | `PyType_GenericNew` | memory |
| 0.58% | `python` | `object_new` | memory |
| 0.57% | `python` | `clear_slots` | unknown |
| 0.52% | `python` | `subtype_dealloc` | memory |
| 0.50% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.48% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.45% | `python` | `method_get` | dynamic |
| 0.45% | `python` | `insertdict` | dict |
| 0.45% | `python` | `type_new` | memory |
| 0.39% | `python` | `list_resize` | list |
| 0.39% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.39% | `python` | `PyObject_RichCompareBool` | dynamic |
| 0.38% | `python` | `PyObject_SetAttr` | dynamic |
| 0.38% | `python` | `insert_to_emptydict` | dict |
| 0.36% | `python` | `_PyArg_UnpackKeywords` | calls |
| 0.33% | `python` | `dict_traverse` | gc |
| 0.33% | `python` | `PyIter_Send` | dynamic |
| 0.32% | `python` | `PyLong_FromLong` | int |
| 0.30% | `python` | `dict_setdefault_ref_lock_held` | dict |
| 0.29% | `python` | `dict_dealloc` | memory |
| 0.26% | `python` | `func_traverse` | gc |
| 0.26% | `python` | `PyObject_VisitManagedDict` | dynamic |
| 0.26% | `python` | `tuple_traverse` | gc |
| 0.26% | `python` | `dictresize` | dict |
| 0.26% | `python` | `_PyObject_Call` | dynamic |
| 0.25% | `_asyncio.cpython-314-x86_64-linux-gnu.so` | `task_step_impl` | library |
| 0.25% | `python` | `PyUnicode_RichCompare` | str |

## async_tree_memoization_tg

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 25.44% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 6.99% | `python` | `deduce_unreachable` | gc |
| 6.36% | `python` | `visit_add_to_container` | gc |
| 6.13% | `python` | `visit_decref` | gc |
| 5.59% | `python` | `visit_reachable` | gc |
| 4.58% | `python` | `gc_collect_region.isra.0` | gc |
| 2.25% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.60% | `python` | `subtype_traverse` | gc |
| 1.45% | `python` | `PyObject_GetAttr` | dynamic |
| 1.15% | `python` | `_PyFunction_Vectorcall` | calls |
| 1.10% | `python` | `gen_traverse` | gc |
| 1.00% | `python` | `tuple_dealloc` | memory |
| 0.93% | `python` | `PyObject_GC_Del` | gc |
| 0.93% | `python` | `PyObject_VectorcallMethod` | dynamic |
| 0.83% | `python` | `_PyObject_GC_New` | gc |
| 0.83% | `python` | `_PyObject_GC_NewVar` | gc |
| 0.74% | `python` | `PyDict_GetItemRef` | dict |
| 0.74% | `_asyncio.cpython-314-x86_64-linux-gnu.so` | `TaskObj_traverse` | library |
| 0.70% | `python` | `slot_tp_init` | unknown |
| 0.68% | `python` | `gen_dealloc` | memory |
| 0.68% | `python` | `_PyGC_Collect` | gc |
| 0.66% | `python` | `_PyObject_MakeTpCall` | dynamic |
| 0.66% | `python` | `meth_dealloc` | memory |
| 0.60% | `python` | `PyType_GenericNew` | memory |
| 0.59% | `python` | `object_new` | memory |
| 0.57% | `python` | `clear_slots` | unknown |
| 0.55% | `python` | `set_traverse` | gc |
| 0.54% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.50% | `python` | `subtype_dealloc` | memory |
| 0.50% | `python` | `type_new` | memory |
| 0.47% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.44% | `python` | `list_dealloc` | memory |
| 0.42% | `python` | `method_get` | dynamic |
| 0.39% | `python` | `PyObject_RichCompareBool` | dynamic |
| 0.35% | `python` | `set_discard_entry` | miscobj |
| 0.35% | `python` | `context_tp_dealloc` | memory |
| 0.35% | `python` | `_PyArg_UnpackKeywords` | calls |
| 0.33% | `python` | `dict_traverse` | gc |
| 0.32% | `python` | `PyIter_Send` | dynamic |
| 0.30% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.30% | `python` | `insertdict` | dict |
| 0.29% | `python` | `dict_setdefault_ref_lock_held` | dict |
| 0.29% | `python` | `PyLong_FromLong` | int |
| 0.28% | `python` | `intern_common.part.0` | str |
| 0.27% | `_asyncio.cpython-314-x86_64-linux-gnu.so` | `task_step_impl` | library |
| 0.27% | `python` | `method_vectorcall` | calls |
| 0.27% | `python` | `PyUnicode_RichCompare` | str |
| 0.26% | `python` | `dict_dealloc` | memory |
| 0.26% | `python` | `insert_to_emptydict` | dict |
| 0.26% | `python` | `_PyCode_New` | interpreter |
| 0.25% | `python` | `_Py_dict_lookup` | lookup |

## async_tree_tg

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 24.24% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 6.53% | `python` | `visit_add_to_container` | gc |
| 6.38% | `python` | `deduce_unreachable` | gc |
| 5.60% | `python` | `visit_decref` | gc |
| 5.53% | `python` | `visit_reachable` | gc |
| 4.34% | `python` | `gc_collect_region.isra.0` | gc |
| 2.16% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.43% | `python` | `subtype_traverse` | gc |
| 1.33% | `python` | `PyObject_GetAttr` | dynamic |
| 1.21% | `python` | `_PyFunction_Vectorcall` | calls |
| 1.19% | `python` | `PyObject_GC_Del` | gc |
| 1.12% | `python` | `gen_traverse` | gc |
| 1.01% | `python` | `tuple_dealloc` | memory |
| 0.99% | `python` | `PyObject_VectorcallMethod` | dynamic |
| 0.95% | `python` | `_PyObject_GC_NewVar` | gc |
| 0.92% | `python` | `PyDict_GetItemRef` | dict |
| 0.89% | `python` | `_PyObject_GC_New` | gc |
| 0.81% | `python` | `slot_tp_init` | unknown |
| 0.79% | `python` | `_PyObject_MakeTpCall` | dynamic |
| 0.72% | `_asyncio.cpython-314-x86_64-linux-gnu.so` | `TaskObj_traverse` | library |
| 0.71% | `python` | `PyType_GenericNew` | memory |
| 0.65% | `python` | `meth_dealloc` | memory |
| 0.64% | `python` | `_PyGC_Collect` | gc |
| 0.62% | `python` | `object_new` | memory |
| 0.61% | `python` | `type_new` | memory |
| 0.59% | `python` | `gen_dealloc` | memory |
| 0.54% | `python` | `set_traverse` | gc |
| 0.54% | `python` | `subtype_dealloc` | memory |
| 0.51% | `python` | `clear_slots` | unknown |
| 0.47% | `[kernel.kallsyms]` | `clear_page_erms` | kernel |
| 0.47% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.46% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.41% | `[kernel.kallsyms]` | `native_irq_return_iret` | kernel |
| 0.41% | `python` | `list_dealloc` | memory |
| 0.39% | `python` | `PyObject_RichCompareBool` | dynamic |
| 0.39% | `python` | `insertdict` | dict |
| 0.38% | `python` | `_PyArg_UnpackKeywords` | calls |
| 0.38% | `python` | `PyLong_FromLong` | int |
| 0.37% | `python` | `dict_traverse` | gc |
| 0.35% | `python` | `intern_common.part.0` | str |
| 0.33% | `[kernel.kallsyms]` | `sync_regs` | kernel |
| 0.33% | `python` | `dict_setdefault_ref_lock_held` | dict |
| 0.32% | `python` | `_PyCode_New` | interpreter |
| 0.31% | `python` | `dict_dealloc` | memory |
| 0.31% | `python` | `method_get` | dynamic |
| 0.30% | `[kernel.kallsyms]` | `rmqueue` | kernel |
| 0.28% | `python` | `insert_to_emptydict` | dict |
| 0.27% | `python` | `long_dealloc` | memory |
| 0.27% | `python` | `_Py_dict_lookup` | lookup |
| 0.27% | `python` | `PyUnicode_RichCompare` | str |
| 0.27% | `python` | `allocate_from_new_pool` | memory |
| 0.27% | `python` | `PyLong_FromUnsignedLongLong` | int |
| 0.26% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.26% | `python` | `method_vectorcall` | calls |
| 0.25% | `python` | `PyObject_VisitManagedDict` | dynamic |

## asyncio_websockets

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 65.43% | `libz.so.1.2.11` | `crc32_combine64` | library |
| 20.67% | `libz.so.1.2.11` | `inflateBackEnd` | library |
| 2.61% | `libc-2.31.so` | `__memcpy_avx_unaligned_erms` | libc |
| 1.60% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 0.42% | `python` | `type_new` | memory |
| 0.41% | `libz.so.1.2.11` | `inflateCodesUsed` | library |
| 0.26% | `python` | `deduce_unreachable` | gc |
| 0.26% | `python` | `intern_common.part.0` | str |

## bpe_tokeniser

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 30.84% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 6.50% | `python` | `tuple_dealloc` | memory |
| 5.75% | `python` | `list_dealloc` | memory |
| 3.77% | `python` | `dict_subscript` | dict |
| 2.70% | `python` | `zip_new` | memory |
| 2.46% | `python` | `_PyObject_MakeTpCall` | dynamic |
| 2.17% | `python` | `list_subscript` | list |
| 2.09% | `python` | `list_iter` | list |
| 2.04% | `python` | `insertdict` | dict |
| 1.91% | `python` | `listiter_dealloc` | memory |
| 1.71% | `python` | `zip_next` | unknown |
| 1.68% | `python` | `listiter_next` | list |
| 1.61% | `python` | `slot_mp_subscript` | unknown |
| 1.50% | `python` | `PyList_New` | memory |
| 1.45% | `python` | `zip_dealloc` | memory |
| 1.45% | `python` | `tuple_hash` | tuple |
| 1.44% | `python` | `deduce_unreachable` | gc |
| 1.41% | `python` | `wrapperdescr_call` | unknown |
| 1.38% | `python` | `tuple_richcompare` | tuple |
| 1.24% | `python` | `list_traverse` | gc |
| 1.23% | `python` | `visit_reachable` | gc |
| 1.18% | `python` | `visit_decref` | gc |
| 1.12% | `python` | `slot_mp_ass_subscript` | unknown |
| 1.03% | `python` | `long_add` | int |
| 1.01% | `python` | `long_sub` | int |
| 0.85% | `python` | `PyObject_RichCompare` | dynamic |
| 0.77% | `python` | `gc_collect_region.isra.0` | gc |
| 0.76% | `python` | `PyObject_GetItem` | dynamic |
| 0.73% | `python` | `_PyObject_GC_New` | gc |
| 0.70% | `python` | `_PyObject_LookupSpecial` | dynamic |
| 0.70% | `python` | `_PyTuple_FromStackRefSteal` | tuple |
| 0.69% | `python` | `PyMem_Malloc` | memory |
| 0.69% | `python` | `wrap_objobjargproc` | unknown |
| 0.67% | `python` | `PyObject_GC_Del` | gc |
| 0.66% | `python` | `list_resize` | list |
| 0.64% | `python` | `visit_add_to_container` | gc |
| 0.56% | `python` | `PyTuple_New` | memory |
| 0.53% | `python` | `_PyObject_Malloc` | memory |
| 0.53% | `python` | `method_vectorcall_O` | calls |
| 0.50% | `python` | `PyNumber_AsSsize_t` | dynamic |
| 0.50% | `python` | `method_dealloc` | memory |
| 0.46% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.46% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.45% | `python` | `PyArg_UnpackTuple` | calls |
| 0.45% | `python` | `dictiter_iternextkey` | dict |
| 0.40% | `python` | `func_descr_get` | unknown |
| 0.36% | `python` | `bytes_richcompare` | str |
| 0.34% | `python` | `_PyFunction_Vectorcall` | calls |
| 0.33% | `python` | `PyObject_SetItem` | dynamic |
| 0.29% | `python` | `tuple_traverse` | gc |
| 0.29% | `python` | `method_vectorcall` | calls |
| 0.29% | `python` | `dict_traverse` | gc |
| 0.28% | `python` | `type_call` | dynamic |
| 0.28% | `python` | `PyObject_Vectorcall` | dynamic |
| 0.27% | `python` | `_PyEvalFramePushAndInit` | interpreter |

## chaos

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 49.04% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 3.20% | `python` | `_PyFloat_FromDouble_ConsumeInputs` | float |
| 2.92% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 2.23% | `python` | `long_sub` | int |
| 1.50% | `python` | `subtype_dealloc` | memory |
| 1.47% | `python` | `range_vectorcall` | miscobj |
| 1.43% | `python` | `long_add` | int |
| 1.41% | `python` | `PyType_GenericAlloc` | memory |
| 1.27% | `python` | `float_div` | float |
| 1.16% | `python` | `float_sub` | float |
| 1.12% | `python` | `type_new` | memory |
| 1.04% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.95% | `libm-2.31.so` | `__ieee754_pow_fma` | library |
| 0.95% | `python` | `PyNumber_TrueDivide` | dynamic |
| 0.93% | `python` | `range_iter` | miscobj |
| 0.84% | `python` | `PyNumber_Subtract` | dynamic |
| 0.83% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.83% | `python` | `PyLong_AsDouble` | int |
| 0.80% | `python` | `PyObject_GC_Del` | gc |
| 0.73% | `python` | `float_richcompare` | float |
| 0.71% | `python` | `deduce_unreachable` | gc |
| 0.68% | `python` | `float_pow` | float |
| 0.68% | `python` | `float_dealloc` | memory |
| 0.67% | `python` | `intern_common.part.0` | str |
| 0.63% | `python` | `tuple_dealloc` | memory |
| 0.61% | `python` | `PyObject_Free` | dynamic |
| 0.61% | `python` | `_PyCode_New` | interpreter |
| 0.60% | `python` | `range_dealloc` | memory |
| 0.58% | `python` | `visit_decref` | gc |
| 0.54% | `python` | `PyLong_FromLong` | int |
| 0.54% | `python` | `convert_to_double` | unknown |
| 0.51% | `python` | `PyObject_RichCompare` | dynamic |
| 0.49% | `python` | `vectorcall_maybe.constprop.0` | unknown |
| 0.48% | `python` | `gc_collect_region.isra.0` | gc |
| 0.45% | `python` | `list_dealloc` | memory |
| 0.43% | `python` | `r_object` | import |
| 0.38% | `python` | `visit_reachable` | gc |
| 0.35% | `python` | `PyUnicode_FromKindAndData` | str |
| 0.28% | `python` | `PyType_IsSubtype` | dynamic |
| 0.26% | `python` | `float_mul` | float |
| 0.25% | `python` | `siphash13` | str |

## comprehensions

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 45.64% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 4.36% | `python` | `dict_get` | dict |
| 2.61% | `python` | `list_resize` | list |
| 2.32% | `python` | `PyFunction_NewWithQualName` | memory |
| 2.04% | `python` | `PyDict_GetItemRef` | dict |
| 1.93% | `python` | `list_dealloc` | memory |
| 1.70% | `python` | `list_iter` | list |
| 1.63% | `python` | `unsafe_tuple_compare` | unknown |
| 1.55% | `python` | `gen_dealloc` | memory |
| 1.46% | `python` | `insertdict` | dict |
| 1.45% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.35% | `python` | `func_dealloc` | memory |
| 1.09% | `python` | `_Py_MakeCoro` | unknown |
| 1.06% | `python` | `type_new` | memory |
| 1.00% | `python` | `PyObject_GC_Del` | gc |
| 0.99% | `python` | `tuple_dealloc` | memory |
| 0.95% | `python` | `long_richcompare` | int |
| 0.90% | `python` | `PyObject_RichCompare` | dynamic |
| 0.89% | `python` | `listiter_dealloc` | memory |
| 0.80% | `python` | `long_hash` | int |
| 0.72% | `python` | `_PyObject_Malloc` | memory |
| 0.70% | `python` | `deduce_unreachable` | gc |
| 0.67% | `python` | `_PyTuple_FromStackRefSteal` | tuple |
| 0.63% | `python` | `_PyCode_New` | interpreter |
| 0.63% | `python` | `list_sort_impl` | list |
| 0.62% | `python` | `PyObject_GetIter` | dynamic |
| 0.62% | `libc-2.31.so` | `__memcpy_avx_unaligned_erms` | libc |
| 0.62% | `python` | `dictresize` | dict |
| 0.60% | `python` | `_Py_type_getattro` | lookup |
| 0.59% | `python` | `intern_common.part.0` | str |
| 0.51% | `python` | `gen_close` | unknown |
| 0.48% | `python` | `gc_collect_region.isra.0` | gc |
| 0.48% | `python` | `visit_decref` | gc |
| 0.48% | `python` | `PyObject_GetAttr` | dynamic |
| 0.45% | `python` | `r_object` | import |
| 0.43% | `python` | `builtin_any` | unknown |
| 0.43% | `python` | `dict_dealloc` | memory |
| 0.40% | `python` | `unsafe_object_compare` | unknown |
| 0.39% | `python` | `visit_reachable` | gc |
| 0.38% | `python` | `PyObject_Hash` | dynamic |
| 0.38% | `python` | `gen_iternext` | miscobj |
| 0.36% | `python` | `tuple_subscript` | tuple |
| 0.34% | `python` | `PyList_New` | memory |
| 0.30% | `python` | `PyUnicode_FromKindAndData` | str |
| 0.29% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.28% | `python` | `object_richcompare` | dynamic |
| 0.26% | `python` | `insert_to_emptydict` | dict |
| 0.25% | `python` | `PyNumber_AsSsize_t` | dynamic |

## concurrent_imap

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 15.67% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 2.78% | `python` | `type_new` | memory |
| 2.08% | `[kernel.kallsyms]` | `memset_erms` | kernel |
| 1.71% | `python` | `intern_common.part.0` | str |
| 1.45% | `python` | `_PyCode_New` | interpreter |
| 1.36% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.98% | `python` | `r_object` | import |
| 0.85% | `python` | `deduce_unreachable` | gc |
| 0.80% | `python` | `tuple_dealloc` | memory |
| 0.80% | `python` | `PyUnicode_FromKindAndData` | str |
| 0.74% | `[kernel.kallsyms]` | `page_counter_cancel` | kernel |
| 0.71% | `[kernel.kallsyms]` | `clear_page_erms` | kernel |
| 0.70% | `python` | `visit_decref` | gc |
| 0.70% | `python` | `PyDict_GetItemRef` | dict |
| 0.66% | `python` | `PyObject_GetAttr` | dynamic |
| 0.65% | `libc-2.31.so` | `__memcpy_avx_unaligned_erms` | libc |
| 0.60% | `python` | `siphash13` | str |
| 0.58% | `[kernel.kallsyms]` | `zap_pte_range.isra.0` | kernel |
| 0.56% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.52% | `[kernel.kallsyms]` | `_raw_spin_lock` | kernel |
| 0.51% | `python` | `visit_reachable` | gc |
| 0.50% | `python` | `find_name_in_mro` | lookup |
| 0.49% | `python` | `insertdict` | dict |
| 0.49% | `python` | `gc_collect_region.isra.0` | gc |
| 0.47% | `libc-2.31.so` | `_int_malloc` | libc |
| 0.44% | `[kernel.kallsyms]` | `clear_bhb_loop` | kernel |
| 0.42% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.42% | `python` | `list_dealloc` | memory |
| 0.40% | `python` | `type_ready` | dynamic |
| 0.39% | `[kernel.kallsyms]` | `memcpy_erms` | kernel |
| 0.38% | `[kernel.kallsyms]` | `__d_lookup_rcu` | kernel |
| 0.38% | `python` | `unicode_dealloc` | memory |
| 0.38% | `[kernel.kallsyms]` | `copy_page` | kernel |
| 0.38% | `[kernel.kallsyms]` | `generic_permission` | kernel |
| 0.37% | `libpthread-2.31.so` | `pthread_create@@GLIBC_2.2.5` | library |
| 0.37% | `python` | `vgetargskeywords.constprop.0` | calls |
| 0.36% | `[kernel.kallsyms]` | `psi_task_change` | kernel |
| 0.36% | `[kernel.kallsyms]` | `perf_event_alloc` | kernel |
| 0.35% | `python` | `PyObject_SetAttr` | dynamic |
| 0.34% | `libc-2.31.so` | `__libc_malloc` | libc |
| 0.34% | `[kernel.kallsyms]` | `copy_process` | kernel |
| 0.33% | `python` | `dict_dealloc` | memory |
| 0.32% | `[kernel.kallsyms]` | `native_flush_tlb_one_user` | kernel |
| 0.32% | `python` | `PyMem_Free` | memory |
| 0.32% | `python` | `_PyObject_MakeTpCall` | dynamic |
| 0.31% | `python` | `PyObject_GC_Del` | gc |
| 0.31% | `[kernel.kallsyms]` | `kmem_cache_alloc` | kernel |
| 0.30% | `[kernel.kallsyms]` | `copy_user_enhanced_fast_string` | kernel |
| 0.30% | `python` | `_Py_dict_lookup` | lookup |
| 0.29% | `python` | `subtype_dealloc` | memory |
| 0.29% | `python` | `PyDict_SetItem` | dict |
| 0.29% | `[kernel.kallsyms]` | `__queue_work` | kernel |
| 0.28% | `libc-2.31.so` | `_int_free` | libc |
| 0.28% | `python` | `dictresize` | dict |
| 0.27% | `[kernel.kallsyms]` | `_raw_spin_lock_irqsave` | kernel |
| 0.27% | `python` | `_PyEval_LoadGlobalStackRef` | interpreter |
| 0.27% | `[kernel.kallsyms]` | `inode_permission` | kernel |
| 0.27% | `python` | `PyObject_Vectorcall` | dynamic |
| 0.27% | `[kernel.kallsyms]` | `native_sched_clock` | kernel |
| 0.26% | `python` | `PyFunction_NewWithQualName` | memory |
| 0.26% | `[kernel.kallsyms]` | `find_vma` | kernel |
| 0.26% | `[kernel.kallsyms]` | `syscall_return_via_sysret` | kernel |
| 0.26% | `python` | `PyType_GenericAlloc` | memory |
| 0.26% | `python` | `PyBytes_FromStringAndSize` | str |
| 0.25% | `python` | `take_gil` | gil |

## coroutines

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 45.34% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 13.34% | `python` | `gen_dealloc` | memory |
| 7.45% | `python` | `_PyObject_GC_NewVar` | gc |
| 4.67% | `python` | `_PyEval_EvalFrameDefault.cold` | interpreter |
| 3.47% | `python` | `make_gen` | miscobj |
| 2.74% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 2.37% | `python` | `long_sub` | int |
| 2.29% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 2.03% | `python` | `_Py_MakeCoro` | unknown |
| 1.70% | `python` | `long_add` | int |
| 1.56% | `python` | `_PyEval_GetAwaitable` | interpreter |
| 1.13% | `python` | `_PyCoro_GetAwaitableIter` | unknown |
| 0.85% | `python` | `type_new` | memory |
| 0.47% | `python` | `deduce_unreachable` | gc |
| 0.46% | `python` | `_PyGen_yf` | miscobj |
| 0.46% | `python` | `_PyCode_New` | interpreter |
| 0.43% | `python` | `intern_common.part.0` | str |
| 0.38% | `python` | `visit_decref` | gc |
| 0.34% | `python` | `gc_collect_region.isra.0` | gc |
| 0.31% | `python` | `r_object` | import |
| 0.25% | `python` | `visit_reachable` | gc |

## coverage

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 21.39% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 8.41% | `tracer.cpython-314-x86_64-linux-gnu.so` | `CTracer_trace` | library |
| 4.94% | `python` | `intern_common.part.0` | str |
| 3.71% | `python` | `call_instrumentation_vector` | interpreter |
| 3.58% | `python` | `siphash13` | str |
| 3.16% | `python` | `PyUnicode_InternFromString` | str |
| 2.78% | `python` | `frame_dealloc` | memory |
| 2.69% | `python` | `PySet_Add` | miscobj |
| 2.69% | `python` | `_Py_dict_lookup` | lookup |
| 2.58% | `python` | `PyObject_SetAttr` | dynamic |
| 2.57% | `python` | `_PyObject_VectorcallTstate.lto_priv.1` | dynamic |
| 2.05% | `python` | `_PyFrame_MakeAndSetFrameObject` | unknown |
| 1.94% | `python` | `call_one_instrument` | unknown |
| 1.90% | `python` | `PyLong_FromLong` | int |
| 1.83% | `python` | `dict_getitem` | dict |
| 1.72% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.64% | `python` | `_PyEval_LoadGlobalStackRef` | interpreter |
| 1.45% | `python` | `unicode_dealloc` | memory |
| 1.26% | `python` | `call_trace_func.isra.0` | unknown |
| 1.03% | `python` | `type_new` | memory |
| 0.71% | `python` | `_PyCode_GetCode` | interpreter |
| 0.65% | `python` | `long_sub` | int |
| 0.63% | `python` | `deduce_unreachable` | gc |
| 0.63% | `python` | `visit_decref` | gc |
| 0.61% | `libc-2.31.so` | `__memcmp_avx2_movbe` | libc |
| 0.60% | `python` | `long_add` | int |
| 0.59% | `tracer.cpython-314-x86_64-linux-gnu.so` | `CTracer_set_pdata_stack` | library |
| 0.57% | `python` | `gc_collect_region.isra.0` | gc |
| 0.56% | `python` | `PyEval_GetFrame` | interpreter |
| 0.56% | `python` | `_PyCode_New` | interpreter |
| 0.51% | `python` | `long_hash` | int |
| 0.50% | `python` | `visit_reachable` | gc |
| 0.48% | `python` | `hashtable_unicode_hash` | unknown |
| 0.47% | `python` | `_Py_CheckFunctionResult` | calls |
| 0.47% | `python` | `PyFrame_GetCode` | exceptions |
| 0.46% | `python` | `_Py_call_instrumentation_arg` | unknown |
| 0.42% | `libc-2.31.so` | `__memcpy_avx_unaligned_erms` | libc |
| 0.41% | `python` | `frame_settrace` | unknown |
| 0.41% | `python` | `r_object` | import |
| 0.41% | `python` | `PyObject_SetAttrString` | dynamic |
| 0.39% | `python` | `_PyEval_GetFrame` | interpreter |
| 0.38% | `python` | `PyFrame_GetLineNumber` | exceptions |
| 0.37% | `libc-2.31.so` | `__strlen_avx2` | libc |
| 0.32% | `python` | `getset_set` | unknown |
| 0.30% | `python` | `PyUnicode_FromKindAndData` | str |
| 0.26% | `python` | `compute_line` | unknown |

## crypto_pyaes

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 37.19% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 8.53% | `python` | `long_dealloc` | memory |
| 7.46% | `python` | `long_bitwise` | int |
| 4.81% | `python` | `long_rshift` | int |
| 3.89% | `python` | `long_mod` | int |
| 3.70% | `python` | `long_and` | int |
| 2.54% | `python` | `_PyLong_New` | memory |
| 1.64% | `python` | `binary_op` | unknown |
| 1.24% | `python` | `long_add` | int |
| 1.13% | `python` | `PyNumber_And` | dynamic |
| 1.09% | `python` | `type_new` | memory |
| 1.04% | `python` | `list_dealloc` | memory |
| 0.81% | `python` | `PyNumber_Remainder` | dynamic |
| 0.79% | `python` | `long_xor` | int |
| 0.78% | `python` | `maybe_small_long` | unknown |
| 0.74% | `python` | `range_vectorcall` | miscobj |
| 0.73% | `python` | `PyNumber_Rshift` | dynamic |
| 0.64% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.63% | `python` | `_PyLong_FromSTwoDigits` | int |
| 0.60% | `python` | `_PyObject_Free` | memory |
| 0.57% | `python` | `intern_common.part.0` | str |
| 0.57% | `python` | `_PyCode_New` | interpreter |
| 0.53% | `python` | `range_iter` | miscobj |
| 0.53% | `python` | `visit_decref` | gc |
| 0.52% | `python` | `deduce_unreachable` | gc |
| 0.52% | `python` | `gc_collect_region.isra.0` | gc |
| 0.48% | `python` | `PyLong_FromLong` | int |
| 0.47% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.44% | `libc-2.31.so` | `__memcpy_avx_unaligned_erms` | libc |
| 0.39% | `python` | `visit_reachable` | gc |
| 0.38% | `python` | `r_object` | import |
| 0.36% | `python` | `PyObject_Free` | dynamic |
| 0.33% | `python` | `dict_get` | dict |
| 0.32% | `python` | `PyUnicode_FromKindAndData` | str |
| 0.25% | `python` | `siphash13` | str |
| 0.25% | `python` | `range_dealloc` | memory |

## deepcopy

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 42.02% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 4.38% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 3.97% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 2.15% | `python` | `dict_get` | dict |
| 1.88% | `python` | `long_dealloc` | memory |
| 1.83% | `python` | `insertdict` | dict |
| 1.63% | `python` | `_PyLong_New` | memory |
| 1.46% | `python` | `set_contains_lock_held` | miscobj |
| 1.32% | `python` | `PyDict_GetItemRef` | dict |
| 1.18% | `python` | `tuple_dealloc` | memory |
| 1.04% | `python` | `insert_to_emptydict` | dict |
| 0.99% | `python` | `list_dealloc` | memory |
| 0.96% | `python` | `PyObject_GetAttr` | dynamic |
| 0.89% | `python` | `dict_dealloc` | memory |
| 0.87% | `python` | `long_hash` | int |
| 0.85% | `python` | `PySys_Audit` | unknown |
| 0.82% | `python` | `type_new` | memory |
| 0.76% | `python` | `PyObject_GetOptionalAttr` | dynamic |
| 0.72% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.65% | `python` | `builtin_id` | unknown |
| 0.62% | `python` | `long_richcompare` | int |
| 0.60% | `python` | `dictiter_iternextitem` | dict |
| 0.56% | `python` | `list_resize` | list |
| 0.56% | `python` | `list_append` | list |
| 0.52% | `python` | `PyTraceBack_Here` | exceptions |
| 0.52% | `python` | `BaseException_vectorcall` | exceptions |
| 0.49% | `python` | `meth_dealloc` | memory |
| 0.47% | `python` | `method_get` | dynamic |
| 0.47% | `python` | `PyMem_Realloc` | memory |
| 0.46% | `python` | `deduce_unreachable` | gc |
| 0.46% | `python` | `PyObject_RichCompare` | dynamic |
| 0.46% | `python` | `_PyFrame_MakeAndSetFrameObject` | unknown |
| 0.44% | `python` | `_PyCode_New` | interpreter |
| 0.44% | `python` | `intern_common.part.0` | str |
| 0.43% | `python` | `PyObject_Hash` | dynamic |
| 0.43% | `python` | `object_new` | memory |
| 0.43% | `python` | `_PyObject_GenericGetAttrWithDict` | dynamic |
| 0.41% | `python` | `PyObject_GC_Del` | gc |
| 0.38% | `python` | `dict_items` | dict |
| 0.37% | `python` | `object_isinstance` | dynamic |
| 0.36% | `python` | `BaseException_dealloc` | memory |
| 0.36% | `python` | `dict_merge` | dict |
| 0.36% | `python` | `_PyObject_GC_New` | gc |
| 0.34% | `python` | `visit_decref` | gc |
| 0.34% | `python` | `dictiter_dealloc` | memory |
| 0.34% | `python` | `PyMem_Free` | memory |
| 0.34% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.33% | `python` | `gc_collect_region.isra.0` | gc |
| 0.32% | `python` | `r_object` | import |
| 0.31% | `python` | `cell_dealloc` | memory |
| 0.31% | `python` | `slot_tp_init` | unknown |
| 0.30% | `python` | `_PyObject_Calloc` | memory |
| 0.30% | `python` | `_Py_type_getattro` | lookup |
| 0.29% | `libc-2.31.so` | `__memcpy_avx_unaligned_erms` | libc |
| 0.25% | `python` | `PyList_New` | memory |

## deltablue

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 57.51% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 6.01% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.66% | `python` | `deduce_unreachable` | gc |
| 1.58% | `python` | `gc_collect_region.isra.0` | gc |
| 1.33% | `python` | `type_new` | memory |
| 1.20% | `python` | `visit_decref` | gc |
| 1.07% | `python` | `_PySuper_Lookup` | dynamic |
| 1.07% | `python` | `_PyObject_GetMethod` | dynamic |
| 0.73% | `python` | `PyObject_GetAttr` | dynamic |
| 0.73% | `python` | `_Py_type_getattro` | lookup |
| 0.72% | `python` | `intern_common.part.0` | str |
| 0.70% | `python` | `_PyCode_New` | interpreter |
| 0.66% | `python` | `cm_descr_get` | unknown |
| 0.63% | `python` | `method_dealloc` | memory |
| 0.60% | `python` | `visit_reachable` | gc |
| 0.55% | `python` | `subtype_dealloc` | memory |
| 0.53% | `python` | `PyObject_GC_Del` | gc |
| 0.51% | `python` | `PyType_GenericNew` | memory |
| 0.50% | `python` | `r_object` | import |
| 0.49% | `python` | `subtype_traverse` | gc |
| 0.43% | `libc-2.31.so` | `__memcpy_avx_unaligned_erms` | libc |
| 0.43% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.42% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.42% | `python` | `list_iter` | list |
| 0.41% | `python` | `PyUnicode_FromKindAndData` | str |
| 0.39% | `python` | `tuple_dealloc` | memory |
| 0.33% | `python` | `list_dealloc` | memory |
| 0.32% | `python` | `long_add` | int |
| 0.32% | `python` | `siphash13` | str |
| 0.31% | `python` | `long_dealloc` | memory |
| 0.30% | `python` | `PyObject_SetAttr` | dynamic |
| 0.29% | `python` | `PyType_GenericAlloc` | memory |
| 0.29% | `python` | `unicode_dealloc` | memory |
| 0.29% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.27% | `python` | `PyObject_RichCompare` | dynamic |
| 0.25% | `python` | `visit_add_to_container` | gc |
| 0.25% | `python` | `_PyObject_Malloc` | memory |

## django_template

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 36.33% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 3.49% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 2.16% | `python` | `type_new` | memory |
| 1.73% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 1.57% | `python` | `object_isinstance` | dynamic |
| 1.31% | `python` | `deduce_unreachable` | gc |
| 1.29% | `python` | `insertdict` | dict |
| 1.26% | `python` | `intern_common.part.0` | str |
| 1.22% | `python` | `tuple_dealloc` | memory |
| 1.13% | `python` | `gc_collect_region.isra.0` | gc |
| 1.10% | `python` | `visit_decref` | gc |
| 1.07% | `python` | `_PyCode_New` | interpreter |
| 0.96% | `python` | `PyDict_GetItemRef` | dict |
| 0.85% | `python` | `PyObject_GC_Del` | gc |
| 0.82% | `python` | `PyFunction_NewWithQualName` | memory |
| 0.81% | `python` | `unicode_replace` | str |
| 0.77% | `python` | `PyObject_GetOptionalAttr` | dynamic |
| 0.77% | `python` | `visit_reachable` | gc |
| 0.73% | `python` | `list_dealloc` | memory |
| 0.72% | `python` | `r_object` | import |
| 0.68% | `python` | `_PyObject_GenericGetAttrWithDict` | dynamic |
| 0.68% | `python` | `_PyObject_GetMethod` | dynamic |
| 0.67% | `python` | `tupleiter_dealloc` | memory |
| 0.67% | `python` | `PyType_GenericAlloc` | memory |
| 0.62% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.60% | `libc-2.31.so` | `__memcpy_avx_unaligned_erms` | libc |
| 0.57% | `python` | `unicode_dealloc` | memory |
| 0.56% | `python` | `dict_dealloc` | memory |
| 0.56% | `python` | `PyUnicode_FromKindAndData` | str |
| 0.54% | `python` | `_PyObject_GC_New` | gc |
| 0.50% | `python` | `tuple_iter` | tuple |
| 0.49% | `python` | `siphash13` | str |
| 0.48% | `python` | `_Py_MakeCoro` | unknown |
| 0.46% | `python` | `slot_sq_contains` | unknown |
| 0.46% | `python` | `func_dealloc` | memory |
| 0.45% | `python` | `long_to_decimal_string_internal` | int |
| 0.43% | `python` | `list_iter` | list |
| 0.42% | `libz.so.1.2.11` | `inflateBackEnd` | library |
| 0.39% | `python` | `PyObject_GetIter` | dynamic |
| 0.38% | `python` | `slot_mp_ass_subscript` | unknown |
| 0.37% | `python` | `code_dealloc` | memory |
| 0.34% | `python` | `_PyObject_MakeTpCall` | dynamic |
| 0.34% | `python` | `list_vectorcall` | list |
| 0.33% | `python` | `_PyUnicode_JoinArray` | str |
| 0.33% | `python` | `getset_get` | dynamic |
| 0.32% | `python` | `find_name_in_mro` | lookup |
| 0.31% | `python` | `_Py_dict_lookup` | lookup |
| 0.29% | `python` | `dict_traverse` | gc |
| 0.28% | `python` | `meth_dealloc` | memory |
| 0.27% | `python` | `gen_dealloc` | memory |
| 0.27% | `python` | `chain_next` | unknown |
| 0.26% | `python` | `type_ready` | dynamic |
| 0.26% | `python` | `long_sub` | int |
| 0.25% | `python` | `_PyObject_Calloc` | memory |

## docutils

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 26.98% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 7.84% | `python` | `sre_ucs1_match` | library |
| 3.85% | `python` | `deduce_unreachable` | gc |
| 3.01% | `python` | `gc_collect_region.isra.0` | gc |
| 2.81% | `python` | `PyObject_GetAttr` | dynamic |
| 2.55% | `python` | `sre_ucs2_charset.isra.0` | library |
| 2.16% | `python` | `visit_add_to_container` | gc |
| 2.05% | `python` | `find_name_in_mro` | lookup |
| 1.99% | `python` | `visit_decref` | gc |
| 1.98% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.87% | `python` | `list_dealloc` | memory |
| 1.34% | `libc-2.31.so` | `__memcpy_avx_unaligned_erms` | libc |
| 1.06% | `python` | `PyObject_SetAttr` | dynamic |
| 1.00% | `python` | `_PyObject_GetMethod` | dynamic |
| 0.98% | `python` | `visit_reachable` | gc |
| 0.98% | `python` | `PyDict_GetItemRef` | dict |
| 0.93% | `python` | `_PyUnicode_JoinArray` | str |
| 0.81% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.80% | `python` | `dict_traverse` | gc |
| 0.79% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.77% | `python` | `object_isinstance` | dynamic |
| 0.76% | `python` | `subtype_traverse` | gc |
| 0.76% | `python` | `list_traverse` | gc |
| 0.75% | `python` | `tuple_dealloc` | memory |
| 0.71% | `python` | `PyMem_Free` | memory |
| 0.67% | `python` | `PyUnicode_Format` | str |
| 0.66% | `python` | `list_subscript` | list |
| 0.62% | `python` | `_PyObject_GenericGetAttrWithDict` | dynamic |
| 0.61% | `python` | `PyMem_Malloc` | memory |
| 0.61% | `python` | `insertdict` | dict |
| 0.59% | `python` | `unicode_dealloc` | memory |
| 0.58% | `python` | `dict_dealloc` | memory |
| 0.51% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.51% | `python` | `sre_ucs1_count` | library |
| 0.50% | `python` | `_sre_SRE_Pattern_match` | library |
| 0.48% | `python` | `func_descr_get` | unknown |
| 0.47% | `python` | `_PyObject_GC_New` | gc |
| 0.44% | `python` | `PyObject_GC_Del` | gc |
| 0.43% | `python` | `_Py_dict_lookup` | lookup |
| 0.41% | `python` | `PyDict_Contains` | dict |
| 0.40% | `python` | `method_dealloc` | memory |
| 0.40% | `libc-2.31.so` | `_int_malloc` | libc |
| 0.39% | `python` | `PyList_New` | memory |
| 0.38% | `python` | `_PyGC_Collect` | gc |
| 0.38% | `python` | `list_iter` | list |
| 0.38% | `python` | `_PyTuple_FromStackRefSteal` | tuple |
| 0.37% | `python` | `getset_get` | dynamic |
| 0.36% | `python` | `list_vectorcall` | list |
| 0.33% | `python` | `_Py_type_getattro` | lookup |
| 0.31% | `python` | `gen_dealloc` | memory |
| 0.28% | `python` | `PyObject_GetOptionalAttr` | dynamic |
| 0.27% | `python` | `siphash13` | str |
| 0.26% | `python` | `list_resize` | list |
| 0.26% | `python` | `unicode_split` | str |
| 0.26% | `python` | `insert_to_emptydict` | dict |
| 0.26% | `python` | `subtype_dealloc` | memory |
| 0.25% | `python` | `_PyUnicodeWriter_PrepareInternal` | str |

## dulwich_log

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 31.18% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 3.15% | `libz.so.1.2.11` | `inflateCodesUsed` | library |
| 2.00% | `libz.so.1.2.11` | `inflateBackEnd` | library |
| 1.72% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.50% | `libz.so.1.2.11` | `inflate` | library |
| 1.38% | `python` | `PyBytes_FromStringAndSize` | str |
| 1.17% | `python` | `type_new` | memory |
| 1.03% | `python` | `tuple_dealloc` | memory |
| 0.99% | `python` | `object_dealloc` | memory |
| 0.80% | `libc-2.31.so` | `__memcpy_avx_unaligned_erms` | libc |
| 0.79% | `python` | `visit_decref` | gc |
| 0.76% | `python` | `long_dealloc` | memory |
| 0.71% | `python` | `list_dealloc` | memory |
| 0.71% | `python` | `intern_common.part.0` | str |
| 0.69% | `python` | `deduce_unreachable` | gc |
| 0.65% | `python` | `_PyCode_New` | interpreter |
| 0.60% | `python` | `gc_collect_region.isra.0` | gc |
| 0.60% | `[kernel.kallsyms]` | `copy_user_enhanced_fast_string` | kernel |
| 0.57% | `python` | `siphash13` | str |
| 0.54% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.53% | `python` | `unicode_dealloc` | memory |
| 0.53% | `[kernel.kallsyms]` | `__d_lookup_rcu` | kernel |
| 0.50% | `python` | `PyList_New` | memory |
| 0.48% | `python` | `visit_reachable` | gc |
| 0.46% | `python` | `long_add` | int |
| 0.46% | `python` | `r_object` | import |
| 0.46% | `python` | `PyObject_GC_Del` | gc |
| 0.45% | `libc-2.31.so` | `_int_malloc` | libc |
| 0.45% | `python` | `_PyTuple_FromStackRefSteal` | tuple |
| 0.43% | `python` | `PyType_GenericAlloc` | memory |
| 0.41% | `python` | `PyDict_GetItemRef` | dict |
| 0.41% | `python` | `unicode_encode` | str |
| 0.40% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.37% | `python` | `slot_tp_init` | unknown |
| 0.37% | `python` | `_PyLong_FromBytes` | int |
| 0.36% | `python` | `PyObject_RichCompare` | dynamic |
| 0.36% | `python` | `PyUnicode_FSConverter` | str |
| 0.35% | `python` | `subtype_dealloc` | memory |
| 0.35% | `python` | `_PyObject_GC_New` | gc |
| 0.35% | `python` | `PyUnicode_FromKindAndData` | str |
| 0.32% | `python` | `object_new` | memory |
| 0.31% | `python` | `PySlice_Unpack` | miscobj |
| 0.31% | `python` | `clear_slots` | unknown |
| 0.30% | `libz.so.1.2.11` | `adler32_z` | library |
| 0.29% | `[kernel.kallsyms]` | `clear_bhb_loop` | kernel |
| 0.29% | `libc-2.31.so` | `__memcmp_avx2_movbe` | libc |
| 0.29% | `python` | `find_name_in_mro` | lookup |
| 0.29% | `libc-2.31.so` | `__libc_malloc` | libc |
| 0.29% | `python` | `bytes_richcompare` | str |
| 0.28% | `python` | `PyFunction_NewWithQualName` | memory |
| 0.27% | `[kernel.kallsyms]` | `link_path_walk.part.0` | kernel |
| 0.27% | `python` | `PyUnicode_New` | memory |
| 0.26% | `python` | `dict_dealloc` | memory |

## fannkuch

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 38.99% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 10.17% | `python` | `list_subscript` | list |
| 7.64% | `python` | `list_ass_slice_lock_held` | list |
| 7.48% | `python` | `list_dealloc` | memory |
| 4.18% | `python` | `list_new_prealloc` | memory |
| 3.85% | `python` | `slice_dealloc` | memory |
| 2.66% | `python` | `long_add` | int |
| 2.60% | `python` | `list_ass_subscript` | list |
| 1.91% | `python` | `PySlice_New` | memory |
| 1.62% | `python` | `_PyBuildSlice_Consume2` | unknown |
| 1.58% | `python` | `PySlice_Unpack` | miscobj |
| 1.33% | `python` | `_PyEval_SliceIndex` | interpreter |
| 1.06% | `python` | `PyObject_GetItem` | dynamic |
| 1.01% | `python` | `ins1` | unknown |
| 0.95% | `python` | `PyNumber_AsSsize_t` | dynamic |
| 0.94% | `libc-2.31.so` | `__memcpy_avx_unaligned_erms` | libc |
| 0.69% | `python` | `PyObject_SetItem` | dynamic |
| 0.68% | `python` | `long_sub` | int |
| 0.67% | `python` | `list_pop` | list |
| 0.66% | `python` | `PySequence_Fast` | dynamic |
| 0.66% | `python` | `PyMem_Malloc` | memory |
| 0.45% | `python` | `PyMem_Free` | memory |
| 0.41% | `python` | `type_new` | memory |
| 0.41% | `python` | `PySlice_AdjustIndices` | miscobj |
| 0.35% | `python` | `list_insert` | list |
| 0.32% | `python` | `PyLong_AsSsize_t` | int |
| 0.27% | `python` | `list_resize` | list |
| 0.26% | `python` | `deduce_unreachable` | gc |

## float

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 38.87% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 2.62% | `libm-2.31.so` | `__sin_fma` | library |
| 2.47% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 2.37% | `python` | `_PyFloat_FromDouble_ConsumeInputs` | float |
| 2.36% | `libm-2.31.so` | `__cos_fma` | library |
| 2.19% | `python` | `subtype_traverse` | gc |
| 1.90% | `python` | `visit_decref` | gc |
| 1.78% | `python` | `_PyObject_Malloc` | memory |
| 1.77% | `python` | `slot_tp_init` | unknown |
| 1.74% | `python` | `float_div` | float |
| 1.70% | `python` | `visit_reachable` | gc |
| 1.67% | `python` | `deduce_unreachable` | gc |
| 1.63% | `python` | `object_new` | memory |
| 1.50% | `python` | `visit_add_to_container` | gc |
| 1.31% | `python` | `clear_slots` | unknown |
| 1.28% | `python` | `PyFloat_AsDouble` | float |
| 1.15% | `python` | `float_dealloc` | memory |
| 1.00% | `python` | `PyFloat_FromDouble` | float |
| 0.98% | `python` | `gc_collect_region.isra.0` | gc |
| 0.95% | `python` | `type_new` | memory |
| 0.95% | `python` | `_PyObject_Free` | memory |
| 0.94% | `python` | `tuple_dealloc` | memory |
| 0.93% | `python` | `_PyObject_MakeTpCall` | dynamic |
| 0.82% | `python` | `subtype_dealloc` | memory |
| 0.76% | `python` | `PyLong_FromLong` | int |
| 0.70% | `python` | `long_dealloc` | memory |
| 0.70% | `python` | `binary_op1` | unknown |
| 0.60% | `python` | `PyLong_AsDouble` | int |
| 0.59% | `python` | `intern_common.part.0` | str |
| 0.58% | `python` | `list_dealloc` | memory |
| 0.56% | `python` | `float_mul` | float |
| 0.55% | `python` | `PyObject_GC_Del` | gc |
| 0.53% | `python` | `_PyCode_New` | interpreter |
| 0.47% | `python` | `binary_iop1` | unknown |
| 0.42% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.42% | `[kernel.kallsyms]` | `native_irq_return_iret` | kernel |
| 0.41% | `python` | `dict_traverse` | gc |
| 0.40% | `python` | `PyNumber_Multiply` | dynamic |
| 0.38% | `python` | `list_subscript` | list |
| 0.37% | `python` | `PyNumber_TrueDivide` | dynamic |
| 0.37% | `python` | `r_object` | import |
| 0.35% | `[kernel.kallsyms]` | `clear_page_erms` | kernel |
| 0.33% | `python` | `list_traverse` | gc |
| 0.31% | `python` | `binary_iop` | unknown |
| 0.30% | `[kernel.kallsyms]` | `sync_regs` | kernel |
| 0.29% | `math.cpython-314-x86_64-linux-gnu.so` | `math_sin` | library |
| 0.29% | `libc-2.31.so` | `__memcpy_avx_unaligned_erms` | libc |
| 0.28% | `[kernel.kallsyms]` | `free_pcppages_bulk` | kernel |
| 0.28% | `python` | `PyUnicode_FromKindAndData` | str |
| 0.27% | `math.cpython-314-x86_64-linux-gnu.so` | `math_cos` | library |
| 0.26% | `python` | `type_call` | dynamic |

## gc_collect

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 20.06% | `python` | `gc_collect_region.isra.0` | gc |
| 15.75% | `python` | `visit_reachable` | gc |
| 15.55% | `python` | `deduce_unreachable` | gc |
| 14.93% | `python` | `visit_decref` | gc |
| 5.34% | `python` | `_PyGC_Collect` | gc |
| 4.76% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 4.44% | `python` | `dict_traverse` | gc |
| 2.58% | `python` | `subtype_traverse` | gc |
| 2.16% | `python` | `func_traverse` | gc |
| 1.23% | `python` | `set_traverse` | gc |
| 1.17% | `python` | `tuple_traverse` | gc |
| 0.80% | `python` | `type_traverse` | gc |
| 0.76% | `python` | `list_traverse` | gc |
| 0.68% | `python` | `PyType_GenericAlloc` | memory |
| 0.59% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.49% | `python` | `type_new` | memory |
| 0.44% | `python` | `meth_traverse` | gc |
| 0.35% | `python` | `subtype_dealloc` | memory |
| 0.31% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.26% | `python` | `_PyCode_New` | interpreter |
| 0.26% | `python` | `intern_common.part.0` | str |
| 0.26% | `python` | `PyObject_GC_Del` | gc |

## gc_traversal

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 28.62% | `python` | `visit_reachable` | gc |
| 22.78% | `python` | `visit_decref` | gc |
| 12.04% | `python` | `list_traverse` | gc |
| 10.01% | `python` | `gc_collect_region.isra.0` | gc |
| 7.84% | `python` | `deduce_unreachable` | gc |
| 3.44% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 2.28% | `python` | `dict_traverse` | gc |
| 1.14% | `python` | `func_traverse` | gc |
| 0.86% | `python` | `subtype_traverse` | gc |
| 0.65% | `python` | `tuple_traverse` | gc |
| 0.64% | `python` | `set_traverse` | gc |
| 0.55% | `python` | `type_new` | memory |
| 0.48% | `python` | `PyLong_FromLong` | int |
| 0.46% | `python` | `long_dealloc` | memory |
| 0.45% | `python` | `type_traverse` | gc |
| 0.30% | `python` | `intern_common.part.0` | str |
| 0.29% | `python` | `_PyCode_New` | interpreter |
| 0.28% | `python` | `list_dealloc` | memory |

## generators

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 53.19% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 3.02% | `python` | `gen_dealloc` | memory |
| 2.46% | `python` | `long_add` | int |
| 1.87% | `python` | `_Py_MakeCoro` | unknown |
| 1.74% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.67% | `python` | `long_dealloc` | memory |
| 1.56% | `python` | `_PyFunction_Vectorcall` | calls |
| 1.44% | `python` | `range_subscript` | miscobj |
| 1.41% | `python` | `deduce_unreachable` | gc |
| 1.13% | `python` | `visit_decref` | gc |
| 1.10% | `python` | `subtype_dealloc` | memory |
| 1.10% | `python` | `visit_reachable` | gc |
| 1.01% | `python` | `subtype_traverse` | gc |
| 0.94% | `python` | `PyType_GenericAlloc` | memory |
| 0.85% | `python` | `_PyObject_New` | memory |
| 0.82% | `python` | `type_new` | memory |
| 0.78% | `python` | `gc_collect_region.isra.0` | gc |
| 0.78% | `python` | `make_range_object` | unknown |
| 0.73% | `python` | `lookup_maybe_method` | unknown |
| 0.68% | `python` | `visit_add_to_container` | gc |
| 0.62% | `python` | `PyNumber_Add` | dynamic |
| 0.60% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 0.60% | `python` | `range_dealloc` | memory |
| 0.55% | `python` | `long_richcompare` | int |
| 0.52% | `python` | `PyObject_CallOneArg` | dynamic |
| 0.51% | `python` | `_PySlice_GetLongIndices` | miscobj |
| 0.50% | `python` | `slot_tp_iter` | unknown |
| 0.49% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.49% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.48% | `python` | `intern_common.part.0` | str |
| 0.47% | `python` | `_PyCode_New` | interpreter |
| 0.47% | `python` | `PyObject_RichCompareBool` | dynamic |
| 0.46% | `python` | `_PyBuildSlice_Consume2` | unknown |
| 0.42% | `python` | `long_div` | int |
| 0.41% | `python` | `long_mul_method` | int |
| 0.40% | `python` | `PyLong_AsLongAndOverflow` | int |
| 0.34% | `python` | `PyNumber_Multiply` | dynamic |
| 0.34% | `python` | `PyObject_GetItem` | dynamic |
| 0.29% | `python` | `slice_dealloc` | memory |
| 0.28% | `python` | `PyObject_GC_Del` | gc |
| 0.28% | `python` | `r_object` | import |
| 0.27% | `python` | `PyObject_IsTrue` | dynamic |
| 0.26% | `python` | `dict_traverse` | gc |

## genshi

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 49.69% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 2.20% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.67% | `python` | `tuple_dealloc` | memory |
| 1.50% | `python` | `insertdict` | dict |
| 1.38% | `python` | `_PyTuple_FromStackRefSteal` | tuple |
| 1.22% | `python` | `_PyObject_GC_New` | gc |
| 1.21% | `python` | `dictresize` | dict |
| 1.18% | `python` | `dict_dealloc` | memory |
| 1.06% | `python` | `dict_get` | dict |
| 0.99% | `python` | `insert_to_emptydict` | dict |
| 0.91% | `python` | `PyObject_GC_Del` | gc |
| 0.84% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.84% | `python` | `PyDict_GetItemRef` | dict |
| 0.84% | `python` | `_Py_type_getattro` | lookup |
| 0.81% | `python` | `long_to_decimal_string_internal` | int |
| 0.79% | `python` | `cm_descr_get` | unknown |
| 0.78% | `python` | `method_dealloc` | memory |
| 0.77% | `python` | `type_new` | memory |
| 0.73% | `python` | `object_isinstance` | dynamic |
| 0.64% | `python` | `PyObject_IsTrue` | dynamic |
| 0.62% | `python` | `PyDict_Contains` | dict |
| 0.61% | `python` | `PyMem_Free` | memory |
| 0.58% | `python` | `deduce_unreachable` | gc |
| 0.55% | `python` | `PyDict_SetItem` | dict |
| 0.54% | `python` | `_PyEval_LoadName` | interpreter |
| 0.54% | `python` | `list_dealloc` | memory |
| 0.53% | `python` | `func_dealloc` | memory |
| 0.50% | `python` | `_PyUnicode_JoinArray` | str |
| 0.50% | `python` | `PyObject_GetAttr` | dynamic |
| 0.50% | `python` | `visit_decref` | gc |
| 0.49% | `python` | `unicode_dealloc` | memory |
| 0.49% | `python` | `tuple_hash` | tuple |
| 0.47% | `libc-2.31.so` | `_int_malloc` | libc |
| 0.47% | `python` | `PyUnicode_New` | memory |
| 0.46% | `python` | `intern_common.part.0` | str |
| 0.44% | `python` | `PyType_GenericAlloc` | memory |
| 0.44% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.43% | `python` | `gc_collect_region.isra.0` | gc |
| 0.42% | `python` | `_PyCode_New` | interpreter |
| 0.42% | `libc-2.31.so` | `__memcpy_avx_unaligned_erms` | libc |
| 0.41% | `python` | `_PyDict_LoadBuiltinsFromGlobals` | dict |
| 0.40% | `python` | `PyObject_Str` | dynamic |
| 0.38% | `python` | `state_init` | unknown |
| 0.37% | `python` | `visit_reachable` | gc |
| 0.34% | `python` | `list_iter` | list |
| 0.34% | `python` | `_PyObject_Malloc` | memory |
| 0.31% | `python` | `dictiter_iternextvalue` | dict |
| 0.30% | `python` | `gen_iternext` | miscobj |
| 0.30% | `python` | `PyObject_RichCompare` | dynamic |
| 0.29% | `python` | `r_object` | import |
| 0.29% | `python` | `pattern_subx` | library |
| 0.29% | `python` | `PyObject_Vectorcall` | dynamic |
| 0.28% | `libc-2.31.so` | `__libc_malloc` | libc |
| 0.28% | `python` | `list_vectorcall` | list |
| 0.28% | `python` | `PyMem_Malloc` | memory |
| 0.27% | `python` | `_PyObject_MakeTpCall` | dynamic |
| 0.26% | `python` | `subtype_dealloc` | memory |
| 0.25% | `python` | `_PyFunction_FromConstructor` | unknown |

## go

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 64.03% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 4.59% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.42% | `python` | `long_bitwise` | int |
| 1.31% | `python` | `long_dealloc` | memory |
| 1.20% | `python` | `type_new` | memory |
| 1.10% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.99% | `python` | `long_add` | int |
| 0.91% | `python` | `PyDict_SetItem` | dict |
| 0.73% | `python` | `deduce_unreachable` | gc |
| 0.68% | `python` | `intern_common.part.0` | str |
| 0.66% | `python` | `_PyCode_New` | interpreter |
| 0.65% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.63% | `python` | `list_iter` | list |
| 0.63% | `python` | `visit_decref` | gc |
| 0.58% | `python` | `gc_collect_region.isra.0` | gc |
| 0.53% | `python` | `PyObject_GC_Del` | gc |
| 0.49% | `python` | `r_object` | import |
| 0.47% | `python` | `long_sub` | int |
| 0.43% | `python` | `visit_reachable` | gc |
| 0.37% | `python` | `PyUnicode_FromKindAndData` | str |
| 0.35% | `libc-2.31.so` | `__memcpy_avx_unaligned_erms` | libc |
| 0.31% | `python` | `tuple_dealloc` | memory |
| 0.27% | `python` | `siphash13` | str |

## hexiom

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 57.46% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 4.54% | `python` | `list_contains` | list |
| 3.22% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 2.02% | `python` | `long_richcompare` | int |
| 1.90% | `python` | `builtin_sum` | unknown |
| 1.42% | `python` | `type_new` | memory |
| 0.90% | `python` | `gen_iternext` | miscobj |
| 0.86% | `python` | `intern_common.part.0` | str |
| 0.82% | `python` | `deduce_unreachable` | gc |
| 0.79% | `python` | `_PyCode_New` | interpreter |
| 0.75% | `python` | `list_dealloc` | memory |
| 0.65% | `python` | `PyFunction_NewWithQualName` | memory |
| 0.62% | `python` | `PyLong_FromLong` | int |
| 0.62% | `python` | `gc_collect_region.isra.0` | gc |
| 0.62% | `python` | `visit_decref` | gc |
| 0.59% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.51% | `python` | `r_object` | import |
| 0.50% | `python` | `tuple_dealloc` | memory |
| 0.47% | `python` | `visit_reachable` | gc |
| 0.44% | `python` | `list_iter` | list |
| 0.41% | `python` | `PyUnicode_FromKindAndData` | str |
| 0.39% | `python` | `func_dealloc` | memory |
| 0.39% | `python` | `siphash13` | str |
| 0.37% | `python` | `PyObject_GC_Del` | gc |
| 0.37% | `python` | `_Py_MakeCoro` | unknown |
| 0.34% | `python` | `long_add` | int |
| 0.32% | `libc-2.31.so` | `__memcpy_avx_unaligned_erms` | libc |
| 0.31% | `python` | `PyList_New` | memory |
| 0.31% | `python` | `gen_dealloc` | memory |
| 0.29% | `python` | `PyObject_Free` | dynamic |
| 0.28% | `python` | `unicode_dealloc` | memory |
| 0.28% | `python` | `range_iter` | miscobj |
| 0.27% | `python` | `listiter_dealloc` | memory |
| 0.27% | `python` | `range_vectorcall` | miscobj |

## html5lib

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 38.95% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 8.53% | `python` | `sre_ucs2_charset.isra.0` | library |
| 2.09% | `python` | `PyDict_GetItemRef` | dict |
| 2.06% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.95% | `python` | `deduce_unreachable` | gc |
| 1.69% | `python` | `gc_collect_region.isra.0` | gc |
| 1.43% | `python` | `visit_decref` | gc |
| 1.33% | `python` | `type_new` | memory |
| 1.17% | `python` | `PyObject_GetAttr` | dynamic |
| 0.88% | `python` | `sre_ucs1_count` | library |
| 0.82% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.81% | `python` | `visit_reachable` | gc |
| 0.76% | `python` | `intern_common.part.0` | str |
| 0.75% | `python` | `_PyCode_New` | interpreter |
| 0.69% | `python` | `unicode_dealloc` | memory |
| 0.66% | `python` | `insertdict` | dict |
| 0.66% | `python` | `_sre_SRE_Pattern_match` | library |
| 0.59% | `python` | `dict_dealloc` | memory |
| 0.59% | `python` | `long_dealloc` | memory |
| 0.58% | `python` | `set_contains_lock_held` | miscobj |
| 0.57% | `python` | `list_dealloc` | memory |
| 0.57% | `libc-2.31.so` | `__memcpy_avx_unaligned_erms` | libc |
| 0.56% | `python` | `visit_add_to_container` | gc |
| 0.54% | `python` | `PyUnicode_Concat` | str |
| 0.53% | `python` | `tuple_dealloc` | memory |
| 0.53% | `python` | `list_contains` | list |
| 0.49% | `python` | `r_object` | import |
| 0.49% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.47% | `python` | `siphash13` | str |
| 0.40% | `python` | `PyUnicode_FromKindAndData` | str |
| 0.39% | `python` | `list_subscript` | list |
| 0.39% | `libc-2.31.so` | `__memcmp_avx2_movbe` | libc |
| 0.36% | `python` | `func_descr_get` | unknown |
| 0.36% | `libc-2.31.so` | `_int_malloc` | libc |
| 0.35% | `python` | `_PyUnicode_TranslateCharmap` | str |
| 0.34% | `python` | `long_add` | int |
| 0.33% | `python` | `method_dealloc` | memory |
| 0.33% | `python` | `insert_to_emptydict` | dict |
| 0.33% | `python` | `PyObject_IsTrue` | dynamic |
| 0.32% | `python` | `PyList_New` | memory |
| 0.31% | `python` | `PyObject_GC_Del` | gc |
| 0.27% | `python` | `dict_traverse` | gc |
| 0.27% | `python` | `PyObject_SetAttr` | dynamic |
| 0.27% | `python` | `tuple_hash` | tuple |
| 0.27% | `python` | `subtype_traverse` | gc |
| 0.26% | `python` | `code_dealloc` | memory |
| 0.26% | `python` | `sre_ucs1_match` | library |
| 0.26% | `python` | `_PyUnicode_JoinArray` | str |
| 0.26% | `python` | `find_name_in_mro` | lookup |
| 0.25% | `python` | `slot_mp_subscript` | unknown |

## json

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 16.63% | `_json.cpython-314-x86_64-linux-gnu.so` | `_parse_object_unicode` | library |
| 7.82% | `python` | `PyUnicode_Substring` | str |
| 7.71% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 6.02% | `python` | `dict_setdefault_ref_lock_held` | dict |
| 5.77% | `python` | `PyDict_SetItem` | dict |
| 5.47% | `python` | `siphash13` | str |
| 4.78% | `python` | `unicode_dealloc` | memory |
| 3.74% | `python` | `dictresize` | dict |
| 3.36% | `python` | `PyLong_FromString` | int |
| 2.78% | `python` | `dict_dealloc` | memory |
| 2.06% | `python` | `_sre_SRE_Pattern_match` | library |
| 1.53% | `python` | `PyBytes_FromStringAndSize` | str |
| 1.50% | `_json.cpython-314-x86_64-linux-gnu.so` | `_match_number_unicode.isra.0` | library |
| 1.26% | `libc-2.31.so` | `__memcpy_avx_unaligned_erms` | libc |
| 1.12% | `libc-2.31.so` | `_int_malloc` | libc |
| 0.90% | `python` | `PyDict_GetItemRef` | dict |
| 0.90% | `python` | `type_new` | memory |
| 0.83% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.71% | `libc-2.31.so` | `_int_free` | libc |
| 0.67% | `python` | `insert_to_emptydict` | dict |
| 0.66% | `python` | `unicode_hash` | str |
| 0.66% | `python` | `object_dealloc` | memory |
| 0.65% | `python` | `sre_ucs1_match` | library |
| 0.64% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.62% | `python` | `long_dealloc` | memory |
| 0.59% | `libc-2.31.so` | `__libc_malloc` | libc |
| 0.59% | `python` | `_PyUnicodeWriter_PrepareInternal` | str |
| 0.57% | `python` | `tuple_dealloc` | memory |
| 0.51% | `python` | `deduce_unreachable` | gc |
| 0.48% | `python` | `resize_compact` | str |
| 0.48% | `python` | `intern_common.part.0` | str |
| 0.47% | `python` | `visit_decref` | gc |
| 0.47% | `python` | `match_dealloc` | memory |
| 0.46% | `python` | `_PyCode_New` | interpreter |
| 0.45% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.42% | `python` | `gc_collect_region.isra.0` | gc |
| 0.40% | `python` | `vgetargskeywords.constprop.0` | calls |
| 0.40% | `python` | `PyMem_Free` | memory |
| 0.35% | `python` | `_PyObject_Free` | memory |
| 0.35% | `python` | `r_object` | import |
| 0.33% | `python` | `_PyLong_New` | memory |
| 0.30% | `python` | `_PyUnicodeWriter_Init` | str |
| 0.29% | `python` | `visit_reachable` | gc |
| 0.27% | `python` | `PyObject_Hash` | dynamic |
| 0.27% | `python` | `_PyUnicodeWriter_WriteSubstring` | str |
| 0.27% | `libc-2.31.so` | `unlink_chunk.isra.0` | libc |
| 0.27% | `python` | `PyUnicode_FromKindAndData` | str |

## json_dumps

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 13.14% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 9.38% | `_json.cpython-314-x86_64-linux-gnu.so` | `encoder_listencode_dict` | library |
| 6.36% | `python` | `PyUnicode_New` | memory |
| 5.21% | `python` | `_PyUnicodeWriter_WriteStr` | str |
| 5.04% | `python` | `PyUnicodeWriter_WriteStr` | str |
| 4.70% | `python` | `unicode_dealloc` | memory |
| 3.44% | `python` | `_PyUnicodeWriter_PrepareInternal` | str |
| 2.93% | `_json.cpython-314-x86_64-linux-gnu.so` | `py_encode_basestring_ascii` | library |
| 2.74% | `python` | `resize_compact` | str |
| 2.47% | `libc-2.31.so` | `__memcpy_avx_unaligned_erms` | libc |
| 2.39% | `python` | `vgetargskeywords.constprop.0` | calls |
| 2.27% | `python` | `PyDict_GetItemRef` | dict |
| 1.51% | `python` | `PyDict_Next` | dict |
| 1.37% | `python` | `long_to_decimal_string_internal` | int |
| 1.36% | `python` | `tuple_dealloc` | memory |
| 1.27% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.21% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 1.11% | `python` | `PyFunction_NewWithQualName` | memory |
| 1.09% | `python` | `object_isinstance` | dynamic |
| 1.07% | `python` | `PyObject_GetAttr` | dynamic |
| 1.04% | `python` | `PyDict_SetItem` | dict |
| 0.84% | `python` | `type_new` | memory |
| 0.82% | `python` | `_PyLong_New` | memory |
| 0.75% | `python` | `PyDict_DelItem` | dict |
| 0.74% | `python` | `long_hash` | int |
| 0.72% | `python` | `_PyObject_MakeTpCall` | dynamic |
| 0.67% | `python` | `PyType_GenericAlloc` | memory |
| 0.65% | `python` | `long_dealloc` | memory |
| 0.64% | `python` | `PyMem_Free` | memory |
| 0.63% | `python` | `PyDict_Contains` | dict |
| 0.60% | `python` | `_Py_dict_lookup` | lookup |
| 0.59% | `python` | `func_dealloc` | memory |
| 0.53% | `python` | `deduce_unreachable` | gc |
| 0.52% | `python` | `unicode_decode_utf8_writer` | str |
| 0.46% | `python` | `insert_to_emptydict` | dict |
| 0.45% | `python` | `intern_common.part.0` | str |
| 0.44% | `python` | `_PyCode_New` | interpreter |
| 0.42% | `python` | `PyMem_Malloc` | memory |
| 0.40% | `python` | `PyUnicodeWriter_Create` | str |
| 0.40% | `python` | `_PyTuple_FromStackRefSteal` | tuple |
| 0.39% | `python` | `dict_dealloc` | memory |
| 0.39% | `python` | `method_dealloc` | memory |
| 0.36% | `python` | `visit_decref` | gc |
| 0.35% | `python` | `PyTuple_Pack` | tuple |
| 0.34% | `python` | `memcpy@plt` | memory |
| 0.34% | `python` | `func_descr_get` | unknown |
| 0.33% | `python` | `gc_collect_region.isra.0` | gc |
| 0.33% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.33% | `python` | `_Py_Dealloc` | memory |
| 0.32% | `_json.cpython-314-x86_64-linux-gnu.so` | `0x0000000000002664` | library |
| 0.32% | `libc-2.31.so` | `pthread_self` | libc |
| 0.30% | `python` | `r_object` | import |
| 0.30% | `python` | `pthread_self@plt` | unknown |
| 0.29% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.29% | `python` | `visit_reachable` | gc |
| 0.27% | `_json.cpython-314-x86_64-linux-gnu.so` | `encoder_new` | library |
| 0.26% | `python` | `PyLong_FromLong` | int |
| 0.25% | `libc-2.31.so` | `__strchr_avx2` | libc |

## json_loads

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 17.09% | `_json.cpython-314-x86_64-linux-gnu.so` | `_parse_object_unicode` | library |
| 12.06% | `python` | `PyUnicode_Substring` | str |
| 6.97% | `python` | `siphash13` | str |
| 6.26% | `python` | `dict_setdefault_ref_lock_held` | dict |
| 5.86% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 5.15% | `python` | `PyDict_SetItem` | dict |
| 5.07% | `python` | `unicode_dealloc` | memory |
| 3.31% | `python` | `PyLong_FromString` | int |
| 2.42% | `python` | `dictresize` | dict |
| 1.77% | `python` | `dict_dealloc` | memory |
| 1.51% | `python` | `PyBytes_FromStringAndSize` | str |
| 1.26% | `_json.cpython-314-x86_64-linux-gnu.so` | `_match_number_unicode.isra.0` | library |
| 1.15% | `python` | `_sre_SRE_Pattern_match` | library |
| 1.12% | `python` | `type_new` | memory |
| 1.09% | `libc-2.31.so` | `__memcpy_avx_unaligned_erms` | libc |
| 0.92% | `python` | `object_dealloc` | memory |
| 0.85% | `_json.cpython-314-x86_64-linux-gnu.so` | `_parse_array_unicode` | library |
| 0.83% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.78% | `python` | `unicode_hash` | str |
| 0.71% | `python` | `deduce_unreachable` | gc |
| 0.65% | `python` | `intern_common.part.0` | str |
| 0.64% | `libc-2.31.so` | `_int_malloc` | libc |
| 0.62% | `libc-2.31.so` | `__memcmp_avx2_movbe` | libc |
| 0.61% | `python` | `_PyCode_New` | interpreter |
| 0.58% | `python` | `long_dealloc` | memory |
| 0.54% | `python` | `PyDict_GetItemRef` | dict |
| 0.52% | `python` | `visit_decref` | gc |
| 0.50% | `python` | `gc_collect_region.isra.0` | gc |
| 0.48% | `python` | `_PyUnicodeWriter_Init` | str |
| 0.47% | `libc-2.31.so` | `__libc_malloc` | libc |
| 0.45% | `python` | `r_object` | import |
| 0.44% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.43% | `libc-2.31.so` | `_int_free` | libc |
| 0.41% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.39% | `python` | `insert_to_emptydict` | dict |
| 0.38% | `python` | `tuple_dealloc` | memory |
| 0.38% | `python` | `visit_reachable` | gc |
| 0.38% | `python` | `PyList_Append` | list |
| 0.36% | `python` | `PyObject_Hash` | dynamic |
| 0.35% | `python` | `list_dealloc` | memory |
| 0.31% | `python` | `PyUnicode_FromKindAndData` | str |
| 0.31% | `python` | `sre_ucs1_match` | library |
| 0.30% | `python` | `PyMem_Realloc` | memory |

## logging

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 48.88% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 6.21% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 2.87% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 2.20% | `python` | `PyDict_GetItemRef` | dict |
| 1.67% | `python` | `PyCode_Addr2Line` | exceptions |
| 1.47% | `python` | `PyObject_GetAttr` | dynamic |
| 1.44% | `python` | `dict_dealloc` | memory |
| 0.92% | `python` | `type_new` | memory |
| 0.89% | `python` | `PyDict_New` | memory |
| 0.85% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.68% | `python` | `tuple_dealloc` | memory |
| 0.68% | `python` | `unicode_dealloc` | memory |
| 0.68% | `python` | `unicode_subscript` | str |
| 0.65% | `python` | `long_dealloc` | memory |
| 0.64% | `python` | `PyLong_FromLong` | int |
| 0.56% | `python` | `PyUnicode_Format` | str |
| 0.52% | `python` | `_PyCode_New` | interpreter |
| 0.50% | `python` | `intern_common.part.0` | str |
| 0.48% | `python` | `deduce_unreachable` | gc |
| 0.44% | `python` | `visit_decref` | gc |
| 0.43% | `python` | `_PyObject_LookupSpecialMethod` | dynamic |
| 0.42% | `python` | `gc_collect_region.isra.0` | gc |
| 0.39% | `python` | `PyUnicode_Contains` | str |
| 0.37% | `python` | `siphash13` | str |
| 0.36% | `python` | `unicode_splitlines` | str |
| 0.36% | `python` | `PyObject_GC_Del` | gc |
| 0.35% | `python` | `r_object` | import |
| 0.34% | `python` | `_PyFrame_MakeAndSetFrameObject` | unknown |
| 0.34% | `python` | `object_isinstance` | dynamic |
| 0.34% | `libc-2.31.so` | `__memcpy_avx_unaligned_erms` | libc |
| 0.33% | `python` | `dict_get` | dict |
| 0.32% | `python` | `visit_reachable` | gc |
| 0.32% | `python` | `PyObject_GetOptionalAttr` | dynamic |
| 0.32% | `python` | `slot_tp_init` | unknown |
| 0.31% | `python` | `frame_dealloc` | memory |
| 0.31% | `python` | `Py_XDECREF.lto_priv.7` | unknown |
| 0.31% | `python` | `long_hash` | int |
| 0.30% | `python` | `method_vectorcall` | calls |
| 0.29% | `python` | `object_new` | memory |
| 0.29% | `python` | `PyObject_Hash` | dynamic |
| 0.28% | `[kernel.kallsyms]` | `clear_bhb_loop` | kernel |
| 0.27% | `python` | `PyObject_Vectorcall` | dynamic |
| 0.27% | `python` | `PyUnicode_FromKindAndData` | str |
| 0.27% | `python` | `make_dict_from_instance_attributes` | unknown |
| 0.26% | `python` | `long_mod` | int |

## mako

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 40.68% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 7.35% | `python` | `unicode_replace` | str |
| 6.60% | `python` | `long_to_decimal_string_internal` | int |
| 4.17% | `python` | `_PyUnicode_JoinArray` | str |
| 2.56% | `python` | `dequeiter_next_lock_held.isra.0` | miscobj |
| 2.54% | `python` | `PyUnicode_New` | memory |
| 2.20% | `python` | `unicode_dealloc` | memory |
| 2.18% | `libc-2.31.so` | `__memcpy_avx_unaligned_erms` | libc |
| 1.65% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.54% | `python` | `PyObject_Str` | dynamic |
| 1.32% | `python` | `_list_extend` | list |
| 1.27% | `python` | `list_dealloc` | memory |
| 1.25% | `python` | `deque_append_lock_held` | miscobj |
| 1.04% | `python` | `deque_append_impl` | miscobj |
| 0.94% | `python` | `sre_ucs2_charset.isra.0` | library |
| 0.92% | `python` | `type_new` | memory |
| 0.79% | `python` | `deque_clear` | miscobj |
| 0.55% | `python` | `deduce_unreachable` | gc |
| 0.54% | `python` | `PyLong_FromLong` | int |
| 0.51% | `[kernel.kallsyms]` | `native_irq_return_iret` | kernel |
| 0.50% | `python` | `intern_common.part.0` | str |
| 0.49% | `python` | `visit_decref` | gc |
| 0.46% | `python` | `_PyCode_New` | interpreter |
| 0.44% | `python` | `gc_collect_region.isra.0` | gc |
| 0.44% | `[kernel.kallsyms]` | `sync_regs` | kernel |
| 0.41% | `libc-2.31.so` | `_int_malloc` | libc |
| 0.36% | `[kernel.kallsyms]` | `clear_page_erms` | kernel |
| 0.34% | `python` | `visit_reachable` | gc |
| 0.33% | `python` | `r_object` | import |
| 0.30% | `python` | `memcpy@plt` | memory |
| 0.29% | `python` | `PyUnicode_FromKindAndData` | str |
| 0.25% | `python` | `dequeiter_next` | miscobj |
| 0.25% | `python` | `tuple_dealloc` | memory |

## mdp

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 35.10% | `python` | `tuple_hash` | tuple |
| 18.65% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 12.98% | `python` | `long_hash` | int |
| 5.80% | `python` | `dict_subscript` | dict |
| 3.17% | `python` | `tuple_richcompare` | tuple |
| 1.34% | `python` | `insertdict` | dict |
| 1.34% | `python` | `_PyLong_GCD` | int |
| 1.18% | `python` | `_PySuper_Lookup` | dynamic |
| 1.16% | `python` | `PyDict_GetItemRef` | dict |
| 1.00% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.96% | `python` | `builtin_sum` | unknown |
| 0.96% | `python` | `PyFunction_NewWithQualName` | memory |
| 0.62% | `python` | `_PyFloat_FromDouble_ConsumeInputs` | float |
| 0.57% | `python` | `set_contains_lock_held` | miscobj |
| 0.52% | `python` | `gen_dealloc` | memory |
| 0.52% | `python` | `tuple_dealloc` | memory |
| 0.51% | `python` | `gen_iternext` | miscobj |
| 0.51% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.50% | `python` | `listiter_dealloc` | memory |
| 0.47% | `python` | `PyObject_GetItem` | dynamic |
| 0.45% | `python` | `func_dealloc` | memory |
| 0.43% | `python` | `long_div` | int |
| 0.43% | `python` | `long_mul` | int |
| 0.43% | `python` | `_Py_MakeCoro` | unknown |
| 0.41% | `python` | `subtype_dealloc` | memory |
| 0.40% | `python` | `PyObject_RichCompare` | dynamic |
| 0.36% | `python` | `tp_new_wrapper` | memory |
| 0.35% | `python` | `list_iter` | list |
| 0.35% | `python` | `long_dealloc` | memory |
| 0.33% | `python` | `PyObject_GetAttr` | dynamic |
| 0.32% | `python` | `vectorcall_maybe.constprop.0` | unknown |
| 0.32% | `python` | `builtin_max` | unknown |
| 0.26% | `python` | `PyObject_Hash` | dynamic |

## meteor_contest

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 23.40% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 9.22% | `python` | `set_issubset_impl` | miscobj |
| 6.46% | `python` | `setiter_iternext` | miscobj |
| 5.30% | `python` | `set_lookkey` | miscobj |
| 5.22% | `python` | `set_difference` | miscobj |
| 4.81% | `python` | `set_dealloc` | memory |
| 4.17% | `python` | `builtin_min` | unknown |
| 2.89% | `python` | `list_dealloc` | memory |
| 2.02% | `python` | `set_add_entry` | miscobj |
| 1.57% | `python` | `list_subscript` | list |
| 1.30% | `python` | `long_richcompare` | int |
| 1.20% | `python` | `set_table_resize` | miscobj |
| 1.19% | `python` | `type_new` | memory |
| 1.09% | `python` | `set_intersection` | miscobj |
| 1.09% | `python` | `PyObject_RichCompare` | dynamic |
| 1.03% | `python` | `make_new_set` | memory |
| 1.03% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 1.00% | `python` | `set_iter` | miscobj |
| 0.86% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.82% | `python` | `setiter_dealloc` | memory |
| 0.77% | `python` | `PyObject_GC_Del` | gc |
| 0.72% | `python` | `deduce_unreachable` | gc |
| 0.67% | `python` | `_PyCode_New` | interpreter |
| 0.66% | `python` | `intern_common.part.0` | str |
| 0.64% | `python` | `set_merge_lock_held.part.0` | miscobj |
| 0.63% | `python` | `list_iter` | list |
| 0.55% | `python` | `visit_decref` | gc |
| 0.55% | `python` | `gc_collect_region.isra.0` | gc |
| 0.54% | `python` | `set_richcompare` | miscobj |
| 0.53% | `python` | `PyMem_Malloc` | memory |
| 0.47% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.47% | `python` | `r_object` | import |
| 0.42% | `python` | `set_difference_update_internal` | miscobj |
| 0.39% | `python` | `visit_reachable` | gc |
| 0.37% | `libc-2.31.so` | `__memcpy_avx_unaligned_erms` | libc |
| 0.35% | `python` | `PyUnicode_FromKindAndData` | str |
| 0.29% | `python` | `list_ass_slice_lock_held` | list |
| 0.29% | `python` | `PyObject_IsTrue` | dynamic |
| 0.29% | `python` | `tuple_dealloc` | memory |
| 0.28% | `python` | `siphash13` | str |
| 0.27% | `python` | `PyList_New` | memory |
| 0.27% | `python` | `PyObject_RichCompareBool` | dynamic |

## nbody

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 60.47% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 16.42% | `python` | `_PyFloat_FromDouble_ConsumeInputs` | float |
| 4.25% | `libm-2.31.so` | `__ieee754_pow_fma` | library |
| 2.53% | `python` | `float_dealloc` | memory |
| 1.31% | `python` | `float_pow` | float |
| 0.82% | `python` | `type_new` | memory |
| 0.49% | `python` | `deduce_unreachable` | gc |
| 0.45% | `python` | `intern_common.part.0` | str |
| 0.44% | `python` | `_PyCode_New` | interpreter |
| 0.41% | `python` | `PyObject_GC_Del` | gc |
| 0.41% | `libm-2.31.so` | `powf64` | library |
| 0.40% | `python` | `visit_decref` | gc |
| 0.39% | `python` | `gc_collect_region.isra.0` | gc |
| 0.36% | `python` | `_PyNumber_PowerNoMod` | dynamic |
| 0.31% | `python` | `r_object` | import |
| 0.29% | `python` | `visit_reachable` | gc |
| 0.28% | `python` | `list_iter` | list |
| 0.28% | `python` | `_PyFloat_ExactDealloc` | memory |

## networkx

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 12.96% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 8.57% | `python` | `visit_decref` | gc |
| 8.46% | `python` | `visit_add_to_container` | gc |
| 7.69% | `python` | `dict_traverse` | gc |
| 7.37% | `python` | `PyDict_GetItemRef` | dict |
| 6.88% | `python` | `visit_reachable` | gc |
| 4.99% | `python` | `set_contains_lock_held` | miscobj |
| 4.73% | `python` | `dictiter_iternextkey` | dict |
| 4.06% | `python` | `PyDict_Contains` | dict |
| 3.47% | `python` | `insertdict` | dict |
| 3.40% | `python` | `deduce_unreachable` | gc |
| 2.84% | `python` | `gc_collect_region.isra.0` | gc |
| 1.96% | `python` | `PyObject_GetAttr` | dynamic |
| 1.92% | `python` | `dict_dealloc` | memory |
| 1.84% | `python` | `dictresize` | dict |
| 0.72% | `python` | `dict_get` | dict |
| 0.67% | `libz.so.1.2.11` | `inflateBackEnd` | library |
| 0.67% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.61% | `python` | `unicode_eq.lto_priv.1` | str |
| 0.61% | `python` | `list_dealloc` | memory |
| 0.56% | `python` | `unicode_dealloc` | memory |
| 0.53% | `python` | `tuple_dealloc` | memory |
| 0.48% | `python` | `_PyObject_GetMethod` | dynamic |
| 0.46% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.45% | `python` | `siphash13` | str |
| 0.43% | `python` | `PyObject_GC_Del` | gc |
| 0.42% | `python` | `split` | str |
| 0.42% | `python` | `_PyGC_Collect` | gc |
| 0.37% | `libc-2.31.so` | `__memcmp_avx2_movbe` | libc |
| 0.35% | `python` | `method_vectorcall_VARARGS_KEYWORDS` | calls |
| 0.32% | `python` | `unicode_decode_utf8` | str |
| 0.31% | `python` | `PyObject_VectorcallMethod` | dynamic |
| 0.30% | `python` | `PyUnicode_New` | memory |
| 0.30% | `python` | `list_iter` | list |

## networkx_connected_components

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 13.41% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 8.62% | `python` | `visit_decref` | gc |
| 8.47% | `python` | `visit_add_to_container` | gc |
| 7.87% | `python` | `dict_traverse` | gc |
| 7.42% | `python` | `PyDict_GetItemRef` | dict |
| 6.95% | `python` | `visit_reachable` | gc |
| 6.37% | `python` | `set_contains_lock_held` | miscobj |
| 4.54% | `python` | `dictiter_iternextkey` | dict |
| 4.24% | `python` | `PyDict_Contains` | dict |
| 3.38% | `python` | `deduce_unreachable` | gc |
| 2.84% | `python` | `gc_collect_region.isra.0` | gc |
| 2.21% | `python` | `insertdict` | dict |
| 2.08% | `python` | `PyObject_GetAttr` | dynamic |
| 1.81% | `python` | `dict_dealloc` | memory |
| 0.74% | `python` | `dict_get` | dict |
| 0.71% | `python` | `unicode_eq.lto_priv.1` | str |
| 0.70% | `libz.so.1.2.11` | `inflateBackEnd` | library |
| 0.69% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.67% | `python` | `dictresize` | dict |
| 0.63% | `python` | `list_dealloc` | memory |
| 0.55% | `python` | `unicode_dealloc` | memory |
| 0.52% | `python` | `_PyObject_GetMethod` | dynamic |
| 0.49% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.46% | `python` | `siphash13` | str |
| 0.46% | `python` | `tuple_dealloc` | memory |
| 0.44% | `python` | `split` | str |
| 0.44% | `python` | `PyObject_GC_Del` | gc |
| 0.42% | `python` | `_PyGC_Collect` | gc |
| 0.41% | `libc-2.31.so` | `__memcmp_avx2_movbe` | libc |
| 0.41% | `python` | `set_dealloc` | memory |
| 0.39% | `python` | `method_vectorcall_VARARGS_KEYWORDS` | calls |
| 0.33% | `python` | `list_iter` | list |
| 0.33% | `python` | `PyObject_VectorcallMethod` | dynamic |
| 0.32% | `python` | `unicode_decode_utf8` | str |
| 0.32% | `python` | `PyUnicode_New` | memory |
| 0.28% | `python` | `_PyObject_Malloc` | memory |
| 0.27% | `python` | `set_merge_lock_held.part.0` | miscobj |

## networkx_k_core

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 15.10% | `python` | `PyDict_GetItemRef` | dict |
| 11.81% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 10.27% | `python` | `visit_add_to_container` | gc |
| 9.90% | `python` | `visit_decref` | gc |
| 8.76% | `python` | `visit_reachable` | gc |
| 7.60% | `python` | `dict_traverse` | gc |
| 4.32% | `python` | `insertdict` | dict |
| 3.76% | `python` | `PyDict_Contains` | dict |
| 3.58% | `python` | `list_remove` | list |
| 3.16% | `python` | `deduce_unreachable` | gc |
| 2.49% | `python` | `gc_collect_region.isra.0` | gc |
| 2.23% | `python` | `dictiter_iternextkey` | dict |
| 1.00% | `python` | `dict_dealloc` | memory |
| 0.97% | `python` | `list_dealloc` | memory |
| 0.96% | `python` | `PyObject_GetAttr` | dynamic |
| 0.94% | `python` | `dictresize` | dict |
| 0.66% | `python` | `PyUnicode_RichCompare` | str |
| 0.65% | `python` | `dict_get` | dict |
| 0.58% | `python` | `listiter_next` | list |
| 0.52% | `python` | `list_traverse` | gc |
| 0.46% | `python` | `long_dealloc` | memory |
| 0.43% | `python` | `_PyGC_Collect` | gc |
| 0.42% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.42% | `libc-2.31.so` | `__memcmp_avx2_movbe` | libc |
| 0.39% | `libc-2.31.so` | `__memcpy_avx_unaligned_erms` | libc |
| 0.39% | `python` | `PyObject_RichCompareBool` | dynamic |
| 0.29% | `libz.so.1.2.11` | `inflateBackEnd` | library |
| 0.27% | `python` | `PyObject_GC_Del` | gc |

## nqueens

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 40.48% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 4.44% | `python` | `set_vectorcall` | miscobj |
| 3.17% | `python` | `list_dealloc` | memory |
| 2.82% | `python` | `PyFunction_NewWithQualName` | memory |
| 2.21% | `python` | `gen_iternext` | miscobj |
| 2.21% | `python` | `set_dealloc` | memory |
| 1.64% | `python` | `list_subscript` | list |
| 1.43% | `python` | `func_dealloc` | memory |
| 1.39% | `python` | `gen_dealloc` | memory |
| 1.30% | `python` | `_Py_MakeCoro` | unknown |
| 1.24% | `python` | `tuple_dealloc` | memory |
| 1.24% | `python` | `long_add` | int |
| 1.20% | `python` | `PyMem_Malloc` | memory |
| 1.14% | `python` | `_PyBuildSlice_Consume2` | unknown |
| 1.10% | `python` | `slice_dealloc` | memory |
| 1.07% | `python` | `PyList_New` | memory |
| 1.05% | `python` | `type_new` | memory |
| 1.00% | `python` | `list_ass_slice_lock_held` | list |
| 0.86% | `python` | `PyLong_FromLong` | int |
| 0.77% | `python` | `PyNumber_AsSsize_t` | dynamic |
| 0.76% | `python` | `list_ass_subscript` | list |
| 0.71% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.70% | `python` | `PyObject_Free` | dynamic |
| 0.61% | `python` | `long_sub` | int |
| 0.57% | `python` | `_PyCode_New` | interpreter |
| 0.55% | `python` | `intern_common.part.0` | str |
| 0.52% | `python` | `deduce_unreachable` | gc |
| 0.52% | `python` | `range_vectorcall` | miscobj |
| 0.50% | `python` | `PySequence_Tuple` | dynamic |
| 0.50% | `python` | `meth_dealloc` | memory |
| 0.49% | `python` | `method_get` | dynamic |
| 0.49% | `python` | `visit_decref` | gc |
| 0.48% | `python` | `range_iter` | miscobj |
| 0.48% | `python` | `list_iter` | list |
| 0.47% | `python` | `_PyObject_LookupSpecial` | dynamic |
| 0.47% | `python` | `gc_collect_region.isra.0` | gc |
| 0.45% | `python` | `_PyObject_GC_NewVar` | gc |
| 0.44% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 0.44% | `python` | `PyObject_GetItem` | dynamic |
| 0.43% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.42% | `python` | `listiter_dealloc` | memory |
| 0.40% | `python` | `list_new_prealloc` | memory |
| 0.40% | `libc-2.31.so` | `__memcpy_avx_unaligned_erms` | libc |
| 0.39% | `python` | `range_reverse` | miscobj |
| 0.39% | `python` | `long_hash` | int |
| 0.39% | `python` | `_PyTuple_FromStackRefSteal` | tuple |
| 0.38% | `python` | `visit_reachable` | gc |
| 0.36% | `python` | `_PyObject_Realloc` | memory |
| 0.35% | `python` | `r_object` | import |
| 0.33% | `python` | `_PyTuple_Resize` | tuple |
| 0.33% | `python` | `PyObject_GetIter` | dynamic |
| 0.31% | `python` | `PySlice_Unpack` | miscobj |
| 0.31% | `python` | `PyNumber_Negative` | dynamic |
| 0.30% | `python` | `PyObject_GC_Del` | gc |
| 0.28% | `python` | `range_dealloc` | memory |
| 0.27% | `python` | `PyUnicode_FromKindAndData` | str |

## pathlib

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 12.55% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 2.53% | `python` | `long_dealloc` | memory |
| 2.25% | `python` | `ScandirIterator_iternext` | unknown |
| 1.63% | `[kernel.kallsyms]` | `__d_lookup_rcu` | kernel |
| 1.50% | `libpthread-2.31.so` | `__pthread_mutex_lock` | library |
| 1.45% | `python` | `PyUnicode_DecodeFSDefault` | str |
| 1.38% | `python` | `k_mul` | int |
| 1.34% | `[kernel.kallsyms]` | `ext4_htree_store_dirent` | kernel |
| 1.31% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.30% | `[kernel.kallsyms]` | `__ext4fs_dirhash` | kernel |
| 1.28% | `python` | `_PyLong_New` | memory |
| 1.26% | `libpthread-2.31.so` | `pthread_mutex_unlock` | library |
| 1.24% | `python` | `unicode_decode_utf8` | str |
| 1.23% | `[kernel.kallsyms]` | `memset_erms` | kernel |
| 1.14% | `python` | `take_gil` | gil |
| 1.03% | `python` | `path_converter` | unknown |
| 0.99% | `python` | `x_add` | int |
| 0.96% | `python` | `type_new` | memory |
| 0.91% | `[kernel.kallsyms]` | `filldir64` | kernel |
| 0.82% | `python` | `tuple_dealloc` | memory |
| 0.81% | `python` | `_sre_SRE_Pattern_match` | library |
| 0.79% | `python` | `PyLong_FromLong` | int |
| 0.76% | `[kernel.kallsyms]` | `kmem_cache_alloc` | kernel |
| 0.73% | `python` | `tp_new_wrapper` | memory |
| 0.68% | `python` | `unicode_dealloc` | memory |
| 0.68% | `[kernel.kallsyms]` | `clear_bhb_loop` | kernel |
| 0.68% | `[kernel.kallsyms]` | `strncpy_from_user` | kernel |
| 0.67% | `[kernel.kallsyms]` | `copy_user_enhanced_fast_string` | kernel |
| 0.66% | `python` | `slot_tp_init` | unknown |
| 0.65% | `python` | `sre_ucs1_match` | library |
| 0.64% | `[kernel.kallsyms]` | `link_path_walk.part.0` | kernel |
| 0.62% | `python` | `_PyObject_LookupSpecial` | dynamic |
| 0.61% | `python` | `vectorcall_method` | calls |
| 0.58% | `python` | `_Py_type_getattro` | lookup |
| 0.58% | `python` | `structseq_dealloc` | memory |
| 0.57% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.57% | `libc-2.31.so` | `_int_malloc` | libc |
| 0.55% | `python` | `clear_slots` | unknown |
| 0.55% | `python` | `fill_time` | unknown |
| 0.53% | `[kernel.kallsyms]` | `__slab_free` | kernel |
| 0.53% | `python` | `object_isinstance` | dynamic |
| 0.53% | `python` | `PyObject_GC_Del` | gc |
| 0.52% | `[kernel.kallsyms]` | `str2hashbuf_signed` | kernel |
| 0.52% | `python` | `list_dealloc` | memory |
| 0.52% | `python` | `deduce_unreachable` | gc |
| 0.52% | `python` | `visit_decref` | gc |
| 0.51% | `[kernel.kallsyms]` | `syscall_return_via_sysret` | kernel |
| 0.50% | `python` | `method_vectorcall` | calls |
| 0.50% | `[kernel.kallsyms]` | `ext4_getattr` | kernel |
| 0.50% | `[kernel.kallsyms]` | `rb_insert_color` | kernel |
| 0.50% | `python` | `get_type_attr_as_size` | unknown |
| 0.49% | `python` | `subtype_dealloc` | memory |
| 0.49% | `python` | `intern_common.part.0` | str |
| 0.48% | `[kernel.kallsyms]` | `rb_next` | kernel |
| 0.48% | `python` | `_PyCode_New` | interpreter |
| 0.47% | `[kernel.kallsyms]` | `security_inode_getattr` | kernel |
| 0.47% | `python` | `_Py_dict_lookup` | lookup |
| 0.45% | `python` | `PyDict_GetItemRef` | dict |
| 0.45% | `[kernel.kallsyms]` | `__ext4_check_dir_entry` | kernel |
| 0.45% | `python` | `gc_collect_region.isra.0` | gc |
| 0.44% | `libc-2.31.so` | `__strcpy_avx2` | libc |
| 0.44% | `[kernel.kallsyms]` | `entry_SYSCALL_64` | kernel |
| 0.42% | `[kernel.kallsyms]` | `__kmalloc` | kernel |
| 0.42% | `libc-2.31.so` | `__xstat64` | libc |
| 0.42% | `python` | `_PyTuple_FromStackRefSteal` | tuple |
| 0.41% | `python` | `_PyObject_GC_NewVar` | gc |
| 0.41% | `python` | `slot_tp_new` | memory |
| 0.40% | `[kernel.kallsyms]` | `lookup_fast` | kernel |
| 0.39% | `[kernel.kallsyms]` | `do_syscall_64` | kernel |
| 0.39% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.37% | `python` | `visit_reachable` | gc |
| 0.37% | `[kernel.kallsyms]` | `kfree` | kernel |
| 0.37% | `python` | `_PyObject_New` | memory |
| 0.37% | `python` | `PyEval_SaveThread` | interpreter |
| 0.37% | `python` | `Py_XDECREF.lto_priv.1` | unknown |
| 0.36% | `python` | `object_dealloc` | memory |
| 0.36% | `[kernel.kallsyms]` | `__virt_addr_valid` | kernel |
| 0.35% | `python` | `PyMem_Malloc` | memory |
| 0.35% | `[kernel.kallsyms]` | `in_group_p` | kernel |
| 0.35% | `python` | `r_object` | import |
| 0.34% | `python` | `_PyArg_UnpackKeywords` | calls |
| 0.33% | `libc-2.31.so` | `__memcpy_avx_unaligned_erms` | libc |
| 0.32% | `[kernel.kallsyms]` | `generic_permission` | kernel |
| 0.32% | `python` | `tuple_iter` | tuple |
| 0.32% | `python` | `PyObject_Free` | dynamic |
| 0.32% | `libc-2.31.so` | `_int_free` | libc |
| 0.32% | `[kernel.kallsyms]` | `kmem_cache_free` | kernel |
| 0.31% | `python` | `PyUnicode_DecodeFSDefaultAndSize` | str |
| 0.30% | `[kernel.kallsyms]` | `walk_component` | kernel |
| 0.30% | `python` | `PyMem_Free` | memory |
| 0.30% | `python` | `PyLong_FromUnsignedLongLong` | int |
| 0.29% | `[kernel.kallsyms]` | `call_filldir` | kernel |
| 0.29% | `[kernel.kallsyms]` | `ext4_find_dest_de` | kernel |
| 0.29% | `python` | `PyFloat_FromDouble` | float |
| 0.28% | `[kernel.kallsyms]` | `set_root` | kernel |
| 0.27% | `python` | `_PyFunction_Vectorcall` | calls |
| 0.27% | `python` | `method_dealloc` | memory |
| 0.26% | `python` | `listiter_next` | list |
| 0.26% | `[kernel.kallsyms]` | `memcpy_erms` | kernel |
| 0.26% | `[kernel.kallsyms]` | `vfs_getattr_nosec` | kernel |
| 0.26% | `[kernel.kallsyms]` | `ext4_search_dir` | kernel |
| 0.26% | `python` | `_PyObject_Malloc` | memory |
| 0.25% | `python` | `PyUnicode_FromKindAndData` | str |

## pickle_pure_python

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 43.85% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 3.94% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 2.27% | `python` | `bytes_concat` | str |
| 2.14% | `python` | `tuple_dealloc` | memory |
| 1.92% | `python` | `unicode_encode` | str |
| 1.78% | `python` | `dict_get` | dict |
| 1.76% | `python` | `_PyLong_New` | memory |
| 1.68% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 1.44% | `python` | `object_dealloc` | memory |
| 1.42% | `python` | `PyDict_GetItemRef` | dict |
| 1.40% | `python` | `type_new` | memory |
| 1.22% | `python` | `insertdict` | dict |
| 1.19% | `python` | `long_dealloc` | memory |
| 1.00% | `python` | `write_bytes` | unknown |
| 0.93% | `libc-2.31.so` | `__memcpy_avx_unaligned_erms` | libc |
| 0.78% | `python` | `intern_common.part.0` | str |
| 0.77% | `python` | `deduce_unreachable` | gc |
| 0.77% | `python` | `unicode_encode_utf8` | str |
| 0.74% | `python` | `_PyCode_New` | interpreter |
| 0.67% | `python` | `gc_collect_region.isra.0` | gc |
| 0.67% | `python` | `_PyTuple_Resize` | tuple |
| 0.66% | `python` | `visit_decref` | gc |
| 0.64% | `python` | `PyDict_Contains` | dict |
| 0.61% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.56% | `_struct.cpython-314-x86_64-linux-gnu.so` | `s_pack` | library |
| 0.54% | `python` | `visit_reachable` | gc |
| 0.53% | `python` | `long_hash` | int |
| 0.53% | `python` | `PySys_Audit` | unknown |
| 0.51% | `python` | `r_object` | import |
| 0.45% | `python` | `PyUnicode_FromKindAndData` | str |
| 0.42% | `python` | `_PyTuple_FromStackRefSteal` | tuple |
| 0.41% | `python` | `_PyObject_GenericGetAttrWithDict` | dynamic |
| 0.38% | `libc-2.31.so` | `_int_malloc` | libc |
| 0.34% | `python` | `siphash13` | str |
| 0.33% | `python` | `dictiter_iternextitem` | dict |
| 0.33% | `python` | `PyNumber_Add` | dynamic |
| 0.32% | `python` | `builtin_id` | unknown |
| 0.32% | `python` | `dict_dealloc` | memory |
| 0.32% | `python` | `builtin_getattr` | lookup |
| 0.30% | `libc-2.31.so` | `__memset_avx2_erms` | libc |
| 0.29% | `_struct.cpython-314-x86_64-linux-gnu.so` | `pack` | library |
| 0.28% | `python` | `_PyBytesWriter_Finish` | unknown |
| 0.27% | `python` | `unicode_dealloc` | memory |
| 0.27% | `python` | `find_name_in_mro` | lookup |
| 0.27% | `python` | `PyObject_GetAttr` | dynamic |
| 0.27% | `python` | `PyObject_Free` | dynamic |

## pidigits

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 34.58% | `python` | `x_divrem` | int |
| 20.58% | `python` | `k_mul` | int |
| 13.23% | `python` | `x_add` | int |
| 8.36% | `python` | `x_sub` | int |
| 4.34% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 1.67% | `libc-2.31.so` | `_int_malloc` | libc |
| 1.02% | `libc-2.31.so` | `__memset_avx2_erms` | libc |
| 0.82% | `python` | `type_new` | memory |
| 0.63% | `libc-2.31.so` | `_int_free` | libc |
| 0.49% | `python` | `intern_common.part.0` | str |
| 0.49% | `python` | `deduce_unreachable` | gc |
| 0.46% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.44% | `python` | `_PyCode_New` | interpreter |
| 0.41% | `python` | `visit_decref` | gc |
| 0.39% | `python` | `gc_collect_region.isra.0` | gc |
| 0.38% | `python` | `long_dealloc` | memory |
| 0.34% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.32% | `libc-2.31.so` | `unlink_chunk.isra.0` | libc |
| 0.32% | `python` | `visit_reachable` | gc |
| 0.32% | `python` | `r_object` | import |
| 0.32% | `python` | `tuple_dealloc` | memory |
| 0.27% | `python` | `long_mul` | int |
| 0.26% | `libc-2.31.so` | `__libc_malloc` | libc |
| 0.25% | `python` | `PyUnicode_FromKindAndData` | str |

## pprint

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 47.55% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 5.38% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 2.84% | `python` | `long_to_decimal_string_internal` | int |
| 2.71% | `python` | `PyUnicode_Format` | str |
| 2.67% | `python` | `_Py_type_getattro_impl` | dynamic |
| 2.52% | `python` | `tuple_dealloc` | memory |
| 2.29% | `python` | `_PyUnicode_JoinArray` | str |
| 1.95% | `python` | `unicode_dealloc` | memory |
| 1.41% | `python` | `_PyTuple_FromStackRefSteal` | tuple |
| 1.24% | `python` | `PyUnicode_New` | memory |
| 1.14% | `python` | `_PyUnicodeWriter_PrepareInternal` | str |
| 1.00% | `python` | `slot_tp_init` | unknown |
| 0.93% | `python` | `list_dealloc` | memory |
| 0.92% | `python` | `PyObject_GetAttr` | dynamic |
| 0.90% | `libc-2.31.so` | `__memcpy_avx_unaligned_erms` | libc |
| 0.86% | `python` | `PyDict_Contains` | dict |
| 0.85% | `python` | `set_contains_lock_held` | miscobj |
| 0.80% | `python` | `meth_dealloc` | memory |
| 0.80% | `python` | `slot_tp_richcompare` | dynamic |
| 0.80% | `python` | `method_get` | dynamic |
| 0.74% | `python` | `builtin_issubclass` | unknown |
| 0.71% | `python` | `object_new` | memory |
| 0.71% | `python` | `insertdict` | dict |
| 0.68% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.68% | `python` | `_PyObject_MakeTpCall` | dynamic |
| 0.66% | `python` | `builtin_sorted` | unknown |
| 0.61% | `python` | `long_hash` | int |
| 0.59% | `python` | `_PyObject_Malloc` | memory |
| 0.58% | `python` | `PyObject_GC_Del` | gc |
| 0.52% | `python` | `builtin_getattr` | lookup |
| 0.49% | `python` | `_PyLong_New` | memory |
| 0.49% | `python` | `list_iter` | list |
| 0.48% | `python` | `list_sort_impl` | list |
| 0.47% | `python` | `list_append` | list |
| 0.45% | `python` | `tuple_iter` | tuple |
| 0.44% | `python` | `subtype_dealloc` | memory |
| 0.42% | `python` | `PyDict_DelItem` | dict |
| 0.38% | `python` | `unicode_repr` | str |
| 0.37% | `python` | `_Py_dict_lookup` | lookup |
| 0.37% | `python` | `builtin_repr` | unknown |
| 0.34% | `python` | `PyList_New` | memory |
| 0.31% | `python` | `long_dealloc` | memory |
| 0.30% | `python` | `clear_slots` | unknown |
| 0.29% | `python` | `tupleiter_dealloc` | memory |
| 0.28% | `python` | `_PyArg_UnpackKeywords` | calls |
| 0.27% | `python` | `PyObject_Hash` | dynamic |
| 0.26% | `python` | `_PyFunction_Vectorcall` | calls |
| 0.25% | `python` | `wrapperdescr_call` | unknown |

## pycparser

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 36.54% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 14.74% | `python` | `sre_ucs1_match` | library |
| 2.80% | `python` | `_sre_SRE_Pattern_match` | library |
| 2.48% | `python` | `PyDict_GetItemRef` | dict |
| 2.14% | `python` | `deduce_unreachable` | gc |
| 2.03% | `python` | `gc_collect_region.isra.0` | gc |
| 1.61% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.56% | `python` | `dict_get` | dict |
| 1.41% | `python` | `object_new` | memory |
| 1.32% | `libc-2.31.so` | `_int_malloc` | libc |
| 1.15% | `python` | `subtype_dealloc` | memory |
| 1.13% | `python` | `list_ass_slice_lock_held` | list |
| 1.09% | `python` | `visit_decref` | gc |
| 1.01% | `python` | `subtype_traverse` | gc |
| 0.89% | `python` | `object_isinstance` | dynamic |
| 0.86% | `python` | `visit_add_to_container` | gc |
| 0.79% | `python` | `sre_ucs1_count` | library |
| 0.78% | `python` | `list_dealloc` | memory |
| 0.72% | `python` | `PyObject_GC_Del` | gc |
| 0.71% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.65% | `python` | `slot_mp_ass_subscript` | unknown |
| 0.63% | `libc-2.31.so` | `__memcpy_avx_unaligned_erms` | libc |
| 0.63% | `libc-2.31.so` | `_int_free` | libc |
| 0.62% | `python` | `PyDict_Contains` | dict |
| 0.61% | `python` | `list_subscript` | list |
| 0.60% | `python` | `visit_reachable` | gc |
| 0.59% | `python` | `PyObject_GetAttr` | dynamic |
| 0.55% | `python` | `_PyObject_MakeTpCall` | dynamic |
| 0.54% | `python` | `sre_ucs2_charset.isra.0` | library |
| 0.54% | `python` | `slice_dealloc` | memory |
| 0.53% | `python` | `PyNumber_Negative` | dynamic |
| 0.51% | `python` | `slot_tp_init` | unknown |
| 0.51% | `python` | `PySlice_New` | memory |
| 0.48% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.44% | `libc-2.31.so` | `__libc_malloc` | libc |
| 0.43% | `python` | `PyMem_Malloc` | memory |
| 0.42% | `python` | `long_dealloc` | memory |
| 0.40% | `python` | `PySlice_Unpack` | miscobj |
| 0.40% | `python` | `_PyFunction_Vectorcall` | calls |
| 0.37% | `python` | `PyObject_Vectorcall` | dynamic |
| 0.37% | `python` | `list_ass_subscript` | list |
| 0.34% | `python` | `PyList_New` | memory |
| 0.34% | `python` | `_PyObject_Malloc` | memory |
| 0.32% | `libc-2.31.so` | `unlink_chunk.isra.0` | libc |
| 0.31% | `python` | `list_resize` | list |
| 0.31% | `python` | `vectorcall_method` | calls |
| 0.29% | `python` | `insertdict` | dict |
| 0.28% | `python` | `_PyGC_Collect` | gc |
| 0.28% | `python` | `_PyLong_New` | memory |
| 0.26% | `python` | `PyObject_SetAttr` | dynamic |
| 0.25% | `python` | `list_iter` | list |

## pyflate

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 44.06% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 7.58% | `python` | `list_dealloc` | memory |
| 5.79% | `python` | `list_ass_slice_lock_held` | list |
| 2.81% | `python` | `list_subscript` | list |
| 2.67% | `python` | `long_dealloc` | memory |
| 2.27% | `python` | `bytes_subscript` | str |
| 1.95% | `python` | `list_concat` | list |
| 1.94% | `python` | `long_add` | int |
| 1.92% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.81% | `libc-2.31.so` | `_int_malloc` | libc |
| 1.38% | `python` | `long_sub` | int |
| 1.29% | `python` | `stringlib_bytes_join.lto_priv.1` | str |
| 1.26% | `python` | `long_lshift_method` | int |
| 1.26% | `python` | `_PyLong_New` | memory |
| 1.00% | `python` | `PyObject_Free` | dynamic |
| 0.94% | `python` | `PySlice_Unpack` | miscobj |
| 0.93% | `libc-2.31.so` | `__memcpy_avx_unaligned_erms` | libc |
| 0.86% | `python` | `list_sort_impl` | list |
| 0.68% | `python` | `unsafe_long_compare` | unknown |
| 0.65% | `libc-2.31.so` | `_int_free` | libc |
| 0.61% | `python` | `long_rshift` | int |
| 0.58% | `python` | `PyObject_GetItem` | dynamic |
| 0.57% | `python` | `PyNumber_AsSsize_t` | dynamic |
| 0.52% | `python` | `long_and` | int |
| 0.52% | `python` | `_PyBuildSlice_Consume2` | unknown |
| 0.50% | `python` | `slice_dealloc` | memory |
| 0.46% | `python` | `PyMem_Malloc` | memory |
| 0.40% | `libc-2.31.so` | `unlink_chunk.isra.0` | libc |
| 0.39% | `python` | `enum_next` | miscobj |
| 0.33% | `python` | `PyList_New` | memory |
| 0.33% | `python` | `_PyLong_FromSTwoDigits` | int |
| 0.33% | `python` | `list_new_prealloc` | memory |
| 0.32% | `python` | `type_new` | memory |
| 0.32% | `python` | `PyLong_FromLong` | int |
| 0.32% | `python` | `PyNumber_Lshift` | dynamic |
| 0.31% | `python` | `list_iter` | list |
| 0.26% | `python` | `PyNumber_And` | dynamic |
| 0.26% | `libc-2.31.so` | `__libc_malloc` | libc |

## pylint

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 25.03% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 9.31% | `python` | `deduce_unreachable` | gc |
| 7.69% | `python` | `gc_collect_region.isra.0` | gc |
| 4.52% | `python` | `visit_decref` | gc |
| 3.66% | `python` | `visit_reachable` | gc |
| 2.35% | `python` | `visit_add_to_container` | gc |
| 1.77% | `python` | `subtype_traverse` | gc |
| 1.76% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.55% | `python` | `PyDict_GetItemRef` | dict |
| 1.50% | `python` | `PyObject_GetAttr` | dynamic |
| 1.02% | `python` | `dict_traverse` | gc |
| 0.98% | `python` | `list_traverse` | gc |
| 0.88% | `python` | `object_isinstance` | dynamic |
| 0.85% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.83% | `python` | `tuple_dealloc` | memory |
| 0.79% | `python` | `PyObject_SetAttr` | dynamic |
| 0.76% | `python` | `_PyObject_GetMethod` | dynamic |
| 0.75% | `python` | `_PyFunction_Vectorcall` | calls |
| 0.73% | `python` | `dict_dealloc` | memory |
| 0.70% | `python` | `find_name_in_mro` | lookup |
| 0.68% | `python` | `insertdict` | dict |
| 0.64% | `python` | `list_dealloc` | memory |
| 0.59% | `python` | `_PyGC_Collect` | gc |
| 0.58% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.51% | `python` | `type_new` | memory |
| 0.51% | `python` | `intern_common.part.0` | str |
| 0.51% | `python` | `subtype_dealloc` | memory |
| 0.44% | `python` | `_Py_MakeCoro` | unknown |
| 0.44% | `libc-2.31.so` | `__memcpy_avx_unaligned_erms` | libc |
| 0.43% | `python` | `gen_dealloc` | memory |
| 0.40% | `python` | `islice_next` | unknown |
| 0.40% | `python` | `PyObject_GC_Del` | gc |
| 0.37% | `python` | `_PySuper_Lookup` | dynamic |
| 0.35% | `python` | `PyMem_Free` | memory |
| 0.32% | `python` | `_PyObject_MakeTpCall` | dynamic |
| 0.32% | `python` | `unicode_dealloc` | memory |
| 0.32% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.31% | `python` | `list_iter` | list |
| 0.30% | `python` | `_PyObject_GC_New` | gc |
| 0.30% | `python` | `_PyCode_New` | interpreter |
| 0.29% | `python` | `object_new` | memory |
| 0.29% | `python` | `siphash13` | str |
| 0.29% | `python` | `tok_get_normal_mode` | compiler |
| 0.28% | `python` | `_Py_slot_tp_getattr_hook` | unknown |
| 0.27% | `python` | `_PyStack_UnpackDict` | unknown |
| 0.27% | `python` | `slot_tp_init` | unknown |
| 0.27% | `python` | `set_dealloc` | memory |
| 0.25% | `python` | `PyFunction_NewWithQualName` | memory |

## python_startup

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 9.03% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 5.96% | `python` | `type_new` | memory |
| 3.35% | `python` | `intern_common.part.0` | str |
| 3.31% | `python` | `_PyCode_New` | interpreter |
| 2.67% | `python` | `visit_decref` | gc |
| 2.54% | `python` | `deduce_unreachable` | gc |
| 2.49% | `python` | `r_object` | import |
| 1.95% | `python` | `gc_collect_region.isra.0` | gc |
| 1.90% | `python` | `PyUnicode_FromKindAndData` | str |
| 1.89% | `python` | `visit_reachable` | gc |
| 1.57% | `python` | `siphash13` | str |
| 1.17% | `libc-2.31.so` | `__memcpy_avx_unaligned_erms` | libc |
| 1.09% | `python` | `tuple_dealloc` | memory |
| 1.05% | `python` | `find_name_in_mro` | lookup |
| 0.88% | `python` | `unicode_dealloc` | memory |
| 0.87% | `python` | `type_ready` | dynamic |
| 0.87% | `python` | `insertdict` | dict |
| 0.81% | `[kernel.kallsyms]` | `filemap_map_pages` | kernel |
| 0.79% | `python` | `dict_traverse` | gc |
| 0.76% | `python` | `PyDict_GetItemRef` | dict |
| 0.76% | `python` | `PyDict_SetItem` | dict |
| 0.71% | `[kernel.kallsyms]` | `native_irq_return_iret` | kernel |
| 0.66% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.66% | `python` | `dictresize` | dict |
| 0.63% | `libc-2.31.so` | `_int_malloc` | libc |
| 0.62% | `ld-2.31.so` | `do_lookup_x` | library |
| 0.57% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.54% | `python` | `PyBytes_FromStringAndSize` | str |
| 0.52% | `python` | `dict_dealloc` | memory |
| 0.51% | `python` | `_Py_dict_lookup` | lookup |
| 0.48% | `[kernel.kallsyms]` | `sync_regs` | kernel |
| 0.47% | `python` | `_PyEval_LoadGlobalStackRef` | interpreter |
| 0.47% | `libc-2.31.so` | `__strlen_avx2` | libc |
| 0.45% | `libc-2.31.so` | `wcsrtombs` | libc |
| 0.43% | `python` | `tuple_traverse` | gc |
| 0.42% | `python` | `list_dealloc` | memory |
| 0.41% | `python` | `code_dealloc` | memory |
| 0.39% | `python` | `_PyObject_GC_NewVar` | gc |
| 0.38% | `python` | `PyFunction_NewWithQualName` | memory |
| 0.38% | `libc-2.31.so` | `__memcmp_avx2_movbe` | libc |
| 0.34% | `[kernel.kallsyms]` | `clear_page_erms` | kernel |
| 0.34% | `python` | `PyType_GenericAlloc` | memory |
| 0.33% | `libc-2.31.so` | `__gconv_transform_internal_utf8` | libc |
| 0.31% | `python` | `func_dealloc` | memory |
| 0.31% | `python` | `_add_methods_to_object` | unknown |
| 0.31% | `python` | `object_dealloc` | memory |
| 0.31% | `ld-2.31.so` | `strcmp` | library |
| 0.30% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.30% | `python` | `PyTuple_New` | memory |
| 0.28% | `python` | `PyUnicode_FromString` | str |
| 0.28% | `[kernel.kallsyms]` | `zap_pte_range.isra.0` | kernel |
| 0.27% | `python` | `set_traverse` | gc |
| 0.27% | `libc-2.31.so` | `_int_free` | libc |
| 0.27% | `python` | `PyObject_GetAttr` | dynamic |
| 0.27% | `[kernel.kallsyms]` | `__d_lookup_rcu` | kernel |
| 0.27% | `python` | `PyObject_GetOptionalAttr` | dynamic |
| 0.27% | `python` | `_Py_module_getattro` | unknown |
| 0.27% | `python` | `func_traverse` | gc |
| 0.26% | `ld-2.31.so` | `_dl_relocate_object` | library |
| 0.26% | `python` | `subtype_dealloc` | memory |
| 0.26% | `python` | `dictkeys_decref.part.0` | unknown |
| 0.25% | `[kernel.kallsyms]` | `ext4_htree_store_dirent` | kernel |
| 0.25% | `[kernel.kallsyms]` | `__handle_mm_fault` | kernel |

## python_startup_no_site

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 8.20% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 5.63% | `python` | `type_new` | memory |
| 3.70% | `python` | `intern_common.part.0` | str |
| 3.35% | `python` | `_PyCode_New` | interpreter |
| 2.92% | `python` | `deduce_unreachable` | gc |
| 2.68% | `python` | `visit_decref` | gc |
| 2.51% | `python` | `r_object` | import |
| 2.19% | `python` | `gc_collect_region.isra.0` | gc |
| 2.00% | `python` | `visit_reachable` | gc |
| 1.91% | `python` | `PyUnicode_FromKindAndData` | str |
| 1.64% | `python` | `siphash13` | str |
| 1.10% | `libc-2.31.so` | `__memcpy_avx_unaligned_erms` | libc |
| 1.04% | `ld-2.31.so` | `do_lookup_x` | library |
| 1.03% | `python` | `insertdict` | dict |
| 1.01% | `ld-2.31.so` | `_dl_relocate_object` | library |
| 0.97% | `[kernel.kallsyms]` | `native_irq_return_iret` | kernel |
| 0.94% | `python` | `type_ready` | dynamic |
| 0.93% | `python` | `find_name_in_mro` | lookup |
| 0.92% | `python` | `tuple_dealloc` | memory |
| 0.89% | `python` | `unicode_dealloc` | memory |
| 0.83% | `python` | `dict_traverse` | gc |
| 0.78% | `[kernel.kallsyms]` | `filemap_map_pages` | kernel |
| 0.69% | `python` | `PyDict_GetItemRef` | dict |
| 0.65% | `libc-2.31.so` | `wcsrtombs` | libc |
| 0.65% | `ld-2.31.so` | `strcmp` | library |
| 0.64% | `python` | `dictresize` | dict |
| 0.63% | `[kernel.kallsyms]` | `sync_regs` | kernel |
| 0.60% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.60% | `libc-2.31.so` | `_int_malloc` | libc |
| 0.58% | `python` | `_Py_dict_lookup` | lookup |
| 0.53% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.53% | `libc-2.31.so` | `__strlen_avx2` | libc |
| 0.52% | `python` | `PyDict_SetItem` | dict |
| 0.52% | `python` | `PyBytes_FromStringAndSize` | str |
| 0.51% | `libc-2.31.so` | `__gconv_transform_internal_utf8` | libc |
| 0.51% | `python` | `dict_dealloc` | memory |
| 0.50% | `[kernel.kallsyms]` | `clear_page_erms` | kernel |
| 0.49% | `python` | `_add_methods_to_object` | unknown |
| 0.44% | `python` | `_PyObject_GC_NewVar` | gc |
| 0.42% | `ld-2.31.so` | `_dl_lookup_symbol_x` | library |
| 0.41% | `python` | `tuple_traverse` | gc |
| 0.40% | `[kernel.kallsyms]` | `copy_page` | kernel |
| 0.40% | `[kernel.kallsyms]` | `zap_pte_range.isra.0` | kernel |
| 0.39% | `python` | `PyType_GenericAlloc` | memory |
| 0.38% | `python` | `PyUnicode_FromString` | str |
| 0.38% | `python` | `code_dealloc` | memory |
| 0.38% | `python` | `PyFunction_NewWithQualName` | memory |
| 0.36% | `libc-2.31.so` | `_int_free` | libc |
| 0.35% | `python` | `_PyEval_LoadGlobalStackRef` | interpreter |
| 0.35% | `ld-2.31.so` | `check_match` | library |
| 0.32% | `python` | `_PyFunction_Vectorcall` | calls |
| 0.32% | `python` | `list_dealloc` | memory |
| 0.32% | `python` | `PyDict_SetItemString` | dict |
| 0.30% | `python` | `func_dealloc` | memory |
| 0.30% | `libc-2.31.so` | `_dl_addr` | libc |
| 0.29% | `python` | `PyTuple_New` | memory |
| 0.29% | `[kernel.kallsyms]` | `rmqueue` | kernel |
| 0.29% | `[kernel.kallsyms]` | `__handle_mm_fault` | kernel |
| 0.28% | `python` | `_PyObject_ClearFreeLists` | dynamic |
| 0.28% | `python` | `PyObject_SetAttr` | dynamic |
| 0.26% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.26% | `python` | `object_new` | memory |
| 0.26% | `[kernel.kallsyms]` | `release_pages` | kernel |
| 0.26% | `python` | `dictkeys_decref.part.0` | unknown |
| 0.26% | `python` | `func_traverse` | gc |
| 0.25% | `libc-2.31.so` | `__memcmp_avx2_movbe` | libc |

## raytrace

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 56.35% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 6.66% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 3.39% | `python` | `_PyFloat_FromDouble_ConsumeInputs` | float |
| 2.80% | `python` | `subtype_dealloc` | memory |
| 2.63% | `python` | `PyType_GenericAlloc` | memory |
| 1.87% | `python` | `PyObject_GC_Del` | gc |
| 1.68% | `python` | `vectorcall_maybe.constprop.0` | unknown |
| 1.66% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 1.12% | `python` | `PyNumber_Subtract` | dynamic |
| 1.03% | `python` | `float_sub` | float |
| 1.01% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.83% | `python` | `float_dealloc` | memory |
| 0.56% | `python` | `type_new` | memory |
| 0.56% | `python` | `tuple_dealloc` | memory |
| 0.54% | `python` | `long_dealloc` | memory |
| 0.49% | `python` | `PyLong_AsDouble` | int |
| 0.49% | `python` | `float_richcompare` | float |
| 0.46% | `python` | `float_mul` | float |
| 0.45% | `python` | `_PyFloat_ExactDealloc` | memory |
| 0.45% | `python` | `PyObject_RichCompare` | dynamic |
| 0.42% | `python` | `PyNumber_Multiply` | dynamic |
| 0.41% | `python` | `convert_to_double` | unknown |
| 0.37% | `python` | `_PyTuple_FromStackRefSteal` | tuple |
| 0.36% | `python` | `list_dealloc` | memory |
| 0.34% | `python` | `intern_common.part.0` | str |
| 0.30% | `python` | `deduce_unreachable` | gc |
| 0.28% | `python` | `_PyCode_New` | interpreter |
| 0.27% | `python` | `slot_nb_subtract` | unknown |
| 0.26% | `python` | `visit_decref` | gc |
| 0.26% | `python` | `float_add` | float |

## regex_compile

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 46.59% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 4.44% | `python` | `sre_ucs1_match` | library |
| 2.97% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 2.04% | `python` | `bytearray_ass_subscript` | miscobj |
| 1.43% | `python` | `long_dealloc` | memory |
| 1.39% | `python` | `PyLong_FromLong` | int |
| 1.11% | `python` | `object_isinstance` | dynamic |
| 1.09% | `python` | `PyObject_GetAttr` | dynamic |
| 1.06% | `python` | `sre_ucs2_charset.isra.0` | library |
| 1.01% | `python` | `list_dealloc` | memory |
| 1.00% | `python` | `tuple_dealloc` | memory |
| 0.86% | `python` | `type_new` | memory |
| 0.60% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.59% | `python` | `_PyTuple_FromStackRefSteal` | tuple |
| 0.59% | `python` | `PyMem_Free` | memory |
| 0.54% | `python` | `intern_common.part.0` | str |
| 0.54% | `python` | `sre_search` | library |
| 0.54% | `python` | `PyObject_GC_Del` | gc |
| 0.52% | `python` | `PyDict_GetItemRef` | dict |
| 0.48% | `python` | `slot_sq_item` | unknown |
| 0.48% | `python` | `vectorcall_method` | calls |
| 0.48% | `python` | `deduce_unreachable` | gc |
| 0.45% | `python` | `method_dealloc` | memory |
| 0.45% | `python` | `_PyCode_New` | interpreter |
| 0.44% | `python` | `meth_dealloc` | memory |
| 0.44% | `python` | `siphash13` | str |
| 0.43% | `python` | `gc_collect_region.isra.0` | gc |
| 0.43% | `python` | `PyUnicode_Contains` | str |
| 0.42% | `python` | `visit_decref` | gc |
| 0.42% | `libc-2.31.so` | `__memcpy_avx_unaligned_erms` | libc |
| 0.41% | `python` | `long_add` | int |
| 0.40% | `python` | `PyObject_SetItem` | dynamic |
| 0.39% | `python` | `subtype_dealloc` | memory |
| 0.39% | `python` | `_PyObject_Malloc` | memory |
| 0.38% | `python` | `frame_dealloc` | memory |
| 0.37% | `python` | `PyMem_Malloc` | memory |
| 0.37% | `python` | `_PyFrame_MakeAndSetFrameObject` | unknown |
| 0.36% | `python` | `sre_ucs1_count` | library |
| 0.36% | `python` | `PyType_GenericAlloc` | memory |
| 0.36% | `python` | `PyMem_Realloc` | memory |
| 0.36% | `python` | `list_append` | list |
| 0.35% | `python` | `list_iter` | list |
| 0.34% | `python` | `set_contains_lock_held` | miscobj |
| 0.34% | `python` | `method_get` | dynamic |
| 0.33% | `python` | `func_descr_get` | unknown |
| 0.31% | `python` | `BaseException_vectorcall` | exceptions |
| 0.31% | `python` | `long_and` | int |
| 0.31% | `python` | `visit_reachable` | gc |
| 0.30% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.30% | `python` | `r_object` | import |
| 0.30% | `python` | `PyList_New` | memory |
| 0.30% | `python` | `PyTraceBack_Here` | exceptions |
| 0.29% | `python` | `builtin_min` | unknown |
| 0.26% | `python` | `unicode_dealloc` | memory |
| 0.26% | `python` | `getset_get` | dynamic |
| 0.25% | `python` | `PyUnicode_FromKindAndData` | str |

## regex_dna

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 35.72% | `python` | `sre_ucs1_match` | library |
| 28.89% | `python` | `sre_ucs2_charset.isra.0` | library |
| 6.32% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 5.42% | `python` | `sre_search` | library |
| 3.22% | `libm-2.31.so` | `__fmod_finite@GLIBC_2.15` | library |
| 1.16% | `_bisect.cpython-314-x86_64-linux-gnu.so` | `_bisect_bisect_right` | library |
| 1.02% | `python` | `pattern_subx` | library |
| 1.00% | `libc-2.31.so` | `__memcpy_avx_unaligned_erms` | libc |
| 0.83% | `python` | `float_richcompare` | float |
| 0.64% | `python` | `stringlib_bytes_join.lto_priv.1` | str |
| 0.64% | `python` | `type_new` | memory |
| 0.52% | `python` | `_PyFloat_FromDouble_ConsumeInputs` | float |
| 0.42% | `python` | `deduce_unreachable` | gc |
| 0.41% | `python` | `PyFloat_FromDouble` | float |
| 0.38% | `python` | `float_rem` | float |
| 0.36% | `python` | `PyBytes_FromStringAndSize` | str |
| 0.36% | `python` | `list_item` | list |
| 0.34% | `python` | `intern_common.part.0` | str |
| 0.34% | `python` | `float_div` | float |
| 0.34% | `python` | `visit_decref` | gc |
| 0.33% | `python` | `_PyCode_New` | interpreter |
| 0.31% | `python` | `bytearray_ass_subscript` | miscobj |
| 0.30% | `python` | `gc_collect_region.isra.0` | gc |

## regex_effbot

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 41.74% | `python` | `sre_ucs1_match` | library |
| 17.16% | `python` | `sre_ucs2_charset.isra.0` | library |
| 7.53% | `python` | `PyMem_Free` | memory |
| 5.82% | `python` | `sre_search` | library |
| 5.63% | `python` | `PyMem_Malloc` | memory |
| 3.60% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 2.27% | `python` | `sre_ucs1_count` | library |
| 0.94% | `python` | `type_new` | memory |
| 0.55% | `python` | `intern_common.part.0` | str |
| 0.54% | `python` | `deduce_unreachable` | gc |
| 0.49% | `python` | `_PyCode_New` | interpreter |
| 0.46% | `python` | `visit_decref` | gc |
| 0.46% | `python` | `siphash13` | str |
| 0.43% | `python` | `gc_collect_region.isra.0` | gc |
| 0.34% | `python` | `r_object` | import |
| 0.32% | `python` | `visit_reachable` | gc |
| 0.31% | `python` | `tuple_dealloc` | memory |
| 0.25% | `python` | `_PyEval_FrameClearAndPop` | interpreter |

## regex_v8

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 36.65% | `python` | `sre_ucs1_match` | library |
| 8.88% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 4.54% | `python` | `sre_ucs1_count` | library |
| 3.14% | `python` | `sre_search` | library |
| 3.08% | `python` | `PyCode_Addr2Line` | exceptions |
| 1.40% | `python` | `pattern_subx` | library |
| 1.34% | `libc-2.31.so` | `_int_malloc` | libc |
| 1.30% | `python` | `type_new` | memory |
| 1.25% | `python` | `PyMem_Free` | memory |
| 1.18% | `python` | `state_init` | unknown |
| 1.13% | `python` | `sre_ucs1_match.cold` | library |
| 0.85% | `libc-2.31.so` | `_int_free` | libc |
| 0.80% | `libc-2.31.so` | `__memcpy_avx_unaligned_erms` | libc |
| 0.77% | `python` | `intern_common.part.0` | str |
| 0.73% | `python` | `PyDict_GetItemRef` | dict |
| 0.70% | `python` | `_PyCode_New` | interpreter |
| 0.68% | `python` | `list_dealloc` | memory |
| 0.66% | `python` | `deduce_unreachable` | gc |
| 0.63% | `python` | `gc_collect_region.isra.0` | gc |
| 0.62% | `python` | `PyLong_FromLong` | int |
| 0.60% | `python` | `unicode_dealloc` | memory |
| 0.60% | `python` | `visit_decref` | gc |
| 0.60% | `python` | `bytearray_ass_subscript` | miscobj |
| 0.59% | `python` | `_PyUnicode_JoinArray` | str |
| 0.58% | `python` | `PyUnicode_Substring` | str |
| 0.57% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.56% | `libc-2.31.so` | `__libc_malloc` | libc |
| 0.56% | `python` | `PyMem_Malloc` | memory |
| 0.52% | `python` | `long_dealloc` | memory |
| 0.49% | `python` | `_PyUnicode_IsAlpha` | str |
| 0.47% | `python` | `r_object` | import |
| 0.47% | `python` | `tuple_dealloc` | memory |
| 0.45% | `python` | `visit_reachable` | gc |
| 0.42% | `python` | `Py_UNICODE_ISALNUM.lto_priv.1` | unknown |
| 0.41% | `python` | `_PyObject_Malloc` | memory |
| 0.39% | `python` | `siphash13` | str |
| 0.38% | `python` | `PyUnicode_FromKindAndData` | str |
| 0.36% | `python` | `PyMem_Realloc` | memory |
| 0.35% | `python` | `_PyObject_GC_NewVar` | gc |
| 0.33% | `python` | `PyList_Append` | list |
| 0.31% | `python` | `pattern_new_match.isra.0` | memory |
| 0.30% | `python` | `object_isinstance` | dynamic |
| 0.27% | `python` | `sre_ucs2_charset.isra.0` | library |

## richards

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 61.97% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 5.81% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 5.55% | `python` | `PyObject_GetAttr` | dynamic |
| 4.70% | `python` | `_PyObject_GetMethod` | dynamic |
| 3.88% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 1.20% | `python` | `PyObject_SetAttr` | dynamic |
| 0.83% | `python` | `long_dealloc` | memory |
| 0.83% | `python` | `type_new` | memory |
| 0.60% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.55% | `python` | `long_add` | int |
| 0.51% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.50% | `python` | `intern_common.part.0` | str |
| 0.49% | `python` | `deduce_unreachable` | gc |
| 0.44% | `python` | `visit_decref` | gc |
| 0.44% | `python` | `_PyCode_New` | interpreter |
| 0.44% | `python` | `gc_collect_region.isra.0` | gc |
| 0.31% | `python` | `r_object` | import |
| 0.29% | `python` | `visit_reachable` | gc |

## richards_super

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 56.77% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 5.43% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 4.55% | `python` | `PyObject_GetAttr` | dynamic |
| 3.68% | `python` | `_PyObject_GetMethod` | dynamic |
| 2.95% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 2.12% | `python` | `_PySuper_Lookup` | dynamic |
| 2.01% | `python` | `PyObject_SetAttr` | dynamic |
| 1.28% | `python` | `type_new` | memory |
| 0.77% | `python` | `deduce_unreachable` | gc |
| 0.72% | `python` | `intern_common.part.0` | str |
| 0.71% | `python` | `_PyCode_New` | interpreter |
| 0.67% | `python` | `long_dealloc` | memory |
| 0.59% | `python` | `gc_collect_region.isra.0` | gc |
| 0.58% | `python` | `visit_decref` | gc |
| 0.54% | `python` | `long_add` | int |
| 0.50% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.46% | `python` | `r_object` | import |
| 0.45% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.43% | `python` | `visit_reachable` | gc |
| 0.43% | `python` | `PyUnicode_FromKindAndData` | str |
| 0.28% | `python` | `tuple_dealloc` | memory |
| 0.26% | `python` | `siphash13` | str |

## scimark

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 40.21% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 6.62% | `python` | `PyNumber_AsSsize_t` | dynamic |
| 4.35% | `python` | `long_dealloc` | memory |
| 3.66% | `array.cpython-314-x86_64-linux-gnu.so` | `array_subscr` | library |
| 3.02% | `python` | `_PyFloat_FromDouble_ConsumeInputs` | float |
| 2.98% | `python` | `long_add` | int |
| 2.64% | `python` | `PyObject_GetItem` | dynamic |
| 2.26% | `python` | `vgetargs1_impl` | calls |
| 2.18% | `python` | `PyLong_FromLong` | int |
| 1.94% | `python` | `PyFloat_FromDouble` | float |
| 1.77% | `python` | `convertitem` | unknown |
| 1.58% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.34% | `array.cpython-314-x86_64-linux-gnu.so` | `array_ass_subscr` | library |
| 1.16% | `python` | `PyType_GetModuleByDef` | dynamic |
| 1.09% | `python` | `long_mul` | int |
| 1.02% | `python` | `object_isinstance` | dynamic |
| 1.00% | `python` | `PyIndex_Check` | unknown |
| 0.93% | `python` | `PyObject_Free` | dynamic |
| 0.92% | `array.cpython-314-x86_64-linux-gnu.so` | `d_setitem` | library |
| 0.89% | `python` | `float_dealloc` | memory |
| 0.74% | `python` | `PyArg_Parse` | calls |
| 0.74% | `python` | `PyObject_SetItem` | dynamic |
| 0.62% | `python` | `type_new` | memory |
| 0.60% | `python` | `_PyFloat_ExactDealloc` | memory |
| 0.55% | `python` | `_PyLong_Frexp` | int |
| 0.50% | `python` | `tuple_dealloc` | memory |
| 0.44% | `python` | `PyFloat_AsDouble` | float |
| 0.39% | `python` | `float_richcompare` | float |
| 0.35% | `python` | `_PyTuple_FromStackRefSteal` | tuple |
| 0.34% | `python` | `intern_common.part.0` | str |
| 0.34% | `python` | `long_sub` | int |
| 0.34% | `array.cpython-314-x86_64-linux-gnu.so` | `d_getitem` | library |
| 0.33% | `python` | `_PyCode_New` | interpreter |
| 0.32% | `python` | `deduce_unreachable` | gc |
| 0.32% | `python` | `range_vectorcall` | miscobj |
| 0.27% | `array.cpython-314-x86_64-linux-gnu.so` | `0x00000000000049c4` | library |
| 0.27% | `python` | `visit_decref` | gc |
| 0.26% | `python` | `gc_collect_region.isra.0` | gc |
| 0.26% | `array.cpython-314-x86_64-linux-gnu.so` | `0x00000000000047e4` | library |
| 0.25% | `array.cpython-314-x86_64-linux-gnu.so` | `0x0000000000004644` | library |

## spectral_norm

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 34.96% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 9.99% | `python` | `long_add` | int |
| 5.99% | `python` | `long_dealloc` | memory |
| 4.67% | `python` | `PyObject_Free` | dynamic |
| 4.44% | `python` | `long_div` | int |
| 3.05% | `python` | `long_mul` | int |
| 3.01% | `python` | `float_div` | float |
| 2.50% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 2.12% | `python` | `enum_next` | miscobj |
| 2.08% | `python` | `_PyFloat_FromDouble_ConsumeInputs` | float |
| 1.46% | `python` | `PyNumber_TrueDivide` | dynamic |
| 1.24% | `python` | `type_new` | memory |
| 1.23% | `python` | `listiter_next` | list |
| 1.15% | `python` | `PyLong_AsDouble` | int |
| 1.06% | `python` | `convert_to_double` | unknown |
| 0.86% | `python` | `deduce_unreachable` | gc |
| 0.74% | `python` | `PyNumber_FloorDivide` | dynamic |
| 0.69% | `python` | `intern_common.part.0` | str |
| 0.66% | `python` | `_PyCode_New` | interpreter |
| 0.60% | `python` | `visit_decref` | gc |
| 0.53% | `python` | `gc_collect_region.isra.0` | gc |
| 0.52% | `python` | `PyType_IsSubtype` | dynamic |
| 0.47% | `python` | `r_object` | import |
| 0.46% | `python` | `float_dealloc` | memory |
| 0.44% | `python` | `_Py_NewReference` | memory |
| 0.41% | `python` | `PyUnicode_FromKindAndData` | str |
| 0.37% | `python` | `visit_reachable` | gc |
| 0.34% | `python` | `tuple_dealloc` | memory |
| 0.30% | `python` | `siphash13` | str |
| 0.27% | `libc-2.31.so` | `__memcpy_avx_unaligned_erms` | libc |

## sphinx

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 25.04% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 6.95% | `python` | `sre_ucs1_match` | library |
| 3.36% | `python` | `deduce_unreachable` | gc |
| 3.08% | `python` | `sre_ucs2_charset.isra.0` | library |
| 2.57% | `python` | `gc_collect_region.isra.0` | gc |
| 2.50% | `python` | `PyObject_GetAttr` | dynamic |
| 2.17% | `python` | `visit_decref` | gc |
| 1.77% | `python` | `object_isinstance` | dynamic |
| 1.73% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.66% | `_pickle.cpython-314-x86_64-linux-gnu.so` | `save` | library |
| 1.58% | `python` | `visit_add_to_container` | gc |
| 1.51% | `python` | `visit_reachable` | gc |
| 1.38% | `python` | `PyDict_GetItemRef` | dict |
| 1.18% | `libc-2.31.so` | `__memcpy_avx_unaligned_erms` | libc |
| 1.14% | `python` | `find_name_in_mro` | lookup |
| 0.94% | `python` | `PyUnicode_Format` | str |
| 0.91% | `python` | `siphash13` | str |
| 0.87% | `python` | `dict_traverse` | gc |
| 0.86% | `python` | `_PyObject_GetMethod` | dynamic |
| 0.81% | `python` | `list_dealloc` | memory |
| 0.80% | `python` | `tuple_dealloc` | memory |
| 0.74% | `python` | `gen_dealloc` | memory |
| 0.73% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.67% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.65% | `python` | `PyObject_SetAttr` | dynamic |
| 0.63% | `python` | `_Py_MakeCoro` | unknown |
| 0.58% | `python` | `subtype_traverse` | gc |
| 0.57% | `python` | `unicode_dealloc` | memory |
| 0.55% | `python` | `PyMem_Free` | memory |
| 0.52% | `python` | `type_new` | memory |
| 0.50% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.46% | `python` | `dict_dealloc` | memory |
| 0.45% | `python` | `_PyFunction_Vectorcall` | calls |
| 0.45% | `python` | `PyMem_Malloc` | memory |
| 0.43% | `python` | `getset_get` | dynamic |
| 0.41% | `python` | `list_iter` | list |
| 0.41% | `python` | `list_traverse` | gc |
| 0.41% | `python` | `_PyGC_Collect` | gc |
| 0.41% | `python` | `PyObject_GC_Del` | gc |
| 0.40% | `_pickle.cpython-314-x86_64-linux-gnu.so` | `memo_put.isra.0` | library |
| 0.39% | `python` | `sre_search` | library |
| 0.38% | `python` | `insertdict` | dict |
| 0.35% | `python` | `PyObject_GetOptionalAttr` | dynamic |
| 0.35% | `python` | `intern_common.part.0` | str |
| 0.33% | `libc-2.31.so` | `_int_malloc` | libc |
| 0.32% | `python` | `tuple_iter` | tuple |
| 0.31% | `python` | `tupleiter_dealloc` | memory |
| 0.29% | `python` | `sre_ucs1_count` | library |
| 0.29% | `python` | `_PyObject_GenericGetAttrWithDict` | dynamic |
| 0.28% | `python` | `_PyTuple_FromStackRefSteal` | tuple |
| 0.28% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 0.28% | `python` | `_PyObject_GC_New` | gc |
| 0.26% | `python` | `_PyUnicode_JoinArray` | str |
| 0.26% | `python` | `_PyCode_New` | interpreter |
| 0.26% | `python` | `PyDict_Next` | dict |

## sqlalchemy_declarative

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 27.72% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 2.74% | `python` | `type_new` | memory |
| 2.37% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 2.03% | `python` | `PyObject_GetAttr` | dynamic |
| 1.91% | `python` | `tuple_dealloc` | memory |
| 1.73% | `python` | `PyObject_SetAttr` | dynamic |
| 1.43% | `python` | `PyDict_GetItemRef` | dict |
| 1.37% | `python` | `find_name_in_mro` | lookup |
| 1.30% | `python` | `deduce_unreachable` | gc |
| 1.16% | `python` | `gc_collect_region.isra.0` | gc |
| 1.13% | `python` | `intern_common.part.0` | str |
| 1.10% | `python` | `visit_decref` | gc |
| 0.97% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.94% | `python` | `_PyCode_New` | interpreter |
| 0.83% | `python` | `visit_reachable` | gc |
| 0.82% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.77% | `python` | `list_dealloc` | memory |
| 0.77% | `python` | `subtype_dealloc` | memory |
| 0.71% | `libpthread-2.31.so` | `pthread_mutex_unlock` | library |
| 0.70% | `python` | `dict_dealloc` | memory |
| 0.70% | `libpthread-2.31.so` | `__pthread_mutex_lock` | library |
| 0.66% | `python` | `r_object` | import |
| 0.62% | `libc-2.31.so` | `__memcpy_avx_unaligned_erms` | libc |
| 0.61% | `python` | `PyObject_GC_Del` | gc |
| 0.60% | `python` | `insertdict` | dict |
| 0.54% | `python` | `set_dealloc` | memory |
| 0.52% | `python` | `PyUnicode_FromKindAndData` | str |
| 0.51% | `python` | `PyType_GenericAlloc` | memory |
| 0.50% | `python` | `siphash13` | str |
| 0.49% | `python` | `sre_ucs1_match` | library |
| 0.46% | `python` | `tuple_hash` | tuple |
| 0.46% | `python` | `_PyObject_GetMethod` | dynamic |
| 0.45% | `python` | `_PyObject_MakeTpCall` | dynamic |
| 0.44% | `python` | `list_iter` | list |
| 0.44% | `python` | `_Py_type_getattro` | lookup |
| 0.41% | `python` | `PyObject_Vectorcall` | dynamic |
| 0.41% | `python` | `unicode_dealloc` | memory |
| 0.39% | `python` | `_Py_slot_tp_getattr_hook` | unknown |
| 0.38% | `python` | `PyFunction_NewWithQualName` | memory |
| 0.37% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.37% | `libc-2.31.so` | `_int_malloc` | libc |
| 0.36% | `python` | `_PyTuple_FromStackRefSteal` | tuple |
| 0.36% | `python` | `code_dealloc` | memory |
| 0.35% | `python` | `_PyFunction_Vectorcall` | calls |
| 0.34% | `python` | `slot_tp_init` | unknown |
| 0.34% | `python` | `take_gil` | gil |
| 0.34% | `python` | `PyMem_Free` | memory |
| 0.32% | `python` | `PyDict_Contains` | dict |
| 0.31% | `python` | `tp_new_wrapper` | memory |
| 0.30% | `python` | `_PyObject_GC_New` | gc |
| 0.30% | `python` | `PyDict_SetItem` | dict |
| 0.29% | `python` | `dictresize` | dict |
| 0.29% | `python` | `tok_get_normal_mode` | compiler |
| 0.29% | `python` | `dict_traverse` | gc |
| 0.28% | `libsqlite3.so.0.8.6` | `sqlite3_reset` | library |
| 0.28% | `python` | `PyObject_IsTrue` | dynamic |
| 0.28% | `python` | `func_dealloc` | memory |
| 0.27% | `python` | `type_ready` | dynamic |
| 0.27% | `python` | `_Py_dict_lookup` | lookup |
| 0.25% | `python` | `insert_to_emptydict` | dict |

## sqlalchemy_imperative

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 31.33% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 3.00% | `python` | `type_new` | memory |
| 2.62% | `python` | `PyObject_GetAttr` | dynamic |
| 1.89% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.68% | `python` | `deduce_unreachable` | gc |
| 1.66% | `python` | `tuple_dealloc` | memory |
| 1.44% | `python` | `gc_collect_region.isra.0` | gc |
| 1.22% | `python` | `visit_decref` | gc |
| 1.18% | `python` | `PyDict_GetItemRef` | dict |
| 1.12% | `python` | `PyObject_SetAttr` | dynamic |
| 1.05% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 1.02% | `python` | `intern_common.part.0` | str |
| 0.91% | `python` | `_PyCode_New` | interpreter |
| 0.89% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.89% | `python` | `dict_dealloc` | memory |
| 0.85% | `python` | `visit_reachable` | gc |
| 0.73% | `python` | `find_name_in_mro` | lookup |
| 0.67% | `python` | `r_object` | import |
| 0.65% | `libc-2.31.so` | `__memcpy_avx_unaligned_erms` | libc |
| 0.64% | `python` | `list_dealloc` | memory |
| 0.58% | `python` | `insertdict` | dict |
| 0.58% | `python` | `subtype_dealloc` | memory |
| 0.55% | `python` | `PyType_GenericAlloc` | memory |
| 0.55% | `libsqlite3.so.0.8.6` | `sqlite3_reset` | library |
| 0.55% | `libpthread-2.31.so` | `__pthread_mutex_lock` | library |
| 0.54% | `libpthread-2.31.so` | `pthread_mutex_unlock` | library |
| 0.48% | `python` | `PyUnicode_FromKindAndData` | str |
| 0.46% | `python` | `sre_ucs1_match` | library |
| 0.46% | `python` | `siphash13` | str |
| 0.44% | `python` | `_PyObject_GetMethod` | dynamic |
| 0.44% | `python` | `_PyTuple_FromStackRefSteal` | tuple |
| 0.44% | `python` | `visit_add_to_container` | gc |
| 0.41% | `python` | `PyDict_SetItem` | dict |
| 0.41% | `python` | `PyFunction_NewWithQualName` | memory |
| 0.40% | `python` | `_PyFunction_Vectorcall` | calls |
| 0.40% | `python` | `_Py_type_getattro` | lookup |
| 0.39% | `python` | `PyObject_GC_Del` | gc |
| 0.39% | `python` | `slot_tp_init` | unknown |
| 0.38% | `python` | `unicode_dealloc` | memory |
| 0.37% | `python` | `insert_to_emptydict` | dict |
| 0.37% | `python` | `dictresize` | dict |
| 0.36% | `python` | `PyMem_Free` | memory |
| 0.35% | `python` | `_PyObject_MakeTpCall` | dynamic |
| 0.35% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.35% | `python` | `method_dealloc` | memory |
| 0.34% | `python` | `code_dealloc` | memory |
| 0.33% | `python` | `PyObject_Vectorcall` | dynamic |
| 0.33% | `python` | `PyObject_IsTrue` | dynamic |
| 0.32% | `python` | `type_ready` | dynamic |
| 0.32% | `python` | `dict_traverse` | gc |
| 0.30% | `libsqlite3.so.0.8.6` | `sqlite3_exec` | library |
| 0.29% | `python` | `object_new` | memory |
| 0.28% | `python` | `_Py_dict_lookup` | lookup |
| 0.27% | `python` | `PyList_New` | memory |
| 0.27% | `python` | `dict_merge` | dict |
| 0.26% | `python` | `_PyStack_UnpackDict` | unknown |
| 0.25% | `libc-2.31.so` | `_int_malloc` | libc |
| 0.25% | `python` | `func_dealloc` | memory |

## sqlglot

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 35.74% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 5.26% | `python` | `object_isinstance` | dynamic |
| 2.55% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 2.28% | `python` | `tuple_dealloc` | memory |
| 1.57% | `python` | `type_new` | memory |
| 1.54% | `python` | `method_get` | dynamic |
| 1.38% | `python` | `PyObject_IsInstance` | dynamic |
| 1.31% | `python` | `meth_dealloc` | memory |
| 1.22% | `python` | `dictiter_iternextitem` | dict |
| 1.21% | `python` | `_Py_MakeCoro` | unknown |
| 1.09% | `python` | `PyFunction_NewWithQualName` | memory |
| 1.05% | `python` | `_PyTuple_FromStackRefSteal` | tuple |
| 0.94% | `python` | `gen_dealloc` | memory |
| 0.90% | `python` | `deduce_unreachable` | gc |
| 0.86% | `python` | `dictiter_dealloc` | memory |
| 0.81% | `python` | `getset_get` | dynamic |
| 0.79% | `python` | `_PyType_LookupRef` | lookup |
| 0.77% | `python` | `_PyCode_New` | interpreter |
| 0.76% | `python` | `intern_common.part.0` | str |
| 0.75% | `python` | `dict_items` | dict |
| 0.74% | `python` | `gc_collect_region.isra.0` | gc |
| 0.74% | `python` | `visit_decref` | gc |
| 0.72% | `python` | `list_dealloc` | memory |
| 0.71% | `python` | `dictview_dealloc` | memory |
| 0.68% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.68% | `python` | `siphash13` | str |
| 0.68% | `python` | `insert_to_emptydict` | dict |
| 0.67% | `python` | `PyObject_GetAttr` | dynamic |
| 0.65% | `python` | `slot_tp_hash` | unknown |
| 0.65% | `python` | `PyObject_GC_Del` | gc |
| 0.61% | `python` | `dictitems_iter` | unknown |
| 0.59% | `python` | `visit_reachable` | gc |
| 0.55% | `python` | `dict_get` | dict |
| 0.54% | `python` | `func_dealloc` | memory |
| 0.52% | `python` | `r_object` | import |
| 0.51% | `python` | `PyTuple_Pack` | tuple |
| 0.51% | `python` | `unicode_dealloc` | memory |
| 0.50% | `python` | `dict_dealloc` | memory |
| 0.47% | `python` | `list_iter` | list |
| 0.47% | `python` | `find_name_in_mro` | lookup |
| 0.46% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.43% | `libc-2.31.so` | `__memcpy_avx_unaligned_erms` | libc |
| 0.43% | `python` | `PyObject_CallOneArg` | dynamic |
| 0.40% | `python` | `_PyFrame_ClearExceptCode` | interpreter |
| 0.39% | `python` | `PyObject_GetIter` | dynamic |
| 0.38% | `python` | `_PyObject_GetMethod` | dynamic |
| 0.38% | `python` | `tuple_hash` | tuple |
| 0.38% | `python` | `_PyLong_New` | memory |
| 0.37% | `python` | `_PyObject_Calloc` | memory |
| 0.37% | `python` | `cfunction_vectorcall_O` | calls |
| 0.36% | `python` | `PyUnicode_FromKindAndData` | str |
| 0.35% | `python` | `PyObject_IsTrue` | dynamic |
| 0.35% | `python` | `_PyFunction_Vectorcall` | calls |
| 0.35% | `python` | `member_get` | unknown |
| 0.35% | `python` | `slot_tp_richcompare` | dynamic |
| 0.33% | `python` | `_PyObject_GC_NewVar` | gc |
| 0.33% | `python` | `long_dealloc` | memory |
| 0.33% | `python` | `insertdict` | dict |
| 0.30% | `python` | `_PyUnicode_JoinArray` | str |
| 0.29% | `python` | `_PyObject_GC_New` | gc |
| 0.28% | `python` | `PyUnicode_New` | memory |
| 0.28% | `python` | `PyList_New` | memory |
| 0.27% | `python` | `_PyObject_Malloc` | memory |

## sqlglot_optimize

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 35.50% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 5.74% | `python` | `object_isinstance` | dynamic |
| 2.42% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 2.26% | `python` | `tuple_dealloc` | memory |
| 1.70% | `python` | `method_get` | dynamic |
| 1.53% | `python` | `dictiter_iternextitem` | dict |
| 1.51% | `python` | `PyObject_IsInstance` | dynamic |
| 1.50% | `python` | `meth_dealloc` | memory |
| 1.47% | `python` | `type_new` | memory |
| 1.35% | `python` | `PyObject_GetAttr` | dynamic |
| 1.06% | `python` | `_PyTuple_FromStackRefSteal` | tuple |
| 0.98% | `python` | `getset_get` | dynamic |
| 0.98% | `python` | `list_dealloc` | memory |
| 0.87% | `python` | `_PyType_LookupRef` | lookup |
| 0.87% | `python` | `PyFunction_NewWithQualName` | memory |
| 0.82% | `python` | `deduce_unreachable` | gc |
| 0.81% | `python` | `gc_collect_region.isra.0` | gc |
| 0.77% | `python` | `visit_decref` | gc |
| 0.74% | `python` | `intern_common.part.0` | str |
| 0.74% | `python` | `_PyCode_New` | interpreter |
| 0.72% | `python` | `dict_get` | dict |
| 0.67% | `python` | `slot_tp_hash` | unknown |
| 0.67% | `python` | `dictiter_dealloc` | memory |
| 0.65% | `python` | `siphash13` | str |
| 0.65% | `python` | `member_get` | unknown |
| 0.59% | `python` | `PyObject_GC_Del` | gc |
| 0.59% | `python` | `dict_items` | dict |
| 0.57% | `python` | `insert_to_emptydict` | dict |
| 0.57% | `python` | `list_iter` | list |
| 0.56% | `python` | `_Py_MakeCoro` | unknown |
| 0.55% | `python` | `dict_dealloc` | memory |
| 0.55% | `python` | `unicode_dealloc` | memory |
| 0.55% | `python` | `tuple_hash` | tuple |
| 0.55% | `python` | `dictitems_iter` | unknown |
| 0.54% | `python` | `find_name_in_mro` | lookup |
| 0.53% | `python` | `visit_reachable` | gc |
| 0.53% | `python` | `dictview_dealloc` | memory |
| 0.51% | `python` | `_PyObject_Calloc` | memory |
| 0.50% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.48% | `python` | `r_object` | import |
| 0.47% | `python` | `gen_dealloc` | memory |
| 0.46% | `python` | `func_dealloc` | memory |
| 0.46% | `python` | `insertdict` | dict |
| 0.45% | `python` | `PyObject_CallOneArg` | dynamic |
| 0.43% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.42% | `python` | `_PyFunction_Vectorcall` | calls |
| 0.42% | `libc-2.31.so` | `__memcpy_avx_unaligned_erms` | libc |
| 0.42% | `python` | `_PyLong_New` | memory |
| 0.39% | `python` | `_PyUnicode_JoinArray` | str |
| 0.38% | `python` | `PyTuple_Pack` | tuple |
| 0.38% | `python` | `cfunction_vectorcall_O` | calls |
| 0.38% | `python` | `long_dealloc` | memory |
| 0.37% | `python` | `PyUnicode_FromKindAndData` | str |
| 0.34% | `python` | `PyObject_IsTrue` | dynamic |
| 0.34% | `python` | `PyList_New` | memory |
| 0.31% | `python` | `_PyObject_Malloc` | memory |
| 0.30% | `python` | `_PyObject_GC_New` | gc |
| 0.27% | `python` | `PyObject_SetAttr` | dynamic |
| 0.27% | `python` | `PyObject_GetIter` | dynamic |
| 0.26% | `python` | `PyDict_GetItemRef` | dict |

## sqlglot_parse

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 50.10% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 3.53% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.48% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 1.42% | `python` | `PyObject_GetAttr` | dynamic |
| 1.40% | `python` | `_Py_type_getattro` | lookup |
| 1.36% | `python` | `PyDict_Contains` | dict |
| 1.29% | `python` | `deduce_unreachable` | gc |
| 1.20% | `python` | `gc_collect_region.isra.0` | gc |
| 1.12% | `python` | `type_new` | memory |
| 0.88% | `python` | `visit_decref` | gc |
| 0.85% | `python` | `long_dealloc` | memory |
| 0.81% | `python` | `dict_get` | dict |
| 0.81% | `python` | `long_add` | int |
| 0.74% | `python` | `_PyFunction_Vectorcall` | calls |
| 0.74% | `python` | `slot_tp_hash` | unknown |
| 0.71% | `python` | `find_name_in_mro` | lookup |
| 0.68% | `python` | `tuple_dealloc` | memory |
| 0.68% | `python` | `PyObject_RichCompare` | dynamic |
| 0.67% | `python` | `PyObject_SetAttr` | dynamic |
| 0.63% | `python` | `dict_dealloc` | memory |
| 0.60% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.59% | `python` | `object_isinstance` | dynamic |
| 0.58% | `python` | `intern_common.part.0` | str |
| 0.57% | `python` | `object_new` | memory |
| 0.55% | `python` | `visit_reachable` | gc |
| 0.55% | `python` | `_PyCode_New` | interpreter |
| 0.48% | `python` | `insert_to_emptydict` | dict |
| 0.48% | `python` | `PyDict_SetItem` | dict |
| 0.47% | `python` | `unicode_dealloc` | memory |
| 0.46% | `python` | `slot_tp_init` | unknown |
| 0.44% | `python` | `long_sub` | int |
| 0.43% | `python` | `unicode_subscript` | str |
| 0.42% | `python` | `PyObject_GC_Del` | gc |
| 0.41% | `python` | `subtype_traverse` | gc |
| 0.39% | `python` | `r_object` | import |
| 0.38% | `python` | `_PyLong_New` | memory |
| 0.38% | `python` | `siphash13` | str |
| 0.36% | `libc-2.31.so` | `__memcpy_avx_unaligned_erms` | libc |
| 0.35% | `python` | `dictiter_iternextitem` | dict |
| 0.35% | `python` | `clear_slots` | unknown |
| 0.34% | `python` | `_PyObject_GC_New` | gc |
| 0.34% | `python` | `PyDict_GetItemRef` | dict |
| 0.33% | `python` | `subtype_dealloc` | memory |
| 0.31% | `python` | `dict_traverse` | gc |
| 0.30% | `python` | `method_get` | dynamic |
| 0.29% | `python` | `meth_dealloc` | memory |
| 0.28% | `python` | `object_richcompare` | dynamic |
| 0.27% | `python` | `PyUnicode_New` | memory |
| 0.27% | `python` | `PyUnicode_FromKindAndData` | str |
| 0.26% | `python` | `PyObject_Free` | dynamic |
| 0.25% | `python` | `dict_merge` | dict |

## sqlglot_transpile

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 44.59% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 3.21% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.61% | `python` | `type_new` | memory |
| 1.53% | `python` | `PyObject_GetAttr` | dynamic |
| 1.46% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 1.36% | `python` | `deduce_unreachable` | gc |
| 1.26% | `python` | `gc_collect_region.isra.0` | gc |
| 1.06% | `python` | `_Py_type_getattro` | lookup |
| 1.05% | `python` | `visit_decref` | gc |
| 1.04% | `python` | `find_name_in_mro` | lookup |
| 1.03% | `python` | `object_isinstance` | dynamic |
| 0.97% | `python` | `dict_get` | dict |
| 0.96% | `python` | `PyDict_Contains` | dict |
| 0.79% | `python` | `intern_common.part.0` | str |
| 0.78% | `python` | `tuple_dealloc` | memory |
| 0.75% | `python` | `_PyCode_New` | interpreter |
| 0.64% | `python` | `dict_dealloc` | memory |
| 0.64% | `python` | `unicode_dealloc` | memory |
| 0.63% | `python` | `_PyFunction_Vectorcall` | calls |
| 0.62% | `python` | `long_dealloc` | memory |
| 0.62% | `libc-2.31.so` | `__memcpy_avx_unaligned_erms` | libc |
| 0.62% | `python` | `long_add` | int |
| 0.61% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.60% | `python` | `visit_reachable` | gc |
| 0.55% | `python` | `PyObject_SetAttr` | dynamic |
| 0.53% | `python` | `r_object` | import |
| 0.53% | `python` | `slot_tp_hash` | unknown |
| 0.49% | `python` | `siphash13` | str |
| 0.47% | `python` | `PyObject_RichCompare` | dynamic |
| 0.45% | `python` | `_PyUnicode_JoinArray` | str |
| 0.44% | `python` | `object_new` | memory |
| 0.44% | `python` | `insert_to_emptydict` | dict |
| 0.43% | `python` | `PyDict_SetItem` | dict |
| 0.41% | `python` | `PyUnicode_FromKindAndData` | str |
| 0.41% | `python` | `meth_dealloc` | memory |
| 0.39% | `python` | `list_dealloc` | memory |
| 0.39% | `python` | `insertdict` | dict |
| 0.39% | `python` | `PyDict_GetItemRef` | dict |
| 0.38% | `python` | `_PyObject_GC_New` | gc |
| 0.37% | `python` | `slot_tp_init` | unknown |
| 0.36% | `python` | `dictiter_iternextitem` | dict |
| 0.35% | `python` | `subtype_traverse` | gc |
| 0.35% | `python` | `method_get` | dynamic |
| 0.35% | `python` | `long_sub` | int |
| 0.33% | `python` | `dict_traverse` | gc |
| 0.32% | `python` | `unicode_subscript` | str |
| 0.32% | `python` | `PyObject_GC_Del` | gc |
| 0.30% | `python` | `_PyLong_New` | memory |
| 0.30% | `python` | `PyObject_IsInstance` | dynamic |
| 0.28% | `python` | `func_descr_get` | unknown |
| 0.27% | `python` | `method_dealloc` | memory |
| 0.27% | `python` | `subtype_dealloc` | memory |
| 0.27% | `python` | `_PyType_LookupRef` | lookup |
| 0.27% | `python` | `member_get` | unknown |
| 0.25% | `python` | `clear_slots` | unknown |

## sqlite_synth

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 12.05% | `libpthread-2.31.so` | `pthread_mutex_unlock` | library |
| 11.98% | `libpthread-2.31.so` | `__pthread_mutex_lock` | library |
| 9.08% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 5.86% | `python` | `take_gil` | gil |
| 4.69% | `libsqlite3.so.0.8.6` | `sqlite3_reset` | library |
| 2.20% | `libm-2.31.so` | `__cos_fma` | library |
| 1.47% | `libsqlite3.so.0.8.6` | `sqlite3_randomness` | library |
| 1.29% | `python` | `PyEval_SaveThread` | interpreter |
| 1.27% | `python` | `long_dealloc` | memory |
| 1.08% | `python` | `tuple_dealloc` | memory |
| 0.99% | `libpthread-2.31.so` | `pthread_cond_signal@@GLIBC_2.3.2` | library |
| 0.97% | `_sqlite3.cpython-314-x86_64-linux-gnu.so` | `_pysqlite_query_execute` | library |
| 0.89% | `libsqlite3.so.0.8.6` | `sqlite3_value_double` | library |
| 0.80% | `python` | `type_new` | memory |
| 0.77% | `libsqlite3.so.0.8.6` | `sqlite3_preupdate_old` | library |
| 0.75% | `libsqlite3.so.0.8.6` | `sqlite3_value_int64` | library |
| 0.74% | `libsqlite3.so.0.8.6` | `sqlite3_wal_checkpoint` | library |
| 0.72% | `libsqlite3.so.0.8.6` | `sqlite3_extended_errcode` | library |
| 0.72% | `python` | `long_to_decimal_string_internal` | int |
| 0.69% | `python` | `list_dealloc` | memory |
| 0.64% | `libsqlite3.so.0.8.6` | `sqlite3_vtab_config` | library |
| 0.63% | `python` | `unicode_dealloc` | memory |
| 0.62% | `libc-2.31.so` | `_int_free` | libc |
| 0.60% | `python` | `PyType_GenericAlloc` | memory |
| 0.60% | `python` | `PyFloat_AsDouble` | float |
| 0.60% | `python` | `_PyObject_MakeTpCall` | dynamic |
| 0.60% | `libsqlite3.so.0.8.6` | `sqlite3_enable_shared_cache` | library |
| 0.59% | `python` | `object_new` | memory |
| 0.59% | `libsqlite3.so.0.8.6` | `sqlite3_step` | library |
| 0.58% | `python` | `_PyObject_Malloc` | memory |
| 0.58% | `libc-2.31.so` | `pthread_mutex_lock` | libc |
| 0.53% | `_sqlite3.cpython-314-x86_64-linux-gnu.so` | `pysqlite_cursor_init` | library |
| 0.51% | `python` | `PyFloat_FromDouble` | float |
| 0.51% | `python` | `bounded_lru_cache_wrapper` | unknown |
| 0.50% | `python` | `intern_common.part.0` | str |
| 0.48% | `python` | `method_vectorcall` | calls |
| 0.47% | `libc-2.31.so` | `pthread_mutex_unlock` | libc |
| 0.47% | `python` | `PyEval_RestoreThread` | interpreter |
| 0.47% | `python` | `deduce_unreachable` | gc |
| 0.45% | `python` | `_PyCode_New` | interpreter |
| 0.42% | `python` | `PyObject_GetAttr` | dynamic |
| 0.42% | `libsqlite3.so.0.8.6` | `sqlite3_str_value` | library |
| 0.40% | `libc-2.31.so` | `__libc_malloc` | libc |
| 0.40% | `_sqlite3.cpython-314-x86_64-linux-gnu.so` | `pysqlite_cursor_iternext` | library |
| 0.40% | `python` | `gc_collect_region.isra.0` | gc |
| 0.39% | `python` | `unicode_decode_utf8` | str |
| 0.39% | `python` | `visit_decref` | gc |
| 0.38% | `python` | `_Py_dict_lookup` | lookup |
| 0.37% | `python` | `long_add` | int |
| 0.37% | `_sqlite3.cpython-314-x86_64-linux-gnu.so` | `pysqlite_connection_execute` | library |
| 0.37% | `libsqlite3.so.0.8.6` | `sqlite3_value_pointer` | library |
| 0.36% | `libsqlite3.so.0.8.6` | `sqlite3_mutex_try` | library |
| 0.36% | `_sqlite3.cpython-314-x86_64-linux-gnu.so` | `bind_param.isra.0` | library |
| 0.35% | `python` | `PyTuple_New` | memory |
| 0.35% | `libc-2.31.so` | `__memcpy_avx_unaligned_erms` | libc |
| 0.34% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.34% | `python` | `method_dealloc` | memory |
| 0.32% | `python` | `PyList_New` | memory |
| 0.32% | `python` | `pthread_mutex_lock@plt` | unknown |
| 0.32% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.32% | `libsqlite3.so.0.8.6` | `sqlite3_close_v2` | library |
| 0.30% | `python` | `PyObject_ClearWeakRefs` | dynamic |
| 0.30% | `libsqlite3.so.0.8.6` | `sqlite3_free` | library |
| 0.30% | `python` | `r_object` | import |
| 0.29% | `python` | `PyUnicode_New` | memory |
| 0.28% | `math.cpython-314-x86_64-linux-gnu.so` | `math_cos` | library |
| 0.28% | `python` | `weakref_dealloc` | memory |
| 0.28% | `python` | `_PyObject_Call` | dynamic |
| 0.28% | `python` | `visit_reachable` | gc |
| 0.27% | `python` | `PyLong_FromLongLong` | int |
| 0.27% | `libsqlite3.so.0.8.6` | `sqlite3_realloc64` | library |
| 0.26% | `python` | `pthread_mutex_unlock@plt` | unknown |
| 0.26% | `python` | `list_iter` | list |
| 0.26% | `python` | `PyObject_CallOneArg` | dynamic |
| 0.25% | `python` | `float_dealloc` | memory |
| 0.25% | `libc-2.31.so` | `cfree@GLIBC_2.2.5` | libc |

## sympy

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 29.59% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 2.37% | `python` | `tuple_dealloc` | memory |
| 2.31% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.48% | `python` | `PyObject_GetAttr` | dynamic |
| 1.32% | `python` | `deduce_unreachable` | gc |
| 1.25% | `python` | `type_new` | memory |
| 1.24% | `python` | `visit_decref` | gc |
| 1.23% | `python` | `PyDict_GetItemRef` | dict |
| 1.21% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 1.15% | `python` | `gc_collect_region.isra.0` | gc |
| 1.02% | `python` | `PyDict_SetItem` | dict |
| 1.02% | `python` | `intern_common.part.0` | str |
| 0.99% | `python` | `find_name_in_mro` | lookup |
| 0.94% | `python` | `_Py_type_getattro` | lookup |
| 0.91% | `python` | `object_isinstance` | dynamic |
| 0.87% | `python` | `_PyCode_New` | interpreter |
| 0.85% | `python` | `visit_reachable` | gc |
| 0.80% | `python` | `PyObject_RichCompareBool` | dynamic |
| 0.80% | `python` | `_Py_dict_lookup` | lookup |
| 0.79% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.78% | `python` | `slot_tp_richcompare` | dynamic |
| 0.73% | `python` | `method_get` | dynamic |
| 0.72% | `python` | `dict_dealloc` | memory |
| 0.71% | `python` | `_PyFunction_Vectorcall` | calls |
| 0.70% | `python` | `meth_dealloc` | memory |
| 0.64% | `python` | `list_dealloc` | memory |
| 0.64% | `python` | `_PyObject_GenericGetAttrWithDict` | dynamic |
| 0.61% | `python` | `PyFunction_NewWithQualName` | memory |
| 0.59% | `libc-2.31.so` | `__memcpy_avx_unaligned_erms` | libc |
| 0.58% | `python` | `r_object` | import |
| 0.56% | `python` | `_PyObject_MakeTpCall` | dynamic |
| 0.52% | `python` | `dict_merge` | dict |
| 0.50% | `python` | `PyUnicode_RichCompare` | str |
| 0.49% | `python` | `dictresize` | dict |
| 0.48% | `python` | `_PyTuple_FromStackRefSteal` | tuple |
| 0.48% | `python` | `PyObject_GetOptionalAttr` | dynamic |
| 0.44% | `python` | `tuple_iter` | tuple |
| 0.43% | `python` | `slot_tp_hash` | unknown |
| 0.43% | `python` | `PyMem_Free` | memory |
| 0.42% | `python` | `PyUnicode_FromKindAndData` | str |
| 0.42% | `python` | `siphash13` | str |
| 0.42% | `python` | `func_dealloc` | memory |
| 0.41% | `python` | `wrapperdescr_call` | unknown |
| 0.39% | `python` | `insert_to_emptydict` | dict |
| 0.38% | `python` | `setiter_iternext` | miscobj |
| 0.37% | `python` | `member_get` | unknown |
| 0.37% | `python` | `_Py_slot_tp_getattr_hook` | unknown |
| 0.37% | `python` | `dictiter_iternextitem` | dict |
| 0.35% | `python` | `dict_subscript` | dict |
| 0.33% | `python` | `insertdict` | dict |
| 0.33% | `python` | `_PyStack_UnpackDict` | unknown |
| 0.32% | `libc-2.31.so` | `__memcmp_avx2_movbe` | libc |
| 0.32% | `python` | `dict_get` | dict |
| 0.32% | `python` | `code_dealloc` | memory |
| 0.32% | `python` | `dict_traverse` | gc |
| 0.31% | `python` | `tuple_hash` | tuple |
| 0.31% | `python` | `PyObject_IsInstance` | dynamic |
| 0.30% | `python` | `tupleiter_dealloc` | memory |
| 0.30% | `python` | `unicode_dealloc` | memory |
| 0.28% | `python` | `_PyType_LookupRef` | lookup |
| 0.27% | `python` | `visit_add_to_container` | gc |
| 0.26% | `python` | `PyObject_GC_Del` | gc |
| 0.26% | `python` | `PyDict_Contains` | dict |
| 0.26% | `python` | `list_iter` | list |
| 0.25% | `python` | `PyObject_CallOneArg` | dynamic |

## telco

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 16.40% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 3.79% | `python` | `_PyObject_GC_New` | gc |
| 3.76% | `python` | `PyObject_GC_Del` | gc |
| 2.32% | `_decimal.cpython-314-x86_64-linux-gnu.so` | `_mpd_qaddsub` | library |
| 2.18% | `_decimal.cpython-314-x86_64-linux-gnu.so` | `nm_mpd_qmul` | library |
| 2.07% | `python` | `tuple_dealloc` | memory |
| 1.92% | `_decimal.cpython-314-x86_64-linux-gnu.so` | `nm_mpd_qadd` | library |
| 1.85% | `python` | `PyObject_GetAttr` | dynamic |
| 1.84% | `_decimal.cpython-314-x86_64-linux-gnu.so` | `_mpd_baseshiftr` | library |
| 1.69% | `python` | `vgetargskeywords.constprop.0` | calls |
| 1.63% | `python` | `meth_dealloc` | memory |
| 1.56% | `python` | `method_get` | dynamic |
| 1.55% | `_decimal.cpython-314-x86_64-linux-gnu.so` | `_mpd_qmul` | library |
| 1.46% | `_decimal.cpython-314-x86_64-linux-gnu.so` | `mpd_qfinalize` | library |
| 1.42% | `python` | `PyContextVar_Get` | unknown |
| 1.42% | `_decimal.cpython-314-x86_64-linux-gnu.so` | `mpd_qshiftr` | library |
| 1.38% | `_decimal.cpython-314-x86_64-linux-gnu.so` | `convert_op` | library |
| 1.36% | `_decimal.cpython-314-x86_64-linux-gnu.so` | `find_state_left_or_right` | library |
| 1.29% | `python` | `PyObject_GC_Track` | gc |
| 1.17% | `_decimal.cpython-314-x86_64-linux-gnu.so` | `dec_mpd_qquantize` | library |
| 1.04% | `python` | `type_new` | memory |
| 1.03% | `python` | `_PyArg_UnpackKeywordsWithVararg` | calls |
| 1.03% | `python` | `PyDict_GetItemRef` | dict |
| 0.91% | `python` | `PyUnicode_New` | memory |
| 0.90% | `python` | `PyObject_GenericGetAttr` | dynamic |
| 0.89% | `python` | `PyObject_GC_UnTrack` | gc |
| 0.83% | `_decimal.cpython-314-x86_64-linux-gnu.so` | `mpd_qquantize` | library |
| 0.82% | `_decimal.cpython-314-x86_64-linux-gnu.so` | `dec_dealloc` | library |
| 0.79% | `python` | `_io_BytesIO_read` | unknown |
| 0.77% | `python` | `vgetargs1_impl` | calls |
| 0.67% | `python` | `method_vectorcall_VARARGS_KEYWORDS` | calls |
| 0.67% | `python` | `deduce_unreachable` | gc |
| 0.66% | `python` | `_PyObject_MakeTpCall` | dynamic |
| 0.65% | `_decimal.cpython-314-x86_64-linux-gnu.so` | `dec_addstatus` | library |
| 0.65% | `python` | `as_ucs4` | unknown |
| 0.62% | `python` | `intern_common.part.0` | str |
| 0.62% | `python` | `_PyCode_New` | interpreter |
| 0.61% | `python` | `find_keyword` | unknown |
| 0.60% | `_decimal.cpython-314-x86_64-linux-gnu.so` | `PyDecType_New.isra.0` | library |
| 0.60% | `_decimal.cpython-314-x86_64-linux-gnu.so` | `PyDecType_FromLongExact` | library |
| 0.60% | `python` | `unicode_dealloc` | memory |
| 0.57% | `python` | `PyObject_RichCompare` | dynamic |
| 0.56% | `python` | `PyType_GetBaseByToken` | unknown |
| 0.54% | `python` | `PyTuple_New` | memory |
| 0.54% | `_decimal.cpython-314-x86_64-linux-gnu.so` | `current_context` | library |
| 0.53% | `_decimal.cpython-314-x86_64-linux-gnu.so` | `dec_str` | library |
| 0.52% | `python` | `visit_decref` | gc |
| 0.50% | `python` | `PyMem_Free` | memory |
| 0.49% | `_decimal.cpython-314-x86_64-linux-gnu.so` | `word_to_string` | library |
| 0.48% | `python` | `long_dealloc` | memory |
| 0.47% | `python` | `PyNumber_Multiply` | dynamic |
| 0.47% | `python` | `write_str` | unknown |
| 0.46% | `_struct.cpython-314-x86_64-linux-gnu.so` | `unpack` | library |
| 0.46% | `libc-2.31.so` | `__strlen_avx2` | libc |
| 0.46% | `python` | `gc_collect_region.isra.0` | gc |
| 0.45% | `python` | `r_object` | import |
| 0.45% | `python` | `PyType_GetModuleByDef` | dynamic |
| 0.44% | `python` | `PyFile_WriteObject` | unknown |
| 0.44% | `libc-2.31.so` | `__strchr_avx2` | libc |
| 0.43% | `python` | `object_dealloc` | memory |
| 0.42% | `python` | `visit_reachable` | gc |
| 0.40% | `python` | `PyObject_Vectorcall` | dynamic |
| 0.40% | `python` | `PyObject_Str` | dynamic |
| 0.40% | `python` | `PyMem_Malloc` | memory |
| 0.39% | `libc-2.31.so` | `__memcpy_avx_unaligned_erms` | libc |
| 0.39% | `python` | `PyLong_FromLong` | int |
| 0.37% | `python` | `binary_op1` | unknown |
| 0.37% | `python` | `PyNumber_InPlaceAdd` | dynamic |
| 0.36% | `python` | `builtin_print` | unknown |
| 0.35% | `_decimal.cpython-314-x86_64-linux-gnu.so` | `ctx_mpd_qquantize` | library |
| 0.35% | `_decimal.cpython-314-x86_64-linux-gnu.so` | `mpd_qadd` | library |
| 0.33% | `python` | `PyObject_CallOneArg` | dynamic |
| 0.32% | `python` | `PyUnicode_FromKindAndData` | str |
| 0.31% | `libc-2.31.so` | `__memcmp_avx2_movbe` | libc |
| 0.29% | `python` | `PyUnicode_CompareWithASCIIString` | str |
| 0.29% | `python` | `cfunction_vectorcall_O` | calls |
| 0.28% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 0.28% | `python` | `PyLong_FromUnsignedLongLong` | int |
| 0.27% | `python` | `siphash13` | str |
| 0.26% | `python` | `PyObject_GetBuffer` | dynamic |
| 0.25% | `_decimal.cpython-314-x86_64-linux-gnu.so` | `_mpd_to_string` | library |

## thrift

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 24.35% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 2.42% | `python` | `PyDict_GetItemRef` | dict |
| 2.41% | `fastbinary.cpython-314-x86_64-linux-gnu.so` | `apache::thrift::py::ProtocolBase<apache::thrift::py::BinaryProtocol>::encodeValue` | library |
| 2.32% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 2.18% | `python` | `subtype_dealloc` | memory |
| 1.88% | `python` | `PyDict_SetItem` | dict |
| 1.76% | `python` | `insert_to_emptydict` | dict |
| 1.70% | `python` | `PyObject_GetAttr` | dynamic |
| 1.67% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 1.52% | `python` | `dict_dealloc` | memory |
| 1.50% | `python` | `_PyFunction_Vectorcall` | calls |
| 1.35% | `python` | `tuple_dealloc` | memory |
| 1.34% | `python` | `type_new` | memory |
| 1.24% | `python` | `_PyStack_UnpackDict` | unknown |
| 1.20% | `python` | `object_new` | memory |
| 1.13% | `python` | `PyObject_GC_Del` | gc |
| 1.09% | `python` | `PyType_GenericAlloc` | memory |
| 1.07% | `python` | `slot_tp_init` | unknown |
| 1.00% | `python` | `PyObject_RichCompareBool` | dynamic |
| 0.95% | `python` | `insertdict` | dict |
| 0.88% | `python` | `_PySuper_Lookup` | dynamic |
| 0.88% | `python` | `PyMem_Free` | memory |
| 0.87% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.82% | `fastbinary.cpython-314-x86_64-linux-gnu.so` | `apache::thrift::py::ProtocolBase<apache::thrift::py::BinaryProtocol>::decodeValue` | library |
| 0.78% | `python` | `_PyObject_MakeTpCall` | dynamic |
| 0.76% | `python` | `_PyCode_New` | interpreter |
| 0.76% | `python` | `deduce_unreachable` | gc |
| 0.75% | `python` | `intern_common.part.0` | str |
| 0.74% | `python` | `unicode_from_format` | str |
| 0.72% | `python` | `_PyObject_GenericGetAttrWithDict` | dynamic |
| 0.72% | `python` | `unicode_dealloc` | memory |
| 0.67% | `python` | `list_dealloc` | memory |
| 0.67% | `fastbinary.cpython-314-x86_64-linux-gnu.so` | `apache::thrift::py::ProtocolBase<apache::thrift::py::BinaryProtocol>::readStruct` | library |
| 0.67% | `fastbinary.cpython-314-x86_64-linux-gnu.so` | `apache::thrift::py::ProtocolBase<apache::thrift::py::BinaryProtocol>::readBytes` | library |
| 0.66% | `python` | `PyErr_Format` | exceptions |
| 0.66% | `python` | `PyUnicode_DecodeUTF8` | str |
| 0.66% | `python` | `gc_collect_region.isra.0` | gc |
| 0.65% | `python` | `PyLong_AsLong` | int |
| 0.64% | `python` | `dictresize` | dict |
| 0.64% | `python` | `visit_decref` | gc |
| 0.62% | `python` | `PyObject_GetOptionalAttr` | dynamic |
| 0.61% | `python` | `PyTuple_Size` | tuple |
| 0.61% | `libc-2.31.so` | `__memcpy_avx_unaligned_erms` | libc |
| 0.55% | `python` | `siphash13` | str |
| 0.54% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.53% | `python` | `PyUnicode_RichCompare` | str |
| 0.50% | `python` | `unicode_encode_utf8` | str |
| 0.50% | `python` | `dict_merge` | dict |
| 0.45% | `python` | `visit_reachable` | gc |
| 0.44% | `python` | `r_object` | import |
| 0.42% | `python` | `_Py_dict_lookup` | lookup |
| 0.41% | `python` | `object_dealloc` | memory |
| 0.40% | `python` | `method_dealloc` | memory |
| 0.39% | `fastbinary.cpython-314-x86_64-linux-gnu.so` | `apache::thrift::py::BinaryProtocol::readFieldBegin` | library |
| 0.39% | `python` | `BaseException_vectorcall` | exceptions |
| 0.39% | `python` | `vgetargs1_impl` | calls |
| 0.39% | `python` | `tuple_iter` | tuple |
| 0.38% | `python` | `_Py_module_getattro` | unknown |
| 0.36% | `python` | `tupleiter_dealloc` | memory |
| 0.33% | `python` | `PyUnicode_FromKindAndData` | str |
| 0.31% | `python` | `PyObject_Call` | dynamic |
| 0.30% | `python` | `PyDict_New` | memory |
| 0.30% | `python` | `PyBytes_FromStringAndSize` | str |
| 0.30% | `fastbinary.cpython-314-x86_64-linux-gnu.so` | `apache::thrift::py::parse_struct_item_spec` | library |
| 0.29% | `libc-2.31.so` | `__libc_malloc` | libc |
| 0.29% | `python` | `PyObject_SetAttr` | dynamic |
| 0.28% | `python` | `PyList_New` | memory |
| 0.27% | `python` | `func_descr_get` | unknown |
| 0.27% | `python` | `unicode_fromformat_write_utf8` | str |
| 0.26% | `python` | `PyImport_ImportModuleLevelObject` | import |
| 0.26% | `libc-2.31.so` | `__strchr_avx2` | libc |

## tomli_loads

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 53.73% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 5.56% | `python` | `set_contains_lock_held` | miscobj |
| 4.50% | `python` | `long_dealloc` | memory |
| 4.10% | `python` | `long_add` | int |
| 2.43% | `python` | `PyDict_GetItemRef` | dict |
| 2.17% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 2.09% | `python` | `PyDict_Contains` | dict |
| 1.14% | `libc-2.31.so` | `__memcmp_avx2_movbe` | libc |
| 0.97% | `python` | `tuple_dealloc` | memory |
| 0.85% | `python` | `object_isinstance` | dynamic |
| 0.82% | `libc-2.31.so` | `__memcpy_avx_unaligned_erms` | libc |
| 0.82% | `python` | `PyObject_GetAttr` | dynamic |
| 0.72% | `python` | `_PyTuple_FromStackRefSteal` | tuple |
| 0.70% | `python` | `_PyIncrementalNewlineDecoder_decode.cold` | memory |
| 0.68% | `python` | `PyUnicode_New` | memory |
| 0.63% | `python` | `_PyIncrementalNewlineDecoder_decode` | memory |
| 0.62% | `python` | `unicode_subscript` | str |
| 0.59% | `python` | `PyFunction_NewWithQualName` | memory |
| 0.57% | `python` | `sre_ucs4_match` | library |
| 0.48% | `python` | `siphash13` | str |
| 0.42% | `python` | `cell_dealloc` | memory |
| 0.42% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.40% | `python` | `ucs4lib_utf8_decode` | unknown |
| 0.39% | `python` | `ucs4lib_fastsearch` | unknown |
| 0.38% | `python` | `_PyUnicode_FromUCS4` | str |
| 0.36% | `python` | `tupleiter_dealloc` | memory |
| 0.35% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.35% | `python` | `tuple_iter` | tuple |
| 0.33% | `python` | `memcmp@plt` | unknown |
| 0.32% | `python` | `insertdict` | dict |
| 0.32% | `python` | `unicode_dealloc` | memory |
| 0.32% | `python` | `_Py_MakeCoro` | unknown |
| 0.32% | `python` | `_sre_SRE_Pattern_match` | library |
| 0.31% | `python` | `_PyObject_GC_New` | gc |
| 0.30% | `python` | `tuple_subscript` | tuple |
| 0.29% | `[kernel.kallsyms]` | `clear_page_erms` | kernel |
| 0.29% | `python` | `ucs4lib_find_max_char` | unknown |
| 0.27% | `[kernel.kallsyms]` | `native_irq_return_iret` | kernel |
| 0.26% | `python` | `func_dealloc` | memory |
| 0.25% | `python` | `range_vectorcall` | miscobj |
| 0.25% | `python` | `dict_dealloc` | memory |
| 0.25% | `python` | `_Py_NewReference` | memory |

## typing_runtime_protocols

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 32.27% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 4.42% | `python` | `tuple_dealloc` | memory |
| 4.13% | `python` | `_PyObject_MakeTpCall` | dynamic |
| 2.89% | `python` | `get_or_create_weakref` | unknown |
| 2.05% | `python` | `PyArg_UnpackTuple` | calls |
| 2.01% | `python` | `_Py_dict_lookup` | lookup |
| 1.86% | `python` | `tuple_iter` | tuple |
| 1.75% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.40% | `python` | `PyDict_Contains` | dict |
| 1.38% | `python` | `list_dealloc` | memory |
| 1.33% | `python` | `tupleiter_dealloc` | memory |
| 1.31% | `python` | `_Py_type_getattro` | lookup |
| 1.22% | `python` | `PyObject_GetAttr` | dynamic |
| 1.22% | `python` | `_PyObject_Malloc` | memory |
| 1.07% | `python` | `PyTraceBack_Here` | exceptions |
| 1.03% | `python` | `bounded_lru_cache_wrapper` | unknown |
| 0.99% | `python` | `PySequence_Tuple` | dynamic |
| 0.93% | `python` | `type_new` | memory |
| 0.89% | `python` | `wrap_descr_get` | unknown |
| 0.81% | `python` | `tuple_hash` | tuple |
| 0.79% | `python` | `frame_dealloc` | memory |
| 0.75% | `python` | `PyObject_Vectorcall` | dynamic |
| 0.74% | `python` | `_PyFrame_MakeAndSetFrameObject` | unknown |
| 0.73% | `python` | `type_call` | dynamic |
| 0.73% | `python` | `type_dict` | dynamic |
| 0.73% | `python` | `PySet_Contains` | miscobj |
| 0.65% | `python` | `PyList_New` | memory |
| 0.65% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.61% | `python` | `deduce_unreachable` | gc |
| 0.60% | `python` | `_PyDict_GetItem_KnownHash` | dict |
| 0.59% | `python` | `mappingproxy_dealloc` | memory |
| 0.59% | `python` | `tuple_contains` | tuple |
| 0.59% | `python` | `_Py_type_getattro_impl` | dynamic |
| 0.55% | `python` | `PyObject_GetIter` | dynamic |
| 0.55% | `python` | `weakref___new__` | memory |
| 0.54% | `python` | `list_resize` | list |
| 0.52% | `python` | `_PyCode_New` | interpreter |
| 0.51% | `python` | `intern_common.part.0` | str |
| 0.50% | `python` | `weakref___init__` | unknown |
| 0.48% | `python` | `tuple_richcompare` | tuple |
| 0.48% | `python` | `weakref_richcompare` | unknown |
| 0.47% | `python` | `method_dealloc` | memory |
| 0.45% | `python` | `visit_decref` | gc |
| 0.45% | `python` | `PyObject_GenericGetAttr` | dynamic |
| 0.45% | `python` | `PyObject_IsInstance` | dynamic |
| 0.45% | `python` | `_PyObject_Call` | dynamic |
| 0.44% | `python` | `gc_collect_region.isra.0` | gc |
| 0.42% | `python` | `tb_dealloc` | memory |
| 0.42% | `python` | `BaseException_new` | memory |
| 0.40% | `python` | `method_vectorcall` | calls |
| 0.37% | `libc-2.31.so` | `__memcpy_avx_unaligned_erms` | libc |
| 0.37% | `python` | `getset_get` | dynamic |
| 0.37% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.37% | `python` | `r_object` | import |
| 0.36% | `python` | `setiter_dealloc` | memory |
| 0.36% | `python` | `lru_cache_make_key` | unknown |
| 0.34% | `python` | `wrapperdescr_call` | unknown |
| 0.33% | `python` | `PyObject_RichCompare` | dynamic |
| 0.33% | `python` | `_abc__abc_instancecheck` | unknown |
| 0.32% | `python` | `visit_reachable` | gc |
| 0.29% | `python` | `dict_get` | dict |
| 0.29% | `python` | `func_descr_get` | unknown |
| 0.29% | `python` | `PyObject_GC_Del` | gc |
| 0.29% | `python` | `dict_dealloc` | memory |
| 0.28% | `python` | `PyUnicode_FromKindAndData` | str |
| 0.27% | `python` | `builtin_getattr` | lookup |
| 0.26% | `python` | `wrapper_call` | unknown |
| 0.26% | `python` | `Py_XDECREF.lto_priv.1` | unknown |
| 0.26% | `python` | `setiter_iternext` | miscobj |
| 0.25% | `python` | `set_iter` | miscobj |

## unpickle_pure_python

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 55.21% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 3.69% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 2.75% | `python` | `PyDict_GetItemRef` | dict |
| 2.47% | `python` | `_io_BytesIO_read` | unknown |
| 1.63% | `python` | `PyObject_IsTrue` | dynamic |
| 1.49% | `python` | `insertdict` | dict |
| 1.35% | `python` | `unicode_decode_utf8` | str |
| 1.11% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 1.11% | `python` | `bytes_subscript` | str |
| 1.07% | `python` | `type_new` | memory |
| 0.99% | `python` | `unicode_vectorcall` | str |
| 0.97% | `python` | `PyObject_GetItem` | dynamic |
| 0.97% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.88% | `python` | `object_dealloc` | memory |
| 0.70% | `python` | `siphash13` | str |
| 0.70% | `python` | `deduce_unreachable` | gc |
| 0.69% | `python` | `unicode_dealloc` | memory |
| 0.68% | `python` | `PyObject_IsInstance` | dynamic |
| 0.66% | `python` | `intern_common.part.0` | str |
| 0.61% | `python` | `_PyCode_New` | interpreter |
| 0.54% | `python` | `visit_decref` | gc |
| 0.49% | `libc-2.31.so` | `__memcpy_avx_unaligned_erms` | libc |
| 0.49% | `python` | `gc_collect_region.isra.0` | gc |
| 0.46% | `python` | `dictresize` | dict |
| 0.41% | `python` | `dict_dealloc` | memory |
| 0.40% | `python` | `PyMem_Realloc` | memory |
| 0.40% | `python` | `list_subscript` | list |
| 0.37% | `python` | `visit_reachable` | gc |
| 0.37% | `python` | `long_hash` | int |
| 0.36% | `python` | `r_object` | import |
| 0.34% | `python` | `list_dealloc` | memory |
| 0.34% | `python` | `tuple_dealloc` | memory |
| 0.33% | `python` | `PyObject_GetAttr` | dynamic |
| 0.32% | `python` | `PyObject_Hash` | dynamic |
| 0.31% | `python` | `list_append` | list |
| 0.30% | `python` | `PyUnicode_FromKindAndData` | str |

## xml_etree

| percentage | object | symbol | category |
| ---: | :--- | :--- | :--- |
| 22.47% | `python` | `_PyEval_EvalFrameDefault` | interpreter |
| 3.70% | `python` | `PyObject_GetAttr` | dynamic |
| 2.93% | `pyexpat.cpython-314-x86_64-linux-gnu.so` | `doContent` | library |
| 2.34% | `pyexpat.cpython-314-x86_64-linux-gnu.so` | `PyExpat_XML_Parse` | library |
| 2.07% | `python` | `_io_TextIOWrapper_write` | unknown |
| 1.94% | `python` | `deduce_unreachable` | gc |
| 1.85% | `pyexpat.cpython-314-x86_64-linux-gnu.so` | `normal_contentTok` | library |
| 1.64% | `pyexpat.cpython-314-x86_64-linux-gnu.so` | `hash` | library |
| 1.60% | `pyexpat.cpython-314-x86_64-linux-gnu.so` | `storeAtts` | library |
| 1.55% | `python` | `visit_decref` | gc |
| 1.54% | `python` | `unicode_dealloc` | memory |
| 1.52% | `python` | `_PyEval_FrameClearAndPop` | interpreter |
| 1.45% | `python` | `visit_reachable` | gc |
| 1.41% | `python` | `_PyObject_GC_New` | gc |
| 1.41% | `_elementtree.cpython-314-x86_64-linux-gnu.so` | `makeuniversal.isra.0` | library |
| 1.32% | `python` | `PyUnicode_Concat` | str |
| 1.24% | `python` | `PyObject_GC_Del` | gc |
| 1.21% | `python` | `PyUnicode_DecodeUTF8` | str |
| 1.21% | `python` | `PyObject_VectorcallMethod` | dynamic |
| 1.19% | `libc-2.31.so` | `__memcpy_avx_unaligned_erms` | libc |
| 1.06% | `python` | `gc_collect_region.isra.0` | gc |
| 1.06% | `python` | `tuple_dealloc` | memory |
| 1.04% | `python` | `object_isinstance` | dynamic |
| 0.99% | `python` | `PyUnicode_Format` | str |
| 0.95% | `python` | `long_to_decimal_string_internal` | int |
| 0.92% | `python` | `_PyFunction_Vectorcall` | calls |
| 0.92% | `python` | `PyBytes_FromStringAndSize` | str |
| 0.90% | `python` | `list_dealloc` | memory |
| 0.83% | `python` | `type_new` | memory |
| 0.81% | `python` | `PyUnicode_Contains` | str |
| 0.80% | `_elementtree.cpython-314-x86_64-linux-gnu.so` | `elementiter_next` | library |
| 0.79% | `_elementtree.cpython-314-x86_64-linux-gnu.so` | `treebuilder_handle_start` | library |
| 0.73% | `python` | `siphash13` | str |
| 0.72% | `python` | `PyDict_GetItemWithError` | dict |
| 0.72% | `python` | `vgetargs1_impl` | calls |
| 0.71% | `_elementtree.cpython-314-x86_64-linux-gnu.so` | `element_dealloc` | library |
| 0.70% | `python` | `getset_get` | dynamic |
| 0.69% | `python` | `object_dealloc` | memory |
| 0.66% | `python` | `BaseException_vectorcall` | exceptions |
| 0.61% | `_elementtree.cpython-314-x86_64-linux-gnu.so` | `element_gc_traverse` | library |
| 0.59% | `_elementtree.cpython-314-x86_64-linux-gnu.so` | `treebuilder_handle_end.isra.0` | library |
| 0.56% | `python` | `visit_add_to_container` | gc |
| 0.56% | `python` | `list_vectorcall` | list |
| 0.56% | `python` | `_PyEvalFramePushAndInit` | interpreter |
| 0.47% | `_elementtree.cpython-314-x86_64-linux-gnu.so` | `expat_data_handler` | library |
| 0.46% | `_elementtree.cpython-314-x86_64-linux-gnu.so` | `Py_XDECREF` | library |
| 0.45% | `python` | `PyDict_GetItemRef` | dict |
| 0.45% | `python` | `unicode_decode_utf8` | str |
| 0.44% | `python` | `intern_common.part.0` | str |
| 0.41% | `python` | `stringlib__two_way.lto_priv.1` | str |
| 0.41% | `python` | `_PyCode_New` | interpreter |
| 0.38% | `python` | `_PyObject_GC_NewVar` | gc |
| 0.37% | `_elementtree.cpython-314-x86_64-linux-gnu.so` | `element_getitem` | library |
| 0.37% | `python` | `_PyObject_MakeTpCall` | dynamic |
| 0.36% | `libc-2.31.so` | `__memcmp_avx2_movbe` | libc |
| 0.36% | `python` | `tuple_traverse` | gc |
| 0.35% | `python` | `_PyErr_SetObject` | exceptions |
| 0.35% | `python` | `unicodekeys_lookup_unicode` | lookup |
| 0.35% | `python` | `PyDict_Contains` | dict |
| 0.35% | `python` | `PyObject_SetAttr` | dynamic |
| 0.33% | `python` | `list_iter` | list |
| 0.33% | `libc-2.31.so` | `__memset_avx2_unaligned_erms` | libc |
| 0.29% | `python` | `r_object` | import |
| 0.29% | `python` | `_textiowrapper_writeflush` | unknown |
| 0.29% | `python` | `PyMem_Realloc` | memory |
| 0.29% | `python` | `dict_dealloc` | memory |
| 0.28% | `python` | `BaseException_dealloc` | memory |
| 0.28% | `python` | `_PyUnicodeWriter_PrepareInternal` | str |
| 0.28% | `python` | `vectorcall_method` | calls |
| 0.27% | `python` | `PyList_New` | memory |
| 0.27% | `python` | `PyList_Append` | list |
| 0.26% | `python` | `PyTuple_Pack` | tuple |


## Categories

### interpreter

34.47% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 30.69% | python | _PyEval_EvalFrameDefault |
| 2.01% | python | _PyEval_FrameClearAndPop |
| 0.58% | python | _PyEvalFramePushAndInit |
| 0.54% | python | _PyCode_New |
| 0.10% | python | _PyEval_LoadGlobalStackRef |
| 0.09% | python | _PyEval_EvalFrameDefault.cold |
| 0.09% | python | _PyFrame_ClearExceptCode |
| 0.05% | python | call_instrumentation_vector |
| 0.05% | python | _PyPegen_fill_token |
| 0.03% | python | _PyEval_LoadName |
| 0.03% | python | PyEval_SaveThread |
| 0.03% | python | _PyPegen_update_memo |
| 0.02% | python | _PyEval_GetAwaitable |
| 0.02% | python | _PyCode_Validate |
| 0.02% | python | _PyPegen_name_token |
| 0.02% | python | _PyEval_SliceIndex |
| 0.01% | python | PyEval_RestoreThread |
| 0.01% | python | _PyCode_GetCode |
| 0.01% | python | _PyPegen_Parser_Free |
| 0.01% | python | PyEval_GetFrame |
| 0.01% | python | _PyEval_ImportName |
| 0.01% | python | _PyPegen_expect_token |
| 0.01% | python | _PyEval_GetFrame |
| 0.00% | python | PyEval_EvalCode |

### gc

12.10% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 2.11% | python | visit_decref |
| 2.03% | python | deduce_unreachable |
| 1.92% | python | visit_reachable |
| 1.68% | python | gc_collect_region.isra.0 |
| 1.17% | python | visit_add_to_container |
| 0.59% | python | dict_traverse |
| 0.47% | python | PyObject_GC_Del |
| 0.36% | python | subtype_traverse |
| 0.27% | python | _PyObject_GC_New |
| 0.26% | python | _PyObject_GC_NewVar |
| 0.26% | python | list_traverse |
| 0.23% | python | _PyGC_Collect |
| 0.13% | python | func_traverse |
| 0.13% | python | tuple_traverse |
| 0.11% | python | gen_traverse |
| 0.09% | python | set_traverse |
| 0.06% | python | type_traverse |
| 0.05% | python | PyObject_GC_UnTrack |
| 0.03% | python | meth_traverse |
| 0.03% | python | PyObject_GC_Track |
| 0.02% | python | context_tp_traverse |
| 0.01% | python | descr_traverse |
| 0.01% | python | gc_traverse |
| 0.01% | python | module_traverse |
| 0.01% | python | PyObject_IS_GC |
| 0.01% | python | method_traverse |
| 0.01% | python | cell_traverse |
| 0.00% | python | _PyObject_GC_Resize |
| 0.00% | python | property_traverse |

### memory

10.38% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 1.03% | python | type_new |
| 0.96% | python | tuple_dealloc |
| 0.83% | python | list_dealloc |
| 0.79% | python | long_dealloc |
| 0.56% | python | unicode_dealloc |
| 0.42% | python | dict_dealloc |
| 0.40% | python | gen_dealloc |
| 0.31% | python | subtype_dealloc |
| 0.27% | python | PyMem_Free |
| 0.24% | python | PyFunction_NewWithQualName |
| 0.22% | python | _PyLong_New |
| 0.22% | python | PyType_GenericAlloc |
| 0.22% | python | PyUnicode_New |
| 0.21% | python | meth_dealloc |
| 0.21% | python | PyMem_Malloc |
| 0.19% | python | object_new |
| 0.18% | python | PyList_New |
| 0.17% | python | _PyObject_Malloc |
| 0.16% | python | func_dealloc |
| 0.15% | python | set_dealloc |
| 0.14% | python | object_dealloc |
| 0.13% | python | code_dealloc |
| 0.12% | python | method_dealloc |
| 0.10% | python | float_dealloc |
| 0.10% | python | slice_dealloc |
| 0.09% | python | listiter_dealloc |
| 0.09% | python | PyTuple_New |
| 0.08% | python | frame_dealloc |
| 0.08% | python | tupleiter_dealloc |
| 0.07% | python | BaseException_new |
| 0.07% | python | PyType_GenericNew |
| 0.07% | python | memset@plt |
| 0.07% | python | list_new_prealloc |
| 0.07% | python | PyMem_Realloc |
| 0.07% | python | _Py_Dealloc |
| 0.06% | python | StopIteration_dealloc |
| 0.06% | python | _PyObject_Calloc |
| 0.06% | python | allocate_from_new_pool |
| 0.05% | python | context_tp_dealloc |
| 0.05% | python | memcpy@plt |
| 0.05% | python | dictiter_dealloc |
| 0.05% | python | PyDict_New |
| 0.04% | python | zip_new |
| 0.04% | python | _PyObject_Free |
| 0.04% | python | range_dealloc |
| 0.04% | python | cell_dealloc |
| 0.04% | python | tp_new_wrapper |
| 0.03% | python | dictview_dealloc |
| 0.03% | python | PySlice_New |
| 0.03% | python | BaseException_dealloc |
| 0.03% | python | async_gen_asend_dealloc |
| 0.03% | python | _PyObject_New |
| 0.03% | python | tb_dealloc |
| 0.03% | python | async_gen_asend_new |
| 0.03% | python | make_new_set |
| 0.03% | python | _Py_NewReference |
| 0.02% | python | zip_dealloc |
| 0.02% | python | _PyFloat_ExactDealloc |
| 0.02% | python | slot_tp_new |
| 0.02% | python | _PyAsyncGenValueWrapperNew |
| 0.02% | python | setiter_dealloc |
| 0.02% | python | match_dealloc |
| 0.02% | python | weakref_dealloc |
| 0.02% | python | async_gen_wrapped_val_dealloc |
| 0.02% | python | PyObject_CallFinalizerFromDealloc |
| 0.02% | python | structseq_dealloc |
| 0.01% | python | PySet_New |
| 0.01% | python | mappingproxy_dealloc |
| 0.01% | python | weakref___new__ |
| 0.01% | python | _PyObject_Realloc |
| 0.01% | python | descr_dealloc |
| 0.01% | python | _PyTokenizer_translate_newlines.constprop.0 |
| 0.01% | python | _PyIncrementalNewlineDecoder_decode.cold |
| 0.01% | python | _PyIncrementalNewlineDecoder_decode |
| 0.01% | python | PyCMethod_New |
| 0.01% | python | unicode_new |
| 0.01% | python | pattern_new_match.isra.0 |
| 0.01% | python | _PyMem_RawMalloc |
| 0.01% | python | context_new_from_vars |
| 0.00% | python | type_dealloc |
| 0.00% | python | PyMem_Calloc |
| 0.00% | python | map_dealloc |
| 0.00% | python | tuple_alloc |
| 0.00% | python | reversed_new_impl |

### library

8.03% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 2.00% | python | sre_ucs1_match |
| 0.85% | libz.so.1.2.11 | crc32_combine64 |
| 0.83% | python | sre_ucs2_charset.isra.0 |
| 0.44% | _json.cpython-314-x86_64-linux-gnu.so | _parse_object_unicode |
| 0.33% | libz.so.1.2.11 | inflateBackEnd |
| 0.22% | libpthread-2.31.so | __pthread_mutex_lock |
| 0.21% | libpthread-2.31.so | pthread_mutex_unlock |
| 0.21% | python | sre_search |
| 0.15% | python | sre_ucs1_count |
| 0.12% | python | _sre_SRE_Pattern_match |
| 0.12% | _json.cpython-314-x86_64-linux-gnu.so | encoder_listencode_dict |
| 0.11% | tracer.cpython-314-x86_64-linux-gnu.so | CTracer_trace |
| 0.07% | libsqlite3.so.0.8.6 | sqlite3_reset |
| 0.07% | libm-2.31.so | __ieee754_pow_fma |
| 0.07% | _asyncio.cpython-314-x86_64-linux-gnu.so | TaskObj_traverse |
| 0.06% | libm-2.31.so | __cos_fma |
| 0.05% | ld-2.31.so | do_lookup_x |
| 0.05% | libz.so.1.2.11 | inflateCodesUsed |
| 0.05% | array.cpython-314-x86_64-linux-gnu.so | array_subscr |
| 0.04% | libm-2.31.so | __fmod_finite@GLIBC_2.15 |
| 0.04% | python | pattern_subx |
| 0.04% | _json.cpython-314-x86_64-linux-gnu.so | py_encode_basestring_ascii |
| 0.04% | pyexpat.cpython-314-x86_64-linux-gnu.so | doContent |
| 0.04% | _json.cpython-314-x86_64-linux-gnu.so | _match_number_unicode.isra.0 |
| 0.03% | libm-2.31.so | __sin_fma |
| 0.03% | ld-2.31.so | strcmp |
| 0.03% | fastbinary.cpython-314-x86_64-linux-gnu.so | apache::thrift::py::ProtocolBase<apache::thrift::py::BinaryProtocol>::encodeValue |
| 0.03% | ld-2.31.so | _dl_relocate_object |
| 0.03% | pyexpat.cpython-314-x86_64-linux-gnu.so | PyExpat_XML_Parse |
| 0.03% | _decimal.cpython-314-x86_64-linux-gnu.so | _mpd_qaddsub |
| 0.03% | _decimal.cpython-314-x86_64-linux-gnu.so | nm_mpd_qmul |
| 0.02% | _decimal.cpython-314-x86_64-linux-gnu.so | nm_mpd_qadd |
| 0.02% | libsqlite3.so.0.8.6 | sqlite3_randomness |
| 0.02% | pyexpat.cpython-314-x86_64-linux-gnu.so | normal_contentTok |
| 0.02% | _decimal.cpython-314-x86_64-linux-gnu.so | _mpd_baseshiftr |
| 0.02% | _asyncio.cpython-314-x86_64-linux-gnu.so | task_step_impl |
| 0.02% | libpthread-2.31.so | pthread_cond_signal@@GLIBC_2.3.2 |
| 0.02% | libz.so.1.2.11 | inflate |
| 0.02% | _pickle.cpython-314-x86_64-linux-gnu.so | save |
| 0.02% | pyexpat.cpython-314-x86_64-linux-gnu.so | hash |
| 0.02% | pyexpat.cpython-314-x86_64-linux-gnu.so | storeAtts |
| 0.02% | _decimal.cpython-314-x86_64-linux-gnu.so | _mpd_qmul |
| 0.02% | _heapq.cpython-314-x86_64-linux-gnu.so | _heapq_heappop |
| 0.02% | math.cpython-314-x86_64-linux-gnu.so | factorial_partial_product |
| 0.02% | ld-2.31.so | _dl_lookup_symbol_x |
| 0.02% | _decimal.cpython-314-x86_64-linux-gnu.so | mpd_qfinalize |
| 0.02% | array.cpython-314-x86_64-linux-gnu.so | array_ass_subscr |
| 0.02% | _decimal.cpython-314-x86_64-linux-gnu.so | mpd_qshiftr |
| 0.02% | _elementtree.cpython-314-x86_64-linux-gnu.so | makeuniversal.isra.0 |
| 0.02% | _decimal.cpython-314-x86_64-linux-gnu.so | convert_op |
| 0.02% | _decimal.cpython-314-x86_64-linux-gnu.so | find_state_left_or_right |
| 0.02% | ld-2.31.so | check_match |
| 0.02% | _asyncio.cpython-314-x86_64-linux-gnu.so | FutureObj_traverse |
| 0.02% | python | sre_ucs1_match.cold |
| 0.02% | _bisect.cpython-314-x86_64-linux-gnu.so | _bisect_bisect_right |
| 0.02% | _decimal.cpython-314-x86_64-linux-gnu.so | dec_mpd_qquantize |
| 0.02% | _asyncio.cpython-314-x86_64-linux-gnu.so | TaskObj_clear |
| 0.02% | _asyncio.cpython-314-x86_64-linux-gnu.so | _asyncio_Task___init__ |
| 0.01% | _asyncio.cpython-314-x86_64-linux-gnu.so | task_step |
| 0.01% | _asyncio.cpython-314-x86_64-linux-gnu.so | TaskStepMethWrapper_traverse |
| 0.01% | _asyncio.cpython-314-x86_64-linux-gnu.so | _asyncio_Future_add_done_callback |
| 0.01% | math.cpython-314-x86_64-linux-gnu.so | math_factorial |
| 0.01% | libsqlite3.so.0.8.6 | sqlite3_value_double |
| 0.01% | libsqlite3.so.0.8.6 | sqlite3_wal_checkpoint |
| 0.01% | _sqlite3.cpython-314-x86_64-linux-gnu.so | _pysqlite_query_execute |
| 0.01% | array.cpython-314-x86_64-linux-gnu.so | d_setitem |
| 0.01% | _json.cpython-314-x86_64-linux-gnu.so | _parse_array_unicode |
| 0.01% | libsqlite3.so.0.8.6 | sqlite3_preupdate_old |
| 0.01% | libsqlite3.so.0.8.6 | sqlite3_value_int64 |
| 0.01% | _decimal.cpython-314-x86_64-linux-gnu.so | mpd_qquantize |
| 0.01% | fastbinary.cpython-314-x86_64-linux-gnu.so | apache::thrift::py::ProtocolBase<apache::thrift::py::BinaryProtocol>::decodeValue |
| 0.01% | _decimal.cpython-314-x86_64-linux-gnu.so | dec_dealloc |
| 0.01% | _asyncio.cpython-314-x86_64-linux-gnu.so | future_init |
| 0.01% | libsqlite3.so.0.8.6 | sqlite3_extended_errcode |
| 0.01% | _elementtree.cpython-314-x86_64-linux-gnu.so | elementiter_next |
| 0.01% | _elementtree.cpython-314-x86_64-linux-gnu.so | treebuilder_handle_start |
| 0.01% | _asyncio.cpython-314-x86_64-linux-gnu.so | enter_task.isra.0 |
| 0.01% | _elementtree.cpython-314-x86_64-linux-gnu.so | element_gc_traverse |
| 0.01% | _elementtree.cpython-314-x86_64-linux-gnu.so | element_dealloc |
| 0.01% | libsqlite3.so.0.8.6 | sqlite3_step |
| 0.01% | libsqlite3.so.0.8.6 | sqlite3_vtab_config |
| 0.01% | _asyncio.cpython-314-x86_64-linux-gnu.so | task_wakeup |
| 0.01% | fastbinary.cpython-314-x86_64-linux-gnu.so | apache::thrift::py::ProtocolBase<apache::thrift::py::BinaryProtocol>::readStruct |
| 0.01% | fastbinary.cpython-314-x86_64-linux-gnu.so | apache::thrift::py::ProtocolBase<apache::thrift::py::BinaryProtocol>::readBytes |
| 0.01% | _decimal.cpython-314-x86_64-linux-gnu.so | dec_addstatus |
| 0.01% | libsqlite3.so.0.8.6 | sqlite3_enable_shared_cache |
| 0.01% | libz.so.1.2.11 | adler32_combine64 |
| 0.01% | _struct.cpython-314-x86_64-linux-gnu.so | unpack |
| 0.01% | _decimal.cpython-314-x86_64-linux-gnu.so | PyDecType_New.isra.0 |
| 0.01% | _decimal.cpython-314-x86_64-linux-gnu.so | PyDecType_FromLongExact |
| 0.01% | _elementtree.cpython-314-x86_64-linux-gnu.so | treebuilder_handle_end.isra.0 |
| 0.01% | tracer.cpython-314-x86_64-linux-gnu.so | CTracer_set_pdata_stack |
| 0.01% | _sqlite3.cpython-314-x86_64-linux-gnu.so | pysqlite_cursor_init |
| 0.01% | math.cpython-314-x86_64-linux-gnu.so | math_sqrt |
| 0.01% | _asyncio.cpython-314-x86_64-linux-gnu.so | TaskObj_finalize |
| 0.01% | _struct.cpython-314-x86_64-linux-gnu.so | s_pack |
| 0.01% | python | sre_ucs4_match |
| 0.01% | math.cpython-314-x86_64-linux-gnu.so | math_cos |
| 0.01% | _asyncio.cpython-314-x86_64-linux-gnu.so | call_soon.isra.0 |
| 0.01% | _decimal.cpython-314-x86_64-linux-gnu.so | current_context |
| 0.01% | _decimal.cpython-314-x86_64-linux-gnu.so | dec_str |
| 0.01% | python | _sre_compile |
| 0.01% | libm-2.31.so | powf64 |
| 0.01% | _decimal.cpython-314-x86_64-linux-gnu.so | word_to_string |
| 0.01% | libsqlite3.so.0.8.6 | sqlite3_str_value |
| 0.01% | _elementtree.cpython-314-x86_64-linux-gnu.so | expat_data_handler |
| 0.01% | _asyncio.cpython-314-x86_64-linux-gnu.so | FutureObj_clear |
| 0.01% | _random.cpython-314-x86_64-linux-gnu.so | _random_Random_getrandbits |
| 0.01% | _elementtree.cpython-314-x86_64-linux-gnu.so | Py_XDECREF |
| 0.01% | _asyncio.cpython-314-x86_64-linux-gnu.so | FutureIter_traverse |
| 0.01% | libsqlite3.so.0.8.6 | sqlite3_mutex_try |
| 0.01% | libsqlite3.so.0.8.6 | sqlite3_value_pointer |
| 0.01% | _elementtree.cpython-314-x86_64-linux-gnu.so | element_getitem |
| 0.01% | libsqlite3.so.0.8.6 | sqlite3_exec |
| 0.01% | _pickle.cpython-314-x86_64-linux-gnu.so | memo_put.isra.0 |
| 0.01% | _asyncio.cpython-314-x86_64-linux-gnu.so | task_call_step_soon |
| 0.01% | _sqlite3.cpython-314-x86_64-linux-gnu.so | pysqlite_cursor_iternext |
| 0.01% | fastbinary.cpython-314-x86_64-linux-gnu.so | apache::thrift::py::BinaryProtocol::readFieldBegin |
| 0.01% | _random.cpython-314-x86_64-linux-gnu.so | _random_Random_random |
| 0.00% | libsqlite3.so.0.8.6 | sqlite3_free |
| 0.00% | ld-2.31.so | _dl_map_object_from_fd |
| 0.00% | _sqlite3.cpython-314-x86_64-linux-gnu.so | pysqlite_connection_execute |
| 0.00% | libpthread-2.31.so | pthread_create@@GLIBC_2.2.5 |
| 0.00% | _sqlite3.cpython-314-x86_64-linux-gnu.so | bind_param.isra.0 |
| 0.00% | _json.cpython-314-x86_64-linux-gnu.so | 0x0000000000002794 |
| 0.00% | libsqlite3.so.0.8.6 | sqlite3_close_v2 |
| 0.00% | python | _sre_SRE_Pattern_sub |
| 0.00% | _decimal.cpython-314-x86_64-linux-gnu.so | ctx_mpd_qquantize |
| 0.00% | _decimal.cpython-314-x86_64-linux-gnu.so | mpd_qadd |
| 0.00% | _json.cpython-314-x86_64-linux-gnu.so | 0x0000000000002534 |
| 0.00% | array.cpython-314-x86_64-linux-gnu.so | d_getitem |
| 0.00% | _asyncio.cpython-314-x86_64-linux-gnu.so | future_schedule_callbacks |
| 0.00% | _json.cpython-314-x86_64-linux-gnu.so | 0x0000000000002664 |
| 0.00% | libpthread-2.31.so | sem_post@@GLIBC_2.2.5 |
| 0.00% | python | _sre_SRE_Pattern_search |
| 0.00% | python | _sre_SRE_Match_end |
| 0.00% | libsqlite3.so.0.8.6 | sqlite3_realloc64 |
| 0.00% | _struct.cpython-314-x86_64-linux-gnu.so | pack |
| 0.00% | _json.cpython-314-x86_64-linux-gnu.so | scanner_call |
| 0.00% | libz.so.1.2.11 | adler32_z |
| 0.00% | fastbinary.cpython-314-x86_64-linux-gnu.so | apache::thrift::py::parse_struct_item_spec |
| 0.00% | math.cpython-314-x86_64-linux-gnu.so | math_sin |
| 0.00% | _asyncio.cpython-314-x86_64-linux-gnu.so | future_add_done_callback |
| 0.00% | array.cpython-314-x86_64-linux-gnu.so | 0x00000000000049c4 |
| 0.00% | libsqlite3.so.0.8.6 | sqlite3_db_config |
| 0.00% | libsqlite3.so.0.8.6 | sqlite3_sourceid |
| 0.00% | _json.cpython-314-x86_64-linux-gnu.so | encoder_new |
| 0.00% | python | sre_ucs2_match |
| 0.00% | array.cpython-314-x86_64-linux-gnu.so | 0x00000000000047e4 |
| 0.00% | array.cpython-314-x86_64-linux-gnu.so | 0x0000000000004644 |
| 0.00% | libpthread-2.31.so | pthread_getspecific |
| 0.00% | _decimal.cpython-314-x86_64-linux-gnu.so | _mpd_to_string |
| 0.00% | libsqlite3.so.0.8.6 | sqlite3_aggregate_context |
| 0.00% | _json.cpython-314-x86_64-linux-gnu.so | 0x00000000000024c4 |
| 0.00% | _asyncio.cpython-314-x86_64-linux-gnu.so | TaskStepMethWrapper_dealloc |

### dynamic

5.59% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 0.85% | python | PyObject_GetAttr |
| 0.37% | python | object_isinstance |
| 0.36% | python | _PyObject_MakeTpCall |
| 0.25% | python | PyObject_SetAttr |
| 0.25% | python | _PyObject_GetMethod |
| 0.18% | python | method_get |
| 0.15% | python | PyObject_Free |
| 0.15% | python | PyNumber_AsSsize_t |
| 0.14% | python | type_ready |
| 0.14% | python | PyObject_VectorcallMethod |
| 0.13% | python | PyObject_Vectorcall |
| 0.13% | python | PyObject_GetItem |
| 0.13% | python | PyObject_RichCompare |
| 0.12% | python | PyObject_IsTrue |
| 0.11% | python | PyObject_GetOptionalAttr |
| 0.11% | python | _PySuper_Lookup |
| 0.10% | python | PyObject_GetIter |
| 0.10% | python | getset_get |
| 0.10% | python | _PyObject_GenericGetAttrWithDict |
| 0.10% | python | PyObject_IsInstance |
| 0.10% | python | PyObject_RichCompareBool |
| 0.08% | python | type_call |
| 0.07% | python | PyObject_Hash |
| 0.07% | python | slot_tp_richcompare |
| 0.06% | python | _Py_type_getattro_impl |
| 0.06% | python | PyObject_CallOneArg |
| 0.06% | python | _PyObject_ClearFreeLists |
| 0.05% | python | _PyObject_Call |
| 0.05% | python | _PyObject_VectorcallTstate.lto_priv.1 |
| 0.05% | python | PyType_GetModuleByDef |
| 0.05% | python | PyObject_Str |
| 0.05% | python | PyNumber_Multiply |
| 0.04% | python | PyObject_SetItem |
| 0.04% | python | PyNumber_TrueDivide |
| 0.04% | python | PySequence_Tuple |
| 0.04% | python | _PyObject_LookupSpecial |
| 0.04% | python | StopIteration_init |
| 0.04% | python | PyNumber_Add |
| 0.03% | python | PyNumber_And |
| 0.03% | python | PyObject_VisitManagedDict |
| 0.03% | python | PyNumber_Subtract |
| 0.03% | python | _PyObject_LookupSpecialMethod |
| 0.02% | python | PyType_IsSubtype |
| 0.02% | python | object_richcompare |
| 0.02% | python | PyIter_Send |
| 0.02% | python | PyNumber_Remainder |
| 0.02% | python | PyObject_SelfIter |
| 0.02% | python | PyObject_GenericGetAttr |
| 0.02% | python | PyObject_ClearWeakRefs |
| 0.02% | python | type_dict |
| 0.01% | python | PyObject_LengthHint |
| 0.01% | python | PyNumber_FloorDivide |
| 0.01% | python | PySequence_Fast |
| 0.01% | python | object_get_class |
| 0.01% | python | PyObject_ClearManagedDict |
| 0.01% | python | PyNumber_Negative |
| 0.01% | python | PyNumber_Rshift |
| 0.01% | python | delitem_common |
| 0.01% | python | PyObject_GenericHash |
| 0.01% | python | _PyNumber_Index |
| 0.01% | python | PyMapping_GetOptionalItem |
| 0.01% | python | object_recursive_isinstance.part.0 |
| 0.01% | python | PyNumber_InPlaceAdd |
| 0.01% | python | PyObject_CallFunction |
| 0.01% | python | PyObject_GetBuffer |
| 0.01% | python | type_dealloc_common |
| 0.01% | python | _PyObject_GenericSetAttrWithDict |
| 0.01% | python | object_vacall |
| 0.01% | python | PyNumber_Index |
| 0.01% | python | object_init |
| 0.01% | python | _PyNumber_PowerNoMod |
| 0.01% | python | PyNumber_Lshift |
| 0.01% | python | PyObject_SetAttrString |
| 0.01% | python | PyObject_DelItem |
| 0.01% | python | type___instancecheck__ |
| 0.00% | python | PyIter_Next |
| 0.00% | python | PyObject_HasAttrWithError |
| 0.00% | python | PyObject_GenericGetDict |
| 0.00% | python | PyObject_Call |
| 0.00% | python | PyObject_VectorcallDict |
| 0.00% | python | type_get_mro |
| 0.00% | python | PyObject_CallMethodObjArgs |
| 0.00% | python | type_clear |
| 0.00% | python | PyNumber_Or |
| 0.00% | python | type_setattro |
| 0.00% | python | object___reduce_ex__ |

### unknown

4.15% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 0.20% | python | slot_tp_init |
| 0.17% | python | _Py_MakeCoro |
| 0.10% | python | clear_slots |
| 0.08% | python | func_descr_get |
| 0.08% | python | _PyFrame_MakeAndSetFrameObject |
| 0.07% | python | _PyBuildSlice_Consume2 |
| 0.06% | python | builtin_min |
| 0.06% | python | _PyStack_UnpackDict |
| 0.05% | python | get_or_create_weakref |
| 0.04% | python | dictkeys_decref.part.0 |
| 0.04% | python | _io_BytesIO_read |
| 0.04% | python | _PyCfg_OptimizeCodeUnit.constprop.0 |
| 0.04% | python | _Py_module_getattro |
| 0.04% | python | path_converter |
| 0.04% | python | slot_tp_hash |
| 0.04% | python | gen_send_ex2 |
| 0.04% | python | builtin_sum |
| 0.04% | python | wrapperdescr_call |
| 0.04% | python | gen_send_ex |
| 0.04% | python | vectorcall_maybe.constprop.0 |
| 0.04% | python | slot_mp_subscript |
| 0.04% | python | ScandirIterator_iternext |
| 0.03% | python | slot_mp_ass_subscript |
| 0.03% | python | member_get |
| 0.03% | python | Py_XDECREF.lto_priv.1 |
| 0.03% | python | cm_descr_get |
| 0.03% | python | _PyAssemble_MakeCodeObject |
| 0.03% | python | zip_next |
| 0.03% | python | PySys_Audit |
| 0.03% | python | dictitems_iter |
| 0.03% | python | convert_to_double |
| 0.03% | python | term_raw |
| 0.03% | python | _io_TextIOWrapper_write |
| 0.03% | python | hashtable_unicode_hash |
| 0.03% | python | state_init |
| 0.03% | python | code_hash |
| 0.03% | python | unsafe_tuple_compare |
| 0.03% | python | call_one_instrument |
| 0.02% | python | bitwise_xor_rule |
| 0.02% | python | finalize_interp_clear |
| 0.02% | python | convertitem |
| 0.02% | python | bounded_lru_cache_wrapper |
| 0.02% | python | hashtable_unicode_compare |
| 0.02% | python | binary_op |
| 0.02% | python | atom_rule |
| 0.02% | python | binary_op1 |
| 0.02% | python | Py_XDECREF.lto_priv.7 |
| 0.02% | python | _add_methods_to_object |
| 0.02% | python | _PyCfg_OptimizedCfgToInstructionSequence |
| 0.02% | python | lookup_maybe_method |
| 0.02% | python | _Py_VaBuildStack.constprop.0 |
| 0.02% | python | _PyCoro_GetAwaitableIter |
| 0.02% | python | make_range_object |
| 0.02% | python | _Py_slot_tp_getattr_hook |
| 0.02% | python | PyContextVar_Get |
| 0.02% | python | memcmp@plt |
| 0.02% | python | _PyModule_ClearDict |
| 0.02% | python | shift_expr_rule |
| 0.02% | python | call_trace_func.isra.0 |
| 0.02% | python | builtin_sorted |
| 0.02% | [vdso] | __vdso_clock_gettime |
| 0.02% | python | builtin_max |
| 0.02% | python | PyIndex_Check |
| 0.02% | python | sum_rule |
| 0.02% | python | pthread_self@plt |
| 0.02% | python | builtin_id |
| 0.02% | python | as_ucs4 |
| 0.01% | python | context_run |
| 0.01% | python | _PyDictKeys_StringLookup |
| 0.01% | python | primary_raw |
| 0.01% | python | write_bytes |
| 0.01% | python | expression_rule |
| 0.01% | python | symtable_add_def_ctx |
| 0.01% | python | classmethod_get |
| 0.01% | python | build_indices_generic |
| 0.01% | python | slot_sq_item |
| 0.01% | python | ins1 |
| 0.01% | python | builtin_hasattr |
| 0.01% | python | builtin_issubclass |
| 0.01% | python | int_bit_length |
| 0.01% | python | get_type_attr_as_size |
| 0.01% | python | mro_implementation_unlocked |
| 0.01% | python | _PyContext_Exit |
| 0.01% | python | slot_sq_contains |
| 0.01% | python | wrap_descr_get |
| 0.01% | python | _PyCompile_ConstCacheMergeOne |
| 0.01% | python | _io_open |
| 0.01% | python | maybe_small_long |
| 0.01% | python | fill_time |
| 0.01% | python | inversion_rule |
| 0.01% | python | builtin_hash |
| 0.01% | python | PyType_FromMetaclass |
| 0.01% | python | _PyLexer_update_fstring_expr |
| 0.01% | python | analyze_block |
| 0.01% | python | unsafe_long_compare |
| 0.01% | python | _PyCfg_FromInstructionSequence |
| 0.01% | python | gc_list_move |
| 0.01% | python | astfold_expr |
| 0.01% | python | codegen_nameop |
| 0.01% | python | map_next |
| 0.01% | python | wrap_objobjargproc |
| 0.01% | python | os_listdir |
| 0.01% | python | symtable_visit_expr |
| 0.01% | python | gen_close |
| 0.01% | python | binary_iop1 |
| 0.01% | python | bitwise_or_rule |
| 0.01% | python | _copy_characters |
| 0.01% | python | codegen_addop_load_const |
| 0.01% | python | builtin_any |
| 0.01% | python | weakref___init__ |
| 0.01% | python | notify_context_watchers.isra.0.constprop.0 |
| 0.01% | python | make_dict_from_instance_attributes |
| 0.01% | python | codegen_visit_expr |
| 0.01% | python | PyModule_AddObjectRef |
| 0.01% | python | do_string_format |
| 0.01% | python | lru_cache_make_key |
| 0.01% | python | ucs4lib_find_max_char |
| 0.01% | python | _PyBytes_Resize |
| 0.01% | python | find_keyword |
| 0.01% | python | weakref_richcompare |
| 0.01% | python | frozenset_vectorcall |
| 0.01% | python | Py_UNICODE_ISALNUM.lto_priv.1 |
| 0.01% | python | delitemif_lock_held |
| 0.01% | python | copy_values |
| 0.01% | python | sm_descr_get |
| 0.01% | python | do_mktuple |
| 0.01% | python | PyType_GetBaseByToken |
| 0.01% | python | unsafe_latin_compare |
| 0.01% | python | chain_next |
| 0.01% | python | getset_set |
| 0.01% | python | write_str |
| 0.01% | python | slot_tp_iter |
| 0.01% | python | simple_stmt_rule |
| 0.01% | python | add_subclass |
| 0.01% | python | 0x0000000000080740 |
| 0.01% | python | iter_iternext |
| 0.01% | python | PyThread_get_thread_ident_ex |
| 0.01% | python | update_slots_callback |
| 0.01% | python | pthread_mutex_unlock@plt |
| 0.01% | python | strlen@plt |
| 0.01% | python | descr_setcheck.isra.0 |
| 0.01% | python | _io_FileIO___init__ |
| 0.01% | python | term_rule |
| 0.01% | python | _stringio_readline.cold |
| 0.01% | python | _PyCfg_ToInstructionSequence |
| 0.01% | python | _Py_SourceAsString |
| 0.01% | python | named_expression_rule |
| 0.01% | python | super_getattro |
| 0.01% | python | pthread_mutex_lock@plt |
| 0.01% | python | builtin___build_class__ |
| 0.01% | python | _Py_call_instrumentation_arg |
| 0.01% | python | unsafe_object_compare |
| 0.01% | python | PyTime_AsSecondsDouble |
| 0.01% | python | ucs4lib_utf8_decode |
| 0.01% | python | remove_unreachable |
| 0.01% | python | new_dict |
| 0.01% | python | PyFile_WriteObject |
| 0.01% | python | subtype_clear |
| 0.01% | python | binary_iop |
| 0.01% | python | update_slot |
| 0.01% | python | _abc__abc_instancecheck |
| 0.01% | python | _PyType_AllocNoTrack |
| 0.01% | python | _validate_inner |
| 0.01% | python | propagate_line_numbers |
| 0.01% | python | remove_redundant_nops_and_jumps |
| 0.01% | python | islice_next |
| 0.01% | python | frame_settrace |
| 0.01% | python | 0x0000000000080750 |
| 0.01% | python | pop_lock_held |
| 0.01% | python | _PyContext_Enter |
| 0.01% | python | __errno_location@plt |
| 0.01% | python | duplicate_exits_without_lineno |
| 0.01% | python | _loop1_30_rule |
| 0.01% | python | _PyRecursiveMutex_TryUnlock |
| 0.01% | python | ucs4lib_fastsearch |
| 0.01% | python | va_build_value |
| 0.01% | python | find_frozen |
| 0.00% | python | update_symbols |
| 0.00% | python | builtin_repr |
| 0.00% | python | os_fspath |
| 0.00% | python | map_vectorcall |
| 0.00% | python | match_getslice_by_index |
| 0.00% | python | assign_version_tag |
| 0.00% | python | primary_rule |
| 0.00% | python | _pystat_fromstructstat |
| 0.00% | python | builtin_print |
| 0.00% | python | weakref_hash |
| 0.00% | python | _PyStack_UnpackDict_Free |
| 0.00% | python | ascii_upper_or_lower |
| 0.00% | python | target_with_star_atom_rule |
| 0.00% | python | wrapper_call |
| 0.00% | python | _PyBytes_FromList |
| 0.00% | python | slot_nb_bool |
| 0.00% | python | dictbytype |
| 0.00% | python | memmove@plt |
| 0.00% | python | _Py_bytes_lower |
| 0.00% | python | _PyFunction_FromConstructor |
| 0.00% | python | subtype_dict |
| 0.00% | python | specialize_py_call |
| 0.00% | python | clear_weakref_lock_held |
| 0.00% | python | keys_lock_held |
| 0.00% | python | _imp_is_builtin |
| 0.00% | python | specialize_dict_access.isra.0 |
| 0.00% | python | solid_base |
| 0.00% | python | _textiowrapper_writeflush |
| 0.00% | python | bitwise_and_rule |
| 0.00% | python | insert_split_value.isra.0 |
| 0.00% | python | pthread_cond_signal@plt |
| 0.00% | python | label_exception_targets |
| 0.00% | python | _PyBytesWriter_Finish |
| 0.00% | python | slot_sq_length |
| 0.00% | python | posix_do_stat.isra.0 |
| 0.00% | python | clear_lock_held |
| 0.00% | python | slot_nb_subtract |
| 0.00% | python | PyOS_FSPath |
| 0.00% | python | os_stat |
| 0.00% | python | t_primary_raw |
| 0.00% | python | decode_current_locale |
| 0.00% | python | _PyInstructionSequence_ApplyLabelMap |
| 0.00% | python | args_rule |
| 0.00% | python | path_cleanup |
| 0.00% | python | import_star |
| 0.00% | python | gallop_right |
| 0.00% | python | strchr@plt |
| 0.00% | python | _io__Buffered_read |
| 0.00% | python | strings_rule |
| 0.00% | python | merge_at |
| 0.00% | python | property_descr_get |
| 0.00% | python | member_set |
| 0.00% | python | _PyMutex_LockTimed |
| 0.00% | python | gallop_left |
| 0.00% | python | new_keys_object.constprop.0 |
| 0.00% | python | compute_item.isra.0 |
| 0.00% | python | slot_tp_setattro |
| 0.00% | python | analyze_descriptor |
| 0.00% | python | compute_line |
| 0.00% | python | merge_from_seq2_lock_held |
| 0.00% | python | state_fini |

### int

3.97% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 0.86% | python | k_mul |
| 0.53% | python | long_add |
| 0.45% | python | x_divrem |
| 0.26% | python | long_hash |
| 0.24% | python | PyLong_FromLong |
| 0.20% | python | x_add |
| 0.19% | python | long_to_decimal_string_internal |
| 0.16% | python | long_sub |
| 0.12% | python | long_bitwise |
| 0.11% | python | x_sub |
| 0.10% | python | long_richcompare |
| 0.09% | python | PyLong_FromString |
| 0.08% | python | long_div |
| 0.07% | python | long_and |
| 0.07% | python | long_mul |
| 0.07% | python | long_rshift |
| 0.06% | python | long_mod |
| 0.04% | python | PyLong_AsDouble |
| 0.04% | python | long_mul_method |
| 0.03% | python | PyLong_FromUnsignedLongLong |
| 0.02% | python | long_lshift_method |
| 0.02% | python | PyLong_FromUnsignedLong |
| 0.02% | python | _PyLong_GCD |
| 0.01% | python | _PyLong_FromBytes |
| 0.01% | python | _PyLong_FromSTwoDigits |
| 0.01% | python | PyLong_AsLong |
| 0.01% | python | long_lshift_int64 |
| 0.01% | python | long_xor |
| 0.01% | python | PyLong_FromSsize_t |
| 0.01% | python | _PyLong_Frexp |
| 0.01% | python | PyLong_AsLongAndOverflow |
| 0.01% | python | PyLong_AsSsize_t |
| 0.01% | python | long_vectorcall |
| 0.01% | python | long_add_method |
| 0.01% | python | PyLong_AsInt |
| 0.00% | python | _PyLong_FromByteArray |
| 0.00% | python | long_or |
| 0.00% | python | PyLong_FromLongLong |
| 0.00% | python | PyLong_FromUnicodeObject |

### dict

3.94% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 1.04% | python | PyDict_GetItemRef |
| 0.53% | python | insertdict |
| 0.33% | python | PyDict_Contains |
| 0.32% | python | PyDict_SetItem |
| 0.29% | python | dictresize |
| 0.26% | python | dict_get |
| 0.20% | python | dict_setdefault_ref_lock_held |
| 0.20% | python | insert_to_emptydict |
| 0.17% | python | dictiter_iternextkey |
| 0.15% | python | dict_subscript |
| 0.08% | python | dictiter_iternextitem |
| 0.06% | python | dict_merge |
| 0.04% | python | dict_items |
| 0.03% | python | PyDict_Copy |
| 0.03% | python | PyDict_GetItemWithError |
| 0.03% | python | PyDict_Next |
| 0.02% | python | dict_getitem |
| 0.02% | python | PyDict_DelItem |
| 0.01% | python | _PyDict_Next |
| 0.01% | python | dictiter_iternextvalue |
| 0.01% | python | _PyDict_GetItem_KnownHash |
| 0.01% | python | PyDict_SetItemString |
| 0.01% | python | PyDict_GetItemStringRef |
| 0.01% | python | dict_update_common |
| 0.01% | python | dict_iter |
| 0.01% | python | _PyDict_LoadBuiltinsFromGlobals |
| 0.01% | python | dict_ass_sub |
| 0.00% | python | _PyDict_DetachFromObject |

### str

3.72% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 0.64% | python | intern_common.part.0 |
| 0.52% | python | siphash13 |
| 0.29% | python | PyUnicode_FromKindAndData |
| 0.29% | python | PyUnicode_Substring |
| 0.18% | python | _PyUnicode_JoinArray |
| 0.16% | python | PyBytes_FromStringAndSize |
| 0.11% | python | unicode_replace |
| 0.09% | python | _PyUnicodeWriter_PrepareInternal |
| 0.09% | python | PyUnicode_Format |
| 0.09% | python | unicode_decode_utf8 |
| 0.07% | python | _PyUnicodeWriter_WriteStr |
| 0.07% | python | PyUnicodeWriter_WriteStr |
| 0.06% | python | PyUnicode_RichCompare |
| 0.05% | python | PyUnicode_InternFromString |
| 0.05% | python | PyUnicode_Concat |
| 0.05% | python | unicode_subscript |
| 0.05% | python | bytes_subscript |
| 0.05% | python | resize_compact |
| 0.05% | python | unicode_hash |
| 0.04% | python | PyUnicode_Contains |
| 0.04% | python | unicode_from_format |
| 0.04% | python | intern_constants |
| 0.03% | python | unicode_encode |
| 0.03% | python | bytes_concat |
| 0.03% | python | PyUnicode_FromString |
| 0.03% | python | PyUnicode_DecodeUTF8 |
| 0.03% | python | stringlib_bytes_join.lto_priv.1 |
| 0.03% | python | PyUnicode_DecodeFSDefault |
| 0.02% | python | unicode_encode_utf8 |
| 0.02% | python | unicode_eq.lto_priv.1 |
| 0.02% | python | unicode_split |
| 0.02% | python | split |
| 0.01% | python | bytes_richcompare |
| 0.01% | python | unicode_vectorcall |
| 0.01% | python | unicode_startswith |
| 0.01% | python | unicode_repr |
| 0.01% | python | unicode_splitlines |
| 0.01% | python | PyUnicode_FSConverter |
| 0.01% | python | unicode_fromformat_write_utf8 |
| 0.01% | python | _PyUnicode_FromUCS4 |
| 0.01% | python | bytes_decode |
| 0.01% | python | unicode_decode_locale |
| 0.01% | python | unicode_join |
| 0.01% | python | _PyUnicodeWriter_Init |
| 0.01% | python | _PyUnicode_IsAlpha |
| 0.01% | python | unicode_rstrip |
| 0.01% | python | _PyUnicodeWriter_Finish |
| 0.01% | python | PyUnicode_FromWideChar |
| 0.01% | python | _PyUnicode_TranslateCharmap |
| 0.01% | python | unicode_find |
| 0.01% | python | unicode_rfind |
| 0.01% | python | unicode_strip |
| 0.01% | python | unicode_decode_utf8_writer |
| 0.01% | python | bytes_hash |
| 0.01% | python | PyUnicode_CompareWithASCIIString |
| 0.01% | python | unicode_isupper |
| 0.01% | python | PyUnicode_RPartition |
| 0.01% | python | PyUnicodeWriter_Create |
| 0.01% | python | stringlib__two_way.lto_priv.1 |
| 0.01% | python | PyUnicode_AsUTF8AndSize |
| 0.00% | python | unicode_endswith |
| 0.00% | python | PyUnicode_Append |
| 0.00% | python | PyUnicode_DecodeFSDefaultAndSize |
| 0.00% | python | PyUnicode_FindChar |
| 0.00% | python | _PyUnicode_FromASCII |
| 0.00% | python | _PyUnicodeWriter_WriteCharInline |
| 0.00% | python | _PyUnicode_IsDigit |
| 0.00% | python | PyUnicode_FromFormat |
| 0.00% | python | _PyUnicodeWriter_WriteSubstring |
| 0.00% | python | _PyUnicode_IsDecimalDigit |
| 0.00% | python | PyUnicode_Join |

### kernel

3.32% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 0.13% | [kernel.kallsyms] | native_irq_return_iret |
| 0.12% | [kernel.kallsyms] | clear_page_erms |
| 0.11% | [kernel.kallsyms] | copy_user_enhanced_fast_string |
| 0.09% | [kernel.kallsyms] | sync_regs |
| 0.09% | [kernel.kallsyms] | __d_lookup_rcu |
| 0.08% | [kernel.kallsyms] | rmqueue |
| 0.07% | [kernel.kallsyms] | zap_pte_range.isra.0 |
| 0.07% | [kernel.kallsyms] | _raw_spin_lock |
| 0.06% | [kernel.kallsyms] | memset_erms |
| 0.06% | [kernel.kallsyms] | free_pcppages_bulk |
| 0.05% | [kernel.kallsyms] | __handle_mm_fault |
| 0.04% | [kernel.kallsyms] | clear_bhb_loop |
| 0.04% | [kernel.kallsyms] | try_charge |
| 0.04% | [kernel.kallsyms] | get_mem_cgroup_from_mm |
| 0.04% | [kernel.kallsyms] | release_pages |
| 0.04% | [kernel.kallsyms] | link_path_walk.part.0 |
| 0.04% | [kernel.kallsyms] | filemap_map_pages |
| 0.03% | [kernel.kallsyms] | __pagevec_lru_add_fn |
| 0.03% | [kernel.kallsyms] | mem_cgroup_throttle_swaprate |
| 0.03% | [kernel.kallsyms] | kmem_cache_alloc |
| 0.03% | [kernel.kallsyms] | ext4_htree_store_dirent |
| 0.03% | [kernel.kallsyms] | __ext4fs_dirhash |
| 0.03% | [kernel.kallsyms] | handle_mm_fault |
| 0.03% | [kernel.kallsyms] | mem_cgroup_try_charge |
| 0.03% | [kernel.kallsyms] | syscall_return_via_sysret |
| 0.02% | [kernel.kallsyms] | strncpy_from_user |
| 0.02% | [kernel.kallsyms] | __alloc_pages_nodemask |
| 0.02% | [kernel.kallsyms] | filldir64 |
| 0.02% | [kernel.kallsyms] | page_remove_rmap |
| 0.02% | [kernel.kallsyms] | do_syscall_64 |
| 0.02% | [kernel.kallsyms] | inode_permission |
| 0.02% | [kernel.kallsyms] | find_get_entry |
| 0.02% | [kernel.kallsyms] | lookup_fast |
| 0.02% | [kernel.kallsyms] | generic_permission |
| 0.02% | [kernel.kallsyms] | copy_page |
| 0.02% | [kernel.kallsyms] | kmem_cache_free |
| 0.02% | [kernel.kallsyms] | do_user_addr_fault |
| 0.02% | [kernel.kallsyms] | entry_SYSCALL_64 |
| 0.02% | [kernel.kallsyms] | do_anonymous_page |
| 0.02% | [kernel.kallsyms] | find_vma |
| 0.02% | [kernel.kallsyms] | memcpy_erms |
| 0.02% | [kernel.kallsyms] | walk_component |
| 0.02% | [kernel.kallsyms] | vmacache_find |
| 0.02% | [kernel.kallsyms] | str2hashbuf_signed |
| 0.02% | [kernel.kallsyms] | memcg_kmem_get_cache |
| 0.02% | [kernel.kallsyms] | get_page_from_freelist |
| 0.01% | [kernel.kallsyms] | __count_memcg_events |
| 0.01% | [kernel.kallsyms] | __mod_memcg_state |
| 0.01% | [kernel.kallsyms] | __virt_addr_valid |
| 0.01% | [kernel.kallsyms] | smp_call_function_single |
| 0.01% | [kernel.kallsyms] | error_entry |
| 0.01% | [kernel.kallsyms] | ext4_getattr |
| 0.01% | [kernel.kallsyms] | __slab_free |
| 0.01% | [kernel.kallsyms] | page_fault |
| 0.01% | [kernel.kallsyms] | __mod_lruvec_state |
| 0.01% | [kernel.kallsyms] | rb_insert_color |
| 0.01% | [kernel.kallsyms] | rb_next |
| 0.01% | [kernel.kallsyms] | kfree |
| 0.01% | [kernel.kallsyms] | prep_new_page |
| 0.01% | [kernel.kallsyms] | perf_iterate_ctx |
| 0.01% | [kernel.kallsyms] | page_counter_cancel |
| 0.01% | [kernel.kallsyms] | set_root |
| 0.01% | [kernel.kallsyms] | security_inode_getattr |
| 0.01% | [kernel.kallsyms] | in_group_p |
| 0.01% | [kernel.kallsyms] | up_read |
| 0.01% | [kernel.kallsyms] | vsnprintf |
| 0.01% | [kernel.kallsyms] | __legitimize_mnt |
| 0.01% | [kernel.kallsyms] | show_cpuinfo |
| 0.01% | [kernel.kallsyms] | format_decode |
| 0.01% | [kernel.kallsyms] | _cond_resched |
| 0.01% | [kernel.kallsyms] | __lru_cache_add |
| 0.01% | [kernel.kallsyms] | generic_file_buffered_read |
| 0.01% | [kernel.kallsyms] | __kmalloc |
| 0.01% | [kernel.kallsyms] | __follow_mount_rcu.isra.0 |
| 0.01% | [kernel.kallsyms] | page_add_file_rmap |
| 0.01% | [kernel.kallsyms] | down_read_trylock |
| 0.01% | [kernel.kallsyms] | swapgs_restore_regs_and_return_to_usermode |
| 0.01% | [kernel.kallsyms] | entry_SYSCALL_64_after_hwframe |
| 0.01% | [kernel.kallsyms] | fsnotify |
| 0.01% | [kernel.kallsyms] | pagevec_lru_move_fn |
| 0.01% | [kernel.kallsyms] | lru_cache_add_active_or_unevictable |
| 0.01% | [kernel.kallsyms] | xas_load |
| 0.01% | [kernel.kallsyms] | __ext4_check_dir_entry |
| 0.01% | [kernel.kallsyms] | native_flush_tlb_one_user |
| 0.01% | [kernel.kallsyms] | mem_cgroup_from_task |
| 0.01% | [kernel.kallsyms] | alloc_pages_vma |
| 0.01% | [kernel.kallsyms] | rcu_all_qs |
| 0.01% | [kernel.kallsyms] | _raw_spin_lock_irqsave |
| 0.01% | [kernel.kallsyms] | page_counter_try_charge |
| 0.01% | [kernel.kallsyms] | string_nocheck |
| 0.01% | [kernel.kallsyms] | __mod_node_page_state |
| 0.01% | [kernel.kallsyms] | alloc_set_pte |
| 0.01% | [kernel.kallsyms] | __fget_light |
| 0.01% | [kernel.kallsyms] | getname_flags |
| 0.01% | [kernel.kallsyms] | memchr |
| 0.01% | [kernel.kallsyms] | __mod_zone_page_state |
| 0.01% | [kernel.kallsyms] | free_unref_page_list |
| 0.01% | [kernel.kallsyms] | mem_cgroup_commit_charge |
| 0.01% | [kernel.kallsyms] | security_inode_permission |
| 0.01% | [kernel.kallsyms] | call_filldir |
| 0.01% | [kernel.kallsyms] | free_unref_page_prepare.part.0 |
| 0.01% | [kernel.kallsyms] | unlock_page |
| 0.01% | [kernel.kallsyms] | fpregs_assert_state_consistent |
| 0.01% | [kernel.kallsyms] | __lookup_mnt |
| 0.01% | [kernel.kallsyms] | free_unref_page_commit |
| 0.01% | [kernel.kallsyms] | common_perm |
| 0.01% | [kernel.kallsyms] | free_pages_and_swap_cache |
| 0.01% | [kernel.kallsyms] | __check_heap_object |
| 0.01% | [kernel.kallsyms] | __vma_adjust |
| 0.01% | [kernel.kallsyms] | psi_task_change |
| 0.01% | [kernel.kallsyms] | __check_object_size |
| 0.01% | [kernel.kallsyms] | ___slab_alloc |
| 0.01% | [kernel.kallsyms] | vfs_getattr_nosec |
| 0.01% | [kernel.kallsyms] | lockref_put_return |
| 0.01% | [kernel.kallsyms] | xas_start |
| 0.01% | [kernel.kallsyms] | update_cfs_group |
| 0.01% | [kernel.kallsyms] | __d_lookup |
| 0.01% | [kernel.kallsyms] | perf_event_alloc |
| 0.01% | [kernel.kallsyms] | kthread_blkcg |
| 0.01% | [kernel.kallsyms] | mem_cgroup_try_charge_delay |
| 0.01% | [kernel.kallsyms] | __alloc_file |
| 0.01% | [kernel.kallsyms] | memcg_kmem_put_cache |
| 0.01% | [kernel.kallsyms] | update_curr |
| 0.01% | [kernel.kallsyms] | unmapped_area_topdown |
| 0.01% | [kernel.kallsyms] | path_init |
| 0.01% | [kernel.kallsyms] | pmd_devmap_trans_unstable |
| 0.01% | [kernel.kallsyms] | page_add_new_anon_rmap |
| 0.00% | [kernel.kallsyms] | vma_interval_tree_insert |
| 0.00% | [kernel.kallsyms] | kmem_cache_alloc_trace |
| 0.00% | [kernel.kallsyms] | common_file_perm |
| 0.00% | [kernel.kallsyms] | update_load_avg |
| 0.00% | [kernel.kallsyms] | cp_new_stat |
| 0.00% | [kernel.kallsyms] | native_sched_clock |
| 0.00% | [kernel.kallsyms] | htree_dirblock_to_tree |
| 0.00% | [kernel.kallsyms] | _raw_spin_lock_irq |
| 0.00% | [kernel.kallsyms] | mem_cgroup_page_lruvec |
| 0.00% | [kernel.kallsyms] | copy_process |
| 0.00% | [kernel.kallsyms] | __lock_text_start |
| 0.00% | [kernel.kallsyms] | do_dentry_open |
| 0.00% | [kernel.kallsyms] | filename_lookup |
| 0.00% | [kernel.kallsyms] | dput |
| 0.00% | [kernel.kallsyms] | rb_next_postorder |
| 0.00% | [kernel.kallsyms] | vma_interval_tree_remove |
| 0.00% | [kernel.kallsyms] | mem_cgroup_update_lru_size |
| 0.00% | [kernel.kallsyms] | uncharge_page |
| 0.00% | [kernel.kallsyms] | __update_load_avg_se |
| 0.00% | [kernel.kallsyms] | map_id_up |
| 0.00% | [kernel.kallsyms] | vm_normal_page |
| 0.00% | [kernel.kallsyms] | mem_cgroup_charge_statistics |
| 0.00% | [kernel.kallsyms] | __fput |
| 0.00% | [kernel.kallsyms] | native_write_msr |
| 0.00% | [kernel.kallsyms] | lockref_get_not_dead |
| 0.00% | [kernel.kallsyms] | mutex_lock |
| 0.00% | [kernel.kallsyms] | __do_page_fault |
| 0.00% | [kernel.kallsyms] | ext4_find_dest_de |
| 0.00% | [kernel.kallsyms] | may_open.isra.0 |
| 0.00% | [kernel.kallsyms] | unmap_page_range |
| 0.00% | [kernel.kallsyms] | __find_get_block |
| 0.00% | [kernel.kallsyms] | down_write |
| 0.00% | [kernel.kallsyms] | __queue_work |
| 0.00% | [kernel.kallsyms] | page_mapping |
| 0.00% | [kernel.kallsyms] | do_page_fault |
| 0.00% | [kernel.kallsyms] | ext4_dx_readdir |
| 0.00% | [kernel.kallsyms] | __calc_delta |
| 0.00% | [kernel.kallsyms] | apparmor_file_alloc_security |
| 0.00% | [kernel.kallsyms] | exit_to_usermode_loop |
| 0.00% | [kernel.kallsyms] | mark_page_accessed |
| 0.00% | [kernel.kallsyms] | do_sys_open |
| 0.00% | [kernel.kallsyms] | ext4_search_dir |
| 0.00% | [kernel.kallsyms] | path_lookupat.isra.0 |
| 0.00% | [kernel.kallsyms] | crc32c_pcl_intel_update |
| 0.00% | [kernel.kallsyms] | nmi_restore |
| 0.00% | [kernel.kallsyms] | prepare_exit_to_usermode |
| 0.00% | [kernel.kallsyms] | get_task_policy.part.0 |
| 0.00% | [kernel.kallsyms] | __x64_sys_newstat |
| 0.00% | [kernel.kallsyms] | propagate_protected_usage |

### libc

2.44% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 0.55% | libc-2.31.so | __memcpy_avx_unaligned_erms |
| 0.47% | libc-2.31.so | __memset_avx2_unaligned_erms |
| 0.26% | libc-2.31.so | _int_malloc |
| 0.16% | libc-2.31.so | __memcmp_avx2_movbe |
| 0.15% | libc-2.31.so | _int_free |
| 0.12% | libc-2.31.so | __libc_malloc |
| 0.09% | libc-2.31.so | __strlen_avx2 |
| 0.06% | libc-2.31.so | __memset_avx2_erms |
| 0.05% | libc-2.31.so | unlink_chunk.isra.0 |
| 0.04% | libc-2.31.so | cfree@GLIBC_2.2.5 |
| 0.03% | libc-2.31.so | __strchr_avx2 |
| 0.02% | libc-2.31.so | pthread_self |
| 0.02% | libc-2.31.so | wcsrtombs |
| 0.02% | libc-2.31.so | __strncmp_avx2 |
| 0.02% | libc-2.31.so | pthread_mutex_lock |
| 0.02% | libc-2.31.so | __strcmp_avx2 |
| 0.02% | libc-2.31.so | __memchr_avx2 |
| 0.02% | libc-2.31.so | __gconv_transform_internal_utf8 |
| 0.02% | libc-2.31.so | __errno_location |
| 0.01% | libc-2.31.so | pthread_mutex_unlock |
| 0.01% | libc-2.31.so | __gconv_transform_utf8_internal |
| 0.01% | libc-2.31.so | __libc_realloc |
| 0.01% | libc-2.31.so | _int_realloc |
| 0.01% | libc-2.31.so | malloc_consolidate |
| 0.01% | libc-2.31.so | __xstat64 |
| 0.01% | libc-2.31.so | _dl_addr |
| 0.01% | libcrypto.so.1.1 | EVP_DecodeUpdate |
| 0.01% | libc-2.31.so | pthread_cond_signal@@GLIBC_2.3.2 |
| 0.01% | libc-2.31.so | __strcpy_avx2 |
| 0.01% | libcrypto.so.1.1 | ASN1_tag2bit |
| 0.01% | libc-2.31.so | clock_gettime@@GLIBC_2.17 |
| 0.01% | libc-2.31.so | __mbsrtowcs_l |
| 0.01% | libcrypto.so.1.1 | ASN1_item_i2d |
| 0.00% | libc-2.31.so | calloc |
| 0.00% | libc-2.31.so | __memrchr_avx2 |
| 0.00% | libcrypto.so.1.1 | EVP_desx_cbc |
| 0.00% | libc-2.31.so | __dcigettext |
| 0.00% | libc-2.31.so | __strrchr_avx2 |
| 0.00% | libc-2.31.so | __wcslen_avx2 |
| 0.00% | libcrypto.so.1.1 | ASN1_item_ex_free |
| 0.00% | libcrypto.so.1.1 | ASN1_ENUMERATED_to_BN |
| 0.00% | libcrypto.so.1.1 | NETSCAPE_SPKI_print |
| 0.00% | libc-2.31.so | msort_with_tmp.part.0 |
| 0.00% | libc-2.31.so | read |
| 0.00% | libc-2.31.so | __open64 |

### miscobj

1.59% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 0.30% | python | set_contains_lock_held |
| 0.12% | python | set_issubset_impl |
| 0.10% | python | setiter_iternext |
| 0.07% | python | set_vectorcall |
| 0.07% | python | gen_iternext |
| 0.07% | python | set_lookkey |
| 0.07% | python | set_difference |
| 0.06% | python | range_vectorcall |
| 0.06% | python | make_gen |
| 0.06% | python | PySlice_Unpack |
| 0.05% | python | range_iter |
| 0.04% | python | bytearray_ass_subscript |
| 0.04% | python | PySet_Add |
| 0.04% | python | enum_next |
| 0.03% | python | dequeiter_next_lock_held.isra.0 |
| 0.03% | python | set_table_resize |
| 0.03% | python | range_subscript |
| 0.03% | python | set_add_entry |
| 0.02% | python | set_iter |
| 0.02% | python | deque_append_lock_held |
| 0.02% | python | set_merge_lock_held.part.0 |
| 0.02% | python | deque_append_impl |
| 0.02% | python | set_add |
| 0.02% | python | set_discard_entry |
| 0.01% | python | set_intersection |
| 0.01% | python | _PyGen_FetchStopIterationValue.cold |
| 0.01% | python | PySlice_AdjustIndices |
| 0.01% | python | _PyGen_SetStopIterationValue |
| 0.01% | python | deque_clear |
| 0.01% | python | deque_popleft_impl |
| 0.01% | python | PySet_Contains |
| 0.01% | python | _PySlice_GetLongIndices |
| 0.01% | python | set_richcompare |
| 0.01% | python | _PyGen_yf |
| 0.01% | python | PyBuffer_Release |
| 0.01% | python | _PyGen_FetchStopIterationValue |
| 0.01% | python | set_difference_update_internal |
| 0.01% | python | range_reverse |
| 0.00% | python | deque_append |
| 0.00% | python | deque_iter |
| 0.00% | python | dequeiter_next |

### list

1.47% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 0.29% | python | list_subscript |
| 0.22% | python | list_ass_slice_lock_held |
| 0.21% | python | list_iter |
| 0.15% | python | list_resize |
| 0.08% | python | listiter_next |
| 0.08% | python | list_contains |
| 0.06% | python | _list_extend |
| 0.05% | python | list_ass_subscript |
| 0.05% | python | list_remove |
| 0.05% | python | PyList_Append |
| 0.05% | python | list_sort_impl |
| 0.03% | python | list_vectorcall |
| 0.03% | python | list_concat |
| 0.03% | python | list_append |
| 0.03% | python | list_pop |
| 0.01% | python | list_clear_impl.constprop.0 |
| 0.01% | python | list_length |
| 0.01% | python | list_richcompare |
| 0.01% | python | list_item |
| 0.00% | python | list_insert |
| 0.00% | python | list_to_tuple |
| 0.00% | python | _PyList_Extend |
| 0.00% | python | list_index |

### tuple

1.12% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 0.54% | python | tuple_hash |
| 0.24% | python | _PyTuple_FromStackRefSteal |
| 0.09% | python | tuple_iter |
| 0.09% | python | tuple_richcompare |
| 0.05% | python | PyTuple_Pack |
| 0.03% | python | _PyTuple_FromArray |
| 0.02% | python | tuple_contains |
| 0.02% | python | _PyTuple_Resize |
| 0.01% | python | tuple_subscript |
| 0.01% | python | tupleiter_next |
| 0.01% | python | PyTuple_Size |
| 0.00% | python | tuple_concat |
| 0.00% | python | tuple_length |

### lookup

0.99% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 0.28% | python | find_name_in_mro |
| 0.21% | python | _Py_dict_lookup |
| 0.21% | python | unicodekeys_lookup_unicode |
| 0.17% | python | _Py_type_getattro |
| 0.05% | python | _PyType_LookupRef |
| 0.04% | python | builtin_getattr |
| 0.01% | python | PyMember_SetOne |
| 0.01% | python | _Py_hashtable_destroy |

### calls

0.90% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 0.30% | python | _PyFunction_Vectorcall |
| 0.08% | python | vgetargskeywords.constprop.0 |
| 0.07% | python | vgetargs1_impl |
| 0.06% | python | method_vectorcall |
| 0.05% | python | PyArg_UnpackTuple |
| 0.04% | python | _PyArg_UnpackKeywords |
| 0.04% | python | vectorcall_method |
| 0.03% | python | method_vectorcall_VARARGS_KEYWORDS |
| 0.03% | python | cfunction_vectorcall_FASTCALL_KEYWORDS |
| 0.02% | python | cfunction_vectorcall_O |
| 0.02% | python | method_vectorcall_FASTCALL_KEYWORDS_METHOD |
| 0.02% | python | cfunction_vectorcall_NOARGS |
| 0.02% | python | _Py_CheckFunctionResult |
| 0.02% | python | method_vectorcall_O |
| 0.01% | python | method_vectorcall_VARARGS |
| 0.01% | python | _PyArg_UnpackKeywordsWithVararg |
| 0.01% | python | method_vectorcall_NOARGS |
| 0.01% | python | PyArg_ParseTupleAndKeywords |
| 0.01% | python | PyArg_Parse |
| 0.01% | python | cfunction_call |
| 0.01% | python | method_vectorcall_FASTCALL |
| 0.01% | python | cfunction_vectorcall_FASTCALL_KEYWORDS_METHOD |
| 0.00% | python | PyArg_ParseTuple |
| 0.00% | python | cfunction_vectorcall_FASTCALL |

### float

0.72% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 0.41% | python | _PyFloat_FromDouble_ConsumeInputs |
| 0.09% | python | float_div |
| 0.06% | python | PyFloat_FromDouble |
| 0.04% | python | float_richcompare |
| 0.03% | python | PyFloat_AsDouble |
| 0.03% | python | float_sub |
| 0.03% | python | float_pow |
| 0.02% | python | float_mul |
| 0.01% | python | float_add |
| 0.00% | python | float_rem |

### exceptions

0.45% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 0.14% | python | _PyErr_SetObject |
| 0.06% | python | PyCode_Addr2Line |
| 0.05% | python | PyTraceBack_Here |
| 0.05% | python | BaseException_vectorcall |
| 0.04% | python | PyErr_GivenExceptionMatches |
| 0.03% | python | PyErr_ExceptionMatches |
| 0.02% | python | PyErr_Format |
| 0.02% | python | PyErr_Occurred |
| 0.01% | python | _PyErr_SetKeyError |
| 0.01% | python | PyFrame_GetCode |
| 0.01% | python | PyFrame_GetLineNumber |
| 0.00% | python | PyErr_GetRaisedException |

### import

0.41% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 0.38% | python | r_object |
| 0.02% | python | PyImport_ImportModuleLevelObject |

### gil

0.12% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 0.11% | python | take_gil |

### async

0.07% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 0.04% | python | async_gen_asend_send |
| 0.02% | python | async_gen_unwrap_value.isra.0 |
| 0.00% | python | async_gen_init_hooks |

### compiler

0.06% total

| percentage | object | symbol |
| ---: | :--- | :--- |
| 0.05% | python | tok_get_normal_mode |
