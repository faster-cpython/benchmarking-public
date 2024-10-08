# Results vs. 3.13.0b2

- fork: python
- ref: 34ddb64d088dd7ccc321
- machine: linux-aarch64
- commit hash: 34ddb64
- commit date: 2024-08-31
- overall geometric mean: 1.03x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 305 ms                                                       | 294 ms: 1.03x faster                                                    |
| docutils       | 3.10 sec                                                     | 3.04 sec: 1.02x faster                                                  |
| html5lib       | 66.1 ms                                                      | 63.7 ms: 1.04x faster                                                   |
| Geometric mean | (ref)                                                        | 1.02x faster                                                            |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 492 ms                                                       | 422 ms: 1.17x faster                                                    |
| async_tree_memoization     | 645 ms                                                       | 559 ms: 1.15x faster                                                    |
| async_tree_none_tg         | 476 ms                                                       | 416 ms: 1.14x faster                                                    |
| async_tree_memoization_tg  | 604 ms                                                       | 544 ms: 1.11x faster                                                    |
| async_tree_io_tg           | 1.27 sec                                                     | 1.16 sec: 1.09x faster                                                  |
| async_tree_io              | 1.22 sec                                                     | 1.12 sec: 1.09x faster                                                  |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 726 ms: 1.09x faster                                                    |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 722 ms: 1.06x faster                                                    |
| Geometric mean             | (ref)                                                        | 1.11x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 114 ms                                                       | 109 ms: 1.05x faster                                                    |
| float          | 91.4 ms                                                      | 92.7 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                        | 1.01x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 31.1 ms                                                      | 30.2 ms: 1.03x faster                                                   |
| regex_dna      | 259 ms                                                       | 254 ms: 1.02x faster                                                    |
| regex_compile  | 128 ms                                                       | 126 ms: 1.02x faster                                                    |
| regex_effbot   | 4.98 ms                                                      | 4.89 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                        | 1.02x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_process    | 80.8 ms                                                      | 79.1 ms: 1.02x faster                                                   |
| unpickle_pure_python | 251 us                                                       | 254 us: 1.01x slower                                                    |
| json_loads           | 32.1 us                                                      | 32.5 us: 1.01x slower                                                   |
| tomli_loads          | 2.57 sec                                                     | 2.62 sec: 1.02x slower                                                  |
| json_dumps           | 13.1 ms                                                      | 13.4 ms: 1.02x slower                                                   |
| Geometric mean       | (ref)                                                        | 1.00x slower                                                            |

Benchmark hidden because not significant (4): xml_etree_parse, pickle_pure_python, xml_etree_generate, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.60 ms                                                      | 8.77 ms: 1.02x slower                                                   |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                            |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| django_template | 42.3 ms                                                      | 41.4 ms: 1.02x faster                                                   |
| mako            | 13.2 ms                                                      | 13.3 ms: 1.01x slower                                                   |
| Geometric mean  | (ref)                                                        | 1.00x faster                                                            |

