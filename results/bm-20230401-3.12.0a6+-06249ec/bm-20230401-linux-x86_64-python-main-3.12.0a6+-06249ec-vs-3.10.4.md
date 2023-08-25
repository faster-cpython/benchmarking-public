
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 06249ec
- commit date: 2023-04-01
- overall geometric mean: 1.29x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230401-linux-x86_64-python-main-3.12.0a6+-06249ec |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 251 ms: 1.34x faster                                   |
| chameleon      | 9.06 ms                                                | 6.49 ms: 1.40x faster                                  |
| docutils       | 3.17 sec                                               | 2.56 sec: 1.24x faster                                 |
| html5lib       | 85.9 ms                                                | 61.4 ms: 1.40x faster                                  |
| tornado_http   | 127 ms                                                 | 91.1 ms: 1.40x faster                                  |
| Geometric mean | (ref)                                                  | 1.35x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230401-linux-x86_64-python-main-3.12.0a6+-06249ec |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 142 ms                                                 | 87.4 ms: 1.62x faster                                  |
| float          | 111 ms                                                 | 75.2 ms: 1.47x faster                                  |
| pidigits       | 190 ms                                                 | 188 ms: 1.01x faster                                   |
| Geometric mean | (ref)                                                  | 1.34x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230401-linux-x86_64-python-main-3.12.0a6+-06249ec |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 134 ms: 1.32x faster                                   |
| regex_v8       | 25.0 ms                                                | 21.9 ms: 1.14x faster                                  |
| regex_dna      | 222 ms                                                 | 207 ms: 1.07x faster                                   |
| regex_effbot   | 3.23 ms                                                | 3.54 ms: 1.10x slower                                  |
| Geometric mean | (ref)                                                  | 1.10x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230401-linux-x86_64-python-main-3.12.0a6+-06249ec |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 288 us: 1.58x faster                                   |
| unpickle_pure_python | 300 us                                                 | 202 us: 1.49x faster                                   |
| json_dumps           | 13.5 ms                                                | 9.43 ms: 1.44x faster                                  |
| xml_etree_process    | 74.9 ms                                                | 56.0 ms: 1.34x faster                                  |
| json_loads           | 28.8 us                                                | 24.3 us: 1.19x faster                                  |
| xml_etree_generate   | 94.2 ms                                                | 80.9 ms: 1.16x faster                                  |
| xml_etree_parse      | 163 ms                                                 | 149 ms: 1.09x faster                                   |
| xml_etree_iterparse  | 111 ms                                                 | 102 ms: 1.09x faster                                   |
| pickle_list          | 4.56 us                                                | 4.20 us: 1.08x faster                                  |
| unpickle             | 14.1 us                                                | 13.3 us: 1.06x faster                                  |
| unpickle_list        | 4.82 us                                                | 5.07 us: 1.05x slower                                  |
| pickle_dict          | 27.3 us                                                | 30.6 us: 1.12x slower                                  |
| Geometric mean       | (ref)                                                  | 1.16x faster                                           |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230401-linux-x86_64-python-main-3.12.0a6+-06249ec |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.83 ms: 1.60x faster                                  |
| python_startup_no_site | 5.82 ms                                                | 6.53 ms: 1.12x slower                                  |
| Geometric mean         | (ref)                                                  | 1.20x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230401-linux-x86_64-python-main-3.12.0a6+-06249ec |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 14.8 ms                                                | 10.1 ms: 1.45x faster                                  |
| genshi_text     | 30.3 ms                                                | 21.3 ms: 1.42x faster                                  |
| django_template | 45.9 ms                                                | 33.8 ms: 1.36x faster                                  |
| genshi_xml      | 63.3 ms                                                | 47.8 ms: 1.32x faster                                  |
| Geometric mean  | (ref)                                                  | 1.39x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230401-linux-x86_64-python-main-3.12.0a6+-06249ec |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| generators              | 76.8 ms                                                | 29.9 ms: 2.57x faster                                  |
| deltablue               | 7.42 ms                                                | 3.24 ms: 2.29x faster                                  |
| asyncio_tcp             | 925 ms                                                 | 505 ms: 1.83x faster                                   |
| logging_silent          | 175 ns                                                 | 96.6 ns: 1.81x faster                                  |
| scimark_sor             | 197 ms                                                 | 115 ms: 1.71x faster                                   |
| richards                | 74.9 ms                                                | 44.3 ms: 1.69x faster                                  |
| go                      | 229 ms                                                 | 140 ms: 1.63x faster                                   |
| raytrace                | 464 ms                                                 | 286 ms: 1.62x faster                                   |
| nbody                   | 142 ms                                                 | 87.4 ms: 1.62x faster                                  |
| crypto_pyaes            | 118 ms                                                 | 73.8 ms: 1.60x faster                                  |
| chaos                   | 106 ms                                                 | 66.2 ms: 1.60x faster                                  |
| python_startup          | 14.2 ms                                                | 8.83 ms: 1.60x faster                                  |
| pyflate                 | 673 ms                                                 | 420 ms: 1.60x faster                                   |
| scimark_monte_carlo     | 108 ms                                                 | 68.3 ms: 1.58x faster                                  |
| pickle_pure_python      | 455 us                                                 | 288 us: 1.58x faster                                   |
| hexiom                  | 9.53 ms                                                | 6.10 ms: 1.56x faster                                  |
| spectral_norm           | 150 ms                                                 | 96.5 ms: 1.55x faster                                  |
| scimark_lu              | 163 ms                                                 | 109 ms: 1.49x faster                                   |
| deepcopy_memo           | 52.3 us                                                | 35.1 us: 1.49x faster                                  |
| unpickle_pure_python    | 300 us                                                 | 202 us: 1.49x faster                                   |
| float                   | 111 ms                                                 | 75.2 ms: 1.47x faster                                  |
| mako                    | 14.8 ms                                                | 10.1 ms: 1.45x faster                                  |
| sqlglot_parse           | 2.06 ms                                                | 1.42 ms: 1.45x faster                                  |
| json_dumps              | 13.5 ms                                                | 9.43 ms: 1.44x faster                                  |
| sqlglot_transpile       | 2.45 ms                                                | 1.72 ms: 1.42x faster                                  |
| genshi_text             | 30.3 ms                                                | 21.3 ms: 1.42x faster                                  |
| logging_simple          | 8.07 us                                                | 5.72 us: 1.41x faster                                  |
| tornado_http            | 127 ms                                                 | 91.1 ms: 1.40x faster                                  |
| html5lib                | 85.9 ms                                                | 61.4 ms: 1.40x faster                                  |
| unpack_sequence         | 64.7 ns                                                | 46.4 ns: 1.40x faster                                  |
| pprint_pformat          | 1.99 sec                                               | 1.42 sec: 1.40x faster                                 |
| chameleon               | 9.06 ms                                                | 6.49 ms: 1.40x faster                                  |
| coroutines              | 31.8 ms                                                | 22.9 ms: 1.39x faster                                  |
| logging_format          | 8.91 us                                                | 6.42 us: 1.39x faster                                  |
| pprint_safe_repr        | 955 ms                                                 | 694 ms: 1.38x faster                                   |
| aiohttp                 | 1.38 ms                                                | 1.01 ms: 1.37x faster                                  |
| async_tree_io           | 1.77 sec                                               | 1.29 sec: 1.37x faster                                 |
| async_tree_none         | 717 ms                                                 | 525 ms: 1.37x faster                                   |
| django_template         | 45.9 ms                                                | 33.8 ms: 1.36x faster                                  |
| pycparser               | 1.50 sec                                               | 1.11 sec: 1.35x faster                                 |
| scimark_fft             | 424 ms                                                 | 314 ms: 1.35x faster                                   |
| gunicorn                | 1.46 ms                                                | 1.09 ms: 1.35x faster                                  |
| deepcopy                | 442 us                                                 | 330 us: 1.34x faster                                   |
| 2to3                    | 336 ms                                                 | 251 ms: 1.34x faster                                   |
| xml_etree_process       | 74.9 ms                                                | 56.0 ms: 1.34x faster                                  |
| genshi_xml              | 63.3 ms                                                | 47.8 ms: 1.32x faster                                  |
| regex_compile           | 177 ms                                                 | 134 ms: 1.32x faster                                   |
| thrift                  | 1.03 ms                                                | 783 us: 1.32x faster                                   |
| async_tree_memoization  | 854 ms                                                 | 657 ms: 1.30x faster                                   |
| sqlglot_normalize       | 135 ms                                                 | 105 ms: 1.29x faster                                   |
| mypy2                   | 428 ms                                                 | 333 ms: 1.29x faster                                   |
| async_tree_cpu_io_mixed | 951 ms                                                 | 741 ms: 1.28x faster                                   |
| sqlglot_optimize        | 65.3 ms                                                | 51.2 ms: 1.28x faster                                  |
| deepcopy_reduce         | 3.82 us                                                | 3.00 us: 1.27x faster                                  |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.29 ms: 1.27x faster                                  |
| fannkuch                | 486 ms                                                 | 385 ms: 1.26x faster                                   |
| docutils                | 3.17 sec                                               | 2.56 sec: 1.24x faster                                 |
| nqueens                 | 100 ms                                                 | 81.3 ms: 1.23x faster                                  |
| sqlalchemy_declarative  | 165 ms                                                 | 137 ms: 1.21x faster                                   |
| bench_thread_pool       | 947 us                                                 | 786 us: 1.21x faster                                   |
| sqlalchemy_imperative   | 21.2 ms                                                | 17.6 ms: 1.20x faster                                  |
| dulwich_log             | 75.9 ms                                                | 63.4 ms: 1.20x faster                                  |
| sympy_integrate         | 24.3 ms                                                | 20.4 ms: 1.19x faster                                  |
| json_loads              | 28.8 us                                                | 24.3 us: 1.19x faster                                  |
| sympy_expand            | 545 ms                                                 | 462 ms: 1.18x faster                                   |
| json                    | 5.42 ms                                                | 4.62 ms: 1.17x faster                                  |
| xml_etree_generate      | 94.2 ms                                                | 80.9 ms: 1.16x faster                                  |
| sympy_str               | 328 ms                                                 | 283 ms: 1.16x faster                                   |
| regex_v8                | 25.0 ms                                                | 21.9 ms: 1.14x faster                                  |
| comprehensions          | 26.8 us                                                | 23.9 us: 1.12x faster                                  |
| sqlite_synth            | 2.93 us                                                | 2.61 us: 1.12x faster                                  |
| create_gc_cycles        | 1.67 ms                                                | 1.49 ms: 1.12x faster                                  |
| mdp                     | 2.82 sec                                               | 2.53 sec: 1.12x faster                                 |
| meteor_contest          | 115 ms                                                 | 103 ms: 1.12x faster                                   |
| pathlib                 | 20.0 ms                                                | 18.0 ms: 1.11x faster                                  |
| sympy_sum               | 185 ms                                                 | 167 ms: 1.11x faster                                   |
| djangocms               | 35.9 us                                                | 32.5 us: 1.11x faster                                  |
| xml_etree_parse         | 163 ms                                                 | 149 ms: 1.09x faster                                   |
| xml_etree_iterparse     | 111 ms                                                 | 102 ms: 1.09x faster                                   |
| pickle_list             | 4.56 us                                                | 4.20 us: 1.08x faster                                  |
| regex_dna               | 222 ms                                                 | 207 ms: 1.07x faster                                   |
| gc_traversal            | 3.84 ms                                                | 3.60 ms: 1.07x faster                                  |
| unpickle                | 14.1 us                                                | 13.3 us: 1.06x faster                                  |
| async_generators        | 425 ms                                                 | 411 ms: 1.03x faster                                   |
| pidigits                | 190 ms                                                 | 188 ms: 1.01x faster                                   |
| unpickle_list           | 4.82 us                                                | 5.07 us: 1.05x slower                                  |
| regex_effbot            | 3.23 ms                                                | 3.54 ms: 1.10x slower                                  |
| python_startup_no_site  | 5.82 ms                                                | 6.53 ms: 1.12x slower                                  |
| pickle_dict             | 27.3 us                                                | 30.6 us: 1.12x slower                                  |
| dask                    | 423 ms                                                 | 512 ms: 1.21x slower                                   |
| coverage                | 72.8 ms                                                | 95.5 ms: 1.31x slower                                  |
| Geometric mean          | (ref)                                                  | 1.29x faster                                           |

Benchmark hidden because not significant (3): telco, bench_mp_pool, pickle
Ignored benchmarks (6) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.24x
