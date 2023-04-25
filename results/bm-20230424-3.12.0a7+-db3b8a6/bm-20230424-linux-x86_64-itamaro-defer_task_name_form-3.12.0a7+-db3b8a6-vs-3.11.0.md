
# Results vs. 3.11.0

- fork: itamaro
- ref: defer_task_name_form
- machine: linux-x86_64
- commit hash: db3b8a6
- commit date: 2023-04-24
- overall geometric mean: 1.01x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230424-linux-x86_64-itamaro-defer_task_name_form-3.12.0a7+-db3b8a6 |
|----------------|:-------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 257 ms                                                              | 267 ms: 1.04x slower                                                    |
| chameleon      | 6.52 ms                                                             | 6.82 ms: 1.05x slower                                                   |
| docutils       | 2.59 sec                                                            | 2.69 sec: 1.04x slower                                                  |
| html5lib       | 64.0 ms                                                             | 65.1 ms: 1.02x slower                                                   |
| tornado_http   | 96.7 ms                                                             | 104 ms: 1.07x slower                                                    |
| Geometric mean | (ref)                                                               | 1.04x slower                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230424-linux-x86_64-itamaro-defer_task_name_form-3.12.0a7+-db3b8a6 |
|----------------|:-------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 96.7 ms                                                             | 89.0 ms: 1.09x faster                                                   |
| pidigits       | 197 ms                                                              | 189 ms: 1.04x faster                                                    |
| float          | 76.0 ms                                                             | 80.0 ms: 1.05x slower                                                   |
| Geometric mean | (ref)                                                               | 1.03x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230424-linux-x86_64-itamaro-defer_task_name_form-3.12.0a7+-db3b8a6 |
|----------------|:-------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 196 ms                                                              | 203 ms: 1.03x slower                                                    |
| regex_compile  | 137 ms                                                              | 142 ms: 1.04x slower                                                    |
| regex_effbot   | 3.32 ms                                                             | 3.66 ms: 1.10x slower                                                   |
| Geometric mean | (ref)                                                               | 1.04x slower                                                            |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230424-linux-x86_64-itamaro-defer_task_name_form-3.12.0a7+-db3b8a6 |
|----------------------|:-------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| json_dumps           | 12.5 ms                                                             | 9.68 ms: 1.30x faster                                                   |
| xml_etree_parse      | 162 ms                                                              | 152 ms: 1.06x faster                                                    |
| xml_etree_iterparse  | 108 ms                                                              | 102 ms: 1.06x faster                                                    |
| json_loads           | 26.2 us                                                             | 24.8 us: 1.05x faster                                                   |
| unpickle_pure_python | 228 us                                                              | 218 us: 1.05x faster                                                    |
| pickle_pure_python   | 307 us                                                              | 313 us: 1.02x slower                                                    |
| pickle_dict          | 30.9 us                                                             | 31.6 us: 1.02x slower                                                   |
| unpickle_list        | 4.96 us                                                             | 5.11 us: 1.03x slower                                                   |
| xml_etree_process    | 54.1 ms                                                             | 57.9 ms: 1.07x slower                                                   |
| xml_etree_generate   | 76.5 ms                                                             | 82.5 ms: 1.08x slower                                                   |
| unpickle             | 13.2 us                                                             | 14.4 us: 1.09x slower                                                   |
| pickle_list          | 4.03 us                                                             | 4.41 us: 1.10x slower                                                   |
| pickle               | 9.79 us                                                             | 10.7 us: 1.10x slower                                                   |
| Geometric mean       | (ref)                                                               | 1.00x slower                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230424-linux-x86_64-itamaro-defer_task_name_form-3.12.0a7+-db3b8a6 |
|------------------------|:-------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 8.49 ms                                                             | 8.99 ms: 1.06x slower                                                   |
| python_startup_no_site | 5.98 ms                                                             | 6.60 ms: 1.10x slower                                                   |
| Geometric mean         | (ref)                                                               | 1.08x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230424-linux-x86_64-itamaro-defer_task_name_form-3.12.0a7+-db3b8a6 |
|-----------------|:-------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                             | 50.5 ms: 1.03x faster                                                   |
| django_template | 32.9 ms                                                             | 34.3 ms: 1.04x slower                                                   |
| genshi_text     | 21.8 ms                                                             | 23.0 ms: 1.05x slower                                                   |
| mako            | 9.82 ms                                                             | 10.8 ms: 1.10x slower                                                   |
| Geometric mean  | (ref)                                                               | 1.04x slower                                                            |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230424-linux-x86_64-itamaro-defer_task_name_form-3.12.0a7+-db3b8a6 |
|-------------------------|:-------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| generators              | 73.4 ms                                                             | 32.2 ms: 2.28x faster                                                   |
| asyncio_tcp             | 888 ms                                                              | 512 ms: 1.73x faster                                                    |
| json_dumps              | 12.5 ms                                                             | 9.68 ms: 1.30x faster                                                   |
| coroutines              | 26.3 ms                                                             | 22.0 ms: 1.19x faster                                                   |
| mypy2                   | 422 ms                                                              | 359 ms: 1.17x faster                                                    |
| nbody                   | 96.7 ms                                                             | 89.0 ms: 1.09x faster                                                   |
| xml_etree_parse         | 162 ms                                                              | 152 ms: 1.06x faster                                                    |
| richards                | 45.7 ms                                                             | 43.2 ms: 1.06x faster                                                   |
| xml_etree_iterparse     | 108 ms                                                              | 102 ms: 1.06x faster                                                    |
| json_loads              | 26.2 us                                                             | 24.8 us: 1.05x faster                                                   |
| async_tree_none         | 525 ms                                                              | 500 ms: 1.05x faster                                                    |
| unpickle_pure_python    | 228 us                                                              | 218 us: 1.05x faster                                                    |
| pidigits                | 197 ms                                                              | 189 ms: 1.04x faster                                                    |
| sqlglot_parse           | 1.36 ms                                                             | 1.32 ms: 1.03x faster                                                   |
| async_tree_io           | 1.28 sec                                                            | 1.25 sec: 1.03x faster                                                  |
| genshi_xml              | 51.8 ms                                                             | 50.5 ms: 1.03x faster                                                   |
| nqueens                 | 84.0 ms                                                             | 82.0 ms: 1.02x faster                                                   |
| async_tree_cpu_io_mixed | 736 ms                                                              | 718 ms: 1.02x faster                                                    |
| json                    | 4.86 ms                                                             | 4.75 ms: 1.02x faster                                                   |
| hexiom                  | 6.48 ms                                                             | 6.36 ms: 1.02x faster                                                   |
| pathlib                 | 18.2 ms                                                             | 17.9 ms: 1.02x faster                                                   |
| mdp                     | 2.64 sec                                                            | 2.59 sec: 1.02x faster                                                  |
| go                      | 138 ms                                                              | 136 ms: 1.02x faster                                                    |
| coverage                | 101 ms                                                              | 99.8 ms: 1.01x faster                                                   |
| pycparser               | 1.14 sec                                                            | 1.13 sec: 1.01x faster                                                  |
| create_gc_cycles        | 1.48 ms                                                             | 1.47 ms: 1.01x faster                                                   |
| deltablue               | 3.66 ms                                                             | 3.64 ms: 1.01x faster                                                   |
| logging_silent          | 98.7 ns                                                             | 98.8 ns: 1.00x slower                                                   |
| telco                   | 6.59 ms                                                             | 6.64 ms: 1.01x slower                                                   |
| chaos                   | 68.0 ms                                                             | 68.5 ms: 1.01x slower                                                   |
| html5lib                | 64.0 ms                                                             | 65.1 ms: 1.02x slower                                                   |
| bench_thread_pool       | 820 us                                                              | 835 us: 1.02x slower                                                    |
| pickle_pure_python      | 307 us                                                              | 313 us: 1.02x slower                                                    |
| pprint_pformat          | 1.45 sec                                                            | 1.48 sec: 1.02x slower                                                  |
| scimark_lu              | 108 ms                                                              | 111 ms: 1.02x slower                                                    |
| sqlglot_normalize       | 108 ms                                                              | 111 ms: 1.02x slower                                                    |
| pickle_dict             | 30.9 us                                                             | 31.6 us: 1.02x slower                                                   |
| logging_simple          | 6.09 us                                                             | 6.23 us: 1.02x slower                                                   |
| sqlglot_optimize        | 53.4 ms                                                             | 54.7 ms: 1.03x slower                                                   |
| raytrace                | 292 ms                                                              | 301 ms: 1.03x slower                                                    |
| djangocms               | 32.3 us                                                             | 33.2 us: 1.03x slower                                                   |
| unpickle_list           | 4.96 us                                                             | 5.11 us: 1.03x slower                                                   |
| pprint_safe_repr        | 701 ms                                                              | 724 ms: 1.03x slower                                                    |
| regex_dna               | 196 ms                                                              | 203 ms: 1.03x slower                                                    |
| logging_format          | 6.64 us                                                             | 6.87 us: 1.03x slower                                                   |
| 2to3                    | 257 ms                                                              | 267 ms: 1.04x slower                                                    |
| docutils                | 2.59 sec                                                            | 2.69 sec: 1.04x slower                                                  |
| thrift                  | 766 us                                                              | 795 us: 1.04x slower                                                    |
| regex_compile           | 137 ms                                                              | 142 ms: 1.04x slower                                                    |
| sympy_integrate         | 21.0 ms                                                             | 21.9 ms: 1.04x slower                                                   |
| django_template         | 32.9 ms                                                             | 34.3 ms: 1.04x slower                                                   |
| crypto_pyaes            | 73.8 ms                                                             | 76.9 ms: 1.04x slower                                                   |
| chameleon               | 6.52 ms                                                             | 6.82 ms: 1.05x slower                                                   |
| spectral_norm           | 99.5 ms                                                             | 104 ms: 1.05x slower                                                    |
| scimark_monte_carlo     | 67.8 ms                                                             | 71.0 ms: 1.05x slower                                                   |
| sympy_expand            | 477 ms                                                              | 500 ms: 1.05x slower                                                    |
| genshi_text             | 21.8 ms                                                             | 23.0 ms: 1.05x slower                                                   |
| comprehensions          | 22.2 us                                                             | 23.4 us: 1.05x slower                                                   |
| float                   | 76.0 ms                                                             | 80.0 ms: 1.05x slower                                                   |
| scimark_sor             | 115 ms                                                              | 122 ms: 1.06x slower                                                    |
| python_startup          | 8.49 ms                                                             | 8.99 ms: 1.06x slower                                                   |
| sqlalchemy_declarative  | 138 ms                                                              | 147 ms: 1.06x slower                                                    |
| sqlite_synth            | 2.51 us                                                             | 2.67 us: 1.06x slower                                                   |
| sympy_str               | 291 ms                                                              | 310 ms: 1.06x slower                                                    |
| scimark_fft             | 328 ms                                                              | 348 ms: 1.06x slower                                                    |
| deepcopy                | 339 us                                                              | 360 us: 1.06x slower                                                    |
| dulwich_log             | 63.6 ms                                                             | 68.0 ms: 1.07x slower                                                   |
| scimark_sparse_mat_mult | 4.47 ms                                                             | 4.78 ms: 1.07x slower                                                   |
| xml_etree_process       | 54.1 ms                                                             | 57.9 ms: 1.07x slower                                                   |
| meteor_contest          | 106 ms                                                              | 114 ms: 1.07x slower                                                    |
| deepcopy_memo           | 36.4 us                                                             | 39.0 us: 1.07x slower                                                   |
| tornado_http            | 96.7 ms                                                             | 104 ms: 1.07x slower                                                    |
| sympy_sum               | 167 ms                                                              | 180 ms: 1.07x slower                                                    |
| deepcopy_reduce         | 2.96 us                                                             | 3.18 us: 1.08x slower                                                   |
| xml_etree_generate      | 76.5 ms                                                             | 82.5 ms: 1.08x slower                                                   |
| sqlalchemy_imperative   | 18.0 ms                                                             | 19.5 ms: 1.08x slower                                                   |
| unpickle                | 13.2 us                                                             | 14.4 us: 1.09x slower                                                   |
| pickle_list             | 4.03 us                                                             | 4.41 us: 1.10x slower                                                   |
| pickle                  | 9.79 us                                                             | 10.7 us: 1.10x slower                                                   |
| mako                    | 9.82 ms                                                             | 10.8 ms: 1.10x slower                                                   |
| regex_effbot            | 3.32 ms                                                             | 3.66 ms: 1.10x slower                                                   |
| python_startup_no_site  | 5.98 ms                                                             | 6.60 ms: 1.10x slower                                                   |
| pyflate                 | 414 ms                                                              | 459 ms: 1.11x slower                                                    |
| gc_traversal            | 3.63 ms                                                             | 4.08 ms: 1.12x slower                                                   |
| async_generators        | 361 ms                                                              | 440 ms: 1.22x slower                                                    |
| dask                    | 368 ms                                                              | 538 ms: 1.46x slower                                                    |
| Geometric mean          | (ref)                                                               | 1.01x slower                                                            |

Benchmark hidden because not significant (7): pylint, sqlglot_transpile, fannkuch, async_tree_memoization, bench_mp_pool, regex_v8, unpack_sequence
Ignored benchmarks (3) of /home/mdboom/Work/builds/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: aiohttp, flaskblogging, gunicorn
