# Results vs. 3.13.0

- fork: Yhg1s
- ref: 3.13_revert_incremen
- machine: windows-amd64
- commit hash: 8504cc0
- commit date: 2024-09-30
- overall geometric mean: 1.00x slower
- HPT reliability: 94.13%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240930-pythonperf1-amd64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-8504cc0 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 217 ms                                                      | 215 ms: 1.01x faster                                                        |
| chameleon      | 4.72 ms                                                     | 4.78 ms: 1.01x slower                                                       |
| docutils       | 1.57 sec                                                    | 1.56 sec: 1.01x faster                                                      |
| html5lib       | 38.6 ms                                                     | 40.0 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                       | 1.01x slower                                                                |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240930-pythonperf1-amd64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-8504cc0 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| asyncio_tcp                | 654 ms                                                      | 579 ms: 1.13x faster                                                        |
| asyncio_tcp_ssl            | 1.64 sec                                                    | 1.54 sec: 1.07x faster                                                      |
| async_tree_none_tg         | 206 ms                                                      | 200 ms: 1.03x faster                                                        |
| async_tree_cpu_io_mixed    | 387 ms                                                      | 377 ms: 1.03x faster                                                        |
| async_generators           | 223 ms                                                      | 219 ms: 1.02x faster                                                        |
| async_tree_none            | 223 ms                                                      | 221 ms: 1.01x faster                                                        |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 370 ms: 1.01x faster                                                        |
| coroutines                 | 12.5 ms                                                     | 12.7 ms: 1.01x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.03x faster                                                                |

Benchmark hidden because not significant (4): async_tree_io_tg, async_tree_io, async_tree_memoization, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240930-pythonperf1-amd64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-8504cc0 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 149 ms: 1.01x slower                                                        |
| float          | 48.1 ms                                                     | 49.9 ms: 1.04x slower                                                       |
| nbody          | 64.5 ms                                                     | 68.5 ms: 1.06x slower                                                       |
| Geometric mean | (ref)                                                       | 1.04x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240930-pythonperf1-amd64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-8504cc0 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 1.62 ms                                                     | 1.58 ms: 1.02x faster                                                       |
| regex_compile  | 80.1 ms                                                     | 81.6 ms: 1.02x slower                                                       |
| regex_dna      | 114 ms                                                      | 117 ms: 1.03x slower                                                        |
| regex_v8       | 14.7 ms                                                     | 15.9 ms: 1.09x slower                                                       |
| Geometric mean | (ref)                                                       | 1.03x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240930-pythonperf1-amd64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-8504cc0 |
|---------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_list       | 2.72 us                                                     | 2.64 us: 1.03x faster                                                       |
| pickle              | 7.34 us                                                     | 7.11 us: 1.03x faster                                                       |
| pickle_pure_python  | 183 us                                                      | 180 us: 1.02x faster                                                        |
| xml_etree_iterparse | 62.3 ms                                                     | 61.4 ms: 1.01x faster                                                       |
| xml_etree_parse     | 93.2 ms                                                     | 92.3 ms: 1.01x faster                                                       |
| json_dumps          | 5.76 ms                                                     | 5.71 ms: 1.01x faster                                                       |
| xml_etree_process   | 36.5 ms                                                     | 36.7 ms: 1.00x slower                                                       |
| xml_etree_generate  | 53.3 ms                                                     | 53.7 ms: 1.01x slower                                                       |
| pickle_dict         | 18.0 us                                                     | 18.3 us: 1.01x slower                                                       |
| tomli_loads         | 1.36 sec                                                    | 1.40 sec: 1.02x slower                                                      |
| unpickle            | 8.63 us                                                     | 8.86 us: 1.03x slower                                                       |
| pickle_list         | 2.89 us                                                     | 3.08 us: 1.06x slower                                                       |
| Geometric mean      | (ref)                                                       | 1.00x slower                                                                |

Benchmark hidden because not significant (2): unpickle_pure_python, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240930-pythonperf1-amd64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-8504cc0 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 17.8 ms                                                     | 18.0 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.01x slower                                                                |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240930-pythonperf1-amd64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-8504cc0 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 14.9 ms                                                     | 15.0 ms: 1.01x slower                                                       |
| django_template | 21.8 ms                                                     | 22.2 ms: 1.02x slower                                                       |
| Geometric mean  | (ref)                                                       | 1.01x slower                                                                |

