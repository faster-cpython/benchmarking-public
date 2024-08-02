# Results vs. base

- fork: gvanrossum
- ref: backoff_counter_woes
- machine: linux-x86_64
- commit hash: 4c1049b
- commit date: 2024-05-04
- overall geometric mean: 1.00x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240504-linux-x86_64-python-5f547585fa56c94c5d83-3.13.0a6+-5f54758 | bm-20240504-linux-x86_64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 272 ms                                                                 | 272 ms: 1.00x faster                                                       |
| html5lib       | 68.4 ms                                                                | 68.8 ms: 1.01x slower                                                      |
| tornado_http   | 95.5 ms                                                                | 94.7 ms: 1.01x faster                                                      |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                               |

Benchmark hidden because not significant (2): chameleon, docutils

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_none_tg, async_tree_io_tg, async_tree_none, async_tree_io, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240504-linux-x86_64-python-5f547585fa56c94c5d83-3.13.0a6+-5f54758 | bm-20240504-linux-x86_64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 79.0 ms                                                                | 78.5 ms: 1.01x faster                                                      |
| nbody          | 87.5 ms                                                                | 90.4 ms: 1.03x slower                                                      |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240504-linux-x86_64-python-5f547585fa56c94c5d83-3.13.0a6+-5f54758 | bm-20240504-linux-x86_64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_v8       | 26.6 ms                                                                | 26.0 ms: 1.02x faster                                                      |
| regex_effbot   | 3.78 ms                                                                | 3.79 ms: 1.00x slower                                                      |
| regex_dna      | 224 ms                                                                 | 232 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                               |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240504-linux-x86_64-python-5f547585fa56c94c5d83-3.13.0a6+-5f54758 | bm-20240504-linux-x86_64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|----------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle_list          | 5.12 us                                                                | 5.00 us: 1.02x faster                                                      |
| json_dumps           | 10.6 ms                                                                | 10.5 ms: 1.01x faster                                                      |
| xml_etree_generate   | 88.6 ms                                                                | 88.1 ms: 1.01x faster                                                      |
| pickle_pure_python   | 312 us                                                                 | 314 us: 1.00x slower                                                       |
| unpickle_pure_python | 223 us                                                                 | 225 us: 1.01x slower                                                       |
| unpickle_list        | 5.37 us                                                                | 5.44 us: 1.01x slower                                                      |
| pickle               | 11.8 us                                                                | 12.0 us: 1.01x slower                                                      |
| pickle_dict          | 35.0 us                                                                | 36.4 us: 1.04x slower                                                      |
| Geometric mean       | (ref)                                                                  | 1.00x slower                                                               |

