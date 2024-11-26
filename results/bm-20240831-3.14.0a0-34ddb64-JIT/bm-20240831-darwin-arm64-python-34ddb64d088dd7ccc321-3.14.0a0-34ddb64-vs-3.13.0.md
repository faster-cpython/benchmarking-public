# Results vs. 3.13.0

- fork: python
- ref: 34ddb64d088dd7ccc321
- machine: darwin-arm64
- commit hash: 34ddb64
- commit date: 2024-08-31
- overall geometric mean: 1.041x faster
- HPT reliability: 99.34%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.66x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 187 ms                                                 | 180 ms: 1.04x faster                                                  |
| docutils       | 1.44 sec                                               | 1.61 sec: 1.12x slower                                                |
| html5lib       | 36.6 ms                                                | 32.8 ms: 1.11x faster                                                 |
| Geometric mean | (ref)                                                  | 1.03x slower                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| coroutines                       | 19.8 ms                                                | 16.1 ms: 1.23x faster                                                 |
| async_tree_memoization_tg        | 288 ms                                                 | 245 ms: 1.17x faster                                                  |
| async_tree_eager_tg              | 47.8 ms                                                | 41.8 ms: 1.14x faster                                                 |
| async_tree_none                  | 215 ms                                                 | 194 ms: 1.11x faster                                                  |
| async_tree_eager                 | 70.1 ms                                                | 63.3 ms: 1.11x faster                                                 |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 125 ms: 1.10x faster                                                  |
| async_tree_memoization           | 268 ms                                                 | 250 ms: 1.07x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 160 ms: 1.06x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 338 ms: 1.03x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 365 ms: 1.02x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 463 ms: 1.03x slower                                                  |
| async_tree_io_tg                 | 497 ms                                                 | 553 ms: 1.11x slower                                                  |
| async_tree_io                    | 507 ms                                                 | 594 ms: 1.17x slower                                                  |
| async_tree_eager_io              | 514 ms                                                 | 681 ms: 1.32x slower                                                  |
| async_tree_eager_io_tg           | 477 ms                                                 | 718 ms: 1.50x slower                                                  |
| asyncio_websockets               | 242 ms                                                 | 409 ms: 1.69x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.03x slower                                                          |

