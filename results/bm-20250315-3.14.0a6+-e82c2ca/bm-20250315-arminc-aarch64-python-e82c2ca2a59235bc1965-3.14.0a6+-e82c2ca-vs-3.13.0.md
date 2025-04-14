# Results vs. 3.13.0

- fork: python
- ref: e82c2ca2a59235bc1965
- machine: linux-aarch64
- commit hash: e82c2ca
- commit date: 2025-03-15
- overall geometric mean: 1.045x faster
- HPT reliability: 99.97%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 296 ms: 1.06x faster                                                     |
| html5lib       | 65.6 ms                                                  | 64.3 ms: 1.02x faster                                                    |
| sphinx         | 1.20 sec                                                 | 1.14 sec: 1.05x faster                                                   |
| Geometric mean | (ref)                                                    | 1.03x faster                                                             |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 470 ms: 1.41x faster                                                     |
| async_tree_memoization     | 664 ms                                                   | 477 ms: 1.39x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 371 ms: 1.31x faster                                                     |
| async_tree_none            | 504 ms                                                   | 388 ms: 1.30x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 885 ms: 1.29x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 911 ms: 1.28x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 650 ms: 1.23x faster                                                     |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 663 ms: 1.19x faster                                                     |
| async_generators           | 500 ms                                                   | 451 ms: 1.11x faster                                                     |
| Geometric mean             | (ref)                                                    | 1.22x faster                                                             |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 87.7 ms: 1.09x faster                                                    |
| nbody          | 118 ms                                                   | 128 ms: 1.08x slower                                                     |
| Geometric mean | (ref)                                                    | 1.01x faster                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 3.89 ms: 1.31x faster                                                    |
| regex_v8       | 32.5 ms                                                  | 29.4 ms: 1.11x faster                                                    |
| regex_dna      | 263 ms                                                   | 243 ms: 1.08x faster                                                     |
| Geometric mean | (ref)                                                    | 1.13x faster                                                             |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|---------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse     | 203 ms                                                   | 178 ms: 1.14x faster                                                     |
| xml_etree_iterparse | 159 ms                                                   | 141 ms: 1.13x faster                                                     |
| tomli_loads         | 2.67 sec                                                 | 2.50 sec: 1.07x faster                                                   |
| Geometric mean      | (ref)                                                    | 1.04x faster                                                             |

Benchmark hidden because not significant (6): json_dumps, xml_etree_generate, xml_etree_process, unpickle_pure_python, pickle_pure_python, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.79 ms                                                  | 10.2 ms: 1.15x slower                                                    |
| Geometric mean         | (ref)                                                    | 1.08x slower                                                             |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|-----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text     | 28.6 ms                                                  | 26.7 ms: 1.07x faster                                                    |
| django_template | 39.4 ms                                                  | 40.5 ms: 1.03x slower                                                    |
| Geometric mean  | (ref)                                                    | 1.01x faster                                                             |

