# Results vs. 3.13.0b2

- fork: python
- ref: 5f547585fa56c94c5d83
- machine: windows-amd64
- commit hash: 5f54758
- commit date: 2024-05-04
- overall geometric mean: 1.01x slower
- HPT reliability: 99.21%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240504-pythonperf1-amd64-python-5f547585fa56c94c5d83-3.13.0a6+-5f54758 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| chameleon      | 4.80 ms                                                         | 4.64 ms: 1.03x faster                                                       |
| docutils       | 1.63 sec                                                        | 1.63 sec: 1.01x slower                                                      |
| html5lib       | 35.0 ms                                                         | 35.8 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                           | 1.00x faster                                                                |

Benchmark hidden because not significant (2): 2to3, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark          | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240504-pythonperf1-amd64-python-5f547585fa56c94c5d83-3.13.0a6+-5f54758 |
|--------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg   | 605 ms                                                          | 614 ms: 1.01x slower                                                        |
| async_tree_none_tg | 202 ms                                                          | 212 ms: 1.05x slower                                                        |
| Geometric mean     | (ref)                                                           | 1.01x slower                                                                |

Benchmark hidden because not significant (6): async_tree_io, async_tree_cpu_io_mixed, async_tree_none, async_tree_cpu_io_mixed_tg, async_tree_memoization, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240504-pythonperf1-amd64-python-5f547585fa56c94c5d83-3.13.0a6+-5f54758 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 67.6 ms                                                         | 66.1 ms: 1.02x faster                                                       |
| pidigits       | 150 ms                                                          | 147 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                           | 1.01x faster                                                                |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240504-pythonperf1-amd64-python-5f547585fa56c94c5d83-3.13.0a6+-5f54758 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 78.0 ms                                                         | 77.6 ms: 1.01x faster                                                       |
| regex_effbot   | 1.58 ms                                                         | 1.61 ms: 1.02x slower                                                       |
| regex_dna      | 119 ms                                                          | 124 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                           | 1.04x slower                                                                |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240504-pythonperf1-amd64-python-5f547585fa56c94c5d83-3.13.0a6+-5f54758 |
|----------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_process    | 36.4 ms                                                         | 36.9 ms: 1.01x slower                                                       |
| tomli_loads          | 1.35 sec                                                        | 1.37 sec: 1.01x slower                                                      |
| pickle_dict          | 18.1 us                                                         | 18.4 us: 1.01x slower                                                       |
| xml_etree_generate   | 53.2 ms                                                         | 53.9 ms: 1.01x slower                                                       |
| pickle               | 7.11 us                                                         | 7.22 us: 1.02x slower                                                       |
| unpickle             | 8.40 us                                                         | 8.58 us: 1.02x slower                                                       |
| json_loads           | 14.2 us                                                         | 14.5 us: 1.02x slower                                                       |
| unpickle_pure_python | 122 us                                                          | 125 us: 1.03x slower                                                        |
| pickle_list          | 2.90 us                                                         | 3.05 us: 1.05x slower                                                       |
| unpickle_list        | 2.62 us                                                         | 2.75 us: 1.05x slower                                                       |
| Geometric mean       | (ref)                                                           | 1.02x slower                                                                |

Benchmark hidden because not significant (4): xml_etree_iterparse, json_dumps, xml_etree_parse, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240504-pythonperf1-amd64-python-5f547585fa56c94c5d83-3.13.0a6+-5f54758 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup | 20.3 ms                                                         | 20.1 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                           | 1.00x faster                                                                |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240504-pythonperf1-amd64-python-5f547585fa56c94c5d83-3.13.0a6+-5f54758 |
|-----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 21.7 ms                                                         | 21.5 ms: 1.01x faster                                                       |
| mako            | 6.36 ms                                                         | 6.42 ms: 1.01x slower                                                       |
| Geometric mean  | (ref)                                                           | 1.00x slower                                                                |

Benchmark hidden because not significant (2): genshi_xml, genshi_text

