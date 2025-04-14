# Results vs. 3.13.0

- fork: python
- ref: e82c2ca2a59235bc1965
- machine: linux-aarch64
- commit hash: e82c2ca
- commit date: 2025-03-15
- overall geometric mean: 1.013x faster
- HPT reliability: 65.46%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| docutils       | 2.96 sec                                                 | 3.14 sec: 1.06x slower                                                   |
| html5lib       | 65.6 ms                                                  | 63.3 ms: 1.04x faster                                                    |
| Geometric mean | (ref)                                                    | 1.00x faster                                                             |

Benchmark hidden because not significant (2): 2to3, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 475 ms: 1.40x faster                                                     |
| async_tree_memoization     | 664 ms                                                   | 480 ms: 1.38x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 375 ms: 1.29x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 887 ms: 1.28x faster                                                     |
| async_tree_none            | 504 ms                                                   | 394 ms: 1.28x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 929 ms: 1.25x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 652 ms: 1.23x faster                                                     |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 669 ms: 1.18x faster                                                     |
| async_generators           | 500 ms                                                   | 474 ms: 1.06x faster                                                     |
| Geometric mean             | (ref)                                                    | 1.21x faster                                                             |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 85.2 ms: 1.12x faster                                                    |
| nbody          | 118 ms                                                   | 132 ms: 1.11x slower                                                     |
| Geometric mean | (ref)                                                    | 1.01x faster                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 3.92 ms: 1.30x faster                                                    |
| regex_v8       | 32.5 ms                                                  | 28.7 ms: 1.13x faster                                                    |
| regex_dna      | 263 ms                                                   | 239 ms: 1.10x faster                                                     |
| Geometric mean | (ref)                                                    | 1.14x faster                                                             |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse      | 203 ms                                                   | 178 ms: 1.14x faster                                                     |
| xml_etree_iterparse  | 159 ms                                                   | 143 ms: 1.11x faster                                                     |
| tomli_loads          | 2.67 sec                                                 | 2.45 sec: 1.09x faster                                                   |
| xml_etree_process    | 82.1 ms                                                  | 77.9 ms: 1.05x faster                                                    |
| pickle_pure_python   | 374 us                                                   | 404 us: 1.08x slower                                                     |
| unpickle_pure_python | 265 us                                                   | 292 us: 1.10x slower                                                     |
| Geometric mean       | (ref)                                                    | 1.03x faster                                                             |

Benchmark hidden because not significant (3): xml_etree_generate, json_dumps, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.79 ms                                                  | 10.2 ms: 1.16x slower                                                    |
| Geometric mean         | (ref)                                                    | 1.08x slower                                                             |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text    | 28.6 ms                                                  | 26.9 ms: 1.06x faster                                                    |
| Geometric mean | (ref)                                                    | 1.01x faster                                                             |

Benchmark hidden because not significant (3): mako, django_template, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| deepcopy                   | 479 us                                                   | 338 us: 1.42x faster                                                     |
| deepcopy_memo              | 53.0 us                                                  | 37.4 us: 1.42x faster                                                    |
| async_tree_memoization_tg  | 663 ms                                                   | 475 ms: 1.40x faster                                                     |
| async_tree_memoization     | 664 ms                                                   | 480 ms: 1.38x faster                                                     |
| regex_effbot               | 5.10 ms                                                  | 3.92 ms: 1.30x faster                                                    |
| async_tree_none_tg         | 484 ms                                                   | 375 ms: 1.29x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 887 ms: 1.28x faster                                                     |
| async_tree_none            | 504 ms                                                   | 394 ms: 1.28x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 929 ms: 1.25x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 652 ms: 1.23x faster                                                     |
| deepcopy_reduce            | 4.24 us                                                  | 3.51 us: 1.21x faster                                                    |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 669 ms: 1.18x faster                                                     |
| xml_etree_parse            | 203 ms                                                   | 178 ms: 1.14x faster                                                     |
| regex_v8                   | 32.5 ms                                                  | 28.7 ms: 1.13x faster                                                    |
| float                      | 95.8 ms                                                  | 85.2 ms: 1.12x faster                                                    |
| xml_etree_iterparse        | 159 ms                                                   | 143 ms: 1.11x faster                                                     |
| regex_dna                  | 263 ms                                                   | 239 ms: 1.10x faster                                                     |
| scimark_sor                | 164 ms                                                   | 150 ms: 1.10x faster                                                     |
| tomli_loads                | 2.67 sec                                                 | 2.45 sec: 1.09x faster                                                   |
| sqlite_synth               | 4.08 us                                                  | 3.75 us: 1.09x faster                                                    |
| generators                 | 40.3 ms                                                  | 37.3 ms: 1.08x faster                                                    |
| coverage                   | 106 ms                                                   | 98.1 ms: 1.08x faster                                                    |
| richards_super             | 60.8 ms                                                  | 56.5 ms: 1.08x faster                                                    |
| thrift                     | 1.01 ms                                                  | 942 us: 1.07x faster                                                     |
| pylint                     | 345 ms                                                   | 322 ms: 1.07x faster                                                     |
| richards                   | 54.5 ms                                                  | 50.8 ms: 1.07x faster                                                    |
| bpe_tokeniser              | 6.02 sec                                                 | 5.65 sec: 1.06x faster                                                   |
| spectral_norm              | 143 ms                                                   | 135 ms: 1.06x faster                                                     |
| pathlib                    | 24.3 ms                                                  | 22.9 ms: 1.06x faster                                                    |
| genshi_text                | 28.6 ms                                                  | 26.9 ms: 1.06x faster                                                    |
| async_generators           | 500 ms                                                   | 474 ms: 1.06x faster                                                     |
| telco                      | 10.5 ms                                                  | 9.91 ms: 1.05x faster                                                    |
| xml_etree_process          | 82.1 ms                                                  | 77.9 ms: 1.05x faster                                                    |
| scimark_fft                | 463 ms                                                   | 440 ms: 1.05x faster                                                     |
| logging_format             | 8.10 us                                                  | 7.73 us: 1.05x faster                                                    |
| k_core                     | 2.99 sec                                                 | 2.87 sec: 1.04x faster                                                   |
| mdp                        | 3.45 sec                                                 | 3.31 sec: 1.04x faster                                                   |
| html5lib                   | 65.6 ms                                                  | 63.3 ms: 1.04x faster                                                    |
| connected_components       | 547 ms                                                   | 565 ms: 1.03x slower                                                     |
| deltablue                  | 3.97 ms                                                  | 4.13 ms: 1.04x slower                                                    |
| pycparser                  | 1.34 sec                                                 | 1.40 sec: 1.04x slower                                                   |
| shortest_path              | 565 ms                                                   | 591 ms: 1.05x slower                                                     |
| create_gc_cycles           | 3.39 ms                                                  | 3.60 ms: 1.06x slower                                                    |
| docutils                   | 2.96 sec                                                 | 3.14 sec: 1.06x slower                                                   |
| scimark_lu                 | 146 ms                                                   | 155 ms: 1.06x slower                                                     |
| sympy_str                  | 265 ms                                                   | 282 ms: 1.06x slower                                                     |
| scimark_sparse_mat_mult    | 6.66 ms                                                  | 7.08 ms: 1.06x slower                                                    |
| sympy_expand               | 472 ms                                                   | 505 ms: 1.07x slower                                                     |
| raytrace                   | 310 ms                                                   | 334 ms: 1.08x slower                                                     |
| meteor_contest             | 117 ms                                                   | 126 ms: 1.08x slower                                                     |
| pickle_pure_python         | 374 us                                                   | 404 us: 1.08x slower                                                     |
| typing_runtime_protocols   | 197 us                                                   | 216 us: 1.10x slower                                                     |
| go                         | 164 ms                                                   | 181 ms: 1.10x slower                                                     |
| unpickle_pure_python       | 265 us                                                   | 292 us: 1.10x slower                                                     |
| fannkuch                   | 478 ms                                                   | 529 ms: 1.11x slower                                                     |
| nbody                      | 118 ms                                                   | 132 ms: 1.11x slower                                                     |
| gc_traversal               | 5.92 ms                                                  | 6.81 ms: 1.15x slower                                                    |
| python_startup_no_site     | 8.79 ms                                                  | 10.2 ms: 1.16x slower                                                    |
| hexiom                     | 7.34 ms                                                  | 8.58 ms: 1.17x slower                                                    |
| crypto_pyaes               | 84.9 ms                                                  | 101 ms: 1.19x slower                                                     |
| comprehensions             | 20.8 us                                                  | 25.6 us: 1.23x slower                                                    |
| subparsers                 | 20.3 ms                                                  | 25.7 ms: 1.26x slower                                                    |
| pprint_pformat             | 1.99 sec                                                 | 2.56 sec: 1.29x slower                                                   |
| pprint_safe_repr           | 962 ms                                                   | 1.24 sec: 1.29x slower                                                   |
| many_optionals             | 626 us                                                   | 872 us: 1.39x slower                                                     |
| bench_mp_pool              | 8.07 ms                                                  | 1.36 sec: 169.04x slower                                                 |
| Geometric mean             | (ref)                                                    | 1.04x slower                                                             |

Benchmark hidden because not significant (25): xml_etree_generate, regex_compile, json_dumps, logging_simple, logging_silent, sphinx, pidigits, 2to3, json, asyncio_websockets, coroutines, sqlalchemy_declarative, mako, django_template, sqlalchemy_imperative, python_startup, scimark_monte_carlo, genshi_xml, chaos, sympy_integrate, pyflate, sympy_sum, nqueens, bench_thread_pool, json_loads
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (13) of results/bm-20250315-3.14.0a6+-e82c2ca-JIT/bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.013x faster

# HPT report

- Reliability score: 65.46% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.05x