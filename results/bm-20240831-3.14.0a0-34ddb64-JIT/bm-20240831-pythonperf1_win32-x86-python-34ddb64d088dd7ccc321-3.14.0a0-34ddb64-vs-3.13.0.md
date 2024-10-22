# Results vs. 3.13.0

- fork: python
- ref: 34ddb64d088dd7ccc321
- machine: windows-x86
- commit hash: 34ddb64
- commit date: 2024-08-31
- overall geometric mean: 1.10x faster
- HPT reliability: 96.15%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf1_win32-x86-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 253 ms                                                          | 263 ms: 1.04x slower                                                           |
| docutils       | 1.82 sec                                                        | 2.00 sec: 1.10x slower                                                         |
| html5lib       | 48.3 ms                                                         | 47.5 ms: 1.02x faster                                                          |
| tornado_http   | 104 ms                                                          | 108 ms: 1.04x slower                                                           |
| Geometric mean | (ref)                                                           | 1.04x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf1_win32-x86-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|---------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| asyncio_tcp               | 842 ms                                                          | 687 ms: 1.23x faster                                                           |
| async_tree_none           | 246 ms                                                          | 215 ms: 1.15x faster                                                           |
| async_tree_memoization_tg | 287 ms                                                          | 251 ms: 1.14x faster                                                           |
| async_tree_memoization    | 302 ms                                                          | 274 ms: 1.10x faster                                                           |
| async_tree_none_tg        | 219 ms                                                          | 202 ms: 1.08x faster                                                           |
| async_tree_cpu_io_mixed   | 494 ms                                                          | 473 ms: 1.05x faster                                                           |
| asyncio_tcp_ssl           | 17.4 sec                                                        | 17.0 sec: 1.02x faster                                                         |
| async_generators          | 274 ms                                                          | 309 ms: 1.13x slower                                                           |
| coroutines                | 15.7 ms                                                         | 17.9 ms: 1.14x slower                                                          |
| Geometric mean            | (ref)                                                           | 1.04x faster                                                                   |

Benchmark hidden because not significant (3): async_tree_io, async_tree_cpu_io_mixed_tg, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf1_win32-x86-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 81.9 ms                                                         | 47.8 ms: 1.71x faster                                                          |
| float          | 57.8 ms                                                         | 43.9 ms: 1.32x faster                                                          |
| pidigits       | 202 ms                                                          | 195 ms: 1.03x faster                                                           |
| Geometric mean | (ref)                                                           | 1.33x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf1_win32-x86-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 103 ms                                                          | 102 ms: 1.02x faster                                                           |
| regex_v8       | 15.6 ms                                                         | 15.8 ms: 1.01x slower                                                          |
| regex_dna      | 117 ms                                                          | 122 ms: 1.05x slower                                                           |
| regex_effbot   | 1.81 ms                                                         | 1.95 ms: 1.08x slower                                                          |
| Geometric mean | (ref)                                                           | 1.03x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf1_win32-x86-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|---------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| tomli_loads         | 1.73 sec                                                        | 1.48 sec: 1.17x faster                                                         |
| xml_etree_generate  | 62.6 ms                                                         | 54.5 ms: 1.15x faster                                                          |
| xml_etree_process   | 45.0 ms                                                         | 41.4 ms: 1.09x faster                                                          |
| json_dumps          | 7.40 ms                                                         | 6.86 ms: 1.08x faster                                                          |
| xml_etree_parse     | 109 ms                                                          | 104 ms: 1.04x faster                                                           |
| xml_etree_iterparse | 65.1 ms                                                         | 62.5 ms: 1.04x faster                                                          |
| pickle_pure_python  | 238 us                                                          | 233 us: 1.02x faster                                                           |
| Geometric mean      | (ref)                                                           | 1.06x faster                                                                   |

Benchmark hidden because not significant (2): json_loads, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf1_win32-x86-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 24.3 ms                                                         | 24.9 ms: 1.03x slower                                                          |
| python_startup_no_site | 19.9 ms                                                         | 21.0 ms: 1.05x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.04x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf1_win32-x86-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 7.31 ms                                                         | 5.60 ms: 1.30x faster                                                          |
| django_template | 32.7 ms                                                         | 33.6 ms: 1.03x slower                                                          |
| genshi_text     | 22.4 ms                                                         | 24.9 ms: 1.11x slower                                                          |
| genshi_xml      | 49.5 ms                                                         | 56.4 ms: 1.14x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.00x faster                                                                   |

