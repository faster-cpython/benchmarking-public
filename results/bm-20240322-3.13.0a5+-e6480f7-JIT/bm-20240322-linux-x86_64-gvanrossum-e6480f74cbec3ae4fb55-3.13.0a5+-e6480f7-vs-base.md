# Results vs. base

- fork: gvanrossum
- ref: e6480f74cbec3ae4fb55
- machine: linux-x86_64
- commit hash: e6480f7
- commit date: 2024-03-22
- overall geometric mean: 1.02x slower
- HPT reliability: 92.65%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240322-linux-x86_64-python-72eea512b88f8fd68b72-3.13.0a5+-72eea51 | bm-20240322-linux-x86_64-gvanrossum-e6480f74cbec3ae4fb55-3.13.0a5+-e6480f7 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| docutils       | 2.88 sec                                                               | 2.80 sec: 1.03x faster                                                     |
| html5lib       | 66.7 ms                                                                | 68.4 ms: 1.02x slower                                                      |
| tornado_http   | 97.0 ms                                                                | 99.3 ms: 1.02x slower                                                      |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                               |

Benchmark hidden because not significant (2): 2to3, chameleon

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240322-linux-x86_64-python-72eea512b88f8fd68b72-3.13.0a5+-72eea51 | bm-20240322-linux-x86_64-gvanrossum-e6480f74cbec3ae4fb55-3.13.0a5+-e6480f7 |
|----------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none            | 379 ms                                                                 | 453 ms: 1.20x slower                                                       |
| async_tree_cpu_io_mixed_tg | 618 ms                                                                 | 743 ms: 1.20x slower                                                       |
| async_tree_cpu_io_mixed    | 603 ms                                                                 | 728 ms: 1.21x slower                                                       |
| async_tree_memoization     | 463 ms                                                                 | 581 ms: 1.26x slower                                                       |
| async_tree_none_tg         | 352 ms                                                                 | 464 ms: 1.32x slower                                                       |
| async_tree_io              | 927 ms                                                                 | 1.23 sec: 1.32x slower                                                     |
| async_tree_memoization_tg  | 448 ms                                                                 | 596 ms: 1.33x slower                                                       |
| async_tree_io_tg           | 927 ms                                                                 | 1.24 sec: 1.34x slower                                                     |
| Geometric mean             | (ref)                                                                  | 1.27x slower                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240322-linux-x86_64-python-72eea512b88f8fd68b72-3.13.0a5+-72eea51 | bm-20240322-linux-x86_64-gvanrossum-e6480f74cbec3ae4fb55-3.13.0a5+-e6480f7 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 95.7 ms                                                                | 92.9 ms: 1.03x faster                                                      |
| float          | 77.2 ms                                                                | 80.6 ms: 1.04x slower                                                      |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240322-linux-x86_64-python-72eea512b88f8fd68b72-3.13.0a5+-72eea51 | bm-20240322-linux-x86_64-gvanrossum-e6480f74cbec3ae4fb55-3.13.0a5+-e6480f7 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 25.8 ms                                                                | 25.1 ms: 1.03x faster                                                      |
| regex_compile  | 144 ms                                                                 | 143 ms: 1.01x faster                                                       |
| regex_dna      | 224 ms                                                                 | 233 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                               |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240322-linux-x86_64-python-72eea512b88f8fd68b72-3.13.0a5+-72eea51 | bm-20240322-linux-x86_64-gvanrossum-e6480f74cbec3ae4fb55-3.13.0a5+-e6480f7 |
|----------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_list        | 5.14 us                                                                | 4.85 us: 1.06x faster                                                      |
| unpickle             | 15.6 us                                                                | 15.1 us: 1.03x faster                                                      |
| json_loads           | 28.6 us                                                                | 28.0 us: 1.02x faster                                                      |
| xml_etree_process    | 60.5 ms                                                                | 59.6 ms: 1.02x faster                                                      |
| pickle_pure_python   | 308 us                                                                 | 304 us: 1.01x faster                                                       |
| tomli_loads          | 2.11 sec                                                               | 2.08 sec: 1.01x faster                                                     |
| unpickle_pure_python | 241 us                                                                 | 239 us: 1.01x faster                                                       |
| xml_etree_generate   | 87.0 ms                                                                | 87.4 ms: 1.01x slower                                                      |
| xml_etree_iterparse  | 107 ms                                                                 | 109 ms: 1.02x slower                                                       |
| pickle               | 11.7 us                                                                | 11.9 us: 1.02x slower                                                      |
| pickle_dict          | 34.2 us                                                                | 35.6 us: 1.04x slower                                                      |
| pickle_list          | 4.93 us                                                                | 5.36 us: 1.09x slower                                                      |
| Geometric mean       | (ref)                                                                  | 1.00x slower                                                               |

Benchmark hidden because not significant (2): xml_etree_parse, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240322-linux-x86_64-python-72eea512b88f8fd68b72-3.13.0a5+-72eea51 | bm-20240322-linux-x86_64-gvanrossum-e6480f74cbec3ae4fb55-3.13.0a5+-e6480f7 |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 11.7 ms                                                                | 11.5 ms: 1.01x faster                                                      |
| python_startup_no_site | 10.1 ms                                                                | 10.1 ms: 1.00x slower                                                      |
| Geometric mean         | (ref)                                                                  | 1.01x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240322-linux-x86_64-python-72eea512b88f8fd68b72-3.13.0a5+-72eea51 | bm-20240322-linux-x86_64-gvanrossum-e6480f74cbec3ae4fb55-3.13.0a5+-e6480f7 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako           | 11.0 ms                                                                | 11.0 ms: 1.00x faster                                                      |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                               |

Benchmark hidden because not significant (3): genshi_text, genshi_xml, django_template

All benchmarks:
===============

| Benchmark                  | bm-20240322-linux-x86_64-python-72eea512b88f8fd68b72-3.13.0a5+-72eea51 | bm-20240322-linux-x86_64-gvanrossum-e6480f74cbec3ae4fb55-3.13.0a5+-e6480f7 |
|----------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mdp                        | 2.80 sec                                                               | 2.64 sec: 1.06x faster                                                     |
| unpickle_list              | 5.14 us                                                                | 4.85 us: 1.06x faster                                                      |
| unpack_sequence            | 93.0 ns                                                                | 89.0 ns: 1.04x faster                                                      |
| scimark_sparse_mat_mult    | 4.99 ms                                                                | 4.78 ms: 1.04x faster                                                      |
| djangocms                  | 32.6 us                                                                | 31.5 us: 1.03x faster                                                      |
| unpickle                   | 15.6 us                                                                | 15.1 us: 1.03x faster                                                      |
| nbody                      | 95.7 ms                                                                | 92.9 ms: 1.03x faster                                                      |
| docutils                   | 2.88 sec                                                               | 2.80 sec: 1.03x faster                                                     |
| generators                 | 30.4 ms                                                                | 29.5 ms: 1.03x faster                                                      |
| regex_v8                   | 25.8 ms                                                                | 25.1 ms: 1.03x faster                                                      |
| json                       | 5.44 ms                                                                | 5.31 ms: 1.02x faster                                                      |
| scimark_monte_carlo        | 72.1 ms                                                                | 70.6 ms: 1.02x faster                                                      |
| coroutines                 | 23.7 ms                                                                | 23.2 ms: 1.02x faster                                                      |
| logging_simple             | 5.98 us                                                                | 5.86 us: 1.02x faster                                                      |
| json_loads                 | 28.6 us                                                                | 28.0 us: 1.02x faster                                                      |
| thrift                     | 824 us                                                                 | 808 us: 1.02x faster                                                       |
| scimark_fft                | 346 ms                                                                 | 341 ms: 1.02x faster                                                       |
| sympy_str                  | 293 ms                                                                 | 288 ms: 1.02x faster                                                       |
| xml_etree_process          | 60.5 ms                                                                | 59.6 ms: 1.02x faster                                                      |
| chaos                      | 64.9 ms                                                                | 63.9 ms: 1.02x faster                                                      |
| logging_format             | 6.63 us                                                                | 6.53 us: 1.01x faster                                                      |
| sympy_integrate            | 22.0 ms                                                                | 21.7 ms: 1.01x faster                                                      |
| sympy_expand               | 497 ms                                                                 | 490 ms: 1.01x faster                                                       |
| pathlib                    | 19.0 ms                                                                | 18.7 ms: 1.01x faster                                                      |
| python_startup             | 11.7 ms                                                                | 11.5 ms: 1.01x faster                                                      |
| pickle_pure_python         | 308 us                                                                 | 304 us: 1.01x faster                                                       |
| dulwich_log                | 70.7 ms                                                                | 69.8 ms: 1.01x faster                                                      |
| deepcopy_reduce            | 3.19 us                                                                | 3.15 us: 1.01x faster                                                      |
| typing_runtime_protocols   | 114 us                                                                 | 112 us: 1.01x faster                                                       |
| pprint_safe_repr           | 752 ms                                                                 | 743 ms: 1.01x faster                                                       |
| tomli_loads                | 2.11 sec                                                               | 2.08 sec: 1.01x faster                                                     |
| hexiom                     | 7.10 ms                                                                | 7.02 ms: 1.01x faster                                                      |
| richards_super             | 53.3 ms                                                                | 52.7 ms: 1.01x faster                                                      |
| asyncio_websockets         | 570 ms                                                                 | 563 ms: 1.01x faster                                                       |
| sqlglot_normalize          | 113 ms                                                                 | 112 ms: 1.01x faster                                                       |
| bench_thread_pool          | 858 us                                                                 | 850 us: 1.01x faster                                                       |
| raytrace                   | 297 ms                                                                 | 294 ms: 1.01x faster                                                       |
| deepcopy                   | 358 us                                                                 | 355 us: 1.01x faster                                                       |
| sqlglot_optimize           | 58.2 ms                                                                | 57.7 ms: 1.01x faster                                                      |
| aiohttp                    | 1.22 ms                                                                | 1.21 ms: 1.01x faster                                                      |
| sympy_sum                  | 166 ms                                                                 | 164 ms: 1.01x faster                                                       |
| regex_compile              | 144 ms                                                                 | 143 ms: 1.01x faster                                                       |
| gunicorn                   | 1.32 ms                                                                | 1.31 ms: 1.01x faster                                                      |
| unpickle_pure_python       | 241 us                                                                 | 239 us: 1.01x faster                                                       |
| fannkuch                   | 401 ms                                                                 | 399 ms: 1.01x faster                                                       |
| comprehensions             | 18.1 us                                                                | 17.9 us: 1.01x faster                                                      |
| asyncio_tcp                | 512 ms                                                                 | 509 ms: 1.01x faster                                                       |
| pyflate                    | 492 ms                                                                 | 489 ms: 1.01x faster                                                       |
| go                         | 156 ms                                                                 | 155 ms: 1.00x faster                                                       |
| mako                       | 11.0 ms                                                                | 11.0 ms: 1.00x faster                                                      |
| python_startup_no_site     | 10.1 ms                                                                | 10.1 ms: 1.00x slower                                                      |
| sqlglot_transpile          | 1.65 ms                                                                | 1.66 ms: 1.00x slower                                                      |
| xml_etree_generate         | 87.0 ms                                                                | 87.4 ms: 1.01x slower                                                      |
| nqueens                    | 89.2 ms                                                                | 89.8 ms: 1.01x slower                                                      |
| scimark_sor                | 130 ms                                                                 | 131 ms: 1.01x slower                                                       |
| telco                      | 8.47 ms                                                                | 8.57 ms: 1.01x slower                                                      |
| xml_etree_iterparse        | 107 ms                                                                 | 109 ms: 1.02x slower                                                       |
| pickle                     | 11.7 us                                                                | 11.9 us: 1.02x slower                                                      |
| deepcopy_memo              | 39.1 us                                                                | 39.8 us: 1.02x slower                                                      |
| tornado_http               | 97.0 ms                                                                | 99.3 ms: 1.02x slower                                                      |
| html5lib                   | 66.7 ms                                                                | 68.4 ms: 1.02x slower                                                      |
| async_generators           | 460 ms                                                                 | 475 ms: 1.03x slower                                                       |
| create_gc_cycles           | 1.48 ms                                                                | 1.53 ms: 1.04x slower                                                      |
| pickle_dict                | 34.2 us                                                                | 35.6 us: 1.04x slower                                                      |
| regex_dna                  | 224 ms                                                                 | 233 ms: 1.04x slower                                                       |
| float                      | 77.2 ms                                                                | 80.6 ms: 1.04x slower                                                      |
| pycparser                  | 1.18 sec                                                               | 1.23 sec: 1.05x slower                                                     |
| gc_traversal               | 3.74 ms                                                                | 3.93 ms: 1.05x slower                                                      |
| pickle_list                | 4.93 us                                                                | 5.36 us: 1.09x slower                                                      |
| mypy2                      | 790 ms                                                                 | 905 ms: 1.15x slower                                                       |
| async_tree_none            | 379 ms                                                                 | 453 ms: 1.20x slower                                                       |
| async_tree_cpu_io_mixed_tg | 618 ms                                                                 | 743 ms: 1.20x slower                                                       |
| async_tree_cpu_io_mixed    | 603 ms                                                                 | 728 ms: 1.21x slower                                                       |
| async_tree_memoization     | 463 ms                                                                 | 581 ms: 1.26x slower                                                       |
| async_tree_none_tg         | 352 ms                                                                 | 464 ms: 1.32x slower                                                       |
| async_tree_io              | 927 ms                                                                 | 1.23 sec: 1.32x slower                                                     |
| async_tree_memoization_tg  | 448 ms                                                                 | 596 ms: 1.33x slower                                                       |
| async_tree_io_tg           | 927 ms                                                                 | 1.24 sec: 1.34x slower                                                     |
| Geometric mean             | (ref)                                                                  | 1.02x slower                                                               |

Benchmark hidden because not significant (24): pylint, crypto_pyaes, genshi_text, dask, genshi_xml, chameleon, richards, meteor_contest, 2to3, bench_mp_pool, sqlglot_parse, pprint_pformat, regex_effbot, spectral_norm, asyncio_tcp_ssl, pidigits, sqlite_synth, logging_silent, xml_etree_parse, deltablue, django_template, json_dumps, scimark_lu, coverage


# HPT report

- Reliability score: 92.65% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x


# Memory

- memory change: 0.98x