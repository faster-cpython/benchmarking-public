
# Results vs. 3.11.0

- fork: iritkatriel
- ref: int_freelist
- machine: linux-x86_64
- commit hash: 1134727
- commit date: 2023-02-08
- overall geometric mean: 1.04x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230208-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-1134727 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 252 ms: 1.03x faster                                                |
| chameleon      | 6.47 ms                                                | 6.30 ms: 1.03x faster                                               |
| docutils       | 2.63 sec                                               | 2.53 sec: 1.04x faster                                              |
| html5lib       | 64.5 ms                                                | 61.0 ms: 1.06x faster                                               |
| tornado_http   | 96.3 ms                                                | 94.2 ms: 1.02x faster                                               |
| Geometric mean | (ref)                                                  | 1.03x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230208-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-1134727 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 77.2 ms                                                | 71.4 ms: 1.08x faster                                               |
| nbody          | 93.1 ms                                                | 95.0 ms: 1.02x slower                                               |
| pidigits       | 198 ms                                                 | 203 ms: 1.02x slower                                                |
| Geometric mean | (ref)                                                  | 1.01x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230208-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-1134727 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.46 ms: 1.16x faster                                               |
| regex_compile  | 138 ms                                                 | 129 ms: 1.07x faster                                                |
| regex_v8       | 22.0 ms                                                | 21.7 ms: 1.02x faster                                               |
| regex_dna      | 204 ms                                                 | 212 ms: 1.04x slower                                                |
| Geometric mean | (ref)                                                  | 1.05x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230208-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-1134727 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.60 ms: 1.31x faster                                               |
| unpickle_pure_python | 228 us                                                 | 197 us: 1.16x faster                                                |
| json_loads           | 26.5 us                                                | 24.1 us: 1.10x faster                                               |
| xml_etree_parse      | 158 ms                                                 | 148 ms: 1.07x faster                                                |
| pickle_pure_python   | 306 us                                                 | 288 us: 1.06x faster                                                |
| unpickle             | 13.7 us                                                | 13.2 us: 1.04x faster                                               |
| xml_etree_iterparse  | 104 ms                                                 | 102 ms: 1.02x faster                                                |
| pickle               | 10.1 us                                                | 10.2 us: 1.01x slower                                               |
| xml_etree_process    | 53.9 ms                                                | 55.1 ms: 1.02x slower                                               |
| pickle_list          | 4.11 us                                                | 4.22 us: 1.03x slower                                               |
| pickle_dict          | 31.1 us                                                | 32.0 us: 1.03x slower                                               |
| xml_etree_generate   | 76.2 ms                                                | 80.4 ms: 1.05x slower                                               |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                        |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230208-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-1134727 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.92 ms: 1.05x slower                                               |
| python_startup_no_site | 6.01 ms                                                | 6.48 ms: 1.08x slower                                               |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230208-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-1134727 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 47.1 ms: 1.10x faster                                               |
| mako            | 10.1 ms                                                | 9.62 ms: 1.05x faster                                               |
| genshi_text     | 21.6 ms                                                | 20.6 ms: 1.04x faster                                               |
| django_template | 32.6 ms                                                | 32.9 ms: 1.01x slower                                               |
| Geometric mean  | (ref)                                                  | 1.05x faster                                                        |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230208-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-1134727 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| asyncio_tcp             | 922 ms                                                 | 492 ms: 1.87x faster                                                |
| json_dumps              | 12.6 ms                                                | 9.60 ms: 1.31x faster                                               |
| mypy2                   | 420 ms                                                 | 330 ms: 1.27x faster                                                |
| scimark_sparse_mat_mult | 4.50 ms                                                | 3.81 ms: 1.18x faster                                               |
| unpickle_pure_python    | 228 us                                                 | 197 us: 1.16x faster                                                |
| regex_effbot            | 3.99 ms                                                | 3.46 ms: 1.16x faster                                               |
| deltablue               | 3.67 ms                                                | 3.21 ms: 1.14x faster                                               |
| gc_traversal            | 4.02 ms                                                | 3.52 ms: 1.14x faster                                               |
| scimark_fft             | 328 ms                                                 | 296 ms: 1.11x faster                                                |
| scimark_sor             | 118 ms                                                 | 107 ms: 1.11x faster                                                |
| logging_silent          | 101 ns                                                 | 91.8 ns: 1.10x faster                                               |
| genshi_xml              | 51.8 ms                                                | 47.1 ms: 1.10x faster                                               |
| json_loads              | 26.5 us                                                | 24.1 us: 1.10x faster                                               |
| aiohttp                 | 1.10 ms                                                | 1.00 ms: 1.10x faster                                               |
| gunicorn                | 1.18 ms                                                | 1.07 ms: 1.10x faster                                               |
| float                   | 77.2 ms                                                | 71.4 ms: 1.08x faster                                               |
| richards                | 45.7 ms                                                | 42.4 ms: 1.08x faster                                               |
| sympy_str               | 290 ms                                                 | 270 ms: 1.07x faster                                                |
| xml_etree_parse         | 158 ms                                                 | 148 ms: 1.07x faster                                                |
| hexiom                  | 6.37 ms                                                | 5.96 ms: 1.07x faster                                               |
| regex_compile           | 138 ms                                                 | 129 ms: 1.07x faster                                                |
| json                    | 4.94 ms                                                | 4.63 ms: 1.07x faster                                               |
| deepcopy_memo           | 37.0 us                                                | 34.7 us: 1.07x faster                                               |
| pickle_pure_python      | 306 us                                                 | 288 us: 1.06x faster                                                |
| sympy_integrate         | 21.0 ms                                                | 19.8 ms: 1.06x faster                                               |
| sympy_sum               | 167 ms                                                 | 157 ms: 1.06x faster                                                |
| fannkuch                | 388 ms                                                 | 366 ms: 1.06x faster                                                |
| html5lib                | 64.5 ms                                                | 61.0 ms: 1.06x faster                                               |
| nqueens                 | 83.4 ms                                                | 79.1 ms: 1.05x faster                                               |
| chaos                   | 69.2 ms                                                | 65.7 ms: 1.05x faster                                               |
| scimark_monte_carlo     | 68.1 ms                                                | 64.6 ms: 1.05x faster                                               |
| logging_format          | 6.68 us                                                | 6.35 us: 1.05x faster                                               |
| spectral_norm           | 100 ms                                                 | 95.2 ms: 1.05x faster                                               |
| mako                    | 10.1 ms                                                | 9.62 ms: 1.05x faster                                               |
| genshi_text             | 21.6 ms                                                | 20.6 ms: 1.04x faster                                               |
| pprint_pformat          | 1.46 sec                                               | 1.40 sec: 1.04x faster                                              |
| bench_thread_pool       | 819 us                                                 | 785 us: 1.04x faster                                                |
| pyflate                 | 418 ms                                                 | 402 ms: 1.04x faster                                                |
| raytrace                | 297 ms                                                 | 285 ms: 1.04x faster                                                |
| docutils                | 2.63 sec                                               | 2.53 sec: 1.04x faster                                              |
| pycparser               | 1.18 sec                                               | 1.14 sec: 1.04x faster                                              |
| sympy_expand            | 475 ms                                                 | 457 ms: 1.04x faster                                                |
| sqlglot_optimize        | 53.1 ms                                                | 51.2 ms: 1.04x faster                                               |
| logging_simple          | 6.03 us                                                | 5.82 us: 1.04x faster                                               |
| unpickle                | 13.7 us                                                | 13.2 us: 1.04x faster                                               |
| go                      | 140 ms                                                 | 135 ms: 1.04x faster                                                |
| pprint_safe_repr        | 701 ms                                                 | 680 ms: 1.03x faster                                                |
| pathlib                 | 18.2 ms                                                | 17.7 ms: 1.03x faster                                               |
| chameleon               | 6.47 ms                                                | 6.30 ms: 1.03x faster                                               |
| 2to3                    | 259 ms                                                 | 252 ms: 1.03x faster                                                |
| sqlglot_normalize       | 108 ms                                                 | 105 ms: 1.02x faster                                                |
| deepcopy                | 342 us                                                 | 334 us: 1.02x faster                                                |
| dulwich_log             | 63.7 ms                                                | 62.3 ms: 1.02x faster                                               |
| tornado_http            | 96.3 ms                                                | 94.2 ms: 1.02x faster                                               |
| coverage                | 100 ms                                                 | 98.0 ms: 1.02x faster                                               |
| unpack_sequence         | 43.1 ns                                                | 42.2 ns: 1.02x faster                                               |
| xml_etree_iterparse     | 104 ms                                                 | 102 ms: 1.02x faster                                                |
| regex_v8                | 22.0 ms                                                | 21.7 ms: 1.02x faster                                               |
| sqlalchemy_declarative  | 138 ms                                                 | 136 ms: 1.02x faster                                                |
| create_gc_cycles        | 1.49 ms                                                | 1.46 ms: 1.02x faster                                               |
| telco                   | 6.58 ms                                                | 6.50 ms: 1.01x faster                                               |
| sqlalchemy_imperative   | 17.9 ms                                                | 17.7 ms: 1.01x faster                                               |
| mdp                     | 2.62 sec                                               | 2.60 sec: 1.00x faster                                              |
| sqlglot_transpile       | 1.70 ms                                                | 1.71 ms: 1.01x slower                                               |
| deepcopy_reduce         | 2.94 us                                                | 2.96 us: 1.01x slower                                               |
| django_template         | 32.6 ms                                                | 32.9 ms: 1.01x slower                                               |
| pickle                  | 10.1 us                                                | 10.2 us: 1.01x slower                                               |
| sqlglot_parse           | 1.40 ms                                                | 1.42 ms: 1.01x slower                                               |
| coroutines              | 25.5 ms                                                | 25.9 ms: 1.01x slower                                               |
| sqlite_synth            | 2.52 us                                                | 2.56 us: 1.02x slower                                               |
| async_tree_io           | 1.30 sec                                               | 1.32 sec: 1.02x slower                                              |
| nbody                   | 93.1 ms                                                | 95.0 ms: 1.02x slower                                               |
| pidigits                | 198 ms                                                 | 203 ms: 1.02x slower                                                |
| xml_etree_process       | 53.9 ms                                                | 55.1 ms: 1.02x slower                                               |
| crypto_pyaes            | 74.7 ms                                                | 76.5 ms: 1.02x slower                                               |
| pickle_list             | 4.11 us                                                | 4.22 us: 1.03x slower                                               |
| pickle_dict             | 31.1 us                                                | 32.0 us: 1.03x slower                                               |
| async_tree_cpu_io_mixed | 739 ms                                                 | 761 ms: 1.03x slower                                                |
| regex_dna               | 204 ms                                                 | 212 ms: 1.04x slower                                                |
| python_startup          | 8.52 ms                                                | 8.92 ms: 1.05x slower                                               |
| xml_etree_generate      | 76.2 ms                                                | 80.4 ms: 1.05x slower                                               |
| async_tree_memoization  | 627 ms                                                 | 662 ms: 1.06x slower                                                |
| python_startup_no_site  | 6.01 ms                                                | 6.48 ms: 1.08x slower                                               |
| generators              | 73.5 ms                                                | 79.4 ms: 1.08x slower                                               |
| async_generators        | 368 ms                                                 | 424 ms: 1.15x slower                                                |
| Geometric mean          | (ref)                                                  | 1.04x faster                                                        |

Benchmark hidden because not significant (7): unpickle_list, thrift, bench_mp_pool, scimark_lu, async_tree_none, djangocms, meteor_contest
Ignored benchmarks (8) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, comprehensions, dask, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x
