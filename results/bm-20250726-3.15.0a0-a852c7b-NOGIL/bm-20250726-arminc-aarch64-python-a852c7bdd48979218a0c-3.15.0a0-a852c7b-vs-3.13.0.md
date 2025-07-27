# Results vs. 3.13.0

- fork: python
- ref: a852c7bdd48979218a0c
- machine: linux-aarch64
- commit hash: a852c7b
- commit date: 2025-07-26
- overall geometric mean: 1.098x slower
- HPT reliability: 99.92%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.29x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 354 ms: 1.13x slower                                                    |
| docutils       | 2.96 sec                                                 | 3.16 sec: 1.07x slower                                                  |
| html5lib       | 65.6 ms                                                  | 70.4 ms: 1.07x slower                                                   |
| sphinx         | 1.20 sec                                                 | 1.29 sec: 1.08x slower                                                  |
| Geometric mean | (ref)                                                    | 1.09x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 445 ms: 1.49x faster                                                    |
| async_tree_io_tg           | 1.16 sec                                                 | 824 ms: 1.41x faster                                                    |
| async_tree_memoization     | 664 ms                                                   | 472 ms: 1.41x faster                                                    |
| async_tree_none_tg         | 484 ms                                                   | 366 ms: 1.32x faster                                                    |
| async_tree_io              | 1.14 sec                                                 | 863 ms: 1.32x faster                                                    |
| async_tree_none            | 504 ms                                                   | 397 ms: 1.27x faster                                                    |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 633 ms: 1.26x faster                                                    |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 674 ms: 1.17x faster                                                    |
| coroutines                 | 29.4 ms                                                  | 31.4 ms: 1.07x slower                                                   |
| Geometric mean             | (ref)                                                    | 1.22x faster                                                            |

Benchmark hidden because not significant (2): asyncio_websockets, async_generators

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 118 ms                                                   | 182 ms: 1.54x slower                                                    |
| Geometric mean | (ref)                                                    | 1.14x slower                                                            |

