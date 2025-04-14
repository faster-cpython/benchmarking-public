# Results vs. 3.12.0

- fork: python
- ref: 275056a7fdcbe36aaac4
- machine: darwin-arm64
- commit hash: 275056a
- commit date: 2025-04-03
- overall geometric mean: 1.045x faster
- HPT reliability: 73.84%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-darwin-arm64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 169 ms: 1.00x slower                                                   |
| docutils       | 1.45 sec                                               | 1.46 sec: 1.01x slower                                                 |
| html5lib       | 33.4 ms                                                | 31.5 ms: 1.06x faster                                                  |
| sphinx         | 613 ms                                                 | 591 ms: 1.04x faster                                                   |
| Geometric mean | (ref)                                                  | 1.02x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-darwin-arm64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg                 | 673 ms                                                 | 375 ms: 1.80x faster                                                   |
| async_tree_eager_io              | 666 ms                                                 | 373 ms: 1.79x faster                                                   |
| async_tree_io                    | 672 ms                                                 | 390 ms: 1.72x faster                                                   |
| async_tree_memoization_tg        | 318 ms                                                 | 194 ms: 1.64x faster                                                   |
| async_tree_eager_io_tg           | 617 ms                                                 | 381 ms: 1.62x faster                                                   |
| async_tree_none_tg               | 255 ms                                                 | 159 ms: 1.61x faster                                                   |
| async_tree_none                  | 263 ms                                                 | 167 ms: 1.57x faster                                                   |
| async_tree_memoization           | 310 ms                                                 | 198 ms: 1.57x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 410 ms: 1.29x faster                                                   |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 412 ms: 1.28x faster                                                   |
| async_tree_eager_memoization     | 168 ms                                                 | 140 ms: 1.20x faster                                                   |
| async_generators                 | 299 ms                                                 | 261 ms: 1.14x faster                                                   |
| coroutines                       | 19.7 ms                                                | 17.3 ms: 1.14x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 357 ms: 1.05x faster                                                   |
| async_tree_eager                 | 65.8 ms                                                | 65.0 ms: 1.01x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 390 ms: 1.12x slower                                                   |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 173 ms: 1.22x slower                                                   |
| async_tree_eager_tg              | 46.9 ms                                                | 134 ms: 2.85x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.21x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-darwin-arm64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 54.1 ms                                                | 49.5 ms: 1.09x faster                                                  |
| pidigits       | 283 ms                                                 | 283 ms: 1.00x slower                                                   |
| nbody          | 67.6 ms                                                | 75.7 ms: 1.12x slower                                                  |
| Geometric mean | (ref)                                                  | 1.01x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-darwin-arm64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 2.44 ms                                                | 2.28 ms: 1.07x faster                                                  |
| regex_compile  | 75.9 ms                                                | 73.2 ms: 1.04x faster                                                  |
| regex_dna      | 143 ms                                                 | 141 ms: 1.01x faster                                                   |
| regex_v8       | 15.1 ms                                                | 16.1 ms: 1.07x slower                                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-darwin-arm64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_parse      | 108 ms                                                 | 104 ms: 1.04x faster                                                   |
| xml_etree_iterparse  | 75.5 ms                                                | 73.6 ms: 1.03x faster                                                  |
| tomli_loads          | 1.36 sec                                               | 1.34 sec: 1.01x faster                                                 |
| xml_etree_generate   | 55.4 ms                                                | 55.9 ms: 1.01x slower                                                  |
| xml_etree_process    | 38.9 ms                                                | 39.9 ms: 1.03x slower                                                  |
| json_loads           | 17.0 us                                                | 17.7 us: 1.04x slower                                                  |
| unpickle_pure_python | 145 us                                                 | 162 us: 1.11x slower                                                   |
| pickle_pure_python   | 197 us                                                 | 220 us: 1.12x slower                                                   |
| json_dumps           | 6.19 ms                                                | 7.43 ms: 1.20x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.05x slower                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-darwin-arm64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 17.8 ms                                                | 19.3 ms: 1.09x slower                                                  |
| python_startup_no_site | 13.2 ms                                                | 14.9 ms: 1.13x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.11x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-darwin-arm64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_xml      | 30.5 ms                                                | 30.8 ms: 1.01x slower                                                  |
| genshi_text     | 14.7 ms                                                | 14.9 ms: 1.02x slower                                                  |
| mako            | 7.44 ms                                                | 7.87 ms: 1.06x slower                                                  |
| django_template | 19.7 ms                                                | 22.2 ms: 1.13x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.05x slower                                                           |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250403-darwin-arm64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 12.6 ms: 2.56x faster                                                  |
| mdp                              | 1.49 sec                                               | 785 ms: 1.90x faster                                                   |
| async_tree_io_tg                 | 673 ms                                                 | 375 ms: 1.80x faster                                                   |
| async_tree_eager_io              | 666 ms                                                 | 373 ms: 1.79x faster                                                   |
| async_tree_io                    | 672 ms                                                 | 390 ms: 1.72x faster                                                   |
| async_tree_memoization_tg        | 318 ms                                                 | 194 ms: 1.64x faster                                                   |
| async_tree_eager_io_tg           | 617 ms                                                 | 381 ms: 1.62x faster                                                   |
| async_tree_none_tg               | 255 ms                                                 | 159 ms: 1.61x faster                                                   |
| async_tree_none                  | 263 ms                                                 | 167 ms: 1.57x faster                                                   |
| async_tree_memoization           | 310 ms                                                 | 198 ms: 1.57x faster                                                   |
| deepcopy                         | 226 us                                                 | 159 us: 1.42x faster                                                   |
| deepcopy_memo                    | 26.0 us                                                | 19.3 us: 1.35x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 410 ms: 1.29x faster                                                   |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 412 ms: 1.28x faster                                                   |
| generators                       | 29.4 ms                                                | 24.3 ms: 1.21x faster                                                  |
| deepcopy_reduce                  | 2.01 us                                                | 1.67 us: 1.20x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 140 ms: 1.20x faster                                                   |
| dulwich_log                      | 29.2 ms                                                | 25.3 ms: 1.16x faster                                                  |
| async_generators                 | 299 ms                                                 | 261 ms: 1.14x faster                                                   |
| raytrace                         | 204 ms                                                 | 179 ms: 1.14x faster                                                   |
| coroutines                       | 19.7 ms                                                | 17.3 ms: 1.14x faster                                                  |
| k_core                           | 1.72 sec                                               | 1.54 sec: 1.12x faster                                                 |
| comprehensions                   | 14.0 us                                                | 12.6 us: 1.11x faster                                                  |
| go                               | 98.5 ms                                                | 88.7 ms: 1.11x faster                                                  |
| pylint                           | 182 ms                                                 | 166 ms: 1.09x faster                                                   |
| float                            | 54.1 ms                                                | 49.5 ms: 1.09x faster                                                  |
| regex_effbot                     | 2.44 ms                                                | 2.28 ms: 1.07x faster                                                  |
| spectral_norm                    | 76.5 ms                                                | 71.5 ms: 1.07x faster                                                  |
| bench_mp_pool                    | 65.5 ms                                                | 61.2 ms: 1.07x faster                                                  |
| html5lib                         | 33.4 ms                                                | 31.5 ms: 1.06x faster                                                  |
| bpe_tokeniser                    | 3.28 sec                                               | 3.12 sec: 1.05x faster                                                 |
| logging_silent                   | 72.5 ns                                                | 69.0 ns: 1.05x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 357 ms: 1.05x faster                                                   |
| logging_simple                   | 3.60 us                                                | 3.45 us: 1.04x faster                                                  |
| xml_etree_parse                  | 108 ms                                                 | 104 ms: 1.04x faster                                                   |
| regex_compile                    | 75.9 ms                                                | 73.2 ms: 1.04x faster                                                  |
| sphinx                           | 613 ms                                                 | 591 ms: 1.04x faster                                                   |
| pathlib                          | 24.7 ms                                                | 23.8 ms: 1.04x faster                                                  |
| logging_format                   | 3.90 us                                                | 3.77 us: 1.03x faster                                                  |
| xml_etree_iterparse              | 75.5 ms                                                | 73.6 ms: 1.03x faster                                                  |
| chaos                            | 41.6 ms                                                | 40.9 ms: 1.02x faster                                                  |
| async_tree_eager                 | 65.8 ms                                                | 65.0 ms: 1.01x faster                                                  |
| regex_dna                        | 143 ms                                                 | 141 ms: 1.01x faster                                                   |
| sqlalchemy_declarative           | 61.9 ms                                                | 61.2 ms: 1.01x faster                                                  |
| tomli_loads                      | 1.36 sec                                               | 1.34 sec: 1.01x faster                                                 |
| scimark_fft                      | 194 ms                                                 | 194 ms: 1.00x faster                                                   |
| deltablue                        | 2.57 ms                                                | 2.56 ms: 1.00x faster                                                  |
| pidigits                         | 283 ms                                                 | 283 ms: 1.00x slower                                                   |
| 2to3                             | 168 ms                                                 | 169 ms: 1.00x slower                                                   |
| sqlite_synth                     | 1.55 us                                                | 1.55 us: 1.00x slower                                                  |
| docutils                         | 1.45 sec                                               | 1.46 sec: 1.01x slower                                                 |
| xml_etree_generate               | 55.4 ms                                                | 55.9 ms: 1.01x slower                                                  |
| genshi_xml                       | 30.5 ms                                                | 30.8 ms: 1.01x slower                                                  |
| json                             | 3.00 ms                                                | 3.04 ms: 1.01x slower                                                  |
| pycparser                        | 673 ms                                                 | 682 ms: 1.01x slower                                                   |
| genshi_text                      | 14.7 ms                                                | 14.9 ms: 1.02x slower                                                  |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 3.20 ms: 1.02x slower                                                  |
| sympy_sum                        | 76.2 ms                                                | 77.6 ms: 1.02x slower                                                  |
| pyflate                          | 311 ms                                                 | 318 ms: 1.02x slower                                                   |
| xml_etree_process                | 38.9 ms                                                | 39.9 ms: 1.03x slower                                                  |
| sympy_integrate                  | 11.1 ms                                                | 11.4 ms: 1.03x slower                                                  |
| sympy_str                        | 144 ms                                                 | 148 ms: 1.03x slower                                                   |
| shortest_path                    | 331 ms                                                 | 341 ms: 1.03x slower                                                   |
| scimark_sor                      | 85.8 ms                                                | 88.6 ms: 1.03x slower                                                  |
| sqlalchemy_imperative            | 6.60 ms                                                | 6.85 ms: 1.04x slower                                                  |
| json_loads                       | 17.0 us                                                | 17.7 us: 1.04x slower                                                  |
| scimark_monte_carlo              | 44.5 ms                                                | 46.4 ms: 1.04x slower                                                  |
| bench_thread_pool                | 483 us                                                 | 505 us: 1.05x slower                                                   |
| gc_traversal                     | 2.95 ms                                                | 3.11 ms: 1.05x slower                                                  |
| pprint_pformat                   | 986 ms                                                 | 1.04 sec: 1.05x slower                                                 |
| mako                             | 7.44 ms                                                | 7.87 ms: 1.06x slower                                                  |
| pprint_safe_repr                 | 483 ms                                                 | 514 ms: 1.06x slower                                                   |
| sympy_expand                     | 233 ms                                                 | 248 ms: 1.06x slower                                                   |
| connected_components             | 300 ms                                                 | 320 ms: 1.07x slower                                                   |
| regex_v8                         | 15.1 ms                                                | 16.1 ms: 1.07x slower                                                  |
| typing_runtime_protocols         | 91.5 us                                                | 98.3 us: 1.07x slower                                                  |
| nqueens                          | 59.5 ms                                                | 64.0 ms: 1.08x slower                                                  |
| python_startup                   | 17.8 ms                                                | 19.3 ms: 1.09x slower                                                  |
| meteor_contest                   | 69.1 ms                                                | 75.7 ms: 1.10x slower                                                  |
| hexiom                           | 4.38 ms                                                | 4.84 ms: 1.11x slower                                                  |
| create_gc_cycles                 | 1.15 ms                                                | 1.27 ms: 1.11x slower                                                  |
| scimark_lu                       | 73.5 ms                                                | 81.4 ms: 1.11x slower                                                  |
| unpickle_pure_python             | 145 us                                                 | 162 us: 1.11x slower                                                   |
| pickle_pure_python               | 197 us                                                 | 220 us: 1.12x slower                                                   |
| crypto_pyaes                     | 51.4 ms                                                | 57.5 ms: 1.12x slower                                                  |
| nbody                            | 67.6 ms                                                | 75.7 ms: 1.12x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 390 ms: 1.12x slower                                                   |
| django_template                  | 19.7 ms                                                | 22.2 ms: 1.13x slower                                                  |
| python_startup_no_site           | 13.2 ms                                                | 14.9 ms: 1.13x slower                                                  |
| many_optionals                   | 403 us                                                 | 456 us: 1.13x slower                                                   |
| fannkuch                         | 250 ms                                                 | 284 ms: 1.14x slower                                                   |
| richards_super                   | 34.6 ms                                                | 40.5 ms: 1.17x slower                                                  |
| telco                            | 3.92 ms                                                | 4.68 ms: 1.19x slower                                                  |
| richards                         | 30.6 ms                                                | 36.5 ms: 1.19x slower                                                  |
| json_dumps                       | 6.19 ms                                                | 7.43 ms: 1.20x slower                                                  |
| coverage                         | 38.5 ms                                                | 46.4 ms: 1.21x slower                                                  |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 173 ms: 1.22x slower                                                   |
| async_tree_eager_tg              | 46.9 ms                                                | 134 ms: 2.85x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.05x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: chameleon, dask, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (4) of results/bm-20250403-3.14.0a6+-275056a/bm-20250403-darwin-arm64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.045x faster

# HPT report

- Reliability score: 73.84% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.11x