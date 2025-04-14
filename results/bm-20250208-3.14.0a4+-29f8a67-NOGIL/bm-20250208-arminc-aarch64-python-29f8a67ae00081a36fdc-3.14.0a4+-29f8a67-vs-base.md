# Results vs. base

- fork: python
- ref: 29f8a67ae00081a36fdc
- machine: linux-aarch64
- commit hash: 29f8a67
- commit date: 2025-02-08
- overall geometric mean: 1.160x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x slower
- Memory change: 1.21x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250208-3.14.0a4+-29f8a67/bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json | results/bm-20250208-3.14.0a4+-29f8a67-NOGIL/bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 307 ms                                                                                                              | 388 ms: 1.26x slower                                                                                                      |
| docutils       | 3.01 sec                                                                                                            | 3.39 sec: 1.12x slower                                                                                                    |
| html5lib       | 62.9 ms                                                                                                             | 80.6 ms: 1.28x slower                                                                                                     |
| sphinx         | 1.16 sec                                                                                                            | 1.38 sec: 1.19x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                               | 1.21x slower                                                                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | results/bm-20250208-3.14.0a4+-29f8a67/bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json | results/bm-20250208-3.14.0a4+-29f8a67-NOGIL/bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json |
|-------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| async_tree_io           | 926 ms                                                                                                              | 955 ms: 1.03x slower                                                                                                      |
| async_tree_cpu_io_mixed | 691 ms                                                                                                              | 716 ms: 1.04x slower                                                                                                      |
| async_tree_none_tg      | 392 ms                                                                                                              | 414 ms: 1.06x slower                                                                                                      |
| async_tree_memoization  | 503 ms                                                                                                              | 539 ms: 1.07x slower                                                                                                      |
| async_tree_none         | 403 ms                                                                                                              | 444 ms: 1.10x slower                                                                                                      |
| asyncio_tcp             | 548 ms                                                                                                              | 608 ms: 1.11x slower                                                                                                      |
| asyncio_tcp_ssl         | 2.29 sec                                                                                                            | 2.54 sec: 1.11x slower                                                                                                    |
| async_generators        | 454 ms                                                                                                              | 542 ms: 1.20x slower                                                                                                      |
| Geometric mean          | (ref)                                                                                                               | 1.06x slower                                                                                                              |

Benchmark hidden because not significant (5): async_tree_io_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250208-3.14.0a4+-29f8a67/bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json | results/bm-20250208-3.14.0a4+-29f8a67-NOGIL/bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| float          | 86.5 ms                                                                                                             | 102 ms: 1.18x slower                                                                                                      |
| nbody          | 120 ms                                                                                                              | 183 ms: 1.52x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                               | 1.22x slower                                                                                                              |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250208-3.14.0a4+-29f8a67/bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json | results/bm-20250208-3.14.0a4+-29f8a67-NOGIL/bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| regex_compile  | 127 ms                                                                                                              | 161 ms: 1.27x slower                                                                                                      |
| Geometric mean | (ref)                                                                                                               | 1.06x slower                                                                                                              |

Benchmark hidden because not significant (3): regex_v8, regex_effbot, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250208-3.14.0a4+-29f8a67/bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json | results/bm-20250208-3.14.0a4+-29f8a67-NOGIL/bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json |
|----------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| xml_etree_iterparse  | 159 ms                                                                                                              | 131 ms: 1.21x faster                                                                                                      |
| pickle_dict          | 38.8 us                                                                                                             | 41.2 us: 1.06x slower                                                                                                     |
| json_loads           | 35.3 us                                                                                                             | 39.9 us: 1.13x slower                                                                                                     |
| unpickle_list        | 6.44 us                                                                                                             | 7.44 us: 1.16x slower                                                                                                     |
| unpickle             | 18.1 us                                                                                                             | 20.9 us: 1.16x slower                                                                                                     |
| json_dumps           | 15.0 ms                                                                                                             | 17.7 ms: 1.18x slower                                                                                                     |
| xml_etree_generate   | 114 ms                                                                                                              | 138 ms: 1.22x slower                                                                                                      |
| tomli_loads          | 2.53 sec                                                                                                            | 3.16 sec: 1.25x slower                                                                                                    |
| xml_etree_process    | 82.5 ms                                                                                                             | 103 ms: 1.25x slower                                                                                                      |
| unpickle_pure_python | 266 us                                                                                                              | 333 us: 1.25x slower                                                                                                      |
| pickle_pure_python   | 390 us                                                                                                              | 499 us: 1.28x slower                                                                                                      |
| Geometric mean       | (ref)                                                                                                               | 1.12x slower                                                                                                              |

Benchmark hidden because not significant (3): xml_etree_parse, pickle, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20250208-3.14.0a4+-29f8a67/bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json | results/bm-20250208-3.14.0a4+-29f8a67-NOGIL/bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json |
|------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 16.4 ms                                                                                                             | 20.1 ms: 1.22x slower                                                                                                     |
| python_startup_no_site | 9.05 ms                                                                                                             | 12.3 ms: 1.35x slower                                                                                                     |
| Geometric mean         | (ref)                                                                                                               | 1.29x slower                                                                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20250208-3.14.0a4+-29f8a67/bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json | results/bm-20250208-3.14.0a4+-29f8a67-NOGIL/bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json |
|-----------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| genshi_xml      | 64.4 ms                                                                                                             | 81.1 ms: 1.26x slower                                                                                                     |
| genshi_text     | 27.4 ms                                                                                                             | 37.0 ms: 1.35x slower                                                                                                     |
| django_template | 39.4 ms                                                                                                             | 60.0 ms: 1.52x slower                                                                                                     |
| mako            | 14.0 ms                                                                                                             | 23.4 ms: 1.68x slower                                                                                                     |
| Geometric mean  | (ref)                                                                                                               | 1.44x slower                                                                                                              |

All benchmarks:
===============

| Benchmark                | results/bm-20250208-3.14.0a4+-29f8a67/bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json | results/bm-20250208-3.14.0a4+-29f8a67-NOGIL/bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json |
|--------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------------------------------------------:|
| bench_mp_pool            | 5.97 sec                                                                                                            | 58.5 ms: 101.95x faster                                                                                                   |
| gc_traversal             | 7.01 ms                                                                                                             | 2.75 ms: 2.55x faster                                                                                                     |
| create_gc_cycles         | 3.59 ms                                                                                                             | 2.20 ms: 1.63x faster                                                                                                     |
| xml_etree_iterparse      | 159 ms                                                                                                              | 131 ms: 1.21x faster                                                                                                      |
| sqlite_synth             | 4.12 us                                                                                                             | 3.80 us: 1.09x faster                                                                                                     |
| async_tree_io            | 926 ms                                                                                                              | 955 ms: 1.03x slower                                                                                                      |
| async_tree_cpu_io_mixed  | 691 ms                                                                                                              | 716 ms: 1.04x slower                                                                                                      |
| async_tree_none_tg       | 392 ms                                                                                                              | 414 ms: 1.06x slower                                                                                                      |
| pickle_dict              | 38.8 us                                                                                                             | 41.2 us: 1.06x slower                                                                                                     |
| async_tree_memoization   | 503 ms                                                                                                              | 539 ms: 1.07x slower                                                                                                      |
| json                     | 6.14 ms                                                                                                             | 6.66 ms: 1.08x slower                                                                                                     |
| async_tree_none          | 403 ms                                                                                                              | 444 ms: 1.10x slower                                                                                                      |
| scimark_sor              | 156 ms                                                                                                              | 173 ms: 1.11x slower                                                                                                      |
| pathlib                  | 21.9 ms                                                                                                             | 24.3 ms: 1.11x slower                                                                                                     |
| asyncio_tcp              | 548 ms                                                                                                              | 608 ms: 1.11x slower                                                                                                      |
| asyncio_tcp_ssl          | 2.29 sec                                                                                                            | 2.54 sec: 1.11x slower                                                                                                    |
| docutils                 | 3.01 sec                                                                                                            | 3.39 sec: 1.12x slower                                                                                                    |
| scimark_fft              | 434 ms                                                                                                              | 489 ms: 1.13x slower                                                                                                      |
| json_loads               | 35.3 us                                                                                                             | 39.9 us: 1.13x slower                                                                                                     |
| logging_silent           | 136 ns                                                                                                              | 154 ns: 1.13x slower                                                                                                      |
| mdp                      | 3.35 sec                                                                                                            | 3.83 sec: 1.14x slower                                                                                                    |
| pycparser                | 1.28 sec                                                                                                            | 1.47 sec: 1.15x slower                                                                                                    |
| k_core                   | 2.85 sec                                                                                                            | 3.28 sec: 1.15x slower                                                                                                    |
| unpickle_list            | 6.44 us                                                                                                             | 7.44 us: 1.16x slower                                                                                                     |
| unpickle                 | 18.1 us                                                                                                             | 20.9 us: 1.16x slower                                                                                                     |
| generators               | 36.8 ms                                                                                                             | 42.5 ms: 1.16x slower                                                                                                     |
| json_dumps               | 15.0 ms                                                                                                             | 17.7 ms: 1.18x slower                                                                                                     |
| float                    | 86.5 ms                                                                                                             | 102 ms: 1.18x slower                                                                                                      |
| sqlglot_normalize        | 131 ms                                                                                                              | 155 ms: 1.18x slower                                                                                                      |
| sphinx                   | 1.16 sec                                                                                                            | 1.38 sec: 1.19x slower                                                                                                    |
| spectral_norm            | 119 ms                                                                                                              | 142 ms: 1.19x slower                                                                                                      |
| async_generators         | 454 ms                                                                                                              | 542 ms: 1.20x slower                                                                                                      |
| dulwich_log              | 59.9 ms                                                                                                             | 72.0 ms: 1.20x slower                                                                                                     |
| logging_format           | 8.09 us                                                                                                             | 9.73 us: 1.20x slower                                                                                                     |
| pprint_pformat           | 1.97 sec                                                                                                            | 2.38 sec: 1.21x slower                                                                                                    |
| pyflate                  | 552 ms                                                                                                              | 671 ms: 1.22x slower                                                                                                      |
| xml_etree_generate       | 114 ms                                                                                                              | 138 ms: 1.22x slower                                                                                                      |
| pprint_safe_repr         | 953 ms                                                                                                              | 1.16 sec: 1.22x slower                                                                                                    |
| shortest_path            | 572 ms                                                                                                              | 698 ms: 1.22x slower                                                                                                      |
| scimark_sparse_mat_mult  | 6.38 ms                                                                                                             | 7.80 ms: 1.22x slower                                                                                                     |
| python_startup           | 16.4 ms                                                                                                             | 20.1 ms: 1.22x slower                                                                                                     |
| connected_components     | 540 ms                                                                                                              | 663 ms: 1.23x slower                                                                                                      |
| logging_simple           | 7.29 us                                                                                                             | 8.97 us: 1.23x slower                                                                                                     |
| telco                    | 9.46 ms                                                                                                             | 11.7 ms: 1.24x slower                                                                                                     |
| go                       | 140 ms                                                                                                              | 174 ms: 1.25x slower                                                                                                      |
| tomli_loads              | 2.53 sec                                                                                                            | 3.16 sec: 1.25x slower                                                                                                    |
| xml_etree_process        | 82.5 ms                                                                                                             | 103 ms: 1.25x slower                                                                                                      |
| unpickle_pure_python     | 266 us                                                                                                              | 333 us: 1.25x slower                                                                                                      |
| deepcopy                 | 339 us                                                                                                              | 427 us: 1.26x slower                                                                                                      |
| comprehensions           | 21.5 us                                                                                                             | 27.0 us: 1.26x slower                                                                                                     |
| genshi_xml               | 64.4 ms                                                                                                             | 81.1 ms: 1.26x slower                                                                                                     |
| many_optionals           | 841 us                                                                                                              | 1.06 ms: 1.26x slower                                                                                                     |
| 2to3                     | 307 ms                                                                                                              | 388 ms: 1.26x slower                                                                                                      |
| deepcopy_reduce          | 3.72 us                                                                                                             | 4.72 us: 1.27x slower                                                                                                     |
| pylint                   | 304 ms                                                                                                              | 385 ms: 1.27x slower                                                                                                      |
| chaos                    | 69.9 ms                                                                                                             | 88.7 ms: 1.27x slower                                                                                                     |
| regex_compile            | 127 ms                                                                                                              | 161 ms: 1.27x slower                                                                                                      |
| hexiom                   | 7.46 ms                                                                                                             | 9.48 ms: 1.27x slower                                                                                                     |
| thrift                   | 994 us                                                                                                              | 1.26 ms: 1.27x slower                                                                                                     |
| pickle_pure_python       | 390 us                                                                                                              | 499 us: 1.28x slower                                                                                                      |
| sqlglot_optimize         | 60.8 ms                                                                                                             | 77.9 ms: 1.28x slower                                                                                                     |
| html5lib                 | 62.9 ms                                                                                                             | 80.6 ms: 1.28x slower                                                                                                     |
| unpack_sequence          | 67.8 ns                                                                                                             | 87.0 ns: 1.28x slower                                                                                                     |
| subparsers               | 25.9 ms                                                                                                             | 33.4 ms: 1.29x slower                                                                                                     |
| nqueens                  | 101 ms                                                                                                              | 130 ms: 1.29x slower                                                                                                      |
| coverage                 | 104 ms                                                                                                              | 135 ms: 1.30x slower                                                                                                      |
| sympy_integrate          | 21.6 ms                                                                                                             | 28.0 ms: 1.30x slower                                                                                                     |
| scimark_monte_carlo      | 86.5 ms                                                                                                             | 113 ms: 1.30x slower                                                                                                      |
| raytrace                 | 323 ms                                                                                                              | 423 ms: 1.31x slower                                                                                                      |
| crypto_pyaes             | 86.6 ms                                                                                                             | 114 ms: 1.31x slower                                                                                                      |
| bpe_tokeniser            | 5.58 sec                                                                                                            | 7.33 sec: 1.31x slower                                                                                                    |
| sympy_sum                | 144 ms                                                                                                              | 191 ms: 1.33x slower                                                                                                      |
| sympy_expand             | 462 ms                                                                                                              | 616 ms: 1.33x slower                                                                                                      |
| sqlglot_transpile        | 1.82 ms                                                                                                             | 2.43 ms: 1.34x slower                                                                                                     |
| sqlalchemy_declarative   | 145 ms                                                                                                              | 195 ms: 1.34x slower                                                                                                      |
| genshi_text              | 27.4 ms                                                                                                             | 37.0 ms: 1.35x slower                                                                                                     |
| meteor_contest           | 114 ms                                                                                                              | 154 ms: 1.35x slower                                                                                                      |
| scimark_lu               | 142 ms                                                                                                              | 193 ms: 1.35x slower                                                                                                      |
| python_startup_no_site   | 9.05 ms                                                                                                             | 12.3 ms: 1.35x slower                                                                                                     |
| deepcopy_memo            | 40.6 us                                                                                                             | 55.2 us: 1.36x slower                                                                                                     |
| sqlglot_parse            | 1.41 ms                                                                                                             | 1.96 ms: 1.39x slower                                                                                                     |
| sympy_str                | 261 ms                                                                                                              | 364 ms: 1.39x slower                                                                                                      |
| richards                 | 52.8 ms                                                                                                             | 74.5 ms: 1.41x slower                                                                                                     |
| fannkuch                 | 486 ms                                                                                                              | 688 ms: 1.41x slower                                                                                                      |
| richards_super           | 60.3 ms                                                                                                             | 85.9 ms: 1.42x slower                                                                                                     |
| bench_thread_pool        | 1.33 ms                                                                                                             | 1.90 ms: 1.43x slower                                                                                                     |
| typing_runtime_protocols | 196 us                                                                                                              | 281 us: 1.43x slower                                                                                                      |
| sqlalchemy_imperative    | 15.4 ms                                                                                                             | 22.4 ms: 1.46x slower                                                                                                     |
| django_template          | 39.4 ms                                                                                                             | 60.0 ms: 1.52x slower                                                                                                     |
| nbody                    | 120 ms                                                                                                              | 183 ms: 1.52x slower                                                                                                      |
| deltablue                | 3.93 ms                                                                                                             | 6.09 ms: 1.55x slower                                                                                                     |
| mako                     | 14.0 ms                                                                                                             | 23.4 ms: 1.68x slower                                                                                                     |
| Geometric mean           | (ref)                                                                                                               | 1.14x slower                                                                                                              |

Benchmark hidden because not significant (12): xml_etree_parse, regex_v8, regex_effbot, async_tree_io_tg, pidigits, async_tree_memoization_tg, pickle, async_tree_cpu_io_mixed_tg, asyncio_websockets, regex_dna, coroutines, pickle_list

- Geometric mean (including insignificant results): 1.160x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.18x
- 95% likely to have a slowdown of 1.17x
- 99% likely to have a slowdown of 1.16x

# Memory
- memory change: 1.21x