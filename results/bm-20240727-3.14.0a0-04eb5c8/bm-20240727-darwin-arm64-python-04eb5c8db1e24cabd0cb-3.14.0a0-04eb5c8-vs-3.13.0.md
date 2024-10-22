# Results vs. 3.13.0

- fork: python
- ref: 04eb5c8db1e24cabd0cb
- machine: darwin-arm64
- commit hash: 04eb5c8
- commit date: 2024-07-27
- overall geometric mean: 1.09x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 178 ms                                                 | 163 ms: 1.09x faster                                                  |
| docutils       | 1.44 sec                                               | 1.49 sec: 1.03x slower                                                |
| html5lib       | 36.6 ms                                                | 31.5 ms: 1.16x faster                                                 |
| Geometric mean | (ref)                                                  | 1.09x faster                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg        | 291 ms                                                 | 226 ms: 1.28x faster                                                  |
| coroutines                       | 19.8 ms                                                | 16.1 ms: 1.23x faster                                                 |
| async_tree_eager_tg              | 48.4 ms                                                | 41.5 ms: 1.17x faster                                                 |
| async_tree_eager                 | 70.5 ms                                                | 61.5 ms: 1.15x faster                                                 |
| async_tree_eager_memoization     | 169 ms                                                 | 150 ms: 1.13x faster                                                  |
| async_tree_memoization           | 270 ms                                                 | 241 ms: 1.12x faster                                                  |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 124 ms: 1.12x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 195 ms: 1.09x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 183 ms: 1.08x faster                                                  |
| asyncio_tcp                      | 457 ms                                                 | 431 ms: 1.06x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 356 ms: 1.05x faster                                                  |
| async_generators                 | 294 ms                                                 | 281 ms: 1.05x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 333 ms: 1.05x faster                                                  |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 451 ms: 1.02x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 447 ms                                                 | 441 ms: 1.01x faster                                                  |
| async_tree_io                    | 507 ms                                                 | 545 ms: 1.08x slower                                                  |
| async_tree_eager_io              | 513 ms                                                 | 641 ms: 1.25x slower                                                  |
| async_tree_eager_io_tg           | 477 ms                                                 | 678 ms: 1.42x slower                                                  |
| asyncio_websockets               | 241 ms                                                 | 408 ms: 1.69x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (2): asyncio_tcp_ssl, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 73.9 ms                                                | 61.7 ms: 1.20x faster                                                 |
| float          | 56.2 ms                                                | 48.1 ms: 1.17x faster                                                 |
| pidigits       | 284 ms                                                 | 281 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.12x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 78.5 ms                                                | 68.4 ms: 1.15x faster                                                 |
| regex_effbot   | 2.63 ms                                                | 2.54 ms: 1.03x faster                                                 |
| regex_dna      | 148 ms                                                 | 149 ms: 1.01x slower                                                  |
| regex_v8       | 16.9 ms                                                | 17.4 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                  | 1.03x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 213 us                                                 | 182 us: 1.17x faster                                                  |
| unpickle_pure_python | 163 us                                                 | 144 us: 1.14x faster                                                  |
| xml_etree_process    | 40.9 ms                                                | 37.4 ms: 1.09x faster                                                 |
| xml_etree_generate   | 56.6 ms                                                | 53.0 ms: 1.07x faster                                                 |
| tomli_loads          | 1.56 sec                                               | 1.48 sec: 1.06x faster                                                |
| json_dumps           | 6.56 ms                                                | 6.37 ms: 1.03x faster                                                 |
| xml_etree_parse      | 109 ms                                                 | 106 ms: 1.03x faster                                                  |
| xml_etree_iterparse  | 74.2 ms                                                | 72.6 ms: 1.02x faster                                                 |
| json_loads           | 16.9 us                                                | 17.0 us: 1.01x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 17.0 ms                                                | 15.2 ms: 1.12x faster                                                 |
| python_startup_no_site | 13.7 ms                                                | 12.5 ms: 1.09x faster                                                 |
| Geometric mean         | (ref)                                                  | 1.11x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 14.2 ms: 1.19x faster                                                 |
| genshi_xml      | 34.4 ms                                                | 30.3 ms: 1.13x faster                                                 |
| django_template | 22.2 ms                                                | 19.7 ms: 1.13x faster                                                 |
| mako            | 7.68 ms                                                | 7.04 ms: 1.09x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.13x faster                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy                         | 232 us                                                 | 145 us: 1.61x faster                                                  |
| deepcopy_memo                    | 27.2 us                                                | 17.0 us: 1.61x faster                                                 |
| generators                       | 31.5 ms                                                | 20.6 ms: 1.53x faster                                                 |
| deepcopy_reduce                  | 2.06 us                                                | 1.49 us: 1.38x faster                                                 |
| async_tree_memoization_tg        | 291 ms                                                 | 226 ms: 1.28x faster                                                  |
| deltablue                        | 2.68 ms                                                | 2.11 ms: 1.27x faster                                                 |
| raytrace                         | 182 ms                                                 | 147 ms: 1.24x faster                                                  |
| coroutines                       | 19.8 ms                                                | 16.1 ms: 1.23x faster                                                 |
| nbody                            | 73.9 ms                                                | 61.7 ms: 1.20x faster                                                 |
| genshi_text                      | 16.9 ms                                                | 14.2 ms: 1.19x faster                                                 |
| scimark_monte_carlo              | 50.4 ms                                                | 42.5 ms: 1.19x faster                                                 |
| chaos                            | 41.3 ms                                                | 34.9 ms: 1.18x faster                                                 |
| hexiom                           | 4.85 ms                                                | 4.12 ms: 1.18x faster                                                 |
| spectral_norm                    | 77.3 ms                                                | 65.9 ms: 1.17x faster                                                 |
| nqueens                          | 62.9 ms                                                | 53.6 ms: 1.17x faster                                                 |
| go                               | 115 ms                                                 | 98.1 ms: 1.17x faster                                                 |
| logging_silent                   | 69.9 ns                                                | 59.7 ns: 1.17x faster                                                 |
| float                            | 56.2 ms                                                | 48.1 ms: 1.17x faster                                                 |
| pickle_pure_python               | 213 us                                                 | 182 us: 1.17x faster                                                  |
| async_tree_eager_tg              | 48.4 ms                                                | 41.5 ms: 1.17x faster                                                 |
| html5lib                         | 36.6 ms                                                | 31.5 ms: 1.16x faster                                                 |
| logging_simple                   | 3.57 us                                                | 3.08 us: 1.16x faster                                                 |
| sqlglot_parse                    | 856 us                                                 | 742 us: 1.15x faster                                                  |
| dask                             | 255 ms                                                 | 222 ms: 1.15x faster                                                  |
| regex_compile                    | 78.5 ms                                                | 68.4 ms: 1.15x faster                                                 |
| async_tree_eager                 | 70.5 ms                                                | 61.5 ms: 1.15x faster                                                 |
| unpickle_pure_python             | 163 us                                                 | 144 us: 1.14x faster                                                  |
| logging_format                   | 3.85 us                                                | 3.39 us: 1.14x faster                                                 |
| genshi_xml                       | 34.4 ms                                                | 30.3 ms: 1.13x faster                                                 |
| sqlglot_transpile                | 1.02 ms                                                | 905 us: 1.13x faster                                                  |
| richards_super                   | 39.1 ms                                                | 34.6 ms: 1.13x faster                                                 |
| pprint_safe_repr                 | 531 ms                                                 | 470 ms: 1.13x faster                                                  |
| pprint_pformat                   | 1.08 sec                                               | 955 ms: 1.13x faster                                                  |
| bench_thread_pool                | 506 us                                                 | 449 us: 1.13x faster                                                  |
| async_tree_eager_memoization     | 169 ms                                                 | 150 ms: 1.13x faster                                                  |
| django_template                  | 22.2 ms                                                | 19.7 ms: 1.13x faster                                                 |
| sqlglot_normalize                | 189 ms                                                 | 168 ms: 1.12x faster                                                  |
| richards                         | 35.4 ms                                                | 31.6 ms: 1.12x faster                                                 |
| async_tree_memoization           | 270 ms                                                 | 241 ms: 1.12x faster                                                  |
| python_startup                   | 17.0 ms                                                | 15.2 ms: 1.12x faster                                                 |
| sqlglot_optimize                 | 34.9 ms                                                | 31.2 ms: 1.12x faster                                                 |
| comprehensions                   | 12.2 us                                                | 10.9 us: 1.12x faster                                                 |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 124 ms: 1.12x faster                                                  |
| scimark_sor                      | 106 ms                                                 | 95.1 ms: 1.11x faster                                                 |
| scimark_fft                      | 201 ms                                                 | 182 ms: 1.10x faster                                                  |
| scimark_lu                       | 76.5 ms                                                | 69.5 ms: 1.10x faster                                                 |
| pycparser                        | 706 ms                                                 | 643 ms: 1.10x faster                                                  |
| xml_etree_process                | 40.9 ms                                                | 37.4 ms: 1.09x faster                                                 |
| python_startup_no_site           | 13.7 ms                                                | 12.5 ms: 1.09x faster                                                 |
| pyflate                          | 351 ms                                                 | 322 ms: 1.09x faster                                                  |
| sympy_str                        | 145 ms                                                 | 133 ms: 1.09x faster                                                  |
| sympy_integrate                  | 11.3 ms                                                | 10.4 ms: 1.09x faster                                                 |
| 2to3                             | 178 ms                                                 | 163 ms: 1.09x faster                                                  |
| mako                             | 7.68 ms                                                | 7.04 ms: 1.09x faster                                                 |
| async_tree_none                  | 212 ms                                                 | 195 ms: 1.09x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 183 ms: 1.08x faster                                                  |
| sympy_sum                        | 75.6 ms                                                | 70.0 ms: 1.08x faster                                                 |
| thrift                           | 466 us                                                 | 432 us: 1.08x faster                                                  |
| typing_runtime_protocols         | 101 us                                                 | 93.7 us: 1.08x faster                                                 |
| sympy_expand                     | 246 ms                                                 | 229 ms: 1.07x faster                                                  |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 2.79 ms: 1.07x faster                                                 |
| crypto_pyaes                     | 54.0 ms                                                | 50.6 ms: 1.07x faster                                                 |
| xml_etree_generate               | 56.6 ms                                                | 53.0 ms: 1.07x faster                                                 |
| asyncio_tcp                      | 457 ms                                                 | 431 ms: 1.06x faster                                                  |
| bench_mp_pool                    | 50.9 ms                                                | 48.1 ms: 1.06x faster                                                 |
| mdp                              | 1.50 sec                                               | 1.42 sec: 1.06x faster                                                |
| dulwich_log                      | 28.7 ms                                                | 27.2 ms: 1.06x faster                                                 |
| fannkuch                         | 282 ms                                                 | 266 ms: 1.06x faster                                                  |
| tomli_loads                      | 1.56 sec                                               | 1.48 sec: 1.06x faster                                                |
| telco                            | 4.80 ms                                                | 4.55 ms: 1.06x faster                                                 |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 356 ms: 1.05x faster                                                  |
| bpe_tokeniser                    | 3.24 sec                                               | 3.10 sec: 1.05x faster                                                |
| async_generators                 | 294 ms                                                 | 281 ms: 1.05x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 333 ms: 1.05x faster                                                  |
| coverage                         | 46.1 ms                                                | 44.2 ms: 1.04x faster                                                 |
| regex_effbot                     | 2.63 ms                                                | 2.54 ms: 1.03x faster                                                 |
| json_dumps                       | 6.56 ms                                                | 6.37 ms: 1.03x faster                                                 |
| meteor_contest                   | 73.8 ms                                                | 71.9 ms: 1.03x faster                                                 |
| xml_etree_parse                  | 109 ms                                                 | 106 ms: 1.03x faster                                                  |
| xml_etree_iterparse              | 74.2 ms                                                | 72.6 ms: 1.02x faster                                                 |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 451 ms: 1.02x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 447 ms                                                 | 441 ms: 1.01x faster                                                  |
| gc_traversal                     | 2.48 ms                                                | 2.46 ms: 1.01x faster                                                 |
| pidigits                         | 284 ms                                                 | 281 ms: 1.01x faster                                                  |
| json_loads                       | 16.9 us                                                | 17.0 us: 1.01x slower                                                 |
| regex_dna                        | 148 ms                                                 | 149 ms: 1.01x slower                                                  |
| regex_v8                         | 16.9 ms                                                | 17.4 ms: 1.02x slower                                                 |
| pathlib                          | 22.8 ms                                                | 23.4 ms: 1.03x slower                                                 |
| docutils                         | 1.44 sec                                               | 1.49 sec: 1.03x slower                                                |
| async_tree_io                    | 507 ms                                                 | 545 ms: 1.08x slower                                                  |
| create_gc_cycles                 | 803 us                                                 | 903 us: 1.12x slower                                                  |
| async_tree_eager_io              | 513 ms                                                 | 641 ms: 1.25x slower                                                  |
| async_tree_eager_io_tg           | 477 ms                                                 | 678 ms: 1.42x slower                                                  |
| asyncio_websockets               | 241 ms                                                 | 408 ms: 1.69x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.09x faster                                                          |

Benchmark hidden because not significant (5): tornado_http, pylint, json, asyncio_tcp_ssl, async_tree_io_tg
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 0.98x