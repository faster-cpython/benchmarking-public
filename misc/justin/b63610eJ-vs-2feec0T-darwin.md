Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231218-darwin-arm64-python-2feec0fc7fd0b9caae7a-3.13.0a2+-2feec0f | bm-20231219-darwin-arm64-brandtbucher-justin-3.13.0a2+-b63610e |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------:|
| 2to3           | 196 ms                                                                 | 182 ms: 1.07x faster                                           |
| chameleon      | 5.51 ms                                                                | 5.12 ms: 1.08x faster                                          |
| docutils       | 1.67 sec                                                               | 1.54 sec: 1.09x faster                                         |
| tornado_http   | 83.4 ms                                                                | 72.8 ms: 1.15x faster                                          |
| Geometric mean | (ref)                                                                  | 1.10x faster                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231218-darwin-arm64-python-2feec0fc7fd0b9caae7a-3.13.0a2+-2feec0f | bm-20231219-darwin-arm64-brandtbucher-justin-3.13.0a2+-b63610e |
|----------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------:|
| async_tree_none_tg         | 289 ms                                                                 | 264 ms: 1.09x faster                                           |
| async_tree_memoization_tg  | 360 ms                                                                 | 331 ms: 1.09x faster                                           |
| async_tree_io_tg           | 735 ms                                                                 | 679 ms: 1.08x faster                                           |
| async_tree_none            | 279 ms                                                                 | 258 ms: 1.08x faster                                           |
| async_tree_memoization     | 360 ms                                                                 | 334 ms: 1.08x faster                                           |
| async_tree_io              | 767 ms                                                                 | 714 ms: 1.07x faster                                           |
| async_tree_cpu_io_mixed_tg | 574 ms                                                                 | 539 ms: 1.06x faster                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                                 | 530 ms: 1.06x faster                                           |
| Geometric mean             | (ref)                                                                  | 1.08x faster                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231218-darwin-arm64-python-2feec0fc7fd0b9caae7a-3.13.0a2+-2feec0f | bm-20231219-darwin-arm64-brandtbucher-justin-3.13.0a2+-b63610e |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------:|
| float          | 74.2 ms                                                                | 58.3 ms: 1.27x faster                                          |
| nbody          | 92.7 ms                                                                | 79.4 ms: 1.17x faster                                          |
| pidigits       | 294 ms                                                                 | 284 ms: 1.04x faster                                           |
| Geometric mean | (ref)                                                                  | 1.15x faster                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231218-darwin-arm64-python-2feec0fc7fd0b9caae7a-3.13.0a2+-2feec0f | bm-20231219-darwin-arm64-brandtbucher-justin-3.13.0a2+-b63610e |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_compile  | 89.4 ms                                                                | 80.6 ms: 1.11x faster                                          |
| regex_dna      | 161 ms                                                                 | 153 ms: 1.05x faster                                           |
| regex_effbot   | 2.84 ms                                                                | 2.71 ms: 1.05x faster                                          |
| regex_v8       | 18.4 ms                                                                | 17.8 ms: 1.04x faster                                          |
| Geometric mean | (ref)                                                                  | 1.06x faster                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231218-darwin-arm64-python-2feec0fc7fd0b9caae7a-3.13.0a2+-2feec0f | bm-20231219-darwin-arm64-brandtbucher-justin-3.13.0a2+-b63610e |
|----------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------:|
| tomli_loads          | 1.76 sec                                                               | 1.53 sec: 1.15x faster                                         |
| xml_etree_iterparse  | 86.0 ms                                                                | 77.6 ms: 1.11x faster                                          |
| xml_etree_generate   | 64.3 ms                                                                | 58.6 ms: 1.10x faster                                          |
| xml_etree_process    | 44.4 ms                                                                | 41.3 ms: 1.08x faster                                          |
| unpickle_pure_python | 180 us                                                                 | 169 us: 1.07x faster                                           |
| unpickle_list        | 3.27 us                                                                | 3.11 us: 1.05x faster                                          |
| json_dumps           | 6.97 ms                                                                | 6.68 ms: 1.04x faster                                          |
| xml_etree_parse      | 113 ms                                                                 | 109 ms: 1.04x faster                                           |
| pickle_list          | 3.04 us                                                                | 2.93 us: 1.04x faster                                          |
| unpickle             | 9.49 us                                                                | 9.16 us: 1.04x faster                                          |
| json_loads           | 17.9 us                                                                | 17.3 us: 1.03x faster                                          |
| pickle_dict          | 18.6 us                                                                | 17.9 us: 1.03x faster                                          |
| pickle_pure_python   | 212 us                                                                 | 207 us: 1.02x faster                                           |
| pickle               | 7.67 us                                                                | 7.51 us: 1.02x faster                                          |
| Geometric mean       | (ref)                                                                  | 1.06x faster                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231218-darwin-arm64-python-2feec0fc7fd0b9caae7a-3.13.0a2+-2feec0f | bm-20231219-darwin-arm64-brandtbucher-justin-3.13.0a2+-b63610e |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup_no_site | 14.0 ms                                                                | 12.0 ms: 1.17x faster                                          |
| python_startup         | 15.6 ms                                                                | 13.3 ms: 1.17x faster                                          |
| Geometric mean         | (ref)                                                                  | 1.17x faster                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20231218-darwin-arm64-python-2feec0fc7fd0b9caae7a-3.13.0a2+-2feec0f | bm-20231219-darwin-arm64-brandtbucher-justin-3.13.0a2+-b63610e |
|-----------|:----------------------------------------------------------------------:|:--------------------------------------------------------------:|
| mako      | 10.5 ms                                                                | 8.10 ms: 1.29x faster                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231218-darwin-arm64-python-2feec0fc7fd0b9caae7a-3.13.0a2+-2feec0f | bm-20231219-darwin-arm64-brandtbucher-justin-3.13.0a2+-b63610e |
|----------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------:|
| deltablue                  | 3.83 ms                                                                | 2.62 ms: 1.46x faster                                          |
| asyncio_tcp                | 595 ms                                                                 | 430 ms: 1.39x faster                                           |
| scimark_sparse_mat_mult    | 4.38 ms                                                                | 3.31 ms: 1.32x faster                                          |
| mako                       | 10.5 ms                                                                | 8.10 ms: 1.29x faster                                          |
| spectral_norm              | 106 ms                                                                 | 82.8 ms: 1.28x faster                                          |
| float                      | 74.2 ms                                                                | 58.3 ms: 1.27x faster                                          |
| asyncio_tcp_ssl            | 1.62 sec                                                               | 1.31 sec: 1.24x faster                                         |
| comprehensions             | 16.9 us                                                                | 13.7 us: 1.23x faster                                          |
| fannkuch                   | 360 ms                                                                 | 302 ms: 1.19x faster                                           |
| scimark_monte_carlo        | 61.4 ms                                                                | 52.1 ms: 1.18x faster                                          |
| scimark_fft                | 261 ms                                                                 | 222 ms: 1.18x faster                                           |
| pyflate                    | 411 ms                                                                 | 351 ms: 1.17x faster                                           |
| nbody                      | 92.7 ms                                                                | 79.4 ms: 1.17x faster                                          |
| python_startup_no_site     | 14.0 ms                                                                | 12.0 ms: 1.17x faster                                          |
| python_startup             | 15.6 ms                                                                | 13.3 ms: 1.17x faster                                          |
| hexiom                     | 6.31 ms                                                                | 5.43 ms: 1.16x faster                                          |
| chaos                      | 50.1 ms                                                                | 43.6 ms: 1.15x faster                                          |
| tomli_loads                | 1.76 sec                                                               | 1.53 sec: 1.15x faster                                         |
| tornado_http               | 83.4 ms                                                                | 72.8 ms: 1.15x faster                                          |
| pprint_pformat             | 1.26 sec                                                               | 1.11 sec: 1.13x faster                                         |
| pprint_safe_repr           | 615 ms                                                                 | 546 ms: 1.13x faster                                           |
| crypto_pyaes               | 57.3 ms                                                                | 50.9 ms: 1.13x faster                                          |
| regex_compile              | 89.4 ms                                                                | 80.6 ms: 1.11x faster                                          |
| xml_etree_iterparse        | 86.0 ms                                                                | 77.6 ms: 1.11x faster                                          |
| pathlib                    | 27.5 ms                                                                | 24.9 ms: 1.10x faster                                          |
| xml_etree_generate         | 64.3 ms                                                                | 58.6 ms: 1.10x faster                                          |
| bench_thread_pool          | 582 us                                                                 | 531 us: 1.10x faster                                           |
| async_tree_none_tg         | 289 ms                                                                 | 264 ms: 1.09x faster                                           |
| nqueens                    | 72.2 ms                                                                | 66.2 ms: 1.09x faster                                          |
| docutils                   | 1.67 sec                                                               | 1.54 sec: 1.09x faster                                         |
| async_tree_memoization_tg  | 360 ms                                                                 | 331 ms: 1.09x faster                                           |
| mdp                        | 1.85 sec                                                               | 1.70 sec: 1.09x faster                                         |
| sympy_str                  | 167 ms                                                                 | 153 ms: 1.09x faster                                           |
| sqlglot_normalize          | 211 ms                                                                 | 195 ms: 1.09x faster                                           |
| sympy_sum                  | 87.7 ms                                                                | 80.8 ms: 1.09x faster                                          |
| meteor_contest             | 83.9 ms                                                                | 77.4 ms: 1.08x faster                                          |
| async_tree_io_tg           | 735 ms                                                                 | 679 ms: 1.08x faster                                           |
| bench_mp_pool              | 51.6 ms                                                                | 47.8 ms: 1.08x faster                                          |
| async_tree_none            | 279 ms                                                                 | 258 ms: 1.08x faster                                           |
| async_tree_memoization     | 360 ms                                                                 | 334 ms: 1.08x faster                                           |
| dask                       | 252 ms                                                                 | 234 ms: 1.08x faster                                           |
| xml_etree_process          | 44.4 ms                                                                | 41.3 ms: 1.08x faster                                          |
| chameleon                  | 5.51 ms                                                                | 5.12 ms: 1.08x faster                                          |
| raytrace                   | 203 ms                                                                 | 188 ms: 1.08x faster                                           |
| async_tree_io              | 767 ms                                                                 | 714 ms: 1.07x faster                                           |
| 2to3                       | 196 ms                                                                 | 182 ms: 1.07x faster                                           |
| sqlglot_optimize           | 39.5 ms                                                                | 36.9 ms: 1.07x faster                                          |
| deepcopy_memo              | 28.4 us                                                                | 26.5 us: 1.07x faster                                          |
| asyncio_websockets         | 437 ms                                                                 | 409 ms: 1.07x faster                                           |
| sqlite_synth               | 1.78 us                                                                | 1.67 us: 1.07x faster                                          |
| unpickle_pure_python       | 180 us                                                                 | 169 us: 1.07x faster                                           |
| sympy_integrate            | 12.8 ms                                                                | 12.0 ms: 1.07x faster                                          |
| gc_traversal               | 2.56 ms                                                                | 2.40 ms: 1.07x faster                                          |
| async_tree_cpu_io_mixed_tg | 574 ms                                                                 | 539 ms: 1.06x faster                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                                 | 530 ms: 1.06x faster                                           |
| typing_runtime_protocols   | 80.6 us                                                                | 75.8 us: 1.06x faster                                          |
| pycparser                  | 769 ms                                                                 | 725 ms: 1.06x faster                                           |
| sqlglot_transpile          | 1.13 ms                                                                | 1.07 ms: 1.06x faster                                          |
| telco                      | 4.95 ms                                                                | 4.69 ms: 1.06x faster                                          |
| logging_simple             | 3.89 us                                                                | 3.69 us: 1.05x faster                                          |
| regex_dna                  | 161 ms                                                                 | 153 ms: 1.05x faster                                           |
| logging_format             | 4.22 us                                                                | 4.00 us: 1.05x faster                                          |
| sympy_expand               | 274 ms                                                                 | 260 ms: 1.05x faster                                           |
| logging_silent             | 77.5 ns                                                                | 73.6 ns: 1.05x faster                                          |
| sqlglot_parse              | 924 us                                                                 | 878 us: 1.05x faster                                           |
| richards                   | 35.9 ms                                                                | 34.1 ms: 1.05x faster                                          |
| create_gc_cycles           | 740 us                                                                 | 704 us: 1.05x faster                                           |
| unpickle_list              | 3.27 us                                                                | 3.11 us: 1.05x faster                                          |
| dulwich_log                | 32.0 ms                                                                | 30.5 ms: 1.05x faster                                          |
| json                       | 3.16 ms                                                                | 3.02 ms: 1.05x faster                                          |
| regex_effbot               | 2.84 ms                                                                | 2.71 ms: 1.05x faster                                          |
| richards_super             | 39.9 ms                                                                | 38.0 ms: 1.05x faster                                          |
| json_dumps                 | 6.97 ms                                                                | 6.68 ms: 1.04x faster                                          |
| scimark_sor                | 114 ms                                                                 | 109 ms: 1.04x faster                                           |
| coverage                   | 49.9 ms                                                                | 47.8 ms: 1.04x faster                                          |
| xml_etree_parse            | 113 ms                                                                 | 109 ms: 1.04x faster                                           |
| pickle_list                | 3.04 us                                                                | 2.93 us: 1.04x faster                                          |
| regex_v8                   | 18.4 ms                                                                | 17.8 ms: 1.04x faster                                          |
| generators                 | 26.6 ms                                                                | 25.7 ms: 1.04x faster                                          |
| deepcopy                   | 247 us                                                                 | 238 us: 1.04x faster                                           |
| unpickle                   | 9.49 us                                                                | 9.16 us: 1.04x faster                                          |
| pidigits                   | 294 ms                                                                 | 284 ms: 1.04x faster                                           |
| json_loads                 | 17.9 us                                                                | 17.3 us: 1.03x faster                                          |
| pickle_dict                | 18.6 us                                                                | 17.9 us: 1.03x faster                                          |
| go                         | 119 ms                                                                 | 115 ms: 1.03x faster                                           |
| deepcopy_reduce            | 2.19 us                                                                | 2.13 us: 1.03x faster                                          |
| unpack_sequence            | 29.8 ns                                                                | 29.0 ns: 1.03x faster                                          |
| async_generators           | 322 ms                                                                 | 315 ms: 1.02x faster                                           |
| pickle_pure_python         | 212 us                                                                 | 207 us: 1.02x faster                                           |
| coroutines                 | 19.4 ms                                                                | 19.0 ms: 1.02x faster                                          |
| pickle                     | 7.67 us                                                                | 7.51 us: 1.02x faster                                          |
| scimark_lu                 | 81.4 ms                                                                | 80.4 ms: 1.01x faster                                          |
| Geometric mean             | (ref)                                                                  | 1.09x faster                                                   |

Benchmark hidden because not significant (1): mypy2


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.07x
