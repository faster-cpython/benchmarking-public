# Results vs. 3.13.0

- fork: brandtbucher
- ref: main
- machine: windows-x86
- commit hash: e256a75
- commit date: 2024-09-24
- overall geometric mean: 1.11x faster
- HPT reliability: 99.56%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf1_win32-x86-brandtbucher-main-3.14.0a0-e256a75 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 253 ms                                                          | 258 ms: 1.02x slower                                                 |
| docutils       | 1.82 sec                                                        | 2.01 sec: 1.10x slower                                               |
| html5lib       | 48.3 ms                                                         | 46.6 ms: 1.04x faster                                                |
| tornado_http   | 104 ms                                                          | 99.4 ms: 1.05x faster                                                |
| Geometric mean | (ref)                                                           | 1.01x slower                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf1_win32-x86-brandtbucher-main-3.14.0a0-e256a75 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------:|
| asyncio_tcp                | 842 ms                                                          | 620 ms: 1.36x faster                                                 |
| async_tree_none            | 246 ms                                                          | 216 ms: 1.14x faster                                                 |
| async_tree_memoization_tg  | 287 ms                                                          | 253 ms: 1.14x faster                                                 |
| async_tree_memoization     | 302 ms                                                          | 272 ms: 1.11x faster                                                 |
| async_tree_none_tg         | 219 ms                                                          | 199 ms: 1.10x faster                                                 |
| async_tree_cpu_io_mixed    | 494 ms                                                          | 475 ms: 1.04x faster                                                 |
| asyncio_tcp_ssl            | 17.4 sec                                                        | 17.0 sec: 1.02x faster                                               |
| async_tree_cpu_io_mixed_tg | 464 ms                                                          | 470 ms: 1.01x slower                                                 |
| async_tree_io_tg           | 509 ms                                                          | 517 ms: 1.02x slower                                                 |
| async_generators           | 274 ms                                                          | 327 ms: 1.20x slower                                                 |
| coroutines                 | 15.7 ms                                                         | 19.2 ms: 1.23x slower                                                |
| Geometric mean             | (ref)                                                           | 1.03x faster                                                         |

Benchmark hidden because not significant (1): async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf1_win32-x86-brandtbucher-main-3.14.0a0-e256a75 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody          | 81.9 ms                                                         | 49.5 ms: 1.65x faster                                                |
| float          | 57.8 ms                                                         | 44.1 ms: 1.31x faster                                                |
| pidigits       | 202 ms                                                          | 198 ms: 1.02x faster                                                 |
| Geometric mean | (ref)                                                           | 1.30x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf1_win32-x86-brandtbucher-main-3.14.0a0-e256a75 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 103 ms                                                          | 103 ms: 1.01x faster                                                 |
| regex_v8       | 15.6 ms                                                         | 15.8 ms: 1.01x slower                                                |
| regex_dna      | 117 ms                                                          | 121 ms: 1.04x slower                                                 |
| regex_effbot   | 1.81 ms                                                         | 1.95 ms: 1.08x slower                                                |
| Geometric mean | (ref)                                                           | 1.03x slower                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf1_win32-x86-brandtbucher-main-3.14.0a0-e256a75 |
|---------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------:|
| xml_etree_generate  | 62.6 ms                                                         | 53.6 ms: 1.17x faster                                                |
| unpickle_list       | 3.09 us                                                         | 2.70 us: 1.15x faster                                                |
| xml_etree_process   | 45.0 ms                                                         | 39.6 ms: 1.14x faster                                                |
| tomli_loads         | 1.73 sec                                                        | 1.54 sec: 1.13x faster                                               |
| pickle_dict         | 21.7 us                                                         | 19.7 us: 1.10x faster                                                |
| xml_etree_iterparse | 65.1 ms                                                         | 61.9 ms: 1.05x faster                                                |
| json_dumps          | 7.40 ms                                                         | 7.06 ms: 1.05x faster                                                |
| xml_etree_parse     | 109 ms                                                          | 104 ms: 1.04x faster                                                 |
| pickle              | 8.42 us                                                         | 8.12 us: 1.04x faster                                                |
| pickle_list         | 3.40 us                                                         | 3.32 us: 1.02x faster                                                |
| unpickle            | 10.5 us                                                         | 10.4 us: 1.02x faster                                                |
| pickle_pure_python  | 238 us                                                          | 236 us: 1.01x faster                                                 |
| Geometric mean      | (ref)                                                           | 1.06x faster                                                         |

