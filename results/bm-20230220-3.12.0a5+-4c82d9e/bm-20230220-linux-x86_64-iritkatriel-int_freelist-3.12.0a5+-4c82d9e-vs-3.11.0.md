
# Results vs. 3.11.0

- fork: iritkatriel
- ref: int_freelist
- machine: linux-x86_64
- commit hash: 4c82d9e
- commit date: 2023-02-20
- overall geometric mean: 1.04x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230220-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-4c82d9e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 251 ms: 1.03x faster                                                |
| chameleon      | 6.47 ms                                                | 6.25 ms: 1.04x faster                                               |
| docutils       | 2.63 sec                                               | 2.53 sec: 1.04x faster                                              |
| html5lib       | 64.5 ms                                                | 61.7 ms: 1.05x faster                                               |
| tornado_http   | 96.3 ms                                                | 93.8 ms: 1.03x faster                                               |
| Geometric mean | (ref)                                                  | 1.04x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230220-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-4c82d9e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 77.2 ms                                                | 72.2 ms: 1.07x faster                                               |
| pidigits       | 198 ms                                                 | 191 ms: 1.04x faster                                                |
| nbody          | 93.1 ms                                                | 94.6 ms: 1.02x slower                                               |
| Geometric mean | (ref)                                                  | 1.03x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230220-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-4c82d9e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.46 ms: 1.16x faster                                               |
| regex_compile  | 138 ms                                                 | 127 ms: 1.08x faster                                                |
| regex_v8       | 22.0 ms                                                | 21.2 ms: 1.04x faster                                               |
| regex_dna      | 204 ms                                                 | 199 ms: 1.03x faster                                                |
| Geometric mean | (ref)                                                  | 1.08x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230220-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-4c82d9e |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.44 ms: 1.33x faster                                               |
| unpickle_pure_python | 228 us                                                 | 197 us: 1.16x faster                                                |
| json_loads           | 26.5 us                                                | 23.8 us: 1.11x faster                                               |
| xml_etree_parse      | 158 ms                                                 | 148 ms: 1.07x faster                                                |
| pickle_pure_python   | 306 us                                                 | 290 us: 1.06x faster                                                |
| pickle_dict          | 31.1 us                                                | 29.7 us: 1.05x faster                                               |
| unpickle             | 13.7 us                                                | 13.2 us: 1.04x faster                                               |
| unpickle_list        | 4.91 us                                                | 4.80 us: 1.02x faster                                               |
| xml_etree_iterparse  | 104 ms                                                 | 102 ms: 1.02x faster                                                |
| pickle_list          | 4.11 us                                                | 4.08 us: 1.01x faster                                               |
| xml_etree_process    | 53.9 ms                                                | 57.2 ms: 1.06x slower                                               |
| xml_etree_generate   | 76.2 ms                                                | 82.2 ms: 1.08x slower                                               |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                        |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230220-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-4c82d9e |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.95 ms: 1.05x slower                                               |
| python_startup_no_site | 6.01 ms                                                | 6.50 ms: 1.08x slower                                               |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230220-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-4c82d9e |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 47.6 ms: 1.09x faster                                               |
| mako            | 10.1 ms                                                | 9.51 ms: 1.06x faster                                               |
| genshi_text     | 21.6 ms                                                | 20.7 ms: 1.04x faster                                               |
| django_template | 32.6 ms                                                | 32.9 ms: 1.01x slower                                               |
| Geometric mean  | (ref)                                                  | 1.04x faster                                                        |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230220-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-4c82d9e |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| asyncio_tcp             | 922 ms                                                 | 496 ms: 1.86x faster                                                |
| json_dumps              | 12.6 ms                                                | 9.44 ms: 1.33x faster                                               |
| mypy2                   | 420 ms                                                 | 331 ms: 1.27x faster                                                |
| unpickle_pure_python    | 228 us                                                 | 197 us: 1.16x faster                                                |
| regex_effbot            | 3.99 ms                                                | 3.46 ms: 1.16x faster                                               |
| deltablue               | 3.67 ms                                                | 3.20 ms: 1.15x faster                                               |
| scimark_sparse_mat_mult | 4.50 ms                                                | 3.96 ms: 1.13x faster                                               |
| scimark_sor             | 118 ms                                                 | 106 ms: 1.12x faster                                                |
| json_loads              | 26.5 us                                                | 23.8 us: 1.11x faster                                               |
| logging_silent          | 101 ns                                                 | 91.6 ns: 1.10x faster                                               |
| aiohttp                 | 1.10 ms                                                | 997 us: 1.10x faster                                                |
| gunicorn                | 1.18 ms                                                | 1.07 ms: 1.10x faster                                               |
| genshi_xml              | 51.8 ms                                                | 47.6 ms: 1.09x faster                                               |
| richards                | 45.7 ms                                                | 42.0 ms: 1.09x faster                                               |
| scimark_fft             | 328 ms                                                 | 303 ms: 1.08x faster                                                |
| regex_compile           | 138 ms                                                 | 127 ms: 1.08x faster                                                |
| sympy_str               | 290 ms                                                 | 270 ms: 1.08x faster                                                |
| pycparser               | 1.18 sec                                               | 1.10 sec: 1.07x faster                                              |
| xml_etree_parse         | 158 ms                                                 | 148 ms: 1.07x faster                                                |
| float                   | 77.2 ms                                                | 72.2 ms: 1.07x faster                                               |
| json                    | 4.94 ms                                                | 4.63 ms: 1.07x faster                                               |
| hexiom                  | 6.37 ms                                                | 5.98 ms: 1.07x faster                                               |
| nqueens                 | 83.4 ms                                                | 78.2 ms: 1.07x faster                                               |
| spectral_norm           | 100 ms                                                 | 93.8 ms: 1.07x faster                                               |
| deepcopy_memo           | 37.0 us                                                | 34.7 us: 1.07x faster                                               |
| logging_format          | 6.68 us                                                | 6.27 us: 1.07x faster                                               |
| chaos                   | 69.2 ms                                                | 65.0 ms: 1.06x faster                                               |
| mako                    | 10.1 ms                                                | 9.51 ms: 1.06x faster                                               |
| sympy_integrate         | 21.0 ms                                                | 19.8 ms: 1.06x faster                                               |
| pickle_pure_python      | 306 us                                                 | 290 us: 1.06x faster                                                |
| raytrace                | 297 ms                                                 | 281 ms: 1.06x faster                                                |
| sympy_sum               | 167 ms                                                 | 158 ms: 1.06x faster                                                |
| pyflate                 | 418 ms                                                 | 398 ms: 1.05x faster                                                |
| logging_simple          | 6.03 us                                                | 5.75 us: 1.05x faster                                               |
| fannkuch                | 388 ms                                                 | 370 ms: 1.05x faster                                                |
| pickle_dict             | 31.1 us                                                | 29.7 us: 1.05x faster                                               |
| pprint_pformat          | 1.46 sec                                               | 1.39 sec: 1.05x faster                                              |
| bench_thread_pool       | 819 us                                                 | 783 us: 1.05x faster                                                |
| html5lib                | 64.5 ms                                                | 61.7 ms: 1.05x faster                                               |
| scimark_monte_carlo     | 68.1 ms                                                | 65.3 ms: 1.04x faster                                               |
| genshi_text             | 21.6 ms                                                | 20.7 ms: 1.04x faster                                               |
| regex_v8                | 22.0 ms                                                | 21.2 ms: 1.04x faster                                               |
| pidigits                | 198 ms                                                 | 191 ms: 1.04x faster                                                |
| docutils                | 2.63 sec                                               | 2.53 sec: 1.04x faster                                              |
| unpickle                | 13.7 us                                                | 13.2 us: 1.04x faster                                               |
| mdp                     | 2.62 sec                                               | 2.52 sec: 1.04x faster                                              |
| sympy_expand            | 475 ms                                                 | 458 ms: 1.04x faster                                                |
| chameleon               | 6.47 ms                                                | 6.25 ms: 1.04x faster                                               |
| go                      | 140 ms                                                 | 136 ms: 1.03x faster                                                |
| telco                   | 6.58 ms                                                | 6.38 ms: 1.03x faster                                               |
| 2to3                    | 259 ms                                                 | 251 ms: 1.03x faster                                                |
| deepcopy                | 342 us                                                 | 332 us: 1.03x faster                                                |
| sqlglot_optimize        | 53.1 ms                                                | 51.7 ms: 1.03x faster                                               |
| dulwich_log             | 63.7 ms                                                | 62.0 ms: 1.03x faster                                               |
| tornado_http            | 96.3 ms                                                | 93.8 ms: 1.03x faster                                               |
| regex_dna               | 204 ms                                                 | 199 ms: 1.03x faster                                                |
| pprint_safe_repr        | 701 ms                                                 | 685 ms: 1.02x faster                                                |
| unpickle_list           | 4.91 us                                                | 4.80 us: 1.02x faster                                               |
| coverage                | 100 ms                                                 | 97.9 ms: 1.02x faster                                               |
| xml_etree_iterparse     | 104 ms                                                 | 102 ms: 1.02x faster                                                |
| pathlib                 | 18.2 ms                                                | 17.9 ms: 1.02x faster                                               |
| sqlalchemy_declarative  | 138 ms                                                 | 136 ms: 1.01x faster                                                |
| create_gc_cycles        | 1.49 ms                                                | 1.47 ms: 1.01x faster                                               |
| unpack_sequence         | 43.1 ns                                                | 42.5 ns: 1.01x faster                                               |
| meteor_contest          | 107 ms                                                 | 105 ms: 1.01x faster                                                |
| sqlglot_normalize       | 108 ms                                                 | 107 ms: 1.01x faster                                                |
| pickle_list             | 4.11 us                                                | 4.08 us: 1.01x faster                                               |
| coroutines              | 25.5 ms                                                | 25.7 ms: 1.01x slower                                               |
| sqlglot_parse           | 1.40 ms                                                | 1.41 ms: 1.01x slower                                               |
| async_tree_none         | 526 ms                                                 | 532 ms: 1.01x slower                                                |
| django_template         | 32.6 ms                                                | 32.9 ms: 1.01x slower                                               |
| scimark_lu              | 110 ms                                                 | 111 ms: 1.01x slower                                                |
| sqlite_synth            | 2.52 us                                                | 2.56 us: 1.01x slower                                               |
| async_tree_io           | 1.30 sec                                               | 1.32 sec: 1.01x slower                                              |
| nbody                   | 93.1 ms                                                | 94.6 ms: 1.02x slower                                               |
| crypto_pyaes            | 74.7 ms                                                | 76.4 ms: 1.02x slower                                               |
| async_tree_cpu_io_mixed | 739 ms                                                 | 759 ms: 1.03x slower                                                |
| python_startup          | 8.52 ms                                                | 8.95 ms: 1.05x slower                                               |
| generators              | 73.5 ms                                                | 77.3 ms: 1.05x slower                                               |
| async_tree_memoization  | 627 ms                                                 | 666 ms: 1.06x slower                                                |
| xml_etree_process       | 53.9 ms                                                | 57.2 ms: 1.06x slower                                               |
| gc_traversal            | 4.02 ms                                                | 4.29 ms: 1.07x slower                                               |
| xml_etree_generate      | 76.2 ms                                                | 82.2 ms: 1.08x slower                                               |
| python_startup_no_site  | 6.01 ms                                                | 6.50 ms: 1.08x slower                                               |
| async_generators        | 368 ms                                                 | 423 ms: 1.15x slower                                                |
| Geometric mean          | (ref)                                                  | 1.04x faster                                                        |

Benchmark hidden because not significant (7): djangocms, pickle, deepcopy_reduce, sqlalchemy_imperative, bench_mp_pool, thrift, sqlglot_transpile
Ignored benchmarks (8) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, comprehensions, dask, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x
