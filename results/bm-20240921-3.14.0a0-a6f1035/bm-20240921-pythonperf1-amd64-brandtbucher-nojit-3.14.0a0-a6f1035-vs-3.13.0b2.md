# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: nojit
- machine: windows-amd64
- commit hash: a6f1035
- commit date: 2024-09-21
- overall geometric mean: 1.06x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240921-pythonperf1-amd64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 226 ms: 1.09x slower                                              |
| docutils       | 1.63 sec                                                        | 1.70 sec: 1.05x slower                                            |
| html5lib       | 35.0 ms                                                         | 40.9 ms: 1.17x slower                                             |
| tornado_http   | 81.8 ms                                                         | 84.2 ms: 1.03x slower                                             |
| Geometric mean | (ref)                                                           | 1.08x slower                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240921-pythonperf1-amd64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_io_tg           | 605 ms                                                          | 562 ms: 1.08x faster                                              |
| async_tree_none            | 218 ms                                                          | 209 ms: 1.04x faster                                              |
| async_tree_cpu_io_mixed_tg | 382 ms                                                          | 398 ms: 1.04x slower                                              |
| Geometric mean             | (ref)                                                           | 1.02x faster                                                      |

Benchmark hidden because not significant (5): async_tree_io, async_tree_memoization_tg, async_tree_memoization, async_tree_cpu_io_mixed, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240921-pythonperf1-amd64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------:|
| pidigits       | 150 ms                                                          | 151 ms: 1.01x slower                                              |
| float          | 49.7 ms                                                         | 55.3 ms: 1.11x slower                                             |
| nbody          | 67.6 ms                                                         | 83.8 ms: 1.24x slower                                             |
| Geometric mean | (ref)                                                           | 1.12x slower                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240921-pythonperf1-amd64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_dna      | 119 ms                                                          | 121 ms: 1.02x slower                                              |
| regex_compile  | 78.0 ms                                                         | 93.1 ms: 1.19x slower                                             |
| Geometric mean | (ref)                                                           | 1.04x slower                                                      |

