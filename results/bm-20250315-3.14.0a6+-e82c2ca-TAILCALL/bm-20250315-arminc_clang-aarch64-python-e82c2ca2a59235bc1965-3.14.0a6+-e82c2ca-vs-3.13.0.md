# Results vs. 3.13.0

- fork: python
- ref: e82c2ca2a59235bc1965
- machine: linux-aarch64
- commit hash: e82c2ca
- commit date: 2025-03-15
- overall geometric mean: 1.063x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 291 ms: 1.08x faster                                                     |
| docutils       | 2.96 sec                                                 | 2.91 sec: 1.02x faster                                                   |
| html5lib       | 65.6 ms                                                  | 59.5 ms: 1.10x faster                                                    |
| sphinx         | 1.20 sec                                                 | 1.12 sec: 1.08x faster                                                   |
| Geometric mean | (ref)                                                    | 1.07x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 458 ms: 1.45x faster                                                     |
| async_tree_memoization     | 664 ms                                                   | 466 ms: 1.42x faster                                                     |
| async_tree_none            | 504 ms                                                   | 376 ms: 1.34x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 366 ms: 1.33x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 889 ms: 1.31x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 876 ms: 1.30x faster                                                     |
| async_generators           | 500 ms                                                   | 416 ms: 1.20x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 709 ms: 1.13x faster                                                     |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 725 ms: 1.09x faster                                                     |
| Geometric mean             | (ref)                                                    | 1.23x faster                                                             |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 85.3 ms: 1.12x faster                                                    |
| pidigits       | 238 ms                                                   | 291 ms: 1.22x slower                                                     |
| Geometric mean | (ref)                                                    | 1.03x slower                                                             |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 4.21 ms: 1.21x faster                                                    |
| regex_dna      | 263 ms                                                   | 233 ms: 1.13x faster                                                     |
| regex_compile  | 134 ms                                                   | 123 ms: 1.08x faster                                                     |
| regex_v8       | 32.5 ms                                                  | 30.3 ms: 1.07x faster                                                    |
| Geometric mean | (ref)                                                    | 1.12x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|---------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_generate  | 118 ms                                                   | 104 ms: 1.14x faster                                                     |
| tomli_loads         | 2.67 sec                                                 | 2.37 sec: 1.12x faster                                                   |
| xml_etree_process   | 82.1 ms                                                  | 74.1 ms: 1.11x faster                                                    |
| xml_etree_iterparse | 159 ms                                                   | 151 ms: 1.05x faster                                                     |
| Geometric mean      | (ref)                                                    | 1.04x faster                                                             |

Benchmark hidden because not significant (5): json_dumps, unpickle_pure_python, json_loads, xml_etree_parse, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.79 ms                                                  | 10.1 ms: 1.15x slower                                                    |
| Geometric mean         | (ref)                                                    | 1.08x slower                                                             |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text    | 28.6 ms                                                  | 25.9 ms: 1.10x faster                                                    |
| genshi_xml     | 61.6 ms                                                  | 58.1 ms: 1.06x faster                                                    |
| Geometric mean | (ref)                                                    | 1.04x faster                                                             |

Benchmark hidden because not significant (2): django_template, mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| deepcopy                   | 479 us                                                   | 312 us: 1.54x faster                                                     |
| deepcopy_memo              | 53.0 us                                                  | 35.6 us: 1.49x faster                                                    |
| async_tree_memoization_tg  | 663 ms                                                   | 458 ms: 1.45x faster                                                     |
| async_tree_memoization     | 664 ms                                                   | 466 ms: 1.42x faster                                                     |
| async_tree_none            | 504 ms                                                   | 376 ms: 1.34x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 366 ms: 1.33x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 889 ms: 1.31x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 876 ms: 1.30x faster                                                     |
| deepcopy_reduce            | 4.24 us                                                  | 3.36 us: 1.26x faster                                                    |
| spectral_norm              | 143 ms                                                   | 114 ms: 1.26x faster                                                     |
| regex_effbot               | 5.10 ms                                                  | 4.21 ms: 1.21x faster                                                    |
| go                         | 164 ms                                                   | 136 ms: 1.20x faster                                                     |
| async_generators           | 500 ms                                                   | 416 ms: 1.20x faster                                                     |
| scimark_fft                | 463 ms                                                   | 388 ms: 1.19x faster                                                     |
| pathlib                    | 24.3 ms                                                  | 21.2 ms: 1.15x faster                                                    |
| scimark_sor                | 164 ms                                                   | 143 ms: 1.15x faster                                                     |
| xml_etree_generate         | 118 ms                                                   | 104 ms: 1.14x faster                                                     |
| pylint                     | 345 ms                                                   | 303 ms: 1.14x faster                                                     |
| telco                      | 10.5 ms                                                  | 9.22 ms: 1.13x faster                                                    |
| coverage                   | 106 ms                                                   | 93.3 ms: 1.13x faster                                                    |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 709 ms: 1.13x faster                                                     |
| regex_dna                  | 263 ms                                                   | 233 ms: 1.13x faster                                                     |
| scimark_monte_carlo        | 87.8 ms                                                  | 78.0 ms: 1.13x faster                                                    |
| tomli_loads                | 2.67 sec                                                 | 2.37 sec: 1.12x faster                                                   |
| float                      | 95.8 ms                                                  | 85.3 ms: 1.12x faster                                                    |
| generators                 | 40.3 ms                                                  | 36.1 ms: 1.12x faster                                                    |
| logging_silent             | 135 ns                                                   | 121 ns: 1.12x faster                                                     |
| xml_etree_process          | 82.1 ms                                                  | 74.1 ms: 1.11x faster                                                    |
| bpe_tokeniser              | 6.02 sec                                                 | 5.45 sec: 1.10x faster                                                   |
| pyflate                    | 582 ms                                                   | 528 ms: 1.10x faster                                                     |
| html5lib                   | 65.6 ms                                                  | 59.5 ms: 1.10x faster                                                    |
| genshi_text                | 28.6 ms                                                  | 25.9 ms: 1.10x faster                                                    |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 725 ms: 1.09x faster                                                     |
| k_core                     | 2.99 sec                                                 | 2.75 sec: 1.09x faster                                                   |
| regex_compile              | 134 ms                                                   | 123 ms: 1.08x faster                                                     |
| richards_super             | 60.8 ms                                                  | 56.1 ms: 1.08x faster                                                    |
| pycparser                  | 1.34 sec                                                 | 1.24 sec: 1.08x faster                                                   |
| sqlalchemy_declarative     | 154 ms                                                   | 143 ms: 1.08x faster                                                     |
| 2to3                       | 313 ms                                                   | 291 ms: 1.08x faster                                                     |
| sphinx                     | 1.20 sec                                                 | 1.12 sec: 1.08x faster                                                   |
| regex_v8                   | 32.5 ms                                                  | 30.3 ms: 1.07x faster                                                    |
| richards                   | 54.5 ms                                                  | 50.9 ms: 1.07x faster                                                    |
| mdp                        | 3.45 sec                                                 | 3.22 sec: 1.07x faster                                                   |
| chaos                      | 70.7 ms                                                  | 66.2 ms: 1.07x faster                                                    |
| scimark_lu                 | 146 ms                                                   | 137 ms: 1.07x faster                                                     |
| sqlite_synth               | 4.08 us                                                  | 3.83 us: 1.07x faster                                                    |
| thrift                     | 1.01 ms                                                  | 949 us: 1.07x faster                                                     |
| scimark_sparse_mat_mult    | 6.66 ms                                                  | 6.25 ms: 1.06x faster                                                    |
| genshi_xml                 | 61.6 ms                                                  | 58.1 ms: 1.06x faster                                                    |
| pprint_pformat             | 1.99 sec                                                 | 1.88 sec: 1.06x faster                                                   |
| pprint_safe_repr           | 962 ms                                                   | 910 ms: 1.06x faster                                                     |
| logging_format             | 8.10 us                                                  | 7.67 us: 1.06x faster                                                    |
| xml_etree_iterparse        | 159 ms                                                   | 151 ms: 1.05x faster                                                     |
| sympy_expand               | 472 ms                                                   | 455 ms: 1.04x faster                                                     |
| logging_simple             | 7.25 us                                                  | 7.00 us: 1.04x faster                                                    |
| typing_runtime_protocols   | 197 us                                                   | 191 us: 1.03x faster                                                     |
| sympy_str                  | 265 ms                                                   | 257 ms: 1.03x faster                                                     |
| docutils                   | 2.96 sec                                                 | 2.91 sec: 1.02x faster                                                   |
| shortest_path              | 565 ms                                                   | 575 ms: 1.02x slower                                                     |
| connected_components       | 547 ms                                                   | 559 ms: 1.02x slower                                                     |
| fannkuch                   | 478 ms                                                   | 502 ms: 1.05x slower                                                     |
| crypto_pyaes               | 84.9 ms                                                  | 90.1 ms: 1.06x slower                                                    |
| create_gc_cycles           | 3.39 ms                                                  | 3.65 ms: 1.07x slower                                                    |
| gc_traversal               | 5.92 ms                                                  | 6.52 ms: 1.10x slower                                                    |
| python_startup_no_site     | 8.79 ms                                                  | 10.1 ms: 1.15x slower                                                    |
| pidigits                   | 238 ms                                                   | 291 ms: 1.22x slower                                                     |
| subparsers                 | 20.3 ms                                                  | 25.8 ms: 1.27x slower                                                    |
| many_optionals             | 626 us                                                   | 843 us: 1.35x slower                                                     |
| bench_mp_pool              | 8.07 ms                                                  | 2.37 sec: 293.85x slower                                                 |
| Geometric mean             | (ref)                                                    | 1.01x faster                                                             |

Benchmark hidden because not significant (22): sympy_sum, nqueens, comprehensions, sympy_integrate, json, json_dumps, bench_thread_pool, deltablue, hexiom, unpickle_pure_python, django_template, asyncio_websockets, mako, meteor_contest, coroutines, nbody, python_startup, raytrace, sqlalchemy_imperative, json_loads, xml_etree_parse, pickle_pure_python
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (13) of results/bm-20250315-3.14.0a6+-e82c2ca-CLANG/bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.063x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.06x