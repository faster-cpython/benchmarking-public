
# Results vs. 3.11.0

- fork: carljm
- ref: inlinecomp2
- machine: linux-x86_64
- commit hash: 36b2917
- commit date: 2023-02-10
- overall geometric mean: 1.03x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230210-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-36b2917 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| 2to3           | 257 ms                                                 | 251 ms: 1.03x faster                                          |
| chameleon      | 6.41 ms                                                | 6.47 ms: 1.01x slower                                         |
| docutils       | 2.60 sec                                               | 2.53 sec: 1.03x faster                                        |
| html5lib       | 63.2 ms                                                | 60.6 ms: 1.04x faster                                         |
| tornado_http   | 96.6 ms                                                | 94.1 ms: 1.03x faster                                         |
| Geometric mean | (ref)                                                  | 1.02x faster                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230210-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-36b2917 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| float          | 76.3 ms                                                | 72.8 ms: 1.05x faster                                         |
| pidigits       | 199 ms                                                 | 193 ms: 1.04x faster                                          |
| nbody          | 95.0 ms                                                | 94.0 ms: 1.01x faster                                         |
| Geometric mean | (ref)                                                  | 1.03x faster                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230210-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-36b2917 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 128 ms: 1.07x faster                                          |
| regex_v8       | 22.3 ms                                                | 21.6 ms: 1.03x faster                                         |
| regex_dna      | 203 ms                                                 | 205 ms: 1.01x slower                                          |
| regex_effbot   | 3.36 ms                                                | 3.66 ms: 1.09x slower                                         |
| Geometric mean | (ref)                                                  | 1.00x faster                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230210-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-36b2917 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| json_dumps           | 12.7 ms                                                | 9.39 ms: 1.35x faster                                         |
| unpickle_pure_python | 225 us                                                 | 198 us: 1.14x faster                                          |
| json_loads           | 26.2 us                                                | 23.7 us: 1.11x faster                                         |
| xml_etree_parse      | 158 ms                                                 | 148 ms: 1.07x faster                                          |
| pickle_pure_python   | 304 us                                                 | 291 us: 1.04x faster                                          |
| pickle_dict          | 31.4 us                                                | 30.9 us: 1.02x faster                                         |
| pickle_list          | 4.17 us                                                | 4.15 us: 1.01x faster                                         |
| xml_etree_process    | 53.8 ms                                                | 54.8 ms: 1.02x slower                                         |
| pickle               | 9.79 us                                                | 10.1 us: 1.03x slower                                         |
| unpickle_list        | 4.95 us                                                | 5.13 us: 1.04x slower                                         |
| xml_etree_generate   | 76.2 ms                                                | 80.2 ms: 1.05x slower                                         |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                  |

