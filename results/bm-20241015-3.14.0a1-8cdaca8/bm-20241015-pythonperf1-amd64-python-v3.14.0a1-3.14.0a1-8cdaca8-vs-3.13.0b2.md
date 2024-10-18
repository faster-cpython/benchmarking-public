# Results vs. 3.13.0b2

- fork: python
- ref: v3.14.0a1
- machine: windows-amd64
- commit hash: 8cdaca8
- commit date: 2024-10-15
- overall geometric mean: 1.09x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241015-pythonperf1-amd64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 231 ms: 1.12x slower                                            |
| docutils       | 1.63 sec                                                        | 1.72 sec: 1.06x slower                                          |
| html5lib       | 35.0 ms                                                         | 40.8 ms: 1.17x slower                                           |
| tornado_http   | 81.8 ms                                                         | 93.8 ms: 1.15x slower                                           |
| Geometric mean | (ref)                                                           | 1.12x slower                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241015-pythonperf1-amd64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_none            | 218 ms                                                          | 226 ms: 1.04x slower                                            |
| async_tree_none_tg         | 202 ms                                                          | 215 ms: 1.06x slower                                            |
| async_tree_cpu_io_mixed_tg | 382 ms                                                          | 407 ms: 1.07x slower                                            |
| async_tree_io_tg           | 605 ms                                                          | 645 ms: 1.07x slower                                            |
| async_tree_memoization     | 264 ms                                                          | 281 ms: 1.07x slower                                            |
| Geometric mean             | (ref)                                                           | 1.04x slower                                                    |

Benchmark hidden because not significant (3): async_tree_io, async_tree_cpu_io_mixed, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241015-pythonperf1-amd64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| pidigits       | 150 ms                                                          | 148 ms: 1.01x faster                                            |
| float          | 49.7 ms                                                         | 55.6 ms: 1.12x slower                                           |
| nbody          | 67.6 ms                                                         | 79.3 ms: 1.17x slower                                           |
| Geometric mean | (ref)                                                           | 1.09x slower                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241015-pythonperf1-amd64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_dna      | 119 ms                                                          | 116 ms: 1.02x faster                                            |
| regex_compile  | 78.0 ms                                                         | 91.1 ms: 1.17x slower                                           |
| Geometric mean | (ref)                                                           | 1.05x slower                                                    |

