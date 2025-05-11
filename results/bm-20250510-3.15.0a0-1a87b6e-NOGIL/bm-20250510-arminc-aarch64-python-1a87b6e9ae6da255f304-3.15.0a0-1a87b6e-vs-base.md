# Results vs. base

- fork: python
- ref: 1a87b6e9ae6da255f304
- machine: linux-aarch64
- commit hash: 1a87b6e
- commit date: 2025-05-10
- overall geometric mean: 1.054x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x slower
- Memory change: 1.22x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250510-3.15.0a0-1a87b6e/bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json | results/bm-20250510-3.15.0a0-1a87b6e-NOGIL/bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 307 ms                                                                                                            | 359 ms: 1.17x slower                                                                                                    |
| docutils       | 2.95 sec                                                                                                          | 3.26 sec: 1.10x slower                                                                                                  |
| html5lib       | 62.0 ms                                                                                                           | 69.0 ms: 1.11x slower                                                                                                   |
| sphinx         | 1.16 sec                                                                                                          | 1.30 sec: 1.12x slower                                                                                                  |
| Geometric mean | (ref)                                                                                                             | 1.13x slower                                                                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | results/bm-20250510-3.15.0a0-1a87b6e/bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json | results/bm-20250510-3.15.0a0-1a87b6e-NOGIL/bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json |
|-------------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| async_tree_io_tg        | 900 ms                                                                                                            | 837 ms: 1.08x faster                                                                                                    |
| async_tree_io           | 887 ms                                                                                                            | 869 ms: 1.02x faster                                                                                                    |
| async_tree_memoization  | 465 ms                                                                                                            | 484 ms: 1.04x slower                                                                                                    |
| async_tree_cpu_io_mixed | 651 ms                                                                                                            | 681 ms: 1.04x slower                                                                                                    |
| async_tree_none         | 387 ms                                                                                                            | 416 ms: 1.07x slower                                                                                                    |
| async_generators        | 460 ms                                                                                                            | 501 ms: 1.09x slower                                                                                                    |
| asyncio_tcp             | 534 ms                                                                                                            | 583 ms: 1.09x slower                                                                                                    |
| asyncio_tcp_ssl         | 2.17 sec                                                                                                          | 2.44 sec: 1.12x slower                                                                                                  |
| Geometric mean          | (ref)                                                                                                             | 1.03x slower                                                                                                            |

Benchmark hidden because not significant (5): async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, asyncio_websockets, async_tree_none_tg, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250510-3.15.0a0-1a87b6e/bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json | results/bm-20250510-3.15.0a0-1a87b6e-NOGIL/bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| pidigits       | 235 ms                                                                                                            | 232 ms: 1.01x faster                                                                                                    |
| float          | 86.3 ms                                                                                                           | 95.1 ms: 1.10x slower                                                                                                   |
| nbody          | 122 ms                                                                                                            | 168 ms: 1.38x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                             | 1.14x slower                                                                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250510-3.15.0a0-1a87b6e/bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json | results/bm-20250510-3.15.0a0-1a87b6e-NOGIL/bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| regex_effbot   | 3.84 ms                                                                                                           | 4.06 ms: 1.06x slower                                                                                                   |
| regex_compile  | 122 ms                                                                                                            | 150 ms: 1.23x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                             | 1.06x slower                                                                                                            |

Benchmark hidden because not significant (2): regex_v8, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250510-3.15.0a0-1a87b6e/bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json | results/bm-20250510-3.15.0a0-1a87b6e-NOGIL/bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json |
|----------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| xml_etree_iterparse  | 143 ms                                                                                                            | 130 ms: 1.10x faster                                                                                                    |
| xml_etree_parse      | 180 ms                                                                                                            | 176 ms: 1.02x faster                                                                                                    |
| json_loads           | 36.4 us                                                                                                           | 39.0 us: 1.07x slower                                                                                                   |
| unpickle             | 18.8 us                                                                                                           | 20.5 us: 1.09x slower                                                                                                   |
| pickle_pure_python   | 395 us                                                                                                            | 438 us: 1.11x slower                                                                                                    |
| json_dumps           | 14.6 ms                                                                                                           | 16.3 ms: 1.11x slower                                                                                                   |
| unpickle_pure_python | 267 us                                                                                                            | 302 us: 1.13x slower                                                                                                    |
| tomli_loads          | 2.44 sec                                                                                                          | 2.88 sec: 1.18x slower                                                                                                  |
| xml_etree_process    | 79.6 ms                                                                                                           | 101 ms: 1.27x slower                                                                                                    |
| xml_etree_generate   | 111 ms                                                                                                            | 144 ms: 1.29x slower                                                                                                    |
| Geometric mean       | (ref)                                                                                                             | 1.08x slower                                                                                                            |

Benchmark hidden because not significant (4): pickle, pickle_list, pickle_dict, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20250510-3.15.0a0-1a87b6e/bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json | results/bm-20250510-3.15.0a0-1a87b6e-NOGIL/bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json |
|------------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 15.1 ms                                                                                                           | 20.0 ms: 1.33x slower                                                                                                   |
| python_startup_no_site | 8.66 ms                                                                                                           | 12.2 ms: 1.41x slower                                                                                                   |
| Geometric mean         | (ref)                                                                                                             | 1.37x slower                                                                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20250510-3.15.0a0-1a87b6e/bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json | results/bm-20250510-3.15.0a0-1a87b6e-NOGIL/bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json |
|-----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| genshi_xml      | 61.8 ms                                                                                                           | 75.7 ms: 1.23x slower                                                                                                   |
| genshi_text     | 27.6 ms                                                                                                           | 35.8 ms: 1.29x slower                                                                                                   |
| django_template | 38.7 ms                                                                                                           | 51.1 ms: 1.32x slower                                                                                                   |
| mako            | 14.0 ms                                                                                                           | 21.4 ms: 1.54x slower                                                                                                   |
| Geometric mean  | (ref)                                                                                                             | 1.34x slower                                                                                                            |

All benchmarks:
===============

| Benchmark                | results/bm-20250510-3.15.0a0-1a87b6e/bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json | results/bm-20250510-3.15.0a0-1a87b6e-NOGIL/bm-20250510-arminc-aarch64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json |
|--------------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| thrift                   | 194 ms                                                                                                            | 1.19 ms: 163.23x faster                                                                                                 |
| bench_mp_pool            | 4.01 sec                                                                                                          | 61.6 ms: 65.09x faster                                                                                                  |
| coverage                 | 545 ms                                                                                                            | 150 ms: 3.64x faster                                                                                                    |
| gc_traversal             | 6.97 ms                                                                                                           | 2.93 ms: 2.38x faster                                                                                                   |
| create_gc_cycles         | 3.70 ms                                                                                                           | 2.33 ms: 1.59x faster                                                                                                   |
| xml_etree_iterparse      | 143 ms                                                                                                            | 130 ms: 1.10x faster                                                                                                    |
| async_tree_io_tg         | 900 ms                                                                                                            | 837 ms: 1.08x faster                                                                                                    |
| sqlite_synth             | 3.75 us                                                                                                           | 3.50 us: 1.07x faster                                                                                                   |
| async_tree_io            | 887 ms                                                                                                            | 869 ms: 1.02x faster                                                                                                    |
| xml_etree_parse          | 180 ms                                                                                                            | 176 ms: 1.02x faster                                                                                                    |
| pidigits                 | 235 ms                                                                                                            | 232 ms: 1.01x faster                                                                                                    |
| async_tree_memoization   | 465 ms                                                                                                            | 484 ms: 1.04x slower                                                                                                    |
| async_tree_cpu_io_mixed  | 651 ms                                                                                                            | 681 ms: 1.04x slower                                                                                                    |
| scimark_fft              | 445 ms                                                                                                            | 469 ms: 1.05x slower                                                                                                    |
| regex_effbot             | 3.84 ms                                                                                                           | 4.06 ms: 1.06x slower                                                                                                   |
| spectral_norm            | 130 ms                                                                                                            | 138 ms: 1.06x slower                                                                                                    |
| json                     | 6.11 ms                                                                                                           | 6.48 ms: 1.06x slower                                                                                                   |
| json_loads               | 36.4 us                                                                                                           | 39.0 us: 1.07x slower                                                                                                   |
| generators               | 36.9 ms                                                                                                           | 39.6 ms: 1.07x slower                                                                                                   |
| async_tree_none          | 387 ms                                                                                                            | 416 ms: 1.07x slower                                                                                                    |
| scimark_sparse_mat_mult  | 6.91 ms                                                                                                           | 7.52 ms: 1.09x slower                                                                                                   |
| async_generators         | 460 ms                                                                                                            | 501 ms: 1.09x slower                                                                                                    |
| asyncio_tcp              | 534 ms                                                                                                            | 583 ms: 1.09x slower                                                                                                    |
| unpickle                 | 18.8 us                                                                                                           | 20.5 us: 1.09x slower                                                                                                   |
| scimark_sor              | 147 ms                                                                                                            | 161 ms: 1.10x slower                                                                                                    |
| pycparser                | 1.26 sec                                                                                                          | 1.39 sec: 1.10x slower                                                                                                  |
| float                    | 86.3 ms                                                                                                           | 95.1 ms: 1.10x slower                                                                                                   |
| docutils                 | 2.95 sec                                                                                                          | 3.26 sec: 1.10x slower                                                                                                  |
| pickle_pure_python       | 395 us                                                                                                            | 438 us: 1.11x slower                                                                                                    |
| json_dumps               | 14.6 ms                                                                                                           | 16.3 ms: 1.11x slower                                                                                                   |
| html5lib                 | 62.0 ms                                                                                                           | 69.0 ms: 1.11x slower                                                                                                   |
| sphinx                   | 1.16 sec                                                                                                          | 1.30 sec: 1.12x slower                                                                                                  |
| asyncio_tcp_ssl          | 2.17 sec                                                                                                          | 2.44 sec: 1.12x slower                                                                                                  |
| hexiom                   | 7.14 ms                                                                                                           | 8.03 ms: 1.12x slower                                                                                                   |
| unpickle_pure_python     | 267 us                                                                                                            | 302 us: 1.13x slower                                                                                                    |
| dulwich_log              | 54.0 ms                                                                                                           | 61.2 ms: 1.13x slower                                                                                                   |
| chaos                    | 70.3 ms                                                                                                           | 80.1 ms: 1.14x slower                                                                                                   |
| sqlglot_v2_normalize     | 126 ms                                                                                                            | 145 ms: 1.15x slower                                                                                                    |
| k_core                   | 2.80 sec                                                                                                          | 3.21 sec: 1.15x slower                                                                                                  |
| shortest_path            | 578 ms                                                                                                            | 669 ms: 1.16x slower                                                                                                    |
| telco                    | 9.70 ms                                                                                                           | 11.2 ms: 1.16x slower                                                                                                   |
| pyflate                  | 523 ms                                                                                                            | 608 ms: 1.16x slower                                                                                                    |
| mdp                      | 1.67 sec                                                                                                          | 1.96 sec: 1.17x slower                                                                                                  |
| 2to3                     | 307 ms                                                                                                            | 359 ms: 1.17x slower                                                                                                    |
| tomli_loads              | 2.44 sec                                                                                                          | 2.88 sec: 1.18x slower                                                                                                  |
| many_optionals           | 886 us                                                                                                            | 1.05 ms: 1.18x slower                                                                                                   |
| connected_components     | 558 ms                                                                                                            | 661 ms: 1.18x slower                                                                                                    |
| pylint                   | 315 ms                                                                                                            | 374 ms: 1.19x slower                                                                                                    |
| subparsers               | 28.4 ms                                                                                                           | 33.7 ms: 1.19x slower                                                                                                   |
| sqlglot_v2_optimize      | 61.1 ms                                                                                                           | 72.9 ms: 1.19x slower                                                                                                   |
| deepcopy                 | 335 us                                                                                                            | 401 us: 1.20x slower                                                                                                    |
| pprint_pformat           | 1.84 sec                                                                                                          | 2.20 sec: 1.20x slower                                                                                                  |
| pprint_safe_repr         | 891 ms                                                                                                            | 1.07 sec: 1.20x slower                                                                                                  |
| logging_format           | 8.39 us                                                                                                           | 10.1 us: 1.20x slower                                                                                                   |
| nqueens                  | 100 ms                                                                                                            | 121 ms: 1.21x slower                                                                                                    |
| comprehensions           | 21.2 us                                                                                                           | 25.6 us: 1.21x slower                                                                                                   |
| deepcopy_reduce          | 3.57 us                                                                                                           | 4.34 us: 1.22x slower                                                                                                   |
| raytrace                 | 325 ms                                                                                                            | 396 ms: 1.22x slower                                                                                                    |
| logging_simple           | 7.63 us                                                                                                           | 9.29 us: 1.22x slower                                                                                                   |
| genshi_xml               | 61.8 ms                                                                                                           | 75.7 ms: 1.23x slower                                                                                                   |
| scimark_lu               | 142 ms                                                                                                            | 174 ms: 1.23x slower                                                                                                    |
| regex_compile            | 122 ms                                                                                                            | 150 ms: 1.23x slower                                                                                                    |
| sympy_str                | 275 ms                                                                                                            | 338 ms: 1.23x slower                                                                                                    |
| sqlglot_v2_transpile     | 1.82 ms                                                                                                           | 2.25 ms: 1.24x slower                                                                                                   |
| go                       | 129 ms                                                                                                            | 160 ms: 1.24x slower                                                                                                    |
| deepcopy_memo            | 38.1 us                                                                                                           | 47.7 us: 1.25x slower                                                                                                   |
| bpe_tokeniser            | 5.50 sec                                                                                                          | 6.93 sec: 1.26x slower                                                                                                  |
| logging_silent           | 605 ns                                                                                                            | 763 ns: 1.26x slower                                                                                                    |
| xml_etree_process        | 79.6 ms                                                                                                           | 101 ms: 1.27x slower                                                                                                    |
| deltablue                | 3.78 ms                                                                                                           | 4.78 ms: 1.27x slower                                                                                                   |
| sympy_integrate          | 20.1 ms                                                                                                           | 25.7 ms: 1.28x slower                                                                                                   |
| sympy_expand             | 465 ms                                                                                                            | 597 ms: 1.28x slower                                                                                                    |
| sqlglot_v2_parse         | 1.44 ms                                                                                                           | 1.85 ms: 1.29x slower                                                                                                   |
| xml_etree_generate       | 111 ms                                                                                                            | 144 ms: 1.29x slower                                                                                                    |
| genshi_text              | 27.6 ms                                                                                                           | 35.8 ms: 1.29x slower                                                                                                   |
| crypto_pyaes             | 85.1 ms                                                                                                           | 111 ms: 1.30x slower                                                                                                    |
| fannkuch                 | 474 ms                                                                                                            | 619 ms: 1.30x slower                                                                                                    |
| typing_runtime_protocols | 198 us                                                                                                            | 261 us: 1.32x slower                                                                                                    |
| django_template          | 38.7 ms                                                                                                           | 51.1 ms: 1.32x slower                                                                                                   |
| python_startup           | 15.1 ms                                                                                                           | 20.0 ms: 1.33x slower                                                                                                   |
| richards                 | 51.6 ms                                                                                                           | 68.5 ms: 1.33x slower                                                                                                   |
| scimark_monte_carlo      | 80.6 ms                                                                                                           | 107 ms: 1.33x slower                                                                                                    |
| meteor_contest           | 113 ms                                                                                                            | 150 ms: 1.33x slower                                                                                                    |
| sympy_sum                | 141 ms                                                                                                            | 188 ms: 1.34x slower                                                                                                    |
| bench_thread_pool        | 1.36 ms                                                                                                           | 1.84 ms: 1.35x slower                                                                                                   |
| richards_super           | 58.3 ms                                                                                                           | 78.5 ms: 1.35x slower                                                                                                   |
| unpack_sequence          | 53.3 ns                                                                                                           | 73.2 ns: 1.37x slower                                                                                                   |
| nbody                    | 122 ms                                                                                                            | 168 ms: 1.38x slower                                                                                                    |
| python_startup_no_site   | 8.66 ms                                                                                                           | 12.2 ms: 1.41x slower                                                                                                   |
| mako                     | 14.0 ms                                                                                                           | 21.4 ms: 1.54x slower                                                                                                   |
| Geometric mean           | (ref)                                                                                                             | 1.02x slower                                                                                                            |

Benchmark hidden because not significant (12): regex_v8, async_tree_cpu_io_mixed_tg, regex_dna, async_tree_memoization_tg, pickle, asyncio_websockets, pickle_list, async_tree_none_tg, coroutines, pathlib, pickle_dict, unpickle_list

- Geometric mean (including insignificant results): 1.054x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.11x
- 95% likely to have a slowdown of 1.11x
- 99% likely to have a slowdown of 1.10x

# Memory
- memory change: 1.22x