Benchmark hidden because not significant (2): xml_etree_iterparse, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230210-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-36b2917 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup         | 8.36 ms                                                | 8.90 ms: 1.07x slower                                         |
| python_startup_no_site | 5.96 ms                                                | 6.46 ms: 1.08x slower                                         |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230210-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-36b2917 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| genshi_xml     | 52.1 ms                                                | 47.8 ms: 1.09x faster                                         |
| genshi_text    | 22.1 ms                                                | 20.9 ms: 1.06x faster                                         |
| mako           | 9.85 ms                                                | 9.90 ms: 1.00x slower                                         |
| Geometric mean | (ref)                                                  | 1.03x faster                                                  |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230210-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-36b2917 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| json_dumps              | 12.7 ms                                                | 9.39 ms: 1.35x faster                                         |
| deltablue               | 3.64 ms                                                | 3.13 ms: 1.16x faster                                         |
| unpickle_pure_python    | 225 us                                                 | 198 us: 1.14x faster                                          |
| nqueens                 | 85.0 ms                                                | 74.9 ms: 1.13x faster                                         |
| scimark_sparse_mat_mult | 4.40 ms                                                | 3.94 ms: 1.12x faster                                         |
| json_loads              | 26.2 us                                                | 23.7 us: 1.11x faster                                         |
| richards                | 46.2 ms                                                | 42.1 ms: 1.10x faster                                         |
| genshi_xml              | 52.1 ms                                                | 47.8 ms: 1.09x faster                                         |
| json                    | 4.95 ms                                                | 4.55 ms: 1.09x faster                                         |
| chaos                   | 68.6 ms                                                | 63.2 ms: 1.09x faster                                         |
| sympy_str               | 287 ms                                                 | 265 ms: 1.09x faster                                          |
| scimark_sor             | 115 ms                                                 | 106 ms: 1.08x faster                                          |
| hexiom                  | 6.35 ms                                                | 5.87 ms: 1.08x faster                                         |
| pycparser               | 1.17 sec                                               | 1.09 sec: 1.08x faster                                        |
| sympy_expand            | 472 ms                                                 | 439 ms: 1.08x faster                                          |
| sympy_integrate         | 20.9 ms                                                | 19.5 ms: 1.07x faster                                         |
| xml_etree_parse         | 158 ms                                                 | 148 ms: 1.07x faster                                          |
| scimark_fft             | 329 ms                                                 | 307 ms: 1.07x faster                                          |
| sympy_sum               | 166 ms                                                 | 155 ms: 1.07x faster                                          |
| deepcopy_memo           | 36.4 us                                                | 34.1 us: 1.07x faster                                         |
| regex_compile           | 136 ms                                                 | 128 ms: 1.07x faster                                          |
| sqlglot_normalize       | 108 ms                                                 | 101 ms: 1.06x faster                                          |
| spectral_norm           | 99.9 ms                                                | 93.9 ms: 1.06x faster                                         |
| async_tree_none         | 529 ms                                                 | 498 ms: 1.06x faster                                          |
| deepcopy                | 344 us                                                 | 324 us: 1.06x faster                                          |
| fannkuch                | 388 ms                                                 | 366 ms: 1.06x faster                                          |
| genshi_text             | 22.1 ms                                                | 20.9 ms: 1.06x faster                                         |
| pprint_pformat          | 1.44 sec                                               | 1.37 sec: 1.05x faster                                        |
| sqlglot_optimize        | 53.0 ms                                                | 50.4 ms: 1.05x faster                                         |
| float                   | 76.3 ms                                                | 72.8 ms: 1.05x faster                                         |
| logging_silent          | 98.5 ns                                                | 94.1 ns: 1.05x faster                                         |
| gunicorn                | 1.12 ms                                                | 1.07 ms: 1.05x faster                                         |
| go                      | 143 ms                                                 | 137 ms: 1.05x faster                                          |
| pickle_pure_python      | 304 us                                                 | 291 us: 1.04x faster                                          |
| html5lib                | 63.2 ms                                                | 60.6 ms: 1.04x faster                                         |
| scimark_monte_carlo     | 68.3 ms                                                | 65.5 ms: 1.04x faster                                         |
| raytrace                | 290 ms                                                 | 279 ms: 1.04x faster                                          |
| logging_simple          | 6.06 us                                                | 5.83 us: 1.04x faster                                         |
| aiohttp                 | 1.05 ms                                                | 1.01 ms: 1.04x faster                                         |
| pathlib                 | 18.2 ms                                                | 17.5 ms: 1.04x faster                                         |
| logging_format          | 6.62 us                                                | 6.39 us: 1.04x faster                                         |
| pyflate                 | 417 ms                                                 | 403 ms: 1.04x faster                                          |
| sqlalchemy_imperative   | 18.0 ms                                                | 17.4 ms: 1.04x faster                                         |
| pidigits                | 199 ms                                                 | 193 ms: 1.04x faster                                          |
| telco                   | 6.62 ms                                                | 6.40 ms: 1.03x faster                                         |
| regex_v8                | 22.3 ms                                                | 21.6 ms: 1.03x faster                                         |
| sqlalchemy_declarative  | 139 ms                                                 | 134 ms: 1.03x faster                                          |
| pprint_safe_repr        | 691 ms                                                 | 668 ms: 1.03x faster                                          |
| bench_thread_pool       | 810 us                                                 | 785 us: 1.03x faster                                          |
| docutils                | 2.60 sec                                               | 2.53 sec: 1.03x faster                                        |
| tornado_http            | 96.6 ms                                                | 94.1 ms: 1.03x faster                                         |
| async_tree_io           | 1.31 sec                                               | 1.27 sec: 1.03x faster                                        |
| 2to3                    | 257 ms                                                 | 251 ms: 1.03x faster                                          |
| deepcopy_reduce         | 2.97 us                                                | 2.90 us: 1.02x faster                                         |
| async_tree_memoization  | 625 ms                                                 | 612 ms: 1.02x faster                                          |
| dulwich_log             | 63.9 ms                                                | 62.6 ms: 1.02x faster                                         |
| pickle_dict             | 31.4 us                                                | 30.9 us: 1.02x faster                                         |
| coroutines              | 26.1 ms                                                | 25.8 ms: 1.01x faster                                         |
| coverage                | 101 ms                                                 | 99.3 ms: 1.01x faster                                         |
| nbody                   | 95.0 ms                                                | 94.0 ms: 1.01x faster                                         |
| meteor_contest          | 105 ms                                                 | 104 ms: 1.01x faster                                          |
| crypto_pyaes            | 73.9 ms                                                | 73.3 ms: 1.01x faster                                         |
| pickle_list             | 4.17 us                                                | 4.15 us: 1.01x faster                                         |
| mako                    | 9.85 ms                                                | 9.90 ms: 1.00x slower                                         |
| chameleon               | 6.41 ms                                                | 6.47 ms: 1.01x slower                                         |
| regex_dna               | 203 ms                                                 | 205 ms: 1.01x slower                                          |
| thrift                  | 752 us                                                 | 760 us: 1.01x slower                                          |
| mdp                     | 2.62 sec                                               | 2.66 sec: 1.01x slower                                        |
| xml_etree_process       | 53.8 ms                                                | 54.8 ms: 1.02x slower                                         |
| unpack_sequence         | 43.4 ns                                                | 44.4 ns: 1.02x slower                                         |
| sqlglot_transpile       | 1.66 ms                                                | 1.71 ms: 1.03x slower                                         |
| sqlglot_parse           | 1.37 ms                                                | 1.41 ms: 1.03x slower                                         |
| pickle                  | 9.79 us                                                | 10.1 us: 1.03x slower                                         |
| unpickle_list           | 4.95 us                                                | 5.13 us: 1.04x slower                                         |
| sqlite_synth            | 2.49 us                                                | 2.58 us: 1.04x slower                                         |
| xml_etree_generate      | 76.2 ms                                                | 80.2 ms: 1.05x slower                                         |
| python_startup          | 8.36 ms                                                | 8.90 ms: 1.07x slower                                         |
| generators              | 72.2 ms                                                | 77.7 ms: 1.08x slower                                         |
| python_startup_no_site  | 5.96 ms                                                | 6.46 ms: 1.08x slower                                         |
| regex_effbot            | 3.36 ms                                                | 3.66 ms: 1.09x slower                                         |
| async_generators        | 359 ms                                                 | 427 ms: 1.19x slower                                          |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                  |

Benchmark hidden because not significant (6): async_tree_cpu_io_mixed, bench_mp_pool, xml_etree_iterparse, django_template, scimark_lu, unpickle
Ignored benchmarks (3) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, mypy, pylint
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20230210-3.12.0a5+-36b2917/bm-20230210-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-36b2917.json: asyncio_tcp, create_gc_cycles, djangocms, gc_traversal, mypy2
