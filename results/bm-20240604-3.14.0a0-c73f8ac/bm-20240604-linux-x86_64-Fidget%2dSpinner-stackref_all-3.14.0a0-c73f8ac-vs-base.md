# Results vs. base

- fork: Fidget-Spinner
- ref: stackref_all
- machine: linux-x86_64
- commit hash: c73f8ac
- commit date: 2024-06-04
- overall geometric mean: 1.02x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240603-linux-x86_64-python-31a4fb3c74a028443634-3.14.0a0-31a4fb3 | bm-20240604-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-c73f8ac |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 269 ms                                                                | 272 ms: 1.01x slower                                                    |
| docutils       | 2.76 sec                                                              | 2.80 sec: 1.01x slower                                                  |
| html5lib       | 65.5 ms                                                               | 67.3 ms: 1.03x slower                                                   |
| tornado_http   | 93.8 ms                                                               | 94.6 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark          | bm-20240603-linux-x86_64-python-31a4fb3c74a028443634-3.14.0a0-31a4fb3 | bm-20240604-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-c73f8ac |
|--------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none_tg | 334 ms                                                                | 342 ms: 1.02x slower                                                    |
| Geometric mean     | (ref)                                                                 | 1.01x slower                                                            |

Benchmark hidden because not significant (7): async_tree_io_tg, async_tree_none, async_tree_memoization, async_tree_io, async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240603-linux-x86_64-python-31a4fb3c74a028443634-3.14.0a0-31a4fb3 | bm-20240604-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-c73f8ac |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pidigits       | 191 ms                                                                | 190 ms: 1.00x faster                                                    |
| float          | 78.3 ms                                                               | 79.0 ms: 1.01x slower                                                   |
| nbody          | 88.7 ms                                                               | 92.2 ms: 1.04x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240603-linux-x86_64-python-31a4fb3c74a028443634-3.14.0a0-31a4fb3 | bm-20240604-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-c73f8ac |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 25.3 ms                                                               | 24.9 ms: 1.02x faster                                                   |
| regex_dna      | 225 ms                                                                | 221 ms: 1.02x faster                                                    |
| regex_compile  | 132 ms                                                                | 136 ms: 1.03x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                            |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240603-linux-x86_64-python-31a4fb3c74a028443634-3.14.0a0-31a4fb3 | bm-20240604-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-c73f8ac |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle             | 15.6 us                                                               | 15.1 us: 1.03x faster                                                   |
| unpickle_list        | 5.35 us                                                               | 5.25 us: 1.02x faster                                                   |
| xml_etree_process    | 60.5 ms                                                               | 61.1 ms: 1.01x slower                                                   |
| pickle               | 11.8 us                                                               | 11.9 us: 1.01x slower                                                   |
| xml_etree_generate   | 86.3 ms                                                               | 87.5 ms: 1.01x slower                                                   |
| pickle_dict          | 35.5 us                                                               | 36.2 us: 1.02x slower                                                   |
| xml_etree_iterparse  | 106 ms                                                                | 108 ms: 1.02x slower                                                    |
| pickle_pure_python   | 304 us                                                                | 312 us: 1.03x slower                                                    |
| tomli_loads          | 2.15 sec                                                              | 2.23 sec: 1.04x slower                                                  |
| pickle_list          | 5.06 us                                                               | 5.35 us: 1.06x slower                                                   |
| unpickle_pure_python | 215 us                                                                | 227 us: 1.06x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                            |

Benchmark hidden because not significant (3): json_loads, xml_etree_parse, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240603-linux-x86_64-python-31a4fb3c74a028443634-3.14.0a0-31a4fb3 | bm-20240604-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-c73f8ac |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 7.09 ms                                                               | 7.11 ms: 1.00x slower                                                   |
| python_startup         | 10.6 ms                                                               | 10.7 ms: 1.01x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240603-linux-x86_64-python-31a4fb3c74a028443634-3.14.0a0-31a4fb3 | bm-20240604-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-c73f8ac |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text     | 23.7 ms                                                               | 23.3 ms: 1.02x faster                                                   |
| genshi_xml      | 51.0 ms                                                               | 53.9 ms: 1.06x slower                                                   |
| django_template | 34.2 ms                                                               | 36.1 ms: 1.06x slower                                                   |
| mako            | 10.8 ms                                                               | 12.0 ms: 1.11x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.05x slower                                                            |