Benchmark hidden because not significant (2): genshi_xml, genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy                   | 448 us                                                       | 337 us: 1.33x faster                                                    |
| deepcopy_memo              | 50.8 us                                                      | 38.2 us: 1.33x faster                                                   |
| go                         | 161 ms                                                       | 138 ms: 1.17x faster                                                    |
| async_tree_none            | 492 ms                                                       | 422 ms: 1.17x faster                                                    |
| async_tree_memoization     | 645 ms                                                       | 559 ms: 1.15x faster                                                    |
| deepcopy_reduce            | 4.04 us                                                      | 3.51 us: 1.15x faster                                                   |
| async_tree_none_tg         | 476 ms                                                       | 416 ms: 1.14x faster                                                    |
| async_tree_memoization_tg  | 604 ms                                                       | 544 ms: 1.11x faster                                                    |
| async_tree_io_tg           | 1.27 sec                                                     | 1.16 sec: 1.09x faster                                                  |
| async_tree_io              | 1.22 sec                                                     | 1.12 sec: 1.09x faster                                                  |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 726 ms: 1.09x faster                                                    |
| pathlib                    | 22.8 ms                                                      | 21.0 ms: 1.08x faster                                                   |
| generators                 | 37.1 ms                                                      | 35.0 ms: 1.06x faster                                                   |
| asyncio_tcp                | 584 ms                                                       | 551 ms: 1.06x faster                                                    |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 722 ms: 1.06x faster                                                    |
| nbody                      | 114 ms                                                       | 109 ms: 1.05x faster                                                    |
| scimark_lu                 | 141 ms                                                       | 135 ms: 1.05x faster                                                    |
| logging_simple             | 7.21 us                                                      | 6.91 us: 1.04x faster                                                   |
| html5lib                   | 66.1 ms                                                      | 63.7 ms: 1.04x faster                                                   |
| gc_traversal               | 5.17 ms                                                      | 4.99 ms: 1.04x faster                                                   |
| 2to3                       | 305 ms                                                       | 294 ms: 1.03x faster                                                    |
| thrift                     | 962 us                                                       | 931 us: 1.03x faster                                                    |
| regex_v8                   | 31.1 ms                                                      | 30.2 ms: 1.03x faster                                                   |
| async_generators           | 488 ms                                                       | 474 ms: 1.03x faster                                                    |
| richards                   | 55.9 ms                                                      | 54.3 ms: 1.03x faster                                                   |
| telco                      | 10.0 ms                                                      | 9.76 ms: 1.03x faster                                                   |
| richards_super             | 62.3 ms                                                      | 60.7 ms: 1.03x faster                                                   |
| coroutines                 | 29.0 ms                                                      | 28.3 ms: 1.02x faster                                                   |
| logging_format             | 7.82 us                                                      | 7.64 us: 1.02x faster                                                   |
| scimark_sparse_mat_mult    | 6.55 ms                                                      | 6.40 ms: 1.02x faster                                                   |
| asyncio_tcp_ssl            | 2.21 sec                                                     | 2.16 sec: 1.02x faster                                                  |
| django_template            | 42.3 ms                                                      | 41.4 ms: 1.02x faster                                                   |
| xml_etree_process          | 80.8 ms                                                      | 79.1 ms: 1.02x faster                                                   |
| sympy_sum                  | 144 ms                                                       | 141 ms: 1.02x faster                                                    |
| pprint_safe_repr           | 933 ms                                                       | 915 ms: 1.02x faster                                                    |
| regex_dna                  | 259 ms                                                       | 254 ms: 1.02x faster                                                    |
| regex_compile              | 128 ms                                                       | 126 ms: 1.02x faster                                                    |
| logging_silent             | 133 ns                                                       | 131 ns: 1.02x faster                                                    |
| docutils                   | 3.10 sec                                                     | 3.04 sec: 1.02x faster                                                  |
| scimark_sor                | 159 ms                                                       | 157 ms: 1.02x faster                                                    |
| regex_effbot               | 4.98 ms                                                      | 4.89 ms: 1.02x faster                                                   |
| meteor_contest             | 113 ms                                                       | 112 ms: 1.02x faster                                                    |
| pprint_pformat             | 1.93 sec                                                     | 1.90 sec: 1.02x faster                                                  |
| bench_thread_pool          | 1.26 ms                                                      | 1.24 ms: 1.02x faster                                                   |
| scimark_fft                | 445 ms                                                       | 439 ms: 1.01x faster                                                    |
| sympy_integrate            | 20.9 ms                                                      | 20.6 ms: 1.01x faster                                                   |
| mdp                        | 3.33 sec                                                     | 3.35 sec: 1.01x slower                                                  |
| bpe_tokeniser              | 5.83 sec                                                     | 5.87 sec: 1.01x slower                                                  |
| mako                       | 13.2 ms                                                      | 13.3 ms: 1.01x slower                                                   |
| unpickle_pure_python       | 251 us                                                       | 254 us: 1.01x slower                                                    |
| json_loads                 | 32.1 us                                                      | 32.5 us: 1.01x slower                                                   |
| sqlglot_transpile          | 1.71 ms                                                      | 1.73 ms: 1.01x slower                                                   |
| float                      | 91.4 ms                                                      | 92.7 ms: 1.01x slower                                                   |
| raytrace                   | 297 ms                                                       | 301 ms: 1.02x slower                                                    |
| crypto_pyaes               | 82.0 ms                                                      | 83.3 ms: 1.02x slower                                                   |
| pyflate                    | 557 ms                                                       | 567 ms: 1.02x slower                                                    |
| tomli_loads                | 2.57 sec                                                     | 2.62 sec: 1.02x slower                                                  |
| python_startup_no_site     | 8.60 ms                                                      | 8.77 ms: 1.02x slower                                                   |
| json_dumps                 | 13.1 ms                                                      | 13.4 ms: 1.02x slower                                                   |
| fannkuch                   | 451 ms                                                       | 465 ms: 1.03x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.03x faster                                                            |

Benchmark hidden because not significant (30): xml_etree_parse, sqlglot_normalize, create_gc_cycles, sqlglot_parse, pickle_pure_python, genshi_xml, bench_mp_pool, sympy_str, pycparser, xml_etree_generate, typing_runtime_protocols, sqlglot_optimize, spectral_norm, genshi_text, pidigits, asyncio_websockets, scimark_monte_carlo, python_startup, dulwich_log, chaos, coverage, hexiom, sympy_expand, nqueens, tornado_http, json, deltablue, comprehensions, xml_etree_iterparse, pylint
Ignored benchmarks (12) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x