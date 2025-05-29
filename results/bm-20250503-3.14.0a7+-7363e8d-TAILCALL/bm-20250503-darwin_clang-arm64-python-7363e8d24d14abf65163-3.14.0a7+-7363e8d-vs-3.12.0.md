# Results vs. 3.12.0

- fork: python
- ref: 7363e8d24d14abf65163
- machine: darwin-arm64
- commit hash: 7363e8d
- commit date: 2025-05-03
- overall geometric mean: 1.134x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250503-darwin-arm64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 155 ms: 1.09x faster                                                   |
| docutils       | 1.45 sec                                               | 1.39 sec: 1.04x faster                                                 |
| html5lib       | 33.4 ms                                                | 29.2 ms: 1.14x faster                                                  |
| sphinx         | 613 ms                                                 | 556 ms: 1.10x faster                                                   |
| Geometric mean | (ref)                                                  | 1.09x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250503-darwin-arm64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io                    | 672 ms                                                 | 339 ms: 1.98x faster                                                   |
| async_tree_io_tg                 | 673 ms                                                 | 349 ms: 1.93x faster                                                   |
| async_tree_eager_io              | 666 ms                                                 | 347 ms: 1.92x faster                                                   |
| async_tree_eager_io_tg           | 617 ms                                                 | 346 ms: 1.78x faster                                                   |
| async_tree_none_tg               | 255 ms                                                 | 145 ms: 1.76x faster                                                   |
| async_tree_memoization_tg        | 318 ms                                                 | 184 ms: 1.73x faster                                                   |
| async_tree_none                  | 263 ms                                                 | 153 ms: 1.72x faster                                                   |
| async_tree_memoization           | 310 ms                                                 | 184 ms: 1.69x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 403 ms: 1.31x faster                                                   |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 405 ms: 1.30x faster                                                   |
| coroutines                       | 19.7 ms                                                | 15.2 ms: 1.30x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 132 ms: 1.27x faster                                                   |
| async_tree_eager                 | 65.8 ms                                                | 58.0 ms: 1.13x faster                                                  |
| async_generators                 | 299 ms                                                 | 279 ms: 1.07x faster                                                   |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 351 ms: 1.07x faster                                                   |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 380 ms: 1.09x slower                                                   |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 163 ms: 1.15x slower                                                   |
| async_tree_eager_tg              | 46.9 ms                                                | 125 ms: 2.66x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.29x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250503-darwin-arm64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 54.1 ms                                                | 43.8 ms: 1.24x faster                                                  |
| pidigits       | 283 ms                                                 | 280 ms: 1.01x faster                                                   |
| nbody          | 67.6 ms                                                | 73.4 ms: 1.09x slower                                                  |
| Geometric mean | (ref)                                                  | 1.05x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250503-darwin-arm64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 75.9 ms                                                | 61.7 ms: 1.23x faster                                                  |
| regex_effbot   | 2.44 ms                                                | 2.20 ms: 1.11x faster                                                  |
| regex_dna      | 143 ms                                                 | 141 ms: 1.01x faster                                                   |
| regex_v8       | 15.1 ms                                                | 15.5 ms: 1.03x slower                                                  |
| Geometric mean | (ref)                                                  | 1.07x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250503-darwin-arm64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 1.36 sec                                               | 1.19 sec: 1.14x faster                                                 |
| unpickle_pure_python | 145 us                                                 | 129 us: 1.13x faster                                                   |
| xml_etree_generate   | 55.4 ms                                                | 49.6 ms: 1.12x faster                                                  |
| xml_etree_process    | 38.9 ms                                                | 35.2 ms: 1.11x faster                                                  |
| xml_etree_iterparse  | 75.5 ms                                                | 70.8 ms: 1.07x faster                                                  |
| pickle_pure_python   | 197 us                                                 | 186 us: 1.06x faster                                                   |
| xml_etree_parse      | 108 ms                                                 | 105 ms: 1.03x faster                                                   |
| json_loads           | 17.0 us                                                | 18.5 us: 1.08x slower                                                  |
| json_dumps           | 6.19 ms                                                | 7.37 ms: 1.19x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250503-darwin-arm64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 17.8 ms                                                | 19.6 ms: 1.10x slower                                                  |
| python_startup_no_site | 13.2 ms                                                | 14.7 ms: 1.11x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.11x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250503-darwin-arm64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 14.7 ms                                                | 12.9 ms: 1.14x faster                                                  |
| genshi_xml      | 30.5 ms                                                | 27.2 ms: 1.12x faster                                                  |
| mako            | 7.44 ms                                                | 7.19 ms: 1.04x faster                                                  |
| django_template | 19.7 ms                                                | 19.7 ms: 1.00x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.07x faster                                                           |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250503-darwin-arm64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 12.6 ms: 2.55x faster                                                  |
| mdp                              | 1.49 sec                                               | 701 ms: 2.13x faster                                                   |
| async_tree_io                    | 672 ms                                                 | 339 ms: 1.98x faster                                                   |
| async_tree_io_tg                 | 673 ms                                                 | 349 ms: 1.93x faster                                                   |
| async_tree_eager_io              | 666 ms                                                 | 347 ms: 1.92x faster                                                   |
| async_tree_eager_io_tg           | 617 ms                                                 | 346 ms: 1.78x faster                                                   |
| async_tree_none_tg               | 255 ms                                                 | 145 ms: 1.76x faster                                                   |
| async_tree_memoization_tg        | 318 ms                                                 | 184 ms: 1.73x faster                                                   |
| async_tree_none                  | 263 ms                                                 | 153 ms: 1.72x faster                                                   |
| async_tree_memoization           | 310 ms                                                 | 184 ms: 1.69x faster                                                   |
| generators                       | 29.4 ms                                                | 18.7 ms: 1.57x faster                                                  |
| deepcopy_memo                    | 26.0 us                                                | 16.6 us: 1.57x faster                                                  |
| deepcopy                         | 226 us                                                 | 145 us: 1.56x faster                                                   |
| go                               | 98.5 ms                                                | 71.1 ms: 1.39x faster                                                  |
| comprehensions                   | 14.0 us                                                | 10.5 us: 1.33x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 403 ms: 1.31x faster                                                   |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 405 ms: 1.30x faster                                                   |
| coroutines                       | 19.7 ms                                                | 15.2 ms: 1.30x faster                                                  |
| deepcopy_reduce                  | 2.01 us                                                | 1.56 us: 1.29x faster                                                  |
| raytrace                         | 204 ms                                                 | 160 ms: 1.27x faster                                                   |
| async_tree_eager_memoization     | 168 ms                                                 | 132 ms: 1.27x faster                                                   |
| deltablue                        | 2.57 ms                                                | 2.05 ms: 1.25x faster                                                  |
| float                            | 54.1 ms                                                | 43.8 ms: 1.24x faster                                                  |
| dulwich_log                      | 29.2 ms                                                | 23.7 ms: 1.23x faster                                                  |
| regex_compile                    | 75.9 ms                                                | 61.7 ms: 1.23x faster                                                  |
| logging_silent                   | 72.5 ns                                                | 60.2 ns: 1.21x faster                                                  |
| logging_simple                   | 3.60 us                                                | 3.01 us: 1.20x faster                                                  |
| pylint                           | 182 ms                                                 | 152 ms: 1.19x faster                                                   |
| logging_format                   | 3.90 us                                                | 3.32 us: 1.17x faster                                                  |
| chaos                            | 41.6 ms                                                | 35.5 ms: 1.17x faster                                                  |
| hexiom                           | 4.38 ms                                                | 3.79 ms: 1.15x faster                                                  |
| html5lib                         | 33.4 ms                                                | 29.2 ms: 1.14x faster                                                  |
| tomli_loads                      | 1.36 sec                                               | 1.19 sec: 1.14x faster                                                 |
| genshi_text                      | 14.7 ms                                                | 12.9 ms: 1.14x faster                                                  |
| k_core                           | 1.72 sec                                               | 1.52 sec: 1.13x faster                                                 |
| async_tree_eager                 | 65.8 ms                                                | 58.0 ms: 1.13x faster                                                  |
| bpe_tokeniser                    | 3.28 sec                                               | 2.91 sec: 1.13x faster                                                 |
| unpickle_pure_python             | 145 us                                                 | 129 us: 1.13x faster                                                   |
| pyflate                          | 311 ms                                                 | 276 ms: 1.12x faster                                                   |
| genshi_xml                       | 30.5 ms                                                | 27.2 ms: 1.12x faster                                                  |
| xml_etree_generate               | 55.4 ms                                                | 49.6 ms: 1.12x faster                                                  |
| spectral_norm                    | 76.5 ms                                                | 68.7 ms: 1.11x faster                                                  |
| regex_effbot                     | 2.44 ms                                                | 2.20 ms: 1.11x faster                                                  |
| xml_etree_process                | 38.9 ms                                                | 35.2 ms: 1.11x faster                                                  |
| sphinx                           | 613 ms                                                 | 556 ms: 1.10x faster                                                   |
| scimark_sor                      | 85.8 ms                                                | 78.0 ms: 1.10x faster                                                  |
| sqlalchemy_declarative           | 61.9 ms                                                | 56.3 ms: 1.10x faster                                                  |
| scimark_monte_carlo              | 44.5 ms                                                | 40.6 ms: 1.09x faster                                                  |
| nqueens                          | 59.5 ms                                                | 54.4 ms: 1.09x faster                                                  |
| 2to3                             | 168 ms                                                 | 155 ms: 1.09x faster                                                   |
| sympy_str                        | 144 ms                                                 | 132 ms: 1.09x faster                                                   |
| sympy_sum                        | 76.2 ms                                                | 70.2 ms: 1.09x faster                                                  |
| sympy_integrate                  | 11.1 ms                                                | 10.2 ms: 1.09x faster                                                  |
| pycparser                        | 673 ms                                                 | 626 ms: 1.08x faster                                                   |
| async_generators                 | 299 ms                                                 | 279 ms: 1.07x faster                                                   |
| xml_etree_iterparse              | 75.5 ms                                                | 70.8 ms: 1.07x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 351 ms: 1.07x faster                                                   |
| pickle_pure_python               | 197 us                                                 | 186 us: 1.06x faster                                                   |
| pathlib                          | 24.7 ms                                                | 23.5 ms: 1.05x faster                                                  |
| sqlalchemy_imperative            | 6.60 ms                                                | 6.28 ms: 1.05x faster                                                  |
| pprint_pformat                   | 986 ms                                                 | 940 ms: 1.05x faster                                                   |
| sympy_expand                     | 233 ms                                                 | 223 ms: 1.05x faster                                                   |
| richards_super                   | 34.6 ms                                                | 33.0 ms: 1.05x faster                                                  |
| docutils                         | 1.45 sec                                               | 1.39 sec: 1.04x faster                                                 |
| scimark_lu                       | 73.5 ms                                                | 70.4 ms: 1.04x faster                                                  |
| richards                         | 30.6 ms                                                | 29.4 ms: 1.04x faster                                                  |
| mako                             | 7.44 ms                                                | 7.19 ms: 1.04x faster                                                  |
| crypto_pyaes                     | 51.4 ms                                                | 49.9 ms: 1.03x faster                                                  |
| xml_etree_parse                  | 108 ms                                                 | 105 ms: 1.03x faster                                                   |
| pprint_safe_repr                 | 483 ms                                                 | 471 ms: 1.03x faster                                                   |
| bench_thread_pool                | 483 us                                                 | 471 us: 1.02x faster                                                   |
| typing_runtime_protocols         | 91.5 us                                                | 90.0 us: 1.02x faster                                                  |
| shortest_path                    | 331 ms                                                 | 327 ms: 1.01x faster                                                   |
| pidigits                         | 283 ms                                                 | 280 ms: 1.01x faster                                                   |
| regex_dna                        | 143 ms                                                 | 141 ms: 1.01x faster                                                   |
| django_template                  | 19.7 ms                                                | 19.7 ms: 1.00x faster                                                  |
| connected_components             | 300 ms                                                 | 302 ms: 1.01x slower                                                   |
| sqlite_synth                     | 1.55 us                                                | 1.58 us: 1.02x slower                                                  |
| json                             | 3.00 ms                                                | 3.07 ms: 1.02x slower                                                  |
| fannkuch                         | 250 ms                                                 | 257 ms: 1.03x slower                                                   |
| regex_v8                         | 15.1 ms                                                | 15.5 ms: 1.03x slower                                                  |
| meteor_contest                   | 69.1 ms                                                | 71.2 ms: 1.03x slower                                                  |
| gc_traversal                     | 2.95 ms                                                | 3.09 ms: 1.05x slower                                                  |
| scimark_fft                      | 194 ms                                                 | 204 ms: 1.05x slower                                                   |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 3.32 ms: 1.06x slower                                                  |
| many_optionals                   | 403 us                                                 | 436 us: 1.08x slower                                                   |
| json_loads                       | 17.0 us                                                | 18.5 us: 1.08x slower                                                  |
| nbody                            | 67.6 ms                                                | 73.4 ms: 1.09x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 380 ms: 1.09x slower                                                   |
| python_startup                   | 17.8 ms                                                | 19.6 ms: 1.10x slower                                                  |
| create_gc_cycles                 | 1.15 ms                                                | 1.28 ms: 1.11x slower                                                  |
| python_startup_no_site           | 13.2 ms                                                | 14.7 ms: 1.11x slower                                                  |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 163 ms: 1.15x slower                                                   |
| json_dumps                       | 6.19 ms                                                | 7.37 ms: 1.19x slower                                                  |
| telco                            | 3.92 ms                                                | 4.69 ms: 1.20x slower                                                  |
| coverage                         | 38.5 ms                                                | 46.1 ms: 1.20x slower                                                  |
| async_tree_eager_tg              | 46.9 ms                                                | 125 ms: 2.66x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.13x faster                                                           |

Benchmark hidden because not significant (2): asyncio_websockets, bench_mp_pool
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: chameleon, dask, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (12) of results/bm-20250503-3.14.0a7+-7363e8d-CLANG/bm-20250503-darwin-arm64-python-7363e8d24d14abf65163-3.14.0a7+-7363e8d.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.134x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 1.11x