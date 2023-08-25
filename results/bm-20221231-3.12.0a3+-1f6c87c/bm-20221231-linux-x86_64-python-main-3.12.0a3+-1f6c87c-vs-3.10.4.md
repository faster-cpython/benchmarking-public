
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 1f6c87c
- commit date: 2022-12-31
- overall geometric mean: 1.31x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221231-linux-x86_64-python-main-3.12.0a3+-1f6c87c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 252 ms: 1.33x faster                                   |
| chameleon      | 9.06 ms                                                | 6.42 ms: 1.41x faster                                  |
| docutils       | 3.17 sec                                               | 2.50 sec: 1.27x faster                                 |
| html5lib       | 85.9 ms                                                | 60.3 ms: 1.43x faster                                  |
| Geometric mean | (ref)                                                  | 1.36x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221231-linux-x86_64-python-main-3.12.0a3+-1f6c87c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| float          | 111 ms                                                 | 71.2 ms: 1.55x faster                                  |
| nbody          | 142 ms                                                 | 94.2 ms: 1.50x faster                                  |
| pidigits       | 190 ms                                                 | 197 ms: 1.04x slower                                   |
| Geometric mean | (ref)                                                  | 1.31x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221231-linux-x86_64-python-main-3.12.0a3+-1f6c87c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 131 ms: 1.35x faster                                   |
| regex_v8       | 25.0 ms                                                | 22.2 ms: 1.13x faster                                  |
| regex_dna      | 222 ms                                                 | 215 ms: 1.03x faster                                   |
| regex_effbot   | 3.23 ms                                                | 3.64 ms: 1.13x slower                                  |
| Geometric mean | (ref)                                                  | 1.09x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221231-linux-x86_64-python-main-3.12.0a3+-1f6c87c |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 282 us: 1.61x faster                                   |
| unpickle_pure_python | 300 us                                                 | 197 us: 1.53x faster                                   |
| json_dumps           | 13.5 ms                                                | 9.33 ms: 1.45x faster                                  |
| xml_etree_process    | 74.9 ms                                                | 53.3 ms: 1.41x faster                                  |
| xml_etree_generate   | 94.2 ms                                                | 76.4 ms: 1.23x faster                                  |
| json_loads           | 28.8 us                                                | 23.8 us: 1.21x faster                                  |
| pickle_list          | 4.56 us                                                | 4.00 us: 1.14x faster                                  |
| unpickle             | 14.1 us                                                | 12.7 us: 1.11x faster                                  |
| xml_etree_parse      | 163 ms                                                 | 147 ms: 1.11x faster                                   |
| xml_etree_iterparse  | 111 ms                                                 | 102 ms: 1.09x faster                                   |
| pickle               | 10.3 us                                                | 9.96 us: 1.03x faster                                  |
| unpickle_list        | 4.82 us                                                | 4.95 us: 1.03x slower                                  |
| pickle_dict          | 27.3 us                                                | 30.1 us: 1.10x slower                                  |
| Geometric mean       | (ref)                                                  | 1.20x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221231-linux-x86_64-python-main-3.12.0a3+-1f6c87c |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.45 ms: 1.67x faster                                  |
| python_startup_no_site | 5.82 ms                                                | 6.05 ms: 1.04x slower                                  |
| Geometric mean         | (ref)                                                  | 1.27x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221231-linux-x86_64-python-main-3.12.0a3+-1f6c87c |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.64 ms: 1.53x faster                                  |
| genshi_text     | 30.3 ms                                                | 20.7 ms: 1.46x faster                                  |
| django_template | 45.9 ms                                                | 32.7 ms: 1.40x faster                                  |
| genshi_xml      | 63.3 ms                                                | 46.6 ms: 1.36x faster                                  |
| Geometric mean  | (ref)                                                  | 1.44x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221231-linux-x86_64-python-main-3.12.0a3+-1f6c87c |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| deltablue               | 7.42 ms                                                | 3.17 ms: 2.34x faster                                  |
| logging_silent          | 175 ns                                                 | 91.4 ns: 1.91x faster                                  |
| scimark_sor             | 197 ms                                                 | 104 ms: 1.89x faster                                   |
| richards                | 74.9 ms                                                | 41.5 ms: 1.81x faster                                  |
| scimark_monte_carlo     | 108 ms                                                 | 64.5 ms: 1.68x faster                                  |
| pyflate                 | 673 ms                                                 | 402 ms: 1.68x faster                                   |
| python_startup          | 14.2 ms                                                | 8.45 ms: 1.67x faster                                  |
| go                      | 229 ms                                                 | 137 ms: 1.67x faster                                   |
| raytrace                | 464 ms                                                 | 281 ms: 1.65x faster                                   |
| pickle_pure_python      | 455 us                                                 | 282 us: 1.61x faster                                   |
| spectral_norm           | 150 ms                                                 | 94.1 ms: 1.59x faster                                  |
| crypto_pyaes            | 118 ms                                                 | 74.4 ms: 1.59x faster                                  |
| hexiom                  | 9.53 ms                                                | 6.04 ms: 1.58x faster                                  |
| chaos                   | 106 ms                                                 | 68.0 ms: 1.56x faster                                  |
| float                   | 111 ms                                                 | 71.2 ms: 1.55x faster                                  |
| unpack_sequence         | 64.7 ns                                                | 42.0 ns: 1.54x faster                                  |
| deepcopy_memo           | 52.3 us                                                | 34.1 us: 1.53x faster                                  |
| mako                    | 14.8 ms                                                | 9.64 ms: 1.53x faster                                  |
| unpickle_pure_python    | 300 us                                                 | 197 us: 1.53x faster                                   |
| scimark_lu              | 163 ms                                                 | 108 ms: 1.51x faster                                   |
| nbody                   | 142 ms                                                 | 94.2 ms: 1.50x faster                                  |
| sqlglot_parse           | 2.06 ms                                                | 1.39 ms: 1.48x faster                                  |
| genshi_text             | 30.3 ms                                                | 20.7 ms: 1.46x faster                                  |
| json_dumps              | 13.5 ms                                                | 9.33 ms: 1.45x faster                                  |
| sqlglot_transpile       | 2.45 ms                                                | 1.69 ms: 1.45x faster                                  |
| html5lib                | 85.9 ms                                                | 60.3 ms: 1.43x faster                                  |
| logging_simple          | 8.07 us                                                | 5.72 us: 1.41x faster                                  |
| chameleon               | 9.06 ms                                                | 6.42 ms: 1.41x faster                                  |
| xml_etree_process       | 74.9 ms                                                | 53.3 ms: 1.41x faster                                  |
| django_template         | 45.9 ms                                                | 32.7 ms: 1.40x faster                                  |
| pprint_pformat          | 1.99 sec                                               | 1.42 sec: 1.40x faster                                 |
| logging_format          | 8.91 us                                                | 6.44 us: 1.38x faster                                  |
| thrift                  | 1.03 ms                                                | 749 us: 1.38x faster                                   |
| async_tree_memoization  | 854 ms                                                 | 620 ms: 1.38x faster                                   |
| pprint_safe_repr        | 955 ms                                                 | 694 ms: 1.38x faster                                   |
| async_tree_none         | 717 ms                                                 | 524 ms: 1.37x faster                                   |
| genshi_xml              | 63.3 ms                                                | 46.6 ms: 1.36x faster                                  |
| async_tree_io           | 1.77 sec                                               | 1.31 sec: 1.35x faster                                 |
| regex_compile           | 177 ms                                                 | 131 ms: 1.35x faster                                   |
| scimark_fft             | 424 ms                                                 | 314 ms: 1.35x faster                                   |
| 2to3                    | 336 ms                                                 | 252 ms: 1.33x faster                                   |
| pycparser               | 1.50 sec                                               | 1.14 sec: 1.32x faster                                 |
| deepcopy                | 442 us                                                 | 338 us: 1.31x faster                                   |
| deepcopy_reduce         | 3.82 us                                                | 2.94 us: 1.30x faster                                  |
| sqlglot_normalize       | 135 ms                                                 | 104 ms: 1.30x faster                                   |
| sqlglot_optimize        | 65.3 ms                                                | 50.7 ms: 1.29x faster                                  |
| fannkuch                | 486 ms                                                 | 377 ms: 1.29x faster                                   |
| docutils                | 3.17 sec                                               | 2.50 sec: 1.27x faster                                 |
| nqueens                 | 100 ms                                                 | 78.9 ms: 1.27x faster                                  |
| async_tree_cpu_io_mixed | 951 ms                                                 | 751 ms: 1.27x faster                                   |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.30 ms: 1.27x faster                                  |
| coroutines              | 31.8 ms                                                | 25.5 ms: 1.25x faster                                  |
| xml_etree_generate      | 94.2 ms                                                | 76.4 ms: 1.23x faster                                  |
| bench_thread_pool       | 947 us                                                 | 777 us: 1.22x faster                                   |
| dulwich_log             | 75.9 ms                                                | 62.4 ms: 1.22x faster                                  |
| sympy_integrate         | 24.3 ms                                                | 20.1 ms: 1.21x faster                                  |
| json_loads              | 28.8 us                                                | 23.8 us: 1.21x faster                                  |
| async_generators        | 425 ms                                                 | 352 ms: 1.21x faster                                   |
| sympy_expand            | 545 ms                                                 | 453 ms: 1.20x faster                                   |
| sympy_str               | 328 ms                                                 | 281 ms: 1.17x faster                                   |
| json                    | 5.42 ms                                                | 4.64 ms: 1.17x faster                                  |
| pickle_list             | 4.56 us                                                | 4.00 us: 1.14x faster                                  |
| sympy_sum               | 185 ms                                                 | 162 ms: 1.14x faster                                   |
| regex_v8                | 25.0 ms                                                | 22.2 ms: 1.13x faster                                  |
| meteor_contest          | 115 ms                                                 | 102 ms: 1.12x faster                                   |
| sqlite_synth            | 2.93 us                                                | 2.62 us: 1.12x faster                                  |
| unpickle                | 14.1 us                                                | 12.7 us: 1.11x faster                                  |
| djangocms               | 35.9 us                                                | 32.3 us: 1.11x faster                                  |
| xml_etree_parse         | 163 ms                                                 | 147 ms: 1.11x faster                                   |
| pathlib                 | 20.0 ms                                                | 18.2 ms: 1.10x faster                                  |
| xml_etree_iterparse     | 111 ms                                                 | 102 ms: 1.09x faster                                   |
| mdp                     | 2.82 sec                                               | 2.64 sec: 1.07x faster                                 |
| telco                   | 6.54 ms                                                | 6.19 ms: 1.06x faster                                  |
| pickle                  | 10.3 us                                                | 9.96 us: 1.03x faster                                  |
| regex_dna               | 222 ms                                                 | 215 ms: 1.03x faster                                   |
| generators              | 76.8 ms                                                | 76.4 ms: 1.01x faster                                  |
| unpickle_list           | 4.82 us                                                | 4.95 us: 1.03x slower                                  |
| pidigits                | 190 ms                                                 | 197 ms: 1.04x slower                                   |
| python_startup_no_site  | 5.82 ms                                                | 6.05 ms: 1.04x slower                                  |
| pickle_dict             | 27.3 us                                                | 30.1 us: 1.10x slower                                  |
| regex_effbot            | 3.23 ms                                                | 3.64 ms: 1.13x slower                                  |
| coverage                | 72.8 ms                                                | 100 ms: 1.38x slower                                   |
| Geometric mean          | (ref)                                                  | 1.31x faster                                           |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, comprehensions, create_gc_cycles, dask, flaskblogging, gc_traversal, gunicorn, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, tornado_http, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20221231-3.12.0a3+-1f6c87c/bm-20221231-linux-x86_64-python-main-3.12.0a3+-1f6c87c.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.26x
