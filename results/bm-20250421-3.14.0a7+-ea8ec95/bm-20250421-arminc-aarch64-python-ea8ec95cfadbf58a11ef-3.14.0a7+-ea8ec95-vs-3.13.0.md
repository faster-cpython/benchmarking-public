# Results vs. 3.13.0

- fork: python
- ref: ea8ec95cfadbf58a11ef
- machine: linux-aarch64
- commit hash: ea8ec95
- commit date: 2025-04-21
- overall geometric mean: 1.063x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250421-arminc-aarch64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 297 ms: 1.05x faster                                                     |
| html5lib       | 65.6 ms                                                  | 62.4 ms: 1.05x faster                                                    |
| sphinx         | 1.20 sec                                                 | 1.14 sec: 1.05x faster                                                   |
| Geometric mean | (ref)                                                    | 1.04x faster                                                             |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250421-arminc-aarch64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 475 ms: 1.39x faster                                                     |
| async_tree_memoization     | 664 ms                                                   | 481 ms: 1.38x faster                                                     |
| async_tree_none            | 504 ms                                                   | 390 ms: 1.29x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 882 ms: 1.29x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 906 ms: 1.29x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 383 ms: 1.26x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 657 ms: 1.22x faster                                                     |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 665 ms: 1.19x faster                                                     |
| async_generators           | 500 ms                                                   | 453 ms: 1.10x faster                                                     |
| Geometric mean             | (ref)                                                    | 1.21x faster                                                             |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250421-arminc-aarch64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 83.3 ms: 1.15x faster                                                    |
| Geometric mean | (ref)                                                    | 1.06x faster                                                             |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250421-arminc-aarch64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 3.73 ms: 1.37x faster                                                    |
| regex_dna      | 263 ms                                                   | 234 ms: 1.12x faster                                                     |
| regex_v8       | 32.5 ms                                                  | 29.0 ms: 1.12x faster                                                    |
| regex_compile  | 134 ms                                                   | 124 ms: 1.08x faster                                                     |
| Geometric mean | (ref)                                                    | 1.17x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250421-arminc-aarch64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 |
|---------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse     | 203 ms                                                   | 181 ms: 1.12x faster                                                     |
| xml_etree_iterparse | 159 ms                                                   | 143 ms: 1.11x faster                                                     |
| tomli_loads         | 2.67 sec                                                 | 2.46 sec: 1.09x faster                                                   |
| Geometric mean      | (ref)                                                    | 1.03x faster                                                             |

Benchmark hidden because not significant (6): xml_etree_generate, xml_etree_process, json_dumps, unpickle_pure_python, pickle_pure_python, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250421-arminc-aarch64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 |
|------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.79 ms                                                  | 10.2 ms: 1.16x slower                                                    |
| Geometric mean         | (ref)                                                    | 1.08x slower                                                             |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250421-arminc-aarch64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text    | 28.6 ms                                                  | 26.5 ms: 1.08x faster                                                    |
| genshi_xml     | 61.6 ms                                                  | 60.5 ms: 1.02x faster                                                    |
| Geometric mean | (ref)                                                    | 1.02x faster                                                             |

Benchmark hidden because not significant (2): django_template, mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250421-arminc-aarch64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| mdp                        | 3.45 sec                                                 | 1.68 sec: 2.05x faster                                                   |
| deepcopy                   | 479 us                                                   | 329 us: 1.45x faster                                                     |
| deepcopy_memo              | 53.0 us                                                  | 37.6 us: 1.41x faster                                                    |
| async_tree_memoization_tg  | 663 ms                                                   | 475 ms: 1.39x faster                                                     |
| async_tree_memoization     | 664 ms                                                   | 481 ms: 1.38x faster                                                     |
| regex_effbot               | 5.10 ms                                                  | 3.73 ms: 1.37x faster                                                    |
| async_tree_none            | 504 ms                                                   | 390 ms: 1.29x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 882 ms: 1.29x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 906 ms: 1.29x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 383 ms: 1.26x faster                                                     |
| go                         | 164 ms                                                   | 132 ms: 1.24x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 657 ms: 1.22x faster                                                     |
| deepcopy_reduce            | 4.24 us                                                  | 3.51 us: 1.21x faster                                                    |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 665 ms: 1.19x faster                                                     |
| float                      | 95.8 ms                                                  | 83.3 ms: 1.15x faster                                                    |
| spectral_norm              | 143 ms                                                   | 126 ms: 1.14x faster                                                     |
| regex_dna                  | 263 ms                                                   | 234 ms: 1.12x faster                                                     |
| xml_etree_parse            | 203 ms                                                   | 181 ms: 1.12x faster                                                     |
| regex_v8                   | 32.5 ms                                                  | 29.0 ms: 1.12x faster                                                    |
| scimark_fft                | 463 ms                                                   | 414 ms: 1.12x faster                                                     |
| scimark_sor                | 164 ms                                                   | 147 ms: 1.12x faster                                                     |
| xml_etree_iterparse        | 159 ms                                                   | 143 ms: 1.11x faster                                                     |
| bpe_tokeniser              | 6.02 sec                                                 | 5.44 sec: 1.11x faster                                                   |
| async_generators           | 500 ms                                                   | 453 ms: 1.10x faster                                                     |
| scimark_monte_carlo        | 87.8 ms                                                  | 79.8 ms: 1.10x faster                                                    |
| pylint                     | 345 ms                                                   | 315 ms: 1.10x faster                                                     |
| pyflate                    | 582 ms                                                   | 531 ms: 1.10x faster                                                     |
| generators                 | 40.3 ms                                                  | 36.8 ms: 1.10x faster                                                    |
| telco                      | 10.5 ms                                                  | 9.59 ms: 1.09x faster                                                    |
| tomli_loads                | 2.67 sec                                                 | 2.46 sec: 1.09x faster                                                   |
| pprint_pformat             | 1.99 sec                                                 | 1.83 sec: 1.08x faster                                                   |
| pprint_safe_repr           | 962 ms                                                   | 891 ms: 1.08x faster                                                     |
| nqueens                    | 105 ms                                                   | 97.3 ms: 1.08x faster                                                    |
| genshi_text                | 28.6 ms                                                  | 26.5 ms: 1.08x faster                                                    |
| regex_compile              | 134 ms                                                   | 124 ms: 1.08x faster                                                     |
| pathlib                    | 24.3 ms                                                  | 22.7 ms: 1.07x faster                                                    |
| k_core                     | 2.99 sec                                                 | 2.81 sec: 1.06x faster                                                   |
| sympy_integrate            | 21.4 ms                                                  | 20.3 ms: 1.06x faster                                                    |
| sqlite_synth               | 4.08 us                                                  | 3.86 us: 1.06x faster                                                    |
| pycparser                  | 1.34 sec                                                 | 1.27 sec: 1.06x faster                                                   |
| 2to3                       | 313 ms                                                   | 297 ms: 1.05x faster                                                     |
| html5lib                   | 65.6 ms                                                  | 62.4 ms: 1.05x faster                                                    |
| sphinx                     | 1.20 sec                                                 | 1.14 sec: 1.05x faster                                                   |
| sqlalchemy_declarative     | 154 ms                                                   | 147 ms: 1.04x faster                                                     |
| richards_super             | 60.8 ms                                                  | 58.6 ms: 1.04x faster                                                    |
| logging_format             | 8.10 us                                                  | 7.82 us: 1.04x faster                                                    |
| logging_simple             | 7.25 us                                                  | 7.01 us: 1.03x faster                                                    |
| crypto_pyaes               | 84.9 ms                                                  | 82.5 ms: 1.03x faster                                                    |
| genshi_xml                 | 61.6 ms                                                  | 60.5 ms: 1.02x faster                                                    |
| shortest_path              | 565 ms                                                   | 583 ms: 1.03x slower                                                     |
| create_gc_cycles           | 3.39 ms                                                  | 3.54 ms: 1.04x slower                                                    |
| raytrace                   | 310 ms                                                   | 324 ms: 1.04x slower                                                     |
| gc_traversal               | 5.92 ms                                                  | 6.54 ms: 1.10x slower                                                    |
| python_startup_no_site     | 8.79 ms                                                  | 10.2 ms: 1.16x slower                                                    |
| subparsers                 | 20.3 ms                                                  | 26.2 ms: 1.29x slower                                                    |
| many_optionals             | 626 us                                                   | 852 us: 1.36x slower                                                     |
| bench_mp_pool              | 8.07 ms                                                  | 4.59 sec: 568.38x slower                                                 |
| Geometric mean             | (ref)                                                    | 1.00x slower                                                             |

Benchmark hidden because not significant (33): sympy_sum, xml_etree_generate, coverage, meteor_contest, fannkuch, sympy_expand, sqlalchemy_imperative, xml_etree_process, chaos, richards, nbody, logging_silent, hexiom, pidigits, asyncio_websockets, deltablue, json_dumps, docutils, unpickle_pure_python, django_template, python_startup, scimark_sparse_mat_mult, connected_components, mako, bench_thread_pool, pickle_pure_python, json, sympy_str, coroutines, comprehensions, scimark_lu, typing_runtime_protocols, json_loads
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (5) of results/bm-20250421-3.14.0a7+-ea8ec95/bm-20250421-arminc-aarch64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95.json: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.063x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.04x