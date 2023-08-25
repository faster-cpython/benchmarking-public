
# Results vs. 3.10.4

- fork: python
- ref: 010576c6ea7e687cf2cb
- machine: windows-amd64
- commit hash: 010576c
- commit date: 2023-01-13
- overall geometric mean: 1.21x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.15x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230113-pythonperf1-amd64-python-010576c6ea7e687cf2cb-3.12.0a4+-010576c |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 237 ms                                                      | 202 ms: 1.18x faster                                                        |
| chameleon      | 5.92 ms                                                     | 4.60 ms: 1.29x faster                                                       |
| docutils       | 1.89 sec                                                    | 1.52 sec: 1.24x faster                                                      |
| html5lib       | 46.5 ms                                                     | 33.5 ms: 1.39x faster                                                       |
| tornado_http   | 109 ms                                                      | 91.2 ms: 1.20x faster                                                       |
| Geometric mean | (ref)                                                       | 1.26x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230113-pythonperf1-amd64-python-010576c6ea7e687cf2cb-3.12.0a4+-010576c |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 60.2 ms                                                     | 49.3 ms: 1.22x faster                                                       |
| nbody          | 69.3 ms                                                     | 61.2 ms: 1.13x faster                                                       |
| pidigits       | 145 ms                                                      | 151 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                       | 1.10x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230113-pythonperf1-amd64-python-010576c6ea7e687cf2cb-3.12.0a4+-010576c |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 103 ms                                                      | 80.4 ms: 1.29x faster                                                       |
| regex_dna      | 132 ms                                                      | 122 ms: 1.08x faster                                                        |
| regex_v8       | 15.0 ms                                                     | 14.0 ms: 1.07x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.60 ms: 1.04x faster                                                       |
| Geometric mean | (ref)                                                       | 1.12x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230113-pythonperf1-amd64-python-010576c6ea7e687cf2cb-3.12.0a4+-010576c |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 8.50 ms                                                     | 5.26 ms: 1.62x faster                                                       |
| pickle_pure_python   | 257 us                                                      | 176 us: 1.46x faster                                                        |
| unpickle_pure_python | 171 us                                                      | 122 us: 1.41x faster                                                        |
| xml_etree_process    | 43.4 ms                                                     | 34.1 ms: 1.27x faster                                                       |
| xml_etree_parse      | 102 ms                                                      | 90.3 ms: 1.13x faster                                                       |
| xml_etree_generate   | 54.5 ms                                                     | 49.5 ms: 1.10x faster                                                       |
| unpickle             | 9.17 us                                                     | 8.48 us: 1.08x faster                                                       |
| unpickle_list        | 2.81 us                                                     | 2.65 us: 1.06x faster                                                       |
| json_loads           | 14.2 us                                                     | 14.4 us: 1.02x slower                                                       |
| pickle               | 6.80 us                                                     | 7.18 us: 1.06x slower                                                       |
| pickle_list          | 2.59 us                                                     | 2.79 us: 1.08x slower                                                       |
| pickle_dict          | 16.9 us                                                     | 19.3 us: 1.14x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.12x faster                                                                |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230113-pythonperf1-amd64-python-010576c6ea7e687cf2cb-3.12.0a4+-010576c |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.0 ms                                                     | 18.6 ms: 1.07x faster                                                       |
| python_startup_no_site | 15.5 ms                                                     | 15.7 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.03x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230113-pythonperf1-amd64-python-010576c6ea7e687cf2cb-3.12.0a4+-010576c |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 8.80 ms                                                     | 6.07 ms: 1.45x faster                                                       |
| genshi_text     | 19.0 ms                                                     | 13.8 ms: 1.38x faster                                                       |
| django_template | 28.2 ms                                                     | 20.7 ms: 1.36x faster                                                       |
| genshi_xml      | 40.5 ms                                                     | 30.8 ms: 1.32x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.38x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230113-pythonperf1-amd64-python-010576c6ea7e687cf2cb-3.12.0a4+-010576c |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deltablue               | 4.17 ms                                                     | 1.96 ms: 2.13x faster                                                       |
| richards                | 41.2 ms                                                     | 24.1 ms: 1.71x faster                                                       |
| logging_silent          | 96.4 ns                                                     | 56.7 ns: 1.70x faster                                                       |
| go                      | 136 ms                                                      | 83.6 ms: 1.63x faster                                                       |
| json_dumps              | 8.50 ms                                                     | 5.26 ms: 1.62x faster                                                       |
| mypy2                   | 352 ms                                                      | 219 ms: 1.61x faster                                                        |
| scimark_sor             | 105 ms                                                      | 66.0 ms: 1.59x faster                                                       |
| raytrace                | 271 ms                                                      | 177 ms: 1.53x faster                                                        |
| scimark_lu              | 85.4 ms                                                     | 57.3 ms: 1.49x faster                                                       |
| hexiom                  | 5.52 ms                                                     | 3.73 ms: 1.48x faster                                                       |
| asyncio_tcp             | 712 ms                                                      | 484 ms: 1.47x faster                                                        |
| pickle_pure_python      | 257 us                                                      | 176 us: 1.46x faster                                                        |
| mako                    | 8.80 ms                                                     | 6.07 ms: 1.45x faster                                                       |
| scimark_monte_carlo     | 55.9 ms                                                     | 39.0 ms: 1.43x faster                                                       |
| unpack_sequence         | 37.8 ns                                                     | 26.4 ns: 1.43x faster                                                       |
| unpickle_pure_python    | 171 us                                                      | 122 us: 1.41x faster                                                        |
| pyflate                 | 387 ms                                                      | 276 ms: 1.40x faster                                                        |
| sqlglot_parse           | 1.22 ms                                                     | 874 us: 1.40x faster                                                        |
| html5lib                | 46.5 ms                                                     | 33.5 ms: 1.39x faster                                                       |
| deepcopy_memo           | 28.5 us                                                     | 20.7 us: 1.38x faster                                                       |
| sqlglot_transpile       | 1.46 ms                                                     | 1.06 ms: 1.38x faster                                                       |
| genshi_text             | 19.0 ms                                                     | 13.8 ms: 1.38x faster                                                       |
| async_tree_memoization  | 497 ms                                                      | 363 ms: 1.37x faster                                                        |
| async_tree_io           | 1.07 sec                                                    | 781 ms: 1.36x faster                                                        |
| django_template         | 28.2 ms                                                     | 20.7 ms: 1.36x faster                                                       |
| pycparser               | 868 ms                                                      | 640 ms: 1.36x faster                                                        |
| crypto_pyaes            | 62.3 ms                                                     | 46.0 ms: 1.36x faster                                                       |
| chaos                   | 58.9 ms                                                     | 43.8 ms: 1.35x faster                                                       |
| genshi_xml              | 40.5 ms                                                     | 30.8 ms: 1.32x faster                                                       |
| async_tree_none         | 420 ms                                                      | 320 ms: 1.31x faster                                                        |
| thrift                  | 615 us                                                      | 475 us: 1.29x faster                                                        |
| chameleon               | 5.92 ms                                                     | 4.60 ms: 1.29x faster                                                       |
| regex_compile           | 103 ms                                                      | 80.4 ms: 1.29x faster                                                       |
| pprint_safe_repr        | 589 ms                                                      | 459 ms: 1.28x faster                                                        |
| async_generators        | 224 ms                                                      | 175 ms: 1.28x faster                                                        |
| spectral_norm           | 78.0 ms                                                     | 61.2 ms: 1.27x faster                                                       |
| xml_etree_process       | 43.4 ms                                                     | 34.1 ms: 1.27x faster                                                       |
| pprint_pformat          | 1.21 sec                                                    | 952 ms: 1.27x faster                                                        |
| sqlglot_optimize        | 39.0 ms                                                     | 30.9 ms: 1.26x faster                                                       |
| async_tree_cpu_io_mixed | 609 ms                                                      | 487 ms: 1.25x faster                                                        |
| docutils                | 1.89 sec                                                    | 1.52 sec: 1.24x faster                                                      |
| deepcopy                | 255 us                                                      | 206 us: 1.24x faster                                                        |
| float                   | 60.2 ms                                                     | 49.3 ms: 1.22x faster                                                       |
| tornado_http            | 109 ms                                                      | 91.2 ms: 1.20x faster                                                       |
| nqueens                 | 67.0 ms                                                     | 56.6 ms: 1.18x faster                                                       |
| scimark_sparse_mat_mult | 2.66 ms                                                     | 2.26 ms: 1.18x faster                                                       |
| 2to3                    | 237 ms                                                      | 202 ms: 1.18x faster                                                        |
| dask                    | 305 ms                                                      | 260 ms: 1.17x faster                                                        |
| sqlglot_normalize       | 202 ms                                                      | 173 ms: 1.17x faster                                                        |
| create_gc_cycles        | 782 us                                                      | 669 us: 1.17x faster                                                        |
| deepcopy_reduce         | 2.16 us                                                     | 1.86 us: 1.16x faster                                                       |
| sympy_integrate         | 14.8 ms                                                     | 12.9 ms: 1.15x faster                                                       |
| scimark_fft             | 193 ms                                                      | 169 ms: 1.14x faster                                                        |
| sympy_expand            | 315 ms                                                      | 276 ms: 1.14x faster                                                        |
| dulwich_log             | 47.6 ms                                                     | 41.9 ms: 1.13x faster                                                       |
| nbody                   | 69.3 ms                                                     | 61.2 ms: 1.13x faster                                                       |
| fannkuch                | 258 ms                                                      | 228 ms: 1.13x faster                                                        |
| xml_etree_parse         | 102 ms                                                      | 90.3 ms: 1.13x faster                                                       |
| bench_thread_pool       | 946 us                                                      | 841 us: 1.13x faster                                                        |
| coroutines              | 15.9 ms                                                     | 14.3 ms: 1.11x faster                                                       |
| xml_etree_generate      | 54.5 ms                                                     | 49.5 ms: 1.10x faster                                                       |
| mdp                     | 1.71 sec                                                    | 1.56 sec: 1.10x faster                                                      |
| sympy_sum               | 104 ms                                                      | 94.9 ms: 1.10x faster                                                       |
| sympy_str               | 188 ms                                                      | 173 ms: 1.09x faster                                                        |
| json                    | 3.05 ms                                                     | 2.81 ms: 1.08x faster                                                       |
| regex_dna               | 132 ms                                                      | 122 ms: 1.08x faster                                                        |
| unpickle                | 9.17 us                                                     | 8.48 us: 1.08x faster                                                       |
| regex_v8                | 15.0 ms                                                     | 14.0 ms: 1.07x faster                                                       |
| python_startup          | 20.0 ms                                                     | 18.6 ms: 1.07x faster                                                       |
| unpickle_list           | 2.81 us                                                     | 2.65 us: 1.06x faster                                                       |
| logging_format          | 6.66 us                                                     | 6.38 us: 1.04x faster                                                       |
| comprehensions          | 16.0 us                                                     | 15.3 us: 1.04x faster                                                       |
| regex_effbot            | 1.66 ms                                                     | 1.60 ms: 1.04x faster                                                       |
| pathlib                 | 77.4 ms                                                     | 75.0 ms: 1.03x faster                                                       |
| telco                   | 3.78 ms                                                     | 3.69 ms: 1.02x faster                                                       |
| sqlite_synth            | 1.84 us                                                     | 1.80 us: 1.02x faster                                                       |
| logging_simple          | 6.20 us                                                     | 6.12 us: 1.01x faster                                                       |
| meteor_contest          | 72.5 ms                                                     | 71.9 ms: 1.01x faster                                                       |
| python_startup_no_site  | 15.5 ms                                                     | 15.7 ms: 1.01x slower                                                       |
| json_loads              | 14.2 us                                                     | 14.4 us: 1.02x slower                                                       |
| bench_mp_pool           | 60.7 ms                                                     | 62.7 ms: 1.03x slower                                                       |
| pidigits                | 145 ms                                                      | 151 ms: 1.04x slower                                                        |
| pickle                  | 6.80 us                                                     | 7.18 us: 1.06x slower                                                       |
| pickle_list             | 2.59 us                                                     | 2.79 us: 1.08x slower                                                       |
| generators              | 31.6 ms                                                     | 34.6 ms: 1.10x slower                                                       |
| gc_traversal            | 1.34 ms                                                     | 1.51 ms: 1.12x slower                                                       |
| pickle_dict             | 16.9 us                                                     | 19.3 us: 1.14x slower                                                       |
| coverage                | 40.0 ms                                                     | 53.2 ms: 1.33x slower                                                       |
| Geometric mean          | (ref)                                                       | 1.21x faster                                                                |

Benchmark hidden because not significant (1): xml_etree_iterparse
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.18x
- 95% likely to have a speedup of 1.17x
- 99% likely to have a speedup of 1.15x
