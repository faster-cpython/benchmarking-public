
# Results vs. 3.11.0

- fork: python
- ref: 3.12
- machine: linux-x86_64
- commit hash: 730c873
- commit date: 2023-07-01
- overall geometric mean: 1.03x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230701-linux-x86_64-python-3.12-3.12.0b3+-730c873 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 267 ms: 1.03x slower                                   |
| docutils       | 2.63 sec                                               | 2.70 sec: 1.03x slower                                 |
| tornado_http   | 96.3 ms                                                | 98.6 ms: 1.02x slower                                  |
| Geometric mean | (ref)                                                  | 1.03x slower                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230701-linux-x86_64-python-3.12-3.12.0b3+-730c873 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 93.1 ms                                                | 87.5 ms: 1.06x faster                                  |
| pidigits       | 198 ms                                                 | 197 ms: 1.00x faster                                   |
| float          | 77.2 ms                                                | 80.5 ms: 1.04x slower                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230701-linux-x86_64-python-3.12-3.12.0b3+-730c873 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.47 ms: 1.15x faster                                  |
| regex_dna      | 204 ms                                                 | 203 ms: 1.00x faster                                   |
| regex_compile  | 138 ms                                                 | 143 ms: 1.04x slower                                   |
| regex_v8       | 22.0 ms                                                | 23.0 ms: 1.04x slower                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230701-linux-x86_64-python-3.12-3.12.0b3+-730c873 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.82 ms: 1.28x faster                                  |
| unpickle_pure_python | 228 us                                                 | 217 us: 1.05x faster                                   |
| json_loads           | 26.5 us                                                | 25.8 us: 1.03x faster                                  |
| xml_etree_parse      | 158 ms                                                 | 154 ms: 1.03x faster                                   |
| tomli_loads          | 2.22 sec                                               | 2.19 sec: 1.01x faster                                 |
| pickle_dict          | 31.1 us                                                | 30.7 us: 1.01x faster                                  |
| unpickle_list        | 4.91 us                                                | 4.98 us: 1.01x slower                                  |
| pickle_pure_python   | 306 us                                                 | 310 us: 1.01x slower                                   |
| pickle               | 10.1 us                                                | 11.0 us: 1.09x slower                                  |
| pickle_list          | 4.11 us                                                | 4.52 us: 1.10x slower                                  |
| unpickle             | 13.7 us                                                | 15.2 us: 1.11x slower                                  |
| xml_etree_process    | 53.9 ms                                                | 59.8 ms: 1.11x slower                                  |
| xml_etree_generate   | 76.2 ms                                                | 85.1 ms: 1.12x slower                                  |
| Geometric mean       | (ref)                                                  | 1.01x slower                                           |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230701-linux-x86_64-python-3.12-3.12.0b3+-730c873 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.32 ms: 1.09x slower                                  |
| python_startup_no_site | 6.01 ms                                                | 6.77 ms: 1.13x slower                                  |
| Geometric mean         | (ref)                                                  | 1.11x slower                                           |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230701-linux-x86_64-python-3.12-3.12.0b3+-730c873 |
|-----------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako      | 10.1 ms                                                | 10.7 ms: 1.06x slower                                  |

All benchmarks:
===============

