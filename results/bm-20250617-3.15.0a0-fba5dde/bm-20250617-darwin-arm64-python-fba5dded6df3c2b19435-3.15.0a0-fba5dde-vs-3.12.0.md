# Results vs. 3.12.0

- fork: python
- ref: fba5dded6df3c2b19435
- machine: darwin-arm64
- commit hash: fba5dde
- commit date: 2025-06-17
- overall geometric mean: 1.029x slower
- HPT reliability: 99.60%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 187 ms: 1.11x slower                                                  |
| docutils       | 1.45 sec                                               | 1.64 sec: 1.13x slower                                                |
| sphinx         | 613 ms                                                 | 647 ms: 1.06x slower                                                  |
| Geometric mean | (ref)                                                  | 1.07x slower                                                          |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io_tg                 | 673 ms                                                 | 387 ms: 1.74x faster                                                  |
| async_tree_eager_io              | 666 ms                                                 | 386 ms: 1.73x faster                                                  |
| async_tree_io                    | 672 ms                                                 | 400 ms: 1.68x faster                                                  |
| async_tree_memoization_tg        | 318 ms                                                 | 202 ms: 1.57x faster                                                  |
| async_tree_eager_io_tg           | 617 ms                                                 | 397 ms: 1.56x faster                                                  |
| async_tree_none_tg               | 255 ms                                                 | 167 ms: 1.53x faster                                                  |
| async_tree_none                  | 263 ms                                                 | 173 ms: 1.53x faster                                                  |
| async_tree_memoization           | 310 ms                                                 | 204 ms: 1.52x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 446 ms: 1.18x faster                                                  |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 450 ms: 1.17x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 148 ms: 1.14x faster                                                  |
| coroutines                       | 19.7 ms                                                | 18.1 ms: 1.09x faster                                                 |
| async_generators                 | 299 ms                                                 | 310 ms: 1.04x slower                                                  |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 389 ms: 1.04x slower                                                  |
| async_tree_eager                 | 65.8 ms                                                | 70.5 ms: 1.07x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 425 ms: 1.22x slower                                                  |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 180 ms: 1.27x slower                                                  |
| async_tree_eager_tg              | 46.9 ms                                                | 141 ms: 3.00x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.15x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 54.1 ms                                                | 51.4 ms: 1.05x faster                                                 |
| pidigits       | 283 ms                                                 | 285 ms: 1.01x slower                                                  |
| nbody          | 67.6 ms                                                | 83.1 ms: 1.23x slower                                                 |
| Geometric mean | (ref)                                                  | 1.06x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.44 ms                                                | 2.19 ms: 1.11x faster                                                 |
| regex_compile  | 75.9 ms                                                | 74.2 ms: 1.02x faster                                                 |
| regex_dna      | 143 ms                                                 | 145 ms: 1.02x slower                                                  |
| regex_v8       | 15.1 ms                                                | 17.4 ms: 1.15x slower                                                 |
| Geometric mean | (ref)                                                  | 1.01x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_iterparse  | 75.5 ms                                                | 76.0 ms: 1.01x slower                                                 |
| tomli_loads          | 1.36 sec                                               | 1.39 sec: 1.02x slower                                                |
| xml_etree_parse      | 108 ms                                                 | 112 ms: 1.04x slower                                                  |
| unpickle_pure_python | 145 us                                                 | 155 us: 1.06x slower                                                  |
| pickle_pure_python   | 197 us                                                 | 221 us: 1.12x slower                                                  |
| xml_etree_process    | 38.9 ms                                                | 43.9 ms: 1.13x slower                                                 |
| xml_etree_generate   | 55.4 ms                                                | 65.2 ms: 1.18x slower                                                 |
| json_dumps           | 6.19 ms                                                | 8.09 ms: 1.31x slower                                                 |
| json_loads           | 17.0 us                                                | 22.7 us: 1.33x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.13x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 17.8 ms                                                | 20.2 ms: 1.14x slower                                                 |
| python_startup_no_site | 13.2 ms                                                | 15.3 ms: 1.16x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.15x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 14.7 ms                                                | 15.7 ms: 1.07x slower                                                 |
| genshi_xml      | 30.5 ms                                                | 33.1 ms: 1.08x slower                                                 |
| mako            | 7.44 ms                                                | 8.21 ms: 1.10x slower                                                 |
| django_template | 19.7 ms                                                | 25.5 ms: 1.30x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.13x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 15.9 ms: 2.02x faster                                                 |
| async_tree_io_tg                 | 673 ms                                                 | 387 ms: 1.74x faster                                                  |
| async_tree_eager_io              | 666 ms                                                 | 386 ms: 1.73x faster                                                  |
| mdp                              | 1.49 sec                                               | 883 ms: 1.69x faster                                                  |
| async_tree_io                    | 672 ms                                                 | 400 ms: 1.68x faster                                                  |
| async_tree_memoization_tg        | 318 ms                                                 | 202 ms: 1.57x faster                                                  |
| async_tree_eager_io_tg           | 617 ms                                                 | 397 ms: 1.56x faster                                                  |
| async_tree_none_tg               | 255 ms                                                 | 167 ms: 1.53x faster                                                  |
| async_tree_none                  | 263 ms                                                 | 173 ms: 1.53x faster                                                  |
| async_tree_memoization           | 310 ms                                                 | 204 ms: 1.52x faster                                                  |
| deepcopy_memo                    | 26.0 us                                                | 19.3 us: 1.35x faster                                                 |
| generators                       | 29.4 ms                                                | 22.8 ms: 1.29x faster                                                 |
| go                               | 98.5 ms                                                | 77.2 ms: 1.28x faster                                                 |
| deepcopy                         | 226 us                                                 | 186 us: 1.21x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 446 ms: 1.18x faster                                                  |
| comprehensions                   | 14.0 us                                                | 12.0 us: 1.17x faster                                                 |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 450 ms: 1.17x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 148 ms: 1.14x faster                                                  |
| k_core                           | 1.72 sec                                               | 1.54 sec: 1.12x faster                                                |
| regex_effbot                     | 2.44 ms                                                | 2.19 ms: 1.11x faster                                                 |
| coroutines                       | 19.7 ms                                                | 18.1 ms: 1.09x faster                                                 |
| dulwich_log                      | 29.2 ms                                                | 27.0 ms: 1.08x faster                                                 |
| float                            | 54.1 ms                                                | 51.4 ms: 1.05x faster                                                 |
| pyflate                          | 311 ms                                                 | 303 ms: 1.02x faster                                                  |
| regex_compile                    | 75.9 ms                                                | 74.2 ms: 1.02x faster                                                 |
| deepcopy_reduce                  | 2.01 us                                                | 1.98 us: 1.02x faster                                                 |
| pathlib                          | 24.7 ms                                                | 24.3 ms: 1.01x faster                                                 |
| dask                             | 779 ms                                                 | 772 ms: 1.01x faster                                                  |
| xml_etree_iterparse              | 75.5 ms                                                | 76.0 ms: 1.01x slower                                                 |
| pidigits                         | 283 ms                                                 | 285 ms: 1.01x slower                                                  |
| regex_dna                        | 143 ms                                                 | 145 ms: 1.02x slower                                                  |
| deltablue                        | 2.57 ms                                                | 2.61 ms: 1.02x slower                                                 |
| tomli_loads                      | 1.36 sec                                               | 1.39 sec: 1.02x slower                                                |
| shortest_path                    | 331 ms                                                 | 340 ms: 1.03x slower                                                  |
| raytrace                         | 204 ms                                                 | 211 ms: 1.04x slower                                                  |
| async_generators                 | 299 ms                                                 | 310 ms: 1.04x slower                                                  |
| xml_etree_parse                  | 108 ms                                                 | 112 ms: 1.04x slower                                                  |
| connected_components             | 300 ms                                                 | 312 ms: 1.04x slower                                                  |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 389 ms: 1.04x slower                                                  |
| spectral_norm                    | 76.5 ms                                                | 79.9 ms: 1.05x slower                                                 |
| hexiom                           | 4.38 ms                                                | 4.58 ms: 1.05x slower                                                 |
| scimark_monte_carlo              | 44.5 ms                                                | 46.7 ms: 1.05x slower                                                 |
| sphinx                           | 613 ms                                                 | 647 ms: 1.06x slower                                                  |
| chaos                            | 41.6 ms                                                | 44.1 ms: 1.06x slower                                                 |
| sympy_integrate                  | 11.1 ms                                                | 11.8 ms: 1.06x slower                                                 |
| scimark_sor                      | 85.8 ms                                                | 91.2 ms: 1.06x slower                                                 |
| unpickle_pure_python             | 145 us                                                 | 155 us: 1.06x slower                                                  |
| genshi_text                      | 14.7 ms                                                | 15.7 ms: 1.07x slower                                                 |
| async_tree_eager                 | 65.8 ms                                                | 70.5 ms: 1.07x slower                                                 |
| gc_traversal                     | 2.95 ms                                                | 3.20 ms: 1.08x slower                                                 |
| genshi_xml                       | 30.5 ms                                                | 33.1 ms: 1.08x slower                                                 |
| meteor_contest                   | 69.1 ms                                                | 75.8 ms: 1.10x slower                                                 |
| logging_simple                   | 3.60 us                                                | 3.96 us: 1.10x slower                                                 |
| logging_format                   | 3.90 us                                                | 4.29 us: 1.10x slower                                                 |
| pycparser                        | 673 ms                                                 | 741 ms: 1.10x slower                                                  |
| mako                             | 7.44 ms                                                | 8.21 ms: 1.10x slower                                                 |
| 2to3                             | 168 ms                                                 | 187 ms: 1.11x slower                                                  |
| bpe_tokeniser                    | 3.28 sec                                               | 3.65 sec: 1.11x slower                                                |
| bench_thread_pool                | 483 us                                                 | 538 us: 1.11x slower                                                  |
| sympy_sum                        | 76.2 ms                                                | 85.1 ms: 1.12x slower                                                 |
| pickle_pure_python               | 197 us                                                 | 221 us: 1.12x slower                                                  |
| docutils                         | 1.45 sec                                               | 1.64 sec: 1.13x slower                                                |
| xml_etree_process                | 38.9 ms                                                | 43.9 ms: 1.13x slower                                                 |
| nqueens                          | 59.5 ms                                                | 67.5 ms: 1.13x slower                                                 |
| python_startup                   | 17.8 ms                                                | 20.2 ms: 1.14x slower                                                 |
| sympy_str                        | 144 ms                                                 | 164 ms: 1.14x slower                                                  |
| bench_mp_pool                    | 65.5 ms                                                | 75.5 ms: 1.15x slower                                                 |
| regex_v8                         | 15.1 ms                                                | 17.4 ms: 1.15x slower                                                 |
| python_startup_no_site           | 13.2 ms                                                | 15.3 ms: 1.16x slower                                                 |
| crypto_pyaes                     | 51.4 ms                                                | 60.1 ms: 1.17x slower                                                 |
| richards_super                   | 34.6 ms                                                | 40.4 ms: 1.17x slower                                                 |
| richards                         | 30.6 ms                                                | 35.9 ms: 1.17x slower                                                 |
| xml_etree_generate               | 55.4 ms                                                | 65.2 ms: 1.18x slower                                                 |
| scimark_lu                       | 73.5 ms                                                | 86.6 ms: 1.18x slower                                                 |
| pprint_pformat                   | 986 ms                                                 | 1.19 sec: 1.21x slower                                                |
| create_gc_cycles                 | 1.15 ms                                                | 1.39 ms: 1.21x slower                                                 |
| pprint_safe_repr                 | 483 ms                                                 | 586 ms: 1.21x slower                                                  |
| sqlite_synth                     | 1.55 us                                                | 1.89 us: 1.22x slower                                                 |
| thrift                           | 468 us                                                 | 571 us: 1.22x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 425 ms: 1.22x slower                                                  |
| sympy_expand                     | 233 ms                                                 | 286 ms: 1.22x slower                                                  |
| nbody                            | 67.6 ms                                                | 83.1 ms: 1.23x slower                                                 |
| fannkuch                         | 250 ms                                                 | 311 ms: 1.24x slower                                                  |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 180 ms: 1.27x slower                                                  |
| json                             | 3.00 ms                                                | 3.83 ms: 1.27x slower                                                 |
| many_optionals                   | 403 us                                                 | 520 us: 1.29x slower                                                  |
| django_template                  | 19.7 ms                                                | 25.5 ms: 1.30x slower                                                 |
| json_dumps                       | 6.19 ms                                                | 8.09 ms: 1.31x slower                                                 |
| typing_runtime_protocols         | 91.5 us                                                | 120 us: 1.31x slower                                                  |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 4.19 ms: 1.33x slower                                                 |
| json_loads                       | 17.0 us                                                | 22.7 us: 1.33x slower                                                 |
| scimark_fft                      | 194 ms                                                 | 267 ms: 1.37x slower                                                  |
| telco                            | 3.92 ms                                                | 5.50 ms: 1.40x slower                                                 |
| coverage                         | 38.5 ms                                                | 59.8 ms: 1.55x slower                                                 |
| async_tree_eager_tg              | 46.9 ms                                                | 141 ms: 3.00x slower                                                  |
| logging_silent                   | 72.5 ns                                                | 413 ns: 5.69x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.05x slower                                                          |

Benchmark hidden because not significant (3): pylint, html5lib, asyncio_websockets
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250617-3.15.0a0-fba5dde/bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.029x slower

# HPT report

- Reliability score: 99.60% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.10x