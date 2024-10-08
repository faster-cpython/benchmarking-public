# Results vs. 3.12.0

- fork: python
- ref: v3.13.0b1
- machine: darwin-arm64
- commit hash: 2268289
- commit date: 2024-05-08
- overall geometric mean: 1.06x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240508-darwin-arm64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 179 ms: 1.06x slower                                       |
| chameleon      | 4.70 ms                                                | 4.35 ms: 1.08x faster                                      |
| docutils       | 1.50 sec                                               | 1.46 sec: 1.03x faster                                     |
| Geometric mean | (ref)                                                  | 1.01x faster                                               |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240508-darwin-arm64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_memoization_tg  | 323 ms                                                 | 245 ms: 1.32x faster                                       |
| async_tree_none_tg         | 258 ms                                                 | 197 ms: 1.31x faster                                       |
| async_tree_none            | 266 ms                                                 | 210 ms: 1.26x faster                                       |
| async_tree_memoization     | 312 ms                                                 | 258 ms: 1.21x faster                                       |
| async_tree_io_tg           | 669 ms                                                 | 564 ms: 1.19x faster                                       |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 453 ms: 1.17x faster                                       |
| async_tree_io              | 668 ms                                                 | 570 ms: 1.17x faster                                       |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 469 ms: 1.12x faster                                       |
| Geometric mean             | (ref)                                                  | 1.22x faster                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240508-darwin-arm64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| float          | 55.8 ms                                                | 49.0 ms: 1.14x faster                                      |
| nbody          | 68.8 ms                                                | 65.7 ms: 1.05x faster                                      |
| Geometric mean | (ref)                                                  | 1.06x faster                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240508-darwin-arm64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 77.9 ms                                                | 68.2 ms: 1.14x faster                                      |
| regex_dna      | 154 ms                                                 | 139 ms: 1.11x faster                                       |
| regex_effbot   | 2.64 ms                                                | 2.55 ms: 1.04x faster                                      |
| regex_v8       | 16.0 ms                                                | 16.8 ms: 1.05x slower                                      |
| Geometric mean | (ref)                                                  | 1.06x faster                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240508-darwin-arm64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pickle_pure_python   | 200 us                                                 | 181 us: 1.10x faster                                       |
| xml_etree_iterparse  | 74.0 ms                                                | 67.5 ms: 1.10x faster                                      |
| xml_etree_parse      | 106 ms                                                 | 97.6 ms: 1.09x faster                                      |
| xml_etree_generate   | 55.8 ms                                                | 51.8 ms: 1.08x faster                                      |
| xml_etree_process    | 39.7 ms                                                | 37.1 ms: 1.07x faster                                      |
| unpickle_pure_python | 151 us                                                 | 141 us: 1.07x faster                                       |
| json_loads           | 17.2 us                                                | 17.3 us: 1.00x slower                                      |
| pickle_dict          | 18.1 us                                                | 18.2 us: 1.01x slower                                      |
| json_dumps           | 6.22 ms                                                | 6.35 ms: 1.02x slower                                      |
| pickle_list          | 2.89 us                                                | 2.98 us: 1.03x slower                                      |
| pickle               | 7.23 us                                                | 7.47 us: 1.03x slower                                      |
| tomli_loads          | 1.39 sec                                               | 1.45 sec: 1.04x slower                                     |
| unpickle             | 9.12 us                                                | 9.70 us: 1.06x slower                                      |
| unpickle_list        | 3.02 us                                                | 3.31 us: 1.10x slower                                      |
| Geometric mean       | (ref)                                                  | 1.01x faster                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240508-darwin-arm64-python-v3.13.0b1-3.13.0b1-2268289 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup_no_site | 9.37 ms                                                | 11.6 ms: 1.24x slower                                      |
| python_startup         | 11.4 ms                                                | 14.3 ms: 1.26x slower                                      |
| Geometric mean         | (ref)                                                  | 1.25x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240508-darwin-arm64-python-v3.13.0b1-3.13.0b1-2268289 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| django_template | 22.3 ms                                                | 19.4 ms: 1.15x faster                                      |
| mako            | 7.71 ms                                                | 6.88 ms: 1.12x faster                                      |
| Geometric mean  | (ref)                                                  | 1.14x faster                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240508-darwin-arm64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| raytrace                   | 212 ms                                                 | 150 ms: 1.42x faster                                       |
| generators                 | 31.1 ms                                                | 22.7 ms: 1.37x faster                                      |
| comprehensions             | 14.5 us                                                | 10.9 us: 1.34x faster                                      |
| async_tree_memoization_tg  | 323 ms                                                 | 245 ms: 1.32x faster                                       |
| async_tree_none_tg         | 258 ms                                                 | 197 ms: 1.31x faster                                       |
| logging_silent             | 76.4 ns                                                | 60.1 ns: 1.27x faster                                      |
| async_tree_none            | 266 ms                                                 | 210 ms: 1.26x faster                                       |
| deltablue                  | 2.71 ms                                                | 2.15 ms: 1.26x faster                                      |
| deepcopy_memo              | 27.7 us                                                | 22.4 us: 1.24x faster                                      |
| async_tree_memoization     | 312 ms                                                 | 258 ms: 1.21x faster                                       |
| logging_simple             | 3.69 us                                                | 3.06 us: 1.20x faster                                      |
| coroutines                 | 19.2 ms                                                | 16.2 ms: 1.19x faster                                      |
| logging_format             | 3.98 us                                                | 3.36 us: 1.19x faster                                      |
| chaos                      | 42.5 ms                                                | 35.9 ms: 1.19x faster                                      |
| async_tree_io_tg           | 669 ms                                                 | 564 ms: 1.19x faster                                       |
| nqueens                    | 62.4 ms                                                | 52.8 ms: 1.18x faster                                      |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 453 ms: 1.17x faster                                       |
| async_tree_io              | 668 ms                                                 | 570 ms: 1.17x faster                                       |
| deepcopy                   | 235 us                                                 | 203 us: 1.16x faster                                       |
| deepcopy_reduce            | 2.07 us                                                | 1.79 us: 1.15x faster                                      |
| django_template            | 22.3 ms                                                | 19.4 ms: 1.15x faster                                      |
| sqlglot_parse              | 848 us                                                 | 739 us: 1.15x faster                                       |
| regex_compile              | 77.9 ms                                                | 68.2 ms: 1.14x faster                                      |
| float                      | 55.8 ms                                                | 49.0 ms: 1.14x faster                                      |
| sqlglot_transpile          | 1.02 ms                                                | 897 us: 1.14x faster                                       |
| mako                       | 7.71 ms                                                | 6.88 ms: 1.12x faster                                      |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 469 ms: 1.12x faster                                       |
| spectral_norm              | 76.4 ms                                                | 68.2 ms: 1.12x faster                                      |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 2.80 ms: 1.12x faster                                      |
| sqlglot_normalize          | 186 ms                                                 | 166 ms: 1.12x faster                                       |
| sympy_str                  | 148 ms                                                 | 133 ms: 1.11x faster                                       |
| scimark_lu                 | 76.0 ms                                                | 68.3 ms: 1.11x faster                                      |
| regex_dna                  | 154 ms                                                 | 139 ms: 1.11x faster                                       |
| hexiom                     | 4.54 ms                                                | 4.09 ms: 1.11x faster                                      |
| sympy_sum                  | 77.6 ms                                                | 70.2 ms: 1.11x faster                                      |
| pickle_pure_python         | 200 us                                                 | 181 us: 1.10x faster                                       |
| sympy_integrate            | 11.4 ms                                                | 10.3 ms: 1.10x faster                                      |
| xml_etree_iterparse        | 74.0 ms                                                | 67.5 ms: 1.10x faster                                      |
| sqlglot_optimize           | 34.0 ms                                                | 31.1 ms: 1.10x faster                                      |
| async_generators           | 304 ms                                                 | 278 ms: 1.09x faster                                       |
| dulwich_log                | 29.8 ms                                                | 27.3 ms: 1.09x faster                                      |
| xml_etree_parse            | 106 ms                                                 | 97.6 ms: 1.09x faster                                      |
| bench_thread_pool          | 504 us                                                 | 464 us: 1.09x faster                                       |
| chameleon                  | 4.70 ms                                                | 4.35 ms: 1.08x faster                                      |
| xml_etree_generate         | 55.8 ms                                                | 51.8 ms: 1.08x faster                                      |
| pycparser                  | 677 ms                                                 | 630 ms: 1.07x faster                                       |
| xml_etree_process          | 39.7 ms                                                | 37.1 ms: 1.07x faster                                      |
| pathlib                    | 24.2 ms                                                | 22.7 ms: 1.07x faster                                      |
| pprint_pformat             | 1.01 sec                                               | 947 ms: 1.07x faster                                       |
| unpickle_pure_python       | 151 us                                                 | 141 us: 1.07x faster                                       |
| pprint_safe_repr           | 497 ms                                                 | 468 ms: 1.06x faster                                       |
| sympy_expand               | 241 ms                                                 | 228 ms: 1.06x faster                                       |
| mdp                        | 1.58 sec                                               | 1.50 sec: 1.06x faster                                     |
| nbody                      | 68.8 ms                                                | 65.7 ms: 1.05x faster                                      |
| scimark_monte_carlo        | 45.0 ms                                                | 43.0 ms: 1.05x faster                                      |
| regex_effbot               | 2.64 ms                                                | 2.55 ms: 1.04x faster                                      |
| gunicorn                   | 1.15 ms                                                | 1.11 ms: 1.03x faster                                      |
| json                       | 3.09 ms                                                | 2.99 ms: 1.03x faster                                      |
| docutils                   | 1.50 sec                                               | 1.46 sec: 1.03x faster                                     |
| crypto_pyaes               | 51.9 ms                                                | 50.3 ms: 1.03x faster                                      |
| scimark_fft                | 195 ms                                                 | 190 ms: 1.03x faster                                       |
| richards_super             | 36.0 ms                                                | 35.2 ms: 1.02x faster                                      |
| sqlite_synth               | 1.57 us                                                | 1.54 us: 1.02x faster                                      |
| meteor_contest             | 71.7 ms                                                | 70.6 ms: 1.02x faster                                      |
| go                         | 102 ms                                                 | 100 ms: 1.01x faster                                       |
| richards                   | 32.1 ms                                                | 31.9 ms: 1.01x faster                                      |
| typing_runtime_protocols   | 93.0 us                                                | 92.5 us: 1.01x faster                                      |
| asyncio_websockets         | 409 ms                                                 | 408 ms: 1.00x faster                                       |
| json_loads                 | 17.2 us                                                | 17.3 us: 1.00x slower                                      |
| pickle_dict                | 18.1 us                                                | 18.2 us: 1.01x slower                                      |
| bench_mp_pool              | 44.9 ms                                                | 45.2 ms: 1.01x slower                                      |
| pyflate                    | 316 ms                                                 | 319 ms: 1.01x slower                                       |
| fannkuch                   | 248 ms                                                 | 252 ms: 1.01x slower                                       |
| json_dumps                 | 6.22 ms                                                | 6.35 ms: 1.02x slower                                      |
| gc_traversal               | 2.40 ms                                                | 2.46 ms: 1.02x slower                                      |
| pickle_list                | 2.89 us                                                | 2.98 us: 1.03x slower                                      |
| pickle                     | 7.23 us                                                | 7.47 us: 1.03x slower                                      |
| asyncio_tcp_ssl            | 1.24 sec                                               | 1.29 sec: 1.04x slower                                     |
| tomli_loads                | 1.39 sec                                               | 1.45 sec: 1.04x slower                                     |
| regex_v8                   | 16.0 ms                                                | 16.8 ms: 1.05x slower                                      |
| 2to3                       | 169 ms                                                 | 179 ms: 1.06x slower                                       |
| unpickle                   | 9.12 us                                                | 9.70 us: 1.06x slower                                      |
| unpickle_list              | 3.02 us                                                | 3.31 us: 1.10x slower                                      |
| scimark_sor                | 87.4 ms                                                | 96.3 ms: 1.10x slower                                      |
| coverage                   | 38.9 ms                                                | 46.5 ms: 1.20x slower                                      |
| mypy2                      | 380 ms                                                 | 461 ms: 1.21x slower                                       |
| python_startup_no_site     | 9.37 ms                                                | 11.6 ms: 1.24x slower                                      |
| telco                      | 3.68 ms                                                | 4.56 ms: 1.24x slower                                      |
| python_startup             | 11.4 ms                                                | 14.3 ms: 1.26x slower                                      |
| create_gc_cycles           | 701 us                                                 | 884 us: 1.26x slower                                       |
| Geometric mean             | (ref)                                                  | 1.06x faster                                               |

Benchmark hidden because not significant (5): asyncio_tcp, dask, pidigits, aiohttp, tornado_http
Ignored benchmarks (3) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (14) of results/bm-20240508-3.13.0b1-2268289/bm-20240508-darwin-arm64-python-v3.13.0b1-3.13.0b1-2268289.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.06x