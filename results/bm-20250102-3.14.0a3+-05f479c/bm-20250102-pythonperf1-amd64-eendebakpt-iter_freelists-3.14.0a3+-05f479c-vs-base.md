# Results vs. base

- fork: eendebakpt
- ref: iter_freelists
- machine: windows-amd64
- commit hash: 05f479c
- commit date: 2025-01-02
- overall geometric mean: 1.002x faster
- HPT reliability: 62.72%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250102-pythonperf1-amd64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 | bm-20250102-pythonperf1-amd64-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| docutils       | 1.67 sec                                                                    | 1.65 sec: 1.01x faster                                                    |
| Geometric mean | (ref)                                                                       | 1.00x faster                                                              |

Benchmark hidden because not significant (3): 2to3, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250102-pythonperf1-amd64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 | bm-20250102-pythonperf1-amd64-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|----------------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| asyncio_websockets         | 316 ms                                                                      | 304 ms: 1.04x faster                                                      |
| async_tree_memoization     | 225 ms                                                                      | 221 ms: 1.02x faster                                                      |
| async_tree_cpu_io_mixed    | 352 ms                                                                      | 347 ms: 1.01x faster                                                      |
| async_tree_cpu_io_mixed_tg | 346 ms                                                                      | 342 ms: 1.01x faster                                                      |
| async_tree_none_tg         | 171 ms                                                                      | 169 ms: 1.01x faster                                                      |
| async_tree_io              | 408 ms                                                                      | 403 ms: 1.01x faster                                                      |
| coroutines                 | 13.6 ms                                                                     | 13.4 ms: 1.01x faster                                                     |
| async_generators           | 232 ms                                                                      | 240 ms: 1.04x slower                                                      |
| Geometric mean             | (ref)                                                                       | 1.01x faster                                                              |

Benchmark hidden because not significant (3): async_tree_io_tg, async_tree_memoization_tg, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250102-pythonperf1-amd64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 | bm-20250102-pythonperf1-amd64-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 51.8 ms                                                                     | 52.7 ms: 1.02x slower                                                     |
| nbody          | 75.9 ms                                                                     | 77.4 ms: 1.02x slower                                                     |
| Geometric mean | (ref)                                                                       | 1.01x slower                                                              |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250102-pythonperf1-amd64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 | bm-20250102-pythonperf1-amd64-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_v8       | 24.6 ms                                                                     | 20.8 ms: 1.18x faster                                                     |
| regex_dna      | 124 ms                                                                      | 118 ms: 1.06x faster                                                      |
| Geometric mean | (ref)                                                                       | 1.06x faster                                                              |

Benchmark hidden because not significant (2): regex_effbot, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250102-pythonperf1-amd64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 | bm-20250102-pythonperf1-amd64-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|----------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| json_loads           | 14.4 us                                                                     | 14.0 us: 1.03x faster                                                     |
| xml_etree_generate   | 57.0 ms                                                                     | 56.4 ms: 1.01x faster                                                     |
| xml_etree_iterparse  | 62.1 ms                                                                     | 62.6 ms: 1.01x slower                                                     |
| xml_etree_parse      | 86.7 ms                                                                     | 88.8 ms: 1.02x slower                                                     |
| pickle_pure_python   | 222 us                                                                      | 228 us: 1.03x slower                                                      |
| unpickle_pure_python | 147 us                                                                      | 157 us: 1.07x slower                                                      |
| Geometric mean       | (ref)                                                                       | 1.01x slower                                                              |

