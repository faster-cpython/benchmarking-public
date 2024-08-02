# Results vs. 3.12.0

- fork: python
- ref: caf6064a1bc15ac344af
- machine: darwin-arm64
- commit hash: caf6064
- commit date: 2024-05-18
- overall geometric mean: 1.08x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 0.54x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 182 ms: 1.07x slower                                                  |
| chameleon      | 4.70 ms                                                | 4.29 ms: 1.10x faster                                                 |
| docutils       | 1.50 sec                                               | 1.44 sec: 1.05x faster                                                |
| tornado_http   | 69.3 ms                                                | 66.2 ms: 1.05x faster                                                 |
| Geometric mean | (ref)                                                  | 1.03x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg  | 323 ms                                                 | 239 ms: 1.35x faster                                                  |
| async_tree_none_tg         | 258 ms                                                 | 197 ms: 1.31x faster                                                  |
| async_tree_none            | 266 ms                                                 | 209 ms: 1.27x faster                                                  |
| async_tree_memoization     | 312 ms                                                 | 258 ms: 1.21x faster                                                  |
| async_tree_io_tg           | 669 ms                                                 | 565 ms: 1.18x faster                                                  |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 451 ms: 1.18x faster                                                  |
| async_tree_io              | 668 ms                                                 | 566 ms: 1.18x faster                                                  |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 468 ms: 1.12x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.22x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 48.2 ms: 1.16x faster                                                 |
| nbody          | 68.8 ms                                                | 60.3 ms: 1.14x faster                                                 |
| pidigits       | 282 ms                                                 | 281 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.10x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 77.9 ms                                                | 68.2 ms: 1.14x faster                                                 |
| regex_dna      | 154 ms                                                 | 149 ms: 1.04x faster                                                  |
| regex_effbot   | 2.64 ms                                                | 2.56 ms: 1.03x faster                                                 |
| regex_v8       | 16.0 ms                                                | 17.3 ms: 1.09x slower                                                 |
| Geometric mean | (ref)                                                  | 1.03x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 200 us                                                 | 178 us: 1.12x faster                                                  |
| unpickle_pure_python | 151 us                                                 | 140 us: 1.08x faster                                                  |
| xml_etree_process    | 39.7 ms                                                | 36.9 ms: 1.07x faster                                                 |
| xml_etree_generate   | 55.8 ms                                                | 52.2 ms: 1.07x faster                                                 |
| unpickle_list        | 3.02 us                                                | 2.90 us: 1.04x faster                                                 |
| xml_etree_iterparse  | 74.0 ms                                                | 71.6 ms: 1.03x faster                                                 |
| xml_etree_parse      | 106 ms                                                 | 104 ms: 1.02x faster                                                  |
| json_loads           | 17.2 us                                                | 16.9 us: 1.02x faster                                                 |
| json_dumps           | 6.22 ms                                                | 6.29 ms: 1.01x slower                                                 |
| pickle_dict          | 18.1 us                                                | 18.3 us: 1.01x slower                                                 |
| unpickle             | 9.12 us                                                | 9.33 us: 1.02x slower                                                 |
| pickle               | 7.23 us                                                | 7.45 us: 1.03x slower                                                 |
| pickle_list          | 2.89 us                                                | 3.00 us: 1.04x slower                                                 |
| tomli_loads          | 1.39 sec                                               | 1.46 sec: 1.05x slower                                                |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 9.37 ms                                                | 11.5 ms: 1.23x slower                                                 |
| python_startup         | 11.4 ms                                                | 14.0 ms: 1.23x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.23x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 22.3 ms                                                | 19.4 ms: 1.15x faster                                                 |
| mako            | 7.71 ms                                                | 6.91 ms: 1.12x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.13x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| raytrace                   | 212 ms                                                 | 147 ms: 1.44x faster                                                  |
| comprehensions             | 14.5 us                                                | 10.7 us: 1.36x faster                                                 |
| generators                 | 31.1 ms                                                | 22.9 ms: 1.36x faster                                                 |
| async_tree_memoization_tg  | 323 ms                                                 | 239 ms: 1.35x faster                                                  |
| async_tree_none_tg         | 258 ms                                                 | 197 ms: 1.31x faster                                                  |
| logging_silent             | 76.4 ns                                                | 60.0 ns: 1.27x faster                                                 |
| async_tree_none            | 266 ms                                                 | 209 ms: 1.27x faster                                                  |
| deltablue                  | 2.71 ms                                                | 2.14 ms: 1.27x faster                                                 |
| chaos                      | 42.5 ms                                                | 34.3 ms: 1.24x faster                                                 |
| deepcopy_memo              | 27.7 us                                                | 22.6 us: 1.22x faster                                                 |
| coroutines                 | 19.2 ms                                                | 15.9 ms: 1.21x faster                                                 |
| async_tree_memoization     | 312 ms                                                 | 258 ms: 1.21x faster                                                  |
| logging_simple             | 3.69 us                                                | 3.07 us: 1.20x faster                                                 |
| logging_format             | 3.98 us                                                | 3.35 us: 1.19x faster                                                 |
| nqueens                    | 62.4 ms                                                | 52.6 ms: 1.19x faster                                                 |
| async_tree_io_tg           | 669 ms                                                 | 565 ms: 1.18x faster                                                  |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 451 ms: 1.18x faster                                                  |
| async_tree_io              | 668 ms                                                 | 566 ms: 1.18x faster                                                  |
| deepcopy                   | 235 us                                                 | 200 us: 1.17x faster                                                  |
| deepcopy_reduce            | 2.07 us                                                | 1.79 us: 1.16x faster                                                 |
| float                      | 55.8 ms                                                | 48.2 ms: 1.16x faster                                                 |
| sqlglot_parse              | 848 us                                                 | 733 us: 1.16x faster                                                  |
| django_template            | 22.3 ms                                                | 19.4 ms: 1.15x faster                                                 |
| sqlglot_transpile          | 1.02 ms                                                | 892 us: 1.14x faster                                                  |
| nbody                      | 68.8 ms                                                | 60.3 ms: 1.14x faster                                                 |
| regex_compile              | 77.9 ms                                                | 68.2 ms: 1.14x faster                                                 |
| spectral_norm              | 76.4 ms                                                | 67.2 ms: 1.14x faster                                                 |
| scimark_lu                 | 76.0 ms                                                | 66.8 ms: 1.14x faster                                                 |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 2.77 ms: 1.13x faster                                                 |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 468 ms: 1.12x faster                                                  |
| pickle_pure_python         | 200 us                                                 | 178 us: 1.12x faster                                                  |
| sympy_str                  | 148 ms                                                 | 132 ms: 1.12x faster                                                  |
| mako                       | 7.71 ms                                                | 6.91 ms: 1.12x faster                                                 |
| sqlglot_normalize          | 186 ms                                                 | 167 ms: 1.12x faster                                                  |
| hexiom                     | 4.54 ms                                                | 4.08 ms: 1.11x faster                                                 |
| sympy_sum                  | 77.6 ms                                                | 69.9 ms: 1.11x faster                                                 |
| sympy_integrate            | 11.4 ms                                                | 10.3 ms: 1.10x faster                                                 |
| sqlglot_optimize           | 34.0 ms                                                | 31.0 ms: 1.10x faster                                                 |
| chameleon                  | 4.70 ms                                                | 4.29 ms: 1.10x faster                                                 |
| bench_thread_pool          | 504 us                                                 | 463 us: 1.09x faster                                                  |
| async_generators           | 304 ms                                                 | 279 ms: 1.09x faster                                                  |
| scimark_fft                | 195 ms                                                 | 180 ms: 1.08x faster                                                  |
| pathlib                    | 24.2 ms                                                | 22.5 ms: 1.08x faster                                                 |
| unpickle_pure_python       | 151 us                                                 | 140 us: 1.08x faster                                                  |
| pprint_safe_repr           | 497 ms                                                 | 462 ms: 1.08x faster                                                  |
| xml_etree_process          | 39.7 ms                                                | 36.9 ms: 1.07x faster                                                 |
| pprint_pformat             | 1.01 sec                                               | 943 ms: 1.07x faster                                                  |
| pycparser                  | 677 ms                                                 | 632 ms: 1.07x faster                                                  |
| xml_etree_generate         | 55.8 ms                                                | 52.2 ms: 1.07x faster                                                 |
| scimark_monte_carlo        | 45.0 ms                                                | 42.2 ms: 1.07x faster                                                 |
| sympy_expand               | 241 ms                                                 | 227 ms: 1.06x faster                                                  |
| mdp                        | 1.58 sec                                               | 1.49 sec: 1.06x faster                                                |
| richards_super             | 36.0 ms                                                | 34.3 ms: 1.05x faster                                                 |
| tornado_http               | 69.3 ms                                                | 66.2 ms: 1.05x faster                                                 |
| docutils                   | 1.50 sec                                               | 1.44 sec: 1.05x faster                                                |
| json                       | 3.09 ms                                                | 2.95 ms: 1.05x faster                                                 |
| crypto_pyaes               | 51.9 ms                                                | 49.6 ms: 1.05x faster                                                 |
| unpickle_list              | 3.02 us                                                | 2.90 us: 1.04x faster                                                 |
| regex_dna                  | 154 ms                                                 | 149 ms: 1.04x faster                                                  |
| xml_etree_iterparse        | 74.0 ms                                                | 71.6 ms: 1.03x faster                                                 |
| richards                   | 32.1 ms                                                | 31.1 ms: 1.03x faster                                                 |
| regex_effbot               | 2.64 ms                                                | 2.56 ms: 1.03x faster                                                 |
| meteor_contest             | 71.7 ms                                                | 69.8 ms: 1.03x faster                                                 |
| xml_etree_parse            | 106 ms                                                 | 104 ms: 1.02x faster                                                  |
| sqlite_synth               | 1.57 us                                                | 1.54 us: 1.02x faster                                                 |
| json_loads                 | 17.2 us                                                | 16.9 us: 1.02x faster                                                 |
| typing_runtime_protocols   | 93.0 us                                                | 91.7 us: 1.01x faster                                                 |
| go                         | 102 ms                                                 | 100 ms: 1.01x faster                                                  |
| asyncio_websockets         | 409 ms                                                 | 408 ms: 1.00x faster                                                  |
| pidigits                   | 282 ms                                                 | 281 ms: 1.00x faster                                                  |
| fannkuch                   | 248 ms                                                 | 249 ms: 1.00x slower                                                  |
| json_dumps                 | 6.22 ms                                                | 6.29 ms: 1.01x slower                                                 |
| pickle_dict                | 18.1 us                                                | 18.3 us: 1.01x slower                                                 |
| pyflate                    | 316 ms                                                 | 320 ms: 1.01x slower                                                  |
| bench_mp_pool              | 44.9 ms                                                | 45.7 ms: 1.02x slower                                                 |
| unpickle                   | 9.12 us                                                | 9.33 us: 1.02x slower                                                 |
| gc_traversal               | 2.40 ms                                                | 2.46 ms: 1.02x slower                                                 |
| asyncio_tcp_ssl            | 1.24 sec                                               | 1.28 sec: 1.03x slower                                                |
| pickle                     | 7.23 us                                                | 7.45 us: 1.03x slower                                                 |
| pickle_list                | 2.89 us                                                | 3.00 us: 1.04x slower                                                 |
| tomli_loads                | 1.39 sec                                               | 1.46 sec: 1.05x slower                                                |
| 2to3                       | 169 ms                                                 | 182 ms: 1.07x slower                                                  |
| scimark_sor                | 87.4 ms                                                | 94.0 ms: 1.08x slower                                                 |
| regex_v8                   | 16.0 ms                                                | 17.3 ms: 1.09x slower                                                 |
| coverage                   | 38.9 ms                                                | 45.9 ms: 1.18x slower                                                 |
| python_startup_no_site     | 9.37 ms                                                | 11.5 ms: 1.23x slower                                                 |
| python_startup             | 11.4 ms                                                | 14.0 ms: 1.23x slower                                                 |
| telco                      | 3.68 ms                                                | 4.61 ms: 1.25x slower                                                 |
| create_gc_cycles           | 701 us                                                 | 910 us: 1.30x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                          |

Benchmark hidden because not significant (2): asyncio_tcp, dask
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, dulwich_log, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (14) of results/bm-20240518-3.14.0a0-caf6064/bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 0.54x