# Results vs. 3.12.0

- fork: faster-cpython
- ref: specialize_binary_fl
- machine: linux-x86_64
- commit hash: cb4cc72
- commit date: 2024-03-26
- overall geometric mean: 1.04x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 0.95x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240326-linux-x86_64-faster%2dcpython-specialize_binary_fl-3.13.0a5+-cb4cc72 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 269 ms: 1.02x faster                                                             |
| chameleon      | 7.41 ms                                                | 6.94 ms: 1.07x faster                                                            |
| tornado_http   | 103 ms                                                 | 95.3 ms: 1.08x faster                                                            |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                     |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240326-linux-x86_64-faster%2dcpython-specialize_binary_fl-3.13.0a5+-cb4cc72 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 446 ms: 1.29x faster                                                             |
| async_tree_io_tg           | 1.18 sec                                               | 922 ms: 1.28x faster                                                             |
| async_tree_none_tg         | 450 ms                                                 | 352 ms: 1.28x faster                                                             |
| async_tree_io              | 1.16 sec                                               | 920 ms: 1.26x faster                                                             |
| async_tree_none            | 472 ms                                                 | 376 ms: 1.25x faster                                                             |
| async_tree_memoization     | 578 ms                                                 | 464 ms: 1.24x faster                                                             |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 599 ms: 1.21x faster                                                             |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 613 ms: 1.18x faster                                                             |
| Geometric mean             | (ref)                                                  | 1.25x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240326-linux-x86_64-faster%2dcpython-specialize_binary_fl-3.13.0a5+-cb4cc72 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 77.2 ms: 1.10x faster                                                            |
| nbody          | 97.0 ms                                                | 91.2 ms: 1.06x faster                                                            |
| pidigits       | 187 ms                                                 | 189 ms: 1.01x slower                                                             |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240326-linux-x86_64-faster%2dcpython-specialize_binary_fl-3.13.0a5+-cb4cc72 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 134 ms: 1.10x faster                                                             |
| regex_effbot   | 3.61 ms                                                | 3.69 ms: 1.02x slower                                                            |
| regex_dna      | 212 ms                                                 | 226 ms: 1.06x slower                                                             |
| regex_v8       | 23.1 ms                                                | 25.6 ms: 1.11x slower                                                            |
| Geometric mean | (ref)                                                  | 1.02x slower                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240326-linux-x86_64-faster%2dcpython-specialize_binary_fl-3.13.0a5+-cb4cc72 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pickle_pure_python   | 324 us                                                 | 302 us: 1.07x faster                                                             |
| tomli_loads          | 2.33 sec                                               | 2.21 sec: 1.06x faster                                                           |
| xml_etree_generate   | 89.2 ms                                                | 85.7 ms: 1.04x faster                                                            |
| unpickle_pure_python | 230 us                                                 | 221 us: 1.04x faster                                                             |
| xml_etree_process    | 61.7 ms                                                | 60.0 ms: 1.03x faster                                                            |
| pickle_dict          | 35.5 us                                                | 35.2 us: 1.01x faster                                                            |
| xml_etree_iterparse  | 107 ms                                                 | 108 ms: 1.01x slower                                                             |
| pickle               | 11.6 us                                                | 11.7 us: 1.01x slower                                                            |
| pickle_list          | 5.08 us                                                | 5.16 us: 1.02x slower                                                            |
| json_dumps           | 10.4 ms                                                | 10.7 ms: 1.03x slower                                                            |
| unpickle_list        | 5.29 us                                                | 5.50 us: 1.04x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                                     |

