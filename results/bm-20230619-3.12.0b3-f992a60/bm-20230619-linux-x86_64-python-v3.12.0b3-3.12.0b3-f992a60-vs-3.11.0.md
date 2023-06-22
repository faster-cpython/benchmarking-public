
# Results vs. 3.11.0

- fork: python
- ref: v3.12.0b3
- machine: linux-x86_64
- commit hash: f992a60
- commit date: 2023-06-19
- overall geometric mean: 1.03x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230619-linux-x86_64-python-v3.12.0b3-3.12.0b3-f992a60 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 267 ms: 1.03x slower                                       |
| docutils       | 2.63 sec                                               | 2.72 sec: 1.04x slower                                     |
| tornado_http   | 96.3 ms                                                | 99.3 ms: 1.03x slower                                      |
| Geometric mean | (ref)                                                  | 1.03x slower                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230619-linux-x86_64-python-v3.12.0b3-3.12.0b3-f992a60 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pidigits       | 198 ms                                                 | 197 ms: 1.01x faster                                       |
| nbody          | 93.1 ms                                                | 94.3 ms: 1.01x slower                                      |
| float          | 77.2 ms                                                | 80.4 ms: 1.04x slower                                      |
| Geometric mean | (ref)                                                  | 1.02x slower                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230619-linux-x86_64-python-v3.12.0b3-3.12.0b3-f992a60 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.56 ms: 1.12x faster                                      |
| regex_dna      | 204 ms                                                 | 200 ms: 1.02x faster                                       |
| regex_v8       | 22.0 ms                                                | 22.9 ms: 1.04x slower                                      |
| regex_compile  | 138 ms                                                 | 144 ms: 1.05x slower                                       |
| Geometric mean | (ref)                                                  | 1.01x faster                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230619-linux-x86_64-python-v3.12.0b3-3.12.0b3-f992a60 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.79 ms: 1.28x faster                                      |
| unpickle_pure_python | 228 us                                                 | 215 us: 1.06x faster                                       |
| json_loads           | 26.5 us                                                | 25.0 us: 1.06x faster                                      |
| xml_etree_parse      | 158 ms                                                 | 152 ms: 1.04x faster                                       |
| tomli_loads          | 2.22 sec                                               | 2.17 sec: 1.02x faster                                     |
| xml_etree_iterparse  | 104 ms                                                 | 103 ms: 1.01x faster                                       |
| unpickle_list        | 4.91 us                                                | 4.96 us: 1.01x slower                                      |
| pickle_pure_python   | 306 us                                                 | 312 us: 1.02x slower                                       |
| pickle_dict          | 31.1 us                                                | 31.8 us: 1.02x slower                                      |
| pickle               | 10.1 us                                                | 11.0 us: 1.09x slower                                      |
| unpickle             | 13.7 us                                                | 14.9 us: 1.09x slower                                      |
| pickle_list          | 4.11 us                                                | 4.49 us: 1.09x slower                                      |
| xml_etree_process    | 53.9 ms                                                | 59.2 ms: 1.10x slower                                      |
| xml_etree_generate   | 76.2 ms                                                | 85.4 ms: 1.12x slower                                      |
| Geometric mean       | (ref)                                                  | 1.01x slower                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230619-linux-x86_64-python-v3.12.0b3-3.12.0b3-f992a60 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.28 ms: 1.09x slower                                      |
| python_startup_no_site | 6.01 ms                                                | 6.74 ms: 1.12x slower                                      |
| Geometric mean         | (ref)                                                  | 1.11x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230619-linux-x86_64-python-v3.12.0b3-3.12.0b3-f992a60 |
|-----------|:------------------------------------------------------:|:----------------------------------------------------------:|
| mako      | 10.1 ms                                                | 10.6 ms: 1.05x slower                                      |

All benchmarks:
===============

| Benchmark                | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230619-linux-x86_64-python-v3.12.0b3-3.12.0b3-f992a60 |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| typing_runtime_protocols | 486 us                                                 | 146 us: 3.33x faster                                       |
| generators               | 73.5 ms                                                | 30.3 ms: 2.42x faster                                      |
| asyncio_tcp              | 922 ms                                                 | 513 ms: 1.80x faster                                       |
| asyncio_tcp_ssl          | 3.14 sec                                               | 1.79 sec: 1.75x faster                                     |
| json_dumps               | 12.6 ms                                                | 9.79 ms: 1.28x faster                                      |
| richards_super           | 56.8 ms                                                | 49.2 ms: 1.15x faster                                      |
| coroutines               | 25.5 ms                                                | 22.2 ms: 1.15x faster                                      |
| async_tree_none          | 526 ms                                                 | 469 ms: 1.12x faster                                       |
| regex_effbot             | 3.99 ms                                                | 3.56 ms: 1.12x faster                                      |
| async_tree_io            | 1.30 sec                                               | 1.16 sec: 1.12x faster                                     |
| async_tree_memoization   | 627 ms                                                 | 575 ms: 1.09x faster                                       |
| chaos                    | 69.2 ms                                                | 63.8 ms: 1.08x faster                                      |
| comprehensions           | 22.4 us                                                | 20.7 us: 1.08x faster                                      |
| unpickle_pure_python     | 228 us                                                 | 215 us: 1.06x faster                                       |
| json_loads               | 26.5 us                                                | 25.0 us: 1.06x faster                                      |
| sqlglot_parse            | 1.40 ms                                                | 1.33 ms: 1.06x faster                                      |
| coverage                 | 100 ms                                                 | 95.0 ms: 1.05x faster                                      |
| deltablue                | 3.67 ms                                                | 3.50 ms: 1.05x faster                                      |
| richards                 | 45.7 ms                                                | 43.8 ms: 1.05x faster                                      |
| xml_etree_parse          | 158 ms                                                 | 152 ms: 1.04x faster                                       |
| json                     | 4.94 ms                                                | 4.74 ms: 1.04x faster                                      |
| hexiom                   | 6.37 ms                                                | 6.13 ms: 1.04x faster                                      |
| sqlglot_transpile        | 1.70 ms                                                | 1.64 ms: 1.04x faster                                      |
| async_tree_cpu_io_mixed  | 739 ms                                                 | 713 ms: 1.04x faster                                       |
| nqueens                  | 83.4 ms                                                | 80.5 ms: 1.04x faster                                      |
| go                       | 140 ms                                                 | 137 ms: 1.02x faster                                       |
| tomli_loads              | 2.22 sec                                               | 2.17 sec: 1.02x faster                                     |
| regex_dna                | 204 ms                                                 | 200 ms: 1.02x faster                                       |
| pycparser                | 1.18 sec                                               | 1.16 sec: 1.02x faster                                     |
| logging_silent           | 101 ns                                                 | 99.7 ns: 1.01x faster                                      |
| meteor_contest           | 107 ms                                                 | 106 ms: 1.01x faster                                       |
| xml_etree_iterparse      | 104 ms                                                 | 103 ms: 1.01x faster                                       |
| pidigits                 | 198 ms                                                 | 197 ms: 1.01x faster                                       |
| raytrace                 | 297 ms                                                 | 298 ms: 1.00x slower                                       |
| sqlglot_normalize        | 108 ms                                                 | 109 ms: 1.01x slower                                       |
| sqlglot_optimize         | 53.1 ms                                                | 53.5 ms: 1.01x slower                                      |
| create_gc_cycles         | 1.49 ms                                                | 1.50 ms: 1.01x slower                                      |
| bench_thread_pool        | 819 us                                                 | 827 us: 1.01x slower                                       |
| mdp                      | 2.62 sec                                               | 2.64 sec: 1.01x slower                                     |
| unpickle_list            | 4.91 us                                                | 4.96 us: 1.01x slower                                      |
| gc_traversal             | 4.02 ms                                                | 4.07 ms: 1.01x slower                                      |
| nbody                    | 93.1 ms                                                | 94.3 ms: 1.01x slower                                      |
| pickle_pure_python       | 306 us                                                 | 312 us: 1.02x slower                                       |
| pickle_dict              | 31.1 us                                                | 31.8 us: 1.02x slower                                      |
| scimark_lu               | 110 ms                                                 | 112 ms: 1.02x slower                                       |
| sqlalchemy_imperative    | 17.9 ms                                                | 18.4 ms: 1.03x slower                                      |
| pprint_pformat           | 1.46 sec                                               | 1.50 sec: 1.03x slower                                     |
| tornado_http             | 96.3 ms                                                | 99.3 ms: 1.03x slower                                      |
| 2to3                     | 259 ms                                                 | 267 ms: 1.03x slower                                       |
| deepcopy_memo            | 37.0 us                                                | 38.3 us: 1.03x slower                                      |
| docutils                 | 2.63 sec                                               | 2.72 sec: 1.04x slower                                     |
| logging_simple           | 6.03 us                                                | 6.25 us: 1.04x slower                                      |
| telco                    | 6.58 ms                                                | 6.82 ms: 1.04x slower                                      |
| regex_v8                 | 22.0 ms                                                | 22.9 ms: 1.04x slower                                      |
| float                    | 77.2 ms                                                | 80.4 ms: 1.04x slower                                      |
| regex_compile            | 138 ms                                                 | 144 ms: 1.05x slower                                       |
| sqlalchemy_declarative   | 138 ms                                                 | 145 ms: 1.05x slower                                       |
| logging_format           | 6.68 us                                                | 6.99 us: 1.05x slower                                      |
| crypto_pyaes             | 74.7 ms                                                | 78.1 ms: 1.05x slower                                      |
| pprint_safe_repr         | 701 ms                                                 | 734 ms: 1.05x slower                                       |
| scimark_monte_carlo      | 68.1 ms                                                | 71.2 ms: 1.05x slower                                      |
| scimark_sor              | 118 ms                                                 | 124 ms: 1.05x slower                                       |
| deepcopy                 | 342 us                                                 | 359 us: 1.05x slower                                       |
| mako                     | 10.1 ms                                                | 10.6 ms: 1.05x slower                                      |
| spectral_norm            | 100 ms                                                 | 106 ms: 1.06x slower                                       |
| deepcopy_reduce          | 2.94 us                                                | 3.12 us: 1.06x slower                                      |
| dulwich_log              | 63.7 ms                                                | 67.9 ms: 1.07x slower                                      |
| pyflate                  | 418 ms                                                 | 453 ms: 1.08x slower                                       |
| scimark_sparse_mat_mult  | 4.50 ms                                                | 4.88 ms: 1.08x slower                                      |
| pickle                   | 10.1 us                                                | 11.0 us: 1.09x slower                                      |
| python_startup           | 8.52 ms                                                | 9.28 ms: 1.09x slower                                      |
| unpickle                 | 13.7 us                                                | 14.9 us: 1.09x slower                                      |
| scimark_fft              | 328 ms                                                 | 358 ms: 1.09x slower                                       |
| sqlite_synth             | 2.52 us                                                | 2.75 us: 1.09x slower                                      |
| pickle_list              | 4.11 us                                                | 4.49 us: 1.09x slower                                      |
| xml_etree_process        | 53.9 ms                                                | 59.2 ms: 1.10x slower                                      |
| unpack_sequence          | 43.1 ns                                                | 47.4 ns: 1.10x slower                                      |
| xml_etree_generate       | 76.2 ms                                                | 85.4 ms: 1.12x slower                                      |
| python_startup_no_site   | 6.01 ms                                                | 6.74 ms: 1.12x slower                                      |
| async_generators         | 368 ms                                                 | 444 ms: 1.20x slower                                       |
| dask                     | 360 ms                                                 | 536 ms: 1.49x slower                                       |
| Geometric mean           | (ref)                                                  | 1.03x faster                                               |

Benchmark hidden because not significant (4): fannkuch, pathlib, bench_mp_pool, mypy2
Ignored benchmarks (15) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
