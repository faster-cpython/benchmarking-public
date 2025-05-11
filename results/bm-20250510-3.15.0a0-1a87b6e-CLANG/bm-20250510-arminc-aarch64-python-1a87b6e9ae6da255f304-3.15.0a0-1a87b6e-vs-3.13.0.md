# Results vs. 3.13.0

- fork: python
- ref: 1a87b6e9ae6da255f304
- machine: linux-aarch64
- commit hash: 1a87b6e
- commit date: 2025-05-10
- overall geometric mean: 1.021x slower
- HPT reliability: 99.99%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 301 ms: 1.04x faster                                                    |
| docutils       | 2.96 sec                                                 | 3.02 sec: 1.02x slower                                                  |
| html5lib       | 65.6 ms                                                  | 60.2 ms: 1.09x faster                                                   |
| sphinx         | 1.20 sec                                                 | 1.16 sec: 1.04x faster                                                  |
| Geometric mean | (ref)                                                    | 1.04x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 449 ms: 1.48x faster                                                    |
| async_tree_memoization     | 664 ms                                                   | 455 ms: 1.46x faster                                                    |
| async_tree_none_tg         | 484 ms                                                   | 360 ms: 1.35x faster                                                    |
| async_tree_io              | 1.14 sec                                                 | 863 ms: 1.32x faster                                                    |
| async_tree_none            | 504 ms                                                   | 383 ms: 1.32x faster                                                    |
| async_tree_io_tg           | 1.16 sec                                                 | 894 ms: 1.30x faster                                                    |
| async_generators           | 500 ms                                                   | 432 ms: 1.16x faster                                                    |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 711 ms: 1.13x faster                                                    |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 721 ms: 1.10x faster                                                    |
| Geometric mean             | (ref)                                                    | 1.23x faster                                                            |

Benchmark hidden because not significant (2): coroutines, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 86.3 ms: 1.11x faster                                                   |
| nbody          | 118 ms                                                   | 129 ms: 1.09x slower                                                    |
| pidigits       | 238 ms                                                   | 292 ms: 1.22x slower                                                    |
| Geometric mean | (ref)                                                    | 1.06x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 134 ms                                                   | 120 ms: 1.12x faster                                                    |
| regex_effbot   | 5.10 ms                                                  | 4.64 ms: 1.10x faster                                                   |
| regex_dna      | 263 ms                                                   | 247 ms: 1.07x faster                                                    |
| regex_v8       | 32.5 ms                                                  | 30.6 ms: 1.06x faster                                                   |
| Geometric mean | (ref)                                                    | 1.09x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|---------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads         | 2.67 sec                                                 | 2.43 sec: 1.10x faster                                                  |
| xml_etree_generate  | 118 ms                                                   | 110 ms: 1.08x faster                                                    |
| xml_etree_process   | 82.1 ms                                                  | 76.1 ms: 1.08x faster                                                   |
| xml_etree_iterparse | 159 ms                                                   | 148 ms: 1.08x faster                                                    |
| Geometric mean      | (ref)                                                    | 1.03x faster                                                            |

Benchmark hidden because not significant (5): unpickle_pure_python, xml_etree_parse, pickle_pure_python, json_dumps, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup | 16.0 ms                                                  | 15.2 ms: 1.06x faster                                                   |
| Geometric mean | (ref)                                                    | 1.03x faster                                                            |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text    | 28.6 ms                                                  | 26.7 ms: 1.07x faster                                                   |
| Geometric mean | (ref)                                                    | 1.02x faster                                                            |

Benchmark hidden because not significant (3): django_template, genshi_xml, mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mdp                        | 3.45 sec                                                 | 1.66 sec: 2.08x faster                                                  |
| deepcopy                   | 479 us                                                   | 318 us: 1.51x faster                                                    |
| deepcopy_memo              | 53.0 us                                                  | 35.7 us: 1.48x faster                                                   |
| async_tree_memoization_tg  | 663 ms                                                   | 449 ms: 1.48x faster                                                    |
| async_tree_memoization     | 664 ms                                                   | 455 ms: 1.46x faster                                                    |
| async_tree_none_tg         | 484 ms                                                   | 360 ms: 1.35x faster                                                    |
| async_tree_io              | 1.14 sec                                                 | 863 ms: 1.32x faster                                                    |
| async_tree_none            | 504 ms                                                   | 383 ms: 1.32x faster                                                    |
| async_tree_io_tg           | 1.16 sec                                                 | 894 ms: 1.30x faster                                                    |
| go                         | 164 ms                                                   | 130 ms: 1.27x faster                                                    |
| deepcopy_reduce            | 4.24 us                                                  | 3.36 us: 1.26x faster                                                   |
| spectral_norm              | 143 ms                                                   | 121 ms: 1.18x faster                                                    |
| async_generators           | 500 ms                                                   | 432 ms: 1.16x faster                                                    |
| scimark_sor                | 164 ms                                                   | 142 ms: 1.16x faster                                                    |
| generators                 | 40.3 ms                                                  | 35.2 ms: 1.14x faster                                                   |
| bpe_tokeniser              | 6.02 sec                                                 | 5.26 sec: 1.14x faster                                                  |
| scimark_fft                | 463 ms                                                   | 407 ms: 1.14x faster                                                    |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 711 ms: 1.13x faster                                                    |
| pathlib                    | 24.3 ms                                                  | 21.6 ms: 1.12x faster                                                   |
| telco                      | 10.5 ms                                                  | 9.36 ms: 1.12x faster                                                   |
| regex_compile              | 134 ms                                                   | 120 ms: 1.12x faster                                                    |
| scimark_monte_carlo        | 87.8 ms                                                  | 78.7 ms: 1.12x faster                                                   |
| richards                   | 54.5 ms                                                  | 49.0 ms: 1.11x faster                                                   |
| pyflate                    | 582 ms                                                   | 523 ms: 1.11x faster                                                    |
| float                      | 95.8 ms                                                  | 86.3 ms: 1.11x faster                                                   |
| regex_effbot               | 5.10 ms                                                  | 4.64 ms: 1.10x faster                                                   |
| pylint                     | 345 ms                                                   | 315 ms: 1.10x faster                                                    |
| tomli_loads                | 2.67 sec                                                 | 2.43 sec: 1.10x faster                                                  |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 721 ms: 1.10x faster                                                    |
| richards_super             | 60.8 ms                                                  | 55.6 ms: 1.09x faster                                                   |
| html5lib                   | 65.6 ms                                                  | 60.2 ms: 1.09x faster                                                   |
| xml_etree_generate         | 118 ms                                                   | 110 ms: 1.08x faster                                                    |
| xml_etree_process          | 82.1 ms                                                  | 76.1 ms: 1.08x faster                                                   |
| xml_etree_iterparse        | 159 ms                                                   | 148 ms: 1.08x faster                                                    |
| sympy_integrate            | 21.4 ms                                                  | 19.9 ms: 1.08x faster                                                   |
| k_core                     | 2.99 sec                                                 | 2.78 sec: 1.07x faster                                                  |
| pycparser                  | 1.34 sec                                                 | 1.25 sec: 1.07x faster                                                  |
| scimark_lu                 | 146 ms                                                   | 137 ms: 1.07x faster                                                    |
| genshi_text                | 28.6 ms                                                  | 26.7 ms: 1.07x faster                                                   |
| regex_dna                  | 263 ms                                                   | 247 ms: 1.07x faster                                                    |
| regex_v8                   | 32.5 ms                                                  | 30.6 ms: 1.06x faster                                                   |
| python_startup             | 16.0 ms                                                  | 15.2 ms: 1.06x faster                                                   |
| pprint_pformat             | 1.99 sec                                                 | 1.88 sec: 1.06x faster                                                  |
| deltablue                  | 3.97 ms                                                  | 3.76 ms: 1.05x faster                                                   |
| sqlite_synth               | 4.08 us                                                  | 3.88 us: 1.05x faster                                                   |
| nqueens                    | 105 ms                                                   | 101 ms: 1.04x faster                                                    |
| 2to3                       | 313 ms                                                   | 301 ms: 1.04x faster                                                    |
| pprint_safe_repr           | 962 ms                                                   | 926 ms: 1.04x faster                                                    |
| sphinx                     | 1.20 sec                                                 | 1.16 sec: 1.04x faster                                                  |
| docutils                   | 2.96 sec                                                 | 3.02 sec: 1.02x slower                                                  |
| shortest_path              | 565 ms                                                   | 578 ms: 1.02x slower                                                    |
| connected_components       | 547 ms                                                   | 561 ms: 1.03x slower                                                    |
| nbody                      | 118 ms                                                   | 129 ms: 1.09x slower                                                    |
| create_gc_cycles           | 3.39 ms                                                  | 3.85 ms: 1.13x slower                                                   |
| gc_traversal               | 5.92 ms                                                  | 6.73 ms: 1.14x slower                                                   |
| pidigits                   | 238 ms                                                   | 292 ms: 1.22x slower                                                    |
| subparsers                 | 20.3 ms                                                  | 27.7 ms: 1.36x slower                                                   |
| many_optionals             | 626 us                                                   | 881 us: 1.41x slower                                                    |
| logging_silent             | 135 ns                                                   | 631 ns: 4.69x slower                                                    |
| coverage                   | 106 ms                                                   | 534 ms: 5.06x slower                                                    |
| thrift                     | 1.01 ms                                                  | 192 ms: 189.53x slower                                                  |
| bench_mp_pool              | 8.07 ms                                                  | 3.51 sec: 434.45x slower                                                |
| Geometric mean             | (ref)                                                    | 1.10x slower                                                            |

Benchmark hidden because not significant (27): sympy_sum, chaos, unpickle_pure_python, sympy_expand, hexiom, comprehensions, coroutines, typing_runtime_protocols, asyncio_websockets, django_template, bench_thread_pool, meteor_contest, json, crypto_pyaes, genshi_xml, python_startup_no_site, logging_format, sympy_str, mako, xml_etree_parse, scimark_sparse_mat_mult, fannkuch, pickle_pure_python, logging_simple, raytrace, json_dumps, json_loads
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (13) of results/bm-20250510-3.15.0a0-1a87b6e-CLANG/bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.021x slower

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.09x