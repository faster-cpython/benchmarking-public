# Results vs. 3.13.0

- fork: faster-cpython
- ref: virtual_iterators
- machine: darwin-arm64
- commit hash: a4b740d
- commit date: 2025-04-16
- overall geometric mean: 1.033x slower
- HPT reliability: 93.30%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250416-darwin-arm64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 218 ms: 1.22x slower                                                          |
| docutils       | 1.44 sec                                               | 1.59 sec: 1.10x slower                                                        |
| sphinx         | 602 ms                                                 | 620 ms: 1.03x slower                                                          |
| Geometric mean | (ref)                                                  | 1.08x slower                                                                  |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250416-darwin-arm64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|----------------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 214 ms: 1.34x faster                                                          |
| async_tree_eager_io              | 511 ms                                                 | 405 ms: 1.26x faster                                                          |
| async_tree_io_tg                 | 500 ms                                                 | 406 ms: 1.23x faster                                                          |
| async_tree_memoization           | 268 ms                                                 | 221 ms: 1.21x faster                                                          |
| async_tree_io                    | 508 ms                                                 | 424 ms: 1.20x faster                                                          |
| async_tree_eager_io_tg           | 479 ms                                                 | 413 ms: 1.16x faster                                                          |
| async_tree_none                  | 212 ms                                                 | 185 ms: 1.14x faster                                                          |
| async_tree_none_tg               | 198 ms                                                 | 174 ms: 1.14x faster                                                          |
| async_tree_eager_memoization     | 168 ms                                                 | 152 ms: 1.11x faster                                                          |
| async_generators                 | 294 ms                                                 | 272 ms: 1.08x faster                                                          |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 431 ms: 1.07x faster                                                          |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 424 ms: 1.06x faster                                                          |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 370 ms: 1.01x faster                                                          |
| asyncio_websockets               | 242 ms                                                 | 245 ms: 1.01x slower                                                          |
| coroutines                       | 20.0 ms                                                | 20.3 ms: 1.01x slower                                                         |
| async_tree_eager                 | 69.9 ms                                                | 75.2 ms: 1.08x slower                                                         |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 404 ms: 1.16x slower                                                          |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 189 ms: 1.37x slower                                                          |
| async_tree_eager_tg              | 47.4 ms                                                | 147 ms: 3.10x slower                                                          |
| Geometric mean                   | (ref)                                                  | 1.01x faster                                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250416-darwin-arm64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 56.4 ms: 1.01x slower                                                         |
| nbody          | 73.6 ms                                                | 87.0 ms: 1.18x slower                                                         |
| Geometric mean | (ref)                                                  | 1.06x slower                                                                  |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250416-darwin-arm64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.30 ms: 1.15x faster                                                         |
| regex_v8       | 17.0 ms                                                | 15.8 ms: 1.07x faster                                                         |
| regex_dna      | 149 ms                                                 | 141 ms: 1.06x faster                                                          |
| regex_compile  | 78.3 ms                                                | 82.8 ms: 1.06x slower                                                         |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250416-darwin-arm64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| tomli_loads          | 1.57 sec                                               | 1.48 sec: 1.06x faster                                                        |
| xml_etree_parse      | 108 ms                                                 | 107 ms: 1.01x faster                                                          |
| xml_etree_iterparse  | 74.2 ms                                                | 76.3 ms: 1.03x slower                                                         |
| json_loads           | 17.0 us                                                | 17.8 us: 1.04x slower                                                         |
| xml_etree_generate   | 57.1 ms                                                | 62.2 ms: 1.09x slower                                                         |
| unpickle_pure_python | 165 us                                                 | 181 us: 1.10x slower                                                          |
| xml_etree_process    | 41.3 ms                                                | 46.0 ms: 1.11x slower                                                         |
| pickle_pure_python   | 215 us                                                 | 247 us: 1.15x slower                                                          |
| json_dumps           | 6.47 ms                                                | 7.78 ms: 1.20x slower                                                         |
| Geometric mean       | (ref)                                                  | 1.07x slower                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250416-darwin-arm64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup         | 18.8 ms                                                | 19.0 ms: 1.01x slower                                                         |
| python_startup_no_site | 13.7 ms                                                | 14.7 ms: 1.07x slower                                                         |
| Geometric mean         | (ref)                                                  | 1.04x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250416-darwin-arm64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| genshi_xml      | 34.1 ms                                                | 37.4 ms: 1.10x slower                                                         |
| mako            | 7.75 ms                                                | 8.88 ms: 1.15x slower                                                         |
| genshi_text     | 16.9 ms                                                | 19.4 ms: 1.15x slower                                                         |
| django_template | 20.5 ms                                                | 26.9 ms: 1.31x slower                                                         |
| Geometric mean  | (ref)                                                  | 1.17x slower                                                                  |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250416-darwin-arm64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|----------------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mdp                              | 1.50 sec                                               | 849 ms: 1.77x faster                                                          |
| async_tree_memoization_tg        | 288 ms                                                 | 214 ms: 1.34x faster                                                          |
| deepcopy                         | 236 us                                                 | 177 us: 1.33x faster                                                          |
| async_tree_eager_io              | 511 ms                                                 | 405 ms: 1.26x faster                                                          |
| async_tree_io_tg                 | 500 ms                                                 | 406 ms: 1.23x faster                                                          |
| async_tree_memoization           | 268 ms                                                 | 221 ms: 1.21x faster                                                          |
| async_tree_io                    | 508 ms                                                 | 424 ms: 1.20x faster                                                          |
| deepcopy_memo                    | 27.4 us                                                | 23.1 us: 1.19x faster                                                         |
| async_tree_eager_io_tg           | 479 ms                                                 | 413 ms: 1.16x faster                                                          |
| regex_effbot                     | 2.63 ms                                                | 2.30 ms: 1.15x faster                                                         |
| async_tree_none                  | 212 ms                                                 | 185 ms: 1.14x faster                                                          |
| async_tree_none_tg               | 198 ms                                                 | 174 ms: 1.14x faster                                                          |
| scimark_sor                      | 106 ms                                                 | 93.7 ms: 1.13x faster                                                         |
| async_tree_eager_memoization     | 168 ms                                                 | 152 ms: 1.11x faster                                                          |
| deepcopy_reduce                  | 2.09 us                                                | 1.90 us: 1.10x faster                                                         |
| go                               | 117 ms                                                 | 106 ms: 1.10x faster                                                          |
| async_generators                 | 294 ms                                                 | 272 ms: 1.08x faster                                                          |
| regex_v8                         | 17.0 ms                                                | 15.8 ms: 1.07x faster                                                         |
| dulwich_log                      | 28.7 ms                                                | 26.8 ms: 1.07x faster                                                         |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 431 ms: 1.07x faster                                                          |
| regex_dna                        | 149 ms                                                 | 141 ms: 1.06x faster                                                          |
| tomli_loads                      | 1.57 sec                                               | 1.48 sec: 1.06x faster                                                        |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 424 ms: 1.06x faster                                                          |
| k_core                           | 1.61 sec                                               | 1.54 sec: 1.05x faster                                                        |
| pyflate                          | 352 ms                                                 | 338 ms: 1.04x faster                                                          |
| shortest_path                    | 345 ms                                                 | 341 ms: 1.01x faster                                                          |
| spectral_norm                    | 76.5 ms                                                | 75.6 ms: 1.01x faster                                                         |
| xml_etree_parse                  | 108 ms                                                 | 107 ms: 1.01x faster                                                          |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 370 ms: 1.01x faster                                                          |
| generators                       | 31.9 ms                                                | 31.8 ms: 1.01x faster                                                         |
| connected_components             | 319 ms                                                 | 317 ms: 1.00x faster                                                          |
| asyncio_websockets               | 242 ms                                                 | 245 ms: 1.01x slower                                                          |
| python_startup                   | 18.8 ms                                                | 19.0 ms: 1.01x slower                                                         |
| float                            | 55.8 ms                                                | 56.4 ms: 1.01x slower                                                         |
| telco                            | 4.84 ms                                                | 4.90 ms: 1.01x slower                                                         |
| coroutines                       | 20.0 ms                                                | 20.3 ms: 1.01x slower                                                         |
| json                             | 3.04 ms                                                | 3.09 ms: 1.02x slower                                                         |
| bpe_tokeniser                    | 3.26 sec                                               | 3.32 sec: 1.02x slower                                                        |
| sqlite_synth                     | 1.55 us                                                | 1.59 us: 1.02x slower                                                         |
| bench_mp_pool                    | 64.7 ms                                                | 66.3 ms: 1.02x slower                                                         |
| xml_etree_iterparse              | 74.2 ms                                                | 76.3 ms: 1.03x slower                                                         |
| meteor_contest                   | 74.0 ms                                                | 76.1 ms: 1.03x slower                                                         |
| sphinx                           | 602 ms                                                 | 620 ms: 1.03x slower                                                          |
| typing_runtime_protocols         | 101 us                                                 | 105 us: 1.04x slower                                                          |
| json_loads                       | 17.0 us                                                | 17.8 us: 1.04x slower                                                         |
| pathlib                          | 23.2 ms                                                | 24.3 ms: 1.05x slower                                                         |
| hexiom                           | 4.87 ms                                                | 5.12 ms: 1.05x slower                                                         |
| coverage                         | 46.2 ms                                                | 48.8 ms: 1.06x slower                                                         |
| scimark_fft                      | 200 ms                                                 | 211 ms: 1.06x slower                                                          |
| deltablue                        | 2.65 ms                                                | 2.80 ms: 1.06x slower                                                         |
| regex_compile                    | 78.3 ms                                                | 82.8 ms: 1.06x slower                                                         |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 3.18 ms: 1.07x slower                                                         |
| gc_traversal                     | 2.94 ms                                                | 3.13 ms: 1.07x slower                                                         |
| pprint_pformat                   | 1.10 sec                                               | 1.17 sec: 1.07x slower                                                        |
| python_startup_no_site           | 13.7 ms                                                | 14.7 ms: 1.07x slower                                                         |
| pprint_safe_repr                 | 541 ms                                                 | 578 ms: 1.07x slower                                                          |
| pycparser                        | 701 ms                                                 | 750 ms: 1.07x slower                                                          |
| async_tree_eager                 | 69.9 ms                                                | 75.2 ms: 1.08x slower                                                         |
| bench_thread_pool                | 503 us                                                 | 542 us: 1.08x slower                                                          |
| richards                         | 36.2 ms                                                | 39.0 ms: 1.08x slower                                                         |
| create_gc_cycles                 | 1.19 ms                                                | 1.29 ms: 1.09x slower                                                         |
| scimark_monte_carlo              | 50.4 ms                                                | 54.9 ms: 1.09x slower                                                         |
| xml_etree_generate               | 57.1 ms                                                | 62.2 ms: 1.09x slower                                                         |
| sqlalchemy_declarative           | 59.0 ms                                                | 64.4 ms: 1.09x slower                                                         |
| comprehensions                   | 12.0 us                                                | 13.1 us: 1.09x slower                                                         |
| unpickle_pure_python             | 165 us                                                 | 181 us: 1.10x slower                                                          |
| logging_silent                   | 71.0 ns                                                | 78.0 ns: 1.10x slower                                                         |
| genshi_xml                       | 34.1 ms                                                | 37.4 ms: 1.10x slower                                                         |
| docutils                         | 1.44 sec                                               | 1.59 sec: 1.10x slower                                                        |
| crypto_pyaes                     | 55.3 ms                                                | 61.3 ms: 1.11x slower                                                         |
| xml_etree_process                | 41.3 ms                                                | 46.0 ms: 1.11x slower                                                         |
| logging_format                   | 3.85 us                                                | 4.29 us: 1.11x slower                                                         |
| scimark_lu                       | 75.9 ms                                                | 84.6 ms: 1.11x slower                                                         |
| sqlalchemy_imperative            | 6.69 ms                                                | 7.48 ms: 1.12x slower                                                         |
| raytrace                         | 181 ms                                                 | 202 ms: 1.12x slower                                                          |
| logging_simple                   | 3.56 us                                                | 3.98 us: 1.12x slower                                                         |
| fannkuch                         | 279 ms                                                 | 315 ms: 1.13x slower                                                          |
| mako                             | 7.75 ms                                                | 8.88 ms: 1.15x slower                                                         |
| genshi_text                      | 16.9 ms                                                | 19.4 ms: 1.15x slower                                                         |
| pickle_pure_python               | 215 us                                                 | 247 us: 1.15x slower                                                          |
| richards_super                   | 39.2 ms                                                | 45.4 ms: 1.16x slower                                                         |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 404 ms: 1.16x slower                                                          |
| many_optionals                   | 409 us                                                 | 478 us: 1.17x slower                                                          |
| nqueens                          | 61.8 ms                                                | 73.0 ms: 1.18x slower                                                         |
| nbody                            | 73.6 ms                                                | 87.0 ms: 1.18x slower                                                         |
| chaos                            | 41.1 ms                                                | 49.2 ms: 1.20x slower                                                         |
| json_dumps                       | 6.47 ms                                                | 7.78 ms: 1.20x slower                                                         |
| 2to3                             | 179 ms                                                 | 218 ms: 1.22x slower                                                          |
| django_template                  | 20.5 ms                                                | 26.9 ms: 1.31x slower                                                         |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 189 ms: 1.37x slower                                                          |
| subparsers                       | 9.44 ms                                                | 13.6 ms: 1.44x slower                                                         |
| async_tree_eager_tg              | 47.4 ms                                                | 147 ms: 3.10x slower                                                          |
| Geometric mean                   | (ref)                                                  | 1.03x slower                                                                  |

Benchmark hidden because not significant (2): html5lib, pidigits
Ignored benchmarks (16) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, dask, djangocms, gevent_hub, gunicorn, pylint, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift, tornado_http
Ignored benchmarks (4) of results/bm-20250416-3.14.0a7+-a4b740d/bm-20250416-darwin-arm64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.033x slower

# HPT report

- Reliability score: 93.30% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.09x