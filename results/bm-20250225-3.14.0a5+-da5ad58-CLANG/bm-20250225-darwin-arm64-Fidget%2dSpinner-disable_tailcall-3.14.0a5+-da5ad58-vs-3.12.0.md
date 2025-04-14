# Results vs. 3.12.0

- fork: Fidget-Spinner
- ref: disable_tailcall
- machine: darwin-arm64
- commit hash: da5ad58
- commit date: 2025-02-25
- overall geometric mean: 1.030x faster
- HPT reliability: 77.55%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250225-darwin-arm64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 196 ms: 1.16x slower                                                         |
| docutils       | 1.45 sec                                               | 1.44 sec: 1.01x faster                                                       |
| html5lib       | 33.4 ms                                                | 32.5 ms: 1.03x faster                                                        |
| sphinx         | 613 ms                                                 | 581 ms: 1.05x faster                                                         |
| Geometric mean | (ref)                                                  | 1.02x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250225-darwin-arm64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg                 | 673 ms                                                 | 372 ms: 1.81x faster                                                         |
| async_tree_eager_io              | 666 ms                                                 | 370 ms: 1.80x faster                                                         |
| async_tree_io                    | 672 ms                                                 | 391 ms: 1.72x faster                                                         |
| async_tree_eager_io_tg           | 617 ms                                                 | 382 ms: 1.62x faster                                                         |
| async_tree_memoization_tg        | 318 ms                                                 | 200 ms: 1.59x faster                                                         |
| async_tree_none_tg               | 255 ms                                                 | 160 ms: 1.59x faster                                                         |
| async_tree_none                  | 263 ms                                                 | 168 ms: 1.57x faster                                                         |
| async_tree_memoization           | 310 ms                                                 | 208 ms: 1.49x faster                                                         |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 414 ms: 1.28x faster                                                         |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 416 ms: 1.27x faster                                                         |
| async_tree_eager_memoization     | 168 ms                                                 | 146 ms: 1.15x faster                                                         |
| async_generators                 | 299 ms                                                 | 265 ms: 1.13x faster                                                         |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 359 ms: 1.04x faster                                                         |
| coroutines                       | 19.7 ms                                                | 19.0 ms: 1.04x faster                                                        |
| async_tree_eager                 | 65.8 ms                                                | 67.1 ms: 1.02x slower                                                        |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 392 ms: 1.13x slower                                                         |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 181 ms: 1.28x slower                                                         |
| async_tree_eager_tg              | 46.9 ms                                                | 135 ms: 2.88x slower                                                         |
| Geometric mean                   | (ref)                                                  | 1.19x faster                                                                 |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250225-darwin-arm64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 54.1 ms                                                | 48.9 ms: 1.11x faster                                                        |
| pidigits       | 283 ms                                                 | 281 ms: 1.01x faster                                                         |
| nbody          | 67.6 ms                                                | 81.0 ms: 1.20x slower                                                        |
| Geometric mean | (ref)                                                  | 1.02x slower                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250225-darwin-arm64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 2.44 ms                                                | 2.34 ms: 1.04x faster                                                        |
| regex_compile  | 75.9 ms                                                | 76.2 ms: 1.00x slower                                                        |
| regex_dna      | 143 ms                                                 | 145 ms: 1.01x slower                                                         |
| regex_v8       | 15.1 ms                                                | 17.9 ms: 1.19x slower                                                        |
| Geometric mean | (ref)                                                  | 1.04x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250225-darwin-arm64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_parse      | 108 ms                                                 | 103 ms: 1.05x faster                                                         |
| xml_etree_iterparse  | 75.5 ms                                                | 72.5 ms: 1.04x faster                                                        |
| xml_etree_generate   | 55.4 ms                                                | 56.5 ms: 1.02x slower                                                        |
| xml_etree_process    | 38.9 ms                                                | 40.9 ms: 1.05x slower                                                        |
| json_loads           | 17.0 us                                                | 18.0 us: 1.05x slower                                                        |
| unpickle_pure_python | 145 us                                                 | 161 us: 1.11x slower                                                         |
| pickle_pure_python   | 197 us                                                 | 220 us: 1.12x slower                                                         |
| tomli_loads          | 1.36 sec                                               | 1.57 sec: 1.16x slower                                                       |
| json_dumps           | 6.19 ms                                                | 7.37 ms: 1.19x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.07x slower                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250225-darwin-arm64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 13.2 ms                                                | 14.1 ms: 1.07x slower                                                        |
| python_startup         | 17.8 ms                                                | 19.0 ms: 1.07x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250225-darwin-arm64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_text     | 14.7 ms                                                | 15.2 ms: 1.04x slower                                                        |
| mako            | 7.44 ms                                                | 7.91 ms: 1.06x slower                                                        |
| genshi_xml      | 30.5 ms                                                | 32.6 ms: 1.07x slower                                                        |
| django_template | 19.7 ms                                                | 23.0 ms: 1.17x slower                                                        |
| Geometric mean  | (ref)                                                  | 1.08x slower                                                                 |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250225-darwin-arm64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 12.7 ms: 2.54x faster                                                        |
| async_tree_io_tg                 | 673 ms                                                 | 372 ms: 1.81x faster                                                         |
| async_tree_eager_io              | 666 ms                                                 | 370 ms: 1.80x faster                                                         |
| async_tree_io                    | 672 ms                                                 | 391 ms: 1.72x faster                                                         |
| async_tree_eager_io_tg           | 617 ms                                                 | 382 ms: 1.62x faster                                                         |
| async_tree_memoization_tg        | 318 ms                                                 | 200 ms: 1.59x faster                                                         |
| async_tree_none_tg               | 255 ms                                                 | 160 ms: 1.59x faster                                                         |
| async_tree_none                  | 263 ms                                                 | 168 ms: 1.57x faster                                                         |
| async_tree_memoization           | 310 ms                                                 | 208 ms: 1.49x faster                                                         |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 414 ms: 1.28x faster                                                         |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 416 ms: 1.27x faster                                                         |
| deepcopy                         | 226 us                                                 | 181 us: 1.25x faster                                                         |
| generators                       | 29.4 ms                                                | 23.9 ms: 1.23x faster                                                        |
| raytrace                         | 204 ms                                                 | 173 ms: 1.18x faster                                                         |
| spectral_norm                    | 76.5 ms                                                | 65.1 ms: 1.17x faster                                                        |
| comprehensions                   | 14.0 us                                                | 11.9 us: 1.17x faster                                                        |
| deepcopy_memo                    | 26.0 us                                                | 22.2 us: 1.17x faster                                                        |
| async_tree_eager_memoization     | 168 ms                                                 | 146 ms: 1.15x faster                                                         |
| k_core                           | 1.72 sec                                               | 1.51 sec: 1.14x faster                                                       |
| pylint                           | 182 ms                                                 | 160 ms: 1.13x faster                                                         |
| async_generators                 | 299 ms                                                 | 265 ms: 1.13x faster                                                         |
| go                               | 98.5 ms                                                | 88.0 ms: 1.12x faster                                                        |
| deepcopy_reduce                  | 2.01 us                                                | 1.81 us: 1.11x faster                                                        |
| float                            | 54.1 ms                                                | 48.9 ms: 1.11x faster                                                        |
| deltablue                        | 2.57 ms                                                | 2.34 ms: 1.10x faster                                                        |
| bench_mp_pool                    | 65.5 ms                                                | 60.5 ms: 1.08x faster                                                        |
| sphinx                           | 613 ms                                                 | 581 ms: 1.05x faster                                                         |
| pathlib                          | 24.7 ms                                                | 23.4 ms: 1.05x faster                                                        |
| xml_etree_parse                  | 108 ms                                                 | 103 ms: 1.05x faster                                                         |
| logging_simple                   | 3.60 us                                                | 3.44 us: 1.05x faster                                                        |
| bpe_tokeniser                    | 3.28 sec                                               | 3.14 sec: 1.05x faster                                                       |
| thrift                           | 468 us                                                 | 448 us: 1.04x faster                                                         |
| logging_format                   | 3.90 us                                                | 3.74 us: 1.04x faster                                                        |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 359 ms: 1.04x faster                                                         |
| regex_effbot                     | 2.44 ms                                                | 2.34 ms: 1.04x faster                                                        |
| xml_etree_iterparse              | 75.5 ms                                                | 72.5 ms: 1.04x faster                                                        |
| coroutines                       | 19.7 ms                                                | 19.0 ms: 1.04x faster                                                        |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 3.03 ms: 1.04x faster                                                        |
| dulwich_log                      | 29.2 ms                                                | 28.2 ms: 1.03x faster                                                        |
| html5lib                         | 33.4 ms                                                | 32.5 ms: 1.03x faster                                                        |
| chaos                            | 41.6 ms                                                | 40.6 ms: 1.03x faster                                                        |
| scimark_fft                      | 194 ms                                                 | 190 ms: 1.03x faster                                                         |
| sqlalchemy_declarative           | 61.9 ms                                                | 60.5 ms: 1.02x faster                                                        |
| logging_silent                   | 72.5 ns                                                | 71.3 ns: 1.02x faster                                                        |
| dask                             | 779 ms                                                 | 767 ms: 1.02x faster                                                         |
| shortest_path                    | 331 ms                                                 | 326 ms: 1.02x faster                                                         |
| mdp                              | 1.49 sec                                               | 1.48 sec: 1.01x faster                                                       |
| pidigits                         | 283 ms                                                 | 281 ms: 1.01x faster                                                         |
| docutils                         | 1.45 sec                                               | 1.44 sec: 1.01x faster                                                       |
| nqueens                          | 59.5 ms                                                | 59.7 ms: 1.00x slower                                                        |
| regex_compile                    | 75.9 ms                                                | 76.2 ms: 1.00x slower                                                        |
| json                             | 3.00 ms                                                | 3.05 ms: 1.01x slower                                                        |
| regex_dna                        | 143 ms                                                 | 145 ms: 1.01x slower                                                         |
| pyflate                          | 311 ms                                                 | 316 ms: 1.02x slower                                                         |
| xml_etree_generate               | 55.4 ms                                                | 56.5 ms: 1.02x slower                                                        |
| async_tree_eager                 | 65.8 ms                                                | 67.1 ms: 1.02x slower                                                        |
| crypto_pyaes                     | 51.4 ms                                                | 52.5 ms: 1.02x slower                                                        |
| sqlglot_parse                    | 808 us                                                 | 829 us: 1.03x slower                                                         |
| richards_super                   | 34.6 ms                                                | 35.5 ms: 1.03x slower                                                        |
| scimark_sor                      | 85.8 ms                                                | 88.0 ms: 1.03x slower                                                        |
| sqlglot_transpile                | 973 us                                                 | 1.00 ms: 1.03x slower                                                        |
| pycparser                        | 673 ms                                                 | 693 ms: 1.03x slower                                                         |
| sqlglot_optimize                 | 33.2 ms                                                | 34.2 ms: 1.03x slower                                                        |
| bench_thread_pool                | 483 us                                                 | 501 us: 1.04x slower                                                         |
| genshi_text                      | 14.7 ms                                                | 15.2 ms: 1.04x slower                                                        |
| sympy_expand                     | 233 ms                                                 | 243 ms: 1.04x slower                                                         |
| gc_traversal                     | 2.95 ms                                                | 3.07 ms: 1.04x slower                                                        |
| sqlglot_normalize                | 180 ms                                                 | 187 ms: 1.04x slower                                                         |
| richards                         | 30.6 ms                                                | 32.0 ms: 1.05x slower                                                        |
| xml_etree_process                | 38.9 ms                                                | 40.9 ms: 1.05x slower                                                        |
| scimark_lu                       | 73.5 ms                                                | 77.4 ms: 1.05x slower                                                        |
| json_loads                       | 17.0 us                                                | 18.0 us: 1.05x slower                                                        |
| mako                             | 7.44 ms                                                | 7.91 ms: 1.06x slower                                                        |
| scimark_monte_carlo              | 44.5 ms                                                | 47.4 ms: 1.07x slower                                                        |
| python_startup_no_site           | 13.2 ms                                                | 14.1 ms: 1.07x slower                                                        |
| typing_runtime_protocols         | 91.5 us                                                | 97.8 us: 1.07x slower                                                        |
| genshi_xml                       | 30.5 ms                                                | 32.6 ms: 1.07x slower                                                        |
| python_startup                   | 17.8 ms                                                | 19.0 ms: 1.07x slower                                                        |
| create_gc_cycles                 | 1.15 ms                                                | 1.25 ms: 1.09x slower                                                        |
| sqlalchemy_imperative            | 6.60 ms                                                | 7.27 ms: 1.10x slower                                                        |
| unpickle_pure_python             | 145 us                                                 | 161 us: 1.11x slower                                                         |
| pickle_pure_python               | 197 us                                                 | 220 us: 1.12x slower                                                         |
| hexiom                           | 4.38 ms                                                | 4.90 ms: 1.12x slower                                                        |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 392 ms: 1.13x slower                                                         |
| pprint_pformat                   | 986 ms                                                 | 1.12 sec: 1.14x slower                                                       |
| meteor_contest                   | 69.1 ms                                                | 79.3 ms: 1.15x slower                                                        |
| many_optionals                   | 403 us                                                 | 466 us: 1.16x slower                                                         |
| tomli_loads                      | 1.36 sec                                               | 1.57 sec: 1.16x slower                                                       |
| pprint_safe_repr                 | 483 ms                                                 | 560 ms: 1.16x slower                                                         |
| 2to3                             | 168 ms                                                 | 196 ms: 1.16x slower                                                         |
| coverage                         | 38.5 ms                                                | 44.7 ms: 1.16x slower                                                        |
| django_template                  | 19.7 ms                                                | 23.0 ms: 1.17x slower                                                        |
| telco                            | 3.92 ms                                                | 4.64 ms: 1.18x slower                                                        |
| regex_v8                         | 15.1 ms                                                | 17.9 ms: 1.19x slower                                                        |
| json_dumps                       | 6.19 ms                                                | 7.37 ms: 1.19x slower                                                        |
| nbody                            | 67.6 ms                                                | 81.0 ms: 1.20x slower                                                        |
| fannkuch                         | 250 ms                                                 | 310 ms: 1.24x slower                                                         |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 181 ms: 1.28x slower                                                         |
| async_tree_eager_tg              | 46.9 ms                                                | 135 ms: 2.88x slower                                                         |
| Geometric mean                   | (ref)                                                  | 1.03x faster                                                                 |

Benchmark hidden because not significant (6): connected_components, sympy_integrate, sympy_sum, asyncio_websockets, sqlite_synth, sympy_str
Ignored benchmarks (5) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.030x faster

# HPT report

- Reliability score: 77.55% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.11x