# Results vs. 3.13.0b2

- fork: python
- ref: edb6883ef3f7a8ef0c83
- machine: darwin-arm64
- commit hash: edb6883
- commit date: 2024-06-01
- overall geometric mean: 1.01x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.52x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240601-darwin-arm64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 161 ms                                                     | 159 ms: 1.01x faster                                                   |
| chameleon      | 4.27 ms                                                    | 4.29 ms: 1.01x slower                                                  |
| docutils       | 1.44 sec                                                   | 1.43 sec: 1.01x faster                                                 |
| Geometric mean | (ref)                                                      | 1.01x faster                                                           |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240601-darwin-arm64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_eager | 60.3 ms                                                    | 60.8 ms: 1.01x slower                                                  |
| Geometric mean   | (ref)                                                      | 1.01x faster                                                           |

Benchmark hidden because not significant (15): async_tree_eager_io, async_tree_eager_io_tg, async_tree_io, async_tree_io_tg, async_tree_memoization, async_tree_none, async_tree_memoization_tg, async_tree_none_tg, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240601-darwin-arm64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 48.6 ms                                                    | 48.1 ms: 1.01x faster                                                  |
| nbody          | 59.6 ms                                                    | 59.8 ms: 1.00x slower                                                  |
| Geometric mean | (ref)                                                      | 1.00x faster                                                           |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240601-darwin-arm64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 68.5 ms                                                    | 68.0 ms: 1.01x faster                                                  |
| regex_v8       | 17.3 ms                                                    | 17.3 ms: 1.00x faster                                                  |
| regex_effbot   | 2.58 ms                                                    | 2.58 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                      | 1.00x faster                                                           |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240601-darwin-arm64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|--------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps         | 6.23 ms                                                    | 6.18 ms: 1.01x faster                                                  |
| xml_etree_process  | 37.1 ms                                                    | 36.9 ms: 1.00x faster                                                  |
| xml_etree_generate | 52.7 ms                                                    | 52.5 ms: 1.00x faster                                                  |
| pickle             | 7.48 us                                                    | 7.51 us: 1.00x slower                                                  |
| pickle_dict        | 18.3 us                                                    | 18.6 us: 1.02x slower                                                  |
| pickle_list        | 2.96 us                                                    | 3.02 us: 1.02x slower                                                  |
| Geometric mean     | (ref)                                                      | 1.00x slower                                                           |

