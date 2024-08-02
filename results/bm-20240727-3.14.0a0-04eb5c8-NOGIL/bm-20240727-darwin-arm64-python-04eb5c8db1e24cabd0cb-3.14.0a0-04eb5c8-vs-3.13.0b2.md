# Results vs. 3.13.0b2

- fork: python
- ref: 04eb5c8db1e24cabd0cb
- machine: darwin-arm64
- commit hash: 04eb5c8
- commit date: 2024-07-27
- overall geometric mean: 1.40x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x slower
- Memory change: 0.48x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 161 ms                                                     | 248 ms: 1.54x slower                                                  |
| docutils       | 1.44 sec                                                   | 1.79 sec: 1.25x slower                                                |
| html5lib       | 31.2 ms                                                    | 51.2 ms: 1.64x slower                                                 |
| tornado_http   | 66.7 ms                                                    | 94.5 ms: 1.42x slower                                                 |
| Geometric mean | (ref)                                                      | 1.45x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager_io_tg           | 768 ms                                                     | 462 ms: 1.66x faster                                                  |
| async_tree_eager_io              | 766 ms                                                     | 484 ms: 1.58x faster                                                  |
| async_tree_io_tg                 | 565 ms                                                     | 495 ms: 1.14x faster                                                  |
| async_tree_io                    | 563 ms                                                     | 522 ms: 1.08x faster                                                  |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 483 ms: 1.03x slower                                                  |
| async_tree_memoization_tg        | 240 ms                                                     | 256 ms: 1.07x slower                                                  |
| async_tree_none                  | 209 ms                                                     | 229 ms: 1.09x slower                                                  |
| async_tree_memoization           | 260 ms                                                     | 284 ms: 1.09x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 364 ms: 1.10x slower                                                  |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 396 ms: 1.11x slower                                                  |
| async_tree_eager_memoization     | 152 ms                                                     | 185 ms: 1.21x slower                                                  |
| async_tree_eager_memoization_tg  | 126 ms                                                     | 157 ms: 1.25x slower                                                  |
| async_tree_eager                 | 60.3 ms                                                    | 105 ms: 1.74x slower                                                  |
| async_tree_eager_tg              | 41.4 ms                                                    | 73.3 ms: 1.77x slower                                                 |
| Geometric mean                   | (ref)                                                      | 1.06x slower                                                          |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed_tg, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 282 ms                                                     | 281 ms: 1.00x faster                                                  |
| float          | 48.6 ms                                                    | 93.2 ms: 1.92x slower                                                 |
| nbody          | 59.6 ms                                                    | 154 ms: 2.58x slower                                                  |
| Geometric mean | (ref)                                                      | 1.70x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_dna      | 149 ms                                                     | 138 ms: 1.08x faster                                                  |
| regex_v8       | 17.3 ms                                                    | 17.5 ms: 1.01x slower                                                 |
| regex_compile  | 68.5 ms                                                    | 122 ms: 1.78x slower                                                  |
| Geometric mean | (ref)                                                      | 1.14x slower                                                          |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_parse      | 106 ms                                                     | 97.3 ms: 1.09x faster                                                 |
| xml_etree_iterparse  | 71.5 ms                                                    | 75.8 ms: 1.06x slower                                                 |
| json_loads           | 16.8 us                                                    | 19.1 us: 1.13x slower                                                 |
| json_dumps           | 6.23 ms                                                    | 7.90 ms: 1.27x slower                                                 |
| xml_etree_generate   | 52.7 ms                                                    | 69.1 ms: 1.31x slower                                                 |
| tomli_loads          | 1.47 sec                                                   | 2.03 sec: 1.39x slower                                                |
| xml_etree_process    | 37.1 ms                                                    | 59.5 ms: 1.61x slower                                                 |
| unpickle_pure_python | 141 us                                                     | 268 us: 1.90x slower                                                  |
| pickle_pure_python   | 179 us                                                     | 342 us: 1.91x slower                                                  |
| Geometric mean       | (ref)                                                      | 1.35x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 12.3 ms                                                    | 13.8 ms: 1.12x slower                                                 |
| python_startup         | 15.2 ms                                                    | 17.0 ms: 1.12x slower                                                 |
| Geometric mean         | (ref)                                                      | 1.12x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|-----------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_xml      | 29.9 ms                                                    | 50.6 ms: 1.69x slower                                                 |
| genshi_text     | 13.9 ms                                                    | 25.4 ms: 1.83x slower                                                 |
| django_template | 19.4 ms                                                    | 35.9 ms: 1.85x slower                                                 |
| mako            | 6.99 ms                                                    | 13.6 ms: 1.95x slower                                                 |
| Geometric mean  | (ref)                                                      | 1.83x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------------------|:----------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager_io_tg           | 768 ms                                                     | 462 ms: 1.66x faster                                                  |
| async_tree_eager_io              | 766 ms                                                     | 484 ms: 1.58x faster                                                  |
| sqlglot_normalize                | 166 ms                                                     | 106 ms: 1.56x faster                                                  |
| create_gc_cycles                 | 897 us                                                     | 656 us: 1.37x faster                                                  |
| gc_traversal                     | 2.45 ms                                                    | 2.03 ms: 1.21x faster                                                 |
| asyncio_tcp                      | 402 ms                                                     | 350 ms: 1.15x faster                                                  |
| async_tree_io_tg                 | 565 ms                                                     | 495 ms: 1.14x faster                                                  |
| xml_etree_parse                  | 106 ms                                                     | 97.3 ms: 1.09x faster                                                 |
| async_tree_io                    | 563 ms                                                     | 522 ms: 1.08x faster                                                  |
| regex_dna                        | 149 ms                                                     | 138 ms: 1.08x faster                                                  |
| asyncio_tcp_ssl                  | 1.29 sec                                                   | 1.23 sec: 1.05x faster                                                |
| asyncio_websockets               | 409 ms                                                     | 403 ms: 1.01x faster                                                  |
| pidigits                         | 282 ms                                                     | 281 ms: 1.00x faster                                                  |
| regex_v8                         | 17.3 ms                                                    | 17.5 ms: 1.01x slower                                                 |
| async_tree_cpu_io_mixed          | 467 ms                                                     | 483 ms: 1.03x slower                                                  |
| xml_etree_iterparse              | 71.5 ms                                                    | 75.8 ms: 1.06x slower                                                 |
| async_tree_memoization_tg        | 240 ms                                                     | 256 ms: 1.07x slower                                                  |
| async_tree_none                  | 209 ms                                                     | 229 ms: 1.09x slower                                                  |
| async_tree_memoization           | 260 ms                                                     | 284 ms: 1.09x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 331 ms                                                     | 364 ms: 1.10x slower                                                  |
| async_tree_eager_cpu_io_mixed    | 358 ms                                                     | 396 ms: 1.11x slower                                                  |
| pathlib                          | 23.3 ms                                                    | 25.9 ms: 1.11x slower                                                 |
| python_startup_no_site           | 12.3 ms                                                    | 13.8 ms: 1.12x slower                                                 |
| python_startup                   | 15.2 ms                                                    | 17.0 ms: 1.12x slower                                                 |
| json_loads                       | 16.8 us                                                    | 19.1 us: 1.13x slower                                                 |
| json                             | 2.93 ms                                                    | 3.37 ms: 1.15x slower                                                 |
| bench_mp_pool                    | 47.2 ms                                                    | 55.4 ms: 1.17x slower                                                 |
| async_generators                 | 281 ms                                                     | 336 ms: 1.20x slower                                                  |
| coverage                         | 45.0 ms                                                    | 54.1 ms: 1.20x slower                                                 |
| mdp                              | 1.53 sec                                                   | 1.85 sec: 1.21x slower                                                |
| async_tree_eager_memoization     | 152 ms                                                     | 185 ms: 1.21x slower                                                  |
| deepcopy                         | 204 us                                                     | 249 us: 1.22x slower                                                  |
| telco                            | 4.60 ms                                                    | 5.65 ms: 1.23x slower                                                 |
| docutils                         | 1.44 sec                                                   | 1.79 sec: 1.25x slower                                                |
| async_tree_eager_memoization_tg  | 126 ms                                                     | 157 ms: 1.25x slower                                                  |
| meteor_contest                   | 70.3 ms                                                    | 88.8 ms: 1.26x slower                                                 |
| json_dumps                       | 6.23 ms                                                    | 7.90 ms: 1.27x slower                                                 |
| pylint                           | 170 ms                                                     | 218 ms: 1.28x slower                                                  |
| xml_etree_generate               | 52.7 ms                                                    | 69.1 ms: 1.31x slower                                                 |
| bpe_tokeniser                    | 3.05 sec                                                   | 4.03 sec: 1.32x slower                                                |
| tomli_loads                      | 1.47 sec                                                   | 2.03 sec: 1.39x slower                                                |
| deepcopy_memo                    | 22.6 us                                                    | 31.3 us: 1.39x slower                                                 |
| deepcopy_reduce                  | 1.82 us                                                    | 2.53 us: 1.39x slower                                                 |
| tornado_http                     | 66.7 ms                                                    | 94.5 ms: 1.42x slower                                                 |
| coroutines                       | 15.8 ms                                                    | 23.1 ms: 1.46x slower                                                 |
| fannkuch                         | 248 ms                                                     | 362 ms: 1.46x slower                                                  |
| scimark_fft                      | 181 ms                                                     | 266 ms: 1.47x slower                                                  |
| pycparser                        | 632 ms                                                     | 933 ms: 1.47x slower                                                  |
| nqueens                          | 52.2 ms                                                    | 77.5 ms: 1.48x slower                                                 |
| dulwich_log                      | 27.6 ms                                                    | 41.0 ms: 1.49x slower                                                 |
| scimark_sparse_mat_mult          | 2.77 ms                                                    | 4.13 ms: 1.49x slower                                                 |
| sympy_integrate                  | 10.3 ms                                                    | 15.5 ms: 1.50x slower                                                 |
| pyflate                          | 321 ms                                                     | 482 ms: 1.50x slower                                                  |
| 2to3                             | 161 ms                                                     | 248 ms: 1.54x slower                                                  |
| thrift                           | 435 us                                                     | 687 us: 1.58x slower                                                  |
| generators                       | 22.9 ms                                                    | 36.2 ms: 1.58x slower                                                 |
| crypto_pyaes                     | 49.5 ms                                                    | 78.3 ms: 1.58x slower                                                 |
| xml_etree_process                | 37.1 ms                                                    | 59.5 ms: 1.61x slower                                                 |
| html5lib                         | 31.2 ms                                                    | 51.2 ms: 1.64x slower                                                 |
| scimark_sor                      | 94.9 ms                                                    | 157 ms: 1.65x slower                                                  |
| typing_runtime_protocols         | 87.6 us                                                    | 145 us: 1.66x slower                                                  |
| genshi_xml                       | 29.9 ms                                                    | 50.6 ms: 1.69x slower                                                 |
| richards                         | 31.8 ms                                                    | 54.2 ms: 1.70x slower                                                 |
| sqlglot_optimize                 | 30.9 ms                                                    | 53.2 ms: 1.72x slower                                                 |
| async_tree_eager                 | 60.3 ms                                                    | 105 ms: 1.74x slower                                                  |
| bench_thread_pool                | 447 us                                                     | 791 us: 1.77x slower                                                  |
| async_tree_eager_tg              | 41.4 ms                                                    | 73.3 ms: 1.77x slower                                                 |
| sympy_str                        | 131 ms                                                     | 234 ms: 1.78x slower                                                  |
| regex_compile                    | 68.5 ms                                                    | 122 ms: 1.78x slower                                                  |
| pprint_pformat                   | 947 ms                                                     | 1.70 sec: 1.80x slower                                                |
| pprint_safe_repr                 | 465 ms                                                     | 836 ms: 1.80x slower                                                  |
| richards_super                   | 35.2 ms                                                    | 63.6 ms: 1.81x slower                                                 |
| scimark_monte_carlo              | 42.5 ms                                                    | 77.4 ms: 1.82x slower                                                 |
| genshi_text                      | 13.9 ms                                                    | 25.4 ms: 1.83x slower                                                 |
| django_template                  | 19.4 ms                                                    | 35.9 ms: 1.85x slower                                                 |
| comprehensions                   | 10.2 us                                                    | 18.9 us: 1.86x slower                                                 |
| unpickle_pure_python             | 141 us                                                     | 268 us: 1.90x slower                                                  |
| go                               | 101 ms                                                     | 192 ms: 1.91x slower                                                  |
| pickle_pure_python               | 179 us                                                     | 342 us: 1.91x slower                                                  |
| float                            | 48.6 ms                                                    | 93.2 ms: 1.92x slower                                                 |
| spectral_norm                    | 66.4 ms                                                    | 128 ms: 1.92x slower                                                  |
| sympy_expand                     | 226 ms                                                     | 438 ms: 1.94x slower                                                  |
| hexiom                           | 4.06 ms                                                    | 7.89 ms: 1.94x slower                                                 |
| mako                             | 6.99 ms                                                    | 13.6 ms: 1.95x slower                                                 |
| logging_format                   | 3.31 us                                                    | 6.58 us: 1.99x slower                                                 |
| logging_simple                   | 3.04 us                                                    | 6.07 us: 2.00x slower                                                 |
| sympy_sum                        | 69.2 ms                                                    | 139 ms: 2.01x slower                                                  |
| sqlglot_transpile                | 891 us                                                     | 1.89 ms: 2.13x slower                                                 |
| logging_silent                   | 60.1 ns                                                    | 130 ns: 2.16x slower                                                  |
| chaos                            | 34.0 ms                                                    | 75.5 ms: 2.22x slower                                                 |
| sqlglot_parse                    | 732 us                                                     | 1.66 ms: 2.26x slower                                                 |
| scimark_lu                       | 66.9 ms                                                    | 155 ms: 2.32x slower                                                  |
| raytrace                         | 147 ms                                                     | 368 ms: 2.50x slower                                                  |
| nbody                            | 59.6 ms                                                    | 154 ms: 2.58x slower                                                  |
| deltablue                        | 2.14 ms                                                    | 5.55 ms: 2.59x slower                                                 |
| Geometric mean                   | (ref)                                                      | 1.40x slower                                                          |

Benchmark hidden because not significant (3): regex_effbot, async_tree_cpu_io_mixed_tg, async_tree_none_tg
Ignored benchmarks (12) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.25x
- 95% likely to have a slowdown of 1.24x
- 99% likely to have a slowdown of 1.20x

# Memory
- memory change: 0.48x