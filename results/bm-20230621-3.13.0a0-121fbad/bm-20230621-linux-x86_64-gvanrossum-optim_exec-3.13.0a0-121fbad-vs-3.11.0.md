
# Results vs. 3.11.0

- fork: gvanrossum
- ref: optim_exec
- machine: linux-x86_64
- commit hash: 121fbad
- commit date: 2023-06-21
- overall geometric mean: 1.04x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230621-linux-x86_64-gvanrossum-optim_exec-3.13.0a0-121fbad |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| docutils       | 2.63 sec                                               | 2.66 sec: 1.01x slower                                          |
| Geometric mean | (ref)                                                  | 1.01x slower                                                    |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230621-linux-x86_64-gvanrossum-optim_exec-3.13.0a0-121fbad |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| nbody          | 93.1 ms                                                | 90.5 ms: 1.03x faster                                           |
| pidigits       | 198 ms                                                 | 197 ms: 1.01x faster                                            |
| float          | 77.2 ms                                                | 80.7 ms: 1.04x slower                                           |
| Geometric mean | (ref)                                                  | 1.00x slower                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230621-linux-x86_64-gvanrossum-optim_exec-3.13.0a0-121fbad |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.39 ms: 1.18x faster                                           |
| regex_v8       | 22.0 ms                                                | 21.7 ms: 1.02x faster                                           |
| regex_dna      | 204 ms                                                 | 201 ms: 1.01x faster                                            |
| regex_compile  | 138 ms                                                 | 138 ms: 1.00x faster                                            |
| Geometric mean | (ref)                                                  | 1.05x faster                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230621-linux-x86_64-gvanrossum-optim_exec-3.13.0a0-121fbad |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.81 ms: 1.28x faster                                           |
| json_loads           | 26.5 us                                                | 25.2 us: 1.05x faster                                           |
| unpickle_pure_python | 228 us                                                 | 218 us: 1.04x faster                                            |
| xml_etree_parse      | 158 ms                                                 | 154 ms: 1.03x faster                                            |
| pickle_pure_python   | 306 us                                                 | 304 us: 1.01x faster                                            |
| pickle_dict          | 31.1 us                                                | 31.3 us: 1.00x slower                                           |
| xml_etree_iterparse  | 104 ms                                                 | 105 ms: 1.02x slower                                            |
| tomli_loads          | 2.22 sec                                               | 2.34 sec: 1.05x slower                                          |
| xml_etree_process    | 53.9 ms                                                | 57.4 ms: 1.07x slower                                           |
| pickle               | 10.1 us                                                | 10.9 us: 1.08x slower                                           |
| unpickle             | 13.7 us                                                | 14.9 us: 1.09x slower                                           |
| xml_etree_generate   | 76.2 ms                                                | 84.6 ms: 1.11x slower                                           |
| pickle_list          | 4.11 us                                                | 4.63 us: 1.13x slower                                           |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                    |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230621-linux-x86_64-gvanrossum-optim_exec-3.13.0a0-121fbad |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.18 ms: 1.08x slower                                           |
| python_startup_no_site | 6.01 ms                                                | 6.66 ms: 1.11x slower                                           |
| Geometric mean         | (ref)                                                  | 1.09x slower                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230621-linux-x86_64-gvanrossum-optim_exec-3.13.0a0-121fbad |
|-----------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| mako      | 10.1 ms                                                | 10.9 ms: 1.08x slower                                           |

All benchmarks:
===============

