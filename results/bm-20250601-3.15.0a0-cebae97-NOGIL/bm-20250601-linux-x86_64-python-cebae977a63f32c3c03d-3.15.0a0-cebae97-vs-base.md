# Results vs. base

- fork: python
- ref: cebae977a63f32c3c03d
- machine: linux-x86_64
- commit hash: cebae97
- commit date: 2025-06-01
- overall geometric mean: 1.061x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x slower
- Memory change: 1.21x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250601-3.15.0a0-cebae97/bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json | results/bm-20250601-3.15.0a0-cebae97-NOGIL/bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json |
|----------------|:---------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 289 ms                                                                                                          | 340 ms: 1.17x slower                                                                                                  |
| docutils       | 2.84 sec                                                                                                        | 3.15 sec: 1.11x slower                                                                                                |
| html5lib       | 66.2 ms                                                                                                         | 74.6 ms: 1.13x slower                                                                                                 |
| sphinx         | 1.12 sec                                                                                                        | 1.26 sec: 1.12x slower                                                                                                |
| Geometric mean | (ref)                                                                                                           | 1.13x slower                                                                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20250601-3.15.0a0-cebae97/bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json | results/bm-20250601-3.15.0a0-cebae97-NOGIL/bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json |
|----------------------------|:---------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| async_tree_io_tg           | 696 ms                                                                                                          | 601 ms: 1.16x faster                                                                                                  |
| async_tree_none_tg         | 279 ms                                                                                                          | 261 ms: 1.07x faster                                                                                                  |
| async_tree_io              | 662 ms                                                                                                          | 637 ms: 1.04x faster                                                                                                  |
| async_tree_memoization_tg  | 352 ms                                                                                                          | 339 ms: 1.04x faster                                                                                                  |
| async_tree_cpu_io_mixed_tg | 598 ms                                                                                                          | 580 ms: 1.03x faster                                                                                                  |
| async_tree_cpu_io_mixed    | 607 ms                                                                                                          | 621 ms: 1.02x slower                                                                                                  |
| async_tree_none            | 291 ms                                                                                                          | 300 ms: 1.03x slower                                                                                                  |
| coroutines                 | 28.1 ms                                                                                                         | 29.5 ms: 1.05x slower                                                                                                 |
| async_tree_memoization     | 350 ms                                                                                                          | 377 ms: 1.08x slower                                                                                                  |
| async_generators           | 416 ms                                                                                                          | 453 ms: 1.09x slower                                                                                                  |
| asyncio_tcp_ssl            | 1.82 sec                                                                                                        | 2.04 sec: 1.13x slower                                                                                                |
| asyncio_tcp                | 484 ms                                                                                                          | 545 ms: 1.13x slower                                                                                                  |
| Geometric mean             | (ref)                                                                                                           | 1.01x slower                                                                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20250601-3.15.0a0-cebae97/bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json | results/bm-20250601-3.15.0a0-cebae97-NOGIL/bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json |
|----------------|:---------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| pidigits       | 202 ms                                                                                                          | 199 ms: 1.02x faster                                                                                                  |
| float          | 75.1 ms                                                                                                         | 80.4 ms: 1.07x slower                                                                                                 |
| nbody          | 109 ms                                                                                                          | 151 ms: 1.38x slower                                                                                                  |
| Geometric mean | (ref)                                                                                                           | 1.13x slower                                                                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20250601-3.15.0a0-cebae97/bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json | results/bm-20250601-3.15.0a0-cebae97-NOGIL/bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json |
|----------------|:---------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| regex_dna      | 204 ms                                                                                                          | 204 ms: 1.00x slower                                                                                                  |
| regex_v8       | 24.0 ms                                                                                                         | 24.5 ms: 1.02x slower                                                                                                 |
| regex_effbot   | 3.00 ms                                                                                                         | 3.29 ms: 1.09x slower                                                                                                 |
| regex_compile  | 143 ms                                                                                                          | 172 ms: 1.20x slower                                                                                                  |
| Geometric mean | (ref)                                                                                                           | 1.08x slower                                                                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20250601-3.15.0a0-cebae97/bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json | results/bm-20250601-3.15.0a0-cebae97-NOGIL/bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json |
|----------------------|:---------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| xml_etree_iterparse  | 111 ms                                                                                                          | 106 ms: 1.04x faster                                                                                                  |
| pickle_list          | 5.85 us                                                                                                         | 5.77 us: 1.01x faster                                                                                                 |
| pickle_dict          | 36.2 us                                                                                                         | 36.0 us: 1.01x faster                                                                                                 |
| xml_etree_parse      | 161 ms                                                                                                          | 165 ms: 1.02x slower                                                                                                  |
| json_loads           | 33.9 us                                                                                                         | 37.4 us: 1.10x slower                                                                                                 |
| pickle_pure_python   | 380 us                                                                                                          | 418 us: 1.10x slower                                                                                                  |
| unpickle_list        | 5.59 us                                                                                                         | 6.36 us: 1.14x slower                                                                                                 |
| json_dumps           | 13.3 ms                                                                                                         | 15.2 ms: 1.14x slower                                                                                                 |
| tomli_loads          | 2.25 sec                                                                                                        | 2.60 sec: 1.16x slower                                                                                                |
| xml_etree_generate   | 107 ms                                                                                                          | 124 ms: 1.16x slower                                                                                                  |
| unpickle             | 18.9 us                                                                                                         | 22.0 us: 1.17x slower                                                                                                 |
| xml_etree_process    | 73.6 ms                                                                                                         | 86.8 ms: 1.18x slower                                                                                                 |
| unpickle_pure_python | 255 us                                                                                                          | 304 us: 1.19x slower                                                                                                  |
| Geometric mean       | (ref)                                                                                                           | 1.09x slower                                                                                                          |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20250601-3.15.0a0-cebae97/bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json | results/bm-20250601-3.15.0a0-cebae97-NOGIL/bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json |
|------------------------|:---------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                                                                         | 17.1 ms: 1.30x slower                                                                                                 |
| python_startup_no_site | 7.42 ms                                                                                                         | 10.00 ms: 1.35x slower                                                                                                |
| Geometric mean         | (ref)                                                                                                           | 1.32x slower                                                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20250601-3.15.0a0-cebae97/bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json | results/bm-20250601-3.15.0a0-cebae97-NOGIL/bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json |
|-----------------|:---------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| genshi_xml      | 57.5 ms                                                                                                         | 73.1 ms: 1.27x slower                                                                                                 |
| django_template | 40.3 ms                                                                                                         | 52.6 ms: 1.30x slower                                                                                                 |
| genshi_text     | 25.0 ms                                                                                                         | 34.1 ms: 1.36x slower                                                                                                 |
| mako            | 13.7 ms                                                                                                         | 19.0 ms: 1.39x slower                                                                                                 |
| Geometric mean  | (ref)                                                                                                           | 1.33x slower                                                                                                          |

All benchmarks:
===============

| Benchmark                  | results/bm-20250601-3.15.0a0-cebae97/bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json | results/bm-20250601-3.15.0a0-cebae97-NOGIL/bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json |
|----------------------------|:---------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| thrift                     | 149 ms                                                                                                          | 1.16 ms: 127.79x faster                                                                                               |
| coverage                   | 514 ms                                                                                                          | 133 ms: 3.88x faster                                                                                                  |
| gc_traversal               | 5.16 ms                                                                                                         | 2.74 ms: 1.88x faster                                                                                                 |
| create_gc_cycles           | 2.63 ms                                                                                                         | 1.88 ms: 1.40x faster                                                                                                 |
| async_tree_io_tg           | 696 ms                                                                                                          | 601 ms: 1.16x faster                                                                                                  |
| async_tree_none_tg         | 279 ms                                                                                                          | 261 ms: 1.07x faster                                                                                                  |
| xml_etree_iterparse        | 111 ms                                                                                                          | 106 ms: 1.04x faster                                                                                                  |
| async_tree_io              | 662 ms                                                                                                          | 637 ms: 1.04x faster                                                                                                  |
| async_tree_memoization_tg  | 352 ms                                                                                                          | 339 ms: 1.04x faster                                                                                                  |
| async_tree_cpu_io_mixed_tg | 598 ms                                                                                                          | 580 ms: 1.03x faster                                                                                                  |
| pidigits                   | 202 ms                                                                                                          | 199 ms: 1.02x faster                                                                                                  |
| pickle_list                | 5.85 us                                                                                                         | 5.77 us: 1.01x faster                                                                                                 |
| pickle_dict                | 36.2 us                                                                                                         | 36.0 us: 1.01x faster                                                                                                 |
| regex_dna                  | 204 ms                                                                                                          | 204 ms: 1.00x slower                                                                                                  |
| sqlite_synth               | 3.17 us                                                                                                         | 3.21 us: 1.01x slower                                                                                                 |
| regex_v8                   | 24.0 ms                                                                                                         | 24.5 ms: 1.02x slower                                                                                                 |
| xml_etree_parse            | 161 ms                                                                                                          | 165 ms: 1.02x slower                                                                                                  |
| async_tree_cpu_io_mixed    | 607 ms                                                                                                          | 621 ms: 1.02x slower                                                                                                  |
| async_tree_none            | 291 ms                                                                                                          | 300 ms: 1.03x slower                                                                                                  |
| pycparser                  | 1.25 sec                                                                                                        | 1.30 sec: 1.04x slower                                                                                                |
| coroutines                 | 28.1 ms                                                                                                         | 29.5 ms: 1.05x slower                                                                                                 |
| k_core                     | 2.41 sec                                                                                                        | 2.56 sec: 1.07x slower                                                                                                |
| float                      | 75.1 ms                                                                                                         | 80.4 ms: 1.07x slower                                                                                                 |
| async_tree_memoization     | 350 ms                                                                                                          | 377 ms: 1.08x slower                                                                                                  |
| bench_mp_pool              | 104 ms                                                                                                          | 112 ms: 1.08x slower                                                                                                  |
| generators                 | 32.4 ms                                                                                                         | 35.0 ms: 1.08x slower                                                                                                 |
| json                       | 6.11 ms                                                                                                         | 6.62 ms: 1.08x slower                                                                                                 |
| pathlib                    | 18.2 ms                                                                                                         | 19.7 ms: 1.08x slower                                                                                                 |
| async_generators           | 416 ms                                                                                                          | 453 ms: 1.09x slower                                                                                                  |
| regex_effbot               | 3.00 ms                                                                                                         | 3.29 ms: 1.09x slower                                                                                                 |
| json_loads                 | 33.9 us                                                                                                         | 37.4 us: 1.10x slower                                                                                                 |
| pickle_pure_python         | 380 us                                                                                                          | 418 us: 1.10x slower                                                                                                  |
| shortest_path              | 529 ms                                                                                                          | 585 ms: 1.10x slower                                                                                                  |
| logging_silent             | 651 ns                                                                                                          | 720 ns: 1.11x slower                                                                                                  |
| docutils                   | 2.84 sec                                                                                                        | 3.15 sec: 1.11x slower                                                                                                |
| connected_components       | 487 ms                                                                                                          | 541 ms: 1.11x slower                                                                                                  |
| bpe_tokeniser              | 5.25 sec                                                                                                        | 5.84 sec: 1.11x slower                                                                                                |
| sphinx                     | 1.12 sec                                                                                                        | 1.26 sec: 1.12x slower                                                                                                |
| asyncio_tcp_ssl            | 1.82 sec                                                                                                        | 2.04 sec: 1.13x slower                                                                                                |
| asyncio_tcp                | 484 ms                                                                                                          | 545 ms: 1.13x slower                                                                                                  |
| html5lib                   | 66.2 ms                                                                                                         | 74.6 ms: 1.13x slower                                                                                                 |
| unpack_sequence            | 50.5 ns                                                                                                         | 57.3 ns: 1.13x slower                                                                                                 |
| scimark_fft                | 420 ms                                                                                                          | 477 ms: 1.14x slower                                                                                                  |
| dulwich_log                | 64.0 ms                                                                                                         | 72.7 ms: 1.14x slower                                                                                                 |
| unpickle_list              | 5.59 us                                                                                                         | 6.36 us: 1.14x slower                                                                                                 |
| scimark_sor                | 136 ms                                                                                                          | 155 ms: 1.14x slower                                                                                                  |
| json_dumps                 | 13.3 ms                                                                                                         | 15.2 ms: 1.14x slower                                                                                                 |
| pylint                     | 310 ms                                                                                                          | 358 ms: 1.15x slower                                                                                                  |
| tomli_loads                | 2.25 sec                                                                                                        | 2.60 sec: 1.16x slower                                                                                                |
| xml_etree_generate         | 107 ms                                                                                                          | 124 ms: 1.16x slower                                                                                                  |
| pyflate                    | 476 ms                                                                                                          | 552 ms: 1.16x slower                                                                                                  |
| sqlglot_v2_normalize       | 126 ms                                                                                                          | 147 ms: 1.16x slower                                                                                                  |
| meteor_contest             | 116 ms                                                                                                          | 135 ms: 1.16x slower                                                                                                  |
| sqlglot_v2_optimize        | 62.0 ms                                                                                                         | 72.2 ms: 1.16x slower                                                                                                 |
| unpickle                   | 18.9 us                                                                                                         | 22.0 us: 1.17x slower                                                                                                 |
| sympy_expand               | 534 ms                                                                                                          | 624 ms: 1.17x slower                                                                                                  |
| go                         | 119 ms                                                                                                          | 140 ms: 1.17x slower                                                                                                  |
| 2to3                       | 289 ms                                                                                                          | 340 ms: 1.17x slower                                                                                                  |
| chaos                      | 69.9 ms                                                                                                         | 82.0 ms: 1.17x slower                                                                                                 |
| many_optionals             | 1.07 ms                                                                                                         | 1.26 ms: 1.17x slower                                                                                                 |
| mdp                        | 1.47 sec                                                                                                        | 1.73 sec: 1.18x slower                                                                                                |
| deltablue                  | 3.86 ms                                                                                                         | 4.54 ms: 1.18x slower                                                                                                 |
| spectral_norm              | 113 ms                                                                                                          | 134 ms: 1.18x slower                                                                                                  |
| xml_etree_process          | 73.6 ms                                                                                                         | 86.8 ms: 1.18x slower                                                                                                 |
| fannkuch                   | 491 ms                                                                                                          | 581 ms: 1.18x slower                                                                                                  |
| pprint_safe_repr           | 988 ms                                                                                                          | 1.17 sec: 1.18x slower                                                                                                |
| comprehensions             | 19.1 us                                                                                                         | 22.6 us: 1.19x slower                                                                                                 |
| nqueens                    | 99.3 ms                                                                                                         | 118 ms: 1.19x slower                                                                                                  |
| logging_format             | 8.58 us                                                                                                         | 10.2 us: 1.19x slower                                                                                                 |
| sympy_str                  | 307 ms                                                                                                          | 366 ms: 1.19x slower                                                                                                  |
| sympy_sum                  | 166 ms                                                                                                          | 198 ms: 1.19x slower                                                                                                  |
| scimark_sparse_mat_mult    | 5.78 ms                                                                                                         | 6.89 ms: 1.19x slower                                                                                                 |
| unpickle_pure_python       | 255 us                                                                                                          | 304 us: 1.19x slower                                                                                                  |
| hexiom                     | 6.66 ms                                                                                                         | 7.95 ms: 1.19x slower                                                                                                 |
| sympy_integrate            | 20.9 ms                                                                                                         | 25.0 ms: 1.20x slower                                                                                                 |
| regex_compile              | 143 ms                                                                                                          | 172 ms: 1.20x slower                                                                                                  |
| deepcopy                   | 310 us                                                                                                          | 371 us: 1.20x slower                                                                                                  |
| pprint_pformat             | 2.01 sec                                                                                                        | 2.41 sec: 1.20x slower                                                                                                |
| deepcopy_memo              | 34.0 us                                                                                                         | 40.9 us: 1.20x slower                                                                                                 |
| logging_simple             | 7.52 us                                                                                                         | 9.07 us: 1.20x slower                                                                                                 |
| typing_runtime_protocols   | 195 us                                                                                                          | 235 us: 1.21x slower                                                                                                  |
| deepcopy_reduce            | 3.30 us                                                                                                         | 4.02 us: 1.22x slower                                                                                                 |
| raytrace                   | 319 ms                                                                                                          | 388 ms: 1.22x slower                                                                                                  |
| richards                   | 54.3 ms                                                                                                         | 67.0 ms: 1.23x slower                                                                                                 |
| subparsers                 | 28.0 ms                                                                                                         | 34.6 ms: 1.24x slower                                                                                                 |
| scimark_lu                 | 134 ms                                                                                                          | 167 ms: 1.24x slower                                                                                                  |
| sqlglot_v2_transpile       | 1.75 ms                                                                                                         | 2.18 ms: 1.25x slower                                                                                                 |
| telco                      | 9.39 ms                                                                                                         | 11.8 ms: 1.26x slower                                                                                                 |
| sqlglot_v2_parse           | 1.40 ms                                                                                                         | 1.78 ms: 1.27x slower                                                                                                 |
| genshi_xml                 | 57.5 ms                                                                                                         | 73.1 ms: 1.27x slower                                                                                                 |
| crypto_pyaes               | 87.1 ms                                                                                                         | 112 ms: 1.29x slower                                                                                                  |
| richards_super             | 61.5 ms                                                                                                         | 79.7 ms: 1.30x slower                                                                                                 |
| scimark_monte_carlo        | 78.2 ms                                                                                                         | 101 ms: 1.30x slower                                                                                                  |
| python_startup             | 13.2 ms                                                                                                         | 17.1 ms: 1.30x slower                                                                                                 |
| django_template            | 40.3 ms                                                                                                         | 52.6 ms: 1.30x slower                                                                                                 |
| python_startup_no_site     | 7.42 ms                                                                                                         | 10.00 ms: 1.35x slower                                                                                                |
| genshi_text                | 25.0 ms                                                                                                         | 34.1 ms: 1.36x slower                                                                                                 |
| nbody                      | 109 ms                                                                                                          | 151 ms: 1.38x slower                                                                                                  |
| mako                       | 13.7 ms                                                                                                         | 19.0 ms: 1.39x slower                                                                                                 |
| bench_thread_pool          | 957 us                                                                                                          | 3.51 ms: 3.67x slower                                                                                                 |
| Geometric mean             | (ref)                                                                                                           | 1.07x slower                                                                                                          |

Benchmark hidden because not significant (2): asyncio_websockets, pickle

- Geometric mean (including insignificant results): 1.061x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.11x
- 95% likely to have a slowdown of 1.11x
- 99% likely to have a slowdown of 1.09x

# Memory
- memory change: 1.21x