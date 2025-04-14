# Results vs. 3.13.0

- fork: python
- ref: 29f8a67ae00081a36fdc
- machine: linux-aarch64
- commit hash: 29f8a67
- commit date: 2025-02-08
- overall geometric mean: 1.124x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x slower
- Memory change: 1.24x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 388 ms: 1.24x slower                                                     |
| docutils       | 2.96 sec                                                 | 3.39 sec: 1.14x slower                                                   |
| html5lib       | 65.6 ms                                                  | 80.6 ms: 1.23x slower                                                    |
| sphinx         | 1.20 sec                                                 | 1.38 sec: 1.15x slower                                                   |
| Geometric mean | (ref)                                                    | 1.19x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 500 ms: 1.33x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 914 ms: 1.27x faster                                                     |
| async_tree_memoization     | 664 ms                                                   | 539 ms: 1.23x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 955 ms: 1.19x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 414 ms: 1.17x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 695 ms: 1.15x faster                                                     |
| async_tree_none            | 504 ms                                                   | 444 ms: 1.14x faster                                                     |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 716 ms: 1.10x faster                                                     |
| async_generators           | 500 ms                                                   | 542 ms: 1.08x slower                                                     |
| Geometric mean             | (ref)                                                    | 1.13x faster                                                             |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 102 ms: 1.07x slower                                                     |
| nbody          | 118 ms                                                   | 183 ms: 1.54x slower                                                     |
| Geometric mean | (ref)                                                    | 1.19x slower                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 4.07 ms: 1.25x faster                                                    |
| regex_compile  | 134 ms                                                   | 161 ms: 1.20x slower                                                     |
| Geometric mean | (ref)                                                    | 1.01x faster                                                             |

