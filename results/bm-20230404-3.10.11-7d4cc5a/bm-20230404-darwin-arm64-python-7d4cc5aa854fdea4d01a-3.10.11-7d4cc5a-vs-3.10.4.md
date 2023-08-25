
# Results vs. 3.10.4

- fork: python
- ref: 7d4cc5aa854fdea4d01a
- machine: darwin-arm64
- commit hash: 7d4cc5a
- commit date: 2023-04-04
- overall geometric mean: 1.00x slower \*
- HPT reliability: 87.12%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230404-darwin-arm64-python-7d4cc5aa854fdea4d01a-3.10.11-7d4cc5a |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 202 ms                                                 | 203 ms: 1.00x slower                                                 |
| chameleon      | 5.84 ms                                                | 5.75 ms: 1.02x faster                                                |
| docutils       | 1.78 sec                                               | 1.79 sec: 1.00x slower                                               |
| html5lib       | 44.1 ms                                                | 47.8 ms: 1.08x slower                                                |
| Geometric mean | (ref)                                                  | 1.01x slower                                                         |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): float, nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230404-darwin-arm64-python-7d4cc5aa854fdea4d01a-3.10.11-7d4cc5a |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 96.6 ms                                                | 96.9 ms: 1.00x slower                                                |
| regex_v8       | 17.5 ms                                                | 18.0 ms: 1.03x slower                                                |
| regex_effbot   | 2.45 ms                                                | 2.69 ms: 1.10x slower                                                |
| regex_dna      | 160 ms                                                 | 185 ms: 1.16x slower                                                 |
| Geometric mean | (ref)                                                  | 1.07x slower                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230404-darwin-arm64-python-7d4cc5aa854fdea4d01a-3.10.11-7d4cc5a |
|---------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| json_dumps          | 8.38 ms                                                | 8.27 ms: 1.01x faster                                                |
| xml_etree_process   | 45.1 ms                                                | 44.9 ms: 1.00x faster                                                |
| pickle_pure_python  | 284 us                                                 | 285 us: 1.01x slower                                                 |
| xml_etree_iterparse | 72.6 ms                                                | 73.2 ms: 1.01x slower                                                |
| unpickle_list       | 2.66 us                                                | 2.69 us: 1.01x slower                                                |
| unpickle            | 9.77 us                                                | 9.89 us: 1.01x slower                                                |
| pickle_list         | 2.83 us                                                | 2.90 us: 1.02x slower                                                |
| pickle              | 7.36 us                                                | 7.56 us: 1.03x slower                                                |
| pickle_dict         | 17.8 us                                                | 18.8 us: 1.06x slower                                                |
| Geometric mean      | (ref)                                                  | 1.01x slower                                                         |

Benchmark hidden because not significant (4): json_loads, xml_etree_generate, unpickle_pure_python, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230404-darwin-arm64-python-7d4cc5aa854fdea4d01a-3.10.11-7d4cc5a |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 9.73 ms                                                | 9.13 ms: 1.06x faster                                                |
| python_startup         | 12.6 ms                                                | 12.1 ms: 1.04x faster                                                |
| Geometric mean         | (ref)                                                  | 1.05x faster                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230404-darwin-arm64-python-7d4cc5aa854fdea4d01a-3.10.11-7d4cc5a |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| genshi_text     | 18.4 ms                                                | 18.2 ms: 1.01x faster                                                |
| genshi_xml      | 37.6 ms                                                | 37.3 ms: 1.01x faster                                                |
| django_template | 27.3 ms                                                | 27.1 ms: 1.01x faster                                                |
| mako            | 10.5 ms                                                | 10.6 ms: 1.01x slower                                                |
| Geometric mean  | (ref)                                                  | 1.00x faster                                                         |

