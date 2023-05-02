
# Results vs. 3.11.0

- fork: ericsnowcurrently
- ref: per_interpreter_stat
- machine: linux-x86_64
- commit hash: 071ef3f
- commit date: 2023-05-01
- overall geometric mean: 1.01x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230501-linux-x86_64-ericsnowcurrently-per_interpreter_stat-3.12.0a7+-071ef3f |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 257 ms                                                              | 271 ms: 1.05x slower                                                              |
| docutils       | 2.59 sec                                                            | 2.72 sec: 1.05x slower                                                            |
| tornado_http   | 96.7 ms                                                             | 102 ms: 1.06x slower                                                              |
| Geometric mean | (ref)                                                               | 1.04x slower                                                                      |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230501-linux-x86_64-ericsnowcurrently-per_interpreter_stat-3.12.0a7+-071ef3f |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| nbody          | 96.7 ms                                                             | 87.4 ms: 1.11x faster                                                             |
| pidigits       | 197 ms                                                              | 189 ms: 1.04x faster                                                              |
| float          | 76.0 ms                                                             | 81.2 ms: 1.07x slower                                                             |
| Geometric mean | (ref)                                                               | 1.03x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230501-linux-x86_64-ericsnowcurrently-per_interpreter_stat-3.12.0a7+-071ef3f |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_v8       | 22.0 ms                                                             | 22.4 ms: 1.02x slower                                                             |
| regex_effbot   | 3.32 ms                                                             | 3.40 ms: 1.02x slower                                                             |
| regex_compile  | 137 ms                                                              | 144 ms: 1.06x slower                                                              |
| regex_dna      | 196 ms                                                              | 209 ms: 1.07x slower                                                              |
| Geometric mean | (ref)                                                               | 1.04x slower                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230501-linux-x86_64-ericsnowcurrently-per_interpreter_stat-3.12.0a7+-071ef3f |
|----------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| json_dumps           | 12.5 ms                                                             | 10.1 ms: 1.24x faster                                                             |
| xml_etree_parse      | 162 ms                                                              | 153 ms: 1.06x faster                                                              |
| unpickle_pure_python | 228 us                                                              | 218 us: 1.05x faster                                                              |
| xml_etree_iterparse  | 108 ms                                                              | 104 ms: 1.04x faster                                                              |
| pickle_pure_python   | 307 us                                                              | 316 us: 1.03x slower                                                              |
| pickle_dict          | 30.9 us                                                             | 32.4 us: 1.05x slower                                                             |
| unpickle             | 13.2 us                                                             | 14.4 us: 1.09x slower                                                             |
| pickle               | 9.79 us                                                             | 10.8 us: 1.11x slower                                                             |
| xml_etree_process    | 54.1 ms                                                             | 60.4 ms: 1.12x slower                                                             |
| xml_etree_generate   | 76.5 ms                                                             | 85.8 ms: 1.12x slower                                                             |
| pickle_list          | 4.03 us                                                             | 4.60 us: 1.14x slower                                                             |
| Geometric mean       | (ref)                                                               | 1.02x slower                                                                      |

