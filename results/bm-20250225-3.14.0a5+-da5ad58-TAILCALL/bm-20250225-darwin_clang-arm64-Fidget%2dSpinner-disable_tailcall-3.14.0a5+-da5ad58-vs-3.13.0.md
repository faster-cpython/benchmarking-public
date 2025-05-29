# Results vs. 3.13.0

- fork: Fidget-Spinner
- ref: disable_tailcall
- machine: darwin-arm64
- commit hash: da5ad58
- commit date: 2025-02-25
- overall geometric mean: 1.033x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250225-darwin-arm64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 196 ms: 1.10x slower                                                         |
| html5lib       | 36.7 ms                                                | 32.5 ms: 1.13x faster                                                        |
| sphinx         | 602 ms                                                 | 581 ms: 1.04x faster                                                         |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                 |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250225-darwin-arm64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 200 ms: 1.44x faster                                                         |
| async_tree_eager_io              | 511 ms                                                 | 370 ms: 1.38x faster                                                         |
| async_tree_io_tg                 | 500 ms                                                 | 372 ms: 1.35x faster                                                         |
| async_tree_io                    | 508 ms                                                 | 391 ms: 1.30x faster                                                         |
| async_tree_memoization           | 268 ms                                                 | 208 ms: 1.29x faster                                                         |
| async_tree_none                  | 212 ms                                                 | 168 ms: 1.26x faster                                                         |
| async_tree_eager_io_tg           | 479 ms                                                 | 382 ms: 1.25x faster                                                         |
| async_tree_none_tg               | 198 ms                                                 | 160 ms: 1.24x faster                                                         |
| async_tree_eager_memoization     | 168 ms                                                 | 146 ms: 1.15x faster                                                         |
| async_generators                 | 294 ms                                                 | 265 ms: 1.11x faster                                                         |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 416 ms: 1.10x faster                                                         |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 414 ms: 1.08x faster                                                         |
| coroutines                       | 20.0 ms                                                | 19.0 ms: 1.06x faster                                                        |
| async_tree_eager                 | 69.9 ms                                                | 67.1 ms: 1.04x faster                                                        |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 359 ms: 1.04x faster                                                         |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 392 ms: 1.13x slower                                                         |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 181 ms: 1.31x slower                                                         |
| async_tree_eager_tg              | 47.4 ms                                                | 135 ms: 2.85x slower                                                         |
| Geometric mean                   | (ref)                                                  | 1.07x faster                                                                 |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250225-darwin-arm64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 48.9 ms: 1.14x faster                                                        |
| pidigits       | 284 ms                                                 | 281 ms: 1.01x faster                                                         |
| nbody          | 73.6 ms                                                | 81.0 ms: 1.10x slower                                                        |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250225-darwin-arm64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.34 ms: 1.12x faster                                                        |
| regex_dna      | 149 ms                                                 | 145 ms: 1.03x faster                                                         |
| regex_compile  | 78.3 ms                                                | 76.2 ms: 1.03x faster                                                        |
| regex_v8       | 17.0 ms                                                | 17.9 ms: 1.05x slower                                                        |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250225-darwin-arm64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_parse      | 108 ms                                                 | 103 ms: 1.05x faster                                                         |
| unpickle_pure_python | 165 us                                                 | 161 us: 1.03x faster                                                         |
| xml_etree_iterparse  | 74.2 ms                                                | 72.5 ms: 1.02x faster                                                        |
| xml_etree_process    | 41.3 ms                                                | 40.9 ms: 1.01x faster                                                        |
| xml_etree_generate   | 57.1 ms                                                | 56.5 ms: 1.01x faster                                                        |
| pickle_pure_python   | 215 us                                                 | 220 us: 1.03x slower                                                         |
| json_loads           | 17.0 us                                                | 18.0 us: 1.05x slower                                                        |
| json_dumps           | 6.47 ms                                                | 7.37 ms: 1.14x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                                 |

