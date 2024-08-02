# Results vs. 3.12.0

- fork: python
- ref: caf6064a1bc15ac344af
- machine: darwin-arm64
- commit hash: caf6064
- commit date: 2024-05-18
- overall geometric mean: 1.05x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.01x faster
- Memory change: 0.77x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 192 ms: 1.13x slower                                                  |
| chameleon      | 4.70 ms                                                | 4.45 ms: 1.06x faster                                                 |
| docutils       | 1.50 sec                                               | 1.52 sec: 1.01x slower                                                |
| Geometric mean | (ref)                                                  | 1.01x slower                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 323 ms                                                 | 242 ms: 1.33x faster                                                  |
| async_tree_none_tg         | 258 ms                                                 | 200 ms: 1.29x faster                                                  |
| async_tree_none            | 266 ms                                                 | 212 ms: 1.25x faster                                                  |
| async_tree_memoization     | 312 ms                                                 | 261 ms: 1.20x faster                                                  |
| async_tree_io              | 668 ms                                                 | 567 ms: 1.18x faster                                                  |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 453 ms: 1.18x faster                                                  |
| async_tree_io_tg           | 669 ms                                                 | 572 ms: 1.17x faster                                                  |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 470 ms: 1.12x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.21x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 47.5 ms: 1.18x faster                                                 |
| nbody          | 68.8 ms                                                | 63.5 ms: 1.08x faster                                                 |
| Geometric mean | (ref)                                                  | 1.08x faster                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 77.9 ms                                                | 72.5 ms: 1.07x faster                                                 |
| regex_dna      | 154 ms                                                 | 149 ms: 1.03x faster                                                  |
| regex_effbot   | 2.64 ms                                                | 2.58 ms: 1.02x faster                                                 |
| regex_v8       | 16.0 ms                                                | 17.4 ms: 1.09x slower                                                 |
| Geometric mean | (ref)                                                  | 1.01x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 200 us                                                 | 172 us: 1.16x faster                                                  |
| unpickle_pure_python | 151 us                                                 | 131 us: 1.15x faster                                                  |
| xml_etree_process    | 39.7 ms                                                | 35.3 ms: 1.12x faster                                                 |
| tomli_loads          | 1.39 sec                                               | 1.25 sec: 1.12x faster                                                |
| xml_etree_generate   | 55.8 ms                                                | 50.8 ms: 1.10x faster                                                 |
| unpickle_list        | 3.02 us                                                | 2.89 us: 1.05x faster                                                 |
| xml_etree_parse      | 106 ms                                                 | 102 ms: 1.04x faster                                                  |
| xml_etree_iterparse  | 74.0 ms                                                | 71.1 ms: 1.04x faster                                                 |
| json_dumps           | 6.22 ms                                                | 6.10 ms: 1.02x faster                                                 |
| json_loads           | 17.2 us                                                | 17.1 us: 1.01x faster                                                 |
| pickle_dict          | 18.1 us                                                | 18.2 us: 1.01x slower                                                 |
| pickle_list          | 2.89 us                                                | 2.92 us: 1.01x slower                                                 |
| unpickle             | 9.12 us                                                | 9.39 us: 1.03x slower                                                 |
| pickle               | 7.23 us                                                | 7.48 us: 1.03x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 11.4 ms                                                | 15.3 ms: 1.34x slower                                                 |
| python_startup_no_site | 9.37 ms                                                | 12.8 ms: 1.37x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.35x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 7.71 ms                                                | 6.38 ms: 1.21x faster                                                 |
| django_template | 22.3 ms                                                | 21.0 ms: 1.06x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.13x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| generators                 | 31.1 ms                                                | 23.2 ms: 1.34x faster                                                 |
| async_tree_memoization_tg  | 323 ms                                                 | 242 ms: 1.33x faster                                                  |
| raytrace                   | 212 ms                                                 | 161 ms: 1.32x faster                                                  |
| async_tree_none_tg         | 258 ms                                                 | 200 ms: 1.29x faster                                                  |
| deepcopy_memo              | 27.7 us                                                | 21.5 us: 1.29x faster                                                 |
| async_tree_none            | 266 ms                                                 | 212 ms: 1.25x faster                                                  |
| logging_silent             | 76.4 ns                                                | 62.1 ns: 1.23x faster                                                 |
| logging_simple             | 3.69 us                                                | 3.03 us: 1.21x faster                                                 |
| mako                       | 7.71 ms                                                | 6.38 ms: 1.21x faster                                                 |
| coroutines                 | 19.2 ms                                                | 15.9 ms: 1.21x faster                                                 |
| logging_format             | 3.98 us                                                | 3.31 us: 1.20x faster                                                 |
| async_tree_memoization     | 312 ms                                                 | 261 ms: 1.20x faster                                                  |
| comprehensions             | 14.5 us                                                | 12.3 us: 1.18x faster                                                 |
| async_tree_io              | 668 ms                                                 | 567 ms: 1.18x faster                                                  |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 453 ms: 1.18x faster                                                  |
| float                      | 55.8 ms                                                | 47.5 ms: 1.18x faster                                                 |
| async_tree_io_tg           | 669 ms                                                 | 572 ms: 1.17x faster                                                  |
| pickle_pure_python         | 200 us                                                 | 172 us: 1.16x faster                                                  |
| unpickle_pure_python       | 151 us                                                 | 131 us: 1.15x faster                                                  |
| deepcopy                   | 235 us                                                 | 204 us: 1.15x faster                                                  |
| deepcopy_reduce            | 2.07 us                                                | 1.81 us: 1.15x faster                                                 |
| spectral_norm              | 76.4 ms                                                | 67.2 ms: 1.14x faster                                                 |
| xml_etree_process          | 39.7 ms                                                | 35.3 ms: 1.12x faster                                                 |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 470 ms: 1.12x faster                                                  |
| tomli_loads                | 1.39 sec                                               | 1.25 sec: 1.12x faster                                                |
| xml_etree_generate         | 55.8 ms                                                | 50.8 ms: 1.10x faster                                                 |
| deltablue                  | 2.71 ms                                                | 2.48 ms: 1.09x faster                                                 |
| nqueens                    | 62.4 ms                                                | 57.4 ms: 1.09x faster                                                 |
| chaos                      | 42.5 ms                                                | 39.2 ms: 1.09x faster                                                 |
| nbody                      | 68.8 ms                                                | 63.5 ms: 1.08x faster                                                 |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 2.90 ms: 1.08x faster                                                 |
| regex_compile              | 77.9 ms                                                | 72.5 ms: 1.07x faster                                                 |
| sympy_sum                  | 77.6 ms                                                | 72.3 ms: 1.07x faster                                                 |
| sympy_str                  | 148 ms                                                 | 138 ms: 1.07x faster                                                  |
| pprint_safe_repr           | 497 ms                                                 | 466 ms: 1.07x faster                                                  |
| pathlib                    | 24.2 ms                                                | 22.7 ms: 1.07x faster                                                 |
| django_template            | 22.3 ms                                                | 21.0 ms: 1.06x faster                                                 |
| scimark_fft                | 195 ms                                                 | 184 ms: 1.06x faster                                                  |
| pprint_pformat             | 1.01 sec                                               | 955 ms: 1.06x faster                                                  |
| fannkuch                   | 248 ms                                                 | 235 ms: 1.06x faster                                                  |
| chameleon                  | 4.70 ms                                                | 4.45 ms: 1.06x faster                                                 |
| json                       | 3.09 ms                                                | 2.94 ms: 1.05x faster                                                 |
| bench_thread_pool          | 504 us                                                 | 482 us: 1.05x faster                                                  |
| unpickle_list              | 3.02 us                                                | 2.89 us: 1.05x faster                                                 |
| sympy_integrate            | 11.4 ms                                                | 10.9 ms: 1.04x faster                                                 |
| xml_etree_parse            | 106 ms                                                 | 102 ms: 1.04x faster                                                  |
| xml_etree_iterparse        | 74.0 ms                                                | 71.1 ms: 1.04x faster                                                 |
| sqlglot_optimize           | 34.0 ms                                                | 33.0 ms: 1.03x faster                                                 |
| async_generators           | 304 ms                                                 | 294 ms: 1.03x faster                                                  |
| regex_dna                  | 154 ms                                                 | 149 ms: 1.03x faster                                                  |
| hexiom                     | 4.54 ms                                                | 4.43 ms: 1.03x faster                                                 |
| regex_effbot               | 2.64 ms                                                | 2.58 ms: 1.02x faster                                                 |
| json_dumps                 | 6.22 ms                                                | 6.10 ms: 1.02x faster                                                 |
| sympy_expand               | 241 ms                                                 | 237 ms: 1.02x faster                                                  |
| sqlglot_parse              | 848 us                                                 | 833 us: 1.02x faster                                                  |
| scimark_monte_carlo        | 45.0 ms                                                | 44.3 ms: 1.02x faster                                                 |
| sqlglot_transpile          | 1.02 ms                                                | 1.01 ms: 1.01x faster                                                 |
| json_loads                 | 17.2 us                                                | 17.1 us: 1.01x faster                                                 |
| pycparser                  | 677 ms                                                 | 671 ms: 1.01x faster                                                  |
| pyflate                    | 316 ms                                                 | 314 ms: 1.01x faster                                                  |
| richards                   | 32.1 ms                                                | 32.2 ms: 1.00x slower                                                 |
| richards_super             | 36.0 ms                                                | 36.2 ms: 1.00x slower                                                 |
| docutils                   | 1.50 sec                                               | 1.52 sec: 1.01x slower                                                |
| meteor_contest             | 71.7 ms                                                | 72.5 ms: 1.01x slower                                                 |
| pickle_dict                | 18.1 us                                                | 18.2 us: 1.01x slower                                                 |
| pickle_list                | 2.89 us                                                | 2.92 us: 1.01x slower                                                 |
| go                         | 102 ms                                                 | 103 ms: 1.02x slower                                                  |
| mdp                        | 1.58 sec                                               | 1.62 sec: 1.03x slower                                                |
| unpickle                   | 9.12 us                                                | 9.39 us: 1.03x slower                                                 |
| scimark_lu                 | 76.0 ms                                                | 78.6 ms: 1.03x slower                                                 |
| pickle                     | 7.23 us                                                | 7.48 us: 1.03x slower                                                 |
| asyncio_tcp_ssl            | 1.24 sec                                               | 1.29 sec: 1.04x slower                                                |
| gc_traversal               | 2.40 ms                                                | 2.61 ms: 1.09x slower                                                 |
| regex_v8                   | 16.0 ms                                                | 17.4 ms: 1.09x slower                                                 |
| bench_mp_pool              | 44.9 ms                                                | 49.0 ms: 1.09x slower                                                 |
| 2to3                       | 169 ms                                                 | 192 ms: 1.13x slower                                                  |
| scimark_sor                | 87.4 ms                                                | 99.9 ms: 1.14x slower                                                 |
| coverage                   | 38.9 ms                                                | 45.7 ms: 1.18x slower                                                 |
| telco                      | 3.68 ms                                                | 4.65 ms: 1.26x slower                                                 |
| create_gc_cycles           | 701 us                                                 | 920 us: 1.31x slower                                                  |
| python_startup             | 11.4 ms                                                | 15.3 ms: 1.34x slower                                                 |
| python_startup_no_site     | 9.37 ms                                                | 12.8 ms: 1.37x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.05x faster                                                          |

Benchmark hidden because not significant (8): asyncio_tcp, tornado_http, typing_runtime_protocols, sqlite_synth, pidigits, asyncio_websockets, crypto_pyaes, dask
Ignored benchmarks (8) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, dulwich_log, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, unpack_sequence
Ignored benchmarks (14) of results/bm-20240518-3.14.0a0-caf6064-JIT/bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 0.77x