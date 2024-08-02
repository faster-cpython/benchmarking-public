# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: warmer_side_exits
- machine: darwin-arm64
- commit hash: 8423e72
- commit date: 2024-07-01
- overall geometric mean: 1.03x slower
- HPT reliability: 99.98%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240701-darwin-arm64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 161 ms                                                     | 181 ms: 1.13x slower                                                     |
| docutils       | 1.44 sec                                                   | 1.52 sec: 1.06x slower                                                   |
| html5lib       | 31.2 ms                                                    | 31.6 ms: 1.01x slower                                                    |
| Geometric mean | (ref)                                                      | 1.05x slower                                                             |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                       | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240701-darwin-arm64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|---------------------------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none_tg              | 198 ms                                                     | 176 ms: 1.12x faster                                                     |
| async_tree_memoization          | 260 ms                                                     | 233 ms: 1.12x faster                                                     |
| async_tree_io_tg                | 565 ms                                                     | 509 ms: 1.11x faster                                                     |
| async_tree_eager_io_tg          | 768 ms                                                     | 698 ms: 1.10x faster                                                     |
| async_tree_none                 | 209 ms                                                     | 194 ms: 1.08x faster                                                     |
| async_tree_io                   | 563 ms                                                     | 529 ms: 1.06x faster                                                     |
| async_tree_cpu_io_mixed         | 467 ms                                                     | 452 ms: 1.03x faster                                                     |
| async_tree_eager_memoization_tg | 126 ms                                                     | 123 ms: 1.02x faster                                                     |
| async_tree_eager_tg             | 41.4 ms                                                    | 41.9 ms: 1.01x slower                                                    |
| async_tree_eager                | 60.3 ms                                                    | 66.0 ms: 1.09x slower                                                    |
| Geometric mean                  | (ref)                                                      | 1.04x faster                                                             |

Benchmark hidden because not significant (6): async_tree_eager_io, async_tree_eager_memoization, async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240701-darwin-arm64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 48.6 ms                                                    | 47.1 ms: 1.03x faster                                                    |
| nbody          | 59.6 ms                                                    | 63.9 ms: 1.07x slower                                                    |
| Geometric mean | (ref)                                                      | 1.01x slower                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240701-darwin-arm64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_dna      | 149 ms                                                     | 150 ms: 1.01x slower                                                     |
| regex_v8       | 17.3 ms                                                    | 17.4 ms: 1.01x slower                                                    |
| regex_compile  | 68.5 ms                                                    | 74.3 ms: 1.08x slower                                                    |
| Geometric mean | (ref)                                                      | 1.02x slower                                                             |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240701-darwin-arm64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|----------------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| tomli_loads          | 1.47 sec                                                   | 1.25 sec: 1.17x faster                                                   |
| unpickle_pure_python | 141 us                                                     | 124 us: 1.14x faster                                                     |
| xml_etree_process    | 37.1 ms                                                    | 36.0 ms: 1.03x faster                                                    |
| pickle_pure_python   | 179 us                                                     | 176 us: 1.02x faster                                                     |
| xml_etree_generate   | 52.7 ms                                                    | 52.0 ms: 1.01x faster                                                    |
| xml_etree_parse      | 106 ms                                                     | 107 ms: 1.02x slower                                                     |
| json_loads           | 16.8 us                                                    | 17.2 us: 1.02x slower                                                    |
| json_dumps           | 6.23 ms                                                    | 6.45 ms: 1.04x slower                                                    |
| Geometric mean       | (ref)                                                      | 1.03x faster                                                             |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240701-darwin-arm64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|------------------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 12.3 ms                                                    | 14.5 ms: 1.18x slower                                                    |
| python_startup         | 15.2 ms                                                    | 21.0 ms: 1.39x slower                                                    |
| Geometric mean         | (ref)                                                      | 1.28x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240701-darwin-arm64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|-----------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 6.99 ms                                                    | 6.50 ms: 1.07x faster                                                    |
| django_template | 19.4 ms                                                    | 21.5 ms: 1.11x slower                                                    |
| genshi_text     | 13.9 ms                                                    | 16.3 ms: 1.17x slower                                                    |
| genshi_xml      | 29.9 ms                                                    | 39.3 ms: 1.31x slower                                                    |
| Geometric mean  | (ref)                                                      | 1.12x slower                                                             |

All benchmarks:
===============

| Benchmark                       | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240701-darwin-arm64-brandtbucher-warmer_side_exits-3.14.0a0-8423e72 |
|---------------------------------|:----------------------------------------------------------:|:------------------------------------------------------------------------:|
| deepcopy                        | 204 us                                                     | 151 us: 1.35x faster                                                     |
| deepcopy_memo                   | 22.6 us                                                    | 17.1 us: 1.32x faster                                                    |
| deepcopy_reduce                 | 1.82 us                                                    | 1.53 us: 1.19x faster                                                    |
| tomli_loads                     | 1.47 sec                                                   | 1.25 sec: 1.17x faster                                                   |
| unpickle_pure_python            | 141 us                                                     | 124 us: 1.14x faster                                                     |
| async_tree_none_tg              | 198 ms                                                     | 176 ms: 1.12x faster                                                     |
| async_tree_memoization          | 260 ms                                                     | 233 ms: 1.12x faster                                                     |
| async_tree_io_tg                | 565 ms                                                     | 509 ms: 1.11x faster                                                     |
| async_tree_eager_io_tg          | 768 ms                                                     | 698 ms: 1.10x faster                                                     |
| richards                        | 31.8 ms                                                    | 29.1 ms: 1.09x faster                                                    |
| richards_super                  | 35.2 ms                                                    | 32.5 ms: 1.08x faster                                                    |
| async_tree_none                 | 209 ms                                                     | 194 ms: 1.08x faster                                                     |
| mako                            | 6.99 ms                                                    | 6.50 ms: 1.07x faster                                                    |
| async_tree_io                   | 563 ms                                                     | 529 ms: 1.06x faster                                                     |
| mdp                             | 1.53 sec                                                   | 1.44 sec: 1.06x faster                                                   |
| async_tree_cpu_io_mixed         | 467 ms                                                     | 452 ms: 1.03x faster                                                     |
| float                           | 48.6 ms                                                    | 47.1 ms: 1.03x faster                                                    |
| xml_etree_process               | 37.1 ms                                                    | 36.0 ms: 1.03x faster                                                    |
| async_tree_eager_memoization_tg | 126 ms                                                     | 123 ms: 1.02x faster                                                     |
| pickle_pure_python              | 179 us                                                     | 176 us: 1.02x faster                                                     |
| telco                           | 4.60 ms                                                    | 4.54 ms: 1.01x faster                                                    |
| xml_etree_generate              | 52.7 ms                                                    | 52.0 ms: 1.01x faster                                                    |
| logging_simple                  | 3.04 us                                                    | 3.05 us: 1.00x slower                                                    |
| regex_dna                       | 149 ms                                                     | 150 ms: 1.01x slower                                                     |
| gc_traversal                    | 2.45 ms                                                    | 2.46 ms: 1.01x slower                                                    |
| pyflate                         | 321 ms                                                     | 323 ms: 1.01x slower                                                     |
| regex_v8                        | 17.3 ms                                                    | 17.4 ms: 1.01x slower                                                    |
| asyncio_tcp_ssl                 | 1.29 sec                                                   | 1.30 sec: 1.01x slower                                                   |
| create_gc_cycles                | 897 us                                                     | 906 us: 1.01x slower                                                     |
| generators                      | 22.9 ms                                                    | 23.1 ms: 1.01x slower                                                    |
| async_tree_eager_tg             | 41.4 ms                                                    | 41.9 ms: 1.01x slower                                                    |
| html5lib                        | 31.2 ms                                                    | 31.6 ms: 1.01x slower                                                    |
| go                              | 101 ms                                                     | 102 ms: 1.02x slower                                                     |
| xml_etree_parse                 | 106 ms                                                     | 107 ms: 1.02x slower                                                     |
| pprint_safe_repr                | 465 ms                                                     | 473 ms: 1.02x slower                                                     |
| coroutines                      | 15.8 ms                                                    | 16.2 ms: 1.02x slower                                                    |
| bpe_tokeniser                   | 3.05 sec                                                   | 3.12 sec: 1.02x slower                                                   |
| logging_format                  | 3.31 us                                                    | 3.39 us: 1.02x slower                                                    |
| json_loads                      | 16.8 us                                                    | 17.2 us: 1.02x slower                                                    |
| meteor_contest                  | 70.3 ms                                                    | 72.2 ms: 1.03x slower                                                    |
| dask                            | 221 ms                                                     | 228 ms: 1.03x slower                                                     |
| pprint_pformat                  | 947 ms                                                     | 976 ms: 1.03x slower                                                     |
| spectral_norm                   | 66.4 ms                                                    | 68.7 ms: 1.04x slower                                                    |
| json_dumps                      | 6.23 ms                                                    | 6.45 ms: 1.04x slower                                                    |
| logging_silent                  | 60.1 ns                                                    | 62.4 ns: 1.04x slower                                                    |
| scimark_monte_carlo             | 42.5 ms                                                    | 44.2 ms: 1.04x slower                                                    |
| coverage                        | 45.0 ms                                                    | 46.9 ms: 1.04x slower                                                    |
| async_generators                | 281 ms                                                     | 295 ms: 1.05x slower                                                     |
| crypto_pyaes                    | 49.5 ms                                                    | 52.0 ms: 1.05x slower                                                    |
| sympy_str                       | 131 ms                                                     | 139 ms: 1.06x slower                                                     |
| scimark_fft                     | 181 ms                                                     | 191 ms: 1.06x slower                                                     |
| docutils                        | 1.44 sec                                                   | 1.52 sec: 1.06x slower                                                   |
| pycparser                       | 632 ms                                                     | 676 ms: 1.07x slower                                                     |
| bench_thread_pool               | 447 us                                                     | 478 us: 1.07x slower                                                     |
| sympy_integrate                 | 10.3 ms                                                    | 11.1 ms: 1.07x slower                                                    |
| nbody                           | 59.6 ms                                                    | 63.9 ms: 1.07x slower                                                    |
| sympy_sum                       | 69.2 ms                                                    | 74.4 ms: 1.08x slower                                                    |
| sympy_expand                    | 226 ms                                                     | 243 ms: 1.08x slower                                                     |
| regex_compile                   | 68.5 ms                                                    | 74.3 ms: 1.08x slower                                                    |
| sqlglot_normalize               | 166 ms                                                     | 180 ms: 1.08x slower                                                     |
| scimark_sor                     | 94.9 ms                                                    | 103 ms: 1.09x slower                                                     |
| sqlglot_optimize                | 30.9 ms                                                    | 33.8 ms: 1.09x slower                                                    |
| async_tree_eager                | 60.3 ms                                                    | 66.0 ms: 1.09x slower                                                    |
| scimark_sparse_mat_mult         | 2.77 ms                                                    | 3.04 ms: 1.10x slower                                                    |
| pylint                          | 170 ms                                                     | 187 ms: 1.10x slower                                                     |
| hexiom                          | 4.06 ms                                                    | 4.48 ms: 1.10x slower                                                    |
| django_template                 | 19.4 ms                                                    | 21.5 ms: 1.11x slower                                                    |
| typing_runtime_protocols        | 87.6 us                                                    | 97.5 us: 1.11x slower                                                    |
| deltablue                       | 2.14 ms                                                    | 2.39 ms: 1.12x slower                                                    |
| asyncio_tcp                     | 402 ms                                                     | 451 ms: 1.12x slower                                                     |
| nqueens                         | 52.2 ms                                                    | 58.6 ms: 1.12x slower                                                    |
| raytrace                        | 147 ms                                                     | 165 ms: 1.12x slower                                                     |
| 2to3                            | 161 ms                                                     | 181 ms: 1.13x slower                                                     |
| sqlglot_transpile               | 891 us                                                     | 1.01 ms: 1.13x slower                                                    |
| sqlglot_parse                   | 732 us                                                     | 833 us: 1.14x slower                                                     |
| chaos                           | 34.0 ms                                                    | 39.8 ms: 1.17x slower                                                    |
| genshi_text                     | 13.9 ms                                                    | 16.3 ms: 1.17x slower                                                    |
| python_startup_no_site          | 12.3 ms                                                    | 14.5 ms: 1.18x slower                                                    |
| comprehensions                  | 10.2 us                                                    | 12.3 us: 1.21x slower                                                    |
| scimark_lu                      | 66.9 ms                                                    | 83.0 ms: 1.24x slower                                                    |
| bench_mp_pool                   | 47.2 ms                                                    | 59.0 ms: 1.25x slower                                                    |
| genshi_xml                      | 29.9 ms                                                    | 39.3 ms: 1.31x slower                                                    |
| python_startup                  | 15.2 ms                                                    | 21.0 ms: 1.39x slower                                                    |
| Geometric mean                  | (ref)                                                      | 1.03x slower                                                             |

Benchmark hidden because not significant (15): async_tree_eager_io, async_tree_eager_memoization, async_tree_cpu_io_mixed_tg, xml_etree_iterparse, async_tree_eager_cpu_io_mixed, thrift, json, pidigits, regex_effbot, asyncio_websockets, async_tree_eager_cpu_io_mixed_tg, fannkuch, pathlib, async_tree_memoization_tg, tornado_http
Ignored benchmarks (12) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.98% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.14x