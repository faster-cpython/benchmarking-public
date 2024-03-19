# Results vs. 3.11.0

- fork: faster-cpython
- ref: exponential_backoff_
- machine: linux-x86_64
- commit hash: bdf272d
- commit date: 2024-03-19
- overall geometric mean: 1.04x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240319-linux-x86_64-faster%2dcpython-exponential_backoff_-3.13.0a5+-bdf272d |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 264 ms                                                 | 300 ms: 1.13x slower                                                             |
| chameleon      | 6.70 ms                                                | 7.14 ms: 1.07x slower                                                            |
| docutils       | 2.66 sec                                               | 2.86 sec: 1.08x slower                                                           |
| html5lib       | 64.8 ms                                                | 69.7 ms: 1.07x slower                                                            |
| tornado_http   | 98.1 ms                                                | 103 ms: 1.05x slower                                                             |
| Geometric mean | (ref)                                                  | 1.08x slower                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240319-linux-x86_64-faster%2dcpython-exponential_backoff_-3.13.0a5+-bdf272d |
|---------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_none           | 528 ms                                                 | 465 ms: 1.14x faster                                                             |
| async_tree_memoization    | 639 ms                                                 | 596 ms: 1.07x faster                                                             |
| async_tree_io             | 1.29 sec                                               | 1.23 sec: 1.05x faster                                                           |
| async_tree_memoization_tg | 626 ms                                                 | 599 ms: 1.05x faster                                                             |
| async_tree_none_tg        | 491 ms                                                 | 472 ms: 1.04x faster                                                             |
| async_tree_io_tg          | 1.29 sec                                               | 1.25 sec: 1.03x faster                                                           |
| Geometric mean            | (ref)                                                  | 1.05x faster                                                                     |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240319-linux-x86_64-faster%2dcpython-exponential_backoff_-3.13.0a5+-bdf272d |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 194 ms                                                 | 191 ms: 1.02x faster                                                             |
| float          | 78.9 ms                                                | 93.9 ms: 1.19x slower                                                            |
| nbody          | 96.0 ms                                                | 121 ms: 1.26x slower                                                             |
| Geometric mean | (ref)                                                  | 1.14x slower                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240319-linux-x86_64-faster%2dcpython-exponential_backoff_-3.13.0a5+-bdf272d |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_effbot   | 3.51 ms                                                | 3.56 ms: 1.01x slower                                                            |
| regex_v8       | 22.9 ms                                                | 24.5 ms: 1.07x slower                                                            |
| regex_dna      | 205 ms                                                 | 219 ms: 1.07x slower                                                             |
| regex_compile  | 141 ms                                                 | 175 ms: 1.24x slower                                                             |
| Geometric mean | (ref)                                                  | 1.09x slower                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240319-linux-x86_64-faster%2dcpython-exponential_backoff_-3.13.0a5+-bdf272d |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_dumps           | 13.3 ms                                                | 10.7 ms: 1.25x faster                                                            |
| unpickle_list        | 5.21 us                                                | 4.94 us: 1.06x faster                                                            |
| json_loads           | 29.2 us                                                | 28.3 us: 1.03x faster                                                            |
| pickle_dict          | 34.6 us                                                | 33.6 us: 1.03x faster                                                            |
| pickle_pure_python   | 320 us                                                 | 313 us: 1.02x faster                                                             |
| xml_etree_iterparse  | 108 ms                                                 | 113 ms: 1.05x slower                                                             |
| pickle               | 11.0 us                                                | 11.7 us: 1.06x slower                                                            |
| tomli_loads          | 2.30 sec                                               | 2.46 sec: 1.07x slower                                                           |
| pickle_list          | 4.59 us                                                | 5.02 us: 1.09x slower                                                            |
| xml_etree_process    | 56.9 ms                                                | 63.6 ms: 1.12x slower                                                            |
| unpickle             | 13.8 us                                                | 15.8 us: 1.14x slower                                                            |
| xml_etree_generate   | 81.1 ms                                                | 92.5 ms: 1.14x slower                                                            |
| unpickle_pure_python | 242 us                                                 | 277 us: 1.15x slower                                                             |
| Geometric mean       | (ref)                                                  | 1.03x slower                                                                     |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240319-linux-x86_64-faster%2dcpython-exponential_backoff_-3.13.0a5+-bdf272d |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 8.56 ms                                                | 10.5 ms: 1.22x slower                                                            |
| python_startup_no_site | 6.01 ms                                                | 9.07 ms: 1.51x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.36x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240319-linux-x86_64-faster%2dcpython-exponential_backoff_-3.13.0a5+-bdf272d |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| django_template | 33.5 ms                                                | 35.0 ms: 1.04x slower                                                            |
| genshi_xml      | 53.4 ms                                                | 62.4 ms: 1.17x slower                                                            |
| genshi_text     | 22.5 ms                                                | 27.7 ms: 1.23x slower                                                            |
| mako            | 10.7 ms                                                | 13.2 ms: 1.24x slower                                                            |
| Geometric mean  | (ref)                                                  | 1.17x slower                                                                     |

