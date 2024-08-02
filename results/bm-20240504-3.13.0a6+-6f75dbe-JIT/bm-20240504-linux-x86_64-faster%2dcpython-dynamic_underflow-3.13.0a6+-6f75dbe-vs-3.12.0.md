# Results vs. 3.12.0

- fork: faster-cpython
- ref: dynamic_underflow
- machine: linux-x86_64
- commit hash: 6f75dbe
- commit date: 2024-05-04
- overall geometric mean: 1.02x faster
- HPT reliability: 86.98%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240504-linux-x86_64-faster%2dcpython-dynamic_underflow-3.13.0a6+-6f75dbe |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 285 ms: 1.04x slower                                                          |
| chameleon      | 7.41 ms                                                | 7.31 ms: 1.01x faster                                                         |
| tornado_http   | 103 ms                                                 | 105 ms: 1.02x slower                                                          |
| Geometric mean | (ref)                                                  | 1.02x slower                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240504-linux-x86_64-faster%2dcpython-dynamic_underflow-3.13.0a6+-6f75dbe |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 354 ms: 1.27x faster                                                          |
| async_tree_none            | 472 ms                                                 | 371 ms: 1.27x faster                                                          |
| async_tree_memoization_tg  | 575 ms                                                 | 453 ms: 1.27x faster                                                          |
| async_tree_io              | 1.16 sec                                               | 931 ms: 1.24x faster                                                          |
| async_tree_io_tg           | 1.18 sec                                               | 968 ms: 1.22x faster                                                          |
| async_tree_memoization     | 578 ms                                                 | 474 ms: 1.22x faster                                                          |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 615 ms: 1.18x faster                                                          |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 639 ms: 1.14x faster                                                          |
| Geometric mean             | (ref)                                                  | 1.22x faster                                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240504-linux-x86_64-faster%2dcpython-dynamic_underflow-3.13.0a6+-6f75dbe |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 79.6 ms: 1.22x faster                                                         |
| float          | 84.7 ms                                                | 73.2 ms: 1.16x faster                                                         |
| pidigits       | 187 ms                                                 | 189 ms: 1.01x slower                                                          |
| Geometric mean | (ref)                                                  | 1.12x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240504-linux-x86_64-faster%2dcpython-dynamic_underflow-3.13.0a6+-6f75dbe |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 143 ms: 1.04x faster                                                          |
| regex_effbot   | 3.61 ms                                                | 3.71 ms: 1.03x slower                                                         |
| regex_dna      | 212 ms                                                 | 227 ms: 1.07x slower                                                          |
| regex_v8       | 23.1 ms                                                | 25.2 ms: 1.09x slower                                                         |
| Geometric mean | (ref)                                                  | 1.04x slower                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240504-linux-x86_64-faster%2dcpython-dynamic_underflow-3.13.0a6+-6f75dbe |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.02 sec: 1.16x faster                                                        |
| unpickle_pure_python | 230 us                                                 | 209 us: 1.10x faster                                                          |
| pickle_pure_python   | 324 us                                                 | 299 us: 1.08x faster                                                          |
| xml_etree_parse      | 159 ms                                                 | 149 ms: 1.07x faster                                                          |
| xml_etree_generate   | 89.2 ms                                                | 83.9 ms: 1.06x faster                                                         |
| xml_etree_process    | 61.7 ms                                                | 58.4 ms: 1.06x faster                                                         |
| xml_etree_iterparse  | 107 ms                                                 | 101 ms: 1.05x faster                                                          |
| json_loads           | 28.5 us                                                | 27.6 us: 1.03x faster                                                         |
| pickle_list          | 5.08 us                                                | 4.92 us: 1.03x faster                                                         |
| unpickle             | 15.9 us                                                | 15.5 us: 1.02x faster                                                         |
| json_dumps           | 10.4 ms                                                | 10.2 ms: 1.02x faster                                                         |
| pickle_dict          | 35.5 us                                                | 35.0 us: 1.02x faster                                                         |
| unpickle_list        | 5.29 us                                                | 5.26 us: 1.01x faster                                                         |
| pickle               | 11.6 us                                                | 11.9 us: 1.03x slower                                                         |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240504-linux-x86_64-faster%2dcpython-dynamic_underflow-3.13.0a6+-6f75dbe |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.65 ms: 1.10x slower                                                         |
| python_startup         | 9.55 ms                                                | 11.1 ms: 1.17x slower                                                         |
| Geometric mean         | (ref)                                                  | 1.13x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240504-linux-x86_64-faster%2dcpython-dynamic_underflow-3.13.0a6+-6f75dbe |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 9.66 ms: 1.23x faster                                                         |
| django_template | 34.6 ms                                                | 36.7 ms: 1.06x slower                                                         |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240504-linux-x86_64-faster%2dcpython-dynamic_underflow-3.13.0a6+-6f75dbe |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| comprehensions             | 21.8 us                                                | 16.6 us: 1.31x faster                                                         |
| async_tree_none_tg         | 450 ms                                                 | 354 ms: 1.27x faster                                                          |
| async_tree_none            | 472 ms                                                 | 371 ms: 1.27x faster                                                          |
| async_tree_memoization_tg  | 575 ms                                                 | 453 ms: 1.27x faster                                                          |
| async_tree_io              | 1.16 sec                                               | 931 ms: 1.24x faster                                                          |
| mako                       | 11.9 ms                                                | 9.66 ms: 1.23x faster                                                         |
| async_tree_io_tg           | 1.18 sec                                               | 968 ms: 1.22x faster                                                          |
| scimark_monte_carlo        | 75.1 ms                                                | 61.6 ms: 1.22x faster                                                         |
| async_tree_memoization     | 578 ms                                                 | 474 ms: 1.22x faster                                                          |
| nbody                      | 97.0 ms                                                | 79.6 ms: 1.22x faster                                                         |
| scimark_fft                | 382 ms                                                 | 322 ms: 1.19x faster                                                          |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 615 ms: 1.18x faster                                                          |
| crypto_pyaes               | 81.9 ms                                                | 69.7 ms: 1.17x faster                                                         |
| chaos                      | 67.0 ms                                                | 57.5 ms: 1.16x faster                                                         |
| float                      | 84.7 ms                                                | 73.2 ms: 1.16x faster                                                         |
| tomli_loads                | 2.33 sec                                               | 2.02 sec: 1.16x faster                                                        |
| raytrace                   | 312 ms                                                 | 273 ms: 1.14x faster                                                          |
| spectral_norm              | 115 ms                                                 | 101 ms: 1.14x faster                                                          |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 639 ms: 1.14x faster                                                          |
| fannkuch                   | 417 ms                                                 | 371 ms: 1.12x faster                                                          |
| unpickle_pure_python       | 230 us                                                 | 209 us: 1.10x faster                                                          |
| logging_format             | 7.23 us                                                | 6.58 us: 1.10x faster                                                         |
| logging_simple             | 6.46 us                                                | 5.92 us: 1.09x faster                                                         |
| pathlib                    | 19.3 ms                                                | 17.8 ms: 1.09x faster                                                         |
| pickle_pure_python         | 324 us                                                 | 299 us: 1.08x faster                                                          |
| pyflate                    | 482 ms                                                 | 447 ms: 1.08x faster                                                          |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.71 ms: 1.07x faster                                                         |
| deepcopy_memo              | 40.7 us                                                | 38.1 us: 1.07x faster                                                         |
| xml_etree_parse            | 159 ms                                                 | 149 ms: 1.07x faster                                                          |
| logging_silent             | 104 ns                                                 | 98.0 ns: 1.07x faster                                                         |
| xml_etree_generate         | 89.2 ms                                                | 83.9 ms: 1.06x faster                                                         |
| xml_etree_process          | 61.7 ms                                                | 58.4 ms: 1.06x faster                                                         |
| xml_etree_iterparse        | 107 ms                                                 | 101 ms: 1.05x faster                                                          |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                                          |
| regex_compile              | 148 ms                                                 | 143 ms: 1.04x faster                                                          |
| sqlglot_parse              | 1.36 ms                                                | 1.31 ms: 1.04x faster                                                         |
| json_loads                 | 28.5 us                                                | 27.6 us: 1.03x faster                                                         |
| pprint_safe_repr           | 776 ms                                                 | 751 ms: 1.03x faster                                                          |
| pickle_list                | 5.08 us                                                | 4.92 us: 1.03x faster                                                         |
| deepcopy_reduce            | 3.35 us                                                | 3.24 us: 1.03x faster                                                         |
| generators                 | 31.2 ms                                                | 30.3 ms: 1.03x faster                                                         |
| json                       | 5.26 ms                                                | 5.11 ms: 1.03x faster                                                         |
| unpickle                   | 15.9 us                                                | 15.5 us: 1.02x faster                                                         |
| json_dumps                 | 10.4 ms                                                | 10.2 ms: 1.02x faster                                                         |
| pickle_dict                | 35.5 us                                                | 35.0 us: 1.02x faster                                                         |
| pprint_pformat             | 1.57 sec                                               | 1.55 sec: 1.01x faster                                                        |
| mdp                        | 2.63 sec                                               | 2.59 sec: 1.01x faster                                                        |
| chameleon                  | 7.41 ms                                                | 7.31 ms: 1.01x faster                                                         |
| deepcopy                   | 371 us                                                 | 367 us: 1.01x faster                                                          |
| unpickle_list              | 5.29 us                                                | 5.26 us: 1.01x faster                                                         |
| sqlglot_transpile          | 1.68 ms                                                | 1.70 ms: 1.01x slower                                                         |
| pidigits                   | 187 ms                                                 | 189 ms: 1.01x slower                                                          |
| nqueens                    | 83.3 ms                                                | 84.7 ms: 1.02x slower                                                         |
| gc_traversal               | 3.79 ms                                                | 3.86 ms: 1.02x slower                                                         |
| tornado_http               | 103 ms                                                 | 105 ms: 1.02x slower                                                          |
| pickle                     | 11.6 us                                                | 11.9 us: 1.03x slower                                                         |
| regex_effbot               | 3.61 ms                                                | 3.71 ms: 1.03x slower                                                         |
| asyncio_websockets         | 551 ms                                                 | 567 ms: 1.03x slower                                                          |
| dask                       | 372 ms                                                 | 383 ms: 1.03x slower                                                          |
| hexiom                     | 6.41 ms                                                | 6.64 ms: 1.04x slower                                                         |
| 2to3                       | 274 ms                                                 | 285 ms: 1.04x slower                                                          |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.86 sec: 1.04x slower                                                        |
| go                         | 139 ms                                                 | 146 ms: 1.05x slower                                                          |
| bench_thread_pool          | 842 us                                                 | 882 us: 1.05x slower                                                          |
| sympy_str                  | 300 ms                                                 | 317 ms: 1.06x slower                                                          |
| coroutines                 | 23.2 ms                                                | 24.5 ms: 1.06x slower                                                         |
| django_template            | 34.6 ms                                                | 36.7 ms: 1.06x slower                                                         |
| sqlglot_optimize           | 54.8 ms                                                | 58.2 ms: 1.06x slower                                                         |
| regex_dna                  | 212 ms                                                 | 227 ms: 1.07x slower                                                          |
| asyncio_tcp                | 491 ms                                                 | 530 ms: 1.08x slower                                                          |
| sqlglot_normalize          | 110 ms                                                 | 119 ms: 1.08x slower                                                          |
| dulwich_log                | 68.5 ms                                                | 74.4 ms: 1.09x slower                                                         |
| sympy_sum                  | 169 ms                                                 | 184 ms: 1.09x slower                                                          |
| regex_v8                   | 23.1 ms                                                | 25.2 ms: 1.09x slower                                                         |
| scimark_lu                 | 118 ms                                                 | 129 ms: 1.09x slower                                                          |
| scimark_sor                | 129 ms                                                 | 142 ms: 1.10x slower                                                          |
| typing_runtime_protocols   | 158 us                                                 | 174 us: 1.10x slower                                                          |
| sympy_integrate            | 21.4 ms                                                | 23.6 ms: 1.10x slower                                                         |
| python_startup_no_site     | 6.94 ms                                                | 7.65 ms: 1.10x slower                                                         |
| sympy_expand               | 478 ms                                                 | 528 ms: 1.10x slower                                                          |
| mypy2                      | 830 ms                                                 | 926 ms: 1.12x slower                                                          |
| deltablue                  | 3.72 ms                                                | 4.21 ms: 1.13x slower                                                         |
| aiohttp                    | 1.15 ms                                                | 1.31 ms: 1.14x slower                                                         |
| gunicorn                   | 1.24 ms                                                | 1.43 ms: 1.15x slower                                                         |
| telco                      | 7.10 ms                                                | 8.18 ms: 1.15x slower                                                         |
| python_startup             | 9.55 ms                                                | 11.1 ms: 1.17x slower                                                         |
| coverage                   | 72.7 ms                                                | 87.4 ms: 1.20x slower                                                         |
| create_gc_cycles           | 1.48 ms                                                | 1.85 ms: 1.25x slower                                                         |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                                  |

Benchmark hidden because not significant (6): bench_mp_pool, richards_super, richards, async_generators, pycparser, sqlite_synth
Ignored benchmarks (4) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: docutils, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (7) of results/bm-20240504-3.13.0a6+-6f75dbe-JIT/bm-20240504-linux-x86_64-faster%2dcpython-dynamic_underflow-3.13.0a6+-6f75dbe.json: djangocms, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 86.98% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.07x