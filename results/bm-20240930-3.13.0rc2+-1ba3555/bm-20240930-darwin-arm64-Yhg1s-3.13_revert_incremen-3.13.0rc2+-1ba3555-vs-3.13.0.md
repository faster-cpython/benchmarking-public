# Results vs. 3.13.0

- fork: Yhg1s
- ref: 3.13_revert_incremen
- machine: darwin-arm64
- commit hash: 1ba3555
- commit date: 2024-09-30
- overall geometric mean: 1.042x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 0.39x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240930-darwin-arm64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 187 ms                                                 | 174 ms: 1.08x faster                                                   |
| chameleon      | 5.08 ms                                                | 4.75 ms: 1.07x faster                                                  |
| docutils       | 1.44 sec                                               | 1.43 sec: 1.01x faster                                                 |
| html5lib       | 36.6 ms                                                | 34.7 ms: 1.05x faster                                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                                           |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240930-darwin-arm64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| coroutines                       | 19.8 ms                                                | 18.5 ms: 1.07x faster                                                  |
| async_tree_eager_tg              | 47.8 ms                                                | 45.4 ms: 1.05x faster                                                  |
| async_tree_eager                 | 70.1 ms                                                | 67.6 ms: 1.04x faster                                                  |
| async_tree_none                  | 215 ms                                                 | 210 ms: 1.03x faster                                                   |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 135 ms: 1.03x faster                                                   |
| async_tree_eager_memoization     | 168 ms                                                 | 165 ms: 1.02x faster                                                   |
| async_tree_none_tg               | 198 ms                                                 | 194 ms: 1.02x faster                                                   |
| async_tree_eager_io_tg           | 477 ms                                                 | 469 ms: 1.02x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 442 ms: 1.01x faster                                                   |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 454 ms: 1.01x faster                                                   |
| async_tree_memoization_tg        | 288 ms                                                 | 285 ms: 1.01x faster                                                   |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 344 ms: 1.01x faster                                                   |
| asyncio_websockets               | 242 ms                                                 | 408 ms: 1.69x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.01x slower                                                           |

Benchmark hidden because not significant (6): async_tree_memoization, async_tree_eager_io, async_tree_io, async_tree_io_tg, async_tree_eager_cpu_io_mixed, async_generators

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240930-darwin-arm64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 56.0 ms                                                | 54.6 ms: 1.03x faster                                                  |
| pidigits       | 284 ms                                                 | 282 ms: 1.00x faster                                                   |
| nbody          | 74.0 ms                                                | 75.1 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240930-darwin-arm64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 78.6 ms                                                | 76.1 ms: 1.03x faster                                                  |
| regex_effbot   | 2.63 ms                                                | 2.58 ms: 1.02x faster                                                  |
| regex_v8       | 17.0 ms                                                | 17.4 ms: 1.02x slower                                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                                           |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240930-darwin-arm64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 214 us                                                 | 203 us: 1.06x faster                                                   |
| unpickle_pure_python | 164 us                                                 | 156 us: 1.06x faster                                                   |
| tomli_loads          | 1.57 sec                                               | 1.52 sec: 1.03x faster                                                 |
| xml_etree_generate   | 57.0 ms                                                | 56.3 ms: 1.01x faster                                                  |
| json_loads           | 17.0 us                                                | 16.9 us: 1.01x faster                                                  |
| xml_etree_process    | 41.0 ms                                                | 40.8 ms: 1.01x faster                                                  |
| json_dumps           | 6.52 ms                                                | 6.56 ms: 1.01x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                           |

Benchmark hidden because not significant (2): xml_etree_parse, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240930-darwin-arm64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 18.9 ms                                                | 16.7 ms: 1.13x faster                                                  |
| python_startup_no_site | 14.5 ms                                                | 13.2 ms: 1.10x faster                                                  |
| Geometric mean         | (ref)                                                  | 1.11x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240930-darwin-arm64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 15.7 ms: 1.08x faster                                                  |
| genshi_xml      | 34.4 ms                                                | 32.7 ms: 1.05x faster                                                  |
| mako            | 7.68 ms                                                | 7.54 ms: 1.02x faster                                                  |
| django_template | 22.2 ms                                                | 22.1 ms: 1.01x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.04x faster                                                           |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240930-darwin-arm64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| dask                             | 790 ms                                                 | 230 ms: 3.43x faster                                                   |
| create_gc_cycles                 | 1.17 ms                                                | 808 us: 1.45x faster                                                   |
| mypy2                            | 701 ms                                                 | 484 ms: 1.45x faster                                                   |
| generators                       | 31.5 ms                                                | 25.4 ms: 1.24x faster                                                  |
| bench_mp_pool                    | 62.5 ms                                                | 50.7 ms: 1.23x faster                                                  |
| gc_traversal                     | 2.91 ms                                                | 2.46 ms: 1.18x faster                                                  |
| python_startup                   | 18.9 ms                                                | 16.7 ms: 1.13x faster                                                  |
| python_startup_no_site           | 14.5 ms                                                | 13.2 ms: 1.10x faster                                                  |
| deltablue                        | 2.68 ms                                                | 2.46 ms: 1.09x faster                                                  |
| genshi_text                      | 16.9 ms                                                | 15.7 ms: 1.08x faster                                                  |
| 2to3                             | 187 ms                                                 | 174 ms: 1.08x faster                                                   |
| chameleon                        | 5.08 ms                                                | 4.75 ms: 1.07x faster                                                  |
| coroutines                       | 19.8 ms                                                | 18.5 ms: 1.07x faster                                                  |
| fannkuch                         | 284 ms                                                 | 267 ms: 1.06x faster                                                   |
| scimark_monte_carlo              | 50.4 ms                                                | 47.7 ms: 1.06x faster                                                  |
| deepcopy_memo                    | 27.4 us                                                | 25.9 us: 1.06x faster                                                  |
| pickle_pure_python               | 214 us                                                 | 203 us: 1.06x faster                                                   |
| unpickle_pure_python             | 164 us                                                 | 156 us: 1.06x faster                                                   |
| html5lib                         | 36.6 ms                                                | 34.7 ms: 1.05x faster                                                  |
| bench_thread_pool                | 505 us                                                 | 479 us: 1.05x faster                                                   |
| async_tree_eager_tg              | 47.8 ms                                                | 45.4 ms: 1.05x faster                                                  |
| spectral_norm                    | 76.3 ms                                                | 72.5 ms: 1.05x faster                                                  |
| nqueens                          | 62.5 ms                                                | 59.6 ms: 1.05x faster                                                  |
| genshi_xml                       | 34.4 ms                                                | 32.7 ms: 1.05x faster                                                  |
| raytrace                         | 181 ms                                                 | 173 ms: 1.04x faster                                                   |
| go                               | 115 ms                                                 | 110 ms: 1.04x faster                                                   |
| logging_simple                   | 3.60 us                                                | 3.47 us: 1.04x faster                                                  |
| chaos                            | 41.2 ms                                                | 39.6 ms: 1.04x faster                                                  |
| logging_format                   | 3.89 us                                                | 3.75 us: 1.04x faster                                                  |
| deepcopy                         | 237 us                                                 | 228 us: 1.04x faster                                                   |
| async_tree_eager                 | 70.1 ms                                                | 67.6 ms: 1.04x faster                                                  |
| hexiom                           | 4.86 ms                                                | 4.70 ms: 1.04x faster                                                  |
| tomli_loads                      | 1.57 sec                                               | 1.52 sec: 1.03x faster                                                 |
| pprint_safe_repr                 | 533 ms                                                 | 516 ms: 1.03x faster                                                   |
| regex_compile                    | 78.6 ms                                                | 76.1 ms: 1.03x faster                                                  |
| pyflate                          | 351 ms                                                 | 341 ms: 1.03x faster                                                   |
| pprint_pformat                   | 1.08 sec                                               | 1.05 sec: 1.03x faster                                                 |
| float                            | 56.0 ms                                                | 54.6 ms: 1.03x faster                                                  |
| deepcopy_reduce                  | 2.07 us                                                | 2.02 us: 1.03x faster                                                  |
| async_tree_none                  | 215 ms                                                 | 210 ms: 1.03x faster                                                   |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 135 ms: 1.03x faster                                                   |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 2.92 ms: 1.02x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 165 ms: 1.02x faster                                                   |
| scimark_sor                      | 105 ms                                                 | 103 ms: 1.02x faster                                                   |
| sqlglot_parse                    | 856 us                                                 | 838 us: 1.02x faster                                                   |
| comprehensions                   | 12.3 us                                                | 12.0 us: 1.02x faster                                                  |
| typing_runtime_protocols         | 101 us                                                 | 99.2 us: 1.02x faster                                                  |
| thrift                           | 466 us                                                 | 457 us: 1.02x faster                                                   |
| richards_super                   | 39.1 ms                                                | 38.4 ms: 1.02x faster                                                  |
| regex_effbot                     | 2.63 ms                                                | 2.58 ms: 1.02x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 194 ms: 1.02x faster                                                   |
| scimark_fft                      | 201 ms                                                 | 197 ms: 1.02x faster                                                   |
| async_tree_eager_io_tg           | 477 ms                                                 | 469 ms: 1.02x faster                                                   |
| mako                             | 7.68 ms                                                | 7.54 ms: 1.02x faster                                                  |
| richards                         | 35.2 ms                                                | 34.6 ms: 1.02x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 442 ms: 1.01x faster                                                   |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 454 ms: 1.01x faster                                                   |
| mdp                              | 1.49 sec                                               | 1.47 sec: 1.01x faster                                                 |
| crypto_pyaes                     | 54.2 ms                                                | 53.6 ms: 1.01x faster                                                  |
| pycparser                        | 705 ms                                                 | 698 ms: 1.01x faster                                                   |
| xml_etree_generate               | 57.0 ms                                                | 56.3 ms: 1.01x faster                                                  |
| bpe_tokeniser                    | 3.25 sec                                               | 3.21 sec: 1.01x faster                                                 |
| logging_silent                   | 70.1 ns                                                | 69.5 ns: 1.01x faster                                                  |
| async_tree_memoization_tg        | 288 ms                                                 | 285 ms: 1.01x faster                                                   |
| meteor_contest                   | 74.0 ms                                                | 73.3 ms: 1.01x faster                                                  |
| docutils                         | 1.44 sec                                               | 1.43 sec: 1.01x faster                                                 |
| sqlglot_transpile                | 1.02 ms                                                | 1.01 ms: 1.01x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 344 ms: 1.01x faster                                                   |
| json                             | 3.03 ms                                                | 3.01 ms: 1.01x faster                                                  |
| sympy_str                        | 145 ms                                                 | 144 ms: 1.01x faster                                                   |
| django_template                  | 22.2 ms                                                | 22.1 ms: 1.01x faster                                                  |
| sqlglot_normalize                | 189 ms                                                 | 188 ms: 1.01x faster                                                   |
| sympy_integrate                  | 11.3 ms                                                | 11.2 ms: 1.01x faster                                                  |
| json_loads                       | 17.0 us                                                | 16.9 us: 1.01x faster                                                  |
| xml_etree_process                | 41.0 ms                                                | 40.8 ms: 1.01x faster                                                  |
| pidigits                         | 284 ms                                                 | 282 ms: 1.00x faster                                                   |
| sqlglot_optimize                 | 34.9 ms                                                | 34.8 ms: 1.00x faster                                                  |
| dulwich_log                      | 28.5 ms                                                | 28.6 ms: 1.00x slower                                                  |
| scimark_lu                       | 76.7 ms                                                | 76.9 ms: 1.00x slower                                                  |
| coverage                         | 46.0 ms                                                | 46.1 ms: 1.00x slower                                                  |
| sympy_expand                     | 246 ms                                                 | 247 ms: 1.00x slower                                                   |
| json_dumps                       | 6.52 ms                                                | 6.56 ms: 1.01x slower                                                  |
| nbody                            | 74.0 ms                                                | 75.1 ms: 1.01x slower                                                  |
| regex_v8                         | 17.0 ms                                                | 17.4 ms: 1.02x slower                                                  |
| pathlib                          | 23.4 ms                                                | 24.5 ms: 1.05x slower                                                  |
| asyncio_websockets               | 242 ms                                                 | 408 ms: 1.69x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.04x faster                                                           |

Benchmark hidden because not significant (13): async_tree_memoization, async_tree_eager_io, async_tree_io, pylint, async_tree_io_tg, async_tree_eager_cpu_io_mixed, regex_dna, telco, sympy_sum, xml_etree_parse, async_generators, xml_etree_iterparse, tornado_http
Ignored benchmarks (7) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: connected_components, gevent_hub, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (12) of results/bm-20240930-3.13.0rc2+-1ba3555/bm-20240930-darwin-arm64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-1ba3555.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.042x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 0.39x