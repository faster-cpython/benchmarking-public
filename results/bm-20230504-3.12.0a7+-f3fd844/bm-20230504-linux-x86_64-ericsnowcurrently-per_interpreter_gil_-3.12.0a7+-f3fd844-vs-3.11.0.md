
# Results vs. 3.11.0

- fork: ericsnowcurrently
- ref: per_interpreter_gil_
- machine: linux-x86_64
- commit hash: f3fd844
- commit date: 2023-05-04
- overall geometric mean: 1.02x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230504-linux-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 257 ms                                                              | 272 ms: 1.06x slower                                                              |
| docutils       | 2.59 sec                                                            | 2.74 sec: 1.06x slower                                                            |
| tornado_http   | 96.7 ms                                                             | 100 ms: 1.04x slower                                                              |
| Geometric mean | (ref)                                                               | 1.05x slower                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230504-linux-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| nbody          | 96.7 ms                                                             | 90.1 ms: 1.07x faster                                                             |
| pidigits       | 197 ms                                                              | 197 ms: 1.00x slower                                                              |
| float          | 76.0 ms                                                             | 82.4 ms: 1.09x slower                                                             |
| Geometric mean | (ref)                                                               | 1.00x slower                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230504-linux-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_v8       | 22.0 ms                                                             | 22.2 ms: 1.01x slower                                                             |
| regex_dna      | 196 ms                                                              | 204 ms: 1.04x slower                                                              |
| regex_compile  | 137 ms                                                              | 146 ms: 1.07x slower                                                              |
| regex_effbot   | 3.32 ms                                                             | 3.66 ms: 1.10x slower                                                             |
| Geometric mean | (ref)                                                               | 1.06x slower                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230504-linux-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|----------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| json_dumps           | 12.5 ms                                                             | 10.1 ms: 1.24x faster                                                             |
| xml_etree_parse      | 162 ms                                                              | 154 ms: 1.06x faster                                                              |
| json_loads           | 26.2 us                                                             | 25.1 us: 1.04x faster                                                             |
| xml_etree_iterparse  | 108 ms                                                              | 104 ms: 1.04x faster                                                              |
| unpickle_pure_python | 228 us                                                              | 222 us: 1.03x faster                                                              |
| unpickle_list        | 4.96 us                                                             | 4.83 us: 1.03x faster                                                             |
| pickle_dict          | 30.9 us                                                             | 30.4 us: 1.02x faster                                                             |
| pickle_pure_python   | 307 us                                                              | 320 us: 1.04x slower                                                              |
| pickle               | 9.79 us                                                             | 10.7 us: 1.09x slower                                                             |
| unpickle             | 13.2 us                                                             | 14.6 us: 1.10x slower                                                             |
| xml_etree_process    | 54.1 ms                                                             | 59.9 ms: 1.11x slower                                                             |
| xml_etree_generate   | 76.5 ms                                                             | 85.1 ms: 1.11x slower                                                             |
| pickle_list          | 4.03 us                                                             | 4.57 us: 1.13x slower                                                             |
| Geometric mean       | (ref)                                                               | 1.01x slower                                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230504-linux-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|------------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 8.49 ms                                                             | 9.14 ms: 1.08x slower                                                             |
| python_startup_no_site | 5.98 ms                                                             | 6.69 ms: 1.12x slower                                                             |
| Geometric mean         | (ref)                                                               | 1.10x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230504-linux-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|-----------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako      | 9.82 ms                                                             | 10.6 ms: 1.08x slower                                                             |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230504-linux-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|-------------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| generators              | 73.4 ms                                                             | 31.4 ms: 2.34x faster                                                             |
| asyncio_tcp             | 888 ms                                                              | 510 ms: 1.74x faster                                                              |
| json_dumps              | 12.5 ms                                                             | 10.1 ms: 1.24x faster                                                             |
| mypy2                   | 422 ms                                                              | 353 ms: 1.19x faster                                                              |
| coroutines              | 26.3 ms                                                             | 23.1 ms: 1.14x faster                                                             |
| nbody                   | 96.7 ms                                                             | 90.1 ms: 1.07x faster                                                             |
| xml_etree_parse         | 162 ms                                                              | 154 ms: 1.06x faster                                                              |
| async_tree_none         | 525 ms                                                              | 502 ms: 1.05x faster                                                              |
| async_tree_io           | 1.28 sec                                                            | 1.23 sec: 1.05x faster                                                            |
| json_loads              | 26.2 us                                                             | 25.1 us: 1.04x faster                                                             |
| xml_etree_iterparse     | 108 ms                                                              | 104 ms: 1.04x faster                                                              |
| richards                | 45.7 ms                                                             | 44.1 ms: 1.04x faster                                                             |
| deltablue               | 3.66 ms                                                             | 3.54 ms: 1.03x faster                                                             |
| unpickle_pure_python    | 228 us                                                              | 222 us: 1.03x faster                                                              |
| unpickle_list           | 4.96 us                                                             | 4.83 us: 1.03x faster                                                             |
| sqlglot_parse           | 1.36 ms                                                             | 1.34 ms: 1.02x faster                                                             |
| pickle_dict             | 30.9 us                                                             | 30.4 us: 1.02x faster                                                             |
| async_tree_cpu_io_mixed | 736 ms                                                              | 726 ms: 1.01x faster                                                              |
| create_gc_cycles        | 1.48 ms                                                             | 1.46 ms: 1.01x faster                                                             |
| mdp                     | 2.64 sec                                                            | 2.61 sec: 1.01x faster                                                            |
| hexiom                  | 6.48 ms                                                             | 6.43 ms: 1.01x faster                                                             |
| unpack_sequence         | 49.5 ns                                                             | 49.1 ns: 1.01x faster                                                             |
| pidigits                | 197 ms                                                              | 197 ms: 1.00x slower                                                              |
| sqlglot_transpile       | 1.65 ms                                                             | 1.67 ms: 1.01x slower                                                             |
| nqueens                 | 84.0 ms                                                             | 84.9 ms: 1.01x slower                                                             |
| coverage                | 101 ms                                                              | 102 ms: 1.01x slower                                                              |
| regex_v8                | 22.0 ms                                                             | 22.2 ms: 1.01x slower                                                             |
| pycparser               | 1.14 sec                                                            | 1.16 sec: 1.01x slower                                                            |
| go                      | 138 ms                                                              | 141 ms: 1.02x slower                                                              |
| pathlib                 | 18.2 ms                                                             | 18.6 ms: 1.02x slower                                                             |
| bench_thread_pool       | 820 us                                                              | 842 us: 1.03x slower                                                              |
| chaos                   | 68.0 ms                                                             | 70.3 ms: 1.03x slower                                                             |
| tornado_http            | 96.7 ms                                                             | 100 ms: 1.04x slower                                                              |
| telco                   | 6.59 ms                                                             | 6.84 ms: 1.04x slower                                                             |
| regex_dna               | 196 ms                                                              | 204 ms: 1.04x slower                                                              |
| pickle_pure_python      | 307 us                                                              | 320 us: 1.04x slower                                                              |
| comprehensions          | 22.2 us                                                             | 23.2 us: 1.04x slower                                                             |
| sqlglot_optimize        | 53.4 ms                                                             | 55.5 ms: 1.04x slower                                                             |
| logging_silent          | 98.7 ns                                                             | 103 ns: 1.04x slower                                                              |
| pprint_pformat          | 1.45 sec                                                            | 1.52 sec: 1.05x slower                                                            |
| sqlglot_normalize       | 108 ms                                                              | 114 ms: 1.05x slower                                                              |
| raytrace                | 292 ms                                                              | 307 ms: 1.05x slower                                                              |
| logging_simple          | 6.09 us                                                             | 6.43 us: 1.06x slower                                                             |
| sqlalchemy_imperative   | 18.0 ms                                                             | 19.0 ms: 1.06x slower                                                             |
| 2to3                    | 257 ms                                                              | 272 ms: 1.06x slower                                                              |
| docutils                | 2.59 sec                                                            | 2.74 sec: 1.06x slower                                                            |
| scimark_lu              | 108 ms                                                              | 115 ms: 1.06x slower                                                              |
| scimark_sparse_mat_mult | 4.47 ms                                                             | 4.75 ms: 1.06x slower                                                             |
| sqlalchemy_declarative  | 138 ms                                                              | 147 ms: 1.06x slower                                                              |
| logging_format          | 6.64 us                                                             | 7.08 us: 1.07x slower                                                             |
| crypto_pyaes            | 73.8 ms                                                             | 78.7 ms: 1.07x slower                                                             |
| pprint_safe_repr        | 701 ms                                                              | 749 ms: 1.07x slower                                                              |
| regex_compile           | 137 ms                                                              | 146 ms: 1.07x slower                                                              |
| sqlite_synth            | 2.51 us                                                             | 2.69 us: 1.07x slower                                                             |
| python_startup          | 8.49 ms                                                             | 9.14 ms: 1.08x slower                                                             |
| scimark_monte_carlo     | 67.8 ms                                                             | 73.0 ms: 1.08x slower                                                             |
| dulwich_log             | 63.6 ms                                                             | 68.5 ms: 1.08x slower                                                             |
| pyflate                 | 414 ms                                                              | 446 ms: 1.08x slower                                                              |
| deepcopy_memo           | 36.4 us                                                             | 39.3 us: 1.08x slower                                                             |
| spectral_norm           | 99.5 ms                                                             | 108 ms: 1.08x slower                                                              |
| scimark_sor             | 115 ms                                                              | 124 ms: 1.08x slower                                                              |
| scimark_fft             | 328 ms                                                              | 355 ms: 1.08x slower                                                              |
| mako                    | 9.82 ms                                                             | 10.6 ms: 1.08x slower                                                             |
| float                   | 76.0 ms                                                             | 82.4 ms: 1.09x slower                                                             |
| pickle                  | 9.79 us                                                             | 10.7 us: 1.09x slower                                                             |
| regex_effbot            | 3.32 ms                                                             | 3.66 ms: 1.10x slower                                                             |
| deepcopy_reduce         | 2.96 us                                                             | 3.26 us: 1.10x slower                                                             |
| unpickle                | 13.2 us                                                             | 14.6 us: 1.10x slower                                                             |
| deepcopy                | 339 us                                                              | 374 us: 1.10x slower                                                              |
| xml_etree_process       | 54.1 ms                                                             | 59.9 ms: 1.11x slower                                                             |
| xml_etree_generate      | 76.5 ms                                                             | 85.1 ms: 1.11x slower                                                             |
| gc_traversal            | 3.63 ms                                                             | 4.04 ms: 1.11x slower                                                             |
| meteor_contest          | 106 ms                                                              | 118 ms: 1.12x slower                                                              |
| python_startup_no_site  | 5.98 ms                                                             | 6.69 ms: 1.12x slower                                                             |
| pickle_list             | 4.03 us                                                             | 4.57 us: 1.13x slower                                                             |
| async_generators        | 361 ms                                                              | 450 ms: 1.24x slower                                                              |
| dask                    | 368 ms                                                              | 543 ms: 1.47x slower                                                              |
| Geometric mean          | (ref)                                                               | 1.02x slower                                                                      |

Benchmark hidden because not significant (4): async_tree_memoization, json, fannkuch, bench_mp_pool
Ignored benchmarks (15) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