| Benchmark                | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230701-linux-x86_64-python-3.12-3.12.0b3+-730c873 |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| typing_runtime_protocols | 486 us                                                 | 145 us: 3.34x faster                                   |
| generators               | 73.5 ms                                                | 31.6 ms: 2.32x faster                                  |
| asyncio_tcp              | 922 ms                                                 | 514 ms: 1.79x faster                                   |
| asyncio_tcp_ssl          | 3.14 sec                                               | 1.79 sec: 1.75x faster                                 |
| json_dumps               | 12.6 ms                                                | 9.82 ms: 1.28x faster                                  |
| mypy2                    | 420 ms                                                 | 344 ms: 1.22x faster                                   |
| coroutines               | 25.5 ms                                                | 22.0 ms: 1.16x faster                                  |
| regex_effbot             | 3.99 ms                                                | 3.47 ms: 1.15x faster                                  |
| richards_super           | 56.8 ms                                                | 49.6 ms: 1.14x faster                                  |
| async_tree_none          | 526 ms                                                 | 471 ms: 1.12x faster                                   |
| async_tree_io            | 1.30 sec                                               | 1.16 sec: 1.12x faster                                 |
| async_tree_memoization   | 627 ms                                                 | 573 ms: 1.10x faster                                   |
| comprehensions           | 22.4 us                                                | 20.5 us: 1.09x faster                                  |
| chaos                    | 69.2 ms                                                | 63.4 ms: 1.09x faster                                  |
| coverage                 | 100 ms                                                 | 93.6 ms: 1.07x faster                                  |
| nbody                    | 93.1 ms                                                | 87.5 ms: 1.06x faster                                  |
| sqlglot_parse            | 1.40 ms                                                | 1.33 ms: 1.06x faster                                  |
| unpickle_pure_python     | 228 us                                                 | 217 us: 1.05x faster                                   |
| richards                 | 45.7 ms                                                | 43.5 ms: 1.05x faster                                  |
| deltablue                | 3.67 ms                                                | 3.51 ms: 1.05x faster                                  |
| async_tree_cpu_io_mixed  | 739 ms                                                 | 712 ms: 1.04x faster                                   |
| sqlglot_transpile        | 1.70 ms                                                | 1.64 ms: 1.04x faster                                  |
| hexiom                   | 6.37 ms                                                | 6.17 ms: 1.03x faster                                  |
| json_loads               | 26.5 us                                                | 25.8 us: 1.03x faster                                  |
| pycparser                | 1.18 sec                                               | 1.15 sec: 1.03x faster                                 |
| go                       | 140 ms                                                 | 136 ms: 1.03x faster                                   |
| xml_etree_parse          | 158 ms                                                 | 154 ms: 1.03x faster                                   |
| nqueens                  | 83.4 ms                                                | 81.4 ms: 1.02x faster                                  |
| meteor_contest           | 107 ms                                                 | 105 ms: 1.02x faster                                   |
| tomli_loads              | 2.22 sec                                               | 2.19 sec: 1.01x faster                                 |
| pickle_dict              | 31.1 us                                                | 30.7 us: 1.01x faster                                  |
| raytrace                 | 297 ms                                                 | 293 ms: 1.01x faster                                   |
| gc_traversal             | 4.02 ms                                                | 3.99 ms: 1.01x faster                                  |
| fannkuch                 | 388 ms                                                 | 385 ms: 1.01x faster                                   |
| pathlib                  | 18.2 ms                                                | 18.1 ms: 1.01x faster                                  |
| regex_dna                | 204 ms                                                 | 203 ms: 1.00x faster                                   |
| pidigits                 | 198 ms                                                 | 197 ms: 1.00x faster                                   |
| logging_silent           | 101 ns                                                 | 102 ns: 1.01x slower                                   |
| sqlglot_normalize        | 108 ms                                                 | 109 ms: 1.01x slower                                   |
| bench_thread_pool        | 819 us                                                 | 830 us: 1.01x slower                                   |
| unpickle_list            | 4.91 us                                                | 4.98 us: 1.01x slower                                  |
| sqlglot_optimize         | 53.1 ms                                                | 53.9 ms: 1.01x slower                                  |
| pickle_pure_python       | 306 us                                                 | 310 us: 1.01x slower                                   |
| pprint_pformat           | 1.46 sec                                               | 1.49 sec: 1.02x slower                                 |
| create_gc_cycles         | 1.49 ms                                                | 1.52 ms: 1.02x slower                                  |
| tornado_http             | 96.3 ms                                                | 98.6 ms: 1.02x slower                                  |
| scimark_lu               | 110 ms                                                 | 113 ms: 1.03x slower                                   |
| sqlalchemy_imperative    | 17.9 ms                                                | 18.4 ms: 1.03x slower                                  |
| docutils                 | 2.63 sec                                               | 2.70 sec: 1.03x slower                                 |
| deepcopy_memo            | 37.0 us                                                | 38.1 us: 1.03x slower                                  |
| mdp                      | 2.62 sec                                               | 2.69 sec: 1.03x slower                                 |
| 2to3                     | 259 ms                                                 | 267 ms: 1.03x slower                                   |
| logging_format           | 6.68 us                                                | 6.89 us: 1.03x slower                                  |
| logging_simple           | 6.03 us                                                | 6.24 us: 1.03x slower                                  |
| regex_compile            | 138 ms                                                 | 143 ms: 1.04x slower                                   |
| spectral_norm            | 100 ms                                                 | 104 ms: 1.04x slower                                   |
| float                    | 77.2 ms                                                | 80.5 ms: 1.04x slower                                  |
| regex_v8                 | 22.0 ms                                                | 23.0 ms: 1.04x slower                                  |
| deepcopy                 | 342 us                                                 | 357 us: 1.04x slower                                   |
| telco                    | 6.58 ms                                                | 6.88 ms: 1.05x slower                                  |
| sqlalchemy_declarative   | 138 ms                                                 | 145 ms: 1.05x slower                                   |
| scimark_sor              | 118 ms                                                 | 124 ms: 1.05x slower                                   |
| crypto_pyaes             | 74.7 ms                                                | 78.4 ms: 1.05x slower                                  |
| pprint_safe_repr         | 701 ms                                                 | 738 ms: 1.05x slower                                   |
| scimark_sparse_mat_mult  | 4.50 ms                                                | 4.75 ms: 1.06x slower                                  |
| scimark_monte_carlo      | 68.1 ms                                                | 71.9 ms: 1.06x slower                                  |
| mako                     | 10.1 ms                                                | 10.7 ms: 1.06x slower                                  |
| pyflate                  | 418 ms                                                 | 445 ms: 1.06x slower                                   |
| dulwich_log              | 63.7 ms                                                | 67.8 ms: 1.07x slower                                  |
| scimark_fft              | 328 ms                                                 | 350 ms: 1.07x slower                                   |
| sqlite_synth             | 2.52 us                                                | 2.74 us: 1.09x slower                                  |
| deepcopy_reduce          | 2.94 us                                                | 3.20 us: 1.09x slower                                  |
| pickle                   | 10.1 us                                                | 11.0 us: 1.09x slower                                  |
| python_startup           | 8.52 ms                                                | 9.32 ms: 1.09x slower                                  |
| pickle_list              | 4.11 us                                                | 4.52 us: 1.10x slower                                  |
| unpickle                 | 13.7 us                                                | 15.2 us: 1.11x slower                                  |
| xml_etree_process        | 53.9 ms                                                | 59.8 ms: 1.11x slower                                  |
| xml_etree_generate       | 76.2 ms                                                | 85.1 ms: 1.12x slower                                  |
| python_startup_no_site   | 6.01 ms                                                | 6.77 ms: 1.13x slower                                  |
| unpack_sequence          | 43.1 ns                                                | 51.5 ns: 1.19x slower                                  |
| async_generators         | 368 ms                                                 | 445 ms: 1.21x slower                                   |
| dask                     | 360 ms                                                 | 535 ms: 1.49x slower                                   |
| Geometric mean           | (ref)                                                  | 1.03x faster                                           |

Benchmark hidden because not significant (3): bench_mp_pool, xml_etree_iterparse, json
Ignored benchmarks (15) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
