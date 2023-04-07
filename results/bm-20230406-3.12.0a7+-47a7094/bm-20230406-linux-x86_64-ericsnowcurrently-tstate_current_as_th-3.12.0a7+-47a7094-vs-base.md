
# Results vs. base

- fork: ericsnowcurrently
- ref: tstate_current_as_th
- machine: linux-x86_64
- commit hash: 47a7094
- commit date: 2023-04-06
- overall geometric mean: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230406-linux-x86_64-python-52bc2e7b9d451821513a-3.12.0a7+-52bc2e7 | bm-20230406-linux-x86_64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-47a7094 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| chameleon      | 6.34 ms                                                                | 6.42 ms: 1.01x slower                                                             |
| tornado_http   | 90.9 ms                                                                | 90.3 ms: 1.01x faster                                                             |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                                      |

Benchmark hidden because not significant (3): 2to3, docutils, html5lib

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230406-linux-x86_64-python-52bc2e7b9d451821513a-3.12.0a7+-52bc2e7 | bm-20230406-linux-x86_64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-47a7094 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| nbody          | 87.5 ms                                                                | 83.6 ms: 1.05x faster                                                             |
| float          | 73.0 ms                                                                | 72.6 ms: 1.01x faster                                                             |
| pidigits       | 188 ms                                                                 | 188 ms: 1.00x slower                                                              |
| Geometric mean | (ref)                                                                  | 1.02x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230406-linux-x86_64-python-52bc2e7b9d451821513a-3.12.0a7+-52bc2e7 | bm-20230406-linux-x86_64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-47a7094 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 133 ms                                                                 | 132 ms: 1.01x faster                                                              |
| regex_v8       | 22.4 ms                                                                | 22.6 ms: 1.01x slower                                                             |
| regex_dna      | 204 ms                                                                 | 214 ms: 1.05x slower                                                              |
| regex_effbot   | 3.43 ms                                                                | 3.63 ms: 1.06x slower                                                             |
| Geometric mean | (ref)                                                                  | 1.03x slower                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20230406-linux-x86_64-python-52bc2e7b9d451821513a-3.12.0a7+-52bc2e7 | bm-20230406-linux-x86_64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-47a7094 |
|--------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| unpickle_list      | 5.03 us                                                                | 4.87 us: 1.03x faster                                                             |
| unpickle           | 13.9 us                                                                | 13.6 us: 1.02x faster                                                             |
| xml_etree_process  | 55.3 ms                                                                | 55.0 ms: 1.00x faster                                                             |
| json_dumps         | 9.40 ms                                                                | 9.46 ms: 1.01x slower                                                             |
| json_loads         | 24.0 us                                                                | 24.5 us: 1.02x slower                                                             |
| pickle_pure_python | 285 us                                                                 | 292 us: 1.02x slower                                                              |
| pickle_list        | 4.22 us                                                                | 4.43 us: 1.05x slower                                                             |
| pickle_dict        | 30.6 us                                                                | 32.3 us: 1.05x slower                                                             |
| Geometric mean     | (ref)                                                                  | 1.01x slower                                                                      |

