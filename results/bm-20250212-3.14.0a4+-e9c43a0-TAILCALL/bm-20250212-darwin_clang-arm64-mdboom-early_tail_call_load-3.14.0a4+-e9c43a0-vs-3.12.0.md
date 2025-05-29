# Results vs. 3.12.0

- fork: mdboom
- ref: early_tail_call_load
- machine: darwin-arm64
- commit hash: e9c43a0
- commit date: 2025-02-12
- overall geometric mean: 1.160x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250212-darwin-arm64-mdboom-early_tail_call_load-3.14.0a4+-e9c43a0 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 152 ms: 1.11x faster                                                   |
| docutils       | 1.45 sec                                               | 1.35 sec: 1.08x faster                                                 |
| html5lib       | 33.4 ms                                                | 28.7 ms: 1.16x faster                                                  |
| sphinx         | 613 ms                                                 | 537 ms: 1.14x faster                                                   |
| Geometric mean | (ref)                                                  | 1.12x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250212-darwin-arm64-mdboom-early_tail_call_load-3.14.0a4+-e9c43a0 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io                    | 672 ms                                                 | 340 ms: 1.97x faster                                                   |
| async_tree_io_tg                 | 673 ms                                                 | 342 ms: 1.97x faster                                                   |
| async_tree_eager_io              | 666 ms                                                 | 345 ms: 1.93x faster                                                   |
| async_tree_eager_io_tg           | 617 ms                                                 | 347 ms: 1.78x faster                                                   |
| async_tree_none_tg               | 255 ms                                                 | 145 ms: 1.76x faster                                                   |
| async_tree_none                  | 263 ms                                                 | 150 ms: 1.76x faster                                                   |
| async_tree_memoization_tg        | 318 ms                                                 | 184 ms: 1.73x faster                                                   |
| async_tree_memoization           | 310 ms                                                 | 183 ms: 1.70x faster                                                   |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 400 ms: 1.32x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 402 ms: 1.31x faster                                                   |
| coroutines                       | 19.7 ms                                                | 15.1 ms: 1.31x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 134 ms: 1.25x faster                                                   |
| async_generators                 | 299 ms                                                 | 250 ms: 1.19x faster                                                   |
| async_tree_eager                 | 65.8 ms                                                | 58.4 ms: 1.13x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 348 ms: 1.07x faster                                                   |
| asyncio_websockets               | 243 ms                                                 | 242 ms: 1.00x faster                                                   |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 381 ms: 1.10x slower                                                   |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 165 ms: 1.17x slower                                                   |
| async_tree_eager_tg              | 46.9 ms                                                | 123 ms: 2.62x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.30x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250212-darwin-arm64-mdboom-early_tail_call_load-3.14.0a4+-e9c43a0 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 54.1 ms                                                | 43.6 ms: 1.24x faster                                                  |
| nbody          | 67.6 ms                                                | 63.3 ms: 1.07x faster                                                  |
| pidigits       | 283 ms                                                 | 280 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                  | 1.10x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250212-darwin-arm64-mdboom-early_tail_call_load-3.14.0a4+-e9c43a0 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 75.9 ms                                                | 62.0 ms: 1.22x faster                                                  |
| regex_effbot   | 2.44 ms                                                | 2.36 ms: 1.03x faster                                                  |
| regex_dna      | 143 ms                                                 | 146 ms: 1.02x slower                                                   |
| regex_v8       | 15.1 ms                                                | 17.7 ms: 1.17x slower                                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250212-darwin-arm64-mdboom-early_tail_call_load-3.14.0a4+-e9c43a0 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| unpickle_pure_python | 145 us                                                 | 123 us: 1.18x faster                                                   |
| tomli_loads          | 1.36 sec                                               | 1.15 sec: 1.18x faster                                                 |
| xml_etree_process    | 38.9 ms                                                | 34.0 ms: 1.14x faster                                                  |
| xml_etree_generate   | 55.4 ms                                                | 48.5 ms: 1.14x faster                                                  |
| xml_etree_iterparse  | 75.5 ms                                                | 69.0 ms: 1.09x faster                                                  |
| pickle_pure_python   | 197 us                                                 | 182 us: 1.08x faster                                                   |
| xml_etree_parse      | 108 ms                                                 | 101 ms: 1.07x faster                                                   |
| json_loads           | 17.0 us                                                | 17.9 us: 1.05x slower                                                  |
| json_dumps           | 6.19 ms                                                | 7.09 ms: 1.15x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250212-darwin-arm64-mdboom-early_tail_call_load-3.14.0a4+-e9c43a0 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 13.2 ms                                                | 12.4 ms: 1.06x faster                                                  |
| python_startup         | 17.8 ms                                                | 17.1 ms: 1.04x faster                                                  |
| Geometric mean         | (ref)                                                  | 1.05x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250212-darwin-arm64-mdboom-early_tail_call_load-3.14.0a4+-e9c43a0 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 14.7 ms                                                | 12.3 ms: 1.20x faster                                                  |
| genshi_xml      | 30.5 ms                                                | 26.3 ms: 1.16x faster                                                  |
| mako            | 7.44 ms                                                | 7.05 ms: 1.06x faster                                                  |
| django_template | 19.7 ms                                                | 19.0 ms: 1.04x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.11x faster                                                           |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250212-darwin-arm64-mdboom-early_tail_call_load-3.14.0a4+-e9c43a0 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 11.3 ms: 2.84x faster                                                  |
| async_tree_io                    | 672 ms                                                 | 340 ms: 1.97x faster                                                   |
| async_tree_io_tg                 | 673 ms                                                 | 342 ms: 1.97x faster                                                   |
| async_tree_eager_io              | 666 ms                                                 | 345 ms: 1.93x faster                                                   |
| async_tree_eager_io_tg           | 617 ms                                                 | 347 ms: 1.78x faster                                                   |
| async_tree_none_tg               | 255 ms                                                 | 145 ms: 1.76x faster                                                   |
| async_tree_none                  | 263 ms                                                 | 150 ms: 1.76x faster                                                   |
| async_tree_memoization_tg        | 318 ms                                                 | 184 ms: 1.73x faster                                                   |
| generators                       | 29.4 ms                                                | 17.2 ms: 1.71x faster                                                  |
| async_tree_memoization           | 310 ms                                                 | 183 ms: 1.70x faster                                                   |
| deepcopy                         | 226 us                                                 | 140 us: 1.61x faster                                                   |
| deepcopy_memo                    | 26.0 us                                                | 16.3 us: 1.60x faster                                                  |
| go                               | 98.5 ms                                                | 70.5 ms: 1.40x faster                                                  |
| deepcopy_reduce                  | 2.01 us                                                | 1.50 us: 1.35x faster                                                  |
| comprehensions                   | 14.0 us                                                | 10.5 us: 1.33x faster                                                  |
| raytrace                         | 204 ms                                                 | 155 ms: 1.32x faster                                                   |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 400 ms: 1.32x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 402 ms: 1.31x faster                                                   |
| coroutines                       | 19.7 ms                                                | 15.1 ms: 1.31x faster                                                  |
| spectral_norm                    | 76.5 ms                                                | 58.6 ms: 1.31x faster                                                  |
| deltablue                        | 2.57 ms                                                | 2.04 ms: 1.26x faster                                                  |
| logging_silent                   | 72.5 ns                                                | 58.1 ns: 1.25x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 134 ms: 1.25x faster                                                   |
| pylint                           | 182 ms                                                 | 146 ms: 1.24x faster                                                   |
| logging_simple                   | 3.60 us                                                | 2.90 us: 1.24x faster                                                  |
| float                            | 54.1 ms                                                | 43.6 ms: 1.24x faster                                                  |
| regex_compile                    | 75.9 ms                                                | 62.0 ms: 1.22x faster                                                  |
| logging_format                   | 3.90 us                                                | 3.21 us: 1.22x faster                                                  |
| genshi_text                      | 14.7 ms                                                | 12.3 ms: 1.20x faster                                                  |
| async_generators                 | 299 ms                                                 | 250 ms: 1.19x faster                                                   |
| bpe_tokeniser                    | 3.28 sec                                               | 2.75 sec: 1.19x faster                                                 |
| sqlglot_parse                    | 808 us                                                 | 678 us: 1.19x faster                                                   |
| chaos                            | 41.6 ms                                                | 35.0 ms: 1.19x faster                                                  |
| unpickle_pure_python             | 145 us                                                 | 123 us: 1.18x faster                                                   |
| sqlglot_transpile                | 973 us                                                 | 825 us: 1.18x faster                                                   |
| tomli_loads                      | 1.36 sec                                               | 1.15 sec: 1.18x faster                                                 |
| nqueens                          | 59.5 ms                                                | 50.6 ms: 1.18x faster                                                  |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 2.67 ms: 1.18x faster                                                  |
| scimark_sor                      | 85.8 ms                                                | 73.3 ms: 1.17x faster                                                  |
| k_core                           | 1.72 sec                                               | 1.48 sec: 1.16x faster                                                 |
| genshi_xml                       | 30.5 ms                                                | 26.3 ms: 1.16x faster                                                  |
| html5lib                         | 33.4 ms                                                | 28.7 ms: 1.16x faster                                                  |
| hexiom                           | 4.38 ms                                                | 3.81 ms: 1.15x faster                                                  |
| sqlalchemy_declarative           | 61.9 ms                                                | 53.9 ms: 1.15x faster                                                  |
| scimark_fft                      | 194 ms                                                 | 169 ms: 1.15x faster                                                   |
| thrift                           | 468 us                                                 | 409 us: 1.14x faster                                                   |
| xml_etree_process                | 38.9 ms                                                | 34.0 ms: 1.14x faster                                                  |
| xml_etree_generate               | 55.4 ms                                                | 48.5 ms: 1.14x faster                                                  |
| sphinx                           | 613 ms                                                 | 537 ms: 1.14x faster                                                   |
| scimark_monte_carlo              | 44.5 ms                                                | 39.0 ms: 1.14x faster                                                  |
| scimark_lu                       | 73.5 ms                                                | 64.8 ms: 1.13x faster                                                  |
| async_tree_eager                 | 65.8 ms                                                | 58.4 ms: 1.13x faster                                                  |
| pyflate                          | 311 ms                                                 | 276 ms: 1.12x faster                                                   |
| pprint_pformat                   | 986 ms                                                 | 879 ms: 1.12x faster                                                   |
| sympy_str                        | 144 ms                                                 | 128 ms: 1.12x faster                                                   |
| pathlib                          | 24.7 ms                                                | 22.1 ms: 1.12x faster                                                  |
| richards_super                   | 34.6 ms                                                | 31.0 ms: 1.12x faster                                                  |
| sqlglot_optimize                 | 33.2 ms                                                | 29.8 ms: 1.11x faster                                                  |
| sympy_sum                        | 76.2 ms                                                | 68.5 ms: 1.11x faster                                                  |
| 2to3                             | 168 ms                                                 | 152 ms: 1.11x faster                                                   |
| richards                         | 30.6 ms                                                | 27.6 ms: 1.11x faster                                                  |
| pprint_safe_repr                 | 483 ms                                                 | 436 ms: 1.11x faster                                                   |
| dulwich_log                      | 29.2 ms                                                | 26.4 ms: 1.11x faster                                                  |
| sympy_integrate                  | 11.1 ms                                                | 10.1 ms: 1.10x faster                                                  |
| crypto_pyaes                     | 51.4 ms                                                | 46.8 ms: 1.10x faster                                                  |
| sqlglot_normalize                | 180 ms                                                 | 164 ms: 1.10x faster                                                   |
| pycparser                        | 673 ms                                                 | 614 ms: 1.10x faster                                                   |
| xml_etree_iterparse              | 75.5 ms                                                | 69.0 ms: 1.09x faster                                                  |
| pickle_pure_python               | 197 us                                                 | 182 us: 1.08x faster                                                   |
| sympy_expand                     | 233 ms                                                 | 216 ms: 1.08x faster                                                   |
| docutils                         | 1.45 sec                                               | 1.35 sec: 1.08x faster                                                 |
| sqlalchemy_imperative            | 6.60 ms                                                | 6.13 ms: 1.08x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 348 ms: 1.07x faster                                                   |
| nbody                            | 67.6 ms                                                | 63.3 ms: 1.07x faster                                                  |
| xml_etree_parse                  | 108 ms                                                 | 101 ms: 1.07x faster                                                   |
| python_startup_no_site           | 13.2 ms                                                | 12.4 ms: 1.06x faster                                                  |
| bench_thread_pool                | 483 us                                                 | 456 us: 1.06x faster                                                   |
| mako                             | 7.44 ms                                                | 7.05 ms: 1.06x faster                                                  |
| typing_runtime_protocols         | 91.5 us                                                | 86.9 us: 1.05x faster                                                  |
| mdp                              | 1.49 sec                                               | 1.43 sec: 1.05x faster                                                 |
| django_template                  | 19.7 ms                                                | 19.0 ms: 1.04x faster                                                  |
| python_startup                   | 17.8 ms                                                | 17.1 ms: 1.04x faster                                                  |
| regex_effbot                     | 2.44 ms                                                | 2.36 ms: 1.03x faster                                                  |
| sqlite_synth                     | 1.55 us                                                | 1.50 us: 1.03x faster                                                  |
| shortest_path                    | 331 ms                                                 | 325 ms: 1.02x faster                                                   |
| fannkuch                         | 250 ms                                                 | 247 ms: 1.01x faster                                                   |
| connected_components             | 300 ms                                                 | 297 ms: 1.01x faster                                                   |
| dask                             | 779 ms                                                 | 770 ms: 1.01x faster                                                   |
| pidigits                         | 283 ms                                                 | 280 ms: 1.01x faster                                                   |
| meteor_contest                   | 69.1 ms                                                | 68.4 ms: 1.01x faster                                                  |
| asyncio_websockets               | 243 ms                                                 | 242 ms: 1.00x faster                                                   |
| many_optionals                   | 403 us                                                 | 411 us: 1.02x slower                                                   |
| regex_dna                        | 143 ms                                                 | 146 ms: 1.02x slower                                                   |
| gc_traversal                     | 2.95 ms                                                | 3.08 ms: 1.04x slower                                                  |
| json_loads                       | 17.0 us                                                | 17.9 us: 1.05x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 381 ms: 1.10x slower                                                   |
| create_gc_cycles                 | 1.15 ms                                                | 1.27 ms: 1.10x slower                                                  |
| telco                            | 3.92 ms                                                | 4.42 ms: 1.13x slower                                                  |
| json_dumps                       | 6.19 ms                                                | 7.09 ms: 1.15x slower                                                  |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 165 ms: 1.17x slower                                                   |
| coverage                         | 38.5 ms                                                | 45.1 ms: 1.17x slower                                                  |
| regex_v8                         | 15.1 ms                                                | 17.7 ms: 1.17x slower                                                  |
| async_tree_eager_tg              | 46.9 ms                                                | 123 ms: 2.62x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.16x faster                                                           |

Benchmark hidden because not significant (2): bench_mp_pool, json
Ignored benchmarks (5) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.160x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.11x
- 95% likely to have a speedup of 1.11x
- 99% likely to have a speedup of 1.10x

# Memory
- memory change: 1.08x