All benchmarks:
===============

| Benchmark                 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240831-pythonperf1_win32-x86-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|---------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                    | 10.1 ms                                                         | 788 us: 12.88x faster                                                          |
| coverage                  | 333 ms                                                          | 51.6 ms: 6.46x faster                                                          |
| deepcopy_memo             | 26.2 us                                                         | 15.0 us: 1.75x faster                                                          |
| nbody                     | 81.9 ms                                                         | 47.8 ms: 1.71x faster                                                          |
| spectral_norm             | 71.3 ms                                                         | 46.3 ms: 1.54x faster                                                          |
| deepcopy                  | 307 us                                                          | 230 us: 1.33x faster                                                           |
| scimark_sor               | 91.8 ms                                                         | 69.4 ms: 1.32x faster                                                          |
| float                     | 57.8 ms                                                         | 43.9 ms: 1.32x faster                                                          |
| mako                      | 7.31 ms                                                         | 5.60 ms: 1.30x faster                                                          |
| fannkuch                  | 293 ms                                                          | 237 ms: 1.23x faster                                                           |
| scimark_fft               | 206 ms                                                          | 168 ms: 1.23x faster                                                           |
| asyncio_tcp               | 842 ms                                                          | 687 ms: 1.23x faster                                                           |
| crypto_pyaes              | 58.2 ms                                                         | 48.2 ms: 1.21x faster                                                          |
| deltablue                 | 2.41 ms                                                         | 2.06 ms: 1.17x faster                                                          |
| pyflate                   | 326 ms                                                          | 279 ms: 1.17x faster                                                           |
| tomli_loads               | 1.73 sec                                                        | 1.48 sec: 1.17x faster                                                         |
| xml_etree_generate        | 62.6 ms                                                         | 54.5 ms: 1.15x faster                                                          |
| async_tree_none           | 246 ms                                                          | 215 ms: 1.15x faster                                                           |
| async_tree_memoization_tg | 287 ms                                                          | 251 ms: 1.14x faster                                                           |
| deepcopy_reduce           | 2.85 us                                                         | 2.51 us: 1.14x faster                                                          |
| async_tree_memoization    | 302 ms                                                          | 274 ms: 1.10x faster                                                           |
| scimark_sparse_mat_mult   | 2.90 ms                                                         | 2.64 ms: 1.10x faster                                                          |
| go                        | 111 ms                                                          | 102 ms: 1.09x faster                                                           |
| xml_etree_process         | 45.0 ms                                                         | 41.4 ms: 1.09x faster                                                          |
| telco                     | 6.67 ms                                                         | 6.14 ms: 1.09x faster                                                          |
| async_tree_none_tg        | 219 ms                                                          | 202 ms: 1.08x faster                                                           |
| pprint_safe_repr          | 644 ms                                                          | 596 ms: 1.08x faster                                                           |
| comprehensions            | 12.7 us                                                         | 11.8 us: 1.08x faster                                                          |
| json_dumps                | 7.40 ms                                                         | 6.86 ms: 1.08x faster                                                          |
| richards_super            | 38.0 ms                                                         | 35.5 ms: 1.07x faster                                                          |
| scimark_lu                | 63.5 ms                                                         | 59.5 ms: 1.07x faster                                                          |
| pycparser                 | 869 ms                                                          | 819 ms: 1.06x faster                                                           |
| meteor_contest            | 77.0 ms                                                         | 73.2 ms: 1.05x faster                                                          |
| pprint_pformat            | 1.30 sec                                                        | 1.24 sec: 1.05x faster                                                         |
| async_tree_cpu_io_mixed   | 494 ms                                                          | 473 ms: 1.05x faster                                                           |
| xml_etree_parse           | 109 ms                                                          | 104 ms: 1.04x faster                                                           |
| richards                  | 33.8 ms                                                         | 32.4 ms: 1.04x faster                                                          |
| xml_etree_iterparse       | 65.1 ms                                                         | 62.5 ms: 1.04x faster                                                          |
| logging_silent            | 61.6 ns                                                         | 59.4 ns: 1.04x faster                                                          |
| pidigits                  | 202 ms                                                          | 195 ms: 1.03x faster                                                           |
| pathlib                   | 89.4 ms                                                         | 86.8 ms: 1.03x faster                                                          |
| json                      | 4.27 ms                                                         | 4.14 ms: 1.03x faster                                                          |
| logging_format            | 8.57 us                                                         | 8.34 us: 1.03x faster                                                          |
| pickle_pure_python        | 238 us                                                          | 233 us: 1.02x faster                                                           |
| asyncio_tcp_ssl           | 17.4 sec                                                        | 17.0 sec: 1.02x faster                                                         |
| logging_simple            | 7.87 us                                                         | 7.71 us: 1.02x faster                                                          |
| regex_compile             | 103 ms                                                          | 102 ms: 1.02x faster                                                           |
| html5lib                  | 48.3 ms                                                         | 47.5 ms: 1.02x faster                                                          |
| sqlglot_parse             | 1.05 ms                                                         | 1.04 ms: 1.01x faster                                                          |
| scimark_monte_carlo       | 50.3 ms                                                         | 49.8 ms: 1.01x faster                                                          |
| dulwich_log               | 49.7 ms                                                         | 49.9 ms: 1.00x slower                                                          |
| gc_traversal              | 1.45 ms                                                         | 1.46 ms: 1.01x slower                                                          |
| regex_v8                  | 15.6 ms                                                         | 15.8 ms: 1.01x slower                                                          |
| python_startup            | 24.3 ms                                                         | 24.9 ms: 1.03x slower                                                          |
| django_template           | 32.7 ms                                                         | 33.6 ms: 1.03x slower                                                          |
| mdp                       | 1.67 sec                                                        | 1.73 sec: 1.04x slower                                                         |
| sqlglot_transpile         | 1.29 ms                                                         | 1.34 ms: 1.04x slower                                                          |
| tornado_http              | 104 ms                                                          | 108 ms: 1.04x slower                                                           |
| 2to3                      | 253 ms                                                          | 263 ms: 1.04x slower                                                           |
| sympy_str                 | 215 ms                                                          | 223 ms: 1.04x slower                                                           |
| nqueens                   | 75.1 ms                                                         | 78.3 ms: 1.04x slower                                                          |
| regex_dna                 | 117 ms                                                          | 122 ms: 1.05x slower                                                           |
| chaos                     | 51.2 ms                                                         | 53.6 ms: 1.05x slower                                                          |
| python_startup_no_site    | 19.9 ms                                                         | 21.0 ms: 1.05x slower                                                          |
| sqlglot_normalize         | 220 ms                                                          | 232 ms: 1.05x slower                                                           |
| typing_runtime_protocols  | 136 us                                                          | 144 us: 1.05x slower                                                           |
| hexiom                    | 4.64 ms                                                         | 4.91 ms: 1.06x slower                                                          |
| sympy_sum                 | 108 ms                                                          | 114 ms: 1.06x slower                                                           |
| sympy_expand              | 375 ms                                                          | 398 ms: 1.06x slower                                                           |
| regex_effbot              | 1.81 ms                                                         | 1.95 ms: 1.08x slower                                                          |
| create_gc_cycles          | 713 us                                                          | 769 us: 1.08x slower                                                           |
| sqlglot_optimize          | 42.5 ms                                                         | 45.9 ms: 1.08x slower                                                          |
| docutils                  | 1.82 sec                                                        | 2.00 sec: 1.10x slower                                                         |
| sympy_integrate           | 15.2 ms                                                         | 16.8 ms: 1.10x slower                                                          |
| genshi_text               | 22.4 ms                                                         | 24.9 ms: 1.11x slower                                                          |
| generators                | 22.1 ms                                                         | 24.5 ms: 1.11x slower                                                          |
| bench_mp_pool             | 74.3 ms                                                         | 82.7 ms: 1.11x slower                                                          |
| async_generators          | 274 ms                                                          | 309 ms: 1.13x slower                                                           |
| genshi_xml                | 49.5 ms                                                         | 56.4 ms: 1.14x slower                                                          |
| coroutines                | 15.7 ms                                                         | 17.9 ms: 1.14x slower                                                          |
| raytrace                  | 205 ms                                                          | 245 ms: 1.19x slower                                                           |
| pylint                    | 225 ms                                                          | 269 ms: 1.20x slower                                                           |
| Geometric mean            | (ref)                                                           | 1.10x faster                                                                   |

Benchmark hidden because not significant (6): bench_thread_pool, async_tree_io, json_loads, unpickle_pure_python, async_tree_cpu_io_mixed_tg, async_tree_io_tg
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 96.15% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown