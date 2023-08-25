
# Results vs. 3.11.0

- fork: gvanrossum
- ref: call_uops_forever
- machine: linux-x86_64
- commit hash: f6a72ae
- commit date: 2023-08-16
- overall geometric mean: 1.01x slower
- HPT reliability: 99.88%
- HPT 99th percentile: 1.01x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230816-linux-x86_64-gvanrossum-call_uops_forever-3.13.0a0-f6a72ae |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| docutils       | 2.63 sec                                               | 2.72 sec: 1.04x slower                                                 |
| tornado_http   | 96.3 ms                                                | 97.9 ms: 1.02x slower                                                  |
| Geometric mean | (ref)                                                  | 1.03x slower                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230816-linux-x86_64-gvanrossum-call_uops_forever-3.13.0a0-f6a72ae |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pidigits       | 198 ms                                                 | 201 ms: 1.02x slower                                                   |
| float          | 77.2 ms                                                | 84.8 ms: 1.10x slower                                                  |
| nbody          | 93.1 ms                                                | 115 ms: 1.24x slower                                                   |
| Geometric mean | (ref)                                                  | 1.11x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230816-linux-x86_64-gvanrossum-call_uops_forever-3.13.0a0-f6a72ae |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.74 ms: 1.07x faster                                                  |
| regex_dna      | 204 ms                                                 | 214 ms: 1.05x slower                                                   |
| regex_v8       | 22.0 ms                                                | 24.0 ms: 1.09x slower                                                  |
| regex_compile  | 138 ms                                                 | 155 ms: 1.13x slower                                                   |
| Geometric mean | (ref)                                                  | 1.05x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230816-linux-x86_64-gvanrossum-call_uops_forever-3.13.0a0-f6a72ae |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.87 ms: 1.27x faster                                                  |
| json_loads           | 26.5 us                                                | 25.2 us: 1.05x faster                                                  |
| xml_etree_parse      | 158 ms                                                 | 152 ms: 1.04x faster                                                   |
| pickle_pure_python   | 306 us                                                 | 301 us: 1.02x faster                                                   |
| unpickle_pure_python | 228 us                                                 | 226 us: 1.01x faster                                                   |
| unpickle_list        | 4.91 us                                                | 4.99 us: 1.02x slower                                                  |
| xml_etree_iterparse  | 104 ms                                                 | 106 ms: 1.02x slower                                                   |
| pickle_dict          | 31.1 us                                                | 31.9 us: 1.02x slower                                                  |
| pickle               | 10.1 us                                                | 10.7 us: 1.06x slower                                                  |
| unpickle             | 13.7 us                                                | 14.6 us: 1.07x slower                                                  |
| xml_etree_process    | 53.9 ms                                                | 58.3 ms: 1.08x slower                                                  |
| xml_etree_generate   | 76.2 ms                                                | 85.5 ms: 1.12x slower                                                  |
| tomli_loads          | 2.22 sec                                               | 2.54 sec: 1.14x slower                                                 |
| pickle_list          | 4.11 us                                                | 4.87 us: 1.18x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.02x slower                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230816-linux-x86_64-gvanrossum-call_uops_forever-3.13.0a0-f6a72ae |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.31 ms: 1.09x slower                                                  |
| python_startup_no_site | 6.01 ms                                                | 6.82 ms: 1.13x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.11x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230816-linux-x86_64-gvanrossum-call_uops_forever-3.13.0a0-f6a72ae |
|-----------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako      | 10.1 ms                                                | 12.8 ms: 1.27x slower                                                  |

All benchmarks:
===============

| Benchmark                | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230816-linux-x86_64-gvanrossum-call_uops_forever-3.13.0a0-f6a72ae |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 486 us                                                 | 153 us: 3.17x faster                                                   |
| generators               | 73.5 ms                                                | 28.5 ms: 2.58x faster                                                  |
| asyncio_tcp              | 922 ms                                                 | 488 ms: 1.89x faster                                                   |
| asyncio_tcp_ssl          | 3.14 sec                                               | 1.79 sec: 1.75x faster                                                 |
| json_dumps               | 12.6 ms                                                | 9.87 ms: 1.27x faster                                                  |
| coroutines               | 25.5 ms                                                | 21.7 ms: 1.18x faster                                                  |
| async_tree_none          | 526 ms                                                 | 450 ms: 1.17x faster                                                   |
| coverage                 | 100 ms                                                 | 86.0 ms: 1.16x faster                                                  |
| async_tree_memoization   | 627 ms                                                 | 570 ms: 1.10x faster                                                   |
| async_tree_io            | 1.30 sec                                               | 1.19 sec: 1.09x faster                                                 |
| regex_effbot             | 3.99 ms                                                | 3.74 ms: 1.07x faster                                                  |
| sqlglot_parse            | 1.40 ms                                                | 1.32 ms: 1.06x faster                                                  |
| json_loads               | 26.5 us                                                | 25.2 us: 1.05x faster                                                  |
| gc_traversal             | 4.02 ms                                                | 3.83 ms: 1.05x faster                                                  |
| xml_etree_parse          | 158 ms                                                 | 152 ms: 1.04x faster                                                   |
| async_tree_cpu_io_mixed  | 739 ms                                                 | 710 ms: 1.04x faster                                                   |
| sqlglot_transpile        | 1.70 ms                                                | 1.64 ms: 1.04x faster                                                  |
| raytrace                 | 297 ms                                                 | 286 ms: 1.04x faster                                                   |
| json                     | 4.94 ms                                                | 4.85 ms: 1.02x faster                                                  |
| pickle_pure_python       | 306 us                                                 | 301 us: 1.02x faster                                                   |
| deltablue                | 3.67 ms                                                | 3.62 ms: 1.01x faster                                                  |
| logging_format           | 6.68 us                                                | 6.60 us: 1.01x faster                                                  |
| create_gc_cycles         | 1.49 ms                                                | 1.47 ms: 1.01x faster                                                  |
| unpickle_pure_python     | 228 us                                                 | 226 us: 1.01x faster                                                   |
| logging_simple           | 6.03 us                                                | 5.99 us: 1.01x faster                                                  |
| sqlglot_normalize        | 108 ms                                                 | 109 ms: 1.01x slower                                                   |
| crypto_pyaes             | 74.7 ms                                                | 75.5 ms: 1.01x slower                                                  |
| pidigits                 | 198 ms                                                 | 201 ms: 1.02x slower                                                   |
| tornado_http             | 96.3 ms                                                | 97.9 ms: 1.02x slower                                                  |
| unpickle_list            | 4.91 us                                                | 4.99 us: 1.02x slower                                                  |
| xml_etree_iterparse      | 104 ms                                                 | 106 ms: 1.02x slower                                                   |
| mdp                      | 2.62 sec                                               | 2.67 sec: 1.02x slower                                                 |
| pickle_dict              | 31.1 us                                                | 31.9 us: 1.02x slower                                                  |
| bench_thread_pool        | 819 us                                                 | 848 us: 1.03x slower                                                   |
| docutils                 | 2.63 sec                                               | 2.72 sec: 1.04x slower                                                 |
| sqlglot_optimize         | 53.1 ms                                                | 55.1 ms: 1.04x slower                                                  |
| logging_silent           | 101 ns                                                 | 105 ns: 1.04x slower                                                   |
| regex_dna                | 204 ms                                                 | 214 ms: 1.05x slower                                                   |
| deepcopy                 | 342 us                                                 | 359 us: 1.05x slower                                                   |
| pycparser                | 1.18 sec                                               | 1.25 sec: 1.06x slower                                                 |
| pathlib                  | 18.2 ms                                                | 19.3 ms: 1.06x slower                                                  |
| pprint_pformat           | 1.46 sec                                               | 1.54 sec: 1.06x slower                                                 |
| pickle                   | 10.1 us                                                | 10.7 us: 1.06x slower                                                  |
| dulwich_log              | 63.7 ms                                                | 67.7 ms: 1.06x slower                                                  |
| pprint_safe_repr         | 701 ms                                                 | 747 ms: 1.07x slower                                                   |
| unpickle                 | 13.7 us                                                | 14.6 us: 1.07x slower                                                  |
| go                       | 140 ms                                                 | 150 ms: 1.07x slower                                                   |
| scimark_lu               | 110 ms                                                 | 118 ms: 1.07x slower                                                   |
| xml_etree_process        | 53.9 ms                                                | 58.3 ms: 1.08x slower                                                  |
| sqlite_synth             | 2.52 us                                                | 2.74 us: 1.09x slower                                                  |
| regex_v8                 | 22.0 ms                                                | 24.0 ms: 1.09x slower                                                  |
| deepcopy_reduce          | 2.94 us                                                | 3.21 us: 1.09x slower                                                  |
| scimark_sor              | 118 ms                                                 | 129 ms: 1.09x slower                                                   |
| python_startup           | 8.52 ms                                                | 9.31 ms: 1.09x slower                                                  |
| float                    | 77.2 ms                                                | 84.8 ms: 1.10x slower                                                  |
| unpack_sequence          | 43.1 ns                                                | 47.3 ns: 1.10x slower                                                  |
| richards                 | 45.7 ms                                                | 50.4 ms: 1.10x slower                                                  |
| meteor_contest           | 107 ms                                                 | 118 ms: 1.10x slower                                                   |
| xml_etree_generate       | 76.2 ms                                                | 85.5 ms: 1.12x slower                                                  |
| regex_compile            | 138 ms                                                 | 155 ms: 1.13x slower                                                   |
| python_startup_no_site   | 6.01 ms                                                | 6.82 ms: 1.13x slower                                                  |
| tomli_loads              | 2.22 sec                                               | 2.54 sec: 1.14x slower                                                 |
| deepcopy_memo            | 37.0 us                                                | 42.5 us: 1.15x slower                                                  |
| comprehensions           | 22.4 us                                                | 26.0 us: 1.16x slower                                                  |
| spectral_norm            | 100 ms                                                 | 116 ms: 1.16x slower                                                   |
| pickle_list              | 4.11 us                                                | 4.87 us: 1.18x slower                                                  |
| nqueens                  | 83.4 ms                                                | 99.4 ms: 1.19x slower                                                  |
| telco                    | 6.58 ms                                                | 8.12 ms: 1.23x slower                                                  |
| nbody                    | 93.1 ms                                                | 115 ms: 1.24x slower                                                   |
| fannkuch                 | 388 ms                                                 | 480 ms: 1.24x slower                                                   |
| pyflate                  | 418 ms                                                 | 519 ms: 1.24x slower                                                   |
| hexiom                   | 6.37 ms                                                | 8.00 ms: 1.26x slower                                                  |
| mako                     | 10.1 ms                                                | 12.8 ms: 1.27x slower                                                  |
| async_generators         | 368 ms                                                 | 472 ms: 1.28x slower                                                   |
| scimark_fft              | 328 ms                                                 | 425 ms: 1.29x slower                                                   |
| scimark_sparse_mat_mult  | 4.50 ms                                                | 6.19 ms: 1.38x slower                                                  |
| dask                     | 360 ms                                                 | 533 ms: 1.48x slower                                                   |
| Geometric mean           | (ref)                                                  | 1.01x slower                                                           |

Benchmark hidden because not significant (5): richards_super, bench_mp_pool, chaos, scimark_monte_carlo, mypy2
Ignored benchmarks (18) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 99.88% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.01x