Benchmark hidden because not significant (5): unpickle_pure_python, xml_etree_parse, xml_etree_generate, pickle, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230406-linux-x86_64-python-52bc2e7b9d451821513a-3.12.0a7+-52bc2e7 | bm-20230406-linux-x86_64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-47a7094 |
|------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup_no_site | 6.50 ms                                                                | 6.55 ms: 1.01x slower                                                             |
| python_startup         | 8.79 ms                                                                | 8.87 ms: 1.01x slower                                                             |
| Geometric mean         | (ref)                                                                  | 1.01x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20230406-linux-x86_64-python-52bc2e7b9d451821513a-3.12.0a7+-52bc2e7 | bm-20230406-linux-x86_64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-47a7094 |
|-----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| genshi_text     | 21.7 ms                                                                | 21.1 ms: 1.03x faster                                                             |
| django_template | 32.6 ms                                                                | 32.0 ms: 1.02x faster                                                             |
| mako            | 10.0 ms                                                                | 9.99 ms: 1.00x faster                                                             |
| Geometric mean  | (ref)                                                                  | 1.01x faster                                                                      |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark               | bm-20230406-linux-x86_64-python-52bc2e7b9d451821513a-3.12.0a7+-52bc2e7 | bm-20230406-linux-x86_64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-47a7094 |
|-------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| nbody                   | 87.5 ms                                                                | 83.6 ms: 1.05x faster                                                             |
| pprint_safe_repr        | 696 ms                                                                 | 671 ms: 1.04x faster                                                              |
| coroutines              | 23.8 ms                                                                | 22.9 ms: 1.04x faster                                                             |
| unpack_sequence         | 43.6 ns                                                                | 42.1 ns: 1.04x faster                                                             |
| richards                | 44.5 ms                                                                | 43.1 ms: 1.03x faster                                                             |
| unpickle_list           | 5.03 us                                                                | 4.87 us: 1.03x faster                                                             |
| genshi_text             | 21.7 ms                                                                | 21.1 ms: 1.03x faster                                                             |
| pprint_pformat          | 1.42 sec                                                               | 1.39 sec: 1.03x faster                                                            |
| unpickle                | 13.9 us                                                                | 13.6 us: 1.02x faster                                                             |
| spectral_norm           | 95.2 ms                                                                | 93.2 ms: 1.02x faster                                                             |
| async_tree_memoization  | 617 ms                                                                 | 605 ms: 1.02x faster                                                              |
| meteor_contest          | 103 ms                                                                 | 101 ms: 1.02x faster                                                              |
| chaos                   | 65.8 ms                                                                | 64.7 ms: 1.02x faster                                                             |
| django_template         | 32.6 ms                                                                | 32.0 ms: 1.02x faster                                                             |
| comprehensions          | 21.8 us                                                                | 21.4 us: 1.02x faster                                                             |
| async_generators        | 416 ms                                                                 | 409 ms: 1.02x faster                                                              |
| async_tree_cpu_io_mixed | 727 ms                                                                 | 715 ms: 1.02x faster                                                              |
| generators              | 29.8 ms                                                                | 29.4 ms: 1.02x faster                                                             |
| go                      | 137 ms                                                                 | 135 ms: 1.01x faster                                                              |
| raytrace                | 279 ms                                                                 | 275 ms: 1.01x faster                                                              |
| telco                   | 6.58 ms                                                                | 6.48 ms: 1.01x faster                                                             |
| nqueens                 | 80.4 ms                                                                | 79.4 ms: 1.01x faster                                                             |
| scimark_sor             | 111 ms                                                                 | 109 ms: 1.01x faster                                                              |
| async_tree_io           | 1.28 sec                                                               | 1.27 sec: 1.01x faster                                                            |
| dask                    | 505 ms                                                                 | 499 ms: 1.01x faster                                                              |
| sqlglot_normalize       | 103 ms                                                                 | 102 ms: 1.01x faster                                                              |
| sympy_expand            | 462 ms                                                                 | 457 ms: 1.01x faster                                                              |
| asyncio_tcp             | 506 ms                                                                 | 501 ms: 1.01x faster                                                              |
| scimark_monte_carlo     | 66.3 ms                                                                | 65.7 ms: 1.01x faster                                                             |
| pycparser               | 1.15 sec                                                               | 1.14 sec: 1.01x faster                                                            |
| sqlglot_parse           | 1.21 ms                                                                | 1.20 ms: 1.01x faster                                                             |
| aiohttp                 | 1.02 ms                                                                | 1.01 ms: 1.01x faster                                                             |
| regex_compile           | 133 ms                                                                 | 132 ms: 1.01x faster                                                              |
| tornado_http            | 90.9 ms                                                                | 90.3 ms: 1.01x faster                                                             |
| sqlglot_optimize        | 50.6 ms                                                                | 50.3 ms: 1.01x faster                                                             |
| sympy_str               | 283 ms                                                                 | 282 ms: 1.01x faster                                                              |
| sympy_integrate         | 20.5 ms                                                                | 20.4 ms: 1.01x faster                                                             |
| float                   | 73.0 ms                                                                | 72.6 ms: 1.01x faster                                                             |
| xml_etree_process       | 55.3 ms                                                                | 55.0 ms: 1.00x faster                                                             |
| mypy2                   | 334 ms                                                                 | 333 ms: 1.00x faster                                                              |
| sqlglot_transpile       | 1.49 ms                                                                | 1.48 ms: 1.00x faster                                                             |
| mako                    | 10.0 ms                                                                | 9.99 ms: 1.00x faster                                                             |
| gunicorn                | 1.10 ms                                                                | 1.09 ms: 1.00x faster                                                             |
| bench_thread_pool       | 790 us                                                                 | 788 us: 1.00x faster                                                              |
| pidigits                | 188 ms                                                                 | 188 ms: 1.00x slower                                                              |
| deepcopy                | 322 us                                                                 | 324 us: 1.01x slower                                                              |
| scimark_fft             | 304 ms                                                                 | 306 ms: 1.01x slower                                                              |
| hexiom                  | 6.01 ms                                                                | 6.05 ms: 1.01x slower                                                             |
| pathlib                 | 18.2 ms                                                                | 18.3 ms: 1.01x slower                                                             |
| coverage                | 96.0 ms                                                                | 96.6 ms: 1.01x slower                                                             |
| json_dumps              | 9.40 ms                                                                | 9.46 ms: 1.01x slower                                                             |
| create_gc_cycles        | 1.47 ms                                                                | 1.48 ms: 1.01x slower                                                             |
| logging_format          | 6.26 us                                                                | 6.31 us: 1.01x slower                                                             |
| python_startup_no_site  | 6.50 ms                                                                | 6.55 ms: 1.01x slower                                                             |
| python_startup          | 8.79 ms                                                                | 8.87 ms: 1.01x slower                                                             |
| regex_v8                | 22.4 ms                                                                | 22.6 ms: 1.01x slower                                                             |
| logging_simple          | 5.62 us                                                                | 5.69 us: 1.01x slower                                                             |
| pyflate                 | 411 ms                                                                 | 416 ms: 1.01x slower                                                              |
| chameleon               | 6.34 ms                                                                | 6.42 ms: 1.01x slower                                                             |
| sqlalchemy_declarative  | 136 ms                                                                 | 139 ms: 1.02x slower                                                              |
| fannkuch                | 370 ms                                                                 | 377 ms: 1.02x slower                                                              |
| json_loads              | 24.0 us                                                                | 24.5 us: 1.02x slower                                                             |
| thrift                  | 771 us                                                                 | 787 us: 1.02x slower                                                              |
| crypto_pyaes            | 72.7 ms                                                                | 74.4 ms: 1.02x slower                                                             |
| pickle_pure_python      | 285 us                                                                 | 292 us: 1.02x slower                                                              |
| mdp                     | 2.61 sec                                                               | 2.68 sec: 1.03x slower                                                            |
| json                    | 4.58 ms                                                                | 4.73 ms: 1.03x slower                                                             |
| pickle_list             | 4.22 us                                                                | 4.43 us: 1.05x slower                                                             |
| regex_dna               | 204 ms                                                                 | 214 ms: 1.05x slower                                                              |
| pickle_dict             | 30.6 us                                                                | 32.3 us: 1.05x slower                                                             |
| regex_effbot            | 3.43 ms                                                                | 3.63 ms: 1.06x slower                                                             |
| gc_traversal            | 3.66 ms                                                                | 4.19 ms: 1.15x slower                                                             |
| Geometric mean          | (ref)                                                                  | 1.00x faster                                                                      |

Benchmark hidden because not significant (22): async_tree_none, scimark_lu, logging_silent, sqlalchemy_imperative, sqlite_synth, unpickle_pure_python, xml_etree_parse, scimark_sparse_mat_mult, bench_mp_pool, deltablue, 2to3, genshi_xml, xml_etree_generate, docutils, deepcopy_reduce, dulwich_log, sympy_sum, html5lib, deepcopy_memo, pickle, djangocms, xml_etree_iterparse
