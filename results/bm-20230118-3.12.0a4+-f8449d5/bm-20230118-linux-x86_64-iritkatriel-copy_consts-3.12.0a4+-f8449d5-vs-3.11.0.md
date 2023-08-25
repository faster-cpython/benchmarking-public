
# Results vs. 3.11.0

- fork: iritkatriel
- ref: copy_consts
- machine: linux-x86_64
- commit hash: f8449d5
- commit date: 2023-01-18
- overall geometric mean: 1.02x faster \*
- HPT reliability: 99.99%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-iritkatriel-copy_consts-3.12.0a4+-f8449d5 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 257 ms: 1.01x faster                                               |
| chameleon      | 6.47 ms                                                | 6.53 ms: 1.01x slower                                              |
| docutils       | 2.63 sec                                               | 2.59 sec: 1.01x faster                                             |
| html5lib       | 64.5 ms                                                | 61.5 ms: 1.05x faster                                              |
| Geometric mean | (ref)                                                  | 1.01x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-iritkatriel-copy_consts-3.12.0a4+-f8449d5 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 77.2 ms                                                | 73.5 ms: 1.05x faster                                              |
| pidigits       | 198 ms                                                 | 190 ms: 1.04x faster                                               |
| Geometric mean | (ref)                                                  | 1.03x faster                                                       |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-iritkatriel-copy_consts-3.12.0a4+-f8449d5 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.41 ms: 1.17x faster                                              |
| regex_compile  | 138 ms                                                 | 132 ms: 1.04x faster                                               |
| regex_v8       | 22.0 ms                                                | 21.3 ms: 1.03x faster                                              |
| regex_dna      | 204 ms                                                 | 201 ms: 1.02x faster                                               |
| Geometric mean | (ref)                                                  | 1.06x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-iritkatriel-copy_consts-3.12.0a4+-f8449d5 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.65 ms: 1.30x faster                                              |
| unpickle_pure_python | 228 us                                                 | 201 us: 1.13x faster                                               |
| json_loads           | 26.5 us                                                | 24.1 us: 1.10x faster                                              |
| xml_etree_parse      | 158 ms                                                 | 150 ms: 1.06x faster                                               |
| pickle_pure_python   | 306 us                                                 | 293 us: 1.04x faster                                               |
| unpickle             | 13.7 us                                                | 13.3 us: 1.03x faster                                              |
| pickle_list          | 4.11 us                                                | 4.03 us: 1.02x faster                                              |
| pickle_dict          | 31.1 us                                                | 30.6 us: 1.02x faster                                              |
| xml_etree_iterparse  | 104 ms                                                 | 103 ms: 1.01x faster                                               |
| unpickle_list        | 4.91 us                                                | 4.97 us: 1.01x slower                                              |
| xml_etree_process    | 53.9 ms                                                | 54.6 ms: 1.01x slower                                              |
| pickle               | 10.1 us                                                | 10.2 us: 1.01x slower                                              |
| xml_etree_generate   | 76.2 ms                                                | 78.6 ms: 1.03x slower                                              |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-iritkatriel-copy_consts-3.12.0a4+-f8449d5 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.56 ms: 1.00x slower                                              |
| python_startup_no_site | 6.01 ms                                                | 6.10 ms: 1.02x slower                                              |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-iritkatriel-copy_consts-3.12.0a4+-f8449d5 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 48.1 ms: 1.08x faster                                              |
| mako            | 10.1 ms                                                | 9.67 ms: 1.04x faster                                              |
| genshi_text     | 21.6 ms                                                | 20.8 ms: 1.04x faster                                              |
| django_template | 32.6 ms                                                | 33.8 ms: 1.04x slower                                              |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                       |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-iritkatriel-copy_consts-3.12.0a4+-f8449d5 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------:|
| asyncio_tcp             | 922 ms                                                 | 511 ms: 1.80x faster                                               |
| json_dumps              | 12.6 ms                                                | 9.65 ms: 1.30x faster                                              |
| regex_effbot            | 3.99 ms                                                | 3.41 ms: 1.17x faster                                              |
| unpickle_pure_python    | 228 us                                                 | 201 us: 1.13x faster                                               |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.03 ms: 1.12x faster                                              |
| json_loads              | 26.5 us                                                | 24.1 us: 1.10x faster                                              |
| scimark_sor             | 118 ms                                                 | 108 ms: 1.10x faster                                               |
| deltablue               | 3.67 ms                                                | 3.38 ms: 1.09x faster                                              |
| genshi_xml              | 51.8 ms                                                | 48.1 ms: 1.08x faster                                              |
| pycparser               | 1.18 sec                                               | 1.11 sec: 1.06x faster                                             |
| logging_silent          | 101 ns                                                 | 95.0 ns: 1.06x faster                                              |
| xml_etree_parse         | 158 ms                                                 | 150 ms: 1.06x faster                                               |
| fannkuch                | 388 ms                                                 | 367 ms: 1.06x faster                                               |
| deepcopy_memo           | 37.0 us                                                | 35.1 us: 1.06x faster                                              |
| json                    | 4.94 ms                                                | 4.70 ms: 1.05x faster                                              |
| float                   | 77.2 ms                                                | 73.5 ms: 1.05x faster                                              |
| html5lib                | 64.5 ms                                                | 61.5 ms: 1.05x faster                                              |
| pidigits                | 198 ms                                                 | 190 ms: 1.04x faster                                               |
| scimark_fft             | 328 ms                                                 | 314 ms: 1.04x faster                                               |
| telco                   | 6.58 ms                                                | 6.31 ms: 1.04x faster                                              |
| richards                | 45.7 ms                                                | 43.8 ms: 1.04x faster                                              |
| pickle_pure_python      | 306 us                                                 | 293 us: 1.04x faster                                               |
| regex_compile           | 138 ms                                                 | 132 ms: 1.04x faster                                               |
| mako                    | 10.1 ms                                                | 9.67 ms: 1.04x faster                                              |
| mdp                     | 2.62 sec                                               | 2.53 sec: 1.04x faster                                             |
| genshi_text             | 21.6 ms                                                | 20.8 ms: 1.04x faster                                              |
| unpack_sequence         | 43.1 ns                                                | 41.6 ns: 1.03x faster                                              |
| regex_v8                | 22.0 ms                                                | 21.3 ms: 1.03x faster                                              |
| hexiom                  | 6.37 ms                                                | 6.18 ms: 1.03x faster                                              |
| pyflate                 | 418 ms                                                 | 406 ms: 1.03x faster                                               |
| async_generators        | 368 ms                                                 | 358 ms: 1.03x faster                                               |
| bench_thread_pool       | 819 us                                                 | 797 us: 1.03x faster                                               |
| unpickle                | 13.7 us                                                | 13.3 us: 1.03x faster                                              |
| pprint_pformat          | 1.46 sec                                               | 1.42 sec: 1.03x faster                                             |
| meteor_contest          | 107 ms                                                 | 104 ms: 1.02x faster                                               |
| pickle_list             | 4.11 us                                                | 4.03 us: 1.02x faster                                              |
| nqueens                 | 83.4 ms                                                | 81.8 ms: 1.02x faster                                              |
| create_gc_cycles        | 1.49 ms                                                | 1.46 ms: 1.02x faster                                              |
| coverage                | 100 ms                                                 | 98.3 ms: 1.02x faster                                              |
| pickle_dict             | 31.1 us                                                | 30.6 us: 1.02x faster                                              |
| regex_dna               | 204 ms                                                 | 201 ms: 1.02x faster                                               |
| raytrace                | 297 ms                                                 | 293 ms: 1.01x faster                                               |
| sympy_expand            | 475 ms                                                 | 469 ms: 1.01x faster                                               |
| docutils                | 2.63 sec                                               | 2.59 sec: 1.01x faster                                             |
| sqlglot_optimize        | 53.1 ms                                                | 52.5 ms: 1.01x faster                                              |
| thrift                  | 756 us                                                 | 749 us: 1.01x faster                                               |
| spectral_norm           | 100 ms                                                 | 99.0 ms: 1.01x faster                                              |
| scimark_monte_carlo     | 68.1 ms                                                | 67.4 ms: 1.01x faster                                              |
| chaos                   | 69.2 ms                                                | 68.6 ms: 1.01x faster                                              |
| xml_etree_iterparse     | 104 ms                                                 | 103 ms: 1.01x faster                                               |
| go                      | 140 ms                                                 | 139 ms: 1.01x faster                                               |
| sympy_str               | 290 ms                                                 | 288 ms: 1.01x faster                                               |
| 2to3                    | 259 ms                                                 | 257 ms: 1.01x faster                                               |
| deepcopy                | 342 us                                                 | 341 us: 1.00x faster                                               |
| sympy_sum               | 167 ms                                                 | 167 ms: 1.00x slower                                               |
| sqlglot_normalize       | 108 ms                                                 | 108 ms: 1.00x slower                                               |
| python_startup          | 8.52 ms                                                | 8.56 ms: 1.00x slower                                              |
| chameleon               | 6.47 ms                                                | 6.53 ms: 1.01x slower                                              |
| unpickle_list           | 4.91 us                                                | 4.97 us: 1.01x slower                                              |
| scimark_lu              | 110 ms                                                 | 111 ms: 1.01x slower                                               |
| xml_etree_process       | 53.9 ms                                                | 54.6 ms: 1.01x slower                                              |
| pickle                  | 10.1 us                                                | 10.2 us: 1.01x slower                                              |
| python_startup_no_site  | 6.01 ms                                                | 6.10 ms: 1.02x slower                                              |
| sqlite_synth            | 2.52 us                                                | 2.56 us: 1.02x slower                                              |
| deepcopy_reduce         | 2.94 us                                                | 3.00 us: 1.02x slower                                              |
| async_tree_cpu_io_mixed | 739 ms                                                 | 757 ms: 1.02x slower                                               |
| sqlglot_transpile       | 1.70 ms                                                | 1.75 ms: 1.03x slower                                              |
| async_tree_io           | 1.30 sec                                               | 1.34 sec: 1.03x slower                                             |
| xml_etree_generate      | 76.2 ms                                                | 78.6 ms: 1.03x slower                                              |
| sqlglot_parse           | 1.40 ms                                                | 1.45 ms: 1.03x slower                                              |
| django_template         | 32.6 ms                                                | 33.8 ms: 1.04x slower                                              |
| sympy_integrate         | 21.0 ms                                                | 21.9 ms: 1.04x slower                                              |
| gc_traversal            | 4.02 ms                                                | 4.30 ms: 1.07x slower                                              |
| async_tree_memoization  | 627 ms                                                 | 674 ms: 1.07x slower                                               |
| generators              | 73.5 ms                                                | 79.0 ms: 1.07x slower                                              |
| dask                    | 360 ms                                                 | 516 ms: 1.43x slower                                               |
| Geometric mean          | (ref)                                                  | 1.02x faster                                                       |

Benchmark hidden because not significant (11): dulwich_log, logging_format, pprint_safe_repr, pathlib, bench_mp_pool, crypto_pyaes, nbody, logging_simple, coroutines, async_tree_none, djangocms
Ignored benchmarks (13) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, comprehensions, flaskblogging, gunicorn, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, tornado_http, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230118-3.12.0a4+-f8449d5/bm-20230118-linux-x86_64-iritkatriel-copy_consts-3.12.0a4+-f8449d5.json: mypy


# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x