| Benchmark                | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230621-linux-x86_64-gvanrossum-optim_exec-3.13.0a0-121fbad |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| typing_runtime_protocols | 486 us                                                 | 149 us: 3.27x faster                                            |
| generators               | 73.5 ms                                                | 29.3 ms: 2.51x faster                                           |
| asyncio_tcp              | 922 ms                                                 | 505 ms: 1.83x faster                                            |
| asyncio_tcp_ssl          | 3.14 sec                                               | 1.79 sec: 1.75x faster                                          |
| json_dumps               | 12.6 ms                                                | 9.81 ms: 1.28x faster                                           |
| mypy2                    | 420 ms                                                 | 335 ms: 1.25x faster                                            |
| regex_effbot             | 3.99 ms                                                | 3.39 ms: 1.18x faster                                           |
| coroutines               | 25.5 ms                                                | 22.1 ms: 1.15x faster                                           |
| richards_super           | 56.8 ms                                                | 50.4 ms: 1.13x faster                                           |
| gc_traversal             | 4.02 ms                                                | 3.58 ms: 1.12x faster                                           |
| deltablue                | 3.67 ms                                                | 3.31 ms: 1.11x faster                                           |
| chaos                    | 69.2 ms                                                | 62.7 ms: 1.10x faster                                           |
| async_tree_none          | 526 ms                                                 | 480 ms: 1.10x faster                                            |
| async_tree_io            | 1.30 sec                                               | 1.19 sec: 1.09x faster                                          |
| async_tree_memoization   | 627 ms                                                 | 583 ms: 1.08x faster                                            |
| coverage                 | 100 ms                                                 | 93.2 ms: 1.07x faster                                           |
| sqlglot_parse            | 1.40 ms                                                | 1.31 ms: 1.07x faster                                           |
| json_loads               | 26.5 us                                                | 25.2 us: 1.05x faster                                           |
| logging_silent           | 101 ns                                                 | 96.7 ns: 1.05x faster                                           |
| sqlglot_transpile        | 1.70 ms                                                | 1.63 ms: 1.05x faster                                           |
| unpickle_pure_python     | 228 us                                                 | 218 us: 1.04x faster                                            |
| richards                 | 45.7 ms                                                | 44.1 ms: 1.04x faster                                           |
| logging_format           | 6.68 us                                                | 6.44 us: 1.04x faster                                           |
| json                     | 4.94 ms                                                | 4.78 ms: 1.03x faster                                           |
| comprehensions           | 22.4 us                                                | 21.7 us: 1.03x faster                                           |
| xml_etree_parse          | 158 ms                                                 | 154 ms: 1.03x faster                                            |
| nbody                    | 93.1 ms                                                | 90.5 ms: 1.03x faster                                           |
| go                       | 140 ms                                                 | 137 ms: 1.02x faster                                            |
| async_tree_cpu_io_mixed  | 739 ms                                                 | 722 ms: 1.02x faster                                            |
| pycparser                | 1.18 sec                                               | 1.15 sec: 1.02x faster                                          |
| hexiom                   | 6.37 ms                                                | 6.23 ms: 1.02x faster                                           |
| raytrace                 | 297 ms                                                 | 291 ms: 1.02x faster                                            |
| logging_simple           | 6.03 us                                                | 5.91 us: 1.02x faster                                           |
| regex_v8                 | 22.0 ms                                                | 21.7 ms: 1.02x faster                                           |
| regex_dna                | 204 ms                                                 | 201 ms: 1.01x faster                                            |
| sqlglot_normalize        | 108 ms                                                 | 107 ms: 1.01x faster                                            |
| pidigits                 | 198 ms                                                 | 197 ms: 1.01x faster                                            |
| sqlglot_optimize         | 53.1 ms                                                | 52.8 ms: 1.01x faster                                           |
| pickle_pure_python       | 306 us                                                 | 304 us: 1.01x faster                                            |
| regex_compile            | 138 ms                                                 | 138 ms: 1.00x faster                                            |
| pickle_dict              | 31.1 us                                                | 31.3 us: 1.00x slower                                           |
| pprint_pformat           | 1.46 sec                                               | 1.47 sec: 1.01x slower                                          |
| scimark_lu               | 110 ms                                                 | 111 ms: 1.01x slower                                            |
| nqueens                  | 83.4 ms                                                | 84.1 ms: 1.01x slower                                           |
| create_gc_cycles         | 1.49 ms                                                | 1.50 ms: 1.01x slower                                           |
| docutils                 | 2.63 sec                                               | 2.66 sec: 1.01x slower                                          |
| bench_thread_pool        | 819 us                                                 | 831 us: 1.01x slower                                            |
| xml_etree_iterparse      | 104 ms                                                 | 105 ms: 1.02x slower                                            |
| unpack_sequence          | 43.1 ns                                                | 43.8 ns: 1.02x slower                                           |
| deepcopy                 | 342 us                                                 | 349 us: 1.02x slower                                            |
| meteor_contest           | 107 ms                                                 | 109 ms: 1.02x slower                                            |
| dulwich_log              | 63.7 ms                                                | 65.1 ms: 1.02x slower                                           |
| pprint_safe_repr         | 701 ms                                                 | 719 ms: 1.02x slower                                            |
| pathlib                  | 18.2 ms                                                | 18.8 ms: 1.03x slower                                           |
| telco                    | 6.58 ms                                                | 6.81 ms: 1.03x slower                                           |
| deepcopy_memo            | 37.0 us                                                | 38.3 us: 1.04x slower                                           |
| mdp                      | 2.62 sec                                               | 2.72 sec: 1.04x slower                                          |
| float                    | 77.2 ms                                                | 80.7 ms: 1.04x slower                                           |
| scimark_monte_carlo      | 68.1 ms                                                | 71.2 ms: 1.05x slower                                           |
| crypto_pyaes             | 74.7 ms                                                | 78.4 ms: 1.05x slower                                           |
| tomli_loads              | 2.22 sec                                               | 2.34 sec: 1.05x slower                                          |
| deepcopy_reduce          | 2.94 us                                                | 3.10 us: 1.06x slower                                           |
| xml_etree_process        | 53.9 ms                                                | 57.4 ms: 1.07x slower                                           |
| pyflate                  | 418 ms                                                 | 449 ms: 1.07x slower                                            |
| python_startup           | 8.52 ms                                                | 9.18 ms: 1.08x slower                                           |
| mako                     | 10.1 ms                                                | 10.9 ms: 1.08x slower                                           |
| pickle                   | 10.1 us                                                | 10.9 us: 1.08x slower                                           |
| unpickle                 | 13.7 us                                                | 14.9 us: 1.09x slower                                           |
| fannkuch                 | 388 ms                                                 | 427 ms: 1.10x slower                                            |
| sqlite_synth             | 2.52 us                                                | 2.78 us: 1.10x slower                                           |
| scimark_fft              | 328 ms                                                 | 363 ms: 1.11x slower                                            |
| spectral_norm            | 100 ms                                                 | 111 ms: 1.11x slower                                            |
| python_startup_no_site   | 6.01 ms                                                | 6.66 ms: 1.11x slower                                           |
| xml_etree_generate       | 76.2 ms                                                | 84.6 ms: 1.11x slower                                           |
| scimark_sparse_mat_mult  | 4.50 ms                                                | 5.06 ms: 1.12x slower                                           |
| pickle_list              | 4.11 us                                                | 4.63 us: 1.13x slower                                           |
| async_generators         | 368 ms                                                 | 463 ms: 1.26x slower                                            |
| dask                     | 360 ms                                                 | 515 ms: 1.43x slower                                            |
| Geometric mean           | (ref)                                                  | 1.04x faster                                                    |

Benchmark hidden because not significant (4): tornado_http, bench_mp_pool, unpickle_list, scimark_sor
Ignored benchmarks (18) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
