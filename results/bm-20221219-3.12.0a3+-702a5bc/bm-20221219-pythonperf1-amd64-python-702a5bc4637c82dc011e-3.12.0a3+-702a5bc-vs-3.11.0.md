
# Results vs. 3.11.0

- fork: python
- ref: 702a5bc4637c82dc011e
- machine: windows-amd64
- commit hash: 702a5bc
- commit date: 2022-12-19
- overall geometric mean: 1.06x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20221219-pythonperf1-amd64-python-702a5bc4637c82dc011e-3.12.0a3+-702a5bc |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 209 ms                                                      | 204 ms: 1.02x faster                                                        |
| chameleon      | 5.11 ms                                                     | 4.63 ms: 1.10x faster                                                       |
| html5lib       | 37.5 ms                                                     | 35.6 ms: 1.05x faster                                                       |
| Geometric mean | (ref)                                                       | 1.05x faster                                                                |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20221219-pythonperf1-amd64-python-702a5bc4637c82dc011e-3.12.0a3+-702a5bc |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 70.0 ms                                                     | 63.8 ms: 1.10x faster                                                       |
| float          | 54.6 ms                                                     | 50.3 ms: 1.09x faster                                                       |
| pidigits       | 148 ms                                                      | 146 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                       | 1.07x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20221219-pythonperf1-amd64-python-702a5bc4637c82dc011e-3.12.0a3+-702a5bc |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 13.8 ms                                                     | 13.1 ms: 1.06x faster                                                       |
| regex_compile  | 90.6 ms                                                     | 85.6 ms: 1.06x faster                                                       |
| regex_effbot   | 1.50 ms                                                     | 1.52 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                       | 1.03x faster                                                                |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20221219-pythonperf1-amd64-python-702a5bc4637c82dc011e-3.12.0a3+-702a5bc |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 7.56 ms                                                     | 5.48 ms: 1.38x faster                                                       |
| unpickle_pure_python | 152 us                                                      | 128 us: 1.19x faster                                                        |
| pickle_pure_python   | 200 us                                                      | 183 us: 1.09x faster                                                        |
| xml_etree_parse      | 95.9 ms                                                     | 90.6 ms: 1.06x faster                                                       |
| xml_etree_process    | 37.1 ms                                                     | 35.5 ms: 1.04x faster                                                       |
| xml_etree_generate   | 52.2 ms                                                     | 50.0 ms: 1.04x faster                                                       |
| pickle_dict          | 18.5 us                                                     | 19.0 us: 1.03x slower                                                       |
| unpickle_list        | 2.55 us                                                     | 2.62 us: 1.03x slower                                                       |
| xml_etree_iterparse  | 62.6 ms                                                     | 64.5 ms: 1.03x slower                                                       |
| json_loads           | 12.9 us                                                     | 13.4 us: 1.04x slower                                                       |
| pickle_list          | 2.68 us                                                     | 2.79 us: 1.04x slower                                                       |
| pickle               | 6.61 us                                                     | 6.99 us: 1.06x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.04x faster                                                                |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20221219-pythonperf1-amd64-python-702a5bc4637c82dc011e-3.12.0a3+-702a5bc |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 15.9 ms                                                     | 15.7 ms: 1.01x faster                                                       |
| python_startup         | 18.7 ms                                                     | 18.9 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.00x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20221219-pythonperf1-amd64-python-702a5bc4637c82dc011e-3.12.0a3+-702a5bc |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 17.0 ms                                                     | 14.3 ms: 1.18x faster                                                       |
| mako            | 7.26 ms                                                     | 6.31 ms: 1.15x faster                                                       |
| django_template | 24.1 ms                                                     | 21.8 ms: 1.11x faster                                                       |
| genshi_xml      | 37.3 ms                                                     | 34.2 ms: 1.09x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.13x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20221219-pythonperf1-amd64-python-702a5bc4637c82dc011e-3.12.0a3+-702a5bc |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpack_sequence         | 46.1 ns                                                     | 29.5 ns: 1.56x faster                                                       |
| asyncio_tcp             | 699 ms                                                      | 486 ms: 1.44x faster                                                        |
| json_dumps              | 7.56 ms                                                     | 5.48 ms: 1.38x faster                                                       |
| deltablue               | 2.61 ms                                                     | 2.18 ms: 1.20x faster                                                       |
| unpickle_pure_python    | 152 us                                                      | 128 us: 1.19x faster                                                        |
| genshi_text             | 17.0 ms                                                     | 14.3 ms: 1.18x faster                                                       |
| logging_silent          | 69.8 ns                                                     | 59.1 ns: 1.18x faster                                                       |
| json                    | 3.25 ms                                                     | 2.80 ms: 1.16x faster                                                       |
| deepcopy_memo           | 25.2 us                                                     | 21.7 us: 1.16x faster                                                       |
| richards                | 30.6 ms                                                     | 26.4 ms: 1.16x faster                                                       |
| mako                    | 7.26 ms                                                     | 6.31 ms: 1.15x faster                                                       |
| deepcopy                | 246 us                                                      | 215 us: 1.15x faster                                                        |
| scimark_monte_carlo     | 44.6 ms                                                     | 40.1 ms: 1.11x faster                                                       |
| spectral_norm           | 67.9 ms                                                     | 61.3 ms: 1.11x faster                                                       |
| raytrace                | 211 ms                                                      | 190 ms: 1.11x faster                                                        |
| django_template         | 24.1 ms                                                     | 21.8 ms: 1.11x faster                                                       |
| chameleon               | 5.11 ms                                                     | 4.63 ms: 1.10x faster                                                       |
| hexiom                  | 4.55 ms                                                     | 4.13 ms: 1.10x faster                                                       |
| scimark_lu              | 63.5 ms                                                     | 57.7 ms: 1.10x faster                                                       |
| nbody                   | 70.0 ms                                                     | 63.8 ms: 1.10x faster                                                       |
| go                      | 97.3 ms                                                     | 88.8 ms: 1.10x faster                                                       |
| pickle_pure_python      | 200 us                                                      | 183 us: 1.09x faster                                                        |
| pprint_safe_repr        | 512 ms                                                      | 469 ms: 1.09x faster                                                        |
| pprint_pformat          | 1.04 sec                                                    | 953 ms: 1.09x faster                                                        |
| genshi_xml              | 37.3 ms                                                     | 34.2 ms: 1.09x faster                                                       |
| float                   | 54.6 ms                                                     | 50.3 ms: 1.09x faster                                                       |
| scimark_sparse_mat_mult | 2.57 ms                                                     | 2.37 ms: 1.09x faster                                                       |
| scimark_sor             | 75.6 ms                                                     | 69.9 ms: 1.08x faster                                                       |
| pyflate                 | 304 ms                                                      | 281 ms: 1.08x faster                                                        |
| deepcopy_reduce         | 2.07 us                                                     | 1.92 us: 1.08x faster                                                       |
| fannkuch                | 252 ms                                                      | 233 ms: 1.08x faster                                                        |
| nqueens                 | 64.9 ms                                                     | 60.1 ms: 1.08x faster                                                       |
| mdp                     | 1.67 sec                                                    | 1.55 sec: 1.08x faster                                                      |
| logging_simple          | 6.61 us                                                     | 6.23 us: 1.06x faster                                                       |
| regex_v8                | 13.8 ms                                                     | 13.1 ms: 1.06x faster                                                       |
| dulwich_log             | 44.5 ms                                                     | 42.0 ms: 1.06x faster                                                       |
| regex_compile           | 90.6 ms                                                     | 85.6 ms: 1.06x faster                                                       |
| xml_etree_parse         | 95.9 ms                                                     | 90.6 ms: 1.06x faster                                                       |
| sqlglot_parse           | 952 us                                                      | 900 us: 1.06x faster                                                        |
| sqlglot_transpile       | 1.16 ms                                                     | 1.10 ms: 1.05x faster                                                       |
| html5lib                | 37.5 ms                                                     | 35.6 ms: 1.05x faster                                                       |
| sqlglot_normalize       | 190 ms                                                      | 182 ms: 1.05x faster                                                        |
| xml_etree_process       | 37.1 ms                                                     | 35.5 ms: 1.04x faster                                                       |
| xml_etree_generate      | 52.2 ms                                                     | 50.0 ms: 1.04x faster                                                       |
| sqlglot_optimize        | 34.9 ms                                                     | 33.5 ms: 1.04x faster                                                       |
| sympy_integrate         | 13.8 ms                                                     | 13.3 ms: 1.04x faster                                                       |
| thrift                  | 491 us                                                      | 473 us: 1.04x faster                                                        |
| coverage                | 55.9 ms                                                     | 54.0 ms: 1.03x faster                                                       |
| sympy_expand            | 295 ms                                                      | 286 ms: 1.03x faster                                                        |
| logging_format          | 7.01 us                                                     | 6.82 us: 1.03x faster                                                       |
| mypy2                   | 229 ms                                                      | 223 ms: 1.03x faster                                                        |
| pycparser               | 691 ms                                                      | 675 ms: 1.02x faster                                                        |
| 2to3                    | 209 ms                                                      | 204 ms: 1.02x faster                                                        |
| meteor_contest          | 74.7 ms                                                     | 73.1 ms: 1.02x faster                                                       |
| create_gc_cycles        | 693 us                                                      | 677 us: 1.02x faster                                                        |
| sympy_str               | 182 ms                                                      | 179 ms: 1.02x faster                                                        |
| crypto_pyaes            | 47.6 ms                                                     | 46.8 ms: 1.02x faster                                                       |
| chaos                   | 47.1 ms                                                     | 46.5 ms: 1.01x faster                                                       |
| pidigits                | 148 ms                                                      | 146 ms: 1.01x faster                                                        |
| telco                   | 3.90 ms                                                     | 3.86 ms: 1.01x faster                                                       |
| python_startup_no_site  | 15.9 ms                                                     | 15.7 ms: 1.01x faster                                                       |
| comprehensions          | 15.9 us                                                     | 16.0 us: 1.01x slower                                                       |
| python_startup          | 18.7 ms                                                     | 18.9 ms: 1.01x slower                                                       |
| bench_mp_pool           | 62.5 ms                                                     | 63.2 ms: 1.01x slower                                                       |
| regex_effbot            | 1.50 ms                                                     | 1.52 ms: 1.01x slower                                                       |
| gc_traversal            | 1.46 ms                                                     | 1.48 ms: 1.02x slower                                                       |
| async_generators        | 178 ms                                                      | 181 ms: 1.02x slower                                                        |
| pickle_dict             | 18.5 us                                                     | 19.0 us: 1.03x slower                                                       |
| unpickle_list           | 2.55 us                                                     | 2.62 us: 1.03x slower                                                       |
| xml_etree_iterparse     | 62.6 ms                                                     | 64.5 ms: 1.03x slower                                                       |
| coroutines              | 14.6 ms                                                     | 15.1 ms: 1.03x slower                                                       |
| async_tree_io           | 779 ms                                                      | 807 ms: 1.04x slower                                                        |
| json_loads              | 12.9 us                                                     | 13.4 us: 1.04x slower                                                       |
| async_tree_memoization  | 371 ms                                                      | 386 ms: 1.04x slower                                                        |
| pickle_list             | 2.68 us                                                     | 2.79 us: 1.04x slower                                                       |
| async_tree_none         | 320 ms                                                      | 334 ms: 1.04x slower                                                        |
| pickle                  | 6.61 us                                                     | 6.99 us: 1.06x slower                                                       |
| sqlite_synth            | 1.68 us                                                     | 1.78 us: 1.06x slower                                                       |
| pathlib                 | 71.4 ms                                                     | 75.7 ms: 1.06x slower                                                       |
| generators              | 33.8 ms                                                     | 38.7 ms: 1.15x slower                                                       |
| Geometric mean          | (ref)                                                       | 1.06x faster                                                                |

Benchmark hidden because not significant (8): dask, unpickle, docutils, async_tree_cpu_io_mixed, sympy_sum, regex_dna, bench_thread_pool, scimark_fft
Ignored benchmarks (10) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, tornado_http, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x
