# Results vs. 3.13.0b2

- fork: mdboom
- ref: accelerate_DJBX33A_m
- machine: linux-aarch64
- commit hash: 04d5e93
- commit date: 2024-08-27
- overall geometric mean: 1.03x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240827-arminc-aarch64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 305 ms                                                       | 294 ms: 1.04x faster                                                    |
| docutils       | 3.10 sec                                                     | 3.07 sec: 1.01x faster                                                  |
| html5lib       | 66.1 ms                                                      | 64.7 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                        | 1.02x faster                                                            |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240827-arminc-aarch64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization     | 645 ms                                                       | 556 ms: 1.16x faster                                                    |
| async_tree_none            | 492 ms                                                       | 426 ms: 1.16x faster                                                    |
| async_tree_none_tg         | 476 ms                                                       | 417 ms: 1.14x faster                                                    |
| async_tree_memoization_tg  | 604 ms                                                       | 551 ms: 1.10x faster                                                    |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 727 ms: 1.09x faster                                                    |
| async_tree_io_tg           | 1.27 sec                                                     | 1.18 sec: 1.08x faster                                                  |
| async_tree_io              | 1.22 sec                                                     | 1.13 sec: 1.08x faster                                                  |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 726 ms: 1.05x faster                                                    |
| Geometric mean             | (ref)                                                        | 1.11x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240827-arminc-aarch64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 114 ms                                                       | 109 ms: 1.05x faster                                                    |
| float          | 91.4 ms                                                      | 92.6 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                        | 1.01x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240827-arminc-aarch64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 259 ms                                                       | 245 ms: 1.06x faster                                                    |
| regex_effbot   | 4.98 ms                                                      | 4.81 ms: 1.03x faster                                                   |
| regex_compile  | 128 ms                                                       | 125 ms: 1.03x faster                                                    |
| Geometric mean | (ref)                                                        | 1.03x faster                                                            |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240827-arminc-aarch64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|---------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_process   | 80.8 ms                                                      | 77.5 ms: 1.04x faster                                                   |
| tomli_loads         | 2.57 sec                                                     | 2.55 sec: 1.01x faster                                                  |
| xml_etree_iterparse | 147 ms                                                       | 146 ms: 1.01x faster                                                    |
| json_loads          | 32.1 us                                                      | 32.2 us: 1.00x slower                                                   |
| Geometric mean      | (ref)                                                        | 1.01x faster                                                            |

Benchmark hidden because not significant (5): xml_etree_parse, pickle_pure_python, xml_etree_generate, unpickle_pure_python, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240827-arminc-aarch64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.60 ms                                                      | 8.79 ms: 1.02x slower                                                   |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                            |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240827-arminc-aarch64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml     | 60.4 ms                                                      | 59.1 ms: 1.02x faster                                                   |
| mako           | 13.2 ms                                                      | 13.6 ms: 1.04x slower                                                   |
| Geometric mean | (ref)                                                        | 1.00x slower                                                            |

Benchmark hidden because not significant (2): django_template, genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240827-arminc-aarch64-mdboom-accelerate_DJBX33A_m-3.14.0a0-04d5e93 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy                   | 448 us                                                       | 329 us: 1.36x faster                                                    |
| deepcopy_memo              | 50.8 us                                                      | 37.6 us: 1.35x faster                                                   |
| deepcopy_reduce            | 4.04 us                                                      | 3.45 us: 1.17x faster                                                   |
| async_tree_memoization     | 645 ms                                                       | 556 ms: 1.16x faster                                                    |
| async_tree_none            | 492 ms                                                       | 426 ms: 1.16x faster                                                    |
| async_tree_none_tg         | 476 ms                                                       | 417 ms: 1.14x faster                                                    |
| async_tree_memoization_tg  | 604 ms                                                       | 551 ms: 1.10x faster                                                    |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 727 ms: 1.09x faster                                                    |
| async_tree_io_tg           | 1.27 sec                                                     | 1.18 sec: 1.08x faster                                                  |
| async_tree_io              | 1.22 sec                                                     | 1.13 sec: 1.08x faster                                                  |
| pathlib                    | 22.8 ms                                                      | 21.3 ms: 1.07x faster                                                   |
| generators                 | 37.1 ms                                                      | 35.1 ms: 1.06x faster                                                   |
| regex_dna                  | 259 ms                                                       | 245 ms: 1.06x faster                                                    |
| scimark_lu                 | 141 ms                                                       | 134 ms: 1.06x faster                                                    |
| richards                   | 55.9 ms                                                      | 53.1 ms: 1.05x faster                                                   |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 726 ms: 1.05x faster                                                    |
| nbody                      | 114 ms                                                       | 109 ms: 1.05x faster                                                    |
| richards_super             | 62.3 ms                                                      | 59.6 ms: 1.05x faster                                                   |
| xml_etree_process          | 80.8 ms                                                      | 77.5 ms: 1.04x faster                                                   |
| pprint_pformat             | 1.93 sec                                                     | 1.85 sec: 1.04x faster                                                  |
| pprint_safe_repr           | 933 ms                                                       | 898 ms: 1.04x faster                                                    |
| logging_simple             | 7.21 us                                                      | 6.93 us: 1.04x faster                                                   |
| gc_traversal               | 5.17 ms                                                      | 4.98 ms: 1.04x faster                                                   |
| thrift                     | 962 us                                                       | 928 us: 1.04x faster                                                    |
| 2to3                       | 305 ms                                                       | 294 ms: 1.04x faster                                                    |
| regex_effbot               | 4.98 ms                                                      | 4.81 ms: 1.03x faster                                                   |
| bench_thread_pool          | 1.26 ms                                                      | 1.22 ms: 1.03x faster                                                   |
| sqlglot_optimize           | 62.6 ms                                                      | 61.0 ms: 1.03x faster                                                   |
| regex_compile              | 128 ms                                                       | 125 ms: 1.03x faster                                                    |
| scimark_sparse_mat_mult    | 6.55 ms                                                      | 6.41 ms: 1.02x faster                                                   |
| sympy_sum                  | 144 ms                                                       | 141 ms: 1.02x faster                                                    |
| genshi_xml                 | 60.4 ms                                                      | 59.1 ms: 1.02x faster                                                   |
| html5lib                   | 66.1 ms                                                      | 64.7 ms: 1.02x faster                                                   |
| logging_format             | 7.82 us                                                      | 7.69 us: 1.02x faster                                                   |
| coroutines                 | 29.0 ms                                                      | 28.5 ms: 1.02x faster                                                   |
| meteor_contest             | 113 ms                                                       | 112 ms: 1.02x faster                                                    |
| coverage                   | 98.4 ms                                                      | 96.9 ms: 1.01x faster                                                   |
| logging_silent             | 133 ns                                                       | 132 ns: 1.01x faster                                                    |
| sympy_str                  | 265 ms                                                       | 262 ms: 1.01x faster                                                    |
| typing_runtime_protocols   | 193 us                                                       | 191 us: 1.01x faster                                                    |
| scimark_monte_carlo        | 82.3 ms                                                      | 81.2 ms: 1.01x faster                                                   |
| scimark_sor                | 159 ms                                                       | 157 ms: 1.01x faster                                                    |
| scimark_fft                | 445 ms                                                       | 440 ms: 1.01x faster                                                    |
| hexiom                     | 7.08 ms                                                      | 7.00 ms: 1.01x faster                                                   |
| docutils                   | 3.10 sec                                                     | 3.07 sec: 1.01x faster                                                  |
| tomli_loads                | 2.57 sec                                                     | 2.55 sec: 1.01x faster                                                  |
| sympy_expand               | 457 ms                                                       | 453 ms: 1.01x faster                                                    |
| xml_etree_iterparse        | 147 ms                                                       | 146 ms: 1.01x faster                                                    |
| json_loads                 | 32.1 us                                                      | 32.2 us: 1.00x slower                                                   |
| raytrace                   | 297 ms                                                       | 300 ms: 1.01x slower                                                    |
| float                      | 91.4 ms                                                      | 92.6 ms: 1.01x slower                                                   |
| asyncio_tcp_ssl            | 2.21 sec                                                     | 2.25 sec: 1.02x slower                                                  |
| python_startup_no_site     | 8.60 ms                                                      | 8.79 ms: 1.02x slower                                                   |
| fannkuch                   | 451 ms                                                       | 467 ms: 1.03x slower                                                    |
| mako                       | 13.2 ms                                                      | 13.6 ms: 1.04x slower                                                   |
| pyflate                    | 557 ms                                                       | 579 ms: 1.04x slower                                                    |
| go                         | 161 ms                                                       | 190 ms: 1.18x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.03x faster                                                            |

Benchmark hidden because not significant (32): sqlglot_parse, regex_v8, xml_etree_parse, sqlglot_normalize, sympy_integrate, nqueens, comprehensions, json, create_gc_cycles, tornado_http, django_template, bench_mp_pool, async_generators, sqlglot_transpile, pickle_pure_python, asyncio_tcp, xml_etree_generate, pidigits, mdp, genshi_text, spectral_norm, bpe_tokeniser, telco, chaos, python_startup, crypto_pyaes, unpickle_pure_python, pycparser, asyncio_websockets, json_dumps, deltablue, pylint
Ignored benchmarks (13) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x