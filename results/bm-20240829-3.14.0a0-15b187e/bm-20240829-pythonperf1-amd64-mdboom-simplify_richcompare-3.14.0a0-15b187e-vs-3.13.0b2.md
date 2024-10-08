# Results vs. 3.13.0b2

- fork: mdboom
- ref: simplify_richcompare
- machine: windows-amd64
- commit hash: 15b187e
- commit date: 2024-08-29
- overall geometric mean: 1.06x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 228 ms: 1.10x slower                                                       |
| docutils       | 1.63 sec                                                        | 1.70 sec: 1.04x slower                                                     |
| html5lib       | 35.0 ms                                                         | 39.9 ms: 1.14x slower                                                      |
| tornado_http   | 81.8 ms                                                         | 93.1 ms: 1.14x slower                                                      |
| Geometric mean | (ref)                                                           | 1.11x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 605 ms                                                          | 560 ms: 1.08x faster                                                       |
| async_tree_none            | 218 ms                                                          | 210 ms: 1.04x faster                                                       |
| async_tree_cpu_io_mixed_tg | 382 ms                                                          | 401 ms: 1.05x slower                                                       |
| Geometric mean             | (ref)                                                           | 1.02x faster                                                               |

Benchmark hidden because not significant (5): async_tree_memoization, async_tree_memoization_tg, async_tree_io, async_tree_none_tg, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 150 ms                                                          | 151 ms: 1.01x slower                                                       |
| float          | 49.7 ms                                                         | 55.9 ms: 1.12x slower                                                      |
| nbody          | 67.6 ms                                                         | 82.8 ms: 1.22x slower                                                      |
| Geometric mean | (ref)                                                           | 1.12x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 1.58 ms                                                         | 1.61 ms: 1.01x slower                                                      |
| regex_dna      | 119 ms                                                          | 123 ms: 1.04x slower                                                       |
| regex_compile  | 78.0 ms                                                         | 90.9 ms: 1.17x slower                                                      |
| Geometric mean | (ref)                                                           | 1.05x slower                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_loads           | 14.2 us                                                         | 14.5 us: 1.03x slower                                                      |
| xml_etree_parse      | 90.9 ms                                                         | 95.0 ms: 1.04x slower                                                      |
| xml_etree_iterparse  | 62.3 ms                                                         | 66.1 ms: 1.06x slower                                                      |
| xml_etree_generate   | 53.2 ms                                                         | 57.7 ms: 1.09x slower                                                      |
| xml_etree_process    | 36.4 ms                                                         | 40.5 ms: 1.11x slower                                                      |
| json_dumps           | 5.61 ms                                                         | 6.25 ms: 1.11x slower                                                      |
| tomli_loads          | 1.35 sec                                                        | 1.58 sec: 1.17x slower                                                     |
| pickle_pure_python   | 175 us                                                          | 210 us: 1.20x slower                                                       |
| unpickle_pure_python | 122 us                                                          | 149 us: 1.23x slower                                                       |
| Geometric mean       | (ref)                                                           | 1.11x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.3 ms                                                         | 22.3 ms: 1.10x slower                                                      |
| python_startup_no_site | 16.2 ms                                                         | 18.2 ms: 1.12x slower                                                      |
| Geometric mean         | (ref)                                                           | 1.11x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.36 ms                                                         | 6.90 ms: 1.09x slower                                                      |
| django_template | 21.7 ms                                                         | 24.3 ms: 1.12x slower                                                      |
| genshi_xml      | 31.6 ms                                                         | 36.1 ms: 1.14x slower                                                      |
| genshi_text     | 14.4 ms                                                         | 16.9 ms: 1.17x slower                                                      |
| Geometric mean  | (ref)                                                           | 1.13x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.11 ms                                                         | 514 us: 15.79x faster                                                      |
| deepcopy                   | 220 us                                                          | 186 us: 1.18x faster                                                       |
| deepcopy_memo              | 22.1 us                                                         | 20.0 us: 1.10x faster                                                      |
| async_tree_io_tg           | 605 ms                                                          | 560 ms: 1.08x faster                                                       |
| deepcopy_reduce            | 1.99 us                                                         | 1.92 us: 1.04x faster                                                      |
| async_tree_none            | 218 ms                                                          | 210 ms: 1.04x faster                                                       |
| pidigits                   | 150 ms                                                          | 151 ms: 1.01x slower                                                       |
| regex_effbot               | 1.58 ms                                                         | 1.61 ms: 1.01x slower                                                      |
| json_loads                 | 14.2 us                                                         | 14.5 us: 1.03x slower                                                      |
| create_gc_cycles           | 888 us                                                          | 917 us: 1.03x slower                                                       |
| spectral_norm              | 63.7 ms                                                         | 66.0 ms: 1.04x slower                                                      |
| regex_dna                  | 119 ms                                                          | 123 ms: 1.04x slower                                                       |
| go                         | 82.1 ms                                                         | 85.1 ms: 1.04x slower                                                      |
| docutils                   | 1.63 sec                                                        | 1.70 sec: 1.04x slower                                                     |
| xml_etree_parse            | 90.9 ms                                                         | 95.0 ms: 1.04x slower                                                      |
| pathlib                    | 75.9 ms                                                         | 79.2 ms: 1.04x slower                                                      |
| async_tree_cpu_io_mixed_tg | 382 ms                                                          | 401 ms: 1.05x slower                                                       |
| scimark_sparse_mat_mult    | 2.50 ms                                                         | 2.63 ms: 1.05x slower                                                      |
| xml_etree_iterparse        | 62.3 ms                                                         | 66.1 ms: 1.06x slower                                                      |
| sympy_sum                  | 84.4 ms                                                         | 89.6 ms: 1.06x slower                                                      |
| crypto_pyaes               | 45.5 ms                                                         | 48.5 ms: 1.07x slower                                                      |
| generators                 | 19.6 ms                                                         | 21.1 ms: 1.08x slower                                                      |
| bench_thread_pool          | 768 us                                                          | 828 us: 1.08x slower                                                       |
| sympy_integrate            | 12.2 ms                                                         | 13.2 ms: 1.08x slower                                                      |
| scimark_lu                 | 56.6 ms                                                         | 61.2 ms: 1.08x slower                                                      |
| mako                       | 6.36 ms                                                         | 6.90 ms: 1.09x slower                                                      |
| xml_etree_generate         | 53.2 ms                                                         | 57.7 ms: 1.09x slower                                                      |
| bench_mp_pool              | 64.8 ms                                                         | 70.6 ms: 1.09x slower                                                      |
| async_generators           | 223 ms                                                          | 243 ms: 1.09x slower                                                       |
| sqlglot_optimize           | 32.7 ms                                                         | 35.9 ms: 1.10x slower                                                      |
| typing_runtime_protocols   | 101 us                                                          | 111 us: 1.10x slower                                                       |
| pylint                     | 205 ms                                                          | 224 ms: 1.10x slower                                                       |
| python_startup             | 20.3 ms                                                         | 22.3 ms: 1.10x slower                                                      |
| 2to3                       | 207 ms                                                          | 228 ms: 1.10x slower                                                       |
| sqlglot_normalize          | 173 ms                                                          | 191 ms: 1.10x slower                                                       |
| pycparser                  | 754 ms                                                          | 833 ms: 1.10x slower                                                       |
| sympy_str                  | 159 ms                                                          | 176 ms: 1.11x slower                                                       |
| coroutines                 | 12.8 ms                                                         | 14.2 ms: 1.11x slower                                                      |
| logging_format             | 6.22 us                                                         | 6.91 us: 1.11x slower                                                      |
| xml_etree_process          | 36.4 ms                                                         | 40.5 ms: 1.11x slower                                                      |
| json_dumps                 | 5.61 ms                                                         | 6.25 ms: 1.11x slower                                                      |
| logging_simple             | 5.78 us                                                         | 6.45 us: 1.11x slower                                                      |
| dulwich_log                | 38.0 ms                                                         | 42.5 ms: 1.12x slower                                                      |
| chaos                      | 38.4 ms                                                         | 42.8 ms: 1.12x slower                                                      |
| sympy_expand               | 271 ms                                                          | 303 ms: 1.12x slower                                                       |
| django_template            | 21.7 ms                                                         | 24.3 ms: 1.12x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                         | 18.2 ms: 1.12x slower                                                      |
| asyncio_tcp                | 471 ms                                                          | 529 ms: 1.12x slower                                                       |
| meteor_contest             | 69.9 ms                                                         | 78.5 ms: 1.12x slower                                                      |
| asyncio_tcp_ssl            | 1.48 sec                                                        | 1.66 sec: 1.12x slower                                                     |
| float                      | 49.7 ms                                                         | 55.9 ms: 1.12x slower                                                      |
| nqueens                    | 56.7 ms                                                         | 63.8 ms: 1.13x slower                                                      |
| telco                      | 4.67 ms                                                         | 5.30 ms: 1.14x slower                                                      |
| tornado_http               | 81.8 ms                                                         | 93.1 ms: 1.14x slower                                                      |
| html5lib                   | 35.0 ms                                                         | 39.9 ms: 1.14x slower                                                      |
| raytrace                   | 162 ms                                                          | 185 ms: 1.14x slower                                                       |
| genshi_xml                 | 31.6 ms                                                         | 36.1 ms: 1.14x slower                                                      |
| mdp                        | 1.31 sec                                                        | 1.50 sec: 1.14x slower                                                     |
| comprehensions             | 10.4 us                                                         | 11.9 us: 1.15x slower                                                      |
| pyflate                    | 279 ms                                                          | 321 ms: 1.15x slower                                                       |
| scimark_fft                | 171 ms                                                          | 197 ms: 1.15x slower                                                       |
| sqlglot_transpile          | 955 us                                                          | 1.10 ms: 1.15x slower                                                      |
| coverage                   | 42.1 ms                                                         | 48.7 ms: 1.16x slower                                                      |
| pprint_safe_repr           | 474 ms                                                          | 551 ms: 1.16x slower                                                       |
| pprint_pformat             | 966 ms                                                          | 1.12 sec: 1.16x slower                                                     |
| regex_compile              | 78.0 ms                                                         | 90.9 ms: 1.17x slower                                                      |
| tomli_loads                | 1.35 sec                                                        | 1.58 sec: 1.17x slower                                                     |
| genshi_text                | 14.4 ms                                                         | 16.9 ms: 1.17x slower                                                      |
| hexiom                     | 3.72 ms                                                         | 4.37 ms: 1.17x slower                                                      |
| fannkuch                   | 243 ms                                                          | 288 ms: 1.18x slower                                                       |
| sqlglot_parse              | 748 us                                                          | 886 us: 1.18x slower                                                       |
| scimark_sor                | 75.3 ms                                                         | 89.4 ms: 1.19x slower                                                      |
| richards                   | 26.7 ms                                                         | 31.8 ms: 1.19x slower                                                      |
| richards_super             | 30.2 ms                                                         | 36.0 ms: 1.19x slower                                                      |
| pickle_pure_python         | 175 us                                                          | 210 us: 1.20x slower                                                       |
| deltablue                  | 1.88 ms                                                         | 2.26 ms: 1.20x slower                                                      |
| logging_silent             | 52.9 ns                                                         | 63.7 ns: 1.20x slower                                                      |
| nbody                      | 67.6 ms                                                         | 82.8 ms: 1.22x slower                                                      |
| unpickle_pure_python       | 122 us                                                          | 149 us: 1.23x slower                                                       |
| scimark_monte_carlo        | 39.1 ms                                                         | 49.0 ms: 1.25x slower                                                      |
| Geometric mean             | (ref)                                                           | 1.06x slower                                                               |

Benchmark hidden because not significant (8): json, async_tree_memoization, async_tree_memoization_tg, async_tree_io, regex_v8, async_tree_none_tg, gc_traversal, async_tree_cpu_io_mixed
Ignored benchmarks (10) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.08x
- 95% likely to have a slowdown of 1.08x
- 99% likely to have a slowdown of 1.07x

# Memory
- memory change: unknown