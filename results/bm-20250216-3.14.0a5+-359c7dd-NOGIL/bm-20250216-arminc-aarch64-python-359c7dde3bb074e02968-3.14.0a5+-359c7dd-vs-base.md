# Results vs. base

- fork: python
- ref: 359c7dde3bb074e02968
- machine: linux-aarch64
- commit hash: 359c7dd
- commit date: 2025-02-16
- overall geometric mean: 1.152x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.14x slower
- Memory change: 1.21x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250216-3.14.0a5+-359c7dd/bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd.json | results/bm-20250216-3.14.0a5+-359c7dd-NOGIL/bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 304 ms                                                                                                              | 377 ms: 1.24x slower                                                                                                      |
| docutils       | 3.01 sec                                                                                                            | 3.32 sec: 1.10x slower                                                                                                    |
| html5lib       | 62.1 ms                                                                                                             | 75.3 ms: 1.21x slower                                                                                                     |
| sphinx         | 1.17 sec                                                                                                            | 1.35 sec: 1.16x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                               | 1.18x slower                                                                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | results/bm-20250216-3.14.0a5+-359c7dd/bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd.json | results/bm-20250216-3.14.0a5+-359c7dd-NOGIL/bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd.json |
|-------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| async_tree_io           | 942 ms                                                                                                              | 974 ms: 1.03x slower                                                                                                      |
| async_tree_none_tg      | 403 ms                                                                                                              | 419 ms: 1.04x slower                                                                                                      |
| async_tree_cpu_io_mixed | 686 ms                                                                                                              | 721 ms: 1.05x slower                                                                                                      |
| async_tree_memoization  | 502 ms                                                                                                              | 549 ms: 1.09x slower                                                                                                      |
| asyncio_tcp             | 550 ms                                                                                                              | 619 ms: 1.13x slower                                                                                                      |
| async_tree_none         | 401 ms                                                                                                              | 452 ms: 1.13x slower                                                                                                      |
| asyncio_tcp_ssl         | 2.24 sec                                                                                                            | 2.57 sec: 1.15x slower                                                                                                    |
| async_generators        | 454 ms                                                                                                              | 530 ms: 1.17x slower                                                                                                      |
| Geometric mean          | (ref)                                                                                                               | 1.07x slower                                                                                                              |

Benchmark hidden because not significant (5): async_tree_io_tg, async_tree_cpu_io_mixed_tg, asyncio_websockets, async_tree_memoization_tg, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250216-3.14.0a5+-359c7dd/bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd.json | results/bm-20250216-3.14.0a5+-359c7dd-NOGIL/bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| float          | 88.3 ms                                                                                                             | 101 ms: 1.14x slower                                                                                                      |
| nbody          | 121 ms                                                                                                              | 185 ms: 1.52x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                               | 1.20x slower                                                                                                              |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250216-3.14.0a5+-359c7dd/bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd.json | results/bm-20250216-3.14.0a5+-359c7dd-NOGIL/bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                                                                              | 165 ms: 1.28x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                               | 1.04x slower                                                                                                              |

Benchmark hidden because not significant (3): regex_effbot, regex_v8, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250216-3.14.0a5+-359c7dd/bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd.json | results/bm-20250216-3.14.0a5+-359c7dd-NOGIL/bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd.json |
|----------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| xml_etree_iterparse  | 145 ms                                                                                                              | 130 ms: 1.11x faster                                                                                                      |
| pickle_dict          | 39.5 us                                                                                                             | 41.0 us: 1.04x slower                                                                                                     |
| json_dumps           | 15.2 ms                                                                                                             | 17.1 ms: 1.12x slower                                                                                                     |
| pickle_pure_python   | 409 us                                                                                                              | 460 us: 1.12x slower                                                                                                      |
| unpickle_list        | 6.44 us                                                                                                             | 7.42 us: 1.15x slower                                                                                                     |
| unpickle             | 17.8 us                                                                                                             | 21.0 us: 1.18x slower                                                                                                     |
| unpickle_pure_python | 263 us                                                                                                              | 319 us: 1.21x slower                                                                                                      |
| xml_etree_process    | 83.2 ms                                                                                                             | 101 ms: 1.22x slower                                                                                                      |
| xml_etree_generate   | 113 ms                                                                                                              | 139 ms: 1.23x slower                                                                                                      |
| tomli_loads          | 2.58 sec                                                                                                            | 3.23 sec: 1.25x slower                                                                                                    |
| Geometric mean       | (ref)                                                                                                               | 1.10x slower                                                                                                              |

