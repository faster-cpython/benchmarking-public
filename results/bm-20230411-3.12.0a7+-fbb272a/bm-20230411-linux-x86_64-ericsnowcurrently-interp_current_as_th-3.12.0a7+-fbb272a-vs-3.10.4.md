
# Results vs. 3.10.4

- fork: ericsnowcurrently
- ref: interp_current_as_th
- machine: linux-x86_64
- commit hash: fbb272a
- commit date: 2023-04-11
- overall geometric mean: 1.31x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230411-linux-x86_64-ericsnowcurrently-interp_current_as_th-3.12.0a7+-fbb272a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 336 ms                                                 | 250 ms: 1.35x faster                                                              |
| chameleon      | 9.06 ms                                                | 6.51 ms: 1.39x faster                                                             |
| docutils       | 3.17 sec                                               | 2.52 sec: 1.26x faster                                                            |
| html5lib       | 85.9 ms                                                | 61.3 ms: 1.40x faster                                                             |
| tornado_http   | 127 ms                                                 | 90.5 ms: 1.41x faster                                                             |
| Geometric mean | (ref)                                                  | 1.36x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230411-linux-x86_64-ericsnowcurrently-interp_current_as_th-3.12.0a7+-fbb272a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 82.7 ms: 1.71x faster                                                             |
| float          | 111 ms                                                 | 73.0 ms: 1.51x faster                                                             |
| pidigits       | 190 ms                                                 | 188 ms: 1.01x faster                                                              |
| Geometric mean | (ref)                                                  | 1.38x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230411-linux-x86_64-ericsnowcurrently-interp_current_as_th-3.12.0a7+-fbb272a |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 131 ms: 1.35x faster                                                              |
| regex_v8       | 25.0 ms                                                | 22.5 ms: 1.11x faster                                                             |
| regex_dna      | 222 ms                                                 | 214 ms: 1.04x faster                                                              |
| regex_effbot   | 3.23 ms                                                | 3.57 ms: 1.11x slower                                                             |
| Geometric mean | (ref)                                                  | 1.09x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230411-linux-x86_64-ericsnowcurrently-interp_current_as_th-3.12.0a7+-fbb272a |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 284 us: 1.60x faster                                                              |
| unpickle_pure_python | 300 us                                                 | 202 us: 1.49x faster                                                              |
| json_dumps           | 13.5 ms                                                | 9.40 ms: 1.44x faster                                                             |
| xml_etree_process    | 74.9 ms                                                | 55.3 ms: 1.36x faster                                                             |
| json_loads           | 28.8 us                                                | 24.4 us: 1.18x faster                                                             |
| xml_etree_generate   | 94.2 ms                                                | 80.2 ms: 1.17x faster                                                             |
| xml_etree_iterparse  | 111 ms                                                 | 98.7 ms: 1.13x faster                                                             |
| xml_etree_parse      | 163 ms                                                 | 150 ms: 1.09x faster                                                              |
| unpickle             | 14.1 us                                                | 13.1 us: 1.08x faster                                                             |
| pickle_list          | 4.56 us                                                | 4.34 us: 1.05x faster                                                             |
| unpickle_list        | 4.82 us                                                | 4.67 us: 1.03x faster                                                             |
| pickle               | 10.3 us                                                | 10.6 us: 1.03x slower                                                             |
| pickle_dict          | 27.3 us                                                | 32.1 us: 1.18x slower                                                             |
| Geometric mean       | (ref)                                                  | 1.17x faster                                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230411-linux-x86_64-ericsnowcurrently-interp_current_as_th-3.12.0a7+-fbb272a |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 8.80 ms: 1.61x faster                                                             |
| python_startup_no_site | 5.82 ms                                                | 6.50 ms: 1.12x slower                                                             |
| Geometric mean         | (ref)                                                  | 1.20x faster                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230411-linux-x86_64-ericsnowcurrently-interp_current_as_th-3.12.0a7+-fbb272a |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako            | 14.8 ms                                                | 9.95 ms: 1.48x faster                                                             |
| django_template | 45.9 ms                                                | 32.0 ms: 1.43x faster                                                             |
| genshi_text     | 30.3 ms                                                | 21.2 ms: 1.43x faster                                                             |
| genshi_xml      | 63.3 ms                                                | 47.1 ms: 1.34x faster                                                             |
| Geometric mean  | (ref)                                                  | 1.42x faster                                                                      |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230411-linux-x86_64-ericsnowcurrently-interp_current_as_th-3.12.0a7+-fbb272a |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| generators              | 76.8 ms                                                | 29.2 ms: 2.63x faster                                                             |
| deltablue               | 7.42 ms                                                | 3.19 ms: 2.32x faster                                                             |
| logging_silent          | 175 ns                                                 | 94.3 ns: 1.86x faster                                                             |
| asyncio_tcp             | 925 ms                                                 | 507 ms: 1.82x faster                                                              |
| scimark_sor             | 197 ms                                                 | 109 ms: 1.80x faster                                                              |
| richards                | 74.9 ms                                                | 43.2 ms: 1.73x faster                                                             |
| sqlglot_parse           | 2.06 ms                                                | 1.20 ms: 1.71x faster                                                             |
| nbody                   | 142 ms                                                 | 82.7 ms: 1.71x faster                                                             |
| raytrace                | 464 ms                                                 | 275 ms: 1.69x faster                                                              |
| chaos                   | 106 ms                                                 | 64.1 ms: 1.66x faster                                                             |
| sqlglot_transpile       | 2.45 ms                                                | 1.49 ms: 1.65x faster                                                             |
| go                      | 229 ms                                                 | 139 ms: 1.65x faster                                                              |
| scimark_monte_carlo     | 108 ms                                                 | 66.6 ms: 1.63x faster                                                             |
| python_startup          | 14.2 ms                                                | 8.80 ms: 1.61x faster                                                             |
| pyflate                 | 673 ms                                                 | 419 ms: 1.61x faster                                                              |
| crypto_pyaes            | 118 ms                                                 | 73.8 ms: 1.61x faster                                                             |
| pickle_pure_python      | 455 us                                                 | 284 us: 1.60x faster                                                              |
| spectral_norm           | 150 ms                                                 | 94.1 ms: 1.59x faster                                                             |
| hexiom                  | 9.53 ms                                                | 5.99 ms: 1.59x faster                                                             |
| deepcopy_memo           | 52.3 us                                                | 33.6 us: 1.56x faster                                                             |
| scimark_lu              | 163 ms                                                 | 106 ms: 1.54x faster                                                              |
| unpack_sequence         | 64.7 ns                                                | 42.3 ns: 1.53x faster                                                             |
| float                   | 111 ms                                                 | 73.0 ms: 1.51x faster                                                             |
| unpickle_pure_python    | 300 us                                                 | 202 us: 1.49x faster                                                              |
| mako                    | 14.8 ms                                                | 9.95 ms: 1.48x faster                                                             |
| logging_format          | 8.91 us                                                | 6.18 us: 1.44x faster                                                             |
| json_dumps              | 13.5 ms                                                | 9.40 ms: 1.44x faster                                                             |
| logging_simple          | 8.07 us                                                | 5.62 us: 1.44x faster                                                             |
| django_template         | 45.9 ms                                                | 32.0 ms: 1.43x faster                                                             |
| pprint_pformat          | 1.99 sec                                               | 1.38 sec: 1.43x faster                                                            |
| genshi_text             | 30.3 ms                                                | 21.2 ms: 1.43x faster                                                             |
| async_tree_memoization  | 854 ms                                                 | 605 ms: 1.41x faster                                                              |
| scimark_fft             | 424 ms                                                 | 300 ms: 1.41x faster                                                              |
| tornado_http            | 127 ms                                                 | 90.5 ms: 1.41x faster                                                             |
| pprint_safe_repr        | 955 ms                                                 | 682 ms: 1.40x faster                                                              |
| html5lib                | 85.9 ms                                                | 61.3 ms: 1.40x faster                                                             |
| chameleon               | 9.06 ms                                                | 6.51 ms: 1.39x faster                                                             |
| async_tree_none         | 717 ms                                                 | 516 ms: 1.39x faster                                                              |
| coroutines              | 31.8 ms                                                | 23.0 ms: 1.38x faster                                                             |
| deepcopy                | 442 us                                                 | 321 us: 1.38x faster                                                              |
| async_tree_io           | 1.77 sec                                               | 1.29 sec: 1.38x faster                                                            |
| aiohttp                 | 1.38 ms                                                | 1.00 ms: 1.38x faster                                                             |
| xml_etree_process       | 74.9 ms                                                | 55.3 ms: 1.36x faster                                                             |
| gunicorn                | 1.46 ms                                                | 1.08 ms: 1.35x faster                                                             |
| thrift                  | 1.03 ms                                                | 767 us: 1.35x faster                                                              |
| regex_compile           | 177 ms                                                 | 131 ms: 1.35x faster                                                              |
| 2to3                    | 336 ms                                                 | 250 ms: 1.35x faster                                                              |
| genshi_xml              | 63.3 ms                                                | 47.1 ms: 1.34x faster                                                             |
| sqlglot_normalize       | 135 ms                                                 | 101 ms: 1.33x faster                                                              |
| deepcopy_reduce         | 3.82 us                                                | 2.87 us: 1.33x faster                                                             |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.12 ms: 1.32x faster                                                             |
| pycparser               | 1.50 sec                                               | 1.14 sec: 1.32x faster                                                            |
| async_tree_cpu_io_mixed | 951 ms                                                 | 721 ms: 1.32x faster                                                              |
| sqlglot_optimize        | 65.3 ms                                                | 49.9 ms: 1.31x faster                                                             |
| mypy2                   | 428 ms                                                 | 333 ms: 1.29x faster                                                              |
| nqueens                 | 100 ms                                                 | 78.8 ms: 1.27x faster                                                             |
| comprehensions          | 26.8 us                                                | 21.2 us: 1.26x faster                                                             |
| docutils                | 3.17 sec                                               | 2.52 sec: 1.26x faster                                                            |
| fannkuch                | 486 ms                                                 | 392 ms: 1.24x faster                                                              |
| dulwich_log             | 75.9 ms                                                | 62.3 ms: 1.22x faster                                                             |
| sqlalchemy_declarative  | 165 ms                                                 | 136 ms: 1.22x faster                                                              |
| bench_thread_pool       | 947 us                                                 | 785 us: 1.21x faster                                                              |
| sqlalchemy_imperative   | 21.2 ms                                                | 17.7 ms: 1.20x faster                                                             |
| sympy_integrate         | 24.3 ms                                                | 20.3 ms: 1.20x faster                                                             |
| sympy_expand            | 545 ms                                                 | 457 ms: 1.19x faster                                                              |
| json_loads              | 28.8 us                                                | 24.4 us: 1.18x faster                                                             |
| xml_etree_generate      | 94.2 ms                                                | 80.2 ms: 1.17x faster                                                             |
| sympy_str               | 328 ms                                                 | 282 ms: 1.17x faster                                                              |
| json                    | 5.42 ms                                                | 4.72 ms: 1.15x faster                                                             |
| meteor_contest          | 115 ms                                                 | 101 ms: 1.13x faster                                                              |
| mdp                     | 2.82 sec                                               | 2.50 sec: 1.13x faster                                                            |
| sqlite_synth            | 2.93 us                                                | 2.60 us: 1.13x faster                                                             |
| xml_etree_iterparse     | 111 ms                                                 | 98.7 ms: 1.13x faster                                                             |
| sympy_sum               | 185 ms                                                 | 164 ms: 1.13x faster                                                              |
| create_gc_cycles        | 1.67 ms                                                | 1.49 ms: 1.12x faster                                                             |
| djangocms               | 35.9 us                                                | 32.1 us: 1.12x faster                                                             |
| pathlib                 | 20.0 ms                                                | 18.0 ms: 1.11x faster                                                             |
| regex_v8                | 25.0 ms                                                | 22.5 ms: 1.11x faster                                                             |
| xml_etree_parse         | 163 ms                                                 | 150 ms: 1.09x faster                                                              |
| unpickle                | 14.1 us                                                | 13.1 us: 1.08x faster                                                             |
| pickle_list             | 4.56 us                                                | 4.34 us: 1.05x faster                                                             |
| async_generators        | 425 ms                                                 | 405 ms: 1.05x faster                                                              |
| regex_dna               | 222 ms                                                 | 214 ms: 1.04x faster                                                              |
| unpickle_list           | 4.82 us                                                | 4.67 us: 1.03x faster                                                             |
| telco                   | 6.54 ms                                                | 6.41 ms: 1.02x faster                                                             |
| pidigits                | 190 ms                                                 | 188 ms: 1.01x faster                                                              |
| pickle                  | 10.3 us                                                | 10.6 us: 1.03x slower                                                             |
| regex_effbot            | 3.23 ms                                                | 3.57 ms: 1.11x slower                                                             |
| python_startup_no_site  | 5.82 ms                                                | 6.50 ms: 1.12x slower                                                             |
| gc_traversal            | 3.84 ms                                                | 4.30 ms: 1.12x slower                                                             |
| dask                    | 423 ms                                                 | 493 ms: 1.17x slower                                                              |
| pickle_dict             | 27.3 us                                                | 32.1 us: 1.18x slower                                                             |
| coverage                | 72.8 ms                                                | 97.8 ms: 1.34x slower                                                             |
| Geometric mean          | (ref)                                                  | 1.31x faster                                                                      |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (6) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.30x
- 95% likely to have a speedup of 1.29x
- 99% likely to have a speedup of 1.25x