All benchmarks:
===============

| Benchmark                | bm-20240605-pythonperf1-amd64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240504-pythonperf1-amd64-python-5f547585fa56c94c5d83-3.13.0a6+-5f54758 |
|--------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| logging_silent           | 52.9 ns                                                         | 50.3 ns: 1.05x faster                                                       |
| generators               | 19.6 ms                                                         | 18.6 ms: 1.05x faster                                                       |
| raytrace                 | 162 ms                                                          | 156 ms: 1.04x faster                                                        |
| chameleon                | 4.80 ms                                                         | 4.64 ms: 1.03x faster                                                       |
| richards                 | 26.7 ms                                                         | 25.9 ms: 1.03x faster                                                       |
| richards_super           | 30.2 ms                                                         | 29.3 ms: 1.03x faster                                                       |
| deepcopy                 | 220 us                                                          | 214 us: 1.03x faster                                                        |
| nbody                    | 67.6 ms                                                         | 66.1 ms: 1.02x faster                                                       |
| deepcopy_reduce          | 1.99 us                                                         | 1.95 us: 1.02x faster                                                       |
| logging_simple           | 5.78 us                                                         | 5.67 us: 1.02x faster                                                       |
| logging_format           | 6.22 us                                                         | 6.11 us: 1.02x faster                                                       |
| pidigits                 | 150 ms                                                          | 147 ms: 1.02x faster                                                        |
| comprehensions           | 10.4 us                                                         | 10.2 us: 1.01x faster                                                       |
| spectral_norm            | 63.7 ms                                                         | 62.8 ms: 1.01x faster                                                       |
| sqlglot_normalize        | 173 ms                                                          | 171 ms: 1.01x faster                                                        |
| python_startup           | 20.3 ms                                                         | 20.1 ms: 1.01x faster                                                       |
| coroutines               | 12.8 ms                                                         | 12.6 ms: 1.01x faster                                                       |
| deltablue                | 1.88 ms                                                         | 1.86 ms: 1.01x faster                                                       |
| typing_runtime_protocols | 101 us                                                          | 100.0 us: 1.01x faster                                                      |
| chaos                    | 38.4 ms                                                         | 38.0 ms: 1.01x faster                                                       |
| scimark_sor              | 75.3 ms                                                         | 74.7 ms: 1.01x faster                                                       |
| django_template          | 21.7 ms                                                         | 21.5 ms: 1.01x faster                                                       |
| regex_compile            | 78.0 ms                                                         | 77.6 ms: 1.01x faster                                                       |
| sqlglot_optimize         | 32.7 ms                                                         | 32.6 ms: 1.00x faster                                                       |
| pprint_pformat           | 966 ms                                                          | 964 ms: 1.00x faster                                                        |
| docutils                 | 1.63 sec                                                        | 1.63 sec: 1.01x slower                                                      |
| sqlglot_transpile        | 955 us                                                          | 963 us: 1.01x slower                                                        |
| sympy_integrate          | 12.2 ms                                                         | 12.3 ms: 1.01x slower                                                       |
| mako                     | 6.36 ms                                                         | 6.42 ms: 1.01x slower                                                       |
| sympy_str                | 159 ms                                                          | 161 ms: 1.01x slower                                                        |
| sqlite_synth             | 1.60 us                                                         | 1.62 us: 1.01x slower                                                       |
| mypy2                    | 418 ms                                                          | 423 ms: 1.01x slower                                                        |
| xml_etree_process        | 36.4 ms                                                         | 36.9 ms: 1.01x slower                                                       |
| sqlglot_parse            | 748 us                                                          | 757 us: 1.01x slower                                                        |
| aiohttp                  | 889 us                                                          | 900 us: 1.01x slower                                                        |
| tomli_loads              | 1.35 sec                                                        | 1.37 sec: 1.01x slower                                                      |
| pickle_dict              | 18.1 us                                                         | 18.4 us: 1.01x slower                                                       |
| async_tree_io_tg         | 605 ms                                                          | 614 ms: 1.01x slower                                                        |
| xml_etree_generate       | 53.2 ms                                                         | 53.9 ms: 1.01x slower                                                       |
| pyflate                  | 279 ms                                                          | 283 ms: 1.01x slower                                                        |
| pickle                   | 7.11 us                                                         | 7.22 us: 1.02x slower                                                       |
| regex_effbot             | 1.58 ms                                                         | 1.61 ms: 1.02x slower                                                       |
| hexiom                   | 3.72 ms                                                         | 3.79 ms: 1.02x slower                                                       |
| nqueens                  | 56.7 ms                                                         | 57.8 ms: 1.02x slower                                                       |
| create_gc_cycles         | 888 us                                                          | 906 us: 1.02x slower                                                        |
| unpickle                 | 8.40 us                                                         | 8.58 us: 1.02x slower                                                       |
| json_loads               | 14.2 us                                                         | 14.5 us: 1.02x slower                                                       |
| html5lib                 | 35.0 ms                                                         | 35.8 ms: 1.02x slower                                                       |
| go                       | 82.1 ms                                                         | 84.0 ms: 1.02x slower                                                       |
| scimark_sparse_mat_mult  | 2.50 ms                                                         | 2.57 ms: 1.03x slower                                                       |
| coverage                 | 42.1 ms                                                         | 43.2 ms: 1.03x slower                                                       |
| scimark_fft              | 171 ms                                                          | 176 ms: 1.03x slower                                                        |
| unpickle_pure_python     | 122 us                                                          | 125 us: 1.03x slower                                                        |
| telco                    | 4.67 ms                                                         | 4.81 ms: 1.03x slower                                                       |
| scimark_monte_carlo      | 39.1 ms                                                         | 40.4 ms: 1.03x slower                                                       |
| meteor_contest           | 69.9 ms                                                         | 72.1 ms: 1.03x slower                                                       |
| pathlib                  | 75.9 ms                                                         | 79.1 ms: 1.04x slower                                                       |
| regex_dna                | 119 ms                                                          | 124 ms: 1.04x slower                                                        |
| pickle_list              | 2.90 us                                                         | 3.05 us: 1.05x slower                                                       |
| async_tree_none_tg       | 202 ms                                                          | 212 ms: 1.05x slower                                                        |
| unpickle_list            | 2.62 us                                                         | 2.75 us: 1.05x slower                                                       |
| dulwich_log              | 38.0 ms                                                         | 40.1 ms: 1.05x slower                                                       |
| bench_thread_pool        | 768 us                                                          | 818 us: 1.07x slower                                                        |
| crypto_pyaes             | 45.5 ms                                                         | 48.6 ms: 1.07x slower                                                       |
| asyncio_tcp_ssl          | 1.48 sec                                                        | 1.61 sec: 1.08x slower                                                      |
| async_generators         | 223 ms                                                          | 244 ms: 1.09x slower                                                        |
| Geometric mean           | (ref)                                                           | 1.01x slower                                                                |

Benchmark hidden because not significant (32): async_tree_io, genshi_xml, async_tree_cpu_io_mixed, xml_etree_iterparse, thrift, pprint_safe_repr, gc_traversal, flaskblogging, json_dumps, tornado_http, bench_mp_pool, fannkuch, mdp, pycparser, xml_etree_parse, 2to3, pickle_pure_python, sympy_expand, sympy_sum, float, scimark_lu, async_tree_none, genshi_text, async_tree_cpu_io_mixed_tg, python_startup_no_site, deepcopy_memo, asyncio_tcp, pylint, async_tree_memoization, async_tree_memoization_tg, json, regex_v8
Ignored benchmarks (1) of results/bm-20240504-3.13.0a6+-5f54758/bm-20240504-pythonperf1-amd64-python-5f547585fa56c94c5d83-3.13.0a6+-5f54758.json: dask

# HPT report

- Reliability score: 99.21% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown