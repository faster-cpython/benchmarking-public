
# Results vs. 3.10.4

- fork: python
- ref: aad5f6a89125ad4529ab
- machine: darwin-arm64
- commit hash: aad5f6a
- commit date: 2023-02-07
- overall geometric mean: 1.01x slower \*
- HPT reliability: 55.02%
- HPT 99th percentile: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-darwin-arm64-python-aad5f6a89125ad4529ab-3.10.10-aad5f6a |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 202 ms                                                 | 203 ms: 1.00x slower                                                 |
| chameleon      | 5.84 ms                                                | 5.78 ms: 1.01x faster                                                |
| docutils       | 1.78 sec                                               | 1.79 sec: 1.00x slower                                               |
| html5lib       | 44.1 ms                                                | 47.8 ms: 1.08x slower                                                |
| Geometric mean | (ref)                                                  | 1.02x slower                                                         |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-darwin-arm64-python-aad5f6a89125ad4529ab-3.10.10-aad5f6a |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| pidigits       | 282 ms                                                 | 282 ms: 1.00x faster                                                 |
| Geometric mean | (ref)                                                  | 1.00x faster                                                         |

Benchmark hidden because not significant (2): nbody, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-darwin-arm64-python-aad5f6a89125ad4529ab-3.10.10-aad5f6a |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 96.6 ms                                                | 96.9 ms: 1.00x slower                                                |
| regex_v8       | 17.5 ms                                                | 18.2 ms: 1.04x slower                                                |
| regex_effbot   | 2.45 ms                                                | 2.75 ms: 1.13x slower                                                |
| regex_dna      | 160 ms                                                 | 187 ms: 1.17x slower                                                 |
| Geometric mean | (ref)                                                  | 1.08x slower                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-darwin-arm64-python-aad5f6a89125ad4529ab-3.10.10-aad5f6a |
|---------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| json_dumps          | 8.38 ms                                                | 8.29 ms: 1.01x faster                                                |
| xml_etree_iterparse | 72.6 ms                                                | 73.1 ms: 1.01x slower                                                |
| unpickle_list       | 2.66 us                                                | 2.68 us: 1.01x slower                                                |
| unpickle            | 9.77 us                                                | 9.86 us: 1.01x slower                                                |
| pickle_pure_python  | 284 us                                                 | 287 us: 1.01x slower                                                 |
| xml_etree_generate  | 54.3 ms                                                | 55.0 ms: 1.01x slower                                                |
| pickle              | 7.36 us                                                | 7.54 us: 1.02x slower                                                |
| pickle_list         | 2.83 us                                                | 2.93 us: 1.03x slower                                                |
| pickle_dict         | 17.8 us                                                | 18.7 us: 1.05x slower                                                |
| Geometric mean      | (ref)                                                  | 1.01x slower                                                         |

Benchmark hidden because not significant (4): xml_etree_parse, xml_etree_process, json_loads, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-darwin-arm64-python-aad5f6a89125ad4529ab-3.10.10-aad5f6a |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 12.6 ms                                                | 12.7 ms: 1.01x slower                                                |
| python_startup_no_site | 9.73 ms                                                | 9.82 ms: 1.01x slower                                                |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-darwin-arm64-python-aad5f6a89125ad4529ab-3.10.10-aad5f6a |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| genshi_text     | 18.4 ms                                                | 18.2 ms: 1.01x faster                                                |
| genshi_xml      | 37.6 ms                                                | 37.3 ms: 1.01x faster                                                |
| django_template | 27.3 ms                                                | 27.2 ms: 1.01x faster                                                |
| mako            | 10.5 ms                                                | 10.5 ms: 1.01x slower                                                |
| Geometric mean  | (ref)                                                  | 1.00x faster                                                         |

All benchmarks:
===============

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-darwin-arm64-python-aad5f6a89125ad4529ab-3.10.10-aad5f6a |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| bench_thread_pool      | 548 us                                                 | 534 us: 1.03x faster                                                 |
| aiohttp                | 1.29 ms                                                | 1.26 ms: 1.03x faster                                                |
| richards               | 51.4 ms                                                | 50.2 ms: 1.02x faster                                                |
| pprint_safe_repr       | 609 ms                                                 | 600 ms: 1.01x faster                                                 |
| deepcopy_reduce        | 2.38 us                                                | 2.35 us: 1.01x faster                                                |
| meteor_contest         | 78.6 ms                                                | 77.6 ms: 1.01x faster                                                |
| genshi_text            | 18.4 ms                                                | 18.2 ms: 1.01x faster                                                |
| chameleon              | 5.84 ms                                                | 5.78 ms: 1.01x faster                                                |
| json_dumps             | 8.38 ms                                                | 8.29 ms: 1.01x faster                                                |
| unpack_sequence        | 38.7 ns                                                | 38.3 ns: 1.01x faster                                                |
| logging_silent         | 119 ns                                                 | 118 ns: 1.01x faster                                                 |
| pprint_pformat         | 1.24 sec                                               | 1.23 sec: 1.01x faster                                               |
| generators             | 32.9 ms                                                | 32.7 ms: 1.01x faster                                                |
| genshi_xml             | 37.6 ms                                                | 37.3 ms: 1.01x faster                                                |
| telco                  | 3.68 ms                                                | 3.65 ms: 1.01x faster                                                |
| django_template        | 27.3 ms                                                | 27.2 ms: 1.01x faster                                                |
| sqlite_synth           | 1.47 us                                                | 1.47 us: 1.00x faster                                                |
| deepcopy_memo          | 34.5 us                                                | 34.4 us: 1.00x faster                                                |
| sqlglot_normalize      | 197 ms                                                 | 196 ms: 1.00x faster                                                 |
| fannkuch               | 317 ms                                                 | 317 ms: 1.00x faster                                                 |
| pidigits               | 282 ms                                                 | 282 ms: 1.00x faster                                                 |
| 2to3                   | 202 ms                                                 | 203 ms: 1.00x slower                                                 |
| create_gc_cycles       | 876 us                                                 | 878 us: 1.00x slower                                                 |
| regex_compile          | 96.6 ms                                                | 96.9 ms: 1.00x slower                                                |
| docutils               | 1.78 sec                                               | 1.79 sec: 1.00x slower                                               |
| comprehensions         | 17.7 us                                                | 17.7 us: 1.00x slower                                                |
| dulwich_log            | 37.1 ms                                                | 37.2 ms: 1.00x slower                                                |
| chaos                  | 66.8 ms                                                | 67.1 ms: 1.00x slower                                                |
| sympy_integrate        | 13.4 ms                                                | 13.4 ms: 1.01x slower                                                |
| mako                   | 10.5 ms                                                | 10.5 ms: 1.01x slower                                                |
| xml_etree_iterparse    | 72.6 ms                                                | 73.1 ms: 1.01x slower                                                |
| unpickle_list          | 2.66 us                                                | 2.68 us: 1.01x slower                                                |
| sqlalchemy_imperative  | 9.03 ms                                                | 9.10 ms: 1.01x slower                                                |
| raytrace               | 328 ms                                                 | 330 ms: 1.01x slower                                                 |
| python_startup         | 12.6 ms                                                | 12.7 ms: 1.01x slower                                                |
| sympy_expand           | 276 ms                                                 | 278 ms: 1.01x slower                                                 |
| python_startup_no_site | 9.73 ms                                                | 9.82 ms: 1.01x slower                                                |
| unpickle               | 9.77 us                                                | 9.86 us: 1.01x slower                                                |
| deepcopy               | 278 us                                                 | 280 us: 1.01x slower                                                 |
| sympy_str              | 169 ms                                                 | 171 ms: 1.01x slower                                                 |
| pickle_pure_python     | 284 us                                                 | 287 us: 1.01x slower                                                 |
| xml_etree_generate     | 54.3 ms                                                | 55.0 ms: 1.01x slower                                                |
| coverage               | 40.8 ms                                                | 41.8 ms: 1.02x slower                                                |
| pickle                 | 7.36 us                                                | 7.54 us: 1.02x slower                                                |
| sympy_sum              | 94.3 ms                                                | 96.8 ms: 1.03x slower                                                |
| dask                   | 258 ms                                                 | 265 ms: 1.03x slower                                                 |
| pickle_list            | 2.83 us                                                | 2.93 us: 1.03x slower                                                |
| regex_v8               | 17.5 ms                                                | 18.2 ms: 1.04x slower                                                |
| pickle_dict            | 17.8 us                                                | 18.7 us: 1.05x slower                                                |
| html5lib               | 44.1 ms                                                | 47.8 ms: 1.08x slower                                                |
| regex_effbot           | 2.45 ms                                                | 2.75 ms: 1.13x slower                                                |
| regex_dna              | 160 ms                                                 | 187 ms: 1.17x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                         |

Benchmark hidden because not significant (43): async_tree_memoization, async_tree_cpu_io_mixed, async_tree_none, pathlib, json, async_tree_io, pycparser, scimark_sor, mypy2, xml_etree_parse, gunicorn, logging_simple, pylint, bench_mp_pool, flaskblogging, nbody, coroutines, scimark_fft, xml_etree_process, sqlglot_parse, asyncio_tcp, spectral_norm, sqlalchemy_declarative, scimark_lu, float, go, json_loads, sqlglot_optimize, logging_format, nqueens, hexiom, crypto_pyaes, unpickle_pure_python, thrift, mdp, gc_traversal, sqlglot_transpile, scimark_sparse_mat_mult, pyflate, async_generators, deltablue, scimark_monte_carlo, tornado_http
Ignored benchmarks (4) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 55.02% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x
