# Results vs. 3.13.0b2

- fork: mdboom
- ref: mdboom_08_17
- machine: windows-amd64
- commit hash: 7ab5aad
- commit date: 2024-08-28
- overall geometric mean: 1.07x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240828-pythonperf1-amd64-mdboom-mdboom_08_17-3.14.0a0-7ab5aad |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 233 ms: 1.13x slower                                               |
| docutils       | 1.63 sec                                                        | 1.75 sec: 1.08x slower                                             |
| html5lib       | 35.0 ms                                                         | 41.9 ms: 1.20x slower                                              |
| tornado_http   | 81.8 ms                                                         | 93.5 ms: 1.14x slower                                              |
| Geometric mean | (ref)                                                           | 1.13x slower                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240828-pythonperf1-amd64-mdboom-mdboom_08_17-3.14.0a0-7ab5aad |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_io_tg           | 605 ms                                                          | 548 ms: 1.11x faster                                               |
| async_tree_cpu_io_mixed_tg | 382 ms                                                          | 394 ms: 1.03x slower                                               |
| Geometric mean             | (ref)                                                           | 1.01x faster                                                       |

Benchmark hidden because not significant (6): async_tree_memoization_tg, async_tree_none_tg, async_tree_io, async_tree_cpu_io_mixed, async_tree_none, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240828-pythonperf1-amd64-mdboom-mdboom_08_17-3.14.0a0-7ab5aad |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------:|
| pidigits       | 150 ms                                                          | 151 ms: 1.01x slower                                               |
| float          | 49.7 ms                                                         | 56.1 ms: 1.13x slower                                              |
| nbody          | 67.6 ms                                                         | 85.1 ms: 1.26x slower                                              |
| Geometric mean | (ref)                                                           | 1.13x slower                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240828-pythonperf1-amd64-mdboom-mdboom_08_17-3.14.0a0-7ab5aad |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 78.0 ms                                                         | 90.4 ms: 1.16x slower                                              |
| Geometric mean | (ref)                                                           | 1.02x slower                                                       |

