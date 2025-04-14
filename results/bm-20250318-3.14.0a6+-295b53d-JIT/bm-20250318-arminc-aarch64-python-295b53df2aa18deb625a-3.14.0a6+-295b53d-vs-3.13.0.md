# Results vs. 3.13.0

- fork: python
- ref: 295b53df2aa18deb625a
- machine: linux-aarch64
- commit hash: 295b53d
- commit date: 2025-03-18
- overall geometric mean: 1.003x faster
- HPT reliability: 52.36%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250318-arminc-aarch64-python-295b53df2aa18deb625a-3.14.0a6+-295b53d |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| docutils       | 2.96 sec                                                 | 3.23 sec: 1.09x slower                                                   |
| Geometric mean | (ref)                                                    | 1.02x slower                                                             |

Benchmark hidden because not significant (3): 2to3, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250318-arminc-aarch64-python-295b53df2aa18deb625a-3.14.0a6+-295b53d |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization     | 664 ms                                                   | 483 ms: 1.37x faster                                                     |
| async_tree_memoization_tg  | 663 ms                                                   | 484 ms: 1.37x faster                                                     |
| async_tree_none            | 504 ms                                                   | 394 ms: 1.28x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 379 ms: 1.28x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 898 ms: 1.27x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 923 ms: 1.26x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 662 ms: 1.21x faster                                                     |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 674 ms: 1.17x faster                                                     |
| async_generators           | 500 ms                                                   | 488 ms: 1.03x faster                                                     |
| Geometric mean             | (ref)                                                    | 1.20x faster                                                             |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250318-arminc-aarch64-python-295b53df2aa18deb625a-3.14.0a6+-295b53d |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 86.6 ms: 1.11x faster                                                    |
| nbody          | 118 ms                                                   | 129 ms: 1.09x slower                                                     |
| Geometric mean | (ref)                                                    | 1.00x faster                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250318-arminc-aarch64-python-295b53df2aa18deb625a-3.14.0a6+-295b53d |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 3.99 ms: 1.28x faster                                                    |
| regex_v8       | 32.5 ms                                                  | 28.0 ms: 1.16x faster                                                    |
| regex_dna      | 263 ms                                                   | 249 ms: 1.05x faster                                                     |
| Geometric mean | (ref)                                                    | 1.13x faster                                                             |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250318-arminc-aarch64-python-295b53df2aa18deb625a-3.14.0a6+-295b53d |
|----------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse      | 203 ms                                                   | 173 ms: 1.17x faster                                                     |
| xml_etree_iterparse  | 159 ms                                                   | 141 ms: 1.13x faster                                                     |
| tomli_loads          | 2.67 sec                                                 | 2.45 sec: 1.09x faster                                                   |
| xml_etree_generate   | 118 ms                                                   | 109 ms: 1.08x faster                                                     |
| unpickle_pure_python | 265 us                                                   | 286 us: 1.08x slower                                                     |
| pickle_pure_python   | 374 us                                                   | 408 us: 1.09x slower                                                     |
| Geometric mean       | (ref)                                                    | 1.03x faster                                                             |

