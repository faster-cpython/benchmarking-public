# Results vs. 3.13.0

- fork: faster-cpython
- ref: use_stackrefs
- machine: darwin-arm64
- commit hash: 3e929d7
- commit date: 2025-02-28
- overall geometric mean: 1.015x faster
- HPT reliability: 73.84%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250228-darwin-arm64-faster%2dcpython-use_stackrefs-3.14.0a5+-3e929d7 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 173 ms: 1.03x faster                                                      |
| docutils       | 1.44 sec                                               | 1.50 sec: 1.04x slower                                                    |
| html5lib       | 36.7 ms                                                | 32.3 ms: 1.14x faster                                                     |
| Geometric mean | (ref)                                                  | 1.03x faster                                                              |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250228-darwin-arm64-faster%2dcpython-use_stackrefs-3.14.0a5+-3e929d7 |
|----------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 206 ms: 1.40x faster                                                      |
| async_tree_eager_io              | 511 ms                                                 | 384 ms: 1.33x faster                                                      |
| async_tree_io_tg                 | 500 ms                                                 | 385 ms: 1.30x faster                                                      |
| async_tree_memoization           | 268 ms                                                 | 209 ms: 1.28x faster                                                      |
| async_tree_io                    | 508 ms                                                 | 400 ms: 1.27x faster                                                      |
| async_tree_none                  | 212 ms                                                 | 172 ms: 1.23x faster                                                      |
| async_tree_eager_io_tg           | 479 ms                                                 | 395 ms: 1.21x faster                                                      |
| async_tree_none_tg               | 198 ms                                                 | 165 ms: 1.20x faster                                                      |
| coroutines                       | 20.0 ms                                                | 17.6 ms: 1.14x faster                                                     |
| async_tree_eager_memoization     | 168 ms                                                 | 149 ms: 1.13x faster                                                      |
| async_generators                 | 294 ms                                                 | 262 ms: 1.12x faster                                                      |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 426 ms: 1.08x faster                                                      |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 424 ms: 1.06x faster                                                      |
| async_tree_eager                 | 69.9 ms                                                | 67.3 ms: 1.04x faster                                                     |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 363 ms: 1.03x faster                                                      |
| asyncio_websockets               | 242 ms                                                 | 242 ms: 1.00x faster                                                      |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 404 ms: 1.16x slower                                                      |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 187 ms: 1.36x slower                                                      |
| async_tree_eager_tg              | 47.4 ms                                                | 140 ms: 2.96x slower                                                      |
| Geometric mean                   | (ref)                                                  | 1.05x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250228-darwin-arm64-faster%2dcpython-use_stackrefs-3.14.0a5+-3e929d7 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 53.0 ms: 1.05x faster                                                     |
| nbody          | 73.6 ms                                                | 79.9 ms: 1.09x slower                                                     |
| Geometric mean | (ref)                                                  | 1.01x slower                                                              |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250228-darwin-arm64-faster%2dcpython-use_stackrefs-3.14.0a5+-3e929d7 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.29 ms: 1.15x faster                                                     |
| regex_dna      | 149 ms                                                 | 141 ms: 1.06x faster                                                      |
| regex_compile  | 78.3 ms                                                | 75.5 ms: 1.04x faster                                                     |
| regex_v8       | 17.0 ms                                                | 16.9 ms: 1.01x faster                                                     |
| Geometric mean | (ref)                                                  | 1.06x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250228-darwin-arm64-faster%2dcpython-use_stackrefs-3.14.0a5+-3e929d7 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 1.57 sec                                               | 1.43 sec: 1.10x faster                                                    |
| xml_etree_parse      | 108 ms                                                 | 102 ms: 1.06x faster                                                      |
| xml_etree_iterparse  | 74.2 ms                                                | 73.4 ms: 1.01x faster                                                     |
| xml_etree_process    | 41.3 ms                                                | 40.9 ms: 1.01x faster                                                     |
| xml_etree_generate   | 57.1 ms                                                | 56.6 ms: 1.01x faster                                                     |
| unpickle_pure_python | 165 us                                                 | 168 us: 1.02x slower                                                      |
| json_loads           | 17.0 us                                                | 17.6 us: 1.03x slower                                                     |
| pickle_pure_python   | 215 us                                                 | 223 us: 1.04x slower                                                      |
| json_dumps           | 6.47 ms                                                | 7.45 ms: 1.15x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250228-darwin-arm64-faster%2dcpython-use_stackrefs-3.14.0a5+-3e929d7 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 13.7 ms                                                | 11.8 ms: 1.16x faster                                                     |
| python_startup         | 18.8 ms                                                | 16.6 ms: 1.14x faster                                                     |
| Geometric mean         | (ref)                                                  | 1.15x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250228-darwin-arm64-faster%2dcpython-use_stackrefs-3.14.0a5+-3e929d7 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 15.4 ms: 1.10x faster                                                     |
| genshi_xml      | 34.1 ms                                                | 32.0 ms: 1.07x faster                                                     |
| mako            | 7.75 ms                                                | 7.81 ms: 1.01x slower                                                     |
| django_template | 20.5 ms                                                | 22.7 ms: 1.11x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                              |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250228-darwin-arm64-faster%2dcpython-use_stackrefs-3.14.0a5+-3e929d7 |
|----------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| deepcopy                         | 236 us                                                 | 164 us: 1.44x faster                                                      |
| async_tree_memoization_tg        | 288 ms                                                 | 206 ms: 1.40x faster                                                      |
| deepcopy_memo                    | 27.4 us                                                | 20.3 us: 1.35x faster                                                     |
| async_tree_eager_io              | 511 ms                                                 | 384 ms: 1.33x faster                                                      |
| async_tree_io_tg                 | 500 ms                                                 | 385 ms: 1.30x faster                                                      |
| async_tree_memoization           | 268 ms                                                 | 209 ms: 1.28x faster                                                      |
| generators                       | 31.9 ms                                                | 24.9 ms: 1.28x faster                                                     |
| async_tree_io                    | 508 ms                                                 | 400 ms: 1.27x faster                                                      |
| go                               | 117 ms                                                 | 93.0 ms: 1.26x faster                                                     |
| async_tree_none                  | 212 ms                                                 | 172 ms: 1.23x faster                                                      |
| deepcopy_reduce                  | 2.09 us                                                | 1.71 us: 1.23x faster                                                     |
| async_tree_eager_io_tg           | 479 ms                                                 | 395 ms: 1.21x faster                                                      |
| async_tree_none_tg               | 198 ms                                                 | 165 ms: 1.20x faster                                                      |
| scimark_sor                      | 106 ms                                                 | 89.1 ms: 1.19x faster                                                     |
| python_startup_no_site           | 13.7 ms                                                | 11.8 ms: 1.16x faster                                                     |
| regex_effbot                     | 2.63 ms                                                | 2.29 ms: 1.15x faster                                                     |
| coroutines                       | 20.0 ms                                                | 17.6 ms: 1.14x faster                                                     |
| html5lib                         | 36.7 ms                                                | 32.3 ms: 1.14x faster                                                     |
| python_startup                   | 18.8 ms                                                | 16.6 ms: 1.14x faster                                                     |
| async_tree_eager_memoization     | 168 ms                                                 | 149 ms: 1.13x faster                                                      |
| async_generators                 | 294 ms                                                 | 262 ms: 1.12x faster                                                      |
| genshi_text                      | 16.9 ms                                                | 15.4 ms: 1.10x faster                                                     |
| tomli_loads                      | 1.57 sec                                               | 1.43 sec: 1.10x faster                                                    |
| bench_mp_pool                    | 64.7 ms                                                | 59.7 ms: 1.08x faster                                                     |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 426 ms: 1.08x faster                                                      |
| pprint_pformat                   | 1.10 sec                                               | 1.03 sec: 1.07x faster                                                    |
| pylint                           | 180 ms                                                 | 168 ms: 1.07x faster                                                      |
| genshi_xml                       | 34.1 ms                                                | 32.0 ms: 1.07x faster                                                     |
| scimark_monte_carlo              | 50.4 ms                                                | 47.5 ms: 1.06x faster                                                     |
| pprint_safe_repr                 | 541 ms                                                 | 509 ms: 1.06x faster                                                      |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 424 ms: 1.06x faster                                                      |
| regex_dna                        | 149 ms                                                 | 141 ms: 1.06x faster                                                      |
| xml_etree_parse                  | 108 ms                                                 | 102 ms: 1.06x faster                                                      |
| float                            | 55.8 ms                                                | 53.0 ms: 1.05x faster                                                     |
| async_tree_eager                 | 69.9 ms                                                | 67.3 ms: 1.04x faster                                                     |
| telco                            | 4.84 ms                                                | 4.66 ms: 1.04x faster                                                     |
| regex_compile                    | 78.3 ms                                                | 75.5 ms: 1.04x faster                                                     |
| 2to3                             | 179 ms                                                 | 173 ms: 1.03x faster                                                      |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 363 ms: 1.03x faster                                                      |
| thrift                           | 466 us                                                 | 454 us: 1.03x faster                                                      |
| k_core                           | 1.61 sec                                               | 1.58 sec: 1.02x faster                                                    |
| json                             | 3.04 ms                                                | 3.00 ms: 1.01x faster                                                     |
| sqlite_synth                     | 1.55 us                                                | 1.54 us: 1.01x faster                                                     |
| xml_etree_iterparse              | 74.2 ms                                                | 73.4 ms: 1.01x faster                                                     |
| xml_etree_process                | 41.3 ms                                                | 40.9 ms: 1.01x faster                                                     |
| xml_etree_generate               | 57.1 ms                                                | 56.6 ms: 1.01x faster                                                     |
| regex_v8                         | 17.0 ms                                                | 16.9 ms: 1.01x faster                                                     |
| asyncio_websockets               | 242 ms                                                 | 242 ms: 1.00x faster                                                      |
| sqlglot_optimize                 | 34.7 ms                                                | 34.6 ms: 1.00x faster                                                     |
| scimark_fft                      | 200 ms                                                 | 200 ms: 1.00x slower                                                      |
| sympy_expand                     | 248 ms                                                 | 249 ms: 1.00x slower                                                      |
| sqlglot_parse                    | 852 us                                                 | 856 us: 1.00x slower                                                      |
| sqlglot_normalize                | 188 ms                                                 | 189 ms: 1.01x slower                                                      |
| deltablue                        | 2.65 ms                                                | 2.66 ms: 1.01x slower                                                     |
| logging_silent                   | 71.0 ns                                                | 71.4 ns: 1.01x slower                                                     |
| mako                             | 7.75 ms                                                | 7.81 ms: 1.01x slower                                                     |
| dulwich_log                      | 28.7 ms                                                | 29.0 ms: 1.01x slower                                                     |
| pathlib                          | 23.2 ms                                                | 23.5 ms: 1.01x slower                                                     |
| shortest_path                    | 345 ms                                                 | 351 ms: 1.02x slower                                                      |
| logging_simple                   | 3.56 us                                                | 3.62 us: 1.02x slower                                                     |
| logging_format                   | 3.85 us                                                | 3.92 us: 1.02x slower                                                     |
| mdp                              | 1.50 sec                                               | 1.53 sec: 1.02x slower                                                    |
| unpickle_pure_python             | 165 us                                                 | 168 us: 1.02x slower                                                      |
| bpe_tokeniser                    | 3.26 sec                                               | 3.32 sec: 1.02x slower                                                    |
| coverage                         | 46.2 ms                                                | 47.1 ms: 1.02x slower                                                     |
| hexiom                           | 4.87 ms                                                | 4.96 ms: 1.02x slower                                                     |
| sympy_str                        | 146 ms                                                 | 149 ms: 1.02x slower                                                      |
| sqlalchemy_imperative            | 6.69 ms                                                | 6.88 ms: 1.03x slower                                                     |
| connected_components             | 319 ms                                                 | 328 ms: 1.03x slower                                                      |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 3.07 ms: 1.03x slower                                                     |
| sympy_sum                        | 75.1 ms                                                | 77.5 ms: 1.03x slower                                                     |
| json_loads                       | 17.0 us                                                | 17.6 us: 1.03x slower                                                     |
| docutils                         | 1.44 sec                                               | 1.50 sec: 1.04x slower                                                    |
| richards                         | 36.2 ms                                                | 37.5 ms: 1.04x slower                                                     |
| spectral_norm                    | 76.5 ms                                                | 79.5 ms: 1.04x slower                                                     |
| pickle_pure_python               | 215 us                                                 | 223 us: 1.04x slower                                                      |
| sqlalchemy_declarative           | 59.0 ms                                                | 61.5 ms: 1.04x slower                                                     |
| meteor_contest                   | 74.0 ms                                                | 77.5 ms: 1.05x slower                                                     |
| bench_thread_pool                | 503 us                                                 | 528 us: 1.05x slower                                                      |
| gc_traversal                     | 2.94 ms                                                | 3.10 ms: 1.06x slower                                                     |
| richards_super                   | 39.2 ms                                                | 41.8 ms: 1.07x slower                                                     |
| raytrace                         | 181 ms                                                 | 193 ms: 1.07x slower                                                      |
| create_gc_cycles                 | 1.19 ms                                                | 1.27 ms: 1.07x slower                                                     |
| sympy_integrate                  | 11.3 ms                                                | 12.1 ms: 1.07x slower                                                     |
| chaos                            | 41.1 ms                                                | 44.1 ms: 1.07x slower                                                     |
| scimark_lu                       | 75.9 ms                                                | 81.8 ms: 1.08x slower                                                     |
| comprehensions                   | 12.0 us                                                | 12.9 us: 1.08x slower                                                     |
| nbody                            | 73.6 ms                                                | 79.9 ms: 1.09x slower                                                     |
| fannkuch                         | 279 ms                                                 | 309 ms: 1.11x slower                                                      |
| django_template                  | 20.5 ms                                                | 22.7 ms: 1.11x slower                                                     |
| crypto_pyaes                     | 55.3 ms                                                | 61.5 ms: 1.11x slower                                                     |
| nqueens                          | 61.8 ms                                                | 69.2 ms: 1.12x slower                                                     |
| many_optionals                   | 409 us                                                 | 462 us: 1.13x slower                                                      |
| json_dumps                       | 6.47 ms                                                | 7.45 ms: 1.15x slower                                                     |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 404 ms: 1.16x slower                                                      |
| subparsers                       | 9.44 ms                                                | 12.7 ms: 1.34x slower                                                     |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 187 ms: 1.36x slower                                                      |
| async_tree_eager_tg              | 47.4 ms                                                | 140 ms: 2.96x slower                                                      |
| Geometric mean                   | (ref)                                                  | 1.02x faster                                                              |

Benchmark hidden because not significant (7): sphinx, dask, sqlglot_transpile, pycparser, pidigits, pyflate, typing_runtime_protocols
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.015x faster

# HPT report

- Reliability score: 73.84% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.08x