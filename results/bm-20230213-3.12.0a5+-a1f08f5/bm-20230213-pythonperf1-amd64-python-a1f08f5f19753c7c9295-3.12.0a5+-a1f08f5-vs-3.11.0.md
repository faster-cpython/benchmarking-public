
# Results vs. 3.11.0

- fork: python
- ref: a1f08f5f19753c7c9295
- machine: windows-amd64
- commit hash: a1f08f5
- commit date: 2023-02-13
- overall geometric mean: 1.09x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230213-pythonperf1-amd64-python-a1f08f5f19753c7c9295-3.12.0a5+-a1f08f5 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 209 ms                                                      | 201 ms: 1.04x faster                                                        |
| chameleon      | 5.11 ms                                                     | 4.43 ms: 1.15x faster                                                       |
| docutils       | 1.60 sec                                                    | 1.57 sec: 1.02x faster                                                      |
| html5lib       | 37.5 ms                                                     | 34.9 ms: 1.08x faster                                                       |
| tornado_http   | 91.8 ms                                                     | 90.3 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                       | 1.06x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230213-pythonperf1-amd64-python-a1f08f5f19753c7c9295-3.12.0a5+-a1f08f5 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 70.0 ms                                                     | 62.7 ms: 1.12x faster                                                       |
| float          | 54.6 ms                                                     | 49.6 ms: 1.10x faster                                                       |
| pidigits       | 148 ms                                                      | 150 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                       | 1.07x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230213-pythonperf1-amd64-python-a1f08f5f19753c7c9295-3.12.0a5+-a1f08f5 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 90.6 ms                                                     | 78.6 ms: 1.15x faster                                                       |
| regex_v8       | 13.8 ms                                                     | 14.4 ms: 1.04x slower                                                       |
| regex_effbot   | 1.50 ms                                                     | 1.60 ms: 1.07x slower                                                       |
| regex_dna      | 115 ms                                                      | 124 ms: 1.08x slower                                                        |
| Geometric mean | (ref)                                                       | 1.01x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230213-pythonperf1-amd64-python-a1f08f5f19753c7c9295-3.12.0a5+-a1f08f5 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 7.56 ms                                                     | 5.27 ms: 1.43x faster                                                       |
| unpickle_pure_python | 152 us                                                      | 119 us: 1.28x faster                                                        |
| pickle_pure_python   | 200 us                                                      | 169 us: 1.18x faster                                                        |
| xml_etree_parse      | 95.9 ms                                                     | 91.5 ms: 1.05x faster                                                       |
| xml_etree_process    | 37.1 ms                                                     | 35.9 ms: 1.03x faster                                                       |
| xml_etree_generate   | 52.2 ms                                                     | 51.6 ms: 1.01x faster                                                       |
| pickle_list          | 2.68 us                                                     | 2.73 us: 1.02x slower                                                       |
| pickle_dict          | 18.5 us                                                     | 19.3 us: 1.04x slower                                                       |
| xml_etree_iterparse  | 62.6 ms                                                     | 65.5 ms: 1.05x slower                                                       |
| pickle               | 6.61 us                                                     | 6.93 us: 1.05x slower                                                       |
| unpickle_list        | 2.55 us                                                     | 2.71 us: 1.07x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.05x faster                                                                |

Benchmark hidden because not significant (2): unpickle, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230213-pythonperf1-amd64-python-a1f08f5f19753c7c9295-3.12.0a5+-a1f08f5 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 15.9 ms                                                     | 15.7 ms: 1.01x faster                                                       |
| Geometric mean         | (ref)                                                       | 1.00x faster                                                                |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230213-pythonperf1-amd64-python-a1f08f5f19753c7c9295-3.12.0a5+-a1f08f5 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 17.0 ms                                                     | 13.5 ms: 1.25x faster                                                       |
| genshi_xml      | 37.3 ms                                                     | 30.5 ms: 1.22x faster                                                       |
| mako            | 7.26 ms                                                     | 5.99 ms: 1.21x faster                                                       |
| django_template | 24.1 ms                                                     | 21.0 ms: 1.15x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.21x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230213-pythonperf1-amd64-python-a1f08f5f19753c7c9295-3.12.0a5+-a1f08f5 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpack_sequence         | 46.1 ns                                                     | 25.6 ns: 1.80x faster                                                       |
| asyncio_tcp             | 699 ms                                                      | 485 ms: 1.44x faster                                                        |
| json_dumps              | 7.56 ms                                                     | 5.27 ms: 1.43x faster                                                       |
| deltablue               | 2.61 ms                                                     | 1.96 ms: 1.33x faster                                                       |
| comprehensions          | 15.9 us                                                     | 12.0 us: 1.33x faster                                                       |
| unpickle_pure_python    | 152 us                                                      | 119 us: 1.28x faster                                                        |
| richards                | 30.6 ms                                                     | 23.9 ms: 1.28x faster                                                       |
| logging_silent          | 69.8 ns                                                     | 54.7 ns: 1.28x faster                                                       |
| genshi_text             | 17.0 ms                                                     | 13.5 ms: 1.25x faster                                                       |
| genshi_xml              | 37.3 ms                                                     | 30.5 ms: 1.22x faster                                                       |
| hexiom                  | 4.55 ms                                                     | 3.73 ms: 1.22x faster                                                       |
| mako                    | 7.26 ms                                                     | 5.99 ms: 1.21x faster                                                       |
| raytrace                | 211 ms                                                      | 174 ms: 1.21x faster                                                        |
| deepcopy_memo           | 25.2 us                                                     | 20.9 us: 1.21x faster                                                       |
| deepcopy                | 246 us                                                      | 205 us: 1.20x faster                                                        |
| go                      | 97.3 ms                                                     | 82.0 ms: 1.19x faster                                                       |
| pickle_pure_python      | 200 us                                                      | 169 us: 1.18x faster                                                        |
| json                    | 3.25 ms                                                     | 2.78 ms: 1.17x faster                                                       |
| chameleon               | 5.11 ms                                                     | 4.43 ms: 1.15x faster                                                       |
| nqueens                 | 64.9 ms                                                     | 56.2 ms: 1.15x faster                                                       |
| regex_compile           | 90.6 ms                                                     | 78.6 ms: 1.15x faster                                                       |
| django_template         | 24.1 ms                                                     | 21.0 ms: 1.15x faster                                                       |
| scimark_sparse_mat_mult | 2.57 ms                                                     | 2.24 ms: 1.15x faster                                                       |
| pyflate                 | 304 ms                                                      | 265 ms: 1.15x faster                                                        |
| scimark_sor             | 75.6 ms                                                     | 66.1 ms: 1.14x faster                                                       |
| chaos                   | 47.1 ms                                                     | 41.6 ms: 1.13x faster                                                       |
| scimark_monte_carlo     | 44.6 ms                                                     | 39.4 ms: 1.13x faster                                                       |
| scimark_lu              | 63.5 ms                                                     | 56.4 ms: 1.13x faster                                                       |
| pprint_pformat          | 1.04 sec                                                    | 925 ms: 1.12x faster                                                        |
| deepcopy_reduce         | 2.07 us                                                     | 1.85 us: 1.12x faster                                                       |
| nbody                   | 70.0 ms                                                     | 62.7 ms: 1.12x faster                                                       |
| fannkuch                | 252 ms                                                      | 226 ms: 1.11x faster                                                        |
| logging_format          | 7.01 us                                                     | 6.31 us: 1.11x faster                                                       |
| pprint_safe_repr        | 512 ms                                                      | 463 ms: 1.10x faster                                                        |
| sympy_str               | 182 ms                                                      | 165 ms: 1.10x faster                                                        |
| float                   | 54.6 ms                                                     | 49.6 ms: 1.10x faster                                                       |
| sympy_integrate         | 13.8 ms                                                     | 12.6 ms: 1.10x faster                                                       |
| sqlglot_parse           | 952 us                                                      | 867 us: 1.10x faster                                                        |
| logging_simple          | 6.61 us                                                     | 6.04 us: 1.10x faster                                                       |
| spectral_norm           | 67.9 ms                                                     | 62.0 ms: 1.10x faster                                                       |
| sympy_expand            | 295 ms                                                      | 270 ms: 1.09x faster                                                        |
| sqlglot_transpile       | 1.16 ms                                                     | 1.07 ms: 1.09x faster                                                       |
| crypto_pyaes            | 47.6 ms                                                     | 43.9 ms: 1.08x faster                                                       |
| sqlglot_normalize       | 190 ms                                                      | 176 ms: 1.08x faster                                                        |
| sqlglot_optimize        | 34.9 ms                                                     | 32.3 ms: 1.08x faster                                                       |
| html5lib                | 37.5 ms                                                     | 34.9 ms: 1.08x faster                                                       |
| sympy_sum               | 99.9 ms                                                     | 93.3 ms: 1.07x faster                                                       |
| dulwich_log             | 44.5 ms                                                     | 41.8 ms: 1.06x faster                                                       |
| mypy2                   | 229 ms                                                      | 216 ms: 1.06x faster                                                        |
| coverage                | 55.9 ms                                                     | 52.7 ms: 1.06x faster                                                       |
| scimark_fft             | 178 ms                                                      | 168 ms: 1.06x faster                                                        |
| mdp                     | 1.67 sec                                                    | 1.58 sec: 1.06x faster                                                      |
| meteor_contest          | 74.7 ms                                                     | 70.9 ms: 1.05x faster                                                       |
| xml_etree_parse         | 95.9 ms                                                     | 91.5 ms: 1.05x faster                                                       |
| 2to3                    | 209 ms                                                      | 201 ms: 1.04x faster                                                        |
| pycparser               | 691 ms                                                      | 666 ms: 1.04x faster                                                        |
| xml_etree_process       | 37.1 ms                                                     | 35.9 ms: 1.03x faster                                                       |
| coroutines              | 14.6 ms                                                     | 14.2 ms: 1.03x faster                                                       |
| async_tree_cpu_io_mixed | 501 ms                                                      | 488 ms: 1.03x faster                                                        |
| thrift                  | 491 us                                                      | 480 us: 1.02x faster                                                        |
| telco                   | 3.90 ms                                                     | 3.82 ms: 1.02x faster                                                       |
| async_tree_none         | 320 ms                                                      | 314 ms: 1.02x faster                                                        |
| docutils                | 1.60 sec                                                    | 1.57 sec: 1.02x faster                                                      |
| tornado_http            | 91.8 ms                                                     | 90.3 ms: 1.02x faster                                                       |
| async_tree_io           | 779 ms                                                      | 769 ms: 1.01x faster                                                        |
| xml_etree_generate      | 52.2 ms                                                     | 51.6 ms: 1.01x faster                                                       |
| bench_thread_pool       | 852 us                                                      | 843 us: 1.01x faster                                                        |
| python_startup_no_site  | 15.9 ms                                                     | 15.7 ms: 1.01x faster                                                       |
| pidigits                | 148 ms                                                      | 150 ms: 1.01x slower                                                        |
| pickle_list             | 2.68 us                                                     | 2.73 us: 1.02x slower                                                       |
| gc_traversal            | 1.46 ms                                                     | 1.49 ms: 1.02x slower                                                       |
| bench_mp_pool           | 62.5 ms                                                     | 64.0 ms: 1.02x slower                                                       |
| regex_v8                | 13.8 ms                                                     | 14.4 ms: 1.04x slower                                                       |
| pathlib                 | 71.4 ms                                                     | 74.3 ms: 1.04x slower                                                       |
| pickle_dict             | 18.5 us                                                     | 19.3 us: 1.04x slower                                                       |
| xml_etree_iterparse     | 62.6 ms                                                     | 65.5 ms: 1.05x slower                                                       |
| pickle                  | 6.61 us                                                     | 6.93 us: 1.05x slower                                                       |
| sqlite_synth            | 1.68 us                                                     | 1.79 us: 1.06x slower                                                       |
| unpickle_list           | 2.55 us                                                     | 2.71 us: 1.07x slower                                                       |
| regex_effbot            | 1.50 ms                                                     | 1.60 ms: 1.07x slower                                                       |
| regex_dna               | 115 ms                                                      | 124 ms: 1.08x slower                                                        |
| async_generators        | 178 ms                                                      | 216 ms: 1.22x slower                                                        |
| Geometric mean          | (ref)                                                       | 1.09x faster                                                                |

Benchmark hidden because not significant (6): unpickle, generators, async_tree_memoization, create_gc_cycles, json_loads, python_startup
Ignored benchmarks (10) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, dask, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x
