# Results vs. 3.13.0

- fork: faster-cpython
- ref: bound_method_instrum
- machine: darwin-arm64
- commit hash: 5787d3e
- commit date: 2024-07-23
- overall geometric mean: 1.10x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240723-darwin-arm64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 178 ms                                                 | 162 ms: 1.10x faster                                                            |
| docutils       | 1.44 sec                                               | 1.48 sec: 1.03x slower                                                          |
| html5lib       | 36.6 ms                                                | 31.5 ms: 1.16x faster                                                           |
| Geometric mean | (ref)                                                  | 1.10x faster                                                                    |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240723-darwin-arm64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| coroutines                       | 19.8 ms                                                | 16.1 ms: 1.23x faster                                                           |
| async_tree_memoization_tg        | 291 ms                                                 | 239 ms: 1.21x faster                                                            |
| async_tree_eager_tg              | 48.4 ms                                                | 40.6 ms: 1.19x faster                                                           |
| async_tree_eager                 | 70.5 ms                                                | 60.6 ms: 1.16x faster                                                           |
| async_tree_eager_memoization     | 169 ms                                                 | 146 ms: 1.16x faster                                                            |
| async_tree_memoization           | 270 ms                                                 | 235 ms: 1.15x faster                                                            |
| async_tree_none_tg               | 198 ms                                                 | 173 ms: 1.15x faster                                                            |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 122 ms: 1.14x faster                                                            |
| asyncio_tcp                      | 457 ms                                                 | 421 ms: 1.09x faster                                                            |
| async_tree_none                  | 212 ms                                                 | 197 ms: 1.07x faster                                                            |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 355 ms: 1.06x faster                                                            |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 330 ms: 1.05x faster                                                            |
| async_generators                 | 294 ms                                                 | 280 ms: 1.05x faster                                                            |
| async_tree_cpu_io_mixed_tg       | 447 ms                                                 | 444 ms: 1.01x faster                                                            |
| async_tree_io                    | 507 ms                                                 | 530 ms: 1.05x slower                                                            |
| async_tree_eager_io              | 513 ms                                                 | 645 ms: 1.26x slower                                                            |
| async_tree_eager_io_tg           | 477 ms                                                 | 668 ms: 1.40x slower                                                            |
| asyncio_websockets               | 241 ms                                                 | 408 ms: 1.69x slower                                                            |
| Geometric mean                   | (ref)                                                  | 1.02x faster                                                                    |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed, async_tree_io_tg, asyncio_tcp_ssl

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240723-darwin-arm64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 73.9 ms                                                | 62.2 ms: 1.19x faster                                                           |
| float          | 56.2 ms                                                | 48.3 ms: 1.16x faster                                                           |
| pidigits       | 284 ms                                                 | 281 ms: 1.01x faster                                                            |
| Geometric mean | (ref)                                                  | 1.12x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240723-darwin-arm64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 78.5 ms                                                | 68.0 ms: 1.15x faster                                                           |
| regex_effbot   | 2.63 ms                                                | 2.54 ms: 1.03x faster                                                           |
| regex_dna      | 148 ms                                                 | 149 ms: 1.01x slower                                                            |
| regex_v8       | 16.9 ms                                                | 17.7 ms: 1.04x slower                                                           |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240723-darwin-arm64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pickle_pure_python   | 213 us                                                 | 182 us: 1.17x faster                                                            |
| unpickle_pure_python | 163 us                                                 | 143 us: 1.14x faster                                                            |
| xml_etree_process    | 40.9 ms                                                | 37.2 ms: 1.10x faster                                                           |
| xml_etree_generate   | 56.6 ms                                                | 52.3 ms: 1.08x faster                                                           |
| tomli_loads          | 1.56 sec                                               | 1.48 sec: 1.05x faster                                                          |
| json_dumps           | 6.56 ms                                                | 6.41 ms: 1.02x faster                                                           |
| xml_etree_parse      | 109 ms                                                 | 107 ms: 1.02x faster                                                            |
| xml_etree_iterparse  | 74.2 ms                                                | 72.8 ms: 1.02x faster                                                           |
| json_loads           | 16.9 us                                                | 17.0 us: 1.01x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240723-darwin-arm64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 17.0 ms                                                | 14.9 ms: 1.14x faster                                                           |
| python_startup_no_site | 13.7 ms                                                | 12.3 ms: 1.11x faster                                                           |
| Geometric mean         | (ref)                                                  | 1.13x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240723-darwin-arm64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 14.0 ms: 1.21x faster                                                           |
| django_template | 22.2 ms                                                | 19.7 ms: 1.12x faster                                                           |
| genshi_xml      | 34.4 ms                                                | 30.8 ms: 1.12x faster                                                           |
| mako            | 7.68 ms                                                | 6.93 ms: 1.11x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.14x faster                                                                    |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240723-darwin-arm64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy_memo                    | 27.2 us                                                | 16.7 us: 1.63x faster                                                           |
| deepcopy                         | 232 us                                                 | 146 us: 1.59x faster                                                            |
| generators                       | 31.5 ms                                                | 20.7 ms: 1.53x faster                                                           |
| deepcopy_reduce                  | 2.06 us                                                | 1.49 us: 1.38x faster                                                           |
| deltablue                        | 2.68 ms                                                | 2.09 ms: 1.28x faster                                                           |
| raytrace                         | 182 ms                                                 | 146 ms: 1.24x faster                                                            |
| coroutines                       | 19.8 ms                                                | 16.1 ms: 1.23x faster                                                           |
| async_tree_memoization_tg        | 291 ms                                                 | 239 ms: 1.21x faster                                                            |
| genshi_text                      | 16.9 ms                                                | 14.0 ms: 1.21x faster                                                           |
| async_tree_eager_tg              | 48.4 ms                                                | 40.6 ms: 1.19x faster                                                           |
| nbody                            | 73.9 ms                                                | 62.2 ms: 1.19x faster                                                           |
| chaos                            | 41.3 ms                                                | 34.8 ms: 1.18x faster                                                           |
| scimark_monte_carlo              | 50.4 ms                                                | 42.7 ms: 1.18x faster                                                           |
| hexiom                           | 4.85 ms                                                | 4.11 ms: 1.18x faster                                                           |
| logging_simple                   | 3.57 us                                                | 3.03 us: 1.18x faster                                                           |
| logging_silent                   | 69.9 ns                                                | 59.3 ns: 1.18x faster                                                           |
| pickle_pure_python               | 213 us                                                 | 182 us: 1.17x faster                                                            |
| spectral_norm                    | 77.3 ms                                                | 66.0 ms: 1.17x faster                                                           |
| nqueens                          | 62.9 ms                                                | 53.8 ms: 1.17x faster                                                           |
| html5lib                         | 36.6 ms                                                | 31.5 ms: 1.16x faster                                                           |
| float                            | 56.2 ms                                                | 48.3 ms: 1.16x faster                                                           |
| async_tree_eager                 | 70.5 ms                                                | 60.6 ms: 1.16x faster                                                           |
| dask                             | 255 ms                                                 | 221 ms: 1.16x faster                                                            |
| logging_format                   | 3.85 us                                                | 3.33 us: 1.16x faster                                                           |
| sqlglot_parse                    | 856 us                                                 | 741 us: 1.16x faster                                                            |
| async_tree_eager_memoization     | 169 ms                                                 | 146 ms: 1.16x faster                                                            |
| regex_compile                    | 78.5 ms                                                | 68.0 ms: 1.15x faster                                                           |
| async_tree_memoization           | 270 ms                                                 | 235 ms: 1.15x faster                                                            |
| async_tree_none_tg               | 198 ms                                                 | 173 ms: 1.15x faster                                                            |
| unpickle_pure_python             | 163 us                                                 | 143 us: 1.14x faster                                                            |
| pprint_safe_repr                 | 531 ms                                                 | 464 ms: 1.14x faster                                                            |
| richards_super                   | 39.1 ms                                                | 34.3 ms: 1.14x faster                                                           |
| python_startup                   | 17.0 ms                                                | 14.9 ms: 1.14x faster                                                           |
| richards                         | 35.4 ms                                                | 31.2 ms: 1.14x faster                                                           |
| pprint_pformat                   | 1.08 sec                                               | 948 ms: 1.14x faster                                                            |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 122 ms: 1.14x faster                                                            |
| sqlglot_transpile                | 1.02 ms                                                | 902 us: 1.13x faster                                                            |
| sqlglot_normalize                | 189 ms                                                 | 167 ms: 1.13x faster                                                            |
| django_template                  | 22.2 ms                                                | 19.7 ms: 1.12x faster                                                           |
| comprehensions                   | 12.2 us                                                | 10.9 us: 1.12x faster                                                           |
| sqlglot_optimize                 | 34.9 ms                                                | 31.2 ms: 1.12x faster                                                           |
| bench_thread_pool                | 506 us                                                 | 453 us: 1.12x faster                                                            |
| genshi_xml                       | 34.4 ms                                                | 30.8 ms: 1.12x faster                                                           |
| python_startup_no_site           | 13.7 ms                                                | 12.3 ms: 1.11x faster                                                           |
| mako                             | 7.68 ms                                                | 6.93 ms: 1.11x faster                                                           |
| scimark_lu                       | 76.5 ms                                                | 69.3 ms: 1.10x faster                                                           |
| pycparser                        | 706 ms                                                 | 639 ms: 1.10x faster                                                            |
| go                               | 115 ms                                                 | 104 ms: 1.10x faster                                                            |
| scimark_sor                      | 106 ms                                                 | 96.1 ms: 1.10x faster                                                           |
| scimark_fft                      | 201 ms                                                 | 183 ms: 1.10x faster                                                            |
| xml_etree_process                | 40.9 ms                                                | 37.2 ms: 1.10x faster                                                           |
| 2to3                             | 178 ms                                                 | 162 ms: 1.10x faster                                                            |
| sympy_str                        | 145 ms                                                 | 133 ms: 1.09x faster                                                            |
| typing_runtime_protocols         | 101 us                                                 | 92.7 us: 1.09x faster                                                           |
| sympy_integrate                  | 11.3 ms                                                | 10.4 ms: 1.09x faster                                                           |
| asyncio_tcp                      | 457 ms                                                 | 421 ms: 1.09x faster                                                            |
| bench_mp_pool                    | 50.9 ms                                                | 46.9 ms: 1.08x faster                                                           |
| pyflate                          | 351 ms                                                 | 324 ms: 1.08x faster                                                            |
| xml_etree_generate               | 56.6 ms                                                | 52.3 ms: 1.08x faster                                                           |
| thrift                           | 466 us                                                 | 431 us: 1.08x faster                                                            |
| sympy_sum                        | 75.6 ms                                                | 70.0 ms: 1.08x faster                                                           |
| async_tree_none                  | 212 ms                                                 | 197 ms: 1.07x faster                                                            |
| sympy_expand                     | 246 ms                                                 | 230 ms: 1.07x faster                                                            |
| crypto_pyaes                     | 54.0 ms                                                | 50.5 ms: 1.07x faster                                                           |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 2.80 ms: 1.07x faster                                                           |
| mdp                              | 1.50 sec                                               | 1.41 sec: 1.07x faster                                                          |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 355 ms: 1.06x faster                                                            |
| fannkuch                         | 282 ms                                                 | 267 ms: 1.06x faster                                                            |
| tomli_loads                      | 1.56 sec                                               | 1.48 sec: 1.05x faster                                                          |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 330 ms: 1.05x faster                                                            |
| async_generators                 | 294 ms                                                 | 280 ms: 1.05x faster                                                            |
| bpe_tokeniser                    | 3.24 sec                                               | 3.10 sec: 1.04x faster                                                          |
| telco                            | 4.80 ms                                                | 4.61 ms: 1.04x faster                                                           |
| regex_effbot                     | 2.63 ms                                                | 2.54 ms: 1.03x faster                                                           |
| meteor_contest                   | 73.8 ms                                                | 71.5 ms: 1.03x faster                                                           |
| coverage                         | 46.1 ms                                                | 44.7 ms: 1.03x faster                                                           |
| json_dumps                       | 6.56 ms                                                | 6.41 ms: 1.02x faster                                                           |
| xml_etree_parse                  | 109 ms                                                 | 107 ms: 1.02x faster                                                            |
| xml_etree_iterparse              | 74.2 ms                                                | 72.8 ms: 1.02x faster                                                           |
| gc_traversal                     | 2.48 ms                                                | 2.46 ms: 1.01x faster                                                           |
| pidigits                         | 284 ms                                                 | 281 ms: 1.01x faster                                                            |
| async_tree_cpu_io_mixed_tg       | 447 ms                                                 | 444 ms: 1.01x faster                                                            |
| json_loads                       | 16.9 us                                                | 17.0 us: 1.01x slower                                                           |
| regex_dna                        | 148 ms                                                 | 149 ms: 1.01x slower                                                            |
| docutils                         | 1.44 sec                                               | 1.48 sec: 1.03x slower                                                          |
| regex_v8                         | 16.9 ms                                                | 17.7 ms: 1.04x slower                                                           |
| async_tree_io                    | 507 ms                                                 | 530 ms: 1.05x slower                                                            |
| create_gc_cycles                 | 803 us                                                 | 893 us: 1.11x slower                                                            |
| async_tree_eager_io              | 513 ms                                                 | 645 ms: 1.26x slower                                                            |
| async_tree_eager_io_tg           | 477 ms                                                 | 668 ms: 1.40x slower                                                            |
| asyncio_websockets               | 241 ms                                                 | 408 ms: 1.69x slower                                                            |
| Geometric mean                   | (ref)                                                  | 1.10x faster                                                                    |

Benchmark hidden because not significant (7): tornado_http, pylint, async_tree_cpu_io_mixed, async_tree_io_tg, pathlib, json, asyncio_tcp_ssl
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: 0.98x