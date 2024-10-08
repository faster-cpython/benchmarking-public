# Results vs. 3.12.0

- fork: python
- ref: 04eb5c8db1e24cabd0cb
- machine: darwin-arm64
- commit hash: 04eb5c8
- commit date: 2024-07-27
- overall geometric mean: 1.32x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x slower
- Memory change: 0.60x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 248 ms: 1.46x slower                                                  |
| docutils       | 1.50 sec                                               | 1.79 sec: 1.19x slower                                                |
| tornado_http   | 69.3 ms                                                | 94.5 ms: 1.36x slower                                                 |
| Geometric mean | (ref)                                                  | 1.34x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io_tg           | 669 ms                                                 | 495 ms: 1.35x faster                                                  |
| async_tree_none_tg         | 258 ms                                                 | 201 ms: 1.28x faster                                                  |
| async_tree_io              | 668 ms                                                 | 522 ms: 1.28x faster                                                  |
| async_tree_memoization_tg  | 323 ms                                                 | 256 ms: 1.26x faster                                                  |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 456 ms: 1.17x faster                                                  |
| async_tree_none            | 266 ms                                                 | 229 ms: 1.16x faster                                                  |
| async_tree_memoization     | 312 ms                                                 | 284 ms: 1.10x faster                                                  |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 483 ms: 1.09x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.21x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 282 ms                                                 | 281 ms: 1.00x faster                                                  |
| float          | 55.8 ms                                                | 93.2 ms: 1.67x slower                                                 |
| nbody          | 68.8 ms                                                | 154 ms: 2.24x slower                                                  |
| Geometric mean | (ref)                                                  | 1.55x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_dna      | 154 ms                                                 | 138 ms: 1.11x faster                                                  |
| regex_effbot   | 2.64 ms                                                | 2.59 ms: 1.02x faster                                                 |
| regex_v8       | 16.0 ms                                                | 17.5 ms: 1.10x slower                                                 |
| regex_compile  | 77.9 ms                                                | 122 ms: 1.57x slower                                                  |
| Geometric mean | (ref)                                                  | 1.11x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_parse      | 106 ms                                                 | 97.3 ms: 1.09x faster                                                 |
| xml_etree_iterparse  | 74.0 ms                                                | 75.8 ms: 1.02x slower                                                 |
| json_loads           | 17.2 us                                                | 19.1 us: 1.11x slower                                                 |
| xml_etree_generate   | 55.8 ms                                                | 69.1 ms: 1.24x slower                                                 |
| json_dumps           | 6.22 ms                                                | 7.90 ms: 1.27x slower                                                 |
| tomli_loads          | 1.39 sec                                               | 2.03 sec: 1.46x slower                                                |
| xml_etree_process    | 39.7 ms                                                | 59.5 ms: 1.50x slower                                                 |
| pickle_pure_python   | 200 us                                                 | 342 us: 1.71x slower                                                  |
| unpickle_pure_python | 151 us                                                 | 268 us: 1.78x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.30x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 9.37 ms                                                | 13.8 ms: 1.47x slower                                                 |
| python_startup         | 11.4 ms                                                | 17.0 ms: 1.49x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.48x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 22.3 ms                                                | 35.9 ms: 1.61x slower                                                 |
| mako            | 7.71 ms                                                | 13.6 ms: 1.77x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.69x slower                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| sqlglot_normalize          | 186 ms                                                 | 106 ms: 1.75x faster                                                  |
| async_tree_io_tg           | 669 ms                                                 | 495 ms: 1.35x faster                                                  |
| asyncio_tcp                | 449 ms                                                 | 350 ms: 1.28x faster                                                  |
| async_tree_none_tg         | 258 ms                                                 | 201 ms: 1.28x faster                                                  |
| async_tree_io              | 668 ms                                                 | 522 ms: 1.28x faster                                                  |
| async_tree_memoization_tg  | 323 ms                                                 | 256 ms: 1.26x faster                                                  |
| gc_traversal               | 2.40 ms                                                | 2.03 ms: 1.18x faster                                                 |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 456 ms: 1.17x faster                                                  |
| async_tree_none            | 266 ms                                                 | 229 ms: 1.16x faster                                                  |
| regex_dna                  | 154 ms                                                 | 138 ms: 1.11x faster                                                  |
| async_tree_memoization     | 312 ms                                                 | 284 ms: 1.10x faster                                                  |
| xml_etree_parse            | 106 ms                                                 | 97.3 ms: 1.09x faster                                                 |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 483 ms: 1.09x faster                                                  |
| create_gc_cycles           | 701 us                                                 | 656 us: 1.07x faster                                                  |
| regex_effbot               | 2.64 ms                                                | 2.59 ms: 1.02x faster                                                 |
| asyncio_websockets         | 409 ms                                                 | 403 ms: 1.02x faster                                                  |
| asyncio_tcp_ssl            | 1.24 sec                                               | 1.23 sec: 1.01x faster                                                |
| pidigits                   | 282 ms                                                 | 281 ms: 1.00x faster                                                  |
| xml_etree_iterparse        | 74.0 ms                                                | 75.8 ms: 1.02x slower                                                 |
| deepcopy                   | 235 us                                                 | 249 us: 1.06x slower                                                  |
| pathlib                    | 24.2 ms                                                | 25.9 ms: 1.07x slower                                                 |
| json                       | 3.09 ms                                                | 3.37 ms: 1.09x slower                                                 |
| regex_v8                   | 16.0 ms                                                | 17.5 ms: 1.10x slower                                                 |
| async_generators           | 304 ms                                                 | 336 ms: 1.11x slower                                                  |
| json_loads                 | 17.2 us                                                | 19.1 us: 1.11x slower                                                 |
| deepcopy_memo              | 27.7 us                                                | 31.3 us: 1.13x slower                                                 |
| generators                 | 31.1 ms                                                | 36.2 ms: 1.16x slower                                                 |
| mdp                        | 1.58 sec                                               | 1.85 sec: 1.17x slower                                                |
| docutils                   | 1.50 sec                                               | 1.79 sec: 1.19x slower                                                |
| coroutines                 | 19.2 ms                                                | 23.1 ms: 1.20x slower                                                 |
| deepcopy_reduce            | 2.07 us                                                | 2.53 us: 1.22x slower                                                 |
| bench_mp_pool              | 44.9 ms                                                | 55.4 ms: 1.23x slower                                                 |
| xml_etree_generate         | 55.8 ms                                                | 69.1 ms: 1.24x slower                                                 |
| meteor_contest             | 71.7 ms                                                | 88.8 ms: 1.24x slower                                                 |
| nqueens                    | 62.4 ms                                                | 77.5 ms: 1.24x slower                                                 |
| json_dumps                 | 6.22 ms                                                | 7.90 ms: 1.27x slower                                                 |
| comprehensions             | 14.5 us                                                | 18.9 us: 1.30x slower                                                 |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 4.13 ms: 1.32x slower                                                 |
| scimark_fft                | 195 ms                                                 | 266 ms: 1.36x slower                                                  |
| sympy_integrate            | 11.4 ms                                                | 15.5 ms: 1.36x slower                                                 |
| tornado_http               | 69.3 ms                                                | 94.5 ms: 1.36x slower                                                 |
| dulwich_log                | 29.8 ms                                                | 41.0 ms: 1.37x slower                                                 |
| pycparser                  | 677 ms                                                 | 933 ms: 1.38x slower                                                  |
| coverage                   | 38.9 ms                                                | 54.1 ms: 1.39x slower                                                 |
| fannkuch                   | 248 ms                                                 | 362 ms: 1.46x slower                                                  |
| tomli_loads                | 1.39 sec                                               | 2.03 sec: 1.46x slower                                                |
| 2to3                       | 169 ms                                                 | 248 ms: 1.46x slower                                                  |
| python_startup_no_site     | 9.37 ms                                                | 13.8 ms: 1.47x slower                                                 |
| python_startup             | 11.4 ms                                                | 17.0 ms: 1.49x slower                                                 |
| xml_etree_process          | 39.7 ms                                                | 59.5 ms: 1.50x slower                                                 |
| crypto_pyaes               | 51.9 ms                                                | 78.3 ms: 1.51x slower                                                 |
| pyflate                    | 316 ms                                                 | 482 ms: 1.53x slower                                                  |
| telco                      | 3.68 ms                                                | 5.65 ms: 1.54x slower                                                 |
| typing_runtime_protocols   | 93.0 us                                                | 145 us: 1.56x slower                                                  |
| sqlglot_optimize           | 34.0 ms                                                | 53.2 ms: 1.56x slower                                                 |
| regex_compile              | 77.9 ms                                                | 122 ms: 1.57x slower                                                  |
| bench_thread_pool          | 504 us                                                 | 791 us: 1.57x slower                                                  |
| sympy_str                  | 148 ms                                                 | 234 ms: 1.58x slower                                                  |
| django_template            | 22.3 ms                                                | 35.9 ms: 1.61x slower                                                 |
| logging_simple             | 3.69 us                                                | 6.07 us: 1.65x slower                                                 |
| logging_format             | 3.98 us                                                | 6.58 us: 1.65x slower                                                 |
| spectral_norm              | 76.4 ms                                                | 128 ms: 1.67x slower                                                  |
| float                      | 55.8 ms                                                | 93.2 ms: 1.67x slower                                                 |
| pprint_safe_repr           | 497 ms                                                 | 836 ms: 1.68x slower                                                  |
| pprint_pformat             | 1.01 sec                                               | 1.70 sec: 1.68x slower                                                |
| richards                   | 32.1 ms                                                | 54.2 ms: 1.69x slower                                                 |
| logging_silent             | 76.4 ns                                                | 130 ns: 1.70x slower                                                  |
| pickle_pure_python         | 200 us                                                 | 342 us: 1.71x slower                                                  |
| scimark_monte_carlo        | 45.0 ms                                                | 77.4 ms: 1.72x slower                                                 |
| hexiom                     | 4.54 ms                                                | 7.89 ms: 1.74x slower                                                 |
| raytrace                   | 212 ms                                                 | 368 ms: 1.74x slower                                                  |
| richards_super             | 36.0 ms                                                | 63.6 ms: 1.76x slower                                                 |
| mako                       | 7.71 ms                                                | 13.6 ms: 1.77x slower                                                 |
| chaos                      | 42.5 ms                                                | 75.5 ms: 1.77x slower                                                 |
| unpickle_pure_python       | 151 us                                                 | 268 us: 1.78x slower                                                  |
| scimark_sor                | 87.4 ms                                                | 157 ms: 1.79x slower                                                  |
| sympy_sum                  | 77.6 ms                                                | 139 ms: 1.79x slower                                                  |
| sympy_expand               | 241 ms                                                 | 438 ms: 1.82x slower                                                  |
| sqlglot_transpile          | 1.02 ms                                                | 1.89 ms: 1.85x slower                                                 |
| go                         | 102 ms                                                 | 192 ms: 1.89x slower                                                  |
| sqlglot_parse              | 848 us                                                 | 1.66 ms: 1.95x slower                                                 |
| scimark_lu                 | 76.0 ms                                                | 155 ms: 2.04x slower                                                  |
| deltablue                  | 2.71 ms                                                | 5.55 ms: 2.05x slower                                                 |
| nbody                      | 68.8 ms                                                | 154 ms: 2.24x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.32x slower                                                          |
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (14) of results/bm-20240727-3.14.0a0-04eb5c8-NOGIL/bm-20240727-darwin-arm64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.21x
- 95% likely to have a slowdown of 1.19x
- 99% likely to have a slowdown of 1.16x

# Memory
- memory change: 0.60x