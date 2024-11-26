# Results vs. 3.13.0

- fork: savannahostrowski
- ref: jit_llvm_19
- machine: windows-x86
- commit hash: 7f9fe5a
- commit date: 2024-09-26
- overall geometric mean: 1.096x faster
- HPT reliability: 91.83%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240926-pythonperf1_win32-x86-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 255 ms                                                          | 260 ms: 1.02x slower                                                             |
| docutils       | 1.80 sec                                                        | 2.00 sec: 1.11x slower                                                           |
| tornado_http   | 105 ms                                                          | 110 ms: 1.06x slower                                                             |
| Geometric mean | (ref)                                                           | 1.05x slower                                                                     |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240926-pythonperf1_win32-x86-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|---------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_none           | 245 ms                                                          | 221 ms: 1.11x faster                                                             |
| async_tree_memoization_tg | 287 ms                                                          | 260 ms: 1.10x faster                                                             |
| async_tree_memoization    | 302 ms                                                          | 280 ms: 1.08x faster                                                             |
| async_tree_none_tg        | 216 ms                                                          | 204 ms: 1.06x faster                                                             |
| async_tree_cpu_io_mixed   | 490 ms                                                          | 474 ms: 1.03x faster                                                             |
| async_tree_io             | 530 ms                                                          | 548 ms: 1.03x slower                                                             |
| async_tree_io_tg          | 499 ms                                                          | 530 ms: 1.06x slower                                                             |
| coroutines                | 16.1 ms                                                         | 18.2 ms: 1.13x slower                                                            |
| async_generators          | 267 ms                                                          | 322 ms: 1.21x slower                                                             |
| Geometric mean            | (ref)                                                           | 1.00x slower                                                                     |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240926-pythonperf1_win32-x86-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 81.4 ms                                                         | 48.6 ms: 1.67x faster                                                            |
| float          | 56.4 ms                                                         | 43.3 ms: 1.30x faster                                                            |
| pidigits       | 204 ms                                                          | 195 ms: 1.04x faster                                                             |
| Geometric mean | (ref)                                                           | 1.31x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240926-pythonperf1_win32-x86-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 101 ms                                                          | 103 ms: 1.02x slower                                                             |
| regex_v8       | 15.5 ms                                                         | 16.1 ms: 1.04x slower                                                            |
| regex_dna      | 112 ms                                                          | 119 ms: 1.06x slower                                                             |
| regex_effbot   | 1.82 ms                                                         | 1.96 ms: 1.08x slower                                                            |
| Geometric mean | (ref)                                                           | 1.05x slower                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240926-pythonperf1_win32-x86-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| xml_etree_generate   | 61.9 ms                                                         | 54.0 ms: 1.15x faster                                                            |
| tomli_loads          | 1.74 sec                                                        | 1.56 sec: 1.12x faster                                                           |
| json_dumps           | 7.53 ms                                                         | 6.85 ms: 1.10x faster                                                            |
| xml_etree_process    | 44.6 ms                                                         | 40.6 ms: 1.10x faster                                                            |
| json_loads           | 21.7 us                                                         | 21.2 us: 1.02x faster                                                            |
| xml_etree_iterparse  | 61.3 ms                                                         | 61.8 ms: 1.01x slower                                                            |
| xml_etree_parse      | 102 ms                                                          | 104 ms: 1.01x slower                                                             |
| unpickle_pure_python | 162 us                                                          | 168 us: 1.04x slower                                                             |
| pickle_pure_python   | 239 us                                                          | 255 us: 1.07x slower                                                             |
| Geometric mean       | (ref)                                                           | 1.04x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240926-pythonperf1_win32-x86-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup | 28.3 ms                                                         | 24.5 ms: 1.16x faster                                                            |
| Geometric mean | (ref)                                                           | 1.07x faster                                                                     |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240926-pythonperf1_win32-x86-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 7.02 ms                                                         | 5.48 ms: 1.28x faster                                                            |
| django_template | 32.0 ms                                                         | 34.7 ms: 1.08x slower                                                            |
| genshi_text     | 21.7 ms                                                         | 24.5 ms: 1.13x slower                                                            |
| genshi_xml      | 49.0 ms                                                         | 56.6 ms: 1.15x slower                                                            |
| Geometric mean  | (ref)                                                           | 1.02x slower                                                                     |

All benchmarks:
===============

