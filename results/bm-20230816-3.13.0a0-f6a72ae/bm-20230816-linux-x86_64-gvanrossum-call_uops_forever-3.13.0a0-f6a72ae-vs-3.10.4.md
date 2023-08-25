
# Results vs. 3.10.4

- fork: gvanrossum
- ref: call_uops_forever
- machine: linux-x86_64
- commit hash: f6a72ae
- commit date: 2023-08-16
- overall geometric mean: 1.23x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.14x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230816-linux-x86_64-gvanrossum-call_uops_forever-3.13.0a0-f6a72ae |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| docutils       | 3.17 sec                                               | 2.72 sec: 1.16x faster                                                 |
| tornado_http   | 127 ms                                                 | 97.9 ms: 1.30x faster                                                  |
| Geometric mean | (ref)                                                  | 1.23x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230816-linux-x86_64-gvanrossum-call_uops_forever-3.13.0a0-f6a72ae |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 111 ms                                                 | 84.8 ms: 1.30x faster                                                  |
| nbody          | 142 ms                                                 | 115 ms: 1.23x faster                                                   |
| pidigits       | 190 ms                                                 | 201 ms: 1.06x slower                                                   |
| Geometric mean | (ref)                                                  | 1.15x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230816-linux-x86_64-gvanrossum-call_uops_forever-3.13.0a0-f6a72ae |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 155 ms: 1.14x faster                                                   |
| regex_v8       | 25.0 ms                                                | 24.0 ms: 1.04x faster                                                  |
| regex_dna      | 222 ms                                                 | 214 ms: 1.04x faster                                                   |
| regex_effbot   | 3.23 ms                                                | 3.74 ms: 1.16x slower                                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230816-linux-x86_64-gvanrossum-call_uops_forever-3.13.0a0-f6a72ae |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 301 us: 1.51x faster                                                   |
| json_dumps           | 13.5 ms                                                | 9.87 ms: 1.37x faster                                                  |
| unpickle_pure_python | 300 us                                                 | 226 us: 1.33x faster                                                   |
| xml_etree_process    | 74.9 ms                                                | 58.3 ms: 1.29x faster                                                  |
| tomli_loads          | 2.92 sec                                               | 2.54 sec: 1.15x faster                                                 |
| json_loads           | 28.8 us                                                | 25.2 us: 1.14x faster                                                  |
| xml_etree_generate   | 94.2 ms                                                | 85.5 ms: 1.10x faster                                                  |
| xml_etree_parse      | 163 ms                                                 | 152 ms: 1.07x faster                                                   |
| xml_etree_iterparse  | 111 ms                                                 | 106 ms: 1.05x faster                                                   |
| unpickle             | 14.1 us                                                | 14.6 us: 1.03x slower                                                  |
| unpickle_list        | 4.82 us                                                | 4.99 us: 1.04x slower                                                  |
| pickle               | 10.3 us                                                | 10.7 us: 1.04x slower                                                  |
| pickle_list          | 4.56 us                                                | 4.87 us: 1.07x slower                                                  |
| pickle_dict          | 27.3 us                                                | 31.9 us: 1.17x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.11x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230816-linux-x86_64-gvanrossum-call_uops_forever-3.13.0a0-f6a72ae |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.31 ms: 1.52x faster                                                  |
| python_startup_no_site | 5.82 ms                                                | 6.82 ms: 1.17x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.14x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230816-linux-x86_64-gvanrossum-call_uops_forever-3.13.0a0-f6a72ae |
|-----------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako      | 14.8 ms                                                | 12.8 ms: 1.15x faster                                                  |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230816-linux-x86_64-gvanrossum-call_uops_forever-3.13.0a0-f6a72ae |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 510 us                                                 | 153 us: 3.33x faster                                                   |
| generators               | 76.8 ms                                                | 28.5 ms: 2.69x faster                                                  |
| deltablue                | 7.42 ms                                                | 3.62 ms: 2.05x faster                                                  |
| asyncio_tcp              | 925 ms                                                 | 488 ms: 1.89x faster                                                   |
| asyncio_tcp_ssl          | 3.01 sec                                               | 1.79 sec: 1.67x faster                                                 |
| logging_silent           | 175 ns                                                 | 105 ns: 1.67x faster                                                   |
| raytrace                 | 464 ms                                                 | 286 ms: 1.62x faster                                                   |
| richards_super           | 90.7 ms                                                | 56.7 ms: 1.60x faster                                                  |
| async_tree_none          | 717 ms                                                 | 450 ms: 1.59x faster                                                   |
| scimark_monte_carlo      | 108 ms                                                 | 68.2 ms: 1.59x faster                                                  |
| crypto_pyaes             | 118 ms                                                 | 75.5 ms: 1.57x faster                                                  |
| sqlglot_parse            | 2.06 ms                                                | 1.32 ms: 1.56x faster                                                  |
| chaos                    | 106 ms                                                 | 69.2 ms: 1.54x faster                                                  |
| go                       | 229 ms                                                 | 150 ms: 1.53x faster                                                   |
| scimark_sor              | 197 ms                                                 | 129 ms: 1.53x faster                                                   |
| python_startup           | 14.2 ms                                                | 9.31 ms: 1.52x faster                                                  |
| pickle_pure_python       | 455 us                                                 | 301 us: 1.51x faster                                                   |
| async_tree_memoization   | 854 ms                                                 | 570 ms: 1.50x faster                                                   |
| async_tree_io            | 1.77 sec                                               | 1.19 sec: 1.49x faster                                                 |
| sqlglot_transpile        | 2.45 ms                                                | 1.64 ms: 1.49x faster                                                  |
| richards                 | 74.9 ms                                                | 50.4 ms: 1.49x faster                                                  |
| coroutines               | 31.8 ms                                                | 21.7 ms: 1.47x faster                                                  |
| scimark_lu               | 163 ms                                                 | 118 ms: 1.38x faster                                                   |
| json_dumps               | 13.5 ms                                                | 9.87 ms: 1.37x faster                                                  |
| unpack_sequence          | 64.7 ns                                                | 47.3 ns: 1.37x faster                                                  |
| logging_format           | 8.91 us                                                | 6.60 us: 1.35x faster                                                  |
| logging_simple           | 8.07 us                                                | 5.99 us: 1.35x faster                                                  |
| async_tree_cpu_io_mixed  | 951 ms                                                 | 710 ms: 1.34x faster                                                   |
| unpickle_pure_python     | 300 us                                                 | 226 us: 1.33x faster                                                   |
| float                    | 111 ms                                                 | 84.8 ms: 1.30x faster                                                  |
| tornado_http             | 127 ms                                                 | 97.9 ms: 1.30x faster                                                  |
| pyflate                  | 673 ms                                                 | 519 ms: 1.30x faster                                                   |
| spectral_norm            | 150 ms                                                 | 116 ms: 1.29x faster                                                   |
| pprint_pformat           | 1.99 sec                                               | 1.54 sec: 1.29x faster                                                 |
| xml_etree_process        | 74.9 ms                                                | 58.3 ms: 1.29x faster                                                  |
| pprint_safe_repr         | 955 ms                                                 | 747 ms: 1.28x faster                                                   |
| sqlglot_normalize        | 135 ms                                                 | 109 ms: 1.25x faster                                                   |
| deepcopy_memo            | 52.3 us                                                | 42.5 us: 1.23x faster                                                  |
| deepcopy                 | 442 us                                                 | 359 us: 1.23x faster                                                   |
| nbody                    | 142 ms                                                 | 115 ms: 1.23x faster                                                   |
| pycparser                | 1.50 sec                                               | 1.25 sec: 1.20x faster                                                 |
| deepcopy_reduce          | 3.82 us                                                | 3.21 us: 1.19x faster                                                  |
| hexiom                   | 9.53 ms                                                | 8.00 ms: 1.19x faster                                                  |
| sqlglot_optimize         | 65.3 ms                                                | 55.1 ms: 1.19x faster                                                  |
| docutils                 | 3.17 sec                                               | 2.72 sec: 1.16x faster                                                 |
| mako                     | 14.8 ms                                                | 12.8 ms: 1.15x faster                                                  |
| tomli_loads              | 2.92 sec                                               | 2.54 sec: 1.15x faster                                                 |
| json_loads               | 28.8 us                                                | 25.2 us: 1.14x faster                                                  |
| regex_compile            | 177 ms                                                 | 155 ms: 1.14x faster                                                   |
| create_gc_cycles         | 1.67 ms                                                | 1.47 ms: 1.14x faster                                                  |
| dulwich_log              | 75.9 ms                                                | 67.7 ms: 1.12x faster                                                  |
| bench_thread_pool        | 947 us                                                 | 848 us: 1.12x faster                                                   |
| json                     | 5.42 ms                                                | 4.85 ms: 1.12x faster                                                  |
| xml_etree_generate       | 94.2 ms                                                | 85.5 ms: 1.10x faster                                                  |
| xml_etree_parse          | 163 ms                                                 | 152 ms: 1.07x faster                                                   |
| sqlite_synth             | 2.93 us                                                | 2.74 us: 1.07x faster                                                  |
| mdp                      | 2.82 sec                                               | 2.67 sec: 1.06x faster                                                 |
| xml_etree_iterparse      | 111 ms                                                 | 106 ms: 1.05x faster                                                   |
| regex_v8                 | 25.0 ms                                                | 24.0 ms: 1.04x faster                                                  |
| pathlib                  | 20.0 ms                                                | 19.3 ms: 1.04x faster                                                  |
| regex_dna                | 222 ms                                                 | 214 ms: 1.04x faster                                                   |
| comprehensions           | 26.8 us                                                | 26.0 us: 1.03x faster                                                  |
| fannkuch                 | 486 ms                                                 | 480 ms: 1.01x faster                                                   |
| nqueens                  | 100 ms                                                 | 99.4 ms: 1.01x faster                                                  |
| gc_traversal             | 3.84 ms                                                | 3.83 ms: 1.00x faster                                                  |
| bench_mp_pool            | 24.0 ms                                                | 24.0 ms: 1.00x slower                                                  |
| meteor_contest           | 115 ms                                                 | 118 ms: 1.03x slower                                                   |
| unpickle                 | 14.1 us                                                | 14.6 us: 1.03x slower                                                  |
| unpickle_list            | 4.82 us                                                | 4.99 us: 1.04x slower                                                  |
| pickle                   | 10.3 us                                                | 10.7 us: 1.04x slower                                                  |
| pidigits                 | 190 ms                                                 | 201 ms: 1.06x slower                                                   |
| pickle_list              | 4.56 us                                                | 4.87 us: 1.07x slower                                                  |
| async_generators         | 425 ms                                                 | 472 ms: 1.11x slower                                                   |
| scimark_sparse_mat_mult  | 5.45 ms                                                | 6.19 ms: 1.13x slower                                                  |
| regex_effbot             | 3.23 ms                                                | 3.74 ms: 1.16x slower                                                  |
| pickle_dict              | 27.3 us                                                | 31.9 us: 1.17x slower                                                  |
| python_startup_no_site   | 5.82 ms                                                | 6.82 ms: 1.17x slower                                                  |
| coverage                 | 72.8 ms                                                | 86.0 ms: 1.18x slower                                                  |
| telco                    | 6.54 ms                                                | 8.12 ms: 1.24x slower                                                  |
| dask                     | 423 ms                                                 | 533 ms: 1.26x slower                                                   |
| Geometric mean           | (ref)                                                  | 1.23x faster                                                           |

Benchmark hidden because not significant (2): scimark_fft, mypy2
Ignored benchmarks (18) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.18x
- 95% likely to have a speedup of 1.16x
- 99% likely to have a speedup of 1.14x
