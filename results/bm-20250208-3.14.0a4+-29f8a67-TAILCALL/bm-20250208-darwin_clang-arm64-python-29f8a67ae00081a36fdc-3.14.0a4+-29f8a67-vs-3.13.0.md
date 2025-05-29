# Results vs. 3.13.0

- fork: python
- ref: 29f8a67ae00081a36fdc
- machine: darwin-arm64
- commit hash: 29f8a67
- commit date: 2025-02-08
- overall geometric mean: 1.160x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.11x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 186 ms: 1.04x slower                                                   |
| docutils       | 1.44 sec                                               | 1.42 sec: 1.01x faster                                                 |
| html5lib       | 36.7 ms                                                | 28.7 ms: 1.28x faster                                                  |
| sphinx         | 602 ms                                                 | 538 ms: 1.12x faster                                                   |
| Geometric mean | (ref)                                                  | 1.09x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 185 ms: 1.56x faster                                                   |
| async_tree_eager_io              | 511 ms                                                 | 334 ms: 1.53x faster                                                   |
| async_tree_io                    | 508 ms                                                 | 338 ms: 1.50x faster                                                   |
| async_tree_memoization           | 268 ms                                                 | 183 ms: 1.47x faster                                                   |
| async_tree_io_tg                 | 500 ms                                                 | 341 ms: 1.47x faster                                                   |
| async_tree_none                  | 212 ms                                                 | 150 ms: 1.41x faster                                                   |
| async_tree_none_tg               | 198 ms                                                 | 145 ms: 1.37x faster                                                   |
| async_tree_eager_io_tg           | 479 ms                                                 | 350 ms: 1.37x faster                                                   |
| coroutines                       | 20.0 ms                                                | 15.3 ms: 1.31x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 134 ms: 1.25x faster                                                   |
| async_tree_eager                 | 69.9 ms                                                | 58.2 ms: 1.20x faster                                                  |
| async_generators                 | 294 ms                                                 | 248 ms: 1.18x faster                                                   |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 402 ms: 1.14x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 402 ms: 1.12x faster                                                   |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 348 ms: 1.07x faster                                                   |
| asyncio_websockets               | 242 ms                                                 | 242 ms: 1.00x faster                                                   |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 380 ms: 1.10x slower                                                   |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 165 ms: 1.19x slower                                                   |
| async_tree_eager_tg              | 47.4 ms                                                | 122 ms: 2.58x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.17x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 43.6 ms: 1.28x faster                                                  |
| nbody          | 73.6 ms                                                | 61.9 ms: 1.19x faster                                                  |
| pidigits       | 284 ms                                                 | 280 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                  | 1.16x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 78.3 ms                                                | 61.9 ms: 1.27x faster                                                  |
| regex_effbot   | 2.63 ms                                                | 2.36 ms: 1.11x faster                                                  |
| regex_dna      | 149 ms                                                 | 146 ms: 1.02x faster                                                   |
| regex_v8       | 17.0 ms                                                | 17.8 ms: 1.05x slower                                                  |
| Geometric mean | (ref)                                                  | 1.08x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 1.57 sec                                               | 1.15 sec: 1.37x faster                                                 |
| unpickle_pure_python | 165 us                                                 | 124 us: 1.33x faster                                                   |
| xml_etree_process    | 41.3 ms                                                | 34.1 ms: 1.21x faster                                                  |
| pickle_pure_python   | 215 us                                                 | 181 us: 1.18x faster                                                   |
| xml_etree_generate   | 57.1 ms                                                | 48.3 ms: 1.18x faster                                                  |
| xml_etree_parse      | 108 ms                                                 | 99.8 ms: 1.08x faster                                                  |
| xml_etree_iterparse  | 74.2 ms                                                | 69.0 ms: 1.08x faster                                                  |
| json_loads           | 17.0 us                                                | 17.8 us: 1.05x slower                                                  |
| json_dumps           | 6.47 ms                                                | 7.09 ms: 1.10x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.14x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 18.8 ms                                                | 19.2 ms: 1.02x slower                                                  |
| python_startup_no_site | 13.7 ms                                                | 14.3 ms: 1.04x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 12.4 ms: 1.37x faster                                                  |
| genshi_xml      | 34.1 ms                                                | 26.2 ms: 1.30x faster                                                  |
| mako            | 7.75 ms                                                | 6.92 ms: 1.12x faster                                                  |
| django_template | 20.5 ms                                                | 19.0 ms: 1.08x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.21x faster                                                           |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| generators                       | 31.9 ms                                                | 17.1 ms: 1.87x faster                                                  |
| deepcopy                         | 236 us                                                 | 139 us: 1.70x faster                                                   |
| deepcopy_memo                    | 27.4 us                                                | 16.2 us: 1.69x faster                                                  |
| go                               | 117 ms                                                 | 70.5 ms: 1.65x faster                                                  |
| async_tree_memoization_tg        | 288 ms                                                 | 185 ms: 1.56x faster                                                   |
| async_tree_eager_io              | 511 ms                                                 | 334 ms: 1.53x faster                                                   |
| async_tree_io                    | 508 ms                                                 | 338 ms: 1.50x faster                                                   |
| async_tree_memoization           | 268 ms                                                 | 183 ms: 1.47x faster                                                   |
| async_tree_io_tg                 | 500 ms                                                 | 341 ms: 1.47x faster                                                   |
| scimark_sor                      | 106 ms                                                 | 73.5 ms: 1.44x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 150 ms: 1.41x faster                                                   |
| deepcopy_reduce                  | 2.09 us                                                | 1.50 us: 1.40x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 145 ms: 1.37x faster                                                   |
| tomli_loads                      | 1.57 sec                                               | 1.15 sec: 1.37x faster                                                 |
| genshi_text                      | 16.9 ms                                                | 12.4 ms: 1.37x faster                                                  |
| async_tree_eager_io_tg           | 479 ms                                                 | 350 ms: 1.37x faster                                                   |
| unpickle_pure_python             | 165 us                                                 | 124 us: 1.33x faster                                                   |
| spectral_norm                    | 76.5 ms                                                | 58.2 ms: 1.31x faster                                                  |
| richards                         | 36.2 ms                                                | 27.5 ms: 1.31x faster                                                  |
| deltablue                        | 2.65 ms                                                | 2.02 ms: 1.31x faster                                                  |
| coroutines                       | 20.0 ms                                                | 15.3 ms: 1.31x faster                                                  |
| scimark_monte_carlo              | 50.4 ms                                                | 38.6 ms: 1.31x faster                                                  |
| genshi_xml                       | 34.1 ms                                                | 26.2 ms: 1.30x faster                                                  |
| pyflate                          | 352 ms                                                 | 271 ms: 1.30x faster                                                   |
| float                            | 55.8 ms                                                | 43.6 ms: 1.28x faster                                                  |
| hexiom                           | 4.87 ms                                                | 3.81 ms: 1.28x faster                                                  |
| html5lib                         | 36.7 ms                                                | 28.7 ms: 1.28x faster                                                  |
| richards_super                   | 39.2 ms                                                | 31.0 ms: 1.27x faster                                                  |
| regex_compile                    | 78.3 ms                                                | 61.9 ms: 1.27x faster                                                  |
| pprint_pformat                   | 1.10 sec                                               | 874 ms: 1.26x faster                                                   |
| sqlglot_transpile                | 1.04 ms                                                | 826 us: 1.26x faster                                                   |
| pprint_safe_repr                 | 541 ms                                                 | 431 ms: 1.25x faster                                                   |
| async_tree_eager_memoization     | 168 ms                                                 | 134 ms: 1.25x faster                                                   |
| sqlglot_parse                    | 852 us                                                 | 681 us: 1.25x faster                                                   |
| logging_simple                   | 3.56 us                                                | 2.89 us: 1.23x faster                                                  |
| logging_silent                   | 71.0 ns                                                | 57.9 ns: 1.23x faster                                                  |
| nqueens                          | 61.8 ms                                                | 50.5 ms: 1.22x faster                                                  |
| pylint                           | 180 ms                                                 | 147 ms: 1.22x faster                                                   |
| xml_etree_process                | 41.3 ms                                                | 34.1 ms: 1.21x faster                                                  |
| logging_format                   | 3.85 us                                                | 3.19 us: 1.21x faster                                                  |
| async_tree_eager                 | 69.9 ms                                                | 58.2 ms: 1.20x faster                                                  |
| nbody                            | 73.6 ms                                                | 61.9 ms: 1.19x faster                                                  |
| bpe_tokeniser                    | 3.26 sec                                               | 2.75 sec: 1.19x faster                                                 |
| scimark_fft                      | 200 ms                                                 | 168 ms: 1.19x faster                                                   |
| async_generators                 | 294 ms                                                 | 248 ms: 1.18x faster                                                   |
| pickle_pure_python               | 215 us                                                 | 181 us: 1.18x faster                                                   |
| xml_etree_generate               | 57.1 ms                                                | 48.3 ms: 1.18x faster                                                  |
| crypto_pyaes                     | 55.3 ms                                                | 47.1 ms: 1.17x faster                                                  |
| chaos                            | 41.1 ms                                                | 35.0 ms: 1.17x faster                                                  |
| raytrace                         | 181 ms                                                 | 155 ms: 1.17x faster                                                   |
| sqlglot_optimize                 | 34.7 ms                                                | 29.8 ms: 1.16x faster                                                  |
| typing_runtime_protocols         | 101 us                                                 | 87.1 us: 1.16x faster                                                  |
| scimark_lu                       | 75.9 ms                                                | 65.9 ms: 1.15x faster                                                  |
| sympy_expand                     | 248 ms                                                 | 215 ms: 1.15x faster                                                   |
| sqlglot_normalize                | 188 ms                                                 | 164 ms: 1.14x faster                                                   |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 402 ms: 1.14x faster                                                   |
| thrift                           | 466 us                                                 | 408 us: 1.14x faster                                                   |
| sympy_str                        | 146 ms                                                 | 128 ms: 1.14x faster                                                   |
| pycparser                        | 701 ms                                                 | 616 ms: 1.14x faster                                                   |
| comprehensions                   | 12.0 us                                                | 10.5 us: 1.14x faster                                                  |
| fannkuch                         | 279 ms                                                 | 246 ms: 1.13x faster                                                   |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 2.64 ms: 1.13x faster                                                  |
| mako                             | 7.75 ms                                                | 6.92 ms: 1.12x faster                                                  |
| sphinx                           | 602 ms                                                 | 538 ms: 1.12x faster                                                   |
| sympy_integrate                  | 11.3 ms                                                | 10.1 ms: 1.12x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 402 ms: 1.12x faster                                                   |
| regex_effbot                     | 2.63 ms                                                | 2.36 ms: 1.11x faster                                                  |
| bench_thread_pool                | 503 us                                                 | 454 us: 1.11x faster                                                   |
| sympy_sum                        | 75.1 ms                                                | 68.4 ms: 1.10x faster                                                  |
| k_core                           | 1.61 sec                                               | 1.47 sec: 1.09x faster                                                 |
| sqlalchemy_imperative            | 6.69 ms                                                | 6.13 ms: 1.09x faster                                                  |
| telco                            | 4.84 ms                                                | 4.44 ms: 1.09x faster                                                  |
| dulwich_log                      | 28.7 ms                                                | 26.4 ms: 1.09x faster                                                  |
| bench_mp_pool                    | 64.7 ms                                                | 59.4 ms: 1.09x faster                                                  |
| sqlalchemy_declarative           | 59.0 ms                                                | 54.5 ms: 1.08x faster                                                  |
| xml_etree_parse                  | 108 ms                                                 | 99.8 ms: 1.08x faster                                                  |
| connected_components             | 319 ms                                                 | 295 ms: 1.08x faster                                                   |
| django_template                  | 20.5 ms                                                | 19.0 ms: 1.08x faster                                                  |
| xml_etree_iterparse              | 74.2 ms                                                | 69.0 ms: 1.08x faster                                                  |
| meteor_contest                   | 74.0 ms                                                | 68.9 ms: 1.07x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 348 ms: 1.07x faster                                                   |
| shortest_path                    | 345 ms                                                 | 323 ms: 1.07x faster                                                   |
| mdp                              | 1.50 sec                                               | 1.43 sec: 1.05x faster                                                 |
| sqlite_synth                     | 1.55 us                                                | 1.50 us: 1.04x faster                                                  |
| pathlib                          | 23.2 ms                                                | 22.5 ms: 1.03x faster                                                  |
| regex_dna                        | 149 ms                                                 | 146 ms: 1.02x faster                                                   |
| coverage                         | 46.2 ms                                                | 45.4 ms: 1.02x faster                                                  |
| docutils                         | 1.44 sec                                               | 1.42 sec: 1.01x faster                                                 |
| pidigits                         | 284 ms                                                 | 280 ms: 1.01x faster                                                   |
| dask                             | 771 ms                                                 | 768 ms: 1.00x faster                                                   |
| asyncio_websockets               | 242 ms                                                 | 242 ms: 1.00x faster                                                   |
| many_optionals                   | 409 us                                                 | 411 us: 1.00x slower                                                   |
| python_startup                   | 18.8 ms                                                | 19.2 ms: 1.02x slower                                                  |
| python_startup_no_site           | 13.7 ms                                                | 14.3 ms: 1.04x slower                                                  |
| 2to3                             | 179 ms                                                 | 186 ms: 1.04x slower                                                   |
| json_loads                       | 17.0 us                                                | 17.8 us: 1.05x slower                                                  |
| regex_v8                         | 17.0 ms                                                | 17.8 ms: 1.05x slower                                                  |
| gc_traversal                     | 2.94 ms                                                | 3.08 ms: 1.05x slower                                                  |
| create_gc_cycles                 | 1.19 ms                                                | 1.27 ms: 1.06x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 380 ms: 1.10x slower                                                   |
| json_dumps                       | 6.47 ms                                                | 7.09 ms: 1.10x slower                                                  |
| subparsers                       | 9.44 ms                                                | 11.3 ms: 1.19x slower                                                  |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 165 ms: 1.19x slower                                                   |
| async_tree_eager_tg              | 47.4 ms                                                | 122 ms: 2.58x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.16x faster                                                           |

Benchmark hidden because not significant (1): json
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.160x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.13x
- 95% likely to have a speedup of 1.12x
- 99% likely to have a speedup of 1.11x

# Memory
- memory change: 1.08x