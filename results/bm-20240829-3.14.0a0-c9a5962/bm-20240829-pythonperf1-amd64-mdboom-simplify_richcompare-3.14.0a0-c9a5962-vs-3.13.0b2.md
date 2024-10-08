# Results vs. 3.13.0b2

- fork: mdboom
- ref: simplify_richcompare
- machine: windows-amd64
- commit hash: c9a5962
- commit date: 2024-08-29
- overall geometric mean: 1.08x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 230 ms: 1.11x slower                                                       |
| docutils       | 1.63 sec                                                        | 1.71 sec: 1.05x slower                                                     |
| html5lib       | 35.0 ms                                                         | 39.7 ms: 1.13x slower                                                      |
| tornado_http   | 81.8 ms                                                         | 93.8 ms: 1.15x slower                                                      |
| Geometric mean | (ref)                                                           | 1.11x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 605 ms                                                          | 569 ms: 1.06x faster                                                       |
| async_tree_none            | 218 ms                                                          | 211 ms: 1.03x faster                                                       |
| async_tree_cpu_io_mixed_tg | 382 ms                                                          | 402 ms: 1.05x slower                                                       |
| Geometric mean             | (ref)                                                           | 1.01x faster                                                               |

Benchmark hidden because not significant (5): async_tree_memoization_tg, async_tree_io, async_tree_memoization, async_tree_cpu_io_mixed, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 150 ms                                                          | 151 ms: 1.01x slower                                                       |
| float          | 49.7 ms                                                         | 58.6 ms: 1.18x slower                                                      |
| nbody          | 67.6 ms                                                         | 87.8 ms: 1.30x slower                                                      |
| Geometric mean | (ref)                                                           | 1.16x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 119 ms                                                          | 120 ms: 1.01x slower                                                       |
| regex_compile  | 78.0 ms                                                         | 92.4 ms: 1.18x slower                                                      |
| Geometric mean | (ref)                                                           | 1.05x slower                                                               |

Benchmark hidden because not significant (2): regex_effbot, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_loads           | 14.2 us                                                         | 14.5 us: 1.02x slower                                                      |
| xml_etree_parse      | 90.9 ms                                                         | 95.0 ms: 1.04x slower                                                      |
| xml_etree_iterparse  | 62.3 ms                                                         | 66.3 ms: 1.06x slower                                                      |
| xml_etree_generate   | 53.2 ms                                                         | 59.4 ms: 1.12x slower                                                      |
| json_dumps           | 5.61 ms                                                         | 6.32 ms: 1.12x slower                                                      |
| xml_etree_process    | 36.4 ms                                                         | 42.3 ms: 1.16x slower                                                      |
| tomli_loads          | 1.35 sec                                                        | 1.62 sec: 1.20x slower                                                     |
| pickle_pure_python   | 175 us                                                          | 214 us: 1.22x slower                                                       |
| unpickle_pure_python | 122 us                                                          | 155 us: 1.28x slower                                                       |
| Geometric mean       | (ref)                                                           | 1.13x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.3 ms                                                         | 22.4 ms: 1.11x slower                                                      |
| python_startup_no_site | 16.2 ms                                                         | 18.1 ms: 1.12x slower                                                      |
| Geometric mean         | (ref)                                                           | 1.11x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.36 ms                                                         | 7.12 ms: 1.12x slower                                                      |
| genshi_xml      | 31.6 ms                                                         | 35.9 ms: 1.14x slower                                                      |
| django_template | 21.7 ms                                                         | 25.5 ms: 1.18x slower                                                      |
| genshi_text     | 14.4 ms                                                         | 17.2 ms: 1.19x slower                                                      |
| Geometric mean  | (ref)                                                           | 1.16x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.11 ms                                                         | 521 us: 15.57x faster                                                      |
| deepcopy                   | 220 us                                                          | 188 us: 1.17x faster                                                       |
| async_tree_io_tg           | 605 ms                                                          | 569 ms: 1.06x faster                                                       |
| json                       | 3.19 ms                                                         | 3.03 ms: 1.05x faster                                                      |
| deepcopy_memo              | 22.1 us                                                         | 21.2 us: 1.04x faster                                                      |
| async_tree_none            | 218 ms                                                          | 211 ms: 1.03x faster                                                       |
| deepcopy_reduce            | 1.99 us                                                         | 1.95 us: 1.02x faster                                                      |
| regex_dna                  | 119 ms                                                          | 120 ms: 1.01x slower                                                       |
| gc_traversal               | 1.55 ms                                                         | 1.57 ms: 1.01x slower                                                      |
| pidigits                   | 150 ms                                                          | 151 ms: 1.01x slower                                                       |
| json_loads                 | 14.2 us                                                         | 14.5 us: 1.02x slower                                                      |
| create_gc_cycles           | 888 us                                                          | 919 us: 1.03x slower                                                       |
| xml_etree_parse            | 90.9 ms                                                         | 95.0 ms: 1.04x slower                                                      |
| generators                 | 19.6 ms                                                         | 20.5 ms: 1.05x slower                                                      |
| pathlib                    | 75.9 ms                                                         | 79.6 ms: 1.05x slower                                                      |
| docutils                   | 1.63 sec                                                        | 1.71 sec: 1.05x slower                                                     |
| async_tree_cpu_io_mixed_tg | 382 ms                                                          | 402 ms: 1.05x slower                                                       |
| xml_etree_iterparse        | 62.3 ms                                                         | 66.3 ms: 1.06x slower                                                      |
| bench_mp_pool              | 64.8 ms                                                         | 69.0 ms: 1.06x slower                                                      |
| bench_thread_pool          | 768 us                                                          | 818 us: 1.07x slower                                                       |
| go                         | 82.1 ms                                                         | 88.1 ms: 1.07x slower                                                      |
| sympy_sum                  | 84.4 ms                                                         | 91.1 ms: 1.08x slower                                                      |
| crypto_pyaes               | 45.5 ms                                                         | 49.3 ms: 1.08x slower                                                      |
| asyncio_tcp_ssl            | 1.48 sec                                                        | 1.60 sec: 1.08x slower                                                     |
| sympy_integrate            | 12.2 ms                                                         | 13.3 ms: 1.09x slower                                                      |
| logging_format             | 6.22 us                                                         | 6.85 us: 1.10x slower                                                      |
| python_startup             | 20.3 ms                                                         | 22.4 ms: 1.11x slower                                                      |
| pylint                     | 205 ms                                                          | 227 ms: 1.11x slower                                                       |
| 2to3                       | 207 ms                                                          | 230 ms: 1.11x slower                                                       |
| typing_runtime_protocols   | 101 us                                                          | 112 us: 1.11x slower                                                       |
| pycparser                  | 754 ms                                                          | 839 ms: 1.11x slower                                                       |
| telco                      | 4.67 ms                                                         | 5.20 ms: 1.11x slower                                                      |
| xml_etree_generate         | 53.2 ms                                                         | 59.4 ms: 1.12x slower                                                      |
| sympy_str                  | 159 ms                                                          | 178 ms: 1.12x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                         | 18.1 ms: 1.12x slower                                                      |
| sqlglot_optimize           | 32.7 ms                                                         | 36.6 ms: 1.12x slower                                                      |
| mako                       | 6.36 ms                                                         | 7.12 ms: 1.12x slower                                                      |
| logging_simple             | 5.78 us                                                         | 6.48 us: 1.12x slower                                                      |
| sqlglot_normalize          | 173 ms                                                          | 194 ms: 1.12x slower                                                       |
| async_generators           | 223 ms                                                          | 251 ms: 1.12x slower                                                       |
| json_dumps                 | 5.61 ms                                                         | 6.32 ms: 1.12x slower                                                      |
| dulwich_log                | 38.0 ms                                                         | 42.9 ms: 1.13x slower                                                      |
| sympy_expand               | 271 ms                                                          | 305 ms: 1.13x slower                                                       |
| html5lib                   | 35.0 ms                                                         | 39.7 ms: 1.13x slower                                                      |
| spectral_norm              | 63.7 ms                                                         | 72.2 ms: 1.13x slower                                                      |
| genshi_xml                 | 31.6 ms                                                         | 35.9 ms: 1.14x slower                                                      |
| meteor_contest             | 69.9 ms                                                         | 79.5 ms: 1.14x slower                                                      |
| asyncio_tcp                | 471 ms                                                          | 536 ms: 1.14x slower                                                       |
| nqueens                    | 56.7 ms                                                         | 64.7 ms: 1.14x slower                                                      |
| mdp                        | 1.31 sec                                                        | 1.50 sec: 1.14x slower                                                     |
| tornado_http               | 81.8 ms                                                         | 93.8 ms: 1.15x slower                                                      |
| coroutines                 | 12.8 ms                                                         | 14.6 ms: 1.15x slower                                                      |
| scimark_lu                 | 56.6 ms                                                         | 65.3 ms: 1.15x slower                                                      |
| chaos                      | 38.4 ms                                                         | 44.4 ms: 1.16x slower                                                      |
| xml_etree_process          | 36.4 ms                                                         | 42.3 ms: 1.16x slower                                                      |
| scimark_sparse_mat_mult    | 2.50 ms                                                         | 2.92 ms: 1.17x slower                                                      |
| comprehensions             | 10.4 us                                                         | 12.1 us: 1.17x slower                                                      |
| pyflate                    | 279 ms                                                          | 327 ms: 1.17x slower                                                       |
| django_template            | 21.7 ms                                                         | 25.5 ms: 1.18x slower                                                      |
| float                      | 49.7 ms                                                         | 58.6 ms: 1.18x slower                                                      |
| regex_compile              | 78.0 ms                                                         | 92.4 ms: 1.18x slower                                                      |
| coverage                   | 42.1 ms                                                         | 49.9 ms: 1.19x slower                                                      |
| sqlglot_transpile          | 955 us                                                          | 1.13 ms: 1.19x slower                                                      |
| pprint_pformat             | 966 ms                                                          | 1.15 sec: 1.19x slower                                                     |
| genshi_text                | 14.4 ms                                                         | 17.2 ms: 1.19x slower                                                      |
| pprint_safe_repr           | 474 ms                                                          | 569 ms: 1.20x slower                                                       |
| tomli_loads                | 1.35 sec                                                        | 1.62 sec: 1.20x slower                                                     |
| deltablue                  | 1.88 ms                                                         | 2.28 ms: 1.21x slower                                                      |
| hexiom                     | 3.72 ms                                                         | 4.52 ms: 1.21x slower                                                      |
| sqlglot_parse              | 748 us                                                          | 910 us: 1.22x slower                                                       |
| richards                   | 26.7 ms                                                         | 32.5 ms: 1.22x slower                                                      |
| raytrace                   | 162 ms                                                          | 198 ms: 1.22x slower                                                       |
| pickle_pure_python         | 175 us                                                          | 214 us: 1.22x slower                                                       |
| logging_silent             | 52.9 ns                                                         | 64.8 ns: 1.23x slower                                                      |
| fannkuch                   | 243 ms                                                          | 300 ms: 1.23x slower                                                       |
| richards_super             | 30.2 ms                                                         | 37.2 ms: 1.23x slower                                                      |
| scimark_sor                | 75.3 ms                                                         | 93.8 ms: 1.24x slower                                                      |
| scimark_fft                | 171 ms                                                          | 214 ms: 1.25x slower                                                       |
| unpickle_pure_python       | 122 us                                                          | 155 us: 1.28x slower                                                       |
| nbody                      | 67.6 ms                                                         | 87.8 ms: 1.30x slower                                                      |
| scimark_monte_carlo        | 39.1 ms                                                         | 51.6 ms: 1.32x slower                                                      |
| Geometric mean             | (ref)                                                           | 1.08x slower                                                               |

Benchmark hidden because not significant (7): async_tree_memoization_tg, async_tree_io, async_tree_memoization, regex_effbot, regex_v8, async_tree_cpu_io_mixed, async_tree_none_tg
Ignored benchmarks (10) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.11x
- 95% likely to have a slowdown of 1.10x
- 99% likely to have a slowdown of 1.08x

# Memory
- memory change: unknown