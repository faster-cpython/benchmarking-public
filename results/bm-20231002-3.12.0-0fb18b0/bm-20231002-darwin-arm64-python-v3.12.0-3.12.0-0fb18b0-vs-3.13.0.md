# Results vs. 3.13.0

- fork: python
- ref: v3.12.0
- machine: darwin-arm64
- commit hash: 0fb18b0
- commit date: 2023-10-02
- overall geometric mean: 1.01x faster
- HPT reliability: 90.11%
- HPT 99th percentile: 1.00x faster
- Memory change: 5.78x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 178 ms                                                 | 169 ms: 1.05x faster                                   |
| chameleon      | 5.08 ms                                                | 4.70 ms: 1.08x faster                                  |
| docutils       | 1.44 sec                                               | 1.50 sec: 1.04x slower                                 |
| Geometric mean | (ref)                                                  | 1.05x faster                                           |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| coroutines                 | 19.8 ms                                                | 19.2 ms: 1.03x faster                                  |
| asyncio_tcp_ssl            | 1.26 sec                                               | 1.24 sec: 1.02x faster                                 |
| async_generators           | 294 ms                                                 | 304 ms: 1.03x slower                                   |
| async_tree_memoization_tg  | 291 ms                                                 | 323 ms: 1.11x slower                                   |
| async_tree_cpu_io_mixed    | 460 ms                                                 | 526 ms: 1.14x slower                                   |
| async_tree_memoization     | 270 ms                                                 | 312 ms: 1.15x slower                                   |
| async_tree_cpu_io_mixed_tg | 447 ms                                                 | 532 ms: 1.19x slower                                   |
| async_tree_none            | 212 ms                                                 | 266 ms: 1.25x slower                                   |
| async_tree_none_tg         | 198 ms                                                 | 258 ms: 1.30x slower                                   |
| async_tree_io              | 507 ms                                                 | 668 ms: 1.32x slower                                   |
| async_tree_io_tg           | 500 ms                                                 | 669 ms: 1.34x slower                                   |
| asyncio_websockets         | 241 ms                                                 | 409 ms: 1.70x slower                                   |
| Geometric mean             | (ref)                                                  | 1.18x slower                                           |

Benchmark hidden because not significant (1): asyncio_tcp

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 73.9 ms                                                | 68.8 ms: 1.07x faster                                  |
| float          | 56.2 ms                                                | 55.8 ms: 1.01x faster                                  |
| pidigits       | 284 ms                                                 | 282 ms: 1.01x faster                                   |
| Geometric mean | (ref)                                                  | 1.03x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_v8       | 16.9 ms                                                | 16.0 ms: 1.06x faster                                  |
| regex_compile  | 78.5 ms                                                | 77.9 ms: 1.01x faster                                  |
| regex_effbot   | 2.63 ms                                                | 2.64 ms: 1.00x slower                                  |
| regex_dna      | 148 ms                                                 | 154 ms: 1.05x slower                                   |
| Geometric mean | (ref)                                                  | 1.00x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| tomli_loads          | 1.56 sec                                               | 1.39 sec: 1.12x faster                                 |
| unpickle_pure_python | 163 us                                                 | 151 us: 1.08x faster                                   |
| pickle_pure_python   | 213 us                                                 | 200 us: 1.07x faster                                   |
| json_dumps           | 6.56 ms                                                | 6.22 ms: 1.05x faster                                  |
| pickle_list          | 2.99 us                                                | 2.89 us: 1.04x faster                                  |
| xml_etree_process    | 40.9 ms                                                | 39.7 ms: 1.03x faster                                  |
| xml_etree_parse      | 109 ms                                                 | 106 ms: 1.02x faster                                   |
| pickle               | 7.36 us                                                | 7.23 us: 1.02x faster                                  |
| xml_etree_generate   | 56.6 ms                                                | 55.8 ms: 1.01x faster                                  |
| pickle_dict          | 18.2 us                                                | 18.1 us: 1.01x faster                                  |
| unpickle             | 9.15 us                                                | 9.12 us: 1.00x faster                                  |
| json_loads           | 16.9 us                                                | 17.2 us: 1.02x slower                                  |
| unpickle_list        | 2.93 us                                                | 3.02 us: 1.03x slower                                  |
| Geometric mean       | (ref)                                                  | 1.03x faster                                           |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 17.0 ms                                                | 11.4 ms: 1.49x faster                                  |
| python_startup_no_site | 13.7 ms                                                | 9.37 ms: 1.46x faster                                  |
| Geometric mean         | (ref)                                                  | 1.47x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 7.68 ms                                                | 7.71 ms: 1.00x slower                                  |
| django_template | 22.2 ms                                                | 22.3 ms: 1.01x slower                                  |
| Geometric mean  | (ref)                                                  | 1.00x slower                                           |

All benchmarks:
===============

| Benchmark                  | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup             | 17.0 ms                                                | 11.4 ms: 1.49x faster                                  |
| python_startup_no_site     | 13.7 ms                                                | 9.37 ms: 1.46x faster                                  |
| telco                      | 4.80 ms                                                | 3.68 ms: 1.30x faster                                  |
| scimark_sor                | 106 ms                                                 | 87.4 ms: 1.21x faster                                  |
| coverage                   | 46.1 ms                                                | 38.9 ms: 1.19x faster                                  |
| aiohttp                    | 1.26 ms                                                | 1.08 ms: 1.17x faster                                  |
| dask                       | 255 ms                                                 | 222 ms: 1.15x faster                                   |
| unpack_sequence            | 36.1 ns                                                | 31.5 ns: 1.15x faster                                  |
| gunicorn                   | 1.31 ms                                                | 1.15 ms: 1.15x faster                                  |
| create_gc_cycles           | 803 us                                                 | 701 us: 1.15x faster                                   |
| bench_mp_pool              | 50.9 ms                                                | 44.9 ms: 1.13x faster                                  |
| fannkuch                   | 282 ms                                                 | 248 ms: 1.13x faster                                   |
| go                         | 115 ms                                                 | 102 ms: 1.13x faster                                   |
| scimark_monte_carlo        | 50.4 ms                                                | 45.0 ms: 1.12x faster                                  |
| tomli_loads                | 1.56 sec                                               | 1.39 sec: 1.12x faster                                 |
| pyflate                    | 351 ms                                                 | 316 ms: 1.11x faster                                   |
| richards                   | 35.4 ms                                                | 32.1 ms: 1.10x faster                                  |
| richards_super             | 39.1 ms                                                | 36.0 ms: 1.09x faster                                  |
| typing_runtime_protocols   | 101 us                                                 | 93.0 us: 1.09x faster                                  |
| unpickle_pure_python       | 163 us                                                 | 151 us: 1.08x faster                                   |
| chameleon                  | 5.08 ms                                                | 4.70 ms: 1.08x faster                                  |
| nbody                      | 73.9 ms                                                | 68.8 ms: 1.07x faster                                  |
| hexiom                     | 4.85 ms                                                | 4.54 ms: 1.07x faster                                  |
| pprint_safe_repr           | 531 ms                                                 | 497 ms: 1.07x faster                                   |
| pprint_pformat             | 1.08 sec                                               | 1.01 sec: 1.07x faster                                 |
| pickle_pure_python         | 213 us                                                 | 200 us: 1.07x faster                                   |
| regex_v8                   | 16.9 ms                                                | 16.0 ms: 1.06x faster                                  |
| json_dumps                 | 6.56 ms                                                | 6.22 ms: 1.05x faster                                  |
| 2to3                       | 178 ms                                                 | 169 ms: 1.05x faster                                   |
| pycparser                  | 706 ms                                                 | 677 ms: 1.04x faster                                   |
| crypto_pyaes               | 54.0 ms                                                | 51.9 ms: 1.04x faster                                  |
| mypy2                      | 396 ms                                                 | 380 ms: 1.04x faster                                   |
| pickle_list                | 2.99 us                                                | 2.89 us: 1.04x faster                                  |
| gc_traversal               | 2.48 ms                                                | 2.40 ms: 1.03x faster                                  |
| xml_etree_process          | 40.9 ms                                                | 39.7 ms: 1.03x faster                                  |
| meteor_contest             | 73.8 ms                                                | 71.7 ms: 1.03x faster                                  |
| coroutines                 | 19.8 ms                                                | 19.2 ms: 1.03x faster                                  |
| scimark_fft                | 201 ms                                                 | 195 ms: 1.03x faster                                   |
| sqlglot_optimize           | 34.9 ms                                                | 34.0 ms: 1.03x faster                                  |
| xml_etree_parse            | 109 ms                                                 | 106 ms: 1.02x faster                                   |
| sympy_expand               | 246 ms                                                 | 241 ms: 1.02x faster                                   |
| pickle                     | 7.36 us                                                | 7.23 us: 1.02x faster                                  |
| asyncio_tcp_ssl            | 1.26 sec                                               | 1.24 sec: 1.02x faster                                 |
| sqlglot_normalize          | 189 ms                                                 | 186 ms: 1.02x faster                                   |
| xml_etree_generate         | 56.6 ms                                                | 55.8 ms: 1.01x faster                                  |
| generators                 | 31.5 ms                                                | 31.1 ms: 1.01x faster                                  |
| spectral_norm              | 77.3 ms                                                | 76.4 ms: 1.01x faster                                  |
| sqlglot_parse              | 856 us                                                 | 848 us: 1.01x faster                                   |
| float                      | 56.2 ms                                                | 55.8 ms: 1.01x faster                                  |
| regex_compile              | 78.5 ms                                                | 77.9 ms: 1.01x faster                                  |
| scimark_lu                 | 76.5 ms                                                | 76.0 ms: 1.01x faster                                  |
| nqueens                    | 62.9 ms                                                | 62.4 ms: 1.01x faster                                  |
| pickle_dict                | 18.2 us                                                | 18.1 us: 1.01x faster                                  |
| pidigits                   | 284 ms                                                 | 282 ms: 1.01x faster                                   |
| bench_thread_pool          | 506 us                                                 | 504 us: 1.00x faster                                   |
| unpickle                   | 9.15 us                                                | 9.12 us: 1.00x faster                                  |
| sqlglot_transpile          | 1.02 ms                                                | 1.02 ms: 1.00x faster                                  |
| sympy_integrate            | 11.3 ms                                                | 11.4 ms: 1.00x slower                                  |
| mako                       | 7.68 ms                                                | 7.71 ms: 1.00x slower                                  |
| regex_effbot               | 2.63 ms                                                | 2.64 ms: 1.00x slower                                  |
| deepcopy_reduce            | 2.06 us                                                | 2.07 us: 1.01x slower                                  |
| django_template            | 22.2 ms                                                | 22.3 ms: 1.01x slower                                  |
| deltablue                  | 2.68 ms                                                | 2.71 ms: 1.01x slower                                  |
| deepcopy                   | 232 us                                                 | 235 us: 1.01x slower                                   |
| sympy_str                  | 145 ms                                                 | 148 ms: 1.01x slower                                   |
| deepcopy_memo              | 27.2 us                                                | 27.7 us: 1.02x slower                                  |
| sqlite_synth               | 1.54 us                                                | 1.57 us: 1.02x slower                                  |
| json_loads                 | 16.9 us                                                | 17.2 us: 1.02x slower                                  |
| sympy_sum                  | 75.6 ms                                                | 77.6 ms: 1.03x slower                                  |
| chaos                      | 41.3 ms                                                | 42.5 ms: 1.03x slower                                  |
| logging_simple             | 3.57 us                                                | 3.69 us: 1.03x slower                                  |
| unpickle_list              | 2.93 us                                                | 3.02 us: 1.03x slower                                  |
| logging_format             | 3.85 us                                                | 3.98 us: 1.03x slower                                  |
| async_generators           | 294 ms                                                 | 304 ms: 1.03x slower                                   |
| dulwich_log                | 28.7 ms                                                | 29.8 ms: 1.04x slower                                  |
| docutils                   | 1.44 sec                                               | 1.50 sec: 1.04x slower                                 |
| regex_dna                  | 148 ms                                                 | 154 ms: 1.05x slower                                   |
| scimark_sparse_mat_mult    | 2.99 ms                                                | 3.14 ms: 1.05x slower                                  |
| json                       | 2.94 ms                                                | 3.09 ms: 1.05x slower                                  |
| mdp                        | 1.50 sec                                               | 1.58 sec: 1.05x slower                                 |
| pathlib                    | 22.8 ms                                                | 24.2 ms: 1.06x slower                                  |
| logging_silent             | 69.9 ns                                                | 76.4 ns: 1.09x slower                                  |
| async_tree_memoization_tg  | 291 ms                                                 | 323 ms: 1.11x slower                                   |
| async_tree_cpu_io_mixed    | 460 ms                                                 | 526 ms: 1.14x slower                                   |
| async_tree_memoization     | 270 ms                                                 | 312 ms: 1.15x slower                                   |
| raytrace                   | 182 ms                                                 | 212 ms: 1.17x slower                                   |
| async_tree_cpu_io_mixed_tg | 447 ms                                                 | 532 ms: 1.19x slower                                   |
| comprehensions             | 12.2 us                                                | 14.5 us: 1.20x slower                                  |
| async_tree_none            | 212 ms                                                 | 266 ms: 1.25x slower                                   |
| async_tree_none_tg         | 198 ms                                                 | 258 ms: 1.30x slower                                   |
| async_tree_io              | 507 ms                                                 | 668 ms: 1.32x slower                                   |
| async_tree_io_tg           | 500 ms                                                 | 669 ms: 1.34x slower                                   |
| asyncio_websockets         | 241 ms                                                 | 409 ms: 1.70x slower                                   |
| Geometric mean             | (ref)                                                  | 1.01x faster                                           |

Benchmark hidden because not significant (3): tornado_http, asyncio_tcp, xml_etree_iterparse
Ignored benchmarks (15) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
Ignored benchmarks (2) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: sqlalchemy_declarative, sqlalchemy_imperative

# HPT report

- Reliability score: 90.11% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 5.78x