
# Results vs. 3.11.0

- fork: python
- ref: 3.12
- machine: linux-x86_64
- commit hash: 9cd3664
- commit date: 2023-06-24
- overall geometric mean: 1.03x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230624-linux-x86_64-python-3.12-3.12.0b3+-9cd3664 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 269 ms: 1.04x slower                                   |
| docutils       | 2.63 sec                                               | 2.72 sec: 1.04x slower                                 |
| tornado_http   | 96.3 ms                                                | 99.9 ms: 1.04x slower                                  |
| Geometric mean | (ref)                                                  | 1.04x slower                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230624-linux-x86_64-python-3.12-3.12.0b3+-9cd3664 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 93.1 ms                                                | 91.0 ms: 1.02x faster                                  |
| pidigits       | 198 ms                                                 | 197 ms: 1.00x faster                                   |
| float          | 77.2 ms                                                | 80.6 ms: 1.04x slower                                  |
| Geometric mean | (ref)                                                  | 1.01x slower                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230624-linux-x86_64-python-3.12-3.12.0b3+-9cd3664 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.66 ms: 1.09x faster                                  |
| regex_dna      | 204 ms                                                 | 200 ms: 1.02x faster                                   |
| regex_v8       | 22.0 ms                                                | 22.7 ms: 1.03x slower                                  |
| regex_compile  | 138 ms                                                 | 145 ms: 1.05x slower                                   |
| Geometric mean | (ref)                                                  | 1.01x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230624-linux-x86_64-python-3.12-3.12.0b3+-9cd3664 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.73 ms: 1.29x faster                                  |
| json_loads           | 26.5 us                                                | 24.9 us: 1.06x faster                                  |
| unpickle_pure_python | 228 us                                                 | 215 us: 1.06x faster                                   |
| xml_etree_parse      | 158 ms                                                 | 152 ms: 1.04x faster                                   |
| tomli_loads          | 2.22 sec                                               | 2.17 sec: 1.02x faster                                 |
| xml_etree_iterparse  | 104 ms                                                 | 103 ms: 1.01x faster                                   |
| pickle_pure_python   | 306 us                                                 | 310 us: 1.02x slower                                   |
| pickle_dict          | 31.1 us                                                | 31.8 us: 1.02x slower                                  |
| pickle               | 10.1 us                                                | 10.9 us: 1.08x slower                                  |
| unpickle             | 13.7 us                                                | 15.0 us: 1.10x slower                                  |
| xml_etree_process    | 53.9 ms                                                | 59.7 ms: 1.11x slower                                  |
| xml_etree_generate   | 76.2 ms                                                | 84.9 ms: 1.11x slower                                  |
| pickle_list          | 4.11 us                                                | 4.71 us: 1.15x slower                                  |
| Geometric mean       | (ref)                                                  | 1.01x slower                                           |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230624-linux-x86_64-python-3.12-3.12.0b3+-9cd3664 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.33 ms: 1.09x slower                                  |
| python_startup_no_site | 6.01 ms                                                | 6.78 ms: 1.13x slower                                  |
| Geometric mean         | (ref)                                                  | 1.11x slower                                           |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230624-linux-x86_64-python-3.12-3.12.0b3+-9cd3664 |
|-----------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako      | 10.1 ms                                                | 10.6 ms: 1.06x slower                                  |

All benchmarks:
===============

| Benchmark                | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230624-linux-x86_64-python-3.12-3.12.0b3+-9cd3664 |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| typing_runtime_protocols | 486 us                                                 | 144 us: 3.37x faster                                   |
| generators               | 73.5 ms                                                | 31.3 ms: 2.34x faster                                  |
| asyncio_tcp              | 922 ms                                                 | 510 ms: 1.81x faster                                   |
| asyncio_tcp_ssl          | 3.14 sec                                               | 1.80 sec: 1.74x faster                                 |
| json_dumps               | 12.6 ms                                                | 9.73 ms: 1.29x faster                                  |
| mypy2                    | 420 ms                                                 | 343 ms: 1.22x faster                                   |
| richards_super           | 56.8 ms                                                | 49.2 ms: 1.15x faster                                  |
| coroutines               | 25.5 ms                                                | 22.1 ms: 1.15x faster                                  |
| async_tree_none          | 526 ms                                                 | 471 ms: 1.12x faster                                   |
| async_tree_io            | 1.30 sec                                               | 1.16 sec: 1.12x faster                                 |
| chaos                    | 69.2 ms                                                | 63.2 ms: 1.09x faster                                  |
| async_tree_memoization   | 627 ms                                                 | 574 ms: 1.09x faster                                   |
| regex_effbot             | 3.99 ms                                                | 3.66 ms: 1.09x faster                                  |
| json_loads               | 26.5 us                                                | 24.9 us: 1.06x faster                                  |
| comprehensions           | 22.4 us                                                | 21.1 us: 1.06x faster                                  |
| unpickle_pure_python     | 228 us                                                 | 215 us: 1.06x faster                                   |
| deltablue                | 3.67 ms                                                | 3.47 ms: 1.06x faster                                  |
| coverage                 | 100 ms                                                 | 94.6 ms: 1.06x faster                                  |
| sqlglot_parse            | 1.40 ms                                                | 1.33 ms: 1.05x faster                                  |
| gc_traversal             | 4.02 ms                                                | 3.83 ms: 1.05x faster                                  |
| hexiom                   | 6.37 ms                                                | 6.07 ms: 1.05x faster                                  |
| xml_etree_parse          | 158 ms                                                 | 152 ms: 1.04x faster                                   |
| json                     | 4.94 ms                                                | 4.76 ms: 1.04x faster                                  |
| async_tree_cpu_io_mixed  | 739 ms                                                 | 712 ms: 1.04x faster                                   |
| richards                 | 45.7 ms                                                | 44.1 ms: 1.04x faster                                  |
| logging_silent           | 101 ns                                                 | 97.9 ns: 1.03x faster                                  |
| go                       | 140 ms                                                 | 136 ms: 1.03x faster                                   |
| sqlglot_transpile        | 1.70 ms                                                | 1.65 ms: 1.03x faster                                  |
| nqueens                  | 83.4 ms                                                | 81.0 ms: 1.03x faster                                  |
| nbody                    | 93.1 ms                                                | 91.0 ms: 1.02x faster                                  |
| tomli_loads              | 2.22 sec                                               | 2.17 sec: 1.02x faster                                 |
| pycparser                | 1.18 sec                                               | 1.16 sec: 1.02x faster                                 |
| regex_dna                | 204 ms                                                 | 200 ms: 1.02x faster                                   |
| meteor_contest           | 107 ms                                                 | 105 ms: 1.02x faster                                   |
| mdp                      | 2.62 sec                                               | 2.58 sec: 1.01x faster                                 |
| raytrace                 | 297 ms                                                 | 294 ms: 1.01x faster                                   |
| xml_etree_iterparse      | 104 ms                                                 | 103 ms: 1.01x faster                                   |
| pidigits                 | 198 ms                                                 | 197 ms: 1.00x faster                                   |
| sqlglot_normalize        | 108 ms                                                 | 109 ms: 1.01x slower                                   |
| sqlglot_optimize         | 53.1 ms                                                | 53.7 ms: 1.01x slower                                  |
| bench_thread_pool        | 819 us                                                 | 828 us: 1.01x slower                                   |
| scimark_lu               | 110 ms                                                 | 111 ms: 1.01x slower                                   |
| pickle_pure_python       | 306 us                                                 | 310 us: 1.02x slower                                   |
| create_gc_cycles         | 1.49 ms                                                | 1.51 ms: 1.02x slower                                  |
| pickle_dict              | 31.1 us                                                | 31.8 us: 1.02x slower                                  |
| deepcopy_memo            | 37.0 us                                                | 37.8 us: 1.02x slower                                  |
| logging_format           | 6.68 us                                                | 6.87 us: 1.03x slower                                  |
| sqlalchemy_imperative    | 17.9 ms                                                | 18.4 ms: 1.03x slower                                  |
| regex_v8                 | 22.0 ms                                                | 22.7 ms: 1.03x slower                                  |
| telco                    | 6.58 ms                                                | 6.80 ms: 1.03x slower                                  |
| pprint_pformat           | 1.46 sec                                               | 1.51 sec: 1.03x slower                                 |
| logging_simple           | 6.03 us                                                | 6.24 us: 1.03x slower                                  |
| spectral_norm            | 100 ms                                                 | 104 ms: 1.04x slower                                   |
| docutils                 | 2.63 sec                                               | 2.72 sec: 1.04x slower                                 |
| 2to3                     | 259 ms                                                 | 269 ms: 1.04x slower                                   |
| tornado_http             | 96.3 ms                                                | 99.9 ms: 1.04x slower                                  |
| scimark_sor              | 118 ms                                                 | 123 ms: 1.04x slower                                   |
| crypto_pyaes             | 74.7 ms                                                | 77.8 ms: 1.04x slower                                  |
| float                    | 77.2 ms                                                | 80.6 ms: 1.04x slower                                  |
| deepcopy                 | 342 us                                                 | 357 us: 1.04x slower                                   |
| sqlalchemy_declarative   | 138 ms                                                 | 144 ms: 1.05x slower                                   |
| regex_compile            | 138 ms                                                 | 145 ms: 1.05x slower                                   |
| pprint_safe_repr         | 701 ms                                                 | 737 ms: 1.05x slower                                   |
| scimark_monte_carlo      | 68.1 ms                                                | 71.8 ms: 1.06x slower                                  |
| mako                     | 10.1 ms                                                | 10.6 ms: 1.06x slower                                  |
| pyflate                  | 418 ms                                                 | 444 ms: 1.06x slower                                   |
| dulwich_log              | 63.7 ms                                                | 68.0 ms: 1.07x slower                                  |
| scimark_sparse_mat_mult  | 4.50 ms                                                | 4.83 ms: 1.07x slower                                  |
| sqlite_synth             | 2.52 us                                                | 2.71 us: 1.07x slower                                  |
| deepcopy_reduce          | 2.94 us                                                | 3.17 us: 1.08x slower                                  |
| pickle                   | 10.1 us                                                | 10.9 us: 1.08x slower                                  |
| scimark_fft              | 328 ms                                                 | 356 ms: 1.08x slower                                   |
| python_startup           | 8.52 ms                                                | 9.33 ms: 1.09x slower                                  |
| unpickle                 | 13.7 us                                                | 15.0 us: 1.10x slower                                  |
| xml_etree_process        | 53.9 ms                                                | 59.7 ms: 1.11x slower                                  |
| xml_etree_generate       | 76.2 ms                                                | 84.9 ms: 1.11x slower                                  |
| python_startup_no_site   | 6.01 ms                                                | 6.78 ms: 1.13x slower                                  |
| pickle_list              | 4.11 us                                                | 4.71 us: 1.15x slower                                  |
| unpack_sequence          | 43.1 ns                                                | 51.4 ns: 1.19x slower                                  |
| async_generators         | 368 ms                                                 | 445 ms: 1.21x slower                                   |
| dask                     | 360 ms                                                 | 535 ms: 1.49x slower                                   |
| Geometric mean           | (ref)                                                  | 1.03x faster                                           |

Benchmark hidden because not significant (4): pathlib, bench_mp_pool, fannkuch, unpickle_list
Ignored benchmarks (15) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
