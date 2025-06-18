# Results vs. 3.12.0

- fork: python
- ref: fba5dded6df3c2b19435
- machine: darwin-arm64
- commit hash: fba5dde
- commit date: 2025-06-17
- overall geometric mean: 1.045x slower
- HPT reliability: 99.82%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 191 ms: 1.13x slower                                                  |
| docutils       | 1.45 sec                                               | 1.63 sec: 1.12x slower                                                |
| sphinx         | 613 ms                                                 | 659 ms: 1.07x slower                                                  |
| Geometric mean | (ref)                                                  | 1.08x slower                                                          |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager_io              | 666 ms                                                 | 390 ms: 1.71x faster                                                  |
| async_tree_io_tg                 | 673 ms                                                 | 397 ms: 1.69x faster                                                  |
| async_tree_io                    | 672 ms                                                 | 405 ms: 1.66x faster                                                  |
| async_tree_memoization_tg        | 318 ms                                                 | 204 ms: 1.56x faster                                                  |
| async_tree_eager_io_tg           | 617 ms                                                 | 400 ms: 1.54x faster                                                  |
| async_tree_none_tg               | 255 ms                                                 | 168 ms: 1.52x faster                                                  |
| async_tree_none                  | 263 ms                                                 | 175 ms: 1.51x faster                                                  |
| async_tree_memoization           | 310 ms                                                 | 207 ms: 1.50x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 447 ms: 1.18x faster                                                  |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 452 ms: 1.17x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 151 ms: 1.11x faster                                                  |
| coroutines                       | 19.7 ms                                                | 18.4 ms: 1.07x faster                                                 |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 393 ms: 1.05x slower                                                  |
| async_generators                 | 299 ms                                                 | 329 ms: 1.10x slower                                                  |
| async_tree_eager                 | 65.8 ms                                                | 73.8 ms: 1.12x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 426 ms: 1.23x slower                                                  |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 182 ms: 1.28x slower                                                  |
| async_tree_eager_tg              | 46.9 ms                                                | 142 ms: 3.02x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.13x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 54.1 ms                                                | 51.6 ms: 1.05x faster                                                 |
| pidigits       | 283 ms                                                 | 285 ms: 1.01x slower                                                  |
| nbody          | 67.6 ms                                                | 80.0 ms: 1.18x slower                                                 |
| Geometric mean | (ref)                                                  | 1.04x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.44 ms                                                | 2.22 ms: 1.10x faster                                                 |
| regex_compile  | 75.9 ms                                                | 76.4 ms: 1.01x slower                                                 |
| regex_dna      | 143 ms                                                 | 145 ms: 1.02x slower                                                  |
| regex_v8       | 15.1 ms                                                | 17.4 ms: 1.15x slower                                                 |
| Geometric mean | (ref)                                                  | 1.02x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_iterparse  | 75.5 ms                                                | 77.1 ms: 1.02x slower                                                 |
| unpickle_pure_python | 145 us                                                 | 150 us: 1.03x slower                                                  |
| xml_etree_parse      | 108 ms                                                 | 112 ms: 1.04x slower                                                  |
| tomli_loads          | 1.36 sec                                               | 1.41 sec: 1.04x slower                                                |
| xml_etree_process    | 38.9 ms                                                | 43.4 ms: 1.12x slower                                                 |
| pickle_pure_python   | 197 us                                                 | 221 us: 1.12x slower                                                  |
| xml_etree_generate   | 55.4 ms                                                | 64.3 ms: 1.16x slower                                                 |
| json_dumps           | 6.19 ms                                                | 8.11 ms: 1.31x slower                                                 |
| json_loads           | 17.0 us                                                | 22.8 us: 1.34x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.13x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 17.8 ms                                                | 18.7 ms: 1.05x slower                                                 |
| python_startup_no_site | 13.2 ms                                                | 13.9 ms: 1.06x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.05x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 14.7 ms                                                | 15.9 ms: 1.08x slower                                                 |
| mako            | 7.44 ms                                                | 8.17 ms: 1.10x slower                                                 |
| genshi_xml      | 30.5 ms                                                | 33.8 ms: 1.11x slower                                                 |
| django_template | 19.7 ms                                                | 25.8 ms: 1.31x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.15x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 16.2 ms: 1.98x faster                                                 |
| async_tree_eager_io              | 666 ms                                                 | 390 ms: 1.71x faster                                                  |
| async_tree_io_tg                 | 673 ms                                                 | 397 ms: 1.69x faster                                                  |
| mdp                              | 1.49 sec                                               | 895 ms: 1.67x faster                                                  |
| async_tree_io                    | 672 ms                                                 | 405 ms: 1.66x faster                                                  |
| async_tree_memoization_tg        | 318 ms                                                 | 204 ms: 1.56x faster                                                  |
| async_tree_eager_io_tg           | 617 ms                                                 | 400 ms: 1.54x faster                                                  |
| async_tree_none_tg               | 255 ms                                                 | 168 ms: 1.52x faster                                                  |
| async_tree_none                  | 263 ms                                                 | 175 ms: 1.51x faster                                                  |
| async_tree_memoization           | 310 ms                                                 | 207 ms: 1.50x faster                                                  |
| deepcopy_memo                    | 26.0 us                                                | 19.6 us: 1.33x faster                                                 |
| generators                       | 29.4 ms                                                | 23.4 ms: 1.26x faster                                                 |
| go                               | 98.5 ms                                                | 79.8 ms: 1.23x faster                                                 |
| deepcopy                         | 226 us                                                 | 190 us: 1.19x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 447 ms: 1.18x faster                                                  |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 452 ms: 1.17x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 151 ms: 1.11x faster                                                  |
| regex_effbot                     | 2.44 ms                                                | 2.22 ms: 1.10x faster                                                 |
| k_core                           | 1.72 sec                                               | 1.59 sec: 1.08x faster                                                |
| coroutines                       | 19.7 ms                                                | 18.4 ms: 1.07x faster                                                 |
| dulwich_log                      | 29.2 ms                                                | 27.3 ms: 1.07x faster                                                 |
| float                            | 54.1 ms                                                | 51.6 ms: 1.05x faster                                                 |
| pathlib                          | 24.7 ms                                                | 23.8 ms: 1.04x faster                                                 |
| comprehensions                   | 14.0 us                                                | 13.6 us: 1.03x faster                                                 |
| pyflate                          | 311 ms                                                 | 304 ms: 1.02x faster                                                  |
| dask                             | 779 ms                                                 | 772 ms: 1.01x faster                                                  |
| regex_compile                    | 75.9 ms                                                | 76.4 ms: 1.01x slower                                                 |
| pidigits                         | 283 ms                                                 | 285 ms: 1.01x slower                                                  |
| deepcopy_reduce                  | 2.01 us                                                | 2.04 us: 1.01x slower                                                 |
| regex_dna                        | 143 ms                                                 | 145 ms: 1.02x slower                                                  |
| xml_etree_iterparse              | 75.5 ms                                                | 77.1 ms: 1.02x slower                                                 |
| unpickle_pure_python             | 145 us                                                 | 150 us: 1.03x slower                                                  |
| shortest_path                    | 331 ms                                                 | 342 ms: 1.04x slower                                                  |
| xml_etree_parse                  | 108 ms                                                 | 112 ms: 1.04x slower                                                  |
| tomli_loads                      | 1.36 sec                                               | 1.41 sec: 1.04x slower                                                |
| raytrace                         | 204 ms                                                 | 214 ms: 1.05x slower                                                  |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 393 ms: 1.05x slower                                                  |
| scimark_monte_carlo              | 44.5 ms                                                | 46.8 ms: 1.05x slower                                                 |
| deltablue                        | 2.57 ms                                                | 2.70 ms: 1.05x slower                                                 |
| connected_components             | 300 ms                                                 | 315 ms: 1.05x slower                                                  |
| python_startup                   | 17.8 ms                                                | 18.7 ms: 1.05x slower                                                 |
| python_startup_no_site           | 13.2 ms                                                | 13.9 ms: 1.06x slower                                                 |
| scimark_sor                      | 85.8 ms                                                | 91.1 ms: 1.06x slower                                                 |
| spectral_norm                    | 76.5 ms                                                | 81.9 ms: 1.07x slower                                                 |
| chaos                            | 41.6 ms                                                | 44.7 ms: 1.07x slower                                                 |
| sphinx                           | 613 ms                                                 | 659 ms: 1.07x slower                                                  |
| genshi_text                      | 14.7 ms                                                | 15.9 ms: 1.08x slower                                                 |
| gc_traversal                     | 2.95 ms                                                | 3.20 ms: 1.09x slower                                                 |
| mako                             | 7.44 ms                                                | 8.17 ms: 1.10x slower                                                 |
| sympy_integrate                  | 11.1 ms                                                | 12.2 ms: 1.10x slower                                                 |
| async_generators                 | 299 ms                                                 | 329 ms: 1.10x slower                                                  |
| genshi_xml                       | 30.5 ms                                                | 33.8 ms: 1.11x slower                                                 |
| xml_etree_process                | 38.9 ms                                                | 43.4 ms: 1.12x slower                                                 |
| docutils                         | 1.45 sec                                               | 1.63 sec: 1.12x slower                                                |
| async_tree_eager                 | 65.8 ms                                                | 73.8 ms: 1.12x slower                                                 |
| pickle_pure_python               | 197 us                                                 | 221 us: 1.12x slower                                                  |
| logging_format                   | 3.90 us                                                | 4.39 us: 1.13x slower                                                 |
| logging_simple                   | 3.60 us                                                | 4.07 us: 1.13x slower                                                 |
| bpe_tokeniser                    | 3.28 sec                                               | 3.71 sec: 1.13x slower                                                |
| bench_thread_pool                | 483 us                                                 | 546 us: 1.13x slower                                                  |
| hexiom                           | 4.38 ms                                                | 4.96 ms: 1.13x slower                                                 |
| 2to3                             | 168 ms                                                 | 191 ms: 1.13x slower                                                  |
| sympy_sum                        | 76.2 ms                                                | 86.7 ms: 1.14x slower                                                 |
| bench_mp_pool                    | 65.5 ms                                                | 75.2 ms: 1.15x slower                                                 |
| nqueens                          | 59.5 ms                                                | 68.3 ms: 1.15x slower                                                 |
| regex_v8                         | 15.1 ms                                                | 17.4 ms: 1.15x slower                                                 |
| xml_etree_generate               | 55.4 ms                                                | 64.3 ms: 1.16x slower                                                 |
| crypto_pyaes                     | 51.4 ms                                                | 60.4 ms: 1.17x slower                                                 |
| pycparser                        | 673 ms                                                 | 792 ms: 1.18x slower                                                  |
| sympy_str                        | 144 ms                                                 | 169 ms: 1.18x slower                                                  |
| meteor_contest                   | 69.1 ms                                                | 81.4 ms: 1.18x slower                                                 |
| nbody                            | 67.6 ms                                                | 80.0 ms: 1.18x slower                                                 |
| richards_super                   | 34.6 ms                                                | 41.0 ms: 1.19x slower                                                 |
| richards                         | 30.6 ms                                                | 36.5 ms: 1.20x slower                                                 |
| scimark_lu                       | 73.5 ms                                                | 88.6 ms: 1.21x slower                                                 |
| create_gc_cycles                 | 1.15 ms                                                | 1.40 ms: 1.21x slower                                                 |
| sqlite_synth                     | 1.55 us                                                | 1.90 us: 1.23x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 426 ms: 1.23x slower                                                  |
| thrift                           | 468 us                                                 | 575 us: 1.23x slower                                                  |
| scimark_fft                      | 194 ms                                                 | 245 ms: 1.26x slower                                                  |
| sympy_expand                     | 233 ms                                                 | 296 ms: 1.27x slower                                                  |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 182 ms: 1.28x slower                                                  |
| json                             | 3.00 ms                                                | 3.85 ms: 1.28x slower                                                 |
| json_dumps                       | 6.19 ms                                                | 8.11 ms: 1.31x slower                                                 |
| django_template                  | 19.7 ms                                                | 25.8 ms: 1.31x slower                                                 |
| many_optionals                   | 403 us                                                 | 536 us: 1.33x slower                                                  |
| json_loads                       | 17.0 us                                                | 22.8 us: 1.34x slower                                                 |
| typing_runtime_protocols         | 91.5 us                                                | 125 us: 1.36x slower                                                  |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 4.32 ms: 1.37x slower                                                 |
| fannkuch                         | 250 ms                                                 | 349 ms: 1.40x slower                                                  |
| pprint_pformat                   | 986 ms                                                 | 1.40 sec: 1.42x slower                                                |
| pprint_safe_repr                 | 483 ms                                                 | 693 ms: 1.43x slower                                                  |
| telco                            | 3.92 ms                                                | 5.63 ms: 1.44x slower                                                 |
| coverage                         | 38.5 ms                                                | 60.8 ms: 1.58x slower                                                 |
| async_tree_eager_tg              | 46.9 ms                                                | 142 ms: 3.02x slower                                                  |
| logging_silent                   | 72.5 ns                                                | 417 ns: 5.75x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.06x slower                                                          |

Benchmark hidden because not significant (3): pylint, asyncio_websockets, html5lib
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250617-3.15.0a0-fba5dde-JIT/bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.045x slower

# HPT report

- Reliability score: 99.82% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.11x