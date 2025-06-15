# Results vs. 3.13.0

- fork: python
- ref: 6eb6c5dbfb528bd07d77
- machine: linux-aarch64
- commit hash: 6eb6c5d
- commit date: 2025-06-13
- overall geometric mean: 1.019x slower
- HPT reliability: 99.99%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250613-arminc-aarch64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 298 ms: 1.05x faster                                                    |
| docutils       | 2.96 sec                                                 | 2.92 sec: 1.01x faster                                                  |
| html5lib       | 65.6 ms                                                  | 61.0 ms: 1.08x faster                                                   |
| sphinx         | 1.20 sec                                                 | 1.13 sec: 1.07x faster                                                  |
| Geometric mean | (ref)                                                    | 1.05x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250613-arminc-aarch64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 463 ms: 1.43x faster                                                    |
| async_tree_memoization     | 664 ms                                                   | 467 ms: 1.42x faster                                                    |
| async_tree_none_tg         | 484 ms                                                   | 379 ms: 1.28x faster                                                    |
| async_tree_io_tg           | 1.16 sec                                                 | 913 ms: 1.28x faster                                                    |
| async_tree_none            | 504 ms                                                   | 396 ms: 1.27x faster                                                    |
| async_tree_io              | 1.14 sec                                                 | 898 ms: 1.27x faster                                                    |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 650 ms: 1.23x faster                                                    |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 657 ms: 1.20x faster                                                    |
| async_generators           | 500 ms                                                   | 453 ms: 1.10x faster                                                    |
| Geometric mean             | (ref)                                                    | 1.22x faster                                                            |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250613-arminc-aarch64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 89.8 ms: 1.07x faster                                                   |
| Geometric mean | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250613-arminc-aarch64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 3.88 ms: 1.32x faster                                                   |
| regex_dna      | 263 ms                                                   | 221 ms: 1.19x faster                                                    |
| regex_v8       | 32.5 ms                                                  | 27.4 ms: 1.19x faster                                                   |
| regex_compile  | 134 ms                                                   | 122 ms: 1.09x faster                                                    |
| Geometric mean | (ref)                                                    | 1.19x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250613-arminc-aarch64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d |
|---------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse     | 203 ms                                                   | 180 ms: 1.12x faster                                                    |
| xml_etree_iterparse | 159 ms                                                   | 142 ms: 1.12x faster                                                    |
| tomli_loads         | 2.67 sec                                                 | 2.44 sec: 1.09x faster                                                  |
| xml_etree_process   | 82.1 ms                                                  | 79.1 ms: 1.04x faster                                                   |
| Geometric mean      | (ref)                                                    | 1.05x faster                                                            |

Benchmark hidden because not significant (5): xml_etree_generate, json_dumps, json_loads, unpickle_pure_python, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250613-arminc-aarch64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d |
|------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 16.0 ms                                                  | 15.1 ms: 1.06x faster                                                   |
| python_startup_no_site | 8.79 ms                                                  | 8.63 ms: 1.02x faster                                                   |
| Geometric mean         | (ref)                                                    | 1.04x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250613-arminc-aarch64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text    | 28.6 ms                                                  | 26.3 ms: 1.09x faster                                                   |
| Geometric mean | (ref)                                                    | 1.03x faster                                                            |

Benchmark hidden because not significant (3): mako, genshi_xml, django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250613-arminc-aarch64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mdp                        | 3.45 sec                                                 | 1.65 sec: 2.09x faster                                                  |
| deepcopy                   | 479 us                                                   | 328 us: 1.46x faster                                                    |
| async_tree_memoization_tg  | 663 ms                                                   | 463 ms: 1.43x faster                                                    |
| async_tree_memoization     | 664 ms                                                   | 467 ms: 1.42x faster                                                    |
| deepcopy_memo              | 53.0 us                                                  | 37.9 us: 1.40x faster                                                   |
| regex_effbot               | 5.10 ms                                                  | 3.88 ms: 1.32x faster                                                   |
| go                         | 164 ms                                                   | 127 ms: 1.29x faster                                                    |
| async_tree_none_tg         | 484 ms                                                   | 379 ms: 1.28x faster                                                    |
| async_tree_io_tg           | 1.16 sec                                                 | 913 ms: 1.28x faster                                                    |
| async_tree_none            | 504 ms                                                   | 396 ms: 1.27x faster                                                    |
| async_tree_io              | 1.14 sec                                                 | 898 ms: 1.27x faster                                                    |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 650 ms: 1.23x faster                                                    |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 657 ms: 1.20x faster                                                    |
| regex_dna                  | 263 ms                                                   | 221 ms: 1.19x faster                                                    |
| regex_v8                   | 32.5 ms                                                  | 27.4 ms: 1.19x faster                                                   |
| deepcopy_reduce            | 4.24 us                                                  | 3.61 us: 1.18x faster                                                   |
| generators                 | 40.3 ms                                                  | 35.6 ms: 1.13x faster                                                   |
| scimark_sor                | 164 ms                                                   | 145 ms: 1.13x faster                                                    |
| xml_etree_parse            | 203 ms                                                   | 180 ms: 1.12x faster                                                    |
| spectral_norm              | 143 ms                                                   | 128 ms: 1.12x faster                                                    |
| xml_etree_iterparse        | 159 ms                                                   | 142 ms: 1.12x faster                                                    |
| pylint                     | 345 ms                                                   | 312 ms: 1.11x faster                                                    |
| pyflate                    | 582 ms                                                   | 527 ms: 1.10x faster                                                    |
| async_generators           | 500 ms                                                   | 453 ms: 1.10x faster                                                    |
| telco                      | 10.5 ms                                                  | 9.48 ms: 1.10x faster                                                   |
| regex_compile              | 134 ms                                                   | 122 ms: 1.09x faster                                                    |
| tomli_loads                | 2.67 sec                                                 | 2.44 sec: 1.09x faster                                                  |
| bpe_tokeniser              | 6.02 sec                                                 | 5.52 sec: 1.09x faster                                                  |
| pycparser                  | 1.34 sec                                                 | 1.24 sec: 1.09x faster                                                  |
| genshi_text                | 28.6 ms                                                  | 26.3 ms: 1.09x faster                                                   |
| scimark_monte_carlo        | 87.8 ms                                                  | 81.0 ms: 1.08x faster                                                   |
| html5lib                   | 65.6 ms                                                  | 61.0 ms: 1.08x faster                                                   |
| k_core                     | 2.99 sec                                                 | 2.79 sec: 1.07x faster                                                  |
| sqlite_synth               | 4.08 us                                                  | 3.81 us: 1.07x faster                                                   |
| sphinx                     | 1.20 sec                                                 | 1.13 sec: 1.07x faster                                                  |
| float                      | 95.8 ms                                                  | 89.8 ms: 1.07x faster                                                   |
| pathlib                    | 24.3 ms                                                  | 22.8 ms: 1.06x faster                                                   |
| meteor_contest             | 117 ms                                                   | 110 ms: 1.06x faster                                                    |
| python_startup             | 16.0 ms                                                  | 15.1 ms: 1.06x faster                                                   |
| hexiom                     | 7.34 ms                                                  | 6.95 ms: 1.06x faster                                                   |
| scimark_fft                | 463 ms                                                   | 439 ms: 1.06x faster                                                    |
| sympy_integrate            | 21.4 ms                                                  | 20.4 ms: 1.05x faster                                                   |
| 2to3                       | 313 ms                                                   | 298 ms: 1.05x faster                                                    |
| nqueens                    | 105 ms                                                   | 99.9 ms: 1.05x faster                                                   |
| richards                   | 54.5 ms                                                  | 52.3 ms: 1.04x faster                                                   |
| richards_super             | 60.8 ms                                                  | 58.5 ms: 1.04x faster                                                   |
| xml_etree_process          | 82.1 ms                                                  | 79.1 ms: 1.04x faster                                                   |
| typing_runtime_protocols   | 197 us                                                   | 191 us: 1.03x faster                                                    |
| python_startup_no_site     | 8.79 ms                                                  | 8.63 ms: 1.02x faster                                                   |
| docutils                   | 2.96 sec                                                 | 2.92 sec: 1.01x faster                                                  |
| pprint_pformat             | 1.99 sec                                                 | 2.02 sec: 1.02x slower                                                  |
| connected_components       | 547 ms                                                   | 559 ms: 1.02x slower                                                    |
| shortest_path              | 565 ms                                                   | 580 ms: 1.03x slower                                                    |
| pprint_safe_repr           | 962 ms                                                   | 989 ms: 1.03x slower                                                    |
| logging_simple             | 7.25 us                                                  | 7.56 us: 1.04x slower                                                   |
| raytrace                   | 310 ms                                                   | 326 ms: 1.05x slower                                                    |
| create_gc_cycles           | 3.39 ms                                                  | 3.88 ms: 1.14x slower                                                   |
| gc_traversal               | 5.92 ms                                                  | 6.84 ms: 1.15x slower                                                   |
| many_optionals             | 626 us                                                   | 739 us: 1.18x slower                                                    |
| subparsers                 | 20.3 ms                                                  | 28.2 ms: 1.39x slower                                                   |
| logging_silent             | 135 ns                                                   | 615 ns: 4.57x slower                                                    |
| coverage                   | 106 ms                                                   | 566 ms: 5.36x slower                                                    |
| thrift                     | 1.01 ms                                                  | 193 ms: 191.39x slower                                                  |
| Geometric mean             | (ref)                                                    | 1.03x slower                                                            |

Benchmark hidden because not significant (24): xml_etree_generate, sympy_sum, json_dumps, json, comprehensions, mako, json_loads, chaos, unpickle_pure_python, asyncio_websockets, genshi_xml, crypto_pyaes, fannkuch, sympy_expand, sympy_str, django_template, pidigits, coroutines, logging_format, deltablue, pickle_pure_python, nbody, scimark_lu, scimark_sparse_mat_mult
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (5) of results/bm-20250613-3.15.0a0-6eb6c5d/bm-20250613-arminc-aarch64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d.json: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.019x slower

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.07x