
# Results vs. 3.11.0

- fork: brandtbucher
- ref: add_small_int_new
- machine: linux-x86_64
- commit hash: eb1608b
- commit date: 2023-03-21
- overall geometric mean: 1.05x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230321-linux-x86_64-brandtbucher-add_small_int_new-3.12.0a6+-eb1608b |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 250 ms: 1.04x faster                                                      |
| chameleon      | 6.47 ms                                                | 6.23 ms: 1.04x faster                                                     |
| docutils       | 2.63 sec                                               | 2.53 sec: 1.04x faster                                                    |
| html5lib       | 64.5 ms                                                | 60.2 ms: 1.07x faster                                                     |
| tornado_http   | 96.3 ms                                                | 91.0 ms: 1.06x faster                                                     |
| Geometric mean | (ref)                                                  | 1.05x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230321-linux-x86_64-brandtbucher-add_small_int_new-3.12.0a6+-eb1608b |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 93.1 ms                                                | 85.9 ms: 1.08x faster                                                     |
| float          | 77.2 ms                                                | 73.9 ms: 1.05x faster                                                     |
| pidigits       | 198 ms                                                 | 193 ms: 1.03x faster                                                      |
| Geometric mean | (ref)                                                  | 1.05x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230321-linux-x86_64-brandtbucher-add_small_int_new-3.12.0a6+-eb1608b |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.38 ms: 1.18x faster                                                     |
| regex_compile  | 138 ms                                                 | 133 ms: 1.04x faster                                                      |
| regex_v8       | 22.0 ms                                                | 21.6 ms: 1.02x faster                                                     |
| regex_dna      | 204 ms                                                 | 205 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                  | 1.06x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230321-linux-x86_64-brandtbucher-add_small_int_new-3.12.0a6+-eb1608b |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.54 ms: 1.32x faster                                                     |
| unpickle_pure_python | 228 us                                                 | 197 us: 1.16x faster                                                      |
| json_loads           | 26.5 us                                                | 24.3 us: 1.09x faster                                                     |
| pickle_pure_python   | 306 us                                                 | 284 us: 1.08x faster                                                      |
| xml_etree_parse      | 158 ms                                                 | 147 ms: 1.08x faster                                                      |
| xml_etree_iterparse  | 104 ms                                                 | 98.7 ms: 1.05x faster                                                     |
| unpickle_list        | 4.91 us                                                | 4.96 us: 1.01x slower                                                     |
| pickle_dict          | 31.1 us                                                | 31.6 us: 1.01x slower                                                     |
| xml_etree_process    | 53.9 ms                                                | 55.3 ms: 1.03x slower                                                     |
| pickle               | 10.1 us                                                | 10.5 us: 1.04x slower                                                     |
| xml_etree_generate   | 76.2 ms                                                | 79.8 ms: 1.05x slower                                                     |
| pickle_list          | 4.11 us                                                | 4.32 us: 1.05x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                              |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230321-linux-x86_64-brandtbucher-add_small_int_new-3.12.0a6+-eb1608b |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.90 ms: 1.04x slower                                                     |
| python_startup_no_site | 6.01 ms                                                | 6.51 ms: 1.08x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230321-linux-x86_64-brandtbucher-add_small_int_new-3.12.0a6+-eb1608b |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 48.3 ms: 1.07x faster                                                     |
| genshi_text     | 21.6 ms                                                | 21.2 ms: 1.01x faster                                                     |
| mako            | 10.1 ms                                                | 10.0 ms: 1.01x faster                                                     |
| django_template | 32.6 ms                                                | 32.5 ms: 1.00x faster                                                     |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                              |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230321-linux-x86_64-brandtbucher-add_small_int_new-3.12.0a6+-eb1608b |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 29.8 ms: 2.47x faster                                                     |
| asyncio_tcp             | 922 ms                                                 | 508 ms: 1.81x faster                                                      |
| json_dumps              | 12.6 ms                                                | 9.54 ms: 1.32x faster                                                     |
| mypy2                   | 420 ms                                                 | 333 ms: 1.26x faster                                                      |
| regex_effbot            | 3.99 ms                                                | 3.38 ms: 1.18x faster                                                     |
| deltablue               | 3.67 ms                                                | 3.15 ms: 1.16x faster                                                     |
| unpickle_pure_python    | 228 us                                                 | 197 us: 1.16x faster                                                      |
| coroutines              | 25.5 ms                                                | 22.3 ms: 1.14x faster                                                     |
| scimark_sor             | 118 ms                                                 | 106 ms: 1.11x faster                                                      |
| richards                | 45.7 ms                                                | 41.7 ms: 1.10x faster                                                     |
| aiohttp                 | 1.10 ms                                                | 1.01 ms: 1.09x faster                                                     |
| json_loads              | 26.5 us                                                | 24.3 us: 1.09x faster                                                     |
| logging_silent          | 101 ns                                                 | 92.8 ns: 1.09x faster                                                     |
| deepcopy_memo           | 37.0 us                                                | 34.1 us: 1.09x faster                                                     |
| nbody                   | 93.1 ms                                                | 85.9 ms: 1.08x faster                                                     |
| gunicorn                | 1.18 ms                                                | 1.09 ms: 1.08x faster                                                     |
| mdp                     | 2.62 sec                                               | 2.43 sec: 1.08x faster                                                    |
| logging_format          | 6.68 us                                                | 6.20 us: 1.08x faster                                                     |
| pickle_pure_python      | 306 us                                                 | 284 us: 1.08x faster                                                      |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.18 ms: 1.08x faster                                                     |
| xml_etree_parse         | 158 ms                                                 | 147 ms: 1.08x faster                                                      |
| go                      | 140 ms                                                 | 130 ms: 1.07x faster                                                      |
| json                    | 4.94 ms                                                | 4.61 ms: 1.07x faster                                                     |
| html5lib                | 64.5 ms                                                | 60.2 ms: 1.07x faster                                                     |
| genshi_xml              | 51.8 ms                                                | 48.3 ms: 1.07x faster                                                     |
| logging_simple          | 6.03 us                                                | 5.64 us: 1.07x faster                                                     |
| scimark_fft             | 328 ms                                                 | 308 ms: 1.07x faster                                                      |
| coverage                | 100 ms                                                 | 94.0 ms: 1.06x faster                                                     |
| raytrace                | 297 ms                                                 | 279 ms: 1.06x faster                                                      |
| fannkuch                | 388 ms                                                 | 365 ms: 1.06x faster                                                      |
| deepcopy                | 342 us                                                 | 323 us: 1.06x faster                                                      |
| tornado_http            | 96.3 ms                                                | 91.0 ms: 1.06x faster                                                     |
| hexiom                  | 6.37 ms                                                | 6.04 ms: 1.05x faster                                                     |
| chaos                   | 69.2 ms                                                | 65.7 ms: 1.05x faster                                                     |
| xml_etree_iterparse     | 104 ms                                                 | 98.7 ms: 1.05x faster                                                     |
| nqueens                 | 83.4 ms                                                | 79.4 ms: 1.05x faster                                                     |
| spectral_norm           | 100 ms                                                 | 95.6 ms: 1.05x faster                                                     |
| float                   | 77.2 ms                                                | 73.9 ms: 1.05x faster                                                     |
| scimark_monte_carlo     | 68.1 ms                                                | 65.2 ms: 1.04x faster                                                     |
| pprint_pformat          | 1.46 sec                                               | 1.40 sec: 1.04x faster                                                    |
| sqlglot_optimize        | 53.1 ms                                                | 51.0 ms: 1.04x faster                                                     |
| bench_thread_pool       | 819 us                                                 | 788 us: 1.04x faster                                                      |
| chameleon               | 6.47 ms                                                | 6.23 ms: 1.04x faster                                                     |
| regex_compile           | 138 ms                                                 | 133 ms: 1.04x faster                                                      |
| docutils                | 2.63 sec                                               | 2.53 sec: 1.04x faster                                                    |
| sqlglot_normalize       | 108 ms                                                 | 104 ms: 1.04x faster                                                      |
| 2to3                    | 259 ms                                                 | 250 ms: 1.04x faster                                                      |
| pathlib                 | 18.2 ms                                                | 17.6 ms: 1.03x faster                                                     |
| pycparser               | 1.18 sec                                               | 1.15 sec: 1.03x faster                                                    |
| meteor_contest          | 107 ms                                                 | 104 ms: 1.03x faster                                                      |
| pidigits                | 198 ms                                                 | 193 ms: 1.03x faster                                                      |
| sympy_integrate         | 21.0 ms                                                | 20.4 ms: 1.03x faster                                                     |
| telco                   | 6.58 ms                                                | 6.42 ms: 1.02x faster                                                     |
| sympy_str               | 290 ms                                                 | 284 ms: 1.02x faster                                                      |
| sympy_expand            | 475 ms                                                 | 465 ms: 1.02x faster                                                      |
| regex_v8                | 22.0 ms                                                | 21.6 ms: 1.02x faster                                                     |
| pyflate                 | 418 ms                                                 | 410 ms: 1.02x faster                                                      |
| pprint_safe_repr        | 701 ms                                                 | 689 ms: 1.02x faster                                                      |
| sqlalchemy_declarative  | 138 ms                                                 | 136 ms: 1.02x faster                                                      |
| genshi_text             | 21.6 ms                                                | 21.2 ms: 1.01x faster                                                     |
| deepcopy_reduce         | 2.94 us                                                | 2.90 us: 1.01x faster                                                     |
| gc_traversal            | 4.02 ms                                                | 3.98 ms: 1.01x faster                                                     |
| async_tree_none         | 526 ms                                                 | 521 ms: 1.01x faster                                                      |
| sqlalchemy_imperative   | 17.9 ms                                                | 17.7 ms: 1.01x faster                                                     |
| async_tree_io           | 1.30 sec                                               | 1.28 sec: 1.01x faster                                                    |
| sympy_sum               | 167 ms                                                 | 165 ms: 1.01x faster                                                      |
| mako                    | 10.1 ms                                                | 10.0 ms: 1.01x faster                                                     |
| django_template         | 32.6 ms                                                | 32.5 ms: 1.00x faster                                                     |
| create_gc_cycles        | 1.49 ms                                                | 1.49 ms: 1.00x slower                                                     |
| regex_dna               | 204 ms                                                 | 205 ms: 1.01x slower                                                      |
| unpickle_list           | 4.91 us                                                | 4.96 us: 1.01x slower                                                     |
| unpack_sequence         | 43.1 ns                                                | 43.5 ns: 1.01x slower                                                     |
| sqlglot_transpile       | 1.70 ms                                                | 1.72 ms: 1.01x slower                                                     |
| pickle_dict             | 31.1 us                                                | 31.6 us: 1.01x slower                                                     |
| thrift                  | 756 us                                                 | 773 us: 1.02x slower                                                      |
| sqlglot_parse           | 1.40 ms                                                | 1.43 ms: 1.02x slower                                                     |
| xml_etree_process       | 53.9 ms                                                | 55.3 ms: 1.03x slower                                                     |
| comprehensions          | 22.4 us                                                | 23.3 us: 1.04x slower                                                     |
| pickle                  | 10.1 us                                                | 10.5 us: 1.04x slower                                                     |
| sqlite_synth            | 2.52 us                                                | 2.62 us: 1.04x slower                                                     |
| python_startup          | 8.52 ms                                                | 8.90 ms: 1.04x slower                                                     |
| xml_etree_generate      | 76.2 ms                                                | 79.8 ms: 1.05x slower                                                     |
| pickle_list             | 4.11 us                                                | 4.32 us: 1.05x slower                                                     |
| python_startup_no_site  | 6.01 ms                                                | 6.51 ms: 1.08x slower                                                     |
| async_generators        | 368 ms                                                 | 416 ms: 1.13x slower                                                      |
| dask                    | 360 ms                                                 | 502 ms: 1.40x slower                                                      |
| Geometric mean          | (ref)                                                  | 1.05x faster                                                              |

Benchmark hidden because not significant (8): unpickle, djangocms, dulwich_log, bench_mp_pool, async_tree_memoization, crypto_pyaes, async_tree_cpu_io_mixed, scimark_lu
Ignored benchmarks (6) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x
