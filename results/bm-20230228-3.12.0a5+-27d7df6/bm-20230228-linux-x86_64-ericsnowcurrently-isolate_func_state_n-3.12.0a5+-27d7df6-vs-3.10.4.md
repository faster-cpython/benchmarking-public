
# Results vs. 3.10.4

- fork: ericsnowcurrently
- ref: isolate_func_state_n
- machine: linux-x86_64
- commit hash: 27d7df6
- commit date: 2023-02-28
- overall geometric mean: 1.29x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_func_state_n-3.12.0a5+-27d7df6 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 251 ms: 1.34x faster                                                              |
| chameleon      | 9.06 ms                                                | 6.34 ms: 1.43x faster                                                             |
| docutils       | 3.17 sec                                               | 2.55 sec: 1.24x faster                                                            |
| html5lib       | 85.9 ms                                                | 62.4 ms: 1.38x faster                                                             |
| tornado_http   | 127 ms                                                 | 95.2 ms: 1.34x faster                                                             |
| Geometric mean | (ref)                                                  | 1.34x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_func_state_n-3.12.0a5+-27d7df6 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 94.1 ms: 1.50x faster                                                             |
| float          | 111 ms                                                 | 74.1 ms: 1.49x faster                                                             |
| pidigits       | 190 ms                                                 | 189 ms: 1.00x faster                                                              |
| Geometric mean | (ref)                                                  | 1.31x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_func_state_n-3.12.0a5+-27d7df6 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 136 ms: 1.30x faster                                                              |
| regex_v8       | 25.0 ms                                                | 21.8 ms: 1.15x faster                                                             |
| regex_dna      | 222 ms                                                 | 199 ms: 1.11x faster                                                              |
| regex_effbot   | 3.23 ms                                                | 3.57 ms: 1.11x slower                                                             |
| Geometric mean | (ref)                                                  | 1.11x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_func_state_n-3.12.0a5+-27d7df6 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 293 us: 1.55x faster                                                              |
| unpickle_pure_python | 300 us                                                 | 202 us: 1.48x faster                                                              |
| json_dumps           | 13.5 ms                                                | 9.58 ms: 1.41x faster                                                             |
| xml_etree_process    | 74.9 ms                                                | 56.4 ms: 1.33x faster                                                             |
| json_loads           | 28.8 us                                                | 24.0 us: 1.20x faster                                                             |
| xml_etree_generate   | 94.2 ms                                                | 81.7 ms: 1.15x faster                                                             |
| pickle_list          | 4.56 us                                                | 4.07 us: 1.12x faster                                                             |
| xml_etree_parse      | 163 ms                                                 | 150 ms: 1.09x faster                                                              |
| xml_etree_iterparse  | 111 ms                                                 | 104 ms: 1.07x faster                                                              |
| unpickle             | 14.1 us                                                | 13.7 us: 1.03x faster                                                             |
| pickle               | 10.3 us                                                | 10.2 us: 1.01x faster                                                             |
| unpickle_list        | 4.82 us                                                | 4.99 us: 1.04x slower                                                             |
| pickle_dict          | 27.3 us                                                | 30.6 us: 1.12x slower                                                             |
| Geometric mean       | (ref)                                                  | 1.16x faster                                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_func_state_n-3.12.0a5+-27d7df6 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.04 ms: 1.57x faster                                                             |
| python_startup_no_site | 5.82 ms                                                | 6.56 ms: 1.13x slower                                                             |
| Geometric mean         | (ref)                                                  | 1.18x faster                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_func_state_n-3.12.0a5+-27d7df6 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.88 ms: 1.49x faster                                                             |
| genshi_text     | 30.3 ms                                                | 21.8 ms: 1.39x faster                                                             |
| django_template | 45.9 ms                                                | 33.6 ms: 1.37x faster                                                             |
| genshi_xml      | 63.3 ms                                                | 49.0 ms: 1.29x faster                                                             |
| Geometric mean  | (ref)                                                  | 1.38x faster                                                                      |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_func_state_n-3.12.0a5+-27d7df6 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| generators              | 76.8 ms                                                | 30.8 ms: 2.50x faster                                                             |
| deltablue               | 7.42 ms                                                | 3.23 ms: 2.29x faster                                                             |
| logging_silent          | 175 ns                                                 | 94.0 ns: 1.86x faster                                                             |
| asyncio_tcp             | 925 ms                                                 | 500 ms: 1.85x faster                                                              |
| scimark_sor             | 197 ms                                                 | 107 ms: 1.83x faster                                                              |
| richards                | 74.9 ms                                                | 43.9 ms: 1.71x faster                                                             |
| pyflate                 | 673 ms                                                 | 405 ms: 1.66x faster                                                              |
| go                      | 229 ms                                                 | 138 ms: 1.66x faster                                                              |
| scimark_monte_carlo     | 108 ms                                                 | 66.6 ms: 1.63x faster                                                             |
| spectral_norm           | 150 ms                                                 | 93.0 ms: 1.61x faster                                                             |
| crypto_pyaes            | 118 ms                                                 | 74.2 ms: 1.60x faster                                                             |
| raytrace                | 464 ms                                                 | 291 ms: 1.59x faster                                                              |
| unpack_sequence         | 64.7 ns                                                | 41.2 ns: 1.57x faster                                                             |
| chaos                   | 106 ms                                                 | 67.7 ms: 1.57x faster                                                             |
| python_startup          | 14.2 ms                                                | 9.04 ms: 1.57x faster                                                             |
| pickle_pure_python      | 455 us                                                 | 293 us: 1.55x faster                                                              |
| hexiom                  | 9.53 ms                                                | 6.14 ms: 1.55x faster                                                             |
| nbody                   | 142 ms                                                 | 94.1 ms: 1.50x faster                                                             |
| mako                    | 14.8 ms                                                | 9.88 ms: 1.49x faster                                                             |
| float                   | 111 ms                                                 | 74.1 ms: 1.49x faster                                                             |
| unpickle_pure_python    | 300 us                                                 | 202 us: 1.48x faster                                                              |
| deepcopy_memo           | 52.3 us                                                | 35.4 us: 1.48x faster                                                             |
| scimark_lu              | 163 ms                                                 | 111 ms: 1.46x faster                                                              |
| chameleon               | 9.06 ms                                                | 6.34 ms: 1.43x faster                                                             |
| sqlglot_parse           | 2.06 ms                                                | 1.44 ms: 1.42x faster                                                             |
| json_dumps              | 13.5 ms                                                | 9.58 ms: 1.41x faster                                                             |
| sqlglot_transpile       | 2.45 ms                                                | 1.74 ms: 1.41x faster                                                             |
| genshi_text             | 30.3 ms                                                | 21.8 ms: 1.39x faster                                                             |
| pprint_pformat          | 1.99 sec                                               | 1.43 sec: 1.39x faster                                                            |
| logging_format          | 8.91 us                                                | 6.45 us: 1.38x faster                                                             |
| async_tree_io           | 1.77 sec                                               | 1.29 sec: 1.38x faster                                                            |
| pprint_safe_repr        | 955 ms                                                 | 694 ms: 1.38x faster                                                              |
| async_tree_none         | 717 ms                                                 | 521 ms: 1.38x faster                                                              |
| html5lib                | 85.9 ms                                                | 62.4 ms: 1.38x faster                                                             |
| aiohttp                 | 1.38 ms                                                | 1.01 ms: 1.37x faster                                                             |
| django_template         | 45.9 ms                                                | 33.6 ms: 1.37x faster                                                             |
| coroutines              | 31.8 ms                                                | 23.3 ms: 1.36x faster                                                             |
| pycparser               | 1.50 sec                                               | 1.10 sec: 1.36x faster                                                            |
| logging_simple          | 8.07 us                                                | 5.93 us: 1.36x faster                                                             |
| scimark_fft             | 424 ms                                                 | 311 ms: 1.36x faster                                                              |
| gunicorn                | 1.46 ms                                                | 1.08 ms: 1.35x faster                                                             |
| thrift                  | 1.03 ms                                                | 772 us: 1.34x faster                                                              |
| tornado_http            | 127 ms                                                 | 95.2 ms: 1.34x faster                                                             |
| 2to3                    | 336 ms                                                 | 251 ms: 1.34x faster                                                              |
| xml_etree_process       | 74.9 ms                                                | 56.4 ms: 1.33x faster                                                             |
| fannkuch                | 486 ms                                                 | 367 ms: 1.32x faster                                                              |
| async_tree_memoization  | 854 ms                                                 | 653 ms: 1.31x faster                                                              |
| regex_compile           | 177 ms                                                 | 136 ms: 1.30x faster                                                              |
| deepcopy                | 442 us                                                 | 340 us: 1.30x faster                                                              |
| sqlglot_normalize       | 135 ms                                                 | 104 ms: 1.30x faster                                                              |
| genshi_xml              | 63.3 ms                                                | 49.0 ms: 1.29x faster                                                             |
| async_tree_cpu_io_mixed | 951 ms                                                 | 741 ms: 1.28x faster                                                              |
| mypy2                   | 428 ms                                                 | 335 ms: 1.28x faster                                                              |
| sqlglot_optimize        | 65.3 ms                                                | 51.3 ms: 1.27x faster                                                             |
| deepcopy_reduce         | 3.82 us                                                | 3.03 us: 1.26x faster                                                             |
| docutils                | 3.17 sec                                               | 2.55 sec: 1.24x faster                                                            |
| nqueens                 | 100 ms                                                 | 80.8 ms: 1.24x faster                                                             |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.44 ms: 1.23x faster                                                             |
| json_loads              | 28.8 us                                                | 24.0 us: 1.20x faster                                                             |
| dulwich_log             | 75.9 ms                                                | 63.4 ms: 1.20x faster                                                             |
| bench_thread_pool       | 947 us                                                 | 797 us: 1.19x faster                                                              |
| sympy_integrate         | 24.3 ms                                                | 20.6 ms: 1.18x faster                                                             |
| sqlalchemy_declarative  | 165 ms                                                 | 141 ms: 1.18x faster                                                              |
| sympy_expand            | 545 ms                                                 | 466 ms: 1.17x faster                                                              |
| sqlalchemy_imperative   | 21.2 ms                                                | 18.2 ms: 1.16x faster                                                             |
| json                    | 5.42 ms                                                | 4.66 ms: 1.16x faster                                                             |
| xml_etree_generate      | 94.2 ms                                                | 81.7 ms: 1.15x faster                                                             |
| mdp                     | 2.82 sec                                               | 2.46 sec: 1.15x faster                                                            |
| regex_v8                | 25.0 ms                                                | 21.8 ms: 1.15x faster                                                             |
| sympy_str               | 328 ms                                                 | 287 ms: 1.15x faster                                                              |
| pathlib                 | 20.0 ms                                                | 17.7 ms: 1.13x faster                                                             |
| djangocms               | 35.9 us                                                | 31.8 us: 1.13x faster                                                             |
| comprehensions          | 26.8 us                                                | 23.9 us: 1.12x faster                                                             |
| sqlite_synth            | 2.93 us                                                | 2.62 us: 1.12x faster                                                             |
| pickle_list             | 4.56 us                                                | 4.07 us: 1.12x faster                                                             |
| meteor_contest          | 115 ms                                                 | 103 ms: 1.11x faster                                                              |
| regex_dna               | 222 ms                                                 | 199 ms: 1.11x faster                                                              |
| create_gc_cycles        | 1.67 ms                                                | 1.51 ms: 1.11x faster                                                             |
| sympy_sum               | 185 ms                                                 | 168 ms: 1.10x faster                                                              |
| xml_etree_parse         | 163 ms                                                 | 150 ms: 1.09x faster                                                              |
| xml_etree_iterparse     | 111 ms                                                 | 104 ms: 1.07x faster                                                              |
| unpickle                | 14.1 us                                                | 13.7 us: 1.03x faster                                                             |
| telco                   | 6.54 ms                                                | 6.45 ms: 1.01x faster                                                             |
| pickle                  | 10.3 us                                                | 10.2 us: 1.01x faster                                                             |
| async_generators        | 425 ms                                                 | 421 ms: 1.01x faster                                                              |
| pidigits                | 190 ms                                                 | 189 ms: 1.00x faster                                                              |
| unpickle_list           | 4.82 us                                                | 4.99 us: 1.04x slower                                                             |
| regex_effbot            | 3.23 ms                                                | 3.57 ms: 1.11x slower                                                             |
| pickle_dict             | 27.3 us                                                | 30.6 us: 1.12x slower                                                             |
| python_startup_no_site  | 5.82 ms                                                | 6.56 ms: 1.13x slower                                                             |
| dask                    | 423 ms                                                 | 508 ms: 1.20x slower                                                              |
| coverage                | 72.8 ms                                                | 98.3 ms: 1.35x slower                                                             |
| Geometric mean          | (ref)                                                  | 1.29x faster                                                                      |

Benchmark hidden because not significant (2): gc_traversal, bench_mp_pool
Ignored benchmarks (6) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.24x
