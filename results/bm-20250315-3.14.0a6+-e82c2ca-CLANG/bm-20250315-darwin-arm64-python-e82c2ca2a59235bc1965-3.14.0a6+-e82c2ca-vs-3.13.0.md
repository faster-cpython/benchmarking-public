# Results vs. 3.13.0

- fork: python
- ref: e82c2ca2a59235bc1965
- machine: darwin-arm64
- commit hash: e82c2ca
- commit date: 2025-03-15
- overall geometric mean: 1.099x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250315-darwin-arm64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 157 ms: 1.13x faster                                                   |
| html5lib       | 36.7 ms                                                | 30.6 ms: 1.20x faster                                                  |
| sphinx         | 602 ms                                                 | 575 ms: 1.05x faster                                                   |
| Geometric mean | (ref)                                                  | 1.09x faster                                                           |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250315-darwin-arm64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 189 ms: 1.52x faster                                                   |
| async_tree_eager_io              | 511 ms                                                 | 347 ms: 1.47x faster                                                   |
| async_tree_io                    | 508 ms                                                 | 354 ms: 1.43x faster                                                   |
| async_tree_memoization           | 268 ms                                                 | 189 ms: 1.42x faster                                                   |
| async_tree_io_tg                 | 500 ms                                                 | 359 ms: 1.40x faster                                                   |
| async_tree_none                  | 212 ms                                                 | 156 ms: 1.36x faster                                                   |
| async_tree_eager_io_tg           | 479 ms                                                 | 358 ms: 1.34x faster                                                   |
| async_tree_none_tg               | 198 ms                                                 | 149 ms: 1.33x faster                                                   |
| coroutines                       | 20.0 ms                                                | 15.2 ms: 1.32x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 137 ms: 1.23x faster                                                   |
| async_tree_eager                 | 69.9 ms                                                | 58.5 ms: 1.20x faster                                                  |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 413 ms: 1.11x faster                                                   |
| async_generators                 | 294 ms                                                 | 264 ms: 1.11x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 414 ms: 1.08x faster                                                   |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 355 ms: 1.05x faster                                                   |
| asyncio_websockets               | 242 ms                                                 | 250 ms: 1.03x slower                                                   |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 392 ms: 1.13x slower                                                   |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 168 ms: 1.22x slower                                                   |
| async_tree_eager_tg              | 47.4 ms                                                | 124 ms: 2.62x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.13x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250315-darwin-arm64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 45.8 ms: 1.22x faster                                                  |
| nbody          | 73.6 ms                                                | 66.7 ms: 1.10x faster                                                  |
| pidigits       | 284 ms                                                 | 290 ms: 1.02x slower                                                   |
| Geometric mean | (ref)                                                  | 1.10x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250315-darwin-arm64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 78.3 ms                                                | 65.8 ms: 1.19x faster                                                  |
| regex_effbot   | 2.63 ms                                                | 2.45 ms: 1.08x faster                                                  |
| regex_v8       | 17.0 ms                                                | 17.4 ms: 1.02x slower                                                  |
| regex_dna      | 149 ms                                                 | 153 ms: 1.03x slower                                                   |
| Geometric mean | (ref)                                                  | 1.05x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250315-darwin-arm64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 1.57 sec                                               | 1.21 sec: 1.29x faster                                                 |
| unpickle_pure_python | 165 us                                                 | 134 us: 1.23x faster                                                   |
| xml_etree_process    | 41.3 ms                                                | 35.5 ms: 1.16x faster                                                  |
| xml_etree_generate   | 57.1 ms                                                | 51.0 ms: 1.12x faster                                                  |
| pickle_pure_python   | 215 us                                                 | 194 us: 1.11x faster                                                   |
| xml_etree_iterparse  | 74.2 ms                                                | 70.3 ms: 1.06x faster                                                  |
| xml_etree_parse      | 108 ms                                                 | 103 ms: 1.05x faster                                                   |
| json_loads           | 17.0 us                                                | 18.3 us: 1.08x slower                                                  |
| json_dumps           | 6.47 ms                                                | 7.44 ms: 1.15x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.08x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250315-darwin-arm64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup | 18.8 ms                                                | 18.0 ms: 1.04x faster                                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                                           |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250315-darwin-arm64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 13.3 ms: 1.27x faster                                                  |
| genshi_xml      | 34.1 ms                                                | 28.4 ms: 1.20x faster                                                  |
| mako            | 7.75 ms                                                | 7.56 ms: 1.02x faster                                                  |
| django_template | 20.5 ms                                                | 20.1 ms: 1.02x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.12x faster                                                           |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250315-darwin-arm64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| generators                       | 31.9 ms                                                | 19.0 ms: 1.68x faster                                                  |
| deepcopy                         | 236 us                                                 | 146 us: 1.61x faster                                                   |
| deepcopy_memo                    | 27.4 us                                                | 17.3 us: 1.58x faster                                                  |
| go                               | 117 ms                                                 | 76.2 ms: 1.53x faster                                                  |
| async_tree_memoization_tg        | 288 ms                                                 | 189 ms: 1.52x faster                                                   |
| async_tree_eager_io              | 511 ms                                                 | 347 ms: 1.47x faster                                                   |
| async_tree_io                    | 508 ms                                                 | 354 ms: 1.43x faster                                                   |
| async_tree_memoization           | 268 ms                                                 | 189 ms: 1.42x faster                                                   |
| scimark_sor                      | 106 ms                                                 | 75.1 ms: 1.41x faster                                                  |
| async_tree_io_tg                 | 500 ms                                                 | 359 ms: 1.40x faster                                                   |
| async_tree_none                  | 212 ms                                                 | 156 ms: 1.36x faster                                                   |
| deepcopy_reduce                  | 2.09 us                                                | 1.56 us: 1.34x faster                                                  |
| async_tree_eager_io_tg           | 479 ms                                                 | 358 ms: 1.34x faster                                                   |
| async_tree_none_tg               | 198 ms                                                 | 149 ms: 1.33x faster                                                   |
| coroutines                       | 20.0 ms                                                | 15.2 ms: 1.32x faster                                                  |
| tomli_loads                      | 1.57 sec                                               | 1.21 sec: 1.29x faster                                                 |
| genshi_text                      | 16.9 ms                                                | 13.3 ms: 1.27x faster                                                  |
| unpickle_pure_python             | 165 us                                                 | 134 us: 1.23x faster                                                   |
| scimark_monte_carlo              | 50.4 ms                                                | 41.0 ms: 1.23x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 137 ms: 1.23x faster                                                   |
| float                            | 55.8 ms                                                | 45.8 ms: 1.22x faster                                                  |
| deltablue                        | 2.65 ms                                                | 2.18 ms: 1.21x faster                                                  |
| hexiom                           | 4.87 ms                                                | 4.02 ms: 1.21x faster                                                  |
| genshi_xml                       | 34.1 ms                                                | 28.4 ms: 1.20x faster                                                  |
| html5lib                         | 36.7 ms                                                | 30.6 ms: 1.20x faster                                                  |
| async_tree_eager                 | 69.9 ms                                                | 58.5 ms: 1.20x faster                                                  |
| richards                         | 36.2 ms                                                | 30.4 ms: 1.19x faster                                                  |
| regex_compile                    | 78.3 ms                                                | 65.8 ms: 1.19x faster                                                  |
| dulwich_log                      | 28.7 ms                                                | 24.3 ms: 1.19x faster                                                  |
| logging_silent                   | 71.0 ns                                                | 60.0 ns: 1.18x faster                                                  |
| pprint_pformat                   | 1.10 sec                                               | 942 ms: 1.17x faster                                                   |
| pprint_safe_repr                 | 541 ms                                                 | 463 ms: 1.17x faster                                                   |
| xml_etree_process                | 41.3 ms                                                | 35.5 ms: 1.16x faster                                                  |
| pylint                           | 180 ms                                                 | 156 ms: 1.15x faster                                                   |
| richards_super                   | 39.2 ms                                                | 34.1 ms: 1.15x faster                                                  |
| comprehensions                   | 12.0 us                                                | 10.5 us: 1.14x faster                                                  |
| 2to3                             | 179 ms                                                 | 157 ms: 1.13x faster                                                   |
| xml_etree_generate               | 57.1 ms                                                | 51.0 ms: 1.12x faster                                                  |
| logging_simple                   | 3.56 us                                                | 3.19 us: 1.12x faster                                                  |
| typing_runtime_protocols         | 101 us                                                 | 90.5 us: 1.11x faster                                                  |
| pyflate                          | 352 ms                                                 | 317 ms: 1.11x faster                                                   |
| logging_format                   | 3.85 us                                                | 3.47 us: 1.11x faster                                                  |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 413 ms: 1.11x faster                                                   |
| async_generators                 | 294 ms                                                 | 264 ms: 1.11x faster                                                   |
| pickle_pure_python               | 215 us                                                 | 194 us: 1.11x faster                                                   |
| nbody                            | 73.6 ms                                                | 66.7 ms: 1.10x faster                                                  |
| sympy_expand                     | 248 ms                                                 | 228 ms: 1.09x faster                                                   |
| thrift                           | 466 us                                                 | 429 us: 1.09x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 414 ms: 1.08x faster                                                   |
| regex_effbot                     | 2.63 ms                                                | 2.45 ms: 1.08x faster                                                  |
| pycparser                        | 701 ms                                                 | 652 ms: 1.07x faster                                                   |
| sympy_str                        | 146 ms                                                 | 136 ms: 1.07x faster                                                   |
| raytrace                         | 181 ms                                                 | 170 ms: 1.07x faster                                                   |
| bench_thread_pool                | 503 us                                                 | 473 us: 1.06x faster                                                   |
| scimark_fft                      | 200 ms                                                 | 188 ms: 1.06x faster                                                   |
| sqlalchemy_imperative            | 6.69 ms                                                | 6.33 ms: 1.06x faster                                                  |
| xml_etree_iterparse              | 74.2 ms                                                | 70.3 ms: 1.06x faster                                                  |
| chaos                            | 41.1 ms                                                | 39.0 ms: 1.05x faster                                                  |
| connected_components             | 319 ms                                                 | 303 ms: 1.05x faster                                                   |
| shortest_path                    | 345 ms                                                 | 329 ms: 1.05x faster                                                   |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 355 ms: 1.05x faster                                                   |
| k_core                           | 1.61 sec                                               | 1.54 sec: 1.05x faster                                                 |
| xml_etree_parse                  | 108 ms                                                 | 103 ms: 1.05x faster                                                   |
| sphinx                           | 602 ms                                                 | 575 ms: 1.05x faster                                                   |
| bench_mp_pool                    | 64.7 ms                                                | 61.8 ms: 1.05x faster                                                  |
| python_startup                   | 18.8 ms                                                | 18.0 ms: 1.04x faster                                                  |
| bpe_tokeniser                    | 3.26 sec                                               | 3.13 sec: 1.04x faster                                                 |
| telco                            | 4.84 ms                                                | 4.65 ms: 1.04x faster                                                  |
| sympy_sum                        | 75.1 ms                                                | 72.3 ms: 1.04x faster                                                  |
| scimark_lu                       | 75.9 ms                                                | 73.2 ms: 1.04x faster                                                  |
| sympy_integrate                  | 11.3 ms                                                | 10.9 ms: 1.04x faster                                                  |
| sqlalchemy_declarative           | 59.0 ms                                                | 57.0 ms: 1.03x faster                                                  |
| nqueens                          | 61.8 ms                                                | 60.0 ms: 1.03x faster                                                  |
| mako                             | 7.75 ms                                                | 7.56 ms: 1.02x faster                                                  |
| meteor_contest                   | 74.0 ms                                                | 72.5 ms: 1.02x faster                                                  |
| django_template                  | 20.5 ms                                                | 20.1 ms: 1.02x faster                                                  |
| sqlite_synth                     | 1.55 us                                                | 1.54 us: 1.01x faster                                                  |
| mdp                              | 1.50 sec                                               | 1.48 sec: 1.01x faster                                                 |
| dask                             | 771 ms                                                 | 765 ms: 1.01x faster                                                   |
| pathlib                          | 23.2 ms                                                | 23.1 ms: 1.01x faster                                                  |
| spectral_norm                    | 76.5 ms                                                | 76.6 ms: 1.00x slower                                                  |
| fannkuch                         | 279 ms                                                 | 281 ms: 1.01x slower                                                   |
| crypto_pyaes                     | 55.3 ms                                                | 55.9 ms: 1.01x slower                                                  |
| regex_v8                         | 17.0 ms                                                | 17.4 ms: 1.02x slower                                                  |
| pidigits                         | 284 ms                                                 | 290 ms: 1.02x slower                                                   |
| regex_dna                        | 149 ms                                                 | 153 ms: 1.03x slower                                                   |
| asyncio_websockets               | 242 ms                                                 | 250 ms: 1.03x slower                                                   |
| json                             | 3.04 ms                                                | 3.18 ms: 1.04x slower                                                  |
| json_loads                       | 17.0 us                                                | 18.3 us: 1.08x slower                                                  |
| many_optionals                   | 409 us                                                 | 441 us: 1.08x slower                                                   |
| gc_traversal                     | 2.94 ms                                                | 3.20 ms: 1.09x slower                                                  |
| create_gc_cycles                 | 1.19 ms                                                | 1.33 ms: 1.11x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 392 ms: 1.13x slower                                                   |
| json_dumps                       | 6.47 ms                                                | 7.44 ms: 1.15x slower                                                  |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 168 ms: 1.22x slower                                                   |
| subparsers                       | 9.44 ms                                                | 12.0 ms: 1.27x slower                                                  |
| async_tree_eager_tg              | 47.4 ms                                                | 124 ms: 2.62x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.10x faster                                                           |

Benchmark hidden because not significant (4): docutils, scimark_sparse_mat_mult, python_startup_no_site, coverage
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250315-3.14.0a6+-e82c2ca-CLANG/bm-20250315-darwin-arm64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.099x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.05x