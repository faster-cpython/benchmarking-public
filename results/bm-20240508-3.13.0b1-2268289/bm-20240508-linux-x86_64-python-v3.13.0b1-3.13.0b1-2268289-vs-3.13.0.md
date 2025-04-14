# Results vs. 3.13.0

- fork: python
- ref: v3.13.0b1
- machine: linux-x86_64
- commit hash: 2268289
- commit date: 2024-05-08
- overall geometric mean: 1.047x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: 0.91x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240508-linux-x86_64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 272 ms: 1.02x slower                                       |
| chameleon      | 6.94 ms                                                | 7.11 ms: 1.03x slower                                      |
| docutils       | 2.59 sec                                               | 2.86 sec: 1.10x slower                                     |
| html5lib       | 64.2 ms                                                | 68.4 ms: 1.07x slower                                      |
| tornado_http   | 92.4 ms                                                | 95.8 ms: 1.04x slower                                      |
| Geometric mean | (ref)                                                  | 1.05x slower                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240508-linux-x86_64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| asyncio_websockets         | 552 ms                                                 | 564 ms: 1.02x slower                                       |
| async_tree_none            | 351 ms                                                 | 363 ms: 1.04x slower                                       |
| async_generators           | 436 ms                                                 | 452 ms: 1.04x slower                                       |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 619 ms: 1.07x slower                                       |
| async_tree_memoization     | 442 ms                                                 | 477 ms: 1.08x slower                                       |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 589 ms: 1.08x slower                                       |
| async_tree_none_tg         | 321 ms                                                 | 346 ms: 1.08x slower                                       |
| async_tree_io              | 842 ms                                                 | 936 ms: 1.11x slower                                       |
| async_tree_io_tg           | 857 ms                                                 | 987 ms: 1.15x slower                                       |
| Geometric mean             | (ref)                                                  | 1.06x slower                                               |

Benchmark hidden because not significant (2): async_tree_memoization_tg, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240508-linux-x86_64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| float          | 79.2 ms                                                | 78.5 ms: 1.01x faster                                      |
| nbody          | 87.0 ms                                                | 87.8 ms: 1.01x slower                                      |
| pidigits       | 186 ms                                                 | 189 ms: 1.01x slower                                       |
| Geometric mean | (ref)                                                  | 1.00x slower                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240508-linux-x86_64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_effbot   | 3.73 ms                                                | 3.67 ms: 1.02x faster                                      |
| regex_compile  | 132 ms                                                 | 135 ms: 1.02x slower                                       |
| regex_dna      | 218 ms                                                 | 226 ms: 1.03x slower                                       |
| Geometric mean | (ref)                                                  | 1.01x slower                                               |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240508-linux-x86_64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| json_dumps           | 10.6 ms                                                | 10.5 ms: 1.01x faster                                      |
| xml_etree_process    | 60.6 ms                                                | 60.3 ms: 1.01x faster                                      |
| xml_etree_generate   | 86.7 ms                                                | 87.7 ms: 1.01x slower                                      |
| xml_etree_parse      | 156 ms                                                 | 159 ms: 1.02x slower                                       |
| unpickle_pure_python | 216 us                                                 | 223 us: 1.03x slower                                       |
| tomli_loads          | 2.14 sec                                               | 2.22 sec: 1.03x slower                                     |
| json_loads           | 27.2 us                                                | 28.9 us: 1.06x slower                                      |
| xml_etree_iterparse  | 101 ms                                                 | 108 ms: 1.06x slower                                       |
| Geometric mean       | (ref)                                                  | 1.02x slower                                               |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240508-linux-x86_64-python-v3.13.0b1-3.13.0b1-2268289 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 10.7 ms: 1.17x faster                                      |
| python_startup_no_site | 6.96 ms                                                | 7.19 ms: 1.03x slower                                      |
| Geometric mean         | (ref)                                                  | 1.06x faster                                               |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240508-linux-x86_64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| genshi_text    | 23.5 ms                                                | 23.1 ms: 1.02x faster                                      |
| mako           | 11.1 ms                                                | 10.9 ms: 1.02x faster                                      |
| genshi_xml     | 50.9 ms                                                | 52.1 ms: 1.02x slower                                      |
| Geometric mean | (ref)                                                  | 1.00x faster                                               |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240508-linux-x86_64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| mypy2                      | 1.04 sec                                               | 743 ms: 1.40x faster                                       |
| create_gc_cycles           | 2.41 ms                                                | 1.80 ms: 1.34x faster                                      |
| python_startup             | 12.5 ms                                                | 10.7 ms: 1.17x faster                                      |
| gc_traversal               | 4.37 ms                                                | 3.85 ms: 1.13x faster                                      |
| mdp                        | 2.72 sec                                               | 2.60 sec: 1.05x faster                                     |
| fannkuch                   | 404 ms                                                 | 393 ms: 1.03x faster                                       |
| spectral_norm              | 115 ms                                                 | 113 ms: 1.02x faster                                       |
| genshi_text                | 23.5 ms                                                | 23.1 ms: 1.02x faster                                      |
| regex_effbot               | 3.73 ms                                                | 3.67 ms: 1.02x faster                                      |
| mako                       | 11.1 ms                                                | 10.9 ms: 1.02x faster                                      |
| json_dumps                 | 10.6 ms                                                | 10.5 ms: 1.01x faster                                      |
| thrift                     | 809 us                                                 | 801 us: 1.01x faster                                       |
| float                      | 79.2 ms                                                | 78.5 ms: 1.01x faster                                      |
| xml_etree_process          | 60.6 ms                                                | 60.3 ms: 1.01x faster                                      |
| bench_mp_pool              | 24.0 ms                                                | 23.9 ms: 1.00x faster                                      |
| hexiom                     | 6.16 ms                                                | 6.15 ms: 1.00x faster                                      |
| pyflate                    | 471 ms                                                 | 473 ms: 1.00x slower                                       |
| deepcopy_memo              | 39.1 us                                                | 39.4 us: 1.01x slower                                      |
| nbody                      | 87.0 ms                                                | 87.8 ms: 1.01x slower                                      |
| json                       | 5.36 ms                                                | 5.41 ms: 1.01x slower                                      |
| generators                 | 29.0 ms                                                | 29.3 ms: 1.01x slower                                      |
| xml_etree_generate         | 86.7 ms                                                | 87.7 ms: 1.01x slower                                      |
| crypto_pyaes               | 75.3 ms                                                | 76.2 ms: 1.01x slower                                      |
| chaos                      | 58.1 ms                                                | 58.8 ms: 1.01x slower                                      |
| deltablue                  | 3.23 ms                                                | 3.27 ms: 1.01x slower                                      |
| pidigits                   | 186 ms                                                 | 189 ms: 1.01x slower                                       |
| meteor_contest             | 109 ms                                                 | 110 ms: 1.01x slower                                       |
| go                         | 144 ms                                                 | 146 ms: 1.02x slower                                       |
| pathlib                    | 17.5 ms                                                | 17.9 ms: 1.02x slower                                      |
| deepcopy_reduce            | 3.20 us                                                | 3.26 us: 1.02x slower                                      |
| regex_compile              | 132 ms                                                 | 135 ms: 1.02x slower                                       |
| 2to3                       | 267 ms                                                 | 272 ms: 1.02x slower                                       |
| xml_etree_parse            | 156 ms                                                 | 159 ms: 1.02x slower                                       |
| bench_thread_pool          | 822 us                                                 | 839 us: 1.02x slower                                       |
| deepcopy                   | 358 us                                                 | 366 us: 1.02x slower                                       |
| asyncio_websockets         | 552 ms                                                 | 564 ms: 1.02x slower                                       |
| logging_format             | 6.40 us                                                | 6.54 us: 1.02x slower                                      |
| genshi_xml                 | 50.9 ms                                                | 52.1 ms: 1.02x slower                                      |
| scimark_fft                | 364 ms                                                 | 373 ms: 1.02x slower                                       |
| scimark_lu                 | 113 ms                                                 | 115 ms: 1.02x slower                                       |
| sqlglot_transpile          | 1.58 ms                                                | 1.62 ms: 1.03x slower                                      |
| chameleon                  | 6.94 ms                                                | 7.11 ms: 1.03x slower                                      |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 5.18 ms: 1.03x slower                                      |
| sqlglot_parse              | 1.27 ms                                                | 1.31 ms: 1.03x slower                                      |
| sympy_expand               | 463 ms                                                 | 477 ms: 1.03x slower                                       |
| comprehensions             | 16.5 us                                                | 17.0 us: 1.03x slower                                      |
| typing_runtime_protocols   | 165 us                                                 | 170 us: 1.03x slower                                       |
| sympy_integrate            | 19.9 ms                                                | 20.5 ms: 1.03x slower                                      |
| logging_simple             | 5.72 us                                                | 5.91 us: 1.03x slower                                      |
| regex_dna                  | 218 ms                                                 | 226 ms: 1.03x slower                                       |
| scimark_sor                | 124 ms                                                 | 128 ms: 1.03x slower                                       |
| python_startup_no_site     | 6.96 ms                                                | 7.19 ms: 1.03x slower                                      |
| unpickle_pure_python       | 216 us                                                 | 223 us: 1.03x slower                                       |
| sympy_str                  | 275 ms                                                 | 284 ms: 1.03x slower                                       |
| tomli_loads                | 2.14 sec                                               | 2.22 sec: 1.03x slower                                     |
| scimark_monte_carlo        | 67.4 ms                                                | 69.9 ms: 1.04x slower                                      |
| async_tree_none            | 351 ms                                                 | 363 ms: 1.04x slower                                       |
| tornado_http               | 92.4 ms                                                | 95.8 ms: 1.04x slower                                      |
| async_generators           | 436 ms                                                 | 452 ms: 1.04x slower                                       |
| richards                   | 48.7 ms                                                | 50.5 ms: 1.04x slower                                      |
| nqueens                    | 78.4 ms                                                | 81.4 ms: 1.04x slower                                      |
| sqlglot_optimize           | 53.7 ms                                                | 55.8 ms: 1.04x slower                                      |
| dulwich_log                | 64.3 ms                                                | 67.0 ms: 1.04x slower                                      |
| logging_silent             | 102 ns                                                 | 106 ns: 1.04x slower                                       |
| richards_super             | 54.9 ms                                                | 57.4 ms: 1.05x slower                                      |
| sympy_sum                  | 150 ms                                                 | 157 ms: 1.05x slower                                       |
| sqlglot_normalize          | 108 ms                                                 | 113 ms: 1.05x slower                                       |
| pprint_pformat             | 1.49 sec                                               | 1.57 sec: 1.05x slower                                     |
| pprint_safe_repr           | 728 ms                                                 | 767 ms: 1.05x slower                                       |
| json_loads                 | 27.2 us                                                | 28.9 us: 1.06x slower                                      |
| xml_etree_iterparse        | 101 ms                                                 | 108 ms: 1.06x slower                                       |
| html5lib                   | 64.2 ms                                                | 68.4 ms: 1.07x slower                                      |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 619 ms: 1.07x slower                                       |
| async_tree_memoization     | 442 ms                                                 | 477 ms: 1.08x slower                                       |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 589 ms: 1.08x slower                                       |
| async_tree_none_tg         | 321 ms                                                 | 346 ms: 1.08x slower                                       |
| coverage                   | 84.0 ms                                                | 92.4 ms: 1.10x slower                                      |
| docutils                   | 2.59 sec                                               | 2.86 sec: 1.10x slower                                     |
| async_tree_io              | 842 ms                                                 | 936 ms: 1.11x slower                                       |
| async_tree_io_tg           | 857 ms                                                 | 987 ms: 1.15x slower                                       |
| telco                      | 8.54 ms                                                | 173 ms: 20.19x slower                                      |
| Geometric mean             | (ref)                                                  | 1.05x slower                                               |

Benchmark hidden because not significant (8): async_tree_memoization_tg, coroutines, django_template, regex_v8, raytrace, pickle_pure_python, pycparser, pylint
Ignored benchmarks (8) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: bpe_tokeniser, connected_components, gevent_hub, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (13) of results/bm-20240508-3.13.0b1-2268289/bm-20240508-linux-x86_64-python-v3.13.0b1-3.13.0b1-2268289.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, djangocms, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.047x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 0.91x