
# Results vs. 3.11.0

- fork: faster-cpython
- ref: nogil_latest
- machine: linux-x86_64
- commit hash: 1d39009
- commit date: 2023-04-16
- overall geometric mean: 1.05x slower \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230416-linux-x86_64-faster%2dcpython-nogil_latest-3.12.0a4-1d39009 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 290 ms: 1.12x slower                                                    |
| chameleon      | 6.47 ms                                                | 7.81 ms: 1.21x slower                                                   |
| docutils       | 2.63 sec                                               | 3.15 sec: 1.20x slower                                                  |
| html5lib       | 64.5 ms                                                | 69.2 ms: 1.07x slower                                                   |
| Geometric mean | (ref)                                                  | 1.15x slower                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230416-linux-x86_64-faster%2dcpython-nogil_latest-3.12.0a4-1d39009 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 77.2 ms                                                | 65.9 ms: 1.17x faster                                                   |
| pidigits       | 198 ms                                                 | 186 ms: 1.06x faster                                                    |
| nbody          | 93.1 ms                                                | 107 ms: 1.15x slower                                                    |
| Geometric mean | (ref)                                                  | 1.03x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230416-linux-x86_64-faster%2dcpython-nogil_latest-3.12.0a4-1d39009 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.46 ms: 1.15x faster                                                   |
| regex_v8       | 22.0 ms                                                | 21.1 ms: 1.05x faster                                                   |
| regex_dna      | 204 ms                                                 | 205 ms: 1.01x slower                                                    |
| regex_compile  | 138 ms                                                 | 152 ms: 1.10x slower                                                    |
| Geometric mean | (ref)                                                  | 1.02x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230416-linux-x86_64-faster%2dcpython-nogil_latest-3.12.0a4-1d39009 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 10.4 ms: 1.21x faster                                                   |
| xml_etree_parse      | 158 ms                                                 | 137 ms: 1.15x faster                                                    |
| pickle_dict          | 31.1 us                                                | 30.0 us: 1.04x faster                                                   |
| unpickle_pure_python | 228 us                                                 | 229 us: 1.00x slower                                                    |
| pickle               | 10.1 us                                                | 10.3 us: 1.02x slower                                                   |
| pickle_pure_python   | 306 us                                                 | 321 us: 1.05x slower                                                    |
| pickle_list          | 4.11 us                                                | 4.33 us: 1.05x slower                                                   |
| json_loads           | 26.5 us                                                | 28.0 us: 1.06x slower                                                   |
| unpickle_list        | 4.91 us                                                | 5.20 us: 1.06x slower                                                   |
| xml_etree_iterparse  | 104 ms                                                 | 114 ms: 1.09x slower                                                    |
| xml_etree_generate   | 76.2 ms                                                | 83.7 ms: 1.10x slower                                                   |
| unpickle             | 13.7 us                                                | 15.5 us: 1.13x slower                                                   |
| xml_etree_process    | 53.9 ms                                                | 61.3 ms: 1.14x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.02x slower                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230416-linux-x86_64-faster%2dcpython-nogil_latest-3.12.0a4-1d39009 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.18 ms: 1.08x slower                                                   |
| python_startup_no_site | 6.01 ms                                                | 6.59 ms: 1.10x slower                                                   |
| Geometric mean         | (ref)                                                  | 1.09x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230416-linux-x86_64-faster%2dcpython-nogil_latest-3.12.0a4-1d39009 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 52.0 ms: 1.00x slower                                                   |
| genshi_text     | 21.6 ms                                                | 24.4 ms: 1.13x slower                                                   |
| django_template | 32.6 ms                                                | 37.4 ms: 1.15x slower                                                   |
| mako            | 10.1 ms                                                | 13.2 ms: 1.31x slower                                                   |
| Geometric mean  | (ref)                                                  | 1.14x slower                                                            |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230416-linux-x86_64-faster%2dcpython-nogil_latest-3.12.0a4-1d39009 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io           | 1.30 sec                                               | 616 ms: 2.10x faster                                                    |
| asyncio_tcp             | 922 ms                                                 | 525 ms: 1.76x faster                                                    |
| async_tree_none         | 526 ms                                                 | 311 ms: 1.69x faster                                                    |
| async_tree_memoization  | 627 ms                                                 | 381 ms: 1.65x faster                                                    |
| async_tree_cpu_io_mixed | 739 ms                                                 | 534 ms: 1.38x faster                                                    |
| json_dumps              | 12.6 ms                                                | 10.4 ms: 1.21x faster                                                   |
| float                   | 77.2 ms                                                | 65.9 ms: 1.17x faster                                                   |
| regex_effbot            | 3.99 ms                                                | 3.46 ms: 1.15x faster                                                   |
| xml_etree_parse         | 158 ms                                                 | 137 ms: 1.15x faster                                                    |
| gc_traversal            | 4.02 ms                                                | 3.67 ms: 1.10x faster                                                   |
| pidigits                | 198 ms                                                 | 186 ms: 1.06x faster                                                    |
| regex_v8                | 22.0 ms                                                | 21.1 ms: 1.05x faster                                                   |
| pickle_dict             | 31.1 us                                                | 30.0 us: 1.04x faster                                                   |
| pycparser               | 1.18 sec                                               | 1.15 sec: 1.02x faster                                                  |
| bench_mp_pool           | 24.0 ms                                                | 23.8 ms: 1.01x faster                                                   |
| unpickle_pure_python    | 228 us                                                 | 229 us: 1.00x slower                                                    |
| genshi_xml              | 51.8 ms                                                | 52.0 ms: 1.00x slower                                                   |
| regex_dna               | 204 ms                                                 | 205 ms: 1.01x slower                                                    |
| pickle                  | 10.1 us                                                | 10.3 us: 1.02x slower                                                   |
| json                    | 4.94 ms                                                | 5.06 ms: 1.02x slower                                                   |
| async_generators        | 368 ms                                                 | 377 ms: 1.02x slower                                                    |
| logging_silent          | 101 ns                                                 | 104 ns: 1.03x slower                                                    |
| nqueens                 | 83.4 ms                                                | 85.8 ms: 1.03x slower                                                   |
| scimark_sor             | 118 ms                                                 | 123 ms: 1.04x slower                                                    |
| sqlite_synth            | 2.52 us                                                | 2.62 us: 1.04x slower                                                   |
| go                      | 140 ms                                                 | 146 ms: 1.05x slower                                                    |
| pickle_pure_python      | 306 us                                                 | 321 us: 1.05x slower                                                    |
| coroutines              | 25.5 ms                                                | 26.8 ms: 1.05x slower                                                   |
| telco                   | 6.58 ms                                                | 6.92 ms: 1.05x slower                                                   |
| pickle_list             | 4.11 us                                                | 4.33 us: 1.05x slower                                                   |
| richards                | 45.7 ms                                                | 48.4 ms: 1.06x slower                                                   |
| json_loads              | 26.5 us                                                | 28.0 us: 1.06x slower                                                   |
| unpickle_list           | 4.91 us                                                | 5.20 us: 1.06x slower                                                   |
| sqlglot_normalize       | 108 ms                                                 | 115 ms: 1.06x slower                                                    |
| mdp                     | 2.62 sec                                               | 2.79 sec: 1.06x slower                                                  |
| deltablue               | 3.67 ms                                                | 3.91 ms: 1.07x slower                                                   |
| dulwich_log             | 63.7 ms                                                | 68.1 ms: 1.07x slower                                                   |
| create_gc_cycles        | 1.49 ms                                                | 1.59 ms: 1.07x slower                                                   |
| html5lib                | 64.5 ms                                                | 69.2 ms: 1.07x slower                                                   |
| generators              | 73.5 ms                                                | 78.8 ms: 1.07x slower                                                   |
| sqlglot_optimize        | 53.1 ms                                                | 57.1 ms: 1.08x slower                                                   |
| python_startup          | 8.52 ms                                                | 9.18 ms: 1.08x slower                                                   |
| chaos                   | 69.2 ms                                                | 74.6 ms: 1.08x slower                                                   |
| hexiom                  | 6.37 ms                                                | 6.89 ms: 1.08x slower                                                   |
| deepcopy_memo           | 37.0 us                                                | 40.1 us: 1.08x slower                                                   |
| pprint_pformat          | 1.46 sec                                               | 1.58 sec: 1.09x slower                                                  |
| mypy2                   | 420 ms                                                 | 457 ms: 1.09x slower                                                    |
| sympy_integrate         | 21.0 ms                                                | 22.8 ms: 1.09x slower                                                   |
| pprint_safe_repr        | 701 ms                                                 | 765 ms: 1.09x slower                                                    |
| coverage                | 100 ms                                                 | 109 ms: 1.09x slower                                                    |
| xml_etree_iterparse     | 104 ms                                                 | 114 ms: 1.09x slower                                                    |
| crypto_pyaes            | 74.7 ms                                                | 81.8 ms: 1.10x slower                                                   |
| python_startup_no_site  | 6.01 ms                                                | 6.59 ms: 1.10x slower                                                   |
| deepcopy                | 342 us                                                 | 375 us: 1.10x slower                                                    |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.94 ms: 1.10x slower                                                   |
| xml_etree_generate      | 76.2 ms                                                | 83.7 ms: 1.10x slower                                                   |
| regex_compile           | 138 ms                                                 | 152 ms: 1.10x slower                                                    |
| 2to3                    | 259 ms                                                 | 290 ms: 1.12x slower                                                    |
| spectral_norm           | 100 ms                                                 | 112 ms: 1.12x slower                                                    |
| scimark_monte_carlo     | 68.1 ms                                                | 76.4 ms: 1.12x slower                                                   |
| pyflate                 | 418 ms                                                 | 470 ms: 1.12x slower                                                    |
| fannkuch                | 388 ms                                                 | 436 ms: 1.12x slower                                                    |
| thrift                  | 756 us                                                 | 851 us: 1.13x slower                                                    |
| genshi_text             | 21.6 ms                                                | 24.4 ms: 1.13x slower                                                   |
| sympy_expand            | 475 ms                                                 | 537 ms: 1.13x slower                                                    |
| unpickle                | 13.7 us                                                | 15.5 us: 1.13x slower                                                   |
| sympy_str               | 290 ms                                                 | 329 ms: 1.13x slower                                                    |
| xml_etree_process       | 53.9 ms                                                | 61.3 ms: 1.14x slower                                                   |
| django_template         | 32.6 ms                                                | 37.4 ms: 1.15x slower                                                   |
| logging_format          | 6.68 us                                                | 7.66 us: 1.15x slower                                                   |
| nbody                   | 93.1 ms                                                | 107 ms: 1.15x slower                                                    |
| sympy_sum               | 167 ms                                                 | 192 ms: 1.15x slower                                                    |
| logging_simple          | 6.03 us                                                | 7.00 us: 1.16x slower                                                   |
| deepcopy_reduce         | 2.94 us                                                | 3.42 us: 1.16x slower                                                   |
| raytrace                | 297 ms                                                 | 346 ms: 1.16x slower                                                    |
| scimark_lu              | 110 ms                                                 | 128 ms: 1.17x slower                                                    |
| scimark_fft             | 328 ms                                                 | 383 ms: 1.17x slower                                                    |
| meteor_contest          | 107 ms                                                 | 124 ms: 1.17x slower                                                    |
| djangocms               | 32.4 us                                                | 37.9 us: 1.17x slower                                                   |
| comprehensions          | 22.4 us                                                | 26.3 us: 1.17x slower                                                   |
| docutils                | 2.63 sec                                               | 3.15 sec: 1.20x slower                                                  |
| chameleon               | 6.47 ms                                                | 7.81 ms: 1.21x slower                                                   |
| sqlglot_transpile       | 1.70 ms                                                | 2.10 ms: 1.23x slower                                                   |
| sqlglot_parse           | 1.40 ms                                                | 1.79 ms: 1.28x slower                                                   |
| mako                    | 10.1 ms                                                | 13.2 ms: 1.31x slower                                                   |
| unpack_sequence         | 43.1 ns                                                | 58.1 ns: 1.35x slower                                                   |
| bench_thread_pool       | 819 us                                                 | 1.64 ms: 2.01x slower                                                   |
| Geometric mean          | (ref)                                                  | 1.05x slower                                                            |

Benchmark hidden because not significant (1): pathlib
Ignored benchmarks (12) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, dask, flaskblogging, gunicorn, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, tornado_http, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.06x
- 99% likely to have a slowdown of 1.05x
