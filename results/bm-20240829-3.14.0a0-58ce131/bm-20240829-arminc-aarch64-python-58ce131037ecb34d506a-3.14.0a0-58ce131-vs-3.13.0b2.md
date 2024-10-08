# Results vs. 3.13.0b2

- fork: python
- ref: 58ce131037ecb34d506a
- machine: linux-aarch64
- commit hash: 58ce131
- commit date: 2024-08-29
- overall geometric mean: 1.02x faster
- HPT reliability: 99.95%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-arminc-aarch64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 305 ms                                                       | 293 ms: 1.04x faster                                                    |
| docutils       | 3.10 sec                                                     | 3.00 sec: 1.03x faster                                                  |
| html5lib       | 66.1 ms                                                      | 63.3 ms: 1.04x faster                                                   |
| Geometric mean | (ref)                                                        | 1.03x faster                                                            |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-arminc-aarch64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 492 ms                                                       | 423 ms: 1.16x faster                                                    |
| async_tree_memoization     | 645 ms                                                       | 556 ms: 1.16x faster                                                    |
| async_tree_none_tg         | 476 ms                                                       | 414 ms: 1.15x faster                                                    |
| async_tree_memoization_tg  | 604 ms                                                       | 548 ms: 1.10x faster                                                    |
| async_tree_io_tg           | 1.27 sec                                                     | 1.17 sec: 1.09x faster                                                  |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 731 ms: 1.08x faster                                                    |
| async_tree_io              | 1.22 sec                                                     | 1.15 sec: 1.06x faster                                                  |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 720 ms: 1.06x faster                                                    |
| Geometric mean             | (ref)                                                        | 1.11x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-arminc-aarch64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 114 ms                                                       | 110 ms: 1.04x faster                                                    |
| float          | 91.4 ms                                                      | 92.4 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                        | 1.01x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-arminc-aarch64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 259 ms                                                       | 249 ms: 1.04x faster                                                    |
| regex_effbot   | 4.98 ms                                                      | 4.80 ms: 1.04x faster                                                   |
| regex_v8       | 31.1 ms                                                      | 30.2 ms: 1.03x faster                                                   |
| Geometric mean | (ref)                                                        | 1.03x faster                                                            |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-arminc-aarch64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| json_loads           | 32.1 us                                                      | 32.6 us: 1.02x slower                                                   |
| unpickle_pure_python | 251 us                                                       | 255 us: 1.02x slower                                                    |
| pickle_pure_python   | 359 us                                                       | 365 us: 1.02x slower                                                    |
| xml_etree_iterparse  | 147 ms                                                       | 149 ms: 1.02x slower                                                    |
| tomli_loads          | 2.57 sec                                                     | 2.62 sec: 1.02x slower                                                  |
| json_dumps           | 13.1 ms                                                      | 13.5 ms: 1.03x slower                                                   |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                            |

Benchmark hidden because not significant (3): xml_etree_parse, xml_etree_process, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-arminc-aarch64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.60 ms                                                      | 8.75 ms: 1.02x slower                                                   |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                            |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-arminc-aarch64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text    | 27.4 ms                                                      | 27.1 ms: 1.01x faster                                                   |
| mako           | 13.2 ms                                                      | 13.4 ms: 1.02x slower                                                   |
| Geometric mean | (ref)                                                        | 1.01x slower                                                            |

Benchmark hidden because not significant (2): genshi_xml, django_template

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-arminc-aarch64-python-58ce131037ecb34d506a-3.14.0a0-58ce131 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy                   | 448 us                                                       | 330 us: 1.36x faster                                                    |
| deepcopy_memo              | 50.8 us                                                      | 38.5 us: 1.32x faster                                                   |
| go                         | 161 ms                                                       | 138 ms: 1.17x faster                                                    |
| async_tree_none            | 492 ms                                                       | 423 ms: 1.16x faster                                                    |
| async_tree_memoization     | 645 ms                                                       | 556 ms: 1.16x faster                                                    |
| async_tree_none_tg         | 476 ms                                                       | 414 ms: 1.15x faster                                                    |
| deepcopy_reduce            | 4.04 us                                                      | 3.56 us: 1.13x faster                                                   |
| async_tree_memoization_tg  | 604 ms                                                       | 548 ms: 1.10x faster                                                    |
| async_tree_io_tg           | 1.27 sec                                                     | 1.17 sec: 1.09x faster                                                  |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 731 ms: 1.08x faster                                                    |
| pathlib                    | 22.8 ms                                                      | 21.3 ms: 1.07x faster                                                   |
| async_tree_io              | 1.22 sec                                                     | 1.15 sec: 1.06x faster                                                  |
| generators                 | 37.1 ms                                                      | 35.0 ms: 1.06x faster                                                   |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 720 ms: 1.06x faster                                                    |
| gc_traversal               | 5.17 ms                                                      | 4.94 ms: 1.05x faster                                                   |
| asyncio_tcp                | 584 ms                                                       | 557 ms: 1.05x faster                                                    |
| richards                   | 55.9 ms                                                      | 53.5 ms: 1.04x faster                                                   |
| html5lib                   | 66.1 ms                                                      | 63.3 ms: 1.04x faster                                                   |
| scimark_lu                 | 141 ms                                                       | 136 ms: 1.04x faster                                                    |
| 2to3                       | 305 ms                                                       | 293 ms: 1.04x faster                                                    |
| nbody                      | 114 ms                                                       | 110 ms: 1.04x faster                                                    |
| regex_dna                  | 259 ms                                                       | 249 ms: 1.04x faster                                                    |
| regex_effbot               | 4.98 ms                                                      | 4.80 ms: 1.04x faster                                                   |
| richards_super             | 62.3 ms                                                      | 60.2 ms: 1.03x faster                                                   |
| docutils                   | 3.10 sec                                                     | 3.00 sec: 1.03x faster                                                  |
| regex_v8                   | 31.1 ms                                                      | 30.2 ms: 1.03x faster                                                   |
| create_gc_cycles           | 2.33 ms                                                      | 2.28 ms: 1.02x faster                                                   |
| logging_simple             | 7.21 us                                                      | 7.05 us: 1.02x faster                                                   |
| async_generators           | 488 ms                                                       | 478 ms: 1.02x faster                                                    |
| thrift                     | 962 us                                                       | 942 us: 1.02x faster                                                    |
| scimark_sparse_mat_mult    | 6.55 ms                                                      | 6.42 ms: 1.02x faster                                                   |
| scimark_sor                | 159 ms                                                       | 157 ms: 1.02x faster                                                    |
| coroutines                 | 29.0 ms                                                      | 28.5 ms: 1.02x faster                                                   |
| sympy_sum                  | 144 ms                                                       | 141 ms: 1.02x faster                                                    |
| asyncio_tcp_ssl            | 2.21 sec                                                     | 2.18 sec: 1.01x faster                                                  |
| sympy_integrate            | 20.9 ms                                                      | 20.6 ms: 1.01x faster                                                   |
| pprint_pformat             | 1.93 sec                                                     | 1.90 sec: 1.01x faster                                                  |
| genshi_text                | 27.4 ms                                                      | 27.1 ms: 1.01x faster                                                   |
| logging_silent             | 133 ns                                                       | 132 ns: 1.01x faster                                                    |
| bench_mp_pool              | 7.03 ms                                                      | 6.96 ms: 1.01x faster                                                   |
| mdp                        | 3.33 sec                                                     | 3.32 sec: 1.00x faster                                                  |
| sqlglot_transpile          | 1.71 ms                                                      | 1.72 ms: 1.01x slower                                                   |
| float                      | 91.4 ms                                                      | 92.4 ms: 1.01x slower                                                   |
| sympy_expand               | 457 ms                                                       | 462 ms: 1.01x slower                                                    |
| json_loads                 | 32.1 us                                                      | 32.6 us: 1.02x slower                                                   |
| unpickle_pure_python       | 251 us                                                       | 255 us: 1.02x slower                                                    |
| python_startup_no_site     | 8.60 ms                                                      | 8.75 ms: 1.02x slower                                                   |
| pickle_pure_python         | 359 us                                                       | 365 us: 1.02x slower                                                    |
| xml_etree_iterparse        | 147 ms                                                       | 149 ms: 1.02x slower                                                    |
| tomli_loads                | 2.57 sec                                                     | 2.62 sec: 1.02x slower                                                  |
| mako                       | 13.2 ms                                                      | 13.4 ms: 1.02x slower                                                   |
| raytrace                   | 297 ms                                                       | 303 ms: 1.02x slower                                                    |
| nqueens                    | 98.9 ms                                                      | 101 ms: 1.02x slower                                                    |
| pyflate                    | 557 ms                                                       | 571 ms: 1.03x slower                                                    |
| fannkuch                   | 451 ms                                                       | 464 ms: 1.03x slower                                                    |
| json_dumps                 | 13.1 ms                                                      | 13.5 ms: 1.03x slower                                                   |
| Geometric mean             | (ref)                                                        | 1.02x faster                                                            |

Benchmark hidden because not significant (33): sqlglot_normalize, regex_compile, logging_format, sqlglot_parse, comprehensions, meteor_contest, sqlglot_optimize, xml_etree_parse, scimark_fft, xml_etree_process, xml_etree_generate, bench_thread_pool, spectral_norm, pprint_safe_repr, pidigits, sympy_str, hexiom, scimark_monte_carlo, chaos, pycparser, telco, bpe_tokeniser, asyncio_websockets, typing_runtime_protocols, python_startup, crypto_pyaes, genshi_xml, coverage, deltablue, django_template, tornado_http, json, pylint
Ignored benchmarks (13) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.95% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x