Benchmark hidden because not significant (3): xml_etree_process, json_dumps, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250318-arminc-aarch64-python-295b53df2aa18deb625a-3.14.0a6+-295b53d |
|------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.79 ms                                                  | 10.2 ms: 1.16x slower                                                    |
| Geometric mean         | (ref)                                                    | 1.08x slower                                                             |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (4): genshi_text, mako, genshi_xml, django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250318-arminc-aarch64-python-295b53df2aa18deb625a-3.14.0a6+-295b53d |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| deepcopy                   | 479 us                                                   | 339 us: 1.41x faster                                                     |
| async_tree_memoization     | 664 ms                                                   | 483 ms: 1.37x faster                                                     |
| async_tree_memoization_tg  | 663 ms                                                   | 484 ms: 1.37x faster                                                     |
| deepcopy_memo              | 53.0 us                                                  | 38.9 us: 1.36x faster                                                    |
| async_tree_none            | 504 ms                                                   | 394 ms: 1.28x faster                                                     |
| regex_effbot               | 5.10 ms                                                  | 3.99 ms: 1.28x faster                                                    |
| async_tree_none_tg         | 484 ms                                                   | 379 ms: 1.28x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 898 ms: 1.27x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 923 ms: 1.26x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 662 ms: 1.21x faster                                                     |
| deepcopy_reduce            | 4.24 us                                                  | 3.57 us: 1.19x faster                                                    |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 674 ms: 1.17x faster                                                     |
| xml_etree_parse            | 203 ms                                                   | 173 ms: 1.17x faster                                                     |
| regex_v8                   | 32.5 ms                                                  | 28.0 ms: 1.16x faster                                                    |
| xml_etree_iterparse        | 159 ms                                                   | 141 ms: 1.13x faster                                                     |
| float                      | 95.8 ms                                                  | 86.6 ms: 1.11x faster                                                    |
| generators                 | 40.3 ms                                                  | 36.6 ms: 1.10x faster                                                    |
| tomli_loads                | 2.67 sec                                                 | 2.45 sec: 1.09x faster                                                   |
| thrift                     | 1.01 ms                                                  | 929 us: 1.09x faster                                                     |
| xml_etree_generate         | 118 ms                                                   | 109 ms: 1.08x faster                                                     |
| coverage                   | 106 ms                                                   | 97.5 ms: 1.08x faster                                                    |
| pathlib                    | 24.3 ms                                                  | 22.5 ms: 1.08x faster                                                    |
| scimark_fft                | 463 ms                                                   | 431 ms: 1.07x faster                                                     |
| richards_super             | 60.8 ms                                                  | 56.8 ms: 1.07x faster                                                    |
| scimark_sor                | 164 ms                                                   | 154 ms: 1.07x faster                                                     |
| regex_dna                  | 263 ms                                                   | 249 ms: 1.05x faster                                                     |
| bpe_tokeniser              | 6.02 sec                                                 | 5.71 sec: 1.05x faster                                                   |
| mdp                        | 3.45 sec                                                 | 3.35 sec: 1.03x faster                                                   |
| async_generators           | 500 ms                                                   | 488 ms: 1.03x faster                                                     |
| meteor_contest             | 117 ms                                                   | 122 ms: 1.05x slower                                                     |
| scimark_lu                 | 146 ms                                                   | 153 ms: 1.05x slower                                                     |
| connected_components       | 547 ms                                                   | 574 ms: 1.05x slower                                                     |
| deltablue                  | 3.97 ms                                                  | 4.17 ms: 1.05x slower                                                    |
| pycparser                  | 1.34 sec                                                 | 1.42 sec: 1.05x slower                                                   |
| sympy_str                  | 265 ms                                                   | 279 ms: 1.05x slower                                                     |
| shortest_path              | 565 ms                                                   | 598 ms: 1.06x slower                                                     |
| typing_runtime_protocols   | 197 us                                                   | 212 us: 1.07x slower                                                     |
| fannkuch                   | 478 ms                                                   | 515 ms: 1.08x slower                                                     |
| sympy_expand               | 472 ms                                                   | 509 ms: 1.08x slower                                                     |
| unpickle_pure_python       | 265 us                                                   | 286 us: 1.08x slower                                                     |
| scimark_sparse_mat_mult    | 6.66 ms                                                  | 7.20 ms: 1.08x slower                                                    |
| docutils                   | 2.96 sec                                                 | 3.23 sec: 1.09x slower                                                   |
| raytrace                   | 310 ms                                                   | 338 ms: 1.09x slower                                                     |
| nbody                      | 118 ms                                                   | 129 ms: 1.09x slower                                                     |
| pickle_pure_python         | 374 us                                                   | 408 us: 1.09x slower                                                     |
| create_gc_cycles           | 3.39 ms                                                  | 3.77 ms: 1.11x slower                                                    |
| go                         | 164 ms                                                   | 185 ms: 1.13x slower                                                     |
| gc_traversal               | 5.92 ms                                                  | 6.77 ms: 1.14x slower                                                    |
| python_startup_no_site     | 8.79 ms                                                  | 10.2 ms: 1.16x slower                                                    |
| hexiom                     | 7.34 ms                                                  | 8.63 ms: 1.17x slower                                                    |
| crypto_pyaes               | 84.9 ms                                                  | 102 ms: 1.20x slower                                                     |
| comprehensions             | 20.8 us                                                  | 25.4 us: 1.22x slower                                                    |
| pprint_safe_repr           | 962 ms                                                   | 1.25 sec: 1.30x slower                                                   |
| subparsers                 | 20.3 ms                                                  | 26.4 ms: 1.30x slower                                                    |
| pprint_pformat             | 1.99 sec                                                 | 2.59 sec: 1.30x slower                                                   |
| many_optionals             | 626 us                                                   | 876 us: 1.40x slower                                                     |
| bench_mp_pool              | 8.07 ms                                                  | 1.88 sec: 233.17x slower                                                 |
| Geometric mean             | (ref)                                                    | 1.05x slower                                                             |

Benchmark hidden because not significant (34): spectral_norm, regex_compile, pylint, genshi_text, sqlite_synth, telco, richards, logging_format, xml_etree_process, json, json_dumps, logging_simple, sqlalchemy_declarative, pyflate, asyncio_websockets, sympy_sum, mako, k_core, 2to3, logging_silent, html5lib, sphinx, python_startup, pidigits, bench_thread_pool, sqlalchemy_imperative, coroutines, nqueens, scimark_monte_carlo, chaos, sympy_integrate, genshi_xml, django_template, json_loads
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (5) of results/bm-20250318-3.14.0a6+-295b53d-JIT/bm-20250318-arminc-aarch64-python-295b53df2aa18deb625a-3.14.0a6+-295b53d.json: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.003x faster

# HPT report

- Reliability score: 52.36% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.05x