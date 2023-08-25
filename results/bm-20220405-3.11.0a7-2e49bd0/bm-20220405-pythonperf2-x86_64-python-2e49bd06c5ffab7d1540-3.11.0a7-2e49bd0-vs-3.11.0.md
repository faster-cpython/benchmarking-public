
# Results vs. 3.11.0

- fork: python
- ref: 2e49bd06c5ffab7d1540
- machine: linux-x86_64
- commit hash: 2e49bd0
- commit date: 2022-04-05
- overall geometric mean: 1.02x slower \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220405-pythonperf2-x86_64-python-2e49bd06c5ffab7d1540-3.11.0a7-2e49bd0 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 288 ms                                                       | 293 ms: 1.02x slower                                                        |
| chameleon      | 7.67 ms                                                      | 7.97 ms: 1.04x slower                                                       |
| docutils       | 2.86 sec                                                     | 2.92 sec: 1.02x slower                                                      |
| html5lib       | 72.9 ms                                                      | 75.0 ms: 1.03x slower                                                       |
| tornado_http   | 122 ms                                                       | 123 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                        | 1.02x slower                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220405-pythonperf2-x86_64-python-2e49bd06c5ffab7d1540-3.11.0a7-2e49bd0 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 90.7 ms                                                      | 93.6 ms: 1.03x slower                                                       |
| float          | 74.2 ms                                                      | 78.4 ms: 1.06x slower                                                       |
| Geometric mean | (ref)                                                        | 1.03x slower                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220405-pythonperf2-x86_64-python-2e49bd06c5ffab7d1540-3.11.0a7-2e49bd0 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.50 ms                                                      | 3.13 ms: 1.12x faster                                                       |
| regex_compile  | 158 ms                                                       | 159 ms: 1.01x slower                                                        |
| regex_v8       | 23.9 ms                                                      | 26.6 ms: 1.11x slower                                                       |
| regex_dna      | 227 ms                                                       | 253 ms: 1.11x slower                                                        |
| Geometric mean | (ref)                                                        | 1.03x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220405-pythonperf2-x86_64-python-2e49bd06c5ffab7d1540-3.11.0a7-2e49bd0 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_loads           | 28.7 us                                                      | 24.5 us: 1.17x faster                                                       |
| unpickle             | 13.4 us                                                      | 13.0 us: 1.03x faster                                                       |
| unpickle_pure_python | 241 us                                                       | 242 us: 1.01x slower                                                        |
| json_dumps           | 13.4 ms                                                      | 13.5 ms: 1.01x slower                                                       |
| pickle_dict          | 30.8 us                                                      | 31.1 us: 1.01x slower                                                       |
| xml_etree_iterparse  | 104 ms                                                       | 106 ms: 1.01x slower                                                        |
| pickle               | 9.64 us                                                      | 9.88 us: 1.03x slower                                                       |
| xml_etree_generate   | 80.5 ms                                                      | 82.8 ms: 1.03x slower                                                       |
| xml_etree_process    | 56.5 ms                                                      | 58.3 ms: 1.03x slower                                                       |
| pickle_pure_python   | 319 us                                                       | 331 us: 1.04x slower                                                        |
| pickle_list          | 3.83 us                                                      | 4.12 us: 1.08x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.00x slower                                                                |

Benchmark hidden because not significant (2): xml_etree_parse, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220405-pythonperf2-x86_64-python-2e49bd06c5ffab7d1540-3.11.0a7-2e49bd0 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 7.76 ms                                                      | 7.46 ms: 1.04x faster                                                       |
| python_startup         | 10.8 ms                                                      | 10.4 ms: 1.04x faster                                                       |
| Geometric mean         | (ref)                                                        | 1.04x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220405-pythonperf2-x86_64-python-2e49bd06c5ffab7d1540-3.11.0a7-2e49bd0 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml     | 58.5 ms                                                      | 59.7 ms: 1.02x slower                                                       |
| mako           | 11.0 ms                                                      | 11.2 ms: 1.02x slower                                                       |
| genshi_text    | 26.1 ms                                                      | 26.8 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                        | 1.02x slower                                                                |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220405-pythonperf2-x86_64-python-2e49bd06c5ffab7d1540-3.11.0a7-2e49bd0 |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_loads              | 28.7 us                                                      | 24.5 us: 1.17x faster                                                       |
| dask                    | 410 ms                                                       | 367 ms: 1.12x faster                                                        |
| regex_effbot            | 3.50 ms                                                      | 3.13 ms: 1.12x faster                                                       |
| chaos                   | 80.9 ms                                                      | 73.4 ms: 1.10x faster                                                       |
| json                    | 5.65 ms                                                      | 5.17 ms: 1.09x faster                                                       |
| logging_simple          | 7.19 us                                                      | 6.69 us: 1.07x faster                                                       |
| gc_traversal            | 3.85 ms                                                      | 3.58 ms: 1.07x faster                                                       |
| logging_format          | 8.11 us                                                      | 7.59 us: 1.07x faster                                                       |
| sympy_sum               | 185 ms                                                       | 177 ms: 1.04x faster                                                        |
| python_startup_no_site  | 7.76 ms                                                      | 7.46 ms: 1.04x faster                                                       |
| python_startup          | 10.8 ms                                                      | 10.4 ms: 1.04x faster                                                       |
| deepcopy                | 399 us                                                       | 385 us: 1.04x faster                                                        |
| unpickle                | 13.4 us                                                      | 13.0 us: 1.03x faster                                                       |
| generators              | 56.0 ms                                                      | 54.7 ms: 1.02x faster                                                       |
| sympy_str               | 337 ms                                                       | 330 ms: 1.02x faster                                                        |
| sympy_integrate         | 25.8 ms                                                      | 25.3 ms: 1.02x faster                                                       |
| deepcopy_reduce         | 3.51 us                                                      | 3.48 us: 1.01x faster                                                       |
| telco                   | 6.86 ms                                                      | 6.79 ms: 1.01x faster                                                       |
| sympy_expand            | 555 ms                                                       | 549 ms: 1.01x faster                                                        |
| asyncio_tcp             | 753 ms                                                       | 746 ms: 1.01x faster                                                        |
| aiohttp                 | 985 us                                                       | 978 us: 1.01x faster                                                        |
| mdp                     | 2.75 sec                                                     | 2.76 sec: 1.00x slower                                                      |
| sqlglot_normalize       | 126 ms                                                       | 127 ms: 1.00x slower                                                        |
| async_tree_cpu_io_mixed | 749 ms                                                       | 753 ms: 1.01x slower                                                        |
| async_tree_none         | 519 ms                                                       | 523 ms: 1.01x slower                                                        |
| regex_compile           | 158 ms                                                       | 159 ms: 1.01x slower                                                        |
| unpickle_pure_python    | 241 us                                                       | 242 us: 1.01x slower                                                        |
| json_dumps              | 13.4 ms                                                      | 13.5 ms: 1.01x slower                                                       |
| async_generators        | 316 ms                                                       | 319 ms: 1.01x slower                                                        |
| pickle_dict             | 30.8 us                                                      | 31.1 us: 1.01x slower                                                       |
| flaskblogging           | 3.88 ms                                                      | 3.92 ms: 1.01x slower                                                       |
| scimark_sor             | 111 ms                                                       | 112 ms: 1.01x slower                                                        |
| xml_etree_iterparse     | 104 ms                                                       | 106 ms: 1.01x slower                                                        |
| tornado_http            | 122 ms                                                       | 123 ms: 1.01x slower                                                        |
| pathlib                 | 19.1 ms                                                      | 19.3 ms: 1.01x slower                                                       |
| go                      | 164 ms                                                       | 166 ms: 1.02x slower                                                        |
| async_tree_memoization  | 630 ms                                                       | 641 ms: 1.02x slower                                                        |
| raytrace                | 317 ms                                                       | 322 ms: 1.02x slower                                                        |
| 2to3                    | 288 ms                                                       | 293 ms: 1.02x slower                                                        |
| meteor_contest          | 131 ms                                                       | 133 ms: 1.02x slower                                                        |
| genshi_xml              | 58.5 ms                                                      | 59.7 ms: 1.02x slower                                                       |
| dulwich_log             | 68.4 ms                                                      | 69.8 ms: 1.02x slower                                                       |
| docutils                | 2.86 sec                                                     | 2.92 sec: 1.02x slower                                                      |
| mako                    | 11.0 ms                                                      | 11.2 ms: 1.02x slower                                                       |
| create_gc_cycles        | 1.61 ms                                                      | 1.65 ms: 1.02x slower                                                       |
| sqlalchemy_imperative   | 20.1 ms                                                      | 20.5 ms: 1.02x slower                                                       |
| pickle                  | 9.64 us                                                      | 9.88 us: 1.03x slower                                                       |
| genshi_text             | 26.1 ms                                                      | 26.8 ms: 1.03x slower                                                       |
| xml_etree_generate      | 80.5 ms                                                      | 82.8 ms: 1.03x slower                                                       |
| html5lib                | 72.9 ms                                                      | 75.0 ms: 1.03x slower                                                       |
| fannkuch                | 429 ms                                                       | 442 ms: 1.03x slower                                                        |
| nbody                   | 90.7 ms                                                      | 93.6 ms: 1.03x slower                                                       |
| xml_etree_process       | 56.5 ms                                                      | 58.3 ms: 1.03x slower                                                       |
| pyflate                 | 449 ms                                                       | 464 ms: 1.03x slower                                                        |
| unpack_sequence         | 45.6 ns                                                      | 47.3 ns: 1.04x slower                                                       |
| sqlglot_optimize        | 59.8 ms                                                      | 61.9 ms: 1.04x slower                                                       |
| logging_silent          | 101 ns                                                       | 105 ns: 1.04x slower                                                        |
| pprint_pformat          | 1.63 sec                                                     | 1.69 sec: 1.04x slower                                                      |
| pickle_pure_python      | 319 us                                                       | 331 us: 1.04x slower                                                        |
| sqlalchemy_declarative  | 154 ms                                                       | 160 ms: 1.04x slower                                                        |
| chameleon               | 7.67 ms                                                      | 7.97 ms: 1.04x slower                                                       |
| scimark_fft             | 285 ms                                                       | 297 ms: 1.04x slower                                                        |
| pprint_safe_repr        | 784 ms                                                       | 818 ms: 1.04x slower                                                        |
| scimark_lu              | 115 ms                                                       | 120 ms: 1.05x slower                                                        |
| coroutines              | 27.6 ms                                                      | 29.0 ms: 1.05x slower                                                       |
| float                   | 74.2 ms                                                      | 78.4 ms: 1.06x slower                                                       |
| deltablue               | 4.00 ms                                                      | 4.23 ms: 1.06x slower                                                       |
| crypto_pyaes            | 83.4 ms                                                      | 89.5 ms: 1.07x slower                                                       |
| hexiom                  | 7.13 ms                                                      | 7.66 ms: 1.07x slower                                                       |
| pickle_list             | 3.83 us                                                      | 4.12 us: 1.08x slower                                                       |
| richards                | 48.3 ms                                                      | 52.8 ms: 1.09x slower                                                       |
| scimark_sparse_mat_mult | 4.05 ms                                                      | 4.51 ms: 1.11x slower                                                       |
| regex_v8                | 23.9 ms                                                      | 26.6 ms: 1.11x slower                                                       |
| regex_dna               | 227 ms                                                       | 253 ms: 1.11x slower                                                        |
| scimark_monte_carlo     | 68.2 ms                                                      | 77.1 ms: 1.13x slower                                                       |
| comprehensions          | 24.6 us                                                      | 27.8 us: 1.13x slower                                                       |
| spectral_norm           | 93.3 ms                                                      | 107 ms: 1.15x slower                                                        |
| sqlglot_transpile       | 1.92 ms                                                      | 2.38 ms: 1.24x slower                                                       |
| sqlglot_parse           | 1.53 ms                                                      | 2.04 ms: 1.33x slower                                                       |
| Geometric mean          | (ref)                                                        | 1.02x slower                                                                |

Benchmark hidden because not significant (15): xml_etree_parse, nqueens, bench_mp_pool, gunicorn, unpickle_list, pidigits, deepcopy_memo, pycparser, mypy2, async_tree_io, thrift, pylint, bench_thread_pool, sqlite_synth, django_template
Ignored benchmarks (5) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, coverage, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x
