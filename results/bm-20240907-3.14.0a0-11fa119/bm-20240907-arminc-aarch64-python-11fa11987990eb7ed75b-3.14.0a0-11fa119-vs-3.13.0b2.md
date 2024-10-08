# Results vs. 3.13.0b2

- fork: python
- ref: 11fa11987990eb7ed75b
- machine: linux-aarch64
- commit hash: 11fa119
- commit date: 2024-09-07
- overall geometric mean: 1.03x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 305 ms                                                       | 293 ms: 1.04x faster                                                    |
| docutils       | 3.10 sec                                                     | 3.05 sec: 1.02x faster                                                  |
| html5lib       | 66.1 ms                                                      | 63.1 ms: 1.05x faster                                                   |
| Geometric mean | (ref)                                                        | 1.03x faster                                                            |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 492 ms                                                       | 423 ms: 1.16x faster                                                    |
| async_tree_memoization     | 645 ms                                                       | 556 ms: 1.16x faster                                                    |
| async_tree_none_tg         | 476 ms                                                       | 416 ms: 1.14x faster                                                    |
| async_tree_memoization_tg  | 604 ms                                                       | 549 ms: 1.10x faster                                                    |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 733 ms: 1.08x faster                                                    |
| async_tree_io              | 1.22 sec                                                     | 1.13 sec: 1.08x faster                                                  |
| async_tree_io_tg           | 1.27 sec                                                     | 1.18 sec: 1.08x faster                                                  |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 725 ms: 1.05x faster                                                    |
| Geometric mean             | (ref)                                                        | 1.11x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 114 ms                                                       | 109 ms: 1.04x faster                                                    |
| float          | 91.4 ms                                                      | 92.7 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                        | 1.01x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 259 ms                                                       | 252 ms: 1.03x faster                                                    |
| regex_v8       | 31.1 ms                                                      | 30.3 ms: 1.03x faster                                                   |
| regex_compile  | 128 ms                                                       | 125 ms: 1.02x faster                                                    |
| regex_effbot   | 4.98 ms                                                      | 4.89 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                        | 1.02x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle_list        | 6.52 us                                                      | 6.28 us: 1.04x faster                                                   |
| xml_etree_parse      | 191 ms                                                       | 186 ms: 1.03x faster                                                    |
| xml_etree_process    | 80.8 ms                                                      | 78.5 ms: 1.03x faster                                                   |
| xml_etree_generate   | 114 ms                                                       | 111 ms: 1.02x faster                                                    |
| xml_etree_iterparse  | 147 ms                                                       | 148 ms: 1.01x slower                                                    |
| json_loads           | 32.1 us                                                      | 32.5 us: 1.01x slower                                                   |
| unpickle_pure_python | 251 us                                                       | 255 us: 1.01x slower                                                    |
| json_dumps           | 13.1 ms                                                      | 13.3 ms: 1.02x slower                                                   |
| tomli_loads          | 2.57 sec                                                     | 2.65 sec: 1.03x slower                                                  |
| Geometric mean       | (ref)                                                        | 1.00x faster                                                            |

Benchmark hidden because not significant (5): unpickle, pickle_dict, pickle_list, pickle_pure_python, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 13.0 ms                                                      | 13.2 ms: 1.02x slower                                                   |
| python_startup_no_site | 8.60 ms                                                      | 8.83 ms: 1.03x slower                                                   |
| Geometric mean         | (ref)                                                        | 1.02x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| django_template | 42.3 ms                                                      | 41.7 ms: 1.01x faster                                                   |
| mako            | 13.2 ms                                                      | 13.4 ms: 1.02x slower                                                   |
| Geometric mean  | (ref)                                                        | 1.00x slower                                                            |

Benchmark hidden because not significant (2): genshi_xml, genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy                   | 448 us                                                       | 332 us: 1.35x faster                                                    |
| deepcopy_memo              | 50.8 us                                                      | 38.0 us: 1.34x faster                                                   |
| deepcopy_reduce            | 4.04 us                                                      | 3.45 us: 1.17x faster                                                   |
| go                         | 161 ms                                                       | 138 ms: 1.17x faster                                                    |
| async_tree_none            | 492 ms                                                       | 423 ms: 1.16x faster                                                    |
| async_tree_memoization     | 645 ms                                                       | 556 ms: 1.16x faster                                                    |
| async_tree_none_tg         | 476 ms                                                       | 416 ms: 1.14x faster                                                    |
| async_tree_memoization_tg  | 604 ms                                                       | 549 ms: 1.10x faster                                                    |
| pathlib                    | 22.8 ms                                                      | 21.0 ms: 1.08x faster                                                   |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 733 ms: 1.08x faster                                                    |
| async_tree_io              | 1.22 sec                                                     | 1.13 sec: 1.08x faster                                                  |
| async_tree_io_tg           | 1.27 sec                                                     | 1.18 sec: 1.08x faster                                                  |
| generators                 | 37.1 ms                                                      | 35.1 ms: 1.06x faster                                                   |
| richards                   | 55.9 ms                                                      | 52.8 ms: 1.06x faster                                                   |
| gc_traversal               | 5.17 ms                                                      | 4.91 ms: 1.05x faster                                                   |
| scimark_lu                 | 141 ms                                                       | 134 ms: 1.05x faster                                                    |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 725 ms: 1.05x faster                                                    |
| html5lib                   | 66.1 ms                                                      | 63.1 ms: 1.05x faster                                                   |
| richards_super             | 62.3 ms                                                      | 59.5 ms: 1.05x faster                                                   |
| nbody                      | 114 ms                                                       | 109 ms: 1.04x faster                                                    |
| 2to3                       | 305 ms                                                       | 293 ms: 1.04x faster                                                    |
| unpickle_list              | 6.52 us                                                      | 6.28 us: 1.04x faster                                                   |
| logging_simple             | 7.21 us                                                      | 6.95 us: 1.04x faster                                                   |
| thrift                     | 962 us                                                       | 931 us: 1.03x faster                                                    |
| xml_etree_parse            | 191 ms                                                       | 186 ms: 1.03x faster                                                    |
| xml_etree_process          | 80.8 ms                                                      | 78.5 ms: 1.03x faster                                                   |
| logging_format             | 7.82 us                                                      | 7.62 us: 1.03x faster                                                   |
| regex_dna                  | 259 ms                                                       | 252 ms: 1.03x faster                                                    |
| scimark_sparse_mat_mult    | 6.55 ms                                                      | 6.38 ms: 1.03x faster                                                   |
| regex_v8                   | 31.1 ms                                                      | 30.3 ms: 1.03x faster                                                   |
| xml_etree_generate         | 114 ms                                                       | 111 ms: 1.02x faster                                                    |
| regex_compile              | 128 ms                                                       | 125 ms: 1.02x faster                                                    |
| pprint_safe_repr           | 933 ms                                                       | 914 ms: 1.02x faster                                                    |
| pprint_pformat             | 1.93 sec                                                     | 1.89 sec: 1.02x faster                                                  |
| regex_effbot               | 4.98 ms                                                      | 4.89 ms: 1.02x faster                                                   |
| docutils                   | 3.10 sec                                                     | 3.05 sec: 1.02x faster                                                  |
| coroutines                 | 29.0 ms                                                      | 28.6 ms: 1.02x faster                                                   |
| meteor_contest             | 113 ms                                                       | 112 ms: 1.01x faster                                                    |
| django_template            | 42.3 ms                                                      | 41.7 ms: 1.01x faster                                                   |
| bench_thread_pool          | 1.26 ms                                                      | 1.24 ms: 1.01x faster                                                   |
| xml_etree_iterparse        | 147 ms                                                       | 148 ms: 1.01x slower                                                    |
| sqlglot_transpile          | 1.71 ms                                                      | 1.73 ms: 1.01x slower                                                   |
| json_loads                 | 32.1 us                                                      | 32.5 us: 1.01x slower                                                   |
| fannkuch                   | 451 ms                                                       | 456 ms: 1.01x slower                                                    |
| float                      | 91.4 ms                                                      | 92.7 ms: 1.01x slower                                                   |
| sympy_expand               | 457 ms                                                       | 464 ms: 1.01x slower                                                    |
| unpickle_pure_python       | 251 us                                                       | 255 us: 1.01x slower                                                    |
| raytrace                   | 297 ms                                                       | 301 ms: 1.02x slower                                                    |
| python_startup             | 13.0 ms                                                      | 13.2 ms: 1.02x slower                                                   |
| crypto_pyaes               | 82.0 ms                                                      | 83.4 ms: 1.02x slower                                                   |
| pyflate                    | 557 ms                                                       | 566 ms: 1.02x slower                                                    |
| json_dumps                 | 13.1 ms                                                      | 13.3 ms: 1.02x slower                                                   |
| mako                       | 13.2 ms                                                      | 13.4 ms: 1.02x slower                                                   |
| python_startup_no_site     | 8.60 ms                                                      | 8.83 ms: 1.03x slower                                                   |
| tomli_loads                | 2.57 sec                                                     | 2.65 sec: 1.03x slower                                                  |
| Geometric mean             | (ref)                                                        | 1.03x faster                                                            |

Benchmark hidden because not significant (41): tornado_http, asyncio_tcp, create_gc_cycles, sqlglot_normalize, scimark_sor, unpickle, logging_silent, typing_runtime_protocols, scimark_fft, sympy_sum, sympy_integrate, asyncio_tcp_ssl, comprehensions, spectral_norm, scimark_monte_carlo, nqueens, telco, pickle_dict, sqlglot_parse, sqlglot_optimize, sqlite_synth, sympy_str, bench_mp_pool, pickle_list, async_generators, bpe_tokeniser, pidigits, mdp, genshi_xml, genshi_text, asyncio_websockets, chaos, dulwich_log, deltablue, pycparser, pickle_pure_python, pickle, json, coverage, hexiom, pylint
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240907-3.14.0a0-11fa119/bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119.json: unpack_sequence

# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x