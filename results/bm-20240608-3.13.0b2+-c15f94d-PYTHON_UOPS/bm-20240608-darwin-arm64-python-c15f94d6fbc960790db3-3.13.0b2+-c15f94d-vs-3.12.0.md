# Results vs. 3.12.0

- fork: python
- ref: c15f94d6fbc960790db3
- machine: darwin-arm64
- commit hash: c15f94d
- commit date: 2024-06-08
- overall geometric mean: 1.06x slower
- HPT reliability: 99.77%
- HPT 99th percentile: 1.01x slower
- Memory change: 0.85x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240608-darwin-arm64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 181 ms: 1.07x slower                                                   |
| chameleon      | 4.70 ms                                                | 4.97 ms: 1.06x slower                                                  |
| docutils       | 1.50 sec                                               | 1.66 sec: 1.11x slower                                                 |
| Geometric mean | (ref)                                                  | 1.06x slower                                                           |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240608-darwin-arm64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_none_tg         | 258 ms                                                 | 205 ms: 1.26x faster                                                   |
| async_tree_memoization_tg  | 323 ms                                                 | 257 ms: 1.25x faster                                                   |
| async_tree_io_tg           | 669 ms                                                 | 550 ms: 1.22x faster                                                   |
| async_tree_none            | 266 ms                                                 | 221 ms: 1.20x faster                                                   |
| async_tree_io              | 668 ms                                                 | 568 ms: 1.18x faster                                                   |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 456 ms: 1.17x faster                                                   |
| async_tree_memoization     | 312 ms                                                 | 269 ms: 1.16x faster                                                   |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 476 ms: 1.10x faster                                                   |
| Geometric mean             | (ref)                                                  | 1.19x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240608-darwin-arm64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pidigits       | 282 ms                                                 | 283 ms: 1.00x slower                                                   |
| float          | 55.8 ms                                                | 60.7 ms: 1.09x slower                                                  |
| nbody          | 68.8 ms                                                | 76.8 ms: 1.12x slower                                                  |
| Geometric mean | (ref)                                                  | 1.07x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240608-darwin-arm64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_dna      | 154 ms                                                 | 149 ms: 1.04x faster                                                   |
| regex_effbot   | 2.64 ms                                                | 2.58 ms: 1.02x faster                                                  |
| regex_v8       | 16.0 ms                                                | 17.6 ms: 1.10x slower                                                  |
| regex_compile  | 77.9 ms                                                | 96.0 ms: 1.23x slower                                                  |
| Geometric mean | (ref)                                                  | 1.06x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240608-darwin-arm64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_parse      | 106 ms                                                 | 103 ms: 1.03x faster                                                   |
| unpickle_list        | 3.02 us                                                | 2.94 us: 1.03x faster                                                  |
| json_loads           | 17.2 us                                                | 16.9 us: 1.02x faster                                                  |
| pickle_dict          | 18.1 us                                                | 18.2 us: 1.01x slower                                                  |
| unpickle             | 9.12 us                                                | 9.31 us: 1.02x slower                                                  |
| xml_etree_iterparse  | 74.0 ms                                                | 76.0 ms: 1.03x slower                                                  |
| xml_etree_process    | 39.7 ms                                                | 41.2 ms: 1.04x slower                                                  |
| pickle_list          | 2.89 us                                                | 3.00 us: 1.04x slower                                                  |
| pickle               | 7.23 us                                                | 7.52 us: 1.04x slower                                                  |
| xml_etree_generate   | 55.8 ms                                                | 59.0 ms: 1.06x slower                                                  |
| json_dumps           | 6.22 ms                                                | 6.60 ms: 1.06x slower                                                  |
| pickle_pure_python   | 200 us                                                 | 226 us: 1.13x slower                                                   |
| unpickle_pure_python | 151 us                                                 | 175 us: 1.16x slower                                                   |
| tomli_loads          | 1.39 sec                                               | 1.63 sec: 1.17x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.05x slower                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240608-darwin-arm64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 9.37 ms                                                | 11.4 ms: 1.21x slower                                                  |
| python_startup         | 11.4 ms                                                | 14.3 ms: 1.25x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.23x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240608-darwin-arm64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 22.3 ms                                                | 23.6 ms: 1.06x slower                                                  |
| mako            | 7.71 ms                                                | 8.85 ms: 1.15x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.10x slower                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240608-darwin-arm64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| generators                 | 31.1 ms                                                | 23.4 ms: 1.33x faster                                                  |
| async_tree_none_tg         | 258 ms                                                 | 205 ms: 1.26x faster                                                   |
| async_tree_memoization_tg  | 323 ms                                                 | 257 ms: 1.25x faster                                                   |
| async_tree_io_tg           | 669 ms                                                 | 550 ms: 1.22x faster                                                   |
| async_tree_none            | 266 ms                                                 | 221 ms: 1.20x faster                                                   |
| coroutines                 | 19.2 ms                                                | 16.2 ms: 1.19x faster                                                  |
| async_tree_io              | 668 ms                                                 | 568 ms: 1.18x faster                                                   |
| raytrace                   | 212 ms                                                 | 180 ms: 1.17x faster                                                   |
| logging_simple             | 3.69 us                                                | 3.16 us: 1.17x faster                                                  |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 456 ms: 1.17x faster                                                   |
| async_tree_memoization     | 312 ms                                                 | 269 ms: 1.16x faster                                                   |
| logging_format             | 3.98 us                                                | 3.46 us: 1.15x faster                                                  |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 476 ms: 1.10x faster                                                   |
| pathlib                    | 24.2 ms                                                | 22.7 ms: 1.07x faster                                                  |
| regex_dna                  | 154 ms                                                 | 149 ms: 1.04x faster                                                   |
| async_generators           | 304 ms                                                 | 294 ms: 1.03x faster                                                   |
| xml_etree_parse            | 106 ms                                                 | 103 ms: 1.03x faster                                                   |
| unpickle_list              | 3.02 us                                                | 2.94 us: 1.03x faster                                                  |
| regex_effbot               | 2.64 ms                                                | 2.58 ms: 1.02x faster                                                  |
| aiohttp                    | 1.08 ms                                                | 1.06 ms: 1.02x faster                                                  |
| gunicorn                   | 1.15 ms                                                | 1.12 ms: 1.02x faster                                                  |
| json_loads                 | 17.2 us                                                | 16.9 us: 1.02x faster                                                  |
| json                       | 3.09 ms                                                | 3.03 ms: 1.02x faster                                                  |
| mdp                        | 1.58 sec                                               | 1.56 sec: 1.01x faster                                                 |
| dulwich_log                | 29.8 ms                                                | 29.5 ms: 1.01x faster                                                  |
| pidigits                   | 282 ms                                                 | 283 ms: 1.00x slower                                                   |
| pickle_dict                | 18.1 us                                                | 18.2 us: 1.01x slower                                                  |
| unpickle                   | 9.12 us                                                | 9.31 us: 1.02x slower                                                  |
| dask                       | 222 ms                                                 | 227 ms: 1.02x slower                                                   |
| gc_traversal               | 2.40 ms                                                | 2.46 ms: 1.02x slower                                                  |
| deepcopy_reduce            | 2.07 us                                                | 2.12 us: 1.02x slower                                                  |
| xml_etree_iterparse        | 74.0 ms                                                | 76.0 ms: 1.03x slower                                                  |
| sqlite_synth               | 1.57 us                                                | 1.62 us: 1.03x slower                                                  |
| bench_thread_pool          | 504 us                                                 | 522 us: 1.03x slower                                                   |
| xml_etree_process          | 39.7 ms                                                | 41.2 ms: 1.04x slower                                                  |
| pickle_list                | 2.89 us                                                | 3.00 us: 1.04x slower                                                  |
| pickle                     | 7.23 us                                                | 7.52 us: 1.04x slower                                                  |
| xml_etree_generate         | 55.8 ms                                                | 59.0 ms: 1.06x slower                                                  |
| django_template            | 22.3 ms                                                | 23.6 ms: 1.06x slower                                                  |
| bench_mp_pool              | 44.9 ms                                                | 47.4 ms: 1.06x slower                                                  |
| chameleon                  | 4.70 ms                                                | 4.97 ms: 1.06x slower                                                  |
| json_dumps                 | 6.22 ms                                                | 6.60 ms: 1.06x slower                                                  |
| 2to3                       | 169 ms                                                 | 181 ms: 1.07x slower                                                   |
| pycparser                  | 677 ms                                                 | 723 ms: 1.07x slower                                                   |
| deepcopy                   | 235 us                                                 | 251 us: 1.07x slower                                                   |
| nqueens                    | 62.4 ms                                                | 67.5 ms: 1.08x slower                                                  |
| deltablue                  | 2.71 ms                                                | 2.94 ms: 1.09x slower                                                  |
| sqlglot_optimize           | 34.0 ms                                                | 37.0 ms: 1.09x slower                                                  |
| float                      | 55.8 ms                                                | 60.7 ms: 1.09x slower                                                  |
| chaos                      | 42.5 ms                                                | 46.4 ms: 1.09x slower                                                  |
| sympy_sum                  | 77.6 ms                                                | 84.9 ms: 1.09x slower                                                  |
| sympy_expand               | 241 ms                                                 | 264 ms: 1.09x slower                                                   |
| meteor_contest             | 71.7 ms                                                | 78.6 ms: 1.10x slower                                                  |
| regex_v8                   | 16.0 ms                                                | 17.6 ms: 1.10x slower                                                  |
| sympy_integrate            | 11.4 ms                                                | 12.5 ms: 1.10x slower                                                  |
| docutils                   | 1.50 sec                                               | 1.66 sec: 1.11x slower                                                 |
| sympy_str                  | 148 ms                                                 | 164 ms: 1.11x slower                                                   |
| nbody                      | 68.8 ms                                                | 76.8 ms: 1.12x slower                                                  |
| sqlglot_parse              | 848 us                                                 | 952 us: 1.12x slower                                                   |
| mypy2                      | 380 ms                                                 | 428 ms: 1.13x slower                                                   |
| pickle_pure_python         | 200 us                                                 | 226 us: 1.13x slower                                                   |
| richards_super             | 36.0 ms                                                | 40.8 ms: 1.13x slower                                                  |
| sqlglot_transpile          | 1.02 ms                                                | 1.16 ms: 1.13x slower                                                  |
| typing_runtime_protocols   | 93.0 us                                                | 106 us: 1.14x slower                                                   |
| scimark_fft                | 195 ms                                                 | 223 ms: 1.14x slower                                                   |
| mako                       | 7.71 ms                                                | 8.85 ms: 1.15x slower                                                  |
| go                         | 102 ms                                                 | 117 ms: 1.15x slower                                                   |
| unpickle_pure_python       | 151 us                                                 | 175 us: 1.16x slower                                                   |
| richards                   | 32.1 ms                                                | 37.4 ms: 1.16x slower                                                  |
| pprint_safe_repr           | 497 ms                                                 | 579 ms: 1.16x slower                                                   |
| pprint_pformat             | 1.01 sec                                               | 1.18 sec: 1.17x slower                                                 |
| tomli_loads                | 1.39 sec                                               | 1.63 sec: 1.17x slower                                                 |
| crypto_pyaes               | 51.9 ms                                                | 60.8 ms: 1.17x slower                                                  |
| deepcopy_memo              | 27.7 us                                                | 32.6 us: 1.18x slower                                                  |
| coverage                   | 38.9 ms                                                | 46.0 ms: 1.18x slower                                                  |
| comprehensions             | 14.5 us                                                | 17.3 us: 1.19x slower                                                  |
| spectral_norm              | 76.4 ms                                                | 92.1 ms: 1.21x slower                                                  |
| python_startup_no_site     | 9.37 ms                                                | 11.4 ms: 1.21x slower                                                  |
| scimark_sor                | 87.4 ms                                                | 107 ms: 1.23x slower                                                   |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 3.86 ms: 1.23x slower                                                  |
| regex_compile              | 77.9 ms                                                | 96.0 ms: 1.23x slower                                                  |
| logging_silent             | 76.4 ns                                                | 94.6 ns: 1.24x slower                                                  |
| fannkuch                   | 248 ms                                                 | 308 ms: 1.24x slower                                                   |
| python_startup             | 11.4 ms                                                | 14.3 ms: 1.25x slower                                                  |
| pyflate                    | 316 ms                                                 | 395 ms: 1.25x slower                                                   |
| scimark_lu                 | 76.0 ms                                                | 97.1 ms: 1.28x slower                                                  |
| create_gc_cycles           | 701 us                                                 | 903 us: 1.29x slower                                                   |
| hexiom                     | 4.54 ms                                                | 5.92 ms: 1.30x slower                                                  |
| telco                      | 3.68 ms                                                | 4.96 ms: 1.35x slower                                                  |
| scimark_monte_carlo        | 45.0 ms                                                | 60.8 ms: 1.35x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.06x slower                                                           |

Benchmark hidden because not significant (4): asyncio_tcp, asyncio_tcp_ssl, asyncio_websockets, tornado_http
Ignored benchmarks (4) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, unpack_sequence
Ignored benchmarks (14) of results/bm-20240608-3.13.0b2+-c15f94d-PYTHON_UOPS/bm-20240608-darwin-arm64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 99.77% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 0.85x