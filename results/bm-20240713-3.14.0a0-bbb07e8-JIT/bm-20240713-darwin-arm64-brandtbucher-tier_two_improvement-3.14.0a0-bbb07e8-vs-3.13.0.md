# Results vs. 3.13.0

- fork: brandtbucher
- ref: tier_two_improvement
- machine: darwin-arm64
- commit hash: bbb07e8
- commit date: 2024-07-13
- overall geometric mean: 1.06x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 6.32x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-darwin-arm64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 178 ms                                                 | 171 ms: 1.04x faster                                                        |
| docutils       | 1.44 sec                                               | 1.51 sec: 1.05x slower                                                      |
| html5lib       | 36.6 ms                                                | 30.9 ms: 1.19x faster                                                       |
| Geometric mean | (ref)                                                  | 1.08x faster                                                                |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-darwin-arm64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| coroutines                       | 19.8 ms                                                | 15.8 ms: 1.25x faster                                                       |
| async_tree_memoization_tg        | 291 ms                                                 | 242 ms: 1.20x faster                                                        |
| async_tree_eager_tg              | 48.4 ms                                                | 41.1 ms: 1.18x faster                                                       |
| async_tree_memoization           | 270 ms                                                 | 232 ms: 1.17x faster                                                        |
| async_tree_eager_memoization     | 169 ms                                                 | 150 ms: 1.13x faster                                                        |
| async_tree_none_tg               | 198 ms                                                 | 177 ms: 1.12x faster                                                        |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 124 ms: 1.12x faster                                                        |
| async_tree_eager                 | 70.5 ms                                                | 63.5 ms: 1.11x faster                                                       |
| asyncio_tcp                      | 457 ms                                                 | 419 ms: 1.09x faster                                                        |
| async_tree_none                  | 212 ms                                                 | 195 ms: 1.09x faster                                                        |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 335 ms: 1.04x faster                                                        |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 361 ms: 1.04x faster                                                        |
| async_tree_cpu_io_mixed_tg       | 447 ms                                                 | 449 ms: 1.00x slower                                                        |
| asyncio_tcp_ssl                  | 1.26 sec                                               | 1.31 sec: 1.04x slower                                                      |
| async_tree_io                    | 507 ms                                                 | 535 ms: 1.06x slower                                                        |
| async_tree_eager_io              | 513 ms                                                 | 740 ms: 1.44x slower                                                        |
| async_tree_eager_io_tg           | 477 ms                                                 | 699 ms: 1.47x slower                                                        |
| asyncio_websockets               | 241 ms                                                 | 410 ms: 1.70x slower                                                        |
| Geometric mean                   | (ref)                                                  | 1.00x faster                                                                |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed, async_generators, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-darwin-arm64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 56.2 ms                                                | 47.6 ms: 1.18x faster                                                       |
| nbody          | 73.9 ms                                                | 64.1 ms: 1.15x faster                                                       |
| Geometric mean | (ref)                                                  | 1.11x faster                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-darwin-arm64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 78.5 ms                                                | 73.8 ms: 1.06x faster                                                       |
| regex_effbot   | 2.63 ms                                                | 2.57 ms: 1.02x faster                                                       |
| regex_dna      | 148 ms                                                 | 149 ms: 1.01x slower                                                        |
| regex_v8       | 16.9 ms                                                | 17.3 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-darwin-arm64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 1.56 sec                                               | 1.23 sec: 1.26x faster                                                      |
| unpickle_pure_python | 163 us                                                 | 133 us: 1.23x faster                                                        |
| pickle_pure_python   | 213 us                                                 | 175 us: 1.21x faster                                                        |
| xml_etree_process    | 40.9 ms                                                | 36.4 ms: 1.12x faster                                                       |
| xml_etree_generate   | 56.6 ms                                                | 52.4 ms: 1.08x faster                                                       |
| xml_etree_iterparse  | 74.2 ms                                                | 70.5 ms: 1.05x faster                                                       |
| json_dumps           | 6.56 ms                                                | 6.41 ms: 1.02x faster                                                       |
| xml_etree_parse      | 109 ms                                                 | 107 ms: 1.02x faster                                                        |
| json_loads           | 16.9 us                                                | 17.4 us: 1.03x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.10x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-darwin-arm64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 17.0 ms                                                | 15.4 ms: 1.10x faster                                                       |
| python_startup_no_site | 13.7 ms                                                | 12.8 ms: 1.07x faster                                                       |
| Geometric mean         | (ref)                                                  | 1.09x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-darwin-arm64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.68 ms                                                | 6.47 ms: 1.19x faster                                                       |
| genshi_text     | 16.9 ms                                                | 16.3 ms: 1.03x faster                                                       |
| django_template | 22.2 ms                                                | 21.6 ms: 1.03x faster                                                       |
| genshi_xml      | 34.4 ms                                                | 39.8 ms: 1.16x slower                                                       |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                                |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240713-darwin-arm64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo                    | 27.2 us                                                | 16.8 us: 1.62x faster                                                       |
| deepcopy                         | 232 us                                                 | 153 us: 1.52x faster                                                        |
| generators                       | 31.5 ms                                                | 22.4 ms: 1.41x faster                                                       |
| deepcopy_reduce                  | 2.06 us                                                | 1.55 us: 1.33x faster                                                       |
| tomli_loads                      | 1.56 sec                                               | 1.23 sec: 1.26x faster                                                      |
| coroutines                       | 19.8 ms                                                | 15.8 ms: 1.25x faster                                                       |
| unpickle_pure_python             | 163 us                                                 | 133 us: 1.23x faster                                                        |
| pickle_pure_python               | 213 us                                                 | 175 us: 1.21x faster                                                        |
| async_tree_memoization_tg        | 291 ms                                                 | 242 ms: 1.20x faster                                                        |
| mako                             | 7.68 ms                                                | 6.47 ms: 1.19x faster                                                       |
| html5lib                         | 36.6 ms                                                | 30.9 ms: 1.19x faster                                                       |
| float                            | 56.2 ms                                                | 47.6 ms: 1.18x faster                                                       |
| async_tree_eager_tg              | 48.4 ms                                                | 41.1 ms: 1.18x faster                                                       |
| async_tree_memoization           | 270 ms                                                 | 232 ms: 1.17x faster                                                        |
| logging_simple                   | 3.57 us                                                | 3.07 us: 1.16x faster                                                       |
| deltablue                        | 2.68 ms                                                | 2.32 ms: 1.15x faster                                                       |
| nbody                            | 73.9 ms                                                | 64.1 ms: 1.15x faster                                                       |
| richards                         | 35.4 ms                                                | 30.9 ms: 1.15x faster                                                       |
| scimark_monte_carlo              | 50.4 ms                                                | 43.9 ms: 1.15x faster                                                       |
| fannkuch                         | 282 ms                                                 | 246 ms: 1.15x faster                                                        |
| logging_format                   | 3.85 us                                                | 3.37 us: 1.14x faster                                                       |
| go                               | 115 ms                                                 | 101 ms: 1.14x faster                                                        |
| richards_super                   | 39.1 ms                                                | 34.5 ms: 1.14x faster                                                       |
| dask                             | 255 ms                                                 | 226 ms: 1.13x faster                                                        |
| async_tree_eager_memoization     | 169 ms                                                 | 150 ms: 1.13x faster                                                        |
| spectral_norm                    | 77.3 ms                                                | 68.6 ms: 1.13x faster                                                       |
| xml_etree_process                | 40.9 ms                                                | 36.4 ms: 1.12x faster                                                       |
| async_tree_none_tg               | 198 ms                                                 | 177 ms: 1.12x faster                                                        |
| logging_silent                   | 69.9 ns                                                | 62.2 ns: 1.12x faster                                                       |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 124 ms: 1.12x faster                                                        |
| pyflate                          | 351 ms                                                 | 314 ms: 1.12x faster                                                        |
| async_tree_eager                 | 70.5 ms                                                | 63.5 ms: 1.11x faster                                                       |
| hexiom                           | 4.85 ms                                                | 4.39 ms: 1.11x faster                                                       |
| python_startup                   | 17.0 ms                                                | 15.4 ms: 1.10x faster                                                       |
| pprint_safe_repr                 | 531 ms                                                 | 482 ms: 1.10x faster                                                        |
| raytrace                         | 182 ms                                                 | 165 ms: 1.10x faster                                                        |
| pprint_pformat                   | 1.08 sec                                               | 986 ms: 1.09x faster                                                        |
| asyncio_tcp                      | 457 ms                                                 | 419 ms: 1.09x faster                                                        |
| async_tree_none                  | 212 ms                                                 | 195 ms: 1.09x faster                                                        |
| nqueens                          | 62.9 ms                                                | 58.0 ms: 1.08x faster                                                       |
| xml_etree_generate               | 56.6 ms                                                | 52.4 ms: 1.08x faster                                                       |
| thrift                           | 466 us                                                 | 435 us: 1.07x faster                                                        |
| python_startup_no_site           | 13.7 ms                                                | 12.8 ms: 1.07x faster                                                       |
| bench_thread_pool                | 506 us                                                 | 473 us: 1.07x faster                                                        |
| bpe_tokeniser                    | 3.24 sec                                               | 3.04 sec: 1.07x faster                                                      |
| regex_compile                    | 78.5 ms                                                | 73.8 ms: 1.06x faster                                                       |
| sqlglot_normalize                | 189 ms                                                 | 179 ms: 1.06x faster                                                        |
| telco                            | 4.80 ms                                                | 4.55 ms: 1.05x faster                                                       |
| xml_etree_iterparse              | 74.2 ms                                                | 70.5 ms: 1.05x faster                                                       |
| sqlglot_optimize                 | 34.9 ms                                                | 33.4 ms: 1.05x faster                                                       |
| scimark_sor                      | 106 ms                                                 | 101 ms: 1.04x faster                                                        |
| scimark_fft                      | 201 ms                                                 | 192 ms: 1.04x faster                                                        |
| chaos                            | 41.3 ms                                                | 39.6 ms: 1.04x faster                                                       |
| crypto_pyaes                     | 54.0 ms                                                | 51.9 ms: 1.04x faster                                                       |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 335 ms: 1.04x faster                                                        |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 361 ms: 1.04x faster                                                        |
| 2to3                             | 178 ms                                                 | 171 ms: 1.04x faster                                                        |
| typing_runtime_protocols         | 101 us                                                 | 97.4 us: 1.04x faster                                                       |
| pycparser                        | 706 ms                                                 | 682 ms: 1.04x faster                                                        |
| sympy_str                        | 145 ms                                                 | 141 ms: 1.04x faster                                                        |
| sympy_sum                        | 75.6 ms                                                | 73.1 ms: 1.03x faster                                                       |
| genshi_text                      | 16.9 ms                                                | 16.3 ms: 1.03x faster                                                       |
| meteor_contest                   | 73.8 ms                                                | 71.6 ms: 1.03x faster                                                       |
| django_template                  | 22.2 ms                                                | 21.6 ms: 1.03x faster                                                       |
| sqlglot_parse                    | 856 us                                                 | 836 us: 1.02x faster                                                        |
| json_dumps                       | 6.56 ms                                                | 6.41 ms: 1.02x faster                                                       |
| sympy_integrate                  | 11.3 ms                                                | 11.1 ms: 1.02x faster                                                       |
| regex_effbot                     | 2.63 ms                                                | 2.57 ms: 1.02x faster                                                       |
| xml_etree_parse                  | 109 ms                                                 | 107 ms: 1.02x faster                                                        |
| sqlglot_transpile                | 1.02 ms                                                | 1.01 ms: 1.02x faster                                                       |
| coverage                         | 46.1 ms                                                | 45.5 ms: 1.01x faster                                                       |
| sympy_expand                     | 246 ms                                                 | 243 ms: 1.01x faster                                                        |
| gc_traversal                     | 2.48 ms                                                | 2.47 ms: 1.01x faster                                                       |
| async_tree_cpu_io_mixed_tg       | 447 ms                                                 | 449 ms: 1.00x slower                                                        |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 3.03 ms: 1.01x slower                                                       |
| regex_dna                        | 148 ms                                                 | 149 ms: 1.01x slower                                                        |
| comprehensions                   | 12.2 us                                                | 12.4 us: 1.02x slower                                                       |
| regex_v8                         | 16.9 ms                                                | 17.3 ms: 1.02x slower                                                       |
| json_loads                       | 16.9 us                                                | 17.4 us: 1.03x slower                                                       |
| pathlib                          | 22.8 ms                                                | 23.6 ms: 1.03x slower                                                       |
| asyncio_tcp_ssl                  | 1.26 sec                                               | 1.31 sec: 1.04x slower                                                      |
| mdp                              | 1.50 sec                                               | 1.56 sec: 1.04x slower                                                      |
| docutils                         | 1.44 sec                                               | 1.51 sec: 1.05x slower                                                      |
| async_tree_io                    | 507 ms                                                 | 535 ms: 1.06x slower                                                        |
| scimark_lu                       | 76.5 ms                                                | 82.8 ms: 1.08x slower                                                       |
| create_gc_cycles                 | 803 us                                                 | 905 us: 1.13x slower                                                        |
| genshi_xml                       | 34.4 ms                                                | 39.8 ms: 1.16x slower                                                       |
| async_tree_eager_io              | 513 ms                                                 | 740 ms: 1.44x slower                                                        |
| async_tree_eager_io_tg           | 477 ms                                                 | 699 ms: 1.47x slower                                                        |
| asyncio_websockets               | 241 ms                                                 | 410 ms: 1.70x slower                                                        |
| Geometric mean                   | (ref)                                                  | 1.06x faster                                                                |

Benchmark hidden because not significant (8): tornado_http, async_tree_cpu_io_mixed, pylint, bench_mp_pool, pidigits, async_generators, json, async_tree_io_tg
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 6.32x