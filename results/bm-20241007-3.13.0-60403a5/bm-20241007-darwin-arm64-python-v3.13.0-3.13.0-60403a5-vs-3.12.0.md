# Results vs. 3.12.0

- fork: python
- ref: v3.13.0
- machine: darwin-arm64
- commit hash: 60403a5
- commit date: 2024-10-07
- overall geometric mean: 1.01x slower
- HPT reliability: 90.11%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.49x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 178 ms: 1.05x slower                                   |
| chameleon      | 4.70 ms                                                | 5.08 ms: 1.08x slower                                  |
| docutils       | 1.50 sec                                               | 1.44 sec: 1.04x faster                                 |
| Geometric mean | (ref)                                                  | 1.05x slower                                           |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| async_tree_io_tg           | 669 ms                                                 | 500 ms: 1.34x faster                                   |
| async_tree_io              | 668 ms                                                 | 507 ms: 1.32x faster                                   |
| async_tree_none_tg         | 258 ms                                                 | 198 ms: 1.30x faster                                   |
| async_tree_none            | 266 ms                                                 | 212 ms: 1.25x faster                                   |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 447 ms: 1.19x faster                                   |
| async_tree_memoization     | 312 ms                                                 | 270 ms: 1.15x faster                                   |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 460 ms: 1.14x faster                                   |
| async_tree_memoization_tg  | 323 ms                                                 | 291 ms: 1.11x faster                                   |
| Geometric mean             | (ref)                                                  | 1.22x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pidigits       | 282 ms                                                 | 284 ms: 1.01x slower                                   |
| float          | 55.8 ms                                                | 56.2 ms: 1.01x slower                                  |
| nbody          | 68.8 ms                                                | 73.9 ms: 1.07x slower                                  |
| Geometric mean | (ref)                                                  | 1.03x slower                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_dna      | 154 ms                                                 | 148 ms: 1.05x faster                                   |
| regex_effbot   | 2.64 ms                                                | 2.63 ms: 1.00x faster                                  |
| regex_compile  | 77.9 ms                                                | 78.5 ms: 1.01x slower                                  |
| regex_v8       | 16.0 ms                                                | 16.9 ms: 1.06x slower                                  |
| Geometric mean | (ref)                                                  | 1.00x slower                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| unpickle_list        | 3.02 us                                                | 2.93 us: 1.03x faster                                  |
| json_loads           | 17.2 us                                                | 16.9 us: 1.02x faster                                  |
| unpickle             | 9.12 us                                                | 9.15 us: 1.00x slower                                  |
| pickle_dict          | 18.1 us                                                | 18.2 us: 1.01x slower                                  |
| xml_etree_generate   | 55.8 ms                                                | 56.6 ms: 1.01x slower                                  |
| pickle               | 7.23 us                                                | 7.36 us: 1.02x slower                                  |
| xml_etree_parse      | 106 ms                                                 | 109 ms: 1.02x slower                                   |
| xml_etree_process    | 39.7 ms                                                | 40.9 ms: 1.03x slower                                  |
| pickle_list          | 2.89 us                                                | 2.99 us: 1.04x slower                                  |
| json_dumps           | 6.22 ms                                                | 6.56 ms: 1.05x slower                                  |
| pickle_pure_python   | 200 us                                                 | 213 us: 1.07x slower                                   |
| unpickle_pure_python | 151 us                                                 | 163 us: 1.08x slower                                   |
| tomli_loads          | 1.39 sec                                               | 1.56 sec: 1.12x slower                                 |
| Geometric mean       | (ref)                                                  | 1.03x slower                                           |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup_no_site | 9.37 ms                                                | 13.7 ms: 1.46x slower                                  |
| python_startup         | 11.4 ms                                                | 17.0 ms: 1.49x slower                                  |
| Geometric mean         | (ref)                                                  | 1.47x slower                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| django_template | 22.3 ms                                                | 22.2 ms: 1.01x faster                                  |
| mako            | 7.71 ms                                                | 7.68 ms: 1.00x faster                                  |
| Geometric mean  | (ref)                                                  | 1.00x faster                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| asyncio_websockets         | 409 ms                                                 | 241 ms: 1.70x faster                                   |
| async_tree_io_tg           | 669 ms                                                 | 500 ms: 1.34x faster                                   |
| async_tree_io              | 668 ms                                                 | 507 ms: 1.32x faster                                   |
| async_tree_none_tg         | 258 ms                                                 | 198 ms: 1.30x faster                                   |
| async_tree_none            | 266 ms                                                 | 212 ms: 1.25x faster                                   |
| comprehensions             | 14.5 us                                                | 12.2 us: 1.20x faster                                  |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 447 ms: 1.19x faster                                   |
| raytrace                   | 212 ms                                                 | 182 ms: 1.17x faster                                   |
| async_tree_memoization     | 312 ms                                                 | 270 ms: 1.15x faster                                   |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 460 ms: 1.14x faster                                   |
| async_tree_memoization_tg  | 323 ms                                                 | 291 ms: 1.11x faster                                   |
| logging_silent             | 76.4 ns                                                | 69.9 ns: 1.09x faster                                  |
| pathlib                    | 24.2 ms                                                | 22.8 ms: 1.06x faster                                  |
| mdp                        | 1.58 sec                                               | 1.50 sec: 1.05x faster                                 |
| json                       | 3.09 ms                                                | 2.94 ms: 1.05x faster                                  |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 2.99 ms: 1.05x faster                                  |
| regex_dna                  | 154 ms                                                 | 148 ms: 1.05x faster                                   |
| docutils                   | 1.50 sec                                               | 1.44 sec: 1.04x faster                                 |
| dulwich_log                | 29.8 ms                                                | 28.7 ms: 1.04x faster                                  |
| async_generators           | 304 ms                                                 | 294 ms: 1.03x faster                                   |
| logging_format             | 3.98 us                                                | 3.85 us: 1.03x faster                                  |
| unpickle_list              | 3.02 us                                                | 2.93 us: 1.03x faster                                  |
| logging_simple             | 3.69 us                                                | 3.57 us: 1.03x faster                                  |
| chaos                      | 42.5 ms                                                | 41.3 ms: 1.03x faster                                  |
| sympy_sum                  | 77.6 ms                                                | 75.6 ms: 1.03x faster                                  |
| json_loads                 | 17.2 us                                                | 16.9 us: 1.02x faster                                  |
| sqlite_synth               | 1.57 us                                                | 1.54 us: 1.02x faster                                  |
| deepcopy_memo              | 27.7 us                                                | 27.2 us: 1.02x faster                                  |
| sympy_str                  | 148 ms                                                 | 145 ms: 1.01x faster                                   |
| deepcopy                   | 235 us                                                 | 232 us: 1.01x faster                                   |
| deltablue                  | 2.71 ms                                                | 2.68 ms: 1.01x faster                                  |
| django_template            | 22.3 ms                                                | 22.2 ms: 1.01x faster                                  |
| deepcopy_reduce            | 2.07 us                                                | 2.06 us: 1.01x faster                                  |
| regex_effbot               | 2.64 ms                                                | 2.63 ms: 1.00x faster                                  |
| mako                       | 7.71 ms                                                | 7.68 ms: 1.00x faster                                  |
| sympy_integrate            | 11.4 ms                                                | 11.3 ms: 1.00x faster                                  |
| sqlglot_transpile          | 1.02 ms                                                | 1.02 ms: 1.00x slower                                  |
| unpickle                   | 9.12 us                                                | 9.15 us: 1.00x slower                                  |
| bench_thread_pool          | 504 us                                                 | 506 us: 1.00x slower                                   |
| pidigits                   | 282 ms                                                 | 284 ms: 1.01x slower                                   |
| pickle_dict                | 18.1 us                                                | 18.2 us: 1.01x slower                                  |
| nqueens                    | 62.4 ms                                                | 62.9 ms: 1.01x slower                                  |
| scimark_lu                 | 76.0 ms                                                | 76.5 ms: 1.01x slower                                  |
| regex_compile              | 77.9 ms                                                | 78.5 ms: 1.01x slower                                  |
| float                      | 55.8 ms                                                | 56.2 ms: 1.01x slower                                  |
| sqlglot_parse              | 848 us                                                 | 856 us: 1.01x slower                                   |
| spectral_norm              | 76.4 ms                                                | 77.3 ms: 1.01x slower                                  |
| generators                 | 31.1 ms                                                | 31.5 ms: 1.01x slower                                  |
| xml_etree_generate         | 55.8 ms                                                | 56.6 ms: 1.01x slower                                  |
| sqlglot_normalize          | 186 ms                                                 | 189 ms: 1.02x slower                                   |
| asyncio_tcp_ssl            | 1.24 sec                                               | 1.26 sec: 1.02x slower                                 |
| pickle                     | 7.23 us                                                | 7.36 us: 1.02x slower                                  |
| sympy_expand               | 241 ms                                                 | 246 ms: 1.02x slower                                   |
| xml_etree_parse            | 106 ms                                                 | 109 ms: 1.02x slower                                   |
| sqlglot_optimize           | 34.0 ms                                                | 34.9 ms: 1.03x slower                                  |
| scimark_fft                | 195 ms                                                 | 201 ms: 1.03x slower                                   |
| coroutines                 | 19.2 ms                                                | 19.8 ms: 1.03x slower                                  |
| meteor_contest             | 71.7 ms                                                | 73.8 ms: 1.03x slower                                  |
| xml_etree_process          | 39.7 ms                                                | 40.9 ms: 1.03x slower                                  |
| gc_traversal               | 2.40 ms                                                | 2.48 ms: 1.03x slower                                  |
| pickle_list                | 2.89 us                                                | 2.99 us: 1.04x slower                                  |
| mypy2                      | 380 ms                                                 | 396 ms: 1.04x slower                                   |
| crypto_pyaes               | 51.9 ms                                                | 54.0 ms: 1.04x slower                                  |
| pycparser                  | 677 ms                                                 | 706 ms: 1.04x slower                                   |
| 2to3                       | 169 ms                                                 | 178 ms: 1.05x slower                                   |
| json_dumps                 | 6.22 ms                                                | 6.56 ms: 1.05x slower                                  |
| regex_v8                   | 16.0 ms                                                | 16.9 ms: 1.06x slower                                  |
| pickle_pure_python         | 200 us                                                 | 213 us: 1.07x slower                                   |
| pprint_pformat             | 1.01 sec                                               | 1.08 sec: 1.07x slower                                 |
| pprint_safe_repr           | 497 ms                                                 | 531 ms: 1.07x slower                                   |
| hexiom                     | 4.54 ms                                                | 4.85 ms: 1.07x slower                                  |
| nbody                      | 68.8 ms                                                | 73.9 ms: 1.07x slower                                  |
| chameleon                  | 4.70 ms                                                | 5.08 ms: 1.08x slower                                  |
| unpickle_pure_python       | 151 us                                                 | 163 us: 1.08x slower                                   |
| typing_runtime_protocols   | 93.0 us                                                | 101 us: 1.09x slower                                   |
| richards_super             | 36.0 ms                                                | 39.1 ms: 1.09x slower                                  |
| richards                   | 32.1 ms                                                | 35.4 ms: 1.10x slower                                  |
| pyflate                    | 316 ms                                                 | 351 ms: 1.11x slower                                   |
| tomli_loads                | 1.39 sec                                               | 1.56 sec: 1.12x slower                                 |
| scimark_monte_carlo        | 45.0 ms                                                | 50.4 ms: 1.12x slower                                  |
| go                         | 102 ms                                                 | 115 ms: 1.13x slower                                   |
| fannkuch                   | 248 ms                                                 | 282 ms: 1.13x slower                                   |
| bench_mp_pool              | 44.9 ms                                                | 50.9 ms: 1.13x slower                                  |
| create_gc_cycles           | 701 us                                                 | 803 us: 1.15x slower                                   |
| gunicorn                   | 1.15 ms                                                | 1.31 ms: 1.15x slower                                  |
| unpack_sequence            | 31.5 ns                                                | 36.1 ns: 1.15x slower                                  |
| dask                       | 222 ms                                                 | 255 ms: 1.15x slower                                   |
| aiohttp                    | 1.08 ms                                                | 1.26 ms: 1.17x slower                                  |
| coverage                   | 38.9 ms                                                | 46.1 ms: 1.19x slower                                  |
| scimark_sor                | 87.4 ms                                                | 106 ms: 1.21x slower                                   |
| telco                      | 3.68 ms                                                | 4.80 ms: 1.30x slower                                  |
| python_startup_no_site     | 9.37 ms                                                | 13.7 ms: 1.46x slower                                  |
| python_startup             | 11.4 ms                                                | 17.0 ms: 1.49x slower                                  |
| Geometric mean             | (ref)                                                  | 1.01x slower                                           |

Benchmark hidden because not significant (3): xml_etree_iterparse, asyncio_tcp, tornado_http
Ignored benchmarks (2) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (15) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 90.11% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.49x