Benchmark hidden because not significant (2): mako, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240930-pythonperf1-amd64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-8504cc0 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpack_sequence            | 40.0 ns                                                     | 35.0 ns: 1.14x faster                                                       |
| asyncio_tcp                | 654 ms                                                      | 579 ms: 1.13x faster                                                        |
| asyncio_tcp_ssl            | 1.64 sec                                                    | 1.54 sec: 1.07x faster                                                      |
| unpickle_list              | 2.72 us                                                     | 2.64 us: 1.03x faster                                                       |
| pickle                     | 7.34 us                                                     | 7.11 us: 1.03x faster                                                       |
| async_tree_none_tg         | 206 ms                                                      | 200 ms: 1.03x faster                                                        |
| async_tree_cpu_io_mixed    | 387 ms                                                      | 377 ms: 1.03x faster                                                        |
| regex_effbot               | 1.62 ms                                                     | 1.58 ms: 1.02x faster                                                       |
| pickle_pure_python         | 183 us                                                      | 180 us: 1.02x faster                                                        |
| create_gc_cycles           | 829 us                                                      | 813 us: 1.02x faster                                                        |
| thrift                     | 8.68 ms                                                     | 8.53 ms: 1.02x faster                                                       |
| async_generators           | 223 ms                                                      | 219 ms: 1.02x faster                                                        |
| mdp                        | 1.38 sec                                                    | 1.36 sec: 1.01x faster                                                      |
| xml_etree_iterparse        | 62.3 ms                                                     | 61.4 ms: 1.01x faster                                                       |
| telco                      | 4.85 ms                                                     | 4.78 ms: 1.01x faster                                                       |
| async_tree_none            | 223 ms                                                      | 221 ms: 1.01x faster                                                        |
| comprehensions             | 10.2 us                                                     | 10.1 us: 1.01x faster                                                       |
| async_tree_cpu_io_mixed_tg | 375 ms                                                      | 370 ms: 1.01x faster                                                        |
| 2to3                       | 217 ms                                                      | 215 ms: 1.01x faster                                                        |
| docutils                   | 1.57 sec                                                    | 1.56 sec: 1.01x faster                                                      |
| xml_etree_parse            | 93.2 ms                                                     | 92.3 ms: 1.01x faster                                                       |
| json_dumps                 | 5.76 ms                                                     | 5.71 ms: 1.01x faster                                                       |
| pathlib                    | 81.2 ms                                                     | 80.5 ms: 1.01x faster                                                       |
| coverage                   | 46.7 ms                                                     | 46.4 ms: 1.01x faster                                                       |
| scimark_fft                | 174 ms                                                      | 173 ms: 1.01x faster                                                        |
| flaskblogging              | 2.04 sec                                                    | 2.03 sec: 1.00x faster                                                      |
| sqlite_synth               | 1.60 us                                                     | 1.60 us: 1.00x slower                                                       |
| pyflate                    | 275 ms                                                      | 277 ms: 1.00x slower                                                        |
| xml_etree_process          | 36.5 ms                                                     | 36.7 ms: 1.00x slower                                                       |
| deltablue                  | 1.86 ms                                                     | 1.88 ms: 1.01x slower                                                       |
| pidigits                   | 148 ms                                                      | 149 ms: 1.01x slower                                                        |
| sympy_str                  | 166 ms                                                      | 167 ms: 1.01x slower                                                        |
| hexiom                     | 3.69 ms                                                     | 3.72 ms: 1.01x slower                                                       |
| genshi_text                | 14.9 ms                                                     | 15.0 ms: 1.01x slower                                                       |
| xml_etree_generate         | 53.3 ms                                                     | 53.7 ms: 1.01x slower                                                       |
| sympy_expand               | 285 ms                                                      | 288 ms: 1.01x slower                                                        |
| sqlglot_parse              | 761 us                                                      | 769 us: 1.01x slower                                                        |
| sympy_integrate            | 12.3 ms                                                     | 12.4 ms: 1.01x slower                                                       |
| coroutines                 | 12.5 ms                                                     | 12.7 ms: 1.01x slower                                                       |
| python_startup_no_site     | 17.8 ms                                                     | 18.0 ms: 1.01x slower                                                       |
| chameleon                  | 4.72 ms                                                     | 4.78 ms: 1.01x slower                                                       |
| pickle_dict                | 18.0 us                                                     | 18.3 us: 1.01x slower                                                       |
| dulwich_log                | 40.4 ms                                                     | 41.0 ms: 1.01x slower                                                       |
| generators                 | 19.5 ms                                                     | 19.8 ms: 1.02x slower                                                       |
| richards_super             | 29.3 ms                                                     | 29.8 ms: 1.02x slower                                                       |
| chaos                      | 37.9 ms                                                     | 38.5 ms: 1.02x slower                                                       |
| regex_compile              | 80.1 ms                                                     | 81.6 ms: 1.02x slower                                                       |
| sqlglot_normalize          | 171 ms                                                      | 175 ms: 1.02x slower                                                        |
| django_template            | 21.8 ms                                                     | 22.2 ms: 1.02x slower                                                       |
| deepcopy                   | 223 us                                                      | 228 us: 1.02x slower                                                        |
| pprint_pformat             | 991 ms                                                      | 1.01 sec: 1.02x slower                                                      |
| sqlglot_optimize           | 33.1 ms                                                     | 33.9 ms: 1.02x slower                                                       |
| scimark_sparse_mat_mult    | 2.34 ms                                                     | 2.40 ms: 1.02x slower                                                       |
| tomli_loads                | 1.36 sec                                                    | 1.40 sec: 1.02x slower                                                      |
| regex_dna                  | 114 ms                                                      | 117 ms: 1.03x slower                                                        |
| unpickle                   | 8.63 us                                                     | 8.86 us: 1.03x slower                                                       |
| sqlglot_transpile          | 952 us                                                      | 978 us: 1.03x slower                                                        |
| richards                   | 26.0 ms                                                     | 26.9 ms: 1.03x slower                                                       |
| nqueens                    | 55.5 ms                                                     | 57.4 ms: 1.03x slower                                                       |
| float                      | 48.1 ms                                                     | 49.9 ms: 1.04x slower                                                       |
| html5lib                   | 38.6 ms                                                     | 40.0 ms: 1.04x slower                                                       |
| crypto_pyaes               | 42.8 ms                                                     | 44.4 ms: 1.04x slower                                                       |
| raytrace                   | 156 ms                                                      | 163 ms: 1.04x slower                                                        |
| logging_silent             | 51.0 ns                                                     | 53.2 ns: 1.04x slower                                                       |
| deepcopy_memo              | 21.8 us                                                     | 22.8 us: 1.04x slower                                                       |
| go                         | 84.6 ms                                                     | 88.7 ms: 1.05x slower                                                       |
| json                       | 2.98 ms                                                     | 3.14 ms: 1.05x slower                                                       |
| scimark_sor                | 72.0 ms                                                     | 75.8 ms: 1.05x slower                                                       |
| nbody                      | 64.5 ms                                                     | 68.5 ms: 1.06x slower                                                       |
| pickle_list                | 2.89 us                                                     | 3.08 us: 1.06x slower                                                       |
| regex_v8                   | 14.7 ms                                                     | 15.9 ms: 1.09x slower                                                       |
| Geometric mean             | (ref)                                                       | 1.00x slower                                                                |

Benchmark hidden because not significant (28): async_tree_io_tg, bench_thread_pool, async_tree_io, async_tree_memoization, async_tree_memoization_tg, pylint, logging_format, bench_mp_pool, scimark_monte_carlo, tornado_http, pycparser, mako, unpickle_pure_python, logging_simple, gc_traversal, scimark_lu, json_loads, fannkuch, aiohttp, sympy_sum, deepcopy_reduce, spectral_norm, meteor_contest, pprint_safe_repr, python_startup, genshi_xml, mypy2, typing_runtime_protocols

# HPT report

- Reliability score: 94.13% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown