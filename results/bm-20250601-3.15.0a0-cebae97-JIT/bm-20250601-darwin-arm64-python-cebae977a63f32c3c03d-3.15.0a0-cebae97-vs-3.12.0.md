# Results vs. 3.12.0

- fork: python
- ref: cebae977a63f32c3c03d
- machine: darwin-arm64
- commit hash: cebae97
- commit date: 2025-06-01
- overall geometric mean: 1.199x faster
- HPT reliability: 99.58%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 226 ms: 1.34x slower                                                  |
| docutils       | 1.45 sec                                               | 1.67 sec: 1.15x slower                                                |
| sphinx         | 613 ms                                                 | 659 ms: 1.08x slower                                                  |
| Geometric mean | (ref)                                                  | 1.14x slower                                                          |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io_tg                 | 673 ms                                                 | 395 ms: 1.70x faster                                                  |
| async_tree_eager_io              | 666 ms                                                 | 394 ms: 1.69x faster                                                  |
| async_tree_io                    | 672 ms                                                 | 406 ms: 1.65x faster                                                  |
| async_tree_memoization_tg        | 318 ms                                                 | 205 ms: 1.55x faster                                                  |
| async_tree_eager_io_tg           | 617 ms                                                 | 405 ms: 1.53x faster                                                  |
| async_tree_none_tg               | 255 ms                                                 | 169 ms: 1.51x faster                                                  |
| async_tree_none                  | 263 ms                                                 | 175 ms: 1.51x faster                                                  |
| async_tree_memoization           | 310 ms                                                 | 208 ms: 1.49x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 450 ms: 1.17x faster                                                  |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 454 ms: 1.16x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 151 ms: 1.11x faster                                                  |
| coroutines                       | 19.7 ms                                                | 18.4 ms: 1.07x faster                                                 |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 395 ms: 1.06x slower                                                  |
| async_generators                 | 299 ms                                                 | 331 ms: 1.11x slower                                                  |
| async_tree_eager                 | 65.8 ms                                                | 73.6 ms: 1.12x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 430 ms: 1.24x slower                                                  |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 184 ms: 1.30x slower                                                  |
| async_tree_eager_tg              | 46.9 ms                                                | 142 ms: 3.03x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.13x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 54.1 ms                                                | 49.2 ms: 1.10x faster                                                 |
| pidigits       | 283 ms                                                 | 284 ms: 1.01x slower                                                  |
| nbody          | 67.6 ms                                                | 77.9 ms: 1.15x slower                                                 |
| Geometric mean | (ref)                                                  | 1.02x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 75.9 ms                                                | 68.1 ms: 1.11x faster                                                 |
| regex_effbot   | 2.44 ms                                                | 2.21 ms: 1.10x faster                                                 |
| regex_dna      | 143 ms                                                 | 145 ms: 1.02x slower                                                  |
| regex_v8       | 15.1 ms                                                | 17.4 ms: 1.16x slower                                                 |
| Geometric mean | (ref)                                                  | 1.01x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_iterparse  | 75.5 ms                                                | 77.5 ms: 1.03x slower                                                 |
| xml_etree_parse      | 108 ms                                                 | 112 ms: 1.04x slower                                                  |
| unpickle_pure_python | 145 us                                                 | 151 us: 1.04x slower                                                  |
| tomli_loads          | 1.36 sec                                               | 1.44 sec: 1.06x slower                                                |
| xml_etree_process    | 38.9 ms                                                | 43.1 ms: 1.11x slower                                                 |
| pickle_pure_python   | 197 us                                                 | 221 us: 1.12x slower                                                  |
| xml_etree_generate   | 55.4 ms                                                | 63.9 ms: 1.15x slower                                                 |
| json_dumps           | 6.19 ms                                                | 8.02 ms: 1.30x slower                                                 |
| json_loads           | 17.0 us                                                | 22.6 us: 1.33x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.13x slower                                                          |

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 14.7 ms                                                | 15.9 ms: 1.08x slower                                                 |
| genshi_xml      | 30.5 ms                                                | 33.7 ms: 1.11x slower                                                 |
| mako            | 7.44 ms                                                | 8.24 ms: 1.11x slower                                                 |
| django_template | 19.7 ms                                                | 25.8 ms: 1.31x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.15x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pprint_pformat                   | 986 ms                                                 | 1.01 us: 973863.69x faster                                            |
| pprint_safe_repr                 | 483 ms                                                 | 590 ns: 818510.09x faster                                             |
| subparsers                       | 32.1 ms                                                | 16.0 ms: 2.01x faster                                                 |
| async_tree_io_tg                 | 673 ms                                                 | 395 ms: 1.70x faster                                                  |
| async_tree_eager_io              | 666 ms                                                 | 394 ms: 1.69x faster                                                  |
| mdp                              | 1.49 sec                                               | 891 ms: 1.68x faster                                                  |
| async_tree_io                    | 672 ms                                                 | 406 ms: 1.65x faster                                                  |
| async_tree_memoization_tg        | 318 ms                                                 | 205 ms: 1.55x faster                                                  |
| async_tree_eager_io_tg           | 617 ms                                                 | 405 ms: 1.53x faster                                                  |
| async_tree_none_tg               | 255 ms                                                 | 169 ms: 1.51x faster                                                  |
| async_tree_none                  | 263 ms                                                 | 175 ms: 1.51x faster                                                  |
| async_tree_memoization           | 310 ms                                                 | 208 ms: 1.49x faster                                                  |
| deepcopy_memo                    | 26.0 us                                                | 19.5 us: 1.33x faster                                                 |
| generators                       | 29.4 ms                                                | 23.4 ms: 1.26x faster                                                 |
| go                               | 98.5 ms                                                | 79.7 ms: 1.24x faster                                                 |
| deepcopy                         | 226 us                                                 | 187 us: 1.21x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 450 ms: 1.17x faster                                                  |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 454 ms: 1.16x faster                                                  |
| regex_compile                    | 75.9 ms                                                | 68.1 ms: 1.11x faster                                                 |
| async_tree_eager_memoization     | 168 ms                                                 | 151 ms: 1.11x faster                                                  |
| regex_effbot                     | 2.44 ms                                                | 2.21 ms: 1.10x faster                                                 |
| float                            | 54.1 ms                                                | 49.2 ms: 1.10x faster                                                 |
| coroutines                       | 19.7 ms                                                | 18.4 ms: 1.07x faster                                                 |
| dulwich_log                      | 29.2 ms                                                | 27.5 ms: 1.06x faster                                                 |
| comprehensions                   | 14.0 us                                                | 13.5 us: 1.04x faster                                                 |
| k_core                           | 1.72 sec                                               | 1.68 sec: 1.02x faster                                                |
| deepcopy_reduce                  | 2.01 us                                                | 1.99 us: 1.01x faster                                                 |
| pidigits                         | 283 ms                                                 | 284 ms: 1.01x slower                                                  |
| regex_dna                        | 143 ms                                                 | 145 ms: 1.02x slower                                                  |
| pathlib                          | 24.7 ms                                                | 25.2 ms: 1.02x slower                                                 |
| xml_etree_iterparse              | 75.5 ms                                                | 77.5 ms: 1.03x slower                                                 |
| scimark_monte_carlo              | 44.5 ms                                                | 45.8 ms: 1.03x slower                                                 |
| raytrace                         | 204 ms                                                 | 211 ms: 1.04x slower                                                  |
| xml_etree_parse                  | 108 ms                                                 | 112 ms: 1.04x slower                                                  |
| unpickle_pure_python             | 145 us                                                 | 151 us: 1.04x slower                                                  |
| scimark_sor                      | 85.8 ms                                                | 89.3 ms: 1.04x slower                                                 |
| deltablue                        | 2.57 ms                                                | 2.68 ms: 1.04x slower                                                 |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 395 ms: 1.06x slower                                                  |
| spectral_norm                    | 76.5 ms                                                | 81.0 ms: 1.06x slower                                                 |
| tomli_loads                      | 1.36 sec                                               | 1.44 sec: 1.06x slower                                                |
| hexiom                           | 4.38 ms                                                | 4.69 ms: 1.07x slower                                                 |
| shortest_path                    | 331 ms                                                 | 355 ms: 1.08x slower                                                  |
| sphinx                           | 613 ms                                                 | 659 ms: 1.08x slower                                                  |
| genshi_text                      | 14.7 ms                                                | 15.9 ms: 1.08x slower                                                 |
| chaos                            | 41.6 ms                                                | 45.1 ms: 1.08x slower                                                 |
| sympy_integrate                  | 11.1 ms                                                | 12.1 ms: 1.09x slower                                                 |
| connected_components             | 300 ms                                                 | 328 ms: 1.09x slower                                                  |
| dask                             | 779 ms                                                 | 853 ms: 1.10x slower                                                  |
| gc_traversal                     | 2.95 ms                                                | 3.23 ms: 1.10x slower                                                 |
| genshi_xml                       | 30.5 ms                                                | 33.7 ms: 1.11x slower                                                 |
| mako                             | 7.44 ms                                                | 8.24 ms: 1.11x slower                                                 |
| xml_etree_process                | 38.9 ms                                                | 43.1 ms: 1.11x slower                                                 |
| async_generators                 | 299 ms                                                 | 331 ms: 1.11x slower                                                  |
| async_tree_eager                 | 65.8 ms                                                | 73.6 ms: 1.12x slower                                                 |
| logging_simple                   | 3.60 us                                                | 4.04 us: 1.12x slower                                                 |
| logging_format                   | 3.90 us                                                | 4.38 us: 1.12x slower                                                 |
| pickle_pure_python               | 197 us                                                 | 221 us: 1.12x slower                                                  |
| sympy_sum                        | 76.2 ms                                                | 86.0 ms: 1.13x slower                                                 |
| bench_thread_pool                | 483 us                                                 | 545 us: 1.13x slower                                                  |
| bench_mp_pool                    | 65.5 ms                                                | 74.8 ms: 1.14x slower                                                 |
| bpe_tokeniser                    | 3.28 sec                                               | 3.76 sec: 1.15x slower                                                |
| docutils                         | 1.45 sec                                               | 1.67 sec: 1.15x slower                                                |
| xml_etree_generate               | 55.4 ms                                                | 63.9 ms: 1.15x slower                                                 |
| nbody                            | 67.6 ms                                                | 77.9 ms: 1.15x slower                                                 |
| nqueens                          | 59.5 ms                                                | 68.7 ms: 1.15x slower                                                 |
| regex_v8                         | 15.1 ms                                                | 17.4 ms: 1.16x slower                                                 |
| sympy_str                        | 144 ms                                                 | 167 ms: 1.16x slower                                                  |
| pycparser                        | 673 ms                                                 | 791 ms: 1.18x slower                                                  |
| meteor_contest                   | 69.1 ms                                                | 81.8 ms: 1.18x slower                                                 |
| richards_super                   | 34.6 ms                                                | 41.0 ms: 1.18x slower                                                 |
| scimark_lu                       | 73.5 ms                                                | 87.3 ms: 1.19x slower                                                 |
| crypto_pyaes                     | 51.4 ms                                                | 61.2 ms: 1.19x slower                                                 |
| richards                         | 30.6 ms                                                | 36.4 ms: 1.19x slower                                                 |
| create_gc_cycles                 | 1.15 ms                                                | 1.40 ms: 1.22x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 430 ms: 1.24x slower                                                  |
| sympy_expand                     | 233 ms                                                 | 292 ms: 1.25x slower                                                  |
| sqlite_synth                     | 1.55 us                                                | 1.94 us: 1.26x slower                                                 |
| scimark_fft                      | 194 ms                                                 | 248 ms: 1.27x slower                                                  |
| json                             | 3.00 ms                                                | 3.84 ms: 1.28x slower                                                 |
| json_dumps                       | 6.19 ms                                                | 8.02 ms: 1.30x slower                                                 |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 184 ms: 1.30x slower                                                  |
| django_template                  | 19.7 ms                                                | 25.8 ms: 1.31x slower                                                 |
| many_optionals                   | 403 us                                                 | 535 us: 1.33x slower                                                  |
| json_loads                       | 17.0 us                                                | 22.6 us: 1.33x slower                                                 |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 4.21 ms: 1.34x slower                                                 |
| 2to3                             | 168 ms                                                 | 226 ms: 1.34x slower                                                  |
| typing_runtime_protocols         | 91.5 us                                                | 123 us: 1.35x slower                                                  |
| telco                            | 3.92 ms                                                | 5.56 ms: 1.42x slower                                                 |
| fannkuch                         | 250 ms                                                 | 358 ms: 1.43x slower                                                  |
| async_tree_eager_tg              | 46.9 ms                                                | 142 ms: 3.03x slower                                                  |
| logging_silent                   | 72.5 ns                                                | 411 ns: 5.66x slower                                                  |
| coverage                         | 38.5 ms                                                | 308 ms: 8.00x slower                                                  |
| thrift                           | 468 us                                                 | 44.3 ms: 94.64x slower                                                |
| Geometric mean                   | (ref)                                                  | 1.17x faster                                                          |

Benchmark hidden because not significant (6): pylint, python_startup_no_site, python_startup, pyflate, html5lib, asyncio_websockets
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250601-3.15.0a0-cebae97-JIT/bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.199x faster

# HPT report

- Reliability score: 99.58% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.09x