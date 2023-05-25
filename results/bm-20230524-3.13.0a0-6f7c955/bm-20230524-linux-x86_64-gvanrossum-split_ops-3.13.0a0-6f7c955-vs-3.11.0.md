
# Results vs. 3.11.0

- fork: gvanrossum
- ref: split_ops
- machine: linux-x86_64
- commit hash: 6f7c955
- commit date: 2023-05-24
- overall geometric mean: 1.03x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230524-linux-x86_64-gvanrossum-split_ops-3.13.0a0-6f7c955 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| docutils       | 2.63 sec                                               | 2.72 sec: 1.04x slower                                         |
| tornado_http   | 96.3 ms                                                | 102 ms: 1.06x slower                                           |
| Geometric mean | (ref)                                                  | 1.05x slower                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230524-linux-x86_64-gvanrossum-split_ops-3.13.0a0-6f7c955 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| nbody          | 93.1 ms                                                | 89.8 ms: 1.04x faster                                          |
| pidigits       | 198 ms                                                 | 197 ms: 1.00x faster                                           |
| float          | 77.2 ms                                                | 80.4 ms: 1.04x slower                                          |
| Geometric mean | (ref)                                                  | 1.00x faster                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230524-linux-x86_64-gvanrossum-split_ops-3.13.0a0-6f7c955 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.64 ms: 1.10x faster                                          |
| regex_v8       | 22.0 ms                                                | 22.8 ms: 1.03x slower                                          |
| regex_dna      | 204 ms                                                 | 214 ms: 1.05x slower                                           |
| regex_compile  | 138 ms                                                 | 145 ms: 1.05x slower                                           |
| Geometric mean | (ref)                                                  | 1.01x slower                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230524-linux-x86_64-gvanrossum-split_ops-3.13.0a0-6f7c955 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.78 ms: 1.29x faster                                          |
| json_loads           | 26.5 us                                                | 25.1 us: 1.06x faster                                          |
| unpickle_pure_python | 228 us                                                 | 218 us: 1.05x faster                                           |
| xml_etree_parse      | 158 ms                                                 | 154 ms: 1.03x faster                                           |
| tomli_loads          | 2.22 sec                                               | 2.18 sec: 1.02x faster                                         |
| pickle_dict          | 31.1 us                                                | 31.0 us: 1.00x faster                                          |
| pickle_pure_python   | 306 us                                                 | 315 us: 1.03x slower                                           |
| unpickle_list        | 4.91 us                                                | 5.08 us: 1.03x slower                                          |
| pickle               | 10.1 us                                                | 10.7 us: 1.06x slower                                          |
| xml_etree_process    | 53.9 ms                                                | 58.9 ms: 1.09x slower                                          |
| unpickle             | 13.7 us                                                | 15.2 us: 1.11x slower                                          |
| pickle_list          | 4.11 us                                                | 4.57 us: 1.11x slower                                          |
| xml_etree_generate   | 76.2 ms                                                | 85.7 ms: 1.12x slower                                          |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                   |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230524-linux-x86_64-gvanrossum-split_ops-3.13.0a0-6f7c955 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.33 ms: 1.09x slower                                          |
| python_startup_no_site | 6.01 ms                                                | 6.78 ms: 1.13x slower                                          |
| Geometric mean         | (ref)                                                  | 1.11x slower                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230524-linux-x86_64-gvanrossum-split_ops-3.13.0a0-6f7c955 |
|-----------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| mako      | 10.1 ms                                                | 10.4 ms: 1.04x slower                                          |

All benchmarks:
===============

| Benchmark                | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230524-linux-x86_64-gvanrossum-split_ops-3.13.0a0-6f7c955 |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| typing_runtime_protocols | 486 us                                                 | 140 us: 3.48x faster                                           |
| generators               | 73.5 ms                                                | 31.1 ms: 2.36x faster                                          |
| asyncio_tcp              | 922 ms                                                 | 515 ms: 1.79x faster                                           |
| asyncio_tcp_ssl          | 3.14 sec                                               | 1.80 sec: 1.74x faster                                         |
| json_dumps               | 12.6 ms                                                | 9.78 ms: 1.29x faster                                          |
| mypy2                    | 420 ms                                                 | 344 ms: 1.22x faster                                           |
| richards_super           | 56.8 ms                                                | 50.0 ms: 1.13x faster                                          |
| coroutines               | 25.5 ms                                                | 22.6 ms: 1.13x faster                                          |
| async_tree_none          | 526 ms                                                 | 471 ms: 1.12x faster                                           |
| async_tree_io            | 1.30 sec                                               | 1.16 sec: 1.12x faster                                         |
| regex_effbot             | 3.99 ms                                                | 3.64 ms: 1.10x faster                                          |
| async_tree_memoization   | 627 ms                                                 | 574 ms: 1.09x faster                                           |
| comprehensions           | 22.4 us                                                | 20.8 us: 1.08x faster                                          |
| deltablue                | 3.67 ms                                                | 3.46 ms: 1.06x faster                                          |
| chaos                    | 69.2 ms                                                | 65.4 ms: 1.06x faster                                          |
| json_loads               | 26.5 us                                                | 25.1 us: 1.06x faster                                          |
| sqlglot_parse            | 1.40 ms                                                | 1.33 ms: 1.06x faster                                          |
| hexiom                   | 6.37 ms                                                | 6.09 ms: 1.05x faster                                          |
| unpickle_pure_python     | 228 us                                                 | 218 us: 1.05x faster                                           |
| async_tree_cpu_io_mixed  | 739 ms                                                 | 711 ms: 1.04x faster                                           |
| logging_silent           | 101 ns                                                 | 97.2 ns: 1.04x faster                                          |
| nbody                    | 93.1 ms                                                | 89.8 ms: 1.04x faster                                          |
| sqlglot_transpile        | 1.70 ms                                                | 1.65 ms: 1.04x faster                                          |
| json                     | 4.94 ms                                                | 4.79 ms: 1.03x faster                                          |
| go                       | 140 ms                                                 | 136 ms: 1.03x faster                                           |
| xml_etree_parse          | 158 ms                                                 | 154 ms: 1.03x faster                                           |
| coverage                 | 100 ms                                                 | 97.5 ms: 1.03x faster                                          |
| meteor_contest           | 107 ms                                                 | 104 ms: 1.03x faster                                           |
| richards                 | 45.7 ms                                                | 44.6 ms: 1.02x faster                                          |
| nqueens                  | 83.4 ms                                                | 81.5 ms: 1.02x faster                                          |
| gc_traversal             | 4.02 ms                                                | 3.94 ms: 1.02x faster                                          |
| fannkuch                 | 388 ms                                                 | 380 ms: 1.02x faster                                           |
| tomli_loads              | 2.22 sec                                               | 2.18 sec: 1.02x faster                                         |
| pycparser                | 1.18 sec                                               | 1.17 sec: 1.01x faster                                         |
| pickle_dict              | 31.1 us                                                | 31.0 us: 1.00x faster                                          |
| pidigits                 | 198 ms                                                 | 197 ms: 1.00x faster                                           |
| raytrace                 | 297 ms                                                 | 298 ms: 1.01x slower                                           |
| pathlib                  | 18.2 ms                                                | 18.4 ms: 1.01x slower                                          |
| sqlglot_normalize        | 108 ms                                                 | 109 ms: 1.01x slower                                           |
| bench_thread_pool        | 819 us                                                 | 831 us: 1.01x slower                                           |
| pprint_pformat           | 1.46 sec                                               | 1.48 sec: 1.02x slower                                         |
| sqlglot_optimize         | 53.1 ms                                                | 54.1 ms: 1.02x slower                                          |
| create_gc_cycles         | 1.49 ms                                                | 1.52 ms: 1.02x slower                                          |
| pickle_pure_python       | 306 us                                                 | 315 us: 1.03x slower                                           |
| mdp                      | 2.62 sec                                               | 2.70 sec: 1.03x slower                                         |
| deepcopy_memo            | 37.0 us                                                | 38.2 us: 1.03x slower                                          |
| scimark_sor              | 118 ms                                                 | 122 ms: 1.03x slower                                           |
| regex_v8                 | 22.0 ms                                                | 22.8 ms: 1.03x slower                                          |
| unpickle_list            | 4.91 us                                                | 5.08 us: 1.03x slower                                          |
| mako                     | 10.1 ms                                                | 10.4 ms: 1.04x slower                                          |
| pprint_safe_repr         | 701 ms                                                 | 727 ms: 1.04x slower                                           |
| docutils                 | 2.63 sec                                               | 2.72 sec: 1.04x slower                                         |
| float                    | 77.2 ms                                                | 80.4 ms: 1.04x slower                                          |
| deepcopy                 | 342 us                                                 | 357 us: 1.04x slower                                           |
| telco                    | 6.58 ms                                                | 6.88 ms: 1.05x slower                                          |
| crypto_pyaes             | 74.7 ms                                                | 78.1 ms: 1.05x slower                                          |
| regex_dna                | 204 ms                                                 | 214 ms: 1.05x slower                                           |
| regex_compile            | 138 ms                                                 | 145 ms: 1.05x slower                                           |
| scimark_monte_carlo      | 68.1 ms                                                | 71.5 ms: 1.05x slower                                          |
| pyflate                  | 418 ms                                                 | 441 ms: 1.05x slower                                           |
| logging_simple           | 6.03 us                                                | 6.37 us: 1.06x slower                                          |
| scimark_lu               | 110 ms                                                 | 116 ms: 1.06x slower                                           |
| pickle                   | 10.1 us                                                | 10.7 us: 1.06x slower                                          |
| tornado_http             | 96.3 ms                                                | 102 ms: 1.06x slower                                           |
| logging_format           | 6.68 us                                                | 7.10 us: 1.06x slower                                          |
| scimark_sparse_mat_mult  | 4.50 ms                                                | 4.78 ms: 1.06x slower                                          |
| scimark_fft              | 328 ms                                                 | 351 ms: 1.07x slower                                           |
| dulwich_log              | 63.7 ms                                                | 68.1 ms: 1.07x slower                                          |
| deepcopy_reduce          | 2.94 us                                                | 3.15 us: 1.07x slower                                          |
| spectral_norm            | 100 ms                                                 | 108 ms: 1.08x slower                                           |
| sqlite_synth             | 2.52 us                                                | 2.74 us: 1.09x slower                                          |
| xml_etree_process        | 53.9 ms                                                | 58.9 ms: 1.09x slower                                          |
| python_startup           | 8.52 ms                                                | 9.33 ms: 1.09x slower                                          |
| unpickle                 | 13.7 us                                                | 15.2 us: 1.11x slower                                          |
| pickle_list              | 4.11 us                                                | 4.57 us: 1.11x slower                                          |
| xml_etree_generate       | 76.2 ms                                                | 85.7 ms: 1.12x slower                                          |
| python_startup_no_site   | 6.01 ms                                                | 6.78 ms: 1.13x slower                                          |
| unpack_sequence          | 43.1 ns                                                | 50.4 ns: 1.17x slower                                          |
| async_generators         | 368 ms                                                 | 446 ms: 1.21x slower                                           |
| dask                     | 360 ms                                                 | 536 ms: 1.49x slower                                           |
| Geometric mean           | (ref)                                                  | 1.03x faster                                                   |

Benchmark hidden because not significant (2): bench_mp_pool, xml_etree_iterparse
Ignored benchmarks (18) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
