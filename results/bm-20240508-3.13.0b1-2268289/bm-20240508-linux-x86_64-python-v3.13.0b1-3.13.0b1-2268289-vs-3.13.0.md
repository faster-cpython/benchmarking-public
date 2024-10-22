# Results vs. 3.13.0

- fork: python
- ref: v3.13.0b1
- machine: linux-x86_64
- commit hash: 2268289
- commit date: 2024-05-08
- overall geometric mean: 1.06x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240508-linux-x86_64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 272 ms: 1.03x slower                                       |
| chameleon      | 6.85 ms                                                | 7.11 ms: 1.04x slower                                      |
| docutils       | 2.58 sec                                               | 2.86 sec: 1.11x slower                                     |
| html5lib       | 64.5 ms                                                | 68.4 ms: 1.06x slower                                      |
| tornado_http   | 91.5 ms                                                | 95.8 ms: 1.05x slower                                      |
| Geometric mean | (ref)                                                  | 1.06x slower                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240508-linux-x86_64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| asyncio_websockets         | 555 ms                                                 | 564 ms: 1.02x slower                                       |
| async_tree_none            | 354 ms                                                 | 363 ms: 1.03x slower                                       |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.84 sec: 1.03x slower                                     |
| asyncio_tcp                | 488 ms                                                 | 510 ms: 1.04x slower                                       |
| async_generators           | 433 ms                                                 | 452 ms: 1.04x slower                                       |
| async_tree_memoization     | 442 ms                                                 | 477 ms: 1.08x slower                                       |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 619 ms: 1.08x slower                                       |
| async_tree_none_tg         | 320 ms                                                 | 346 ms: 1.08x slower                                       |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 589 ms: 1.08x slower                                       |
| async_tree_io              | 843 ms                                                 | 936 ms: 1.11x slower                                       |
| async_tree_io_tg           | 825 ms                                                 | 987 ms: 1.20x slower                                       |
| Geometric mean             | (ref)                                                  | 1.06x slower                                               |

Benchmark hidden because not significant (2): async_tree_memoization_tg, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240508-linux-x86_64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pidigits       | 186 ms                                                 | 189 ms: 1.02x slower                                       |
| nbody          | 85.7 ms                                                | 87.8 ms: 1.02x slower                                      |
| Geometric mean | (ref)                                                  | 1.01x slower                                               |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240508-linux-x86_64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.67 ms: 1.06x faster                                      |
| regex_dna      | 220 ms                                                 | 226 ms: 1.03x slower                                       |
| regex_compile  | 131 ms                                                 | 135 ms: 1.03x slower                                       |
| regex_v8       | 25.3 ms                                                | 26.2 ms: 1.04x slower                                      |
| Geometric mean | (ref)                                                  | 1.01x slower                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240508-linux-x86_64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| xml_etree_generate   | 87.0 ms                                                | 87.7 ms: 1.01x slower                                      |
| pickle_dict          | 33.2 us                                                | 33.8 us: 1.02x slower                                      |
| xml_etree_parse      | 156 ms                                                 | 159 ms: 1.02x slower                                       |
| pickle               | 11.6 us                                                | 11.8 us: 1.02x slower                                      |
| pickle_pure_python   | 300 us                                                 | 311 us: 1.04x slower                                       |
| unpickle_pure_python | 213 us                                                 | 223 us: 1.04x slower                                       |
| tomli_loads          | 2.11 sec                                               | 2.22 sec: 1.05x slower                                     |
| xml_etree_iterparse  | 102 ms                                                 | 108 ms: 1.06x slower                                       |
| pickle_list          | 5.01 us                                                | 5.30 us: 1.06x slower                                      |
| json_loads           | 27.0 us                                                | 28.9 us: 1.07x slower                                      |
| unpickle_list        | 4.96 us                                                | 5.38 us: 1.08x slower                                      |
| unpickle             | 14.9 us                                                | 17.0 us: 1.14x slower                                      |
| Geometric mean       | (ref)                                                  | 1.04x slower                                               |

Benchmark hidden because not significant (2): xml_etree_process, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240508-linux-x86_64-python-v3.13.0b1-3.13.0b1-2268289 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.7 ms: 1.01x slower                                      |
| python_startup_no_site | 6.99 ms                                                | 7.19 ms: 1.03x slower                                      |
| Geometric mean         | (ref)                                                  | 1.02x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240508-linux-x86_64-python-v3.13.0b1-3.13.0b1-2268289 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| mako            | 11.1 ms                                                | 10.9 ms: 1.02x faster                                      |
| genshi_text     | 22.9 ms                                                | 23.1 ms: 1.01x slower                                      |
| django_template | 34.4 ms                                                | 35.1 ms: 1.02x slower                                      |
| genshi_xml      | 50.3 ms                                                | 52.1 ms: 1.04x slower                                      |
| Geometric mean  | (ref)                                                  | 1.01x slower                                               |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240508-linux-x86_64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| mypy2                      | 1.07 sec                                               | 743 ms: 1.44x faster                                       |
| regex_effbot               | 3.88 ms                                                | 3.67 ms: 1.06x faster                                      |
| mdp                        | 2.74 sec                                               | 2.60 sec: 1.05x faster                                     |
| spectral_norm              | 115 ms                                                 | 113 ms: 1.02x faster                                       |
| mako                       | 11.1 ms                                                | 10.9 ms: 1.02x faster                                      |
| bench_mp_pool              | 24.0 ms                                                | 23.9 ms: 1.00x faster                                      |
| hexiom                     | 6.13 ms                                                | 6.15 ms: 1.00x slower                                      |
| chaos                      | 58.4 ms                                                | 58.8 ms: 1.01x slower                                      |
| xml_etree_generate         | 87.0 ms                                                | 87.7 ms: 1.01x slower                                      |
| nqueens                    | 80.6 ms                                                | 81.4 ms: 1.01x slower                                      |
| genshi_text                | 22.9 ms                                                | 23.1 ms: 1.01x slower                                      |
| scimark_fft                | 369 ms                                                 | 373 ms: 1.01x slower                                       |
| gc_traversal               | 3.81 ms                                                | 3.85 ms: 1.01x slower                                      |
| pycparser                  | 1.19 sec                                               | 1.21 sec: 1.01x slower                                     |
| python_startup             | 10.6 ms                                                | 10.7 ms: 1.01x slower                                      |
| pidigits                   | 186 ms                                                 | 189 ms: 1.02x slower                                       |
| generators                 | 28.8 ms                                                | 29.3 ms: 1.02x slower                                      |
| asyncio_websockets         | 555 ms                                                 | 564 ms: 1.02x slower                                       |
| pickle_dict                | 33.2 us                                                | 33.8 us: 1.02x slower                                      |
| django_template            | 34.4 ms                                                | 35.1 ms: 1.02x slower                                      |
| xml_etree_parse            | 156 ms                                                 | 159 ms: 1.02x slower                                       |
| raytrace                   | 262 ms                                                 | 267 ms: 1.02x slower                                       |
| pickle                     | 11.6 us                                                | 11.8 us: 1.02x slower                                      |
| nbody                      | 85.7 ms                                                | 87.8 ms: 1.02x slower                                      |
| async_tree_none            | 354 ms                                                 | 363 ms: 1.03x slower                                       |
| meteor_contest             | 108 ms                                                 | 110 ms: 1.03x slower                                       |
| regex_dna                  | 220 ms                                                 | 226 ms: 1.03x slower                                       |
| regex_compile              | 131 ms                                                 | 135 ms: 1.03x slower                                       |
| 2to3                       | 265 ms                                                 | 272 ms: 1.03x slower                                       |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.84 sec: 1.03x slower                                     |
| pyflate                    | 460 ms                                                 | 473 ms: 1.03x slower                                       |
| python_startup_no_site     | 6.99 ms                                                | 7.19 ms: 1.03x slower                                      |
| deepcopy_reduce            | 3.17 us                                                | 3.26 us: 1.03x slower                                      |
| bench_thread_pool          | 815 us                                                 | 839 us: 1.03x slower                                       |
| pprint_safe_repr           | 744 ms                                                 | 767 ms: 1.03x slower                                       |
| sympy_integrate            | 19.9 ms                                                | 20.5 ms: 1.03x slower                                      |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 5.18 ms: 1.03x slower                                      |
| fannkuch                   | 381 ms                                                 | 393 ms: 1.03x slower                                       |
| sqlglot_transpile          | 1.57 ms                                                | 1.62 ms: 1.03x slower                                      |
| go                         | 142 ms                                                 | 146 ms: 1.03x slower                                       |
| sympy_expand               | 462 ms                                                 | 477 ms: 1.03x slower                                       |
| comprehensions             | 16.4 us                                                | 17.0 us: 1.03x slower                                      |
| sqlglot_parse              | 1.27 ms                                                | 1.31 ms: 1.03x slower                                      |
| genshi_xml                 | 50.3 ms                                                | 52.1 ms: 1.04x slower                                      |
| sqlglot_optimize           | 53.9 ms                                                | 55.8 ms: 1.04x slower                                      |
| pickle_pure_python         | 300 us                                                 | 311 us: 1.04x slower                                       |
| regex_v8                   | 25.3 ms                                                | 26.2 ms: 1.04x slower                                      |
| deepcopy_memo              | 38.0 us                                                | 39.4 us: 1.04x slower                                      |
| deltablue                  | 3.15 ms                                                | 3.27 ms: 1.04x slower                                      |
| chameleon                  | 6.85 ms                                                | 7.11 ms: 1.04x slower                                      |
| deepcopy                   | 352 us                                                 | 366 us: 1.04x slower                                       |
| sympy_str                  | 274 ms                                                 | 284 ms: 1.04x slower                                       |
| pprint_pformat             | 1.51 sec                                               | 1.57 sec: 1.04x slower                                     |
| sqlite_synth               | 2.85 us                                                | 2.96 us: 1.04x slower                                      |
| logging_silent             | 102 ns                                                 | 106 ns: 1.04x slower                                       |
| json                       | 5.20 ms                                                | 5.41 ms: 1.04x slower                                      |
| scimark_sor                | 122 ms                                                 | 128 ms: 1.04x slower                                       |
| logging_simple             | 5.66 us                                                | 5.91 us: 1.04x slower                                      |
| asyncio_tcp                | 488 ms                                                 | 510 ms: 1.04x slower                                       |
| crypto_pyaes               | 73.0 ms                                                | 76.2 ms: 1.04x slower                                      |
| async_generators           | 433 ms                                                 | 452 ms: 1.04x slower                                       |
| unpickle_pure_python       | 213 us                                                 | 223 us: 1.04x slower                                       |
| aiohttp                    | 1.14 ms                                                | 1.20 ms: 1.05x slower                                      |
| logging_format             | 6.25 us                                                | 6.54 us: 1.05x slower                                      |
| tornado_http               | 91.5 ms                                                | 95.8 ms: 1.05x slower                                      |
| pathlib                    | 17.1 ms                                                | 17.9 ms: 1.05x slower                                      |
| sqlglot_normalize          | 107 ms                                                 | 113 ms: 1.05x slower                                       |
| tomli_loads                | 2.11 sec                                               | 2.22 sec: 1.05x slower                                     |
| richards                   | 48.1 ms                                                | 50.5 ms: 1.05x slower                                      |
| gunicorn                   | 1.23 ms                                                | 1.29 ms: 1.05x slower                                      |
| sympy_sum                  | 150 ms                                                 | 157 ms: 1.05x slower                                       |
| richards_super             | 54.4 ms                                                | 57.4 ms: 1.05x slower                                      |
| scimark_monte_carlo        | 66.3 ms                                                | 69.9 ms: 1.05x slower                                      |
| xml_etree_iterparse        | 102 ms                                                 | 108 ms: 1.06x slower                                       |
| pickle_list                | 5.01 us                                                | 5.30 us: 1.06x slower                                      |
| html5lib                   | 64.5 ms                                                | 68.4 ms: 1.06x slower                                      |
| dulwich_log                | 63.0 ms                                                | 67.0 ms: 1.06x slower                                      |
| typing_runtime_protocols   | 159 us                                                 | 170 us: 1.06x slower                                       |
| json_loads                 | 27.0 us                                                | 28.9 us: 1.07x slower                                      |
| async_tree_memoization     | 442 ms                                                 | 477 ms: 1.08x slower                                       |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 619 ms: 1.08x slower                                       |
| async_tree_none_tg         | 320 ms                                                 | 346 ms: 1.08x slower                                       |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 589 ms: 1.08x slower                                       |
| unpickle_list              | 4.96 us                                                | 5.38 us: 1.08x slower                                      |
| dask                       | 338 ms                                                 | 372 ms: 1.10x slower                                       |
| coverage                   | 83.7 ms                                                | 92.4 ms: 1.10x slower                                      |
| docutils                   | 2.58 sec                                               | 2.86 sec: 1.11x slower                                     |
| async_tree_io              | 843 ms                                                 | 936 ms: 1.11x slower                                       |
| create_gc_cycles           | 1.61 ms                                                | 1.80 ms: 1.12x slower                                      |
| unpickle                   | 14.9 us                                                | 17.0 us: 1.14x slower                                      |
| async_tree_io_tg           | 825 ms                                                 | 987 ms: 1.20x slower                                       |
| telco                      | 8.45 ms                                                | 173 ms: 20.41x slower                                      |
| Geometric mean             | (ref)                                                  | 1.06x slower                                               |

Benchmark hidden because not significant (10): async_tree_memoization_tg, djangocms, flaskblogging, xml_etree_process, float, coroutines, scimark_lu, json_dumps, thrift, pylint
Ignored benchmarks (2) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: bpe_tokeniser, unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.00x