Benchmark hidden because not significant (2): regex_v8, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240921-pythonperf1-amd64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------:|
| pickle_list          | 2.90 us                                                         | 2.73 us: 1.06x faster                                             |
| pickle_dict          | 18.1 us                                                         | 17.6 us: 1.03x faster                                             |
| pickle               | 7.11 us                                                         | 7.10 us: 1.00x faster                                             |
| xml_etree_parse      | 90.9 ms                                                         | 94.3 ms: 1.04x slower                                             |
| xml_etree_iterparse  | 62.3 ms                                                         | 65.2 ms: 1.05x slower                                             |
| unpickle_list        | 2.62 us                                                         | 2.78 us: 1.06x slower                                             |
| unpickle             | 8.40 us                                                         | 9.12 us: 1.09x slower                                             |
| xml_etree_generate   | 53.2 ms                                                         | 58.6 ms: 1.10x slower                                             |
| json_dumps           | 5.61 ms                                                         | 6.26 ms: 1.11x slower                                             |
| xml_etree_process    | 36.4 ms                                                         | 40.9 ms: 1.12x slower                                             |
| tomli_loads          | 1.35 sec                                                        | 1.61 sec: 1.19x slower                                            |
| pickle_pure_python   | 175 us                                                          | 215 us: 1.23x slower                                              |
| unpickle_pure_python | 122 us                                                          | 153 us: 1.26x slower                                              |
| Geometric mean       | (ref)                                                           | 1.08x slower                                                      |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240921-pythonperf1-amd64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 20.3 ms                                                         | 21.9 ms: 1.08x slower                                             |
| python_startup_no_site | 16.2 ms                                                         | 17.9 ms: 1.11x slower                                             |
| Geometric mean         | (ref)                                                           | 1.09x slower                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240921-pythonperf1-amd64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|-----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------:|
| mako            | 6.36 ms                                                         | 6.85 ms: 1.08x slower                                             |
| genshi_xml      | 31.6 ms                                                         | 35.6 ms: 1.13x slower                                             |
| genshi_text     | 14.4 ms                                                         | 16.9 ms: 1.18x slower                                             |
| django_template | 21.7 ms                                                         | 25.9 ms: 1.20x slower                                             |
| Geometric mean  | (ref)                                                           | 1.14x slower                                                      |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240921-pythonperf1-amd64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------:|
| thrift                     | 8.11 ms                                                         | 512 us: 15.82x faster                                             |
| deepcopy                   | 220 us                                                          | 191 us: 1.15x faster                                              |
| async_tree_io_tg           | 605 ms                                                          | 562 ms: 1.08x faster                                              |
| deepcopy_memo              | 22.1 us                                                         | 20.6 us: 1.07x faster                                             |
| pickle_list                | 2.90 us                                                         | 2.73 us: 1.06x faster                                             |
| async_tree_none            | 218 ms                                                          | 209 ms: 1.04x faster                                              |
| pickle_dict                | 18.1 us                                                         | 17.6 us: 1.03x faster                                             |
| deepcopy_reduce            | 1.99 us                                                         | 1.94 us: 1.03x faster                                             |
| gc_traversal               | 1.55 ms                                                         | 1.53 ms: 1.02x faster                                             |
| pickle                     | 7.11 us                                                         | 7.10 us: 1.00x faster                                             |
| pidigits                   | 150 ms                                                          | 151 ms: 1.01x slower                                              |
| regex_dna                  | 119 ms                                                          | 121 ms: 1.02x slower                                              |
| sqlite_synth               | 1.60 us                                                         | 1.64 us: 1.02x slower                                             |
| bench_mp_pool              | 64.8 ms                                                         | 66.6 ms: 1.03x slower                                             |
| tornado_http               | 81.8 ms                                                         | 84.2 ms: 1.03x slower                                             |
| xml_etree_parse            | 90.9 ms                                                         | 94.3 ms: 1.04x slower                                             |
| async_tree_cpu_io_mixed_tg | 382 ms                                                          | 398 ms: 1.04x slower                                              |
| xml_etree_iterparse        | 62.3 ms                                                         | 65.2 ms: 1.05x slower                                             |
| docutils                   | 1.63 sec                                                        | 1.70 sec: 1.05x slower                                            |
| bench_thread_pool          | 768 us                                                          | 805 us: 1.05x slower                                              |
| crypto_pyaes               | 45.5 ms                                                         | 47.9 ms: 1.05x slower                                             |
| unpickle_list              | 2.62 us                                                         | 2.78 us: 1.06x slower                                             |
| sympy_sum                  | 84.4 ms                                                         | 90.6 ms: 1.07x slower                                             |
| mako                       | 6.36 ms                                                         | 6.85 ms: 1.08x slower                                             |
| python_startup             | 20.3 ms                                                         | 21.9 ms: 1.08x slower                                             |
| sympy_integrate            | 12.2 ms                                                         | 13.2 ms: 1.08x slower                                             |
| go                         | 82.1 ms                                                         | 88.9 ms: 1.08x slower                                             |
| coroutines                 | 12.8 ms                                                         | 13.8 ms: 1.08x slower                                             |
| unpickle                   | 8.40 us                                                         | 9.12 us: 1.09x slower                                             |
| generators                 | 19.6 ms                                                         | 21.3 ms: 1.09x slower                                             |
| 2to3                       | 207 ms                                                          | 226 ms: 1.09x slower                                              |
| spectral_norm              | 63.7 ms                                                         | 69.9 ms: 1.10x slower                                             |
| pylint                     | 205 ms                                                          | 225 ms: 1.10x slower                                              |
| async_generators           | 223 ms                                                          | 245 ms: 1.10x slower                                              |
| typing_runtime_protocols   | 101 us                                                          | 111 us: 1.10x slower                                              |
| xml_etree_generate         | 53.2 ms                                                         | 58.6 ms: 1.10x slower                                             |
| python_startup_no_site     | 16.2 ms                                                         | 17.9 ms: 1.11x slower                                             |
| float                      | 49.7 ms                                                         | 55.3 ms: 1.11x slower                                             |
| telco                      | 4.67 ms                                                         | 5.20 ms: 1.11x slower                                             |
| json_dumps                 | 5.61 ms                                                         | 6.26 ms: 1.11x slower                                             |
| sympy_str                  | 159 ms                                                          | 178 ms: 1.12x slower                                              |
| xml_etree_process          | 36.4 ms                                                         | 40.9 ms: 1.12x slower                                             |
| sqlglot_optimize           | 32.7 ms                                                         | 36.8 ms: 1.12x slower                                             |
| sympy_expand               | 271 ms                                                          | 305 ms: 1.13x slower                                              |
| genshi_xml                 | 31.6 ms                                                         | 35.6 ms: 1.13x slower                                             |
| meteor_contest             | 69.9 ms                                                         | 78.9 ms: 1.13x slower                                             |
| logging_format             | 6.22 us                                                         | 7.08 us: 1.14x slower                                             |
| sqlglot_normalize          | 173 ms                                                          | 197 ms: 1.14x slower                                              |
| dulwich_log                | 38.0 ms                                                         | 43.4 ms: 1.14x slower                                             |
| mdp                        | 1.31 sec                                                        | 1.51 sec: 1.15x slower                                            |
| coverage                   | 42.1 ms                                                         | 48.5 ms: 1.15x slower                                             |
| comprehensions             | 10.4 us                                                         | 12.0 us: 1.15x slower                                             |
| logging_simple             | 5.78 us                                                         | 6.68 us: 1.16x slower                                             |
| scimark_lu                 | 56.6 ms                                                         | 65.7 ms: 1.16x slower                                             |
| pyflate                    | 279 ms                                                          | 324 ms: 1.16x slower                                              |
| pprint_safe_repr           | 474 ms                                                          | 551 ms: 1.16x slower                                              |
| nqueens                    | 56.7 ms                                                         | 65.9 ms: 1.16x slower                                             |
| html5lib                   | 35.0 ms                                                         | 40.9 ms: 1.17x slower                                             |
| chaos                      | 38.4 ms                                                         | 44.9 ms: 1.17x slower                                             |
| pprint_pformat             | 966 ms                                                          | 1.13 sec: 1.17x slower                                            |
| scimark_sparse_mat_mult    | 2.50 ms                                                         | 2.93 ms: 1.17x slower                                             |
| sqlglot_transpile          | 955 us                                                          | 1.12 ms: 1.17x slower                                             |
| genshi_text                | 14.4 ms                                                         | 16.9 ms: 1.18x slower                                             |
| tomli_loads                | 1.35 sec                                                        | 1.61 sec: 1.19x slower                                            |
| regex_compile              | 78.0 ms                                                         | 93.1 ms: 1.19x slower                                             |
| django_template            | 21.7 ms                                                         | 25.9 ms: 1.20x slower                                             |
| logging_silent             | 52.9 ns                                                         | 63.5 ns: 1.20x slower                                             |
| scimark_sor                | 75.3 ms                                                         | 90.7 ms: 1.20x slower                                             |
| sqlglot_parse              | 748 us                                                          | 902 us: 1.21x slower                                              |
| raytrace                   | 162 ms                                                          | 197 ms: 1.22x slower                                              |
| richards_super             | 30.2 ms                                                         | 36.9 ms: 1.22x slower                                             |
| pickle_pure_python         | 175 us                                                          | 215 us: 1.23x slower                                              |
| richards                   | 26.7 ms                                                         | 33.0 ms: 1.23x slower                                             |
| deltablue                  | 1.88 ms                                                         | 2.32 ms: 1.23x slower                                             |
| nbody                      | 67.6 ms                                                         | 83.8 ms: 1.24x slower                                             |
| hexiom                     | 3.72 ms                                                         | 4.62 ms: 1.24x slower                                             |
| scimark_fft                | 171 ms                                                          | 212 ms: 1.24x slower                                              |
| unpickle_pure_python       | 122 us                                                          | 153 us: 1.26x slower                                              |
| fannkuch                   | 243 ms                                                          | 308 ms: 1.27x slower                                              |
| scimark_monte_carlo        | 39.1 ms                                                         | 51.4 ms: 1.31x slower                                             |
| Geometric mean             | (ref)                                                           | 1.06x slower                                                      |

Benchmark hidden because not significant (14): regex_v8, async_tree_io, json, async_tree_memoization_tg, asyncio_tcp_ssl, async_tree_memoization, async_tree_cpu_io_mixed, async_tree_none_tg, create_gc_cycles, asyncio_tcp, json_loads, pathlib, regex_effbot, pycparser
Ignored benchmarks (4) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, flaskblogging, mypy2
Ignored benchmarks (1) of results/bm-20240921-3.14.0a0-a6f1035/bm-20240921-pythonperf1-amd64-brandtbucher-nojit-3.14.0a0-a6f1035.json: unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.08x
- 95% likely to have a slowdown of 1.08x
- 99% likely to have a slowdown of 1.07x

# Memory
- memory change: unknown