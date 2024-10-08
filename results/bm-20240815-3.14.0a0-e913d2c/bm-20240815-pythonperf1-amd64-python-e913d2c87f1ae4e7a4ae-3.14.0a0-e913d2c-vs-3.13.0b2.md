# Results vs. 3.13.0b2

- fork: python
- ref: e913d2c87f1ae4e7a4ae
- machine: windows-amd64
- commit hash: e913d2c
- commit date: 2024-08-15
- overall geometric mean: 1.06x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240815-pythonperf1-amd64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 231 ms: 1.12x slower                                                       |
| docutils       | 1.63 sec                                                        | 1.75 sec: 1.08x slower                                                     |
| html5lib       | 35.0 ms                                                         | 42.0 ms: 1.20x slower                                                      |
| tornado_http   | 81.8 ms                                                         | 93.2 ms: 1.14x slower                                                      |
| Geometric mean | (ref)                                                           | 1.13x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240815-pythonperf1-amd64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 605 ms                                                          | 547 ms: 1.11x faster                                                       |
| async_tree_cpu_io_mixed_tg | 382 ms                                                          | 395 ms: 1.03x slower                                                       |
| Geometric mean             | (ref)                                                           | 1.02x faster                                                               |

Benchmark hidden because not significant (6): async_tree_memoization_tg, async_tree_none_tg, async_tree_io, async_tree_none, async_tree_cpu_io_mixed, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240815-pythonperf1-amd64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 150 ms                                                          | 151 ms: 1.01x slower                                                       |
| float          | 49.7 ms                                                         | 56.4 ms: 1.13x slower                                                      |
| nbody          | 67.6 ms                                                         | 82.3 ms: 1.22x slower                                                      |
| Geometric mean | (ref)                                                           | 1.12x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240815-pythonperf1-amd64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 1.58 ms                                                         | 1.56 ms: 1.01x faster                                                      |
| regex_dna      | 119 ms                                                          | 118 ms: 1.01x faster                                                       |
| regex_compile  | 78.0 ms                                                         | 91.7 ms: 1.18x slower                                                      |
| Geometric mean | (ref)                                                           | 1.05x slower                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240815-pythonperf1-amd64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_parse      | 90.9 ms                                                         | 94.6 ms: 1.04x slower                                                      |
| xml_etree_iterparse  | 62.3 ms                                                         | 65.8 ms: 1.06x slower                                                      |
| xml_etree_generate   | 53.2 ms                                                         | 57.8 ms: 1.09x slower                                                      |
| json_dumps           | 5.61 ms                                                         | 6.22 ms: 1.11x slower                                                      |
| xml_etree_process    | 36.4 ms                                                         | 41.2 ms: 1.13x slower                                                      |
| tomli_loads          | 1.35 sec                                                        | 1.58 sec: 1.17x slower                                                     |
| pickle_pure_python   | 175 us                                                          | 211 us: 1.21x slower                                                       |
| unpickle_pure_python | 122 us                                                          | 148 us: 1.22x slower                                                       |
| Geometric mean       | (ref)                                                           | 1.11x slower                                                               |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240815-pythonperf1-amd64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.3 ms                                                         | 22.0 ms: 1.08x slower                                                      |
| python_startup_no_site | 16.2 ms                                                         | 17.8 ms: 1.10x slower                                                      |
| Geometric mean         | (ref)                                                           | 1.09x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240815-pythonperf1-amd64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.36 ms                                                         | 7.03 ms: 1.11x slower                                                      |
| django_template | 21.7 ms                                                         | 24.6 ms: 1.14x slower                                                      |
| genshi_xml      | 31.6 ms                                                         | 36.4 ms: 1.15x slower                                                      |
| genshi_text     | 14.4 ms                                                         | 17.5 ms: 1.21x slower                                                      |
| Geometric mean  | (ref)                                                           | 1.15x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240815-pythonperf1-amd64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.11 ms                                                         | 530 us: 15.31x faster                                                      |
| deepcopy                   | 220 us                                                          | 188 us: 1.17x faster                                                       |
| async_tree_io_tg           | 605 ms                                                          | 547 ms: 1.11x faster                                                       |
| deepcopy_memo              | 22.1 us                                                         | 20.4 us: 1.08x faster                                                      |
| json                       | 3.19 ms                                                         | 2.98 ms: 1.07x faster                                                      |
| deepcopy_reduce            | 1.99 us                                                         | 1.89 us: 1.05x faster                                                      |
| regex_effbot               | 1.58 ms                                                         | 1.56 ms: 1.01x faster                                                      |
| regex_dna                  | 119 ms                                                          | 118 ms: 1.01x faster                                                       |
| pidigits                   | 150 ms                                                          | 151 ms: 1.01x slower                                                       |
| gc_traversal               | 1.55 ms                                                         | 1.57 ms: 1.01x slower                                                      |
| create_gc_cycles           | 888 us                                                          | 909 us: 1.02x slower                                                       |
| pathlib                    | 75.9 ms                                                         | 78.3 ms: 1.03x slower                                                      |
| async_tree_cpu_io_mixed_tg | 382 ms                                                          | 395 ms: 1.03x slower                                                       |
| xml_etree_parse            | 90.9 ms                                                         | 94.6 ms: 1.04x slower                                                      |
| telco                      | 4.67 ms                                                         | 4.87 ms: 1.04x slower                                                      |
| crypto_pyaes               | 45.5 ms                                                         | 47.8 ms: 1.05x slower                                                      |
| xml_etree_iterparse        | 62.3 ms                                                         | 65.8 ms: 1.06x slower                                                      |
| spectral_norm              | 63.7 ms                                                         | 67.6 ms: 1.06x slower                                                      |
| bench_mp_pool              | 64.8 ms                                                         | 68.8 ms: 1.06x slower                                                      |
| scimark_sparse_mat_mult    | 2.50 ms                                                         | 2.68 ms: 1.07x slower                                                      |
| bench_thread_pool          | 768 us                                                          | 824 us: 1.07x slower                                                       |
| docutils                   | 1.63 sec                                                        | 1.75 sec: 1.08x slower                                                     |
| logging_format             | 6.22 us                                                         | 6.72 us: 1.08x slower                                                      |
| python_startup             | 20.3 ms                                                         | 22.0 ms: 1.08x slower                                                      |
| generators                 | 19.6 ms                                                         | 21.2 ms: 1.08x slower                                                      |
| logging_simple             | 5.78 us                                                         | 6.29 us: 1.09x slower                                                      |
| xml_etree_generate         | 53.2 ms                                                         | 57.8 ms: 1.09x slower                                                      |
| sympy_integrate            | 12.2 ms                                                         | 13.4 ms: 1.09x slower                                                      |
| sympy_sum                  | 84.4 ms                                                         | 92.3 ms: 1.09x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                         | 17.8 ms: 1.10x slower                                                      |
| coroutines                 | 12.8 ms                                                         | 14.1 ms: 1.10x slower                                                      |
| nqueens                    | 56.7 ms                                                         | 62.4 ms: 1.10x slower                                                      |
| meteor_contest             | 69.9 ms                                                         | 77.2 ms: 1.11x slower                                                      |
| mako                       | 6.36 ms                                                         | 7.03 ms: 1.11x slower                                                      |
| async_generators           | 223 ms                                                          | 247 ms: 1.11x slower                                                       |
| json_dumps                 | 5.61 ms                                                         | 6.22 ms: 1.11x slower                                                      |
| sqlglot_optimize           | 32.7 ms                                                         | 36.3 ms: 1.11x slower                                                      |
| pylint                     | 205 ms                                                          | 228 ms: 1.11x slower                                                       |
| sqlglot_normalize          | 173 ms                                                          | 193 ms: 1.12x slower                                                       |
| 2to3                       | 207 ms                                                          | 231 ms: 1.12x slower                                                       |
| coverage                   | 42.1 ms                                                         | 47.4 ms: 1.13x slower                                                      |
| xml_etree_process          | 36.4 ms                                                         | 41.2 ms: 1.13x slower                                                      |
| sympy_str                  | 159 ms                                                          | 180 ms: 1.13x slower                                                       |
| mdp                        | 1.31 sec                                                        | 1.49 sec: 1.13x slower                                                     |
| float                      | 49.7 ms                                                         | 56.4 ms: 1.13x slower                                                      |
| django_template            | 21.7 ms                                                         | 24.6 ms: 1.14x slower                                                      |
| chaos                      | 38.4 ms                                                         | 43.7 ms: 1.14x slower                                                      |
| typing_runtime_protocols   | 101 us                                                          | 115 us: 1.14x slower                                                       |
| tornado_http               | 81.8 ms                                                         | 93.2 ms: 1.14x slower                                                      |
| dulwich_log                | 38.0 ms                                                         | 43.4 ms: 1.14x slower                                                      |
| asyncio_tcp                | 471 ms                                                          | 539 ms: 1.14x slower                                                       |
| genshi_xml                 | 31.6 ms                                                         | 36.4 ms: 1.15x slower                                                      |
| sympy_expand               | 271 ms                                                          | 312 ms: 1.15x slower                                                       |
| comprehensions             | 10.4 us                                                         | 12.0 us: 1.15x slower                                                      |
| scimark_lu                 | 56.6 ms                                                         | 65.5 ms: 1.16x slower                                                      |
| pprint_safe_repr           | 474 ms                                                          | 549 ms: 1.16x slower                                                       |
| pyflate                    | 279 ms                                                          | 324 ms: 1.16x slower                                                       |
| sqlglot_transpile          | 955 us                                                          | 1.11 ms: 1.16x slower                                                      |
| tomli_loads                | 1.35 sec                                                        | 1.58 sec: 1.17x slower                                                     |
| regex_compile              | 78.0 ms                                                         | 91.7 ms: 1.18x slower                                                      |
| pycparser                  | 754 ms                                                          | 888 ms: 1.18x slower                                                       |
| pprint_pformat             | 966 ms                                                          | 1.14 sec: 1.18x slower                                                     |
| sqlglot_parse              | 748 us                                                          | 888 us: 1.19x slower                                                       |
| hexiom                     | 3.72 ms                                                         | 4.46 ms: 1.20x slower                                                      |
| go                         | 82.1 ms                                                         | 98.5 ms: 1.20x slower                                                      |
| html5lib                   | 35.0 ms                                                         | 42.0 ms: 1.20x slower                                                      |
| richards_super             | 30.2 ms                                                         | 36.2 ms: 1.20x slower                                                      |
| scimark_fft                | 171 ms                                                          | 205 ms: 1.20x slower                                                       |
| logging_silent             | 52.9 ns                                                         | 63.7 ns: 1.20x slower                                                      |
| raytrace                   | 162 ms                                                          | 195 ms: 1.20x slower                                                       |
| pickle_pure_python         | 175 us                                                          | 211 us: 1.21x slower                                                       |
| richards                   | 26.7 ms                                                         | 32.3 ms: 1.21x slower                                                      |
| deltablue                  | 1.88 ms                                                         | 2.27 ms: 1.21x slower                                                      |
| fannkuch                   | 243 ms                                                          | 294 ms: 1.21x slower                                                       |
| genshi_text                | 14.4 ms                                                         | 17.5 ms: 1.21x slower                                                      |
| unpickle_pure_python       | 122 us                                                          | 148 us: 1.22x slower                                                       |
| nbody                      | 67.6 ms                                                         | 82.3 ms: 1.22x slower                                                      |
| scimark_sor                | 75.3 ms                                                         | 92.2 ms: 1.22x slower                                                      |
| scimark_monte_carlo        | 39.1 ms                                                         | 50.3 ms: 1.28x slower                                                      |
| Geometric mean             | (ref)                                                           | 1.06x slower                                                               |

Benchmark hidden because not significant (9): async_tree_memoization_tg, async_tree_none_tg, async_tree_io, async_tree_none, async_tree_cpu_io_mixed, json_loads, async_tree_memoization, asyncio_tcp_ssl, regex_v8
Ignored benchmarks (10) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.09x
- 95% likely to have a slowdown of 1.09x
- 99% likely to have a slowdown of 1.08x

# Memory
- memory change: unknown