
# Results vs. 3.11.0

- fork: JelleZijlstra
- ref: tvobject
- machine: linux-x86_64
- commit hash: 827b9e5
- commit date: 2023-05-02
- overall geometric mean: 1.04x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230502-pythonperf2-x86_64-JelleZijlstra-tvobject-3.12.0a7+-827b9e5 |
|----------------|:-------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 289 ms                                                                    | 284 ms: 1.02x faster                                                    |
| docutils       | 2.86 sec                                                                  | 2.88 sec: 1.01x slower                                                  |
| html5lib       | 70.2 ms                                                                   | 69.2 ms: 1.01x faster                                                   |
| tornado_http   | 125 ms                                                                    | 113 ms: 1.10x faster                                                    |
| Geometric mean | (ref)                                                                     | 1.03x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230502-pythonperf2-x86_64-JelleZijlstra-tvobject-3.12.0a7+-827b9e5 |
|----------------|:-------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 92.1 ms                                                                   | 87.7 ms: 1.05x faster                                                   |
| float          | 75.7 ms                                                                   | 78.0 ms: 1.03x slower                                                   |
| pidigits       | 252 ms                                                                    | 260 ms: 1.03x slower                                                    |
| Geometric mean | (ref)                                                                     | 1.00x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230502-pythonperf2-x86_64-JelleZijlstra-tvobject-3.12.0a7+-827b9e5 |
|----------------|:-------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 154 ms                                                                    | 144 ms: 1.07x faster                                                    |
| regex_v8       | 24.4 ms                                                                   | 23.4 ms: 1.05x faster                                                   |
| regex_dna      | 225 ms                                                                    | 234 ms: 1.04x slower                                                    |
| regex_effbot   | 3.31 ms                                                                   | 3.50 ms: 1.06x slower                                                   |
| Geometric mean | (ref)                                                                     | 1.01x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230502-pythonperf2-x86_64-JelleZijlstra-tvobject-3.12.0a7+-827b9e5 |
|----------------------|:-------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| json_dumps           | 13.4 ms                                                                   | 10.5 ms: 1.28x faster                                                   |
| unpickle_pure_python | 238 us                                                                    | 204 us: 1.17x faster                                                    |
| json_loads           | 28.4 us                                                                   | 25.1 us: 1.13x faster                                                   |
| xml_etree_parse      | 161 ms                                                                    | 145 ms: 1.11x faster                                                    |
| xml_etree_iterparse  | 106 ms                                                                    | 104 ms: 1.02x faster                                                    |
| pickle               | 9.92 us                                                                   | 10.0 us: 1.01x slower                                                   |
| pickle_dict          | 31.1 us                                                                   | 31.9 us: 1.03x slower                                                   |
| xml_etree_process    | 55.8 ms                                                                   | 58.5 ms: 1.05x slower                                                   |
| unpickle_list        | 4.52 us                                                                   | 4.83 us: 1.07x slower                                                   |
| xml_etree_generate   | 79.1 ms                                                                   | 86.0 ms: 1.09x slower                                                   |
| unpickle             | 13.0 us                                                                   | 14.3 us: 1.09x slower                                                   |
| pickle_list          | 3.78 us                                                                   | 4.28 us: 1.13x slower                                                   |
| Geometric mean       | (ref)                                                                     | 1.01x faster                                                            |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230502-pythonperf2-x86_64-JelleZijlstra-tvobject-3.12.0a7+-827b9e5 |
|------------------------|:-------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 10.7 ms                                                                   | 11.3 ms: 1.05x slower                                                   |
| python_startup_no_site | 7.73 ms                                                                   | 8.47 ms: 1.10x slower                                                   |
| Geometric mean         | (ref)                                                                     | 1.07x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230502-pythonperf2-x86_64-JelleZijlstra-tvobject-3.12.0a7+-827b9e5 |
|----------------|:-------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text    | 26.3 ms                                                                   | 24.3 ms: 1.08x faster                                                   |
| genshi_xml     | 57.8 ms                                                                   | 53.5 ms: 1.08x faster                                                   |
| mako           | 10.9 ms                                                                   | 10.1 ms: 1.08x faster                                                   |
| Geometric mean | (ref)                                                                     | 1.08x faster                                                            |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230502-pythonperf2-x86_64-JelleZijlstra-tvobject-3.12.0a7+-827b9e5 |
|-------------------------|:-------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| asyncio_tcp             | 752 ms                                                                    | 381 ms: 1.98x faster                                                    |
| generators              | 56.0 ms                                                                   | 35.9 ms: 1.56x faster                                                   |
| coroutines              | 29.5 ms                                                                   | 22.5 ms: 1.31x faster                                                   |
| fannkuch                | 449 ms                                                                    | 346 ms: 1.30x faster                                                    |
| json_dumps              | 13.4 ms                                                                   | 10.5 ms: 1.28x faster                                                   |
| deltablue               | 3.99 ms                                                                   | 3.25 ms: 1.23x faster                                                   |
| scimark_lu              | 114 ms                                                                    | 96.2 ms: 1.19x faster                                                   |
| mypy2                   | 446 ms                                                                    | 376 ms: 1.19x faster                                                    |
| hexiom                  | 7.00 ms                                                                   | 5.91 ms: 1.18x faster                                                   |
| unpickle_pure_python    | 238 us                                                                    | 204 us: 1.17x faster                                                    |
| chaos                   | 76.2 ms                                                                   | 66.2 ms: 1.15x faster                                                   |
| richards                | 49.1 ms                                                                   | 42.7 ms: 1.15x faster                                                   |
| nqueens                 | 101 ms                                                                    | 88.9 ms: 1.13x faster                                                   |
| json_loads              | 28.4 us                                                                   | 25.1 us: 1.13x faster                                                   |
| async_tree_memoization  | 639 ms                                                                    | 575 ms: 1.11x faster                                                    |
| sqlglot_parse           | 1.53 ms                                                                   | 1.38 ms: 1.11x faster                                                   |
| async_tree_none         | 529 ms                                                                    | 478 ms: 1.11x faster                                                    |
| xml_etree_parse         | 161 ms                                                                    | 145 ms: 1.11x faster                                                    |
| tornado_http            | 125 ms                                                                    | 113 ms: 1.10x faster                                                    |
| json                    | 5.59 ms                                                                   | 5.12 ms: 1.09x faster                                                   |
| dulwich_log             | 69.1 ms                                                                   | 63.5 ms: 1.09x faster                                                   |
| logging_silent          | 103 ns                                                                    | 94.7 ns: 1.08x faster                                                   |
| genshi_text             | 26.3 ms                                                                   | 24.3 ms: 1.08x faster                                                   |
| genshi_xml              | 57.8 ms                                                                   | 53.5 ms: 1.08x faster                                                   |
| go                      | 158 ms                                                                    | 147 ms: 1.08x faster                                                    |
| mako                    | 10.9 ms                                                                   | 10.1 ms: 1.08x faster                                                   |
| async_tree_io           | 1.18 sec                                                                  | 1.10 sec: 1.08x faster                                                  |
| mdp                     | 2.73 sec                                                                  | 2.54 sec: 1.07x faster                                                  |
| regex_compile           | 154 ms                                                                    | 144 ms: 1.07x faster                                                    |
| spectral_norm           | 95.1 ms                                                                   | 88.9 ms: 1.07x faster                                                   |
| logging_format          | 7.84 us                                                                   | 7.34 us: 1.07x faster                                                   |
| pycparser               | 1.30 sec                                                                  | 1.22 sec: 1.07x faster                                                  |
| logging_simple          | 6.95 us                                                                   | 6.53 us: 1.06x faster                                                   |
| crypto_pyaes            | 85.0 ms                                                                   | 80.3 ms: 1.06x faster                                                   |
| async_tree_cpu_io_mixed | 754 ms                                                                    | 716 ms: 1.05x faster                                                    |
| thrift                  | 942 us                                                                    | 896 us: 1.05x faster                                                    |
| nbody                   | 92.1 ms                                                                   | 87.7 ms: 1.05x faster                                                   |
| gc_traversal            | 4.22 ms                                                                   | 4.02 ms: 1.05x faster                                                   |
| sqlglot_transpile       | 1.88 ms                                                                   | 1.79 ms: 1.05x faster                                                   |
| regex_v8                | 24.4 ms                                                                   | 23.4 ms: 1.05x faster                                                   |
| bench_thread_pool       | 990 us                                                                    | 955 us: 1.04x faster                                                    |
| sqlglot_normalize       | 122 ms                                                                    | 119 ms: 1.03x faster                                                    |
| comprehensions          | 24.7 us                                                                   | 24.3 us: 1.02x faster                                                   |
| 2to3                    | 289 ms                                                                    | 284 ms: 1.02x faster                                                    |
| xml_etree_iterparse     | 106 ms                                                                    | 104 ms: 1.02x faster                                                    |
| html5lib                | 70.2 ms                                                                   | 69.2 ms: 1.01x faster                                                   |
| raytrace                | 303 ms                                                                    | 300 ms: 1.01x faster                                                    |
| sqlglot_optimize        | 58.6 ms                                                                   | 58.7 ms: 1.00x slower                                                   |
| scimark_sor             | 109 ms                                                                    | 110 ms: 1.00x slower                                                    |
| deepcopy                | 384 us                                                                    | 386 us: 1.01x slower                                                    |
| docutils                | 2.86 sec                                                                  | 2.88 sec: 1.01x slower                                                  |
| pickle                  | 9.92 us                                                                   | 10.0 us: 1.01x slower                                                   |
| deepcopy_reduce         | 3.39 us                                                                   | 3.44 us: 1.01x slower                                                   |
| pathlib                 | 19.2 ms                                                                   | 19.7 ms: 1.02x slower                                                   |
| pprint_pformat          | 1.60 sec                                                                  | 1.64 sec: 1.03x slower                                                  |
| pickle_dict             | 31.1 us                                                                   | 31.9 us: 1.03x slower                                                   |
| float                   | 75.7 ms                                                                   | 78.0 ms: 1.03x slower                                                   |
| pidigits                | 252 ms                                                                    | 260 ms: 1.03x slower                                                    |
| unpack_sequence         | 45.9 ns                                                                   | 47.6 ns: 1.04x slower                                                   |
| create_gc_cycles        | 1.65 ms                                                                   | 1.71 ms: 1.04x slower                                                   |
| regex_dna               | 225 ms                                                                    | 234 ms: 1.04x slower                                                    |
| scimark_monte_carlo     | 67.8 ms                                                                   | 70.8 ms: 1.04x slower                                                   |
| xml_etree_process       | 55.8 ms                                                                   | 58.5 ms: 1.05x slower                                                   |
| pprint_safe_repr        | 768 ms                                                                    | 806 ms: 1.05x slower                                                    |
| scimark_fft             | 276 ms                                                                    | 291 ms: 1.05x slower                                                    |
| python_startup          | 10.7 ms                                                                   | 11.3 ms: 1.05x slower                                                   |
| regex_effbot            | 3.31 ms                                                                   | 3.50 ms: 1.06x slower                                                   |
| meteor_contest          | 129 ms                                                                    | 137 ms: 1.06x slower                                                    |
| sqlite_synth            | 2.49 us                                                                   | 2.65 us: 1.07x slower                                                   |
| unpickle_list           | 4.52 us                                                                   | 4.83 us: 1.07x slower                                                   |
| telco                   | 6.70 ms                                                                   | 7.19 ms: 1.07x slower                                                   |
| scimark_sparse_mat_mult | 4.06 ms                                                                   | 4.37 ms: 1.08x slower                                                   |
| xml_etree_generate      | 79.1 ms                                                                   | 86.0 ms: 1.09x slower                                                   |
| unpickle                | 13.0 us                                                                   | 14.3 us: 1.09x slower                                                   |
| python_startup_no_site  | 7.73 ms                                                                   | 8.47 ms: 1.10x slower                                                   |
| coverage                | 86.0 ms                                                                   | 96.0 ms: 1.12x slower                                                   |
| pickle_list             | 3.78 us                                                                   | 4.28 us: 1.13x slower                                                   |
| async_generators        | 318 ms                                                                    | 384 ms: 1.21x slower                                                    |
| bench_mp_pool           | 4.54 ms                                                                   | 5.54 ms: 1.22x slower                                                   |
| dask                    | 418 ms                                                                    | 560 ms: 1.34x slower                                                    |
| Geometric mean          | (ref)                                                                     | 1.04x faster                                                            |

Benchmark hidden because not significant (3): pickle_pure_python, deepcopy_memo, pyflate
Ignored benchmarks (12) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: aiohttp, chameleon, django_template, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum
