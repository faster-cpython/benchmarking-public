
# Results vs. 3.11.0

- fork: brandtbucher
- ref: scan_small_dicts
- machine: linux-x86_64
- commit hash: 79daf93
- commit date: 2022-12-22
- overall geometric mean: 1.04x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-79daf93 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 253 ms: 1.02x faster                                                     |
| chameleon      | 6.47 ms                                                | 6.54 ms: 1.01x slower                                                    |
| docutils       | 2.63 sec                                               | 2.55 sec: 1.03x faster                                                   |
| html5lib       | 64.5 ms                                                | 59.8 ms: 1.08x faster                                                    |
| Geometric mean | (ref)                                                  | 1.03x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-79daf93 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 77.2 ms                                                | 73.2 ms: 1.06x faster                                                    |
| pidigits       | 198 ms                                                 | 193 ms: 1.03x faster                                                     |
| nbody          | 93.1 ms                                                | 94.7 ms: 1.02x slower                                                    |
| Geometric mean | (ref)                                                  | 1.02x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-79daf93 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.43 ms: 1.16x faster                                                    |
| regex_compile  | 138 ms                                                 | 131 ms: 1.06x faster                                                     |
| regex_v8       | 22.0 ms                                                | 21.9 ms: 1.01x faster                                                    |
| regex_dna      | 204 ms                                                 | 204 ms: 1.00x faster                                                     |
| Geometric mean | (ref)                                                  | 1.05x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-79daf93 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.32 ms: 1.35x faster                                                    |
| unpickle_pure_python | 228 us                                                 | 198 us: 1.15x faster                                                     |
| pickle_pure_python   | 306 us                                                 | 278 us: 1.10x faster                                                     |
| json_loads           | 26.5 us                                                | 24.1 us: 1.10x faster                                                    |
| xml_etree_parse      | 158 ms                                                 | 148 ms: 1.07x faster                                                     |
| unpickle             | 13.7 us                                                | 13.2 us: 1.04x faster                                                    |
| pickle_dict          | 31.1 us                                                | 31.2 us: 1.00x slower                                                    |
| unpickle_list        | 4.91 us                                                | 5.01 us: 1.02x slower                                                    |
| xml_etree_generate   | 76.2 ms                                                | 78.1 ms: 1.02x slower                                                    |
| xml_etree_iterparse  | 104 ms                                                 | 107 ms: 1.03x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                             |

Benchmark hidden because not significant (3): pickle_list, xml_etree_process, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-79daf93 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.56 ms: 1.00x slower                                                    |
| python_startup_no_site | 6.01 ms                                                | 6.12 ms: 1.02x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-79daf93 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 47.4 ms: 1.09x faster                                                    |
| mako            | 10.1 ms                                                | 9.51 ms: 1.06x faster                                                    |
| genshi_text     | 21.6 ms                                                | 20.5 ms: 1.05x faster                                                    |
| django_template | 32.6 ms                                                | 32.5 ms: 1.00x faster                                                    |
| Geometric mean  | (ref)                                                  | 1.05x faster                                                             |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-79daf93 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| json_dumps              | 12.6 ms                                                | 9.32 ms: 1.35x faster                                                    |
| regex_effbot            | 3.99 ms                                                | 3.43 ms: 1.16x faster                                                    |
| unpickle_pure_python    | 228 us                                                 | 198 us: 1.15x faster                                                     |
| deltablue               | 3.67 ms                                                | 3.24 ms: 1.13x faster                                                    |
| deepcopy_memo           | 37.0 us                                                | 32.9 us: 1.12x faster                                                    |
| logging_silent          | 101 ns                                                 | 91.2 ns: 1.11x faster                                                    |
| scimark_sor             | 118 ms                                                 | 107 ms: 1.11x faster                                                     |
| pickle_pure_python      | 306 us                                                 | 278 us: 1.10x faster                                                     |
| json_loads              | 26.5 us                                                | 24.1 us: 1.10x faster                                                    |
| genshi_xml              | 51.8 ms                                                | 47.4 ms: 1.09x faster                                                    |
| richards                | 45.7 ms                                                | 41.9 ms: 1.09x faster                                                    |
| html5lib                | 64.5 ms                                                | 59.8 ms: 1.08x faster                                                    |
| logging_format          | 6.68 us                                                | 6.22 us: 1.07x faster                                                    |
| logging_simple          | 6.03 us                                                | 5.63 us: 1.07x faster                                                    |
| pycparser               | 1.18 sec                                               | 1.10 sec: 1.07x faster                                                   |
| xml_etree_parse         | 158 ms                                                 | 148 ms: 1.07x faster                                                     |
| pprint_pformat          | 1.46 sec                                               | 1.37 sec: 1.06x faster                                                   |
| nqueens                 | 83.4 ms                                                | 78.4 ms: 1.06x faster                                                    |
| deepcopy                | 342 us                                                 | 322 us: 1.06x faster                                                     |
| go                      | 140 ms                                                 | 132 ms: 1.06x faster                                                     |
| raytrace                | 297 ms                                                 | 279 ms: 1.06x faster                                                     |
| mako                    | 10.1 ms                                                | 9.51 ms: 1.06x faster                                                    |
| fannkuch                | 388 ms                                                 | 366 ms: 1.06x faster                                                     |
| async_generators        | 368 ms                                                 | 349 ms: 1.06x faster                                                     |
| regex_compile           | 138 ms                                                 | 131 ms: 1.06x faster                                                     |
| float                   | 77.2 ms                                                | 73.2 ms: 1.06x faster                                                    |
| pyflate                 | 418 ms                                                 | 397 ms: 1.05x faster                                                     |
| telco                   | 6.58 ms                                                | 6.24 ms: 1.05x faster                                                    |
| pprint_safe_repr        | 701 ms                                                 | 666 ms: 1.05x faster                                                     |
| bench_thread_pool       | 819 us                                                 | 778 us: 1.05x faster                                                     |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.27 ms: 1.05x faster                                                    |
| sqlglot_optimize        | 53.1 ms                                                | 50.6 ms: 1.05x faster                                                    |
| genshi_text             | 21.6 ms                                                | 20.5 ms: 1.05x faster                                                    |
| sympy_expand            | 475 ms                                                 | 453 ms: 1.05x faster                                                     |
| hexiom                  | 6.37 ms                                                | 6.10 ms: 1.04x faster                                                    |
| spectral_norm           | 100 ms                                                 | 95.8 ms: 1.04x faster                                                    |
| chaos                   | 69.2 ms                                                | 66.4 ms: 1.04x faster                                                    |
| scimark_fft             | 328 ms                                                 | 316 ms: 1.04x faster                                                     |
| unpickle                | 13.7 us                                                | 13.2 us: 1.04x faster                                                    |
| sqlglot_normalize       | 108 ms                                                 | 104 ms: 1.04x faster                                                     |
| scimark_monte_carlo     | 68.1 ms                                                | 65.9 ms: 1.03x faster                                                    |
| docutils                | 2.63 sec                                               | 2.55 sec: 1.03x faster                                                   |
| coroutines              | 25.5 ms                                                | 24.8 ms: 1.03x faster                                                    |
| scimark_lu              | 110 ms                                                 | 107 ms: 1.03x faster                                                     |
| pidigits                | 198 ms                                                 | 193 ms: 1.03x faster                                                     |
| pathlib                 | 18.2 ms                                                | 17.7 ms: 1.03x faster                                                    |
| coverage                | 100 ms                                                 | 97.5 ms: 1.03x faster                                                    |
| sympy_integrate         | 21.0 ms                                                | 20.5 ms: 1.03x faster                                                    |
| 2to3                    | 259 ms                                                 | 253 ms: 1.02x faster                                                     |
| sympy_str               | 290 ms                                                 | 283 ms: 1.02x faster                                                     |
| unpack_sequence         | 43.1 ns                                                | 42.1 ns: 1.02x faster                                                    |
| dulwich_log             | 63.7 ms                                                | 62.5 ms: 1.02x faster                                                    |
| sympy_sum               | 167 ms                                                 | 164 ms: 1.02x faster                                                     |
| deepcopy_reduce         | 2.94 us                                                | 2.89 us: 1.02x faster                                                    |
| thrift                  | 756 us                                                 | 750 us: 1.01x faster                                                     |
| regex_v8                | 22.0 ms                                                | 21.9 ms: 1.01x faster                                                    |
| django_template         | 32.6 ms                                                | 32.5 ms: 1.00x faster                                                    |
| regex_dna               | 204 ms                                                 | 204 ms: 1.00x faster                                                     |
| pickle_dict             | 31.1 us                                                | 31.2 us: 1.00x slower                                                    |
| python_startup          | 8.52 ms                                                | 8.56 ms: 1.00x slower                                                    |
| chameleon               | 6.47 ms                                                | 6.54 ms: 1.01x slower                                                    |
| sqlglot_parse           | 1.40 ms                                                | 1.42 ms: 1.01x slower                                                    |
| nbody                   | 93.1 ms                                                | 94.7 ms: 1.02x slower                                                    |
| crypto_pyaes            | 74.7 ms                                                | 75.9 ms: 1.02x slower                                                    |
| generators              | 73.5 ms                                                | 74.8 ms: 1.02x slower                                                    |
| json                    | 4.94 ms                                                | 5.03 ms: 1.02x slower                                                    |
| python_startup_no_site  | 6.01 ms                                                | 6.12 ms: 1.02x slower                                                    |
| async_tree_none         | 526 ms                                                 | 537 ms: 1.02x slower                                                     |
| unpickle_list           | 4.91 us                                                | 5.01 us: 1.02x slower                                                    |
| xml_etree_generate      | 76.2 ms                                                | 78.1 ms: 1.02x slower                                                    |
| sqlite_synth            | 2.52 us                                                | 2.58 us: 1.03x slower                                                    |
| xml_etree_iterparse     | 104 ms                                                 | 107 ms: 1.03x slower                                                     |
| async_tree_io           | 1.30 sec                                               | 1.34 sec: 1.03x slower                                                   |
| async_tree_memoization  | 627 ms                                                 | 651 ms: 1.04x slower                                                     |
| mdp                     | 2.62 sec                                               | 2.71 sec: 1.04x slower                                                   |
| async_tree_cpu_io_mixed | 739 ms                                                 | 768 ms: 1.04x slower                                                     |
| Geometric mean          | (ref)                                                  | 1.04x faster                                                             |

Benchmark hidden because not significant (7): pickle_list, bench_mp_pool, xml_etree_process, sqlglot_transpile, pickle, meteor_contest, djangocms
Ignored benchmarks (17) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, comprehensions, create_gc_cycles, dask, flaskblogging, gc_traversal, gunicorn, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, tornado_http, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20221222-3.12.0a3+-79daf93/bm-20221222-linux-x86_64-brandtbucher-scan_small_dicts-3.12.0a3+-79daf93.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x
