# Results vs. 3.13.0b2

- fork: python
- ref: 04eb5c8db1e24cabd0cb
- machine: linux-aarch64
- commit hash: 04eb5c8
- commit date: 2024-07-27
- overall geometric mean: 1.02x faster
- HPT reliability: 97.88%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (4): 2to3, docutils, html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none_tg         | 476 ms                                                       | 413 ms: 1.15x faster                                                    |
| async_tree_memoization     | 645 ms                                                       | 563 ms: 1.15x faster                                                    |
| async_tree_io_tg           | 1.27 sec                                                     | 1.13 sec: 1.12x faster                                                  |
| async_tree_memoization_tg  | 604 ms                                                       | 543 ms: 1.11x faster                                                    |
| async_tree_none            | 492 ms                                                       | 444 ms: 1.11x faster                                                    |
| async_tree_io              | 1.22 sec                                                     | 1.13 sec: 1.09x faster                                                  |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 730 ms: 1.08x faster                                                    |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 712 ms: 1.07x faster                                                    |
| Geometric mean             | (ref)                                                        | 1.11x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 114 ms                                                       | 109 ms: 1.05x faster                                                    |
| float          | 91.4 ms                                                      | 92.0 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                        | 1.01x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 31.1 ms                                                      | 30.4 ms: 1.02x faster                                                   |
| regex_dna      | 259 ms                                                       | 255 ms: 1.01x faster                                                    |
| regex_effbot   | 4.98 ms                                                      | 4.92 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                        | 1.01x faster                                                            |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|---------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_generate  | 114 ms                                                       | 112 ms: 1.01x faster                                                    |
| xml_etree_iterparse | 147 ms                                                       | 145 ms: 1.01x faster                                                    |
| tomli_loads         | 2.57 sec                                                     | 2.55 sec: 1.01x faster                                                  |
| json_loads          | 32.1 us                                                      | 32.8 us: 1.02x slower                                                   |
| json_dumps          | 13.1 ms                                                      | 13.4 ms: 1.02x slower                                                   |
| Geometric mean      | (ref)                                                        | 1.00x faster                                                            |

Benchmark hidden because not significant (4): xml_etree_parse, xml_etree_process, unpickle_pure_python, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 13.0 ms                                                      | 13.2 ms: 1.02x slower                                                   |
| python_startup_no_site | 8.60 ms                                                      | 8.89 ms: 1.03x slower                                                   |
| Geometric mean         | (ref)                                                        | 1.03x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| django_template | 42.3 ms                                                      | 41.6 ms: 1.02x faster                                                   |
| genshi_xml      | 60.4 ms                                                      | 61.2 ms: 1.01x slower                                                   |
| mako            | 13.2 ms                                                      | 13.3 ms: 1.01x slower                                                   |
| genshi_text     | 27.4 ms                                                      | 28.0 ms: 1.02x slower                                                   |
| Geometric mean  | (ref)                                                        | 1.01x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy                   | 448 us                                                       | 335 us: 1.34x faster                                                    |
| deepcopy_memo              | 50.8 us                                                      | 38.2 us: 1.33x faster                                                   |
| deepcopy_reduce            | 4.04 us                                                      | 3.43 us: 1.18x faster                                                   |
| async_tree_none_tg         | 476 ms                                                       | 413 ms: 1.15x faster                                                    |
| async_tree_memoization     | 645 ms                                                       | 563 ms: 1.15x faster                                                    |
| async_tree_io_tg           | 1.27 sec                                                     | 1.13 sec: 1.12x faster                                                  |
| async_tree_memoization_tg  | 604 ms                                                       | 543 ms: 1.11x faster                                                    |
| async_tree_none            | 492 ms                                                       | 444 ms: 1.11x faster                                                    |
| async_tree_io              | 1.22 sec                                                     | 1.13 sec: 1.09x faster                                                  |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 730 ms: 1.08x faster                                                    |
| gc_traversal               | 5.17 ms                                                      | 4.82 ms: 1.07x faster                                                   |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 712 ms: 1.07x faster                                                    |
| pathlib                    | 22.8 ms                                                      | 21.3 ms: 1.07x faster                                                   |
| richards                   | 55.9 ms                                                      | 52.3 ms: 1.07x faster                                                   |
| richards_super             | 62.3 ms                                                      | 58.7 ms: 1.06x faster                                                   |
| generators                 | 37.1 ms                                                      | 35.3 ms: 1.05x faster                                                   |
| nbody                      | 114 ms                                                       | 109 ms: 1.05x faster                                                    |
| scimark_lu                 | 141 ms                                                       | 136 ms: 1.04x faster                                                    |
| logging_simple             | 7.21 us                                                      | 6.97 us: 1.03x faster                                                   |
| logging_silent             | 133 ns                                                       | 129 ns: 1.03x faster                                                    |
| scimark_sparse_mat_mult    | 6.55 ms                                                      | 6.37 ms: 1.03x faster                                                   |
| bench_thread_pool          | 1.26 ms                                                      | 1.23 ms: 1.03x faster                                                   |
| regex_v8                   | 31.1 ms                                                      | 30.4 ms: 1.02x faster                                                   |
| logging_format             | 7.82 us                                                      | 7.67 us: 1.02x faster                                                   |
| scimark_fft                | 445 ms                                                       | 438 ms: 1.02x faster                                                    |
| django_template            | 42.3 ms                                                      | 41.6 ms: 1.02x faster                                                   |
| xml_etree_generate         | 114 ms                                                       | 112 ms: 1.01x faster                                                    |
| xml_etree_iterparse        | 147 ms                                                       | 145 ms: 1.01x faster                                                    |
| regex_dna                  | 259 ms                                                       | 255 ms: 1.01x faster                                                    |
| regex_effbot               | 4.98 ms                                                      | 4.92 ms: 1.01x faster                                                   |
| coverage                   | 98.4 ms                                                      | 97.4 ms: 1.01x faster                                                   |
| tomli_loads                | 2.57 sec                                                     | 2.55 sec: 1.01x faster                                                  |
| float                      | 91.4 ms                                                      | 92.0 ms: 1.01x slower                                                   |
| pprint_pformat             | 1.93 sec                                                     | 1.95 sec: 1.01x slower                                                  |
| sympy_expand               | 457 ms                                                       | 463 ms: 1.01x slower                                                    |
| sympy_str                  | 265 ms                                                       | 268 ms: 1.01x slower                                                    |
| sympy_integrate            | 20.9 ms                                                      | 21.1 ms: 1.01x slower                                                   |
| genshi_xml                 | 60.4 ms                                                      | 61.2 ms: 1.01x slower                                                   |
| mako                       | 13.2 ms                                                      | 13.3 ms: 1.01x slower                                                   |
| asyncio_tcp_ssl            | 2.21 sec                                                     | 2.24 sec: 1.01x slower                                                  |
| thrift                     | 962 us                                                       | 977 us: 1.02x slower                                                    |
| typing_runtime_protocols   | 193 us                                                       | 197 us: 1.02x slower                                                    |
| bench_mp_pool              | 7.03 ms                                                      | 7.15 ms: 1.02x slower                                                   |
| python_startup             | 13.0 ms                                                      | 13.2 ms: 1.02x slower                                                   |
| genshi_text                | 27.4 ms                                                      | 28.0 ms: 1.02x slower                                                   |
| json_loads                 | 32.1 us                                                      | 32.8 us: 1.02x slower                                                   |
| pprint_safe_repr           | 933 ms                                                       | 952 ms: 1.02x slower                                                    |
| json_dumps                 | 13.1 ms                                                      | 13.4 ms: 1.02x slower                                                   |
| sympy_sum                  | 144 ms                                                       | 147 ms: 1.03x slower                                                    |
| python_startup_no_site     | 8.60 ms                                                      | 8.89 ms: 1.03x slower                                                   |
| pyflate                    | 557 ms                                                       | 580 ms: 1.04x slower                                                    |
| fannkuch                   | 451 ms                                                       | 476 ms: 1.06x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.02x faster                                                            |

Benchmark hidden because not significant (38): dask, xml_etree_parse, sqlglot_normalize, scimark_sor, chaos, sqlglot_parse, coroutines, deltablue, spectral_norm, xml_etree_process, telco, asyncio_tcp, sqlglot_optimize, 2to3, scimark_monte_carlo, crypto_pyaes, raytrace, unpickle_pure_python, create_gc_cycles, pidigits, meteor_contest, comprehensions, mdp, bpe_tokeniser, pickle_pure_python, asyncio_websockets, docutils, regex_compile, html5lib, pycparser, go, nqueens, tornado_http, async_generators, hexiom, json, sqlglot_transpile, pylint
Ignored benchmarks (12) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 97.88% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x