Benchmark hidden because not significant (2): regex_effbot, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241015-pythonperf1-amd64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| pickle_list          | 2.90 us                                                         | 3.00 us: 1.03x slower                                           |
| pickle               | 7.11 us                                                         | 7.37 us: 1.04x slower                                           |
| xml_etree_parse      | 90.9 ms                                                         | 95.4 ms: 1.05x slower                                           |
| xml_etree_iterparse  | 62.3 ms                                                         | 66.3 ms: 1.06x slower                                           |
| pickle_dict          | 18.1 us                                                         | 19.3 us: 1.06x slower                                           |
| unpickle             | 8.40 us                                                         | 9.00 us: 1.07x slower                                           |
| unpickle_list        | 2.62 us                                                         | 2.83 us: 1.08x slower                                           |
| json_loads           | 14.2 us                                                         | 15.5 us: 1.09x slower                                           |
| xml_etree_generate   | 53.2 ms                                                         | 59.3 ms: 1.12x slower                                           |
| xml_etree_process    | 36.4 ms                                                         | 41.7 ms: 1.14x slower                                           |
| tomli_loads          | 1.35 sec                                                        | 1.61 sec: 1.20x slower                                          |
| json_dumps           | 5.61 ms                                                         | 6.93 ms: 1.23x slower                                           |
| pickle_pure_python   | 175 us                                                          | 217 us: 1.24x slower                                            |
| unpickle_pure_python | 122 us                                                          | 151 us: 1.24x slower                                            |
| Geometric mean       | (ref)                                                           | 1.12x slower                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241015-pythonperf1-amd64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                         | 18.3 ms: 1.13x slower                                           |
| python_startup         | 20.3 ms                                                         | 24.6 ms: 1.21x slower                                           |
| Geometric mean         | (ref)                                                           | 1.17x slower                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241015-pythonperf1-amd64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|-----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| mako            | 6.36 ms                                                         | 6.73 ms: 1.06x slower                                           |
| django_template | 21.7 ms                                                         | 25.9 ms: 1.20x slower                                           |
| genshi_text     | 14.4 ms                                                         | 17.5 ms: 1.21x slower                                           |
| genshi_xml      | 31.6 ms                                                         | 39.6 ms: 1.25x slower                                           |
| Geometric mean  | (ref)                                                           | 1.18x slower                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241015-pythonperf1-amd64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| thrift                     | 8.11 ms                                                         | 539 us: 15.05x faster                                           |
| deepcopy                   | 220 us                                                          | 194 us: 1.14x faster                                            |
| deepcopy_memo              | 22.1 us                                                         | 20.4 us: 1.08x faster                                           |
| regex_dna                  | 119 ms                                                          | 116 ms: 1.02x faster                                            |
| pidigits                   | 150 ms                                                          | 148 ms: 1.01x faster                                            |
| deepcopy_reduce            | 1.99 us                                                         | 2.02 us: 1.01x slower                                           |
| sqlite_synth               | 1.60 us                                                         | 1.63 us: 1.02x slower                                           |
| pickle_list                | 2.90 us                                                         | 3.00 us: 1.03x slower                                           |
| async_tree_none            | 218 ms                                                          | 226 ms: 1.04x slower                                            |
| pickle                     | 7.11 us                                                         | 7.37 us: 1.04x slower                                           |
| telco                      | 4.67 ms                                                         | 4.89 ms: 1.05x slower                                           |
| xml_etree_parse            | 90.9 ms                                                         | 95.4 ms: 1.05x slower                                           |
| mako                       | 6.36 ms                                                         | 6.73 ms: 1.06x slower                                           |
| docutils                   | 1.63 sec                                                        | 1.72 sec: 1.06x slower                                          |
| xml_etree_iterparse        | 62.3 ms                                                         | 66.3 ms: 1.06x slower                                           |
| pickle_dict                | 18.1 us                                                         | 19.3 us: 1.06x slower                                           |
| async_tree_none_tg         | 202 ms                                                          | 215 ms: 1.06x slower                                            |
| pathlib                    | 75.9 ms                                                         | 80.8 ms: 1.07x slower                                           |
| async_tree_cpu_io_mixed_tg | 382 ms                                                          | 407 ms: 1.07x slower                                            |
| async_tree_io_tg           | 605 ms                                                          | 645 ms: 1.07x slower                                            |
| async_tree_memoization     | 264 ms                                                          | 281 ms: 1.07x slower                                            |
| scimark_sparse_mat_mult    | 2.50 ms                                                         | 2.68 ms: 1.07x slower                                           |
| unpickle                   | 8.40 us                                                         | 9.00 us: 1.07x slower                                           |
| sympy_sum                  | 84.4 ms                                                         | 90.9 ms: 1.08x slower                                           |
| go                         | 82.1 ms                                                         | 88.5 ms: 1.08x slower                                           |
| unpickle_list              | 2.62 us                                                         | 2.83 us: 1.08x slower                                           |
| bench_thread_pool          | 768 us                                                          | 831 us: 1.08x slower                                            |
| coroutines                 | 12.8 ms                                                         | 13.9 ms: 1.09x slower                                           |
| json_loads                 | 14.2 us                                                         | 15.5 us: 1.09x slower                                           |
| logging_format             | 6.22 us                                                         | 6.85 us: 1.10x slower                                           |
| meteor_contest             | 69.9 ms                                                         | 77.0 ms: 1.10x slower                                           |
| sympy_integrate            | 12.2 ms                                                         | 13.5 ms: 1.10x slower                                           |
| crypto_pyaes               | 45.5 ms                                                         | 50.3 ms: 1.11x slower                                           |
| logging_simple             | 5.78 us                                                         | 6.42 us: 1.11x slower                                           |
| typing_runtime_protocols   | 101 us                                                          | 112 us: 1.11x slower                                            |
| async_generators           | 223 ms                                                          | 249 ms: 1.11x slower                                            |
| xml_etree_generate         | 53.2 ms                                                         | 59.3 ms: 1.12x slower                                           |
| scimark_lu                 | 56.6 ms                                                         | 63.2 ms: 1.12x slower                                           |
| pylint                     | 205 ms                                                          | 229 ms: 1.12x slower                                            |
| float                      | 49.7 ms                                                         | 55.6 ms: 1.12x slower                                           |
| 2to3                       | 207 ms                                                          | 231 ms: 1.12x slower                                            |
| python_startup_no_site     | 16.2 ms                                                         | 18.3 ms: 1.13x slower                                           |
| nqueens                    | 56.7 ms                                                         | 63.9 ms: 1.13x slower                                           |
| generators                 | 19.6 ms                                                         | 22.1 ms: 1.13x slower                                           |
| sqlglot_optimize           | 32.7 ms                                                         | 37.2 ms: 1.14x slower                                           |
| sympy_str                  | 159 ms                                                          | 181 ms: 1.14x slower                                            |
| mdp                        | 1.31 sec                                                        | 1.50 sec: 1.14x slower                                          |
| comprehensions             | 10.4 us                                                         | 11.9 us: 1.14x slower                                           |
| spectral_norm              | 63.7 ms                                                         | 72.9 ms: 1.14x slower                                           |
| xml_etree_process          | 36.4 ms                                                         | 41.7 ms: 1.14x slower                                           |
| dulwich_log                | 38.0 ms                                                         | 43.6 ms: 1.15x slower                                           |
| tornado_http               | 81.8 ms                                                         | 93.8 ms: 1.15x slower                                           |
| sqlglot_normalize          | 173 ms                                                          | 199 ms: 1.15x slower                                            |
| sympy_expand               | 271 ms                                                          | 312 ms: 1.15x slower                                            |
| chaos                      | 38.4 ms                                                         | 44.6 ms: 1.16x slower                                           |
| coverage                   | 42.1 ms                                                         | 49.0 ms: 1.17x slower                                           |
| html5lib                   | 35.0 ms                                                         | 40.8 ms: 1.17x slower                                           |
| regex_compile              | 78.0 ms                                                         | 91.1 ms: 1.17x slower                                           |
| nbody                      | 67.6 ms                                                         | 79.3 ms: 1.17x slower                                           |
| pyflate                    | 279 ms                                                          | 327 ms: 1.17x slower                                            |
| fannkuch                   | 243 ms                                                          | 286 ms: 1.17x slower                                            |
| scimark_fft                | 171 ms                                                          | 202 ms: 1.18x slower                                            |
| pprint_pformat             | 966 ms                                                          | 1.14 sec: 1.18x slower                                          |
| logging_silent             | 52.9 ns                                                         | 62.9 ns: 1.19x slower                                           |
| pprint_safe_repr           | 474 ms                                                          | 565 ms: 1.19x slower                                            |
| sqlglot_transpile          | 955 us                                                          | 1.14 ms: 1.19x slower                                           |
| tomli_loads                | 1.35 sec                                                        | 1.61 sec: 1.20x slower                                          |
| django_template            | 21.7 ms                                                         | 25.9 ms: 1.20x slower                                           |
| hexiom                     | 3.72 ms                                                         | 4.46 ms: 1.20x slower                                           |
| richards                   | 26.7 ms                                                         | 32.3 ms: 1.21x slower                                           |
| python_startup             | 20.3 ms                                                         | 24.6 ms: 1.21x slower                                           |
| deltablue                  | 1.88 ms                                                         | 2.29 ms: 1.21x slower                                           |
| genshi_text                | 14.4 ms                                                         | 17.5 ms: 1.21x slower                                           |
| richards_super             | 30.2 ms                                                         | 36.8 ms: 1.22x slower                                           |
| raytrace                   | 162 ms                                                          | 198 ms: 1.22x slower                                            |
| sqlglot_parse              | 748 us                                                          | 921 us: 1.23x slower                                            |
| scimark_monte_carlo        | 39.1 ms                                                         | 48.2 ms: 1.23x slower                                           |
| json_dumps                 | 5.61 ms                                                         | 6.93 ms: 1.23x slower                                           |
| scimark_sor                | 75.3 ms                                                         | 93.2 ms: 1.24x slower                                           |
| pickle_pure_python         | 175 us                                                          | 217 us: 1.24x slower                                            |
| unpickle_pure_python       | 122 us                                                          | 151 us: 1.24x slower                                            |
| genshi_xml                 | 31.6 ms                                                         | 39.6 ms: 1.25x slower                                           |
| gc_traversal               | 1.55 ms                                                         | 1.97 ms: 1.27x slower                                           |
| bench_mp_pool              | 64.8 ms                                                         | 84.0 ms: 1.30x slower                                           |
| asyncio_tcp                | 471 ms                                                          | 661 ms: 1.40x slower                                            |
| create_gc_cycles           | 888 us                                                          | 1.41 ms: 1.59x slower                                           |
| Geometric mean             | (ref)                                                           | 1.09x slower                                                    |

Benchmark hidden because not significant (8): async_tree_io, json, async_tree_cpu_io_mixed, pycparser, regex_effbot, async_tree_memoization_tg, asyncio_tcp_ssl, regex_v8
Ignored benchmarks (4) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, flaskblogging, mypy2
Ignored benchmarks (2) of results/bm-20241015-3.14.0a1-8cdaca8/bm-20241015-pythonperf1-amd64-python-v3.14.0a1-3.14.0a1-8cdaca8.json: sphinx, unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.11x
- 95% likely to have a slowdown of 1.11x
- 99% likely to have a slowdown of 1.10x

# Memory
- memory change: unknown