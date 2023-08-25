
# Results vs. 3.10.4

- fork: iritkatriel
- ref: InitializeHeader
- machine: linux-x86_64
- commit hash: e73d0cf
- commit date: 2023-01-04
- overall geometric mean: 1.31x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230104-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3+-e73d0cf |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 252 ms: 1.33x faster                                                    |
| chameleon      | 9.06 ms                                                | 6.17 ms: 1.47x faster                                                   |
| docutils       | 3.17 sec                                               | 2.51 sec: 1.26x faster                                                  |
| html5lib       | 85.9 ms                                                | 60.1 ms: 1.43x faster                                                   |
| Geometric mean | (ref)                                                  | 1.37x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230104-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3+-e73d0cf |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 111 ms                                                 | 71.7 ms: 1.54x faster                                                   |
| nbody          | 142 ms                                                 | 92.8 ms: 1.52x faster                                                   |
| pidigits       | 190 ms                                                 | 192 ms: 1.01x slower                                                    |
| Geometric mean | (ref)                                                  | 1.32x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230104-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3+-e73d0cf |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 131 ms: 1.35x faster                                                    |
| regex_v8       | 25.0 ms                                                | 22.5 ms: 1.11x faster                                                   |
| regex_dna      | 222 ms                                                 | 211 ms: 1.05x faster                                                    |
| regex_effbot   | 3.23 ms                                                | 3.58 ms: 1.11x slower                                                   |
| Geometric mean | (ref)                                                  | 1.09x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230104-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3+-e73d0cf |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 282 us: 1.61x faster                                                    |
| unpickle_pure_python | 300 us                                                 | 196 us: 1.53x faster                                                    |
| json_dumps           | 13.5 ms                                                | 9.42 ms: 1.44x faster                                                   |
| xml_etree_process    | 74.9 ms                                                | 53.7 ms: 1.40x faster                                                   |
| xml_etree_generate   | 94.2 ms                                                | 75.7 ms: 1.24x faster                                                   |
| json_loads           | 28.8 us                                                | 24.0 us: 1.20x faster                                                   |
| pickle_list          | 4.56 us                                                | 4.11 us: 1.11x faster                                                   |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                                    |
| unpickle             | 14.1 us                                                | 13.2 us: 1.07x faster                                                   |
| xml_etree_iterparse  | 111 ms                                                 | 104 ms: 1.07x faster                                                    |
| pickle               | 10.3 us                                                | 10.2 us: 1.01x faster                                                   |
| unpickle_list        | 4.82 us                                                | 4.94 us: 1.02x slower                                                   |
| pickle_dict          | 27.3 us                                                | 30.4 us: 1.12x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.18x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230104-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3+-e73d0cf |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.48 ms: 1.67x faster                                                   |
| python_startup_no_site | 5.82 ms                                                | 6.08 ms: 1.04x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.26x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230104-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3+-e73d0cf |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.83 ms: 1.50x faster                                                   |
| genshi_text     | 30.3 ms                                                | 20.4 ms: 1.48x faster                                                   |
| django_template | 45.9 ms                                                | 32.3 ms: 1.42x faster                                                   |
| genshi_xml      | 63.3 ms                                                | 46.3 ms: 1.37x faster                                                   |
| Geometric mean  | (ref)                                                  | 1.44x faster                                                            |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230104-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3+-e73d0cf |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deltablue               | 7.42 ms                                                | 3.34 ms: 2.22x faster                                                   |
| logging_silent          | 175 ns                                                 | 90.4 ns: 1.94x faster                                                   |
| scimark_sor             | 197 ms                                                 | 107 ms: 1.85x faster                                                    |
| richards                | 74.9 ms                                                | 42.4 ms: 1.77x faster                                                   |
| pyflate                 | 673 ms                                                 | 391 ms: 1.72x faster                                                    |
| go                      | 229 ms                                                 | 135 ms: 1.70x faster                                                    |
| scimark_monte_carlo     | 108 ms                                                 | 64.4 ms: 1.68x faster                                                   |
| python_startup          | 14.2 ms                                                | 8.48 ms: 1.67x faster                                                   |
| raytrace                | 464 ms                                                 | 282 ms: 1.65x faster                                                    |
| pickle_pure_python      | 455 us                                                 | 282 us: 1.61x faster                                                    |
| crypto_pyaes            | 118 ms                                                 | 73.5 ms: 1.61x faster                                                   |
| chaos                   | 106 ms                                                 | 67.9 ms: 1.57x faster                                                   |
| hexiom                  | 9.53 ms                                                | 6.09 ms: 1.56x faster                                                   |
| unpack_sequence         | 64.7 ns                                                | 41.5 ns: 1.56x faster                                                   |
| deepcopy_memo           | 52.3 us                                                | 33.7 us: 1.55x faster                                                   |
| float                   | 111 ms                                                 | 71.7 ms: 1.54x faster                                                   |
| spectral_norm           | 150 ms                                                 | 97.5 ms: 1.54x faster                                                   |
| unpickle_pure_python    | 300 us                                                 | 196 us: 1.53x faster                                                    |
| scimark_lu              | 163 ms                                                 | 107 ms: 1.53x faster                                                    |
| nbody                   | 142 ms                                                 | 92.8 ms: 1.52x faster                                                   |
| mako                    | 14.8 ms                                                | 9.83 ms: 1.50x faster                                                   |
| genshi_text             | 30.3 ms                                                | 20.4 ms: 1.48x faster                                                   |
| chameleon               | 9.06 ms                                                | 6.17 ms: 1.47x faster                                                   |
| sqlglot_parse           | 2.06 ms                                                | 1.41 ms: 1.46x faster                                                   |
| pprint_pformat          | 1.99 sec                                               | 1.38 sec: 1.44x faster                                                  |
| json_dumps              | 13.5 ms                                                | 9.42 ms: 1.44x faster                                                   |
| sqlglot_transpile       | 2.45 ms                                                | 1.71 ms: 1.43x faster                                                   |
| html5lib                | 85.9 ms                                                | 60.1 ms: 1.43x faster                                                   |
| django_template         | 45.9 ms                                                | 32.3 ms: 1.42x faster                                                   |
| pprint_safe_repr        | 955 ms                                                 | 674 ms: 1.42x faster                                                    |
| logging_format          | 8.91 us                                                | 6.35 us: 1.40x faster                                                   |
| logging_simple          | 8.07 us                                                | 5.76 us: 1.40x faster                                                   |
| xml_etree_process       | 74.9 ms                                                | 53.7 ms: 1.40x faster                                                   |
| thrift                  | 1.03 ms                                                | 753 us: 1.37x faster                                                    |
| async_tree_memoization  | 854 ms                                                 | 623 ms: 1.37x faster                                                    |
| async_tree_none         | 717 ms                                                 | 524 ms: 1.37x faster                                                    |
| genshi_xml              | 63.3 ms                                                | 46.3 ms: 1.37x faster                                                   |
| scimark_fft             | 424 ms                                                 | 313 ms: 1.35x faster                                                    |
| async_tree_io           | 1.77 sec                                               | 1.32 sec: 1.35x faster                                                  |
| regex_compile           | 177 ms                                                 | 131 ms: 1.35x faster                                                    |
| deepcopy                | 442 us                                                 | 330 us: 1.34x faster                                                    |
| 2to3                    | 336 ms                                                 | 252 ms: 1.33x faster                                                    |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.10 ms: 1.33x faster                                                   |
| fannkuch                | 486 ms                                                 | 368 ms: 1.32x faster                                                    |
| deepcopy_reduce         | 3.82 us                                                | 2.90 us: 1.32x faster                                                   |
| pycparser               | 1.50 sec                                               | 1.15 sec: 1.31x faster                                                  |
| sqlglot_normalize       | 135 ms                                                 | 105 ms: 1.29x faster                                                    |
| sqlglot_optimize        | 65.3 ms                                                | 50.8 ms: 1.29x faster                                                   |
| coroutines              | 31.8 ms                                                | 25.0 ms: 1.27x faster                                                   |
| async_tree_cpu_io_mixed | 951 ms                                                 | 750 ms: 1.27x faster                                                    |
| docutils                | 3.17 sec                                               | 2.51 sec: 1.26x faster                                                  |
| xml_etree_generate      | 94.2 ms                                                | 75.7 ms: 1.24x faster                                                   |
| nqueens                 | 100 ms                                                 | 80.6 ms: 1.24x faster                                                   |
| dulwich_log             | 75.9 ms                                                | 62.0 ms: 1.22x faster                                                   |
| bench_thread_pool       | 947 us                                                 | 774 us: 1.22x faster                                                    |
| json_loads              | 28.8 us                                                | 24.0 us: 1.20x faster                                                   |
| async_generators        | 425 ms                                                 | 355 ms: 1.20x faster                                                    |
| sympy_expand            | 545 ms                                                 | 456 ms: 1.19x faster                                                    |
| sympy_integrate         | 24.3 ms                                                | 20.4 ms: 1.19x faster                                                   |
| sympy_str               | 328 ms                                                 | 282 ms: 1.17x faster                                                    |
| json                    | 5.42 ms                                                | 4.73 ms: 1.15x faster                                                   |
| sqlite_synth            | 2.93 us                                                | 2.59 us: 1.13x faster                                                   |
| sympy_sum               | 185 ms                                                 | 163 ms: 1.13x faster                                                    |
| djangocms               | 35.9 us                                                | 32.3 us: 1.11x faster                                                   |
| regex_v8                | 25.0 ms                                                | 22.5 ms: 1.11x faster                                                   |
| pickle_list             | 4.56 us                                                | 4.11 us: 1.11x faster                                                   |
| pathlib                 | 20.0 ms                                                | 18.1 ms: 1.11x faster                                                   |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                                    |
| mdp                     | 2.82 sec                                               | 2.57 sec: 1.10x faster                                                  |
| meteor_contest          | 115 ms                                                 | 105 ms: 1.09x faster                                                    |
| unpickle                | 14.1 us                                                | 13.2 us: 1.07x faster                                                   |
| xml_etree_iterparse     | 111 ms                                                 | 104 ms: 1.07x faster                                                    |
| regex_dna               | 222 ms                                                 | 211 ms: 1.05x faster                                                    |
| telco                   | 6.54 ms                                                | 6.41 ms: 1.02x faster                                                   |
| pickle                  | 10.3 us                                                | 10.2 us: 1.01x faster                                                   |
| generators              | 76.8 ms                                                | 77.1 ms: 1.00x slower                                                   |
| pidigits                | 190 ms                                                 | 192 ms: 1.01x slower                                                    |
| unpickle_list           | 4.82 us                                                | 4.94 us: 1.02x slower                                                   |
| python_startup_no_site  | 5.82 ms                                                | 6.08 ms: 1.04x slower                                                   |
| regex_effbot            | 3.23 ms                                                | 3.58 ms: 1.11x slower                                                   |
| pickle_dict             | 27.3 us                                                | 30.4 us: 1.12x slower                                                   |
| coverage                | 72.8 ms                                                | 98.7 ms: 1.36x slower                                                   |
| Geometric mean          | (ref)                                                  | 1.31x faster                                                            |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, comprehensions, create_gc_cycles, dask, flaskblogging, gc_traversal, gunicorn, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, tornado_http, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230104-3.12.0a3+-e73d0cf/bm-20230104-linux-x86_64-iritkatriel-InitializeHeader-3.12.0a3+-e73d0cf.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.26x
