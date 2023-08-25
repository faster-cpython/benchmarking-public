
# Results vs. 3.10.4

- fork: python
- ref: 84e20c689a8b3b6cebfd
- machine: linux-x86_64
- commit hash: 84e20c6
- commit date: 2023-03-16
- overall geometric mean: 1.31x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230316-linux-x86_64-python-84e20c689a8b3b6cebfd-3.12.0a6+-84e20c6 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 250 ms: 1.35x faster                                                   |
| chameleon      | 9.06 ms                                                | 6.47 ms: 1.40x faster                                                  |
| docutils       | 3.17 sec                                               | 2.52 sec: 1.26x faster                                                 |
| html5lib       | 85.9 ms                                                | 60.7 ms: 1.42x faster                                                  |
| tornado_http   | 127 ms                                                 | 91.0 ms: 1.40x faster                                                  |
| Geometric mean | (ref)                                                  | 1.36x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230316-linux-x86_64-python-84e20c689a8b3b6cebfd-3.12.0a6+-84e20c6 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 88.8 ms: 1.59x faster                                                  |
| float          | 111 ms                                                 | 73.7 ms: 1.50x faster                                                  |
| pidigits       | 190 ms                                                 | 193 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                  | 1.33x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230316-linux-x86_64-python-84e20c689a8b3b6cebfd-3.12.0a6+-84e20c6 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 133 ms: 1.33x faster                                                   |
| regex_v8       | 25.0 ms                                                | 21.7 ms: 1.15x faster                                                  |
| regex_dna      | 222 ms                                                 | 200 ms: 1.11x faster                                                   |
| regex_effbot   | 3.23 ms                                                | 3.62 ms: 1.12x slower                                                  |
| Geometric mean | (ref)                                                  | 1.11x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230316-linux-x86_64-python-84e20c689a8b3b6cebfd-3.12.0a6+-84e20c6 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 280 us: 1.63x faster                                                   |
| unpickle_pure_python | 300 us                                                 | 197 us: 1.53x faster                                                   |
| json_dumps           | 13.5 ms                                                | 9.40 ms: 1.44x faster                                                  |
| xml_etree_process    | 74.9 ms                                                | 56.1 ms: 1.34x faster                                                  |
| json_loads           | 28.8 us                                                | 24.0 us: 1.20x faster                                                  |
| xml_etree_generate   | 94.2 ms                                                | 81.1 ms: 1.16x faster                                                  |
| xml_etree_iterparse  | 111 ms                                                 | 98.5 ms: 1.13x faster                                                  |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                                   |
| unpickle             | 14.1 us                                                | 13.2 us: 1.07x faster                                                  |
| pickle_list          | 4.56 us                                                | 4.28 us: 1.06x faster                                                  |
| pickle               | 10.3 us                                                | 10.5 us: 1.02x slower                                                  |
| unpickle_list        | 4.82 us                                                | 5.08 us: 1.05x slower                                                  |
| pickle_dict          | 27.3 us                                                | 31.0 us: 1.14x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.17x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230316-linux-x86_64-python-84e20c689a8b3b6cebfd-3.12.0a6+-84e20c6 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.93 ms: 1.58x faster                                                  |
| python_startup_no_site | 5.82 ms                                                | 6.52 ms: 1.12x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.19x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230316-linux-x86_64-python-84e20c689a8b3b6cebfd-3.12.0a6+-84e20c6 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 10.0 ms: 1.47x faster                                                  |
| genshi_text     | 30.3 ms                                                | 21.5 ms: 1.41x faster                                                  |
| django_template | 45.9 ms                                                | 33.5 ms: 1.37x faster                                                  |
| genshi_xml      | 63.3 ms                                                | 47.5 ms: 1.33x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.39x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230316-linux-x86_64-python-84e20c689a8b3b6cebfd-3.12.0a6+-84e20c6 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| generators              | 76.8 ms                                                | 29.5 ms: 2.60x faster                                                  |
| deltablue               | 7.42 ms                                                | 3.15 ms: 2.36x faster                                                  |
| logging_silent          | 175 ns                                                 | 93.4 ns: 1.87x faster                                                  |
| scimark_sor             | 197 ms                                                 | 106 ms: 1.85x faster                                                   |
| asyncio_tcp             | 925 ms                                                 | 507 ms: 1.82x faster                                                   |
| richards                | 74.9 ms                                                | 42.0 ms: 1.78x faster                                                  |
| go                      | 229 ms                                                 | 132 ms: 1.73x faster                                                   |
| raytrace                | 464 ms                                                 | 278 ms: 1.67x faster                                                   |
| scimark_monte_carlo     | 108 ms                                                 | 66.0 ms: 1.64x faster                                                  |
| pyflate                 | 673 ms                                                 | 412 ms: 1.63x faster                                                   |
| pickle_pure_python      | 455 us                                                 | 280 us: 1.63x faster                                                   |
| spectral_norm           | 150 ms                                                 | 92.3 ms: 1.63x faster                                                  |
| chaos                   | 106 ms                                                 | 66.0 ms: 1.61x faster                                                  |
| nbody                   | 142 ms                                                 | 88.8 ms: 1.59x faster                                                  |
| python_startup          | 14.2 ms                                                | 8.93 ms: 1.58x faster                                                  |
| deepcopy_memo           | 52.3 us                                                | 33.1 us: 1.58x faster                                                  |
| crypto_pyaes            | 118 ms                                                 | 75.1 ms: 1.58x faster                                                  |
| hexiom                  | 9.53 ms                                                | 6.10 ms: 1.56x faster                                                  |
| unpickle_pure_python    | 300 us                                                 | 197 us: 1.53x faster                                                   |
| scimark_lu              | 163 ms                                                 | 109 ms: 1.50x faster                                                   |
| float                   | 111 ms                                                 | 73.7 ms: 1.50x faster                                                  |
| mako                    | 14.8 ms                                                | 10.0 ms: 1.47x faster                                                  |
| sqlglot_parse           | 2.06 ms                                                | 1.40 ms: 1.47x faster                                                  |
| unpack_sequence         | 64.7 ns                                                | 44.2 ns: 1.46x faster                                                  |
| json_dumps              | 13.5 ms                                                | 9.40 ms: 1.44x faster                                                  |
| sqlglot_transpile       | 2.45 ms                                                | 1.70 ms: 1.44x faster                                                  |
| logging_simple          | 8.07 us                                                | 5.62 us: 1.43x faster                                                  |
| logging_format          | 8.91 us                                                | 6.22 us: 1.43x faster                                                  |
| pprint_pformat          | 1.99 sec                                               | 1.40 sec: 1.42x faster                                                 |
| html5lib                | 85.9 ms                                                | 60.7 ms: 1.42x faster                                                  |
| genshi_text             | 30.3 ms                                                | 21.5 ms: 1.41x faster                                                  |
| chameleon               | 9.06 ms                                                | 6.47 ms: 1.40x faster                                                  |
| pprint_safe_repr        | 955 ms                                                 | 682 ms: 1.40x faster                                                   |
| tornado_http            | 127 ms                                                 | 91.0 ms: 1.40x faster                                                  |
| async_tree_io           | 1.77 sec                                               | 1.27 sec: 1.40x faster                                                 |
| async_tree_memoization  | 854 ms                                                 | 614 ms: 1.39x faster                                                   |
| scimark_fft             | 424 ms                                                 | 306 ms: 1.39x faster                                                   |
| async_tree_none         | 717 ms                                                 | 518 ms: 1.39x faster                                                   |
| coroutines              | 31.8 ms                                                | 23.1 ms: 1.38x faster                                                  |
| aiohttp                 | 1.38 ms                                                | 1.01 ms: 1.37x faster                                                  |
| pycparser               | 1.50 sec                                               | 1.09 sec: 1.37x faster                                                 |
| django_template         | 45.9 ms                                                | 33.5 ms: 1.37x faster                                                  |
| deepcopy                | 442 us                                                 | 324 us: 1.36x faster                                                   |
| gunicorn                | 1.46 ms                                                | 1.08 ms: 1.35x faster                                                  |
| 2to3                    | 336 ms                                                 | 250 ms: 1.35x faster                                                   |
| thrift                  | 1.03 ms                                                | 769 us: 1.34x faster                                                   |
| xml_etree_process       | 74.9 ms                                                | 56.1 ms: 1.34x faster                                                  |
| genshi_xml              | 63.3 ms                                                | 47.5 ms: 1.33x faster                                                  |
| regex_compile           | 177 ms                                                 | 133 ms: 1.33x faster                                                   |
| fannkuch                | 486 ms                                                 | 367 ms: 1.32x faster                                                   |
| deepcopy_reduce         | 3.82 us                                                | 2.91 us: 1.31x faster                                                  |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.17 ms: 1.31x faster                                                  |
| sqlglot_normalize       | 135 ms                                                 | 104 ms: 1.30x faster                                                   |
| async_tree_cpu_io_mixed | 951 ms                                                 | 736 ms: 1.29x faster                                                   |
| mypy2                   | 428 ms                                                 | 332 ms: 1.29x faster                                                   |
| sqlglot_optimize        | 65.3 ms                                                | 51.0 ms: 1.28x faster                                                  |
| docutils                | 3.17 sec                                               | 2.52 sec: 1.26x faster                                                 |
| nqueens                 | 100 ms                                                 | 79.9 ms: 1.25x faster                                                  |
| sqlalchemy_declarative  | 165 ms                                                 | 136 ms: 1.22x faster                                                   |
| dulwich_log             | 75.9 ms                                                | 62.9 ms: 1.21x faster                                                  |
| sqlalchemy_imperative   | 21.2 ms                                                | 17.6 ms: 1.20x faster                                                  |
| json_loads              | 28.8 us                                                | 24.0 us: 1.20x faster                                                  |
| bench_thread_pool       | 947 us                                                 | 791 us: 1.20x faster                                                   |
| sympy_integrate         | 24.3 ms                                                | 20.4 ms: 1.19x faster                                                  |
| sympy_expand            | 545 ms                                                 | 459 ms: 1.19x faster                                                   |
| json                    | 5.42 ms                                                | 4.59 ms: 1.18x faster                                                  |
| mdp                     | 2.82 sec                                               | 2.43 sec: 1.16x faster                                                 |
| xml_etree_generate      | 94.2 ms                                                | 81.1 ms: 1.16x faster                                                  |
| sympy_str               | 328 ms                                                 | 283 ms: 1.16x faster                                                   |
| regex_v8                | 25.0 ms                                                | 21.7 ms: 1.15x faster                                                  |
| create_gc_cycles        | 1.67 ms                                                | 1.47 ms: 1.13x faster                                                  |
| xml_etree_iterparse     | 111 ms                                                 | 98.5 ms: 1.13x faster                                                  |
| pathlib                 | 20.0 ms                                                | 17.8 ms: 1.12x faster                                                  |
| sqlite_synth            | 2.93 us                                                | 2.62 us: 1.12x faster                                                  |
| comprehensions          | 26.8 us                                                | 24.1 us: 1.11x faster                                                  |
| meteor_contest          | 115 ms                                                 | 103 ms: 1.11x faster                                                   |
| sympy_sum               | 185 ms                                                 | 166 ms: 1.11x faster                                                   |
| regex_dna               | 222 ms                                                 | 200 ms: 1.11x faster                                                   |
| djangocms               | 35.9 us                                                | 32.5 us: 1.10x faster                                                  |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                                   |
| unpickle                | 14.1 us                                                | 13.2 us: 1.07x faster                                                  |
| pickle_list             | 4.56 us                                                | 4.28 us: 1.06x faster                                                  |
| gc_traversal            | 3.84 ms                                                | 3.67 ms: 1.05x faster                                                  |
| async_generators        | 425 ms                                                 | 410 ms: 1.04x faster                                                   |
| telco                   | 6.54 ms                                                | 6.46 ms: 1.01x faster                                                  |
| pidigits                | 190 ms                                                 | 193 ms: 1.01x slower                                                   |
| pickle                  | 10.3 us                                                | 10.5 us: 1.02x slower                                                  |
| unpickle_list           | 4.82 us                                                | 5.08 us: 1.05x slower                                                  |
| python_startup_no_site  | 5.82 ms                                                | 6.52 ms: 1.12x slower                                                  |
| regex_effbot            | 3.23 ms                                                | 3.62 ms: 1.12x slower                                                  |
| pickle_dict             | 27.3 us                                                | 31.0 us: 1.14x slower                                                  |
| dask                    | 423 ms                                                 | 500 ms: 1.18x slower                                                   |
| coverage                | 72.8 ms                                                | 94.2 ms: 1.29x slower                                                  |
| Geometric mean          | (ref)                                                  | 1.31x faster                                                           |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (6) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.30x
- 95% likely to have a speedup of 1.29x
- 99% likely to have a speedup of 1.26x
