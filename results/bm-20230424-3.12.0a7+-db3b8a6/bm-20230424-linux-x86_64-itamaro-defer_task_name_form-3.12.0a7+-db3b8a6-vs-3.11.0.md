
# Results vs. 3.11.0

- fork: itamaro
- ref: defer_task_name_form
- machine: linux-x86_64
- commit hash: db3b8a6
- commit date: 2023-04-24
- overall geometric mean: 1.00x slower \*
- HPT reliability: 96.52%
- HPT 99th percentile: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230424-linux-x86_64-itamaro-defer_task_name_form-3.12.0a7+-db3b8a6 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 267 ms: 1.03x slower                                                    |
| chameleon      | 6.47 ms                                                | 6.82 ms: 1.05x slower                                                   |
| docutils       | 2.63 sec                                               | 2.69 sec: 1.02x slower                                                  |
| tornado_http   | 96.3 ms                                                | 104 ms: 1.08x slower                                                    |
| Geometric mean | (ref)                                                  | 1.04x slower                                                            |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230424-linux-x86_64-itamaro-defer_task_name_form-3.12.0a7+-db3b8a6 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pidigits       | 198 ms                                                 | 189 ms: 1.05x faster                                                    |
| nbody          | 93.1 ms                                                | 89.0 ms: 1.05x faster                                                   |
| float          | 77.2 ms                                                | 80.0 ms: 1.04x slower                                                   |
| Geometric mean | (ref)                                                  | 1.02x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230424-linux-x86_64-itamaro-defer_task_name_form-3.12.0a7+-db3b8a6 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.66 ms: 1.09x faster                                                   |
| regex_dna      | 204 ms                                                 | 203 ms: 1.00x faster                                                    |
| regex_compile  | 138 ms                                                 | 142 ms: 1.03x slower                                                    |
| Geometric mean | (ref)                                                  | 1.02x faster                                                            |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230424-linux-x86_64-itamaro-defer_task_name_form-3.12.0a7+-db3b8a6 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.68 ms: 1.30x faster                                                   |
| json_loads           | 26.5 us                                                | 24.8 us: 1.07x faster                                                   |
| unpickle_pure_python | 228 us                                                 | 218 us: 1.04x faster                                                    |
| xml_etree_parse      | 158 ms                                                 | 152 ms: 1.04x faster                                                    |
| xml_etree_iterparse  | 104 ms                                                 | 102 ms: 1.02x faster                                                    |
| pickle_dict          | 31.1 us                                                | 31.6 us: 1.02x slower                                                   |
| pickle_pure_python   | 306 us                                                 | 313 us: 1.02x slower                                                    |
| unpickle_list        | 4.91 us                                                | 5.11 us: 1.04x slower                                                   |
| unpickle             | 13.7 us                                                | 14.4 us: 1.05x slower                                                   |
| pickle               | 10.1 us                                                | 10.7 us: 1.06x slower                                                   |
| pickle_list          | 4.11 us                                                | 4.41 us: 1.07x slower                                                   |
| xml_etree_process    | 53.9 ms                                                | 57.9 ms: 1.07x slower                                                   |
| xml_etree_generate   | 76.2 ms                                                | 82.5 ms: 1.08x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.00x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230424-linux-x86_64-itamaro-defer_task_name_form-3.12.0a7+-db3b8a6 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.99 ms: 1.06x slower                                                   |
| python_startup_no_site | 6.01 ms                                                | 6.60 ms: 1.10x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.08x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230424-linux-x86_64-itamaro-defer_task_name_form-3.12.0a7+-db3b8a6 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 50.5 ms: 1.02x faster                                                   |
| django_template | 32.6 ms                                                | 34.3 ms: 1.05x slower                                                   |
| genshi_text     | 21.6 ms                                                | 23.0 ms: 1.06x slower                                                   |
| mako            | 10.1 ms                                                | 10.8 ms: 1.07x slower                                                   |
| Geometric mean  | (ref)                                                  | 1.04x slower                                                            |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230424-linux-x86_64-itamaro-defer_task_name_form-3.12.0a7+-db3b8a6 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 32.2 ms: 2.28x faster                                                   |
| asyncio_tcp             | 922 ms                                                 | 512 ms: 1.80x faster                                                    |
| json_dumps              | 12.6 ms                                                | 9.68 ms: 1.30x faster                                                   |
| mypy2                   | 420 ms                                                 | 359 ms: 1.17x faster                                                    |
| coroutines              | 25.5 ms                                                | 22.0 ms: 1.16x faster                                                   |
| regex_effbot            | 3.99 ms                                                | 3.66 ms: 1.09x faster                                                   |
| json_loads              | 26.5 us                                                | 24.8 us: 1.07x faster                                                   |
| richards                | 45.7 ms                                                | 43.2 ms: 1.06x faster                                                   |
| sqlglot_parse           | 1.40 ms                                                | 1.32 ms: 1.06x faster                                                   |
| async_tree_none         | 526 ms                                                 | 500 ms: 1.05x faster                                                    |
| pidigits                | 198 ms                                                 | 189 ms: 1.05x faster                                                    |
| nbody                   | 93.1 ms                                                | 89.0 ms: 1.05x faster                                                   |
| unpickle_pure_python    | 228 us                                                 | 218 us: 1.04x faster                                                    |
| pycparser               | 1.18 sec                                               | 1.13 sec: 1.04x faster                                                  |
| json                    | 4.94 ms                                                | 4.75 ms: 1.04x faster                                                   |
| xml_etree_parse         | 158 ms                                                 | 152 ms: 1.04x faster                                                    |
| async_tree_io           | 1.30 sec                                               | 1.25 sec: 1.04x faster                                                  |
| sqlglot_transpile       | 1.70 ms                                                | 1.65 ms: 1.03x faster                                                   |
| async_tree_cpu_io_mixed | 739 ms                                                 | 718 ms: 1.03x faster                                                    |
| go                      | 140 ms                                                 | 136 ms: 1.03x faster                                                    |
| genshi_xml              | 51.8 ms                                                | 50.5 ms: 1.02x faster                                                   |
| logging_silent          | 101 ns                                                 | 98.8 ns: 1.02x faster                                                   |
| xml_etree_iterparse     | 104 ms                                                 | 102 ms: 1.02x faster                                                    |
| pathlib                 | 18.2 ms                                                | 17.9 ms: 1.02x faster                                                   |
| nqueens                 | 83.4 ms                                                | 82.0 ms: 1.02x faster                                                   |
| fannkuch                | 388 ms                                                 | 383 ms: 1.01x faster                                                    |
| async_tree_memoization  | 627 ms                                                 | 621 ms: 1.01x faster                                                    |
| create_gc_cycles        | 1.49 ms                                                | 1.47 ms: 1.01x faster                                                   |
| chaos                   | 69.2 ms                                                | 68.5 ms: 1.01x faster                                                   |
| mdp                     | 2.62 sec                                               | 2.59 sec: 1.01x faster                                                  |
| deltablue               | 3.67 ms                                                | 3.64 ms: 1.01x faster                                                   |
| regex_dna               | 204 ms                                                 | 203 ms: 1.00x faster                                                    |
| hexiom                  | 6.37 ms                                                | 6.36 ms: 1.00x faster                                                   |
| telco                   | 6.58 ms                                                | 6.64 ms: 1.01x slower                                                   |
| scimark_lu              | 110 ms                                                 | 111 ms: 1.01x slower                                                    |
| raytrace                | 297 ms                                                 | 301 ms: 1.01x slower                                                    |
| gc_traversal            | 4.02 ms                                                | 4.08 ms: 1.01x slower                                                   |
| pickle_dict             | 31.1 us                                                | 31.6 us: 1.02x slower                                                   |
| pprint_pformat          | 1.46 sec                                               | 1.48 sec: 1.02x slower                                                  |
| bench_thread_pool       | 819 us                                                 | 835 us: 1.02x slower                                                    |
| docutils                | 2.63 sec                                               | 2.69 sec: 1.02x slower                                                  |
| pickle_pure_python      | 306 us                                                 | 313 us: 1.02x slower                                                    |
| logging_format          | 6.68 us                                                | 6.87 us: 1.03x slower                                                   |
| sqlglot_normalize       | 108 ms                                                 | 111 ms: 1.03x slower                                                    |
| scimark_sor             | 118 ms                                                 | 122 ms: 1.03x slower                                                    |
| 2to3                    | 259 ms                                                 | 267 ms: 1.03x slower                                                    |
| regex_compile           | 138 ms                                                 | 142 ms: 1.03x slower                                                    |
| crypto_pyaes            | 74.7 ms                                                | 76.9 ms: 1.03x slower                                                   |
| sqlglot_optimize        | 53.1 ms                                                | 54.7 ms: 1.03x slower                                                   |
| pprint_safe_repr        | 701 ms                                                 | 724 ms: 1.03x slower                                                    |
| logging_simple          | 6.03 us                                                | 6.23 us: 1.03x slower                                                   |
| float                   | 77.2 ms                                                | 80.0 ms: 1.04x slower                                                   |
| spectral_norm           | 100 ms                                                 | 104 ms: 1.04x slower                                                    |
| unpickle_list           | 4.91 us                                                | 5.11 us: 1.04x slower                                                   |
| comprehensions          | 22.4 us                                                | 23.4 us: 1.04x slower                                                   |
| scimark_monte_carlo     | 68.1 ms                                                | 71.0 ms: 1.04x slower                                                   |
| sympy_integrate         | 21.0 ms                                                | 21.9 ms: 1.05x slower                                                   |
| thrift                  | 756 us                                                 | 795 us: 1.05x slower                                                    |
| django_template         | 32.6 ms                                                | 34.3 ms: 1.05x slower                                                   |
| chameleon               | 6.47 ms                                                | 6.82 ms: 1.05x slower                                                   |
| sympy_expand            | 475 ms                                                 | 500 ms: 1.05x slower                                                    |
| deepcopy                | 342 us                                                 | 360 us: 1.05x slower                                                    |
| deepcopy_memo           | 37.0 us                                                | 39.0 us: 1.05x slower                                                   |
| unpickle                | 13.7 us                                                | 14.4 us: 1.05x slower                                                   |
| python_startup          | 8.52 ms                                                | 8.99 ms: 1.06x slower                                                   |
| sqlite_synth            | 2.52 us                                                | 2.67 us: 1.06x slower                                                   |
| scimark_fft             | 328 ms                                                 | 348 ms: 1.06x slower                                                    |
| sqlalchemy_declarative  | 138 ms                                                 | 147 ms: 1.06x slower                                                    |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.78 ms: 1.06x slower                                                   |
| pickle                  | 10.1 us                                                | 10.7 us: 1.06x slower                                                   |
| genshi_text             | 21.6 ms                                                | 23.0 ms: 1.06x slower                                                   |
| meteor_contest          | 107 ms                                                 | 114 ms: 1.07x slower                                                    |
| sympy_str               | 290 ms                                                 | 310 ms: 1.07x slower                                                    |
| dulwich_log             | 63.7 ms                                                | 68.0 ms: 1.07x slower                                                   |
| mako                    | 10.1 ms                                                | 10.8 ms: 1.07x slower                                                   |
| pickle_list             | 4.11 us                                                | 4.41 us: 1.07x slower                                                   |
| xml_etree_process       | 53.9 ms                                                | 57.9 ms: 1.07x slower                                                   |
| tornado_http            | 96.3 ms                                                | 104 ms: 1.08x slower                                                    |
| sympy_sum               | 167 ms                                                 | 180 ms: 1.08x slower                                                    |
| deepcopy_reduce         | 2.94 us                                                | 3.18 us: 1.08x slower                                                   |
| xml_etree_generate      | 76.2 ms                                                | 82.5 ms: 1.08x slower                                                   |
| sqlalchemy_imperative   | 17.9 ms                                                | 19.5 ms: 1.09x slower                                                   |
| python_startup_no_site  | 6.01 ms                                                | 6.60 ms: 1.10x slower                                                   |
| pyflate                 | 418 ms                                                 | 459 ms: 1.10x slower                                                    |
| unpack_sequence         | 43.1 ns                                                | 49.5 ns: 1.15x slower                                                   |
| async_generators        | 368 ms                                                 | 440 ms: 1.19x slower                                                    |
| dask                    | 360 ms                                                 | 538 ms: 1.49x slower                                                    |
| Geometric mean          | (ref)                                                  | 1.00x slower                                                            |

Benchmark hidden because not significant (6): regex_v8, coverage, bench_mp_pool, pylint, html5lib, djangocms
Ignored benchmarks (7) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 96.52% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x