Benchmark hidden because not significant (2): json_loads, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf1_win32-x86-brandtbucher-main-3.14.0a0-e256a75 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 19.9 ms                                                         | 20.1 ms: 1.01x slower                                                |
| Geometric mean         | (ref)                                                           | 1.01x slower                                                         |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf1_win32-x86-brandtbucher-main-3.14.0a0-e256a75 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 7.31 ms                                                         | 5.52 ms: 1.32x faster                                                |
| django_template | 32.7 ms                                                         | 33.4 ms: 1.02x slower                                                |
| genshi_text     | 22.4 ms                                                         | 23.6 ms: 1.05x slower                                                |
| genshi_xml      | 49.5 ms                                                         | 55.9 ms: 1.13x slower                                                |
| Geometric mean  | (ref)                                                           | 1.02x faster                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240924-pythonperf1_win32-x86-brandtbucher-main-3.14.0a0-e256a75 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------:|
| thrift                     | 10.1 ms                                                         | 762 us: 13.31x faster                                                |
| coverage                   | 333 ms                                                          | 51.6 ms: 6.46x faster                                                |
| sqlglot_normalize          | 220 ms                                                          | 102 ms: 2.15x faster                                                 |
| deepcopy_memo              | 26.2 us                                                         | 15.1 us: 1.74x faster                                                |
| nbody                      | 81.9 ms                                                         | 49.5 ms: 1.65x faster                                                |
| spectral_norm              | 71.3 ms                                                         | 46.1 ms: 1.55x faster                                                |
| scimark_sor                | 91.8 ms                                                         | 67.4 ms: 1.36x faster                                                |
| asyncio_tcp                | 842 ms                                                          | 620 ms: 1.36x faster                                                 |
| mako                       | 7.31 ms                                                         | 5.52 ms: 1.32x faster                                                |
| float                      | 57.8 ms                                                         | 44.1 ms: 1.31x faster                                                |
| deepcopy                   | 307 us                                                          | 238 us: 1.29x faster                                                 |
| fannkuch                   | 293 ms                                                          | 243 ms: 1.21x faster                                                 |
| crypto_pyaes               | 58.2 ms                                                         | 48.6 ms: 1.20x faster                                                |
| scimark_fft                | 206 ms                                                          | 173 ms: 1.20x faster                                                 |
| telco                      | 6.67 ms                                                         | 5.68 ms: 1.17x faster                                                |
| pyflate                    | 326 ms                                                          | 279 ms: 1.17x faster                                                 |
| xml_etree_generate         | 62.6 ms                                                         | 53.6 ms: 1.17x faster                                                |
| deltablue                  | 2.41 ms                                                         | 2.07 ms: 1.16x faster                                                |
| unpickle_list              | 3.09 us                                                         | 2.70 us: 1.15x faster                                                |
| async_tree_none            | 246 ms                                                          | 216 ms: 1.14x faster                                                 |
| deepcopy_reduce            | 2.85 us                                                         | 2.51 us: 1.14x faster                                                |
| xml_etree_process          | 45.0 ms                                                         | 39.6 ms: 1.14x faster                                                |
| async_tree_memoization_tg  | 287 ms                                                          | 253 ms: 1.14x faster                                                 |
| tomli_loads                | 1.73 sec                                                        | 1.54 sec: 1.13x faster                                               |
| go                         | 111 ms                                                          | 99.3 ms: 1.12x faster                                                |
| async_tree_memoization     | 302 ms                                                          | 272 ms: 1.11x faster                                                 |
| scimark_sparse_mat_mult    | 2.90 ms                                                         | 2.62 ms: 1.11x faster                                                |
| pickle_dict                | 21.7 us                                                         | 19.7 us: 1.10x faster                                                |
| async_tree_none_tg         | 219 ms                                                          | 199 ms: 1.10x faster                                                 |
| pprint_safe_repr           | 644 ms                                                          | 595 ms: 1.08x faster                                                 |
| comprehensions             | 12.7 us                                                         | 11.9 us: 1.07x faster                                                |
| pathlib                    | 89.4 ms                                                         | 83.5 ms: 1.07x faster                                                |
| scimark_lu                 | 63.5 ms                                                         | 59.7 ms: 1.06x faster                                                |
| pycparser                  | 869 ms                                                          | 819 ms: 1.06x faster                                                 |
| richards_super             | 38.0 ms                                                         | 35.9 ms: 1.06x faster                                                |
| logging_silent             | 61.6 ns                                                         | 58.5 ns: 1.05x faster                                                |
| xml_etree_iterparse        | 65.1 ms                                                         | 61.9 ms: 1.05x faster                                                |
| json                       | 4.27 ms                                                         | 4.06 ms: 1.05x faster                                                |
| tornado_http               | 104 ms                                                          | 99.4 ms: 1.05x faster                                                |
| json_dumps                 | 7.40 ms                                                         | 7.06 ms: 1.05x faster                                                |
| xml_etree_parse            | 109 ms                                                          | 104 ms: 1.04x faster                                                 |
| sqlite_synth               | 1.97 us                                                         | 1.89 us: 1.04x faster                                                |
| async_tree_cpu_io_mixed    | 494 ms                                                          | 475 ms: 1.04x faster                                                 |
| meteor_contest             | 77.0 ms                                                         | 74.2 ms: 1.04x faster                                                |
| pickle                     | 8.42 us                                                         | 8.12 us: 1.04x faster                                                |
| html5lib                   | 48.3 ms                                                         | 46.6 ms: 1.04x faster                                                |
| dulwich_log                | 49.7 ms                                                         | 48.1 ms: 1.03x faster                                                |
| richards                   | 33.8 ms                                                         | 32.9 ms: 1.03x faster                                                |
| pprint_pformat             | 1.30 sec                                                        | 1.26 sec: 1.03x faster                                               |
| unpack_sequence            | 42.9 ns                                                         | 41.8 ns: 1.03x faster                                                |
| pickle_list                | 3.40 us                                                         | 3.32 us: 1.02x faster                                                |
| pidigits                   | 202 ms                                                          | 198 ms: 1.02x faster                                                 |
| asyncio_tcp_ssl            | 17.4 sec                                                        | 17.0 sec: 1.02x faster                                               |
| unpickle                   | 10.5 us                                                         | 10.4 us: 1.02x faster                                                |
| pickle_pure_python         | 238 us                                                          | 236 us: 1.01x faster                                                 |
| logging_simple             | 7.87 us                                                         | 7.80 us: 1.01x faster                                                |
| gc_traversal               | 1.45 ms                                                         | 1.44 ms: 1.01x faster                                                |
| regex_compile              | 103 ms                                                          | 103 ms: 1.01x faster                                                 |
| mdp                        | 1.67 sec                                                        | 1.66 sec: 1.01x faster                                               |
| logging_format             | 8.57 us                                                         | 8.51 us: 1.01x faster                                                |
| scimark_monte_carlo        | 50.3 ms                                                         | 50.6 ms: 1.01x slower                                                |
| python_startup_no_site     | 19.9 ms                                                         | 20.1 ms: 1.01x slower                                                |
| regex_v8                   | 15.6 ms                                                         | 15.8 ms: 1.01x slower                                                |
| async_tree_cpu_io_mixed_tg | 464 ms                                                          | 470 ms: 1.01x slower                                                 |
| async_tree_io_tg           | 509 ms                                                          | 517 ms: 1.02x slower                                                 |
| 2to3                       | 253 ms                                                          | 258 ms: 1.02x slower                                                 |
| bench_mp_pool              | 74.3 ms                                                         | 75.9 ms: 1.02x slower                                                |
| django_template            | 32.7 ms                                                         | 33.4 ms: 1.02x slower                                                |
| regex_dna                  | 117 ms                                                          | 121 ms: 1.04x slower                                                 |
| sympy_str                  | 215 ms                                                          | 223 ms: 1.04x slower                                                 |
| create_gc_cycles           | 713 us                                                          | 742 us: 1.04x slower                                                 |
| nqueens                    | 75.1 ms                                                         | 78.2 ms: 1.04x slower                                                |
| sqlglot_transpile          | 1.29 ms                                                         | 1.35 ms: 1.05x slower                                                |
| genshi_text                | 22.4 ms                                                         | 23.6 ms: 1.05x slower                                                |
| sympy_sum                  | 108 ms                                                          | 114 ms: 1.06x slower                                                 |
| hexiom                     | 4.64 ms                                                         | 4.91 ms: 1.06x slower                                                |
| typing_runtime_protocols   | 136 us                                                          | 144 us: 1.06x slower                                                 |
| sympy_expand               | 375 ms                                                          | 399 ms: 1.07x slower                                                 |
| generators                 | 22.1 ms                                                         | 23.7 ms: 1.07x slower                                                |
| regex_effbot               | 1.81 ms                                                         | 1.95 ms: 1.08x slower                                                |
| chaos                      | 51.2 ms                                                         | 55.1 ms: 1.08x slower                                                |
| docutils                   | 1.82 sec                                                        | 2.01 sec: 1.10x slower                                               |
| sympy_integrate            | 15.2 ms                                                         | 16.8 ms: 1.11x slower                                                |
| sqlglot_optimize           | 42.5 ms                                                         | 47.7 ms: 1.12x slower                                                |
| genshi_xml                 | 49.5 ms                                                         | 55.9 ms: 1.13x slower                                                |
| pylint                     | 225 ms                                                          | 268 ms: 1.19x slower                                                 |
| async_generators           | 274 ms                                                          | 327 ms: 1.20x slower                                                 |
| raytrace                   | 205 ms                                                          | 248 ms: 1.21x slower                                                 |
| coroutines                 | 15.7 ms                                                         | 19.2 ms: 1.23x slower                                                |
| Geometric mean             | (ref)                                                           | 1.11x faster                                                         |

Benchmark hidden because not significant (6): bench_thread_pool, json_loads, async_tree_io, unpickle_pure_python, python_startup, sqlglot_parse
Ignored benchmarks (2) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, flaskblogging

# HPT report

- Reliability score: 99.56% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown