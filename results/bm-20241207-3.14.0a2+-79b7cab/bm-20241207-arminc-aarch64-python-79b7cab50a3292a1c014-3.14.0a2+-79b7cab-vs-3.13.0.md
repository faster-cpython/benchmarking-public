# Results vs. 3.13.0

- fork: python
- ref: 79b7cab50a3292a1c014
- machine: linux-aarch64
- commit hash: 79b7cab
- commit date: 2024-12-07
- overall geometric mean: 1.030x faster
- HPT reliability: 99.45%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| docutils       | 2.96 sec                                                 | 3.05 sec: 1.03x slower                                                   |
| html5lib       | 65.6 ms                                                  | 63.8 ms: 1.03x faster                                                    |
| Geometric mean | (ref)                                                    | 1.01x faster                                                             |

Benchmark hidden because not significant (2): 2to3, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 520 ms: 1.27x faster                                                     |
| async_tree_none            | 504 ms                                                   | 401 ms: 1.26x faster                                                     |
| async_tree_memoization     | 664 ms                                                   | 528 ms: 1.26x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 917 ms: 1.24x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 946 ms: 1.23x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 411 ms: 1.18x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 698 ms: 1.15x faster                                                     |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 690 ms: 1.14x faster                                                     |
| Geometric mean             | (ref)                                                    | 1.15x faster                                                             |

Benchmark hidden because not significant (3): coroutines, asyncio_websockets, async_generators

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): pidigits, float, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 4.09 ms: 1.25x faster                                                    |
| regex_dna      | 263 ms                                                   | 255 ms: 1.03x faster                                                     |
| Geometric mean | (ref)                                                    | 1.08x faster                                                             |

Benchmark hidden because not significant (2): regex_compile, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|---------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_iterparse | 159 ms                                                   | 140 ms: 1.13x faster                                                     |
| xml_etree_parse     | 203 ms                                                   | 184 ms: 1.10x faster                                                     |
| tomli_loads         | 2.67 sec                                                 | 2.76 sec: 1.04x slower                                                   |
| Geometric mean      | (ref)                                                    | 1.02x faster                                                             |

Benchmark hidden because not significant (6): json_loads, xml_etree_generate, json_dumps, unpickle_pure_python, xml_etree_process, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.79 ms                                                  | 9.08 ms: 1.03x slower                                                    |
| Geometric mean         | (ref)                                                    | 1.02x slower                                                             |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|-----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 39.4 ms                                                  | 40.5 ms: 1.03x slower                                                    |
| Geometric mean  | (ref)                                                    | 1.03x slower                                                             |

Benchmark hidden because not significant (3): genshi_xml, genshi_text, mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| deepcopy                   | 479 us                                                   | 344 us: 1.39x faster                                                     |
| deepcopy_memo              | 53.0 us                                                  | 40.3 us: 1.32x faster                                                    |
| async_tree_memoization_tg  | 663 ms                                                   | 520 ms: 1.27x faster                                                     |
| async_tree_none            | 504 ms                                                   | 401 ms: 1.26x faster                                                     |
| async_tree_memoization     | 664 ms                                                   | 528 ms: 1.26x faster                                                     |
| regex_effbot               | 5.10 ms                                                  | 4.09 ms: 1.25x faster                                                    |
| async_tree_io              | 1.14 sec                                                 | 917 ms: 1.24x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 946 ms: 1.23x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 411 ms: 1.18x faster                                                     |
| deepcopy_reduce            | 4.24 us                                                  | 3.62 us: 1.17x faster                                                    |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 698 ms: 1.15x faster                                                     |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 690 ms: 1.14x faster                                                     |
| go                         | 164 ms                                                   | 144 ms: 1.14x faster                                                     |
| xml_etree_iterparse        | 159 ms                                                   | 140 ms: 1.13x faster                                                     |
| generators                 | 40.3 ms                                                  | 36.6 ms: 1.10x faster                                                    |
| xml_etree_parse            | 203 ms                                                   | 184 ms: 1.10x faster                                                     |
| pycparser                  | 1.34 sec                                                 | 1.23 sec: 1.10x faster                                                   |
| pylint                     | 345 ms                                                   | 318 ms: 1.09x faster                                                     |
| coverage                   | 106 ms                                                   | 98.7 ms: 1.07x faster                                                    |
| scimark_lu                 | 146 ms                                                   | 137 ms: 1.06x faster                                                     |
| sqlalchemy_declarative     | 154 ms                                                   | 145 ms: 1.06x faster                                                     |
| k_core                     | 2.99 sec                                                 | 2.84 sec: 1.05x faster                                                   |
| bpe_tokeniser              | 6.02 sec                                                 | 5.73 sec: 1.05x faster                                                   |
| logging_format             | 8.10 us                                                  | 7.74 us: 1.05x faster                                                    |
| regex_dna                  | 263 ms                                                   | 255 ms: 1.03x faster                                                     |
| html5lib                   | 65.6 ms                                                  | 63.8 ms: 1.03x faster                                                    |
| docutils                   | 2.96 sec                                                 | 3.05 sec: 1.03x slower                                                   |
| django_template            | 39.4 ms                                                  | 40.5 ms: 1.03x slower                                                    |
| python_startup_no_site     | 8.79 ms                                                  | 9.08 ms: 1.03x slower                                                    |
| tomli_loads                | 2.67 sec                                                 | 2.76 sec: 1.04x slower                                                   |
| pyflate                    | 582 ms                                                   | 605 ms: 1.04x slower                                                     |
| sympy_str                  | 265 ms                                                   | 278 ms: 1.05x slower                                                     |
| logging_silent             | 135 ns                                                   | 143 ns: 1.06x slower                                                     |
| many_optionals             | 626 us                                                   | 712 us: 1.14x slower                                                     |
| gc_traversal               | 5.92 ms                                                  | 6.92 ms: 1.17x slower                                                    |
| subparsers                 | 20.3 ms                                                  | 25.9 ms: 1.27x slower                                                    |
| bench_mp_pool              | 8.07 ms                                                  | 3.66 sec: 454.18x slower                                                 |
| Geometric mean             | (ref)                                                    | 1.03x slower                                                             |

Benchmark hidden because not significant (59): sympy_sum, pathlib, regex_compile, telco, sqlalchemy_imperative, json, sqlglot_optimize, thrift, sqlglot_transpile, create_gc_cycles, scimark_monte_carlo, json_loads, xml_etree_generate, scimark_fft, sphinx, 2to3, pprint_pformat, hexiom, coroutines, pprint_safe_repr, bench_thread_pool, sympy_expand, asyncio_websockets, logging_simple, djangocms, pidigits, scimark_sor, mdp, float, regex_v8, sqlite_synth, json_dumps, crypto_pyaes, connected_components, deltablue, chaos, comprehensions, richards, python_startup, shortest_path, meteor_contest, sqlglot_parse, unpickle_pure_python, nbody, richards_super, nqueens, xml_etree_process, spectral_norm, sympy_integrate, async_generators, sqlglot_normalize, fannkuch, genshi_xml, genshi_text, mako, scimark_sparse_mat_mult, pickle_pure_python, raytrace, typing_runtime_protocols
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (1) of results/bm-20241207-3.14.0a2+-79b7cab/bm-20241207-arminc-aarch64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab.json: dulwich_log

- Geometric mean (including insignificant results): 1.030x faster

# HPT report

- Reliability score: 99.45% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.02x