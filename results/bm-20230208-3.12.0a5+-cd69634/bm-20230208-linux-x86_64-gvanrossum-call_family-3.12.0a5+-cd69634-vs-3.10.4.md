
# Results vs. 3.10.4

- fork: gvanrossum
- ref: call_family
- machine: linux-x86_64
- commit hash: cd69634
- commit date: 2023-02-08
- overall geometric mean: 1.30x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.27x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230208-linux-x86_64-gvanrossum-call_family-3.12.0a5+-cd69634 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 251 ms: 1.34x faster                                              |
| chameleon      | 9.06 ms                                                | 6.44 ms: 1.41x faster                                             |
| docutils       | 3.17 sec                                               | 2.50 sec: 1.27x faster                                            |
| html5lib       | 85.9 ms                                                | 60.7 ms: 1.41x faster                                             |
| tornado_http   | 127 ms                                                 | 94.3 ms: 1.35x faster                                             |
| Geometric mean | (ref)                                                  | 1.36x faster                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230208-linux-x86_64-gvanrossum-call_family-3.12.0a5+-cd69634 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 94.6 ms: 1.50x faster                                             |
| float          | 111 ms                                                 | 74.0 ms: 1.49x faster                                             |
| pidigits       | 190 ms                                                 | 189 ms: 1.00x faster                                              |
| Geometric mean | (ref)                                                  | 1.31x faster                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230208-linux-x86_64-gvanrossum-call_family-3.12.0a5+-cd69634 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 129 ms: 1.37x faster                                              |
| regex_v8       | 25.0 ms                                                | 21.0 ms: 1.20x faster                                             |
| regex_dna      | 222 ms                                                 | 206 ms: 1.08x faster                                              |
| regex_effbot   | 3.23 ms                                                | 3.64 ms: 1.13x slower                                             |
| Geometric mean | (ref)                                                  | 1.12x faster                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230208-linux-x86_64-gvanrossum-call_family-3.12.0a5+-cd69634 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 286 us: 1.59x faster                                              |
| unpickle_pure_python | 300 us                                                 | 199 us: 1.51x faster                                              |
| json_dumps           | 13.5 ms                                                | 9.44 ms: 1.43x faster                                             |
| xml_etree_process    | 74.9 ms                                                | 53.2 ms: 1.41x faster                                             |
| xml_etree_generate   | 94.2 ms                                                | 77.1 ms: 1.22x faster                                             |
| json_loads           | 28.8 us                                                | 23.8 us: 1.21x faster                                             |
| pickle_list          | 4.56 us                                                | 4.03 us: 1.13x faster                                             |
| xml_etree_parse      | 163 ms                                                 | 146 ms: 1.12x faster                                              |
| xml_etree_iterparse  | 111 ms                                                 | 102 ms: 1.09x faster                                              |
| unpickle             | 14.1 us                                                | 13.0 us: 1.09x faster                                             |
| pickle               | 10.3 us                                                | 10.1 us: 1.01x faster                                             |
| unpickle_list        | 4.82 us                                                | 4.97 us: 1.03x slower                                             |
| pickle_dict          | 27.3 us                                                | 30.3 us: 1.11x slower                                             |
| Geometric mean       | (ref)                                                  | 1.19x faster                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230208-linux-x86_64-gvanrossum-call_family-3.12.0a5+-cd69634 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.91 ms: 1.59x faster                                             |
| python_startup_no_site | 5.82 ms                                                | 6.47 ms: 1.11x slower                                             |
| Geometric mean         | (ref)                                                  | 1.20x faster                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230208-linux-x86_64-gvanrossum-call_family-3.12.0a5+-cd69634 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.97 ms: 1.48x faster                                             |
| genshi_text     | 30.3 ms                                                | 20.5 ms: 1.48x faster                                             |
| django_template | 45.9 ms                                                | 33.2 ms: 1.38x faster                                             |
| genshi_xml      | 63.3 ms                                                | 47.1 ms: 1.34x faster                                             |
| Geometric mean  | (ref)                                                  | 1.42x faster                                                      |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230208-linux-x86_64-gvanrossum-call_family-3.12.0a5+-cd69634 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| deltablue               | 7.42 ms                                                | 3.17 ms: 2.34x faster                                             |
| asyncio_tcp             | 925 ms                                                 | 490 ms: 1.89x faster                                              |
| scimark_sor             | 197 ms                                                 | 105 ms: 1.88x faster                                              |
| logging_silent          | 175 ns                                                 | 96.3 ns: 1.82x faster                                             |
| richards                | 74.9 ms                                                | 42.3 ms: 1.77x faster                                             |
| go                      | 229 ms                                                 | 138 ms: 1.66x faster                                              |
| pyflate                 | 673 ms                                                 | 407 ms: 1.65x faster                                              |
| scimark_monte_carlo     | 108 ms                                                 | 65.8 ms: 1.64x faster                                             |
| crypto_pyaes            | 118 ms                                                 | 72.7 ms: 1.63x faster                                             |
| raytrace                | 464 ms                                                 | 288 ms: 1.61x faster                                              |
| pickle_pure_python      | 455 us                                                 | 286 us: 1.59x faster                                              |
| chaos                   | 106 ms                                                 | 66.7 ms: 1.59x faster                                             |
| python_startup          | 14.2 ms                                                | 8.91 ms: 1.59x faster                                             |
| hexiom                  | 9.53 ms                                                | 6.02 ms: 1.58x faster                                             |
| spectral_norm           | 150 ms                                                 | 96.1 ms: 1.56x faster                                             |
| unpickle_pure_python    | 300 us                                                 | 199 us: 1.51x faster                                              |
| scimark_lu              | 163 ms                                                 | 108 ms: 1.51x faster                                              |
| deepcopy_memo           | 52.3 us                                                | 34.9 us: 1.50x faster                                             |
| nbody                   | 142 ms                                                 | 94.6 ms: 1.50x faster                                             |
| float                   | 111 ms                                                 | 74.0 ms: 1.49x faster                                             |
| mako                    | 14.8 ms                                                | 9.97 ms: 1.48x faster                                             |
| genshi_text             | 30.3 ms                                                | 20.5 ms: 1.48x faster                                             |
| unpack_sequence         | 64.7 ns                                                | 44.4 ns: 1.46x faster                                             |
| json_dumps              | 13.5 ms                                                | 9.44 ms: 1.43x faster                                             |
| sqlglot_parse           | 2.06 ms                                                | 1.44 ms: 1.43x faster                                             |
| html5lib                | 85.9 ms                                                | 60.7 ms: 1.41x faster                                             |
| sqlglot_transpile       | 2.45 ms                                                | 1.74 ms: 1.41x faster                                             |
| xml_etree_process       | 74.9 ms                                                | 53.2 ms: 1.41x faster                                             |
| chameleon               | 9.06 ms                                                | 6.44 ms: 1.41x faster                                             |
| thrift                  | 1.03 ms                                                | 740 us: 1.40x faster                                              |
| pprint_pformat          | 1.99 sec                                               | 1.43 sec: 1.39x faster                                            |
| scimark_fft             | 424 ms                                                 | 305 ms: 1.39x faster                                              |
| django_template         | 45.9 ms                                                | 33.2 ms: 1.38x faster                                             |
| logging_format          | 8.91 us                                                | 6.46 us: 1.38x faster                                             |
| pycparser               | 1.50 sec                                               | 1.09 sec: 1.38x faster                                            |
| aiohttp                 | 1.38 ms                                                | 1.00 ms: 1.38x faster                                             |
| logging_simple          | 8.07 us                                                | 5.88 us: 1.37x faster                                             |
| regex_compile           | 177 ms                                                 | 129 ms: 1.37x faster                                              |
| pprint_safe_repr        | 955 ms                                                 | 697 ms: 1.37x faster                                              |
| async_tree_none         | 717 ms                                                 | 524 ms: 1.37x faster                                              |
| fannkuch                | 486 ms                                                 | 356 ms: 1.37x faster                                              |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.01 ms: 1.36x faster                                             |
| gunicorn                | 1.46 ms                                                | 1.08 ms: 1.35x faster                                             |
| tornado_http            | 127 ms                                                 | 94.3 ms: 1.35x faster                                             |
| genshi_xml              | 63.3 ms                                                | 47.1 ms: 1.34x faster                                             |
| async_tree_io           | 1.77 sec                                               | 1.32 sec: 1.34x faster                                            |
| async_tree_memoization  | 854 ms                                                 | 637 ms: 1.34x faster                                              |
| 2to3                    | 336 ms                                                 | 251 ms: 1.34x faster                                              |
| deepcopy                | 442 us                                                 | 332 us: 1.33x faster                                              |
| coroutines              | 31.8 ms                                                | 24.3 ms: 1.31x faster                                             |
| mypy2                   | 428 ms                                                 | 331 ms: 1.29x faster                                              |
| deepcopy_reduce         | 3.82 us                                                | 2.96 us: 1.29x faster                                             |
| sqlglot_normalize       | 135 ms                                                 | 106 ms: 1.28x faster                                              |
| sqlglot_optimize        | 65.3 ms                                                | 51.4 ms: 1.27x faster                                             |
| docutils                | 3.17 sec                                               | 2.50 sec: 1.27x faster                                            |
| async_tree_cpu_io_mixed | 951 ms                                                 | 752 ms: 1.26x faster                                              |
| nqueens                 | 100 ms                                                 | 79.2 ms: 1.26x faster                                             |
| async_generators        | 425 ms                                                 | 346 ms: 1.23x faster                                              |
| sympy_integrate         | 24.3 ms                                                | 19.8 ms: 1.23x faster                                             |
| xml_etree_generate      | 94.2 ms                                                | 77.1 ms: 1.22x faster                                             |
| sympy_str               | 328 ms                                                 | 270 ms: 1.22x faster                                              |
| bench_thread_pool       | 947 us                                                 | 783 us: 1.21x faster                                              |
| json_loads              | 28.8 us                                                | 23.8 us: 1.21x faster                                             |
| sqlalchemy_declarative  | 165 ms                                                 | 137 ms: 1.20x faster                                              |
| sympy_expand            | 545 ms                                                 | 454 ms: 1.20x faster                                              |
| dulwich_log             | 75.9 ms                                                | 63.4 ms: 1.20x faster                                             |
| regex_v8                | 25.0 ms                                                | 21.0 ms: 1.20x faster                                             |
| sympy_sum               | 185 ms                                                 | 156 ms: 1.18x faster                                              |
| sqlalchemy_imperative   | 21.2 ms                                                | 18.1 ms: 1.17x faster                                             |
| json                    | 5.42 ms                                                | 4.64 ms: 1.17x faster                                             |
| create_gc_cycles        | 1.67 ms                                                | 1.46 ms: 1.14x faster                                             |
| mdp                     | 2.82 sec                                               | 2.48 sec: 1.14x faster                                            |
| pickle_list             | 4.56 us                                                | 4.03 us: 1.13x faster                                             |
| sqlite_synth            | 2.93 us                                                | 2.60 us: 1.13x faster                                             |
| djangocms               | 35.9 us                                                | 31.8 us: 1.13x faster                                             |
| xml_etree_parse         | 163 ms                                                 | 146 ms: 1.12x faster                                              |
| pathlib                 | 20.0 ms                                                | 18.0 ms: 1.11x faster                                             |
| xml_etree_iterparse     | 111 ms                                                 | 102 ms: 1.09x faster                                              |
| unpickle                | 14.1 us                                                | 13.0 us: 1.09x faster                                             |
| regex_dna               | 222 ms                                                 | 206 ms: 1.08x faster                                              |
| meteor_contest          | 115 ms                                                 | 107 ms: 1.08x faster                                              |
| generators              | 76.8 ms                                                | 72.1 ms: 1.06x faster                                             |
| telco                   | 6.54 ms                                                | 6.36 ms: 1.03x faster                                             |
| pickle                  | 10.3 us                                                | 10.1 us: 1.01x faster                                             |
| pidigits                | 190 ms                                                 | 189 ms: 1.00x faster                                              |
| unpickle_list           | 4.82 us                                                | 4.97 us: 1.03x slower                                             |
| gc_traversal            | 3.84 ms                                                | 4.17 ms: 1.09x slower                                             |
| python_startup_no_site  | 5.82 ms                                                | 6.47 ms: 1.11x slower                                             |
| pickle_dict             | 27.3 us                                                | 30.3 us: 1.11x slower                                             |
| regex_effbot            | 3.23 ms                                                | 3.64 ms: 1.13x slower                                             |
| coverage                | 72.8 ms                                                | 98.8 ms: 1.36x slower                                             |
| Geometric mean          | (ref)                                                  | 1.30x faster                                                      |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, comprehensions, dask, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.30x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.27x
