# Results vs. 3.13.0

- fork: python
- ref: 1a87b6e9ae6da255f304
- machine: linux-aarch64
- commit hash: 1a87b6e
- commit date: 2025-05-10
- overall geometric mean: 1.024x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| html5lib       | 65.6 ms                                                  | 62.0 ms: 1.06x faster                                                   |
| sphinx         | 1.20 sec                                                 | 1.16 sec: 1.04x faster                                                  |
| Geometric mean | (ref)                                                    | 1.03x faster                                                            |

Benchmark hidden because not significant (2): 2to3, docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 463 ms: 1.43x faster                                                    |
| async_tree_memoization     | 664 ms                                                   | 465 ms: 1.43x faster                                                    |
| async_tree_none            | 504 ms                                                   | 387 ms: 1.30x faster                                                    |
| async_tree_none_tg         | 484 ms                                                   | 373 ms: 1.30x faster                                                    |
| async_tree_io_tg           | 1.16 sec                                                 | 900 ms: 1.29x faster                                                    |
| async_tree_io              | 1.14 sec                                                 | 887 ms: 1.28x faster                                                    |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 655 ms: 1.22x faster                                                    |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 651 ms: 1.21x faster                                                    |
| async_generators           | 500 ms                                                   | 460 ms: 1.09x faster                                                    |
| Geometric mean             | (ref)                                                    | 1.22x faster                                                            |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 86.3 ms: 1.11x faster                                                   |
| Geometric mean | (ref)                                                    | 1.03x faster                                                            |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 3.84 ms: 1.33x faster                                                   |
| regex_v8       | 32.5 ms                                                  | 28.5 ms: 1.14x faster                                                   |
| regex_dna      | 263 ms                                                   | 240 ms: 1.09x faster                                                    |
| regex_compile  | 134 ms                                                   | 122 ms: 1.09x faster                                                    |
| Geometric mean | (ref)                                                    | 1.16x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|---------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse     | 203 ms                                                   | 180 ms: 1.13x faster                                                    |
| xml_etree_iterparse | 159 ms                                                   | 143 ms: 1.11x faster                                                    |
| tomli_loads         | 2.67 sec                                                 | 2.44 sec: 1.09x faster                                                  |
| xml_etree_generate  | 118 ms                                                   | 111 ms: 1.06x faster                                                    |
| json_loads          | 32.8 us                                                  | 36.4 us: 1.11x slower                                                   |
| Geometric mean      | (ref)                                                    | 1.02x faster                                                            |

