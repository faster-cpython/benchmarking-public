# Results vs. 3.13.0

- fork: python
- ref: e82c2ca2a59235bc1965
- machine: linux-aarch64
- commit hash: e82c2ca
- commit date: 2025-03-15
- overall geometric mean: 1.093x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x slower
- Memory change: 1.25x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 357 ms: 1.14x slower                                                     |
| docutils       | 2.96 sec                                                 | 3.18 sec: 1.07x slower                                                   |
| html5lib       | 65.6 ms                                                  | 73.5 ms: 1.12x slower                                                    |
| sphinx         | 1.20 sec                                                 | 1.30 sec: 1.09x slower                                                   |
| Geometric mean | (ref)                                                    | 1.10x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 469 ms: 1.41x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 863 ms: 1.35x faster                                                     |
| async_tree_memoization     | 664 ms                                                   | 511 ms: 1.30x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 376 ms: 1.29x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 902 ms: 1.26x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 652 ms: 1.23x faster                                                     |
| async_tree_none            | 504 ms                                                   | 428 ms: 1.18x faster                                                     |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 689 ms: 1.14x faster                                                     |
| async_generators           | 500 ms                                                   | 514 ms: 1.03x slower                                                     |
| Geometric mean             | (ref)                                                    | 1.19x faster                                                             |

