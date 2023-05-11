
# Results vs. 3.11.0

- fork: faster-cpython
- ref: instrument_all_possi
- machine: linux-x86_64
- commit hash: 5418580
- commit date: 2023-05-10
- overall geometric mean: 1.04x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230510-pythonperf2-x86_64-faster%2dcpython-instrument_all_possi-3.12.0a7+-5418580 |
|----------------|:-------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| 2to3           | 289 ms                                                                    | 285 ms: 1.02x faster                                                                   |
| docutils       | 2.86 sec                                                                  | 2.88 sec: 1.01x slower                                                                 |
| tornado_http   | 125 ms                                                                    | 113 ms: 1.10x faster                                                                   |
| Geometric mean | (ref)                                                                     | 1.04x faster                                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230510-pythonperf2-x86_64-faster%2dcpython-instrument_all_possi-3.12.0a7+-5418580 |
|----------------|:-------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| nbody          | 92.1 ms                                                                   | 84.7 ms: 1.09x faster                                                                  |
| pidigits       | 252 ms                                                                    | 261 ms: 1.04x slower                                                                   |
| float          | 75.7 ms                                                                   | 79.0 ms: 1.04x slower                                                                  |
| Geometric mean | (ref)                                                                     | 1.00x faster                                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230510-pythonperf2-x86_64-faster%2dcpython-instrument_all_possi-3.12.0a7+-5418580 |
|----------------|:-------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| regex_compile  | 154 ms                                                                    | 144 ms: 1.07x faster                                                                   |
| regex_v8       | 24.4 ms                                                                   | 23.4 ms: 1.04x faster                                                                  |
| regex_dna      | 225 ms                                                                    | 227 ms: 1.01x slower                                                                   |
| regex_effbot   | 3.31 ms                                                                   | 3.41 ms: 1.03x slower                                                                  |
| Geometric mean | (ref)                                                                     | 1.02x faster                                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230510-pythonperf2-x86_64-faster%2dcpython-instrument_all_possi-3.12.0a7+-5418580 |
|----------------------|:-------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| json_dumps           | 13.4 ms                                                                   | 10.2 ms: 1.31x faster                                                                  |
| json_loads           | 28.4 us                                                                   | 24.5 us: 1.16x faster                                                                  |
| unpickle_pure_python | 238 us                                                                    | 205 us: 1.16x faster                                                                   |
| xml_etree_parse      | 161 ms                                                                    | 149 ms: 1.08x faster                                                                   |
| xml_etree_iterparse  | 106 ms                                                                    | 104 ms: 1.02x faster                                                                   |
| pickle               | 9.92 us                                                                   | 10.3 us: 1.04x slower                                                                  |
| unpickle_list        | 4.52 us                                                                   | 4.72 us: 1.04x slower                                                                  |
| pickle_dict          | 31.1 us                                                                   | 32.6 us: 1.05x slower                                                                  |
| xml_etree_process    | 55.8 ms                                                                   | 58.7 ms: 1.05x slower                                                                  |
| xml_etree_generate   | 79.1 ms                                                                   | 85.6 ms: 1.08x slower                                                                  |
| unpickle             | 13.0 us                                                                   | 14.9 us: 1.14x slower                                                                  |
| pickle_list          | 3.78 us                                                                   | 4.45 us: 1.18x slower                                                                  |
| Geometric mean       | (ref)                                                                     | 1.01x faster                                                                           |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230510-pythonperf2-x86_64-faster%2dcpython-instrument_all_possi-3.12.0a7+-5418580 |
|------------------------|:-------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| python_startup         | 10.7 ms                                                                   | 11.3 ms: 1.05x slower                                                                  |
| python_startup_no_site | 7.73 ms                                                                   | 8.38 ms: 1.08x slower                                                                  |
| Geometric mean         | (ref)                                                                     | 1.07x slower                                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230510-pythonperf2-x86_64-faster%2dcpython-instrument_all_possi-3.12.0a7+-5418580 |
|-----------|:-------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| mako      | 10.9 ms                                                                   | 10.2 ms: 1.07x faster                                                                  |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230510-pythonperf2-x86_64-faster%2dcpython-instrument_all_possi-3.12.0a7+-5418580 |
|-------------------------|:-------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| asyncio_tcp             | 752 ms                                                                    | 379 ms: 1.98x faster                                                                   |
| generators              | 56.0 ms                                                                   | 36.4 ms: 1.54x faster                                                                  |
| fannkuch                | 449 ms                                                                    | 343 ms: 1.31x faster                                                                   |
| json_dumps              | 13.4 ms                                                                   | 10.2 ms: 1.31x faster                                                                  |
| coroutines              | 29.5 ms                                                                   | 22.6 ms: 1.30x faster                                                                  |
| deltablue               | 3.99 ms                                                                   | 3.22 ms: 1.24x faster                                                                  |
| mypy2                   | 446 ms                                                                    | 369 ms: 1.21x faster                                                                   |
| hexiom                  | 7.00 ms                                                                   | 5.79 ms: 1.21x faster                                                                  |
| chaos                   | 76.2 ms                                                                   | 64.3 ms: 1.19x faster                                                                  |
| async_tree_memoization  | 639 ms                                                                    | 546 ms: 1.17x faster                                                                   |
| async_tree_none         | 529 ms                                                                    | 455 ms: 1.16x faster                                                                   |
| json_loads              | 28.4 us                                                                   | 24.5 us: 1.16x faster                                                                  |
| unpickle_pure_python    | 238 us                                                                    | 205 us: 1.16x faster                                                                   |
| scimark_lu              | 114 ms                                                                    | 99.6 ms: 1.15x faster                                                                  |
| async_tree_io           | 1.18 sec                                                                  | 1.05 sec: 1.13x faster                                                                 |
| richards                | 49.1 ms                                                                   | 43.5 ms: 1.13x faster                                                                  |
| logging_silent          | 103 ns                                                                    | 91.1 ns: 1.13x faster                                                                  |
| comprehensions          | 24.7 us                                                                   | 22.0 us: 1.12x faster                                                                  |
| nqueens                 | 101 ms                                                                    | 90.1 ms: 1.12x faster                                                                  |
| tornado_http            | 125 ms                                                                    | 113 ms: 1.10x faster                                                                   |
| sqlglot_parse           | 1.53 ms                                                                   | 1.39 ms: 1.10x faster                                                                  |
| go                      | 158 ms                                                                    | 144 ms: 1.10x faster                                                                   |
| nbody                   | 92.1 ms                                                                   | 84.7 ms: 1.09x faster                                                                  |
| async_tree_cpu_io_mixed | 754 ms                                                                    | 698 ms: 1.08x faster                                                                   |
| json                    | 5.59 ms                                                                   | 5.18 ms: 1.08x faster                                                                  |
| mdp                     | 2.73 sec                                                                  | 2.53 sec: 1.08x faster                                                                 |
| xml_etree_parse         | 161 ms                                                                    | 149 ms: 1.08x faster                                                                   |
| crypto_pyaes            | 85.0 ms                                                                   | 79.2 ms: 1.07x faster                                                                  |
| mako                    | 10.9 ms                                                                   | 10.2 ms: 1.07x faster                                                                  |
| regex_compile           | 154 ms                                                                    | 144 ms: 1.07x faster                                                                   |
| dulwich_log             | 69.1 ms                                                                   | 65.9 ms: 1.05x faster                                                                  |
| sqlglot_transpile       | 1.88 ms                                                                   | 1.79 ms: 1.05x faster                                                                  |
| logging_format          | 7.84 us                                                                   | 7.51 us: 1.04x faster                                                                  |
| regex_v8                | 24.4 ms                                                                   | 23.4 ms: 1.04x faster                                                                  |
| pycparser               | 1.30 sec                                                                  | 1.25 sec: 1.04x faster                                                                 |
| gc_traversal            | 4.22 ms                                                                   | 4.06 ms: 1.04x faster                                                                  |
| sqlglot_normalize       | 122 ms                                                                    | 118 ms: 1.04x faster                                                                   |
| bench_thread_pool       | 990 us                                                                    | 959 us: 1.03x faster                                                                   |
| spectral_norm           | 95.1 ms                                                                   | 92.6 ms: 1.03x faster                                                                  |
| unpack_sequence         | 45.9 ns                                                                   | 44.8 ns: 1.02x faster                                                                  |
| deepcopy                | 384 us                                                                    | 375 us: 1.02x faster                                                                   |
| logging_simple          | 6.95 us                                                                   | 6.80 us: 1.02x faster                                                                  |
| xml_etree_iterparse     | 106 ms                                                                    | 104 ms: 1.02x faster                                                                   |
| 2to3                    | 289 ms                                                                    | 285 ms: 1.02x faster                                                                   |
| raytrace                | 303 ms                                                                    | 299 ms: 1.01x faster                                                                   |
| meteor_contest          | 129 ms                                                                    | 128 ms: 1.01x faster                                                                   |
| deepcopy_memo           | 37.0 us                                                                   | 37.2 us: 1.01x slower                                                                  |
| docutils                | 2.86 sec                                                                  | 2.88 sec: 1.01x slower                                                                 |
| regex_dna               | 225 ms                                                                    | 227 ms: 1.01x slower                                                                   |
| deepcopy_reduce         | 3.39 us                                                                   | 3.45 us: 1.02x slower                                                                  |
| pprint_pformat          | 1.60 sec                                                                  | 1.64 sec: 1.02x slower                                                                 |
| coverage                | 86.0 ms                                                                   | 88.5 ms: 1.03x slower                                                                  |
| regex_effbot            | 3.31 ms                                                                   | 3.41 ms: 1.03x slower                                                                  |
| pidigits                | 252 ms                                                                    | 261 ms: 1.04x slower                                                                   |
| pprint_safe_repr        | 768 ms                                                                    | 798 ms: 1.04x slower                                                                   |
| pickle                  | 9.92 us                                                                   | 10.3 us: 1.04x slower                                                                  |
| scimark_sparse_mat_mult | 4.06 ms                                                                   | 4.23 ms: 1.04x slower                                                                  |
| float                   | 75.7 ms                                                                   | 79.0 ms: 1.04x slower                                                                  |
| unpickle_list           | 4.52 us                                                                   | 4.72 us: 1.04x slower                                                                  |
| pathlib                 | 19.2 ms                                                                   | 20.1 ms: 1.05x slower                                                                  |
| pickle_dict             | 31.1 us                                                                   | 32.6 us: 1.05x slower                                                                  |
| xml_etree_process       | 55.8 ms                                                                   | 58.7 ms: 1.05x slower                                                                  |
| python_startup          | 10.7 ms                                                                   | 11.3 ms: 1.05x slower                                                                  |
| pyflate                 | 438 ms                                                                    | 461 ms: 1.05x slower                                                                   |
| sqlite_synth            | 2.49 us                                                                   | 2.66 us: 1.07x slower                                                                  |
| scimark_fft             | 276 ms                                                                    | 298 ms: 1.08x slower                                                                   |
| telco                   | 6.70 ms                                                                   | 7.23 ms: 1.08x slower                                                                  |
| xml_etree_generate      | 79.1 ms                                                                   | 85.6 ms: 1.08x slower                                                                  |
| python_startup_no_site  | 7.73 ms                                                                   | 8.38 ms: 1.08x slower                                                                  |
| unpickle                | 13.0 us                                                                   | 14.9 us: 1.14x slower                                                                  |
| pickle_list             | 3.78 us                                                                   | 4.45 us: 1.18x slower                                                                  |
| async_generators        | 318 ms                                                                    | 380 ms: 1.19x slower                                                                   |
| dask                    | 418 ms                                                                    | 556 ms: 1.33x slower                                                                   |
| bench_mp_pool           | 4.54 ms                                                                   | 7.35 ms: 1.62x slower                                                                  |
| Geometric mean          | (ref)                                                                     | 1.04x faster                                                                           |

Benchmark hidden because not significant (5): create_gc_cycles, sqlglot_optimize, scimark_sor, pickle_pure_python, scimark_monte_carlo
Ignored benchmarks (16) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: aiohttp, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
