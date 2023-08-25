
# Results vs. 3.10.4

- fork: python
- ref: 3d5d3f7af6498effbc60
- machine: linux-x86_64
- commit hash: 3d5d3f7
- commit date: 2023-01-10
- overall geometric mean: 1.25x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230110-pythonperf2-x86_64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 286 ms: 1.22x faster                                                        |
| chameleon      | 9.72 ms                                                      | 7.31 ms: 1.33x faster                                                       |
| docutils       | 3.40 sec                                                     | 2.78 sec: 1.23x faster                                                      |
| html5lib       | 94.6 ms                                                      | 66.8 ms: 1.42x faster                                                       |
| Geometric mean | (ref)                                                        | 1.30x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230110-pythonperf2-x86_64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 110 ms                                                       | 72.4 ms: 1.52x faster                                                       |
| nbody          | 137 ms                                                       | 98.1 ms: 1.40x faster                                                       |
| pidigits       | 271 ms                                                       | 252 ms: 1.07x faster                                                        |
| Geometric mean | (ref)                                                        | 1.32x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230110-pythonperf2-x86_64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 194 ms                                                       | 149 ms: 1.30x faster                                                        |
| regex_v8       | 26.6 ms                                                      | 23.0 ms: 1.16x faster                                                       |
| regex_dna      | 259 ms                                                       | 229 ms: 1.13x faster                                                        |
| regex_effbot   | 2.99 ms                                                      | 3.43 ms: 1.15x slower                                                       |
| Geometric mean | (ref)                                                        | 1.10x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230110-pythonperf2-x86_64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 321 us                                                       | 214 us: 1.50x faster                                                        |
| pickle_pure_python   | 457 us                                                       | 313 us: 1.46x faster                                                        |
| json_dumps           | 14.2 ms                                                      | 10.1 ms: 1.41x faster                                                       |
| xml_etree_process    | 76.0 ms                                                      | 55.4 ms: 1.37x faster                                                       |
| json_loads           | 30.0 us                                                      | 24.0 us: 1.25x faster                                                       |
| xml_etree_generate   | 94.6 ms                                                      | 80.3 ms: 1.18x faster                                                       |
| xml_etree_parse      | 162 ms                                                       | 144 ms: 1.12x faster                                                        |
| pickle_list          | 4.11 us                                                      | 3.70 us: 1.11x faster                                                       |
| unpickle             | 14.2 us                                                      | 13.3 us: 1.06x faster                                                       |
| xml_etree_iterparse  | 110 ms                                                       | 104 ms: 1.06x faster                                                        |
| pickle               | 9.94 us                                                      | 9.71 us: 1.02x faster                                                       |
| pickle_dict          | 30.0 us                                                      | 31.1 us: 1.04x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.18x faster                                                                |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230110-pythonperf2-x86_64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 10.8 ms: 1.07x faster                                                       |
| python_startup_no_site | 7.32 ms                                                      | 7.87 ms: 1.07x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.00x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230110-pythonperf2-x86_64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.2 ms: 1.43x faster                                                       |
| django_template | 51.5 ms                                                      | 39.2 ms: 1.31x faster                                                       |
| genshi_text     | 31.5 ms                                                      | 24.8 ms: 1.27x faster                                                       |
| genshi_xml      | 64.7 ms                                                      | 53.7 ms: 1.21x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.30x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230110-pythonperf2-x86_64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| asyncio_tcp             | 782 ms                                                       | 386 ms: 2.03x faster                                                        |
| deltablue               | 7.47 ms                                                      | 3.69 ms: 2.03x faster                                                       |
| go                      | 259 ms                                                       | 153 ms: 1.69x faster                                                        |
| scimark_monte_carlo     | 109 ms                                                       | 66.6 ms: 1.64x faster                                                       |
| scimark_sor             | 177 ms                                                       | 108 ms: 1.64x faster                                                        |
| raytrace                | 488 ms                                                       | 299 ms: 1.63x faster                                                        |
| logging_silent          | 166 ns                                                       | 102 ns: 1.63x faster                                                        |
| scimark_lu              | 164 ms                                                       | 101 ms: 1.62x faster                                                        |
| pyflate                 | 697 ms                                                       | 433 ms: 1.61x faster                                                        |
| richards                | 74.1 ms                                                      | 46.9 ms: 1.58x faster                                                       |
| float                   | 110 ms                                                       | 72.4 ms: 1.52x faster                                                       |
| chaos                   | 107 ms                                                       | 70.9 ms: 1.51x faster                                                       |
| unpickle_pure_python    | 321 us                                                       | 214 us: 1.50x faster                                                        |
| pickle_pure_python      | 457 us                                                       | 313 us: 1.46x faster                                                        |
| crypto_pyaes            | 118 ms                                                       | 81.1 ms: 1.46x faster                                                       |
| bench_mp_pool           | 7.18 ms                                                      | 4.94 ms: 1.45x faster                                                       |
| mako                    | 14.7 ms                                                      | 10.2 ms: 1.43x faster                                                       |
| sqlglot_parse           | 2.26 ms                                                      | 1.59 ms: 1.42x faster                                                       |
| html5lib                | 94.6 ms                                                      | 66.8 ms: 1.42x faster                                                       |
| hexiom                  | 9.52 ms                                                      | 6.77 ms: 1.41x faster                                                       |
| json_dumps              | 14.2 ms                                                      | 10.1 ms: 1.41x faster                                                       |
| scimark_sparse_mat_mult | 5.19 ms                                                      | 3.70 ms: 1.40x faster                                                       |
| nbody                   | 137 ms                                                       | 98.1 ms: 1.40x faster                                                       |
| async_tree_io           | 1.61 sec                                                     | 1.15 sec: 1.39x faster                                                      |
| sqlglot_transpile       | 2.71 ms                                                      | 1.95 ms: 1.39x faster                                                       |
| async_tree_none         | 700 ms                                                       | 505 ms: 1.39x faster                                                        |
| xml_etree_process       | 76.0 ms                                                      | 55.4 ms: 1.37x faster                                                       |
| async_tree_memoization  | 824 ms                                                       | 608 ms: 1.36x faster                                                        |
| unpack_sequence         | 59.5 ns                                                      | 44.0 ns: 1.35x faster                                                       |
| spectral_norm           | 136 ms                                                       | 101 ms: 1.35x faster                                                        |
| deepcopy_memo           | 48.9 us                                                      | 36.7 us: 1.33x faster                                                       |
| chameleon               | 9.72 ms                                                      | 7.31 ms: 1.33x faster                                                       |
| pprint_pformat          | 2.15 sec                                                     | 1.63 sec: 1.32x faster                                                      |
| pprint_safe_repr        | 1.05 sec                                                     | 794 ms: 1.32x faster                                                        |
| pycparser               | 1.66 sec                                                     | 1.26 sec: 1.32x faster                                                      |
| django_template         | 51.5 ms                                                      | 39.2 ms: 1.31x faster                                                       |
| async_generators        | 422 ms                                                       | 322 ms: 1.31x faster                                                        |
| fannkuch                | 496 ms                                                       | 380 ms: 1.30x faster                                                        |
| regex_compile           | 194 ms                                                       | 149 ms: 1.30x faster                                                        |
| async_tree_cpu_io_mixed | 952 ms                                                       | 742 ms: 1.28x faster                                                        |
| thrift                  | 1.16 ms                                                      | 908 us: 1.28x faster                                                        |
| logging_simple          | 8.90 us                                                      | 6.95 us: 1.28x faster                                                       |
| scimark_fft             | 359 ms                                                       | 283 ms: 1.27x faster                                                        |
| genshi_text             | 31.5 ms                                                      | 24.8 ms: 1.27x faster                                                       |
| logging_format          | 9.57 us                                                      | 7.66 us: 1.25x faster                                                       |
| json_loads              | 30.0 us                                                      | 24.0 us: 1.25x faster                                                       |
| mypy2                   | 466 ms                                                       | 380 ms: 1.23x faster                                                        |
| docutils                | 3.40 sec                                                     | 2.78 sec: 1.23x faster                                                      |
| 2to3                    | 350 ms                                                       | 286 ms: 1.22x faster                                                        |
| deepcopy_reduce         | 4.03 us                                                      | 3.33 us: 1.21x faster                                                       |
| genshi_xml              | 64.7 ms                                                      | 53.7 ms: 1.21x faster                                                       |
| deepcopy                | 454 us                                                       | 379 us: 1.20x faster                                                        |
| nqueens                 | 112 ms                                                       | 94.0 ms: 1.20x faster                                                       |
| dulwich_log             | 80.1 ms                                                      | 67.5 ms: 1.19x faster                                                       |
| sqlglot_optimize        | 70.3 ms                                                      | 59.3 ms: 1.19x faster                                                       |
| xml_etree_generate      | 94.6 ms                                                      | 80.3 ms: 1.18x faster                                                       |
| sqlglot_normalize       | 144 ms                                                       | 123 ms: 1.18x faster                                                        |
| regex_v8                | 26.6 ms                                                      | 23.0 ms: 1.16x faster                                                       |
| sqlite_synth            | 2.97 us                                                      | 2.56 us: 1.16x faster                                                       |
| bench_thread_pool       | 1.14 ms                                                      | 987 us: 1.15x faster                                                        |
| create_gc_cycles        | 1.82 ms                                                      | 1.58 ms: 1.15x faster                                                       |
| json                    | 5.96 ms                                                      | 5.24 ms: 1.14x faster                                                       |
| dask                    | 463 ms                                                       | 408 ms: 1.13x faster                                                        |
| regex_dna               | 259 ms                                                       | 229 ms: 1.13x faster                                                        |
| xml_etree_parse         | 162 ms                                                       | 144 ms: 1.12x faster                                                        |
| pathlib                 | 21.7 ms                                                      | 19.4 ms: 1.12x faster                                                       |
| sympy_expand            | 599 ms                                                       | 537 ms: 1.12x faster                                                        |
| pickle_list             | 4.11 us                                                      | 3.70 us: 1.11x faster                                                       |
| mdp                     | 3.03 sec                                                     | 2.75 sec: 1.10x faster                                                      |
| sympy_integrate         | 28.1 ms                                                      | 25.6 ms: 1.10x faster                                                       |
| coroutines              | 30.4 ms                                                      | 27.9 ms: 1.09x faster                                                       |
| pidigits                | 271 ms                                                       | 252 ms: 1.07x faster                                                        |
| sympy_str               | 358 ms                                                       | 335 ms: 1.07x faster                                                        |
| telco                   | 7.14 ms                                                      | 6.70 ms: 1.07x faster                                                       |
| python_startup          | 11.5 ms                                                      | 10.8 ms: 1.07x faster                                                       |
| unpickle                | 14.2 us                                                      | 13.3 us: 1.06x faster                                                       |
| xml_etree_iterparse     | 110 ms                                                       | 104 ms: 1.06x faster                                                        |
| meteor_contest          | 137 ms                                                       | 131 ms: 1.04x faster                                                        |
| sympy_sum               | 193 ms                                                       | 186 ms: 1.04x faster                                                        |
| pickle                  | 9.94 us                                                      | 9.71 us: 1.02x faster                                                       |
| comprehensions          | 26.9 us                                                      | 27.1 us: 1.00x slower                                                       |
| gc_traversal            | 3.45 ms                                                      | 3.54 ms: 1.03x slower                                                       |
| pickle_dict             | 30.0 us                                                      | 31.1 us: 1.04x slower                                                       |
| generators              | 58.0 ms                                                      | 60.5 ms: 1.04x slower                                                       |
| python_startup_no_site  | 7.32 ms                                                      | 7.87 ms: 1.07x slower                                                       |
| regex_effbot            | 2.99 ms                                                      | 3.43 ms: 1.15x slower                                                       |
| coverage                | 64.0 ms                                                      | 89.3 ms: 1.40x slower                                                       |
| Geometric mean          | (ref)                                                        | 1.25x faster                                                                |

Benchmark hidden because not significant (1): unpickle_list
Ignored benchmarks (11) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, tornado_http, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.22x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.19x
