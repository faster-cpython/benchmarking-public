# Results vs. 3.12.0

- fork: gvanrossum
- ref: backoff_counter_woes
- machine: darwin-arm64
- commit hash: 4c1049b
- commit date: 2024-05-04
- overall geometric mean: 1.07x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240504-darwin-arm64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 169 ms                                                 | 159 ms: 1.07x faster                                                       |
| chameleon      | 4.70 ms                                                | 4.38 ms: 1.07x faster                                                      |
| docutils       | 1.50 sec                                               | 1.46 sec: 1.03x faster                                                     |
| Geometric mean | (ref)                                                  | 1.03x faster                                                               |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240504-darwin-arm64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 323 ms                                                 | 240 ms: 1.34x faster                                                       |
| async_tree_none_tg         | 258 ms                                                 | 195 ms: 1.32x faster                                                       |
| async_tree_none            | 266 ms                                                 | 210 ms: 1.26x faster                                                       |
| async_tree_memoization     | 312 ms                                                 | 255 ms: 1.22x faster                                                       |
| async_tree_io              | 668 ms                                                 | 561 ms: 1.19x faster                                                       |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 454 ms: 1.17x faster                                                       |
| async_tree_io_tg           | 669 ms                                                 | 573 ms: 1.17x faster                                                       |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 465 ms: 1.13x faster                                                       |
| Geometric mean             | (ref)                                                  | 1.22x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240504-darwin-arm64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 68.8 ms                                                | 59.3 ms: 1.16x faster                                                      |
| float          | 55.8 ms                                                | 48.6 ms: 1.15x faster                                                      |
| Geometric mean | (ref)                                                  | 1.10x faster                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240504-darwin-arm64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 77.9 ms                                                | 68.7 ms: 1.13x faster                                                      |
| regex_dna      | 154 ms                                                 | 139 ms: 1.11x faster                                                       |
| regex_effbot   | 2.64 ms                                                | 2.56 ms: 1.03x faster                                                      |
| regex_v8       | 16.0 ms                                                | 16.6 ms: 1.04x slower                                                      |
| Geometric mean | (ref)                                                  | 1.06x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240504-darwin-arm64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle_pure_python   | 200 us                                                 | 181 us: 1.10x faster                                                       |
| xml_etree_iterparse  | 74.0 ms                                                | 67.7 ms: 1.09x faster                                                      |
| xml_etree_parse      | 106 ms                                                 | 98.1 ms: 1.08x faster                                                      |
| xml_etree_process    | 39.7 ms                                                | 37.0 ms: 1.07x faster                                                      |
| unpickle_pure_python | 151 us                                                 | 142 us: 1.06x faster                                                       |
| xml_etree_generate   | 55.8 ms                                                | 53.1 ms: 1.05x faster                                                      |
| json_dumps           | 6.22 ms                                                | 6.14 ms: 1.01x faster                                                      |
| pickle_dict          | 18.1 us                                                | 18.3 us: 1.01x slower                                                      |
| pickle               | 7.23 us                                                | 7.44 us: 1.03x slower                                                      |
| pickle_list          | 2.89 us                                                | 2.99 us: 1.04x slower                                                      |
| tomli_loads          | 1.39 sec                                               | 1.45 sec: 1.04x slower                                                     |
| unpickle             | 9.12 us                                                | 9.67 us: 1.06x slower                                                      |
| unpickle_list        | 3.02 us                                                | 3.26 us: 1.08x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                               |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240504-darwin-arm64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 9.37 ms                                                | 10.9 ms: 1.17x slower                                                      |
| python_startup         | 11.4 ms                                                | 13.7 ms: 1.20x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.18x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240504-darwin-arm64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| django_template | 22.3 ms                                                | 19.4 ms: 1.15x faster                                                      |
| mako            | 7.71 ms                                                | 6.89 ms: 1.12x faster                                                      |
| Geometric mean  | (ref)                                                  | 1.13x faster                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240504-darwin-arm64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| raytrace                   | 212 ms                                                 | 148 ms: 1.43x faster                                                       |
| generators                 | 31.1 ms                                                | 22.6 ms: 1.37x faster                                                      |
| comprehensions             | 14.5 us                                                | 10.6 us: 1.37x faster                                                      |
| async_tree_memoization_tg  | 323 ms                                                 | 240 ms: 1.34x faster                                                       |
| async_tree_none_tg         | 258 ms                                                 | 195 ms: 1.32x faster                                                       |
| logging_silent             | 76.4 ns                                                | 60.5 ns: 1.26x faster                                                      |
| async_tree_none            | 266 ms                                                 | 210 ms: 1.26x faster                                                       |
| deltablue                  | 2.71 ms                                                | 2.15 ms: 1.26x faster                                                      |
| chaos                      | 42.5 ms                                                | 34.7 ms: 1.23x faster                                                      |
| async_tree_memoization     | 312 ms                                                 | 255 ms: 1.22x faster                                                       |
| logging_simple             | 3.69 us                                                | 3.04 us: 1.21x faster                                                      |
| deepcopy_memo              | 27.7 us                                                | 22.9 us: 1.21x faster                                                      |
| logging_format             | 3.98 us                                                | 3.33 us: 1.20x faster                                                      |
| async_tree_io              | 668 ms                                                 | 561 ms: 1.19x faster                                                       |
| nqueens                    | 62.4 ms                                                | 52.8 ms: 1.18x faster                                                      |
| async_tree_cpu_io_mixed_tg | 532 ms                                                 | 454 ms: 1.17x faster                                                       |
| coroutines                 | 19.2 ms                                                | 16.4 ms: 1.17x faster                                                      |
| async_tree_io_tg           | 669 ms                                                 | 573 ms: 1.17x faster                                                       |
| deepcopy_reduce            | 2.07 us                                                | 1.78 us: 1.16x faster                                                      |
| nbody                      | 68.8 ms                                                | 59.3 ms: 1.16x faster                                                      |
| deepcopy                   | 235 us                                                 | 202 us: 1.16x faster                                                       |
| sqlglot_parse              | 848 us                                                 | 737 us: 1.15x faster                                                       |
| django_template            | 22.3 ms                                                | 19.4 ms: 1.15x faster                                                      |
| float                      | 55.8 ms                                                | 48.6 ms: 1.15x faster                                                      |
| spectral_norm              | 76.4 ms                                                | 66.5 ms: 1.15x faster                                                      |
| scimark_sparse_mat_mult    | 3.14 ms                                                | 2.76 ms: 1.14x faster                                                      |
| sqlglot_transpile          | 1.02 ms                                                | 900 us: 1.13x faster                                                       |
| regex_compile              | 77.9 ms                                                | 68.7 ms: 1.13x faster                                                      |
| crypto_pyaes               | 51.9 ms                                                | 45.8 ms: 1.13x faster                                                      |
| async_tree_cpu_io_mixed    | 526 ms                                                 | 465 ms: 1.13x faster                                                       |
| asyncio_tcp                | 449 ms                                                 | 398 ms: 1.13x faster                                                       |
| scimark_lu                 | 76.0 ms                                                | 67.8 ms: 1.12x faster                                                      |
| mako                       | 7.71 ms                                                | 6.89 ms: 1.12x faster                                                      |
| sqlglot_normalize          | 186 ms                                                 | 166 ms: 1.12x faster                                                       |
| sympy_sum                  | 77.6 ms                                                | 69.4 ms: 1.12x faster                                                      |
| sympy_str                  | 148 ms                                                 | 132 ms: 1.12x faster                                                       |
| regex_dna                  | 154 ms                                                 | 139 ms: 1.11x faster                                                       |
| hexiom                     | 4.54 ms                                                | 4.10 ms: 1.11x faster                                                      |
| sympy_integrate            | 11.4 ms                                                | 10.3 ms: 1.11x faster                                                      |
| pickle_pure_python         | 200 us                                                 | 181 us: 1.10x faster                                                       |
| sqlglot_optimize           | 34.0 ms                                                | 31.0 ms: 1.10x faster                                                      |
| xml_etree_iterparse        | 74.0 ms                                                | 67.7 ms: 1.09x faster                                                      |
| bench_thread_pool          | 504 us                                                 | 461 us: 1.09x faster                                                       |
| dulwich_log                | 29.8 ms                                                | 27.3 ms: 1.09x faster                                                      |
| async_generators           | 304 ms                                                 | 279 ms: 1.09x faster                                                       |
| xml_etree_parse            | 106 ms                                                 | 98.1 ms: 1.08x faster                                                      |
| chameleon                  | 4.70 ms                                                | 4.38 ms: 1.07x faster                                                      |
| xml_etree_process          | 39.7 ms                                                | 37.0 ms: 1.07x faster                                                      |
| pycparser                  | 677 ms                                                 | 634 ms: 1.07x faster                                                       |
| 2to3                       | 169 ms                                                 | 159 ms: 1.07x faster                                                       |
| pprint_pformat             | 1.01 sec                                               | 949 ms: 1.07x faster                                                       |
| sympy_expand               | 241 ms                                                 | 227 ms: 1.06x faster                                                       |
| scimark_fft                | 195 ms                                                 | 184 ms: 1.06x faster                                                       |
| unpickle_pure_python       | 151 us                                                 | 142 us: 1.06x faster                                                       |
| scimark_monte_carlo        | 45.0 ms                                                | 42.4 ms: 1.06x faster                                                      |
| pathlib                    | 24.2 ms                                                | 22.8 ms: 1.06x faster                                                      |
| pprint_safe_repr           | 497 ms                                                 | 469 ms: 1.06x faster                                                       |
| mdp                        | 1.58 sec                                               | 1.50 sec: 1.05x faster                                                     |
| xml_etree_generate         | 55.8 ms                                                | 53.1 ms: 1.05x faster                                                      |
| typing_runtime_protocols   | 93.0 us                                                | 88.9 us: 1.05x faster                                                      |
| docutils                   | 1.50 sec                                               | 1.46 sec: 1.03x faster                                                     |
| regex_effbot               | 2.64 ms                                                | 2.56 ms: 1.03x faster                                                      |
| richards_super             | 36.0 ms                                                | 35.3 ms: 1.02x faster                                                      |
| go                         | 102 ms                                                 | 99.7 ms: 1.02x faster                                                      |
| dask                       | 222 ms                                                 | 218 ms: 1.02x faster                                                       |
| json                       | 3.09 ms                                                | 3.03 ms: 1.02x faster                                                      |
| sqlite_synth               | 1.57 us                                                | 1.55 us: 1.02x faster                                                      |
| json_dumps                 | 6.22 ms                                                | 6.14 ms: 1.01x faster                                                      |
| meteor_contest             | 71.7 ms                                                | 71.5 ms: 1.00x faster                                                      |
| asyncio_websockets         | 409 ms                                                 | 408 ms: 1.00x faster                                                       |
| pickle_dict                | 18.1 us                                                | 18.3 us: 1.01x slower                                                      |
| pyflate                    | 316 ms                                                 | 321 ms: 1.02x slower                                                       |
| pickle                     | 7.23 us                                                | 7.44 us: 1.03x slower                                                      |
| pickle_list                | 2.89 us                                                | 2.99 us: 1.04x slower                                                      |
| gc_traversal               | 2.40 ms                                                | 2.49 ms: 1.04x slower                                                      |
| fannkuch                   | 248 ms                                                 | 258 ms: 1.04x slower                                                       |
| regex_v8                   | 16.0 ms                                                | 16.6 ms: 1.04x slower                                                      |
| tomli_loads                | 1.39 sec                                               | 1.45 sec: 1.04x slower                                                     |
| unpickle                   | 9.12 us                                                | 9.67 us: 1.06x slower                                                      |
| asyncio_tcp_ssl            | 1.24 sec                                               | 1.32 sec: 1.06x slower                                                     |
| unpickle_list              | 3.02 us                                                | 3.26 us: 1.08x slower                                                      |
| scimark_sor                | 87.4 ms                                                | 95.1 ms: 1.09x slower                                                      |
| python_startup_no_site     | 9.37 ms                                                | 10.9 ms: 1.17x slower                                                      |
| coverage                   | 38.9 ms                                                | 45.4 ms: 1.17x slower                                                      |
| telco                      | 3.68 ms                                                | 4.40 ms: 1.20x slower                                                      |
| python_startup             | 11.4 ms                                                | 13.7 ms: 1.20x slower                                                      |
| mypy2                      | 380 ms                                                 | 458 ms: 1.21x slower                                                       |
| create_gc_cycles           | 701 us                                                 | 946 us: 1.35x slower                                                       |
| Geometric mean             | (ref)                                                  | 1.07x faster                                                               |

Benchmark hidden because not significant (7): gunicorn, json_loads, pidigits, aiohttp, richards, bench_mp_pool, tornado_http
Ignored benchmarks (3) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (14) of results/bm-20240504-3.13.0a6+-4c1049b/bm-20240504-darwin-arm64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 1.06x