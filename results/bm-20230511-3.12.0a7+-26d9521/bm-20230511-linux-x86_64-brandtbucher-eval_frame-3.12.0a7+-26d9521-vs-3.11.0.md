
# Results vs. 3.11.0

- fork: brandtbucher
- ref: eval_frame
- machine: linux-x86_64
- commit hash: 26d9521
- commit date: 2023-05-11
- overall geometric mean: 1.03x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230511-linux-x86_64-brandtbucher-eval_frame-3.12.0a7+-26d9521 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 269 ms: 1.04x slower                                               |
| docutils       | 2.63 sec                                               | 2.72 sec: 1.04x slower                                             |
| tornado_http   | 96.3 ms                                                | 99.3 ms: 1.03x slower                                              |
| Geometric mean | (ref)                                                  | 1.04x slower                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230511-linux-x86_64-brandtbucher-eval_frame-3.12.0a7+-26d9521 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| pidigits       | 198 ms                                                 | 189 ms: 1.05x faster                                               |
| nbody          | 93.1 ms                                                | 90.5 ms: 1.03x faster                                              |
| float          | 77.2 ms                                                | 81.8 ms: 1.06x slower                                              |
| Geometric mean | (ref)                                                  | 1.01x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230511-linux-x86_64-brandtbucher-eval_frame-3.12.0a7+-26d9521 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.53 ms: 1.13x faster                                              |
| regex_v8       | 22.0 ms                                                | 20.9 ms: 1.05x faster                                              |
| regex_compile  | 138 ms                                                 | 145 ms: 1.05x slower                                               |
| Geometric mean | (ref)                                                  | 1.03x faster                                                       |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230511-linux-x86_64-brandtbucher-eval_frame-3.12.0a7+-26d9521 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 10.0 ms: 1.26x faster                                              |
| json_loads           | 26.5 us                                                | 25.0 us: 1.06x faster                                              |
| unpickle_pure_python | 228 us                                                 | 220 us: 1.04x faster                                               |
| xml_etree_parse      | 158 ms                                                 | 155 ms: 1.02x faster                                               |
| xml_etree_iterparse  | 104 ms                                                 | 104 ms: 1.01x slower                                               |
| pickle_pure_python   | 306 us                                                 | 314 us: 1.03x slower                                               |
| pickle_dict          | 31.1 us                                                | 32.2 us: 1.03x slower                                              |
| pickle               | 10.1 us                                                | 10.5 us: 1.04x slower                                              |
| unpickle             | 13.7 us                                                | 14.8 us: 1.09x slower                                              |
| xml_etree_process    | 53.9 ms                                                | 59.2 ms: 1.10x slower                                              |
| xml_etree_generate   | 76.2 ms                                                | 85.6 ms: 1.12x slower                                              |
| pickle_list          | 4.11 us                                                | 4.80 us: 1.17x slower                                              |
| Geometric mean       | (ref)                                                  | 1.02x slower                                                       |

Benchmark hidden because not significant (2): tomli_loads, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230511-linux-x86_64-brandtbucher-eval_frame-3.12.0a7+-26d9521 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.18 ms: 1.08x slower                                              |
| python_startup_no_site | 6.01 ms                                                | 6.71 ms: 1.12x slower                                              |
| Geometric mean         | (ref)                                                  | 1.10x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230511-linux-x86_64-brandtbucher-eval_frame-3.12.0a7+-26d9521 |
|-----------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| mako      | 10.1 ms                                                | 10.9 ms: 1.08x slower                                              |

All benchmarks:
===============

