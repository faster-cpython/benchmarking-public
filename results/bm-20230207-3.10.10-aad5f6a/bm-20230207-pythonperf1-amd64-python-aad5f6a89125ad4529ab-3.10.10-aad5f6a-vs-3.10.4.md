
# Results vs. 3.10.4

- fork: python
- ref: aad5f6a89125ad4529ab
- machine: windows-amd64
- commit hash: aad5f6a
- commit date: 2023-02-07
- overall geometric mean: 1.00x slower \*
- HPT reliability: 54.88%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-pythonperf1-amd64-python-aad5f6a89125ad4529ab-3.10.10-aad5f6a |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 237 ms                                                      | 231 ms: 1.02x faster                                                      |
| chameleon      | 5.92 ms                                                     | 5.49 ms: 1.08x faster                                                     |
| docutils       | 1.89 sec                                                    | 1.84 sec: 1.03x faster                                                    |
| html5lib       | 46.5 ms                                                     | 48.2 ms: 1.04x slower                                                     |
| Geometric mean | (ref)                                                       | 1.02x faster                                                              |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-pythonperf1-amd64-python-aad5f6a89125ad4529ab-3.10.10-aad5f6a |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pidigits       | 145 ms                                                      | 148 ms: 1.02x slower                                                      |
| nbody          | 69.3 ms                                                     | 71.9 ms: 1.04x slower                                                     |
| Geometric mean | (ref)                                                       | 1.02x slower                                                              |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-pythonperf1-amd64-python-aad5f6a89125ad4529ab-3.10.10-aad5f6a |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 1.66 ms                                                     | 1.81 ms: 1.09x slower                                                     |
| Geometric mean | (ref)                                                       | 1.02x slower                                                              |

Benchmark hidden because not significant (3): regex_v8, regex_compile, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-pythonperf1-amd64-python-aad5f6a89125ad4529ab-3.10.10-aad5f6a |
|----------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| xml_etree_parse      | 102 ms                                                      | 96.6 ms: 1.05x faster                                                     |
| unpickle_list        | 2.81 us                                                     | 2.73 us: 1.03x faster                                                     |
| xml_etree_generate   | 54.5 ms                                                     | 53.3 ms: 1.02x faster                                                     |
| xml_etree_process    | 43.4 ms                                                     | 42.7 ms: 1.02x faster                                                     |
| xml_etree_iterparse  | 63.5 ms                                                     | 64.4 ms: 1.01x slower                                                     |
| pickle               | 6.80 us                                                     | 7.00 us: 1.03x slower                                                     |
| pickle_pure_python   | 257 us                                                      | 267 us: 1.04x slower                                                      |
| json_dumps           | 8.50 ms                                                     | 8.93 ms: 1.05x slower                                                     |
| unpickle_pure_python | 171 us                                                      | 180 us: 1.05x slower                                                      |
| pickle_list          | 2.59 us                                                     | 2.91 us: 1.12x slower                                                     |
| pickle_dict          | 16.9 us                                                     | 19.1 us: 1.13x slower                                                     |
| Geometric mean       | (ref)                                                       | 1.02x slower                                                              |

Benchmark hidden because not significant (2): unpickle, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-pythonperf1-amd64-python-aad5f6a89125ad4529ab-3.10.10-aad5f6a |
|------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 15.0 ms: 1.03x faster                                                     |
| python_startup         | 20.0 ms                                                     | 19.8 ms: 1.01x faster                                                     |
| Geometric mean         | (ref)                                                       | 1.02x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-pythonperf1-amd64-python-aad5f6a89125ad4529ab-3.10.10-aad5f6a |
|-----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_text     | 19.0 ms                                                     | 18.3 ms: 1.04x faster                                                     |
| genshi_xml      | 40.5 ms                                                     | 39.0 ms: 1.04x faster                                                     |
| django_template | 28.2 ms                                                     | 29.2 ms: 1.03x slower                                                     |
| Geometric mean  | (ref)                                                       | 1.01x faster                                                              |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-pythonperf1-amd64-python-aad5f6a89125ad4529ab-3.10.10-aad5f6a |
|-------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| chameleon               | 5.92 ms                                                     | 5.49 ms: 1.08x faster                                                     |
| xml_etree_parse         | 102 ms                                                      | 96.6 ms: 1.05x faster                                                     |
| asyncio_tcp             | 712 ms                                                      | 678 ms: 1.05x faster                                                      |
| genshi_text             | 19.0 ms                                                     | 18.3 ms: 1.04x faster                                                     |
| genshi_xml              | 40.5 ms                                                     | 39.0 ms: 1.04x faster                                                     |
| pathlib                 | 77.4 ms                                                     | 75.0 ms: 1.03x faster                                                     |
| python_startup_no_site  | 15.5 ms                                                     | 15.0 ms: 1.03x faster                                                     |
| unpickle_list           | 2.81 us                                                     | 2.73 us: 1.03x faster                                                     |
| aiohttp                 | 1.01 ms                                                     | 980 us: 1.03x faster                                                      |
| scimark_lu              | 85.4 ms                                                     | 83.2 ms: 1.03x faster                                                     |
| nqueens                 | 67.0 ms                                                     | 65.3 ms: 1.03x faster                                                     |
| docutils                | 1.89 sec                                                    | 1.84 sec: 1.03x faster                                                    |
| hexiom                  | 5.52 ms                                                     | 5.38 ms: 1.02x faster                                                     |
| 2to3                    | 237 ms                                                      | 231 ms: 1.02x faster                                                      |
| pprint_safe_repr        | 589 ms                                                      | 576 ms: 1.02x faster                                                      |
| pprint_pformat          | 1.21 sec                                                    | 1.18 sec: 1.02x faster                                                    |
| xml_etree_generate      | 54.5 ms                                                     | 53.3 ms: 1.02x faster                                                     |
| comprehensions          | 16.0 us                                                     | 15.7 us: 1.02x faster                                                     |
| raytrace                | 271 ms                                                      | 266 ms: 1.02x faster                                                      |
| async_tree_io           | 1.07 sec                                                    | 1.05 sec: 1.02x faster                                                    |
| pylint                  | 347 ms                                                      | 340 ms: 1.02x faster                                                      |
| xml_etree_process       | 43.4 ms                                                     | 42.7 ms: 1.02x faster                                                     |
| thrift                  | 615 us                                                      | 605 us: 1.02x faster                                                      |
| async_tree_memoization  | 497 ms                                                      | 490 ms: 1.02x faster                                                      |
| pycparser               | 868 ms                                                      | 855 ms: 1.01x faster                                                      |
| sqlglot_optimize        | 39.0 ms                                                     | 38.5 ms: 1.01x faster                                                     |
| scimark_monte_carlo     | 55.9 ms                                                     | 55.2 ms: 1.01x faster                                                     |
| chaos                   | 58.9 ms                                                     | 58.2 ms: 1.01x faster                                                     |
| sympy_integrate         | 14.8 ms                                                     | 14.6 ms: 1.01x faster                                                     |
| bench_mp_pool           | 60.7 ms                                                     | 60.0 ms: 1.01x faster                                                     |
| python_startup          | 20.0 ms                                                     | 19.8 ms: 1.01x faster                                                     |
| sqlglot_transpile       | 1.46 ms                                                     | 1.45 ms: 1.01x faster                                                     |
| scimark_sor             | 105 ms                                                      | 104 ms: 1.01x faster                                                      |
| deepcopy_reduce         | 2.16 us                                                     | 2.14 us: 1.01x faster                                                     |
| create_gc_cycles        | 782 us                                                      | 776 us: 1.01x faster                                                      |
| meteor_contest          | 72.5 ms                                                     | 72.9 ms: 1.00x slower                                                     |
| scimark_fft             | 193 ms                                                      | 194 ms: 1.00x slower                                                      |
| json                    | 3.05 ms                                                     | 3.06 ms: 1.01x slower                                                     |
| sqlglot_parse           | 1.22 ms                                                     | 1.23 ms: 1.01x slower                                                     |
| sqlite_synth            | 1.84 us                                                     | 1.86 us: 1.01x slower                                                     |
| deepcopy                | 255 us                                                      | 258 us: 1.01x slower                                                      |
| async_generators        | 224 ms                                                      | 227 ms: 1.01x slower                                                      |
| crypto_pyaes            | 62.3 ms                                                     | 63.1 ms: 1.01x slower                                                     |
| sympy_str               | 188 ms                                                      | 191 ms: 1.01x slower                                                      |
| xml_etree_iterparse     | 63.5 ms                                                     | 64.4 ms: 1.01x slower                                                     |
| go                      | 136 ms                                                      | 138 ms: 1.02x slower                                                      |
| pyflate                 | 387 ms                                                      | 393 ms: 1.02x slower                                                      |
| deepcopy_memo           | 28.5 us                                                     | 29.1 us: 1.02x slower                                                     |
| sqlalchemy_declarative  | 95.4 ms                                                     | 97.2 ms: 1.02x slower                                                     |
| pidigits                | 145 ms                                                      | 148 ms: 1.02x slower                                                      |
| sympy_sum               | 104 ms                                                      | 106 ms: 1.02x slower                                                      |
| logging_format          | 6.66 us                                                     | 6.81 us: 1.02x slower                                                     |
| telco                   | 3.78 ms                                                     | 3.88 ms: 1.02x slower                                                     |
| richards                | 41.2 ms                                                     | 42.3 ms: 1.03x slower                                                     |
| logging_silent          | 96.4 ns                                                     | 99.1 ns: 1.03x slower                                                     |
| pickle                  | 6.80 us                                                     | 7.00 us: 1.03x slower                                                     |
| generators              | 31.6 ms                                                     | 32.5 ms: 1.03x slower                                                     |
| dulwich_log             | 47.6 ms                                                     | 49.0 ms: 1.03x slower                                                     |
| dask                    | 305 ms                                                      | 314 ms: 1.03x slower                                                      |
| django_template         | 28.2 ms                                                     | 29.2 ms: 1.03x slower                                                     |
| html5lib                | 46.5 ms                                                     | 48.2 ms: 1.04x slower                                                     |
| nbody                   | 69.3 ms                                                     | 71.9 ms: 1.04x slower                                                     |
| gc_traversal            | 1.34 ms                                                     | 1.40 ms: 1.04x slower                                                     |
| logging_simple          | 6.20 us                                                     | 6.45 us: 1.04x slower                                                     |
| pickle_pure_python      | 257 us                                                      | 267 us: 1.04x slower                                                      |
| sqlalchemy_imperative   | 11.0 ms                                                     | 11.5 ms: 1.05x slower                                                     |
| json_dumps              | 8.50 ms                                                     | 8.93 ms: 1.05x slower                                                     |
| unpickle_pure_python    | 171 us                                                      | 180 us: 1.05x slower                                                      |
| spectral_norm           | 78.0 ms                                                     | 82.5 ms: 1.06x slower                                                     |
| scimark_sparse_mat_mult | 2.66 ms                                                     | 2.82 ms: 1.06x slower                                                     |
| unpack_sequence         | 37.8 ns                                                     | 40.8 ns: 1.08x slower                                                     |
| regex_effbot            | 1.66 ms                                                     | 1.81 ms: 1.09x slower                                                     |
| pickle_list             | 2.59 us                                                     | 2.91 us: 1.12x slower                                                     |
| pickle_dict             | 16.9 us                                                     | 19.1 us: 1.13x slower                                                     |
| Geometric mean          | (ref)                                                       | 1.00x slower                                                              |

Benchmark hidden because not significant (20): mypy2, unpickle, async_tree_none, sympy_expand, regex_v8, coroutines, mdp, bench_thread_pool, deltablue, regex_compile, coverage, sqlglot_normalize, regex_dna, flaskblogging, json_loads, tornado_http, mako, fannkuch, float, async_tree_cpu_io_mixed
Ignored benchmarks (4) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 54.88% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x
