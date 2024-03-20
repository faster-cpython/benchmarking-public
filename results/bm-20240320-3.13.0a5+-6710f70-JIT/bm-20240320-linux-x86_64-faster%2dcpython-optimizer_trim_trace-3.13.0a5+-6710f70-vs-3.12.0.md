# Results vs. 3.12.0

- fork: faster-cpython
- ref: optimizer_trim_trace
- machine: linux-x86_64
- commit hash: 6710f70
- commit date: 2024-03-20
- overall geometric mean: 1.01x slower
- HPT reliability: 95.33%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.17x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240320-linux-x86_64-faster%2dcpython-optimizer_trim_trace-3.13.0a5+-6710f70 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 282 ms: 1.03x slower                                                             |
| chameleon      | 7.41 ms                                                | 7.06 ms: 1.05x faster                                                            |
| docutils       | 2.77 sec                                               | 2.80 sec: 1.01x slower                                                           |
| tornado_http   | 103 ms                                                 | 98.8 ms: 1.04x faster                                                            |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240320-linux-x86_64-faster%2dcpython-optimizer_trim_trace-3.13.0a5+-6710f70 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_none            | 472 ms                                                 | 449 ms: 1.05x faster                                                             |
| async_tree_none_tg         | 450 ms                                                 | 460 ms: 1.02x slower                                                             |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 746 ms: 1.03x slower                                                             |
| async_tree_memoization_tg  | 575 ms                                                 | 599 ms: 1.04x slower                                                             |
| async_tree_io_tg           | 1.18 sec                                               | 1.24 sec: 1.05x slower                                                           |
| async_tree_io              | 1.16 sec                                               | 1.22 sec: 1.06x slower                                                           |
| Geometric mean             | (ref)                                                  | 1.02x slower                                                                     |

Benchmark hidden because not significant (2): async_tree_memoization, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240320-linux-x86_64-faster%2dcpython-optimizer_trim_trace-3.13.0a5+-6710f70 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 80.2 ms: 1.06x faster                                                            |
| nbody          | 97.0 ms                                                | 94.6 ms: 1.02x faster                                                            |
| pidigits       | 187 ms                                                 | 190 ms: 1.01x slower                                                             |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240320-linux-x86_64-faster%2dcpython-optimizer_trim_trace-3.13.0a5+-6710f70 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 145 ms: 1.02x faster                                                             |
| regex_effbot   | 3.61 ms                                                | 3.81 ms: 1.06x slower                                                            |
| regex_dna      | 212 ms                                                 | 230 ms: 1.09x slower                                                             |
| regex_v8       | 23.1 ms                                                | 25.5 ms: 1.10x slower                                                            |
| Geometric mean | (ref)                                                  | 1.06x slower                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240320-linux-x86_64-faster%2dcpython-optimizer_trim_trace-3.13.0a5+-6710f70 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.06 sec: 1.13x faster                                                           |
| pickle_pure_python   | 324 us                                                 | 304 us: 1.07x faster                                                             |
| pickle_dict          | 35.5 us                                                | 34.4 us: 1.03x faster                                                            |
| pickle_list          | 5.08 us                                                | 4.95 us: 1.03x faster                                                            |
| xml_etree_process    | 61.7 ms                                                | 60.1 ms: 1.03x faster                                                            |
| xml_etree_generate   | 89.2 ms                                                | 87.2 ms: 1.02x faster                                                            |
| unpickle_list        | 5.29 us                                                | 5.19 us: 1.02x faster                                                            |
| pickle               | 11.6 us                                                | 11.5 us: 1.01x faster                                                            |
| json_loads           | 28.5 us                                                | 28.4 us: 1.00x faster                                                            |
| json_dumps           | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                            |
| xml_etree_iterparse  | 107 ms                                                 | 109 ms: 1.02x slower                                                             |
| unpickle_pure_python | 230 us                                                 | 239 us: 1.04x slower                                                             |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                                     |

