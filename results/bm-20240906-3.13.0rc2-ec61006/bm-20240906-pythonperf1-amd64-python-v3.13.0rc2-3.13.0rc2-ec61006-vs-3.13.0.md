# Results vs. 3.13.0

- fork: python
- ref: v3.13.0rc2
- machine: windows-amd64
- commit hash: ec61006
- commit date: 2024-09-06
- overall geometric mean: 1.01x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-pythonperf1-amd64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| chameleon      | 4.72 ms                                                     | 4.89 ms: 1.04x slower                                             |
| docutils       | 1.57 sec                                                    | 1.67 sec: 1.06x slower                                            |
| html5lib       | 38.6 ms                                                     | 39.8 ms: 1.03x slower                                             |
| Geometric mean | (ref)                                                       | 1.02x slower                                                      |

Benchmark hidden because not significant (2): 2to3, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-pythonperf1-amd64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|---------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| asyncio_tcp               | 654 ms                                                      | 530 ms: 1.23x faster                                              |
| async_tree_memoization_tg | 288 ms                                                      | 266 ms: 1.09x faster                                              |
| coroutines                | 12.5 ms                                                     | 12.9 ms: 1.03x slower                                             |
| async_generators          | 223 ms                                                      | 232 ms: 1.04x slower                                              |
| async_tree_io             | 521 ms                                                      | 591 ms: 1.13x slower                                              |
| async_tree_io_tg          | 512 ms                                                      | 613 ms: 1.20x slower                                              |
| Geometric mean            | (ref)                                                       | 1.01x slower                                                      |

Benchmark hidden because not significant (6): asyncio_tcp_ssl, async_tree_none, async_tree_cpu_io_mixed, async_tree_memoization, async_tree_none_tg, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-pythonperf1-amd64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 152 ms: 1.02x slower                                              |
| float          | 48.1 ms                                                     | 50.1 ms: 1.04x slower                                             |
| nbody          | 64.5 ms                                                     | 68.0 ms: 1.05x slower                                             |
| Geometric mean | (ref)                                                       | 1.04x slower                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-pythonperf1-amd64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_compile  | 80.1 ms                                                     | 82.0 ms: 1.02x slower                                             |
| regex_v8       | 14.7 ms                                                     | 15.3 ms: 1.04x slower                                             |
| regex_dna      | 114 ms                                                      | 126 ms: 1.10x slower                                              |
| Geometric mean | (ref)                                                       | 1.04x slower                                                      |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-pythonperf1-amd64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|----------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| pickle               | 7.34 us                                                     | 6.91 us: 1.06x faster                                             |
| unpickle_list        | 2.72 us                                                     | 2.60 us: 1.05x faster                                             |
| json_loads           | 14.3 us                                                     | 14.1 us: 1.02x faster                                             |
| unpickle_pure_python | 127 us                                                      | 126 us: 1.01x faster                                              |
| json_dumps           | 5.76 ms                                                     | 5.80 ms: 1.01x slower                                             |
| pickle_pure_python   | 183 us                                                      | 185 us: 1.01x slower                                              |
| unpickle             | 8.63 us                                                     | 8.78 us: 1.02x slower                                             |
| tomli_loads          | 1.36 sec                                                    | 1.38 sec: 1.02x slower                                            |
| xml_etree_generate   | 53.3 ms                                                     | 54.4 ms: 1.02x slower                                             |
| pickle_dict          | 18.0 us                                                     | 18.4 us: 1.02x slower                                             |
| xml_etree_iterparse  | 62.3 ms                                                     | 64.2 ms: 1.03x slower                                             |
| xml_etree_process    | 36.5 ms                                                     | 37.8 ms: 1.03x slower                                             |
| Geometric mean       | (ref)                                                       | 1.00x slower                                                      |

Benchmark hidden because not significant (2): xml_etree_parse, pickle_list

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-pythonperf1-amd64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|-----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| genshi_xml      | 32.8 ms                                                     | 32.0 ms: 1.03x faster                                             |
| django_template | 21.8 ms                                                     | 22.1 ms: 1.01x slower                                             |
| genshi_text     | 14.9 ms                                                     | 15.2 ms: 1.02x slower                                             |
| mako            | 6.24 ms                                                     | 6.50 ms: 1.04x slower                                             |
| Geometric mean  | (ref)                                                       | 1.01x slower                                                      |

