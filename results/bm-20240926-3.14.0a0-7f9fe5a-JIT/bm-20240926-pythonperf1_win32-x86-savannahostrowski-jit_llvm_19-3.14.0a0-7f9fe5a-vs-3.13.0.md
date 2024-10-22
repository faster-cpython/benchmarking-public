# Results vs. 3.13.0

- fork: savannahostrowski
- ref: jit_llvm_19
- machine: windows-x86
- commit hash: 7f9fe5a
- commit date: 2024-09-26
- overall geometric mean: 1.09x faster
- HPT reliability: 93.56%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240926-pythonperf1_win32-x86-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 253 ms                                                          | 260 ms: 1.03x slower                                                             |
| docutils       | 1.82 sec                                                        | 2.00 sec: 1.10x slower                                                           |
| html5lib       | 48.3 ms                                                         | 47.0 ms: 1.03x faster                                                            |
| tornado_http   | 104 ms                                                          | 110 ms: 1.06x slower                                                             |
| Geometric mean | (ref)                                                           | 1.04x slower                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240926-pythonperf1_win32-x86-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_tcp                | 842 ms                                                          | 668 ms: 1.26x faster                                                             |
| async_tree_none            | 246 ms                                                          | 221 ms: 1.11x faster                                                             |
| async_tree_memoization_tg  | 287 ms                                                          | 260 ms: 1.10x faster                                                             |
| async_tree_memoization     | 302 ms                                                          | 280 ms: 1.08x faster                                                             |
| async_tree_none_tg         | 219 ms                                                          | 204 ms: 1.07x faster                                                             |
| async_tree_cpu_io_mixed    | 494 ms                                                          | 474 ms: 1.04x faster                                                             |
| asyncio_tcp_ssl            | 17.4 sec                                                        | 17.0 sec: 1.02x faster                                                           |
| async_tree_cpu_io_mixed_tg | 464 ms                                                          | 467 ms: 1.01x slower                                                             |
| async_tree_io              | 537 ms                                                          | 548 ms: 1.02x slower                                                             |
| async_tree_io_tg           | 509 ms                                                          | 530 ms: 1.04x slower                                                             |
| coroutines                 | 15.7 ms                                                         | 18.2 ms: 1.16x slower                                                            |
| async_generators           | 274 ms                                                          | 322 ms: 1.18x slower                                                             |
| Geometric mean             | (ref)                                                           | 1.02x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240926-pythonperf1_win32-x86-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 81.9 ms                                                         | 48.6 ms: 1.68x faster                                                            |
| float          | 57.8 ms                                                         | 43.3 ms: 1.33x faster                                                            |
| pidigits       | 202 ms                                                          | 195 ms: 1.03x faster                                                             |
| Geometric mean | (ref)                                                           | 1.32x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240926-pythonperf1_win32-x86-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_dna      | 117 ms                                                          | 119 ms: 1.02x slower                                                             |
| regex_v8       | 15.6 ms                                                         | 16.1 ms: 1.03x slower                                                            |
| regex_effbot   | 1.81 ms                                                         | 1.96 ms: 1.08x slower                                                            |
| Geometric mean | (ref)                                                           | 1.03x slower                                                                     |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240926-pythonperf1_win32-x86-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| xml_etree_generate   | 62.6 ms                                                         | 54.0 ms: 1.16x faster                                                            |
| unpickle_list        | 3.09 us                                                         | 2.75 us: 1.13x faster                                                            |
| tomli_loads          | 1.73 sec                                                        | 1.56 sec: 1.11x faster                                                           |
| xml_etree_process    | 45.0 ms                                                         | 40.6 ms: 1.11x faster                                                            |
| pickle_dict          | 21.7 us                                                         | 20.0 us: 1.08x faster                                                            |
| json_dumps           | 7.40 ms                                                         | 6.85 ms: 1.08x faster                                                            |
| xml_etree_iterparse  | 65.1 ms                                                         | 61.8 ms: 1.05x faster                                                            |
| pickle               | 8.42 us                                                         | 8.02 us: 1.05x faster                                                            |
| xml_etree_parse      | 109 ms                                                          | 104 ms: 1.05x faster                                                             |
| pickle_list          | 3.40 us                                                         | 3.38 us: 1.01x faster                                                            |
| json_loads           | 21.0 us                                                         | 21.2 us: 1.01x slower                                                            |
| unpickle_pure_python | 162 us                                                          | 168 us: 1.04x slower                                                             |
| pickle_pure_python   | 238 us                                                          | 255 us: 1.07x slower                                                             |
| Geometric mean       | (ref)                                                           | 1.05x faster                                                                     |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240926-pythonperf1_win32-x86-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 24.3 ms                                                         | 24.5 ms: 1.01x slower                                                            |
| python_startup_no_site | 19.9 ms                                                         | 20.2 ms: 1.01x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.01x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240926-pythonperf1_win32-x86-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 7.31 ms                                                         | 5.48 ms: 1.33x faster                                                            |
| django_template | 32.7 ms                                                         | 34.7 ms: 1.06x slower                                                            |
| genshi_text     | 22.4 ms                                                         | 24.5 ms: 1.09x slower                                                            |
| genshi_xml      | 49.5 ms                                                         | 56.6 ms: 1.14x slower                                                            |
| Geometric mean  | (ref)                                                           | 1.00x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240926-pythonperf1_win32-x86-savannahostrowski-jit_llvm_19-3.14.0a0-7f9fe5a |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| thrift                     | 10.1 ms                                                         | 788 us: 12.87x faster                                                            |
| coverage                   | 333 ms                                                          | 54.9 ms: 6.06x faster                                                            |
| deepcopy_memo              | 26.2 us                                                         | 15.5 us: 1.68x faster                                                            |
| nbody                      | 81.9 ms                                                         | 48.6 ms: 1.68x faster                                                            |
| spectral_norm              | 71.3 ms                                                         | 47.0 ms: 1.52x faster                                                            |
| scimark_sor                | 91.8 ms                                                         | 68.2 ms: 1.35x faster                                                            |
| float                      | 57.8 ms                                                         | 43.3 ms: 1.33x faster                                                            |
| mako                       | 7.31 ms                                                         | 5.48 ms: 1.33x faster                                                            |
| deepcopy                   | 307 us                                                          | 239 us: 1.28x faster                                                             |
| asyncio_tcp                | 842 ms                                                          | 668 ms: 1.26x faster                                                             |
| fannkuch                   | 293 ms                                                          | 235 ms: 1.24x faster                                                             |
| scimark_sparse_mat_mult    | 2.90 ms                                                         | 2.36 ms: 1.23x faster                                                            |
| crypto_pyaes               | 58.2 ms                                                         | 47.6 ms: 1.22x faster                                                            |
| scimark_fft                | 206 ms                                                          | 173 ms: 1.19x faster                                                             |
| xml_etree_generate         | 62.6 ms                                                         | 54.0 ms: 1.16x faster                                                            |
| deltablue                  | 2.41 ms                                                         | 2.12 ms: 1.13x faster                                                            |
| unpickle_list              | 3.09 us                                                         | 2.75 us: 1.13x faster                                                            |
| deepcopy_reduce            | 2.85 us                                                         | 2.56 us: 1.11x faster                                                            |
| async_tree_none            | 246 ms                                                          | 221 ms: 1.11x faster                                                             |
| tomli_loads                | 1.73 sec                                                        | 1.56 sec: 1.11x faster                                                           |
| xml_etree_process          | 45.0 ms                                                         | 40.6 ms: 1.11x faster                                                            |
| async_tree_memoization_tg  | 287 ms                                                          | 260 ms: 1.10x faster                                                             |
| telco                      | 6.67 ms                                                         | 6.08 ms: 1.10x faster                                                            |
| pyflate                    | 326 ms                                                          | 297 ms: 1.10x faster                                                             |
| pickle_dict                | 21.7 us                                                         | 20.0 us: 1.08x faster                                                            |
| json_dumps                 | 7.40 ms                                                         | 6.85 ms: 1.08x faster                                                            |
| async_tree_memoization     | 302 ms                                                          | 280 ms: 1.08x faster                                                             |
| pprint_safe_repr           | 644 ms                                                          | 599 ms: 1.07x faster                                                             |
| comprehensions             | 12.7 us                                                         | 11.9 us: 1.07x faster                                                            |
| async_tree_none_tg         | 219 ms                                                          | 204 ms: 1.07x faster                                                             |
| meteor_contest             | 77.0 ms                                                         | 72.2 ms: 1.07x faster                                                            |
| go                         | 111 ms                                                          | 104 ms: 1.07x faster                                                             |
| scimark_lu                 | 63.5 ms                                                         | 59.8 ms: 1.06x faster                                                            |
| pycparser                  | 869 ms                                                          | 818 ms: 1.06x faster                                                             |
| richards_super             | 38.0 ms                                                         | 35.9 ms: 1.06x faster                                                            |
| xml_etree_iterparse        | 65.1 ms                                                         | 61.8 ms: 1.05x faster                                                            |
| pickle                     | 8.42 us                                                         | 8.02 us: 1.05x faster                                                            |
| xml_etree_parse            | 109 ms                                                          | 104 ms: 1.05x faster                                                             |
| scimark_monte_carlo        | 50.3 ms                                                         | 48.2 ms: 1.04x faster                                                            |
| async_tree_cpu_io_mixed    | 494 ms                                                          | 474 ms: 1.04x faster                                                             |
| json                       | 4.27 ms                                                         | 4.11 ms: 1.04x faster                                                            |
| pidigits                   | 202 ms                                                          | 195 ms: 1.03x faster                                                             |
| pprint_pformat             | 1.30 sec                                                        | 1.26 sec: 1.03x faster                                                           |
| sqlite_synth               | 1.97 us                                                         | 1.91 us: 1.03x faster                                                            |
| html5lib                   | 48.3 ms                                                         | 47.0 ms: 1.03x faster                                                            |
| richards                   | 33.8 ms                                                         | 33.0 ms: 1.02x faster                                                            |
| pathlib                    | 89.4 ms                                                         | 87.5 ms: 1.02x faster                                                            |
| asyncio_tcp_ssl            | 17.4 sec                                                        | 17.0 sec: 1.02x faster                                                           |
| nqueens                    | 75.1 ms                                                         | 74.5 ms: 1.01x faster                                                            |
| pickle_list                | 3.40 us                                                         | 3.38 us: 1.01x faster                                                            |
| sqlglot_parse              | 1.05 ms                                                         | 1.06 ms: 1.01x slower                                                            |
| async_tree_cpu_io_mixed_tg | 464 ms                                                          | 467 ms: 1.01x slower                                                             |
| python_startup             | 24.3 ms                                                         | 24.5 ms: 1.01x slower                                                            |
| logging_silent             | 61.6 ns                                                         | 62.2 ns: 1.01x slower                                                            |
| logging_format             | 8.57 us                                                         | 8.65 us: 1.01x slower                                                            |
| json_loads                 | 21.0 us                                                         | 21.2 us: 1.01x slower                                                            |
| python_startup_no_site     | 19.9 ms                                                         | 20.2 ms: 1.01x slower                                                            |
| regex_dna                  | 117 ms                                                          | 119 ms: 1.02x slower                                                             |
| async_tree_io              | 537 ms                                                          | 548 ms: 1.02x slower                                                             |
| logging_simple             | 7.87 us                                                         | 8.05 us: 1.02x slower                                                            |
| generators                 | 22.1 ms                                                         | 22.7 ms: 1.02x slower                                                            |
| mdp                        | 1.67 sec                                                        | 1.72 sec: 1.03x slower                                                           |
| 2to3                       | 253 ms                                                          | 260 ms: 1.03x slower                                                             |
| regex_v8                   | 15.6 ms                                                         | 16.1 ms: 1.03x slower                                                            |
| sympy_str                  | 215 ms                                                          | 222 ms: 1.03x slower                                                             |
| unpickle_pure_python       | 162 us                                                          | 168 us: 1.04x slower                                                             |
| async_tree_io_tg           | 509 ms                                                          | 530 ms: 1.04x slower                                                             |
| bench_mp_pool              | 74.3 ms                                                         | 77.5 ms: 1.04x slower                                                            |
| sqlglot_normalize          | 220 ms                                                          | 230 ms: 1.04x slower                                                             |
| sympy_sum                  | 108 ms                                                          | 114 ms: 1.05x slower                                                             |
| chaos                      | 51.2 ms                                                         | 53.9 ms: 1.05x slower                                                            |
| sqlglot_transpile          | 1.29 ms                                                         | 1.36 ms: 1.05x slower                                                            |
| create_gc_cycles           | 713 us                                                          | 754 us: 1.06x slower                                                             |
| tornado_http               | 104 ms                                                          | 110 ms: 1.06x slower                                                             |
| django_template            | 32.7 ms                                                         | 34.7 ms: 1.06x slower                                                            |
| unpack_sequence            | 42.9 ns                                                         | 45.6 ns: 1.06x slower                                                            |
| sympy_expand               | 375 ms                                                          | 400 ms: 1.07x slower                                                             |
| hexiom                     | 4.64 ms                                                         | 4.96 ms: 1.07x slower                                                            |
| pickle_pure_python         | 238 us                                                          | 255 us: 1.07x slower                                                             |
| regex_effbot               | 1.81 ms                                                         | 1.96 ms: 1.08x slower                                                            |
| typing_runtime_protocols   | 136 us                                                          | 148 us: 1.08x slower                                                             |
| genshi_text                | 22.4 ms                                                         | 24.5 ms: 1.09x slower                                                            |
| docutils                   | 1.82 sec                                                        | 2.00 sec: 1.10x slower                                                           |
| sympy_integrate            | 15.2 ms                                                         | 16.8 ms: 1.11x slower                                                            |
| sqlglot_optimize           | 42.5 ms                                                         | 46.9 ms: 1.11x slower                                                            |
| genshi_xml                 | 49.5 ms                                                         | 56.6 ms: 1.14x slower                                                            |
| coroutines                 | 15.7 ms                                                         | 18.2 ms: 1.16x slower                                                            |
| async_generators           | 274 ms                                                          | 322 ms: 1.18x slower                                                             |
| pylint                     | 225 ms                                                          | 271 ms: 1.20x slower                                                             |
| raytrace                   | 205 ms                                                          | 249 ms: 1.21x slower                                                             |
| Geometric mean             | (ref)                                                           | 1.09x faster                                                                     |

Benchmark hidden because not significant (5): bench_thread_pool, gc_traversal, unpickle, dulwich_log, regex_compile
Ignored benchmarks (2) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, flaskblogging

# HPT report

- Reliability score: 93.56% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown