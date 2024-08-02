# Results vs. base

- fork: brandtbucher
- ref: exits
- machine: linux-x86_64
- commit hash: 345fc71
- commit date: 2024-05-04
- overall geometric mean: 1.00x slower
- HPT reliability: 52.09%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240504-linux-x86_64-python-f34e965e52b9bdf157b8-3.13.0a6+-f34e965 | bm-20240504-linux-x86_64-brandtbucher-exits-3.13.0a6+-345fc71 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| chameleon      | 7.32 ms                                                                | 7.16 ms: 1.02x faster                                         |
| html5lib       | 69.0 ms                                                                | 69.7 ms: 1.01x slower                                         |
| tornado_http   | 98.2 ms                                                                | 97.4 ms: 1.01x faster                                         |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                  |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20240504-linux-x86_64-python-f34e965e52b9bdf157b8-3.13.0a6+-f34e965 | bm-20240504-linux-x86_64-brandtbucher-exits-3.13.0a6+-345fc71 |
|------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| async_tree_io_tg | 1.02 sec                                                               | 931 ms: 1.09x faster                                          |
| Geometric mean   | (ref)                                                                  | 1.01x faster                                                  |

Benchmark hidden because not significant (7): async_tree_cpu_io_mixed, async_tree_none, async_tree_memoization, async_tree_io, async_tree_memoization_tg, async_tree_none_tg, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240504-linux-x86_64-python-f34e965e52b9bdf157b8-3.13.0a6+-f34e965 | bm-20240504-linux-x86_64-brandtbucher-exits-3.13.0a6+-345fc71 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| nbody          | 82.6 ms                                                                | 81.4 ms: 1.01x faster                                         |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                  |

Benchmark hidden because not significant (2): pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240504-linux-x86_64-python-f34e965e52b9bdf157b8-3.13.0a6+-f34e965 | bm-20240504-linux-x86_64-brandtbucher-exits-3.13.0a6+-345fc71 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_v8       | 25.3 ms                                                                | 25.4 ms: 1.01x slower                                         |
| regex_dna      | 224 ms                                                                 | 226 ms: 1.01x slower                                          |
| regex_effbot   | 3.59 ms                                                                | 3.77 ms: 1.05x slower                                         |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                  |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20240504-linux-x86_64-python-f34e965e52b9bdf157b8-3.13.0a6+-f34e965 | bm-20240504-linux-x86_64-brandtbucher-exits-3.13.0a6+-345fc71 |
|--------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| pickle_dict        | 35.2 us                                                                | 33.9 us: 1.04x faster                                         |
| unpickle_list      | 5.32 us                                                                | 5.15 us: 1.03x faster                                         |
| xml_etree_process  | 59.6 ms                                                                | 58.7 ms: 1.01x faster                                         |
| tomli_loads        | 1.96 sec                                                               | 1.95 sec: 1.01x faster                                        |
| xml_etree_parse    | 149 ms                                                                 | 151 ms: 1.01x slower                                          |
| pickle_pure_python | 301 us                                                                 | 305 us: 1.01x slower                                          |
| pickle_list        | 5.01 us                                                                | 5.09 us: 1.02x slower                                         |
| unpickle           | 15.6 us                                                                | 16.2 us: 1.04x slower                                         |
| Geometric mean     | (ref)                                                                  | 1.00x faster                                                  |

Benchmark hidden because not significant (6): unpickle_pure_python, json_loads, json_dumps, xml_etree_generate, xml_etree_iterparse, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240504-linux-x86_64-python-f34e965e52b9bdf157b8-3.13.0a6+-f34e965 | bm-20240504-linux-x86_64-brandtbucher-exits-3.13.0a6+-345fc71 |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup         | 11.1 ms                                                                | 11.2 ms: 1.01x slower                                         |
| python_startup_no_site | 7.62 ms                                                                | 7.69 ms: 1.01x slower                                         |
| Geometric mean         | (ref)                                                                  | 1.01x slower                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240504-linux-x86_64-python-f34e965e52b9bdf157b8-3.13.0a6+-f34e965 | bm-20240504-linux-x86_64-brandtbucher-exits-3.13.0a6+-345fc71 |
|-----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| mako            | 9.65 ms                                                                | 9.45 ms: 1.02x faster                                         |
| django_template | 37.4 ms                                                                | 36.7 ms: 1.02x faster                                         |
| genshi_text     | 24.3 ms                                                                | 24.1 ms: 1.01x faster                                         |
| Geometric mean  | (ref)                                                                  | 1.01x faster                                                  |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                | bm-20240504-linux-x86_64-python-f34e965e52b9bdf157b8-3.13.0a6+-f34e965 | bm-20240504-linux-x86_64-brandtbucher-exits-3.13.0a6+-345fc71 |
|--------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| async_tree_io_tg         | 1.02 sec                                                               | 931 ms: 1.09x faster                                          |
| gc_traversal             | 3.86 ms                                                                | 3.65 ms: 1.06x faster                                         |
| pickle_dict              | 35.2 us                                                                | 33.9 us: 1.04x faster                                         |
| unpickle_list            | 5.32 us                                                                | 5.15 us: 1.03x faster                                         |
| chaos                    | 59.0 ms                                                                | 57.4 ms: 1.03x faster                                         |
| raytrace                 | 279 ms                                                                 | 272 ms: 1.02x faster                                          |
| logging_silent           | 107 ns                                                                 | 105 ns: 1.02x faster                                          |
| go                       | 150 ms                                                                 | 147 ms: 1.02x faster                                          |
| chameleon                | 7.32 ms                                                                | 7.16 ms: 1.02x faster                                         |
| mako                     | 9.65 ms                                                                | 9.45 ms: 1.02x faster                                         |
| pyflate                  | 454 ms                                                                 | 445 ms: 1.02x faster                                          |
| django_template          | 37.4 ms                                                                | 36.7 ms: 1.02x faster                                         |
| nqueens                  | 88.0 ms                                                                | 86.3 ms: 1.02x faster                                         |
| typing_runtime_protocols | 181 us                                                                 | 178 us: 1.02x faster                                          |
| xml_etree_process        | 59.6 ms                                                                | 58.7 ms: 1.01x faster                                         |
| nbody                    | 82.6 ms                                                                | 81.4 ms: 1.01x faster                                         |
| fannkuch                 | 362 ms                                                                 | 357 ms: 1.01x faster                                          |
| genshi_text              | 24.3 ms                                                                | 24.1 ms: 1.01x faster                                         |
| scimark_lu               | 125 ms                                                                 | 124 ms: 1.01x faster                                          |
| tornado_http             | 98.2 ms                                                                | 97.4 ms: 1.01x faster                                         |
| telco                    | 8.25 ms                                                                | 8.18 ms: 1.01x faster                                         |
| tomli_loads              | 1.96 sec                                                               | 1.95 sec: 1.01x faster                                        |
| hexiom                   | 6.61 ms                                                                | 6.57 ms: 1.01x faster                                         |
| sympy_expand             | 508 ms                                                                 | 506 ms: 1.00x faster                                          |
| meteor_contest           | 108 ms                                                                 | 108 ms: 1.00x faster                                          |
| asyncio_tcp_ssl          | 1.86 sec                                                               | 1.86 sec: 1.00x slower                                        |
| sqlglot_transpile        | 1.64 ms                                                                | 1.64 ms: 1.00x slower                                         |
| spectral_norm            | 97.0 ms                                                                | 97.4 ms: 1.00x slower                                         |
| regex_v8                 | 25.3 ms                                                                | 25.4 ms: 1.01x slower                                         |
| async_generators         | 467 ms                                                                 | 470 ms: 1.01x slower                                          |
| regex_dna                | 224 ms                                                                 | 226 ms: 1.01x slower                                          |
| python_startup           | 11.1 ms                                                                | 11.2 ms: 1.01x slower                                         |
| comprehensions           | 16.7 us                                                                | 16.8 us: 1.01x slower                                         |
| python_startup_no_site   | 7.62 ms                                                                | 7.69 ms: 1.01x slower                                         |
| aiohttp                  | 1.25 ms                                                                | 1.26 ms: 1.01x slower                                         |
| html5lib                 | 69.0 ms                                                                | 69.7 ms: 1.01x slower                                         |
| gunicorn                 | 1.34 ms                                                                | 1.36 ms: 1.01x slower                                         |
| xml_etree_parse          | 149 ms                                                                 | 151 ms: 1.01x slower                                          |
| pickle_pure_python       | 301 us                                                                 | 305 us: 1.01x slower                                          |
| bench_thread_pool        | 869 us                                                                 | 880 us: 1.01x slower                                          |
| dulwich_log              | 69.3 ms                                                                | 70.2 ms: 1.01x slower                                         |
| scimark_fft              | 314 ms                                                                 | 318 ms: 1.01x slower                                          |
| pickle_list              | 5.01 us                                                                | 5.09 us: 1.02x slower                                         |
| pprint_pformat           | 1.46 sec                                                               | 1.48 sec: 1.02x slower                                        |
| coroutines               | 23.4 ms                                                                | 23.8 ms: 1.02x slower                                         |
| deepcopy_reduce          | 3.31 us                                                                | 3.37 us: 1.02x slower                                         |
| pprint_safe_repr         | 708 ms                                                                 | 721 ms: 1.02x slower                                          |
| thrift                   | 800 us                                                                 | 816 us: 1.02x slower                                          |
| crypto_pyaes             | 68.8 ms                                                                | 70.3 ms: 1.02x slower                                         |
| pycparser                | 1.18 sec                                                               | 1.22 sec: 1.04x slower                                        |
| scimark_sparse_mat_mult  | 4.51 ms                                                                | 4.69 ms: 1.04x slower                                         |
| unpickle                 | 15.6 us                                                                | 16.2 us: 1.04x slower                                         |
| logging_format           | 6.40 us                                                                | 6.70 us: 1.05x slower                                         |
| logging_simple           | 5.78 us                                                                | 6.06 us: 1.05x slower                                         |
| regex_effbot             | 3.59 ms                                                                | 3.77 ms: 1.05x slower                                         |
| mdp                      | 2.60 sec                                                               | 2.82 sec: 1.08x slower                                        |
| Geometric mean           | (ref)                                                                  | 1.00x slower                                                  |

Benchmark hidden because not significant (45): unpickle_pure_python, async_tree_cpu_io_mixed, deltablue, deepcopy, richards, json_loads, json_dumps, regex_compile, json, deepcopy_memo, xml_etree_generate, async_tree_none, pylint, djangocms, 2to3, asyncio_tcp, pidigits, asyncio_websockets, sympy_sum, xml_etree_iterparse, sqlglot_parse, sqlglot_optimize, async_tree_memoization, mypy2, sympy_str, sympy_integrate, scimark_monte_carlo, float, sqlite_synth, pathlib, sqlglot_normalize, richards_super, dask, generators, scimark_sor, create_gc_cycles, async_tree_io, coverage, bench_mp_pool, genshi_xml, async_tree_memoization_tg, flaskblogging, async_tree_none_tg, pickle, async_tree_cpu_io_mixed_tg

# HPT report

- Reliability score: 52.09% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x