Benchmark hidden because not significant (2): coroutines, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| pidigits       | 238 ms                                                   | 231 ms: 1.03x faster                                                     |
| float          | 95.8 ms                                                  | 102 ms: 1.07x slower                                                     |
| nbody          | 118 ms                                                   | 181 ms: 1.53x slower                                                     |
| Geometric mean | (ref)                                                    | 1.17x slower                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 4.04 ms: 1.26x faster                                                    |
| regex_v8       | 32.5 ms                                                  | 27.4 ms: 1.19x faster                                                    |
| regex_dna      | 263 ms                                                   | 248 ms: 1.06x faster                                                     |
| regex_compile  | 134 ms                                                   | 159 ms: 1.19x slower                                                     |
| Geometric mean | (ref)                                                    | 1.07x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_iterparse  | 159 ms                                                   | 127 ms: 1.26x faster                                                     |
| xml_etree_parse      | 203 ms                                                   | 176 ms: 1.15x faster                                                     |
| xml_etree_generate   | 118 ms                                                   | 134 ms: 1.13x slower                                                     |
| tomli_loads          | 2.67 sec                                                 | 3.06 sec: 1.15x slower                                                   |
| json_dumps           | 14.2 ms                                                  | 16.4 ms: 1.15x slower                                                    |
| json_loads           | 32.8 us                                                  | 38.2 us: 1.17x slower                                                    |
| unpickle_pure_python | 265 us                                                   | 310 us: 1.17x slower                                                     |
| pickle_pure_python   | 374 us                                                   | 440 us: 1.18x slower                                                     |
| xml_etree_process    | 82.1 ms                                                  | 98.6 ms: 1.20x slower                                                    |
| Geometric mean       | (ref)                                                    | 1.08x slower                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 16.0 ms                                                  | 19.6 ms: 1.22x slower                                                    |
| python_startup_no_site | 8.79 ms                                                  | 14.0 ms: 1.59x slower                                                    |
| Geometric mean         | (ref)                                                    | 1.39x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|-----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_xml      | 61.6 ms                                                  | 74.0 ms: 1.20x slower                                                    |
| genshi_text     | 28.6 ms                                                  | 37.4 ms: 1.31x slower                                                    |
| django_template | 39.4 ms                                                  | 53.5 ms: 1.36x slower                                                    |
| mako            | 14.0 ms                                                  | 21.9 ms: 1.57x slower                                                    |
| Geometric mean  | (ref)                                                    | 1.35x slower                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| gc_traversal               | 5.92 ms                                                  | 2.71 ms: 2.19x faster                                                    |
| create_gc_cycles           | 3.39 ms                                                  | 2.08 ms: 1.63x faster                                                    |
| async_tree_memoization_tg  | 663 ms                                                   | 469 ms: 1.41x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 863 ms: 1.35x faster                                                     |
| async_tree_memoization     | 664 ms                                                   | 511 ms: 1.30x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 376 ms: 1.29x faster                                                     |
| regex_effbot               | 5.10 ms                                                  | 4.04 ms: 1.26x faster                                                    |
| async_tree_io              | 1.14 sec                                                 | 902 ms: 1.26x faster                                                     |
| xml_etree_iterparse        | 159 ms                                                   | 127 ms: 1.26x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 652 ms: 1.23x faster                                                     |
| deepcopy                   | 479 us                                                   | 399 us: 1.20x faster                                                     |
| regex_v8                   | 32.5 ms                                                  | 27.4 ms: 1.19x faster                                                    |
| sqlite_synth               | 4.08 us                                                  | 3.44 us: 1.19x faster                                                    |
| async_tree_none            | 504 ms                                                   | 428 ms: 1.18x faster                                                     |
| xml_etree_parse            | 203 ms                                                   | 176 ms: 1.15x faster                                                     |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 689 ms: 1.14x faster                                                     |
| deepcopy_memo              | 53.0 us                                                  | 49.7 us: 1.07x faster                                                    |
| regex_dna                  | 263 ms                                                   | 248 ms: 1.06x faster                                                     |
| pidigits                   | 238 ms                                                   | 231 ms: 1.03x faster                                                     |
| async_generators           | 500 ms                                                   | 514 ms: 1.03x slower                                                     |
| go                         | 164 ms                                                   | 169 ms: 1.03x slower                                                     |
| scimark_fft                | 463 ms                                                   | 481 ms: 1.04x slower                                                     |
| k_core                     | 2.99 sec                                                 | 3.14 sec: 1.05x slower                                                   |
| logging_silent             | 135 ns                                                   | 143 ns: 1.06x slower                                                     |
| deepcopy_reduce            | 4.24 us                                                  | 4.52 us: 1.06x slower                                                    |
| float                      | 95.8 ms                                                  | 102 ms: 1.07x slower                                                     |
| docutils                   | 2.96 sec                                                 | 3.18 sec: 1.07x slower                                                   |
| pyflate                    | 582 ms                                                   | 625 ms: 1.07x slower                                                     |
| mdp                        | 3.45 sec                                                 | 3.71 sec: 1.08x slower                                                   |
| pylint                     | 345 ms                                                   | 373 ms: 1.08x slower                                                     |
| sphinx                     | 1.20 sec                                                 | 1.30 sec: 1.09x slower                                                   |
| json                       | 5.94 ms                                                  | 6.47 ms: 1.09x slower                                                    |
| telco                      | 10.5 ms                                                  | 11.5 ms: 1.10x slower                                                    |
| html5lib                   | 65.6 ms                                                  | 73.5 ms: 1.12x slower                                                    |
| xml_etree_generate         | 118 ms                                                   | 134 ms: 1.13x slower                                                     |
| thrift                     | 1.01 ms                                                  | 1.14 ms: 1.13x slower                                                    |
| 2to3                       | 313 ms                                                   | 357 ms: 1.14x slower                                                     |
| tomli_loads                | 2.67 sec                                                 | 3.06 sec: 1.15x slower                                                   |
| pprint_pformat             | 1.99 sec                                                 | 2.28 sec: 1.15x slower                                                   |
| pprint_safe_repr           | 962 ms                                                   | 1.11 sec: 1.15x slower                                                   |
| json_dumps                 | 14.2 ms                                                  | 16.4 ms: 1.15x slower                                                    |
| logging_format             | 8.10 us                                                  | 9.42 us: 1.16x slower                                                    |
| json_loads                 | 32.8 us                                                  | 38.2 us: 1.17x slower                                                    |
| unpickle_pure_python       | 265 us                                                   | 310 us: 1.17x slower                                                     |
| logging_simple             | 7.25 us                                                  | 8.53 us: 1.18x slower                                                    |
| pickle_pure_python         | 374 us                                                   | 440 us: 1.18x slower                                                     |
| shortest_path              | 565 ms                                                   | 670 ms: 1.19x slower                                                     |
| connected_components       | 547 ms                                                   | 649 ms: 1.19x slower                                                     |
| regex_compile              | 134 ms                                                   | 159 ms: 1.19x slower                                                     |
| xml_etree_process          | 82.1 ms                                                  | 98.6 ms: 1.20x slower                                                    |
| genshi_xml                 | 61.6 ms                                                  | 74.0 ms: 1.20x slower                                                    |
| bpe_tokeniser              | 6.02 sec                                                 | 7.28 sec: 1.21x slower                                                   |
| coverage                   | 106 ms                                                   | 128 ms: 1.21x slower                                                     |
| nqueens                    | 105 ms                                                   | 127 ms: 1.21x slower                                                     |
| sqlalchemy_declarative     | 154 ms                                                   | 187 ms: 1.22x slower                                                     |
| python_startup             | 16.0 ms                                                  | 19.6 ms: 1.22x slower                                                    |
| chaos                      | 70.7 ms                                                  | 87.2 ms: 1.23x slower                                                    |
| hexiom                     | 7.34 ms                                                  | 9.08 ms: 1.24x slower                                                    |
| scimark_sparse_mat_mult    | 6.66 ms                                                  | 8.24 ms: 1.24x slower                                                    |
| scimark_monte_carlo        | 87.8 ms                                                  | 110 ms: 1.25x slower                                                     |
| deltablue                  | 3.97 ms                                                  | 4.97 ms: 1.25x slower                                                    |
| sympy_expand               | 472 ms                                                   | 595 ms: 1.26x slower                                                     |
| sympy_integrate            | 21.4 ms                                                  | 27.1 ms: 1.26x slower                                                    |
| sympy_sum                  | 151 ms                                                   | 192 ms: 1.27x slower                                                     |
| crypto_pyaes               | 84.9 ms                                                  | 108 ms: 1.28x slower                                                     |
| richards                   | 54.5 ms                                                  | 69.8 ms: 1.28x slower                                                    |
| comprehensions             | 20.8 us                                                  | 26.9 us: 1.29x slower                                                    |
| scimark_lu                 | 146 ms                                                   | 189 ms: 1.30x slower                                                     |
| genshi_text                | 28.6 ms                                                  | 37.4 ms: 1.31x slower                                                    |
| sqlalchemy_imperative      | 16.1 ms                                                  | 21.1 ms: 1.31x slower                                                    |
| raytrace                   | 310 ms                                                   | 407 ms: 1.31x slower                                                     |
| meteor_contest             | 117 ms                                                   | 155 ms: 1.32x slower                                                     |
| sympy_str                  | 265 ms                                                   | 352 ms: 1.33x slower                                                     |
| typing_runtime_protocols   | 197 us                                                   | 263 us: 1.33x slower                                                     |
| richards_super             | 60.8 ms                                                  | 81.7 ms: 1.34x slower                                                    |
| django_template            | 39.4 ms                                                  | 53.5 ms: 1.36x slower                                                    |
| bench_thread_pool          | 1.34 ms                                                  | 1.82 ms: 1.36x slower                                                    |
| fannkuch                   | 478 ms                                                   | 652 ms: 1.36x slower                                                     |
| nbody                      | 118 ms                                                   | 181 ms: 1.53x slower                                                     |
| subparsers                 | 20.3 ms                                                  | 31.7 ms: 1.56x slower                                                    |
| mako                       | 14.0 ms                                                  | 21.9 ms: 1.57x slower                                                    |
| python_startup_no_site     | 8.79 ms                                                  | 14.0 ms: 1.59x slower                                                    |
| many_optionals             | 626 us                                                   | 1.02 ms: 1.62x slower                                                    |
| bench_mp_pool              | 8.07 ms                                                  | 57.7 ms: 7.15x slower                                                    |
| Geometric mean             | (ref)                                                    | 1.12x slower                                                             |

Benchmark hidden because not significant (7): pathlib, coroutines, generators, asyncio_websockets, spectral_norm, pycparser, scimark_sor
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (13) of results/bm-20250315-3.14.0a6+-e82c2ca-NOGIL/bm-20250315-arminc-aarch64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.093x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.07x
- 95% likely to have a slowdown of 1.07x
- 99% likely to have a slowdown of 1.05x

# Memory
- memory change: 1.25x