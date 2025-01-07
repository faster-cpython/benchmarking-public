# Results vs. base

- fork: kumaraditya303
- ref: fast_state
- machine: windows-amd64
- commit hash: 7de6e22
- commit date: 2025-01-07
- overall geometric mean: 1.001x slower
- HPT reliability: 98.10%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250105-pythonperf1-amd64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-pythonperf1-amd64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 224 ms                                                                      | 225 ms: 1.01x slower                                                      |
| docutils       | 1.67 sec                                                                    | 1.66 sec: 1.00x faster                                                    |
| html5lib       | 40.2 ms                                                                     | 39.7 ms: 1.01x faster                                                     |
| Geometric mean | (ref)                                                                       | 1.00x faster                                                              |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250105-pythonperf1-amd64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-pythonperf1-amd64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none_tg         | 172 ms                                                                      | 166 ms: 1.03x faster                                                      |
| async_tree_memoization     | 224 ms                                                                      | 218 ms: 1.03x faster                                                      |
| async_tree_io_tg           | 401 ms                                                                      | 393 ms: 1.02x faster                                                      |
| async_tree_cpu_io_mixed_tg | 347 ms                                                                      | 344 ms: 1.01x faster                                                      |
| async_tree_cpu_io_mixed    | 350 ms                                                                      | 347 ms: 1.01x faster                                                      |
| async_generators           | 238 ms                                                                      | 241 ms: 1.01x slower                                                      |
| coroutines                 | 13.4 ms                                                                     | 13.6 ms: 1.01x slower                                                     |
| Geometric mean             | (ref)                                                                       | 1.01x faster                                                              |

Benchmark hidden because not significant (4): async_tree_memoization_tg, async_tree_io, asyncio_websockets, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250105-pythonperf1-amd64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-pythonperf1-amd64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 53.0 ms                                                                     | 52.6 ms: 1.01x faster                                                     |
| pidigits       | 146 ms                                                                      | 146 ms: 1.00x faster                                                      |
| nbody          | 77.0 ms                                                                     | 77.8 ms: 1.01x slower                                                     |
| Geometric mean | (ref)                                                                       | 1.00x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250105-pythonperf1-amd64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-pythonperf1-amd64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_v8       | 24.6 ms                                                                     | 20.1 ms: 1.23x faster                                                     |
| regex_dna      | 127 ms                                                                      | 113 ms: 1.12x faster                                                      |
| regex_effbot   | 1.47 ms                                                                     | 1.42 ms: 1.04x faster                                                     |
| regex_compile  | 87.5 ms                                                                     | 88.0 ms: 1.01x slower                                                     |
| Geometric mean | (ref)                                                                       | 1.09x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20250105-pythonperf1-amd64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-pythonperf1-amd64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|--------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| json_dumps         | 6.70 ms                                                                     | 6.76 ms: 1.01x slower                                                     |
| xml_etree_generate | 57.4 ms                                                                     | 58.0 ms: 1.01x slower                                                     |
| pickle_pure_python | 221 us                                                                      | 225 us: 1.02x slower                                                      |
| xml_etree_process  | 40.2 ms                                                                     | 41.2 ms: 1.02x slower                                                     |
| tomli_loads        | 1.39 sec                                                                    | 1.43 sec: 1.03x slower                                                    |
| Geometric mean     | (ref)                                                                       | 1.01x slower                                                              |

Benchmark hidden because not significant (4): unpickle_pure_python, xml_etree_iterparse, xml_etree_parse, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250105-pythonperf1-amd64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-pythonperf1-amd64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|------------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 23.1 ms                                                                     | 24.1 ms: 1.04x slower                                                     |
| python_startup_no_site | 17.2 ms                                                                     | 18.0 ms: 1.05x slower                                                     |
| Geometric mean         | (ref)                                                                       | 1.04x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250105-pythonperf1-amd64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-pythonperf1-amd64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|-----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 6.87 ms                                                                     | 6.80 ms: 1.01x faster                                                     |
| genshi_text     | 16.7 ms                                                                     | 16.8 ms: 1.01x slower                                                     |
| django_template | 24.8 ms                                                                     | 25.6 ms: 1.03x slower                                                     |
| Geometric mean  | (ref)                                                                       | 1.01x slower                                                              |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20250105-pythonperf1-amd64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-pythonperf1-amd64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_v8                   | 24.6 ms                                                                     | 20.1 ms: 1.23x faster                                                     |
| regex_dna                  | 127 ms                                                                      | 113 ms: 1.12x faster                                                      |
| regex_effbot               | 1.47 ms                                                                     | 1.42 ms: 1.04x faster                                                     |
| async_tree_none_tg         | 172 ms                                                                      | 166 ms: 1.03x faster                                                      |
| raytrace                   | 193 ms                                                                      | 188 ms: 1.03x faster                                                      |
| async_tree_memoization     | 224 ms                                                                      | 218 ms: 1.03x faster                                                      |
| dulwich_log                | 42.7 ms                                                                     | 41.8 ms: 1.02x faster                                                     |
| async_tree_io_tg           | 401 ms                                                                      | 393 ms: 1.02x faster                                                      |
| json                       | 3.01 ms                                                                     | 2.97 ms: 1.01x faster                                                     |
| html5lib                   | 40.2 ms                                                                     | 39.7 ms: 1.01x faster                                                     |
| scimark_lu                 | 61.5 ms                                                                     | 60.9 ms: 1.01x faster                                                     |
| mako                       | 6.87 ms                                                                     | 6.80 ms: 1.01x faster                                                     |
| async_tree_cpu_io_mixed_tg | 347 ms                                                                      | 344 ms: 1.01x faster                                                      |
| async_tree_cpu_io_mixed    | 350 ms                                                                      | 347 ms: 1.01x faster                                                      |
| logging_simple             | 6.38 us                                                                     | 6.32 us: 1.01x faster                                                     |
| float                      | 53.0 ms                                                                     | 52.6 ms: 1.01x faster                                                     |
| logging_format             | 6.89 us                                                                     | 6.84 us: 1.01x faster                                                     |
| bpe_tokeniser              | 3.03 sec                                                                    | 3.01 sec: 1.00x faster                                                    |
| docutils                   | 1.67 sec                                                                    | 1.66 sec: 1.00x faster                                                    |
| pidigits                   | 146 ms                                                                      | 146 ms: 1.00x faster                                                      |
| deepcopy_memo              | 20.8 us                                                                     | 20.9 us: 1.00x slower                                                     |
| coverage                   | 46.5 ms                                                                     | 46.7 ms: 1.00x slower                                                     |
| sympy_expand               | 305 ms                                                                      | 306 ms: 1.00x slower                                                      |
| genshi_text                | 16.7 ms                                                                     | 16.8 ms: 1.01x slower                                                     |
| regex_compile              | 87.5 ms                                                                     | 88.0 ms: 1.01x slower                                                     |
| 2to3                       | 224 ms                                                                      | 225 ms: 1.01x slower                                                      |
| sqlglot_normalize          | 196 ms                                                                      | 197 ms: 1.01x slower                                                      |
| sympy_sum                  | 90.2 ms                                                                     | 90.7 ms: 1.01x slower                                                     |
| sqlglot_optimize           | 35.9 ms                                                                     | 36.1 ms: 1.01x slower                                                     |
| scimark_sor                | 90.3 ms                                                                     | 91.1 ms: 1.01x slower                                                     |
| sympy_integrate            | 13.4 ms                                                                     | 13.5 ms: 1.01x slower                                                     |
| sympy_str                  | 177 ms                                                                      | 179 ms: 1.01x slower                                                      |
| json_dumps                 | 6.70 ms                                                                     | 6.76 ms: 1.01x slower                                                     |
| nbody                      | 77.0 ms                                                                     | 77.8 ms: 1.01x slower                                                     |
| meteor_contest             | 77.0 ms                                                                     | 77.7 ms: 1.01x slower                                                     |
| xml_etree_generate         | 57.4 ms                                                                     | 58.0 ms: 1.01x slower                                                     |
| deepcopy_reduce            | 1.89 us                                                                     | 1.91 us: 1.01x slower                                                     |
| async_generators           | 238 ms                                                                      | 241 ms: 1.01x slower                                                      |
| shortest_path              | 349 ms                                                                      | 353 ms: 1.01x slower                                                      |
| logging_silent             | 61.6 ns                                                                     | 62.3 ns: 1.01x slower                                                     |
| coroutines                 | 13.4 ms                                                                     | 13.6 ms: 1.01x slower                                                     |
| pickle_pure_python         | 221 us                                                                      | 225 us: 1.02x slower                                                      |
| connected_components       | 316 ms                                                                      | 321 ms: 1.02x slower                                                      |
| scimark_fft                | 193 ms                                                                      | 196 ms: 1.02x slower                                                      |
| deepcopy                   | 184 us                                                                      | 187 us: 1.02x slower                                                      |
| crypto_pyaes               | 48.2 ms                                                                     | 49.1 ms: 1.02x slower                                                     |
| richards_super             | 34.1 ms                                                                     | 34.8 ms: 1.02x slower                                                     |
| scimark_monte_carlo        | 47.8 ms                                                                     | 48.8 ms: 1.02x slower                                                     |
| xml_etree_process          | 40.2 ms                                                                     | 41.2 ms: 1.02x slower                                                     |
| pprint_safe_repr           | 531 ms                                                                      | 543 ms: 1.02x slower                                                      |
| richards                   | 29.7 ms                                                                     | 30.5 ms: 1.03x slower                                                     |
| tomli_loads                | 1.39 sec                                                                    | 1.43 sec: 1.03x slower                                                    |
| django_template            | 24.8 ms                                                                     | 25.6 ms: 1.03x slower                                                     |
| pprint_pformat             | 1.07 sec                                                                    | 1.11 sec: 1.03x slower                                                    |
| comprehensions             | 11.9 us                                                                     | 12.3 us: 1.03x slower                                                     |
| scimark_sparse_mat_mult    | 2.60 ms                                                                     | 2.68 ms: 1.03x slower                                                     |
| spectral_norm              | 64.1 ms                                                                     | 66.4 ms: 1.04x slower                                                     |
| nqueens                    | 62.2 ms                                                                     | 64.4 ms: 1.04x slower                                                     |
| fannkuch                   | 266 ms                                                                      | 276 ms: 1.04x slower                                                      |
| python_startup             | 23.1 ms                                                                     | 24.1 ms: 1.04x slower                                                     |
| hexiom                     | 4.27 ms                                                                     | 4.45 ms: 1.04x slower                                                     |
| python_startup_no_site     | 17.2 ms                                                                     | 18.0 ms: 1.05x slower                                                     |
| mdp                        | 1.43 sec                                                                    | 1.52 sec: 1.07x slower                                                    |
| Geometric mean             | (ref)                                                                       | 1.00x slower                                                              |

Benchmark hidden because not significant (32): pyflate, pathlib, sphinx, async_tree_memoization_tg, async_tree_io, bench_mp_pool, sqlglot_parse, sqlglot_transpile, gc_traversal, asyncio_websockets, unpickle_pure_python, telco, chaos, pylint, generators, deltablue, create_gc_cycles, mypy2, xml_etree_iterparse, go, k_core, async_tree_none, sqlite_synth, bench_thread_pool, many_optionals, typing_runtime_protocols, xml_etree_parse, json_loads, pycparser, thrift, subparsers, genshi_xml

- Geometric mean (including insignificant results): 1.001x slower

# HPT report

- Reliability score: 98.10% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown