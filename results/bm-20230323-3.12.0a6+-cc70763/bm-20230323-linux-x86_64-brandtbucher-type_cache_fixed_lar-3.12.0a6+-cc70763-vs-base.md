
# Results vs. base

- fork: brandtbucher
- ref: type_cache_fixed_lar
- machine: linux-x86_64
- commit hash: cc70763
- commit date: 2023-03-23
- overall geometric mean: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230322-linux-x86_64-python-87be8d95228ee95de904-3.12.0a6+-87be8d9 | bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed_lar-3.12.0a6+-cc70763 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 251 ms                                                                 | 251 ms: 1.00x faster                                                         |
| chameleon      | 6.45 ms                                                                | 6.38 ms: 1.01x faster                                                        |
| docutils       | 2.54 sec                                                               | 2.52 sec: 1.01x faster                                                       |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                                 |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230322-linux-x86_64-python-87be8d95228ee95de904-3.12.0a6+-87be8d9 | bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed_lar-3.12.0a6+-cc70763 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 73.8 ms                                                                | 72.5 ms: 1.02x faster                                                        |
| nbody          | 88.6 ms                                                                | 87.7 ms: 1.01x faster                                                        |
| pidigits       | 188 ms                                                                 | 188 ms: 1.00x slower                                                         |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230322-linux-x86_64-python-87be8d95228ee95de904-3.12.0a6+-87be8d9 | bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed_lar-3.12.0a6+-cc70763 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.61 ms                                                                | 3.42 ms: 1.06x faster                                                        |
| regex_v8       | 22.4 ms                                                                | 21.3 ms: 1.05x faster                                                        |
| regex_compile  | 135 ms                                                                 | 133 ms: 1.02x faster                                                         |
| regex_dna      | 209 ms                                                                 | 206 ms: 1.02x faster                                                         |
| Geometric mean | (ref)                                                                  | 1.04x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230322-linux-x86_64-python-87be8d95228ee95de904-3.12.0a6+-87be8d9 | bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed_lar-3.12.0a6+-cc70763 |
|----------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_parse      | 150 ms                                                                 | 147 ms: 1.02x faster                                                         |
| xml_etree_generate   | 81.7 ms                                                                | 80.6 ms: 1.01x faster                                                        |
| xml_etree_process    | 56.8 ms                                                                | 56.2 ms: 1.01x faster                                                        |
| unpickle_pure_python | 201 us                                                                 | 199 us: 1.01x faster                                                         |
| pickle_pure_python   | 287 us                                                                 | 286 us: 1.00x faster                                                         |
| xml_etree_iterparse  | 99.2 ms                                                                | 99.9 ms: 1.01x slower                                                        |
| pickle               | 10.4 us                                                                | 10.6 us: 1.02x slower                                                        |
| unpickle_list        | 4.98 us                                                                | 5.09 us: 1.02x slower                                                        |
| pickle_list          | 4.24 us                                                                | 4.36 us: 1.03x slower                                                        |
| pickle_dict          | 30.5 us                                                                | 31.7 us: 1.04x slower                                                        |
| Geometric mean       | (ref)                                                                  | 1.00x slower                                                                 |

Benchmark hidden because not significant (3): json_dumps, unpickle, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230322-linux-x86_64-python-87be8d95228ee95de904-3.12.0a6+-87be8d9 | bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed_lar-3.12.0a6+-cc70763 |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 6.50 ms                                                                | 6.55 ms: 1.01x slower                                                        |
| python_startup         | 8.79 ms                                                                | 8.85 ms: 1.01x slower                                                        |
| Geometric mean         | (ref)                                                                  | 1.01x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20230322-linux-x86_64-python-87be8d95228ee95de904-3.12.0a6+-87be8d9 | bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed_lar-3.12.0a6+-cc70763 |
|-----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_text     | 21.8 ms                                                                | 21.2 ms: 1.03x faster                                                        |
| django_template | 33.8 ms                                                                | 33.1 ms: 1.02x faster                                                        |
| genshi_xml      | 48.1 ms                                                                | 47.2 ms: 1.02x faster                                                        |
| mako            | 10.1 ms                                                                | 10.00 ms: 1.01x faster                                                       |
| Geometric mean  | (ref)                                                                  | 1.02x faster                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20230322-linux-x86_64-python-87be8d95228ee95de904-3.12.0a6+-87be8d9 | bm-20230323-linux-x86_64-brandtbucher-type_cache_fixed_lar-3.12.0a6+-cc70763 |
|-------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot            | 3.61 ms                                                                | 3.42 ms: 1.06x faster                                                        |
| regex_v8                | 22.4 ms                                                                | 21.3 ms: 1.05x faster                                                        |
| pycparser               | 1.15 sec                                                               | 1.10 sec: 1.05x faster                                                       |
| scimark_fft             | 319 ms                                                                 | 305 ms: 1.04x faster                                                         |
| scimark_sparse_mat_mult | 4.21 ms                                                                | 4.05 ms: 1.04x faster                                                        |
| deepcopy_reduce         | 3.03 us                                                                | 2.94 us: 1.03x faster                                                        |
| genshi_text             | 21.8 ms                                                                | 21.2 ms: 1.03x faster                                                        |
| fannkuch                | 375 ms                                                                 | 366 ms: 1.03x faster                                                         |
| deepcopy                | 333 us                                                                 | 325 us: 1.02x faster                                                         |
| django_template         | 33.8 ms                                                                | 33.1 ms: 1.02x faster                                                        |
| coverage                | 95.0 ms                                                                | 93.0 ms: 1.02x faster                                                        |
| pathlib                 | 18.2 ms                                                                | 17.8 ms: 1.02x faster                                                        |
| genshi_xml              | 48.1 ms                                                                | 47.2 ms: 1.02x faster                                                        |
| float                   | 73.8 ms                                                                | 72.5 ms: 1.02x faster                                                        |
| regex_compile           | 135 ms                                                                 | 133 ms: 1.02x faster                                                         |
| regex_dna               | 209 ms                                                                 | 206 ms: 1.02x faster                                                         |
| xml_etree_parse         | 150 ms                                                                 | 147 ms: 1.02x faster                                                         |
| thrift                  | 787 us                                                                 | 775 us: 1.02x faster                                                         |
| xml_etree_generate      | 81.7 ms                                                                | 80.6 ms: 1.01x faster                                                        |
| deepcopy_memo           | 35.0 us                                                                | 34.6 us: 1.01x faster                                                        |
| hexiom                  | 6.16 ms                                                                | 6.09 ms: 1.01x faster                                                        |
| chameleon               | 6.45 ms                                                                | 6.38 ms: 1.01x faster                                                        |
| xml_etree_process       | 56.8 ms                                                                | 56.2 ms: 1.01x faster                                                        |
| sympy_str               | 285 ms                                                                 | 282 ms: 1.01x faster                                                         |
| nbody                   | 88.6 ms                                                                | 87.7 ms: 1.01x faster                                                        |
| comprehensions          | 24.0 us                                                                | 23.8 us: 1.01x faster                                                        |
| docutils                | 2.54 sec                                                               | 2.52 sec: 1.01x faster                                                       |
| sympy_expand            | 462 ms                                                                 | 458 ms: 1.01x faster                                                         |
| sympy_sum               | 167 ms                                                                 | 165 ms: 1.01x faster                                                         |
| unpickle_pure_python    | 201 us                                                                 | 199 us: 1.01x faster                                                         |
| sqlglot_normalize       | 107 ms                                                                 | 106 ms: 1.01x faster                                                         |
| async_tree_io           | 1.30 sec                                                               | 1.30 sec: 1.01x faster                                                       |
| mako                    | 10.1 ms                                                                | 10.00 ms: 1.01x faster                                                       |
| mdp                     | 2.71 sec                                                               | 2.69 sec: 1.01x faster                                                       |
| pickle_pure_python      | 287 us                                                                 | 286 us: 1.00x faster                                                         |
| dulwich_log             | 63.2 ms                                                                | 63.0 ms: 1.00x faster                                                        |
| sympy_integrate         | 20.5 ms                                                                | 20.4 ms: 1.00x faster                                                        |
| 2to3                    | 251 ms                                                                 | 251 ms: 1.00x faster                                                         |
| pidigits                | 188 ms                                                                 | 188 ms: 1.00x slower                                                         |
| asyncio_tcp             | 506 ms                                                                 | 509 ms: 1.01x slower                                                         |
| xml_etree_iterparse     | 99.2 ms                                                                | 99.9 ms: 1.01x slower                                                        |
| python_startup_no_site  | 6.50 ms                                                                | 6.55 ms: 1.01x slower                                                        |
| python_startup          | 8.79 ms                                                                | 8.85 ms: 1.01x slower                                                        |
| async_generators        | 409 ms                                                                 | 413 ms: 1.01x slower                                                         |
| sqlite_synth            | 2.61 us                                                                | 2.63 us: 1.01x slower                                                        |
| chaos                   | 65.3 ms                                                                | 66.2 ms: 1.01x slower                                                        |
| crypto_pyaes            | 73.9 ms                                                                | 75.0 ms: 1.01x slower                                                        |
| meteor_contest          | 102 ms                                                                 | 104 ms: 1.02x slower                                                         |
| generators              | 29.3 ms                                                                | 29.8 ms: 1.02x slower                                                        |
| pyflate                 | 408 ms                                                                 | 415 ms: 1.02x slower                                                         |
| pickle                  | 10.4 us                                                                | 10.6 us: 1.02x slower                                                        |
| spectral_norm           | 93.0 ms                                                                | 95.0 ms: 1.02x slower                                                        |
| unpickle_list           | 4.98 us                                                                | 5.09 us: 1.02x slower                                                        |
| deltablue               | 3.23 ms                                                                | 3.30 ms: 1.02x slower                                                        |
| pickle_list             | 4.24 us                                                                | 4.36 us: 1.03x slower                                                        |
| pickle_dict             | 30.5 us                                                                | 31.7 us: 1.04x slower                                                        |
| go                      | 134 ms                                                                 | 140 ms: 1.04x slower                                                         |
| unpack_sequence         | 42.4 ns                                                                | 45.9 ns: 1.08x slower                                                        |
| coroutines              | 21.9 ms                                                                | 23.7 ms: 1.08x slower                                                        |
| Geometric mean          | (ref)                                                                  | 1.00x faster                                                                 |

Benchmark hidden because not significant (32): async_tree_none, async_tree_cpu_io_mixed, telco, sqlglot_transpile, json_dumps, logging_format, create_gc_cycles, richards, scimark_monte_carlo, pprint_pformat, sqlglot_parse, unpickle, bench_mp_pool, json_loads, raytrace, mypy2, scimark_sor, gc_traversal, bench_thread_pool, sqlglot_optimize, tornado_http, logging_simple, gunicorn, logging_silent, pprint_safe_repr, nqueens, html5lib, dask, djangocms, json, async_tree_memoization, scimark_lu
Ignored benchmarks (3) of /home/runner/work/benchmarking/benchmarking/results/bm-20230322-3.12.0a6+-87be8d9/bm-20230322-linux-x86_64-python-87be8d95228ee95de904-3.12.0a6+-87be8d9.json: aiohttp, sqlalchemy_declarative, sqlalchemy_imperative
