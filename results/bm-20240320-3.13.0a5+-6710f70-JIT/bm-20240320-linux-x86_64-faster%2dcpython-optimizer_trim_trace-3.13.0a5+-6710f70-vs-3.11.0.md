# Results vs. 3.11.0

- fork: faster-cpython
- ref: optimizer_trim_trace
- machine: linux-x86_64
- commit hash: 6710f70
- commit date: 2024-03-20
- overall geometric mean: 1.02x faster
- HPT reliability: 54.72%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.24x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240320-linux-x86_64-faster%2dcpython-optimizer_trim_trace-3.13.0a5+-6710f70 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 264 ms                                                 | 282 ms: 1.07x slower                                                             |
| chameleon      | 6.70 ms                                                | 7.06 ms: 1.05x slower                                                            |
| docutils       | 2.66 sec                                               | 2.80 sec: 1.05x slower                                                           |
| html5lib       | 64.8 ms                                                | 65.9 ms: 1.02x slower                                                            |
| tornado_http   | 98.1 ms                                                | 98.8 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                  | 1.04x slower                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240320-linux-x86_64-faster%2dcpython-optimizer_trim_trace-3.13.0a5+-6710f70 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_none            | 528 ms                                                 | 449 ms: 1.18x faster                                                             |
| async_tree_memoization     | 639 ms                                                 | 578 ms: 1.10x faster                                                             |
| async_tree_none_tg         | 491 ms                                                 | 460 ms: 1.07x faster                                                             |
| async_tree_io              | 1.29 sec                                               | 1.22 sec: 1.05x faster                                                           |
| async_tree_memoization_tg  | 626 ms                                                 | 599 ms: 1.05x faster                                                             |
| async_tree_io_tg           | 1.29 sec                                               | 1.24 sec: 1.05x faster                                                           |
| async_tree_cpu_io_mixed    | 749 ms                                                 | 727 ms: 1.03x faster                                                             |
| async_tree_cpu_io_mixed_tg | 761 ms                                                 | 746 ms: 1.02x faster                                                             |
| Geometric mean             | (ref)                                                  | 1.07x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240320-linux-x86_64-faster%2dcpython-optimizer_trim_trace-3.13.0a5+-6710f70 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 194 ms                                                 | 190 ms: 1.02x faster                                                             |
| nbody          | 96.0 ms                                                | 94.6 ms: 1.01x faster                                                            |
| float          | 78.9 ms                                                | 80.2 ms: 1.02x slower                                                            |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240320-linux-x86_64-faster%2dcpython-optimizer_trim_trace-3.13.0a5+-6710f70 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 141 ms                                                 | 145 ms: 1.03x slower                                                             |
| regex_effbot   | 3.51 ms                                                | 3.81 ms: 1.09x slower                                                            |
| regex_v8       | 22.9 ms                                                | 25.5 ms: 1.12x slower                                                            |
| regex_dna      | 205 ms                                                 | 230 ms: 1.13x slower                                                             |
| Geometric mean | (ref)                                                  | 1.09x slower                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240320-linux-x86_64-faster%2dcpython-optimizer_trim_trace-3.13.0a5+-6710f70 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_dumps           | 13.3 ms                                                | 10.5 ms: 1.27x faster                                                            |
| tomli_loads          | 2.30 sec                                               | 2.06 sec: 1.12x faster                                                           |
| pickle_pure_python   | 320 us                                                 | 304 us: 1.05x faster                                                             |
| json_loads           | 29.2 us                                                | 28.4 us: 1.03x faster                                                            |
| xml_etree_parse      | 164 ms                                                 | 160 ms: 1.02x faster                                                             |
| unpickle_pure_python | 242 us                                                 | 239 us: 1.01x faster                                                             |
| pickle_dict          | 34.6 us                                                | 34.4 us: 1.00x faster                                                            |
| pickle               | 11.0 us                                                | 11.5 us: 1.04x slower                                                            |
| xml_etree_process    | 56.9 ms                                                | 60.1 ms: 1.06x slower                                                            |
| xml_etree_generate   | 81.1 ms                                                | 87.2 ms: 1.08x slower                                                            |
| pickle_list          | 4.59 us                                                | 4.95 us: 1.08x slower                                                            |
| unpickle             | 13.8 us                                                | 15.5 us: 1.12x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                                     |

Benchmark hidden because not significant (2): unpickle_list, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240320-linux-x86_64-faster%2dcpython-optimizer_trim_trace-3.13.0a5+-6710f70 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 8.56 ms                                                | 12.6 ms: 1.47x slower                                                            |
| python_startup_no_site | 6.01 ms                                                | 11.1 ms: 1.85x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.65x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240320-linux-x86_64-faster%2dcpython-optimizer_trim_trace-3.13.0a5+-6710f70 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 10.7 ms                                                | 11.0 ms: 1.03x slower                                                            |
| genshi_xml      | 53.4 ms                                                | 55.1 ms: 1.03x slower                                                            |
| django_template | 33.5 ms                                                | 35.2 ms: 1.05x slower                                                            |
| genshi_text     | 22.5 ms                                                | 24.6 ms: 1.09x slower                                                            |
| Geometric mean  | (ref)                                                  | 1.05x slower                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240320-linux-x86_64-faster%2dcpython-optimizer_trim_trace-3.13.0a5+-6710f70 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| typing_runtime_protocols   | 520 us                                                 | 112 us: 4.63x faster                                                             |
| generators                 | 74.9 ms                                                | 29.6 ms: 2.53x faster                                                            |
| asyncio_tcp                | 875 ms                                                 | 515 ms: 1.70x faster                                                             |
| asyncio_tcp_ssl            | 3.11 sec                                               | 1.85 sec: 1.68x faster                                                           |
| pylint                     | 476 ms                                                 | 326 ms: 1.46x faster                                                             |
| comprehensions             | 23.6 us                                                | 17.8 us: 1.33x faster                                                            |
| json_dumps                 | 13.3 ms                                                | 10.5 ms: 1.27x faster                                                            |
| richards_super             | 61.9 ms                                                | 52.1 ms: 1.19x faster                                                            |
| async_tree_none            | 528 ms                                                 | 449 ms: 1.18x faster                                                             |
| coroutines                 | 27.0 ms                                                | 23.0 ms: 1.17x faster                                                            |
| deltablue                  | 3.92 ms                                                | 3.43 ms: 1.14x faster                                                            |
| chaos                      | 71.9 ms                                                | 64.0 ms: 1.12x faster                                                            |
| tomli_loads                | 2.30 sec                                               | 2.06 sec: 1.12x faster                                                           |
| async_tree_memoization     | 639 ms                                                 | 578 ms: 1.10x faster                                                             |
| logging_silent             | 111 ns                                                 | 101 ns: 1.10x faster                                                             |
| sqlglot_parse              | 1.43 ms                                                | 1.32 ms: 1.09x faster                                                            |
| richards                   | 49.8 ms                                                | 46.0 ms: 1.08x faster                                                            |
| async_tree_none_tg         | 491 ms                                                 | 460 ms: 1.07x faster                                                             |
| logging_simple             | 6.22 us                                                | 5.86 us: 1.06x faster                                                            |
| async_tree_io              | 1.29 sec                                               | 1.22 sec: 1.05x faster                                                           |
| pickle_pure_python         | 320 us                                                 | 304 us: 1.05x faster                                                             |
| raytrace                   | 309 ms                                                 | 293 ms: 1.05x faster                                                             |
| sqlglot_transpile          | 1.75 ms                                                | 1.66 ms: 1.05x faster                                                            |
| deepcopy                   | 365 us                                                 | 349 us: 1.05x faster                                                             |
| logging_format             | 6.81 us                                                | 6.51 us: 1.05x faster                                                            |
| async_tree_memoization_tg  | 626 ms                                                 | 599 ms: 1.05x faster                                                             |
| async_tree_io_tg           | 1.29 sec                                               | 1.24 sec: 1.05x faster                                                           |
| deepcopy_memo              | 40.2 us                                                | 38.6 us: 1.04x faster                                                            |
| djangocms                  | 33.5 us                                                | 32.4 us: 1.04x faster                                                            |
| mdp                        | 2.77 sec                                               | 2.68 sec: 1.04x faster                                                           |
| sympy_str                  | 297 ms                                                 | 288 ms: 1.03x faster                                                             |
| sympy_sum                  | 169 ms                                                 | 163 ms: 1.03x faster                                                             |
| async_tree_cpu_io_mixed    | 749 ms                                                 | 727 ms: 1.03x faster                                                             |
| json_loads                 | 29.2 us                                                | 28.4 us: 1.03x faster                                                            |
| sqlglot_normalize          | 113 ms                                                 | 110 ms: 1.03x faster                                                             |
| deepcopy_reduce            | 3.22 us                                                | 3.13 us: 1.03x faster                                                            |
| xml_etree_parse            | 164 ms                                                 | 160 ms: 1.02x faster                                                             |
| pidigits                   | 194 ms                                                 | 190 ms: 1.02x faster                                                             |
| crypto_pyaes               | 76.7 ms                                                | 75.1 ms: 1.02x faster                                                            |
| async_tree_cpu_io_mixed_tg | 761 ms                                                 | 746 ms: 1.02x faster                                                             |
| fannkuch                   | 405 ms                                                 | 398 ms: 1.02x faster                                                             |
| nbody                      | 96.0 ms                                                | 94.6 ms: 1.01x faster                                                            |
| unpickle_pure_python       | 242 us                                                 | 239 us: 1.01x faster                                                             |
| pickle_dict                | 34.6 us                                                | 34.4 us: 1.00x faster                                                            |
| tornado_http               | 98.1 ms                                                | 98.8 ms: 1.01x slower                                                            |
| meteor_contest             | 109 ms                                                 | 110 ms: 1.01x slower                                                             |
| hexiom                     | 6.89 ms                                                | 6.99 ms: 1.02x slower                                                            |
| nqueens                    | 87.9 ms                                                | 89.3 ms: 1.02x slower                                                            |
| float                      | 78.9 ms                                                | 80.2 ms: 1.02x slower                                                            |
| html5lib                   | 64.8 ms                                                | 65.9 ms: 1.02x slower                                                            |
| sympy_integrate            | 21.5 ms                                                | 21.8 ms: 1.02x slower                                                            |
| gc_traversal               | 4.01 ms                                                | 4.08 ms: 1.02x slower                                                            |
| pprint_safe_repr           | 747 ms                                                 | 762 ms: 1.02x slower                                                             |
| dask                       | 365 ms                                                 | 373 ms: 1.02x slower                                                             |
| bench_thread_pool          | 834 us                                                 | 853 us: 1.02x slower                                                             |
| asyncio_websockets         | 550 ms                                                 | 564 ms: 1.02x slower                                                             |
| sqlglot_optimize           | 55.3 ms                                                | 56.9 ms: 1.03x slower                                                            |
| regex_compile              | 141 ms                                                 | 145 ms: 1.03x slower                                                             |
| mako                       | 10.7 ms                                                | 11.0 ms: 1.03x slower                                                            |
| genshi_xml                 | 53.4 ms                                                | 55.1 ms: 1.03x slower                                                            |
| go                         | 149 ms                                                 | 154 ms: 1.04x slower                                                             |
| pycparser                  | 1.19 sec                                               | 1.24 sec: 1.04x slower                                                           |
| pickle                     | 11.0 us                                                | 11.5 us: 1.04x slower                                                            |
| django_template            | 33.5 ms                                                | 35.2 ms: 1.05x slower                                                            |
| docutils                   | 2.66 sec                                               | 2.80 sec: 1.05x slower                                                           |
| chameleon                  | 6.70 ms                                                | 7.06 ms: 1.05x slower                                                            |
| thrift                     | 784 us                                                 | 827 us: 1.05x slower                                                             |
| create_gc_cycles           | 1.43 ms                                                | 1.51 ms: 1.06x slower                                                            |
| xml_etree_process          | 56.9 ms                                                | 60.1 ms: 1.06x slower                                                            |
| spectral_norm              | 108 ms                                                 | 115 ms: 1.07x slower                                                             |
| scimark_sor                | 121 ms                                                 | 129 ms: 1.07x slower                                                             |
| 2to3                       | 264 ms                                                 | 282 ms: 1.07x slower                                                             |
| xml_etree_generate         | 81.1 ms                                                | 87.2 ms: 1.08x slower                                                            |
| aiohttp                    | 1.12 ms                                                | 1.20 ms: 1.08x slower                                                            |
| pickle_list                | 4.59 us                                                | 4.95 us: 1.08x slower                                                            |
| dulwich_log                | 64.6 ms                                                | 70.1 ms: 1.08x slower                                                            |
| gunicorn                   | 1.20 ms                                                | 1.30 ms: 1.09x slower                                                            |
| regex_effbot               | 3.51 ms                                                | 3.81 ms: 1.09x slower                                                            |
| genshi_text                | 22.5 ms                                                | 24.6 ms: 1.09x slower                                                            |
| bench_mp_pool              | 24.0 ms                                                | 26.4 ms: 1.10x slower                                                            |
| scimark_lu                 | 116 ms                                                 | 129 ms: 1.11x slower                                                             |
| sqlite_synth               | 2.57 us                                                | 2.87 us: 1.11x slower                                                            |
| regex_v8                   | 22.9 ms                                                | 25.5 ms: 1.12x slower                                                            |
| unpickle                   | 13.8 us                                                | 15.5 us: 1.12x slower                                                            |
| pyflate                    | 434 ms                                                 | 488 ms: 1.12x slower                                                             |
| regex_dna                  | 205 ms                                                 | 230 ms: 1.13x slower                                                             |
| telco                      | 6.86 ms                                                | 8.41 ms: 1.23x slower                                                            |
| coverage                   | 78.8 ms                                                | 98.0 ms: 1.24x slower                                                            |
| async_generators           | 374 ms                                                 | 469 ms: 1.25x slower                                                             |
| mypy2                      | 686 ms                                                 | 911 ms: 1.33x slower                                                             |
| python_startup             | 8.56 ms                                                | 12.6 ms: 1.47x slower                                                            |
| python_startup_no_site     | 6.01 ms                                                | 11.1 ms: 1.85x slower                                                            |
| unpack_sequence            | 43.5 ns                                                | 92.9 ns: 2.14x slower                                                            |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                                     |

Benchmark hidden because not significant (9): unpickle_list, scimark_fft, json, sympy_expand, pprint_pformat, scimark_monte_carlo, pathlib, xml_etree_iterparse, scimark_sparse_mat_mult
Ignored benchmarks (3) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative


# HPT report

- Reliability score: 54.72% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x


# Memory

- memory change: 1.24x