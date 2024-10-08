# Results vs. 3.13.0b2

- fork: python
- ref: 04eb5c8db1e24cabd0cb
- machine: windows-amd64
- commit hash: 04eb5c8
- commit date: 2024-07-27
- overall geometric mean: 1.07x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-pythonperf1-amd64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 234 ms: 1.13x slower                                                       |
| docutils       | 1.63 sec                                                        | 1.75 sec: 1.07x slower                                                     |
| html5lib       | 35.0 ms                                                         | 42.0 ms: 1.20x slower                                                      |
| tornado_http   | 81.8 ms                                                         | 93.3 ms: 1.14x slower                                                      |
| Geometric mean | (ref)                                                           | 1.14x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-pythonperf1-amd64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg | 605 ms                                                          | 548 ms: 1.11x faster                                                       |
| async_tree_io    | 588 ms                                                          | 559 ms: 1.05x faster                                                       |
| Geometric mean   | (ref)                                                           | 1.03x faster                                                               |

Benchmark hidden because not significant (6): async_tree_memoization_tg, async_tree_none_tg, async_tree_none, async_tree_cpu_io_mixed, async_tree_memoization, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-pythonperf1-amd64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 150 ms                                                          | 151 ms: 1.01x slower                                                       |
| float          | 49.7 ms                                                         | 55.9 ms: 1.12x slower                                                      |
| nbody          | 67.6 ms                                                         | 83.2 ms: 1.23x slower                                                      |
| Geometric mean | (ref)                                                           | 1.12x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-pythonperf1-amd64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 1.58 ms                                                         | 1.58 ms: 1.01x faster                                                      |
| regex_dna      | 119 ms                                                          | 119 ms: 1.00x faster                                                       |
| regex_compile  | 78.0 ms                                                         | 90.4 ms: 1.16x slower                                                      |
| Geometric mean | (ref)                                                           | 1.06x slower                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-pythonperf1-amd64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_loads           | 14.2 us                                                         | 14.4 us: 1.01x slower                                                      |
| xml_etree_parse      | 90.9 ms                                                         | 92.8 ms: 1.02x slower                                                      |
| xml_etree_iterparse  | 62.3 ms                                                         | 65.9 ms: 1.06x slower                                                      |
| xml_etree_generate   | 53.2 ms                                                         | 58.9 ms: 1.11x slower                                                      |
| json_dumps           | 5.61 ms                                                         | 6.26 ms: 1.12x slower                                                      |
| xml_etree_process    | 36.4 ms                                                         | 41.2 ms: 1.13x slower                                                      |
| tomli_loads          | 1.35 sec                                                        | 1.59 sec: 1.18x slower                                                     |
| pickle_pure_python   | 175 us                                                          | 213 us: 1.21x slower                                                       |
| unpickle_pure_python | 122 us                                                          | 151 us: 1.24x slower                                                       |
| Geometric mean       | (ref)                                                           | 1.12x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-pythonperf1-amd64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.3 ms                                                         | 22.2 ms: 1.09x slower                                                      |
| python_startup_no_site | 16.2 ms                                                         | 18.4 ms: 1.14x slower                                                      |
| Geometric mean         | (ref)                                                           | 1.11x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-pythonperf1-amd64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.36 ms                                                         | 7.07 ms: 1.11x slower                                                      |
| django_template | 21.7 ms                                                         | 24.6 ms: 1.13x slower                                                      |
| genshi_xml      | 31.6 ms                                                         | 36.9 ms: 1.17x slower                                                      |
| genshi_text     | 14.4 ms                                                         | 17.3 ms: 1.20x slower                                                      |
| Geometric mean  | (ref)                                                           | 1.15x slower                                                               |

All benchmarks:
===============

| Benchmark                | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-pythonperf1-amd64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|--------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                   | 8.11 ms                                                         | 519 us: 15.63x faster                                                      |
| deepcopy                 | 220 us                                                          | 187 us: 1.17x faster                                                       |
| async_tree_io_tg         | 605 ms                                                          | 548 ms: 1.11x faster                                                       |
| deepcopy_memo            | 22.1 us                                                         | 20.6 us: 1.07x faster                                                      |
| deepcopy_reduce          | 1.99 us                                                         | 1.87 us: 1.07x faster                                                      |
| async_tree_io            | 588 ms                                                          | 559 ms: 1.05x faster                                                       |
| regex_effbot             | 1.58 ms                                                         | 1.58 ms: 1.01x faster                                                      |
| regex_dna                | 119 ms                                                          | 119 ms: 1.00x faster                                                       |
| pidigits                 | 150 ms                                                          | 151 ms: 1.01x slower                                                       |
| json_loads               | 14.2 us                                                         | 14.4 us: 1.01x slower                                                      |
| xml_etree_parse          | 90.9 ms                                                         | 92.8 ms: 1.02x slower                                                      |
| create_gc_cycles         | 888 us                                                          | 908 us: 1.02x slower                                                       |
| generators               | 19.6 ms                                                         | 20.3 ms: 1.04x slower                                                      |
| telco                    | 4.67 ms                                                         | 4.89 ms: 1.05x slower                                                      |
| bench_thread_pool        | 768 us                                                          | 805 us: 1.05x slower                                                       |
| xml_etree_iterparse      | 62.3 ms                                                         | 65.9 ms: 1.06x slower                                                      |
| pathlib                  | 75.9 ms                                                         | 80.9 ms: 1.07x slower                                                      |
| async_generators         | 223 ms                                                          | 240 ms: 1.07x slower                                                       |
| sympy_sum                | 84.4 ms                                                         | 90.6 ms: 1.07x slower                                                      |
| docutils                 | 1.63 sec                                                        | 1.75 sec: 1.07x slower                                                     |
| coroutines               | 12.8 ms                                                         | 13.8 ms: 1.08x slower                                                      |
| sympy_integrate          | 12.2 ms                                                         | 13.3 ms: 1.08x slower                                                      |
| python_startup           | 20.3 ms                                                         | 22.2 ms: 1.09x slower                                                      |
| meteor_contest           | 69.9 ms                                                         | 77.0 ms: 1.10x slower                                                      |
| pycparser                | 754 ms                                                          | 834 ms: 1.11x slower                                                       |
| xml_etree_generate       | 53.2 ms                                                         | 58.9 ms: 1.11x slower                                                      |
| pylint                   | 205 ms                                                          | 227 ms: 1.11x slower                                                       |
| mako                     | 6.36 ms                                                         | 7.07 ms: 1.11x slower                                                      |
| crypto_pyaes             | 45.5 ms                                                         | 50.6 ms: 1.11x slower                                                      |
| logging_simple           | 5.78 us                                                         | 6.43 us: 1.11x slower                                                      |
| spectral_norm            | 63.7 ms                                                         | 70.9 ms: 1.11x slower                                                      |
| scimark_sparse_mat_mult  | 2.50 ms                                                         | 2.79 ms: 1.11x slower                                                      |
| json_dumps               | 5.61 ms                                                         | 6.26 ms: 1.12x slower                                                      |
| coverage                 | 42.1 ms                                                         | 47.0 ms: 1.12x slower                                                      |
| scimark_lu               | 56.6 ms                                                         | 63.2 ms: 1.12x slower                                                      |
| logging_format           | 6.22 us                                                         | 6.98 us: 1.12x slower                                                      |
| dulwich_log              | 38.0 ms                                                         | 42.7 ms: 1.12x slower                                                      |
| sympy_str                | 159 ms                                                          | 178 ms: 1.12x slower                                                       |
| bench_mp_pool            | 64.8 ms                                                         | 72.7 ms: 1.12x slower                                                      |
| sqlglot_optimize         | 32.7 ms                                                         | 36.8 ms: 1.12x slower                                                      |
| float                    | 49.7 ms                                                         | 55.9 ms: 1.12x slower                                                      |
| typing_runtime_protocols | 101 us                                                          | 114 us: 1.13x slower                                                       |
| asyncio_tcp              | 471 ms                                                          | 533 ms: 1.13x slower                                                       |
| xml_etree_process        | 36.4 ms                                                         | 41.2 ms: 1.13x slower                                                      |
| sympy_expand             | 271 ms                                                          | 306 ms: 1.13x slower                                                       |
| 2to3                     | 207 ms                                                          | 234 ms: 1.13x slower                                                       |
| sqlglot_normalize        | 173 ms                                                          | 196 ms: 1.13x slower                                                       |
| django_template          | 21.7 ms                                                         | 24.6 ms: 1.13x slower                                                      |
| python_startup_no_site   | 16.2 ms                                                         | 18.4 ms: 1.14x slower                                                      |
| nqueens                  | 56.7 ms                                                         | 64.5 ms: 1.14x slower                                                      |
| tornado_http             | 81.8 ms                                                         | 93.3 ms: 1.14x slower                                                      |
| pyflate                  | 279 ms                                                          | 319 ms: 1.15x slower                                                       |
| mdp                      | 1.31 sec                                                        | 1.51 sec: 1.15x slower                                                     |
| chaos                    | 38.4 ms                                                         | 44.4 ms: 1.16x slower                                                      |
| regex_compile            | 78.0 ms                                                         | 90.4 ms: 1.16x slower                                                      |
| comprehensions           | 10.4 us                                                         | 12.0 us: 1.16x slower                                                      |
| sqlglot_transpile        | 955 us                                                          | 1.11 ms: 1.16x slower                                                      |
| scimark_sor              | 75.3 ms                                                         | 88.0 ms: 1.17x slower                                                      |
| genshi_xml               | 31.6 ms                                                         | 36.9 ms: 1.17x slower                                                      |
| tomli_loads              | 1.35 sec                                                        | 1.59 sec: 1.18x slower                                                     |
| go                       | 82.1 ms                                                         | 96.8 ms: 1.18x slower                                                      |
| sqlglot_parse            | 748 us                                                          | 886 us: 1.18x slower                                                       |
| hexiom                   | 3.72 ms                                                         | 4.43 ms: 1.19x slower                                                      |
| pprint_safe_repr         | 474 ms                                                          | 566 ms: 1.19x slower                                                       |
| fannkuch                 | 243 ms                                                          | 291 ms: 1.19x slower                                                       |
| pprint_pformat           | 966 ms                                                          | 1.15 sec: 1.19x slower                                                     |
| deltablue                | 1.88 ms                                                         | 2.25 ms: 1.20x slower                                                      |
| html5lib                 | 35.0 ms                                                         | 42.0 ms: 1.20x slower                                                      |
| logging_silent           | 52.9 ns                                                         | 63.7 ns: 1.20x slower                                                      |
| genshi_text              | 14.4 ms                                                         | 17.3 ms: 1.20x slower                                                      |
| richards_super           | 30.2 ms                                                         | 36.4 ms: 1.21x slower                                                      |
| scimark_fft              | 171 ms                                                          | 206 ms: 1.21x slower                                                       |
| richards                 | 26.7 ms                                                         | 32.3 ms: 1.21x slower                                                      |
| raytrace                 | 162 ms                                                          | 197 ms: 1.21x slower                                                       |
| pickle_pure_python       | 175 us                                                          | 213 us: 1.21x slower                                                       |
| nbody                    | 67.6 ms                                                         | 83.2 ms: 1.23x slower                                                      |
| unpickle_pure_python     | 122 us                                                          | 151 us: 1.24x slower                                                       |
| scimark_monte_carlo      | 39.1 ms                                                         | 50.9 ms: 1.30x slower                                                      |
| Geometric mean           | (ref)                                                           | 1.07x slower                                                               |

Benchmark hidden because not significant (10): async_tree_memoization_tg, async_tree_none_tg, async_tree_none, async_tree_cpu_io_mixed, json, gc_traversal, async_tree_memoization, async_tree_cpu_io_mixed_tg, asyncio_tcp_ssl, regex_v8
Ignored benchmarks (10) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.10x
- 95% likely to have a slowdown of 1.09x
- 99% likely to have a slowdown of 1.08x

# Memory
- memory change: unknown