Benchmark hidden because not significant (2): json_loads, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230501-linux-x86_64-ericsnowcurrently-per_interpreter_stat-3.12.0a7+-071ef3f |
|------------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 8.49 ms                                                             | 9.15 ms: 1.08x slower                                                             |
| python_startup_no_site | 5.98 ms                                                             | 6.71 ms: 1.12x slower                                                             |
| Geometric mean         | (ref)                                                               | 1.10x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230501-linux-x86_64-ericsnowcurrently-per_interpreter_stat-3.12.0a7+-071ef3f |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| genshi_xml     | 51.8 ms                                                             | 50.8 ms: 1.02x faster                                                             |
| genshi_text    | 21.8 ms                                                             | 22.3 ms: 1.02x slower                                                             |
| mako           | 9.82 ms                                                             | 10.7 ms: 1.09x slower                                                             |
| Geometric mean | (ref)                                                               | 1.03x slower                                                                      |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230501-linux-x86_64-ericsnowcurrently-per_interpreter_stat-3.12.0a7+-071ef3f |
|-------------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| generators              | 73.4 ms                                                             | 30.7 ms: 2.39x faster                                                             |
| asyncio_tcp             | 888 ms                                                              | 513 ms: 1.73x faster                                                              |
| json_dumps              | 12.5 ms                                                             | 10.1 ms: 1.24x faster                                                             |
| mypy2                   | 422 ms                                                              | 352 ms: 1.20x faster                                                              |
| coroutines              | 26.3 ms                                                             | 22.4 ms: 1.17x faster                                                             |
| nbody                   | 96.7 ms                                                             | 87.4 ms: 1.11x faster                                                             |
| hexiom                  | 6.48 ms                                                             | 6.12 ms: 1.06x faster                                                             |
| richards                | 45.7 ms                                                             | 43.2 ms: 1.06x faster                                                             |
| xml_etree_parse         | 162 ms                                                              | 153 ms: 1.06x faster                                                              |
| deltablue               | 3.66 ms                                                             | 3.47 ms: 1.05x faster                                                             |
| async_tree_none         | 525 ms                                                              | 499 ms: 1.05x faster                                                              |
| nqueens                 | 84.0 ms                                                             | 80.0 ms: 1.05x faster                                                             |
| unpickle_pure_python    | 228 us                                                              | 218 us: 1.05x faster                                                              |
| pidigits                | 197 ms                                                              | 189 ms: 1.04x faster                                                              |
| async_tree_io           | 1.28 sec                                                            | 1.23 sec: 1.04x faster                                                            |
| xml_etree_iterparse     | 108 ms                                                              | 104 ms: 1.04x faster                                                              |
| async_tree_cpu_io_mixed | 736 ms                                                              | 720 ms: 1.02x faster                                                              |
| pathlib                 | 18.2 ms                                                             | 17.9 ms: 1.02x faster                                                             |
| genshi_xml              | 51.8 ms                                                             | 50.8 ms: 1.02x faster                                                             |
| go                      | 138 ms                                                              | 136 ms: 1.02x faster                                                              |
| sqlglot_parse           | 1.36 ms                                                             | 1.34 ms: 1.02x faster                                                             |
| mdp                     | 2.64 sec                                                            | 2.60 sec: 1.01x faster                                                            |
| async_tree_memoization  | 621 ms                                                              | 612 ms: 1.01x faster                                                              |
| fannkuch                | 384 ms                                                              | 381 ms: 1.01x faster                                                              |
| logging_silent          | 98.7 ns                                                             | 99.0 ns: 1.00x slower                                                             |
| create_gc_cycles        | 1.48 ms                                                             | 1.49 ms: 1.01x slower                                                             |
| sqlglot_transpile       | 1.65 ms                                                             | 1.67 ms: 1.01x slower                                                             |
| json                    | 4.86 ms                                                             | 4.93 ms: 1.02x slower                                                             |
| bench_thread_pool       | 820 us                                                              | 834 us: 1.02x slower                                                              |
| pycparser               | 1.14 sec                                                            | 1.16 sec: 1.02x slower                                                            |
| genshi_text             | 21.8 ms                                                             | 22.3 ms: 1.02x slower                                                             |
| regex_v8                | 22.0 ms                                                             | 22.4 ms: 1.02x slower                                                             |
| coverage                | 101 ms                                                              | 103 ms: 1.02x slower                                                              |
| chaos                   | 68.0 ms                                                             | 69.3 ms: 1.02x slower                                                             |
| unpack_sequence         | 49.5 ns                                                             | 50.6 ns: 1.02x slower                                                             |
| regex_effbot            | 3.32 ms                                                             | 3.40 ms: 1.02x slower                                                             |
| logging_simple          | 6.09 us                                                             | 6.25 us: 1.03x slower                                                             |
| pickle_pure_python      | 307 us                                                              | 316 us: 1.03x slower                                                              |
| scimark_lu              | 108 ms                                                              | 112 ms: 1.03x slower                                                              |
| raytrace                | 292 ms                                                              | 302 ms: 1.03x slower                                                              |
| pprint_pformat          | 1.45 sec                                                            | 1.51 sec: 1.04x slower                                                            |
| thrift                  | 766 us                                                              | 797 us: 1.04x slower                                                              |
| spectral_norm           | 99.5 ms                                                             | 104 ms: 1.04x slower                                                              |
| sqlglot_optimize        | 53.4 ms                                                             | 55.7 ms: 1.04x slower                                                             |
| sqlglot_normalize       | 108 ms                                                              | 113 ms: 1.04x slower                                                              |
| telco                   | 6.59 ms                                                             | 6.88 ms: 1.04x slower                                                             |
| pickle_dict             | 30.9 us                                                             | 32.4 us: 1.05x slower                                                             |
| logging_format          | 6.64 us                                                             | 6.98 us: 1.05x slower                                                             |
| deepcopy_memo           | 36.4 us                                                             | 38.3 us: 1.05x slower                                                             |
| pprint_safe_repr        | 701 ms                                                              | 738 ms: 1.05x slower                                                              |
| docutils                | 2.59 sec                                                            | 2.72 sec: 1.05x slower                                                            |
| 2to3                    | 257 ms                                                              | 271 ms: 1.05x slower                                                              |
| scimark_sor             | 115 ms                                                              | 121 ms: 1.05x slower                                                              |
| regex_compile           | 137 ms                                                              | 144 ms: 1.06x slower                                                              |
| tornado_http            | 96.7 ms                                                             | 102 ms: 1.06x slower                                                              |
| crypto_pyaes            | 73.8 ms                                                             | 77.9 ms: 1.06x slower                                                             |
| comprehensions          | 22.2 us                                                             | 23.5 us: 1.06x slower                                                             |
| sqlite_synth            | 2.51 us                                                             | 2.67 us: 1.06x slower                                                             |
| sqlalchemy_declarative  | 138 ms                                                              | 147 ms: 1.06x slower                                                              |
| regex_dna               | 196 ms                                                              | 209 ms: 1.07x slower                                                              |
| meteor_contest          | 106 ms                                                              | 113 ms: 1.07x slower                                                              |
| sqlalchemy_imperative   | 18.0 ms                                                             | 19.3 ms: 1.07x slower                                                             |
| float                   | 76.0 ms                                                             | 81.2 ms: 1.07x slower                                                             |
| scimark_monte_carlo     | 67.8 ms                                                             | 72.5 ms: 1.07x slower                                                             |
| dulwich_log             | 63.6 ms                                                             | 68.3 ms: 1.07x slower                                                             |
| python_startup          | 8.49 ms                                                             | 9.15 ms: 1.08x slower                                                             |
| deepcopy                | 339 us                                                              | 367 us: 1.08x slower                                                              |
| scimark_fft             | 328 ms                                                              | 355 ms: 1.08x slower                                                              |
| scimark_sparse_mat_mult | 4.47 ms                                                             | 4.86 ms: 1.09x slower                                                             |
| mako                    | 9.82 ms                                                             | 10.7 ms: 1.09x slower                                                             |
| pyflate                 | 414 ms                                                              | 449 ms: 1.09x slower                                                              |
| unpickle                | 13.2 us                                                             | 14.4 us: 1.09x slower                                                             |
| deepcopy_reduce         | 2.96 us                                                             | 3.24 us: 1.10x slower                                                             |
| pickle                  | 9.79 us                                                             | 10.8 us: 1.11x slower                                                             |
| xml_etree_process       | 54.1 ms                                                             | 60.4 ms: 1.12x slower                                                             |
| xml_etree_generate      | 76.5 ms                                                             | 85.8 ms: 1.12x slower                                                             |
| python_startup_no_site  | 5.98 ms                                                             | 6.71 ms: 1.12x slower                                                             |
| pickle_list             | 4.03 us                                                             | 4.60 us: 1.14x slower                                                             |
| gc_traversal            | 3.63 ms                                                             | 4.19 ms: 1.15x slower                                                             |
| async_generators        | 361 ms                                                              | 451 ms: 1.25x slower                                                              |
| dask                    | 368 ms                                                              | 540 ms: 1.47x slower                                                              |
| Geometric mean          | (ref)                                                               | 1.01x slower                                                                      |

Benchmark hidden because not significant (4): json_loads, unpickle_list, bench_mp_pool, html5lib
Ignored benchmarks (11) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: aiohttp, chameleon, django_template, djangocms, flaskblogging, gunicorn, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum
