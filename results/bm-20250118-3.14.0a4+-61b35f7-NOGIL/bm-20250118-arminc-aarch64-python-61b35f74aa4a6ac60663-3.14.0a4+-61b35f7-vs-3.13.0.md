# Results vs. 3.13.0

- fork: python
- ref: 61b35f74aa4a6ac60663
- machine: linux-aarch64
- commit hash: 61b35f7
- commit date: 2025-01-18
- overall geometric mean: 1.134x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x slower
- Memory change: 1.23x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 313 ms                                                   | 387 ms: 1.24x slower                                                     |
| docutils       | 2.96 sec                                                 | 3.41 sec: 1.15x slower                                                   |
| html5lib       | 65.6 ms                                                  | 76.2 ms: 1.16x slower                                                    |
| sphinx         | 1.20 sec                                                 | 1.40 sec: 1.16x slower                                                   |
| Geometric mean | (ref)                                                    | 1.18x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 492 ms: 1.35x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 920 ms: 1.27x faster                                                     |
| async_tree_memoization     | 664 ms                                                   | 538 ms: 1.23x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 399 ms: 1.21x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 678 ms: 1.18x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 966 ms: 1.18x faster                                                     |
| async_tree_none            | 504 ms                                                   | 442 ms: 1.14x faster                                                     |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 733 ms: 1.08x faster                                                     |
| coroutines                 | 29.4 ms                                                  | 31.8 ms: 1.08x slower                                                    |
| async_generators           | 500 ms                                                   | 542 ms: 1.08x slower                                                     |
| Geometric mean             | (ref)                                                    | 1.13x faster                                                             |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 103 ms: 1.08x slower                                                     |
| nbody          | 118 ms                                                   | 182 ms: 1.53x slower                                                     |
| Geometric mean | (ref)                                                    | 1.18x slower                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 4.02 ms: 1.27x faster                                                    |
| regex_compile  | 134 ms                                                   | 159 ms: 1.19x slower                                                     |
| Geometric mean | (ref)                                                    | 1.02x faster                                                             |

Benchmark hidden because not significant (2): regex_v8, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_iterparse  | 159 ms                                                   | 133 ms: 1.20x faster                                                     |
| xml_etree_parse      | 203 ms                                                   | 177 ms: 1.15x faster                                                     |
| json_loads           | 32.8 us                                                  | 37.2 us: 1.14x slower                                                    |
| json_dumps           | 14.2 ms                                                  | 16.7 ms: 1.17x slower                                                    |
| xml_etree_generate   | 118 ms                                                   | 140 ms: 1.18x slower                                                     |
| tomli_loads          | 2.67 sec                                                 | 3.25 sec: 1.22x slower                                                   |
| unpickle_pure_python | 265 us                                                   | 331 us: 1.25x slower                                                     |
| xml_etree_process    | 82.1 ms                                                  | 104 ms: 1.27x slower                                                     |
| pickle_pure_python   | 374 us                                                   | 483 us: 1.29x slower                                                     |
| Geometric mean       | (ref)                                                    | 1.12x slower                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 16.0 ms                                                  | 20.0 ms: 1.25x slower                                                    |
| python_startup_no_site | 8.79 ms                                                  | 12.2 ms: 1.39x slower                                                    |
| Geometric mean         | (ref)                                                    | 1.32x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|-----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_xml      | 61.6 ms                                                  | 80.2 ms: 1.30x slower                                                    |
| genshi_text     | 28.6 ms                                                  | 37.2 ms: 1.30x slower                                                    |
| django_template | 39.4 ms                                                  | 56.5 ms: 1.43x slower                                                    |
| mako            | 14.0 ms                                                  | 23.6 ms: 1.69x slower                                                    |
| Geometric mean  | (ref)                                                    | 1.42x slower                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| create_gc_cycles           | 3.39 ms                                                  | 2.17 ms: 1.56x faster                                                    |
| async_tree_memoization_tg  | 663 ms                                                   | 492 ms: 1.35x faster                                                     |
| regex_effbot               | 5.10 ms                                                  | 4.02 ms: 1.27x faster                                                    |
| async_tree_io_tg           | 1.16 sec                                                 | 920 ms: 1.27x faster                                                     |
| async_tree_memoization     | 664 ms                                                   | 538 ms: 1.23x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 399 ms: 1.21x faster                                                     |
| xml_etree_iterparse        | 159 ms                                                   | 133 ms: 1.20x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 678 ms: 1.18x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 966 ms: 1.18x faster                                                     |
| xml_etree_parse            | 203 ms                                                   | 177 ms: 1.15x faster                                                     |
| async_tree_none            | 504 ms                                                   | 442 ms: 1.14x faster                                                     |
| deepcopy                   | 479 us                                                   | 429 us: 1.12x faster                                                     |
| gc_traversal               | 5.92 ms                                                  | 5.42 ms: 1.09x faster                                                    |
| sqlite_synth               | 4.08 us                                                  | 3.75 us: 1.09x faster                                                    |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 733 ms: 1.08x faster                                                     |
| scimark_fft                | 463 ms                                                   | 494 ms: 1.07x slower                                                     |
| json                       | 5.94 ms                                                  | 6.34 ms: 1.07x slower                                                    |
| k_core                     | 2.99 sec                                                 | 3.23 sec: 1.08x slower                                                   |
| float                      | 95.8 ms                                                  | 103 ms: 1.08x slower                                                     |
| coroutines                 | 29.4 ms                                                  | 31.8 ms: 1.08x slower                                                    |
| pycparser                  | 1.34 sec                                                 | 1.46 sec: 1.08x slower                                                   |
| async_generators           | 500 ms                                                   | 542 ms: 1.08x slower                                                     |
| generators                 | 40.3 ms                                                  | 43.9 ms: 1.09x slower                                                    |
| go                         | 164 ms                                                   | 181 ms: 1.10x slower                                                     |
| scimark_sor                | 164 ms                                                   | 183 ms: 1.11x slower                                                     |
| mdp                        | 3.45 sec                                                 | 3.84 sec: 1.11x slower                                                   |
| deepcopy_reduce            | 4.24 us                                                  | 4.76 us: 1.12x slower                                                    |
| telco                      | 10.5 ms                                                  | 11.8 ms: 1.13x slower                                                    |
| pylint                     | 345 ms                                                   | 392 ms: 1.13x slower                                                     |
| json_loads                 | 32.8 us                                                  | 37.2 us: 1.14x slower                                                    |
| pyflate                    | 582 ms                                                   | 661 ms: 1.14x slower                                                     |
| docutils                   | 2.96 sec                                                 | 3.41 sec: 1.15x slower                                                   |
| html5lib                   | 65.6 ms                                                  | 76.2 ms: 1.16x slower                                                    |
| sphinx                     | 1.20 sec                                                 | 1.40 sec: 1.16x slower                                                   |
| json_dumps                 | 14.2 ms                                                  | 16.7 ms: 1.17x slower                                                    |
| logging_silent             | 135 ns                                                   | 159 ns: 1.18x slower                                                     |
| xml_etree_generate         | 118 ms                                                   | 140 ms: 1.18x slower                                                     |
| regex_compile              | 134 ms                                                   | 159 ms: 1.19x slower                                                     |
| connected_components       | 547 ms                                                   | 656 ms: 1.20x slower                                                     |
| pprint_pformat             | 1.99 sec                                                 | 2.39 sec: 1.20x slower                                                   |
| pprint_safe_repr           | 962 ms                                                   | 1.16 sec: 1.21x slower                                                   |
| scimark_sparse_mat_mult    | 6.66 ms                                                  | 8.06 ms: 1.21x slower                                                    |
| shortest_path              | 565 ms                                                   | 685 ms: 1.21x slower                                                     |
| sqlglot_normalize          | 131 ms                                                   | 159 ms: 1.22x slower                                                     |
| sqlglot_optimize           | 65.2 ms                                                  | 79.4 ms: 1.22x slower                                                    |
| tomli_loads                | 2.67 sec                                                 | 3.25 sec: 1.22x slower                                                   |
| 2to3                       | 313 ms                                                   | 387 ms: 1.24x slower                                                     |
| logging_format             | 8.10 us                                                  | 10.1 us: 1.24x slower                                                    |
| python_startup             | 16.0 ms                                                  | 20.0 ms: 1.25x slower                                                    |
| coverage                   | 106 ms                                                   | 132 ms: 1.25x slower                                                     |
| unpickle_pure_python       | 265 us                                                   | 331 us: 1.25x slower                                                     |
| bpe_tokeniser              | 6.02 sec                                                 | 7.53 sec: 1.25x slower                                                   |
| chaos                      | 70.7 ms                                                  | 88.7 ms: 1.25x slower                                                    |
| logging_simple             | 7.25 us                                                  | 9.16 us: 1.26x slower                                                    |
| xml_etree_process          | 82.1 ms                                                  | 104 ms: 1.27x slower                                                     |
| thrift                     | 1.01 ms                                                  | 1.29 ms: 1.28x slower                                                    |
| nqueens                    | 105 ms                                                   | 135 ms: 1.29x slower                                                     |
| scimark_monte_carlo        | 87.8 ms                                                  | 113 ms: 1.29x slower                                                     |
| pickle_pure_python         | 374 us                                                   | 483 us: 1.29x slower                                                     |
| scimark_lu                 | 146 ms                                                   | 189 ms: 1.29x slower                                                     |
| genshi_xml                 | 61.6 ms                                                  | 80.2 ms: 1.30x slower                                                    |
| genshi_text                | 28.6 ms                                                  | 37.2 ms: 1.30x slower                                                    |
| hexiom                     | 7.34 ms                                                  | 9.63 ms: 1.31x slower                                                    |
| sympy_expand               | 472 ms                                                   | 621 ms: 1.31x slower                                                     |
| sympy_sum                  | 151 ms                                                   | 199 ms: 1.32x slower                                                     |
| crypto_pyaes               | 84.9 ms                                                  | 112 ms: 1.32x slower                                                     |
| sqlalchemy_declarative     | 154 ms                                                   | 205 ms: 1.33x slower                                                     |
| sqlglot_transpile          | 1.84 ms                                                  | 2.49 ms: 1.35x slower                                                    |
| meteor_contest             | 117 ms                                                   | 158 ms: 1.35x slower                                                     |
| richards                   | 54.5 ms                                                  | 73.8 ms: 1.35x slower                                                    |
| sqlalchemy_imperative      | 16.1 ms                                                  | 21.8 ms: 1.36x slower                                                    |
| bench_thread_pool          | 1.34 ms                                                  | 1.83 ms: 1.37x slower                                                    |
| raytrace                   | 310 ms                                                   | 426 ms: 1.37x slower                                                     |
| sympy_str                  | 265 ms                                                   | 364 ms: 1.37x slower                                                     |
| python_startup_no_site     | 8.79 ms                                                  | 12.2 ms: 1.39x slower                                                    |
| fannkuch                   | 478 ms                                                   | 678 ms: 1.42x slower                                                     |
| comprehensions             | 20.8 us                                                  | 29.6 us: 1.42x slower                                                    |
| django_template            | 39.4 ms                                                  | 56.5 ms: 1.43x slower                                                    |
| sympy_integrate            | 21.4 ms                                                  | 31.0 ms: 1.45x slower                                                    |
| richards_super             | 60.8 ms                                                  | 88.6 ms: 1.46x slower                                                    |
| typing_runtime_protocols   | 197 us                                                   | 288 us: 1.46x slower                                                     |
| sqlglot_parse              | 1.43 ms                                                  | 2.12 ms: 1.48x slower                                                    |
| many_optionals             | 626 us                                                   | 938 us: 1.50x slower                                                     |
| nbody                      | 118 ms                                                   | 182 ms: 1.53x slower                                                     |
| deltablue                  | 3.97 ms                                                  | 6.30 ms: 1.59x slower                                                    |
| subparsers                 | 20.3 ms                                                  | 34.2 ms: 1.68x slower                                                    |
| mako                       | 14.0 ms                                                  | 23.6 ms: 1.69x slower                                                    |
| bench_mp_pool              | 8.07 ms                                                  | 56.3 ms: 6.98x slower                                                    |
| Geometric mean             | (ref)                                                    | 1.18x slower                                                             |

Benchmark hidden because not significant (7): pathlib, pidigits, regex_v8, regex_dna, deepcopy_memo, asyncio_websockets, spectral_norm
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (9) of results/bm-20250118-3.14.0a4+-61b35f7-NOGIL/bm-20250118-arminc-aarch64-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.134x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.13x
- 95% likely to have a slowdown of 1.12x
- 99% likely to have a slowdown of 1.09x

# Memory
- memory change: 1.23x