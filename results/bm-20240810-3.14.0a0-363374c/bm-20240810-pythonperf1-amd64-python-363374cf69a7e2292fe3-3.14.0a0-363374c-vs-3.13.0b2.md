# Results vs. 3.13.0b2

- fork: python
- ref: 363374cf69a7e2292fe3
- machine: windows-amd64
- commit hash: 363374c
- commit date: 2024-08-10
- overall geometric mean: 1.08x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240810-pythonperf1-amd64-python-363374cf69a7e2292fe3-3.14.0a0-363374c |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 207 ms                                                          | 233 ms: 1.13x slower                                                       |
| docutils       | 1.63 sec                                                        | 1.78 sec: 1.09x slower                                                     |
| html5lib       | 35.0 ms                                                         | 42.4 ms: 1.21x slower                                                      |
| tornado_http   | 81.8 ms                                                         | 94.9 ms: 1.16x slower                                                      |
| Geometric mean | (ref)                                                           | 1.15x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240810-pythonperf1-amd64-python-363374cf69a7e2292fe3-3.14.0a0-363374c |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io_tg           | 605 ms                                                          | 550 ms: 1.10x faster                                                       |
| async_tree_memoization_tg  | 258 ms                                                          | 248 ms: 1.04x faster                                                       |
| async_tree_cpu_io_mixed_tg | 382 ms                                                          | 398 ms: 1.04x slower                                                       |
| Geometric mean             | (ref)                                                           | 1.01x faster                                                               |

Benchmark hidden because not significant (5): async_tree_none_tg, async_tree_io, async_tree_memoization, async_tree_none, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240810-pythonperf1-amd64-python-363374cf69a7e2292fe3-3.14.0a0-363374c |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pidigits       | 150 ms                                                          | 151 ms: 1.01x slower                                                       |
| float          | 49.7 ms                                                         | 55.5 ms: 1.12x slower                                                      |
| nbody          | 67.6 ms                                                         | 84.9 ms: 1.26x slower                                                      |
| Geometric mean | (ref)                                                           | 1.12x slower                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240810-pythonperf1-amd64-python-363374cf69a7e2292fe3-3.14.0a0-363374c |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_dna      | 119 ms                                                          | 118 ms: 1.01x faster                                                       |
| regex_compile  | 78.0 ms                                                         | 92.3 ms: 1.18x slower                                                      |
| Geometric mean | (ref)                                                           | 1.03x slower                                                               |

