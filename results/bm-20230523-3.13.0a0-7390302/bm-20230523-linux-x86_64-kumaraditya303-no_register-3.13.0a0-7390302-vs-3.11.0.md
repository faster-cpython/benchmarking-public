
# Results vs. 3.11.0

- fork: kumaraditya303
- ref: no_register
- machine: linux-x86_64
- commit hash: 7390302
- commit date: 2023-05-23
- overall geometric mean: 1.04x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230523-linux-x86_64-kumaraditya303-no_register-3.13.0a0-7390302 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 267 ms: 1.03x slower                                                 |
| docutils       | 2.63 sec                                               | 2.67 sec: 1.02x slower                                               |
| tornado_http   | 96.3 ms                                                | 97.7 ms: 1.01x slower                                                |
| Geometric mean | (ref)                                                  | 1.02x slower                                                         |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230523-linux-x86_64-kumaraditya303-no_register-3.13.0a0-7390302 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody          | 93.1 ms                                                | 91.9 ms: 1.01x faster                                                |
| pidigits       | 198 ms                                                 | 196 ms: 1.01x faster                                                 |
| float          | 77.2 ms                                                | 80.2 ms: 1.04x slower                                                |
| Geometric mean | (ref)                                                  | 1.01x slower                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230523-linux-x86_64-kumaraditya303-no_register-3.13.0a0-7390302 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.48 ms: 1.15x faster                                                |
| regex_v8       | 22.0 ms                                                | 21.8 ms: 1.01x faster                                                |
| regex_dna      | 204 ms                                                 | 208 ms: 1.02x slower                                                 |
| regex_compile  | 138 ms                                                 | 145 ms: 1.05x slower                                                 |
| Geometric mean | (ref)                                                  | 1.02x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230523-linux-x86_64-kumaraditya303-no_register-3.13.0a0-7390302 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.75 ms: 1.29x faster                                                |
| json_loads           | 26.5 us                                                | 24.9 us: 1.06x faster                                                |
| unpickle_pure_python | 228 us                                                 | 215 us: 1.06x faster                                                 |
| xml_etree_parse      | 158 ms                                                 | 153 ms: 1.04x faster                                                 |
| xml_etree_iterparse  | 104 ms                                                 | 103 ms: 1.01x faster                                                 |
| tomli_loads          | 2.22 sec                                               | 2.21 sec: 1.00x faster                                               |
| pickle_pure_python   | 306 us                                                 | 311 us: 1.02x slower                                                 |
| pickle               | 10.1 us                                                | 10.5 us: 1.04x slower                                                |
| unpickle_list        | 4.91 us                                                | 5.11 us: 1.04x slower                                                |
| pickle_dict          | 31.1 us                                                | 32.9 us: 1.06x slower                                                |
| xml_etree_process    | 53.9 ms                                                | 59.1 ms: 1.10x slower                                                |
| unpickle             | 13.7 us                                                | 15.1 us: 1.10x slower                                                |
| xml_etree_generate   | 76.2 ms                                                | 84.9 ms: 1.11x slower                                                |
| pickle_list          | 4.11 us                                                | 4.65 us: 1.13x slower                                                |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230523-linux-x86_64-kumaraditya303-no_register-3.13.0a0-7390302 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.14 ms: 1.07x slower                                                |
| python_startup_no_site | 6.01 ms                                                | 6.77 ms: 1.13x slower                                                |
| Geometric mean         | (ref)                                                  | 1.10x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230523-linux-x86_64-kumaraditya303-no_register-3.13.0a0-7390302 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| genshi_xml     | 51.8 ms                                                | 50.3 ms: 1.03x faster                                                |
| genshi_text    | 21.6 ms                                                | 22.5 ms: 1.04x slower                                                |
| mako           | 10.1 ms                                                | 10.8 ms: 1.07x slower                                                |
| Geometric mean | (ref)                                                  | 1.03x slower                                                         |

All benchmarks:
===============

| Benchmark                | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230523-linux-x86_64-kumaraditya303-no_register-3.13.0a0-7390302 |
|--------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| typing_runtime_protocols | 486 us                                                 | 141 us: 3.44x faster                                                 |
| generators               | 73.5 ms                                                | 31.0 ms: 2.37x faster                                                |
| asyncio_tcp              | 922 ms                                                 | 507 ms: 1.82x faster                                                 |
| asyncio_tcp_ssl          | 3.14 sec                                               | 1.79 sec: 1.76x faster                                               |
| async_tree_none          | 526 ms                                                 | 378 ms: 1.39x faster                                                 |
| json_dumps               | 12.6 ms                                                | 9.75 ms: 1.29x faster                                                |
| async_tree_memoization   | 627 ms                                                 | 506 ms: 1.24x faster                                                 |
| async_tree_io            | 1.30 sec                                               | 1.07 sec: 1.21x faster                                               |
| async_tree_cpu_io_mixed  | 739 ms                                                 | 615 ms: 1.20x faster                                                 |
| coroutines               | 25.5 ms                                                | 22.0 ms: 1.16x faster                                                |
| regex_effbot             | 3.99 ms                                                | 3.48 ms: 1.15x faster                                                |
| richards_super           | 56.8 ms                                                | 49.6 ms: 1.14x faster                                                |
| gc_traversal             | 4.02 ms                                                | 3.54 ms: 1.14x faster                                                |
| comprehensions           | 22.4 us                                                | 20.8 us: 1.08x faster                                                |
| chaos                    | 69.2 ms                                                | 64.1 ms: 1.08x faster                                                |
| json_loads               | 26.5 us                                                | 24.9 us: 1.06x faster                                                |
| sqlglot_parse            | 1.40 ms                                                | 1.32 ms: 1.06x faster                                                |
| unpickle_pure_python     | 228 us                                                 | 215 us: 1.06x faster                                                 |
| json                     | 4.94 ms                                                | 4.72 ms: 1.05x faster                                                |
| deltablue                | 3.67 ms                                                | 3.51 ms: 1.05x faster                                                |
| richards                 | 45.7 ms                                                | 43.9 ms: 1.04x faster                                                |
| sqlglot_transpile        | 1.70 ms                                                | 1.64 ms: 1.04x faster                                                |
| go                       | 140 ms                                                 | 135 ms: 1.04x faster                                                 |
| xml_etree_parse          | 158 ms                                                 | 153 ms: 1.04x faster                                                 |
| hexiom                   | 6.37 ms                                                | 6.15 ms: 1.04x faster                                                |
| meteor_contest           | 107 ms                                                 | 103 ms: 1.04x faster                                                 |
| nqueens                  | 83.4 ms                                                | 80.6 ms: 1.03x faster                                                |
| genshi_xml               | 51.8 ms                                                | 50.3 ms: 1.03x faster                                                |
| fannkuch                 | 388 ms                                                 | 379 ms: 1.02x faster                                                 |
| coverage                 | 100 ms                                                 | 97.8 ms: 1.02x faster                                                |
| logging_silent           | 101 ns                                                 | 98.9 ns: 1.02x faster                                                |
| nbody                    | 93.1 ms                                                | 91.9 ms: 1.01x faster                                                |
| xml_etree_iterparse      | 104 ms                                                 | 103 ms: 1.01x faster                                                 |
| regex_v8                 | 22.0 ms                                                | 21.8 ms: 1.01x faster                                                |
| pidigits                 | 198 ms                                                 | 196 ms: 1.01x faster                                                 |
| tomli_loads              | 2.22 sec                                               | 2.21 sec: 1.00x faster                                               |
| sqlglot_optimize         | 53.1 ms                                                | 53.4 ms: 1.01x slower                                                |
| create_gc_cycles         | 1.49 ms                                                | 1.50 ms: 1.01x slower                                                |
| bench_thread_pool        | 819 us                                                 | 829 us: 1.01x slower                                                 |
| pathlib                  | 18.2 ms                                                | 18.5 ms: 1.01x slower                                                |
| tornado_http             | 96.3 ms                                                | 97.7 ms: 1.01x slower                                                |
| docutils                 | 2.63 sec                                               | 2.67 sec: 1.02x slower                                               |
| pickle_pure_python       | 306 us                                                 | 311 us: 1.02x slower                                                 |
| regex_dna                | 204 ms                                                 | 208 ms: 1.02x slower                                                 |
| scimark_lu               | 110 ms                                                 | 112 ms: 1.02x slower                                                 |
| djangocms                | 32.4 us                                                | 33.3 us: 1.03x slower                                                |
| deepcopy_memo            | 37.0 us                                                | 38.1 us: 1.03x slower                                                |
| telco                    | 6.58 ms                                                | 6.78 ms: 1.03x slower                                                |
| 2to3                     | 259 ms                                                 | 267 ms: 1.03x slower                                                 |
| pprint_pformat           | 1.46 sec                                               | 1.50 sec: 1.03x slower                                               |
| mdp                      | 2.62 sec                                               | 2.71 sec: 1.04x slower                                               |
| float                    | 77.2 ms                                                | 80.2 ms: 1.04x slower                                                |
| pickle                   | 10.1 us                                                | 10.5 us: 1.04x slower                                                |
| pyflate                  | 418 ms                                                 | 435 ms: 1.04x slower                                                 |
| unpickle_list            | 4.91 us                                                | 5.11 us: 1.04x slower                                                |
| genshi_text              | 21.6 ms                                                | 22.5 ms: 1.04x slower                                                |
| crypto_pyaes             | 74.7 ms                                                | 78.0 ms: 1.04x slower                                                |
| scimark_monte_carlo      | 68.1 ms                                                | 71.3 ms: 1.05x slower                                                |
| regex_compile            | 138 ms                                                 | 145 ms: 1.05x slower                                                 |
| pprint_safe_repr         | 701 ms                                                 | 736 ms: 1.05x slower                                                 |
| spectral_norm            | 100 ms                                                 | 105 ms: 1.05x slower                                                 |
| logging_simple           | 6.03 us                                                | 6.34 us: 1.05x slower                                                |
| deepcopy                 | 342 us                                                 | 359 us: 1.05x slower                                                 |
| logging_format           | 6.68 us                                                | 7.06 us: 1.06x slower                                                |
| pickle_dict              | 31.1 us                                                | 32.9 us: 1.06x slower                                                |
| scimark_fft              | 328 ms                                                 | 350 ms: 1.07x slower                                                 |
| dulwich_log              | 63.7 ms                                                | 68.0 ms: 1.07x slower                                                |
| mako                     | 10.1 ms                                                | 10.8 ms: 1.07x slower                                                |
| python_startup           | 8.52 ms                                                | 9.14 ms: 1.07x slower                                                |
| sqlite_synth             | 2.52 us                                                | 2.71 us: 1.08x slower                                                |
| scimark_sparse_mat_mult  | 4.50 ms                                                | 4.92 ms: 1.09x slower                                                |
| deepcopy_reduce          | 2.94 us                                                | 3.22 us: 1.10x slower                                                |
| xml_etree_process        | 53.9 ms                                                | 59.1 ms: 1.10x slower                                                |
| unpickle                 | 13.7 us                                                | 15.1 us: 1.10x slower                                                |
| xml_etree_generate       | 76.2 ms                                                | 84.9 ms: 1.11x slower                                                |
| python_startup_no_site   | 6.01 ms                                                | 6.77 ms: 1.13x slower                                                |
| pickle_list              | 4.11 us                                                | 4.65 us: 1.13x slower                                                |
| unpack_sequence          | 43.1 ns                                                | 51.7 ns: 1.20x slower                                                |
| async_generators         | 368 ms                                                 | 449 ms: 1.22x slower                                                 |
| Geometric mean           | (ref)                                                  | 1.04x faster                                                         |

Benchmark hidden because not significant (7): bench_mp_pool, raytrace, sqlglot_normalize, scimark_sor, pycparser, html5lib, mypy2
Ignored benchmarks (14) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, chameleon, dask, django_template, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
