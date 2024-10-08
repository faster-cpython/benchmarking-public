# Results vs. 3.13.0b2

- fork: mdboom
- ref: pysequence_tuple
- machine: windows-amd64
- commit hash: 3b5fdc8
- commit date: 2024-09-11
- overall geometric mean: 1.05x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-pythonperf1-amd64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 222 ms: 1.07x slower                                                   |
| docutils       | 1.63 sec                                                        | 1.70 sec: 1.05x slower                                                 |
| html5lib       | 35.0 ms                                                         | 40.3 ms: 1.15x slower                                                  |
| tornado_http   | 81.8 ms                                                         | 84.1 ms: 1.03x slower                                                  |
| Geometric mean | (ref)                                                           | 1.07x slower                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-pythonperf1-amd64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 605 ms                                                          | 560 ms: 1.08x faster                                                   |
| async_tree_none            | 218 ms                                                          | 205 ms: 1.06x faster                                                   |
| async_tree_io              | 588 ms                                                          | 566 ms: 1.04x faster                                                   |
| async_tree_memoization     | 264 ms                                                          | 259 ms: 1.02x faster                                                   |
| async_tree_cpu_io_mixed_tg | 382 ms                                                          | 395 ms: 1.03x slower                                                   |
| Geometric mean             | (ref)                                                           | 1.02x faster                                                           |

Benchmark hidden because not significant (3): async_tree_memoization_tg, async_tree_none_tg, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-pythonperf1-amd64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------:|
| pidigits       | 150 ms                                                          | 151 ms: 1.00x slower                                                   |
| float          | 49.7 ms                                                         | 56.6 ms: 1.14x slower                                                  |
| nbody          | 67.6 ms                                                         | 81.8 ms: 1.21x slower                                                  |
| Geometric mean | (ref)                                                           | 1.11x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-pythonperf1-amd64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_dna      | 119 ms                                                          | 121 ms: 1.02x slower                                                   |
| regex_compile  | 78.0 ms                                                         | 91.5 ms: 1.17x slower                                                  |
| Geometric mean | (ref)                                                           | 1.04x slower                                                           |

Benchmark hidden because not significant (2): regex_v8, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-pythonperf1-amd64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle               | 7.11 us                                                         | 7.17 us: 1.01x slower                                                  |
| json_loads           | 14.2 us                                                         | 14.6 us: 1.03x slower                                                  |
| pickle_list          | 2.90 us                                                         | 2.99 us: 1.03x slower                                                  |
| pickle_dict          | 18.1 us                                                         | 18.7 us: 1.03x slower                                                  |
| xml_etree_parse      | 90.9 ms                                                         | 93.8 ms: 1.03x slower                                                  |
| unpickle_list        | 2.62 us                                                         | 2.72 us: 1.04x slower                                                  |
| xml_etree_iterparse  | 62.3 ms                                                         | 65.1 ms: 1.04x slower                                                  |
| xml_etree_generate   | 53.2 ms                                                         | 58.6 ms: 1.10x slower                                                  |
| unpickle             | 8.40 us                                                         | 9.28 us: 1.11x slower                                                  |
| json_dumps           | 5.61 ms                                                         | 6.23 ms: 1.11x slower                                                  |
| xml_etree_process    | 36.4 ms                                                         | 40.8 ms: 1.12x slower                                                  |
| tomli_loads          | 1.35 sec                                                        | 1.59 sec: 1.18x slower                                                 |
| pickle_pure_python   | 175 us                                                          | 212 us: 1.21x slower                                                   |
| unpickle_pure_python | 122 us                                                          | 153 us: 1.25x slower                                                   |
| Geometric mean       | (ref)                                                           | 1.09x slower                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-pythonperf1-amd64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 20.3 ms                                                         | 21.4 ms: 1.06x slower                                                  |
| python_startup_no_site | 16.2 ms                                                         | 17.5 ms: 1.08x slower                                                  |
| Geometric mean         | (ref)                                                           | 1.07x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-pythonperf1-amd64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|-----------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 6.36 ms                                                         | 6.89 ms: 1.08x slower                                                  |
| django_template | 21.7 ms                                                         | 24.9 ms: 1.15x slower                                                  |
| genshi_xml      | 31.6 ms                                                         | 37.4 ms: 1.18x slower                                                  |
| genshi_text     | 14.4 ms                                                         | 17.3 ms: 1.20x slower                                                  |
| Geometric mean  | (ref)                                                           | 1.15x slower                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-pythonperf1-amd64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------------------|:---------------------------------------------------------------:|:----------------------------------------------------------------------:|
| thrift                     | 8.11 ms                                                         | 544 us: 14.90x faster                                                  |
| deepcopy                   | 220 us                                                          | 188 us: 1.17x faster                                                   |
| async_tree_io_tg           | 605 ms                                                          | 560 ms: 1.08x faster                                                   |
| deepcopy_memo              | 22.1 us                                                         | 20.6 us: 1.07x faster                                                  |
| async_tree_none            | 218 ms                                                          | 205 ms: 1.06x faster                                                   |
| deepcopy_reduce            | 1.99 us                                                         | 1.92 us: 1.04x faster                                                  |
| async_tree_io              | 588 ms                                                          | 566 ms: 1.04x faster                                                   |
| pathlib                    | 75.9 ms                                                         | 73.5 ms: 1.03x faster                                                  |
| gc_traversal               | 1.55 ms                                                         | 1.52 ms: 1.02x faster                                                  |
| async_tree_memoization     | 264 ms                                                          | 259 ms: 1.02x faster                                                   |
| create_gc_cycles           | 888 us                                                          | 878 us: 1.01x faster                                                   |
| pidigits                   | 150 ms                                                          | 151 ms: 1.00x slower                                                   |
| pickle                     | 7.11 us                                                         | 7.17 us: 1.01x slower                                                  |
| sqlite_synth               | 1.60 us                                                         | 1.62 us: 1.02x slower                                                  |
| regex_dna                  | 119 ms                                                          | 121 ms: 1.02x slower                                                   |
| tornado_http               | 81.8 ms                                                         | 84.1 ms: 1.03x slower                                                  |
| bench_mp_pool              | 64.8 ms                                                         | 66.6 ms: 1.03x slower                                                  |
| json_loads                 | 14.2 us                                                         | 14.6 us: 1.03x slower                                                  |
| pickle_list                | 2.90 us                                                         | 2.99 us: 1.03x slower                                                  |
| pickle_dict                | 18.1 us                                                         | 18.7 us: 1.03x slower                                                  |
| xml_etree_parse            | 90.9 ms                                                         | 93.8 ms: 1.03x slower                                                  |
| async_tree_cpu_io_mixed_tg | 382 ms                                                          | 395 ms: 1.03x slower                                                   |
| unpickle_list              | 2.62 us                                                         | 2.72 us: 1.04x slower                                                  |
| xml_etree_iterparse        | 62.3 ms                                                         | 65.1 ms: 1.04x slower                                                  |
| docutils                   | 1.63 sec                                                        | 1.70 sec: 1.05x slower                                                 |
| bench_thread_pool          | 768 us                                                          | 805 us: 1.05x slower                                                   |
| python_startup             | 20.3 ms                                                         | 21.4 ms: 1.06x slower                                                  |
| crypto_pyaes               | 45.5 ms                                                         | 48.1 ms: 1.06x slower                                                  |
| go                         | 82.1 ms                                                         | 87.3 ms: 1.06x slower                                                  |
| async_generators           | 223 ms                                                          | 239 ms: 1.07x slower                                                   |
| 2to3                       | 207 ms                                                          | 222 ms: 1.07x slower                                                   |
| generators                 | 19.6 ms                                                         | 21.0 ms: 1.08x slower                                                  |
| python_startup_no_site     | 16.2 ms                                                         | 17.5 ms: 1.08x slower                                                  |
| sympy_sum                  | 84.4 ms                                                         | 91.2 ms: 1.08x slower                                                  |
| sympy_integrate            | 12.2 ms                                                         | 13.2 ms: 1.08x slower                                                  |
| spectral_norm              | 63.7 ms                                                         | 69.0 ms: 1.08x slower                                                  |
| mako                       | 6.36 ms                                                         | 6.89 ms: 1.08x slower                                                  |
| scimark_sparse_mat_mult    | 2.50 ms                                                         | 2.72 ms: 1.09x slower                                                  |
| typing_runtime_protocols   | 101 us                                                          | 111 us: 1.10x slower                                                   |
| coroutines                 | 12.8 ms                                                         | 14.0 ms: 1.10x slower                                                  |
| xml_etree_generate         | 53.2 ms                                                         | 58.6 ms: 1.10x slower                                                  |
| pylint                     | 205 ms                                                          | 226 ms: 1.10x slower                                                   |
| logging_simple             | 5.78 us                                                         | 6.39 us: 1.10x slower                                                  |
| unpickle                   | 8.40 us                                                         | 9.28 us: 1.11x slower                                                  |
| telco                      | 4.67 ms                                                         | 5.16 ms: 1.11x slower                                                  |
| logging_format             | 6.22 us                                                         | 6.88 us: 1.11x slower                                                  |
| json_dumps                 | 5.61 ms                                                         | 6.23 ms: 1.11x slower                                                  |
| sqlglot_normalize          | 173 ms                                                          | 193 ms: 1.11x slower                                                   |
| meteor_contest             | 69.9 ms                                                         | 77.9 ms: 1.11x slower                                                  |
| coverage                   | 42.1 ms                                                         | 46.9 ms: 1.11x slower                                                  |
| sqlglot_optimize           | 32.7 ms                                                         | 36.5 ms: 1.12x slower                                                  |
| dulwich_log                | 38.0 ms                                                         | 42.6 ms: 1.12x slower                                                  |
| xml_etree_process          | 36.4 ms                                                         | 40.8 ms: 1.12x slower                                                  |
| sympy_str                  | 159 ms                                                          | 178 ms: 1.12x slower                                                   |
| scimark_lu                 | 56.6 ms                                                         | 63.6 ms: 1.12x slower                                                  |
| comprehensions             | 10.4 us                                                         | 11.7 us: 1.12x slower                                                  |
| nqueens                    | 56.7 ms                                                         | 63.7 ms: 1.12x slower                                                  |
| sympy_expand               | 271 ms                                                          | 307 ms: 1.14x slower                                                   |
| chaos                      | 38.4 ms                                                         | 43.7 ms: 1.14x slower                                                  |
| float                      | 49.7 ms                                                         | 56.6 ms: 1.14x slower                                                  |
| mdp                        | 1.31 sec                                                        | 1.50 sec: 1.14x slower                                                 |
| pyflate                    | 279 ms                                                          | 319 ms: 1.14x slower                                                   |
| pprint_pformat             | 966 ms                                                          | 1.11 sec: 1.15x slower                                                 |
| html5lib                   | 35.0 ms                                                         | 40.3 ms: 1.15x slower                                                  |
| django_template            | 21.7 ms                                                         | 24.9 ms: 1.15x slower                                                  |
| pprint_safe_repr           | 474 ms                                                          | 546 ms: 1.15x slower                                                   |
| raytrace                   | 162 ms                                                          | 188 ms: 1.16x slower                                                   |
| sqlglot_transpile          | 955 us                                                          | 1.12 ms: 1.17x slower                                                  |
| regex_compile              | 78.0 ms                                                         | 91.5 ms: 1.17x slower                                                  |
| scimark_sor                | 75.3 ms                                                         | 88.8 ms: 1.18x slower                                                  |
| hexiom                     | 3.72 ms                                                         | 4.39 ms: 1.18x slower                                                  |
| tomli_loads                | 1.35 sec                                                        | 1.59 sec: 1.18x slower                                                 |
| logging_silent             | 52.9 ns                                                         | 62.6 ns: 1.18x slower                                                  |
| genshi_xml                 | 31.6 ms                                                         | 37.4 ms: 1.18x slower                                                  |
| scimark_fft                | 171 ms                                                          | 203 ms: 1.19x slower                                                   |
| fannkuch                   | 243 ms                                                          | 292 ms: 1.20x slower                                                   |
| deltablue                  | 1.88 ms                                                         | 2.26 ms: 1.20x slower                                                  |
| genshi_text                | 14.4 ms                                                         | 17.3 ms: 1.20x slower                                                  |
| sqlglot_parse              | 748 us                                                          | 900 us: 1.20x slower                                                   |
| richards_super             | 30.2 ms                                                         | 36.4 ms: 1.21x slower                                                  |
| nbody                      | 67.6 ms                                                         | 81.8 ms: 1.21x slower                                                  |
| pickle_pure_python         | 175 us                                                          | 212 us: 1.21x slower                                                   |
| richards                   | 26.7 ms                                                         | 32.4 ms: 1.21x slower                                                  |
| unpickle_pure_python       | 122 us                                                          | 153 us: 1.25x slower                                                   |
| scimark_monte_carlo        | 39.1 ms                                                         | 49.9 ms: 1.28x slower                                                  |
| Geometric mean             | (ref)                                                           | 1.05x slower                                                           |

Benchmark hidden because not significant (9): regex_v8, async_tree_memoization_tg, json, async_tree_none_tg, async_tree_cpu_io_mixed, asyncio_tcp, regex_effbot, asyncio_tcp_ssl, pycparser
Ignored benchmarks (4) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, flaskblogging, mypy2
Ignored benchmarks (1) of results/bm-20240911-3.14.0a0-3b5fdc8/bm-20240911-pythonperf1-amd64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8.json: unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.07x
- 95% likely to have a slowdown of 1.07x
- 99% likely to have a slowdown of 1.06x

# Memory
- memory change: unknown