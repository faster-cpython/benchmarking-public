
# Results vs. 3.10.4

- fork: python
- ref: a7715ccfba5b86ab09f8
- machine: linux-x86_64
- commit hash: a7715cc
- commit date: 2022-12-21
- overall geometric mean: 1.32x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221221-linux-x86_64-python-a7715ccfba5b86ab09f8-3.12.0a3+-a7715cc |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 253 ms: 1.33x faster                                                   |
| chameleon      | 9.06 ms                                                | 6.36 ms: 1.43x faster                                                  |
| docutils       | 3.17 sec                                               | 2.48 sec: 1.28x faster                                                 |
| html5lib       | 85.9 ms                                                | 59.5 ms: 1.44x faster                                                  |
| Geometric mean | (ref)                                                  | 1.37x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221221-linux-x86_64-python-a7715ccfba5b86ab09f8-3.12.0a3+-a7715cc |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 111 ms                                                 | 71.8 ms: 1.54x faster                                                  |
| nbody          | 142 ms                                                 | 93.1 ms: 1.52x faster                                                  |
| pidigits       | 190 ms                                                 | 197 ms: 1.04x slower                                                   |
| Geometric mean | (ref)                                                  | 1.31x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221221-linux-x86_64-python-a7715ccfba5b86ab09f8-3.12.0a3+-a7715cc |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 130 ms: 1.36x faster                                                   |
| regex_v8       | 25.0 ms                                                | 21.7 ms: 1.16x faster                                                  |
| regex_dna      | 222 ms                                                 | 203 ms: 1.09x faster                                                   |
| regex_effbot   | 3.23 ms                                                | 3.45 ms: 1.07x slower                                                  |
| Geometric mean | (ref)                                                  | 1.12x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221221-linux-x86_64-python-a7715ccfba5b86ab09f8-3.12.0a3+-a7715cc |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 283 us: 1.61x faster                                                   |
| unpickle_pure_python | 300 us                                                 | 197 us: 1.53x faster                                                   |
| json_dumps           | 13.5 ms                                                | 9.43 ms: 1.44x faster                                                  |
| xml_etree_process    | 74.9 ms                                                | 53.5 ms: 1.40x faster                                                  |
| xml_etree_generate   | 94.2 ms                                                | 76.5 ms: 1.23x faster                                                  |
| json_loads           | 28.8 us                                                | 23.6 us: 1.22x faster                                                  |
| pickle_list          | 4.56 us                                                | 3.98 us: 1.14x faster                                                  |
| xml_etree_parse      | 163 ms                                                 | 147 ms: 1.11x faster                                                   |
| unpickle             | 14.1 us                                                | 13.2 us: 1.07x faster                                                  |
| xml_etree_iterparse  | 111 ms                                                 | 106 ms: 1.05x faster                                                   |
| pickle               | 10.3 us                                                | 10.4 us: 1.01x slower                                                  |
| unpickle_list        | 4.82 us                                                | 4.93 us: 1.02x slower                                                  |
| pickle_dict          | 27.3 us                                                | 30.6 us: 1.12x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.19x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221221-linux-x86_64-python-a7715ccfba5b86ab09f8-3.12.0a3+-a7715cc |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.43 ms: 1.68x faster                                                  |
| python_startup_no_site | 5.82 ms                                                | 6.09 ms: 1.05x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.27x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221221-linux-x86_64-python-a7715ccfba5b86ab09f8-3.12.0a3+-a7715cc |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.47 ms: 1.56x faster                                                  |
| genshi_text     | 30.3 ms                                                | 20.4 ms: 1.48x faster                                                  |
| django_template | 45.9 ms                                                | 32.5 ms: 1.41x faster                                                  |
| genshi_xml      | 63.3 ms                                                | 47.6 ms: 1.33x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.44x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221221-linux-x86_64-python-a7715ccfba5b86ab09f8-3.12.0a3+-a7715cc |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| deltablue               | 7.42 ms                                                | 3.20 ms: 2.32x faster                                                  |
| logging_silent          | 175 ns                                                 | 90.4 ns: 1.94x faster                                                  |
| scimark_sor             | 197 ms                                                 | 105 ms: 1.87x faster                                                   |
| richards                | 74.9 ms                                                | 41.4 ms: 1.81x faster                                                  |
| pyflate                 | 673 ms                                                 | 396 ms: 1.70x faster                                                   |
| scimark_monte_carlo     | 108 ms                                                 | 64.2 ms: 1.69x faster                                                  |
| python_startup          | 14.2 ms                                                | 8.43 ms: 1.68x faster                                                  |
| go                      | 229 ms                                                 | 138 ms: 1.67x faster                                                   |
| raytrace                | 464 ms                                                 | 280 ms: 1.65x faster                                                   |
| pickle_pure_python      | 455 us                                                 | 283 us: 1.61x faster                                                   |
| crypto_pyaes            | 118 ms                                                 | 74.4 ms: 1.59x faster                                                  |
| spectral_norm           | 150 ms                                                 | 94.8 ms: 1.58x faster                                                  |
| hexiom                  | 9.53 ms                                                | 6.02 ms: 1.58x faster                                                  |
| unpack_sequence         | 64.7 ns                                                | 41.3 ns: 1.57x faster                                                  |
| mako                    | 14.8 ms                                                | 9.47 ms: 1.56x faster                                                  |
| chaos                   | 106 ms                                                 | 68.7 ms: 1.55x faster                                                  |
| deepcopy_memo           | 52.3 us                                                | 33.9 us: 1.54x faster                                                  |
| float                   | 111 ms                                                 | 71.8 ms: 1.54x faster                                                  |
| scimark_lu              | 163 ms                                                 | 107 ms: 1.53x faster                                                   |
| unpickle_pure_python    | 300 us                                                 | 197 us: 1.53x faster                                                   |
| nbody                   | 142 ms                                                 | 93.1 ms: 1.52x faster                                                  |
| genshi_text             | 30.3 ms                                                | 20.4 ms: 1.48x faster                                                  |
| sqlglot_parse           | 2.06 ms                                                | 1.39 ms: 1.48x faster                                                  |
| pprint_pformat          | 1.99 sec                                               | 1.36 sec: 1.46x faster                                                 |
| sqlglot_transpile       | 2.45 ms                                                | 1.68 ms: 1.46x faster                                                  |
| pprint_safe_repr        | 955 ms                                                 | 661 ms: 1.44x faster                                                   |
| html5lib                | 85.9 ms                                                | 59.5 ms: 1.44x faster                                                  |
| json_dumps              | 13.5 ms                                                | 9.43 ms: 1.44x faster                                                  |
| logging_format          | 8.91 us                                                | 6.22 us: 1.43x faster                                                  |
| chameleon               | 9.06 ms                                                | 6.36 ms: 1.43x faster                                                  |
| logging_simple          | 8.07 us                                                | 5.68 us: 1.42x faster                                                  |
| django_template         | 45.9 ms                                                | 32.5 ms: 1.41x faster                                                  |
| xml_etree_process       | 74.9 ms                                                | 53.5 ms: 1.40x faster                                                  |
| thrift                  | 1.03 ms                                                | 741 us: 1.40x faster                                                   |
| scimark_fft             | 424 ms                                                 | 309 ms: 1.37x faster                                                   |
| pycparser               | 1.50 sec                                               | 1.10 sec: 1.37x faster                                                 |
| regex_compile           | 177 ms                                                 | 130 ms: 1.36x faster                                                   |
| deepcopy                | 442 us                                                 | 328 us: 1.35x faster                                                   |
| async_tree_io           | 1.77 sec                                               | 1.32 sec: 1.34x faster                                                 |
| async_tree_none         | 717 ms                                                 | 535 ms: 1.34x faster                                                   |
| fannkuch                | 486 ms                                                 | 363 ms: 1.34x faster                                                   |
| 2to3                    | 336 ms                                                 | 253 ms: 1.33x faster                                                   |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.10 ms: 1.33x faster                                                  |
| genshi_xml              | 63.3 ms                                                | 47.6 ms: 1.33x faster                                                  |
| async_tree_memoization  | 854 ms                                                 | 644 ms: 1.33x faster                                                   |
| deepcopy_reduce         | 3.82 us                                                | 2.90 us: 1.32x faster                                                  |
| sqlglot_normalize       | 135 ms                                                 | 104 ms: 1.31x faster                                                   |
| sqlglot_optimize        | 65.3 ms                                                | 50.1 ms: 1.30x faster                                                  |
| coroutines              | 31.8 ms                                                | 24.5 ms: 1.30x faster                                                  |
| docutils                | 3.17 sec                                               | 2.48 sec: 1.28x faster                                                 |
| nqueens                 | 100 ms                                                 | 78.5 ms: 1.27x faster                                                  |
| async_tree_cpu_io_mixed | 951 ms                                                 | 765 ms: 1.24x faster                                                   |
| xml_etree_generate      | 94.2 ms                                                | 76.5 ms: 1.23x faster                                                  |
| json_loads              | 28.8 us                                                | 23.6 us: 1.22x faster                                                  |
| dulwich_log             | 75.9 ms                                                | 62.6 ms: 1.21x faster                                                  |
| bench_thread_pool       | 947 us                                                 | 783 us: 1.21x faster                                                   |
| sympy_expand            | 545 ms                                                 | 451 ms: 1.21x faster                                                   |
| sympy_integrate         | 24.3 ms                                                | 20.2 ms: 1.20x faster                                                  |
| async_generators        | 425 ms                                                 | 356 ms: 1.19x faster                                                   |
| sympy_str               | 328 ms                                                 | 280 ms: 1.17x faster                                                   |
| json                    | 5.42 ms                                                | 4.63 ms: 1.17x faster                                                  |
| regex_v8                | 25.0 ms                                                | 21.7 ms: 1.16x faster                                                  |
| pickle_list             | 4.56 us                                                | 3.98 us: 1.14x faster                                                  |
| sqlite_synth            | 2.93 us                                                | 2.58 us: 1.14x faster                                                  |
| sympy_sum               | 185 ms                                                 | 162 ms: 1.14x faster                                                   |
| pathlib                 | 20.0 ms                                                | 17.9 ms: 1.12x faster                                                  |
| xml_etree_parse         | 163 ms                                                 | 147 ms: 1.11x faster                                                   |
| mdp                     | 2.82 sec                                               | 2.54 sec: 1.11x faster                                                 |
| meteor_contest          | 115 ms                                                 | 104 ms: 1.11x faster                                                   |
| regex_dna               | 222 ms                                                 | 203 ms: 1.09x faster                                                   |
| unpickle                | 14.1 us                                                | 13.2 us: 1.07x faster                                                  |
| xml_etree_iterparse     | 111 ms                                                 | 106 ms: 1.05x faster                                                   |
| telco                   | 6.54 ms                                                | 6.29 ms: 1.04x faster                                                  |
| generators              | 76.8 ms                                                | 77.4 ms: 1.01x slower                                                  |
| pickle                  | 10.3 us                                                | 10.4 us: 1.01x slower                                                  |
| unpickle_list           | 4.82 us                                                | 4.93 us: 1.02x slower                                                  |
| pidigits                | 190 ms                                                 | 197 ms: 1.04x slower                                                   |
| python_startup_no_site  | 5.82 ms                                                | 6.09 ms: 1.05x slower                                                  |
| regex_effbot            | 3.23 ms                                                | 3.45 ms: 1.07x slower                                                  |
| pickle_dict             | 27.3 us                                                | 30.6 us: 1.12x slower                                                  |
| coverage                | 72.8 ms                                                | 102 ms: 1.40x slower                                                   |
| Geometric mean          | (ref)                                                  | 1.32x faster                                                           |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (18) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, comprehensions, create_gc_cycles, dask, djangocms, flaskblogging, gc_traversal, gunicorn, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, tornado_http, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20221221-3.12.0a3+-a7715cc/bm-20221221-linux-x86_64-python-a7715ccfba5b86ab09f8-3.12.0a3+-a7715cc.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.30x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.26x