Benchmark hidden because not significant (3): regex_v8, regex_effbot, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240828-pythonperf1-amd64-mdboom-mdboom_08_17-3.14.0a0-7ab5aad |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------:|
| json_loads           | 14.2 us                                                         | 14.8 us: 1.04x slower                                              |
| xml_etree_iterparse  | 62.3 ms                                                         | 65.1 ms: 1.04x slower                                              |
| xml_etree_parse      | 90.9 ms                                                         | 96.0 ms: 1.06x slower                                              |
| json_dumps           | 5.61 ms                                                         | 6.08 ms: 1.08x slower                                              |
| xml_etree_generate   | 53.2 ms                                                         | 57.7 ms: 1.09x slower                                              |
| xml_etree_process    | 36.4 ms                                                         | 40.2 ms: 1.10x slower                                              |
| tomli_loads          | 1.35 sec                                                        | 1.58 sec: 1.17x slower                                             |
| pickle_pure_python   | 175 us                                                          | 210 us: 1.20x slower                                               |
| unpickle_pure_python | 122 us                                                          | 148 us: 1.22x slower                                               |
| Geometric mean       | (ref)                                                           | 1.11x slower                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240828-pythonperf1-amd64-mdboom-mdboom_08_17-3.14.0a0-7ab5aad |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 20.3 ms                                                         | 22.2 ms: 1.10x slower                                              |
| python_startup_no_site | 16.2 ms                                                         | 18.0 ms: 1.11x slower                                              |
| Geometric mean         | (ref)                                                           | 1.10x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240828-pythonperf1-amd64-mdboom-mdboom_08_17-3.14.0a0-7ab5aad |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------:|
| mako            | 6.36 ms                                                         | 6.98 ms: 1.10x slower                                              |
| django_template | 21.7 ms                                                         | 25.0 ms: 1.15x slower                                              |
| genshi_xml      | 31.6 ms                                                         | 37.1 ms: 1.18x slower                                              |
| genshi_text     | 14.4 ms                                                         | 17.5 ms: 1.22x slower                                              |
| Geometric mean  | (ref)                                                           | 1.16x slower                                                       |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240828-pythonperf1-amd64-mdboom-mdboom_08_17-3.14.0a0-7ab5aad |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------:|
| thrift                     | 8.11 ms                                                         | 520 us: 15.58x faster                                              |
| deepcopy                   | 220 us                                                          | 189 us: 1.16x faster                                               |
| async_tree_io_tg           | 605 ms                                                          | 548 ms: 1.11x faster                                               |
| deepcopy_memo              | 22.1 us                                                         | 20.3 us: 1.09x faster                                              |
| deepcopy_reduce            | 1.99 us                                                         | 1.92 us: 1.04x faster                                              |
| pidigits                   | 150 ms                                                          | 151 ms: 1.01x slower                                               |
| gc_traversal               | 1.55 ms                                                         | 1.58 ms: 1.02x slower                                              |
| create_gc_cycles           | 888 us                                                          | 908 us: 1.02x slower                                               |
| pathlib                    | 75.9 ms                                                         | 77.9 ms: 1.03x slower                                              |
| async_tree_cpu_io_mixed_tg | 382 ms                                                          | 394 ms: 1.03x slower                                               |
| json_loads                 | 14.2 us                                                         | 14.8 us: 1.04x slower                                              |
| xml_etree_iterparse        | 62.3 ms                                                         | 65.1 ms: 1.04x slower                                              |
| generators                 | 19.6 ms                                                         | 20.6 ms: 1.05x slower                                              |
| xml_etree_parse            | 90.9 ms                                                         | 96.0 ms: 1.06x slower                                              |
| bench_mp_pool              | 64.8 ms                                                         | 68.4 ms: 1.06x slower                                              |
| crypto_pyaes               | 45.5 ms                                                         | 48.1 ms: 1.06x slower                                              |
| telco                      | 4.67 ms                                                         | 4.99 ms: 1.07x slower                                              |
| bench_thread_pool          | 768 us                                                          | 825 us: 1.07x slower                                               |
| docutils                   | 1.63 sec                                                        | 1.75 sec: 1.08x slower                                             |
| sympy_sum                  | 84.4 ms                                                         | 90.8 ms: 1.08x slower                                              |
| mdp                        | 1.31 sec                                                        | 1.42 sec: 1.08x slower                                             |
| json_dumps                 | 5.61 ms                                                         | 6.08 ms: 1.08x slower                                              |
| xml_etree_generate         | 53.2 ms                                                         | 57.7 ms: 1.09x slower                                              |
| sympy_integrate            | 12.2 ms                                                         | 13.3 ms: 1.09x slower                                              |
| logging_format             | 6.22 us                                                         | 6.78 us: 1.09x slower                                              |
| logging_simple             | 5.78 us                                                         | 6.32 us: 1.09x slower                                              |
| python_startup             | 20.3 ms                                                         | 22.2 ms: 1.10x slower                                              |
| mako                       | 6.36 ms                                                         | 6.98 ms: 1.10x slower                                              |
| sqlglot_optimize           | 32.7 ms                                                         | 36.0 ms: 1.10x slower                                              |
| xml_etree_process          | 36.4 ms                                                         | 40.2 ms: 1.10x slower                                              |
| pylint                     | 205 ms                                                          | 227 ms: 1.11x slower                                               |
| python_startup_no_site     | 16.2 ms                                                         | 18.0 ms: 1.11x slower                                              |
| meteor_contest             | 69.9 ms                                                         | 77.8 ms: 1.11x slower                                              |
| sqlglot_normalize          | 173 ms                                                          | 193 ms: 1.12x slower                                               |
| scimark_lu                 | 56.6 ms                                                         | 63.3 ms: 1.12x slower                                              |
| spectral_norm              | 63.7 ms                                                         | 71.3 ms: 1.12x slower                                              |
| sympy_str                  | 159 ms                                                          | 178 ms: 1.12x slower                                               |
| 2to3                       | 207 ms                                                          | 233 ms: 1.13x slower                                               |
| float                      | 49.7 ms                                                         | 56.1 ms: 1.13x slower                                              |
| coroutines                 | 12.8 ms                                                         | 14.4 ms: 1.13x slower                                              |
| dulwich_log                | 38.0 ms                                                         | 43.0 ms: 1.13x slower                                              |
| typing_runtime_protocols   | 101 us                                                          | 114 us: 1.13x slower                                               |
| asyncio_tcp_ssl            | 1.48 sec                                                        | 1.68 sec: 1.13x slower                                             |
| async_generators           | 223 ms                                                          | 253 ms: 1.13x slower                                               |
| sympy_expand               | 271 ms                                                          | 308 ms: 1.14x slower                                               |
| nqueens                    | 56.7 ms                                                         | 64.7 ms: 1.14x slower                                              |
| tornado_http               | 81.8 ms                                                         | 93.5 ms: 1.14x slower                                              |
| scimark_sparse_mat_mult    | 2.50 ms                                                         | 2.86 ms: 1.14x slower                                              |
| asyncio_tcp                | 471 ms                                                          | 539 ms: 1.14x slower                                               |
| chaos                      | 38.4 ms                                                         | 44.0 ms: 1.15x slower                                              |
| comprehensions             | 10.4 us                                                         | 11.9 us: 1.15x slower                                              |
| django_template            | 21.7 ms                                                         | 25.0 ms: 1.15x slower                                              |
| raytrace                   | 162 ms                                                          | 187 ms: 1.15x slower                                               |
| pycparser                  | 754 ms                                                          | 871 ms: 1.16x slower                                               |
| sqlglot_transpile          | 955 us                                                          | 1.10 ms: 1.16x slower                                              |
| regex_compile              | 78.0 ms                                                         | 90.4 ms: 1.16x slower                                              |
| pyflate                    | 279 ms                                                          | 325 ms: 1.16x slower                                               |
| tomli_loads                | 1.35 sec                                                        | 1.58 sec: 1.17x slower                                             |
| hexiom                     | 3.72 ms                                                         | 4.36 ms: 1.17x slower                                              |
| pprint_safe_repr           | 474 ms                                                          | 555 ms: 1.17x slower                                               |
| genshi_xml                 | 31.6 ms                                                         | 37.1 ms: 1.18x slower                                              |
| pprint_pformat             | 966 ms                                                          | 1.14 sec: 1.18x slower                                             |
| deltablue                  | 1.88 ms                                                         | 2.24 ms: 1.19x slower                                              |
| logging_silent             | 52.9 ns                                                         | 62.9 ns: 1.19x slower                                              |
| sqlglot_parse              | 748 us                                                          | 889 us: 1.19x slower                                               |
| go                         | 82.1 ms                                                         | 97.6 ms: 1.19x slower                                              |
| coverage                   | 42.1 ms                                                         | 50.1 ms: 1.19x slower                                              |
| pickle_pure_python         | 175 us                                                          | 210 us: 1.20x slower                                               |
| html5lib                   | 35.0 ms                                                         | 41.9 ms: 1.20x slower                                              |
| scimark_fft                | 171 ms                                                          | 207 ms: 1.21x slower                                               |
| unpickle_pure_python       | 122 us                                                          | 148 us: 1.22x slower                                               |
| genshi_text                | 14.4 ms                                                         | 17.5 ms: 1.22x slower                                              |
| fannkuch                   | 243 ms                                                          | 297 ms: 1.22x slower                                               |
| scimark_sor                | 75.3 ms                                                         | 93.0 ms: 1.23x slower                                              |
| richards                   | 26.7 ms                                                         | 33.3 ms: 1.25x slower                                              |
| richards_super             | 30.2 ms                                                         | 37.7 ms: 1.25x slower                                              |
| nbody                      | 67.6 ms                                                         | 85.1 ms: 1.26x slower                                              |
| scimark_monte_carlo        | 39.1 ms                                                         | 49.5 ms: 1.27x slower                                              |
| Geometric mean             | (ref)                                                           | 1.07x slower                                                       |

Benchmark hidden because not significant (10): regex_v8, json, async_tree_memoization_tg, async_tree_none_tg, async_tree_io, regex_effbot, async_tree_cpu_io_mixed, regex_dna, async_tree_none, async_tree_memoization
Ignored benchmarks (10) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.09x
- 95% likely to have a slowdown of 1.08x
- 99% likely to have a slowdown of 1.08x

# Memory
- memory change: unknown