
# Results vs. 3.10.4

- fork: python
- ref: f9774e57d84162ff0cba
- machine: linux-x86_64
- commit hash: f9774e5
- commit date: 2023-03-07
- overall geometric mean: 1.26x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230307-pythonperf2-x86_64-python-f9774e57d84162ff0cba-3.12.0a6-f9774e5 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 284 ms: 1.23x faster                                                        |
| chameleon      | 9.72 ms                                                      | 6.94 ms: 1.40x faster                                                       |
| docutils       | 3.40 sec                                                     | 2.79 sec: 1.22x faster                                                      |
| html5lib       | 94.6 ms                                                      | 65.9 ms: 1.44x faster                                                       |
| tornado_http   | 152 ms                                                       | 115 ms: 1.32x faster                                                        |
| Geometric mean | (ref)                                                        | 1.32x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230307-pythonperf2-x86_64-python-f9774e57d84162ff0cba-3.12.0a6-f9774e5 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 137 ms                                                       | 91.0 ms: 1.51x faster                                                       |
| float          | 110 ms                                                       | 73.9 ms: 1.49x faster                                                       |
| pidigits       | 271 ms                                                       | 251 ms: 1.08x faster                                                        |
| Geometric mean | (ref)                                                        | 1.34x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230307-pythonperf2-x86_64-python-f9774e57d84162ff0cba-3.12.0a6-f9774e5 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 194 ms                                                       | 146 ms: 1.33x faster                                                        |
| regex_v8       | 26.6 ms                                                      | 22.8 ms: 1.17x faster                                                       |
| regex_dna      | 259 ms                                                       | 225 ms: 1.15x faster                                                        |
| regex_effbot   | 2.99 ms                                                      | 3.36 ms: 1.12x slower                                                       |
| Geometric mean | (ref)                                                        | 1.12x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230307-pythonperf2-x86_64-python-f9774e57d84162ff0cba-3.12.0a6-f9774e5 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 321 us                                                       | 202 us: 1.59x faster                                                        |
| pickle_pure_python   | 457 us                                                       | 306 us: 1.49x faster                                                        |
| json_dumps           | 14.2 ms                                                      | 10.2 ms: 1.39x faster                                                       |
| xml_etree_process    | 76.0 ms                                                      | 57.3 ms: 1.33x faster                                                       |
| json_loads           | 30.0 us                                                      | 24.4 us: 1.23x faster                                                       |
| xml_etree_generate   | 94.6 ms                                                      | 83.5 ms: 1.13x faster                                                       |
| xml_etree_parse      | 162 ms                                                       | 144 ms: 1.12x faster                                                        |
| pickle_list          | 4.11 us                                                      | 3.80 us: 1.08x faster                                                       |
| xml_etree_iterparse  | 110 ms                                                       | 103 ms: 1.07x faster                                                        |
| unpickle             | 14.2 us                                                      | 13.4 us: 1.06x faster                                                       |
| unpickle_list        | 4.49 us                                                      | 4.44 us: 1.01x faster                                                       |
| pickle               | 9.94 us                                                      | 10.0 us: 1.01x slower                                                       |
| pickle_dict          | 30.0 us                                                      | 31.8 us: 1.06x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.17x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230307-pythonperf2-x86_64-python-f9774e57d84162ff0cba-3.12.0a6-f9774e5 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 11.3 ms: 1.02x faster                                                       |
| python_startup_no_site | 7.32 ms                                                      | 8.34 ms: 1.14x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.06x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230307-pythonperf2-x86_64-python-f9774e57d84162ff0cba-3.12.0a6-f9774e5 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.0 ms: 1.46x faster                                                       |
| django_template | 51.5 ms                                                      | 39.1 ms: 1.32x faster                                                       |
| genshi_text     | 31.5 ms                                                      | 24.6 ms: 1.28x faster                                                       |
| genshi_xml      | 64.7 ms                                                      | 53.0 ms: 1.22x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.32x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230307-pythonperf2-x86_64-python-f9774e57d84162ff0cba-3.12.0a6-f9774e5 |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deltablue               | 7.47 ms                                                      | 3.33 ms: 2.24x faster                                                       |
| asyncio_tcp             | 782 ms                                                       | 382 ms: 2.05x faster                                                        |
| logging_silent          | 166 ns                                                       | 94.5 ns: 1.75x faster                                                       |
| go                      | 259 ms                                                       | 151 ms: 1.72x faster                                                        |
| raytrace                | 488 ms                                                       | 290 ms: 1.68x faster                                                        |
| scimark_sor             | 177 ms                                                       | 105 ms: 1.68x faster                                                        |
| pyflate                 | 697 ms                                                       | 432 ms: 1.61x faster                                                        |
| richards                | 74.1 ms                                                      | 46.4 ms: 1.60x faster                                                       |
| unpickle_pure_python    | 321 us                                                       | 202 us: 1.59x faster                                                        |
| scimark_monte_carlo     | 109 ms                                                       | 69.5 ms: 1.57x faster                                                       |
| scimark_lu              | 164 ms                                                       | 105 ms: 1.56x faster                                                        |
| chaos                   | 107 ms                                                       | 70.9 ms: 1.51x faster                                                       |
| generators              | 58.0 ms                                                      | 38.4 ms: 1.51x faster                                                       |
| nbody                   | 137 ms                                                       | 91.0 ms: 1.51x faster                                                       |
| pickle_pure_python      | 457 us                                                       | 306 us: 1.49x faster                                                        |
| float                   | 110 ms                                                       | 73.9 ms: 1.49x faster                                                       |
| bench_mp_pool           | 7.18 ms                                                      | 4.84 ms: 1.48x faster                                                       |
| hexiom                  | 9.52 ms                                                      | 6.46 ms: 1.47x faster                                                       |
| mako                    | 14.7 ms                                                      | 10.0 ms: 1.46x faster                                                       |
| crypto_pyaes            | 118 ms                                                       | 81.5 ms: 1.45x faster                                                       |
| html5lib                | 94.6 ms                                                      | 65.9 ms: 1.44x faster                                                       |
| sqlglot_parse           | 2.26 ms                                                      | 1.58 ms: 1.43x faster                                                       |
| spectral_norm           | 136 ms                                                       | 95.6 ms: 1.42x faster                                                       |
| chameleon               | 9.72 ms                                                      | 6.94 ms: 1.40x faster                                                       |
| sqlglot_transpile       | 2.71 ms                                                      | 1.94 ms: 1.40x faster                                                       |
| json_dumps              | 14.2 ms                                                      | 10.2 ms: 1.39x faster                                                       |
| pprint_pformat          | 2.15 sec                                                     | 1.55 sec: 1.39x faster                                                      |
| deepcopy_memo           | 48.9 us                                                      | 35.4 us: 1.38x faster                                                       |
| pprint_safe_repr        | 1.05 sec                                                     | 762 ms: 1.38x faster                                                        |
| async_tree_io           | 1.61 sec                                                     | 1.17 sec: 1.38x faster                                                      |
| async_tree_none         | 700 ms                                                       | 510 ms: 1.37x faster                                                        |
| async_tree_memoization  | 824 ms                                                       | 611 ms: 1.35x faster                                                        |
| pycparser               | 1.66 sec                                                     | 1.23 sec: 1.35x faster                                                      |
| unpack_sequence         | 59.5 ns                                                      | 44.4 ns: 1.34x faster                                                       |
| regex_compile           | 194 ms                                                       | 146 ms: 1.33x faster                                                        |
| xml_etree_process       | 76.0 ms                                                      | 57.3 ms: 1.33x faster                                                       |
| tornado_http            | 152 ms                                                       | 115 ms: 1.32x faster                                                        |
| django_template         | 51.5 ms                                                      | 39.1 ms: 1.32x faster                                                       |
| logging_simple          | 8.90 us                                                      | 6.79 us: 1.31x faster                                                       |
| scimark_fft             | 359 ms                                                       | 278 ms: 1.29x faster                                                        |
| thrift                  | 1.16 ms                                                      | 909 us: 1.28x faster                                                        |
| genshi_text             | 31.5 ms                                                      | 24.6 ms: 1.28x faster                                                       |
| async_tree_cpu_io_mixed | 952 ms                                                       | 745 ms: 1.28x faster                                                        |
| logging_format          | 9.57 us                                                      | 7.59 us: 1.26x faster                                                       |
| dulwich_log             | 80.1 ms                                                      | 63.7 ms: 1.26x faster                                                       |
| scimark_sparse_mat_mult | 5.19 ms                                                      | 4.14 ms: 1.26x faster                                                       |
| mypy2                   | 466 ms                                                       | 377 ms: 1.24x faster                                                        |
| coroutines              | 30.4 ms                                                      | 24.7 ms: 1.23x faster                                                       |
| 2to3                    | 350 ms                                                       | 284 ms: 1.23x faster                                                        |
| json_loads              | 30.0 us                                                      | 24.4 us: 1.23x faster                                                       |
| genshi_xml              | 64.7 ms                                                      | 53.0 ms: 1.22x faster                                                       |
| docutils                | 3.40 sec                                                     | 2.79 sec: 1.22x faster                                                      |
| fannkuch                | 496 ms                                                       | 408 ms: 1.22x faster                                                        |
| deepcopy_reduce         | 4.03 us                                                      | 3.33 us: 1.21x faster                                                       |
| sqlglot_optimize        | 70.3 ms                                                      | 58.2 ms: 1.21x faster                                                       |
| deepcopy                | 454 us                                                       | 377 us: 1.20x faster                                                        |
| sqlglot_normalize       | 144 ms                                                       | 120 ms: 1.20x faster                                                        |
| mdp                     | 3.03 sec                                                     | 2.54 sec: 1.19x faster                                                      |
| json                    | 5.96 ms                                                      | 5.00 ms: 1.19x faster                                                       |
| pathlib                 | 21.7 ms                                                      | 18.5 ms: 1.17x faster                                                       |
| regex_v8                | 26.6 ms                                                      | 22.8 ms: 1.17x faster                                                       |
| bench_thread_pool       | 1.14 ms                                                      | 974 us: 1.17x faster                                                        |
| nqueens                 | 112 ms                                                       | 96.9 ms: 1.16x faster                                                       |
| regex_dna               | 259 ms                                                       | 225 ms: 1.15x faster                                                        |
| xml_etree_generate      | 94.6 ms                                                      | 83.5 ms: 1.13x faster                                                       |
| sqlite_synth            | 2.97 us                                                      | 2.63 us: 1.13x faster                                                       |
| sympy_integrate         | 28.1 ms                                                      | 25.0 ms: 1.12x faster                                                       |
| xml_etree_parse         | 162 ms                                                       | 144 ms: 1.12x faster                                                        |
| create_gc_cycles        | 1.82 ms                                                      | 1.63 ms: 1.12x faster                                                       |
| sympy_expand            | 599 ms                                                       | 538 ms: 1.11x faster                                                        |
| async_generators        | 422 ms                                                       | 385 ms: 1.10x faster                                                        |
| sympy_str               | 358 ms                                                       | 328 ms: 1.09x faster                                                        |
| pickle_list             | 4.11 us                                                      | 3.80 us: 1.08x faster                                                       |
| pidigits                | 271 ms                                                       | 251 ms: 1.08x faster                                                        |
| xml_etree_iterparse     | 110 ms                                                       | 103 ms: 1.07x faster                                                        |
| meteor_contest          | 137 ms                                                       | 128 ms: 1.07x faster                                                        |
| unpickle                | 14.2 us                                                      | 13.4 us: 1.06x faster                                                       |
| sympy_sum               | 193 ms                                                       | 184 ms: 1.05x faster                                                        |
| telco                   | 7.14 ms                                                      | 6.90 ms: 1.04x faster                                                       |
| python_startup          | 11.5 ms                                                      | 11.3 ms: 1.02x faster                                                       |
| unpickle_list           | 4.49 us                                                      | 4.44 us: 1.01x faster                                                       |
| comprehensions          | 26.9 us                                                      | 26.7 us: 1.01x faster                                                       |
| pickle                  | 9.94 us                                                      | 10.0 us: 1.01x slower                                                       |
| pickle_dict             | 30.0 us                                                      | 31.8 us: 1.06x slower                                                       |
| regex_effbot            | 2.99 ms                                                      | 3.36 ms: 1.12x slower                                                       |
| python_startup_no_site  | 7.32 ms                                                      | 8.34 ms: 1.14x slower                                                       |
| gc_traversal            | 3.45 ms                                                      | 3.99 ms: 1.16x slower                                                       |
| dask                    | 463 ms                                                       | 560 ms: 1.21x slower                                                        |
| coverage                | 64.0 ms                                                      | 82.2 ms: 1.29x slower                                                       |
| Geometric mean          | (ref)                                                        | 1.26x faster                                                                |
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.21x