Benchmark hidden because not significant (6): xml_etree_parse, json_loads, xml_etree_iterparse, tomli_loads, xml_etree_process, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240504-linux-x86_64-python-5f547585fa56c94c5d83-3.13.0a6+-5f54758 | bm-20240504-linux-x86_64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 7.20 ms                                                                | 7.21 ms: 1.00x slower                                                      |
| python_startup         | 10.7 ms                                                                | 10.7 ms: 1.00x slower                                                      |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240504-linux-x86_64-python-5f547585fa56c94c5d83-3.13.0a6+-5f54758 | bm-20240504-linux-x86_64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml     | 54.3 ms                                                                | 52.2 ms: 1.04x faster                                                      |
| genshi_text    | 23.6 ms                                                                | 22.8 ms: 1.03x faster                                                      |
| mako           | 10.9 ms                                                                | 10.7 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                                  | 1.02x faster                                                               |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                | bm-20240504-linux-x86_64-python-5f547585fa56c94c5d83-3.13.0a6+-5f54758 | bm-20240504-linux-x86_64-gvanrossum-backoff_counter_woes-3.13.0a6+-4c1049b |
|--------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| scimark_sparse_mat_mult  | 5.50 ms                                                                | 5.29 ms: 1.04x faster                                                      |
| genshi_xml               | 54.3 ms                                                                | 52.2 ms: 1.04x faster                                                      |
| pycparser                | 1.21 sec                                                               | 1.17 sec: 1.04x faster                                                     |
| genshi_text              | 23.6 ms                                                                | 22.8 ms: 1.03x faster                                                      |
| scimark_sor              | 132 ms                                                                 | 128 ms: 1.03x faster                                                       |
| go                       | 148 ms                                                                 | 144 ms: 1.03x faster                                                       |
| logging_silent           | 105 ns                                                                 | 103 ns: 1.03x faster                                                       |
| typing_runtime_protocols | 172 us                                                                 | 168 us: 1.03x faster                                                       |
| logging_simple           | 5.97 us                                                                | 5.82 us: 1.03x faster                                                      |
| regex_v8                 | 26.6 ms                                                                | 26.0 ms: 1.02x faster                                                      |
| logging_format           | 6.61 us                                                                | 6.46 us: 1.02x faster                                                      |
| pickle_list              | 5.12 us                                                                | 5.00 us: 1.02x faster                                                      |
| scimark_monte_carlo      | 71.3 ms                                                                | 69.6 ms: 1.02x faster                                                      |
| pprint_pformat           | 1.58 sec                                                               | 1.55 sec: 1.02x faster                                                     |
| pprint_safe_repr         | 771 ms                                                                 | 755 ms: 1.02x faster                                                       |
| spectral_norm            | 112 ms                                                                 | 110 ms: 1.02x faster                                                       |
| meteor_contest           | 110 ms                                                                 | 108 ms: 1.02x faster                                                       |
| mako                     | 10.9 ms                                                                | 10.7 ms: 1.02x faster                                                      |
| comprehensions           | 17.1 us                                                                | 16.8 us: 1.02x faster                                                      |
| scimark_fft              | 379 ms                                                                 | 372 ms: 1.02x faster                                                       |
| fannkuch                 | 407 ms                                                                 | 401 ms: 1.02x faster                                                       |
| deepcopy                 | 367 us                                                                 | 363 us: 1.01x faster                                                       |
| sympy_expand             | 484 ms                                                                 | 477 ms: 1.01x faster                                                       |
| hexiom                   | 6.25 ms                                                                | 6.18 ms: 1.01x faster                                                      |
| json_dumps               | 10.6 ms                                                                | 10.5 ms: 1.01x faster                                                      |
| richards_super           | 56.9 ms                                                                | 56.4 ms: 1.01x faster                                                      |
| richards                 | 50.8 ms                                                                | 50.4 ms: 1.01x faster                                                      |
| tornado_http             | 95.5 ms                                                                | 94.7 ms: 1.01x faster                                                      |
| sympy_sum                | 157 ms                                                                 | 156 ms: 1.01x faster                                                       |
| pathlib                  | 17.6 ms                                                                | 17.5 ms: 1.01x faster                                                      |
| float                    | 79.0 ms                                                                | 78.5 ms: 1.01x faster                                                      |
| async_generators         | 447 ms                                                                 | 444 ms: 1.01x faster                                                       |
| asyncio_tcp              | 509 ms                                                                 | 506 ms: 1.01x faster                                                       |
| sqlglot_transpile        | 1.65 ms                                                                | 1.64 ms: 1.01x faster                                                      |
| xml_etree_generate       | 88.6 ms                                                                | 88.1 ms: 1.01x faster                                                      |
| bench_thread_pool        | 837 us                                                                 | 833 us: 1.01x faster                                                       |
| sqlite_synth             | 2.91 us                                                                | 2.90 us: 1.00x faster                                                      |
| sqlglot_optimize         | 55.7 ms                                                                | 55.5 ms: 1.00x faster                                                      |
| raytrace                 | 266 ms                                                                 | 265 ms: 1.00x faster                                                       |
| sqlglot_normalize        | 113 ms                                                                 | 112 ms: 1.00x faster                                                       |
| 2to3                     | 272 ms                                                                 | 272 ms: 1.00x faster                                                       |
| asyncio_tcp_ssl          | 1.85 sec                                                               | 1.84 sec: 1.00x faster                                                     |
| python_startup_no_site   | 7.20 ms                                                                | 7.21 ms: 1.00x slower                                                      |
| python_startup           | 10.7 ms                                                                | 10.7 ms: 1.00x slower                                                      |
| regex_effbot             | 3.78 ms                                                                | 3.79 ms: 1.00x slower                                                      |
| pickle_pure_python       | 312 us                                                                 | 314 us: 1.00x slower                                                       |
| thrift                   | 813 us                                                                 | 818 us: 1.01x slower                                                       |
| html5lib                 | 68.4 ms                                                                | 68.8 ms: 1.01x slower                                                      |
| chaos                    | 58.5 ms                                                                | 58.9 ms: 1.01x slower                                                      |
| create_gc_cycles         | 1.82 ms                                                                | 1.84 ms: 1.01x slower                                                      |
| unpickle_pure_python     | 223 us                                                                 | 225 us: 1.01x slower                                                       |
| unpickle_list            | 5.37 us                                                                | 5.44 us: 1.01x slower                                                      |
| nqueens                  | 82.4 ms                                                                | 83.4 ms: 1.01x slower                                                      |
| pickle                   | 11.8 us                                                                | 12.0 us: 1.01x slower                                                      |
| scimark_lu               | 118 ms                                                                 | 120 ms: 1.02x slower                                                       |
| mdp                      | 2.58 sec                                                               | 2.65 sec: 1.03x slower                                                     |
| nbody                    | 87.5 ms                                                                | 90.4 ms: 1.03x slower                                                      |
| regex_dna                | 224 ms                                                                 | 232 ms: 1.04x slower                                                       |
| gc_traversal             | 3.84 ms                                                                | 3.99 ms: 1.04x slower                                                      |
| pickle_dict              | 35.0 us                                                                | 36.4 us: 1.04x slower                                                      |
| Geometric mean           | (ref)                                                                  | 1.00x faster                                                               |

Benchmark hidden because not significant (42): async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, coverage, flaskblogging, xml_etree_parse, generators, bench_mp_pool, json_loads, async_tree_memoization_tg, deepcopy_memo, pyflate, aiohttp, json, sqlglot_parse, sympy_integrate, dulwich_log, chameleon, telco, coroutines, async_tree_none_tg, django_template, sympy_str, docutils, async_tree_io_tg, pidigits, asyncio_websockets, xml_etree_iterparse, mypy2, tomli_loads, pylint, xml_etree_process, async_tree_none, deltablue, deepcopy_reduce, gunicorn, dask, regex_compile, crypto_pyaes, async_tree_io, async_tree_memoization, djangocms, unpickle

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x