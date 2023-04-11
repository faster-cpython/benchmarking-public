
# Results vs. base

- fork: ericsnowcurrently
- ref: interp_current_as_th
- machine: linux-x86_64
- commit hash: fbb272a
- commit date: 2023-04-11
- overall geometric mean: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230406-linux-x86_64-python-52bc2e7b9d451821513a-3.12.0a7+-52bc2e7 | bm-20230411-linux-x86_64-ericsnowcurrently-interp_current_as_th-3.12.0a7+-fbb272a |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 251 ms                                                                 | 250 ms: 1.00x faster                                                              |
| chameleon      | 6.34 ms                                                                | 6.51 ms: 1.03x slower                                                             |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                                      |

Benchmark hidden because not significant (3): docutils, html5lib, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230406-linux-x86_64-python-52bc2e7b9d451821513a-3.12.0a7+-52bc2e7 | bm-20230411-linux-x86_64-ericsnowcurrently-interp_current_as_th-3.12.0a7+-fbb272a |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| nbody          | 87.5 ms                                                                | 82.7 ms: 1.06x faster                                                             |
| pidigits       | 188 ms                                                                 | 188 ms: 1.00x slower                                                              |
| Geometric mean | (ref)                                                                  | 1.02x faster                                                                      |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230406-linux-x86_64-python-52bc2e7b9d451821513a-3.12.0a7+-52bc2e7 | bm-20230411-linux-x86_64-ericsnowcurrently-interp_current_as_th-3.12.0a7+-fbb272a |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 133 ms                                                                 | 131 ms: 1.01x faster                                                              |
| regex_v8       | 22.4 ms                                                                | 22.5 ms: 1.01x slower                                                             |
| regex_effbot   | 3.43 ms                                                                | 3.57 ms: 1.04x slower                                                             |
| regex_dna      | 204 ms                                                                 | 214 ms: 1.05x slower                                                              |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20230406-linux-x86_64-python-52bc2e7b9d451821513a-3.12.0a7+-52bc2e7 | bm-20230411-linux-x86_64-ericsnowcurrently-interp_current_as_th-3.12.0a7+-fbb272a |
|--------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| unpickle_list      | 5.03 us                                                                | 4.67 us: 1.08x faster                                                             |
| unpickle           | 13.9 us                                                                | 13.1 us: 1.06x faster                                                             |
| xml_etree_generate | 80.6 ms                                                                | 80.2 ms: 1.01x faster                                                             |
| pickle             | 10.5 us                                                                | 10.6 us: 1.01x slower                                                             |
| json_loads         | 24.0 us                                                                | 24.4 us: 1.02x slower                                                             |
| xml_etree_parse    | 147 ms                                                                 | 150 ms: 1.02x slower                                                              |
| pickle_list        | 4.22 us                                                                | 4.34 us: 1.03x slower                                                             |
| pickle_dict        | 30.6 us                                                                | 32.1 us: 1.05x slower                                                             |
| Geometric mean     | (ref)                                                                  | 1.00x faster                                                                      |

Benchmark hidden because not significant (5): pickle_pure_python, xml_etree_iterparse, xml_etree_process, json_dumps, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230406-linux-x86_64-python-52bc2e7b9d451821513a-3.12.0a7+-52bc2e7 | bm-20230411-linux-x86_64-ericsnowcurrently-interp_current_as_th-3.12.0a7+-fbb272a |
|------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup_no_site | 6.50 ms                                                                | 6.50 ms: 1.00x slower                                                             |
| python_startup         | 8.79 ms                                                                | 8.80 ms: 1.00x slower                                                             |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20230406-linux-x86_64-python-52bc2e7b9d451821513a-3.12.0a7+-52bc2e7 | bm-20230411-linux-x86_64-ericsnowcurrently-interp_current_as_th-3.12.0a7+-fbb272a |
|-----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| genshi_text     | 21.7 ms                                                                | 21.2 ms: 1.03x faster                                                             |
| django_template | 32.6 ms                                                                | 32.0 ms: 1.02x faster                                                             |
| mako            | 10.0 ms                                                                | 9.95 ms: 1.01x faster                                                             |
| genshi_xml      | 47.3 ms                                                                | 47.1 ms: 1.00x faster                                                             |
| Geometric mean  | (ref)                                                                  | 1.01x faster                                                                      |

All benchmarks:
===============

| Benchmark               | bm-20230406-linux-x86_64-python-52bc2e7b9d451821513a-3.12.0a7+-52bc2e7 | bm-20230411-linux-x86_64-ericsnowcurrently-interp_current_as_th-3.12.0a7+-fbb272a |
|-------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| unpickle_list           | 5.03 us                                                                | 4.67 us: 1.08x faster                                                             |
| unpickle                | 13.9 us                                                                | 13.1 us: 1.06x faster                                                             |
| nbody                   | 87.5 ms                                                                | 82.7 ms: 1.06x faster                                                             |
| mdp                     | 2.61 sec                                                               | 2.50 sec: 1.05x faster                                                            |
| coroutines              | 23.8 ms                                                                | 23.0 ms: 1.03x faster                                                             |
| unpack_sequence         | 43.6 ns                                                                | 42.3 ns: 1.03x faster                                                             |
| richards                | 44.5 ms                                                                | 43.2 ms: 1.03x faster                                                             |
| pprint_pformat          | 1.42 sec                                                               | 1.38 sec: 1.03x faster                                                            |
| comprehensions          | 21.8 us                                                                | 21.2 us: 1.03x faster                                                             |
| async_generators        | 416 ms                                                                 | 405 ms: 1.03x faster                                                              |
| chaos                   | 65.8 ms                                                                | 64.1 ms: 1.03x faster                                                             |
| genshi_text             | 21.7 ms                                                                | 21.2 ms: 1.03x faster                                                             |
| telco                   | 6.58 ms                                                                | 6.41 ms: 1.03x faster                                                             |
| dask                    | 505 ms                                                                 | 493 ms: 1.02x faster                                                              |
| nqueens                 | 80.4 ms                                                                | 78.8 ms: 1.02x faster                                                             |
| generators              | 29.8 ms                                                                | 29.2 ms: 1.02x faster                                                             |
| deepcopy_reduce         | 2.93 us                                                                | 2.87 us: 1.02x faster                                                             |
| pprint_safe_repr        | 696 ms                                                                 | 682 ms: 1.02x faster                                                              |
| async_tree_memoization  | 617 ms                                                                 | 605 ms: 1.02x faster                                                              |
| meteor_contest          | 103 ms                                                                 | 101 ms: 1.02x faster                                                              |
| django_template         | 32.6 ms                                                                | 32.0 ms: 1.02x faster                                                             |
| sqlite_synth            | 2.64 us                                                                | 2.60 us: 1.02x faster                                                             |
| raytrace                | 279 ms                                                                 | 275 ms: 1.02x faster                                                              |
| sqlglot_normalize       | 103 ms                                                                 | 101 ms: 1.01x faster                                                              |
| regex_compile           | 133 ms                                                                 | 131 ms: 1.01x faster                                                              |
| sqlglot_optimize        | 50.6 ms                                                                | 49.9 ms: 1.01x faster                                                             |
| gunicorn                | 1.10 ms                                                                | 1.08 ms: 1.01x faster                                                             |
| logging_format          | 6.26 us                                                                | 6.18 us: 1.01x faster                                                             |
| scimark_sor             | 111 ms                                                                 | 109 ms: 1.01x faster                                                              |
| scimark_fft             | 304 ms                                                                 | 300 ms: 1.01x faster                                                              |
| spectral_norm           | 95.2 ms                                                                | 94.1 ms: 1.01x faster                                                             |
| aiohttp                 | 1.02 ms                                                                | 1.00 ms: 1.01x faster                                                             |
| sympy_expand            | 462 ms                                                                 | 457 ms: 1.01x faster                                                              |
| pathlib                 | 18.2 ms                                                                | 18.0 ms: 1.01x faster                                                             |
| sympy_integrate         | 20.5 ms                                                                | 20.3 ms: 1.01x faster                                                             |
| pycparser               | 1.15 sec                                                               | 1.14 sec: 1.01x faster                                                            |
| dulwich_log             | 62.7 ms                                                                | 62.3 ms: 1.01x faster                                                             |
| mako                    | 10.0 ms                                                                | 9.95 ms: 1.01x faster                                                             |
| bench_thread_pool       | 790 us                                                                 | 785 us: 1.01x faster                                                              |
| sympy_str               | 283 ms                                                                 | 282 ms: 1.01x faster                                                              |
| xml_etree_generate      | 80.6 ms                                                                | 80.2 ms: 1.01x faster                                                             |
| thrift                  | 771 us                                                                 | 767 us: 1.01x faster                                                              |
| deepcopy                | 322 us                                                                 | 321 us: 1.01x faster                                                              |
| 2to3                    | 251 ms                                                                 | 250 ms: 1.00x faster                                                              |
| genshi_xml              | 47.3 ms                                                                | 47.1 ms: 1.00x faster                                                             |
| sqlglot_parse           | 1.21 ms                                                                | 1.20 ms: 1.00x faster                                                             |
| hexiom                  | 6.01 ms                                                                | 5.99 ms: 1.00x faster                                                             |
| sympy_sum               | 165 ms                                                                 | 164 ms: 1.00x faster                                                              |
| pidigits                | 188 ms                                                                 | 188 ms: 1.00x slower                                                              |
| python_startup_no_site  | 6.50 ms                                                                | 6.50 ms: 1.00x slower                                                             |
| python_startup          | 8.79 ms                                                                | 8.80 ms: 1.00x slower                                                             |
| asyncio_tcp             | 506 ms                                                                 | 507 ms: 1.00x slower                                                              |
| async_tree_io           | 1.28 sec                                                               | 1.29 sec: 1.01x slower                                                            |
| regex_v8                | 22.4 ms                                                                | 22.5 ms: 1.01x slower                                                             |
| pickle                  | 10.5 us                                                                | 10.6 us: 1.01x slower                                                             |
| crypto_pyaes            | 72.7 ms                                                                | 73.8 ms: 1.01x slower                                                             |
| create_gc_cycles        | 1.47 ms                                                                | 1.49 ms: 1.01x slower                                                             |
| go                      | 137 ms                                                                 | 139 ms: 1.01x slower                                                              |
| json_loads              | 24.0 us                                                                | 24.4 us: 1.02x slower                                                             |
| xml_etree_parse         | 147 ms                                                                 | 150 ms: 1.02x slower                                                              |
| coverage                | 96.0 ms                                                                | 97.8 ms: 1.02x slower                                                             |
| pyflate                 | 411 ms                                                                 | 419 ms: 1.02x slower                                                              |
| chameleon               | 6.34 ms                                                                | 6.51 ms: 1.03x slower                                                             |
| scimark_sparse_mat_mult | 4.01 ms                                                                | 4.12 ms: 1.03x slower                                                             |
| pickle_list             | 4.22 us                                                                | 4.34 us: 1.03x slower                                                             |
| json                    | 4.58 ms                                                                | 4.72 ms: 1.03x slower                                                             |
| regex_effbot            | 3.43 ms                                                                | 3.57 ms: 1.04x slower                                                             |
| regex_dna               | 204 ms                                                                 | 214 ms: 1.05x slower                                                              |
| pickle_dict             | 30.6 us                                                                | 32.1 us: 1.05x slower                                                             |
| fannkuch                | 370 ms                                                                 | 392 ms: 1.06x slower                                                              |
| gc_traversal            | 3.66 ms                                                                | 4.30 ms: 1.18x slower                                                             |
| Geometric mean          | (ref)                                                                  | 1.00x faster                                                                      |

Benchmark hidden because not significant (23): async_tree_cpu_io_mixed, scimark_lu, tornado_http, sqlalchemy_declarative, mypy2, deltablue, async_tree_none, pickle_pure_python, xml_etree_iterparse, logging_simple, docutils, float, xml_etree_process, bench_mp_pool, json_dumps, sqlglot_transpile, djangocms, unpickle_pure_python, sqlalchemy_imperative, deepcopy_memo, logging_silent, scimark_monte_carlo, html5lib
