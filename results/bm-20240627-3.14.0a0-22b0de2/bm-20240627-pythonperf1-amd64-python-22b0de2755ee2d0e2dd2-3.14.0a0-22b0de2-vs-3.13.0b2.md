# Results vs. 3.13.0b2

- fork: python
- ref: 22b0de2755ee2d0e2dd2
- machine: windows-amd64
- commit hash: 22b0de2
- commit date: 2024-06-27
- overall geometric mean: 1.06x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240627-pythonperf1-amd64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 227 ms: 1.10x slower                                                       |
| docutils       | 1.63 sec                                                        | 1.68 sec: 1.04x slower                                                     |
| html5lib       | 35.0 ms                                                         | 38.4 ms: 1.10x slower                                                      |
| tornado_http   | 81.8 ms                                                         | 82.7 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                           | 1.06x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240627-pythonperf1-amd64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 605 ms                                                          | 539 ms: 1.12x faster                                                       |
| async_tree_memoization_tg  | 258 ms                                                          | 247 ms: 1.04x faster                                                       |
| async_tree_cpu_io_mixed_tg | 382 ms                                                          | 392 ms: 1.02x slower                                                       |
| Geometric mean             | (ref)                                                           | 1.03x faster                                                               |

Benchmark hidden because not significant (5): async_tree_io, async_tree_none_tg, async_tree_memoization, async_tree_cpu_io_mixed, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240627-pythonperf1-amd64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 49.7 ms                                                         | 58.3 ms: 1.17x slower                                                      |
| nbody          | 67.6 ms                                                         | 83.8 ms: 1.24x slower                                                      |
| Geometric mean | (ref)                                                           | 1.13x slower                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240627-pythonperf1-amd64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 1.58 ms                                                         | 1.63 ms: 1.03x slower                                                      |
| regex_dna      | 119 ms                                                          | 127 ms: 1.06x slower                                                       |
| regex_compile  | 78.0 ms                                                         | 88.1 ms: 1.13x slower                                                      |
| Geometric mean | (ref)                                                           | 1.07x slower                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240627-pythonperf1-amd64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| xml_etree_parse      | 90.9 ms                                                         | 93.4 ms: 1.03x slower                                                      |
| json_dumps           | 5.61 ms                                                         | 6.00 ms: 1.07x slower                                                      |
| xml_etree_iterparse  | 62.3 ms                                                         | 67.7 ms: 1.09x slower                                                      |
| xml_etree_generate   | 53.2 ms                                                         | 59.5 ms: 1.12x slower                                                      |
| xml_etree_process    | 36.4 ms                                                         | 42.1 ms: 1.15x slower                                                      |
| tomli_loads          | 1.35 sec                                                        | 1.62 sec: 1.20x slower                                                     |
| pickle_pure_python   | 175 us                                                          | 214 us: 1.22x slower                                                       |
| unpickle_pure_python | 122 us                                                          | 161 us: 1.32x slower                                                       |
| Geometric mean       | (ref)                                                           | 1.13x slower                                                               |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240627-pythonperf1-amd64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.3 ms                                                         | 20.7 ms: 1.02x slower                                                      |
| python_startup_no_site | 16.2 ms                                                         | 17.0 ms: 1.05x slower                                                      |
| Geometric mean         | (ref)                                                           | 1.03x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240627-pythonperf1-amd64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 21.7 ms                                                         | 24.7 ms: 1.14x slower                                                      |
| genshi_text     | 14.4 ms                                                         | 16.9 ms: 1.18x slower                                                      |
| genshi_xml      | 31.6 ms                                                         | 38.6 ms: 1.22x slower                                                      |
| mako            | 6.36 ms                                                         | 7.87 ms: 1.24x slower                                                      |
| Geometric mean  | (ref)                                                           | 1.19x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240627-pythonperf1-amd64-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.11 ms                                                         | 528 us: 15.34x faster                                                      |
| deepcopy                   | 220 us                                                          | 185 us: 1.19x faster                                                       |
| async_tree_io_tg           | 605 ms                                                          | 539 ms: 1.12x faster                                                       |
| json                       | 3.19 ms                                                         | 2.96 ms: 1.08x faster                                                      |
| deepcopy_reduce            | 1.99 us                                                         | 1.87 us: 1.06x faster                                                      |
| async_tree_memoization_tg  | 258 ms                                                          | 247 ms: 1.04x faster                                                       |
| deepcopy_memo              | 22.1 us                                                         | 21.8 us: 1.01x faster                                                      |
| pathlib                    | 75.9 ms                                                         | 75.4 ms: 1.01x faster                                                      |
| tornado_http               | 81.8 ms                                                         | 82.7 ms: 1.01x slower                                                      |
| create_gc_cycles           | 888 us                                                          | 902 us: 1.02x slower                                                       |
| python_startup             | 20.3 ms                                                         | 20.7 ms: 1.02x slower                                                      |
| bench_mp_pool              | 64.8 ms                                                         | 66.0 ms: 1.02x slower                                                      |
| async_tree_cpu_io_mixed_tg | 382 ms                                                          | 392 ms: 1.02x slower                                                       |
| asyncio_tcp                | 471 ms                                                          | 483 ms: 1.02x slower                                                       |
| regex_effbot               | 1.58 ms                                                         | 1.63 ms: 1.03x slower                                                      |
| xml_etree_parse            | 90.9 ms                                                         | 93.4 ms: 1.03x slower                                                      |
| docutils                   | 1.63 sec                                                        | 1.68 sec: 1.04x slower                                                     |
| python_startup_no_site     | 16.2 ms                                                         | 17.0 ms: 1.05x slower                                                      |
| sympy_sum                  | 84.4 ms                                                         | 88.8 ms: 1.05x slower                                                      |
| asyncio_tcp_ssl            | 1.48 sec                                                        | 1.57 sec: 1.06x slower                                                     |
| regex_dna                  | 119 ms                                                          | 127 ms: 1.06x slower                                                       |
| json_dumps                 | 5.61 ms                                                         | 6.00 ms: 1.07x slower                                                      |
| sqlglot_optimize           | 32.7 ms                                                         | 35.2 ms: 1.07x slower                                                      |
| telco                      | 4.67 ms                                                         | 5.03 ms: 1.08x slower                                                      |
| sympy_integrate            | 12.2 ms                                                         | 13.2 ms: 1.08x slower                                                      |
| sympy_str                  | 159 ms                                                          | 173 ms: 1.09x slower                                                       |
| mdp                        | 1.31 sec                                                        | 1.42 sec: 1.09x slower                                                     |
| xml_etree_iterparse        | 62.3 ms                                                         | 67.7 ms: 1.09x slower                                                      |
| logging_format             | 6.22 us                                                         | 6.76 us: 1.09x slower                                                      |
| sqlglot_normalize          | 173 ms                                                          | 188 ms: 1.09x slower                                                       |
| logging_simple             | 5.78 us                                                         | 6.29 us: 1.09x slower                                                      |
| sympy_expand               | 271 ms                                                          | 295 ms: 1.09x slower                                                       |
| html5lib                   | 35.0 ms                                                         | 38.4 ms: 1.10x slower                                                      |
| 2to3                       | 207 ms                                                          | 227 ms: 1.10x slower                                                       |
| coverage                   | 42.1 ms                                                         | 46.4 ms: 1.10x slower                                                      |
| meteor_contest             | 69.9 ms                                                         | 77.5 ms: 1.11x slower                                                      |
| xml_etree_generate         | 53.2 ms                                                         | 59.5 ms: 1.12x slower                                                      |
| regex_compile              | 78.0 ms                                                         | 88.1 ms: 1.13x slower                                                      |
| typing_runtime_protocols   | 101 us                                                          | 114 us: 1.13x slower                                                       |
| django_template            | 21.7 ms                                                         | 24.7 ms: 1.14x slower                                                      |
| async_generators           | 223 ms                                                          | 255 ms: 1.14x slower                                                       |
| nqueens                    | 56.7 ms                                                         | 64.8 ms: 1.14x slower                                                      |
| raytrace                   | 162 ms                                                          | 186 ms: 1.15x slower                                                       |
| richards_super             | 30.2 ms                                                         | 34.7 ms: 1.15x slower                                                      |
| coroutines                 | 12.8 ms                                                         | 14.7 ms: 1.15x slower                                                      |
| xml_etree_process          | 36.4 ms                                                         | 42.1 ms: 1.15x slower                                                      |
| chaos                      | 38.4 ms                                                         | 44.6 ms: 1.16x slower                                                      |
| richards                   | 26.7 ms                                                         | 31.1 ms: 1.16x slower                                                      |
| go                         | 82.1 ms                                                         | 95.8 ms: 1.17x slower                                                      |
| spectral_norm              | 63.7 ms                                                         | 74.7 ms: 1.17x slower                                                      |
| float                      | 49.7 ms                                                         | 58.3 ms: 1.17x slower                                                      |
| crypto_pyaes               | 45.5 ms                                                         | 53.5 ms: 1.18x slower                                                      |
| genshi_text                | 14.4 ms                                                         | 16.9 ms: 1.18x slower                                                      |
| pyflate                    | 279 ms                                                          | 328 ms: 1.18x slower                                                       |
| sqlglot_transpile          | 955 us                                                          | 1.13 ms: 1.18x slower                                                      |
| pprint_pformat             | 966 ms                                                          | 1.15 sec: 1.19x slower                                                     |
| pprint_safe_repr           | 474 ms                                                          | 564 ms: 1.19x slower                                                       |
| scimark_lu                 | 56.6 ms                                                         | 67.5 ms: 1.19x slower                                                      |
| generators                 | 19.6 ms                                                         | 23.3 ms: 1.19x slower                                                      |
| tomli_loads                | 1.35 sec                                                        | 1.62 sec: 1.20x slower                                                     |
| deltablue                  | 1.88 ms                                                         | 2.27 ms: 1.21x slower                                                      |
| comprehensions             | 10.4 us                                                         | 12.5 us: 1.21x slower                                                      |
| sqlglot_parse              | 748 us                                                          | 911 us: 1.22x slower                                                       |
| pickle_pure_python         | 175 us                                                          | 214 us: 1.22x slower                                                       |
| scimark_sor                | 75.3 ms                                                         | 92.0 ms: 1.22x slower                                                      |
| genshi_xml                 | 31.6 ms                                                         | 38.6 ms: 1.22x slower                                                      |
| hexiom                     | 3.72 ms                                                         | 4.56 ms: 1.23x slower                                                      |
| scimark_sparse_mat_mult    | 2.50 ms                                                         | 3.09 ms: 1.23x slower                                                      |
| mako                       | 6.36 ms                                                         | 7.87 ms: 1.24x slower                                                      |
| nbody                      | 67.6 ms                                                         | 83.8 ms: 1.24x slower                                                      |
| logging_silent             | 52.9 ns                                                         | 66.3 ns: 1.25x slower                                                      |
| fannkuch                   | 243 ms                                                          | 311 ms: 1.28x slower                                                       |
| scimark_fft                | 171 ms                                                          | 220 ms: 1.29x slower                                                       |
| unpickle_pure_python       | 122 us                                                          | 161 us: 1.32x slower                                                       |
| scimark_monte_carlo        | 39.1 ms                                                         | 51.9 ms: 1.33x slower                                                      |
| Geometric mean             | (ref)                                                           | 1.06x slower                                                               |

Benchmark hidden because not significant (12): async_tree_io, async_tree_none_tg, async_tree_memoization, async_tree_cpu_io_mixed, gc_traversal, json_loads, async_tree_none, pidigits, bench_thread_pool, pycparser, pylint, regex_v8
Ignored benchmarks (11) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dulwich_log, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.08x
- 95% likely to have a slowdown of 1.07x
- 99% likely to have a slowdown of 1.06x

# Memory
- memory change: unknown