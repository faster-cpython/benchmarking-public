# Results vs. 3.13.0b2

- fork: python
- ref: 401fff7423ca3c8bf1d0
- machine: linux-aarch64
- commit hash: 401fff7
- commit date: 2024-09-14
- overall geometric mean: 1.02x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 305 ms                                                       | 295 ms: 1.03x faster                                                    |
| docutils       | 3.10 sec                                                     | 3.01 sec: 1.03x faster                                                  |
| Geometric mean | (ref)                                                        | 1.02x faster                                                            |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 492 ms                                                       | 424 ms: 1.16x faster                                                    |
| async_tree_memoization     | 645 ms                                                       | 558 ms: 1.16x faster                                                    |
| async_tree_none_tg         | 476 ms                                                       | 422 ms: 1.13x faster                                                    |
| async_tree_memoization_tg  | 604 ms                                                       | 555 ms: 1.09x faster                                                    |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 737 ms: 1.07x faster                                                    |
| async_tree_io              | 1.22 sec                                                     | 1.14 sec: 1.07x faster                                                  |
| async_tree_io_tg           | 1.27 sec                                                     | 1.19 sec: 1.07x faster                                                  |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 728 ms: 1.05x faster                                                    |
| Geometric mean             | (ref)                                                        | 1.10x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 114 ms                                                       | 110 ms: 1.03x faster                                                    |
| float          | 91.4 ms                                                      | 92.7 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                        | 1.01x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 259 ms                                                       | 249 ms: 1.04x faster                                                    |
| regex_v8       | 31.1 ms                                                      | 30.3 ms: 1.03x faster                                                   |
| regex_compile  | 128 ms                                                       | 126 ms: 1.01x faster                                                    |
| regex_effbot   | 4.98 ms                                                      | 4.92 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                        | 1.02x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|---------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle            | 19.8 us                                                      | 19.4 us: 1.02x faster                                                   |
| unpickle_list       | 6.52 us                                                      | 6.41 us: 1.02x faster                                                   |
| xml_etree_process   | 80.8 ms                                                      | 79.5 ms: 1.02x faster                                                   |
| pickle_list         | 5.27 us                                                      | 5.19 us: 1.02x faster                                                   |
| xml_etree_generate  | 114 ms                                                       | 112 ms: 1.02x faster                                                    |
| json_loads          | 32.1 us                                                      | 31.8 us: 1.01x faster                                                   |
| json_dumps          | 13.1 ms                                                      | 13.2 ms: 1.01x slower                                                   |
| xml_etree_iterparse | 147 ms                                                       | 149 ms: 1.01x slower                                                    |
| tomli_loads         | 2.57 sec                                                     | 2.64 sec: 1.03x slower                                                  |
| Geometric mean      | (ref)                                                        | 1.00x faster                                                            |

Benchmark hidden because not significant (5): xml_etree_parse, pickle_dict, unpickle_pure_python, pickle_pure_python, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup | 13.0 ms                                                      | 12.9 ms: 1.00x faster                                                   |
| Geometric mean | (ref)                                                        | 1.00x faster                                                            |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| django_template | 42.3 ms                                                      | 41.7 ms: 1.01x faster                                                   |
| mako            | 13.2 ms                                                      | 13.5 ms: 1.03x slower                                                   |
| Geometric mean  | (ref)                                                        | 1.01x slower                                                            |

Benchmark hidden because not significant (2): genshi_xml, genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy_memo              | 50.8 us                                                      | 37.7 us: 1.35x faster                                                   |
| deepcopy                   | 448 us                                                       | 334 us: 1.34x faster                                                    |
| async_tree_none            | 492 ms                                                       | 424 ms: 1.16x faster                                                    |
| go                         | 161 ms                                                       | 139 ms: 1.16x faster                                                    |
| async_tree_memoization     | 645 ms                                                       | 558 ms: 1.16x faster                                                    |
| deepcopy_reduce            | 4.04 us                                                      | 3.52 us: 1.15x faster                                                   |
| async_tree_none_tg         | 476 ms                                                       | 422 ms: 1.13x faster                                                    |
| pathlib                    | 22.8 ms                                                      | 20.7 ms: 1.10x faster                                                   |
| async_tree_memoization_tg  | 604 ms                                                       | 555 ms: 1.09x faster                                                    |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 737 ms: 1.07x faster                                                    |
| async_tree_io              | 1.22 sec                                                     | 1.14 sec: 1.07x faster                                                  |
| generators                 | 37.1 ms                                                      | 34.7 ms: 1.07x faster                                                   |
| async_tree_io_tg           | 1.27 sec                                                     | 1.19 sec: 1.07x faster                                                  |
| richards                   | 55.9 ms                                                      | 52.7 ms: 1.06x faster                                                   |
| richards_super             | 62.3 ms                                                      | 59.4 ms: 1.05x faster                                                   |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 728 ms: 1.05x faster                                                    |
| scimark_lu                 | 141 ms                                                       | 135 ms: 1.05x faster                                                    |
| regex_dna                  | 259 ms                                                       | 249 ms: 1.04x faster                                                    |
| nbody                      | 114 ms                                                       | 110 ms: 1.03x faster                                                    |
| thrift                     | 962 us                                                       | 931 us: 1.03x faster                                                    |
| 2to3                       | 305 ms                                                       | 295 ms: 1.03x faster                                                    |
| docutils                   | 3.10 sec                                                     | 3.01 sec: 1.03x faster                                                  |
| logging_simple             | 7.21 us                                                      | 7.01 us: 1.03x faster                                                   |
| regex_v8                   | 31.1 ms                                                      | 30.3 ms: 1.03x faster                                                   |
| logging_format             | 7.82 us                                                      | 7.63 us: 1.03x faster                                                   |
| sqlite_synth               | 3.90 us                                                      | 3.81 us: 1.03x faster                                                   |
| scimark_sparse_mat_mult    | 6.55 ms                                                      | 6.42 ms: 1.02x faster                                                   |
| unpickle                   | 19.8 us                                                      | 19.4 us: 1.02x faster                                                   |
| bench_thread_pool          | 1.26 ms                                                      | 1.23 ms: 1.02x faster                                                   |
| meteor_contest             | 113 ms                                                       | 111 ms: 1.02x faster                                                    |
| unpickle_list              | 6.52 us                                                      | 6.41 us: 1.02x faster                                                   |
| xml_etree_process          | 80.8 ms                                                      | 79.5 ms: 1.02x faster                                                   |
| telco                      | 10.0 ms                                                      | 9.86 ms: 1.02x faster                                                   |
| pickle_list                | 5.27 us                                                      | 5.19 us: 1.02x faster                                                   |
| xml_etree_generate         | 114 ms                                                       | 112 ms: 1.02x faster                                                    |
| django_template            | 42.3 ms                                                      | 41.7 ms: 1.01x faster                                                   |
| scimark_sor                | 159 ms                                                       | 157 ms: 1.01x faster                                                    |
| regex_compile              | 128 ms                                                       | 126 ms: 1.01x faster                                                    |
| pprint_pformat             | 1.93 sec                                                     | 1.91 sec: 1.01x faster                                                  |
| regex_effbot               | 4.98 ms                                                      | 4.92 ms: 1.01x faster                                                   |
| json_loads                 | 32.1 us                                                      | 31.8 us: 1.01x faster                                                   |
| pprint_safe_repr           | 933 ms                                                       | 926 ms: 1.01x faster                                                    |
| crypto_pyaes               | 82.0 ms                                                      | 81.3 ms: 1.01x faster                                                   |
| python_startup             | 13.0 ms                                                      | 12.9 ms: 1.00x faster                                                   |
| bpe_tokeniser              | 5.83 sec                                                     | 5.86 sec: 1.01x slower                                                  |
| pyflate                    | 557 ms                                                       | 562 ms: 1.01x slower                                                    |
| chaos                      | 68.3 ms                                                      | 69.0 ms: 1.01x slower                                                   |
| json_dumps                 | 13.1 ms                                                      | 13.2 ms: 1.01x slower                                                   |
| xml_etree_iterparse        | 147 ms                                                       | 149 ms: 1.01x slower                                                    |
| float                      | 91.4 ms                                                      | 92.7 ms: 1.01x slower                                                   |
| nqueens                    | 98.9 ms                                                      | 101 ms: 1.02x slower                                                    |
| sqlglot_transpile          | 1.71 ms                                                      | 1.74 ms: 1.02x slower                                                   |
| fannkuch                   | 451 ms                                                       | 460 ms: 1.02x slower                                                    |
| raytrace                   | 297 ms                                                       | 303 ms: 1.02x slower                                                    |
| tomli_loads                | 2.57 sec                                                     | 2.64 sec: 1.03x slower                                                  |
| mako                       | 13.2 ms                                                      | 13.5 ms: 1.03x slower                                                   |
| Geometric mean             | (ref)                                                        | 1.02x faster                                                            |

Benchmark hidden because not significant (40): sqlglot_parse, sqlglot_normalize, sympy_sum, json, asyncio_tcp, xml_etree_parse, async_generators, coroutines, html5lib, spectral_norm, coverage, scimark_fft, logging_silent, sqlglot_optimize, typing_runtime_protocols, dulwich_log, sympy_str, pycparser, bench_mp_pool, tornado_http, sympy_integrate, pickle_dict, create_gc_cycles, gc_traversal, genshi_xml, mdp, pidigits, comprehensions, scimark_monte_carlo, python_startup_no_site, asyncio_tcp_ssl, hexiom, unpickle_pure_python, genshi_text, asyncio_websockets, sympy_expand, pickle_pure_python, deltablue, pickle, pylint
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240914-3.14.0a0-401fff7/bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json: unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x