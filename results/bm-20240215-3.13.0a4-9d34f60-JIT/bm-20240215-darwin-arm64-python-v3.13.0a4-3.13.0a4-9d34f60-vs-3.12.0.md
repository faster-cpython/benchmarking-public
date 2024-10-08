# Results vs. 3.12.0

- fork: python
- ref: v3.13.0a4
- machine: darwin-arm64
- commit hash: 9d34f60
- commit date: 2024-02-15
- overall geometric mean: 1.01x slower \*
- HPT reliability: 83.43%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240215-darwin-arm64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 190 ms: 1.12x slower                                       |
| chameleon      | 4.70 ms                                                | 4.81 ms: 1.02x slower                                      |
| docutils       | 1.50 sec                                               | 1.48 sec: 1.02x faster                                     |
| Geometric mean | (ref)                                                  | 1.03x slower                                               |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240215-darwin-arm64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_none         | 266 ms                                                 | 252 ms: 1.05x faster                                       |
| async_tree_cpu_io_mixed | 526 ms                                                 | 519 ms: 1.01x faster                                       |
| async_tree_io_tg        | 669 ms                                                 | 666 ms: 1.00x faster                                       |
| async_tree_none_tg      | 258 ms                                                 | 259 ms: 1.00x slower                                       |
| async_tree_io           | 668 ms                                                 | 699 ms: 1.05x slower                                       |
| async_tree_memoization  | 312 ms                                                 | 328 ms: 1.05x slower                                       |
| Geometric mean          | (ref)                                                  | 1.00x slower                                               |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed_tg, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240215-darwin-arm64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pidigits       | 282 ms                                                 | 283 ms: 1.00x slower                                       |
| nbody          | 68.8 ms                                                | 75.9 ms: 1.10x slower                                      |
| Geometric mean | (ref)                                                  | 1.03x slower                                               |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240215-darwin-arm64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_effbot   | 2.64 ms                                                | 2.54 ms: 1.04x faster                                      |
| regex_compile  | 77.9 ms                                                | 75.1 ms: 1.04x faster                                      |
| regex_dna      | 154 ms                                                 | 150 ms: 1.03x faster                                       |
| regex_v8       | 16.0 ms                                                | 17.4 ms: 1.09x slower                                      |
| Geometric mean | (ref)                                                  | 1.00x faster                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240215-darwin-arm64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| xml_etree_process    | 39.7 ms                                                | 38.7 ms: 1.02x faster                                      |
| pickle_pure_python   | 200 us                                                 | 196 us: 1.02x faster                                       |
| json_loads           | 17.2 us                                                | 16.9 us: 1.02x faster                                      |
| xml_etree_parse      | 106 ms                                                 | 105 ms: 1.01x faster                                       |
| xml_etree_generate   | 55.8 ms                                                | 56.1 ms: 1.00x slower                                      |
| pickle_dict          | 18.1 us                                                | 18.2 us: 1.01x slower                                      |
| tomli_loads          | 1.39 sec                                               | 1.40 sec: 1.01x slower                                     |
| xml_etree_iterparse  | 74.0 ms                                                | 74.8 ms: 1.01x slower                                      |
| pickle               | 7.23 us                                                | 7.33 us: 1.01x slower                                      |
| unpickle_list        | 3.02 us                                                | 3.10 us: 1.03x slower                                      |
| pickle_list          | 2.89 us                                                | 2.99 us: 1.03x slower                                      |
| json_dumps           | 6.22 ms                                                | 6.48 ms: 1.04x slower                                      |
| unpickle_pure_python | 151 us                                                 | 158 us: 1.05x slower                                       |
| Geometric mean       | (ref)                                                  | 1.01x slower                                               |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240215-darwin-arm64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 11.4 ms                                                | 13.1 ms: 1.15x slower                                      |
| python_startup_no_site | 9.37 ms                                                | 11.6 ms: 1.23x slower                                      |
| Geometric mean         | (ref)                                                  | 1.19x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240215-darwin-arm64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|-----------|:------------------------------------------------------:|:----------------------------------------------------------:|
| mako      | 7.71 ms                                                | 7.79 ms: 1.01x slower                                      |

All benchmarks:
===============

| Benchmark                | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240215-darwin-arm64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| typing_runtime_protocols | 93.0 us                                                | 70.9 us: 1.31x faster                                      |
| raytrace                 | 212 ms                                                 | 176 ms: 1.20x faster                                       |
| comprehensions           | 14.5 us                                                | 12.6 us: 1.16x faster                                      |
| asyncio_tcp              | 449 ms                                                 | 401 ms: 1.12x faster                                       |
| unpack_sequence          | 31.5 ns                                                | 28.4 ns: 1.11x faster                                      |
| deltablue                | 2.71 ms                                                | 2.45 ms: 1.10x faster                                      |
| generators               | 31.1 ms                                                | 28.3 ms: 1.10x faster                                      |
| logging_silent           | 76.4 ns                                                | 70.3 ns: 1.09x faster                                      |
| sqlglot_parse            | 848 us                                                 | 787 us: 1.08x faster                                       |
| logging_simple           | 3.69 us                                                | 3.45 us: 1.07x faster                                      |
| logging_format           | 3.98 us                                                | 3.76 us: 1.06x faster                                      |
| crypto_pyaes             | 51.9 ms                                                | 49.1 ms: 1.06x faster                                      |
| async_tree_none          | 266 ms                                                 | 252 ms: 1.05x faster                                       |
| deepcopy_memo            | 27.7 us                                                | 26.3 us: 1.05x faster                                      |
| sqlglot_transpile        | 1.02 ms                                                | 973 us: 1.05x faster                                       |
| json                     | 3.09 ms                                                | 2.95 ms: 1.05x faster                                      |
| sympy_str                | 148 ms                                                 | 141 ms: 1.05x faster                                       |
| deepcopy_reduce          | 2.07 us                                                | 1.98 us: 1.04x faster                                      |
| regex_effbot             | 2.64 ms                                                | 2.54 ms: 1.04x faster                                      |
| deepcopy                 | 235 us                                                 | 226 us: 1.04x faster                                       |
| regex_compile            | 77.9 ms                                                | 75.1 ms: 1.04x faster                                      |
| chaos                    | 42.5 ms                                                | 41.0 ms: 1.04x faster                                      |
| sympy_sum                | 77.6 ms                                                | 75.3 ms: 1.03x faster                                      |
| coroutines               | 19.2 ms                                                | 18.7 ms: 1.03x faster                                      |
| sympy_integrate          | 11.4 ms                                                | 11.1 ms: 1.03x faster                                      |
| regex_dna                | 154 ms                                                 | 150 ms: 1.03x faster                                       |
| xml_etree_process        | 39.7 ms                                                | 38.7 ms: 1.02x faster                                      |
| pickle_pure_python       | 200 us                                                 | 196 us: 1.02x faster                                       |
| sqlglot_normalize        | 186 ms                                                 | 182 ms: 1.02x faster                                       |
| json_loads               | 17.2 us                                                | 16.9 us: 1.02x faster                                      |
| scimark_lu               | 76.0 ms                                                | 74.8 ms: 1.02x faster                                      |
| docutils                 | 1.50 sec                                               | 1.48 sec: 1.02x faster                                     |
| nqueens                  | 62.4 ms                                                | 61.6 ms: 1.01x faster                                      |
| async_tree_cpu_io_mixed  | 526 ms                                                 | 519 ms: 1.01x faster                                       |
| richards_super           | 36.0 ms                                                | 35.7 ms: 1.01x faster                                      |
| xml_etree_parse          | 106 ms                                                 | 105 ms: 1.01x faster                                       |
| richards                 | 32.1 ms                                                | 31.9 ms: 1.01x faster                                      |
| async_tree_io_tg         | 669 ms                                                 | 666 ms: 1.00x faster                                       |
| gc_traversal             | 2.40 ms                                                | 2.39 ms: 1.00x faster                                      |
| async_generators         | 304 ms                                                 | 303 ms: 1.00x faster                                       |
| pidigits                 | 282 ms                                                 | 283 ms: 1.00x slower                                       |
| xml_etree_generate       | 55.8 ms                                                | 56.1 ms: 1.00x slower                                      |
| async_tree_none_tg       | 258 ms                                                 | 259 ms: 1.00x slower                                       |
| create_gc_cycles         | 701 us                                                 | 705 us: 1.01x slower                                       |
| pickle_dict              | 18.1 us                                                | 18.2 us: 1.01x slower                                      |
| tomli_loads              | 1.39 sec                                               | 1.40 sec: 1.01x slower                                     |
| mako                     | 7.71 ms                                                | 7.79 ms: 1.01x slower                                      |
| xml_etree_iterparse      | 74.0 ms                                                | 74.8 ms: 1.01x slower                                      |
| sqlglot_optimize         | 34.0 ms                                                | 34.4 ms: 1.01x slower                                      |
| sqlite_synth             | 1.57 us                                                | 1.59 us: 1.01x slower                                      |
| pickle                   | 7.23 us                                                | 7.33 us: 1.01x slower                                      |
| mdp                      | 1.58 sec                                               | 1.61 sec: 1.02x slower                                     |
| bench_mp_pool            | 44.9 ms                                                | 45.9 ms: 1.02x slower                                      |
| pycparser                | 677 ms                                                 | 693 ms: 1.02x slower                                       |
| chameleon                | 4.70 ms                                                | 4.81 ms: 1.02x slower                                      |
| unpickle_list            | 3.02 us                                                | 3.10 us: 1.03x slower                                      |
| spectral_norm            | 76.4 ms                                                | 78.8 ms: 1.03x slower                                      |
| pyflate                  | 316 ms                                                 | 326 ms: 1.03x slower                                       |
| pickle_list              | 2.89 us                                                | 2.99 us: 1.03x slower                                      |
| meteor_contest           | 71.7 ms                                                | 74.3 ms: 1.04x slower                                      |
| pprint_safe_repr         | 497 ms                                                 | 515 ms: 1.04x slower                                       |
| pprint_pformat           | 1.01 sec                                               | 1.05 sec: 1.04x slower                                     |
| json_dumps               | 6.22 ms                                                | 6.48 ms: 1.04x slower                                      |
| async_tree_io            | 668 ms                                                 | 699 ms: 1.05x slower                                       |
| pathlib                  | 24.2 ms                                                | 25.4 ms: 1.05x slower                                      |
| unpickle_pure_python     | 151 us                                                 | 158 us: 1.05x slower                                       |
| async_tree_memoization   | 312 ms                                                 | 328 ms: 1.05x slower                                       |
| asyncio_tcp_ssl          | 1.24 sec                                               | 1.31 sec: 1.05x slower                                     |
| scimark_sparse_mat_mult  | 3.14 ms                                                | 3.31 ms: 1.06x slower                                      |
| fannkuch                 | 248 ms                                                 | 267 ms: 1.07x slower                                       |
| scimark_monte_carlo      | 45.0 ms                                                | 48.5 ms: 1.08x slower                                      |
| hexiom                   | 4.54 ms                                                | 4.91 ms: 1.08x slower                                      |
| go                       | 102 ms                                                 | 110 ms: 1.08x slower                                       |
| regex_v8                 | 16.0 ms                                                | 17.4 ms: 1.09x slower                                      |
| scimark_fft              | 195 ms                                                 | 213 ms: 1.09x slower                                       |
| nbody                    | 68.8 ms                                                | 75.9 ms: 1.10x slower                                      |
| 2to3                     | 169 ms                                                 | 190 ms: 1.12x slower                                       |
| python_startup           | 11.4 ms                                                | 13.1 ms: 1.15x slower                                      |
| scimark_sor              | 87.4 ms                                                | 106 ms: 1.21x slower                                       |
| coverage                 | 38.9 ms                                                | 47.5 ms: 1.22x slower                                      |
| telco                    | 3.68 ms                                                | 4.51 ms: 1.22x slower                                      |
| python_startup_no_site   | 9.37 ms                                                | 11.6 ms: 1.23x slower                                      |
| dask                     | 222 ms                                                 | 335 ms: 1.51x slower                                       |
| mypy2                    | 380 ms                                                 | 577 ms: 1.52x slower                                       |
| Geometric mean           | (ref)                                                  | 1.01x slower                                               |

Benchmark hidden because not significant (9): async_tree_cpu_io_mixed_tg, float, async_tree_memoization_tg, sympy_expand, bench_thread_pool, asyncio_websockets, dulwich_log, tornado_http, unpickle
Ignored benchmarks (5) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, django_template, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative


# HPT report

- Reliability score: 83.43% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x


# Memory

- memory change: 1.13x