# Results vs. base

- fork: mdboom
- ref: pysequence_tuple
- machine: windows-x86
- commit hash: 3b5fdc8
- commit date: 2024-09-11
- overall geometric mean: 1.002x faster
- HPT reliability: 65.36%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240911-pythonperf1_win32-x86-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b | bm-20240911-pythonperf1_win32-x86-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:------------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| html5lib       | 44.1 ms                                                                        | 45.7 ms: 1.04x slower                                                      |
| Geometric mean | (ref)                                                                          | 1.01x slower                                                               |

Benchmark hidden because not significant (3): 2to3, docutils, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240911-pythonperf1_win32-x86-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b | bm-20240911-pythonperf1_win32-x86-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------------------|:------------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_generators           | 305 ms                                                                         | 294 ms: 1.04x faster                                                       |
| coroutines                 | 18.7 ms                                                                        | 18.3 ms: 1.02x faster                                                      |
| async_tree_memoization     | 271 ms                                                                         | 278 ms: 1.03x slower                                                       |
| async_tree_cpu_io_mixed_tg | 457 ms                                                                         | 473 ms: 1.03x slower                                                       |
| async_tree_memoization_tg  | 250 ms                                                                         | 259 ms: 1.04x slower                                                       |
| async_tree_none            | 218 ms                                                                         | 226 ms: 1.04x slower                                                       |
| async_tree_io_tg           | 510 ms                                                                         | 531 ms: 1.04x slower                                                       |
| async_tree_io              | 529 ms                                                                         | 551 ms: 1.04x slower                                                       |
| async_tree_cpu_io_mixed    | 464 ms                                                                         | 488 ms: 1.05x slower                                                       |
| async_tree_none_tg         | 198 ms                                                                         | 208 ms: 1.05x slower                                                       |
| Geometric mean             | (ref)                                                                          | 1.02x slower                                                               |

Benchmark hidden because not significant (2): asyncio_tcp, asyncio_tcp_ssl

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240911-pythonperf1_win32-x86-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b | bm-20240911-pythonperf1_win32-x86-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:------------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 62.2 ms                                                                        | 61.0 ms: 1.02x faster                                                      |
| pidigits       | 196 ms                                                                         | 197 ms: 1.00x slower                                                       |
| Geometric mean | (ref)                                                                          | 1.01x faster                                                               |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240911-pythonperf1_win32-x86-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b | bm-20240911-pythonperf1_win32-x86-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:------------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 119 ms                                                                         | 117 ms: 1.02x faster                                                       |
| regex_effbot   | 1.92 ms                                                                        | 1.91 ms: 1.01x faster                                                      |
| regex_compile  | 108 ms                                                                         | 107 ms: 1.01x faster                                                       |
| regex_v8       | 16.3 ms                                                                        | 16.4 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                                          | 1.01x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20240911-pythonperf1_win32-x86-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b | bm-20240911-pythonperf1_win32-x86-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|--------------------|:------------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle_list        | 3.65 us                                                                        | 3.34 us: 1.09x faster                                                      |
| unpickle_list      | 3.10 us                                                                        | 2.94 us: 1.06x faster                                                      |
| pickle_dict        | 21.0 us                                                                        | 20.3 us: 1.04x faster                                                      |
| pickle_pure_python | 262 us                                                                         | 256 us: 1.02x faster                                                       |
| tomli_loads        | 1.89 sec                                                                       | 1.85 sec: 1.02x faster                                                     |
| xml_etree_parse    | 108 ms                                                                         | 107 ms: 1.01x faster                                                       |
| pickle             | 7.99 us                                                                        | 7.94 us: 1.01x faster                                                      |
| json_dumps         | 7.62 ms                                                                        | 7.70 ms: 1.01x slower                                                      |
| json_loads         | 20.6 us                                                                        | 20.9 us: 1.02x slower                                                      |
| xml_etree_generate | 68.2 ms                                                                        | 69.2 ms: 1.02x slower                                                      |
| xml_etree_process  | 49.8 ms                                                                        | 50.7 ms: 1.02x slower                                                      |
| unpickle           | 10.3 us                                                                        | 10.5 us: 1.02x slower                                                      |
| Geometric mean     | (ref)                                                                          | 1.01x faster                                                               |

Benchmark hidden because not significant (2): xml_etree_iterparse, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240911-pythonperf1_win32-x86-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b | bm-20240911-pythonperf1_win32-x86-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|------------------------|:------------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 19.8 ms                                                                        | 19.4 ms: 1.02x faster                                                      |
| python_startup         | 24.0 ms                                                                        | 23.6 ms: 1.02x faster                                                      |
| Geometric mean         | (ref)                                                                          | 1.02x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240911-pythonperf1_win32-x86-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b | bm-20240911-pythonperf1_win32-x86-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|-----------------|:------------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 8.18 ms                                                                        | 8.08 ms: 1.01x faster                                                      |
| django_template | 32.6 ms                                                                        | 32.4 ms: 1.01x faster                                                      |
| Geometric mean  | (ref)                                                                          | 1.00x faster                                                               |

Benchmark hidden because not significant (2): genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20240911-pythonperf1_win32-x86-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b | bm-20240911-pythonperf1_win32-x86-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------------------|:------------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle_list                | 3.65 us                                                                        | 3.34 us: 1.09x faster                                                      |
| scimark_sor                | 104 ms                                                                         | 97.5 ms: 1.07x faster                                                      |
| unpickle_list              | 3.10 us                                                                        | 2.94 us: 1.06x faster                                                      |
| unpack_sequence            | 49.3 ns                                                                        | 46.6 ns: 1.06x faster                                                      |
| scimark_monte_carlo        | 57.5 ms                                                                        | 54.8 ms: 1.05x faster                                                      |
| async_generators           | 305 ms                                                                         | 294 ms: 1.04x faster                                                       |
| chaos                      | 53.7 ms                                                                        | 51.8 ms: 1.04x faster                                                      |
| raytrace                   | 235 ms                                                                         | 227 ms: 1.04x faster                                                       |
| pickle_dict                | 21.0 us                                                                        | 20.3 us: 1.04x faster                                                      |
| fannkuch                   | 338 ms                                                                         | 328 ms: 1.03x faster                                                       |
| coverage                   | 54.7 ms                                                                        | 53.1 ms: 1.03x faster                                                      |
| richards_super             | 45.0 ms                                                                        | 43.8 ms: 1.03x faster                                                      |
| telco                      | 6.37 ms                                                                        | 6.19 ms: 1.03x faster                                                      |
| logging_format             | 8.77 us                                                                        | 8.55 us: 1.03x faster                                                      |
| bench_thread_pool          | 1.02 ms                                                                        | 995 us: 1.03x faster                                                       |
| sqlglot_transpile          | 1.35 ms                                                                        | 1.31 ms: 1.02x faster                                                      |
| typing_runtime_protocols   | 145 us                                                                         | 141 us: 1.02x faster                                                       |
| sqlglot_parse              | 1.08 ms                                                                        | 1.06 ms: 1.02x faster                                                      |
| python_startup_no_site     | 19.8 ms                                                                        | 19.4 ms: 1.02x faster                                                      |
| crypto_pyaes               | 58.1 ms                                                                        | 56.8 ms: 1.02x faster                                                      |
| coroutines                 | 18.7 ms                                                                        | 18.3 ms: 1.02x faster                                                      |
| pickle_pure_python         | 262 us                                                                         | 256 us: 1.02x faster                                                       |
| scimark_fft                | 236 ms                                                                         | 231 ms: 1.02x faster                                                       |
| nqueens                    | 74.9 ms                                                                        | 73.3 ms: 1.02x faster                                                      |
| dulwich_log                | 50.8 ms                                                                        | 49.8 ms: 1.02x faster                                                      |
| float                      | 62.2 ms                                                                        | 61.0 ms: 1.02x faster                                                      |
| logging_simple             | 8.04 us                                                                        | 7.89 us: 1.02x faster                                                      |
| deepcopy_reduce            | 2.54 us                                                                        | 2.49 us: 1.02x faster                                                      |
| tomli_loads                | 1.89 sec                                                                       | 1.85 sec: 1.02x faster                                                     |
| regex_dna                  | 119 ms                                                                         | 117 ms: 1.02x faster                                                       |
| python_startup             | 24.0 ms                                                                        | 23.6 ms: 1.02x faster                                                      |
| meteor_contest             | 81.9 ms                                                                        | 80.5 ms: 1.02x faster                                                      |
| deepcopy                   | 246 us                                                                         | 242 us: 1.02x faster                                                       |
| go                         | 104 ms                                                                         | 103 ms: 1.01x faster                                                       |
| mako                       | 8.18 ms                                                                        | 8.08 ms: 1.01x faster                                                      |
| xml_etree_parse            | 108 ms                                                                         | 107 ms: 1.01x faster                                                       |
| scimark_sparse_mat_mult    | 3.08 ms                                                                        | 3.04 ms: 1.01x faster                                                      |
| deepcopy_memo              | 22.3 us                                                                        | 22.0 us: 1.01x faster                                                      |
| deltablue                  | 2.72 ms                                                                        | 2.70 ms: 1.01x faster                                                      |
| comprehensions             | 14.0 us                                                                        | 13.9 us: 1.01x faster                                                      |
| regex_effbot               | 1.92 ms                                                                        | 1.91 ms: 1.01x faster                                                      |
| regex_compile              | 108 ms                                                                         | 107 ms: 1.01x faster                                                       |
| pickle                     | 7.99 us                                                                        | 7.94 us: 1.01x faster                                                      |
| django_template            | 32.6 ms                                                                        | 32.4 ms: 1.01x faster                                                      |
| spectral_norm              | 76.1 ms                                                                        | 75.7 ms: 1.01x faster                                                      |
| hexiom                     | 5.15 ms                                                                        | 5.13 ms: 1.00x faster                                                      |
| pprint_pformat             | 1.35 sec                                                                       | 1.36 sec: 1.00x slower                                                     |
| pidigits                   | 196 ms                                                                         | 197 ms: 1.00x slower                                                       |
| scimark_lu                 | 68.1 ms                                                                        | 68.5 ms: 1.01x slower                                                      |
| regex_v8                   | 16.3 ms                                                                        | 16.4 ms: 1.01x slower                                                      |
| pprint_safe_repr           | 659 ms                                                                         | 666 ms: 1.01x slower                                                       |
| json_dumps                 | 7.62 ms                                                                        | 7.70 ms: 1.01x slower                                                      |
| mdp                        | 1.70 sec                                                                       | 1.72 sec: 1.01x slower                                                     |
| create_gc_cycles           | 731 us                                                                         | 741 us: 1.01x slower                                                       |
| json_loads                 | 20.6 us                                                                        | 20.9 us: 1.02x slower                                                      |
| xml_etree_generate         | 68.2 ms                                                                        | 69.2 ms: 1.02x slower                                                      |
| gc_traversal               | 1.39 ms                                                                        | 1.42 ms: 1.02x slower                                                      |
| xml_etree_process          | 49.8 ms                                                                        | 50.7 ms: 1.02x slower                                                      |
| pycparser                  | 864 ms                                                                         | 882 ms: 1.02x slower                                                       |
| bench_mp_pool              | 69.9 ms                                                                        | 71.5 ms: 1.02x slower                                                      |
| generators                 | 26.2 ms                                                                        | 26.8 ms: 1.02x slower                                                      |
| unpickle                   | 10.3 us                                                                        | 10.5 us: 1.02x slower                                                      |
| async_tree_memoization     | 271 ms                                                                         | 278 ms: 1.03x slower                                                       |
| sqlglot_optimize           | 43.2 ms                                                                        | 44.4 ms: 1.03x slower                                                      |
| async_tree_cpu_io_mixed_tg | 457 ms                                                                         | 473 ms: 1.03x slower                                                       |
| thrift                     | 737 us                                                                         | 763 us: 1.04x slower                                                       |
| async_tree_memoization_tg  | 250 ms                                                                         | 259 ms: 1.04x slower                                                       |
| html5lib                   | 44.1 ms                                                                        | 45.7 ms: 1.04x slower                                                      |
| async_tree_none            | 218 ms                                                                         | 226 ms: 1.04x slower                                                       |
| async_tree_io_tg           | 510 ms                                                                         | 531 ms: 1.04x slower                                                       |
| async_tree_io              | 529 ms                                                                         | 551 ms: 1.04x slower                                                       |
| sqlglot_normalize          | 226 ms                                                                         | 236 ms: 1.05x slower                                                       |
| async_tree_cpu_io_mixed    | 464 ms                                                                         | 488 ms: 1.05x slower                                                       |
| async_tree_none_tg         | 198 ms                                                                         | 208 ms: 1.05x slower                                                       |
| Geometric mean             | (ref)                                                                          | 1.00x faster                                                               |

Benchmark hidden because not significant (21): asyncio_tcp, logging_silent, tornado_http, nbody, docutils, asyncio_tcp_ssl, sympy_sum, xml_etree_iterparse, 2to3, pylint, pyflate, unpickle_pure_python, sympy_expand, genshi_text, sympy_str, genshi_xml, sqlite_synth, sympy_integrate, pathlib, richards, json

- Geometric mean (including insignificant results): 1.002x faster
# HPT report

- Reliability score: 65.36% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown