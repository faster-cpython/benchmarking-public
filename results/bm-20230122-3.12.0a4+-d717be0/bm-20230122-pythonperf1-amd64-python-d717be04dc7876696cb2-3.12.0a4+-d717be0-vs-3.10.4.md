
# Results vs. 3.10.4

- fork: python
- ref: d717be04dc7876696cb2
- machine: windows-amd64
- commit hash: d717be0
- commit date: 2023-01-22
- overall geometric mean: 1.22x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230122-pythonperf1-amd64-python-d717be04dc7876696cb2-3.12.0a4+-d717be0 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 237 ms                                                      | 202 ms: 1.17x faster                                                        |
| chameleon      | 5.92 ms                                                     | 4.37 ms: 1.36x faster                                                       |
| docutils       | 1.89 sec                                                    | 1.55 sec: 1.22x faster                                                      |
| html5lib       | 46.5 ms                                                     | 35.7 ms: 1.30x faster                                                       |
| tornado_http   | 109 ms                                                      | 88.8 ms: 1.23x faster                                                       |
| Geometric mean | (ref)                                                       | 1.25x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230122-pythonperf1-amd64-python-d717be04dc7876696cb2-3.12.0a4+-d717be0 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 60.2 ms                                                     | 47.2 ms: 1.28x faster                                                       |
| nbody          | 69.3 ms                                                     | 59.7 ms: 1.16x faster                                                       |
| pidigits       | 145 ms                                                      | 151 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                       | 1.13x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230122-pythonperf1-amd64-python-d717be04dc7876696cb2-3.12.0a4+-d717be0 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 103 ms                                                      | 78.1 ms: 1.32x faster                                                       |
| regex_dna      | 132 ms                                                      | 117 ms: 1.12x faster                                                        |
| regex_v8       | 15.0 ms                                                     | 13.6 ms: 1.11x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.54 ms: 1.08x faster                                                       |
| Geometric mean | (ref)                                                       | 1.15x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230122-pythonperf1-amd64-python-d717be04dc7876696cb2-3.12.0a4+-d717be0 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 8.50 ms                                                     | 5.43 ms: 1.57x faster                                                       |
| pickle_pure_python   | 257 us                                                      | 171 us: 1.50x faster                                                        |
| unpickle_pure_python | 171 us                                                      | 121 us: 1.42x faster                                                        |
| xml_etree_process    | 43.4 ms                                                     | 35.0 ms: 1.24x faster                                                       |
| json_loads           | 14.2 us                                                     | 12.8 us: 1.11x faster                                                       |
| xml_etree_generate   | 54.5 ms                                                     | 49.7 ms: 1.10x faster                                                       |
| xml_etree_parse      | 102 ms                                                      | 94.7 ms: 1.07x faster                                                       |
| unpickle_list        | 2.81 us                                                     | 2.76 us: 1.02x faster                                                       |
| pickle               | 6.80 us                                                     | 6.94 us: 1.02x slower                                                       |
| pickle_list          | 2.59 us                                                     | 2.72 us: 1.05x slower                                                       |
| pickle_dict          | 16.9 us                                                     | 18.4 us: 1.09x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.13x faster                                                                |

