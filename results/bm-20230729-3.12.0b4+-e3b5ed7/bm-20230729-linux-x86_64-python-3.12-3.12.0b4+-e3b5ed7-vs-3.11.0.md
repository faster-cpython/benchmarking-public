
# Results vs. 3.11.0

- fork: python
- ref: 3.12
- machine: linux-x86_64
- commit hash: e3b5ed7
- commit date: 2023-07-29
- overall geometric mean: 1.03x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230729-linux-x86_64-python-3.12-3.12.0b4+-e3b5ed7 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 268 ms: 1.03x slower                                   |
| docutils       | 2.63 sec                                               | 2.72 sec: 1.03x slower                                 |
| tornado_http   | 96.3 ms                                                | 102 ms: 1.06x slower                                   |
| Geometric mean | (ref)                                                  | 1.04x slower                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230729-linux-x86_64-python-3.12-3.12.0b4+-e3b5ed7 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 93.1 ms                                                | 88.9 ms: 1.05x faster                                  |
| pidigits       | 198 ms                                                 | 196 ms: 1.01x faster                                   |
| float          | 77.2 ms                                                | 79.7 ms: 1.03x slower                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230729-linux-x86_64-python-3.12-3.12.0b4+-e3b5ed7 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.54 ms: 1.13x faster                                  |
| regex_dna      | 204 ms                                                 | 206 ms: 1.01x slower                                   |
| regex_v8       | 22.0 ms                                                | 23.0 ms: 1.05x slower                                  |
| regex_compile  | 138 ms                                                 | 145 ms: 1.05x slower                                   |
| Geometric mean | (ref)                                                  | 1.01x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230729-linux-x86_64-python-3.12-3.12.0b4+-e3b5ed7 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.98 ms: 1.26x faster                                  |
| unpickle_pure_python | 228 us                                                 | 217 us: 1.05x faster                                   |
| json_loads           | 26.5 us                                                | 25.6 us: 1.03x faster                                  |
| xml_etree_parse      | 158 ms                                                 | 155 ms: 1.03x faster                                   |
| tomli_loads          | 2.22 sec                                               | 2.21 sec: 1.01x faster                                 |
| xml_etree_iterparse  | 104 ms                                                 | 103 ms: 1.01x faster                                   |
| pickle_dict          | 31.1 us                                                | 31.3 us: 1.01x slower                                  |
| unpickle_list        | 4.91 us                                                | 4.94 us: 1.01x slower                                  |
| pickle_pure_python   | 306 us                                                 | 310 us: 1.01x slower                                   |
| pickle               | 10.1 us                                                | 10.8 us: 1.07x slower                                  |
| unpickle             | 13.7 us                                                | 14.8 us: 1.08x slower                                  |
| xml_etree_process    | 53.9 ms                                                | 59.2 ms: 1.10x slower                                  |
| xml_etree_generate   | 76.2 ms                                                | 84.7 ms: 1.11x slower                                  |
| pickle_list          | 4.11 us                                                | 4.71 us: 1.14x slower                                  |
| Geometric mean       | (ref)                                                  | 1.01x slower                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230729-linux-x86_64-python-3.12-3.12.0b4+-e3b5ed7 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.29 ms: 1.09x slower                                  |
| python_startup_no_site | 6.01 ms                                                | 6.75 ms: 1.12x slower                                  |
| Geometric mean         | (ref)                                                  | 1.11x slower                                           |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230729-linux-x86_64-python-3.12-3.12.0b4+-e3b5ed7 |
|-----------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako      | 10.1 ms                                                | 10.7 ms: 1.06x slower                                  |

All benchmarks:
===============

| Benchmark                | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230729-linux-x86_64-python-3.12-3.12.0b4+-e3b5ed7 |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| typing_runtime_protocols | 486 us                                                 | 148 us: 3.29x faster                                   |
| generators               | 73.5 ms                                                | 30.2 ms: 2.43x faster                                  |
| asyncio_tcp              | 922 ms                                                 | 522 ms: 1.76x faster                                   |
| asyncio_tcp_ssl          | 3.14 sec                                               | 1.79 sec: 1.75x faster                                 |
| json_dumps               | 12.6 ms                                                | 9.98 ms: 1.26x faster                                  |
| mypy2                    | 420 ms                                                 | 345 ms: 1.22x faster                                   |
| richards_super           | 56.8 ms                                                | 49.6 ms: 1.14x faster                                  |
| coroutines               | 25.5 ms                                                | 22.5 ms: 1.13x faster                                  |
| regex_effbot             | 3.99 ms                                                | 3.54 ms: 1.13x faster                                  |
| async_tree_io            | 1.30 sec                                               | 1.17 sec: 1.11x faster                                 |
| async_tree_none          | 526 ms                                                 | 476 ms: 1.11x faster                                   |
| async_tree_memoization   | 627 ms                                                 | 579 ms: 1.08x faster                                   |
| comprehensions           | 22.4 us                                                | 20.8 us: 1.08x faster                                  |
| chaos                    | 69.2 ms                                                | 64.2 ms: 1.08x faster                                  |
| coverage                 | 100 ms                                                 | 93.8 ms: 1.07x faster                                  |
| unpickle_pure_python     | 228 us                                                 | 217 us: 1.05x faster                                   |
| nbody                    | 93.1 ms                                                | 88.9 ms: 1.05x faster                                  |
| gc_traversal             | 4.02 ms                                                | 3.85 ms: 1.05x faster                                  |
| deltablue                | 3.67 ms                                                | 3.51 ms: 1.05x faster                                  |
| sqlglot_parse            | 1.40 ms                                                | 1.34 ms: 1.04x faster                                  |
| richards                 | 45.7 ms                                                | 43.8 ms: 1.04x faster                                  |
| hexiom                   | 6.37 ms                                                | 6.15 ms: 1.04x faster                                  |
| async_tree_cpu_io_mixed  | 739 ms                                                 | 714 ms: 1.04x faster                                   |
| json_loads               | 26.5 us                                                | 25.6 us: 1.03x faster                                  |
| go                       | 140 ms                                                 | 135 ms: 1.03x faster                                   |
| mdp                      | 2.62 sec                                               | 2.54 sec: 1.03x faster                                 |
| pycparser                | 1.18 sec                                               | 1.15 sec: 1.03x faster                                 |
| xml_etree_parse          | 158 ms                                                 | 155 ms: 1.03x faster                                   |
| sqlglot_transpile        | 1.70 ms                                                | 1.67 ms: 1.02x faster                                  |
| meteor_contest           | 107 ms                                                 | 104 ms: 1.02x faster                                   |
| pathlib                  | 18.2 ms                                                | 18.1 ms: 1.01x faster                                  |
| pidigits                 | 198 ms                                                 | 196 ms: 1.01x faster                                   |
| raytrace                 | 297 ms                                                 | 295 ms: 1.01x faster                                   |
| tomli_loads              | 2.22 sec                                               | 2.21 sec: 1.01x faster                                 |
| nqueens                  | 83.4 ms                                                | 82.9 ms: 1.01x faster                                  |
| xml_etree_iterparse      | 104 ms                                                 | 103 ms: 1.01x faster                                   |
| logging_silent           | 101 ns                                                 | 101 ns: 1.01x faster                                   |
| pickle_dict              | 31.1 us                                                | 31.3 us: 1.01x slower                                  |
| unpickle_list            | 4.91 us                                                | 4.94 us: 1.01x slower                                  |
| sqlglot_normalize        | 108 ms                                                 | 109 ms: 1.01x slower                                   |
| regex_dna                | 204 ms                                                 | 206 ms: 1.01x slower                                   |
| pickle_pure_python       | 306 us                                                 | 310 us: 1.01x slower                                   |
| bench_thread_pool        | 819 us                                                 | 830 us: 1.01x slower                                   |
| sqlglot_optimize         | 53.1 ms                                                | 54.0 ms: 1.02x slower                                  |
| create_gc_cycles         | 1.49 ms                                                | 1.51 ms: 1.02x slower                                  |
| telco                    | 6.58 ms                                                | 6.73 ms: 1.02x slower                                  |
| deepcopy_memo            | 37.0 us                                                | 38.0 us: 1.03x slower                                  |
| logging_simple           | 6.03 us                                                | 6.20 us: 1.03x slower                                  |
| float                    | 77.2 ms                                                | 79.7 ms: 1.03x slower                                  |
| 2to3                     | 259 ms                                                 | 268 ms: 1.03x slower                                   |
| docutils                 | 2.63 sec                                               | 2.72 sec: 1.03x slower                                 |
| logging_format           | 6.68 us                                                | 6.92 us: 1.04x slower                                  |
| scimark_sor              | 118 ms                                                 | 122 ms: 1.04x slower                                   |
| deepcopy                 | 342 us                                                 | 356 us: 1.04x slower                                   |
| pprint_pformat           | 1.46 sec                                               | 1.52 sec: 1.04x slower                                 |
| sqlalchemy_imperative    | 17.9 ms                                                | 18.7 ms: 1.04x slower                                  |
| regex_v8                 | 22.0 ms                                                | 23.0 ms: 1.05x slower                                  |
| regex_compile            | 138 ms                                                 | 145 ms: 1.05x slower                                   |
| scimark_monte_carlo      | 68.1 ms                                                | 71.3 ms: 1.05x slower                                  |
| sqlalchemy_declarative   | 138 ms                                                 | 146 ms: 1.05x slower                                   |
| crypto_pyaes             | 74.7 ms                                                | 78.9 ms: 1.06x slower                                  |
| scimark_sparse_mat_mult  | 4.50 ms                                                | 4.76 ms: 1.06x slower                                  |
| tornado_http             | 96.3 ms                                                | 102 ms: 1.06x slower                                   |
| mako                     | 10.1 ms                                                | 10.7 ms: 1.06x slower                                  |
| deepcopy_reduce          | 2.94 us                                                | 3.13 us: 1.07x slower                                  |
| pprint_safe_repr         | 701 ms                                                 | 747 ms: 1.07x slower                                   |
| scimark_fft              | 328 ms                                                 | 351 ms: 1.07x slower                                   |
| pyflate                  | 418 ms                                                 | 447 ms: 1.07x slower                                   |
| pickle                   | 10.1 us                                                | 10.8 us: 1.07x slower                                  |
| spectral_norm            | 100 ms                                                 | 107 ms: 1.07x slower                                   |
| dulwich_log              | 63.7 ms                                                | 68.4 ms: 1.07x slower                                  |
| unpickle                 | 13.7 us                                                | 14.8 us: 1.08x slower                                  |
| sqlite_synth             | 2.52 us                                                | 2.74 us: 1.09x slower                                  |
| python_startup           | 8.52 ms                                                | 9.29 ms: 1.09x slower                                  |
| xml_etree_process        | 53.9 ms                                                | 59.2 ms: 1.10x slower                                  |
| xml_etree_generate       | 76.2 ms                                                | 84.7 ms: 1.11x slower                                  |
| python_startup_no_site   | 6.01 ms                                                | 6.75 ms: 1.12x slower                                  |
| unpack_sequence          | 43.1 ns                                                | 48.8 ns: 1.13x slower                                  |
| pickle_list              | 4.11 us                                                | 4.71 us: 1.14x slower                                  |
| async_generators         | 368 ms                                                 | 444 ms: 1.21x slower                                   |
| dask                     | 360 ms                                                 | 538 ms: 1.50x slower                                   |
| Geometric mean           | (ref)                                                  | 1.03x faster                                           |

Benchmark hidden because not significant (4): json, bench_mp_pool, fannkuch, scimark_lu
Ignored benchmarks (15) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
