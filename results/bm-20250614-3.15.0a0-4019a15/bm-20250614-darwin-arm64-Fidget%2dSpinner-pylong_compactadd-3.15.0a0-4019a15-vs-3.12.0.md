# Results vs. 3.12.0

- fork: Fidget-Spinner
- ref: pylong_compactadd
- machine: darwin-arm64
- commit hash: 4019a15
- commit date: 2025-06-14
- overall geometric mean: 1.010x slower
- HPT reliability: 92.72%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250614-darwin-arm64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 170 ms: 1.01x slower                                                         |
| docutils       | 1.45 sec                                               | 1.44 sec: 1.01x faster                                                       |
| html5lib       | 33.4 ms                                                | 31.7 ms: 1.05x faster                                                        |
| sphinx         | 613 ms                                                 | 584 ms: 1.05x faster                                                         |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250614-darwin-arm64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_eager_io              | 666 ms                                                 | 364 ms: 1.83x faster                                                         |
| async_tree_io_tg                 | 673 ms                                                 | 375 ms: 1.79x faster                                                         |
| async_tree_io                    | 672 ms                                                 | 380 ms: 1.77x faster                                                         |
| async_tree_memoization_tg        | 318 ms                                                 | 192 ms: 1.66x faster                                                         |
| async_tree_eager_io_tg           | 617 ms                                                 | 374 ms: 1.65x faster                                                         |
| async_tree_none_tg               | 255 ms                                                 | 157 ms: 1.62x faster                                                         |
| async_tree_none                  | 263 ms                                                 | 165 ms: 1.60x faster                                                         |
| async_tree_memoization           | 310 ms                                                 | 196 ms: 1.59x faster                                                         |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 411 ms: 1.28x faster                                                         |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 418 ms: 1.26x faster                                                         |
| async_tree_eager_memoization     | 168 ms                                                 | 140 ms: 1.20x faster                                                         |
| coroutines                       | 19.7 ms                                                | 17.1 ms: 1.15x faster                                                        |
| async_generators                 | 299 ms                                                 | 262 ms: 1.14x faster                                                         |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 357 ms: 1.05x faster                                                         |
| async_tree_eager                 | 65.8 ms                                                | 64.1 ms: 1.03x faster                                                        |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 389 ms: 1.12x slower                                                         |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 168 ms: 1.19x slower                                                         |
| async_tree_eager_tg              | 46.9 ms                                                | 129 ms: 2.76x slower                                                         |
| Geometric mean                   | (ref)                                                  | 1.23x faster                                                                 |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250614-darwin-arm64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 54.1 ms                                                | 49.6 ms: 1.09x faster                                                        |
| pidigits       | 283 ms                                                 | 283 ms: 1.00x slower                                                         |
| nbody          | 67.6 ms                                                | 73.8 ms: 1.09x slower                                                        |
| Geometric mean | (ref)                                                  | 1.00x slower                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250614-darwin-arm64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 75.9 ms                                                | 71.8 ms: 1.06x faster                                                        |
| regex_effbot   | 2.44 ms                                                | 2.35 ms: 1.04x faster                                                        |
| regex_v8       | 15.1 ms                                                | 16.1 ms: 1.07x slower                                                        |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                 |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250614-darwin-arm64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_parse      | 108 ms                                                 | 103 ms: 1.04x faster                                                         |
| xml_etree_iterparse  | 75.5 ms                                                | 72.7 ms: 1.04x faster                                                        |
| json_loads           | 17.0 us                                                | 16.5 us: 1.03x faster                                                        |
| xml_etree_generate   | 55.4 ms                                                | 53.7 ms: 1.03x faster                                                        |
| tomli_loads          | 1.36 sec                                               | 1.36 sec: 1.01x slower                                                       |
| json_dumps           | 6.19 ms                                                | 6.54 ms: 1.06x slower                                                        |
| unpickle_pure_python | 145 us                                                 | 160 us: 1.10x slower                                                         |
| pickle_pure_python   | 197 us                                                 | 218 us: 1.11x slower                                                         |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                                 |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250614-darwin-arm64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 13.2 ms                                                | 11.6 ms: 1.14x faster                                                        |
| python_startup         | 17.8 ms                                                | 15.9 ms: 1.12x faster                                                        |
| Geometric mean         | (ref)                                                  | 1.13x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250614-darwin-arm64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_text     | 14.7 ms                                                | 14.6 ms: 1.01x faster                                                        |
| genshi_xml      | 30.5 ms                                                | 31.2 ms: 1.02x slower                                                        |
| mako            | 7.44 ms                                                | 7.72 ms: 1.04x slower                                                        |
| django_template | 19.7 ms                                                | 22.0 ms: 1.12x slower                                                        |
| Geometric mean  | (ref)                                                  | 1.04x slower                                                                 |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250614-darwin-arm64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 13.7 ms: 2.35x faster                                                        |
| mdp                              | 1.49 sec                                               | 761 ms: 1.96x faster                                                         |
| async_tree_eager_io              | 666 ms                                                 | 364 ms: 1.83x faster                                                         |
| async_tree_io_tg                 | 673 ms                                                 | 375 ms: 1.79x faster                                                         |
| async_tree_io                    | 672 ms                                                 | 380 ms: 1.77x faster                                                         |
| async_tree_memoization_tg        | 318 ms                                                 | 192 ms: 1.66x faster                                                         |
| async_tree_eager_io_tg           | 617 ms                                                 | 374 ms: 1.65x faster                                                         |
| async_tree_none_tg               | 255 ms                                                 | 157 ms: 1.62x faster                                                         |
| async_tree_none                  | 263 ms                                                 | 165 ms: 1.60x faster                                                         |
| async_tree_memoization           | 310 ms                                                 | 196 ms: 1.59x faster                                                         |
| deepcopy                         | 226 us                                                 | 156 us: 1.45x faster                                                         |
| deepcopy_memo                    | 26.0 us                                                | 19.2 us: 1.36x faster                                                        |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 411 ms: 1.28x faster                                                         |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 418 ms: 1.26x faster                                                         |
| generators                       | 29.4 ms                                                | 24.1 ms: 1.22x faster                                                        |
| async_tree_eager_memoization     | 168 ms                                                 | 140 ms: 1.20x faster                                                         |
| deepcopy_reduce                  | 2.01 us                                                | 1.69 us: 1.20x faster                                                        |
| dulwich_log                      | 29.2 ms                                                | 25.0 ms: 1.17x faster                                                        |
| k_core                           | 1.72 sec                                               | 1.47 sec: 1.17x faster                                                       |
| comprehensions                   | 14.0 us                                                | 12.0 us: 1.17x faster                                                        |
| coroutines                       | 19.7 ms                                                | 17.1 ms: 1.15x faster                                                        |
| async_generators                 | 299 ms                                                 | 262 ms: 1.14x faster                                                         |
| python_startup_no_site           | 13.2 ms                                                | 11.6 ms: 1.14x faster                                                        |
| raytrace                         | 204 ms                                                 | 180 ms: 1.13x faster                                                         |
| pylint                           | 182 ms                                                 | 161 ms: 1.13x faster                                                         |
| go                               | 98.5 ms                                                | 87.6 ms: 1.12x faster                                                        |
| python_startup                   | 17.8 ms                                                | 15.9 ms: 1.12x faster                                                        |
| float                            | 54.1 ms                                                | 49.6 ms: 1.09x faster                                                        |
| spectral_norm                    | 76.5 ms                                                | 70.7 ms: 1.08x faster                                                        |
| bpe_tokeniser                    | 3.28 sec                                               | 3.08 sec: 1.07x faster                                                       |
| regex_compile                    | 75.9 ms                                                | 71.8 ms: 1.06x faster                                                        |
| html5lib                         | 33.4 ms                                                | 31.7 ms: 1.05x faster                                                        |
| sphinx                           | 613 ms                                                 | 584 ms: 1.05x faster                                                         |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 357 ms: 1.05x faster                                                         |
| xml_etree_parse                  | 108 ms                                                 | 103 ms: 1.04x faster                                                         |
| regex_effbot                     | 2.44 ms                                                | 2.35 ms: 1.04x faster                                                        |
| chaos                            | 41.6 ms                                                | 40.1 ms: 1.04x faster                                                        |
| xml_etree_iterparse              | 75.5 ms                                                | 72.7 ms: 1.04x faster                                                        |
| pathlib                          | 24.7 ms                                                | 23.9 ms: 1.03x faster                                                        |
| json_loads                       | 17.0 us                                                | 16.5 us: 1.03x faster                                                        |
| xml_etree_generate               | 55.4 ms                                                | 53.7 ms: 1.03x faster                                                        |
| async_tree_eager                 | 65.8 ms                                                | 64.1 ms: 1.03x faster                                                        |
| json                             | 3.00 ms                                                | 2.94 ms: 1.02x faster                                                        |
| dask                             | 779 ms                                                 | 769 ms: 1.01x faster                                                         |
| sympy_sum                        | 76.2 ms                                                | 75.5 ms: 1.01x faster                                                        |
| docutils                         | 1.45 sec                                               | 1.44 sec: 1.01x faster                                                       |
| genshi_text                      | 14.7 ms                                                | 14.6 ms: 1.01x faster                                                        |
| sympy_str                        | 144 ms                                                 | 143 ms: 1.01x faster                                                         |
| sympy_integrate                  | 11.1 ms                                                | 11.0 ms: 1.00x faster                                                        |
| pidigits                         | 283 ms                                                 | 283 ms: 1.00x slower                                                         |
| deltablue                        | 2.57 ms                                                | 2.58 ms: 1.00x slower                                                        |
| scimark_fft                      | 194 ms                                                 | 195 ms: 1.01x slower                                                         |
| tomli_loads                      | 1.36 sec                                               | 1.36 sec: 1.01x slower                                                       |
| 2to3                             | 168 ms                                                 | 170 ms: 1.01x slower                                                         |
| pyflate                          | 311 ms                                                 | 317 ms: 1.02x slower                                                         |
| logging_simple                   | 3.60 us                                                | 3.68 us: 1.02x slower                                                        |
| connected_components             | 300 ms                                                 | 307 ms: 1.02x slower                                                         |
| genshi_xml                       | 30.5 ms                                                | 31.2 ms: 1.02x slower                                                        |
| logging_format                   | 3.90 us                                                | 4.00 us: 1.03x slower                                                        |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 3.23 ms: 1.03x slower                                                        |
| sympy_expand                     | 233 ms                                                 | 240 ms: 1.03x slower                                                         |
| nqueens                          | 59.5 ms                                                | 61.5 ms: 1.03x slower                                                        |
| scimark_sor                      | 85.8 ms                                                | 88.7 ms: 1.03x slower                                                        |
| mako                             | 7.44 ms                                                | 7.72 ms: 1.04x slower                                                        |
| sqlite_synth                     | 1.55 us                                                | 1.60 us: 1.04x slower                                                        |
| scimark_monte_carlo              | 44.5 ms                                                | 46.2 ms: 1.04x slower                                                        |
| typing_runtime_protocols         | 91.5 us                                                | 95.9 us: 1.05x slower                                                        |
| json_dumps                       | 6.19 ms                                                | 6.54 ms: 1.06x slower                                                        |
| fannkuch                         | 250 ms                                                 | 266 ms: 1.06x slower                                                         |
| meteor_contest                   | 69.1 ms                                                | 73.7 ms: 1.07x slower                                                        |
| regex_v8                         | 15.1 ms                                                | 16.1 ms: 1.07x slower                                                        |
| hexiom                           | 4.38 ms                                                | 4.68 ms: 1.07x slower                                                        |
| gc_traversal                     | 2.95 ms                                                | 3.19 ms: 1.08x slower                                                        |
| nbody                            | 67.6 ms                                                | 73.8 ms: 1.09x slower                                                        |
| unpickle_pure_python             | 145 us                                                 | 160 us: 1.10x slower                                                         |
| pickle_pure_python               | 197 us                                                 | 218 us: 1.11x slower                                                         |
| crypto_pyaes                     | 51.4 ms                                                | 57.2 ms: 1.11x slower                                                        |
| django_template                  | 19.7 ms                                                | 22.0 ms: 1.12x slower                                                        |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 389 ms: 1.12x slower                                                         |
| scimark_lu                       | 73.5 ms                                                | 83.5 ms: 1.14x slower                                                        |
| richards_super                   | 34.6 ms                                                | 39.7 ms: 1.15x slower                                                        |
| pprint_pformat                   | 986 ms                                                 | 1.13 sec: 1.15x slower                                                       |
| telco                            | 3.92 ms                                                | 4.51 ms: 1.15x slower                                                        |
| pprint_safe_repr                 | 483 ms                                                 | 558 ms: 1.15x slower                                                         |
| many_optionals                   | 403 us                                                 | 466 us: 1.16x slower                                                         |
| richards                         | 30.6 ms                                                | 35.8 ms: 1.17x slower                                                        |
| create_gc_cycles                 | 1.15 ms                                                | 1.36 ms: 1.18x slower                                                        |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 168 ms: 1.19x slower                                                         |
| async_tree_eager_tg              | 46.9 ms                                                | 129 ms: 2.76x slower                                                         |
| logging_silent                   | 72.5 ns                                                | 328 ns: 4.52x slower                                                         |
| coverage                         | 38.5 ms                                                | 290 ms: 7.54x slower                                                         |
| thrift                           | 468 us                                                 | 43.5 ms: 93.04x slower                                                       |
| Geometric mean                   | (ref)                                                  | 1.02x slower                                                                 |

Benchmark hidden because not significant (5): shortest_path, asyncio_websockets, xml_etree_process, regex_dna, pycparser
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250614-3.15.0a0-4019a15/bm-20250614-darwin-arm64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.010x slower

# HPT report

- Reliability score: 92.72% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.12x