Benchmark hidden because not significant (4): pickle, xml_etree_parse, pickle_list, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20250216-3.14.0a5+-359c7dd/bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd.json | results/bm-20250216-3.14.0a5+-359c7dd-NOGIL/bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd.json |
|------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 16.3 ms                                                                                                             | 20.1 ms: 1.24x slower                                                                                                     |
| python_startup_no_site | 9.08 ms                                                                                                             | 12.2 ms: 1.35x slower                                                                                                     |
| Geometric mean         | (ref)                                                                                                               | 1.29x slower                                                                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20250216-3.14.0a5+-359c7dd/bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd.json | results/bm-20250216-3.14.0a5+-359c7dd-NOGIL/bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd.json |
|-----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| genshi_xml      | 61.9 ms                                                                                                             | 78.7 ms: 1.27x slower                                                                                                     |
| genshi_text     | 27.3 ms                                                                                                             | 36.8 ms: 1.35x slower                                                                                                     |
| django_template | 39.0 ms                                                                                                             | 54.6 ms: 1.40x slower                                                                                                     |
| mako            | 14.1 ms                                                                                                             | 22.4 ms: 1.58x slower                                                                                                     |
| Geometric mean  | (ref)                                                                                                               | 1.39x slower                                                                                                              |

All benchmarks:
===============

| Benchmark                | results/bm-20250216-3.14.0a5+-359c7dd/bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd.json | results/bm-20250216-3.14.0a5+-359c7dd-NOGIL/bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd.json |
|--------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| bench_mp_pool            | 5.29 sec                                                                                                            | 58.8 ms: 89.93x faster                                                                                                    |
| gc_traversal             | 7.03 ms                                                                                                             | 2.78 ms: 2.53x faster                                                                                                     |
| create_gc_cycles         | 3.57 ms                                                                                                             | 2.22 ms: 1.61x faster                                                                                                     |
| xml_etree_iterparse      | 145 ms                                                                                                              | 130 ms: 1.11x faster                                                                                                      |
| async_tree_io            | 942 ms                                                                                                              | 974 ms: 1.03x slower                                                                                                      |
| pickle_dict              | 39.5 us                                                                                                             | 41.0 us: 1.04x slower                                                                                                     |
| async_tree_none_tg       | 403 ms                                                                                                              | 419 ms: 1.04x slower                                                                                                      |
| async_tree_cpu_io_mixed  | 686 ms                                                                                                              | 721 ms: 1.05x slower                                                                                                      |
| json                     | 6.06 ms                                                                                                             | 6.50 ms: 1.07x slower                                                                                                     |
| async_tree_memoization   | 502 ms                                                                                                              | 549 ms: 1.09x slower                                                                                                      |
| docutils                 | 3.01 sec                                                                                                            | 3.32 sec: 1.10x slower                                                                                                    |
| k_core                   | 2.86 sec                                                                                                            | 3.18 sec: 1.11x slower                                                                                                    |
| mdp                      | 3.46 sec                                                                                                            | 3.86 sec: 1.11x slower                                                                                                    |
| pycparser                | 1.29 sec                                                                                                            | 1.44 sec: 1.12x slower                                                                                                    |
| logging_silent           | 139 ns                                                                                                              | 156 ns: 1.12x slower                                                                                                      |
| json_dumps               | 15.2 ms                                                                                                             | 17.1 ms: 1.12x slower                                                                                                     |
| pickle_pure_python       | 409 us                                                                                                              | 460 us: 1.12x slower                                                                                                      |
| asyncio_tcp              | 550 ms                                                                                                              | 619 ms: 1.13x slower                                                                                                      |
| async_tree_none          | 401 ms                                                                                                              | 452 ms: 1.13x slower                                                                                                      |
| scimark_sor              | 157 ms                                                                                                              | 178 ms: 1.13x slower                                                                                                      |
| pyflate                  | 590 ms                                                                                                              | 671 ms: 1.14x slower                                                                                                      |
| unpack_sequence          | 67.7 ns                                                                                                             | 77.3 ns: 1.14x slower                                                                                                     |
| float                    | 88.3 ms                                                                                                             | 101 ms: 1.14x slower                                                                                                      |
| asyncio_tcp_ssl          | 2.24 sec                                                                                                            | 2.57 sec: 1.15x slower                                                                                                    |
| dulwich_log              | 61.1 ms                                                                                                             | 70.4 ms: 1.15x slower                                                                                                     |
| unpickle_list            | 6.44 us                                                                                                             | 7.42 us: 1.15x slower                                                                                                     |
| sphinx                   | 1.17 sec                                                                                                            | 1.35 sec: 1.16x slower                                                                                                    |
| scimark_fft              | 420 ms                                                                                                              | 487 ms: 1.16x slower                                                                                                      |
| spectral_norm            | 123 ms                                                                                                              | 142 ms: 1.16x slower                                                                                                      |
| async_generators         | 454 ms                                                                                                              | 530 ms: 1.17x slower                                                                                                      |
| generators               | 36.7 ms                                                                                                             | 43.0 ms: 1.17x slower                                                                                                     |
| unpickle                 | 17.8 us                                                                                                             | 21.0 us: 1.18x slower                                                                                                     |
| pprint_safe_repr         | 969 ms                                                                                                              | 1.16 sec: 1.19x slower                                                                                                    |
| pprint_pformat           | 1.98 sec                                                                                                            | 2.37 sec: 1.20x slower                                                                                                    |
| logging_simple           | 7.25 us                                                                                                             | 8.75 us: 1.21x slower                                                                                                     |
| unpickle_pure_python     | 263 us                                                                                                              | 319 us: 1.21x slower                                                                                                      |
| hexiom                   | 7.47 ms                                                                                                             | 9.06 ms: 1.21x slower                                                                                                     |
| html5lib                 | 62.1 ms                                                                                                             | 75.3 ms: 1.21x slower                                                                                                     |
| xml_etree_process        | 83.2 ms                                                                                                             | 101 ms: 1.22x slower                                                                                                      |
| deepcopy_reduce          | 3.71 us                                                                                                             | 4.51 us: 1.22x slower                                                                                                     |
| connected_components     | 553 ms                                                                                                              | 674 ms: 1.22x slower                                                                                                      |
| sqlglot_normalize        | 127 ms                                                                                                              | 155 ms: 1.22x slower                                                                                                      |
| shortest_path            | 568 ms                                                                                                              | 696 ms: 1.22x slower                                                                                                      |
| deepcopy                 | 345 us                                                                                                              | 423 us: 1.23x slower                                                                                                      |
| xml_etree_generate       | 113 ms                                                                                                              | 139 ms: 1.23x slower                                                                                                      |
| 2to3                     | 304 ms                                                                                                              | 377 ms: 1.24x slower                                                                                                      |
| python_startup           | 16.3 ms                                                                                                             | 20.1 ms: 1.24x slower                                                                                                     |
| subparsers               | 26.1 ms                                                                                                             | 32.4 ms: 1.24x slower                                                                                                     |
| sqlglot_optimize         | 61.3 ms                                                                                                             | 76.5 ms: 1.25x slower                                                                                                     |
| pylint                   | 305 ms                                                                                                              | 382 ms: 1.25x slower                                                                                                      |
| logging_format           | 7.96 us                                                                                                             | 9.96 us: 1.25x slower                                                                                                     |
| tomli_loads              | 2.58 sec                                                                                                            | 3.23 sec: 1.25x slower                                                                                                    |
| deepcopy_memo            | 41.0 us                                                                                                             | 51.6 us: 1.26x slower                                                                                                     |
| telco                    | 9.51 ms                                                                                                             | 12.0 ms: 1.27x slower                                                                                                     |
| go                       | 141 ms                                                                                                              | 178 ms: 1.27x slower                                                                                                      |
| genshi_xml               | 61.9 ms                                                                                                             | 78.7 ms: 1.27x slower                                                                                                     |
| scimark_sparse_mat_mult  | 6.45 ms                                                                                                             | 8.22 ms: 1.27x slower                                                                                                     |
| comprehensions           | 21.2 us                                                                                                             | 27.0 us: 1.28x slower                                                                                                     |
| coverage                 | 99.5 ms                                                                                                             | 127 ms: 1.28x slower                                                                                                      |
| regex_compile            | 129 ms                                                                                                              | 165 ms: 1.28x slower                                                                                                      |
| many_optionals           | 841 us                                                                                                              | 1.08 ms: 1.28x slower                                                                                                     |
| thrift                   | 949 us                                                                                                              | 1.22 ms: 1.29x slower                                                                                                     |
| sympy_expand             | 466 ms                                                                                                              | 605 ms: 1.30x slower                                                                                                      |
| sympy_str                | 276 ms                                                                                                              | 359 ms: 1.30x slower                                                                                                      |
| raytrace                 | 325 ms                                                                                                              | 423 ms: 1.30x slower                                                                                                      |
| chaos                    | 69.0 ms                                                                                                             | 90.0 ms: 1.30x slower                                                                                                     |
| nqueens                  | 101 ms                                                                                                              | 133 ms: 1.31x slower                                                                                                      |
| sqlglot_transpile        | 1.86 ms                                                                                                             | 2.45 ms: 1.32x slower                                                                                                     |
| bpe_tokeniser            | 5.57 sec                                                                                                            | 7.35 sec: 1.32x slower                                                                                                    |
| deltablue                | 3.98 ms                                                                                                             | 5.29 ms: 1.33x slower                                                                                                     |
| sqlalchemy_declarative   | 147 ms                                                                                                              | 196 ms: 1.33x slower                                                                                                      |
| scimark_monte_carlo      | 86.9 ms                                                                                                             | 116 ms: 1.33x slower                                                                                                      |
| sympy_integrate          | 21.7 ms                                                                                                             | 29.0 ms: 1.34x slower                                                                                                     |
| sqlglot_parse            | 1.47 ms                                                                                                             | 1.98 ms: 1.34x slower                                                                                                     |
| sympy_sum                | 144 ms                                                                                                              | 194 ms: 1.34x slower                                                                                                      |
| python_startup_no_site   | 9.08 ms                                                                                                             | 12.2 ms: 1.35x slower                                                                                                     |
| genshi_text              | 27.3 ms                                                                                                             | 36.8 ms: 1.35x slower                                                                                                     |
| meteor_contest           | 116 ms                                                                                                              | 157 ms: 1.36x slower                                                                                                      |
| scimark_lu               | 141 ms                                                                                                              | 193 ms: 1.37x slower                                                                                                      |
| richards                 | 52.1 ms                                                                                                             | 71.5 ms: 1.37x slower                                                                                                     |
| crypto_pyaes             | 85.2 ms                                                                                                             | 117 ms: 1.38x slower                                                                                                      |
| fannkuch                 | 494 ms                                                                                                              | 681 ms: 1.38x slower                                                                                                      |
| django_template          | 39.0 ms                                                                                                             | 54.6 ms: 1.40x slower                                                                                                     |
| richards_super           | 62.0 ms                                                                                                             | 87.4 ms: 1.41x slower                                                                                                     |
| typing_runtime_protocols | 201 us                                                                                                              | 287 us: 1.43x slower                                                                                                      |
| bench_thread_pool        | 1.31 ms                                                                                                             | 1.87 ms: 1.43x slower                                                                                                     |
| sqlalchemy_imperative    | 15.0 ms                                                                                                             | 22.2 ms: 1.49x slower                                                                                                     |
| nbody                    | 121 ms                                                                                                              | 185 ms: 1.52x slower                                                                                                      |
| mako                     | 14.1 ms                                                                                                             | 22.4 ms: 1.58x slower                                                                                                     |
| Geometric mean           | (ref)                                                                                                               | 1.12x slower                                                                                                              |

Benchmark hidden because not significant (15): sqlite_synth, regex_effbot, regex_v8, regex_dna, pickle, xml_etree_parse, pidigits, async_tree_io_tg, async_tree_cpu_io_mixed_tg, pickle_list, asyncio_websockets, async_tree_memoization_tg, json_loads, pathlib, coroutines

- Geometric mean (including insignificant results): 1.152x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.16x
- 95% likely to have a slowdown of 1.16x
- 99% likely to have a slowdown of 1.14x

# Memory
- memory change: 1.21x