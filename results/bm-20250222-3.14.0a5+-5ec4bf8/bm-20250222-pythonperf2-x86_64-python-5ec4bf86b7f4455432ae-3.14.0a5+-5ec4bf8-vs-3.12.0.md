# Results vs. 3.12.0

- fork: python
- ref: 5ec4bf86b7f4455432ae
- machine: linux-x86_64
- commit hash: 5ec4bf8
- commit date: 2025-02-22
- overall geometric mean: 1.048x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250222-pythonperf2-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 284 ms: 1.00x faster                                                         |
| Geometric mean | (ref)                                                        | 1.00x faster                                                                 |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250222-pythonperf2-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 641 ms: 1.64x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 330 ms: 1.64x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 642 ms: 1.62x faster                                                         |
| async_tree_none            | 452 ms                                                       | 285 ms: 1.58x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 273 ms: 1.58x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 345 ms: 1.58x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 501 ms: 1.39x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 514 ms: 1.36x faster                                                         |
| Geometric mean             | (ref)                                                        | 1.55x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250222-pythonperf2-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 70.3 ms: 1.09x faster                                                        |
| pidigits       | 265 ms                                                       | 255 ms: 1.04x faster                                                         |
| nbody          | 88.0 ms                                                      | 93.0 ms: 1.06x slower                                                        |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250222-pythonperf2-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.09 ms: 1.15x faster                                                        |
| regex_compile  | 144 ms                                                       | 135 ms: 1.06x faster                                                         |
| regex_v8       | 23.6 ms                                                      | 25.3 ms: 1.07x slower                                                        |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                 |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250222-pythonperf2-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|---------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_iterparse | 103 ms                                                       | 95.8 ms: 1.07x faster                                                        |
| xml_etree_parse     | 144 ms                                                       | 136 ms: 1.06x faster                                                         |
| unpickle            | 14.8 us                                                      | 14.0 us: 1.05x faster                                                        |
| tomli_loads         | 2.16 sec                                                     | 2.06 sec: 1.05x faster                                                       |
| xml_etree_generate  | 86.1 ms                                                      | 82.8 ms: 1.04x faster                                                        |
| pickle_pure_python  | 318 us                                                       | 331 us: 1.04x slower                                                         |
| json_loads          | 24.4 us                                                      | 25.9 us: 1.06x slower                                                        |
| unpickle_list       | 4.66 us                                                      | 4.96 us: 1.07x slower                                                        |
| json_dumps          | 10.2 ms                                                      | 11.3 ms: 1.11x slower                                                        |
| pickle_dict         | 32.5 us                                                      | 36.2 us: 1.11x slower                                                        |
| pickle_list         | 4.43 us                                                      | 4.99 us: 1.13x slower                                                        |
| pickle              | 10.5 us                                                      | 12.1 us: 1.15x slower                                                        |
| Geometric mean      | (ref)                                                        | 1.03x slower                                                                 |

