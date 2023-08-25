
# Results vs. 3.11.0

- fork: python
- ref: f883b7f8ee3209b52863
- machine: windows-amd64
- commit hash: f883b7f
- commit date: 2022-11-10
- overall geometric mean: 1.03x faster \*
- HPT reliability: 99.99%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20221110-pythonperf1-amd64-python-f883b7f8ee3209b52863-3.12.0a1+-f883b7f |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 209 ms                                                      | 200 ms: 1.05x faster                                                        |
| chameleon      | 5.11 ms                                                     | 4.97 ms: 1.03x faster                                                       |
| html5lib       | 37.5 ms                                                     | 36.2 ms: 1.04x faster                                                       |
| tornado_http   | 91.8 ms                                                     | 93.2 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                       | 1.02x faster                                                                |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20221110-pythonperf1-amd64-python-f883b7f8ee3209b52863-3.12.0a1+-f883b7f |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 70.0 ms                                                     | 62.7 ms: 1.12x faster                                                       |
| float          | 54.6 ms                                                     | 52.3 ms: 1.04x faster                                                       |
| pidigits       | 148 ms                                                      | 150 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                       | 1.05x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20221110-pythonperf1-amd64-python-f883b7f8ee3209b52863-3.12.0a1+-f883b7f |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 90.6 ms                                                     | 87.2 ms: 1.04x faster                                                       |
| regex_v8       | 13.8 ms                                                     | 14.0 ms: 1.01x slower                                                       |
| regex_dna      | 115 ms                                                      | 122 ms: 1.06x slower                                                        |
| regex_effbot   | 1.50 ms                                                     | 1.60 ms: 1.07x slower                                                       |
| Geometric mean | (ref)                                                       | 1.02x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20221110-pythonperf1-amd64-python-f883b7f8ee3209b52863-3.12.0a1+-f883b7f |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 7.56 ms                                                     | 5.48 ms: 1.38x faster                                                       |
| xml_etree_parse      | 95.9 ms                                                     | 90.9 ms: 1.06x faster                                                       |
| pickle_pure_python   | 200 us                                                      | 190 us: 1.06x faster                                                        |
| unpickle_pure_python | 152 us                                                      | 148 us: 1.02x faster                                                        |
| xml_etree_process    | 37.1 ms                                                     | 36.6 ms: 1.01x faster                                                       |
| json_loads           | 12.9 us                                                     | 13.1 us: 1.02x slower                                                       |
| unpickle_list        | 2.55 us                                                     | 2.60 us: 1.02x slower                                                       |
| xml_etree_iterparse  | 62.6 ms                                                     | 63.9 ms: 1.02x slower                                                       |
| pickle_dict          | 18.5 us                                                     | 19.1 us: 1.03x slower                                                       |
| pickle_list          | 2.68 us                                                     | 2.82 us: 1.05x slower                                                       |
| pickle               | 6.61 us                                                     | 7.14 us: 1.08x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.02x faster                                                                |

Benchmark hidden because not significant (2): unpickle, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20221110-pythonperf1-amd64-python-f883b7f8ee3209b52863-3.12.0a1+-f883b7f |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup | 18.7 ms                                                     | 18.9 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                       | 1.00x slower                                                                |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20221110-pythonperf1-amd64-python-f883b7f8ee3209b52863-3.12.0a1+-f883b7f |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.26 ms                                                     | 6.58 ms: 1.10x faster                                                       |
| django_template | 24.1 ms                                                     | 22.1 ms: 1.09x faster                                                       |
| genshi_text     | 17.0 ms                                                     | 16.3 ms: 1.04x faster                                                       |
| genshi_xml      | 37.3 ms                                                     | 35.9 ms: 1.04x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.07x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20221110-pythonperf1-amd64-python-f883b7f8ee3209b52863-3.12.0a1+-f883b7f |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpack_sequence         | 46.1 ns                                                     | 32.4 ns: 1.42x faster                                                       |
| json_dumps              | 7.56 ms                                                     | 5.48 ms: 1.38x faster                                                       |
| json                    | 3.25 ms                                                     | 2.70 ms: 1.20x faster                                                       |
| richards                | 30.6 ms                                                     | 26.8 ms: 1.14x faster                                                       |
| nbody                   | 70.0 ms                                                     | 62.7 ms: 1.12x faster                                                       |
| raytrace                | 211 ms                                                      | 190 ms: 1.11x faster                                                        |
| mako                    | 7.26 ms                                                     | 6.58 ms: 1.10x faster                                                       |
| deltablue               | 2.61 ms                                                     | 2.37 ms: 1.10x faster                                                       |
| scimark_sparse_mat_mult | 2.57 ms                                                     | 2.36 ms: 1.09x faster                                                       |
| logging_silent          | 69.8 ns                                                     | 64.1 ns: 1.09x faster                                                       |
| django_template         | 24.1 ms                                                     | 22.1 ms: 1.09x faster                                                       |
| go                      | 97.3 ms                                                     | 89.7 ms: 1.09x faster                                                       |
| scimark_monte_carlo     | 44.6 ms                                                     | 41.3 ms: 1.08x faster                                                       |
| sqlglot_optimize        | 34.9 ms                                                     | 32.6 ms: 1.07x faster                                                       |
| sqlglot_transpile       | 1.16 ms                                                     | 1.09 ms: 1.07x faster                                                       |
| mdp                     | 1.67 sec                                                    | 1.57 sec: 1.06x faster                                                      |
| meteor_contest          | 74.7 ms                                                     | 70.5 ms: 1.06x faster                                                       |
| xml_etree_parse         | 95.9 ms                                                     | 90.9 ms: 1.06x faster                                                       |
| pickle_pure_python      | 200 us                                                      | 190 us: 1.06x faster                                                        |
| pprint_safe_repr        | 512 ms                                                      | 485 ms: 1.05x faster                                                        |
| nqueens                 | 64.9 ms                                                     | 61.8 ms: 1.05x faster                                                       |
| crypto_pyaes            | 47.6 ms                                                     | 45.3 ms: 1.05x faster                                                       |
| hexiom                  | 4.55 ms                                                     | 4.34 ms: 1.05x faster                                                       |
| pyflate                 | 304 ms                                                      | 290 ms: 1.05x faster                                                        |
| 2to3                    | 209 ms                                                      | 200 ms: 1.05x faster                                                        |
| float                   | 54.6 ms                                                     | 52.3 ms: 1.04x faster                                                       |
| genshi_text             | 17.0 ms                                                     | 16.3 ms: 1.04x faster                                                       |
| genshi_xml              | 37.3 ms                                                     | 35.9 ms: 1.04x faster                                                       |
| regex_compile           | 90.6 ms                                                     | 87.2 ms: 1.04x faster                                                       |
| scimark_fft             | 178 ms                                                      | 172 ms: 1.04x faster                                                        |
| sympy_integrate         | 13.8 ms                                                     | 13.3 ms: 1.04x faster                                                       |
| chaos                   | 47.1 ms                                                     | 45.4 ms: 1.04x faster                                                       |
| sqlglot_normalize       | 190 ms                                                      | 184 ms: 1.04x faster                                                        |
| html5lib                | 37.5 ms                                                     | 36.2 ms: 1.04x faster                                                       |
| sympy_expand            | 295 ms                                                      | 285 ms: 1.03x faster                                                        |
| pycparser               | 691 ms                                                      | 669 ms: 1.03x faster                                                        |
| coverage                | 55.9 ms                                                     | 54.2 ms: 1.03x faster                                                       |
| sqlglot_parse           | 952 us                                                      | 924 us: 1.03x faster                                                        |
| chameleon               | 5.11 ms                                                     | 4.97 ms: 1.03x faster                                                       |
| pprint_pformat          | 1.04 sec                                                    | 1.01 sec: 1.03x faster                                                      |
| scimark_sor             | 75.6 ms                                                     | 73.7 ms: 1.03x faster                                                       |
| sympy_sum               | 99.9 ms                                                     | 97.5 ms: 1.02x faster                                                       |
| thrift                  | 491 us                                                      | 479 us: 1.02x faster                                                        |
| unpickle_pure_python    | 152 us                                                      | 148 us: 1.02x faster                                                        |
| fannkuch                | 252 ms                                                      | 247 ms: 1.02x faster                                                        |
| deepcopy_memo           | 25.2 us                                                     | 24.7 us: 1.02x faster                                                       |
| deepcopy_reduce         | 2.07 us                                                     | 2.03 us: 1.02x faster                                                       |
| scimark_lu              | 63.5 ms                                                     | 62.4 ms: 1.02x faster                                                       |
| mypy2                   | 229 ms                                                      | 225 ms: 1.02x faster                                                        |
| deepcopy                | 246 us                                                      | 241 us: 1.02x faster                                                        |
| dulwich_log             | 44.5 ms                                                     | 43.8 ms: 1.02x faster                                                       |
| xml_etree_process       | 37.1 ms                                                     | 36.6 ms: 1.01x faster                                                       |
| telco                   | 3.90 ms                                                     | 3.86 ms: 1.01x faster                                                       |
| python_startup          | 18.7 ms                                                     | 18.9 ms: 1.01x slower                                                       |
| regex_v8                | 13.8 ms                                                     | 14.0 ms: 1.01x slower                                                       |
| bench_mp_pool           | 62.5 ms                                                     | 63.2 ms: 1.01x slower                                                       |
| pidigits                | 148 ms                                                      | 150 ms: 1.01x slower                                                        |
| gc_traversal            | 1.46 ms                                                     | 1.48 ms: 1.01x slower                                                       |
| tornado_http            | 91.8 ms                                                     | 93.2 ms: 1.01x slower                                                       |
| dask                    | 264 ms                                                      | 268 ms: 1.02x slower                                                        |
| async_tree_cpu_io_mixed | 501 ms                                                      | 510 ms: 1.02x slower                                                        |
| json_loads              | 12.9 us                                                     | 13.1 us: 1.02x slower                                                       |
| unpickle_list           | 2.55 us                                                     | 2.60 us: 1.02x slower                                                       |
| xml_etree_iterparse     | 62.6 ms                                                     | 63.9 ms: 1.02x slower                                                       |
| async_tree_none         | 320 ms                                                      | 330 ms: 1.03x slower                                                        |
| pathlib                 | 71.4 ms                                                     | 73.5 ms: 1.03x slower                                                       |
| pickle_dict             | 18.5 us                                                     | 19.1 us: 1.03x slower                                                       |
| async_tree_memoization  | 371 ms                                                      | 389 ms: 1.05x slower                                                        |
| pickle_list             | 2.68 us                                                     | 2.82 us: 1.05x slower                                                       |
| regex_dna               | 115 ms                                                      | 122 ms: 1.06x slower                                                        |
| sqlite_synth            | 1.68 us                                                     | 1.79 us: 1.07x slower                                                       |
| regex_effbot            | 1.50 ms                                                     | 1.60 ms: 1.07x slower                                                       |
| pickle                  | 6.61 us                                                     | 7.14 us: 1.08x slower                                                       |
| Geometric mean          | (ref)                                                       | 1.03x faster                                                                |

Benchmark hidden because not significant (16): bench_thread_pool, coroutines, create_gc_cycles, spectral_norm, docutils, generators, unpickle, python_startup_no_site, logging_simple, async_generators, comprehensions, xml_etree_generate, async_tree_io, sympy_str, logging_format, asyncio_tcp
Ignored benchmarks (9) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x
