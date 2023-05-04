
# Results vs. 3.11.0

- fork: python
- ref: 872cbc613245db7a1fc5
- machine: linux-x86_64
- commit hash: 872cbc6
- commit date: 2023-05-02
- overall geometric mean: 1.03x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230502-pythonperf2-x86_64-python-872cbc613245db7a1fc5-3.12.0a7+-872cbc6 |
|----------------|:-------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 289 ms                                                                    | 285 ms: 1.02x faster                                                         |
| docutils       | 2.86 sec                                                                  | 2.89 sec: 1.01x slower                                                       |
| tornado_http   | 125 ms                                                                    | 113 ms: 1.11x faster                                                         |
| Geometric mean | (ref)                                                                     | 1.03x faster                                                                 |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230502-pythonperf2-x86_64-python-872cbc613245db7a1fc5-3.12.0a7+-872cbc6 |
|----------------|:-------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 92.1 ms                                                                   | 86.2 ms: 1.07x faster                                                        |
| pidigits       | 252 ms                                                                    | 260 ms: 1.04x slower                                                         |
| float          | 75.7 ms                                                                   | 79.4 ms: 1.05x slower                                                        |
| Geometric mean | (ref)                                                                     | 1.01x slower                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230502-pythonperf2-x86_64-python-872cbc613245db7a1fc5-3.12.0a7+-872cbc6 |
|----------------|:-------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 154 ms                                                                    | 144 ms: 1.07x faster                                                         |
| regex_v8       | 24.4 ms                                                                   | 23.9 ms: 1.02x faster                                                        |
| regex_dna      | 225 ms                                                                    | 227 ms: 1.01x slower                                                         |
| regex_effbot   | 3.31 ms                                                                   | 3.46 ms: 1.05x slower                                                        |
| Geometric mean | (ref)                                                                     | 1.01x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230502-pythonperf2-x86_64-python-872cbc613245db7a1fc5-3.12.0a7+-872cbc6 |
|----------------------|:-------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| json_dumps           | 13.4 ms                                                                   | 10.4 ms: 1.28x faster                                                        |
| unpickle_pure_python | 238 us                                                                    | 208 us: 1.15x faster                                                         |
| json_loads           | 28.4 us                                                                   | 25.0 us: 1.14x faster                                                        |
| xml_etree_parse      | 161 ms                                                                    | 148 ms: 1.09x faster                                                         |
| xml_etree_iterparse  | 106 ms                                                                    | 104 ms: 1.02x faster                                                         |
| pickle_pure_python   | 319 us                                                                    | 321 us: 1.00x slower                                                         |
| pickle_dict          | 31.1 us                                                                   | 31.5 us: 1.01x slower                                                        |
| pickle               | 9.92 us                                                                   | 10.3 us: 1.04x slower                                                        |
| xml_etree_process    | 55.8 ms                                                                   | 58.5 ms: 1.05x slower                                                        |
| unpickle_list        | 4.52 us                                                                   | 4.87 us: 1.08x slower                                                        |
| xml_etree_generate   | 79.1 ms                                                                   | 86.3 ms: 1.09x slower                                                        |
| pickle_list          | 3.78 us                                                                   | 4.29 us: 1.14x slower                                                        |
| unpickle             | 13.0 us                                                                   | 15.0 us: 1.15x slower                                                        |
| Geometric mean       | (ref)                                                                     | 1.01x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230502-pythonperf2-x86_64-python-872cbc613245db7a1fc5-3.12.0a7+-872cbc6 |
|------------------------|:-------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 10.7 ms                                                                   | 11.2 ms: 1.04x slower                                                        |
| python_startup_no_site | 7.73 ms                                                                   | 8.37 ms: 1.08x slower                                                        |
| Geometric mean         | (ref)                                                                     | 1.06x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230502-pythonperf2-x86_64-python-872cbc613245db7a1fc5-3.12.0a7+-872cbc6 |
|----------------|:-------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_text    | 26.3 ms                                                                   | 24.4 ms: 1.08x faster                                                        |
| mako           | 10.9 ms                                                                   | 10.2 ms: 1.07x faster                                                        |
| genshi_xml     | 57.8 ms                                                                   | 54.3 ms: 1.07x faster                                                        |
| Geometric mean | (ref)                                                                     | 1.07x faster                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230502-pythonperf2-x86_64-python-872cbc613245db7a1fc5-3.12.0a7+-872cbc6 |
|-------------------------|:-------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| asyncio_tcp             | 752 ms                                                                    | 377 ms: 1.99x faster                                                         |
| generators              | 56.0 ms                                                                   | 36.2 ms: 1.55x faster                                                        |
| fannkuch                | 449 ms                                                                    | 345 ms: 1.30x faster                                                         |
| coroutines              | 29.5 ms                                                                   | 22.9 ms: 1.28x faster                                                        |
| json_dumps              | 13.4 ms                                                                   | 10.4 ms: 1.28x faster                                                        |
| deltablue               | 3.99 ms                                                                   | 3.22 ms: 1.24x faster                                                        |
| mypy2                   | 446 ms                                                                    | 376 ms: 1.19x faster                                                         |
| hexiom                  | 7.00 ms                                                                   | 5.98 ms: 1.17x faster                                                        |
| scimark_lu              | 114 ms                                                                    | 98.7 ms: 1.16x faster                                                        |
| unpickle_pure_python    | 238 us                                                                    | 208 us: 1.15x faster                                                         |
| json_loads              | 28.4 us                                                                   | 25.0 us: 1.14x faster                                                        |
| chaos                   | 76.2 ms                                                                   | 67.1 ms: 1.14x faster                                                        |
| richards                | 49.1 ms                                                                   | 43.2 ms: 1.14x faster                                                        |
| nqueens                 | 101 ms                                                                    | 89.5 ms: 1.13x faster                                                        |
| gc_traversal            | 4.22 ms                                                                   | 3.80 ms: 1.11x faster                                                        |
| tornado_http            | 125 ms                                                                    | 113 ms: 1.11x faster                                                         |
| async_tree_memoization  | 639 ms                                                                    | 577 ms: 1.11x faster                                                         |
| async_tree_none         | 529 ms                                                                    | 480 ms: 1.10x faster                                                         |
| sqlglot_parse           | 1.53 ms                                                                   | 1.40 ms: 1.09x faster                                                        |
| xml_etree_parse         | 161 ms                                                                    | 148 ms: 1.09x faster                                                         |
| json                    | 5.59 ms                                                                   | 5.17 ms: 1.08x faster                                                        |
| genshi_text             | 26.3 ms                                                                   | 24.4 ms: 1.08x faster                                                        |
| async_tree_io           | 1.18 sec                                                                  | 1.10 sec: 1.08x faster                                                       |
| mdp                     | 2.73 sec                                                                  | 2.55 sec: 1.07x faster                                                       |
| nbody                   | 92.1 ms                                                                   | 86.2 ms: 1.07x faster                                                        |
| logging_format          | 7.84 us                                                                   | 7.34 us: 1.07x faster                                                        |
| regex_compile           | 154 ms                                                                    | 144 ms: 1.07x faster                                                         |
| mako                    | 10.9 ms                                                                   | 10.2 ms: 1.07x faster                                                        |
| go                      | 158 ms                                                                    | 148 ms: 1.07x faster                                                         |
| genshi_xml              | 57.8 ms                                                                   | 54.3 ms: 1.07x faster                                                        |
| dulwich_log             | 69.1 ms                                                                   | 65.6 ms: 1.05x faster                                                        |
| async_tree_cpu_io_mixed | 754 ms                                                                    | 717 ms: 1.05x faster                                                         |
| crypto_pyaes            | 85.0 ms                                                                   | 81.5 ms: 1.04x faster                                                        |
| spectral_norm           | 95.1 ms                                                                   | 91.3 ms: 1.04x faster                                                        |
| sqlglot_transpile       | 1.88 ms                                                                   | 1.81 ms: 1.04x faster                                                        |
| logging_simple          | 6.95 us                                                                   | 6.71 us: 1.04x faster                                                        |
| logging_silent          | 103 ns                                                                    | 99.5 ns: 1.03x faster                                                        |
| thrift                  | 942 us                                                                    | 917 us: 1.03x faster                                                         |
| pycparser               | 1.30 sec                                                                  | 1.27 sec: 1.03x faster                                                       |
| regex_v8                | 24.4 ms                                                                   | 23.9 ms: 1.02x faster                                                        |
| xml_etree_iterparse     | 106 ms                                                                    | 104 ms: 1.02x faster                                                         |
| 2to3                    | 289 ms                                                                    | 285 ms: 1.02x faster                                                         |
| sqlglot_normalize       | 122 ms                                                                    | 121 ms: 1.01x faster                                                         |
| pickle_pure_python      | 319 us                                                                    | 321 us: 1.00x slower                                                         |
| pathlib                 | 19.2 ms                                                                   | 19.3 ms: 1.01x slower                                                        |
| raytrace                | 303 ms                                                                    | 306 ms: 1.01x slower                                                         |
| sqlglot_optimize        | 58.6 ms                                                                   | 59.1 ms: 1.01x slower                                                        |
| regex_dna               | 225 ms                                                                    | 227 ms: 1.01x slower                                                         |
| docutils                | 2.86 sec                                                                  | 2.89 sec: 1.01x slower                                                       |
| pickle_dict             | 31.1 us                                                                   | 31.5 us: 1.01x slower                                                        |
| pyflate                 | 438 ms                                                                    | 444 ms: 1.01x slower                                                         |
| comprehensions          | 24.7 us                                                                   | 25.2 us: 1.02x slower                                                        |
| deepcopy_reduce         | 3.39 us                                                                   | 3.49 us: 1.03x slower                                                        |
| pidigits                | 252 ms                                                                    | 260 ms: 1.04x slower                                                         |
| pprint_pformat          | 1.60 sec                                                                  | 1.66 sec: 1.04x slower                                                       |
| scimark_sor             | 109 ms                                                                    | 113 ms: 1.04x slower                                                         |
| deepcopy_memo           | 37.0 us                                                                   | 38.4 us: 1.04x slower                                                        |
| scimark_monte_carlo     | 67.8 ms                                                                   | 70.4 ms: 1.04x slower                                                        |
| pickle                  | 9.92 us                                                                   | 10.3 us: 1.04x slower                                                        |
| python_startup          | 10.7 ms                                                                   | 11.2 ms: 1.04x slower                                                        |
| coverage                | 86.0 ms                                                                   | 89.9 ms: 1.05x slower                                                        |
| regex_effbot            | 3.31 ms                                                                   | 3.46 ms: 1.05x slower                                                        |
| xml_etree_process       | 55.8 ms                                                                   | 58.5 ms: 1.05x slower                                                        |
| float                   | 75.7 ms                                                                   | 79.4 ms: 1.05x slower                                                        |
| pprint_safe_repr        | 768 ms                                                                    | 806 ms: 1.05x slower                                                         |
| sqlite_synth            | 2.49 us                                                                   | 2.64 us: 1.06x slower                                                        |
| scimark_sparse_mat_mult | 4.06 ms                                                                   | 4.32 ms: 1.06x slower                                                        |
| telco                   | 6.70 ms                                                                   | 7.17 ms: 1.07x slower                                                        |
| meteor_contest          | 129 ms                                                                    | 139 ms: 1.08x slower                                                         |
| unpickle_list           | 4.52 us                                                                   | 4.87 us: 1.08x slower                                                        |
| python_startup_no_site  | 7.73 ms                                                                   | 8.37 ms: 1.08x slower                                                        |
| xml_etree_generate      | 79.1 ms                                                                   | 86.3 ms: 1.09x slower                                                        |
| scimark_fft             | 276 ms                                                                    | 304 ms: 1.10x slower                                                         |
| pickle_list             | 3.78 us                                                                   | 4.29 us: 1.14x slower                                                        |
| bench_mp_pool           | 4.54 ms                                                                   | 5.16 ms: 1.14x slower                                                        |
| unpack_sequence         | 45.9 ns                                                                   | 52.3 ns: 1.14x slower                                                        |
| unpickle                | 13.0 us                                                                   | 15.0 us: 1.15x slower                                                        |
| async_generators        | 318 ms                                                                    | 385 ms: 1.21x slower                                                         |
| dask                    | 418 ms                                                                    | 562 ms: 1.34x slower                                                         |
| Geometric mean          | (ref)                                                                     | 1.03x faster                                                                 |

Benchmark hidden because not significant (4): bench_thread_pool, deepcopy, html5lib, create_gc_cycles
Ignored benchmarks (12) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: aiohttp, chameleon, django_template, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum
