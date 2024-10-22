# Results vs. 3.12.0

- fork: faster-cpython
- ref: monitoring_branch_ta
- machine: darwin-arm64
- commit hash: dc5a9d5
- commit date: 2024-08-01
- overall geometric mean: 1.08x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 0.68x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240801-darwin-arm64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| docutils       | 1.50 sec                                               | 1.53 sec: 1.02x slower                                                          |
| tornado_http   | 69.3 ms                                                | 66.7 ms: 1.04x faster                                                           |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                    |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240801-darwin-arm64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none_tg         | 258 ms                                                 | 178 ms: 1.45x faster                                                            |
| async_tree_memoization_tg  | 323 ms                                                 | 224 ms: 1.44x faster                                                            |
| async_tree_none            | 266 ms                                                 | 189 ms: 1.41x faster                                                            |
| async_tree_io_tg           | 669 ms                                                 | 498 ms: 1.34x faster                                                            |
| async_tree_memoization     | 312 ms                                                 | 236 ms: 1.32x faster                                                            |
| async_tree_io              | 668 ms                                                 | 538 ms: 1.24x faster                                                            |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 436 ms: 1.22x faster                                                            |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 448 ms: 1.17x faster                                                            |
| Geometric mean             | (ref)                                                  | 1.32x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240801-darwin-arm64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 46.6 ms: 1.20x faster                                                           |
| nbody          | 68.8 ms                                                | 62.9 ms: 1.09x faster                                                           |
| Geometric mean | (ref)                                                  | 1.09x faster                                                                    |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240801-darwin-arm64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 77.9 ms                                                | 72.1 ms: 1.08x faster                                                           |
| regex_dna      | 154 ms                                                 | 149 ms: 1.04x faster                                                            |
| regex_effbot   | 2.64 ms                                                | 2.56 ms: 1.03x faster                                                           |
| regex_v8       | 16.0 ms                                                | 17.2 ms: 1.08x slower                                                           |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240801-darwin-arm64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| unpickle_pure_python | 151 us                                                 | 128 us: 1.17x faster                                                            |
| pickle_pure_python   | 200 us                                                 | 170 us: 1.17x faster                                                            |
| tomli_loads          | 1.39 sec                                               | 1.21 sec: 1.15x faster                                                          |
| xml_etree_process    | 39.7 ms                                                | 34.8 ms: 1.14x faster                                                           |
| xml_etree_generate   | 55.8 ms                                                | 51.1 ms: 1.09x faster                                                           |
| xml_etree_iterparse  | 74.0 ms                                                | 71.2 ms: 1.04x faster                                                           |
| json_loads           | 17.2 us                                                | 17.1 us: 1.01x faster                                                           |
| json_dumps           | 6.22 ms                                                | 6.19 ms: 1.00x faster                                                           |
| xml_etree_parse      | 106 ms                                                 | 108 ms: 1.01x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.08x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240801-darwin-arm64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 11.4 ms                                                | 15.4 ms: 1.35x slower                                                           |
| python_startup_no_site | 9.37 ms                                                | 12.8 ms: 1.37x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.36x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240801-darwin-arm64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 7.71 ms                                                | 6.47 ms: 1.19x faster                                                           |
| django_template | 22.3 ms                                                | 21.4 ms: 1.04x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.12x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240801-darwin-arm64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy_memo              | 27.7 us                                                | 16.8 us: 1.65x faster                                                           |
| deepcopy                   | 235 us                                                 | 154 us: 1.53x faster                                                            |
| async_tree_none_tg         | 258 ms                                                 | 178 ms: 1.45x faster                                                            |
| async_tree_memoization_tg  | 323 ms                                                 | 224 ms: 1.44x faster                                                            |
| async_tree_none            | 266 ms                                                 | 189 ms: 1.41x faster                                                            |
| deepcopy_reduce            | 2.07 us                                                | 1.52 us: 1.36x faster                                                           |
| async_tree_io_tg           | 669 ms                                                 | 498 ms: 1.34x faster                                                            |
| coroutines                 | 19.2 ms                                                | 14.4 ms: 1.33x faster                                                           |
| async_tree_memoization     | 312 ms                                                 | 236 ms: 1.32x faster                                                            |
| raytrace                   | 212 ms                                                 | 161 ms: 1.32x faster                                                            |
| generators                 | 31.1 ms                                                | 24.5 ms: 1.27x faster                                                           |
| logging_simple             | 3.69 us                                                | 2.93 us: 1.26x faster                                                           |
| logging_silent             | 76.4 ns                                                | 61.0 ns: 1.25x faster                                                           |
| deltablue                  | 2.71 ms                                                | 2.17 ms: 1.25x faster                                                           |
| async_tree_io              | 668 ms                                                 | 538 ms: 1.24x faster                                                            |
| logging_format             | 3.98 us                                                | 3.24 us: 1.23x faster                                                           |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 436 ms: 1.22x faster                                                            |
| float                      | 55.8 ms                                                | 46.6 ms: 1.20x faster                                                           |
| mako                       | 7.71 ms                                                | 6.47 ms: 1.19x faster                                                           |
| comprehensions             | 14.5 us                                                | 12.2 us: 1.19x faster                                                           |
| unpickle_pure_python       | 151 us                                                 | 128 us: 1.17x faster                                                            |
| pickle_pure_python         | 200 us                                                 | 170 us: 1.17x faster                                                            |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 448 ms: 1.17x faster                                                            |
| tomli_loads                | 1.39 sec                                               | 1.21 sec: 1.15x faster                                                          |
| xml_etree_process          | 39.7 ms                                                | 34.8 ms: 1.14x faster                                                           |
| spectral_norm              | 76.4 ms                                                | 68.6 ms: 1.11x faster                                                           |
| chaos                      | 42.5 ms                                                | 38.5 ms: 1.10x faster                                                           |
| scimark_sor                | 87.4 ms                                                | 79.6 ms: 1.10x faster                                                           |
| nbody                      | 68.8 ms                                                | 62.9 ms: 1.09x faster                                                           |
| xml_etree_generate         | 55.8 ms                                                | 51.1 ms: 1.09x faster                                                           |
| mdp                        | 1.58 sec                                               | 1.46 sec: 1.08x faster                                                          |
| nqueens                    | 62.4 ms                                                | 57.7 ms: 1.08x faster                                                           |
| go                         | 102 ms                                                 | 94.0 ms: 1.08x faster                                                           |
| regex_compile              | 77.9 ms                                                | 72.1 ms: 1.08x faster                                                           |
| bench_thread_pool          | 504 us                                                 | 469 us: 1.07x faster                                                            |
| richards                   | 32.1 ms                                                | 30.0 ms: 1.07x faster                                                           |
| dulwich_log                | 29.8 ms                                                | 28.0 ms: 1.07x faster                                                           |
| sympy_str                  | 148 ms                                                 | 140 ms: 1.06x faster                                                            |
| sympy_sum                  | 77.6 ms                                                | 73.4 ms: 1.06x faster                                                           |
| json                       | 3.09 ms                                                | 2.92 ms: 1.06x faster                                                           |
| sqlglot_normalize          | 186 ms                                                 | 176 ms: 1.05x faster                                                            |
| richards_super             | 36.0 ms                                                | 34.3 ms: 1.05x faster                                                           |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 3.00 ms: 1.04x faster                                                           |
| django_template            | 22.3 ms                                                | 21.4 ms: 1.04x faster                                                           |
| async_generators           | 304 ms                                                 | 292 ms: 1.04x faster                                                            |
| xml_etree_iterparse        | 74.0 ms                                                | 71.2 ms: 1.04x faster                                                           |
| tornado_http               | 69.3 ms                                                | 66.7 ms: 1.04x faster                                                           |
| regex_dna                  | 154 ms                                                 | 149 ms: 1.04x faster                                                            |
| sqlglot_optimize           | 34.0 ms                                                | 32.9 ms: 1.03x faster                                                           |
| scimark_monte_carlo        | 45.0 ms                                                | 43.5 ms: 1.03x faster                                                           |
| scimark_fft                | 195 ms                                                 | 189 ms: 1.03x faster                                                            |
| regex_effbot               | 2.64 ms                                                | 2.56 ms: 1.03x faster                                                           |
| pathlib                    | 24.2 ms                                                | 23.5 ms: 1.03x faster                                                           |
| pycparser                  | 677 ms                                                 | 662 ms: 1.02x faster                                                            |
| pyflate                    | 316 ms                                                 | 309 ms: 1.02x faster                                                            |
| hexiom                     | 4.54 ms                                                | 4.46 ms: 1.02x faster                                                           |
| sqlglot_parse              | 848 us                                                 | 836 us: 1.01x faster                                                            |
| pprint_safe_repr           | 497 ms                                                 | 491 ms: 1.01x faster                                                            |
| sqlglot_transpile          | 1.02 ms                                                | 1.01 ms: 1.01x faster                                                           |
| typing_runtime_protocols   | 93.0 us                                                | 92.1 us: 1.01x faster                                                           |
| json_loads                 | 17.2 us                                                | 17.1 us: 1.01x faster                                                           |
| pprint_pformat             | 1.01 sec                                               | 1.01 sec: 1.01x faster                                                          |
| json_dumps                 | 6.22 ms                                                | 6.19 ms: 1.00x faster                                                           |
| sympy_integrate            | 11.4 ms                                                | 11.3 ms: 1.00x faster                                                           |
| asyncio_websockets         | 409 ms                                                 | 408 ms: 1.00x faster                                                            |
| sympy_expand               | 241 ms                                                 | 242 ms: 1.01x slower                                                            |
| xml_etree_parse            | 106 ms                                                 | 108 ms: 1.01x slower                                                            |
| docutils                   | 1.50 sec                                               | 1.53 sec: 1.02x slower                                                          |
| fannkuch                   | 248 ms                                                 | 254 ms: 1.02x slower                                                            |
| asyncio_tcp_ssl            | 1.24 sec                                               | 1.27 sec: 1.03x slower                                                          |
| gc_traversal               | 2.40 ms                                                | 2.48 ms: 1.03x slower                                                           |
| scimark_lu                 | 76.0 ms                                                | 79.9 ms: 1.05x slower                                                           |
| regex_v8                   | 16.0 ms                                                | 17.2 ms: 1.08x slower                                                           |
| bench_mp_pool              | 44.9 ms                                                | 50.9 ms: 1.13x slower                                                           |
| coverage                   | 38.9 ms                                                | 45.0 ms: 1.16x slower                                                           |
| telco                      | 3.68 ms                                                | 4.59 ms: 1.25x slower                                                           |
| create_gc_cycles           | 701 us                                                 | 902 us: 1.29x slower                                                            |
| python_startup             | 11.4 ms                                                | 15.4 ms: 1.35x slower                                                           |
| python_startup_no_site     | 9.37 ms                                                | 12.8 ms: 1.37x slower                                                           |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                                    |

Benchmark hidden because not significant (6): asyncio_tcp, dask, crypto_pyaes, meteor_contest, pidigits, 2to3
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (14) of results/bm-20240801-3.14.0a0-dc5a9d5-JIT/bm-20240801-darwin-arm64-faster%2dcpython-monitoring_branch_ta-3.14.0a0-dc5a9d5.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 0.68x