# Results vs. 3.13.0

- fork: python
- ref: 801cf3fcdd27d8b6dd0f
- machine: linux-aarch64
- commit hash: 801cf3f
- commit date: 2025-08-02
- overall geometric mean: 1.028x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 301 ms: 1.04x faster                                                    |
| html5lib       | 65.6 ms                                                  | 60.8 ms: 1.08x faster                                                   |
| sphinx         | 1.20 sec                                                 | 1.13 sec: 1.06x faster                                                  |
| Geometric mean | (ref)                                                    | 1.05x faster                                                            |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 451 ms: 1.47x faster                                                    |
| async_tree_memoization     | 664 ms                                                   | 456 ms: 1.45x faster                                                    |
| async_tree_none_tg         | 484 ms                                                   | 363 ms: 1.34x faster                                                    |
| async_tree_none            | 504 ms                                                   | 383 ms: 1.32x faster                                                    |
| async_tree_io              | 1.14 sec                                                 | 879 ms: 1.30x faster                                                    |
| async_tree_io_tg           | 1.16 sec                                                 | 906 ms: 1.29x faster                                                    |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 646 ms: 1.24x faster                                                    |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 654 ms: 1.21x faster                                                    |
| async_generators           | 500 ms                                                   | 453 ms: 1.10x faster                                                    |
| Geometric mean             | (ref)                                                    | 1.24x faster                                                            |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 84.7 ms: 1.13x faster                                                   |
| Geometric mean | (ref)                                                    | 1.03x faster                                                            |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 3.86 ms: 1.32x faster                                                   |
| regex_v8       | 32.5 ms                                                  | 27.2 ms: 1.20x faster                                                   |
| regex_dna      | 263 ms                                                   | 222 ms: 1.18x faster                                                    |
| regex_compile  | 134 ms                                                   | 121 ms: 1.10x faster                                                    |
| Geometric mean | (ref)                                                    | 1.20x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|---------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse     | 203 ms                                                   | 178 ms: 1.14x faster                                                    |
| xml_etree_iterparse | 159 ms                                                   | 141 ms: 1.13x faster                                                    |
| tomli_loads         | 2.67 sec                                                 | 2.45 sec: 1.09x faster                                                  |
| xml_etree_generate  | 118 ms                                                   | 110 ms: 1.08x faster                                                    |
| xml_etree_process   | 82.1 ms                                                  | 78.6 ms: 1.04x faster                                                   |
| Geometric mean      | (ref)                                                    | 1.05x faster                                                            |

Benchmark hidden because not significant (4): json_dumps, unpickle_pure_python, json_loads, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 16.0 ms                                                  | 15.1 ms: 1.06x faster                                                   |
| python_startup_no_site | 8.79 ms                                                  | 8.58 ms: 1.02x faster                                                   |
| Geometric mean         | (ref)                                                    | 1.04x faster                                                            |

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (4): genshi_text, genshi_xml, mako, django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mdp                        | 3.45 sec                                                 | 1.68 sec: 2.05x faster                                                  |
| async_tree_memoization_tg  | 663 ms                                                   | 451 ms: 1.47x faster                                                    |
| deepcopy                   | 479 us                                                   | 329 us: 1.45x faster                                                    |
| async_tree_memoization     | 664 ms                                                   | 456 ms: 1.45x faster                                                    |
| deepcopy_memo              | 53.0 us                                                  | 36.7 us: 1.44x faster                                                   |
| async_tree_none_tg         | 484 ms                                                   | 363 ms: 1.34x faster                                                    |
| regex_effbot               | 5.10 ms                                                  | 3.86 ms: 1.32x faster                                                   |
| async_tree_none            | 504 ms                                                   | 383 ms: 1.32x faster                                                    |
| async_tree_io              | 1.14 sec                                                 | 879 ms: 1.30x faster                                                    |
| async_tree_io_tg           | 1.16 sec                                                 | 906 ms: 1.29x faster                                                    |
| go                         | 164 ms                                                   | 128 ms: 1.28x faster                                                    |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 646 ms: 1.24x faster                                                    |
| spectral_norm              | 143 ms                                                   | 118 ms: 1.22x faster                                                    |
| deepcopy_reduce            | 4.24 us                                                  | 3.50 us: 1.21x faster                                                   |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 654 ms: 1.21x faster                                                    |
| regex_v8                   | 32.5 ms                                                  | 27.2 ms: 1.20x faster                                                   |
| regex_dna                  | 263 ms                                                   | 222 ms: 1.18x faster                                                    |
| scimark_sor                | 164 ms                                                   | 142 ms: 1.16x faster                                                    |
| xml_etree_parse            | 203 ms                                                   | 178 ms: 1.14x faster                                                    |
| generators                 | 40.3 ms                                                  | 35.3 ms: 1.14x faster                                                   |
| float                      | 95.8 ms                                                  | 84.7 ms: 1.13x faster                                                   |
| xml_etree_iterparse        | 159 ms                                                   | 141 ms: 1.13x faster                                                    |
| pyflate                    | 582 ms                                                   | 515 ms: 1.13x faster                                                    |
| pathlib                    | 24.3 ms                                                  | 21.7 ms: 1.12x faster                                                   |
| async_generators           | 500 ms                                                   | 453 ms: 1.10x faster                                                    |
| regex_compile              | 134 ms                                                   | 121 ms: 1.10x faster                                                    |
| scimark_fft                | 463 ms                                                   | 422 ms: 1.10x faster                                                    |
| scimark_monte_carlo        | 87.8 ms                                                  | 80.3 ms: 1.09x faster                                                   |
| bpe_tokeniser              | 6.02 sec                                                 | 5.52 sec: 1.09x faster                                                  |
| tomli_loads                | 2.67 sec                                                 | 2.45 sec: 1.09x faster                                                  |
| pprint_pformat             | 1.99 sec                                                 | 1.82 sec: 1.09x faster                                                  |
| sqlite_synth               | 4.08 us                                                  | 3.75 us: 1.09x faster                                                   |
| pycparser                  | 1.34 sec                                                 | 1.24 sec: 1.08x faster                                                  |
| k_core                     | 2.99 sec                                                 | 2.77 sec: 1.08x faster                                                  |
| html5lib                   | 65.6 ms                                                  | 60.8 ms: 1.08x faster                                                   |
| xml_etree_generate         | 118 ms                                                   | 110 ms: 1.08x faster                                                    |
| pylint                     | 345 ms                                                   | 321 ms: 1.07x faster                                                    |
| pprint_safe_repr           | 962 ms                                                   | 896 ms: 1.07x faster                                                    |
| logging_format             | 8.10 us                                                  | 7.56 us: 1.07x faster                                                   |
| nqueens                    | 105 ms                                                   | 98.2 ms: 1.07x faster                                                   |
| sympy_integrate            | 21.4 ms                                                  | 20.1 ms: 1.07x faster                                                   |
| sympy_sum                  | 151 ms                                                   | 142 ms: 1.07x faster                                                    |
| python_startup             | 16.0 ms                                                  | 15.1 ms: 1.06x faster                                                   |
| hexiom                     | 7.34 ms                                                  | 6.92 ms: 1.06x faster                                                   |
| sphinx                     | 1.20 sec                                                 | 1.13 sec: 1.06x faster                                                  |
| logging_silent             | 135 ns                                                   | 128 ns: 1.05x faster                                                    |
| logging_simple             | 7.25 us                                                  | 6.90 us: 1.05x faster                                                   |
| comprehensions             | 20.8 us                                                  | 19.9 us: 1.05x faster                                                   |
| xml_etree_process          | 82.1 ms                                                  | 78.6 ms: 1.04x faster                                                   |
| 2to3                       | 313 ms                                                   | 301 ms: 1.04x faster                                                    |
| python_startup_no_site     | 8.79 ms                                                  | 8.58 ms: 1.02x faster                                                   |
| djangocms                  | 66.2 us                                                  | 65.0 us: 1.02x faster                                                   |
| shortest_path              | 565 ms                                                   | 585 ms: 1.03x slower                                                    |
| raytrace                   | 310 ms                                                   | 323 ms: 1.04x slower                                                    |
| scimark_sparse_mat_mult    | 6.66 ms                                                  | 7.05 ms: 1.06x slower                                                   |
| create_gc_cycles           | 3.39 ms                                                  | 3.74 ms: 1.10x slower                                                   |
| gc_traversal               | 5.92 ms                                                  | 6.88 ms: 1.16x slower                                                   |
| many_optionals             | 626 us                                                   | 973 us: 1.55x slower                                                    |
| subparsers                 | 20.3 ms                                                  | 47.5 ms: 2.34x slower                                                   |
| telco                      | 10.5 ms                                                  | 164 ms: 15.70x slower                                                   |
| bench_mp_pool              | 8.07 ms                                                  | 2.99 sec: 370.79x slower                                                |
| Geometric mean             | (ref)                                                    | 1.03x slower                                                            |

Benchmark hidden because not significant (29): meteor_contest, genshi_text, fannkuch, json_dumps, coverage, thrift, scimark_lu, json, sympy_expand, richards, chaos, unpickle_pure_python, genshi_xml, deltablue, typing_runtime_protocols, mako, crypto_pyaes, docutils, asyncio_websockets, pidigits, coroutines, json_loads, connected_components, bench_thread_pool, django_template, sympy_str, richards_super, nbody, pickle_pure_python
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (13) of results/bm-20250802-3.15.0a0-801cf3f/bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.028x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.08x