Benchmark hidden because not significant (1): tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250225-darwin-arm64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 18.8 ms                                                | 19.0 ms: 1.01x slower                                                        |
| python_startup_no_site | 13.7 ms                                                | 14.1 ms: 1.02x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250225-darwin-arm64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 15.2 ms: 1.11x faster                                                        |
| genshi_xml      | 34.1 ms                                                | 32.6 ms: 1.04x faster                                                        |
| mako            | 7.75 ms                                                | 7.91 ms: 1.02x slower                                                        |
| django_template | 20.5 ms                                                | 23.0 ms: 1.12x slower                                                        |
| Geometric mean  | (ref)                                                  | 1.00x faster                                                                 |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250225-darwin-arm64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 200 ms: 1.44x faster                                                         |
| async_tree_eager_io              | 511 ms                                                 | 370 ms: 1.38x faster                                                         |
| async_tree_io_tg                 | 500 ms                                                 | 372 ms: 1.35x faster                                                         |
| generators                       | 31.9 ms                                                | 23.9 ms: 1.34x faster                                                        |
| go                               | 117 ms                                                 | 88.0 ms: 1.33x faster                                                        |
| deepcopy                         | 236 us                                                 | 181 us: 1.31x faster                                                         |
| async_tree_io                    | 508 ms                                                 | 391 ms: 1.30x faster                                                         |
| async_tree_memoization           | 268 ms                                                 | 208 ms: 1.29x faster                                                         |
| async_tree_none                  | 212 ms                                                 | 168 ms: 1.26x faster                                                         |
| async_tree_eager_io_tg           | 479 ms                                                 | 382 ms: 1.25x faster                                                         |
| async_tree_none_tg               | 198 ms                                                 | 160 ms: 1.24x faster                                                         |
| deepcopy_memo                    | 27.4 us                                                | 22.2 us: 1.23x faster                                                        |
| scimark_sor                      | 106 ms                                                 | 88.0 ms: 1.20x faster                                                        |
| spectral_norm                    | 76.5 ms                                                | 65.1 ms: 1.17x faster                                                        |
| deepcopy_reduce                  | 2.09 us                                                | 1.81 us: 1.16x faster                                                        |
| async_tree_eager_memoization     | 168 ms                                                 | 146 ms: 1.15x faster                                                         |
| float                            | 55.8 ms                                                | 48.9 ms: 1.14x faster                                                        |
| richards                         | 36.2 ms                                                | 32.0 ms: 1.13x faster                                                        |
| deltablue                        | 2.65 ms                                                | 2.34 ms: 1.13x faster                                                        |
| html5lib                         | 36.7 ms                                                | 32.5 ms: 1.13x faster                                                        |
| regex_effbot                     | 2.63 ms                                                | 2.34 ms: 1.12x faster                                                        |
| pylint                           | 180 ms                                                 | 160 ms: 1.12x faster                                                         |
| pyflate                          | 352 ms                                                 | 316 ms: 1.12x faster                                                         |
| genshi_text                      | 16.9 ms                                                | 15.2 ms: 1.11x faster                                                        |
| async_generators                 | 294 ms                                                 | 265 ms: 1.11x faster                                                         |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 416 ms: 1.10x faster                                                         |
| richards_super                   | 39.2 ms                                                | 35.5 ms: 1.10x faster                                                        |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 414 ms: 1.08x faster                                                         |
| bench_mp_pool                    | 64.7 ms                                                | 60.5 ms: 1.07x faster                                                        |
| k_core                           | 1.61 sec                                               | 1.51 sec: 1.07x faster                                                       |
| connected_components             | 319 ms                                                 | 299 ms: 1.06x faster                                                         |
| scimark_monte_carlo              | 50.4 ms                                                | 47.4 ms: 1.06x faster                                                        |
| shortest_path                    | 345 ms                                                 | 326 ms: 1.06x faster                                                         |
| coroutines                       | 20.0 ms                                                | 19.0 ms: 1.06x faster                                                        |
| crypto_pyaes                     | 55.3 ms                                                | 52.5 ms: 1.05x faster                                                        |
| scimark_fft                      | 200 ms                                                 | 190 ms: 1.05x faster                                                         |
| xml_etree_parse                  | 108 ms                                                 | 103 ms: 1.05x faster                                                         |
| raytrace                         | 181 ms                                                 | 173 ms: 1.05x faster                                                         |
| genshi_xml                       | 34.1 ms                                                | 32.6 ms: 1.04x faster                                                        |
| telco                            | 4.84 ms                                                | 4.64 ms: 1.04x faster                                                        |
| async_tree_eager                 | 69.9 ms                                                | 67.1 ms: 1.04x faster                                                        |
| thrift                           | 466 us                                                 | 448 us: 1.04x faster                                                         |
| bpe_tokeniser                    | 3.26 sec                                               | 3.14 sec: 1.04x faster                                                       |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 359 ms: 1.04x faster                                                         |
| sqlglot_transpile                | 1.04 ms                                                | 1.00 ms: 1.04x faster                                                        |
| nqueens                          | 61.8 ms                                                | 59.7 ms: 1.04x faster                                                        |
| sphinx                           | 602 ms                                                 | 581 ms: 1.04x faster                                                         |
| coverage                         | 46.2 ms                                                | 44.7 ms: 1.03x faster                                                        |
| logging_simple                   | 3.56 us                                                | 3.44 us: 1.03x faster                                                        |
| logging_format                   | 3.85 us                                                | 3.74 us: 1.03x faster                                                        |
| typing_runtime_protocols         | 101 us                                                 | 97.8 us: 1.03x faster                                                        |
| sqlglot_parse                    | 852 us                                                 | 829 us: 1.03x faster                                                         |
| regex_dna                        | 149 ms                                                 | 145 ms: 1.03x faster                                                         |
| regex_compile                    | 78.3 ms                                                | 76.2 ms: 1.03x faster                                                        |
| unpickle_pure_python             | 165 us                                                 | 161 us: 1.03x faster                                                         |
| xml_etree_iterparse              | 74.2 ms                                                | 72.5 ms: 1.02x faster                                                        |
| sympy_integrate                  | 11.3 ms                                                | 11.1 ms: 1.02x faster                                                        |
| sympy_expand                     | 248 ms                                                 | 243 ms: 1.02x faster                                                         |
| dulwich_log                      | 28.7 ms                                                | 28.2 ms: 1.02x faster                                                        |
| mdp                              | 1.50 sec                                               | 1.48 sec: 1.01x faster                                                       |
| sqlglot_optimize                 | 34.7 ms                                                | 34.2 ms: 1.01x faster                                                        |
| chaos                            | 41.1 ms                                                | 40.6 ms: 1.01x faster                                                        |
| pycparser                        | 701 ms                                                 | 693 ms: 1.01x faster                                                         |
| xml_etree_process                | 41.3 ms                                                | 40.9 ms: 1.01x faster                                                        |
| pidigits                         | 284 ms                                                 | 281 ms: 1.01x faster                                                         |
| sympy_str                        | 146 ms                                                 | 144 ms: 1.01x faster                                                         |
| xml_etree_generate               | 57.1 ms                                                | 56.5 ms: 1.01x faster                                                        |
| sqlglot_normalize                | 188 ms                                                 | 187 ms: 1.01x faster                                                         |
| dask                             | 771 ms                                                 | 767 ms: 1.01x faster                                                         |
| bench_thread_pool                | 503 us                                                 | 501 us: 1.01x faster                                                         |
| sqlite_synth                     | 1.55 us                                                | 1.55 us: 1.00x faster                                                        |
| logging_silent                   | 71.0 ns                                                | 71.3 ns: 1.00x slower                                                        |
| hexiom                           | 4.87 ms                                                | 4.90 ms: 1.01x slower                                                        |
| pathlib                          | 23.2 ms                                                | 23.4 ms: 1.01x slower                                                        |
| python_startup                   | 18.8 ms                                                | 19.0 ms: 1.01x slower                                                        |
| sympy_sum                        | 75.1 ms                                                | 76.2 ms: 1.01x slower                                                        |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 3.03 ms: 1.02x slower                                                        |
| scimark_lu                       | 75.9 ms                                                | 77.4 ms: 1.02x slower                                                        |
| mako                             | 7.75 ms                                                | 7.91 ms: 1.02x slower                                                        |
| pprint_pformat                   | 1.10 sec                                               | 1.12 sec: 1.02x slower                                                       |
| python_startup_no_site           | 13.7 ms                                                | 14.1 ms: 1.02x slower                                                        |
| sqlalchemy_declarative           | 59.0 ms                                                | 60.5 ms: 1.02x slower                                                        |
| pickle_pure_python               | 215 us                                                 | 220 us: 1.03x slower                                                         |
| pprint_safe_repr                 | 541 ms                                                 | 560 ms: 1.04x slower                                                         |
| gc_traversal                     | 2.94 ms                                                | 3.07 ms: 1.05x slower                                                        |
| regex_v8                         | 17.0 ms                                                | 17.9 ms: 1.05x slower                                                        |
| create_gc_cycles                 | 1.19 ms                                                | 1.25 ms: 1.05x slower                                                        |
| json_loads                       | 17.0 us                                                | 18.0 us: 1.05x slower                                                        |
| meteor_contest                   | 74.0 ms                                                | 79.3 ms: 1.07x slower                                                        |
| sqlalchemy_imperative            | 6.69 ms                                                | 7.27 ms: 1.09x slower                                                        |
| 2to3                             | 179 ms                                                 | 196 ms: 1.10x slower                                                         |
| nbody                            | 73.6 ms                                                | 81.0 ms: 1.10x slower                                                        |
| fannkuch                         | 279 ms                                                 | 310 ms: 1.11x slower                                                         |
| django_template                  | 20.5 ms                                                | 23.0 ms: 1.12x slower                                                        |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 392 ms: 1.13x slower                                                         |
| json_dumps                       | 6.47 ms                                                | 7.37 ms: 1.14x slower                                                        |
| many_optionals                   | 409 us                                                 | 466 us: 1.14x slower                                                         |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 181 ms: 1.31x slower                                                         |
| subparsers                       | 9.44 ms                                                | 12.7 ms: 1.34x slower                                                        |
| async_tree_eager_tg              | 47.4 ms                                                | 135 ms: 2.85x slower                                                         |
| Geometric mean                   | (ref)                                                  | 1.03x faster                                                                 |

Benchmark hidden because not significant (5): comprehensions, docutils, asyncio_websockets, json, tomli_loads
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.033x faster

# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.08x