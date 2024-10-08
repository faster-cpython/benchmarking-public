# Results vs. 3.13.0b2

- fork: mdboom
- ref: simplify_richcompare
- machine: linux-aarch64
- commit hash: 2fa7b0e
- commit date: 2024-09-04
- overall geometric mean: 1.02x faster
- HPT reliability: 99.74%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240904-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 305 ms                                                       | 294 ms: 1.04x faster                                                    |
| docutils       | 3.10 sec                                                     | 3.01 sec: 1.03x faster                                                  |
| html5lib       | 66.1 ms                                                      | 63.7 ms: 1.04x faster                                                   |
| Geometric mean | (ref)                                                        | 1.03x faster                                                            |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240904-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none_tg         | 476 ms                                                       | 419 ms: 1.14x faster                                                    |
| async_tree_memoization     | 645 ms                                                       | 568 ms: 1.14x faster                                                    |
| async_tree_none            | 492 ms                                                       | 437 ms: 1.13x faster                                                    |
| async_tree_memoization_tg  | 604 ms                                                       | 553 ms: 1.09x faster                                                    |
| async_tree_io_tg           | 1.27 sec                                                     | 1.17 sec: 1.08x faster                                                  |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 739 ms: 1.07x faster                                                    |
| async_tree_io              | 1.22 sec                                                     | 1.15 sec: 1.07x faster                                                  |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 732 ms: 1.04x faster                                                    |
| Geometric mean             | (ref)                                                        | 1.09x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240904-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 114 ms                                                       | 109 ms: 1.04x faster                                                    |
| float          | 91.4 ms                                                      | 92.6 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                        | 1.01x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240904-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 31.1 ms                                                      | 30.5 ms: 1.02x faster                                                   |
| regex_dna      | 259 ms                                                       | 254 ms: 1.02x faster                                                    |
| Geometric mean | (ref)                                                        | 1.01x faster                                                            |

Benchmark hidden because not significant (2): regex_compile, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240904-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|---------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_generate  | 114 ms                                                       | 111 ms: 1.02x faster                                                    |
| xml_etree_iterparse | 147 ms                                                       | 146 ms: 1.01x faster                                                    |
| json_loads          | 32.1 us                                                      | 32.7 us: 1.02x slower                                                   |
| tomli_loads         | 2.57 sec                                                     | 2.63 sec: 1.02x slower                                                  |
| json_dumps          | 13.1 ms                                                      | 13.5 ms: 1.03x slower                                                   |
| Geometric mean      | (ref)                                                        | 1.00x slower                                                            |

