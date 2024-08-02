
# Results vs. 3.12.0

- fork: python
- ref: v3.13.0a2
- machine: darwin-arm64
- commit hash: 9c4347e
- commit date: 2023-11-22
- overall geometric mean: 1.06x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 179 ms: 1.06x slower                                       |
| chameleon      | 4.70 ms                                                | 4.93 ms: 1.05x slower                                      |
| docutils       | 1.50 sec                                               | 1.51 sec: 1.00x slower                                     |
| Geometric mean | (ref)                                                  | 1.03x slower                                               |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 526 ms                                                 | 532 ms: 1.01x slower                                       |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 549 ms: 1.03x slower                                       |
| async_tree_io_tg           | 669 ms                                                 | 703 ms: 1.05x slower                                       |
| async_tree_memoization_tg  | 323 ms                                                 | 346 ms: 1.07x slower                                       |
| async_tree_none_tg         | 258 ms                                                 | 277 ms: 1.08x slower                                       |
| async_tree_io              | 668 ms                                                 | 719 ms: 1.08x slower                                       |
| async_tree_memoization     | 312 ms                                                 | 339 ms: 1.09x slower                                       |
| Geometric mean             | (ref)                                                  | 1.05x slower                                               |

Benchmark hidden because not significant (1): async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pidigits       | 282 ms                                                 | 284 ms: 1.01x slower                                       |
| float          | 55.8 ms                                                | 68.2 ms: 1.22x slower                                      |
| nbody          | 68.8 ms                                                | 86.3 ms: 1.25x slower                                      |
| Geometric mean | (ref)                                                  | 1.16x slower                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_effbot   | 2.64 ms                                                | 2.56 ms: 1.03x faster                                      |
| regex_dna      | 154 ms                                                 | 155 ms: 1.01x slower                                       |
| regex_v8       | 16.0 ms                                                | 17.4 ms: 1.09x slower                                      |
| regex_compile  | 77.9 ms                                                | 85.5 ms: 1.10x slower                                      |
| Geometric mean | (ref)                                                  | 1.04x slower                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| unpickle_list        | 3.02 us                                                | 2.98 us: 1.01x faster                                      |
| unpickle             | 9.12 us                                                | 8.99 us: 1.01x faster                                      |
| json_loads           | 17.2 us                                                | 17.1 us: 1.01x faster                                      |
| pickle_pure_python   | 200 us                                                 | 201 us: 1.00x slower                                       |
| pickle_list          | 2.89 us                                                | 2.93 us: 1.02x slower                                      |
| pickle               | 7.23 us                                                | 7.36 us: 1.02x slower                                      |
| xml_etree_process    | 39.7 ms                                                | 41.2 ms: 1.04x slower                                      |
| json_dumps           | 6.22 ms                                                | 6.61 ms: 1.06x slower                                      |
| xml_etree_generate   | 55.8 ms                                                | 59.6 ms: 1.07x slower                                      |
| xml_etree_iterparse  | 74.0 ms                                                | 81.1 ms: 1.10x slower                                      |
| unpickle_pure_python | 151 us                                                 | 168 us: 1.11x slower                                       |
| tomli_loads          | 1.39 sec                                               | 1.67 sec: 1.20x slower                                     |
| Geometric mean       | (ref)                                                  | 1.04x slower                                               |

