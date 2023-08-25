
# Results vs. 3.11.0

- fork: python
- ref: c03e05c2e72f3ea5e797
- machine: windows-amd64
- commit hash: c03e05c
- commit date: 2022-11-09
- overall geometric mean: 1.02x slower \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20221109-pythonperf1-amd64-python-c03e05c2e72f3ea5e797-3.12.0a1+-c03e05c |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| chameleon      | 5.11 ms                                                     | 5.20 ms: 1.02x slower                                                       |
| docutils       | 1.60 sec                                                    | 1.63 sec: 1.02x slower                                                      |
| html5lib       | 37.5 ms                                                     | 39.9 ms: 1.06x slower                                                       |
| Geometric mean | (ref)                                                       | 1.02x slower                                                                |

Benchmark hidden because not significant (2): 2to3, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20221109-pythonperf1-amd64-python-c03e05c2e72f3ea5e797-3.12.0a1+-c03e05c |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 70.0 ms                                                     | 71.3 ms: 1.02x slower                                                       |
| pidigits       | 148 ms                                                      | 151 ms: 1.02x slower                                                        |
| float          | 54.6 ms                                                     | 55.8 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                       | 1.02x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20221109-pythonperf1-amd64-python-c03e05c2e72f3ea5e797-3.12.0a1+-c03e05c |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 13.8 ms                                                     | 13.1 ms: 1.06x faster                                                       |
| regex_compile  | 90.6 ms                                                     | 89.9 ms: 1.01x faster                                                       |
| regex_dna      | 115 ms                                                      | 118 ms: 1.02x slower                                                        |
| regex_effbot   | 1.50 ms                                                     | 1.56 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                       | 1.00x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20221109-pythonperf1-amd64-python-c03e05c2e72f3ea5e797-3.12.0a1+-c03e05c |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 7.56 ms                                                     | 5.54 ms: 1.36x faster                                                       |
| xml_etree_parse      | 95.9 ms                                                     | 89.7 ms: 1.07x faster                                                       |
| json_loads           | 12.9 us                                                     | 13.0 us: 1.01x slower                                                       |
| unpickle_pure_python | 152 us                                                      | 154 us: 1.01x slower                                                        |
| xml_etree_process    | 37.1 ms                                                     | 37.8 ms: 1.02x slower                                                       |
| pickle_list          | 2.68 us                                                     | 2.76 us: 1.03x slower                                                       |
| xml_etree_generate   | 52.2 ms                                                     | 53.9 ms: 1.03x slower                                                       |
| pickle_dict          | 18.5 us                                                     | 19.1 us: 1.03x slower                                                       |
| pickle_pure_python   | 200 us                                                      | 208 us: 1.04x slower                                                        |
| xml_etree_iterparse  | 62.6 ms                                                     | 65.2 ms: 1.04x slower                                                       |
| pickle               | 6.61 us                                                     | 7.06 us: 1.07x slower                                                       |
| unpickle_list        | 2.55 us                                                     | 2.78 us: 1.09x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.00x faster                                                                |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20221109-pythonperf1-amd64-python-c03e05c2e72f3ea5e797-3.12.0a1+-c03e05c |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 18.7 ms                                                     | 19.3 ms: 1.03x slower                                                       |
| python_startup_no_site | 15.9 ms                                                     | 16.4 ms: 1.03x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.03x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20221109-pythonperf1-amd64-python-c03e05c2e72f3ea5e797-3.12.0a1+-c03e05c |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.26 ms                                                     | 7.18 ms: 1.01x faster                                                       |
| django_template | 24.1 ms                                                     | 24.4 ms: 1.01x slower                                                       |
| genshi_xml      | 37.3 ms                                                     | 38.8 ms: 1.04x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.01x slower                                                                |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20221109-pythonperf1-amd64-python-c03e05c2e72f3ea5e797-3.12.0a1+-c03e05c |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps              | 7.56 ms                                                     | 5.54 ms: 1.36x faster                                                       |
| json                    | 3.25 ms                                                     | 2.74 ms: 1.19x faster                                                       |
| unpack_sequence         | 46.1 ns                                                     | 39.2 ns: 1.18x faster                                                       |
| xml_etree_parse         | 95.9 ms                                                     | 89.7 ms: 1.07x faster                                                       |
| dulwich_log             | 44.5 ms                                                     | 41.6 ms: 1.07x faster                                                       |
| regex_v8                | 13.8 ms                                                     | 13.1 ms: 1.06x faster                                                       |
| scimark_sparse_mat_mult | 2.57 ms                                                     | 2.43 ms: 1.06x faster                                                       |
| raytrace                | 211 ms                                                      | 203 ms: 1.04x faster                                                        |
| meteor_contest          | 74.7 ms                                                     | 72.0 ms: 1.04x faster                                                       |
| create_gc_cycles        | 693 us                                                      | 672 us: 1.03x faster                                                        |
| mypy2                   | 229 ms                                                      | 224 ms: 1.02x faster                                                        |
| coverage                | 55.9 ms                                                     | 55.0 ms: 1.02x faster                                                       |
| sympy_integrate         | 13.8 ms                                                     | 13.6 ms: 1.01x faster                                                       |
| mako                    | 7.26 ms                                                     | 7.18 ms: 1.01x faster                                                       |
| pprint_safe_repr        | 512 ms                                                      | 506 ms: 1.01x faster                                                        |
| deltablue               | 2.61 ms                                                     | 2.59 ms: 1.01x faster                                                       |
| regex_compile           | 90.6 ms                                                     | 89.9 ms: 1.01x faster                                                       |
| sqlglot_transpile       | 1.16 ms                                                     | 1.16 ms: 1.01x faster                                                       |
| json_loads              | 12.9 us                                                     | 13.0 us: 1.01x slower                                                       |
| telco                   | 3.90 ms                                                     | 3.95 ms: 1.01x slower                                                       |
| django_template         | 24.1 ms                                                     | 24.4 ms: 1.01x slower                                                       |
| thrift                  | 491 us                                                      | 497 us: 1.01x slower                                                        |
| unpickle_pure_python    | 152 us                                                      | 154 us: 1.01x slower                                                        |
| sympy_sum               | 99.9 ms                                                     | 101 ms: 1.02x slower                                                        |
| sqlglot_optimize        | 34.9 ms                                                     | 35.4 ms: 1.02x slower                                                       |
| pprint_pformat          | 1.04 sec                                                    | 1.06 sec: 1.02x slower                                                      |
| chameleon               | 5.11 ms                                                     | 5.20 ms: 1.02x slower                                                       |
| deepcopy_reduce         | 2.07 us                                                     | 2.11 us: 1.02x slower                                                       |
| nbody                   | 70.0 ms                                                     | 71.3 ms: 1.02x slower                                                       |
| bench_thread_pool       | 852 us                                                      | 868 us: 1.02x slower                                                        |
| pidigits                | 148 ms                                                      | 151 ms: 1.02x slower                                                        |
| docutils                | 1.60 sec                                                    | 1.63 sec: 1.02x slower                                                      |
| deepcopy_memo           | 25.2 us                                                     | 25.7 us: 1.02x slower                                                       |
| dask                    | 264 ms                                                      | 270 ms: 1.02x slower                                                        |
| xml_etree_process       | 37.1 ms                                                     | 37.8 ms: 1.02x slower                                                       |
| mdp                     | 1.67 sec                                                    | 1.70 sec: 1.02x slower                                                      |
| regex_dna               | 115 ms                                                      | 118 ms: 1.02x slower                                                        |
| generators              | 33.8 ms                                                     | 34.5 ms: 1.02x slower                                                       |
| float                   | 54.6 ms                                                     | 55.8 ms: 1.02x slower                                                       |
| crypto_pyaes            | 47.6 ms                                                     | 48.6 ms: 1.02x slower                                                       |
| pyflate                 | 304 ms                                                      | 311 ms: 1.02x slower                                                        |
| sqlglot_normalize       | 190 ms                                                      | 196 ms: 1.03x slower                                                        |
| pycparser               | 691 ms                                                      | 711 ms: 1.03x slower                                                        |
| richards                | 30.6 ms                                                     | 31.5 ms: 1.03x slower                                                       |
| sympy_str               | 182 ms                                                      | 188 ms: 1.03x slower                                                        |
| logging_silent          | 69.8 ns                                                     | 72.0 ns: 1.03x slower                                                       |
| pickle_list             | 2.68 us                                                     | 2.76 us: 1.03x slower                                                       |
| async_tree_cpu_io_mixed | 501 ms                                                      | 517 ms: 1.03x slower                                                        |
| coroutines              | 14.6 ms                                                     | 15.1 ms: 1.03x slower                                                       |
| xml_etree_generate      | 52.2 ms                                                     | 53.9 ms: 1.03x slower                                                       |
| nqueens                 | 64.9 ms                                                     | 67.1 ms: 1.03x slower                                                       |
| python_startup          | 18.7 ms                                                     | 19.3 ms: 1.03x slower                                                       |
| pickle_dict             | 18.5 us                                                     | 19.1 us: 1.03x slower                                                       |
| python_startup_no_site  | 15.9 ms                                                     | 16.4 ms: 1.03x slower                                                       |
| spectral_norm           | 67.9 ms                                                     | 70.5 ms: 1.04x slower                                                       |
| pickle_pure_python      | 200 us                                                      | 208 us: 1.04x slower                                                        |
| deepcopy                | 246 us                                                      | 255 us: 1.04x slower                                                        |
| pathlib                 | 71.4 ms                                                     | 74.2 ms: 1.04x slower                                                       |
| genshi_xml              | 37.3 ms                                                     | 38.8 ms: 1.04x slower                                                       |
| xml_etree_iterparse     | 62.6 ms                                                     | 65.2 ms: 1.04x slower                                                       |
| chaos                   | 47.1 ms                                                     | 49.1 ms: 1.04x slower                                                       |
| regex_effbot            | 1.50 ms                                                     | 1.56 ms: 1.04x slower                                                       |
| async_tree_none         | 320 ms                                                      | 338 ms: 1.06x slower                                                        |
| logging_format          | 7.01 us                                                     | 7.41 us: 1.06x slower                                                       |
| async_generators        | 178 ms                                                      | 188 ms: 1.06x slower                                                        |
| scimark_sor             | 75.6 ms                                                     | 80.1 ms: 1.06x slower                                                       |
| scimark_fft             | 178 ms                                                      | 189 ms: 1.06x slower                                                        |
| async_tree_io           | 779 ms                                                      | 827 ms: 1.06x slower                                                        |
| scimark_monte_carlo     | 44.6 ms                                                     | 47.5 ms: 1.06x slower                                                       |
| html5lib                | 37.5 ms                                                     | 39.9 ms: 1.06x slower                                                       |
| logging_simple          | 6.61 us                                                     | 7.05 us: 1.07x slower                                                       |
| scimark_lu              | 63.5 ms                                                     | 67.9 ms: 1.07x slower                                                       |
| pickle                  | 6.61 us                                                     | 7.06 us: 1.07x slower                                                       |
| fannkuch                | 252 ms                                                      | 270 ms: 1.07x slower                                                        |
| sqlite_synth            | 1.68 us                                                     | 1.80 us: 1.07x slower                                                       |
| go                      | 97.3 ms                                                     | 105 ms: 1.08x slower                                                        |
| comprehensions          | 15.9 us                                                     | 17.1 us: 1.08x slower                                                       |
| bench_mp_pool           | 62.5 ms                                                     | 67.3 ms: 1.08x slower                                                       |
| asyncio_tcp             | 699 ms                                                      | 753 ms: 1.08x slower                                                        |
| async_tree_memoization  | 371 ms                                                      | 402 ms: 1.08x slower                                                        |
| hexiom                  | 4.55 ms                                                     | 4.95 ms: 1.09x slower                                                       |
| unpickle_list           | 2.55 us                                                     | 2.78 us: 1.09x slower                                                       |
| Geometric mean          | (ref)                                                       | 1.02x slower                                                                |

Benchmark hidden because not significant (7): gc_traversal, genshi_text, 2to3, sqlglot_parse, sympy_expand, tornado_http, unpickle
Ignored benchmarks (9) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x