Benchmark hidden because not significant (2): genshi_xml, mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| deepcopy                   | 479 us                                                   | 333 us: 1.44x faster                                                     |
| async_tree_memoization_tg  | 663 ms                                                   | 470 ms: 1.41x faster                                                     |
| deepcopy_memo              | 53.0 us                                                  | 37.9 us: 1.40x faster                                                    |
| async_tree_memoization     | 664 ms                                                   | 477 ms: 1.39x faster                                                     |
| regex_effbot               | 5.10 ms                                                  | 3.89 ms: 1.31x faster                                                    |
| async_tree_none_tg         | 484 ms                                                   | 371 ms: 1.31x faster                                                     |
| async_tree_none            | 504 ms                                                   | 388 ms: 1.30x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 885 ms: 1.29x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 911 ms: 1.28x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 650 ms: 1.23x faster                                                     |
| deepcopy_reduce            | 4.24 us                                                  | 3.56 us: 1.19x faster                                                    |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 663 ms: 1.19x faster                                                     |
| spectral_norm              | 143 ms                                                   | 122 ms: 1.17x faster                                                     |
| go                         | 164 ms                                                   | 144 ms: 1.14x faster                                                     |
| xml_etree_parse            | 203 ms                                                   | 178 ms: 1.14x faster                                                     |
| xml_etree_iterparse        | 159 ms                                                   | 141 ms: 1.13x faster                                                     |
| async_generators           | 500 ms                                                   | 451 ms: 1.11x faster                                                     |
| pylint                     | 345 ms                                                   | 312 ms: 1.11x faster                                                     |
| pathlib                    | 24.3 ms                                                  | 22.0 ms: 1.11x faster                                                    |
| regex_v8                   | 32.5 ms                                                  | 29.4 ms: 1.11x faster                                                    |
| generators                 | 40.3 ms                                                  | 36.5 ms: 1.10x faster                                                    |
| telco                      | 10.5 ms                                                  | 9.49 ms: 1.10x faster                                                    |
| float                      | 95.8 ms                                                  | 87.7 ms: 1.09x faster                                                    |
| scimark_sor                | 164 ms                                                   | 150 ms: 1.09x faster                                                     |
| regex_dna                  | 263 ms                                                   | 243 ms: 1.08x faster                                                     |
| scimark_fft                | 463 ms                                                   | 430 ms: 1.07x faster                                                     |
| genshi_text                | 28.6 ms                                                  | 26.7 ms: 1.07x faster                                                    |
| sqlite_synth               | 4.08 us                                                  | 3.82 us: 1.07x faster                                                    |
| tomli_loads                | 2.67 sec                                                 | 2.50 sec: 1.07x faster                                                   |
| logging_format             | 8.10 us                                                  | 7.60 us: 1.07x faster                                                    |
| bpe_tokeniser              | 6.02 sec                                                 | 5.65 sec: 1.07x faster                                                   |
| k_core                     | 2.99 sec                                                 | 2.81 sec: 1.07x faster                                                   |
| thrift                     | 1.01 ms                                                  | 949 us: 1.06x faster                                                     |
| sqlalchemy_declarative     | 154 ms                                                   | 145 ms: 1.06x faster                                                     |
| pycparser                  | 1.34 sec                                                 | 1.27 sec: 1.06x faster                                                   |
| 2to3                       | 313 ms                                                   | 296 ms: 1.06x faster                                                     |
| coverage                   | 106 ms                                                   | 100 ms: 1.05x faster                                                     |
| sphinx                     | 1.20 sec                                                 | 1.14 sec: 1.05x faster                                                   |
| logging_simple             | 7.25 us                                                  | 6.95 us: 1.04x faster                                                    |
| mdp                        | 3.45 sec                                                 | 3.32 sec: 1.04x faster                                                   |
| pprint_pformat             | 1.99 sec                                                 | 1.92 sec: 1.03x faster                                                   |
| richards_super             | 60.8 ms                                                  | 58.9 ms: 1.03x faster                                                    |
| html5lib                   | 65.6 ms                                                  | 64.3 ms: 1.02x faster                                                    |
| shortest_path              | 565 ms                                                   | 577 ms: 1.02x slower                                                     |
| connected_components       | 547 ms                                                   | 560 ms: 1.02x slower                                                     |
| django_template            | 39.4 ms                                                  | 40.5 ms: 1.03x slower                                                    |
| raytrace                   | 310 ms                                                   | 322 ms: 1.04x slower                                                     |
| create_gc_cycles           | 3.39 ms                                                  | 3.54 ms: 1.04x slower                                                    |
| sympy_str                  | 265 ms                                                   | 277 ms: 1.04x slower                                                     |
| fannkuch                   | 478 ms                                                   | 502 ms: 1.05x slower                                                     |
| nbody                      | 118 ms                                                   | 128 ms: 1.08x slower                                                     |
| gc_traversal               | 5.92 ms                                                  | 6.64 ms: 1.12x slower                                                    |
| python_startup_no_site     | 8.79 ms                                                  | 10.2 ms: 1.15x slower                                                    |
| subparsers                 | 20.3 ms                                                  | 25.8 ms: 1.27x slower                                                    |
| many_optionals             | 626 us                                                   | 833 us: 1.33x slower                                                     |
| bench_mp_pool              | 8.07 ms                                                  | 2.92 sec: 361.70x slower                                                 |
| Geometric mean             | (ref)                                                    | 1.01x slower                                                             |

Benchmark hidden because not significant (35): sympy_sum, regex_compile, scimark_monte_carlo, json_dumps, sqlalchemy_imperative, xml_etree_generate, richards, xml_etree_process, pyflate, scimark_sparse_mat_mult, pidigits, json, asyncio_websockets, pprint_safe_repr, logging_silent, sympy_integrate, genshi_xml, bench_thread_pool, deltablue, sympy_expand, python_startup, nqueens, meteor_contest, chaos, typing_runtime_protocols, docutils, coroutines, unpickle_pure_python, comprehensions, scimark_lu, hexiom, mako, crypto_pyaes, pickle_pure_python, json_loads
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (13) of results/bm-20250315-3.14.0a6+-e82c2ca/bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.045x faster

# HPT report

- Reliability score: 99.97% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.03x