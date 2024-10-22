# Results vs. 3.13.0

- fork: python
- ref: 006b53a42f72be83ecdf
- machine: windows-x86
- commit hash: 006b53a
- commit date: 2024-07-08
- overall geometric mean: 1.11x faster
- HPT reliability: 99.26%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240708-pythonperf1_win32-x86-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| docutils       | 1.82 sec                                                        | 1.93 sec: 1.06x slower                                                         |
| html5lib       | 48.3 ms                                                         | 46.8 ms: 1.03x faster                                                          |
| tornado_http   | 104 ms                                                          | 98.3 ms: 1.06x faster                                                          |
| Geometric mean | (ref)                                                           | 1.01x faster                                                                   |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240708-pythonperf1_win32-x86-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|---------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| asyncio_tcp               | 842 ms                                                          | 613 ms: 1.37x faster                                                           |
| async_tree_memoization_tg | 287 ms                                                          | 248 ms: 1.16x faster                                                           |
| async_tree_none_tg        | 219 ms                                                          | 195 ms: 1.12x faster                                                           |
| async_tree_none           | 246 ms                                                          | 219 ms: 1.12x faster                                                           |
| async_tree_memoization    | 302 ms                                                          | 272 ms: 1.11x faster                                                           |
| async_tree_cpu_io_mixed   | 494 ms                                                          | 470 ms: 1.05x faster                                                           |
| asyncio_tcp_ssl           | 17.4 sec                                                        | 16.8 sec: 1.03x faster                                                         |
| async_tree_io_tg          | 509 ms                                                          | 503 ms: 1.01x faster                                                           |
| coroutines                | 15.7 ms                                                         | 17.9 ms: 1.14x slower                                                          |
| async_generators          | 274 ms                                                          | 317 ms: 1.16x slower                                                           |
| Geometric mean            | (ref)                                                           | 1.05x faster                                                                   |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240708-pythonperf1_win32-x86-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 81.9 ms                                                         | 55.7 ms: 1.47x faster                                                          |
| float          | 57.8 ms                                                         | 44.1 ms: 1.31x faster                                                          |
| pidigits       | 202 ms                                                          | 195 ms: 1.03x faster                                                           |
| Geometric mean | (ref)                                                           | 1.26x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240708-pythonperf1_win32-x86-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 103 ms                                                          | 95.0 ms: 1.09x faster                                                          |
| regex_v8       | 15.6 ms                                                         | 15.8 ms: 1.01x slower                                                          |
| regex_effbot   | 1.81 ms                                                         | 1.90 ms: 1.05x slower                                                          |
| regex_dna      | 117 ms                                                          | 123 ms: 1.05x slower                                                           |
| Geometric mean | (ref)                                                           | 1.01x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240708-pythonperf1_win32-x86-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| tomli_loads          | 1.73 sec                                                        | 1.48 sec: 1.17x faster                                                         |
| pickle_pure_python   | 238 us                                                          | 212 us: 1.12x faster                                                           |
| unpickle_pure_python | 162 us                                                          | 148 us: 1.09x faster                                                           |
| xml_etree_iterparse  | 65.1 ms                                                         | 61.8 ms: 1.05x faster                                                          |
| xml_etree_parse      | 109 ms                                                          | 104 ms: 1.04x faster                                                           |
| json_dumps           | 7.40 ms                                                         | 7.14 ms: 1.04x faster                                                          |
| xml_etree_generate   | 62.6 ms                                                         | 60.9 ms: 1.03x faster                                                          |
| xml_etree_process    | 45.0 ms                                                         | 44.0 ms: 1.02x faster                                                          |
| json_loads           | 21.0 us                                                         | 21.3 us: 1.02x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.06x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240708-pythonperf1_win32-x86-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 24.3 ms                                                         | 23.2 ms: 1.05x faster                                                          |
| python_startup_no_site | 19.9 ms                                                         | 19.3 ms: 1.04x faster                                                          |
| Geometric mean         | (ref)                                                           | 1.04x faster                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240708-pythonperf1_win32-x86-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako           | 7.31 ms                                                         | 5.44 ms: 1.34x faster                                                          |
| genshi_text    | 22.4 ms                                                         | 22.8 ms: 1.01x slower                                                          |
| genshi_xml     | 49.5 ms                                                         | 53.2 ms: 1.07x slower                                                          |
| Geometric mean | (ref)                                                           | 1.05x faster                                                                   |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240708-pythonperf1_win32-x86-python-006b53a42f72be83ecdf-3.14.0a0-006b53a |
|---------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                    | 10.1 ms                                                         | 747 us: 13.59x faster                                                          |
| coverage                  | 333 ms                                                          | 51.3 ms: 6.48x faster                                                          |
| deepcopy_memo             | 26.2 us                                                         | 15.5 us: 1.69x faster                                                          |
| spectral_norm             | 71.3 ms                                                         | 47.3 ms: 1.51x faster                                                          |
| nbody                     | 81.9 ms                                                         | 55.7 ms: 1.47x faster                                                          |
| asyncio_tcp               | 842 ms                                                          | 613 ms: 1.37x faster                                                           |
| mako                      | 7.31 ms                                                         | 5.44 ms: 1.34x faster                                                          |
| float                     | 57.8 ms                                                         | 44.1 ms: 1.31x faster                                                          |
| fannkuch                  | 293 ms                                                          | 226 ms: 1.30x faster                                                           |
| deepcopy                  | 307 us                                                          | 239 us: 1.28x faster                                                           |
| scimark_fft               | 206 ms                                                          | 165 ms: 1.25x faster                                                           |
| scimark_sparse_mat_mult   | 2.90 ms                                                         | 2.36 ms: 1.23x faster                                                          |
| scimark_monte_carlo       | 50.3 ms                                                         | 41.2 ms: 1.22x faster                                                          |
| deepcopy_reduce           | 2.85 us                                                         | 2.37 us: 1.20x faster                                                          |
| crypto_pyaes              | 58.2 ms                                                         | 49.2 ms: 1.18x faster                                                          |
| pyflate                   | 326 ms                                                          | 278 ms: 1.17x faster                                                           |
| tomli_loads               | 1.73 sec                                                        | 1.48 sec: 1.17x faster                                                         |
| pprint_safe_repr          | 644 ms                                                          | 552 ms: 1.17x faster                                                           |
| async_tree_memoization_tg | 287 ms                                                          | 248 ms: 1.16x faster                                                           |
| pprint_pformat            | 1.30 sec                                                        | 1.14 sec: 1.14x faster                                                         |
| telco                     | 6.67 ms                                                         | 5.92 ms: 1.13x faster                                                          |
| async_tree_none_tg        | 219 ms                                                          | 195 ms: 1.12x faster                                                           |
| async_tree_none           | 246 ms                                                          | 219 ms: 1.12x faster                                                           |
| comprehensions            | 12.7 us                                                         | 11.4 us: 1.12x faster                                                          |
| pickle_pure_python        | 238 us                                                          | 212 us: 1.12x faster                                                           |
| async_tree_memoization    | 302 ms                                                          | 272 ms: 1.11x faster                                                           |
| sqlglot_parse             | 1.05 ms                                                         | 958 us: 1.10x faster                                                           |
| unpickle_pure_python      | 162 us                                                          | 148 us: 1.09x faster                                                           |
| regex_compile             | 103 ms                                                          | 95.0 ms: 1.09x faster                                                          |
| pathlib                   | 89.4 ms                                                         | 83.3 ms: 1.07x faster                                                          |
| tornado_http              | 104 ms                                                          | 98.3 ms: 1.06x faster                                                          |
| sqlglot_transpile         | 1.29 ms                                                         | 1.22 ms: 1.06x faster                                                          |
| logging_format            | 8.57 us                                                         | 8.13 us: 1.05x faster                                                          |
| xml_etree_iterparse       | 65.1 ms                                                         | 61.8 ms: 1.05x faster                                                          |
| async_tree_cpu_io_mixed   | 494 ms                                                          | 470 ms: 1.05x faster                                                           |
| logging_silent            | 61.6 ns                                                         | 58.6 ns: 1.05x faster                                                          |
| python_startup            | 24.3 ms                                                         | 23.2 ms: 1.05x faster                                                          |
| xml_etree_parse           | 109 ms                                                          | 104 ms: 1.04x faster                                                           |
| richards                  | 33.8 ms                                                         | 32.4 ms: 1.04x faster                                                          |
| bench_thread_pool         | 1.02 ms                                                         | 978 us: 1.04x faster                                                           |
| logging_simple            | 7.87 us                                                         | 7.55 us: 1.04x faster                                                          |
| json_dumps                | 7.40 ms                                                         | 7.14 ms: 1.04x faster                                                          |
| python_startup_no_site    | 19.9 ms                                                         | 19.3 ms: 1.04x faster                                                          |
| pidigits                  | 202 ms                                                          | 195 ms: 1.03x faster                                                           |
| meteor_contest            | 77.0 ms                                                         | 74.6 ms: 1.03x faster                                                          |
| asyncio_tcp_ssl           | 17.4 sec                                                        | 16.8 sec: 1.03x faster                                                         |
| html5lib                  | 48.3 ms                                                         | 46.8 ms: 1.03x faster                                                          |
| pycparser                 | 869 ms                                                          | 844 ms: 1.03x faster                                                           |
| xml_etree_generate        | 62.6 ms                                                         | 60.9 ms: 1.03x faster                                                          |
| nqueens                   | 75.1 ms                                                         | 73.2 ms: 1.03x faster                                                          |
| xml_etree_process         | 45.0 ms                                                         | 44.0 ms: 1.02x faster                                                          |
| async_tree_io_tg          | 509 ms                                                          | 503 ms: 1.01x faster                                                           |
| hexiom                    | 4.64 ms                                                         | 4.60 ms: 1.01x faster                                                          |
| bench_mp_pool             | 74.3 ms                                                         | 73.7 ms: 1.01x faster                                                          |
| mdp                       | 1.67 sec                                                        | 1.66 sec: 1.01x faster                                                         |
| go                        | 111 ms                                                          | 112 ms: 1.01x slower                                                           |
| sympy_sum                 | 108 ms                                                          | 109 ms: 1.01x slower                                                           |
| regex_v8                  | 15.6 ms                                                         | 15.8 ms: 1.01x slower                                                          |
| genshi_text               | 22.4 ms                                                         | 22.8 ms: 1.01x slower                                                          |
| json_loads                | 21.0 us                                                         | 21.3 us: 1.02x slower                                                          |
| sympy_str                 | 215 ms                                                          | 219 ms: 1.02x slower                                                           |
| richards_super            | 38.0 ms                                                         | 38.9 ms: 1.02x slower                                                          |
| sqlglot_optimize          | 42.5 ms                                                         | 44.1 ms: 1.04x slower                                                          |
| sympy_expand              | 375 ms                                                          | 392 ms: 1.05x slower                                                           |
| regex_effbot              | 1.81 ms                                                         | 1.90 ms: 1.05x slower                                                          |
| sympy_integrate           | 15.2 ms                                                         | 15.9 ms: 1.05x slower                                                          |
| regex_dna                 | 117 ms                                                          | 123 ms: 1.05x slower                                                           |
| create_gc_cycles          | 713 us                                                          | 751 us: 1.05x slower                                                           |
| chaos                     | 51.2 ms                                                         | 54.0 ms: 1.05x slower                                                          |
| typing_runtime_protocols  | 136 us                                                          | 145 us: 1.06x slower                                                           |
| docutils                  | 1.82 sec                                                        | 1.93 sec: 1.06x slower                                                         |
| genshi_xml                | 49.5 ms                                                         | 53.2 ms: 1.07x slower                                                          |
| pylint                    | 225 ms                                                          | 242 ms: 1.08x slower                                                           |
| sqlglot_normalize         | 220 ms                                                          | 241 ms: 1.09x slower                                                           |
| scimark_sor               | 91.8 ms                                                         | 102 ms: 1.11x slower                                                           |
| deltablue                 | 2.41 ms                                                         | 2.73 ms: 1.14x slower                                                          |
| raytrace                  | 205 ms                                                          | 235 ms: 1.14x slower                                                           |
| coroutines                | 15.7 ms                                                         | 17.9 ms: 1.14x slower                                                          |
| async_generators          | 274 ms                                                          | 317 ms: 1.16x slower                                                           |
| scimark_lu                | 63.5 ms                                                         | 77.9 ms: 1.23x slower                                                          |
| generators                | 22.1 ms                                                         | 27.7 ms: 1.26x slower                                                          |
| Geometric mean            | (ref)                                                           | 1.11x faster                                                                   |

Benchmark hidden because not significant (6): json, 2to3, async_tree_cpu_io_mixed_tg, django_template, gc_traversal, async_tree_io
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, dulwich_log, flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 99.26% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown