# Results vs. 3.13.0

- fork: python
- ref: a852c7bdd48979218a0c
- machine: linux-aarch64
- commit hash: a852c7b
- commit date: 2025-07-26
- overall geometric mean: 1.010x faster
- HPT reliability: 98.41%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| docutils       | 2.96 sec                                                 | 3.12 sec: 1.05x slower                                                  |
| sphinx         | 1.20 sec                                                 | 1.15 sec: 1.04x faster                                                  |
| Geometric mean | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (2): 2to3, html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 460 ms: 1.44x faster                                                    |
| async_tree_memoization     | 664 ms                                                   | 466 ms: 1.42x faster                                                    |
| async_tree_io              | 1.14 sec                                                 | 883 ms: 1.29x faster                                                    |
| async_tree_none_tg         | 484 ms                                                   | 376 ms: 1.29x faster                                                    |
| async_tree_none            | 504 ms                                                   | 392 ms: 1.28x faster                                                    |
| async_tree_io_tg           | 1.16 sec                                                 | 912 ms: 1.28x faster                                                    |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 649 ms: 1.23x faster                                                    |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 652 ms: 1.21x faster                                                    |
| async_generators           | 500 ms                                                   | 478 ms: 1.05x faster                                                    |
| Geometric mean             | (ref)                                                    | 1.21x faster                                                            |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 82.5 ms: 1.16x faster                                                   |
| nbody          | 118 ms                                                   | 129 ms: 1.09x slower                                                    |
| Geometric mean | (ref)                                                    | 1.02x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 3.77 ms: 1.35x faster                                                   |
| regex_v8       | 32.5 ms                                                  | 26.4 ms: 1.23x faster                                                   |
| regex_dna      | 263 ms                                                   | 216 ms: 1.22x faster                                                    |
| regex_compile  | 134 ms                                                   | 121 ms: 1.10x faster                                                    |
| Geometric mean | (ref)                                                    | 1.22x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|---------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads         | 2.67 sec                                                 | 2.32 sec: 1.15x faster                                                  |
| xml_etree_parse     | 203 ms                                                   | 177 ms: 1.14x faster                                                    |
| xml_etree_iterparse | 159 ms                                                   | 144 ms: 1.11x faster                                                    |
| xml_etree_process   | 82.1 ms                                                  | 78.4 ms: 1.05x faster                                                   |
| Geometric mean      | (ref)                                                    | 1.06x faster                                                            |

Benchmark hidden because not significant (5): xml_etree_generate, unpickle_pure_python, json_dumps, json_loads, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup | 16.0 ms                                                  | 15.2 ms: 1.06x faster                                                   |
| Geometric mean | (ref)                                                    | 1.03x faster                                                            |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako           | 14.0 ms                                                  | 12.9 ms: 1.09x faster                                                   |
| genshi_xml     | 61.6 ms                                                  | 64.1 ms: 1.04x slower                                                   |
| Geometric mean | (ref)                                                    | 1.02x faster                                                            |

Benchmark hidden because not significant (2): genshi_text, django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mdp                        | 3.45 sec                                                 | 1.62 sec: 2.12x faster                                                  |
| deepcopy                   | 479 us                                                   | 321 us: 1.49x faster                                                    |
| async_tree_memoization_tg  | 663 ms                                                   | 460 ms: 1.44x faster                                                    |
| deepcopy_memo              | 53.0 us                                                  | 37.0 us: 1.43x faster                                                   |
| async_tree_memoization     | 664 ms                                                   | 466 ms: 1.42x faster                                                    |
| regex_effbot               | 5.10 ms                                                  | 3.77 ms: 1.35x faster                                                   |
| async_tree_io              | 1.14 sec                                                 | 883 ms: 1.29x faster                                                    |
| async_tree_none_tg         | 484 ms                                                   | 376 ms: 1.29x faster                                                    |
| async_tree_none            | 504 ms                                                   | 392 ms: 1.28x faster                                                    |
| async_tree_io_tg           | 1.16 sec                                                 | 912 ms: 1.28x faster                                                    |
| spectral_norm              | 143 ms                                                   | 116 ms: 1.24x faster                                                    |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 649 ms: 1.23x faster                                                    |
| regex_v8                   | 32.5 ms                                                  | 26.4 ms: 1.23x faster                                                   |
| richards                   | 54.5 ms                                                  | 44.3 ms: 1.23x faster                                                   |
| regex_dna                  | 263 ms                                                   | 216 ms: 1.22x faster                                                    |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 652 ms: 1.21x faster                                                    |
| deepcopy_reduce            | 4.24 us                                                  | 3.52 us: 1.21x faster                                                   |
| richards_super             | 60.8 ms                                                  | 50.8 ms: 1.20x faster                                                   |
| float                      | 95.8 ms                                                  | 82.5 ms: 1.16x faster                                                   |
| tomli_loads                | 2.67 sec                                                 | 2.32 sec: 1.15x faster                                                  |
| xml_etree_parse            | 203 ms                                                   | 177 ms: 1.14x faster                                                    |
| scimark_sor                | 164 ms                                                   | 145 ms: 1.13x faster                                                    |
| scimark_fft                | 463 ms                                                   | 408 ms: 1.13x faster                                                    |
| bpe_tokeniser              | 6.02 sec                                                 | 5.37 sec: 1.12x faster                                                  |
| xml_etree_iterparse        | 159 ms                                                   | 144 ms: 1.11x faster                                                    |
| regex_compile              | 134 ms                                                   | 121 ms: 1.10x faster                                                    |
| generators                 | 40.3 ms                                                  | 37.1 ms: 1.09x faster                                                   |
| mako                       | 14.0 ms                                                  | 12.9 ms: 1.09x faster                                                   |
| sqlite_synth               | 4.08 us                                                  | 3.77 us: 1.08x faster                                                   |
| logging_format             | 8.10 us                                                  | 7.58 us: 1.07x faster                                                   |
| go                         | 164 ms                                                   | 154 ms: 1.07x faster                                                    |
| python_startup             | 16.0 ms                                                  | 15.2 ms: 1.06x faster                                                   |
| pyflate                    | 582 ms                                                   | 553 ms: 1.05x faster                                                    |
| xml_etree_process          | 82.1 ms                                                  | 78.4 ms: 1.05x faster                                                   |
| async_generators           | 500 ms                                                   | 478 ms: 1.05x faster                                                    |
| logging_simple             | 7.25 us                                                  | 6.95 us: 1.04x faster                                                   |
| logging_silent             | 135 ns                                                   | 129 ns: 1.04x faster                                                    |
| sphinx                     | 1.20 sec                                                 | 1.15 sec: 1.04x faster                                                  |
| k_core                     | 2.99 sec                                                 | 2.88 sec: 1.04x faster                                                  |
| meteor_contest             | 117 ms                                                   | 113 ms: 1.03x faster                                                    |
| djangocms                  | 66.2 us                                                  | 65.0 us: 1.02x faster                                                   |
| connected_components       | 547 ms                                                   | 561 ms: 1.03x slower                                                    |
| comprehensions             | 20.8 us                                                  | 21.5 us: 1.03x slower                                                   |
| genshi_xml                 | 61.6 ms                                                  | 64.1 ms: 1.04x slower                                                   |
| sympy_str                  | 265 ms                                                   | 276 ms: 1.04x slower                                                    |
| typing_runtime_protocols   | 197 us                                                   | 205 us: 1.04x slower                                                    |
| sympy_expand               | 472 ms                                                   | 494 ms: 1.05x slower                                                    |
| shortest_path              | 565 ms                                                   | 593 ms: 1.05x slower                                                    |
| docutils                   | 2.96 sec                                                 | 3.12 sec: 1.05x slower                                                  |
| raytrace                   | 310 ms                                                   | 329 ms: 1.06x slower                                                    |
| scimark_sparse_mat_mult    | 6.66 ms                                                  | 7.16 ms: 1.07x slower                                                   |
| crypto_pyaes               | 84.9 ms                                                  | 91.5 ms: 1.08x slower                                                   |
| nbody                      | 118 ms                                                   | 129 ms: 1.09x slower                                                    |
| gc_traversal               | 5.92 ms                                                  | 6.80 ms: 1.15x slower                                                   |
| pprint_pformat             | 1.99 sec                                                 | 2.29 sec: 1.15x slower                                                  |
| create_gc_cycles           | 3.39 ms                                                  | 3.96 ms: 1.17x slower                                                   |
| pprint_safe_repr           | 962 ms                                                   | 1.13 sec: 1.17x slower                                                  |
| many_optionals             | 626 us                                                   | 964 us: 1.54x slower                                                    |
| subparsers                 | 20.3 ms                                                  | 47.9 ms: 2.36x slower                                                   |
| telco                      | 10.5 ms                                                  | 164 ms: 15.73x slower                                                   |
| bench_mp_pool              | 8.07 ms                                                  | 1.27 sec: 157.18x slower                                                |
| Geometric mean             | (ref)                                                    | 1.03x slower                                                            |

Benchmark hidden because not significant (29): xml_etree_generate, unpickle_pure_python, pylint, pathlib, scimark_monte_carlo, thrift, fannkuch, genshi_text, deltablue, sympy_integrate, html5lib, json, json_dumps, coverage, nqueens, chaos, python_startup_no_site, sympy_sum, pycparser, asyncio_websockets, 2to3, pidigits, django_template, json_loads, hexiom, scimark_lu, bench_thread_pool, coroutines, pickle_pure_python
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (13) of results/bm-20250726-3.15.0a0-a852c7b-JIT/bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.010x faster

# HPT report

- Reliability score: 98.41% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.10x