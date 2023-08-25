
# Results vs. 3.10.4

- fork: python
- ref: 7d4cc5aa854fdea4d01a
- machine: linux-x86_64
- commit hash: 7d4cc5a
- commit date: 2023-04-04
- overall geometric mean: 1.00x faster \*
- HPT reliability: 99.70%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230404-linux-x86_64-python-7d4cc5aa854fdea4d01a-3.10.11-7d4cc5a |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 335 ms: 1.00x faster                                                 |
| chameleon      | 9.06 ms                                                | 8.93 ms: 1.01x faster                                                |
| docutils       | 3.17 sec                                               | 3.21 sec: 1.01x slower                                               |
| tornado_http   | 127 ms                                                 | 131 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                  | 1.00x slower                                                         |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230404-linux-x86_64-python-7d4cc5aa854fdea4d01a-3.10.11-7d4cc5a |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 137 ms: 1.03x faster                                                 |
| float          | 111 ms                                                 | 108 ms: 1.02x faster                                                 |
| pidigits       | 190 ms                                                 | 188 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                  | 1.02x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230404-linux-x86_64-python-7d4cc5aa854fdea4d01a-3.10.11-7d4cc5a |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_dna      | 222 ms                                                 | 213 ms: 1.04x faster                                                 |
| regex_compile  | 177 ms                                                 | 176 ms: 1.00x faster                                                 |
| regex_v8       | 25.0 ms                                                | 25.5 ms: 1.02x slower                                                |
| regex_effbot   | 3.23 ms                                                | 3.63 ms: 1.12x slower                                                |
| Geometric mean | (ref)                                                  | 1.02x slower                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230404-linux-x86_64-python-7d4cc5aa854fdea4d01a-3.10.11-7d4cc5a |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| pickle_list          | 4.56 us                                                | 4.38 us: 1.04x faster                                                |
| xml_etree_generate   | 94.2 ms                                                | 93.1 ms: 1.01x faster                                                |
| xml_etree_process    | 74.9 ms                                                | 74.1 ms: 1.01x faster                                                |
| xml_etree_iterparse  | 111 ms                                                 | 110 ms: 1.01x faster                                                 |
| unpickle_pure_python | 300 us                                                 | 298 us: 1.01x faster                                                 |
| pickle_pure_python   | 455 us                                                 | 452 us: 1.01x faster                                                 |
| json_loads           | 28.8 us                                                | 29.0 us: 1.01x slower                                                |
| json_dumps           | 13.5 ms                                                | 13.6 ms: 1.01x slower                                                |
| pickle               | 10.3 us                                                | 10.4 us: 1.01x slower                                                |
| unpickle             | 14.1 us                                                | 14.3 us: 1.01x slower                                                |
| pickle_dict          | 27.3 us                                                | 33.7 us: 1.24x slower                                                |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                         |

Benchmark hidden because not significant (2): unpickle_list, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230404-linux-x86_64-python-7d4cc5aa854fdea4d01a-3.10.11-7d4cc5a |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 5.82 ms                                                | 5.83 ms: 1.00x slower                                                |
| python_startup         | 14.2 ms                                                | 14.2 ms: 1.00x slower                                                |
| Geometric mean         | (ref)                                                  | 1.00x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230404-linux-x86_64-python-7d4cc5aa854fdea4d01a-3.10.11-7d4cc5a |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| genshi_xml     | 63.3 ms                                                | 62.6 ms: 1.01x faster                                                |
| genshi_text    | 30.3 ms                                                | 30.1 ms: 1.01x faster                                                |
| Geometric mean | (ref)                                                  | 1.01x faster                                                         |

