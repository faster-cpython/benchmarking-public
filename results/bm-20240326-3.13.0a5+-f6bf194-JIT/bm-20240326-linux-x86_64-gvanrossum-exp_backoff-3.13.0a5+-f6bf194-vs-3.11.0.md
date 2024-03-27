# Results vs. 3.11.0

- fork: gvanrossum
- ref: exp_backoff
- machine: linux-x86_64
- commit hash: f6bf194
- commit date: 2024-03-26
- overall geometric mean: 1.05x faster
- HPT reliability: 87.08%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240326-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5+-f6bf194 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 264 ms                                                 | 279 ms: 1.05x slower                                              |
| chameleon      | 6.70 ms                                                | 7.17 ms: 1.07x slower                                             |
| docutils       | 2.66 sec                                               | 2.84 sec: 1.07x slower                                            |
| html5lib       | 64.8 ms                                                | 66.2 ms: 1.02x slower                                             |
| tornado_http   | 98.1 ms                                                | 96.5 ms: 1.02x faster                                             |
| Geometric mean | (ref)                                                  | 1.04x slower                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240326-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5+-f6bf194 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_none_tg         | 491 ms                                                 | 341 ms: 1.44x faster                                              |
| async_tree_io_tg           | 1.29 sec                                               | 918 ms: 1.41x faster                                              |
| async_tree_io              | 1.29 sec                                               | 920 ms: 1.40x faster                                              |
| async_tree_memoization_tg  | 626 ms                                                 | 448 ms: 1.40x faster                                              |
| async_tree_memoization     | 639 ms                                                 | 459 ms: 1.39x faster                                              |
| async_tree_none            | 528 ms                                                 | 386 ms: 1.37x faster                                              |
| async_tree_cpu_io_mixed_tg | 761 ms                                                 | 583 ms: 1.31x faster                                              |
| async_tree_cpu_io_mixed    | 749 ms                                                 | 599 ms: 1.25x faster                                              |
| Geometric mean             | (ref)                                                  | 1.37x faster                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240326-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5+-f6bf194 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| nbody          | 96.0 ms                                                | 92.2 ms: 1.04x faster                                             |
| pidigits       | 194 ms                                                 | 189 ms: 1.03x faster                                              |
| float          | 78.9 ms                                                | 77.5 ms: 1.02x faster                                             |
| Geometric mean | (ref)                                                  | 1.03x faster                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240326-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5+-f6bf194 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_compile  | 141 ms                                                 | 139 ms: 1.02x faster                                              |
| regex_effbot   | 3.51 ms                                                | 3.77 ms: 1.08x slower                                             |
| regex_dna      | 205 ms                                                 | 227 ms: 1.11x slower                                              |
| regex_v8       | 22.9 ms                                                | 25.7 ms: 1.12x slower                                             |
| Geometric mean | (ref)                                                  | 1.07x slower                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240326-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5+-f6bf194 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| json_dumps           | 13.3 ms                                                | 10.6 ms: 1.26x faster                                             |
| tomli_loads          | 2.30 sec                                               | 2.06 sec: 1.12x faster                                            |
| pickle_pure_python   | 320 us                                                 | 305 us: 1.05x faster                                              |
| unpickle_pure_python | 242 us                                                 | 232 us: 1.04x faster                                              |
| pickle_dict          | 34.6 us                                                | 33.5 us: 1.03x faster                                             |
| xml_etree_parse      | 164 ms                                                 | 161 ms: 1.02x faster                                              |
| json_loads           | 29.2 us                                                | 28.7 us: 1.02x faster                                             |
| xml_etree_iterparse  | 108 ms                                                 | 107 ms: 1.01x faster                                              |
| unpickle_list        | 5.21 us                                                | 5.43 us: 1.04x slower                                             |
| xml_etree_process    | 56.9 ms                                                | 60.1 ms: 1.06x slower                                             |
| xml_etree_generate   | 81.1 ms                                                | 86.9 ms: 1.07x slower                                             |
| pickle_list          | 4.59 us                                                | 4.95 us: 1.08x slower                                             |
| pickle               | 11.0 us                                                | 12.0 us: 1.10x slower                                             |
| unpickle             | 13.8 us                                                | 17.0 us: 1.23x slower                                             |
| Geometric mean       | (ref)                                                  | 1.00x slower                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240326-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5+-f6bf194 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 8.56 ms                                                | 11.0 ms: 1.28x slower                                             |
| python_startup_no_site | 6.01 ms                                                | 9.48 ms: 1.58x slower                                             |
| Geometric mean         | (ref)                                                  | 1.42x slower                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240326-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5+-f6bf194 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| genshi_xml      | 53.4 ms                                                | 54.1 ms: 1.01x slower                                             |
| mako            | 10.7 ms                                                | 10.9 ms: 1.02x slower                                             |
| django_template | 33.5 ms                                                | 35.8 ms: 1.07x slower                                             |
| genshi_text     | 22.5 ms                                                | 25.2 ms: 1.12x slower                                             |
| Geometric mean  | (ref)                                                  | 1.05x slower                                                      |

All benchmarks:
===============

| Benchmark                  | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240326-linux-x86_64-gvanrossum-exp_backoff-3.13.0a5+-f6bf194 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| typing_runtime_protocols   | 520 us                                                 | 114 us: 4.56x faster                                              |
| generators                 | 74.9 ms                                                | 30.3 ms: 2.47x faster                                             |
| asyncio_tcp                | 875 ms                                                 | 506 ms: 1.73x faster                                              |
| asyncio_tcp_ssl            | 3.11 sec                                               | 1.85 sec: 1.68x faster                                            |
| async_tree_none_tg         | 491 ms                                                 | 341 ms: 1.44x faster                                              |
| pylint                     | 476 ms                                                 | 332 ms: 1.44x faster                                              |
| async_tree_io_tg           | 1.29 sec                                               | 918 ms: 1.41x faster                                              |
| async_tree_io              | 1.29 sec                                               | 920 ms: 1.40x faster                                              |
| async_tree_memoization_tg  | 626 ms                                                 | 448 ms: 1.40x faster                                              |
| async_tree_memoization     | 639 ms                                                 | 459 ms: 1.39x faster                                              |
| async_tree_none            | 528 ms                                                 | 386 ms: 1.37x faster                                              |
| comprehensions             | 23.6 us                                                | 18.0 us: 1.31x faster                                             |
| async_tree_cpu_io_mixed_tg | 761 ms                                                 | 583 ms: 1.31x faster                                              |
| json_dumps                 | 13.3 ms                                                | 10.6 ms: 1.26x faster                                             |
| async_tree_cpu_io_mixed    | 749 ms                                                 | 599 ms: 1.25x faster                                              |
| richards_super             | 61.9 ms                                                | 50.7 ms: 1.22x faster                                             |
| deltablue                  | 3.92 ms                                                | 3.32 ms: 1.18x faster                                             |
| coroutines                 | 27.0 ms                                                | 23.6 ms: 1.14x faster                                             |
| chaos                      | 71.9 ms                                                | 63.3 ms: 1.14x faster                                             |
| richards                   | 49.8 ms                                                | 44.1 ms: 1.13x faster                                             |
| raytrace                   | 309 ms                                                 | 275 ms: 1.12x faster                                              |
| tomli_loads                | 2.30 sec                                               | 2.06 sec: 1.12x faster                                            |
| sqlglot_parse              | 1.43 ms                                                | 1.33 ms: 1.08x faster                                             |
| sqlglot_transpile          | 1.75 ms                                                | 1.65 ms: 1.06x faster                                             |
| logging_silent             | 111 ns                                                 | 105 ns: 1.06x faster                                              |
| pickle_pure_python         | 320 us                                                 | 305 us: 1.05x faster                                              |
| mdp                        | 2.77 sec                                               | 2.66 sec: 1.04x faster                                            |
| unpickle_pure_python       | 242 us                                                 | 232 us: 1.04x faster                                              |
| djangocms                  | 33.5 us                                                | 32.2 us: 1.04x faster                                             |
| nbody                      | 96.0 ms                                                | 92.2 ms: 1.04x faster                                             |
| gc_traversal               | 4.01 ms                                                | 3.86 ms: 1.04x faster                                             |
| sympy_sum                  | 169 ms                                                 | 163 ms: 1.04x faster                                              |
| logging_simple             | 6.22 us                                                | 6.02 us: 1.03x faster                                             |
| pickle_dict                | 34.6 us                                                | 33.5 us: 1.03x faster                                             |
| sympy_str                  | 297 ms                                                 | 289 ms: 1.03x faster                                              |
| deepcopy_memo              | 40.2 us                                                | 39.0 us: 1.03x faster                                             |
| pidigits                   | 194 ms                                                 | 189 ms: 1.03x faster                                              |
| logging_format             | 6.81 us                                                | 6.66 us: 1.02x faster                                             |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.93 ms: 1.02x faster                                             |
| deepcopy_reduce            | 3.22 us                                                | 3.15 us: 1.02x faster                                             |
| float                      | 78.9 ms                                                | 77.5 ms: 1.02x faster                                             |
| regex_compile              | 141 ms                                                 | 139 ms: 1.02x faster                                              |
| xml_etree_parse            | 164 ms                                                 | 161 ms: 1.02x faster                                              |
| deepcopy                   | 365 us                                                 | 359 us: 1.02x faster                                              |
| crypto_pyaes               | 76.7 ms                                                | 75.5 ms: 1.02x faster                                             |
| tornado_http               | 98.1 ms                                                | 96.5 ms: 1.02x faster                                             |
| json_loads                 | 29.2 us                                                | 28.7 us: 1.02x faster                                             |
| scimark_lu                 | 116 ms                                                 | 115 ms: 1.01x faster                                              |
| fannkuch                   | 405 ms                                                 | 401 ms: 1.01x faster                                              |
| xml_etree_iterparse        | 108 ms                                                 | 107 ms: 1.01x faster                                              |
| sympy_integrate            | 21.5 ms                                                | 21.3 ms: 1.01x faster                                             |
| go                         | 149 ms                                                 | 148 ms: 1.01x faster                                              |
| scimark_fft                | 345 ms                                                 | 344 ms: 1.00x faster                                              |
| sqlglot_normalize          | 113 ms                                                 | 112 ms: 1.00x faster                                              |
| hexiom                     | 6.89 ms                                                | 6.87 ms: 1.00x faster                                             |
| pprint_pformat             | 1.55 sec                                               | 1.57 sec: 1.01x slower                                            |
| genshi_xml                 | 53.4 ms                                                | 54.1 ms: 1.01x slower                                             |
| sympy_expand               | 484 ms                                                 | 491 ms: 1.01x slower                                              |
| pprint_safe_repr           | 747 ms                                                 | 762 ms: 1.02x slower                                              |
| mako                       | 10.7 ms                                                | 10.9 ms: 1.02x slower                                             |
| bench_thread_pool          | 834 us                                                 | 852 us: 1.02x slower                                              |
| pathlib                    | 18.5 ms                                                | 18.9 ms: 1.02x slower                                             |
| html5lib                   | 64.8 ms                                                | 66.2 ms: 1.02x slower                                             |
| meteor_contest             | 109 ms                                                 | 111 ms: 1.02x slower                                              |
| scimark_sor                | 121 ms                                                 | 124 ms: 1.03x slower                                              |
| sqlglot_optimize           | 55.3 ms                                                | 56.7 ms: 1.03x slower                                             |
| dask                       | 365 ms                                                 | 376 ms: 1.03x slower                                              |
| json                       | 5.24 ms                                                | 5.42 ms: 1.03x slower                                             |
| asyncio_websockets         | 550 ms                                                 | 570 ms: 1.04x slower                                              |
| unpickle_list              | 5.21 us                                                | 5.43 us: 1.04x slower                                             |
| pycparser                  | 1.19 sec                                               | 1.24 sec: 1.05x slower                                            |
| 2to3                       | 264 ms                                                 | 279 ms: 1.05x slower                                              |
| xml_etree_process          | 56.9 ms                                                | 60.1 ms: 1.06x slower                                             |
| dulwich_log                | 64.6 ms                                                | 68.6 ms: 1.06x slower                                             |
| docutils                   | 2.66 sec                                               | 2.84 sec: 1.07x slower                                            |
| django_template            | 33.5 ms                                                | 35.8 ms: 1.07x slower                                             |
| chameleon                  | 6.70 ms                                                | 7.17 ms: 1.07x slower                                             |
| xml_etree_generate         | 81.1 ms                                                | 86.9 ms: 1.07x slower                                             |
| spectral_norm              | 108 ms                                                 | 116 ms: 1.07x slower                                              |
| regex_effbot               | 3.51 ms                                                | 3.77 ms: 1.08x slower                                             |
| pickle_list                | 4.59 us                                                | 4.95 us: 1.08x slower                                             |
| aiohttp                    | 1.12 ms                                                | 1.21 ms: 1.09x slower                                             |
| gunicorn                   | 1.20 ms                                                | 1.30 ms: 1.09x slower                                             |
| thrift                     | 784 us                                                 | 858 us: 1.09x slower                                              |
| pickle                     | 11.0 us                                                | 12.0 us: 1.10x slower                                             |
| regex_dna                  | 205 ms                                                 | 227 ms: 1.11x slower                                              |
| mypy2                      | 686 ms                                                 | 766 ms: 1.12x slower                                              |
| genshi_text                | 22.5 ms                                                | 25.2 ms: 1.12x slower                                             |
| pyflate                    | 434 ms                                                 | 486 ms: 1.12x slower                                              |
| regex_v8                   | 22.9 ms                                                | 25.7 ms: 1.12x slower                                             |
| sqlite_synth               | 2.57 us                                                | 2.89 us: 1.12x slower                                             |
| create_gc_cycles           | 1.43 ms                                                | 1.69 ms: 1.18x slower                                             |
| unpack_sequence            | 43.5 ns                                                | 51.5 ns: 1.19x slower                                             |
| unpickle                   | 13.8 us                                                | 17.0 us: 1.23x slower                                             |
| async_generators           | 374 ms                                                 | 468 ms: 1.25x slower                                              |
| telco                      | 6.86 ms                                                | 8.58 ms: 1.25x slower                                             |
| coverage                   | 78.8 ms                                                | 100 ms: 1.27x slower                                              |
| python_startup             | 8.56 ms                                                | 11.0 ms: 1.28x slower                                             |
| python_startup_no_site     | 6.01 ms                                                | 9.48 ms: 1.58x slower                                             |
| Geometric mean             | (ref)                                                  | 1.05x faster                                                      |

Benchmark hidden because not significant (3): nqueens, bench_mp_pool, scimark_monte_carlo
Ignored benchmarks (3) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative


# HPT report

- Reliability score: 87.08% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x


# Memory

- memory change: 1.08x