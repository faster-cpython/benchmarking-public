
# Results vs. 3.10.4

- fork: python
- ref: d8f239d86eb70c31aa4c
- machine: windows-amd64
- commit hash: d8f239d
- commit date: 2022-11-10
- overall geometric mean: 1.15x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.11x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20221110-pythonperf1-amd64-python-d8f239d86eb70c31aa4c-3.12.0a1+-d8f239d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 237 ms                                                      | 203 ms: 1.17x faster                                                        |
| chameleon      | 5.92 ms                                                     | 5.01 ms: 1.18x faster                                                       |
| docutils       | 1.89 sec                                                    | 1.59 sec: 1.19x faster                                                      |
| html5lib       | 46.5 ms                                                     | 34.8 ms: 1.34x faster                                                       |
| tornado_http   | 109 ms                                                      | 93.3 ms: 1.17x faster                                                       |
| Geometric mean | (ref)                                                       | 1.21x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20221110-pythonperf1-amd64-python-d8f239d86eb70c31aa4c-3.12.0a1+-d8f239d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 60.2 ms                                                     | 53.0 ms: 1.13x faster                                                       |
| nbody          | 69.3 ms                                                     | 63.5 ms: 1.09x faster                                                       |
| pidigits       | 145 ms                                                      | 153 ms: 1.05x slower                                                        |
| Geometric mean | (ref)                                                       | 1.06x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20221110-pythonperf1-amd64-python-d8f239d86eb70c31aa4c-3.12.0a1+-d8f239d |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 103 ms                                                      | 85.4 ms: 1.21x faster                                                       |
| regex_v8       | 15.0 ms                                                     | 13.6 ms: 1.10x faster                                                       |
| regex_dna      | 132 ms                                                      | 121 ms: 1.09x faster                                                        |
| regex_effbot   | 1.66 ms                                                     | 1.57 ms: 1.06x faster                                                       |
| Geometric mean | (ref)                                                       | 1.11x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20221110-pythonperf1-amd64-python-d8f239d86eb70c31aa4c-3.12.0a1+-d8f239d |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 8.50 ms                                                     | 5.52 ms: 1.54x faster                                                       |
| pickle_pure_python   | 257 us                                                      | 198 us: 1.30x faster                                                        |
| unpickle_pure_python | 171 us                                                      | 138 us: 1.24x faster                                                        |
| xml_etree_process    | 43.4 ms                                                     | 36.6 ms: 1.19x faster                                                       |
| unpickle             | 9.17 us                                                     | 8.22 us: 1.12x faster                                                       |
| xml_etree_parse      | 102 ms                                                      | 91.7 ms: 1.11x faster                                                       |
| unpickle_list        | 2.81 us                                                     | 2.55 us: 1.10x faster                                                       |
| json_loads           | 14.2 us                                                     | 13.2 us: 1.07x faster                                                       |
| xml_etree_generate   | 54.5 ms                                                     | 51.6 ms: 1.06x faster                                                       |
| pickle               | 6.80 us                                                     | 7.20 us: 1.06x slower                                                       |
| pickle_list          | 2.59 us                                                     | 2.88 us: 1.11x slower                                                       |
| pickle_dict          | 16.9 us                                                     | 19.2 us: 1.14x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.10x faster                                                                |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20221110-pythonperf1-amd64-python-d8f239d86eb70c31aa4c-3.12.0a1+-d8f239d |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.0 ms                                                     | 18.7 ms: 1.07x faster                                                       |
| python_startup_no_site | 15.5 ms                                                     | 15.9 ms: 1.02x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.02x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20221110-pythonperf1-amd64-python-d8f239d86eb70c31aa4c-3.12.0a1+-d8f239d |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 8.80 ms                                                     | 6.42 ms: 1.37x faster                                                       |
| django_template | 28.2 ms                                                     | 22.0 ms: 1.28x faster                                                       |
| genshi_text     | 19.0 ms                                                     | 16.1 ms: 1.18x faster                                                       |
| genshi_xml      | 40.5 ms                                                     | 35.5 ms: 1.14x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.24x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20221110-pythonperf1-amd64-python-d8f239d86eb70c31aa4c-3.12.0a1+-d8f239d |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deltablue               | 4.17 ms                                                     | 2.42 ms: 1.73x faster                                                       |
| mypy2                   | 352 ms                                                      | 226 ms: 1.56x faster                                                        |
| json_dumps              | 8.50 ms                                                     | 5.52 ms: 1.54x faster                                                       |
| richards                | 41.2 ms                                                     | 27.6 ms: 1.49x faster                                                       |
| go                      | 136 ms                                                      | 92.1 ms: 1.48x faster                                                       |
| logging_silent          | 96.4 ns                                                     | 65.3 ns: 1.48x faster                                                       |
| raytrace                | 271 ms                                                      | 191 ms: 1.42x faster                                                        |
| scimark_sor             | 105 ms                                                      | 75.1 ms: 1.40x faster                                                       |
| scimark_lu              | 85.4 ms                                                     | 61.5 ms: 1.39x faster                                                       |
| mako                    | 8.80 ms                                                     | 6.42 ms: 1.37x faster                                                       |
| crypto_pyaes            | 62.3 ms                                                     | 45.9 ms: 1.36x faster                                                       |
| async_tree_io           | 1.07 sec                                                    | 788 ms: 1.35x faster                                                        |
| sqlglot_transpile       | 1.46 ms                                                     | 1.09 ms: 1.35x faster                                                       |
| sqlglot_parse           | 1.22 ms                                                     | 907 us: 1.34x faster                                                        |
| pyflate                 | 387 ms                                                      | 289 ms: 1.34x faster                                                        |
| html5lib                | 46.5 ms                                                     | 34.8 ms: 1.34x faster                                                       |
| scimark_monte_carlo     | 55.9 ms                                                     | 42.5 ms: 1.31x faster                                                       |
| pycparser               | 868 ms                                                      | 662 ms: 1.31x faster                                                        |
| pickle_pure_python      | 257 us                                                      | 198 us: 1.30x faster                                                        |
| hexiom                  | 5.52 ms                                                     | 4.30 ms: 1.28x faster                                                       |
| chaos                   | 58.9 ms                                                     | 45.9 ms: 1.28x faster                                                       |
| django_template         | 28.2 ms                                                     | 22.0 ms: 1.28x faster                                                       |
| async_tree_none         | 420 ms                                                      | 330 ms: 1.27x faster                                                        |
| async_generators        | 224 ms                                                      | 176 ms: 1.27x faster                                                        |
| async_tree_memoization  | 497 ms                                                      | 394 ms: 1.26x faster                                                        |
| unpickle_pure_python    | 171 us                                                      | 138 us: 1.24x faster                                                        |
| thrift                  | 615 us                                                      | 505 us: 1.22x faster                                                        |
| deepcopy_memo           | 28.5 us                                                     | 23.4 us: 1.22x faster                                                       |
| pprint_safe_repr        | 589 ms                                                      | 485 ms: 1.21x faster                                                        |
| sqlglot_optimize        | 39.0 ms                                                     | 32.2 ms: 1.21x faster                                                       |
| regex_compile           | 103 ms                                                      | 85.4 ms: 1.21x faster                                                       |
| pprint_pformat          | 1.21 sec                                                    | 1.00 sec: 1.20x faster                                                      |
| async_tree_cpu_io_mixed | 609 ms                                                      | 508 ms: 1.20x faster                                                        |
| docutils                | 1.89 sec                                                    | 1.59 sec: 1.19x faster                                                      |
| xml_etree_process       | 43.4 ms                                                     | 36.6 ms: 1.19x faster                                                       |
| spectral_norm           | 78.0 ms                                                     | 65.8 ms: 1.19x faster                                                       |
| chameleon               | 5.92 ms                                                     | 5.01 ms: 1.18x faster                                                       |
| genshi_text             | 19.0 ms                                                     | 16.1 ms: 1.18x faster                                                       |
| tornado_http            | 109 ms                                                      | 93.3 ms: 1.17x faster                                                       |
| 2to3                    | 237 ms                                                      | 203 ms: 1.17x faster                                                        |
| dask                    | 305 ms                                                      | 261 ms: 1.17x faster                                                        |
| genshi_xml              | 40.5 ms                                                     | 35.5 ms: 1.14x faster                                                       |
| float                   | 60.2 ms                                                     | 53.0 ms: 1.13x faster                                                       |
| scimark_fft             | 193 ms                                                      | 171 ms: 1.13x faster                                                        |
| create_gc_cycles        | 782 us                                                      | 691 us: 1.13x faster                                                        |
| scimark_sparse_mat_mult | 2.66 ms                                                     | 2.35 ms: 1.13x faster                                                       |
| unpickle                | 9.17 us                                                     | 8.22 us: 1.12x faster                                                       |
| sqlglot_normalize       | 202 ms                                                      | 182 ms: 1.11x faster                                                        |
| nqueens                 | 67.0 ms                                                     | 60.4 ms: 1.11x faster                                                       |
| xml_etree_parse         | 102 ms                                                      | 91.7 ms: 1.11x faster                                                       |
| sympy_integrate         | 14.8 ms                                                     | 13.4 ms: 1.11x faster                                                       |
| deepcopy_reduce         | 2.16 us                                                     | 1.95 us: 1.11x faster                                                       |
| json                    | 3.05 ms                                                     | 2.75 ms: 1.11x faster                                                       |
| dulwich_log             | 47.6 ms                                                     | 43.1 ms: 1.11x faster                                                       |
| bench_thread_pool       | 946 us                                                      | 858 us: 1.10x faster                                                        |
| unpickle_list           | 2.81 us                                                     | 2.55 us: 1.10x faster                                                       |
| regex_v8                | 15.0 ms                                                     | 13.6 ms: 1.10x faster                                                       |
| deepcopy                | 255 us                                                      | 232 us: 1.10x faster                                                        |
| coroutines              | 15.9 ms                                                     | 14.5 ms: 1.10x faster                                                       |
| fannkuch                | 258 ms                                                      | 236 ms: 1.09x faster                                                        |
| nbody                   | 69.3 ms                                                     | 63.5 ms: 1.09x faster                                                       |
| regex_dna               | 132 ms                                                      | 121 ms: 1.09x faster                                                        |
| sympy_expand            | 315 ms                                                      | 290 ms: 1.09x faster                                                        |
| mdp                     | 1.71 sec                                                    | 1.59 sec: 1.07x faster                                                      |
| json_loads              | 14.2 us                                                     | 13.2 us: 1.07x faster                                                       |
| python_startup          | 20.0 ms                                                     | 18.7 ms: 1.07x faster                                                       |
| unpack_sequence         | 37.8 ns                                                     | 35.5 ns: 1.07x faster                                                       |
| regex_effbot            | 1.66 ms                                                     | 1.57 ms: 1.06x faster                                                       |
| xml_etree_generate      | 54.5 ms                                                     | 51.6 ms: 1.06x faster                                                       |
| sympy_sum               | 104 ms                                                      | 99.1 ms: 1.05x faster                                                       |
| sympy_str               | 188 ms                                                      | 180 ms: 1.04x faster                                                        |
| pathlib                 | 77.4 ms                                                     | 74.2 ms: 1.04x faster                                                       |
| meteor_contest          | 72.5 ms                                                     | 70.7 ms: 1.03x faster                                                       |
| sqlite_synth            | 1.84 us                                                     | 1.80 us: 1.02x faster                                                       |
| comprehensions          | 16.0 us                                                     | 15.9 us: 1.01x faster                                                       |
| python_startup_no_site  | 15.5 ms                                                     | 15.9 ms: 1.02x slower                                                       |
| logging_format          | 6.66 us                                                     | 6.85 us: 1.03x slower                                                       |
| asyncio_tcp             | 712 ms                                                      | 745 ms: 1.05x slower                                                        |
| logging_simple          | 6.20 us                                                     | 6.49 us: 1.05x slower                                                       |
| bench_mp_pool           | 60.7 ms                                                     | 63.5 ms: 1.05x slower                                                       |
| pidigits                | 145 ms                                                      | 153 ms: 1.05x slower                                                        |
| pickle                  | 6.80 us                                                     | 7.20 us: 1.06x slower                                                       |
| generators              | 31.6 ms                                                     | 34.4 ms: 1.09x slower                                                       |
| gc_traversal            | 1.34 ms                                                     | 1.49 ms: 1.11x slower                                                       |
| pickle_list             | 2.59 us                                                     | 2.88 us: 1.11x slower                                                       |
| pickle_dict             | 16.9 us                                                     | 19.2 us: 1.14x slower                                                       |
| coverage                | 40.0 ms                                                     | 54.9 ms: 1.37x slower                                                       |
| Geometric mean          | (ref)                                                       | 1.15x faster                                                                |

Benchmark hidden because not significant (2): telco, xml_etree_iterparse
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.13x
- 95% likely to have a speedup of 1.12x
- 99% likely to have a speedup of 1.11x