All benchmarks:
===============

| Benchmark                | bm-20240603-linux-x86_64-python-31a4fb3c74a028443634-3.14.0a0-31a4fb3 | bm-20240604-linux-x86_64-Fidget%2dSpinner-stackref_all-3.14.0a0-c73f8ac |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle                 | 15.6 us                                                               | 15.1 us: 1.03x faster                                                   |
| unpickle_list            | 5.35 us                                                               | 5.25 us: 1.02x faster                                                   |
| pyflate                  | 480 ms                                                                | 471 ms: 1.02x faster                                                    |
| regex_v8                 | 25.3 ms                                                               | 24.9 ms: 1.02x faster                                                   |
| scimark_sparse_mat_mult  | 5.08 ms                                                               | 5.00 ms: 1.02x faster                                                   |
| genshi_text              | 23.7 ms                                                               | 23.3 ms: 1.02x faster                                                   |
| regex_dna                | 225 ms                                                                | 221 ms: 1.02x faster                                                    |
| sqlite_synth             | 2.97 us                                                               | 2.94 us: 1.01x faster                                                   |
| richards                 | 48.6 ms                                                               | 48.2 ms: 1.01x faster                                                   |
| richards_super           | 54.8 ms                                                               | 54.4 ms: 1.01x faster                                                   |
| scimark_sor              | 132 ms                                                                | 131 ms: 1.01x faster                                                    |
| create_gc_cycles         | 1.78 ms                                                               | 1.77 ms: 1.00x faster                                                   |
| pidigits                 | 191 ms                                                                | 190 ms: 1.00x faster                                                    |
| python_startup_no_site   | 7.09 ms                                                               | 7.11 ms: 1.00x slower                                                   |
| asyncio_tcp_ssl          | 1.84 sec                                                              | 1.85 sec: 1.00x slower                                                  |
| python_startup           | 10.6 ms                                                               | 10.7 ms: 1.01x slower                                                   |
| generators               | 29.5 ms                                                               | 29.7 ms: 1.01x slower                                                   |
| sympy_sum                | 154 ms                                                                | 155 ms: 1.01x slower                                                    |
| gc_traversal             | 3.92 ms                                                               | 3.95 ms: 1.01x slower                                                   |
| float                    | 78.3 ms                                                               | 79.0 ms: 1.01x slower                                                   |
| xml_etree_process        | 60.5 ms                                                               | 61.1 ms: 1.01x slower                                                   |
| tornado_http             | 93.8 ms                                                               | 94.6 ms: 1.01x slower                                                   |
| 2to3                     | 269 ms                                                                | 272 ms: 1.01x slower                                                    |
| sqlglot_normalize        | 110 ms                                                                | 111 ms: 1.01x slower                                                    |
| sympy_integrate          | 20.3 ms                                                               | 20.5 ms: 1.01x slower                                                   |
| telco                    | 8.35 ms                                                               | 8.45 ms: 1.01x slower                                                   |
| sqlglot_optimize         | 54.9 ms                                                               | 55.6 ms: 1.01x slower                                                   |
| pickle                   | 11.8 us                                                               | 11.9 us: 1.01x slower                                                   |
| sympy_expand             | 468 ms                                                                | 474 ms: 1.01x slower                                                    |
| dulwich_log              | 65.1 ms                                                               | 66.0 ms: 1.01x slower                                                   |
| docutils                 | 2.76 sec                                                              | 2.80 sec: 1.01x slower                                                  |
| xml_etree_generate       | 86.3 ms                                                               | 87.5 ms: 1.01x slower                                                   |
| sympy_str                | 278 ms                                                                | 282 ms: 1.02x slower                                                    |
| go                       | 143 ms                                                                | 145 ms: 1.02x slower                                                    |
| async_generators         | 444 ms                                                                | 452 ms: 1.02x slower                                                    |
| crypto_pyaes             | 75.3 ms                                                               | 76.6 ms: 1.02x slower                                                   |
| logging_format           | 6.37 us                                                               | 6.48 us: 1.02x slower                                                   |
| pickle_dict              | 35.5 us                                                               | 36.2 us: 1.02x slower                                                   |
| deepcopy                 | 366 us                                                                | 373 us: 1.02x slower                                                    |
| deepcopy_reduce          | 3.29 us                                                               | 3.36 us: 1.02x slower                                                   |
| async_tree_none_tg       | 334 ms                                                                | 342 ms: 1.02x slower                                                    |
| xml_etree_iterparse      | 106 ms                                                                | 108 ms: 1.02x slower                                                    |
| nqueens                  | 80.1 ms                                                               | 82.1 ms: 1.03x slower                                                   |
| pickle_pure_python       | 304 us                                                                | 312 us: 1.03x slower                                                    |
| html5lib                 | 65.5 ms                                                               | 67.3 ms: 1.03x slower                                                   |
| logging_simple           | 5.69 us                                                               | 5.84 us: 1.03x slower                                                   |
| deltablue                | 3.25 ms                                                               | 3.35 ms: 1.03x slower                                                   |
| regex_compile            | 132 ms                                                                | 136 ms: 1.03x slower                                                    |
| sqlglot_parse            | 1.31 ms                                                               | 1.34 ms: 1.03x slower                                                   |
| sqlglot_transpile        | 1.61 ms                                                               | 1.66 ms: 1.03x slower                                                   |
| chaos                    | 60.0 ms                                                               | 62.0 ms: 1.03x slower                                                   |
| scimark_lu               | 114 ms                                                                | 118 ms: 1.03x slower                                                    |
| coroutines               | 22.9 ms                                                               | 23.7 ms: 1.03x slower                                                   |
| meteor_contest           | 108 ms                                                                | 111 ms: 1.04x slower                                                    |
| typing_runtime_protocols | 165 us                                                                | 171 us: 1.04x slower                                                    |
| scimark_monte_carlo      | 67.4 ms                                                               | 69.9 ms: 1.04x slower                                                   |
| comprehensions           | 16.5 us                                                               | 17.1 us: 1.04x slower                                                   |
| tomli_loads              | 2.15 sec                                                              | 2.23 sec: 1.04x slower                                                  |
| nbody                    | 88.7 ms                                                               | 92.2 ms: 1.04x slower                                                   |
| pprint_pformat           | 1.52 sec                                                              | 1.58 sec: 1.04x slower                                                  |
| pprint_safe_repr         | 749 ms                                                                | 780 ms: 1.04x slower                                                    |
| hexiom                   | 6.13 ms                                                               | 6.38 ms: 1.04x slower                                                   |
| deepcopy_memo            | 39.4 us                                                               | 41.0 us: 1.04x slower                                                   |
| spectral_norm            | 113 ms                                                                | 118 ms: 1.04x slower                                                    |
| fannkuch                 | 390 ms                                                                | 406 ms: 1.04x slower                                                    |
| logging_silent           | 101 ns                                                                | 107 ns: 1.05x slower                                                    |
| scimark_fft              | 357 ms                                                                | 376 ms: 1.05x slower                                                    |
| genshi_xml               | 51.0 ms                                                               | 53.9 ms: 1.06x slower                                                   |
| django_template          | 34.2 ms                                                               | 36.1 ms: 1.06x slower                                                   |
| pickle_list              | 5.06 us                                                               | 5.35 us: 1.06x slower                                                   |
| unpickle_pure_python     | 215 us                                                                | 227 us: 1.06x slower                                                    |
| mdp                      | 2.56 sec                                                              | 2.76 sec: 1.08x slower                                                  |
| mako                     | 10.8 ms                                                               | 12.0 ms: 1.11x slower                                                   |
| Geometric mean           | (ref)                                                                 | 1.02x slower                                                            |

Benchmark hidden because not significant (23): asyncio_websockets, pathlib, async_tree_io_tg, raytrace, coverage, thrift, pycparser, asyncio_tcp, bench_mp_pool, async_tree_none, json_loads, xml_etree_parse, json_dumps, json, async_tree_memoization, regex_effbot, bench_thread_pool, async_tree_io, dask, pylint, async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x