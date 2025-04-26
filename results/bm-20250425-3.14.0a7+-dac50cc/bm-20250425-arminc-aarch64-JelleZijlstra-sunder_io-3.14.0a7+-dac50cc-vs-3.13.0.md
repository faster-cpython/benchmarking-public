# Results vs. 3.13.0

- fork: JelleZijlstra
- ref: sunder_io
- machine: linux-aarch64
- commit hash: dac50cc
- commit date: 2025-04-25
- overall geometric mean: 1.067x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250425-arminc-aarch64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|----------------|:--------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 295 ms: 1.06x faster                                                 |
| html5lib       | 65.6 ms                                                  | 61.7 ms: 1.06x faster                                                |
| sphinx         | 1.20 sec                                                 | 1.14 sec: 1.05x faster                                               |
| Geometric mean | (ref)                                                    | 1.05x faster                                                         |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250425-arminc-aarch64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|----------------------------|:--------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_memoization     | 664 ms                                                   | 461 ms: 1.44x faster                                                 |
| async_tree_memoization_tg  | 663 ms                                                   | 463 ms: 1.43x faster                                                 |
| async_tree_io_tg           | 1.16 sec                                                 | 887 ms: 1.31x faster                                                 |
| async_tree_none            | 504 ms                                                   | 385 ms: 1.31x faster                                                 |
| async_tree_none_tg         | 484 ms                                                   | 373 ms: 1.30x faster                                                 |
| async_tree_io              | 1.14 sec                                                 | 894 ms: 1.27x faster                                                 |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 644 ms: 1.24x faster                                                 |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 658 ms: 1.20x faster                                                 |
| async_generators           | 500 ms                                                   | 446 ms: 1.12x faster                                                 |
| Geometric mean             | (ref)                                                    | 1.23x faster                                                         |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250425-arminc-aarch64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|----------------|:--------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 84.8 ms: 1.13x faster                                                |
| Geometric mean | (ref)                                                    | 1.04x faster                                                         |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250425-arminc-aarch64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|----------------|:--------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 3.82 ms: 1.34x faster                                                |
| regex_v8       | 32.5 ms                                                  | 27.4 ms: 1.19x faster                                                |
| regex_dna      | 263 ms                                                   | 236 ms: 1.12x faster                                                 |
| regex_compile  | 134 ms                                                   | 120 ms: 1.11x faster                                                 |
| Geometric mean | (ref)                                                    | 1.18x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250425-arminc-aarch64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|---------------------|:--------------------------------------------------------:|:--------------------------------------------------------------------:|
| xml_etree_parse     | 203 ms                                                   | 180 ms: 1.13x faster                                                 |
| xml_etree_iterparse | 159 ms                                                   | 144 ms: 1.11x faster                                                 |
| tomli_loads         | 2.67 sec                                                 | 2.44 sec: 1.09x faster                                               |
| json_loads          | 32.8 us                                                  | 35.1 us: 1.07x slower                                                |
| Geometric mean      | (ref)                                                    | 1.03x faster                                                         |

Benchmark hidden because not significant (5): xml_etree_generate, xml_etree_process, unpickle_pure_python, json_dumps, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250425-arminc-aarch64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|------------------------|:--------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 8.79 ms                                                  | 8.59 ms: 1.02x faster                                                |
| Geometric mean         | (ref)                                                    | 1.01x faster                                                         |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250425-arminc-aarch64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|----------------|:--------------------------------------------------------:|:--------------------------------------------------------------------:|
| genshi_text    | 28.6 ms                                                  | 26.4 ms: 1.08x faster                                                |
| genshi_xml     | 61.6 ms                                                  | 60.1 ms: 1.02x faster                                                |
| Geometric mean | (ref)                                                    | 1.02x faster                                                         |

