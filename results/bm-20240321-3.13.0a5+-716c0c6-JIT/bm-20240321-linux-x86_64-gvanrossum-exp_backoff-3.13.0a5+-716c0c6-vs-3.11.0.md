# Results vs. 3.11.0

- fork: gvanrossum
- ref: exp_backoff
- machine: linux-x86_64
- commit hash: 716c0c6
- commit date: 2024-03-21
- overall geometric mean: 1.21x slower
- HPT reliability: 99.99%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240321-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5+-716c0c6 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 264 ms                                                 | 304 ms: 1.15x slower                                              |
| chameleon      | 6.70 ms                                                | 6.98 ms: 1.04x slower                                             |
| docutils       | 2.66 sec                                               | 4.82 sec: 1.81x slower                                            |
| html5lib       | 64.8 ms                                                | 75.8 ms: 1.17x slower                                             |
| tornado_http   | 98.1 ms                                                | 101 ms: 1.03x slower                                              |
| Geometric mean | (ref)                                                  | 1.21x slower                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240321-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5+-716c0c6 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 749 ms                                                 | 4.17 sec: 5.57x slower                                            |
| async_tree_cpu_io_mixed_tg | 761 ms                                                 | 4.55 sec: 5.98x slower                                            |
| async_tree_none            | 528 ms                                                 | 3.39 sec: 6.41x slower                                            |
| async_tree_memoization     | 639 ms                                                 | 4.37 sec: 6.84x slower                                            |
| async_tree_memoization_tg  | 626 ms                                                 | 4.65 sec: 7.42x slower                                            |
| async_tree_none_tg         | 491 ms                                                 | 3.70 sec: 7.53x slower                                            |
| async_tree_io              | 1.29 sec                                               | 13.1 sec: 10.19x slower                                           |
| async_tree_io_tg           | 1.29 sec                                               | 13.9 sec: 10.74x slower                                           |
| Geometric mean             | (ref)                                                  | 7.39x slower                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240321-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5+-716c0c6 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| pidigits       | 194 ms                                                 | 190 ms: 1.02x faster                                              |
| nbody          | 96.0 ms                                                | 94.2 ms: 1.02x faster                                             |
| float          | 78.9 ms                                                | 143 ms: 1.81x slower                                              |
| Geometric mean | (ref)                                                  | 1.20x slower                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240321-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5+-716c0c6 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_compile  | 141 ms                                                 | 142 ms: 1.00x slower                                              |
| regex_v8       | 22.9 ms                                                | 24.2 ms: 1.06x slower                                             |
| regex_dna      | 205 ms                                                 | 218 ms: 1.06x slower                                              |
| regex_effbot   | 3.51 ms                                                | 3.81 ms: 1.09x slower                                             |
| Geometric mean | (ref)                                                  | 1.05x slower                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240321-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5+-716c0c6 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| json_dumps           | 13.3 ms                                                | 10.5 ms: 1.27x faster                                             |
| tomli_loads          | 2.30 sec                                               | 2.10 sec: 1.10x faster                                            |
| pickle_pure_python   | 320 us                                                 | 303 us: 1.06x faster                                              |
| json_loads           | 29.2 us                                                | 27.7 us: 1.05x faster                                             |
| unpickle_pure_python | 242 us                                                 | 241 us: 1.00x faster                                              |
| pickle_dict          | 34.6 us                                                | 34.5 us: 1.00x faster                                             |
| unpickle_list        | 5.21 us                                                | 5.27 us: 1.01x slower                                             |
| pickle_list          | 4.59 us                                                | 4.80 us: 1.05x slower                                             |
| pickle               | 11.0 us                                                | 11.6 us: 1.05x slower                                             |
| unpickle             | 13.8 us                                                | 15.5 us: 1.12x slower                                             |
| xml_etree_process    | 56.9 ms                                                | 68.8 ms: 1.21x slower                                             |
| xml_etree_generate   | 81.1 ms                                                | 99.6 ms: 1.23x slower                                             |
| xml_etree_parse      | 164 ms                                                 | 216 ms: 1.32x slower                                              |
| xml_etree_iterparse  | 108 ms                                                 | 163 ms: 1.51x slower                                              |
| Geometric mean       | (ref)                                                  | 1.06x slower                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240321-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5+-716c0c6 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 8.56 ms                                                | 11.8 ms: 1.38x slower                                             |
| python_startup_no_site | 6.01 ms                                                | 10.1 ms: 1.68x slower                                             |
| Geometric mean         | (ref)                                                  | 1.52x slower                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240321-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5+-716c0c6 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| mako            | 10.7 ms                                                | 11.1 ms: 1.05x slower                                             |
| django_template | 33.5 ms                                                | 36.0 ms: 1.07x slower                                             |
| genshi_text     | 22.5 ms                                                | 24.2 ms: 1.07x slower                                             |
| genshi_xml      | 53.4 ms                                                | 59.8 ms: 1.12x slower                                             |
| Geometric mean  | (ref)                                                  | 1.08x slower                                                      |

All benchmarks:
===============

| Benchmark                  | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240321-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5+-716c0c6 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| typing_runtime_protocols   | 520 us                                                 | 111 us: 4.67x faster                                              |
| generators                 | 74.9 ms                                                | 30.2 ms: 2.48x faster                                             |
| asyncio_tcp                | 875 ms                                                 | 509 ms: 1.72x faster                                              |
| asyncio_tcp_ssl            | 3.11 sec                                               | 1.85 sec: 1.68x faster                                            |
| comprehensions             | 23.6 us                                                | 17.6 us: 1.34x faster                                             |
| json_dumps                 | 13.3 ms                                                | 10.5 ms: 1.27x faster                                             |
| richards_super             | 61.9 ms                                                | 50.0 ms: 1.24x faster                                             |
| coroutines                 | 27.0 ms                                                | 23.0 ms: 1.17x faster                                             |
| richards                   | 49.8 ms                                                | 44.3 ms: 1.12x faster                                             |
| chaos                      | 71.9 ms                                                | 64.5 ms: 1.11x faster                                             |
| tomli_loads                | 2.30 sec                                               | 2.10 sec: 1.10x faster                                            |
| logging_silent             | 111 ns                                                 | 102 ns: 1.09x faster                                              |
| raytrace                   | 309 ms                                                 | 284 ms: 1.09x faster                                              |
| gc_traversal               | 4.01 ms                                                | 3.74 ms: 1.07x faster                                             |
| logging_simple             | 6.22 us                                                | 5.85 us: 1.06x faster                                             |
| pickle_pure_python         | 320 us                                                 | 303 us: 1.06x faster                                              |
| json_loads                 | 29.2 us                                                | 27.7 us: 1.05x faster                                             |
| logging_format             | 6.81 us                                                | 6.47 us: 1.05x faster                                             |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.79 ms: 1.05x faster                                             |
| sympy_str                  | 297 ms                                                 | 288 ms: 1.03x faster                                              |
| deepcopy_memo              | 40.2 us                                                | 39.0 us: 1.03x faster                                             |
| sympy_sum                  | 169 ms                                                 | 165 ms: 1.03x faster                                              |
| pidigits                   | 194 ms                                                 | 190 ms: 1.02x faster                                              |
| pprint_pformat             | 1.55 sec                                               | 1.52 sec: 1.02x faster                                            |
| deepcopy                   | 365 us                                                 | 358 us: 1.02x faster                                              |
| nbody                      | 96.0 ms                                                | 94.2 ms: 1.02x faster                                             |
| scimark_monte_carlo        | 70.7 ms                                                | 69.5 ms: 1.02x faster                                             |
| scimark_fft                | 345 ms                                                 | 341 ms: 1.01x faster                                              |
| deepcopy_reduce            | 3.22 us                                                | 3.18 us: 1.01x faster                                             |
| unpickle_pure_python       | 242 us                                                 | 241 us: 1.00x faster                                              |
| sympy_integrate            | 21.5 ms                                                | 21.4 ms: 1.00x faster                                             |
| pickle_dict                | 34.6 us                                                | 34.5 us: 1.00x faster                                             |
| regex_compile              | 141 ms                                                 | 142 ms: 1.00x slower                                              |
| fannkuch                   | 405 ms                                                 | 407 ms: 1.01x slower                                              |
| sqlglot_parse              | 1.43 ms                                                | 1.44 ms: 1.01x slower                                             |
| sqlglot_normalize          | 113 ms                                                 | 114 ms: 1.01x slower                                              |
| hexiom                     | 6.89 ms                                                | 6.96 ms: 1.01x slower                                             |
| unpickle_list              | 5.21 us                                                | 5.27 us: 1.01x slower                                             |
| sympy_expand               | 484 ms                                                 | 491 ms: 1.01x slower                                              |
| meteor_contest             | 109 ms                                                 | 111 ms: 1.01x slower                                              |
| bench_thread_pool          | 834 us                                                 | 847 us: 1.01x slower                                              |
| json                       | 5.24 ms                                                | 5.32 ms: 1.02x slower                                             |
| tornado_http               | 98.1 ms                                                | 101 ms: 1.03x slower                                              |
| sqlglot_transpile          | 1.75 ms                                                | 1.80 ms: 1.03x slower                                             |
| mdp                        | 2.77 sec                                               | 2.86 sec: 1.03x slower                                            |
| pathlib                    | 18.5 ms                                                | 19.1 ms: 1.03x slower                                             |
| asyncio_websockets         | 550 ms                                                 | 570 ms: 1.04x slower                                              |
| thrift                     | 784 us                                                 | 813 us: 1.04x slower                                              |
| create_gc_cycles           | 1.43 ms                                                | 1.49 ms: 1.04x slower                                             |
| chameleon                  | 6.70 ms                                                | 6.98 ms: 1.04x slower                                             |
| go                         | 149 ms                                                 | 155 ms: 1.04x slower                                              |
| mako                       | 10.7 ms                                                | 11.1 ms: 1.05x slower                                             |
| pickle_list                | 4.59 us                                                | 4.80 us: 1.05x slower                                             |
| pickle                     | 11.0 us                                                | 11.6 us: 1.05x slower                                             |
| regex_v8                   | 22.9 ms                                                | 24.2 ms: 1.06x slower                                             |
| sqlglot_optimize           | 55.3 ms                                                | 58.8 ms: 1.06x slower                                             |
| regex_dna                  | 205 ms                                                 | 218 ms: 1.06x slower                                              |
| spectral_norm              | 108 ms                                                 | 115 ms: 1.07x slower                                              |
| dulwich_log                | 64.6 ms                                                | 69.0 ms: 1.07x slower                                             |
| django_template            | 33.5 ms                                                | 36.0 ms: 1.07x slower                                             |
| genshi_text                | 22.5 ms                                                | 24.2 ms: 1.07x slower                                             |
| scimark_sor                | 121 ms                                                 | 131 ms: 1.08x slower                                              |
| regex_effbot               | 3.51 ms                                                | 3.81 ms: 1.09x slower                                             |
| scimark_lu                 | 116 ms                                                 | 129 ms: 1.11x slower                                              |
| sqlite_synth               | 2.57 us                                                | 2.86 us: 1.11x slower                                             |
| unpickle                   | 13.8 us                                                | 15.5 us: 1.12x slower                                             |
| genshi_xml                 | 53.4 ms                                                | 59.8 ms: 1.12x slower                                             |
| gunicorn                   | 1.20 ms                                                | 1.36 ms: 1.14x slower                                             |
| aiohttp                    | 1.12 ms                                                | 1.27 ms: 1.14x slower                                             |
| pyflate                    | 434 ms                                                 | 493 ms: 1.14x slower                                              |
| 2to3                       | 264 ms                                                 | 304 ms: 1.15x slower                                              |
| html5lib                   | 64.8 ms                                                | 75.8 ms: 1.17x slower                                             |
| xml_etree_process          | 56.9 ms                                                | 68.8 ms: 1.21x slower                                             |
| xml_etree_generate         | 81.1 ms                                                | 99.6 ms: 1.23x slower                                             |
| telco                      | 6.86 ms                                                | 8.43 ms: 1.23x slower                                             |
| coverage                   | 78.8 ms                                                | 96.9 ms: 1.23x slower                                             |
| pycparser                  | 1.19 sec                                               | 1.47 sec: 1.24x slower                                            |
| mypy2                      | 686 ms                                                 | 851 ms: 1.24x slower                                              |
| xml_etree_parse            | 164 ms                                                 | 216 ms: 1.32x slower                                              |
| python_startup             | 8.56 ms                                                | 11.8 ms: 1.38x slower                                             |
| async_generators           | 374 ms                                                 | 556 ms: 1.49x slower                                              |
| xml_etree_iterparse        | 108 ms                                                 | 163 ms: 1.51x slower                                              |
| python_startup_no_site     | 6.01 ms                                                | 10.1 ms: 1.68x slower                                             |
| float                      | 78.9 ms                                                | 143 ms: 1.81x slower                                              |
| docutils                   | 2.66 sec                                               | 4.82 sec: 1.81x slower                                            |
| dask                       | 365 ms                                                 | 759 ms: 2.08x slower                                              |
| unpack_sequence            | 43.5 ns                                                | 91.8 ns: 2.11x slower                                             |
| pylint                     | 476 ms                                                 | 1.01 sec: 2.12x slower                                            |
| async_tree_cpu_io_mixed    | 749 ms                                                 | 4.17 sec: 5.57x slower                                            |
| async_tree_cpu_io_mixed_tg | 761 ms                                                 | 4.55 sec: 5.98x slower                                            |
| async_tree_none            | 528 ms                                                 | 3.39 sec: 6.41x slower                                            |
| async_tree_memoization     | 639 ms                                                 | 4.37 sec: 6.84x slower                                            |
| async_tree_memoization_tg  | 626 ms                                                 | 4.65 sec: 7.42x slower                                            |
| async_tree_none_tg         | 491 ms                                                 | 3.70 sec: 7.53x slower                                            |
| async_tree_io              | 1.29 sec                                               | 13.1 sec: 10.19x slower                                           |
| async_tree_io_tg           | 1.29 sec                                               | 13.9 sec: 10.74x slower                                           |
| Geometric mean             | (ref)                                                  | 1.21x slower                                                      |

Benchmark hidden because not significant (6): deltablue, crypto_pyaes, bench_mp_pool, pprint_safe_repr, nqueens, djangocms
Ignored benchmarks (3) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative


# HPT report

- Reliability score: 99.99% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x


# Memory

- memory change: 1.12x