# Results vs. 3.12.0

- fork: python
- ref: a2bec77d25b11f50362a
- machine: darwin-arm64
- commit hash: a2bec77
- commit date: 2024-07-13
- overall geometric mean: 1.34x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x slower
- Memory change: 1.16x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 250 ms: 1.48x slower                                                  |
| docutils       | 1.50 sec                                               | 1.80 sec: 1.20x slower                                                |
| tornado_http   | 69.3 ms                                                | 96.0 ms: 1.38x slower                                                 |
| Geometric mean | (ref)                                                  | 1.35x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io_tg           | 669 ms                                                 | 507 ms: 1.32x faster                                                  |
| async_tree_io              | 668 ms                                                 | 538 ms: 1.24x faster                                                  |
| async_tree_none_tg         | 258 ms                                                 | 208 ms: 1.24x faster                                                  |
| async_tree_memoization_tg  | 323 ms                                                 | 265 ms: 1.22x faster                                                  |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 465 ms: 1.15x faster                                                  |
| async_tree_none            | 266 ms                                                 | 235 ms: 1.13x faster                                                  |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 491 ms: 1.07x faster                                                  |
| async_tree_memoization     | 312 ms                                                 | 292 ms: 1.07x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.18x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 282 ms                                                 | 281 ms: 1.00x faster                                                  |
| float          | 55.8 ms                                                | 96.6 ms: 1.73x slower                                                 |
| nbody          | 68.8 ms                                                | 159 ms: 2.31x slower                                                  |
| Geometric mean | (ref)                                                  | 1.59x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_dna      | 154 ms                                                 | 139 ms: 1.11x faster                                                  |
| regex_effbot   | 2.64 ms                                                | 2.43 ms: 1.09x faster                                                 |
| regex_v8       | 16.0 ms                                                | 17.5 ms: 1.10x slower                                                 |
| regex_compile  | 77.9 ms                                                | 125 ms: 1.60x slower                                                  |
| Geometric mean | (ref)                                                  | 1.10x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_parse      | 106 ms                                                 | 98.9 ms: 1.08x faster                                                 |
| xml_etree_iterparse  | 74.0 ms                                                | 76.8 ms: 1.04x slower                                                 |
| json_loads           | 17.2 us                                                | 19.3 us: 1.12x slower                                                 |
| xml_etree_generate   | 55.8 ms                                                | 70.7 ms: 1.27x slower                                                 |
| json_dumps           | 6.22 ms                                                | 8.14 ms: 1.31x slower                                                 |
| tomli_loads          | 1.39 sec                                               | 2.06 sec: 1.48x slower                                                |
| xml_etree_process    | 39.7 ms                                                | 60.9 ms: 1.54x slower                                                 |
| pickle_pure_python   | 200 us                                                 | 346 us: 1.73x slower                                                  |
| unpickle_pure_python | 151 us                                                 | 269 us: 1.79x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.33x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 9.37 ms                                                | 14.0 ms: 1.49x slower                                                 |
| python_startup         | 11.4 ms                                                | 17.3 ms: 1.51x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.50x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 22.3 ms                                                | 35.9 ms: 1.61x slower                                                 |
| mako            | 7.71 ms                                                | 13.4 ms: 1.74x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.67x slower                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| sqlglot_normalize          | 186 ms                                                 | 109 ms: 1.70x faster                                                  |
| async_tree_io_tg           | 669 ms                                                 | 507 ms: 1.32x faster                                                  |
| asyncio_tcp                | 449 ms                                                 | 353 ms: 1.27x faster                                                  |
| async_tree_io              | 668 ms                                                 | 538 ms: 1.24x faster                                                  |
| async_tree_none_tg         | 258 ms                                                 | 208 ms: 1.24x faster                                                  |
| async_tree_memoization_tg  | 323 ms                                                 | 265 ms: 1.22x faster                                                  |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 465 ms: 1.15x faster                                                  |
| gc_traversal               | 2.40 ms                                                | 2.11 ms: 1.14x faster                                                 |
| async_tree_none            | 266 ms                                                 | 235 ms: 1.13x faster                                                  |
| regex_dna                  | 154 ms                                                 | 139 ms: 1.11x faster                                                  |
| regex_effbot               | 2.64 ms                                                | 2.43 ms: 1.09x faster                                                 |
| xml_etree_parse            | 106 ms                                                 | 98.9 ms: 1.08x faster                                                 |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 491 ms: 1.07x faster                                                  |
| async_tree_memoization     | 312 ms                                                 | 292 ms: 1.07x faster                                                  |
| create_gc_cycles           | 701 us                                                 | 665 us: 1.05x faster                                                  |
| asyncio_websockets         | 409 ms                                                 | 406 ms: 1.01x faster                                                  |
| pidigits                   | 282 ms                                                 | 281 ms: 1.00x faster                                                  |
| xml_etree_iterparse        | 74.0 ms                                                | 76.8 ms: 1.04x slower                                                 |
| pathlib                    | 24.2 ms                                                | 25.9 ms: 1.07x slower                                                 |
| deepcopy                   | 235 us                                                 | 252 us: 1.07x slower                                                  |
| regex_v8                   | 16.0 ms                                                | 17.5 ms: 1.10x slower                                                 |
| json                       | 3.09 ms                                                | 3.42 ms: 1.11x slower                                                 |
| deepcopy_memo              | 27.7 us                                                | 30.9 us: 1.12x slower                                                 |
| json_loads                 | 17.2 us                                                | 19.3 us: 1.12x slower                                                 |
| async_generators           | 304 ms                                                 | 343 ms: 1.13x slower                                                  |
| generators                 | 31.1 ms                                                | 37.0 ms: 1.19x slower                                                 |
| mdp                        | 1.58 sec                                               | 1.88 sec: 1.19x slower                                                |
| docutils                   | 1.50 sec                                               | 1.80 sec: 1.20x slower                                                |
| coroutines                 | 19.2 ms                                                | 23.1 ms: 1.20x slower                                                 |
| bench_mp_pool              | 44.9 ms                                                | 54.6 ms: 1.22x slower                                                 |
| deepcopy_reduce            | 2.07 us                                                | 2.55 us: 1.23x slower                                                 |
| xml_etree_generate         | 55.8 ms                                                | 70.7 ms: 1.27x slower                                                 |
| nqueens                    | 62.4 ms                                                | 79.2 ms: 1.27x slower                                                 |
| meteor_contest             | 71.7 ms                                                | 91.5 ms: 1.28x slower                                                 |
| json_dumps                 | 6.22 ms                                                | 8.14 ms: 1.31x slower                                                 |
| comprehensions             | 14.5 us                                                | 19.3 us: 1.33x slower                                                 |
| tornado_http               | 69.3 ms                                                | 96.0 ms: 1.38x slower                                                 |
| sympy_integrate            | 11.4 ms                                                | 15.8 ms: 1.39x slower                                                 |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 4.35 ms: 1.39x slower                                                 |
| pycparser                  | 677 ms                                                 | 955 ms: 1.41x slower                                                  |
| scimark_fft                | 195 ms                                                 | 277 ms: 1.42x slower                                                  |
| fannkuch                   | 248 ms                                                 | 359 ms: 1.44x slower                                                  |
| coverage                   | 38.9 ms                                                | 56.5 ms: 1.45x slower                                                 |
| 2to3                       | 169 ms                                                 | 250 ms: 1.48x slower                                                  |
| tomli_loads                | 1.39 sec                                               | 2.06 sec: 1.48x slower                                                |
| python_startup_no_site     | 9.37 ms                                                | 14.0 ms: 1.49x slower                                                 |
| telco                      | 3.68 ms                                                | 5.53 ms: 1.50x slower                                                 |
| python_startup             | 11.4 ms                                                | 17.3 ms: 1.51x slower                                                 |
| pyflate                    | 316 ms                                                 | 482 ms: 1.53x slower                                                  |
| crypto_pyaes               | 51.9 ms                                                | 79.5 ms: 1.53x slower                                                 |
| xml_etree_process          | 39.7 ms                                                | 60.9 ms: 1.54x slower                                                 |
| bench_thread_pool          | 504 us                                                 | 790 us: 1.57x slower                                                  |
| spectral_norm              | 76.4 ms                                                | 122 ms: 1.59x slower                                                  |
| typing_runtime_protocols   | 93.0 us                                                | 149 us: 1.60x slower                                                  |
| sqlglot_optimize           | 34.0 ms                                                | 54.4 ms: 1.60x slower                                                 |
| regex_compile              | 77.9 ms                                                | 125 ms: 1.60x slower                                                  |
| django_template            | 22.3 ms                                                | 35.9 ms: 1.61x slower                                                 |
| sympy_str                  | 148 ms                                                 | 238 ms: 1.61x slower                                                  |
| logging_simple             | 3.69 us                                                | 6.16 us: 1.67x slower                                                 |
| logging_format             | 3.98 us                                                | 6.72 us: 1.69x slower                                                 |
| pprint_safe_repr           | 497 ms                                                 | 851 ms: 1.71x slower                                                  |
| pprint_pformat             | 1.01 sec                                               | 1.73 sec: 1.71x slower                                                |
| float                      | 55.8 ms                                                | 96.6 ms: 1.73x slower                                                 |
| pickle_pure_python         | 200 us                                                 | 346 us: 1.73x slower                                                  |
| mako                       | 7.71 ms                                                | 13.4 ms: 1.74x slower                                                 |
| raytrace                   | 212 ms                                                 | 373 ms: 1.76x slower                                                  |
| logging_silent             | 76.4 ns                                                | 135 ns: 1.76x slower                                                  |
| hexiom                     | 4.54 ms                                                | 8.02 ms: 1.77x slower                                                 |
| richards                   | 32.1 ms                                                | 56.8 ms: 1.77x slower                                                 |
| unpickle_pure_python       | 151 us                                                 | 269 us: 1.79x slower                                                  |
| scimark_monte_carlo        | 45.0 ms                                                | 80.5 ms: 1.79x slower                                                 |
| chaos                      | 42.5 ms                                                | 76.5 ms: 1.80x slower                                                 |
| sympy_sum                  | 77.6 ms                                                | 141 ms: 1.82x slower                                                  |
| scimark_sor                | 87.4 ms                                                | 160 ms: 1.83x slower                                                  |
| sympy_expand               | 241 ms                                                 | 444 ms: 1.84x slower                                                  |
| richards_super             | 36.0 ms                                                | 66.5 ms: 1.84x slower                                                 |
| sqlglot_transpile          | 1.02 ms                                                | 1.95 ms: 1.91x slower                                                 |
| go                         | 102 ms                                                 | 200 ms: 1.97x slower                                                  |
| sqlglot_parse              | 848 us                                                 | 1.71 ms: 2.01x slower                                                 |
| scimark_lu                 | 76.0 ms                                                | 159 ms: 2.10x slower                                                  |
| deltablue                  | 2.71 ms                                                | 5.76 ms: 2.13x slower                                                 |
| nbody                      | 68.8 ms                                                | 159 ms: 2.31x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.34x slower                                                          |

Benchmark hidden because not significant (1): asyncio_tcp_ssl
Ignored benchmarks (15) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (14) of results/bm-20240713-3.14.0a0-a2bec77-NOGIL/bm-20240713-darwin-arm64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.26x
- 95% likely to have a slowdown of 1.22x
- 99% likely to have a slowdown of 1.19x

# Memory
- memory change: 1.16x