Benchmark hidden because not significant (2): regex_v8, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240810-pythonperf1-amd64-python-363374cf69a7e2292fe3-3.14.0a0-363374c |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_loads           | 14.2 us                                                         | 14.3 us: 1.01x slower                                                      |
| xml_etree_parse      | 90.9 ms                                                         | 95.4 ms: 1.05x slower                                                      |
| xml_etree_generate   | 53.2 ms                                                         | 59.0 ms: 1.11x slower                                                      |
| xml_etree_iterparse  | 62.3 ms                                                         | 69.7 ms: 1.12x slower                                                      |
| json_dumps           | 5.61 ms                                                         | 6.34 ms: 1.13x slower                                                      |
| xml_etree_process    | 36.4 ms                                                         | 41.7 ms: 1.15x slower                                                      |
| tomli_loads          | 1.35 sec                                                        | 1.62 sec: 1.20x slower                                                     |
| pickle_pure_python   | 175 us                                                          | 215 us: 1.22x slower                                                       |
| unpickle_pure_python | 122 us                                                          | 153 us: 1.25x slower                                                       |
| Geometric mean       | (ref)                                                           | 1.13x slower                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240810-pythonperf1-amd64-python-363374cf69a7e2292fe3-3.14.0a0-363374c |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 20.3 ms                                                         | 21.9 ms: 1.08x slower                                                      |
| python_startup_no_site | 16.2 ms                                                         | 17.7 ms: 1.09x slower                                                      |
| Geometric mean         | (ref)                                                           | 1.08x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240810-pythonperf1-amd64-python-363374cf69a7e2292fe3-3.14.0a0-363374c |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 6.36 ms                                                         | 6.85 ms: 1.08x slower                                                      |
| django_template | 21.7 ms                                                         | 24.8 ms: 1.14x slower                                                      |
| genshi_xml      | 31.6 ms                                                         | 36.6 ms: 1.16x slower                                                      |
| genshi_text     | 14.4 ms                                                         | 17.7 ms: 1.23x slower                                                      |
| Geometric mean  | (ref)                                                           | 1.15x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240810-pythonperf1-amd64-python-363374cf69a7e2292fe3-3.14.0a0-363374c |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| thrift                     | 8.11 ms                                                         | 524 us: 15.47x faster                                                      |
| deepcopy                   | 220 us                                                          | 191 us: 1.15x faster                                                       |
| async_tree_io_tg           | 605 ms                                                          | 550 ms: 1.10x faster                                                       |
| deepcopy_memo              | 22.1 us                                                         | 21.1 us: 1.05x faster                                                      |
| async_tree_memoization_tg  | 258 ms                                                          | 248 ms: 1.04x faster                                                       |
| deepcopy_reduce            | 1.99 us                                                         | 1.96 us: 1.02x faster                                                      |
| regex_dna                  | 119 ms                                                          | 118 ms: 1.01x faster                                                       |
| json_loads                 | 14.2 us                                                         | 14.3 us: 1.01x slower                                                      |
| pidigits                   | 150 ms                                                          | 151 ms: 1.01x slower                                                       |
| gc_traversal               | 1.55 ms                                                         | 1.57 ms: 1.01x slower                                                      |
| create_gc_cycles           | 888 us                                                          | 920 us: 1.04x slower                                                       |
| async_tree_cpu_io_mixed_tg | 382 ms                                                          | 398 ms: 1.04x slower                                                       |
| xml_etree_parse            | 90.9 ms                                                         | 95.4 ms: 1.05x slower                                                      |
| sympy_sum                  | 84.4 ms                                                         | 88.9 ms: 1.05x slower                                                      |
| bench_thread_pool          | 768 us                                                          | 814 us: 1.06x slower                                                       |
| telco                      | 4.67 ms                                                         | 4.99 ms: 1.07x slower                                                      |
| pathlib                    | 75.9 ms                                                         | 81.2 ms: 1.07x slower                                                      |
| bench_mp_pool              | 64.8 ms                                                         | 69.5 ms: 1.07x slower                                                      |
| python_startup             | 20.3 ms                                                         | 21.9 ms: 1.08x slower                                                      |
| mako                       | 6.36 ms                                                         | 6.85 ms: 1.08x slower                                                      |
| sympy_integrate            | 12.2 ms                                                         | 13.3 ms: 1.09x slower                                                      |
| python_startup_no_site     | 16.2 ms                                                         | 17.7 ms: 1.09x slower                                                      |
| docutils                   | 1.63 sec                                                        | 1.78 sec: 1.09x slower                                                     |
| generators                 | 19.6 ms                                                         | 21.4 ms: 1.09x slower                                                      |
| async_generators           | 223 ms                                                          | 246 ms: 1.10x slower                                                       |
| logging_simple             | 5.78 us                                                         | 6.37 us: 1.10x slower                                                      |
| logging_format             | 6.22 us                                                         | 6.88 us: 1.11x slower                                                      |
| sympy_expand               | 271 ms                                                          | 299 ms: 1.11x slower                                                       |
| meteor_contest             | 69.9 ms                                                         | 77.4 ms: 1.11x slower                                                      |
| xml_etree_generate         | 53.2 ms                                                         | 59.0 ms: 1.11x slower                                                      |
| sympy_str                  | 159 ms                                                          | 177 ms: 1.11x slower                                                       |
| coroutines                 | 12.8 ms                                                         | 14.2 ms: 1.12x slower                                                      |
| float                      | 49.7 ms                                                         | 55.5 ms: 1.12x slower                                                      |
| xml_etree_iterparse        | 62.3 ms                                                         | 69.7 ms: 1.12x slower                                                      |
| sqlglot_optimize           | 32.7 ms                                                         | 36.6 ms: 1.12x slower                                                      |
| scimark_sparse_mat_mult    | 2.50 ms                                                         | 2.81 ms: 1.12x slower                                                      |
| pylint                     | 205 ms                                                          | 230 ms: 1.12x slower                                                       |
| coverage                   | 42.1 ms                                                         | 47.3 ms: 1.12x slower                                                      |
| 2to3                       | 207 ms                                                          | 233 ms: 1.13x slower                                                       |
| json_dumps                 | 5.61 ms                                                         | 6.34 ms: 1.13x slower                                                      |
| dulwich_log                | 38.0 ms                                                         | 43.2 ms: 1.13x slower                                                      |
| asyncio_tcp                | 471 ms                                                          | 535 ms: 1.14x slower                                                       |
| django_template            | 21.7 ms                                                         | 24.8 ms: 1.14x slower                                                      |
| scimark_lu                 | 56.6 ms                                                         | 64.7 ms: 1.14x slower                                                      |
| spectral_norm              | 63.7 ms                                                         | 73.0 ms: 1.14x slower                                                      |
| sqlglot_normalize          | 173 ms                                                          | 198 ms: 1.14x slower                                                       |
| xml_etree_process          | 36.4 ms                                                         | 41.7 ms: 1.15x slower                                                      |
| crypto_pyaes               | 45.5 ms                                                         | 52.1 ms: 1.15x slower                                                      |
| sqlglot_transpile          | 955 us                                                          | 1.09 ms: 1.15x slower                                                      |
| nqueens                    | 56.7 ms                                                         | 65.1 ms: 1.15x slower                                                      |
| chaos                      | 38.4 ms                                                         | 44.3 ms: 1.16x slower                                                      |
| genshi_xml                 | 31.6 ms                                                         | 36.6 ms: 1.16x slower                                                      |
| tornado_http               | 81.8 ms                                                         | 94.9 ms: 1.16x slower                                                      |
| mdp                        | 1.31 sec                                                        | 1.53 sec: 1.16x slower                                                     |
| comprehensions             | 10.4 us                                                         | 12.1 us: 1.17x slower                                                      |
| pyflate                    | 279 ms                                                          | 325 ms: 1.17x slower                                                       |
| typing_runtime_protocols   | 101 us                                                          | 118 us: 1.17x slower                                                       |
| sqlglot_parse              | 748 us                                                          | 878 us: 1.17x slower                                                       |
| pycparser                  | 754 ms                                                          | 892 ms: 1.18x slower                                                       |
| regex_compile              | 78.0 ms                                                         | 92.3 ms: 1.18x slower                                                      |
| scimark_fft                | 171 ms                                                          | 203 ms: 1.19x slower                                                       |
| raytrace                   | 162 ms                                                          | 193 ms: 1.19x slower                                                       |
| tomli_loads                | 1.35 sec                                                        | 1.62 sec: 1.20x slower                                                     |
| html5lib                   | 35.0 ms                                                         | 42.4 ms: 1.21x slower                                                      |
| pprint_safe_repr           | 474 ms                                                          | 575 ms: 1.21x slower                                                       |
| deltablue                  | 1.88 ms                                                         | 2.29 ms: 1.22x slower                                                      |
| pprint_pformat             | 966 ms                                                          | 1.18 sec: 1.22x slower                                                     |
| fannkuch                   | 243 ms                                                          | 297 ms: 1.22x slower                                                       |
| logging_silent             | 52.9 ns                                                         | 64.7 ns: 1.22x slower                                                      |
| pickle_pure_python         | 175 us                                                          | 215 us: 1.22x slower                                                       |
| go                         | 82.1 ms                                                         | 101 ms: 1.23x slower                                                       |
| genshi_text                | 14.4 ms                                                         | 17.7 ms: 1.23x slower                                                      |
| hexiom                     | 3.72 ms                                                         | 4.59 ms: 1.23x slower                                                      |
| scimark_sor                | 75.3 ms                                                         | 93.1 ms: 1.24x slower                                                      |
| unpickle_pure_python       | 122 us                                                          | 153 us: 1.25x slower                                                       |
| nbody                      | 67.6 ms                                                         | 84.9 ms: 1.26x slower                                                      |
| richards_super             | 30.2 ms                                                         | 37.9 ms: 1.26x slower                                                      |
| richards                   | 26.7 ms                                                         | 33.7 ms: 1.26x slower                                                      |
| scimark_monte_carlo        | 39.1 ms                                                         | 49.8 ms: 1.27x slower                                                      |
| Geometric mean             | (ref)                                                           | 1.08x slower                                                               |

Benchmark hidden because not significant (9): regex_v8, async_tree_none_tg, async_tree_io, regex_effbot, async_tree_memoization, async_tree_none, async_tree_cpu_io_mixed, json, asyncio_tcp_ssl
Ignored benchmarks (10) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.10x
- 95% likely to have a slowdown of 1.10x
- 99% likely to have a slowdown of 1.09x

# Memory
- memory change: unknown