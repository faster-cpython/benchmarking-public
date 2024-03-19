# Results vs. 3.11.0

- fork: faster-cpython
- ref: optimizer_trim_trace
- machine: linux-x86_64
- commit hash: f012ce0
- commit date: 2024-03-19
- overall geometric mean: 1.05x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240319-linux-x86_64-faster%2dcpython-optimizer_trim_trace-3.13.0a5+-f012ce0 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 264 ms                                                 | 299 ms: 1.13x slower                                                             |
| chameleon      | 6.70 ms                                                | 7.35 ms: 1.10x slower                                                            |
| docutils       | 2.66 sec                                               | 2.92 sec: 1.10x slower                                                           |
| html5lib       | 64.8 ms                                                | 68.9 ms: 1.06x slower                                                            |
| tornado_http   | 98.1 ms                                                | 105 ms: 1.07x slower                                                             |
| Geometric mean | (ref)                                                  | 1.09x slower                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240319-linux-x86_64-faster%2dcpython-optimizer_trim_trace-3.13.0a5+-f012ce0 |
|---------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_none           | 528 ms                                                 | 468 ms: 1.13x faster                                                             |
| async_tree_memoization    | 639 ms                                                 | 599 ms: 1.07x faster                                                             |
| async_tree_memoization_tg | 626 ms                                                 | 603 ms: 1.04x faster                                                             |
| async_tree_io             | 1.29 sec                                               | 1.25 sec: 1.03x faster                                                           |
| async_tree_none_tg        | 491 ms                                                 | 476 ms: 1.03x faster                                                             |
| async_tree_io_tg          | 1.29 sec                                               | 1.27 sec: 1.02x faster                                                           |
| Geometric mean            | (ref)                                                  | 1.04x faster                                                                     |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240319-linux-x86_64-faster%2dcpython-optimizer_trim_trace-3.13.0a5+-f012ce0 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 194 ms                                                 | 191 ms: 1.02x faster                                                             |
| float          | 78.9 ms                                                | 97.7 ms: 1.24x slower                                                            |
| nbody          | 96.0 ms                                                | 125 ms: 1.30x slower                                                             |
| Geometric mean | (ref)                                                  | 1.17x slower                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240319-linux-x86_64-faster%2dcpython-optimizer_trim_trace-3.13.0a5+-f012ce0 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_effbot   | 3.51 ms                                                | 3.68 ms: 1.05x slower                                                            |
| regex_v8       | 22.9 ms                                                | 25.2 ms: 1.10x slower                                                            |
| regex_dna      | 205 ms                                                 | 227 ms: 1.11x slower                                                             |
| regex_compile  | 141 ms                                                 | 178 ms: 1.26x slower                                                             |
| Geometric mean | (ref)                                                  | 1.13x slower                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240319-linux-x86_64-faster%2dcpython-optimizer_trim_trace-3.13.0a5+-f012ce0 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_dumps           | 13.3 ms                                                | 10.7 ms: 1.25x faster                                                            |
| json_loads           | 29.2 us                                                | 27.9 us: 1.05x faster                                                            |
| pickle_pure_python   | 320 us                                                 | 309 us: 1.04x faster                                                             |
| unpickle_list        | 5.21 us                                                | 5.07 us: 1.03x faster                                                            |
| pickle_dict          | 34.6 us                                                | 35.6 us: 1.03x slower                                                            |
| xml_etree_iterparse  | 108 ms                                                 | 113 ms: 1.05x slower                                                             |
| pickle               | 11.0 us                                                | 11.6 us: 1.06x slower                                                            |
| tomli_loads          | 2.30 sec                                               | 2.48 sec: 1.08x slower                                                           |
| xml_etree_process    | 56.9 ms                                                | 63.5 ms: 1.12x slower                                                            |
| pickle_list          | 4.59 us                                                | 5.19 us: 1.13x slower                                                            |
| xml_etree_generate   | 81.1 ms                                                | 92.7 ms: 1.14x slower                                                            |
| unpickle_pure_python | 242 us                                                 | 278 us: 1.15x slower                                                             |
| unpickle             | 13.8 us                                                | 16.0 us: 1.16x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.04x slower                                                                     |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240319-linux-x86_64-faster%2dcpython-optimizer_trim_trace-3.13.0a5+-f012ce0 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 8.56 ms                                                | 10.5 ms: 1.23x slower                                                            |
| python_startup_no_site | 6.01 ms                                                | 9.08 ms: 1.51x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.36x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240319-linux-x86_64-faster%2dcpython-optimizer_trim_trace-3.13.0a5+-f012ce0 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| django_template | 33.5 ms                                                | 37.6 ms: 1.12x slower                                                            |
| genshi_xml      | 53.4 ms                                                | 63.9 ms: 1.20x slower                                                            |
| genshi_text     | 22.5 ms                                                | 27.5 ms: 1.22x slower                                                            |
| mako            | 10.7 ms                                                | 13.7 ms: 1.28x slower                                                            |
| Geometric mean  | (ref)                                                  | 1.20x slower                                                                     |

