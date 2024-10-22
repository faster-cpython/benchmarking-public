# Results vs. 3.13.0

- fork: python
- ref: v3.14.0a1
- machine: windows-amd64
- commit hash: 8cdaca8
- commit date: 2024-10-15
- overall geometric mean: 1.08x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-pythonperf1-amd64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 217 ms                                                      | 231 ms: 1.07x slower                                            |
| docutils       | 1.57 sec                                                    | 1.72 sec: 1.09x slower                                          |
| html5lib       | 38.6 ms                                                     | 40.8 ms: 1.06x slower                                           |
| tornado_http   | 92.8 ms                                                     | 93.8 ms: 1.01x slower                                           |
| Geometric mean | (ref)                                                       | 1.06x slower                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-pythonperf1-amd64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_memoization_tg  | 288 ms                                                      | 266 ms: 1.09x faster                                            |
| asyncio_tcp_ssl            | 1.64 sec                                                    | 1.53 sec: 1.07x faster                                          |
| async_tree_memoization     | 271 ms                                                      | 281 ms: 1.04x slower                                            |
| async_tree_none_tg         | 206 ms                                                      | 215 ms: 1.04x slower                                            |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 407 ms: 1.09x slower                                            |
| async_tree_io              | 521 ms                                                      | 574 ms: 1.10x slower                                            |
| coroutines                 | 12.5 ms                                                     | 13.9 ms: 1.11x slower                                           |
| async_generators           | 223 ms                                                      | 249 ms: 1.12x slower                                            |
| async_tree_io_tg           | 512 ms                                                      | 645 ms: 1.26x slower                                            |
| Geometric mean             | (ref)                                                       | 1.05x slower                                                    |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed, asyncio_tcp, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-pythonperf1-amd64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| float          | 48.1 ms                                                     | 55.6 ms: 1.16x slower                                           |
| nbody          | 64.5 ms                                                     | 79.3 ms: 1.23x slower                                           |
| Geometric mean | (ref)                                                       | 1.12x slower                                                    |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-pythonperf1-amd64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.59 ms: 1.02x faster                                           |
| regex_dna      | 114 ms                                                      | 116 ms: 1.02x slower                                            |
| regex_v8       | 14.7 ms                                                     | 16.5 ms: 1.12x slower                                           |
| regex_compile  | 80.1 ms                                                     | 91.1 ms: 1.14x slower                                           |
| Geometric mean | (ref)                                                       | 1.06x slower                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-pythonperf1-amd64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| xml_etree_parse      | 93.2 ms                                                     | 95.4 ms: 1.02x slower                                           |
| pickle_list          | 2.89 us                                                     | 3.00 us: 1.04x slower                                           |
| unpickle_list        | 2.72 us                                                     | 2.83 us: 1.04x slower                                           |
| unpickle             | 8.63 us                                                     | 9.00 us: 1.04x slower                                           |
| xml_etree_iterparse  | 62.3 ms                                                     | 66.3 ms: 1.06x slower                                           |
| pickle_dict          | 18.0 us                                                     | 19.3 us: 1.07x slower                                           |
| json_loads           | 14.3 us                                                     | 15.5 us: 1.08x slower                                           |
| xml_etree_generate   | 53.3 ms                                                     | 59.3 ms: 1.11x slower                                           |
| xml_etree_process    | 36.5 ms                                                     | 41.7 ms: 1.14x slower                                           |
| tomli_loads          | 1.36 sec                                                    | 1.61 sec: 1.19x slower                                          |
| pickle_pure_python   | 183 us                                                      | 217 us: 1.19x slower                                            |
| unpickle_pure_python | 127 us                                                      | 151 us: 1.20x slower                                            |
| json_dumps           | 5.76 ms                                                     | 6.93 ms: 1.20x slower                                           |
| Geometric mean       | (ref)                                                       | 1.10x slower                                                    |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-pythonperf1-amd64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup_no_site | 17.8 ms                                                     | 18.3 ms: 1.03x slower                                           |
| python_startup         | 22.2 ms                                                     | 24.6 ms: 1.11x slower                                           |
| Geometric mean         | (ref)                                                       | 1.07x slower                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-pythonperf1-amd64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| mako            | 6.24 ms                                                     | 6.73 ms: 1.08x slower                                           |
| genshi_text     | 14.9 ms                                                     | 17.5 ms: 1.17x slower                                           |
| django_template | 21.8 ms                                                     | 25.9 ms: 1.19x slower                                           |
| genshi_xml      | 32.8 ms                                                     | 39.6 ms: 1.21x slower                                           |
| Geometric mean  | (ref)                                                       | 1.16x slower                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-pythonperf1-amd64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| thrift                     | 8.68 ms                                                     | 539 us: 16.11x faster                                           |
| deepcopy                   | 223 us                                                      | 194 us: 1.15x faster                                            |
| async_tree_memoization_tg  | 288 ms                                                      | 266 ms: 1.09x faster                                            |
| asyncio_tcp_ssl            | 1.64 sec                                                    | 1.53 sec: 1.07x faster                                          |
| deepcopy_memo              | 21.8 us                                                     | 20.4 us: 1.07x faster                                           |
| regex_effbot               | 1.62 ms                                                     | 1.59 ms: 1.02x faster                                           |
| telco                      | 4.85 ms                                                     | 4.89 ms: 1.01x slower                                           |
| tornado_http               | 92.8 ms                                                     | 93.8 ms: 1.01x slower                                           |
| regex_dna                  | 114 ms                                                      | 116 ms: 1.02x slower                                            |
| sqlite_synth               | 1.60 us                                                     | 1.63 us: 1.02x slower                                           |
| xml_etree_parse            | 93.2 ms                                                     | 95.4 ms: 1.02x slower                                           |
| python_startup_no_site     | 17.8 ms                                                     | 18.3 ms: 1.03x slower                                           |
| async_tree_memoization     | 271 ms                                                      | 281 ms: 1.04x slower                                            |
| pickle_list                | 2.89 us                                                     | 3.00 us: 1.04x slower                                           |
| unpickle_list              | 2.72 us                                                     | 2.83 us: 1.04x slower                                           |
| unpickle                   | 8.63 us                                                     | 9.00 us: 1.04x slower                                           |
| async_tree_none_tg         | 206 ms                                                      | 215 ms: 1.04x slower                                            |
| go                         | 84.6 ms                                                     | 88.5 ms: 1.05x slower                                           |
| coverage                   | 46.7 ms                                                     | 49.0 ms: 1.05x slower                                           |
| sympy_sum                  | 86.4 ms                                                     | 90.9 ms: 1.05x slower                                           |
| json                       | 2.98 ms                                                     | 3.15 ms: 1.06x slower                                           |
| html5lib                   | 38.6 ms                                                     | 40.8 ms: 1.06x slower                                           |
| xml_etree_iterparse        | 62.3 ms                                                     | 66.3 ms: 1.06x slower                                           |
| meteor_contest             | 72.3 ms                                                     | 77.0 ms: 1.06x slower                                           |
| 2to3                       | 217 ms                                                      | 231 ms: 1.07x slower                                            |
| unpack_sequence            | 40.0 ns                                                     | 42.7 ns: 1.07x slower                                           |
| pickle_dict                | 18.0 us                                                     | 19.3 us: 1.07x slower                                           |
| mako                       | 6.24 ms                                                     | 6.73 ms: 1.08x slower                                           |
| dulwich_log                | 40.4 ms                                                     | 43.6 ms: 1.08x slower                                           |
| mdp                        | 1.38 sec                                                    | 1.50 sec: 1.08x slower                                          |
| json_loads                 | 14.3 us                                                     | 15.5 us: 1.08x slower                                           |
| pylint                     | 211 ms                                                      | 229 ms: 1.08x slower                                            |
| sympy_str                  | 166 ms                                                      | 181 ms: 1.09x slower                                            |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 407 ms: 1.09x slower                                            |
| docutils                   | 1.57 sec                                                    | 1.72 sec: 1.09x slower                                          |
| sympy_expand               | 285 ms                                                      | 312 ms: 1.10x slower                                            |
| sympy_integrate            | 12.3 ms                                                     | 13.5 ms: 1.10x slower                                           |
| async_tree_io              | 521 ms                                                      | 574 ms: 1.10x slower                                            |
| coroutines                 | 12.5 ms                                                     | 13.9 ms: 1.11x slower                                           |
| python_startup             | 22.2 ms                                                     | 24.6 ms: 1.11x slower                                           |
| xml_etree_generate         | 53.3 ms                                                     | 59.3 ms: 1.11x slower                                           |
| logging_format             | 6.15 us                                                     | 6.85 us: 1.11x slower                                           |
| async_generators           | 223 ms                                                      | 249 ms: 1.12x slower                                            |
| typing_runtime_protocols   | 100 us                                                      | 112 us: 1.12x slower                                            |
| logging_simple             | 5.72 us                                                     | 6.42 us: 1.12x slower                                           |
| sqlglot_optimize           | 33.1 ms                                                     | 37.2 ms: 1.12x slower                                           |
| regex_v8                   | 14.7 ms                                                     | 16.5 ms: 1.12x slower                                           |
| generators                 | 19.5 ms                                                     | 22.1 ms: 1.13x slower                                           |
| regex_compile              | 80.1 ms                                                     | 91.1 ms: 1.14x slower                                           |
| xml_etree_process          | 36.5 ms                                                     | 41.7 ms: 1.14x slower                                           |
| scimark_sparse_mat_mult    | 2.34 ms                                                     | 2.68 ms: 1.15x slower                                           |
| pprint_safe_repr           | 493 ms                                                      | 565 ms: 1.15x slower                                            |
| nqueens                    | 55.5 ms                                                     | 63.9 ms: 1.15x slower                                           |
| pprint_pformat             | 991 ms                                                      | 1.14 sec: 1.15x slower                                          |
| float                      | 48.1 ms                                                     | 55.6 ms: 1.16x slower                                           |
| comprehensions             | 10.2 us                                                     | 11.9 us: 1.16x slower                                           |
| scimark_fft                | 174 ms                                                      | 202 ms: 1.16x slower                                            |
| sqlglot_normalize          | 171 ms                                                      | 199 ms: 1.16x slower                                            |
| fannkuch                   | 245 ms                                                      | 286 ms: 1.17x slower                                            |
| scimark_lu                 | 54.0 ms                                                     | 63.2 ms: 1.17x slower                                           |
| genshi_text                | 14.9 ms                                                     | 17.5 ms: 1.17x slower                                           |
| crypto_pyaes               | 42.8 ms                                                     | 50.3 ms: 1.18x slower                                           |
| chaos                      | 37.9 ms                                                     | 44.6 ms: 1.18x slower                                           |
| tomli_loads                | 1.36 sec                                                    | 1.61 sec: 1.19x slower                                          |
| pickle_pure_python         | 183 us                                                      | 217 us: 1.19x slower                                            |
| pyflate                    | 275 ms                                                      | 327 ms: 1.19x slower                                            |
| django_template            | 21.8 ms                                                     | 25.9 ms: 1.19x slower                                           |
| unpickle_pure_python       | 127 us                                                      | 151 us: 1.20x slower                                            |
| scimark_monte_carlo        | 40.3 ms                                                     | 48.2 ms: 1.20x slower                                           |
| sqlglot_transpile          | 952 us                                                      | 1.14 ms: 1.20x slower                                           |
| json_dumps                 | 5.76 ms                                                     | 6.93 ms: 1.20x slower                                           |
| bench_mp_pool              | 69.6 ms                                                     | 84.0 ms: 1.21x slower                                           |
| genshi_xml                 | 32.8 ms                                                     | 39.6 ms: 1.21x slower                                           |
| hexiom                     | 3.69 ms                                                     | 4.46 ms: 1.21x slower                                           |
| sqlglot_parse              | 761 us                                                      | 921 us: 1.21x slower                                            |
| deltablue                  | 1.86 ms                                                     | 2.29 ms: 1.23x slower                                           |
| nbody                      | 64.5 ms                                                     | 79.3 ms: 1.23x slower                                           |
| spectral_norm              | 59.2 ms                                                     | 72.9 ms: 1.23x slower                                           |
| logging_silent             | 51.0 ns                                                     | 62.9 ns: 1.23x slower                                           |
| richards                   | 26.0 ms                                                     | 32.3 ms: 1.24x slower                                           |
| richards_super             | 29.3 ms                                                     | 36.8 ms: 1.26x slower                                           |
| async_tree_io_tg           | 512 ms                                                      | 645 ms: 1.26x slower                                            |
| gc_traversal               | 1.55 ms                                                     | 1.97 ms: 1.27x slower                                           |
| raytrace                   | 156 ms                                                      | 198 ms: 1.27x slower                                            |
| scimark_sor                | 72.0 ms                                                     | 93.2 ms: 1.29x slower                                           |
| create_gc_cycles           | 829 us                                                      | 1.41 ms: 1.71x slower                                           |
| Geometric mean             | (ref)                                                       | 1.08x slower                                                    |

Benchmark hidden because not significant (9): pathlib, async_tree_cpu_io_mixed, pycparser, deepcopy_reduce, pidigits, bench_thread_pool, pickle, asyncio_tcp, async_tree_none
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, flaskblogging, mypy2
Ignored benchmarks (1) of results/bm-20241015-3.14.0a1-8cdaca8/bm-20241015-pythonperf1-amd64-python-v3.14.0a1-3.14.0a1-8cdaca8.json: sphinx

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.09x
- 95% likely to have a slowdown of 1.08x
- 99% likely to have a slowdown of 1.08x

# Memory
- memory change: unknown