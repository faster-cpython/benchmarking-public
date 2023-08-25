
# Results vs. 3.10.4

- fork: iritkatriel
- ref: InitializeHeader
- machine: linux-x86_64
- commit hash: d501577
- commit date: 2023-01-05
- overall geometric mean: 1.31x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230105-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3+-d501577 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 252 ms: 1.33x faster                                                    |
| chameleon      | 9.06 ms                                                | 6.23 ms: 1.45x faster                                                   |
| docutils       | 3.17 sec                                               | 2.49 sec: 1.27x faster                                                  |
| html5lib       | 85.9 ms                                                | 59.9 ms: 1.43x faster                                                   |
| Geometric mean | (ref)                                                  | 1.37x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230105-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3+-d501577 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 111 ms                                                 | 71.9 ms: 1.54x faster                                                   |
| nbody          | 142 ms                                                 | 93.4 ms: 1.52x faster                                                   |
| pidigits       | 190 ms                                                 | 198 ms: 1.04x slower                                                    |
| Geometric mean | (ref)                                                  | 1.31x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230105-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3+-d501577 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 129 ms: 1.37x faster                                                    |
| regex_v8       | 25.0 ms                                                | 22.5 ms: 1.11x faster                                                   |
| regex_dna      | 222 ms                                                 | 208 ms: 1.07x faster                                                    |
| regex_effbot   | 3.23 ms                                                | 3.60 ms: 1.11x slower                                                   |
| Geometric mean | (ref)                                                  | 1.10x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230105-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3+-d501577 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 283 us: 1.61x faster                                                    |
| unpickle_pure_python | 300 us                                                 | 199 us: 1.51x faster                                                    |
| json_dumps           | 13.5 ms                                                | 9.36 ms: 1.45x faster                                                   |
| xml_etree_process    | 74.9 ms                                                | 53.7 ms: 1.39x faster                                                   |
| xml_etree_generate   | 94.2 ms                                                | 77.0 ms: 1.22x faster                                                   |
| json_loads           | 28.8 us                                                | 23.9 us: 1.20x faster                                                   |
| pickle_list          | 4.56 us                                                | 4.00 us: 1.14x faster                                                   |
| xml_etree_parse      | 163 ms                                                 | 149 ms: 1.09x faster                                                    |
| unpickle             | 14.1 us                                                | 13.0 us: 1.08x faster                                                   |
| xml_etree_iterparse  | 111 ms                                                 | 107 ms: 1.04x faster                                                    |
| pickle               | 10.3 us                                                | 9.96 us: 1.03x faster                                                   |
| unpickle_list        | 4.82 us                                                | 4.94 us: 1.03x slower                                                   |
| pickle_dict          | 27.3 us                                                | 29.8 us: 1.10x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.19x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230105-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3+-d501577 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.48 ms: 1.67x faster                                                   |
| python_startup_no_site | 5.82 ms                                                | 6.07 ms: 1.04x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.26x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230105-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3+-d501577 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.71 ms: 1.52x faster                                                   |
| genshi_text     | 30.3 ms                                                | 20.3 ms: 1.49x faster                                                   |
| django_template | 45.9 ms                                                | 32.7 ms: 1.40x faster                                                   |
| genshi_xml      | 63.3 ms                                                | 46.6 ms: 1.36x faster                                                   |
| Geometric mean  | (ref)                                                  | 1.44x faster                                                            |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230105-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3+-d501577 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deltablue               | 7.42 ms                                                | 3.23 ms: 2.30x faster                                                   |
| logging_silent          | 175 ns                                                 | 92.5 ns: 1.89x faster                                                   |
| scimark_sor             | 197 ms                                                 | 108 ms: 1.82x faster                                                    |
| richards                | 74.9 ms                                                | 41.3 ms: 1.82x faster                                                   |
| go                      | 229 ms                                                 | 134 ms: 1.71x faster                                                    |
| pyflate                 | 673 ms                                                 | 401 ms: 1.68x faster                                                    |
| scimark_monte_carlo     | 108 ms                                                 | 64.6 ms: 1.68x faster                                                   |
| python_startup          | 14.2 ms                                                | 8.48 ms: 1.67x faster                                                   |
| raytrace                | 464 ms                                                 | 284 ms: 1.63x faster                                                    |
| pickle_pure_python      | 455 us                                                 | 283 us: 1.61x faster                                                    |
| crypto_pyaes            | 118 ms                                                 | 74.3 ms: 1.59x faster                                                   |
| chaos                   | 106 ms                                                 | 67.5 ms: 1.57x faster                                                   |
| hexiom                  | 9.53 ms                                                | 6.06 ms: 1.57x faster                                                   |
| spectral_norm           | 150 ms                                                 | 95.9 ms: 1.56x faster                                                   |
| float                   | 111 ms                                                 | 71.9 ms: 1.54x faster                                                   |
| unpack_sequence         | 64.7 ns                                                | 42.5 ns: 1.52x faster                                                   |
| deepcopy_memo           | 52.3 us                                                | 34.4 us: 1.52x faster                                                   |
| mako                    | 14.8 ms                                                | 9.71 ms: 1.52x faster                                                   |
| nbody                   | 142 ms                                                 | 93.4 ms: 1.52x faster                                                   |
| scimark_lu              | 163 ms                                                 | 108 ms: 1.51x faster                                                    |
| unpickle_pure_python    | 300 us                                                 | 199 us: 1.51x faster                                                    |
| genshi_text             | 30.3 ms                                                | 20.3 ms: 1.49x faster                                                   |
| sqlglot_parse           | 2.06 ms                                                | 1.40 ms: 1.47x faster                                                   |
| chameleon               | 9.06 ms                                                | 6.23 ms: 1.45x faster                                                   |
| sqlglot_transpile       | 2.45 ms                                                | 1.69 ms: 1.45x faster                                                   |
| json_dumps              | 13.5 ms                                                | 9.36 ms: 1.45x faster                                                   |
| pprint_pformat          | 1.99 sec                                               | 1.38 sec: 1.44x faster                                                  |
| html5lib                | 85.9 ms                                                | 59.9 ms: 1.43x faster                                                   |
| pprint_safe_repr        | 955 ms                                                 | 674 ms: 1.42x faster                                                    |
| logging_simple          | 8.07 us                                                | 5.72 us: 1.41x faster                                                   |
| django_template         | 45.9 ms                                                | 32.7 ms: 1.40x faster                                                   |
| logging_format          | 8.91 us                                                | 6.35 us: 1.40x faster                                                   |
| xml_etree_process       | 74.9 ms                                                | 53.7 ms: 1.39x faster                                                   |
| thrift                  | 1.03 ms                                                | 743 us: 1.39x faster                                                    |
| scimark_sparse_mat_mult | 5.45 ms                                                | 3.98 ms: 1.37x faster                                                   |
| regex_compile           | 177 ms                                                 | 129 ms: 1.37x faster                                                    |
| scimark_fft             | 424 ms                                                 | 310 ms: 1.36x faster                                                    |
| async_tree_none         | 717 ms                                                 | 527 ms: 1.36x faster                                                    |
| genshi_xml              | 63.3 ms                                                | 46.6 ms: 1.36x faster                                                   |
| async_tree_io           | 1.77 sec                                               | 1.32 sec: 1.34x faster                                                  |
| async_tree_memoization  | 854 ms                                                 | 638 ms: 1.34x faster                                                    |
| fannkuch                | 486 ms                                                 | 363 ms: 1.34x faster                                                    |
| 2to3                    | 336 ms                                                 | 252 ms: 1.33x faster                                                    |
| deepcopy                | 442 us                                                 | 334 us: 1.32x faster                                                    |
| pycparser               | 1.50 sec                                               | 1.15 sec: 1.31x faster                                                  |
| deepcopy_reduce         | 3.82 us                                                | 2.97 us: 1.29x faster                                                   |
| sqlglot_optimize        | 65.3 ms                                                | 51.0 ms: 1.28x faster                                                   |
| sqlglot_normalize       | 135 ms                                                 | 106 ms: 1.28x faster                                                    |
| coroutines              | 31.8 ms                                                | 25.0 ms: 1.27x faster                                                   |
| docutils                | 3.17 sec                                               | 2.49 sec: 1.27x faster                                                  |
| async_tree_cpu_io_mixed | 951 ms                                                 | 758 ms: 1.25x faster                                                    |
| nqueens                 | 100 ms                                                 | 80.8 ms: 1.24x faster                                                   |
| dulwich_log             | 75.9 ms                                                | 62.0 ms: 1.22x faster                                                   |
| xml_etree_generate      | 94.2 ms                                                | 77.0 ms: 1.22x faster                                                   |
| bench_thread_pool       | 947 us                                                 | 777 us: 1.22x faster                                                    |
| async_generators        | 425 ms                                                 | 352 ms: 1.21x faster                                                    |
| json_loads              | 28.8 us                                                | 23.9 us: 1.20x faster                                                   |
| sympy_expand            | 545 ms                                                 | 455 ms: 1.20x faster                                                    |
| sympy_integrate         | 24.3 ms                                                | 20.3 ms: 1.19x faster                                                   |
| sympy_str               | 328 ms                                                 | 281 ms: 1.17x faster                                                    |
| json                    | 5.42 ms                                                | 4.69 ms: 1.16x faster                                                   |
| pickle_list             | 4.56 us                                                | 4.00 us: 1.14x faster                                                   |
| sympy_sum               | 185 ms                                                 | 163 ms: 1.13x faster                                                    |
| sqlite_synth            | 2.93 us                                                | 2.59 us: 1.13x faster                                                   |
| regex_v8                | 25.0 ms                                                | 22.5 ms: 1.11x faster                                                   |
| meteor_contest          | 115 ms                                                 | 104 ms: 1.10x faster                                                    |
| djangocms               | 35.9 us                                                | 32.6 us: 1.10x faster                                                   |
| pathlib                 | 20.0 ms                                                | 18.2 ms: 1.10x faster                                                   |
| xml_etree_parse         | 163 ms                                                 | 149 ms: 1.09x faster                                                    |
| unpickle                | 14.1 us                                                | 13.0 us: 1.08x faster                                                   |
| regex_dna               | 222 ms                                                 | 208 ms: 1.07x faster                                                    |
| xml_etree_iterparse     | 111 ms                                                 | 107 ms: 1.04x faster                                                    |
| pickle                  | 10.3 us                                                | 9.96 us: 1.03x faster                                                   |
| mdp                     | 2.82 sec                                               | 2.74 sec: 1.03x faster                                                  |
| telco                   | 6.54 ms                                                | 6.36 ms: 1.03x faster                                                   |
| generators              | 76.8 ms                                                | 75.4 ms: 1.02x faster                                                   |
| unpickle_list           | 4.82 us                                                | 4.94 us: 1.03x slower                                                   |
| pidigits                | 190 ms                                                 | 198 ms: 1.04x slower                                                    |
| python_startup_no_site  | 5.82 ms                                                | 6.07 ms: 1.04x slower                                                   |
| pickle_dict             | 27.3 us                                                | 29.8 us: 1.10x slower                                                   |
| regex_effbot            | 3.23 ms                                                | 3.60 ms: 1.11x slower                                                   |
| coverage                | 72.8 ms                                                | 100 ms: 1.38x slower                                                    |
| Geometric mean          | (ref)                                                  | 1.31x faster                                                            |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, comprehensions, create_gc_cycles, dask, flaskblogging, gc_traversal, gunicorn, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, tornado_http, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230105-3.12.0a3+-d501577/bm-20230105-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3+-d501577.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.26x
