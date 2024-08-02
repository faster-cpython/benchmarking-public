# Results vs. 3.12.0

- fork: python
- ref: e418fc3a6e7bade68ab5
- machine: darwin-arm64
- commit hash: e418fc3
- commit date: 2024-05-25
- overall geometric mean: 1.07x slower
- HPT reliability: 99.99%
- HPT 99th percentile: 1.03x slower
- Memory change: 0.70x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240525-darwin-arm64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 182 ms: 1.07x slower                                                  |
| chameleon      | 4.70 ms                                                | 4.99 ms: 1.06x slower                                                 |
| docutils       | 1.50 sec                                               | 1.68 sec: 1.12x slower                                                |
| Geometric mean | (ref)                                                  | 1.07x slower                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240525-darwin-arm64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none_tg         | 258 ms                                                 | 207 ms: 1.24x faster                                                  |
| async_tree_memoization_tg  | 323 ms                                                 | 261 ms: 1.24x faster                                                  |
| async_tree_io_tg           | 669 ms                                                 | 565 ms: 1.18x faster                                                  |
| async_tree_none            | 266 ms                                                 | 226 ms: 1.17x faster                                                  |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 459 ms: 1.16x faster                                                  |
| async_tree_io              | 668 ms                                                 | 587 ms: 1.14x faster                                                  |
| async_tree_memoization     | 312 ms                                                 | 279 ms: 1.12x faster                                                  |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 488 ms: 1.08x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.16x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240525-darwin-arm64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 282 ms                                                 | 283 ms: 1.00x slower                                                  |
| float          | 55.8 ms                                                | 61.3 ms: 1.10x slower                                                 |
| nbody          | 68.8 ms                                                | 76.1 ms: 1.11x slower                                                 |
| Geometric mean | (ref)                                                  | 1.07x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240525-darwin-arm64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_dna      | 154 ms                                                 | 149 ms: 1.03x faster                                                  |
| regex_effbot   | 2.64 ms                                                | 2.59 ms: 1.02x faster                                                 |
| regex_v8       | 16.0 ms                                                | 17.6 ms: 1.10x slower                                                 |
| regex_compile  | 77.9 ms                                                | 96.5 ms: 1.24x slower                                                 |
| Geometric mean | (ref)                                                  | 1.07x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240525-darwin-arm64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| unpickle_list        | 3.02 us                                                | 2.90 us: 1.04x faster                                                 |
| json_loads           | 17.2 us                                                | 17.0 us: 1.02x faster                                                 |
| pickle_dict          | 18.1 us                                                | 18.2 us: 1.01x slower                                                 |
| unpickle             | 9.12 us                                                | 9.28 us: 1.02x slower                                                 |
| pickle_list          | 2.89 us                                                | 2.95 us: 1.02x slower                                                 |
| pickle               | 7.23 us                                                | 7.41 us: 1.03x slower                                                 |
| xml_etree_iterparse  | 74.0 ms                                                | 76.6 ms: 1.03x slower                                                 |
| xml_etree_process    | 39.7 ms                                                | 41.4 ms: 1.04x slower                                                 |
| xml_etree_generate   | 55.8 ms                                                | 59.0 ms: 1.06x slower                                                 |
| json_dumps           | 6.22 ms                                                | 6.62 ms: 1.06x slower                                                 |
| pickle_pure_python   | 200 us                                                 | 228 us: 1.14x slower                                                  |
| tomli_loads          | 1.39 sec                                               | 1.65 sec: 1.19x slower                                                |
| unpickle_pure_python | 151 us                                                 | 179 us: 1.19x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.05x slower                                                          |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240525-darwin-arm64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 9.37 ms                                                | 12.0 ms: 1.28x slower                                                 |
| python_startup         | 11.4 ms                                                | 14.6 ms: 1.28x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.28x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240525-darwin-arm64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 22.3 ms                                                | 24.1 ms: 1.08x slower                                                 |
| mako            | 7.71 ms                                                | 9.12 ms: 1.18x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.13x slower                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240525-darwin-arm64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| generators                 | 31.1 ms                                                | 23.4 ms: 1.33x faster                                                 |
| async_tree_none_tg         | 258 ms                                                 | 207 ms: 1.24x faster                                                  |
| async_tree_memoization_tg  | 323 ms                                                 | 261 ms: 1.24x faster                                                  |
| raytrace                   | 212 ms                                                 | 178 ms: 1.19x faster                                                  |
| async_tree_io_tg           | 669 ms                                                 | 565 ms: 1.18x faster                                                  |
| async_tree_none            | 266 ms                                                 | 226 ms: 1.17x faster                                                  |
| coroutines                 | 19.2 ms                                                | 16.6 ms: 1.16x faster                                                 |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 459 ms: 1.16x faster                                                  |
| async_tree_io              | 668 ms                                                 | 587 ms: 1.14x faster                                                  |
| logging_simple             | 3.69 us                                                | 3.25 us: 1.14x faster                                                 |
| logging_format             | 3.98 us                                                | 3.56 us: 1.12x faster                                                 |
| async_tree_memoization     | 312 ms                                                 | 279 ms: 1.12x faster                                                  |
| asyncio_tcp                | 449 ms                                                 | 406 ms: 1.11x faster                                                  |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 488 ms: 1.08x faster                                                  |
| pathlib                    | 24.2 ms                                                | 23.0 ms: 1.05x faster                                                 |
| unpickle_list              | 3.02 us                                                | 2.90 us: 1.04x faster                                                 |
| json                       | 3.09 ms                                                | 2.98 ms: 1.04x faster                                                 |
| regex_dna                  | 154 ms                                                 | 149 ms: 1.03x faster                                                  |
| async_generators           | 304 ms                                                 | 295 ms: 1.03x faster                                                  |
| regex_effbot               | 2.64 ms                                                | 2.59 ms: 1.02x faster                                                 |
| json_loads                 | 17.2 us                                                | 17.0 us: 1.02x faster                                                 |
| pidigits                   | 282 ms                                                 | 283 ms: 1.00x slower                                                  |
| pickle_dict                | 18.1 us                                                | 18.2 us: 1.01x slower                                                 |
| unpickle                   | 9.12 us                                                | 9.28 us: 1.02x slower                                                 |
| pickle_list                | 2.89 us                                                | 2.95 us: 1.02x slower                                                 |
| pickle                     | 7.23 us                                                | 7.41 us: 1.03x slower                                                 |
| sqlite_synth               | 1.57 us                                                | 1.61 us: 1.03x slower                                                 |
| dask                       | 222 ms                                                 | 228 ms: 1.03x slower                                                  |
| gc_traversal               | 2.40 ms                                                | 2.47 ms: 1.03x slower                                                 |
| xml_etree_iterparse        | 74.0 ms                                                | 76.6 ms: 1.03x slower                                                 |
| asyncio_tcp_ssl            | 1.24 sec                                               | 1.29 sec: 1.04x slower                                                |
| deepcopy_reduce            | 2.07 us                                                | 2.15 us: 1.04x slower                                                 |
| mdp                        | 1.58 sec                                               | 1.65 sec: 1.04x slower                                                |
| xml_etree_process          | 39.7 ms                                                | 41.4 ms: 1.04x slower                                                 |
| xml_etree_generate         | 55.8 ms                                                | 59.0 ms: 1.06x slower                                                 |
| bench_thread_pool          | 504 us                                                 | 533 us: 1.06x slower                                                  |
| bench_mp_pool              | 44.9 ms                                                | 47.5 ms: 1.06x slower                                                 |
| chameleon                  | 4.70 ms                                                | 4.99 ms: 1.06x slower                                                 |
| json_dumps                 | 6.22 ms                                                | 6.62 ms: 1.06x slower                                                 |
| 2to3                       | 169 ms                                                 | 182 ms: 1.07x slower                                                  |
| deepcopy                   | 235 us                                                 | 253 us: 1.08x slower                                                  |
| django_template            | 22.3 ms                                                | 24.1 ms: 1.08x slower                                                 |
| pycparser                  | 677 ms                                                 | 731 ms: 1.08x slower                                                  |
| deltablue                  | 2.71 ms                                                | 2.93 ms: 1.08x slower                                                 |
| float                      | 55.8 ms                                                | 61.3 ms: 1.10x slower                                                 |
| chaos                      | 42.5 ms                                                | 46.8 ms: 1.10x slower                                                 |
| regex_v8                   | 16.0 ms                                                | 17.6 ms: 1.10x slower                                                 |
| sqlglot_optimize           | 34.0 ms                                                | 37.6 ms: 1.10x slower                                                 |
| sympy_expand               | 241 ms                                                 | 266 ms: 1.10x slower                                                  |
| nbody                      | 68.8 ms                                                | 76.1 ms: 1.11x slower                                                 |
| nqueens                    | 62.4 ms                                                | 69.1 ms: 1.11x slower                                                 |
| sympy_integrate            | 11.4 ms                                                | 12.7 ms: 1.12x slower                                                 |
| meteor_contest             | 71.7 ms                                                | 80.1 ms: 1.12x slower                                                 |
| docutils                   | 1.50 sec                                               | 1.68 sec: 1.12x slower                                                |
| sympy_str                  | 148 ms                                                 | 166 ms: 1.12x slower                                                  |
| sympy_sum                  | 77.6 ms                                                | 87.2 ms: 1.12x slower                                                 |
| sqlglot_parse              | 848 us                                                 | 958 us: 1.13x slower                                                  |
| sqlglot_transpile          | 1.02 ms                                                | 1.16 ms: 1.13x slower                                                 |
| richards_super             | 36.0 ms                                                | 40.9 ms: 1.14x slower                                                 |
| pickle_pure_python         | 200 us                                                 | 228 us: 1.14x slower                                                  |
| scimark_fft                | 195 ms                                                 | 223 ms: 1.14x slower                                                  |
| go                         | 102 ms                                                 | 117 ms: 1.15x slower                                                  |
| pprint_safe_repr           | 497 ms                                                 | 576 ms: 1.16x slower                                                  |
| richards                   | 32.1 ms                                                | 37.3 ms: 1.16x slower                                                 |
| pprint_pformat             | 1.01 sec                                               | 1.18 sec: 1.16x slower                                                |
| typing_runtime_protocols   | 93.0 us                                                | 109 us: 1.17x slower                                                  |
| deepcopy_memo              | 27.7 us                                                | 32.6 us: 1.18x slower                                                 |
| crypto_pyaes               | 51.9 ms                                                | 61.3 ms: 1.18x slower                                                 |
| mako                       | 7.71 ms                                                | 9.12 ms: 1.18x slower                                                 |
| tomli_loads                | 1.39 sec                                               | 1.65 sec: 1.19x slower                                                |
| unpickle_pure_python       | 151 us                                                 | 179 us: 1.19x slower                                                  |
| coverage                   | 38.9 ms                                                | 46.2 ms: 1.19x slower                                                 |
| comprehensions             | 14.5 us                                                | 17.5 us: 1.20x slower                                                 |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 3.82 ms: 1.22x slower                                                 |
| scimark_sor                | 87.4 ms                                                | 107 ms: 1.22x slower                                                  |
| spectral_norm              | 76.4 ms                                                | 94.6 ms: 1.24x slower                                                 |
| regex_compile              | 77.9 ms                                                | 96.5 ms: 1.24x slower                                                 |
| logging_silent             | 76.4 ns                                                | 95.9 ns: 1.25x slower                                                 |
| pyflate                    | 316 ms                                                 | 399 ms: 1.27x slower                                                  |
| python_startup_no_site     | 9.37 ms                                                | 12.0 ms: 1.28x slower                                                 |
| python_startup             | 11.4 ms                                                | 14.6 ms: 1.28x slower                                                 |
| fannkuch                   | 248 ms                                                 | 319 ms: 1.28x slower                                                  |
| create_gc_cycles           | 701 us                                                 | 905 us: 1.29x slower                                                  |
| scimark_lu                 | 76.0 ms                                                | 100.0 ms: 1.32x slower                                                |
| hexiom                     | 4.54 ms                                                | 5.98 ms: 1.32x slower                                                 |
| scimark_monte_carlo        | 45.0 ms                                                | 61.4 ms: 1.36x slower                                                 |
| telco                      | 3.68 ms                                                | 5.05 ms: 1.37x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.07x slower                                                          |

Benchmark hidden because not significant (3): asyncio_websockets, xml_etree_parse, tornado_http
Ignored benchmarks (8) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, dulwich_log, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, unpack_sequence
Ignored benchmarks (14) of results/bm-20240525-3.14.0a0-e418fc3-PYTHON_UOPS/bm-20240525-darwin-arm64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.99% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: 0.70x