Benchmark hidden because not significant (4): xml_etree_parse, xml_etree_process, pickle_pure_python, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240904-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 13.0 ms                                                      | 13.1 ms: 1.01x slower                                                   |
| python_startup_no_site | 8.60 ms                                                      | 8.80 ms: 1.02x slower                                                   |
| Geometric mean         | (ref)                                                        | 1.02x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240904-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 60.4 ms                                                      | 59.5 ms: 1.01x faster                                                   |
| django_template | 42.3 ms                                                      | 41.7 ms: 1.01x faster                                                   |
| mako            | 13.2 ms                                                      | 13.5 ms: 1.02x slower                                                   |
| Geometric mean  | (ref)                                                        | 1.00x faster                                                            |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240904-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy                   | 448 us                                                       | 329 us: 1.36x faster                                                    |
| deepcopy_memo              | 50.8 us                                                      | 38.4 us: 1.32x faster                                                   |
| go                         | 161 ms                                                       | 136 ms: 1.18x faster                                                    |
| deepcopy_reduce            | 4.04 us                                                      | 3.48 us: 1.16x faster                                                   |
| async_tree_none_tg         | 476 ms                                                       | 419 ms: 1.14x faster                                                    |
| async_tree_memoization     | 645 ms                                                       | 568 ms: 1.14x faster                                                    |
| async_tree_none            | 492 ms                                                       | 437 ms: 1.13x faster                                                    |
| async_tree_memoization_tg  | 604 ms                                                       | 553 ms: 1.09x faster                                                    |
| pathlib                    | 22.8 ms                                                      | 20.9 ms: 1.09x faster                                                   |
| async_tree_io_tg           | 1.27 sec                                                     | 1.17 sec: 1.08x faster                                                  |
| generators                 | 37.1 ms                                                      | 34.6 ms: 1.07x faster                                                   |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 739 ms: 1.07x faster                                                    |
| async_tree_io              | 1.22 sec                                                     | 1.15 sec: 1.07x faster                                                  |
| richards_super             | 62.3 ms                                                      | 59.2 ms: 1.05x faster                                                   |
| richards                   | 55.9 ms                                                      | 53.2 ms: 1.05x faster                                                   |
| scimark_lu                 | 141 ms                                                       | 135 ms: 1.05x faster                                                    |
| nbody                      | 114 ms                                                       | 109 ms: 1.04x faster                                                    |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 732 ms: 1.04x faster                                                    |
| gc_traversal               | 5.17 ms                                                      | 4.99 ms: 1.04x faster                                                   |
| html5lib                   | 66.1 ms                                                      | 63.7 ms: 1.04x faster                                                   |
| 2to3                       | 305 ms                                                       | 294 ms: 1.04x faster                                                    |
| pprint_pformat             | 1.93 sec                                                     | 1.87 sec: 1.03x faster                                                  |
| pprint_safe_repr           | 933 ms                                                       | 905 ms: 1.03x faster                                                    |
| docutils                   | 3.10 sec                                                     | 3.01 sec: 1.03x faster                                                  |
| logging_simple             | 7.21 us                                                      | 7.00 us: 1.03x faster                                                   |
| bench_thread_pool          | 1.26 ms                                                      | 1.23 ms: 1.03x faster                                                   |
| scimark_sparse_mat_mult    | 6.55 ms                                                      | 6.39 ms: 1.02x faster                                                   |
| thrift                     | 962 us                                                       | 939 us: 1.02x faster                                                    |
| coroutines                 | 29.0 ms                                                      | 28.3 ms: 1.02x faster                                                   |
| xml_etree_generate         | 114 ms                                                       | 111 ms: 1.02x faster                                                    |
| async_generators           | 488 ms                                                       | 479 ms: 1.02x faster                                                    |
| regex_v8                   | 31.1 ms                                                      | 30.5 ms: 1.02x faster                                                   |
| logging_format             | 7.82 us                                                      | 7.69 us: 1.02x faster                                                   |
| regex_dna                  | 259 ms                                                       | 254 ms: 1.02x faster                                                    |
| genshi_xml                 | 60.4 ms                                                      | 59.5 ms: 1.01x faster                                                   |
| django_template            | 42.3 ms                                                      | 41.7 ms: 1.01x faster                                                   |
| scimark_fft                | 445 ms                                                       | 440 ms: 1.01x faster                                                    |
| logging_silent             | 133 ns                                                       | 132 ns: 1.01x faster                                                    |
| scimark_sor                | 159 ms                                                       | 157 ms: 1.01x faster                                                    |
| xml_etree_iterparse        | 147 ms                                                       | 146 ms: 1.01x faster                                                    |
| mdp                        | 3.33 sec                                                     | 3.35 sec: 1.01x slower                                                  |
| sqlglot_transpile          | 1.71 ms                                                      | 1.73 ms: 1.01x slower                                                   |
| coverage                   | 98.4 ms                                                      | 99.4 ms: 1.01x slower                                                   |
| python_startup             | 13.0 ms                                                      | 13.1 ms: 1.01x slower                                                   |
| float                      | 91.4 ms                                                      | 92.6 ms: 1.01x slower                                                   |
| meteor_contest             | 113 ms                                                       | 115 ms: 1.01x slower                                                    |
| typing_runtime_protocols   | 193 us                                                       | 197 us: 1.02x slower                                                    |
| json_loads                 | 32.1 us                                                      | 32.7 us: 1.02x slower                                                   |
| bpe_tokeniser              | 5.83 sec                                                     | 5.94 sec: 1.02x slower                                                  |
| raytrace                   | 297 ms                                                       | 303 ms: 1.02x slower                                                    |
| tomli_loads                | 2.57 sec                                                     | 2.63 sec: 1.02x slower                                                  |
| python_startup_no_site     | 8.60 ms                                                      | 8.80 ms: 1.02x slower                                                   |
| mako                       | 13.2 ms                                                      | 13.5 ms: 1.02x slower                                                   |
| json_dumps                 | 13.1 ms                                                      | 13.5 ms: 1.03x slower                                                   |
| fannkuch                   | 451 ms                                                       | 465 ms: 1.03x slower                                                    |
| pyflate                    | 557 ms                                                       | 582 ms: 1.05x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.02x faster                                                            |

Benchmark hidden because not significant (33): sqlglot_normalize, asyncio_tcp, create_gc_cycles, tornado_http, genshi_text, sqlglot_parse, xml_etree_parse, regex_compile, regex_effbot, sqlglot_optimize, sympy_sum, asyncio_tcp_ssl, sympy_integrate, sympy_str, scimark_monte_carlo, nqueens, xml_etree_process, pickle_pure_python, pidigits, deltablue, telco, chaos, comprehensions, spectral_norm, unpickle_pure_python, asyncio_websockets, bench_mp_pool, sympy_expand, pycparser, crypto_pyaes, json, hexiom, pylint
Ignored benchmarks (13) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.74% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x