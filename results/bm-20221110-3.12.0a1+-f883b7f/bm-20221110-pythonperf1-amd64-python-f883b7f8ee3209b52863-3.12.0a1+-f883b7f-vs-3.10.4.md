
# Results vs. 3.10.4

- fork: python
- ref: f883b7f8ee3209b52863
- machine: windows-amd64
- commit hash: f883b7f
- commit date: 2022-11-10
- overall geometric mean: 1.15x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.11x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20221110-pythonperf1-amd64-python-f883b7f8ee3209b52863-3.12.0a1+-f883b7f |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 237 ms                                                      | 200 ms: 1.19x faster                                                        |
| chameleon      | 5.92 ms                                                     | 4.97 ms: 1.19x faster                                                       |
| docutils       | 1.89 sec                                                    | 1.59 sec: 1.19x faster                                                      |
| html5lib       | 46.5 ms                                                     | 36.2 ms: 1.28x faster                                                       |
| tornado_http   | 109 ms                                                      | 93.2 ms: 1.17x faster                                                       |
| Geometric mean | (ref)                                                       | 1.20x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20221110-pythonperf1-amd64-python-f883b7f8ee3209b52863-3.12.0a1+-f883b7f |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 60.2 ms                                                     | 52.3 ms: 1.15x faster                                                       |
| nbody          | 69.3 ms                                                     | 62.7 ms: 1.11x faster                                                       |
| pidigits       | 145 ms                                                      | 150 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                       | 1.07x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20221110-pythonperf1-amd64-python-f883b7f8ee3209b52863-3.12.0a1+-f883b7f |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 103 ms                                                      | 87.2 ms: 1.19x faster                                                       |
| regex_dna      | 132 ms                                                      | 122 ms: 1.08x faster                                                        |
| regex_v8       | 15.0 ms                                                     | 14.0 ms: 1.07x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.60 ms: 1.04x faster                                                       |
| Geometric mean | (ref)                                                       | 1.09x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20221110-pythonperf1-amd64-python-f883b7f8ee3209b52863-3.12.0a1+-f883b7f |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 8.50 ms                                                     | 5.48 ms: 1.55x faster                                                       |
| pickle_pure_python   | 257 us                                                      | 190 us: 1.35x faster                                                        |
| xml_etree_process    | 43.4 ms                                                     | 36.6 ms: 1.19x faster                                                       |
| unpickle_pure_python | 171 us                                                      | 148 us: 1.15x faster                                                        |
| unpickle             | 9.17 us                                                     | 8.06 us: 1.14x faster                                                       |
| xml_etree_parse      | 102 ms                                                      | 90.9 ms: 1.12x faster                                                       |
| unpickle_list        | 2.81 us                                                     | 2.60 us: 1.08x faster                                                       |
| json_loads           | 14.2 us                                                     | 13.1 us: 1.08x faster                                                       |
| xml_etree_generate   | 54.5 ms                                                     | 52.2 ms: 1.04x faster                                                       |
| pickle               | 6.80 us                                                     | 7.14 us: 1.05x slower                                                       |
| pickle_list          | 2.59 us                                                     | 2.82 us: 1.09x slower                                                       |
| pickle_dict          | 16.9 us                                                     | 19.1 us: 1.13x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.10x faster                                                                |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20221110-pythonperf1-amd64-python-f883b7f8ee3209b52863-3.12.0a1+-f883b7f |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.0 ms                                                     | 18.9 ms: 1.06x faster                                                       |
| python_startup_no_site | 15.5 ms                                                     | 15.8 ms: 1.02x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.02x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20221110-pythonperf1-amd64-python-f883b7f8ee3209b52863-3.12.0a1+-f883b7f |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 8.80 ms                                                     | 6.58 ms: 1.34x faster                                                       |
| django_template | 28.2 ms                                                     | 22.1 ms: 1.28x faster                                                       |
| genshi_text     | 19.0 ms                                                     | 16.3 ms: 1.17x faster                                                       |
| genshi_xml      | 40.5 ms                                                     | 35.9 ms: 1.13x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.23x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20221110-pythonperf1-amd64-python-f883b7f8ee3209b52863-3.12.0a1+-f883b7f |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deltablue               | 4.17 ms                                                     | 2.37 ms: 1.76x faster                                                       |
| mypy2                   | 352 ms                                                      | 225 ms: 1.57x faster                                                        |
| json_dumps              | 8.50 ms                                                     | 5.48 ms: 1.55x faster                                                       |
| richards                | 41.2 ms                                                     | 26.8 ms: 1.53x faster                                                       |
| go                      | 136 ms                                                      | 89.7 ms: 1.52x faster                                                       |
| logging_silent          | 96.4 ns                                                     | 64.1 ns: 1.50x faster                                                       |
| raytrace                | 271 ms                                                      | 190 ms: 1.43x faster                                                        |
| scimark_sor             | 105 ms                                                      | 73.7 ms: 1.42x faster                                                       |
| crypto_pyaes            | 62.3 ms                                                     | 45.3 ms: 1.38x faster                                                       |
| scimark_lu              | 85.4 ms                                                     | 62.4 ms: 1.37x faster                                                       |
| async_tree_io           | 1.07 sec                                                    | 782 ms: 1.36x faster                                                        |
| pickle_pure_python      | 257 us                                                      | 190 us: 1.35x faster                                                        |
| scimark_monte_carlo     | 55.9 ms                                                     | 41.3 ms: 1.35x faster                                                       |
| sqlglot_transpile       | 1.46 ms                                                     | 1.09 ms: 1.34x faster                                                       |
| mako                    | 8.80 ms                                                     | 6.58 ms: 1.34x faster                                                       |
| pyflate                 | 387 ms                                                      | 290 ms: 1.33x faster                                                        |
| sqlglot_parse           | 1.22 ms                                                     | 924 us: 1.32x faster                                                        |
| pycparser               | 868 ms                                                      | 669 ms: 1.30x faster                                                        |
| chaos                   | 58.9 ms                                                     | 45.4 ms: 1.30x faster                                                       |
| thrift                  | 615 us                                                      | 479 us: 1.28x faster                                                        |
| html5lib                | 46.5 ms                                                     | 36.2 ms: 1.28x faster                                                       |
| async_tree_memoization  | 497 ms                                                      | 389 ms: 1.28x faster                                                        |
| django_template         | 28.2 ms                                                     | 22.1 ms: 1.28x faster                                                       |
| async_tree_none         | 420 ms                                                      | 330 ms: 1.27x faster                                                        |
| hexiom                  | 5.52 ms                                                     | 4.34 ms: 1.27x faster                                                       |
| async_generators        | 224 ms                                                      | 177 ms: 1.26x faster                                                        |
| pprint_safe_repr        | 589 ms                                                      | 485 ms: 1.21x faster                                                        |
| async_tree_cpu_io_mixed | 609 ms                                                      | 510 ms: 1.20x faster                                                        |
| pprint_pformat          | 1.21 sec                                                    | 1.01 sec: 1.19x faster                                                      |
| sqlglot_optimize        | 39.0 ms                                                     | 32.6 ms: 1.19x faster                                                       |
| chameleon               | 5.92 ms                                                     | 4.97 ms: 1.19x faster                                                       |
| docutils                | 1.89 sec                                                    | 1.59 sec: 1.19x faster                                                      |
| xml_etree_process       | 43.4 ms                                                     | 36.6 ms: 1.19x faster                                                       |
| 2to3                    | 237 ms                                                      | 200 ms: 1.19x faster                                                        |
| regex_compile           | 103 ms                                                      | 87.2 ms: 1.19x faster                                                       |
| genshi_text             | 19.0 ms                                                     | 16.3 ms: 1.17x faster                                                       |
| tornado_http            | 109 ms                                                      | 93.2 ms: 1.17x faster                                                       |
| unpack_sequence         | 37.8 ns                                                     | 32.4 ns: 1.17x faster                                                       |
| deepcopy_memo           | 28.5 us                                                     | 24.7 us: 1.16x faster                                                       |
| spectral_norm           | 78.0 ms                                                     | 67.5 ms: 1.16x faster                                                       |
| unpickle_pure_python    | 171 us                                                      | 148 us: 1.15x faster                                                        |
| float                   | 60.2 ms                                                     | 52.3 ms: 1.15x faster                                                       |
| unpickle                | 9.17 us                                                     | 8.06 us: 1.14x faster                                                       |
| create_gc_cycles        | 782 us                                                      | 688 us: 1.14x faster                                                        |
| dask                    | 305 ms                                                      | 268 ms: 1.14x faster                                                        |
| genshi_xml              | 40.5 ms                                                     | 35.9 ms: 1.13x faster                                                       |
| scimark_sparse_mat_mult | 2.66 ms                                                     | 2.36 ms: 1.13x faster                                                       |
| json                    | 3.05 ms                                                     | 2.70 ms: 1.13x faster                                                       |
| scimark_fft             | 193 ms                                                      | 172 ms: 1.13x faster                                                        |
| bench_thread_pool       | 946 us                                                      | 843 us: 1.12x faster                                                        |
| xml_etree_parse         | 102 ms                                                      | 90.9 ms: 1.12x faster                                                       |
| sympy_integrate         | 14.8 ms                                                     | 13.3 ms: 1.12x faster                                                       |
| nbody                   | 69.3 ms                                                     | 62.7 ms: 1.11x faster                                                       |
| sympy_expand            | 315 ms                                                      | 285 ms: 1.10x faster                                                        |
| sqlglot_normalize       | 202 ms                                                      | 184 ms: 1.10x faster                                                        |
| coroutines              | 15.9 ms                                                     | 14.5 ms: 1.10x faster                                                       |
| mdp                     | 1.71 sec                                                    | 1.57 sec: 1.09x faster                                                      |
| dulwich_log             | 47.6 ms                                                     | 43.8 ms: 1.09x faster                                                       |
| nqueens                 | 67.0 ms                                                     | 61.8 ms: 1.08x faster                                                       |
| unpickle_list           | 2.81 us                                                     | 2.60 us: 1.08x faster                                                       |
| regex_dna               | 132 ms                                                      | 122 ms: 1.08x faster                                                        |
| json_loads              | 14.2 us                                                     | 13.1 us: 1.08x faster                                                       |
| regex_v8                | 15.0 ms                                                     | 14.0 ms: 1.07x faster                                                       |
| sympy_sum               | 104 ms                                                      | 97.5 ms: 1.07x faster                                                       |
| deepcopy_reduce         | 2.16 us                                                     | 2.03 us: 1.06x faster                                                       |
| python_startup          | 20.0 ms                                                     | 18.9 ms: 1.06x faster                                                       |
| deepcopy                | 255 us                                                      | 241 us: 1.06x faster                                                        |
| pathlib                 | 77.4 ms                                                     | 73.5 ms: 1.05x faster                                                       |
| fannkuch                | 258 ms                                                      | 247 ms: 1.04x faster                                                        |
| xml_etree_generate      | 54.5 ms                                                     | 52.2 ms: 1.04x faster                                                       |
| regex_effbot            | 1.66 ms                                                     | 1.60 ms: 1.04x faster                                                       |
| sympy_str               | 188 ms                                                      | 183 ms: 1.03x faster                                                        |
| meteor_contest          | 72.5 ms                                                     | 70.5 ms: 1.03x faster                                                       |
| sqlite_synth            | 1.84 us                                                     | 1.79 us: 1.03x faster                                                       |
| python_startup_no_site  | 15.5 ms                                                     | 15.8 ms: 1.02x slower                                                       |
| telco                   | 3.78 ms                                                     | 3.86 ms: 1.02x slower                                                       |
| pidigits                | 145 ms                                                      | 150 ms: 1.03x slower                                                        |
| bench_mp_pool           | 60.7 ms                                                     | 63.2 ms: 1.04x slower                                                       |
| pickle                  | 6.80 us                                                     | 7.14 us: 1.05x slower                                                       |
| logging_format          | 6.66 us                                                     | 7.05 us: 1.06x slower                                                       |
| logging_simple          | 6.20 us                                                     | 6.60 us: 1.06x slower                                                       |
| generators              | 31.6 ms                                                     | 33.6 ms: 1.06x slower                                                       |
| pickle_list             | 2.59 us                                                     | 2.82 us: 1.09x slower                                                       |
| gc_traversal            | 1.34 ms                                                     | 1.48 ms: 1.10x slower                                                       |
| pickle_dict             | 16.9 us                                                     | 19.1 us: 1.13x slower                                                       |
| coverage                | 40.0 ms                                                     | 54.2 ms: 1.35x slower                                                       |
| Geometric mean          | (ref)                                                       | 1.15x faster                                                                |

Benchmark hidden because not significant (3): comprehensions, asyncio_tcp, xml_etree_iterparse
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.13x
- 95% likely to have a speedup of 1.12x
- 99% likely to have a speedup of 1.11x
