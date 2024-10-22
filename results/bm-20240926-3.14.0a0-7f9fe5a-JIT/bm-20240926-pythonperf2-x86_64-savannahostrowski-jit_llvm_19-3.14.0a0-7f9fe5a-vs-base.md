# Results vs. base

- fork: savannahostrowski
- ref: jit_llvm_19
- machine: linux-x86_64
- commit hash: 7f9fe5a
- commit date: 2024-09-26
- overall geometric mean: 1.00x slower
- HPT reliability: 91.86%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240924-pythonperf2-x86_64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f | bm-20240926-pythonperf2-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 312 ms                                                                      | 309 ms: 1.01x faster                                                          |
| html5lib       | 71.4 ms                                                                     | 70.6 ms: 1.01x faster                                                         |
| Geometric mean | (ref)                                                                       | 1.01x faster                                                                  |

Benchmark hidden because not significant (2): docutils, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20240924-pythonperf2-x86_64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f | bm-20240926-pythonperf2-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|---------------------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_memoization    | 408 ms                                                                      | 404 ms: 1.01x faster                                                          |
| async_tree_memoization_tg | 394 ms                                                                      | 391 ms: 1.01x faster                                                          |
| asyncio_tcp_ssl           | 1.58 sec                                                                    | 1.58 sec: 1.00x faster                                                        |
| coroutines                | 21.3 ms                                                                     | 21.3 ms: 1.00x slower                                                         |
| Geometric mean            | (ref)                                                                       | 1.00x faster                                                                  |

Benchmark hidden because not significant (9): async_tree_none_tg, async_tree_none, async_tree_cpu_io_mixed, async_tree_io, async_tree_io_tg, async_tree_cpu_io_mixed_tg, asyncio_tcp, async_generators, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240924-pythonperf2-x86_64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f | bm-20240926-pythonperf2-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| pidigits       | 250 ms                                                                      | 250 ms: 1.00x slower                                                          |
| float          | 73.6 ms                                                                     | 75.6 ms: 1.03x slower                                                         |
| Geometric mean | (ref)                                                                       | 1.01x slower                                                                  |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240924-pythonperf2-x86_64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f | bm-20240926-pythonperf2-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                                      | 149 ms: 1.01x slower                                                          |
| regex_v8       | 25.8 ms                                                                     | 26.1 ms: 1.01x slower                                                         |
| regex_dna      | 234 ms                                                                      | 236 ms: 1.01x slower                                                          |
| regex_effbot   | 3.50 ms                                                                     | 3.56 ms: 1.02x slower                                                         |
| Geometric mean | (ref)                                                                       | 1.01x slower                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240924-pythonperf2-x86_64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f | bm-20240926-pythonperf2-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|---------------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| xml_etree_parse     | 143 ms                                                                      | 142 ms: 1.01x faster                                                          |
| json_loads          | 24.2 us                                                                     | 24.0 us: 1.01x faster                                                         |
| pickle_list         | 4.54 us                                                                     | 4.52 us: 1.00x faster                                                         |
| xml_etree_generate  | 80.2 ms                                                                     | 79.9 ms: 1.00x faster                                                         |
| pickle              | 10.6 us                                                                     | 10.7 us: 1.00x slower                                                         |
| unpickle_list       | 4.63 us                                                                     | 4.67 us: 1.01x slower                                                         |
| tomli_loads         | 2.11 sec                                                                    | 2.13 sec: 1.01x slower                                                        |
| json_dumps          | 10.6 ms                                                                     | 10.7 ms: 1.01x slower                                                         |
| xml_etree_iterparse | 98.2 ms                                                                     | 99.5 ms: 1.01x slower                                                         |
| pickle_dict         | 32.2 us                                                                     | 32.7 us: 1.01x slower                                                         |
| pickle_pure_python  | 325 us                                                                      | 330 us: 1.01x slower                                                          |
| unpickle            | 14.9 us                                                                     | 15.2 us: 1.02x slower                                                         |
| Geometric mean      | (ref)                                                                       | 1.01x slower                                                                  |

Benchmark hidden because not significant (2): xml_etree_process, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240924-pythonperf2-x86_64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f | bm-20240926-pythonperf2-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|------------------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup_no_site | 9.00 ms                                                                     | 8.98 ms: 1.00x faster                                                         |
| python_startup         | 13.4 ms                                                                     | 13.4 ms: 1.00x faster                                                         |
| Geometric mean         | (ref)                                                                       | 1.00x faster                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240924-pythonperf2-x86_64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f | bm-20240926-pythonperf2-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|-----------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| genshi_xml      | 68.6 ms                                                                     | 64.3 ms: 1.07x faster                                                         |
| django_template | 42.4 ms                                                                     | 40.8 ms: 1.04x faster                                                         |
| mako            | 9.16 ms                                                                     | 9.21 ms: 1.01x slower                                                         |
| Geometric mean  | (ref)                                                                       | 1.03x faster                                                                  |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                 | bm-20240924-pythonperf2-x86_64-python-54dd77fb8c880d7655ff-3.14.0a0-54dd77f | bm-20240926-pythonperf2-x86_64-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|---------------------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| raytrace                  | 332 ms                                                                      | 309 ms: 1.07x faster                                                          |
| genshi_xml                | 68.6 ms                                                                     | 64.3 ms: 1.07x faster                                                         |
| django_template           | 42.4 ms                                                                     | 40.8 ms: 1.04x faster                                                         |
| thrift                    | 915 us                                                                      | 889 us: 1.03x faster                                                          |
| sympy_expand              | 537 ms                                                                      | 525 ms: 1.02x faster                                                          |
| logging_simple            | 6.67 us                                                                     | 6.53 us: 1.02x faster                                                         |
| logging_format            | 7.26 us                                                                     | 7.12 us: 1.02x faster                                                         |
| json                      | 5.33 ms                                                                     | 5.24 ms: 1.02x faster                                                         |
| scimark_lu                | 98.4 ms                                                                     | 96.8 ms: 1.02x faster                                                         |
| chaos                     | 66.9 ms                                                                     | 66.0 ms: 1.01x faster                                                         |
| generators                | 37.3 ms                                                                     | 36.8 ms: 1.01x faster                                                         |
| bench_thread_pool         | 927 us                                                                      | 915 us: 1.01x faster                                                          |
| html5lib                  | 71.4 ms                                                                     | 70.6 ms: 1.01x faster                                                         |
| sympy_str                 | 313 ms                                                                      | 309 ms: 1.01x faster                                                          |
| async_tree_memoization    | 408 ms                                                                      | 404 ms: 1.01x faster                                                          |
| pathlib                   | 15.9 ms                                                                     | 15.7 ms: 1.01x faster                                                         |
| async_tree_memoization_tg | 394 ms                                                                      | 391 ms: 1.01x faster                                                          |
| 2to3                      | 312 ms                                                                      | 309 ms: 1.01x faster                                                          |
| xml_etree_parse           | 143 ms                                                                      | 142 ms: 1.01x faster                                                          |
| json_loads                | 24.2 us                                                                     | 24.0 us: 1.01x faster                                                         |
| sqlglot_transpile         | 1.95 ms                                                                     | 1.93 ms: 1.01x faster                                                         |
| pickle_list               | 4.54 us                                                                     | 4.52 us: 1.00x faster                                                         |
| sympy_sum                 | 170 ms                                                                      | 169 ms: 1.00x faster                                                          |
| sympy_integrate           | 26.5 ms                                                                     | 26.4 ms: 1.00x faster                                                         |
| xml_etree_generate        | 80.2 ms                                                                     | 79.9 ms: 1.00x faster                                                         |
| asyncio_tcp_ssl           | 1.58 sec                                                                    | 1.58 sec: 1.00x faster                                                        |
| python_startup_no_site    | 9.00 ms                                                                     | 8.98 ms: 1.00x faster                                                         |
| python_startup            | 13.4 ms                                                                     | 13.4 ms: 1.00x faster                                                         |
| pidigits                  | 250 ms                                                                      | 250 ms: 1.00x slower                                                          |
| coroutines                | 21.3 ms                                                                     | 21.3 ms: 1.00x slower                                                         |
| pickle                    | 10.6 us                                                                     | 10.7 us: 1.00x slower                                                         |
| regex_compile             | 148 ms                                                                      | 149 ms: 1.01x slower                                                          |
| mako                      | 9.16 ms                                                                     | 9.21 ms: 1.01x slower                                                         |
| unpickle_list             | 4.63 us                                                                     | 4.67 us: 1.01x slower                                                         |
| regex_v8                  | 25.8 ms                                                                     | 26.1 ms: 1.01x slower                                                         |
| tomli_loads               | 2.11 sec                                                                    | 2.13 sec: 1.01x slower                                                        |
| deepcopy_reduce           | 2.92 us                                                                     | 2.95 us: 1.01x slower                                                         |
| regex_dna                 | 234 ms                                                                      | 236 ms: 1.01x slower                                                          |
| sqlglot_optimize          | 65.6 ms                                                                     | 66.3 ms: 1.01x slower                                                         |
| telco                     | 8.20 ms                                                                     | 8.30 ms: 1.01x slower                                                         |
| json_dumps                | 10.6 ms                                                                     | 10.7 ms: 1.01x slower                                                         |
| go                        | 148 ms                                                                      | 150 ms: 1.01x slower                                                          |
| coverage                  | 79.8 ms                                                                     | 80.8 ms: 1.01x slower                                                         |
| deltablue                 | 3.17 ms                                                                     | 3.21 ms: 1.01x slower                                                         |
| xml_etree_iterparse       | 98.2 ms                                                                     | 99.5 ms: 1.01x slower                                                         |
| pickle_dict               | 32.2 us                                                                     | 32.7 us: 1.01x slower                                                         |
| pickle_pure_python        | 325 us                                                                      | 330 us: 1.01x slower                                                          |
| regex_effbot              | 3.50 ms                                                                     | 3.56 ms: 1.02x slower                                                         |
| crypto_pyaes              | 69.9 ms                                                                     | 71.1 ms: 1.02x slower                                                         |
| fannkuch                  | 360 ms                                                                      | 366 ms: 1.02x slower                                                          |
| hexiom                    | 6.95 ms                                                                     | 7.06 ms: 1.02x slower                                                         |
| comprehensions            | 18.2 us                                                                     | 18.5 us: 1.02x slower                                                         |
| bpe_tokeniser             | 4.73 sec                                                                    | 4.82 sec: 1.02x slower                                                        |
| meteor_contest            | 129 ms                                                                      | 131 ms: 1.02x slower                                                          |
| unpickle                  | 14.9 us                                                                     | 15.2 us: 1.02x slower                                                         |
| sqlite_synth              | 2.66 us                                                                     | 2.72 us: 1.02x slower                                                         |
| richards_super            | 51.6 ms                                                                     | 52.8 ms: 1.02x slower                                                         |
| scimark_sor               | 104 ms                                                                      | 106 ms: 1.02x slower                                                          |
| float                     | 73.6 ms                                                                     | 75.6 ms: 1.03x slower                                                         |
| richards                  | 44.6 ms                                                                     | 45.9 ms: 1.03x slower                                                         |
| sqlglot_normalize         | 128 ms                                                                      | 132 ms: 1.03x slower                                                          |
| deepcopy_memo             | 26.9 us                                                                     | 28.0 us: 1.04x slower                                                         |
| Geometric mean            | (ref)                                                                       | 1.00x slower                                                                  |

Benchmark hidden because not significant (35): async_tree_none_tg, async_tree_none, genshi_text, pycparser, pprint_pformat, async_tree_cpu_io_mixed, async_tree_io, async_tree_io_tg, sqlglot_parse, nbody, mdp, async_tree_cpu_io_mixed_tg, tornado_http, pylint, logging_silent, asyncio_tcp, deepcopy, gc_traversal, async_generators, pprint_safe_repr, spectral_norm, docutils, pyflate, asyncio_websockets, xml_etree_process, dulwich_log, typing_runtime_protocols, create_gc_cycles, scimark_sparse_mat_mult, unpack_sequence, unpickle_pure_python, nqueens, scimark_monte_carlo, scimark_fft, bench_mp_pool

# HPT report

- Reliability score: 91.86% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x