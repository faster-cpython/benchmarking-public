# Results vs. 3.13.0

- fork: python
- ref: 5ec4bf86b7f4455432ae
- machine: darwin-arm64
- commit hash: 5ec4bf8
- commit date: 2025-02-22
- overall geometric mean: 1.009x slower
- HPT reliability: 56.53%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 177 ms: 1.01x faster                                                   |
| docutils       | 1.44 sec                                               | 1.49 sec: 1.03x slower                                                 |
| html5lib       | 36.7 ms                                                | 34.0 ms: 1.08x faster                                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                                           |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 214 ms: 1.35x faster                                                   |
| async_tree_eager_io              | 511 ms                                                 | 398 ms: 1.28x faster                                                   |
| async_tree_io_tg                 | 500 ms                                                 | 398 ms: 1.26x faster                                                   |
| async_tree_memoization           | 268 ms                                                 | 217 ms: 1.23x faster                                                   |
| async_tree_io                    | 508 ms                                                 | 417 ms: 1.22x faster                                                   |
| async_tree_none                  | 212 ms                                                 | 179 ms: 1.18x faster                                                   |
| async_tree_eager_io_tg           | 479 ms                                                 | 407 ms: 1.18x faster                                                   |
| async_tree_none_tg               | 198 ms                                                 | 170 ms: 1.16x faster                                                   |
| async_tree_eager_memoization     | 168 ms                                                 | 152 ms: 1.11x faster                                                   |
| async_generators                 | 294 ms                                                 | 266 ms: 1.10x faster                                                   |
| coroutines                       | 20.0 ms                                                | 18.6 ms: 1.08x faster                                                  |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 437 ms: 1.05x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 431 ms: 1.04x faster                                                   |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 367 ms: 1.02x faster                                                   |
| async_tree_eager                 | 69.9 ms                                                | 69.8 ms: 1.00x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 403 ms: 1.16x slower                                                   |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 191 ms: 1.38x slower                                                   |
| async_tree_eager_tg              | 47.4 ms                                                | 143 ms: 3.03x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.02x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 54.3 ms: 1.03x faster                                                  |
| nbody          | 73.6 ms                                                | 92.1 ms: 1.25x slower                                                  |
| Geometric mean | (ref)                                                  | 1.07x slower                                                           |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.27 ms: 1.16x faster                                                  |
| regex_dna      | 149 ms                                                 | 140 ms: 1.06x faster                                                   |
| regex_v8       | 17.0 ms                                                | 16.8 ms: 1.01x faster                                                  |
| regex_compile  | 78.3 ms                                                | 77.8 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.06x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 1.57 sec                                               | 1.45 sec: 1.08x faster                                                 |
| xml_etree_parse      | 108 ms                                                 | 104 ms: 1.04x faster                                                   |
| xml_etree_iterparse  | 74.2 ms                                                | 74.9 ms: 1.01x slower                                                  |
| xml_etree_generate   | 57.1 ms                                                | 58.2 ms: 1.02x slower                                                  |
| unpickle_pure_python | 165 us                                                 | 169 us: 1.02x slower                                                   |
| xml_etree_process    | 41.3 ms                                                | 42.7 ms: 1.03x slower                                                  |
| json_loads           | 17.0 us                                                | 17.8 us: 1.05x slower                                                  |
| pickle_pure_python   | 215 us                                                 | 230 us: 1.07x slower                                                   |
| json_dumps           | 6.47 ms                                                | 7.57 ms: 1.17x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.03x slower                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 18.8 ms                                                | 18.2 ms: 1.03x faster                                                  |
| python_startup_no_site | 13.7 ms                                                | 13.3 ms: 1.03x faster                                                  |
| Geometric mean         | (ref)                                                  | 1.03x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 16.4 ms: 1.03x faster                                                  |
| mako            | 7.75 ms                                                | 8.12 ms: 1.05x slower                                                  |
| django_template | 20.5 ms                                                | 24.2 ms: 1.18x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.05x slower                                                           |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| deepcopy                         | 236 us                                                 | 168 us: 1.40x faster                                                   |
| async_tree_memoization_tg        | 288 ms                                                 | 214 ms: 1.35x faster                                                   |
| deepcopy_memo                    | 27.4 us                                                | 21.0 us: 1.30x faster                                                  |
| async_tree_eager_io              | 511 ms                                                 | 398 ms: 1.28x faster                                                   |
| async_tree_io_tg                 | 500 ms                                                 | 398 ms: 1.26x faster                                                   |
| async_tree_memoization           | 268 ms                                                 | 217 ms: 1.23x faster                                                   |
| go                               | 117 ms                                                 | 94.8 ms: 1.23x faster                                                  |
| async_tree_io                    | 508 ms                                                 | 417 ms: 1.22x faster                                                   |
| deepcopy_reduce                  | 2.09 us                                                | 1.76 us: 1.19x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 179 ms: 1.18x faster                                                   |
| async_tree_eager_io_tg           | 479 ms                                                 | 407 ms: 1.18x faster                                                   |
| async_tree_none_tg               | 198 ms                                                 | 170 ms: 1.16x faster                                                   |
| regex_effbot                     | 2.63 ms                                                | 2.27 ms: 1.16x faster                                                  |
| scimark_sor                      | 106 ms                                                 | 92.4 ms: 1.14x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 152 ms: 1.11x faster                                                   |
| async_generators                 | 294 ms                                                 | 266 ms: 1.10x faster                                                   |
| generators                       | 31.9 ms                                                | 29.0 ms: 1.10x faster                                                  |
| tomli_loads                      | 1.57 sec                                               | 1.45 sec: 1.08x faster                                                 |
| coroutines                       | 20.0 ms                                                | 18.6 ms: 1.08x faster                                                  |
| html5lib                         | 36.7 ms                                                | 34.0 ms: 1.08x faster                                                  |
| bench_mp_pool                    | 64.7 ms                                                | 60.8 ms: 1.06x faster                                                  |
| regex_dna                        | 149 ms                                                 | 140 ms: 1.06x faster                                                   |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 437 ms: 1.05x faster                                                   |
| xml_etree_parse                  | 108 ms                                                 | 104 ms: 1.04x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 431 ms: 1.04x faster                                                   |
| k_core                           | 1.61 sec                                               | 1.55 sec: 1.04x faster                                                 |
| pprint_pformat                   | 1.10 sec                                               | 1.06 sec: 1.04x faster                                                 |
| genshi_text                      | 16.9 ms                                                | 16.4 ms: 1.03x faster                                                  |
| python_startup                   | 18.8 ms                                                | 18.2 ms: 1.03x faster                                                  |
| python_startup_no_site           | 13.7 ms                                                | 13.3 ms: 1.03x faster                                                  |
| float                            | 55.8 ms                                                | 54.3 ms: 1.03x faster                                                  |
| pprint_safe_repr                 | 541 ms                                                 | 527 ms: 1.03x faster                                                   |
| telco                            | 4.84 ms                                                | 4.74 ms: 1.02x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 367 ms: 1.02x faster                                                   |
| regex_v8                         | 17.0 ms                                                | 16.8 ms: 1.01x faster                                                  |
| scimark_fft                      | 200 ms                                                 | 197 ms: 1.01x faster                                                   |
| thrift                           | 466 us                                                 | 461 us: 1.01x faster                                                   |
| sqlite_synth                     | 1.55 us                                                | 1.54 us: 1.01x faster                                                  |
| scimark_monte_carlo              | 50.4 ms                                                | 50.0 ms: 1.01x faster                                                  |
| bpe_tokeniser                    | 3.26 sec                                               | 3.23 sec: 1.01x faster                                                 |
| 2to3                             | 179 ms                                                 | 177 ms: 1.01x faster                                                   |
| regex_compile                    | 78.3 ms                                                | 77.8 ms: 1.01x faster                                                  |
| pyflate                          | 352 ms                                                 | 351 ms: 1.00x faster                                                   |
| async_tree_eager                 | 69.9 ms                                                | 69.8 ms: 1.00x faster                                                  |
| shortest_path                    | 345 ms                                                 | 348 ms: 1.01x slower                                                   |
| xml_etree_iterparse              | 74.2 ms                                                | 74.9 ms: 1.01x slower                                                  |
| spectral_norm                    | 76.5 ms                                                | 77.8 ms: 1.02x slower                                                  |
| xml_etree_generate               | 57.1 ms                                                | 58.2 ms: 1.02x slower                                                  |
| unpickle_pure_python             | 165 us                                                 | 169 us: 1.02x slower                                                   |
| dulwich_log                      | 28.7 ms                                                | 29.4 ms: 1.02x slower                                                  |
| logging_silent                   | 71.0 ns                                                | 73.0 ns: 1.03x slower                                                  |
| typing_runtime_protocols         | 101 us                                                 | 104 us: 1.03x slower                                                   |
| pathlib                          | 23.2 ms                                                | 23.9 ms: 1.03x slower                                                  |
| xml_etree_process                | 41.3 ms                                                | 42.7 ms: 1.03x slower                                                  |
| docutils                         | 1.44 sec                                               | 1.49 sec: 1.03x slower                                                 |
| coverage                         | 46.2 ms                                                | 47.9 ms: 1.04x slower                                                  |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 3.09 ms: 1.04x slower                                                  |
| sqlglot_optimize                 | 34.7 ms                                                | 36.0 ms: 1.04x slower                                                  |
| mdp                              | 1.50 sec                                               | 1.56 sec: 1.04x slower                                                 |
| sympy_expand                     | 248 ms                                                 | 258 ms: 1.04x slower                                                   |
| logging_format                   | 3.85 us                                                | 4.01 us: 1.04x slower                                                  |
| logging_simple                   | 3.56 us                                                | 3.71 us: 1.04x slower                                                  |
| bench_thread_pool                | 503 us                                                 | 525 us: 1.04x slower                                                   |
| json_loads                       | 17.0 us                                                | 17.8 us: 1.05x slower                                                  |
| mako                             | 7.75 ms                                                | 8.12 ms: 1.05x slower                                                  |
| sqlalchemy_imperative            | 6.69 ms                                                | 7.02 ms: 1.05x slower                                                  |
| meteor_contest                   | 74.0 ms                                                | 77.6 ms: 1.05x slower                                                  |
| sqlalchemy_declarative           | 59.0 ms                                                | 62.0 ms: 1.05x slower                                                  |
| nqueens                          | 61.8 ms                                                | 65.0 ms: 1.05x slower                                                  |
| sqlglot_parse                    | 852 us                                                 | 896 us: 1.05x slower                                                   |
| sympy_str                        | 146 ms                                                 | 153 ms: 1.05x slower                                                   |
| gc_traversal                     | 2.94 ms                                                | 3.10 ms: 1.05x slower                                                  |
| sqlglot_normalize                | 188 ms                                                 | 199 ms: 1.06x slower                                                   |
| sympy_sum                        | 75.1 ms                                                | 79.4 ms: 1.06x slower                                                  |
| crypto_pyaes                     | 55.3 ms                                                | 58.5 ms: 1.06x slower                                                  |
| deltablue                        | 2.65 ms                                                | 2.80 ms: 1.06x slower                                                  |
| sqlglot_transpile                | 1.04 ms                                                | 1.11 ms: 1.07x slower                                                  |
| create_gc_cycles                 | 1.19 ms                                                | 1.27 ms: 1.07x slower                                                  |
| fannkuch                         | 279 ms                                                 | 298 ms: 1.07x slower                                                   |
| richards                         | 36.2 ms                                                | 38.6 ms: 1.07x slower                                                  |
| pickle_pure_python               | 215 us                                                 | 230 us: 1.07x slower                                                   |
| chaos                            | 41.1 ms                                                | 44.3 ms: 1.08x slower                                                  |
| hexiom                           | 4.87 ms                                                | 5.26 ms: 1.08x slower                                                  |
| sympy_integrate                  | 11.3 ms                                                | 12.3 ms: 1.08x slower                                                  |
| comprehensions                   | 12.0 us                                                | 13.0 us: 1.09x slower                                                  |
| richards_super                   | 39.2 ms                                                | 42.8 ms: 1.09x slower                                                  |
| scimark_lu                       | 75.9 ms                                                | 83.3 ms: 1.10x slower                                                  |
| many_optionals                   | 409 us                                                 | 467 us: 1.14x slower                                                   |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 403 ms: 1.16x slower                                                   |
| raytrace                         | 181 ms                                                 | 212 ms: 1.17x slower                                                   |
| json_dumps                       | 6.47 ms                                                | 7.57 ms: 1.17x slower                                                  |
| django_template                  | 20.5 ms                                                | 24.2 ms: 1.18x slower                                                  |
| nbody                            | 73.6 ms                                                | 92.1 ms: 1.25x slower                                                  |
| subparsers                       | 9.44 ms                                                | 13.0 ms: 1.38x slower                                                  |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 191 ms: 1.38x slower                                                   |
| async_tree_eager_tg              | 47.4 ms                                                | 143 ms: 3.03x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.01x slower                                                           |

Benchmark hidden because not significant (9): pylint, connected_components, dask, json, asyncio_websockets, genshi_xml, pidigits, pycparser, sphinx
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (8) of results/bm-20250222-3.14.0a5+-5ec4bf8/bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.009x slower

# HPT report

- Reliability score: 56.53% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.08x