Benchmark hidden because not significant (2): unpickle, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230122-pythonperf1-amd64-python-d717be04dc7876696cb2-3.12.0a4+-d717be0 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.0 ms                                                     | 19.2 ms: 1.04x faster                                                       |
| python_startup_no_site | 15.5 ms                                                     | 16.5 ms: 1.06x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.01x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230122-pythonperf1-amd64-python-d717be04dc7876696cb2-3.12.0a4+-d717be0 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 19.0 ms                                                     | 13.4 ms: 1.42x faster                                                       |
| mako            | 8.80 ms                                                     | 6.21 ms: 1.42x faster                                                       |
| django_template | 28.2 ms                                                     | 20.4 ms: 1.38x faster                                                       |
| genshi_xml      | 40.5 ms                                                     | 33.0 ms: 1.23x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.36x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230122-pythonperf1-amd64-python-d717be04dc7876696cb2-3.12.0a4+-d717be0 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deltablue               | 4.17 ms                                                     | 2.02 ms: 2.07x faster                                                       |
| logging_silent          | 96.4 ns                                                     | 56.5 ns: 1.71x faster                                                       |
| richards                | 41.2 ms                                                     | 24.2 ms: 1.70x faster                                                       |
| scimark_sor             | 105 ms                                                      | 64.2 ms: 1.63x faster                                                       |
| go                      | 136 ms                                                      | 83.7 ms: 1.63x faster                                                       |
| mypy2                   | 352 ms                                                      | 216 ms: 1.63x faster                                                        |
| raytrace                | 271 ms                                                      | 173 ms: 1.57x faster                                                        |
| json_dumps              | 8.50 ms                                                     | 5.43 ms: 1.57x faster                                                       |
| pyflate                 | 387 ms                                                      | 258 ms: 1.50x faster                                                        |
| pickle_pure_python      | 257 us                                                      | 171 us: 1.50x faster                                                        |
| scimark_lu              | 85.4 ms                                                     | 57.6 ms: 1.48x faster                                                       |
| hexiom                  | 5.52 ms                                                     | 3.73 ms: 1.48x faster                                                       |
| asyncio_tcp             | 712 ms                                                      | 483 ms: 1.48x faster                                                        |
| unpack_sequence         | 37.8 ns                                                     | 25.7 ns: 1.47x faster                                                       |
| chaos                   | 58.9 ms                                                     | 40.1 ms: 1.47x faster                                                       |
| genshi_text             | 19.0 ms                                                     | 13.4 ms: 1.42x faster                                                       |
| mako                    | 8.80 ms                                                     | 6.21 ms: 1.42x faster                                                       |
| unpickle_pure_python    | 171 us                                                      | 121 us: 1.42x faster                                                        |
| sqlglot_parse           | 1.22 ms                                                     | 863 us: 1.41x faster                                                        |
| deepcopy_memo           | 28.5 us                                                     | 20.2 us: 1.41x faster                                                       |
| scimark_monte_carlo     | 55.9 ms                                                     | 40.2 ms: 1.39x faster                                                       |
| sqlglot_transpile       | 1.46 ms                                                     | 1.06 ms: 1.39x faster                                                       |
| django_template         | 28.2 ms                                                     | 20.4 ms: 1.38x faster                                                       |
| async_tree_io           | 1.07 sec                                                    | 770 ms: 1.38x faster                                                        |
| crypto_pyaes            | 62.3 ms                                                     | 45.2 ms: 1.38x faster                                                       |
| async_tree_none         | 420 ms                                                      | 308 ms: 1.37x faster                                                        |
| chameleon               | 5.92 ms                                                     | 4.37 ms: 1.36x faster                                                       |
| thrift                  | 615 us                                                      | 456 us: 1.35x faster                                                        |
| async_tree_memoization  | 497 ms                                                      | 374 ms: 1.33x faster                                                        |
| pycparser               | 868 ms                                                      | 653 ms: 1.33x faster                                                        |
| regex_compile           | 103 ms                                                      | 78.1 ms: 1.32x faster                                                       |
| async_generators        | 224 ms                                                      | 171 ms: 1.31x faster                                                        |
| html5lib                | 46.5 ms                                                     | 35.7 ms: 1.30x faster                                                       |
| spectral_norm           | 78.0 ms                                                     | 60.5 ms: 1.29x faster                                                       |
| pprint_pformat          | 1.21 sec                                                    | 945 ms: 1.28x faster                                                        |
| float                   | 60.2 ms                                                     | 47.2 ms: 1.28x faster                                                       |
| deepcopy                | 255 us                                                      | 201 us: 1.27x faster                                                        |
| pprint_safe_repr        | 589 ms                                                      | 469 ms: 1.26x faster                                                        |
| xml_etree_process       | 43.4 ms                                                     | 35.0 ms: 1.24x faster                                                       |
| genshi_xml              | 40.5 ms                                                     | 33.0 ms: 1.23x faster                                                       |
| tornado_http            | 109 ms                                                      | 88.8 ms: 1.23x faster                                                       |
| scimark_sparse_mat_mult | 2.66 ms                                                     | 2.16 ms: 1.23x faster                                                       |
| docutils                | 1.89 sec                                                    | 1.55 sec: 1.22x faster                                                      |
| async_tree_cpu_io_mixed | 609 ms                                                      | 502 ms: 1.21x faster                                                        |
| deepcopy_reduce         | 2.16 us                                                     | 1.80 us: 1.20x faster                                                       |
| sqlglot_optimize        | 39.0 ms                                                     | 32.5 ms: 1.20x faster                                                       |
| nqueens                 | 67.0 ms                                                     | 55.9 ms: 1.20x faster                                                       |
| dask                    | 305 ms                                                      | 257 ms: 1.19x faster                                                        |
| fannkuch                | 258 ms                                                      | 218 ms: 1.18x faster                                                        |
| 2to3                    | 237 ms                                                      | 202 ms: 1.17x faster                                                        |
| sqlglot_normalize       | 202 ms                                                      | 174 ms: 1.16x faster                                                        |
| sympy_expand            | 315 ms                                                      | 271 ms: 1.16x faster                                                        |
| nbody                   | 69.3 ms                                                     | 59.7 ms: 1.16x faster                                                       |
| sympy_integrate         | 14.8 ms                                                     | 12.8 ms: 1.16x faster                                                       |
| scimark_fft             | 193 ms                                                      | 167 ms: 1.16x faster                                                        |
| regex_dna               | 132 ms                                                      | 117 ms: 1.12x faster                                                        |
| dulwich_log             | 47.6 ms                                                     | 42.5 ms: 1.12x faster                                                       |
| bench_thread_pool       | 946 us                                                      | 846 us: 1.12x faster                                                        |
| sympy_str               | 188 ms                                                      | 169 ms: 1.11x faster                                                        |
| create_gc_cycles        | 782 us                                                      | 702 us: 1.11x faster                                                        |
| json_loads              | 14.2 us                                                     | 12.8 us: 1.11x faster                                                       |
| json                    | 3.05 ms                                                     | 2.75 ms: 1.11x faster                                                       |
| regex_v8                | 15.0 ms                                                     | 13.6 ms: 1.11x faster                                                       |
| xml_etree_generate      | 54.5 ms                                                     | 49.7 ms: 1.10x faster                                                       |
| coroutines              | 15.9 ms                                                     | 14.6 ms: 1.09x faster                                                       |
| sympy_sum               | 104 ms                                                      | 95.6 ms: 1.09x faster                                                       |
| mdp                     | 1.71 sec                                                    | 1.57 sec: 1.09x faster                                                      |
| regex_effbot            | 1.66 ms                                                     | 1.54 ms: 1.08x faster                                                       |
| xml_etree_parse         | 102 ms                                                      | 94.7 ms: 1.07x faster                                                       |
| comprehensions          | 16.0 us                                                     | 15.0 us: 1.07x faster                                                       |
| sqlite_synth            | 1.84 us                                                     | 1.74 us: 1.06x faster                                                       |
| telco                   | 3.78 ms                                                     | 3.61 ms: 1.05x faster                                                       |
| logging_format          | 6.66 us                                                     | 6.38 us: 1.04x faster                                                       |
| python_startup          | 20.0 ms                                                     | 19.2 ms: 1.04x faster                                                       |
| pathlib                 | 77.4 ms                                                     | 74.8 ms: 1.03x faster                                                       |
| meteor_contest          | 72.5 ms                                                     | 70.3 ms: 1.03x faster                                                       |
| unpickle_list           | 2.81 us                                                     | 2.76 us: 1.02x faster                                                       |
| pickle                  | 6.80 us                                                     | 6.94 us: 1.02x slower                                                       |
| pidigits                | 145 ms                                                      | 151 ms: 1.04x slower                                                        |
| bench_mp_pool           | 60.7 ms                                                     | 63.3 ms: 1.04x slower                                                       |
| pickle_list             | 2.59 us                                                     | 2.72 us: 1.05x slower                                                       |
| python_startup_no_site  | 15.5 ms                                                     | 16.5 ms: 1.06x slower                                                       |
| generators              | 31.6 ms                                                     | 33.9 ms: 1.07x slower                                                       |
| pickle_dict             | 16.9 us                                                     | 18.4 us: 1.09x slower                                                       |
| gc_traversal            | 1.34 ms                                                     | 1.51 ms: 1.13x slower                                                       |
| coverage                | 40.0 ms                                                     | 52.6 ms: 1.31x slower                                                       |
| Geometric mean          | (ref)                                                       | 1.22x faster                                                                |

Benchmark hidden because not significant (3): unpickle, xml_etree_iterparse, logging_simple
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.19x
- 95% likely to have a speedup of 1.18x
- 99% likely to have a speedup of 1.16x
