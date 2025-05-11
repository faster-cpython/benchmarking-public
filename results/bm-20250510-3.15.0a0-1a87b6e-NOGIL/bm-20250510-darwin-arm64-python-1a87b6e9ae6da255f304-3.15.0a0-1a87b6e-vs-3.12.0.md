# Results vs. 3.12.0

- fork: python
- ref: 1a87b6e9ae6da255f304
- machine: darwin-arm64
- commit hash: 1a87b6e
- commit date: 2025-05-10
- overall geometric mean: 1.051x slower
- HPT reliability: 99.49%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-darwin-arm64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 210 ms: 1.25x slower                                                  |
| docutils       | 1.45 sec                                               | 1.52 sec: 1.05x slower                                                |
| html5lib       | 33.4 ms                                                | 36.0 ms: 1.08x slower                                                 |
| sphinx         | 613 ms                                                 | 637 ms: 1.04x slower                                                  |
| Geometric mean | (ref)                                                  | 1.10x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-darwin-arm64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io_tg                 | 673 ms                                                 | 339 ms: 1.98x faster                                                  |
| async_tree_eager_io              | 666 ms                                                 | 347 ms: 1.92x faster                                                  |
| async_tree_io                    | 672 ms                                                 | 358 ms: 1.87x faster                                                  |
| async_tree_eager_io_tg           | 617 ms                                                 | 330 ms: 1.87x faster                                                  |
| async_tree_memoization_tg        | 318 ms                                                 | 187 ms: 1.70x faster                                                  |
| async_tree_none_tg               | 255 ms                                                 | 151 ms: 1.69x faster                                                  |
| async_tree_none                  | 263 ms                                                 | 171 ms: 1.54x faster                                                  |
| async_tree_memoization           | 310 ms                                                 | 211 ms: 1.47x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 397 ms: 1.33x faster                                                  |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 421 ms: 1.25x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 157 ms: 1.07x faster                                                  |
| coroutines                       | 19.7 ms                                                | 18.9 ms: 1.04x faster                                                 |
| asyncio_websockets               | 243 ms                                                 | 237 ms: 1.02x faster                                                  |
| async_generators                 | 299 ms                                                 | 293 ms: 1.02x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 377 ms: 1.01x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 380 ms: 1.10x slower                                                  |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 171 ms: 1.20x slower                                                  |
| async_tree_eager                 | 65.8 ms                                                | 86.8 ms: 1.32x slower                                                 |
| async_tree_eager_tg              | 46.9 ms                                                | 130 ms: 2.77x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.21x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-darwin-arm64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 283 ms                                                 | 281 ms: 1.01x faster                                                  |
| float          | 54.1 ms                                                | 55.2 ms: 1.02x slower                                                 |
| nbody          | 67.6 ms                                                | 95.5 ms: 1.41x slower                                                 |
| Geometric mean | (ref)                                                  | 1.13x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-darwin-arm64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.44 ms                                                | 2.12 ms: 1.15x faster                                                 |
| regex_dna      | 143 ms                                                 | 135 ms: 1.06x faster                                                  |
| regex_v8       | 15.1 ms                                                | 15.2 ms: 1.01x slower                                                 |
| regex_compile  | 75.9 ms                                                | 95.9 ms: 1.26x slower                                                 |
| Geometric mean | (ref)                                                  | 1.01x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-darwin-arm64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_iterparse  | 75.5 ms                                                | 67.4 ms: 1.12x faster                                                 |
| xml_etree_parse      | 108 ms                                                 | 99.1 ms: 1.09x faster                                                 |
| json_loads           | 17.0 us                                                | 19.2 us: 1.13x slower                                                 |
| xml_etree_generate   | 55.4 ms                                                | 63.7 ms: 1.15x slower                                                 |
| tomli_loads          | 1.36 sec                                               | 1.63 sec: 1.20x slower                                                |
| xml_etree_process    | 38.9 ms                                                | 48.4 ms: 1.25x slower                                                 |
| unpickle_pure_python | 145 us                                                 | 190 us: 1.31x slower                                                  |
| json_dumps           | 6.19 ms                                                | 8.32 ms: 1.35x slower                                                 |
| pickle_pure_python   | 197 us                                                 | 274 us: 1.39x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.16x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-darwin-arm64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 17.8 ms                                                | 18.9 ms: 1.06x slower                                                 |
| python_startup_no_site | 13.2 ms                                                | 14.5 ms: 1.10x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.08x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-darwin-arm64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_xml      | 30.5 ms                                                | 39.3 ms: 1.29x slower                                                 |
| genshi_text     | 14.7 ms                                                | 19.9 ms: 1.36x slower                                                 |
| django_template | 19.7 ms                                                | 28.0 ms: 1.42x slower                                                 |
| mako            | 7.44 ms                                                | 11.6 ms: 1.56x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.40x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250510-darwin-arm64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 15.2 ms: 2.11x faster                                                 |
| async_tree_io_tg                 | 673 ms                                                 | 339 ms: 1.98x faster                                                  |
| gc_traversal                     | 2.95 ms                                                | 1.50 ms: 1.96x faster                                                 |
| async_tree_eager_io              | 666 ms                                                 | 347 ms: 1.92x faster                                                  |
| async_tree_io                    | 672 ms                                                 | 358 ms: 1.87x faster                                                  |
| async_tree_eager_io_tg           | 617 ms                                                 | 330 ms: 1.87x faster                                                  |
| async_tree_memoization_tg        | 318 ms                                                 | 187 ms: 1.70x faster                                                  |
| async_tree_none_tg               | 255 ms                                                 | 151 ms: 1.69x faster                                                  |
| mdp                              | 1.49 sec                                               | 930 ms: 1.60x faster                                                  |
| async_tree_none                  | 263 ms                                                 | 171 ms: 1.54x faster                                                  |
| async_tree_memoization           | 310 ms                                                 | 211 ms: 1.47x faster                                                  |
| create_gc_cycles                 | 1.15 ms                                                | 830 us: 1.39x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 397 ms: 1.33x faster                                                  |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 421 ms: 1.25x faster                                                  |
| regex_effbot                     | 2.44 ms                                                | 2.12 ms: 1.15x faster                                                 |
| xml_etree_iterparse              | 75.5 ms                                                | 67.4 ms: 1.12x faster                                                 |
| sqlite_synth                     | 1.55 us                                                | 1.38 us: 1.12x faster                                                 |
| deepcopy                         | 226 us                                                 | 202 us: 1.12x faster                                                  |
| xml_etree_parse                  | 108 ms                                                 | 99.1 ms: 1.09x faster                                                 |
| async_tree_eager_memoization     | 168 ms                                                 | 157 ms: 1.07x faster                                                  |
| regex_dna                        | 143 ms                                                 | 135 ms: 1.06x faster                                                  |
| k_core                           | 1.72 sec                                               | 1.64 sec: 1.05x faster                                                |
| coroutines                       | 19.7 ms                                                | 18.9 ms: 1.04x faster                                                 |
| dulwich_log                      | 29.2 ms                                                | 28.2 ms: 1.04x faster                                                 |
| pathlib                          | 24.7 ms                                                | 24.0 ms: 1.03x faster                                                 |
| asyncio_websockets               | 243 ms                                                 | 237 ms: 1.02x faster                                                  |
| async_generators                 | 299 ms                                                 | 293 ms: 1.02x faster                                                  |
| pidigits                         | 283 ms                                                 | 281 ms: 1.01x faster                                                  |
| regex_v8                         | 15.1 ms                                                | 15.2 ms: 1.01x slower                                                 |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 377 ms: 1.01x slower                                                  |
| float                            | 54.1 ms                                                | 55.2 ms: 1.02x slower                                                 |
| deepcopy_memo                    | 26.0 us                                                | 26.7 us: 1.03x slower                                                 |
| sphinx                           | 613 ms                                                 | 637 ms: 1.04x slower                                                  |
| docutils                         | 1.45 sec                                               | 1.52 sec: 1.05x slower                                                |
| spectral_norm                    | 76.5 ms                                                | 80.6 ms: 1.05x slower                                                 |
| json                             | 3.00 ms                                                | 3.18 ms: 1.06x slower                                                 |
| python_startup                   | 17.8 ms                                                | 18.9 ms: 1.06x slower                                                 |
| deepcopy_reduce                  | 2.01 us                                                | 2.14 us: 1.06x slower                                                 |
| comprehensions                   | 14.0 us                                                | 15.0 us: 1.07x slower                                                 |
| html5lib                         | 33.4 ms                                                | 36.0 ms: 1.08x slower                                                 |
| shortest_path                    | 331 ms                                                 | 357 ms: 1.08x slower                                                  |
| generators                       | 29.4 ms                                                | 32.0 ms: 1.09x slower                                                 |
| pycparser                        | 673 ms                                                 | 736 ms: 1.09x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 380 ms: 1.10x slower                                                  |
| python_startup_no_site           | 13.2 ms                                                | 14.5 ms: 1.10x slower                                                 |
| connected_components             | 300 ms                                                 | 331 ms: 1.10x slower                                                  |
| raytrace                         | 204 ms                                                 | 228 ms: 1.12x slower                                                  |
| bench_mp_pool                    | 65.5 ms                                                | 73.3 ms: 1.12x slower                                                 |
| sympy_integrate                  | 11.1 ms                                                | 12.4 ms: 1.12x slower                                                 |
| json_loads                       | 17.0 us                                                | 19.2 us: 1.13x slower                                                 |
| go                               | 98.5 ms                                                | 111 ms: 1.13x slower                                                  |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 3.55 ms: 1.13x slower                                                 |
| thrift                           | 468 us                                                 | 532 us: 1.14x slower                                                  |
| xml_etree_generate               | 55.4 ms                                                | 63.7 ms: 1.15x slower                                                 |
| scimark_fft                      | 194 ms                                                 | 224 ms: 1.15x slower                                                  |
| sympy_sum                        | 76.2 ms                                                | 88.7 ms: 1.16x slower                                                 |
| scimark_sor                      | 85.8 ms                                                | 100 ms: 1.17x slower                                                  |
| pyflate                          | 311 ms                                                 | 363 ms: 1.17x slower                                                  |
| deltablue                        | 2.57 ms                                                | 3.03 ms: 1.18x slower                                                 |
| sympy_str                        | 144 ms                                                 | 173 ms: 1.20x slower                                                  |
| tomli_loads                      | 1.36 sec                                               | 1.63 sec: 1.20x slower                                                |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 171 ms: 1.20x slower                                                  |
| meteor_contest                   | 69.1 ms                                                | 83.6 ms: 1.21x slower                                                 |
| chaos                            | 41.6 ms                                                | 50.4 ms: 1.21x slower                                                 |
| nqueens                          | 59.5 ms                                                | 74.0 ms: 1.24x slower                                                 |
| xml_etree_process                | 38.9 ms                                                | 48.4 ms: 1.25x slower                                                 |
| 2to3                             | 168 ms                                                 | 210 ms: 1.25x slower                                                  |
| regex_compile                    | 75.9 ms                                                | 95.9 ms: 1.26x slower                                                 |
| fannkuch                         | 250 ms                                                 | 317 ms: 1.27x slower                                                  |
| sympy_expand                     | 233 ms                                                 | 297 ms: 1.27x slower                                                  |
| many_optionals                   | 403 us                                                 | 517 us: 1.28x slower                                                  |
| pprint_pformat                   | 986 ms                                                 | 1.27 sec: 1.29x slower                                                |
| crypto_pyaes                     | 51.4 ms                                                | 66.2 ms: 1.29x slower                                                 |
| genshi_xml                       | 30.5 ms                                                | 39.3 ms: 1.29x slower                                                 |
| pprint_safe_repr                 | 483 ms                                                 | 625 ms: 1.29x slower                                                  |
| logging_format                   | 3.90 us                                                | 5.06 us: 1.30x slower                                                 |
| logging_simple                   | 3.60 us                                                | 4.68 us: 1.30x slower                                                 |
| unpickle_pure_python             | 145 us                                                 | 190 us: 1.31x slower                                                  |
| hexiom                           | 4.38 ms                                                | 5.77 ms: 1.32x slower                                                 |
| async_tree_eager                 | 65.8 ms                                                | 86.8 ms: 1.32x slower                                                 |
| scimark_lu                       | 73.5 ms                                                | 97.8 ms: 1.33x slower                                                 |
| json_dumps                       | 6.19 ms                                                | 8.32 ms: 1.35x slower                                                 |
| richards_super                   | 34.6 ms                                                | 46.6 ms: 1.35x slower                                                 |
| scimark_monte_carlo              | 44.5 ms                                                | 60.3 ms: 1.36x slower                                                 |
| telco                            | 3.92 ms                                                | 5.32 ms: 1.36x slower                                                 |
| genshi_text                      | 14.7 ms                                                | 19.9 ms: 1.36x slower                                                 |
| richards                         | 30.6 ms                                                | 41.6 ms: 1.36x slower                                                 |
| typing_runtime_protocols         | 91.5 us                                                | 125 us: 1.37x slower                                                  |
| pickle_pure_python               | 197 us                                                 | 274 us: 1.39x slower                                                  |
| nbody                            | 67.6 ms                                                | 95.5 ms: 1.41x slower                                                 |
| django_template                  | 19.7 ms                                                | 28.0 ms: 1.42x slower                                                 |
| mako                             | 7.44 ms                                                | 11.6 ms: 1.56x slower                                                 |
| bench_thread_pool                | 483 us                                                 | 760 us: 1.57x slower                                                  |
| coverage                         | 38.5 ms                                                | 66.9 ms: 1.74x slower                                                 |
| async_tree_eager_tg              | 46.9 ms                                                | 130 ms: 2.77x slower                                                  |
| logging_silent                   | 72.5 ns                                                | 377 ns: 5.20x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.08x slower                                                          |

Benchmark hidden because not significant (2): pylint, bpe_tokeniser
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: chameleon, dask, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250510-3.15.0a0-1a87b6e-NOGIL/bm-20250510-darwin-arm64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.051x slower

# HPT report

- Reliability score: 99.49% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.28x