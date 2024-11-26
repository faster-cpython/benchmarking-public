# Results vs. 3.13.0

- fork: faster-cpython
- ref: more_robust_immortal
- machine: windows-amd64
- commit hash: 94f8fd0
- commit date: 2024-10-10
- overall geometric mean: 1.027x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241010-pythonperf1-amd64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 221 ms                                                      | 227 ms: 1.03x slower                                                                 |
| docutils       | 1.57 sec                                                    | 1.71 sec: 1.09x slower                                                               |
| html5lib       | 38.9 ms                                                     | 42.2 ms: 1.08x slower                                                                |
| tornado_http   | 93.0 ms                                                     | 94.8 ms: 1.02x slower                                                                |
| Geometric mean | (ref)                                                       | 1.05x slower                                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241010-pythonperf1-amd64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 288 ms                                                      | 257 ms: 1.12x faster                                                                 |
| async_tree_none            | 226 ms                                                      | 212 ms: 1.07x faster                                                                 |
| async_tree_cpu_io_mixed    | 383 ms                                                      | 398 ms: 1.04x slower                                                                 |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 393 ms: 1.04x slower                                                                 |
| coroutines                 | 12.8 ms                                                     | 13.9 ms: 1.09x slower                                                                |
| async_generators           | 223 ms                                                      | 253 ms: 1.13x slower                                                                 |
| async_tree_io_tg           | 518 ms                                                      | 587 ms: 1.13x slower                                                                 |
| async_tree_io              | 521 ms                                                      | 593 ms: 1.14x slower                                                                 |
| Geometric mean             | (ref)                                                       | 1.04x slower                                                                         |

Benchmark hidden because not significant (2): async_tree_memoization, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241010-pythonperf1-amd64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| float          | 49.9 ms                                                     | 54.8 ms: 1.10x slower                                                                |
| nbody          | 68.4 ms                                                     | 80.7 ms: 1.18x slower                                                                |
| Geometric mean | (ref)                                                       | 1.09x slower                                                                         |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241010-pythonperf1-amd64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_v8       | 21.4 ms                                                     | 14.9 ms: 1.44x faster                                                                |
| regex_effbot   | 1.58 ms                                                     | 1.56 ms: 1.01x faster                                                                |
| regex_compile  | 80.5 ms                                                     | 90.1 ms: 1.12x slower                                                                |
| Geometric mean | (ref)                                                       | 1.07x faster                                                                         |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241010-pythonperf1-amd64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| json_dumps           | 5.92 ms                                                     | 6.34 ms: 1.07x slower                                                                |
| xml_etree_iterparse  | 61.8 ms                                                     | 66.9 ms: 1.08x slower                                                                |
| xml_etree_generate   | 54.0 ms                                                     | 58.7 ms: 1.09x slower                                                                |
| xml_etree_process    | 37.0 ms                                                     | 41.1 ms: 1.11x slower                                                                |
| unpickle_pure_python | 133 us                                                      | 149 us: 1.11x slower                                                                 |
| pickle_pure_python   | 190 us                                                      | 215 us: 1.14x slower                                                                 |
| tomli_loads          | 1.39 sec                                                    | 1.62 sec: 1.16x slower                                                               |
| Geometric mean       | (ref)                                                       | 1.08x slower                                                                         |

Benchmark hidden because not significant (2): json_loads, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241010-pythonperf1-amd64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup         | 25.4 ms                                                     | 22.1 ms: 1.15x faster                                                                |
| python_startup_no_site | 18.1 ms                                                     | 17.9 ms: 1.02x faster                                                                |
| Geometric mean         | (ref)                                                       | 1.08x faster                                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241010-pythonperf1-amd64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| genshi_xml      | 35.5 ms                                                     | 38.2 ms: 1.08x slower                                                                |
| mako            | 6.35 ms                                                     | 6.85 ms: 1.08x slower                                                                |
| genshi_text     | 15.6 ms                                                     | 17.8 ms: 1.14x slower                                                                |
| django_template | 22.4 ms                                                     | 26.7 ms: 1.20x slower                                                                |
| Geometric mean  | (ref)                                                       | 1.12x slower                                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241010-pythonperf1-amd64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| thrift                     | 8.80 ms                                                     | 522 us: 16.85x faster                                                                |
| regex_v8                   | 21.4 ms                                                     | 14.9 ms: 1.44x faster                                                                |
| create_gc_cycles           | 1.26 ms                                                     | 934 us: 1.35x faster                                                                 |
| gc_traversal               | 1.97 ms                                                     | 1.53 ms: 1.29x faster                                                                |
| bench_mp_pool              | 86.4 ms                                                     | 69.6 ms: 1.24x faster                                                                |
| deepcopy                   | 226 us                                                      | 192 us: 1.18x faster                                                                 |
| deepcopy_memo              | 23.3 us                                                     | 19.9 us: 1.17x faster                                                                |
| python_startup             | 25.4 ms                                                     | 22.1 ms: 1.15x faster                                                                |
| async_tree_memoization_tg  | 288 ms                                                      | 257 ms: 1.12x faster                                                                 |
| async_tree_none            | 226 ms                                                      | 212 ms: 1.07x faster                                                                 |
| deepcopy_reduce            | 2.06 us                                                     | 1.97 us: 1.05x faster                                                                |
| python_startup_no_site     | 18.1 ms                                                     | 17.9 ms: 1.02x faster                                                                |
| regex_effbot               | 1.58 ms                                                     | 1.56 ms: 1.01x faster                                                                |
| pathlib                    | 80.9 ms                                                     | 80.3 ms: 1.01x faster                                                                |
| go                         | 87.0 ms                                                     | 87.4 ms: 1.01x slower                                                                |
| tornado_http               | 93.0 ms                                                     | 94.8 ms: 1.02x slower                                                                |
| 2to3                       | 221 ms                                                      | 227 ms: 1.03x slower                                                                 |
| telco                      | 4.79 ms                                                     | 4.93 ms: 1.03x slower                                                                |
| sympy_sum                  | 86.9 ms                                                     | 90.2 ms: 1.04x slower                                                                |
| meteor_contest             | 73.5 ms                                                     | 76.4 ms: 1.04x slower                                                                |
| async_tree_cpu_io_mixed    | 383 ms                                                      | 398 ms: 1.04x slower                                                                 |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 393 ms: 1.04x slower                                                                 |
| sympy_expand               | 291 ms                                                      | 308 ms: 1.06x slower                                                                 |
| sympy_str                  | 169 ms                                                      | 179 ms: 1.06x slower                                                                 |
| crypto_pyaes               | 45.4 ms                                                     | 48.3 ms: 1.06x slower                                                                |
| json_dumps                 | 5.92 ms                                                     | 6.34 ms: 1.07x slower                                                                |
| typing_runtime_protocols   | 105 us                                                      | 113 us: 1.07x slower                                                                 |
| coverage                   | 45.6 ms                                                     | 48.9 ms: 1.07x slower                                                                |
| genshi_xml                 | 35.5 ms                                                     | 38.2 ms: 1.08x slower                                                                |
| mako                       | 6.35 ms                                                     | 6.85 ms: 1.08x slower                                                                |
| pylint                     | 211 ms                                                      | 228 ms: 1.08x slower                                                                 |
| dulwich_log                | 40.8 ms                                                     | 44.2 ms: 1.08x slower                                                                |
| sympy_integrate            | 12.5 ms                                                     | 13.5 ms: 1.08x slower                                                                |
| xml_etree_iterparse        | 61.8 ms                                                     | 66.9 ms: 1.08x slower                                                                |
| logging_simple             | 5.96 us                                                     | 6.45 us: 1.08x slower                                                                |
| html5lib                   | 38.9 ms                                                     | 42.2 ms: 1.08x slower                                                                |
| scimark_sparse_mat_mult    | 2.46 ms                                                     | 2.66 ms: 1.08x slower                                                                |
| scimark_lu                 | 53.0 ms                                                     | 57.4 ms: 1.08x slower                                                                |
| xml_etree_generate         | 54.0 ms                                                     | 58.7 ms: 1.09x slower                                                                |
| coroutines                 | 12.8 ms                                                     | 13.9 ms: 1.09x slower                                                                |
| docutils                   | 1.57 sec                                                    | 1.71 sec: 1.09x slower                                                               |
| float                      | 49.9 ms                                                     | 54.8 ms: 1.10x slower                                                                |
| logging_silent             | 54.6 ns                                                     | 60.1 ns: 1.10x slower                                                                |
| fannkuch                   | 253 ms                                                      | 279 ms: 1.10x slower                                                                 |
| spectral_norm              | 62.8 ms                                                     | 69.3 ms: 1.10x slower                                                                |
| logging_format             | 6.26 us                                                     | 6.91 us: 1.10x slower                                                                |
| pycparser                  | 683 ms                                                      | 756 ms: 1.11x slower                                                                 |
| hexiom                     | 3.89 ms                                                     | 4.32 ms: 1.11x slower                                                                |
| xml_etree_process          | 37.0 ms                                                     | 41.1 ms: 1.11x slower                                                                |
| generators                 | 19.5 ms                                                     | 21.7 ms: 1.11x slower                                                                |
| unpickle_pure_python       | 133 us                                                      | 149 us: 1.11x slower                                                                 |
| pprint_safe_repr           | 494 ms                                                      | 552 ms: 1.12x slower                                                                 |
| regex_compile              | 80.5 ms                                                     | 90.1 ms: 1.12x slower                                                                |
| pyflate                    | 283 ms                                                      | 319 ms: 1.13x slower                                                                 |
| pprint_pformat             | 999 ms                                                      | 1.13 sec: 1.13x slower                                                               |
| nqueens                    | 56.7 ms                                                     | 64.1 ms: 1.13x slower                                                                |
| async_generators           | 223 ms                                                      | 253 ms: 1.13x slower                                                                 |
| async_tree_io_tg           | 518 ms                                                      | 587 ms: 1.13x slower                                                                 |
| pickle_pure_python         | 190 us                                                      | 215 us: 1.14x slower                                                                 |
| async_tree_io              | 521 ms                                                      | 593 ms: 1.14x slower                                                                 |
| chaos                      | 38.5 ms                                                     | 43.8 ms: 1.14x slower                                                                |
| mdp                        | 1.39 sec                                                    | 1.58 sec: 1.14x slower                                                               |
| genshi_text                | 15.6 ms                                                     | 17.8 ms: 1.14x slower                                                                |
| sqlglot_optimize           | 32.9 ms                                                     | 37.6 ms: 1.14x slower                                                                |
| sqlglot_normalize          | 175 ms                                                      | 200 ms: 1.14x slower                                                                 |
| scimark_monte_carlo        | 40.8 ms                                                     | 46.9 ms: 1.15x slower                                                                |
| comprehensions             | 10.3 us                                                     | 11.8 us: 1.15x slower                                                                |
| scimark_sor                | 76.2 ms                                                     | 88.0 ms: 1.16x slower                                                                |
| tomli_loads                | 1.39 sec                                                    | 1.62 sec: 1.16x slower                                                               |
| scimark_fft                | 172 ms                                                      | 202 ms: 1.18x slower                                                                 |
| nbody                      | 68.4 ms                                                     | 80.7 ms: 1.18x slower                                                                |
| sqlglot_parse              | 771 us                                                      | 912 us: 1.18x slower                                                                 |
| richards_super             | 30.9 ms                                                     | 36.6 ms: 1.19x slower                                                                |
| richards                   | 27.3 ms                                                     | 32.5 ms: 1.19x slower                                                                |
| sqlglot_transpile          | 956 us                                                      | 1.14 ms: 1.19x slower                                                                |
| deltablue                  | 1.92 ms                                                     | 2.29 ms: 1.19x slower                                                                |
| django_template            | 22.4 ms                                                     | 26.7 ms: 1.20x slower                                                                |
| raytrace                   | 160 ms                                                      | 192 ms: 1.20x slower                                                                 |
| json                       | 3.19 ms                                                     | 4.15 ms: 1.30x slower                                                                |
| Geometric mean             | (ref)                                                       | 1.02x slower                                                                         |

Benchmark hidden because not significant (7): json_loads, bench_thread_pool, async_tree_memoization, async_tree_none_tg, regex_dna, pidigits, xml_etree_parse
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20241010-3.14.0a0-94f8fd0/bm-20241010-pythonperf1-amd64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.027x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.07x
- 95% likely to have a slowdown of 1.06x
- 99% likely to have a slowdown of 1.06x

# Memory
- memory change: unknown