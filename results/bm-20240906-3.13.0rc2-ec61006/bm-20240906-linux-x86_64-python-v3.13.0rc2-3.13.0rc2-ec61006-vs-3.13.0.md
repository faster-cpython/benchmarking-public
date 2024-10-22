# Results vs. 3.13.0

- fork: python
- ref: v3.13.0rc2
- machine: linux-x86_64
- commit hash: ec61006
- commit date: 2024-09-06
- overall geometric mean: 1.01x slower
- HPT reliability: 99.30%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-linux-x86_64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 263 ms: 1.01x faster                                         |
| chameleon      | 6.85 ms                                                | 6.97 ms: 1.02x slower                                        |
| docutils       | 2.58 sec                                               | 2.74 sec: 1.06x slower                                       |
| html5lib       | 64.5 ms                                                | 64.9 ms: 1.01x slower                                        |
| Geometric mean | (ref)                                                  | 1.02x slower                                                 |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-linux-x86_64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 434 ms: 1.07x faster                                         |
| coroutines                 | 22.5 ms                                                | 22.1 ms: 1.02x faster                                        |
| asyncio_tcp                | 488 ms                                                 | 480 ms: 1.02x faster                                         |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.78 sec: 1.01x faster                                       |
| async_generators           | 433 ms                                                 | 435 ms: 1.01x slower                                         |
| async_tree_none            | 354 ms                                                 | 362 ms: 1.02x slower                                         |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 588 ms: 1.03x slower                                         |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 564 ms: 1.04x slower                                         |
| async_tree_none_tg         | 320 ms                                                 | 336 ms: 1.05x slower                                         |
| async_tree_io              | 843 ms                                                 | 889 ms: 1.05x slower                                         |
| async_tree_io_tg           | 825 ms                                                 | 931 ms: 1.13x slower                                         |
| Geometric mean             | (ref)                                                  | 1.02x slower                                                 |

Benchmark hidden because not significant (2): asyncio_websockets, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-linux-x86_64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| float          | 78.5 ms                                                | 77.4 ms: 1.01x faster                                        |
| nbody          | 85.7 ms                                                | 88.0 ms: 1.03x slower                                        |
| Geometric mean | (ref)                                                  | 1.00x slower                                                 |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-linux-x86_64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.49 ms: 1.11x faster                                        |
| regex_v8       | 25.3 ms                                                | 24.2 ms: 1.05x faster                                        |
| regex_dna      | 220 ms                                                 | 216 ms: 1.02x faster                                         |
| regex_compile  | 131 ms                                                 | 133 ms: 1.02x slower                                         |
| Geometric mean | (ref)                                                  | 1.04x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-linux-x86_64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| tomli_loads          | 2.11 sec                                               | 2.07 sec: 1.02x faster                                       |
| pickle               | 11.6 us                                                | 11.4 us: 1.01x faster                                        |
| json_loads           | 27.0 us                                                | 27.1 us: 1.00x slower                                        |
| unpickle             | 14.9 us                                                | 14.9 us: 1.00x slower                                        |
| xml_etree_process    | 60.4 ms                                                | 60.8 ms: 1.01x slower                                        |
| xml_etree_generate   | 87.0 ms                                                | 87.5 ms: 1.01x slower                                        |
| pickle_pure_python   | 300 us                                                 | 302 us: 1.01x slower                                         |
| unpickle_list        | 4.96 us                                                | 5.06 us: 1.02x slower                                        |
| unpickle_pure_python | 213 us                                                 | 218 us: 1.02x slower                                         |
| pickle_dict          | 33.2 us                                                | 34.5 us: 1.04x slower                                        |
| pickle_list          | 5.01 us                                                | 5.25 us: 1.05x slower                                        |
| xml_etree_iterparse  | 102 ms                                                 | 107 ms: 1.05x slower                                         |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                 |

Benchmark hidden because not significant (2): json_dumps, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-linux-x86_64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup_no_site | 6.99 ms                                                | 6.96 ms: 1.00x faster                                        |
| python_startup         | 10.6 ms                                                | 10.5 ms: 1.00x faster                                        |
| Geometric mean         | (ref)                                                  | 1.00x faster                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-linux-x86_64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| django_template | 34.4 ms                                                | 33.9 ms: 1.01x faster                                        |
| genshi_xml      | 50.3 ms                                                | 50.9 ms: 1.01x slower                                        |
| genshi_text     | 22.9 ms                                                | 23.4 ms: 1.02x slower                                        |
| mako            | 11.1 ms                                                | 11.4 ms: 1.03x slower                                        |
| Geometric mean  | (ref)                                                  | 1.01x slower                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-linux-x86_64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| mypy2                      | 1.07 sec                                               | 717 ms: 1.49x faster                                         |
| regex_effbot               | 3.88 ms                                                | 3.49 ms: 1.11x faster                                        |
| async_tree_memoization_tg  | 465 ms                                                 | 434 ms: 1.07x faster                                         |
| pycparser                  | 1.19 sec                                               | 1.14 sec: 1.05x faster                                       |
| regex_v8                   | 25.3 ms                                                | 24.2 ms: 1.05x faster                                        |
| richards_super             | 54.4 ms                                                | 53.2 ms: 1.02x faster                                        |
| nqueens                    | 80.6 ms                                                | 78.9 ms: 1.02x faster                                        |
| tomli_loads                | 2.11 sec                                               | 2.07 sec: 1.02x faster                                       |
| scimark_lu                 | 115 ms                                                 | 113 ms: 1.02x faster                                         |
| gc_traversal               | 3.81 ms                                                | 3.73 ms: 1.02x faster                                        |
| coroutines                 | 22.5 ms                                                | 22.1 ms: 1.02x faster                                        |
| richards                   | 48.1 ms                                                | 47.3 ms: 1.02x faster                                        |
| asyncio_tcp                | 488 ms                                                 | 480 ms: 1.02x faster                                         |
| regex_dna                  | 220 ms                                                 | 216 ms: 1.02x faster                                         |
| django_template            | 34.4 ms                                                | 33.9 ms: 1.01x faster                                        |
| float                      | 78.5 ms                                                | 77.4 ms: 1.01x faster                                        |
| pickle                     | 11.6 us                                                | 11.4 us: 1.01x faster                                        |
| scimark_fft                | 369 ms                                                 | 365 ms: 1.01x faster                                         |
| go                         | 142 ms                                                 | 141 ms: 1.01x faster                                         |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.78 sec: 1.01x faster                                       |
| 2to3                       | 265 ms                                                 | 263 ms: 1.01x faster                                         |
| python_startup_no_site     | 6.99 ms                                                | 6.96 ms: 1.00x faster                                        |
| python_startup             | 10.6 ms                                                | 10.5 ms: 1.00x faster                                        |
| sympy_integrate            | 19.9 ms                                                | 19.9 ms: 1.00x slower                                        |
| json_loads                 | 27.0 us                                                | 27.1 us: 1.00x slower                                        |
| comprehensions             | 16.4 us                                                | 16.4 us: 1.00x slower                                        |
| mdp                        | 2.74 sec                                               | 2.75 sec: 1.00x slower                                       |
| bench_thread_pool          | 815 us                                                 | 818 us: 1.00x slower                                         |
| unpickle                   | 14.9 us                                                | 14.9 us: 1.00x slower                                        |
| async_generators           | 433 ms                                                 | 435 ms: 1.01x slower                                         |
| html5lib                   | 64.5 ms                                                | 64.9 ms: 1.01x slower                                        |
| xml_etree_process          | 60.4 ms                                                | 60.8 ms: 1.01x slower                                        |
| pprint_pformat             | 1.51 sec                                               | 1.52 sec: 1.01x slower                                       |
| xml_etree_generate         | 87.0 ms                                                | 87.5 ms: 1.01x slower                                        |
| pickle_pure_python         | 300 us                                                 | 302 us: 1.01x slower                                         |
| gunicorn                   | 1.23 ms                                                | 1.24 ms: 1.01x slower                                        |
| pathlib                    | 17.1 ms                                                | 17.2 ms: 1.01x slower                                        |
| generators                 | 28.8 ms                                                | 29.1 ms: 1.01x slower                                        |
| sympy_sum                  | 150 ms                                                 | 151 ms: 1.01x slower                                         |
| genshi_xml                 | 50.3 ms                                                | 50.9 ms: 1.01x slower                                        |
| thrift                     | 796 us                                                 | 806 us: 1.01x slower                                         |
| dulwich_log                | 63.0 ms                                                | 63.7 ms: 1.01x slower                                        |
| sqlglot_normalize          | 107 ms                                                 | 109 ms: 1.01x slower                                         |
| meteor_contest             | 108 ms                                                 | 109 ms: 1.01x slower                                         |
| spectral_norm              | 115 ms                                                 | 117 ms: 1.01x slower                                         |
| sqlglot_transpile          | 1.57 ms                                                | 1.60 ms: 1.01x slower                                        |
| regex_compile              | 131 ms                                                 | 133 ms: 1.02x slower                                         |
| pyflate                    | 460 ms                                                 | 467 ms: 1.02x slower                                         |
| chameleon                  | 6.85 ms                                                | 6.97 ms: 1.02x slower                                        |
| deepcopy_reduce            | 3.17 us                                                | 3.22 us: 1.02x slower                                        |
| typing_runtime_protocols   | 159 us                                                 | 162 us: 1.02x slower                                         |
| deepcopy                   | 352 us                                                 | 359 us: 1.02x slower                                         |
| sqlglot_parse              | 1.27 ms                                                | 1.29 ms: 1.02x slower                                        |
| unpickle_list              | 4.96 us                                                | 5.06 us: 1.02x slower                                        |
| djangocms                  | 31.9 us                                                | 32.5 us: 1.02x slower                                        |
| telco                      | 8.45 ms                                                | 8.63 ms: 1.02x slower                                        |
| chaos                      | 58.4 ms                                                | 59.6 ms: 1.02x slower                                        |
| raytrace                   | 262 ms                                                 | 267 ms: 1.02x slower                                         |
| logging_format             | 6.25 us                                                | 6.39 us: 1.02x slower                                        |
| unpickle_pure_python       | 213 us                                                 | 218 us: 1.02x slower                                         |
| async_tree_none            | 354 ms                                                 | 362 ms: 1.02x slower                                         |
| genshi_text                | 22.9 ms                                                | 23.4 ms: 1.02x slower                                        |
| bpe_tokeniser              | 4.69 sec                                               | 4.80 sec: 1.02x slower                                       |
| async_tree_cpu_io_mixed    | 574 ms                                                 | 588 ms: 1.03x slower                                         |
| mako                       | 11.1 ms                                                | 11.4 ms: 1.03x slower                                        |
| nbody                      | 85.7 ms                                                | 88.0 ms: 1.03x slower                                        |
| hexiom                     | 6.13 ms                                                | 6.29 ms: 1.03x slower                                        |
| scimark_monte_carlo        | 66.3 ms                                                | 68.2 ms: 1.03x slower                                        |
| scimark_sor                | 122 ms                                                 | 126 ms: 1.03x slower                                         |
| deltablue                  | 3.15 ms                                                | 3.25 ms: 1.03x slower                                        |
| crypto_pyaes               | 73.0 ms                                                | 75.3 ms: 1.03x slower                                        |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 564 ms: 1.04x slower                                         |
| deepcopy_memo              | 38.0 us                                                | 39.5 us: 1.04x slower                                        |
| pickle_dict                | 33.2 us                                                | 34.5 us: 1.04x slower                                        |
| fannkuch                   | 381 ms                                                 | 398 ms: 1.05x slower                                         |
| pickle_list                | 5.01 us                                                | 5.25 us: 1.05x slower                                        |
| async_tree_none_tg         | 320 ms                                                 | 336 ms: 1.05x slower                                         |
| xml_etree_iterparse        | 102 ms                                                 | 107 ms: 1.05x slower                                         |
| async_tree_io              | 843 ms                                                 | 889 ms: 1.05x slower                                         |
| dask                       | 338 ms                                                 | 358 ms: 1.06x slower                                         |
| docutils                   | 2.58 sec                                               | 2.74 sec: 1.06x slower                                       |
| create_gc_cycles           | 1.61 ms                                                | 1.74 ms: 1.08x slower                                        |
| async_tree_io_tg           | 825 ms                                                 | 931 ms: 1.13x slower                                         |
| unpack_sequence            | 42.4 ns                                                | 47.9 ns: 1.13x slower                                        |
| Geometric mean             | (ref)                                                  | 1.01x slower                                                 |

Benchmark hidden because not significant (20): json_dumps, scimark_sparse_mat_mult, sqlite_synth, tornado_http, asyncio_websockets, pprint_safe_repr, aiohttp, xml_etree_parse, pidigits, sqlglot_optimize, bench_mp_pool, logging_silent, coverage, sympy_str, logging_simple, flaskblogging, sympy_expand, json, async_tree_memoization, pylint

# HPT report

- Reliability score: 99.30% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.02x