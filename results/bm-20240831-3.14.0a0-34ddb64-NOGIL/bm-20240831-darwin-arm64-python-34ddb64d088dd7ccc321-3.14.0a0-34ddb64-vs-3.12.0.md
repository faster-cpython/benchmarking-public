# Results vs. 3.12.0

- fork: python
- ref: 34ddb64d088dd7ccc321
- machine: darwin-arm64
- commit hash: 34ddb64
- commit date: 2024-08-31
- overall geometric mean: 1.36x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x slower
- Memory change: 0.69x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 254 ms: 1.50x slower                                                  |
| docutils       | 1.50 sec                                               | 1.79 sec: 1.19x slower                                                |
| tornado_http   | 69.3 ms                                                | 110 ms: 1.59x slower                                                  |
| Geometric mean | (ref)                                                  | 1.42x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io_tg           | 669 ms                                                 | 521 ms: 1.28x faster                                                  |
| async_tree_io              | 668 ms                                                 | 550 ms: 1.22x faster                                                  |
| async_tree_none_tg         | 258 ms                                                 | 216 ms: 1.19x faster                                                  |
| async_tree_memoization_tg  | 323 ms                                                 | 274 ms: 1.18x faster                                                  |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 476 ms: 1.12x faster                                                  |
| async_tree_none            | 266 ms                                                 | 243 ms: 1.09x faster                                                  |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 504 ms: 1.04x faster                                                  |
| async_tree_memoization     | 312 ms                                                 | 300 ms: 1.04x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.14x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 282 ms                                                 | 281 ms: 1.00x faster                                                  |
| float          | 55.8 ms                                                | 98.7 ms: 1.77x slower                                                 |
| nbody          | 68.8 ms                                                | 159 ms: 2.31x slower                                                  |
| Geometric mean | (ref)                                                  | 1.60x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_dna      | 154 ms                                                 | 139 ms: 1.11x faster                                                  |
| regex_effbot   | 2.64 ms                                                | 2.45 ms: 1.08x faster                                                 |
| regex_v8       | 16.0 ms                                                | 17.4 ms: 1.09x slower                                                 |
| regex_compile  | 77.9 ms                                                | 125 ms: 1.61x slower                                                  |
| Geometric mean | (ref)                                                  | 1.10x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_parse      | 106 ms                                                 | 105 ms: 1.01x faster                                                  |
| xml_etree_iterparse  | 74.0 ms                                                | 78.2 ms: 1.06x slower                                                 |
| json_loads           | 17.2 us                                                | 19.4 us: 1.13x slower                                                 |
| xml_etree_generate   | 55.8 ms                                                | 71.9 ms: 1.29x slower                                                 |
| json_dumps           | 6.22 ms                                                | 8.12 ms: 1.31x slower                                                 |
| tomli_loads          | 1.39 sec                                               | 2.07 sec: 1.49x slower                                                |
| xml_etree_process    | 39.7 ms                                                | 59.8 ms: 1.51x slower                                                 |
| pickle_pure_python   | 200 us                                                 | 365 us: 1.82x slower                                                  |
| unpickle_pure_python | 151 us                                                 | 280 us: 1.86x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.35x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 9.37 ms                                                | 15.6 ms: 1.67x slower                                                 |
| python_startup         | 11.4 ms                                                | 19.2 ms: 1.68x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.68x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 22.3 ms                                                | 37.9 ms: 1.70x slower                                                 |
| mako            | 7.71 ms                                                | 13.7 ms: 1.78x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.74x slower                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| sqlglot_normalize          | 186 ms                                                 | 110 ms: 1.69x faster                                                  |
| async_tree_io_tg           | 669 ms                                                 | 521 ms: 1.28x faster                                                  |
| asyncio_tcp                | 449 ms                                                 | 352 ms: 1.28x faster                                                  |
| async_tree_io              | 668 ms                                                 | 550 ms: 1.22x faster                                                  |
| async_tree_none_tg         | 258 ms                                                 | 216 ms: 1.19x faster                                                  |
| async_tree_memoization_tg  | 323 ms                                                 | 274 ms: 1.18x faster                                                  |
| gc_traversal               | 2.40 ms                                                | 2.05 ms: 1.17x faster                                                 |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 476 ms: 1.12x faster                                                  |
| regex_dna                  | 154 ms                                                 | 139 ms: 1.11x faster                                                  |
| async_tree_none            | 266 ms                                                 | 243 ms: 1.09x faster                                                  |
| regex_effbot               | 2.64 ms                                                | 2.45 ms: 1.08x faster                                                 |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 504 ms: 1.04x faster                                                  |
| async_tree_memoization     | 312 ms                                                 | 300 ms: 1.04x faster                                                  |
| xml_etree_parse            | 106 ms                                                 | 105 ms: 1.01x faster                                                  |
| asyncio_websockets         | 409 ms                                                 | 405 ms: 1.01x faster                                                  |
| create_gc_cycles           | 701 us                                                 | 696 us: 1.01x faster                                                  |
| pidigits                   | 282 ms                                                 | 281 ms: 1.00x faster                                                  |
| xml_etree_iterparse        | 74.0 ms                                                | 78.2 ms: 1.06x slower                                                 |
| regex_v8                   | 16.0 ms                                                | 17.4 ms: 1.09x slower                                                 |
| deepcopy                   | 235 us                                                 | 256 us: 1.09x slower                                                  |
| pathlib                    | 24.2 ms                                                | 26.5 ms: 1.09x slower                                                 |
| async_generators           | 304 ms                                                 | 336 ms: 1.10x slower                                                  |
| json                       | 3.09 ms                                                | 3.42 ms: 1.11x slower                                                 |
| json_loads                 | 17.2 us                                                | 19.4 us: 1.13x slower                                                 |
| generators                 | 31.1 ms                                                | 35.3 ms: 1.14x slower                                                 |
| deepcopy_memo              | 27.7 us                                                | 32.4 us: 1.17x slower                                                 |
| mdp                        | 1.58 sec                                               | 1.87 sec: 1.18x slower                                                |
| docutils                   | 1.50 sec                                               | 1.79 sec: 1.19x slower                                                |
| deepcopy_reduce            | 2.07 us                                                | 2.57 us: 1.24x slower                                                 |
| meteor_contest             | 71.7 ms                                                | 89.9 ms: 1.25x slower                                                 |
| nqueens                    | 62.4 ms                                                | 78.7 ms: 1.26x slower                                                 |
| bench_mp_pool              | 44.9 ms                                                | 56.7 ms: 1.26x slower                                                 |
| xml_etree_generate         | 55.8 ms                                                | 71.9 ms: 1.29x slower                                                 |
| json_dumps                 | 6.22 ms                                                | 8.12 ms: 1.31x slower                                                 |
| comprehensions             | 14.5 us                                                | 19.3 us: 1.32x slower                                                 |
| coroutines                 | 19.2 ms                                                | 26.0 ms: 1.35x slower                                                 |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 4.32 ms: 1.38x slower                                                 |
| sympy_integrate            | 11.4 ms                                                | 16.0 ms: 1.41x slower                                                 |
| dulwich_log                | 29.8 ms                                                | 42.1 ms: 1.41x slower                                                 |
| pycparser                  | 677 ms                                                 | 961 ms: 1.42x slower                                                  |
| scimark_fft                | 195 ms                                                 | 279 ms: 1.43x slower                                                  |
| fannkuch                   | 248 ms                                                 | 358 ms: 1.44x slower                                                  |
| coverage                   | 38.9 ms                                                | 56.8 ms: 1.46x slower                                                 |
| tomli_loads                | 1.39 sec                                               | 2.07 sec: 1.49x slower                                                |
| 2to3                       | 169 ms                                                 | 254 ms: 1.50x slower                                                  |
| xml_etree_process          | 39.7 ms                                                | 59.8 ms: 1.51x slower                                                 |
| crypto_pyaes               | 51.9 ms                                                | 78.9 ms: 1.52x slower                                                 |
| pyflate                    | 316 ms                                                 | 489 ms: 1.55x slower                                                  |
| tornado_http               | 69.3 ms                                                | 110 ms: 1.59x slower                                                  |
| sympy_str                  | 148 ms                                                 | 236 ms: 1.60x slower                                                  |
| bench_thread_pool          | 504 us                                                 | 810 us: 1.61x slower                                                  |
| regex_compile              | 77.9 ms                                                | 125 ms: 1.61x slower                                                  |
| sqlglot_optimize           | 34.0 ms                                                | 55.0 ms: 1.61x slower                                                 |
| typing_runtime_protocols   | 93.0 us                                                | 151 us: 1.62x slower                                                  |
| telco                      | 3.68 ms                                                | 5.99 ms: 1.63x slower                                                 |
| python_startup_no_site     | 9.37 ms                                                | 15.6 ms: 1.67x slower                                                 |
| python_startup             | 11.4 ms                                                | 19.2 ms: 1.68x slower                                                 |
| django_template            | 22.3 ms                                                | 37.9 ms: 1.70x slower                                                 |
| logging_simple             | 3.69 us                                                | 6.34 us: 1.72x slower                                                 |
| pprint_pformat             | 1.01 sec                                               | 1.74 sec: 1.72x slower                                                |
| pprint_safe_repr           | 497 ms                                                 | 859 ms: 1.73x slower                                                  |
| logging_format             | 3.98 us                                                | 6.92 us: 1.74x slower                                                 |
| hexiom                     | 4.54 ms                                                | 7.94 ms: 1.75x slower                                                 |
| spectral_norm              | 76.4 ms                                                | 134 ms: 1.75x slower                                                  |
| float                      | 55.8 ms                                                | 98.7 ms: 1.77x slower                                                 |
| mako                       | 7.71 ms                                                | 13.7 ms: 1.78x slower                                                 |
| sympy_expand               | 241 ms                                                 | 438 ms: 1.82x slower                                                  |
| sympy_sum                  | 77.6 ms                                                | 142 ms: 1.82x slower                                                  |
| pickle_pure_python         | 200 us                                                 | 365 us: 1.82x slower                                                  |
| richards                   | 32.1 ms                                                | 58.8 ms: 1.83x slower                                                 |
| go                         | 102 ms                                                 | 186 ms: 1.84x slower                                                  |
| scimark_monte_carlo        | 45.0 ms                                                | 82.6 ms: 1.84x slower                                                 |
| raytrace                   | 212 ms                                                 | 390 ms: 1.84x slower                                                  |
| chaos                      | 42.5 ms                                                | 78.5 ms: 1.85x slower                                                 |
| unpickle_pure_python       | 151 us                                                 | 280 us: 1.86x slower                                                  |
| logging_silent             | 76.4 ns                                                | 143 ns: 1.87x slower                                                  |
| richards_super             | 36.0 ms                                                | 68.3 ms: 1.89x slower                                                 |
| scimark_sor                | 87.4 ms                                                | 167 ms: 1.91x slower                                                  |
| sqlglot_transpile          | 1.02 ms                                                | 1.97 ms: 1.93x slower                                                 |
| sqlglot_parse              | 848 us                                                 | 1.72 ms: 2.03x slower                                                 |
| scimark_lu                 | 76.0 ms                                                | 158 ms: 2.08x slower                                                  |
| deltablue                  | 2.71 ms                                                | 5.96 ms: 2.20x slower                                                 |
| nbody                      | 68.8 ms                                                | 159 ms: 2.31x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.36x slower                                                          |

Benchmark hidden because not significant (1): asyncio_tcp_ssl
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (14) of results/bm-20240831-3.14.0a0-34ddb64-NOGIL/bm-20240831-darwin-arm64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.27x
- 95% likely to have a slowdown of 1.24x
- 99% likely to have a slowdown of 1.19x

# Memory
- memory change: 0.69x