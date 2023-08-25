
# Results vs. 3.10.4

- fork: python
- ref: 92d8bfffbf377e91d8b9
- machine: linux-x86_64
- commit hash: 92d8bff
- commit date: 2023-05-06
- overall geometric mean: 1.24x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230506-linux-x86_64-python-92d8bfffbf377e91d8b9-3.12.0a7+-92d8bff |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 270 ms: 1.25x faster                                                   |
| docutils       | 3.17 sec                                               | 2.73 sec: 1.16x faster                                                 |
| tornado_http   | 127 ms                                                 | 103 ms: 1.24x faster                                                   |
| Geometric mean | (ref)                                                  | 1.22x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230506-linux-x86_64-python-92d8bfffbf377e91d8b9-3.12.0a7+-92d8bff |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 90.6 ms: 1.56x faster                                                  |
| float          | 111 ms                                                 | 81.2 ms: 1.36x faster                                                  |
| pidigits       | 190 ms                                                 | 189 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                  | 1.29x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230506-linux-x86_64-python-92d8bfffbf377e91d8b9-3.12.0a7+-92d8bff |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 146 ms: 1.21x faster                                                   |
| regex_v8       | 25.0 ms                                                | 22.0 ms: 1.14x faster                                                  |
| regex_dna      | 222 ms                                                 | 207 ms: 1.07x faster                                                   |
| regex_effbot   | 3.23 ms                                                | 3.60 ms: 1.11x slower                                                  |
| Geometric mean | (ref)                                                  | 1.07x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230506-linux-x86_64-python-92d8bfffbf377e91d8b9-3.12.0a7+-92d8bff |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 316 us: 1.44x faster                                                   |
| json_dumps           | 13.5 ms                                                | 9.87 ms: 1.37x faster                                                  |
| unpickle_pure_python | 300 us                                                 | 220 us: 1.37x faster                                                   |
| xml_etree_process    | 74.9 ms                                                | 59.3 ms: 1.26x faster                                                  |
| json_loads           | 28.8 us                                                | 25.3 us: 1.14x faster                                                  |
| xml_etree_generate   | 94.2 ms                                                | 84.9 ms: 1.11x faster                                                  |
| xml_etree_iterparse  | 111 ms                                                 | 104 ms: 1.07x faster                                                   |
| xml_etree_parse      | 163 ms                                                 | 156 ms: 1.05x faster                                                   |
| pickle               | 10.3 us                                                | 10.5 us: 1.02x slower                                                  |
| unpickle_list        | 4.82 us                                                | 4.99 us: 1.04x slower                                                  |
| unpickle             | 14.1 us                                                | 15.0 us: 1.06x slower                                                  |
| pickle_dict          | 27.3 us                                                | 31.6 us: 1.16x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.11x faster                                                           |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230506-linux-x86_64-python-92d8bfffbf377e91d8b9-3.12.0a7+-92d8bff |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.15 ms: 1.55x faster                                                  |
| python_startup_no_site | 5.82 ms                                                | 6.69 ms: 1.15x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.16x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230506-linux-x86_64-python-92d8bfffbf377e91d8b9-3.12.0a7+-92d8bff |
|-----------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako      | 14.8 ms                                                | 10.7 ms: 1.38x faster                                                  |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230506-linux-x86_64-python-92d8bfffbf377e91d8b9-3.12.0a7+-92d8bff |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| generators              | 76.8 ms                                                | 30.9 ms: 2.48x faster                                                  |
| deltablue               | 7.42 ms                                                | 3.57 ms: 2.08x faster                                                  |
| asyncio_tcp             | 925 ms                                                 | 507 ms: 1.82x faster                                                   |
| logging_silent          | 175 ns                                                 | 102 ns: 1.71x faster                                                   |
| go                      | 229 ms                                                 | 136 ms: 1.68x faster                                                   |
| richards                | 74.9 ms                                                | 44.8 ms: 1.67x faster                                                  |
| scimark_sor             | 197 ms                                                 | 123 ms: 1.61x faster                                                   |
| nbody                   | 142 ms                                                 | 90.6 ms: 1.56x faster                                                  |
| chaos                   | 106 ms                                                 | 68.2 ms: 1.56x faster                                                  |
| hexiom                  | 9.53 ms                                                | 6.11 ms: 1.56x faster                                                  |
| python_startup          | 14.2 ms                                                | 9.15 ms: 1.55x faster                                                  |
| sqlglot_parse           | 2.06 ms                                                | 1.33 ms: 1.54x faster                                                  |
| pyflate                 | 673 ms                                                 | 442 ms: 1.52x faster                                                   |
| crypto_pyaes            | 118 ms                                                 | 77.8 ms: 1.52x faster                                                  |
| raytrace                | 464 ms                                                 | 310 ms: 1.50x faster                                                   |
| scimark_monte_carlo     | 108 ms                                                 | 72.9 ms: 1.49x faster                                                  |
| sqlglot_transpile       | 2.45 ms                                                | 1.66 ms: 1.47x faster                                                  |
| async_tree_io           | 1.77 sec                                               | 1.23 sec: 1.45x faster                                                 |
| scimark_lu              | 163 ms                                                 | 113 ms: 1.44x faster                                                   |
| pickle_pure_python      | 455 us                                                 | 316 us: 1.44x faster                                                   |
| async_tree_none         | 717 ms                                                 | 505 ms: 1.42x faster                                                   |
| spectral_norm           | 150 ms                                                 | 107 ms: 1.41x faster                                                   |
| coroutines              | 31.8 ms                                                | 22.7 ms: 1.40x faster                                                  |
| async_tree_memoization  | 854 ms                                                 | 613 ms: 1.39x faster                                                   |
| deepcopy_memo           | 52.3 us                                                | 37.7 us: 1.39x faster                                                  |
| mako                    | 14.8 ms                                                | 10.7 ms: 1.38x faster                                                  |
| json_dumps              | 13.5 ms                                                | 9.87 ms: 1.37x faster                                                  |
| unpickle_pure_python    | 300 us                                                 | 220 us: 1.37x faster                                                   |
| float                   | 111 ms                                                 | 81.2 ms: 1.36x faster                                                  |
| pprint_pformat          | 1.99 sec                                               | 1.50 sec: 1.32x faster                                                 |
| async_tree_cpu_io_mixed | 951 ms                                                 | 727 ms: 1.31x faster                                                   |
| pprint_safe_repr        | 955 ms                                                 | 734 ms: 1.30x faster                                                   |
| pycparser               | 1.50 sec                                               | 1.16 sec: 1.30x faster                                                 |
| fannkuch                | 486 ms                                                 | 377 ms: 1.29x faster                                                   |
| logging_simple          | 8.07 us                                                | 6.35 us: 1.27x faster                                                  |
| xml_etree_process       | 74.9 ms                                                | 59.3 ms: 1.26x faster                                                  |
| logging_format          | 8.91 us                                                | 7.05 us: 1.26x faster                                                  |
| nqueens                 | 100 ms                                                 | 79.5 ms: 1.26x faster                                                  |
| 2to3                    | 336 ms                                                 | 270 ms: 1.25x faster                                                   |
| tornado_http            | 127 ms                                                 | 103 ms: 1.24x faster                                                   |
| deepcopy                | 442 us                                                 | 362 us: 1.22x faster                                                   |
| regex_compile           | 177 ms                                                 | 146 ms: 1.21x faster                                                   |
| mypy2                   | 428 ms                                                 | 353 ms: 1.21x faster                                                   |
| sqlglot_normalize       | 135 ms                                                 | 112 ms: 1.20x faster                                                   |
| deepcopy_reduce         | 3.82 us                                                | 3.21 us: 1.19x faster                                                  |
| sqlglot_optimize        | 65.3 ms                                                | 55.1 ms: 1.19x faster                                                  |
| scimark_fft             | 424 ms                                                 | 358 ms: 1.18x faster                                                   |
| docutils                | 3.17 sec                                               | 2.73 sec: 1.16x faster                                                 |
| comprehensions          | 26.8 us                                                | 23.2 us: 1.16x faster                                                  |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.75 ms: 1.15x faster                                                  |
| bench_thread_pool       | 947 us                                                 | 831 us: 1.14x faster                                                   |
| regex_v8                | 25.0 ms                                                | 22.0 ms: 1.14x faster                                                  |
| json_loads              | 28.8 us                                                | 25.3 us: 1.14x faster                                                  |
| json                    | 5.42 ms                                                | 4.77 ms: 1.13x faster                                                  |
| sqlalchemy_declarative  | 165 ms                                                 | 146 ms: 1.13x faster                                                   |
| create_gc_cycles        | 1.67 ms                                                | 1.49 ms: 1.12x faster                                                  |
| dulwich_log             | 75.9 ms                                                | 68.1 ms: 1.11x faster                                                  |
| xml_etree_generate      | 94.2 ms                                                | 84.9 ms: 1.11x faster                                                  |
| unpack_sequence         | 64.7 ns                                                | 58.6 ns: 1.10x faster                                                  |
| sqlalchemy_imperative   | 21.2 ms                                                | 19.4 ms: 1.09x faster                                                  |
| meteor_contest          | 115 ms                                                 | 105 ms: 1.09x faster                                                   |
| sqlite_synth            | 2.93 us                                                | 2.74 us: 1.07x faster                                                  |
| regex_dna               | 222 ms                                                 | 207 ms: 1.07x faster                                                   |
| xml_etree_iterparse     | 111 ms                                                 | 104 ms: 1.07x faster                                                   |
| pathlib                 | 20.0 ms                                                | 18.8 ms: 1.06x faster                                                  |
| mdp                     | 2.82 sec                                               | 2.68 sec: 1.05x faster                                                 |
| xml_etree_parse         | 163 ms                                                 | 156 ms: 1.05x faster                                                   |
| pidigits                | 190 ms                                                 | 189 ms: 1.01x faster                                                   |
| bench_mp_pool           | 24.0 ms                                                | 24.0 ms: 1.00x slower                                                  |
| pickle                  | 10.3 us                                                | 10.5 us: 1.02x slower                                                  |
| telco                   | 6.54 ms                                                | 6.77 ms: 1.03x slower                                                  |
| unpickle_list           | 4.82 us                                                | 4.99 us: 1.04x slower                                                  |
| async_generators        | 425 ms                                                 | 448 ms: 1.05x slower                                                   |
| unpickle                | 14.1 us                                                | 15.0 us: 1.06x slower                                                  |
| regex_effbot            | 3.23 ms                                                | 3.60 ms: 1.11x slower                                                  |
| gc_traversal            | 3.84 ms                                                | 4.37 ms: 1.14x slower                                                  |
| python_startup_no_site  | 5.82 ms                                                | 6.69 ms: 1.15x slower                                                  |
| pickle_dict             | 27.3 us                                                | 31.6 us: 1.16x slower                                                  |
| dask                    | 423 ms                                                 | 539 ms: 1.27x slower                                                   |
| coverage                | 72.8 ms                                                | 102 ms: 1.41x slower                                                   |
| Geometric mean          | (ref)                                                  | 1.24x faster                                                           |

Benchmark hidden because not significant (1): pickle_list
Ignored benchmarks (19) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, richards_super, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.22x
- 95% likely to have a speedup of 1.21x
- 99% likely to have a speedup of 1.18x
