
# Results vs. 3.10.4

- fork: ericsnowcurrently
- ref: per_interpreter_gil_
- machine: windows-amd64
- commit hash: f3fd844
- commit date: 2023-05-04
- overall geometric mean: 1.17x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.11x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230504-pythonperf1-amd64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| 2to3           | 237 ms                                                      | 208 ms: 1.14x faster                                                                   |
| docutils       | 1.89 sec                                                    | 1.60 sec: 1.18x faster                                                                 |
| tornado_http   | 109 ms                                                      | 89.0 ms: 1.23x faster                                                                  |
| Geometric mean | (ref)                                                       | 1.18x faster                                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230504-pythonperf1-amd64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| float          | 60.2 ms                                                     | 52.1 ms: 1.16x faster                                                                  |
| nbody          | 69.3 ms                                                     | 68.6 ms: 1.01x faster                                                                  |
| pidigits       | 145 ms                                                      | 150 ms: 1.03x slower                                                                   |
| Geometric mean | (ref)                                                       | 1.04x faster                                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230504-pythonperf1-amd64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| regex_compile  | 103 ms                                                      | 85.1 ms: 1.22x faster                                                                  |
| regex_dna      | 132 ms                                                      | 116 ms: 1.13x faster                                                                   |
| regex_v8       | 15.0 ms                                                     | 14.1 ms: 1.07x faster                                                                  |
| regex_effbot   | 1.66 ms                                                     | 1.58 ms: 1.06x faster                                                                  |
| Geometric mean | (ref)                                                       | 1.12x faster                                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230504-pythonperf1-amd64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| json_dumps           | 8.50 ms                                                     | 5.60 ms: 1.52x faster                                                                  |
| pickle_pure_python   | 257 us                                                      | 191 us: 1.34x faster                                                                   |
| unpickle_pure_python | 171 us                                                      | 136 us: 1.26x faster                                                                   |
| xml_etree_process    | 43.4 ms                                                     | 37.2 ms: 1.17x faster                                                                  |
| xml_etree_parse      | 102 ms                                                      | 91.3 ms: 1.11x faster                                                                  |
| unpickle             | 9.17 us                                                     | 8.46 us: 1.09x faster                                                                  |
| xml_etree_iterparse  | 63.5 ms                                                     | 61.1 ms: 1.04x faster                                                                  |
| pickle               | 6.80 us                                                     | 6.95 us: 1.02x slower                                                                  |
| pickle_dict          | 16.9 us                                                     | 18.1 us: 1.07x slower                                                                  |
| pickle_list          | 2.59 us                                                     | 2.76 us: 1.07x slower                                                                  |
| Geometric mean       | (ref)                                                       | 1.09x faster                                                                           |