Benchmark hidden because not significant (2): pickle_dict, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 11.4 ms                                                | 12.7 ms: 1.11x slower                                      |
| python_startup_no_site | 9.37 ms                                                | 11.4 ms: 1.21x slower                                      |
| Geometric mean         | (ref)                                                  | 1.16x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e |
|-----------|:------------------------------------------------------:|:----------------------------------------------------------:|
| mako      | 7.71 ms                                                | 9.60 ms: 1.24x slower                                      |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231122-darwin-arm64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| typing_runtime_protocols   | 93.0 us                                                | 77.1 us: 1.21x faster                                      |
| unpack_sequence            | 31.5 ns                                                | 28.2 ns: 1.12x faster                                      |
| generators                 | 31.1 ms                                                | 28.0 ms: 1.11x faster                                      |
| raytrace                   | 212 ms                                                 | 195 ms: 1.09x faster                                       |
| logging_silent             | 76.4 ns                                                | 72.1 ns: 1.06x faster                                      |
| deepcopy_reduce            | 2.07 us                                                | 1.95 us: 1.06x faster                                      |
| deepcopy                   | 235 us                                                 | 224 us: 1.05x faster                                       |
| deepcopy_memo              | 27.7 us                                                | 26.7 us: 1.04x faster                                      |
| coroutines                 | 19.2 ms                                                | 18.6 ms: 1.03x faster                                      |
| json                       | 3.09 ms                                                | 2.99 ms: 1.03x faster                                      |
| regex_effbot               | 2.64 ms                                                | 2.56 ms: 1.03x faster                                      |
| logging_simple             | 3.69 us                                                | 3.60 us: 1.02x faster                                      |
| logging_format             | 3.98 us                                                | 3.90 us: 1.02x faster                                      |
| unpickle_list              | 3.02 us                                                | 2.98 us: 1.01x faster                                      |
| unpickle                   | 9.12 us                                                | 8.99 us: 1.01x faster                                      |
| sqlglot_parse              | 848 us                                                 | 838 us: 1.01x faster                                       |
| async_generators           | 304 ms                                                 | 301 ms: 1.01x faster                                       |
| json_loads                 | 17.2 us                                                | 17.1 us: 1.01x faster                                      |
| sqlglot_transpile          | 1.02 ms                                                | 1.02 ms: 1.00x faster                                      |
| asyncio_websockets         | 409 ms                                                 | 409 ms: 1.00x faster                                       |
| scimark_lu                 | 76.0 ms                                                | 76.1 ms: 1.00x slower                                      |
| gc_traversal               | 2.40 ms                                                | 2.40 ms: 1.00x slower                                      |
| pickle_pure_python         | 200 us                                                 | 201 us: 1.00x slower                                       |
| create_gc_cycles           | 701 us                                                 | 704 us: 1.00x slower                                       |
| docutils                   | 1.50 sec                                               | 1.51 sec: 1.00x slower                                     |
| regex_dna                  | 154 ms                                                 | 155 ms: 1.01x slower                                       |
| pidigits                   | 282 ms                                                 | 284 ms: 1.01x slower                                       |
| dulwich_log                | 29.8 ms                                                | 30.1 ms: 1.01x slower                                      |
| sympy_expand               | 241 ms                                                 | 243 ms: 1.01x slower                                       |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 532 ms: 1.01x slower                                       |
| sympy_str                  | 148 ms                                                 | 149 ms: 1.01x slower                                       |
| pickle_list                | 2.89 us                                                | 2.93 us: 1.02x slower                                      |
| pickle                     | 7.23 us                                                | 7.36 us: 1.02x slower                                      |
| sqlglot_normalize          | 186 ms                                                 | 191 ms: 1.03x slower                                       |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 549 ms: 1.03x slower                                       |
| sympy_integrate            | 11.4 ms                                                | 11.7 ms: 1.03x slower                                      |
| sympy_sum                  | 77.6 ms                                                | 80.2 ms: 1.03x slower                                      |
| mdp                        | 1.58 sec                                               | 1.63 sec: 1.03x slower                                     |
| dask                       | 222 ms                                                 | 230 ms: 1.04x slower                                       |
| bench_thread_pool          | 504 us                                                 | 523 us: 1.04x slower                                       |
| xml_etree_process          | 39.7 ms                                                | 41.2 ms: 1.04x slower                                      |
| pycparser                  | 677 ms                                                 | 706 ms: 1.04x slower                                       |
| pathlib                    | 24.2 ms                                                | 25.3 ms: 1.04x slower                                      |
| richards                   | 32.1 ms                                                | 33.6 ms: 1.04x slower                                      |
| sqlite_synth               | 1.57 us                                                | 1.64 us: 1.05x slower                                      |
| richards_super             | 36.0 ms                                                | 37.7 ms: 1.05x slower                                      |
| chameleon                  | 4.70 ms                                                | 4.93 ms: 1.05x slower                                      |
| asyncio_tcp_ssl            | 1.24 sec                                               | 1.30 sec: 1.05x slower                                     |
| async_tree_io_tg           | 669 ms                                                 | 703 ms: 1.05x slower                                       |
| crypto_pyaes               | 51.9 ms                                                | 54.5 ms: 1.05x slower                                      |
| sqlglot_optimize           | 34.0 ms                                                | 35.9 ms: 1.05x slower                                      |
| 2to3                       | 169 ms                                                 | 179 ms: 1.06x slower                                       |
| json_dumps                 | 6.22 ms                                                | 6.61 ms: 1.06x slower                                      |
| xml_etree_generate         | 55.8 ms                                                | 59.6 ms: 1.07x slower                                      |
| async_tree_memoization_tg  | 323 ms                                                 | 346 ms: 1.07x slower                                       |
| async_tree_none_tg         | 258 ms                                                 | 277 ms: 1.08x slower                                       |
| async_tree_io              | 668 ms                                                 | 719 ms: 1.08x slower                                       |
| comprehensions             | 14.5 us                                                | 15.7 us: 1.08x slower                                      |
| async_tree_memoization     | 312 ms                                                 | 339 ms: 1.09x slower                                       |
| regex_v8                   | 16.0 ms                                                | 17.4 ms: 1.09x slower                                      |
| xml_etree_iterparse        | 74.0 ms                                                | 81.1 ms: 1.10x slower                                      |
| meteor_contest             | 71.7 ms                                                | 78.7 ms: 1.10x slower                                      |
| regex_compile              | 77.9 ms                                                | 85.5 ms: 1.10x slower                                      |
| go                         | 102 ms                                                 | 112 ms: 1.10x slower                                       |
| python_startup             | 11.4 ms                                                | 12.7 ms: 1.11x slower                                      |
| unpickle_pure_python       | 151 us                                                 | 168 us: 1.11x slower                                       |
| chaos                      | 42.5 ms                                                | 47.5 ms: 1.12x slower                                      |
| nqueens                    | 62.4 ms                                                | 69.7 ms: 1.12x slower                                      |
| pprint_safe_repr           | 497 ms                                                 | 561 ms: 1.13x slower                                       |
| pprint_pformat             | 1.01 sec                                               | 1.15 sec: 1.14x slower                                     |
| pyflate                    | 316 ms                                                 | 369 ms: 1.17x slower                                       |
| tomli_loads                | 1.39 sec                                               | 1.67 sec: 1.20x slower                                     |
| python_startup_no_site     | 9.37 ms                                                | 11.4 ms: 1.21x slower                                      |
| scimark_sor                | 87.4 ms                                                | 106 ms: 1.22x slower                                       |
| float                      | 55.8 ms                                                | 68.2 ms: 1.22x slower                                      |
| coverage                   | 38.9 ms                                                | 47.9 ms: 1.23x slower                                      |
| mako                       | 7.71 ms                                                | 9.60 ms: 1.24x slower                                      |
| nbody                      | 68.8 ms                                                | 86.3 ms: 1.25x slower                                      |
| telco                      | 3.68 ms                                                | 4.63 ms: 1.26x slower                                      |
| scimark_fft                | 195 ms                                                 | 246 ms: 1.26x slower                                       |
| scimark_monte_carlo        | 45.0 ms                                                | 57.9 ms: 1.29x slower                                      |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 4.04 ms: 1.29x slower                                      |
| fannkuch                   | 248 ms                                                 | 324 ms: 1.30x slower                                       |
| deltablue                  | 2.71 ms                                                | 3.59 ms: 1.33x slower                                      |
| spectral_norm              | 76.4 ms                                                | 102 ms: 1.34x slower                                       |
| hexiom                     | 4.54 ms                                                | 6.21 ms: 1.37x slower                                      |
| mypy2                      | 380 ms                                                 | 532 ms: 1.40x slower                                       |
| Geometric mean             | (ref)                                                  | 1.06x slower                                               |

Benchmark hidden because not significant (6): asyncio_tcp, async_tree_none, bench_mp_pool, pickle_dict, xml_etree_parse, tornado_http
Ignored benchmarks (5) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, django_template, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative


# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.03x


# Memory

- memory change: 1.00x