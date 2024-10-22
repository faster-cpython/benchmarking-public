# Results vs. 3.13.0

- fork: python
- ref: a2bec77d25b11f50362a
- machine: windows-x86
- commit hash: a2bec77
- commit date: 2024-07-13
- overall geometric mean: 1.10x faster
- HPT reliability: 97.89%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240713-pythonperf1_win32-x86-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| docutils       | 1.82 sec                                                        | 1.93 sec: 1.06x slower                                                         |
| html5lib       | 48.3 ms                                                         | 47.0 ms: 1.03x faster                                                          |
| tornado_http   | 104 ms                                                          | 97.5 ms: 1.07x faster                                                          |
| Geometric mean | (ref)                                                           | 1.01x faster                                                                   |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240713-pythonperf1_win32-x86-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| asyncio_tcp                | 842 ms                                                          | 668 ms: 1.26x faster                                                           |
| async_tree_memoization_tg  | 287 ms                                                          | 249 ms: 1.15x faster                                                           |
| async_tree_none            | 246 ms                                                          | 220 ms: 1.12x faster                                                           |
| async_tree_none_tg         | 219 ms                                                          | 196 ms: 1.11x faster                                                           |
| async_tree_memoization     | 302 ms                                                          | 272 ms: 1.11x faster                                                           |
| async_tree_cpu_io_mixed    | 494 ms                                                          | 468 ms: 1.06x faster                                                           |
| asyncio_tcp_ssl            | 17.4 sec                                                        | 16.9 sec: 1.03x faster                                                         |
| async_tree_io_tg           | 509 ms                                                          | 501 ms: 1.02x faster                                                           |
| async_tree_cpu_io_mixed_tg | 464 ms                                                          | 458 ms: 1.01x faster                                                           |
| async_generators           | 274 ms                                                          | 307 ms: 1.12x slower                                                           |
| coroutines                 | 15.7 ms                                                         | 18.0 ms: 1.15x slower                                                          |
| Geometric mean             | (ref)                                                           | 1.05x faster                                                                   |

