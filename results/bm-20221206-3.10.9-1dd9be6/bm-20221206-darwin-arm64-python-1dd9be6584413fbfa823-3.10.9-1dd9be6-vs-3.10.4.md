
# Results vs. 3.10.4

- fork: python
- ref: 1dd9be6584413fbfa823
- machine: darwin-arm64
- commit hash: 1dd9be6
- commit date: 2022-12-06
- overall geometric mean: 1.01x faster \*
- HPT reliability: 99.96%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221206-darwin-arm64-python-1dd9be6584413fbfa823-3.10.9-1dd9be6 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 202 ms                                                 | 223 ms: 1.10x slower                                                |
| docutils       | 1.78 sec                                               | 1.77 sec: 1.01x faster                                              |
| html5lib       | 44.1 ms                                                | 46.5 ms: 1.05x slower                                               |
| Geometric mean | (ref)                                                  | 1.03x slower                                                        |

Benchmark hidden because not significant (2): chameleon, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221206-darwin-arm64-python-1dd9be6584413fbfa823-3.10.9-1dd9be6 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 94.1 ms                                                | 92.6 ms: 1.02x faster                                               |
| float          | 72.3 ms                                                | 72.1 ms: 1.00x faster                                               |
| pidigits       | 282 ms                                                 | 284 ms: 1.01x slower                                                |
| Geometric mean | (ref)                                                  | 1.01x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221206-darwin-arm64-python-1dd9be6584413fbfa823-3.10.9-1dd9be6 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 96.6 ms                                                | 96.5 ms: 1.00x faster                                               |
| regex_v8       | 17.5 ms                                                | 18.3 ms: 1.04x slower                                               |
| regex_effbot   | 2.45 ms                                                | 2.64 ms: 1.08x slower                                               |
| regex_dna      | 160 ms                                                 | 180 ms: 1.13x slower                                                |
| Geometric mean | (ref)                                                  | 1.06x slower                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221206-darwin-arm64-python-1dd9be6584413fbfa823-3.10.9-1dd9be6 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| xml_etree_parse      | 107 ms                                                 | 100 ms: 1.07x faster                                                |
| xml_etree_iterparse  | 72.6 ms                                                | 69.0 ms: 1.05x faster                                               |
| json_dumps           | 8.38 ms                                                | 8.25 ms: 1.02x faster                                               |
| xml_etree_process    | 45.1 ms                                                | 44.9 ms: 1.00x faster                                               |
| unpickle_pure_python | 203 us                                                 | 203 us: 1.00x faster                                                |
| json_loads           | 16.9 us                                                | 17.0 us: 1.01x slower                                               |
| unpickle             | 9.77 us                                                | 9.87 us: 1.01x slower                                               |
| pickle               | 7.36 us                                                | 7.56 us: 1.03x slower                                               |
| pickle_list          | 2.83 us                                                | 2.96 us: 1.05x slower                                               |
| pickle_dict          | 17.8 us                                                | 18.8 us: 1.06x slower                                               |
| Geometric mean       | (ref)                                                  | 1.00x slower                                                        |

Benchmark hidden because not significant (3): unpickle_list, xml_etree_generate, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221206-darwin-arm64-python-1dd9be6584413fbfa823-3.10.9-1dd9be6 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 9.73 ms                                                | 6.95 ms: 1.40x faster                                               |
| python_startup         | 12.6 ms                                                | 9.57 ms: 1.32x faster                                               |
| Geometric mean         | (ref)                                                  | 1.36x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221206-darwin-arm64-python-1dd9be6584413fbfa823-3.10.9-1dd9be6 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_text     | 18.4 ms                                                | 18.2 ms: 1.01x faster                                               |
| genshi_xml      | 37.6 ms                                                | 37.3 ms: 1.01x faster                                               |
| django_template | 27.3 ms                                                | 27.3 ms: 1.00x faster                                               |
| mako            | 10.5 ms                                                | 10.7 ms: 1.02x slower                                               |
| Geometric mean  | (ref)                                                  | 1.00x faster                                                        |

All benchmarks:
===============

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20221206-darwin-arm64-python-1dd9be6584413fbfa823-3.10.9-1dd9be6 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site  | 9.73 ms                                                | 6.95 ms: 1.40x faster                                               |
| python_startup          | 12.6 ms                                                | 9.57 ms: 1.32x faster                                               |
| pathlib                 | 28.8 ms                                                | 22.0 ms: 1.31x faster                                               |
| aiohttp                 | 1.29 ms                                                | 1.19 ms: 1.09x faster                                               |
| xml_etree_parse         | 107 ms                                                 | 100 ms: 1.07x faster                                                |
| gunicorn                | 1.34 ms                                                | 1.26 ms: 1.06x faster                                               |
| bench_thread_pool       | 548 us                                                 | 518 us: 1.06x faster                                                |
| flaskblogging           | 2.75 ms                                                | 2.60 ms: 1.06x faster                                               |
| xml_etree_iterparse     | 72.6 ms                                                | 69.0 ms: 1.05x faster                                               |
| unpack_sequence         | 38.7 ns                                                | 37.4 ns: 1.03x faster                                               |
| async_tree_memoization  | 493 ms                                                 | 481 ms: 1.02x faster                                                |
| pylint                  | 307 ms                                                 | 300 ms: 1.02x faster                                                |
| async_tree_none         | 402 ms                                                 | 394 ms: 1.02x faster                                                |
| deepcopy_reduce         | 2.38 us                                                | 2.34 us: 1.02x faster                                               |
| async_tree_io           | 1.02 sec                                               | 1.00 sec: 1.02x faster                                              |
| nbody                   | 94.1 ms                                                | 92.6 ms: 1.02x faster                                               |
| meteor_contest          | 78.6 ms                                                | 77.4 ms: 1.02x faster                                               |
| generators              | 32.9 ms                                                | 32.4 ms: 1.02x faster                                               |
| json_dumps              | 8.38 ms                                                | 8.25 ms: 1.02x faster                                               |
| async_tree_cpu_io_mixed | 670 ms                                                 | 661 ms: 1.01x faster                                                |
| genshi_text             | 18.4 ms                                                | 18.2 ms: 1.01x faster                                               |
| telco                   | 3.68 ms                                                | 3.64 ms: 1.01x faster                                               |
| scimark_fft             | 232 ms                                                 | 230 ms: 1.01x faster                                                |
| dulwich_log             | 37.1 ms                                                | 36.7 ms: 1.01x faster                                               |
| async_generators        | 233 ms                                                 | 231 ms: 1.01x faster                                                |
| pprint_safe_repr        | 609 ms                                                 | 603 ms: 1.01x faster                                                |
| pprint_pformat          | 1.24 sec                                               | 1.23 sec: 1.01x faster                                              |
| sqlalchemy_imperative   | 9.03 ms                                                | 8.96 ms: 1.01x faster                                               |
| thrift                  | 586 us                                                 | 582 us: 1.01x faster                                                |
| docutils                | 1.78 sec                                               | 1.77 sec: 1.01x faster                                              |
| genshi_xml              | 37.6 ms                                                | 37.3 ms: 1.01x faster                                               |
| richards                | 51.4 ms                                                | 51.0 ms: 1.01x faster                                               |
| coverage                | 40.8 ms                                                | 40.6 ms: 1.00x faster                                               |
| logging_format          | 5.01 us                                                | 4.99 us: 1.00x faster                                               |
| sqlalchemy_declarative  | 74.8 ms                                                | 74.5 ms: 1.00x faster                                               |
| float                   | 72.3 ms                                                | 72.1 ms: 1.00x faster                                               |
| sqlglot_normalize       | 197 ms                                                 | 196 ms: 1.00x faster                                                |
| scimark_lu              | 110 ms                                                 | 110 ms: 1.00x faster                                                |
| chaos                   | 66.8 ms                                                | 66.6 ms: 1.00x faster                                               |
| mdp                     | 1.67 sec                                               | 1.66 sec: 1.00x faster                                              |
| sqlglot_optimize        | 38.0 ms                                                | 37.9 ms: 1.00x faster                                               |
| xml_etree_process       | 45.1 ms                                                | 44.9 ms: 1.00x faster                                               |
| unpickle_pure_python    | 203 us                                                 | 203 us: 1.00x faster                                                |
| hexiom                  | 6.32 ms                                                | 6.30 ms: 1.00x faster                                               |
| django_template         | 27.3 ms                                                | 27.3 ms: 1.00x faster                                               |
| spectral_norm           | 96.4 ms                                                | 96.2 ms: 1.00x faster                                               |
| scimark_sparse_mat_mult | 3.47 ms                                                | 3.46 ms: 1.00x faster                                               |
| regex_compile           | 96.6 ms                                                | 96.5 ms: 1.00x faster                                               |
| coroutines              | 20.2 ms                                                | 20.1 ms: 1.00x faster                                               |
| crypto_pyaes            | 78.0 ms                                                | 77.9 ms: 1.00x faster                                               |
| fannkuch                | 317 ms                                                 | 318 ms: 1.00x slower                                                |
| sympy_expand            | 276 ms                                                 | 276 ms: 1.00x slower                                                |
| go                      | 165 ms                                                 | 165 ms: 1.00x slower                                                |
| sympy_str               | 169 ms                                                 | 170 ms: 1.00x slower                                                |
| json                    | 3.10 ms                                                | 3.11 ms: 1.01x slower                                               |
| pidigits                | 282 ms                                                 | 284 ms: 1.01x slower                                                |
| sqlglot_transpile       | 1.54 ms                                                | 1.55 ms: 1.01x slower                                               |
| deepcopy                | 278 us                                                 | 280 us: 1.01x slower                                                |
| json_loads              | 16.9 us                                                | 17.0 us: 1.01x slower                                               |
| sqlite_synth            | 1.47 us                                                | 1.49 us: 1.01x slower                                               |
| unpickle                | 9.77 us                                                | 9.87 us: 1.01x slower                                               |
| sympy_sum               | 94.3 ms                                                | 95.4 ms: 1.01x slower                                               |
| mako                    | 10.5 ms                                                | 10.7 ms: 1.02x slower                                               |
| pickle                  | 7.36 us                                                | 7.56 us: 1.03x slower                                               |
| regex_v8                | 17.5 ms                                                | 18.3 ms: 1.04x slower                                               |
| pickle_list             | 2.83 us                                                | 2.96 us: 1.05x slower                                               |
| html5lib                | 44.1 ms                                                | 46.5 ms: 1.05x slower                                               |
| pickle_dict             | 17.8 us                                                | 18.8 us: 1.06x slower                                               |
| regex_effbot            | 2.45 ms                                                | 2.64 ms: 1.08x slower                                               |
| 2to3                    | 202 ms                                                 | 223 ms: 1.10x slower                                                |
| regex_dna               | 160 ms                                                 | 180 ms: 1.13x slower                                                |
| Geometric mean          | (ref)                                                  | 1.01x faster                                                        |

Benchmark hidden because not significant (18): logging_silent, scimark_sor, bench_mp_pool, scimark_monte_carlo, pycparser, raytrace, chameleon, pyflate, deepcopy_memo, unpickle_list, deltablue, logging_simple, xml_etree_generate, nqueens, sympy_integrate, pickle_pure_python, sqlglot_parse, tornado_http
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: asyncio_tcp, asyncio_tcp_ssl, comprehensions, create_gc_cycles, dask, gc_traversal, mypy2, richards_super, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20221206-3.10.9-1dd9be6/bm-20221206-darwin-arm64-python-1dd9be6584413fbfa823-3.10.9-1dd9be6.json: mypy


# HPT report

- Reliability score: 99.96% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x
