# Results vs. 3.12.0

- fork: python
- ref: bc26f95e8ff60ccca981
- machine: darwin-arm64
- commit hash: bc26f95
- commit date: 2025-03-22
- overall geometric mean: 1.131x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 152 ms: 1.11x faster                                                   |
| docutils       | 1.45 sec                                               | 1.39 sec: 1.05x faster                                                 |
| html5lib       | 33.4 ms                                                | 29.6 ms: 1.13x faster                                                  |
| sphinx         | 613 ms                                                 | 556 ms: 1.10x faster                                                   |
| Geometric mean | (ref)                                                  | 1.09x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg                 | 673 ms                                                 | 336 ms: 2.00x faster                                                   |
| async_tree_io                    | 672 ms                                                 | 342 ms: 1.96x faster                                                   |
| async_tree_eager_io              | 666 ms                                                 | 345 ms: 1.93x faster                                                   |
| async_tree_none_tg               | 255 ms                                                 | 144 ms: 1.77x faster                                                   |
| async_tree_eager_io_tg           | 617 ms                                                 | 349 ms: 1.77x faster                                                   |
| async_tree_memoization_tg        | 318 ms                                                 | 181 ms: 1.76x faster                                                   |
| async_tree_none                  | 263 ms                                                 | 152 ms: 1.73x faster                                                   |
| async_tree_memoization           | 310 ms                                                 | 181 ms: 1.72x faster                                                   |
| coroutines                       | 19.7 ms                                                | 14.6 ms: 1.35x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 400 ms: 1.32x faster                                                   |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 400 ms: 1.32x faster                                                   |
| async_tree_eager_memoization     | 168 ms                                                 | 133 ms: 1.26x faster                                                   |
| async_generators                 | 299 ms                                                 | 255 ms: 1.17x faster                                                   |
| async_tree_eager                 | 65.8 ms                                                | 56.8 ms: 1.16x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 345 ms: 1.08x faster                                                   |
| asyncio_websockets               | 243 ms                                                 | 242 ms: 1.00x faster                                                   |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 376 ms: 1.08x slower                                                   |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 161 ms: 1.14x slower                                                   |
| async_tree_eager_tg              | 46.9 ms                                                | 121 ms: 2.58x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.31x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 54.1 ms                                                | 44.3 ms: 1.22x faster                                                  |
| nbody          | 67.6 ms                                                | 64.8 ms: 1.04x faster                                                  |
| pidigits       | 283 ms                                                 | 279 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                  | 1.09x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 75.9 ms                                                | 64.0 ms: 1.19x faster                                                  |
| regex_effbot   | 2.44 ms                                                | 2.42 ms: 1.01x faster                                                  |
| regex_dna      | 143 ms                                                 | 149 ms: 1.05x slower                                                   |
| regex_v8       | 15.1 ms                                                | 17.0 ms: 1.13x slower                                                  |
| Geometric mean | (ref)                                                  | 1.00x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 1.36 sec                                               | 1.18 sec: 1.15x faster                                                 |
| xml_etree_process    | 38.9 ms                                                | 34.4 ms: 1.13x faster                                                  |
| unpickle_pure_python | 145 us                                                 | 130 us: 1.12x faster                                                   |
| xml_etree_generate   | 55.4 ms                                                | 49.7 ms: 1.12x faster                                                  |
| xml_etree_parse      | 108 ms                                                 | 98.5 ms: 1.10x faster                                                  |
| xml_etree_iterparse  | 75.5 ms                                                | 69.8 ms: 1.08x faster                                                  |
| pickle_pure_python   | 197 us                                                 | 186 us: 1.06x faster                                                   |
| json_loads           | 17.0 us                                                | 17.8 us: 1.04x slower                                                  |
| json_dumps           | 6.19 ms                                                | 7.21 ms: 1.17x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 17.8 ms                                                | 18.3 ms: 1.03x slower                                                  |
| python_startup_no_site | 13.2 ms                                                | 14.1 ms: 1.07x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.05x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 14.7 ms                                                | 13.0 ms: 1.13x faster                                                  |
| genshi_xml      | 30.5 ms                                                | 27.8 ms: 1.10x faster                                                  |
| mako            | 7.44 ms                                                | 7.31 ms: 1.02x faster                                                  |
| django_template | 19.7 ms                                                | 19.4 ms: 1.02x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.07x faster                                                           |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 11.6 ms: 2.76x faster                                                  |
| async_tree_io_tg                 | 673 ms                                                 | 336 ms: 2.00x faster                                                   |
| async_tree_io                    | 672 ms                                                 | 342 ms: 1.96x faster                                                   |
| async_tree_eager_io              | 666 ms                                                 | 345 ms: 1.93x faster                                                   |
| async_tree_none_tg               | 255 ms                                                 | 144 ms: 1.77x faster                                                   |
| async_tree_eager_io_tg           | 617 ms                                                 | 349 ms: 1.77x faster                                                   |
| async_tree_memoization_tg        | 318 ms                                                 | 181 ms: 1.76x faster                                                   |
| async_tree_none                  | 263 ms                                                 | 152 ms: 1.73x faster                                                   |
| async_tree_memoization           | 310 ms                                                 | 181 ms: 1.72x faster                                                   |
| deepcopy                         | 226 us                                                 | 141 us: 1.61x faster                                                   |
| generators                       | 29.4 ms                                                | 18.3 ms: 1.60x faster                                                  |
| deepcopy_memo                    | 26.0 us                                                | 16.5 us: 1.58x faster                                                  |
| comprehensions                   | 14.0 us                                                | 10.2 us: 1.38x faster                                                  |
| coroutines                       | 19.7 ms                                                | 14.6 ms: 1.35x faster                                                  |
| go                               | 98.5 ms                                                | 73.6 ms: 1.34x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 400 ms: 1.32x faster                                                   |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 400 ms: 1.32x faster                                                   |
| deepcopy_reduce                  | 2.01 us                                                | 1.53 us: 1.31x faster                                                  |
| logging_silent                   | 72.5 ns                                                | 57.2 ns: 1.27x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 133 ms: 1.26x faster                                                   |
| raytrace                         | 204 ms                                                 | 165 ms: 1.24x faster                                                   |
| dulwich_log                      | 29.2 ms                                                | 23.6 ms: 1.24x faster                                                  |
| deltablue                        | 2.57 ms                                                | 2.10 ms: 1.22x faster                                                  |
| float                            | 54.1 ms                                                | 44.3 ms: 1.22x faster                                                  |
| pylint                           | 182 ms                                                 | 151 ms: 1.20x faster                                                   |
| scimark_sor                      | 85.8 ms                                                | 71.9 ms: 1.19x faster                                                  |
| regex_compile                    | 75.9 ms                                                | 64.0 ms: 1.19x faster                                                  |
| logging_simple                   | 3.60 us                                                | 3.07 us: 1.17x faster                                                  |
| async_generators                 | 299 ms                                                 | 255 ms: 1.17x faster                                                   |
| async_tree_eager                 | 65.8 ms                                                | 56.8 ms: 1.16x faster                                                  |
| logging_format                   | 3.90 us                                                | 3.38 us: 1.15x faster                                                  |
| tomli_loads                      | 1.36 sec                                               | 1.18 sec: 1.15x faster                                                 |
| genshi_text                      | 14.7 ms                                                | 13.0 ms: 1.13x faster                                                  |
| k_core                           | 1.72 sec                                               | 1.52 sec: 1.13x faster                                                 |
| xml_etree_process                | 38.9 ms                                                | 34.4 ms: 1.13x faster                                                  |
| html5lib                         | 33.4 ms                                                | 29.6 ms: 1.13x faster                                                  |
| chaos                            | 41.6 ms                                                | 36.9 ms: 1.13x faster                                                  |
| thrift                           | 468 us                                                 | 415 us: 1.13x faster                                                   |
| hexiom                           | 4.38 ms                                                | 3.91 ms: 1.12x faster                                                  |
| unpickle_pure_python             | 145 us                                                 | 130 us: 1.12x faster                                                   |
| sqlalchemy_declarative           | 61.9 ms                                                | 55.5 ms: 1.12x faster                                                  |
| xml_etree_generate               | 55.4 ms                                                | 49.7 ms: 1.12x faster                                                  |
| scimark_monte_carlo              | 44.5 ms                                                | 40.1 ms: 1.11x faster                                                  |
| 2to3                             | 168 ms                                                 | 152 ms: 1.11x faster                                                   |
| sphinx                           | 613 ms                                                 | 556 ms: 1.10x faster                                                   |
| sympy_str                        | 144 ms                                                 | 131 ms: 1.10x faster                                                   |
| genshi_xml                       | 30.5 ms                                                | 27.8 ms: 1.10x faster                                                  |
| bench_mp_pool                    | 65.5 ms                                                | 59.8 ms: 1.10x faster                                                  |
| xml_etree_parse                  | 108 ms                                                 | 98.5 ms: 1.10x faster                                                  |
| pprint_pformat                   | 986 ms                                                 | 901 ms: 1.09x faster                                                   |
| sympy_sum                        | 76.2 ms                                                | 70.2 ms: 1.09x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 345 ms: 1.08x faster                                                   |
| pprint_safe_repr                 | 483 ms                                                 | 446 ms: 1.08x faster                                                   |
| bpe_tokeniser                    | 3.28 sec                                               | 3.03 sec: 1.08x faster                                                 |
| xml_etree_iterparse              | 75.5 ms                                                | 69.8 ms: 1.08x faster                                                  |
| sympy_integrate                  | 11.1 ms                                                | 10.3 ms: 1.08x faster                                                  |
| pathlib                          | 24.7 ms                                                | 23.0 ms: 1.07x faster                                                  |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 2.93 ms: 1.07x faster                                                  |
| scimark_fft                      | 194 ms                                                 | 182 ms: 1.07x faster                                                   |
| pycparser                        | 673 ms                                                 | 633 ms: 1.06x faster                                                   |
| sqlalchemy_imperative            | 6.60 ms                                                | 6.21 ms: 1.06x faster                                                  |
| sympy_expand                     | 233 ms                                                 | 220 ms: 1.06x faster                                                   |
| pickle_pure_python               | 197 us                                                 | 186 us: 1.06x faster                                                   |
| richards_super                   | 34.6 ms                                                | 32.9 ms: 1.05x faster                                                  |
| bench_thread_pool                | 483 us                                                 | 461 us: 1.05x faster                                                   |
| docutils                         | 1.45 sec                                               | 1.39 sec: 1.05x faster                                                 |
| mdp                              | 1.49 sec                                               | 1.43 sec: 1.05x faster                                                 |
| nbody                            | 67.6 ms                                                | 64.8 ms: 1.04x faster                                                  |
| typing_runtime_protocols         | 91.5 us                                                | 88.2 us: 1.04x faster                                                  |
| scimark_lu                       | 73.5 ms                                                | 71.1 ms: 1.03x faster                                                  |
| richards                         | 30.6 ms                                                | 29.7 ms: 1.03x faster                                                  |
| spectral_norm                    | 76.5 ms                                                | 74.4 ms: 1.03x faster                                                  |
| nqueens                          | 59.5 ms                                                | 57.9 ms: 1.03x faster                                                  |
| sqlite_synth                     | 1.55 us                                                | 1.51 us: 1.02x faster                                                  |
| mako                             | 7.44 ms                                                | 7.31 ms: 1.02x faster                                                  |
| django_template                  | 19.7 ms                                                | 19.4 ms: 1.02x faster                                                  |
| pyflate                          | 311 ms                                                 | 306 ms: 1.02x faster                                                   |
| dask                             | 779 ms                                                 | 768 ms: 1.01x faster                                                   |
| shortest_path                    | 331 ms                                                 | 326 ms: 1.01x faster                                                   |
| pidigits                         | 283 ms                                                 | 279 ms: 1.01x faster                                                   |
| regex_effbot                     | 2.44 ms                                                | 2.42 ms: 1.01x faster                                                  |
| asyncio_websockets               | 243 ms                                                 | 242 ms: 1.00x faster                                                   |
| json                             | 3.00 ms                                                | 3.05 ms: 1.02x slower                                                  |
| meteor_contest                   | 69.1 ms                                                | 70.3 ms: 1.02x slower                                                  |
| python_startup                   | 17.8 ms                                                | 18.3 ms: 1.03x slower                                                  |
| json_loads                       | 17.0 us                                                | 17.8 us: 1.04x slower                                                  |
| regex_dna                        | 143 ms                                                 | 149 ms: 1.05x slower                                                   |
| gc_traversal                     | 2.95 ms                                                | 3.09 ms: 1.05x slower                                                  |
| crypto_pyaes                     | 51.4 ms                                                | 54.2 ms: 1.05x slower                                                  |
| many_optionals                   | 403 us                                                 | 428 us: 1.06x slower                                                   |
| python_startup_no_site           | 13.2 ms                                                | 14.1 ms: 1.07x slower                                                  |
| fannkuch                         | 250 ms                                                 | 270 ms: 1.08x slower                                                   |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 376 ms: 1.08x slower                                                   |
| create_gc_cycles                 | 1.15 ms                                                | 1.28 ms: 1.11x slower                                                  |
| regex_v8                         | 15.1 ms                                                | 17.0 ms: 1.13x slower                                                  |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 161 ms: 1.14x slower                                                   |
| telco                            | 3.92 ms                                                | 4.49 ms: 1.15x slower                                                  |
| coverage                         | 38.5 ms                                                | 44.8 ms: 1.16x slower                                                  |
| json_dumps                       | 6.19 ms                                                | 7.21 ms: 1.17x slower                                                  |
| async_tree_eager_tg              | 46.9 ms                                                | 121 ms: 2.58x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.13x faster                                                           |

Benchmark hidden because not significant (1): connected_components
Ignored benchmarks (9) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250322-3.14.0a6+-bc26f95-CLANG/bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.131x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 1.11x