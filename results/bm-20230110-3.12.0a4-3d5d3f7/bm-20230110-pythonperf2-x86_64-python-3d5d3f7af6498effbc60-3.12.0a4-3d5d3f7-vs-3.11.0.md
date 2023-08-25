
# Results vs. 3.11.0

- fork: python
- ref: 3d5d3f7af6498effbc60
- machine: linux-x86_64
- commit hash: 3d5d3f7
- commit date: 2023-01-10
- overall geometric mean: 1.04x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230110-pythonperf2-x86_64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 288 ms                                                       | 286 ms: 1.01x faster                                                        |
| chameleon      | 7.67 ms                                                      | 7.31 ms: 1.05x faster                                                       |
| docutils       | 2.86 sec                                                     | 2.78 sec: 1.03x faster                                                      |
| html5lib       | 72.9 ms                                                      | 66.8 ms: 1.09x faster                                                       |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230110-pythonperf2-x86_64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 74.2 ms                                                      | 72.4 ms: 1.03x faster                                                       |
| pidigits       | 251 ms                                                       | 252 ms: 1.00x slower                                                        |
| nbody          | 90.7 ms                                                      | 98.1 ms: 1.08x slower                                                       |
| Geometric mean | (ref)                                                        | 1.02x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230110-pythonperf2-x86_64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 158 ms                                                       | 149 ms: 1.06x faster                                                        |
| regex_v8       | 23.9 ms                                                      | 23.0 ms: 1.04x faster                                                       |
| regex_effbot   | 3.50 ms                                                      | 3.43 ms: 1.02x faster                                                       |
| regex_dna      | 227 ms                                                       | 229 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230110-pythonperf2-x86_64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 13.4 ms                                                      | 10.1 ms: 1.32x faster                                                       |
| json_loads           | 28.7 us                                                      | 24.0 us: 1.19x faster                                                       |
| unpickle_pure_python | 241 us                                                       | 214 us: 1.12x faster                                                        |
| xml_etree_parse      | 158 ms                                                       | 144 ms: 1.10x faster                                                        |
| pickle_list          | 3.83 us                                                      | 3.70 us: 1.03x faster                                                       |
| pickle_pure_python   | 319 us                                                       | 313 us: 1.02x faster                                                        |
| xml_etree_process    | 56.5 ms                                                      | 55.4 ms: 1.02x faster                                                       |
| unpickle_list        | 4.53 us                                                      | 4.48 us: 1.01x faster                                                       |
| unpickle             | 13.4 us                                                      | 13.3 us: 1.01x faster                                                       |
| xml_etree_generate   | 80.5 ms                                                      | 80.3 ms: 1.00x faster                                                       |
| pickle               | 9.64 us                                                      | 9.71 us: 1.01x slower                                                       |
| pickle_dict          | 30.8 us                                                      | 31.1 us: 1.01x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.06x faster                                                                |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230110-pythonperf2-x86_64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 10.8 ms                                                      | 10.8 ms: 1.00x slower                                                       |
| python_startup_no_site | 7.76 ms                                                      | 7.87 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230110-pythonperf2-x86_64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 58.5 ms                                                      | 53.7 ms: 1.09x faster                                                       |
| mako            | 11.0 ms                                                      | 10.2 ms: 1.07x faster                                                       |
| genshi_text     | 26.1 ms                                                      | 24.8 ms: 1.05x faster                                                       |
| django_template | 40.2 ms                                                      | 39.2 ms: 1.03x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.06x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230110-pythonperf2-x86_64-python-3d5d3f7af6498effbc60-3.12.0a4-3d5d3f7 |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| asyncio_tcp             | 753 ms                                                       | 386 ms: 1.95x faster                                                        |
| json_dumps              | 13.4 ms                                                      | 10.1 ms: 1.32x faster                                                       |
| json_loads              | 28.7 us                                                      | 24.0 us: 1.19x faster                                                       |
| mypy2                   | 451 ms                                                       | 380 ms: 1.19x faster                                                        |
| chaos                   | 80.9 ms                                                      | 70.9 ms: 1.14x faster                                                       |
| scimark_lu              | 115 ms                                                       | 101 ms: 1.14x faster                                                        |
| fannkuch                | 429 ms                                                       | 380 ms: 1.13x faster                                                        |
| unpickle_pure_python    | 241 us                                                       | 214 us: 1.12x faster                                                        |
| xml_etree_parse         | 158 ms                                                       | 144 ms: 1.10x faster                                                        |
| scimark_sparse_mat_mult | 4.05 ms                                                      | 3.70 ms: 1.09x faster                                                       |
| nqueens                 | 103 ms                                                       | 94.0 ms: 1.09x faster                                                       |
| html5lib                | 72.9 ms                                                      | 66.8 ms: 1.09x faster                                                       |
| genshi_xml              | 58.5 ms                                                      | 53.7 ms: 1.09x faster                                                       |
| gc_traversal            | 3.85 ms                                                      | 3.54 ms: 1.09x faster                                                       |
| deltablue               | 4.00 ms                                                      | 3.69 ms: 1.08x faster                                                       |
| json                    | 5.65 ms                                                      | 5.24 ms: 1.08x faster                                                       |
| mako                    | 11.0 ms                                                      | 10.2 ms: 1.07x faster                                                       |
| go                      | 164 ms                                                       | 153 ms: 1.07x faster                                                        |
| raytrace                | 317 ms                                                       | 299 ms: 1.06x faster                                                        |
| logging_format          | 8.11 us                                                      | 7.66 us: 1.06x faster                                                       |
| deepcopy_memo           | 38.8 us                                                      | 36.7 us: 1.06x faster                                                       |
| regex_compile           | 158 ms                                                       | 149 ms: 1.06x faster                                                        |
| deepcopy                | 399 us                                                       | 379 us: 1.05x faster                                                        |
| hexiom                  | 7.13 ms                                                      | 6.77 ms: 1.05x faster                                                       |
| genshi_text             | 26.1 ms                                                      | 24.8 ms: 1.05x faster                                                       |
| deepcopy_reduce         | 3.51 us                                                      | 3.33 us: 1.05x faster                                                       |
| pycparser               | 1.32 sec                                                     | 1.26 sec: 1.05x faster                                                      |
| chameleon               | 7.67 ms                                                      | 7.31 ms: 1.05x faster                                                       |
| regex_v8                | 23.9 ms                                                      | 23.0 ms: 1.04x faster                                                       |
| unpack_sequence         | 45.6 ns                                                      | 44.0 ns: 1.04x faster                                                       |
| async_tree_memoization  | 630 ms                                                       | 608 ms: 1.04x faster                                                        |
| pyflate                 | 449 ms                                                       | 433 ms: 1.04x faster                                                        |
| pickle_list             | 3.83 us                                                      | 3.70 us: 1.03x faster                                                       |
| logging_simple          | 7.19 us                                                      | 6.95 us: 1.03x faster                                                       |
| sympy_expand            | 555 ms                                                       | 537 ms: 1.03x faster                                                        |
| richards                | 48.3 ms                                                      | 46.9 ms: 1.03x faster                                                       |
| crypto_pyaes            | 83.4 ms                                                      | 81.1 ms: 1.03x faster                                                       |
| docutils                | 2.86 sec                                                     | 2.78 sec: 1.03x faster                                                      |
| async_tree_none         | 519 ms                                                       | 505 ms: 1.03x faster                                                        |
| scimark_sor             | 111 ms                                                       | 108 ms: 1.03x faster                                                        |
| sqlglot_normalize       | 126 ms                                                       | 123 ms: 1.03x faster                                                        |
| django_template         | 40.2 ms                                                      | 39.2 ms: 1.03x faster                                                       |
| float                   | 74.2 ms                                                      | 72.4 ms: 1.03x faster                                                       |
| bench_thread_pool       | 1.01 ms                                                      | 987 us: 1.02x faster                                                        |
| scimark_monte_carlo     | 68.2 ms                                                      | 66.6 ms: 1.02x faster                                                       |
| telco                   | 6.86 ms                                                      | 6.70 ms: 1.02x faster                                                       |
| regex_effbot            | 3.50 ms                                                      | 3.43 ms: 1.02x faster                                                       |
| pickle_pure_python      | 319 us                                                       | 313 us: 1.02x faster                                                        |
| xml_etree_process       | 56.5 ms                                                      | 55.4 ms: 1.02x faster                                                       |
| thrift                  | 925 us                                                       | 908 us: 1.02x faster                                                        |
| async_tree_io           | 1.17 sec                                                     | 1.15 sec: 1.02x faster                                                      |
| create_gc_cycles        | 1.61 ms                                                      | 1.58 ms: 1.02x faster                                                       |
| dulwich_log             | 68.4 ms                                                      | 67.5 ms: 1.01x faster                                                       |
| unpickle_list           | 4.53 us                                                      | 4.48 us: 1.01x faster                                                       |
| async_tree_cpu_io_mixed | 749 ms                                                       | 742 ms: 1.01x faster                                                        |
| sympy_integrate         | 25.8 ms                                                      | 25.6 ms: 1.01x faster                                                       |
| sqlglot_optimize        | 59.8 ms                                                      | 59.3 ms: 1.01x faster                                                       |
| scimark_fft             | 285 ms                                                       | 283 ms: 1.01x faster                                                        |
| unpickle                | 13.4 us                                                      | 13.3 us: 1.01x faster                                                       |
| sympy_str               | 337 ms                                                       | 335 ms: 1.01x faster                                                        |
| 2to3                    | 288 ms                                                       | 286 ms: 1.01x faster                                                        |
| xml_etree_generate      | 80.5 ms                                                      | 80.3 ms: 1.00x faster                                                       |
| mdp                     | 2.75 sec                                                     | 2.75 sec: 1.00x slower                                                      |
| python_startup          | 10.8 ms                                                      | 10.8 ms: 1.00x slower                                                       |
| pidigits                | 251 ms                                                       | 252 ms: 1.00x slower                                                        |
| meteor_contest          | 131 ms                                                       | 131 ms: 1.00x slower                                                        |
| pickle                  | 9.64 us                                                      | 9.71 us: 1.01x slower                                                       |
| sympy_sum               | 185 ms                                                       | 186 ms: 1.01x slower                                                        |
| regex_dna               | 227 ms                                                       | 229 ms: 1.01x slower                                                        |
| logging_silent          | 101 ns                                                       | 102 ns: 1.01x slower                                                        |
| pickle_dict             | 30.8 us                                                      | 31.1 us: 1.01x slower                                                       |
| coroutines              | 27.6 ms                                                      | 27.9 ms: 1.01x slower                                                       |
| pprint_safe_repr        | 784 ms                                                       | 794 ms: 1.01x slower                                                        |
| python_startup_no_site  | 7.76 ms                                                      | 7.87 ms: 1.01x slower                                                       |
| sqlglot_transpile       | 1.92 ms                                                      | 1.95 ms: 1.02x slower                                                       |
| pathlib                 | 19.1 ms                                                      | 19.4 ms: 1.02x slower                                                       |
| async_generators        | 316 ms                                                       | 322 ms: 1.02x slower                                                        |
| sqlite_synth            | 2.50 us                                                      | 2.56 us: 1.03x slower                                                       |
| sqlglot_parse           | 1.53 ms                                                      | 1.59 ms: 1.04x slower                                                       |
| coverage                | 84.8 ms                                                      | 89.3 ms: 1.05x slower                                                       |
| bench_mp_pool           | 4.62 ms                                                      | 4.94 ms: 1.07x slower                                                       |
| generators              | 56.0 ms                                                      | 60.5 ms: 1.08x slower                                                       |
| nbody                   | 90.7 ms                                                      | 98.1 ms: 1.08x slower                                                       |
| spectral_norm           | 93.3 ms                                                      | 101 ms: 1.08x slower                                                        |
| comprehensions          | 24.6 us                                                      | 27.1 us: 1.10x slower                                                       |
| Geometric mean          | (ref)                                                        | 1.04x faster                                                                |

Benchmark hidden because not significant (3): dask, pprint_pformat, xml_etree_iterparse
Ignored benchmarks (11) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, tornado_http, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x
