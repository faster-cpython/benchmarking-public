# Results vs. 3.12.0

- fork: brandtbucher
- ref: no_cold_exits
- machine: darwin-arm64
- commit hash: f837cc6
- commit date: 2024-06-10
- overall geometric mean: 1.05x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 0.85x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240610-darwin-arm64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 168 ms: 1.01x faster                                                 |
| docutils       | 1.50 sec                                               | 1.50 sec: 1.00x faster                                               |
| Geometric mean | (ref)                                                  | 1.01x faster                                                         |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240610-darwin-arm64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_memoization_tg  | 323 ms                                                 | 238 ms: 1.36x faster                                                 |
| async_tree_none_tg         | 258 ms                                                 | 196 ms: 1.31x faster                                                 |
| async_tree_none            | 266 ms                                                 | 214 ms: 1.24x faster                                                 |
| async_tree_io_tg           | 669 ms                                                 | 554 ms: 1.21x faster                                                 |
| async_tree_memoization     | 312 ms                                                 | 263 ms: 1.19x faster                                                 |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 451 ms: 1.18x faster                                                 |
| async_tree_io              | 668 ms                                                 | 571 ms: 1.17x faster                                                 |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 472 ms: 1.11x faster                                                 |
| Geometric mean             | (ref)                                                  | 1.22x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240610-darwin-arm64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 47.6 ms: 1.17x faster                                                |
| nbody          | 68.8 ms                                                | 63.7 ms: 1.08x faster                                                |
| Geometric mean | (ref)                                                  | 1.08x faster                                                         |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240610-darwin-arm64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 77.9 ms                                                | 73.4 ms: 1.06x faster                                                |
| regex_dna      | 154 ms                                                 | 149 ms: 1.04x faster                                                 |
| regex_effbot   | 2.64 ms                                                | 2.56 ms: 1.03x faster                                                |
| regex_v8       | 16.0 ms                                                | 17.3 ms: 1.09x slower                                                |
| Geometric mean | (ref)                                                  | 1.01x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240610-darwin-arm64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| pickle_pure_python   | 200 us                                                 | 173 us: 1.16x faster                                                 |
| unpickle_pure_python | 151 us                                                 | 132 us: 1.14x faster                                                 |
| xml_etree_process    | 39.7 ms                                                | 35.9 ms: 1.11x faster                                                |
| tomli_loads          | 1.39 sec                                               | 1.26 sec: 1.10x faster                                               |
| xml_etree_generate   | 55.8 ms                                                | 51.2 ms: 1.09x faster                                                |
| xml_etree_iterparse  | 74.0 ms                                                | 70.1 ms: 1.06x faster                                                |
| xml_etree_parse      | 106 ms                                                 | 102 ms: 1.04x faster                                                 |
| json_loads           | 17.2 us                                                | 16.9 us: 1.02x faster                                                |
| pickle_dict          | 18.1 us                                                | 18.2 us: 1.01x slower                                                |
| json_dumps           | 6.22 ms                                                | 6.31 ms: 1.01x slower                                                |
| unpickle_list        | 3.02 us                                                | 3.07 us: 1.02x slower                                                |
| unpickle             | 9.12 us                                                | 9.31 us: 1.02x slower                                                |
| pickle               | 7.23 us                                                | 7.45 us: 1.03x slower                                                |
| pickle_list          | 2.89 us                                                | 2.98 us: 1.03x slower                                                |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240610-darwin-arm64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 9.37 ms                                                | 11.6 ms: 1.23x slower                                                |
| python_startup         | 11.4 ms                                                | 14.1 ms: 1.24x slower                                                |
| Geometric mean         | (ref)                                                  | 1.24x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240610-darwin-arm64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 7.71 ms                                                | 6.36 ms: 1.21x faster                                                |
| django_template | 22.3 ms                                                | 21.4 ms: 1.05x faster                                                |
| Geometric mean  | (ref)                                                  | 1.13x faster                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240610-darwin-arm64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_memoization_tg  | 323 ms                                                 | 238 ms: 1.36x faster                                                 |
| generators                 | 31.1 ms                                                | 23.3 ms: 1.33x faster                                                |
| async_tree_none_tg         | 258 ms                                                 | 196 ms: 1.31x faster                                                 |
| deepcopy_memo              | 27.7 us                                                | 21.2 us: 1.30x faster                                                |
| raytrace                   | 212 ms                                                 | 165 ms: 1.29x faster                                                 |
| async_tree_none            | 266 ms                                                 | 214 ms: 1.24x faster                                                 |
| logging_silent             | 76.4 ns                                                | 62.3 ns: 1.23x faster                                                |
| coroutines                 | 19.2 ms                                                | 15.8 ms: 1.21x faster                                                |
| mako                       | 7.71 ms                                                | 6.36 ms: 1.21x faster                                                |
| async_tree_io_tg           | 669 ms                                                 | 554 ms: 1.21x faster                                                 |
| logging_simple             | 3.69 us                                                | 3.09 us: 1.19x faster                                                |
| async_tree_memoization     | 312 ms                                                 | 263 ms: 1.19x faster                                                 |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 451 ms: 1.18x faster                                                 |
| logging_format             | 3.98 us                                                | 3.39 us: 1.18x faster                                                |
| float                      | 55.8 ms                                                | 47.6 ms: 1.17x faster                                                |
| async_tree_io              | 668 ms                                                 | 571 ms: 1.17x faster                                                 |
| comprehensions             | 14.5 us                                                | 12.4 us: 1.17x faster                                                |
| pickle_pure_python         | 200 us                                                 | 173 us: 1.16x faster                                                 |
| unpickle_pure_python       | 151 us                                                 | 132 us: 1.14x faster                                                 |
| spectral_norm              | 76.4 ms                                                | 67.2 ms: 1.14x faster                                                |
| deepcopy                   | 235 us                                                 | 207 us: 1.13x faster                                                 |
| deepcopy_reduce            | 2.07 us                                                | 1.83 us: 1.13x faster                                                |
| pathlib                    | 24.2 ms                                                | 21.6 ms: 1.12x faster                                                |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 472 ms: 1.11x faster                                                 |
| xml_etree_process          | 39.7 ms                                                | 35.9 ms: 1.11x faster                                                |
| tomli_loads                | 1.39 sec                                               | 1.26 sec: 1.10x faster                                               |
| mdp                        | 1.58 sec                                               | 1.44 sec: 1.10x faster                                               |
| deltablue                  | 2.71 ms                                                | 2.46 ms: 1.10x faster                                                |
| nqueens                    | 62.4 ms                                                | 57.1 ms: 1.09x faster                                                |
| xml_etree_generate         | 55.8 ms                                                | 51.2 ms: 1.09x faster                                                |
| asyncio_tcp                | 449 ms                                                 | 415 ms: 1.08x faster                                                 |
| nbody                      | 68.8 ms                                                | 63.7 ms: 1.08x faster                                                |
| chaos                      | 42.5 ms                                                | 39.5 ms: 1.08x faster                                                |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 2.92 ms: 1.08x faster                                                |
| sympy_sum                  | 77.6 ms                                                | 72.4 ms: 1.07x faster                                                |
| sympy_str                  | 148 ms                                                 | 138 ms: 1.07x faster                                                 |
| regex_compile              | 77.9 ms                                                | 73.4 ms: 1.06x faster                                                |
| async_generators           | 304 ms                                                 | 287 ms: 1.06x faster                                                 |
| scimark_fft                | 195 ms                                                 | 185 ms: 1.06x faster                                                 |
| richards                   | 32.1 ms                                                | 30.4 ms: 1.06x faster                                                |
| xml_etree_iterparse        | 74.0 ms                                                | 70.1 ms: 1.06x faster                                                |
| richards_super             | 36.0 ms                                                | 34.2 ms: 1.05x faster                                                |
| json                       | 3.09 ms                                                | 2.94 ms: 1.05x faster                                                |
| bench_thread_pool          | 504 us                                                 | 481 us: 1.05x faster                                                 |
| django_template            | 22.3 ms                                                | 21.4 ms: 1.05x faster                                                |
| sympy_integrate            | 11.4 ms                                                | 10.9 ms: 1.04x faster                                                |
| xml_etree_parse            | 106 ms                                                 | 102 ms: 1.04x faster                                                 |
| regex_dna                  | 154 ms                                                 | 149 ms: 1.04x faster                                                 |
| regex_effbot               | 2.64 ms                                                | 2.56 ms: 1.03x faster                                                |
| pprint_safe_repr           | 497 ms                                                 | 483 ms: 1.03x faster                                                 |
| sqlglot_optimize           | 34.0 ms                                                | 33.2 ms: 1.03x faster                                                |
| pprint_pformat             | 1.01 sec                                               | 986 ms: 1.03x faster                                                 |
| hexiom                     | 4.54 ms                                                | 4.44 ms: 1.02x faster                                                |
| scimark_monte_carlo        | 45.0 ms                                                | 44.0 ms: 1.02x faster                                                |
| json_loads                 | 17.2 us                                                | 16.9 us: 1.02x faster                                                |
| sympy_expand               | 241 ms                                                 | 237 ms: 1.02x faster                                                 |
| sqlite_synth               | 1.57 us                                                | 1.55 us: 1.01x faster                                                |
| sqlglot_parse              | 848 us                                                 | 840 us: 1.01x faster                                                 |
| sqlglot_transpile          | 1.02 ms                                                | 1.01 ms: 1.01x faster                                                |
| asyncio_tcp_ssl            | 1.24 sec                                               | 1.23 sec: 1.01x faster                                               |
| 2to3                       | 169 ms                                                 | 168 ms: 1.01x faster                                                 |
| docutils                   | 1.50 sec                                               | 1.50 sec: 1.00x faster                                               |
| asyncio_websockets         | 409 ms                                                 | 409 ms: 1.00x faster                                                 |
| pickle_dict                | 18.1 us                                                | 18.2 us: 1.01x slower                                                |
| go                         | 102 ms                                                 | 103 ms: 1.01x slower                                                 |
| typing_runtime_protocols   | 93.0 us                                                | 94.1 us: 1.01x slower                                                |
| fannkuch                   | 248 ms                                                 | 251 ms: 1.01x slower                                                 |
| pyflate                    | 316 ms                                                 | 320 ms: 1.01x slower                                                 |
| json_dumps                 | 6.22 ms                                                | 6.31 ms: 1.01x slower                                                |
| unpickle_list              | 3.02 us                                                | 3.07 us: 1.02x slower                                                |
| crypto_pyaes               | 51.9 ms                                                | 52.8 ms: 1.02x slower                                                |
| unpickle                   | 9.12 us                                                | 9.31 us: 1.02x slower                                                |
| gc_traversal               | 2.40 ms                                                | 2.46 ms: 1.02x slower                                                |
| meteor_contest             | 71.7 ms                                                | 73.5 ms: 1.03x slower                                                |
| pickle                     | 7.23 us                                                | 7.45 us: 1.03x slower                                                |
| pickle_list                | 2.89 us                                                | 2.98 us: 1.03x slower                                                |
| scimark_lu                 | 76.0 ms                                                | 79.4 ms: 1.04x slower                                                |
| bench_mp_pool              | 44.9 ms                                                | 48.0 ms: 1.07x slower                                                |
| regex_v8                   | 16.0 ms                                                | 17.3 ms: 1.09x slower                                                |
| scimark_sor                | 87.4 ms                                                | 101 ms: 1.15x slower                                                 |
| coverage                   | 38.9 ms                                                | 45.9 ms: 1.18x slower                                                |
| python_startup_no_site     | 9.37 ms                                                | 11.6 ms: 1.23x slower                                                |
| python_startup             | 11.4 ms                                                | 14.1 ms: 1.24x slower                                                |
| telco                      | 3.68 ms                                                | 4.57 ms: 1.24x slower                                                |
| create_gc_cycles           | 701 us                                                 | 895 us: 1.28x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.05x faster                                                         |

Benchmark hidden because not significant (4): tornado_http, pycparser, dask, pidigits
Ignored benchmarks (9) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dulwich_log, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, unpack_sequence
Ignored benchmarks (13) of results/bm-20240610-3.14.0a0-f837cc6-JIT/bm-20240610-darwin-arm64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 0.85x