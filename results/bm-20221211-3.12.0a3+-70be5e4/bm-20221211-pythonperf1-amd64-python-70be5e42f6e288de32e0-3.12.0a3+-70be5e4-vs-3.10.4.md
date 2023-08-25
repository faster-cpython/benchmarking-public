
# Results vs. 3.10.4

- fork: python
- ref: 70be5e42f6e288de32e0
- machine: windows-amd64
- commit hash: 70be5e4
- commit date: 2022-12-11
- overall geometric mean: 1.18x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20221211-pythonperf1-amd64-python-70be5e42f6e288de32e0-3.12.0a3+-70be5e4 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 237 ms                                                      | 201 ms: 1.18x faster                                                        |
| chameleon      | 5.92 ms                                                     | 4.68 ms: 1.26x faster                                                       |
| docutils       | 1.89 sec                                                    | 1.58 sec: 1.20x faster                                                      |
| html5lib       | 46.5 ms                                                     | 36.2 ms: 1.28x faster                                                       |
| Geometric mean | (ref)                                                       | 1.23x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20221211-pythonperf1-amd64-python-70be5e42f6e288de32e0-3.12.0a3+-70be5e4 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 60.2 ms                                                     | 49.7 ms: 1.21x faster                                                       |
| nbody          | 69.3 ms                                                     | 62.7 ms: 1.11x faster                                                       |
| pidigits       | 145 ms                                                      | 147 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                       | 1.10x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20221211-pythonperf1-amd64-python-70be5e42f6e288de32e0-3.12.0a3+-70be5e4 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 103 ms                                                      | 84.9 ms: 1.22x faster                                                       |
| regex_v8       | 15.0 ms                                                     | 13.6 ms: 1.10x faster                                                       |
| regex_dna      | 132 ms                                                      | 120 ms: 1.09x faster                                                        |
| regex_effbot   | 1.66 ms                                                     | 1.54 ms: 1.08x faster                                                       |
| Geometric mean | (ref)                                                       | 1.12x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20221211-pythonperf1-amd64-python-70be5e42f6e288de32e0-3.12.0a3+-70be5e4 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 8.50 ms                                                     | 5.41 ms: 1.57x faster                                                       |
| pickle_pure_python   | 257 us                                                      | 184 us: 1.40x faster                                                        |
| unpickle_pure_python | 171 us                                                      | 130 us: 1.31x faster                                                        |
| xml_etree_process    | 43.4 ms                                                     | 35.3 ms: 1.23x faster                                                       |
| unpickle             | 9.17 us                                                     | 8.01 us: 1.15x faster                                                       |
| xml_etree_parse      | 102 ms                                                      | 91.5 ms: 1.11x faster                                                       |
| unpickle_list        | 2.81 us                                                     | 2.60 us: 1.08x faster                                                       |
| json_loads           | 14.2 us                                                     | 13.3 us: 1.07x faster                                                       |
| xml_etree_generate   | 54.5 ms                                                     | 51.2 ms: 1.06x faster                                                       |
| pickle               | 6.80 us                                                     | 7.21 us: 1.06x slower                                                       |
| pickle_list          | 2.59 us                                                     | 2.83 us: 1.09x slower                                                       |
| pickle_dict          | 16.9 us                                                     | 19.2 us: 1.13x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.12x faster                                                                |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20221211-pythonperf1-amd64-python-70be5e42f6e288de32e0-3.12.0a3+-70be5e4 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.0 ms                                                     | 19.0 ms: 1.05x faster                                                       |
| python_startup_no_site | 15.5 ms                                                     | 15.8 ms: 1.02x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.02x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20221211-pythonperf1-amd64-python-70be5e42f6e288de32e0-3.12.0a3+-70be5e4 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 8.80 ms                                                     | 6.18 ms: 1.42x faster                                                       |
| genshi_text     | 19.0 ms                                                     | 14.4 ms: 1.32x faster                                                       |
| django_template | 28.2 ms                                                     | 22.2 ms: 1.27x faster                                                       |
| genshi_xml      | 40.5 ms                                                     | 32.6 ms: 1.24x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.31x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20221211-pythonperf1-amd64-python-70be5e42f6e288de32e0-3.12.0a3+-70be5e4 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deltablue               | 4.17 ms                                                     | 2.17 ms: 1.92x faster                                                       |
| logging_silent          | 96.4 ns                                                     | 59.5 ns: 1.62x faster                                                       |
| mypy2                   | 352 ms                                                      | 221 ms: 1.59x faster                                                        |
| scimark_sor             | 105 ms                                                      | 66.7 ms: 1.57x faster                                                       |
| json_dumps              | 8.50 ms                                                     | 5.41 ms: 1.57x faster                                                       |
| richards                | 41.2 ms                                                     | 26.3 ms: 1.56x faster                                                       |
| go                      | 136 ms                                                      | 88.5 ms: 1.54x faster                                                       |
| raytrace                | 271 ms                                                      | 189 ms: 1.44x faster                                                        |
| scimark_lu              | 85.4 ms                                                     | 59.8 ms: 1.43x faster                                                       |
| asyncio_tcp             | 712 ms                                                      | 499 ms: 1.43x faster                                                        |
| mako                    | 8.80 ms                                                     | 6.18 ms: 1.42x faster                                                       |
| pickle_pure_python      | 257 us                                                      | 184 us: 1.40x faster                                                        |
| sqlglot_parse           | 1.22 ms                                                     | 878 us: 1.39x faster                                                        |
| pyflate                 | 387 ms                                                      | 282 ms: 1.37x faster                                                        |
| scimark_monte_carlo     | 55.9 ms                                                     | 41.2 ms: 1.36x faster                                                       |
| hexiom                  | 5.52 ms                                                     | 4.10 ms: 1.35x faster                                                       |
| sqlglot_transpile       | 1.46 ms                                                     | 1.09 ms: 1.35x faster                                                       |
| thrift                  | 615 us                                                      | 460 us: 1.34x faster                                                        |
| deepcopy_memo           | 28.5 us                                                     | 21.5 us: 1.33x faster                                                       |
| async_tree_io           | 1.07 sec                                                    | 803 ms: 1.33x faster                                                        |
| crypto_pyaes            | 62.3 ms                                                     | 47.0 ms: 1.32x faster                                                       |
| genshi_text             | 19.0 ms                                                     | 14.4 ms: 1.32x faster                                                       |
| unpickle_pure_python    | 171 us                                                      | 130 us: 1.31x faster                                                        |
| unpack_sequence         | 37.8 ns                                                     | 29.1 ns: 1.30x faster                                                       |
| chaos                   | 58.9 ms                                                     | 45.6 ms: 1.29x faster                                                       |
| async_tree_memoization  | 497 ms                                                      | 387 ms: 1.29x faster                                                        |
| html5lib                | 46.5 ms                                                     | 36.2 ms: 1.28x faster                                                       |
| async_tree_none         | 420 ms                                                      | 331 ms: 1.27x faster                                                        |
| django_template         | 28.2 ms                                                     | 22.2 ms: 1.27x faster                                                       |
| spectral_norm           | 78.0 ms                                                     | 61.6 ms: 1.27x faster                                                       |
| chameleon               | 5.92 ms                                                     | 4.68 ms: 1.26x faster                                                       |
| pycparser               | 868 ms                                                      | 689 ms: 1.26x faster                                                        |
| async_generators        | 224 ms                                                      | 179 ms: 1.25x faster                                                        |
| genshi_xml              | 40.5 ms                                                     | 32.6 ms: 1.24x faster                                                       |
| pprint_safe_repr        | 589 ms                                                      | 474 ms: 1.24x faster                                                        |
| pprint_pformat          | 1.21 sec                                                    | 972 ms: 1.24x faster                                                        |
| async_tree_cpu_io_mixed | 609 ms                                                      | 494 ms: 1.23x faster                                                        |
| xml_etree_process       | 43.4 ms                                                     | 35.3 ms: 1.23x faster                                                       |
| regex_compile           | 103 ms                                                      | 84.9 ms: 1.22x faster                                                       |
| float                   | 60.2 ms                                                     | 49.7 ms: 1.21x faster                                                       |
| docutils                | 1.89 sec                                                    | 1.58 sec: 1.20x faster                                                      |
| deepcopy                | 255 us                                                      | 214 us: 1.19x faster                                                        |
| 2to3                    | 237 ms                                                      | 201 ms: 1.18x faster                                                        |
| sqlglot_optimize        | 39.0 ms                                                     | 33.1 ms: 1.18x faster                                                       |
| deepcopy_reduce         | 2.16 us                                                     | 1.88 us: 1.15x faster                                                       |
| dask                    | 305 ms                                                      | 266 ms: 1.15x faster                                                        |
| unpickle                | 9.17 us                                                     | 8.01 us: 1.15x faster                                                       |
| create_gc_cycles        | 782 us                                                      | 683 us: 1.14x faster                                                        |
| dulwich_log             | 47.6 ms                                                     | 41.9 ms: 1.14x faster                                                       |
| sympy_integrate         | 14.8 ms                                                     | 13.1 ms: 1.13x faster                                                       |
| sqlglot_normalize       | 202 ms                                                      | 180 ms: 1.13x faster                                                        |
| bench_thread_pool       | 946 us                                                      | 846 us: 1.12x faster                                                        |
| scimark_sparse_mat_mult | 2.66 ms                                                     | 2.38 ms: 1.12x faster                                                       |
| sympy_expand            | 315 ms                                                      | 282 ms: 1.12x faster                                                        |
| xml_etree_parse         | 102 ms                                                      | 91.5 ms: 1.11x faster                                                       |
| nqueens                 | 67.0 ms                                                     | 60.4 ms: 1.11x faster                                                       |
| nbody                   | 69.3 ms                                                     | 62.7 ms: 1.11x faster                                                       |
| mdp                     | 1.71 sec                                                    | 1.55 sec: 1.11x faster                                                      |
| regex_v8                | 15.0 ms                                                     | 13.6 ms: 1.10x faster                                                       |
| json                    | 3.05 ms                                                     | 2.78 ms: 1.10x faster                                                       |
| regex_dna               | 132 ms                                                      | 120 ms: 1.09x faster                                                        |
| fannkuch                | 258 ms                                                      | 237 ms: 1.09x faster                                                        |
| scimark_fft             | 193 ms                                                      | 178 ms: 1.08x faster                                                        |
| coroutines              | 15.9 ms                                                     | 14.7 ms: 1.08x faster                                                       |
| regex_effbot            | 1.66 ms                                                     | 1.54 ms: 1.08x faster                                                       |
| unpickle_list           | 2.81 us                                                     | 2.60 us: 1.08x faster                                                       |
| sympy_str               | 188 ms                                                      | 176 ms: 1.07x faster                                                        |
| json_loads              | 14.2 us                                                     | 13.3 us: 1.07x faster                                                       |
| xml_etree_generate      | 54.5 ms                                                     | 51.2 ms: 1.06x faster                                                       |
| python_startup          | 20.0 ms                                                     | 19.0 ms: 1.05x faster                                                       |
| sympy_sum               | 104 ms                                                      | 99.4 ms: 1.05x faster                                                       |
| sqlite_synth            | 1.84 us                                                     | 1.78 us: 1.03x faster                                                       |
| pathlib                 | 77.4 ms                                                     | 75.4 ms: 1.03x faster                                                       |
| logging_simple          | 6.20 us                                                     | 6.11 us: 1.01x faster                                                       |
| comprehensions          | 16.0 us                                                     | 15.7 us: 1.01x faster                                                       |
| logging_format          | 6.66 us                                                     | 6.73 us: 1.01x slower                                                       |
| pidigits                | 145 ms                                                      | 147 ms: 1.01x slower                                                        |
| telco                   | 3.78 ms                                                     | 3.84 ms: 1.01x slower                                                       |
| python_startup_no_site  | 15.5 ms                                                     | 15.8 ms: 1.02x slower                                                       |
| bench_mp_pool           | 60.7 ms                                                     | 63.6 ms: 1.05x slower                                                       |
| pickle                  | 6.80 us                                                     | 7.21 us: 1.06x slower                                                       |
| pickle_list             | 2.59 us                                                     | 2.83 us: 1.09x slower                                                       |
| gc_traversal            | 1.34 ms                                                     | 1.51 ms: 1.12x slower                                                       |
| pickle_dict             | 16.9 us                                                     | 19.2 us: 1.13x slower                                                       |
| generators              | 31.6 ms                                                     | 38.0 ms: 1.20x slower                                                       |
| coverage                | 40.0 ms                                                     | 54.5 ms: 1.36x slower                                                       |
| Geometric mean          | (ref)                                                       | 1.18x faster                                                                |

Benchmark hidden because not significant (2): xml_etree_iterparse, meteor_contest
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, tornado_http, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.15x
- 95% likely to have a speedup of 1.14x
- 99% likely to have a speedup of 1.12x
