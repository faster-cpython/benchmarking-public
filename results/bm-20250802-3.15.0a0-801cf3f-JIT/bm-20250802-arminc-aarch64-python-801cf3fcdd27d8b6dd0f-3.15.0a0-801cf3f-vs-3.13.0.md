# Results vs. 3.13.0

- fork: python
- ref: 801cf3fcdd27d8b6dd0f
- machine: linux-aarch64
- commit hash: 801cf3f
- commit date: 2025-08-02
- overall geometric mean: 1.010x faster
- HPT reliability: 98.52%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| docutils       | 2.96 sec                                                 | 3.13 sec: 1.06x slower                                                  |
| sphinx         | 1.20 sec                                                 | 1.16 sec: 1.04x faster                                                  |
| Geometric mean | (ref)                                                    | 1.00x faster                                                            |

Benchmark hidden because not significant (2): 2to3, html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization     | 664 ms                                                   | 472 ms: 1.41x faster                                                    |
| async_tree_memoization_tg  | 663 ms                                                   | 472 ms: 1.40x faster                                                    |
| async_tree_none            | 504 ms                                                   | 391 ms: 1.29x faster                                                    |
| async_tree_io_tg           | 1.16 sec                                                 | 914 ms: 1.27x faster                                                    |
| async_tree_io              | 1.14 sec                                                 | 902 ms: 1.26x faster                                                    |
| async_tree_none_tg         | 484 ms                                                   | 385 ms: 1.26x faster                                                    |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 662 ms: 1.21x faster                                                    |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 663 ms: 1.19x faster                                                    |
| async_generators           | 500 ms                                                   | 485 ms: 1.03x faster                                                    |
| Geometric mean             | (ref)                                                    | 1.20x faster                                                            |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 82.9 ms: 1.15x faster                                                   |
| nbody          | 118 ms                                                   | 127 ms: 1.07x slower                                                    |
| Geometric mean | (ref)                                                    | 1.02x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 3.79 ms: 1.34x faster                                                   |
| regex_v8       | 32.5 ms                                                  | 26.0 ms: 1.25x faster                                                   |
| regex_dna      | 263 ms                                                   | 218 ms: 1.20x faster                                                    |
| Geometric mean | (ref)                                                    | 1.21x faster                                                            |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|---------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads         | 2.67 sec                                                 | 2.31 sec: 1.16x faster                                                  |
| xml_etree_parse     | 203 ms                                                   | 178 ms: 1.14x faster                                                    |
| xml_etree_iterparse | 159 ms                                                   | 145 ms: 1.10x faster                                                    |
| xml_etree_generate  | 118 ms                                                   | 109 ms: 1.09x faster                                                    |
| xml_etree_process   | 82.1 ms                                                  | 77.3 ms: 1.06x faster                                                   |
| pickle_pure_python  | 374 us                                                   | 399 us: 1.07x slower                                                    |
| Geometric mean      | (ref)                                                    | 1.06x faster                                                            |

Benchmark hidden because not significant (3): unpickle_pure_python, json_dumps, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 16.0 ms                                                  | 15.2 ms: 1.06x faster                                                   |
| python_startup_no_site | 8.79 ms                                                  | 8.62 ms: 1.02x faster                                                   |
| Geometric mean         | (ref)                                                    | 1.04x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako           | 14.0 ms                                                  | 12.9 ms: 1.08x faster                                                   |
| genshi_text    | 28.6 ms                                                  | 26.8 ms: 1.07x faster                                                   |
| Geometric mean | (ref)                                                    | 1.02x faster                                                            |

Benchmark hidden because not significant (2): django_template, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mdp                        | 3.45 sec                                                 | 1.69 sec: 2.04x faster                                                  |
| deepcopy                   | 479 us                                                   | 331 us: 1.45x faster                                                    |
| deepcopy_memo              | 53.0 us                                                  | 37.1 us: 1.43x faster                                                   |
| async_tree_memoization     | 664 ms                                                   | 472 ms: 1.41x faster                                                    |
| async_tree_memoization_tg  | 663 ms                                                   | 472 ms: 1.40x faster                                                    |
| regex_effbot               | 5.10 ms                                                  | 3.79 ms: 1.34x faster                                                   |
| async_tree_none            | 504 ms                                                   | 391 ms: 1.29x faster                                                    |
| async_tree_io_tg           | 1.16 sec                                                 | 914 ms: 1.27x faster                                                    |
| async_tree_io              | 1.14 sec                                                 | 902 ms: 1.26x faster                                                    |
| async_tree_none_tg         | 484 ms                                                   | 385 ms: 1.26x faster                                                    |
| regex_v8                   | 32.5 ms                                                  | 26.0 ms: 1.25x faster                                                   |
| richards                   | 54.5 ms                                                  | 44.4 ms: 1.23x faster                                                   |
| spectral_norm              | 143 ms                                                   | 117 ms: 1.22x faster                                                    |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 662 ms: 1.21x faster                                                    |
| regex_dna                  | 263 ms                                                   | 218 ms: 1.20x faster                                                    |
| deepcopy_reduce            | 4.24 us                                                  | 3.54 us: 1.20x faster                                                   |
| richards_super             | 60.8 ms                                                  | 50.8 ms: 1.20x faster                                                   |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 663 ms: 1.19x faster                                                    |
| tomli_loads                | 2.67 sec                                                 | 2.31 sec: 1.16x faster                                                  |
| float                      | 95.8 ms                                                  | 82.9 ms: 1.15x faster                                                   |
| scimark_sor                | 164 ms                                                   | 143 ms: 1.14x faster                                                    |
| scimark_fft                | 463 ms                                                   | 405 ms: 1.14x faster                                                    |
| xml_etree_parse            | 203 ms                                                   | 178 ms: 1.14x faster                                                    |
| sqlite_synth               | 4.08 us                                                  | 3.64 us: 1.12x faster                                                   |
| generators                 | 40.3 ms                                                  | 36.3 ms: 1.11x faster                                                   |
| xml_etree_iterparse        | 159 ms                                                   | 145 ms: 1.10x faster                                                    |
| bpe_tokeniser              | 6.02 sec                                                 | 5.48 sec: 1.10x faster                                                  |
| pyflate                    | 582 ms                                                   | 533 ms: 1.09x faster                                                    |
| pathlib                    | 24.3 ms                                                  | 22.4 ms: 1.09x faster                                                   |
| scimark_monte_carlo        | 87.8 ms                                                  | 80.7 ms: 1.09x faster                                                   |
| xml_etree_generate         | 118 ms                                                   | 109 ms: 1.09x faster                                                    |
| mako                       | 14.0 ms                                                  | 12.9 ms: 1.08x faster                                                   |
| thrift                     | 1.01 ms                                                  | 935 us: 1.08x faster                                                    |
| logging_format             | 8.10 us                                                  | 7.56 us: 1.07x faster                                                   |
| go                         | 164 ms                                                   | 154 ms: 1.07x faster                                                    |
| genshi_text                | 28.6 ms                                                  | 26.8 ms: 1.07x faster                                                   |
| xml_etree_process          | 82.1 ms                                                  | 77.3 ms: 1.06x faster                                                   |
| python_startup             | 16.0 ms                                                  | 15.2 ms: 1.06x faster                                                   |
| logging_simple             | 7.25 us                                                  | 6.90 us: 1.05x faster                                                   |
| k_core                     | 2.99 sec                                                 | 2.87 sec: 1.04x faster                                                  |
| sphinx                     | 1.20 sec                                                 | 1.16 sec: 1.04x faster                                                  |
| async_generators           | 500 ms                                                   | 485 ms: 1.03x faster                                                    |
| python_startup_no_site     | 8.79 ms                                                  | 8.62 ms: 1.02x faster                                                   |
| djangocms                  | 66.2 us                                                  | 65.2 us: 1.02x faster                                                   |
| sympy_str                  | 265 ms                                                   | 272 ms: 1.03x slower                                                    |
| scimark_sparse_mat_mult    | 6.66 ms                                                  | 6.94 ms: 1.04x slower                                                   |
| crypto_pyaes               | 84.9 ms                                                  | 89.0 ms: 1.05x slower                                                   |
| connected_components       | 547 ms                                                   | 577 ms: 1.06x slower                                                    |
| docutils                   | 2.96 sec                                                 | 3.13 sec: 1.06x slower                                                  |
| pickle_pure_python         | 374 us                                                   | 399 us: 1.07x slower                                                    |
| shortest_path              | 565 ms                                                   | 606 ms: 1.07x slower                                                    |
| nbody                      | 118 ms                                                   | 127 ms: 1.07x slower                                                    |
| raytrace                   | 310 ms                                                   | 336 ms: 1.08x slower                                                    |
| comprehensions             | 20.8 us                                                  | 22.6 us: 1.09x slower                                                   |
| create_gc_cycles           | 3.39 ms                                                  | 3.79 ms: 1.12x slower                                                   |
| pprint_pformat             | 1.99 sec                                                 | 2.32 sec: 1.17x slower                                                  |
| gc_traversal               | 5.92 ms                                                  | 7.00 ms: 1.18x slower                                                   |
| pprint_safe_repr           | 962 ms                                                   | 1.15 sec: 1.19x slower                                                  |
| many_optionals             | 626 us                                                   | 1.01 ms: 1.61x slower                                                   |
| subparsers                 | 20.3 ms                                                  | 48.2 ms: 2.37x slower                                                   |
| telco                      | 10.5 ms                                                  | 167 ms: 15.98x slower                                                   |
| bench_mp_pool              | 8.07 ms                                                  | 3.60 sec: 446.71x slower                                                |
| Geometric mean             | (ref)                                                    | 1.05x slower                                                            |

Benchmark hidden because not significant (28): regex_compile, pylint, unpickle_pure_python, json_dumps, sympy_sum, sympy_integrate, nqueens, coverage, logging_silent, meteor_contest, deltablue, fannkuch, html5lib, chaos, json, asyncio_websockets, pycparser, 2to3, pidigits, coroutines, json_loads, scimark_lu, django_template, bench_thread_pool, sympy_expand, hexiom, genshi_xml, typing_runtime_protocols
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (13) of results/bm-20250802-3.15.0a0-801cf3f-JIT/bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.010x faster

# HPT report

- Reliability score: 98.52% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.10x