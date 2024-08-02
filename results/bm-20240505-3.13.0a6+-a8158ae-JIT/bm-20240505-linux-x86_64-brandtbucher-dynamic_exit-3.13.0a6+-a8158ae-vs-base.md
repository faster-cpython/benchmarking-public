# Results vs. base

- fork: brandtbucher
- ref: dynamic_exit
- machine: linux-x86_64
- commit hash: a8158ae
- commit date: 2024-05-05
- overall geometric mean: 1.01x slower
- HPT reliability: 99.83%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240505-linux-x86_64-python-d8d94911e2393bd30ca5-3.13.0a6+-d8d9491 | bm-20240505-linux-x86_64-brandtbucher-dynamic_exit-3.13.0a6+-a8158ae |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 279 ms                                                                 | 284 ms: 1.02x slower                                                 |
| chameleon      | 7.02 ms                                                                | 7.30 ms: 1.04x slower                                                |
| html5lib       | 70.1 ms                                                                | 70.5 ms: 1.00x slower                                                |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                         |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_cpu_io_mixed, async_tree_memoization, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_none, async_tree_none_tg, async_tree_io, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240505-linux-x86_64-python-d8d94911e2393bd30ca5-3.13.0a6+-d8d9491 | bm-20240505-linux-x86_64-brandtbucher-dynamic_exit-3.13.0a6+-a8158ae |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody          | 79.9 ms                                                                | 79.0 ms: 1.01x faster                                                |
| pidigits       | 189 ms                                                                 | 189 ms: 1.00x slower                                                 |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                         |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240505-linux-x86_64-python-d8d94911e2393bd30ca5-3.13.0a6+-d8d9491 | bm-20240505-linux-x86_64-brandtbucher-dynamic_exit-3.13.0a6+-a8158ae |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_dna      | 228 ms                                                                 | 226 ms: 1.01x faster                                                 |
| regex_effbot   | 3.71 ms                                                                | 3.74 ms: 1.01x slower                                                |
| regex_v8       | 24.5 ms                                                                | 24.8 ms: 1.01x slower                                                |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                         |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240505-linux-x86_64-python-d8d94911e2393bd30ca5-3.13.0a6+-d8d9491 | bm-20240505-linux-x86_64-brandtbucher-dynamic_exit-3.13.0a6+-a8158ae |
|---------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| pickle_list         | 5.49 us                                                                | 4.99 us: 1.10x faster                                                |
| pickle_dict         | 37.9 us                                                                | 35.5 us: 1.07x faster                                                |
| pickle              | 12.2 us                                                                | 11.8 us: 1.03x faster                                                |
| xml_etree_process   | 58.6 ms                                                                | 58.9 ms: 1.01x slower                                                |
| xml_etree_iterparse | 101 ms                                                                 | 101 ms: 1.01x slower                                                 |
| xml_etree_generate  | 83.4 ms                                                                | 84.2 ms: 1.01x slower                                                |
| json_loads          | 27.4 us                                                                | 27.9 us: 1.02x slower                                                |
| xml_etree_parse     | 150 ms                                                                 | 153 ms: 1.02x slower                                                 |
| Geometric mean      | (ref)                                                                  | 1.01x faster                                                         |

Benchmark hidden because not significant (6): unpickle, unpickle_pure_python, tomli_loads, json_dumps, pickle_pure_python, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240505-linux-x86_64-python-d8d94911e2393bd30ca5-3.13.0a6+-d8d9491 | bm-20240505-linux-x86_64-brandtbucher-dynamic_exit-3.13.0a6+-a8158ae |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 7.63 ms                                                                | 7.66 ms: 1.00x slower                                                |
| python_startup         | 11.1 ms                                                                | 11.2 ms: 1.00x slower                                                |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240505-linux-x86_64-python-d8d94911e2393bd30ca5-3.13.0a6+-d8d9491 | bm-20240505-linux-x86_64-brandtbucher-dynamic_exit-3.13.0a6+-a8158ae |
|-----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| django_template | 36.5 ms                                                                | 35.8 ms: 1.02x faster                                                |
| genshi_xml      | 59.3 ms                                                                | 58.2 ms: 1.02x faster                                                |
| mako            | 9.51 ms                                                                | 9.67 ms: 1.02x slower                                                |
| Geometric mean  | (ref)                                                                  | 1.01x faster                                                         |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                | bm-20240505-linux-x86_64-python-d8d94911e2393bd30ca5-3.13.0a6+-d8d9491 | bm-20240505-linux-x86_64-brandtbucher-dynamic_exit-3.13.0a6+-a8158ae |
|--------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| pickle_list              | 5.49 us                                                                | 4.99 us: 1.10x faster                                                |
| pickle_dict              | 37.9 us                                                                | 35.5 us: 1.07x faster                                                |
| pickle                   | 12.2 us                                                                | 11.8 us: 1.03x faster                                                |
| async_generators         | 476 ms                                                                 | 465 ms: 1.02x faster                                                 |
| spectral_norm            | 101 ms                                                                 | 99.0 ms: 1.02x faster                                                |
| deepcopy                 | 375 us                                                                 | 368 us: 1.02x faster                                                 |
| logging_simple           | 5.87 us                                                                | 5.75 us: 1.02x faster                                                |
| django_template          | 36.5 ms                                                                | 35.8 ms: 1.02x faster                                                |
| coroutines               | 24.1 ms                                                                | 23.7 ms: 1.02x faster                                                |
| genshi_xml               | 59.3 ms                                                                | 58.2 ms: 1.02x faster                                                |
| scimark_monte_carlo      | 65.3 ms                                                                | 64.2 ms: 1.02x faster                                                |
| crypto_pyaes             | 70.1 ms                                                                | 69.1 ms: 1.01x faster                                                |
| nbody                    | 79.9 ms                                                                | 79.0 ms: 1.01x faster                                                |
| logging_format           | 6.50 us                                                                | 6.43 us: 1.01x faster                                                |
| thrift                   | 819 us                                                                 | 810 us: 1.01x faster                                                 |
| regex_dna                | 228 ms                                                                 | 226 ms: 1.01x faster                                                 |
| coverage                 | 87.7 ms                                                                | 87.1 ms: 1.01x faster                                                |
| pathlib                  | 18.0 ms                                                                | 17.9 ms: 1.01x faster                                                |
| sqlglot_transpile        | 1.64 ms                                                                | 1.64 ms: 1.01x faster                                                |
| scimark_fft              | 314 ms                                                                 | 313 ms: 1.00x faster                                                 |
| mdp                      | 2.59 sec                                                               | 2.59 sec: 1.00x faster                                               |
| asyncio_tcp_ssl          | 1.86 sec                                                               | 1.86 sec: 1.00x slower                                               |
| pidigits                 | 189 ms                                                                 | 189 ms: 1.00x slower                                                 |
| bench_thread_pool        | 869 us                                                                 | 871 us: 1.00x slower                                                 |
| sqlglot_optimize         | 56.8 ms                                                                | 57.0 ms: 1.00x slower                                                |
| hexiom                   | 6.57 ms                                                                | 6.60 ms: 1.00x slower                                                |
| python_startup_no_site   | 7.63 ms                                                                | 7.66 ms: 1.00x slower                                                |
| html5lib                 | 70.1 ms                                                                | 70.5 ms: 1.00x slower                                                |
| python_startup           | 11.1 ms                                                                | 11.2 ms: 1.00x slower                                                |
| xml_etree_process        | 58.6 ms                                                                | 58.9 ms: 1.01x slower                                                |
| dulwich_log              | 70.0 ms                                                                | 70.4 ms: 1.01x slower                                                |
| xml_etree_iterparse      | 101 ms                                                                 | 101 ms: 1.01x slower                                                 |
| regex_effbot             | 3.71 ms                                                                | 3.74 ms: 1.01x slower                                                |
| sqlite_synth             | 2.84 us                                                                | 2.87 us: 1.01x slower                                                |
| create_gc_cycles         | 1.86 ms                                                                | 1.87 ms: 1.01x slower                                                |
| aiohttp                  | 1.25 ms                                                                | 1.26 ms: 1.01x slower                                                |
| xml_etree_generate       | 83.4 ms                                                                | 84.2 ms: 1.01x slower                                                |
| regex_v8                 | 24.5 ms                                                                | 24.8 ms: 1.01x slower                                                |
| go                       | 147 ms                                                                 | 148 ms: 1.01x slower                                                 |
| pyflate                  | 448 ms                                                                 | 452 ms: 1.01x slower                                                 |
| typing_runtime_protocols | 174 us                                                                 | 175 us: 1.01x slower                                                 |
| sympy_integrate          | 22.5 ms                                                                | 22.8 ms: 1.01x slower                                                |
| meteor_contest           | 108 ms                                                                 | 109 ms: 1.01x slower                                                 |
| deepcopy_memo            | 37.3 us                                                                | 37.8 us: 1.01x slower                                                |
| 2to3                     | 279 ms                                                                 | 284 ms: 1.02x slower                                                 |
| nqueens                  | 87.0 ms                                                                | 88.4 ms: 1.02x slower                                                |
| mako                     | 9.51 ms                                                                | 9.67 ms: 1.02x slower                                                |
| sqlglot_normalize        | 114 ms                                                                 | 116 ms: 1.02x slower                                                 |
| telco                    | 8.23 ms                                                                | 8.37 ms: 1.02x slower                                                |
| json_loads               | 27.4 us                                                                | 27.9 us: 1.02x slower                                                |
| xml_etree_parse          | 150 ms                                                                 | 153 ms: 1.02x slower                                                 |
| json                     | 5.08 ms                                                                | 5.20 ms: 1.02x slower                                                |
| scimark_sparse_mat_mult  | 4.52 ms                                                                | 4.63 ms: 1.02x slower                                                |
| raytrace                 | 275 ms                                                                 | 282 ms: 1.02x slower                                                 |
| pprint_safe_repr         | 712 ms                                                                 | 731 ms: 1.03x slower                                                 |
| pprint_pformat           | 1.46 sec                                                               | 1.51 sec: 1.03x slower                                               |
| scimark_sor              | 129 ms                                                                 | 133 ms: 1.04x slower                                                 |
| deltablue                | 3.72 ms                                                                | 3.86 ms: 1.04x slower                                                |
| chameleon                | 7.02 ms                                                                | 7.30 ms: 1.04x slower                                                |
| gc_traversal             | 3.87 ms                                                                | 4.12 ms: 1.06x slower                                                |
| generators               | 30.1 ms                                                                | 51.4 ms: 1.71x slower                                                |
| Geometric mean           | (ref)                                                                  | 1.01x slower                                                         |

Benchmark hidden because not significant (40): unpickle, unpickle_pure_python, richards_super, float, tomli_loads, scimark_lu, comprehensions, deepcopy_reduce, sympy_str, sympy_sum, asyncio_tcp, async_tree_cpu_io_mixed, sympy_expand, genshi_text, json_dumps, pycparser, regex_compile, asyncio_websockets, async_tree_memoization, pickle_pure_python, djangocms, bench_mp_pool, async_tree_memoization_tg, sqlglot_parse, fannkuch, chaos, tornado_http, logging_silent, unpickle_list, async_tree_cpu_io_mixed_tg, gunicorn, flaskblogging, mypy2, richards, async_tree_none, async_tree_none_tg, dask, async_tree_io, async_tree_io_tg, pylint

# HPT report

- Reliability score: 99.83% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x