All benchmarks:
===============

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230404-darwin-arm64-python-7d4cc5aa854fdea4d01a-3.10.11-7d4cc5a |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site  | 9.73 ms                                                | 9.13 ms: 1.06x faster                                                |
| python_startup          | 12.6 ms                                                | 12.1 ms: 1.04x faster                                                |
| bench_thread_pool       | 548 us                                                 | 532 us: 1.03x faster                                                 |
| aiohttp                 | 1.29 ms                                                | 1.26 ms: 1.03x faster                                                |
| pathlib                 | 28.8 ms                                                | 28.3 ms: 1.02x faster                                                |
| bench_mp_pool           | 41.0 ms                                                | 40.2 ms: 1.02x faster                                                |
| chameleon               | 5.84 ms                                                | 5.75 ms: 1.02x faster                                                |
| telco                   | 3.68 ms                                                | 3.63 ms: 1.01x faster                                                |
| json_dumps              | 8.38 ms                                                | 8.27 ms: 1.01x faster                                                |
| richards                | 51.4 ms                                                | 50.7 ms: 1.01x faster                                                |
| json                    | 3.10 ms                                                | 3.06 ms: 1.01x faster                                                |
| pprint_safe_repr        | 609 ms                                                 | 602 ms: 1.01x faster                                                 |
| thrift                  | 586 us                                                 | 580 us: 1.01x faster                                                 |
| genshi_text             | 18.4 ms                                                | 18.2 ms: 1.01x faster                                                |
| unpack_sequence         | 38.7 ns                                                | 38.3 ns: 1.01x faster                                                |
| genshi_xml              | 37.6 ms                                                | 37.3 ms: 1.01x faster                                                |
| meteor_contest          | 78.6 ms                                                | 78.0 ms: 1.01x faster                                                |
| generators              | 32.9 ms                                                | 32.7 ms: 1.01x faster                                                |
| django_template         | 27.3 ms                                                | 27.1 ms: 1.01x faster                                                |
| pprint_pformat          | 1.24 sec                                               | 1.23 sec: 1.01x faster                                               |
| asyncio_tcp             | 673 ms                                                 | 669 ms: 1.01x faster                                                 |
| dulwich_log             | 37.1 ms                                                | 36.9 ms: 1.00x faster                                                |
| scimark_sor             | 127 ms                                                 | 126 ms: 1.00x faster                                                 |
| scimark_fft             | 232 ms                                                 | 231 ms: 1.00x faster                                                 |
| xml_etree_process       | 45.1 ms                                                | 44.9 ms: 1.00x faster                                                |
| scimark_sparse_mat_mult | 3.47 ms                                                | 3.46 ms: 1.00x faster                                                |
| sqlglot_normalize       | 197 ms                                                 | 196 ms: 1.00x faster                                                 |
| sqlglot_transpile       | 1.54 ms                                                | 1.53 ms: 1.00x faster                                                |
| deepcopy_reduce         | 2.38 us                                                | 2.38 us: 1.00x faster                                                |
| mdp                     | 1.67 sec                                               | 1.67 sec: 1.00x faster                                               |
| create_gc_cycles        | 876 us                                                 | 874 us: 1.00x faster                                                 |
| coroutines              | 20.2 ms                                                | 20.1 ms: 1.00x faster                                                |
| sqlglot_optimize        | 38.0 ms                                                | 38.0 ms: 1.00x faster                                                |
| regex_compile           | 96.6 ms                                                | 96.9 ms: 1.00x slower                                                |
| sqlite_synth            | 1.47 us                                                | 1.48 us: 1.00x slower                                                |
| pyflate                 | 453 ms                                                 | 455 ms: 1.00x slower                                                 |
| 2to3                    | 202 ms                                                 | 203 ms: 1.00x slower                                                 |
| deepcopy                | 278 us                                                 | 279 us: 1.00x slower                                                 |
| fannkuch                | 317 ms                                                 | 319 ms: 1.00x slower                                                 |
| crypto_pyaes            | 78.0 ms                                                | 78.3 ms: 1.00x slower                                                |
| docutils                | 1.78 sec                                               | 1.79 sec: 1.00x slower                                               |
| sympy_expand            | 276 ms                                                 | 277 ms: 1.00x slower                                                 |
| pickle_pure_python      | 284 us                                                 | 285 us: 1.01x slower                                                 |
| logging_simple          | 4.63 us                                                | 4.65 us: 1.01x slower                                                |
| sympy_str               | 169 ms                                                 | 170 ms: 1.01x slower                                                 |
| xml_etree_iterparse     | 72.6 ms                                                | 73.2 ms: 1.01x slower                                                |
| logging_format          | 5.01 us                                                | 5.05 us: 1.01x slower                                                |
| raytrace                | 328 ms                                                 | 331 ms: 1.01x slower                                                 |
| mako                    | 10.5 ms                                                | 10.6 ms: 1.01x slower                                                |
| unpickle_list           | 2.66 us                                                | 2.69 us: 1.01x slower                                                |
| comprehensions          | 17.7 us                                                | 17.9 us: 1.01x slower                                                |
| unpickle                | 9.77 us                                                | 9.89 us: 1.01x slower                                                |
| chaos                   | 66.8 ms                                                | 68.0 ms: 1.02x slower                                                |
| sympy_sum               | 94.3 ms                                                | 96.4 ms: 1.02x slower                                                |
| pickle_list             | 2.83 us                                                | 2.90 us: 1.02x slower                                                |
| coverage                | 40.8 ms                                                | 41.9 ms: 1.03x slower                                                |
| regex_v8                | 17.5 ms                                                | 18.0 ms: 1.03x slower                                                |
| pickle                  | 7.36 us                                                | 7.56 us: 1.03x slower                                                |
| pickle_dict             | 17.8 us                                                | 18.8 us: 1.06x slower                                                |
| html5lib                | 44.1 ms                                                | 47.8 ms: 1.08x slower                                                |
| regex_effbot            | 2.45 ms                                                | 2.69 ms: 1.10x slower                                                |
| regex_dna               | 160 ms                                                 | 185 ms: 1.16x slower                                                 |
| Geometric mean          | (ref)                                                  | 1.00x slower                                                         |

Benchmark hidden because not significant (33): tornado_http, async_tree_none, async_tree_memoization, pycparser, async_tree_cpu_io_mixed, mypy2, async_tree_io, float, json_loads, sqlalchemy_imperative, sqlglot_parse, nbody, scimark_lu, dask, gc_traversal, async_generators, deepcopy_memo, nqueens, pylint, pidigits, spectral_norm, scimark_monte_carlo, xml_etree_generate, unpickle_pure_python, go, sympy_integrate, hexiom, sqlalchemy_declarative, gunicorn, logging_silent, deltablue, flaskblogging, xml_etree_parse
Ignored benchmarks (4) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp_ssl, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 87.12% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x
