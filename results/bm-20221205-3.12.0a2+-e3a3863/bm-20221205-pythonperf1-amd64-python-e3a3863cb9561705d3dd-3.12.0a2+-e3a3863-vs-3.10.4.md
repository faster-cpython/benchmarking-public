
# Results vs. 3.10.4

- fork: python
- ref: e3a3863cb9561705d3dd
- machine: windows-amd64
- commit hash: e3a3863
- commit date: 2022-12-05
- overall geometric mean: 1.20x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.14x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20221205-pythonperf1-amd64-python-e3a3863cb9561705d3dd-3.12.0a2+-e3a3863 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 237 ms                                                      | 199 ms: 1.19x faster                                                        |
| chameleon      | 5.92 ms                                                     | 4.68 ms: 1.27x faster                                                       |
| docutils       | 1.89 sec                                                    | 1.55 sec: 1.22x faster                                                      |
| html5lib       | 46.5 ms                                                     | 34.5 ms: 1.35x faster                                                       |
| tornado_http   | 109 ms                                                      | 90.7 ms: 1.20x faster                                                       |
| Geometric mean | (ref)                                                       | 1.24x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20221205-pythonperf1-amd64-python-e3a3863cb9561705d3dd-3.12.0a2+-e3a3863 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 60.2 ms                                                     | 49.8 ms: 1.21x faster                                                       |
| nbody          | 69.3 ms                                                     | 61.5 ms: 1.13x faster                                                       |
| pidigits       | 145 ms                                                      | 147 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                       | 1.10x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20221205-pythonperf1-amd64-python-e3a3863cb9561705d3dd-3.12.0a2+-e3a3863 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 103 ms                                                      | 81.9 ms: 1.26x faster                                                       |
| regex_v8       | 15.0 ms                                                     | 13.8 ms: 1.09x faster                                                       |
| regex_dna      | 132 ms                                                      | 121 ms: 1.09x faster                                                        |
| regex_effbot   | 1.66 ms                                                     | 1.60 ms: 1.04x faster                                                       |
| Geometric mean | (ref)                                                       | 1.12x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20221205-pythonperf1-amd64-python-e3a3863cb9561705d3dd-3.12.0a2+-e3a3863 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 8.50 ms                                                     | 5.16 ms: 1.65x faster                                                       |
| pickle_pure_python   | 257 us                                                      | 172 us: 1.49x faster                                                        |
| unpickle_pure_python | 171 us                                                      | 124 us: 1.38x faster                                                        |
| xml_etree_process    | 43.4 ms                                                     | 34.3 ms: 1.27x faster                                                       |
| unpickle             | 9.17 us                                                     | 7.98 us: 1.15x faster                                                       |
| xml_etree_parse      | 102 ms                                                      | 89.7 ms: 1.13x faster                                                       |
| json_loads           | 14.2 us                                                     | 12.9 us: 1.10x faster                                                       |
| unpickle_list        | 2.81 us                                                     | 2.59 us: 1.09x faster                                                       |
| xml_etree_generate   | 54.5 ms                                                     | 50.6 ms: 1.08x faster                                                       |
| pickle               | 6.80 us                                                     | 7.11 us: 1.04x slower                                                       |
| pickle_list          | 2.59 us                                                     | 2.84 us: 1.10x slower                                                       |
| pickle_dict          | 16.9 us                                                     | 18.9 us: 1.12x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.14x faster                                                                |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20221205-pythonperf1-amd64-python-e3a3863cb9561705d3dd-3.12.0a2+-e3a3863 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.0 ms                                                     | 18.7 ms: 1.07x faster                                                       |
| python_startup_no_site | 15.5 ms                                                     | 15.9 ms: 1.03x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.02x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20221205-pythonperf1-amd64-python-e3a3863cb9561705d3dd-3.12.0a2+-e3a3863 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 8.80 ms                                                     | 6.20 ms: 1.42x faster                                                       |
| genshi_text     | 19.0 ms                                                     | 14.4 ms: 1.32x faster                                                       |
| django_template | 28.2 ms                                                     | 21.8 ms: 1.29x faster                                                       |
| genshi_xml      | 40.5 ms                                                     | 32.1 ms: 1.26x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.32x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20221205-pythonperf1-amd64-python-e3a3863cb9561705d3dd-3.12.0a2+-e3a3863 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deltablue               | 4.17 ms                                                     | 2.07 ms: 2.01x faster                                                       |
| logging_silent          | 96.4 ns                                                     | 55.3 ns: 1.74x faster                                                       |
| go                      | 136 ms                                                      | 82.2 ms: 1.66x faster                                                       |
| json_dumps              | 8.50 ms                                                     | 5.16 ms: 1.65x faster                                                       |
| richards                | 41.2 ms                                                     | 25.3 ms: 1.63x faster                                                       |
| mypy2                   | 352 ms                                                      | 218 ms: 1.62x faster                                                        |
| scimark_sor             | 105 ms                                                      | 67.8 ms: 1.55x faster                                                       |
| scimark_lu              | 85.4 ms                                                     | 57.2 ms: 1.49x faster                                                       |
| pickle_pure_python      | 257 us                                                      | 172 us: 1.49x faster                                                        |
| raytrace                | 271 ms                                                      | 182 ms: 1.49x faster                                                        |
| sqlglot_parse           | 1.22 ms                                                     | 835 us: 1.46x faster                                                        |
| pyflate                 | 387 ms                                                      | 267 ms: 1.45x faster                                                        |
| unpack_sequence         | 37.8 ns                                                     | 26.3 ns: 1.44x faster                                                       |
| mako                    | 8.80 ms                                                     | 6.20 ms: 1.42x faster                                                       |
| scimark_monte_carlo     | 55.9 ms                                                     | 39.5 ms: 1.41x faster                                                       |
| sqlglot_transpile       | 1.46 ms                                                     | 1.05 ms: 1.39x faster                                                       |
| hexiom                  | 5.52 ms                                                     | 3.98 ms: 1.39x faster                                                       |
| unpickle_pure_python    | 171 us                                                      | 124 us: 1.38x faster                                                        |
| deepcopy_memo           | 28.5 us                                                     | 20.9 us: 1.36x faster                                                       |
| crypto_pyaes            | 62.3 ms                                                     | 45.8 ms: 1.36x faster                                                       |
| html5lib                | 46.5 ms                                                     | 34.5 ms: 1.35x faster                                                       |
| async_tree_io           | 1.07 sec                                                    | 792 ms: 1.34x faster                                                        |
| genshi_text             | 19.0 ms                                                     | 14.4 ms: 1.32x faster                                                       |
| thrift                  | 615 us                                                      | 465 us: 1.32x faster                                                        |
| chaos                   | 58.9 ms                                                     | 44.8 ms: 1.31x faster                                                       |
| pycparser               | 868 ms                                                      | 662 ms: 1.31x faster                                                        |
| async_tree_memoization  | 497 ms                                                      | 381 ms: 1.30x faster                                                        |
| django_template         | 28.2 ms                                                     | 21.8 ms: 1.29x faster                                                       |
| pprint_pformat          | 1.21 sec                                                    | 934 ms: 1.29x faster                                                        |
| spectral_norm           | 78.0 ms                                                     | 60.5 ms: 1.29x faster                                                       |
| async_tree_none         | 420 ms                                                      | 327 ms: 1.28x faster                                                        |
| xml_etree_process       | 43.4 ms                                                     | 34.3 ms: 1.27x faster                                                       |
| chameleon               | 5.92 ms                                                     | 4.68 ms: 1.27x faster                                                       |
| regex_compile           | 103 ms                                                      | 81.9 ms: 1.26x faster                                                       |
| genshi_xml              | 40.5 ms                                                     | 32.1 ms: 1.26x faster                                                       |
| pprint_safe_repr        | 589 ms                                                      | 467 ms: 1.26x faster                                                        |
| async_generators        | 224 ms                                                      | 181 ms: 1.24x faster                                                        |
| async_tree_cpu_io_mixed | 609 ms                                                      | 495 ms: 1.23x faster                                                        |
| docutils                | 1.89 sec                                                    | 1.55 sec: 1.22x faster                                                      |
| sqlglot_optimize        | 39.0 ms                                                     | 32.0 ms: 1.22x faster                                                       |
| float                   | 60.2 ms                                                     | 49.8 ms: 1.21x faster                                                       |
| tornado_http            | 109 ms                                                      | 90.7 ms: 1.20x faster                                                       |
| fannkuch                | 258 ms                                                      | 215 ms: 1.20x faster                                                        |
| deepcopy                | 255 us                                                      | 213 us: 1.20x faster                                                        |
| 2to3                    | 237 ms                                                      | 199 ms: 1.19x faster                                                        |
| deepcopy_reduce         | 2.16 us                                                     | 1.85 us: 1.17x faster                                                       |
| scimark_sparse_mat_mult | 2.66 ms                                                     | 2.29 ms: 1.16x faster                                                       |
| dask                    | 305 ms                                                      | 264 ms: 1.15x faster                                                        |
| sqlglot_normalize       | 202 ms                                                      | 176 ms: 1.15x faster                                                        |
| unpickle                | 9.17 us                                                     | 7.98 us: 1.15x faster                                                       |
| sympy_integrate         | 14.8 ms                                                     | 12.9 ms: 1.15x faster                                                       |
| create_gc_cycles        | 782 us                                                      | 682 us: 1.15x faster                                                        |
| xml_etree_parse         | 102 ms                                                      | 89.7 ms: 1.13x faster                                                       |
| sympy_expand            | 315 ms                                                      | 278 ms: 1.13x faster                                                        |
| nbody                   | 69.3 ms                                                     | 61.5 ms: 1.13x faster                                                       |
| scimark_fft             | 193 ms                                                      | 171 ms: 1.13x faster                                                        |
| json                    | 3.05 ms                                                     | 2.72 ms: 1.12x faster                                                       |
| dulwich_log             | 47.6 ms                                                     | 42.4 ms: 1.12x faster                                                       |
| nqueens                 | 67.0 ms                                                     | 59.9 ms: 1.12x faster                                                       |
| bench_thread_pool       | 946 us                                                      | 848 us: 1.12x faster                                                        |
| json_loads              | 14.2 us                                                     | 12.9 us: 1.10x faster                                                       |
| regex_v8                | 15.0 ms                                                     | 13.8 ms: 1.09x faster                                                       |
| regex_dna               | 132 ms                                                      | 121 ms: 1.09x faster                                                        |
| unpickle_list           | 2.81 us                                                     | 2.59 us: 1.09x faster                                                       |
| xml_etree_generate      | 54.5 ms                                                     | 50.6 ms: 1.08x faster                                                       |
| mdp                     | 1.71 sec                                                    | 1.59 sec: 1.07x faster                                                      |
| python_startup          | 20.0 ms                                                     | 18.7 ms: 1.07x faster                                                       |
| coroutines              | 15.9 ms                                                     | 15.0 ms: 1.06x faster                                                       |
| sympy_str               | 188 ms                                                      | 178 ms: 1.06x faster                                                        |
| comprehensions          | 16.0 us                                                     | 15.3 us: 1.05x faster                                                       |
| sympy_sum               | 104 ms                                                      | 99.6 ms: 1.05x faster                                                       |
| regex_effbot            | 1.66 ms                                                     | 1.60 ms: 1.04x faster                                                       |
| sqlite_synth            | 1.84 us                                                     | 1.78 us: 1.03x faster                                                       |
| meteor_contest          | 72.5 ms                                                     | 70.4 ms: 1.03x faster                                                       |
| pathlib                 | 77.4 ms                                                     | 75.1 ms: 1.03x faster                                                       |
| logging_simple          | 6.20 us                                                     | 6.12 us: 1.01x faster                                                       |
| telco                   | 3.78 ms                                                     | 3.75 ms: 1.01x faster                                                       |
| pidigits                | 145 ms                                                      | 147 ms: 1.01x slower                                                        |
| python_startup_no_site  | 15.5 ms                                                     | 15.9 ms: 1.03x slower                                                       |
| pickle                  | 6.80 us                                                     | 7.11 us: 1.04x slower                                                       |
| bench_mp_pool           | 60.7 ms                                                     | 63.8 ms: 1.05x slower                                                       |
| asyncio_tcp             | 712 ms                                                      | 758 ms: 1.06x slower                                                        |
| pickle_list             | 2.59 us                                                     | 2.84 us: 1.10x slower                                                       |
| gc_traversal            | 1.34 ms                                                     | 1.49 ms: 1.11x slower                                                       |
| pickle_dict             | 16.9 us                                                     | 18.9 us: 1.12x slower                                                       |
| generators              | 31.6 ms                                                     | 36.3 ms: 1.15x slower                                                       |
| coverage                | 40.0 ms                                                     | 52.8 ms: 1.32x slower                                                       |
| Geometric mean          | (ref)                                                       | 1.20x faster                                                                |

Benchmark hidden because not significant (2): xml_etree_iterparse, logging_format
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.16x
- 95% likely to have a speedup of 1.15x
- 99% likely to have a speedup of 1.14x
