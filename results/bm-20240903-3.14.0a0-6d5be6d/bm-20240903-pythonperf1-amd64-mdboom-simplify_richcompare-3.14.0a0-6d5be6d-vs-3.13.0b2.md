# Results vs. 3.13.0b2

- fork: mdboom
- ref: simplify_richcompare
- machine: windows-amd64
- commit hash: 6d5be6d
- commit date: 2024-09-03
- overall geometric mean: 1.05x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240903-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 227 ms: 1.10x slower                                                       |
| docutils       | 1.63 sec                                                        | 1.71 sec: 1.05x slower                                                     |
| html5lib       | 35.0 ms                                                         | 40.5 ms: 1.16x slower                                                      |
| tornado_http   | 81.8 ms                                                         | 93.6 ms: 1.14x slower                                                      |
| Geometric mean | (ref)                                                           | 1.11x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240903-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 605 ms                                                          | 558 ms: 1.08x faster                                                       |
| async_tree_none            | 218 ms                                                          | 208 ms: 1.05x faster                                                       |
| async_tree_memoization     | 264 ms                                                          | 255 ms: 1.04x faster                                                       |
| async_tree_cpu_io_mixed_tg | 382 ms                                                          | 399 ms: 1.04x slower                                                       |
| Geometric mean             | (ref)                                                           | 1.02x faster                                                               |

Benchmark hidden because not significant (4): async_tree_io, async_tree_memoization_tg, async_tree_none_tg, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240903-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 150 ms                                                          | 151 ms: 1.01x slower                                                       |
| float          | 49.7 ms                                                         | 56.5 ms: 1.14x slower                                                      |
| nbody          | 67.6 ms                                                         | 80.9 ms: 1.20x slower                                                      |
| Geometric mean | (ref)                                                           | 1.11x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240903-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 119 ms                                                          | 120 ms: 1.01x slower                                                       |
| regex_compile  | 78.0 ms                                                         | 91.4 ms: 1.17x slower                                                      |
| Geometric mean | (ref)                                                           | 1.03x slower                                                               |

Benchmark hidden because not significant (2): regex_v8, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240903-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_loads           | 14.2 us                                                         | 14.4 us: 1.02x slower                                                      |
| xml_etree_parse      | 90.9 ms                                                         | 94.7 ms: 1.04x slower                                                      |
| xml_etree_iterparse  | 62.3 ms                                                         | 66.1 ms: 1.06x slower                                                      |
| xml_etree_generate   | 53.2 ms                                                         | 58.5 ms: 1.10x slower                                                      |
| json_dumps           | 5.61 ms                                                         | 6.28 ms: 1.12x slower                                                      |
| xml_etree_process    | 36.4 ms                                                         | 41.5 ms: 1.14x slower                                                      |
| tomli_loads          | 1.35 sec                                                        | 1.58 sec: 1.17x slower                                                     |
| pickle_pure_python   | 175 us                                                          | 210 us: 1.20x slower                                                       |
| unpickle_pure_python | 122 us                                                          | 148 us: 1.22x slower                                                       |
| Geometric mean       | (ref)                                                           | 1.12x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240903-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.3 ms                                                         | 22.0 ms: 1.08x slower                                                      |
| python_startup_no_site | 16.2 ms                                                         | 18.1 ms: 1.12x slower                                                      |
| Geometric mean         | (ref)                                                           | 1.10x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240903-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.36 ms                                                         | 6.92 ms: 1.09x slower                                                      |
| genshi_xml      | 31.6 ms                                                         | 35.7 ms: 1.13x slower                                                      |
| django_template | 21.7 ms                                                         | 24.9 ms: 1.15x slower                                                      |
| genshi_text     | 14.4 ms                                                         | 17.0 ms: 1.18x slower                                                      |
| Geometric mean  | (ref)                                                           | 1.14x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240903-pythonperf1-amd64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.11 ms                                                         | 522 us: 15.53x faster                                                      |
| deepcopy                   | 220 us                                                          | 189 us: 1.16x faster                                                       |
| deepcopy_memo              | 22.1 us                                                         | 19.9 us: 1.11x faster                                                      |
| async_tree_io_tg           | 605 ms                                                          | 558 ms: 1.08x faster                                                       |
| async_tree_none            | 218 ms                                                          | 208 ms: 1.05x faster                                                       |
| deepcopy_reduce            | 1.99 us                                                         | 1.92 us: 1.04x faster                                                      |
| async_tree_memoization     | 264 ms                                                          | 255 ms: 1.04x faster                                                       |
| pidigits                   | 150 ms                                                          | 151 ms: 1.01x slower                                                       |
| regex_dna                  | 119 ms                                                          | 120 ms: 1.01x slower                                                       |
| json_loads                 | 14.2 us                                                         | 14.4 us: 1.02x slower                                                      |
| create_gc_cycles           | 888 us                                                          | 908 us: 1.02x slower                                                       |
| go                         | 82.1 ms                                                         | 84.5 ms: 1.03x slower                                                      |
| pathlib                    | 75.9 ms                                                         | 78.8 ms: 1.04x slower                                                      |
| xml_etree_parse            | 90.9 ms                                                         | 94.7 ms: 1.04x slower                                                      |
| async_tree_cpu_io_mixed_tg | 382 ms                                                          | 399 ms: 1.04x slower                                                       |
| docutils                   | 1.63 sec                                                        | 1.71 sec: 1.05x slower                                                     |
| spectral_norm              | 63.7 ms                                                         | 67.1 ms: 1.05x slower                                                      |
| crypto_pyaes               | 45.5 ms                                                         | 47.9 ms: 1.05x slower                                                      |
| bench_mp_pool              | 64.8 ms                                                         | 68.5 ms: 1.06x slower                                                      |
| xml_etree_iterparse        | 62.3 ms                                                         | 66.1 ms: 1.06x slower                                                      |
| generators                 | 19.6 ms                                                         | 20.8 ms: 1.06x slower                                                      |
| bench_thread_pool          | 768 us                                                          | 816 us: 1.06x slower                                                       |
| sympy_sum                  | 84.4 ms                                                         | 89.9 ms: 1.07x slower                                                      |
| sympy_integrate            | 12.2 ms                                                         | 13.2 ms: 1.08x slower                                                      |
| telco                      | 4.67 ms                                                         | 5.03 ms: 1.08x slower                                                      |
| scimark_sparse_mat_mult    | 2.50 ms                                                         | 2.70 ms: 1.08x slower                                                      |
| python_startup             | 20.3 ms                                                         | 22.0 ms: 1.08x slower                                                      |
| mako                       | 6.36 ms                                                         | 6.92 ms: 1.09x slower                                                      |
| logging_format             | 6.22 us                                                         | 6.82 us: 1.10x slower                                                      |
| 2to3                       | 207 ms                                                          | 227 ms: 1.10x slower                                                       |
| coroutines                 | 12.8 ms                                                         | 14.0 ms: 1.10x slower                                                      |
| sqlglot_optimize           | 32.7 ms                                                         | 35.9 ms: 1.10x slower                                                      |
| xml_etree_generate         | 53.2 ms                                                         | 58.5 ms: 1.10x slower                                                      |
| sqlglot_normalize          | 173 ms                                                          | 190 ms: 1.10x slower                                                       |
| meteor_contest             | 69.9 ms                                                         | 77.0 ms: 1.10x slower                                                      |
| typing_runtime_protocols   | 101 us                                                          | 111 us: 1.10x slower                                                       |
| logging_simple             | 5.78 us                                                         | 6.38 us: 1.10x slower                                                      |
| async_generators           | 223 ms                                                          | 247 ms: 1.11x slower                                                       |
| scimark_lu                 | 56.6 ms                                                         | 62.6 ms: 1.11x slower                                                      |
| sympy_str                  | 159 ms                                                          | 177 ms: 1.11x slower                                                       |
| pylint                     | 205 ms                                                          | 228 ms: 1.11x slower                                                       |
| python_startup_no_site     | 16.2 ms                                                         | 18.1 ms: 1.12x slower                                                      |
| chaos                      | 38.4 ms                                                         | 42.8 ms: 1.12x slower                                                      |
| json_dumps                 | 5.61 ms                                                         | 6.28 ms: 1.12x slower                                                      |
| dulwich_log                | 38.0 ms                                                         | 42.8 ms: 1.13x slower                                                      |
| sympy_expand               | 271 ms                                                          | 305 ms: 1.13x slower                                                       |
| asyncio_tcp                | 471 ms                                                          | 532 ms: 1.13x slower                                                       |
| nqueens                    | 56.7 ms                                                         | 64.0 ms: 1.13x slower                                                      |
| genshi_xml                 | 31.6 ms                                                         | 35.7 ms: 1.13x slower                                                      |
| float                      | 49.7 ms                                                         | 56.5 ms: 1.14x slower                                                      |
| xml_etree_process          | 36.4 ms                                                         | 41.5 ms: 1.14x slower                                                      |
| tornado_http               | 81.8 ms                                                         | 93.6 ms: 1.14x slower                                                      |
| comprehensions             | 10.4 us                                                         | 11.9 us: 1.15x slower                                                      |
| pprint_safe_repr           | 474 ms                                                          | 543 ms: 1.15x slower                                                       |
| django_template            | 21.7 ms                                                         | 24.9 ms: 1.15x slower                                                      |
| html5lib                   | 35.0 ms                                                         | 40.5 ms: 1.16x slower                                                      |
| pprint_pformat             | 966 ms                                                          | 1.12 sec: 1.16x slower                                                     |
| sqlglot_transpile          | 955 us                                                          | 1.11 ms: 1.16x slower                                                      |
| coverage                   | 42.1 ms                                                         | 48.7 ms: 1.16x slower                                                      |
| pyflate                    | 279 ms                                                          | 323 ms: 1.16x slower                                                       |
| hexiom                     | 3.72 ms                                                         | 4.32 ms: 1.16x slower                                                      |
| scimark_sor                | 75.3 ms                                                         | 87.7 ms: 1.16x slower                                                      |
| regex_compile              | 78.0 ms                                                         | 91.4 ms: 1.17x slower                                                      |
| tomli_loads                | 1.35 sec                                                        | 1.58 sec: 1.17x slower                                                     |
| raytrace                   | 162 ms                                                          | 191 ms: 1.18x slower                                                       |
| sqlglot_parse              | 748 us                                                          | 884 us: 1.18x slower                                                       |
| genshi_text                | 14.4 ms                                                         | 17.0 ms: 1.18x slower                                                      |
| richards                   | 26.7 ms                                                         | 31.6 ms: 1.18x slower                                                      |
| deltablue                  | 1.88 ms                                                         | 2.23 ms: 1.18x slower                                                      |
| fannkuch                   | 243 ms                                                          | 288 ms: 1.19x slower                                                       |
| logging_silent             | 52.9 ns                                                         | 62.7 ns: 1.19x slower                                                      |
| mdp                        | 1.31 sec                                                        | 1.56 sec: 1.19x slower                                                     |
| nbody                      | 67.6 ms                                                         | 80.9 ms: 1.20x slower                                                      |
| richards_super             | 30.2 ms                                                         | 36.1 ms: 1.20x slower                                                      |
| pickle_pure_python         | 175 us                                                          | 210 us: 1.20x slower                                                       |
| scimark_fft                | 171 ms                                                          | 207 ms: 1.21x slower                                                       |
| unpickle_pure_python       | 122 us                                                          | 148 us: 1.22x slower                                                       |
| scimark_monte_carlo        | 39.1 ms                                                         | 49.2 ms: 1.26x slower                                                      |
| Geometric mean             | (ref)                                                           | 1.05x slower                                                               |

Benchmark hidden because not significant (10): regex_v8, async_tree_io, json, async_tree_memoization_tg, pycparser, async_tree_none_tg, regex_effbot, async_tree_cpu_io_mixed, gc_traversal, asyncio_tcp_ssl
Ignored benchmarks (10) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.08x
- 95% likely to have a slowdown of 1.08x
- 99% likely to have a slowdown of 1.07x

# Memory
- memory change: unknown