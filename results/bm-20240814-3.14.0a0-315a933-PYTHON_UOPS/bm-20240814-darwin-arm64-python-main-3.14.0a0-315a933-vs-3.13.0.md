# Results vs. 3.13.0

- fork: python
- ref: main
- machine: darwin-arm64
- commit hash: 315a933
- commit date: 2024-08-14
- overall geometric mean: 1.05x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240814-darwin-arm64-python-main-3.14.0a0-315a933 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| 2to3           | 178 ms                                                 | 186 ms: 1.05x slower                                  |
| docutils       | 1.44 sec                                               | 1.70 sec: 1.18x slower                                |
| html5lib       | 36.6 ms                                                | 35.3 ms: 1.04x faster                                 |
| Geometric mean | (ref)                                                  | 1.02x slower                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240814-darwin-arm64-python-main-3.14.0a0-315a933 |
|----------------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| async_tree_memoization_tg        | 291 ms                                                 | 235 ms: 1.24x faster                                  |
| coroutines                       | 19.8 ms                                                | 16.2 ms: 1.22x faster                                 |
| async_tree_eager_tg              | 48.4 ms                                                | 44.8 ms: 1.08x faster                                 |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 129 ms: 1.08x faster                                  |
| async_tree_memoization           | 270 ms                                                 | 251 ms: 1.08x faster                                  |
| async_tree_eager_memoization     | 169 ms                                                 | 157 ms: 1.08x faster                                  |
| asyncio_tcp                      | 457 ms                                                 | 430 ms: 1.06x faster                                  |
| async_tree_none_tg               | 198 ms                                                 | 190 ms: 1.04x faster                                  |
| async_tree_none                  | 212 ms                                                 | 205 ms: 1.03x faster                                  |
| async_tree_eager                 | 70.5 ms                                                | 68.4 ms: 1.03x faster                                 |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 340 ms: 1.03x faster                                  |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 367 ms: 1.02x faster                                  |
| async_generators                 | 294 ms                                                 | 292 ms: 1.01x faster                                  |
| asyncio_tcp_ssl                  | 1.26 sec                                               | 1.30 sec: 1.03x slower                                |
| async_tree_io_tg                 | 500 ms                                                 | 525 ms: 1.05x slower                                  |
| async_tree_io                    | 507 ms                                                 | 577 ms: 1.14x slower                                  |
| async_tree_eager_io              | 513 ms                                                 | 654 ms: 1.28x slower                                  |
| async_tree_eager_io_tg           | 477 ms                                                 | 689 ms: 1.45x slower                                  |
| asyncio_websockets               | 241 ms                                                 | 408 ms: 1.69x slower                                  |
| Geometric mean                   | (ref)                                                  | 1.02x slower                                          |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240814-darwin-arm64-python-main-3.14.0a0-315a933 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| float          | 56.2 ms                                                | 55.5 ms: 1.01x faster                                 |
| pidigits       | 284 ms                                                 | 283 ms: 1.00x faster                                  |
| nbody          | 73.9 ms                                                | 75.9 ms: 1.03x slower                                 |
| Geometric mean | (ref)                                                  | 1.00x slower                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240814-darwin-arm64-python-main-3.14.0a0-315a933 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.48 ms: 1.06x faster                                 |
| regex_dna      | 148 ms                                                 | 145 ms: 1.02x faster                                  |
| regex_v8       | 16.9 ms                                                | 16.8 ms: 1.01x faster                                 |
| regex_compile  | 78.5 ms                                                | 94.5 ms: 1.20x slower                                 |
| Geometric mean | (ref)                                                  | 1.03x slower                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240814-darwin-arm64-python-main-3.14.0a0-315a933 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| unpickle_pure_python | 163 us                                                 | 165 us: 1.01x slower                                  |
| json_dumps           | 6.56 ms                                                | 6.65 ms: 1.01x slower                                 |
| xml_etree_parse      | 109 ms                                                 | 111 ms: 1.02x slower                                  |
| tomli_loads          | 1.56 sec                                               | 1.59 sec: 1.02x slower                                |
| xml_etree_process    | 40.9 ms                                                | 41.9 ms: 1.02x slower                                 |
| json_loads           | 16.9 us                                                | 17.3 us: 1.03x slower                                 |
| xml_etree_iterparse  | 74.2 ms                                                | 78.1 ms: 1.05x slower                                 |
| xml_etree_generate   | 56.6 ms                                                | 60.5 ms: 1.07x slower                                 |
| Geometric mean       | (ref)                                                  | 1.03x slower                                          |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240814-darwin-arm64-python-main-3.14.0a0-315a933 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup         | 17.0 ms                                                | 16.9 ms: 1.01x faster                                 |
| python_startup_no_site | 13.7 ms                                                | 13.9 ms: 1.02x slower                                 |
| Geometric mean         | (ref)                                                  | 1.01x slower                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240814-darwin-arm64-python-main-3.14.0a0-315a933 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 16.4 ms: 1.03x faster                                 |
| genshi_xml      | 34.4 ms                                                | 35.6 ms: 1.03x slower                                 |
| django_template | 22.2 ms                                                | 24.1 ms: 1.09x slower                                 |
| mako            | 7.68 ms                                                | 9.09 ms: 1.18x slower                                 |
| Geometric mean  | (ref)                                                  | 1.07x slower                                          |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240814-darwin-arm64-python-main-3.14.0a0-315a933 |
|----------------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| deepcopy                         | 232 us                                                 | 185 us: 1.26x faster                                  |
| async_tree_memoization_tg        | 291 ms                                                 | 235 ms: 1.24x faster                                  |
| coroutines                       | 19.8 ms                                                | 16.2 ms: 1.22x faster                                 |
| deepcopy_reduce                  | 2.06 us                                                | 1.70 us: 1.21x faster                                 |
| logging_simple                   | 3.57 us                                                | 3.20 us: 1.12x faster                                 |
| logging_format                   | 3.85 us                                                | 3.50 us: 1.10x faster                                 |
| deepcopy_memo                    | 27.2 us                                                | 25.1 us: 1.09x faster                                 |
| async_tree_eager_tg              | 48.4 ms                                                | 44.8 ms: 1.08x faster                                 |
| async_tree_eager_memoization_tg  | 139 ms                                                 | 129 ms: 1.08x faster                                  |
| async_tree_memoization           | 270 ms                                                 | 251 ms: 1.08x faster                                  |
| async_tree_eager_memoization     | 169 ms                                                 | 157 ms: 1.08x faster                                  |
| asyncio_tcp                      | 457 ms                                                 | 430 ms: 1.06x faster                                  |
| regex_effbot                     | 2.63 ms                                                | 2.48 ms: 1.06x faster                                 |
| thrift                           | 466 us                                                 | 442 us: 1.05x faster                                  |
| raytrace                         | 182 ms                                                 | 173 ms: 1.05x faster                                  |
| async_tree_none_tg               | 198 ms                                                 | 190 ms: 1.04x faster                                  |
| html5lib                         | 36.6 ms                                                | 35.3 ms: 1.04x faster                                 |
| async_tree_none                  | 212 ms                                                 | 205 ms: 1.03x faster                                  |
| async_tree_eager                 | 70.5 ms                                                | 68.4 ms: 1.03x faster                                 |
| genshi_text                      | 16.9 ms                                                | 16.4 ms: 1.03x faster                                 |
| coverage                         | 46.1 ms                                                | 45.0 ms: 1.03x faster                                 |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 340 ms: 1.03x faster                                  |
| async_tree_eager_cpu_io_mixed    | 375 ms                                                 | 367 ms: 1.02x faster                                  |
| regex_dna                        | 148 ms                                                 | 145 ms: 1.02x faster                                  |
| bench_mp_pool                    | 50.9 ms                                                | 50.1 ms: 1.02x faster                                 |
| float                            | 56.2 ms                                                | 55.5 ms: 1.01x faster                                 |
| go                               | 115 ms                                                 | 114 ms: 1.01x faster                                  |
| dulwich_log                      | 28.7 ms                                                | 28.5 ms: 1.01x faster                                 |
| gc_traversal                     | 2.48 ms                                                | 2.46 ms: 1.01x faster                                 |
| async_generators                 | 294 ms                                                 | 292 ms: 1.01x faster                                  |
| regex_v8                         | 16.9 ms                                                | 16.8 ms: 1.01x faster                                 |
| python_startup                   | 17.0 ms                                                | 16.9 ms: 1.01x faster                                 |
| pidigits                         | 284 ms                                                 | 283 ms: 1.00x faster                                  |
| unpickle_pure_python             | 163 us                                                 | 165 us: 1.01x slower                                  |
| json_dumps                       | 6.56 ms                                                | 6.65 ms: 1.01x slower                                 |
| python_startup_no_site           | 13.7 ms                                                | 13.9 ms: 1.02x slower                                 |
| xml_etree_parse                  | 109 ms                                                 | 111 ms: 1.02x slower                                  |
| tomli_loads                      | 1.56 sec                                               | 1.59 sec: 1.02x slower                                |
| xml_etree_process                | 40.9 ms                                                | 41.9 ms: 1.02x slower                                 |
| asyncio_tcp_ssl                  | 1.26 sec                                               | 1.30 sec: 1.03x slower                                |
| nbody                            | 73.9 ms                                                | 75.9 ms: 1.03x slower                                 |
| bench_thread_pool                | 506 us                                                 | 519 us: 1.03x slower                                  |
| json_loads                       | 16.9 us                                                | 17.3 us: 1.03x slower                                 |
| json                             | 2.94 ms                                                | 3.03 ms: 1.03x slower                                 |
| mdp                              | 1.50 sec                                               | 1.55 sec: 1.03x slower                                |
| genshi_xml                       | 34.4 ms                                                | 35.6 ms: 1.03x slower                                 |
| pathlib                          | 22.8 ms                                                | 23.7 ms: 1.04x slower                                 |
| generators                       | 31.5 ms                                                | 32.9 ms: 1.04x slower                                 |
| pycparser                        | 706 ms                                                 | 739 ms: 1.05x slower                                  |
| 2to3                             | 178 ms                                                 | 186 ms: 1.05x slower                                  |
| telco                            | 4.80 ms                                                | 5.04 ms: 1.05x slower                                 |
| async_tree_io_tg                 | 500 ms                                                 | 525 ms: 1.05x slower                                  |
| xml_etree_iterparse              | 74.2 ms                                                | 78.1 ms: 1.05x slower                                 |
| scimark_sor                      | 106 ms                                                 | 112 ms: 1.06x slower                                  |
| scimark_lu                       | 76.5 ms                                                | 81.5 ms: 1.06x slower                                 |
| bpe_tokeniser                    | 3.24 sec                                               | 3.46 sec: 1.07x slower                                |
| xml_etree_generate               | 56.6 ms                                                | 60.5 ms: 1.07x slower                                 |
| typing_runtime_protocols         | 101 us                                                 | 108 us: 1.07x slower                                  |
| sqlglot_normalize                | 189 ms                                                 | 204 ms: 1.08x slower                                  |
| nqueens                          | 62.9 ms                                                | 67.9 ms: 1.08x slower                                 |
| django_template                  | 22.2 ms                                                | 24.1 ms: 1.09x slower                                 |
| sympy_expand                     | 246 ms                                                 | 268 ms: 1.09x slower                                  |
| pprint_safe_repr                 | 531 ms                                                 | 581 ms: 1.09x slower                                  |
| sqlglot_optimize                 | 34.9 ms                                                | 38.4 ms: 1.10x slower                                 |
| pprint_pformat                   | 1.08 sec                                               | 1.19 sec: 1.10x slower                                |
| pyflate                          | 351 ms                                                 | 387 ms: 1.10x slower                                  |
| chaos                            | 41.3 ms                                                | 45.7 ms: 1.11x slower                                 |
| sqlglot_parse                    | 856 us                                                 | 951 us: 1.11x slower                                  |
| meteor_contest                   | 73.8 ms                                                | 82.6 ms: 1.12x slower                                 |
| create_gc_cycles                 | 803 us                                                 | 902 us: 1.12x slower                                  |
| scimark_fft                      | 201 ms                                                 | 226 ms: 1.13x slower                                  |
| sqlglot_transpile                | 1.02 ms                                                | 1.16 ms: 1.13x slower                                 |
| scimark_monte_carlo              | 50.4 ms                                                | 57.2 ms: 1.14x slower                                 |
| async_tree_io                    | 507 ms                                                 | 577 ms: 1.14x slower                                  |
| sympy_str                        | 145 ms                                                 | 166 ms: 1.14x slower                                  |
| sympy_integrate                  | 11.3 ms                                                | 13.0 ms: 1.15x slower                                 |
| pylint                           | 181 ms                                                 | 208 ms: 1.15x slower                                  |
| richards_super                   | 39.1 ms                                                | 45.2 ms: 1.15x slower                                 |
| richards                         | 35.4 ms                                                | 41.0 ms: 1.16x slower                                 |
| fannkuch                         | 282 ms                                                 | 326 ms: 1.16x slower                                  |
| crypto_pyaes                     | 54.0 ms                                                | 62.6 ms: 1.16x slower                                 |
| sympy_sum                        | 75.6 ms                                                | 88.3 ms: 1.17x slower                                 |
| docutils                         | 1.44 sec                                               | 1.70 sec: 1.18x slower                                |
| mako                             | 7.68 ms                                                | 9.09 ms: 1.18x slower                                 |
| hexiom                           | 4.85 ms                                                | 5.79 ms: 1.19x slower                                 |
| regex_compile                    | 78.5 ms                                                | 94.5 ms: 1.20x slower                                 |
| spectral_norm                    | 77.3 ms                                                | 94.3 ms: 1.22x slower                                 |
| deltablue                        | 2.68 ms                                                | 3.29 ms: 1.23x slower                                 |
| async_tree_eager_io              | 513 ms                                                 | 654 ms: 1.28x slower                                  |
| logging_silent                   | 69.9 ns                                                | 90.6 ns: 1.30x slower                                 |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 3.92 ms: 1.31x slower                                 |
| comprehensions                   | 12.2 us                                                | 16.9 us: 1.39x slower                                 |
| async_tree_eager_io_tg           | 477 ms                                                 | 689 ms: 1.45x slower                                  |
| asyncio_websockets               | 241 ms                                                 | 408 ms: 1.69x slower                                  |
| Geometric mean                   | (ref)                                                  | 1.05x slower                                          |

Benchmark hidden because not significant (4): tornado_http, async_tree_cpu_io_mixed, pickle_pure_python, async_tree_cpu_io_mixed_tg
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 0.98x