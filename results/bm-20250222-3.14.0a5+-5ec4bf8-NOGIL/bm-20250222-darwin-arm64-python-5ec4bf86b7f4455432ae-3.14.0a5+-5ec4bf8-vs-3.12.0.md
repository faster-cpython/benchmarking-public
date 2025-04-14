# Results vs. 3.12.0

- fork: python
- ref: 5ec4bf86b7f4455432ae
- machine: darwin-arm64
- commit hash: 5ec4bf8
- commit date: 2025-02-22
- overall geometric mean: 1.041x slower
- HPT reliability: 99.92%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.22x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 195 ms: 1.16x slower                                                   |
| html5lib       | 33.4 ms                                                | 34.6 ms: 1.04x slower                                                  |
| sphinx         | 613 ms                                                 | 622 ms: 1.02x slower                                                   |
| Geometric mean | (ref)                                                  | 1.05x slower                                                           |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg                 | 673 ms                                                 | 328 ms: 2.05x faster                                                   |
| async_tree_eager_io              | 666 ms                                                 | 338 ms: 1.97x faster                                                   |
| async_tree_eager_io_tg           | 617 ms                                                 | 319 ms: 1.94x faster                                                   |
| async_tree_io                    | 672 ms                                                 | 352 ms: 1.91x faster                                                   |
| async_tree_none_tg               | 255 ms                                                 | 146 ms: 1.75x faster                                                   |
| async_tree_memoization_tg        | 318 ms                                                 | 187 ms: 1.71x faster                                                   |
| async_tree_none                  | 263 ms                                                 | 170 ms: 1.55x faster                                                   |
| async_tree_memoization           | 310 ms                                                 | 210 ms: 1.47x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 394 ms: 1.34x faster                                                   |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 418 ms: 1.26x faster                                                   |
| async_generators                 | 299 ms                                                 | 274 ms: 1.09x faster                                                   |
| async_tree_eager_memoization     | 168 ms                                                 | 157 ms: 1.07x faster                                                   |
| coroutines                       | 19.7 ms                                                | 18.7 ms: 1.05x faster                                                  |
| asyncio_websockets               | 243 ms                                                 | 238 ms: 1.02x faster                                                   |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 377 ms: 1.08x slower                                                   |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 171 ms: 1.20x slower                                                   |
| async_tree_eager                 | 65.8 ms                                                | 85.3 ms: 1.30x slower                                                  |
| async_tree_eager_tg              | 46.9 ms                                                | 127 ms: 2.71x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.22x faster                                                           |

