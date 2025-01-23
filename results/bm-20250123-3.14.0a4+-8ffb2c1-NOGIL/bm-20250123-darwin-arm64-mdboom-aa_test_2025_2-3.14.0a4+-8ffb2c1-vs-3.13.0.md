# Results vs. 3.13.0

- fork: mdboom
- ref: aa_test_2025_2
- machine: darwin-arm64
- commit hash: 8ffb2c1
- commit date: 2025-01-23
- overall geometric mean: 1.004x faster
- HPT reliability: 55.47%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.20x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250123-darwin-arm64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 189 ms: 1.06x slower                                             |
| docutils       | 1.44 sec                                               | 1.43 sec: 1.01x faster                                           |
| html5lib       | 36.7 ms                                                | 33.3 ms: 1.10x faster                                            |
| sphinx         | 602 ms                                                 | 614 ms: 1.02x slower                                             |
| Geometric mean | (ref)                                                  | 1.01x faster                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250123-darwin-arm64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 176 ms: 1.63x faster                                             |
| async_tree_io_tg                 | 500 ms                                                 | 320 ms: 1.56x faster                                             |
| async_tree_eager_io              | 511 ms                                                 | 329 ms: 1.55x faster                                             |
| async_tree_eager_io_tg           | 479 ms                                                 | 312 ms: 1.53x faster                                             |
| async_tree_io                    | 508 ms                                                 | 343 ms: 1.48x faster                                             |
| async_tree_none_tg               | 198 ms                                                 | 136 ms: 1.45x faster                                             |
| async_tree_memoization           | 268 ms                                                 | 199 ms: 1.35x faster                                             |
| async_tree_none                  | 212 ms                                                 | 160 ms: 1.32x faster                                             |
| coroutines                       | 20.0 ms                                                | 17.0 ms: 1.18x faster                                            |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 386 ms: 1.16x faster                                             |
| async_generators                 | 294 ms                                                 | 260 ms: 1.13x faster                                             |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 409 ms: 1.12x faster                                             |
| async_tree_eager_memoization     | 168 ms                                                 | 151 ms: 1.11x faster                                             |
| asyncio_websockets               | 242 ms                                                 | 238 ms: 1.02x faster                                             |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 370 ms: 1.01x faster                                             |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 368 ms: 1.06x slower                                             |
| async_tree_eager                 | 69.9 ms                                                | 81.5 ms: 1.17x slower                                            |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 162 ms: 1.17x slower                                             |
| async_tree_eager_tg              | 47.4 ms                                                | 120 ms: 2.54x slower                                             |
| Geometric mean                   | (ref)                                                  | 1.14x faster                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250123-darwin-arm64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| float          | 55.8 ms                                                | 50.7 ms: 1.10x faster                                            |
| pidigits       | 284 ms                                                 | 280 ms: 1.01x faster                                             |
| nbody          | 73.6 ms                                                | 87.6 ms: 1.19x slower                                            |
| Geometric mean | (ref)                                                  | 1.02x slower                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250123-darwin-arm64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.08 ms: 1.26x faster                                            |
| regex_v8       | 17.0 ms                                                | 15.5 ms: 1.10x faster                                            |
| regex_dna      | 149 ms                                                 | 137 ms: 1.09x faster                                             |
| regex_compile  | 78.3 ms                                                | 77.1 ms: 1.02x faster                                            |
| Geometric mean | (ref)                                                  | 1.11x faster                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250123-darwin-arm64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| xml_etree_iterparse  | 74.2 ms                                                | 62.5 ms: 1.19x faster                                            |
| tomli_loads          | 1.57 sec                                               | 1.36 sec: 1.15x faster                                           |
| xml_etree_parse      | 108 ms                                                 | 99.6 ms: 1.08x faster                                            |
| unpickle_pure_python | 165 us                                                 | 162 us: 1.02x faster                                             |
| xml_etree_generate   | 57.1 ms                                                | 56.1 ms: 1.02x faster                                            |
| json_loads           | 17.0 us                                                | 17.7 us: 1.04x slower                                            |
| pickle_pure_python   | 215 us                                                 | 224 us: 1.04x slower                                             |
| xml_etree_process    | 41.3 ms                                                | 45.6 ms: 1.10x slower                                            |
| json_dumps           | 6.47 ms                                                | 7.96 ms: 1.23x slower                                            |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250123-darwin-arm64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 18.8 ms                                                | 20.7 ms: 1.10x slower                                            |
| python_startup_no_site | 13.7 ms                                                | 16.1 ms: 1.17x slower                                            |
| Geometric mean         | (ref)                                                  | 1.13x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250123-darwin-arm64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| genshi_xml      | 34.1 ms                                                | 33.1 ms: 1.03x faster                                            |
| genshi_text     | 16.9 ms                                                | 17.2 ms: 1.02x slower                                            |
| django_template | 20.5 ms                                                | 24.6 ms: 1.20x slower                                            |
| mako            | 7.75 ms                                                | 9.98 ms: 1.29x slower                                            |
| Geometric mean  | (ref)                                                  | 1.11x slower                                                     |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250123-darwin-arm64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 176 ms: 1.63x faster                                             |
| async_tree_io_tg                 | 500 ms                                                 | 320 ms: 1.56x faster                                             |
| async_tree_eager_io              | 511 ms                                                 | 329 ms: 1.55x faster                                             |
| async_tree_eager_io_tg           | 479 ms                                                 | 312 ms: 1.53x faster                                             |
| async_tree_io                    | 508 ms                                                 | 343 ms: 1.48x faster                                             |
| async_tree_none_tg               | 198 ms                                                 | 136 ms: 1.45x faster                                             |
| create_gc_cycles                 | 1.19 ms                                                | 821 us: 1.45x faster                                             |
| deepcopy                         | 236 us                                                 | 173 us: 1.36x faster                                             |
| async_tree_memoization           | 268 ms                                                 | 199 ms: 1.35x faster                                             |
| generators                       | 31.9 ms                                                | 23.8 ms: 1.34x faster                                            |
| async_tree_none                  | 212 ms                                                 | 160 ms: 1.32x faster                                             |
| gc_traversal                     | 2.94 ms                                                | 2.31 ms: 1.27x faster                                            |
| regex_effbot                     | 2.63 ms                                                | 2.08 ms: 1.26x faster                                            |
| deepcopy_memo                    | 27.4 us                                                | 21.8 us: 1.26x faster                                            |
| sqlite_synth                     | 1.55 us                                                | 1.31 us: 1.19x faster                                            |
| xml_etree_iterparse              | 74.2 ms                                                | 62.5 ms: 1.19x faster                                            |
| coroutines                       | 20.0 ms                                                | 17.0 ms: 1.18x faster                                            |
| deepcopy_reduce                  | 2.09 us                                                | 1.78 us: 1.18x faster                                            |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 386 ms: 1.16x faster                                             |
| tomli_loads                      | 1.57 sec                                               | 1.36 sec: 1.15x faster                                           |
| async_generators                 | 294 ms                                                 | 260 ms: 1.13x faster                                             |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 409 ms: 1.12x faster                                             |
| go                               | 117 ms                                                 | 104 ms: 1.12x faster                                             |
| async_tree_eager_memoization     | 168 ms                                                 | 151 ms: 1.11x faster                                             |
| pyflate                          | 352 ms                                                 | 317 ms: 1.11x faster                                             |
| html5lib                         | 36.7 ms                                                | 33.3 ms: 1.10x faster                                            |
| float                            | 55.8 ms                                                | 50.7 ms: 1.10x faster                                            |
| regex_v8                         | 17.0 ms                                                | 15.5 ms: 1.10x faster                                            |
| scimark_sor                      | 106 ms                                                 | 96.8 ms: 1.09x faster                                            |
| regex_dna                        | 149 ms                                                 | 137 ms: 1.09x faster                                             |
| xml_etree_parse                  | 108 ms                                                 | 99.6 ms: 1.08x faster                                            |
| bpe_tokeniser                    | 3.26 sec                                               | 3.03 sec: 1.08x faster                                           |
| pylint                           | 180 ms                                                 | 170 ms: 1.06x faster                                             |
| pycparser                        | 701 ms                                                 | 673 ms: 1.04x faster                                             |
| spectral_norm                    | 76.5 ms                                                | 74.2 ms: 1.03x faster                                            |
| genshi_xml                       | 34.1 ms                                                | 33.1 ms: 1.03x faster                                            |
| nqueens                          | 61.8 ms                                                | 60.4 ms: 1.02x faster                                            |
| json                             | 3.04 ms                                                | 2.98 ms: 1.02x faster                                            |
| asyncio_websockets               | 242 ms                                                 | 238 ms: 1.02x faster                                             |
| unpickle_pure_python             | 165 us                                                 | 162 us: 1.02x faster                                             |
| xml_etree_generate               | 57.1 ms                                                | 56.1 ms: 1.02x faster                                            |
| regex_compile                    | 78.3 ms                                                | 77.1 ms: 1.02x faster                                            |
| pathlib                          | 23.2 ms                                                | 22.9 ms: 1.01x faster                                            |
| docutils                         | 1.44 sec                                               | 1.43 sec: 1.01x faster                                           |
| pidigits                         | 284 ms                                                 | 280 ms: 1.01x faster                                             |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 370 ms: 1.01x faster                                             |
| sqlglot_normalize                | 188 ms                                                 | 191 ms: 1.01x slower                                             |
| shortest_path                    | 345 ms                                                 | 350 ms: 1.01x slower                                             |
| telco                            | 4.84 ms                                                | 4.92 ms: 1.02x slower                                            |
| genshi_text                      | 16.9 ms                                                | 17.2 ms: 1.02x slower                                            |
| sphinx                           | 602 ms                                                 | 614 ms: 1.02x slower                                             |
| fannkuch                         | 279 ms                                                 | 285 ms: 1.02x slower                                             |
| sqlglot_optimize                 | 34.7 ms                                                | 35.4 ms: 1.02x slower                                            |
| connected_components             | 319 ms                                                 | 326 ms: 1.02x slower                                             |
| dulwich_log                      | 28.7 ms                                                | 29.6 ms: 1.03x slower                                            |
| bench_mp_pool                    | 64.7 ms                                                | 66.9 ms: 1.03x slower                                            |
| json_loads                       | 17.0 us                                                | 17.7 us: 1.04x slower                                            |
| pickle_pure_python               | 215 us                                                 | 224 us: 1.04x slower                                             |
| scimark_fft                      | 200 ms                                                 | 211 ms: 1.06x slower                                             |
| 2to3                             | 179 ms                                                 | 189 ms: 1.06x slower                                             |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 368 ms: 1.06x slower                                             |
| mdp                              | 1.50 sec                                               | 1.60 sec: 1.07x slower                                           |
| sympy_str                        | 146 ms                                                 | 156 ms: 1.07x slower                                             |
| sympy_expand                     | 248 ms                                                 | 265 ms: 1.07x slower                                             |
| logging_simple                   | 3.56 us                                                | 3.81 us: 1.07x slower                                            |
| sympy_sum                        | 75.1 ms                                                | 80.4 ms: 1.07x slower                                            |
| meteor_contest                   | 74.0 ms                                                | 79.4 ms: 1.07x slower                                            |
| logging_format                   | 3.85 us                                                | 4.18 us: 1.09x slower                                            |
| sympy_integrate                  | 11.3 ms                                                | 12.3 ms: 1.09x slower                                            |
| richards                         | 36.2 ms                                                | 39.4 ms: 1.09x slower                                            |
| python_startup                   | 18.8 ms                                                | 20.7 ms: 1.10x slower                                            |
| xml_etree_process                | 41.3 ms                                                | 45.6 ms: 1.10x slower                                            |
| coverage                         | 46.2 ms                                                | 51.3 ms: 1.11x slower                                            |
| hexiom                           | 4.87 ms                                                | 5.40 ms: 1.11x slower                                            |
| crypto_pyaes                     | 55.3 ms                                                | 61.5 ms: 1.11x slower                                            |
| thrift                           | 466 us                                                 | 519 us: 1.11x slower                                             |
| chaos                            | 41.1 ms                                                | 46.2 ms: 1.13x slower                                            |
| richards_super                   | 39.2 ms                                                | 44.2 ms: 1.13x slower                                            |
| scimark_monte_carlo              | 50.4 ms                                                | 56.9 ms: 1.13x slower                                            |
| many_optionals                   | 409 us                                                 | 466 us: 1.14x slower                                             |
| sqlalchemy_declarative           | 59.0 ms                                                | 67.4 ms: 1.14x slower                                            |
| sqlglot_transpile                | 1.04 ms                                                | 1.19 ms: 1.15x slower                                            |
| typing_runtime_protocols         | 101 us                                                 | 117 us: 1.16x slower                                             |
| sqlalchemy_imperative            | 6.69 ms                                                | 7.78 ms: 1.16x slower                                            |
| async_tree_eager                 | 69.9 ms                                                | 81.5 ms: 1.17x slower                                            |
| python_startup_no_site           | 13.7 ms                                                | 16.1 ms: 1.17x slower                                            |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 162 ms: 1.17x slower                                             |
| sqlglot_parse                    | 852 us                                                 | 1.01 ms: 1.18x slower                                            |
| comprehensions                   | 12.0 us                                                | 14.2 us: 1.19x slower                                            |
| nbody                            | 73.6 ms                                                | 87.6 ms: 1.19x slower                                            |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 3.58 ms: 1.20x slower                                            |
| django_template                  | 20.5 ms                                                | 24.6 ms: 1.20x slower                                            |
| json_dumps                       | 6.47 ms                                                | 7.96 ms: 1.23x slower                                            |
| mako                             | 7.75 ms                                                | 9.98 ms: 1.29x slower                                            |
| deltablue                        | 2.65 ms                                                | 3.41 ms: 1.29x slower                                            |
| logging_silent                   | 71.0 ns                                                | 92.6 ns: 1.30x slower                                            |
| scimark_lu                       | 75.9 ms                                                | 99.1 ms: 1.31x slower                                            |
| raytrace                         | 181 ms                                                 | 249 ms: 1.37x slower                                             |
| subparsers                       | 9.44 ms                                                | 13.4 ms: 1.42x slower                                            |
| bench_thread_pool                | 503 us                                                 | 794 us: 1.58x slower                                             |
| async_tree_eager_tg              | 47.4 ms                                                | 120 ms: 2.54x slower                                             |
| Geometric mean                   | (ref)                                                  | 1.00x slower                                                     |

Benchmark hidden because not significant (3): pprint_safe_repr, pprint_pformat, k_core
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.004x faster

# HPT report

- Reliability score: 55.47% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.20x