Benchmark hidden because not significant (2): mako, django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250425-arminc-aarch64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc |
|----------------------------|:--------------------------------------------------------:|:--------------------------------------------------------------------:|
| mdp                        | 3.45 sec                                                 | 1.64 sec: 2.10x faster                                               |
| async_tree_memoization     | 664 ms                                                   | 461 ms: 1.44x faster                                                 |
| deepcopy                   | 479 us                                                   | 334 us: 1.44x faster                                                 |
| async_tree_memoization_tg  | 663 ms                                                   | 463 ms: 1.43x faster                                                 |
| deepcopy_memo              | 53.0 us                                                  | 38.6 us: 1.37x faster                                                |
| regex_effbot               | 5.10 ms                                                  | 3.82 ms: 1.34x faster                                                |
| async_tree_io_tg           | 1.16 sec                                                 | 887 ms: 1.31x faster                                                 |
| async_tree_none            | 504 ms                                                   | 385 ms: 1.31x faster                                                 |
| async_tree_none_tg         | 484 ms                                                   | 373 ms: 1.30x faster                                                 |
| async_tree_io              | 1.14 sec                                                 | 894 ms: 1.27x faster                                                 |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 644 ms: 1.24x faster                                                 |
| go                         | 164 ms                                                   | 134 ms: 1.23x faster                                                 |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 658 ms: 1.20x faster                                                 |
| deepcopy_reduce            | 4.24 us                                                  | 3.55 us: 1.20x faster                                                |
| regex_v8                   | 32.5 ms                                                  | 27.4 ms: 1.19x faster                                                |
| telco                      | 10.5 ms                                                  | 9.00 ms: 1.16x faster                                                |
| spectral_norm              | 143 ms                                                   | 125 ms: 1.15x faster                                                 |
| float                      | 95.8 ms                                                  | 84.8 ms: 1.13x faster                                                |
| xml_etree_parse            | 203 ms                                                   | 180 ms: 1.13x faster                                                 |
| bpe_tokeniser              | 6.02 sec                                                 | 5.35 sec: 1.12x faster                                               |
| async_generators           | 500 ms                                                   | 446 ms: 1.12x faster                                                 |
| regex_dna                  | 263 ms                                                   | 236 ms: 1.12x faster                                                 |
| scimark_sor                | 164 ms                                                   | 148 ms: 1.11x faster                                                 |
| scimark_monte_carlo        | 87.8 ms                                                  | 78.9 ms: 1.11x faster                                                |
| regex_compile              | 134 ms                                                   | 120 ms: 1.11x faster                                                 |
| xml_etree_iterparse        | 159 ms                                                   | 144 ms: 1.11x faster                                                 |
| generators                 | 40.3 ms                                                  | 36.5 ms: 1.10x faster                                                |
| pylint                     | 345 ms                                                   | 314 ms: 1.10x faster                                                 |
| scimark_fft                | 463 ms                                                   | 421 ms: 1.10x faster                                                 |
| tomli_loads                | 2.67 sec                                                 | 2.44 sec: 1.09x faster                                               |
| sqlite_synth               | 4.08 us                                                  | 3.75 us: 1.09x faster                                                |
| pathlib                    | 24.3 ms                                                  | 22.4 ms: 1.08x faster                                                |
| genshi_text                | 28.6 ms                                                  | 26.4 ms: 1.08x faster                                                |
| pprint_pformat             | 1.99 sec                                                 | 1.84 sec: 1.08x faster                                               |
| nqueens                    | 105 ms                                                   | 97.5 ms: 1.08x faster                                                |
| pycparser                  | 1.34 sec                                                 | 1.26 sec: 1.07x faster                                               |
| k_core                     | 2.99 sec                                                 | 2.81 sec: 1.07x faster                                               |
| html5lib                   | 65.6 ms                                                  | 61.7 ms: 1.06x faster                                                |
| pyflate                    | 582 ms                                                   | 548 ms: 1.06x faster                                                 |
| pprint_safe_repr           | 962 ms                                                   | 906 ms: 1.06x faster                                                 |
| logging_format             | 8.10 us                                                  | 7.65 us: 1.06x faster                                                |
| 2to3                       | 313 ms                                                   | 295 ms: 1.06x faster                                                 |
| coverage                   | 106 ms                                                   | 100 ms: 1.06x faster                                                 |
| richards                   | 54.5 ms                                                  | 51.6 ms: 1.06x faster                                                |
| sphinx                     | 1.20 sec                                                 | 1.14 sec: 1.05x faster                                               |
| logging_simple             | 7.25 us                                                  | 7.00 us: 1.04x faster                                                |
| genshi_xml                 | 61.6 ms                                                  | 60.1 ms: 1.02x faster                                                |
| sympy_str                  | 265 ms                                                   | 259 ms: 1.02x faster                                                 |
| python_startup_no_site     | 8.79 ms                                                  | 8.59 ms: 1.02x faster                                                |
| connected_components       | 547 ms                                                   | 556 ms: 1.02x slower                                                 |
| shortest_path              | 565 ms                                                   | 584 ms: 1.03x slower                                                 |
| create_gc_cycles           | 3.39 ms                                                  | 3.55 ms: 1.05x slower                                                |
| raytrace                   | 310 ms                                                   | 325 ms: 1.05x slower                                                 |
| json_loads                 | 32.8 us                                                  | 35.1 us: 1.07x slower                                                |
| gc_traversal               | 5.92 ms                                                  | 6.56 ms: 1.11x slower                                                |
| subparsers                 | 20.3 ms                                                  | 26.4 ms: 1.30x slower                                                |
| many_optionals             | 626 us                                                   | 825 us: 1.32x slower                                                 |
| bench_mp_pool              | 8.07 ms                                                  | 2.22 sec: 275.20x slower                                             |
| Geometric mean             | (ref)                                                    | 1.01x faster                                                         |

Benchmark hidden because not significant (32): sympy_integrate, sympy_sum, xml_etree_generate, chaos, sqlalchemy_declarative, sqlalchemy_imperative, meteor_contest, xml_etree_process, sympy_expand, richards_super, crypto_pyaes, hexiom, scimark_sparse_mat_mult, asyncio_websockets, pidigits, logging_silent, deltablue, docutils, unpickle_pure_python, fannkuch, mako, comprehensions, django_template, json, python_startup, nbody, coroutines, json_dumps, pickle_pure_python, scimark_lu, bench_thread_pool, typing_runtime_protocols
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (5) of results/bm-20250425-3.14.0a7+-dac50cc/bm-20250425-arminc-aarch64-JelleZijlstra-sunder_io-3.14.0a7+-dac50cc.json: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.067x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.04x