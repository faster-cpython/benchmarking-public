# Results vs. 3.13.0b2

- fork: python
- ref: v3.13.0b4
- machine: darwin-arm64
- commit hash: 567c38b
- commit date: 2024-07-18
- overall geometric mean: 1.00x slower
- HPT reliability: 98.28%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240718-darwin-arm64-python-v3.13.0b4-3.13.0b4-567c38b |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 161 ms                                                     | 162 ms: 1.01x slower                                       |
| chameleon      | 4.27 ms                                                    | 4.31 ms: 1.01x slower                                      |
| docutils       | 1.44 sec                                                   | 1.45 sec: 1.01x slower                                     |
| html5lib       | 31.2 ms                                                    | 31.5 ms: 1.01x slower                                      |
| Geometric mean | (ref)                                                      | 1.01x slower                                               |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark           | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240718-darwin-arm64-python-v3.13.0b4-3.13.0b4-567c38b |
|---------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| async_tree_eager_tg | 41.4 ms                                                    | 41.6 ms: 1.00x slower                                      |
| async_tree_eager    | 60.3 ms                                                    | 61.1 ms: 1.01x slower                                      |
| Geometric mean      | (ref)                                                      | 1.00x slower                                               |

Benchmark hidden because not significant (14): async_tree_eager_memoization, async_tree_io, async_tree_io_tg, async_tree_eager_io_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_memoization, async_tree_eager_io, async_tree_cpu_io_mixed, async_tree_eager_cpu_io_mixed, async_tree_memoization_tg, async_tree_none, async_tree_cpu_io_mixed_tg, async_tree_none_tg, async_tree_eager_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240718-darwin-arm64-python-v3.13.0b4-3.13.0b4-567c38b |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| pidigits       | 282 ms                                                     | 281 ms: 1.00x faster                                       |
| nbody          | 59.6 ms                                                    | 59.8 ms: 1.00x slower                                      |
| Geometric mean | (ref)                                                      | 1.00x slower                                               |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240718-darwin-arm64-python-v3.13.0b4-3.13.0b4-567c38b |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| regex_effbot   | 2.58 ms                                                    | 2.57 ms: 1.01x faster                                      |
| regex_v8       | 17.3 ms                                                    | 17.2 ms: 1.00x faster                                      |
| Geometric mean | (ref)                                                      | 1.00x faster                                               |