| Benchmark                 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240926-pythonperf1_win32-x86-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|---------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| thrift                    | 10.3 ms                                                         | 788 us: 13.01x faster                                                            |
| coverage                  | 326 ms                                                          | 54.9 ms: 5.94x faster                                                            |
| deepcopy_memo             | 26.2 us                                                         | 15.5 us: 1.69x faster                                                            |
| nbody                     | 81.4 ms                                                         | 48.6 ms: 1.67x faster                                                            |
| spectral_norm             | 70.0 ms                                                         | 47.0 ms: 1.49x faster                                                            |
| create_gc_cycles          | 1.08 ms                                                         | 754 us: 1.44x faster                                                             |
| float                     | 56.4 ms                                                         | 43.3 ms: 1.30x faster                                                            |
| deepcopy                  | 311 us                                                          | 239 us: 1.30x faster                                                             |
| mako                      | 7.02 ms                                                         | 5.48 ms: 1.28x faster                                                            |
| scimark_sor               | 85.8 ms                                                         | 68.2 ms: 1.26x faster                                                            |
| fannkuch                  | 288 ms                                                          | 235 ms: 1.22x faster                                                             |
| gc_traversal              | 1.76 ms                                                         | 1.44 ms: 1.22x faster                                                            |
| scimark_sparse_mat_mult   | 2.88 ms                                                         | 2.36 ms: 1.22x faster                                                            |
| bench_mp_pool             | 93.6 ms                                                         | 77.5 ms: 1.21x faster                                                            |
| crypto_pyaes              | 56.6 ms                                                         | 47.6 ms: 1.19x faster                                                            |
| scimark_fft               | 204 ms                                                          | 173 ms: 1.18x faster                                                             |
| python_startup            | 28.3 ms                                                         | 24.5 ms: 1.16x faster                                                            |
| deepcopy_reduce           | 2.94 us                                                         | 2.56 us: 1.15x faster                                                            |
| xml_etree_generate        | 61.9 ms                                                         | 54.0 ms: 1.15x faster                                                            |
| tomli_loads               | 1.74 sec                                                        | 1.56 sec: 1.12x faster                                                           |
| comprehensions            | 13.1 us                                                         | 11.9 us: 1.11x faster                                                            |
| deltablue                 | 2.35 ms                                                         | 2.12 ms: 1.11x faster                                                            |
| async_tree_none           | 245 ms                                                          | 221 ms: 1.11x faster                                                             |
| async_tree_memoization_tg | 287 ms                                                          | 260 ms: 1.10x faster                                                             |
| json_dumps                | 7.53 ms                                                         | 6.85 ms: 1.10x faster                                                            |
| pprint_safe_repr          | 658 ms                                                          | 599 ms: 1.10x faster                                                             |
| xml_etree_process         | 44.6 ms                                                         | 40.6 ms: 1.10x faster                                                            |
| pyflate                   | 322 ms                                                          | 297 ms: 1.08x faster                                                             |
| meteor_contest            | 78.1 ms                                                         | 72.2 ms: 1.08x faster                                                            |
| async_tree_memoization    | 302 ms                                                          | 280 ms: 1.08x faster                                                             |
| json                      | 4.40 ms                                                         | 4.11 ms: 1.07x faster                                                            |
| pycparser                 | 869 ms                                                          | 818 ms: 1.06x faster                                                             |
| go                        | 111 ms                                                          | 104 ms: 1.06x faster                                                             |
| async_tree_none_tg        | 216 ms                                                          | 204 ms: 1.06x faster                                                             |
| pprint_pformat            | 1.32 sec                                                        | 1.26 sec: 1.05x faster                                                           |
| bench_thread_pool         | 1.04 ms                                                         | 995 us: 1.05x faster                                                             |
| pidigits                  | 204 ms                                                          | 195 ms: 1.04x faster                                                             |
| async_tree_cpu_io_mixed   | 490 ms                                                          | 474 ms: 1.03x faster                                                             |
| telco                     | 6.27 ms                                                         | 6.08 ms: 1.03x faster                                                            |
| richards_super            | 37.0 ms                                                         | 35.9 ms: 1.03x faster                                                            |
| json_loads                | 21.7 us                                                         | 21.2 us: 1.02x faster                                                            |
| pathlib                   | 89.1 ms                                                         | 87.5 ms: 1.02x faster                                                            |
| scimark_lu                | 60.7 ms                                                         | 59.8 ms: 1.02x faster                                                            |
| richards                  | 33.4 ms                                                         | 33.0 ms: 1.01x faster                                                            |
| dulwich_log               | 50.2 ms                                                         | 49.7 ms: 1.01x faster                                                            |
| scimark_monte_carlo       | 48.7 ms                                                         | 48.2 ms: 1.01x faster                                                            |
| nqueens                   | 75.1 ms                                                         | 74.5 ms: 1.01x faster                                                            |
| logging_format            | 8.59 us                                                         | 8.65 us: 1.01x slower                                                            |
| xml_etree_iterparse       | 61.3 ms                                                         | 61.8 ms: 1.01x slower                                                            |
| mdp                       | 1.70 sec                                                        | 1.72 sec: 1.01x slower                                                           |
| xml_etree_parse           | 102 ms                                                          | 104 ms: 1.01x slower                                                             |
| 2to3                      | 255 ms                                                          | 260 ms: 1.02x slower                                                             |
| logging_simple            | 7.89 us                                                         | 8.05 us: 1.02x slower                                                            |
| regex_compile             | 101 ms                                                          | 103 ms: 1.02x slower                                                             |
| sqlglot_normalize         | 223 ms                                                          | 230 ms: 1.03x slower                                                             |
| async_tree_io             | 530 ms                                                          | 548 ms: 1.03x slower                                                             |
| sqlglot_parse             | 1.02 ms                                                         | 1.06 ms: 1.04x slower                                                            |
| unpickle_pure_python      | 162 us                                                          | 168 us: 1.04x slower                                                             |
| sympy_str                 | 214 ms                                                          | 222 ms: 1.04x slower                                                             |
| regex_v8                  | 15.5 ms                                                         | 16.1 ms: 1.04x slower                                                            |
| typing_runtime_protocols  | 141 us                                                          | 148 us: 1.05x slower                                                             |
| sympy_sum                 | 108 ms                                                          | 114 ms: 1.05x slower                                                             |
| generators                | 21.5 ms                                                         | 22.7 ms: 1.05x slower                                                            |
| tornado_http              | 105 ms                                                          | 110 ms: 1.06x slower                                                             |
| sympy_expand              | 377 ms                                                          | 400 ms: 1.06x slower                                                             |
| async_tree_io_tg          | 499 ms                                                          | 530 ms: 1.06x slower                                                             |
| regex_dna                 | 112 ms                                                          | 119 ms: 1.06x slower                                                             |
| pickle_pure_python        | 239 us                                                          | 255 us: 1.07x slower                                                             |
| regex_effbot              | 1.82 ms                                                         | 1.96 ms: 1.08x slower                                                            |
| hexiom                    | 4.60 ms                                                         | 4.96 ms: 1.08x slower                                                            |
| sqlglot_transpile         | 1.26 ms                                                         | 1.36 ms: 1.08x slower                                                            |
| django_template           | 32.0 ms                                                         | 34.7 ms: 1.08x slower                                                            |
| chaos                     | 49.4 ms                                                         | 53.9 ms: 1.09x slower                                                            |
| sympy_integrate           | 15.2 ms                                                         | 16.8 ms: 1.10x slower                                                            |
| sqlglot_optimize          | 42.4 ms                                                         | 46.9 ms: 1.11x slower                                                            |
| docutils                  | 1.80 sec                                                        | 2.00 sec: 1.11x slower                                                           |
| genshi_text               | 21.7 ms                                                         | 24.5 ms: 1.13x slower                                                            |
| coroutines                | 16.1 ms                                                         | 18.2 ms: 1.13x slower                                                            |
| genshi_xml                | 49.0 ms                                                         | 56.6 ms: 1.15x slower                                                            |
| pylint                    | 225 ms                                                          | 271 ms: 1.21x slower                                                             |
| async_generators          | 267 ms                                                          | 322 ms: 1.21x slower                                                             |
| raytrace                  | 203 ms                                                          | 249 ms: 1.23x slower                                                             |
| Geometric mean            | (ref)                                                           | 1.10x faster                                                                     |

Benchmark hidden because not significant (4): async_tree_cpu_io_mixed_tg, logging_silent, html5lib, python_startup_no_site
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, gevent_hub, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240926-3.14.0a0-7f9fe5a-JIT/bm-20240926-pythonperf1_win32-x86-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.096x faster
# HPT report

- Reliability score: 91.83% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown