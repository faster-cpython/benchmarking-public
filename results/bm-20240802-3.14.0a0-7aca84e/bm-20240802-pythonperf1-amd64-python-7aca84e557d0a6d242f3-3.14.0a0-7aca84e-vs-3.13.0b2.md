# Results vs. 3.13.0b2

- fork: python
- ref: 7aca84e557d0a6d242f3
- machine: windows-amd64
- commit hash: 7aca84e
- commit date: 2024-08-02
- overall geometric mean: 1.09x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 236 ms: 1.14x slower                                                       |
| docutils       | 1.63 sec                                                        | 1.79 sec: 1.10x slower                                                     |
| html5lib       | 35.0 ms                                                         | 42.0 ms: 1.20x slower                                                      |
| tornado_http   | 81.8 ms                                                         | 95.3 ms: 1.16x slower                                                      |
| Geometric mean | (ref)                                                           | 1.15x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 605 ms                                                          | 559 ms: 1.08x faster                                                       |
| async_tree_cpu_io_mixed_tg | 382 ms                                                          | 396 ms: 1.04x slower                                                       |
| Geometric mean             | (ref)                                                           | 1.00x slower                                                               |

Benchmark hidden because not significant (6): async_tree_memoization_tg, async_tree_none_tg, async_tree_cpu_io_mixed, async_tree_io, async_tree_none, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 150 ms                                                          | 151 ms: 1.01x slower                                                       |
| float          | 49.7 ms                                                         | 57.0 ms: 1.15x slower                                                      |
| nbody          | 67.6 ms                                                         | 85.4 ms: 1.26x slower                                                      |
| Geometric mean | (ref)                                                           | 1.13x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 119 ms                                                          | 115 ms: 1.04x faster                                                       |
| regex_effbot   | 1.58 ms                                                         | 1.57 ms: 1.01x faster                                                      |
| regex_compile  | 78.0 ms                                                         | 94.5 ms: 1.21x slower                                                      |
| Geometric mean | (ref)                                                           | 1.05x slower                                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_loads           | 14.2 us                                                         | 14.3 us: 1.01x slower                                                      |
| xml_etree_parse      | 90.9 ms                                                         | 94.8 ms: 1.04x slower                                                      |
| xml_etree_iterparse  | 62.3 ms                                                         | 66.6 ms: 1.07x slower                                                      |
| xml_etree_generate   | 53.2 ms                                                         | 58.7 ms: 1.10x slower                                                      |
| json_dumps           | 5.61 ms                                                         | 6.26 ms: 1.12x slower                                                      |
| xml_etree_process    | 36.4 ms                                                         | 42.1 ms: 1.16x slower                                                      |
| tomli_loads          | 1.35 sec                                                        | 1.62 sec: 1.20x slower                                                     |
| unpickle_pure_python | 122 us                                                          | 153 us: 1.25x slower                                                       |
| pickle_pure_python   | 175 us                                                          | 221 us: 1.26x slower                                                       |
| Geometric mean       | (ref)                                                           | 1.13x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.3 ms                                                         | 22.2 ms: 1.09x slower                                                      |
| python_startup_no_site | 16.2 ms                                                         | 17.8 ms: 1.10x slower                                                      |
| Geometric mean         | (ref)                                                           | 1.10x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.36 ms                                                         | 7.06 ms: 1.11x slower                                                      |
| genshi_xml      | 31.6 ms                                                         | 37.4 ms: 1.19x slower                                                      |
| django_template | 21.7 ms                                                         | 26.1 ms: 1.21x slower                                                      |
| genshi_text     | 14.4 ms                                                         | 17.8 ms: 1.24x slower                                                      |
| Geometric mean  | (ref)                                                           | 1.18x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240802-pythonperf1-amd64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.11 ms                                                         | 524 us: 15.47x faster                                                      |
| deepcopy                   | 220 us                                                          | 189 us: 1.16x faster                                                       |
| async_tree_io_tg           | 605 ms                                                          | 559 ms: 1.08x faster                                                       |
| deepcopy_memo              | 22.1 us                                                         | 20.7 us: 1.07x faster                                                      |
| json                       | 3.19 ms                                                         | 3.01 ms: 1.06x faster                                                      |
| regex_dna                  | 119 ms                                                          | 115 ms: 1.04x faster                                                       |
| deepcopy_reduce            | 1.99 us                                                         | 1.96 us: 1.02x faster                                                      |
| regex_effbot               | 1.58 ms                                                         | 1.57 ms: 1.01x faster                                                      |
| json_loads                 | 14.2 us                                                         | 14.3 us: 1.01x slower                                                      |
| pidigits                   | 150 ms                                                          | 151 ms: 1.01x slower                                                       |
| gc_traversal               | 1.55 ms                                                         | 1.57 ms: 1.01x slower                                                      |
| create_gc_cycles           | 888 us                                                          | 912 us: 1.03x slower                                                       |
| async_tree_cpu_io_mixed_tg | 382 ms                                                          | 396 ms: 1.04x slower                                                       |
| xml_etree_parse            | 90.9 ms                                                         | 94.8 ms: 1.04x slower                                                      |
| scimark_sparse_mat_mult    | 2.50 ms                                                         | 2.62 ms: 1.05x slower                                                      |
| xml_etree_iterparse        | 62.3 ms                                                         | 66.6 ms: 1.07x slower                                                      |
| bench_mp_pool              | 64.8 ms                                                         | 69.4 ms: 1.07x slower                                                      |
| pathlib                    | 75.9 ms                                                         | 81.5 ms: 1.07x slower                                                      |
| pycparser                  | 754 ms                                                          | 811 ms: 1.08x slower                                                       |
| bench_thread_pool          | 768 us                                                          | 837 us: 1.09x slower                                                       |
| python_startup             | 20.3 ms                                                         | 22.2 ms: 1.09x slower                                                      |
| telco                      | 4.67 ms                                                         | 5.13 ms: 1.10x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                         | 17.8 ms: 1.10x slower                                                      |
| xml_etree_generate         | 53.2 ms                                                         | 58.7 ms: 1.10x slower                                                      |
| docutils                   | 1.63 sec                                                        | 1.79 sec: 1.10x slower                                                     |
| meteor_contest             | 69.9 ms                                                         | 77.2 ms: 1.10x slower                                                      |
| sympy_integrate            | 12.2 ms                                                         | 13.5 ms: 1.10x slower                                                      |
| coroutines                 | 12.8 ms                                                         | 14.1 ms: 1.11x slower                                                      |
| mako                       | 6.36 ms                                                         | 7.06 ms: 1.11x slower                                                      |
| generators                 | 19.6 ms                                                         | 21.8 ms: 1.11x slower                                                      |
| sympy_sum                  | 84.4 ms                                                         | 94.0 ms: 1.11x slower                                                      |
| json_dumps                 | 5.61 ms                                                         | 6.26 ms: 1.12x slower                                                      |
| coverage                   | 42.1 ms                                                         | 47.2 ms: 1.12x slower                                                      |
| asyncio_tcp_ssl            | 1.48 sec                                                        | 1.67 sec: 1.12x slower                                                     |
| logging_format             | 6.22 us                                                         | 7.01 us: 1.13x slower                                                      |
| async_generators           | 223 ms                                                          | 252 ms: 1.13x slower                                                       |
| logging_simple             | 5.78 us                                                         | 6.52 us: 1.13x slower                                                      |
| pylint                     | 205 ms                                                          | 232 ms: 1.14x slower                                                       |
| 2to3                       | 207 ms                                                          | 236 ms: 1.14x slower                                                       |
| crypto_pyaes               | 45.5 ms                                                         | 52.0 ms: 1.14x slower                                                      |
| sympy_str                  | 159 ms                                                          | 182 ms: 1.14x slower                                                       |
| typing_runtime_protocols   | 101 us                                                          | 116 us: 1.14x slower                                                       |
| float                      | 49.7 ms                                                         | 57.0 ms: 1.15x slower                                                      |
| scimark_lu                 | 56.6 ms                                                         | 64.8 ms: 1.15x slower                                                      |
| sqlglot_optimize           | 32.7 ms                                                         | 37.8 ms: 1.16x slower                                                      |
| nqueens                    | 56.7 ms                                                         | 65.5 ms: 1.16x slower                                                      |
| xml_etree_process          | 36.4 ms                                                         | 42.1 ms: 1.16x slower                                                      |
| sympy_expand               | 271 ms                                                          | 314 ms: 1.16x slower                                                       |
| tornado_http               | 81.8 ms                                                         | 95.3 ms: 1.16x slower                                                      |
| dulwich_log                | 38.0 ms                                                         | 44.5 ms: 1.17x slower                                                      |
| sqlglot_normalize          | 173 ms                                                          | 203 ms: 1.17x slower                                                       |
| chaos                      | 38.4 ms                                                         | 44.9 ms: 1.17x slower                                                      |
| spectral_norm              | 63.7 ms                                                         | 74.7 ms: 1.17x slower                                                      |
| sqlglot_transpile          | 955 us                                                          | 1.13 ms: 1.18x slower                                                      |
| scimark_fft                | 171 ms                                                          | 202 ms: 1.18x slower                                                       |
| genshi_xml                 | 31.6 ms                                                         | 37.4 ms: 1.19x slower                                                      |
| pyflate                    | 279 ms                                                          | 332 ms: 1.19x slower                                                       |
| html5lib                   | 35.0 ms                                                         | 42.0 ms: 1.20x slower                                                      |
| tomli_loads                | 1.35 sec                                                        | 1.62 sec: 1.20x slower                                                     |
| comprehensions             | 10.4 us                                                         | 12.5 us: 1.20x slower                                                      |
| mdp                        | 1.31 sec                                                        | 1.58 sec: 1.20x slower                                                     |
| django_template            | 21.7 ms                                                         | 26.1 ms: 1.21x slower                                                      |
| sqlglot_parse              | 748 us                                                          | 903 us: 1.21x slower                                                       |
| regex_compile              | 78.0 ms                                                         | 94.5 ms: 1.21x slower                                                      |
| fannkuch                   | 243 ms                                                          | 296 ms: 1.22x slower                                                       |
| pprint_pformat             | 966 ms                                                          | 1.18 sec: 1.23x slower                                                     |
| pprint_safe_repr           | 474 ms                                                          | 581 ms: 1.23x slower                                                       |
| go                         | 82.1 ms                                                         | 101 ms: 1.24x slower                                                       |
| logging_silent             | 52.9 ns                                                         | 65.5 ns: 1.24x slower                                                      |
| genshi_text                | 14.4 ms                                                         | 17.8 ms: 1.24x slower                                                      |
| unpickle_pure_python       | 122 us                                                          | 153 us: 1.25x slower                                                       |
| deltablue                  | 1.88 ms                                                         | 2.37 ms: 1.26x slower                                                      |
| pickle_pure_python         | 175 us                                                          | 221 us: 1.26x slower                                                       |
| hexiom                     | 3.72 ms                                                         | 4.70 ms: 1.26x slower                                                      |
| nbody                      | 67.6 ms                                                         | 85.4 ms: 1.26x slower                                                      |
| raytrace                   | 162 ms                                                          | 206 ms: 1.27x slower                                                       |
| scimark_sor                | 75.3 ms                                                         | 95.8 ms: 1.27x slower                                                      |
| scimark_monte_carlo        | 39.1 ms                                                         | 50.4 ms: 1.29x slower                                                      |
| richards                   | 26.7 ms                                                         | 34.7 ms: 1.30x slower                                                      |
| richards_super             | 30.2 ms                                                         | 39.3 ms: 1.30x slower                                                      |
| asyncio_tcp                | 471 ms                                                          | 637 ms: 1.35x slower                                                       |
| Geometric mean             | (ref)                                                           | 1.09x slower                                                               |

Benchmark hidden because not significant (7): async_tree_memoization_tg, async_tree_none_tg, async_tree_cpu_io_mixed, async_tree_io, async_tree_none, async_tree_memoization, regex_v8
Ignored benchmarks (10) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.11x
- 95% likely to have a slowdown of 1.11x
- 99% likely to have a slowdown of 1.10x

# Memory
- memory change: unknown