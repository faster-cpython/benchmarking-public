
# Results vs. 3.11.0

- fork: python
- ref: c4170c36b0b54c10456f
- machine: windows-amd64
- commit hash: c4170c3
- commit date: 2023-01-29
- overall geometric mean: 1.10x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230129-pythonperf1-amd64-python-c4170c36b0b54c10456f-3.12.0a4+-c4170c3 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 209 ms                                                      | 199 ms: 1.05x faster                                                        |
| chameleon      | 5.11 ms                                                     | 4.43 ms: 1.16x faster                                                       |
| docutils       | 1.60 sec                                                    | 1.53 sec: 1.05x faster                                                      |
| html5lib       | 37.5 ms                                                     | 35.1 ms: 1.07x faster                                                       |
| Geometric mean | (ref)                                                       | 1.06x faster                                                                |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230129-pythonperf1-amd64-python-c4170c36b0b54c10456f-3.12.0a4+-c4170c3 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 54.6 ms                                                     | 48.2 ms: 1.13x faster                                                       |
| nbody          | 70.0 ms                                                     | 61.8 ms: 1.13x faster                                                       |
| pidigits       | 148 ms                                                      | 151 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                       | 1.08x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230129-pythonperf1-amd64-python-c4170c36b0b54c10456f-3.12.0a4+-c4170c3 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 90.6 ms                                                     | 79.7 ms: 1.14x faster                                                       |
| regex_dna      | 115 ms                                                      | 121 ms: 1.05x slower                                                        |
| regex_effbot   | 1.50 ms                                                     | 1.57 ms: 1.05x slower                                                       |
| Geometric mean | (ref)                                                       | 1.01x faster                                                                |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230129-pythonperf1-amd64-python-c4170c36b0b54c10456f-3.12.0a4+-c4170c3 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 7.56 ms                                                     | 5.15 ms: 1.47x faster                                                       |
| unpickle_pure_python | 152 us                                                      | 120 us: 1.26x faster                                                        |
| pickle_pure_python   | 200 us                                                      | 176 us: 1.13x faster                                                        |
| xml_etree_parse      | 95.9 ms                                                     | 87.3 ms: 1.10x faster                                                       |
| xml_etree_process    | 37.1 ms                                                     | 34.3 ms: 1.08x faster                                                       |
| xml_etree_generate   | 52.2 ms                                                     | 50.1 ms: 1.04x faster                                                       |
| json_loads           | 12.9 us                                                     | 12.8 us: 1.01x faster                                                       |
| xml_etree_iterparse  | 62.6 ms                                                     | 63.3 ms: 1.01x slower                                                       |
| pickle               | 6.61 us                                                     | 6.73 us: 1.02x slower                                                       |
| pickle_list          | 2.68 us                                                     | 2.78 us: 1.04x slower                                                       |
| unpickle_list        | 2.55 us                                                     | 2.78 us: 1.09x slower                                                       |
| unpickle             | 8.09 us                                                     | 8.95 us: 1.11x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.06x faster                                                                |

