# Results vs. 3.13.0

- fork: python
- ref: 5ec4bf86b7f4455432ae
- machine: darwin-arm64
- commit hash: 5ec4bf8
- commit date: 2025-02-22
- overall geometric mean: 1.038x slower
- HPT reliability: 99.83%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.21x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 195 ms: 1.09x slower                                                   |
| docutils       | 1.44 sec                                               | 1.45 sec: 1.01x slower                                                 |
| html5lib       | 36.7 ms                                                | 34.6 ms: 1.06x faster                                                  |
| sphinx         | 602 ms                                                 | 622 ms: 1.03x slower                                                   |
| Geometric mean | (ref)                                                  | 1.02x slower                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 187 ms: 1.54x faster                                                   |
| async_tree_io_tg                 | 500 ms                                                 | 328 ms: 1.53x faster                                                   |
| async_tree_eager_io              | 511 ms                                                 | 338 ms: 1.51x faster                                                   |
| async_tree_eager_io_tg           | 479 ms                                                 | 319 ms: 1.50x faster                                                   |
| async_tree_io                    | 508 ms                                                 | 352 ms: 1.44x faster                                                   |
| async_tree_none_tg               | 198 ms                                                 | 146 ms: 1.36x faster                                                   |
| async_tree_memoization           | 268 ms                                                 | 210 ms: 1.27x faster                                                   |
| async_tree_none                  | 212 ms                                                 | 170 ms: 1.24x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 394 ms: 1.14x faster                                                   |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 418 ms: 1.10x faster                                                   |
| async_generators                 | 294 ms                                                 | 274 ms: 1.07x faster                                                   |
| async_tree_eager_memoization     | 168 ms                                                 | 157 ms: 1.07x faster                                                   |
| coroutines                       | 20.0 ms                                                | 18.7 ms: 1.07x faster                                                  |
| asyncio_websockets               | 242 ms                                                 | 238 ms: 1.02x faster                                                   |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 374 ms: 1.00x slower                                                   |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 377 ms: 1.08x slower                                                   |
| async_tree_eager                 | 69.9 ms                                                | 85.3 ms: 1.22x slower                                                  |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 171 ms: 1.24x slower                                                   |
| async_tree_eager_tg              | 47.4 ms                                                | 127 ms: 2.69x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.10x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 55.0 ms: 1.02x faster                                                  |
| pidigits       | 284 ms                                                 | 281 ms: 1.01x faster                                                   |
| nbody          | 73.6 ms                                                | 101 ms: 1.37x slower                                                   |
| Geometric mean | (ref)                                                  | 1.10x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.11 ms: 1.25x faster                                                  |
| regex_dna      | 149 ms                                                 | 137 ms: 1.09x faster                                                   |
| regex_v8       | 17.0 ms                                                | 15.7 ms: 1.08x faster                                                  |
| regex_compile  | 78.3 ms                                                | 86.8 ms: 1.11x slower                                                  |
| Geometric mean | (ref)                                                  | 1.07x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_iterparse  | 74.2 ms                                                | 66.3 ms: 1.12x faster                                                  |
| xml_etree_parse      | 108 ms                                                 | 96.8 ms: 1.11x faster                                                  |
| tomli_loads          | 1.57 sec                                               | 1.61 sec: 1.03x slower                                                 |
| xml_etree_generate   | 57.1 ms                                                | 59.7 ms: 1.05x slower                                                  |
| xml_etree_process    | 41.3 ms                                                | 44.6 ms: 1.08x slower                                                  |
| json_loads           | 17.0 us                                                | 18.6 us: 1.09x slower                                                  |
| unpickle_pure_python | 165 us                                                 | 182 us: 1.10x slower                                                   |
| pickle_pure_python   | 215 us                                                 | 250 us: 1.16x slower                                                   |
| json_dumps           | 6.47 ms                                                | 7.97 ms: 1.23x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.05x slower                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 18.8 ms                                                | 19.7 ms: 1.05x slower                                                  |
| python_startup_no_site | 13.7 ms                                                | 15.1 ms: 1.10x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 18.2 ms: 1.07x slower                                                  |
| genshi_xml      | 34.1 ms                                                | 37.0 ms: 1.09x slower                                                  |
| django_template | 20.5 ms                                                | 26.2 ms: 1.28x slower                                                  |
| mako            | 7.75 ms                                                | 10.9 ms: 1.41x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.20x slower                                                           |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| gc_traversal                     | 2.94 ms                                                | 1.39 ms: 2.11x faster                                                  |
| create_gc_cycles                 | 1.19 ms                                                | 736 us: 1.62x faster                                                   |
| async_tree_memoization_tg        | 288 ms                                                 | 187 ms: 1.54x faster                                                   |
| async_tree_io_tg                 | 500 ms                                                 | 328 ms: 1.53x faster                                                   |
| async_tree_eager_io              | 511 ms                                                 | 338 ms: 1.51x faster                                                   |
| async_tree_eager_io_tg           | 479 ms                                                 | 319 ms: 1.50x faster                                                   |
| async_tree_io                    | 508 ms                                                 | 352 ms: 1.44x faster                                                   |
| async_tree_none_tg               | 198 ms                                                 | 146 ms: 1.36x faster                                                   |
| deepcopy                         | 236 us                                                 | 183 us: 1.29x faster                                                   |
| async_tree_memoization           | 268 ms                                                 | 210 ms: 1.27x faster                                                   |
| regex_effbot                     | 2.63 ms                                                | 2.11 ms: 1.25x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 170 ms: 1.24x faster                                                   |
| sqlite_synth                     | 1.55 us                                                | 1.30 us: 1.20x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 394 ms: 1.14x faster                                                   |
| xml_etree_iterparse              | 74.2 ms                                                | 66.3 ms: 1.12x faster                                                  |
| xml_etree_parse                  | 108 ms                                                 | 96.8 ms: 1.11x faster                                                  |
| deepcopy_memo                    | 27.4 us                                                | 24.6 us: 1.11x faster                                                  |
| go                               | 117 ms                                                 | 106 ms: 1.10x faster                                                   |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 418 ms: 1.10x faster                                                   |
| deepcopy_reduce                  | 2.09 us                                                | 1.93 us: 1.09x faster                                                  |
| regex_dna                        | 149 ms                                                 | 137 ms: 1.09x faster                                                   |
| regex_v8                         | 17.0 ms                                                | 15.7 ms: 1.08x faster                                                  |
| async_generators                 | 294 ms                                                 | 274 ms: 1.07x faster                                                   |
| async_tree_eager_memoization     | 168 ms                                                 | 157 ms: 1.07x faster                                                   |
| coroutines                       | 20.0 ms                                                | 18.7 ms: 1.07x faster                                                  |
| html5lib                         | 36.7 ms                                                | 34.6 ms: 1.06x faster                                                  |
| generators                       | 31.9 ms                                                | 30.5 ms: 1.05x faster                                                  |
| pycparser                        | 701 ms                                                 | 687 ms: 1.02x faster                                                   |
| scimark_sor                      | 106 ms                                                 | 104 ms: 1.02x faster                                                   |
| asyncio_websockets               | 242 ms                                                 | 238 ms: 1.02x faster                                                   |
| float                            | 55.8 ms                                                | 55.0 ms: 1.02x faster                                                  |
| pidigits                         | 284 ms                                                 | 281 ms: 1.01x faster                                                   |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 374 ms: 1.00x slower                                                   |
| docutils                         | 1.44 sec                                               | 1.45 sec: 1.01x slower                                                 |
| pathlib                          | 23.2 ms                                                | 23.6 ms: 1.02x slower                                                  |
| bench_mp_pool                    | 64.7 ms                                                | 65.9 ms: 1.02x slower                                                  |
| bpe_tokeniser                    | 3.26 sec                                               | 3.34 sec: 1.02x slower                                                 |
| tomli_loads                      | 1.57 sec                                               | 1.61 sec: 1.03x slower                                                 |
| json                             | 3.04 ms                                                | 3.12 ms: 1.03x slower                                                  |
| sphinx                           | 602 ms                                                 | 622 ms: 1.03x slower                                                   |
| xml_etree_generate               | 57.1 ms                                                | 59.7 ms: 1.05x slower                                                  |
| k_core                           | 1.61 sec                                               | 1.69 sec: 1.05x slower                                                 |
| python_startup                   | 18.8 ms                                                | 19.7 ms: 1.05x slower                                                  |
| pyflate                          | 352 ms                                                 | 370 ms: 1.05x slower                                                   |
| shortest_path                    | 345 ms                                                 | 366 ms: 1.06x slower                                                   |
| telco                            | 4.84 ms                                                | 5.16 ms: 1.07x slower                                                  |
| genshi_text                      | 16.9 ms                                                | 18.2 ms: 1.07x slower                                                  |
| sqlglot_optimize                 | 34.7 ms                                                | 37.3 ms: 1.08x slower                                                  |
| xml_etree_process                | 41.3 ms                                                | 44.6 ms: 1.08x slower                                                  |
| sqlglot_normalize                | 188 ms                                                 | 203 ms: 1.08x slower                                                   |
| thrift                           | 466 us                                                 | 504 us: 1.08x slower                                                   |
| dulwich_log                      | 28.7 ms                                                | 31.1 ms: 1.08x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 377 ms: 1.08x slower                                                   |
| genshi_xml                       | 34.1 ms                                                | 37.0 ms: 1.09x slower                                                  |
| 2to3                             | 179 ms                                                 | 195 ms: 1.09x slower                                                   |
| connected_components             | 319 ms                                                 | 348 ms: 1.09x slower                                                   |
| json_loads                       | 17.0 us                                                | 18.6 us: 1.09x slower                                                  |
| mdp                              | 1.50 sec                                               | 1.64 sec: 1.10x slower                                                 |
| python_startup_no_site           | 13.7 ms                                                | 15.1 ms: 1.10x slower                                                  |
| unpickle_pure_python             | 165 us                                                 | 182 us: 1.10x slower                                                   |
| pprint_pformat                   | 1.10 sec                                               | 1.22 sec: 1.11x slower                                                 |
| regex_compile                    | 78.3 ms                                                | 86.8 ms: 1.11x slower                                                  |
| pprint_safe_repr                 | 541 ms                                                 | 601 ms: 1.11x slower                                                   |
| nqueens                          | 61.8 ms                                                | 69.0 ms: 1.12x slower                                                  |
| sympy_expand                     | 248 ms                                                 | 280 ms: 1.13x slower                                                   |
| sympy_sum                        | 75.1 ms                                                | 85.2 ms: 1.13x slower                                                  |
| logging_simple                   | 3.56 us                                                | 4.05 us: 1.14x slower                                                  |
| deltablue                        | 2.65 ms                                                | 3.03 ms: 1.14x slower                                                  |
| sympy_str                        | 146 ms                                                 | 167 ms: 1.15x slower                                                   |
| sqlglot_transpile                | 1.04 ms                                                | 1.20 ms: 1.15x slower                                                  |
| meteor_contest                   | 74.0 ms                                                | 85.3 ms: 1.15x slower                                                  |
| logging_format                   | 3.85 us                                                | 4.45 us: 1.16x slower                                                  |
| sqlalchemy_imperative            | 6.69 ms                                                | 7.74 ms: 1.16x slower                                                  |
| fannkuch                         | 279 ms                                                 | 323 ms: 1.16x slower                                                   |
| pickle_pure_python               | 215 us                                                 | 250 us: 1.16x slower                                                   |
| scimark_fft                      | 200 ms                                                 | 233 ms: 1.17x slower                                                   |
| typing_runtime_protocols         | 101 us                                                 | 117 us: 1.17x slower                                                   |
| scimark_monte_carlo              | 50.4 ms                                                | 58.9 ms: 1.17x slower                                                  |
| coverage                         | 46.2 ms                                                | 54.0 ms: 1.17x slower                                                  |
| sympy_integrate                  | 11.3 ms                                                | 13.2 ms: 1.17x slower                                                  |
| richards                         | 36.2 ms                                                | 42.3 ms: 1.17x slower                                                  |
| many_optionals                   | 409 us                                                 | 480 us: 1.17x slower                                                   |
| sqlalchemy_declarative           | 59.0 ms                                                | 69.3 ms: 1.17x slower                                                  |
| spectral_norm                    | 76.5 ms                                                | 90.7 ms: 1.19x slower                                                  |
| hexiom                           | 4.87 ms                                                | 5.78 ms: 1.19x slower                                                  |
| sqlglot_parse                    | 852 us                                                 | 1.02 ms: 1.19x slower                                                  |
| chaos                            | 41.1 ms                                                | 49.3 ms: 1.20x slower                                                  |
| comprehensions                   | 12.0 us                                                | 14.4 us: 1.20x slower                                                  |
| crypto_pyaes                     | 55.3 ms                                                | 67.2 ms: 1.21x slower                                                  |
| richards_super                   | 39.2 ms                                                | 47.7 ms: 1.22x slower                                                  |
| async_tree_eager                 | 69.9 ms                                                | 85.3 ms: 1.22x slower                                                  |
| logging_silent                   | 71.0 ns                                                | 87.3 ns: 1.23x slower                                                  |
| json_dumps                       | 6.47 ms                                                | 7.97 ms: 1.23x slower                                                  |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 171 ms: 1.24x slower                                                   |
| django_template                  | 20.5 ms                                                | 26.2 ms: 1.28x slower                                                  |
| scimark_lu                       | 75.9 ms                                                | 97.2 ms: 1.28x slower                                                  |
| raytrace                         | 181 ms                                                 | 237 ms: 1.31x slower                                                   |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 3.93 ms: 1.32x slower                                                  |
| nbody                            | 73.6 ms                                                | 101 ms: 1.37x slower                                                   |
| mako                             | 7.75 ms                                                | 10.9 ms: 1.41x slower                                                  |
| subparsers                       | 9.44 ms                                                | 13.5 ms: 1.43x slower                                                  |
| bench_thread_pool                | 503 us                                                 | 815 us: 1.62x slower                                                   |
| async_tree_eager_tg              | 47.4 ms                                                | 127 ms: 2.69x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.04x slower                                                           |

Benchmark hidden because not significant (1): pylint
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (8) of results/bm-20250222-3.14.0a5+-5ec4bf8-NOGIL/bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.038x slower

# HPT report

- Reliability score: 99.83% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.21x