All benchmarks:
===============

| Benchmark                 | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240319-linux-x86_64-faster%2dcpython-optimizer_trim_trace-3.13.0a5+-f012ce0 |
|---------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| typing_runtime_protocols  | 520 us                                                 | 118 us: 4.40x faster                                                             |
| generators                | 74.9 ms                                                | 29.6 ms: 2.53x faster                                                            |
| asyncio_tcp               | 875 ms                                                 | 510 ms: 1.72x faster                                                             |
| asyncio_tcp_ssl           | 3.11 sec                                               | 1.86 sec: 1.67x faster                                                           |
| pylint                    | 476 ms                                                 | 333 ms: 1.43x faster                                                             |
| json_dumps                | 13.3 ms                                                | 10.7 ms: 1.25x faster                                                            |
| coroutines                | 27.0 ms                                                | 22.7 ms: 1.19x faster                                                            |
| async_tree_none           | 528 ms                                                 | 468 ms: 1.13x faster                                                             |
| async_tree_memoization    | 639 ms                                                 | 599 ms: 1.07x faster                                                             |
| logging_silent            | 111 ns                                                 | 105 ns: 1.06x faster                                                             |
| comprehensions            | 23.6 us                                                | 22.6 us: 1.05x faster                                                            |
| json_loads                | 29.2 us                                                | 27.9 us: 1.05x faster                                                            |
| async_tree_memoization_tg | 626 ms                                                 | 603 ms: 1.04x faster                                                             |
| pickle_pure_python        | 320 us                                                 | 309 us: 1.04x faster                                                             |
| async_tree_io             | 1.29 sec                                               | 1.25 sec: 1.03x faster                                                           |
| djangocms                 | 33.5 us                                                | 32.5 us: 1.03x faster                                                            |
| async_tree_none_tg        | 491 ms                                                 | 476 ms: 1.03x faster                                                             |
| unpickle_list             | 5.21 us                                                | 5.07 us: 1.03x faster                                                            |
| mdp                       | 2.77 sec                                               | 2.70 sec: 1.03x faster                                                           |
| async_tree_io_tg          | 1.29 sec                                               | 1.27 sec: 1.02x faster                                                           |
| deltablue                 | 3.92 ms                                                | 3.86 ms: 1.02x faster                                                            |
| pidigits                  | 194 ms                                                 | 191 ms: 1.02x faster                                                             |
| gc_traversal              | 4.01 ms                                                | 3.96 ms: 1.01x faster                                                            |
| deepcopy                  | 365 us                                                 | 367 us: 1.01x slower                                                             |
| sympy_sum                 | 169 ms                                                 | 170 ms: 1.01x slower                                                             |
| sqlglot_parse             | 1.43 ms                                                | 1.45 ms: 1.01x slower                                                            |
| sqlglot_transpile         | 1.75 ms                                                | 1.79 ms: 1.02x slower                                                            |
| asyncio_websockets        | 550 ms                                                 | 563 ms: 1.02x slower                                                             |
| deepcopy_reduce           | 3.22 us                                                | 3.30 us: 1.03x slower                                                            |
| pickle_dict               | 34.6 us                                                | 35.6 us: 1.03x slower                                                            |
| sympy_str                 | 297 ms                                                 | 308 ms: 1.04x slower                                                             |
| logging_simple            | 6.22 us                                                | 6.45 us: 1.04x slower                                                            |
| bench_thread_pool         | 834 us                                                 | 866 us: 1.04x slower                                                             |
| dask                      | 365 ms                                                 | 379 ms: 1.04x slower                                                             |
| sympy_integrate           | 21.5 ms                                                | 22.3 ms: 1.04x slower                                                            |
| xml_etree_iterparse       | 108 ms                                                 | 113 ms: 1.05x slower                                                             |
| regex_effbot              | 3.51 ms                                                | 3.68 ms: 1.05x slower                                                            |
| thrift                    | 784 us                                                 | 824 us: 1.05x slower                                                             |
| deepcopy_memo             | 40.2 us                                                | 42.2 us: 1.05x slower                                                            |
| chaos                     | 71.9 ms                                                | 75.7 ms: 1.05x slower                                                            |
| pickle                    | 11.0 us                                                | 11.6 us: 1.06x slower                                                            |
| html5lib                  | 64.8 ms                                                | 68.9 ms: 1.06x slower                                                            |
| sqlglot_normalize         | 113 ms                                                 | 120 ms: 1.06x slower                                                             |
| tornado_http              | 98.1 ms                                                | 105 ms: 1.07x slower                                                             |
| logging_format            | 6.81 us                                                | 7.26 us: 1.07x slower                                                            |
| sympy_expand              | 484 ms                                                 | 517 ms: 1.07x slower                                                             |
| pathlib                   | 18.5 ms                                                | 19.8 ms: 1.07x slower                                                            |
| tomli_loads               | 2.30 sec                                               | 2.48 sec: 1.08x slower                                                           |
| create_gc_cycles          | 1.43 ms                                                | 1.56 ms: 1.09x slower                                                            |
| meteor_contest            | 109 ms                                                 | 119 ms: 1.09x slower                                                             |
| docutils                  | 2.66 sec                                               | 2.92 sec: 1.10x slower                                                           |
| chameleon                 | 6.70 ms                                                | 7.35 ms: 1.10x slower                                                            |
| aiohttp                   | 1.12 ms                                                | 1.22 ms: 1.10x slower                                                            |
| gunicorn                  | 1.20 ms                                                | 1.32 ms: 1.10x slower                                                            |
| regex_v8                  | 22.9 ms                                                | 25.2 ms: 1.10x slower                                                            |
| sqlglot_optimize          | 55.3 ms                                                | 61.2 ms: 1.11x slower                                                            |
| pycparser                 | 1.19 sec                                               | 1.31 sec: 1.11x slower                                                           |
| regex_dna                 | 205 ms                                                 | 227 ms: 1.11x slower                                                             |
| xml_etree_process         | 56.9 ms                                                | 63.5 ms: 1.12x slower                                                            |
| raytrace                  | 309 ms                                                 | 345 ms: 1.12x slower                                                             |
| richards                  | 49.8 ms                                                | 55.7 ms: 1.12x slower                                                            |
| django_template           | 33.5 ms                                                | 37.6 ms: 1.12x slower                                                            |
| 2to3                      | 264 ms                                                 | 299 ms: 1.13x slower                                                             |
| pickle_list               | 4.59 us                                                | 5.19 us: 1.13x slower                                                            |
| dulwich_log               | 64.6 ms                                                | 73.6 ms: 1.14x slower                                                            |
| xml_etree_generate        | 81.1 ms                                                | 92.7 ms: 1.14x slower                                                            |
| sqlite_synth              | 2.57 us                                                | 2.96 us: 1.15x slower                                                            |
| crypto_pyaes              | 76.7 ms                                                | 88.2 ms: 1.15x slower                                                            |
| unpickle_pure_python      | 242 us                                                 | 278 us: 1.15x slower                                                             |
| unpickle                  | 13.8 us                                                | 16.0 us: 1.16x slower                                                            |
| nqueens                   | 87.9 ms                                                | 103 ms: 1.18x slower                                                             |
| scimark_sor               | 121 ms                                                 | 144 ms: 1.19x slower                                                             |
| fannkuch                  | 405 ms                                                 | 481 ms: 1.19x slower                                                             |
| genshi_xml                | 53.4 ms                                                | 63.9 ms: 1.20x slower                                                            |
| pprint_safe_repr          | 747 ms                                                 | 901 ms: 1.21x slower                                                             |
| scimark_sparse_mat_mult   | 5.03 ms                                                | 6.07 ms: 1.21x slower                                                            |
| go                        | 149 ms                                                 | 180 ms: 1.21x slower                                                             |
| pprint_pformat            | 1.55 sec                                               | 1.89 sec: 1.21x slower                                                           |
| genshi_text               | 22.5 ms                                                | 27.5 ms: 1.22x slower                                                            |
| unpack_sequence           | 43.5 ns                                                | 53.1 ns: 1.22x slower                                                            |
| python_startup            | 8.56 ms                                                | 10.5 ms: 1.23x slower                                                            |
| coverage                  | 78.8 ms                                                | 97.0 ms: 1.23x slower                                                            |
| float                     | 78.9 ms                                                | 97.7 ms: 1.24x slower                                                            |
| regex_compile             | 141 ms                                                 | 178 ms: 1.26x slower                                                             |
| scimark_monte_carlo       | 70.7 ms                                                | 89.3 ms: 1.26x slower                                                            |
| scimark_fft               | 345 ms                                                 | 437 ms: 1.27x slower                                                             |
| async_generators          | 374 ms                                                 | 477 ms: 1.28x slower                                                             |
| mako                      | 10.7 ms                                                | 13.7 ms: 1.28x slower                                                            |
| telco                     | 6.86 ms                                                | 8.85 ms: 1.29x slower                                                            |
| spectral_norm             | 108 ms                                                 | 140 ms: 1.30x slower                                                             |
| nbody                     | 96.0 ms                                                | 125 ms: 1.30x slower                                                             |
| mypy2                     | 686 ms                                                 | 923 ms: 1.35x slower                                                             |
| hexiom                    | 6.89 ms                                                | 9.27 ms: 1.35x slower                                                            |
| pyflate                   | 434 ms                                                 | 589 ms: 1.36x slower                                                             |
| scimark_lu                | 116 ms                                                 | 168 ms: 1.44x slower                                                             |
| python_startup_no_site    | 6.01 ms                                                | 9.08 ms: 1.51x slower                                                            |
| Geometric mean            | (ref)                                                  | 1.05x slower                                                                     |

Benchmark hidden because not significant (6): json, xml_etree_parse, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, richards_super, bench_mp_pool
Ignored benchmarks (3) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative


# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x


# Memory

- memory change: 1.01x