Benchmark hidden because not significant (1): pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230129-pythonperf1-amd64-python-c4170c36b0b54c10456f-3.12.0a4+-c4170c3 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 18.7 ms                                                     | 19.0 ms: 1.02x slower                                                       |
| python_startup_no_site | 15.9 ms                                                     | 16.3 ms: 1.03x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.02x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230129-pythonperf1-amd64-python-c4170c36b0b54c10456f-3.12.0a4+-c4170c3 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 37.3 ms                                                     | 30.8 ms: 1.21x faster                                                       |
| genshi_text     | 17.0 ms                                                     | 14.0 ms: 1.21x faster                                                       |
| mako            | 7.26 ms                                                     | 6.16 ms: 1.18x faster                                                       |
| django_template | 24.1 ms                                                     | 20.9 ms: 1.15x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.19x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230129-pythonperf1-amd64-python-c4170c36b0b54c10456f-3.12.0a4+-c4170c3 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpack_sequence         | 46.1 ns                                                     | 26.2 ns: 1.75x faster                                                       |
| json_dumps              | 7.56 ms                                                     | 5.15 ms: 1.47x faster                                                       |
| asyncio_tcp             | 699 ms                                                      | 489 ms: 1.43x faster                                                        |
| comprehensions          | 15.9 us                                                     | 12.0 us: 1.33x faster                                                       |
| richards                | 30.6 ms                                                     | 23.1 ms: 1.32x faster                                                       |
| deltablue               | 2.61 ms                                                     | 1.99 ms: 1.31x faster                                                       |
| unpickle_pure_python    | 152 us                                                      | 120 us: 1.26x faster                                                        |
| logging_silent          | 69.8 ns                                                     | 55.7 ns: 1.25x faster                                                       |
| raytrace                | 211 ms                                                      | 171 ms: 1.23x faster                                                        |
| scimark_sor             | 75.6 ms                                                     | 61.9 ms: 1.22x faster                                                       |
| genshi_xml              | 37.3 ms                                                     | 30.8 ms: 1.21x faster                                                       |
| hexiom                  | 4.55 ms                                                     | 3.76 ms: 1.21x faster                                                       |
| deepcopy_memo           | 25.2 us                                                     | 20.8 us: 1.21x faster                                                       |
| genshi_text             | 17.0 ms                                                     | 14.0 ms: 1.21x faster                                                       |
| go                      | 97.3 ms                                                     | 80.6 ms: 1.21x faster                                                       |
| scimark_monte_carlo     | 44.6 ms                                                     | 37.0 ms: 1.20x faster                                                       |
| json                    | 3.25 ms                                                     | 2.70 ms: 1.20x faster                                                       |
| deepcopy                | 246 us                                                      | 208 us: 1.18x faster                                                        |
| mako                    | 7.26 ms                                                     | 6.16 ms: 1.18x faster                                                       |
| pyflate                 | 304 ms                                                      | 260 ms: 1.17x faster                                                        |
| chameleon               | 5.11 ms                                                     | 4.43 ms: 1.16x faster                                                       |
| django_template         | 24.1 ms                                                     | 20.9 ms: 1.15x faster                                                       |
| nqueens                 | 64.9 ms                                                     | 56.4 ms: 1.15x faster                                                       |
| sympy_str               | 182 ms                                                      | 159 ms: 1.15x faster                                                        |
| regex_compile           | 90.6 ms                                                     | 79.7 ms: 1.14x faster                                                       |
| pickle_pure_python      | 200 us                                                      | 176 us: 1.13x faster                                                        |
| chaos                   | 47.1 ms                                                     | 41.6 ms: 1.13x faster                                                       |
| float                   | 54.6 ms                                                     | 48.2 ms: 1.13x faster                                                       |
| nbody                   | 70.0 ms                                                     | 61.8 ms: 1.13x faster                                                       |
| scimark_sparse_mat_mult | 2.57 ms                                                     | 2.27 ms: 1.13x faster                                                       |
| sqlglot_normalize       | 190 ms                                                      | 170 ms: 1.12x faster                                                        |
| scimark_lu              | 63.5 ms                                                     | 56.7 ms: 1.12x faster                                                       |
| spectral_norm           | 67.9 ms                                                     | 60.8 ms: 1.12x faster                                                       |
| pprint_pformat          | 1.04 sec                                                    | 935 ms: 1.11x faster                                                        |
| deepcopy_reduce         | 2.07 us                                                     | 1.87 us: 1.11x faster                                                       |
| sqlglot_transpile       | 1.16 ms                                                     | 1.05 ms: 1.11x faster                                                       |
| dulwich_log             | 44.5 ms                                                     | 40.3 ms: 1.10x faster                                                       |
| mdp                     | 1.67 sec                                                    | 1.52 sec: 1.10x faster                                                      |
| pprint_safe_repr        | 512 ms                                                      | 465 ms: 1.10x faster                                                        |
| sympy_sum               | 99.9 ms                                                     | 90.8 ms: 1.10x faster                                                       |
| xml_etree_parse         | 95.9 ms                                                     | 87.3 ms: 1.10x faster                                                       |
| sympy_integrate         | 13.8 ms                                                     | 12.6 ms: 1.10x faster                                                       |
| sqlglot_optimize        | 34.9 ms                                                     | 32.0 ms: 1.09x faster                                                       |
| sympy_expand            | 295 ms                                                      | 271 ms: 1.09x faster                                                        |
| sqlglot_parse           | 952 us                                                      | 874 us: 1.09x faster                                                        |
| xml_etree_process       | 37.1 ms                                                     | 34.3 ms: 1.08x faster                                                       |
| telco                   | 3.90 ms                                                     | 3.62 ms: 1.08x faster                                                       |
| pycparser               | 691 ms                                                      | 641 ms: 1.08x faster                                                        |
| logging_simple          | 6.61 us                                                     | 6.16 us: 1.07x faster                                                       |
| meteor_contest          | 74.7 ms                                                     | 69.6 ms: 1.07x faster                                                       |
| logging_format          | 7.01 us                                                     | 6.54 us: 1.07x faster                                                       |
| scimark_fft             | 178 ms                                                      | 167 ms: 1.07x faster                                                        |
| html5lib                | 37.5 ms                                                     | 35.1 ms: 1.07x faster                                                       |
| thrift                  | 491 us                                                      | 460 us: 1.07x faster                                                        |
| mypy2                   | 229 ms                                                      | 216 ms: 1.06x faster                                                        |
| crypto_pyaes            | 47.6 ms                                                     | 45.0 ms: 1.06x faster                                                       |
| 2to3                    | 209 ms                                                      | 199 ms: 1.05x faster                                                        |
| docutils                | 1.60 sec                                                    | 1.53 sec: 1.05x faster                                                      |
| fannkuch                | 252 ms                                                      | 242 ms: 1.04x faster                                                        |
| xml_etree_generate      | 52.2 ms                                                     | 50.1 ms: 1.04x faster                                                       |
| coverage                | 55.9 ms                                                     | 54.1 ms: 1.03x faster                                                       |
| bench_thread_pool       | 852 us                                                      | 833 us: 1.02x faster                                                        |
| async_tree_none         | 320 ms                                                      | 315 ms: 1.02x faster                                                        |
| async_tree_io           | 779 ms                                                      | 768 ms: 1.01x faster                                                        |
| async_generators        | 178 ms                                                      | 176 ms: 1.01x faster                                                        |
| json_loads              | 12.9 us                                                     | 12.8 us: 1.01x faster                                                       |
| gc_traversal            | 1.46 ms                                                     | 1.47 ms: 1.01x slower                                                       |
| coroutines              | 14.6 ms                                                     | 14.8 ms: 1.01x slower                                                       |
| sqlite_synth            | 1.68 us                                                     | 1.70 us: 1.01x slower                                                       |
| bench_mp_pool           | 62.5 ms                                                     | 63.3 ms: 1.01x slower                                                       |
| xml_etree_iterparse     | 62.6 ms                                                     | 63.3 ms: 1.01x slower                                                       |
| pidigits                | 148 ms                                                      | 151 ms: 1.02x slower                                                        |
| generators              | 33.8 ms                                                     | 34.4 ms: 1.02x slower                                                       |
| async_tree_memoization  | 371 ms                                                      | 378 ms: 1.02x slower                                                        |
| python_startup          | 18.7 ms                                                     | 19.0 ms: 1.02x slower                                                       |
| pickle                  | 6.61 us                                                     | 6.73 us: 1.02x slower                                                       |
| python_startup_no_site  | 15.9 ms                                                     | 16.3 ms: 1.03x slower                                                       |
| pickle_list             | 2.68 us                                                     | 2.78 us: 1.04x slower                                                       |
| pathlib                 | 71.4 ms                                                     | 74.2 ms: 1.04x slower                                                       |
| regex_dna               | 115 ms                                                      | 121 ms: 1.05x slower                                                        |
| regex_effbot            | 1.50 ms                                                     | 1.57 ms: 1.05x slower                                                       |
| unpickle_list           | 2.55 us                                                     | 2.78 us: 1.09x slower                                                       |
| unpickle                | 8.09 us                                                     | 8.95 us: 1.11x slower                                                       |
| Geometric mean          | (ref)                                                       | 1.10x faster                                                                |

Benchmark hidden because not significant (6): async_tree_cpu_io_mixed, dask, regex_v8, tornado_http, pickle_dict, create_gc_cycles
Ignored benchmarks (9) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.05x
