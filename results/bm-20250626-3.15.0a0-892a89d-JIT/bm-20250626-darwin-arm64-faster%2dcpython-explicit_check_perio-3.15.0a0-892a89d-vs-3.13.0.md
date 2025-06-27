# Results vs. 3.13.0

- fork: faster-cpython
- ref: explicit_check_perio
- machine: darwin-arm64
- commit hash: 892a89d
- commit date: 2025-06-26
- overall geometric mean: 1.093x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250626-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 168 ms: 1.06x faster                                                            |
| docutils       | 1.44 sec                                               | 1.45 sec: 1.01x slower                                                          |
| html5lib       | 36.7 ms                                                | 29.4 ms: 1.25x faster                                                           |
| sphinx         | 602 ms                                                 | 574 ms: 1.05x faster                                                            |
| Geometric mean | (ref)                                                  | 1.08x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250626-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 187 ms: 1.54x faster                                                            |
| async_tree_eager_io              | 511 ms                                                 | 348 ms: 1.47x faster                                                            |
| async_tree_memoization           | 268 ms                                                 | 186 ms: 1.44x faster                                                            |
| async_tree_io_tg                 | 500 ms                                                 | 360 ms: 1.39x faster                                                            |
| async_tree_io                    | 508 ms                                                 | 368 ms: 1.38x faster                                                            |
| async_tree_none                  | 212 ms                                                 | 156 ms: 1.35x faster                                                            |
| async_tree_eager_io_tg           | 479 ms                                                 | 361 ms: 1.32x faster                                                            |
| async_tree_none_tg               | 198 ms                                                 | 151 ms: 1.32x faster                                                            |
| coroutines                       | 20.0 ms                                                | 16.1 ms: 1.25x faster                                                           |
| async_tree_eager_memoization     | 168 ms                                                 | 138 ms: 1.22x faster                                                            |
| async_tree_eager                 | 69.9 ms                                                | 61.3 ms: 1.14x faster                                                           |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 410 ms: 1.12x faster                                                            |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 407 ms: 1.10x faster                                                            |
| async_generators                 | 294 ms                                                 | 276 ms: 1.06x faster                                                            |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 356 ms: 1.05x faster                                                            |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 387 ms: 1.11x slower                                                            |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 163 ms: 1.18x slower                                                            |
| async_tree_eager_tg              | 47.4 ms                                                | 125 ms: 2.64x slower                                                            |
| Geometric mean                   | (ref)                                                  | 1.13x faster                                                                    |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250626-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 46.8 ms: 1.19x faster                                                           |
| pidigits       | 284 ms                                                 | 283 ms: 1.00x faster                                                            |
| nbody          | 73.6 ms                                                | 74.3 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                  | 1.06x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250626-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 78.3 ms                                                | 66.6 ms: 1.18x faster                                                           |
| regex_effbot   | 2.63 ms                                                | 2.34 ms: 1.12x faster                                                           |
| regex_v8       | 17.0 ms                                                | 16.1 ms: 1.06x faster                                                           |
| regex_dna      | 149 ms                                                 | 143 ms: 1.04x faster                                                            |
| Geometric mean | (ref)                                                  | 1.10x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250626-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 1.57 sec                                               | 1.17 sec: 1.34x faster                                                          |
| unpickle_pure_python | 165 us                                                 | 133 us: 1.25x faster                                                            |
| xml_etree_process    | 41.3 ms                                                | 35.0 ms: 1.18x faster                                                           |
| xml_etree_generate   | 57.1 ms                                                | 50.2 ms: 1.14x faster                                                           |
| pickle_pure_python   | 215 us                                                 | 200 us: 1.08x faster                                                            |
| xml_etree_parse      | 108 ms                                                 | 102 ms: 1.05x faster                                                            |
| xml_etree_iterparse  | 74.2 ms                                                | 70.8 ms: 1.05x faster                                                           |
| json_loads           | 17.0 us                                                | 16.4 us: 1.04x faster                                                           |
| Geometric mean       | (ref)                                                  | 1.12x faster                                                                    |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250626-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 18.8 ms                                                | 17.9 ms: 1.05x faster                                                           |
| python_startup_no_site | 13.7 ms                                                | 13.4 ms: 1.02x faster                                                           |
| Geometric mean         | (ref)                                                  | 1.04x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250626-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 13.5 ms: 1.25x faster                                                           |
| genshi_xml      | 34.1 ms                                                | 29.0 ms: 1.17x faster                                                           |
| mako            | 7.75 ms                                                | 6.82 ms: 1.14x faster                                                           |
| django_template | 20.5 ms                                                | 21.0 ms: 1.03x slower                                                           |
| Geometric mean  | (ref)                                                  | 1.13x faster                                                                    |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250626-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mdp                              | 1.50 sec                                               | 732 ms: 2.05x faster                                                            |
| deepcopy                         | 236 us                                                 | 149 us: 1.58x faster                                                            |
| async_tree_memoization_tg        | 288 ms                                                 | 187 ms: 1.54x faster                                                            |
| go                               | 117 ms                                                 | 77.9 ms: 1.50x faster                                                           |
| deepcopy_memo                    | 27.4 us                                                | 18.3 us: 1.50x faster                                                           |
| async_tree_eager_io              | 511 ms                                                 | 348 ms: 1.47x faster                                                            |
| async_tree_memoization           | 268 ms                                                 | 186 ms: 1.44x faster                                                            |
| async_tree_io_tg                 | 500 ms                                                 | 360 ms: 1.39x faster                                                            |
| scimark_sor                      | 106 ms                                                 | 76.3 ms: 1.38x faster                                                           |
| generators                       | 31.9 ms                                                | 23.1 ms: 1.38x faster                                                           |
| async_tree_io                    | 508 ms                                                 | 368 ms: 1.38x faster                                                            |
| async_tree_none                  | 212 ms                                                 | 156 ms: 1.35x faster                                                            |
| tomli_loads                      | 1.57 sec                                               | 1.17 sec: 1.34x faster                                                          |
| async_tree_eager_io_tg           | 479 ms                                                 | 361 ms: 1.32x faster                                                            |
| async_tree_none_tg               | 198 ms                                                 | 151 ms: 1.32x faster                                                            |
| deepcopy_reduce                  | 2.09 us                                                | 1.62 us: 1.29x faster                                                           |
| pyflate                          | 352 ms                                                 | 277 ms: 1.27x faster                                                            |
| genshi_text                      | 16.9 ms                                                | 13.5 ms: 1.25x faster                                                           |
| html5lib                         | 36.7 ms                                                | 29.4 ms: 1.25x faster                                                           |
| coroutines                       | 20.0 ms                                                | 16.1 ms: 1.25x faster                                                           |
| unpickle_pure_python             | 165 us                                                 | 133 us: 1.25x faster                                                            |
| async_tree_eager_memoization     | 168 ms                                                 | 138 ms: 1.22x faster                                                            |
| scimark_monte_carlo              | 50.4 ms                                                | 42.3 ms: 1.19x faster                                                           |
| float                            | 55.8 ms                                                | 46.8 ms: 1.19x faster                                                           |
| dulwich_log                      | 28.7 ms                                                | 24.2 ms: 1.19x faster                                                           |
| spectral_norm                    | 76.5 ms                                                | 64.7 ms: 1.18x faster                                                           |
| xml_etree_process                | 41.3 ms                                                | 35.0 ms: 1.18x faster                                                           |
| regex_compile                    | 78.3 ms                                                | 66.6 ms: 1.18x faster                                                           |
| genshi_xml                       | 34.1 ms                                                | 29.0 ms: 1.17x faster                                                           |
| async_tree_eager                 | 69.9 ms                                                | 61.3 ms: 1.14x faster                                                           |
| xml_etree_generate               | 57.1 ms                                                | 50.2 ms: 1.14x faster                                                           |
| mako                             | 7.75 ms                                                | 6.82 ms: 1.14x faster                                                           |
| pylint                           | 180 ms                                                 | 159 ms: 1.13x faster                                                            |
| regex_effbot                     | 2.63 ms                                                | 2.34 ms: 1.12x faster                                                           |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 410 ms: 1.12x faster                                                            |
| richards                         | 36.2 ms                                                | 32.5 ms: 1.11x faster                                                           |
| chaos                            | 41.1 ms                                                | 37.0 ms: 1.11x faster                                                           |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 407 ms: 1.10x faster                                                            |
| hexiom                           | 4.87 ms                                                | 4.49 ms: 1.08x faster                                                           |
| pickle_pure_python               | 215 us                                                 | 200 us: 1.08x faster                                                            |
| thrift                           | 466 us                                                 | 434 us: 1.07x faster                                                            |
| bpe_tokeniser                    | 3.26 sec                                               | 3.04 sec: 1.07x faster                                                          |
| raytrace                         | 181 ms                                                 | 170 ms: 1.07x faster                                                            |
| async_generators                 | 294 ms                                                 | 276 ms: 1.06x faster                                                            |
| 2to3                             | 179 ms                                                 | 168 ms: 1.06x faster                                                            |
| deltablue                        | 2.65 ms                                                | 2.49 ms: 1.06x faster                                                           |
| k_core                           | 1.61 sec                                               | 1.52 sec: 1.06x faster                                                          |
| richards_super                   | 39.2 ms                                                | 37.0 ms: 1.06x faster                                                           |
| regex_v8                         | 17.0 ms                                                | 16.1 ms: 1.06x faster                                                           |
| sympy_integrate                  | 11.3 ms                                                | 10.7 ms: 1.06x faster                                                           |
| typing_runtime_protocols         | 101 us                                                 | 95.2 us: 1.06x faster                                                           |
| pathlib                          | 23.2 ms                                                | 21.9 ms: 1.06x faster                                                           |
| json                             | 3.04 ms                                                | 2.88 ms: 1.06x faster                                                           |
| xml_etree_parse                  | 108 ms                                                 | 102 ms: 1.05x faster                                                            |
| python_startup                   | 18.8 ms                                                | 17.9 ms: 1.05x faster                                                           |
| nqueens                          | 61.8 ms                                                | 58.9 ms: 1.05x faster                                                           |
| sympy_str                        | 146 ms                                                 | 139 ms: 1.05x faster                                                            |
| sympy_expand                     | 248 ms                                                 | 236 ms: 1.05x faster                                                            |
| sphinx                           | 602 ms                                                 | 574 ms: 1.05x faster                                                            |
| xml_etree_iterparse              | 74.2 ms                                                | 70.8 ms: 1.05x faster                                                           |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 356 ms: 1.05x faster                                                            |
| telco                            | 4.84 ms                                                | 4.62 ms: 1.05x faster                                                           |
| regex_dna                        | 149 ms                                                 | 143 ms: 1.04x faster                                                            |
| json_loads                       | 17.0 us                                                | 16.4 us: 1.04x faster                                                           |
| connected_components             | 319 ms                                                 | 309 ms: 1.03x faster                                                            |
| shortest_path                    | 345 ms                                                 | 335 ms: 1.03x faster                                                            |
| comprehensions                   | 12.0 us                                                | 11.6 us: 1.03x faster                                                           |
| logging_simple                   | 3.56 us                                                | 3.47 us: 1.03x faster                                                           |
| scimark_lu                       | 75.9 ms                                                | 74.0 ms: 1.03x faster                                                           |
| sympy_sum                        | 75.1 ms                                                | 73.3 ms: 1.02x faster                                                           |
| python_startup_no_site           | 13.7 ms                                                | 13.4 ms: 1.02x faster                                                           |
| pycparser                        | 701 ms                                                 | 686 ms: 1.02x faster                                                            |
| logging_format                   | 3.85 us                                                | 3.79 us: 1.02x faster                                                           |
| crypto_pyaes                     | 55.3 ms                                                | 55.0 ms: 1.00x faster                                                           |
| dask                             | 771 ms                                                 | 768 ms: 1.00x faster                                                            |
| pidigits                         | 284 ms                                                 | 283 ms: 1.00x faster                                                            |
| docutils                         | 1.44 sec                                               | 1.45 sec: 1.01x slower                                                          |
| scimark_fft                      | 200 ms                                                 | 201 ms: 1.01x slower                                                            |
| sqlite_synth                     | 1.55 us                                                | 1.57 us: 1.01x slower                                                           |
| nbody                            | 73.6 ms                                                | 74.3 ms: 1.01x slower                                                           |
| coverage                         | 46.2 ms                                                | 47.0 ms: 1.02x slower                                                           |
| meteor_contest                   | 74.0 ms                                                | 75.7 ms: 1.02x slower                                                           |
| django_template                  | 20.5 ms                                                | 21.0 ms: 1.03x slower                                                           |
| fannkuch                         | 279 ms                                                 | 290 ms: 1.04x slower                                                            |
| pprint_pformat                   | 1.10 sec                                               | 1.14 sec: 1.04x slower                                                          |
| pprint_safe_repr                 | 541 ms                                                 | 568 ms: 1.05x slower                                                            |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 387 ms: 1.11x slower                                                            |
| many_optionals                   | 409 us                                                 | 466 us: 1.14x slower                                                            |
| gc_traversal                     | 2.94 ms                                                | 3.35 ms: 1.14x slower                                                           |
| create_gc_cycles                 | 1.19 ms                                                | 1.37 ms: 1.15x slower                                                           |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 163 ms: 1.18x slower                                                            |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 3.55 ms: 1.19x slower                                                           |
| subparsers                       | 9.44 ms                                                | 13.1 ms: 1.39x slower                                                           |
| async_tree_eager_tg              | 47.4 ms                                                | 125 ms: 2.64x slower                                                            |
| logging_silent                   | 71.0 ns                                                | 325 ns: 4.58x slower                                                            |
| Geometric mean                   | (ref)                                                  | 1.08x faster                                                                    |

Benchmark hidden because not significant (2): json_dumps, asyncio_websockets
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250626-3.15.0a0-892a89d-JIT/bm-20250626-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.093x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.13x