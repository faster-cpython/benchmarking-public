# Results vs. 3.13.0

- fork: faster-cpython
- ref: monitoring_branch_ta
- machine: darwin-arm64
- commit hash: dc5a9d5
- commit date: 2024-08-01
- overall geometric mean: 1.08x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240801-darwin-arm64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 178 ms                                                 | 170 ms: 1.05x faster                                                            |
| docutils       | 1.44 sec                                               | 1.53 sec: 1.06x slower                                                          |
| html5lib       | 36.6 ms                                                | 29.4 ms: 1.25x faster                                                           |
| Geometric mean | (ref)                                                  | 1.09x faster                                                                    |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240801-darwin-arm64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| coroutines                       | 19.8 ms                                                | 14.4 ms: 1.37x faster                                                           |
| async_tree_memoization_tg        | 291 ms                                                 | 224 ms: 1.30x faster                                                            |
| async_tree_eager_tg              | 48.4 ms                                                | 41.5 ms: 1.17x faster                                                           |
| async_tree_eager_memoization     | 169 ms                                                 | 147 ms: 1.15x faster                                                            |
| async_tree_memoization           | 270 ms                                                 | 236 ms: 1.15x faster                                                            |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 121 ms: 1.14x faster                                                            |
| async_tree_eager                 | 70.5 ms                                                | 61.9 ms: 1.14x faster                                                           |
| async_tree_none                  | 212 ms                                                 | 189 ms: 1.12x faster                                                            |
| async_tree_none_tg               | 198 ms                                                 | 178 ms: 1.11x faster                                                            |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 354 ms: 1.06x faster                                                            |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 331 ms: 1.05x faster                                                            |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 448 ms: 1.03x faster                                                            |
| async_tree_cpu_io_mixed_tg       | 447 ms                                                 | 436 ms: 1.03x faster                                                            |
| async_generators                 | 294 ms                                                 | 292 ms: 1.01x faster                                                            |
| async_tree_io                    | 507 ms                                                 | 538 ms: 1.06x slower                                                            |
| async_tree_eager_io              | 513 ms                                                 | 616 ms: 1.20x slower                                                            |
| async_tree_eager_io_tg           | 477 ms                                                 | 652 ms: 1.37x slower                                                            |
| asyncio_websockets               | 241 ms                                                 | 408 ms: 1.69x slower                                                            |
| Geometric mean                   | (ref)                                                  | 1.03x faster                                                                    |

Benchmark hidden because not significant (3): asyncio_tcp, async_tree_io_tg, asyncio_tcp_ssl

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240801-darwin-arm64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 56.2 ms                                                | 46.6 ms: 1.21x faster                                                           |
| nbody          | 73.9 ms                                                | 62.9 ms: 1.18x faster                                                           |
| pidigits       | 284 ms                                                 | 282 ms: 1.01x faster                                                            |
| Geometric mean | (ref)                                                  | 1.13x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240801-darwin-arm64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 78.5 ms                                                | 72.1 ms: 1.09x faster                                                           |
| regex_effbot   | 2.63 ms                                                | 2.56 ms: 1.03x faster                                                           |
| regex_dna      | 148 ms                                                 | 149 ms: 1.01x slower                                                            |
| regex_v8       | 16.9 ms                                                | 17.2 ms: 1.02x slower                                                           |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240801-darwin-arm64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 1.56 sec                                               | 1.21 sec: 1.29x faster                                                          |
| unpickle_pure_python | 163 us                                                 | 128 us: 1.27x faster                                                            |
| pickle_pure_python   | 213 us                                                 | 170 us: 1.25x faster                                                            |
| xml_etree_process    | 40.9 ms                                                | 34.8 ms: 1.17x faster                                                           |
| xml_etree_generate   | 56.6 ms                                                | 51.1 ms: 1.11x faster                                                           |
| json_dumps           | 6.56 ms                                                | 6.19 ms: 1.06x faster                                                           |
| xml_etree_iterparse  | 74.2 ms                                                | 71.2 ms: 1.04x faster                                                           |
| xml_etree_parse      | 109 ms                                                 | 108 ms: 1.01x faster                                                            |
| json_loads           | 16.9 us                                                | 17.1 us: 1.02x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.13x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240801-darwin-arm64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 17.0 ms                                                | 15.4 ms: 1.11x faster                                                           |
| python_startup_no_site | 13.7 ms                                                | 12.8 ms: 1.06x faster                                                           |
| Geometric mean         | (ref)                                                  | 1.09x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240801-darwin-arm64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 13.7 ms: 1.23x faster                                                           |
| mako            | 7.68 ms                                                | 6.47 ms: 1.19x faster                                                           |
| django_template | 22.2 ms                                                | 21.4 ms: 1.04x faster                                                           |
| genshi_xml      | 34.4 ms                                                | 33.3 ms: 1.03x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.12x faster                                                                    |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240801-darwin-arm64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy_memo                    | 27.2 us                                                | 16.8 us: 1.62x faster                                                           |
| deepcopy                         | 232 us                                                 | 154 us: 1.51x faster                                                            |
| coroutines                       | 19.8 ms                                                | 14.4 ms: 1.37x faster                                                           |
| deepcopy_reduce                  | 2.06 us                                                | 1.52 us: 1.35x faster                                                           |
| scimark_sor                      | 106 ms                                                 | 79.6 ms: 1.33x faster                                                           |
| async_tree_memoization_tg        | 291 ms                                                 | 224 ms: 1.30x faster                                                            |
| tomli_loads                      | 1.56 sec                                               | 1.21 sec: 1.29x faster                                                          |
| generators                       | 31.5 ms                                                | 24.5 ms: 1.29x faster                                                           |
| unpickle_pure_python             | 163 us                                                 | 128 us: 1.27x faster                                                            |
| pickle_pure_python               | 213 us                                                 | 170 us: 1.25x faster                                                            |
| html5lib                         | 36.6 ms                                                | 29.4 ms: 1.25x faster                                                           |
| deltablue                        | 2.68 ms                                                | 2.17 ms: 1.24x faster                                                           |
| genshi_text                      | 16.9 ms                                                | 13.7 ms: 1.23x faster                                                           |
| go                               | 115 ms                                                 | 94.0 ms: 1.22x faster                                                           |
| logging_simple                   | 3.57 us                                                | 2.93 us: 1.22x faster                                                           |
| float                            | 56.2 ms                                                | 46.6 ms: 1.21x faster                                                           |
| logging_format                   | 3.85 us                                                | 3.24 us: 1.19x faster                                                           |
| mako                             | 7.68 ms                                                | 6.47 ms: 1.19x faster                                                           |
| richards                         | 35.4 ms                                                | 30.0 ms: 1.18x faster                                                           |
| nbody                            | 73.9 ms                                                | 62.9 ms: 1.18x faster                                                           |
| xml_etree_process                | 40.9 ms                                                | 34.8 ms: 1.17x faster                                                           |
| async_tree_eager_tg              | 48.4 ms                                                | 41.5 ms: 1.17x faster                                                           |
| scimark_monte_carlo              | 50.4 ms                                                | 43.5 ms: 1.16x faster                                                           |
| dask                             | 255 ms                                                 | 221 ms: 1.16x faster                                                            |
| async_tree_eager_memoization     | 169 ms                                                 | 147 ms: 1.15x faster                                                            |
| async_tree_memoization           | 270 ms                                                 | 236 ms: 1.15x faster                                                            |
| logging_silent                   | 69.9 ns                                                | 61.0 ns: 1.15x faster                                                           |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 121 ms: 1.14x faster                                                            |
| richards_super                   | 39.1 ms                                                | 34.3 ms: 1.14x faster                                                           |
| async_tree_eager                 | 70.5 ms                                                | 61.9 ms: 1.14x faster                                                           |
| pyflate                          | 351 ms                                                 | 309 ms: 1.14x faster                                                            |
| raytrace                         | 182 ms                                                 | 161 ms: 1.13x faster                                                            |
| spectral_norm                    | 77.3 ms                                                | 68.6 ms: 1.13x faster                                                           |
| async_tree_none                  | 212 ms                                                 | 189 ms: 1.12x faster                                                            |
| async_tree_none_tg               | 198 ms                                                 | 178 ms: 1.11x faster                                                            |
| fannkuch                         | 282 ms                                                 | 254 ms: 1.11x faster                                                            |
| xml_etree_generate               | 56.6 ms                                                | 51.1 ms: 1.11x faster                                                           |
| python_startup                   | 17.0 ms                                                | 15.4 ms: 1.11x faster                                                           |
| typing_runtime_protocols         | 101 us                                                 | 92.1 us: 1.10x faster                                                           |
| nqueens                          | 62.9 ms                                                | 57.7 ms: 1.09x faster                                                           |
| regex_compile                    | 78.5 ms                                                | 72.1 ms: 1.09x faster                                                           |
| hexiom                           | 4.85 ms                                                | 4.46 ms: 1.09x faster                                                           |
| pprint_safe_repr                 | 531 ms                                                 | 491 ms: 1.08x faster                                                            |
| bench_thread_pool                | 506 us                                                 | 469 us: 1.08x faster                                                            |
| pprint_pformat                   | 1.08 sec                                               | 1.01 sec: 1.07x faster                                                          |
| chaos                            | 41.3 ms                                                | 38.5 ms: 1.07x faster                                                           |
| sqlglot_normalize                | 189 ms                                                 | 176 ms: 1.07x faster                                                            |
| bpe_tokeniser                    | 3.24 sec                                               | 3.04 sec: 1.07x faster                                                          |
| pycparser                        | 706 ms                                                 | 662 ms: 1.07x faster                                                            |
| python_startup_no_site           | 13.7 ms                                                | 12.8 ms: 1.06x faster                                                           |
| thrift                           | 466 us                                                 | 438 us: 1.06x faster                                                            |
| sqlglot_optimize                 | 34.9 ms                                                | 32.9 ms: 1.06x faster                                                           |
| scimark_fft                      | 201 ms                                                 | 189 ms: 1.06x faster                                                            |
| json_dumps                       | 6.56 ms                                                | 6.19 ms: 1.06x faster                                                           |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 354 ms: 1.06x faster                                                            |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 331 ms: 1.05x faster                                                            |
| 2to3                             | 178 ms                                                 | 170 ms: 1.05x faster                                                            |
| telco                            | 4.80 ms                                                | 4.59 ms: 1.05x faster                                                           |
| crypto_pyaes                     | 54.0 ms                                                | 51.7 ms: 1.04x faster                                                           |
| sympy_str                        | 145 ms                                                 | 140 ms: 1.04x faster                                                            |
| xml_etree_iterparse              | 74.2 ms                                                | 71.2 ms: 1.04x faster                                                           |
| django_template                  | 22.2 ms                                                | 21.4 ms: 1.04x faster                                                           |
| genshi_xml                       | 34.4 ms                                                | 33.3 ms: 1.03x faster                                                           |
| sympy_sum                        | 75.6 ms                                                | 73.4 ms: 1.03x faster                                                           |
| meteor_contest                   | 73.8 ms                                                | 71.7 ms: 1.03x faster                                                           |
| mdp                              | 1.50 sec                                               | 1.46 sec: 1.03x faster                                                          |
| regex_effbot                     | 2.63 ms                                                | 2.56 ms: 1.03x faster                                                           |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 448 ms: 1.03x faster                                                            |
| dulwich_log                      | 28.7 ms                                                | 28.0 ms: 1.03x faster                                                           |
| async_tree_cpu_io_mixed_tg       | 447 ms                                                 | 436 ms: 1.03x faster                                                            |
| sqlglot_parse                    | 856 us                                                 | 836 us: 1.02x faster                                                            |
| coverage                         | 46.1 ms                                                | 45.0 ms: 1.02x faster                                                           |
| sympy_expand                     | 246 ms                                                 | 242 ms: 1.02x faster                                                            |
| sqlglot_transpile                | 1.02 ms                                                | 1.01 ms: 1.01x faster                                                           |
| xml_etree_parse                  | 109 ms                                                 | 108 ms: 1.01x faster                                                            |
| async_generators                 | 294 ms                                                 | 292 ms: 1.01x faster                                                            |
| pidigits                         | 284 ms                                                 | 282 ms: 1.01x faster                                                            |
| comprehensions                   | 12.2 us                                                | 12.2 us: 1.01x slower                                                           |
| regex_dna                        | 148 ms                                                 | 149 ms: 1.01x slower                                                            |
| json_loads                       | 16.9 us                                                | 17.1 us: 1.02x slower                                                           |
| regex_v8                         | 16.9 ms                                                | 17.2 ms: 1.02x slower                                                           |
| pathlib                          | 22.8 ms                                                | 23.5 ms: 1.03x slower                                                           |
| scimark_lu                       | 76.5 ms                                                | 79.9 ms: 1.04x slower                                                           |
| docutils                         | 1.44 sec                                               | 1.53 sec: 1.06x slower                                                          |
| async_tree_io                    | 507 ms                                                 | 538 ms: 1.06x slower                                                            |
| create_gc_cycles                 | 803 us                                                 | 902 us: 1.12x slower                                                            |
| async_tree_eager_io              | 513 ms                                                 | 616 ms: 1.20x slower                                                            |
| async_tree_eager_io_tg           | 477 ms                                                 | 652 ms: 1.37x slower                                                            |
| asyncio_websockets               | 241 ms                                                 | 408 ms: 1.69x slower                                                            |
| Geometric mean                   | (ref)                                                  | 1.08x faster                                                                    |

Benchmark hidden because not significant (10): tornado_http, asyncio_tcp, json, async_tree_io_tg, gc_traversal, sympy_integrate, bench_mp_pool, scimark_sparse_mat_mult, asyncio_tcp_ssl, pylint
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 0.98x