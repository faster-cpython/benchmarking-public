# Results vs. 3.13.0

- fork: mdboom
- ref: aa_test_2025
- machine: darwin-arm64
- commit hash: 4844db8
- commit date: 2025-01-21
- overall geometric mean: 1.005x faster
- HPT reliability: 57.90%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.20x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250121-darwin-arm64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 189 ms: 1.06x slower                                           |
| docutils       | 1.44 sec                                               | 1.43 sec: 1.01x faster                                         |
| html5lib       | 36.7 ms                                                | 33.3 ms: 1.10x faster                                          |
| sphinx         | 602 ms                                                 | 624 ms: 1.04x slower                                           |
| Geometric mean | (ref)                                                  | 1.00x faster                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250121-darwin-arm64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 176 ms: 1.64x faster                                           |
| async_tree_io_tg                 | 500 ms                                                 | 319 ms: 1.57x faster                                           |
| async_tree_eager_io              | 511 ms                                                 | 329 ms: 1.55x faster                                           |
| async_tree_eager_io_tg           | 479 ms                                                 | 312 ms: 1.54x faster                                           |
| async_tree_io                    | 508 ms                                                 | 342 ms: 1.48x faster                                           |
| async_tree_none_tg               | 198 ms                                                 | 136 ms: 1.46x faster                                           |
| async_tree_memoization           | 268 ms                                                 | 198 ms: 1.35x faster                                           |
| async_tree_none                  | 212 ms                                                 | 160 ms: 1.32x faster                                           |
| coroutines                       | 20.0 ms                                                | 16.9 ms: 1.18x faster                                          |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 385 ms: 1.16x faster                                           |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 409 ms: 1.12x faster                                           |
| async_generators                 | 294 ms                                                 | 261 ms: 1.12x faster                                           |
| async_tree_eager_memoization     | 168 ms                                                 | 152 ms: 1.11x faster                                           |
| asyncio_websockets               | 242 ms                                                 | 237 ms: 1.02x faster                                           |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 369 ms: 1.01x faster                                           |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 367 ms: 1.06x slower                                           |
| async_tree_eager                 | 69.9 ms                                                | 81.5 ms: 1.16x slower                                          |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 161 ms: 1.17x slower                                           |
| async_tree_eager_tg              | 47.4 ms                                                | 119 ms: 2.52x slower                                           |
| Geometric mean                   | (ref)                                                  | 1.14x faster                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250121-darwin-arm64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| float          | 55.8 ms                                                | 50.6 ms: 1.10x faster                                          |
| pidigits       | 284 ms                                                 | 280 ms: 1.01x faster                                           |
| nbody          | 73.6 ms                                                | 87.3 ms: 1.19x slower                                          |
| Geometric mean | (ref)                                                  | 1.02x slower                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250121-darwin-arm64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.08 ms: 1.27x faster                                          |
| regex_v8       | 17.0 ms                                                | 15.6 ms: 1.09x faster                                          |
| regex_dna      | 149 ms                                                 | 137 ms: 1.09x faster                                           |
| regex_compile  | 78.3 ms                                                | 76.9 ms: 1.02x faster                                          |
| Geometric mean | (ref)                                                  | 1.11x faster                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250121-darwin-arm64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| xml_etree_iterparse  | 74.2 ms                                                | 62.4 ms: 1.19x faster                                          |
| tomli_loads          | 1.57 sec                                               | 1.37 sec: 1.15x faster                                         |
| xml_etree_parse      | 108 ms                                                 | 95.6 ms: 1.13x faster                                          |
| unpickle_pure_python | 165 us                                                 | 162 us: 1.02x faster                                           |
| xml_etree_generate   | 57.1 ms                                                | 56.1 ms: 1.02x faster                                          |
| json_loads           | 17.0 us                                                | 17.8 us: 1.04x slower                                          |
| pickle_pure_python   | 215 us                                                 | 224 us: 1.04x slower                                           |
| xml_etree_process    | 41.3 ms                                                | 45.6 ms: 1.10x slower                                          |
| json_dumps           | 6.47 ms                                                | 7.94 ms: 1.23x slower                                          |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250121-darwin-arm64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup         | 18.8 ms                                                | 20.5 ms: 1.09x slower                                          |
| python_startup_no_site | 13.7 ms                                                | 15.8 ms: 1.15x slower                                          |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250121-darwin-arm64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| genshi_xml      | 34.1 ms                                                | 33.2 ms: 1.03x faster                                          |
| genshi_text     | 16.9 ms                                                | 17.2 ms: 1.02x slower                                          |
| django_template | 20.5 ms                                                | 24.5 ms: 1.20x slower                                          |
| mako            | 7.75 ms                                                | 9.97 ms: 1.29x slower                                          |
| Geometric mean  | (ref)                                                  | 1.11x slower                                                   |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250121-darwin-arm64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 176 ms: 1.64x faster                                           |
| async_tree_io_tg                 | 500 ms                                                 | 319 ms: 1.57x faster                                           |
| async_tree_eager_io              | 511 ms                                                 | 329 ms: 1.55x faster                                           |
| async_tree_eager_io_tg           | 479 ms                                                 | 312 ms: 1.54x faster                                           |
| async_tree_io                    | 508 ms                                                 | 342 ms: 1.48x faster                                           |
| async_tree_none_tg               | 198 ms                                                 | 136 ms: 1.46x faster                                           |
| create_gc_cycles                 | 1.19 ms                                                | 817 us: 1.46x faster                                           |
| deepcopy                         | 236 us                                                 | 173 us: 1.37x faster                                           |
| async_tree_memoization           | 268 ms                                                 | 198 ms: 1.35x faster                                           |
| generators                       | 31.9 ms                                                | 24.0 ms: 1.33x faster                                          |
| async_tree_none                  | 212 ms                                                 | 160 ms: 1.32x faster                                           |
| gc_traversal                     | 2.94 ms                                                | 2.30 ms: 1.27x faster                                          |
| deepcopy_memo                    | 27.4 us                                                | 21.6 us: 1.27x faster                                          |
| regex_effbot                     | 2.63 ms                                                | 2.08 ms: 1.27x faster                                          |
| sqlite_synth                     | 1.55 us                                                | 1.30 us: 1.19x faster                                          |
| xml_etree_iterparse              | 74.2 ms                                                | 62.4 ms: 1.19x faster                                          |
| coroutines                       | 20.0 ms                                                | 16.9 ms: 1.18x faster                                          |
| deepcopy_reduce                  | 2.09 us                                                | 1.78 us: 1.17x faster                                          |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 385 ms: 1.16x faster                                           |
| tomli_loads                      | 1.57 sec                                               | 1.37 sec: 1.15x faster                                         |
| xml_etree_parse                  | 108 ms                                                 | 95.6 ms: 1.13x faster                                          |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 409 ms: 1.12x faster                                           |
| async_generators                 | 294 ms                                                 | 261 ms: 1.12x faster                                           |
| go                               | 117 ms                                                 | 104 ms: 1.12x faster                                           |
| async_tree_eager_memoization     | 168 ms                                                 | 152 ms: 1.11x faster                                           |
| pyflate                          | 352 ms                                                 | 318 ms: 1.11x faster                                           |
| float                            | 55.8 ms                                                | 50.6 ms: 1.10x faster                                          |
| html5lib                         | 36.7 ms                                                | 33.3 ms: 1.10x faster                                          |
| regex_v8                         | 17.0 ms                                                | 15.6 ms: 1.09x faster                                          |
| scimark_sor                      | 106 ms                                                 | 97.0 ms: 1.09x faster                                          |
| regex_dna                        | 149 ms                                                 | 137 ms: 1.09x faster                                           |
| bpe_tokeniser                    | 3.26 sec                                               | 3.03 sec: 1.08x faster                                         |
| pylint                           | 180 ms                                                 | 170 ms: 1.06x faster                                           |
| pycparser                        | 701 ms                                                 | 672 ms: 1.04x faster                                           |
| spectral_norm                    | 76.5 ms                                                | 74.2 ms: 1.03x faster                                          |
| genshi_xml                       | 34.1 ms                                                | 33.2 ms: 1.03x faster                                          |
| nqueens                          | 61.8 ms                                                | 60.4 ms: 1.02x faster                                          |
| unpickle_pure_python             | 165 us                                                 | 162 us: 1.02x faster                                           |
| asyncio_websockets               | 242 ms                                                 | 237 ms: 1.02x faster                                           |
| json                             | 3.04 ms                                                | 2.98 ms: 1.02x faster                                          |
| regex_compile                    | 78.3 ms                                                | 76.9 ms: 1.02x faster                                          |
| xml_etree_generate               | 57.1 ms                                                | 56.1 ms: 1.02x faster                                          |
| pathlib                          | 23.2 ms                                                | 22.9 ms: 1.01x faster                                          |
| pidigits                         | 284 ms                                                 | 280 ms: 1.01x faster                                           |
| docutils                         | 1.44 sec                                               | 1.43 sec: 1.01x faster                                         |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 369 ms: 1.01x faster                                           |
| pprint_pformat                   | 1.10 sec                                               | 1.11 sec: 1.01x slower                                         |
| pprint_safe_repr                 | 541 ms                                                 | 545 ms: 1.01x slower                                           |
| shortest_path                    | 345 ms                                                 | 351 ms: 1.02x slower                                           |
| sqlglot_optimize                 | 34.7 ms                                                | 35.2 ms: 1.02x slower                                          |
| genshi_text                      | 16.9 ms                                                | 17.2 ms: 1.02x slower                                          |
| bench_mp_pool                    | 64.7 ms                                                | 66.0 ms: 1.02x slower                                          |
| fannkuch                         | 279 ms                                                 | 285 ms: 1.02x slower                                           |
| telco                            | 4.84 ms                                                | 4.96 ms: 1.02x slower                                          |
| connected_components             | 319 ms                                                 | 327 ms: 1.03x slower                                           |
| dulwich_log                      | 28.7 ms                                                | 29.6 ms: 1.03x slower                                          |
| sphinx                           | 602 ms                                                 | 624 ms: 1.04x slower                                           |
| json_loads                       | 17.0 us                                                | 17.8 us: 1.04x slower                                          |
| pickle_pure_python               | 215 us                                                 | 224 us: 1.04x slower                                           |
| scimark_fft                      | 200 ms                                                 | 210 ms: 1.05x slower                                           |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 367 ms: 1.06x slower                                           |
| 2to3                             | 179 ms                                                 | 189 ms: 1.06x slower                                           |
| meteor_contest                   | 74.0 ms                                                | 78.9 ms: 1.07x slower                                          |
| mdp                              | 1.50 sec                                               | 1.60 sec: 1.07x slower                                         |
| sympy_str                        | 146 ms                                                 | 156 ms: 1.07x slower                                           |
| logging_simple                   | 3.56 us                                                | 3.82 us: 1.07x slower                                          |
| sympy_expand                     | 248 ms                                                 | 266 ms: 1.07x slower                                           |
| sympy_sum                        | 75.1 ms                                                | 80.7 ms: 1.07x slower                                          |
| python_startup                   | 18.8 ms                                                | 20.5 ms: 1.09x slower                                          |
| sympy_integrate                  | 11.3 ms                                                | 12.3 ms: 1.09x slower                                          |
| richards                         | 36.2 ms                                                | 39.5 ms: 1.09x slower                                          |
| logging_format                   | 3.85 us                                                | 4.21 us: 1.09x slower                                          |
| xml_etree_process                | 41.3 ms                                                | 45.6 ms: 1.10x slower                                          |
| thrift                           | 466 us                                                 | 517 us: 1.11x slower                                           |
| hexiom                           | 4.87 ms                                                | 5.40 ms: 1.11x slower                                          |
| crypto_pyaes                     | 55.3 ms                                                | 61.6 ms: 1.11x slower                                          |
| chaos                            | 41.1 ms                                                | 46.1 ms: 1.12x slower                                          |
| richards_super                   | 39.2 ms                                                | 44.2 ms: 1.13x slower                                          |
| coverage                         | 46.2 ms                                                | 52.2 ms: 1.13x slower                                          |
| scimark_monte_carlo              | 50.4 ms                                                | 57.1 ms: 1.13x slower                                          |
| sqlglot_transpile                | 1.04 ms                                                | 1.18 ms: 1.13x slower                                          |
| sqlalchemy_imperative            | 6.69 ms                                                | 7.61 ms: 1.14x slower                                          |
| sqlalchemy_declarative           | 59.0 ms                                                | 67.2 ms: 1.14x slower                                          |
| many_optionals                   | 409 us                                                 | 468 us: 1.15x slower                                           |
| python_startup_no_site           | 13.7 ms                                                | 15.8 ms: 1.15x slower                                          |
| async_tree_eager                 | 69.9 ms                                                | 81.5 ms: 1.16x slower                                          |
| typing_runtime_protocols         | 101 us                                                 | 117 us: 1.17x slower                                           |
| sqlglot_parse                    | 852 us                                                 | 995 us: 1.17x slower                                           |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 161 ms: 1.17x slower                                           |
| nbody                            | 73.6 ms                                                | 87.3 ms: 1.19x slower                                          |
| comprehensions                   | 12.0 us                                                | 14.2 us: 1.19x slower                                          |
| django_template                  | 20.5 ms                                                | 24.5 ms: 1.20x slower                                          |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 3.58 ms: 1.20x slower                                          |
| json_dumps                       | 6.47 ms                                                | 7.94 ms: 1.23x slower                                          |
| mako                             | 7.75 ms                                                | 9.97 ms: 1.29x slower                                          |
| deltablue                        | 2.65 ms                                                | 3.41 ms: 1.29x slower                                          |
| scimark_lu                       | 75.9 ms                                                | 98.9 ms: 1.30x slower                                          |
| logging_silent                   | 71.0 ns                                                | 93.0 ns: 1.31x slower                                          |
| raytrace                         | 181 ms                                                 | 247 ms: 1.37x slower                                           |
| subparsers                       | 9.44 ms                                                | 13.4 ms: 1.42x slower                                          |
| bench_thread_pool                | 503 us                                                 | 795 us: 1.58x slower                                           |
| async_tree_eager_tg              | 47.4 ms                                                | 119 ms: 2.52x slower                                           |
| Geometric mean                   | (ref)                                                  | 1.00x slower                                                   |

Benchmark hidden because not significant (2): sqlglot_normalize, k_core
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.005x faster

# HPT report

- Reliability score: 57.90% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.20x