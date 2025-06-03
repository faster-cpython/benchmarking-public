# Results vs. 3.13.0

- fork: python
- ref: ec12559ebafca01ded22
- machine: linux-aarch64
- commit hash: ec12559
- commit date: 2025-06-03
- overall geometric mean: 1.026x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250603-arminc-aarch64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 300 ms: 1.04x faster                                                    |
| docutils       | 2.96 sec                                                 | 2.91 sec: 1.02x faster                                                  |
| html5lib       | 65.6 ms                                                  | 60.8 ms: 1.08x faster                                                   |
| sphinx         | 1.20 sec                                                 | 1.13 sec: 1.06x faster                                                  |
| Geometric mean | (ref)                                                    | 1.05x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250603-arminc-aarch64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization     | 664 ms                                                   | 465 ms: 1.43x faster                                                    |
| async_tree_memoization_tg  | 663 ms                                                   | 464 ms: 1.43x faster                                                    |
| async_tree_io              | 1.14 sec                                                 | 870 ms: 1.31x faster                                                    |
| async_tree_none_tg         | 484 ms                                                   | 373 ms: 1.30x faster                                                    |
| async_tree_io_tg           | 1.16 sec                                                 | 909 ms: 1.28x faster                                                    |
| async_tree_none            | 504 ms                                                   | 394 ms: 1.28x faster                                                    |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 649 ms: 1.23x faster                                                    |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 659 ms: 1.20x faster                                                    |
| async_generators           | 500 ms                                                   | 461 ms: 1.09x faster                                                    |
| Geometric mean             | (ref)                                                    | 1.22x faster                                                            |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250603-arminc-aarch64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 86.8 ms: 1.10x faster                                                   |
| Geometric mean | (ref)                                                    | 1.03x faster                                                            |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250603-arminc-aarch64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 3.80 ms: 1.34x faster                                                   |
| regex_dna      | 263 ms                                                   | 235 ms: 1.12x faster                                                    |
| regex_v8       | 32.5 ms                                                  | 29.1 ms: 1.12x faster                                                   |
| regex_compile  | 134 ms                                                   | 124 ms: 1.08x faster                                                    |
| Geometric mean | (ref)                                                    | 1.16x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250603-arminc-aarch64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 |
|---------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse     | 203 ms                                                   | 181 ms: 1.12x faster                                                    |
| xml_etree_iterparse | 159 ms                                                   | 142 ms: 1.12x faster                                                    |
| tomli_loads         | 2.67 sec                                                 | 2.50 sec: 1.07x faster                                                  |
| xml_etree_generate  | 118 ms                                                   | 112 ms: 1.06x faster                                                    |
| Geometric mean      | (ref)                                                    | 1.04x faster                                                            |

Benchmark hidden because not significant (5): json_dumps, xml_etree_process, unpickle_pure_python, json_loads, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250603-arminc-aarch64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 |
|------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 16.0 ms                                                  | 15.1 ms: 1.07x faster                                                   |
| python_startup_no_site | 8.79 ms                                                  | 8.62 ms: 1.02x faster                                                   |
| Geometric mean         | (ref)                                                    | 1.04x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250603-arminc-aarch64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text    | 28.6 ms                                                  | 27.0 ms: 1.06x faster                                                   |
| Geometric mean | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (3): mako, genshi_xml, django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250603-arminc-aarch64-python-ec12559ebafca01ded22-3.15.0a0-ec12559 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mdp                        | 3.45 sec                                                 | 1.68 sec: 2.05x faster                                                  |
| deepcopy                   | 479 us                                                   | 330 us: 1.45x faster                                                    |
| async_tree_memoization     | 664 ms                                                   | 465 ms: 1.43x faster                                                    |
| async_tree_memoization_tg  | 663 ms                                                   | 464 ms: 1.43x faster                                                    |
| deepcopy_memo              | 53.0 us                                                  | 38.2 us: 1.39x faster                                                   |
| regex_effbot               | 5.10 ms                                                  | 3.80 ms: 1.34x faster                                                   |
| async_tree_io              | 1.14 sec                                                 | 870 ms: 1.31x faster                                                    |
| async_tree_none_tg         | 484 ms                                                   | 373 ms: 1.30x faster                                                    |
| async_tree_io_tg           | 1.16 sec                                                 | 909 ms: 1.28x faster                                                    |
| async_tree_none            | 504 ms                                                   | 394 ms: 1.28x faster                                                    |
| go                         | 164 ms                                                   | 129 ms: 1.27x faster                                                    |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 649 ms: 1.23x faster                                                    |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 659 ms: 1.20x faster                                                    |
| deepcopy_reduce            | 4.24 us                                                  | 3.60 us: 1.18x faster                                                   |
| scimark_sor                | 164 ms                                                   | 144 ms: 1.14x faster                                                    |
| telco                      | 10.5 ms                                                  | 9.18 ms: 1.14x faster                                                   |
| generators                 | 40.3 ms                                                  | 35.6 ms: 1.13x faster                                                   |
| xml_etree_parse            | 203 ms                                                   | 181 ms: 1.12x faster                                                    |
| regex_dna                  | 263 ms                                                   | 235 ms: 1.12x faster                                                    |
| xml_etree_iterparse        | 159 ms                                                   | 142 ms: 1.12x faster                                                    |
| regex_v8                   | 32.5 ms                                                  | 29.1 ms: 1.12x faster                                                   |
| spectral_norm              | 143 ms                                                   | 129 ms: 1.11x faster                                                    |
| scimark_monte_carlo        | 87.8 ms                                                  | 79.0 ms: 1.11x faster                                                   |
| bpe_tokeniser              | 6.02 sec                                                 | 5.45 sec: 1.10x faster                                                  |
| float                      | 95.8 ms                                                  | 86.8 ms: 1.10x faster                                                   |
| pylint                     | 345 ms                                                   | 318 ms: 1.09x faster                                                    |
| async_generators           | 500 ms                                                   | 461 ms: 1.09x faster                                                    |
| html5lib                   | 65.6 ms                                                  | 60.8 ms: 1.08x faster                                                   |
| regex_compile              | 134 ms                                                   | 124 ms: 1.08x faster                                                    |
| pathlib                    | 24.3 ms                                                  | 22.6 ms: 1.08x faster                                                   |
| tomli_loads                | 2.67 sec                                                 | 2.50 sec: 1.07x faster                                                  |
| python_startup             | 16.0 ms                                                  | 15.1 ms: 1.07x faster                                                   |
| sympy_integrate            | 21.4 ms                                                  | 20.2 ms: 1.06x faster                                                   |
| scimark_fft                | 463 ms                                                   | 435 ms: 1.06x faster                                                    |
| sphinx                     | 1.20 sec                                                 | 1.13 sec: 1.06x faster                                                  |
| xml_etree_generate         | 118 ms                                                   | 112 ms: 1.06x faster                                                    |
| genshi_text                | 28.6 ms                                                  | 27.0 ms: 1.06x faster                                                   |
| k_core                     | 2.99 sec                                                 | 2.83 sec: 1.06x faster                                                  |
| pyflate                    | 582 ms                                                   | 550 ms: 1.06x faster                                                    |
| sqlite_synth               | 4.08 us                                                  | 3.86 us: 1.06x faster                                                   |
| pycparser                  | 1.34 sec                                                 | 1.28 sec: 1.05x faster                                                  |
| 2to3                       | 313 ms                                                   | 300 ms: 1.04x faster                                                    |
| python_startup_no_site     | 8.79 ms                                                  | 8.62 ms: 1.02x faster                                                   |
| docutils                   | 2.96 sec                                                 | 2.91 sec: 1.02x faster                                                  |
| sympy_str                  | 265 ms                                                   | 262 ms: 1.01x faster                                                    |
| pprint_pformat             | 1.99 sec                                                 | 2.03 sec: 1.02x slower                                                  |
| connected_components       | 547 ms                                                   | 558 ms: 1.02x slower                                                    |
| shortest_path              | 565 ms                                                   | 582 ms: 1.03x slower                                                    |
| pprint_safe_repr           | 962 ms                                                   | 1.00 sec: 1.04x slower                                                  |
| logging_format             | 8.10 us                                                  | 8.49 us: 1.05x slower                                                   |
| raytrace                   | 310 ms                                                   | 327 ms: 1.05x slower                                                    |
| logging_simple             | 7.25 us                                                  | 7.69 us: 1.06x slower                                                   |
| create_gc_cycles           | 3.39 ms                                                  | 3.68 ms: 1.08x slower                                                   |
| gc_traversal               | 5.92 ms                                                  | 6.97 ms: 1.18x slower                                                   |
| subparsers                 | 20.3 ms                                                  | 28.4 ms: 1.40x slower                                                   |
| many_optionals             | 626 us                                                   | 879 us: 1.40x slower                                                    |
| logging_silent             | 135 ns                                                   | 639 ns: 4.75x slower                                                    |
| coverage                   | 106 ms                                                   | 555 ms: 5.25x slower                                                    |
| thrift                     | 1.01 ms                                                  | 197 ms: 194.80x slower                                                  |
| Geometric mean             | (ref)                                                    | 1.03x slower                                                            |

Benchmark hidden because not significant (28): sympy_sum, hexiom, nqueens, json_dumps, richards, xml_etree_process, fannkuch, json, chaos, comprehensions, richards_super, mako, crypto_pyaes, meteor_contest, sympy_expand, unpickle_pure_python, asyncio_websockets, typing_runtime_protocols, pidigits, nbody, json_loads, genshi_xml, deltablue, coroutines, django_template, scimark_lu, scimark_sparse_mat_mult, pickle_pure_python
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (5) of results/bm-20250603-3.15.0a0-ec12559/bm-20250603-arminc-aarch64-python-ec12559ebafca01ded22-3.15.0a0-ec12559.json: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.026x slower

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.06x