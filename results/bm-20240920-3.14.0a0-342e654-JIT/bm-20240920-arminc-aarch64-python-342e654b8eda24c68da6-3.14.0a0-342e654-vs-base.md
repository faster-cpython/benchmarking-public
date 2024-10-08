# Results vs. base

- fork: python
- ref: 342e654b8eda24c68da6
- machine: linux-aarch64
- commit hash: 342e654
- commit date: 2024-09-20
- overall geometric mean: 1.12x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240920-3.14.0a0-342e654/bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json | results/bm-20240920-3.14.0a0-342e654-JIT/bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 296 ms                                                                                                            | 382 ms: 1.29x slower                                                                                                  |
| docutils       | 3.02 sec                                                                                                          | 3.94 sec: 1.31x slower                                                                                                |
| html5lib       | 64.4 ms                                                                                                           | 71.9 ms: 1.12x slower                                                                                                 |
| tornado_http   | 125 ms                                                                                                            | 150 ms: 1.20x slower                                                                                                  |
| Geometric mean | (ref)                                                                                                             | 1.22x slower                                                                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20240920-3.14.0a0-342e654/bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json | results/bm-20240920-3.14.0a0-342e654-JIT/bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json |
|----------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 725 ms                                                                                                            | 735 ms: 1.01x slower                                                                                                  |
| async_tree_io              | 1.13 sec                                                                                                          | 1.15 sec: 1.02x slower                                                                                                |
| async_tree_cpu_io_mixed    | 728 ms                                                                                                            | 748 ms: 1.03x slower                                                                                                  |
| asyncio_tcp_ssl            | 2.19 sec                                                                                                          | 2.27 sec: 1.04x slower                                                                                                |
| async_tree_none            | 424 ms                                                                                                            | 442 ms: 1.04x slower                                                                                                  |
| async_tree_memoization     | 563 ms                                                                                                            | 589 ms: 1.05x slower                                                                                                  |
| async_generators           | 481 ms                                                                                                            | 512 ms: 1.06x slower                                                                                                  |
| asyncio_tcp                | 557 ms                                                                                                            | 629 ms: 1.13x slower                                                                                                  |
| Geometric mean             | (ref)                                                                                                             | 1.03x slower                                                                                                          |

Benchmark hidden because not significant (5): async_tree_io_tg, coroutines, async_tree_memoization_tg, asyncio_websockets, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20240920-3.14.0a0-342e654/bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json | results/bm-20240920-3.14.0a0-342e654-JIT/bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| float          | 93.1 ms                                                                                                           | 87.5 ms: 1.06x faster                                                                                                 |
| nbody          | 112 ms                                                                                                            | 114 ms: 1.02x slower                                                                                                  |
| Geometric mean | (ref)                                                                                                             | 1.01x faster                                                                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240920-3.14.0a0-342e654/bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json | results/bm-20240920-3.14.0a0-342e654-JIT/bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| regex_dna      | 248 ms                                                                                                            | 252 ms: 1.02x slower                                                                                                  |
| regex_v8       | 30.6 ms                                                                                                           | 31.1 ms: 1.02x slower                                                                                                 |
| regex_compile  | 126 ms                                                                                                            | 196 ms: 1.55x slower                                                                                                  |
| Geometric mean | (ref)                                                                                                             | 1.13x slower                                                                                                          |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20240920-3.14.0a0-342e654/bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json | results/bm-20240920-3.14.0a0-342e654-JIT/bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json |
|----------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| unpickle_list        | 6.55 us                                                                                                           | 6.42 us: 1.02x faster                                                                                                 |
| unpickle             | 19.5 us                                                                                                           | 19.3 us: 1.01x faster                                                                                                 |
| pickle_list          | 5.24 us                                                                                                           | 5.20 us: 1.01x faster                                                                                                 |
| json_dumps           | 13.2 ms                                                                                                           | 13.5 ms: 1.02x slower                                                                                                 |
| unpickle_pure_python | 256 us                                                                                                            | 267 us: 1.04x slower                                                                                                  |
| pickle_pure_python   | 366 us                                                                                                            | 392 us: 1.07x slower                                                                                                  |
| Geometric mean       | (ref)                                                                                                             | 1.00x slower                                                                                                          |

Benchmark hidden because not significant (8): xml_etree_iterparse, xml_etree_generate, json_loads, xml_etree_parse, pickle, xml_etree_process, tomli_loads, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20240920-3.14.0a0-342e654/bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json | results/bm-20240920-3.14.0a0-342e654-JIT/bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json |
|------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 13.0 ms                                                                                                           | 13.1 ms: 1.01x slower                                                                                                 |
| python_startup_no_site | 8.63 ms                                                                                                           | 8.79 ms: 1.02x slower                                                                                                 |
| Geometric mean         | (ref)                                                                                                             | 1.01x slower                                                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20240920-3.14.0a0-342e654/bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json | results/bm-20240920-3.14.0a0-342e654-JIT/bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json |
|-----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| mako            | 13.4 ms                                                                                                           | 12.9 ms: 1.04x faster                                                                                                 |
| django_template | 42.5 ms                                                                                                           | 51.4 ms: 1.21x slower                                                                                                 |
| genshi_text     | 27.1 ms                                                                                                           | 35.0 ms: 1.29x slower                                                                                                 |
| genshi_xml      | 59.4 ms                                                                                                           | 80.8 ms: 1.36x slower                                                                                                 |
| Geometric mean  | (ref)                                                                                                             | 1.20x slower                                                                                                          |

All benchmarks:
===============

| Benchmark                  | results/bm-20240920-3.14.0a0-342e654/bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json | results/bm-20240920-3.14.0a0-342e654-JIT/bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json |
|----------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| float                      | 93.1 ms                                                                                                           | 87.5 ms: 1.06x faster                                                                                                 |
| sqlite_synth               | 4.00 us                                                                                                           | 3.84 us: 1.04x faster                                                                                                 |
| mako                       | 13.4 ms                                                                                                           | 12.9 ms: 1.04x faster                                                                                                 |
| scimark_sor                | 157 ms                                                                                                            | 152 ms: 1.03x faster                                                                                                  |
| unpickle_list              | 6.55 us                                                                                                           | 6.42 us: 1.02x faster                                                                                                 |
| unpickle                   | 19.5 us                                                                                                           | 19.3 us: 1.01x faster                                                                                                 |
| pickle_list                | 5.24 us                                                                                                           | 5.20 us: 1.01x faster                                                                                                 |
| python_startup             | 13.0 ms                                                                                                           | 13.1 ms: 1.01x slower                                                                                                 |
| async_tree_cpu_io_mixed_tg | 725 ms                                                                                                            | 735 ms: 1.01x slower                                                                                                  |
| bpe_tokeniser              | 5.89 sec                                                                                                          | 5.98 sec: 1.01x slower                                                                                                |
| regex_dna                  | 248 ms                                                                                                            | 252 ms: 1.02x slower                                                                                                  |
| regex_v8                   | 30.6 ms                                                                                                           | 31.1 ms: 1.02x slower                                                                                                 |
| python_startup_no_site     | 8.63 ms                                                                                                           | 8.79 ms: 1.02x slower                                                                                                 |
| async_tree_io              | 1.13 sec                                                                                                          | 1.15 sec: 1.02x slower                                                                                                |
| json_dumps                 | 13.2 ms                                                                                                           | 13.5 ms: 1.02x slower                                                                                                 |
| nbody                      | 112 ms                                                                                                            | 114 ms: 1.02x slower                                                                                                  |
| json                       | 5.53 ms                                                                                                           | 5.67 ms: 1.03x slower                                                                                                 |
| async_tree_cpu_io_mixed    | 728 ms                                                                                                            | 748 ms: 1.03x slower                                                                                                  |
| coverage                   | 99.1 ms                                                                                                           | 102 ms: 1.03x slower                                                                                                  |
| asyncio_tcp_ssl            | 2.19 sec                                                                                                          | 2.27 sec: 1.04x slower                                                                                                |
| logging_silent             | 132 ns                                                                                                            | 137 ns: 1.04x slower                                                                                                  |
| pathlib                    | 20.9 ms                                                                                                           | 21.7 ms: 1.04x slower                                                                                                 |
| spectral_norm              | 140 ms                                                                                                            | 146 ms: 1.04x slower                                                                                                  |
| thrift                     | 933 us                                                                                                            | 970 us: 1.04x slower                                                                                                  |
| unpickle_pure_python       | 256 us                                                                                                            | 267 us: 1.04x slower                                                                                                  |
| scimark_fft                | 441 ms                                                                                                            | 459 ms: 1.04x slower                                                                                                  |
| async_tree_none            | 424 ms                                                                                                            | 442 ms: 1.04x slower                                                                                                  |
| async_tree_memoization     | 563 ms                                                                                                            | 589 ms: 1.05x slower                                                                                                  |
| mdp                        | 3.34 sec                                                                                                          | 3.52 sec: 1.05x slower                                                                                                |
| bench_mp_pool              | 7.14 ms                                                                                                           | 7.57 ms: 1.06x slower                                                                                                 |
| async_generators           | 481 ms                                                                                                            | 512 ms: 1.06x slower                                                                                                  |
| scimark_sparse_mat_mult    | 6.41 ms                                                                                                           | 6.85 ms: 1.07x slower                                                                                                 |
| logging_simple             | 6.98 us                                                                                                           | 7.46 us: 1.07x slower                                                                                                 |
| pickle_pure_python         | 366 us                                                                                                            | 392 us: 1.07x slower                                                                                                  |
| logging_format             | 7.63 us                                                                                                           | 8.20 us: 1.07x slower                                                                                                 |
| bench_thread_pool          | 1.24 ms                                                                                                           | 1.35 ms: 1.09x slower                                                                                                 |
| scimark_lu                 | 136 ms                                                                                                            | 148 ms: 1.09x slower                                                                                                  |
| crypto_pyaes               | 81.9 ms                                                                                                           | 89.7 ms: 1.09x slower                                                                                                 |
| typing_runtime_protocols   | 195 us                                                                                                            | 213 us: 1.10x slower                                                                                                  |
| deepcopy_reduce            | 3.48 us                                                                                                           | 3.83 us: 1.10x slower                                                                                                 |
| scimark_monte_carlo        | 83.9 ms                                                                                                           | 92.6 ms: 1.10x slower                                                                                                 |
| fannkuch                   | 460 ms                                                                                                            | 508 ms: 1.11x slower                                                                                                  |
| meteor_contest             | 112 ms                                                                                                            | 124 ms: 1.11x slower                                                                                                  |
| deltablue                  | 3.94 ms                                                                                                           | 4.39 ms: 1.11x slower                                                                                                 |
| html5lib                   | 64.4 ms                                                                                                           | 71.9 ms: 1.12x slower                                                                                                 |
| asyncio_tcp                | 557 ms                                                                                                            | 629 ms: 1.13x slower                                                                                                  |
| raytrace                   | 305 ms                                                                                                            | 348 ms: 1.14x slower                                                                                                  |
| pyflate                    | 564 ms                                                                                                            | 657 ms: 1.17x slower                                                                                                  |
| sqlglot_normalize          | 127 ms                                                                                                            | 150 ms: 1.18x slower                                                                                                  |
| comprehensions             | 20.6 us                                                                                                           | 24.5 us: 1.19x slower                                                                                                 |
| tornado_http               | 125 ms                                                                                                            | 150 ms: 1.20x slower                                                                                                  |
| django_template            | 42.5 ms                                                                                                           | 51.4 ms: 1.21x slower                                                                                                 |
| sqlglot_parse              | 1.44 ms                                                                                                           | 1.76 ms: 1.22x slower                                                                                                 |
| deepcopy                   | 329 us                                                                                                            | 401 us: 1.22x slower                                                                                                  |
| pycparser                  | 1.22 sec                                                                                                          | 1.53 sec: 1.25x slower                                                                                                |
| richards                   | 53.0 ms                                                                                                           | 66.3 ms: 1.25x slower                                                                                                 |
| sqlglot_transpile          | 1.77 ms                                                                                                           | 2.23 ms: 1.26x slower                                                                                                 |
| richards_super             | 59.9 ms                                                                                                           | 75.9 ms: 1.27x slower                                                                                                 |
| sqlglot_optimize           | 61.7 ms                                                                                                           | 78.5 ms: 1.27x slower                                                                                                 |
| nqueens                    | 98.4 ms                                                                                                           | 126 ms: 1.28x slower                                                                                                  |
| 2to3                       | 296 ms                                                                                                            | 382 ms: 1.29x slower                                                                                                  |
| genshi_text                | 27.1 ms                                                                                                           | 35.0 ms: 1.29x slower                                                                                                 |
| docutils                   | 3.02 sec                                                                                                          | 3.94 sec: 1.31x slower                                                                                                |
| chaos                      | 69.6 ms                                                                                                           | 92.2 ms: 1.33x slower                                                                                                 |
| pylint                     | 359 ms                                                                                                            | 479 ms: 1.33x slower                                                                                                  |
| sympy_expand               | 459 ms                                                                                                            | 613 ms: 1.33x slower                                                                                                  |
| pprint_safe_repr           | 920 ms                                                                                                            | 1.25 sec: 1.35x slower                                                                                                |
| genshi_xml                 | 59.4 ms                                                                                                           | 80.8 ms: 1.36x slower                                                                                                 |
| go                         | 138 ms                                                                                                            | 190 ms: 1.37x slower                                                                                                  |
| pprint_pformat             | 1.89 sec                                                                                                          | 2.61 sec: 1.38x slower                                                                                                |
| sympy_integrate            | 20.7 ms                                                                                                           | 28.5 ms: 1.38x slower                                                                                                 |
| dulwich_log                | 59.1 ms                                                                                                           | 82.0 ms: 1.39x slower                                                                                                 |
| sympy_str                  | 263 ms                                                                                                            | 369 ms: 1.40x slower                                                                                                  |
| hexiom                     | 7.19 ms                                                                                                           | 10.3 ms: 1.44x slower                                                                                                 |
| sympy_sum                  | 141 ms                                                                                                            | 211 ms: 1.49x slower                                                                                                  |
| regex_compile              | 126 ms                                                                                                            | 196 ms: 1.55x slower                                                                                                  |
| generators                 | 34.7 ms                                                                                                           | 57.6 ms: 1.66x slower                                                                                                 |
| unpack_sequence            | 55.1 ns                                                                                                           | 150 ns: 2.73x slower                                                                                                  |
| Geometric mean             | (ref)                                                                                                             | 1.12x slower                                                                                                          |

Benchmark hidden because not significant (19): async_tree_io_tg, xml_etree_iterparse, xml_etree_generate, json_loads, xml_etree_parse, deepcopy_memo, gc_traversal, pickle, xml_etree_process, tomli_loads, regex_effbot, coroutines, pidigits, pickle_dict, async_tree_memoization_tg, asyncio_websockets, telco, create_gc_cycles, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: 1.09x