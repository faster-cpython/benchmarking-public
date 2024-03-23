# Results vs. 3.11.0

- fork: gvanrossum
- ref: e6480f74cbec3ae4fb55
- machine: linux-x86_64
- commit hash: e6480f7
- commit date: 2024-03-22
- overall geometric mean: 1.02x faster
- HPT reliability: 65.26%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240322-linux-x86_64-gvanrossum-e6480f74cbec3ae4fb55-3.13.0a5+-e6480f7 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 264 ms                                                 | 280 ms: 1.06x slower                                                       |
| chameleon      | 6.70 ms                                                | 7.11 ms: 1.06x slower                                                      |
| docutils       | 2.66 sec                                               | 2.80 sec: 1.05x slower                                                     |
| html5lib       | 64.8 ms                                                | 68.4 ms: 1.05x slower                                                      |
| tornado_http   | 98.1 ms                                                | 99.3 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                  | 1.05x slower                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240322-linux-x86_64-gvanrossum-e6480f74cbec3ae4fb55-3.13.0a5+-e6480f7 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_none            | 528 ms                                                 | 453 ms: 1.17x faster                                                       |
| async_tree_memoization     | 639 ms                                                 | 581 ms: 1.10x faster                                                       |
| async_tree_none_tg         | 491 ms                                                 | 464 ms: 1.06x faster                                                       |
| async_tree_memoization_tg  | 626 ms                                                 | 596 ms: 1.05x faster                                                       |
| async_tree_io              | 1.29 sec                                               | 1.23 sec: 1.05x faster                                                     |
| async_tree_io_tg           | 1.29 sec                                               | 1.24 sec: 1.04x faster                                                     |
| async_tree_cpu_io_mixed    | 749 ms                                                 | 728 ms: 1.03x faster                                                       |
| async_tree_cpu_io_mixed_tg | 761 ms                                                 | 743 ms: 1.02x faster                                                       |
| Geometric mean             | (ref)                                                  | 1.06x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240322-linux-x86_64-gvanrossum-e6480f74cbec3ae4fb55-3.13.0a5+-e6480f7 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 96.0 ms                                                | 92.9 ms: 1.03x faster                                                      |
| pidigits       | 194 ms                                                 | 190 ms: 1.02x faster                                                       |
| float          | 78.9 ms                                                | 80.6 ms: 1.02x slower                                                      |
| Geometric mean | (ref)                                                  | 1.01x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240322-linux-x86_64-gvanrossum-e6480f74cbec3ae4fb55-3.13.0a5+-e6480f7 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 141 ms                                                 | 143 ms: 1.01x slower                                                       |
| regex_effbot   | 3.51 ms                                                | 3.85 ms: 1.10x slower                                                      |
| regex_v8       | 22.9 ms                                                | 25.1 ms: 1.10x slower                                                      |
| regex_dna      | 205 ms                                                 | 233 ms: 1.14x slower                                                       |
| Geometric mean | (ref)                                                  | 1.09x slower                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240322-linux-x86_64-gvanrossum-e6480f74cbec3ae4fb55-3.13.0a5+-e6480f7 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 13.3 ms                                                | 10.5 ms: 1.27x faster                                                      |
| tomli_loads          | 2.30 sec                                               | 2.08 sec: 1.11x faster                                                     |
| unpickle_list        | 5.21 us                                                | 4.85 us: 1.08x faster                                                      |
| pickle_pure_python   | 320 us                                                 | 304 us: 1.05x faster                                                       |
| json_loads           | 29.2 us                                                | 28.0 us: 1.04x faster                                                      |
| xml_etree_parse      | 164 ms                                                 | 160 ms: 1.03x faster                                                       |
| unpickle_pure_python | 242 us                                                 | 239 us: 1.01x faster                                                       |
| xml_etree_iterparse  | 108 ms                                                 | 109 ms: 1.01x slower                                                       |
| pickle_dict          | 34.6 us                                                | 35.6 us: 1.03x slower                                                      |
| xml_etree_process    | 56.9 ms                                                | 59.6 ms: 1.05x slower                                                      |
| xml_etree_generate   | 81.1 ms                                                | 87.4 ms: 1.08x slower                                                      |
| pickle               | 11.0 us                                                | 11.9 us: 1.08x slower                                                      |
| unpickle             | 13.8 us                                                | 15.1 us: 1.09x slower                                                      |
| pickle_list          | 4.59 us                                                | 5.36 us: 1.17x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.00x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240322-linux-x86_64-gvanrossum-e6480f74cbec3ae4fb55-3.13.0a5+-e6480f7 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 8.56 ms                                                | 11.5 ms: 1.34x slower                                                      |
| python_startup_no_site | 6.01 ms                                                | 10.1 ms: 1.68x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.50x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240322-linux-x86_64-gvanrossum-e6480f74cbec3ae4fb55-3.13.0a5+-e6480f7 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml      | 53.4 ms                                                | 54.8 ms: 1.03x slower                                                      |
| mako            | 10.7 ms                                                | 11.0 ms: 1.03x slower                                                      |
| django_template | 33.5 ms                                                | 36.2 ms: 1.08x slower                                                      |
| genshi_text     | 22.5 ms                                                | 24.7 ms: 1.10x slower                                                      |
| Geometric mean  | (ref)                                                  | 1.06x slower                                                               |

All benchmarks:
===============

| Benchmark                  | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240322-linux-x86_64-gvanrossum-e6480f74cbec3ae4fb55-3.13.0a5+-e6480f7 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols   | 520 us                                                 | 112 us: 4.62x faster                                                       |
| generators                 | 74.9 ms                                                | 29.5 ms: 2.53x faster                                                      |
| asyncio_tcp                | 875 ms                                                 | 509 ms: 1.72x faster                                                       |
| asyncio_tcp_ssl            | 3.11 sec                                               | 1.85 sec: 1.68x faster                                                     |
| pylint                     | 476 ms                                                 | 327 ms: 1.46x faster                                                       |
| comprehensions             | 23.6 us                                                | 17.9 us: 1.32x faster                                                      |
| json_dumps                 | 13.3 ms                                                | 10.5 ms: 1.27x faster                                                      |
| richards_super             | 61.9 ms                                                | 52.7 ms: 1.17x faster                                                      |
| async_tree_none            | 528 ms                                                 | 453 ms: 1.17x faster                                                       |
| coroutines                 | 27.0 ms                                                | 23.2 ms: 1.16x faster                                                      |
| deltablue                  | 3.92 ms                                                | 3.49 ms: 1.13x faster                                                      |
| chaos                      | 71.9 ms                                                | 63.9 ms: 1.12x faster                                                      |
| tomli_loads                | 2.30 sec                                               | 2.08 sec: 1.11x faster                                                     |
| async_tree_memoization     | 639 ms                                                 | 581 ms: 1.10x faster                                                       |
| richards                   | 49.8 ms                                                | 45.9 ms: 1.08x faster                                                      |
| sqlglot_parse              | 1.43 ms                                                | 1.32 ms: 1.08x faster                                                      |
| unpickle_list              | 5.21 us                                                | 4.85 us: 1.08x faster                                                      |
| logging_silent             | 111 ns                                                 | 103 ns: 1.07x faster                                                       |
| djangocms                  | 33.5 us                                                | 31.5 us: 1.06x faster                                                      |
| logging_simple             | 6.22 us                                                | 5.86 us: 1.06x faster                                                      |
| async_tree_none_tg         | 491 ms                                                 | 464 ms: 1.06x faster                                                       |
| sqlglot_transpile          | 1.75 ms                                                | 1.66 ms: 1.06x faster                                                      |
| pickle_pure_python         | 320 us                                                 | 304 us: 1.05x faster                                                       |
| mdp                        | 2.77 sec                                               | 2.64 sec: 1.05x faster                                                     |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.78 ms: 1.05x faster                                                      |
| async_tree_memoization_tg  | 626 ms                                                 | 596 ms: 1.05x faster                                                       |
| async_tree_io              | 1.29 sec                                               | 1.23 sec: 1.05x faster                                                     |
| raytrace                   | 309 ms                                                 | 294 ms: 1.05x faster                                                       |
| logging_format             | 6.81 us                                                | 6.53 us: 1.04x faster                                                      |
| json_loads                 | 29.2 us                                                | 28.0 us: 1.04x faster                                                      |
| async_tree_io_tg           | 1.29 sec                                               | 1.24 sec: 1.04x faster                                                     |
| nbody                      | 96.0 ms                                                | 92.9 ms: 1.03x faster                                                      |
| sympy_str                  | 297 ms                                                 | 288 ms: 1.03x faster                                                       |
| async_tree_cpu_io_mixed    | 749 ms                                                 | 728 ms: 1.03x faster                                                       |
| deepcopy                   | 365 us                                                 | 355 us: 1.03x faster                                                       |
| sympy_sum                  | 169 ms                                                 | 164 ms: 1.03x faster                                                       |
| xml_etree_parse            | 164 ms                                                 | 160 ms: 1.03x faster                                                       |
| async_tree_cpu_io_mixed_tg | 761 ms                                                 | 743 ms: 1.02x faster                                                       |
| pidigits                   | 194 ms                                                 | 190 ms: 1.02x faster                                                       |
| gc_traversal               | 4.01 ms                                                | 3.93 ms: 1.02x faster                                                      |
| deepcopy_reduce            | 3.22 us                                                | 3.15 us: 1.02x faster                                                      |
| crypto_pyaes               | 76.7 ms                                                | 75.3 ms: 1.02x faster                                                      |
| fannkuch                   | 405 ms                                                 | 399 ms: 1.02x faster                                                       |
| scimark_fft                | 345 ms                                                 | 341 ms: 1.01x faster                                                       |
| unpickle_pure_python       | 242 us                                                 | 239 us: 1.01x faster                                                       |
| deepcopy_memo              | 40.2 us                                                | 39.8 us: 1.01x faster                                                      |
| pprint_safe_repr           | 747 ms                                                 | 743 ms: 1.01x faster                                                       |
| xml_etree_iterparse        | 108 ms                                                 | 109 ms: 1.01x slower                                                       |
| meteor_contest             | 109 ms                                                 | 110 ms: 1.01x slower                                                       |
| sympy_integrate            | 21.5 ms                                                | 21.7 ms: 1.01x slower                                                      |
| pathlib                    | 18.5 ms                                                | 18.7 ms: 1.01x slower                                                      |
| sympy_expand               | 484 ms                                                 | 490 ms: 1.01x slower                                                       |
| tornado_http               | 98.1 ms                                                | 99.3 ms: 1.01x slower                                                      |
| json                       | 5.24 ms                                                | 5.31 ms: 1.01x slower                                                      |
| regex_compile              | 141 ms                                                 | 143 ms: 1.01x slower                                                       |
| hexiom                     | 6.89 ms                                                | 7.02 ms: 1.02x slower                                                      |
| bench_thread_pool          | 834 us                                                 | 850 us: 1.02x slower                                                       |
| float                      | 78.9 ms                                                | 80.6 ms: 1.02x slower                                                      |
| nqueens                    | 87.9 ms                                                | 89.8 ms: 1.02x slower                                                      |
| asyncio_websockets         | 550 ms                                                 | 563 ms: 1.02x slower                                                       |
| genshi_xml                 | 53.4 ms                                                | 54.8 ms: 1.03x slower                                                      |
| dask                       | 365 ms                                                 | 375 ms: 1.03x slower                                                       |
| pickle_dict                | 34.6 us                                                | 35.6 us: 1.03x slower                                                      |
| thrift                     | 784 us                                                 | 808 us: 1.03x slower                                                       |
| mako                       | 10.7 ms                                                | 11.0 ms: 1.03x slower                                                      |
| pycparser                  | 1.19 sec                                               | 1.23 sec: 1.04x slower                                                     |
| sqlglot_optimize           | 55.3 ms                                                | 57.7 ms: 1.04x slower                                                      |
| go                         | 149 ms                                                 | 155 ms: 1.04x slower                                                       |
| xml_etree_process          | 56.9 ms                                                | 59.6 ms: 1.05x slower                                                      |
| docutils                   | 2.66 sec                                               | 2.80 sec: 1.05x slower                                                     |
| html5lib                   | 64.8 ms                                                | 68.4 ms: 1.05x slower                                                      |
| chameleon                  | 6.70 ms                                                | 7.11 ms: 1.06x slower                                                      |
| 2to3                       | 264 ms                                                 | 280 ms: 1.06x slower                                                       |
| create_gc_cycles           | 1.43 ms                                                | 1.53 ms: 1.07x slower                                                      |
| spectral_norm              | 108 ms                                                 | 116 ms: 1.07x slower                                                       |
| django_template            | 33.5 ms                                                | 36.2 ms: 1.08x slower                                                      |
| scimark_sor                | 121 ms                                                 | 131 ms: 1.08x slower                                                       |
| xml_etree_generate         | 81.1 ms                                                | 87.4 ms: 1.08x slower                                                      |
| dulwich_log                | 64.6 ms                                                | 69.8 ms: 1.08x slower                                                      |
| pickle                     | 11.0 us                                                | 11.9 us: 1.08x slower                                                      |
| aiohttp                    | 1.12 ms                                                | 1.21 ms: 1.08x slower                                                      |
| unpickle                   | 13.8 us                                                | 15.1 us: 1.09x slower                                                      |
| gunicorn                   | 1.20 ms                                                | 1.31 ms: 1.09x slower                                                      |
| genshi_text                | 22.5 ms                                                | 24.7 ms: 1.10x slower                                                      |
| regex_effbot               | 3.51 ms                                                | 3.85 ms: 1.10x slower                                                      |
| regex_v8                   | 22.9 ms                                                | 25.1 ms: 1.10x slower                                                      |
| sqlite_synth               | 2.57 us                                                | 2.85 us: 1.11x slower                                                      |
| pyflate                    | 434 ms                                                 | 489 ms: 1.13x slower                                                       |
| scimark_lu                 | 116 ms                                                 | 131 ms: 1.13x slower                                                       |
| regex_dna                  | 205 ms                                                 | 233 ms: 1.14x slower                                                       |
| pickle_list                | 4.59 us                                                | 5.36 us: 1.17x slower                                                      |
| coverage                   | 78.8 ms                                                | 98.2 ms: 1.25x slower                                                      |
| telco                      | 6.86 ms                                                | 8.57 ms: 1.25x slower                                                      |
| async_generators           | 374 ms                                                 | 475 ms: 1.27x slower                                                       |
| mypy2                      | 686 ms                                                 | 905 ms: 1.32x slower                                                       |
| python_startup             | 8.56 ms                                                | 11.5 ms: 1.34x slower                                                      |
| python_startup_no_site     | 6.01 ms                                                | 10.1 ms: 1.68x slower                                                      |
| unpack_sequence            | 43.5 ns                                                | 89.0 ns: 2.05x slower                                                      |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                               |

Benchmark hidden because not significant (4): pprint_pformat, sqlglot_normalize, scimark_monte_carlo, bench_mp_pool
Ignored benchmarks (3) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative


# HPT report

- Reliability score: 65.26% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x


# Memory

- memory change: 1.13x