| Benchmark                | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230511-linux-x86_64-brandtbucher-eval_frame-3.12.0a7+-26d9521 |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| typing_runtime_protocols | 486 us                                                 | 146 us: 3.33x faster                                               |
| generators               | 73.5 ms                                                | 32.2 ms: 2.28x faster                                              |
| asyncio_tcp              | 922 ms                                                 | 516 ms: 1.79x faster                                               |
| asyncio_tcp_ssl          | 3.14 sec                                               | 1.79 sec: 1.75x faster                                             |
| json_dumps               | 12.6 ms                                                | 10.0 ms: 1.26x faster                                              |
| mypy2                    | 420 ms                                                 | 346 ms: 1.21x faster                                               |
| regex_effbot             | 3.99 ms                                                | 3.53 ms: 1.13x faster                                              |
| coroutines               | 25.5 ms                                                | 22.7 ms: 1.12x faster                                              |
| async_tree_none          | 526 ms                                                 | 471 ms: 1.12x faster                                               |
| async_tree_io            | 1.30 sec                                               | 1.16 sec: 1.12x faster                                             |
| richards_super           | 56.8 ms                                                | 51.0 ms: 1.11x faster                                              |
| async_tree_memoization   | 627 ms                                                 | 575 ms: 1.09x faster                                               |
| comprehensions           | 22.4 us                                                | 20.9 us: 1.07x faster                                              |
| json_loads               | 26.5 us                                                | 25.0 us: 1.06x faster                                              |
| chaos                    | 69.2 ms                                                | 65.4 ms: 1.06x faster                                              |
| regex_v8                 | 22.0 ms                                                | 20.9 ms: 1.05x faster                                              |
| pidigits                 | 198 ms                                                 | 189 ms: 1.05x faster                                               |
| sqlglot_parse            | 1.40 ms                                                | 1.34 ms: 1.05x faster                                              |
| deltablue                | 3.67 ms                                                | 3.52 ms: 1.04x faster                                              |
| coverage                 | 100 ms                                                 | 96.0 ms: 1.04x faster                                              |
| async_tree_cpu_io_mixed  | 739 ms                                                 | 710 ms: 1.04x faster                                               |
| json                     | 4.94 ms                                                | 4.76 ms: 1.04x faster                                              |
| unpickle_pure_python     | 228 us                                                 | 220 us: 1.04x faster                                               |
| nbody                    | 93.1 ms                                                | 90.5 ms: 1.03x faster                                              |
| pycparser                | 1.18 sec                                               | 1.15 sec: 1.03x faster                                             |
| mdp                      | 2.62 sec                                               | 2.55 sec: 1.03x faster                                             |
| go                       | 140 ms                                                 | 136 ms: 1.03x faster                                               |
| sqlglot_transpile        | 1.70 ms                                                | 1.66 ms: 1.03x faster                                              |
| hexiom                   | 6.37 ms                                                | 6.22 ms: 1.02x faster                                              |
| gc_traversal             | 4.02 ms                                                | 3.93 ms: 1.02x faster                                              |
| xml_etree_parse          | 158 ms                                                 | 155 ms: 1.02x faster                                               |
| richards                 | 45.7 ms                                                | 45.1 ms: 1.01x faster                                              |
| nqueens                  | 83.4 ms                                                | 82.6 ms: 1.01x faster                                              |
| fannkuch                 | 388 ms                                                 | 386 ms: 1.00x faster                                               |
| xml_etree_iterparse      | 104 ms                                                 | 104 ms: 1.01x slower                                               |
| create_gc_cycles         | 1.49 ms                                                | 1.50 ms: 1.01x slower                                              |
| raytrace                 | 297 ms                                                 | 300 ms: 1.01x slower                                               |
| sqlglot_normalize        | 108 ms                                                 | 109 ms: 1.01x slower                                               |
| bench_thread_pool        | 819 us                                                 | 829 us: 1.01x slower                                               |
| pathlib                  | 18.2 ms                                                | 18.5 ms: 1.01x slower                                              |
| sqlglot_optimize         | 53.1 ms                                                | 53.9 ms: 1.02x slower                                              |
| deepcopy_memo            | 37.0 us                                                | 37.9 us: 1.02x slower                                              |
| pickle_pure_python       | 306 us                                                 | 314 us: 1.03x slower                                               |
| tornado_http             | 96.3 ms                                                | 99.3 ms: 1.03x slower                                              |
| pprint_pformat           | 1.46 sec                                               | 1.50 sec: 1.03x slower                                             |
| logging_simple           | 6.03 us                                                | 6.23 us: 1.03x slower                                              |
| pickle_dict              | 31.1 us                                                | 32.2 us: 1.03x slower                                              |
| sqlalchemy_imperative    | 17.9 ms                                                | 18.5 ms: 1.03x slower                                              |
| docutils                 | 2.63 sec                                               | 2.72 sec: 1.04x slower                                             |
| deepcopy                 | 342 us                                                 | 354 us: 1.04x slower                                               |
| crypto_pyaes             | 74.7 ms                                                | 77.5 ms: 1.04x slower                                              |
| scimark_lu               | 110 ms                                                 | 114 ms: 1.04x slower                                               |
| 2to3                     | 259 ms                                                 | 269 ms: 1.04x slower                                               |
| telco                    | 6.58 ms                                                | 6.84 ms: 1.04x slower                                              |
| logging_format           | 6.68 us                                                | 6.94 us: 1.04x slower                                              |
| scimark_sor              | 118 ms                                                 | 123 ms: 1.04x slower                                               |
| pickle                   | 10.1 us                                                | 10.5 us: 1.04x slower                                              |
| pprint_safe_repr         | 701 ms                                                 | 733 ms: 1.05x slower                                               |
| regex_compile            | 138 ms                                                 | 145 ms: 1.05x slower                                               |
| sqlalchemy_declarative   | 138 ms                                                 | 145 ms: 1.05x slower                                               |
| spectral_norm            | 100 ms                                                 | 105 ms: 1.05x slower                                               |
| float                    | 77.2 ms                                                | 81.8 ms: 1.06x slower                                              |
| dulwich_log              | 63.7 ms                                                | 67.8 ms: 1.07x slower                                              |
| pyflate                  | 418 ms                                                 | 448 ms: 1.07x slower                                               |
| scimark_monte_carlo      | 68.1 ms                                                | 73.0 ms: 1.07x slower                                              |
| deepcopy_reduce          | 2.94 us                                                | 3.16 us: 1.08x slower                                              |
| python_startup           | 8.52 ms                                                | 9.18 ms: 1.08x slower                                              |
| mako                     | 10.1 ms                                                | 10.9 ms: 1.08x slower                                              |
| sqlite_synth             | 2.52 us                                                | 2.73 us: 1.08x slower                                              |
| unpack_sequence          | 43.1 ns                                                | 46.7 ns: 1.08x slower                                              |
| unpickle                 | 13.7 us                                                | 14.8 us: 1.09x slower                                              |
| scimark_fft              | 328 ms                                                 | 361 ms: 1.10x slower                                               |
| xml_etree_process        | 53.9 ms                                                | 59.2 ms: 1.10x slower                                              |
| scimark_sparse_mat_mult  | 4.50 ms                                                | 4.98 ms: 1.11x slower                                              |
| python_startup_no_site   | 6.01 ms                                                | 6.71 ms: 1.12x slower                                              |
| xml_etree_generate       | 76.2 ms                                                | 85.6 ms: 1.12x slower                                              |
| pickle_list              | 4.11 us                                                | 4.80 us: 1.17x slower                                              |
| async_generators         | 368 ms                                                 | 456 ms: 1.24x slower                                               |
| dask                     | 360 ms                                                 | 539 ms: 1.50x slower                                               |
| Geometric mean           | (ref)                                                  | 1.03x faster                                                       |

Benchmark hidden because not significant (6): meteor_contest, regex_dna, tomli_loads, unpickle_list, bench_mp_pool, logging_silent
Ignored benchmarks (15) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
