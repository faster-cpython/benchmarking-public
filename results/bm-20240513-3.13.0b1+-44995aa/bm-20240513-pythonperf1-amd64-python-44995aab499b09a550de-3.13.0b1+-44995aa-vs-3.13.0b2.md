# Results vs. 3.13.0b2

- fork: python
- ref: 44995aab499b09a550de
- machine: windows-amd64
- commit hash: 44995aa
- commit date: 2024-05-13
- overall geometric mean: 1.00x faster
- HPT reliability: 98.12%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| chameleon      | 4.80 ms                                                         | 4.71 ms: 1.02x faster                                                       |
| docutils       | 1.63 sec                                                        | 1.61 sec: 1.01x faster                                                      |
| html5lib       | 35.0 ms                                                         | 35.2 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                           | 1.00x faster                                                                |

Benchmark hidden because not significant (2): 2to3, tornado_http

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_none, async_tree_io, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_memoization, async_tree_io_tg, async_tree_none_tg, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 49.7 ms                                                         | 48.2 ms: 1.03x faster                                                       |
| nbody          | 67.6 ms                                                         | 66.2 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                           | 1.02x faster                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 78.0 ms                                                         | 76.9 ms: 1.01x faster                                                       |
| regex_effbot   | 1.58 ms                                                         | 1.57 ms: 1.01x faster                                                       |
| regex_dna      | 119 ms                                                          | 118 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                           | 1.01x faster                                                                |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_process    | 36.4 ms                                                         | 35.9 ms: 1.02x faster                                                       |
| unpickle_pure_python | 122 us                                                          | 120 us: 1.01x faster                                                        |
| pickle_pure_python   | 175 us                                                          | 173 us: 1.01x faster                                                        |
| json_loads           | 14.2 us                                                         | 14.0 us: 1.01x faster                                                       |
| xml_etree_iterparse  | 62.3 ms                                                         | 61.8 ms: 1.01x faster                                                       |
| json_dumps           | 5.61 ms                                                         | 5.57 ms: 1.01x faster                                                       |
| xml_etree_generate   | 53.2 ms                                                         | 52.9 ms: 1.01x faster                                                       |
| pickle               | 7.11 us                                                         | 7.18 us: 1.01x slower                                                       |
| pickle_dict          | 18.1 us                                                         | 19.4 us: 1.07x slower                                                       |
| Geometric mean       | (ref)                                                           | 1.00x slower                                                                |

Benchmark hidden because not significant (5): tomli_loads, unpickle_list, xml_etree_parse, unpickle, pickle_list

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|-----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 21.7 ms                                                         | 21.1 ms: 1.03x faster                                                       |
| mako            | 6.36 ms                                                         | 6.28 ms: 1.01x faster                                                       |
| genshi_text     | 14.4 ms                                                         | 14.5 ms: 1.01x slower                                                       |
| Geometric mean  | (ref)                                                           | 1.01x faster                                                                |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240513-pythonperf1-amd64-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|--------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pycparser                | 754 ms                                                          | 697 ms: 1.08x faster                                                        |
| spectral_norm            | 63.7 ms                                                         | 60.1 ms: 1.06x faster                                                       |
| scimark_lu               | 56.6 ms                                                         | 53.7 ms: 1.05x faster                                                       |
| scimark_sparse_mat_mult  | 2.50 ms                                                         | 2.39 ms: 1.05x faster                                                       |
| richards                 | 26.7 ms                                                         | 25.8 ms: 1.04x faster                                                       |
| scimark_sor              | 75.3 ms                                                         | 73.1 ms: 1.03x faster                                                       |
| float                    | 49.7 ms                                                         | 48.2 ms: 1.03x faster                                                       |
| comprehensions           | 10.4 us                                                         | 10.1 us: 1.03x faster                                                       |
| richards_super           | 30.2 ms                                                         | 29.3 ms: 1.03x faster                                                       |
| django_template          | 21.7 ms                                                         | 21.1 ms: 1.03x faster                                                       |
| hexiom                   | 3.72 ms                                                         | 3.64 ms: 1.02x faster                                                       |
| nbody                    | 67.6 ms                                                         | 66.2 ms: 1.02x faster                                                       |
| nqueens                  | 56.7 ms                                                         | 55.5 ms: 1.02x faster                                                       |
| fannkuch                 | 243 ms                                                          | 238 ms: 1.02x faster                                                        |
| chameleon                | 4.80 ms                                                         | 4.71 ms: 1.02x faster                                                       |
| telco                    | 4.67 ms                                                         | 4.59 ms: 1.02x faster                                                       |
| sqlglot_normalize        | 173 ms                                                          | 170 ms: 1.02x faster                                                        |
| logging_format           | 6.22 us                                                         | 6.12 us: 1.02x faster                                                       |
| xml_etree_process        | 36.4 ms                                                         | 35.9 ms: 1.02x faster                                                       |
| deepcopy_memo            | 22.1 us                                                         | 21.7 us: 1.02x faster                                                       |
| unpickle_pure_python     | 122 us                                                          | 120 us: 1.01x faster                                                        |
| pickle_pure_python       | 175 us                                                          | 173 us: 1.01x faster                                                        |
| pprint_safe_repr         | 474 ms                                                          | 467 ms: 1.01x faster                                                        |
| regex_compile            | 78.0 ms                                                         | 76.9 ms: 1.01x faster                                                       |
| mako                     | 6.36 ms                                                         | 6.28 ms: 1.01x faster                                                       |
| crypto_pyaes             | 45.5 ms                                                         | 44.9 ms: 1.01x faster                                                       |
| json_loads               | 14.2 us                                                         | 14.0 us: 1.01x faster                                                       |
| sympy_expand             | 271 ms                                                          | 267 ms: 1.01x faster                                                        |
| generators               | 19.6 ms                                                         | 19.3 ms: 1.01x faster                                                       |
| regex_effbot             | 1.58 ms                                                         | 1.57 ms: 1.01x faster                                                       |
| deepcopy_reduce          | 1.99 us                                                         | 1.97 us: 1.01x faster                                                       |
| docutils                 | 1.63 sec                                                        | 1.61 sec: 1.01x faster                                                      |
| sympy_str                | 159 ms                                                          | 158 ms: 1.01x faster                                                        |
| sympy_integrate          | 12.2 ms                                                         | 12.1 ms: 1.01x faster                                                       |
| logging_simple           | 5.78 us                                                         | 5.73 us: 1.01x faster                                                       |
| pyflate                  | 279 ms                                                          | 276 ms: 1.01x faster                                                        |
| xml_etree_iterparse      | 62.3 ms                                                         | 61.8 ms: 1.01x faster                                                       |
| typing_runtime_protocols | 101 us                                                          | 100 us: 1.01x faster                                                        |
| json_dumps               | 5.61 ms                                                         | 5.57 ms: 1.01x faster                                                       |
| raytrace                 | 162 ms                                                          | 161 ms: 1.01x faster                                                        |
| regex_dna                | 119 ms                                                          | 118 ms: 1.01x faster                                                        |
| pprint_pformat           | 966 ms                                                          | 959 ms: 1.01x faster                                                        |
| sympy_sum                | 84.4 ms                                                         | 83.8 ms: 1.01x faster                                                       |
| deepcopy                 | 220 us                                                          | 218 us: 1.01x faster                                                        |
| xml_etree_generate       | 53.2 ms                                                         | 52.9 ms: 1.01x faster                                                       |
| thrift                   | 8.11 ms                                                         | 8.07 ms: 1.00x faster                                                       |
| chaos                    | 38.4 ms                                                         | 38.2 ms: 1.00x faster                                                       |
| sqlglot_optimize         | 32.7 ms                                                         | 32.6 ms: 1.00x faster                                                       |
| html5lib                 | 35.0 ms                                                         | 35.2 ms: 1.01x slower                                                       |
| genshi_text              | 14.4 ms                                                         | 14.5 ms: 1.01x slower                                                       |
| sqlite_synth             | 1.60 us                                                         | 1.61 us: 1.01x slower                                                       |
| scimark_fft              | 171 ms                                                          | 172 ms: 1.01x slower                                                        |
| deltablue                | 1.88 ms                                                         | 1.90 ms: 1.01x slower                                                       |
| pickle                   | 7.11 us                                                         | 7.18 us: 1.01x slower                                                       |
| async_generators         | 223 ms                                                          | 226 ms: 1.01x slower                                                        |
| meteor_contest           | 69.9 ms                                                         | 71.0 ms: 1.02x slower                                                       |
| mdp                      | 1.31 sec                                                        | 1.33 sec: 1.02x slower                                                      |
| go                       | 82.1 ms                                                         | 83.5 ms: 1.02x slower                                                       |
| create_gc_cycles         | 888 us                                                          | 903 us: 1.02x slower                                                        |
| bench_mp_pool            | 64.8 ms                                                         | 66.2 ms: 1.02x slower                                                       |
| dulwich_log              | 38.0 ms                                                         | 39.1 ms: 1.03x slower                                                       |
| coverage                 | 42.1 ms                                                         | 43.5 ms: 1.03x slower                                                       |
| pathlib                  | 75.9 ms                                                         | 79.3 ms: 1.04x slower                                                       |
| bench_thread_pool        | 768 us                                                          | 808 us: 1.05x slower                                                        |
| pickle_dict              | 18.1 us                                                         | 19.4 us: 1.07x slower                                                       |
| asyncio_tcp              | 471 ms                                                          | 566 ms: 1.20x slower                                                        |
| Geometric mean           | (ref)                                                           | 1.00x faster                                                                |

Benchmark hidden because not significant (32): regex_v8, json, async_tree_none, python_startup, coroutines, tornado_http, mypy2, logging_silent, sqlglot_transpile, scimark_monte_carlo, flaskblogging, pidigits, tomli_loads, async_tree_io, async_tree_cpu_io_mixed, sqlglot_parse, unpickle_list, genshi_xml, async_tree_cpu_io_mixed_tg, gc_traversal, async_tree_memoization, 2to3, pylint, xml_etree_parse, async_tree_io_tg, unpickle, aiohttp, python_startup_no_site, pickle_list, async_tree_none_tg, async_tree_memoization_tg, asyncio_tcp_ssl

# HPT report

- Reliability score: 98.12% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown