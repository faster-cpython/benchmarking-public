# Results vs. 3.12.0

- fork: python
- ref: main
- machine: darwin-arm64
- commit hash: 315a933
- commit date: 2024-08-14
- overall geometric mean: 1.06x slower
- HPT reliability: 99.87%
- HPT 99th percentile: 1.02x slower
- Memory change: 0.47x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240814-darwin-arm64-python-main-3.14.0a0-315a933 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| 2to3           | 169 ms                                                 | 186 ms: 1.10x slower                                  |
| docutils       | 1.50 sec                                               | 1.70 sec: 1.13x slower                                |
| Geometric mean | (ref)                                                  | 1.08x slower                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240814-darwin-arm64-python-main-3.14.0a0-315a933 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| async_tree_memoization_tg  | 323 ms                                                 | 235 ms: 1.37x faster                                  |
| async_tree_none_tg         | 258 ms                                                 | 190 ms: 1.36x faster                                  |
| async_tree_none            | 266 ms                                                 | 205 ms: 1.30x faster                                  |
| async_tree_io_tg           | 669 ms                                                 | 525 ms: 1.27x faster                                  |
| async_tree_memoization     | 312 ms                                                 | 251 ms: 1.24x faster                                  |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 449 ms: 1.19x faster                                  |
| async_tree_io              | 668 ms                                                 | 577 ms: 1.16x faster                                  |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 459 ms: 1.15x faster                                  |
| Geometric mean             | (ref)                                                  | 1.25x faster                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240814-darwin-arm64-python-main-3.14.0a0-315a933 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| float          | 55.8 ms                                                | 55.5 ms: 1.00x faster                                 |
| pidigits       | 282 ms                                                 | 283 ms: 1.00x slower                                  |
| nbody          | 68.8 ms                                                | 75.9 ms: 1.10x slower                                 |
| Geometric mean | (ref)                                                  | 1.03x slower                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240814-darwin-arm64-python-main-3.14.0a0-315a933 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| regex_effbot   | 2.64 ms                                                | 2.48 ms: 1.07x faster                                 |
| regex_dna      | 154 ms                                                 | 145 ms: 1.06x faster                                  |
| regex_v8       | 16.0 ms                                                | 16.8 ms: 1.05x slower                                 |
| regex_compile  | 77.9 ms                                                | 94.5 ms: 1.21x slower                                 |
| Geometric mean | (ref)                                                  | 1.03x slower                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240814-darwin-arm64-python-main-3.14.0a0-315a933 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| json_loads           | 17.2 us                                                | 17.3 us: 1.00x slower                                 |
| xml_etree_parse      | 106 ms                                                 | 111 ms: 1.04x slower                                  |
| xml_etree_iterparse  | 74.0 ms                                                | 78.1 ms: 1.05x slower                                 |
| xml_etree_process    | 39.7 ms                                                | 41.9 ms: 1.06x slower                                 |
| pickle_pure_python   | 200 us                                                 | 213 us: 1.07x slower                                  |
| json_dumps           | 6.22 ms                                                | 6.65 ms: 1.07x slower                                 |
| xml_etree_generate   | 55.8 ms                                                | 60.5 ms: 1.08x slower                                 |
| unpickle_pure_python | 151 us                                                 | 165 us: 1.10x slower                                  |
| tomli_loads          | 1.39 sec                                               | 1.59 sec: 1.14x slower                                |
| Geometric mean       | (ref)                                                  | 1.07x slower                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240814-darwin-arm64-python-main-3.14.0a0-315a933 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup_no_site | 9.37 ms                                                | 13.9 ms: 1.48x slower                                 |
| python_startup         | 11.4 ms                                                | 16.9 ms: 1.48x slower                                 |
| Geometric mean         | (ref)                                                  | 1.48x slower                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240814-darwin-arm64-python-main-3.14.0a0-315a933 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| django_template | 22.3 ms                                                | 24.1 ms: 1.08x slower                                 |
| mako            | 7.71 ms                                                | 9.09 ms: 1.18x slower                                 |
| Geometric mean  | (ref)                                                  | 1.13x slower                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240814-darwin-arm64-python-main-3.14.0a0-315a933 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| async_tree_memoization_tg  | 323 ms                                                 | 235 ms: 1.37x faster                                  |
| async_tree_none_tg         | 258 ms                                                 | 190 ms: 1.36x faster                                  |
| async_tree_none            | 266 ms                                                 | 205 ms: 1.30x faster                                  |
| async_tree_io_tg           | 669 ms                                                 | 525 ms: 1.27x faster                                  |
| deepcopy                   | 235 us                                                 | 185 us: 1.27x faster                                  |
| async_tree_memoization     | 312 ms                                                 | 251 ms: 1.24x faster                                  |
| raytrace                   | 212 ms                                                 | 173 ms: 1.23x faster                                  |
| deepcopy_reduce            | 2.07 us                                                | 1.70 us: 1.22x faster                                 |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 449 ms: 1.19x faster                                  |
| coroutines                 | 19.2 ms                                                | 16.2 ms: 1.19x faster                                 |
| async_tree_io              | 668 ms                                                 | 577 ms: 1.16x faster                                  |
| logging_simple             | 3.69 us                                                | 3.20 us: 1.15x faster                                 |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 459 ms: 1.15x faster                                  |
| logging_format             | 3.98 us                                                | 3.50 us: 1.14x faster                                 |
| deepcopy_memo              | 27.7 us                                                | 25.1 us: 1.10x faster                                 |
| regex_effbot               | 2.64 ms                                                | 2.48 ms: 1.07x faster                                 |
| regex_dna                  | 154 ms                                                 | 145 ms: 1.06x faster                                  |
| dulwich_log                | 29.8 ms                                                | 28.5 ms: 1.05x faster                                 |
| async_generators           | 304 ms                                                 | 292 ms: 1.04x faster                                  |
| mdp                        | 1.58 sec                                               | 1.55 sec: 1.02x faster                                |
| pathlib                    | 24.2 ms                                                | 23.7 ms: 1.02x faster                                 |
| json                       | 3.09 ms                                                | 3.03 ms: 1.02x faster                                 |
| float                      | 55.8 ms                                                | 55.5 ms: 1.00x faster                                 |
| asyncio_websockets         | 409 ms                                                 | 408 ms: 1.00x faster                                  |
| pidigits                   | 282 ms                                                 | 283 ms: 1.00x slower                                  |
| json_loads                 | 17.2 us                                                | 17.3 us: 1.00x slower                                 |
| gc_traversal               | 2.40 ms                                                | 2.46 ms: 1.02x slower                                 |
| bench_thread_pool          | 504 us                                                 | 519 us: 1.03x slower                                  |
| xml_etree_parse            | 106 ms                                                 | 111 ms: 1.04x slower                                  |
| asyncio_tcp_ssl            | 1.24 sec                                               | 1.30 sec: 1.04x slower                                |
| xml_etree_iterparse        | 74.0 ms                                                | 78.1 ms: 1.05x slower                                 |
| regex_v8                   | 16.0 ms                                                | 16.8 ms: 1.05x slower                                 |
| xml_etree_process          | 39.7 ms                                                | 41.9 ms: 1.06x slower                                 |
| generators                 | 31.1 ms                                                | 32.9 ms: 1.06x slower                                 |
| pickle_pure_python         | 200 us                                                 | 213 us: 1.07x slower                                  |
| json_dumps                 | 6.22 ms                                                | 6.65 ms: 1.07x slower                                 |
| scimark_lu                 | 76.0 ms                                                | 81.5 ms: 1.07x slower                                 |
| chaos                      | 42.5 ms                                                | 45.7 ms: 1.07x slower                                 |
| django_template            | 22.3 ms                                                | 24.1 ms: 1.08x slower                                 |
| xml_etree_generate         | 55.8 ms                                                | 60.5 ms: 1.08x slower                                 |
| nqueens                    | 62.4 ms                                                | 67.9 ms: 1.09x slower                                 |
| pycparser                  | 677 ms                                                 | 739 ms: 1.09x slower                                  |
| sqlglot_normalize          | 186 ms                                                 | 204 ms: 1.10x slower                                  |
| unpickle_pure_python       | 151 us                                                 | 165 us: 1.10x slower                                  |
| 2to3                       | 169 ms                                                 | 186 ms: 1.10x slower                                  |
| nbody                      | 68.8 ms                                                | 75.9 ms: 1.10x slower                                 |
| sympy_expand               | 241 ms                                                 | 268 ms: 1.11x slower                                  |
| bench_mp_pool              | 44.9 ms                                                | 50.1 ms: 1.12x slower                                 |
| go                         | 102 ms                                                 | 114 ms: 1.12x slower                                  |
| sqlglot_parse              | 848 us                                                 | 951 us: 1.12x slower                                  |
| sympy_str                  | 148 ms                                                 | 166 ms: 1.13x slower                                  |
| sqlglot_optimize           | 34.0 ms                                                | 38.4 ms: 1.13x slower                                 |
| docutils                   | 1.50 sec                                               | 1.70 sec: 1.13x slower                                |
| sqlglot_transpile          | 1.02 ms                                                | 1.16 ms: 1.14x slower                                 |
| sympy_sum                  | 77.6 ms                                                | 88.3 ms: 1.14x slower                                 |
| sympy_integrate            | 11.4 ms                                                | 13.0 ms: 1.14x slower                                 |
| tomli_loads                | 1.39 sec                                               | 1.59 sec: 1.14x slower                                |
| meteor_contest             | 71.7 ms                                                | 82.6 ms: 1.15x slower                                 |
| coverage                   | 38.9 ms                                                | 45.0 ms: 1.16x slower                                 |
| comprehensions             | 14.5 us                                                | 16.9 us: 1.16x slower                                 |
| scimark_fft                | 195 ms                                                 | 226 ms: 1.16x slower                                  |
| typing_runtime_protocols   | 93.0 us                                                | 108 us: 1.16x slower                                  |
| pprint_safe_repr           | 497 ms                                                 | 581 ms: 1.17x slower                                  |
| pprint_pformat             | 1.01 sec                                               | 1.19 sec: 1.17x slower                                |
| mako                       | 7.71 ms                                                | 9.09 ms: 1.18x slower                                 |
| logging_silent             | 76.4 ns                                                | 90.6 ns: 1.19x slower                                 |
| crypto_pyaes               | 51.9 ms                                                | 62.6 ms: 1.21x slower                                 |
| regex_compile              | 77.9 ms                                                | 94.5 ms: 1.21x slower                                 |
| deltablue                  | 2.71 ms                                                | 3.29 ms: 1.22x slower                                 |
| pyflate                    | 316 ms                                                 | 387 ms: 1.23x slower                                  |
| spectral_norm              | 76.4 ms                                                | 94.3 ms: 1.23x slower                                 |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 3.92 ms: 1.25x slower                                 |
| richards_super             | 36.0 ms                                                | 45.2 ms: 1.25x slower                                 |
| scimark_monte_carlo        | 45.0 ms                                                | 57.2 ms: 1.27x slower                                 |
| hexiom                     | 4.54 ms                                                | 5.79 ms: 1.27x slower                                 |
| richards                   | 32.1 ms                                                | 41.0 ms: 1.28x slower                                 |
| create_gc_cycles           | 701 us                                                 | 902 us: 1.29x slower                                  |
| scimark_sor                | 87.4 ms                                                | 112 ms: 1.29x slower                                  |
| fannkuch                   | 248 ms                                                 | 326 ms: 1.31x slower                                  |
| telco                      | 3.68 ms                                                | 5.04 ms: 1.37x slower                                 |
| python_startup_no_site     | 9.37 ms                                                | 13.9 ms: 1.48x slower                                 |
| python_startup             | 11.4 ms                                                | 16.9 ms: 1.48x slower                                 |
| Geometric mean             | (ref)                                                  | 1.06x slower                                          |

Benchmark hidden because not significant (2): asyncio_tcp, tornado_http
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (14) of results/bm-20240814-3.14.0a0-315a933-PYTHON_UOPS/bm-20240814-darwin-arm64-python-main-3.14.0a0-315a933.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.87% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 0.47x