Benchmark hidden because not significant (2): pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 3.76 ms: 1.36x faster                                                   |
| regex_v8       | 32.5 ms                                                  | 26.2 ms: 1.24x faster                                                   |
| regex_dna      | 263 ms                                                   | 240 ms: 1.09x faster                                                    |
| regex_compile  | 134 ms                                                   | 149 ms: 1.11x slower                                                    |
| Geometric mean | (ref)                                                    | 1.13x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_iterparse  | 159 ms                                                   | 133 ms: 1.20x faster                                                    |
| xml_etree_parse      | 203 ms                                                   | 181 ms: 1.12x faster                                                    |
| tomli_loads          | 2.67 sec                                                 | 2.89 sec: 1.08x slower                                                  |
| unpickle_pure_python | 265 us                                                   | 301 us: 1.14x slower                                                    |
| json_loads           | 32.8 us                                                  | 37.6 us: 1.15x slower                                                   |
| xml_etree_generate   | 118 ms                                                   | 139 ms: 1.18x slower                                                    |
| pickle_pure_python   | 374 us                                                   | 452 us: 1.21x slower                                                    |
| xml_etree_process    | 82.1 ms                                                  | 100 ms: 1.22x slower                                                    |
| Geometric mean       | (ref)                                                    | 1.07x slower                                                            |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 16.0 ms                                                  | 20.0 ms: 1.25x slower                                                   |
| python_startup_no_site | 8.79 ms                                                  | 12.2 ms: 1.38x slower                                                   |
| Geometric mean         | (ref)                                                    | 1.31x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|-----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 61.6 ms                                                  | 75.7 ms: 1.23x slower                                                   |
| genshi_text     | 28.6 ms                                                  | 35.7 ms: 1.25x slower                                                   |
| django_template | 39.4 ms                                                  | 51.3 ms: 1.30x slower                                                   |
| mako            | 14.0 ms                                                  | 21.3 ms: 1.52x slower                                                   |
| Geometric mean  | (ref)                                                    | 1.32x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| gc_traversal               | 5.92 ms                                                  | 2.92 ms: 2.03x faster                                                   |
| mdp                        | 3.45 sec                                                 | 1.93 sec: 1.78x faster                                                  |
| create_gc_cycles           | 3.39 ms                                                  | 2.28 ms: 1.49x faster                                                   |
| async_tree_memoization_tg  | 663 ms                                                   | 445 ms: 1.49x faster                                                    |
| async_tree_io_tg           | 1.16 sec                                                 | 824 ms: 1.41x faster                                                    |
| async_tree_memoization     | 664 ms                                                   | 472 ms: 1.41x faster                                                    |
| regex_effbot               | 5.10 ms                                                  | 3.76 ms: 1.36x faster                                                   |
| async_tree_none_tg         | 484 ms                                                   | 366 ms: 1.32x faster                                                    |
| async_tree_io              | 1.14 sec                                                 | 863 ms: 1.32x faster                                                    |
| async_tree_none            | 504 ms                                                   | 397 ms: 1.27x faster                                                    |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 633 ms: 1.26x faster                                                    |
| regex_v8                   | 32.5 ms                                                  | 26.2 ms: 1.24x faster                                                   |
| deepcopy                   | 479 us                                                   | 395 us: 1.21x faster                                                    |
| xml_etree_iterparse        | 159 ms                                                   | 133 ms: 1.20x faster                                                    |
| sqlite_synth               | 4.08 us                                                  | 3.44 us: 1.19x faster                                                   |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 674 ms: 1.17x faster                                                    |
| deepcopy_memo              | 53.0 us                                                  | 46.1 us: 1.15x faster                                                   |
| xml_etree_parse            | 203 ms                                                   | 181 ms: 1.12x faster                                                    |
| regex_dna                  | 263 ms                                                   | 240 ms: 1.09x faster                                                    |
| go                         | 164 ms                                                   | 154 ms: 1.06x faster                                                    |
| k_core                     | 2.99 sec                                                 | 3.07 sec: 1.03x slower                                                  |
| logging_silent             | 135 ns                                                   | 140 ns: 1.04x slower                                                    |
| hexiom                     | 7.34 ms                                                  | 7.81 ms: 1.06x slower                                                   |
| docutils                   | 2.96 sec                                                 | 3.16 sec: 1.07x slower                                                  |
| coroutines                 | 29.4 ms                                                  | 31.4 ms: 1.07x slower                                                   |
| json                       | 5.94 ms                                                  | 6.36 ms: 1.07x slower                                                   |
| html5lib                   | 65.6 ms                                                  | 70.4 ms: 1.07x slower                                                   |
| sphinx                     | 1.20 sec                                                 | 1.29 sec: 1.08x slower                                                  |
| pprint_pformat             | 1.99 sec                                                 | 2.14 sec: 1.08x slower                                                  |
| tomli_loads                | 2.67 sec                                                 | 2.89 sec: 1.08x slower                                                  |
| pprint_safe_repr           | 962 ms                                                   | 1.04 sec: 1.08x slower                                                  |
| logging_simple             | 7.25 us                                                  | 8.03 us: 1.11x slower                                                   |
| regex_compile              | 134 ms                                                   | 149 ms: 1.11x slower                                                    |
| pylint                     | 345 ms                                                   | 385 ms: 1.11x slower                                                    |
| logging_format             | 8.10 us                                                  | 9.09 us: 1.12x slower                                                   |
| 2to3                       | 313 ms                                                   | 354 ms: 1.13x slower                                                    |
| unpickle_pure_python       | 265 us                                                   | 301 us: 1.14x slower                                                    |
| bpe_tokeniser              | 6.02 sec                                                 | 6.89 sec: 1.14x slower                                                  |
| json_loads                 | 32.8 us                                                  | 37.6 us: 1.15x slower                                                   |
| nqueens                    | 105 ms                                                   | 121 ms: 1.15x slower                                                    |
| chaos                      | 70.7 ms                                                  | 81.9 ms: 1.16x slower                                                   |
| scimark_sparse_mat_mult    | 6.66 ms                                                  | 7.71 ms: 1.16x slower                                                   |
| meteor_contest             | 117 ms                                                   | 136 ms: 1.16x slower                                                    |
| xml_etree_generate         | 118 ms                                                   | 139 ms: 1.18x slower                                                    |
| scimark_monte_carlo        | 87.8 ms                                                  | 103 ms: 1.18x slower                                                    |
| comprehensions             | 20.8 us                                                  | 24.6 us: 1.18x slower                                                   |
| thrift                     | 1.01 ms                                                  | 1.20 ms: 1.19x slower                                                   |
| deltablue                  | 3.97 ms                                                  | 4.74 ms: 1.19x slower                                                   |
| shortest_path              | 565 ms                                                   | 682 ms: 1.21x slower                                                    |
| pickle_pure_python         | 374 us                                                   | 452 us: 1.21x slower                                                    |
| connected_components       | 547 ms                                                   | 662 ms: 1.21x slower                                                    |
| sympy_integrate            | 21.4 ms                                                  | 26.1 ms: 1.22x slower                                                   |
| xml_etree_process          | 82.1 ms                                                  | 100 ms: 1.22x slower                                                    |
| genshi_xml                 | 61.6 ms                                                  | 75.7 ms: 1.23x slower                                                   |
| sympy_sum                  | 151 ms                                                   | 186 ms: 1.23x slower                                                    |
| typing_runtime_protocols   | 197 us                                                   | 244 us: 1.24x slower                                                    |
| fannkuch                   | 478 ms                                                   | 596 ms: 1.25x slower                                                    |
| sympy_expand               | 472 ms                                                   | 589 ms: 1.25x slower                                                    |
| genshi_text                | 28.6 ms                                                  | 35.7 ms: 1.25x slower                                                   |
| python_startup             | 16.0 ms                                                  | 20.0 ms: 1.25x slower                                                   |
| scimark_lu                 | 146 ms                                                   | 184 ms: 1.26x slower                                                    |
| crypto_pyaes               | 84.9 ms                                                  | 107 ms: 1.26x slower                                                    |
| raytrace                   | 310 ms                                                   | 394 ms: 1.27x slower                                                    |
| richards                   | 54.5 ms                                                  | 70.8 ms: 1.30x slower                                                   |
| django_template            | 39.4 ms                                                  | 51.3 ms: 1.30x slower                                                   |
| sympy_str                  | 265 ms                                                   | 345 ms: 1.30x slower                                                    |
| coverage                   | 106 ms                                                   | 143 ms: 1.35x slower                                                    |
| richards_super             | 60.8 ms                                                  | 82.2 ms: 1.35x slower                                                   |
| bench_thread_pool          | 1.34 ms                                                  | 1.83 ms: 1.37x slower                                                   |
| python_startup_no_site     | 8.79 ms                                                  | 12.2 ms: 1.38x slower                                                   |
| mako                       | 14.0 ms                                                  | 21.3 ms: 1.52x slower                                                   |
| nbody                      | 118 ms                                                   | 182 ms: 1.54x slower                                                    |
| many_optionals             | 626 us                                                   | 1.12 ms: 1.79x slower                                                   |
| subparsers                 | 20.3 ms                                                  | 60.4 ms: 2.97x slower                                                   |
| bench_mp_pool              | 8.07 ms                                                  | 64.7 ms: 8.02x slower                                                   |
| telco                      | 10.5 ms                                                  | 189 ms: 18.03x slower                                                   |
| Geometric mean             | (ref)                                                    | 1.12x slower                                                            |

Benchmark hidden because not significant (13): pathlib, pidigits, float, spectral_norm, scimark_sor, asyncio_websockets, generators, async_generators, pycparser, deepcopy_reduce, scimark_fft, pyflate, json_dumps
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (13) of results/bm-20250726-3.15.0a0-a852c7b-NOGIL/bm-20250726-arminc-aarch64-python-a852c7bdd48979218a0c-3.15.0a0-a852c7b.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.098x slower

# HPT report

- Reliability score: 99.92% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.29x