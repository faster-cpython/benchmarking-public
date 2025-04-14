# Results vs. 3.13.0

- fork: python
- ref: 98fa4a49fecbac3c990a
- machine: linux-aarch64
- commit hash: 98fa4a4
- commit date: 2025-03-09
- overall geometric mean: 1.039x faster
- HPT reliability: 99.25%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250309-arminc-aarch64-python-98fa4a49fecbac3c990a-3.14.0a5+-98fa4a4 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 303 ms: 1.03x faster                                                     |
| docutils       | 2.96 sec                                                 | 3.09 sec: 1.04x slower                                                   |
| html5lib       | 65.6 ms                                                  | 61.7 ms: 1.06x faster                                                    |
| sphinx         | 1.20 sec                                                 | 1.14 sec: 1.05x faster                                                   |
| Geometric mean | (ref)                                                    | 1.03x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250309-arminc-aarch64-python-98fa4a49fecbac3c990a-3.14.0a5+-98fa4a4 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization     | 664 ms                                                   | 468 ms: 1.42x faster                                                     |
| async_tree_memoization_tg  | 663 ms                                                   | 471 ms: 1.41x faster                                                     |
| async_tree_none            | 504 ms                                                   | 382 ms: 1.32x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 891 ms: 1.31x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 373 ms: 1.30x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 886 ms: 1.29x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 652 ms: 1.23x faster                                                     |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 660 ms: 1.20x faster                                                     |
| async_generators           | 500 ms                                                   | 454 ms: 1.10x faster                                                     |
| coroutines                 | 29.4 ms                                                  | 27.7 ms: 1.06x faster                                                    |
| Geometric mean             | (ref)                                                    | 1.23x faster                                                             |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250309-arminc-aarch64-python-98fa4a49fecbac3c990a-3.14.0a5+-98fa4a4 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 82.7 ms: 1.16x faster                                                    |
| Geometric mean | (ref)                                                    | 1.05x faster                                                             |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250309-arminc-aarch64-python-98fa4a49fecbac3c990a-3.14.0a5+-98fa4a4 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 3.79 ms: 1.35x faster                                                    |
| regex_v8       | 32.5 ms                                                  | 27.8 ms: 1.17x faster                                                    |
| regex_dna      | 263 ms                                                   | 237 ms: 1.11x faster                                                     |
| regex_compile  | 134 ms                                                   | 124 ms: 1.08x faster                                                     |
| Geometric mean | (ref)                                                    | 1.17x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250309-arminc-aarch64-python-98fa4a49fecbac3c990a-3.14.0a5+-98fa4a4 |
|---------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse     | 203 ms                                                   | 178 ms: 1.14x faster                                                     |
| xml_etree_iterparse | 159 ms                                                   | 142 ms: 1.12x faster                                                     |
| tomli_loads         | 2.67 sec                                                 | 2.39 sec: 1.11x faster                                                   |
| xml_etree_generate  | 118 ms                                                   | 107 ms: 1.11x faster                                                     |
| xml_etree_process   | 82.1 ms                                                  | 76.4 ms: 1.08x faster                                                    |
| Geometric mean      | (ref)                                                    | 1.05x faster                                                             |

Benchmark hidden because not significant (4): json_dumps, unpickle_pure_python, pickle_pure_python, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250309-arminc-aarch64-python-98fa4a49fecbac3c990a-3.14.0a5+-98fa4a4 |
|------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.79 ms                                                  | 10.1 ms: 1.15x slower                                                    |
| Geometric mean         | (ref)                                                    | 1.07x slower                                                             |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250309-arminc-aarch64-python-98fa4a49fecbac3c990a-3.14.0a5+-98fa4a4 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako           | 14.0 ms                                                  | 13.4 ms: 1.04x faster                                                    |
| Geometric mean | (ref)                                                    | 1.02x faster                                                             |

