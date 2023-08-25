
# Results vs. 3.10.4

- fork: python
- ref: v3.11.0b2
- machine: linux-x86_64
- commit hash: 72f00f4
- commit date: 2022-05-30
- overall geometric mean: 1.26x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220530-linux-x86_64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 256 ms: 1.31x faster                                       |
| chameleon      | 9.06 ms                                                | 6.62 ms: 1.37x faster                                      |
| docutils       | 3.17 sec                                               | 2.56 sec: 1.24x faster                                     |
| html5lib       | 85.9 ms                                                | 63.7 ms: 1.35x faster                                      |
| tornado_http   | 127 ms                                                 | 94.9 ms: 1.34x faster                                      |
| Geometric mean | (ref)                                                  | 1.32x faster                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220530-linux-x86_64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| nbody          | 142 ms                                                 | 92.0 ms: 1.54x faster                                      |
| float          | 111 ms                                                 | 74.4 ms: 1.49x faster                                      |
| pidigits       | 190 ms                                                 | 199 ms: 1.05x slower                                       |
| Geometric mean | (ref)                                                  | 1.30x faster                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220530-linux-x86_64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 138 ms: 1.29x faster                                       |
| regex_v8       | 25.0 ms                                                | 22.0 ms: 1.14x faster                                      |
| regex_dna      | 222 ms                                                 | 196 ms: 1.13x faster                                       |
| regex_effbot   | 3.23 ms                                                | 3.11 ms: 1.04x faster                                      |
| Geometric mean | (ref)                                                  | 1.15x faster                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220530-linux-x86_64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 305 us: 1.49x faster                                       |
| xml_etree_process    | 74.9 ms                                                | 53.4 ms: 1.40x faster                                      |
| unpickle_pure_python | 300 us                                                 | 227 us: 1.33x faster                                       |
| xml_etree_generate   | 94.2 ms                                                | 76.1 ms: 1.24x faster                                      |
| json_loads           | 28.8 us                                                | 25.0 us: 1.15x faster                                      |
| pickle               | 10.3 us                                                | 9.44 us: 1.09x faster                                      |
| unpickle             | 14.1 us                                                | 13.3 us: 1.06x faster                                      |
| json_dumps           | 13.5 ms                                                | 12.8 ms: 1.06x faster                                      |
| pickle_list          | 4.56 us                                                | 4.30 us: 1.06x faster                                      |
| xml_etree_iterparse  | 111 ms                                                 | 105 ms: 1.06x faster                                       |
| pickle_dict          | 27.3 us                                                | 26.4 us: 1.03x faster                                      |
| xml_etree_parse      | 163 ms                                                 | 159 ms: 1.03x faster                                       |
| unpickle_list        | 4.82 us                                                | 5.00 us: 1.04x slower                                      |
| Geometric mean       | (ref)                                                  | 1.14x faster                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220530-linux-x86_64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.49 ms: 1.67x faster                                      |
| python_startup_no_site | 5.82 ms                                                | 5.99 ms: 1.03x slower                                      |
| Geometric mean         | (ref)                                                  | 1.27x faster                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220530-linux-x86_64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.96 ms: 1.48x faster                                      |
| django_template | 45.9 ms                                                | 32.6 ms: 1.41x faster                                      |
| genshi_text     | 30.3 ms                                                | 21.5 ms: 1.41x faster                                      |
| genshi_xml      | 63.3 ms                                                | 52.4 ms: 1.21x faster                                      |
| Geometric mean  | (ref)                                                  | 1.37x faster                                               |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20220530-linux-x86_64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| deltablue               | 7.42 ms                                                | 3.84 ms: 1.93x faster                                      |
| scimark_sor             | 197 ms                                                 | 115 ms: 1.71x faster                                       |
| logging_silent          | 175 ns                                                 | 103 ns: 1.70x faster                                       |
| richards                | 74.9 ms                                                | 44.5 ms: 1.68x faster                                      |
| python_startup          | 14.2 ms                                                | 8.49 ms: 1.67x faster                                      |
| go                      | 229 ms                                                 | 139 ms: 1.65x faster                                       |
| scimark_monte_carlo     | 108 ms                                                 | 66.0 ms: 1.64x faster                                      |
| pyflate                 | 673 ms                                                 | 413 ms: 1.63x faster                                       |
| raytrace                | 464 ms                                                 | 287 ms: 1.62x faster                                       |
| crypto_pyaes            | 118 ms                                                 | 74.8 ms: 1.58x faster                                      |
| chaos                   | 106 ms                                                 | 67.3 ms: 1.58x faster                                      |
| spectral_norm           | 150 ms                                                 | 97.3 ms: 1.54x faster                                      |
| nbody                   | 142 ms                                                 | 92.0 ms: 1.54x faster                                      |
| hexiom                  | 9.53 ms                                                | 6.27 ms: 1.52x faster                                      |
| scimark_lu              | 163 ms                                                 | 109 ms: 1.50x faster                                       |
| pickle_pure_python      | 455 us                                                 | 305 us: 1.49x faster                                       |
| float                   | 111 ms                                                 | 74.4 ms: 1.49x faster                                      |
| mako                    | 14.8 ms                                                | 9.96 ms: 1.48x faster                                      |
| deepcopy_memo           | 52.3 us                                                | 35.9 us: 1.46x faster                                      |
| django_template         | 45.9 ms                                                | 32.6 ms: 1.41x faster                                      |
| genshi_text             | 30.3 ms                                                | 21.5 ms: 1.41x faster                                      |
| logging_simple          | 8.07 us                                                | 5.74 us: 1.41x faster                                      |
| xml_etree_process       | 74.9 ms                                                | 53.4 ms: 1.40x faster                                      |
| logging_format          | 8.91 us                                                | 6.34 us: 1.40x faster                                      |
| unpack_sequence         | 64.7 ns                                                | 46.2 ns: 1.40x faster                                      |
| thrift                  | 1.03 ms                                                | 750 us: 1.38x faster                                       |
| pprint_pformat          | 1.99 sec                                               | 1.45 sec: 1.37x faster                                     |
| chameleon               | 9.06 ms                                                | 6.62 ms: 1.37x faster                                      |
| pprint_safe_repr        | 955 ms                                                 | 699 ms: 1.37x faster                                       |
| async_tree_none         | 717 ms                                                 | 526 ms: 1.36x faster                                       |
| async_tree_memoization  | 854 ms                                                 | 628 ms: 1.36x faster                                       |
| async_tree_io           | 1.77 sec                                               | 1.31 sec: 1.36x faster                                     |
| html5lib                | 85.9 ms                                                | 63.7 ms: 1.35x faster                                      |
| tornado_http            | 127 ms                                                 | 94.9 ms: 1.34x faster                                      |
| unpickle_pure_python    | 300 us                                                 | 227 us: 1.33x faster                                       |
| pycparser               | 1.50 sec                                               | 1.14 sec: 1.32x faster                                     |
| 2to3                    | 336 ms                                                 | 256 ms: 1.31x faster                                       |
| aiohttp                 | 1.38 ms                                                | 1.06 ms: 1.31x faster                                      |
| deepcopy                | 442 us                                                 | 340 us: 1.30x faster                                       |
| gunicorn                | 1.46 ms                                                | 1.13 ms: 1.30x faster                                      |
| scimark_fft             | 424 ms                                                 | 329 ms: 1.29x faster                                       |
| regex_compile           | 177 ms                                                 | 138 ms: 1.29x faster                                       |
| async_tree_cpu_io_mixed | 951 ms                                                 | 743 ms: 1.28x faster                                       |
| deepcopy_reduce         | 3.82 us                                                | 3.03 us: 1.26x faster                                      |
| docutils                | 3.17 sec                                               | 2.56 sec: 1.24x faster                                     |
| xml_etree_generate      | 94.2 ms                                                | 76.1 ms: 1.24x faster                                      |
| coroutines              | 31.8 ms                                                | 25.7 ms: 1.24x faster                                      |
| sqlglot_normalize       | 135 ms                                                 | 110 ms: 1.23x faster                                       |
| sqlglot_optimize        | 65.3 ms                                                | 53.9 ms: 1.21x faster                                      |
| sqlalchemy_declarative  | 165 ms                                                 | 137 ms: 1.21x faster                                       |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.51 ms: 1.21x faster                                      |
| genshi_xml              | 63.3 ms                                                | 52.4 ms: 1.21x faster                                      |
| fannkuch                | 486 ms                                                 | 403 ms: 1.20x faster                                       |
| dulwich_log             | 75.9 ms                                                | 63.1 ms: 1.20x faster                                      |
| async_generators        | 425 ms                                                 | 354 ms: 1.20x faster                                       |
| sqlglot_transpile       | 2.45 ms                                                | 2.05 ms: 1.20x faster                                      |
| nqueens                 | 100 ms                                                 | 84.2 ms: 1.19x faster                                      |
| sqlalchemy_imperative   | 21.2 ms                                                | 17.9 ms: 1.18x faster                                      |
| sympy_integrate         | 24.3 ms                                                | 20.7 ms: 1.17x faster                                      |
| sqlglot_parse           | 2.06 ms                                                | 1.75 ms: 1.17x faster                                      |
| bench_thread_pool       | 947 us                                                 | 811 us: 1.17x faster                                       |
| sqlite_synth            | 2.93 us                                                | 2.52 us: 1.16x faster                                      |
| json_loads              | 28.8 us                                                | 25.0 us: 1.15x faster                                      |
| dask                    | 423 ms                                                 | 368 ms: 1.15x faster                                       |
| sympy_expand            | 545 ms                                                 | 475 ms: 1.15x faster                                       |
| sympy_sum               | 185 ms                                                 | 161 ms: 1.14x faster                                       |
| sympy_str               | 328 ms                                                 | 288 ms: 1.14x faster                                       |
| regex_v8                | 25.0 ms                                                | 22.0 ms: 1.14x faster                                      |
| json                    | 5.42 ms                                                | 4.75 ms: 1.14x faster                                      |
| pylint                  | 525 ms                                                 | 462 ms: 1.14x faster                                       |
| regex_dna               | 222 ms                                                 | 196 ms: 1.13x faster                                       |
| pathlib                 | 20.0 ms                                                | 18.1 ms: 1.11x faster                                      |
| create_gc_cycles        | 1.67 ms                                                | 1.51 ms: 1.11x faster                                      |
| meteor_contest          | 115 ms                                                 | 104 ms: 1.10x faster                                       |
| pickle                  | 10.3 us                                                | 9.44 us: 1.09x faster                                      |
| djangocms               | 35.9 us                                                | 33.5 us: 1.07x faster                                      |
| unpickle                | 14.1 us                                                | 13.3 us: 1.06x faster                                      |
| json_dumps              | 13.5 ms                                                | 12.8 ms: 1.06x faster                                      |
| pickle_list             | 4.56 us                                                | 4.30 us: 1.06x faster                                      |
| xml_etree_iterparse     | 111 ms                                                 | 105 ms: 1.06x faster                                       |
| mdp                     | 2.82 sec                                               | 2.67 sec: 1.06x faster                                     |
| asyncio_tcp             | 925 ms                                                 | 890 ms: 1.04x faster                                       |
| regex_effbot            | 3.23 ms                                                | 3.11 ms: 1.04x faster                                      |
| comprehensions          | 26.8 us                                                | 26.0 us: 1.03x faster                                      |
| generators              | 76.8 ms                                                | 74.4 ms: 1.03x faster                                      |
| pickle_dict             | 27.3 us                                                | 26.4 us: 1.03x faster                                      |
| xml_etree_parse         | 163 ms                                                 | 159 ms: 1.03x faster                                       |
| bench_mp_pool           | 24.0 ms                                                | 24.0 ms: 1.00x slower                                      |
| python_startup_no_site  | 5.82 ms                                                | 5.99 ms: 1.03x slower                                      |
| unpickle_list           | 4.82 us                                                | 5.00 us: 1.04x slower                                      |
| pidigits                | 190 ms                                                 | 199 ms: 1.05x slower                                       |
| gc_traversal            | 3.84 ms                                                | 4.21 ms: 1.10x slower                                      |
| Geometric mean          | (ref)                                                  | 1.26x faster                                               |

Benchmark hidden because not significant (2): mypy2, telco
Ignored benchmarks (6) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, coverage, flaskblogging, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.22x
- 95% likely to have a speedup of 1.21x
- 99% likely to have a speedup of 1.20x
