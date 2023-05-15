
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 7d2deaf
- commit date: 2023-05-13
- overall geometric mean: 1.03x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230513-linux-x86_64-python-main-3.12.0a7+-7d2deaf |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 268 ms: 1.03x slower                                   |
| docutils       | 2.63 sec                                               | 2.71 sec: 1.03x slower                                 |
| tornado_http   | 96.3 ms                                                | 99.2 ms: 1.03x slower                                  |
| Geometric mean | (ref)                                                  | 1.03x slower                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230513-linux-x86_64-python-main-3.12.0a7+-7d2deaf |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pidigits       | 198 ms                                                 | 189 ms: 1.05x faster                                   |
| nbody          | 93.1 ms                                                | 90.4 ms: 1.03x faster                                  |
| float          | 77.2 ms                                                | 81.1 ms: 1.05x slower                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230513-linux-x86_64-python-main-3.12.0a7+-7d2deaf |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.63 ms: 1.10x faster                                  |
| regex_v8       | 22.0 ms                                                | 21.9 ms: 1.01x faster                                  |
| regex_dna      | 204 ms                                                 | 204 ms: 1.00x faster                                   |
| regex_compile  | 138 ms                                                 | 147 ms: 1.07x slower                                   |
| Geometric mean | (ref)                                                  | 1.01x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230513-linux-x86_64-python-main-3.12.0a7+-7d2deaf |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.75 ms: 1.29x faster                                  |
| json_loads           | 26.5 us                                                | 25.0 us: 1.06x faster                                  |
| unpickle_pure_python | 228 us                                                 | 218 us: 1.04x faster                                   |
| xml_etree_parse      | 158 ms                                                 | 154 ms: 1.03x faster                                   |
| unpickle_list        | 4.91 us                                                | 4.88 us: 1.01x faster                                  |
| pickle_dict          | 31.1 us                                                | 31.3 us: 1.00x slower                                  |
| pickle_pure_python   | 306 us                                                 | 313 us: 1.02x slower                                   |
| unpickle             | 13.7 us                                                | 14.4 us: 1.05x slower                                  |
| pickle               | 10.1 us                                                | 10.8 us: 1.07x slower                                  |
| xml_etree_process    | 53.9 ms                                                | 59.3 ms: 1.10x slower                                  |
| xml_etree_generate   | 76.2 ms                                                | 85.8 ms: 1.13x slower                                  |
| pickle_list          | 4.11 us                                                | 4.69 us: 1.14x slower                                  |
| Geometric mean       | (ref)                                                  | 1.01x slower                                           |

Benchmark hidden because not significant (2): xml_etree_iterparse, tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230513-linux-x86_64-python-main-3.12.0a7+-7d2deaf |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.13 ms: 1.07x slower                                  |
| python_startup_no_site | 6.01 ms                                                | 6.66 ms: 1.11x slower                                  |
| Geometric mean         | (ref)                                                  | 1.09x slower                                           |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230513-linux-x86_64-python-main-3.12.0a7+-7d2deaf |
|-----------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako      | 10.1 ms                                                | 10.9 ms: 1.08x slower                                  |

All benchmarks:
===============

