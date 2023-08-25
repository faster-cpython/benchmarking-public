
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 206f05a
- commit date: 2023-01-14
- overall geometric mean: 1.31x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230114-linux-x86_64-python-main-3.12.0a4+-206f05a |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 252 ms: 1.33x faster                                   |
| chameleon      | 9.06 ms                                                | 6.35 ms: 1.43x faster                                  |
| docutils       | 3.17 sec                                               | 2.48 sec: 1.28x faster                                 |
| html5lib       | 85.9 ms                                                | 59.2 ms: 1.45x faster                                  |
| tornado_http   | 127 ms                                                 | 93.4 ms: 1.36x faster                                  |
| Geometric mean | (ref)                                                  | 1.37x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230114-linux-x86_64-python-main-3.12.0a4+-206f05a |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| float          | 111 ms                                                 | 72.2 ms: 1.53x faster                                  |
| nbody          | 142 ms                                                 | 95.1 ms: 1.49x faster                                  |
| pidigits       | 190 ms                                                 | 189 ms: 1.00x faster                                   |
| Geometric mean | (ref)                                                  | 1.32x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230114-linux-x86_64-python-main-3.12.0a4+-206f05a |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 130 ms: 1.36x faster                                   |
| regex_v8       | 25.0 ms                                                | 21.2 ms: 1.18x faster                                  |
| regex_dna      | 222 ms                                                 | 201 ms: 1.11x faster                                   |
| regex_effbot   | 3.23 ms                                                | 3.39 ms: 1.05x slower                                  |
| Geometric mean | (ref)                                                  | 1.14x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230114-linux-x86_64-python-main-3.12.0a4+-206f05a |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 281 us: 1.62x faster                                   |
| unpickle_pure_python | 300 us                                                 | 198 us: 1.52x faster                                   |
| json_dumps           | 13.5 ms                                                | 9.40 ms: 1.44x faster                                  |
| xml_etree_process    | 74.9 ms                                                | 53.5 ms: 1.40x faster                                  |
| xml_etree_generate   | 94.2 ms                                                | 76.6 ms: 1.23x faster                                  |
| json_loads           | 28.8 us                                                | 24.2 us: 1.19x faster                                  |
| pickle_list          | 4.56 us                                                | 4.08 us: 1.12x faster                                  |
| xml_etree_parse      | 163 ms                                                 | 149 ms: 1.10x faster                                   |
| unpickle             | 14.1 us                                                | 13.1 us: 1.08x faster                                  |
| xml_etree_iterparse  | 111 ms                                                 | 107 ms: 1.04x faster                                   |
| pickle               | 10.3 us                                                | 10.2 us: 1.01x faster                                  |
| unpickle_list        | 4.82 us                                                | 4.97 us: 1.03x slower                                  |
| pickle_dict          | 27.3 us                                                | 30.5 us: 1.12x slower                                  |
| Geometric mean       | (ref)                                                  | 1.18x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230114-linux-x86_64-python-main-3.12.0a4+-206f05a |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.95 ms: 1.58x faster                                  |
| python_startup_no_site | 5.82 ms                                                | 6.49 ms: 1.12x slower                                  |
| Geometric mean         | (ref)                                                  | 1.19x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230114-linux-x86_64-python-main-3.12.0a4+-206f05a |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| genshi_text     | 30.3 ms                                                | 20.2 ms: 1.50x faster                                  |
| mako            | 14.8 ms                                                | 9.90 ms: 1.49x faster                                  |
| django_template | 45.9 ms                                                | 32.0 ms: 1.43x faster                                  |
| genshi_xml      | 63.3 ms                                                | 47.1 ms: 1.34x faster                                  |
| Geometric mean  | (ref)                                                  | 1.44x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230114-linux-x86_64-python-main-3.12.0a4+-206f05a |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| deltablue               | 7.42 ms                                                | 3.23 ms: 2.30x faster                                  |
| logging_silent          | 175 ns                                                 | 90.6 ns: 1.93x faster                                  |
| scimark_sor             | 197 ms                                                 | 106 ms: 1.85x faster                                   |
| asyncio_tcp             | 925 ms                                                 | 505 ms: 1.83x faster                                   |
| richards                | 74.9 ms                                                | 41.1 ms: 1.82x faster                                  |
| go                      | 229 ms                                                 | 132 ms: 1.74x faster                                   |
| scimark_monte_carlo     | 108 ms                                                 | 63.8 ms: 1.70x faster                                  |
| pyflate                 | 673 ms                                                 | 398 ms: 1.69x faster                                   |
| raytrace                | 464 ms                                                 | 278 ms: 1.67x faster                                   |
| pickle_pure_python      | 455 us                                                 | 281 us: 1.62x faster                                   |
| spectral_norm           | 150 ms                                                 | 93.9 ms: 1.60x faster                                  |
| crypto_pyaes            | 118 ms                                                 | 74.3 ms: 1.59x faster                                  |
| python_startup          | 14.2 ms                                                | 8.95 ms: 1.58x faster                                  |
| hexiom                  | 9.53 ms                                                | 6.07 ms: 1.57x faster                                  |
| unpack_sequence         | 64.7 ns                                                | 41.3 ns: 1.57x faster                                  |
| chaos                   | 106 ms                                                 | 67.9 ms: 1.56x faster                                  |
| deepcopy_memo           | 52.3 us                                                | 33.7 us: 1.55x faster                                  |
| scimark_lu              | 163 ms                                                 | 106 ms: 1.53x faster                                   |
| float                   | 111 ms                                                 | 72.2 ms: 1.53x faster                                  |
| unpickle_pure_python    | 300 us                                                 | 198 us: 1.52x faster                                   |
| genshi_text             | 30.3 ms                                                | 20.2 ms: 1.50x faster                                  |
| mako                    | 14.8 ms                                                | 9.90 ms: 1.49x faster                                  |
| nbody                   | 142 ms                                                 | 95.1 ms: 1.49x faster                                  |
| sqlglot_parse           | 2.06 ms                                                | 1.39 ms: 1.48x faster                                  |
| sqlglot_transpile       | 2.45 ms                                                | 1.67 ms: 1.46x faster                                  |
| html5lib                | 85.9 ms                                                | 59.2 ms: 1.45x faster                                  |
| pprint_pformat          | 1.99 sec                                               | 1.38 sec: 1.44x faster                                 |
| json_dumps              | 13.5 ms                                                | 9.40 ms: 1.44x faster                                  |
| logging_simple          | 8.07 us                                                | 5.61 us: 1.44x faster                                  |
| logging_format          | 8.91 us                                                | 6.20 us: 1.44x faster                                  |
| django_template         | 45.9 ms                                                | 32.0 ms: 1.43x faster                                  |
| chameleon               | 9.06 ms                                                | 6.35 ms: 1.43x faster                                  |
| pprint_safe_repr        | 955 ms                                                 | 670 ms: 1.42x faster                                   |
| xml_etree_process       | 74.9 ms                                                | 53.5 ms: 1.40x faster                                  |
| pycparser               | 1.50 sec                                               | 1.08 sec: 1.39x faster                                 |
| aiohttp                 | 1.38 ms                                                | 998 us: 1.39x faster                                   |
| scimark_fft             | 424 ms                                                 | 306 ms: 1.38x faster                                   |
| thrift                  | 1.03 ms                                                | 749 us: 1.38x faster                                   |
| gunicorn                | 1.46 ms                                                | 1.07 ms: 1.37x faster                                  |
| async_tree_none         | 717 ms                                                 | 524 ms: 1.37x faster                                   |
| tornado_http            | 127 ms                                                 | 93.4 ms: 1.36x faster                                  |
| regex_compile           | 177 ms                                                 | 130 ms: 1.36x faster                                   |
| async_tree_memoization  | 854 ms                                                 | 627 ms: 1.36x faster                                   |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.05 ms: 1.35x faster                                  |
| async_tree_io           | 1.77 sec                                               | 1.32 sec: 1.34x faster                                 |
| genshi_xml              | 63.3 ms                                                | 47.1 ms: 1.34x faster                                  |
| 2to3                    | 336 ms                                                 | 252 ms: 1.33x faster                                   |
| deepcopy                | 442 us                                                 | 331 us: 1.33x faster                                   |
| fannkuch                | 486 ms                                                 | 371 ms: 1.31x faster                                   |
| deepcopy_reduce         | 3.82 us                                                | 2.94 us: 1.30x faster                                  |
| sqlglot_normalize       | 135 ms                                                 | 104 ms: 1.30x faster                                   |
| async_tree_cpu_io_mixed | 951 ms                                                 | 732 ms: 1.30x faster                                   |
| sqlglot_optimize        | 65.3 ms                                                | 50.5 ms: 1.29x faster                                  |
| docutils                | 3.17 sec                                               | 2.48 sec: 1.28x faster                                 |
| coroutines              | 31.8 ms                                                | 25.2 ms: 1.26x faster                                  |
| nqueens                 | 100 ms                                                 | 80.8 ms: 1.24x faster                                  |
| xml_etree_generate      | 94.2 ms                                                | 76.6 ms: 1.23x faster                                  |
| dulwich_log             | 75.9 ms                                                | 61.9 ms: 1.23x faster                                  |
| bench_thread_pool       | 947 us                                                 | 779 us: 1.22x faster                                   |
| json_loads              | 28.8 us                                                | 24.2 us: 1.19x faster                                  |
| sympy_integrate         | 24.3 ms                                                | 20.4 ms: 1.19x faster                                  |
| sympy_expand            | 545 ms                                                 | 459 ms: 1.19x faster                                   |
| async_generators        | 425 ms                                                 | 358 ms: 1.19x faster                                   |
| regex_v8                | 25.0 ms                                                | 21.2 ms: 1.18x faster                                  |
| sympy_str               | 328 ms                                                 | 283 ms: 1.16x faster                                   |
| json                    | 5.42 ms                                                | 4.68 ms: 1.16x faster                                  |
| create_gc_cycles        | 1.67 ms                                                | 1.47 ms: 1.14x faster                                  |
| sqlite_synth            | 2.93 us                                                | 2.59 us: 1.13x faster                                  |
| sympy_sum               | 185 ms                                                 | 164 ms: 1.13x faster                                   |
| pathlib                 | 20.0 ms                                                | 17.9 ms: 1.12x faster                                  |
| pickle_list             | 4.56 us                                                | 4.08 us: 1.12x faster                                  |
| djangocms               | 35.9 us                                                | 32.3 us: 1.11x faster                                  |
| regex_dna               | 222 ms                                                 | 201 ms: 1.11x faster                                   |
| meteor_contest          | 115 ms                                                 | 105 ms: 1.10x faster                                   |
| xml_etree_parse         | 163 ms                                                 | 149 ms: 1.10x faster                                   |
| unpickle                | 14.1 us                                                | 13.1 us: 1.08x faster                                  |
| mdp                     | 2.82 sec                                               | 2.69 sec: 1.05x faster                                 |
| telco                   | 6.54 ms                                                | 6.24 ms: 1.05x faster                                  |
| xml_etree_iterparse     | 111 ms                                                 | 107 ms: 1.04x faster                                   |
| gc_traversal            | 3.84 ms                                                | 3.81 ms: 1.01x faster                                  |
| pickle                  | 10.3 us                                                | 10.2 us: 1.01x faster                                  |
| pidigits                | 190 ms                                                 | 189 ms: 1.00x faster                                   |
| generators              | 76.8 ms                                                | 78.8 ms: 1.03x slower                                  |
| unpickle_list           | 4.82 us                                                | 4.97 us: 1.03x slower                                  |
| regex_effbot            | 3.23 ms                                                | 3.39 ms: 1.05x slower                                  |
| python_startup_no_site  | 5.82 ms                                                | 6.49 ms: 1.12x slower                                  |
| pickle_dict             | 27.3 us                                                | 30.5 us: 1.12x slower                                  |
| dask                    | 423 ms                                                 | 494 ms: 1.17x slower                                   |
| coverage                | 72.8 ms                                                | 98.6 ms: 1.35x slower                                  |
| Geometric mean          | (ref)                                                  | 1.31x faster                                           |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, comprehensions, flaskblogging, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230114-3.12.0a4+-206f05a/bm-20230114-linux-x86_64-python-main-3.12.0a4+-206f05a.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.30x
- 95% likely to have a speedup of 1.29x
- 99% likely to have a speedup of 1.26x
