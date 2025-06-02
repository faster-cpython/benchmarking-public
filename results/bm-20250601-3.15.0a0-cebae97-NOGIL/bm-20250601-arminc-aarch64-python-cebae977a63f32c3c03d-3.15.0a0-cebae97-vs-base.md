# Results vs. base

- fork: python
- ref: cebae977a63f32c3c03d
- machine: linux-aarch64
- commit hash: cebae97
- commit date: 2025-06-01
- overall geometric mean: 1.045x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.13x slower
- Memory change: 1.23x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250601-3.15.0a0-cebae97/bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json | results/bm-20250601-3.15.0a0-cebae97-NOGIL/bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 356 ms                                                                                                            | 443 ms: 1.24x slower                                                                                                    |
| docutils       | 3.45 sec                                                                                                          | 3.90 sec: 1.13x slower                                                                                                  |
| html5lib       | 67.3 ms                                                                                                           | 82.9 ms: 1.23x slower                                                                                                   |
| sphinx         | 1.36 sec                                                                                                          | 1.59 sec: 1.18x slower                                                                                                  |
| Geometric mean | (ref)                                                                                                             | 1.20x slower                                                                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | results/bm-20250601-3.15.0a0-cebae97/bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json | results/bm-20250601-3.15.0a0-cebae97-NOGIL/bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json |
|-------------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| async_tree_io_tg        | 1.02 sec                                                                                                          | 992 ms: 1.03x faster                                                                                                    |
| async_tree_io           | 987 ms                                                                                                            | 1.01 sec: 1.03x slower                                                                                                  |
| async_tree_none         | 441 ms                                                                                                            | 469 ms: 1.06x slower                                                                                                    |
| async_tree_memoization  | 525 ms                                                                                                            | 560 ms: 1.07x slower                                                                                                    |
| async_tree_cpu_io_mixed | 808 ms                                                                                                            | 863 ms: 1.07x slower                                                                                                    |
| asyncio_tcp             | 556 ms                                                                                                            | 625 ms: 1.12x slower                                                                                                    |
| asyncio_tcp_ssl         | 2.25 sec                                                                                                          | 2.53 sec: 1.13x slower                                                                                                  |
| coroutines              | 33.1 ms                                                                                                           | 38.2 ms: 1.15x slower                                                                                                   |
| async_generators        | 521 ms                                                                                                            | 632 ms: 1.21x slower                                                                                                    |
| Geometric mean          | (ref)                                                                                                             | 1.06x slower                                                                                                            |

Benchmark hidden because not significant (4): async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, asyncio_websockets, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250601-3.15.0a0-cebae97/bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json | results/bm-20250601-3.15.0a0-cebae97-NOGIL/bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| float          | 96.5 ms                                                                                                           | 106 ms: 1.09x slower                                                                                                    |
| nbody          | 144 ms                                                                                                            | 191 ms: 1.33x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                             | 1.14x slower                                                                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250601-3.15.0a0-cebae97/bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json | results/bm-20250601-3.15.0a0-cebae97-NOGIL/bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| regex_dna      | 226 ms                                                                                                            | 231 ms: 1.02x slower                                                                                                    |
| regex_compile  | 158 ms                                                                                                            | 197 ms: 1.25x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                             | 1.06x slower                                                                                                            |

Benchmark hidden because not significant (2): regex_v8, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250601-3.15.0a0-cebae97/bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json | results/bm-20250601-3.15.0a0-cebae97-NOGIL/bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json |
|----------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| xml_etree_iterparse  | 167 ms                                                                                                            | 156 ms: 1.07x faster                                                                                                    |
| xml_etree_parse      | 229 ms                                                                                                            | 232 ms: 1.01x slower                                                                                                    |
| pickle_dict          | 42.6 us                                                                                                           | 45.7 us: 1.07x slower                                                                                                   |
| unpickle_list        | 6.91 us                                                                                                           | 7.78 us: 1.13x slower                                                                                                   |
| json_dumps           | 17.2 ms                                                                                                           | 19.8 ms: 1.15x slower                                                                                                   |
| unpickle             | 22.6 us                                                                                                           | 26.5 us: 1.17x slower                                                                                                   |
| json_loads           | 38.0 us                                                                                                           | 44.6 us: 1.17x slower                                                                                                   |
| xml_etree_process    | 108 ms                                                                                                            | 129 ms: 1.20x slower                                                                                                    |
| pickle_pure_python   | 474 us                                                                                                            | 569 us: 1.20x slower                                                                                                    |
| xml_etree_generate   | 161 ms                                                                                                            | 193 ms: 1.20x slower                                                                                                    |
| unpickle_pure_python | 328 us                                                                                                            | 402 us: 1.23x slower                                                                                                    |
| tomli_loads          | 2.93 sec                                                                                                          | 3.61 sec: 1.23x slower                                                                                                  |
| Geometric mean       | (ref)                                                                                                             | 1.12x slower                                                                                                            |

Benchmark hidden because not significant (2): pickle_list, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20250601-3.15.0a0-cebae97/bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json | results/bm-20250601-3.15.0a0-cebae97-NOGIL/bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json |
|------------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 17.2 ms                                                                                                           | 22.9 ms: 1.33x slower                                                                                                   |
| python_startup_no_site | 9.71 ms                                                                                                           | 13.7 ms: 1.41x slower                                                                                                   |
| Geometric mean         | (ref)                                                                                                             | 1.37x slower                                                                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20250601-3.15.0a0-cebae97/bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json | results/bm-20250601-3.15.0a0-cebae97-NOGIL/bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json |
|-----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| genshi_xml      | 74.7 ms                                                                                                           | 97.2 ms: 1.30x slower                                                                                                   |
| mako            | 17.9 ms                                                                                                           | 23.7 ms: 1.32x slower                                                                                                   |
| genshi_text     | 34.4 ms                                                                                                           | 45.5 ms: 1.32x slower                                                                                                   |
| django_template | 52.5 ms                                                                                                           | 74.2 ms: 1.41x slower                                                                                                   |
| Geometric mean  | (ref)                                                                                                             | 1.34x slower                                                                                                            |

All benchmarks:
===============

| Benchmark                | results/bm-20250601-3.15.0a0-cebae97/bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json | results/bm-20250601-3.15.0a0-cebae97-NOGIL/bm-20250601-arminc-aarch64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json |
|--------------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| thrift                   | 199 ms                                                                                                            | 1.63 ms: 121.97x faster                                                                                                 |
| bench_mp_pool            | 5.59 sec                                                                                                          | 72.0 ms: 77.63x faster                                                                                                  |
| coverage                 | 739 ms                                                                                                            | 184 ms: 4.01x faster                                                                                                    |
| gc_traversal             | 7.69 ms                                                                                                           | 3.68 ms: 2.09x faster                                                                                                   |
| create_gc_cycles         | 3.97 ms                                                                                                           | 2.45 ms: 1.62x faster                                                                                                   |
| sqlite_synth             | 4.81 us                                                                                                           | 4.43 us: 1.08x faster                                                                                                   |
| xml_etree_iterparse      | 167 ms                                                                                                            | 156 ms: 1.07x faster                                                                                                    |
| async_tree_io_tg         | 1.02 sec                                                                                                          | 992 ms: 1.03x faster                                                                                                    |
| xml_etree_parse          | 229 ms                                                                                                            | 232 ms: 1.01x slower                                                                                                    |
| regex_dna                | 226 ms                                                                                                            | 231 ms: 1.02x slower                                                                                                    |
| async_tree_io            | 987 ms                                                                                                            | 1.01 sec: 1.03x slower                                                                                                  |
| async_tree_none          | 441 ms                                                                                                            | 469 ms: 1.06x slower                                                                                                    |
| async_tree_memoization   | 525 ms                                                                                                            | 560 ms: 1.07x slower                                                                                                    |
| async_tree_cpu_io_mixed  | 808 ms                                                                                                            | 863 ms: 1.07x slower                                                                                                    |
| pickle_dict              | 42.6 us                                                                                                           | 45.7 us: 1.07x slower                                                                                                   |
| pathlib                  | 26.9 ms                                                                                                           | 29.2 ms: 1.09x slower                                                                                                   |
| float                    | 96.5 ms                                                                                                           | 106 ms: 1.09x slower                                                                                                    |
| asyncio_tcp              | 556 ms                                                                                                            | 625 ms: 1.12x slower                                                                                                    |
| unpickle_list            | 6.91 us                                                                                                           | 7.78 us: 1.13x slower                                                                                                   |
| asyncio_tcp_ssl          | 2.25 sec                                                                                                          | 2.53 sec: 1.13x slower                                                                                                  |
| k_core                   | 2.93 sec                                                                                                          | 3.31 sec: 1.13x slower                                                                                                  |
| docutils                 | 3.45 sec                                                                                                          | 3.90 sec: 1.13x slower                                                                                                  |
| pycparser                | 1.49 sec                                                                                                          | 1.71 sec: 1.14x slower                                                                                                  |
| json_dumps               | 17.2 ms                                                                                                           | 19.8 ms: 1.15x slower                                                                                                   |
| scimark_sor              | 173 ms                                                                                                            | 200 ms: 1.15x slower                                                                                                    |
| coroutines               | 33.1 ms                                                                                                           | 38.2 ms: 1.15x slower                                                                                                   |
| pyflate                  | 590 ms                                                                                                            | 682 ms: 1.16x slower                                                                                                    |
| scimark_sparse_mat_mult  | 7.78 ms                                                                                                           | 9.08 ms: 1.17x slower                                                                                                   |
| json                     | 6.95 ms                                                                                                           | 8.12 ms: 1.17x slower                                                                                                   |
| unpickle                 | 22.6 us                                                                                                           | 26.5 us: 1.17x slower                                                                                                   |
| json_loads               | 38.0 us                                                                                                           | 44.6 us: 1.17x slower                                                                                                   |
| sphinx                   | 1.36 sec                                                                                                          | 1.59 sec: 1.18x slower                                                                                                  |
| hexiom                   | 8.37 ms                                                                                                           | 9.83 ms: 1.18x slower                                                                                                   |
| fannkuch                 | 596 ms                                                                                                            | 701 ms: 1.18x slower                                                                                                    |
| pprint_safe_repr         | 1.35 sec                                                                                                          | 1.59 sec: 1.18x slower                                                                                                  |
| connected_components     | 570 ms                                                                                                            | 673 ms: 1.18x slower                                                                                                    |
| scimark_fft              | 500 ms                                                                                                            | 590 ms: 1.18x slower                                                                                                    |
| pprint_pformat           | 2.76 sec                                                                                                          | 3.27 sec: 1.19x slower                                                                                                  |
| shortest_path            | 599 ms                                                                                                            | 717 ms: 1.20x slower                                                                                                    |
| xml_etree_process        | 108 ms                                                                                                            | 129 ms: 1.20x slower                                                                                                    |
| pickle_pure_python       | 474 us                                                                                                            | 569 us: 1.20x slower                                                                                                    |
| xml_etree_generate       | 161 ms                                                                                                            | 193 ms: 1.20x slower                                                                                                    |
| generators               | 39.6 ms                                                                                                           | 47.8 ms: 1.21x slower                                                                                                   |
| dulwich_log              | 65.6 ms                                                                                                           | 79.3 ms: 1.21x slower                                                                                                   |
| async_generators         | 521 ms                                                                                                            | 632 ms: 1.21x slower                                                                                                    |
| scimark_lu               | 184 ms                                                                                                            | 225 ms: 1.22x slower                                                                                                    |
| unpickle_pure_python     | 328 us                                                                                                            | 402 us: 1.23x slower                                                                                                    |
| chaos                    | 83.8 ms                                                                                                           | 103 ms: 1.23x slower                                                                                                    |
| pylint                   | 374 ms                                                                                                            | 459 ms: 1.23x slower                                                                                                    |
| deltablue                | 4.54 ms                                                                                                           | 5.57 ms: 1.23x slower                                                                                                   |
| tomli_loads              | 2.93 sec                                                                                                          | 3.61 sec: 1.23x slower                                                                                                  |
| nqueens                  | 125 ms                                                                                                            | 155 ms: 1.23x slower                                                                                                    |
| html5lib                 | 67.3 ms                                                                                                           | 82.9 ms: 1.23x slower                                                                                                   |
| meteor_contest           | 127 ms                                                                                                            | 157 ms: 1.23x slower                                                                                                    |
| logging_simple           | 9.31 us                                                                                                           | 11.5 us: 1.24x slower                                                                                                   |
| 2to3                     | 356 ms                                                                                                            | 443 ms: 1.24x slower                                                                                                    |
| logging_format           | 10.3 us                                                                                                           | 12.8 us: 1.24x slower                                                                                                   |
| regex_compile            | 158 ms                                                                                                            | 197 ms: 1.25x slower                                                                                                    |
| sqlglot_v2_normalize     | 165 ms                                                                                                            | 206 ms: 1.25x slower                                                                                                    |
| many_optionals           | 1.10 ms                                                                                                           | 1.37 ms: 1.25x slower                                                                                                   |
| go                       | 141 ms                                                                                                            | 176 ms: 1.25x slower                                                                                                    |
| subparsers               | 36.8 ms                                                                                                           | 46.2 ms: 1.26x slower                                                                                                   |
| spectral_norm            | 151 ms                                                                                                            | 190 ms: 1.26x slower                                                                                                    |
| mdp                      | 2.01 sec                                                                                                          | 2.55 sec: 1.27x slower                                                                                                  |
| raytrace                 | 390 ms                                                                                                            | 498 ms: 1.28x slower                                                                                                    |
| sqlglot_v2_optimize      | 75.7 ms                                                                                                           | 97.3 ms: 1.29x slower                                                                                                   |
| deepcopy_reduce          | 4.61 us                                                                                                           | 6.01 us: 1.30x slower                                                                                                   |
| sqlglot_v2_transpile     | 2.14 ms                                                                                                           | 2.79 ms: 1.30x slower                                                                                                   |
| genshi_xml               | 74.7 ms                                                                                                           | 97.2 ms: 1.30x slower                                                                                                   |
| comprehensions           | 23.1 us                                                                                                           | 30.2 us: 1.30x slower                                                                                                   |
| deepcopy_memo            | 43.7 us                                                                                                           | 57.2 us: 1.31x slower                                                                                                   |
| bpe_tokeniser            | 6.64 sec                                                                                                          | 8.69 sec: 1.31x slower                                                                                                  |
| logging_silent           | 914 ns                                                                                                            | 1.20 us: 1.31x slower                                                                                                   |
| sympy_expand             | 599 ms                                                                                                            | 785 ms: 1.31x slower                                                                                                    |
| sqlglot_v2_parse         | 1.73 ms                                                                                                           | 2.27 ms: 1.31x slower                                                                                                   |
| mako                     | 17.9 ms                                                                                                           | 23.7 ms: 1.32x slower                                                                                                   |
| sympy_integrate          | 23.9 ms                                                                                                           | 31.6 ms: 1.32x slower                                                                                                   |
| deepcopy                 | 401 us                                                                                                            | 530 us: 1.32x slower                                                                                                    |
| unpack_sequence          | 56.4 ns                                                                                                           | 74.5 ns: 1.32x slower                                                                                                   |
| genshi_text              | 34.4 ms                                                                                                           | 45.5 ms: 1.32x slower                                                                                                   |
| nbody                    | 144 ms                                                                                                            | 191 ms: 1.33x slower                                                                                                    |
| sympy_str                | 339 ms                                                                                                            | 450 ms: 1.33x slower                                                                                                    |
| python_startup           | 17.2 ms                                                                                                           | 22.9 ms: 1.33x slower                                                                                                   |
| sympy_sum                | 178 ms                                                                                                            | 240 ms: 1.35x slower                                                                                                    |
| bench_thread_pool        | 1.48 ms                                                                                                           | 2.00 ms: 1.35x slower                                                                                                   |
| telco                    | 13.2 ms                                                                                                           | 17.9 ms: 1.35x slower                                                                                                   |
| typing_runtime_protocols | 260 us                                                                                                            | 354 us: 1.36x slower                                                                                                    |
| richards                 | 62.9 ms                                                                                                           | 87.3 ms: 1.39x slower                                                                                                   |
| crypto_pyaes             | 105 ms                                                                                                            | 147 ms: 1.39x slower                                                                                                    |
| scimark_monte_carlo      | 94.8 ms                                                                                                           | 133 ms: 1.40x slower                                                                                                    |
| richards_super           | 71.2 ms                                                                                                           | 100 ms: 1.41x slower                                                                                                    |
| django_template          | 52.5 ms                                                                                                           | 74.2 ms: 1.41x slower                                                                                                   |
| python_startup_no_site   | 9.71 ms                                                                                                           | 13.7 ms: 1.41x slower                                                                                                   |
| Geometric mean           | (ref)                                                                                                             | 1.06x slower                                                                                                            |

Benchmark hidden because not significant (9): async_tree_cpu_io_mixed_tg, regex_v8, async_tree_memoization_tg, asyncio_websockets, async_tree_none_tg, regex_effbot, pidigits, pickle_list, pickle

- Geometric mean (including insignificant results): 1.045x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.16x
- 95% likely to have a slowdown of 1.15x
- 99% likely to have a slowdown of 1.13x

# Memory
- memory change: 1.23x