| Benchmark                | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230513-linux-x86_64-python-main-3.12.0a7+-7d2deaf |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| typing_runtime_protocols | 486 us                                                 | 148 us: 3.29x faster                                   |
| generators               | 73.5 ms                                                | 30.8 ms: 2.39x faster                                  |
| asyncio_tcp              | 922 ms                                                 | 514 ms: 1.79x faster                                   |
| asyncio_tcp_ssl          | 3.14 sec                                               | 1.80 sec: 1.74x faster                                 |
| json_dumps               | 12.6 ms                                                | 9.75 ms: 1.29x faster                                  |
| mypy2                    | 420 ms                                                 | 345 ms: 1.22x faster                                   |
| async_tree_none          | 526 ms                                                 | 468 ms: 1.13x faster                                   |
| async_tree_io            | 1.30 sec                                               | 1.15 sec: 1.12x faster                                 |
| richards_super           | 56.8 ms                                                | 50.5 ms: 1.12x faster                                  |
| coroutines               | 25.5 ms                                                | 22.9 ms: 1.12x faster                                  |
| async_tree_memoization   | 627 ms                                                 | 569 ms: 1.10x faster                                   |
| regex_effbot             | 3.99 ms                                                | 3.63 ms: 1.10x faster                                  |
| comprehensions           | 22.4 us                                                | 20.5 us: 1.10x faster                                  |
| json_loads               | 26.5 us                                                | 25.0 us: 1.06x faster                                  |
| chaos                    | 69.2 ms                                                | 65.4 ms: 1.06x faster                                  |
| sqlglot_parse            | 1.40 ms                                                | 1.33 ms: 1.05x faster                                  |
| async_tree_cpu_io_mixed  | 739 ms                                                 | 704 ms: 1.05x faster                                   |
| pidigits                 | 198 ms                                                 | 189 ms: 1.05x faster                                   |
| unpickle_pure_python     | 228 us                                                 | 218 us: 1.04x faster                                   |
| deltablue                | 3.67 ms                                                | 3.53 ms: 1.04x faster                                  |
| coverage                 | 100 ms                                                 | 96.4 ms: 1.04x faster                                  |
| nqueens                  | 83.4 ms                                                | 80.5 ms: 1.04x faster                                  |
| hexiom                   | 6.37 ms                                                | 6.16 ms: 1.03x faster                                  |
| json                     | 4.94 ms                                                | 4.79 ms: 1.03x faster                                  |
| sqlglot_transpile        | 1.70 ms                                                | 1.65 ms: 1.03x faster                                  |
| nbody                    | 93.1 ms                                                | 90.4 ms: 1.03x faster                                  |
| xml_etree_parse          | 158 ms                                                 | 154 ms: 1.03x faster                                   |
| mdp                      | 2.62 sec                                               | 2.54 sec: 1.03x faster                                 |
| meteor_contest           | 107 ms                                                 | 104 ms: 1.03x faster                                   |
| richards                 | 45.7 ms                                                | 44.7 ms: 1.02x faster                                  |
| go                       | 140 ms                                                 | 138 ms: 1.02x faster                                   |
| create_gc_cycles         | 1.49 ms                                                | 1.47 ms: 1.01x faster                                  |
| regex_v8                 | 22.0 ms                                                | 21.9 ms: 1.01x faster                                  |
| unpickle_list            | 4.91 us                                                | 4.88 us: 1.01x faster                                  |
| regex_dna                | 204 ms                                                 | 204 ms: 1.00x faster                                   |
| pickle_dict              | 31.1 us                                                | 31.3 us: 1.00x slower                                  |
| logging_silent           | 101 ns                                                 | 102 ns: 1.01x slower                                   |
| sqlglot_normalize        | 108 ms                                                 | 109 ms: 1.01x slower                                   |
| pathlib                  | 18.2 ms                                                | 18.4 ms: 1.01x slower                                  |
| bench_thread_pool        | 819 us                                                 | 828 us: 1.01x slower                                   |
| gc_traversal             | 4.02 ms                                                | 4.07 ms: 1.01x slower                                  |
| pycparser                | 1.18 sec                                               | 1.20 sec: 1.01x slower                                 |
| raytrace                 | 297 ms                                                 | 301 ms: 1.01x slower                                   |
| sqlglot_optimize         | 53.1 ms                                                | 54.1 ms: 1.02x slower                                  |
| pickle_pure_python       | 306 us                                                 | 313 us: 1.02x slower                                   |
| crypto_pyaes             | 74.7 ms                                                | 76.8 ms: 1.03x slower                                  |
| tornado_http             | 96.3 ms                                                | 99.2 ms: 1.03x slower                                  |
| pprint_pformat           | 1.46 sec                                               | 1.50 sec: 1.03x slower                                 |
| docutils                 | 2.63 sec                                               | 2.71 sec: 1.03x slower                                 |
| 2to3                     | 259 ms                                                 | 268 ms: 1.03x slower                                   |
| sqlalchemy_imperative    | 17.9 ms                                                | 18.6 ms: 1.04x slower                                  |
| deepcopy                 | 342 us                                                 | 355 us: 1.04x slower                                   |
| logging_format           | 6.68 us                                                | 6.95 us: 1.04x slower                                  |
| deepcopy_memo            | 37.0 us                                                | 38.6 us: 1.04x slower                                  |
| logging_simple           | 6.03 us                                                | 6.29 us: 1.04x slower                                  |
| scimark_sor              | 118 ms                                                 | 123 ms: 1.05x slower                                   |
| scimark_lu               | 110 ms                                                 | 115 ms: 1.05x slower                                   |
| sqlalchemy_declarative   | 138 ms                                                 | 145 ms: 1.05x slower                                   |
| float                    | 77.2 ms                                                | 81.1 ms: 1.05x slower                                  |
| pprint_safe_repr         | 701 ms                                                 | 737 ms: 1.05x slower                                   |
| unpickle                 | 13.7 us                                                | 14.4 us: 1.05x slower                                  |
| spectral_norm            | 100 ms                                                 | 105 ms: 1.05x slower                                   |
| dulwich_log              | 63.7 ms                                                | 67.4 ms: 1.06x slower                                  |
| telco                    | 6.58 ms                                                | 6.97 ms: 1.06x slower                                  |
| regex_compile            | 138 ms                                                 | 147 ms: 1.07x slower                                   |
| pickle                   | 10.1 us                                                | 10.8 us: 1.07x slower                                  |
| python_startup           | 8.52 ms                                                | 9.13 ms: 1.07x slower                                  |
| scimark_sparse_mat_mult  | 4.50 ms                                                | 4.85 ms: 1.08x slower                                  |
| mako                     | 10.1 ms                                                | 10.9 ms: 1.08x slower                                  |
| deepcopy_reduce          | 2.94 us                                                | 3.18 us: 1.08x slower                                  |
| sqlite_synth             | 2.52 us                                                | 2.73 us: 1.09x slower                                  |
| pyflate                  | 418 ms                                                 | 454 ms: 1.09x slower                                   |
| scimark_monte_carlo      | 68.1 ms                                                | 74.0 ms: 1.09x slower                                  |
| scimark_fft              | 328 ms                                                 | 360 ms: 1.10x slower                                   |
| xml_etree_process        | 53.9 ms                                                | 59.3 ms: 1.10x slower                                  |
| python_startup_no_site   | 6.01 ms                                                | 6.66 ms: 1.11x slower                                  |
| xml_etree_generate       | 76.2 ms                                                | 85.8 ms: 1.13x slower                                  |
| unpack_sequence          | 43.1 ns                                                | 49.1 ns: 1.14x slower                                  |
| pickle_list              | 4.11 us                                                | 4.69 us: 1.14x slower                                  |
| async_generators         | 368 ms                                                 | 452 ms: 1.23x slower                                   |
| dask                     | 360 ms                                                 | 536 ms: 1.49x slower                                   |
| Geometric mean           | (ref)                                                  | 1.03x faster                                           |

Benchmark hidden because not significant (4): fannkuch, xml_etree_iterparse, bench_mp_pool, tomli_loads
Ignored benchmarks (15) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