Benchmark hidden because not significant (1): async_tree_eager_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pidigits       | 283 ms                                                 | 281 ms: 1.01x faster                                                   |
| float          | 54.1 ms                                                | 55.0 ms: 1.02x slower                                                  |
| nbody          | 67.6 ms                                                | 101 ms: 1.49x slower                                                   |
| Geometric mean | (ref)                                                  | 1.15x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 2.44 ms                                                | 2.11 ms: 1.16x faster                                                  |
| regex_dna      | 143 ms                                                 | 137 ms: 1.04x faster                                                   |
| regex_v8       | 15.1 ms                                                | 15.7 ms: 1.04x slower                                                  |
| regex_compile  | 75.9 ms                                                | 86.8 ms: 1.14x slower                                                  |
| Geometric mean | (ref)                                                  | 1.00x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_iterparse  | 75.5 ms                                                | 66.3 ms: 1.14x faster                                                  |
| xml_etree_parse      | 108 ms                                                 | 96.8 ms: 1.11x faster                                                  |
| xml_etree_generate   | 55.4 ms                                                | 59.7 ms: 1.08x slower                                                  |
| json_loads           | 17.0 us                                                | 18.6 us: 1.09x slower                                                  |
| xml_etree_process    | 38.9 ms                                                | 44.6 ms: 1.15x slower                                                  |
| tomli_loads          | 1.36 sec                                               | 1.61 sec: 1.18x slower                                                 |
| unpickle_pure_python | 145 us                                                 | 182 us: 1.25x slower                                                   |
| pickle_pure_python   | 197 us                                                 | 250 us: 1.27x slower                                                   |
| json_dumps           | 6.19 ms                                                | 7.97 ms: 1.29x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.11x slower                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 17.8 ms                                                | 19.7 ms: 1.11x slower                                                  |
| python_startup_no_site | 13.2 ms                                                | 15.1 ms: 1.15x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.13x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_xml      | 30.5 ms                                                | 37.0 ms: 1.21x slower                                                  |
| genshi_text     | 14.7 ms                                                | 18.2 ms: 1.24x slower                                                  |
| django_template | 19.7 ms                                                | 26.2 ms: 1.33x slower                                                  |
| mako            | 7.44 ms                                                | 10.9 ms: 1.46x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.31x slower                                                           |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 13.5 ms: 2.37x faster                                                  |
| gc_traversal                     | 2.95 ms                                                | 1.39 ms: 2.12x faster                                                  |
| async_tree_io_tg                 | 673 ms                                                 | 328 ms: 2.05x faster                                                   |
| async_tree_eager_io              | 666 ms                                                 | 338 ms: 1.97x faster                                                   |
| async_tree_eager_io_tg           | 617 ms                                                 | 319 ms: 1.94x faster                                                   |
| async_tree_io                    | 672 ms                                                 | 352 ms: 1.91x faster                                                   |
| async_tree_none_tg               | 255 ms                                                 | 146 ms: 1.75x faster                                                   |
| async_tree_memoization_tg        | 318 ms                                                 | 187 ms: 1.71x faster                                                   |
| create_gc_cycles                 | 1.15 ms                                                | 736 us: 1.56x faster                                                   |
| async_tree_none                  | 263 ms                                                 | 170 ms: 1.55x faster                                                   |
| async_tree_memoization           | 310 ms                                                 | 210 ms: 1.47x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 394 ms: 1.34x faster                                                   |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 418 ms: 1.26x faster                                                   |
| deepcopy                         | 226 us                                                 | 183 us: 1.24x faster                                                   |
| sqlite_synth                     | 1.55 us                                                | 1.30 us: 1.19x faster                                                  |
| regex_effbot                     | 2.44 ms                                                | 2.11 ms: 1.16x faster                                                  |
| xml_etree_iterparse              | 75.5 ms                                                | 66.3 ms: 1.14x faster                                                  |
| xml_etree_parse                  | 108 ms                                                 | 96.8 ms: 1.11x faster                                                  |
| async_generators                 | 299 ms                                                 | 274 ms: 1.09x faster                                                   |
| async_tree_eager_memoization     | 168 ms                                                 | 157 ms: 1.07x faster                                                   |
| deepcopy_memo                    | 26.0 us                                                | 24.6 us: 1.06x faster                                                  |
| coroutines                       | 19.7 ms                                                | 18.7 ms: 1.05x faster                                                  |
| pathlib                          | 24.7 ms                                                | 23.6 ms: 1.05x faster                                                  |
| deepcopy_reduce                  | 2.01 us                                                | 1.93 us: 1.05x faster                                                  |
| regex_dna                        | 143 ms                                                 | 137 ms: 1.04x faster                                                   |
| asyncio_websockets               | 243 ms                                                 | 238 ms: 1.02x faster                                                   |
| k_core                           | 1.72 sec                                               | 1.69 sec: 1.02x faster                                                 |
| pidigits                         | 283 ms                                                 | 281 ms: 1.01x faster                                                   |
| bench_mp_pool                    | 65.5 ms                                                | 65.9 ms: 1.01x slower                                                  |
| sphinx                           | 613 ms                                                 | 622 ms: 1.02x slower                                                   |
| float                            | 54.1 ms                                                | 55.0 ms: 1.02x slower                                                  |
| bpe_tokeniser                    | 3.28 sec                                               | 3.34 sec: 1.02x slower                                                 |
| pycparser                        | 673 ms                                                 | 687 ms: 1.02x slower                                                   |
| comprehensions                   | 14.0 us                                                | 14.4 us: 1.03x slower                                                  |
| html5lib                         | 33.4 ms                                                | 34.6 ms: 1.04x slower                                                  |
| generators                       | 29.4 ms                                                | 30.5 ms: 1.04x slower                                                  |
| json                             | 3.00 ms                                                | 3.12 ms: 1.04x slower                                                  |
| regex_v8                         | 15.1 ms                                                | 15.7 ms: 1.04x slower                                                  |
| dulwich_log                      | 29.2 ms                                                | 31.1 ms: 1.06x slower                                                  |
| thrift                           | 468 us                                                 | 504 us: 1.08x slower                                                   |
| xml_etree_generate               | 55.4 ms                                                | 59.7 ms: 1.08x slower                                                  |
| go                               | 98.5 ms                                                | 106 ms: 1.08x slower                                                   |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 377 ms: 1.08x slower                                                   |
| json_loads                       | 17.0 us                                                | 18.6 us: 1.09x slower                                                  |
| mdp                              | 1.49 sec                                               | 1.64 sec: 1.10x slower                                                 |
| shortest_path                    | 331 ms                                                 | 366 ms: 1.11x slower                                                   |
| python_startup                   | 17.8 ms                                                | 19.7 ms: 1.11x slower                                                  |
| sympy_sum                        | 76.2 ms                                                | 85.2 ms: 1.12x slower                                                  |
| sqlalchemy_declarative           | 61.9 ms                                                | 69.3 ms: 1.12x slower                                                  |
| sqlglot_optimize                 | 33.2 ms                                                | 37.3 ms: 1.12x slower                                                  |
| logging_simple                   | 3.60 us                                                | 4.05 us: 1.12x slower                                                  |
| sqlglot_normalize                | 180 ms                                                 | 203 ms: 1.13x slower                                                   |
| logging_format                   | 3.90 us                                                | 4.45 us: 1.14x slower                                                  |
| regex_compile                    | 75.9 ms                                                | 86.8 ms: 1.14x slower                                                  |
| python_startup_no_site           | 13.2 ms                                                | 15.1 ms: 1.15x slower                                                  |
| xml_etree_process                | 38.9 ms                                                | 44.6 ms: 1.15x slower                                                  |
| 2to3                             | 168 ms                                                 | 195 ms: 1.16x slower                                                   |
| nqueens                          | 59.5 ms                                                | 69.0 ms: 1.16x slower                                                  |
| connected_components             | 300 ms                                                 | 348 ms: 1.16x slower                                                   |
| sympy_str                        | 144 ms                                                 | 167 ms: 1.16x slower                                                   |
| raytrace                         | 204 ms                                                 | 237 ms: 1.16x slower                                                   |
| sqlalchemy_imperative            | 6.60 ms                                                | 7.74 ms: 1.17x slower                                                  |
| deltablue                        | 2.57 ms                                                | 3.03 ms: 1.18x slower                                                  |
| chaos                            | 41.6 ms                                                | 49.3 ms: 1.18x slower                                                  |
| tomli_loads                      | 1.36 sec                                               | 1.61 sec: 1.18x slower                                                 |
| spectral_norm                    | 76.5 ms                                                | 90.7 ms: 1.19x slower                                                  |
| many_optionals                   | 403 us                                                 | 480 us: 1.19x slower                                                   |
| pyflate                          | 311 ms                                                 | 370 ms: 1.19x slower                                                   |
| sympy_integrate                  | 11.1 ms                                                | 13.2 ms: 1.19x slower                                                  |
| scimark_fft                      | 194 ms                                                 | 233 ms: 1.20x slower                                                   |
| sympy_expand                     | 233 ms                                                 | 280 ms: 1.20x slower                                                   |
| logging_silent                   | 72.5 ns                                                | 87.3 ns: 1.20x slower                                                  |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 171 ms: 1.20x slower                                                   |
| scimark_sor                      | 85.8 ms                                                | 104 ms: 1.21x slower                                                   |
| genshi_xml                       | 30.5 ms                                                | 37.0 ms: 1.21x slower                                                  |
| sqlglot_transpile                | 973 us                                                 | 1.20 ms: 1.23x slower                                                  |
| meteor_contest                   | 69.1 ms                                                | 85.3 ms: 1.23x slower                                                  |
| pprint_pformat                   | 986 ms                                                 | 1.22 sec: 1.24x slower                                                 |
| genshi_text                      | 14.7 ms                                                | 18.2 ms: 1.24x slower                                                  |
| pprint_safe_repr                 | 483 ms                                                 | 601 ms: 1.24x slower                                                   |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 3.93 ms: 1.25x slower                                                  |
| unpickle_pure_python             | 145 us                                                 | 182 us: 1.25x slower                                                   |
| sqlglot_parse                    | 808 us                                                 | 1.02 ms: 1.26x slower                                                  |
| pickle_pure_python               | 197 us                                                 | 250 us: 1.27x slower                                                   |
| typing_runtime_protocols         | 91.5 us                                                | 117 us: 1.28x slower                                                   |
| json_dumps                       | 6.19 ms                                                | 7.97 ms: 1.29x slower                                                  |
| fannkuch                         | 250 ms                                                 | 323 ms: 1.29x slower                                                   |
| async_tree_eager                 | 65.8 ms                                                | 85.3 ms: 1.30x slower                                                  |
| crypto_pyaes                     | 51.4 ms                                                | 67.2 ms: 1.31x slower                                                  |
| telco                            | 3.92 ms                                                | 5.16 ms: 1.32x slower                                                  |
| hexiom                           | 4.38 ms                                                | 5.78 ms: 1.32x slower                                                  |
| scimark_lu                       | 73.5 ms                                                | 97.2 ms: 1.32x slower                                                  |
| scimark_monte_carlo              | 44.5 ms                                                | 58.9 ms: 1.33x slower                                                  |
| django_template                  | 19.7 ms                                                | 26.2 ms: 1.33x slower                                                  |
| richards_super                   | 34.6 ms                                                | 47.7 ms: 1.38x slower                                                  |
| richards                         | 30.6 ms                                                | 42.3 ms: 1.39x slower                                                  |
| coverage                         | 38.5 ms                                                | 54.0 ms: 1.40x slower                                                  |
| mako                             | 7.44 ms                                                | 10.9 ms: 1.46x slower                                                  |
| nbody                            | 67.6 ms                                                | 101 ms: 1.49x slower                                                   |
| bench_thread_pool                | 483 us                                                 | 815 us: 1.69x slower                                                   |
| async_tree_eager_tg              | 46.9 ms                                                | 127 ms: 2.71x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.05x slower                                                           |

Benchmark hidden because not significant (3): pylint, docutils, async_tree_eager_cpu_io_mixed
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (8) of results/bm-20250222-3.14.0a5+-5ec4bf8-NOGIL/bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.041x slower

# HPT report

- Reliability score: 99.92% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.22x