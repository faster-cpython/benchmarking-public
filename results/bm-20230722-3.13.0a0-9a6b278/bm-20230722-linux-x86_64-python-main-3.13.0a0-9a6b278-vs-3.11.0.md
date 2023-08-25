
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 9a6b278
- commit date: 2023-07-22
- overall geometric mean: 1.04x faster
- HPT reliability: 83.82%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230722-linux-x86_64-python-main-3.13.0a0-9a6b278 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| docutils       | 2.63 sec                                               | 2.66 sec: 1.01x slower                                |
| tornado_http   | 96.3 ms                                                | 95.2 ms: 1.01x faster                                 |
| Geometric mean | (ref)                                                  | 1.00x slower                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230722-linux-x86_64-python-main-3.13.0a0-9a6b278 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| nbody          | 93.1 ms                                                | 89.2 ms: 1.04x faster                                 |
| pidigits       | 198 ms                                                 | 192 ms: 1.03x faster                                  |
| float          | 77.2 ms                                                | 79.7 ms: 1.03x slower                                 |
| Geometric mean | (ref)                                                  | 1.01x faster                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230722-linux-x86_64-python-main-3.13.0a0-9a6b278 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.61 ms: 1.11x faster                                 |
| regex_compile  | 138 ms                                                 | 137 ms: 1.01x faster                                  |
| regex_v8       | 22.0 ms                                                | 22.2 ms: 1.01x slower                                 |
| regex_dna      | 204 ms                                                 | 216 ms: 1.06x slower                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230722-linux-x86_64-python-main-3.13.0a0-9a6b278 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.88 ms: 1.27x faster                                 |
| unpickle_pure_python | 228 us                                                 | 212 us: 1.08x faster                                  |
| xml_etree_parse      | 158 ms                                                 | 153 ms: 1.04x faster                                  |
| pickle_pure_python   | 306 us                                                 | 298 us: 1.03x faster                                  |
| json_loads           | 26.5 us                                                | 26.0 us: 1.02x faster                                 |
| xml_etree_iterparse  | 104 ms                                                 | 103 ms: 1.01x faster                                  |
| unpickle_list        | 4.91 us                                                | 4.94 us: 1.01x slower                                 |
| pickle_dict          | 31.1 us                                                | 31.9 us: 1.03x slower                                 |
| tomli_loads          | 2.22 sec                                               | 2.32 sec: 1.04x slower                                |
| unpickle             | 13.7 us                                                | 14.6 us: 1.07x slower                                 |
| pickle               | 10.1 us                                                | 10.9 us: 1.08x slower                                 |
| xml_etree_process    | 53.9 ms                                                | 58.3 ms: 1.08x slower                                 |
| xml_etree_generate   | 76.2 ms                                                | 84.0 ms: 1.10x slower                                 |
| pickle_list          | 4.11 us                                                | 4.54 us: 1.10x slower                                 |
| Geometric mean       | (ref)                                                  | 1.01x slower                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230722-linux-x86_64-python-main-3.13.0a0-9a6b278 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.19 ms: 1.08x slower                                 |
| python_startup_no_site | 6.01 ms                                                | 6.68 ms: 1.11x slower                                 |
| Geometric mean         | (ref)                                                  | 1.09x slower                                          |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230722-linux-x86_64-python-main-3.13.0a0-9a6b278 |
|-----------|:------------------------------------------------------:|:-----------------------------------------------------:|
| mako      | 10.1 ms                                                | 10.6 ms: 1.05x slower                                 |

All benchmarks:
===============

| Benchmark                | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230722-linux-x86_64-python-main-3.13.0a0-9a6b278 |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| typing_runtime_protocols | 486 us                                                 | 142 us: 3.43x faster                                  |
| generators               | 73.5 ms                                                | 28.0 ms: 2.62x faster                                 |
| asyncio_tcp              | 922 ms                                                 | 480 ms: 1.92x faster                                  |
| asyncio_tcp_ssl          | 3.14 sec                                               | 1.79 sec: 1.76x faster                                |
| json_dumps               | 12.6 ms                                                | 9.88 ms: 1.27x faster                                 |
| mypy2                    | 420 ms                                                 | 336 ms: 1.25x faster                                  |
| coroutines               | 25.5 ms                                                | 21.5 ms: 1.19x faster                                 |
| chaos                    | 69.2 ms                                                | 60.0 ms: 1.15x faster                                 |
| deltablue                | 3.67 ms                                                | 3.23 ms: 1.14x faster                                 |
| comprehensions           | 22.4 us                                                | 20.1 us: 1.12x faster                                 |
| regex_effbot             | 3.99 ms                                                | 3.61 ms: 1.11x faster                                 |
| raytrace                 | 297 ms                                                 | 270 ms: 1.10x faster                                  |
| async_tree_none          | 526 ms                                                 | 480 ms: 1.10x faster                                  |
| async_tree_io            | 1.30 sec                                               | 1.19 sec: 1.09x faster                                |
| sqlglot_parse            | 1.40 ms                                                | 1.29 ms: 1.09x faster                                 |
| unpickle_pure_python     | 228 us                                                 | 212 us: 1.08x faster                                  |
| coverage                 | 100 ms                                                 | 93.0 ms: 1.08x faster                                 |
| richards_super           | 56.8 ms                                                | 53.1 ms: 1.07x faster                                 |
| async_tree_memoization   | 627 ms                                                 | 587 ms: 1.07x faster                                  |
| sqlglot_transpile        | 1.70 ms                                                | 1.60 ms: 1.06x faster                                 |
| crypto_pyaes             | 74.7 ms                                                | 70.5 ms: 1.06x faster                                 |
| hexiom                   | 6.37 ms                                                | 6.05 ms: 1.05x faster                                 |
| nbody                    | 93.1 ms                                                | 89.2 ms: 1.04x faster                                 |
| nqueens                  | 83.4 ms                                                | 79.9 ms: 1.04x faster                                 |
| xml_etree_parse          | 158 ms                                                 | 153 ms: 1.04x faster                                  |
| pidigits                 | 198 ms                                                 | 192 ms: 1.03x faster                                  |
| logging_format           | 6.68 us                                                | 6.50 us: 1.03x faster                                 |
| pickle_pure_python       | 306 us                                                 | 298 us: 1.03x faster                                  |
| go                       | 140 ms                                                 | 136 ms: 1.03x faster                                  |
| sqlglot_normalize        | 108 ms                                                 | 106 ms: 1.02x faster                                  |
| async_tree_cpu_io_mixed  | 739 ms                                                 | 725 ms: 1.02x faster                                  |
| json_loads               | 26.5 us                                                | 26.0 us: 1.02x faster                                 |
| logging_simple           | 6.03 us                                                | 5.93 us: 1.02x faster                                 |
| meteor_contest           | 107 ms                                                 | 105 ms: 1.02x faster                                  |
| mdp                      | 2.62 sec                                               | 2.57 sec: 1.02x faster                                |
| pycparser                | 1.18 sec                                               | 1.16 sec: 1.02x faster                                |
| tornado_http             | 96.3 ms                                                | 95.2 ms: 1.01x faster                                 |
| regex_compile            | 138 ms                                                 | 137 ms: 1.01x faster                                  |
| xml_etree_iterparse      | 104 ms                                                 | 103 ms: 1.01x faster                                  |
| scimark_monte_carlo      | 68.1 ms                                                | 67.6 ms: 1.01x faster                                 |
| fannkuch                 | 388 ms                                                 | 386 ms: 1.01x faster                                  |
| bench_thread_pool        | 819 us                                                 | 817 us: 1.00x faster                                  |
| unpickle_list            | 4.91 us                                                | 4.94 us: 1.01x slower                                 |
| regex_v8                 | 22.0 ms                                                | 22.2 ms: 1.01x slower                                 |
| docutils                 | 2.63 sec                                               | 2.66 sec: 1.01x slower                                |
| scimark_lu               | 110 ms                                                 | 111 ms: 1.01x slower                                  |
| pathlib                  | 18.2 ms                                                | 18.6 ms: 1.02x slower                                 |
| create_gc_cycles         | 1.49 ms                                                | 1.52 ms: 1.02x slower                                 |
| pprint_pformat           | 1.46 sec                                               | 1.49 sec: 1.02x slower                                |
| pickle_dict              | 31.1 us                                                | 31.9 us: 1.03x slower                                 |
| deepcopy_memo            | 37.0 us                                                | 38.1 us: 1.03x slower                                 |
| float                    | 77.2 ms                                                | 79.7 ms: 1.03x slower                                 |
| dulwich_log              | 63.7 ms                                                | 65.8 ms: 1.03x slower                                 |
| deepcopy                 | 342 us                                                 | 354 us: 1.03x slower                                  |
| pprint_safe_repr         | 701 ms                                                 | 727 ms: 1.04x slower                                  |
| logging_silent           | 101 ns                                                 | 105 ns: 1.04x slower                                  |
| tomli_loads              | 2.22 sec                                               | 2.32 sec: 1.04x slower                                |
| richards                 | 45.7 ms                                                | 47.9 ms: 1.05x slower                                 |
| mako                     | 10.1 ms                                                | 10.6 ms: 1.05x slower                                 |
| regex_dna                | 204 ms                                                 | 216 ms: 1.06x slower                                  |
| scimark_sparse_mat_mult  | 4.50 ms                                                | 4.79 ms: 1.06x slower                                 |
| unpickle                 | 13.7 us                                                | 14.6 us: 1.07x slower                                 |
| gc_traversal             | 4.02 ms                                                | 4.32 ms: 1.07x slower                                 |
| pyflate                  | 418 ms                                                 | 449 ms: 1.07x slower                                  |
| sqlite_synth             | 2.52 us                                                | 2.71 us: 1.08x slower                                 |
| spectral_norm            | 100 ms                                                 | 108 ms: 1.08x slower                                  |
| deepcopy_reduce          | 2.94 us                                                | 3.17 us: 1.08x slower                                 |
| python_startup           | 8.52 ms                                                | 9.19 ms: 1.08x slower                                 |
| pickle                   | 10.1 us                                                | 10.9 us: 1.08x slower                                 |
| scimark_fft              | 328 ms                                                 | 354 ms: 1.08x slower                                  |
| xml_etree_process        | 53.9 ms                                                | 58.3 ms: 1.08x slower                                 |
| unpack_sequence          | 43.1 ns                                                | 46.7 ns: 1.08x slower                                 |
| telco                    | 6.58 ms                                                | 7.23 ms: 1.10x slower                                 |
| xml_etree_generate       | 76.2 ms                                                | 84.0 ms: 1.10x slower                                 |
| pickle_list              | 4.11 us                                                | 4.54 us: 1.10x slower                                 |
| python_startup_no_site   | 6.01 ms                                                | 6.68 ms: 1.11x slower                                 |
| async_generators         | 368 ms                                                 | 447 ms: 1.21x slower                                  |
| dask                     | 360 ms                                                 | 516 ms: 1.43x slower                                  |
| Geometric mean           | (ref)                                                  | 1.04x faster                                          |

Benchmark hidden because not significant (4): sqlglot_optimize, bench_mp_pool, scimark_sor, json
Ignored benchmarks (18) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 83.82% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x
