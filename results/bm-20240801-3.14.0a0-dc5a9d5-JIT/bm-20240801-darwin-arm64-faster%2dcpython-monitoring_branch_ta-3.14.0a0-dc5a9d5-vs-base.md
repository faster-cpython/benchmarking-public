# Results vs. base

- fork: faster-cpython
- ref: monitoring_branch_ta
- machine: darwin-arm64
- commit hash: dc5a9d5
- commit date: 2024-08-01
- overall geometric mean: 1.01x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240801-darwin-arm64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 | bm-20240801-darwin-arm64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 173 ms                                                                | 170 ms: 1.02x faster                                                            |
| docutils       | 1.54 sec                                                              | 1.53 sec: 1.00x faster                                                          |
| html5lib       | 31.0 ms                                                               | 29.4 ms: 1.05x faster                                                           |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                                    |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20240801-darwin-arm64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 | bm-20240801-darwin-arm64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| coroutines                       | 16.1 ms                                                               | 14.4 ms: 1.12x faster                                                           |
| async_tree_none                  | 194 ms                                                                | 189 ms: 1.03x faster                                                            |
| async_tree_eager_memoization_tg  | 125 ms                                                                | 121 ms: 1.03x faster                                                            |
| async_tree_eager_memoization     | 151 ms                                                                | 147 ms: 1.02x faster                                                            |
| async_tree_none_tg               | 182 ms                                                                | 178 ms: 1.02x faster                                                            |
| async_tree_memoization           | 240 ms                                                                | 236 ms: 1.02x faster                                                            |
| async_tree_eager_tg              | 42.1 ms                                                               | 41.5 ms: 1.01x faster                                                           |
| async_tree_io                    | 546 ms                                                                | 538 ms: 1.01x faster                                                            |
| async_generators                 | 296 ms                                                                | 292 ms: 1.01x faster                                                            |
| async_tree_eager_cpu_io_mixed_tg | 334 ms                                                                | 331 ms: 1.01x faster                                                            |
| async_tree_eager                 | 62.4 ms                                                               | 61.9 ms: 1.01x faster                                                           |
| async_tree_eager_cpu_io_mixed    | 357 ms                                                                | 354 ms: 1.01x faster                                                            |
| Geometric mean                   | (ref)                                                                 | 1.02x faster                                                                    |

Benchmark hidden because not significant (9): async_tree_eager_io, async_tree_eager_io_tg, async_tree_memoization_tg, async_tree_io_tg, async_tree_cpu_io_mixed_tg, asyncio_tcp, async_tree_cpu_io_mixed, asyncio_tcp_ssl, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240801-darwin-arm64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 | bm-20240801-darwin-arm64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 282 ms                                                                | 282 ms: 1.00x faster                                                            |
| nbody          | 62.8 ms                                                               | 62.9 ms: 1.00x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                                    |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240801-darwin-arm64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 | bm-20240801-darwin-arm64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 73.4 ms                                                               | 72.1 ms: 1.02x faster                                                           |
| regex_effbot   | 2.57 ms                                                               | 2.56 ms: 1.00x faster                                                           |
| regex_v8       | 17.2 ms                                                               | 17.2 ms: 1.00x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                                    |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240801-darwin-arm64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 | bm-20240801-darwin-arm64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_process    | 35.7 ms                                                               | 34.8 ms: 1.03x faster                                                           |
| unpickle_pure_python | 131 us                                                                | 128 us: 1.03x faster                                                            |
| tomli_loads          | 1.23 sec                                                              | 1.21 sec: 1.02x faster                                                          |
| pickle_pure_python   | 173 us                                                                | 170 us: 1.02x faster                                                            |
| json_dumps           | 6.29 ms                                                               | 6.19 ms: 1.02x faster                                                           |
| xml_etree_generate   | 51.8 ms                                                               | 51.1 ms: 1.01x faster                                                           |
| json_loads           | 17.2 us                                                               | 17.1 us: 1.00x faster                                                           |
| xml_etree_parse      | 107 ms                                                                | 108 ms: 1.01x slower                                                            |
| Geometric mean       | (ref)                                                                 | 1.01x faster                                                                    |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240801-darwin-arm64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 | bm-20240801-darwin-arm64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 15.5 ms                                                               | 15.4 ms: 1.01x faster                                                           |
| python_startup_no_site | 12.9 ms                                                               | 12.8 ms: 1.01x faster                                                           |
| Geometric mean         | (ref)                                                                 | 1.01x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240801-darwin-arm64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 | bm-20240801-darwin-arm64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 14.7 ms                                                               | 13.7 ms: 1.07x faster                                                           |
| genshi_xml      | 34.5 ms                                                               | 33.3 ms: 1.04x faster                                                           |
| django_template | 21.3 ms                                                               | 21.4 ms: 1.00x slower                                                           |
| Geometric mean  | (ref)                                                                 | 1.02x faster                                                                    |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                        | bm-20240801-darwin-arm64-python-a9d56e38a08ec198a228-3.14.0a0-a9d56e3 | bm-20240801-darwin-arm64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| scimark_sor                      | 102 ms                                                                | 79.6 ms: 1.28x faster                                                           |
| coroutines                       | 16.1 ms                                                               | 14.4 ms: 1.12x faster                                                           |
| go                               | 101 ms                                                                | 94.0 ms: 1.07x faster                                                           |
| genshi_text                      | 14.7 ms                                                               | 13.7 ms: 1.07x faster                                                           |
| deltablue                        | 2.30 ms                                                               | 2.17 ms: 1.06x faster                                                           |
| html5lib                         | 31.0 ms                                                               | 29.4 ms: 1.05x faster                                                           |
| genshi_xml                       | 34.5 ms                                                               | 33.3 ms: 1.04x faster                                                           |
| typing_runtime_protocols         | 95.4 us                                                               | 92.1 us: 1.04x faster                                                           |
| deepcopy_reduce                  | 1.57 us                                                               | 1.52 us: 1.03x faster                                                           |
| async_tree_none                  | 194 ms                                                                | 189 ms: 1.03x faster                                                            |
| async_tree_eager_memoization_tg  | 125 ms                                                                | 121 ms: 1.03x faster                                                            |
| logging_simple                   | 3.01 us                                                               | 2.93 us: 1.03x faster                                                           |
| pprint_safe_repr                 | 504 ms                                                                | 491 ms: 1.03x faster                                                            |
| xml_etree_process                | 35.7 ms                                                               | 34.8 ms: 1.03x faster                                                           |
| unpickle_pure_python             | 131 us                                                                | 128 us: 1.03x faster                                                            |
| scimark_lu                       | 81.9 ms                                                               | 79.9 ms: 1.03x faster                                                           |
| async_tree_eager_memoization     | 151 ms                                                                | 147 ms: 1.02x faster                                                            |
| tomli_loads                      | 1.23 sec                                                              | 1.21 sec: 1.02x faster                                                          |
| logging_format                   | 3.31 us                                                               | 3.24 us: 1.02x faster                                                           |
| async_tree_none_tg               | 182 ms                                                                | 178 ms: 1.02x faster                                                            |
| pprint_pformat                   | 1.02 sec                                                              | 1.01 sec: 1.02x faster                                                          |
| 2to3                             | 173 ms                                                                | 170 ms: 1.02x faster                                                            |
| regex_compile                    | 73.4 ms                                                               | 72.1 ms: 1.02x faster                                                           |
| pickle_pure_python               | 173 us                                                                | 170 us: 1.02x faster                                                            |
| sympy_expand                     | 246 ms                                                                | 242 ms: 1.02x faster                                                            |
| async_tree_memoization           | 240 ms                                                                | 236 ms: 1.02x faster                                                            |
| dask                             | 225 ms                                                                | 221 ms: 1.02x faster                                                            |
| json_dumps                       | 6.29 ms                                                               | 6.19 ms: 1.02x faster                                                           |
| richards                         | 30.5 ms                                                               | 30.0 ms: 1.01x faster                                                           |
| sympy_str                        | 142 ms                                                                | 140 ms: 1.01x faster                                                            |
| async_tree_eager_tg              | 42.1 ms                                                               | 41.5 ms: 1.01x faster                                                           |
| xml_etree_generate               | 51.8 ms                                                               | 51.1 ms: 1.01x faster                                                           |
| async_tree_io                    | 546 ms                                                                | 538 ms: 1.01x faster                                                            |
| sympy_sum                        | 74.4 ms                                                               | 73.4 ms: 1.01x faster                                                           |
| pyflate                          | 313 ms                                                                | 309 ms: 1.01x faster                                                            |
| async_generators                 | 296 ms                                                                | 292 ms: 1.01x faster                                                            |
| dulwich_log                      | 28.3 ms                                                               | 28.0 ms: 1.01x faster                                                           |
| sqlglot_parse                    | 845 us                                                                | 836 us: 1.01x faster                                                            |
| deepcopy                         | 155 us                                                                | 154 us: 1.01x faster                                                            |
| python_startup                   | 15.5 ms                                                               | 15.4 ms: 1.01x faster                                                           |
| async_tree_eager_cpu_io_mixed_tg | 334 ms                                                                | 331 ms: 1.01x faster                                                            |
| async_tree_eager                 | 62.4 ms                                                               | 61.9 ms: 1.01x faster                                                           |
| python_startup_no_site           | 12.9 ms                                                               | 12.8 ms: 1.01x faster                                                           |
| async_tree_eager_cpu_io_mixed    | 357 ms                                                                | 354 ms: 1.01x faster                                                            |
| chaos                            | 38.8 ms                                                               | 38.5 ms: 1.01x faster                                                           |
| sqlglot_optimize                 | 33.1 ms                                                               | 32.9 ms: 1.01x faster                                                           |
| scimark_monte_carlo              | 43.8 ms                                                               | 43.5 ms: 1.01x faster                                                           |
| sqlglot_transpile                | 1.02 ms                                                               | 1.01 ms: 1.01x faster                                                           |
| scimark_fft                      | 190 ms                                                                | 189 ms: 1.00x faster                                                            |
| docutils                         | 1.54 sec                                                              | 1.53 sec: 1.00x faster                                                          |
| sqlglot_normalize                | 177 ms                                                                | 176 ms: 1.00x faster                                                            |
| scimark_sparse_mat_mult          | 3.01 ms                                                               | 3.00 ms: 1.00x faster                                                           |
| json_loads                       | 17.2 us                                                               | 17.1 us: 1.00x faster                                                           |
| regex_effbot                     | 2.57 ms                                                               | 2.56 ms: 1.00x faster                                                           |
| nqueens                          | 57.9 ms                                                               | 57.7 ms: 1.00x faster                                                           |
| raytrace                         | 161 ms                                                                | 161 ms: 1.00x faster                                                            |
| pidigits                         | 282 ms                                                                | 282 ms: 1.00x faster                                                            |
| nbody                            | 62.8 ms                                                               | 62.9 ms: 1.00x slower                                                           |
| hexiom                           | 4.45 ms                                                               | 4.46 ms: 1.00x slower                                                           |
| comprehensions                   | 12.2 us                                                               | 12.2 us: 1.00x slower                                                           |
| sympy_integrate                  | 11.3 ms                                                               | 11.3 ms: 1.00x slower                                                           |
| generators                       | 24.4 ms                                                               | 24.5 ms: 1.00x slower                                                           |
| create_gc_cycles                 | 899 us                                                                | 902 us: 1.00x slower                                                            |
| deepcopy_memo                    | 16.7 us                                                               | 16.8 us: 1.00x slower                                                           |
| regex_v8                         | 17.2 ms                                                               | 17.2 ms: 1.00x slower                                                           |
| coverage                         | 44.8 ms                                                               | 45.0 ms: 1.00x slower                                                           |
| django_template                  | 21.3 ms                                                               | 21.4 ms: 1.00x slower                                                           |
| meteor_contest                   | 71.4 ms                                                               | 71.7 ms: 1.00x slower                                                           |
| thrift                           | 435 us                                                                | 438 us: 1.01x slower                                                            |
| mdp                              | 1.45 sec                                                              | 1.46 sec: 1.01x slower                                                          |
| crypto_pyaes                     | 51.4 ms                                                               | 51.7 ms: 1.01x slower                                                           |
| bpe_tokeniser                    | 3.01 sec                                                              | 3.04 sec: 1.01x slower                                                          |
| xml_etree_parse                  | 107 ms                                                                | 108 ms: 1.01x slower                                                            |
| fannkuch                         | 251 ms                                                                | 254 ms: 1.01x slower                                                            |
| Geometric mean                   | (ref)                                                                 | 1.01x faster                                                                    |

Benchmark hidden because not significant (25): async_tree_eager_io, async_tree_eager_io_tg, async_tree_memoization_tg, async_tree_io_tg, async_tree_cpu_io_mixed_tg, tornado_http, asyncio_tcp, async_tree_cpu_io_mixed, pylint, asyncio_tcp_ssl, pycparser, richards_super, xml_etree_iterparse, json, bench_thread_pool, bench_mp_pool, regex_dna, float, spectral_norm, asyncio_websockets, logging_silent, mako, telco, pathlib, gc_traversal

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x