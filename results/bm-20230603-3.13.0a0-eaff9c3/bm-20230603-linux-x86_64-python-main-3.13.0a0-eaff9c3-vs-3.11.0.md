
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: eaff9c3
- commit date: 2023-06-03
- overall geometric mean: 1.03x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230603-linux-x86_64-python-main-3.13.0a0-eaff9c3 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| docutils       | 2.63 sec                                               | 2.71 sec: 1.03x slower                                |
| tornado_http   | 96.3 ms                                                | 102 ms: 1.06x slower                                  |
| Geometric mean | (ref)                                                  | 1.05x slower                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230603-linux-x86_64-python-main-3.13.0a0-eaff9c3 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| nbody          | 93.1 ms                                                | 89.0 ms: 1.05x faster                                 |
| pidigits       | 198 ms                                                 | 192 ms: 1.03x faster                                  |
| float          | 77.2 ms                                                | 81.4 ms: 1.05x slower                                 |
| Geometric mean | (ref)                                                  | 1.01x faster                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230603-linux-x86_64-python-main-3.13.0a0-eaff9c3 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.56 ms: 1.12x faster                                 |
| regex_v8       | 22.0 ms                                                | 21.9 ms: 1.01x faster                                 |
| regex_dna      | 204 ms                                                 | 205 ms: 1.01x slower                                  |
| regex_compile  | 138 ms                                                 | 145 ms: 1.05x slower                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230603-linux-x86_64-python-main-3.13.0a0-eaff9c3 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.78 ms: 1.29x faster                                 |
| json_loads           | 26.5 us                                                | 25.2 us: 1.05x faster                                 |
| unpickle_pure_python | 228 us                                                 | 218 us: 1.04x faster                                  |
| xml_etree_parse      | 158 ms                                                 | 153 ms: 1.04x faster                                  |
| pickle_dict          | 31.1 us                                                | 31.6 us: 1.01x slower                                 |
| unpickle_list        | 4.91 us                                                | 4.99 us: 1.02x slower                                 |
| pickle_pure_python   | 306 us                                                 | 312 us: 1.02x slower                                  |
| pickle               | 10.1 us                                                | 10.6 us: 1.05x slower                                 |
| xml_etree_process    | 53.9 ms                                                | 59.0 ms: 1.09x slower                                 |
| xml_etree_generate   | 76.2 ms                                                | 84.5 ms: 1.11x slower                                 |
| unpickle             | 13.7 us                                                | 15.2 us: 1.11x slower                                 |
| pickle_list          | 4.11 us                                                | 4.66 us: 1.13x slower                                 |
| Geometric mean       | (ref)                                                  | 1.01x slower                                          |

Benchmark hidden because not significant (2): xml_etree_iterparse, tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230603-linux-x86_64-python-main-3.13.0a0-eaff9c3 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.30 ms: 1.09x slower                                 |
| python_startup_no_site | 6.01 ms                                                | 6.77 ms: 1.13x slower                                 |
| Geometric mean         | (ref)                                                  | 1.11x slower                                          |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230603-linux-x86_64-python-main-3.13.0a0-eaff9c3 |
|-----------|:------------------------------------------------------:|:-----------------------------------------------------:|
| mako      | 10.1 ms                                                | 10.8 ms: 1.07x slower                                 |

All benchmarks:
===============

| Benchmark                | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230603-linux-x86_64-python-main-3.13.0a0-eaff9c3 |
|--------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| typing_runtime_protocols | 486 us                                                 | 143 us: 3.39x faster                                  |
| generators               | 73.5 ms                                                | 30.5 ms: 2.40x faster                                 |
| asyncio_tcp              | 922 ms                                                 | 511 ms: 1.80x faster                                  |
| asyncio_tcp_ssl          | 3.14 sec                                               | 1.79 sec: 1.75x faster                                |
| json_dumps               | 12.6 ms                                                | 9.78 ms: 1.29x faster                                 |
| mypy2                    | 420 ms                                                 | 345 ms: 1.22x faster                                  |
| richards_super           | 56.8 ms                                                | 50.5 ms: 1.12x faster                                 |
| regex_effbot             | 3.99 ms                                                | 3.56 ms: 1.12x faster                                 |
| comprehensions           | 22.4 us                                                | 20.5 us: 1.09x faster                                 |
| coroutines               | 25.5 ms                                                | 23.7 ms: 1.08x faster                                 |
| chaos                    | 69.2 ms                                                | 64.5 ms: 1.07x faster                                 |
| async_tree_io            | 1.30 sec                                               | 1.21 sec: 1.07x faster                                |
| async_tree_none          | 526 ms                                                 | 496 ms: 1.06x faster                                  |
| async_tree_memoization   | 627 ms                                                 | 595 ms: 1.05x faster                                  |
| deltablue                | 3.67 ms                                                | 3.49 ms: 1.05x faster                                 |
| json_loads               | 26.5 us                                                | 25.2 us: 1.05x faster                                 |
| nbody                    | 93.1 ms                                                | 89.0 ms: 1.05x faster                                 |
| unpickle_pure_python     | 228 us                                                 | 218 us: 1.04x faster                                  |
| sqlglot_parse            | 1.40 ms                                                | 1.34 ms: 1.04x faster                                 |
| coverage                 | 100 ms                                                 | 96.3 ms: 1.04x faster                                 |
| xml_etree_parse          | 158 ms                                                 | 153 ms: 1.04x faster                                  |
| json                     | 4.94 ms                                                | 4.77 ms: 1.04x faster                                 |
| pidigits                 | 198 ms                                                 | 192 ms: 1.03x faster                                  |
| go                       | 140 ms                                                 | 136 ms: 1.03x faster                                  |
| gc_traversal             | 4.02 ms                                                | 3.91 ms: 1.03x faster                                 |
| richards                 | 45.7 ms                                                | 44.5 ms: 1.03x faster                                 |
| mdp                      | 2.62 sec                                               | 2.54 sec: 1.03x faster                                |
| sqlglot_transpile        | 1.70 ms                                                | 1.66 ms: 1.03x faster                                 |
| hexiom                   | 6.37 ms                                                | 6.21 ms: 1.03x faster                                 |
| nqueens                  | 83.4 ms                                                | 81.6 ms: 1.02x faster                                 |
| meteor_contest           | 107 ms                                                 | 105 ms: 1.01x faster                                  |
| regex_v8                 | 22.0 ms                                                | 21.9 ms: 1.01x faster                                 |
| fannkuch                 | 388 ms                                                 | 386 ms: 1.00x faster                                  |
| regex_dna                | 204 ms                                                 | 205 ms: 1.01x slower                                  |
| sqlglot_normalize        | 108 ms                                                 | 109 ms: 1.01x slower                                  |
| scimark_sor              | 118 ms                                                 | 119 ms: 1.01x slower                                  |
| pickle_dict              | 31.1 us                                                | 31.6 us: 1.01x slower                                 |
| bench_thread_pool        | 819 us                                                 | 831 us: 1.01x slower                                  |
| create_gc_cycles         | 1.49 ms                                                | 1.51 ms: 1.02x slower                                 |
| unpickle_list            | 4.91 us                                                | 4.99 us: 1.02x slower                                 |
| pathlib                  | 18.2 ms                                                | 18.5 ms: 1.02x slower                                 |
| sqlglot_optimize         | 53.1 ms                                                | 54.0 ms: 1.02x slower                                 |
| logging_silent           | 101 ns                                                 | 103 ns: 1.02x slower                                  |
| pickle_pure_python       | 306 us                                                 | 312 us: 1.02x slower                                  |
| unpack_sequence          | 43.1 ns                                                | 44.2 ns: 1.03x slower                                 |
| pprint_pformat           | 1.46 sec                                               | 1.50 sec: 1.03x slower                                |
| deepcopy_memo            | 37.0 us                                                | 38.0 us: 1.03x slower                                 |
| docutils                 | 2.63 sec                                               | 2.71 sec: 1.03x slower                                |
| scimark_lu               | 110 ms                                                 | 114 ms: 1.03x slower                                  |
| deepcopy                 | 342 us                                                 | 354 us: 1.04x slower                                  |
| telco                    | 6.58 ms                                                | 6.82 ms: 1.04x slower                                 |
| pprint_safe_repr         | 701 ms                                                 | 733 ms: 1.04x slower                                  |
| regex_compile            | 138 ms                                                 | 145 ms: 1.05x slower                                  |
| pickle                   | 10.1 us                                                | 10.6 us: 1.05x slower                                 |
| scimark_monte_carlo      | 68.1 ms                                                | 71.7 ms: 1.05x slower                                 |
| float                    | 77.2 ms                                                | 81.4 ms: 1.05x slower                                 |
| crypto_pyaes             | 74.7 ms                                                | 78.7 ms: 1.05x slower                                 |
| logging_simple           | 6.03 us                                                | 6.37 us: 1.06x slower                                 |
| logging_format           | 6.68 us                                                | 7.05 us: 1.06x slower                                 |
| pyflate                  | 418 ms                                                 | 442 ms: 1.06x slower                                  |
| tornado_http             | 96.3 ms                                                | 102 ms: 1.06x slower                                  |
| deepcopy_reduce          | 2.94 us                                                | 3.12 us: 1.06x slower                                 |
| dulwich_log              | 63.7 ms                                                | 67.7 ms: 1.06x slower                                 |
| spectral_norm            | 100 ms                                                 | 107 ms: 1.07x slower                                  |
| mako                     | 10.1 ms                                                | 10.8 ms: 1.07x slower                                 |
| sqlite_synth             | 2.52 us                                                | 2.72 us: 1.08x slower                                 |
| scimark_fft              | 328 ms                                                 | 358 ms: 1.09x slower                                  |
| python_startup           | 8.52 ms                                                | 9.30 ms: 1.09x slower                                 |
| xml_etree_process        | 53.9 ms                                                | 59.0 ms: 1.09x slower                                 |
| scimark_sparse_mat_mult  | 4.50 ms                                                | 4.95 ms: 1.10x slower                                 |
| xml_etree_generate       | 76.2 ms                                                | 84.5 ms: 1.11x slower                                 |
| unpickle                 | 13.7 us                                                | 15.2 us: 1.11x slower                                 |
| python_startup_no_site   | 6.01 ms                                                | 6.77 ms: 1.13x slower                                 |
| pickle_list              | 4.11 us                                                | 4.66 us: 1.13x slower                                 |
| async_generators         | 368 ms                                                 | 450 ms: 1.22x slower                                  |
| dask                     | 360 ms                                                 | 538 ms: 1.49x slower                                  |
| Geometric mean           | (ref)                                                  | 1.03x faster                                          |

Benchmark hidden because not significant (6): async_tree_cpu_io_mixed, xml_etree_iterparse, tomli_loads, bench_mp_pool, raytrace, pycparser
Ignored benchmarks (18) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
