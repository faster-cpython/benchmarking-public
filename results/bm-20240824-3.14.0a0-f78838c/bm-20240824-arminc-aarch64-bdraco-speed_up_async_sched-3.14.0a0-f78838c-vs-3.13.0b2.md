# Results vs. 3.13.0b2

- fork: bdraco
- ref: speed_up_async_sched
- machine: linux-aarch64
- commit hash: f78838c
- commit date: 2024-08-24
- overall geometric mean: 1.02x faster
- HPT reliability: 96.01%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240824-arminc-aarch64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 305 ms                                                       | 293 ms: 1.04x faster                                                    |
| html5lib       | 66.1 ms                                                      | 65.0 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                        | 1.02x faster                                                            |

Benchmark hidden because not significant (2): docutils, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240824-arminc-aarch64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 492 ms                                                       | 426 ms: 1.16x faster                                                    |
| async_tree_none_tg         | 476 ms                                                       | 423 ms: 1.12x faster                                                    |
| async_tree_memoization     | 645 ms                                                       | 575 ms: 1.12x faster                                                    |
| async_tree_memoization_tg  | 604 ms                                                       | 541 ms: 1.12x faster                                                    |
| async_tree_io_tg           | 1.27 sec                                                     | 1.14 sec: 1.11x faster                                                  |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 733 ms: 1.08x faster                                                    |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 732 ms: 1.04x faster                                                    |
| Geometric mean             | (ref)                                                        | 1.10x faster                                                            |

Benchmark hidden because not significant (1): async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240824-arminc-aarch64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 114 ms                                                       | 110 ms: 1.04x faster                                                    |
| float          | 91.4 ms                                                      | 91.1 ms: 1.00x faster                                                   |
| Geometric mean | (ref)                                                        | 1.01x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240824-arminc-aarch64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 259 ms                                                       | 247 ms: 1.05x faster                                                    |
| regex_effbot   | 4.98 ms                                                      | 4.85 ms: 1.03x faster                                                   |
| Geometric mean | (ref)                                                        | 1.02x faster                                                            |

Benchmark hidden because not significant (2): regex_compile, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240824-arminc-aarch64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_generate   | 114 ms                                                       | 112 ms: 1.01x faster                                                    |
| unpickle_pure_python | 251 us                                                       | 253 us: 1.01x slower                                                    |
| xml_etree_iterparse  | 147 ms                                                       | 148 ms: 1.01x slower                                                    |
| json_loads           | 32.1 us                                                      | 32.9 us: 1.02x slower                                                   |
| tomli_loads          | 2.57 sec                                                     | 2.64 sec: 1.03x slower                                                  |
| Geometric mean       | (ref)                                                        | 1.00x slower                                                            |

Benchmark hidden because not significant (4): xml_etree_process, pickle_pure_python, xml_etree_parse, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240824-arminc-aarch64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.60 ms                                                      | 8.81 ms: 1.02x slower                                                   |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                            |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240824-arminc-aarch64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text    | 27.4 ms                                                      | 27.8 ms: 1.01x slower                                                   |
| mako           | 13.2 ms                                                      | 13.4 ms: 1.02x slower                                                   |
| Geometric mean | (ref)                                                        | 1.01x slower                                                            |

