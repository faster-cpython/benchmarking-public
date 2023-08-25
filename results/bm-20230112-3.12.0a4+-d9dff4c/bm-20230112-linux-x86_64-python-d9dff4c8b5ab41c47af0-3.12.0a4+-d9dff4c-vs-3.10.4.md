
# Results vs. 3.10.4

- fork: python
- ref: d9dff4c8b5ab41c47af0
- machine: linux-x86_64
- commit hash: d9dff4c
- commit date: 2023-01-12
- overall geometric mean: 1.30x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230112-linux-x86_64-python-d9dff4c8b5ab41c47af0-3.12.0a4+-d9dff4c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 253 ms: 1.33x faster                                                   |
| chameleon      | 9.06 ms                                                | 6.39 ms: 1.42x faster                                                  |
| docutils       | 3.17 sec                                               | 2.51 sec: 1.26x faster                                                 |
| html5lib       | 85.9 ms                                                | 59.7 ms: 1.44x faster                                                  |
| Geometric mean | (ref)                                                  | 1.36x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230112-linux-x86_64-python-d9dff4c8b5ab41c47af0-3.12.0a4+-d9dff4c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 111 ms                                                 | 72.4 ms: 1.53x faster                                                  |
| nbody          | 142 ms                                                 | 94.4 ms: 1.50x faster                                                  |
| pidigits       | 190 ms                                                 | 190 ms: 1.00x faster                                                   |
| Geometric mean | (ref)                                                  | 1.32x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230112-linux-x86_64-python-d9dff4c8b5ab41c47af0-3.12.0a4+-d9dff4c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 129 ms: 1.37x faster                                                   |
| regex_v8       | 25.0 ms                                                | 22.5 ms: 1.11x faster                                                  |
| regex_dna      | 222 ms                                                 | 206 ms: 1.08x faster                                                   |
| regex_effbot   | 3.23 ms                                                | 3.61 ms: 1.12x slower                                                  |
| Geometric mean | (ref)                                                  | 1.10x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230112-linux-x86_64-python-d9dff4c8b5ab41c47af0-3.12.0a4+-d9dff4c |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 282 us: 1.61x faster                                                   |
| unpickle_pure_python | 300 us                                                 | 198 us: 1.52x faster                                                   |
| json_dumps           | 13.5 ms                                                | 9.39 ms: 1.44x faster                                                  |
| xml_etree_process    | 74.9 ms                                                | 53.3 ms: 1.41x faster                                                  |
| xml_etree_generate   | 94.2 ms                                                | 76.2 ms: 1.24x faster                                                  |
| json_loads           | 28.8 us                                                | 23.6 us: 1.22x faster                                                  |
| pickle_list          | 4.56 us                                                | 4.04 us: 1.13x faster                                                  |
| xml_etree_parse      | 163 ms                                                 | 149 ms: 1.10x faster                                                   |
| unpickle             | 14.1 us                                                | 12.9 us: 1.09x faster                                                  |
| xml_etree_iterparse  | 111 ms                                                 | 106 ms: 1.05x faster                                                   |
| pickle               | 10.3 us                                                | 10.1 us: 1.02x faster                                                  |
| unpickle_list        | 4.82 us                                                | 4.98 us: 1.03x slower                                                  |
| pickle_dict          | 27.3 us                                                | 30.4 us: 1.12x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.19x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230112-linux-x86_64-python-d9dff4c8b5ab41c47af0-3.12.0a4+-d9dff4c |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.58 ms: 1.65x faster                                                  |
| python_startup_no_site | 5.82 ms                                                | 6.13 ms: 1.05x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.25x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230112-linux-x86_64-python-d9dff4c8b5ab41c47af0-3.12.0a4+-d9dff4c |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.77 ms: 1.51x faster                                                  |
| genshi_text     | 30.3 ms                                                | 20.3 ms: 1.49x faster                                                  |
| django_template | 45.9 ms                                                | 33.0 ms: 1.39x faster                                                  |
| genshi_xml      | 63.3 ms                                                | 47.0 ms: 1.35x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.43x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230112-linux-x86_64-python-d9dff4c8b5ab41c47af0-3.12.0a4+-d9dff4c |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| deltablue               | 7.42 ms                                                | 3.20 ms: 2.32x faster                                                  |
| logging_silent          | 175 ns                                                 | 89.8 ns: 1.95x faster                                                  |
| scimark_sor             | 197 ms                                                 | 106 ms: 1.85x faster                                                   |
| asyncio_tcp             | 925 ms                                                 | 505 ms: 1.83x faster                                                   |
| richards                | 74.9 ms                                                | 41.3 ms: 1.81x faster                                                  |
| go                      | 229 ms                                                 | 134 ms: 1.71x faster                                                   |
| pyflate                 | 673 ms                                                 | 400 ms: 1.68x faster                                                   |
| scimark_monte_carlo     | 108 ms                                                 | 64.5 ms: 1.68x faster                                                  |
| python_startup          | 14.2 ms                                                | 8.58 ms: 1.65x faster                                                  |
| raytrace                | 464 ms                                                 | 283 ms: 1.64x faster                                                   |
| pickle_pure_python      | 455 us                                                 | 282 us: 1.61x faster                                                   |
| chaos                   | 106 ms                                                 | 66.8 ms: 1.59x faster                                                  |
| crypto_pyaes            | 118 ms                                                 | 74.8 ms: 1.58x faster                                                  |
| hexiom                  | 9.53 ms                                                | 6.02 ms: 1.58x faster                                                  |
| deepcopy_memo           | 52.3 us                                                | 33.8 us: 1.55x faster                                                  |
| spectral_norm           | 150 ms                                                 | 97.1 ms: 1.54x faster                                                  |
| float                   | 111 ms                                                 | 72.4 ms: 1.53x faster                                                  |
| unpickle_pure_python    | 300 us                                                 | 198 us: 1.52x faster                                                   |
| mako                    | 14.8 ms                                                | 9.77 ms: 1.51x faster                                                  |
| scimark_lu              | 163 ms                                                 | 109 ms: 1.50x faster                                                   |
| nbody                   | 142 ms                                                 | 94.4 ms: 1.50x faster                                                  |
| genshi_text             | 30.3 ms                                                | 20.3 ms: 1.49x faster                                                  |
| sqlglot_parse           | 2.06 ms                                                | 1.39 ms: 1.48x faster                                                  |
| sqlglot_transpile       | 2.45 ms                                                | 1.69 ms: 1.45x faster                                                  |
| json_dumps              | 13.5 ms                                                | 9.39 ms: 1.44x faster                                                  |
| html5lib                | 85.9 ms                                                | 59.7 ms: 1.44x faster                                                  |
| unpack_sequence         | 64.7 ns                                                | 45.1 ns: 1.44x faster                                                  |
| pprint_pformat          | 1.99 sec                                               | 1.39 sec: 1.43x faster                                                 |
| pprint_safe_repr        | 955 ms                                                 | 673 ms: 1.42x faster                                                   |
| chameleon               | 9.06 ms                                                | 6.39 ms: 1.42x faster                                                  |
| xml_etree_process       | 74.9 ms                                                | 53.3 ms: 1.41x faster                                                  |
| logging_simple          | 8.07 us                                                | 5.74 us: 1.41x faster                                                  |
| django_template         | 45.9 ms                                                | 33.0 ms: 1.39x faster                                                  |
| logging_format          | 8.91 us                                                | 6.42 us: 1.39x faster                                                  |
| regex_compile           | 177 ms                                                 | 129 ms: 1.37x faster                                                   |
| thrift                  | 1.03 ms                                                | 755 us: 1.37x faster                                                   |
| async_tree_none         | 717 ms                                                 | 528 ms: 1.36x faster                                                   |
| scimark_fft             | 424 ms                                                 | 312 ms: 1.36x faster                                                   |
| genshi_xml              | 63.3 ms                                                | 47.0 ms: 1.35x faster                                                  |
| async_tree_io           | 1.77 sec                                               | 1.32 sec: 1.34x faster                                                 |
| deepcopy                | 442 us                                                 | 331 us: 1.33x faster                                                   |
| 2to3                    | 336 ms                                                 | 253 ms: 1.33x faster                                                   |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.11 ms: 1.33x faster                                                  |
| pycparser               | 1.50 sec                                               | 1.15 sec: 1.31x faster                                                 |
| sqlglot_normalize       | 135 ms                                                 | 104 ms: 1.30x faster                                                   |
| async_tree_memoization  | 854 ms                                                 | 657 ms: 1.30x faster                                                   |
| sqlglot_optimize        | 65.3 ms                                                | 50.3 ms: 1.30x faster                                                  |
| deepcopy_reduce         | 3.82 us                                                | 2.95 us: 1.30x faster                                                  |
| coroutines              | 31.8 ms                                                | 24.7 ms: 1.29x faster                                                  |
| fannkuch                | 486 ms                                                 | 377 ms: 1.29x faster                                                   |
| docutils                | 3.17 sec                                               | 2.51 sec: 1.26x faster                                                 |
| async_tree_cpu_io_mixed | 951 ms                                                 | 754 ms: 1.26x faster                                                   |
| nqueens                 | 100 ms                                                 | 80.3 ms: 1.25x faster                                                  |
| xml_etree_generate      | 94.2 ms                                                | 76.2 ms: 1.24x faster                                                  |
| bench_thread_pool       | 947 us                                                 | 776 us: 1.22x faster                                                   |
| json_loads              | 28.8 us                                                | 23.6 us: 1.22x faster                                                  |
| dulwich_log             | 75.9 ms                                                | 62.3 ms: 1.22x faster                                                  |
| sympy_integrate         | 24.3 ms                                                | 20.2 ms: 1.20x faster                                                  |
| async_generators        | 425 ms                                                 | 355 ms: 1.20x faster                                                   |
| sympy_expand            | 545 ms                                                 | 458 ms: 1.19x faster                                                   |
| sympy_str               | 328 ms                                                 | 282 ms: 1.16x faster                                                   |
| json                    | 5.42 ms                                                | 4.70 ms: 1.15x faster                                                  |
| sqlite_synth            | 2.93 us                                                | 2.57 us: 1.14x faster                                                  |
| create_gc_cycles        | 1.67 ms                                                | 1.47 ms: 1.14x faster                                                  |
| sympy_sum               | 185 ms                                                 | 163 ms: 1.13x faster                                                   |
| pickle_list             | 4.56 us                                                | 4.04 us: 1.13x faster                                                  |
| mdp                     | 2.82 sec                                               | 2.50 sec: 1.13x faster                                                 |
| djangocms               | 35.9 us                                                | 32.1 us: 1.12x faster                                                  |
| pathlib                 | 20.0 ms                                                | 17.9 ms: 1.12x faster                                                  |
| regex_v8                | 25.0 ms                                                | 22.5 ms: 1.11x faster                                                  |
| xml_etree_parse         | 163 ms                                                 | 149 ms: 1.10x faster                                                   |
| unpickle                | 14.1 us                                                | 12.9 us: 1.09x faster                                                  |
| meteor_contest          | 115 ms                                                 | 106 ms: 1.08x faster                                                   |
| regex_dna               | 222 ms                                                 | 206 ms: 1.08x faster                                                   |
| xml_etree_iterparse     | 111 ms                                                 | 106 ms: 1.05x faster                                                   |
| telco                   | 6.54 ms                                                | 6.33 ms: 1.03x faster                                                  |
| pickle                  | 10.3 us                                                | 10.1 us: 1.02x faster                                                  |
| generators              | 76.8 ms                                                | 75.4 ms: 1.02x faster                                                  |
| gc_traversal            | 3.84 ms                                                | 3.80 ms: 1.01x faster                                                  |
| pidigits                | 190 ms                                                 | 190 ms: 1.00x faster                                                   |
| unpickle_list           | 4.82 us                                                | 4.98 us: 1.03x slower                                                  |
| python_startup_no_site  | 5.82 ms                                                | 6.13 ms: 1.05x slower                                                  |
| pickle_dict             | 27.3 us                                                | 30.4 us: 1.12x slower                                                  |
| regex_effbot            | 3.23 ms                                                | 3.61 ms: 1.12x slower                                                  |
| dask                    | 423 ms                                                 | 495 ms: 1.17x slower                                                   |
| coverage                | 72.8 ms                                                | 101 ms: 1.39x slower                                                   |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                           |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, comprehensions, flaskblogging, gunicorn, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, tornado_http, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230112-3.12.0a4+-d9dff4c/bm-20230112-linux-x86_64-python-d9dff4c8b5ab41c47af0-3.12.0a4+-d9dff4c.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.25x
