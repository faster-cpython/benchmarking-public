
# Results vs. 3.10.4

- fork: python
- ref: da1980afcb8820ffaa05
- machine: linux-x86_64
- commit hash: da1980a
- commit date: 2023-05-03
- overall geometric mean: 1.24x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230503-linux-x86_64-python-da1980afcb8820ffaa05-3.12.0a7+-da1980a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 271 ms: 1.24x faster                                                   |
| docutils       | 3.17 sec                                               | 2.73 sec: 1.16x faster                                                 |
| tornado_http   | 127 ms                                                 | 99.9 ms: 1.28x faster                                                  |
| Geometric mean | (ref)                                                  | 1.23x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230503-linux-x86_64-python-da1980afcb8820ffaa05-3.12.0a7+-da1980a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 87.4 ms: 1.62x faster                                                  |
| float          | 111 ms                                                 | 82.0 ms: 1.35x faster                                                  |
| pidigits       | 190 ms                                                 | 189 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                  | 1.30x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230503-linux-x86_64-python-da1980afcb8820ffaa05-3.12.0a7+-da1980a |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 145 ms: 1.22x faster                                                   |
| regex_v8       | 25.0 ms                                                | 22.2 ms: 1.13x faster                                                  |
| regex_dna      | 222 ms                                                 | 205 ms: 1.08x faster                                                   |
| regex_effbot   | 3.23 ms                                                | 3.40 ms: 1.05x slower                                                  |
| Geometric mean | (ref)                                                  | 1.09x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230503-linux-x86_64-python-da1980afcb8820ffaa05-3.12.0a7+-da1980a |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 316 us: 1.44x faster                                                   |
| unpickle_pure_python | 300 us                                                 | 220 us: 1.37x faster                                                   |
| json_dumps           | 13.5 ms                                                | 10.0 ms: 1.35x faster                                                  |
| xml_etree_process    | 74.9 ms                                                | 58.7 ms: 1.28x faster                                                  |
| json_loads           | 28.8 us                                                | 25.7 us: 1.12x faster                                                  |
| xml_etree_generate   | 94.2 ms                                                | 84.3 ms: 1.12x faster                                                  |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.08x faster                                                   |
| xml_etree_parse      | 163 ms                                                 | 153 ms: 1.07x faster                                                   |
| pickle_list          | 4.56 us                                                | 4.58 us: 1.01x slower                                                  |
| pickle               | 10.3 us                                                | 10.5 us: 1.02x slower                                                  |
| unpickle             | 14.1 us                                                | 14.8 us: 1.05x slower                                                  |
| unpickle_list        | 4.82 us                                                | 5.10 us: 1.06x slower                                                  |
| pickle_dict          | 27.3 us                                                | 31.8 us: 1.17x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.11x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230503-linux-x86_64-python-da1980afcb8820ffaa05-3.12.0a7+-da1980a |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.14 ms: 1.55x faster                                                  |
| python_startup_no_site | 5.82 ms                                                | 6.69 ms: 1.15x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.16x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230503-linux-x86_64-python-da1980afcb8820ffaa05-3.12.0a7+-da1980a |
|-----------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako      | 14.8 ms                                                | 10.9 ms: 1.36x faster                                                  |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230503-linux-x86_64-python-da1980afcb8820ffaa05-3.12.0a7+-da1980a |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| generators              | 76.8 ms                                                | 32.3 ms: 2.38x faster                                                  |
| deltablue               | 7.42 ms                                                | 3.64 ms: 2.04x faster                                                  |
| asyncio_tcp             | 925 ms                                                 | 510 ms: 1.81x faster                                                   |
| logging_silent          | 175 ns                                                 | 104 ns: 1.69x faster                                                   |
| richards                | 74.9 ms                                                | 44.7 ms: 1.68x faster                                                  |
| go                      | 229 ms                                                 | 138 ms: 1.66x faster                                                   |
| nbody                   | 142 ms                                                 | 87.4 ms: 1.62x faster                                                  |
| scimark_sor             | 197 ms                                                 | 127 ms: 1.55x faster                                                   |
| python_startup          | 14.2 ms                                                | 9.14 ms: 1.55x faster                                                  |
| sqlglot_parse           | 2.06 ms                                                | 1.34 ms: 1.54x faster                                                  |
| hexiom                  | 9.53 ms                                                | 6.23 ms: 1.53x faster                                                  |
| chaos                   | 106 ms                                                 | 69.9 ms: 1.52x faster                                                  |
| raytrace                | 464 ms                                                 | 306 ms: 1.51x faster                                                   |
| crypto_pyaes            | 118 ms                                                 | 79.6 ms: 1.49x faster                                                  |
| scimark_monte_carlo     | 108 ms                                                 | 73.3 ms: 1.48x faster                                                  |
| pyflate                 | 673 ms                                                 | 456 ms: 1.48x faster                                                   |
| sqlglot_transpile       | 2.45 ms                                                | 1.67 ms: 1.47x faster                                                  |
| async_tree_io           | 1.77 sec                                               | 1.23 sec: 1.44x faster                                                 |
| pickle_pure_python      | 455 us                                                 | 316 us: 1.44x faster                                                   |
| async_tree_none         | 717 ms                                                 | 500 ms: 1.44x faster                                                   |
| scimark_lu              | 163 ms                                                 | 115 ms: 1.42x faster                                                   |
| async_tree_memoization  | 854 ms                                                 | 612 ms: 1.40x faster                                                   |
| coroutines              | 31.8 ms                                                | 22.9 ms: 1.39x faster                                                  |
| spectral_norm           | 150 ms                                                 | 109 ms: 1.38x faster                                                   |
| unpickle_pure_python    | 300 us                                                 | 220 us: 1.37x faster                                                   |
| mako                    | 14.8 ms                                                | 10.9 ms: 1.36x faster                                                  |
| json_dumps              | 13.5 ms                                                | 10.0 ms: 1.35x faster                                                  |
| float                   | 111 ms                                                 | 82.0 ms: 1.35x faster                                                  |
| deepcopy_memo           | 52.3 us                                                | 38.9 us: 1.35x faster                                                  |
| pprint_pformat          | 1.99 sec                                               | 1.50 sec: 1.33x faster                                                 |
| async_tree_cpu_io_mixed | 951 ms                                                 | 724 ms: 1.31x faster                                                   |
| pycparser               | 1.50 sec                                               | 1.15 sec: 1.30x faster                                                 |
| pprint_safe_repr        | 955 ms                                                 | 734 ms: 1.30x faster                                                   |
| unpack_sequence         | 64.7 ns                                                | 49.9 ns: 1.30x faster                                                  |
| xml_etree_process       | 74.9 ms                                                | 58.7 ms: 1.28x faster                                                  |
| tornado_http            | 127 ms                                                 | 99.9 ms: 1.28x faster                                                  |
| logging_simple          | 8.07 us                                                | 6.35 us: 1.27x faster                                                  |
| fannkuch                | 486 ms                                                 | 383 ms: 1.27x faster                                                   |
| logging_format          | 8.91 us                                                | 7.06 us: 1.26x faster                                                  |
| 2to3                    | 336 ms                                                 | 271 ms: 1.24x faster                                                   |
| mypy2                   | 428 ms                                                 | 352 ms: 1.22x faster                                                   |
| regex_compile           | 177 ms                                                 | 145 ms: 1.22x faster                                                   |
| nqueens                 | 100 ms                                                 | 82.8 ms: 1.21x faster                                                  |
| scimark_fft             | 424 ms                                                 | 353 ms: 1.20x faster                                                   |
| deepcopy                | 442 us                                                 | 370 us: 1.19x faster                                                   |
| sqlglot_normalize       | 135 ms                                                 | 114 ms: 1.19x faster                                                   |
| sqlglot_optimize        | 65.3 ms                                                | 55.5 ms: 1.18x faster                                                  |
| deepcopy_reduce         | 3.82 us                                                | 3.28 us: 1.17x faster                                                  |
| docutils                | 3.17 sec                                               | 2.73 sec: 1.16x faster                                                 |
| comprehensions          | 26.8 us                                                | 23.2 us: 1.16x faster                                                  |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.73 ms: 1.15x faster                                                  |
| create_gc_cycles        | 1.67 ms                                                | 1.46 ms: 1.15x faster                                                  |
| bench_thread_pool       | 947 us                                                 | 836 us: 1.13x faster                                                   |
| sqlalchemy_declarative  | 165 ms                                                 | 146 ms: 1.13x faster                                                   |
| regex_v8                | 25.0 ms                                                | 22.2 ms: 1.13x faster                                                  |
| json_loads              | 28.8 us                                                | 25.7 us: 1.12x faster                                                  |
| dulwich_log             | 75.9 ms                                                | 67.8 ms: 1.12x faster                                                  |
| xml_etree_generate      | 94.2 ms                                                | 84.3 ms: 1.12x faster                                                  |
| sqlalchemy_imperative   | 21.2 ms                                                | 19.0 ms: 1.11x faster                                                  |
| json                    | 5.42 ms                                                | 4.91 ms: 1.10x faster                                                  |
| sqlite_synth            | 2.93 us                                                | 2.70 us: 1.09x faster                                                  |
| pathlib                 | 20.0 ms                                                | 18.5 ms: 1.08x faster                                                  |
| regex_dna               | 222 ms                                                 | 205 ms: 1.08x faster                                                   |
| mdp                     | 2.82 sec                                               | 2.61 sec: 1.08x faster                                                 |
| xml_etree_iterparse     | 111 ms                                                 | 103 ms: 1.08x faster                                                   |
| xml_etree_parse         | 163 ms                                                 | 153 ms: 1.07x faster                                                   |
| gc_traversal            | 3.84 ms                                                | 3.64 ms: 1.06x faster                                                  |
| pidigits                | 190 ms                                                 | 189 ms: 1.01x faster                                                   |
| pickle_list             | 4.56 us                                                | 4.58 us: 1.01x slower                                                  |
| pickle                  | 10.3 us                                                | 10.5 us: 1.02x slower                                                  |
| meteor_contest          | 115 ms                                                 | 118 ms: 1.02x slower                                                   |
| telco                   | 6.54 ms                                                | 6.78 ms: 1.04x slower                                                  |
| unpickle                | 14.1 us                                                | 14.8 us: 1.05x slower                                                  |
| regex_effbot            | 3.23 ms                                                | 3.40 ms: 1.05x slower                                                  |
| unpickle_list           | 4.82 us                                                | 5.10 us: 1.06x slower                                                  |
| async_generators        | 425 ms                                                 | 453 ms: 1.06x slower                                                   |
| python_startup_no_site  | 5.82 ms                                                | 6.69 ms: 1.15x slower                                                  |
| pickle_dict             | 27.3 us                                                | 31.8 us: 1.17x slower                                                  |
| dask                    | 423 ms                                                 | 542 ms: 1.28x slower                                                   |
| coverage                | 72.8 ms                                                | 103 ms: 1.41x slower                                                   |
| Geometric mean          | (ref)                                                  | 1.24x faster                                                           |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (19) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, richards_super, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.21x
- 95% likely to have a speedup of 1.20x
- 99% likely to have a speedup of 1.17x
