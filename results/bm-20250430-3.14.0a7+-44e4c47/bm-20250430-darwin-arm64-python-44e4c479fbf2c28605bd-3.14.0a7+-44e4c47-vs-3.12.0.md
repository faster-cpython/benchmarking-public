# Results vs. 3.12.0

- fork: python
- ref: 44e4c479fbf2c28605bd
- machine: darwin-arm64
- commit hash: 44e4c47
- commit date: 2025-04-30
- overall geometric mean: 1.046x slower
- HPT reliability: 99.95%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250430-darwin-arm64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 190 ms: 1.13x slower                                                   |
| docutils       | 1.45 sec                                               | 1.55 sec: 1.07x slower                                                 |
| html5lib       | 33.4 ms                                                | 35.1 ms: 1.05x slower                                                  |
| sphinx         | 613 ms                                                 | 632 ms: 1.03x slower                                                   |
| Geometric mean | (ref)                                                  | 1.07x slower                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250430-darwin-arm64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_eager_io              | 666 ms                                                 | 410 ms: 1.63x faster                                                   |
| async_tree_io_tg                 | 673 ms                                                 | 418 ms: 1.61x faster                                                   |
| async_tree_io                    | 672 ms                                                 | 424 ms: 1.58x faster                                                   |
| async_tree_memoization_tg        | 318 ms                                                 | 210 ms: 1.51x faster                                                   |
| async_tree_eager_io_tg           | 617 ms                                                 | 409 ms: 1.51x faster                                                   |
| async_tree_none_tg               | 255 ms                                                 | 176 ms: 1.45x faster                                                   |
| async_tree_none                  | 263 ms                                                 | 191 ms: 1.38x faster                                                   |
| async_tree_memoization           | 310 ms                                                 | 229 ms: 1.36x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 430 ms: 1.23x faster                                                   |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 441 ms: 1.19x faster                                                   |
| async_tree_eager_memoization     | 168 ms                                                 | 154 ms: 1.09x faster                                                   |
| async_generators                 | 299 ms                                                 | 279 ms: 1.07x faster                                                   |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 402 ms: 1.16x slower                                                   |
| async_tree_eager                 | 65.8 ms                                                | 78.1 ms: 1.19x slower                                                  |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 189 ms: 1.34x slower                                                   |
| async_tree_eager_tg              | 46.9 ms                                                | 149 ms: 3.17x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.11x faster                                                           |

