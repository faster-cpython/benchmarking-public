
# Results vs. 3.11.0

- fork: python
- ref: v3.12.0b2
- machine: linux-x86_64
- commit hash: e6c0efa
- commit date: 2023-06-06
- overall geometric mean: 1.02x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230606-linux-x86_64-python-v3.12.0b2-3.12.0b2-e6c0efa |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 269 ms: 1.04x slower                                       |
| docutils       | 2.63 sec                                               | 2.72 sec: 1.04x slower                                     |
| tornado_http   | 96.3 ms                                                | 99.3 ms: 1.03x slower                                      |
| Geometric mean | (ref)                                                  | 1.04x slower                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230606-linux-x86_64-python-v3.12.0b2-3.12.0b2-e6c0efa |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| nbody          | 93.1 ms                                                | 89.7 ms: 1.04x faster                                      |
| pidigits       | 198 ms                                                 | 197 ms: 1.00x faster                                       |
| float          | 77.2 ms                                                | 80.3 ms: 1.04x slower                                      |
| Geometric mean | (ref)                                                  | 1.00x faster                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230606-linux-x86_64-python-v3.12.0b2-3.12.0b2-e6c0efa |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.83 ms: 1.04x faster                                      |
| regex_dna      | 204 ms                                                 | 202 ms: 1.01x faster                                       |
| regex_v8       | 22.0 ms                                                | 22.9 ms: 1.04x slower                                      |
| regex_compile  | 138 ms                                                 | 145 ms: 1.05x slower                                       |
| Geometric mean | (ref)                                                  | 1.01x slower                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230606-linux-x86_64-python-v3.12.0b2-3.12.0b2-e6c0efa |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.69 ms: 1.30x faster                                      |
| json_loads           | 26.5 us                                                | 25.1 us: 1.05x faster                                      |
| unpickle_pure_python | 228 us                                                 | 217 us: 1.05x faster                                       |
| xml_etree_parse      | 158 ms                                                 | 156 ms: 1.01x faster                                       |
| pickle_dict          | 31.1 us                                                | 31.3 us: 1.01x slower                                      |
| tomli_loads          | 2.22 sec                                               | 2.24 sec: 1.01x slower                                     |
| pickle_pure_python   | 306 us                                                 | 314 us: 1.03x slower                                       |
| pickle               | 10.1 us                                                | 10.9 us: 1.08x slower                                      |
| unpickle             | 13.7 us                                                | 15.0 us: 1.10x slower                                      |
| xml_etree_process    | 53.9 ms                                                | 59.1 ms: 1.10x slower                                      |
| xml_etree_generate   | 76.2 ms                                                | 85.6 ms: 1.12x slower                                      |
| pickle_list          | 4.11 us                                                | 4.75 us: 1.16x slower                                      |
| Geometric mean       | (ref)                                                  | 1.01x slower                                               |

Benchmark hidden because not significant (2): unpickle_list, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230606-linux-x86_64-python-v3.12.0b2-3.12.0b2-e6c0efa |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.30 ms: 1.09x slower                                      |
| python_startup_no_site | 6.01 ms                                                | 6.76 ms: 1.13x slower                                      |
| Geometric mean         | (ref)                                                  | 1.11x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230606-linux-x86_64-python-v3.12.0b2-3.12.0b2-e6c0efa |
|-----------|:------------------------------------------------------:|:----------------------------------------------------------:|
| mako      | 10.1 ms                                                | 10.6 ms: 1.05x slower                                      |

All benchmarks:
===============

| Benchmark                | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230606-linux-x86_64-python-v3.12.0b2-3.12.0b2-e6c0efa |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| typing_runtime_protocols | 486 us                                                 | 148 us: 3.29x faster                                       |
| generators               | 73.5 ms                                                | 31.6 ms: 2.33x faster                                      |
| asyncio_tcp              | 922 ms                                                 | 511 ms: 1.80x faster                                       |
| asyncio_tcp_ssl          | 3.14 sec                                               | 1.80 sec: 1.74x faster                                     |
| json_dumps               | 12.6 ms                                                | 9.69 ms: 1.30x faster                                      |
| richards_super           | 56.8 ms                                                | 48.9 ms: 1.16x faster                                      |
| coroutines               | 25.5 ms                                                | 22.1 ms: 1.16x faster                                      |
| async_tree_none          | 526 ms                                                 | 468 ms: 1.12x faster                                       |
| async_tree_io            | 1.30 sec                                               | 1.15 sec: 1.12x faster                                     |
| async_tree_memoization   | 627 ms                                                 | 570 ms: 1.10x faster                                       |
| chaos                    | 69.2 ms                                                | 63.6 ms: 1.09x faster                                      |
| comprehensions           | 22.4 us                                                | 20.9 us: 1.07x faster                                      |
| coverage                 | 100 ms                                                 | 93.8 ms: 1.07x faster                                      |
| deltablue                | 3.67 ms                                                | 3.46 ms: 1.06x faster                                      |
| richards                 | 45.7 ms                                                | 43.1 ms: 1.06x faster                                      |
| json_loads               | 26.5 us                                                | 25.1 us: 1.05x faster                                      |
| unpickle_pure_python     | 228 us                                                 | 217 us: 1.05x faster                                       |
| async_tree_cpu_io_mixed  | 739 ms                                                 | 708 ms: 1.04x faster                                       |
| regex_effbot             | 3.99 ms                                                | 3.83 ms: 1.04x faster                                      |
| nbody                    | 93.1 ms                                                | 89.7 ms: 1.04x faster                                      |
| json                     | 4.94 ms                                                | 4.76 ms: 1.04x faster                                      |
| sqlglot_parse            | 1.40 ms                                                | 1.35 ms: 1.04x faster                                      |
| go                       | 140 ms                                                 | 136 ms: 1.03x faster                                       |
| hexiom                   | 6.37 ms                                                | 6.19 ms: 1.03x faster                                      |
| mdp                      | 2.62 sec                                               | 2.55 sec: 1.03x faster                                     |
| sqlglot_transpile        | 1.70 ms                                                | 1.67 ms: 1.02x faster                                      |
| xml_etree_parse          | 158 ms                                                 | 156 ms: 1.01x faster                                       |
| nqueens                  | 83.4 ms                                                | 82.6 ms: 1.01x faster                                      |
| regex_dna                | 204 ms                                                 | 202 ms: 1.01x faster                                       |
| pidigits                 | 198 ms                                                 | 197 ms: 1.00x faster                                       |
| pickle_dict              | 31.1 us                                                | 31.3 us: 1.01x slower                                      |
| sqlglot_normalize        | 108 ms                                                 | 109 ms: 1.01x slower                                       |
| tomli_loads              | 2.22 sec                                               | 2.24 sec: 1.01x slower                                     |
| bench_thread_pool        | 819 us                                                 | 829 us: 1.01x slower                                       |
| logging_silent           | 101 ns                                                 | 103 ns: 1.01x slower                                       |
| scimark_sor              | 118 ms                                                 | 120 ms: 1.02x slower                                       |
| sqlglot_optimize         | 53.1 ms                                                | 54.2 ms: 1.02x slower                                      |
| create_gc_cycles         | 1.49 ms                                                | 1.52 ms: 1.02x slower                                      |
| fannkuch                 | 388 ms                                                 | 398 ms: 1.03x slower                                       |
| pickle_pure_python       | 306 us                                                 | 314 us: 1.03x slower                                       |
| deepcopy_memo            | 37.0 us                                                | 38.1 us: 1.03x slower                                      |
| scimark_lu               | 110 ms                                                 | 113 ms: 1.03x slower                                       |
| tornado_http             | 96.3 ms                                                | 99.3 ms: 1.03x slower                                      |
| pathlib                  | 18.2 ms                                                | 18.8 ms: 1.03x slower                                      |
| logging_simple           | 6.03 us                                                | 6.24 us: 1.03x slower                                      |
| pprint_pformat           | 1.46 sec                                               | 1.51 sec: 1.04x slower                                     |
| docutils                 | 2.63 sec                                               | 2.72 sec: 1.04x slower                                     |
| 2to3                     | 259 ms                                                 | 269 ms: 1.04x slower                                       |
| telco                    | 6.58 ms                                                | 6.83 ms: 1.04x slower                                      |
| float                    | 77.2 ms                                                | 80.3 ms: 1.04x slower                                      |
| regex_v8                 | 22.0 ms                                                | 22.9 ms: 1.04x slower                                      |
| logging_format           | 6.68 us                                                | 6.96 us: 1.04x slower                                      |
| spectral_norm            | 100 ms                                                 | 104 ms: 1.04x slower                                       |
| crypto_pyaes             | 74.7 ms                                                | 78.0 ms: 1.04x slower                                      |
| regex_compile            | 138 ms                                                 | 145 ms: 1.05x slower                                       |
| pprint_safe_repr         | 701 ms                                                 | 735 ms: 1.05x slower                                       |
| scimark_monte_carlo      | 68.1 ms                                                | 71.3 ms: 1.05x slower                                      |
| mako                     | 10.1 ms                                                | 10.6 ms: 1.05x slower                                      |
| sqlalchemy_declarative   | 138 ms                                                 | 145 ms: 1.05x slower                                       |
| deepcopy                 | 342 us                                                 | 359 us: 1.05x slower                                       |
| sqlalchemy_imperative    | 17.9 ms                                                | 18.8 ms: 1.05x slower                                      |
| gc_traversal             | 4.02 ms                                                | 4.25 ms: 1.06x slower                                      |
| pyflate                  | 418 ms                                                 | 448 ms: 1.07x slower                                       |
| dulwich_log              | 63.7 ms                                                | 68.4 ms: 1.07x slower                                      |
| sqlite_synth             | 2.52 us                                                | 2.73 us: 1.08x slower                                      |
| pickle                   | 10.1 us                                                | 10.9 us: 1.08x slower                                      |
| unpack_sequence          | 43.1 ns                                                | 46.7 ns: 1.08x slower                                      |
| deepcopy_reduce          | 2.94 us                                                | 3.19 us: 1.09x slower                                      |
| scimark_sparse_mat_mult  | 4.50 ms                                                | 4.89 ms: 1.09x slower                                      |
| scimark_fft              | 328 ms                                                 | 358 ms: 1.09x slower                                       |
| python_startup           | 8.52 ms                                                | 9.30 ms: 1.09x slower                                      |
| unpickle                 | 13.7 us                                                | 15.0 us: 1.10x slower                                      |
| xml_etree_process        | 53.9 ms                                                | 59.1 ms: 1.10x slower                                      |
| xml_etree_generate       | 76.2 ms                                                | 85.6 ms: 1.12x slower                                      |
| python_startup_no_site   | 6.01 ms                                                | 6.76 ms: 1.13x slower                                      |
| pickle_list              | 4.11 us                                                | 4.75 us: 1.16x slower                                      |
| async_generators         | 368 ms                                                 | 450 ms: 1.22x slower                                       |
| dask                     | 360 ms                                                 | 536 ms: 1.49x slower                                       |
| Geometric mean           | (ref)                                                  | 1.02x faster                                               |

Benchmark hidden because not significant (7): pycparser, meteor_contest, raytrace, bench_mp_pool, unpickle_list, xml_etree_iterparse, mypy2
Ignored benchmarks (15) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