Benchmark hidden because not significant (3): genshi_text, genshi_xml, django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250309-arminc-aarch64-python-98fa4a49fecbac3c990a-3.14.0a5+-98fa4a4 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| deepcopy                   | 479 us                                                   | 324 us: 1.48x faster                                                     |
| async_tree_memoization     | 664 ms                                                   | 468 ms: 1.42x faster                                                     |
| async_tree_memoization_tg  | 663 ms                                                   | 471 ms: 1.41x faster                                                     |
| deepcopy_memo              | 53.0 us                                                  | 37.9 us: 1.40x faster                                                    |
| regex_effbot               | 5.10 ms                                                  | 3.79 ms: 1.35x faster                                                    |
| async_tree_none            | 504 ms                                                   | 382 ms: 1.32x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 891 ms: 1.31x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 373 ms: 1.30x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 886 ms: 1.29x faster                                                     |
| deepcopy_reduce            | 4.24 us                                                  | 3.40 us: 1.25x faster                                                    |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 652 ms: 1.23x faster                                                     |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 660 ms: 1.20x faster                                                     |
| regex_v8                   | 32.5 ms                                                  | 27.8 ms: 1.17x faster                                                    |
| float                      | 95.8 ms                                                  | 82.7 ms: 1.16x faster                                                    |
| xml_etree_parse            | 203 ms                                                   | 178 ms: 1.14x faster                                                     |
| richards                   | 54.5 ms                                                  | 48.1 ms: 1.13x faster                                                    |
| richards_super             | 60.8 ms                                                  | 53.9 ms: 1.13x faster                                                    |
| generators                 | 40.3 ms                                                  | 36.0 ms: 1.12x faster                                                    |
| xml_etree_iterparse        | 159 ms                                                   | 142 ms: 1.12x faster                                                     |
| tomli_loads                | 2.67 sec                                                 | 2.39 sec: 1.11x faster                                                   |
| scimark_fft                | 463 ms                                                   | 417 ms: 1.11x faster                                                     |
| xml_etree_generate         | 118 ms                                                   | 107 ms: 1.11x faster                                                     |
| regex_dna                  | 263 ms                                                   | 237 ms: 1.11x faster                                                     |
| pathlib                    | 24.3 ms                                                  | 22.1 ms: 1.10x faster                                                    |
| pylint                     | 345 ms                                                   | 313 ms: 1.10x faster                                                     |
| spectral_norm              | 143 ms                                                   | 130 ms: 1.10x faster                                                     |
| async_generators           | 500 ms                                                   | 454 ms: 1.10x faster                                                     |
| telco                      | 10.5 ms                                                  | 9.50 ms: 1.10x faster                                                    |
| scimark_sor                | 164 ms                                                   | 150 ms: 1.10x faster                                                     |
| sqlite_synth               | 4.08 us                                                  | 3.73 us: 1.10x faster                                                    |
| thrift                     | 1.01 ms                                                  | 923 us: 1.10x faster                                                     |
| regex_compile              | 134 ms                                                   | 124 ms: 1.08x faster                                                     |
| coverage                   | 106 ms                                                   | 98.1 ms: 1.08x faster                                                    |
| xml_etree_process          | 82.1 ms                                                  | 76.4 ms: 1.08x faster                                                    |
| logging_format             | 8.10 us                                                  | 7.57 us: 1.07x faster                                                    |
| bpe_tokeniser              | 6.02 sec                                                 | 5.62 sec: 1.07x faster                                                   |
| chaos                      | 70.7 ms                                                  | 66.4 ms: 1.06x faster                                                    |
| html5lib                   | 65.6 ms                                                  | 61.7 ms: 1.06x faster                                                    |
| coroutines                 | 29.4 ms                                                  | 27.7 ms: 1.06x faster                                                    |
| logging_simple             | 7.25 us                                                  | 6.84 us: 1.06x faster                                                    |
| mdp                        | 3.45 sec                                                 | 3.28 sec: 1.05x faster                                                   |
| sphinx                     | 1.20 sec                                                 | 1.14 sec: 1.05x faster                                                   |
| sqlalchemy_declarative     | 154 ms                                                   | 147 ms: 1.05x faster                                                     |
| mako                       | 14.0 ms                                                  | 13.4 ms: 1.04x faster                                                    |
| 2to3                       | 313 ms                                                   | 303 ms: 1.03x faster                                                     |
| k_core                     | 2.99 sec                                                 | 2.92 sec: 1.03x faster                                                   |
| sympy_str                  | 265 ms                                                   | 271 ms: 1.02x slower                                                     |
| typing_runtime_protocols   | 197 us                                                   | 204 us: 1.04x slower                                                     |
| docutils                   | 2.96 sec                                                 | 3.09 sec: 1.04x slower                                                   |
| go                         | 164 ms                                                   | 172 ms: 1.05x slower                                                     |
| create_gc_cycles           | 3.39 ms                                                  | 3.60 ms: 1.06x slower                                                    |
| fannkuch                   | 478 ms                                                   | 515 ms: 1.08x slower                                                     |
| hexiom                     | 7.34 ms                                                  | 8.12 ms: 1.11x slower                                                    |
| gc_traversal               | 5.92 ms                                                  | 6.58 ms: 1.11x slower                                                    |
| python_startup_no_site     | 8.79 ms                                                  | 10.1 ms: 1.15x slower                                                    |
| crypto_pyaes               | 84.9 ms                                                  | 98.3 ms: 1.16x slower                                                    |
| comprehensions             | 20.8 us                                                  | 24.2 us: 1.16x slower                                                    |
| subparsers                 | 20.3 ms                                                  | 25.1 ms: 1.23x slower                                                    |
| pprint_pformat             | 1.99 sec                                                 | 2.52 sec: 1.27x slower                                                   |
| pprint_safe_repr           | 962 ms                                                   | 1.24 sec: 1.29x slower                                                   |
| many_optionals             | 626 us                                                   | 846 us: 1.35x slower                                                     |
| bench_mp_pool              | 8.07 ms                                                  | 2.67 sec: 330.72x slower                                                 |
| Geometric mean             | (ref)                                                    | 1.01x slower                                                             |

Benchmark hidden because not significant (29): sympy_sum, json, scimark_monte_carlo, scimark_lu, genshi_text, logging_silent, nqueens, json_dumps, asyncio_websockets, sqlalchemy_imperative, deltablue, python_startup, pidigits, genshi_xml, bench_thread_pool, sympy_integrate, pyflate, connected_components, django_template, scimark_sparse_mat_mult, sympy_expand, shortest_path, unpickle_pure_python, meteor_contest, pycparser, raytrace, nbody, pickle_pure_python, json_loads
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (5) of results/bm-20250309-3.14.0a5+-98fa4a4-JIT/bm-20250309-arminc-aarch64-python-98fa4a49fecbac3c990a-3.14.0a5+-98fa4a4.json: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.039x faster

# HPT report

- Reliability score: 99.25% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x