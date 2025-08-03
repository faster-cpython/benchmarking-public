# Results vs. 3.13.0

- fork: python
- ref: 801cf3fcdd27d8b6dd0f
- machine: linux-aarch64
- commit hash: 801cf3f
- commit date: 2025-08-02
- overall geometric mean: 1.094x slower
- HPT reliability: 99.92%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.29x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 350 ms: 1.12x slower                                                    |
| docutils       | 2.96 sec                                                 | 3.16 sec: 1.07x slower                                                  |
| html5lib       | 65.6 ms                                                  | 70.0 ms: 1.07x slower                                                   |
| sphinx         | 1.20 sec                                                 | 1.27 sec: 1.06x slower                                                  |
| Geometric mean | (ref)                                                    | 1.08x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 438 ms: 1.51x faster                                                    |
| async_tree_memoization     | 664 ms                                                   | 470 ms: 1.41x faster                                                    |
| async_tree_io_tg           | 1.16 sec                                                 | 827 ms: 1.41x faster                                                    |
| async_tree_io              | 1.14 sec                                                 | 846 ms: 1.35x faster                                                    |
| async_tree_none_tg         | 484 ms                                                   | 362 ms: 1.34x faster                                                    |
| async_tree_none            | 504 ms                                                   | 390 ms: 1.29x faster                                                    |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 633 ms: 1.27x faster                                                    |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 657 ms: 1.20x faster                                                    |
| async_generators           | 500 ms                                                   | 519 ms: 1.04x slower                                                    |
| coroutines                 | 29.4 ms                                                  | 31.6 ms: 1.08x slower                                                   |
| Geometric mean             | (ref)                                                    | 1.23x faster                                                            |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 118 ms                                                   | 183 ms: 1.54x slower                                                    |
| Geometric mean | (ref)                                                    | 1.14x slower                                                            |

Benchmark hidden because not significant (2): float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 3.83 ms: 1.33x faster                                                   |
| regex_v8       | 32.5 ms                                                  | 25.9 ms: 1.26x faster                                                   |
| regex_dna      | 263 ms                                                   | 238 ms: 1.10x faster                                                    |
| regex_compile  | 134 ms                                                   | 153 ms: 1.14x slower                                                    |
| Geometric mean | (ref)                                                    | 1.13x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_iterparse  | 159 ms                                                   | 130 ms: 1.22x faster                                                    |
| xml_etree_parse      | 203 ms                                                   | 186 ms: 1.09x faster                                                    |
| tomli_loads          | 2.67 sec                                                 | 2.86 sec: 1.07x slower                                                  |
| json_loads           | 32.8 us                                                  | 36.6 us: 1.12x slower                                                   |
| unpickle_pure_python | 265 us                                                   | 300 us: 1.13x slower                                                    |
| xml_etree_generate   | 118 ms                                                   | 139 ms: 1.17x slower                                                    |
| pickle_pure_python   | 374 us                                                   | 442 us: 1.18x slower                                                    |
| xml_etree_process    | 82.1 ms                                                  | 101 ms: 1.23x slower                                                    |
| Geometric mean       | (ref)                                                    | 1.07x slower                                                            |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 16.0 ms                                                  | 19.9 ms: 1.24x slower                                                   |
| python_startup_no_site | 8.79 ms                                                  | 12.0 ms: 1.36x slower                                                   |
| Geometric mean         | (ref)                                                    | 1.30x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|-----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 61.6 ms                                                  | 76.0 ms: 1.23x slower                                                   |
| genshi_text     | 28.6 ms                                                  | 36.2 ms: 1.27x slower                                                   |
| django_template | 39.4 ms                                                  | 50.9 ms: 1.29x slower                                                   |
| mako            | 14.0 ms                                                  | 21.4 ms: 1.53x slower                                                   |
| Geometric mean  | (ref)                                                    | 1.33x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| gc_traversal               | 5.92 ms                                                  | 2.87 ms: 2.06x faster                                                   |
| mdp                        | 3.45 sec                                                 | 1.93 sec: 1.79x faster                                                  |
| async_tree_memoization_tg  | 663 ms                                                   | 438 ms: 1.51x faster                                                    |
| create_gc_cycles           | 3.39 ms                                                  | 2.27 ms: 1.50x faster                                                   |
| async_tree_memoization     | 664 ms                                                   | 470 ms: 1.41x faster                                                    |
| async_tree_io_tg           | 1.16 sec                                                 | 827 ms: 1.41x faster                                                    |
| async_tree_io              | 1.14 sec                                                 | 846 ms: 1.35x faster                                                    |
| async_tree_none_tg         | 484 ms                                                   | 362 ms: 1.34x faster                                                    |
| regex_effbot               | 5.10 ms                                                  | 3.83 ms: 1.33x faster                                                   |
| async_tree_none            | 504 ms                                                   | 390 ms: 1.29x faster                                                    |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 633 ms: 1.27x faster                                                    |
| regex_v8                   | 32.5 ms                                                  | 25.9 ms: 1.26x faster                                                   |
| deepcopy                   | 479 us                                                   | 386 us: 1.24x faster                                                    |
| xml_etree_iterparse        | 159 ms                                                   | 130 ms: 1.22x faster                                                    |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 657 ms: 1.20x faster                                                    |
| sqlite_synth               | 4.08 us                                                  | 3.44 us: 1.19x faster                                                   |
| deepcopy_memo              | 53.0 us                                                  | 45.3 us: 1.17x faster                                                   |
| regex_dna                  | 263 ms                                                   | 238 ms: 1.10x faster                                                    |
| xml_etree_parse            | 203 ms                                                   | 186 ms: 1.09x faster                                                    |
| go                         | 164 ms                                                   | 152 ms: 1.08x faster                                                    |
| pathlib                    | 24.3 ms                                                  | 22.6 ms: 1.08x faster                                                   |
| logging_silent             | 135 ns                                                   | 139 ns: 1.03x slower                                                    |
| async_generators           | 500 ms                                                   | 519 ms: 1.04x slower                                                    |
| json                       | 5.94 ms                                                  | 6.25 ms: 1.05x slower                                                   |
| hexiom                     | 7.34 ms                                                  | 7.77 ms: 1.06x slower                                                   |
| sphinx                     | 1.20 sec                                                 | 1.27 sec: 1.06x slower                                                  |
| docutils                   | 2.96 sec                                                 | 3.16 sec: 1.07x slower                                                  |
| html5lib                   | 65.6 ms                                                  | 70.0 ms: 1.07x slower                                                   |
| tomli_loads                | 2.67 sec                                                 | 2.86 sec: 1.07x slower                                                  |
| coroutines                 | 29.4 ms                                                  | 31.6 ms: 1.08x slower                                                   |
| pylint                     | 345 ms                                                   | 373 ms: 1.08x slower                                                    |
| pprint_pformat             | 1.99 sec                                                 | 2.14 sec: 1.08x slower                                                  |
| pprint_safe_repr           | 962 ms                                                   | 1.04 sec: 1.09x slower                                                  |
| nqueens                    | 105 ms                                                   | 116 ms: 1.11x slower                                                    |
| json_loads                 | 32.8 us                                                  | 36.6 us: 1.12x slower                                                   |
| 2to3                       | 313 ms                                                   | 350 ms: 1.12x slower                                                    |
| unpickle_pure_python       | 265 us                                                   | 300 us: 1.13x slower                                                    |
| logging_simple             | 7.25 us                                                  | 8.24 us: 1.14x slower                                                   |
| logging_format             | 8.10 us                                                  | 9.21 us: 1.14x slower                                                   |
| regex_compile              | 134 ms                                                   | 153 ms: 1.14x slower                                                    |
| bpe_tokeniser              | 6.02 sec                                                 | 6.92 sec: 1.15x slower                                                  |
| comprehensions             | 20.8 us                                                  | 24.1 us: 1.16x slower                                                   |
| chaos                      | 70.7 ms                                                  | 82.0 ms: 1.16x slower                                                   |
| scimark_sparse_mat_mult    | 6.66 ms                                                  | 7.73 ms: 1.16x slower                                                   |
| xml_etree_generate         | 118 ms                                                   | 139 ms: 1.17x slower                                                    |
| scimark_monte_carlo        | 87.8 ms                                                  | 103 ms: 1.18x slower                                                    |
| pickle_pure_python         | 374 us                                                   | 442 us: 1.18x slower                                                    |
| meteor_contest             | 117 ms                                                   | 139 ms: 1.19x slower                                                    |
| thrift                     | 1.01 ms                                                  | 1.20 ms: 1.19x slower                                                   |
| sympy_integrate            | 21.4 ms                                                  | 25.6 ms: 1.19x slower                                                   |
| connected_components       | 547 ms                                                   | 654 ms: 1.20x slower                                                    |
| shortest_path              | 565 ms                                                   | 678 ms: 1.20x slower                                                    |
| deltablue                  | 3.97 ms                                                  | 4.80 ms: 1.21x slower                                                   |
| xml_etree_process          | 82.1 ms                                                  | 101 ms: 1.23x slower                                                    |
| fannkuch                   | 478 ms                                                   | 588 ms: 1.23x slower                                                    |
| sympy_sum                  | 151 ms                                                   | 186 ms: 1.23x slower                                                    |
| genshi_xml                 | 61.6 ms                                                  | 76.0 ms: 1.23x slower                                                   |
| typing_runtime_protocols   | 197 us                                                   | 244 us: 1.24x slower                                                    |
| sympy_expand               | 472 ms                                                   | 586 ms: 1.24x slower                                                    |
| python_startup             | 16.0 ms                                                  | 19.9 ms: 1.24x slower                                                   |
| crypto_pyaes               | 84.9 ms                                                  | 107 ms: 1.26x slower                                                    |
| genshi_text                | 28.6 ms                                                  | 36.2 ms: 1.27x slower                                                   |
| sympy_str                  | 265 ms                                                   | 337 ms: 1.27x slower                                                    |
| scimark_lu                 | 146 ms                                                   | 186 ms: 1.28x slower                                                    |
| raytrace                   | 310 ms                                                   | 398 ms: 1.29x slower                                                    |
| django_template            | 39.4 ms                                                  | 50.9 ms: 1.29x slower                                                   |
| richards                   | 54.5 ms                                                  | 70.7 ms: 1.30x slower                                                   |
| richards_super             | 60.8 ms                                                  | 80.3 ms: 1.32x slower                                                   |
| coverage                   | 106 ms                                                   | 142 ms: 1.34x slower                                                    |
| bench_thread_pool          | 1.34 ms                                                  | 1.80 ms: 1.34x slower                                                   |
| python_startup_no_site     | 8.79 ms                                                  | 12.0 ms: 1.36x slower                                                   |
| mako                       | 14.0 ms                                                  | 21.4 ms: 1.53x slower                                                   |
| nbody                      | 118 ms                                                   | 183 ms: 1.54x slower                                                    |
| many_optionals             | 626 us                                                   | 1.08 ms: 1.73x slower                                                   |
| subparsers                 | 20.3 ms                                                  | 58.0 ms: 2.85x slower                                                   |
| bench_mp_pool              | 8.07 ms                                                  | 63.8 ms: 7.91x slower                                                   |
| telco                      | 10.5 ms                                                  | 186 ms: 17.83x slower                                                   |
| Geometric mean             | (ref)                                                    | 1.12x slower                                                            |

Benchmark hidden because not significant (12): float, pidigits, scimark_sor, pycparser, asyncio_websockets, pyflate, spectral_norm, scimark_fft, generators, k_core, deepcopy_reduce, json_dumps
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (13) of results/bm-20250802-3.15.0a0-801cf3f-NOGIL/bm-20250802-arminc-aarch64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.094x slower

# HPT report

- Reliability score: 99.92% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.29x