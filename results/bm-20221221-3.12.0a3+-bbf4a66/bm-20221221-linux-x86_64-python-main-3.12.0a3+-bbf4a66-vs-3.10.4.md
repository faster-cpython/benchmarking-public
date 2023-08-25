
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: bbf4a66
- commit date: 2022-12-21
- overall geometric mean: 1.32x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221221-linux-x86_64-python-main-3.12.0a3+-bbf4a66 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 252 ms: 1.33x faster                                   |
| chameleon      | 9.06 ms                                                | 6.35 ms: 1.43x faster                                  |
| docutils       | 3.17 sec                                               | 2.49 sec: 1.27x faster                                 |
| html5lib       | 85.9 ms                                                | 59.2 ms: 1.45x faster                                  |
| Geometric mean | (ref)                                                  | 1.37x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221221-linux-x86_64-python-main-3.12.0a3+-bbf4a66 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| float          | 111 ms                                                 | 71.9 ms: 1.54x faster                                  |
| nbody          | 142 ms                                                 | 94.4 ms: 1.50x faster                                  |
| pidigits       | 190 ms                                                 | 189 ms: 1.00x faster                                   |
| Geometric mean | (ref)                                                  | 1.32x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221221-linux-x86_64-python-main-3.12.0a3+-bbf4a66 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 129 ms: 1.37x faster                                   |
| regex_v8       | 25.0 ms                                                | 22.4 ms: 1.12x faster                                  |
| regex_dna      | 222 ms                                                 | 210 ms: 1.05x faster                                   |
| regex_effbot   | 3.23 ms                                                | 3.47 ms: 1.08x slower                                  |
| Geometric mean | (ref)                                                  | 1.11x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221221-linux-x86_64-python-main-3.12.0a3+-bbf4a66 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 282 us: 1.61x faster                                   |
| unpickle_pure_python | 300 us                                                 | 197 us: 1.53x faster                                   |
| json_dumps           | 13.5 ms                                                | 9.49 ms: 1.43x faster                                  |
| xml_etree_process    | 74.9 ms                                                | 54.2 ms: 1.38x faster                                  |
| xml_etree_generate   | 94.2 ms                                                | 77.2 ms: 1.22x faster                                  |
| json_loads           | 28.8 us                                                | 23.9 us: 1.21x faster                                  |
| xml_etree_parse      | 163 ms                                                 | 146 ms: 1.12x faster                                   |
| pickle_list          | 4.56 us                                                | 4.17 us: 1.09x faster                                  |
| xml_etree_iterparse  | 111 ms                                                 | 102 ms: 1.09x faster                                   |
| pickle               | 10.3 us                                                | 10.2 us: 1.01x faster                                  |
| unpickle_list        | 4.82 us                                                | 5.01 us: 1.04x slower                                  |
| pickle_dict          | 27.3 us                                                | 30.9 us: 1.14x slower                                  |
| Geometric mean       | (ref)                                                  | 1.17x faster                                           |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221221-linux-x86_64-python-main-3.12.0a3+-bbf4a66 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.41 ms: 1.68x faster                                  |
| python_startup_no_site | 5.82 ms                                                | 6.07 ms: 1.04x slower                                  |
| Geometric mean         | (ref)                                                  | 1.27x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221221-linux-x86_64-python-main-3.12.0a3+-bbf4a66 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.46 ms: 1.56x faster                                  |
| genshi_text     | 30.3 ms                                                | 20.0 ms: 1.52x faster                                  |
| django_template | 45.9 ms                                                | 32.3 ms: 1.42x faster                                  |
| genshi_xml      | 63.3 ms                                                | 46.3 ms: 1.37x faster                                  |
| Geometric mean  | (ref)                                                  | 1.46x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20221221-linux-x86_64-python-main-3.12.0a3+-bbf4a66 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| deltablue               | 7.42 ms                                                | 3.21 ms: 2.31x faster                                  |
| logging_silent          | 175 ns                                                 | 93.0 ns: 1.88x faster                                  |
| scimark_sor             | 197 ms                                                 | 105 ms: 1.88x faster                                   |
| richards                | 74.9 ms                                                | 41.7 ms: 1.79x faster                                  |
| go                      | 229 ms                                                 | 131 ms: 1.75x faster                                   |
| pyflate                 | 673 ms                                                 | 395 ms: 1.70x faster                                   |
| python_startup          | 14.2 ms                                                | 8.41 ms: 1.68x faster                                  |
| scimark_monte_carlo     | 108 ms                                                 | 65.5 ms: 1.65x faster                                  |
| raytrace                | 464 ms                                                 | 282 ms: 1.64x faster                                   |
| pickle_pure_python      | 455 us                                                 | 282 us: 1.61x faster                                   |
| spectral_norm           | 150 ms                                                 | 93.6 ms: 1.60x faster                                  |
| chaos                   | 106 ms                                                 | 66.6 ms: 1.60x faster                                  |
| crypto_pyaes            | 118 ms                                                 | 74.8 ms: 1.58x faster                                  |
| hexiom                  | 9.53 ms                                                | 6.09 ms: 1.57x faster                                  |
| mako                    | 14.8 ms                                                | 9.46 ms: 1.56x faster                                  |
| deepcopy_memo           | 52.3 us                                                | 33.7 us: 1.55x faster                                  |
| scimark_lu              | 163 ms                                                 | 105 ms: 1.55x faster                                   |
| float                   | 111 ms                                                 | 71.9 ms: 1.54x faster                                  |
| unpickle_pure_python    | 300 us                                                 | 197 us: 1.53x faster                                   |
| genshi_text             | 30.3 ms                                                | 20.0 ms: 1.52x faster                                  |
| nbody                   | 142 ms                                                 | 94.4 ms: 1.50x faster                                  |
| unpack_sequence         | 64.7 ns                                                | 43.2 ns: 1.50x faster                                  |
| sqlglot_parse           | 2.06 ms                                                | 1.38 ms: 1.49x faster                                  |
| sqlglot_transpile       | 2.45 ms                                                | 1.67 ms: 1.47x faster                                  |
| html5lib                | 85.9 ms                                                | 59.2 ms: 1.45x faster                                  |
| pprint_pformat          | 1.99 sec                                               | 1.39 sec: 1.43x faster                                 |
| json_dumps              | 13.5 ms                                                | 9.49 ms: 1.43x faster                                  |
| chameleon               | 9.06 ms                                                | 6.35 ms: 1.43x faster                                  |
| django_template         | 45.9 ms                                                | 32.3 ms: 1.42x faster                                  |
| logging_simple          | 8.07 us                                                | 5.69 us: 1.42x faster                                  |
| pprint_safe_repr        | 955 ms                                                 | 675 ms: 1.41x faster                                   |
| logging_format          | 8.91 us                                                | 6.33 us: 1.41x faster                                  |
| thrift                  | 1.03 ms                                                | 744 us: 1.39x faster                                   |
| xml_etree_process       | 74.9 ms                                                | 54.2 ms: 1.38x faster                                  |
| pycparser               | 1.50 sec                                               | 1.09 sec: 1.38x faster                                 |
| regex_compile           | 177 ms                                                 | 129 ms: 1.37x faster                                   |
| genshi_xml              | 63.3 ms                                                | 46.3 ms: 1.37x faster                                  |
| scimark_fft             | 424 ms                                                 | 310 ms: 1.37x faster                                   |
| deepcopy                | 442 us                                                 | 329 us: 1.34x faster                                   |
| async_tree_none         | 717 ms                                                 | 533 ms: 1.34x faster                                   |
| fannkuch                | 486 ms                                                 | 362 ms: 1.34x faster                                   |
| 2to3                    | 336 ms                                                 | 252 ms: 1.33x faster                                   |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.10 ms: 1.33x faster                                  |
| async_tree_io           | 1.77 sec                                               | 1.34 sec: 1.33x faster                                 |
| deepcopy_reduce         | 3.82 us                                                | 2.88 us: 1.33x faster                                  |
| sqlglot_normalize       | 135 ms                                                 | 103 ms: 1.32x faster                                   |
| sqlglot_optimize        | 65.3 ms                                                | 49.9 ms: 1.31x faster                                  |
| async_tree_memoization  | 854 ms                                                 | 656 ms: 1.30x faster                                   |
| docutils                | 3.17 sec                                               | 2.49 sec: 1.27x faster                                 |
| nqueens                 | 100 ms                                                 | 78.6 ms: 1.27x faster                                  |
| async_tree_cpu_io_mixed | 951 ms                                                 | 763 ms: 1.25x faster                                   |
| coroutines              | 31.8 ms                                                | 25.8 ms: 1.24x faster                                  |
| dulwich_log             | 75.9 ms                                                | 61.6 ms: 1.23x faster                                  |
| bench_thread_pool       | 947 us                                                 | 775 us: 1.22x faster                                   |
| xml_etree_generate      | 94.2 ms                                                | 77.2 ms: 1.22x faster                                  |
| sympy_expand            | 545 ms                                                 | 447 ms: 1.22x faster                                   |
| json_loads              | 28.8 us                                                | 23.9 us: 1.21x faster                                  |
| sympy_integrate         | 24.3 ms                                                | 20.1 ms: 1.21x faster                                  |
| async_generators        | 425 ms                                                 | 356 ms: 1.20x faster                                   |
| sympy_str               | 328 ms                                                 | 277 ms: 1.19x faster                                   |
| json                    | 5.42 ms                                                | 4.59 ms: 1.18x faster                                  |
| sympy_sum               | 185 ms                                                 | 161 ms: 1.15x faster                                   |
| pathlib                 | 20.0 ms                                                | 17.5 ms: 1.15x faster                                  |
| sqlite_synth            | 2.93 us                                                | 2.58 us: 1.14x faster                                  |
| mdp                     | 2.82 sec                                               | 2.51 sec: 1.13x faster                                 |
| regex_v8                | 25.0 ms                                                | 22.4 ms: 1.12x faster                                  |
| xml_etree_parse         | 163 ms                                                 | 146 ms: 1.12x faster                                   |
| meteor_contest          | 115 ms                                                 | 105 ms: 1.10x faster                                   |
| pickle_list             | 4.56 us                                                | 4.17 us: 1.09x faster                                  |
| xml_etree_iterparse     | 111 ms                                                 | 102 ms: 1.09x faster                                   |
| regex_dna               | 222 ms                                                 | 210 ms: 1.05x faster                                   |
| telco                   | 6.54 ms                                                | 6.23 ms: 1.05x faster                                  |
| pickle                  | 10.3 us                                                | 10.2 us: 1.01x faster                                  |
| pidigits                | 190 ms                                                 | 189 ms: 1.00x faster                                   |
| generators              | 76.8 ms                                                | 78.3 ms: 1.02x slower                                  |
| unpickle_list           | 4.82 us                                                | 5.01 us: 1.04x slower                                  |
| python_startup_no_site  | 5.82 ms                                                | 6.07 ms: 1.04x slower                                  |
| regex_effbot            | 3.23 ms                                                | 3.47 ms: 1.08x slower                                  |
| pickle_dict             | 27.3 us                                                | 30.9 us: 1.14x slower                                  |
| coverage                | 72.8 ms                                                | 100 ms: 1.38x slower                                   |
| Geometric mean          | (ref)                                                  | 1.32x faster                                           |

Benchmark hidden because not significant (2): unpickle, bench_mp_pool
Ignored benchmarks (18) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, comprehensions, create_gc_cycles, dask, djangocms, flaskblogging, gc_traversal, gunicorn, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, tornado_http, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20221221-3.12.0a3+-bbf4a66/bm-20221221-linux-x86_64-python-main-3.12.0a3+-bbf4a66.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.26x
