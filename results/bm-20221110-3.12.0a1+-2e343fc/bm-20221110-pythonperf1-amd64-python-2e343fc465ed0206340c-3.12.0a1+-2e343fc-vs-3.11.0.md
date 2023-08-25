
# Results vs. 3.11.0

- fork: python
- ref: 2e343fc465ed0206340c
- machine: windows-amd64
- commit hash: 2e343fc
- commit date: 2022-11-10
- overall geometric mean: 1.04x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20221110-pythonperf1-amd64-python-2e343fc465ed0206340c-3.12.0a1+-2e343fc |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 209 ms                                                      | 198 ms: 1.06x faster                                                        |
| chameleon      | 5.11 ms                                                     | 4.89 ms: 1.05x faster                                                       |
| docutils       | 1.60 sec                                                    | 1.58 sec: 1.01x faster                                                      |
| html5lib       | 37.5 ms                                                     | 35.7 ms: 1.05x faster                                                       |
| tornado_http   | 91.8 ms                                                     | 93.4 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                       | 1.03x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20221110-pythonperf1-amd64-python-2e343fc465ed0206340c-3.12.0a1+-2e343fc |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 70.0 ms                                                     | 63.1 ms: 1.11x faster                                                       |
| float          | 54.6 ms                                                     | 54.1 ms: 1.01x faster                                                       |
| pidigits       | 148 ms                                                      | 151 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                       | 1.03x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20221110-pythonperf1-amd64-python-2e343fc465ed0206340c-3.12.0a1+-2e343fc |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 90.6 ms                                                     | 84.7 ms: 1.07x faster                                                       |
| regex_v8       | 13.8 ms                                                     | 13.5 ms: 1.02x faster                                                       |
| regex_effbot   | 1.50 ms                                                     | 1.58 ms: 1.06x slower                                                       |
| regex_dna      | 115 ms                                                      | 124 ms: 1.08x slower                                                        |
| Geometric mean | (ref)                                                       | 1.01x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20221110-pythonperf1-amd64-python-2e343fc465ed0206340c-3.12.0a1+-2e343fc |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 7.56 ms                                                     | 5.38 ms: 1.41x faster                                                       |
| unpickle_pure_python | 152 us                                                      | 140 us: 1.08x faster                                                        |
| pickle_pure_python   | 200 us                                                      | 190 us: 1.05x faster                                                        |
| xml_etree_parse      | 95.9 ms                                                     | 91.9 ms: 1.04x faster                                                       |
| unpickle             | 8.09 us                                                     | 7.75 us: 1.04x faster                                                       |
| xml_etree_process    | 37.1 ms                                                     | 36.3 ms: 1.02x faster                                                       |
| xml_etree_generate   | 52.2 ms                                                     | 51.6 ms: 1.01x faster                                                       |
| json_loads           | 12.9 us                                                     | 13.1 us: 1.02x slower                                                       |
| xml_etree_iterparse  | 62.6 ms                                                     | 64.5 ms: 1.03x slower                                                       |
| pickle_dict          | 18.5 us                                                     | 19.3 us: 1.04x slower                                                       |
| pickle_list          | 2.68 us                                                     | 2.80 us: 1.05x slower                                                       |
| pickle               | 6.61 us                                                     | 6.96 us: 1.05x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.03x faster                                                                |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20221110-pythonperf1-amd64-python-2e343fc465ed0206340c-3.12.0a1+-2e343fc |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 15.9 ms                                                     | 16.1 ms: 1.01x slower                                                       |
| python_startup         | 18.7 ms                                                     | 18.9 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.01x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20221110-pythonperf1-amd64-python-2e343fc465ed0206340c-3.12.0a1+-2e343fc |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 24.1 ms                                                     | 21.7 ms: 1.11x faster                                                       |
| mako            | 7.26 ms                                                     | 6.55 ms: 1.11x faster                                                       |
| genshi_text     | 17.0 ms                                                     | 15.8 ms: 1.07x faster                                                       |
| genshi_xml      | 37.3 ms                                                     | 35.3 ms: 1.06x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.09x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20221110-pythonperf1-amd64-python-2e343fc465ed0206340c-3.12.0a1+-2e343fc |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpack_sequence         | 46.1 ns                                                     | 32.2 ns: 1.43x faster                                                       |
| json_dumps              | 7.56 ms                                                     | 5.38 ms: 1.41x faster                                                       |
| json                    | 3.25 ms                                                     | 2.76 ms: 1.18x faster                                                       |
| richards                | 30.6 ms                                                     | 27.2 ms: 1.12x faster                                                       |
| raytrace                | 211 ms                                                      | 188 ms: 1.12x faster                                                        |
| django_template         | 24.1 ms                                                     | 21.7 ms: 1.11x faster                                                       |
| nbody                   | 70.0 ms                                                     | 63.1 ms: 1.11x faster                                                       |
| mako                    | 7.26 ms                                                     | 6.55 ms: 1.11x faster                                                       |
| deltablue               | 2.61 ms                                                     | 2.35 ms: 1.11x faster                                                       |
| scimark_sparse_mat_mult | 2.57 ms                                                     | 2.32 ms: 1.11x faster                                                       |
| sqlglot_transpile       | 1.16 ms                                                     | 1.07 ms: 1.09x faster                                                       |
| deepcopy                | 246 us                                                      | 226 us: 1.09x faster                                                        |
| deepcopy_reduce         | 2.07 us                                                     | 1.91 us: 1.09x faster                                                       |
| unpickle_pure_python    | 152 us                                                      | 140 us: 1.08x faster                                                        |
| mdp                     | 1.67 sec                                                    | 1.55 sec: 1.08x faster                                                      |
| sqlglot_parse           | 952 us                                                      | 885 us: 1.08x faster                                                        |
| genshi_text             | 17.0 ms                                                     | 15.8 ms: 1.07x faster                                                       |
| logging_silent          | 69.8 ns                                                     | 65.3 ns: 1.07x faster                                                       |
| regex_compile           | 90.6 ms                                                     | 84.7 ms: 1.07x faster                                                       |
| fannkuch                | 252 ms                                                      | 236 ms: 1.07x faster                                                        |
| go                      | 97.3 ms                                                     | 91.2 ms: 1.07x faster                                                       |
| sqlglot_optimize        | 34.9 ms                                                     | 32.7 ms: 1.07x faster                                                       |
| hexiom                  | 4.55 ms                                                     | 4.28 ms: 1.07x faster                                                       |
| pprint_safe_repr        | 512 ms                                                      | 481 ms: 1.06x faster                                                        |
| meteor_contest          | 74.7 ms                                                     | 70.4 ms: 1.06x faster                                                       |
| 2to3                    | 209 ms                                                      | 198 ms: 1.06x faster                                                        |
| genshi_xml              | 37.3 ms                                                     | 35.3 ms: 1.06x faster                                                       |
| scimark_monte_carlo     | 44.6 ms                                                     | 42.3 ms: 1.05x faster                                                       |
| sympy_expand            | 295 ms                                                      | 280 ms: 1.05x faster                                                        |
| coroutines              | 14.6 ms                                                     | 13.9 ms: 1.05x faster                                                       |
| html5lib                | 37.5 ms                                                     | 35.7 ms: 1.05x faster                                                       |
| pickle_pure_python      | 200 us                                                      | 190 us: 1.05x faster                                                        |
| chameleon               | 5.11 ms                                                     | 4.89 ms: 1.05x faster                                                       |
| coverage                | 55.9 ms                                                     | 53.4 ms: 1.05x faster                                                       |
| sqlglot_normalize       | 190 ms                                                      | 182 ms: 1.05x faster                                                        |
| pyflate                 | 304 ms                                                      | 291 ms: 1.04x faster                                                        |
| deepcopy_memo           | 25.2 us                                                     | 24.1 us: 1.04x faster                                                       |
| xml_etree_parse         | 95.9 ms                                                     | 91.9 ms: 1.04x faster                                                       |
| unpickle                | 8.09 us                                                     | 7.75 us: 1.04x faster                                                       |
| spectral_norm           | 67.9 ms                                                     | 65.3 ms: 1.04x faster                                                       |
| chaos                   | 47.1 ms                                                     | 45.5 ms: 1.04x faster                                                       |
| sympy_integrate         | 13.8 ms                                                     | 13.3 ms: 1.04x faster                                                       |
| pycparser               | 691 ms                                                      | 669 ms: 1.03x faster                                                        |
| nqueens                 | 64.9 ms                                                     | 62.8 ms: 1.03x faster                                                       |
| scimark_sor             | 75.6 ms                                                     | 73.4 ms: 1.03x faster                                                       |
| sympy_str               | 182 ms                                                      | 177 ms: 1.03x faster                                                        |
| sympy_sum               | 99.9 ms                                                     | 97.3 ms: 1.03x faster                                                       |
| regex_v8                | 13.8 ms                                                     | 13.5 ms: 1.02x faster                                                       |
| pprint_pformat          | 1.04 sec                                                    | 1.01 sec: 1.02x faster                                                      |
| create_gc_cycles        | 693 us                                                      | 676 us: 1.02x faster                                                        |
| xml_etree_process       | 37.1 ms                                                     | 36.3 ms: 1.02x faster                                                       |
| comprehensions          | 15.9 us                                                     | 15.6 us: 1.02x faster                                                       |
| mypy2                   | 229 ms                                                      | 225 ms: 1.02x faster                                                        |
| scimark_lu              | 63.5 ms                                                     | 62.4 ms: 1.02x faster                                                       |
| dulwich_log             | 44.5 ms                                                     | 43.9 ms: 1.01x faster                                                       |
| async_generators        | 178 ms                                                      | 175 ms: 1.01x faster                                                        |
| xml_etree_generate      | 52.2 ms                                                     | 51.6 ms: 1.01x faster                                                       |
| docutils                | 1.60 sec                                                    | 1.58 sec: 1.01x faster                                                      |
| float                   | 54.6 ms                                                     | 54.1 ms: 1.01x faster                                                       |
| logging_simple          | 6.61 us                                                     | 6.58 us: 1.01x faster                                                       |
| bench_mp_pool           | 62.5 ms                                                     | 63.2 ms: 1.01x slower                                                       |
| python_startup_no_site  | 15.9 ms                                                     | 16.1 ms: 1.01x slower                                                       |
| python_startup          | 18.7 ms                                                     | 18.9 ms: 1.01x slower                                                       |
| json_loads              | 12.9 us                                                     | 13.1 us: 1.02x slower                                                       |
| tornado_http            | 91.8 ms                                                     | 93.4 ms: 1.02x slower                                                       |
| pidigits                | 148 ms                                                      | 151 ms: 1.02x slower                                                        |
| async_tree_none         | 320 ms                                                      | 330 ms: 1.03x slower                                                        |
| xml_etree_iterparse     | 62.6 ms                                                     | 64.5 ms: 1.03x slower                                                       |
| pickle_dict             | 18.5 us                                                     | 19.3 us: 1.04x slower                                                       |
| pathlib                 | 71.4 ms                                                     | 74.4 ms: 1.04x slower                                                       |
| async_tree_memoization  | 371 ms                                                      | 387 ms: 1.04x slower                                                        |
| pickle_list             | 2.68 us                                                     | 2.80 us: 1.05x slower                                                       |
| pickle                  | 6.61 us                                                     | 6.96 us: 1.05x slower                                                       |
| regex_effbot            | 1.50 ms                                                     | 1.58 ms: 1.06x slower                                                       |
| sqlite_synth            | 1.68 us                                                     | 1.79 us: 1.06x slower                                                       |
| asyncio_tcp             | 699 ms                                                      | 746 ms: 1.07x slower                                                        |
| regex_dna               | 115 ms                                                      | 124 ms: 1.08x slower                                                        |
| Geometric mean          | (ref)                                                       | 1.04x faster                                                                |

Benchmark hidden because not significant (12): thrift, gc_traversal, dask, logging_format, crypto_pyaes, bench_thread_pool, telco, scimark_fft, generators, unpickle_list, async_tree_io, async_tree_cpu_io_mixed
Ignored benchmarks (9) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x
