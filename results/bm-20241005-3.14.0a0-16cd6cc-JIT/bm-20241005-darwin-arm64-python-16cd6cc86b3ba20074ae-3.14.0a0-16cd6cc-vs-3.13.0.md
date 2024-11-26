# Results vs. 3.13.0

- fork: python
- ref: 16cd6cc86b3ba20074ae
- machine: darwin-arm64
- commit hash: 16cd6cc
- commit date: 2024-10-05
- overall geometric mean: 1.047x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.47x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 187 ms                                                 | 181 ms: 1.04x faster                                                  |
| docutils       | 1.44 sec                                               | 1.60 sec: 1.11x slower                                                |
| html5lib       | 36.6 ms                                                | 34.2 ms: 1.07x faster                                                 |
| Geometric mean | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| coroutines                       | 19.8 ms                                                | 16.2 ms: 1.22x faster                                                 |
| async_tree_eager_tg              | 47.8 ms                                                | 41.6 ms: 1.15x faster                                                 |
| async_tree_memoization_tg        | 288 ms                                                 | 260 ms: 1.11x faster                                                  |
| async_tree_eager                 | 70.1 ms                                                | 63.5 ms: 1.10x faster                                                 |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 126 ms: 1.09x faster                                                  |
| async_tree_none                  | 215 ms                                                 | 201 ms: 1.07x faster                                                  |
| async_tree_memoization           | 268 ms                                                 | 251 ms: 1.07x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 158 ms: 1.06x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 187 ms: 1.06x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 335 ms: 1.03x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 364 ms: 1.02x faster                                                  |
| async_generators                 | 295 ms                                                 | 291 ms: 1.01x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 458 ms: 1.02x slower                                                  |
| async_tree_io                    | 507 ms                                                 | 583 ms: 1.15x slower                                                  |
| async_tree_io_tg                 | 497 ms                                                 | 573 ms: 1.15x slower                                                  |
| async_tree_eager_io              | 514 ms                                                 | 677 ms: 1.32x slower                                                  |
| async_tree_eager_io_tg           | 477 ms                                                 | 701 ms: 1.47x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.00x slower                                                          |

Benchmark hidden because not significant (2): asyncio_websockets, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 56.0 ms                                                | 46.7 ms: 1.20x faster                                                 |
| nbody          | 74.0 ms                                                | 63.6 ms: 1.16x faster                                                 |
| pidigits       | 284 ms                                                 | 283 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.12x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 78.6 ms                                                | 76.0 ms: 1.03x faster                                                 |
| regex_v8       | 17.0 ms                                                | 16.9 ms: 1.00x faster                                                 |
| regex_dna      | 149 ms                                                 | 149 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                                          |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| unpickle_pure_python | 164 us                                                 | 130 us: 1.26x faster                                                  |
| tomli_loads          | 1.57 sec                                               | 1.26 sec: 1.25x faster                                                |
| pickle_pure_python   | 214 us                                                 | 176 us: 1.22x faster                                                  |
| xml_etree_process    | 41.0 ms                                                | 34.6 ms: 1.18x faster                                                 |
| xml_etree_generate   | 57.0 ms                                                | 50.1 ms: 1.14x faster                                                 |
| json_dumps           | 6.52 ms                                                | 6.14 ms: 1.06x faster                                                 |
| xml_etree_iterparse  | 73.6 ms                                                | 70.7 ms: 1.04x faster                                                 |
| xml_etree_parse      | 107 ms                                                 | 104 ms: 1.03x faster                                                  |
| json_loads           | 17.0 us                                                | 16.5 us: 1.03x faster                                                 |
| Geometric mean       | (ref)                                                  | 1.13x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 18.9 ms                                                | 18.2 ms: 1.04x faster                                                 |
| python_startup_no_site | 14.5 ms                                                | 15.2 ms: 1.05x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 7.68 ms                                                | 6.39 ms: 1.20x faster                                                 |
| genshi_text     | 16.9 ms                                                | 17.2 ms: 1.02x slower                                                 |
| django_template | 22.2 ms                                                | 23.4 ms: 1.05x slower                                                 |
| genshi_xml      | 34.4 ms                                                | 42.7 ms: 1.24x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.03x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo                    | 27.4 us                                                | 16.5 us: 1.65x faster                                                 |
| deepcopy                         | 237 us                                                 | 157 us: 1.50x faster                                                  |
| deepcopy_reduce                  | 2.07 us                                                | 1.52 us: 1.36x faster                                                 |
| create_gc_cycles                 | 1.17 ms                                                | 899 us: 1.30x faster                                                  |
| unpickle_pure_python             | 164 us                                                 | 130 us: 1.26x faster                                                  |
| tomli_loads                      | 1.57 sec                                               | 1.26 sec: 1.25x faster                                                |
| generators                       | 31.5 ms                                                | 25.4 ms: 1.24x faster                                                 |
| pickle_pure_python               | 214 us                                                 | 176 us: 1.22x faster                                                  |
| bench_mp_pool                    | 62.5 ms                                                | 51.4 ms: 1.22x faster                                                 |
| coroutines                       | 19.8 ms                                                | 16.2 ms: 1.22x faster                                                 |
| scimark_sor                      | 105 ms                                                 | 87.3 ms: 1.21x faster                                                 |
| mako                             | 7.68 ms                                                | 6.39 ms: 1.20x faster                                                 |
| float                            | 56.0 ms                                                | 46.7 ms: 1.20x faster                                                 |
| scimark_lu                       | 76.7 ms                                                | 64.0 ms: 1.20x faster                                                 |
| xml_etree_process                | 41.0 ms                                                | 34.6 ms: 1.18x faster                                                 |
| gc_traversal                     | 2.91 ms                                                | 2.47 ms: 1.18x faster                                                 |
| logging_simple                   | 3.60 us                                                | 3.08 us: 1.17x faster                                                 |
| nbody                            | 74.0 ms                                                | 63.6 ms: 1.16x faster                                                 |
| logging_format                   | 3.89 us                                                | 3.35 us: 1.16x faster                                                 |
| logging_silent                   | 70.1 ns                                                | 60.7 ns: 1.16x faster                                                 |
| async_tree_eager_tg              | 47.8 ms                                                | 41.6 ms: 1.15x faster                                                 |
| go                               | 115 ms                                                 | 101 ms: 1.14x faster                                                  |
| spectral_norm                    | 76.3 ms                                                | 67.0 ms: 1.14x faster                                                 |
| xml_etree_generate               | 57.0 ms                                                | 50.1 ms: 1.14x faster                                                 |
| thrift                           | 466 us                                                 | 419 us: 1.11x faster                                                  |
| deltablue                        | 2.68 ms                                                | 2.41 ms: 1.11x faster                                                 |
| async_tree_memoization_tg        | 288 ms                                                 | 260 ms: 1.11x faster                                                  |
| async_tree_eager                 | 70.1 ms                                                | 63.5 ms: 1.10x faster                                                 |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 126 ms: 1.09x faster                                                  |
| pyflate                          | 351 ms                                                 | 323 ms: 1.09x faster                                                  |
| scimark_fft                      | 201 ms                                                 | 184 ms: 1.09x faster                                                  |
| fannkuch                         | 284 ms                                                 | 265 ms: 1.07x faster                                                  |
| async_tree_none                  | 215 ms                                                 | 201 ms: 1.07x faster                                                  |
| pprint_pformat                   | 1.08 sec                                               | 1.01 sec: 1.07x faster                                                |
| html5lib                         | 36.6 ms                                                | 34.2 ms: 1.07x faster                                                 |
| async_tree_memoization           | 268 ms                                                 | 251 ms: 1.07x faster                                                  |
| pprint_safe_repr                 | 533 ms                                                 | 501 ms: 1.07x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 158 ms: 1.06x faster                                                  |
| json_dumps                       | 6.52 ms                                                | 6.14 ms: 1.06x faster                                                 |
| async_tree_none_tg               | 198 ms                                                 | 187 ms: 1.06x faster                                                  |
| telco                            | 4.76 ms                                                | 4.49 ms: 1.06x faster                                                 |
| nqueens                          | 62.5 ms                                                | 59.0 ms: 1.06x faster                                                 |
| typing_runtime_protocols         | 101 us                                                 | 95.5 us: 1.06x faster                                                 |
| bpe_tokeniser                    | 3.25 sec                                               | 3.07 sec: 1.06x faster                                                |
| pathlib                          | 23.4 ms                                                | 22.2 ms: 1.05x faster                                                 |
| scimark_monte_carlo              | 50.4 ms                                                | 47.8 ms: 1.05x faster                                                 |
| json                             | 3.03 ms                                                | 2.88 ms: 1.05x faster                                                 |
| bench_thread_pool                | 505 us                                                 | 482 us: 1.05x faster                                                  |
| coverage                         | 46.0 ms                                                | 44.0 ms: 1.05x faster                                                 |
| xml_etree_iterparse              | 73.6 ms                                                | 70.7 ms: 1.04x faster                                                 |
| python_startup                   | 18.9 ms                                                | 18.2 ms: 1.04x faster                                                 |
| pycparser                        | 705 ms                                                 | 679 ms: 1.04x faster                                                  |
| 2to3                             | 187 ms                                                 | 181 ms: 1.04x faster                                                  |
| crypto_pyaes                     | 54.2 ms                                                | 52.3 ms: 1.04x faster                                                 |
| hexiom                           | 4.86 ms                                                | 4.70 ms: 1.03x faster                                                 |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 335 ms: 1.03x faster                                                  |
| regex_compile                    | 78.6 ms                                                | 76.0 ms: 1.03x faster                                                 |
| xml_etree_parse                  | 107 ms                                                 | 104 ms: 1.03x faster                                                  |
| json_loads                       | 17.0 us                                                | 16.5 us: 1.03x faster                                                 |
| raytrace                         | 181 ms                                                 | 177 ms: 1.02x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 364 ms: 1.02x faster                                                  |
| chaos                            | 41.2 ms                                                | 40.5 ms: 1.02x faster                                                 |
| async_generators                 | 295 ms                                                 | 291 ms: 1.01x faster                                                  |
| sqlglot_parse                    | 856 us                                                 | 848 us: 1.01x faster                                                  |
| mdp                              | 1.49 sec                                               | 1.48 sec: 1.01x faster                                                |
| regex_v8                         | 17.0 ms                                                | 16.9 ms: 1.00x faster                                                 |
| sqlglot_normalize                | 189 ms                                                 | 188 ms: 1.00x faster                                                  |
| pidigits                         | 284 ms                                                 | 283 ms: 1.00x faster                                                  |
| regex_dna                        | 149 ms                                                 | 149 ms: 1.00x faster                                                  |
| meteor_contest                   | 74.0 ms                                                | 75.1 ms: 1.02x slower                                                 |
| genshi_text                      | 16.9 ms                                                | 17.2 ms: 1.02x slower                                                 |
| dulwich_log                      | 28.5 ms                                                | 29.0 ms: 1.02x slower                                                 |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 458 ms: 1.02x slower                                                  |
| sqlglot_transpile                | 1.02 ms                                                | 1.05 ms: 1.02x slower                                                 |
| sympy_str                        | 145 ms                                                 | 150 ms: 1.03x slower                                                  |
| sympy_sum                        | 75.4 ms                                                | 78.9 ms: 1.05x slower                                                 |
| comprehensions                   | 12.3 us                                                | 12.9 us: 1.05x slower                                                 |
| django_template                  | 22.2 ms                                                | 23.4 ms: 1.05x slower                                                 |
| python_startup_no_site           | 14.5 ms                                                | 15.2 ms: 1.05x slower                                                 |
| sqlglot_optimize                 | 34.9 ms                                                | 37.8 ms: 1.08x slower                                                 |
| docutils                         | 1.44 sec                                               | 1.60 sec: 1.11x slower                                                |
| sympy_integrate                  | 11.3 ms                                                | 12.6 ms: 1.12x slower                                                 |
| async_tree_io                    | 507 ms                                                 | 583 ms: 1.15x slower                                                  |
| async_tree_io_tg                 | 497 ms                                                 | 573 ms: 1.15x slower                                                  |
| pylint                           | 180 ms                                                 | 214 ms: 1.19x slower                                                  |
| richards_super                   | 39.1 ms                                                | 46.6 ms: 1.19x slower                                                 |
| genshi_xml                       | 34.4 ms                                                | 42.7 ms: 1.24x slower                                                 |
| richards                         | 35.2 ms                                                | 45.2 ms: 1.29x slower                                                 |
| async_tree_eager_io              | 514 ms                                                 | 677 ms: 1.32x slower                                                  |
| async_tree_eager_io_tg           | 477 ms                                                 | 701 ms: 1.47x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.05x faster                                                          |

Benchmark hidden because not significant (6): tornado_http, sympy_expand, scimark_sparse_mat_mult, asyncio_websockets, async_tree_cpu_io_mixed, regex_effbot
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, dask, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20241005-3.14.0a0-16cd6cc-JIT/bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.047x faster
# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.47x