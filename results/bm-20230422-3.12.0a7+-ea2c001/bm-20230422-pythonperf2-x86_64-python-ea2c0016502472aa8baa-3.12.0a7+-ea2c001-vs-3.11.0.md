
# Results vs. 3.11.0

- fork: python
- ref: ea2c0016502472aa8baa
- machine: linux-x86_64
- commit hash: ea2c001
- commit date: 2023-04-22
- overall geometric mean: 1.04x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230422-pythonperf2-x86_64-python-ea2c0016502472aa8baa-3.12.0a7+-ea2c001 |
|----------------|:-------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 289 ms                                                                    | 284 ms: 1.02x faster                                                         |
| chameleon      | 7.50 ms                                                                   | 7.44 ms: 1.01x faster                                                        |
| docutils       | 2.86 sec                                                                  | 2.89 sec: 1.01x slower                                                       |
| html5lib       | 70.2 ms                                                                   | 68.9 ms: 1.02x faster                                                        |
| tornado_http   | 125 ms                                                                    | 119 ms: 1.05x faster                                                         |
| Geometric mean | (ref)                                                                     | 1.02x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230422-pythonperf2-x86_64-python-ea2c0016502472aa8baa-3.12.0a7+-ea2c001 |
|----------------|:-------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 92.1 ms                                                                   | 83.7 ms: 1.10x faster                                                        |
| float          | 75.7 ms                                                                   | 77.1 ms: 1.02x slower                                                        |
| pidigits       | 252 ms                                                                    | 260 ms: 1.03x slower                                                         |
| Geometric mean | (ref)                                                                     | 1.01x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230422-pythonperf2-x86_64-python-ea2c0016502472aa8baa-3.12.0a7+-ea2c001 |
|----------------|:-------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 154 ms                                                                    | 143 ms: 1.08x faster                                                         |
| regex_v8       | 24.4 ms                                                                   | 23.6 ms: 1.03x faster                                                        |
| regex_dna      | 225 ms                                                                    | 230 ms: 1.02x slower                                                         |
| regex_effbot   | 3.31 ms                                                                   | 3.40 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                                     | 1.02x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230422-pythonperf2-x86_64-python-ea2c0016502472aa8baa-3.12.0a7+-ea2c001 |
|----------------------|:-------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| json_dumps           | 13.4 ms                                                                   | 10.3 ms: 1.30x faster                                                        |
| json_loads           | 28.4 us                                                                   | 24.7 us: 1.15x faster                                                        |
| unpickle_pure_python | 238 us                                                                    | 209 us: 1.14x faster                                                         |
| xml_etree_parse      | 161 ms                                                                    | 151 ms: 1.06x faster                                                         |
| pickle_dict          | 31.1 us                                                                   | 30.7 us: 1.01x faster                                                        |
| pickle_pure_python   | 319 us                                                                    | 319 us: 1.00x faster                                                         |
| pickle_list          | 3.78 us                                                                   | 3.95 us: 1.05x slower                                                        |
| xml_etree_process    | 55.8 ms                                                                   | 58.5 ms: 1.05x slower                                                        |
| xml_etree_generate   | 79.1 ms                                                                   | 85.2 ms: 1.08x slower                                                        |
| unpickle             | 13.0 us                                                                   | 14.2 us: 1.09x slower                                                        |
| Geometric mean       | (ref)                                                                     | 1.03x faster                                                                 |

Benchmark hidden because not significant (3): xml_etree_iterparse, pickle, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230422-pythonperf2-x86_64-python-ea2c0016502472aa8baa-3.12.0a7+-ea2c001 |
|------------------------|:-------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 10.7 ms                                                                   | 11.1 ms: 1.04x slower                                                        |
| python_startup_no_site | 7.73 ms                                                                   | 8.37 ms: 1.08x slower                                                        |
| Geometric mean         | (ref)                                                                     | 1.06x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230422-pythonperf2-x86_64-python-ea2c0016502472aa8baa-3.12.0a7+-ea2c001 |
|-----------------|:-------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 10.9 ms                                                                   | 10.0 ms: 1.09x faster                                                        |
| genshi_xml      | 57.8 ms                                                                   | 53.9 ms: 1.07x faster                                                        |
| genshi_text     | 26.3 ms                                                                   | 25.0 ms: 1.05x faster                                                        |
| django_template | 39.6 ms                                                                   | 38.3 ms: 1.03x faster                                                        |
| Geometric mean  | (ref)                                                                     | 1.06x faster                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230422-pythonperf2-x86_64-python-ea2c0016502472aa8baa-3.12.0a7+-ea2c001 |
|-------------------------|:-------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| asyncio_tcp             | 752 ms                                                                    | 379 ms: 1.98x faster                                                         |
| generators              | 56.0 ms                                                                   | 36.6 ms: 1.53x faster                                                        |
| json_dumps              | 13.4 ms                                                                   | 10.3 ms: 1.30x faster                                                        |
| coroutines              | 29.5 ms                                                                   | 22.7 ms: 1.30x faster                                                        |
| fannkuch                | 449 ms                                                                    | 351 ms: 1.28x faster                                                         |
| deltablue               | 3.99 ms                                                                   | 3.30 ms: 1.21x faster                                                        |
| scimark_lu              | 114 ms                                                                    | 95.5 ms: 1.20x faster                                                        |
| hexiom                  | 7.00 ms                                                                   | 5.92 ms: 1.18x faster                                                        |
| json_loads              | 28.4 us                                                                   | 24.7 us: 1.15x faster                                                        |
| mypy2                   | 446 ms                                                                    | 388 ms: 1.15x faster                                                         |
| chaos                   | 76.2 ms                                                                   | 66.3 ms: 1.15x faster                                                        |
| unpickle_pure_python    | 238 us                                                                    | 209 us: 1.14x faster                                                         |
| nqueens                 | 101 ms                                                                    | 90.1 ms: 1.12x faster                                                        |
| richards                | 49.1 ms                                                                   | 43.9 ms: 1.12x faster                                                        |
| sqlglot_parse           | 1.53 ms                                                                   | 1.38 ms: 1.11x faster                                                        |
| spectral_norm           | 95.1 ms                                                                   | 86.0 ms: 1.11x faster                                                        |
| nbody                   | 92.1 ms                                                                   | 83.7 ms: 1.10x faster                                                        |
| logging_silent          | 103 ns                                                                    | 93.5 ns: 1.10x faster                                                        |
| json                    | 5.59 ms                                                                   | 5.13 ms: 1.09x faster                                                        |
| mako                    | 10.9 ms                                                                   | 10.0 ms: 1.09x faster                                                        |
| go                      | 158 ms                                                                    | 146 ms: 1.08x faster                                                         |
| regex_compile           | 154 ms                                                                    | 143 ms: 1.08x faster                                                         |
| async_tree_memoization  | 639 ms                                                                    | 594 ms: 1.08x faster                                                         |
| crypto_pyaes            | 85.0 ms                                                                   | 79.0 ms: 1.08x faster                                                        |
| mdp                     | 2.73 sec                                                                  | 2.54 sec: 1.07x faster                                                       |
| genshi_xml              | 57.8 ms                                                                   | 53.9 ms: 1.07x faster                                                        |
| logging_format          | 7.84 us                                                                   | 7.32 us: 1.07x faster                                                        |
| xml_etree_parse         | 161 ms                                                                    | 151 ms: 1.06x faster                                                         |
| dulwich_log             | 69.1 ms                                                                   | 65.0 ms: 1.06x faster                                                        |
| thrift                  | 942 us                                                                    | 887 us: 1.06x faster                                                         |
| sqlglot_transpile       | 1.88 ms                                                                   | 1.78 ms: 1.05x faster                                                        |
| logging_simple          | 6.95 us                                                                   | 6.60 us: 1.05x faster                                                        |
| genshi_text             | 26.3 ms                                                                   | 25.0 ms: 1.05x faster                                                        |
| gc_traversal            | 4.22 ms                                                                   | 4.02 ms: 1.05x faster                                                        |
| tornado_http            | 125 ms                                                                    | 119 ms: 1.05x faster                                                         |
| async_tree_none         | 529 ms                                                                    | 505 ms: 1.05x faster                                                         |
| pylint                  | 517 ms                                                                    | 498 ms: 1.04x faster                                                         |
| regex_v8                | 24.4 ms                                                                   | 23.6 ms: 1.03x faster                                                        |
| pycparser               | 1.30 sec                                                                  | 1.26 sec: 1.03x faster                                                       |
| django_template         | 39.6 ms                                                                   | 38.3 ms: 1.03x faster                                                        |
| sympy_expand            | 547 ms                                                                    | 529 ms: 1.03x faster                                                         |
| pathlib                 | 19.2 ms                                                                   | 18.6 ms: 1.03x faster                                                        |
| async_tree_io           | 1.18 sec                                                                  | 1.15 sec: 1.03x faster                                                       |
| bench_thread_pool       | 990 us                                                                    | 966 us: 1.02x faster                                                         |
| sympy_str               | 333 ms                                                                    | 325 ms: 1.02x faster                                                         |
| async_tree_cpu_io_mixed | 754 ms                                                                    | 739 ms: 1.02x faster                                                         |
| html5lib                | 70.2 ms                                                                   | 68.9 ms: 1.02x faster                                                        |
| comprehensions          | 24.7 us                                                                   | 24.3 us: 1.02x faster                                                        |
| 2to3                    | 289 ms                                                                    | 284 ms: 1.02x faster                                                         |
| pickle_dict             | 31.1 us                                                                   | 30.7 us: 1.01x faster                                                        |
| raytrace                | 303 ms                                                                    | 299 ms: 1.01x faster                                                         |
| sqlglot_normalize       | 122 ms                                                                    | 121 ms: 1.01x faster                                                         |
| scimark_sparse_mat_mult | 4.06 ms                                                                   | 4.01 ms: 1.01x faster                                                        |
| chameleon               | 7.50 ms                                                                   | 7.44 ms: 1.01x faster                                                        |
| sympy_sum               | 182 ms                                                                    | 182 ms: 1.00x faster                                                         |
| pickle_pure_python      | 319 us                                                                    | 319 us: 1.00x faster                                                         |
| sqlglot_optimize        | 58.6 ms                                                                   | 59.0 ms: 1.01x slower                                                        |
| scimark_sor             | 109 ms                                                                    | 110 ms: 1.01x slower                                                         |
| docutils                | 2.86 sec                                                                  | 2.89 sec: 1.01x slower                                                       |
| deepcopy_memo           | 37.0 us                                                                   | 37.5 us: 1.01x slower                                                        |
| deepcopy_reduce         | 3.39 us                                                                   | 3.45 us: 1.02x slower                                                        |
| float                   | 75.7 ms                                                                   | 77.1 ms: 1.02x slower                                                        |
| create_gc_cycles        | 1.65 ms                                                                   | 1.68 ms: 1.02x slower                                                        |
| regex_dna               | 225 ms                                                                    | 230 ms: 1.02x slower                                                         |
| regex_effbot            | 3.31 ms                                                                   | 3.40 ms: 1.03x slower                                                        |
| pprint_pformat          | 1.60 sec                                                                  | 1.65 sec: 1.03x slower                                                       |
| pidigits                | 252 ms                                                                    | 260 ms: 1.03x slower                                                         |
| coverage                | 86.0 ms                                                                   | 89.2 ms: 1.04x slower                                                        |
| python_startup          | 10.7 ms                                                                   | 11.1 ms: 1.04x slower                                                        |
| pickle_list             | 3.78 us                                                                   | 3.95 us: 1.05x slower                                                        |
| pyflate                 | 438 ms                                                                    | 458 ms: 1.05x slower                                                         |
| xml_etree_process       | 55.8 ms                                                                   | 58.5 ms: 1.05x slower                                                        |
| telco                   | 6.70 ms                                                                   | 7.04 ms: 1.05x slower                                                        |
| scimark_fft             | 276 ms                                                                    | 292 ms: 1.06x slower                                                         |
| pprint_safe_repr        | 768 ms                                                                    | 811 ms: 1.06x slower                                                         |
| meteor_contest          | 129 ms                                                                    | 138 ms: 1.07x slower                                                         |
| sqlite_synth            | 2.49 us                                                                   | 2.66 us: 1.07x slower                                                        |
| xml_etree_generate      | 79.1 ms                                                                   | 85.2 ms: 1.08x slower                                                        |
| python_startup_no_site  | 7.73 ms                                                                   | 8.37 ms: 1.08x slower                                                        |
| unpickle                | 13.0 us                                                                   | 14.2 us: 1.09x slower                                                        |
| unpack_sequence         | 45.9 ns                                                                   | 52.8 ns: 1.15x slower                                                        |
| async_generators        | 318 ms                                                                    | 386 ms: 1.21x slower                                                         |
| bench_mp_pool           | 4.54 ms                                                                   | 6.08 ms: 1.34x slower                                                        |
| dask                    | 418 ms                                                                    | 563 ms: 1.35x slower                                                         |
| Geometric mean          | (ref)                                                                     | 1.04x faster                                                                 |

Benchmark hidden because not significant (6): xml_etree_iterparse, pickle, sympy_integrate, deepcopy, scimark_monte_carlo, unpickle_list
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: aiohttp, flaskblogging, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative
