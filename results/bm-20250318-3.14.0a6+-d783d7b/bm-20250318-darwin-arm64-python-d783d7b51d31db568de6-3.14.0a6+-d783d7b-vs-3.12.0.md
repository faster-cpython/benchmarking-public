# Results vs. 3.12.0

- fork: python
- ref: d783d7b51d31db568de6
- machine: darwin-arm64
- commit hash: d783d7b
- commit date: 2025-03-18
- overall geometric mean: 1.069x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250318-darwin-arm64-python-d783d7b51d31db568de6-3.14.0a6+-d783d7b |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 162 ms: 1.04x faster                                                   |
| docutils       | 1.45 sec                                               | 1.45 sec: 1.01x faster                                                 |
| html5lib       | 33.4 ms                                                | 29.8 ms: 1.12x faster                                                  |
| sphinx         | 613 ms                                                 | 582 ms: 1.05x faster                                                   |
| Geometric mean | (ref)                                                  | 1.05x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250318-darwin-arm64-python-d783d7b51d31db568de6-3.14.0a6+-d783d7b |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg                 | 673 ms                                                 | 366 ms: 1.84x faster                                                   |
| async_tree_eager_io              | 666 ms                                                 | 363 ms: 1.84x faster                                                   |
| async_tree_io                    | 672 ms                                                 | 377 ms: 1.78x faster                                                   |
| async_tree_eager_io_tg           | 617 ms                                                 | 375 ms: 1.65x faster                                                   |
| async_tree_none_tg               | 255 ms                                                 | 156 ms: 1.64x faster                                                   |
| async_tree_none                  | 263 ms                                                 | 161 ms: 1.64x faster                                                   |
| async_tree_memoization_tg        | 318 ms                                                 | 196 ms: 1.62x faster                                                   |
| async_tree_memoization           | 310 ms                                                 | 197 ms: 1.57x faster                                                   |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 411 ms: 1.28x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 414 ms: 1.28x faster                                                   |
| coroutines                       | 19.7 ms                                                | 16.4 ms: 1.20x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 142 ms: 1.18x faster                                                   |
| async_generators                 | 299 ms                                                 | 257 ms: 1.16x faster                                                   |
| async_tree_eager                 | 65.8 ms                                                | 61.2 ms: 1.07x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 357 ms: 1.05x faster                                                   |
| asyncio_websockets               | 243 ms                                                 | 242 ms: 1.00x faster                                                   |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 392 ms: 1.13x slower                                                   |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 175 ms: 1.23x slower                                                   |
| async_tree_eager_tg              | 46.9 ms                                                | 130 ms: 2.77x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.23x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250318-darwin-arm64-python-d783d7b51d31db568de6-3.14.0a6+-d783d7b |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 54.1 ms                                                | 47.7 ms: 1.13x faster                                                  |
| pidigits       | 283 ms                                                 | 283 ms: 1.00x slower                                                   |
| nbody          | 67.6 ms                                                | 72.9 ms: 1.08x slower                                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250318-darwin-arm64-python-d783d7b51d31db568de6-3.14.0a6+-d783d7b |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 75.9 ms                                                | 68.8 ms: 1.10x faster                                                  |
| regex_effbot   | 2.44 ms                                                | 2.27 ms: 1.08x faster                                                  |
| regex_dna      | 143 ms                                                 | 141 ms: 1.01x faster                                                   |
| regex_v8       | 15.1 ms                                                | 15.9 ms: 1.05x slower                                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250318-darwin-arm64-python-d783d7b51d31db568de6-3.14.0a6+-d783d7b |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 1.36 sec                                               | 1.24 sec: 1.09x faster                                                 |
| xml_etree_iterparse  | 75.5 ms                                                | 71.7 ms: 1.05x faster                                                  |
| xml_etree_parse      | 108 ms                                                 | 104 ms: 1.04x faster                                                   |
| xml_etree_generate   | 55.4 ms                                                | 53.7 ms: 1.03x faster                                                  |
| xml_etree_process    | 38.9 ms                                                | 38.9 ms: 1.00x slower                                                  |
| unpickle_pure_python | 145 us                                                 | 149 us: 1.02x slower                                                   |
| pickle_pure_python   | 197 us                                                 | 205 us: 1.04x slower                                                   |
| json_loads           | 17.0 us                                                | 17.9 us: 1.05x slower                                                  |
| json_dumps           | 6.19 ms                                                | 7.30 ms: 1.18x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250318-darwin-arm64-python-d783d7b51d31db568de6-3.14.0a6+-d783d7b |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup | 17.8 ms                                                | 17.4 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                                           |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250318-darwin-arm64-python-d783d7b51d31db568de6-3.14.0a6+-d783d7b |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_xml      | 30.5 ms                                                | 28.9 ms: 1.05x faster                                                  |
| genshi_text     | 14.7 ms                                                | 14.1 ms: 1.04x faster                                                  |
| mako            | 7.44 ms                                                | 7.60 ms: 1.02x slower                                                  |
| django_template | 19.7 ms                                                | 21.2 ms: 1.08x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.00x slower                                                           |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250318-darwin-arm64-python-d783d7b51d31db568de6-3.14.0a6+-d783d7b |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 12.2 ms: 2.64x faster                                                  |
| async_tree_io_tg                 | 673 ms                                                 | 366 ms: 1.84x faster                                                   |
| async_tree_eager_io              | 666 ms                                                 | 363 ms: 1.84x faster                                                   |
| async_tree_io                    | 672 ms                                                 | 377 ms: 1.78x faster                                                   |
| async_tree_eager_io_tg           | 617 ms                                                 | 375 ms: 1.65x faster                                                   |
| async_tree_none_tg               | 255 ms                                                 | 156 ms: 1.64x faster                                                   |
| async_tree_none                  | 263 ms                                                 | 161 ms: 1.64x faster                                                   |
| async_tree_memoization_tg        | 318 ms                                                 | 196 ms: 1.62x faster                                                   |
| async_tree_memoization           | 310 ms                                                 | 197 ms: 1.57x faster                                                   |
| deepcopy                         | 226 us                                                 | 151 us: 1.50x faster                                                   |
| deepcopy_memo                    | 26.0 us                                                | 18.4 us: 1.42x faster                                                  |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 411 ms: 1.28x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 414 ms: 1.28x faster                                                   |
| deepcopy_reduce                  | 2.01 us                                                | 1.62 us: 1.24x faster                                                  |
| generators                       | 29.4 ms                                                | 24.2 ms: 1.21x faster                                                  |
| comprehensions                   | 14.0 us                                                | 11.6 us: 1.21x faster                                                  |
| coroutines                       | 19.7 ms                                                | 16.4 ms: 1.20x faster                                                  |
| go                               | 98.5 ms                                                | 82.2 ms: 1.20x faster                                                  |
| dulwich_log                      | 29.2 ms                                                | 24.6 ms: 1.19x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 142 ms: 1.18x faster                                                   |
| async_generators                 | 299 ms                                                 | 257 ms: 1.16x faster                                                   |
| float                            | 54.1 ms                                                | 47.7 ms: 1.13x faster                                                  |
| raytrace                         | 204 ms                                                 | 182 ms: 1.12x faster                                                   |
| html5lib                         | 33.4 ms                                                | 29.8 ms: 1.12x faster                                                  |
| pylint                           | 182 ms                                                 | 163 ms: 1.11x faster                                                   |
| k_core                           | 1.72 sec                                               | 1.55 sec: 1.11x faster                                                 |
| regex_compile                    | 75.9 ms                                                | 68.8 ms: 1.10x faster                                                  |
| logging_silent                   | 72.5 ns                                                | 66.2 ns: 1.10x faster                                                  |
| tomli_loads                      | 1.36 sec                                               | 1.24 sec: 1.09x faster                                                 |
| logging_simple                   | 3.60 us                                                | 3.32 us: 1.09x faster                                                  |
| scimark_sor                      | 85.8 ms                                                | 79.1 ms: 1.08x faster                                                  |
| bench_mp_pool                    | 65.5 ms                                                | 60.8 ms: 1.08x faster                                                  |
| logging_format                   | 3.90 us                                                | 3.62 us: 1.08x faster                                                  |
| regex_effbot                     | 2.44 ms                                                | 2.27 ms: 1.08x faster                                                  |
| async_tree_eager                 | 65.8 ms                                                | 61.2 ms: 1.07x faster                                                  |
| deltablue                        | 2.57 ms                                                | 2.39 ms: 1.07x faster                                                  |
| thrift                           | 468 us                                                 | 440 us: 1.06x faster                                                   |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 2.96 ms: 1.06x faster                                                  |
| scimark_fft                      | 194 ms                                                 | 184 ms: 1.06x faster                                                   |
| genshi_xml                       | 30.5 ms                                                | 28.9 ms: 1.05x faster                                                  |
| xml_etree_iterparse              | 75.5 ms                                                | 71.7 ms: 1.05x faster                                                  |
| sphinx                           | 613 ms                                                 | 582 ms: 1.05x faster                                                   |
| sqlalchemy_declarative           | 61.9 ms                                                | 58.9 ms: 1.05x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 357 ms: 1.05x faster                                                   |
| xml_etree_parse                  | 108 ms                                                 | 104 ms: 1.04x faster                                                   |
| 2to3                             | 168 ms                                                 | 162 ms: 1.04x faster                                                   |
| pprint_pformat                   | 986 ms                                                 | 948 ms: 1.04x faster                                                   |
| genshi_text                      | 14.7 ms                                                | 14.1 ms: 1.04x faster                                                  |
| pathlib                          | 24.7 ms                                                | 23.8 ms: 1.04x faster                                                  |
| pprint_safe_repr                 | 483 ms                                                 | 467 ms: 1.03x faster                                                   |
| xml_etree_generate               | 55.4 ms                                                | 53.7 ms: 1.03x faster                                                  |
| scimark_monte_carlo              | 44.5 ms                                                | 43.3 ms: 1.03x faster                                                  |
| bpe_tokeniser                    | 3.28 sec                                               | 3.20 sec: 1.03x faster                                                 |
| sympy_sum                        | 76.2 ms                                                | 74.3 ms: 1.03x faster                                                  |
| python_startup                   | 17.8 ms                                                | 17.4 ms: 1.02x faster                                                  |
| pycparser                        | 673 ms                                                 | 663 ms: 1.02x faster                                                   |
| dask                             | 779 ms                                                 | 767 ms: 1.01x faster                                                   |
| sympy_str                        | 144 ms                                                 | 142 ms: 1.01x faster                                                   |
| regex_dna                        | 143 ms                                                 | 141 ms: 1.01x faster                                                   |
| spectral_norm                    | 76.5 ms                                                | 75.7 ms: 1.01x faster                                                  |
| chaos                            | 41.6 ms                                                | 41.4 ms: 1.01x faster                                                  |
| docutils                         | 1.45 sec                                               | 1.45 sec: 1.01x faster                                                 |
| asyncio_websockets               | 243 ms                                                 | 242 ms: 1.00x faster                                                   |
| mdp                              | 1.49 sec                                               | 1.49 sec: 1.00x faster                                                 |
| xml_etree_process                | 38.9 ms                                                | 38.9 ms: 1.00x slower                                                  |
| pidigits                         | 283 ms                                                 | 283 ms: 1.00x slower                                                   |
| shortest_path                    | 331 ms                                                 | 334 ms: 1.01x slower                                                   |
| sympy_expand                     | 233 ms                                                 | 236 ms: 1.01x slower                                                   |
| bench_thread_pool                | 483 us                                                 | 490 us: 1.01x slower                                                   |
| hexiom                           | 4.38 ms                                                | 4.44 ms: 1.01x slower                                                  |
| scimark_lu                       | 73.5 ms                                                | 74.6 ms: 1.02x slower                                                  |
| mako                             | 7.44 ms                                                | 7.60 ms: 1.02x slower                                                  |
| typing_runtime_protocols         | 91.5 us                                                | 93.6 us: 1.02x slower                                                  |
| unpickle_pure_python             | 145 us                                                 | 149 us: 1.02x slower                                                   |
| connected_components             | 300 ms                                                 | 308 ms: 1.03x slower                                                   |
| pyflate                          | 311 ms                                                 | 320 ms: 1.03x slower                                                   |
| sympy_integrate                  | 11.1 ms                                                | 11.5 ms: 1.04x slower                                                  |
| json                             | 3.00 ms                                                | 3.13 ms: 1.04x slower                                                  |
| pickle_pure_python               | 197 us                                                 | 205 us: 1.04x slower                                                   |
| json_loads                       | 17.0 us                                                | 17.9 us: 1.05x slower                                                  |
| regex_v8                         | 15.1 ms                                                | 15.9 ms: 1.05x slower                                                  |
| gc_traversal                     | 2.95 ms                                                | 3.11 ms: 1.06x slower                                                  |
| meteor_contest                   | 69.1 ms                                                | 73.0 ms: 1.06x slower                                                  |
| django_template                  | 19.7 ms                                                | 21.2 ms: 1.08x slower                                                  |
| nbody                            | 67.6 ms                                                | 72.9 ms: 1.08x slower                                                  |
| richards_super                   | 34.6 ms                                                | 37.6 ms: 1.09x slower                                                  |
| richards                         | 30.6 ms                                                | 33.4 ms: 1.09x slower                                                  |
| nqueens                          | 59.5 ms                                                | 65.3 ms: 1.10x slower                                                  |
| fannkuch                         | 250 ms                                                 | 277 ms: 1.11x slower                                                   |
| many_optionals                   | 403 us                                                 | 448 us: 1.11x slower                                                   |
| create_gc_cycles                 | 1.15 ms                                                | 1.29 ms: 1.12x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 392 ms: 1.13x slower                                                   |
| crypto_pyaes                     | 51.4 ms                                                | 58.3 ms: 1.13x slower                                                  |
| telco                            | 3.92 ms                                                | 4.58 ms: 1.17x slower                                                  |
| json_dumps                       | 6.19 ms                                                | 7.30 ms: 1.18x slower                                                  |
| coverage                         | 38.5 ms                                                | 45.7 ms: 1.19x slower                                                  |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 175 ms: 1.23x slower                                                   |
| async_tree_eager_tg              | 46.9 ms                                                | 130 ms: 2.77x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.07x faster                                                           |

Benchmark hidden because not significant (3): sqlite_synth, sqlalchemy_imperative, python_startup_no_site
Ignored benchmarks (9) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250318-3.14.0a6+-d783d7b/bm-20250318-darwin-arm64-python-d783d7b51d31db568de6-3.14.0a6+-d783d7b.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.069x faster

# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.11x