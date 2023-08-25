
# Results vs. 3.10.4

- fork: ericsnowcurrently
- ref: per_interpreter_gil_
- machine: linux-x86_64
- commit hash: f3fd844
- commit date: 2023-05-04
- overall geometric mean: 1.23x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230504-linux-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 272 ms: 1.24x faster                                                              |
| docutils       | 3.17 sec                                               | 2.74 sec: 1.16x faster                                                            |
| tornado_http   | 127 ms                                                 | 100 ms: 1.27x faster                                                              |
| Geometric mean | (ref)                                                  | 1.22x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230504-linux-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 90.1 ms: 1.57x faster                                                             |
| float          | 111 ms                                                 | 82.4 ms: 1.34x faster                                                             |
| pidigits       | 190 ms                                                 | 197 ms: 1.04x slower                                                              |
| Geometric mean | (ref)                                                  | 1.27x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230504-linux-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 146 ms: 1.21x faster                                                              |
| regex_v8       | 25.0 ms                                                | 22.2 ms: 1.13x faster                                                             |
| regex_dna      | 222 ms                                                 | 204 ms: 1.09x faster                                                              |
| regex_effbot   | 3.23 ms                                                | 3.66 ms: 1.13x slower                                                             |
| Geometric mean | (ref)                                                  | 1.07x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230504-linux-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 320 us: 1.43x faster                                                              |
| unpickle_pure_python | 300 us                                                 | 222 us: 1.36x faster                                                              |
| json_dumps           | 13.5 ms                                                | 10.1 ms: 1.33x faster                                                             |
| xml_etree_process    | 74.9 ms                                                | 59.9 ms: 1.25x faster                                                             |
| json_loads           | 28.8 us                                                | 25.1 us: 1.15x faster                                                             |
| xml_etree_generate   | 94.2 ms                                                | 85.1 ms: 1.11x faster                                                             |
| xml_etree_iterparse  | 111 ms                                                 | 104 ms: 1.07x faster                                                              |
| xml_etree_parse      | 163 ms                                                 | 154 ms: 1.06x faster                                                              |
| unpickle             | 14.1 us                                                | 14.6 us: 1.03x slower                                                             |
| pickle               | 10.3 us                                                | 10.7 us: 1.04x slower                                                             |
| pickle_dict          | 27.3 us                                                | 30.4 us: 1.12x slower                                                             |
| Geometric mean       | (ref)                                                  | 1.11x faster                                                                      |

Benchmark hidden because not significant (2): unpickle_list, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230504-linux-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.14 ms: 1.55x faster                                                             |
| python_startup_no_site | 5.82 ms                                                | 6.69 ms: 1.15x slower                                                             |
| Geometric mean         | (ref)                                                  | 1.16x faster                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230504-linux-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|-----------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako      | 14.8 ms                                                | 10.6 ms: 1.39x faster                                                             |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230504-linux-x86_64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| generators              | 76.8 ms                                                | 31.4 ms: 2.44x faster                                                             |
| deltablue               | 7.42 ms                                                | 3.54 ms: 2.10x faster                                                             |
| asyncio_tcp             | 925 ms                                                 | 510 ms: 1.82x faster                                                              |
| logging_silent          | 175 ns                                                 | 103 ns: 1.70x faster                                                              |
| richards                | 74.9 ms                                                | 44.1 ms: 1.70x faster                                                             |
| go                      | 229 ms                                                 | 141 ms: 1.63x faster                                                              |
| scimark_sor             | 197 ms                                                 | 124 ms: 1.58x faster                                                              |
| nbody                   | 142 ms                                                 | 90.1 ms: 1.57x faster                                                             |
| python_startup          | 14.2 ms                                                | 9.14 ms: 1.55x faster                                                             |
| sqlglot_parse           | 2.06 ms                                                | 1.34 ms: 1.54x faster                                                             |
| chaos                   | 106 ms                                                 | 70.3 ms: 1.51x faster                                                             |
| raytrace                | 464 ms                                                 | 307 ms: 1.51x faster                                                              |
| pyflate                 | 673 ms                                                 | 446 ms: 1.51x faster                                                              |
| crypto_pyaes            | 118 ms                                                 | 78.7 ms: 1.50x faster                                                             |
| scimark_monte_carlo     | 108 ms                                                 | 73.0 ms: 1.48x faster                                                             |
| hexiom                  | 9.53 ms                                                | 6.43 ms: 1.48x faster                                                             |
| sqlglot_transpile       | 2.45 ms                                                | 1.67 ms: 1.46x faster                                                             |
| async_tree_io           | 1.77 sec                                               | 1.23 sec: 1.45x faster                                                            |
| async_tree_none         | 717 ms                                                 | 502 ms: 1.43x faster                                                              |
| pickle_pure_python      | 455 us                                                 | 320 us: 1.43x faster                                                              |
| scimark_lu              | 163 ms                                                 | 115 ms: 1.42x faster                                                              |
| spectral_norm           | 150 ms                                                 | 108 ms: 1.39x faster                                                              |
| async_tree_memoization  | 854 ms                                                 | 616 ms: 1.39x faster                                                              |
| mako                    | 14.8 ms                                                | 10.6 ms: 1.39x faster                                                             |
| coroutines              | 31.8 ms                                                | 23.1 ms: 1.38x faster                                                             |
| unpickle_pure_python    | 300 us                                                 | 222 us: 1.36x faster                                                              |
| float                   | 111 ms                                                 | 82.4 ms: 1.34x faster                                                             |
| json_dumps              | 13.5 ms                                                | 10.1 ms: 1.33x faster                                                             |
| deepcopy_memo           | 52.3 us                                                | 39.3 us: 1.33x faster                                                             |
| unpack_sequence         | 64.7 ns                                                | 49.1 ns: 1.32x faster                                                             |
| async_tree_cpu_io_mixed | 951 ms                                                 | 726 ms: 1.31x faster                                                              |
| pprint_pformat          | 1.99 sec                                               | 1.52 sec: 1.31x faster                                                            |
| pycparser               | 1.50 sec                                               | 1.16 sec: 1.29x faster                                                            |
| pprint_safe_repr        | 955 ms                                                 | 749 ms: 1.27x faster                                                              |
| tornado_http            | 127 ms                                                 | 100 ms: 1.27x faster                                                              |
| fannkuch                | 486 ms                                                 | 383 ms: 1.27x faster                                                              |
| logging_format          | 8.91 us                                                | 7.08 us: 1.26x faster                                                             |
| logging_simple          | 8.07 us                                                | 6.43 us: 1.26x faster                                                             |
| xml_etree_process       | 74.9 ms                                                | 59.9 ms: 1.25x faster                                                             |
| 2to3                    | 336 ms                                                 | 272 ms: 1.24x faster                                                              |
| mypy2                   | 428 ms                                                 | 353 ms: 1.21x faster                                                              |
| regex_compile           | 177 ms                                                 | 146 ms: 1.21x faster                                                              |
| scimark_fft             | 424 ms                                                 | 355 ms: 1.19x faster                                                              |
| sqlglot_normalize       | 135 ms                                                 | 114 ms: 1.19x faster                                                              |
| deepcopy                | 442 us                                                 | 374 us: 1.18x faster                                                              |
| nqueens                 | 100 ms                                                 | 84.9 ms: 1.18x faster                                                             |
| sqlglot_optimize        | 65.3 ms                                                | 55.5 ms: 1.18x faster                                                             |
| deepcopy_reduce         | 3.82 us                                                | 3.26 us: 1.17x faster                                                             |
| comprehensions          | 26.8 us                                                | 23.2 us: 1.16x faster                                                             |
| docutils                | 3.17 sec                                               | 2.74 sec: 1.16x faster                                                            |
| json_loads              | 28.8 us                                                | 25.1 us: 1.15x faster                                                             |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.75 ms: 1.15x faster                                                             |
| create_gc_cycles        | 1.67 ms                                                | 1.46 ms: 1.14x faster                                                             |
| regex_v8                | 25.0 ms                                                | 22.2 ms: 1.13x faster                                                             |
| bench_thread_pool       | 947 us                                                 | 842 us: 1.12x faster                                                              |
| json                    | 5.42 ms                                                | 4.82 ms: 1.12x faster                                                             |
| sqlalchemy_declarative  | 165 ms                                                 | 147 ms: 1.12x faster                                                              |
| sqlalchemy_imperative   | 21.2 ms                                                | 19.0 ms: 1.11x faster                                                             |
| dulwich_log             | 75.9 ms                                                | 68.5 ms: 1.11x faster                                                             |
| xml_etree_generate      | 94.2 ms                                                | 85.1 ms: 1.11x faster                                                             |
| sqlite_synth            | 2.93 us                                                | 2.69 us: 1.09x faster                                                             |
| regex_dna               | 222 ms                                                 | 204 ms: 1.09x faster                                                              |
| mdp                     | 2.82 sec                                               | 2.61 sec: 1.08x faster                                                            |
| pathlib                 | 20.0 ms                                                | 18.6 ms: 1.08x faster                                                             |
| xml_etree_iterparse     | 111 ms                                                 | 104 ms: 1.07x faster                                                              |
| xml_etree_parse         | 163 ms                                                 | 154 ms: 1.06x faster                                                              |
| bench_mp_pool           | 24.0 ms                                                | 24.0 ms: 1.00x slower                                                             |
| unpickle                | 14.1 us                                                | 14.6 us: 1.03x slower                                                             |
| meteor_contest          | 115 ms                                                 | 118 ms: 1.03x slower                                                              |
| pidigits                | 190 ms                                                 | 197 ms: 1.04x slower                                                              |
| pickle                  | 10.3 us                                                | 10.7 us: 1.04x slower                                                             |
| telco                   | 6.54 ms                                                | 6.84 ms: 1.05x slower                                                             |
| gc_traversal            | 3.84 ms                                                | 4.04 ms: 1.05x slower                                                             |
| async_generators        | 425 ms                                                 | 450 ms: 1.06x slower                                                              |
| pickle_dict             | 27.3 us                                                | 30.4 us: 1.12x slower                                                             |
| regex_effbot            | 3.23 ms                                                | 3.66 ms: 1.13x slower                                                             |
| python_startup_no_site  | 5.82 ms                                                | 6.69 ms: 1.15x slower                                                             |
| dask                    | 423 ms                                                 | 543 ms: 1.29x slower                                                              |
| coverage                | 72.8 ms                                                | 102 ms: 1.41x slower                                                              |
| Geometric mean          | (ref)                                                  | 1.23x faster                                                                      |

Benchmark hidden because not significant (2): unpickle_list, pickle_list
Ignored benchmarks (19) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, richards_super, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.20x
- 95% likely to have a speedup of 1.18x
- 99% likely to have a speedup of 1.17x