Benchmark hidden because not significant (3): json_loads, xml_etree_parse, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240326-linux-x86_64-faster%2dcpython-specialize_binary_fl-3.13.0a5+-cb4cc72 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 9.55 ms                                                | 10.6 ms: 1.11x slower                                                            |
| python_startup_no_site | 6.94 ms                                                | 8.95 ms: 1.29x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.20x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240326-linux-x86_64-faster%2dcpython-specialize_binary_fl-3.13.0a5+-cb4cc72 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako           | 11.9 ms                                                | 11.3 ms: 1.05x faster                                                            |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                     |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240326-linux-x86_64-faster%2dcpython-specialize_binary_fl-3.13.0a5+-cb4cc72 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| typing_runtime_protocols   | 158 us                                                 | 109 us: 1.45x faster                                                             |
| comprehensions             | 21.8 us                                                | 16.5 us: 1.32x faster                                                            |
| async_tree_memoization_tg  | 575 ms                                                 | 446 ms: 1.29x faster                                                             |
| async_tree_io_tg           | 1.18 sec                                               | 922 ms: 1.28x faster                                                             |
| async_tree_none_tg         | 450 ms                                                 | 352 ms: 1.28x faster                                                             |
| unpack_sequence            | 54.0 ns                                                | 42.3 ns: 1.28x faster                                                            |
| async_tree_io              | 1.16 sec                                               | 920 ms: 1.26x faster                                                             |
| async_tree_none            | 472 ms                                                 | 376 ms: 1.25x faster                                                             |
| async_tree_memoization     | 578 ms                                                 | 464 ms: 1.24x faster                                                             |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 599 ms: 1.21x faster                                                             |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 613 ms: 1.18x faster                                                             |
| raytrace                   | 312 ms                                                 | 267 ms: 1.17x faster                                                             |
| deltablue                  | 3.72 ms                                                | 3.25 ms: 1.14x faster                                                            |
| crypto_pyaes               | 81.9 ms                                                | 72.8 ms: 1.12x faster                                                            |
| mypy2                      | 830 ms                                                 | 741 ms: 1.12x faster                                                             |
| scimark_monte_carlo        | 75.1 ms                                                | 67.4 ms: 1.11x faster                                                            |
| chaos                      | 67.0 ms                                                | 60.4 ms: 1.11x faster                                                            |
| regex_compile              | 148 ms                                                 | 134 ms: 1.10x faster                                                             |
| sympy_sum                  | 169 ms                                                 | 153 ms: 1.10x faster                                                             |
| logging_format             | 7.23 us                                                | 6.56 us: 1.10x faster                                                            |
| float                      | 84.7 ms                                                | 77.2 ms: 1.10x faster                                                            |
| logging_simple             | 6.46 us                                                | 5.91 us: 1.09x faster                                                            |
| sympy_str                  | 300 ms                                                 | 276 ms: 1.09x faster                                                             |
| tornado_http               | 103 ms                                                 | 95.3 ms: 1.08x faster                                                            |
| pickle_pure_python         | 324 us                                                 | 302 us: 1.07x faster                                                             |
| sqlglot_parse              | 1.36 ms                                                | 1.27 ms: 1.07x faster                                                            |
| chameleon                  | 7.41 ms                                                | 6.94 ms: 1.07x faster                                                            |
| sqlglot_transpile          | 1.68 ms                                                | 1.58 ms: 1.07x faster                                                            |
| sympy_integrate            | 21.4 ms                                                | 20.1 ms: 1.07x faster                                                            |
| nbody                      | 97.0 ms                                                | 91.2 ms: 1.06x faster                                                            |
| pprint_safe_repr           | 776 ms                                                 | 731 ms: 1.06x faster                                                             |
| gc_traversal               | 3.79 ms                                                | 3.58 ms: 1.06x faster                                                            |
| tomli_loads                | 2.33 sec                                               | 2.21 sec: 1.06x faster                                                           |
| mako                       | 11.9 ms                                                | 11.3 ms: 1.05x faster                                                            |
| scimark_sor                | 129 ms                                                 | 123 ms: 1.05x faster                                                             |
| deepcopy_reduce            | 3.35 us                                                | 3.19 us: 1.05x faster                                                            |
| scimark_lu                 | 118 ms                                                 | 113 ms: 1.05x faster                                                             |
| generators                 | 31.2 ms                                                | 29.9 ms: 1.04x faster                                                            |
| async_generators           | 463 ms                                                 | 443 ms: 1.04x faster                                                             |
| deepcopy                   | 371 us                                                 | 356 us: 1.04x faster                                                             |
| pprint_pformat             | 1.57 sec                                               | 1.51 sec: 1.04x faster                                                           |
| scimark_fft                | 382 ms                                                 | 367 ms: 1.04x faster                                                             |
| deepcopy_memo              | 40.7 us                                                | 39.2 us: 1.04x faster                                                            |
| xml_etree_generate         | 89.2 ms                                                | 85.7 ms: 1.04x faster                                                            |
| unpickle_pure_python       | 230 us                                                 | 221 us: 1.04x faster                                                             |
| pathlib                    | 19.3 ms                                                | 18.7 ms: 1.04x faster                                                            |
| logging_silent             | 104 ns                                                 | 101 ns: 1.04x faster                                                             |
| fannkuch                   | 417 ms                                                 | 403 ms: 1.04x faster                                                             |
| nqueens                    | 83.3 ms                                                | 80.7 ms: 1.03x faster                                                            |
| sympy_expand               | 478 ms                                                 | 463 ms: 1.03x faster                                                             |
| xml_etree_process          | 61.7 ms                                                | 60.0 ms: 1.03x faster                                                            |
| meteor_contest             | 112 ms                                                 | 109 ms: 1.03x faster                                                             |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.93 ms: 1.03x faster                                                            |
| 2to3                       | 274 ms                                                 | 269 ms: 1.02x faster                                                             |
| spectral_norm              | 115 ms                                                 | 113 ms: 1.02x faster                                                             |
| sqlglot_normalize          | 110 ms                                                 | 109 ms: 1.01x faster                                                             |
| hexiom                     | 6.41 ms                                                | 6.33 ms: 1.01x faster                                                            |
| create_gc_cycles           | 1.48 ms                                                | 1.46 ms: 1.01x faster                                                            |
| bench_thread_pool          | 842 us                                                 | 833 us: 1.01x faster                                                             |
| pyflate                    | 482 ms                                                 | 478 ms: 1.01x faster                                                             |
| pickle_dict                | 35.5 us                                                | 35.2 us: 1.01x faster                                                            |
| coroutines                 | 23.2 ms                                                | 23.0 ms: 1.01x faster                                                            |
| dulwich_log                | 68.5 ms                                                | 68.0 ms: 1.01x faster                                                            |
| sqlglot_optimize           | 54.8 ms                                                | 55.0 ms: 1.00x slower                                                            |
| go                         | 139 ms                                                 | 140 ms: 1.00x slower                                                             |
| xml_etree_iterparse        | 107 ms                                                 | 108 ms: 1.01x slower                                                             |
| pidigits                   | 187 ms                                                 | 189 ms: 1.01x slower                                                             |
| pickle                     | 11.6 us                                                | 11.7 us: 1.01x slower                                                            |
| json                       | 5.26 ms                                                | 5.32 ms: 1.01x slower                                                            |
| pickle_list                | 5.08 us                                                | 5.16 us: 1.02x slower                                                            |
| regex_effbot               | 3.61 ms                                                | 3.69 ms: 1.02x slower                                                            |
| asyncio_websockets         | 551 ms                                                 | 565 ms: 1.03x slower                                                             |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.83 sec: 1.03x slower                                                           |
| json_dumps                 | 10.4 ms                                                | 10.7 ms: 1.03x slower                                                            |
| asyncio_tcp                | 491 ms                                                 | 505 ms: 1.03x slower                                                             |
| sqlite_synth               | 2.83 us                                                | 2.92 us: 1.03x slower                                                            |
| aiohttp                    | 1.15 ms                                                | 1.19 ms: 1.03x slower                                                            |
| gunicorn                   | 1.24 ms                                                | 1.28 ms: 1.03x slower                                                            |
| unpickle_list              | 5.29 us                                                | 5.50 us: 1.04x slower                                                            |
| mdp                        | 2.63 sec                                               | 2.78 sec: 1.06x slower                                                           |
| regex_dna                  | 212 ms                                                 | 226 ms: 1.06x slower                                                             |
| regex_v8                   | 23.1 ms                                                | 25.6 ms: 1.11x slower                                                            |
| python_startup             | 9.55 ms                                                | 10.6 ms: 1.11x slower                                                            |
| telco                      | 7.10 ms                                                | 8.55 ms: 1.20x slower                                                            |
| python_startup_no_site     | 6.94 ms                                                | 8.95 ms: 1.29x slower                                                            |
| coverage                   | 72.7 ms                                                | 96.4 ms: 1.33x slower                                                            |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                                     |

Benchmark hidden because not significant (10): dask, bench_mp_pool, docutils, django_template, json_loads, richards, pycparser, xml_etree_parse, richards_super, unpickle
Ignored benchmarks (2) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20240326-3.13.0a5+-cb4cc72/bm-20240326-linux-x86_64-faster%2dcpython-specialize_binary_fl-3.13.0a5+-cb4cc72.json: djangocms, genshi_text, genshi_xml, html5lib, pylint, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x


# Memory

- memory change: 0.95x