All benchmarks:
===============

| Benchmark                 | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240906-pythonperf1-amd64-python-v3.13.0rc2-3.13.0rc2-ec61006 |
|---------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------:|
| asyncio_tcp               | 654 ms                                                      | 530 ms: 1.23x faster                                              |
| unpack_sequence           | 40.0 ns                                                     | 33.1 ns: 1.21x faster                                             |
| pylint                    | 211 ms                                                      | 186 ms: 1.13x faster                                              |
| async_tree_memoization_tg | 288 ms                                                      | 266 ms: 1.09x faster                                              |
| pickle                    | 7.34 us                                                     | 6.91 us: 1.06x faster                                             |
| unpickle_list             | 2.72 us                                                     | 2.60 us: 1.05x faster                                             |
| genshi_xml                | 32.8 ms                                                     | 32.0 ms: 1.03x faster                                             |
| bench_mp_pool             | 69.6 ms                                                     | 68.0 ms: 1.02x faster                                             |
| telco                     | 4.85 ms                                                     | 4.74 ms: 1.02x faster                                             |
| pathlib                   | 81.2 ms                                                     | 79.6 ms: 1.02x faster                                             |
| json_loads                | 14.3 us                                                     | 14.1 us: 1.02x faster                                             |
| coverage                  | 46.7 ms                                                     | 46.0 ms: 1.02x faster                                             |
| scimark_fft               | 174 ms                                                      | 172 ms: 1.01x faster                                              |
| logging_format            | 6.15 us                                                     | 6.09 us: 1.01x faster                                             |
| logging_simple            | 5.72 us                                                     | 5.67 us: 1.01x faster                                             |
| unpickle_pure_python      | 127 us                                                      | 126 us: 1.01x faster                                              |
| thrift                    | 8.68 ms                                                     | 8.64 ms: 1.00x faster                                             |
| scimark_sparse_mat_mult   | 2.34 ms                                                     | 2.35 ms: 1.01x slower                                             |
| json_dumps                | 5.76 ms                                                     | 5.80 ms: 1.01x slower                                             |
| richards_super            | 29.3 ms                                                     | 29.5 ms: 1.01x slower                                             |
| richards                  | 26.0 ms                                                     | 26.2 ms: 1.01x slower                                             |
| mypy2                     | 429 ms                                                      | 433 ms: 1.01x slower                                              |
| sqlite_synth              | 1.60 us                                                     | 1.61 us: 1.01x slower                                             |
| pickle_pure_python        | 183 us                                                      | 185 us: 1.01x slower                                              |
| sympy_sum                 | 86.4 ms                                                     | 87.3 ms: 1.01x slower                                             |
| fannkuch                  | 245 ms                                                      | 248 ms: 1.01x slower                                              |
| chaos                     | 37.9 ms                                                     | 38.3 ms: 1.01x slower                                             |
| go                        | 84.6 ms                                                     | 85.7 ms: 1.01x slower                                             |
| django_template           | 21.8 ms                                                     | 22.1 ms: 1.01x slower                                             |
| comprehensions            | 10.2 us                                                     | 10.4 us: 1.01x slower                                             |
| aiohttp                   | 932 us                                                      | 946 us: 1.01x slower                                              |
| hexiom                    | 3.69 ms                                                     | 3.75 ms: 1.02x slower                                             |
| pprint_pformat            | 991 ms                                                      | 1.01 sec: 1.02x slower                                            |
| unpickle                  | 8.63 us                                                     | 8.78 us: 1.02x slower                                             |
| tomli_loads               | 1.36 sec                                                    | 1.38 sec: 1.02x slower                                            |
| sqlglot_normalize         | 171 ms                                                      | 174 ms: 1.02x slower                                              |
| sympy_str                 | 166 ms                                                      | 169 ms: 1.02x slower                                              |
| deltablue                 | 1.86 ms                                                     | 1.90 ms: 1.02x slower                                             |
| sympy_expand              | 285 ms                                                      | 291 ms: 1.02x slower                                              |
| genshi_text               | 14.9 ms                                                     | 15.2 ms: 1.02x slower                                             |
| xml_etree_generate        | 53.3 ms                                                     | 54.4 ms: 1.02x slower                                             |
| sympy_integrate           | 12.3 ms                                                     | 12.5 ms: 1.02x slower                                             |
| pidigits                  | 148 ms                                                      | 152 ms: 1.02x slower                                              |
| pickle_dict               | 18.0 us                                                     | 18.4 us: 1.02x slower                                             |
| regex_compile             | 80.1 ms                                                     | 82.0 ms: 1.02x slower                                             |
| pyflate                   | 275 ms                                                      | 282 ms: 1.02x slower                                              |
| coroutines                | 12.5 ms                                                     | 12.9 ms: 1.03x slower                                             |
| xml_etree_iterparse       | 62.3 ms                                                     | 64.2 ms: 1.03x slower                                             |
| html5lib                  | 38.6 ms                                                     | 39.8 ms: 1.03x slower                                             |
| nqueens                   | 55.5 ms                                                     | 57.3 ms: 1.03x slower                                             |
| spectral_norm             | 59.2 ms                                                     | 61.2 ms: 1.03x slower                                             |
| xml_etree_process         | 36.5 ms                                                     | 37.8 ms: 1.03x slower                                             |
| sqlglot_transpile         | 952 us                                                      | 985 us: 1.04x slower                                              |
| typing_runtime_protocols  | 100 us                                                      | 104 us: 1.04x slower                                              |
| chameleon                 | 4.72 ms                                                     | 4.89 ms: 1.04x slower                                             |
| raytrace                  | 156 ms                                                      | 162 ms: 1.04x slower                                              |
| scimark_monte_carlo       | 40.3 ms                                                     | 41.8 ms: 1.04x slower                                             |
| generators                | 19.5 ms                                                     | 20.2 ms: 1.04x slower                                             |
| dulwich_log               | 40.4 ms                                                     | 42.0 ms: 1.04x slower                                             |
| deepcopy_memo             | 21.8 us                                                     | 22.7 us: 1.04x slower                                             |
| async_generators          | 223 ms                                                      | 232 ms: 1.04x slower                                              |
| float                     | 48.1 ms                                                     | 50.1 ms: 1.04x slower                                             |
| mako                      | 6.24 ms                                                     | 6.50 ms: 1.04x slower                                             |
| crypto_pyaes              | 42.8 ms                                                     | 44.6 ms: 1.04x slower                                             |
| sqlglot_parse             | 761 us                                                      | 793 us: 1.04x slower                                              |
| regex_v8                  | 14.7 ms                                                     | 15.3 ms: 1.04x slower                                             |
| logging_silent            | 51.0 ns                                                     | 53.3 ns: 1.04x slower                                             |
| scimark_sor               | 72.0 ms                                                     | 75.3 ms: 1.05x slower                                             |
| scimark_lu                | 54.0 ms                                                     | 56.5 ms: 1.05x slower                                             |
| nbody                     | 64.5 ms                                                     | 68.0 ms: 1.05x slower                                             |
| docutils                  | 1.57 sec                                                    | 1.67 sec: 1.06x slower                                            |
| mdp                       | 1.38 sec                                                    | 1.49 sec: 1.07x slower                                            |
| create_gc_cycles          | 829 us                                                      | 901 us: 1.09x slower                                              |
| regex_dna                 | 114 ms                                                      | 126 ms: 1.10x slower                                              |
| async_tree_io             | 521 ms                                                      | 591 ms: 1.13x slower                                              |
| async_tree_io_tg          | 512 ms                                                      | 613 ms: 1.20x slower                                              |
| Geometric mean            | (ref)                                                       | 1.01x slower                                                      |

Benchmark hidden because not significant (23): pycparser, asyncio_tcp_ssl, async_tree_none, gc_traversal, xml_etree_parse, 2to3, tornado_http, deepcopy_reduce, flaskblogging, json, meteor_contest, deepcopy, pprint_safe_repr, python_startup, regex_effbot, sqlglot_optimize, async_tree_cpu_io_mixed, bench_thread_pool, async_tree_memoization, python_startup_no_site, async_tree_none_tg, pickle_list, async_tree_cpu_io_mixed_tg

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: unknown