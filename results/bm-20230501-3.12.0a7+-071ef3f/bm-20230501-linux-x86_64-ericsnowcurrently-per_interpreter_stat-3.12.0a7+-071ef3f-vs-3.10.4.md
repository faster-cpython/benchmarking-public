
# Results vs. 3.10.4

- fork: ericsnowcurrently
- ref: per_interpreter_stat
- machine: linux-x86_64
- commit hash: 071ef3f
- commit date: 2023-05-01
- overall geometric mean: 1.24x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230501-linux-x86_64-ericsnowcurrently-per_interpreter_stat-3.12.0a7+-071ef3f |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 271 ms: 1.24x faster                                                              |
| docutils       | 3.17 sec                                               | 2.72 sec: 1.16x faster                                                            |
| html5lib       | 85.9 ms                                                | 64.9 ms: 1.32x faster                                                             |
| tornado_http   | 127 ms                                                 | 102 ms: 1.25x faster                                                              |
| Geometric mean | (ref)                                                  | 1.24x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230501-linux-x86_64-ericsnowcurrently-per_interpreter_stat-3.12.0a7+-071ef3f |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 87.4 ms: 1.62x faster                                                             |
| float          | 111 ms                                                 | 81.2 ms: 1.36x faster                                                             |
| pidigits       | 190 ms                                                 | 189 ms: 1.01x faster                                                              |
| Geometric mean | (ref)                                                  | 1.30x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230501-linux-x86_64-ericsnowcurrently-per_interpreter_stat-3.12.0a7+-071ef3f |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 144 ms: 1.23x faster                                                              |
| regex_v8       | 25.0 ms                                                | 22.4 ms: 1.12x faster                                                             |
| regex_dna      | 222 ms                                                 | 209 ms: 1.06x faster                                                              |
| regex_effbot   | 3.23 ms                                                | 3.40 ms: 1.05x slower                                                             |
| Geometric mean | (ref)                                                  | 1.08x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230501-linux-x86_64-ericsnowcurrently-per_interpreter_stat-3.12.0a7+-071ef3f |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 316 us: 1.44x faster                                                              |
| unpickle_pure_python | 300 us                                                 | 218 us: 1.38x faster                                                              |
| json_dumps           | 13.5 ms                                                | 10.1 ms: 1.34x faster                                                             |
| xml_etree_process    | 74.9 ms                                                | 60.4 ms: 1.24x faster                                                             |
| json_loads           | 28.8 us                                                | 25.9 us: 1.11x faster                                                             |
| xml_etree_generate   | 94.2 ms                                                | 85.8 ms: 1.10x faster                                                             |
| xml_etree_iterparse  | 111 ms                                                 | 104 ms: 1.07x faster                                                              |
| xml_etree_parse      | 163 ms                                                 | 153 ms: 1.06x faster                                                              |
| pickle_list          | 4.56 us                                                | 4.60 us: 1.01x slower                                                             |
| unpickle             | 14.1 us                                                | 14.4 us: 1.02x slower                                                             |
| unpickle_list        | 4.82 us                                                | 4.95 us: 1.03x slower                                                             |
| pickle               | 10.3 us                                                | 10.8 us: 1.05x slower                                                             |
| pickle_dict          | 27.3 us                                                | 32.4 us: 1.19x slower                                                             |
| Geometric mean       | (ref)                                                  | 1.10x faster                                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230501-linux-x86_64-ericsnowcurrently-per_interpreter_stat-3.12.0a7+-071ef3f |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.15 ms: 1.55x faster                                                             |
| python_startup_no_site | 5.82 ms                                                | 6.71 ms: 1.15x slower                                                             |
| Geometric mean         | (ref)                                                  | 1.16x faster                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230501-linux-x86_64-ericsnowcurrently-per_interpreter_stat-3.12.0a7+-071ef3f |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako           | 14.8 ms                                                | 10.7 ms: 1.38x faster                                                             |
| genshi_text    | 30.3 ms                                                | 22.3 ms: 1.36x faster                                                             |
| genshi_xml     | 63.3 ms                                                | 50.8 ms: 1.25x faster                                                             |
| Geometric mean | (ref)                                                  | 1.33x faster                                                                      |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230501-linux-x86_64-ericsnowcurrently-per_interpreter_stat-3.12.0a7+-071ef3f |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| generators              | 76.8 ms                                                | 30.7 ms: 2.50x faster                                                             |
| deltablue               | 7.42 ms                                                | 3.47 ms: 2.14x faster                                                             |
| asyncio_tcp             | 925 ms                                                 | 513 ms: 1.80x faster                                                              |
| logging_silent          | 175 ns                                                 | 99.0 ns: 1.77x faster                                                             |
| richards                | 74.9 ms                                                | 43.2 ms: 1.74x faster                                                             |
| go                      | 229 ms                                                 | 136 ms: 1.69x faster                                                              |
| scimark_sor             | 197 ms                                                 | 121 ms: 1.62x faster                                                              |
| nbody                   | 142 ms                                                 | 87.4 ms: 1.62x faster                                                             |
| hexiom                  | 9.53 ms                                                | 6.12 ms: 1.56x faster                                                             |
| python_startup          | 14.2 ms                                                | 9.15 ms: 1.55x faster                                                             |
| raytrace                | 464 ms                                                 | 302 ms: 1.54x faster                                                              |
| sqlglot_parse           | 2.06 ms                                                | 1.34 ms: 1.54x faster                                                             |
| chaos                   | 106 ms                                                 | 69.3 ms: 1.53x faster                                                             |
| crypto_pyaes            | 118 ms                                                 | 77.9 ms: 1.52x faster                                                             |
| pyflate                 | 673 ms                                                 | 449 ms: 1.50x faster                                                              |
| scimark_monte_carlo     | 108 ms                                                 | 72.5 ms: 1.49x faster                                                             |
| sqlglot_transpile       | 2.45 ms                                                | 1.67 ms: 1.47x faster                                                             |
| scimark_lu              | 163 ms                                                 | 112 ms: 1.46x faster                                                              |
| spectral_norm           | 150 ms                                                 | 104 ms: 1.45x faster                                                              |
| pickle_pure_python      | 455 us                                                 | 316 us: 1.44x faster                                                              |
| async_tree_io           | 1.77 sec                                               | 1.23 sec: 1.44x faster                                                            |
| async_tree_none         | 717 ms                                                 | 499 ms: 1.44x faster                                                              |
| coroutines              | 31.8 ms                                                | 22.4 ms: 1.42x faster                                                             |
| async_tree_memoization  | 854 ms                                                 | 612 ms: 1.40x faster                                                              |
| mako                    | 14.8 ms                                                | 10.7 ms: 1.38x faster                                                             |
| unpickle_pure_python    | 300 us                                                 | 218 us: 1.38x faster                                                              |
| deepcopy_memo           | 52.3 us                                                | 38.3 us: 1.37x faster                                                             |
| genshi_text             | 30.3 ms                                                | 22.3 ms: 1.36x faster                                                             |
| float                   | 111 ms                                                 | 81.2 ms: 1.36x faster                                                             |
| json_dumps              | 13.5 ms                                                | 10.1 ms: 1.34x faster                                                             |
| html5lib                | 85.9 ms                                                | 64.9 ms: 1.32x faster                                                             |
| async_tree_cpu_io_mixed | 951 ms                                                 | 720 ms: 1.32x faster                                                              |
| pprint_pformat          | 1.99 sec                                               | 1.51 sec: 1.31x faster                                                            |
| thrift                  | 1.03 ms                                                | 797 us: 1.30x faster                                                              |
| pprint_safe_repr        | 955 ms                                                 | 738 ms: 1.29x faster                                                              |
| logging_simple          | 8.07 us                                                | 6.25 us: 1.29x faster                                                             |
| pycparser               | 1.50 sec                                               | 1.16 sec: 1.29x faster                                                            |
| unpack_sequence         | 64.7 ns                                                | 50.6 ns: 1.28x faster                                                             |
| logging_format          | 8.91 us                                                | 6.98 us: 1.28x faster                                                             |
| fannkuch                | 486 ms                                                 | 381 ms: 1.28x faster                                                              |
| nqueens                 | 100 ms                                                 | 80.0 ms: 1.25x faster                                                             |
| tornado_http            | 127 ms                                                 | 102 ms: 1.25x faster                                                              |
| genshi_xml              | 63.3 ms                                                | 50.8 ms: 1.25x faster                                                             |
| 2to3                    | 336 ms                                                 | 271 ms: 1.24x faster                                                              |
| xml_etree_process       | 74.9 ms                                                | 60.4 ms: 1.24x faster                                                             |
| regex_compile           | 177 ms                                                 | 144 ms: 1.23x faster                                                              |
| mypy2                   | 428 ms                                                 | 352 ms: 1.22x faster                                                              |
| deepcopy                | 442 us                                                 | 367 us: 1.21x faster                                                              |
| sqlglot_normalize       | 135 ms                                                 | 113 ms: 1.20x faster                                                              |
| scimark_fft             | 424 ms                                                 | 355 ms: 1.19x faster                                                              |
| deepcopy_reduce         | 3.82 us                                                | 3.24 us: 1.18x faster                                                             |
| sqlglot_optimize        | 65.3 ms                                                | 55.7 ms: 1.17x faster                                                             |
| docutils                | 3.17 sec                                               | 2.72 sec: 1.16x faster                                                            |
| comprehensions          | 26.8 us                                                | 23.5 us: 1.14x faster                                                             |
| bench_thread_pool       | 947 us                                                 | 834 us: 1.14x faster                                                              |
| sqlalchemy_declarative  | 165 ms                                                 | 147 ms: 1.12x faster                                                              |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.86 ms: 1.12x faster                                                             |
| create_gc_cycles        | 1.67 ms                                                | 1.49 ms: 1.12x faster                                                             |
| pathlib                 | 20.0 ms                                                | 17.9 ms: 1.12x faster                                                             |
| regex_v8                | 25.0 ms                                                | 22.4 ms: 1.12x faster                                                             |
| json_loads              | 28.8 us                                                | 25.9 us: 1.11x faster                                                             |
| dulwich_log             | 75.9 ms                                                | 68.3 ms: 1.11x faster                                                             |
| sqlite_synth            | 2.93 us                                                | 2.67 us: 1.10x faster                                                             |
| sqlalchemy_imperative   | 21.2 ms                                                | 19.3 ms: 1.10x faster                                                             |
| json                    | 5.42 ms                                                | 4.93 ms: 1.10x faster                                                             |
| xml_etree_generate      | 94.2 ms                                                | 85.8 ms: 1.10x faster                                                             |
| mdp                     | 2.82 sec                                               | 2.60 sec: 1.09x faster                                                            |
| xml_etree_iterparse     | 111 ms                                                 | 104 ms: 1.07x faster                                                              |
| xml_etree_parse         | 163 ms                                                 | 153 ms: 1.06x faster                                                              |
| regex_dna               | 222 ms                                                 | 209 ms: 1.06x faster                                                              |
| meteor_contest          | 115 ms                                                 | 113 ms: 1.01x faster                                                              |
| pidigits                | 190 ms                                                 | 189 ms: 1.01x faster                                                              |
| pickle_list             | 4.56 us                                                | 4.60 us: 1.01x slower                                                             |
| unpickle                | 14.1 us                                                | 14.4 us: 1.02x slower                                                             |
| unpickle_list           | 4.82 us                                                | 4.95 us: 1.03x slower                                                             |
| telco                   | 6.54 ms                                                | 6.88 ms: 1.05x slower                                                             |
| pickle                  | 10.3 us                                                | 10.8 us: 1.05x slower                                                             |
| regex_effbot            | 3.23 ms                                                | 3.40 ms: 1.05x slower                                                             |
| async_generators        | 425 ms                                                 | 451 ms: 1.06x slower                                                              |
| gc_traversal            | 3.84 ms                                                | 4.19 ms: 1.09x slower                                                             |
| python_startup_no_site  | 5.82 ms                                                | 6.71 ms: 1.15x slower                                                             |
| pickle_dict             | 27.3 us                                                | 32.4 us: 1.19x slower                                                             |
| dask                    | 423 ms                                                 | 540 ms: 1.28x slower                                                              |
| coverage                | 72.8 ms                                                | 103 ms: 1.42x slower                                                              |
| Geometric mean          | (ref)                                                  | 1.24x faster                                                                      |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, chameleon, django_template, djangocms, flaskblogging, gunicorn, pylint, richards_super, sympy_expand, sympy_integrate, sympy_str, sympy_sum, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.19x
