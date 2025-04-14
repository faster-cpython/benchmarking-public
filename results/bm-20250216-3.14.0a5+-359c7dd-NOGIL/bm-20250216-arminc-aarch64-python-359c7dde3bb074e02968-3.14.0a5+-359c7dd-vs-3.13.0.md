# Results vs. 3.13.0

- fork: python
- ref: 359c7dde3bb074e02968
- machine: linux-aarch64
- commit hash: 359c7dd
- commit date: 2025-02-16
- overall geometric mean: 1.119x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x slower
- Memory change: 1.24x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 377 ms: 1.21x slower                                                     |
| docutils       | 2.96 sec                                                 | 3.32 sec: 1.12x slower                                                   |
| html5lib       | 65.6 ms                                                  | 75.3 ms: 1.15x slower                                                    |
| sphinx         | 1.20 sec                                                 | 1.35 sec: 1.13x slower                                                   |
| Geometric mean | (ref)                                                    | 1.15x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 499 ms: 1.33x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 925 ms: 1.26x faster                                                     |
| async_tree_memoization     | 664 ms                                                   | 549 ms: 1.21x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 974 ms: 1.17x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 690 ms: 1.16x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 419 ms: 1.16x faster                                                     |
| async_tree_none            | 504 ms                                                   | 452 ms: 1.11x faster                                                     |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 721 ms: 1.09x faster                                                     |
| async_generators           | 500 ms                                                   | 530 ms: 1.06x slower                                                     |
| Geometric mean             | (ref)                                                    | 1.12x faster                                                             |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 101 ms: 1.05x slower                                                     |
| nbody          | 118 ms                                                   | 185 ms: 1.56x slower                                                     |
| Geometric mean | (ref)                                                    | 1.18x slower                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 4.00 ms: 1.28x faster                                                    |
| regex_compile  | 134 ms                                                   | 165 ms: 1.23x slower                                                     |
| Geometric mean | (ref)                                                    | 1.02x faster                                                             |

Benchmark hidden because not significant (2): regex_v8, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_iterparse  | 159 ms                                                   | 130 ms: 1.22x faster                                                     |
| xml_etree_parse      | 203 ms                                                   | 179 ms: 1.13x faster                                                     |
| json_loads           | 32.8 us                                                  | 38.4 us: 1.17x slower                                                    |
| xml_etree_generate   | 118 ms                                                   | 139 ms: 1.17x slower                                                     |
| unpickle_pure_python | 265 us                                                   | 319 us: 1.20x slower                                                     |
| json_dumps           | 14.2 ms                                                  | 17.1 ms: 1.21x slower                                                    |
| tomli_loads          | 2.67 sec                                                 | 3.23 sec: 1.21x slower                                                   |
| pickle_pure_python   | 374 us                                                   | 460 us: 1.23x slower                                                     |
| xml_etree_process    | 82.1 ms                                                  | 101 ms: 1.23x slower                                                     |
| Geometric mean       | (ref)                                                    | 1.11x slower                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 16.0 ms                                                  | 20.1 ms: 1.26x slower                                                    |
| python_startup_no_site | 8.79 ms                                                  | 12.2 ms: 1.39x slower                                                    |
| Geometric mean         | (ref)                                                    | 1.32x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|-----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_xml      | 61.6 ms                                                  | 78.7 ms: 1.28x slower                                                    |
| genshi_text     | 28.6 ms                                                  | 36.8 ms: 1.29x slower                                                    |
| django_template | 39.4 ms                                                  | 54.6 ms: 1.39x slower                                                    |
| mako            | 14.0 ms                                                  | 22.4 ms: 1.60x slower                                                    |
| Geometric mean  | (ref)                                                    | 1.38x slower                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| gc_traversal               | 5.92 ms                                                  | 2.78 ms: 2.13x faster                                                    |
| create_gc_cycles           | 3.39 ms                                                  | 2.22 ms: 1.53x faster                                                    |
| async_tree_memoization_tg  | 663 ms                                                   | 499 ms: 1.33x faster                                                     |
| regex_effbot               | 5.10 ms                                                  | 4.00 ms: 1.28x faster                                                    |
| async_tree_io_tg           | 1.16 sec                                                 | 925 ms: 1.26x faster                                                     |
| xml_etree_iterparse        | 159 ms                                                   | 130 ms: 1.22x faster                                                     |
| async_tree_memoization     | 664 ms                                                   | 549 ms: 1.21x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 974 ms: 1.17x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 690 ms: 1.16x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 419 ms: 1.16x faster                                                     |
| deepcopy                   | 479 us                                                   | 423 us: 1.13x faster                                                     |
| xml_etree_parse            | 203 ms                                                   | 179 ms: 1.13x faster                                                     |
| async_tree_none            | 504 ms                                                   | 452 ms: 1.11x faster                                                     |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 721 ms: 1.09x faster                                                     |
| sqlite_synth               | 4.08 us                                                  | 3.81 us: 1.07x faster                                                    |
| deepcopy_memo              | 53.0 us                                                  | 51.6 us: 1.03x faster                                                    |
| scimark_fft                | 463 ms                                                   | 487 ms: 1.05x slower                                                     |
| float                      | 95.8 ms                                                  | 101 ms: 1.05x slower                                                     |
| async_generators           | 500 ms                                                   | 530 ms: 1.06x slower                                                     |
| k_core                     | 2.99 sec                                                 | 3.18 sec: 1.06x slower                                                   |
| deepcopy_reduce            | 4.24 us                                                  | 4.51 us: 1.06x slower                                                    |
| pycparser                  | 1.34 sec                                                 | 1.44 sec: 1.07x slower                                                   |
| scimark_sor                | 164 ms                                                   | 178 ms: 1.08x slower                                                     |
| go                         | 164 ms                                                   | 178 ms: 1.08x slower                                                     |
| json                       | 5.94 ms                                                  | 6.50 ms: 1.09x slower                                                    |
| pylint                     | 345 ms                                                   | 382 ms: 1.11x slower                                                     |
| mdp                        | 3.45 sec                                                 | 3.86 sec: 1.12x slower                                                   |
| docutils                   | 2.96 sec                                                 | 3.32 sec: 1.12x slower                                                   |
| sphinx                     | 1.20 sec                                                 | 1.35 sec: 1.13x slower                                                   |
| html5lib                   | 65.6 ms                                                  | 75.3 ms: 1.15x slower                                                    |
| telco                      | 10.5 ms                                                  | 12.0 ms: 1.15x slower                                                    |
| pyflate                    | 582 ms                                                   | 671 ms: 1.15x slower                                                     |
| logging_silent             | 135 ns                                                   | 156 ns: 1.16x slower                                                     |
| json_loads                 | 32.8 us                                                  | 38.4 us: 1.17x slower                                                    |
| xml_etree_generate         | 118 ms                                                   | 139 ms: 1.17x slower                                                     |
| sqlglot_optimize           | 65.2 ms                                                  | 76.5 ms: 1.17x slower                                                    |
| sqlglot_normalize          | 131 ms                                                   | 155 ms: 1.18x slower                                                     |
| pprint_pformat             | 1.99 sec                                                 | 2.37 sec: 1.20x slower                                                   |
| pprint_safe_repr           | 962 ms                                                   | 1.16 sec: 1.20x slower                                                   |
| coverage                   | 106 ms                                                   | 127 ms: 1.20x slower                                                     |
| unpickle_pure_python       | 265 us                                                   | 319 us: 1.20x slower                                                     |
| 2to3                       | 313 ms                                                   | 377 ms: 1.21x slower                                                     |
| json_dumps                 | 14.2 ms                                                  | 17.1 ms: 1.21x slower                                                    |
| logging_simple             | 7.25 us                                                  | 8.75 us: 1.21x slower                                                    |
| tomli_loads                | 2.67 sec                                                 | 3.23 sec: 1.21x slower                                                   |
| thrift                     | 1.01 ms                                                  | 1.22 ms: 1.21x slower                                                    |
| bpe_tokeniser              | 6.02 sec                                                 | 7.35 sec: 1.22x slower                                                   |
| logging_format             | 8.10 us                                                  | 9.96 us: 1.23x slower                                                    |
| shortest_path              | 565 ms                                                   | 696 ms: 1.23x slower                                                     |
| pickle_pure_python         | 374 us                                                   | 460 us: 1.23x slower                                                     |
| xml_etree_process          | 82.1 ms                                                  | 101 ms: 1.23x slower                                                     |
| connected_components       | 547 ms                                                   | 674 ms: 1.23x slower                                                     |
| hexiom                     | 7.34 ms                                                  | 9.06 ms: 1.23x slower                                                    |
| regex_compile              | 134 ms                                                   | 165 ms: 1.23x slower                                                     |
| scimark_sparse_mat_mult    | 6.66 ms                                                  | 8.22 ms: 1.24x slower                                                    |
| python_startup             | 16.0 ms                                                  | 20.1 ms: 1.26x slower                                                    |
| nqueens                    | 105 ms                                                   | 133 ms: 1.27x slower                                                     |
| chaos                      | 70.7 ms                                                  | 90.0 ms: 1.27x slower                                                    |
| sqlalchemy_declarative     | 154 ms                                                   | 196 ms: 1.28x slower                                                     |
| genshi_xml                 | 61.6 ms                                                  | 78.7 ms: 1.28x slower                                                    |
| sympy_expand               | 472 ms                                                   | 605 ms: 1.28x slower                                                     |
| sympy_sum                  | 151 ms                                                   | 194 ms: 1.28x slower                                                     |
| genshi_text                | 28.6 ms                                                  | 36.8 ms: 1.29x slower                                                    |
| comprehensions             | 20.8 us                                                  | 27.0 us: 1.30x slower                                                    |
| richards                   | 54.5 ms                                                  | 71.5 ms: 1.31x slower                                                    |
| scimark_monte_carlo        | 87.8 ms                                                  | 116 ms: 1.32x slower                                                     |
| scimark_lu                 | 146 ms                                                   | 193 ms: 1.32x slower                                                     |
| deltablue                  | 3.97 ms                                                  | 5.29 ms: 1.33x slower                                                    |
| sqlglot_transpile          | 1.84 ms                                                  | 2.45 ms: 1.33x slower                                                    |
| meteor_contest             | 117 ms                                                   | 157 ms: 1.35x slower                                                     |
| sympy_integrate            | 21.4 ms                                                  | 29.0 ms: 1.35x slower                                                    |
| sympy_str                  | 265 ms                                                   | 359 ms: 1.35x slower                                                     |
| raytrace                   | 310 ms                                                   | 423 ms: 1.36x slower                                                     |
| sqlalchemy_imperative      | 16.1 ms                                                  | 22.2 ms: 1.38x slower                                                    |
| sqlglot_parse              | 1.43 ms                                                  | 1.98 ms: 1.38x slower                                                    |
| crypto_pyaes               | 84.9 ms                                                  | 117 ms: 1.38x slower                                                     |
| django_template            | 39.4 ms                                                  | 54.6 ms: 1.39x slower                                                    |
| python_startup_no_site     | 8.79 ms                                                  | 12.2 ms: 1.39x slower                                                    |
| bench_thread_pool          | 1.34 ms                                                  | 1.87 ms: 1.40x slower                                                    |
| fannkuch                   | 478 ms                                                   | 681 ms: 1.42x slower                                                     |
| richards_super             | 60.8 ms                                                  | 87.4 ms: 1.44x slower                                                    |
| typing_runtime_protocols   | 197 us                                                   | 287 us: 1.46x slower                                                     |
| nbody                      | 118 ms                                                   | 185 ms: 1.56x slower                                                     |
| subparsers                 | 20.3 ms                                                  | 32.4 ms: 1.59x slower                                                    |
| mako                       | 14.0 ms                                                  | 22.4 ms: 1.60x slower                                                    |
| many_optionals             | 626 us                                                   | 1.08 ms: 1.72x slower                                                    |
| bench_mp_pool              | 8.07 ms                                                  | 58.8 ms: 7.29x slower                                                    |
| Geometric mean             | (ref)                                                    | 1.16x slower                                                             |

Benchmark hidden because not significant (8): regex_v8, pathlib, regex_dna, spectral_norm, pidigits, asyncio_websockets, generators, coroutines
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (9) of results/bm-20250216-3.14.0a5+-359c7dd-NOGIL/bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.119x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.12x
- 95% likely to have a slowdown of 1.11x
- 99% likely to have a slowdown of 1.08x

# Memory
- memory change: 1.24x