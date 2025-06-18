# Results vs. 3.12.0

- fork: python
- ref: fba5dded6df3c2b19435
- machine: darwin-arm64
- commit hash: fba5dde
- commit date: 2025-06-17
- overall geometric mean: 1.065x slower
- HPT reliability: 99.89%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.27x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 202 ms: 1.20x slower                                                  |
| docutils       | 1.45 sec                                               | 1.59 sec: 1.09x slower                                                |
| html5lib       | 33.4 ms                                                | 34.3 ms: 1.03x slower                                                 |
| sphinx         | 613 ms                                                 | 678 ms: 1.11x slower                                                  |
| Geometric mean | (ref)                                                  | 1.10x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io_tg                 | 673 ms                                                 | 327 ms: 2.06x faster                                                  |
| async_tree_eager_io              | 666 ms                                                 | 332 ms: 2.01x faster                                                  |
| async_tree_io                    | 672 ms                                                 | 343 ms: 1.96x faster                                                  |
| async_tree_eager_io_tg           | 617 ms                                                 | 317 ms: 1.94x faster                                                  |
| async_tree_memoization_tg        | 318 ms                                                 | 180 ms: 1.77x faster                                                  |
| async_tree_none_tg               | 255 ms                                                 | 146 ms: 1.75x faster                                                  |
| async_tree_none                  | 263 ms                                                 | 164 ms: 1.61x faster                                                  |
| async_tree_memoization           | 310 ms                                                 | 198 ms: 1.56x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 413 ms: 1.28x faster                                                  |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 432 ms: 1.22x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 148 ms: 1.13x faster                                                  |
| coroutines                       | 19.7 ms                                                | 18.0 ms: 1.09x faster                                                 |
| asyncio_websockets               | 243 ms                                                 | 238 ms: 1.02x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 391 ms: 1.04x slower                                                  |
| async_generators                 | 299 ms                                                 | 324 ms: 1.08x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 397 ms: 1.14x slower                                                  |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 163 ms: 1.15x slower                                                  |
| async_tree_eager                 | 65.8 ms                                                | 81.9 ms: 1.24x slower                                                 |
| async_tree_eager_tg              | 46.9 ms                                                | 127 ms: 2.71x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.23x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 54.1 ms                                                | 48.6 ms: 1.11x faster                                                 |
| pidigits       | 283 ms                                                 | 281 ms: 1.00x faster                                                  |
| nbody          | 67.6 ms                                                | 93.1 ms: 1.38x slower                                                 |
| Geometric mean | (ref)                                                  | 1.07x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.44 ms                                                | 2.22 ms: 1.10x faster                                                 |
| regex_dna      | 143 ms                                                 | 145 ms: 1.01x slower                                                  |
| regex_compile  | 75.9 ms                                                | 83.7 ms: 1.10x slower                                                 |
| regex_v8       | 15.1 ms                                                | 17.1 ms: 1.13x slower                                                 |
| Geometric mean | (ref)                                                  | 1.04x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_iterparse  | 75.5 ms                                                | 69.2 ms: 1.09x faster                                                 |
| xml_etree_parse      | 108 ms                                                 | 111 ms: 1.03x slower                                                  |
| tomli_loads          | 1.36 sec                                               | 1.55 sec: 1.15x slower                                                |
| unpickle_pure_python | 145 us                                                 | 169 us: 1.16x slower                                                  |
| pickle_pure_python   | 197 us                                                 | 237 us: 1.20x slower                                                  |
| xml_etree_process    | 38.9 ms                                                | 50.0 ms: 1.29x slower                                                 |
| xml_etree_generate   | 55.4 ms                                                | 72.5 ms: 1.31x slower                                                 |
| json_dumps           | 6.19 ms                                                | 8.33 ms: 1.35x slower                                                 |
| json_loads           | 17.0 us                                                | 24.5 us: 1.44x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.19x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 17.8 ms                                                | 20.5 ms: 1.15x slower                                                 |
| python_startup_no_site | 13.2 ms                                                | 15.5 ms: 1.18x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.17x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 14.7 ms                                                | 18.4 ms: 1.25x slower                                                 |
| genshi_xml      | 30.5 ms                                                | 39.3 ms: 1.29x slower                                                 |
| django_template | 19.7 ms                                                | 28.4 ms: 1.44x slower                                                 |
| mako            | 7.44 ms                                                | 10.8 ms: 1.45x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.36x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| gc_traversal                     | 2.95 ms                                                | 1.41 ms: 2.09x faster                                                 |
| async_tree_io_tg                 | 673 ms                                                 | 327 ms: 2.06x faster                                                  |
| async_tree_eager_io              | 666 ms                                                 | 332 ms: 2.01x faster                                                  |
| async_tree_io                    | 672 ms                                                 | 343 ms: 1.96x faster                                                  |
| async_tree_eager_io_tg           | 617 ms                                                 | 317 ms: 1.94x faster                                                  |
| subparsers                       | 32.1 ms                                                | 17.0 ms: 1.89x faster                                                 |
| async_tree_memoization_tg        | 318 ms                                                 | 180 ms: 1.77x faster                                                  |
| async_tree_none_tg               | 255 ms                                                 | 146 ms: 1.75x faster                                                  |
| async_tree_none                  | 263 ms                                                 | 164 ms: 1.61x faster                                                  |
| async_tree_memoization           | 310 ms                                                 | 198 ms: 1.56x faster                                                  |
| mdp                              | 1.49 sec                                               | 993 ms: 1.50x faster                                                  |
| create_gc_cycles                 | 1.15 ms                                                | 859 us: 1.34x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 413 ms: 1.28x faster                                                  |
| generators                       | 29.4 ms                                                | 24.0 ms: 1.22x faster                                                 |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 432 ms: 1.22x faster                                                  |
| deepcopy_memo                    | 26.0 us                                                | 22.1 us: 1.17x faster                                                 |
| go                               | 98.5 ms                                                | 84.2 ms: 1.17x faster                                                 |
| async_tree_eager_memoization     | 168 ms                                                 | 148 ms: 1.13x faster                                                  |
| float                            | 54.1 ms                                                | 48.6 ms: 1.11x faster                                                 |
| regex_effbot                     | 2.44 ms                                                | 2.22 ms: 1.10x faster                                                 |
| coroutines                       | 19.7 ms                                                | 18.0 ms: 1.09x faster                                                 |
| xml_etree_iterparse              | 75.5 ms                                                | 69.2 ms: 1.09x faster                                                 |
| deepcopy                         | 226 us                                                 | 213 us: 1.06x faster                                                  |
| k_core                           | 1.72 sec                                               | 1.65 sec: 1.04x faster                                                |
| dulwich_log                      | 29.2 ms                                                | 28.6 ms: 1.02x faster                                                 |
| asyncio_websockets               | 243 ms                                                 | 238 ms: 1.02x faster                                                  |
| pathlib                          | 24.7 ms                                                | 24.5 ms: 1.01x faster                                                 |
| pidigits                         | 283 ms                                                 | 281 ms: 1.00x faster                                                  |
| dask                             | 779 ms                                                 | 787 ms: 1.01x slower                                                  |
| regex_dna                        | 143 ms                                                 | 145 ms: 1.01x slower                                                  |
| pyflate                          | 311 ms                                                 | 316 ms: 1.02x slower                                                  |
| html5lib                         | 33.4 ms                                                | 34.3 ms: 1.03x slower                                                 |
| xml_etree_parse                  | 108 ms                                                 | 111 ms: 1.03x slower                                                  |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 391 ms: 1.04x slower                                                  |
| shortest_path                    | 331 ms                                                 | 346 ms: 1.05x slower                                                  |
| sqlite_synth                     | 1.55 us                                                | 1.62 us: 1.05x slower                                                 |
| deltablue                        | 2.57 ms                                                | 2.70 ms: 1.05x slower                                                 |
| connected_components             | 300 ms                                                 | 320 ms: 1.07x slower                                                  |
| async_generators                 | 299 ms                                                 | 324 ms: 1.08x slower                                                  |
| docutils                         | 1.45 sec                                               | 1.59 sec: 1.09x slower                                                |
| comprehensions                   | 14.0 us                                                | 15.3 us: 1.10x slower                                                 |
| pycparser                        | 673 ms                                                 | 739 ms: 1.10x slower                                                  |
| bpe_tokeniser                    | 3.28 sec                                               | 3.61 sec: 1.10x slower                                                |
| regex_compile                    | 75.9 ms                                                | 83.7 ms: 1.10x slower                                                 |
| sphinx                           | 613 ms                                                 | 678 ms: 1.11x slower                                                  |
| deepcopy_reduce                  | 2.01 us                                                | 2.27 us: 1.13x slower                                                 |
| regex_v8                         | 15.1 ms                                                | 17.1 ms: 1.13x slower                                                 |
| hexiom                           | 4.38 ms                                                | 4.99 ms: 1.14x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 397 ms: 1.14x slower                                                  |
| tomli_loads                      | 1.36 sec                                               | 1.55 sec: 1.15x slower                                                |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 163 ms: 1.15x slower                                                  |
| raytrace                         | 204 ms                                                 | 235 ms: 1.15x slower                                                  |
| python_startup                   | 17.8 ms                                                | 20.5 ms: 1.15x slower                                                 |
| scimark_sor                      | 85.8 ms                                                | 99.3 ms: 1.16x slower                                                 |
| chaos                            | 41.6 ms                                                | 48.2 ms: 1.16x slower                                                 |
| unpickle_pure_python             | 145 us                                                 | 169 us: 1.16x slower                                                  |
| spectral_norm                    | 76.5 ms                                                | 89.6 ms: 1.17x slower                                                 |
| sympy_integrate                  | 11.1 ms                                                | 13.0 ms: 1.17x slower                                                 |
| python_startup_no_site           | 13.2 ms                                                | 15.5 ms: 1.18x slower                                                 |
| bench_mp_pool                    | 65.5 ms                                                | 77.6 ms: 1.18x slower                                                 |
| 2to3                             | 168 ms                                                 | 202 ms: 1.20x slower                                                  |
| meteor_contest                   | 69.1 ms                                                | 82.8 ms: 1.20x slower                                                 |
| pickle_pure_python               | 197 us                                                 | 237 us: 1.20x slower                                                  |
| nqueens                          | 59.5 ms                                                | 71.7 ms: 1.20x slower                                                 |
| logging_simple                   | 3.60 us                                                | 4.40 us: 1.22x slower                                                 |
| sympy_sum                        | 76.2 ms                                                | 93.1 ms: 1.22x slower                                                 |
| scimark_monte_carlo              | 44.5 ms                                                | 54.9 ms: 1.23x slower                                                 |
| logging_format                   | 3.90 us                                                | 4.84 us: 1.24x slower                                                 |
| async_tree_eager                 | 65.8 ms                                                | 81.9 ms: 1.24x slower                                                 |
| genshi_text                      | 14.7 ms                                                | 18.4 ms: 1.25x slower                                                 |
| sympy_str                        | 144 ms                                                 | 184 ms: 1.28x slower                                                  |
| xml_etree_process                | 38.9 ms                                                | 50.0 ms: 1.29x slower                                                 |
| genshi_xml                       | 30.5 ms                                                | 39.3 ms: 1.29x slower                                                 |
| xml_etree_generate               | 55.4 ms                                                | 72.5 ms: 1.31x slower                                                 |
| richards                         | 30.6 ms                                                | 40.4 ms: 1.32x slower                                                 |
| richards_super                   | 34.6 ms                                                | 46.4 ms: 1.34x slower                                                 |
| json                             | 3.00 ms                                                | 4.04 ms: 1.35x slower                                                 |
| json_dumps                       | 6.19 ms                                                | 8.33 ms: 1.35x slower                                                 |
| many_optionals                   | 403 us                                                 | 546 us: 1.36x slower                                                  |
| thrift                           | 468 us                                                 | 635 us: 1.36x slower                                                  |
| scimark_lu                       | 73.5 ms                                                | 99.9 ms: 1.36x slower                                                 |
| crypto_pyaes                     | 51.4 ms                                                | 70.3 ms: 1.37x slower                                                 |
| nbody                            | 67.6 ms                                                | 93.1 ms: 1.38x slower                                                 |
| sympy_expand                     | 233 ms                                                 | 325 ms: 1.39x slower                                                  |
| fannkuch                         | 250 ms                                                 | 348 ms: 1.39x slower                                                  |
| pprint_pformat                   | 986 ms                                                 | 1.39 sec: 1.41x slower                                                |
| pprint_safe_repr                 | 483 ms                                                 | 684 ms: 1.42x slower                                                  |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 4.50 ms: 1.43x slower                                                 |
| scimark_fft                      | 194 ms                                                 | 280 ms: 1.44x slower                                                  |
| json_loads                       | 17.0 us                                                | 24.5 us: 1.44x slower                                                 |
| django_template                  | 19.7 ms                                                | 28.4 ms: 1.44x slower                                                 |
| mako                             | 7.44 ms                                                | 10.8 ms: 1.45x slower                                                 |
| typing_runtime_protocols         | 91.5 us                                                | 140 us: 1.53x slower                                                  |
| telco                            | 3.92 ms                                                | 6.14 ms: 1.57x slower                                                 |
| bench_thread_pool                | 483 us                                                 | 780 us: 1.62x slower                                                  |
| coverage                         | 38.5 ms                                                | 75.3 ms: 1.96x slower                                                 |
| async_tree_eager_tg              | 46.9 ms                                                | 127 ms: 2.71x slower                                                  |
| logging_silent                   | 72.5 ns                                                | 442 ns: 6.09x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.09x slower                                                          |

Benchmark hidden because not significant (1): pylint
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250617-3.15.0a0-fba5dde-NOGIL/bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.065x slower

# HPT report

- Reliability score: 99.89% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.27x