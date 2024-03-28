# Results vs. 3.11.0

- fork: gvanrossum
- ref: exp_backoff
- machine: linux-x86_64
- commit hash: 225ea17
- commit date: 2024-03-27
- overall geometric mean: 1.03x faster
- HPT reliability: 54.72%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240327-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5+-225ea17 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 264 ms                                                 | 279 ms: 1.06x slower                                              |
| chameleon      | 6.70 ms                                                | 7.21 ms: 1.08x slower                                             |
| docutils       | 2.66 sec                                               | 2.89 sec: 1.09x slower                                            |
| html5lib       | 64.8 ms                                                | 66.2 ms: 1.02x slower                                             |
| tornado_http   | 98.1 ms                                                | 96.6 ms: 1.01x faster                                             |
| Geometric mean | (ref)                                                  | 1.04x slower                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240327-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5+-225ea17 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_none_tg         | 491 ms                                                 | 341 ms: 1.44x faster                                              |
| async_tree_io_tg           | 1.29 sec                                               | 923 ms: 1.40x faster                                              |
| async_tree_memoization     | 639 ms                                                 | 459 ms: 1.39x faster                                              |
| async_tree_memoization_tg  | 626 ms                                                 | 451 ms: 1.39x faster                                              |
| async_tree_io              | 1.29 sec                                               | 942 ms: 1.37x faster                                              |
| async_tree_none            | 528 ms                                                 | 390 ms: 1.35x faster                                              |
| async_tree_cpu_io_mixed_tg | 761 ms                                                 | 583 ms: 1.31x faster                                              |
| async_tree_cpu_io_mixed    | 749 ms                                                 | 601 ms: 1.25x faster                                              |
| Geometric mean             | (ref)                                                  | 1.36x faster                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240327-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5+-225ea17 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| nbody          | 96.0 ms                                                | 91.9 ms: 1.04x faster                                             |
| pidigits       | 194 ms                                                 | 189 ms: 1.03x faster                                              |
| float          | 78.9 ms                                                | 77.8 ms: 1.01x faster                                             |
| Geometric mean | (ref)                                                  | 1.03x faster                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240327-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5+-225ea17 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_compile  | 141 ms                                                 | 146 ms: 1.03x slower                                              |
| regex_effbot   | 3.51 ms                                                | 3.81 ms: 1.09x slower                                             |
| regex_dna      | 205 ms                                                 | 229 ms: 1.12x slower                                              |
| regex_v8       | 22.9 ms                                                | 26.1 ms: 1.14x slower                                             |
| Geometric mean | (ref)                                                  | 1.09x slower                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240327-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5+-225ea17 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| json_dumps           | 13.3 ms                                                | 10.6 ms: 1.26x faster                                             |
| tomli_loads          | 2.30 sec                                               | 2.07 sec: 1.12x faster                                            |
| pickle_pure_python   | 320 us                                                 | 308 us: 1.04x faster                                              |
| xml_etree_parse      | 164 ms                                                 | 162 ms: 1.01x faster                                              |
| unpickle_list        | 5.21 us                                                | 5.24 us: 1.00x slower                                             |
| unpickle_pure_python | 242 us                                                 | 246 us: 1.02x slower                                              |
| xml_etree_process    | 56.9 ms                                                | 60.5 ms: 1.06x slower                                             |
| pickle_dict          | 34.6 us                                                | 37.2 us: 1.07x slower                                             |
| xml_etree_generate   | 81.1 ms                                                | 88.6 ms: 1.09x slower                                             |
| pickle               | 11.0 us                                                | 12.3 us: 1.12x slower                                             |
| pickle_list          | 4.59 us                                                | 5.30 us: 1.16x slower                                             |
| unpickle             | 13.8 us                                                | 16.4 us: 1.19x slower                                             |
| Geometric mean       | (ref)                                                  | 1.02x slower                                                      |

Benchmark hidden because not significant (2): json_loads, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240327-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5+-225ea17 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 8.56 ms                                                | 11.1 ms: 1.29x slower                                             |
| python_startup_no_site | 6.01 ms                                                | 9.55 ms: 1.59x slower                                             |
| Geometric mean         | (ref)                                                  | 1.43x slower                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240327-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5+-225ea17 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| mako            | 10.7 ms                                                | 10.8 ms: 1.01x slower                                             |
| django_template | 33.5 ms                                                | 35.9 ms: 1.07x slower                                             |
| genshi_text     | 22.5 ms                                                | 24.5 ms: 1.09x slower                                             |
| Geometric mean  | (ref)                                                  | 1.04x slower                                                      |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240327-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5+-225ea17 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| typing_runtime_protocols   | 520 us                                                 | 115 us: 4.52x faster                                              |
| generators                 | 74.9 ms                                                | 30.2 ms: 2.48x faster                                             |
| asyncio_tcp                | 875 ms                                                 | 508 ms: 1.72x faster                                              |
| asyncio_tcp_ssl            | 3.11 sec                                               | 1.85 sec: 1.68x faster                                            |
| async_tree_none_tg         | 491 ms                                                 | 341 ms: 1.44x faster                                              |
| pylint                     | 476 ms                                                 | 337 ms: 1.41x faster                                              |
| async_tree_io_tg           | 1.29 sec                                               | 923 ms: 1.40x faster                                              |
| async_tree_memoization     | 639 ms                                                 | 459 ms: 1.39x faster                                              |
| async_tree_memoization_tg  | 626 ms                                                 | 451 ms: 1.39x faster                                              |
| async_tree_io              | 1.29 sec                                               | 942 ms: 1.37x faster                                              |
| async_tree_none            | 528 ms                                                 | 390 ms: 1.35x faster                                              |
| async_tree_cpu_io_mixed_tg | 761 ms                                                 | 583 ms: 1.31x faster                                              |
| comprehensions             | 23.6 us                                                | 18.2 us: 1.30x faster                                             |
| json_dumps                 | 13.3 ms                                                | 10.6 ms: 1.26x faster                                             |
| async_tree_cpu_io_mixed    | 749 ms                                                 | 601 ms: 1.25x faster                                              |
| richards_super             | 61.9 ms                                                | 52.8 ms: 1.17x faster                                             |
| coroutines                 | 27.0 ms                                                | 23.2 ms: 1.17x faster                                             |
| chaos                      | 71.9 ms                                                | 63.3 ms: 1.14x faster                                             |
| tomli_loads                | 2.30 sec                                               | 2.07 sec: 1.12x faster                                            |
| sqlglot_parse              | 1.43 ms                                                | 1.34 ms: 1.07x faster                                             |
| richards                   | 49.8 ms                                                | 47.0 ms: 1.06x faster                                             |
| raytrace                   | 309 ms                                                 | 293 ms: 1.05x faster                                              |
| logging_silent             | 111 ns                                                 | 105 ns: 1.05x faster                                              |
| sqlglot_transpile          | 1.75 ms                                                | 1.66 ms: 1.05x faster                                             |
| mdp                        | 2.77 sec                                               | 2.65 sec: 1.05x faster                                            |
| nbody                      | 96.0 ms                                                | 91.9 ms: 1.04x faster                                             |
| fannkuch                   | 405 ms                                                 | 389 ms: 1.04x faster                                              |
| logging_simple             | 6.22 us                                                | 5.98 us: 1.04x faster                                             |
| pickle_pure_python         | 320 us                                                 | 308 us: 1.04x faster                                              |
| djangocms                  | 33.5 us                                                | 32.4 us: 1.03x faster                                             |
| pidigits                   | 194 ms                                                 | 189 ms: 1.03x faster                                              |
| crypto_pyaes               | 76.7 ms                                                | 74.9 ms: 1.02x faster                                             |
| deepcopy                   | 365 us                                                 | 356 us: 1.02x faster                                              |
| deepcopy_memo              | 40.2 us                                                | 39.3 us: 1.02x faster                                             |
| logging_format             | 6.81 us                                                | 6.68 us: 1.02x faster                                             |
| gc_traversal               | 4.01 ms                                                | 3.95 ms: 1.02x faster                                             |
| tornado_http               | 98.1 ms                                                | 96.6 ms: 1.01x faster                                             |
| float                      | 78.9 ms                                                | 77.8 ms: 1.01x faster                                             |
| sympy_str                  | 297 ms                                                 | 293 ms: 1.01x faster                                              |
| xml_etree_parse            | 164 ms                                                 | 162 ms: 1.01x faster                                              |
| sympy_sum                  | 169 ms                                                 | 167 ms: 1.01x faster                                              |
| pprint_pformat             | 1.55 sec                                               | 1.54 sec: 1.01x faster                                            |
| unpickle_list              | 5.21 us                                                | 5.24 us: 1.00x slower                                             |
| scimark_fft                | 345 ms                                                 | 348 ms: 1.01x slower                                              |
| mako                       | 10.7 ms                                                | 10.8 ms: 1.01x slower                                             |
| nqueens                    | 87.9 ms                                                | 88.7 ms: 1.01x slower                                             |
| scimark_monte_carlo        | 70.7 ms                                                | 71.6 ms: 1.01x slower                                             |
| unpickle_pure_python       | 242 us                                                 | 246 us: 1.02x slower                                              |
| meteor_contest             | 109 ms                                                 | 111 ms: 1.02x slower                                              |
| sympy_integrate            | 21.5 ms                                                | 21.9 ms: 1.02x slower                                             |
| html5lib                   | 64.8 ms                                                | 66.2 ms: 1.02x slower                                             |
| bench_thread_pool          | 834 us                                                 | 856 us: 1.03x slower                                              |
| sympy_expand               | 484 ms                                                 | 497 ms: 1.03x slower                                              |
| pathlib                    | 18.5 ms                                                | 19.0 ms: 1.03x slower                                             |
| dask                       | 365 ms                                                 | 375 ms: 1.03x slower                                              |
| regex_compile              | 141 ms                                                 | 146 ms: 1.03x slower                                              |
| hexiom                     | 6.89 ms                                                | 7.12 ms: 1.03x slower                                             |
| go                         | 149 ms                                                 | 154 ms: 1.03x slower                                              |
| asyncio_websockets         | 550 ms                                                 | 570 ms: 1.04x slower                                              |
| sqlglot_optimize           | 55.3 ms                                                | 58.0 ms: 1.05x slower                                             |
| json                       | 5.24 ms                                                | 5.50 ms: 1.05x slower                                             |
| thrift                     | 784 us                                                 | 823 us: 1.05x slower                                              |
| pycparser                  | 1.19 sec                                               | 1.25 sec: 1.05x slower                                            |
| 2to3                       | 264 ms                                                 | 279 ms: 1.06x slower                                              |
| xml_etree_process          | 56.9 ms                                                | 60.5 ms: 1.06x slower                                             |
| django_template            | 33.5 ms                                                | 35.9 ms: 1.07x slower                                             |
| pickle_dict                | 34.6 us                                                | 37.2 us: 1.07x slower                                             |
| chameleon                  | 6.70 ms                                                | 7.21 ms: 1.08x slower                                             |
| spectral_norm              | 108 ms                                                 | 117 ms: 1.08x slower                                              |
| regex_effbot               | 3.51 ms                                                | 3.81 ms: 1.09x slower                                             |
| genshi_text                | 22.5 ms                                                | 24.5 ms: 1.09x slower                                             |
| docutils                   | 2.66 sec                                               | 2.89 sec: 1.09x slower                                            |
| aiohttp                    | 1.12 ms                                                | 1.21 ms: 1.09x slower                                             |
| xml_etree_generate         | 81.1 ms                                                | 88.6 ms: 1.09x slower                                             |
| gunicorn                   | 1.20 ms                                                | 1.31 ms: 1.09x slower                                             |
| dulwich_log                | 64.6 ms                                                | 70.8 ms: 1.10x slower                                             |
| scimark_sor                | 121 ms                                                 | 134 ms: 1.10x slower                                              |
| sqlite_synth               | 2.57 us                                                | 2.87 us: 1.12x slower                                             |
| pyflate                    | 434 ms                                                 | 485 ms: 1.12x slower                                              |
| regex_dna                  | 205 ms                                                 | 229 ms: 1.12x slower                                              |
| pickle                     | 11.0 us                                                | 12.3 us: 1.12x slower                                             |
| regex_v8                   | 22.9 ms                                                | 26.1 ms: 1.14x slower                                             |
| mypy2                      | 686 ms                                                 | 785 ms: 1.14x slower                                              |
| scimark_lu                 | 116 ms                                                 | 134 ms: 1.15x slower                                              |
| pickle_list                | 4.59 us                                                | 5.30 us: 1.16x slower                                             |
| create_gc_cycles           | 1.43 ms                                                | 1.70 ms: 1.18x slower                                             |
| unpickle                   | 13.8 us                                                | 16.4 us: 1.19x slower                                             |
| coverage                   | 78.8 ms                                                | 97.9 ms: 1.24x slower                                             |
| async_generators           | 374 ms                                                 | 467 ms: 1.25x slower                                              |
| telco                      | 6.86 ms                                                | 8.82 ms: 1.29x slower                                             |
| python_startup             | 8.56 ms                                                | 11.1 ms: 1.29x slower                                             |
| python_startup_no_site     | 6.01 ms                                                | 9.55 ms: 1.59x slower                                             |
| unpack_sequence            | 43.5 ns                                                | 86.4 ns: 1.99x slower                                             |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                      |

Benchmark hidden because not significant (9): scimark_sparse_mat_mult, json_loads, sqlglot_normalize, deepcopy_reduce, pprint_safe_repr, genshi_xml, xml_etree_iterparse, bench_mp_pool, deltablue
Ignored benchmarks (3) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative


# HPT report

- Reliability score: 54.72% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x


# Memory

- memory change: 1.09x