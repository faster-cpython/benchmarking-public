# Results vs. base

- fork: faster-cpython
- ref: dynamic_underflow
- machine: linux-x86_64
- commit hash: 6f75dbe
- commit date: 2024-05-04
- overall geometric mean: 1.03x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240504-pythonperf2-x86_64-python-b034f14a4b6e9197d392-3.13.0a6+-b034f14 | bm-20240504-pythonperf2-x86_64-faster%2dcpython-dynamic_underflow-3.13.0a6+-6f75dbe |
|----------------|:----------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| chameleon      | 8.78 ms                                                                      | 8.59 ms: 1.02x faster                                                               |
| tornado_http   | 131 ms                                                                       | 141 ms: 1.08x slower                                                                |
| Geometric mean | (ref)                                                                        | 1.03x slower                                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark       | bm-20240504-pythonperf2-x86_64-python-b034f14a4b6e9197d392-3.13.0a6+-b034f14 | bm-20240504-pythonperf2-x86_64-faster%2dcpython-dynamic_underflow-3.13.0a6+-6f75dbe |
|-----------------|:----------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| async_tree_none | 398 ms                                                                       | 391 ms: 1.02x faster                                                                |
| Geometric mean  | (ref)                                                                        | 1.01x faster                                                                        |

Benchmark hidden because not significant (7): async_tree_cpu_io_mixed, async_tree_memoization, async_tree_none_tg, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_io_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240504-pythonperf2-x86_64-python-b034f14a4b6e9197d392-3.13.0a6+-b034f14 | bm-20240504-pythonperf2-x86_64-faster%2dcpython-dynamic_underflow-3.13.0a6+-6f75dbe |
|----------------|:----------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| float          | 101 ms                                                                       | 98.7 ms: 1.02x faster                                                               |
| pidigits       | 258 ms                                                                       | 259 ms: 1.01x slower                                                                |
| nbody          | 126 ms                                                                       | 130 ms: 1.03x slower                                                                |
| Geometric mean | (ref)                                                                        | 1.00x slower                                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240504-pythonperf2-x86_64-python-b034f14a4b6e9197d392-3.13.0a6+-b034f14 | bm-20240504-pythonperf2-x86_64-faster%2dcpython-dynamic_underflow-3.13.0a6+-6f75dbe |
|----------------|:----------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| regex_dna      | 236 ms                                                                       | 246 ms: 1.04x slower                                                                |
| regex_v8       | 25.9 ms                                                                      | 27.0 ms: 1.04x slower                                                               |
| regex_compile  | 218 ms                                                                       | 231 ms: 1.06x slower                                                                |
| Geometric mean | (ref)                                                                        | 1.04x slower                                                                        |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240504-pythonperf2-x86_64-python-b034f14a4b6e9197d392-3.13.0a6+-b034f14 | bm-20240504-pythonperf2-x86_64-faster%2dcpython-dynamic_underflow-3.13.0a6+-6f75dbe |
|----------------------|:----------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| json_dumps           | 11.6 ms                                                                      | 11.2 ms: 1.04x faster                                                               |
| unpickle_list        | 4.82 us                                                                      | 4.72 us: 1.02x faster                                                               |
| pickle               | 10.8 us                                                                      | 10.7 us: 1.01x faster                                                               |
| json_loads           | 24.5 us                                                                      | 24.5 us: 1.00x slower                                                               |
| pickle_dict          | 32.8 us                                                                      | 32.9 us: 1.00x slower                                                               |
| xml_etree_process    | 67.7 ms                                                                      | 68.1 ms: 1.01x slower                                                               |
| xml_etree_generate   | 98.5 ms                                                                      | 99.2 ms: 1.01x slower                                                               |
| pickle_list          | 4.38 us                                                                      | 4.44 us: 1.01x slower                                                               |
| xml_etree_parse      | 144 ms                                                                       | 147 ms: 1.02x slower                                                                |
| xml_etree_iterparse  | 113 ms                                                                       | 116 ms: 1.02x slower                                                                |
| pickle_pure_python   | 439 us                                                                       | 471 us: 1.07x slower                                                                |
| unpickle_pure_python | 300 us                                                                       | 338 us: 1.13x slower                                                                |
| tomli_loads          | 2.97 sec                                                                     | 3.36 sec: 1.13x slower                                                              |
| Geometric mean       | (ref)                                                                        | 1.02x slower                                                                        |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240504-pythonperf2-x86_64-python-b034f14a4b6e9197d392-3.13.0a6+-b034f14 | bm-20240504-pythonperf2-x86_64-faster%2dcpython-dynamic_underflow-3.13.0a6+-6f75dbe |
|------------------------|:----------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| python_startup         | 13.0 ms                                                                      | 13.0 ms: 1.01x slower                                                               |
| python_startup_no_site | 8.88 ms                                                                      | 8.95 ms: 1.01x slower                                                               |
| Geometric mean         | (ref)                                                                        | 1.01x slower                                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240504-pythonperf2-x86_64-python-b034f14a4b6e9197d392-3.13.0a6+-b034f14 | bm-20240504-pythonperf2-x86_64-faster%2dcpython-dynamic_underflow-3.13.0a6+-6f75dbe |
|-----------------|:----------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| django_template | 49.9 ms                                                                      | 47.5 ms: 1.05x faster                                                               |
| Geometric mean  | (ref)                                                                        | 1.02x faster                                                                        |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                | bm-20240504-pythonperf2-x86_64-python-b034f14a4b6e9197d392-3.13.0a6+-b034f14 | bm-20240504-pythonperf2-x86_64-faster%2dcpython-dynamic_underflow-3.13.0a6+-6f75dbe |
|--------------------------|:----------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| async_generators         | 439 ms                                                                       | 403 ms: 1.09x faster                                                                |
| json                     | 5.84 ms                                                                      | 5.50 ms: 1.06x faster                                                               |
| django_template          | 49.9 ms                                                                      | 47.5 ms: 1.05x faster                                                               |
| json_dumps               | 11.6 ms                                                                      | 11.2 ms: 1.04x faster                                                               |
| pathlib                  | 19.1 ms                                                                      | 18.5 ms: 1.03x faster                                                               |
| typing_runtime_protocols | 210 us                                                                       | 204 us: 1.03x faster                                                                |
| chameleon                | 8.78 ms                                                                      | 8.59 ms: 1.02x faster                                                               |
| float                    | 101 ms                                                                       | 98.7 ms: 1.02x faster                                                               |
| unpickle_list            | 4.82 us                                                                      | 4.72 us: 1.02x faster                                                               |
| bench_mp_pool            | 5.00 ms                                                                      | 4.90 ms: 1.02x faster                                                               |
| async_tree_none          | 398 ms                                                                       | 391 ms: 1.02x faster                                                                |
| telco                    | 9.30 ms                                                                      | 9.15 ms: 1.02x faster                                                               |
| mdp                      | 2.77 sec                                                                     | 2.73 sec: 1.02x faster                                                              |
| sqlite_synth             | 2.97 us                                                                      | 2.93 us: 1.01x faster                                                               |
| deepcopy                 | 491 us                                                                       | 485 us: 1.01x faster                                                                |
| pickle                   | 10.8 us                                                                      | 10.7 us: 1.01x faster                                                               |
| logging_format           | 7.74 us                                                                      | 7.69 us: 1.01x faster                                                               |
| comprehensions           | 27.8 us                                                                      | 27.7 us: 1.01x faster                                                               |
| crypto_pyaes             | 95.2 ms                                                                      | 94.8 ms: 1.00x faster                                                               |
| json_loads               | 24.5 us                                                                      | 24.5 us: 1.00x slower                                                               |
| pickle_dict              | 32.8 us                                                                      | 32.9 us: 1.00x slower                                                               |
| pidigits                 | 258 ms                                                                       | 259 ms: 1.01x slower                                                                |
| xml_etree_process        | 67.7 ms                                                                      | 68.1 ms: 1.01x slower                                                               |
| python_startup           | 13.0 ms                                                                      | 13.0 ms: 1.01x slower                                                               |
| sqlglot_parse            | 1.76 ms                                                                      | 1.77 ms: 1.01x slower                                                               |
| xml_etree_generate       | 98.5 ms                                                                      | 99.2 ms: 1.01x slower                                                               |
| python_startup_no_site   | 8.88 ms                                                                      | 8.95 ms: 1.01x slower                                                               |
| scimark_sparse_mat_mult  | 6.76 ms                                                                      | 6.82 ms: 1.01x slower                                                               |
| logging_simple           | 7.03 us                                                                      | 7.09 us: 1.01x slower                                                               |
| pickle_list              | 4.38 us                                                                      | 4.44 us: 1.01x slower                                                               |
| meteor_contest           | 147 ms                                                                       | 149 ms: 1.02x slower                                                                |
| gc_traversal             | 4.45 ms                                                                      | 4.52 ms: 1.02x slower                                                               |
| deepcopy_reduce          | 4.08 us                                                                      | 4.14 us: 1.02x slower                                                               |
| create_gc_cycles         | 2.03 ms                                                                      | 2.06 ms: 1.02x slower                                                               |
| fannkuch                 | 489 ms                                                                       | 497 ms: 1.02x slower                                                                |
| pyflate                  | 620 ms                                                                       | 632 ms: 1.02x slower                                                                |
| asyncio_tcp              | 388 ms                                                                       | 395 ms: 1.02x slower                                                                |
| bench_thread_pool        | 1.03 ms                                                                      | 1.05 ms: 1.02x slower                                                               |
| thrift                   | 895 us                                                                       | 914 us: 1.02x slower                                                                |
| sqlglot_transpile        | 2.21 ms                                                                      | 2.26 ms: 1.02x slower                                                               |
| xml_etree_parse          | 144 ms                                                                       | 147 ms: 1.02x slower                                                                |
| nqueens                  | 120 ms                                                                       | 122 ms: 1.02x slower                                                                |
| xml_etree_iterparse      | 113 ms                                                                       | 116 ms: 1.02x slower                                                                |
| pycparser                | 1.51 sec                                                                     | 1.55 sec: 1.02x slower                                                              |
| hexiom                   | 10.6 ms                                                                      | 10.9 ms: 1.03x slower                                                               |
| chaos                    | 79.8 ms                                                                      | 81.9 ms: 1.03x slower                                                               |
| coroutines               | 22.8 ms                                                                      | 23.4 ms: 1.03x slower                                                               |
| scimark_fft              | 416 ms                                                                       | 428 ms: 1.03x slower                                                                |
| nbody                    | 126 ms                                                                       | 130 ms: 1.03x slower                                                                |
| pprint_safe_repr         | 1.06 sec                                                                     | 1.10 sec: 1.03x slower                                                              |
| scimark_sor              | 160 ms                                                                       | 165 ms: 1.04x slower                                                                |
| dask                     | 426 ms                                                                       | 441 ms: 1.04x slower                                                                |
| pprint_pformat           | 2.17 sec                                                                     | 2.24 sec: 1.04x slower                                                              |
| deepcopy_memo            | 59.0 us                                                                      | 61.3 us: 1.04x slower                                                               |
| flaskblogging            | 4.99 ms                                                                      | 5.19 ms: 1.04x slower                                                               |
| regex_dna                | 236 ms                                                                       | 246 ms: 1.04x slower                                                                |
| sqlglot_optimize         | 71.6 ms                                                                      | 74.6 ms: 1.04x slower                                                               |
| regex_v8                 | 25.9 ms                                                                      | 27.0 ms: 1.04x slower                                                               |
| regex_compile            | 218 ms                                                                       | 231 ms: 1.06x slower                                                                |
| sympy_integrate          | 28.8 ms                                                                      | 30.6 ms: 1.06x slower                                                               |
| scimark_monte_carlo      | 103 ms                                                                       | 109 ms: 1.07x slower                                                                |
| sympy_expand             | 651 ms                                                                       | 698 ms: 1.07x slower                                                                |
| pickle_pure_python       | 439 us                                                                       | 471 us: 1.07x slower                                                                |
| sqlglot_normalize        | 144 ms                                                                       | 155 ms: 1.08x slower                                                                |
| gunicorn                 | 1.17 ms                                                                      | 1.26 ms: 1.08x slower                                                               |
| go                       | 201 ms                                                                       | 217 ms: 1.08x slower                                                                |
| tornado_http             | 131 ms                                                                       | 141 ms: 1.08x slower                                                                |
| sympy_str                | 383 ms                                                                       | 417 ms: 1.09x slower                                                                |
| sympy_sum                | 193 ms                                                                       | 211 ms: 1.09x slower                                                                |
| aiohttp                  | 1.20 ms                                                                      | 1.31 ms: 1.09x slower                                                               |
| raytrace                 | 323 ms                                                                       | 360 ms: 1.11x slower                                                                |
| scimark_lu               | 135 ms                                                                       | 151 ms: 1.12x slower                                                                |
| mypy2                    | 901 ms                                                                       | 1.01 sec: 1.12x slower                                                              |
| unpickle_pure_python     | 300 us                                                                       | 338 us: 1.13x slower                                                                |
| tomli_loads              | 2.97 sec                                                                     | 3.36 sec: 1.13x slower                                                              |
| pylint                   | 402 ms                                                                       | 457 ms: 1.14x slower                                                                |
| dulwich_log              | 78.4 ms                                                                      | 91.1 ms: 1.16x slower                                                               |
| richards_super           | 66.9 ms                                                                      | 79.8 ms: 1.19x slower                                                               |
| richards                 | 60.2 ms                                                                      | 72.0 ms: 1.20x slower                                                               |
| logging_silent           | 154 ns                                                                       | 185 ns: 1.20x slower                                                                |
| deltablue                | 4.52 ms                                                                      | 6.15 ms: 1.36x slower                                                               |
| Geometric mean           | (ref)                                                                        | 1.03x slower                                                                        |

Benchmark hidden because not significant (15): async_tree_cpu_io_mixed, async_tree_memoization, async_tree_none_tg, coverage, async_tree_cpu_io_mixed_tg, regex_effbot, unpickle, mako, spectral_norm, async_tree_memoization_tg, async_tree_io_tg, asyncio_tcp_ssl, generators, async_tree_io, asyncio_websockets
Ignored benchmarks (4) of results/bm-20240504-3.13.0a6+-b034f14-PYTHON_UOPS/bm-20240504-pythonperf2-x86_64-python-b034f14a4b6e9197d392-3.13.0a6+-b034f14.json: 2to3, genshi_text, genshi_xml, html5lib

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x