Benchmark hidden because not significant (3): asyncio_websockets, coroutines, async_tree_eager_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250430-darwin-arm64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pidigits       | 283 ms                                                 | 284 ms: 1.00x slower                                                   |
| float          | 54.1 ms                                                | 58.5 ms: 1.08x slower                                                  |
| nbody          | 67.6 ms                                                | 93.6 ms: 1.39x slower                                                  |
| Geometric mean | (ref)                                                  | 1.15x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250430-darwin-arm64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 2.44 ms                                                | 2.27 ms: 1.07x faster                                                  |
| regex_dna      | 143 ms                                                 | 141 ms: 1.01x faster                                                   |
| regex_v8       | 15.1 ms                                                | 15.9 ms: 1.06x slower                                                  |
| regex_compile  | 75.9 ms                                                | 86.5 ms: 1.14x slower                                                  |
| Geometric mean | (ref)                                                  | 1.03x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250430-darwin-arm64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_parse      | 108 ms                                                 | 106 ms: 1.02x faster                                                   |
| xml_etree_iterparse  | 75.5 ms                                                | 76.1 ms: 1.01x slower                                                  |
| json_loads           | 17.0 us                                                | 18.6 us: 1.09x slower                                                  |
| xml_etree_generate   | 55.4 ms                                                | 62.0 ms: 1.12x slower                                                  |
| tomli_loads          | 1.36 sec                                               | 1.52 sec: 1.12x slower                                                 |
| xml_etree_process    | 38.9 ms                                                | 45.7 ms: 1.18x slower                                                  |
| unpickle_pure_python | 145 us                                                 | 186 us: 1.28x slower                                                   |
| pickle_pure_python   | 197 us                                                 | 253 us: 1.29x slower                                                   |
| json_dumps           | 6.19 ms                                                | 8.13 ms: 1.31x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.15x slower                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250430-darwin-arm64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 17.8 ms                                                | 19.7 ms: 1.11x slower                                                  |
| python_startup_no_site | 13.2 ms                                                | 14.6 ms: 1.11x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.11x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250430-darwin-arm64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_xml      | 30.5 ms                                                | 37.5 ms: 1.23x slower                                                  |
| mako            | 7.44 ms                                                | 9.16 ms: 1.23x slower                                                  |
| genshi_text     | 14.7 ms                                                | 18.5 ms: 1.26x slower                                                  |
| django_template | 19.7 ms                                                | 26.2 ms: 1.33x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.26x slower                                                           |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250430-darwin-arm64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 13.7 ms: 2.35x faster                                                  |
| mdp                              | 1.49 sec                                               | 872 ms: 1.71x faster                                                   |
| async_tree_eager_io              | 666 ms                                                 | 410 ms: 1.63x faster                                                   |
| async_tree_io_tg                 | 673 ms                                                 | 418 ms: 1.61x faster                                                   |
| async_tree_io                    | 672 ms                                                 | 424 ms: 1.58x faster                                                   |
| async_tree_memoization_tg        | 318 ms                                                 | 210 ms: 1.51x faster                                                   |
| async_tree_eager_io_tg           | 617 ms                                                 | 409 ms: 1.51x faster                                                   |
| async_tree_none_tg               | 255 ms                                                 | 176 ms: 1.45x faster                                                   |
| async_tree_none                  | 263 ms                                                 | 191 ms: 1.38x faster                                                   |
| async_tree_memoization           | 310 ms                                                 | 229 ms: 1.36x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 430 ms: 1.23x faster                                                   |
| deepcopy                         | 226 us                                                 | 188 us: 1.20x faster                                                   |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 441 ms: 1.19x faster                                                   |
| k_core                           | 1.72 sec                                               | 1.55 sec: 1.11x faster                                                 |
| async_tree_eager_memoization     | 168 ms                                                 | 154 ms: 1.09x faster                                                   |
| deepcopy_memo                    | 26.0 us                                                | 24.0 us: 1.08x faster                                                  |
| regex_effbot                     | 2.44 ms                                                | 2.27 ms: 1.07x faster                                                  |
| dulwich_log                      | 29.2 ms                                                | 27.3 ms: 1.07x faster                                                  |
| async_generators                 | 299 ms                                                 | 279 ms: 1.07x faster                                                   |
| deepcopy_reduce                  | 2.01 us                                                | 1.97 us: 1.02x faster                                                  |
| xml_etree_parse                  | 108 ms                                                 | 106 ms: 1.02x faster                                                   |
| regex_dna                        | 143 ms                                                 | 141 ms: 1.01x faster                                                   |
| pidigits                         | 283 ms                                                 | 284 ms: 1.00x slower                                                   |
| xml_etree_iterparse              | 75.5 ms                                                | 76.1 ms: 1.01x slower                                                  |
| raytrace                         | 204 ms                                                 | 206 ms: 1.01x slower                                                   |
| bench_mp_pool                    | 65.5 ms                                                | 66.9 ms: 1.02x slower                                                  |
| spectral_norm                    | 76.5 ms                                                | 78.2 ms: 1.02x slower                                                  |
| bpe_tokeniser                    | 3.28 sec                                               | 3.36 sec: 1.02x slower                                                 |
| shortest_path                    | 331 ms                                                 | 339 ms: 1.03x slower                                                   |
| sphinx                           | 613 ms                                                 | 632 ms: 1.03x slower                                                   |
| pathlib                          | 24.7 ms                                                | 25.5 ms: 1.03x slower                                                  |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 3.25 ms: 1.03x slower                                                  |
| comprehensions                   | 14.0 us                                                | 14.5 us: 1.04x slower                                                  |
| connected_components             | 300 ms                                                 | 311 ms: 1.04x slower                                                   |
| sqlite_synth                     | 1.55 us                                                | 1.61 us: 1.04x slower                                                  |
| html5lib                         | 33.4 ms                                                | 35.1 ms: 1.05x slower                                                  |
| sympy_integrate                  | 11.1 ms                                                | 11.7 ms: 1.05x slower                                                  |
| regex_v8                         | 15.1 ms                                                | 15.9 ms: 1.06x slower                                                  |
| gc_traversal                     | 2.95 ms                                                | 3.12 ms: 1.06x slower                                                  |
| json                             | 3.00 ms                                                | 3.18 ms: 1.06x slower                                                  |
| generators                       | 29.4 ms                                                | 31.4 ms: 1.07x slower                                                  |
| docutils                         | 1.45 sec                                               | 1.55 sec: 1.07x slower                                                 |
| go                               | 98.5 ms                                                | 105 ms: 1.07x slower                                                   |
| sqlalchemy_declarative           | 61.9 ms                                                | 66.5 ms: 1.07x slower                                                  |
| float                            | 54.1 ms                                                | 58.5 ms: 1.08x slower                                                  |
| scimark_fft                      | 194 ms                                                 | 210 ms: 1.08x slower                                                   |
| json_loads                       | 17.0 us                                                | 18.6 us: 1.09x slower                                                  |
| sympy_sum                        | 76.2 ms                                                | 83.2 ms: 1.09x slower                                                  |
| logging_silent                   | 72.5 ns                                                | 79.9 ns: 1.10x slower                                                  |
| logging_simple                   | 3.60 us                                                | 3.98 us: 1.10x slower                                                  |
| logging_format                   | 3.90 us                                                | 4.30 us: 1.10x slower                                                  |
| scimark_sor                      | 85.8 ms                                                | 95.0 ms: 1.11x slower                                                  |
| python_startup                   | 17.8 ms                                                | 19.7 ms: 1.11x slower                                                  |
| python_startup_no_site           | 13.2 ms                                                | 14.6 ms: 1.11x slower                                                  |
| sympy_str                        | 144 ms                                                 | 160 ms: 1.11x slower                                                   |
| create_gc_cycles                 | 1.15 ms                                                | 1.28 ms: 1.12x slower                                                  |
| deltablue                        | 2.57 ms                                                | 2.86 ms: 1.12x slower                                                  |
| xml_etree_generate               | 55.4 ms                                                | 62.0 ms: 1.12x slower                                                  |
| tomli_loads                      | 1.36 sec                                               | 1.52 sec: 1.12x slower                                                 |
| chaos                            | 41.6 ms                                                | 46.7 ms: 1.12x slower                                                  |
| 2to3                             | 168 ms                                                 | 190 ms: 1.13x slower                                                   |
| pycparser                        | 673 ms                                                 | 758 ms: 1.13x slower                                                   |
| meteor_contest                   | 69.1 ms                                                | 77.9 ms: 1.13x slower                                                  |
| pyflate                          | 311 ms                                                 | 351 ms: 1.13x slower                                                   |
| scimark_lu                       | 73.5 ms                                                | 83.0 ms: 1.13x slower                                                  |
| sqlalchemy_imperative            | 6.60 ms                                                | 7.46 ms: 1.13x slower                                                  |
| regex_compile                    | 75.9 ms                                                | 86.5 ms: 1.14x slower                                                  |
| bench_thread_pool                | 483 us                                                 | 553 us: 1.14x slower                                                   |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 402 ms: 1.16x slower                                                   |
| sympy_expand                     | 233 ms                                                 | 271 ms: 1.16x slower                                                   |
| xml_etree_process                | 38.9 ms                                                | 45.7 ms: 1.18x slower                                                  |
| async_tree_eager                 | 65.8 ms                                                | 78.1 ms: 1.19x slower                                                  |
| pprint_pformat                   | 986 ms                                                 | 1.17 sec: 1.19x slower                                                 |
| pprint_safe_repr                 | 483 ms                                                 | 579 ms: 1.20x slower                                                   |
| crypto_pyaes                     | 51.4 ms                                                | 62.0 ms: 1.20x slower                                                  |
| scimark_monte_carlo              | 44.5 ms                                                | 54.0 ms: 1.21x slower                                                  |
| typing_runtime_protocols         | 91.5 us                                                | 112 us: 1.22x slower                                                   |
| genshi_xml                       | 30.5 ms                                                | 37.5 ms: 1.23x slower                                                  |
| mako                             | 7.44 ms                                                | 9.16 ms: 1.23x slower                                                  |
| many_optionals                   | 403 us                                                 | 497 us: 1.23x slower                                                   |
| hexiom                           | 4.38 ms                                                | 5.46 ms: 1.25x slower                                                  |
| genshi_text                      | 14.7 ms                                                | 18.5 ms: 1.26x slower                                                  |
| nqueens                          | 59.5 ms                                                | 75.3 ms: 1.26x slower                                                  |
| telco                            | 3.92 ms                                                | 4.97 ms: 1.27x slower                                                  |
| fannkuch                         | 250 ms                                                 | 318 ms: 1.27x slower                                                   |
| richards_super                   | 34.6 ms                                                | 44.0 ms: 1.27x slower                                                  |
| unpickle_pure_python             | 145 us                                                 | 186 us: 1.28x slower                                                   |
| pickle_pure_python               | 197 us                                                 | 253 us: 1.29x slower                                                   |
| richards                         | 30.6 ms                                                | 39.5 ms: 1.29x slower                                                  |
| coverage                         | 38.5 ms                                                | 50.4 ms: 1.31x slower                                                  |
| json_dumps                       | 6.19 ms                                                | 8.13 ms: 1.31x slower                                                  |
| django_template                  | 19.7 ms                                                | 26.2 ms: 1.33x slower                                                  |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 189 ms: 1.34x slower                                                   |
| nbody                            | 67.6 ms                                                | 93.6 ms: 1.39x slower                                                  |
| async_tree_eager_tg              | 46.9 ms                                                | 149 ms: 3.17x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.05x slower                                                           |

Benchmark hidden because not significant (4): pylint, asyncio_websockets, coroutines, async_tree_eager_cpu_io_mixed
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: chameleon, dask, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (4) of results/bm-20250430-3.14.0a7+-44e4c47/bm-20250430-darwin-arm64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.046x slower

# HPT report

- Reliability score: 99.95% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.10x