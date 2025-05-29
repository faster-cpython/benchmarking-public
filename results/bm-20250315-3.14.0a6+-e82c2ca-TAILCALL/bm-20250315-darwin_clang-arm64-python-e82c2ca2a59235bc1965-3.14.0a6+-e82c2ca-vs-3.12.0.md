# Results vs. 3.12.0

- fork: python
- ref: e82c2ca2a59235bc1965
- machine: darwin-arm64
- commit hash: e82c2ca
- commit date: 2025-03-15
- overall geometric mean: 1.098x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250315-darwin-arm64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 157 ms: 1.07x faster                                                   |
| docutils       | 1.45 sec                                               | 1.44 sec: 1.01x faster                                                 |
| html5lib       | 33.4 ms                                                | 30.6 ms: 1.09x faster                                                  |
| sphinx         | 613 ms                                                 | 575 ms: 1.07x faster                                                   |
| Geometric mean | (ref)                                                  | 1.06x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250315-darwin-arm64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_eager_io              | 666 ms                                                 | 347 ms: 1.92x faster                                                   |
| async_tree_io                    | 672 ms                                                 | 354 ms: 1.90x faster                                                   |
| async_tree_io_tg                 | 673 ms                                                 | 359 ms: 1.88x faster                                                   |
| async_tree_eager_io_tg           | 617 ms                                                 | 358 ms: 1.72x faster                                                   |
| async_tree_none_tg               | 255 ms                                                 | 149 ms: 1.71x faster                                                   |
| async_tree_none                  | 263 ms                                                 | 156 ms: 1.69x faster                                                   |
| async_tree_memoization_tg        | 318 ms                                                 | 189 ms: 1.69x faster                                                   |
| async_tree_memoization           | 310 ms                                                 | 189 ms: 1.64x faster                                                   |
| coroutines                       | 19.7 ms                                                | 15.2 ms: 1.29x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 414 ms: 1.27x faster                                                   |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 413 ms: 1.27x faster                                                   |
| async_tree_eager_memoization     | 168 ms                                                 | 137 ms: 1.22x faster                                                   |
| async_generators                 | 299 ms                                                 | 264 ms: 1.13x faster                                                   |
| async_tree_eager                 | 65.8 ms                                                | 58.5 ms: 1.13x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 355 ms: 1.05x faster                                                   |
| asyncio_websockets               | 243 ms                                                 | 250 ms: 1.03x slower                                                   |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 392 ms: 1.13x slower                                                   |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 168 ms: 1.19x slower                                                   |
| async_tree_eager_tg              | 46.9 ms                                                | 124 ms: 2.65x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.27x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250315-darwin-arm64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 54.1 ms                                                | 45.8 ms: 1.18x faster                                                  |
| nbody          | 67.6 ms                                                | 66.7 ms: 1.01x faster                                                  |
| pidigits       | 283 ms                                                 | 290 ms: 1.03x slower                                                   |
| Geometric mean | (ref)                                                  | 1.05x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250315-darwin-arm64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 75.9 ms                                                | 65.8 ms: 1.15x faster                                                  |
| regex_effbot   | 2.44 ms                                                | 2.45 ms: 1.00x slower                                                  |
| regex_dna      | 143 ms                                                 | 153 ms: 1.07x slower                                                   |
| regex_v8       | 15.1 ms                                                | 17.4 ms: 1.15x slower                                                  |
| Geometric mean | (ref)                                                  | 1.02x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250315-darwin-arm64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 1.36 sec                                               | 1.21 sec: 1.12x faster                                                 |
| xml_etree_process    | 38.9 ms                                                | 35.5 ms: 1.09x faster                                                  |
| unpickle_pure_python | 145 us                                                 | 134 us: 1.09x faster                                                   |
| xml_etree_generate   | 55.4 ms                                                | 51.0 ms: 1.09x faster                                                  |
| xml_etree_iterparse  | 75.5 ms                                                | 70.3 ms: 1.07x faster                                                  |
| xml_etree_parse      | 108 ms                                                 | 103 ms: 1.05x faster                                                   |
| pickle_pure_python   | 197 us                                                 | 194 us: 1.02x faster                                                   |
| json_loads           | 17.0 us                                                | 18.3 us: 1.08x slower                                                  |
| json_dumps           | 6.19 ms                                                | 7.44 ms: 1.20x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250315-darwin-arm64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 17.8 ms                                                | 18.0 ms: 1.02x slower                                                  |
| python_startup_no_site | 13.2 ms                                                | 13.7 ms: 1.04x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250315-darwin-arm64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 14.7 ms                                                | 13.3 ms: 1.10x faster                                                  |
| genshi_xml      | 30.5 ms                                                | 28.4 ms: 1.08x faster                                                  |
| mako            | 7.44 ms                                                | 7.56 ms: 1.02x slower                                                  |
| django_template | 19.7 ms                                                | 20.1 ms: 1.02x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                           |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250315-darwin-arm64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 12.0 ms: 2.68x faster                                                  |
| async_tree_eager_io              | 666 ms                                                 | 347 ms: 1.92x faster                                                   |
| async_tree_io                    | 672 ms                                                 | 354 ms: 1.90x faster                                                   |
| async_tree_io_tg                 | 673 ms                                                 | 359 ms: 1.88x faster                                                   |
| async_tree_eager_io_tg           | 617 ms                                                 | 358 ms: 1.72x faster                                                   |
| async_tree_none_tg               | 255 ms                                                 | 149 ms: 1.71x faster                                                   |
| async_tree_none                  | 263 ms                                                 | 156 ms: 1.69x faster                                                   |
| async_tree_memoization_tg        | 318 ms                                                 | 189 ms: 1.69x faster                                                   |
| async_tree_memoization           | 310 ms                                                 | 189 ms: 1.64x faster                                                   |
| generators                       | 29.4 ms                                                | 19.0 ms: 1.55x faster                                                  |
| deepcopy                         | 226 us                                                 | 146 us: 1.54x faster                                                   |
| deepcopy_memo                    | 26.0 us                                                | 17.3 us: 1.50x faster                                                  |
| comprehensions                   | 14.0 us                                                | 10.5 us: 1.33x faster                                                  |
| coroutines                       | 19.7 ms                                                | 15.2 ms: 1.29x faster                                                  |
| go                               | 98.5 ms                                                | 76.2 ms: 1.29x faster                                                  |
| deepcopy_reduce                  | 2.01 us                                                | 1.56 us: 1.29x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 414 ms: 1.27x faster                                                   |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 413 ms: 1.27x faster                                                   |
| async_tree_eager_memoization     | 168 ms                                                 | 137 ms: 1.22x faster                                                   |
| logging_silent                   | 72.5 ns                                                | 60.0 ns: 1.21x faster                                                  |
| dulwich_log                      | 29.2 ms                                                | 24.3 ms: 1.21x faster                                                  |
| raytrace                         | 204 ms                                                 | 170 ms: 1.20x faster                                                   |
| float                            | 54.1 ms                                                | 45.8 ms: 1.18x faster                                                  |
| deltablue                        | 2.57 ms                                                | 2.18 ms: 1.18x faster                                                  |
| pylint                           | 182 ms                                                 | 156 ms: 1.17x faster                                                   |
| regex_compile                    | 75.9 ms                                                | 65.8 ms: 1.15x faster                                                  |
| scimark_sor                      | 85.8 ms                                                | 75.1 ms: 1.14x faster                                                  |
| logging_simple                   | 3.60 us                                                | 3.19 us: 1.13x faster                                                  |
| async_generators                 | 299 ms                                                 | 264 ms: 1.13x faster                                                   |
| async_tree_eager                 | 65.8 ms                                                | 58.5 ms: 1.13x faster                                                  |
| logging_format                   | 3.90 us                                                | 3.47 us: 1.12x faster                                                  |
| tomli_loads                      | 1.36 sec                                               | 1.21 sec: 1.12x faster                                                 |
| k_core                           | 1.72 sec                                               | 1.54 sec: 1.12x faster                                                 |
| genshi_text                      | 14.7 ms                                                | 13.3 ms: 1.10x faster                                                  |
| xml_etree_process                | 38.9 ms                                                | 35.5 ms: 1.09x faster                                                  |
| thrift                           | 468 us                                                 | 429 us: 1.09x faster                                                   |
| html5lib                         | 33.4 ms                                                | 30.6 ms: 1.09x faster                                                  |
| hexiom                           | 4.38 ms                                                | 4.02 ms: 1.09x faster                                                  |
| unpickle_pure_python             | 145 us                                                 | 134 us: 1.09x faster                                                   |
| xml_etree_generate               | 55.4 ms                                                | 51.0 ms: 1.09x faster                                                  |
| sqlalchemy_declarative           | 61.9 ms                                                | 57.0 ms: 1.09x faster                                                  |
| scimark_monte_carlo              | 44.5 ms                                                | 41.0 ms: 1.09x faster                                                  |
| genshi_xml                       | 30.5 ms                                                | 28.4 ms: 1.08x faster                                                  |
| xml_etree_iterparse              | 75.5 ms                                                | 70.3 ms: 1.07x faster                                                  |
| pathlib                          | 24.7 ms                                                | 23.1 ms: 1.07x faster                                                  |
| 2to3                             | 168 ms                                                 | 157 ms: 1.07x faster                                                   |
| sphinx                           | 613 ms                                                 | 575 ms: 1.07x faster                                                   |
| chaos                            | 41.6 ms                                                | 39.0 ms: 1.07x faster                                                  |
| sympy_str                        | 144 ms                                                 | 136 ms: 1.06x faster                                                   |
| bench_mp_pool                    | 65.5 ms                                                | 61.8 ms: 1.06x faster                                                  |
| sympy_sum                        | 76.2 ms                                                | 72.3 ms: 1.05x faster                                                  |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 2.99 ms: 1.05x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 355 ms: 1.05x faster                                                   |
| xml_etree_parse                  | 108 ms                                                 | 103 ms: 1.05x faster                                                   |
| bpe_tokeniser                    | 3.28 sec                                               | 3.13 sec: 1.05x faster                                                 |
| pprint_pformat                   | 986 ms                                                 | 942 ms: 1.05x faster                                                   |
| pprint_safe_repr                 | 483 ms                                                 | 463 ms: 1.04x faster                                                   |
| sqlalchemy_imperative            | 6.60 ms                                                | 6.33 ms: 1.04x faster                                                  |
| scimark_fft                      | 194 ms                                                 | 188 ms: 1.03x faster                                                   |
| pycparser                        | 673 ms                                                 | 652 ms: 1.03x faster                                                   |
| sympy_expand                     | 233 ms                                                 | 228 ms: 1.03x faster                                                   |
| bench_thread_pool                | 483 us                                                 | 473 us: 1.02x faster                                                   |
| dask                             | 779 ms                                                 | 765 ms: 1.02x faster                                                   |
| pickle_pure_python               | 197 us                                                 | 194 us: 1.02x faster                                                   |
| sympy_integrate                  | 11.1 ms                                                | 10.9 ms: 1.02x faster                                                  |
| richards_super                   | 34.6 ms                                                | 34.1 ms: 1.01x faster                                                  |
| nbody                            | 67.6 ms                                                | 66.7 ms: 1.01x faster                                                  |
| typing_runtime_protocols         | 91.5 us                                                | 90.5 us: 1.01x faster                                                  |
| docutils                         | 1.45 sec                                               | 1.44 sec: 1.01x faster                                                 |
| richards                         | 30.6 ms                                                | 30.4 ms: 1.01x faster                                                  |
| mdp                              | 1.49 sec                                               | 1.48 sec: 1.01x faster                                                 |
| sqlite_synth                     | 1.55 us                                                | 1.54 us: 1.01x faster                                                  |
| scimark_lu                       | 73.5 ms                                                | 73.2 ms: 1.00x faster                                                  |
| regex_effbot                     | 2.44 ms                                                | 2.45 ms: 1.00x slower                                                  |
| nqueens                          | 59.5 ms                                                | 60.0 ms: 1.01x slower                                                  |
| connected_components             | 300 ms                                                 | 303 ms: 1.01x slower                                                   |
| mako                             | 7.44 ms                                                | 7.56 ms: 1.02x slower                                                  |
| python_startup                   | 17.8 ms                                                | 18.0 ms: 1.02x slower                                                  |
| pyflate                          | 311 ms                                                 | 317 ms: 1.02x slower                                                   |
| django_template                  | 19.7 ms                                                | 20.1 ms: 1.02x slower                                                  |
| pidigits                         | 283 ms                                                 | 290 ms: 1.03x slower                                                   |
| asyncio_websockets               | 243 ms                                                 | 250 ms: 1.03x slower                                                   |
| python_startup_no_site           | 13.2 ms                                                | 13.7 ms: 1.04x slower                                                  |
| meteor_contest                   | 69.1 ms                                                | 72.5 ms: 1.05x slower                                                  |
| json                             | 3.00 ms                                                | 3.18 ms: 1.06x slower                                                  |
| regex_dna                        | 143 ms                                                 | 153 ms: 1.07x slower                                                   |
| json_loads                       | 17.0 us                                                | 18.3 us: 1.08x slower                                                  |
| gc_traversal                     | 2.95 ms                                                | 3.20 ms: 1.08x slower                                                  |
| crypto_pyaes                     | 51.4 ms                                                | 55.9 ms: 1.09x slower                                                  |
| many_optionals                   | 403 us                                                 | 441 us: 1.10x slower                                                   |
| fannkuch                         | 250 ms                                                 | 281 ms: 1.12x slower                                                   |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 392 ms: 1.13x slower                                                   |
| regex_v8                         | 15.1 ms                                                | 17.4 ms: 1.15x slower                                                  |
| create_gc_cycles                 | 1.15 ms                                                | 1.33 ms: 1.15x slower                                                  |
| telco                            | 3.92 ms                                                | 4.65 ms: 1.19x slower                                                  |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 168 ms: 1.19x slower                                                   |
| json_dumps                       | 6.19 ms                                                | 7.44 ms: 1.20x slower                                                  |
| coverage                         | 38.5 ms                                                | 46.4 ms: 1.21x slower                                                  |
| async_tree_eager_tg              | 46.9 ms                                                | 124 ms: 2.65x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.10x faster                                                           |

Benchmark hidden because not significant (2): shortest_path, spectral_norm
Ignored benchmarks (9) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250315-3.14.0a6+-e82c2ca-CLANG/bm-20250315-darwin-arm64-python-e82c2ca2a59235bc1965-3.14.0a6+-e82c2ca.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.098x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.07x