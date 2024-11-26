# Results vs. 3.13.0

- fork: Fidget-Spinner
- ref: deferred_globals_fin
- machine: windows-amd64
- commit hash: bfd4400
- commit date: 2024-08-28
- overall geometric mean: 1.017x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-pythonperf1-amd64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 221 ms                                                      | 231 ms: 1.04x slower                                                                 |
| docutils       | 1.57 sec                                                    | 1.74 sec: 1.11x slower                                                               |
| html5lib       | 38.9 ms                                                     | 41.4 ms: 1.06x slower                                                                |
| Geometric mean | (ref)                                                       | 1.05x slower                                                                         |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-pythonperf1-amd64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 288 ms                                                      | 249 ms: 1.16x faster                                                                 |
| async_tree_none_tg         | 209 ms                                                      | 197 ms: 1.06x faster                                                                 |
| async_tree_memoization     | 276 ms                                                      | 264 ms: 1.04x faster                                                                 |
| async_tree_none            | 226 ms                                                      | 218 ms: 1.03x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 392 ms: 1.04x slower                                                                 |
| async_tree_io_tg           | 518 ms                                                      | 546 ms: 1.05x slower                                                                 |
| coroutines                 | 12.8 ms                                                     | 14.2 ms: 1.11x slower                                                                |
| async_tree_io              | 521 ms                                                      | 583 ms: 1.12x slower                                                                 |
| async_generators           | 223 ms                                                      | 250 ms: 1.12x slower                                                                 |
| Geometric mean             | (ref)                                                       | 1.02x slower                                                                         |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-pythonperf1-amd64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 152 ms: 1.03x slower                                                                 |
| float          | 49.9 ms                                                     | 56.8 ms: 1.14x slower                                                                |
| nbody          | 68.4 ms                                                     | 83.5 ms: 1.22x slower                                                                |
| Geometric mean | (ref)                                                       | 1.13x slower                                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-pythonperf1-amd64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_v8       | 21.4 ms                                                     | 14.7 ms: 1.46x faster                                                                |
| regex_effbot   | 1.58 ms                                                     | 1.55 ms: 1.02x faster                                                                |
| regex_dna      | 115 ms                                                      | 114 ms: 1.01x faster                                                                 |
| regex_compile  | 80.5 ms                                                     | 90.4 ms: 1.12x slower                                                                |
| Geometric mean | (ref)                                                       | 1.08x faster                                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-pythonperf1-amd64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| json_loads           | 15.1 us                                                     | 14.0 us: 1.08x faster                                                                |
| xml_etree_parse      | 93.6 ms                                                     | 95.9 ms: 1.02x slower                                                                |
| json_dumps           | 5.92 ms                                                     | 6.16 ms: 1.04x slower                                                                |
| xml_etree_iterparse  | 61.8 ms                                                     | 65.8 ms: 1.06x slower                                                                |
| xml_etree_generate   | 54.0 ms                                                     | 57.9 ms: 1.07x slower                                                                |
| unpickle_pure_python | 133 us                                                      | 146 us: 1.09x slower                                                                 |
| xml_etree_process    | 37.0 ms                                                     | 40.7 ms: 1.10x slower                                                                |
| pickle_pure_python   | 190 us                                                      | 212 us: 1.12x slower                                                                 |
| tomli_loads          | 1.39 sec                                                    | 1.57 sec: 1.13x slower                                                               |
| Geometric mean       | (ref)                                                       | 1.06x slower                                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-pythonperf1-amd64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup         | 25.4 ms                                                     | 21.9 ms: 1.16x faster                                                                |
| python_startup_no_site | 18.1 ms                                                     | 17.8 ms: 1.02x faster                                                                |
| Geometric mean         | (ref)                                                       | 1.09x faster                                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-pythonperf1-amd64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| genshi_text     | 15.6 ms                                                     | 17.0 ms: 1.09x slower                                                                |
| mako            | 6.35 ms                                                     | 6.97 ms: 1.10x slower                                                                |
| django_template | 22.4 ms                                                     | 24.6 ms: 1.10x slower                                                                |
| Geometric mean  | (ref)                                                       | 1.07x slower                                                                         |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-pythonperf1-amd64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| thrift                     | 8.80 ms                                                     | 526 us: 16.73x faster                                                                |
| regex_v8                   | 21.4 ms                                                     | 14.7 ms: 1.46x faster                                                                |
| create_gc_cycles           | 1.26 ms                                                     | 910 us: 1.38x faster                                                                 |
| bench_mp_pool              | 86.4 ms                                                     | 68.2 ms: 1.27x faster                                                                |
| gc_traversal               | 1.97 ms                                                     | 1.57 ms: 1.25x faster                                                                |
| deepcopy                   | 226 us                                                      | 188 us: 1.21x faster                                                                 |
| deepcopy_memo              | 23.3 us                                                     | 20.0 us: 1.16x faster                                                                |
| python_startup             | 25.4 ms                                                     | 21.9 ms: 1.16x faster                                                                |
| async_tree_memoization_tg  | 288 ms                                                      | 249 ms: 1.16x faster                                                                 |
| deepcopy_reduce            | 2.06 us                                                     | 1.90 us: 1.09x faster                                                                |
| json_loads                 | 15.1 us                                                     | 14.0 us: 1.08x faster                                                                |
| async_tree_none_tg         | 209 ms                                                      | 197 ms: 1.06x faster                                                                 |
| async_tree_memoization     | 276 ms                                                      | 264 ms: 1.04x faster                                                                 |
| async_tree_none            | 226 ms                                                      | 218 ms: 1.03x faster                                                                 |
| pathlib                    | 80.9 ms                                                     | 78.9 ms: 1.02x faster                                                                |
| regex_effbot               | 1.58 ms                                                     | 1.55 ms: 1.02x faster                                                                |
| python_startup_no_site     | 18.1 ms                                                     | 17.8 ms: 1.02x faster                                                                |
| regex_dna                  | 115 ms                                                      | 114 ms: 1.01x faster                                                                 |
| xml_etree_parse            | 93.6 ms                                                     | 95.9 ms: 1.02x slower                                                                |
| pidigits                   | 148 ms                                                      | 152 ms: 1.03x slower                                                                 |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 392 ms: 1.04x slower                                                                 |
| coverage                   | 45.6 ms                                                     | 47.4 ms: 1.04x slower                                                                |
| json_dumps                 | 5.92 ms                                                     | 6.16 ms: 1.04x slower                                                                |
| 2to3                       | 221 ms                                                      | 231 ms: 1.04x slower                                                                 |
| telco                      | 4.79 ms                                                     | 5.02 ms: 1.05x slower                                                                |
| sympy_sum                  | 86.9 ms                                                     | 91.2 ms: 1.05x slower                                                                |
| crypto_pyaes               | 45.4 ms                                                     | 47.9 ms: 1.05x slower                                                                |
| sympy_integrate            | 12.5 ms                                                     | 13.2 ms: 1.05x slower                                                                |
| async_tree_io_tg           | 518 ms                                                      | 546 ms: 1.05x slower                                                                 |
| sympy_str                  | 169 ms                                                      | 178 ms: 1.06x slower                                                                 |
| dulwich_log                | 40.8 ms                                                     | 43.2 ms: 1.06x slower                                                                |
| sympy_expand               | 291 ms                                                      | 308 ms: 1.06x slower                                                                 |
| html5lib                   | 38.9 ms                                                     | 41.4 ms: 1.06x slower                                                                |
| logging_simple             | 5.96 us                                                     | 6.34 us: 1.06x slower                                                                |
| xml_etree_iterparse        | 61.8 ms                                                     | 65.8 ms: 1.06x slower                                                                |
| generators                 | 19.5 ms                                                     | 20.8 ms: 1.07x slower                                                                |
| meteor_contest             | 73.5 ms                                                     | 78.5 ms: 1.07x slower                                                                |
| xml_etree_generate         | 54.0 ms                                                     | 57.9 ms: 1.07x slower                                                                |
| mdp                        | 1.39 sec                                                    | 1.50 sec: 1.08x slower                                                               |
| logging_format             | 6.26 us                                                     | 6.77 us: 1.08x slower                                                                |
| scimark_sparse_mat_mult    | 2.46 ms                                                     | 2.66 ms: 1.08x slower                                                                |
| spectral_norm              | 62.8 ms                                                     | 68.3 ms: 1.09x slower                                                                |
| typing_runtime_protocols   | 105 us                                                      | 115 us: 1.09x slower                                                                 |
| genshi_text                | 15.6 ms                                                     | 17.0 ms: 1.09x slower                                                                |
| unpickle_pure_python       | 133 us                                                      | 146 us: 1.09x slower                                                                 |
| mako                       | 6.35 ms                                                     | 6.97 ms: 1.10x slower                                                                |
| sqlglot_normalize          | 175 ms                                                      | 192 ms: 1.10x slower                                                                 |
| xml_etree_process          | 37.0 ms                                                     | 40.7 ms: 1.10x slower                                                                |
| django_template            | 22.4 ms                                                     | 24.6 ms: 1.10x slower                                                                |
| docutils                   | 1.57 sec                                                    | 1.74 sec: 1.11x slower                                                               |
| sqlglot_optimize           | 32.9 ms                                                     | 36.4 ms: 1.11x slower                                                                |
| coroutines                 | 12.8 ms                                                     | 14.2 ms: 1.11x slower                                                                |
| hexiom                     | 3.89 ms                                                     | 4.33 ms: 1.11x slower                                                                |
| nqueens                    | 56.7 ms                                                     | 63.1 ms: 1.11x slower                                                                |
| pprint_safe_repr           | 494 ms                                                      | 551 ms: 1.12x slower                                                                 |
| pyflate                    | 283 ms                                                      | 316 ms: 1.12x slower                                                                 |
| pickle_pure_python         | 190 us                                                      | 212 us: 1.12x slower                                                                 |
| async_tree_io              | 521 ms                                                      | 583 ms: 1.12x slower                                                                 |
| async_generators           | 223 ms                                                      | 250 ms: 1.12x slower                                                                 |
| regex_compile              | 80.5 ms                                                     | 90.4 ms: 1.12x slower                                                                |
| chaos                      | 38.5 ms                                                     | 43.3 ms: 1.13x slower                                                                |
| tomli_loads                | 1.39 sec                                                    | 1.57 sec: 1.13x slower                                                               |
| pprint_pformat             | 999 ms                                                      | 1.13 sec: 1.13x slower                                                               |
| float                      | 49.9 ms                                                     | 56.8 ms: 1.14x slower                                                                |
| go                         | 87.0 ms                                                     | 99.2 ms: 1.14x slower                                                                |
| fannkuch                   | 253 ms                                                      | 290 ms: 1.14x slower                                                                 |
| logging_silent             | 54.6 ns                                                     | 62.7 ns: 1.15x slower                                                                |
| sqlglot_transpile          | 956 us                                                      | 1.10 ms: 1.15x slower                                                                |
| sqlglot_parse              | 771 us                                                      | 890 us: 1.15x slower                                                                 |
| scimark_lu                 | 53.0 ms                                                     | 61.6 ms: 1.16x slower                                                                |
| comprehensions             | 10.3 us                                                     | 12.0 us: 1.16x slower                                                                |
| scimark_fft                | 172 ms                                                      | 203 ms: 1.18x slower                                                                 |
| richards_super             | 30.9 ms                                                     | 36.5 ms: 1.18x slower                                                                |
| deltablue                  | 1.92 ms                                                     | 2.27 ms: 1.18x slower                                                                |
| scimark_sor                | 76.2 ms                                                     | 90.2 ms: 1.18x slower                                                                |
| richards                   | 27.3 ms                                                     | 32.5 ms: 1.19x slower                                                                |
| scimark_monte_carlo        | 40.8 ms                                                     | 49.0 ms: 1.20x slower                                                                |
| raytrace                   | 160 ms                                                      | 194 ms: 1.21x slower                                                                 |
| nbody                      | 68.4 ms                                                     | 83.5 ms: 1.22x slower                                                                |
| pycparser                  | 683 ms                                                      | 883 ms: 1.29x slower                                                                 |
| Geometric mean             | (ref)                                                       | 1.02x slower                                                                         |

Benchmark hidden because not significant (6): json, bench_thread_pool, tornado_http, async_tree_cpu_io_mixed, genshi_xml, pylint
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (2) of results/bm-20240828-3.14.0a0-bfd4400/bm-20240828-pythonperf1-amd64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400.json: asyncio_tcp, asyncio_tcp_ssl

- Geometric mean (including insignificant results): 1.017x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.05x

# Memory
- memory change: unknown