Benchmark hidden because not significant (1): async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240713-pythonperf1_win32-x86-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 81.9 ms                                                         | 54.7 ms: 1.50x faster                                                          |
| float          | 57.8 ms                                                         | 43.9 ms: 1.32x faster                                                          |
| pidigits       | 202 ms                                                          | 195 ms: 1.03x faster                                                           |
| Geometric mean | (ref)                                                           | 1.27x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240713-pythonperf1_win32-x86-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 103 ms                                                          | 95.3 ms: 1.08x faster                                                          |
| regex_v8       | 15.6 ms                                                         | 16.0 ms: 1.03x slower                                                          |
| regex_dna      | 117 ms                                                          | 123 ms: 1.06x slower                                                           |
| regex_effbot   | 1.81 ms                                                         | 1.99 ms: 1.10x slower                                                          |
| Geometric mean | (ref)                                                           | 1.02x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240713-pythonperf1_win32-x86-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pickle_pure_python   | 238 us                                                          | 209 us: 1.14x faster                                                           |
| tomli_loads          | 1.73 sec                                                        | 1.53 sec: 1.13x faster                                                         |
| unpickle_pure_python | 162 us                                                          | 147 us: 1.10x faster                                                           |
| xml_etree_iterparse  | 65.1 ms                                                         | 61.9 ms: 1.05x faster                                                          |
| xml_etree_parse      | 109 ms                                                          | 104 ms: 1.05x faster                                                           |
| json_dumps           | 7.40 ms                                                         | 7.15 ms: 1.04x faster                                                          |
| xml_etree_generate   | 62.6 ms                                                         | 61.4 ms: 1.02x faster                                                          |
| xml_etree_process    | 45.0 ms                                                         | 46.5 ms: 1.03x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.05x faster                                                                   |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240713-pythonperf1_win32-x86-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 24.3 ms                                                         | 23.1 ms: 1.05x faster                                                          |
| python_startup_no_site | 19.9 ms                                                         | 19.1 ms: 1.04x faster                                                          |
| Geometric mean         | (ref)                                                           | 1.05x faster                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240713-pythonperf1_win32-x86-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 7.31 ms                                                         | 5.44 ms: 1.34x faster                                                          |
| django_template | 32.7 ms                                                         | 33.3 ms: 1.02x slower                                                          |
| genshi_text     | 22.4 ms                                                         | 23.5 ms: 1.04x slower                                                          |
| genshi_xml      | 49.5 ms                                                         | 53.6 ms: 1.08x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.04x faster                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240713-pythonperf1_win32-x86-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                     | 10.1 ms                                                         | 760 us: 13.36x faster                                                          |
| coverage                   | 333 ms                                                          | 52.0 ms: 6.41x faster                                                          |
| deepcopy_memo              | 26.2 us                                                         | 15.3 us: 1.71x faster                                                          |
| spectral_norm              | 71.3 ms                                                         | 47.2 ms: 1.51x faster                                                          |
| nbody                      | 81.9 ms                                                         | 54.7 ms: 1.50x faster                                                          |
| mako                       | 7.31 ms                                                         | 5.44 ms: 1.34x faster                                                          |
| float                      | 57.8 ms                                                         | 43.9 ms: 1.32x faster                                                          |
| deepcopy                   | 307 us                                                          | 237 us: 1.30x faster                                                           |
| asyncio_tcp                | 842 ms                                                          | 668 ms: 1.26x faster                                                           |
| telco                      | 6.67 ms                                                         | 5.31 ms: 1.26x faster                                                          |
| scimark_fft                | 206 ms                                                          | 166 ms: 1.24x faster                                                           |
| fannkuch                   | 293 ms                                                          | 236 ms: 1.24x faster                                                           |
| scimark_sparse_mat_mult    | 2.90 ms                                                         | 2.38 ms: 1.22x faster                                                          |
| crypto_pyaes               | 58.2 ms                                                         | 48.0 ms: 1.21x faster                                                          |
| scimark_monte_carlo        | 50.3 ms                                                         | 42.3 ms: 1.19x faster                                                          |
| deepcopy_reduce            | 2.85 us                                                         | 2.41 us: 1.18x faster                                                          |
| pyflate                    | 326 ms                                                          | 277 ms: 1.18x faster                                                           |
| async_tree_memoization_tg  | 287 ms                                                          | 249 ms: 1.15x faster                                                           |
| pprint_safe_repr           | 644 ms                                                          | 565 ms: 1.14x faster                                                           |
| pickle_pure_python         | 238 us                                                          | 209 us: 1.14x faster                                                           |
| tomli_loads                | 1.73 sec                                                        | 1.53 sec: 1.13x faster                                                         |
| async_tree_none            | 246 ms                                                          | 220 ms: 1.12x faster                                                           |
| pprint_pformat             | 1.30 sec                                                        | 1.16 sec: 1.11x faster                                                         |
| async_tree_none_tg         | 219 ms                                                          | 196 ms: 1.11x faster                                                           |
| async_tree_memoization     | 302 ms                                                          | 272 ms: 1.11x faster                                                           |
| comprehensions             | 12.7 us                                                         | 11.5 us: 1.11x faster                                                          |
| sqlglot_parse              | 1.05 ms                                                         | 956 us: 1.10x faster                                                           |
| unpickle_pure_python       | 162 us                                                          | 147 us: 1.10x faster                                                           |
| pathlib                    | 89.4 ms                                                         | 82.0 ms: 1.09x faster                                                          |
| regex_compile              | 103 ms                                                          | 95.3 ms: 1.08x faster                                                          |
| tornado_http               | 104 ms                                                          | 97.5 ms: 1.07x faster                                                          |
| sqlglot_transpile          | 1.29 ms                                                         | 1.22 ms: 1.06x faster                                                          |
| async_tree_cpu_io_mixed    | 494 ms                                                          | 468 ms: 1.06x faster                                                           |
| logging_silent             | 61.6 ns                                                         | 58.4 ns: 1.05x faster                                                          |
| xml_etree_iterparse        | 65.1 ms                                                         | 61.9 ms: 1.05x faster                                                          |
| python_startup             | 24.3 ms                                                         | 23.1 ms: 1.05x faster                                                          |
| xml_etree_parse            | 109 ms                                                          | 104 ms: 1.05x faster                                                           |
| logging_format             | 8.57 us                                                         | 8.21 us: 1.04x faster                                                          |
| python_startup_no_site     | 19.9 ms                                                         | 19.1 ms: 1.04x faster                                                          |
| logging_simple             | 7.87 us                                                         | 7.56 us: 1.04x faster                                                          |
| bench_thread_pool          | 1.02 ms                                                         | 983 us: 1.04x faster                                                           |
| json_dumps                 | 7.40 ms                                                         | 7.15 ms: 1.04x faster                                                          |
| pidigits                   | 202 ms                                                          | 195 ms: 1.03x faster                                                           |
| pycparser                  | 869 ms                                                          | 845 ms: 1.03x faster                                                           |
| asyncio_tcp_ssl            | 17.4 sec                                                        | 16.9 sec: 1.03x faster                                                         |
| html5lib                   | 48.3 ms                                                         | 47.0 ms: 1.03x faster                                                          |
| meteor_contest             | 77.0 ms                                                         | 75.1 ms: 1.03x faster                                                          |
| nqueens                    | 75.1 ms                                                         | 73.3 ms: 1.03x faster                                                          |
| xml_etree_generate         | 62.6 ms                                                         | 61.4 ms: 1.02x faster                                                          |
| async_tree_io_tg           | 509 ms                                                          | 501 ms: 1.02x faster                                                           |
| async_tree_cpu_io_mixed_tg | 464 ms                                                          | 458 ms: 1.01x faster                                                           |
| gc_traversal               | 1.45 ms                                                         | 1.44 ms: 1.01x faster                                                          |
| bench_mp_pool              | 74.3 ms                                                         | 73.7 ms: 1.01x faster                                                          |
| mdp                        | 1.67 sec                                                        | 1.68 sec: 1.01x slower                                                         |
| hexiom                     | 4.64 ms                                                         | 4.70 ms: 1.01x slower                                                          |
| go                         | 111 ms                                                          | 113 ms: 1.02x slower                                                           |
| django_template            | 32.7 ms                                                         | 33.3 ms: 1.02x slower                                                          |
| sympy_str                  | 215 ms                                                          | 220 ms: 1.02x slower                                                           |
| chaos                      | 51.2 ms                                                         | 52.3 ms: 1.02x slower                                                          |
| regex_v8                   | 15.6 ms                                                         | 16.0 ms: 1.03x slower                                                          |
| sympy_sum                  | 108 ms                                                          | 111 ms: 1.03x slower                                                           |
| richards_super             | 38.0 ms                                                         | 39.1 ms: 1.03x slower                                                          |
| xml_etree_process          | 45.0 ms                                                         | 46.5 ms: 1.03x slower                                                          |
| genshi_text                | 22.4 ms                                                         | 23.5 ms: 1.04x slower                                                          |
| sqlglot_optimize           | 42.5 ms                                                         | 44.4 ms: 1.04x slower                                                          |
| sympy_expand               | 375 ms                                                          | 393 ms: 1.05x slower                                                           |
| sympy_integrate            | 15.2 ms                                                         | 16.0 ms: 1.05x slower                                                          |
| regex_dna                  | 117 ms                                                          | 123 ms: 1.06x slower                                                           |
| docutils                   | 1.82 sec                                                        | 1.93 sec: 1.06x slower                                                         |
| create_gc_cycles           | 713 us                                                          | 757 us: 1.06x slower                                                           |
| pylint                     | 225 ms                                                          | 241 ms: 1.07x slower                                                           |
| genshi_xml                 | 49.5 ms                                                         | 53.6 ms: 1.08x slower                                                          |
| sqlglot_normalize          | 220 ms                                                          | 241 ms: 1.10x slower                                                           |
| regex_effbot               | 1.81 ms                                                         | 1.99 ms: 1.10x slower                                                          |
| raytrace                   | 205 ms                                                          | 229 ms: 1.12x slower                                                           |
| deltablue                  | 2.41 ms                                                         | 2.69 ms: 1.12x slower                                                          |
| async_generators           | 274 ms                                                          | 307 ms: 1.12x slower                                                           |
| typing_runtime_protocols   | 136 us                                                          | 153 us: 1.12x slower                                                           |
| scimark_sor                | 91.8 ms                                                         | 104 ms: 1.13x slower                                                           |
| coroutines                 | 15.7 ms                                                         | 18.0 ms: 1.15x slower                                                          |
| generators                 | 22.1 ms                                                         | 27.6 ms: 1.25x slower                                                          |
| scimark_lu                 | 63.5 ms                                                         | 82.6 ms: 1.30x slower                                                          |
| Geometric mean             | (ref)                                                           | 1.10x faster                                                                   |

Benchmark hidden because not significant (5): json, richards, json_loads, 2to3, async_tree_io
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, dulwich_log, flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 97.89% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown