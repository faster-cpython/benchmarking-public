# Results vs. 3.13.0

- fork: python
- ref: 04eb5c8db1e24cabd0cb
- machine: darwin-arm64
- commit hash: 04eb5c8
- commit date: 2024-07-27
- overall geometric mean: 1.07x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 178 ms                                                 | 171 ms: 1.04x faster                                                  |
| docutils       | 1.44 sec                                               | 1.53 sec: 1.06x slower                                                |
| html5lib       | 36.6 ms                                                | 30.6 ms: 1.20x faster                                                 |
| Geometric mean | (ref)                                                  | 1.08x faster                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg        | 291 ms                                                 | 228 ms: 1.27x faster                                                  |
| coroutines                       | 19.8 ms                                                | 16.1 ms: 1.23x faster                                                 |
| async_tree_eager_tg              | 48.4 ms                                                | 41.6 ms: 1.16x faster                                                 |
| async_tree_eager                 | 70.5 ms                                                | 61.7 ms: 1.14x faster                                                 |
| async_tree_eager_memoization     | 169 ms                                                 | 151 ms: 1.12x faster                                                  |
| async_tree_memoization           | 270 ms                                                 | 241 ms: 1.12x faster                                                  |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 124 ms: 1.12x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 182 ms: 1.09x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 195 ms: 1.09x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 355 ms: 1.05x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 332 ms: 1.05x faster                                                  |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 454 ms: 1.01x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 447 ms                                                 | 441 ms: 1.01x faster                                                  |
| async_generators                 | 294 ms                                                 | 292 ms: 1.01x faster                                                  |
| asyncio_tcp_ssl                  | 1.26 sec                                               | 1.28 sec: 1.01x slower                                                |
| async_tree_io                    | 507 ms                                                 | 544 ms: 1.07x slower                                                  |
| async_tree_eager_io              | 513 ms                                                 | 638 ms: 1.24x slower                                                  |
| async_tree_eager_io_tg           | 477 ms                                                 | 677 ms: 1.42x slower                                                  |
| asyncio_websockets               | 241 ms                                                 | 408 ms: 1.69x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (2): asyncio_tcp, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 56.2 ms                                                | 45.9 ms: 1.22x faster                                                 |
| nbody          | 73.9 ms                                                | 63.0 ms: 1.17x faster                                                 |
| pidigits       | 284 ms                                                 | 282 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.13x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 78.5 ms                                                | 72.8 ms: 1.08x faster                                                 |
| regex_effbot   | 2.63 ms                                                | 2.56 ms: 1.03x faster                                                 |
| regex_dna      | 148 ms                                                 | 149 ms: 1.01x slower                                                  |
| regex_v8       | 16.9 ms                                                | 17.3 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                  | 1.02x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 1.56 sec                                               | 1.24 sec: 1.26x faster                                                |
| pickle_pure_python   | 213 us                                                 | 171 us: 1.24x faster                                                  |
| unpickle_pure_python | 163 us                                                 | 133 us: 1.23x faster                                                  |
| xml_etree_process    | 40.9 ms                                                | 35.4 ms: 1.15x faster                                                 |
| xml_etree_generate   | 56.6 ms                                                | 52.0 ms: 1.09x faster                                                 |
| xml_etree_parse      | 109 ms                                                 | 104 ms: 1.05x faster                                                  |
| xml_etree_iterparse  | 74.2 ms                                                | 70.9 ms: 1.05x faster                                                 |
| json_dumps           | 6.56 ms                                                | 6.38 ms: 1.03x faster                                                 |
| json_loads           | 16.9 us                                                | 17.0 us: 1.01x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.12x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 17.0 ms                                                | 15.3 ms: 1.11x faster                                                 |
| python_startup_no_site | 13.7 ms                                                | 12.7 ms: 1.07x faster                                                 |
| Geometric mean         | (ref)                                                  | 1.09x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 7.68 ms                                                | 6.39 ms: 1.20x faster                                                 |
| django_template | 22.2 ms                                                | 21.1 ms: 1.05x faster                                                 |
| genshi_text     | 16.9 ms                                                | 16.5 ms: 1.02x faster                                                 |
| genshi_xml      | 34.4 ms                                                | 40.4 ms: 1.17x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo                    | 27.2 us                                                | 16.5 us: 1.65x faster                                                 |
| deepcopy                         | 232 us                                                 | 151 us: 1.54x faster                                                  |
| generators                       | 31.5 ms                                                | 21.5 ms: 1.46x faster                                                 |
| deepcopy_reduce                  | 2.06 us                                                | 1.56 us: 1.32x faster                                                 |
| async_tree_memoization_tg        | 291 ms                                                 | 228 ms: 1.27x faster                                                  |
| tomli_loads                      | 1.56 sec                                               | 1.24 sec: 1.26x faster                                                |
| pickle_pure_python               | 213 us                                                 | 171 us: 1.24x faster                                                  |
| unpickle_pure_python             | 163 us                                                 | 133 us: 1.23x faster                                                  |
| coroutines                       | 19.8 ms                                                | 16.1 ms: 1.23x faster                                                 |
| float                            | 56.2 ms                                                | 45.9 ms: 1.22x faster                                                 |
| logging_simple                   | 3.57 us                                                | 2.94 us: 1.22x faster                                                 |
| mako                             | 7.68 ms                                                | 6.39 ms: 1.20x faster                                                 |
| html5lib                         | 36.6 ms                                                | 30.6 ms: 1.20x faster                                                 |
| logging_format                   | 3.85 us                                                | 3.24 us: 1.19x faster                                                 |
| scimark_monte_carlo              | 50.4 ms                                                | 42.7 ms: 1.18x faster                                                 |
| deltablue                        | 2.68 ms                                                | 2.27 ms: 1.18x faster                                                 |
| nbody                            | 73.9 ms                                                | 63.0 ms: 1.17x faster                                                 |
| richards                         | 35.4 ms                                                | 30.2 ms: 1.17x faster                                                 |
| async_tree_eager_tg              | 48.4 ms                                                | 41.6 ms: 1.16x faster                                                 |
| xml_etree_process                | 40.9 ms                                                | 35.4 ms: 1.15x faster                                                 |
| spectral_norm                    | 77.3 ms                                                | 66.9 ms: 1.15x faster                                                 |
| go                               | 115 ms                                                 | 99.7 ms: 1.15x faster                                                 |
| richards_super                   | 39.1 ms                                                | 33.9 ms: 1.15x faster                                                 |
| logging_silent                   | 69.9 ns                                                | 61.0 ns: 1.15x faster                                                 |
| async_tree_eager                 | 70.5 ms                                                | 61.7 ms: 1.14x faster                                                 |
| dask                             | 255 ms                                                 | 224 ms: 1.14x faster                                                  |
| raytrace                         | 182 ms                                                 | 160 ms: 1.14x faster                                                  |
| pyflate                          | 351 ms                                                 | 310 ms: 1.13x faster                                                  |
| fannkuch                         | 282 ms                                                 | 249 ms: 1.13x faster                                                  |
| async_tree_eager_memoization     | 169 ms                                                 | 151 ms: 1.12x faster                                                  |
| async_tree_memoization           | 270 ms                                                 | 241 ms: 1.12x faster                                                  |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 124 ms: 1.12x faster                                                  |
| python_startup                   | 17.0 ms                                                | 15.3 ms: 1.11x faster                                                 |
| pprint_safe_repr                 | 531 ms                                                 | 477 ms: 1.11x faster                                                  |
| nqueens                          | 62.9 ms                                                | 56.6 ms: 1.11x faster                                                 |
| hexiom                           | 4.85 ms                                                | 4.38 ms: 1.11x faster                                                 |
| pprint_pformat                   | 1.08 sec                                               | 974 ms: 1.11x faster                                                  |
| scimark_fft                      | 201 ms                                                 | 184 ms: 1.09x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 182 ms: 1.09x faster                                                  |
| xml_etree_generate               | 56.6 ms                                                | 52.0 ms: 1.09x faster                                                 |
| async_tree_none                  | 212 ms                                                 | 195 ms: 1.09x faster                                                  |
| regex_compile                    | 78.5 ms                                                | 72.8 ms: 1.08x faster                                                 |
| sqlglot_normalize                | 189 ms                                                 | 175 ms: 1.08x faster                                                  |
| bench_thread_pool                | 506 us                                                 | 470 us: 1.08x faster                                                  |
| python_startup_no_site           | 13.7 ms                                                | 12.7 ms: 1.07x faster                                                 |
| bpe_tokeniser                    | 3.24 sec                                               | 3.02 sec: 1.07x faster                                                |
| thrift                           | 466 us                                                 | 434 us: 1.07x faster                                                  |
| chaos                            | 41.3 ms                                                | 38.5 ms: 1.07x faster                                                 |
| sqlglot_optimize                 | 34.9 ms                                                | 32.8 ms: 1.06x faster                                                 |
| typing_runtime_protocols         | 101 us                                                 | 95.1 us: 1.06x faster                                                 |
| scimark_sor                      | 106 ms                                                 | 99.6 ms: 1.06x faster                                                 |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 355 ms: 1.05x faster                                                  |
| django_template                  | 22.2 ms                                                | 21.1 ms: 1.05x faster                                                 |
| pycparser                        | 706 ms                                                 | 670 ms: 1.05x faster                                                  |
| crypto_pyaes                     | 54.0 ms                                                | 51.4 ms: 1.05x faster                                                 |
| telco                            | 4.80 ms                                                | 4.57 ms: 1.05x faster                                                 |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 332 ms: 1.05x faster                                                  |
| xml_etree_parse                  | 109 ms                                                 | 104 ms: 1.05x faster                                                  |
| sympy_str                        | 145 ms                                                 | 139 ms: 1.05x faster                                                  |
| xml_etree_iterparse              | 74.2 ms                                                | 70.9 ms: 1.05x faster                                                 |
| mdp                              | 1.50 sec                                               | 1.44 sec: 1.04x faster                                                |
| sqlglot_parse                    | 856 us                                                 | 820 us: 1.04x faster                                                  |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 2.87 ms: 1.04x faster                                                 |
| meteor_contest                   | 73.8 ms                                                | 71.0 ms: 1.04x faster                                                 |
| 2to3                             | 178 ms                                                 | 171 ms: 1.04x faster                                                  |
| sympy_sum                        | 75.6 ms                                                | 73.1 ms: 1.03x faster                                                 |
| json_dumps                       | 6.56 ms                                                | 6.38 ms: 1.03x faster                                                 |
| sqlglot_transpile                | 1.02 ms                                                | 996 us: 1.03x faster                                                  |
| sympy_expand                     | 246 ms                                                 | 240 ms: 1.03x faster                                                  |
| regex_effbot                     | 2.63 ms                                                | 2.56 ms: 1.03x faster                                                 |
| genshi_text                      | 16.9 ms                                                | 16.5 ms: 1.02x faster                                                 |
| sympy_integrate                  | 11.3 ms                                                | 11.1 ms: 1.02x faster                                                 |
| coverage                         | 46.1 ms                                                | 45.1 ms: 1.02x faster                                                 |
| dulwich_log                      | 28.7 ms                                                | 28.2 ms: 1.02x faster                                                 |
| json                             | 2.94 ms                                                | 2.89 ms: 1.02x faster                                                 |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 454 ms: 1.01x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 447 ms                                                 | 441 ms: 1.01x faster                                                  |
| gc_traversal                     | 2.48 ms                                                | 2.46 ms: 1.01x faster                                                 |
| pidigits                         | 284 ms                                                 | 282 ms: 1.01x faster                                                  |
| async_generators                 | 294 ms                                                 | 292 ms: 1.01x faster                                                  |
| comprehensions                   | 12.2 us                                                | 12.3 us: 1.01x slower                                                 |
| json_loads                       | 16.9 us                                                | 17.0 us: 1.01x slower                                                 |
| regex_dna                        | 148 ms                                                 | 149 ms: 1.01x slower                                                  |
| asyncio_tcp_ssl                  | 1.26 sec                                               | 1.28 sec: 1.01x slower                                                |
| regex_v8                         | 16.9 ms                                                | 17.3 ms: 1.02x slower                                                 |
| pathlib                          | 22.8 ms                                                | 23.4 ms: 1.03x slower                                                 |
| scimark_lu                       | 76.5 ms                                                | 79.6 ms: 1.04x slower                                                 |
| docutils                         | 1.44 sec                                               | 1.53 sec: 1.06x slower                                                |
| async_tree_io                    | 507 ms                                                 | 544 ms: 1.07x slower                                                  |
| create_gc_cycles                 | 803 us                                                 | 907 us: 1.13x slower                                                  |
| genshi_xml                       | 34.4 ms                                                | 40.4 ms: 1.17x slower                                                 |
| async_tree_eager_io              | 513 ms                                                 | 638 ms: 1.24x slower                                                  |
| async_tree_eager_io_tg           | 477 ms                                                 | 677 ms: 1.42x slower                                                  |
| asyncio_websockets               | 241 ms                                                 | 408 ms: 1.69x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.07x faster                                                          |

Benchmark hidden because not significant (5): tornado_http, asyncio_tcp, async_tree_io_tg, bench_mp_pool, pylint
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 0.98x