# Results vs. 3.13.0

- fork: python
- ref: v3.13.0a4
- machine: linux-x86_64
- commit hash: 9d34f60
- commit date: 2024-02-15
- overall geometric mean: 1.05x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 276 ms: 1.04x slower                                       |
| chameleon      | 6.85 ms                                                | 6.75 ms: 1.01x faster                                      |
| docutils       | 2.58 sec                                               | 2.64 sec: 1.02x slower                                     |
| tornado_http   | 91.5 ms                                                | 96.9 ms: 1.06x slower                                      |
| Geometric mean | (ref)                                                  | 1.03x slower                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| asyncio_websockets         | 555 ms                                                 | 552 ms: 1.01x faster                                       |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.01x slower                                     |
| asyncio_tcp                | 488 ms                                                 | 497 ms: 1.02x slower                                       |
| coroutines                 | 22.5 ms                                                | 23.7 ms: 1.05x slower                                      |
| async_generators           | 433 ms                                                 | 463 ms: 1.07x slower                                       |
| async_tree_none            | 354 ms                                                 | 439 ms: 1.24x slower                                       |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 716 ms: 1.25x slower                                       |
| async_tree_memoization_tg  | 465 ms                                                 | 592 ms: 1.27x slower                                       |
| async_tree_memoization     | 442 ms                                                 | 568 ms: 1.28x slower                                       |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 727 ms: 1.34x slower                                       |
| async_tree_io              | 843 ms                                                 | 1.18 sec: 1.40x slower                                     |
| async_tree_none_tg         | 320 ms                                                 | 452 ms: 1.41x slower                                       |
| async_tree_io_tg           | 825 ms                                                 | 1.20 sec: 1.45x slower                                     |
| Geometric mean             | (ref)                                                  | 1.20x slower                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pidigits       | 186 ms                                                 | 188 ms: 1.01x slower                                       |
| float          | 78.5 ms                                                | 86.1 ms: 1.10x slower                                      |
| nbody          | 85.7 ms                                                | 102 ms: 1.19x slower                                       |
| Geometric mean | (ref)                                                  | 1.10x slower                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.57 ms: 1.09x faster                                      |
| regex_v8       | 25.3 ms                                                | 25.1 ms: 1.01x faster                                      |
| regex_dna      | 220 ms                                                 | 225 ms: 1.02x slower                                       |
| regex_compile  | 131 ms                                                 | 141 ms: 1.07x slower                                       |
| Geometric mean | (ref)                                                  | 1.00x slower                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| xml_etree_process    | 60.4 ms                                                | 57.9 ms: 1.04x faster                                      |
| pickle               | 11.6 us                                                | 11.4 us: 1.02x faster                                      |
| xml_etree_generate   | 87.0 ms                                                | 85.7 ms: 1.02x faster                                      |
| pickle_pure_python   | 300 us                                                 | 296 us: 1.01x faster                                       |
| xml_etree_parse      | 156 ms                                                 | 157 ms: 1.01x slower                                       |
| json_loads           | 27.0 us                                                | 27.3 us: 1.01x slower                                      |
| unpickle             | 14.9 us                                                | 15.1 us: 1.01x slower                                      |
| json_dumps           | 10.4 ms                                                | 10.5 ms: 1.01x slower                                      |
| pickle_dict          | 33.2 us                                                | 33.6 us: 1.01x slower                                      |
| pickle_list          | 5.01 us                                                | 5.07 us: 1.01x slower                                      |
| unpickle_list        | 4.96 us                                                | 5.11 us: 1.03x slower                                      |
| tomli_loads          | 2.11 sec                                               | 2.19 sec: 1.04x slower                                     |
| xml_etree_iterparse  | 102 ms                                                 | 108 ms: 1.06x slower                                       |
| unpickle_pure_python | 213 us                                                 | 228 us: 1.07x slower                                       |
| Geometric mean       | (ref)                                                  | 1.01x slower                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.3 ms: 1.03x faster                                      |
| python_startup_no_site | 6.99 ms                                                | 8.95 ms: 1.28x slower                                      |
| Geometric mean         | (ref)                                                  | 1.12x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|-----------|:------------------------------------------------------:|:----------------------------------------------------------:|
| mako      | 11.1 ms                                                | 12.4 ms: 1.12x slower                                      |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-linux-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| typing_runtime_protocols   | 159 us                                                 | 110 us: 1.45x faster                                       |
| mypy2                      | 1.07 sec                                               | 861 ms: 1.24x faster                                       |
| regex_effbot               | 3.88 ms                                                | 3.57 ms: 1.09x faster                                      |
| create_gc_cycles           | 1.61 ms                                                | 1.49 ms: 1.08x faster                                      |
| richards                   | 48.1 ms                                                | 44.8 ms: 1.07x faster                                      |
| richards_super             | 54.4 ms                                                | 50.8 ms: 1.07x faster                                      |
| xml_etree_process          | 60.4 ms                                                | 57.9 ms: 1.04x faster                                      |
| deepcopy_reduce            | 3.17 us                                                | 3.04 us: 1.04x faster                                      |
| python_startup             | 10.6 ms                                                | 10.3 ms: 1.03x faster                                      |
| scimark_lu                 | 115 ms                                                 | 112 ms: 1.02x faster                                       |
| deepcopy                   | 352 us                                                 | 345 us: 1.02x faster                                       |
| pickle                     | 11.6 us                                                | 11.4 us: 1.02x faster                                      |
| xml_etree_generate         | 87.0 ms                                                | 85.7 ms: 1.02x faster                                      |
| pickle_pure_python         | 300 us                                                 | 296 us: 1.01x faster                                       |
| json                       | 5.20 ms                                                | 5.12 ms: 1.01x faster                                      |
| chameleon                  | 6.85 ms                                                | 6.75 ms: 1.01x faster                                      |
| gc_traversal               | 3.81 ms                                                | 3.76 ms: 1.01x faster                                      |
| sqlite_synth               | 2.85 us                                                | 2.82 us: 1.01x faster                                      |
| scimark_fft                | 369 ms                                                 | 366 ms: 1.01x faster                                       |
| scimark_sor                | 122 ms                                                 | 122 ms: 1.01x faster                                       |
| regex_v8                   | 25.3 ms                                                | 25.1 ms: 1.01x faster                                      |
| asyncio_websockets         | 555 ms                                                 | 552 ms: 1.01x faster                                       |
| sqlglot_normalize          | 107 ms                                                 | 107 ms: 1.00x faster                                       |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.80 sec: 1.01x slower                                     |
| logging_format             | 6.25 us                                                | 6.30 us: 1.01x slower                                      |
| xml_etree_parse            | 156 ms                                                 | 157 ms: 1.01x slower                                       |
| generators                 | 28.8 ms                                                | 29.1 ms: 1.01x slower                                      |
| json_loads                 | 27.0 us                                                | 27.3 us: 1.01x slower                                      |
| sqlglot_parse              | 1.27 ms                                                | 1.28 ms: 1.01x slower                                      |
| pidigits                   | 186 ms                                                 | 188 ms: 1.01x slower                                       |
| unpickle                   | 14.9 us                                                | 15.1 us: 1.01x slower                                      |
| json_dumps                 | 10.4 ms                                                | 10.5 ms: 1.01x slower                                      |
| pickle_dict                | 33.2 us                                                | 33.6 us: 1.01x slower                                      |
| logging_simple             | 5.66 us                                                | 5.74 us: 1.01x slower                                      |
| pickle_list                | 5.01 us                                                | 5.07 us: 1.01x slower                                      |
| mdp                        | 2.74 sec                                               | 2.78 sec: 1.01x slower                                     |
| asyncio_tcp                | 488 ms                                                 | 497 ms: 1.02x slower                                       |
| pycparser                  | 1.19 sec                                               | 1.22 sec: 1.02x slower                                     |
| docutils                   | 2.58 sec                                               | 2.64 sec: 1.02x slower                                     |
| sqlglot_optimize           | 53.9 ms                                                | 55.1 ms: 1.02x slower                                      |
| meteor_contest             | 108 ms                                                 | 110 ms: 1.02x slower                                       |
| sympy_integrate            | 19.9 ms                                                | 20.3 ms: 1.02x slower                                      |
| sqlglot_transpile          | 1.57 ms                                                | 1.61 ms: 1.02x slower                                      |
| regex_dna                  | 220 ms                                                 | 225 ms: 1.02x slower                                       |
| bench_thread_pool          | 815 us                                                 | 836 us: 1.03x slower                                       |
| sympy_str                  | 274 ms                                                 | 281 ms: 1.03x slower                                       |
| unpickle_list              | 4.96 us                                                | 5.11 us: 1.03x slower                                      |
| go                         | 142 ms                                                 | 146 ms: 1.03x slower                                       |
| tomli_loads                | 2.11 sec                                               | 2.19 sec: 1.04x slower                                     |
| sympy_expand               | 462 ms                                                 | 480 ms: 1.04x slower                                       |
| pprint_safe_repr           | 744 ms                                                 | 775 ms: 1.04x slower                                       |
| 2to3                       | 265 ms                                                 | 276 ms: 1.04x slower                                       |
| sympy_sum                  | 150 ms                                                 | 157 ms: 1.05x slower                                       |
| coroutines                 | 22.5 ms                                                | 23.7 ms: 1.05x slower                                      |
| deltablue                  | 3.15 ms                                                | 3.32 ms: 1.05x slower                                      |
| xml_etree_iterparse        | 102 ms                                                 | 108 ms: 1.06x slower                                       |
| unpack_sequence            | 42.4 ns                                                | 44.9 ns: 1.06x slower                                      |
| tornado_http               | 91.5 ms                                                | 96.9 ms: 1.06x slower                                      |
| pathlib                    | 17.1 ms                                                | 18.1 ms: 1.06x slower                                      |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 5.35 ms: 1.06x slower                                      |
| unpickle_pure_python       | 213 us                                                 | 228 us: 1.07x slower                                       |
| pprint_pformat             | 1.51 sec                                               | 1.61 sec: 1.07x slower                                     |
| raytrace                   | 262 ms                                                 | 280 ms: 1.07x slower                                       |
| async_generators           | 433 ms                                                 | 463 ms: 1.07x slower                                       |
| regex_compile              | 131 ms                                                 | 141 ms: 1.07x slower                                       |
| dulwich_log                | 63.0 ms                                                | 68.2 ms: 1.08x slower                                      |
| crypto_pyaes               | 73.0 ms                                                | 79.1 ms: 1.08x slower                                      |
| float                      | 78.5 ms                                                | 86.1 ms: 1.10x slower                                      |
| comprehensions             | 16.4 us                                                | 18.2 us: 1.11x slower                                      |
| fannkuch                   | 381 ms                                                 | 422 ms: 1.11x slower                                       |
| nqueens                    | 80.6 ms                                                | 89.8 ms: 1.11x slower                                      |
| mako                       | 11.1 ms                                                | 12.4 ms: 1.12x slower                                      |
| scimark_monte_carlo        | 66.3 ms                                                | 74.0 ms: 1.12x slower                                      |
| pyflate                    | 460 ms                                                 | 514 ms: 1.12x slower                                       |
| spectral_norm              | 115 ms                                                 | 132 ms: 1.14x slower                                       |
| coverage                   | 83.7 ms                                                | 95.8 ms: 1.14x slower                                      |
| chaos                      | 58.4 ms                                                | 69.1 ms: 1.18x slower                                      |
| nbody                      | 85.7 ms                                                | 102 ms: 1.19x slower                                       |
| async_tree_none            | 354 ms                                                 | 439 ms: 1.24x slower                                       |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 716 ms: 1.25x slower                                       |
| hexiom                     | 6.13 ms                                                | 7.72 ms: 1.26x slower                                      |
| async_tree_memoization_tg  | 465 ms                                                 | 592 ms: 1.27x slower                                       |
| python_startup_no_site     | 6.99 ms                                                | 8.95 ms: 1.28x slower                                      |
| async_tree_memoization     | 442 ms                                                 | 568 ms: 1.28x slower                                       |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 727 ms: 1.34x slower                                       |
| async_tree_io              | 843 ms                                                 | 1.18 sec: 1.40x slower                                     |
| async_tree_none_tg         | 320 ms                                                 | 452 ms: 1.41x slower                                       |
| async_tree_io_tg           | 825 ms                                                 | 1.20 sec: 1.45x slower                                     |
| dask                       | 338 ms                                                 | 527 ms: 1.56x slower                                       |
| Geometric mean             | (ref)                                                  | 1.05x slower                                               |

Benchmark hidden because not significant (4): logging_silent, telco, bench_mp_pool, deepcopy_memo
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, bpe_tokeniser, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: 0.99x