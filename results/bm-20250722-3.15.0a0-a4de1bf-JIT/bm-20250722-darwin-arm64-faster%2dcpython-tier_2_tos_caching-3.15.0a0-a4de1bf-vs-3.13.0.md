# Results vs. 3.13.0

- fork: faster-cpython
- ref: tier_2_tos_caching
- machine: darwin-arm64
- commit hash: a4de1bf
- commit date: 2025-07-22
- overall geometric mean: 1.084x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250722-darwin-arm64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 167 ms: 1.07x faster                                                          |
| docutils       | 1.44 sec                                               | 1.45 sec: 1.01x slower                                                        |
| html5lib       | 36.7 ms                                                | 32.9 ms: 1.11x faster                                                         |
| sphinx         | 602 ms                                                 | 574 ms: 1.05x faster                                                          |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250722-darwin-arm64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|----------------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 191 ms: 1.51x faster                                                          |
| async_tree_eager_io              | 511 ms                                                 | 359 ms: 1.42x faster                                                          |
| async_tree_memoization           | 268 ms                                                 | 193 ms: 1.39x faster                                                          |
| async_tree_io_tg                 | 500 ms                                                 | 367 ms: 1.36x faster                                                          |
| async_tree_io                    | 508 ms                                                 | 380 ms: 1.34x faster                                                          |
| async_tree_eager_io_tg           | 479 ms                                                 | 368 ms: 1.30x faster                                                          |
| async_tree_none                  | 212 ms                                                 | 163 ms: 1.30x faster                                                          |
| async_tree_none_tg               | 198 ms                                                 | 156 ms: 1.27x faster                                                          |
| coroutines                       | 20.0 ms                                                | 16.6 ms: 1.21x faster                                                         |
| async_tree_eager_memoization     | 168 ms                                                 | 140 ms: 1.20x faster                                                          |
| async_tree_eager                 | 69.9 ms                                                | 63.2 ms: 1.11x faster                                                         |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 417 ms: 1.10x faster                                                          |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 412 ms: 1.09x faster                                                          |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 359 ms: 1.04x faster                                                          |
| async_generators                 | 294 ms                                                 | 286 ms: 1.03x faster                                                          |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 390 ms: 1.12x slower                                                          |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 167 ms: 1.21x slower                                                          |
| async_tree_eager_tg              | 47.4 ms                                                | 128 ms: 2.71x slower                                                          |
| Geometric mean                   | (ref)                                                  | 1.10x faster                                                                  |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250722-darwin-arm64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| nbody          | 73.6 ms                                                | 60.3 ms: 1.22x faster                                                         |
| float          | 55.8 ms                                                | 51.5 ms: 1.08x faster                                                         |
| pidigits       | 284 ms                                                 | 284 ms: 1.00x slower                                                          |
| Geometric mean | (ref)                                                  | 1.10x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250722-darwin-arm64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.13 ms: 1.24x faster                                                         |
| regex_v8       | 17.0 ms                                                | 15.5 ms: 1.10x faster                                                         |
| regex_compile  | 78.3 ms                                                | 71.6 ms: 1.09x faster                                                         |
| regex_dna      | 149 ms                                                 | 138 ms: 1.08x faster                                                          |
| Geometric mean | (ref)                                                  | 1.13x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250722-darwin-arm64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| unpickle_pure_python | 165 us                                                 | 118 us: 1.40x faster                                                          |
| tomli_loads          | 1.57 sec                                               | 1.15 sec: 1.36x faster                                                        |
| xml_etree_process    | 41.3 ms                                                | 33.6 ms: 1.23x faster                                                         |
| xml_etree_generate   | 57.1 ms                                                | 48.2 ms: 1.19x faster                                                         |
| pickle_pure_python   | 215 us                                                 | 202 us: 1.06x faster                                                          |
| xml_etree_parse      | 108 ms                                                 | 103 ms: 1.04x faster                                                          |
| xml_etree_iterparse  | 74.2 ms                                                | 72.2 ms: 1.03x faster                                                         |
| json_loads           | 17.0 us                                                | 16.9 us: 1.01x faster                                                         |
| json_dumps           | 6.47 ms                                                | 6.60 ms: 1.02x slower                                                         |
| Geometric mean       | (ref)                                                  | 1.14x faster                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250722-darwin-arm64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup         | 18.8 ms                                                | 16.5 ms: 1.14x faster                                                         |
| python_startup_no_site | 13.7 ms                                                | 12.4 ms: 1.11x faster                                                         |
| Geometric mean         | (ref)                                                  | 1.12x faster                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250722-darwin-arm64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mako            | 7.75 ms                                                | 6.44 ms: 1.20x faster                                                         |
| genshi_text     | 16.9 ms                                                | 15.2 ms: 1.12x faster                                                         |
| genshi_xml      | 34.1 ms                                                | 32.7 ms: 1.04x faster                                                         |
| django_template | 20.5 ms                                                | 23.0 ms: 1.12x slower                                                         |
| Geometric mean  | (ref)                                                  | 1.06x faster                                                                  |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250722-darwin-arm64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|----------------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mdp                              | 1.50 sec                                               | 745 ms: 2.01x faster                                                          |
| async_tree_memoization_tg        | 288 ms                                                 | 191 ms: 1.51x faster                                                          |
| async_tree_eager_io              | 511 ms                                                 | 359 ms: 1.42x faster                                                          |
| unpickle_pure_python             | 165 us                                                 | 118 us: 1.40x faster                                                          |
| async_tree_memoization           | 268 ms                                                 | 193 ms: 1.39x faster                                                          |
| deepcopy                         | 236 us                                                 | 173 us: 1.37x faster                                                          |
| go                               | 117 ms                                                 | 85.4 ms: 1.37x faster                                                         |
| tomli_loads                      | 1.57 sec                                               | 1.15 sec: 1.36x faster                                                        |
| async_tree_io_tg                 | 500 ms                                                 | 367 ms: 1.36x faster                                                          |
| async_tree_io                    | 508 ms                                                 | 380 ms: 1.34x faster                                                          |
| generators                       | 31.9 ms                                                | 24.3 ms: 1.31x faster                                                         |
| pyflate                          | 352 ms                                                 | 270 ms: 1.30x faster                                                          |
| async_tree_eager_io_tg           | 479 ms                                                 | 368 ms: 1.30x faster                                                          |
| spectral_norm                    | 76.5 ms                                                | 58.8 ms: 1.30x faster                                                         |
| async_tree_none                  | 212 ms                                                 | 163 ms: 1.30x faster                                                          |
| async_tree_none_tg               | 198 ms                                                 | 156 ms: 1.27x faster                                                          |
| deepcopy_memo                    | 27.4 us                                                | 21.6 us: 1.27x faster                                                         |
| scimark_sor                      | 106 ms                                                 | 83.8 ms: 1.26x faster                                                         |
| regex_effbot                     | 2.63 ms                                                | 2.13 ms: 1.24x faster                                                         |
| xml_etree_process                | 41.3 ms                                                | 33.6 ms: 1.23x faster                                                         |
| nbody                            | 73.6 ms                                                | 60.3 ms: 1.22x faster                                                         |
| pprint_safe_repr                 | 541 ms                                                 | 447 ms: 1.21x faster                                                          |
| coroutines                       | 20.0 ms                                                | 16.6 ms: 1.21x faster                                                         |
| mako                             | 7.75 ms                                                | 6.44 ms: 1.20x faster                                                         |
| async_tree_eager_memoization     | 168 ms                                                 | 140 ms: 1.20x faster                                                          |
| pprint_pformat                   | 1.10 sec                                               | 921 ms: 1.20x faster                                                          |
| xml_etree_generate               | 57.1 ms                                                | 48.2 ms: 1.19x faster                                                         |
| deepcopy_reduce                  | 2.09 us                                                | 1.78 us: 1.18x faster                                                         |
| hexiom                           | 4.87 ms                                                | 4.15 ms: 1.17x faster                                                         |
| bpe_tokeniser                    | 3.26 sec                                               | 2.80 sec: 1.16x faster                                                        |
| dulwich_log                      | 28.7 ms                                                | 25.1 ms: 1.15x faster                                                         |
| fannkuch                         | 279 ms                                                 | 243 ms: 1.15x faster                                                          |
| python_startup                   | 18.8 ms                                                | 16.5 ms: 1.14x faster                                                         |
| scimark_monte_carlo              | 50.4 ms                                                | 44.7 ms: 1.13x faster                                                         |
| crypto_pyaes                     | 55.3 ms                                                | 49.2 ms: 1.12x faster                                                         |
| genshi_text                      | 16.9 ms                                                | 15.2 ms: 1.12x faster                                                         |
| pylint                           | 180 ms                                                 | 161 ms: 1.12x faster                                                          |
| html5lib                         | 36.7 ms                                                | 32.9 ms: 1.11x faster                                                         |
| python_startup_no_site           | 13.7 ms                                                | 12.4 ms: 1.11x faster                                                         |
| async_tree_eager                 | 69.9 ms                                                | 63.2 ms: 1.11x faster                                                         |
| scimark_fft                      | 200 ms                                                 | 180 ms: 1.11x faster                                                          |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 417 ms: 1.10x faster                                                          |
| regex_v8                         | 17.0 ms                                                | 15.5 ms: 1.10x faster                                                         |
| telco                            | 4.84 ms                                                | 4.42 ms: 1.10x faster                                                         |
| deltablue                        | 2.65 ms                                                | 2.42 ms: 1.09x faster                                                         |
| regex_compile                    | 78.3 ms                                                | 71.6 ms: 1.09x faster                                                         |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 412 ms: 1.09x faster                                                          |
| float                            | 55.8 ms                                                | 51.5 ms: 1.08x faster                                                         |
| richards                         | 36.2 ms                                                | 33.4 ms: 1.08x faster                                                         |
| regex_dna                        | 149 ms                                                 | 138 ms: 1.08x faster                                                          |
| chaos                            | 41.1 ms                                                | 38.3 ms: 1.07x faster                                                         |
| comprehensions                   | 12.0 us                                                | 11.2 us: 1.07x faster                                                         |
| 2to3                             | 179 ms                                                 | 167 ms: 1.07x faster                                                          |
| pickle_pure_python               | 215 us                                                 | 202 us: 1.06x faster                                                          |
| logging_simple                   | 3.56 us                                                | 3.35 us: 1.06x faster                                                         |
| logging_format                   | 3.85 us                                                | 3.63 us: 1.06x faster                                                         |
| raytrace                         | 181 ms                                                 | 172 ms: 1.06x faster                                                          |
| meteor_contest                   | 74.0 ms                                                | 70.1 ms: 1.05x faster                                                         |
| k_core                           | 1.61 sec                                               | 1.53 sec: 1.05x faster                                                        |
| typing_runtime_protocols         | 101 us                                                 | 95.9 us: 1.05x faster                                                         |
| sphinx                           | 602 ms                                                 | 574 ms: 1.05x faster                                                          |
| xml_etree_parse                  | 108 ms                                                 | 103 ms: 1.04x faster                                                          |
| genshi_xml                       | 34.1 ms                                                | 32.7 ms: 1.04x faster                                                         |
| sympy_integrate                  | 11.3 ms                                                | 10.9 ms: 1.04x faster                                                         |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 359 ms: 1.04x faster                                                          |
| richards_super                   | 39.2 ms                                                | 37.8 ms: 1.04x faster                                                         |
| nqueens                          | 61.8 ms                                                | 59.6 ms: 1.04x faster                                                         |
| xml_etree_iterparse              | 74.2 ms                                                | 72.2 ms: 1.03x faster                                                         |
| async_generators                 | 294 ms                                                 | 286 ms: 1.03x faster                                                          |
| scimark_lu                       | 75.9 ms                                                | 74.2 ms: 1.02x faster                                                         |
| thrift                           | 466 us                                                 | 456 us: 1.02x faster                                                          |
| json                             | 3.04 ms                                                | 2.98 ms: 1.02x faster                                                         |
| connected_components             | 319 ms                                                 | 313 ms: 1.02x faster                                                          |
| shortest_path                    | 345 ms                                                 | 341 ms: 1.01x faster                                                          |
| pycparser                        | 701 ms                                                 | 692 ms: 1.01x faster                                                          |
| sympy_expand                     | 248 ms                                                 | 245 ms: 1.01x faster                                                          |
| sympy_str                        | 146 ms                                                 | 144 ms: 1.01x faster                                                          |
| json_loads                       | 17.0 us                                                | 16.9 us: 1.01x faster                                                         |
| pidigits                         | 284 ms                                                 | 284 ms: 1.00x slower                                                          |
| docutils                         | 1.44 sec                                               | 1.45 sec: 1.01x slower                                                        |
| sympy_sum                        | 75.1 ms                                                | 76.1 ms: 1.01x slower                                                         |
| coverage                         | 46.2 ms                                                | 47.1 ms: 1.02x slower                                                         |
| json_dumps                       | 6.47 ms                                                | 6.60 ms: 1.02x slower                                                         |
| sqlite_synth                     | 1.55 us                                                | 1.59 us: 1.03x slower                                                         |
| logging_silent                   | 71.0 ns                                                | 73.6 ns: 1.04x slower                                                         |
| gc_traversal                     | 2.94 ms                                                | 3.21 ms: 1.09x slower                                                         |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 3.28 ms: 1.10x slower                                                         |
| django_template                  | 20.5 ms                                                | 23.0 ms: 1.12x slower                                                         |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 390 ms: 1.12x slower                                                          |
| create_gc_cycles                 | 1.19 ms                                                | 1.36 ms: 1.14x slower                                                         |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 167 ms: 1.21x slower                                                          |
| many_optionals                   | 409 us                                                 | 595 us: 1.46x slower                                                          |
| subparsers                       | 9.44 ms                                                | 25.2 ms: 2.67x slower                                                         |
| async_tree_eager_tg              | 47.4 ms                                                | 128 ms: 2.71x slower                                                          |
| Geometric mean                   | (ref)                                                  | 1.08x faster                                                                  |

Benchmark hidden because not significant (3): pathlib, dask, asyncio_websockets
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250722-3.15.0a0-a4de1bf-JIT/bm-20250722-darwin-arm64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.084x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.13x