Benchmark hidden because not significant (3): json_loads, xml_etree_generate, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230504-pythonperf1-amd64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| python_startup         | 20.0 ms                                                     | 18.8 ms: 1.06x faster                                                                  |
| python_startup_no_site | 15.5 ms                                                     | 15.9 ms: 1.02x slower                                                                  |
| Geometric mean         | (ref)                                                       | 1.02x faster                                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230504-pythonperf1-amd64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|-----------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| mako      | 8.80 ms                                                     | 6.60 ms: 1.33x faster                                                                  |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230504-pythonperf1-amd64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| deltablue               | 4.17 ms                                                     | 2.05 ms: 2.03x faster                                                                  |
| logging_silent          | 96.4 ns                                                     | 58.1 ns: 1.66x faster                                                                  |
| mypy2                   | 352 ms                                                      | 214 ms: 1.64x faster                                                                   |
| richards                | 41.2 ms                                                     | 25.7 ms: 1.60x faster                                                                  |
| asyncio_tcp             | 712 ms                                                      | 456 ms: 1.56x faster                                                                   |
| go                      | 136 ms                                                      | 87.9 ms: 1.55x faster                                                                  |
| sqlglot_parse           | 1.22 ms                                                     | 791 us: 1.54x faster                                                                   |
| generators              | 31.6 ms                                                     | 20.7 ms: 1.53x faster                                                                  |
| json_dumps              | 8.50 ms                                                     | 5.60 ms: 1.52x faster                                                                  |
| scimark_lu              | 85.4 ms                                                     | 56.8 ms: 1.50x faster                                                                  |
| async_tree_io           | 1.07 sec                                                    | 727 ms: 1.47x faster                                                                   |
| sqlglot_transpile       | 1.46 ms                                                     | 999 us: 1.46x faster                                                                   |
| raytrace                | 271 ms                                                      | 185 ms: 1.46x faster                                                                   |
| async_tree_memoization  | 497 ms                                                      | 341 ms: 1.46x faster                                                                   |
| async_tree_none         | 420 ms                                                      | 289 ms: 1.45x faster                                                                   |
| hexiom                  | 5.52 ms                                                     | 3.99 ms: 1.38x faster                                                                  |
| scimark_sor             | 105 ms                                                      | 78.1 ms: 1.34x faster                                                                  |
| pickle_pure_python      | 257 us                                                      | 191 us: 1.34x faster                                                                   |
| pyflate                 | 387 ms                                                      | 289 ms: 1.34x faster                                                                   |
| mako                    | 8.80 ms                                                     | 6.60 ms: 1.33x faster                                                                  |
| chaos                   | 58.9 ms                                                     | 44.8 ms: 1.32x faster                                                                  |
| crypto_pyaes            | 62.3 ms                                                     | 47.4 ms: 1.31x faster                                                                  |
| async_tree_cpu_io_mixed | 609 ms                                                      | 464 ms: 1.31x faster                                                                   |
| pycparser               | 868 ms                                                      | 666 ms: 1.30x faster                                                                   |
| scimark_monte_carlo     | 55.9 ms                                                     | 43.3 ms: 1.29x faster                                                                  |
| unpickle_pure_python    | 171 us                                                      | 136 us: 1.26x faster                                                                   |
| tornado_http            | 109 ms                                                      | 89.0 ms: 1.23x faster                                                                  |
| regex_compile           | 103 ms                                                      | 85.1 ms: 1.22x faster                                                                  |
| spectral_norm           | 78.0 ms                                                     | 64.3 ms: 1.21x faster                                                                  |
| mdp                     | 1.71 sec                                                    | 1.42 sec: 1.21x faster                                                                 |
| deepcopy_memo           | 28.5 us                                                     | 23.9 us: 1.20x faster                                                                  |
| docutils                | 1.89 sec                                                    | 1.60 sec: 1.18x faster                                                                 |
| xml_etree_process       | 43.4 ms                                                     | 37.2 ms: 1.17x faster                                                                  |
| pprint_pformat          | 1.21 sec                                                    | 1.04 sec: 1.16x faster                                                                 |
| create_gc_cycles        | 782 us                                                      | 676 us: 1.16x faster                                                                   |
| float                   | 60.2 ms                                                     | 52.1 ms: 1.16x faster                                                                  |
| pprint_safe_repr        | 589 ms                                                      | 511 ms: 1.15x faster                                                                   |
| sqlglot_optimize        | 39.0 ms                                                     | 34.0 ms: 1.15x faster                                                                  |
| 2to3                    | 237 ms                                                      | 208 ms: 1.14x faster                                                                   |
| coroutines              | 15.9 ms                                                     | 14.0 ms: 1.14x faster                                                                  |
| regex_dna               | 132 ms                                                      | 116 ms: 1.13x faster                                                                   |
| bench_thread_pool       | 946 us                                                      | 843 us: 1.12x faster                                                                   |
| nqueens                 | 67.0 ms                                                     | 59.9 ms: 1.12x faster                                                                  |
| xml_etree_parse         | 102 ms                                                      | 91.3 ms: 1.11x faster                                                                  |
| scimark_fft             | 193 ms                                                      | 174 ms: 1.11x faster                                                                   |
| dulwich_log             | 47.6 ms                                                     | 43.1 ms: 1.11x faster                                                                  |
| scimark_sparse_mat_mult | 2.66 ms                                                     | 2.42 ms: 1.10x faster                                                                  |
| sqlglot_normalize       | 202 ms                                                      | 185 ms: 1.09x faster                                                                   |
| deepcopy                | 255 us                                                      | 234 us: 1.09x faster                                                                   |
| unpickle                | 9.17 us                                                     | 8.46 us: 1.09x faster                                                                  |
| sqlite_synth            | 1.84 us                                                     | 1.71 us: 1.08x faster                                                                  |
| regex_v8                | 15.0 ms                                                     | 14.1 ms: 1.07x faster                                                                  |
| python_startup          | 20.0 ms                                                     | 18.8 ms: 1.06x faster                                                                  |
| fannkuch                | 258 ms                                                      | 244 ms: 1.06x faster                                                                   |
| regex_effbot            | 1.66 ms                                                     | 1.58 ms: 1.06x faster                                                                  |
| deepcopy_reduce         | 2.16 us                                                     | 2.07 us: 1.04x faster                                                                  |
| xml_etree_iterparse     | 63.5 ms                                                     | 61.1 ms: 1.04x faster                                                                  |
| json                    | 3.05 ms                                                     | 2.96 ms: 1.03x faster                                                                  |
| nbody                   | 69.3 ms                                                     | 68.6 ms: 1.01x faster                                                                  |
| comprehensions          | 16.0 us                                                     | 15.9 us: 1.00x faster                                                                  |
| async_generators        | 224 ms                                                      | 228 ms: 1.02x slower                                                                   |
| pickle                  | 6.80 us                                                     | 6.95 us: 1.02x slower                                                                  |
| python_startup_no_site  | 15.5 ms                                                     | 15.9 ms: 1.02x slower                                                                  |
| pidigits                | 145 ms                                                      | 150 ms: 1.03x slower                                                                   |
| logging_simple          | 6.20 us                                                     | 6.51 us: 1.05x slower                                                                  |
| logging_format          | 6.66 us                                                     | 7.03 us: 1.06x slower                                                                  |
| pathlib                 | 77.4 ms                                                     | 81.7 ms: 1.06x slower                                                                  |
| gc_traversal            | 1.34 ms                                                     | 1.43 ms: 1.06x slower                                                                  |
| pickle_dict             | 16.9 us                                                     | 18.1 us: 1.07x slower                                                                  |
| pickle_list             | 2.59 us                                                     | 2.76 us: 1.07x slower                                                                  |
| meteor_contest          | 72.5 ms                                                     | 79.0 ms: 1.09x slower                                                                  |
| telco                   | 3.78 ms                                                     | 4.14 ms: 1.10x slower                                                                  |
| bench_mp_pool           | 60.7 ms                                                     | 67.1 ms: 1.11x slower                                                                  |
| unpack_sequence         | 37.8 ns                                                     | 42.2 ns: 1.12x slower                                                                  |
| dask                    | 305 ms                                                      | 366 ms: 1.20x slower                                                                   |
| coverage                | 40.0 ms                                                     | 52.3 ms: 1.31x slower                                                                  |
| Geometric mean          | (ref)                                                       | 1.17x faster                                                                           |

Benchmark hidden because not significant (3): json_loads, xml_etree_generate, unpickle_list
Ignored benchmarks (19) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.14x
- 95% likely to have a speedup of 1.13x
- 99% likely to have a speedup of 1.11x
