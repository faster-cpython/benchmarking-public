# Results vs. 3.13.0

- fork: python
- ref: 16cd6cc86b3ba20074ae
- machine: darwin-arm64
- commit hash: 16cd6cc
- commit date: 2024-10-05
- overall geometric mean: 1.103x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 0.71x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 187 ms                                                 | 161 ms: 1.17x faster                                                  |
| docutils       | 1.44 sec                                               | 1.40 sec: 1.03x faster                                                |
| html5lib       | 36.6 ms                                                | 31.9 ms: 1.15x faster                                                 |
| Geometric mean | (ref)                                                  | 1.10x faster                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| coroutines                       | 19.8 ms                                                | 16.4 ms: 1.21x faster                                                 |
| async_tree_eager                 | 70.1 ms                                                | 59.3 ms: 1.18x faster                                                 |
| async_tree_eager_tg              | 47.8 ms                                                | 41.2 ms: 1.16x faster                                                 |
| async_tree_memoization_tg        | 288 ms                                                 | 258 ms: 1.11x faster                                                  |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 124 ms: 1.11x faster                                                  |
| async_tree_none                  | 215 ms                                                 | 197 ms: 1.09x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 154 ms: 1.09x faster                                                  |
| async_tree_memoization           | 268 ms                                                 | 248 ms: 1.08x faster                                                  |
| async_generators                 | 295 ms                                                 | 274 ms: 1.08x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 185 ms: 1.07x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 359 ms: 1.04x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 335 ms: 1.04x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 460 ms: 1.03x slower                                                  |
| async_tree_io_tg                 | 497 ms                                                 | 529 ms: 1.07x slower                                                  |
| async_tree_io                    | 507 ms                                                 | 585 ms: 1.15x slower                                                  |
| async_tree_eager_io              | 514 ms                                                 | 675 ms: 1.31x slower                                                  |
| async_tree_eager_io_tg           | 477 ms                                                 | 700 ms: 1.47x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.02x faster                                                          |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 56.0 ms                                                | 48.8 ms: 1.15x faster                                                 |
| nbody          | 74.0 ms                                                | 65.7 ms: 1.13x faster                                                 |
| pidigits       | 284 ms                                                 | 283 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.09x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 78.6 ms                                                | 67.8 ms: 1.16x faster                                                 |
| regex_v8       | 17.0 ms                                                | 16.4 ms: 1.04x faster                                                 |
| regex_dna      | 149 ms                                                 | 148 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.05x faster                                                          |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 214 us                                                 | 182 us: 1.18x faster                                                  |
| unpickle_pure_python | 164 us                                                 | 140 us: 1.17x faster                                                  |
| xml_etree_process    | 41.0 ms                                                | 37.4 ms: 1.10x faster                                                 |
| xml_etree_generate   | 57.0 ms                                                | 52.3 ms: 1.09x faster                                                 |
| json_dumps           | 6.52 ms                                                | 6.20 ms: 1.05x faster                                                 |
| tomli_loads          | 1.57 sec                                               | 1.51 sec: 1.04x faster                                                |
| json_loads           | 17.0 us                                                | 16.5 us: 1.03x faster                                                 |
| xml_etree_iterparse  | 73.6 ms                                                | 73.1 ms: 1.01x faster                                                 |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                          |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 18.9 ms                                                | 16.3 ms: 1.16x faster                                                 |
| python_startup_no_site | 14.5 ms                                                | 13.3 ms: 1.09x faster                                                 |
| Geometric mean         | (ref)                                                  | 1.12x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 13.6 ms: 1.24x faster                                                 |
| genshi_xml      | 34.4 ms                                                | 29.7 ms: 1.16x faster                                                 |
| django_template | 22.2 ms                                                | 19.7 ms: 1.13x faster                                                 |
| mako            | 7.68 ms                                                | 6.83 ms: 1.12x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.16x faster                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy                         | 237 us                                                 | 144 us: 1.65x faster                                                  |
| deepcopy_memo                    | 27.4 us                                                | 16.7 us: 1.63x faster                                                 |
| generators                       | 31.5 ms                                                | 20.6 ms: 1.53x faster                                                 |
| go                               | 115 ms                                                 | 81.6 ms: 1.41x faster                                                 |
| deepcopy_reduce                  | 2.07 us                                                | 1.50 us: 1.38x faster                                                 |
| create_gc_cycles                 | 1.17 ms                                                | 900 us: 1.30x faster                                                  |
| bench_mp_pool                    | 62.5 ms                                                | 48.6 ms: 1.29x faster                                                 |
| genshi_text                      | 16.9 ms                                                | 13.6 ms: 1.24x faster                                                 |
| deltablue                        | 2.68 ms                                                | 2.22 ms: 1.21x faster                                                 |
| coroutines                       | 19.8 ms                                                | 16.4 ms: 1.21x faster                                                 |
| raytrace                         | 181 ms                                                 | 151 ms: 1.20x faster                                                  |
| nqueens                          | 62.5 ms                                                | 52.2 ms: 1.20x faster                                                 |
| hexiom                           | 4.86 ms                                                | 4.08 ms: 1.19x faster                                                 |
| logging_simple                   | 3.60 us                                                | 3.04 us: 1.19x faster                                                 |
| async_tree_eager                 | 70.1 ms                                                | 59.3 ms: 1.18x faster                                                 |
| pickle_pure_python               | 214 us                                                 | 182 us: 1.18x faster                                                  |
| gc_traversal                     | 2.91 ms                                                | 2.47 ms: 1.18x faster                                                 |
| scimark_lu                       | 76.7 ms                                                | 65.2 ms: 1.18x faster                                                 |
| logging_format                   | 3.89 us                                                | 3.32 us: 1.17x faster                                                 |
| unpickle_pure_python             | 164 us                                                 | 140 us: 1.17x faster                                                  |
| 2to3                             | 187 ms                                                 | 161 ms: 1.17x faster                                                  |
| pprint_safe_repr                 | 533 ms                                                 | 458 ms: 1.16x faster                                                  |
| sqlglot_parse                    | 856 us                                                 | 736 us: 1.16x faster                                                  |
| async_tree_eager_tg              | 47.8 ms                                                | 41.2 ms: 1.16x faster                                                 |
| regex_compile                    | 78.6 ms                                                | 67.8 ms: 1.16x faster                                                 |
| python_startup                   | 18.9 ms                                                | 16.3 ms: 1.16x faster                                                 |
| pprint_pformat                   | 1.08 sec                                               | 936 ms: 1.16x faster                                                  |
| genshi_xml                       | 34.4 ms                                                | 29.7 ms: 1.16x faster                                                 |
| scimark_monte_carlo              | 50.4 ms                                                | 43.7 ms: 1.15x faster                                                 |
| float                            | 56.0 ms                                                | 48.8 ms: 1.15x faster                                                 |
| html5lib                         | 36.6 ms                                                | 31.9 ms: 1.15x faster                                                 |
| chaos                            | 41.2 ms                                                | 36.0 ms: 1.14x faster                                                 |
| logging_silent                   | 70.1 ns                                                | 61.5 ns: 1.14x faster                                                 |
| sqlglot_normalize                | 189 ms                                                 | 166 ms: 1.14x faster                                                  |
| sqlglot_transpile                | 1.02 ms                                                | 899 us: 1.14x faster                                                  |
| sqlglot_optimize                 | 34.9 ms                                                | 30.8 ms: 1.14x faster                                                 |
| django_template                  | 22.2 ms                                                | 19.7 ms: 1.13x faster                                                 |
| nbody                            | 74.0 ms                                                | 65.7 ms: 1.13x faster                                                 |
| mako                             | 7.68 ms                                                | 6.83 ms: 1.12x faster                                                 |
| comprehensions                   | 12.3 us                                                | 10.9 us: 1.12x faster                                                 |
| thrift                           | 466 us                                                 | 416 us: 1.12x faster                                                  |
| richards_super                   | 39.1 ms                                                | 35.0 ms: 1.12x faster                                                 |
| pycparser                        | 705 ms                                                 | 632 ms: 1.12x faster                                                  |
| async_tree_memoization_tg        | 288 ms                                                 | 258 ms: 1.11x faster                                                  |
| richards                         | 35.2 ms                                                | 31.6 ms: 1.11x faster                                                 |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 124 ms: 1.11x faster                                                  |
| bench_thread_pool                | 505 us                                                 | 455 us: 1.11x faster                                                  |
| scimark_sor                      | 105 ms                                                 | 95.5 ms: 1.10x faster                                                 |
| sympy_str                        | 145 ms                                                 | 132 ms: 1.10x faster                                                  |
| sympy_expand                     | 246 ms                                                 | 224 ms: 1.10x faster                                                  |
| xml_etree_process                | 41.0 ms                                                | 37.4 ms: 1.10x faster                                                 |
| sympy_sum                        | 75.4 ms                                                | 68.8 ms: 1.10x faster                                                 |
| async_tree_none                  | 215 ms                                                 | 197 ms: 1.09x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 154 ms: 1.09x faster                                                  |
| typing_runtime_protocols         | 101 us                                                 | 92.8 us: 1.09x faster                                                 |
| pathlib                          | 23.4 ms                                                | 21.4 ms: 1.09x faster                                                 |
| xml_etree_generate               | 57.0 ms                                                | 52.3 ms: 1.09x faster                                                 |
| python_startup_no_site           | 14.5 ms                                                | 13.3 ms: 1.09x faster                                                 |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 2.75 ms: 1.09x faster                                                 |
| spectral_norm                    | 76.3 ms                                                | 70.3 ms: 1.08x faster                                                 |
| async_tree_memoization           | 268 ms                                                 | 248 ms: 1.08x faster                                                  |
| pyflate                          | 351 ms                                                 | 325 ms: 1.08x faster                                                  |
| async_generators                 | 295 ms                                                 | 274 ms: 1.08x faster                                                  |
| fannkuch                         | 284 ms                                                 | 263 ms: 1.08x faster                                                  |
| json                             | 3.03 ms                                                | 2.82 ms: 1.08x faster                                                 |
| scimark_fft                      | 201 ms                                                 | 187 ms: 1.07x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 185 ms: 1.07x faster                                                  |
| crypto_pyaes                     | 54.2 ms                                                | 51.3 ms: 1.06x faster                                                 |
| json_dumps                       | 6.52 ms                                                | 6.20 ms: 1.05x faster                                                 |
| coverage                         | 46.0 ms                                                | 43.7 ms: 1.05x faster                                                 |
| telco                            | 4.76 ms                                                | 4.56 ms: 1.05x faster                                                 |
| dulwich_log                      | 28.5 ms                                                | 27.4 ms: 1.04x faster                                                 |
| mdp                              | 1.49 sec                                               | 1.44 sec: 1.04x faster                                                |
| regex_v8                         | 17.0 ms                                                | 16.4 ms: 1.04x faster                                                 |
| sympy_integrate                  | 11.3 ms                                                | 10.9 ms: 1.04x faster                                                 |
| bpe_tokeniser                    | 3.25 sec                                               | 3.13 sec: 1.04x faster                                                |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 359 ms: 1.04x faster                                                  |
| tomli_loads                      | 1.57 sec                                               | 1.51 sec: 1.04x faster                                                |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 335 ms: 1.04x faster                                                  |
| meteor_contest                   | 74.0 ms                                                | 71.6 ms: 1.03x faster                                                 |
| json_loads                       | 17.0 us                                                | 16.5 us: 1.03x faster                                                 |
| docutils                         | 1.44 sec                                               | 1.40 sec: 1.03x faster                                                |
| regex_dna                        | 149 ms                                                 | 148 ms: 1.01x faster                                                  |
| xml_etree_iterparse              | 73.6 ms                                                | 73.1 ms: 1.01x faster                                                 |
| pidigits                         | 284 ms                                                 | 283 ms: 1.00x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 460 ms: 1.03x slower                                                  |
| async_tree_io_tg                 | 497 ms                                                 | 529 ms: 1.07x slower                                                  |
| async_tree_io                    | 507 ms                                                 | 585 ms: 1.15x slower                                                  |
| async_tree_eager_io              | 514 ms                                                 | 675 ms: 1.31x slower                                                  |
| async_tree_eager_io_tg           | 477 ms                                                 | 700 ms: 1.47x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.11x faster                                                          |

Benchmark hidden because not significant (6): tornado_http, pylint, async_tree_cpu_io_mixed, regex_effbot, asyncio_websockets, xml_etree_parse
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, dask, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20241005-3.14.0a0-16cd6cc/bm-20241005-darwin-arm64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.103x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 0.71x