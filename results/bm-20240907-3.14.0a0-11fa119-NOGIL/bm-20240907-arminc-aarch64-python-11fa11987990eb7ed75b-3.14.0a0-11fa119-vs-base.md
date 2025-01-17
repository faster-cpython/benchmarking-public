# Results vs. base

- fork: python
- ref: 11fa11987990eb7ed75b
- machine: linux-aarch64
- commit hash: 11fa119
- commit date: 2024-09-07
- overall geometric mean: 1.383x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.45x slower
- Memory change: 1.16x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240907-3.14.0a0-11fa119/bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119.json | results/bm-20240907-3.14.0a0-11fa119-NOGIL/bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 293 ms                                                                                                            | 518 ms: 1.76x slower                                                                                                    |
| docutils       | 3.05 sec                                                                                                          | 4.10 sec: 1.34x slower                                                                                                  |
| html5lib       | 63.1 ms                                                                                                           | 121 ms: 1.92x slower                                                                                                    |
| tornado_http   | 124 ms                                                                                                            | 207 ms: 1.66x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                             | 1.66x slower                                                                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20240907-3.14.0a0-11fa119/bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119.json | results/bm-20240907-3.14.0a0-11fa119-NOGIL/bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119.json |
|----------------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| asyncio_websockets         | 659 ms                                                                                                            | 672 ms: 1.02x slower                                                                                                    |
| async_tree_io_tg           | 1.18 sec                                                                                                          | 1.36 sec: 1.15x slower                                                                                                  |
| asyncio_tcp_ssl            | 2.20 sec                                                                                                          | 2.62 sec: 1.19x slower                                                                                                  |
| asyncio_tcp                | 574 ms                                                                                                            | 683 ms: 1.19x slower                                                                                                    |
| async_tree_cpu_io_mixed_tg | 725 ms                                                                                                            | 871 ms: 1.20x slower                                                                                                    |
| async_tree_io              | 1.13 sec                                                                                                          | 1.41 sec: 1.24x slower                                                                                                  |
| async_tree_cpu_io_mixed    | 733 ms                                                                                                            | 914 ms: 1.25x slower                                                                                                    |
| async_tree_memoization_tg  | 549 ms                                                                                                            | 699 ms: 1.27x slower                                                                                                    |
| async_tree_memoization     | 556 ms                                                                                                            | 739 ms: 1.33x slower                                                                                                    |
| async_generators           | 487 ms                                                                                                            | 653 ms: 1.34x slower                                                                                                    |
| async_tree_none_tg         | 416 ms                                                                                                            | 572 ms: 1.38x slower                                                                                                    |
| coroutines                 | 28.6 ms                                                                                                           | 40.9 ms: 1.43x slower                                                                                                   |
| async_tree_none            | 423 ms                                                                                                            | 625 ms: 1.48x slower                                                                                                    |
| Geometric mean             | (ref)                                                                                                             | 1.26x slower                                                                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20240907-3.14.0a0-11fa119/bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119.json | results/bm-20240907-3.14.0a0-11fa119-NOGIL/bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| float          | 92.7 ms                                                                                                           | 207 ms: 2.24x slower                                                                                                    |
| nbody          | 109 ms                                                                                                            | 281 ms: 2.57x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                             | 1.79x slower                                                                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240907-3.14.0a0-11fa119/bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119.json | results/bm-20240907-3.14.0a0-11fa119-NOGIL/bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| regex_effbot   | 4.89 ms                                                                                                           | 4.48 ms: 1.09x faster                                                                                                   |
| regex_dna      | 252 ms                                                                                                            | 261 ms: 1.04x slower                                                                                                    |
| regex_v8       | 30.3 ms                                                                                                           | 33.0 ms: 1.09x slower                                                                                                   |
| regex_compile  | 125 ms                                                                                                            | 259 ms: 2.08x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                             | 1.21x slower                                                                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20240907-3.14.0a0-11fa119/bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119.json | results/bm-20240907-3.14.0a0-11fa119-NOGIL/bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119.json |
|----------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| pickle               | 13.5 us                                                                                                           | 13.3 us: 1.02x faster                                                                                                   |
| pickle_dict          | 37.5 us                                                                                                           | 38.8 us: 1.03x slower                                                                                                   |
| xml_etree_iterparse  | 148 ms                                                                                                            | 157 ms: 1.06x slower                                                                                                    |
| unpickle             | 19.6 us                                                                                                           | 21.7 us: 1.11x slower                                                                                                   |
| unpickle_list        | 6.28 us                                                                                                           | 6.99 us: 1.11x slower                                                                                                   |
| json_loads           | 32.5 us                                                                                                           | 39.3 us: 1.21x slower                                                                                                   |
| json_dumps           | 13.3 ms                                                                                                           | 17.9 ms: 1.34x slower                                                                                                   |
| xml_etree_generate   | 111 ms                                                                                                            | 163 ms: 1.47x slower                                                                                                    |
| tomli_loads          | 2.65 sec                                                                                                          | 4.19 sec: 1.58x slower                                                                                                  |
| xml_etree_process    | 78.5 ms                                                                                                           | 130 ms: 1.66x slower                                                                                                    |
| unpickle_pure_python | 255 us                                                                                                            | 542 us: 2.13x slower                                                                                                    |
| pickle_pure_python   | 361 us                                                                                                            | 777 us: 2.15x slower                                                                                                    |
| Geometric mean       | (ref)                                                                                                             | 1.30x slower                                                                                                            |

Benchmark hidden because not significant (2): xml_etree_parse, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20240907-3.14.0a0-11fa119/bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119.json | results/bm-20240907-3.14.0a0-11fa119-NOGIL/bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119.json |
|------------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                                                                           | 18.2 ms: 1.38x slower                                                                                                   |
| python_startup_no_site | 8.83 ms                                                                                                           | 12.2 ms: 1.38x slower                                                                                                   |
| Geometric mean         | (ref)                                                                                                             | 1.38x slower                                                                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20240907-3.14.0a0-11fa119/bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119.json | results/bm-20240907-3.14.0a0-11fa119-NOGIL/bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119.json |
|-----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| genshi_xml      | 60.6 ms                                                                                                           | 104 ms: 1.71x slower                                                                                                    |
| genshi_text     | 27.5 ms                                                                                                           | 53.3 ms: 1.94x slower                                                                                                   |
| django_template | 41.7 ms                                                                                                           | 83.4 ms: 2.00x slower                                                                                                   |
| mako            | 13.4 ms                                                                                                           | 28.9 ms: 2.15x slower                                                                                                   |
| Geometric mean  | (ref)                                                                                                             | 1.94x slower                                                                                                            |

All benchmarks:
===============

| Benchmark                  | results/bm-20240907-3.14.0a0-11fa119/bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119.json | results/bm-20240907-3.14.0a0-11fa119-NOGIL/bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119.json |
|----------------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| gc_traversal               | 4.91 ms                                                                                                           | 3.45 ms: 1.42x faster                                                                                                   |
| create_gc_cycles           | 2.30 ms                                                                                                           | 1.62 ms: 1.42x faster                                                                                                   |
| regex_effbot               | 4.89 ms                                                                                                           | 4.48 ms: 1.09x faster                                                                                                   |
| pickle                     | 13.5 us                                                                                                           | 13.3 us: 1.02x faster                                                                                                   |
| asyncio_websockets         | 659 ms                                                                                                            | 672 ms: 1.02x slower                                                                                                    |
| bench_mp_pool              | 7.02 ms                                                                                                           | 7.20 ms: 1.03x slower                                                                                                   |
| pickle_dict                | 37.5 us                                                                                                           | 38.8 us: 1.03x slower                                                                                                   |
| regex_dna                  | 252 ms                                                                                                            | 261 ms: 1.04x slower                                                                                                    |
| xml_etree_iterparse        | 148 ms                                                                                                            | 157 ms: 1.06x slower                                                                                                    |
| sqlite_synth               | 3.90 us                                                                                                           | 4.17 us: 1.07x slower                                                                                                   |
| regex_v8                   | 30.3 ms                                                                                                           | 33.0 ms: 1.09x slower                                                                                                   |
| unpickle                   | 19.6 us                                                                                                           | 21.7 us: 1.11x slower                                                                                                   |
| unpickle_list              | 6.28 us                                                                                                           | 6.99 us: 1.11x slower                                                                                                   |
| async_tree_io_tg           | 1.18 sec                                                                                                          | 1.36 sec: 1.15x slower                                                                                                  |
| asyncio_tcp_ssl            | 2.20 sec                                                                                                          | 2.62 sec: 1.19x slower                                                                                                  |
| asyncio_tcp                | 574 ms                                                                                                            | 683 ms: 1.19x slower                                                                                                    |
| async_tree_cpu_io_mixed_tg | 725 ms                                                                                                            | 871 ms: 1.20x slower                                                                                                    |
| json_loads                 | 32.5 us                                                                                                           | 39.3 us: 1.21x slower                                                                                                   |
| json                       | 5.70 ms                                                                                                           | 7.03 ms: 1.23x slower                                                                                                   |
| async_tree_io              | 1.13 sec                                                                                                          | 1.41 sec: 1.24x slower                                                                                                  |
| async_tree_cpu_io_mixed    | 733 ms                                                                                                            | 914 ms: 1.25x slower                                                                                                    |
| async_tree_memoization_tg  | 549 ms                                                                                                            | 699 ms: 1.27x slower                                                                                                    |
| pathlib                    | 21.0 ms                                                                                                           | 26.8 ms: 1.27x slower                                                                                                   |
| telco                      | 9.99 ms                                                                                                           | 12.8 ms: 1.28x slower                                                                                                   |
| scimark_fft                | 443 ms                                                                                                            | 573 ms: 1.29x slower                                                                                                    |
| mdp                        | 3.34 sec                                                                                                          | 4.32 sec: 1.30x slower                                                                                                  |
| async_tree_memoization     | 556 ms                                                                                                            | 739 ms: 1.33x slower                                                                                                    |
| async_generators           | 487 ms                                                                                                            | 653 ms: 1.34x slower                                                                                                    |
| json_dumps                 | 13.3 ms                                                                                                           | 17.9 ms: 1.34x slower                                                                                                   |
| docutils                   | 3.05 sec                                                                                                          | 4.10 sec: 1.34x slower                                                                                                  |
| coverage                   | 99.5 ms                                                                                                           | 136 ms: 1.36x slower                                                                                                    |
| async_tree_none_tg         | 416 ms                                                                                                            | 572 ms: 1.38x slower                                                                                                    |
| python_startup             | 13.2 ms                                                                                                           | 18.2 ms: 1.38x slower                                                                                                   |
| python_startup_no_site     | 8.83 ms                                                                                                           | 12.2 ms: 1.38x slower                                                                                                   |
| scimark_sparse_mat_mult    | 6.38 ms                                                                                                           | 8.82 ms: 1.38x slower                                                                                                   |
| pylint                     | 359 ms                                                                                                            | 511 ms: 1.42x slower                                                                                                    |
| coroutines                 | 28.6 ms                                                                                                           | 40.9 ms: 1.43x slower                                                                                                   |
| xml_etree_generate         | 111 ms                                                                                                            | 163 ms: 1.47x slower                                                                                                    |
| async_tree_none            | 423 ms                                                                                                            | 625 ms: 1.48x slower                                                                                                    |
| meteor_contest             | 112 ms                                                                                                            | 167 ms: 1.49x slower                                                                                                    |
| nqueens                    | 98.6 ms                                                                                                           | 152 ms: 1.55x slower                                                                                                    |
| tomli_loads                | 2.65 sec                                                                                                          | 4.19 sec: 1.58x slower                                                                                                  |
| spectral_norm              | 140 ms                                                                                                            | 226 ms: 1.61x slower                                                                                                    |
| fannkuch                   | 456 ms                                                                                                            | 738 ms: 1.62x slower                                                                                                    |
| bpe_tokeniser              | 5.83 sec                                                                                                          | 9.48 sec: 1.63x slower                                                                                                  |
| dulwich_log                | 58.8 ms                                                                                                           | 96.1 ms: 1.64x slower                                                                                                   |
| crypto_pyaes               | 83.4 ms                                                                                                           | 137 ms: 1.64x slower                                                                                                    |
| pycparser                  | 1.23 sec                                                                                                          | 2.02 sec: 1.64x slower                                                                                                  |
| generators                 | 35.1 ms                                                                                                           | 57.7 ms: 1.64x slower                                                                                                   |
| xml_etree_process          | 78.5 ms                                                                                                           | 130 ms: 1.66x slower                                                                                                    |
| tornado_http               | 124 ms                                                                                                            | 207 ms: 1.66x slower                                                                                                    |
| sympy_integrate            | 20.8 ms                                                                                                           | 34.7 ms: 1.67x slower                                                                                                   |
| genshi_xml                 | 60.6 ms                                                                                                           | 104 ms: 1.71x slower                                                                                                    |
| bench_thread_pool          | 1.24 ms                                                                                                           | 2.13 ms: 1.72x slower                                                                                                   |
| deepcopy                   | 332 us                                                                                                            | 571 us: 1.72x slower                                                                                                    |
| typing_runtime_protocols   | 192 us                                                                                                            | 336 us: 1.75x slower                                                                                                    |
| 2to3                       | 293 ms                                                                                                            | 518 ms: 1.76x slower                                                                                                    |
| deepcopy_reduce            | 3.45 us                                                                                                           | 6.14 us: 1.78x slower                                                                                                   |
| pyflate                    | 566 ms                                                                                                            | 1.02 sec: 1.80x slower                                                                                                  |
| thrift                     | 931 us                                                                                                            | 1.69 ms: 1.81x slower                                                                                                   |
| sqlglot_normalize          | 127 ms                                                                                                            | 237 ms: 1.86x slower                                                                                                    |
| deepcopy_memo              | 38.0 us                                                                                                           | 72.1 us: 1.90x slower                                                                                                   |
| sqlglot_optimize           | 62.5 ms                                                                                                           | 119 ms: 1.90x slower                                                                                                    |
| html5lib                   | 63.1 ms                                                                                                           | 121 ms: 1.92x slower                                                                                                    |
| pprint_pformat             | 1.89 sec                                                                                                          | 3.64 sec: 1.92x slower                                                                                                  |
| pprint_safe_repr           | 914 ms                                                                                                            | 1.76 sec: 1.92x slower                                                                                                  |
| genshi_text                | 27.5 ms                                                                                                           | 53.3 ms: 1.94x slower                                                                                                   |
| sympy_str                  | 265 ms                                                                                                            | 514 ms: 1.94x slower                                                                                                    |
| django_template            | 41.7 ms                                                                                                           | 83.4 ms: 2.00x slower                                                                                                   |
| comprehensions             | 20.4 us                                                                                                           | 40.9 us: 2.00x slower                                                                                                   |
| sympy_expand               | 464 ms                                                                                                            | 961 ms: 2.07x slower                                                                                                    |
| regex_compile              | 125 ms                                                                                                            | 259 ms: 2.08x slower                                                                                                    |
| logging_format             | 7.62 us                                                                                                           | 15.9 us: 2.09x slower                                                                                                   |
| logging_simple             | 6.95 us                                                                                                           | 14.6 us: 2.10x slower                                                                                                   |
| unpickle_pure_python       | 255 us                                                                                                            | 542 us: 2.13x slower                                                                                                    |
| logging_silent             | 133 ns                                                                                                            | 284 ns: 2.14x slower                                                                                                    |
| scimark_monte_carlo        | 82.0 ms                                                                                                           | 176 ms: 2.15x slower                                                                                                    |
| pickle_pure_python         | 361 us                                                                                                            | 777 us: 2.15x slower                                                                                                    |
| mako                       | 13.4 ms                                                                                                           | 28.9 ms: 2.15x slower                                                                                                   |
| scimark_sor                | 158 ms                                                                                                            | 341 ms: 2.16x slower                                                                                                    |
| richards                   | 52.8 ms                                                                                                           | 117 ms: 2.21x slower                                                                                                    |
| hexiom                     | 7.17 ms                                                                                                           | 15.9 ms: 2.22x slower                                                                                                   |
| sympy_sum                  | 143 ms                                                                                                            | 318 ms: 2.22x slower                                                                                                    |
| float                      | 92.7 ms                                                                                                           | 207 ms: 2.24x slower                                                                                                    |
| chaos                      | 68.5 ms                                                                                                           | 160 ms: 2.33x slower                                                                                                    |
| richards_super             | 59.5 ms                                                                                                           | 143 ms: 2.40x slower                                                                                                    |
| nbody                      | 109 ms                                                                                                            | 281 ms: 2.57x slower                                                                                                    |
| sqlglot_transpile          | 1.73 ms                                                                                                           | 4.45 ms: 2.58x slower                                                                                                   |
| sqlglot_parse              | 1.42 ms                                                                                                           | 3.67 ms: 2.59x slower                                                                                                   |
| scimark_lu                 | 134 ms                                                                                                            | 350 ms: 2.61x slower                                                                                                    |
| raytrace                   | 301 ms                                                                                                            | 815 ms: 2.70x slower                                                                                                    |
| go                         | 138 ms                                                                                                            | 404 ms: 2.93x slower                                                                                                    |
| deltablue                  | 3.91 ms                                                                                                           | 12.7 ms: 3.26x slower                                                                                                   |
| unpack_sequence            | 54.0 ns                                                                                                           | 182 ns: 3.38x slower                                                                                                    |
| Geometric mean             | (ref)                                                                                                             | 1.59x slower                                                                                                            |

Benchmark hidden because not significant (3): xml_etree_parse, pidigits, pickle_list

- Geometric mean (including insignificant results): 1.383x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.54x
- 95% likely to have a slowdown of 1.49x
- 99% likely to have a slowdown of 1.45x

# Memory
- memory change: 1.16x