Benchmark hidden because not significant (2): regex_compile, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240718-darwin-arm64-python-v3.13.0b4-3.13.0b4-567c38b |
|----------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| xml_etree_parse      | 106 ms                                                     | 105 ms: 1.01x faster                                       |
| json_dumps           | 6.23 ms                                                    | 6.25 ms: 1.00x slower                                      |
| xml_etree_generate   | 52.7 ms                                                    | 53.0 ms: 1.01x slower                                      |
| xml_etree_process    | 37.1 ms                                                    | 37.3 ms: 1.01x slower                                      |
| pickle_pure_python   | 179 us                                                     | 180 us: 1.01x slower                                       |
| tomli_loads          | 1.47 sec                                                   | 1.48 sec: 1.01x slower                                     |
| json_loads           | 16.8 us                                                    | 17.0 us: 1.01x slower                                      |
| unpickle_pure_python | 141 us                                                     | 142 us: 1.01x slower                                       |
| Geometric mean       | (ref)                                                      | 1.00x slower                                               |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240718-darwin-arm64-python-v3.13.0b4-3.13.0b4-567c38b |
|------------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup_no_site | 12.3 ms                                                    | 11.3 ms: 1.09x faster                                      |
| python_startup         | 15.2 ms                                                    | 14.1 ms: 1.08x faster                                      |
| Geometric mean         | (ref)                                                      | 1.08x faster                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240718-darwin-arm64-python-v3.13.0b4-3.13.0b4-567c38b |
|-----------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| genshi_text     | 13.9 ms                                                    | 13.8 ms: 1.01x faster                                      |
| genshi_xml      | 29.9 ms                                                    | 29.8 ms: 1.01x faster                                      |
| django_template | 19.4 ms                                                    | 19.5 ms: 1.01x slower                                      |
| Geometric mean  | (ref)                                                      | 1.00x faster                                               |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240718-darwin-arm64-python-v3.13.0b4-3.13.0b4-567c38b |
|--------------------------|:----------------------------------------------------------:|:----------------------------------------------------------:|
| mdp                      | 1.53 sec                                                   | 1.41 sec: 1.09x faster                                     |
| python_startup_no_site   | 12.3 ms                                                    | 11.3 ms: 1.09x faster                                      |
| python_startup           | 15.2 ms                                                    | 14.1 ms: 1.08x faster                                      |
| create_gc_cycles         | 897 us                                                     | 867 us: 1.03x faster                                       |
| richards_super           | 35.2 ms                                                    | 34.3 ms: 1.03x faster                                      |
| richards                 | 31.8 ms                                                    | 31.2 ms: 1.02x faster                                      |
| asyncio_tcp_ssl          | 1.29 sec                                                   | 1.27 sec: 1.01x faster                                     |
| pprint_safe_repr         | 465 ms                                                     | 459 ms: 1.01x faster                                       |
| pprint_pformat           | 947 ms                                                     | 936 ms: 1.01x faster                                       |
| genshi_text              | 13.9 ms                                                    | 13.8 ms: 1.01x faster                                      |
| xml_etree_parse          | 106 ms                                                     | 105 ms: 1.01x faster                                       |
| dulwich_log              | 27.6 ms                                                    | 27.4 ms: 1.01x faster                                      |
| genshi_xml               | 29.9 ms                                                    | 29.8 ms: 1.01x faster                                      |
| regex_effbot             | 2.58 ms                                                    | 2.57 ms: 1.01x faster                                      |
| thrift                   | 435 us                                                     | 433 us: 1.00x faster                                       |
| regex_v8                 | 17.3 ms                                                    | 17.2 ms: 1.00x faster                                      |
| sympy_expand             | 226 ms                                                     | 225 ms: 1.00x faster                                       |
| go                       | 101 ms                                                     | 100 ms: 1.00x faster                                       |
| sqlglot_parse            | 732 us                                                     | 730 us: 1.00x faster                                       |
| scimark_lu               | 66.9 ms                                                    | 66.7 ms: 1.00x faster                                      |
| pidigits                 | 282 ms                                                     | 281 ms: 1.00x faster                                       |
| asyncio_websockets       | 409 ms                                                     | 408 ms: 1.00x faster                                       |
| logging_silent           | 60.1 ns                                                    | 60.1 ns: 1.00x faster                                      |
| gc_traversal             | 2.45 ms                                                    | 2.45 ms: 1.00x slower                                      |
| scimark_sor              | 94.9 ms                                                    | 95.0 ms: 1.00x slower                                      |
| coroutines               | 15.8 ms                                                    | 15.9 ms: 1.00x slower                                      |
| hexiom                   | 4.06 ms                                                    | 4.07 ms: 1.00x slower                                      |
| meteor_contest           | 70.3 ms                                                    | 70.5 ms: 1.00x slower                                      |
| scimark_monte_carlo      | 42.5 ms                                                    | 42.6 ms: 1.00x slower                                      |
| deepcopy_memo            | 22.6 us                                                    | 22.7 us: 1.00x slower                                      |
| comprehensions           | 10.2 us                                                    | 10.2 us: 1.00x slower                                      |
| nbody                    | 59.6 ms                                                    | 59.8 ms: 1.00x slower                                      |
| json_dumps               | 6.23 ms                                                    | 6.25 ms: 1.00x slower                                      |
| generators               | 22.9 ms                                                    | 23.0 ms: 1.00x slower                                      |
| async_tree_eager_tg      | 41.4 ms                                                    | 41.6 ms: 1.00x slower                                      |
| async_generators         | 281 ms                                                     | 282 ms: 1.01x slower                                       |
| deltablue                | 2.14 ms                                                    | 2.15 ms: 1.01x slower                                      |
| django_template          | 19.4 ms                                                    | 19.5 ms: 1.01x slower                                      |
| xml_etree_generate       | 52.7 ms                                                    | 53.0 ms: 1.01x slower                                      |
| spectral_norm            | 66.4 ms                                                    | 66.8 ms: 1.01x slower                                      |
| telco                    | 4.60 ms                                                    | 4.63 ms: 1.01x slower                                      |
| docutils                 | 1.44 sec                                                   | 1.45 sec: 1.01x slower                                     |
| xml_etree_process        | 37.1 ms                                                    | 37.3 ms: 1.01x slower                                      |
| pickle_pure_python       | 179 us                                                     | 180 us: 1.01x slower                                       |
| tomli_loads              | 1.47 sec                                                   | 1.48 sec: 1.01x slower                                     |
| chameleon                | 4.27 ms                                                    | 4.31 ms: 1.01x slower                                      |
| raytrace                 | 147 ms                                                     | 148 ms: 1.01x slower                                       |
| json_loads               | 16.8 us                                                    | 17.0 us: 1.01x slower                                      |
| html5lib                 | 31.2 ms                                                    | 31.5 ms: 1.01x slower                                      |
| scimark_sparse_mat_mult  | 2.77 ms                                                    | 2.80 ms: 1.01x slower                                      |
| 2to3                     | 161 ms                                                     | 162 ms: 1.01x slower                                       |
| crypto_pyaes             | 49.5 ms                                                    | 50.0 ms: 1.01x slower                                      |
| unpickle_pure_python     | 141 us                                                     | 142 us: 1.01x slower                                       |
| typing_runtime_protocols | 87.6 us                                                    | 88.7 us: 1.01x slower                                      |
| async_tree_eager         | 60.3 ms                                                    | 61.1 ms: 1.01x slower                                      |
| nqueens                  | 52.2 ms                                                    | 52.9 ms: 1.01x slower                                      |
| pathlib                  | 23.3 ms                                                    | 23.7 ms: 1.01x slower                                      |
| chaos                    | 34.0 ms                                                    | 34.7 ms: 1.02x slower                                      |
| logging_simple           | 3.04 us                                                    | 3.11 us: 1.02x slower                                      |
| fannkuch                 | 248 ms                                                     | 254 ms: 1.02x slower                                       |
| logging_format           | 3.31 us                                                    | 3.40 us: 1.03x slower                                      |
| bench_thread_pool        | 447 us                                                     | 460 us: 1.03x slower                                       |
| asyncio_tcp              | 402 ms                                                     | 445 ms: 1.11x slower                                       |
| mypy2                    | 379 ms                                                     | 447 ms: 1.18x slower                                       |
| Geometric mean           | (ref)                                                      | 1.00x slower                                               |

Benchmark hidden because not significant (37): async_tree_eager_memoization, bench_mp_pool, async_tree_io, dask, async_tree_io_tg, pycparser, json, async_tree_eager_io_tg, xml_etree_iterparse, pylint, regex_compile, sympy_integrate, sqlglot_optimize, deepcopy_reduce, deepcopy, regex_dna, scimark_fft, pyflate, sqlglot_normalize, coverage, bpe_tokeniser, sqlglot_transpile, tornado_http, async_tree_eager_cpu_io_mixed_tg, async_tree_memoization, sympy_str, mako, async_tree_eager_io, async_tree_cpu_io_mixed, float, async_tree_eager_cpu_io_mixed, async_tree_memoization_tg, async_tree_none, sympy_sum, async_tree_cpu_io_mixed_tg, async_tree_none_tg, async_tree_eager_memoization_tg
Ignored benchmarks (9) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 98.28% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x