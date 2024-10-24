# Results vs. 3.12.0

- fork: python
- ref: 04eb5c8db1e24cabd0cb
- machine: darwin-arm64
- commit hash: 04eb5c8
- commit date: 2024-07-27
- overall geometric mean: 1.08x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 0.43x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 171 ms: 1.01x slower                                                  |
| docutils       | 1.50 sec                                               | 1.53 sec: 1.02x slower                                                |
| Geometric mean | (ref)                                                  | 1.00x slower                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none_tg         | 258 ms                                                 | 182 ms: 1.42x faster                                                  |
| async_tree_memoization_tg  | 323 ms                                                 | 228 ms: 1.41x faster                                                  |
| async_tree_none            | 266 ms                                                 | 195 ms: 1.36x faster                                                  |
| async_tree_io_tg           | 669 ms                                                 | 498 ms: 1.34x faster                                                  |
| async_tree_memoization     | 312 ms                                                 | 241 ms: 1.29x faster                                                  |
| async_tree_io              | 668 ms                                                 | 544 ms: 1.23x faster                                                  |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 441 ms: 1.21x faster                                                  |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 454 ms: 1.16x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.30x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 45.9 ms: 1.21x faster                                                 |
| nbody          | 68.8 ms                                                | 63.0 ms: 1.09x faster                                                 |
| Geometric mean | (ref)                                                  | 1.10x faster                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 77.9 ms                                                | 72.8 ms: 1.07x faster                                                 |
| regex_dna      | 154 ms                                                 | 149 ms: 1.04x faster                                                  |
| regex_effbot   | 2.64 ms                                                | 2.56 ms: 1.03x faster                                                 |
| regex_v8       | 16.0 ms                                                | 17.3 ms: 1.08x slower                                                 |
| Geometric mean | (ref)                                                  | 1.01x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 200 us                                                 | 171 us: 1.17x faster                                                  |
| unpickle_pure_python | 151 us                                                 | 133 us: 1.13x faster                                                  |
| tomli_loads          | 1.39 sec                                               | 1.24 sec: 1.13x faster                                                |
| xml_etree_process    | 39.7 ms                                                | 35.4 ms: 1.12x faster                                                 |
| xml_etree_generate   | 55.8 ms                                                | 52.0 ms: 1.07x faster                                                 |
| xml_etree_iterparse  | 74.0 ms                                                | 70.9 ms: 1.04x faster                                                 |
| xml_etree_parse      | 106 ms                                                 | 104 ms: 1.02x faster                                                  |
| json_loads           | 17.2 us                                                | 17.0 us: 1.01x faster                                                 |
| json_dumps           | 6.22 ms                                                | 6.38 ms: 1.03x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 11.4 ms                                                | 15.3 ms: 1.34x slower                                                 |
| python_startup_no_site | 9.37 ms                                                | 12.7 ms: 1.36x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.35x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 7.71 ms                                                | 6.39 ms: 1.21x faster                                                 |
| django_template | 22.3 ms                                                | 21.1 ms: 1.06x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.13x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| deepcopy_memo              | 27.7 us                                                | 16.5 us: 1.68x faster                                                 |
| deepcopy                   | 235 us                                                 | 151 us: 1.55x faster                                                  |
| generators                 | 31.1 ms                                                | 21.5 ms: 1.44x faster                                                 |
| async_tree_none_tg         | 258 ms                                                 | 182 ms: 1.42x faster                                                  |
| async_tree_memoization_tg  | 323 ms                                                 | 228 ms: 1.41x faster                                                  |
| async_tree_none            | 266 ms                                                 | 195 ms: 1.36x faster                                                  |
| async_tree_io_tg           | 669 ms                                                 | 498 ms: 1.34x faster                                                  |
| raytrace                   | 212 ms                                                 | 160 ms: 1.33x faster                                                  |
| deepcopy_reduce            | 2.07 us                                                | 1.56 us: 1.33x faster                                                 |
| async_tree_memoization     | 312 ms                                                 | 241 ms: 1.29x faster                                                  |
| logging_simple             | 3.69 us                                                | 2.94 us: 1.25x faster                                                 |
| logging_silent             | 76.4 ns                                                | 61.0 ns: 1.25x faster                                                 |
| async_tree_io              | 668 ms                                                 | 544 ms: 1.23x faster                                                  |
| logging_format             | 3.98 us                                                | 3.24 us: 1.23x faster                                                 |
| float                      | 55.8 ms                                                | 45.9 ms: 1.21x faster                                                 |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 441 ms: 1.21x faster                                                  |
| mako                       | 7.71 ms                                                | 6.39 ms: 1.21x faster                                                 |
| coroutines                 | 19.2 ms                                                | 16.1 ms: 1.19x faster                                                 |
| deltablue                  | 2.71 ms                                                | 2.27 ms: 1.19x faster                                                 |
| comprehensions             | 14.5 us                                                | 12.3 us: 1.19x faster                                                 |
| pickle_pure_python         | 200 us                                                 | 171 us: 1.17x faster                                                  |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 454 ms: 1.16x faster                                                  |
| spectral_norm              | 76.4 ms                                                | 66.9 ms: 1.14x faster                                                 |
| unpickle_pure_python       | 151 us                                                 | 133 us: 1.13x faster                                                  |
| tomli_loads                | 1.39 sec                                               | 1.24 sec: 1.13x faster                                                |
| xml_etree_process          | 39.7 ms                                                | 35.4 ms: 1.12x faster                                                 |
| chaos                      | 42.5 ms                                                | 38.5 ms: 1.10x faster                                                 |
| nqueens                    | 62.4 ms                                                | 56.6 ms: 1.10x faster                                                 |
| mdp                        | 1.58 sec                                               | 1.44 sec: 1.10x faster                                                |
| nbody                      | 68.8 ms                                                | 63.0 ms: 1.09x faster                                                 |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 2.87 ms: 1.09x faster                                                 |
| xml_etree_generate         | 55.8 ms                                                | 52.0 ms: 1.07x faster                                                 |
| bench_thread_pool          | 504 us                                                 | 470 us: 1.07x faster                                                  |
| regex_compile              | 77.9 ms                                                | 72.8 ms: 1.07x faster                                                 |
| json                       | 3.09 ms                                                | 2.89 ms: 1.07x faster                                                 |
| richards                   | 32.1 ms                                                | 30.2 ms: 1.06x faster                                                 |
| sympy_str                  | 148 ms                                                 | 139 ms: 1.06x faster                                                  |
| sympy_sum                  | 77.6 ms                                                | 73.1 ms: 1.06x faster                                                 |
| scimark_fft                | 195 ms                                                 | 184 ms: 1.06x faster                                                  |
| richards_super             | 36.0 ms                                                | 33.9 ms: 1.06x faster                                                 |
| sqlglot_normalize          | 186 ms                                                 | 175 ms: 1.06x faster                                                  |
| django_template            | 22.3 ms                                                | 21.1 ms: 1.06x faster                                                 |
| dulwich_log                | 29.8 ms                                                | 28.2 ms: 1.06x faster                                                 |
| scimark_monte_carlo        | 45.0 ms                                                | 42.7 ms: 1.05x faster                                                 |
| xml_etree_iterparse        | 74.0 ms                                                | 70.9 ms: 1.04x faster                                                 |
| pprint_safe_repr           | 497 ms                                                 | 477 ms: 1.04x faster                                                  |
| async_generators           | 304 ms                                                 | 292 ms: 1.04x faster                                                  |
| pprint_pformat             | 1.01 sec                                               | 974 ms: 1.04x faster                                                  |
| hexiom                     | 4.54 ms                                                | 4.38 ms: 1.04x faster                                                 |
| regex_dna                  | 154 ms                                                 | 149 ms: 1.04x faster                                                  |
| sqlglot_optimize           | 34.0 ms                                                | 32.8 ms: 1.04x faster                                                 |
| pathlib                    | 24.2 ms                                                | 23.4 ms: 1.04x faster                                                 |
| sqlglot_parse              | 848 us                                                 | 820 us: 1.03x faster                                                  |
| regex_effbot               | 2.64 ms                                                | 2.56 ms: 1.03x faster                                                 |
| sympy_integrate            | 11.4 ms                                                | 11.1 ms: 1.03x faster                                                 |
| sqlglot_transpile          | 1.02 ms                                                | 996 us: 1.03x faster                                                  |
| xml_etree_parse            | 106 ms                                                 | 104 ms: 1.02x faster                                                  |
| go                         | 102 ms                                                 | 99.7 ms: 1.02x faster                                                 |
| pyflate                    | 316 ms                                                 | 310 ms: 1.02x faster                                                  |
| json_loads                 | 17.2 us                                                | 17.0 us: 1.01x faster                                                 |
| meteor_contest             | 71.7 ms                                                | 71.0 ms: 1.01x faster                                                 |
| pycparser                  | 677 ms                                                 | 670 ms: 1.01x faster                                                  |
| crypto_pyaes               | 51.9 ms                                                | 51.4 ms: 1.01x faster                                                 |
| sympy_expand               | 241 ms                                                 | 240 ms: 1.00x faster                                                  |
| asyncio_websockets         | 409 ms                                                 | 408 ms: 1.00x faster                                                  |
| fannkuch                   | 248 ms                                                 | 249 ms: 1.00x slower                                                  |
| 2to3                       | 169 ms                                                 | 171 ms: 1.01x slower                                                  |
| docutils                   | 1.50 sec                                               | 1.53 sec: 1.02x slower                                                |
| typing_runtime_protocols   | 93.0 us                                                | 95.1 us: 1.02x slower                                                 |
| json_dumps                 | 6.22 ms                                                | 6.38 ms: 1.03x slower                                                 |
| gc_traversal               | 2.40 ms                                                | 2.46 ms: 1.03x slower                                                 |
| asyncio_tcp_ssl            | 1.24 sec                                               | 1.28 sec: 1.03x slower                                                |
| scimark_lu                 | 76.0 ms                                                | 79.6 ms: 1.05x slower                                                 |
| regex_v8                   | 16.0 ms                                                | 17.3 ms: 1.08x slower                                                 |
| bench_mp_pool              | 44.9 ms                                                | 50.9 ms: 1.14x slower                                                 |
| scimark_sor                | 87.4 ms                                                | 99.6 ms: 1.14x slower                                                 |
| coverage                   | 38.9 ms                                                | 45.1 ms: 1.16x slower                                                 |
| telco                      | 3.68 ms                                                | 4.57 ms: 1.24x slower                                                 |
| create_gc_cycles           | 701 us                                                 | 907 us: 1.29x slower                                                  |
| python_startup             | 11.4 ms                                                | 15.3 ms: 1.34x slower                                                 |
| python_startup_no_site     | 9.37 ms                                                | 12.7 ms: 1.36x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                          |

Benchmark hidden because not significant (4): tornado_http, asyncio_tcp, pidigits, dask
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (14) of results/bm-20240727-3.14.0a0-04eb5c8-JIT/bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 0.43x