# Results vs. 3.12.0

- fork: python
- ref: 313b96eb8b8d0ad3bac5
- machine: darwin-arm64
- commit hash: 313b96e
- commit date: 2025-01-16
- overall geometric mean: 1.048x faster
- HPT reliability: 93.13%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250116-darwin-arm64-python-313b96eb8b8d0ad3bac5-3.14.0a4+-313b96e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| docutils       | 1.45 sec                                               | 1.44 sec: 1.01x faster                                                 |
| html5lib       | 33.4 ms                                                | 32.9 ms: 1.01x faster                                                  |
| sphinx         | 613 ms                                                 | 577 ms: 1.06x faster                                                   |
| Geometric mean | (ref)                                                  | 1.02x faster                                                           |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250116-darwin-arm64-python-313b96eb8b8d0ad3bac5-3.14.0a4+-313b96e |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg                 | 673 ms                                                 | 365 ms: 1.84x faster                                                   |
| async_tree_eager_io              | 666 ms                                                 | 373 ms: 1.78x faster                                                   |
| async_tree_io                    | 672 ms                                                 | 379 ms: 1.77x faster                                                   |
| async_tree_memoization_tg        | 318 ms                                                 | 193 ms: 1.65x faster                                                   |
| async_tree_eager_io_tg           | 617 ms                                                 | 377 ms: 1.64x faster                                                   |
| async_tree_none_tg               | 255 ms                                                 | 158 ms: 1.62x faster                                                   |
| async_tree_none                  | 263 ms                                                 | 170 ms: 1.55x faster                                                   |
| async_tree_memoization           | 310 ms                                                 | 209 ms: 1.48x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 411 ms: 1.29x faster                                                   |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 422 ms: 1.25x faster                                                   |
| coroutines                       | 19.7 ms                                                | 16.9 ms: 1.16x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 147 ms: 1.14x faster                                                   |
| async_generators                 | 299 ms                                                 | 266 ms: 1.12x faster                                                   |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 129 ms: 1.10x faster                                                   |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 363 ms: 1.03x faster                                                   |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 338 ms: 1.03x faster                                                   |
| asyncio_websockets               | 243 ms                                                 | 242 ms: 1.00x faster                                                   |
| async_tree_eager_tg              | 46.9 ms                                                | 49.0 ms: 1.04x slower                                                  |
| async_tree_eager                 | 65.8 ms                                                | 69.6 ms: 1.06x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.30x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250116-darwin-arm64-python-313b96eb8b8d0ad3bac5-3.14.0a4+-313b96e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 54.1 ms                                                | 51.5 ms: 1.05x faster                                                  |
| pidigits       | 283 ms                                                 | 280 ms: 1.01x faster                                                   |
| nbody          | 67.6 ms                                                | 83.0 ms: 1.23x slower                                                  |
| Geometric mean | (ref)                                                  | 1.05x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250116-darwin-arm64-python-313b96eb8b8d0ad3bac5-3.14.0a4+-313b96e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 2.44 ms                                                | 2.05 ms: 1.19x faster                                                  |
| regex_dna      | 143 ms                                                 | 138 ms: 1.03x faster                                                   |
| regex_compile  | 75.9 ms                                                | 77.5 ms: 1.02x slower                                                  |
| regex_v8       | 15.1 ms                                                | 17.0 ms: 1.13x slower                                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250116-darwin-arm64-python-313b96eb8b8d0ad3bac5-3.14.0a4+-313b96e |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_parse      | 108 ms                                                 | 103 ms: 1.05x faster                                                   |
| xml_etree_iterparse  | 75.5 ms                                                | 72.5 ms: 1.04x faster                                                  |
| json_loads           | 17.0 us                                                | 16.4 us: 1.04x faster                                                  |
| xml_etree_process    | 38.9 ms                                                | 41.1 ms: 1.06x slower                                                  |
| unpickle_pure_python | 145 us                                                 | 160 us: 1.10x slower                                                   |
| pickle_pure_python   | 197 us                                                 | 220 us: 1.12x slower                                                   |
| tomli_loads          | 1.36 sec                                               | 1.59 sec: 1.17x slower                                                 |
| json_dumps           | 6.19 ms                                                | 7.41 ms: 1.20x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.05x slower                                                           |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250116-darwin-arm64-python-313b96eb8b8d0ad3bac5-3.14.0a4+-313b96e |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 13.2 ms                                                | 12.2 ms: 1.08x faster                                                  |
| python_startup         | 17.8 ms                                                | 16.7 ms: 1.06x faster                                                  |
| Geometric mean         | (ref)                                                  | 1.07x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250116-darwin-arm64-python-313b96eb8b8d0ad3bac5-3.14.0a4+-313b96e |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 14.7 ms                                                | 15.8 ms: 1.08x slower                                                  |
| mako            | 7.44 ms                                                | 8.07 ms: 1.08x slower                                                  |
| genshi_xml      | 30.5 ms                                                | 33.2 ms: 1.09x slower                                                  |
| django_template | 19.7 ms                                                | 22.7 ms: 1.15x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.10x slower                                                           |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250116-darwin-arm64-python-313b96eb8b8d0ad3bac5-3.14.0a4+-313b96e |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 12.7 ms: 2.53x faster                                                  |
| async_tree_io_tg                 | 673 ms                                                 | 365 ms: 1.84x faster                                                   |
| async_tree_eager_io              | 666 ms                                                 | 373 ms: 1.78x faster                                                   |
| async_tree_io                    | 672 ms                                                 | 379 ms: 1.77x faster                                                   |
| async_tree_memoization_tg        | 318 ms                                                 | 193 ms: 1.65x faster                                                   |
| async_tree_eager_io_tg           | 617 ms                                                 | 377 ms: 1.64x faster                                                   |
| async_tree_none_tg               | 255 ms                                                 | 158 ms: 1.62x faster                                                   |
| async_tree_none                  | 263 ms                                                 | 170 ms: 1.55x faster                                                   |
| async_tree_memoization           | 310 ms                                                 | 209 ms: 1.48x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 411 ms: 1.29x faster                                                   |
| deepcopy                         | 226 us                                                 | 177 us: 1.28x faster                                                   |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 422 ms: 1.25x faster                                                   |
| deepcopy_memo                    | 26.0 us                                                | 21.7 us: 1.20x faster                                                  |
| regex_effbot                     | 2.44 ms                                                | 2.05 ms: 1.19x faster                                                  |
| raytrace                         | 204 ms                                                 | 175 ms: 1.17x faster                                                   |
| coroutines                       | 19.7 ms                                                | 16.9 ms: 1.16x faster                                                  |
| k_core                           | 1.72 sec                                               | 1.48 sec: 1.16x faster                                                 |
| generators                       | 29.4 ms                                                | 25.4 ms: 1.16x faster                                                  |
| deepcopy_reduce                  | 2.01 us                                                | 1.76 us: 1.14x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 147 ms: 1.14x faster                                                   |
| spectral_norm                    | 76.5 ms                                                | 67.7 ms: 1.13x faster                                                  |
| async_generators                 | 299 ms                                                 | 266 ms: 1.12x faster                                                   |
| pylint                           | 182 ms                                                 | 162 ms: 1.12x faster                                                   |
| bench_mp_pool                    | 65.5 ms                                                | 59.2 ms: 1.11x faster                                                  |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 129 ms: 1.10x faster                                                   |
| pathlib                          | 24.7 ms                                                | 22.8 ms: 1.09x faster                                                  |
| python_startup_no_site           | 13.2 ms                                                | 12.2 ms: 1.08x faster                                                  |
| deltablue                        | 2.57 ms                                                | 2.39 ms: 1.08x faster                                                  |
| comprehensions                   | 14.0 us                                                | 13.1 us: 1.07x faster                                                  |
| go                               | 98.5 ms                                                | 92.6 ms: 1.06x faster                                                  |
| python_startup                   | 17.8 ms                                                | 16.7 ms: 1.06x faster                                                  |
| sphinx                           | 613 ms                                                 | 577 ms: 1.06x faster                                                   |
| json                             | 3.00 ms                                                | 2.85 ms: 1.06x faster                                                  |
| logging_format                   | 3.90 us                                                | 3.71 us: 1.05x faster                                                  |
| xml_etree_parse                  | 108 ms                                                 | 103 ms: 1.05x faster                                                   |
| float                            | 54.1 ms                                                | 51.5 ms: 1.05x faster                                                  |
| logging_simple                   | 3.60 us                                                | 3.43 us: 1.05x faster                                                  |
| xml_etree_iterparse              | 75.5 ms                                                | 72.5 ms: 1.04x faster                                                  |
| json_loads                       | 17.0 us                                                | 16.4 us: 1.04x faster                                                  |
| thrift                           | 468 us                                                 | 450 us: 1.04x faster                                                   |
| regex_dna                        | 143 ms                                                 | 138 ms: 1.03x faster                                                   |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 363 ms: 1.03x faster                                                   |
| dulwich_log                      | 29.2 ms                                                | 28.4 ms: 1.03x faster                                                  |
| bpe_tokeniser                    | 3.28 sec                                               | 3.20 sec: 1.03x faster                                                 |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 338 ms: 1.03x faster                                                   |
| shortest_path                    | 331 ms                                                 | 324 ms: 1.02x faster                                                   |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 3.08 ms: 1.02x faster                                                  |
| logging_silent                   | 72.5 ns                                                | 71.3 ns: 1.02x faster                                                  |
| html5lib                         | 33.4 ms                                                | 32.9 ms: 1.01x faster                                                  |
| sqlalchemy_declarative           | 61.9 ms                                                | 61.2 ms: 1.01x faster                                                  |
| dask                             | 779 ms                                                 | 771 ms: 1.01x faster                                                   |
| scimark_fft                      | 194 ms                                                 | 192 ms: 1.01x faster                                                   |
| pidigits                         | 283 ms                                                 | 280 ms: 1.01x faster                                                   |
| connected_components             | 300 ms                                                 | 297 ms: 1.01x faster                                                   |
| docutils                         | 1.45 sec                                               | 1.44 sec: 1.01x faster                                                 |
| asyncio_websockets               | 243 ms                                                 | 242 ms: 1.00x faster                                                   |
| sqlite_synth                     | 1.55 us                                                | 1.56 us: 1.01x slower                                                  |
| sympy_sum                        | 76.2 ms                                                | 77.3 ms: 1.01x slower                                                  |
| mdp                              | 1.49 sec                                               | 1.52 sec: 1.02x slower                                                 |
| nqueens                          | 59.5 ms                                                | 60.6 ms: 1.02x slower                                                  |
| chaos                            | 41.6 ms                                                | 42.4 ms: 1.02x slower                                                  |
| sympy_str                        | 144 ms                                                 | 147 ms: 1.02x slower                                                   |
| scimark_lu                       | 73.5 ms                                                | 74.9 ms: 1.02x slower                                                  |
| regex_compile                    | 75.9 ms                                                | 77.5 ms: 1.02x slower                                                  |
| crypto_pyaes                     | 51.4 ms                                                | 52.8 ms: 1.03x slower                                                  |
| pycparser                        | 673 ms                                                 | 692 ms: 1.03x slower                                                   |
| bench_thread_pool                | 483 us                                                 | 498 us: 1.03x slower                                                   |
| sqlglot_parse                    | 808 us                                                 | 837 us: 1.04x slower                                                   |
| sqlglot_optimize                 | 33.2 ms                                                | 34.4 ms: 1.04x slower                                                  |
| sqlglot_transpile                | 973 us                                                 | 1.01 ms: 1.04x slower                                                  |
| pyflate                          | 311 ms                                                 | 324 ms: 1.04x slower                                                   |
| async_tree_eager_tg              | 46.9 ms                                                | 49.0 ms: 1.04x slower                                                  |
| sqlglot_normalize                | 180 ms                                                 | 188 ms: 1.05x slower                                                   |
| scimark_sor                      | 85.8 ms                                                | 90.3 ms: 1.05x slower                                                  |
| sympy_expand                     | 233 ms                                                 | 246 ms: 1.05x slower                                                   |
| gc_traversal                     | 2.95 ms                                                | 3.11 ms: 1.06x slower                                                  |
| async_tree_eager                 | 65.8 ms                                                | 69.6 ms: 1.06x slower                                                  |
| xml_etree_process                | 38.9 ms                                                | 41.1 ms: 1.06x slower                                                  |
| richards_super                   | 34.6 ms                                                | 36.9 ms: 1.07x slower                                                  |
| scimark_monte_carlo              | 44.5 ms                                                | 47.7 ms: 1.07x slower                                                  |
| genshi_text                      | 14.7 ms                                                | 15.8 ms: 1.08x slower                                                  |
| mako                             | 7.44 ms                                                | 8.07 ms: 1.08x slower                                                  |
| hexiom                           | 4.38 ms                                                | 4.76 ms: 1.09x slower                                                  |
| genshi_xml                       | 30.5 ms                                                | 33.2 ms: 1.09x slower                                                  |
| richards                         | 30.6 ms                                                | 33.4 ms: 1.09x slower                                                  |
| create_gc_cycles                 | 1.15 ms                                                | 1.27 ms: 1.10x slower                                                  |
| unpickle_pure_python             | 145 us                                                 | 160 us: 1.10x slower                                                   |
| meteor_contest                   | 69.1 ms                                                | 76.7 ms: 1.11x slower                                                  |
| pickle_pure_python               | 197 us                                                 | 220 us: 1.12x slower                                                   |
| pprint_pformat                   | 986 ms                                                 | 1.11 sec: 1.12x slower                                                 |
| sqlalchemy_imperative            | 6.60 ms                                                | 7.45 ms: 1.13x slower                                                  |
| regex_v8                         | 15.1 ms                                                | 17.0 ms: 1.13x slower                                                  |
| typing_runtime_protocols         | 91.5 us                                                | 104 us: 1.13x slower                                                   |
| pprint_safe_repr                 | 483 ms                                                 | 547 ms: 1.13x slower                                                   |
| django_template                  | 19.7 ms                                                | 22.7 ms: 1.15x slower                                                  |
| many_optionals                   | 403 us                                                 | 467 us: 1.16x slower                                                   |
| coverage                         | 38.5 ms                                                | 44.7 ms: 1.16x slower                                                  |
| tomli_loads                      | 1.36 sec                                               | 1.59 sec: 1.17x slower                                                 |
| telco                            | 3.92 ms                                                | 4.69 ms: 1.20x slower                                                  |
| json_dumps                       | 6.19 ms                                                | 7.41 ms: 1.20x slower                                                  |
| nbody                            | 67.6 ms                                                | 83.0 ms: 1.23x slower                                                  |
| fannkuch                         | 250 ms                                                 | 315 ms: 1.26x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.05x faster                                                           |

Benchmark hidden because not significant (3): 2to3, xml_etree_generate, sympy_integrate
Ignored benchmarks (5) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.048x faster

# HPT report

- Reliability score: 93.13% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x