Benchmark hidden because not significant (2): django_template, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240824-arminc-aarch64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy_memo              | 50.8 us                                                      | 37.9 us: 1.34x faster                                                   |
| deepcopy                   | 448 us                                                       | 338 us: 1.33x faster                                                    |
| async_tree_none            | 492 ms                                                       | 426 ms: 1.16x faster                                                    |
| deepcopy_reduce            | 4.04 us                                                      | 3.53 us: 1.14x faster                                                   |
| async_tree_none_tg         | 476 ms                                                       | 423 ms: 1.12x faster                                                    |
| async_tree_memoization     | 645 ms                                                       | 575 ms: 1.12x faster                                                    |
| async_tree_memoization_tg  | 604 ms                                                       | 541 ms: 1.12x faster                                                    |
| async_tree_io_tg           | 1.27 sec                                                     | 1.14 sec: 1.11x faster                                                  |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 733 ms: 1.08x faster                                                    |
| pathlib                    | 22.8 ms                                                      | 21.2 ms: 1.07x faster                                                   |
| generators                 | 37.1 ms                                                      | 34.8 ms: 1.07x faster                                                   |
| thrift                     | 962 us                                                       | 918 us: 1.05x faster                                                    |
| scimark_lu                 | 141 ms                                                       | 135 ms: 1.05x faster                                                    |
| regex_dna                  | 259 ms                                                       | 247 ms: 1.05x faster                                                    |
| gc_traversal               | 5.17 ms                                                      | 4.96 ms: 1.04x faster                                                   |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 732 ms: 1.04x faster                                                    |
| 2to3                       | 305 ms                                                       | 293 ms: 1.04x faster                                                    |
| nbody                      | 114 ms                                                       | 110 ms: 1.04x faster                                                    |
| richards                   | 55.9 ms                                                      | 53.9 ms: 1.04x faster                                                   |
| richards_super             | 62.3 ms                                                      | 60.2 ms: 1.03x faster                                                   |
| regex_effbot               | 4.98 ms                                                      | 4.85 ms: 1.03x faster                                                   |
| bench_thread_pool          | 1.26 ms                                                      | 1.23 ms: 1.02x faster                                                   |
| scimark_sparse_mat_mult    | 6.55 ms                                                      | 6.44 ms: 1.02x faster                                                   |
| html5lib                   | 66.1 ms                                                      | 65.0 ms: 1.02x faster                                                   |
| scimark_sor                | 159 ms                                                       | 157 ms: 1.02x faster                                                    |
| xml_etree_generate         | 114 ms                                                       | 112 ms: 1.01x faster                                                    |
| pprint_safe_repr           | 933 ms                                                       | 924 ms: 1.01x faster                                                    |
| pprint_pformat             | 1.93 sec                                                     | 1.91 sec: 1.01x faster                                                  |
| float                      | 91.4 ms                                                      | 91.1 ms: 1.00x faster                                                   |
| bpe_tokeniser              | 5.83 sec                                                     | 5.87 sec: 1.01x slower                                                  |
| unpickle_pure_python       | 251 us                                                       | 253 us: 1.01x slower                                                    |
| xml_etree_iterparse        | 147 ms                                                       | 148 ms: 1.01x slower                                                    |
| mdp                        | 3.33 sec                                                     | 3.36 sec: 1.01x slower                                                  |
| sympy_expand               | 457 ms                                                       | 463 ms: 1.01x slower                                                    |
| asyncio_tcp_ssl            | 2.21 sec                                                     | 2.24 sec: 1.01x slower                                                  |
| sqlglot_transpile          | 1.71 ms                                                      | 1.73 ms: 1.01x slower                                                   |
| genshi_text                | 27.4 ms                                                      | 27.8 ms: 1.01x slower                                                   |
| raytrace                   | 297 ms                                                       | 302 ms: 1.02x slower                                                    |
| mako                       | 13.2 ms                                                      | 13.4 ms: 1.02x slower                                                   |
| json_loads                 | 32.1 us                                                      | 32.9 us: 1.02x slower                                                   |
| fannkuch                   | 451 ms                                                       | 462 ms: 1.02x slower                                                    |
| python_startup_no_site     | 8.60 ms                                                      | 8.81 ms: 1.02x slower                                                   |
| json                       | 5.64 ms                                                      | 5.79 ms: 1.03x slower                                                   |
| tomli_loads                | 2.57 sec                                                     | 2.64 sec: 1.03x slower                                                  |
| pyflate                    | 557 ms                                                       | 593 ms: 1.06x slower                                                    |
| go                         | 161 ms                                                       | 191 ms: 1.19x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.02x faster                                                            |

Benchmark hidden because not significant (43): async_tree_io, sqlglot_normalize, create_gc_cycles, tornado_http, xml_etree_process, sympy_sum, meteor_contest, logging_simple, coroutines, regex_compile, pickle_pure_python, scimark_monte_carlo, logging_silent, logging_format, django_template, sympy_integrate, scimark_fft, asyncio_tcp, crypto_pyaes, xml_etree_parse, docutils, nqueens, json_dumps, coverage, spectral_norm, pidigits, telco, deltablue, comprehensions, pycparser, python_startup, genshi_xml, sqlglot_optimize, hexiom, chaos, regex_v8, sympy_str, typing_runtime_protocols, asyncio_websockets, async_generators, bench_mp_pool, sqlglot_parse, pylint
Ignored benchmarks (13) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 96.01% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x