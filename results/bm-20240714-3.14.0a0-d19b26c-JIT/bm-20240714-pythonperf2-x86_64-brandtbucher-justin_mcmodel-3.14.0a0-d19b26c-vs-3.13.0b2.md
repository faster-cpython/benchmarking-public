# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: justin_mcmodel
- machine: linux-x86_64
- commit hash: d19b26c
- commit date: 2024-07-14
- overall geometric mean: 1.02x faster
- HPT reliability: 73.63%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240714-pythonperf2-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 298 ms: 1.02x slower                                                        |
| docutils       | 2.98 sec                                                         | 3.10 sec: 1.04x slower                                                      |
| html5lib       | 74.7 ms                                                          | 69.1 ms: 1.08x faster                                                       |
| tornado_http   | 119 ms                                                           | 121 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                            | 1.00x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240714-pythonperf2-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization     | 460 ms                                                           | 405 ms: 1.13x faster                                                        |
| async_tree_io_tg           | 900 ms                                                           | 801 ms: 1.12x faster                                                        |
| async_tree_none_tg         | 340 ms                                                           | 304 ms: 1.12x faster                                                        |
| async_tree_memoization_tg  | 421 ms                                                           | 383 ms: 1.10x faster                                                        |
| async_tree_none            | 365 ms                                                           | 338 ms: 1.08x faster                                                        |
| async_tree_io              | 873 ms                                                           | 811 ms: 1.08x faster                                                        |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 540 ms: 1.06x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 579 ms: 1.04x faster                                                        |
| Geometric mean             | (ref)                                                            | 1.09x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240714-pythonperf2-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 80.2 ms                                                          | 73.2 ms: 1.09x faster                                                       |
| nbody          | 87.8 ms                                                          | 81.1 ms: 1.08x faster                                                       |
| pidigits       | 254 ms                                                           | 251 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                            | 1.06x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240714-pythonperf2-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                           | 133 ms: 1.08x faster                                                        |
| regex_v8       | 26.0 ms                                                          | 27.1 ms: 1.04x slower                                                       |
| regex_dna      | 249 ms                                                           | 262 ms: 1.05x slower                                                        |
| regex_effbot   | 3.40 ms                                                          | 3.58 ms: 1.05x slower                                                       |
| Geometric mean | (ref)                                                            | 1.02x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240714-pythonperf2-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.40 sec                                                         | 2.04 sec: 1.18x faster                                                      |
| xml_etree_generate   | 85.7 ms                                                          | 80.9 ms: 1.06x faster                                                       |
| xml_etree_iterparse  | 103 ms                                                           | 97.7 ms: 1.05x faster                                                       |
| xml_etree_process    | 59.7 ms                                                          | 57.6 ms: 1.04x faster                                                       |
| unpickle_pure_python | 224 us                                                           | 217 us: 1.03x faster                                                        |
| json_loads           | 25.0 us                                                          | 25.4 us: 1.01x slower                                                       |
| pickle_pure_python   | 307 us                                                           | 312 us: 1.02x slower                                                        |
| json_dumps           | 10.8 ms                                                          | 11.0 ms: 1.02x slower                                                       |
| Geometric mean       | (ref)                                                            | 1.03x faster                                                                |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240714-pythonperf2-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                          | 13.4 ms: 1.01x slower                                                       |
| python_startup_no_site | 8.85 ms                                                          | 9.04 ms: 1.02x slower                                                       |
| Geometric mean         | (ref)                                                            | 1.02x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240714-pythonperf2-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|-----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 10.4 ms                                                          | 8.96 ms: 1.16x faster                                                       |
| genshi_xml      | 58.1 ms                                                          | 58.8 ms: 1.01x slower                                                       |
| genshi_text     | 25.9 ms                                                          | 26.5 ms: 1.02x slower                                                       |
| django_template | 39.0 ms                                                          | 40.8 ms: 1.05x slower                                                       |
| Geometric mean  | (ref)                                                            | 1.02x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240714-pythonperf2-x86_64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo              | 37.3 us                                                          | 28.6 us: 1.30x faster                                                       |
| deepcopy                   | 377 us                                                           | 301 us: 1.25x faster                                                        |
| richards                   | 53.4 ms                                                          | 43.0 ms: 1.24x faster                                                       |
| richards_super             | 61.2 ms                                                          | 49.6 ms: 1.23x faster                                                       |
| tomli_loads                | 2.40 sec                                                         | 2.04 sec: 1.18x faster                                                      |
| spectral_norm              | 97.3 ms                                                          | 82.9 ms: 1.17x faster                                                       |
| mako                       | 10.4 ms                                                          | 8.96 ms: 1.16x faster                                                       |
| async_tree_memoization     | 460 ms                                                           | 405 ms: 1.13x faster                                                        |
| async_tree_io_tg           | 900 ms                                                           | 801 ms: 1.12x faster                                                        |
| deepcopy_reduce            | 3.39 us                                                          | 3.02 us: 1.12x faster                                                       |
| async_tree_none_tg         | 340 ms                                                           | 304 ms: 1.12x faster                                                        |
| pyflate                    | 482 ms                                                           | 438 ms: 1.10x faster                                                        |
| async_tree_memoization_tg  | 421 ms                                                           | 383 ms: 1.10x faster                                                        |
| float                      | 80.2 ms                                                          | 73.2 ms: 1.09x faster                                                       |
| nbody                      | 87.8 ms                                                          | 81.1 ms: 1.08x faster                                                       |
| async_tree_none            | 365 ms                                                           | 338 ms: 1.08x faster                                                        |
| regex_compile              | 144 ms                                                           | 133 ms: 1.08x faster                                                        |
| html5lib                   | 74.7 ms                                                          | 69.1 ms: 1.08x faster                                                       |
| async_tree_io              | 873 ms                                                           | 811 ms: 1.08x faster                                                        |
| go                         | 165 ms                                                           | 155 ms: 1.07x faster                                                        |
| pathlib                    | 17.1 ms                                                          | 16.1 ms: 1.06x faster                                                       |
| xml_etree_generate         | 85.7 ms                                                          | 80.9 ms: 1.06x faster                                                       |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 540 ms: 1.06x faster                                                        |
| gc_traversal               | 4.69 ms                                                          | 4.43 ms: 1.06x faster                                                       |
| crypto_pyaes               | 73.6 ms                                                          | 70.1 ms: 1.05x faster                                                       |
| xml_etree_iterparse        | 103 ms                                                           | 97.7 ms: 1.05x faster                                                       |
| create_gc_cycles           | 2.00 ms                                                          | 1.92 ms: 1.05x faster                                                       |
| coroutines                 | 22.0 ms                                                          | 21.0 ms: 1.04x faster                                                       |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 579 ms: 1.04x faster                                                        |
| xml_etree_process          | 59.7 ms                                                          | 57.6 ms: 1.04x faster                                                       |
| pprint_pformat             | 1.66 sec                                                         | 1.60 sec: 1.04x faster                                                      |
| unpickle_pure_python       | 224 us                                                           | 217 us: 1.03x faster                                                        |
| pprint_safe_repr           | 818 ms                                                           | 794 ms: 1.03x faster                                                        |
| logging_simple             | 6.40 us                                                          | 6.27 us: 1.02x faster                                                       |
| dulwich_log                | 67.3 ms                                                          | 65.9 ms: 1.02x faster                                                       |
| fannkuch                   | 353 ms                                                           | 346 ms: 1.02x faster                                                        |
| scimark_sparse_mat_mult    | 4.28 ms                                                          | 4.20 ms: 1.02x faster                                                       |
| pycparser                  | 1.22 sec                                                         | 1.20 sec: 1.02x faster                                                      |
| logging_format             | 7.11 us                                                          | 7.00 us: 1.02x faster                                                       |
| pidigits                   | 254 ms                                                           | 251 ms: 1.01x faster                                                        |
| asyncio_websockets         | 395 ms                                                           | 391 ms: 1.01x faster                                                        |
| coverage                   | 83.5 ms                                                          | 82.8 ms: 1.01x faster                                                       |
| python_startup             | 13.2 ms                                                          | 13.4 ms: 1.01x slower                                                       |
| genshi_xml                 | 58.1 ms                                                          | 58.8 ms: 1.01x slower                                                       |
| meteor_contest             | 128 ms                                                           | 130 ms: 1.01x slower                                                        |
| bpe_tokeniser              | 5.14 sec                                                         | 5.21 sec: 1.01x slower                                                      |
| json_loads                 | 25.0 us                                                          | 25.4 us: 1.01x slower                                                       |
| tornado_http               | 119 ms                                                           | 121 ms: 1.02x slower                                                        |
| pickle_pure_python         | 307 us                                                           | 312 us: 1.02x slower                                                        |
| dask                       | 391 ms                                                           | 397 ms: 1.02x slower                                                        |
| bench_thread_pool          | 908 us                                                           | 924 us: 1.02x slower                                                        |
| thrift                     | 880 us                                                           | 897 us: 1.02x slower                                                        |
| genshi_text                | 25.9 ms                                                          | 26.5 ms: 1.02x slower                                                       |
| python_startup_no_site     | 8.85 ms                                                          | 9.04 ms: 1.02x slower                                                       |
| scimark_monte_carlo        | 65.5 ms                                                          | 66.9 ms: 1.02x slower                                                       |
| sympy_expand               | 501 ms                                                           | 512 ms: 1.02x slower                                                        |
| sqlglot_transpile          | 1.76 ms                                                          | 1.80 ms: 1.02x slower                                                       |
| json_dumps                 | 10.8 ms                                                          | 11.0 ms: 1.02x slower                                                       |
| 2to3                       | 291 ms                                                           | 298 ms: 1.02x slower                                                        |
| generators                 | 33.5 ms                                                          | 34.4 ms: 1.03x slower                                                       |
| json                       | 5.35 ms                                                          | 5.50 ms: 1.03x slower                                                       |
| sympy_str                  | 295 ms                                                           | 303 ms: 1.03x slower                                                        |
| hexiom                     | 6.35 ms                                                          | 6.57 ms: 1.03x slower                                                       |
| async_generators           | 363 ms                                                           | 376 ms: 1.04x slower                                                        |
| docutils                   | 2.98 sec                                                         | 3.10 sec: 1.04x slower                                                      |
| regex_v8                   | 26.0 ms                                                          | 27.1 ms: 1.04x slower                                                       |
| sqlglot_optimize           | 59.5 ms                                                          | 62.2 ms: 1.04x slower                                                       |
| scimark_sor                | 119 ms                                                           | 124 ms: 1.05x slower                                                        |
| django_template            | 39.0 ms                                                          | 40.8 ms: 1.05x slower                                                       |
| regex_dna                  | 249 ms                                                           | 262 ms: 1.05x slower                                                        |
| regex_effbot               | 3.40 ms                                                          | 3.58 ms: 1.05x slower                                                       |
| sympy_sum                  | 155 ms                                                           | 164 ms: 1.06x slower                                                        |
| deltablue                  | 3.37 ms                                                          | 3.57 ms: 1.06x slower                                                       |
| raytrace                   | 260 ms                                                           | 275 ms: 1.06x slower                                                        |
| sqlglot_normalize          | 120 ms                                                           | 128 ms: 1.06x slower                                                        |
| mdp                        | 2.46 sec                                                         | 2.62 sec: 1.06x slower                                                      |
| comprehensions             | 17.0 us                                                          | 18.1 us: 1.07x slower                                                       |
| nqueens                    | 88.4 ms                                                          | 94.7 ms: 1.07x slower                                                       |
| chaos                      | 59.6 ms                                                          | 64.3 ms: 1.08x slower                                                       |
| typing_runtime_protocols   | 171 us                                                           | 185 us: 1.08x slower                                                        |
| logging_silent             | 96.3 ns                                                          | 105 ns: 1.09x slower                                                        |
| sympy_integrate            | 23.2 ms                                                          | 25.4 ms: 1.10x slower                                                       |
| pylint                     | 339 ms                                                           | 372 ms: 1.10x slower                                                        |
| scimark_lu                 | 97.5 ms                                                          | 123 ms: 1.26x slower                                                        |
| Geometric mean             | (ref)                                                            | 1.02x faster                                                                |

Benchmark hidden because not significant (7): bench_mp_pool, scimark_fft, telco, asyncio_tcp_ssl, xml_etree_parse, sqlglot_parse, asyncio_tcp
Ignored benchmarks (11) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 73.63% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.06x