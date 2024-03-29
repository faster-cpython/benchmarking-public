
# Results vs. 3.11.0

- fork: python
- ref: 1ae7ceba29771baf8f2e
- machine: darwin-arm64
- commit hash: 1ae7ceb
- commit date: 2024-01-04
- overall geometric mean: 1.04x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20240104-darwin-arm64-python-1ae7ceba29771baf8f2e-3.13.0a2+-1ae7ceb |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 154 ms                                                 | 173 ms: 1.12x slower                                                   |
| chameleon      | 4.30 ms                                                | 4.81 ms: 1.12x slower                                                  |
| docutils       | 1.43 sec                                               | 1.49 sec: 1.04x slower                                                 |
| Geometric mean | (ref)                                                  | 1.07x slower                                                           |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20240104-darwin-arm64-python-1ae7ceba29771baf8f2e-3.13.0a2+-1ae7ceb |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_none            | 282 ms                                                 | 250 ms: 1.13x faster                                                   |
| async_tree_memoization_tg  | 352 ms                                                 | 322 ms: 1.10x faster                                                   |
| async_tree_io_tg           | 724 ms                                                 | 672 ms: 1.08x faster                                                   |
| async_tree_none_tg         | 276 ms                                                 | 259 ms: 1.07x faster                                                   |
| async_tree_cpu_io_mixed_tg | 550 ms                                                 | 533 ms: 1.03x faster                                                   |
| async_tree_memoization     | 336 ms                                                 | 328 ms: 1.03x faster                                                   |
| async_tree_cpu_io_mixed    | 519 ms                                                 | 522 ms: 1.01x slower                                                   |
| async_tree_io              | 697 ms                                                 | 709 ms: 1.02x slower                                                   |
| Geometric mean             | (ref)                                                  | 1.05x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20240104-darwin-arm64-python-1ae7ceba29771baf8f2e-3.13.0a2+-1ae7ceb |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pidigits       | 280 ms                                                 | 283 ms: 1.01x slower                                                   |
| float          | 50.8 ms                                                | 57.9 ms: 1.14x slower                                                  |
| nbody          | 61.7 ms                                                | 79.0 ms: 1.28x slower                                                  |
| Geometric mean | (ref)                                                  | 1.14x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20240104-darwin-arm64-python-1ae7ceba29771baf8f2e-3.13.0a2+-1ae7ceb |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_dna      | 148 ms                                                 | 148 ms: 1.00x slower                                                   |
| regex_compile  | 72.8 ms                                                | 73.9 ms: 1.01x slower                                                  |
| regex_effbot   | 2.43 ms                                                | 2.49 ms: 1.02x slower                                                  |
| regex_v8       | 15.1 ms                                                | 16.9 ms: 1.11x slower                                                  |
| Geometric mean | (ref)                                                  | 1.04x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20240104-darwin-arm64-python-1ae7ceba29771baf8f2e-3.13.0a2+-1ae7ceb |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps           | 7.53 ms                                                | 6.60 ms: 1.14x faster                                                  |
| pickle_pure_python   | 191 us                                                 | 198 us: 1.04x slower                                                   |
| pickle_dict          | 17.1 us                                                | 17.9 us: 1.05x slower                                                  |
| unpickle_pure_python | 149 us                                                 | 157 us: 1.06x slower                                                   |
| xml_etree_parse      | 100 ms                                                 | 107 ms: 1.06x slower                                                   |
| pickle_list          | 2.70 us                                                | 2.88 us: 1.07x slower                                                  |
| pickle               | 6.98 us                                                | 7.49 us: 1.07x slower                                                  |
| xml_etree_iterparse  | 68.3 ms                                                | 76.1 ms: 1.11x slower                                                  |
| json_loads           | 15.3 us                                                | 17.3 us: 1.12x slower                                                  |
| unpickle             | 8.29 us                                                | 9.33 us: 1.13x slower                                                  |
| unpickle_list        | 2.69 us                                                | 3.15 us: 1.17x slower                                                  |
| xml_etree_process    | 33.6 ms                                                | 40.0 ms: 1.19x slower                                                  |
| xml_etree_generate   | 45.8 ms                                                | 56.7 ms: 1.24x slower                                                  |
| tomli_loads          | 1.27 sec                                               | 1.58 sec: 1.24x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.10x slower                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20240104-darwin-arm64-python-1ae7ceba29771baf8f2e-3.13.0a2+-1ae7ceb |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                | 13.4 ms: 1.24x slower                                                  |
| python_startup_no_site | 8.57 ms                                                | 12.0 ms: 1.40x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.32x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20240104-darwin-arm64-python-1ae7ceba29771baf8f2e-3.13.0a2+-1ae7ceb |
|-----------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako      | 7.93 ms                                                | 7.61 ms: 1.04x faster                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20240104-darwin-arm64-python-1ae7ceba29771baf8f2e-3.13.0a2+-1ae7ceb |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols   | 301 us                                                 | 73.6 us: 4.09x faster                                                  |
| asyncio_tcp                | 643 ms                                                 | 428 ms: 1.50x faster                                                   |
| unpack_sequence            | 33.6 ns                                                | 26.6 ns: 1.26x faster                                                  |
| generators                 | 30.3 ms                                                | 24.8 ms: 1.22x faster                                                  |
| chaos                      | 47.4 ms                                                | 40.0 ms: 1.18x faster                                                  |
| raytrace                   | 206 ms                                                 | 174 ms: 1.18x faster                                                   |
| comprehensions             | 14.4 us                                                | 12.2 us: 1.18x faster                                                  |
| json_dumps                 | 7.53 ms                                                | 6.60 ms: 1.14x faster                                                  |
| async_tree_none            | 282 ms                                                 | 250 ms: 1.13x faster                                                   |
| deltablue                  | 2.75 ms                                                | 2.47 ms: 1.11x faster                                                  |
| asyncio_tcp_ssl            | 1.40 sec                                               | 1.27 sec: 1.10x faster                                                 |
| async_tree_memoization_tg  | 352 ms                                                 | 322 ms: 1.10x faster                                                   |
| sqlglot_parse              | 890 us                                                 | 818 us: 1.09x faster                                                   |
| async_tree_io_tg           | 724 ms                                                 | 672 ms: 1.08x faster                                                   |
| sympy_sum                  | 80.2 ms                                                | 75.1 ms: 1.07x faster                                                  |
| async_tree_none_tg         | 276 ms                                                 | 259 ms: 1.07x faster                                                   |
| sqlglot_transpile          | 1.05 ms                                                | 1000 us: 1.05x faster                                                  |
| mako                       | 7.93 ms                                                | 7.61 ms: 1.04x faster                                                  |
| deepcopy_memo              | 25.7 us                                                | 24.9 us: 1.03x faster                                                  |
| async_tree_cpu_io_mixed_tg | 550 ms                                                 | 533 ms: 1.03x faster                                                   |
| async_tree_memoization     | 336 ms                                                 | 328 ms: 1.03x faster                                                   |
| sympy_integrate            | 11.3 ms                                                | 11.0 ms: 1.02x faster                                                  |
| hexiom                     | 4.58 ms                                                | 4.49 ms: 1.02x faster                                                  |
| create_gc_cycles           | 711 us                                                 | 702 us: 1.01x faster                                                   |
| go                         | 105 ms                                                 | 104 ms: 1.01x faster                                                   |
| regex_dna                  | 148 ms                                                 | 148 ms: 1.00x slower                                                   |
| asyncio_websockets         | 408 ms                                                 | 409 ms: 1.00x slower                                                   |
| richards_super             | 37.3 ms                                                | 37.5 ms: 1.01x slower                                                  |
| async_tree_cpu_io_mixed    | 519 ms                                                 | 522 ms: 1.01x slower                                                   |
| gc_traversal               | 2.38 ms                                                | 2.40 ms: 1.01x slower                                                  |
| pidigits                   | 280 ms                                                 | 283 ms: 1.01x slower                                                   |
| sympy_str                  | 144 ms                                                 | 145 ms: 1.01x slower                                                   |
| regex_compile              | 72.8 ms                                                | 73.9 ms: 1.01x slower                                                  |
| crypto_pyaes               | 47.5 ms                                                | 48.2 ms: 1.02x slower                                                  |
| async_tree_io              | 697 ms                                                 | 709 ms: 1.02x slower                                                   |
| regex_effbot               | 2.43 ms                                                | 2.49 ms: 1.02x slower                                                  |
| dask                       | 219 ms                                                 | 227 ms: 1.03x slower                                                   |
| dulwich_log                | 28.6 ms                                                | 29.6 ms: 1.03x slower                                                  |
| pickle_pure_python         | 191 us                                                 | 198 us: 1.04x slower                                                   |
| logging_simple             | 3.41 us                                                | 3.53 us: 1.04x slower                                                  |
| coroutines                 | 17.2 ms                                                | 17.8 ms: 1.04x slower                                                  |
| meteor_contest             | 71.1 ms                                                | 74.0 ms: 1.04x slower                                                  |
| docutils                   | 1.43 sec                                               | 1.49 sec: 1.04x slower                                                 |
| logging_format             | 3.67 us                                                | 3.84 us: 1.05x slower                                                  |
| pickle_dict                | 17.1 us                                                | 17.9 us: 1.05x slower                                                  |
| unpickle_pure_python       | 149 us                                                 | 157 us: 1.06x slower                                                   |
| deepcopy                   | 215 us                                                 | 229 us: 1.06x slower                                                   |
| pathlib                    | 23.2 ms                                                | 24.6 ms: 1.06x slower                                                  |
| pycparser                  | 659 ms                                                 | 702 ms: 1.06x slower                                                   |
| xml_etree_parse            | 100 ms                                                 | 107 ms: 1.06x slower                                                   |
| pickle_list                | 2.70 us                                                | 2.88 us: 1.07x slower                                                  |
| logging_silent             | 66.5 ns                                                | 71.1 ns: 1.07x slower                                                  |
| pickle                     | 6.98 us                                                | 7.49 us: 1.07x slower                                                  |
| nqueens                    | 55.9 ms                                                | 61.0 ms: 1.09x slower                                                  |
| richards                   | 31.1 ms                                                | 34.0 ms: 1.09x slower                                                  |
| pprint_pformat             | 979 ms                                                 | 1.07 sec: 1.09x slower                                                 |
| sympy_expand               | 229 ms                                                 | 251 ms: 1.10x slower                                                   |
| scimark_monte_carlo        | 43.5 ms                                                | 47.7 ms: 1.10x slower                                                  |
| mdp                        | 1.48 sec                                               | 1.63 sec: 1.10x slower                                                 |
| json                       | 2.75 ms                                                | 3.03 ms: 1.10x slower                                                  |
| bench_thread_pool          | 465 us                                                 | 514 us: 1.10x slower                                                   |
| pprint_safe_repr           | 478 ms                                                 | 529 ms: 1.11x slower                                                   |
| bench_mp_pool              | 41.0 ms                                                | 45.6 ms: 1.11x slower                                                  |
| scimark_sparse_mat_mult    | 2.81 ms                                                | 3.14 ms: 1.11x slower                                                  |
| xml_etree_iterparse        | 68.3 ms                                                | 76.1 ms: 1.11x slower                                                  |
| regex_v8                   | 15.1 ms                                                | 16.9 ms: 1.11x slower                                                  |
| chameleon                  | 4.30 ms                                                | 4.81 ms: 1.12x slower                                                  |
| scimark_lu                 | 67.7 ms                                                | 75.9 ms: 1.12x slower                                                  |
| 2to3                       | 154 ms                                                 | 173 ms: 1.12x slower                                                   |
| json_loads                 | 15.3 us                                                | 17.3 us: 1.12x slower                                                  |
| coverage                   | 43.9 ms                                                | 49.3 ms: 1.12x slower                                                  |
| unpickle                   | 8.29 us                                                | 9.33 us: 1.13x slower                                                  |
| spectral_norm              | 65.7 ms                                                | 74.0 ms: 1.13x slower                                                  |
| float                      | 50.8 ms                                                | 57.9 ms: 1.14x slower                                                  |
| deepcopy_reduce            | 1.79 us                                                | 2.06 us: 1.15x slower                                                  |
| sqlglot_normalize          | 162 ms                                                 | 187 ms: 1.15x slower                                                   |
| unpickle_list              | 2.69 us                                                | 3.15 us: 1.17x slower                                                  |
| sqlglot_optimize           | 29.6 ms                                                | 34.9 ms: 1.18x slower                                                  |
| scimark_fft                | 173 ms                                                 | 205 ms: 1.19x slower                                                   |
| xml_etree_process          | 33.6 ms                                                | 40.0 ms: 1.19x slower                                                  |
| pyflate                    | 284 ms                                                 | 343 ms: 1.21x slower                                                   |
| fannkuch                   | 240 ms                                                 | 295 ms: 1.23x slower                                                   |
| xml_etree_generate         | 45.8 ms                                                | 56.7 ms: 1.24x slower                                                  |
| tomli_loads                | 1.27 sec                                               | 1.58 sec: 1.24x slower                                                 |
| python_startup             | 10.8 ms                                                | 13.4 ms: 1.24x slower                                                  |
| nbody                      | 61.7 ms                                                | 79.0 ms: 1.28x slower                                                  |
| sqlite_synth               | 1.26 us                                                | 1.66 us: 1.32x slower                                                  |
| scimark_sor                | 79.2 ms                                                | 107 ms: 1.35x slower                                                   |
| python_startup_no_site     | 8.57 ms                                                | 12.0 ms: 1.40x slower                                                  |
| mypy2                      | 372 ms                                                 | 521 ms: 1.40x slower                                                   |
| telco                      | 3.17 ms                                                | 4.74 ms: 1.50x slower                                                  |
| async_generators           | 192 ms                                                 | 302 ms: 1.57x slower                                                   |
| Geometric mean             | (ref)                                                  | 1.04x slower                                                           |

Benchmark hidden because not significant (1): tornado_http
Ignored benchmarks (11) of results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, thrift


# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x


# Memory

- memory change: 1.02x