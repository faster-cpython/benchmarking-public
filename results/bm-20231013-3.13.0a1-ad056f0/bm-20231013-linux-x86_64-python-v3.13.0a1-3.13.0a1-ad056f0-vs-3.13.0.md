# Results vs. 3.13.0

- fork: python
- ref: v3.13.0a1
- machine: linux-x86_64
- commit hash: ad056f0
- commit date: 2023-10-13
- overall geometric mean: 1.04x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: 0.95x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 269 ms: 1.02x slower                                       |
| chameleon      | 6.85 ms                                                | 7.07 ms: 1.03x slower                                      |
| docutils       | 2.58 sec                                               | 2.64 sec: 1.02x slower                                     |
| tornado_http   | 91.5 ms                                                | 96.0 ms: 1.05x slower                                      |
| Geometric mean | (ref)                                                  | 1.03x slower                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| asyncio_tcp                | 488 ms                                                 | 484 ms: 1.01x faster                                       |
| asyncio_websockets         | 555 ms                                                 | 552 ms: 1.01x faster                                       |
| coroutines                 | 22.5 ms                                                | 23.4 ms: 1.04x slower                                      |
| async_generators           | 433 ms                                                 | 453 ms: 1.05x slower                                       |
| async_tree_none            | 354 ms                                                 | 437 ms: 1.23x slower                                       |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 712 ms: 1.24x slower                                       |
| async_tree_memoization     | 442 ms                                                 | 564 ms: 1.27x slower                                       |
| async_tree_memoization_tg  | 465 ms                                                 | 595 ms: 1.28x slower                                       |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 741 ms: 1.36x slower                                       |
| async_tree_io              | 843 ms                                                 | 1.19 sec: 1.41x slower                                     |
| async_tree_none_tg         | 320 ms                                                 | 453 ms: 1.42x slower                                       |
| async_tree_io_tg           | 825 ms                                                 | 1.23 sec: 1.49x slower                                     |
| Geometric mean             | (ref)                                                  | 1.20x slower                                               |

Benchmark hidden because not significant (1): asyncio_tcp_ssl

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| nbody          | 85.7 ms                                                | 88.6 ms: 1.03x slower                                      |
| float          | 78.5 ms                                                | 81.6 ms: 1.04x slower                                      |
| pidigits       | 186 ms                                                 | 195 ms: 1.05x slower                                       |
| Geometric mean | (ref)                                                  | 1.04x slower                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.67 ms: 1.06x faster                                      |
| regex_dna      | 220 ms                                                 | 212 ms: 1.04x faster                                       |
| regex_v8       | 25.3 ms                                                | 24.7 ms: 1.02x faster                                      |
| regex_compile  | 131 ms                                                 | 138 ms: 1.06x slower                                       |
| Geometric mean | (ref)                                                  | 1.01x faster                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| xml_etree_process    | 60.4 ms                                                | 59.9 ms: 1.01x faster                                      |
| pickle               | 11.6 us                                                | 11.6 us: 1.01x slower                                      |
| json_dumps           | 10.4 ms                                                | 10.5 ms: 1.01x slower                                      |
| xml_etree_parse      | 156 ms                                                 | 157 ms: 1.01x slower                                       |
| unpickle_list        | 4.96 us                                                | 5.05 us: 1.02x slower                                      |
| tomli_loads          | 2.11 sec                                               | 2.15 sec: 1.02x slower                                     |
| pickle_list          | 5.01 us                                                | 5.10 us: 1.02x slower                                      |
| json_loads           | 27.0 us                                                | 27.8 us: 1.03x slower                                      |
| xml_etree_iterparse  | 102 ms                                                 | 106 ms: 1.03x slower                                       |
| unpickle_pure_python | 213 us                                                 | 222 us: 1.04x slower                                       |
| pickle_dict          | 33.2 us                                                | 34.6 us: 1.04x slower                                      |
| Geometric mean       | (ref)                                                  | 1.02x slower                                               |

Benchmark hidden because not significant (3): pickle_pure_python, xml_etree_generate, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.1 ms: 1.05x faster                                      |
| python_startup_no_site | 6.99 ms                                                | 6.87 ms: 1.02x faster                                      |
| Geometric mean         | (ref)                                                  | 1.03x faster                                               |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|-----------|:------------------------------------------------------:|:----------------------------------------------------------:|
| mako      | 11.1 ms                                                | 11.2 ms: 1.01x slower                                      |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| create_gc_cycles           | 1.61 ms                                                | 1.48 ms: 1.09x faster                                      |
| regex_effbot               | 3.88 ms                                                | 3.67 ms: 1.06x faster                                      |
| python_startup             | 10.6 ms                                                | 10.1 ms: 1.05x faster                                      |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.79 ms: 1.05x faster                                      |
| spectral_norm              | 115 ms                                                 | 110 ms: 1.05x faster                                       |
| regex_dna                  | 220 ms                                                 | 212 ms: 1.04x faster                                       |
| telco                      | 8.45 ms                                                | 8.17 ms: 1.03x faster                                      |
| typing_runtime_protocols   | 159 us                                                 | 156 us: 1.02x faster                                       |
| sympy_expand               | 462 ms                                                 | 452 ms: 1.02x faster                                       |
| regex_v8                   | 25.3 ms                                                | 24.7 ms: 1.02x faster                                      |
| sqlite_synth               | 2.85 us                                                | 2.80 us: 1.02x faster                                      |
| python_startup_no_site     | 6.99 ms                                                | 6.87 ms: 1.02x faster                                      |
| crypto_pyaes               | 73.0 ms                                                | 71.8 ms: 1.02x faster                                      |
| asyncio_tcp                | 488 ms                                                 | 484 ms: 1.01x faster                                       |
| deepcopy_reduce            | 3.17 us                                                | 3.14 us: 1.01x faster                                      |
| xml_etree_process          | 60.4 ms                                                | 59.9 ms: 1.01x faster                                      |
| sqlglot_normalize          | 107 ms                                                 | 107 ms: 1.01x faster                                       |
| asyncio_websockets         | 555 ms                                                 | 552 ms: 1.01x faster                                       |
| pickle                     | 11.6 us                                                | 11.6 us: 1.01x slower                                      |
| hexiom                     | 6.13 ms                                                | 6.16 ms: 1.01x slower                                      |
| json_dumps                 | 10.4 ms                                                | 10.5 ms: 1.01x slower                                      |
| pycparser                  | 1.19 sec                                               | 1.20 sec: 1.01x slower                                     |
| richards                   | 48.1 ms                                                | 48.6 ms: 1.01x slower                                      |
| xml_etree_parse            | 156 ms                                                 | 157 ms: 1.01x slower                                       |
| pprint_safe_repr           | 744 ms                                                 | 752 ms: 1.01x slower                                       |
| richards_super             | 54.4 ms                                                | 55.0 ms: 1.01x slower                                      |
| pprint_pformat             | 1.51 sec                                               | 1.53 sec: 1.01x slower                                     |
| mako                       | 11.1 ms                                                | 11.2 ms: 1.01x slower                                      |
| 2to3                       | 265 ms                                                 | 269 ms: 1.02x slower                                       |
| nqueens                    | 80.6 ms                                                | 81.9 ms: 1.02x slower                                      |
| sqlglot_parse              | 1.27 ms                                                | 1.29 ms: 1.02x slower                                      |
| gc_traversal               | 3.81 ms                                                | 3.87 ms: 1.02x slower                                      |
| sympy_integrate            | 19.9 ms                                                | 20.2 ms: 1.02x slower                                      |
| deepcopy_memo              | 38.0 us                                                | 38.7 us: 1.02x slower                                      |
| unpickle_list              | 4.96 us                                                | 5.05 us: 1.02x slower                                      |
| tomli_loads                | 2.11 sec                                               | 2.15 sec: 1.02x slower                                     |
| meteor_contest             | 108 ms                                                 | 109 ms: 1.02x slower                                       |
| pickle_list                | 5.01 us                                                | 5.10 us: 1.02x slower                                      |
| sqlglot_transpile          | 1.57 ms                                                | 1.60 ms: 1.02x slower                                      |
| docutils                   | 2.58 sec                                               | 2.64 sec: 1.02x slower                                     |
| sympy_str                  | 274 ms                                                 | 281 ms: 1.03x slower                                       |
| pyflate                    | 460 ms                                                 | 473 ms: 1.03x slower                                       |
| json_loads                 | 27.0 us                                                | 27.8 us: 1.03x slower                                      |
| chameleon                  | 6.85 ms                                                | 7.07 ms: 1.03x slower                                      |
| nbody                      | 85.7 ms                                                | 88.6 ms: 1.03x slower                                      |
| xml_etree_iterparse        | 102 ms                                                 | 106 ms: 1.03x slower                                       |
| logging_format             | 6.25 us                                                | 6.47 us: 1.03x slower                                      |
| generators                 | 28.8 ms                                                | 29.9 ms: 1.04x slower                                      |
| coroutines                 | 22.5 ms                                                | 23.4 ms: 1.04x slower                                      |
| unpickle_pure_python       | 213 us                                                 | 222 us: 1.04x slower                                       |
| float                      | 78.5 ms                                                | 81.6 ms: 1.04x slower                                      |
| sympy_sum                  | 150 ms                                                 | 156 ms: 1.04x slower                                       |
| logging_simple             | 5.66 us                                                | 5.90 us: 1.04x slower                                      |
| pickle_dict                | 33.2 us                                                | 34.6 us: 1.04x slower                                      |
| raytrace                   | 262 ms                                                 | 274 ms: 1.05x slower                                       |
| async_generators           | 433 ms                                                 | 453 ms: 1.05x slower                                       |
| pidigits                   | 186 ms                                                 | 195 ms: 1.05x slower                                       |
| tornado_http               | 91.5 ms                                                | 96.0 ms: 1.05x slower                                      |
| logging_silent             | 102 ns                                                 | 107 ns: 1.05x slower                                       |
| scimark_monte_carlo        | 66.3 ms                                                | 69.5 ms: 1.05x slower                                      |
| regex_compile              | 131 ms                                                 | 138 ms: 1.06x slower                                       |
| fannkuch                   | 381 ms                                                 | 402 ms: 1.06x slower                                       |
| chaos                      | 58.4 ms                                                | 61.7 ms: 1.06x slower                                      |
| deltablue                  | 3.15 ms                                                | 3.34 ms: 1.06x slower                                      |
| dulwich_log                | 63.0 ms                                                | 67.1 ms: 1.07x slower                                      |
| coverage                   | 83.7 ms                                                | 94.4 ms: 1.13x slower                                      |
| pathlib                    | 17.1 ms                                                | 19.4 ms: 1.14x slower                                      |
| unpack_sequence            | 42.4 ns                                                | 51.0 ns: 1.20x slower                                      |
| async_tree_none            | 354 ms                                                 | 437 ms: 1.23x slower                                       |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 712 ms: 1.24x slower                                       |
| comprehensions             | 16.4 us                                                | 20.8 us: 1.27x slower                                      |
| async_tree_memoization     | 442 ms                                                 | 564 ms: 1.27x slower                                       |
| async_tree_memoization_tg  | 465 ms                                                 | 595 ms: 1.28x slower                                       |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 741 ms: 1.36x slower                                       |
| async_tree_io              | 843 ms                                                 | 1.19 sec: 1.41x slower                                     |
| async_tree_none_tg         | 320 ms                                                 | 453 ms: 1.42x slower                                       |
| async_tree_io_tg           | 825 ms                                                 | 1.23 sec: 1.49x slower                                     |
| Geometric mean             | (ref)                                                  | 1.04x slower                                               |

Benchmark hidden because not significant (14): json, go, pickle_pure_python, sqlglot_optimize, xml_etree_generate, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, deepcopy, mdp, scimark_lu, scimark_fft, unpickle, scimark_sor
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, bpe_tokeniser, dask, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, mypy2, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 0.95x