# Results vs. 3.12.0

- fork: faster-cpython
- ref: bound_method_instrum
- machine: windows-amd64
- commit hash: 5787d3e
- commit date: 2024-07-23
- overall geometric mean: 1.00x slower
- HPT reliability: 98.85%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240723-pythonperf1-amd64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 218 ms                                                      | 227 ms: 1.04x slower                                                                 |
| docutils       | 1.66 sec                                                    | 1.69 sec: 1.02x slower                                                               |
| tornado_http   | 89.5 ms                                                     | 91.6 ms: 1.02x slower                                                                |
| Geometric mean | (ref)                                                       | 1.03x slower                                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240723-pythonperf1-amd64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 245 ms: 1.49x faster                                                                 |
| async_tree_none_tg         | 285 ms                                                      | 193 ms: 1.48x faster                                                                 |
| async_tree_io_tg           | 771 ms                                                      | 533 ms: 1.45x faster                                                                 |
| async_tree_none            | 291 ms                                                      | 214 ms: 1.36x faster                                                                 |
| async_tree_io              | 731 ms                                                      | 547 ms: 1.34x faster                                                                 |
| async_tree_memoization     | 339 ms                                                      | 258 ms: 1.32x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 387 ms: 1.30x faster                                                                 |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 382 ms: 1.28x faster                                                                 |
| Geometric mean             | (ref)                                                       | 1.37x faster                                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240723-pythonperf1-amd64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| pidigits       | 152 ms                                                      | 151 ms: 1.01x faster                                                                 |
| float          | 56.8 ms                                                     | 56.3 ms: 1.01x faster                                                                |
| nbody          | 71.9 ms                                                     | 83.8 ms: 1.17x slower                                                                |
| Geometric mean | (ref)                                                       | 1.05x slower                                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240723-pythonperf1-amd64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_dna      | 126 ms                                                      | 120 ms: 1.05x faster                                                                 |
| regex_effbot   | 1.62 ms                                                     | 1.60 ms: 1.01x faster                                                                |
| regex_v8       | 14.2 ms                                                     | 14.6 ms: 1.02x slower                                                                |
| regex_compile  | 87.5 ms                                                     | 90.4 ms: 1.03x slower                                                                |
| Geometric mean | (ref)                                                       | 1.00x faster                                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240723-pythonperf1-amd64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| xml_etree_parse      | 93.0 ms                                                     | 91.9 ms: 1.01x faster                                                                |
| json_loads           | 13.9 us                                                     | 14.0 us: 1.00x slower                                                                |
| xml_etree_iterparse  | 65.2 ms                                                     | 66.3 ms: 1.02x slower                                                                |
| xml_etree_generate   | 55.8 ms                                                     | 58.1 ms: 1.04x slower                                                                |
| json_dumps           | 5.70 ms                                                     | 6.00 ms: 1.05x slower                                                                |
| pickle_pure_python   | 195 us                                                      | 209 us: 1.07x slower                                                                 |
| xml_etree_process    | 37.7 ms                                                     | 40.6 ms: 1.08x slower                                                                |
| unpickle_pure_python | 133 us                                                      | 150 us: 1.13x slower                                                                 |
| tomli_loads          | 1.37 sec                                                    | 1.57 sec: 1.15x slower                                                               |
| Geometric mean       | (ref)                                                       | 1.06x slower                                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240723-pythonperf1-amd64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup_no_site | 16.2 ms                                                     | 17.6 ms: 1.08x slower                                                                |
| python_startup         | 19.5 ms                                                     | 21.7 ms: 1.11x slower                                                                |
| Geometric mean         | (ref)                                                       | 1.10x slower                                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240723-pythonperf1-amd64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| django_template | 22.9 ms                                                     | 23.7 ms: 1.04x slower                                                                |
| mako            | 7.09 ms                                                     | 7.48 ms: 1.06x slower                                                                |
| Geometric mean  | (ref)                                                       | 1.05x slower                                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240723-pythonperf1-amd64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 367 ms                                                      | 245 ms: 1.49x faster                                                                 |
| async_tree_none_tg         | 285 ms                                                      | 193 ms: 1.48x faster                                                                 |
| async_tree_io_tg           | 771 ms                                                      | 533 ms: 1.45x faster                                                                 |
| async_tree_none            | 291 ms                                                      | 214 ms: 1.36x faster                                                                 |
| async_tree_io              | 731 ms                                                      | 547 ms: 1.34x faster                                                                 |
| async_tree_memoization     | 339 ms                                                      | 258 ms: 1.32x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 502 ms                                                      | 387 ms: 1.30x faster                                                                 |
| deepcopy                   | 238 us                                                      | 184 us: 1.29x faster                                                                 |
| async_tree_cpu_io_mixed    | 489 ms                                                      | 382 ms: 1.28x faster                                                                 |
| comprehensions             | 14.1 us                                                     | 11.6 us: 1.21x faster                                                                |
| asyncio_tcp_ssl            | 2.10 sec                                                    | 1.79 sec: 1.17x faster                                                               |
| deepcopy_reduce            | 2.09 us                                                     | 1.89 us: 1.11x faster                                                                |
| deepcopy_memo              | 23.7 us                                                     | 21.7 us: 1.09x faster                                                                |
| raytrace                   | 192 ms                                                      | 179 ms: 1.07x faster                                                                 |
| generators                 | 22.5 ms                                                     | 21.2 ms: 1.06x faster                                                                |
| bench_thread_pool          | 857 us                                                      | 806 us: 1.06x faster                                                                 |
| coroutines                 | 14.3 ms                                                     | 13.5 ms: 1.06x faster                                                                |
| regex_dna                  | 126 ms                                                      | 120 ms: 1.05x faster                                                                 |
| json                       | 3.05 ms                                                     | 2.93 ms: 1.04x faster                                                                |
| bench_mp_pool              | 69.2 ms                                                     | 67.3 ms: 1.03x faster                                                                |
| sympy_sum                  | 91.5 ms                                                     | 89.3 ms: 1.02x faster                                                                |
| sqlglot_normalize          | 187 ms                                                      | 184 ms: 1.02x faster                                                                 |
| logging_simple             | 6.28 us                                                     | 6.20 us: 1.01x faster                                                                |
| regex_effbot               | 1.62 ms                                                     | 1.60 ms: 1.01x faster                                                                |
| xml_etree_parse            | 93.0 ms                                                     | 91.9 ms: 1.01x faster                                                                |
| pidigits                   | 152 ms                                                      | 151 ms: 1.01x faster                                                                 |
| float                      | 56.8 ms                                                     | 56.3 ms: 1.01x faster                                                                |
| logging_format             | 6.72 us                                                     | 6.68 us: 1.00x faster                                                                |
| sympy_str                  | 175 ms                                                      | 174 ms: 1.00x faster                                                                 |
| json_loads                 | 13.9 us                                                     | 14.0 us: 1.00x slower                                                                |
| sympy_integrate            | 13.0 ms                                                     | 13.0 ms: 1.00x slower                                                                |
| nqueens                    | 62.8 ms                                                     | 63.2 ms: 1.01x slower                                                                |
| meteor_contest             | 74.6 ms                                                     | 75.6 ms: 1.01x slower                                                                |
| docutils                   | 1.66 sec                                                    | 1.69 sec: 1.02x slower                                                               |
| xml_etree_iterparse        | 65.2 ms                                                     | 66.3 ms: 1.02x slower                                                                |
| gc_traversal               | 1.52 ms                                                     | 1.55 ms: 1.02x slower                                                                |
| regex_v8                   | 14.2 ms                                                     | 14.6 ms: 1.02x slower                                                                |
| async_generators           | 239 ms                                                      | 245 ms: 1.02x slower                                                                 |
| tornado_http               | 89.5 ms                                                     | 91.6 ms: 1.02x slower                                                                |
| deltablue                  | 2.16 ms                                                     | 2.21 ms: 1.02x slower                                                                |
| mdp                        | 1.37 sec                                                    | 1.40 sec: 1.02x slower                                                               |
| chaos                      | 43.3 ms                                                     | 44.5 ms: 1.03x slower                                                                |
| regex_compile              | 87.5 ms                                                     | 90.4 ms: 1.03x slower                                                                |
| django_template            | 22.9 ms                                                     | 23.7 ms: 1.04x slower                                                                |
| crypto_pyaes               | 48.5 ms                                                     | 50.2 ms: 1.04x slower                                                                |
| logging_silent             | 60.5 ns                                                     | 62.6 ns: 1.04x slower                                                                |
| 2to3                       | 218 ms                                                      | 227 ms: 1.04x slower                                                                 |
| xml_etree_generate         | 55.8 ms                                                     | 58.1 ms: 1.04x slower                                                                |
| go                         | 91.6 ms                                                     | 95.5 ms: 1.04x slower                                                                |
| sympy_expand               | 284 ms                                                      | 298 ms: 1.05x slower                                                                 |
| json_dumps                 | 5.70 ms                                                     | 6.00 ms: 1.05x slower                                                                |
| mako                       | 7.09 ms                                                     | 7.48 ms: 1.06x slower                                                                |
| pickle_pure_python         | 195 us                                                      | 209 us: 1.07x slower                                                                 |
| pyflate                    | 295 ms                                                      | 316 ms: 1.07x slower                                                                 |
| sqlglot_transpile          | 1.02 ms                                                     | 1.10 ms: 1.08x slower                                                                |
| xml_etree_process          | 37.7 ms                                                     | 40.6 ms: 1.08x slower                                                                |
| python_startup_no_site     | 16.2 ms                                                     | 17.6 ms: 1.08x slower                                                                |
| hexiom                     | 4.10 ms                                                     | 4.46 ms: 1.09x slower                                                                |
| richards_super             | 32.1 ms                                                     | 35.1 ms: 1.09x slower                                                                |
| asyncio_tcp                | 487 ms                                                      | 533 ms: 1.09x slower                                                                 |
| pprint_pformat             | 1.05 sec                                                    | 1.15 sec: 1.10x slower                                                               |
| pprint_safe_repr           | 513 ms                                                      | 563 ms: 1.10x slower                                                                 |
| spectral_norm              | 66.9 ms                                                     | 73.5 ms: 1.10x slower                                                                |
| richards                   | 28.4 ms                                                     | 31.4 ms: 1.11x slower                                                                |
| sqlglot_parse              | 804 us                                                      | 893 us: 1.11x slower                                                                 |
| python_startup             | 19.5 ms                                                     | 21.7 ms: 1.11x slower                                                                |
| pycparser                  | 699 ms                                                      | 781 ms: 1.12x slower                                                                 |
| scimark_lu                 | 58.9 ms                                                     | 65.9 ms: 1.12x slower                                                                |
| unpickle_pure_python       | 133 us                                                      | 150 us: 1.13x slower                                                                 |
| scimark_sparse_mat_mult    | 2.56 ms                                                     | 2.90 ms: 1.13x slower                                                                |
| typing_runtime_protocols   | 95.1 us                                                     | 108 us: 1.13x slower                                                                 |
| scimark_monte_carlo        | 43.7 ms                                                     | 50.1 ms: 1.15x slower                                                                |
| tomli_loads                | 1.37 sec                                                    | 1.57 sec: 1.15x slower                                                               |
| scimark_sor                | 78.8 ms                                                     | 90.9 ms: 1.15x slower                                                                |
| coverage                   | 40.8 ms                                                     | 47.4 ms: 1.16x slower                                                                |
| nbody                      | 71.9 ms                                                     | 83.8 ms: 1.17x slower                                                                |
| telco                      | 4.13 ms                                                     | 4.87 ms: 1.18x slower                                                                |
| scimark_fft                | 184 ms                                                      | 219 ms: 1.19x slower                                                                 |
| create_gc_cycles           | 752 us                                                      | 903 us: 1.20x slower                                                                 |
| fannkuch                   | 247 ms                                                      | 300 ms: 1.22x slower                                                                 |
| Geometric mean             | (ref)                                                       | 1.00x slower                                                                         |

Benchmark hidden because not significant (2): pathlib, sqlglot_optimize
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1-amd64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240723-3.14.0a0-5787d3e/bm-20240723-pythonperf1-amd64-faster%2dcpython-bound_method_instrum-3.14.0a0-5787d3e.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 98.85% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown