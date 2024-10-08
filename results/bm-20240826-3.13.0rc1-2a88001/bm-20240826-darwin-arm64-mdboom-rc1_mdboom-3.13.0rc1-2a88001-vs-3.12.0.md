# Results vs. 3.12.0

- fork: mdboom
- ref: rc1_mdboom
- machine: darwin-arm64
- commit hash: 2a88001
- commit date: 2024-08-26
- overall geometric mean: 1.00x slower
- HPT reliability: 81.02%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.45x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240826-darwin-arm64-mdboom-rc1_mdboom-3.13.0rc1-2a88001 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 200 ms: 1.18x slower                                         |
| chameleon      | 4.70 ms                                                | 4.65 ms: 1.01x faster                                        |
| docutils       | 1.50 sec                                               | 1.54 sec: 1.02x slower                                       |
| tornado_http   | 69.3 ms                                                | 84.8 ms: 1.22x slower                                        |
| Geometric mean | (ref)                                                  | 1.10x slower                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240826-darwin-arm64-mdboom-rc1_mdboom-3.13.0rc1-2a88001 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_none_tg         | 258 ms                                                 | 213 ms: 1.21x faster                                         |
| async_tree_memoization_tg  | 323 ms                                                 | 267 ms: 1.21x faster                                         |
| async_tree_none            | 266 ms                                                 | 227 ms: 1.17x faster                                         |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 464 ms: 1.15x faster                                         |
| async_tree_io_tg           | 669 ms                                                 | 587 ms: 1.14x faster                                         |
| async_tree_io              | 668 ms                                                 | 587 ms: 1.14x faster                                         |
| async_tree_memoization     | 312 ms                                                 | 279 ms: 1.12x faster                                         |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 488 ms: 1.08x faster                                         |
| Geometric mean             | (ref)                                                  | 1.15x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240826-darwin-arm64-mdboom-rc1_mdboom-3.13.0rc1-2a88001 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| float          | 55.8 ms                                                | 51.4 ms: 1.09x faster                                        |
| nbody          | 68.8 ms                                                | 66.0 ms: 1.04x faster                                        |
| pidigits       | 282 ms                                                 | 283 ms: 1.00x slower                                         |
| Geometric mean | (ref)                                                  | 1.04x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240826-darwin-arm64-mdboom-rc1_mdboom-3.13.0rc1-2a88001 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| regex_dna      | 154 ms                                                 | 144 ms: 1.07x faster                                         |
| regex_compile  | 77.9 ms                                                | 73.9 ms: 1.05x faster                                        |
| regex_effbot   | 2.64 ms                                                | 2.55 ms: 1.04x faster                                        |
| regex_v8       | 16.0 ms                                                | 16.8 ms: 1.05x slower                                        |
| Geometric mean | (ref)                                                  | 1.03x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240826-darwin-arm64-mdboom-rc1_mdboom-3.13.0rc1-2a88001 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| pickle_pure_python   | 200 us                                                 | 191 us: 1.05x faster                                         |
| unpickle_pure_python | 151 us                                                 | 152 us: 1.01x slower                                         |
| xml_etree_parse      | 106 ms                                                 | 108 ms: 1.02x slower                                         |
| json_loads           | 17.2 us                                                | 17.8 us: 1.03x slower                                        |
| xml_etree_process    | 39.7 ms                                                | 42.2 ms: 1.06x slower                                        |
| json_dumps           | 6.22 ms                                                | 6.65 ms: 1.07x slower                                        |
| xml_etree_generate   | 55.8 ms                                                | 59.9 ms: 1.07x slower                                        |
| tomli_loads          | 1.39 sec                                               | 1.56 sec: 1.12x slower                                       |
| Geometric mean       | (ref)                                                  | 1.04x slower                                                 |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240826-darwin-arm64-mdboom-rc1_mdboom-3.13.0rc1-2a88001 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup_no_site | 9.37 ms                                                | 13.0 ms: 1.38x slower                                        |
| python_startup         | 11.4 ms                                                | 15.9 ms: 1.39x slower                                        |
| Geometric mean         | (ref)                                                  | 1.39x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240826-darwin-arm64-mdboom-rc1_mdboom-3.13.0rc1-2a88001 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| mako            | 7.71 ms                                                | 7.37 ms: 1.05x faster                                        |
| django_template | 22.3 ms                                                | 22.2 ms: 1.00x faster                                        |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240826-darwin-arm64-mdboom-rc1_mdboom-3.13.0rc1-2a88001 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| generators                 | 31.1 ms                                                | 23.7 ms: 1.31x faster                                        |
| raytrace                   | 212 ms                                                 | 168 ms: 1.26x faster                                         |
| comprehensions             | 14.5 us                                                | 11.8 us: 1.24x faster                                        |
| async_tree_none_tg         | 258 ms                                                 | 213 ms: 1.21x faster                                         |
| async_tree_memoization_tg  | 323 ms                                                 | 267 ms: 1.21x faster                                         |
| deltablue                  | 2.71 ms                                                | 2.29 ms: 1.18x faster                                        |
| async_tree_none            | 266 ms                                                 | 227 ms: 1.17x faster                                         |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 464 ms: 1.15x faster                                         |
| deepcopy_memo              | 27.7 us                                                | 24.3 us: 1.14x faster                                        |
| async_tree_io_tg           | 669 ms                                                 | 587 ms: 1.14x faster                                         |
| async_tree_io              | 668 ms                                                 | 587 ms: 1.14x faster                                         |
| logging_silent             | 76.4 ns                                                | 67.8 ns: 1.13x faster                                        |
| async_tree_memoization     | 312 ms                                                 | 279 ms: 1.12x faster                                         |
| chaos                      | 42.5 ms                                                | 38.1 ms: 1.12x faster                                        |
| float                      | 55.8 ms                                                | 51.4 ms: 1.09x faster                                        |
| hexiom                     | 4.54 ms                                                | 4.20 ms: 1.08x faster                                        |
| asyncio_tcp                | 449 ms                                                 | 415 ms: 1.08x faster                                         |
| sqlglot_parse              | 848 us                                                 | 784 us: 1.08x faster                                         |
| nqueens                    | 62.4 ms                                                | 57.8 ms: 1.08x faster                                        |
| logging_simple             | 3.69 us                                                | 3.42 us: 1.08x faster                                        |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 488 ms: 1.08x faster                                         |
| regex_dna                  | 154 ms                                                 | 144 ms: 1.07x faster                                         |
| logging_format             | 3.98 us                                                | 3.74 us: 1.07x faster                                        |
| sqlglot_transpile          | 1.02 ms                                                | 958 us: 1.07x faster                                         |
| dulwich_log                | 29.8 ms                                                | 28.2 ms: 1.06x faster                                        |
| spectral_norm              | 76.4 ms                                                | 72.5 ms: 1.05x faster                                        |
| regex_compile              | 77.9 ms                                                | 73.9 ms: 1.05x faster                                        |
| pickle_pure_python         | 200 us                                                 | 191 us: 1.05x faster                                         |
| mako                       | 7.71 ms                                                | 7.37 ms: 1.05x faster                                        |
| nbody                      | 68.8 ms                                                | 66.0 ms: 1.04x faster                                        |
| bench_thread_pool          | 504 us                                                 | 486 us: 1.04x faster                                         |
| regex_effbot               | 2.64 ms                                                | 2.55 ms: 1.04x faster                                        |
| deepcopy                   | 235 us                                                 | 227 us: 1.04x faster                                         |
| crypto_pyaes               | 51.9 ms                                                | 50.5 ms: 1.03x faster                                        |
| deepcopy_reduce            | 2.07 us                                                | 2.03 us: 1.02x faster                                        |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 3.08 ms: 1.02x faster                                        |
| sympy_integrate            | 11.4 ms                                                | 11.2 ms: 1.02x faster                                        |
| chameleon                  | 4.70 ms                                                | 4.65 ms: 1.01x faster                                        |
| scimark_monte_carlo        | 45.0 ms                                                | 44.6 ms: 1.01x faster                                        |
| json                       | 3.09 ms                                                | 3.06 ms: 1.01x faster                                        |
| sympy_sum                  | 77.6 ms                                                | 77.1 ms: 1.01x faster                                        |
| django_template            | 22.3 ms                                                | 22.2 ms: 1.00x faster                                        |
| asyncio_websockets         | 409 ms                                                 | 408 ms: 1.00x faster                                         |
| pidigits                   | 282 ms                                                 | 283 ms: 1.00x slower                                         |
| scimark_fft                | 195 ms                                                 | 197 ms: 1.01x slower                                         |
| scimark_lu                 | 76.0 ms                                                | 76.7 ms: 1.01x slower                                        |
| unpickle_pure_python       | 151 us                                                 | 152 us: 1.01x slower                                         |
| mdp                        | 1.58 sec                                               | 1.60 sec: 1.01x slower                                       |
| xml_etree_parse            | 106 ms                                                 | 108 ms: 1.02x slower                                         |
| go                         | 102 ms                                                 | 103 ms: 1.02x slower                                         |
| docutils                   | 1.50 sec                                               | 1.54 sec: 1.02x slower                                       |
| pprint_pformat             | 1.01 sec                                               | 1.04 sec: 1.02x slower                                       |
| meteor_contest             | 71.7 ms                                                | 73.6 ms: 1.03x slower                                        |
| richards_super             | 36.0 ms                                                | 37.0 ms: 1.03x slower                                        |
| pprint_safe_repr           | 497 ms                                                 | 511 ms: 1.03x slower                                         |
| gc_traversal               | 2.40 ms                                                | 2.47 ms: 1.03x slower                                        |
| coroutines                 | 19.2 ms                                                | 19.8 ms: 1.03x slower                                        |
| json_loads                 | 17.2 us                                                | 17.8 us: 1.03x slower                                        |
| asyncio_tcp_ssl            | 1.24 sec                                               | 1.29 sec: 1.04x slower                                       |
| sqlglot_normalize          | 186 ms                                                 | 193 ms: 1.04x slower                                         |
| richards                   | 32.1 ms                                                | 33.5 ms: 1.04x slower                                        |
| pathlib                    | 24.2 ms                                                | 25.5 ms: 1.05x slower                                        |
| regex_v8                   | 16.0 ms                                                | 16.8 ms: 1.05x slower                                        |
| sqlglot_optimize           | 34.0 ms                                                | 35.8 ms: 1.05x slower                                        |
| async_generators           | 304 ms                                                 | 323 ms: 1.06x slower                                         |
| xml_etree_process          | 39.7 ms                                                | 42.2 ms: 1.06x slower                                        |
| pyflate                    | 316 ms                                                 | 336 ms: 1.07x slower                                         |
| sympy_expand               | 241 ms                                                 | 257 ms: 1.07x slower                                         |
| json_dumps                 | 6.22 ms                                                | 6.65 ms: 1.07x slower                                        |
| xml_etree_generate         | 55.8 ms                                                | 59.9 ms: 1.07x slower                                        |
| bench_mp_pool              | 44.9 ms                                                | 48.8 ms: 1.09x slower                                        |
| dask                       | 222 ms                                                 | 243 ms: 1.10x slower                                         |
| tomli_loads                | 1.39 sec                                               | 1.56 sec: 1.12x slower                                       |
| typing_runtime_protocols   | 93.0 us                                                | 108 us: 1.16x slower                                         |
| 2to3                       | 169 ms                                                 | 200 ms: 1.18x slower                                         |
| scimark_sor                | 87.4 ms                                                | 104 ms: 1.19x slower                                         |
| fannkuch                   | 248 ms                                                 | 296 ms: 1.19x slower                                         |
| tornado_http               | 69.3 ms                                                | 84.8 ms: 1.22x slower                                        |
| create_gc_cycles           | 701 us                                                 | 882 us: 1.26x slower                                         |
| mypy2                      | 380 ms                                                 | 494 ms: 1.30x slower                                         |
| coverage                   | 38.9 ms                                                | 50.8 ms: 1.31x slower                                        |
| telco                      | 3.68 ms                                                | 4.95 ms: 1.35x slower                                        |
| python_startup_no_site     | 9.37 ms                                                | 13.0 ms: 1.38x slower                                        |
| python_startup             | 11.4 ms                                                | 15.9 ms: 1.39x slower                                        |
| Geometric mean             | (ref)                                                  | 1.00x slower                                                 |

Benchmark hidden because not significant (3): sympy_str, xml_etree_iterparse, pycparser
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, gunicorn, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (14) of results/bm-20240826-3.13.0rc1-2a88001/bm-20240826-darwin-arm64-mdboom-rc1_mdboom-3.13.0rc1-2a88001.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 81.02% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.45x