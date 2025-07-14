# Results vs. base

- fork: python
- ref: 47b01da4ccedd9c00fad
- machine: linux-aarch64
- commit hash: 47b01da
- commit date: 2025-07-12
- overall geometric mean: 1.124x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.11x slower
- Memory change: 1.19x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250712-3.15.0a0-47b01da/bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json | results/bm-20250712-3.15.0a0-47b01da-NOGIL/bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 300 ms                                                                                                            | 349 ms: 1.16x slower                                                                                                    |
| docutils       | 2.93 sec                                                                                                          | 3.19 sec: 1.09x slower                                                                                                  |
| html5lib       | 61.5 ms                                                                                                           | 70.2 ms: 1.14x slower                                                                                                   |
| sphinx         | 1.12 sec                                                                                                          | 1.27 sec: 1.13x slower                                                                                                  |
| Geometric mean | (ref)                                                                                                             | 1.13x slower                                                                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20250712-3.15.0a0-47b01da/bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json | results/bm-20250712-3.15.0a0-47b01da-NOGIL/bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json |
|----------------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| async_tree_io_tg           | 883 ms                                                                                                            | 854 ms: 1.03x faster                                                                                                    |
| async_tree_memoization_tg  | 470 ms                                                                                                            | 459 ms: 1.02x faster                                                                                                    |
| async_tree_cpu_io_mixed_tg | 652 ms                                                                                                            | 643 ms: 1.01x faster                                                                                                    |
| async_tree_memoization     | 473 ms                                                                                                            | 487 ms: 1.03x slower                                                                                                    |
| async_tree_cpu_io_mixed    | 659 ms                                                                                                            | 683 ms: 1.04x slower                                                                                                    |
| asyncio_tcp                | 543 ms                                                                                                            | 565 ms: 1.04x slower                                                                                                    |
| async_tree_none            | 374 ms                                                                                                            | 407 ms: 1.09x slower                                                                                                    |
| async_generators           | 460 ms                                                                                                            | 505 ms: 1.10x slower                                                                                                    |
| asyncio_tcp_ssl            | 2.16 sec                                                                                                          | 2.42 sec: 1.12x slower                                                                                                  |
| Geometric mean             | (ref)                                                                                                             | 1.03x slower                                                                                                            |

Benchmark hidden because not significant (4): asyncio_websockets, async_tree_none_tg, async_tree_io, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250712-3.15.0a0-47b01da/bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json | results/bm-20250712-3.15.0a0-47b01da-NOGIL/bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| pidigits       | 236 ms                                                                                                            | 232 ms: 1.02x faster                                                                                                    |
| float          | 85.3 ms                                                                                                           | 95.6 ms: 1.12x slower                                                                                                   |
| nbody          | 123 ms                                                                                                            | 181 ms: 1.48x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                             | 1.18x slower                                                                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250712-3.15.0a0-47b01da/bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json | results/bm-20250712-3.15.0a0-47b01da-NOGIL/bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| regex_v8       | 28.6 ms                                                                                                           | 26.0 ms: 1.10x faster                                                                                                   |
| regex_dna      | 221 ms                                                                                                            | 237 ms: 1.07x slower                                                                                                    |
| regex_compile  | 122 ms                                                                                                            | 149 ms: 1.22x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                             | 1.05x slower                                                                                                            |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250712-3.15.0a0-47b01da/bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json | results/bm-20250712-3.15.0a0-47b01da-NOGIL/bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json |
|----------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| xml_etree_iterparse  | 142 ms                                                                                                            | 133 ms: 1.07x faster                                                                                                    |
| pickle_list          | 5.86 us                                                                                                           | 5.65 us: 1.04x faster                                                                                                   |
| xml_etree_parse      | 181 ms                                                                                                            | 183 ms: 1.01x slower                                                                                                    |
| json_dumps           | 14.2 ms                                                                                                           | 14.8 ms: 1.05x slower                                                                                                   |
| unpickle_list        | 6.55 us                                                                                                           | 6.94 us: 1.06x slower                                                                                                   |
| unpickle             | 18.7 us                                                                                                           | 20.4 us: 1.09x slower                                                                                                   |
| json_loads           | 32.8 us                                                                                                           | 36.5 us: 1.11x slower                                                                                                   |
| pickle_pure_python   | 393 us                                                                                                            | 450 us: 1.15x slower                                                                                                    |
| unpickle_pure_python | 261 us                                                                                                            | 303 us: 1.16x slower                                                                                                    |
| tomli_loads          | 2.45 sec                                                                                                          | 2.87 sec: 1.17x slower                                                                                                  |
| xml_etree_generate   | 111 ms                                                                                                            | 140 ms: 1.26x slower                                                                                                    |
| xml_etree_process    | 78.8 ms                                                                                                           | 101 ms: 1.29x slower                                                                                                    |
| Geometric mean       | (ref)                                                                                                             | 1.08x slower                                                                                                            |

Benchmark hidden because not significant (2): pickle_dict, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20250712-3.15.0a0-47b01da/bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json | results/bm-20250712-3.15.0a0-47b01da-NOGIL/bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json |
|------------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 15.0 ms                                                                                                           | 20.0 ms: 1.34x slower                                                                                                   |
| python_startup_no_site | 8.59 ms                                                                                                           | 12.1 ms: 1.41x slower                                                                                                   |
| Geometric mean         | (ref)                                                                                                             | 1.37x slower                                                                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20250712-3.15.0a0-47b01da/bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json | results/bm-20250712-3.15.0a0-47b01da-NOGIL/bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json |
|-----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| django_template | 41.7 ms                                                                                                           | 51.3 ms: 1.23x slower                                                                                                   |
| genshi_xml      | 59.7 ms                                                                                                           | 75.2 ms: 1.26x slower                                                                                                   |
| genshi_text     | 27.1 ms                                                                                                           | 35.2 ms: 1.30x slower                                                                                                   |
| mako            | 13.6 ms                                                                                                           | 21.1 ms: 1.55x slower                                                                                                   |
| Geometric mean  | (ref)                                                                                                             | 1.33x slower                                                                                                            |

All benchmarks:
===============

| Benchmark                  | results/bm-20250712-3.15.0a0-47b01da/bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json | results/bm-20250712-3.15.0a0-47b01da-NOGIL/bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json |
|----------------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| bench_mp_pool              | 2.81 sec                                                                                                          | 65.2 ms: 43.08x faster                                                                                                  |
| gc_traversal               | 7.17 ms                                                                                                           | 2.87 ms: 2.50x faster                                                                                                   |
| create_gc_cycles           | 4.13 ms                                                                                                           | 2.24 ms: 1.84x faster                                                                                                   |
| sqlite_synth               | 3.80 us                                                                                                           | 3.39 us: 1.12x faster                                                                                                   |
| regex_v8                   | 28.6 ms                                                                                                           | 26.0 ms: 1.10x faster                                                                                                   |
| xml_etree_iterparse        | 142 ms                                                                                                            | 133 ms: 1.07x faster                                                                                                    |
| pickle_list                | 5.86 us                                                                                                           | 5.65 us: 1.04x faster                                                                                                   |
| async_tree_io_tg           | 883 ms                                                                                                            | 854 ms: 1.03x faster                                                                                                    |
| async_tree_memoization_tg  | 470 ms                                                                                                            | 459 ms: 1.02x faster                                                                                                    |
| pidigits                   | 236 ms                                                                                                            | 232 ms: 1.02x faster                                                                                                    |
| async_tree_cpu_io_mixed_tg | 652 ms                                                                                                            | 643 ms: 1.01x faster                                                                                                    |
| xml_etree_parse            | 181 ms                                                                                                            | 183 ms: 1.01x slower                                                                                                    |
| async_tree_memoization     | 473 ms                                                                                                            | 487 ms: 1.03x slower                                                                                                    |
| async_tree_cpu_io_mixed    | 659 ms                                                                                                            | 683 ms: 1.04x slower                                                                                                    |
| asyncio_tcp                | 543 ms                                                                                                            | 565 ms: 1.04x slower                                                                                                    |
| json_dumps                 | 14.2 ms                                                                                                           | 14.8 ms: 1.05x slower                                                                                                   |
| unpickle_list              | 6.55 us                                                                                                           | 6.94 us: 1.06x slower                                                                                                   |
| regex_dna                  | 221 ms                                                                                                            | 237 ms: 1.07x slower                                                                                                    |
| k_core                     | 2.84 sec                                                                                                          | 3.05 sec: 1.07x slower                                                                                                  |
| pycparser                  | 1.26 sec                                                                                                          | 1.36 sec: 1.08x slower                                                                                                  |
| async_tree_none            | 374 ms                                                                                                            | 407 ms: 1.09x slower                                                                                                    |
| docutils                   | 2.93 sec                                                                                                          | 3.19 sec: 1.09x slower                                                                                                  |
| json                       | 5.74 ms                                                                                                           | 6.26 ms: 1.09x slower                                                                                                   |
| unpickle                   | 18.7 us                                                                                                           | 20.4 us: 1.09x slower                                                                                                   |
| scimark_sparse_mat_mult    | 6.90 ms                                                                                                           | 7.56 ms: 1.10x slower                                                                                                   |
| async_generators           | 460 ms                                                                                                            | 505 ms: 1.10x slower                                                                                                    |
| logging_silent             | 129 ns                                                                                                            | 143 ns: 1.11x slower                                                                                                    |
| scimark_fft                | 427 ms                                                                                                            | 473 ms: 1.11x slower                                                                                                    |
| json_loads                 | 32.8 us                                                                                                           | 36.5 us: 1.11x slower                                                                                                   |
| asyncio_tcp_ssl            | 2.16 sec                                                                                                          | 2.42 sec: 1.12x slower                                                                                                  |
| float                      | 85.3 ms                                                                                                           | 95.6 ms: 1.12x slower                                                                                                   |
| connected_components       | 574 ms                                                                                                            | 645 ms: 1.12x slower                                                                                                    |
| scimark_sor                | 145 ms                                                                                                            | 163 ms: 1.12x slower                                                                                                    |
| dulwich_log                | 52.8 ms                                                                                                           | 59.5 ms: 1.13x slower                                                                                                   |
| generators                 | 35.4 ms                                                                                                           | 39.8 ms: 1.13x slower                                                                                                   |
| sphinx                     | 1.12 sec                                                                                                          | 1.27 sec: 1.13x slower                                                                                                  |
| pyflate                    | 522 ms                                                                                                            | 592 ms: 1.13x slower                                                                                                    |
| shortest_path              | 594 ms                                                                                                            | 677 ms: 1.14x slower                                                                                                    |
| html5lib                   | 61.5 ms                                                                                                           | 70.2 ms: 1.14x slower                                                                                                   |
| mdp                        | 1.68 sec                                                                                                          | 1.92 sec: 1.14x slower                                                                                                  |
| telco                      | 166 ms                                                                                                            | 190 ms: 1.14x slower                                                                                                    |
| pickle_pure_python         | 393 us                                                                                                            | 450 us: 1.15x slower                                                                                                    |
| hexiom                     | 6.79 ms                                                                                                           | 7.81 ms: 1.15x slower                                                                                                   |
| logging_simple             | 7.12 us                                                                                                           | 8.21 us: 1.15x slower                                                                                                   |
| unpickle_pure_python       | 261 us                                                                                                            | 303 us: 1.16x slower                                                                                                    |
| 2to3                       | 300 ms                                                                                                            | 349 ms: 1.16x slower                                                                                                    |
| tomli_loads                | 2.45 sec                                                                                                          | 2.87 sec: 1.17x slower                                                                                                  |
| deltablue                  | 4.00 ms                                                                                                           | 4.68 ms: 1.17x slower                                                                                                   |
| pylint                     | 319 ms                                                                                                            | 374 ms: 1.17x slower                                                                                                    |
| logging_format             | 7.65 us                                                                                                           | 9.07 us: 1.19x slower                                                                                                   |
| pprint_safe_repr           | 884 ms                                                                                                            | 1.05 sec: 1.19x slower                                                                                                  |
| pprint_pformat             | 1.82 sec                                                                                                          | 2.17 sec: 1.19x slower                                                                                                  |
| chaos                      | 66.7 ms                                                                                                           | 80.5 ms: 1.21x slower                                                                                                   |
| go                         | 127 ms                                                                                                            | 153 ms: 1.21x slower                                                                                                    |
| sqlglot_v2_normalize       | 125 ms                                                                                                            | 152 ms: 1.21x slower                                                                                                    |
| many_optionals             | 745 us                                                                                                            | 905 us: 1.21x slower                                                                                                    |
| sympy_str                  | 273 ms                                                                                                            | 333 ms: 1.22x slower                                                                                                    |
| regex_compile              | 122 ms                                                                                                            | 149 ms: 1.22x slower                                                                                                    |
| subparsers                 | 27.8 ms                                                                                                           | 34.0 ms: 1.22x slower                                                                                                   |
| deepcopy                   | 321 us                                                                                                            | 394 us: 1.23x slower                                                                                                    |
| spectral_norm              | 118 ms                                                                                                            | 145 ms: 1.23x slower                                                                                                    |
| comprehensions             | 20.0 us                                                                                                           | 24.6 us: 1.23x slower                                                                                                   |
| sympy_integrate            | 20.3 ms                                                                                                           | 25.0 ms: 1.23x slower                                                                                                   |
| django_template            | 41.7 ms                                                                                                           | 51.3 ms: 1.23x slower                                                                                                   |
| sqlglot_v2_optimize        | 60.7 ms                                                                                                           | 74.7 ms: 1.23x slower                                                                                                   |
| raytrace                   | 326 ms                                                                                                            | 401 ms: 1.23x slower                                                                                                    |
| nqueens                    | 97.1 ms                                                                                                           | 121 ms: 1.24x slower                                                                                                    |
| deepcopy_memo              | 37.2 us                                                                                                           | 46.5 us: 1.25x slower                                                                                                   |
| deepcopy_reduce            | 3.55 us                                                                                                           | 4.45 us: 1.25x slower                                                                                                   |
| bpe_tokeniser              | 5.52 sec                                                                                                          | 6.94 sec: 1.26x slower                                                                                                  |
| xml_etree_generate         | 111 ms                                                                                                            | 140 ms: 1.26x slower                                                                                                    |
| genshi_xml                 | 59.7 ms                                                                                                           | 75.2 ms: 1.26x slower                                                                                                   |
| thrift                     | 946 us                                                                                                            | 1.19 ms: 1.26x slower                                                                                                   |
| meteor_contest             | 108 ms                                                                                                            | 137 ms: 1.27x slower                                                                                                    |
| sqlglot_v2_parse           | 1.43 ms                                                                                                           | 1.81 ms: 1.27x slower                                                                                                   |
| crypto_pyaes               | 84.6 ms                                                                                                           | 107 ms: 1.27x slower                                                                                                    |
| typing_runtime_protocols   | 193 us                                                                                                            | 246 us: 1.27x slower                                                                                                    |
| sympy_expand               | 460 ms                                                                                                            | 586 ms: 1.27x slower                                                                                                    |
| fannkuch                   | 467 ms                                                                                                            | 597 ms: 1.28x slower                                                                                                    |
| xml_etree_process          | 78.8 ms                                                                                                           | 101 ms: 1.29x slower                                                                                                    |
| scimark_lu                 | 146 ms                                                                                                            | 189 ms: 1.29x slower                                                                                                    |
| genshi_text                | 27.1 ms                                                                                                           | 35.2 ms: 1.30x slower                                                                                                   |
| sympy_sum                  | 141 ms                                                                                                            | 183 ms: 1.30x slower                                                                                                    |
| scimark_monte_carlo        | 80.3 ms                                                                                                           | 105 ms: 1.31x slower                                                                                                    |
| sqlglot_v2_transpile       | 1.75 ms                                                                                                           | 2.31 ms: 1.32x slower                                                                                                   |
| bench_thread_pool          | 1.36 ms                                                                                                           | 1.81 ms: 1.33x slower                                                                                                   |
| richards_super             | 61.5 ms                                                                                                           | 82.0 ms: 1.33x slower                                                                                                   |
| python_startup             | 15.0 ms                                                                                                           | 20.0 ms: 1.34x slower                                                                                                   |
| richards                   | 52.2 ms                                                                                                           | 69.8 ms: 1.34x slower                                                                                                   |
| coverage                   | 105 ms                                                                                                            | 142 ms: 1.35x slower                                                                                                    |
| python_startup_no_site     | 8.59 ms                                                                                                           | 12.1 ms: 1.41x slower                                                                                                   |
| unpack_sequence            | 52.2 ns                                                                                                           | 74.4 ns: 1.43x slower                                                                                                   |
| nbody                      | 123 ms                                                                                                            | 181 ms: 1.48x slower                                                                                                    |
| mako                       | 13.6 ms                                                                                                           | 21.1 ms: 1.55x slower                                                                                                   |
| Geometric mean             | (ref)                                                                                                             | 1.09x slower                                                                                                            |

Benchmark hidden because not significant (8): pathlib, asyncio_websockets, pickle_dict, async_tree_none_tg, async_tree_io, pickle, regex_effbot, coroutines
Ignored benchmarks (1) of results/bm-20250712-3.15.0a0-47b01da/bm-20250712-arminc-aarch64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json: djangocms

- Geometric mean (including insignificant results): 1.124x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.13x
- 95% likely to have a slowdown of 1.12x
- 99% likely to have a slowdown of 1.11x

# Memory
- memory change: 1.19x