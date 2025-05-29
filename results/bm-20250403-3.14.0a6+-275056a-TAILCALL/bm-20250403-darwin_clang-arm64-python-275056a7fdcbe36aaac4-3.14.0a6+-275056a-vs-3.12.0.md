# Results vs. 3.12.0

- fork: python
- ref: 275056a7fdcbe36aaac4
- machine: darwin-arm64
- commit hash: 275056a
- commit date: 2025-04-03
- overall geometric mean: 1.149x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-darwin-arm64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 186 ms: 1.10x slower                                                   |
| docutils       | 1.45 sec                                               | 1.37 sec: 1.06x faster                                                 |
| html5lib       | 33.4 ms                                                | 29.0 ms: 1.15x faster                                                  |
| sphinx         | 613 ms                                                 | 548 ms: 1.12x faster                                                   |
| Geometric mean | (ref)                                                  | 1.06x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-darwin-arm64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg                 | 673 ms                                                 | 339 ms: 1.99x faster                                                   |
| async_tree_io                    | 672 ms                                                 | 339 ms: 1.98x faster                                                   |
| async_tree_eager_io              | 666 ms                                                 | 338 ms: 1.97x faster                                                   |
| async_tree_none_tg               | 255 ms                                                 | 143 ms: 1.79x faster                                                   |
| async_tree_eager_io_tg           | 617 ms                                                 | 348 ms: 1.77x faster                                                   |
| async_tree_memoization_tg        | 318 ms                                                 | 181 ms: 1.76x faster                                                   |
| async_tree_memoization           | 310 ms                                                 | 179 ms: 1.74x faster                                                   |
| async_tree_none                  | 263 ms                                                 | 155 ms: 1.70x faster                                                   |
| coroutines                       | 19.7 ms                                                | 14.8 ms: 1.33x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 398 ms: 1.33x faster                                                   |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 398 ms: 1.32x faster                                                   |
| async_tree_eager_memoization     | 168 ms                                                 | 130 ms: 1.29x faster                                                   |
| async_generators                 | 299 ms                                                 | 239 ms: 1.25x faster                                                   |
| async_tree_eager                 | 65.8 ms                                                | 56.2 ms: 1.17x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 345 ms: 1.08x faster                                                   |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 378 ms: 1.09x slower                                                   |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 160 ms: 1.13x slower                                                   |
| async_tree_eager_tg              | 46.9 ms                                                | 124 ms: 2.63x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.32x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-darwin-arm64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 54.1 ms                                                | 42.9 ms: 1.26x faster                                                  |
| pidigits       | 283 ms                                                 | 280 ms: 1.01x faster                                                   |
| nbody          | 67.6 ms                                                | 71.6 ms: 1.06x slower                                                  |
| Geometric mean | (ref)                                                  | 1.06x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-darwin-arm64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 75.9 ms                                                | 62.0 ms: 1.22x faster                                                  |
| regex_effbot   | 2.44 ms                                                | 2.39 ms: 1.02x faster                                                  |
| regex_dna      | 143 ms                                                 | 148 ms: 1.04x slower                                                   |
| regex_v8       | 15.1 ms                                                | 16.7 ms: 1.11x slower                                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-darwin-arm64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 1.36 sec                                               | 1.16 sec: 1.17x faster                                                 |
| xml_etree_generate   | 55.4 ms                                                | 48.5 ms: 1.14x faster                                                  |
| xml_etree_process    | 38.9 ms                                                | 34.4 ms: 1.13x faster                                                  |
| unpickle_pure_python | 145 us                                                 | 129 us: 1.13x faster                                                   |
| xml_etree_parse      | 108 ms                                                 | 98.8 ms: 1.09x faster                                                  |
| xml_etree_iterparse  | 75.5 ms                                                | 70.2 ms: 1.08x faster                                                  |
| pickle_pure_python   | 197 us                                                 | 186 us: 1.06x faster                                                   |
| json_loads           | 17.0 us                                                | 18.0 us: 1.06x slower                                                  |
| json_dumps           | 6.19 ms                                                | 7.20 ms: 1.16x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-darwin-arm64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 17.8 ms                                                | 19.2 ms: 1.08x slower                                                  |
| python_startup_no_site | 13.2 ms                                                | 14.9 ms: 1.13x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.10x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-darwin-arm64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 14.7 ms                                                | 12.7 ms: 1.16x faster                                                  |
| genshi_xml      | 30.5 ms                                                | 26.7 ms: 1.14x faster                                                  |
| django_template | 19.7 ms                                                | 19.3 ms: 1.02x faster                                                  |
| mako            | 7.44 ms                                                | 7.32 ms: 1.02x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                           |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-darwin-arm64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 11.5 ms: 2.79x faster                                                  |
| mdp                              | 1.49 sec                                               | 691 ms: 2.16x faster                                                   |
| async_tree_io_tg                 | 673 ms                                                 | 339 ms: 1.99x faster                                                   |
| async_tree_io                    | 672 ms                                                 | 339 ms: 1.98x faster                                                   |
| async_tree_eager_io              | 666 ms                                                 | 338 ms: 1.97x faster                                                   |
| async_tree_none_tg               | 255 ms                                                 | 143 ms: 1.79x faster                                                   |
| async_tree_eager_io_tg           | 617 ms                                                 | 348 ms: 1.77x faster                                                   |
| async_tree_memoization_tg        | 318 ms                                                 | 181 ms: 1.76x faster                                                   |
| async_tree_memoization           | 310 ms                                                 | 179 ms: 1.74x faster                                                   |
| async_tree_none                  | 263 ms                                                 | 155 ms: 1.70x faster                                                   |
| deepcopy_memo                    | 26.0 us                                                | 16.0 us: 1.62x faster                                                  |
| deepcopy                         | 226 us                                                 | 141 us: 1.60x faster                                                   |
| generators                       | 29.4 ms                                                | 19.0 ms: 1.54x faster                                                  |
| comprehensions                   | 14.0 us                                                | 10.1 us: 1.39x faster                                                  |
| go                               | 98.5 ms                                                | 70.8 ms: 1.39x faster                                                  |
| coroutines                       | 19.7 ms                                                | 14.8 ms: 1.33x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 398 ms: 1.33x faster                                                   |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 398 ms: 1.32x faster                                                   |
| deepcopy_reduce                  | 2.01 us                                                | 1.53 us: 1.32x faster                                                  |
| raytrace                         | 204 ms                                                 | 157 ms: 1.30x faster                                                   |
| async_tree_eager_memoization     | 168 ms                                                 | 130 ms: 1.29x faster                                                   |
| float                            | 54.1 ms                                                | 42.9 ms: 1.26x faster                                                  |
| logging_silent                   | 72.5 ns                                                | 57.9 ns: 1.25x faster                                                  |
| async_generators                 | 299 ms                                                 | 239 ms: 1.25x faster                                                   |
| dulwich_log                      | 29.2 ms                                                | 23.4 ms: 1.25x faster                                                  |
| deltablue                        | 2.57 ms                                                | 2.06 ms: 1.25x faster                                                  |
| regex_compile                    | 75.9 ms                                                | 62.0 ms: 1.22x faster                                                  |
| pylint                           | 182 ms                                                 | 151 ms: 1.20x faster                                                   |
| logging_simple                   | 3.60 us                                                | 3.01 us: 1.20x faster                                                  |
| logging_format                   | 3.90 us                                                | 3.28 us: 1.19x faster                                                  |
| chaos                            | 41.6 ms                                                | 35.5 ms: 1.17x faster                                                  |
| async_tree_eager                 | 65.8 ms                                                | 56.2 ms: 1.17x faster                                                  |
| tomli_loads                      | 1.36 sec                                               | 1.16 sec: 1.17x faster                                                 |
| bpe_tokeniser                    | 3.28 sec                                               | 2.81 sec: 1.17x faster                                                 |
| genshi_text                      | 14.7 ms                                                | 12.7 ms: 1.16x faster                                                  |
| k_core                           | 1.72 sec                                               | 1.49 sec: 1.15x faster                                                 |
| html5lib                         | 33.4 ms                                                | 29.0 ms: 1.15x faster                                                  |
| spectral_norm                    | 76.5 ms                                                | 66.8 ms: 1.15x faster                                                  |
| xml_etree_generate               | 55.4 ms                                                | 48.5 ms: 1.14x faster                                                  |
| hexiom                           | 4.38 ms                                                | 3.83 ms: 1.14x faster                                                  |
| genshi_xml                       | 30.5 ms                                                | 26.7 ms: 1.14x faster                                                  |
| scimark_sor                      | 85.8 ms                                                | 75.2 ms: 1.14x faster                                                  |
| pyflate                          | 311 ms                                                 | 273 ms: 1.14x faster                                                   |
| xml_etree_process                | 38.9 ms                                                | 34.4 ms: 1.13x faster                                                  |
| unpickle_pure_python             | 145 us                                                 | 129 us: 1.13x faster                                                   |
| scimark_monte_carlo              | 44.5 ms                                                | 39.4 ms: 1.13x faster                                                  |
| nqueens                          | 59.5 ms                                                | 52.8 ms: 1.13x faster                                                  |
| sqlalchemy_declarative           | 61.9 ms                                                | 55.2 ms: 1.12x faster                                                  |
| sphinx                           | 613 ms                                                 | 548 ms: 1.12x faster                                                   |
| sympy_str                        | 144 ms                                                 | 130 ms: 1.10x faster                                                   |
| sympy_integrate                  | 11.1 ms                                                | 10.1 ms: 1.09x faster                                                  |
| xml_etree_parse                  | 108 ms                                                 | 98.8 ms: 1.09x faster                                                  |
| bench_mp_pool                    | 65.5 ms                                                | 60.0 ms: 1.09x faster                                                  |
| sympy_sum                        | 76.2 ms                                                | 69.9 ms: 1.09x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 345 ms: 1.08x faster                                                   |
| xml_etree_iterparse              | 75.5 ms                                                | 70.2 ms: 1.08x faster                                                  |
| pycparser                        | 673 ms                                                 | 626 ms: 1.08x faster                                                   |
| sqlalchemy_imperative            | 6.60 ms                                                | 6.18 ms: 1.07x faster                                                  |
| pathlib                          | 24.7 ms                                                | 23.2 ms: 1.06x faster                                                  |
| sympy_expand                     | 233 ms                                                 | 219 ms: 1.06x faster                                                   |
| docutils                         | 1.45 sec                                               | 1.37 sec: 1.06x faster                                                 |
| pprint_pformat                   | 986 ms                                                 | 929 ms: 1.06x faster                                                   |
| pickle_pure_python               | 197 us                                                 | 186 us: 1.06x faster                                                   |
| scimark_lu                       | 73.5 ms                                                | 69.4 ms: 1.06x faster                                                  |
| typing_runtime_protocols         | 91.5 us                                                | 86.5 us: 1.06x faster                                                  |
| pprint_safe_repr                 | 483 ms                                                 | 461 ms: 1.05x faster                                                   |
| richards_super                   | 34.6 ms                                                | 33.1 ms: 1.05x faster                                                  |
| bench_thread_pool                | 483 us                                                 | 462 us: 1.05x faster                                                   |
| richards                         | 30.6 ms                                                | 29.4 ms: 1.04x faster                                                  |
| crypto_pyaes                     | 51.4 ms                                                | 49.5 ms: 1.04x faster                                                  |
| regex_effbot                     | 2.44 ms                                                | 2.39 ms: 1.02x faster                                                  |
| django_template                  | 19.7 ms                                                | 19.3 ms: 1.02x faster                                                  |
| shortest_path                    | 331 ms                                                 | 324 ms: 1.02x faster                                                   |
| sqlite_synth                     | 1.55 us                                                | 1.52 us: 1.02x faster                                                  |
| mako                             | 7.44 ms                                                | 7.32 ms: 1.02x faster                                                  |
| pidigits                         | 283 ms                                                 | 280 ms: 1.01x faster                                                   |
| connected_components             | 300 ms                                                 | 299 ms: 1.00x faster                                                   |
| scimark_fft                      | 194 ms                                                 | 194 ms: 1.00x faster                                                   |
| json                             | 3.00 ms                                                | 3.03 ms: 1.01x slower                                                  |
| meteor_contest                   | 69.1 ms                                                | 70.4 ms: 1.02x slower                                                  |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 3.20 ms: 1.02x slower                                                  |
| regex_dna                        | 143 ms                                                 | 148 ms: 1.04x slower                                                   |
| many_optionals                   | 403 us                                                 | 420 us: 1.04x slower                                                   |
| gc_traversal                     | 2.95 ms                                                | 3.09 ms: 1.05x slower                                                  |
| json_loads                       | 17.0 us                                                | 18.0 us: 1.06x slower                                                  |
| nbody                            | 67.6 ms                                                | 71.6 ms: 1.06x slower                                                  |
| python_startup                   | 17.8 ms                                                | 19.2 ms: 1.08x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 378 ms: 1.09x slower                                                   |
| 2to3                             | 168 ms                                                 | 186 ms: 1.10x slower                                                   |
| create_gc_cycles                 | 1.15 ms                                                | 1.27 ms: 1.10x slower                                                  |
| regex_v8                         | 15.1 ms                                                | 16.7 ms: 1.11x slower                                                  |
| python_startup_no_site           | 13.2 ms                                                | 14.9 ms: 1.13x slower                                                  |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 160 ms: 1.13x slower                                                   |
| telco                            | 3.92 ms                                                | 4.51 ms: 1.15x slower                                                  |
| json_dumps                       | 6.19 ms                                                | 7.20 ms: 1.16x slower                                                  |
| coverage                         | 38.5 ms                                                | 45.3 ms: 1.18x slower                                                  |
| async_tree_eager_tg              | 46.9 ms                                                | 124 ms: 2.63x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.15x faster                                                           |

Benchmark hidden because not significant (2): asyncio_websockets, fannkuch
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: chameleon, dask, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (4) of results/bm-20250403-3.14.0a6+-275056a-CLANG/bm-20250403-darwin-arm64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.149x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.09x
- 95% likely to have a speedup of 1.08x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: 1.10x