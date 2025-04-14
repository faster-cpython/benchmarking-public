# Results vs. 3.13.0

- fork: python
- ref: bc26f95e8ff60ccca981
- machine: darwin-arm64
- commit hash: bc26f95
- commit date: 2025-03-22
- overall geometric mean: 1.019x faster
- HPT reliability: 94.35%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 203 ms: 1.14x slower                                                   |
| docutils       | 1.44 sec                                               | 1.48 sec: 1.02x slower                                                 |
| html5lib       | 36.7 ms                                                | 32.6 ms: 1.12x faster                                                  |
| Geometric mean | (ref)                                                  | 1.01x slower                                                           |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 204 ms: 1.41x faster                                                   |
| async_tree_io_tg                 | 500 ms                                                 | 383 ms: 1.31x faster                                                   |
| async_tree_memoization           | 268 ms                                                 | 205 ms: 1.30x faster                                                   |
| async_tree_eager_io              | 511 ms                                                 | 392 ms: 1.30x faster                                                   |
| async_tree_io                    | 508 ms                                                 | 397 ms: 1.28x faster                                                   |
| async_tree_none                  | 212 ms                                                 | 171 ms: 1.23x faster                                                   |
| async_tree_eager_io_tg           | 479 ms                                                 | 391 ms: 1.22x faster                                                   |
| async_tree_none_tg               | 198 ms                                                 | 164 ms: 1.21x faster                                                   |
| async_tree_eager_memoization     | 168 ms                                                 | 143 ms: 1.17x faster                                                   |
| coroutines                       | 20.0 ms                                                | 17.3 ms: 1.16x faster                                                  |
| async_generators                 | 294 ms                                                 | 264 ms: 1.11x faster                                                   |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 419 ms: 1.10x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 419 ms: 1.07x faster                                                   |
| async_tree_eager                 | 69.9 ms                                                | 65.7 ms: 1.07x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 360 ms: 1.03x faster                                                   |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 395 ms: 1.14x slower                                                   |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 180 ms: 1.30x slower                                                   |
| async_tree_eager_tg              | 47.4 ms                                                | 135 ms: 2.86x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.07x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 52.7 ms: 1.06x faster                                                  |
| pidigits       | 284 ms                                                 | 283 ms: 1.00x faster                                                   |
| nbody          | 73.6 ms                                                | 81.1 ms: 1.10x slower                                                  |
| Geometric mean | (ref)                                                  | 1.01x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.24 ms: 1.17x faster                                                  |
| regex_v8       | 17.0 ms                                                | 15.7 ms: 1.08x faster                                                  |
| regex_dna      | 149 ms                                                 | 141 ms: 1.06x faster                                                   |
| regex_compile  | 78.3 ms                                                | 74.9 ms: 1.04x faster                                                  |
| Geometric mean | (ref)                                                  | 1.09x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|---------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads         | 1.57 sec                                               | 1.40 sec: 1.12x faster                                                 |
| xml_etree_parse     | 108 ms                                                 | 103 ms: 1.04x faster                                                   |
| xml_etree_generate  | 57.1 ms                                                | 56.2 ms: 1.02x faster                                                  |
| xml_etree_process   | 41.3 ms                                                | 40.9 ms: 1.01x faster                                                  |
| xml_etree_iterparse | 74.2 ms                                                | 73.5 ms: 1.01x faster                                                  |
| pickle_pure_python  | 215 us                                                 | 221 us: 1.03x slower                                                   |
| json_loads          | 17.0 us                                                | 17.9 us: 1.05x slower                                                  |
| json_dumps          | 6.47 ms                                                | 7.48 ms: 1.16x slower                                                  |
| Geometric mean      | (ref)                                                  | 1.00x slower                                                           |

Benchmark hidden because not significant (1): unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup | 18.8 ms                                                | 17.9 ms: 1.05x faster                                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                                           |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 15.6 ms: 1.09x faster                                                  |
| genshi_xml      | 34.1 ms                                                | 32.2 ms: 1.06x faster                                                  |
| mako            | 7.75 ms                                                | 7.83 ms: 1.01x slower                                                  |
| django_template | 20.5 ms                                                | 22.8 ms: 1.11x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                           |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| deepcopy                         | 236 us                                                 | 162 us: 1.46x faster                                                   |
| async_tree_memoization_tg        | 288 ms                                                 | 204 ms: 1.41x faster                                                   |
| deepcopy_memo                    | 27.4 us                                                | 20.4 us: 1.34x faster                                                  |
| async_tree_io_tg                 | 500 ms                                                 | 383 ms: 1.31x faster                                                   |
| async_tree_memoization           | 268 ms                                                 | 205 ms: 1.30x faster                                                   |
| async_tree_eager_io              | 511 ms                                                 | 392 ms: 1.30x faster                                                   |
| async_tree_io                    | 508 ms                                                 | 397 ms: 1.28x faster                                                   |
| generators                       | 31.9 ms                                                | 25.1 ms: 1.27x faster                                                  |
| go                               | 117 ms                                                 | 92.7 ms: 1.26x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 171 ms: 1.23x faster                                                   |
| async_tree_eager_io_tg           | 479 ms                                                 | 391 ms: 1.22x faster                                                   |
| deepcopy_reduce                  | 2.09 us                                                | 1.73 us: 1.21x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 164 ms: 1.21x faster                                                   |
| scimark_sor                      | 106 ms                                                 | 87.8 ms: 1.20x faster                                                  |
| regex_effbot                     | 2.63 ms                                                | 2.24 ms: 1.17x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 143 ms: 1.17x faster                                                   |
| coroutines                       | 20.0 ms                                                | 17.3 ms: 1.16x faster                                                  |
| dulwich_log                      | 28.7 ms                                                | 25.6 ms: 1.12x faster                                                  |
| html5lib                         | 36.7 ms                                                | 32.6 ms: 1.12x faster                                                  |
| tomli_loads                      | 1.57 sec                                               | 1.40 sec: 1.12x faster                                                 |
| async_generators                 | 294 ms                                                 | 264 ms: 1.11x faster                                                   |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 419 ms: 1.10x faster                                                   |
| genshi_text                      | 16.9 ms                                                | 15.6 ms: 1.09x faster                                                  |
| regex_v8                         | 17.0 ms                                                | 15.7 ms: 1.08x faster                                                  |
| pprint_pformat                   | 1.10 sec                                               | 1.02 sec: 1.08x faster                                                 |
| pylint                           | 180 ms                                                 | 167 ms: 1.08x faster                                                   |
| scimark_monte_carlo              | 50.4 ms                                                | 47.0 ms: 1.07x faster                                                  |
| pprint_safe_repr                 | 541 ms                                                 | 506 ms: 1.07x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 419 ms: 1.07x faster                                                   |
| bench_mp_pool                    | 64.7 ms                                                | 60.7 ms: 1.07x faster                                                  |
| async_tree_eager                 | 69.9 ms                                                | 65.7 ms: 1.07x faster                                                  |
| float                            | 55.8 ms                                                | 52.7 ms: 1.06x faster                                                  |
| regex_dna                        | 149 ms                                                 | 141 ms: 1.06x faster                                                   |
| genshi_xml                       | 34.1 ms                                                | 32.2 ms: 1.06x faster                                                  |
| python_startup                   | 18.8 ms                                                | 17.9 ms: 1.05x faster                                                  |
| telco                            | 4.84 ms                                                | 4.63 ms: 1.05x faster                                                  |
| regex_compile                    | 78.3 ms                                                | 74.9 ms: 1.04x faster                                                  |
| xml_etree_parse                  | 108 ms                                                 | 103 ms: 1.04x faster                                                   |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 360 ms: 1.03x faster                                                   |
| scimark_fft                      | 200 ms                                                 | 194 ms: 1.03x faster                                                   |
| thrift                           | 466 us                                                 | 455 us: 1.02x faster                                                   |
| xml_etree_generate               | 57.1 ms                                                | 56.2 ms: 1.02x faster                                                  |
| sqlite_synth                     | 1.55 us                                                | 1.54 us: 1.01x faster                                                  |
| connected_components             | 319 ms                                                 | 316 ms: 1.01x faster                                                   |
| xml_etree_process                | 41.3 ms                                                | 40.9 ms: 1.01x faster                                                  |
| xml_etree_iterparse              | 74.2 ms                                                | 73.5 ms: 1.01x faster                                                  |
| shortest_path                    | 345 ms                                                 | 342 ms: 1.01x faster                                                   |
| logging_silent                   | 71.0 ns                                                | 70.4 ns: 1.01x faster                                                  |
| typing_runtime_protocols         | 101 us                                                 | 100.0 us: 1.01x faster                                                 |
| coverage                         | 46.2 ms                                                | 45.9 ms: 1.01x faster                                                  |
| deltablue                        | 2.65 ms                                                | 2.63 ms: 1.01x faster                                                  |
| pyflate                          | 352 ms                                                 | 350 ms: 1.01x faster                                                   |
| pidigits                         | 284 ms                                                 | 283 ms: 1.00x faster                                                   |
| bench_thread_pool                | 503 us                                                 | 506 us: 1.01x slower                                                   |
| logging_simple                   | 3.56 us                                                | 3.59 us: 1.01x slower                                                  |
| mako                             | 7.75 ms                                                | 7.83 ms: 1.01x slower                                                  |
| logging_format                   | 3.85 us                                                | 3.90 us: 1.01x slower                                                  |
| bpe_tokeniser                    | 3.26 sec                                               | 3.30 sec: 1.01x slower                                                 |
| sympy_str                        | 146 ms                                                 | 148 ms: 1.01x slower                                                   |
| mdp                              | 1.50 sec                                               | 1.52 sec: 1.02x slower                                                 |
| docutils                         | 1.44 sec                                               | 1.48 sec: 1.02x slower                                                 |
| sqlalchemy_imperative            | 6.69 ms                                                | 6.84 ms: 1.02x slower                                                  |
| hexiom                           | 4.87 ms                                                | 5.01 ms: 1.03x slower                                                  |
| sympy_integrate                  | 11.3 ms                                                | 11.6 ms: 1.03x slower                                                  |
| sympy_sum                        | 75.1 ms                                                | 77.3 ms: 1.03x slower                                                  |
| pickle_pure_python               | 215 us                                                 | 221 us: 1.03x slower                                                   |
| json                             | 3.04 ms                                                | 3.14 ms: 1.03x slower                                                  |
| richards                         | 36.2 ms                                                | 37.4 ms: 1.03x slower                                                  |
| sqlalchemy_declarative           | 59.0 ms                                                | 61.1 ms: 1.04x slower                                                  |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 3.10 ms: 1.04x slower                                                  |
| scimark_lu                       | 75.9 ms                                                | 78.9 ms: 1.04x slower                                                  |
| spectral_norm                    | 76.5 ms                                                | 79.5 ms: 1.04x slower                                                  |
| meteor_contest                   | 74.0 ms                                                | 76.9 ms: 1.04x slower                                                  |
| pathlib                          | 23.2 ms                                                | 24.1 ms: 1.04x slower                                                  |
| json_loads                       | 17.0 us                                                | 17.9 us: 1.05x slower                                                  |
| richards_super                   | 39.2 ms                                                | 41.6 ms: 1.06x slower                                                  |
| raytrace                         | 181 ms                                                 | 192 ms: 1.06x slower                                                   |
| gc_traversal                     | 2.94 ms                                                | 3.12 ms: 1.06x slower                                                  |
| chaos                            | 41.1 ms                                                | 43.8 ms: 1.07x slower                                                  |
| comprehensions                   | 12.0 us                                                | 12.9 us: 1.08x slower                                                  |
| create_gc_cycles                 | 1.19 ms                                                | 1.29 ms: 1.08x slower                                                  |
| fannkuch                         | 279 ms                                                 | 303 ms: 1.09x slower                                                   |
| crypto_pyaes                     | 55.3 ms                                                | 60.6 ms: 1.10x slower                                                  |
| nbody                            | 73.6 ms                                                | 81.1 ms: 1.10x slower                                                  |
| django_template                  | 20.5 ms                                                | 22.8 ms: 1.11x slower                                                  |
| nqueens                          | 61.8 ms                                                | 69.2 ms: 1.12x slower                                                  |
| 2to3                             | 179 ms                                                 | 203 ms: 1.14x slower                                                   |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 395 ms: 1.14x slower                                                   |
| many_optionals                   | 409 us                                                 | 471 us: 1.15x slower                                                   |
| json_dumps                       | 6.47 ms                                                | 7.48 ms: 1.16x slower                                                  |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 180 ms: 1.30x slower                                                   |
| subparsers                       | 9.44 ms                                                | 12.7 ms: 1.34x slower                                                  |
| async_tree_eager_tg              | 47.4 ms                                                | 135 ms: 2.86x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.02x faster                                                           |

Benchmark hidden because not significant (8): sphinx, k_core, pycparser, unpickle_pure_python, python_startup_no_site, dask, asyncio_websockets, sympy_expand
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250322-3.14.0a6+-bc26f95/bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.019x faster

# HPT report

- Reliability score: 94.35% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.09x