Benchmark hidden because not significant (3): async_generators, async_tree_cpu_io_mixed, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 56.0 ms                                                | 46.4 ms: 1.21x faster                                                 |
| nbody          | 74.0 ms                                                | 63.8 ms: 1.16x faster                                                 |
| pidigits       | 284 ms                                                 | 282 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.12x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.47 ms: 1.06x faster                                                 |
| regex_compile  | 78.6 ms                                                | 74.9 ms: 1.05x faster                                                 |
| regex_dna      | 149 ms                                                 | 145 ms: 1.03x faster                                                  |
| regex_v8       | 17.0 ms                                                | 16.6 ms: 1.02x faster                                                 |
| Geometric mean | (ref)                                                  | 1.04x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 1.57 sec                                               | 1.24 sec: 1.27x faster                                                |
| unpickle_pure_python | 164 us                                                 | 133 us: 1.24x faster                                                  |
| pickle_pure_python   | 214 us                                                 | 177 us: 1.21x faster                                                  |
| xml_etree_process    | 41.0 ms                                                | 34.6 ms: 1.19x faster                                                 |
| xml_etree_generate   | 57.0 ms                                                | 50.7 ms: 1.12x faster                                                 |
| json_dumps           | 6.52 ms                                                | 6.28 ms: 1.04x faster                                                 |
| xml_etree_iterparse  | 73.6 ms                                                | 71.9 ms: 1.02x faster                                                 |
| json_loads           | 17.0 us                                                | 17.3 us: 1.02x slower                                                 |
| xml_etree_parse      | 107 ms                                                 | 110 ms: 1.02x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.11x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 18.9 ms                                                | 16.8 ms: 1.12x faster                                                 |
| python_startup_no_site | 14.5 ms                                                | 13.9 ms: 1.04x faster                                                 |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 7.68 ms                                                | 6.47 ms: 1.19x faster                                                 |
| django_template | 22.2 ms                                                | 22.1 ms: 1.00x faster                                                 |
| genshi_text     | 16.9 ms                                                | 16.8 ms: 1.00x faster                                                 |
| genshi_xml      | 34.4 ms                                                | 41.2 ms: 1.20x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.00x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo                    | 27.4 us                                                | 16.1 us: 1.70x faster                                                 |
| deepcopy                         | 237 us                                                 | 154 us: 1.54x faster                                                  |
| deepcopy_reduce                  | 2.07 us                                                | 1.49 us: 1.39x faster                                                 |
| create_gc_cycles                 | 1.17 ms                                                | 904 us: 1.29x faster                                                  |
| generators                       | 31.5 ms                                                | 24.6 ms: 1.28x faster                                                 |
| tomli_loads                      | 1.57 sec                                               | 1.24 sec: 1.27x faster                                                |
| unpickle_pure_python             | 164 us                                                 | 133 us: 1.24x faster                                                  |
| coroutines                       | 19.8 ms                                                | 16.1 ms: 1.23x faster                                                 |
| bench_mp_pool                    | 62.5 ms                                                | 51.6 ms: 1.21x faster                                                 |
| pickle_pure_python               | 214 us                                                 | 177 us: 1.21x faster                                                  |
| float                            | 56.0 ms                                                | 46.4 ms: 1.21x faster                                                 |
| logging_simple                   | 3.60 us                                                | 3.03 us: 1.19x faster                                                 |
| scimark_sor                      | 105 ms                                                 | 88.7 ms: 1.19x faster                                                 |
| mako                             | 7.68 ms                                                | 6.47 ms: 1.19x faster                                                 |
| xml_etree_process                | 41.0 ms                                                | 34.6 ms: 1.19x faster                                                 |
| gc_traversal                     | 2.91 ms                                                | 2.46 ms: 1.18x faster                                                 |
| async_tree_memoization_tg        | 288 ms                                                 | 245 ms: 1.17x faster                                                  |
| logging_format                   | 3.89 us                                                | 3.34 us: 1.17x faster                                                 |
| scimark_lu                       | 76.7 ms                                                | 65.7 ms: 1.17x faster                                                 |
| nbody                            | 74.0 ms                                                | 63.8 ms: 1.16x faster                                                 |
| async_tree_eager_tg              | 47.8 ms                                                | 41.8 ms: 1.14x faster                                                 |
| go                               | 115 ms                                                 | 102 ms: 1.13x faster                                                  |
| logging_silent                   | 70.1 ns                                                | 62.4 ns: 1.12x faster                                                 |
| xml_etree_generate               | 57.0 ms                                                | 50.7 ms: 1.12x faster                                                 |
| python_startup                   | 18.9 ms                                                | 16.8 ms: 1.12x faster                                                 |
| deltablue                        | 2.68 ms                                                | 2.39 ms: 1.12x faster                                                 |
| spectral_norm                    | 76.3 ms                                                | 68.3 ms: 1.12x faster                                                 |
| html5lib                         | 36.6 ms                                                | 32.8 ms: 1.11x faster                                                 |
| async_tree_none                  | 215 ms                                                 | 194 ms: 1.11x faster                                                  |
| async_tree_eager                 | 70.1 ms                                                | 63.3 ms: 1.11x faster                                                 |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 125 ms: 1.10x faster                                                  |
| thrift                           | 466 us                                                 | 427 us: 1.09x faster                                                  |
| fannkuch                         | 284 ms                                                 | 264 ms: 1.08x faster                                                  |
| async_tree_memoization           | 268 ms                                                 | 250 ms: 1.07x faster                                                  |
| pyflate                          | 351 ms                                                 | 328 ms: 1.07x faster                                                  |
| typing_runtime_protocols         | 101 us                                                 | 95.0 us: 1.06x faster                                                 |
| bench_thread_pool                | 505 us                                                 | 474 us: 1.06x faster                                                  |
| regex_effbot                     | 2.63 ms                                                | 2.47 ms: 1.06x faster                                                 |
| async_tree_eager_memoization     | 168 ms                                                 | 160 ms: 1.06x faster                                                  |
| nqueens                          | 62.5 ms                                                | 59.5 ms: 1.05x faster                                                 |
| regex_compile                    | 78.6 ms                                                | 74.9 ms: 1.05x faster                                                 |
| bpe_tokeniser                    | 3.25 sec                                               | 3.10 sec: 1.05x faster                                                |
| scimark_fft                      | 201 ms                                                 | 191 ms: 1.05x faster                                                  |
| 2to3                             | 187 ms                                                 | 180 ms: 1.04x faster                                                  |
| pprint_safe_repr                 | 533 ms                                                 | 511 ms: 1.04x faster                                                  |
| pprint_pformat                   | 1.08 sec                                               | 1.04 sec: 1.04x faster                                                |
| crypto_pyaes                     | 54.2 ms                                                | 52.1 ms: 1.04x faster                                                 |
| raytrace                         | 181 ms                                                 | 174 ms: 1.04x faster                                                  |
| json_dumps                       | 6.52 ms                                                | 6.28 ms: 1.04x faster                                                 |
| python_startup_no_site           | 14.5 ms                                                | 13.9 ms: 1.04x faster                                                 |
| scimark_monte_carlo              | 50.4 ms                                                | 48.6 ms: 1.04x faster                                                 |
| pycparser                        | 705 ms                                                 | 681 ms: 1.04x faster                                                  |
| regex_dna                        | 149 ms                                                 | 145 ms: 1.03x faster                                                  |
| json                             | 3.03 ms                                                | 2.94 ms: 1.03x faster                                                 |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 338 ms: 1.03x faster                                                  |
| sqlglot_normalize                | 189 ms                                                 | 184 ms: 1.02x faster                                                  |
| xml_etree_iterparse              | 73.6 ms                                                | 71.9 ms: 1.02x faster                                                 |
| regex_v8                         | 17.0 ms                                                | 16.6 ms: 1.02x faster                                                 |
| chaos                            | 41.2 ms                                                | 40.4 ms: 1.02x faster                                                 |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 365 ms: 1.02x faster                                                  |
| coverage                         | 46.0 ms                                                | 45.2 ms: 1.02x faster                                                 |
| hexiom                           | 4.86 ms                                                | 4.78 ms: 1.02x faster                                                 |
| pidigits                         | 284 ms                                                 | 282 ms: 1.01x faster                                                  |
| django_template                  | 22.2 ms                                                | 22.1 ms: 1.00x faster                                                 |
| genshi_text                      | 16.9 ms                                                | 16.8 ms: 1.00x faster                                                 |
| meteor_contest                   | 74.0 ms                                                | 73.8 ms: 1.00x faster                                                 |
| sympy_sum                        | 75.4 ms                                                | 76.4 ms: 1.01x slower                                                 |
| sympy_expand                     | 246 ms                                                 | 250 ms: 1.02x slower                                                  |
| telco                            | 4.76 ms                                                | 4.85 ms: 1.02x slower                                                 |
| dulwich_log                      | 28.5 ms                                                | 29.1 ms: 1.02x slower                                                 |
| json_loads                       | 17.0 us                                                | 17.3 us: 1.02x slower                                                 |
| xml_etree_parse                  | 107 ms                                                 | 110 ms: 1.02x slower                                                  |
| sqlglot_transpile                | 1.02 ms                                                | 1.05 ms: 1.03x slower                                                 |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 3.07 ms: 1.03x slower                                                 |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 463 ms: 1.03x slower                                                  |
| sqlglot_optimize                 | 34.9 ms                                                | 36.2 ms: 1.04x slower                                                 |
| comprehensions                   | 12.3 us                                                | 12.8 us: 1.04x slower                                                 |
| mdp                              | 1.49 sec                                               | 1.57 sec: 1.05x slower                                                |
| sympy_integrate                  | 11.3 ms                                                | 11.9 ms: 1.05x slower                                                 |
| async_tree_io_tg                 | 497 ms                                                 | 553 ms: 1.11x slower                                                  |
| docutils                         | 1.44 sec                                               | 1.61 sec: 1.12x slower                                                |
| pylint                           | 180 ms                                                 | 207 ms: 1.15x slower                                                  |
| async_tree_io                    | 507 ms                                                 | 594 ms: 1.17x slower                                                  |
| genshi_xml                       | 34.4 ms                                                | 41.2 ms: 1.20x slower                                                 |
| richards_super                   | 39.1 ms                                                | 49.7 ms: 1.27x slower                                                 |
| async_tree_eager_io              | 514 ms                                                 | 681 ms: 1.32x slower                                                  |
| richards                         | 35.2 ms                                                | 47.7 ms: 1.36x slower                                                 |
| async_tree_eager_io_tg           | 477 ms                                                 | 718 ms: 1.50x slower                                                  |
| asyncio_websockets               | 242 ms                                                 | 409 ms: 1.69x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.04x faster                                                          |

Benchmark hidden because not significant (7): sympy_str, async_generators, async_tree_cpu_io_mixed, sqlglot_parse, pathlib, async_tree_none_tg, tornado_http
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, dask, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (2) of results/bm-20240831-3.14.0a0-34ddb64-JIT/bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json: asyncio_tcp, asyncio_tcp_ssl

- Geometric mean (including insignificant results): 1.041x faster
# HPT report

- Reliability score: 99.34% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.66x