Benchmark hidden because not significant (2): unpickle, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240320-linux-x86_64-faster%2dcpython-optimizer_trim_trace-3.13.0a5+-6710f70 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 9.55 ms                                                | 12.6 ms: 1.32x slower                                                            |
| python_startup_no_site | 6.94 ms                                                | 11.1 ms: 1.61x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.45x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240320-linux-x86_64-faster%2dcpython-optimizer_trim_trace-3.13.0a5+-6710f70 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.0 ms: 1.08x faster                                                            |
| django_template | 34.6 ms                                                | 35.2 ms: 1.02x slower                                                            |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240320-linux-x86_64-faster%2dcpython-optimizer_trim_trace-3.13.0a5+-6710f70 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| typing_runtime_protocols   | 158 us                                                 | 112 us: 1.41x faster                                                             |
| comprehensions             | 21.8 us                                                | 17.8 us: 1.22x faster                                                            |
| tomli_loads                | 2.33 sec                                               | 2.06 sec: 1.13x faster                                                           |
| logging_format             | 7.23 us                                                | 6.51 us: 1.11x faster                                                            |
| scimark_fft                | 382 ms                                                 | 345 ms: 1.11x faster                                                             |
| logging_simple             | 6.46 us                                                | 5.86 us: 1.10x faster                                                            |
| crypto_pyaes               | 81.9 ms                                                | 75.1 ms: 1.09x faster                                                            |
| deltablue                  | 3.72 ms                                                | 3.43 ms: 1.08x faster                                                            |
| mako                       | 11.9 ms                                                | 11.0 ms: 1.08x faster                                                            |
| deepcopy_reduce            | 3.35 us                                                | 3.13 us: 1.07x faster                                                            |
| pickle_pure_python         | 324 us                                                 | 304 us: 1.07x faster                                                             |
| raytrace                   | 312 ms                                                 | 293 ms: 1.07x faster                                                             |
| deepcopy                   | 371 us                                                 | 349 us: 1.06x faster                                                             |
| scimark_monte_carlo        | 75.1 ms                                                | 70.9 ms: 1.06x faster                                                            |
| float                      | 84.7 ms                                                | 80.2 ms: 1.06x faster                                                            |
| generators                 | 31.2 ms                                                | 29.6 ms: 1.06x faster                                                            |
| deepcopy_memo              | 40.7 us                                                | 38.6 us: 1.05x faster                                                            |
| async_tree_none            | 472 ms                                                 | 449 ms: 1.05x faster                                                             |
| chameleon                  | 7.41 ms                                                | 7.06 ms: 1.05x faster                                                            |
| fannkuch                   | 417 ms                                                 | 398 ms: 1.05x faster                                                             |
| chaos                      | 67.0 ms                                                | 64.0 ms: 1.05x faster                                                            |
| sympy_str                  | 300 ms                                                 | 288 ms: 1.04x faster                                                             |
| pathlib                    | 19.3 ms                                                | 18.6 ms: 1.04x faster                                                            |
| tornado_http               | 103 ms                                                 | 98.8 ms: 1.04x faster                                                            |
| logging_silent             | 104 ns                                                 | 101 ns: 1.04x faster                                                             |
| sympy_sum                  | 169 ms                                                 | 163 ms: 1.03x faster                                                             |
| sqlglot_parse              | 1.36 ms                                                | 1.32 ms: 1.03x faster                                                            |
| pickle_dict                | 35.5 us                                                | 34.4 us: 1.03x faster                                                            |
| pickle_list                | 5.08 us                                                | 4.95 us: 1.03x faster                                                            |
| xml_etree_process          | 61.7 ms                                                | 60.1 ms: 1.03x faster                                                            |
| nbody                      | 97.0 ms                                                | 94.6 ms: 1.02x faster                                                            |
| meteor_contest             | 112 ms                                                 | 110 ms: 1.02x faster                                                             |
| xml_etree_generate         | 89.2 ms                                                | 87.2 ms: 1.02x faster                                                            |
| regex_compile              | 148 ms                                                 | 145 ms: 1.02x faster                                                             |
| unpickle_list              | 5.29 us                                                | 5.19 us: 1.02x faster                                                            |
| pprint_safe_repr           | 776 ms                                                 | 762 ms: 1.02x faster                                                             |
| sqlglot_transpile          | 1.68 ms                                                | 1.66 ms: 1.01x faster                                                            |
| pickle                     | 11.6 us                                                | 11.5 us: 1.01x faster                                                            |
| coroutines                 | 23.2 ms                                                | 23.0 ms: 1.01x faster                                                            |
| sqlglot_normalize          | 110 ms                                                 | 110 ms: 1.01x faster                                                             |
| json_loads                 | 28.5 us                                                | 28.4 us: 1.00x faster                                                            |
| docutils                   | 2.77 sec                                               | 2.80 sec: 1.01x slower                                                           |
| pyflate                    | 482 ms                                                 | 488 ms: 1.01x slower                                                             |
| json_dumps                 | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                            |
| richards_super             | 51.5 ms                                                | 52.1 ms: 1.01x slower                                                            |
| sqlite_synth               | 2.83 us                                                | 2.87 us: 1.01x slower                                                            |
| async_generators           | 463 ms                                                 | 469 ms: 1.01x slower                                                             |
| bench_thread_pool          | 842 us                                                 | 853 us: 1.01x slower                                                             |
| pidigits                   | 187 ms                                                 | 190 ms: 1.01x slower                                                             |
| sympy_expand               | 478 ms                                                 | 485 ms: 1.02x slower                                                             |
| xml_etree_iterparse        | 107 ms                                                 | 109 ms: 1.02x slower                                                             |
| django_template            | 34.6 ms                                                | 35.2 ms: 1.02x slower                                                            |
| mdp                        | 2.63 sec                                               | 2.68 sec: 1.02x slower                                                           |
| sympy_integrate            | 21.4 ms                                                | 21.8 ms: 1.02x slower                                                            |
| asyncio_websockets         | 551 ms                                                 | 564 ms: 1.02x slower                                                             |
| dulwich_log                | 68.5 ms                                                | 70.1 ms: 1.02x slower                                                            |
| async_tree_none_tg         | 450 ms                                                 | 460 ms: 1.02x slower                                                             |
| create_gc_cycles           | 1.48 ms                                                | 1.51 ms: 1.02x slower                                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 746 ms: 1.03x slower                                                             |
| 2to3                       | 274 ms                                                 | 282 ms: 1.03x slower                                                             |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.85 sec: 1.04x slower                                                           |
| sqlglot_optimize           | 54.8 ms                                                | 56.9 ms: 1.04x slower                                                            |
| unpickle_pure_python       | 230 us                                                 | 239 us: 1.04x slower                                                             |
| async_tree_memoization_tg  | 575 ms                                                 | 599 ms: 1.04x slower                                                             |
| aiohttp                    | 1.15 ms                                                | 1.20 ms: 1.05x slower                                                            |
| async_tree_io_tg           | 1.18 sec                                               | 1.24 sec: 1.05x slower                                                           |
| gunicorn                   | 1.24 ms                                                | 1.30 ms: 1.05x slower                                                            |
| asyncio_tcp                | 491 ms                                                 | 515 ms: 1.05x slower                                                             |
| pycparser                  | 1.18 sec                                               | 1.24 sec: 1.05x slower                                                           |
| regex_effbot               | 3.61 ms                                                | 3.81 ms: 1.06x slower                                                            |
| async_tree_io              | 1.16 sec                                               | 1.22 sec: 1.06x slower                                                           |
| nqueens                    | 83.3 ms                                                | 89.3 ms: 1.07x slower                                                            |
| gc_traversal               | 3.79 ms                                                | 4.08 ms: 1.07x slower                                                            |
| regex_dna                  | 212 ms                                                 | 230 ms: 1.09x slower                                                             |
| hexiom                     | 6.41 ms                                                | 6.99 ms: 1.09x slower                                                            |
| scimark_lu                 | 118 ms                                                 | 129 ms: 1.10x slower                                                             |
| mypy2                      | 830 ms                                                 | 911 ms: 1.10x slower                                                             |
| bench_mp_pool              | 24.0 ms                                                | 26.4 ms: 1.10x slower                                                            |
| regex_v8                   | 23.1 ms                                                | 25.5 ms: 1.10x slower                                                            |
| go                         | 139 ms                                                 | 154 ms: 1.11x slower                                                             |
| telco                      | 7.10 ms                                                | 8.41 ms: 1.19x slower                                                            |
| python_startup             | 9.55 ms                                                | 12.6 ms: 1.32x slower                                                            |
| coverage                   | 72.7 ms                                                | 98.0 ms: 1.35x slower                                                            |
| python_startup_no_site     | 6.94 ms                                                | 11.1 ms: 1.61x slower                                                            |
| unpack_sequence            | 54.0 ns                                                | 92.9 ns: 1.72x slower                                                            |
| Geometric mean             | (ref)                                                  | 1.01x slower                                                                     |

Benchmark hidden because not significant (11): unpickle, pprint_pformat, json, async_tree_memoization, async_tree_cpu_io_mixed, scimark_sor, scimark_sparse_mat_mult, dask, richards, xml_etree_parse, spectral_norm
Ignored benchmarks (2) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20240320-3.13.0a5+-6710f70-JIT/bm-20240320-linux-x86_64-faster%2dcpython-optimizer_trim_trace-3.13.0a5+-6710f70.json: djangocms, genshi_text, genshi_xml, html5lib, pylint, thrift


# HPT report

- Reliability score: 95.33% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x


# Memory

- memory change: 1.17x