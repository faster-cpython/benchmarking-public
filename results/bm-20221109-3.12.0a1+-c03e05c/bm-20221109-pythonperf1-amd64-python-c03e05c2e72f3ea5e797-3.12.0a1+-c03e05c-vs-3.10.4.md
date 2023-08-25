
# Results vs. 3.10.4

- fork: python
- ref: c03e05c2e72f3ea5e797
- machine: windows-amd64
- commit hash: c03e05c
- commit date: 2022-11-09
- overall geometric mean: 1.10x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20221109-pythonperf1-amd64-python-c03e05c2e72f3ea5e797-3.12.0a1+-c03e05c |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 237 ms                                                      | 209 ms: 1.13x faster                                                        |
| chameleon      | 5.92 ms                                                     | 5.20 ms: 1.14x faster                                                       |
| docutils       | 1.89 sec                                                    | 1.63 sec: 1.16x faster                                                      |
| html5lib       | 46.5 ms                                                     | 39.9 ms: 1.16x faster                                                       |
| tornado_http   | 109 ms                                                      | 92.5 ms: 1.18x faster                                                       |
| Geometric mean | (ref)                                                       | 1.15x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20221109-pythonperf1-amd64-python-c03e05c2e72f3ea5e797-3.12.0a1+-c03e05c |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 60.2 ms                                                     | 55.8 ms: 1.08x faster                                                       |
| nbody          | 69.3 ms                                                     | 71.3 ms: 1.03x slower                                                       |
| pidigits       | 145 ms                                                      | 151 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                       | 1.00x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20221109-pythonperf1-amd64-python-c03e05c2e72f3ea5e797-3.12.0a1+-c03e05c |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 103 ms                                                      | 89.9 ms: 1.15x faster                                                       |
| regex_v8       | 15.0 ms                                                     | 13.1 ms: 1.15x faster                                                       |
| regex_dna      | 132 ms                                                      | 118 ms: 1.12x faster                                                        |
| regex_effbot   | 1.66 ms                                                     | 1.56 ms: 1.07x faster                                                       |
| Geometric mean | (ref)                                                       | 1.12x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20221109-pythonperf1-amd64-python-c03e05c2e72f3ea5e797-3.12.0a1+-c03e05c |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 8.50 ms                                                     | 5.54 ms: 1.53x faster                                                       |
| pickle_pure_python   | 257 us                                                      | 208 us: 1.24x faster                                                        |
| xml_etree_process    | 43.4 ms                                                     | 37.8 ms: 1.15x faster                                                       |
| xml_etree_parse      | 102 ms                                                      | 89.7 ms: 1.13x faster                                                       |
| unpickle             | 9.17 us                                                     | 8.17 us: 1.12x faster                                                       |
| unpickle_pure_python | 171 us                                                      | 154 us: 1.11x faster                                                        |
| json_loads           | 14.2 us                                                     | 13.0 us: 1.09x faster                                                       |
| xml_etree_generate   | 54.5 ms                                                     | 53.9 ms: 1.01x faster                                                       |
| xml_etree_iterparse  | 63.5 ms                                                     | 65.2 ms: 1.03x slower                                                       |
| pickle               | 6.80 us                                                     | 7.06 us: 1.04x slower                                                       |
| pickle_list          | 2.59 us                                                     | 2.76 us: 1.07x slower                                                       |
| pickle_dict          | 16.9 us                                                     | 19.1 us: 1.13x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.08x faster                                                                |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20221109-pythonperf1-amd64-python-c03e05c2e72f3ea5e797-3.12.0a1+-c03e05c |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 20.0 ms                                                     | 19.3 ms: 1.03x faster                                                       |
| python_startup_no_site | 15.5 ms                                                     | 16.4 ms: 1.06x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.01x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20221109-pythonperf1-amd64-python-c03e05c2e72f3ea5e797-3.12.0a1+-c03e05c |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 8.80 ms                                                     | 7.18 ms: 1.23x faster                                                       |
| django_template | 28.2 ms                                                     | 24.4 ms: 1.16x faster                                                       |
| genshi_text     | 19.0 ms                                                     | 16.9 ms: 1.13x faster                                                       |
| genshi_xml      | 40.5 ms                                                     | 38.8 ms: 1.04x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.14x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20221109-pythonperf1-amd64-python-c03e05c2e72f3ea5e797-3.12.0a1+-c03e05c |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deltablue               | 4.17 ms                                                     | 2.59 ms: 1.61x faster                                                       |
| mypy2                   | 352 ms                                                      | 224 ms: 1.57x faster                                                        |
| json_dumps              | 8.50 ms                                                     | 5.54 ms: 1.53x faster                                                       |
| logging_silent          | 96.4 ns                                                     | 72.0 ns: 1.34x faster                                                       |
| raytrace                | 271 ms                                                      | 203 ms: 1.34x faster                                                        |
| scimark_sor             | 105 ms                                                      | 80.1 ms: 1.31x faster                                                       |
| richards                | 41.2 ms                                                     | 31.5 ms: 1.31x faster                                                       |
| go                      | 136 ms                                                      | 105 ms: 1.30x faster                                                        |
| async_tree_io           | 1.07 sec                                                    | 827 ms: 1.29x faster                                                        |
| crypto_pyaes            | 62.3 ms                                                     | 48.6 ms: 1.28x faster                                                       |
| sqlglot_parse           | 1.22 ms                                                     | 956 us: 1.27x faster                                                        |
| sqlglot_transpile       | 1.46 ms                                                     | 1.16 ms: 1.27x faster                                                       |
| scimark_lu              | 85.4 ms                                                     | 67.9 ms: 1.26x faster                                                       |
| pyflate                 | 387 ms                                                      | 311 ms: 1.24x faster                                                        |
| async_tree_none         | 420 ms                                                      | 338 ms: 1.24x faster                                                        |
| thrift                  | 615 us                                                      | 497 us: 1.24x faster                                                        |
| async_tree_memoization  | 497 ms                                                      | 402 ms: 1.24x faster                                                        |
| pickle_pure_python      | 257 us                                                      | 208 us: 1.24x faster                                                        |
| mako                    | 8.80 ms                                                     | 7.18 ms: 1.23x faster                                                       |
| pycparser               | 868 ms                                                      | 711 ms: 1.22x faster                                                        |
| chaos                   | 58.9 ms                                                     | 49.1 ms: 1.20x faster                                                       |
| async_generators        | 224 ms                                                      | 188 ms: 1.19x faster                                                        |
| tornado_http            | 109 ms                                                      | 92.5 ms: 1.18x faster                                                       |
| async_tree_cpu_io_mixed | 609 ms                                                      | 517 ms: 1.18x faster                                                        |
| scimark_monte_carlo     | 55.9 ms                                                     | 47.5 ms: 1.18x faster                                                       |
| create_gc_cycles        | 782 us                                                      | 672 us: 1.16x faster                                                        |
| html5lib                | 46.5 ms                                                     | 39.9 ms: 1.16x faster                                                       |
| pprint_safe_repr        | 589 ms                                                      | 506 ms: 1.16x faster                                                        |
| docutils                | 1.89 sec                                                    | 1.63 sec: 1.16x faster                                                      |
| django_template         | 28.2 ms                                                     | 24.4 ms: 1.16x faster                                                       |
| regex_compile           | 103 ms                                                      | 89.9 ms: 1.15x faster                                                       |
| regex_v8                | 15.0 ms                                                     | 13.1 ms: 1.15x faster                                                       |
| xml_etree_process       | 43.4 ms                                                     | 37.8 ms: 1.15x faster                                                       |
| dulwich_log             | 47.6 ms                                                     | 41.6 ms: 1.14x faster                                                       |
| pprint_pformat          | 1.21 sec                                                    | 1.06 sec: 1.14x faster                                                      |
| chameleon               | 5.92 ms                                                     | 5.20 ms: 1.14x faster                                                       |
| xml_etree_parse         | 102 ms                                                      | 89.7 ms: 1.13x faster                                                       |
| 2to3                    | 237 ms                                                      | 209 ms: 1.13x faster                                                        |
| dask                    | 305 ms                                                      | 270 ms: 1.13x faster                                                        |
| genshi_text             | 19.0 ms                                                     | 16.9 ms: 1.13x faster                                                       |
| unpickle                | 9.17 us                                                     | 8.17 us: 1.12x faster                                                       |
| regex_dna               | 132 ms                                                      | 118 ms: 1.12x faster                                                        |
| hexiom                  | 5.52 ms                                                     | 4.95 ms: 1.12x faster                                                       |
| json                    | 3.05 ms                                                     | 2.74 ms: 1.11x faster                                                       |
| unpickle_pure_python    | 171 us                                                      | 154 us: 1.11x faster                                                        |
| deepcopy_memo           | 28.5 us                                                     | 25.7 us: 1.11x faster                                                       |
| spectral_norm           | 78.0 ms                                                     | 70.5 ms: 1.11x faster                                                       |
| sqlglot_optimize        | 39.0 ms                                                     | 35.4 ms: 1.10x faster                                                       |
| scimark_sparse_mat_mult | 2.66 ms                                                     | 2.43 ms: 1.09x faster                                                       |
| json_loads              | 14.2 us                                                     | 13.0 us: 1.09x faster                                                       |
| bench_thread_pool       | 946 us                                                      | 868 us: 1.09x faster                                                        |
| sympy_integrate         | 14.8 ms                                                     | 13.6 ms: 1.09x faster                                                       |
| float                   | 60.2 ms                                                     | 55.8 ms: 1.08x faster                                                       |
| regex_effbot            | 1.66 ms                                                     | 1.56 ms: 1.07x faster                                                       |
| sympy_expand            | 315 ms                                                      | 297 ms: 1.06x faster                                                        |
| coroutines              | 15.9 ms                                                     | 15.1 ms: 1.06x faster                                                       |
| genshi_xml              | 40.5 ms                                                     | 38.8 ms: 1.04x faster                                                       |
| pathlib                 | 77.4 ms                                                     | 74.2 ms: 1.04x faster                                                       |
| python_startup          | 20.0 ms                                                     | 19.3 ms: 1.03x faster                                                       |
| sqlglot_normalize       | 202 ms                                                      | 196 ms: 1.03x faster                                                        |
| sympy_sum               | 104 ms                                                      | 101 ms: 1.03x faster                                                        |
| deepcopy_reduce         | 2.16 us                                                     | 2.11 us: 1.02x faster                                                       |
| scimark_fft             | 193 ms                                                      | 189 ms: 1.02x faster                                                        |
| sqlite_synth            | 1.84 us                                                     | 1.80 us: 1.02x faster                                                       |
| xml_etree_generate      | 54.5 ms                                                     | 53.9 ms: 1.01x faster                                                       |
| meteor_contest          | 72.5 ms                                                     | 72.0 ms: 1.01x faster                                                       |
| xml_etree_iterparse     | 63.5 ms                                                     | 65.2 ms: 1.03x slower                                                       |
| nbody                   | 69.3 ms                                                     | 71.3 ms: 1.03x slower                                                       |
| unpack_sequence         | 37.8 ns                                                     | 39.2 ns: 1.04x slower                                                       |
| pickle                  | 6.80 us                                                     | 7.06 us: 1.04x slower                                                       |
| pidigits                | 145 ms                                                      | 151 ms: 1.04x slower                                                        |
| telco                   | 3.78 ms                                                     | 3.95 ms: 1.04x slower                                                       |
| fannkuch                | 258 ms                                                      | 270 ms: 1.05x slower                                                        |
| asyncio_tcp             | 712 ms                                                      | 753 ms: 1.06x slower                                                        |
| python_startup_no_site  | 15.5 ms                                                     | 16.4 ms: 1.06x slower                                                       |
| pickle_list             | 2.59 us                                                     | 2.76 us: 1.07x slower                                                       |
| comprehensions          | 16.0 us                                                     | 17.1 us: 1.07x slower                                                       |
| gc_traversal            | 1.34 ms                                                     | 1.45 ms: 1.08x slower                                                       |
| generators              | 31.6 ms                                                     | 34.5 ms: 1.09x slower                                                       |
| bench_mp_pool           | 60.7 ms                                                     | 67.3 ms: 1.11x slower                                                       |
| logging_format          | 6.66 us                                                     | 7.41 us: 1.11x slower                                                       |
| pickle_dict             | 16.9 us                                                     | 19.1 us: 1.13x slower                                                       |
| logging_simple          | 6.20 us                                                     | 7.05 us: 1.14x slower                                                       |
| coverage                | 40.0 ms                                                     | 55.0 ms: 1.37x slower                                                       |
| Geometric mean          | (ref)                                                       | 1.10x faster                                                                |

Benchmark hidden because not significant (5): unpickle_list, mdp, sympy_str, nqueens, deepcopy
Ignored benchmarks (9) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.10x
- 95% likely to have a speedup of 1.09x
- 99% likely to have a speedup of 1.07x
