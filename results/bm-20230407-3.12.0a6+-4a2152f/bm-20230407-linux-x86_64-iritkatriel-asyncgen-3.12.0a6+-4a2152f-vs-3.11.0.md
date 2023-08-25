
# Results vs. 3.11.0

- fork: iritkatriel
- ref: asyncgen
- machine: linux-x86_64
- commit hash: 4a2152f
- commit date: 2023-04-07
- overall geometric mean: 1.04x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230407-linux-x86_64-iritkatriel-asyncgen-3.12.0a6+-4a2152f |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 252 ms: 1.03x faster                                            |
| chameleon      | 6.47 ms                                                | 6.54 ms: 1.01x slower                                           |
| docutils       | 2.63 sec                                               | 2.55 sec: 1.03x faster                                          |
| html5lib       | 64.5 ms                                                | 62.0 ms: 1.04x faster                                           |
| tornado_http   | 96.3 ms                                                | 90.9 ms: 1.06x faster                                           |
| Geometric mean | (ref)                                                  | 1.03x faster                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230407-linux-x86_64-iritkatriel-asyncgen-3.12.0a6+-4a2152f |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| nbody          | 93.1 ms                                                | 87.4 ms: 1.07x faster                                           |
| pidigits       | 198 ms                                                 | 188 ms: 1.05x faster                                            |
| float          | 77.2 ms                                                | 74.4 ms: 1.04x faster                                           |
| Geometric mean | (ref)                                                  | 1.05x faster                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230407-linux-x86_64-iritkatriel-asyncgen-3.12.0a6+-4a2152f |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.74 ms: 1.07x faster                                           |
| regex_compile  | 138 ms                                                 | 135 ms: 1.03x faster                                            |
| regex_v8       | 22.0 ms                                                | 22.4 ms: 1.02x slower                                           |
| regex_dna      | 204 ms                                                 | 213 ms: 1.04x slower                                            |
| Geometric mean | (ref)                                                  | 1.01x faster                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230407-linux-x86_64-iritkatriel-asyncgen-3.12.0a6+-4a2152f |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.59 ms: 1.31x faster                                           |
| unpickle_pure_python | 228 us                                                 | 198 us: 1.15x faster                                            |
| json_loads           | 26.5 us                                                | 24.3 us: 1.09x faster                                           |
| pickle_pure_python   | 306 us                                                 | 287 us: 1.07x faster                                            |
| xml_etree_parse      | 158 ms                                                 | 149 ms: 1.07x faster                                            |
| xml_etree_iterparse  | 104 ms                                                 | 99.4 ms: 1.04x faster                                           |
| unpickle_list        | 4.91 us                                                | 4.98 us: 1.01x slower                                           |
| xml_etree_process    | 53.9 ms                                                | 55.0 ms: 1.02x slower                                           |
| pickle_list          | 4.11 us                                                | 4.24 us: 1.03x slower                                           |
| pickle_dict          | 31.1 us                                                | 32.2 us: 1.03x slower                                           |
| pickle               | 10.1 us                                                | 10.4 us: 1.03x slower                                           |
| xml_etree_generate   | 76.2 ms                                                | 80.6 ms: 1.06x slower                                           |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                    |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230407-linux-x86_64-iritkatriel-asyncgen-3.12.0a6+-4a2152f |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.84 ms: 1.04x slower                                           |
| python_startup_no_site | 6.01 ms                                                | 6.52 ms: 1.09x slower                                           |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230407-linux-x86_64-iritkatriel-asyncgen-3.12.0a6+-4a2152f |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 47.8 ms: 1.08x faster                                           |
| mako            | 10.1 ms                                                | 9.97 ms: 1.01x faster                                           |
| django_template | 32.6 ms                                                | 33.0 ms: 1.01x slower                                           |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                    |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230407-linux-x86_64-iritkatriel-asyncgen-3.12.0a6+-4a2152f |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 29.6 ms: 2.48x faster                                           |
| asyncio_tcp             | 922 ms                                                 | 507 ms: 1.82x faster                                            |
| json_dumps              | 12.6 ms                                                | 9.59 ms: 1.31x faster                                           |
| mypy2                   | 420 ms                                                 | 332 ms: 1.27x faster                                            |
| deltablue               | 3.67 ms                                                | 3.19 ms: 1.15x faster                                           |
| unpickle_pure_python    | 228 us                                                 | 198 us: 1.15x faster                                            |
| coroutines              | 25.5 ms                                                | 23.3 ms: 1.10x faster                                           |
| aiohttp                 | 1.10 ms                                                | 1.01 ms: 1.09x faster                                           |
| json_loads              | 26.5 us                                                | 24.3 us: 1.09x faster                                           |
| deepcopy_memo           | 37.0 us                                                | 34.0 us: 1.09x faster                                           |
| gunicorn                | 1.18 ms                                                | 1.09 ms: 1.08x faster                                           |
| genshi_xml              | 51.8 ms                                                | 47.8 ms: 1.08x faster                                           |
| logging_silent          | 101 ns                                                 | 94.5 ns: 1.07x faster                                           |
| scimark_fft             | 328 ms                                                 | 307 ms: 1.07x faster                                            |
| logging_format          | 6.68 us                                                | 6.25 us: 1.07x faster                                           |
| regex_effbot            | 3.99 ms                                                | 3.74 ms: 1.07x faster                                           |
| pickle_pure_python      | 306 us                                                 | 287 us: 1.07x faster                                            |
| scimark_sor             | 118 ms                                                 | 111 ms: 1.07x faster                                            |
| xml_etree_parse         | 158 ms                                                 | 149 ms: 1.07x faster                                            |
| nbody                   | 93.1 ms                                                | 87.4 ms: 1.07x faster                                           |
| deepcopy                | 342 us                                                 | 322 us: 1.06x faster                                            |
| json                    | 4.94 ms                                                | 4.65 ms: 1.06x faster                                           |
| raytrace                | 297 ms                                                 | 280 ms: 1.06x faster                                            |
| tornado_http            | 96.3 ms                                                | 90.9 ms: 1.06x faster                                           |
| logging_simple          | 6.03 us                                                | 5.70 us: 1.06x faster                                           |
| hexiom                  | 6.37 ms                                                | 6.04 ms: 1.06x faster                                           |
| pidigits                | 198 ms                                                 | 188 ms: 1.05x faster                                            |
| coverage                | 100 ms                                                 | 95.4 ms: 1.05x faster                                           |
| mdp                     | 2.62 sec                                               | 2.50 sec: 1.05x faster                                          |
| xml_etree_iterparse     | 104 ms                                                 | 99.4 ms: 1.04x faster                                           |
| chaos                   | 69.2 ms                                                | 66.3 ms: 1.04x faster                                           |
| nqueens                 | 83.4 ms                                                | 80.1 ms: 1.04x faster                                           |
| meteor_contest          | 107 ms                                                 | 103 ms: 1.04x faster                                            |
| html5lib                | 64.5 ms                                                | 62.0 ms: 1.04x faster                                           |
| spectral_norm           | 100 ms                                                 | 96.2 ms: 1.04x faster                                           |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.33 ms: 1.04x faster                                           |
| float                   | 77.2 ms                                                | 74.4 ms: 1.04x faster                                           |
| sqlglot_optimize        | 53.1 ms                                                | 51.2 ms: 1.04x faster                                           |
| bench_thread_pool       | 819 us                                                 | 790 us: 1.04x faster                                            |
| pycparser               | 1.18 sec                                               | 1.14 sec: 1.03x faster                                          |
| sympy_expand            | 475 ms                                                 | 460 ms: 1.03x faster                                            |
| richards                | 45.7 ms                                                | 44.3 ms: 1.03x faster                                           |
| pprint_pformat          | 1.46 sec                                               | 1.41 sec: 1.03x faster                                          |
| docutils                | 2.63 sec                                               | 2.55 sec: 1.03x faster                                          |
| sympy_integrate         | 21.0 ms                                                | 20.4 ms: 1.03x faster                                           |
| 2to3                    | 259 ms                                                 | 252 ms: 1.03x faster                                            |
| regex_compile           | 138 ms                                                 | 135 ms: 1.03x faster                                            |
| sqlglot_normalize       | 108 ms                                                 | 105 ms: 1.02x faster                                            |
| sympy_str               | 290 ms                                                 | 284 ms: 1.02x faster                                            |
| pprint_safe_repr        | 701 ms                                                 | 687 ms: 1.02x faster                                            |
| telco                   | 6.58 ms                                                | 6.46 ms: 1.02x faster                                           |
| sqlalchemy_declarative  | 138 ms                                                 | 136 ms: 1.01x faster                                            |
| deepcopy_reduce         | 2.94 us                                                | 2.90 us: 1.01x faster                                           |
| create_gc_cycles        | 1.49 ms                                                | 1.47 ms: 1.01x faster                                           |
| scimark_lu              | 110 ms                                                 | 108 ms: 1.01x faster                                            |
| mako                    | 10.1 ms                                                | 9.97 ms: 1.01x faster                                           |
| dulwich_log             | 63.7 ms                                                | 63.0 ms: 1.01x faster                                           |
| unpack_sequence         | 43.1 ns                                                | 42.7 ns: 1.01x faster                                           |
| crypto_pyaes            | 74.7 ms                                                | 74.0 ms: 1.01x faster                                           |
| pathlib                 | 18.2 ms                                                | 18.1 ms: 1.01x faster                                           |
| pyflate                 | 418 ms                                                 | 421 ms: 1.01x slower                                            |
| sqlglot_transpile       | 1.70 ms                                                | 1.72 ms: 1.01x slower                                           |
| chameleon               | 6.47 ms                                                | 6.54 ms: 1.01x slower                                           |
| scimark_monte_carlo     | 68.1 ms                                                | 68.9 ms: 1.01x slower                                           |
| django_template         | 32.6 ms                                                | 33.0 ms: 1.01x slower                                           |
| unpickle_list           | 4.91 us                                                | 4.98 us: 1.01x slower                                           |
| async_tree_memoization  | 627 ms                                                 | 637 ms: 1.02x slower                                            |
| fannkuch                | 388 ms                                                 | 394 ms: 1.02x slower                                            |
| regex_v8                | 22.0 ms                                                | 22.4 ms: 1.02x slower                                           |
| sqlglot_parse           | 1.40 ms                                                | 1.43 ms: 1.02x slower                                           |
| xml_etree_process       | 53.9 ms                                                | 55.0 ms: 1.02x slower                                           |
| thrift                  | 756 us                                                 | 781 us: 1.03x slower                                            |
| pickle_list             | 4.11 us                                                | 4.24 us: 1.03x slower                                           |
| pickle_dict             | 31.1 us                                                | 32.2 us: 1.03x slower                                           |
| pickle                  | 10.1 us                                                | 10.4 us: 1.03x slower                                           |
| sqlite_synth            | 2.52 us                                                | 2.61 us: 1.04x slower                                           |
| python_startup          | 8.52 ms                                                | 8.84 ms: 1.04x slower                                           |
| regex_dna               | 204 ms                                                 | 213 ms: 1.04x slower                                            |
| xml_etree_generate      | 76.2 ms                                                | 80.6 ms: 1.06x slower                                           |
| comprehensions          | 22.4 us                                                | 23.8 us: 1.06x slower                                           |
| gc_traversal            | 4.02 ms                                                | 4.32 ms: 1.07x slower                                           |
| python_startup_no_site  | 6.01 ms                                                | 6.52 ms: 1.09x slower                                           |
| async_generators        | 368 ms                                                 | 407 ms: 1.10x slower                                            |
| dask                    | 360 ms                                                 | 509 ms: 1.42x slower                                            |
| Geometric mean          | (ref)                                                  | 1.04x faster                                                    |

Benchmark hidden because not significant (10): unpickle, sqlalchemy_imperative, async_tree_none, async_tree_io, bench_mp_pool, sympy_sum, go, async_tree_cpu_io_mixed, djangocms, genshi_text
Ignored benchmarks (6) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x
