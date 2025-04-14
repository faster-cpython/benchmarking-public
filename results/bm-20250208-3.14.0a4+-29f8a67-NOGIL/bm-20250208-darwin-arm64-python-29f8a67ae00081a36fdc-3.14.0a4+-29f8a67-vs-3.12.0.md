# Results vs. 3.12.0

- fork: python
- ref: 29f8a67ae00081a36fdc
- machine: darwin-arm64
- commit hash: 29f8a67
- commit date: 2025-02-08
- overall geometric mean: 1.073x slower
- HPT reliability: 99.99%
- HPT 99th percentile: 1.03x slower
- Memory change: 1.22x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 202 ms: 1.20x slower                                                   |
| docutils       | 1.45 sec                                               | 1.50 sec: 1.03x slower                                                 |
| html5lib       | 33.4 ms                                                | 36.2 ms: 1.09x slower                                                  |
| sphinx         | 613 ms                                                 | 636 ms: 1.04x slower                                                   |
| Geometric mean | (ref)                                                  | 1.09x slower                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg                 | 673 ms                                                 | 351 ms: 1.91x faster                                                   |
| async_tree_eager_io              | 666 ms                                                 | 361 ms: 1.85x faster                                                   |
| async_tree_eager_io_tg           | 617 ms                                                 | 336 ms: 1.83x faster                                                   |
| async_tree_io                    | 672 ms                                                 | 374 ms: 1.80x faster                                                   |
| async_tree_memoization_tg        | 318 ms                                                 | 200 ms: 1.59x faster                                                   |
| async_tree_none_tg               | 255 ms                                                 | 164 ms: 1.55x faster                                                   |
| async_tree_none                  | 263 ms                                                 | 182 ms: 1.45x faster                                                   |
| async_tree_memoization           | 310 ms                                                 | 228 ms: 1.36x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 406 ms: 1.30x faster                                                   |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 435 ms: 1.21x faster                                                   |
| async_generators                 | 299 ms                                                 | 282 ms: 1.06x faster                                                   |
| coroutines                       | 19.7 ms                                                | 18.9 ms: 1.04x faster                                                  |
| asyncio_websockets               | 243 ms                                                 | 238 ms: 1.02x faster                                                   |
| async_tree_eager_memoization     | 168 ms                                                 | 167 ms: 1.01x faster                                                   |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 383 ms: 1.02x slower                                                   |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 385 ms: 1.11x slower                                                   |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 181 ms: 1.28x slower                                                   |
| async_tree_eager                 | 65.8 ms                                                | 93.3 ms: 1.42x slower                                                  |
| async_tree_eager_tg              | 46.9 ms                                                | 135 ms: 2.88x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.16x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pidigits       | 283 ms                                                 | 281 ms: 1.01x faster                                                   |
| float          | 54.1 ms                                                | 56.2 ms: 1.04x slower                                                  |
| nbody          | 67.6 ms                                                | 106 ms: 1.56x slower                                                   |
| Geometric mean | (ref)                                                  | 1.17x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 2.44 ms                                                | 2.16 ms: 1.13x faster                                                  |
| regex_dna      | 143 ms                                                 | 138 ms: 1.04x faster                                                   |
| regex_v8       | 15.1 ms                                                | 16.1 ms: 1.07x slower                                                  |
| regex_compile  | 75.9 ms                                                | 92.9 ms: 1.22x slower                                                  |
| Geometric mean | (ref)                                                  | 1.03x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_iterparse  | 75.5 ms                                                | 67.4 ms: 1.12x faster                                                  |
| xml_etree_parse      | 108 ms                                                 | 96.7 ms: 1.12x faster                                                  |
| xml_etree_generate   | 55.4 ms                                                | 60.9 ms: 1.10x slower                                                  |
| json_loads           | 17.0 us                                                | 19.1 us: 1.12x slower                                                  |
| xml_etree_process    | 38.9 ms                                                | 45.9 ms: 1.18x slower                                                  |
| tomli_loads          | 1.36 sec                                               | 1.66 sec: 1.23x slower                                                 |
| json_dumps           | 6.19 ms                                                | 7.98 ms: 1.29x slower                                                  |
| unpickle_pure_python | 145 us                                                 | 189 us: 1.30x slower                                                   |
| pickle_pure_python   | 197 us                                                 | 270 us: 1.37x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.14x slower                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 17.8 ms                                                | 20.5 ms: 1.15x slower                                                  |
| python_startup_no_site | 13.2 ms                                                | 15.8 ms: 1.20x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.17x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_xml      | 30.5 ms                                                | 39.2 ms: 1.29x slower                                                  |
| genshi_text     | 14.7 ms                                                | 20.1 ms: 1.37x slower                                                  |
| django_template | 19.7 ms                                                | 27.1 ms: 1.38x slower                                                  |
| mako            | 7.44 ms                                                | 11.0 ms: 1.47x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.37x slower                                                           |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 14.1 ms: 2.28x faster                                                  |
| gc_traversal                     | 2.95 ms                                                | 1.40 ms: 2.11x faster                                                  |
| async_tree_io_tg                 | 673 ms                                                 | 351 ms: 1.91x faster                                                   |
| async_tree_eager_io              | 666 ms                                                 | 361 ms: 1.85x faster                                                   |
| async_tree_eager_io_tg           | 617 ms                                                 | 336 ms: 1.83x faster                                                   |
| async_tree_io                    | 672 ms                                                 | 374 ms: 1.80x faster                                                   |
| async_tree_memoization_tg        | 318 ms                                                 | 200 ms: 1.59x faster                                                   |
| async_tree_none_tg               | 255 ms                                                 | 164 ms: 1.55x faster                                                   |
| create_gc_cycles                 | 1.15 ms                                                | 764 us: 1.51x faster                                                   |
| async_tree_none                  | 263 ms                                                 | 182 ms: 1.45x faster                                                   |
| async_tree_memoization           | 310 ms                                                 | 228 ms: 1.36x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 406 ms: 1.30x faster                                                   |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 435 ms: 1.21x faster                                                   |
| sqlite_synth                     | 1.55 us                                                | 1.32 us: 1.18x faster                                                  |
| regex_effbot                     | 2.44 ms                                                | 2.16 ms: 1.13x faster                                                  |
| xml_etree_iterparse              | 75.5 ms                                                | 67.4 ms: 1.12x faster                                                  |
| xml_etree_parse                  | 108 ms                                                 | 96.7 ms: 1.12x faster                                                  |
| deepcopy                         | 226 us                                                 | 204 us: 1.11x faster                                                   |
| async_generators                 | 299 ms                                                 | 282 ms: 1.06x faster                                                   |
| pathlib                          | 24.7 ms                                                | 23.5 ms: 1.05x faster                                                  |
| coroutines                       | 19.7 ms                                                | 18.9 ms: 1.04x faster                                                  |
| regex_dna                        | 143 ms                                                 | 138 ms: 1.04x faster                                                   |
| asyncio_websockets               | 243 ms                                                 | 238 ms: 1.02x faster                                                   |
| k_core                           | 1.72 sec                                               | 1.69 sec: 1.02x faster                                                 |
| bench_mp_pool                    | 65.5 ms                                                | 64.5 ms: 1.02x faster                                                  |
| pidigits                         | 283 ms                                                 | 281 ms: 1.01x faster                                                   |
| async_tree_eager_memoization     | 168 ms                                                 | 167 ms: 1.01x faster                                                   |
| bpe_tokeniser                    | 3.28 sec                                               | 3.33 sec: 1.01x slower                                                 |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 383 ms: 1.02x slower                                                   |
| docutils                         | 1.45 sec                                               | 1.50 sec: 1.03x slower                                                 |
| sphinx                           | 613 ms                                                 | 636 ms: 1.04x slower                                                   |
| float                            | 54.1 ms                                                | 56.2 ms: 1.04x slower                                                  |
| comprehensions                   | 14.0 us                                                | 14.7 us: 1.05x slower                                                  |
| deepcopy_reduce                  | 2.01 us                                                | 2.12 us: 1.05x slower                                                  |
| json                             | 3.00 ms                                                | 3.16 ms: 1.05x slower                                                  |
| pycparser                        | 673 ms                                                 | 716 ms: 1.06x slower                                                   |
| regex_v8                         | 15.1 ms                                                | 16.1 ms: 1.07x slower                                                  |
| spectral_norm                    | 76.5 ms                                                | 82.1 ms: 1.07x slower                                                  |
| html5lib                         | 33.4 ms                                                | 36.2 ms: 1.09x slower                                                  |
| dulwich_log                      | 29.2 ms                                                | 31.7 ms: 1.09x slower                                                  |
| xml_etree_generate               | 55.4 ms                                                | 60.9 ms: 1.10x slower                                                  |
| deepcopy_memo                    | 26.0 us                                                | 28.8 us: 1.11x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 385 ms: 1.11x slower                                                   |
| mdp                              | 1.49 sec                                               | 1.66 sec: 1.11x slower                                                 |
| thrift                           | 468 us                                                 | 522 us: 1.12x slower                                                   |
| generators                       | 29.4 ms                                                | 32.8 ms: 1.12x slower                                                  |
| json_loads                       | 17.0 us                                                | 19.1 us: 1.12x slower                                                  |
| shortest_path                    | 331 ms                                                 | 371 ms: 1.12x slower                                                   |
| connected_components             | 300 ms                                                 | 340 ms: 1.13x slower                                                   |
| sqlalchemy_declarative           | 61.9 ms                                                | 70.6 ms: 1.14x slower                                                  |
| sympy_sum                        | 76.2 ms                                                | 87.0 ms: 1.14x slower                                                  |
| python_startup                   | 17.8 ms                                                | 20.5 ms: 1.15x slower                                                  |
| sqlglot_optimize                 | 33.2 ms                                                | 38.5 ms: 1.16x slower                                                  |
| go                               | 98.5 ms                                                | 115 ms: 1.16x slower                                                   |
| sqlglot_normalize                | 180 ms                                                 | 210 ms: 1.17x slower                                                   |
| logging_simple                   | 3.60 us                                                | 4.25 us: 1.18x slower                                                  |
| xml_etree_process                | 38.9 ms                                                | 45.9 ms: 1.18x slower                                                  |
| pyflate                          | 311 ms                                                 | 369 ms: 1.19x slower                                                   |
| sympy_str                        | 144 ms                                                 | 171 ms: 1.19x slower                                                   |
| raytrace                         | 204 ms                                                 | 243 ms: 1.19x slower                                                   |
| scimark_fft                      | 194 ms                                                 | 232 ms: 1.19x slower                                                   |
| nqueens                          | 59.5 ms                                                | 71.0 ms: 1.19x slower                                                  |
| python_startup_no_site           | 13.2 ms                                                | 15.8 ms: 1.20x slower                                                  |
| 2to3                             | 168 ms                                                 | 202 ms: 1.20x slower                                                   |
| sqlalchemy_imperative            | 6.60 ms                                                | 7.93 ms: 1.20x slower                                                  |
| logging_silent                   | 72.5 ns                                                | 87.3 ns: 1.20x slower                                                  |
| meteor_contest                   | 69.1 ms                                                | 83.5 ms: 1.21x slower                                                  |
| logging_format                   | 3.90 us                                                | 4.72 us: 1.21x slower                                                  |
| sympy_expand                     | 233 ms                                                 | 285 ms: 1.22x slower                                                   |
| regex_compile                    | 75.9 ms                                                | 92.9 ms: 1.22x slower                                                  |
| tomli_loads                      | 1.36 sec                                               | 1.66 sec: 1.23x slower                                                 |
| many_optionals                   | 403 us                                                 | 499 us: 1.24x slower                                                   |
| scimark_sor                      | 85.8 ms                                                | 107 ms: 1.24x slower                                                   |
| sqlglot_transpile                | 973 us                                                 | 1.21 ms: 1.24x slower                                                  |
| sympy_integrate                  | 11.1 ms                                                | 13.8 ms: 1.25x slower                                                  |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 3.92 ms: 1.25x slower                                                  |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 181 ms: 1.28x slower                                                   |
| chaos                            | 41.6 ms                                                | 53.4 ms: 1.28x slower                                                  |
| genshi_xml                       | 30.5 ms                                                | 39.2 ms: 1.29x slower                                                  |
| crypto_pyaes                     | 51.4 ms                                                | 66.3 ms: 1.29x slower                                                  |
| json_dumps                       | 6.19 ms                                                | 7.98 ms: 1.29x slower                                                  |
| unpickle_pure_python             | 145 us                                                 | 189 us: 1.30x slower                                                   |
| pprint_pformat                   | 986 ms                                                 | 1.29 sec: 1.30x slower                                                 |
| sqlglot_parse                    | 808 us                                                 | 1.06 ms: 1.31x slower                                                  |
| pprint_safe_repr                 | 483 ms                                                 | 632 ms: 1.31x slower                                                   |
| telco                            | 3.92 ms                                                | 5.15 ms: 1.31x slower                                                  |
| fannkuch                         | 250 ms                                                 | 329 ms: 1.32x slower                                                   |
| scimark_lu                       | 73.5 ms                                                | 98.8 ms: 1.34x slower                                                  |
| deltablue                        | 2.57 ms                                                | 3.46 ms: 1.35x slower                                                  |
| richards_super                   | 34.6 ms                                                | 47.3 ms: 1.37x slower                                                  |
| genshi_text                      | 14.7 ms                                                | 20.1 ms: 1.37x slower                                                  |
| pickle_pure_python               | 197 us                                                 | 270 us: 1.37x slower                                                   |
| richards                         | 30.6 ms                                                | 42.0 ms: 1.37x slower                                                  |
| django_template                  | 19.7 ms                                                | 27.1 ms: 1.38x slower                                                  |
| hexiom                           | 4.38 ms                                                | 6.02 ms: 1.38x slower                                                  |
| typing_runtime_protocols         | 91.5 us                                                | 126 us: 1.38x slower                                                   |
| scimark_monte_carlo              | 44.5 ms                                                | 62.5 ms: 1.41x slower                                                  |
| async_tree_eager                 | 65.8 ms                                                | 93.3 ms: 1.42x slower                                                  |
| coverage                         | 38.5 ms                                                | 54.7 ms: 1.42x slower                                                  |
| mako                             | 7.44 ms                                                | 11.0 ms: 1.47x slower                                                  |
| nbody                            | 67.6 ms                                                | 106 ms: 1.56x slower                                                   |
| bench_thread_pool                | 483 us                                                 | 802 us: 1.66x slower                                                   |
| async_tree_eager_tg              | 46.9 ms                                                | 135 ms: 2.88x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.08x slower                                                           |

Benchmark hidden because not significant (1): pylint
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (8) of results/bm-20250208-3.14.0a4+-29f8a67-NOGIL/bm-20250208-darwin-arm64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.073x slower

# HPT report

- Reliability score: 99.99% likely to be slow
- 90% likely to have a slowdown of 1.07x
- 95% likely to have a slowdown of 1.06x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: 1.22x