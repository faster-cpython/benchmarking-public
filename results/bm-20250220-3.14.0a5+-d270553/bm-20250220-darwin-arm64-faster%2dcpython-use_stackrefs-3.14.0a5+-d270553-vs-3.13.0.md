# Results vs. 3.13.0

- fork: faster-cpython
- ref: use_stackrefs
- machine: darwin-arm64
- commit hash: d270553
- commit date: 2025-02-20
- overall geometric mean: 1.008x faster
- HPT reliability: 50.20%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250220-darwin-arm64-faster%2dcpython-use_stackrefs-3.14.0a5+-d270553 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 200 ms: 1.12x slower                                                      |
| docutils       | 1.44 sec                                               | 1.49 sec: 1.03x slower                                                    |
| html5lib       | 36.7 ms                                                | 32.2 ms: 1.14x faster                                                     |
| Geometric mean | (ref)                                                  | 1.01x slower                                                              |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250220-darwin-arm64-faster%2dcpython-use_stackrefs-3.14.0a5+-d270553 |
|----------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 208 ms: 1.38x faster                                                      |
| async_tree_eager_io              | 511 ms                                                 | 389 ms: 1.31x faster                                                      |
| async_tree_io_tg                 | 500 ms                                                 | 388 ms: 1.29x faster                                                      |
| async_tree_memoization           | 268 ms                                                 | 211 ms: 1.27x faster                                                      |
| async_tree_io                    | 508 ms                                                 | 408 ms: 1.25x faster                                                      |
| async_tree_eager_io_tg           | 479 ms                                                 | 400 ms: 1.20x faster                                                      |
| async_tree_none                  | 212 ms                                                 | 177 ms: 1.19x faster                                                      |
| async_tree_none_tg               | 198 ms                                                 | 166 ms: 1.19x faster                                                      |
| coroutines                       | 20.0 ms                                                | 17.9 ms: 1.12x faster                                                     |
| async_tree_eager_memoization     | 168 ms                                                 | 151 ms: 1.12x faster                                                      |
| async_generators                 | 294 ms                                                 | 270 ms: 1.09x faster                                                      |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 429 ms: 1.07x faster                                                      |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 426 ms: 1.05x faster                                                      |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 367 ms: 1.02x faster                                                      |
| async_tree_eager                 | 69.9 ms                                                | 69.2 ms: 1.01x faster                                                     |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 407 ms: 1.17x slower                                                      |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 189 ms: 1.37x slower                                                      |
| async_tree_eager_tg              | 47.4 ms                                                | 144 ms: 3.04x slower                                                      |
| Geometric mean                   | (ref)                                                  | 1.04x faster                                                              |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250220-darwin-arm64-faster%2dcpython-use_stackrefs-3.14.0a5+-d270553 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 53.2 ms: 1.05x faster                                                     |
| nbody          | 73.6 ms                                                | 80.7 ms: 1.10x slower                                                     |
| Geometric mean | (ref)                                                  | 1.01x slower                                                              |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250220-darwin-arm64-faster%2dcpython-use_stackrefs-3.14.0a5+-d270553 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.30 ms: 1.15x faster                                                     |
| regex_dna      | 149 ms                                                 | 141 ms: 1.05x faster                                                      |
| regex_compile  | 78.3 ms                                                | 74.4 ms: 1.05x faster                                                     |
| regex_v8       | 17.0 ms                                                | 16.9 ms: 1.01x faster                                                     |
| Geometric mean | (ref)                                                  | 1.06x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250220-darwin-arm64-faster%2dcpython-use_stackrefs-3.14.0a5+-d270553 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 1.57 sec                                               | 1.39 sec: 1.12x faster                                                    |
| xml_etree_parse      | 108 ms                                                 | 102 ms: 1.05x faster                                                      |
| xml_etree_iterparse  | 74.2 ms                                                | 73.7 ms: 1.01x faster                                                     |
| xml_etree_generate   | 57.1 ms                                                | 57.4 ms: 1.01x slower                                                     |
| unpickle_pure_python | 165 us                                                 | 167 us: 1.01x slower                                                      |
| xml_etree_process    | 41.3 ms                                                | 41.8 ms: 1.01x slower                                                     |
| json_loads           | 17.0 us                                                | 17.8 us: 1.04x slower                                                     |
| pickle_pure_python   | 215 us                                                 | 225 us: 1.05x slower                                                      |
| json_dumps           | 6.47 ms                                                | 7.49 ms: 1.16x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250220-darwin-arm64-faster%2dcpython-use_stackrefs-3.14.0a5+-d270553 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 13.7 ms                                                | 12.3 ms: 1.12x faster                                                     |
| python_startup         | 18.8 ms                                                | 17.1 ms: 1.10x faster                                                     |
| Geometric mean         | (ref)                                                  | 1.11x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250220-darwin-arm64-faster%2dcpython-use_stackrefs-3.14.0a5+-d270553 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 15.5 ms: 1.09x faster                                                     |
| genshi_xml      | 34.1 ms                                                | 32.2 ms: 1.06x faster                                                     |
| mako            | 7.75 ms                                                | 7.97 ms: 1.03x slower                                                     |
| django_template | 20.5 ms                                                | 23.0 ms: 1.12x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.00x slower                                                              |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250220-darwin-arm64-faster%2dcpython-use_stackrefs-3.14.0a5+-d270553 |
|----------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| deepcopy                         | 236 us                                                 | 165 us: 1.43x faster                                                      |
| async_tree_memoization_tg        | 288 ms                                                 | 208 ms: 1.38x faster                                                      |
| deepcopy_memo                    | 27.4 us                                                | 20.6 us: 1.33x faster                                                     |
| async_tree_eager_io              | 511 ms                                                 | 389 ms: 1.31x faster                                                      |
| async_tree_io_tg                 | 500 ms                                                 | 388 ms: 1.29x faster                                                      |
| generators                       | 31.9 ms                                                | 25.0 ms: 1.28x faster                                                     |
| async_tree_memoization           | 268 ms                                                 | 211 ms: 1.27x faster                                                      |
| go                               | 117 ms                                                 | 92.9 ms: 1.26x faster                                                     |
| async_tree_io                    | 508 ms                                                 | 408 ms: 1.25x faster                                                      |
| deepcopy_reduce                  | 2.09 us                                                | 1.72 us: 1.22x faster                                                     |
| async_tree_eager_io_tg           | 479 ms                                                 | 400 ms: 1.20x faster                                                      |
| async_tree_none                  | 212 ms                                                 | 177 ms: 1.19x faster                                                      |
| async_tree_none_tg               | 198 ms                                                 | 166 ms: 1.19x faster                                                      |
| scimark_sor                      | 106 ms                                                 | 89.0 ms: 1.19x faster                                                     |
| regex_effbot                     | 2.63 ms                                                | 2.30 ms: 1.15x faster                                                     |
| html5lib                         | 36.7 ms                                                | 32.2 ms: 1.14x faster                                                     |
| tomli_loads                      | 1.57 sec                                               | 1.39 sec: 1.12x faster                                                    |
| coroutines                       | 20.0 ms                                                | 17.9 ms: 1.12x faster                                                     |
| python_startup_no_site           | 13.7 ms                                                | 12.3 ms: 1.12x faster                                                     |
| async_tree_eager_memoization     | 168 ms                                                 | 151 ms: 1.12x faster                                                      |
| python_startup                   | 18.8 ms                                                | 17.1 ms: 1.10x faster                                                     |
| genshi_text                      | 16.9 ms                                                | 15.5 ms: 1.09x faster                                                     |
| async_generators                 | 294 ms                                                 | 270 ms: 1.09x faster                                                      |
| bench_mp_pool                    | 64.7 ms                                                | 59.9 ms: 1.08x faster                                                     |
| pprint_pformat                   | 1.10 sec                                               | 1.02 sec: 1.08x faster                                                    |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 429 ms: 1.07x faster                                                      |
| scimark_monte_carlo              | 50.4 ms                                                | 47.2 ms: 1.07x faster                                                     |
| pprint_safe_repr                 | 541 ms                                                 | 506 ms: 1.07x faster                                                      |
| pylint                           | 180 ms                                                 | 170 ms: 1.06x faster                                                      |
| genshi_xml                       | 34.1 ms                                                | 32.2 ms: 1.06x faster                                                     |
| xml_etree_parse                  | 108 ms                                                 | 102 ms: 1.05x faster                                                      |
| regex_dna                        | 149 ms                                                 | 141 ms: 1.05x faster                                                      |
| regex_compile                    | 78.3 ms                                                | 74.4 ms: 1.05x faster                                                     |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 426 ms: 1.05x faster                                                      |
| float                            | 55.8 ms                                                | 53.2 ms: 1.05x faster                                                     |
| scimark_fft                      | 200 ms                                                 | 195 ms: 1.03x faster                                                      |
| telco                            | 4.84 ms                                                | 4.72 ms: 1.03x faster                                                     |
| thrift                           | 466 us                                                 | 459 us: 1.02x faster                                                      |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 367 ms: 1.02x faster                                                      |
| k_core                           | 1.61 sec                                               | 1.59 sec: 1.01x faster                                                    |
| async_tree_eager                 | 69.9 ms                                                | 69.2 ms: 1.01x faster                                                     |
| xml_etree_iterparse              | 74.2 ms                                                | 73.7 ms: 1.01x faster                                                     |
| logging_silent                   | 71.0 ns                                                | 70.6 ns: 1.01x faster                                                     |
| regex_v8                         | 17.0 ms                                                | 16.9 ms: 1.01x faster                                                     |
| connected_components             | 319 ms                                                 | 317 ms: 1.01x faster                                                      |
| sqlite_synth                     | 1.55 us                                                | 1.55 us: 1.00x faster                                                     |
| sqlglot_optimize                 | 34.7 ms                                                | 34.8 ms: 1.00x slower                                                     |
| xml_etree_generate               | 57.1 ms                                                | 57.4 ms: 1.01x slower                                                     |
| pyflate                          | 352 ms                                                 | 354 ms: 1.01x slower                                                      |
| logging_simple                   | 3.56 us                                                | 3.59 us: 1.01x slower                                                     |
| dulwich_log                      | 28.7 ms                                                | 29.0 ms: 1.01x slower                                                     |
| sympy_expand                     | 248 ms                                                 | 250 ms: 1.01x slower                                                      |
| sqlglot_normalize                | 188 ms                                                 | 190 ms: 1.01x slower                                                      |
| bench_thread_pool                | 503 us                                                 | 507 us: 1.01x slower                                                      |
| deltablue                        | 2.65 ms                                                | 2.67 ms: 1.01x slower                                                     |
| unpickle_pure_python             | 165 us                                                 | 167 us: 1.01x slower                                                      |
| xml_etree_process                | 41.3 ms                                                | 41.8 ms: 1.01x slower                                                     |
| json                             | 3.04 ms                                                | 3.08 ms: 1.01x slower                                                     |
| sqlglot_parse                    | 852 us                                                 | 864 us: 1.01x slower                                                      |
| logging_format                   | 3.85 us                                                | 3.91 us: 1.01x slower                                                     |
| pathlib                          | 23.2 ms                                                | 23.5 ms: 1.01x slower                                                     |
| mdp                              | 1.50 sec                                               | 1.52 sec: 1.01x slower                                                    |
| bpe_tokeniser                    | 3.26 sec                                               | 3.32 sec: 1.02x slower                                                    |
| coverage                         | 46.2 ms                                                | 47.3 ms: 1.02x slower                                                     |
| hexiom                           | 4.87 ms                                                | 4.97 ms: 1.02x slower                                                     |
| mako                             | 7.75 ms                                                | 7.97 ms: 1.03x slower                                                     |
| sympy_str                        | 146 ms                                                 | 150 ms: 1.03x slower                                                      |
| docutils                         | 1.44 sec                                               | 1.49 sec: 1.03x slower                                                    |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 3.09 ms: 1.03x slower                                                     |
| sqlalchemy_imperative            | 6.69 ms                                                | 6.94 ms: 1.04x slower                                                     |
| sympy_sum                        | 75.1 ms                                                | 78.1 ms: 1.04x slower                                                     |
| richards                         | 36.2 ms                                                | 37.7 ms: 1.04x slower                                                     |
| json_loads                       | 17.0 us                                                | 17.8 us: 1.04x slower                                                     |
| pickle_pure_python               | 215 us                                                 | 225 us: 1.05x slower                                                      |
| sqlalchemy_declarative           | 59.0 ms                                                | 61.8 ms: 1.05x slower                                                     |
| meteor_contest                   | 74.0 ms                                                | 77.5 ms: 1.05x slower                                                     |
| spectral_norm                    | 76.5 ms                                                | 80.2 ms: 1.05x slower                                                     |
| gc_traversal                     | 2.94 ms                                                | 3.11 ms: 1.06x slower                                                     |
| scimark_lu                       | 75.9 ms                                                | 81.1 ms: 1.07x slower                                                     |
| raytrace                         | 181 ms                                                 | 194 ms: 1.07x slower                                                      |
| sympy_integrate                  | 11.3 ms                                                | 12.1 ms: 1.07x slower                                                     |
| chaos                            | 41.1 ms                                                | 44.2 ms: 1.08x slower                                                     |
| create_gc_cycles                 | 1.19 ms                                                | 1.29 ms: 1.08x slower                                                     |
| richards_super                   | 39.2 ms                                                | 42.5 ms: 1.08x slower                                                     |
| comprehensions                   | 12.0 us                                                | 13.0 us: 1.09x slower                                                     |
| fannkuch                         | 279 ms                                                 | 306 ms: 1.10x slower                                                      |
| nbody                            | 73.6 ms                                                | 80.7 ms: 1.10x slower                                                     |
| crypto_pyaes                     | 55.3 ms                                                | 61.7 ms: 1.12x slower                                                     |
| 2to3                             | 179 ms                                                 | 200 ms: 1.12x slower                                                      |
| django_template                  | 20.5 ms                                                | 23.0 ms: 1.12x slower                                                     |
| nqueens                          | 61.8 ms                                                | 70.1 ms: 1.13x slower                                                     |
| many_optionals                   | 409 us                                                 | 468 us: 1.14x slower                                                      |
| json_dumps                       | 6.47 ms                                                | 7.49 ms: 1.16x slower                                                     |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 407 ms: 1.17x slower                                                      |
| subparsers                       | 9.44 ms                                                | 12.8 ms: 1.35x slower                                                     |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 189 ms: 1.37x slower                                                      |
| async_tree_eager_tg              | 47.4 ms                                                | 144 ms: 3.04x slower                                                      |
| Geometric mean                   | (ref)                                                  | 1.01x faster                                                              |

Benchmark hidden because not significant (8): asyncio_websockets, pycparser, pidigits, dask, typing_runtime_protocols, shortest_path, sqlglot_transpile, sphinx
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.008x faster

# HPT report

- Reliability score: 50.20% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.08x