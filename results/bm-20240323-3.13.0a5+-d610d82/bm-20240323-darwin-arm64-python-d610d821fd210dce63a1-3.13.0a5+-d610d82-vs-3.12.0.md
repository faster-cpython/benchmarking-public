# Results vs. 3.12.0

- fork: python
- ref: d610d821fd210dce63a1
- machine: darwin-arm64
- commit hash: d610d82
- commit date: 2024-03-23
- overall geometric mean: 1.05x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.03x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 164 ms: 1.03x faster                                                   |
| chameleon      | 4.70 ms                                                | 4.46 ms: 1.05x faster                                                  |
| docutils       | 1.50 sec                                               | 1.48 sec: 1.01x faster                                                 |
| tornado_http   | 69.3 ms                                                | 81.6 ms: 1.18x slower                                                  |
| Geometric mean | (ref)                                                  | 1.02x slower                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 323 ms                                                 | 241 ms: 1.34x faster                                                   |
| async_tree_memoization     | 312 ms                                                 | 251 ms: 1.25x faster                                                   |
| async_tree_none_tg         | 258 ms                                                 | 208 ms: 1.24x faster                                                   |
| async_tree_none            | 266 ms                                                 | 220 ms: 1.21x faster                                                   |
| async_tree_io              | 668 ms                                                 | 561 ms: 1.19x faster                                                   |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 451 ms: 1.18x faster                                                   |
| async_tree_io_tg           | 669 ms                                                 | 575 ms: 1.16x faster                                                   |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 455 ms: 1.15x faster                                                   |
| Geometric mean             | (ref)                                                  | 1.21x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 51.2 ms: 1.09x faster                                                  |
| pidigits       | 282 ms                                                 | 283 ms: 1.00x slower                                                   |
| nbody          | 68.8 ms                                                | 71.0 ms: 1.03x slower                                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 77.9 ms                                                | 70.0 ms: 1.11x faster                                                  |
| regex_effbot   | 2.64 ms                                                | 2.54 ms: 1.04x faster                                                  |
| regex_dna      | 154 ms                                                 | 152 ms: 1.02x faster                                                   |
| regex_v8       | 16.0 ms                                                | 16.9 ms: 1.06x slower                                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 200 us                                                 | 185 us: 1.08x faster                                                   |
| xml_etree_parse      | 106 ms                                                 | 99.4 ms: 1.07x faster                                                  |
| xml_etree_iterparse  | 74.0 ms                                                | 69.6 ms: 1.06x faster                                                  |
| xml_etree_process    | 39.7 ms                                                | 37.5 ms: 1.06x faster                                                  |
| xml_etree_generate   | 55.8 ms                                                | 54.6 ms: 1.02x faster                                                  |
| unpickle_pure_python | 151 us                                                 | 148 us: 1.02x faster                                                   |
| json_loads           | 17.2 us                                                | 17.0 us: 1.01x faster                                                  |
| pickle_dict          | 18.1 us                                                | 18.1 us: 1.00x slower                                                  |
| pickle               | 7.23 us                                                | 7.25 us: 1.00x slower                                                  |
| unpickle             | 9.12 us                                                | 9.17 us: 1.01x slower                                                  |
| unpickle_list        | 3.02 us                                                | 3.05 us: 1.01x slower                                                  |
| json_dumps           | 6.22 ms                                                | 6.36 ms: 1.02x slower                                                  |
| pickle_list          | 2.89 us                                                | 2.95 us: 1.02x slower                                                  |
| tomli_loads          | 1.39 sec                                               | 1.52 sec: 1.09x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 11.4 ms                                                | 14.9 ms: 1.31x slower                                                  |
| python_startup_no_site | 9.37 ms                                                | 13.0 ms: 1.39x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.35x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 22.3 ms                                                | 20.3 ms: 1.10x faster                                                  |
| mako            | 7.71 ms                                                | 7.06 ms: 1.09x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.10x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| raytrace                   | 212 ms                                                 | 156 ms: 1.36x faster                                                   |
| async_tree_memoization_tg  | 323 ms                                                 | 241 ms: 1.34x faster                                                   |
| typing_runtime_protocols   | 93.0 us                                                | 69.7 us: 1.34x faster                                                  |
| comprehensions             | 14.5 us                                                | 11.2 us: 1.30x faster                                                  |
| async_tree_memoization     | 312 ms                                                 | 251 ms: 1.25x faster                                                   |
| async_tree_none_tg         | 258 ms                                                 | 208 ms: 1.24x faster                                                   |
| async_tree_none            | 266 ms                                                 | 220 ms: 1.21x faster                                                   |
| deltablue                  | 2.71 ms                                                | 2.27 ms: 1.19x faster                                                  |
| async_tree_io              | 668 ms                                                 | 561 ms: 1.19x faster                                                   |
| unpack_sequence            | 31.5 ns                                                | 26.5 ns: 1.19x faster                                                  |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 451 ms: 1.18x faster                                                   |
| deepcopy_memo              | 27.7 us                                                | 23.6 us: 1.17x faster                                                  |
| logging_silent             | 76.4 ns                                                | 65.1 ns: 1.17x faster                                                  |
| async_tree_io_tg           | 669 ms                                                 | 575 ms: 1.16x faster                                                   |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 455 ms: 1.15x faster                                                   |
| chaos                      | 42.5 ms                                                | 36.9 ms: 1.15x faster                                                  |
| generators                 | 31.1 ms                                                | 27.1 ms: 1.15x faster                                                  |
| sqlglot_parse              | 848 us                                                 | 748 us: 1.13x faster                                                   |
| asyncio_tcp                | 449 ms                                                 | 399 ms: 1.13x faster                                                   |
| sqlglot_transpile          | 1.02 ms                                                | 909 us: 1.12x faster                                                   |
| logging_format             | 3.98 us                                                | 3.55 us: 1.12x faster                                                  |
| logging_simple             | 3.69 us                                                | 3.29 us: 1.12x faster                                                  |
| nqueens                    | 62.4 ms                                                | 55.9 ms: 1.12x faster                                                  |
| deepcopy_reduce            | 2.07 us                                                | 1.86 us: 1.12x faster                                                  |
| sympy_str                  | 148 ms                                                 | 132 ms: 1.11x faster                                                   |
| regex_compile              | 77.9 ms                                                | 70.0 ms: 1.11x faster                                                  |
| coroutines                 | 19.2 ms                                                | 17.3 ms: 1.11x faster                                                  |
| scimark_lu                 | 76.0 ms                                                | 68.5 ms: 1.11x faster                                                  |
| sympy_sum                  | 77.6 ms                                                | 70.0 ms: 1.11x faster                                                  |
| sympy_integrate            | 11.4 ms                                                | 10.3 ms: 1.10x faster                                                  |
| deepcopy                   | 235 us                                                 | 213 us: 1.10x faster                                                   |
| django_template            | 22.3 ms                                                | 20.3 ms: 1.10x faster                                                  |
| crypto_pyaes               | 51.9 ms                                                | 47.1 ms: 1.10x faster                                                  |
| mako                       | 7.71 ms                                                | 7.06 ms: 1.09x faster                                                  |
| float                      | 55.8 ms                                                | 51.2 ms: 1.09x faster                                                  |
| sqlglot_normalize          | 186 ms                                                 | 171 ms: 1.09x faster                                                   |
| hexiom                     | 4.54 ms                                                | 4.20 ms: 1.08x faster                                                  |
| pickle_pure_python         | 200 us                                                 | 185 us: 1.08x faster                                                   |
| spectral_norm              | 76.4 ms                                                | 71.3 ms: 1.07x faster                                                  |
| xml_etree_parse            | 106 ms                                                 | 99.4 ms: 1.07x faster                                                  |
| sqlglot_optimize           | 34.0 ms                                                | 31.9 ms: 1.07x faster                                                  |
| gunicorn                   | 1.15 ms                                                | 1.08 ms: 1.06x faster                                                  |
| xml_etree_iterparse        | 74.0 ms                                                | 69.6 ms: 1.06x faster                                                  |
| async_generators           | 304 ms                                                 | 286 ms: 1.06x faster                                                   |
| xml_etree_process          | 39.7 ms                                                | 37.5 ms: 1.06x faster                                                  |
| bench_thread_pool          | 504 us                                                 | 477 us: 1.06x faster                                                   |
| sympy_expand               | 241 ms                                                 | 228 ms: 1.06x faster                                                   |
| json                       | 3.09 ms                                                | 2.93 ms: 1.05x faster                                                  |
| chameleon                  | 4.70 ms                                                | 4.46 ms: 1.05x faster                                                  |
| dulwich_log                | 29.8 ms                                                | 28.6 ms: 1.04x faster                                                  |
| pprint_pformat             | 1.01 sec                                               | 972 ms: 1.04x faster                                                   |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 3.02 ms: 1.04x faster                                                  |
| pprint_safe_repr           | 497 ms                                                 | 478 ms: 1.04x faster                                                   |
| mdp                        | 1.58 sec                                               | 1.52 sec: 1.04x faster                                                 |
| regex_effbot               | 2.64 ms                                                | 2.54 ms: 1.04x faster                                                  |
| 2to3                       | 169 ms                                                 | 164 ms: 1.03x faster                                                   |
| pycparser                  | 677 ms                                                 | 661 ms: 1.02x faster                                                   |
| xml_etree_generate         | 55.8 ms                                                | 54.6 ms: 1.02x faster                                                  |
| unpickle_pure_python       | 151 us                                                 | 148 us: 1.02x faster                                                   |
| regex_dna                  | 154 ms                                                 | 152 ms: 1.02x faster                                                   |
| docutils                   | 1.50 sec                                               | 1.48 sec: 1.01x faster                                                 |
| json_loads                 | 17.2 us                                                | 17.0 us: 1.01x faster                                                  |
| scimark_monte_carlo        | 45.0 ms                                                | 44.6 ms: 1.01x faster                                                  |
| richards_super             | 36.0 ms                                                | 35.7 ms: 1.01x faster                                                  |
| go                         | 102 ms                                                 | 101 ms: 1.01x faster                                                   |
| meteor_contest             | 71.7 ms                                                | 71.2 ms: 1.01x faster                                                  |
| sqlite_synth               | 1.57 us                                                | 1.56 us: 1.01x faster                                                  |
| gc_traversal               | 2.40 ms                                                | 2.39 ms: 1.00x faster                                                  |
| asyncio_websockets         | 409 ms                                                 | 408 ms: 1.00x faster                                                   |
| pickle_dict                | 18.1 us                                                | 18.1 us: 1.00x slower                                                  |
| pidigits                   | 282 ms                                                 | 283 ms: 1.00x slower                                                   |
| pickle                     | 7.23 us                                                | 7.25 us: 1.00x slower                                                  |
| unpickle                   | 9.12 us                                                | 9.17 us: 1.01x slower                                                  |
| richards                   | 32.1 ms                                                | 32.3 ms: 1.01x slower                                                  |
| scimark_fft                | 195 ms                                                 | 197 ms: 1.01x slower                                                   |
| unpickle_list              | 3.02 us                                                | 3.05 us: 1.01x slower                                                  |
| create_gc_cycles           | 701 us                                                 | 712 us: 1.02x slower                                                   |
| pathlib                    | 24.2 ms                                                | 24.7 ms: 1.02x slower                                                  |
| json_dumps                 | 6.22 ms                                                | 6.36 ms: 1.02x slower                                                  |
| pickle_list                | 2.89 us                                                | 2.95 us: 1.02x slower                                                  |
| nbody                      | 68.8 ms                                                | 71.0 ms: 1.03x slower                                                  |
| pyflate                    | 316 ms                                                 | 329 ms: 1.04x slower                                                   |
| asyncio_tcp_ssl            | 1.24 sec                                               | 1.31 sec: 1.05x slower                                                 |
| regex_v8                   | 16.0 ms                                                | 16.9 ms: 1.06x slower                                                  |
| fannkuch                   | 248 ms                                                 | 266 ms: 1.07x slower                                                   |
| tomli_loads                | 1.39 sec                                               | 1.52 sec: 1.09x slower                                                 |
| scimark_sor                | 87.4 ms                                                | 100 ms: 1.15x slower                                                   |
| tornado_http               | 69.3 ms                                                | 81.6 ms: 1.18x slower                                                  |
| coverage                   | 38.9 ms                                                | 47.2 ms: 1.21x slower                                                  |
| mypy2                      | 380 ms                                                 | 466 ms: 1.23x slower                                                   |
| telco                      | 3.68 ms                                                | 4.53 ms: 1.23x slower                                                  |
| python_startup             | 11.4 ms                                                | 14.9 ms: 1.31x slower                                                  |
| python_startup_no_site     | 9.37 ms                                                | 13.0 ms: 1.39x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.05x faster                                                           |

Benchmark hidden because not significant (3): aiohttp, dask, bench_mp_pool
Ignored benchmarks (2) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (13) of results/bm-20240323-3.13.0a5+-d610d82/bm-20240323-darwin-arm64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, genshi_text, genshi_xml, html5lib, pylint, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x


# Memory

- memory change: 1.03x