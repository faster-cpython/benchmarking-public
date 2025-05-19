# Results vs. 3.13.0

- fork: python
- ref: 009e7b36981fd07f7cca
- machine: linux-aarch64
- commit hash: 009e7b3
- commit date: 2025-05-18
- overall geometric mean: 1.023x slower
- HPT reliability: 99.99%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 301 ms: 1.04x faster                                                    |
| docutils       | 2.96 sec                                                 | 3.01 sec: 1.01x slower                                                  |
| html5lib       | 65.6 ms                                                  | 60.6 ms: 1.08x faster                                                   |
| sphinx         | 1.20 sec                                                 | 1.14 sec: 1.05x faster                                                  |
| Geometric mean | (ref)                                                    | 1.04x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 453 ms: 1.46x faster                                                    |
| async_tree_memoization     | 664 ms                                                   | 454 ms: 1.46x faster                                                    |
| async_tree_none_tg         | 484 ms                                                   | 364 ms: 1.33x faster                                                    |
| async_tree_io              | 1.14 sec                                                 | 866 ms: 1.31x faster                                                    |
| async_tree_none            | 504 ms                                                   | 384 ms: 1.31x faster                                                    |
| async_tree_io_tg           | 1.16 sec                                                 | 894 ms: 1.30x faster                                                    |
| async_generators           | 500 ms                                                   | 429 ms: 1.17x faster                                                    |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 715 ms: 1.12x faster                                                    |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 721 ms: 1.09x faster                                                    |
| Geometric mean             | (ref)                                                    | 1.23x faster                                                            |

Benchmark hidden because not significant (2): coroutines, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 87.0 ms: 1.10x faster                                                   |
| nbody          | 118 ms                                                   | 128 ms: 1.08x slower                                                    |
| pidigits       | 238 ms                                                   | 292 ms: 1.22x slower                                                    |
| Geometric mean | (ref)                                                    | 1.06x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 4.50 ms: 1.13x faster                                                   |
| regex_compile  | 134 ms                                                   | 120 ms: 1.11x faster                                                    |
| regex_dna      | 263 ms                                                   | 246 ms: 1.07x faster                                                    |
| Geometric mean | (ref)                                                    | 1.08x faster                                                            |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|---------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads         | 2.67 sec                                                 | 2.41 sec: 1.11x faster                                                  |
| xml_etree_generate  | 118 ms                                                   | 108 ms: 1.10x faster                                                    |
| xml_etree_process   | 82.1 ms                                                  | 75.9 ms: 1.08x faster                                                   |
| xml_etree_iterparse | 159 ms                                                   | 148 ms: 1.08x faster                                                    |
| json_dumps          | 14.2 ms                                                  | 13.4 ms: 1.06x faster                                                   |
| Geometric mean      | (ref)                                                    | 1.04x faster                                                            |

Benchmark hidden because not significant (4): unpickle_pure_python, xml_etree_parse, json_loads, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup | 16.0 ms                                                  | 15.3 ms: 1.05x faster                                                   |
| Geometric mean | (ref)                                                    | 1.02x faster                                                            |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml     | 61.6 ms                                                  | 59.9 ms: 1.03x faster                                                   |
| Geometric mean | (ref)                                                    | 1.02x faster                                                            |

Benchmark hidden because not significant (3): genshi_text, django_template, mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mdp                        | 3.45 sec                                                 | 1.64 sec: 2.10x faster                                                  |
| deepcopy                   | 479 us                                                   | 321 us: 1.49x faster                                                    |
| deepcopy_memo              | 53.0 us                                                  | 35.7 us: 1.48x faster                                                   |
| async_tree_memoization_tg  | 663 ms                                                   | 453 ms: 1.46x faster                                                    |
| async_tree_memoization     | 664 ms                                                   | 454 ms: 1.46x faster                                                    |
| async_tree_none_tg         | 484 ms                                                   | 364 ms: 1.33x faster                                                    |
| async_tree_io              | 1.14 sec                                                 | 866 ms: 1.31x faster                                                    |
| async_tree_none            | 504 ms                                                   | 384 ms: 1.31x faster                                                    |
| async_tree_io_tg           | 1.16 sec                                                 | 894 ms: 1.30x faster                                                    |
| go                         | 164 ms                                                   | 130 ms: 1.26x faster                                                    |
| deepcopy_reduce            | 4.24 us                                                  | 3.42 us: 1.24x faster                                                   |
| spectral_norm              | 143 ms                                                   | 122 ms: 1.17x faster                                                    |
| async_generators           | 500 ms                                                   | 429 ms: 1.17x faster                                                    |
| scimark_fft                | 463 ms                                                   | 400 ms: 1.16x faster                                                    |
| scimark_sor                | 164 ms                                                   | 143 ms: 1.15x faster                                                    |
| bpe_tokeniser              | 6.02 sec                                                 | 5.24 sec: 1.15x faster                                                  |
| generators                 | 40.3 ms                                                  | 35.5 ms: 1.14x faster                                                   |
| regex_effbot               | 5.10 ms                                                  | 4.50 ms: 1.13x faster                                                   |
| pyflate                    | 582 ms                                                   | 519 ms: 1.12x faster                                                    |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 715 ms: 1.12x faster                                                    |
| scimark_monte_carlo        | 87.8 ms                                                  | 78.8 ms: 1.11x faster                                                   |
| regex_compile              | 134 ms                                                   | 120 ms: 1.11x faster                                                    |
| pathlib                    | 24.3 ms                                                  | 21.9 ms: 1.11x faster                                                   |
| telco                      | 10.5 ms                                                  | 9.44 ms: 1.11x faster                                                   |
| tomli_loads                | 2.67 sec                                                 | 2.41 sec: 1.11x faster                                                  |
| float                      | 95.8 ms                                                  | 87.0 ms: 1.10x faster                                                   |
| xml_etree_generate         | 118 ms                                                   | 108 ms: 1.10x faster                                                    |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 721 ms: 1.09x faster                                                    |
| richards                   | 54.5 ms                                                  | 49.8 ms: 1.09x faster                                                   |
| scimark_lu                 | 146 ms                                                   | 134 ms: 1.09x faster                                                    |
| html5lib                   | 65.6 ms                                                  | 60.6 ms: 1.08x faster                                                   |
| xml_etree_process          | 82.1 ms                                                  | 75.9 ms: 1.08x faster                                                   |
| pycparser                  | 1.34 sec                                                 | 1.25 sec: 1.08x faster                                                  |
| chaos                      | 70.7 ms                                                  | 65.5 ms: 1.08x faster                                                   |
| richards_super             | 60.8 ms                                                  | 56.4 ms: 1.08x faster                                                   |
| k_core                     | 2.99 sec                                                 | 2.78 sec: 1.08x faster                                                  |
| xml_etree_iterparse        | 159 ms                                                   | 148 ms: 1.08x faster                                                    |
| pylint                     | 345 ms                                                   | 321 ms: 1.08x faster                                                    |
| sympy_integrate            | 21.4 ms                                                  | 20.0 ms: 1.07x faster                                                   |
| regex_dna                  | 263 ms                                                   | 246 ms: 1.07x faster                                                    |
| json_dumps                 | 14.2 ms                                                  | 13.4 ms: 1.06x faster                                                   |
| sqlite_synth               | 4.08 us                                                  | 3.86 us: 1.06x faster                                                   |
| sphinx                     | 1.20 sec                                                 | 1.14 sec: 1.05x faster                                                  |
| python_startup             | 16.0 ms                                                  | 15.3 ms: 1.05x faster                                                   |
| pprint_pformat             | 1.99 sec                                                 | 1.90 sec: 1.04x faster                                                  |
| 2to3                       | 313 ms                                                   | 301 ms: 1.04x faster                                                    |
| pprint_safe_repr           | 962 ms                                                   | 927 ms: 1.04x faster                                                    |
| sympy_expand               | 472 ms                                                   | 457 ms: 1.03x faster                                                    |
| genshi_xml                 | 61.6 ms                                                  | 59.9 ms: 1.03x faster                                                   |
| docutils                   | 2.96 sec                                                 | 3.01 sec: 1.01x slower                                                  |
| shortest_path              | 565 ms                                                   | 575 ms: 1.02x slower                                                    |
| logging_simple             | 7.25 us                                                  | 7.58 us: 1.04x slower                                                   |
| nbody                      | 118 ms                                                   | 128 ms: 1.08x slower                                                    |
| create_gc_cycles           | 3.39 ms                                                  | 3.81 ms: 1.12x slower                                                   |
| gc_traversal               | 5.92 ms                                                  | 6.70 ms: 1.13x slower                                                   |
| pidigits                   | 238 ms                                                   | 292 ms: 1.22x slower                                                    |
| many_optionals             | 626 us                                                   | 877 us: 1.40x slower                                                    |
| subparsers                 | 20.3 ms                                                  | 28.7 ms: 1.41x slower                                                   |
| logging_silent             | 135 ns                                                   | 647 ns: 4.81x slower                                                    |
| coverage                   | 106 ms                                                   | 535 ms: 5.06x slower                                                    |
| thrift                     | 1.01 ms                                                  | 193 ms: 191.00x slower                                                  |
| bench_mp_pool              | 8.07 ms                                                  | 3.27 sec: 405.01x slower                                                |
| Geometric mean             | (ref)                                                    | 1.10x slower                                                            |

Benchmark hidden because not significant (27): sympy_sum, unpickle_pure_python, genshi_text, coroutines, nqueens, comprehensions, django_template, deltablue, asyncio_websockets, typing_runtime_protocols, hexiom, json, regex_v8, scimark_sparse_mat_mult, python_startup_no_site, meteor_contest, crypto_pyaes, fannkuch, xml_etree_parse, bench_thread_pool, sympy_str, connected_components, logging_format, mako, raytrace, json_loads, pickle_pure_python
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (13) of results/bm-20250518-3.15.0a0-009e7b3-CLANG/bm-20250518-arminc-aarch64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.023x slower

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.09x