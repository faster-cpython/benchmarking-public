# Results vs. 3.13.0

- fork: python
- ref: 29f8a67ae00081a36fdc
- machine: linux-aarch64
- commit hash: 29f8a67
- commit date: 2025-02-08
- overall geometric mean: 1.004x faster
- HPT reliability: 79.48%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| docutils       | 2.96 sec                                                 | 3.27 sec: 1.10x slower                                                   |
| Geometric mean | (ref)                                                    | 1.02x slower                                                             |

Benchmark hidden because not significant (3): 2to3, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 496 ms: 1.34x faster                                                     |
| async_tree_memoization     | 664 ms                                                   | 505 ms: 1.31x faster                                                     |
| async_tree_none            | 504 ms                                                   | 402 ms: 1.25x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 955 ms: 1.22x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 397 ms: 1.22x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 958 ms: 1.19x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 683 ms: 1.17x faster                                                     |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 698 ms: 1.13x faster                                                     |
| async_generators           | 500 ms                                                   | 483 ms: 1.04x faster                                                     |
| Geometric mean             | (ref)                                                    | 1.17x faster                                                             |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 84.1 ms: 1.14x faster                                                    |
| nbody          | 118 ms                                                   | 129 ms: 1.09x slower                                                     |
| Geometric mean | (ref)                                                    | 1.01x faster                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 4.06 ms: 1.26x faster                                                    |
| regex_dna      | 263 ms                                                   | 250 ms: 1.05x faster                                                     |
| Geometric mean | (ref)                                                    | 1.08x faster                                                             |

Benchmark hidden because not significant (2): regex_v8, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|---------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse     | 203 ms                                                   | 183 ms: 1.11x faster                                                     |
| xml_etree_iterparse | 159 ms                                                   | 147 ms: 1.08x faster                                                     |
| xml_etree_generate  | 118 ms                                                   | 111 ms: 1.07x faster                                                     |
| tomli_loads         | 2.67 sec                                                 | 2.52 sec: 1.06x faster                                                   |
| json_loads          | 32.8 us                                                  | 35.8 us: 1.09x slower                                                    |
| pickle_pure_python  | 374 us                                                   | 415 us: 1.11x slower                                                     |
| Geometric mean      | (ref)                                                    | 1.01x faster                                                             |

Benchmark hidden because not significant (3): xml_etree_process, unpickle_pure_python, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.79 ms                                                  | 9.00 ms: 1.02x slower                                                    |
| Geometric mean         | (ref)                                                    | 1.02x slower                                                             |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_xml     | 61.6 ms                                                  | 65.1 ms: 1.06x slower                                                    |
| Geometric mean | (ref)                                                    | 1.02x slower                                                             |

