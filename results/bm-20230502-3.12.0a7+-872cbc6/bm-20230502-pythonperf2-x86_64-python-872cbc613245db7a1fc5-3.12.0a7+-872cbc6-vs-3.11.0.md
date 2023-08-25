
# Results vs. 3.11.0

- fork: python
- ref: 872cbc613245db7a1fc5
- machine: linux-x86_64
- commit hash: 872cbc6
- commit date: 2023-05-02
- overall geometric mean: 1.04x faster \*
- HPT reliability: 99.33%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230502-pythonperf2-x86_64-python-872cbc613245db7a1fc5-3.12.0a7+-872cbc6 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 288 ms                                                       | 285 ms: 1.01x faster                                                         |
| docutils       | 2.86 sec                                                     | 2.89 sec: 1.01x slower                                                       |
| html5lib       | 72.9 ms                                                      | 70.2 ms: 1.04x faster                                                        |
| tornado_http   | 122 ms                                                       | 113 ms: 1.08x faster                                                         |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230502-pythonperf2-x86_64-python-872cbc613245db7a1fc5-3.12.0a7+-872cbc6 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 90.7 ms                                                      | 86.2 ms: 1.05x faster                                                        |
| pidigits       | 251 ms                                                       | 260 ms: 1.04x slower                                                         |
| float          | 74.2 ms                                                      | 79.4 ms: 1.07x slower                                                        |
| Geometric mean | (ref)                                                        | 1.02x slower                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230502-pythonperf2-x86_64-python-872cbc613245db7a1fc5-3.12.0a7+-872cbc6 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 158 ms                                                       | 144 ms: 1.09x faster                                                         |
| regex_effbot   | 3.50 ms                                                      | 3.46 ms: 1.01x faster                                                        |
| regex_v8       | 23.9 ms                                                      | 23.9 ms: 1.00x faster                                                        |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                 |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230502-pythonperf2-x86_64-python-872cbc613245db7a1fc5-3.12.0a7+-872cbc6 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| json_dumps           | 13.4 ms                                                      | 10.4 ms: 1.28x faster                                                        |
| unpickle_pure_python | 241 us                                                       | 208 us: 1.16x faster                                                         |
| json_loads           | 28.7 us                                                      | 25.0 us: 1.15x faster                                                        |
| xml_etree_parse      | 158 ms                                                       | 148 ms: 1.07x faster                                                         |
| pickle_pure_python   | 319 us                                                       | 321 us: 1.01x slower                                                         |
| pickle_dict          | 30.8 us                                                      | 31.5 us: 1.02x slower                                                        |
| xml_etree_process    | 56.5 ms                                                      | 58.5 ms: 1.04x slower                                                        |
| xml_etree_generate   | 80.5 ms                                                      | 86.3 ms: 1.07x slower                                                        |
| pickle               | 9.64 us                                                      | 10.3 us: 1.07x slower                                                        |
| unpickle_list        | 4.53 us                                                      | 4.87 us: 1.07x slower                                                        |
| unpickle             | 13.4 us                                                      | 15.0 us: 1.12x slower                                                        |
| pickle_list          | 3.83 us                                                      | 4.29 us: 1.12x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.01x faster                                                                 |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230502-pythonperf2-x86_64-python-872cbc613245db7a1fc5-3.12.0a7+-872cbc6 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                      | 11.2 ms: 1.04x slower                                                        |
| python_startup_no_site | 7.76 ms                                                      | 8.37 ms: 1.08x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.06x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230502-pythonperf2-x86_64-python-872cbc613245db7a1fc5-3.12.0a7+-872cbc6 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_xml     | 58.5 ms                                                      | 54.3 ms: 1.08x faster                                                        |
| mako           | 11.0 ms                                                      | 10.2 ms: 1.08x faster                                                        |
| genshi_text    | 26.1 ms                                                      | 24.4 ms: 1.07x faster                                                        |
| Geometric mean | (ref)                                                        | 1.08x faster                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230502-pythonperf2-x86_64-python-872cbc613245db7a1fc5-3.12.0a7+-872cbc6 |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| asyncio_tcp             | 753 ms                                                       | 377 ms: 2.00x faster                                                         |
| generators              | 56.0 ms                                                      | 36.2 ms: 1.55x faster                                                        |
| json_dumps              | 13.4 ms                                                      | 10.4 ms: 1.28x faster                                                        |
| fannkuch                | 429 ms                                                       | 345 ms: 1.24x faster                                                         |
| deltablue               | 4.00 ms                                                      | 3.22 ms: 1.24x faster                                                        |
| chaos                   | 80.9 ms                                                      | 67.1 ms: 1.21x faster                                                        |
| coroutines              | 27.6 ms                                                      | 22.9 ms: 1.20x faster                                                        |
| mypy2                   | 451 ms                                                       | 376 ms: 1.20x faster                                                         |
| hexiom                  | 7.13 ms                                                      | 5.98 ms: 1.19x faster                                                        |
| scimark_lu              | 115 ms                                                       | 98.7 ms: 1.16x faster                                                        |
| unpickle_pure_python    | 241 us                                                       | 208 us: 1.16x faster                                                         |
| nqueens                 | 103 ms                                                       | 89.5 ms: 1.15x faster                                                        |
| json_loads              | 28.7 us                                                      | 25.0 us: 1.15x faster                                                        |
| richards                | 48.3 ms                                                      | 43.2 ms: 1.12x faster                                                        |
| logging_format          | 8.11 us                                                      | 7.34 us: 1.10x faster                                                        |
| go                      | 164 ms                                                       | 148 ms: 1.10x faster                                                         |
| sqlglot_parse           | 1.53 ms                                                      | 1.40 ms: 1.10x faster                                                        |
| async_tree_memoization  | 630 ms                                                       | 577 ms: 1.09x faster                                                         |
| json                    | 5.65 ms                                                      | 5.17 ms: 1.09x faster                                                        |
| regex_compile           | 158 ms                                                       | 144 ms: 1.09x faster                                                         |
| async_tree_none         | 519 ms                                                       | 480 ms: 1.08x faster                                                         |
| genshi_xml              | 58.5 ms                                                      | 54.3 ms: 1.08x faster                                                        |
| tornado_http            | 122 ms                                                       | 113 ms: 1.08x faster                                                         |
| mako                    | 11.0 ms                                                      | 10.2 ms: 1.08x faster                                                        |
| mdp                     | 2.75 sec                                                     | 2.55 sec: 1.08x faster                                                       |
| genshi_text             | 26.1 ms                                                      | 24.4 ms: 1.07x faster                                                        |
| logging_simple          | 7.19 us                                                      | 6.71 us: 1.07x faster                                                        |
| async_tree_io           | 1.17 sec                                                     | 1.10 sec: 1.07x faster                                                       |
| xml_etree_parse         | 158 ms                                                       | 148 ms: 1.07x faster                                                         |
| sqlglot_transpile       | 1.92 ms                                                      | 1.81 ms: 1.06x faster                                                        |
| nbody                   | 90.7 ms                                                      | 86.2 ms: 1.05x faster                                                        |
| deepcopy                | 399 us                                                       | 382 us: 1.05x faster                                                         |
| async_tree_cpu_io_mixed | 749 ms                                                       | 717 ms: 1.04x faster                                                         |
| dulwich_log             | 68.4 ms                                                      | 65.6 ms: 1.04x faster                                                        |
| pycparser               | 1.32 sec                                                     | 1.27 sec: 1.04x faster                                                       |
| sqlglot_normalize       | 126 ms                                                       | 121 ms: 1.04x faster                                                         |
| html5lib                | 72.9 ms                                                      | 70.2 ms: 1.04x faster                                                        |
| bench_thread_pool       | 1.01 ms                                                      | 974 us: 1.04x faster                                                         |
| raytrace                | 317 ms                                                       | 306 ms: 1.04x faster                                                         |
| crypto_pyaes            | 83.4 ms                                                      | 81.5 ms: 1.02x faster                                                        |
| spectral_norm           | 93.3 ms                                                      | 91.3 ms: 1.02x faster                                                        |
| logging_silent          | 101 ns                                                       | 99.5 ns: 1.01x faster                                                        |
| gc_traversal            | 3.85 ms                                                      | 3.80 ms: 1.01x faster                                                        |
| sqlglot_optimize        | 59.8 ms                                                      | 59.1 ms: 1.01x faster                                                        |
| deepcopy_memo           | 38.8 us                                                      | 38.4 us: 1.01x faster                                                        |
| pyflate                 | 449 ms                                                       | 444 ms: 1.01x faster                                                         |
| regex_effbot            | 3.50 ms                                                      | 3.46 ms: 1.01x faster                                                        |
| thrift                  | 925 us                                                       | 917 us: 1.01x faster                                                         |
| 2to3                    | 288 ms                                                       | 285 ms: 1.01x faster                                                         |
| deepcopy_reduce         | 3.51 us                                                      | 3.49 us: 1.01x faster                                                        |
| regex_v8                | 23.9 ms                                                      | 23.9 ms: 1.00x faster                                                        |
| pickle_pure_python      | 319 us                                                       | 321 us: 1.01x slower                                                         |
| docutils                | 2.86 sec                                                     | 2.89 sec: 1.01x slower                                                       |
| pathlib                 | 19.1 ms                                                      | 19.3 ms: 1.01x slower                                                        |
| pprint_pformat          | 1.63 sec                                                     | 1.66 sec: 1.02x slower                                                       |
| scimark_sor             | 111 ms                                                       | 113 ms: 1.02x slower                                                         |
| pickle_dict             | 30.8 us                                                      | 31.5 us: 1.02x slower                                                        |
| comprehensions          | 24.6 us                                                      | 25.2 us: 1.02x slower                                                        |
| create_gc_cycles        | 1.61 ms                                                      | 1.65 ms: 1.03x slower                                                        |
| pprint_safe_repr        | 784 ms                                                       | 806 ms: 1.03x slower                                                         |
| scimark_monte_carlo     | 68.2 ms                                                      | 70.4 ms: 1.03x slower                                                        |
| xml_etree_process       | 56.5 ms                                                      | 58.5 ms: 1.04x slower                                                        |
| pidigits                | 251 ms                                                       | 260 ms: 1.04x slower                                                         |
| python_startup          | 10.8 ms                                                      | 11.2 ms: 1.04x slower                                                        |
| telco                   | 6.86 ms                                                      | 7.17 ms: 1.04x slower                                                        |
| sqlite_synth            | 2.50 us                                                      | 2.64 us: 1.06x slower                                                        |
| coverage                | 84.8 ms                                                      | 89.9 ms: 1.06x slower                                                        |
| meteor_contest          | 131 ms                                                       | 139 ms: 1.06x slower                                                         |
| scimark_sparse_mat_mult | 4.05 ms                                                      | 4.32 ms: 1.07x slower                                                        |
| scimark_fft             | 285 ms                                                       | 304 ms: 1.07x slower                                                         |
| float                   | 74.2 ms                                                      | 79.4 ms: 1.07x slower                                                        |
| xml_etree_generate      | 80.5 ms                                                      | 86.3 ms: 1.07x slower                                                        |
| pickle                  | 9.64 us                                                      | 10.3 us: 1.07x slower                                                        |
| unpickle_list           | 4.53 us                                                      | 4.87 us: 1.07x slower                                                        |
| python_startup_no_site  | 7.76 ms                                                      | 8.37 ms: 1.08x slower                                                        |
| bench_mp_pool           | 4.62 ms                                                      | 5.16 ms: 1.12x slower                                                        |
| unpickle                | 13.4 us                                                      | 15.0 us: 1.12x slower                                                        |
| pickle_list             | 3.83 us                                                      | 4.29 us: 1.12x slower                                                        |
| unpack_sequence         | 45.6 ns                                                      | 52.3 ns: 1.15x slower                                                        |
| async_generators        | 316 ms                                                       | 385 ms: 1.22x slower                                                         |
| dask                    | 410 ms                                                       | 562 ms: 1.37x slower                                                         |
| Geometric mean          | (ref)                                                        | 1.04x faster                                                                 |

Benchmark hidden because not significant (2): xml_etree_iterparse, regex_dna
Ignored benchmarks (16) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, chameleon, django_template, flaskblogging, gunicorn, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 99.33% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x