Benchmark hidden because not significant (2): unpickle_pure_python, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250222-pythonperf2-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.01 ms: 1.04x slower                                                        |
| python_startup         | 11.6 ms                                                      | 16.1 ms: 1.39x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.20x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250222-pythonperf2-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 36.0 ms: 1.06x faster                                                        |
| mako            | 10.0 ms                                                      | 10.7 ms: 1.07x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.00x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250222-pythonperf2-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 641 ms: 1.64x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 330 ms: 1.64x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 642 ms: 1.62x faster                                                         |
| async_tree_none            | 452 ms                                                       | 285 ms: 1.58x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 273 ms: 1.58x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 345 ms: 1.58x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 501 ms: 1.39x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 514 ms: 1.36x faster                                                         |
| generators                 | 37.4 ms                                                      | 28.1 ms: 1.33x faster                                                        |
| comprehensions             | 21.9 us                                                      | 17.1 us: 1.28x faster                                                        |
| deepcopy                   | 368 us                                                       | 290 us: 1.27x faster                                                         |
| deepcopy_memo              | 36.8 us                                                      | 29.5 us: 1.25x faster                                                        |
| regex_effbot               | 3.57 ms                                                      | 3.09 ms: 1.15x faster                                                        |
| deepcopy_reduce            | 3.37 us                                                      | 2.95 us: 1.14x faster                                                        |
| go                         | 150 ms                                                       | 132 ms: 1.14x faster                                                         |
| scimark_monte_carlo        | 69.0 ms                                                      | 61.2 ms: 1.13x faster                                                        |
| sqlalchemy_declarative     | 159 ms                                                       | 142 ms: 1.12x faster                                                         |
| pathlib                    | 18.9 ms                                                      | 16.9 ms: 1.12x faster                                                        |
| spectral_norm              | 91.6 ms                                                      | 83.8 ms: 1.09x faster                                                        |
| float                      | 76.6 ms                                                      | 70.3 ms: 1.09x faster                                                        |
| crypto_pyaes               | 80.3 ms                                                      | 73.8 ms: 1.09x faster                                                        |
| coroutines                 | 23.0 ms                                                      | 21.2 ms: 1.09x faster                                                        |
| raytrace                   | 298 ms                                                       | 275 ms: 1.08x faster                                                         |
| sympy_sum                  | 162 ms                                                       | 150 ms: 1.08x faster                                                         |
| xml_etree_iterparse        | 103 ms                                                       | 95.8 ms: 1.07x faster                                                        |
| unpack_sequence            | 53.2 ns                                                      | 49.7 ns: 1.07x faster                                                        |
| regex_compile              | 144 ms                                                       | 135 ms: 1.06x faster                                                         |
| logging_format             | 7.48 us                                                      | 7.04 us: 1.06x faster                                                        |
| sqlalchemy_imperative      | 18.7 ms                                                      | 17.6 ms: 1.06x faster                                                        |
| django_template            | 38.2 ms                                                      | 36.0 ms: 1.06x faster                                                        |
| chaos                      | 64.0 ms                                                      | 60.4 ms: 1.06x faster                                                        |
| xml_etree_parse            | 144 ms                                                       | 136 ms: 1.06x faster                                                         |
| unpickle                   | 14.8 us                                                      | 14.0 us: 1.05x faster                                                        |
| sympy_str                  | 302 ms                                                       | 287 ms: 1.05x faster                                                         |
| mdp                        | 2.57 sec                                                     | 2.45 sec: 1.05x faster                                                       |
| sympy_integrate            | 23.9 ms                                                      | 22.8 ms: 1.05x faster                                                        |
| tomli_loads                | 2.16 sec                                                     | 2.06 sec: 1.05x faster                                                       |
| logging_simple             | 6.71 us                                                      | 6.45 us: 1.04x faster                                                        |
| xml_etree_generate         | 86.1 ms                                                      | 82.8 ms: 1.04x faster                                                        |
| pidigits                   | 265 ms                                                       | 255 ms: 1.04x faster                                                         |
| pprint_pformat             | 1.65 sec                                                     | 1.60 sec: 1.03x faster                                                       |
| sqlglot_transpile          | 1.78 ms                                                      | 1.73 ms: 1.03x faster                                                        |
| sqlglot_parse              | 1.38 ms                                                      | 1.34 ms: 1.02x faster                                                        |
| meteor_contest             | 128 ms                                                       | 125 ms: 1.02x faster                                                         |
| pprint_safe_repr           | 807 ms                                                       | 789 ms: 1.02x faster                                                         |
| nqueens                    | 89.9 ms                                                      | 87.9 ms: 1.02x faster                                                        |
| pyflate                    | 439 ms                                                       | 430 ms: 1.02x faster                                                         |
| asyncio_tcp                | 378 ms                                                       | 372 ms: 1.01x faster                                                         |
| sqlglot_normalize          | 116 ms                                                       | 114 ms: 1.01x faster                                                         |
| scimark_lu                 | 98.8 ms                                                      | 98.1 ms: 1.01x faster                                                        |
| sqlglot_optimize           | 57.5 ms                                                      | 57.2 ms: 1.01x faster                                                        |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.58 sec: 1.00x faster                                                       |
| 2to3                       | 285 ms                                                       | 284 ms: 1.00x faster                                                         |
| sympy_expand               | 484 ms                                                       | 487 ms: 1.01x slower                                                         |
| richards_super             | 51.3 ms                                                      | 51.8 ms: 1.01x slower                                                        |
| pycparser                  | 1.23 sec                                                     | 1.25 sec: 1.01x slower                                                       |
| logging_silent             | 94.4 ns                                                      | 96.4 ns: 1.02x slower                                                        |
| deltablue                  | 3.24 ms                                                      | 3.31 ms: 1.02x slower                                                        |
| fannkuch                   | 350 ms                                                       | 358 ms: 1.02x slower                                                         |
| dulwich_log                | 65.4 ms                                                      | 67.2 ms: 1.03x slower                                                        |
| hexiom                     | 5.96 ms                                                      | 6.13 ms: 1.03x slower                                                        |
| scimark_sor                | 109 ms                                                       | 113 ms: 1.03x slower                                                         |
| scimark_fft                | 301 ms                                                       | 312 ms: 1.04x slower                                                         |
| pickle_pure_python         | 318 us                                                       | 331 us: 1.04x slower                                                         |
| json                       | 5.12 ms                                                      | 5.33 ms: 1.04x slower                                                        |
| python_startup_no_site     | 8.64 ms                                                      | 9.01 ms: 1.04x slower                                                        |
| async_generators           | 390 ms                                                       | 412 ms: 1.06x slower                                                         |
| nbody                      | 88.0 ms                                                      | 93.0 ms: 1.06x slower                                                        |
| json_loads                 | 24.4 us                                                      | 25.9 us: 1.06x slower                                                        |
| unpickle_list              | 4.66 us                                                      | 4.96 us: 1.07x slower                                                        |
| mako                       | 10.0 ms                                                      | 10.7 ms: 1.07x slower                                                        |
| regex_v8                   | 23.6 ms                                                      | 25.3 ms: 1.07x slower                                                        |
| json_dumps                 | 10.2 ms                                                      | 11.3 ms: 1.11x slower                                                        |
| pickle_dict                | 32.5 us                                                      | 36.2 us: 1.11x slower                                                        |
| pickle_list                | 4.43 us                                                      | 4.99 us: 1.13x slower                                                        |
| typing_runtime_protocols   | 152 us                                                       | 172 us: 1.14x slower                                                         |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.78 ms: 1.14x slower                                                        |
| telco                      | 6.96 ms                                                      | 7.95 ms: 1.14x slower                                                        |
| pickle                     | 10.5 us                                                      | 12.1 us: 1.15x slower                                                        |
| coverage                   | 66.7 ms                                                      | 78.9 ms: 1.18x slower                                                        |
| python_startup             | 11.6 ms                                                      | 16.1 ms: 1.39x slower                                                        |
| create_gc_cycles           | 1.59 ms                                                      | 2.79 ms: 1.75x slower                                                        |
| gc_traversal               | 3.48 ms                                                      | 6.32 ms: 1.82x slower                                                        |
| bench_mp_pool              | 4.76 ms                                                      | 854 ms: 179.20x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.02x slower                                                                 |

Benchmark hidden because not significant (8): bench_thread_pool, docutils, asyncio_websockets, regex_dna, unpickle_pure_python, xml_etree_process, sqlite_synth, richards
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, tornado_http
Ignored benchmarks (12) of results/bm-20250222-3.14.0a5+-5ec4bf8/bm-20250222-pythonperf2-x86_64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.048x faster

# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x