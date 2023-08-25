
# Results vs. 3.10.4

- fork: python
- ref: 144aaa74bbd77aee822e
- machine: linux-x86_64
- commit hash: 144aaa7
- commit date: 2023-02-04
- overall geometric mean: 1.30x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230204-linux-x86_64-python-144aaa74bbd77aee822e-3.12.0a4+-144aaa7 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 253 ms: 1.33x faster                                                   |
| chameleon      | 9.06 ms                                                | 6.25 ms: 1.45x faster                                                  |
| docutils       | 3.17 sec                                               | 2.50 sec: 1.27x faster                                                 |
| html5lib       | 85.9 ms                                                | 59.6 ms: 1.44x faster                                                  |
| tornado_http   | 127 ms                                                 | 93.8 ms: 1.36x faster                                                  |
| Geometric mean | (ref)                                                  | 1.37x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230204-linux-x86_64-python-144aaa74bbd77aee822e-3.12.0a4+-144aaa7 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 111 ms                                                 | 72.4 ms: 1.53x faster                                                  |
| nbody          | 142 ms                                                 | 97.5 ms: 1.45x faster                                                  |
| pidigits       | 190 ms                                                 | 193 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                  | 1.30x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230204-linux-x86_64-python-144aaa74bbd77aee822e-3.12.0a4+-144aaa7 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 126 ms: 1.40x faster                                                   |
| regex_v8       | 25.0 ms                                                | 22.2 ms: 1.13x faster                                                  |
| regex_dna      | 222 ms                                                 | 210 ms: 1.06x faster                                                   |
| regex_effbot   | 3.23 ms                                                | 3.63 ms: 1.12x slower                                                  |
| Geometric mean | (ref)                                                  | 1.10x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230204-linux-x86_64-python-144aaa74bbd77aee822e-3.12.0a4+-144aaa7 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 281 us: 1.62x faster                                                   |
| unpickle_pure_python | 300 us                                                 | 197 us: 1.52x faster                                                   |
| json_dumps           | 13.5 ms                                                | 9.48 ms: 1.43x faster                                                  |
| xml_etree_process    | 74.9 ms                                                | 53.5 ms: 1.40x faster                                                  |
| xml_etree_generate   | 94.2 ms                                                | 77.4 ms: 1.22x faster                                                  |
| json_loads           | 28.8 us                                                | 24.1 us: 1.19x faster                                                  |
| xml_etree_parse      | 163 ms                                                 | 147 ms: 1.11x faster                                                   |
| xml_etree_iterparse  | 111 ms                                                 | 102 ms: 1.09x faster                                                   |
| pickle_list          | 4.56 us                                                | 4.24 us: 1.08x faster                                                  |
| pickle               | 10.3 us                                                | 10.1 us: 1.02x faster                                                  |
| unpickle             | 14.1 us                                                | 14.9 us: 1.05x slower                                                  |
| unpickle_list        | 4.82 us                                                | 5.12 us: 1.06x slower                                                  |
| pickle_dict          | 27.3 us                                                | 31.9 us: 1.17x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.16x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230204-linux-x86_64-python-144aaa74bbd77aee822e-3.12.0a4+-144aaa7 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.93 ms: 1.59x faster                                                  |
| python_startup_no_site | 5.82 ms                                                | 6.46 ms: 1.11x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.19x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230204-linux-x86_64-python-144aaa74bbd77aee822e-3.12.0a4+-144aaa7 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.79 ms: 1.51x faster                                                  |
| genshi_text     | 30.3 ms                                                | 20.5 ms: 1.48x faster                                                  |
| django_template | 45.9 ms                                                | 32.6 ms: 1.41x faster                                                  |
| genshi_xml      | 63.3 ms                                                | 47.0 ms: 1.35x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.43x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230204-linux-x86_64-python-144aaa74bbd77aee822e-3.12.0a4+-144aaa7 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| deltablue               | 7.42 ms                                                | 3.21 ms: 2.31x faster                                                  |
| logging_silent          | 175 ns                                                 | 92.3 ns: 1.90x faster                                                  |
| asyncio_tcp             | 925 ms                                                 | 491 ms: 1.88x faster                                                   |
| scimark_sor             | 197 ms                                                 | 109 ms: 1.81x faster                                                   |
| richards                | 74.9 ms                                                | 42.3 ms: 1.77x faster                                                  |
| go                      | 229 ms                                                 | 134 ms: 1.71x faster                                                   |
| pyflate                 | 673 ms                                                 | 404 ms: 1.67x faster                                                   |
| raytrace                | 464 ms                                                 | 282 ms: 1.64x faster                                                   |
| crypto_pyaes            | 118 ms                                                 | 72.1 ms: 1.64x faster                                                  |
| chaos                   | 106 ms                                                 | 65.0 ms: 1.64x faster                                                  |
| pickle_pure_python      | 455 us                                                 | 281 us: 1.62x faster                                                   |
| scimark_monte_carlo     | 108 ms                                                 | 67.2 ms: 1.61x faster                                                  |
| python_startup          | 14.2 ms                                                | 8.93 ms: 1.59x faster                                                  |
| hexiom                  | 9.53 ms                                                | 6.05 ms: 1.57x faster                                                  |
| unpack_sequence         | 64.7 ns                                                | 41.7 ns: 1.55x faster                                                  |
| spectral_norm           | 150 ms                                                 | 97.2 ms: 1.54x faster                                                  |
| deepcopy_memo           | 52.3 us                                                | 34.2 us: 1.53x faster                                                  |
| float                   | 111 ms                                                 | 72.4 ms: 1.53x faster                                                  |
| unpickle_pure_python    | 300 us                                                 | 197 us: 1.52x faster                                                   |
| mako                    | 14.8 ms                                                | 9.79 ms: 1.51x faster                                                  |
| scimark_lu              | 163 ms                                                 | 110 ms: 1.49x faster                                                   |
| genshi_text             | 30.3 ms                                                | 20.5 ms: 1.48x faster                                                  |
| nbody                   | 142 ms                                                 | 97.5 ms: 1.45x faster                                                  |
| chameleon               | 9.06 ms                                                | 6.25 ms: 1.45x faster                                                  |
| pprint_pformat          | 1.99 sec                                               | 1.37 sec: 1.45x faster                                                 |
| sqlglot_parse           | 2.06 ms                                                | 1.43 ms: 1.44x faster                                                  |
| html5lib                | 85.9 ms                                                | 59.6 ms: 1.44x faster                                                  |
| json_dumps              | 13.5 ms                                                | 9.48 ms: 1.43x faster                                                  |
| pprint_safe_repr        | 955 ms                                                 | 669 ms: 1.43x faster                                                   |
| sqlglot_transpile       | 2.45 ms                                                | 1.72 ms: 1.43x faster                                                  |
| logging_format          | 8.91 us                                                | 6.29 us: 1.42x faster                                                  |
| logging_simple          | 8.07 us                                                | 5.71 us: 1.41x faster                                                  |
| django_template         | 45.9 ms                                                | 32.6 ms: 1.41x faster                                                  |
| regex_compile           | 177 ms                                                 | 126 ms: 1.40x faster                                                   |
| xml_etree_process       | 74.9 ms                                                | 53.5 ms: 1.40x faster                                                  |
| aiohttp                 | 1.38 ms                                                | 997 us: 1.39x faster                                                   |
| deepcopy                | 442 us                                                 | 323 us: 1.37x faster                                                   |
| scimark_fft             | 424 ms                                                 | 310 ms: 1.37x faster                                                   |
| thrift                  | 1.03 ms                                                | 758 us: 1.36x faster                                                   |
| async_tree_none         | 717 ms                                                 | 526 ms: 1.36x faster                                                   |
| tornado_http            | 127 ms                                                 | 93.8 ms: 1.36x faster                                                  |
| gunicorn                | 1.46 ms                                                | 1.08 ms: 1.35x faster                                                  |
| genshi_xml              | 63.3 ms                                                | 47.0 ms: 1.35x faster                                                  |
| async_tree_io           | 1.77 sec                                               | 1.32 sec: 1.34x faster                                                 |
| fannkuch                | 486 ms                                                 | 363 ms: 1.34x faster                                                   |
| 2to3                    | 336 ms                                                 | 253 ms: 1.33x faster                                                   |
| pycparser               | 1.50 sec                                               | 1.14 sec: 1.32x faster                                                 |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.15 ms: 1.31x faster                                                  |
| async_tree_memoization  | 854 ms                                                 | 652 ms: 1.31x faster                                                   |
| deepcopy_reduce         | 3.82 us                                                | 2.94 us: 1.30x faster                                                  |
| sqlglot_normalize       | 135 ms                                                 | 105 ms: 1.29x faster                                                   |
| sqlglot_optimize        | 65.3 ms                                                | 50.8 ms: 1.29x faster                                                  |
| nqueens                 | 100 ms                                                 | 78.3 ms: 1.28x faster                                                  |
| docutils                | 3.17 sec                                               | 2.50 sec: 1.27x faster                                                 |
| async_tree_cpu_io_mixed | 951 ms                                                 | 760 ms: 1.25x faster                                                   |
| coroutines              | 31.8 ms                                                | 25.7 ms: 1.24x faster                                                  |
| sympy_integrate         | 24.3 ms                                                | 19.7 ms: 1.23x faster                                                  |
| xml_etree_generate      | 94.2 ms                                                | 77.4 ms: 1.22x faster                                                  |
| sympy_str               | 328 ms                                                 | 270 ms: 1.22x faster                                                   |
| dulwich_log             | 75.9 ms                                                | 62.8 ms: 1.21x faster                                                  |
| async_generators        | 425 ms                                                 | 352 ms: 1.21x faster                                                   |
| bench_thread_pool       | 947 us                                                 | 785 us: 1.21x faster                                                   |
| sympy_expand            | 545 ms                                                 | 455 ms: 1.20x faster                                                   |
| json_loads              | 28.8 us                                                | 24.1 us: 1.19x faster                                                  |
| sympy_sum               | 185 ms                                                 | 156 ms: 1.19x faster                                                   |
| json                    | 5.42 ms                                                | 4.72 ms: 1.15x faster                                                  |
| create_gc_cycles        | 1.67 ms                                                | 1.46 ms: 1.14x faster                                                  |
| sqlite_synth            | 2.93 us                                                | 2.60 us: 1.13x faster                                                  |
| regex_v8                | 25.0 ms                                                | 22.2 ms: 1.13x faster                                                  |
| djangocms               | 35.9 us                                                | 32.2 us: 1.12x faster                                                  |
| pathlib                 | 20.0 ms                                                | 18.0 ms: 1.11x faster                                                  |
| xml_etree_parse         | 163 ms                                                 | 147 ms: 1.11x faster                                                   |
| meteor_contest          | 115 ms                                                 | 103 ms: 1.11x faster                                                   |
| xml_etree_iterparse     | 111 ms                                                 | 102 ms: 1.09x faster                                                   |
| mdp                     | 2.82 sec                                               | 2.61 sec: 1.08x faster                                                 |
| pickle_list             | 4.56 us                                                | 4.24 us: 1.08x faster                                                  |
| regex_dna               | 222 ms                                                 | 210 ms: 1.06x faster                                                   |
| gc_traversal            | 3.84 ms                                                | 3.65 ms: 1.05x faster                                                  |
| pickle                  | 10.3 us                                                | 10.1 us: 1.02x faster                                                  |
| pidigits                | 190 ms                                                 | 193 ms: 1.01x slower                                                   |
| unpickle                | 14.1 us                                                | 14.9 us: 1.05x slower                                                  |
| unpickle_list           | 4.82 us                                                | 5.12 us: 1.06x slower                                                  |
| python_startup_no_site  | 5.82 ms                                                | 6.46 ms: 1.11x slower                                                  |
| regex_effbot            | 3.23 ms                                                | 3.63 ms: 1.12x slower                                                  |
| pickle_dict             | 27.3 us                                                | 31.9 us: 1.17x slower                                                  |
| dask                    | 423 ms                                                 | 497 ms: 1.18x slower                                                   |
| coverage                | 72.8 ms                                                | 94.5 ms: 1.30x slower                                                  |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                           |

Benchmark hidden because not significant (3): generators, bench_mp_pool, telco
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, comprehensions, flaskblogging, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230204-3.12.0a4+-144aaa7/bm-20230204-linux-x86_64-python-144aaa74bbd77aee822e-3.12.0a4+-144aaa7.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.26x