Benchmark hidden because not significant (4): xml_etree_process, unpickle_pure_python, json_dumps, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup | 16.0 ms                                                  | 15.1 ms: 1.06x faster                                                   |
| Geometric mean | (ref)                                                    | 1.04x faster                                                            |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (4): genshi_text, django_template, mako, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mdp                        | 3.45 sec                                                 | 1.67 sec: 2.06x faster                                                  |
| async_tree_memoization_tg  | 663 ms                                                   | 463 ms: 1.43x faster                                                    |
| deepcopy                   | 479 us                                                   | 335 us: 1.43x faster                                                    |
| async_tree_memoization     | 664 ms                                                   | 465 ms: 1.43x faster                                                    |
| deepcopy_memo              | 53.0 us                                                  | 38.1 us: 1.39x faster                                                   |
| regex_effbot               | 5.10 ms                                                  | 3.84 ms: 1.33x faster                                                   |
| async_tree_none            | 504 ms                                                   | 387 ms: 1.30x faster                                                    |
| async_tree_none_tg         | 484 ms                                                   | 373 ms: 1.30x faster                                                    |
| async_tree_io_tg           | 1.16 sec                                                 | 900 ms: 1.29x faster                                                    |
| async_tree_io              | 1.14 sec                                                 | 887 ms: 1.28x faster                                                    |
| go                         | 164 ms                                                   | 129 ms: 1.27x faster                                                    |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 655 ms: 1.22x faster                                                    |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 651 ms: 1.21x faster                                                    |
| deepcopy_reduce            | 4.24 us                                                  | 3.57 us: 1.19x faster                                                   |
| regex_v8                   | 32.5 ms                                                  | 28.5 ms: 1.14x faster                                                   |
| xml_etree_parse            | 203 ms                                                   | 180 ms: 1.13x faster                                                    |
| xml_etree_iterparse        | 159 ms                                                   | 143 ms: 1.11x faster                                                    |
| scimark_sor                | 164 ms                                                   | 147 ms: 1.11x faster                                                    |
| pyflate                    | 582 ms                                                   | 523 ms: 1.11x faster                                                    |
| float                      | 95.8 ms                                                  | 86.3 ms: 1.11x faster                                                   |
| spectral_norm              | 143 ms                                                   | 130 ms: 1.10x faster                                                    |
| pylint                     | 345 ms                                                   | 315 ms: 1.10x faster                                                    |
| bpe_tokeniser              | 6.02 sec                                                 | 5.50 sec: 1.09x faster                                                  |
| regex_dna                  | 263 ms                                                   | 240 ms: 1.09x faster                                                    |
| regex_compile              | 134 ms                                                   | 122 ms: 1.09x faster                                                    |
| tomli_loads                | 2.67 sec                                                 | 2.44 sec: 1.09x faster                                                  |
| generators                 | 40.3 ms                                                  | 36.9 ms: 1.09x faster                                                   |
| sqlite_synth               | 4.08 us                                                  | 3.75 us: 1.09x faster                                                   |
| scimark_monte_carlo        | 87.8 ms                                                  | 80.6 ms: 1.09x faster                                                   |
| async_generators           | 500 ms                                                   | 460 ms: 1.09x faster                                                    |
| pprint_pformat             | 1.99 sec                                                 | 1.84 sec: 1.08x faster                                                  |
| pprint_safe_repr           | 962 ms                                                   | 891 ms: 1.08x faster                                                    |
| telco                      | 10.5 ms                                                  | 9.70 ms: 1.08x faster                                                   |
| sympy_sum                  | 151 ms                                                   | 141 ms: 1.08x faster                                                    |
| pathlib                    | 24.3 ms                                                  | 22.7 ms: 1.07x faster                                                   |
| k_core                     | 2.99 sec                                                 | 2.80 sec: 1.07x faster                                                  |
| sympy_integrate            | 21.4 ms                                                  | 20.1 ms: 1.07x faster                                                   |
| pycparser                  | 1.34 sec                                                 | 1.26 sec: 1.06x faster                                                  |
| python_startup             | 16.0 ms                                                  | 15.1 ms: 1.06x faster                                                   |
| xml_etree_generate         | 118 ms                                                   | 111 ms: 1.06x faster                                                    |
| html5lib                   | 65.6 ms                                                  | 62.0 ms: 1.06x faster                                                   |
| richards                   | 54.5 ms                                                  | 51.6 ms: 1.06x faster                                                   |
| deltablue                  | 3.97 ms                                                  | 3.78 ms: 1.05x faster                                                   |
| scimark_fft                | 463 ms                                                   | 445 ms: 1.04x faster                                                    |
| meteor_contest             | 117 ms                                                   | 113 ms: 1.04x faster                                                    |
| sphinx                     | 1.20 sec                                                 | 1.16 sec: 1.04x faster                                                  |
| connected_components       | 547 ms                                                   | 558 ms: 1.02x slower                                                    |
| shortest_path              | 565 ms                                                   | 578 ms: 1.02x slower                                                    |
| scimark_sparse_mat_mult    | 6.66 ms                                                  | 6.91 ms: 1.04x slower                                                   |
| raytrace                   | 310 ms                                                   | 325 ms: 1.05x slower                                                    |
| logging_simple             | 7.25 us                                                  | 7.63 us: 1.05x slower                                                   |
| create_gc_cycles           | 3.39 ms                                                  | 3.70 ms: 1.09x slower                                                   |
| json_loads                 | 32.8 us                                                  | 36.4 us: 1.11x slower                                                   |
| gc_traversal               | 5.92 ms                                                  | 6.97 ms: 1.18x slower                                                   |
| subparsers                 | 20.3 ms                                                  | 28.4 ms: 1.39x slower                                                   |
| many_optionals             | 626 us                                                   | 886 us: 1.41x slower                                                    |
| logging_silent             | 135 ns                                                   | 605 ns: 4.50x slower                                                    |
| coverage                   | 106 ms                                                   | 545 ms: 5.16x slower                                                    |
| thrift                     | 1.01 ms                                                  | 194 ms: 191.58x slower                                                  |
| bench_mp_pool              | 8.07 ms                                                  | 4.01 sec: 497.21x slower                                                |
| Geometric mean             | (ref)                                                    | 1.11x slower                                                            |

Benchmark hidden because not significant (29): nqueens, richards_super, genshi_text, xml_etree_process, hexiom, scimark_lu, django_template, 2to3, pidigits, sympy_expand, python_startup_no_site, asyncio_websockets, fannkuch, chaos, docutils, mako, crypto_pyaes, genshi_xml, typing_runtime_protocols, unpickle_pure_python, comprehensions, bench_thread_pool, coroutines, nbody, json, json_dumps, logging_format, sympy_str, pickle_pure_python
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (13) of results/bm-20250510-3.15.0a0-1a87b6e/bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.024x slower

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.06x