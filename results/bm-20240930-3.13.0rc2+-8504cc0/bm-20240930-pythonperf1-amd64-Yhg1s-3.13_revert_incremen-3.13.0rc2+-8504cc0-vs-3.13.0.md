# Results vs. 3.13.0

- fork: Yhg1s
- ref: 3.13_revert_incremen
- machine: windows-amd64
- commit hash: 8504cc0
- commit date: 2024-09-30
- overall geometric mean: 1.028x faster
- HPT reliability: 99.93%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240930-pythonperf1-amd64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-8504cc0 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 221 ms                                                      | 215 ms: 1.03x faster                                                        |
| chameleon      | 4.82 ms                                                     | 4.78 ms: 1.01x faster                                                       |
| docutils       | 1.57 sec                                                    | 1.56 sec: 1.01x faster                                                      |
| html5lib       | 38.9 ms                                                     | 40.0 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                       | 1.00x faster                                                                |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240930-pythonperf1-amd64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-8504cc0 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none_tg         | 209 ms                                                      | 200 ms: 1.04x faster                                                        |
| async_tree_io_tg           | 518 ms                                                      | 505 ms: 1.03x faster                                                        |
| async_tree_none            | 226 ms                                                      | 221 ms: 1.02x faster                                                        |
| async_generators           | 223 ms                                                      | 219 ms: 1.02x faster                                                        |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 370 ms: 1.02x faster                                                        |
| async_tree_cpu_io_mixed    | 383 ms                                                      | 377 ms: 1.02x faster                                                        |
| coroutines                 | 12.8 ms                                                     | 12.7 ms: 1.01x faster                                                       |
| Geometric mean             | (ref)                                                       | 1.02x faster                                                                |

Benchmark hidden because not significant (3): async_tree_memoization, async_tree_io, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240930-pythonperf1-amd64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-8504cc0 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 149 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                       | 1.00x slower                                                                |

Benchmark hidden because not significant (2): float, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240930-pythonperf1-amd64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-8504cc0 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 21.4 ms                                                     | 15.9 ms: 1.34x faster                                                       |
| regex_effbot   | 1.58 ms                                                     | 1.58 ms: 1.01x slower                                                       |
| regex_compile  | 80.5 ms                                                     | 81.6 ms: 1.01x slower                                                       |
| regex_dna      | 115 ms                                                      | 117 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                       | 1.07x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240930-pythonperf1-amd64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-8504cc0 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_loads           | 15.1 us                                                     | 14.3 us: 1.06x faster                                                       |
| pickle_pure_python   | 190 us                                                      | 180 us: 1.05x faster                                                        |
| unpickle_pure_python | 133 us                                                      | 127 us: 1.05x faster                                                        |
| json_dumps           | 5.92 ms                                                     | 5.71 ms: 1.04x faster                                                       |
| xml_etree_parse      | 93.6 ms                                                     | 92.3 ms: 1.01x faster                                                       |
| xml_etree_process    | 37.0 ms                                                     | 36.7 ms: 1.01x faster                                                       |
| Geometric mean       | (ref)                                                       | 1.03x faster                                                                |