All benchmarks:
===============

| Benchmark                 | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240319-linux-x86_64-faster%2dcpython-exponential_backoff_-3.13.0a5+-bdf272d |
|---------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| typing_runtime_protocols  | 520 us                                                 | 115 us: 4.51x faster                                                             |
| generators                | 74.9 ms                                                | 29.8 ms: 2.51x faster                                                            |
| asyncio_tcp               | 875 ms                                                 | 508 ms: 1.72x faster                                                             |
| asyncio_tcp_ssl           | 3.11 sec                                               | 1.85 sec: 1.68x faster                                                           |
| pylint                    | 476 ms                                                 | 329 ms: 1.45x faster                                                             |
| json_dumps                | 13.3 ms                                                | 10.7 ms: 1.25x faster                                                            |
| coroutines                | 27.0 ms                                                | 22.9 ms: 1.18x faster                                                            |
| async_tree_none           | 528 ms                                                 | 465 ms: 1.14x faster                                                             |
| comprehensions            | 23.6 us                                                | 21.3 us: 1.11x faster                                                            |
| async_tree_memoization    | 639 ms                                                 | 596 ms: 1.07x faster                                                             |
| logging_silent            | 111 ns                                                 | 105 ns: 1.06x faster                                                             |
| unpickle_list             | 5.21 us                                                | 4.94 us: 1.06x faster                                                            |
| async_tree_io             | 1.29 sec                                               | 1.23 sec: 1.05x faster                                                           |
| async_tree_memoization_tg | 626 ms                                                 | 599 ms: 1.05x faster                                                             |
| djangocms                 | 33.5 us                                                | 32.2 us: 1.04x faster                                                            |
| async_tree_none_tg        | 491 ms                                                 | 472 ms: 1.04x faster                                                             |
| async_tree_io_tg          | 1.29 sec                                               | 1.25 sec: 1.03x faster                                                           |
| json_loads                | 29.2 us                                                | 28.3 us: 1.03x faster                                                            |
| mdp                       | 2.77 sec                                               | 2.70 sec: 1.03x faster                                                           |
| pickle_dict               | 34.6 us                                                | 33.6 us: 1.03x faster                                                            |
| deltablue                 | 3.92 ms                                                | 3.83 ms: 1.03x faster                                                            |
| gc_traversal              | 4.01 ms                                                | 3.91 ms: 1.02x faster                                                            |
| pickle_pure_python        | 320 us                                                 | 313 us: 1.02x faster                                                             |
| pidigits                  | 194 ms                                                 | 191 ms: 1.02x faster                                                             |
| sympy_sum                 | 169 ms                                                 | 168 ms: 1.01x faster                                                             |
| deepcopy_reduce           | 3.22 us                                                | 3.20 us: 1.01x faster                                                            |
| sympy_integrate           | 21.5 ms                                                | 21.5 ms: 1.00x slower                                                            |
| deepcopy                  | 365 us                                                 | 368 us: 1.01x slower                                                             |
| richards_super            | 61.9 ms                                                | 62.3 ms: 1.01x slower                                                            |
| json                      | 5.24 ms                                                | 5.29 ms: 1.01x slower                                                            |
| sqlglot_normalize         | 113 ms                                                 | 114 ms: 1.01x slower                                                             |
| regex_effbot              | 3.51 ms                                                | 3.56 ms: 1.01x slower                                                            |
| sqlglot_transpile         | 1.75 ms                                                | 1.79 ms: 1.02x slower                                                            |
| sympy_str                 | 297 ms                                                 | 304 ms: 1.02x slower                                                             |
| asyncio_websockets        | 550 ms                                                 | 564 ms: 1.02x slower                                                             |
| logging_simple            | 6.22 us                                                | 6.38 us: 1.03x slower                                                            |
| dask                      | 365 ms                                                 | 377 ms: 1.03x slower                                                             |
| bench_thread_pool         | 834 us                                                 | 867 us: 1.04x slower                                                             |
| logging_format            | 6.81 us                                                | 7.08 us: 1.04x slower                                                            |
| django_template           | 33.5 ms                                                | 35.0 ms: 1.04x slower                                                            |
| xml_etree_iterparse       | 108 ms                                                 | 113 ms: 1.05x slower                                                             |
| tornado_http              | 98.1 ms                                                | 103 ms: 1.05x slower                                                             |
| thrift                    | 784 us                                                 | 825 us: 1.05x slower                                                             |
| chaos                     | 71.9 ms                                                | 76.1 ms: 1.06x slower                                                            |
| pickle                    | 11.0 us                                                | 11.7 us: 1.06x slower                                                            |
| pathlib                   | 18.5 ms                                                | 19.7 ms: 1.06x slower                                                            |
| sympy_expand              | 484 ms                                                 | 516 ms: 1.06x slower                                                             |
| chameleon                 | 6.70 ms                                                | 7.14 ms: 1.07x slower                                                            |
| tomli_loads               | 2.30 sec                                               | 2.46 sec: 1.07x slower                                                           |
| regex_v8                  | 22.9 ms                                                | 24.5 ms: 1.07x slower                                                            |
| regex_dna                 | 205 ms                                                 | 219 ms: 1.07x slower                                                             |
| html5lib                  | 64.8 ms                                                | 69.7 ms: 1.07x slower                                                            |
| deepcopy_memo             | 40.2 us                                                | 43.2 us: 1.07x slower                                                            |
| create_gc_cycles          | 1.43 ms                                                | 1.54 ms: 1.08x slower                                                            |
| docutils                  | 2.66 sec                                               | 2.86 sec: 1.08x slower                                                           |
| aiohttp                   | 1.12 ms                                                | 1.21 ms: 1.09x slower                                                            |
| gunicorn                  | 1.20 ms                                                | 1.30 ms: 1.09x slower                                                            |
| meteor_contest            | 109 ms                                                 | 119 ms: 1.09x slower                                                             |
| pycparser                 | 1.19 sec                                               | 1.30 sec: 1.09x slower                                                           |
| pickle_list               | 4.59 us                                                | 5.02 us: 1.09x slower                                                            |
| sqlglot_optimize          | 55.3 ms                                                | 61.2 ms: 1.11x slower                                                            |
| xml_etree_process         | 56.9 ms                                                | 63.6 ms: 1.12x slower                                                            |
| raytrace                  | 309 ms                                                 | 346 ms: 1.12x slower                                                             |
| richards                  | 49.8 ms                                                | 56.1 ms: 1.13x slower                                                            |
| 2to3                      | 264 ms                                                 | 300 ms: 1.13x slower                                                             |
| dulwich_log               | 64.6 ms                                                | 73.4 ms: 1.14x slower                                                            |
| unpickle                  | 13.8 us                                                | 15.8 us: 1.14x slower                                                            |
| nqueens                   | 87.9 ms                                                | 100 ms: 1.14x slower                                                             |
| xml_etree_generate        | 81.1 ms                                                | 92.5 ms: 1.14x slower                                                            |
| sqlite_synth              | 2.57 us                                                | 2.95 us: 1.15x slower                                                            |
| unpickle_pure_python      | 242 us                                                 | 277 us: 1.15x slower                                                             |
| go                        | 149 ms                                                 | 172 ms: 1.16x slower                                                             |
| crypto_pyaes              | 76.7 ms                                                | 88.8 ms: 1.16x slower                                                            |
| genshi_xml                | 53.4 ms                                                | 62.4 ms: 1.17x slower                                                            |
| fannkuch                  | 405 ms                                                 | 481 ms: 1.19x slower                                                             |
| pprint_safe_repr          | 747 ms                                                 | 887 ms: 1.19x slower                                                             |
| pprint_pformat            | 1.55 sec                                               | 1.85 sec: 1.19x slower                                                           |
| float                     | 78.9 ms                                                | 93.9 ms: 1.19x slower                                                            |
| scimark_sparse_mat_mult   | 5.03 ms                                                | 5.99 ms: 1.19x slower                                                            |
| python_startup            | 8.56 ms                                                | 10.5 ms: 1.22x slower                                                            |
| genshi_text               | 22.5 ms                                                | 27.7 ms: 1.23x slower                                                            |
| scimark_sor               | 121 ms                                                 | 149 ms: 1.23x slower                                                             |
| regex_compile             | 141 ms                                                 | 175 ms: 1.24x slower                                                             |
| mako                      | 10.7 ms                                                | 13.2 ms: 1.24x slower                                                            |
| scimark_monte_carlo       | 70.7 ms                                                | 87.6 ms: 1.24x slower                                                            |
| coverage                  | 78.8 ms                                                | 99.2 ms: 1.26x slower                                                            |
| nbody                     | 96.0 ms                                                | 121 ms: 1.26x slower                                                             |
| async_generators          | 374 ms                                                 | 476 ms: 1.27x slower                                                             |
| scimark_fft               | 345 ms                                                 | 444 ms: 1.29x slower                                                             |
| hexiom                    | 6.89 ms                                                | 8.92 ms: 1.29x slower                                                            |
| spectral_norm             | 108 ms                                                 | 142 ms: 1.31x slower                                                             |
| telco                     | 6.86 ms                                                | 9.02 ms: 1.32x slower                                                            |
| mypy2                     | 686 ms                                                 | 914 ms: 1.33x slower                                                             |
| unpack_sequence           | 43.5 ns                                                | 58.9 ns: 1.36x slower                                                            |
| pyflate                   | 434 ms                                                 | 590 ms: 1.36x slower                                                             |
| scimark_lu                | 116 ms                                                 | 162 ms: 1.39x slower                                                             |
| python_startup_no_site    | 6.01 ms                                                | 9.07 ms: 1.51x slower                                                            |
| Geometric mean            | (ref)                                                  | 1.04x slower                                                                     |

Benchmark hidden because not significant (5): xml_etree_parse, bench_mp_pool, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, sqlglot_parse
Ignored benchmarks (3) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative


# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x


# Memory

- memory change: 1.01x