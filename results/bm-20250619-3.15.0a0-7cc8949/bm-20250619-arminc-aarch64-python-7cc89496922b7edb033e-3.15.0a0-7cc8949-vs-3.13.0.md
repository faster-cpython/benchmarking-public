# Results vs. 3.13.0

- fork: python
- ref: 7cc89496922b7edb033e
- machine: linux-aarch64
- commit hash: 7cc8949
- commit date: 2025-06-19
- overall geometric mean: 1.063x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250619-arminc-aarch64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 297 ms: 1.05x faster                                                    |
| html5lib       | 65.6 ms                                                  | 62.8 ms: 1.04x faster                                                   |
| sphinx         | 1.20 sec                                                 | 1.14 sec: 1.05x faster                                                  |
| Geometric mean | (ref)                                                    | 1.04x faster                                                            |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250619-arminc-aarch64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 460 ms: 1.44x faster                                                    |
| async_tree_memoization     | 664 ms                                                   | 463 ms: 1.43x faster                                                    |
| async_tree_none            | 504 ms                                                   | 389 ms: 1.29x faster                                                    |
| async_tree_none_tg         | 484 ms                                                   | 375 ms: 1.29x faster                                                    |
| async_tree_io_tg           | 1.16 sec                                                 | 906 ms: 1.29x faster                                                    |
| async_tree_io              | 1.14 sec                                                 | 894 ms: 1.27x faster                                                    |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 650 ms: 1.23x faster                                                    |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 654 ms: 1.21x faster                                                    |
| async_generators           | 500 ms                                                   | 454 ms: 1.10x faster                                                    |
| Geometric mean             | (ref)                                                    | 1.22x faster                                                            |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250619-arminc-aarch64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 86.1 ms: 1.11x faster                                                   |
| Geometric mean | (ref)                                                    | 1.04x faster                                                            |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250619-arminc-aarch64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 3.85 ms: 1.33x faster                                                   |
| regex_v8       | 32.5 ms                                                  | 26.9 ms: 1.21x faster                                                   |
| regex_dna      | 263 ms                                                   | 219 ms: 1.20x faster                                                    |
| regex_compile  | 134 ms                                                   | 123 ms: 1.09x faster                                                    |
| Geometric mean | (ref)                                                    | 1.20x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250619-arminc-aarch64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 |
|---------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse     | 203 ms                                                   | 178 ms: 1.14x faster                                                    |
| xml_etree_iterparse | 159 ms                                                   | 143 ms: 1.11x faster                                                    |
| tomli_loads         | 2.67 sec                                                 | 2.45 sec: 1.09x faster                                                  |
| xml_etree_generate  | 118 ms                                                   | 111 ms: 1.06x faster                                                    |
| Geometric mean      | (ref)                                                    | 1.05x faster                                                            |

Benchmark hidden because not significant (5): json_dumps, xml_etree_process, json_loads, unpickle_pure_python, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250619-arminc-aarch64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 |
|------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 16.0 ms                                                  | 15.1 ms: 1.06x faster                                                   |
| python_startup_no_site | 8.79 ms                                                  | 8.60 ms: 1.02x faster                                                   |
| Geometric mean         | (ref)                                                    | 1.04x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250619-arminc-aarch64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text    | 28.6 ms                                                  | 26.6 ms: 1.07x faster                                                   |
| Geometric mean | (ref)                                                    | 1.02x faster                                                            |

Benchmark hidden because not significant (3): mako, genshi_xml, django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250619-arminc-aarch64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mdp                        | 3.45 sec                                                 | 1.69 sec: 2.04x faster                                                  |
| deepcopy                   | 479 us                                                   | 325 us: 1.47x faster                                                    |
| async_tree_memoization_tg  | 663 ms                                                   | 460 ms: 1.44x faster                                                    |
| async_tree_memoization     | 664 ms                                                   | 463 ms: 1.43x faster                                                    |
| deepcopy_memo              | 53.0 us                                                  | 38.2 us: 1.39x faster                                                   |
| regex_effbot               | 5.10 ms                                                  | 3.85 ms: 1.33x faster                                                   |
| async_tree_none            | 504 ms                                                   | 389 ms: 1.29x faster                                                    |
| async_tree_none_tg         | 484 ms                                                   | 375 ms: 1.29x faster                                                    |
| async_tree_io_tg           | 1.16 sec                                                 | 906 ms: 1.29x faster                                                    |
| async_tree_io              | 1.14 sec                                                 | 894 ms: 1.27x faster                                                    |
| go                         | 164 ms                                                   | 129 ms: 1.27x faster                                                    |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 650 ms: 1.23x faster                                                    |
| spectral_norm              | 143 ms                                                   | 118 ms: 1.21x faster                                                    |
| regex_v8                   | 32.5 ms                                                  | 26.9 ms: 1.21x faster                                                   |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 654 ms: 1.21x faster                                                    |
| regex_dna                  | 263 ms                                                   | 219 ms: 1.20x faster                                                    |
| deepcopy_reduce            | 4.24 us                                                  | 3.58 us: 1.19x faster                                                   |
| scimark_sor                | 164 ms                                                   | 144 ms: 1.14x faster                                                    |
| xml_etree_parse            | 203 ms                                                   | 178 ms: 1.14x faster                                                    |
| xml_etree_iterparse        | 159 ms                                                   | 143 ms: 1.11x faster                                                    |
| pyflate                    | 582 ms                                                   | 522 ms: 1.11x faster                                                    |
| float                      | 95.8 ms                                                  | 86.1 ms: 1.11x faster                                                   |
| telco                      | 10.5 ms                                                  | 9.44 ms: 1.11x faster                                                   |
| async_generators           | 500 ms                                                   | 454 ms: 1.10x faster                                                    |
| scimark_fft                | 463 ms                                                   | 421 ms: 1.10x faster                                                    |
| pathlib                    | 24.3 ms                                                  | 22.2 ms: 1.10x faster                                                   |
| pylint                     | 345 ms                                                   | 317 ms: 1.09x faster                                                    |
| tomli_loads                | 2.67 sec                                                 | 2.45 sec: 1.09x faster                                                  |
| regex_compile              | 134 ms                                                   | 123 ms: 1.09x faster                                                    |
| pycparser                  | 1.34 sec                                                 | 1.24 sec: 1.09x faster                                                  |
| bpe_tokeniser              | 6.02 sec                                                 | 5.53 sec: 1.09x faster                                                  |
| scimark_monte_carlo        | 87.8 ms                                                  | 80.9 ms: 1.09x faster                                                   |
| generators                 | 40.3 ms                                                  | 37.3 ms: 1.08x faster                                                   |
| meteor_contest             | 117 ms                                                   | 109 ms: 1.08x faster                                                    |
| genshi_text                | 28.6 ms                                                  | 26.6 ms: 1.07x faster                                                   |
| nqueens                    | 105 ms                                                   | 97.6 ms: 1.07x faster                                                   |
| sqlite_synth               | 4.08 us                                                  | 3.80 us: 1.07x faster                                                   |
| thrift                     | 1.01 ms                                                  | 943 us: 1.07x faster                                                    |
| python_startup             | 16.0 ms                                                  | 15.1 ms: 1.06x faster                                                   |
| xml_etree_generate         | 118 ms                                                   | 111 ms: 1.06x faster                                                    |
| 2to3                       | 313 ms                                                   | 297 ms: 1.05x faster                                                    |
| sphinx                     | 1.20 sec                                                 | 1.14 sec: 1.05x faster                                                  |
| k_core                     | 2.99 sec                                                 | 2.86 sec: 1.05x faster                                                  |
| html5lib                   | 65.6 ms                                                  | 62.8 ms: 1.04x faster                                                   |
| coverage                   | 106 ms                                                   | 102 ms: 1.04x faster                                                    |
| python_startup_no_site     | 8.79 ms                                                  | 8.60 ms: 1.02x faster                                                   |
| djangocms                  | 66.2 us                                                  | 65.0 us: 1.02x faster                                                   |
| connected_components       | 547 ms                                                   | 566 ms: 1.03x slower                                                    |
| shortest_path              | 565 ms                                                   | 587 ms: 1.04x slower                                                    |
| logging_simple             | 7.25 us                                                  | 7.56 us: 1.04x slower                                                   |
| pprint_pformat             | 1.99 sec                                                 | 2.08 sec: 1.05x slower                                                  |
| pprint_safe_repr           | 962 ms                                                   | 1.01 sec: 1.05x slower                                                  |
| raytrace                   | 310 ms                                                   | 326 ms: 1.05x slower                                                    |
| create_gc_cycles           | 3.39 ms                                                  | 3.75 ms: 1.11x slower                                                   |
| gc_traversal               | 5.92 ms                                                  | 6.97 ms: 1.18x slower                                                   |
| many_optionals             | 626 us                                                   | 746 us: 1.19x slower                                                    |
| subparsers                 | 20.3 ms                                                  | 29.1 ms: 1.43x slower                                                   |
| logging_silent             | 135 ns                                                   | 627 ns: 4.66x slower                                                    |
| Geometric mean             | (ref)                                                    | 1.05x faster                                                            |

Benchmark hidden because not significant (30): json_dumps, sympy_integrate, hexiom, xml_etree_process, chaos, json, comprehensions, crypto_pyaes, json_loads, pidigits, sympy_expand, docutils, asyncio_websockets, deltablue, mako, fannkuch, genshi_xml, django_template, sympy_sum, nbody, coroutines, typing_runtime_protocols, unpickle_pure_python, sympy_str, richards, richards_super, logging_format, scimark_sparse_mat_mult, pickle_pure_python, scimark_lu
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (5) of results/bm-20250619-3.15.0a0-7cc8949/bm-20250619-arminc-aarch64-python-7cc89496922b7edb033e-3.15.0a0-7cc8949.json: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.063x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.07x