Benchmark hidden because not significant (3): xml_etree_iterparse, xml_etree_generate, tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240930-pythonperf1-amd64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-8504cc0 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup | 25.4 ms                                                     | 22.3 ms: 1.14x faster                                                       |
| Geometric mean | (ref)                                                       | 1.07x faster                                                                |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240930-pythonperf1-amd64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-8504cc0 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 35.5 ms                                                     | 32.9 ms: 1.08x faster                                                       |
| genshi_text     | 15.6 ms                                                     | 15.0 ms: 1.04x faster                                                       |
| mako            | 6.35 ms                                                     | 6.23 ms: 1.02x faster                                                       |
| django_template | 22.4 ms                                                     | 22.2 ms: 1.01x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.04x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240930-pythonperf1-amd64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-8504cc0 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mypy2                      | 679 ms                                                      | 430 ms: 1.58x faster                                                        |
| create_gc_cycles           | 1.26 ms                                                     | 813 us: 1.55x faster                                                        |
| regex_v8                   | 21.4 ms                                                     | 15.9 ms: 1.34x faster                                                       |
| gc_traversal               | 1.97 ms                                                     | 1.55 ms: 1.27x faster                                                       |
| bench_mp_pool              | 86.4 ms                                                     | 69.3 ms: 1.25x faster                                                       |
| python_startup             | 25.4 ms                                                     | 22.3 ms: 1.14x faster                                                       |
| genshi_xml                 | 35.5 ms                                                     | 32.9 ms: 1.08x faster                                                       |
| spectral_norm              | 62.8 ms                                                     | 59.4 ms: 1.06x faster                                                       |
| json_loads                 | 15.1 us                                                     | 14.3 us: 1.06x faster                                                       |
| pickle_pure_python         | 190 us                                                      | 180 us: 1.05x faster                                                        |
| unpickle_pure_python       | 133 us                                                      | 127 us: 1.05x faster                                                        |
| hexiom                     | 3.89 ms                                                     | 3.72 ms: 1.05x faster                                                       |
| async_tree_none_tg         | 209 ms                                                      | 200 ms: 1.04x faster                                                        |
| typing_runtime_protocols   | 105 us                                                      | 101 us: 1.04x faster                                                        |
| genshi_text                | 15.6 ms                                                     | 15.0 ms: 1.04x faster                                                       |
| logging_simple             | 5.96 us                                                     | 5.72 us: 1.04x faster                                                       |
| bench_thread_pool          | 847 us                                                      | 816 us: 1.04x faster                                                        |
| richards_super             | 30.9 ms                                                     | 29.8 ms: 1.04x faster                                                       |
| json_dumps                 | 5.92 ms                                                     | 5.71 ms: 1.04x faster                                                       |
| fannkuch                   | 253 ms                                                      | 245 ms: 1.03x faster                                                        |
| thrift                     | 8.80 ms                                                     | 8.53 ms: 1.03x faster                                                       |
| 2to3                       | 221 ms                                                      | 215 ms: 1.03x faster                                                        |
| logging_silent             | 54.6 ns                                                     | 53.2 ns: 1.03x faster                                                       |
| async_tree_io_tg           | 518 ms                                                      | 505 ms: 1.03x faster                                                        |
| scimark_sparse_mat_mult    | 2.46 ms                                                     | 2.40 ms: 1.02x faster                                                       |
| pyflate                    | 283 ms                                                      | 277 ms: 1.02x faster                                                        |
| async_tree_none            | 226 ms                                                      | 221 ms: 1.02x faster                                                        |
| crypto_pyaes               | 45.4 ms                                                     | 44.4 ms: 1.02x faster                                                       |
| deltablue                  | 1.92 ms                                                     | 1.88 ms: 1.02x faster                                                       |
| logging_format             | 6.26 us                                                     | 6.12 us: 1.02x faster                                                       |
| deepcopy_memo              | 23.3 us                                                     | 22.8 us: 1.02x faster                                                       |
| mako                       | 6.35 ms                                                     | 6.23 ms: 1.02x faster                                                       |
| deepcopy_reduce            | 2.06 us                                                     | 2.02 us: 1.02x faster                                                       |
| async_generators           | 223 ms                                                      | 219 ms: 1.02x faster                                                        |
| scimark_monte_carlo        | 40.8 ms                                                     | 40.1 ms: 1.02x faster                                                       |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 370 ms: 1.02x faster                                                        |
| mdp                        | 1.39 sec                                                    | 1.36 sec: 1.02x faster                                                      |
| richards                   | 27.3 ms                                                     | 26.9 ms: 1.02x faster                                                       |
| async_tree_cpu_io_mixed    | 383 ms                                                      | 377 ms: 1.02x faster                                                        |
| meteor_contest             | 73.5 ms                                                     | 72.5 ms: 1.01x faster                                                       |
| xml_etree_parse            | 93.6 ms                                                     | 92.3 ms: 1.01x faster                                                       |
| sympy_expand               | 291 ms                                                      | 288 ms: 1.01x faster                                                        |
| comprehensions             | 10.3 us                                                     | 10.1 us: 1.01x faster                                                       |
| chameleon                  | 4.82 ms                                                     | 4.78 ms: 1.01x faster                                                       |
| xml_etree_process          | 37.0 ms                                                     | 36.7 ms: 1.01x faster                                                       |
| sympy_str                  | 169 ms                                                      | 167 ms: 1.01x faster                                                        |
| docutils                   | 1.57 sec                                                    | 1.56 sec: 1.01x faster                                                      |
| sympy_integrate            | 12.5 ms                                                     | 12.4 ms: 1.01x faster                                                       |
| coroutines                 | 12.8 ms                                                     | 12.7 ms: 1.01x faster                                                       |
| django_template            | 22.4 ms                                                     | 22.2 ms: 1.01x faster                                                       |
| scimark_sor                | 76.2 ms                                                     | 75.8 ms: 1.00x faster                                                       |
| regex_effbot               | 1.58 ms                                                     | 1.58 ms: 1.01x slower                                                       |
| scimark_fft                | 172 ms                                                      | 173 ms: 1.01x slower                                                        |
| deepcopy                   | 226 us                                                      | 228 us: 1.01x slower                                                        |
| pidigits                   | 148 ms                                                      | 149 ms: 1.01x slower                                                        |
| nqueens                    | 56.7 ms                                                     | 57.4 ms: 1.01x slower                                                       |
| generators                 | 19.5 ms                                                     | 19.8 ms: 1.01x slower                                                       |
| regex_compile              | 80.5 ms                                                     | 81.6 ms: 1.01x slower                                                       |
| pprint_pformat             | 999 ms                                                      | 1.01 sec: 1.02x slower                                                      |
| regex_dna                  | 115 ms                                                      | 117 ms: 1.02x slower                                                        |
| coverage                   | 45.6 ms                                                     | 46.4 ms: 1.02x slower                                                       |
| raytrace                   | 160 ms                                                      | 163 ms: 1.02x slower                                                        |
| go                         | 87.0 ms                                                     | 88.7 ms: 1.02x slower                                                       |
| scimark_lu                 | 53.0 ms                                                     | 54.0 ms: 1.02x slower                                                       |
| sqlglot_transpile          | 956 us                                                      | 978 us: 1.02x slower                                                        |
| sqlglot_optimize           | 32.9 ms                                                     | 33.9 ms: 1.03x slower                                                       |
| html5lib                   | 38.9 ms                                                     | 40.0 ms: 1.03x slower                                                       |
| pycparser                  | 683 ms                                                      | 756 ms: 1.11x slower                                                        |
| Geometric mean             | (ref)                                                       | 1.03x faster                                                                |

Benchmark hidden because not significant (20): async_tree_memoization, json, async_tree_io, python_startup_no_site, async_tree_memoization_tg, xml_etree_iterparse, pylint, tornado_http, xml_etree_generate, pathlib, sympy_sum, telco, sqlglot_parse, float, sqlglot_normalize, chaos, pprint_safe_repr, tomli_loads, nbody, dulwich_log
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, connected_components, gevent_hub, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (11) of results/bm-20240930-3.13.0rc2+-8504cc0/bm-20240930-pythonperf1-amd64-Yhg1s-3.13_revert_incremen-3.13.0rc2+-8504cc0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.028x faster
# HPT report

- Reliability score: 99.93% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown