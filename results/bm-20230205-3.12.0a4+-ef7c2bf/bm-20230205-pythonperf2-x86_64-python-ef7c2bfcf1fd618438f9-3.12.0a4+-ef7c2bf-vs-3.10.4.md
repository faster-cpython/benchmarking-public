
# Results vs. 3.10.4

- fork: python
- ref: ef7c2bfcf1fd618438f9
- machine: linux-x86_64
- commit hash: ef7c2bf
- commit date: 2023-02-05
- overall geometric mean: 1.27x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230205-pythonperf2-x86_64-python-ef7c2bfcf1fd618438f9-3.12.0a4+-ef7c2bf |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 281 ms: 1.24x faster                                                         |
| chameleon      | 9.72 ms                                                      | 7.63 ms: 1.27x faster                                                        |
| docutils       | 3.40 sec                                                     | 2.75 sec: 1.24x faster                                                       |
| html5lib       | 94.6 ms                                                      | 66.2 ms: 1.43x faster                                                        |
| tornado_http   | 152 ms                                                       | 120 ms: 1.27x faster                                                         |
| Geometric mean | (ref)                                                        | 1.29x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230205-pythonperf2-x86_64-python-ef7c2bfcf1fd618438f9-3.12.0a4+-ef7c2bf |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 110 ms                                                       | 71.5 ms: 1.54x faster                                                        |
| nbody          | 137 ms                                                       | 89.9 ms: 1.53x faster                                                        |
| pidigits       | 271 ms                                                       | 251 ms: 1.08x faster                                                         |
| Geometric mean | (ref)                                                        | 1.36x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230205-pythonperf2-x86_64-python-ef7c2bfcf1fd618438f9-3.12.0a4+-ef7c2bf |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 194 ms                                                       | 145 ms: 1.33x faster                                                         |
| regex_v8       | 26.6 ms                                                      | 22.1 ms: 1.20x faster                                                        |
| regex_dna      | 259 ms                                                       | 222 ms: 1.17x faster                                                         |
| regex_effbot   | 2.99 ms                                                      | 3.31 ms: 1.11x slower                                                        |
| Geometric mean | (ref)                                                        | 1.14x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230205-pythonperf2-x86_64-python-ef7c2bfcf1fd618438f9-3.12.0a4+-ef7c2bf |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_pure_python | 321 us                                                       | 208 us: 1.54x faster                                                         |
| pickle_pure_python   | 457 us                                                       | 307 us: 1.49x faster                                                         |
| json_dumps           | 14.2 ms                                                      | 10.0 ms: 1.42x faster                                                        |
| xml_etree_process    | 76.0 ms                                                      | 55.7 ms: 1.36x faster                                                        |
| json_loads           | 30.0 us                                                      | 24.1 us: 1.25x faster                                                        |
| xml_etree_generate   | 94.6 ms                                                      | 81.1 ms: 1.17x faster                                                        |
| xml_etree_parse      | 162 ms                                                       | 143 ms: 1.13x faster                                                         |
| unpickle             | 14.2 us                                                      | 13.5 us: 1.05x faster                                                        |
| xml_etree_iterparse  | 110 ms                                                       | 106 ms: 1.04x faster                                                         |
| pickle_list          | 4.11 us                                                      | 3.95 us: 1.04x faster                                                        |
| unpickle_list        | 4.49 us                                                      | 4.36 us: 1.03x faster                                                        |
| pickle               | 9.94 us                                                      | 10.1 us: 1.02x slower                                                        |
| pickle_dict          | 30.0 us                                                      | 32.6 us: 1.09x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.17x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230205-pythonperf2-x86_64-python-ef7c2bfcf1fd618438f9-3.12.0a4+-ef7c2bf |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 11.2 ms: 1.03x faster                                                        |
| python_startup_no_site | 7.32 ms                                                      | 8.26 ms: 1.13x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.05x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230205-pythonperf2-x86_64-python-ef7c2bfcf1fd618438f9-3.12.0a4+-ef7c2bf |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.2 ms: 1.44x faster                                                        |
| django_template | 51.5 ms                                                      | 38.3 ms: 1.35x faster                                                        |
| genshi_text     | 31.5 ms                                                      | 24.9 ms: 1.26x faster                                                        |
| genshi_xml      | 64.7 ms                                                      | 54.1 ms: 1.20x faster                                                        |
| Geometric mean  | (ref)                                                        | 1.31x faster                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230205-pythonperf2-x86_64-python-ef7c2bfcf1fd618438f9-3.12.0a4+-ef7c2bf |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| deltablue               | 7.47 ms                                                      | 3.49 ms: 2.14x faster                                                        |
| asyncio_tcp             | 782 ms                                                       | 387 ms: 2.02x faster                                                         |
| logging_silent          | 166 ns                                                       | 95.9 ns: 1.73x faster                                                        |
| raytrace                | 488 ms                                                       | 291 ms: 1.68x faster                                                         |
| go                      | 259 ms                                                       | 155 ms: 1.67x faster                                                         |
| scimark_sor             | 177 ms                                                       | 107 ms: 1.65x faster                                                         |
| scimark_monte_carlo     | 109 ms                                                       | 66.9 ms: 1.64x faster                                                        |
| pyflate                 | 697 ms                                                       | 431 ms: 1.62x faster                                                         |
| scimark_lu              | 164 ms                                                       | 102 ms: 1.60x faster                                                         |
| richards                | 74.1 ms                                                      | 46.5 ms: 1.59x faster                                                        |
| chaos                   | 107 ms                                                       | 67.4 ms: 1.59x faster                                                        |
| unpickle_pure_python    | 321 us                                                       | 208 us: 1.54x faster                                                         |
| float                   | 110 ms                                                       | 71.5 ms: 1.54x faster                                                        |
| nbody                   | 137 ms                                                       | 89.9 ms: 1.53x faster                                                        |
| bench_mp_pool           | 7.18 ms                                                      | 4.80 ms: 1.50x faster                                                        |
| pickle_pure_python      | 457 us                                                       | 307 us: 1.49x faster                                                         |
| hexiom                  | 9.52 ms                                                      | 6.43 ms: 1.48x faster                                                        |
| crypto_pyaes            | 118 ms                                                       | 80.0 ms: 1.48x faster                                                        |
| scimark_sparse_mat_mult | 5.19 ms                                                      | 3.59 ms: 1.45x faster                                                        |
| mako                    | 14.7 ms                                                      | 10.2 ms: 1.44x faster                                                        |
| spectral_norm           | 136 ms                                                       | 95.3 ms: 1.43x faster                                                        |
| sqlglot_parse           | 2.26 ms                                                      | 1.58 ms: 1.43x faster                                                        |
| html5lib                | 94.6 ms                                                      | 66.2 ms: 1.43x faster                                                        |
| json_dumps              | 14.2 ms                                                      | 10.0 ms: 1.42x faster                                                        |
| sqlglot_transpile       | 2.71 ms                                                      | 1.95 ms: 1.39x faster                                                        |
| unpack_sequence         | 59.5 ns                                                      | 43.2 ns: 1.38x faster                                                        |
| async_tree_none         | 700 ms                                                       | 508 ms: 1.38x faster                                                         |
| async_tree_io           | 1.61 sec                                                     | 1.17 sec: 1.37x faster                                                       |
| pycparser               | 1.66 sec                                                     | 1.21 sec: 1.37x faster                                                       |
| pprint_safe_repr        | 1.05 sec                                                     | 767 ms: 1.37x faster                                                         |
| pprint_pformat          | 2.15 sec                                                     | 1.58 sec: 1.37x faster                                                       |
| xml_etree_process       | 76.0 ms                                                      | 55.7 ms: 1.36x faster                                                        |
| async_tree_memoization  | 824 ms                                                       | 608 ms: 1.36x faster                                                         |
| django_template         | 51.5 ms                                                      | 38.3 ms: 1.35x faster                                                        |
| regex_compile           | 194 ms                                                       | 145 ms: 1.33x faster                                                         |
| deepcopy_memo           | 48.9 us                                                      | 36.8 us: 1.33x faster                                                        |
| scimark_fft             | 359 ms                                                       | 271 ms: 1.32x faster                                                         |
| async_generators        | 422 ms                                                       | 322 ms: 1.31x faster                                                         |
| thrift                  | 1.16 ms                                                      | 892 us: 1.31x faster                                                         |
| async_tree_cpu_io_mixed | 952 ms                                                       | 739 ms: 1.29x faster                                                         |
| logging_simple          | 8.90 us                                                      | 6.93 us: 1.28x faster                                                        |
| chameleon               | 9.72 ms                                                      | 7.63 ms: 1.27x faster                                                        |
| tornado_http            | 152 ms                                                       | 120 ms: 1.27x faster                                                         |
| genshi_text             | 31.5 ms                                                      | 24.9 ms: 1.26x faster                                                        |
| logging_format          | 9.57 us                                                      | 7.64 us: 1.25x faster                                                        |
| comprehensions          | 26.9 us                                                      | 21.5 us: 1.25x faster                                                        |
| mypy2                   | 466 ms                                                       | 374 ms: 1.25x faster                                                         |
| json_loads              | 30.0 us                                                      | 24.1 us: 1.25x faster                                                        |
| 2to3                    | 350 ms                                                       | 281 ms: 1.24x faster                                                         |
| docutils                | 3.40 sec                                                     | 2.75 sec: 1.24x faster                                                       |
| deepcopy_reduce         | 4.03 us                                                      | 3.28 us: 1.23x faster                                                        |
| fannkuch                | 496 ms                                                       | 404 ms: 1.23x faster                                                         |
| dulwich_log             | 80.1 ms                                                      | 65.6 ms: 1.22x faster                                                        |
| sqlglot_optimize        | 70.3 ms                                                      | 57.8 ms: 1.22x faster                                                        |
| sqlglot_normalize       | 144 ms                                                       | 119 ms: 1.21x faster                                                         |
| regex_v8                | 26.6 ms                                                      | 22.1 ms: 1.20x faster                                                        |
| genshi_xml              | 64.7 ms                                                      | 54.1 ms: 1.20x faster                                                        |
| deepcopy                | 454 us                                                       | 380 us: 1.20x faster                                                         |
| bench_thread_pool       | 1.14 ms                                                      | 959 us: 1.19x faster                                                         |
| json                    | 5.96 ms                                                      | 5.07 ms: 1.18x faster                                                        |
| regex_dna               | 259 ms                                                       | 222 ms: 1.17x faster                                                         |
| xml_etree_generate      | 94.6 ms                                                      | 81.1 ms: 1.17x faster                                                        |
| sqlite_synth            | 2.97 us                                                      | 2.56 us: 1.16x faster                                                        |
| sympy_integrate         | 28.1 ms                                                      | 24.3 ms: 1.16x faster                                                        |
| sympy_str               | 358 ms                                                       | 311 ms: 1.15x faster                                                         |
| pathlib                 | 21.7 ms                                                      | 18.9 ms: 1.15x faster                                                        |
| create_gc_cycles        | 1.82 ms                                                      | 1.60 ms: 1.14x faster                                                        |
| sympy_expand            | 599 ms                                                       | 528 ms: 1.13x faster                                                         |
| xml_etree_parse         | 162 ms                                                       | 143 ms: 1.13x faster                                                         |
| nqueens                 | 112 ms                                                       | 100 ms: 1.12x faster                                                         |
| sympy_sum               | 193 ms                                                       | 172 ms: 1.12x faster                                                         |
| mdp                     | 3.03 sec                                                     | 2.72 sec: 1.11x faster                                                       |
| telco                   | 7.14 ms                                                      | 6.61 ms: 1.08x faster                                                        |
| pidigits                | 271 ms                                                       | 251 ms: 1.08x faster                                                         |
| meteor_contest          | 137 ms                                                       | 128 ms: 1.07x faster                                                         |
| unpickle                | 14.2 us                                                      | 13.5 us: 1.05x faster                                                        |
| xml_etree_iterparse     | 110 ms                                                       | 106 ms: 1.04x faster                                                         |
| coroutines              | 30.4 ms                                                      | 29.2 ms: 1.04x faster                                                        |
| pickle_list             | 4.11 us                                                      | 3.95 us: 1.04x faster                                                        |
| unpickle_list           | 4.49 us                                                      | 4.36 us: 1.03x faster                                                        |
| python_startup          | 11.5 ms                                                      | 11.2 ms: 1.03x faster                                                        |
| pickle                  | 9.94 us                                                      | 10.1 us: 1.02x slower                                                        |
| generators              | 58.0 ms                                                      | 60.8 ms: 1.05x slower                                                        |
| pickle_dict             | 30.0 us                                                      | 32.6 us: 1.09x slower                                                        |
| gc_traversal            | 3.45 ms                                                      | 3.76 ms: 1.09x slower                                                        |
| regex_effbot            | 2.99 ms                                                      | 3.31 ms: 1.11x slower                                                        |
| python_startup_no_site  | 7.32 ms                                                      | 8.26 ms: 1.13x slower                                                        |
| dask                    | 463 ms                                                       | 568 ms: 1.23x slower                                                         |
| coverage                | 64.0 ms                                                      | 82.2 ms: 1.29x slower                                                        |
| Geometric mean          | (ref)                                                        | 1.27x faster                                                                 |
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.21x