Benchmark hidden because not significant (2): django_template, mako

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230404-linux-x86_64-python-7d4cc5aa854fdea4d01a-3.10.11-7d4cc5a |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| aiohttp                 | 1.38 ms                                                | 1.29 ms: 1.07x faster                                                |
| spectral_norm           | 150 ms                                                 | 142 ms: 1.05x faster                                                 |
| deepcopy_memo           | 52.3 us                                                | 49.8 us: 1.05x faster                                                |
| gunicorn                | 1.46 ms                                                | 1.39 ms: 1.05x faster                                                |
| pickle_list             | 4.56 us                                                | 4.38 us: 1.04x faster                                                |
| regex_dna               | 222 ms                                                 | 213 ms: 1.04x faster                                                 |
| crypto_pyaes            | 118 ms                                                 | 114 ms: 1.04x faster                                                 |
| gc_traversal            | 3.84 ms                                                | 3.71 ms: 1.04x faster                                                |
| asyncio_tcp             | 925 ms                                                 | 894 ms: 1.03x faster                                                 |
| fannkuch                | 486 ms                                                 | 471 ms: 1.03x faster                                                 |
| deepcopy                | 442 us                                                 | 429 us: 1.03x faster                                                 |
| nbody                   | 142 ms                                                 | 137 ms: 1.03x faster                                                 |
| scimark_lu              | 163 ms                                                 | 159 ms: 1.03x faster                                                 |
| coroutines              | 31.8 ms                                                | 31.0 ms: 1.03x faster                                                |
| float                   | 111 ms                                                 | 108 ms: 1.02x faster                                                 |
| richards                | 74.9 ms                                                | 73.1 ms: 1.02x faster                                                |
| bench_thread_pool       | 947 us                                                 | 925 us: 1.02x faster                                                 |
| nqueens                 | 100 ms                                                 | 97.9 ms: 1.02x faster                                                |
| pyflate                 | 673 ms                                                 | 660 ms: 1.02x faster                                                 |
| json                    | 5.42 ms                                                | 5.32 ms: 1.02x faster                                                |
| scimark_fft             | 424 ms                                                 | 416 ms: 1.02x faster                                                 |
| generators              | 76.8 ms                                                | 75.5 ms: 1.02x faster                                                |
| chaos                   | 106 ms                                                 | 105 ms: 1.02x faster                                                 |
| meteor_contest          | 115 ms                                                 | 113 ms: 1.02x faster                                                 |
| scimark_sor             | 197 ms                                                 | 194 ms: 1.02x faster                                                 |
| chameleon               | 9.06 ms                                                | 8.93 ms: 1.01x faster                                                |
| deepcopy_reduce         | 3.82 us                                                | 3.77 us: 1.01x faster                                                |
| hexiom                  | 9.53 ms                                                | 9.41 ms: 1.01x faster                                                |
| xml_etree_generate      | 94.2 ms                                                | 93.1 ms: 1.01x faster                                                |
| genshi_xml              | 63.3 ms                                                | 62.6 ms: 1.01x faster                                                |
| xml_etree_process       | 74.9 ms                                                | 74.1 ms: 1.01x faster                                                |
| deltablue               | 7.42 ms                                                | 7.35 ms: 1.01x faster                                                |
| xml_etree_iterparse     | 111 ms                                                 | 110 ms: 1.01x faster                                                 |
| async_generators        | 425 ms                                                 | 421 ms: 1.01x faster                                                 |
| coverage                | 72.8 ms                                                | 72.1 ms: 1.01x faster                                                |
| genshi_text             | 30.3 ms                                                | 30.1 ms: 1.01x faster                                                |
| go                      | 229 ms                                                 | 227 ms: 1.01x faster                                                 |
| pathlib                 | 20.0 ms                                                | 19.9 ms: 1.01x faster                                                |
| pprint_pformat          | 1.99 sec                                               | 1.97 sec: 1.01x faster                                               |
| unpickle_pure_python    | 300 us                                                 | 298 us: 1.01x faster                                                 |
| pidigits                | 190 ms                                                 | 188 ms: 1.01x faster                                                 |
| pickle_pure_python      | 455 us                                                 | 452 us: 1.01x faster                                                 |
| sqlglot_parse           | 2.06 ms                                                | 2.04 ms: 1.01x faster                                                |
| dulwich_log             | 75.9 ms                                                | 75.5 ms: 1.01x faster                                                |
| create_gc_cycles        | 1.67 ms                                                | 1.66 ms: 1.01x faster                                                |
| regex_compile           | 177 ms                                                 | 176 ms: 1.00x faster                                                 |
| 2to3                    | 336 ms                                                 | 335 ms: 1.00x faster                                                 |
| python_startup_no_site  | 5.82 ms                                                | 5.83 ms: 1.00x slower                                                |
| sqlglot_optimize        | 65.3 ms                                                | 65.5 ms: 1.00x slower                                                |
| pylint                  | 525 ms                                                 | 526 ms: 1.00x slower                                                 |
| python_startup          | 14.2 ms                                                | 14.2 ms: 1.00x slower                                                |
| json_loads              | 28.8 us                                                | 29.0 us: 1.01x slower                                                |
| comprehensions          | 26.8 us                                                | 27.0 us: 1.01x slower                                                |
| json_dumps              | 13.5 ms                                                | 13.6 ms: 1.01x slower                                                |
| thrift                  | 1.03 ms                                                | 1.04 ms: 1.01x slower                                                |
| pickle                  | 10.3 us                                                | 10.4 us: 1.01x slower                                                |
| scimark_sparse_mat_mult | 5.45 ms                                                | 5.50 ms: 1.01x slower                                                |
| docutils                | 3.17 sec                                               | 3.21 sec: 1.01x slower                                               |
| mdp                     | 2.82 sec                                               | 2.85 sec: 1.01x slower                                               |
| unpickle                | 14.1 us                                                | 14.3 us: 1.01x slower                                                |
| pycparser               | 1.50 sec                                               | 1.52 sec: 1.01x slower                                               |
| sqlalchemy_declarative  | 165 ms                                                 | 168 ms: 1.01x slower                                                 |
| regex_v8                | 25.0 ms                                                | 25.5 ms: 1.02x slower                                                |
| sympy_sum               | 185 ms                                                 | 188 ms: 1.02x slower                                                 |
| async_tree_none         | 717 ms                                                 | 732 ms: 1.02x slower                                                 |
| async_tree_memoization  | 854 ms                                                 | 873 ms: 1.02x slower                                                 |
| async_tree_io           | 1.77 sec                                               | 1.82 sec: 1.02x slower                                               |
| async_tree_cpu_io_mixed | 951 ms                                                 | 975 ms: 1.03x slower                                                 |
| tornado_http            | 127 ms                                                 | 131 ms: 1.03x slower                                                 |
| logging_format          | 8.91 us                                                | 9.16 us: 1.03x slower                                                |
| sqlite_synth            | 2.93 us                                                | 3.02 us: 1.03x slower                                                |
| flaskblogging           | 8.27 ms                                                | 8.53 ms: 1.03x slower                                                |
| telco                   | 6.54 ms                                                | 6.78 ms: 1.04x slower                                                |
| djangocms               | 35.9 us                                                | 37.3 us: 1.04x slower                                                |
| logging_simple          | 8.07 us                                                | 8.40 us: 1.04x slower                                                |
| unpack_sequence         | 64.7 ns                                                | 67.6 ns: 1.04x slower                                                |
| regex_effbot            | 3.23 ms                                                | 3.63 ms: 1.12x slower                                                |
| pickle_dict             | 27.3 us                                                | 33.7 us: 1.24x slower                                                |
| Geometric mean          | (ref)                                                  | 1.00x faster                                                         |

Benchmark hidden because not significant (18): sqlalchemy_imperative, html5lib, dask, sqlglot_transpile, raytrace, unpickle_list, logging_silent, django_template, xml_etree_parse, mako, pprint_safe_repr, sympy_expand, sympy_integrate, bench_mp_pool, mypy2, sympy_str, sqlglot_normalize, scimark_monte_carlo
Ignored benchmarks (4) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 99.70% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x
