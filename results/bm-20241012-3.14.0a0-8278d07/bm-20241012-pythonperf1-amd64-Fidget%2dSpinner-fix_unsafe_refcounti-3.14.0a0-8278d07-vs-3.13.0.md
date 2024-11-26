# Results vs. 3.13.0

- fork: Fidget-Spinner
- ref: fix_unsafe_refcounti
- machine: windows-amd64
- commit hash: 8278d07
- commit date: 2024-10-12
- overall geometric mean: 1.030x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241012-pythonperf1-amd64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| 2to3           | 221 ms                                                      | 229 ms: 1.04x slower                                                                 |
| docutils       | 1.57 sec                                                    | 1.72 sec: 1.09x slower                                                               |
| html5lib       | 38.9 ms                                                     | 43.8 ms: 1.12x slower                                                                |
| tornado_http   | 93.0 ms                                                     | 94.1 ms: 1.01x slower                                                                |
| Geometric mean | (ref)                                                       | 1.07x slower                                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241012-pythonperf1-amd64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 288 ms                                                      | 259 ms: 1.11x faster                                                                 |
| async_tree_none            | 226 ms                                                      | 214 ms: 1.06x faster                                                                 |
| async_tree_cpu_io_mixed    | 383 ms                                                      | 396 ms: 1.04x slower                                                                 |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 395 ms: 1.05x slower                                                                 |
| async_tree_io_tg           | 518 ms                                                      | 581 ms: 1.12x slower                                                                 |
| coroutines                 | 12.8 ms                                                     | 14.3 ms: 1.12x slower                                                                |
| async_generators           | 223 ms                                                      | 253 ms: 1.13x slower                                                                 |
| async_tree_io              | 521 ms                                                      | 594 ms: 1.14x slower                                                                 |
| Geometric mean             | (ref)                                                       | 1.04x slower                                                                         |

Benchmark hidden because not significant (2): async_tree_memoization, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241012-pythonperf1-amd64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 148 ms: 1.01x slower                                                                 |
| float          | 49.9 ms                                                     | 54.1 ms: 1.08x slower                                                                |
| nbody          | 68.4 ms                                                     | 82.9 ms: 1.21x slower                                                                |
| Geometric mean | (ref)                                                       | 1.10x slower                                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241012-pythonperf1-amd64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| regex_v8       | 21.4 ms                                                     | 14.9 ms: 1.44x faster                                                                |
| regex_dna      | 115 ms                                                      | 114 ms: 1.01x faster                                                                 |
| regex_compile  | 80.5 ms                                                     | 90.8 ms: 1.13x slower                                                                |
| Geometric mean | (ref)                                                       | 1.07x faster                                                                         |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241012-pythonperf1-amd64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| xml_etree_parse      | 93.6 ms                                                     | 96.2 ms: 1.03x slower                                                                |
| xml_etree_generate   | 54.0 ms                                                     | 58.0 ms: 1.07x slower                                                                |
| xml_etree_iterparse  | 61.8 ms                                                     | 67.0 ms: 1.08x slower                                                                |
| xml_etree_process    | 37.0 ms                                                     | 41.0 ms: 1.11x slower                                                                |
| unpickle_pure_python | 133 us                                                      | 149 us: 1.11x slower                                                                 |
| json_dumps           | 5.92 ms                                                     | 6.73 ms: 1.14x slower                                                                |
| pickle_pure_python   | 190 us                                                      | 217 us: 1.15x slower                                                                 |
| tomli_loads          | 1.39 sec                                                    | 1.65 sec: 1.18x slower                                                               |
| Geometric mean       | (ref)                                                       | 1.09x slower                                                                         |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241012-pythonperf1-amd64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| python_startup | 25.4 ms                                                     | 22.2 ms: 1.14x faster                                                                |
| Geometric mean | (ref)                                                       | 1.07x faster                                                                         |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241012-pythonperf1-amd64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|-----------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| genshi_xml      | 35.5 ms                                                     | 37.1 ms: 1.05x slower                                                                |
| mako            | 6.35 ms                                                     | 6.79 ms: 1.07x slower                                                                |
| genshi_text     | 15.6 ms                                                     | 17.4 ms: 1.11x slower                                                                |
| django_template | 22.4 ms                                                     | 26.3 ms: 1.18x slower                                                                |
| Geometric mean  | (ref)                                                       | 1.10x slower                                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20241012-pythonperf1-amd64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07 |
|----------------------------|:-----------------------------------------------------------:|:------------------------------------------------------------------------------------:|
| thrift                     | 8.80 ms                                                     | 524 us: 16.80x faster                                                                |
| regex_v8                   | 21.4 ms                                                     | 14.9 ms: 1.44x faster                                                                |
| create_gc_cycles           | 1.26 ms                                                     | 939 us: 1.34x faster                                                                 |
| gc_traversal               | 1.97 ms                                                     | 1.55 ms: 1.27x faster                                                                |
| bench_mp_pool              | 86.4 ms                                                     | 68.7 ms: 1.26x faster                                                                |
| deepcopy                   | 226 us                                                      | 193 us: 1.17x faster                                                                 |
| deepcopy_memo              | 23.3 us                                                     | 19.9 us: 1.17x faster                                                                |
| python_startup             | 25.4 ms                                                     | 22.2 ms: 1.14x faster                                                                |
| async_tree_memoization_tg  | 288 ms                                                      | 259 ms: 1.11x faster                                                                 |
| async_tree_none            | 226 ms                                                      | 214 ms: 1.06x faster                                                                 |
| deepcopy_reduce            | 2.06 us                                                     | 2.02 us: 1.02x faster                                                                |
| regex_dna                  | 115 ms                                                      | 114 ms: 1.01x faster                                                                 |
| go                         | 87.0 ms                                                     | 86.4 ms: 1.01x faster                                                                |
| pidigits                   | 148 ms                                                      | 148 ms: 1.01x slower                                                                 |
| tornado_http               | 93.0 ms                                                     | 94.1 ms: 1.01x slower                                                                |
| xml_etree_parse            | 93.6 ms                                                     | 96.2 ms: 1.03x slower                                                                |
| sympy_sum                  | 86.9 ms                                                     | 89.8 ms: 1.03x slower                                                                |
| async_tree_cpu_io_mixed    | 383 ms                                                      | 396 ms: 1.04x slower                                                                 |
| 2to3                       | 221 ms                                                      | 229 ms: 1.04x slower                                                                 |
| genshi_xml                 | 35.5 ms                                                     | 37.1 ms: 1.05x slower                                                                |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 395 ms: 1.05x slower                                                                 |
| sympy_expand               | 291 ms                                                      | 307 ms: 1.05x slower                                                                 |
| meteor_contest             | 73.5 ms                                                     | 77.6 ms: 1.06x slower                                                                |
| logging_simple             | 5.96 us                                                     | 6.29 us: 1.06x slower                                                                |
| sympy_str                  | 169 ms                                                      | 178 ms: 1.06x slower                                                                 |
| crypto_pyaes               | 45.4 ms                                                     | 48.1 ms: 1.06x slower                                                                |
| coverage                   | 45.6 ms                                                     | 48.6 ms: 1.07x slower                                                                |
| mako                       | 6.35 ms                                                     | 6.79 ms: 1.07x slower                                                                |
| xml_etree_generate         | 54.0 ms                                                     | 58.0 ms: 1.07x slower                                                                |
| dulwich_log                | 40.8 ms                                                     | 43.9 ms: 1.07x slower                                                                |
| pylint                     | 211 ms                                                      | 228 ms: 1.08x slower                                                                 |
| logging_format             | 6.26 us                                                     | 6.77 us: 1.08x slower                                                                |
| xml_etree_iterparse        | 61.8 ms                                                     | 67.0 ms: 1.08x slower                                                                |
| sympy_integrate            | 12.5 ms                                                     | 13.5 ms: 1.08x slower                                                                |
| float                      | 49.9 ms                                                     | 54.1 ms: 1.08x slower                                                                |
| pycparser                  | 683 ms                                                      | 741 ms: 1.08x slower                                                                 |
| scimark_sparse_mat_mult    | 2.46 ms                                                     | 2.67 ms: 1.09x slower                                                                |
| docutils                   | 1.57 sec                                                    | 1.72 sec: 1.09x slower                                                               |
| mdp                        | 1.39 sec                                                    | 1.52 sec: 1.10x slower                                                               |
| spectral_norm              | 62.8 ms                                                     | 69.0 ms: 1.10x slower                                                                |
| typing_runtime_protocols   | 105 us                                                      | 116 us: 1.10x slower                                                                 |
| xml_etree_process          | 37.0 ms                                                     | 41.0 ms: 1.11x slower                                                                |
| pprint_safe_repr           | 494 ms                                                      | 547 ms: 1.11x slower                                                                 |
| logging_silent             | 54.6 ns                                                     | 60.8 ns: 1.11x slower                                                                |
| genshi_text                | 15.6 ms                                                     | 17.4 ms: 1.11x slower                                                                |
| unpickle_pure_python       | 133 us                                                      | 149 us: 1.11x slower                                                                 |
| generators                 | 19.5 ms                                                     | 21.8 ms: 1.12x slower                                                                |
| pprint_pformat             | 999 ms                                                      | 1.12 sec: 1.12x slower                                                               |
| async_tree_io_tg           | 518 ms                                                      | 581 ms: 1.12x slower                                                                 |
| coroutines                 | 12.8 ms                                                     | 14.3 ms: 1.12x slower                                                                |
| html5lib                   | 38.9 ms                                                     | 43.8 ms: 1.12x slower                                                                |
| scimark_lu                 | 53.0 ms                                                     | 59.6 ms: 1.13x slower                                                                |
| regex_compile              | 80.5 ms                                                     | 90.8 ms: 1.13x slower                                                                |
| sqlglot_optimize           | 32.9 ms                                                     | 37.1 ms: 1.13x slower                                                                |
| hexiom                     | 3.89 ms                                                     | 4.39 ms: 1.13x slower                                                                |
| fannkuch                   | 253 ms                                                      | 286 ms: 1.13x slower                                                                 |
| sqlglot_normalize          | 175 ms                                                      | 198 ms: 1.13x slower                                                                 |
| async_generators           | 223 ms                                                      | 253 ms: 1.13x slower                                                                 |
| pyflate                    | 283 ms                                                      | 321 ms: 1.13x slower                                                                 |
| json_dumps                 | 5.92 ms                                                     | 6.73 ms: 1.14x slower                                                                |
| nqueens                    | 56.7 ms                                                     | 64.6 ms: 1.14x slower                                                                |
| async_tree_io              | 521 ms                                                      | 594 ms: 1.14x slower                                                                 |
| scimark_monte_carlo        | 40.8 ms                                                     | 46.6 ms: 1.14x slower                                                                |
| pickle_pure_python         | 190 us                                                      | 217 us: 1.15x slower                                                                 |
| comprehensions             | 10.3 us                                                     | 11.8 us: 1.15x slower                                                                |
| chaos                      | 38.5 ms                                                     | 44.2 ms: 1.15x slower                                                                |
| richards_super             | 30.9 ms                                                     | 35.7 ms: 1.16x slower                                                                |
| richards                   | 27.3 ms                                                     | 31.7 ms: 1.16x slower                                                                |
| sqlglot_parse              | 771 us                                                      | 894 us: 1.16x slower                                                                 |
| sqlglot_transpile          | 956 us                                                      | 1.12 ms: 1.17x slower                                                                |
| django_template            | 22.4 ms                                                     | 26.3 ms: 1.18x slower                                                                |
| tomli_loads                | 1.39 sec                                                    | 1.65 sec: 1.18x slower                                                               |
| scimark_sor                | 76.2 ms                                                     | 90.1 ms: 1.18x slower                                                                |
| scimark_fft                | 172 ms                                                      | 204 ms: 1.18x slower                                                                 |
| deltablue                  | 1.92 ms                                                     | 2.28 ms: 1.19x slower                                                                |
| nbody                      | 68.4 ms                                                     | 82.9 ms: 1.21x slower                                                                |
| raytrace                   | 160 ms                                                      | 194 ms: 1.22x slower                                                                 |
| json                       | 3.19 ms                                                     | 4.46 ms: 1.40x slower                                                                |
| Geometric mean             | (ref)                                                       | 1.03x slower                                                                         |

Benchmark hidden because not significant (8): bench_thread_pool, async_tree_memoization, json_loads, python_startup_no_site, pathlib, regex_effbot, async_tree_none_tg, telco
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20241012-3.14.0a0-8278d07/bm-20241012-pythonperf1-amd64-Fidget%2dSpinner-fix_unsafe_refcounti-3.14.0a0-8278d07.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.030x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.07x
- 95% likely to have a slowdown of 1.06x
- 99% likely to have a slowdown of 1.05x

# Memory
- memory change: unknown