
# Results vs. 3.11.0

- fork: iritkatriel
- ref: const_regs2
- machine: linux-x86_64
- commit hash: 1c97383
- commit date: 2023-01-17
- overall geometric mean: 1.01x faster \*
- HPT reliability: 89.64%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230117-linux-x86_64-iritkatriel-const_regs2-3.12.0a4+-1c97383 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| docutils       | 2.63 sec                                               | 2.61 sec: 1.00x faster                                             |
| html5lib       | 64.5 ms                                                | 60.7 ms: 1.06x faster                                              |
| Geometric mean | (ref)                                                  | 1.02x faster                                                       |

Benchmark hidden because not significant (2): 2to3, chameleon

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230117-linux-x86_64-iritkatriel-const_regs2-3.12.0a4+-1c97383 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 77.2 ms                                                | 74.9 ms: 1.03x faster                                              |
| pidigits       | 198 ms                                                 | 198 ms: 1.00x faster                                               |
| nbody          | 93.1 ms                                                | 96.2 ms: 1.03x slower                                              |
| Geometric mean | (ref)                                                  | 1.00x slower                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230117-linux-x86_64-iritkatriel-const_regs2-3.12.0a4+-1c97383 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.47 ms: 1.15x faster                                              |
| regex_compile  | 138 ms                                                 | 134 ms: 1.03x faster                                               |
| regex_v8       | 22.0 ms                                                | 22.6 ms: 1.03x slower                                              |
| regex_dna      | 204 ms                                                 | 210 ms: 1.03x slower                                               |
| Geometric mean | (ref)                                                  | 1.03x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230117-linux-x86_64-iritkatriel-const_regs2-3.12.0a4+-1c97383 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.51 ms: 1.32x faster                                              |
| unpickle_pure_python | 228 us                                                 | 205 us: 1.11x faster                                               |
| json_loads           | 26.5 us                                                | 24.2 us: 1.10x faster                                              |
| xml_etree_parse      | 158 ms                                                 | 150 ms: 1.06x faster                                               |
| pickle_pure_python   | 306 us                                                 | 299 us: 1.02x faster                                               |
| pickle_dict          | 31.1 us                                                | 30.7 us: 1.01x faster                                              |
| xml_etree_iterparse  | 104 ms                                                 | 103 ms: 1.01x faster                                               |
| unpickle_list        | 4.91 us                                                | 4.88 us: 1.00x faster                                              |
| pickle_list          | 4.11 us                                                | 4.17 us: 1.01x slower                                              |
| xml_etree_process    | 53.9 ms                                                | 54.9 ms: 1.02x slower                                              |
| xml_etree_generate   | 76.2 ms                                                | 78.8 ms: 1.03x slower                                              |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                       |

Benchmark hidden because not significant (2): unpickle, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230117-linux-x86_64-iritkatriel-const_regs2-3.12.0a4+-1c97383 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.60 ms: 1.01x slower                                              |
| python_startup_no_site | 6.01 ms                                                | 6.13 ms: 1.02x slower                                              |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230117-linux-x86_64-iritkatriel-const_regs2-3.12.0a4+-1c97383 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 47.8 ms: 1.08x faster                                              |
| genshi_text     | 21.6 ms                                                | 20.8 ms: 1.03x faster                                              |
| mako            | 10.1 ms                                                | 9.85 ms: 1.02x faster                                              |
| django_template | 32.6 ms                                                | 34.5 ms: 1.06x slower                                              |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                       |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230117-linux-x86_64-iritkatriel-const_regs2-3.12.0a4+-1c97383 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| asyncio_tcp             | 922 ms                                                 | 505 ms: 1.83x faster                                               |
| json_dumps              | 12.6 ms                                                | 9.51 ms: 1.32x faster                                              |
| regex_effbot            | 3.99 ms                                                | 3.47 ms: 1.15x faster                                              |
| unpickle_pure_python    | 228 us                                                 | 205 us: 1.11x faster                                               |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.07 ms: 1.10x faster                                              |
| json_loads              | 26.5 us                                                | 24.2 us: 1.10x faster                                              |
| genshi_xml              | 51.8 ms                                                | 47.8 ms: 1.08x faster                                              |
| deltablue               | 3.67 ms                                                | 3.42 ms: 1.08x faster                                              |
| scimark_sor             | 118 ms                                                 | 111 ms: 1.07x faster                                               |
| html5lib                | 64.5 ms                                                | 60.7 ms: 1.06x faster                                              |
| fannkuch                | 388 ms                                                 | 366 ms: 1.06x faster                                               |
| xml_etree_parse         | 158 ms                                                 | 150 ms: 1.06x faster                                               |
| nqueens                 | 83.4 ms                                                | 78.9 ms: 1.06x faster                                              |
| json                    | 4.94 ms                                                | 4.74 ms: 1.04x faster                                              |
| scimark_fft             | 328 ms                                                 | 315 ms: 1.04x faster                                               |
| genshi_text             | 21.6 ms                                                | 20.8 ms: 1.03x faster                                              |
| unpack_sequence         | 43.1 ns                                                | 41.7 ns: 1.03x faster                                              |
| async_generators        | 368 ms                                                 | 356 ms: 1.03x faster                                               |
| deepcopy_memo           | 37.0 us                                                | 35.8 us: 1.03x faster                                              |
| meteor_contest          | 107 ms                                                 | 103 ms: 1.03x faster                                               |
| float                   | 77.2 ms                                                | 74.9 ms: 1.03x faster                                              |
| richards                | 45.7 ms                                                | 44.4 ms: 1.03x faster                                              |
| regex_compile           | 138 ms                                                 | 134 ms: 1.03x faster                                               |
| scimark_monte_carlo     | 68.1 ms                                                | 66.1 ms: 1.03x faster                                              |
| telco                   | 6.58 ms                                                | 6.41 ms: 1.03x faster                                              |
| mdp                     | 2.62 sec                                               | 2.55 sec: 1.03x faster                                             |
| logging_silent          | 101 ns                                                 | 98.6 ns: 1.03x faster                                              |
| mako                    | 10.1 ms                                                | 9.85 ms: 1.02x faster                                              |
| pycparser               | 1.18 sec                                               | 1.15 sec: 1.02x faster                                             |
| pickle_pure_python      | 306 us                                                 | 299 us: 1.02x faster                                               |
| bench_thread_pool       | 819 us                                                 | 801 us: 1.02x faster                                               |
| pyflate                 | 418 ms                                                 | 409 ms: 1.02x faster                                               |
| pprint_pformat          | 1.46 sec                                               | 1.43 sec: 1.02x faster                                             |
| logging_format          | 6.68 us                                                | 6.57 us: 1.02x faster                                              |
| create_gc_cycles        | 1.49 ms                                                | 1.46 ms: 1.02x faster                                              |
| pickle_dict             | 31.1 us                                                | 30.7 us: 1.01x faster                                              |
| sympy_expand            | 475 ms                                                 | 470 ms: 1.01x faster                                               |
| hexiom                  | 6.37 ms                                                | 6.31 ms: 1.01x faster                                              |
| xml_etree_iterparse     | 104 ms                                                 | 103 ms: 1.01x faster                                               |
| pprint_safe_repr        | 701 ms                                                 | 697 ms: 1.01x faster                                               |
| thrift                  | 756 us                                                 | 753 us: 1.01x faster                                               |
| docutils                | 2.63 sec                                               | 2.61 sec: 1.00x faster                                             |
| unpickle_list           | 4.91 us                                                | 4.88 us: 1.00x faster                                              |
| sqlglot_optimize        | 53.1 ms                                                | 53.0 ms: 1.00x faster                                              |
| pidigits                | 198 ms                                                 | 198 ms: 1.00x faster                                               |
| sympy_sum               | 167 ms                                                 | 168 ms: 1.01x slower                                               |
| go                      | 140 ms                                                 | 141 ms: 1.01x slower                                               |
| python_startup          | 8.52 ms                                                | 8.60 ms: 1.01x slower                                              |
| dulwich_log             | 63.7 ms                                                | 64.3 ms: 1.01x slower                                              |
| coverage                | 100 ms                                                 | 101 ms: 1.01x slower                                               |
| sqlglot_normalize       | 108 ms                                                 | 109 ms: 1.01x slower                                               |
| pickle_list             | 4.11 us                                                | 4.17 us: 1.01x slower                                              |
| raytrace                | 297 ms                                                 | 301 ms: 1.01x slower                                               |
| async_tree_none         | 526 ms                                                 | 534 ms: 1.01x slower                                               |
| crypto_pyaes            | 74.7 ms                                                | 75.9 ms: 1.02x slower                                              |
| coroutines              | 25.5 ms                                                | 26.0 ms: 1.02x slower                                              |
| xml_etree_process       | 53.9 ms                                                | 54.9 ms: 1.02x slower                                              |
| python_startup_no_site  | 6.01 ms                                                | 6.13 ms: 1.02x slower                                              |
| deepcopy                | 342 us                                                 | 350 us: 1.02x slower                                               |
| regex_v8                | 22.0 ms                                                | 22.6 ms: 1.03x slower                                              |
| sqlite_synth            | 2.52 us                                                | 2.59 us: 1.03x slower                                              |
| regex_dna               | 204 ms                                                 | 210 ms: 1.03x slower                                               |
| async_tree_io           | 1.30 sec                                               | 1.33 sec: 1.03x slower                                             |
| nbody                   | 93.1 ms                                                | 96.2 ms: 1.03x slower                                              |
| xml_etree_generate      | 76.2 ms                                                | 78.8 ms: 1.03x slower                                              |
| async_tree_cpu_io_mixed | 739 ms                                                 | 765 ms: 1.03x slower                                               |
| sqlglot_transpile       | 1.70 ms                                                | 1.78 ms: 1.04x slower                                              |
| sqlglot_parse           | 1.40 ms                                                | 1.48 ms: 1.05x slower                                              |
| sympy_integrate         | 21.0 ms                                                | 22.1 ms: 1.05x slower                                              |
| django_template         | 32.6 ms                                                | 34.5 ms: 1.06x slower                                              |
| deepcopy_reduce         | 2.94 us                                                | 3.12 us: 1.06x slower                                              |
| async_tree_memoization  | 627 ms                                                 | 667 ms: 1.06x slower                                               |
| gc_traversal            | 4.02 ms                                                | 4.29 ms: 1.07x slower                                              |
| generators              | 73.5 ms                                                | 79.9 ms: 1.09x slower                                              |
| dask                    | 360 ms                                                 | 519 ms: 1.44x slower                                               |
| Geometric mean          | (ref)                                                  | 1.01x faster                                                       |

Benchmark hidden because not significant (12): unpickle, logging_simple, chaos, pickle, chameleon, bench_mp_pool, 2to3, sympy_str, spectral_norm, pathlib, djangocms, scimark_lu
Ignored benchmarks (13) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, comprehensions, flaskblogging, gunicorn, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, tornado_http, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230117-3.12.0a4+-1c97383/bm-20230117-linux-x86_64-iritkatriel-const_regs2-3.12.0a4+-1c97383.json: mypy


# HPT report

- Reliability score: 89.64% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x
