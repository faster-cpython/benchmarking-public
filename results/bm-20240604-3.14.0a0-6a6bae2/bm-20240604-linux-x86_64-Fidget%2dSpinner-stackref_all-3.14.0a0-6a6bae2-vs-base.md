# Results vs. base

- fork: Fidget-Spinner
- ref: stackref_all
- machine: linux-x86_64
- commit hash: 6a6bae2
- commit date: 2024-06-04
- overall geometric mean: 1.00x slower
- HPT reliability: 90.27%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240603-linux-x86_64-python-31a4fb3c74a028443634-3.14.0a0-31a4fb3 | bm-20240604-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-6a6bae2 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 269 ms                                                                | 270 ms: 1.00x slower                                                    |
| docutils       | 2.76 sec                                                              | 2.78 sec: 1.01x slower                                                  |
| html5lib       | 65.5 ms                                                               | 67.1 ms: 1.02x slower                                                   |
| tornado_http   | 93.8 ms                                                               | 94.0 ms: 1.00x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_io_tg, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_memoization, async_tree_none, async_tree_io, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240603-linux-x86_64-python-31a4fb3c74a028443634-3.14.0a0-31a4fb3 | bm-20240604-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-6a6bae2 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 88.7 ms                                                               | 88.1 ms: 1.01x faster                                                   |
| float          | 78.3 ms                                                               | 77.8 ms: 1.01x faster                                                   |
| pidigits       | 191 ms                                                                | 190 ms: 1.00x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240603-linux-x86_64-python-31a4fb3c74a028443634-3.14.0a0-31a4fb3 | bm-20240604-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-6a6bae2 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 3.69 ms                                                               | 3.75 ms: 1.02x slower                                                   |
| regex_dna      | 225 ms                                                                | 229 ms: 1.02x slower                                                    |
| regex_compile  | 132 ms                                                                | 135 ms: 1.03x slower                                                    |
| regex_v8       | 25.3 ms                                                               | 26.2 ms: 1.04x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240603-linux-x86_64-python-31a4fb3c74a028443634-3.14.0a0-31a4fb3 | bm-20240604-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-6a6bae2 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle             | 15.6 us                                                               | 15.2 us: 1.03x faster                                                   |
| xml_etree_process    | 60.5 ms                                                               | 59.9 ms: 1.01x faster                                                   |
| json_loads           | 29.1 us                                                               | 28.8 us: 1.01x faster                                                   |
| xml_etree_generate   | 86.3 ms                                                               | 85.8 ms: 1.01x faster                                                   |
| pickle_dict          | 35.5 us                                                               | 35.6 us: 1.00x slower                                                   |
| json_dumps           | 10.6 ms                                                               | 10.6 ms: 1.00x slower                                                   |
| pickle_pure_python   | 304 us                                                                | 306 us: 1.00x slower                                                    |
| pickle               | 11.8 us                                                               | 11.9 us: 1.01x slower                                                   |
| unpickle_list        | 5.35 us                                                               | 5.42 us: 1.01x slower                                                   |
| xml_etree_iterparse  | 106 ms                                                                | 108 ms: 1.02x slower                                                    |
| unpickle_pure_python | 215 us                                                                | 221 us: 1.03x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.00x slower                                                            |

Benchmark hidden because not significant (3): tomli_loads, pickle_list, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240603-linux-x86_64-python-31a4fb3c74a028443634-3.14.0a0-31a4fb3 | bm-20240604-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-6a6bae2 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 7.09 ms                                                               | 7.13 ms: 1.00x slower                                                   |
| python_startup         | 10.6 ms                                                               | 10.7 ms: 1.01x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.01x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240603-linux-x86_64-python-31a4fb3c74a028443634-3.14.0a0-31a4fb3 | bm-20240604-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-6a6bae2 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text     | 23.7 ms                                                               | 23.3 ms: 1.02x faster                                                   |
| genshi_xml      | 51.0 ms                                                               | 52.0 ms: 1.02x slower                                                   |
| django_template | 34.2 ms                                                               | 34.9 ms: 1.02x slower                                                   |
| mako            | 10.8 ms                                                               | 11.4 ms: 1.05x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.02x slower                                                            |

All benchmarks:
===============

| Benchmark               | bm-20240603-linux-x86_64-python-31a4fb3c74a028443634-3.14.0a0-31a4fb3 | bm-20240604-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-6a6bae2 |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| scimark_sor             | 132 ms                                                                | 126 ms: 1.04x faster                                                    |
| gc_traversal            | 3.92 ms                                                               | 3.81 ms: 1.03x faster                                                   |
| scimark_sparse_mat_mult | 5.08 ms                                                               | 4.94 ms: 1.03x faster                                                   |
| unpickle                | 15.6 us                                                               | 15.2 us: 1.03x faster                                                   |
| raytrace                | 270 ms                                                                | 263 ms: 1.02x faster                                                    |
| crypto_pyaes            | 75.3 ms                                                               | 73.7 ms: 1.02x faster                                                   |
| genshi_text             | 23.7 ms                                                               | 23.3 ms: 1.02x faster                                                   |
| richards                | 48.6 ms                                                               | 47.7 ms: 1.02x faster                                                   |
| logging_silent          | 101 ns                                                                | 99.6 ns: 1.02x faster                                                   |
| richards_super          | 54.8 ms                                                               | 54.0 ms: 1.01x faster                                                   |
| pyflate                 | 480 ms                                                                | 474 ms: 1.01x faster                                                    |
| xml_etree_process       | 60.5 ms                                                               | 59.9 ms: 1.01x faster                                                   |
| spectral_norm           | 113 ms                                                                | 112 ms: 1.01x faster                                                    |
| json_loads              | 29.1 us                                                               | 28.8 us: 1.01x faster                                                   |
| go                      | 143 ms                                                                | 142 ms: 1.01x faster                                                    |
| nbody                   | 88.7 ms                                                               | 88.1 ms: 1.01x faster                                                   |
| asyncio_tcp             | 505 ms                                                                | 501 ms: 1.01x faster                                                    |
| float                   | 78.3 ms                                                               | 77.8 ms: 1.01x faster                                                   |
| xml_etree_generate      | 86.3 ms                                                               | 85.8 ms: 1.01x faster                                                   |
| sqlglot_normalize       | 110 ms                                                                | 109 ms: 1.00x faster                                                    |
| create_gc_cycles        | 1.78 ms                                                               | 1.78 ms: 1.00x faster                                                   |
| pidigits                | 191 ms                                                                | 190 ms: 1.00x faster                                                    |
| asyncio_tcp_ssl         | 1.84 sec                                                              | 1.84 sec: 1.00x faster                                                  |
| sqlglot_optimize        | 54.9 ms                                                               | 54.8 ms: 1.00x faster                                                   |
| tornado_http            | 93.8 ms                                                               | 94.0 ms: 1.00x slower                                                   |
| pickle_dict             | 35.5 us                                                               | 35.6 us: 1.00x slower                                                   |
| 2to3                    | 269 ms                                                                | 270 ms: 1.00x slower                                                    |
| sympy_sum               | 154 ms                                                                | 155 ms: 1.00x slower                                                    |
| json_dumps              | 10.6 ms                                                               | 10.6 ms: 1.00x slower                                                   |
| pickle_pure_python      | 304 us                                                                | 306 us: 1.00x slower                                                    |
| sympy_expand            | 468 ms                                                                | 470 ms: 1.00x slower                                                    |
| python_startup_no_site  | 7.09 ms                                                               | 7.13 ms: 1.00x slower                                                   |
| docutils                | 2.76 sec                                                              | 2.78 sec: 1.01x slower                                                  |
| async_generators        | 444 ms                                                                | 447 ms: 1.01x slower                                                    |
| sympy_str               | 278 ms                                                                | 279 ms: 1.01x slower                                                    |
| deepcopy_reduce         | 3.29 us                                                               | 3.32 us: 1.01x slower                                                   |
| python_startup          | 10.6 ms                                                               | 10.7 ms: 1.01x slower                                                   |
| pprint_pformat          | 1.52 sec                                                              | 1.54 sec: 1.01x slower                                                  |
| pickle                  | 11.8 us                                                               | 11.9 us: 1.01x slower                                                   |
| meteor_contest          | 108 ms                                                                | 109 ms: 1.01x slower                                                    |
| unpickle_list           | 5.35 us                                                               | 5.42 us: 1.01x slower                                                   |
| regex_effbot            | 3.69 ms                                                               | 3.75 ms: 1.02x slower                                                   |
| scimark_monte_carlo     | 67.4 ms                                                               | 68.5 ms: 1.02x slower                                                   |
| xml_etree_iterparse     | 106 ms                                                                | 108 ms: 1.02x slower                                                    |
| genshi_xml              | 51.0 ms                                                               | 52.0 ms: 1.02x slower                                                   |
| django_template         | 34.2 ms                                                               | 34.9 ms: 1.02x slower                                                   |
| regex_dna               | 225 ms                                                                | 229 ms: 1.02x slower                                                    |
| coroutines              | 22.9 ms                                                               | 23.4 ms: 1.02x slower                                                   |
| scimark_lu              | 114 ms                                                                | 117 ms: 1.02x slower                                                    |
| comprehensions          | 16.5 us                                                               | 16.9 us: 1.02x slower                                                   |
| html5lib                | 65.5 ms                                                               | 67.1 ms: 1.02x slower                                                   |
| regex_compile           | 132 ms                                                                | 135 ms: 1.03x slower                                                    |
| hexiom                  | 6.13 ms                                                               | 6.29 ms: 1.03x slower                                                   |
| unpickle_pure_python    | 215 us                                                                | 221 us: 1.03x slower                                                    |
| pycparser               | 1.17 sec                                                              | 1.21 sec: 1.03x slower                                                  |
| fannkuch                | 390 ms                                                                | 403 ms: 1.04x slower                                                    |
| regex_v8                | 25.3 ms                                                               | 26.2 ms: 1.04x slower                                                   |
| mako                    | 10.8 ms                                                               | 11.4 ms: 1.05x slower                                                   |
| scimark_fft             | 357 ms                                                                | 379 ms: 1.06x slower                                                    |
| mdp                     | 2.56 sec                                                              | 2.73 sec: 1.07x slower                                                  |
| Geometric mean          | (ref)                                                                 | 1.00x slower                                                            |

Benchmark hidden because not significant (36): asyncio_websockets, async_tree_io_tg, async_tree_cpu_io_mixed, json, async_tree_cpu_io_mixed_tg, chaos, async_tree_memoization_tg, thrift, pathlib, async_tree_memoization, bench_thread_pool, async_tree_none, deepcopy_memo, coverage, logging_format, dulwich_log, tomli_loads, deltablue, sqlite_synth, pylint, generators, pickle_list, async_tree_io, sqlglot_parse, telco, logging_simple, bench_mp_pool, sympy_integrate, nqueens, sqlglot_transpile, dask, xml_etree_parse, deepcopy, typing_runtime_protocols, pprint_safe_repr, async_tree_none_tg

# HPT report

- Reliability score: 90.27% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x