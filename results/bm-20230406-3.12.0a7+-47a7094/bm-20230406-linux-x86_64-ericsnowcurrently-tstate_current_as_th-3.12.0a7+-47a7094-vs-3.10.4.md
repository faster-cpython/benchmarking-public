
# Results vs. 3.10.4

- fork: ericsnowcurrently
- ref: tstate_current_as_th
- machine: linux-x86_64
- commit hash: 47a7094
- commit date: 2023-04-06
- overall geometric mean: 1.31x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230406-linux-x86_64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-47a7094 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 251 ms: 1.34x faster                                                              |
| chameleon      | 9.06 ms                                                | 6.42 ms: 1.41x faster                                                             |
| docutils       | 3.17 sec                                               | 2.53 sec: 1.25x faster                                                            |
| html5lib       | 85.9 ms                                                | 61.2 ms: 1.40x faster                                                             |
| tornado_http   | 127 ms                                                 | 90.3 ms: 1.41x faster                                                             |
| Geometric mean | (ref)                                                  | 1.36x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230406-linux-x86_64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-47a7094 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 83.6 ms: 1.69x faster                                                             |
| float          | 111 ms                                                 | 72.6 ms: 1.52x faster                                                             |
| pidigits       | 190 ms                                                 | 188 ms: 1.01x faster                                                              |
| Geometric mean | (ref)                                                  | 1.38x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230406-linux-x86_64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-47a7094 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 132 ms: 1.34x faster                                                              |
| regex_v8       | 25.0 ms                                                | 22.6 ms: 1.11x faster                                                             |
| regex_dna      | 222 ms                                                 | 214 ms: 1.04x faster                                                              |
| regex_effbot   | 3.23 ms                                                | 3.63 ms: 1.12x slower                                                             |
| Geometric mean | (ref)                                                  | 1.08x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230406-linux-x86_64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-47a7094 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 292 us: 1.56x faster                                                              |
| unpickle_pure_python | 300 us                                                 | 201 us: 1.50x faster                                                              |
| json_dumps           | 13.5 ms                                                | 9.46 ms: 1.43x faster                                                             |
| xml_etree_process    | 74.9 ms                                                | 55.0 ms: 1.36x faster                                                             |
| json_loads           | 28.8 us                                                | 24.5 us: 1.18x faster                                                             |
| xml_etree_generate   | 94.2 ms                                                | 80.7 ms: 1.17x faster                                                             |
| xml_etree_iterparse  | 111 ms                                                 | 99.4 ms: 1.12x faster                                                             |
| xml_etree_parse      | 163 ms                                                 | 147 ms: 1.11x faster                                                              |
| unpickle             | 14.1 us                                                | 13.6 us: 1.04x faster                                                             |
| pickle_list          | 4.56 us                                                | 4.43 us: 1.03x faster                                                             |
| unpickle_list        | 4.82 us                                                | 4.87 us: 1.01x slower                                                             |
| pickle               | 10.3 us                                                | 10.6 us: 1.03x slower                                                             |
| pickle_dict          | 27.3 us                                                | 32.3 us: 1.18x slower                                                             |
| Geometric mean       | (ref)                                                  | 1.16x faster                                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230406-linux-x86_64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-47a7094 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.87 ms: 1.59x faster                                                             |
| python_startup_no_site | 5.82 ms                                                | 6.55 ms: 1.13x slower                                                             |
| Geometric mean         | (ref)                                                  | 1.19x faster                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230406-linux-x86_64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-47a7094 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.99 ms: 1.48x faster                                                             |
| genshi_text     | 30.3 ms                                                | 21.1 ms: 1.44x faster                                                             |
| django_template | 45.9 ms                                                | 32.0 ms: 1.43x faster                                                             |
| genshi_xml      | 63.3 ms                                                | 47.3 ms: 1.34x faster                                                             |
| Geometric mean  | (ref)                                                  | 1.42x faster                                                                      |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230406-linux-x86_64-ericsnowcurrently-tstate_current_as_th-3.12.0a7+-47a7094 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| generators              | 76.8 ms                                                | 29.4 ms: 2.62x faster                                                             |
| deltablue               | 7.42 ms                                                | 3.20 ms: 2.32x faster                                                             |
| logging_silent          | 175 ns                                                 | 93.5 ns: 1.87x faster                                                             |
| asyncio_tcp             | 925 ms                                                 | 501 ms: 1.85x faster                                                              |
| scimark_sor             | 197 ms                                                 | 109 ms: 1.80x faster                                                              |
| richards                | 74.9 ms                                                | 43.1 ms: 1.74x faster                                                             |
| sqlglot_parse           | 2.06 ms                                                | 1.20 ms: 1.72x faster                                                             |
| nbody                   | 142 ms                                                 | 83.6 ms: 1.69x faster                                                             |
| go                      | 229 ms                                                 | 135 ms: 1.69x faster                                                              |
| raytrace                | 464 ms                                                 | 275 ms: 1.69x faster                                                              |
| sqlglot_transpile       | 2.45 ms                                                | 1.48 ms: 1.65x faster                                                             |
| scimark_monte_carlo     | 108 ms                                                 | 65.7 ms: 1.65x faster                                                             |
| chaos                   | 106 ms                                                 | 64.7 ms: 1.64x faster                                                             |
| pyflate                 | 673 ms                                                 | 416 ms: 1.62x faster                                                              |
| spectral_norm           | 150 ms                                                 | 93.2 ms: 1.61x faster                                                             |
| python_startup          | 14.2 ms                                                | 8.87 ms: 1.59x faster                                                             |
| crypto_pyaes            | 118 ms                                                 | 74.4 ms: 1.59x faster                                                             |
| hexiom                  | 9.53 ms                                                | 6.05 ms: 1.58x faster                                                             |
| pickle_pure_python      | 455 us                                                 | 292 us: 1.56x faster                                                              |
| deepcopy_memo           | 52.3 us                                                | 33.6 us: 1.56x faster                                                             |
| scimark_lu              | 163 ms                                                 | 106 ms: 1.54x faster                                                              |
| unpack_sequence         | 64.7 ns                                                | 42.1 ns: 1.54x faster                                                             |
| float                   | 111 ms                                                 | 72.6 ms: 1.52x faster                                                             |
| unpickle_pure_python    | 300 us                                                 | 201 us: 1.50x faster                                                              |
| mako                    | 14.8 ms                                                | 9.99 ms: 1.48x faster                                                             |
| genshi_text             | 30.3 ms                                                | 21.1 ms: 1.44x faster                                                             |
| django_template         | 45.9 ms                                                | 32.0 ms: 1.43x faster                                                             |
| pprint_pformat          | 1.99 sec                                               | 1.39 sec: 1.43x faster                                                            |
| json_dumps              | 13.5 ms                                                | 9.46 ms: 1.43x faster                                                             |
| pprint_safe_repr        | 955 ms                                                 | 671 ms: 1.42x faster                                                              |
| logging_simple          | 8.07 us                                                | 5.69 us: 1.42x faster                                                             |
| async_tree_memoization  | 854 ms                                                 | 605 ms: 1.41x faster                                                              |
| logging_format          | 8.91 us                                                | 6.31 us: 1.41x faster                                                             |
| tornado_http            | 127 ms                                                 | 90.3 ms: 1.41x faster                                                             |
| chameleon               | 9.06 ms                                                | 6.42 ms: 1.41x faster                                                             |
| html5lib                | 85.9 ms                                                | 61.2 ms: 1.40x faster                                                             |
| async_tree_none         | 717 ms                                                 | 512 ms: 1.40x faster                                                              |
| async_tree_io           | 1.77 sec                                               | 1.27 sec: 1.40x faster                                                            |
| coroutines              | 31.8 ms                                                | 22.9 ms: 1.39x faster                                                             |
| scimark_fft             | 424 ms                                                 | 306 ms: 1.39x faster                                                              |
| aiohttp                 | 1.38 ms                                                | 1.01 ms: 1.37x faster                                                             |
| deepcopy                | 442 us                                                 | 324 us: 1.36x faster                                                              |
| xml_etree_process       | 74.9 ms                                                | 55.0 ms: 1.36x faster                                                             |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.01 ms: 1.36x faster                                                             |
| regex_compile           | 177 ms                                                 | 132 ms: 1.34x faster                                                              |
| 2to3                    | 336 ms                                                 | 251 ms: 1.34x faster                                                              |
| genshi_xml              | 63.3 ms                                                | 47.3 ms: 1.34x faster                                                             |
| gunicorn                | 1.46 ms                                                | 1.09 ms: 1.34x faster                                                             |
| async_tree_cpu_io_mixed | 951 ms                                                 | 715 ms: 1.33x faster                                                              |
| sqlglot_normalize       | 135 ms                                                 | 102 ms: 1.33x faster                                                              |
| pycparser               | 1.50 sec                                               | 1.14 sec: 1.32x faster                                                            |
| thrift                  | 1.03 ms                                                | 787 us: 1.31x faster                                                              |
| deepcopy_reduce         | 3.82 us                                                | 2.94 us: 1.30x faster                                                             |
| sqlglot_optimize        | 65.3 ms                                                | 50.3 ms: 1.30x faster                                                             |
| fannkuch                | 486 ms                                                 | 377 ms: 1.29x faster                                                              |
| mypy2                   | 428 ms                                                 | 333 ms: 1.29x faster                                                              |
| nqueens                 | 100 ms                                                 | 79.4 ms: 1.26x faster                                                             |
| docutils                | 3.17 sec                                               | 2.53 sec: 1.25x faster                                                            |
| comprehensions          | 26.8 us                                                | 21.4 us: 1.25x faster                                                             |
| dulwich_log             | 75.9 ms                                                | 62.8 ms: 1.21x faster                                                             |
| sqlalchemy_imperative   | 21.2 ms                                                | 17.6 ms: 1.21x faster                                                             |
| bench_thread_pool       | 947 us                                                 | 788 us: 1.20x faster                                                              |
| sqlalchemy_declarative  | 165 ms                                                 | 139 ms: 1.19x faster                                                              |
| sympy_expand            | 545 ms                                                 | 457 ms: 1.19x faster                                                              |
| sympy_integrate         | 24.3 ms                                                | 20.4 ms: 1.19x faster                                                             |
| json_loads              | 28.8 us                                                | 24.5 us: 1.18x faster                                                             |
| xml_etree_generate      | 94.2 ms                                                | 80.7 ms: 1.17x faster                                                             |
| sympy_str               | 328 ms                                                 | 282 ms: 1.17x faster                                                              |
| json                    | 5.42 ms                                                | 4.73 ms: 1.14x faster                                                             |
| meteor_contest          | 115 ms                                                 | 101 ms: 1.13x faster                                                              |
| create_gc_cycles        | 1.67 ms                                                | 1.48 ms: 1.13x faster                                                             |
| xml_etree_iterparse     | 111 ms                                                 | 99.4 ms: 1.12x faster                                                             |
| sympy_sum               | 185 ms                                                 | 165 ms: 1.12x faster                                                              |
| djangocms               | 35.9 us                                                | 32.2 us: 1.11x faster                                                             |
| sqlite_synth            | 2.93 us                                                | 2.63 us: 1.11x faster                                                             |
| xml_etree_parse         | 163 ms                                                 | 147 ms: 1.11x faster                                                              |
| regex_v8                | 25.0 ms                                                | 22.6 ms: 1.11x faster                                                             |
| pathlib                 | 20.0 ms                                                | 18.3 ms: 1.10x faster                                                             |
| mdp                     | 2.82 sec                                               | 2.68 sec: 1.05x faster                                                            |
| unpickle                | 14.1 us                                                | 13.6 us: 1.04x faster                                                             |
| async_generators        | 425 ms                                                 | 409 ms: 1.04x faster                                                              |
| regex_dna               | 222 ms                                                 | 214 ms: 1.04x faster                                                              |
| pickle_list             | 4.56 us                                                | 4.43 us: 1.03x faster                                                             |
| telco                   | 6.54 ms                                                | 6.48 ms: 1.01x faster                                                             |
| pidigits                | 190 ms                                                 | 188 ms: 1.01x faster                                                              |
| unpickle_list           | 4.82 us                                                | 4.87 us: 1.01x slower                                                             |
| pickle                  | 10.3 us                                                | 10.6 us: 1.03x slower                                                             |
| gc_traversal            | 3.84 ms                                                | 4.19 ms: 1.09x slower                                                             |
| regex_effbot            | 3.23 ms                                                | 3.63 ms: 1.12x slower                                                             |
| python_startup_no_site  | 5.82 ms                                                | 6.55 ms: 1.13x slower                                                             |
| dask                    | 423 ms                                                 | 499 ms: 1.18x slower                                                              |
| pickle_dict             | 27.3 us                                                | 32.3 us: 1.18x slower                                                             |
| coverage                | 72.8 ms                                                | 96.6 ms: 1.33x slower                                                             |
| Geometric mean          | (ref)                                                  | 1.31x faster                                                                      |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (6) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.30x
- 95% likely to have a speedup of 1.29x
- 99% likely to have a speedup of 1.25x
