
# Results vs. 3.11.0

- fork: iritkatriel
- ref: int_freelist
- machine: linux-x86_64
- commit hash: 906fc0d
- commit date: 2023-01-30
- overall geometric mean: 1.04x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230130-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-906fc0d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 253 ms: 1.02x faster                                                |
| chameleon      | 6.47 ms                                                | 6.31 ms: 1.03x faster                                               |
| docutils       | 2.63 sec                                               | 2.49 sec: 1.05x faster                                              |
| html5lib       | 64.5 ms                                                | 60.3 ms: 1.07x faster                                               |
| tornado_http   | 96.3 ms                                                | 93.9 ms: 1.02x faster                                               |
| Geometric mean | (ref)                                                  | 1.04x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230130-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-906fc0d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 77.2 ms                                                | 72.1 ms: 1.07x faster                                               |
| pidigits       | 198 ms                                                 | 199 ms: 1.00x slower                                                |
| nbody          | 93.1 ms                                                | 95.5 ms: 1.03x slower                                               |
| Geometric mean | (ref)                                                  | 1.01x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230130-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-906fc0d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.63 ms: 1.10x faster                                               |
| regex_compile  | 138 ms                                                 | 128 ms: 1.08x faster                                                |
| regex_v8       | 22.0 ms                                                | 21.7 ms: 1.01x faster                                               |
| regex_dna      | 204 ms                                                 | 209 ms: 1.03x slower                                                |
| Geometric mean | (ref)                                                  | 1.04x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230130-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-906fc0d |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.58 ms: 1.31x faster                                               |
| unpickle_pure_python | 228 us                                                 | 197 us: 1.16x faster                                                |
| json_loads           | 26.5 us                                                | 24.2 us: 1.09x faster                                               |
| pickle_pure_python   | 306 us                                                 | 287 us: 1.06x faster                                                |
| xml_etree_parse      | 158 ms                                                 | 149 ms: 1.06x faster                                                |
| unpickle             | 13.7 us                                                | 13.2 us: 1.04x faster                                               |
| xml_etree_iterparse  | 104 ms                                                 | 103 ms: 1.01x faster                                                |
| xml_etree_process    | 53.9 ms                                                | 53.5 ms: 1.01x faster                                               |
| unpickle_list        | 4.91 us                                                | 4.89 us: 1.00x faster                                               |
| pickle_dict          | 31.1 us                                                | 31.2 us: 1.00x slower                                               |
| pickle               | 10.1 us                                                | 10.2 us: 1.01x slower                                               |
| xml_etree_generate   | 76.2 ms                                                | 77.6 ms: 1.02x slower                                               |
| pickle_list          | 4.11 us                                                | 4.24 us: 1.03x slower                                               |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230130-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-906fc0d |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.98 ms: 1.05x slower                                               |
| python_startup_no_site | 6.01 ms                                                | 6.49 ms: 1.08x slower                                               |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230130-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-906fc0d |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 47.6 ms: 1.09x faster                                               |
| genshi_text     | 21.6 ms                                                | 21.0 ms: 1.03x faster                                               |
| mako            | 10.1 ms                                                | 9.87 ms: 1.02x faster                                               |
| django_template | 32.6 ms                                                | 33.1 ms: 1.02x slower                                               |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                        |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230130-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-906fc0d |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| asyncio_tcp             | 922 ms                                                 | 494 ms: 1.87x faster                                                |
| json_dumps              | 12.6 ms                                                | 9.58 ms: 1.31x faster                                               |
| unpickle_pure_python    | 228 us                                                 | 197 us: 1.16x faster                                                |
| deltablue               | 3.67 ms                                                | 3.20 ms: 1.15x faster                                               |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.02 ms: 1.12x faster                                               |
| aiohttp                 | 1.10 ms                                                | 997 us: 1.10x faster                                                |
| regex_effbot            | 3.99 ms                                                | 3.63 ms: 1.10x faster                                               |
| gunicorn                | 1.18 ms                                                | 1.07 ms: 1.10x faster                                               |
| richards                | 45.7 ms                                                | 41.6 ms: 1.10x faster                                               |
| logging_silent          | 101 ns                                                 | 92.2 ns: 1.10x faster                                               |
| json_loads              | 26.5 us                                                | 24.2 us: 1.09x faster                                               |
| genshi_xml              | 51.8 ms                                                | 47.6 ms: 1.09x faster                                               |
| chaos                   | 69.2 ms                                                | 63.9 ms: 1.08x faster                                               |
| fannkuch                | 388 ms                                                 | 358 ms: 1.08x faster                                                |
| regex_compile           | 138 ms                                                 | 128 ms: 1.08x faster                                                |
| sympy_str               | 290 ms                                                 | 270 ms: 1.07x faster                                                |
| float                   | 77.2 ms                                                | 72.1 ms: 1.07x faster                                               |
| sympy_sum               | 167 ms                                                 | 156 ms: 1.07x faster                                                |
| html5lib                | 64.5 ms                                                | 60.3 ms: 1.07x faster                                               |
| hexiom                  | 6.37 ms                                                | 5.97 ms: 1.07x faster                                               |
| deepcopy_memo           | 37.0 us                                                | 34.6 us: 1.07x faster                                               |
| scimark_sor             | 118 ms                                                 | 111 ms: 1.07x faster                                                |
| pickle_pure_python      | 306 us                                                 | 287 us: 1.06x faster                                                |
| xml_etree_parse         | 158 ms                                                 | 149 ms: 1.06x faster                                                |
| sympy_integrate         | 21.0 ms                                                | 19.8 ms: 1.06x faster                                               |
| logging_simple          | 6.03 us                                                | 5.68 us: 1.06x faster                                               |
| logging_format          | 6.68 us                                                | 6.30 us: 1.06x faster                                               |
| pycparser               | 1.18 sec                                               | 1.12 sec: 1.06x faster                                              |
| json                    | 4.94 ms                                                | 4.67 ms: 1.06x faster                                               |
| pyflate                 | 418 ms                                                 | 396 ms: 1.06x faster                                                |
| scimark_fft             | 328 ms                                                 | 311 ms: 1.06x faster                                                |
| pprint_pformat          | 1.46 sec                                               | 1.38 sec: 1.05x faster                                              |
| docutils                | 2.63 sec                                               | 2.49 sec: 1.05x faster                                              |
| gc_traversal            | 4.02 ms                                                | 3.82 ms: 1.05x faster                                               |
| nqueens                 | 83.4 ms                                                | 79.5 ms: 1.05x faster                                               |
| pprint_safe_repr        | 701 ms                                                 | 669 ms: 1.05x faster                                                |
| sympy_expand            | 475 ms                                                 | 453 ms: 1.05x faster                                                |
| async_generators        | 368 ms                                                 | 353 ms: 1.04x faster                                                |
| coverage                | 100 ms                                                 | 96.0 ms: 1.04x faster                                               |
| go                      | 140 ms                                                 | 134 ms: 1.04x faster                                                |
| sqlglot_optimize        | 53.1 ms                                                | 51.2 ms: 1.04x faster                                               |
| unpickle                | 13.7 us                                                | 13.2 us: 1.04x faster                                               |
| bench_thread_pool       | 819 us                                                 | 790 us: 1.04x faster                                                |
| deepcopy                | 342 us                                                 | 330 us: 1.04x faster                                                |
| scimark_lu              | 110 ms                                                 | 106 ms: 1.04x faster                                                |
| telco                   | 6.58 ms                                                | 6.38 ms: 1.03x faster                                               |
| genshi_text             | 21.6 ms                                                | 21.0 ms: 1.03x faster                                               |
| raytrace                | 297 ms                                                 | 289 ms: 1.03x faster                                                |
| chameleon               | 6.47 ms                                                | 6.31 ms: 1.03x faster                                               |
| tornado_http            | 96.3 ms                                                | 93.9 ms: 1.02x faster                                               |
| sqlglot_normalize       | 108 ms                                                 | 105 ms: 1.02x faster                                                |
| pathlib                 | 18.2 ms                                                | 17.8 ms: 1.02x faster                                               |
| mako                    | 10.1 ms                                                | 9.87 ms: 1.02x faster                                               |
| 2to3                    | 259 ms                                                 | 253 ms: 1.02x faster                                                |
| scimark_monte_carlo     | 68.1 ms                                                | 66.7 ms: 1.02x faster                                               |
| thrift                  | 756 us                                                 | 742 us: 1.02x faster                                                |
| create_gc_cycles        | 1.49 ms                                                | 1.46 ms: 1.02x faster                                               |
| coroutines              | 25.5 ms                                                | 25.1 ms: 1.02x faster                                               |
| dulwich_log             | 63.7 ms                                                | 62.8 ms: 1.01x faster                                               |
| regex_v8                | 22.0 ms                                                | 21.7 ms: 1.01x faster                                               |
| xml_etree_iterparse     | 104 ms                                                 | 103 ms: 1.01x faster                                                |
| xml_etree_process       | 53.9 ms                                                | 53.5 ms: 1.01x faster                                               |
| unpickle_list           | 4.91 us                                                | 4.89 us: 1.00x faster                                               |
| mdp                     | 2.62 sec                                               | 2.62 sec: 1.00x slower                                              |
| pickle_dict             | 31.1 us                                                | 31.2 us: 1.00x slower                                               |
| pidigits                | 198 ms                                                 | 199 ms: 1.00x slower                                                |
| sqlglot_parse           | 1.40 ms                                                | 1.41 ms: 1.00x slower                                               |
| async_tree_io           | 1.30 sec                                               | 1.31 sec: 1.01x slower                                              |
| pickle                  | 10.1 us                                                | 10.2 us: 1.01x slower                                               |
| django_template         | 32.6 ms                                                | 33.1 ms: 1.02x slower                                               |
| crypto_pyaes            | 74.7 ms                                                | 76.0 ms: 1.02x slower                                               |
| xml_etree_generate      | 76.2 ms                                                | 77.6 ms: 1.02x slower                                               |
| async_tree_cpu_io_mixed | 739 ms                                                 | 752 ms: 1.02x slower                                                |
| regex_dna               | 204 ms                                                 | 209 ms: 1.03x slower                                                |
| nbody                   | 93.1 ms                                                | 95.5 ms: 1.03x slower                                               |
| pickle_list             | 4.11 us                                                | 4.24 us: 1.03x slower                                               |
| sqlite_synth            | 2.52 us                                                | 2.60 us: 1.03x slower                                               |
| spectral_norm           | 100 ms                                                 | 105 ms: 1.05x slower                                                |
| async_tree_memoization  | 627 ms                                                 | 658 ms: 1.05x slower                                                |
| python_startup          | 8.52 ms                                                | 8.98 ms: 1.05x slower                                               |
| generators              | 73.5 ms                                                | 78.0 ms: 1.06x slower                                               |
| python_startup_no_site  | 6.01 ms                                                | 6.49 ms: 1.08x slower                                               |
| dask                    | 360 ms                                                 | 498 ms: 1.38x slower                                                |
| Geometric mean          | (ref)                                                  | 1.04x faster                                                        |

Benchmark hidden because not significant (7): djangocms, async_tree_none, deepcopy_reduce, bench_mp_pool, sqlglot_transpile, unpack_sequence, meteor_contest
Ignored benchmarks (10) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, comprehensions, flaskblogging, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230130-3.12.0a4+-906fc0d/bm-20230130-linux-x86_64-iritkatriel-int_freelist-3.12.0a4+-906fc0d.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x