Benchmark hidden because not significant (8): xml_etree_parse, tomli_loads, unpickle_list, json_loads, xml_etree_iterparse, unpickle_pure_python, unpickle, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240601-darwin-arm64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|------------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 12.3 ms                                                    | 10.3 ms: 1.20x faster                                                  |
| python_startup         | 15.2 ms                                                    | 13.3 ms: 1.14x faster                                                  |
| Geometric mean         | (ref)                                                      | 1.17x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240601-darwin-arm64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|-----------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 19.4 ms                                                    | 19.3 ms: 1.01x faster                                                  |
| genshi_xml      | 29.9 ms                                                    | 30.2 ms: 1.01x slower                                                  |
| genshi_text     | 13.9 ms                                                    | 14.0 ms: 1.01x slower                                                  |
| Geometric mean  | (ref)                                                      | 1.00x slower                                                           |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                | bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240601-darwin-arm64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|--------------------------|:----------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site   | 12.3 ms                                                    | 10.3 ms: 1.20x faster                                                  |
| flaskblogging            | 3.61 ms                                                    | 3.10 ms: 1.16x faster                                                  |
| python_startup           | 15.2 ms                                                    | 13.3 ms: 1.14x faster                                                  |
| pathlib                  | 23.3 ms                                                    | 22.1 ms: 1.06x faster                                                  |
| asyncio_tcp_ssl          | 1.29 sec                                                   | 1.23 sec: 1.05x faster                                                 |
| bench_mp_pool            | 47.2 ms                                                    | 45.3 ms: 1.04x faster                                                  |
| mdp                      | 1.53 sec                                                   | 1.48 sec: 1.04x faster                                                 |
| dask                     | 221 ms                                                     | 218 ms: 1.02x faster                                                   |
| pprint_pformat           | 947 ms                                                     | 934 ms: 1.01x faster                                                   |
| scimark_lu               | 66.9 ms                                                    | 66.0 ms: 1.01x faster                                                  |
| thrift                   | 435 us                                                     | 430 us: 1.01x faster                                                   |
| pprint_safe_repr         | 465 ms                                                     | 459 ms: 1.01x faster                                                   |
| 2to3                     | 161 ms                                                     | 159 ms: 1.01x faster                                                   |
| deepcopy_reduce          | 1.82 us                                                    | 1.80 us: 1.01x faster                                                  |
| float                    | 48.6 ms                                                    | 48.1 ms: 1.01x faster                                                  |
| sqlite_synth             | 1.55 us                                                    | 1.54 us: 1.01x faster                                                  |
| pyflate                  | 321 ms                                                     | 318 ms: 1.01x faster                                                   |
| generators               | 22.9 ms                                                    | 22.7 ms: 1.01x faster                                                  |
| json_dumps               | 6.23 ms                                                    | 6.18 ms: 1.01x faster                                                  |
| regex_compile            | 68.5 ms                                                    | 68.0 ms: 1.01x faster                                                  |
| django_template          | 19.4 ms                                                    | 19.3 ms: 1.01x faster                                                  |
| dulwich_log              | 27.6 ms                                                    | 27.4 ms: 1.01x faster                                                  |
| docutils                 | 1.44 sec                                                   | 1.43 sec: 1.01x faster                                                 |
| fannkuch                 | 248 ms                                                     | 247 ms: 1.01x faster                                                   |
| crypto_pyaes             | 49.5 ms                                                    | 49.2 ms: 1.00x faster                                                  |
| scimark_sparse_mat_mult  | 2.77 ms                                                    | 2.76 ms: 1.00x faster                                                  |
| telco                    | 4.60 ms                                                    | 4.58 ms: 1.00x faster                                                  |
| xml_etree_process        | 37.1 ms                                                    | 36.9 ms: 1.00x faster                                                  |
| sqlglot_normalize        | 166 ms                                                     | 165 ms: 1.00x faster                                                   |
| xml_etree_generate       | 52.7 ms                                                    | 52.5 ms: 1.00x faster                                                  |
| go                       | 101 ms                                                     | 100 ms: 1.00x faster                                                   |
| sympy_integrate          | 10.3 ms                                                    | 10.3 ms: 1.00x faster                                                  |
| richards                 | 31.8 ms                                                    | 31.7 ms: 1.00x faster                                                  |
| scimark_fft              | 181 ms                                                     | 180 ms: 1.00x faster                                                   |
| sympy_expand             | 226 ms                                                     | 225 ms: 1.00x faster                                                   |
| scimark_monte_carlo      | 42.5 ms                                                    | 42.4 ms: 1.00x faster                                                  |
| deltablue                | 2.14 ms                                                    | 2.14 ms: 1.00x faster                                                  |
| regex_v8                 | 17.3 ms                                                    | 17.3 ms: 1.00x faster                                                  |
| raytrace                 | 147 ms                                                     | 147 ms: 1.00x faster                                                   |
| regex_effbot             | 2.58 ms                                                    | 2.58 ms: 1.00x faster                                                  |
| meteor_contest           | 70.3 ms                                                    | 70.2 ms: 1.00x faster                                                  |
| gc_traversal             | 2.45 ms                                                    | 2.45 ms: 1.00x slower                                                  |
| deepcopy_memo            | 22.6 us                                                    | 22.6 us: 1.00x slower                                                  |
| nbody                    | 59.6 ms                                                    | 59.8 ms: 1.00x slower                                                  |
| logging_silent           | 60.1 ns                                                    | 60.3 ns: 1.00x slower                                                  |
| logging_format           | 3.31 us                                                    | 3.32 us: 1.00x slower                                                  |
| hexiom                   | 4.06 ms                                                    | 4.07 ms: 1.00x slower                                                  |
| comprehensions           | 10.2 us                                                    | 10.2 us: 1.00x slower                                                  |
| chaos                    | 34.0 ms                                                    | 34.1 ms: 1.00x slower                                                  |
| create_gc_cycles         | 897 us                                                     | 900 us: 1.00x slower                                                   |
| pickle                   | 7.48 us                                                    | 7.51 us: 1.00x slower                                                  |
| chameleon                | 4.27 ms                                                    | 4.29 ms: 1.01x slower                                                  |
| nqueens                  | 52.2 ms                                                    | 52.6 ms: 1.01x slower                                                  |
| typing_runtime_protocols | 87.6 us                                                    | 88.2 us: 1.01x slower                                                  |
| genshi_xml               | 29.9 ms                                                    | 30.2 ms: 1.01x slower                                                  |
| async_tree_eager         | 60.3 ms                                                    | 60.8 ms: 1.01x slower                                                  |
| genshi_text              | 13.9 ms                                                    | 14.0 ms: 1.01x slower                                                  |
| pickle_dict              | 18.3 us                                                    | 18.6 us: 1.02x slower                                                  |
| pickle_list              | 2.96 us                                                    | 3.02 us: 1.02x slower                                                  |
| bench_thread_pool        | 447 us                                                     | 457 us: 1.02x slower                                                   |
| gunicorn                 | 1.04 ms                                                    | 1.06 ms: 1.03x slower                                                  |
| Geometric mean           | (ref)                                                      | 1.01x faster                                                           |

Benchmark hidden because not significant (48): asyncio_tcp, async_tree_eager_io, async_tree_eager_io_tg, async_tree_io, async_tree_io_tg, async_tree_memoization, tornado_http, async_tree_none, async_tree_memoization_tg, async_tree_none_tg, pylint, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, mypy2, async_tree_eager_memoization, async_tree_eager_memoization_tg, xml_etree_parse, tomli_loads, sympy_sum, mako, async_tree_eager_cpu_io_mixed, coverage, pycparser, logging_simple, unpickle_list, async_tree_eager_cpu_io_mixed_tg, sqlglot_parse, sympy_str, async_tree_eager_tg, richards_super, spectral_norm, html5lib, regex_dna, json, sqlglot_transpile, asyncio_websockets, pidigits, deepcopy, json_loads, scimark_sor, xml_etree_iterparse, unpickle_pure_python, coroutines, unpickle, pickle_pure_python, async_generators, sqlglot_optimize, aiohttp
Ignored benchmarks (1) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-darwin-arm64-python-v3.13.0b2-3.13.0b2-3a83b17.json: bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.52x