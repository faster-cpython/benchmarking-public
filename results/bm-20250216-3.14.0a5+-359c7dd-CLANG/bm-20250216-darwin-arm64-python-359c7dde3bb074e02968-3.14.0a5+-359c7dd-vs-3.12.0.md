# Results vs. 3.12.0

- fork: python
- ref: 359c7dde3bb074e02968
- machine: darwin-arm64
- commit hash: 359c7dd
- commit date: 2025-02-16
- overall geometric mean: 1.150x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250216-darwin-arm64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 153 ms: 1.10x faster                                                   |
| docutils       | 1.45 sec                                               | 1.36 sec: 1.07x faster                                                 |
| html5lib       | 33.4 ms                                                | 28.9 ms: 1.16x faster                                                  |
| sphinx         | 613 ms                                                 | 540 ms: 1.13x faster                                                   |
| Geometric mean | (ref)                                                  | 1.11x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250216-darwin-arm64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io                    | 672 ms                                                 | 343 ms: 1.96x faster                                                   |
| async_tree_io_tg                 | 673 ms                                                 | 345 ms: 1.95x faster                                                   |
| async_tree_eager_io              | 666 ms                                                 | 344 ms: 1.94x faster                                                   |
| async_tree_eager_io_tg           | 617 ms                                                 | 349 ms: 1.77x faster                                                   |
| async_tree_none_tg               | 255 ms                                                 | 145 ms: 1.76x faster                                                   |
| async_tree_none                  | 263 ms                                                 | 152 ms: 1.73x faster                                                   |
| async_tree_memoization_tg        | 318 ms                                                 | 185 ms: 1.72x faster                                                   |
| async_tree_memoization           | 310 ms                                                 | 183 ms: 1.69x faster                                                   |
| coroutines                       | 19.7 ms                                                | 14.9 ms: 1.32x faster                                                  |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 401 ms: 1.31x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 403 ms: 1.31x faster                                                   |
| async_tree_eager_memoization     | 168 ms                                                 | 135 ms: 1.24x faster                                                   |
| async_generators                 | 299 ms                                                 | 252 ms: 1.19x faster                                                   |
| async_tree_eager                 | 65.8 ms                                                | 58.9 ms: 1.12x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 349 ms: 1.07x faster                                                   |
| asyncio_websockets               | 243 ms                                                 | 242 ms: 1.00x faster                                                   |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 381 ms: 1.10x slower                                                   |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 165 ms: 1.16x slower                                                   |
| async_tree_eager_tg              | 46.9 ms                                                | 124 ms: 2.63x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.30x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250216-darwin-arm64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 54.1 ms                                                | 44.4 ms: 1.22x faster                                                  |
| nbody          | 67.6 ms                                                | 62.8 ms: 1.08x faster                                                  |
| pidigits       | 283 ms                                                 | 280 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                  | 1.10x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250216-darwin-arm64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 75.9 ms                                                | 61.7 ms: 1.23x faster                                                  |
| regex_effbot   | 2.44 ms                                                | 2.34 ms: 1.04x faster                                                  |
| regex_dna      | 143 ms                                                 | 145 ms: 1.02x slower                                                   |
| regex_v8       | 15.1 ms                                                | 17.6 ms: 1.17x slower                                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250216-darwin-arm64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 1.36 sec                                               | 1.15 sec: 1.18x faster                                                 |
| unpickle_pure_python | 145 us                                                 | 124 us: 1.18x faster                                                   |
| xml_etree_process    | 38.9 ms                                                | 33.6 ms: 1.16x faster                                                  |
| xml_etree_generate   | 55.4 ms                                                | 48.2 ms: 1.15x faster                                                  |
| xml_etree_iterparse  | 75.5 ms                                                | 68.9 ms: 1.10x faster                                                  |
| xml_etree_parse      | 108 ms                                                 | 101 ms: 1.07x faster                                                   |
| pickle_pure_python   | 197 us                                                 | 186 us: 1.06x faster                                                   |
| json_loads           | 17.0 us                                                | 17.9 us: 1.05x slower                                                  |
| json_dumps           | 6.19 ms                                                | 7.12 ms: 1.15x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250216-darwin-arm64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup | 17.8 ms                                                | 18.0 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                  | 1.01x slower                                                           |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250216-darwin-arm64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 14.7 ms                                                | 12.6 ms: 1.17x faster                                                  |
| genshi_xml      | 30.5 ms                                                | 26.7 ms: 1.14x faster                                                  |
| django_template | 19.7 ms                                                | 18.8 ms: 1.05x faster                                                  |
| mako            | 7.44 ms                                                | 7.14 ms: 1.04x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.10x faster                                                           |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250216-darwin-arm64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 11.3 ms: 2.84x faster                                                  |
| async_tree_io                    | 672 ms                                                 | 343 ms: 1.96x faster                                                   |
| async_tree_io_tg                 | 673 ms                                                 | 345 ms: 1.95x faster                                                   |
| async_tree_eager_io              | 666 ms                                                 | 344 ms: 1.94x faster                                                   |
| async_tree_eager_io_tg           | 617 ms                                                 | 349 ms: 1.77x faster                                                   |
| async_tree_none_tg               | 255 ms                                                 | 145 ms: 1.76x faster                                                   |
| async_tree_none                  | 263 ms                                                 | 152 ms: 1.73x faster                                                   |
| async_tree_memoization_tg        | 318 ms                                                 | 185 ms: 1.72x faster                                                   |
| async_tree_memoization           | 310 ms                                                 | 183 ms: 1.69x faster                                                   |
| generators                       | 29.4 ms                                                | 17.7 ms: 1.66x faster                                                  |
| deepcopy                         | 226 us                                                 | 139 us: 1.62x faster                                                   |
| deepcopy_memo                    | 26.0 us                                                | 16.6 us: 1.56x faster                                                  |
| comprehensions                   | 14.0 us                                                | 9.74 us: 1.44x faster                                                  |
| go                               | 98.5 ms                                                | 70.6 ms: 1.39x faster                                                  |
| deepcopy_reduce                  | 2.01 us                                                | 1.48 us: 1.36x faster                                                  |
| coroutines                       | 19.7 ms                                                | 14.9 ms: 1.32x faster                                                  |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 401 ms: 1.31x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 403 ms: 1.31x faster                                                   |
| logging_silent                   | 72.5 ns                                                | 57.5 ns: 1.26x faster                                                  |
| raytrace                         | 204 ms                                                 | 163 ms: 1.25x faster                                                   |
| deltablue                        | 2.57 ms                                                | 2.05 ms: 1.25x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 135 ms: 1.24x faster                                                   |
| regex_compile                    | 75.9 ms                                                | 61.7 ms: 1.23x faster                                                  |
| pylint                           | 182 ms                                                 | 149 ms: 1.22x faster                                                   |
| logging_simple                   | 3.60 us                                                | 2.95 us: 1.22x faster                                                  |
| float                            | 54.1 ms                                                | 44.4 ms: 1.22x faster                                                  |
| logging_format                   | 3.90 us                                                | 3.23 us: 1.21x faster                                                  |
| async_generators                 | 299 ms                                                 | 252 ms: 1.19x faster                                                   |
| tomli_loads                      | 1.36 sec                                               | 1.15 sec: 1.18x faster                                                 |
| unpickle_pure_python             | 145 us                                                 | 124 us: 1.18x faster                                                   |
| chaos                            | 41.6 ms                                                | 35.5 ms: 1.17x faster                                                  |
| genshi_text                      | 14.7 ms                                                | 12.6 ms: 1.17x faster                                                  |
| k_core                           | 1.72 sec                                               | 1.48 sec: 1.17x faster                                                 |
| nqueens                          | 59.5 ms                                                | 51.3 ms: 1.16x faster                                                  |
| bpe_tokeniser                    | 3.28 sec                                               | 2.83 sec: 1.16x faster                                                 |
| sqlglot_parse                    | 808 us                                                 | 698 us: 1.16x faster                                                   |
| xml_etree_process                | 38.9 ms                                                | 33.6 ms: 1.16x faster                                                  |
| html5lib                         | 33.4 ms                                                | 28.9 ms: 1.16x faster                                                  |
| hexiom                           | 4.38 ms                                                | 3.79 ms: 1.15x faster                                                  |
| scimark_sor                      | 85.8 ms                                                | 74.4 ms: 1.15x faster                                                  |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 2.73 ms: 1.15x faster                                                  |
| sqlglot_transpile                | 973 us                                                 | 846 us: 1.15x faster                                                   |
| xml_etree_generate               | 55.4 ms                                                | 48.2 ms: 1.15x faster                                                  |
| thrift                           | 468 us                                                 | 408 us: 1.15x faster                                                   |
| sqlalchemy_declarative           | 61.9 ms                                                | 54.1 ms: 1.14x faster                                                  |
| genshi_xml                       | 30.5 ms                                                | 26.7 ms: 1.14x faster                                                  |
| sphinx                           | 613 ms                                                 | 540 ms: 1.13x faster                                                   |
| scimark_fft                      | 194 ms                                                 | 172 ms: 1.13x faster                                                   |
| bench_mp_pool                    | 65.5 ms                                                | 58.1 ms: 1.13x faster                                                  |
| pprint_pformat                   | 986 ms                                                 | 874 ms: 1.13x faster                                                   |
| spectral_norm                    | 76.5 ms                                                | 67.9 ms: 1.13x faster                                                  |
| scimark_monte_carlo              | 44.5 ms                                                | 39.5 ms: 1.12x faster                                                  |
| async_tree_eager                 | 65.8 ms                                                | 58.9 ms: 1.12x faster                                                  |
| sympy_str                        | 144 ms                                                 | 129 ms: 1.12x faster                                                   |
| sqlglot_optimize                 | 33.2 ms                                                | 29.8 ms: 1.11x faster                                                  |
| pathlib                          | 24.7 ms                                                | 22.2 ms: 1.11x faster                                                  |
| pprint_safe_repr                 | 483 ms                                                 | 435 ms: 1.11x faster                                                   |
| richards_super                   | 34.6 ms                                                | 31.2 ms: 1.11x faster                                                  |
| richards                         | 30.6 ms                                                | 27.6 ms: 1.11x faster                                                  |
| sympy_sum                        | 76.2 ms                                                | 69.0 ms: 1.10x faster                                                  |
| dulwich_log                      | 29.2 ms                                                | 26.5 ms: 1.10x faster                                                  |
| 2to3                             | 168 ms                                                 | 153 ms: 1.10x faster                                                   |
| xml_etree_iterparse              | 75.5 ms                                                | 68.9 ms: 1.10x faster                                                  |
| pycparser                        | 673 ms                                                 | 615 ms: 1.10x faster                                                   |
| sqlglot_normalize                | 180 ms                                                 | 164 ms: 1.09x faster                                                   |
| sympy_integrate                  | 11.1 ms                                                | 10.2 ms: 1.09x faster                                                  |
| sqlalchemy_imperative            | 6.60 ms                                                | 6.07 ms: 1.09x faster                                                  |
| sympy_expand                     | 233 ms                                                 | 216 ms: 1.08x faster                                                   |
| nbody                            | 67.6 ms                                                | 62.8 ms: 1.08x faster                                                  |
| typing_runtime_protocols         | 91.5 us                                                | 85.3 us: 1.07x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 349 ms: 1.07x faster                                                   |
| docutils                         | 1.45 sec                                               | 1.36 sec: 1.07x faster                                                 |
| xml_etree_parse                  | 108 ms                                                 | 101 ms: 1.07x faster                                                   |
| bench_thread_pool                | 483 us                                                 | 455 us: 1.06x faster                                                   |
| pickle_pure_python               | 197 us                                                 | 186 us: 1.06x faster                                                   |
| pyflate                          | 311 ms                                                 | 295 ms: 1.05x faster                                                   |
| django_template                  | 19.7 ms                                                | 18.8 ms: 1.05x faster                                                  |
| mdp                              | 1.49 sec                                               | 1.43 sec: 1.04x faster                                                 |
| regex_effbot                     | 2.44 ms                                                | 2.34 ms: 1.04x faster                                                  |
| mako                             | 7.44 ms                                                | 7.14 ms: 1.04x faster                                                  |
| crypto_pyaes                     | 51.4 ms                                                | 49.5 ms: 1.04x faster                                                  |
| scimark_lu                       | 73.5 ms                                                | 71.0 ms: 1.04x faster                                                  |
| sqlite_synth                     | 1.55 us                                                | 1.50 us: 1.03x faster                                                  |
| shortest_path                    | 331 ms                                                 | 323 ms: 1.02x faster                                                   |
| dask                             | 779 ms                                                 | 770 ms: 1.01x faster                                                   |
| connected_components             | 300 ms                                                 | 296 ms: 1.01x faster                                                   |
| pidigits                         | 283 ms                                                 | 280 ms: 1.01x faster                                                   |
| asyncio_websockets               | 243 ms                                                 | 242 ms: 1.00x faster                                                   |
| json                             | 3.00 ms                                                | 3.03 ms: 1.01x slower                                                  |
| python_startup                   | 17.8 ms                                                | 18.0 ms: 1.01x slower                                                  |
| regex_dna                        | 143 ms                                                 | 145 ms: 1.02x slower                                                   |
| meteor_contest                   | 69.1 ms                                                | 70.7 ms: 1.02x slower                                                  |
| many_optionals                   | 403 us                                                 | 414 us: 1.03x slower                                                   |
| gc_traversal                     | 2.95 ms                                                | 3.07 ms: 1.04x slower                                                  |
| json_loads                       | 17.0 us                                                | 17.9 us: 1.05x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 381 ms: 1.10x slower                                                   |
| create_gc_cycles                 | 1.15 ms                                                | 1.27 ms: 1.10x slower                                                  |
| json_dumps                       | 6.19 ms                                                | 7.12 ms: 1.15x slower                                                  |
| telco                            | 3.92 ms                                                | 4.52 ms: 1.15x slower                                                  |
| coverage                         | 38.5 ms                                                | 44.6 ms: 1.16x slower                                                  |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 165 ms: 1.16x slower                                                   |
| regex_v8                         | 15.1 ms                                                | 17.6 ms: 1.17x slower                                                  |
| async_tree_eager_tg              | 46.9 ms                                                | 124 ms: 2.63x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.15x faster                                                           |

Benchmark hidden because not significant (2): fannkuch, python_startup_no_site
Ignored benchmarks (5) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (8) of results/bm-20250216-3.14.0a5+-359c7dd-CLANG/bm-20250216-darwin-arm64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.150x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.10x
- 95% likely to have a speedup of 1.09x
- 99% likely to have a speedup of 1.08x

# Memory
- memory change: 1.08x