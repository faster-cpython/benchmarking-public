# Results vs. 3.12.0

- fork: nelhage
- ref: computed_goto_nomerg
- machine: darwin-arm64
- commit hash: 4603470
- commit date: 2025-02-10
- overall geometric mean: 1.091x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250210-darwin-arm64-nelhage-computed_goto_nomerg-3.14.0a4+-4603470 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 162 ms: 1.04x faster                                                    |
| docutils       | 1.45 sec                                               | 1.41 sec: 1.03x faster                                                  |
| html5lib       | 33.4 ms                                                | 29.2 ms: 1.14x faster                                                   |
| sphinx         | 613 ms                                                 | 563 ms: 1.09x faster                                                    |
| Geometric mean | (ref)                                                  | 1.07x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250210-darwin-arm64-nelhage-computed_goto_nomerg-3.14.0a4+-4603470 |
|----------------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_eager_io              | 666 ms                                                 | 360 ms: 1.85x faster                                                    |
| async_tree_io_tg                 | 673 ms                                                 | 365 ms: 1.84x faster                                                    |
| async_tree_io                    | 672 ms                                                 | 372 ms: 1.80x faster                                                    |
| async_tree_none                  | 263 ms                                                 | 160 ms: 1.65x faster                                                    |
| async_tree_none_tg               | 255 ms                                                 | 155 ms: 1.64x faster                                                    |
| async_tree_eager_io_tg           | 617 ms                                                 | 376 ms: 1.64x faster                                                    |
| async_tree_memoization_tg        | 318 ms                                                 | 196 ms: 1.62x faster                                                    |
| async_tree_memoization           | 310 ms                                                 | 197 ms: 1.58x faster                                                    |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 414 ms: 1.27x faster                                                    |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 416 ms: 1.27x faster                                                    |
| coroutines                       | 19.7 ms                                                | 15.9 ms: 1.24x faster                                                   |
| async_generators                 | 299 ms                                                 | 252 ms: 1.18x faster                                                    |
| async_tree_eager_memoization     | 168 ms                                                 | 142 ms: 1.18x faster                                                    |
| async_tree_eager                 | 65.8 ms                                                | 62.7 ms: 1.05x faster                                                   |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 359 ms: 1.04x faster                                                    |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 392 ms: 1.13x slower                                                    |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 175 ms: 1.23x slower                                                    |
| async_tree_eager_tg              | 46.9 ms                                                | 131 ms: 2.80x slower                                                    |
| Geometric mean                   | (ref)                                                  | 1.23x faster                                                            |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250210-darwin-arm64-nelhage-computed_goto_nomerg-3.14.0a4+-4603470 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 54.1 ms                                                | 46.6 ms: 1.16x faster                                                   |
| pidigits       | 283 ms                                                 | 283 ms: 1.00x slower                                                    |
| nbody          | 67.6 ms                                                | 71.0 ms: 1.05x slower                                                   |
| Geometric mean | (ref)                                                  | 1.03x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250210-darwin-arm64-nelhage-computed_goto_nomerg-3.14.0a4+-4603470 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 75.9 ms                                                | 66.8 ms: 1.14x faster                                                   |
| regex_effbot   | 2.44 ms                                                | 2.27 ms: 1.07x faster                                                   |
| regex_dna      | 143 ms                                                 | 142 ms: 1.00x faster                                                    |
| regex_v8       | 15.1 ms                                                | 16.9 ms: 1.12x slower                                                   |
| Geometric mean | (ref)                                                  | 1.02x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250210-darwin-arm64-nelhage-computed_goto_nomerg-3.14.0a4+-4603470 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 1.36 sec                                               | 1.19 sec: 1.14x faster                                                  |
| xml_etree_parse      | 108 ms                                                 | 98.8 ms: 1.09x faster                                                   |
| xml_etree_iterparse  | 75.5 ms                                                | 71.0 ms: 1.06x faster                                                   |
| xml_etree_generate   | 55.4 ms                                                | 53.2 ms: 1.04x faster                                                   |
| unpickle_pure_python | 145 us                                                 | 142 us: 1.02x faster                                                    |
| xml_etree_process    | 38.9 ms                                                | 38.4 ms: 1.01x faster                                                   |
| pickle_pure_python   | 197 us                                                 | 199 us: 1.01x slower                                                    |
| json_loads           | 17.0 us                                                | 17.8 us: 1.05x slower                                                   |
| json_dumps           | 6.19 ms                                                | 7.24 ms: 1.17x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250210-darwin-arm64-nelhage-computed_goto_nomerg-3.14.0a4+-4603470 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 13.2 ms                                                | 14.0 ms: 1.07x slower                                                   |
| python_startup         | 17.8 ms                                                | 19.1 ms: 1.07x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250210-darwin-arm64-nelhage-computed_goto_nomerg-3.14.0a4+-4603470 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text     | 14.7 ms                                                | 13.5 ms: 1.09x faster                                                   |
| genshi_xml      | 30.5 ms                                                | 28.4 ms: 1.07x faster                                                   |
| mako            | 7.44 ms                                                | 7.38 ms: 1.01x faster                                                   |
| django_template | 19.7 ms                                                | 20.7 ms: 1.05x slower                                                   |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                            |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250210-darwin-arm64-nelhage-computed_goto_nomerg-3.14.0a4+-4603470 |
|----------------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 11.7 ms: 2.74x faster                                                   |
| async_tree_eager_io              | 666 ms                                                 | 360 ms: 1.85x faster                                                    |
| async_tree_io_tg                 | 673 ms                                                 | 365 ms: 1.84x faster                                                    |
| async_tree_io                    | 672 ms                                                 | 372 ms: 1.80x faster                                                    |
| async_tree_none                  | 263 ms                                                 | 160 ms: 1.65x faster                                                    |
| async_tree_none_tg               | 255 ms                                                 | 155 ms: 1.64x faster                                                    |
| async_tree_eager_io_tg           | 617 ms                                                 | 376 ms: 1.64x faster                                                    |
| async_tree_memoization_tg        | 318 ms                                                 | 196 ms: 1.62x faster                                                    |
| async_tree_memoization           | 310 ms                                                 | 197 ms: 1.58x faster                                                    |
| deepcopy                         | 226 us                                                 | 148 us: 1.53x faster                                                    |
| deepcopy_memo                    | 26.0 us                                                | 18.2 us: 1.43x faster                                                   |
| deepcopy_reduce                  | 2.01 us                                                | 1.57 us: 1.29x faster                                                   |
| generators                       | 29.4 ms                                                | 22.9 ms: 1.28x faster                                                   |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 414 ms: 1.27x faster                                                    |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 416 ms: 1.27x faster                                                    |
| spectral_norm                    | 76.5 ms                                                | 61.3 ms: 1.25x faster                                                   |
| go                               | 98.5 ms                                                | 79.2 ms: 1.24x faster                                                   |
| coroutines                       | 19.7 ms                                                | 15.9 ms: 1.24x faster                                                   |
| raytrace                         | 204 ms                                                 | 170 ms: 1.20x faster                                                    |
| comprehensions                   | 14.0 us                                                | 11.8 us: 1.19x faster                                                   |
| async_generators                 | 299 ms                                                 | 252 ms: 1.18x faster                                                    |
| async_tree_eager_memoization     | 168 ms                                                 | 142 ms: 1.18x faster                                                    |
| float                            | 54.1 ms                                                | 46.6 ms: 1.16x faster                                                   |
| k_core                           | 1.72 sec                                               | 1.49 sec: 1.16x faster                                                  |
| pylint                           | 182 ms                                                 | 157 ms: 1.16x faster                                                    |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 2.74 ms: 1.15x faster                                                   |
| html5lib                         | 33.4 ms                                                | 29.2 ms: 1.14x faster                                                   |
| bpe_tokeniser                    | 3.28 sec                                               | 2.88 sec: 1.14x faster                                                  |
| regex_compile                    | 75.9 ms                                                | 66.8 ms: 1.14x faster                                                   |
| logging_simple                   | 3.60 us                                                | 3.17 us: 1.14x faster                                                   |
| tomli_loads                      | 1.36 sec                                               | 1.19 sec: 1.14x faster                                                  |
| scimark_fft                      | 194 ms                                                 | 171 ms: 1.13x faster                                                    |
| logging_format                   | 3.90 us                                                | 3.49 us: 1.12x faster                                                   |
| scimark_sor                      | 85.8 ms                                                | 77.9 ms: 1.10x faster                                                   |
| logging_silent                   | 72.5 ns                                                | 65.9 ns: 1.10x faster                                                   |
| deltablue                        | 2.57 ms                                                | 2.34 ms: 1.10x faster                                                   |
| xml_etree_parse                  | 108 ms                                                 | 98.8 ms: 1.09x faster                                                   |
| genshi_text                      | 14.7 ms                                                | 13.5 ms: 1.09x faster                                                   |
| sphinx                           | 613 ms                                                 | 563 ms: 1.09x faster                                                    |
| pyflate                          | 311 ms                                                 | 288 ms: 1.08x faster                                                    |
| pathlib                          | 24.7 ms                                                | 22.9 ms: 1.08x faster                                                   |
| thrift                           | 468 us                                                 | 435 us: 1.08x faster                                                    |
| regex_effbot                     | 2.44 ms                                                | 2.27 ms: 1.07x faster                                                   |
| genshi_xml                       | 30.5 ms                                                | 28.4 ms: 1.07x faster                                                   |
| sqlalchemy_declarative           | 61.9 ms                                                | 57.9 ms: 1.07x faster                                                   |
| chaos                            | 41.6 ms                                                | 38.9 ms: 1.07x faster                                                   |
| bench_mp_pool                    | 65.5 ms                                                | 61.3 ms: 1.07x faster                                                   |
| xml_etree_iterparse              | 75.5 ms                                                | 71.0 ms: 1.06x faster                                                   |
| sqlglot_parse                    | 808 us                                                 | 762 us: 1.06x faster                                                    |
| dulwich_log                      | 29.2 ms                                                | 27.5 ms: 1.06x faster                                                   |
| sqlglot_transpile                | 973 us                                                 | 918 us: 1.06x faster                                                    |
| pprint_pformat                   | 986 ms                                                 | 934 ms: 1.06x faster                                                    |
| async_tree_eager                 | 65.8 ms                                                | 62.7 ms: 1.05x faster                                                   |
| pprint_safe_repr                 | 483 ms                                                 | 463 ms: 1.04x faster                                                    |
| sympy_str                        | 144 ms                                                 | 138 ms: 1.04x faster                                                    |
| sympy_sum                        | 76.2 ms                                                | 73.1 ms: 1.04x faster                                                   |
| xml_etree_generate               | 55.4 ms                                                | 53.2 ms: 1.04x faster                                                   |
| pycparser                        | 673 ms                                                 | 646 ms: 1.04x faster                                                    |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 359 ms: 1.04x faster                                                    |
| scimark_monte_carlo              | 44.5 ms                                                | 42.7 ms: 1.04x faster                                                   |
| 2to3                             | 168 ms                                                 | 162 ms: 1.04x faster                                                    |
| sqlglot_optimize                 | 33.2 ms                                                | 32.1 ms: 1.03x faster                                                   |
| docutils                         | 1.45 sec                                               | 1.41 sec: 1.03x faster                                                  |
| nqueens                          | 59.5 ms                                                | 57.9 ms: 1.03x faster                                                   |
| sqlalchemy_imperative            | 6.60 ms                                                | 6.42 ms: 1.03x faster                                                   |
| unpickle_pure_python             | 145 us                                                 | 142 us: 1.02x faster                                                    |
| hexiom                           | 4.38 ms                                                | 4.29 ms: 1.02x faster                                                   |
| shortest_path                    | 331 ms                                                 | 324 ms: 1.02x faster                                                    |
| sqlite_synth                     | 1.55 us                                                | 1.52 us: 1.02x faster                                                   |
| sqlglot_normalize                | 180 ms                                                 | 177 ms: 1.02x faster                                                    |
| dask                             | 779 ms                                                 | 768 ms: 1.01x faster                                                    |
| xml_etree_process                | 38.9 ms                                                | 38.4 ms: 1.01x faster                                                   |
| mdp                              | 1.49 sec                                               | 1.48 sec: 1.01x faster                                                  |
| connected_components             | 300 ms                                                 | 297 ms: 1.01x faster                                                    |
| sympy_expand                     | 233 ms                                                 | 231 ms: 1.01x faster                                                    |
| mako                             | 7.44 ms                                                | 7.38 ms: 1.01x faster                                                   |
| regex_dna                        | 143 ms                                                 | 142 ms: 1.00x faster                                                    |
| pidigits                         | 283 ms                                                 | 283 ms: 1.00x slower                                                    |
| bench_thread_pool                | 483 us                                                 | 485 us: 1.01x slower                                                    |
| sympy_integrate                  | 11.1 ms                                                | 11.2 ms: 1.01x slower                                                   |
| pickle_pure_python               | 197 us                                                 | 199 us: 1.01x slower                                                    |
| crypto_pyaes                     | 51.4 ms                                                | 52.2 ms: 1.02x slower                                                   |
| fannkuch                         | 250 ms                                                 | 254 ms: 1.02x slower                                                    |
| typing_runtime_protocols         | 91.5 us                                                | 93.2 us: 1.02x slower                                                   |
| meteor_contest                   | 69.1 ms                                                | 70.5 ms: 1.02x slower                                                   |
| richards                         | 30.6 ms                                                | 31.7 ms: 1.04x slower                                                   |
| richards_super                   | 34.6 ms                                                | 36.0 ms: 1.04x slower                                                   |
| json_loads                       | 17.0 us                                                | 17.8 us: 1.05x slower                                                   |
| nbody                            | 67.6 ms                                                | 71.0 ms: 1.05x slower                                                   |
| django_template                  | 19.7 ms                                                | 20.7 ms: 1.05x slower                                                   |
| gc_traversal                     | 2.95 ms                                                | 3.12 ms: 1.06x slower                                                   |
| python_startup_no_site           | 13.2 ms                                                | 14.0 ms: 1.07x slower                                                   |
| many_optionals                   | 403 us                                                 | 430 us: 1.07x slower                                                    |
| python_startup                   | 17.8 ms                                                | 19.1 ms: 1.07x slower                                                   |
| create_gc_cycles                 | 1.15 ms                                                | 1.29 ms: 1.12x slower                                                   |
| regex_v8                         | 15.1 ms                                                | 16.9 ms: 1.12x slower                                                   |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 392 ms: 1.13x slower                                                    |
| telco                            | 3.92 ms                                                | 4.53 ms: 1.16x slower                                                   |
| json_dumps                       | 6.19 ms                                                | 7.24 ms: 1.17x slower                                                   |
| coverage                         | 38.5 ms                                                | 46.0 ms: 1.19x slower                                                   |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 175 ms: 1.23x slower                                                    |
| async_tree_eager_tg              | 46.9 ms                                                | 131 ms: 2.80x slower                                                    |
| Geometric mean                   | (ref)                                                  | 1.09x faster                                                            |

Benchmark hidden because not significant (3): json, asyncio_websockets, scimark_lu
Ignored benchmarks (5) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.091x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.12x