Benchmark hidden because not significant (3): mako, genshi_text, django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| deepcopy                   | 479 us                                                   | 353 us: 1.36x faster                                                     |
| async_tree_memoization_tg  | 663 ms                                                   | 496 ms: 1.34x faster                                                     |
| deepcopy_memo              | 53.0 us                                                  | 40.1 us: 1.32x faster                                                    |
| async_tree_memoization     | 664 ms                                                   | 505 ms: 1.31x faster                                                     |
| regex_effbot               | 5.10 ms                                                  | 4.06 ms: 1.26x faster                                                    |
| async_tree_none            | 504 ms                                                   | 402 ms: 1.25x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 955 ms: 1.22x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 397 ms: 1.22x faster                                                     |
| spectral_norm              | 143 ms                                                   | 119 ms: 1.21x faster                                                     |
| deepcopy_reduce            | 4.24 us                                                  | 3.56 us: 1.19x faster                                                    |
| async_tree_io              | 1.14 sec                                                 | 958 ms: 1.19x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 683 ms: 1.17x faster                                                     |
| float                      | 95.8 ms                                                  | 84.1 ms: 1.14x faster                                                    |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 698 ms: 1.13x faster                                                     |
| xml_etree_parse            | 203 ms                                                   | 183 ms: 1.11x faster                                                     |
| scimark_fft                | 463 ms                                                   | 423 ms: 1.09x faster                                                     |
| generators                 | 40.3 ms                                                  | 37.1 ms: 1.09x faster                                                    |
| xml_etree_iterparse        | 159 ms                                                   | 147 ms: 1.08x faster                                                     |
| pathlib                    | 24.3 ms                                                  | 22.6 ms: 1.08x faster                                                    |
| coverage                   | 106 ms                                                   | 98.1 ms: 1.08x faster                                                    |
| xml_etree_generate         | 118 ms                                                   | 111 ms: 1.07x faster                                                     |
| scimark_lu                 | 146 ms                                                   | 138 ms: 1.06x faster                                                     |
| tomli_loads                | 2.67 sec                                                 | 2.52 sec: 1.06x faster                                                   |
| scimark_sor                | 164 ms                                                   | 155 ms: 1.06x faster                                                     |
| regex_dna                  | 263 ms                                                   | 250 ms: 1.05x faster                                                     |
| bpe_tokeniser              | 6.02 sec                                                 | 5.73 sec: 1.05x faster                                                   |
| async_generators           | 500 ms                                                   | 483 ms: 1.04x faster                                                     |
| k_core                     | 2.99 sec                                                 | 2.92 sec: 1.03x faster                                                   |
| python_startup_no_site     | 8.79 ms                                                  | 9.00 ms: 1.02x slower                                                    |
| mdp                        | 3.45 sec                                                 | 3.55 sec: 1.03x slower                                                   |
| shortest_path              | 565 ms                                                   | 589 ms: 1.04x slower                                                     |
| create_gc_cycles           | 3.39 ms                                                  | 3.54 ms: 1.04x slower                                                    |
| genshi_xml                 | 61.6 ms                                                  | 65.1 ms: 1.06x slower                                                    |
| sympy_expand               | 472 ms                                                   | 503 ms: 1.07x slower                                                     |
| pycparser                  | 1.34 sec                                                 | 1.44 sec: 1.07x slower                                                   |
| deltablue                  | 3.97 ms                                                  | 4.27 ms: 1.08x slower                                                    |
| meteor_contest             | 117 ms                                                   | 126 ms: 1.08x slower                                                     |
| raytrace                   | 310 ms                                                   | 335 ms: 1.08x slower                                                     |
| sqlglot_parse              | 1.43 ms                                                  | 1.55 ms: 1.08x slower                                                    |
| sympy_str                  | 265 ms                                                   | 288 ms: 1.09x slower                                                     |
| typing_runtime_protocols   | 197 us                                                   | 215 us: 1.09x slower                                                     |
| json_loads                 | 32.8 us                                                  | 35.8 us: 1.09x slower                                                    |
| nbody                      | 118 ms                                                   | 129 ms: 1.09x slower                                                     |
| docutils                   | 2.96 sec                                                 | 3.27 sec: 1.10x slower                                                   |
| pickle_pure_python         | 374 us                                                   | 415 us: 1.11x slower                                                     |
| crypto_pyaes               | 84.9 ms                                                  | 95.2 ms: 1.12x slower                                                    |
| fannkuch                   | 478 ms                                                   | 543 ms: 1.14x slower                                                     |
| gc_traversal               | 5.92 ms                                                  | 6.75 ms: 1.14x slower                                                    |
| comprehensions             | 20.8 us                                                  | 24.6 us: 1.18x slower                                                    |
| nqueens                    | 105 ms                                                   | 126 ms: 1.20x slower                                                     |
| hexiom                     | 7.34 ms                                                  | 9.10 ms: 1.24x slower                                                    |
| pprint_pformat             | 1.99 sec                                                 | 2.70 sec: 1.36x slower                                                   |
| pprint_safe_repr           | 962 ms                                                   | 1.31 sec: 1.36x slower                                                   |
| subparsers                 | 20.3 ms                                                  | 28.0 ms: 1.37x slower                                                    |
| many_optionals             | 626 us                                                   | 871 us: 1.39x slower                                                     |
| bench_mp_pool              | 8.07 ms                                                  | 2.46 sec: 304.89x slower                                                 |
| Geometric mean             | (ref)                                                    | 1.06x slower                                                             |

Benchmark hidden because not significant (39): thrift, telco, pylint, scimark_monte_carlo, html5lib, sqlite_synth, logging_format, xml_etree_process, regex_v8, richards, mako, regex_compile, logging_silent, asyncio_websockets, sphinx, coroutines, connected_components, chaos, sqlalchemy_declarative, genshi_text, pyflate, logging_simple, sqlglot_optimize, richards_super, pidigits, django_template, 2to3, go, python_startup, sqlglot_normalize, scimark_sparse_mat_mult, unpickle_pure_python, sqlglot_transpile, bench_thread_pool, sympy_sum, json_dumps, json, sympy_integrate, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (9) of results/bm-20250208-3.14.0a4+-29f8a67-JIT/bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.004x faster

# HPT report

- Reliability score: 79.48% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x