Benchmark hidden because not significant (2): regex_v8, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_iterparse  | 159 ms                                                   | 131 ms: 1.21x faster                                                     |
| xml_etree_parse      | 203 ms                                                   | 180 ms: 1.13x faster                                                     |
| xml_etree_generate   | 118 ms                                                   | 138 ms: 1.17x slower                                                     |
| tomli_loads          | 2.67 sec                                                 | 3.16 sec: 1.18x slower                                                   |
| json_loads           | 32.8 us                                                  | 39.9 us: 1.22x slower                                                    |
| json_dumps           | 14.2 ms                                                  | 17.7 ms: 1.25x slower                                                    |
| xml_etree_process    | 82.1 ms                                                  | 103 ms: 1.25x slower                                                     |
| unpickle_pure_python | 265 us                                                   | 333 us: 1.26x slower                                                     |
| pickle_pure_python   | 374 us                                                   | 499 us: 1.33x slower                                                     |
| Geometric mean       | (ref)                                                    | 1.14x slower                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 16.0 ms                                                  | 20.1 ms: 1.25x slower                                                    |
| python_startup_no_site | 8.79 ms                                                  | 12.3 ms: 1.39x slower                                                    |
| Geometric mean         | (ref)                                                    | 1.32x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|-----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text     | 28.6 ms                                                  | 37.0 ms: 1.29x slower                                                    |
| genshi_xml      | 61.6 ms                                                  | 81.1 ms: 1.32x slower                                                    |
| django_template | 39.4 ms                                                  | 60.0 ms: 1.52x slower                                                    |
| mako            | 14.0 ms                                                  | 23.4 ms: 1.68x slower                                                    |
| Geometric mean  | (ref)                                                    | 1.44x slower                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| gc_traversal               | 5.92 ms                                                  | 2.75 ms: 2.16x faster                                                    |
| create_gc_cycles           | 3.39 ms                                                  | 2.20 ms: 1.54x faster                                                    |
| async_tree_memoization_tg  | 663 ms                                                   | 500 ms: 1.33x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 914 ms: 1.27x faster                                                     |
| regex_effbot               | 5.10 ms                                                  | 4.07 ms: 1.25x faster                                                    |
| async_tree_memoization     | 664 ms                                                   | 539 ms: 1.23x faster                                                     |
| xml_etree_iterparse        | 159 ms                                                   | 131 ms: 1.21x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 955 ms: 1.19x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 414 ms: 1.17x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 695 ms: 1.15x faster                                                     |
| async_tree_none            | 504 ms                                                   | 444 ms: 1.14x faster                                                     |
| xml_etree_parse            | 203 ms                                                   | 180 ms: 1.13x faster                                                     |
| deepcopy                   | 479 us                                                   | 427 us: 1.12x faster                                                     |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 716 ms: 1.10x faster                                                     |
| sqlite_synth               | 4.08 us                                                  | 3.80 us: 1.07x faster                                                    |
| scimark_sor                | 164 ms                                                   | 173 ms: 1.05x slower                                                     |
| scimark_fft                | 463 ms                                                   | 489 ms: 1.06x slower                                                     |
| go                         | 164 ms                                                   | 174 ms: 1.06x slower                                                     |
| float                      | 95.8 ms                                                  | 102 ms: 1.07x slower                                                     |
| async_generators           | 500 ms                                                   | 542 ms: 1.08x slower                                                     |
| pycparser                  | 1.34 sec                                                 | 1.47 sec: 1.09x slower                                                   |
| k_core                     | 2.99 sec                                                 | 3.28 sec: 1.10x slower                                                   |
| deepcopy_reduce            | 4.24 us                                                  | 4.72 us: 1.11x slower                                                    |
| mdp                        | 3.45 sec                                                 | 3.83 sec: 1.11x slower                                                   |
| pylint                     | 345 ms                                                   | 385 ms: 1.11x slower                                                     |
| telco                      | 10.5 ms                                                  | 11.7 ms: 1.12x slower                                                    |
| json                       | 5.94 ms                                                  | 6.66 ms: 1.12x slower                                                    |
| docutils                   | 2.96 sec                                                 | 3.39 sec: 1.14x slower                                                   |
| logging_silent             | 135 ns                                                   | 154 ns: 1.14x slower                                                     |
| sphinx                     | 1.20 sec                                                 | 1.38 sec: 1.15x slower                                                   |
| pyflate                    | 582 ms                                                   | 671 ms: 1.15x slower                                                     |
| xml_etree_generate         | 118 ms                                                   | 138 ms: 1.17x slower                                                     |
| scimark_sparse_mat_mult    | 6.66 ms                                                  | 7.80 ms: 1.17x slower                                                    |
| sqlglot_normalize          | 131 ms                                                   | 155 ms: 1.18x slower                                                     |
| tomli_loads                | 2.67 sec                                                 | 3.16 sec: 1.18x slower                                                   |
| sqlglot_optimize           | 65.2 ms                                                  | 77.9 ms: 1.19x slower                                                    |
| pprint_pformat             | 1.99 sec                                                 | 2.38 sec: 1.20x slower                                                   |
| logging_format             | 8.10 us                                                  | 9.73 us: 1.20x slower                                                    |
| regex_compile              | 134 ms                                                   | 161 ms: 1.20x slower                                                     |
| pprint_safe_repr           | 962 ms                                                   | 1.16 sec: 1.21x slower                                                   |
| connected_components       | 547 ms                                                   | 663 ms: 1.21x slower                                                     |
| json_loads                 | 32.8 us                                                  | 39.9 us: 1.22x slower                                                    |
| bpe_tokeniser              | 6.02 sec                                                 | 7.33 sec: 1.22x slower                                                   |
| html5lib                   | 65.6 ms                                                  | 80.6 ms: 1.23x slower                                                    |
| shortest_path              | 565 ms                                                   | 698 ms: 1.23x slower                                                     |
| logging_simple             | 7.25 us                                                  | 8.97 us: 1.24x slower                                                    |
| nqueens                    | 105 ms                                                   | 130 ms: 1.24x slower                                                     |
| 2to3                       | 313 ms                                                   | 388 ms: 1.24x slower                                                     |
| json_dumps                 | 14.2 ms                                                  | 17.7 ms: 1.25x slower                                                    |
| thrift                     | 1.01 ms                                                  | 1.26 ms: 1.25x slower                                                    |
| python_startup             | 16.0 ms                                                  | 20.1 ms: 1.25x slower                                                    |
| chaos                      | 70.7 ms                                                  | 88.7 ms: 1.25x slower                                                    |
| xml_etree_process          | 82.1 ms                                                  | 103 ms: 1.25x slower                                                     |
| unpickle_pure_python       | 265 us                                                   | 333 us: 1.26x slower                                                     |
| sympy_sum                  | 151 ms                                                   | 191 ms: 1.26x slower                                                     |
| sqlalchemy_declarative     | 154 ms                                                   | 195 ms: 1.27x slower                                                     |
| coverage                   | 106 ms                                                   | 135 ms: 1.27x slower                                                     |
| scimark_monte_carlo        | 87.8 ms                                                  | 113 ms: 1.29x slower                                                     |
| hexiom                     | 7.34 ms                                                  | 9.48 ms: 1.29x slower                                                    |
| genshi_text                | 28.6 ms                                                  | 37.0 ms: 1.29x slower                                                    |
| comprehensions             | 20.8 us                                                  | 27.0 us: 1.30x slower                                                    |
| sympy_expand               | 472 ms                                                   | 616 ms: 1.30x slower                                                     |
| sympy_integrate            | 21.4 ms                                                  | 28.0 ms: 1.31x slower                                                    |
| meteor_contest             | 117 ms                                                   | 154 ms: 1.32x slower                                                     |
| genshi_xml                 | 61.6 ms                                                  | 81.1 ms: 1.32x slower                                                    |
| scimark_lu                 | 146 ms                                                   | 193 ms: 1.32x slower                                                     |
| sqlglot_transpile          | 1.84 ms                                                  | 2.43 ms: 1.32x slower                                                    |
| pickle_pure_python         | 374 us                                                   | 499 us: 1.33x slower                                                     |
| crypto_pyaes               | 84.9 ms                                                  | 114 ms: 1.34x slower                                                     |
| raytrace                   | 310 ms                                                   | 423 ms: 1.36x slower                                                     |
| richards                   | 54.5 ms                                                  | 74.5 ms: 1.37x slower                                                    |
| sqlglot_parse              | 1.43 ms                                                  | 1.96 ms: 1.37x slower                                                    |
| sympy_str                  | 265 ms                                                   | 364 ms: 1.37x slower                                                     |
| sqlalchemy_imperative      | 16.1 ms                                                  | 22.4 ms: 1.39x slower                                                    |
| python_startup_no_site     | 8.79 ms                                                  | 12.3 ms: 1.39x slower                                                    |
| richards_super             | 60.8 ms                                                  | 85.9 ms: 1.41x slower                                                    |
| bench_thread_pool          | 1.34 ms                                                  | 1.90 ms: 1.42x slower                                                    |
| typing_runtime_protocols   | 197 us                                                   | 281 us: 1.42x slower                                                     |
| fannkuch                   | 478 ms                                                   | 688 ms: 1.44x slower                                                     |
| django_template            | 39.4 ms                                                  | 60.0 ms: 1.52x slower                                                    |
| deltablue                  | 3.97 ms                                                  | 6.09 ms: 1.54x slower                                                    |
| nbody                      | 118 ms                                                   | 183 ms: 1.54x slower                                                     |
| subparsers                 | 20.3 ms                                                  | 33.4 ms: 1.64x slower                                                    |
| mako                       | 14.0 ms                                                  | 23.4 ms: 1.68x slower                                                    |
| many_optionals             | 626 us                                                   | 1.06 ms: 1.69x slower                                                    |
| bench_mp_pool              | 8.07 ms                                                  | 58.5 ms: 7.25x slower                                                    |
| Geometric mean             | (ref)                                                    | 1.17x slower                                                             |

Benchmark hidden because not significant (9): regex_v8, spectral_norm, pathlib, asyncio_websockets, regex_dna, coroutines, pidigits, deepcopy_memo, generators
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (9) of results/bm-20250208-3.14.0a4+-29f8a67-NOGIL/bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.124x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.13x
- 95% likely to have a slowdown of 1.12x
- 99% likely to have a slowdown of 1.09x

# Memory
- memory change: 1.24x