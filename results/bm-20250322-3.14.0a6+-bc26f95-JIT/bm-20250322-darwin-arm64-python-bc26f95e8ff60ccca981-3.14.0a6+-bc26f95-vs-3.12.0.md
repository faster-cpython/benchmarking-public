# Results vs. 3.12.0

- fork: python
- ref: bc26f95e8ff60ccca981
- machine: darwin-arm64
- commit hash: bc26f95
- commit date: 2025-03-22
- overall geometric mean: 1.042x faster
- HPT reliability: 87.26%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 170 ms: 1.01x slower                                                   |
| docutils       | 1.45 sec                                               | 1.48 sec: 1.02x slower                                                 |
| html5lib       | 33.4 ms                                                | 32.3 ms: 1.03x faster                                                  |
| sphinx         | 613 ms                                                 | 598 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                  | 1.01x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg                 | 673 ms                                                 | 381 ms: 1.77x faster                                                   |
| async_tree_eager_io              | 666 ms                                                 | 385 ms: 1.73x faster                                                   |
| async_tree_io                    | 672 ms                                                 | 391 ms: 1.72x faster                                                   |
| async_tree_memoization_tg        | 318 ms                                                 | 198 ms: 1.60x faster                                                   |
| async_tree_eager_io_tg           | 617 ms                                                 | 387 ms: 1.59x faster                                                   |
| async_tree_none_tg               | 255 ms                                                 | 161 ms: 1.58x faster                                                   |
| async_tree_none                  | 263 ms                                                 | 167 ms: 1.57x faster                                                   |
| async_tree_memoization           | 310 ms                                                 | 202 ms: 1.54x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 417 ms: 1.27x faster                                                   |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 416 ms: 1.27x faster                                                   |
| async_tree_eager_memoization     | 168 ms                                                 | 143 ms: 1.17x faster                                                   |
| coroutines                       | 19.7 ms                                                | 17.3 ms: 1.14x faster                                                  |
| async_generators                 | 299 ms                                                 | 283 ms: 1.05x faster                                                   |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 360 ms: 1.04x faster                                                   |
| async_tree_eager                 | 65.8 ms                                                | 65.4 ms: 1.01x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 392 ms: 1.13x slower                                                   |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 177 ms: 1.24x slower                                                   |
| async_tree_eager_tg              | 46.9 ms                                                | 134 ms: 2.86x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.20x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 54.1 ms                                                | 45.7 ms: 1.18x faster                                                  |
| pidigits       | 283 ms                                                 | 283 ms: 1.00x slower                                                   |
| nbody          | 67.6 ms                                                | 69.6 ms: 1.03x slower                                                  |
| Geometric mean | (ref)                                                  | 1.05x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 2.44 ms                                                | 2.27 ms: 1.07x faster                                                  |
| regex_compile  | 75.9 ms                                                | 73.5 ms: 1.03x faster                                                  |
| regex_dna      | 143 ms                                                 | 140 ms: 1.02x faster                                                   |
| regex_v8       | 15.1 ms                                                | 15.9 ms: 1.05x slower                                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_parse      | 108 ms                                                 | 99.1 ms: 1.09x faster                                                  |
| tomli_loads          | 1.36 sec                                               | 1.25 sec: 1.08x faster                                                 |
| xml_etree_generate   | 55.4 ms                                                | 51.4 ms: 1.08x faster                                                  |
| xml_etree_process    | 38.9 ms                                                | 36.5 ms: 1.06x faster                                                  |
| unpickle_pure_python | 145 us                                                 | 140 us: 1.04x faster                                                   |
| xml_etree_iterparse  | 75.5 ms                                                | 72.5 ms: 1.04x faster                                                  |
| json_loads           | 17.0 us                                                | 17.8 us: 1.05x slower                                                  |
| pickle_pure_python   | 197 us                                                 | 212 us: 1.08x slower                                                   |
| json_dumps           | 6.19 ms                                                | 7.53 ms: 1.22x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 17.8 ms                                                | 18.7 ms: 1.05x slower                                                  |
| python_startup_no_site | 13.2 ms                                                | 14.2 ms: 1.08x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 7.44 ms                                                | 6.69 ms: 1.11x faster                                                  |
| genshi_xml      | 30.5 ms                                                | 32.1 ms: 1.05x slower                                                  |
| genshi_text     | 14.7 ms                                                | 15.4 ms: 1.05x slower                                                  |
| django_template | 19.7 ms                                                | 22.7 ms: 1.15x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.03x slower                                                           |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 12.8 ms: 2.52x faster                                                  |
| async_tree_io_tg                 | 673 ms                                                 | 381 ms: 1.77x faster                                                   |
| async_tree_eager_io              | 666 ms                                                 | 385 ms: 1.73x faster                                                   |
| async_tree_io                    | 672 ms                                                 | 391 ms: 1.72x faster                                                   |
| async_tree_memoization_tg        | 318 ms                                                 | 198 ms: 1.60x faster                                                   |
| async_tree_eager_io_tg           | 617 ms                                                 | 387 ms: 1.59x faster                                                   |
| async_tree_none_tg               | 255 ms                                                 | 161 ms: 1.58x faster                                                   |
| async_tree_none                  | 263 ms                                                 | 167 ms: 1.57x faster                                                   |
| async_tree_memoization           | 310 ms                                                 | 202 ms: 1.54x faster                                                   |
| deepcopy                         | 226 us                                                 | 162 us: 1.39x faster                                                   |
| deepcopy_memo                    | 26.0 us                                                | 20.3 us: 1.28x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 417 ms: 1.27x faster                                                   |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 416 ms: 1.27x faster                                                   |
| spectral_norm                    | 76.5 ms                                                | 64.3 ms: 1.19x faster                                                  |
| float                            | 54.1 ms                                                | 45.7 ms: 1.18x faster                                                  |
| generators                       | 29.4 ms                                                | 25.0 ms: 1.18x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 143 ms: 1.17x faster                                                   |
| deepcopy_reduce                  | 2.01 us                                                | 1.74 us: 1.16x faster                                                  |
| coroutines                       | 19.7 ms                                                | 17.3 ms: 1.14x faster                                                  |
| dulwich_log                      | 29.2 ms                                                | 25.9 ms: 1.13x faster                                                  |
| comprehensions                   | 14.0 us                                                | 12.4 us: 1.13x faster                                                  |
| deltablue                        | 2.57 ms                                                | 2.29 ms: 1.12x faster                                                  |
| mako                             | 7.44 ms                                                | 6.69 ms: 1.11x faster                                                  |
| k_core                           | 1.72 sec                                               | 1.55 sec: 1.11x faster                                                 |
| pylint                           | 182 ms                                                 | 167 ms: 1.09x faster                                                   |
| xml_etree_parse                  | 108 ms                                                 | 99.1 ms: 1.09x faster                                                  |
| bpe_tokeniser                    | 3.28 sec                                               | 3.02 sec: 1.09x faster                                                 |
| tomli_loads                      | 1.36 sec                                               | 1.25 sec: 1.08x faster                                                 |
| xml_etree_generate               | 55.4 ms                                                | 51.4 ms: 1.08x faster                                                  |
| regex_effbot                     | 2.44 ms                                                | 2.27 ms: 1.07x faster                                                  |
| bench_mp_pool                    | 65.5 ms                                                | 61.4 ms: 1.07x faster                                                  |
| xml_etree_process                | 38.9 ms                                                | 36.5 ms: 1.06x faster                                                  |
| raytrace                         | 204 ms                                                 | 192 ms: 1.06x faster                                                   |
| async_generators                 | 299 ms                                                 | 283 ms: 1.05x faster                                                   |
| unpickle_pure_python             | 145 us                                                 | 140 us: 1.04x faster                                                   |
| xml_etree_iterparse              | 75.5 ms                                                | 72.5 ms: 1.04x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 360 ms: 1.04x faster                                                   |
| html5lib                         | 33.4 ms                                                | 32.3 ms: 1.03x faster                                                  |
| regex_compile                    | 75.9 ms                                                | 73.5 ms: 1.03x faster                                                  |
| pathlib                          | 24.7 ms                                                | 23.9 ms: 1.03x faster                                                  |
| scimark_fft                      | 194 ms                                                 | 189 ms: 1.03x faster                                                   |
| thrift                           | 468 us                                                 | 456 us: 1.03x faster                                                   |
| sphinx                           | 613 ms                                                 | 598 ms: 1.02x faster                                                   |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 3.07 ms: 1.02x faster                                                  |
| logging_silent                   | 72.5 ns                                                | 71.3 ns: 1.02x faster                                                  |
| regex_dna                        | 143 ms                                                 | 140 ms: 1.02x faster                                                   |
| dask                             | 779 ms                                                 | 769 ms: 1.01x faster                                                   |
| sqlalchemy_declarative           | 61.9 ms                                                | 61.4 ms: 1.01x faster                                                  |
| async_tree_eager                 | 65.8 ms                                                | 65.4 ms: 1.01x faster                                                  |
| mdp                              | 1.49 sec                                               | 1.48 sec: 1.01x faster                                                 |
| pidigits                         | 283 ms                                                 | 283 ms: 1.00x slower                                                   |
| sqlite_synth                     | 1.55 us                                                | 1.55 us: 1.01x slower                                                  |
| logging_format                   | 3.90 us                                                | 3.92 us: 1.01x slower                                                  |
| 2to3                             | 168 ms                                                 | 170 ms: 1.01x slower                                                   |
| shortest_path                    | 331 ms                                                 | 336 ms: 1.02x slower                                                   |
| connected_components             | 300 ms                                                 | 304 ms: 1.02x slower                                                   |
| sympy_str                        | 144 ms                                                 | 146 ms: 1.02x slower                                                   |
| richards_super                   | 34.6 ms                                                | 35.3 ms: 1.02x slower                                                  |
| go                               | 98.5 ms                                                | 100 ms: 1.02x slower                                                   |
| docutils                         | 1.45 sec                                               | 1.48 sec: 1.02x slower                                                 |
| json                             | 3.00 ms                                                | 3.07 ms: 1.02x slower                                                  |
| scimark_sor                      | 85.8 ms                                                | 87.8 ms: 1.02x slower                                                  |
| nbody                            | 67.6 ms                                                | 69.6 ms: 1.03x slower                                                  |
| pyflate                          | 311 ms                                                 | 321 ms: 1.03x slower                                                   |
| richards                         | 30.6 ms                                                | 31.7 ms: 1.04x slower                                                  |
| scimark_monte_carlo              | 44.5 ms                                                | 46.3 ms: 1.04x slower                                                  |
| json_loads                       | 17.0 us                                                | 17.8 us: 1.05x slower                                                  |
| bench_thread_pool                | 483 us                                                 | 505 us: 1.05x slower                                                   |
| pprint_safe_repr                 | 483 ms                                                 | 507 ms: 1.05x slower                                                   |
| pprint_pformat                   | 986 ms                                                 | 1.04 sec: 1.05x slower                                                 |
| python_startup                   | 17.8 ms                                                | 18.7 ms: 1.05x slower                                                  |
| genshi_xml                       | 30.5 ms                                                | 32.1 ms: 1.05x slower                                                  |
| genshi_text                      | 14.7 ms                                                | 15.4 ms: 1.05x slower                                                  |
| regex_v8                         | 15.1 ms                                                | 15.9 ms: 1.05x slower                                                  |
| chaos                            | 41.6 ms                                                | 43.8 ms: 1.05x slower                                                  |
| sqlalchemy_imperative            | 6.60 ms                                                | 6.96 ms: 1.06x slower                                                  |
| sympy_integrate                  | 11.1 ms                                                | 11.7 ms: 1.06x slower                                                  |
| pycparser                        | 673 ms                                                 | 713 ms: 1.06x slower                                                   |
| gc_traversal                     | 2.95 ms                                                | 3.13 ms: 1.06x slower                                                  |
| sympy_expand                     | 233 ms                                                 | 250 ms: 1.07x slower                                                   |
| typing_runtime_protocols         | 91.5 us                                                | 98.3 us: 1.07x slower                                                  |
| pickle_pure_python               | 197 us                                                 | 212 us: 1.08x slower                                                   |
| python_startup_no_site           | 13.2 ms                                                | 14.2 ms: 1.08x slower                                                  |
| scimark_lu                       | 73.5 ms                                                | 79.9 ms: 1.09x slower                                                  |
| meteor_contest                   | 69.1 ms                                                | 75.8 ms: 1.10x slower                                                  |
| nqueens                          | 59.5 ms                                                | 66.0 ms: 1.11x slower                                                  |
| create_gc_cycles                 | 1.15 ms                                                | 1.29 ms: 1.12x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 392 ms: 1.13x slower                                                   |
| telco                            | 3.92 ms                                                | 4.49 ms: 1.15x slower                                                  |
| fannkuch                         | 250 ms                                                 | 287 ms: 1.15x slower                                                   |
| django_template                  | 19.7 ms                                                | 22.7 ms: 1.15x slower                                                  |
| hexiom                           | 4.38 ms                                                | 5.06 ms: 1.16x slower                                                  |
| many_optionals                   | 403 us                                                 | 473 us: 1.17x slower                                                   |
| crypto_pyaes                     | 51.4 ms                                                | 60.6 ms: 1.18x slower                                                  |
| json_dumps                       | 6.19 ms                                                | 7.53 ms: 1.22x slower                                                  |
| coverage                         | 38.5 ms                                                | 47.1 ms: 1.22x slower                                                  |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 177 ms: 1.24x slower                                                   |
| async_tree_eager_tg              | 46.9 ms                                                | 134 ms: 2.86x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.04x faster                                                           |

Benchmark hidden because not significant (3): sympy_sum, asyncio_websockets, logging_simple
Ignored benchmarks (9) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250322-3.14.0a6+-bc26f95-JIT/bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.042x faster

# HPT report

- Reliability score: 87.26% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.12x