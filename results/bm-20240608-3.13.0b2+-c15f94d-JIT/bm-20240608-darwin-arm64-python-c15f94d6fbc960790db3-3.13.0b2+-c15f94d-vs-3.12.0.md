# Results vs. 3.12.0

- fork: python
- ref: c15f94d6fbc960790db3
- machine: darwin-arm64
- commit hash: c15f94d
- commit date: 2024-06-08
- overall geometric mean: 1.05x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 0.64x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240608-darwin-arm64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 172 ms: 1.02x slower                                                   |
| chameleon      | 4.70 ms                                                | 4.47 ms: 1.05x faster                                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                                           |

Benchmark hidden because not significant (2): docutils, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240608-darwin-arm64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 323 ms                                                 | 239 ms: 1.35x faster                                                   |
| async_tree_none_tg         | 258 ms                                                 | 196 ms: 1.31x faster                                                   |
| async_tree_none            | 266 ms                                                 | 210 ms: 1.26x faster                                                   |
| async_tree_io_tg           | 669 ms                                                 | 537 ms: 1.25x faster                                                   |
| async_tree_io              | 668 ms                                                 | 550 ms: 1.21x faster                                                   |
| async_tree_memoization     | 312 ms                                                 | 258 ms: 1.21x faster                                                   |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 451 ms: 1.18x faster                                                   |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 467 ms: 1.12x faster                                                   |
| Geometric mean             | (ref)                                                  | 1.24x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240608-darwin-arm64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 47.5 ms: 1.17x faster                                                  |
| nbody          | 68.8 ms                                                | 63.7 ms: 1.08x faster                                                  |
| Geometric mean | (ref)                                                  | 1.08x faster                                                           |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240608-darwin-arm64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 77.9 ms                                                | 72.5 ms: 1.07x faster                                                  |
| regex_dna      | 154 ms                                                 | 149 ms: 1.04x faster                                                   |
| regex_effbot   | 2.64 ms                                                | 2.56 ms: 1.03x faster                                                  |
| regex_v8       | 16.0 ms                                                | 17.4 ms: 1.09x slower                                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240608-darwin-arm64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 200 us                                                 | 172 us: 1.16x faster                                                   |
| unpickle_pure_python | 151 us                                                 | 131 us: 1.15x faster                                                   |
| tomli_loads          | 1.39 sec                                               | 1.26 sec: 1.11x faster                                                 |
| xml_etree_process    | 39.7 ms                                                | 35.9 ms: 1.11x faster                                                  |
| xml_etree_generate   | 55.8 ms                                                | 51.7 ms: 1.08x faster                                                  |
| xml_etree_iterparse  | 74.0 ms                                                | 69.9 ms: 1.06x faster                                                  |
| unpickle_list        | 3.02 us                                                | 2.88 us: 1.05x faster                                                  |
| xml_etree_parse      | 106 ms                                                 | 102 ms: 1.05x faster                                                   |
| json_loads           | 17.2 us                                                | 16.9 us: 1.02x faster                                                  |
| json_dumps           | 6.22 ms                                                | 6.17 ms: 1.01x faster                                                  |
| unpickle             | 9.12 us                                                | 9.20 us: 1.01x slower                                                  |
| pickle_dict          | 18.1 us                                                | 18.4 us: 1.02x slower                                                  |
| pickle               | 7.23 us                                                | 7.40 us: 1.02x slower                                                  |
| pickle_list          | 2.89 us                                                | 3.00 us: 1.04x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240608-darwin-arm64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 9.37 ms                                                | 12.7 ms: 1.35x slower                                                  |
| python_startup         | 11.4 ms                                                | 15.6 ms: 1.37x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.36x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240608-darwin-arm64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 7.71 ms                                                | 6.37 ms: 1.21x faster                                                  |
| django_template | 22.3 ms                                                | 21.3 ms: 1.05x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.13x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240608-darwin-arm64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 323 ms                                                 | 239 ms: 1.35x faster                                                   |
| generators                 | 31.1 ms                                                | 23.4 ms: 1.33x faster                                                  |
| async_tree_none_tg         | 258 ms                                                 | 196 ms: 1.31x faster                                                   |
| raytrace                   | 212 ms                                                 | 163 ms: 1.30x faster                                                   |
| deepcopy_memo              | 27.7 us                                                | 21.6 us: 1.28x faster                                                  |
| async_tree_none            | 266 ms                                                 | 210 ms: 1.26x faster                                                   |
| async_tree_io_tg           | 669 ms                                                 | 537 ms: 1.25x faster                                                   |
| logging_silent             | 76.4 ns                                                | 62.6 ns: 1.22x faster                                                  |
| async_tree_io              | 668 ms                                                 | 550 ms: 1.21x faster                                                   |
| mako                       | 7.71 ms                                                | 6.37 ms: 1.21x faster                                                  |
| async_tree_memoization     | 312 ms                                                 | 258 ms: 1.21x faster                                                   |
| logging_simple             | 3.69 us                                                | 3.06 us: 1.20x faster                                                  |
| coroutines                 | 19.2 ms                                                | 16.0 ms: 1.20x faster                                                  |
| logging_format             | 3.98 us                                                | 3.35 us: 1.19x faster                                                  |
| comprehensions             | 14.5 us                                                | 12.3 us: 1.19x faster                                                  |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 451 ms: 1.18x faster                                                   |
| asyncio_tcp                | 449 ms                                                 | 382 ms: 1.18x faster                                                   |
| float                      | 55.8 ms                                                | 47.5 ms: 1.17x faster                                                  |
| pickle_pure_python         | 200 us                                                 | 172 us: 1.16x faster                                                   |
| unpickle_pure_python       | 151 us                                                 | 131 us: 1.15x faster                                                   |
| spectral_norm              | 76.4 ms                                                | 67.2 ms: 1.14x faster                                                  |
| deepcopy                   | 235 us                                                 | 209 us: 1.13x faster                                                   |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 467 ms: 1.12x faster                                                   |
| deepcopy_reduce            | 2.07 us                                                | 1.84 us: 1.12x faster                                                  |
| tomli_loads                | 1.39 sec                                               | 1.26 sec: 1.11x faster                                                 |
| xml_etree_process          | 39.7 ms                                                | 35.9 ms: 1.11x faster                                                  |
| nqueens                    | 62.4 ms                                                | 56.7 ms: 1.10x faster                                                  |
| mdp                        | 1.58 sec                                               | 1.44 sec: 1.09x faster                                                 |
| chaos                      | 42.5 ms                                                | 39.2 ms: 1.09x faster                                                  |
| deltablue                  | 2.71 ms                                                | 2.50 ms: 1.08x faster                                                  |
| sympy_sum                  | 77.6 ms                                                | 71.7 ms: 1.08x faster                                                  |
| pprint_safe_repr           | 497 ms                                                 | 460 ms: 1.08x faster                                                   |
| nbody                      | 68.8 ms                                                | 63.7 ms: 1.08x faster                                                  |
| xml_etree_generate         | 55.8 ms                                                | 51.7 ms: 1.08x faster                                                  |
| sympy_str                  | 148 ms                                                 | 137 ms: 1.08x faster                                                   |
| regex_compile              | 77.9 ms                                                | 72.5 ms: 1.07x faster                                                  |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 2.92 ms: 1.07x faster                                                  |
| pathlib                    | 24.2 ms                                                | 22.6 ms: 1.07x faster                                                  |
| fannkuch                   | 248 ms                                                 | 233 ms: 1.07x faster                                                   |
| pprint_pformat             | 1.01 sec                                               | 949 ms: 1.07x faster                                                   |
| xml_etree_iterparse        | 74.0 ms                                                | 69.9 ms: 1.06x faster                                                  |
| bench_thread_pool          | 504 us                                                 | 477 us: 1.06x faster                                                   |
| json                       | 3.09 ms                                                | 2.92 ms: 1.06x faster                                                  |
| scimark_fft                | 195 ms                                                 | 185 ms: 1.06x faster                                                   |
| chameleon                  | 4.70 ms                                                | 4.47 ms: 1.05x faster                                                  |
| django_template            | 22.3 ms                                                | 21.3 ms: 1.05x faster                                                  |
| unpickle_list              | 3.02 us                                                | 2.88 us: 1.05x faster                                                  |
| sympy_integrate            | 11.4 ms                                                | 10.9 ms: 1.05x faster                                                  |
| xml_etree_parse            | 106 ms                                                 | 102 ms: 1.05x faster                                                   |
| sqlglot_optimize           | 34.0 ms                                                | 32.7 ms: 1.04x faster                                                  |
| aiohttp                    | 1.08 ms                                                | 1.04 ms: 1.04x faster                                                  |
| hexiom                     | 4.54 ms                                                | 4.38 ms: 1.04x faster                                                  |
| regex_dna                  | 154 ms                                                 | 149 ms: 1.04x faster                                                   |
| regex_effbot               | 2.64 ms                                                | 2.56 ms: 1.03x faster                                                  |
| gunicorn                   | 1.15 ms                                                | 1.11 ms: 1.03x faster                                                  |
| async_generators           | 304 ms                                                 | 296 ms: 1.03x faster                                                   |
| sympy_expand               | 241 ms                                                 | 235 ms: 1.02x faster                                                   |
| sqlglot_parse              | 848 us                                                 | 828 us: 1.02x faster                                                   |
| dulwich_log                | 29.8 ms                                                | 29.2 ms: 1.02x faster                                                  |
| json_loads                 | 17.2 us                                                | 16.9 us: 1.02x faster                                                  |
| scimark_monte_carlo        | 45.0 ms                                                | 44.2 ms: 1.02x faster                                                  |
| sqlglot_transpile          | 1.02 ms                                                | 1.00 ms: 1.02x faster                                                  |
| pycparser                  | 677 ms                                                 | 668 ms: 1.01x faster                                                   |
| json_dumps                 | 6.22 ms                                                | 6.17 ms: 1.01x faster                                                  |
| pyflate                    | 316 ms                                                 | 313 ms: 1.01x faster                                                   |
| sqlite_synth               | 1.57 us                                                | 1.57 us: 1.00x faster                                                  |
| unpickle                   | 9.12 us                                                | 9.20 us: 1.01x slower                                                  |
| 2to3                       | 169 ms                                                 | 172 ms: 1.02x slower                                                   |
| richards                   | 32.1 ms                                                | 32.7 ms: 1.02x slower                                                  |
| pickle_dict                | 18.1 us                                                | 18.4 us: 1.02x slower                                                  |
| go                         | 102 ms                                                 | 104 ms: 1.02x slower                                                   |
| pickle                     | 7.23 us                                                | 7.40 us: 1.02x slower                                                  |
| richards_super             | 36.0 ms                                                | 36.9 ms: 1.02x slower                                                  |
| gc_traversal               | 2.40 ms                                                | 2.46 ms: 1.03x slower                                                  |
| pickle_list                | 2.89 us                                                | 3.00 us: 1.04x slower                                                  |
| scimark_lu                 | 76.0 ms                                                | 79.0 ms: 1.04x slower                                                  |
| mypy2                      | 380 ms                                                 | 405 ms: 1.06x slower                                                   |
| regex_v8                   | 16.0 ms                                                | 17.4 ms: 1.09x slower                                                  |
| bench_mp_pool              | 44.9 ms                                                | 49.6 ms: 1.10x slower                                                  |
| scimark_sor                | 87.4 ms                                                | 101 ms: 1.16x slower                                                   |
| coverage                   | 38.9 ms                                                | 45.9 ms: 1.18x slower                                                  |
| telco                      | 3.68 ms                                                | 4.56 ms: 1.24x slower                                                  |
| create_gc_cycles           | 701 us                                                 | 906 us: 1.29x slower                                                   |
| python_startup_no_site     | 9.37 ms                                                | 12.7 ms: 1.35x slower                                                  |
| python_startup             | 11.4 ms                                                | 15.6 ms: 1.37x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.05x faster                                                           |

Benchmark hidden because not significant (9): tornado_http, asyncio_tcp_ssl, dask, crypto_pyaes, meteor_contest, asyncio_websockets, docutils, pidigits, typing_runtime_protocols
Ignored benchmarks (4) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, unpack_sequence
Ignored benchmarks (14) of results/bm-20240608-3.13.0b2+-c15f94d-JIT/bm-20240608-darwin-arm64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 0.64x