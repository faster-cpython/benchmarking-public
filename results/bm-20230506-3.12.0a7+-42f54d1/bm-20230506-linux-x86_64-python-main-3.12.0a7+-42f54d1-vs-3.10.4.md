
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 42f54d1
- commit date: 2023-05-06
- overall geometric mean: 1.25x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230506-linux-x86_64-python-main-3.12.0a7+-42f54d1 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 269 ms: 1.25x faster                                   |
| docutils       | 3.17 sec                                               | 2.72 sec: 1.16x faster                                 |
| tornado_http   | 127 ms                                                 | 99.9 ms: 1.28x faster                                  |
| Geometric mean | (ref)                                                  | 1.23x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230506-linux-x86_64-python-main-3.12.0a7+-42f54d1 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 142 ms                                                 | 88.0 ms: 1.61x faster                                  |
| float          | 111 ms                                                 | 81.2 ms: 1.36x faster                                  |
| pidigits       | 190 ms                                                 | 197 ms: 1.04x slower                                   |
| Geometric mean | (ref)                                                  | 1.28x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230506-linux-x86_64-python-main-3.12.0a7+-42f54d1 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 146 ms: 1.21x faster                                   |
| regex_v8       | 25.0 ms                                                | 22.3 ms: 1.12x faster                                  |
| regex_dna      | 222 ms                                                 | 200 ms: 1.11x faster                                   |
| regex_effbot   | 3.23 ms                                                | 3.54 ms: 1.10x slower                                  |
| Geometric mean | (ref)                                                  | 1.08x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230506-linux-x86_64-python-main-3.12.0a7+-42f54d1 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 311 us: 1.47x faster                                   |
| unpickle_pure_python | 300 us                                                 | 216 us: 1.39x faster                                   |
| json_dumps           | 13.5 ms                                                | 9.94 ms: 1.36x faster                                  |
| xml_etree_process    | 74.9 ms                                                | 59.0 ms: 1.27x faster                                  |
| json_loads           | 28.8 us                                                | 25.4 us: 1.13x faster                                  |
| xml_etree_generate   | 94.2 ms                                                | 85.3 ms: 1.10x faster                                  |
| xml_etree_iterparse  | 111 ms                                                 | 104 ms: 1.08x faster                                   |
| xml_etree_parse      | 163 ms                                                 | 155 ms: 1.05x faster                                   |
| unpickle_list        | 4.82 us                                                | 4.85 us: 1.01x slower                                  |
| pickle               | 10.3 us                                                | 10.6 us: 1.03x slower                                  |
| pickle_list          | 4.56 us                                                | 4.74 us: 1.04x slower                                  |
| unpickle             | 14.1 us                                                | 15.1 us: 1.07x slower                                  |
| pickle_dict          | 27.3 us                                                | 31.4 us: 1.15x slower                                  |
| Geometric mean       | (ref)                                                  | 1.11x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230506-linux-x86_64-python-main-3.12.0a7+-42f54d1 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.17 ms: 1.54x faster                                  |
| python_startup_no_site | 5.82 ms                                                | 6.69 ms: 1.15x slower                                  |
| Geometric mean         | (ref)                                                  | 1.16x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230506-linux-x86_64-python-main-3.12.0a7+-42f54d1 |
|-----------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako      | 14.8 ms                                                | 11.0 ms: 1.34x faster                                  |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230506-linux-x86_64-python-main-3.12.0a7+-42f54d1 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| generators              | 76.8 ms                                                | 31.3 ms: 2.45x faster                                  |
| deltablue               | 7.42 ms                                                | 3.51 ms: 2.11x faster                                  |
| asyncio_tcp             | 925 ms                                                 | 512 ms: 1.81x faster                                   |
| logging_silent          | 175 ns                                                 | 99.3 ns: 1.76x faster                                  |
| richards                | 74.9 ms                                                | 43.0 ms: 1.74x faster                                  |
| go                      | 229 ms                                                 | 137 ms: 1.68x faster                                   |
| nbody                   | 142 ms                                                 | 88.0 ms: 1.61x faster                                  |
| scimark_sor             | 197 ms                                                 | 124 ms: 1.59x faster                                   |
| sqlglot_parse           | 2.06 ms                                                | 1.32 ms: 1.56x faster                                  |
| chaos                   | 106 ms                                                 | 68.9 ms: 1.54x faster                                  |
| python_startup          | 14.2 ms                                                | 9.17 ms: 1.54x faster                                  |
| raytrace                | 464 ms                                                 | 301 ms: 1.54x faster                                   |
| hexiom                  | 9.53 ms                                                | 6.22 ms: 1.53x faster                                  |
| pyflate                 | 673 ms                                                 | 441 ms: 1.53x faster                                   |
| sqlglot_transpile       | 2.45 ms                                                | 1.64 ms: 1.50x faster                                  |
| scimark_monte_carlo     | 108 ms                                                 | 72.7 ms: 1.49x faster                                  |
| crypto_pyaes            | 118 ms                                                 | 80.2 ms: 1.48x faster                                  |
| pickle_pure_python      | 455 us                                                 | 311 us: 1.47x faster                                   |
| async_tree_io           | 1.77 sec                                               | 1.23 sec: 1.45x faster                                 |
| async_tree_none         | 717 ms                                                 | 498 ms: 1.44x faster                                   |
| scimark_lu              | 163 ms                                                 | 113 ms: 1.44x faster                                   |
| coroutines              | 31.8 ms                                                | 22.1 ms: 1.44x faster                                  |
| unpack_sequence         | 64.7 ns                                                | 45.1 ns: 1.43x faster                                  |
| async_tree_memoization  | 854 ms                                                 | 613 ms: 1.39x faster                                   |
| spectral_norm           | 150 ms                                                 | 108 ms: 1.39x faster                                   |
| unpickle_pure_python    | 300 us                                                 | 216 us: 1.39x faster                                   |
| deepcopy_memo           | 52.3 us                                                | 37.8 us: 1.39x faster                                  |
| json_dumps              | 13.5 ms                                                | 9.94 ms: 1.36x faster                                  |
| float                   | 111 ms                                                 | 81.2 ms: 1.36x faster                                  |
| mako                    | 14.8 ms                                                | 11.0 ms: 1.34x faster                                  |
| pprint_pformat          | 1.99 sec                                               | 1.49 sec: 1.33x faster                                 |
| async_tree_cpu_io_mixed | 951 ms                                                 | 721 ms: 1.32x faster                                   |
| pprint_safe_repr        | 955 ms                                                 | 728 ms: 1.31x faster                                   |
| pycparser               | 1.50 sec                                               | 1.16 sec: 1.30x faster                                 |
| fannkuch                | 486 ms                                                 | 380 ms: 1.28x faster                                   |
| logging_simple          | 8.07 us                                                | 6.31 us: 1.28x faster                                  |
| tornado_http            | 127 ms                                                 | 99.9 ms: 1.28x faster                                  |
| logging_format          | 8.91 us                                                | 7.00 us: 1.27x faster                                  |
| xml_etree_process       | 74.9 ms                                                | 59.0 ms: 1.27x faster                                  |
| 2to3                    | 336 ms                                                 | 269 ms: 1.25x faster                                   |
| nqueens                 | 100 ms                                                 | 80.2 ms: 1.25x faster                                  |
| deepcopy                | 442 us                                                 | 358 us: 1.23x faster                                   |
| mypy2                   | 428 ms                                                 | 351 ms: 1.22x faster                                   |
| deepcopy_reduce         | 3.82 us                                                | 3.14 us: 1.22x faster                                  |
| sqlglot_normalize       | 135 ms                                                 | 111 ms: 1.21x faster                                   |
| regex_compile           | 177 ms                                                 | 146 ms: 1.21x faster                                   |
| sqlglot_optimize        | 65.3 ms                                                | 54.7 ms: 1.19x faster                                  |
| scimark_fft             | 424 ms                                                 | 358 ms: 1.18x faster                                   |
| docutils                | 3.17 sec                                               | 2.72 sec: 1.16x faster                                 |
| comprehensions          | 26.8 us                                                | 23.4 us: 1.14x faster                                  |
| bench_thread_pool       | 947 us                                                 | 829 us: 1.14x faster                                   |
| json_loads              | 28.8 us                                                | 25.4 us: 1.13x faster                                  |
| create_gc_cycles        | 1.67 ms                                                | 1.47 ms: 1.13x faster                                  |
| sqlalchemy_declarative  | 165 ms                                                 | 147 ms: 1.13x faster                                   |
| json                    | 5.42 ms                                                | 4.80 ms: 1.13x faster                                  |
| regex_v8                | 25.0 ms                                                | 22.3 ms: 1.12x faster                                  |
| dulwich_log             | 75.9 ms                                                | 67.7 ms: 1.12x faster                                  |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.91 ms: 1.11x faster                                  |
| regex_dna               | 222 ms                                                 | 200 ms: 1.11x faster                                   |
| xml_etree_generate      | 94.2 ms                                                | 85.3 ms: 1.10x faster                                  |
| sqlalchemy_imperative   | 21.2 ms                                                | 19.3 ms: 1.10x faster                                  |
| mdp                     | 2.82 sec                                               | 2.58 sec: 1.10x faster                                 |
| meteor_contest          | 115 ms                                                 | 105 ms: 1.09x faster                                   |
| xml_etree_iterparse     | 111 ms                                                 | 104 ms: 1.08x faster                                   |
| sqlite_synth            | 2.93 us                                                | 2.76 us: 1.06x faster                                  |
| pathlib                 | 20.0 ms                                                | 18.9 ms: 1.06x faster                                  |
| xml_etree_parse         | 163 ms                                                 | 155 ms: 1.05x faster                                   |
| gc_traversal            | 3.84 ms                                                | 3.68 ms: 1.05x faster                                  |
| unpickle_list           | 4.82 us                                                | 4.85 us: 1.01x slower                                  |
| pickle                  | 10.3 us                                                | 10.6 us: 1.03x slower                                  |
| pidigits                | 190 ms                                                 | 197 ms: 1.04x slower                                   |
| pickle_list             | 4.56 us                                                | 4.74 us: 1.04x slower                                  |
| telco                   | 6.54 ms                                                | 6.88 ms: 1.05x slower                                  |
| async_generators        | 425 ms                                                 | 451 ms: 1.06x slower                                   |
| unpickle                | 14.1 us                                                | 15.1 us: 1.07x slower                                  |
| regex_effbot            | 3.23 ms                                                | 3.54 ms: 1.10x slower                                  |
| python_startup_no_site  | 5.82 ms                                                | 6.69 ms: 1.15x slower                                  |
| pickle_dict             | 27.3 us                                                | 31.4 us: 1.15x slower                                  |
| dask                    | 423 ms                                                 | 537 ms: 1.27x slower                                   |
| coverage                | 72.8 ms                                                | 102 ms: 1.40x slower                                   |
| Geometric mean          | (ref)                                                  | 1.25x faster                                           |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (19) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, richards_super, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.22x
- 95% likely to have a speedup of 1.21x
- 99% likely to have a speedup of 1.18x