Benchmark hidden because not significant (3): xml_etree_process, tomli_loads, json_dumps

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250102-pythonperf1-amd64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 | bm-20250102-pythonperf1-amd64-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|-----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_text     | 16.7 ms                                                                     | 15.7 ms: 1.06x faster                                                     |
| django_template | 25.3 ms                                                                     | 24.4 ms: 1.04x faster                                                     |
| genshi_xml      | 35.4 ms                                                                     | 34.4 ms: 1.03x faster                                                     |
| mako            | 6.77 ms                                                                     | 6.94 ms: 1.02x slower                                                     |
| Geometric mean  | (ref)                                                                       | 1.03x faster                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20250102-pythonperf1-amd64-python-e1baa778f602ede66831-3.14.0a3+-e1baa77 | bm-20250102-pythonperf1-amd64-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|----------------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_v8                   | 24.6 ms                                                                     | 20.8 ms: 1.18x faster                                                     |
| genshi_text                | 16.7 ms                                                                     | 15.7 ms: 1.06x faster                                                     |
| regex_dna                  | 124 ms                                                                      | 118 ms: 1.06x faster                                                      |
| telco                      | 4.77 ms                                                                     | 4.58 ms: 1.04x faster                                                     |
| asyncio_websockets         | 316 ms                                                                      | 304 ms: 1.04x faster                                                      |
| django_template            | 25.3 ms                                                                     | 24.4 ms: 1.04x faster                                                     |
| nqueens                    | 65.1 ms                                                                     | 62.9 ms: 1.04x faster                                                     |
| sqlglot_optimize           | 35.7 ms                                                                     | 34.6 ms: 1.03x faster                                                     |
| deltablue                  | 2.29 ms                                                                     | 2.22 ms: 1.03x faster                                                     |
| json_loads                 | 14.4 us                                                                     | 14.0 us: 1.03x faster                                                     |
| genshi_xml                 | 35.4 ms                                                                     | 34.4 ms: 1.03x faster                                                     |
| many_optionals             | 440 us                                                                      | 431 us: 1.02x faster                                                      |
| coverage                   | 47.3 ms                                                                     | 46.3 ms: 1.02x faster                                                     |
| sqlglot_normalize          | 193 ms                                                                      | 190 ms: 1.02x faster                                                      |
| bpe_tokeniser              | 3.01 sec                                                                    | 2.96 sec: 1.02x faster                                                    |
| scimark_monte_carlo        | 48.2 ms                                                                     | 47.3 ms: 1.02x faster                                                     |
| async_tree_memoization     | 225 ms                                                                      | 221 ms: 1.02x faster                                                      |
| async_tree_cpu_io_mixed    | 352 ms                                                                      | 347 ms: 1.01x faster                                                      |
| sympy_integrate            | 13.4 ms                                                                     | 13.2 ms: 1.01x faster                                                     |
| spectral_norm              | 63.7 ms                                                                     | 62.8 ms: 1.01x faster                                                     |
| sqlglot_transpile          | 1.12 ms                                                                     | 1.10 ms: 1.01x faster                                                     |
| sympy_expand               | 305 ms                                                                      | 301 ms: 1.01x faster                                                      |
| async_tree_cpu_io_mixed_tg | 346 ms                                                                      | 342 ms: 1.01x faster                                                      |
| docutils                   | 1.67 sec                                                                    | 1.65 sec: 1.01x faster                                                    |
| async_tree_none_tg         | 171 ms                                                                      | 169 ms: 1.01x faster                                                      |
| async_tree_io              | 408 ms                                                                      | 403 ms: 1.01x faster                                                      |
| xml_etree_generate         | 57.0 ms                                                                     | 56.4 ms: 1.01x faster                                                     |
| coroutines                 | 13.6 ms                                                                     | 13.4 ms: 1.01x faster                                                     |
| sympy_sum                  | 90.7 ms                                                                     | 89.9 ms: 1.01x faster                                                     |
| sympy_str                  | 178 ms                                                                      | 177 ms: 1.01x faster                                                      |
| mypy2                      | 639 ms                                                                      | 634 ms: 1.01x faster                                                      |
| typing_runtime_protocols   | 110 us                                                                      | 109 us: 1.01x faster                                                      |
| scimark_sor                | 91.3 ms                                                                     | 90.7 ms: 1.01x faster                                                     |
| meteor_contest             | 77.5 ms                                                                     | 77.1 ms: 1.01x faster                                                     |
| scimark_sparse_mat_mult    | 2.70 ms                                                                     | 2.68 ms: 1.01x faster                                                     |
| sqlglot_parse              | 900 us                                                                      | 896 us: 1.00x faster                                                      |
| shortest_path              | 349 ms                                                                      | 351 ms: 1.00x slower                                                      |
| deepcopy                   | 183 us                                                                      | 184 us: 1.01x slower                                                      |
| xml_etree_iterparse        | 62.1 ms                                                                     | 62.6 ms: 1.01x slower                                                     |
| go                         | 88.2 ms                                                                     | 88.9 ms: 1.01x slower                                                     |
| subparsers                 | 16.0 ms                                                                     | 16.2 ms: 1.01x slower                                                     |
| deepcopy_reduce            | 1.87 us                                                                     | 1.89 us: 1.01x slower                                                     |
| k_core                     | 1.67 sec                                                                    | 1.70 sec: 1.01x slower                                                    |
| fannkuch                   | 277 ms                                                                      | 281 ms: 1.02x slower                                                      |
| pprint_safe_repr           | 541 ms                                                                      | 550 ms: 1.02x slower                                                      |
| float                      | 51.8 ms                                                                     | 52.7 ms: 1.02x slower                                                     |
| nbody                      | 75.9 ms                                                                     | 77.4 ms: 1.02x slower                                                     |
| hexiom                     | 4.44 ms                                                                     | 4.53 ms: 1.02x slower                                                     |
| crypto_pyaes               | 47.8 ms                                                                     | 48.8 ms: 1.02x slower                                                     |
| xml_etree_parse            | 86.7 ms                                                                     | 88.8 ms: 1.02x slower                                                     |
| mako                       | 6.77 ms                                                                     | 6.94 ms: 1.02x slower                                                     |
| pickle_pure_python         | 222 us                                                                      | 228 us: 1.03x slower                                                      |
| raytrace                   | 197 ms                                                                      | 202 ms: 1.03x slower                                                      |
| richards_super             | 34.8 ms                                                                     | 35.8 ms: 1.03x slower                                                     |
| generators                 | 21.2 ms                                                                     | 21.7 ms: 1.03x slower                                                     |
| logging_format             | 6.65 us                                                                     | 6.83 us: 1.03x slower                                                     |
| scimark_lu                 | 63.2 ms                                                                     | 65.0 ms: 1.03x slower                                                     |
| logging_simple             | 6.25 us                                                                     | 6.43 us: 1.03x slower                                                     |
| richards                   | 30.7 ms                                                                     | 31.8 ms: 1.04x slower                                                     |
| async_generators           | 232 ms                                                                      | 240 ms: 1.04x slower                                                      |
| deepcopy_memo              | 20.5 us                                                                     | 21.4 us: 1.05x slower                                                     |
| pprint_pformat             | 1.08 sec                                                                    | 1.14 sec: 1.05x slower                                                    |
| logging_silent             | 62.4 ns                                                                     | 66.4 ns: 1.06x slower                                                     |
| unpickle_pure_python       | 147 us                                                                      | 157 us: 1.07x slower                                                      |
| json                       | 2.91 ms                                                                     | 3.18 ms: 1.09x slower                                                     |
| Geometric mean             | (ref)                                                                       | 1.00x faster                                                              |

Benchmark hidden because not significant (30): mdp, bench_thread_pool, sphinx, pylint, gc_traversal, create_gc_cycles, pathlib, pyflate, xml_etree_process, bench_mp_pool, regex_effbot, sqlite_synth, scimark_fft, dulwich_log, chaos, pidigits, async_tree_io_tg, regex_compile, comprehensions, 2to3, tomli_loads, async_tree_memoization_tg, python_startup, json_dumps, connected_components, python_startup_no_site, html5lib, pycparser, async_tree_none, thrift

- Geometric mean (including insignificant results): 1.002x faster

# HPT report

- Reliability score: 62.72% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown