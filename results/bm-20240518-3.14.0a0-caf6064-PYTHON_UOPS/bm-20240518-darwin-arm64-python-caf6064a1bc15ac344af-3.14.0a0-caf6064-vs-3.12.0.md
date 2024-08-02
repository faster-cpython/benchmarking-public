# Results vs. 3.12.0

- fork: python
- ref: caf6064a1bc15ac344af
- machine: darwin-arm64
- commit hash: caf6064
- commit date: 2024-05-18
- overall geometric mean: 1.06x slower
- HPT reliability: 99.98%
- HPT 99th percentile: 1.03x slower
- Memory change: 0.47x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 182 ms: 1.07x slower                                                  |
| chameleon      | 4.70 ms                                                | 4.94 ms: 1.05x slower                                                 |
| docutils       | 1.50 sec                                               | 1.66 sec: 1.11x slower                                                |
| Geometric mean | (ref)                                                  | 1.06x slower                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none_tg         | 258 ms                                                 | 206 ms: 1.25x faster                                                  |
| async_tree_memoization_tg  | 323 ms                                                 | 259 ms: 1.25x faster                                                  |
| async_tree_none            | 266 ms                                                 | 221 ms: 1.20x faster                                                  |
| async_tree_io_tg           | 669 ms                                                 | 564 ms: 1.19x faster                                                  |
| async_tree_io              | 668 ms                                                 | 573 ms: 1.17x faster                                                  |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 458 ms: 1.16x faster                                                  |
| async_tree_memoization     | 312 ms                                                 | 272 ms: 1.15x faster                                                  |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 480 ms: 1.09x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.18x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 282 ms                                                 | 282 ms: 1.00x slower                                                  |
| float          | 55.8 ms                                                | 60.5 ms: 1.08x slower                                                 |
| nbody          | 68.8 ms                                                | 77.3 ms: 1.12x slower                                                 |
| Geometric mean | (ref)                                                  | 1.07x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_dna      | 154 ms                                                 | 149 ms: 1.03x faster                                                  |
| regex_effbot   | 2.64 ms                                                | 2.59 ms: 1.02x faster                                                 |
| regex_v8       | 16.0 ms                                                | 17.6 ms: 1.10x slower                                                 |
| regex_compile  | 77.9 ms                                                | 95.7 ms: 1.23x slower                                                 |
| Geometric mean | (ref)                                                  | 1.06x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| unpickle_list        | 3.02 us                                                | 2.88 us: 1.05x faster                                                 |
| json_loads           | 17.2 us                                                | 16.9 us: 1.02x faster                                                 |
| pickle_dict          | 18.1 us                                                | 18.2 us: 1.01x slower                                                 |
| pickle_list          | 2.89 us                                                | 2.97 us: 1.03x slower                                                 |
| unpickle             | 9.12 us                                                | 9.39 us: 1.03x slower                                                 |
| xml_etree_iterparse  | 74.0 ms                                                | 76.5 ms: 1.03x slower                                                 |
| pickle               | 7.23 us                                                | 7.47 us: 1.03x slower                                                 |
| xml_etree_process    | 39.7 ms                                                | 41.1 ms: 1.04x slower                                                 |
| json_dumps           | 6.22 ms                                                | 6.53 ms: 1.05x slower                                                 |
| xml_etree_generate   | 55.8 ms                                                | 58.7 ms: 1.05x slower                                                 |
| pickle_pure_python   | 200 us                                                 | 228 us: 1.14x slower                                                  |
| unpickle_pure_python | 151 us                                                 | 176 us: 1.17x slower                                                  |
| tomli_loads          | 1.39 sec                                               | 1.64 sec: 1.17x slower                                                |
| Geometric mean       | (ref)                                                  | 1.05x slower                                                          |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 11.4 ms                                                | 14.2 ms: 1.24x slower                                                 |
| python_startup_no_site | 9.37 ms                                                | 11.7 ms: 1.25x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.25x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 22.3 ms                                                | 23.8 ms: 1.07x slower                                                 |
| mako            | 7.71 ms                                                | 9.09 ms: 1.18x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.12x slower                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| generators                 | 31.1 ms                                                | 23.6 ms: 1.32x faster                                                 |
| async_tree_none_tg         | 258 ms                                                 | 206 ms: 1.25x faster                                                  |
| async_tree_memoization_tg  | 323 ms                                                 | 259 ms: 1.25x faster                                                  |
| raytrace                   | 212 ms                                                 | 175 ms: 1.21x faster                                                  |
| async_tree_none            | 266 ms                                                 | 221 ms: 1.20x faster                                                  |
| coroutines                 | 19.2 ms                                                | 16.1 ms: 1.20x faster                                                 |
| async_tree_io_tg           | 669 ms                                                 | 564 ms: 1.19x faster                                                  |
| async_tree_io              | 668 ms                                                 | 573 ms: 1.17x faster                                                  |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 458 ms: 1.16x faster                                                  |
| logging_simple             | 3.69 us                                                | 3.18 us: 1.16x faster                                                 |
| logging_format             | 3.98 us                                                | 3.45 us: 1.16x faster                                                 |
| async_tree_memoization     | 312 ms                                                 | 272 ms: 1.15x faster                                                  |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 480 ms: 1.09x faster                                                  |
| pathlib                    | 24.2 ms                                                | 22.5 ms: 1.08x faster                                                 |
| asyncio_tcp                | 449 ms                                                 | 418 ms: 1.07x faster                                                  |
| unpickle_list              | 3.02 us                                                | 2.88 us: 1.05x faster                                                 |
| regex_dna                  | 154 ms                                                 | 149 ms: 1.03x faster                                                  |
| json                       | 3.09 ms                                                | 3.00 ms: 1.03x faster                                                 |
| async_generators           | 304 ms                                                 | 296 ms: 1.03x faster                                                  |
| regex_effbot               | 2.64 ms                                                | 2.59 ms: 1.02x faster                                                 |
| json_loads                 | 17.2 us                                                | 16.9 us: 1.02x faster                                                 |
| asyncio_websockets         | 409 ms                                                 | 408 ms: 1.00x faster                                                  |
| pidigits                   | 282 ms                                                 | 282 ms: 1.00x slower                                                  |
| pickle_dict                | 18.1 us                                                | 18.2 us: 1.01x slower                                                 |
| deepcopy_reduce            | 2.07 us                                                | 2.11 us: 1.02x slower                                                 |
| dask                       | 222 ms                                                 | 227 ms: 1.02x slower                                                  |
| sqlite_synth               | 1.57 us                                                | 1.61 us: 1.02x slower                                                 |
| gc_traversal               | 2.40 ms                                                | 2.46 ms: 1.03x slower                                                 |
| pickle_list                | 2.89 us                                                | 2.97 us: 1.03x slower                                                 |
| unpickle                   | 9.12 us                                                | 9.39 us: 1.03x slower                                                 |
| xml_etree_iterparse        | 74.0 ms                                                | 76.5 ms: 1.03x slower                                                 |
| pickle                     | 7.23 us                                                | 7.47 us: 1.03x slower                                                 |
| xml_etree_process          | 39.7 ms                                                | 41.1 ms: 1.04x slower                                                 |
| mdp                        | 1.58 sec                                               | 1.64 sec: 1.04x slower                                                |
| bench_thread_pool          | 504 us                                                 | 525 us: 1.04x slower                                                  |
| asyncio_tcp_ssl            | 1.24 sec                                               | 1.30 sec: 1.04x slower                                                |
| json_dumps                 | 6.22 ms                                                | 6.53 ms: 1.05x slower                                                 |
| bench_mp_pool              | 44.9 ms                                                | 47.1 ms: 1.05x slower                                                 |
| xml_etree_generate         | 55.8 ms                                                | 58.7 ms: 1.05x slower                                                 |
| chameleon                  | 4.70 ms                                                | 4.94 ms: 1.05x slower                                                 |
| deepcopy                   | 235 us                                                 | 248 us: 1.06x slower                                                  |
| django_template            | 22.3 ms                                                | 23.8 ms: 1.07x slower                                                 |
| pycparser                  | 677 ms                                                 | 723 ms: 1.07x slower                                                  |
| 2to3                       | 169 ms                                                 | 182 ms: 1.07x slower                                                  |
| float                      | 55.8 ms                                                | 60.5 ms: 1.08x slower                                                 |
| deltablue                  | 2.71 ms                                                | 2.94 ms: 1.09x slower                                                 |
| sqlglot_optimize           | 34.0 ms                                                | 37.2 ms: 1.09x slower                                                 |
| sympy_expand               | 241 ms                                                 | 266 ms: 1.10x slower                                                  |
| regex_v8                   | 16.0 ms                                                | 17.6 ms: 1.10x slower                                                 |
| chaos                      | 42.5 ms                                                | 47.0 ms: 1.10x slower                                                 |
| sympy_sum                  | 77.6 ms                                                | 85.9 ms: 1.11x slower                                                 |
| nqueens                    | 62.4 ms                                                | 69.1 ms: 1.11x slower                                                 |
| docutils                   | 1.50 sec                                               | 1.66 sec: 1.11x slower                                                |
| sympy_str                  | 148 ms                                                 | 164 ms: 1.11x slower                                                  |
| sympy_integrate            | 11.4 ms                                                | 12.6 ms: 1.11x slower                                                 |
| meteor_contest             | 71.7 ms                                                | 80.1 ms: 1.12x slower                                                 |
| nbody                      | 68.8 ms                                                | 77.3 ms: 1.12x slower                                                 |
| sqlglot_parse              | 848 us                                                 | 957 us: 1.13x slower                                                  |
| sqlglot_transpile          | 1.02 ms                                                | 1.15 ms: 1.13x slower                                                 |
| pickle_pure_python         | 200 us                                                 | 228 us: 1.14x slower                                                  |
| richards_super             | 36.0 ms                                                | 41.2 ms: 1.14x slower                                                 |
| go                         | 102 ms                                                 | 117 ms: 1.15x slower                                                  |
| typing_runtime_protocols   | 93.0 us                                                | 108 us: 1.16x slower                                                  |
| pprint_safe_repr           | 497 ms                                                 | 578 ms: 1.16x slower                                                  |
| pprint_pformat             | 1.01 sec                                               | 1.18 sec: 1.17x slower                                                |
| unpickle_pure_python       | 151 us                                                 | 176 us: 1.17x slower                                                  |
| deepcopy_memo              | 27.7 us                                                | 32.4 us: 1.17x slower                                                 |
| richards                   | 32.1 ms                                                | 37.6 ms: 1.17x slower                                                 |
| tomli_loads                | 1.39 sec                                               | 1.64 sec: 1.17x slower                                                |
| coverage                   | 38.9 ms                                                | 45.7 ms: 1.18x slower                                                 |
| mako                       | 7.71 ms                                                | 9.09 ms: 1.18x slower                                                 |
| crypto_pyaes               | 51.9 ms                                                | 61.2 ms: 1.18x slower                                                 |
| scimark_fft                | 195 ms                                                 | 232 ms: 1.19x slower                                                  |
| comprehensions             | 14.5 us                                                | 17.3 us: 1.19x slower                                                 |
| regex_compile              | 77.9 ms                                                | 95.7 ms: 1.23x slower                                                 |
| spectral_norm              | 76.4 ms                                                | 94.2 ms: 1.23x slower                                                 |
| scimark_sor                | 87.4 ms                                                | 108 ms: 1.23x slower                                                  |
| python_startup             | 11.4 ms                                                | 14.2 ms: 1.24x slower                                                 |
| logging_silent             | 76.4 ns                                                | 95.4 ns: 1.25x slower                                                 |
| python_startup_no_site     | 9.37 ms                                                | 11.7 ms: 1.25x slower                                                 |
| pyflate                    | 316 ms                                                 | 399 ms: 1.27x slower                                                  |
| fannkuch                   | 248 ms                                                 | 318 ms: 1.28x slower                                                  |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 4.01 ms: 1.28x slower                                                 |
| scimark_lu                 | 76.0 ms                                                | 98.1 ms: 1.29x slower                                                 |
| create_gc_cycles           | 701 us                                                 | 914 us: 1.30x slower                                                  |
| hexiom                     | 4.54 ms                                                | 6.00 ms: 1.32x slower                                                 |
| scimark_monte_carlo        | 45.0 ms                                                | 61.1 ms: 1.36x slower                                                 |
| telco                      | 3.68 ms                                                | 5.12 ms: 1.39x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.06x slower                                                          |

Benchmark hidden because not significant (2): xml_etree_parse, tornado_http
Ignored benchmarks (8) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, dulwich_log, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, unpack_sequence
Ignored benchmarks (14) of results/bm-20240518-3.14.0a0-caf6064-PYTHON_UOPS/bm-20240518-darwin-arm64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.98% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: 0.47x