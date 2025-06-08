# Results vs. base

- fork: python
- ref: 8fdbbf8b18f1405abe67
- machine: linux-aarch64
- commit hash: 8fdbbf8
- commit date: 2025-06-07
- overall geometric mean: 1.050x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.14x slower
- Memory change: 1.23x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250607-3.15.0a0-8fdbbf8/bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json | results/bm-20250607-3.15.0a0-8fdbbf8-NOGIL/bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 352 ms                                                                                                            | 447 ms: 1.27x slower                                                                                                    |
| docutils       | 3.44 sec                                                                                                          | 3.92 sec: 1.14x slower                                                                                                  |
| html5lib       | 67.4 ms                                                                                                           | 82.9 ms: 1.23x slower                                                                                                   |
| sphinx         | 1.34 sec                                                                                                          | 1.60 sec: 1.20x slower                                                                                                  |
| Geometric mean | (ref)                                                                                                             | 1.21x slower                                                                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | results/bm-20250607-3.15.0a0-8fdbbf8/bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json | results/bm-20250607-3.15.0a0-8fdbbf8-NOGIL/bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json |
|-------------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| async_tree_io_tg        | 1.02 sec                                                                                                          | 983 ms: 1.04x faster                                                                                                    |
| async_tree_none_tg      | 418 ms                                                                                                            | 430 ms: 1.03x slower                                                                                                    |
| async_tree_io           | 979 ms                                                                                                            | 1.01 sec: 1.03x slower                                                                                                  |
| async_tree_cpu_io_mixed | 805 ms                                                                                                            | 847 ms: 1.05x slower                                                                                                    |
| async_tree_none         | 433 ms                                                                                                            | 466 ms: 1.08x slower                                                                                                    |
| asyncio_tcp             | 581 ms                                                                                                            | 627 ms: 1.08x slower                                                                                                    |
| async_tree_memoization  | 509 ms                                                                                                            | 560 ms: 1.10x slower                                                                                                    |
| asyncio_tcp_ssl         | 2.26 sec                                                                                                          | 2.50 sec: 1.10x slower                                                                                                  |
| coroutines              | 34.0 ms                                                                                                           | 38.4 ms: 1.13x slower                                                                                                   |
| async_generators        | 519 ms                                                                                                            | 626 ms: 1.21x slower                                                                                                    |
| Geometric mean          | (ref)                                                                                                             | 1.06x slower                                                                                                            |

Benchmark hidden because not significant (3): async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250607-3.15.0a0-8fdbbf8/bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json | results/bm-20250607-3.15.0a0-8fdbbf8-NOGIL/bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| pidigits       | 281 ms                                                                                                            | 277 ms: 1.01x faster                                                                                                    |
| float          | 97.2 ms                                                                                                           | 106 ms: 1.09x slower                                                                                                    |
| nbody          | 138 ms                                                                                                            | 192 ms: 1.39x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                             | 1.14x slower                                                                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250607-3.15.0a0-8fdbbf8/bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json | results/bm-20250607-3.15.0a0-8fdbbf8-NOGIL/bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| regex_dna      | 231 ms                                                                                                            | 233 ms: 1.01x slower                                                                                                    |
| regex_v8       | 30.1 ms                                                                                                           | 30.8 ms: 1.02x slower                                                                                                   |
| regex_compile  | 152 ms                                                                                                            | 196 ms: 1.29x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                             | 1.08x slower                                                                                                            |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250607-3.15.0a0-8fdbbf8/bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json | results/bm-20250607-3.15.0a0-8fdbbf8-NOGIL/bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json |
|----------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| xml_etree_iterparse  | 168 ms                                                                                                            | 158 ms: 1.07x faster                                                                                                    |
| pickle               | 19.7 us                                                                                                           | 20.0 us: 1.01x slower                                                                                                   |
| xml_etree_parse      | 230 ms                                                                                                            | 236 ms: 1.03x slower                                                                                                    |
| json_dumps           | 17.4 ms                                                                                                           | 19.7 ms: 1.14x slower                                                                                                   |
| unpickle_list        | 6.83 us                                                                                                           | 7.77 us: 1.14x slower                                                                                                   |
| json_loads           | 38.6 us                                                                                                           | 44.9 us: 1.16x slower                                                                                                   |
| unpickle             | 22.5 us                                                                                                           | 26.7 us: 1.19x slower                                                                                                   |
| xml_etree_generate   | 160 ms                                                                                                            | 192 ms: 1.20x slower                                                                                                    |
| xml_etree_process    | 106 ms                                                                                                            | 129 ms: 1.22x slower                                                                                                    |
| pickle_pure_python   | 471 us                                                                                                            | 580 us: 1.23x slower                                                                                                    |
| tomli_loads          | 2.86 sec                                                                                                          | 3.55 sec: 1.24x slower                                                                                                  |
| unpickle_pure_python | 321 us                                                                                                            | 420 us: 1.31x slower                                                                                                    |
| Geometric mean       | (ref)                                                                                                             | 1.13x slower                                                                                                            |

Benchmark hidden because not significant (2): pickle_list, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20250607-3.15.0a0-8fdbbf8/bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json | results/bm-20250607-3.15.0a0-8fdbbf8-NOGIL/bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json |
|------------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 16.9 ms                                                                                                           | 22.9 ms: 1.36x slower                                                                                                   |
| python_startup_no_site | 9.58 ms                                                                                                           | 13.8 ms: 1.44x slower                                                                                                   |
| Geometric mean         | (ref)                                                                                                             | 1.40x slower                                                                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20250607-3.15.0a0-8fdbbf8/bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json | results/bm-20250607-3.15.0a0-8fdbbf8-NOGIL/bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json |
|-----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| genshi_xml      | 74.3 ms                                                                                                           | 97.3 ms: 1.31x slower                                                                                                   |
| genshi_text     | 33.9 ms                                                                                                           | 46.0 ms: 1.35x slower                                                                                                   |
| mako            | 17.4 ms                                                                                                           | 24.1 ms: 1.39x slower                                                                                                   |
| django_template | 52.6 ms                                                                                                           | 73.3 ms: 1.39x slower                                                                                                   |
| Geometric mean  | (ref)                                                                                                             | 1.36x slower                                                                                                            |

All benchmarks:
===============

| Benchmark                | results/bm-20250607-3.15.0a0-8fdbbf8/bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json | results/bm-20250607-3.15.0a0-8fdbbf8-NOGIL/bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json |
|--------------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| thrift                   | 196 ms                                                                                                            | 1.63 ms: 120.80x faster                                                                                                 |
| bench_mp_pool            | 6.68 sec                                                                                                          | 72.6 ms: 92.04x faster                                                                                                  |
| coverage                 | 695 ms                                                                                                            | 184 ms: 3.78x faster                                                                                                    |
| gc_traversal             | 7.47 ms                                                                                                           | 3.58 ms: 2.09x faster                                                                                                   |
| create_gc_cycles         | 4.05 ms                                                                                                           | 2.49 ms: 1.63x faster                                                                                                   |
| sqlite_synth             | 4.92 us                                                                                                           | 4.51 us: 1.09x faster                                                                                                   |
| xml_etree_iterparse      | 168 ms                                                                                                            | 158 ms: 1.07x faster                                                                                                    |
| async_tree_io_tg         | 1.02 sec                                                                                                          | 983 ms: 1.04x faster                                                                                                    |
| pidigits                 | 281 ms                                                                                                            | 277 ms: 1.01x faster                                                                                                    |
| regex_dna                | 231 ms                                                                                                            | 233 ms: 1.01x slower                                                                                                    |
| pickle                   | 19.7 us                                                                                                           | 20.0 us: 1.01x slower                                                                                                   |
| regex_v8                 | 30.1 ms                                                                                                           | 30.8 ms: 1.02x slower                                                                                                   |
| xml_etree_parse          | 230 ms                                                                                                            | 236 ms: 1.03x slower                                                                                                    |
| async_tree_none_tg       | 418 ms                                                                                                            | 430 ms: 1.03x slower                                                                                                    |
| async_tree_io            | 979 ms                                                                                                            | 1.01 sec: 1.03x slower                                                                                                  |
| async_tree_cpu_io_mixed  | 805 ms                                                                                                            | 847 ms: 1.05x slower                                                                                                    |
| async_tree_none          | 433 ms                                                                                                            | 466 ms: 1.08x slower                                                                                                    |
| asyncio_tcp              | 581 ms                                                                                                            | 627 ms: 1.08x slower                                                                                                    |
| float                    | 97.2 ms                                                                                                           | 106 ms: 1.09x slower                                                                                                    |
| k_core                   | 2.97 sec                                                                                                          | 3.25 sec: 1.09x slower                                                                                                  |
| async_tree_memoization   | 509 ms                                                                                                            | 560 ms: 1.10x slower                                                                                                    |
| asyncio_tcp_ssl          | 2.26 sec                                                                                                          | 2.50 sec: 1.10x slower                                                                                                  |
| pathlib                  | 26.6 ms                                                                                                           | 29.9 ms: 1.12x slower                                                                                                   |
| coroutines               | 34.0 ms                                                                                                           | 38.4 ms: 1.13x slower                                                                                                   |
| json_dumps               | 17.4 ms                                                                                                           | 19.7 ms: 1.14x slower                                                                                                   |
| unpickle_list            | 6.83 us                                                                                                           | 7.77 us: 1.14x slower                                                                                                   |
| docutils                 | 3.44 sec                                                                                                          | 3.92 sec: 1.14x slower                                                                                                  |
| scimark_sparse_mat_mult  | 7.88 ms                                                                                                           | 9.05 ms: 1.15x slower                                                                                                   |
| json                     | 7.02 ms                                                                                                           | 8.06 ms: 1.15x slower                                                                                                   |
| scimark_sor              | 176 ms                                                                                                            | 204 ms: 1.15x slower                                                                                                    |
| shortest_path            | 612 ms                                                                                                            | 710 ms: 1.16x slower                                                                                                    |
| scimark_fft              | 501 ms                                                                                                            | 583 ms: 1.16x slower                                                                                                    |
| generators               | 40.3 ms                                                                                                           | 46.9 ms: 1.16x slower                                                                                                   |
| json_loads               | 38.6 us                                                                                                           | 44.9 us: 1.16x slower                                                                                                   |
| pyflate                  | 584 ms                                                                                                            | 685 ms: 1.17x slower                                                                                                    |
| connected_components     | 580 ms                                                                                                            | 682 ms: 1.17x slower                                                                                                    |
| unpickle                 | 22.5 us                                                                                                           | 26.7 us: 1.19x slower                                                                                                   |
| hexiom                   | 8.40 ms                                                                                                           | 10.0 ms: 1.19x slower                                                                                                   |
| sphinx                   | 1.34 sec                                                                                                          | 1.60 sec: 1.20x slower                                                                                                  |
| pycparser                | 1.46 sec                                                                                                          | 1.75 sec: 1.20x slower                                                                                                  |
| xml_etree_generate       | 160 ms                                                                                                            | 192 ms: 1.20x slower                                                                                                    |
| meteor_contest           | 128 ms                                                                                                            | 154 ms: 1.20x slower                                                                                                    |
| fannkuch                 | 593 ms                                                                                                            | 713 ms: 1.20x slower                                                                                                    |
| chaos                    | 83.9 ms                                                                                                           | 101 ms: 1.20x slower                                                                                                    |
| async_generators         | 519 ms                                                                                                            | 626 ms: 1.21x slower                                                                                                    |
| logging_silent           | 929 ns                                                                                                            | 1.13 us: 1.21x slower                                                                                                   |
| unpack_sequence          | 61.9 ns                                                                                                           | 75.5 ns: 1.22x slower                                                                                                   |
| xml_etree_process        | 106 ms                                                                                                            | 129 ms: 1.22x slower                                                                                                    |
| html5lib                 | 67.4 ms                                                                                                           | 82.9 ms: 1.23x slower                                                                                                   |
| pickle_pure_python       | 471 us                                                                                                            | 580 us: 1.23x slower                                                                                                    |
| many_optionals           | 1.11 ms                                                                                                           | 1.37 ms: 1.23x slower                                                                                                   |
| raytrace                 | 400 ms                                                                                                            | 496 ms: 1.24x slower                                                                                                    |
| tomli_loads              | 2.86 sec                                                                                                          | 3.55 sec: 1.24x slower                                                                                                  |
| spectral_norm            | 156 ms                                                                                                            | 193 ms: 1.24x slower                                                                                                    |
| pprint_safe_repr         | 1.30 sec                                                                                                          | 1.62 sec: 1.24x slower                                                                                                  |
| nqueens                  | 125 ms                                                                                                            | 156 ms: 1.25x slower                                                                                                    |
| scimark_lu               | 188 ms                                                                                                            | 234 ms: 1.25x slower                                                                                                    |
| pprint_pformat           | 2.64 sec                                                                                                          | 3.31 sec: 1.25x slower                                                                                                  |
| logging_simple           | 9.33 us                                                                                                           | 11.7 us: 1.25x slower                                                                                                   |
| pylint                   | 373 ms                                                                                                            | 468 ms: 1.26x slower                                                                                                    |
| subparsers               | 36.5 ms                                                                                                           | 45.9 ms: 1.26x slower                                                                                                   |
| deltablue                | 4.50 ms                                                                                                           | 5.68 ms: 1.26x slower                                                                                                   |
| 2to3                     | 352 ms                                                                                                            | 447 ms: 1.27x slower                                                                                                    |
| deepcopy_reduce          | 4.70 us                                                                                                           | 5.97 us: 1.27x slower                                                                                                   |
| logging_format           | 10.2 us                                                                                                           | 13.0 us: 1.27x slower                                                                                                   |
| dulwich_log              | 62.0 ms                                                                                                           | 79.5 ms: 1.28x slower                                                                                                   |
| mdp                      | 1.98 sec                                                                                                          | 2.54 sec: 1.28x slower                                                                                                  |
| regex_compile            | 152 ms                                                                                                            | 196 ms: 1.29x slower                                                                                                    |
| sqlglot_v2_normalize     | 163 ms                                                                                                            | 210 ms: 1.29x slower                                                                                                    |
| deepcopy_memo            | 44.0 us                                                                                                           | 56.9 us: 1.29x slower                                                                                                   |
| go                       | 141 ms                                                                                                            | 182 ms: 1.29x slower                                                                                                    |
| bpe_tokeniser            | 6.75 sec                                                                                                          | 8.81 sec: 1.30x slower                                                                                                  |
| unpickle_pure_python     | 321 us                                                                                                            | 420 us: 1.31x slower                                                                                                    |
| sqlglot_v2_optimize      | 76.2 ms                                                                                                           | 99.5 ms: 1.31x slower                                                                                                   |
| deepcopy                 | 405 us                                                                                                            | 529 us: 1.31x slower                                                                                                    |
| genshi_xml               | 74.3 ms                                                                                                           | 97.3 ms: 1.31x slower                                                                                                   |
| comprehensions           | 23.0 us                                                                                                           | 30.2 us: 1.32x slower                                                                                                   |
| sympy_integrate          | 23.6 ms                                                                                                           | 31.3 ms: 1.32x slower                                                                                                   |
| bench_thread_pool        | 1.49 ms                                                                                                           | 1.98 ms: 1.33x slower                                                                                                   |
| sqlglot_v2_transpile     | 2.17 ms                                                                                                           | 2.91 ms: 1.34x slower                                                                                                   |
| sqlglot_v2_parse         | 1.74 ms                                                                                                           | 2.34 ms: 1.34x slower                                                                                                   |
| sympy_expand             | 585 ms                                                                                                            | 790 ms: 1.35x slower                                                                                                    |
| sympy_str                | 332 ms                                                                                                            | 449 ms: 1.35x slower                                                                                                    |
| genshi_text              | 33.9 ms                                                                                                           | 46.0 ms: 1.35x slower                                                                                                   |
| python_startup           | 16.9 ms                                                                                                           | 22.9 ms: 1.36x slower                                                                                                   |
| telco                    | 13.4 ms                                                                                                           | 18.1 ms: 1.36x slower                                                                                                   |
| typing_runtime_protocols | 259 us                                                                                                            | 354 us: 1.37x slower                                                                                                    |
| richards                 | 63.5 ms                                                                                                           | 86.8 ms: 1.37x slower                                                                                                   |
| sympy_sum                | 179 ms                                                                                                            | 246 ms: 1.37x slower                                                                                                    |
| mako                     | 17.4 ms                                                                                                           | 24.1 ms: 1.39x slower                                                                                                   |
| nbody                    | 138 ms                                                                                                            | 192 ms: 1.39x slower                                                                                                    |
| django_template          | 52.6 ms                                                                                                           | 73.3 ms: 1.39x slower                                                                                                   |
| richards_super           | 71.8 ms                                                                                                           | 101 ms: 1.41x slower                                                                                                    |
| crypto_pyaes             | 103 ms                                                                                                            | 145 ms: 1.41x slower                                                                                                    |
| scimark_monte_carlo      | 98.2 ms                                                                                                           | 139 ms: 1.41x slower                                                                                                    |
| python_startup_no_site   | 9.58 ms                                                                                                           | 13.8 ms: 1.44x slower                                                                                                   |
| Geometric mean           | (ref)                                                                                                             | 1.06x slower                                                                                                            |

Benchmark hidden because not significant (6): async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, pickle_list, asyncio_websockets, regex_effbot, pickle_dict

- Geometric mean (including insignificant results): 1.050x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.16x
- 95% likely to have a slowdown of 1.16x
- 99% likely to have a slowdown of 1.14x

# Memory
- memory change: 1.23x