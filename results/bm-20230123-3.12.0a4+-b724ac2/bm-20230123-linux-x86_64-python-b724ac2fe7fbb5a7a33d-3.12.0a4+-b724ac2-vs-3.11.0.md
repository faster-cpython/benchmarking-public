
# Results vs. 3.11.0

- fork: python
- ref: b724ac2fe7fbb5a7a33d
- machine: linux-x86_64
- commit hash: b724ac2
- commit date: 2023-01-23
- overall geometric mean: 1.04x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230123-linux-x86_64-python-b724ac2fe7fbb5a7a33d-3.12.0a4+-b724ac2 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 253 ms: 1.02x faster                                                   |
| chameleon      | 6.47 ms                                                | 6.42 ms: 1.01x faster                                                  |
| docutils       | 2.63 sec                                               | 2.52 sec: 1.04x faster                                                 |
| html5lib       | 64.5 ms                                                | 60.3 ms: 1.07x faster                                                  |
| tornado_http   | 96.3 ms                                                | 93.7 ms: 1.03x faster                                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230123-linux-x86_64-python-b724ac2fe7fbb5a7a33d-3.12.0a4+-b724ac2 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 77.2 ms                                                | 72.6 ms: 1.06x faster                                                  |
| pidigits       | 198 ms                                                 | 197 ms: 1.00x faster                                                   |
| nbody          | 93.1 ms                                                | 93.8 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230123-linux-x86_64-python-b724ac2fe7fbb5a7a33d-3.12.0a4+-b724ac2 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.44 ms: 1.16x faster                                                  |
| regex_compile  | 138 ms                                                 | 129 ms: 1.07x faster                                                   |
| regex_v8       | 22.0 ms                                                | 21.0 ms: 1.05x faster                                                  |
| regex_dna      | 204 ms                                                 | 201 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                  | 1.07x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230123-linux-x86_64-python-b724ac2fe7fbb5a7a33d-3.12.0a4+-b724ac2 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.38 ms: 1.34x faster                                                  |
| unpickle_pure_python | 228 us                                                 | 197 us: 1.16x faster                                                   |
| json_loads           | 26.5 us                                                | 24.3 us: 1.09x faster                                                  |
| pickle_pure_python   | 306 us                                                 | 284 us: 1.08x faster                                                   |
| xml_etree_parse      | 158 ms                                                 | 156 ms: 1.01x faster                                                   |
| xml_etree_process    | 53.9 ms                                                | 54.4 ms: 1.01x slower                                                  |
| xml_etree_iterparse  | 104 ms                                                 | 106 ms: 1.03x slower                                                   |
| pickle               | 10.1 us                                                | 10.3 us: 1.03x slower                                                  |
| pickle_dict          | 31.1 us                                                | 32.2 us: 1.03x slower                                                  |
| unpickle_list        | 4.91 us                                                | 5.08 us: 1.04x slower                                                  |
| pickle_list          | 4.11 us                                                | 4.26 us: 1.04x slower                                                  |
| xml_etree_generate   | 76.2 ms                                                | 79.1 ms: 1.04x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                           |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230123-linux-x86_64-python-b724ac2fe7fbb5a7a33d-3.12.0a4+-b724ac2 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.96 ms: 1.05x slower                                                  |
| python_startup_no_site | 6.01 ms                                                | 6.49 ms: 1.08x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230123-linux-x86_64-python-b724ac2fe7fbb5a7a33d-3.12.0a4+-b724ac2 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 46.8 ms: 1.10x faster                                                  |
| mako            | 10.1 ms                                                | 9.66 ms: 1.04x faster                                                  |
| django_template | 32.6 ms                                                | 32.9 ms: 1.01x slower                                                  |
| genshi_text     | 21.6 ms                                                | 22.1 ms: 1.03x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230123-linux-x86_64-python-b724ac2fe7fbb5a7a33d-3.12.0a4+-b724ac2 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| asyncio_tcp             | 922 ms                                                 | 490 ms: 1.88x faster                                                   |
| json_dumps              | 12.6 ms                                                | 9.38 ms: 1.34x faster                                                  |
| regex_effbot            | 3.99 ms                                                | 3.44 ms: 1.16x faster                                                  |
| unpickle_pure_python    | 228 us                                                 | 197 us: 1.16x faster                                                   |
| deltablue               | 3.67 ms                                                | 3.23 ms: 1.14x faster                                                  |
| scimark_sor             | 118 ms                                                 | 105 ms: 1.12x faster                                                   |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.06 ms: 1.11x faster                                                  |
| aiohttp                 | 1.10 ms                                                | 994 us: 1.11x faster                                                   |
| genshi_xml              | 51.8 ms                                                | 46.8 ms: 1.10x faster                                                  |
| gunicorn                | 1.18 ms                                                | 1.07 ms: 1.10x faster                                                  |
| nqueens                 | 83.4 ms                                                | 76.2 ms: 1.09x faster                                                  |
| json_loads              | 26.5 us                                                | 24.3 us: 1.09x faster                                                  |
| chaos                   | 69.2 ms                                                | 63.6 ms: 1.09x faster                                                  |
| logging_silent          | 101 ns                                                 | 93.3 ns: 1.08x faster                                                  |
| pycparser               | 1.18 sec                                               | 1.10 sec: 1.08x faster                                                 |
| mdp                     | 2.62 sec                                               | 2.43 sec: 1.08x faster                                                 |
| pickle_pure_python      | 306 us                                                 | 284 us: 1.08x faster                                                   |
| json                    | 4.94 ms                                                | 4.60 ms: 1.07x faster                                                  |
| scimark_fft             | 328 ms                                                 | 306 ms: 1.07x faster                                                   |
| hexiom                  | 6.37 ms                                                | 5.95 ms: 1.07x faster                                                  |
| html5lib                | 64.5 ms                                                | 60.3 ms: 1.07x faster                                                  |
| fannkuch                | 388 ms                                                 | 363 ms: 1.07x faster                                                   |
| deepcopy_memo           | 37.0 us                                                | 34.6 us: 1.07x faster                                                  |
| regex_compile           | 138 ms                                                 | 129 ms: 1.07x faster                                                   |
| richards                | 45.7 ms                                                | 42.9 ms: 1.06x faster                                                  |
| float                   | 77.2 ms                                                | 72.6 ms: 1.06x faster                                                  |
| raytrace                | 297 ms                                                 | 280 ms: 1.06x faster                                                   |
| bench_thread_pool       | 819 us                                                 | 774 us: 1.06x faster                                                   |
| logging_format          | 6.68 us                                                | 6.34 us: 1.05x faster                                                  |
| logging_simple          | 6.03 us                                                | 5.74 us: 1.05x faster                                                  |
| pprint_pformat          | 1.46 sec                                               | 1.39 sec: 1.05x faster                                                 |
| async_generators        | 368 ms                                                 | 351 ms: 1.05x faster                                                   |
| regex_v8                | 22.0 ms                                                | 21.0 ms: 1.05x faster                                                  |
| pyflate                 | 418 ms                                                 | 400 ms: 1.05x faster                                                   |
| deepcopy                | 342 us                                                 | 327 us: 1.04x faster                                                   |
| docutils                | 2.63 sec                                               | 2.52 sec: 1.04x faster                                                 |
| scimark_monte_carlo     | 68.1 ms                                                | 65.2 ms: 1.04x faster                                                  |
| mako                    | 10.1 ms                                                | 9.66 ms: 1.04x faster                                                  |
| sympy_expand            | 475 ms                                                 | 456 ms: 1.04x faster                                                   |
| pprint_safe_repr        | 701 ms                                                 | 674 ms: 1.04x faster                                                   |
| sympy_integrate         | 21.0 ms                                                | 20.2 ms: 1.04x faster                                                  |
| unpack_sequence         | 43.1 ns                                                | 41.6 ns: 1.04x faster                                                  |
| sqlglot_optimize        | 53.1 ms                                                | 51.3 ms: 1.03x faster                                                  |
| sympy_str               | 290 ms                                                 | 281 ms: 1.03x faster                                                   |
| telco                   | 6.58 ms                                                | 6.38 ms: 1.03x faster                                                  |
| go                      | 140 ms                                                 | 136 ms: 1.03x faster                                                   |
| sqlglot_normalize       | 108 ms                                                 | 105 ms: 1.03x faster                                                   |
| coverage                | 100 ms                                                 | 97.3 ms: 1.03x faster                                                  |
| dulwich_log             | 63.7 ms                                                | 62.0 ms: 1.03x faster                                                  |
| tornado_http            | 96.3 ms                                                | 93.7 ms: 1.03x faster                                                  |
| djangocms               | 32.4 us                                                | 31.6 us: 1.03x faster                                                  |
| spectral_norm           | 100 ms                                                 | 97.7 ms: 1.02x faster                                                  |
| scimark_lu              | 110 ms                                                 | 107 ms: 1.02x faster                                                   |
| 2to3                    | 259 ms                                                 | 253 ms: 1.02x faster                                                   |
| meteor_contest          | 107 ms                                                 | 105 ms: 1.02x faster                                                   |
| pathlib                 | 18.2 ms                                                | 17.9 ms: 1.02x faster                                                  |
| crypto_pyaes            | 74.7 ms                                                | 73.3 ms: 1.02x faster                                                  |
| sympy_sum               | 167 ms                                                 | 164 ms: 1.02x faster                                                   |
| gc_traversal            | 4.02 ms                                                | 3.96 ms: 1.02x faster                                                  |
| xml_etree_parse         | 158 ms                                                 | 156 ms: 1.01x faster                                                   |
| thrift                  | 756 us                                                 | 746 us: 1.01x faster                                                   |
| regex_dna               | 204 ms                                                 | 201 ms: 1.01x faster                                                   |
| chameleon               | 6.47 ms                                                | 6.42 ms: 1.01x faster                                                  |
| pidigits                | 198 ms                                                 | 197 ms: 1.00x faster                                                   |
| nbody                   | 93.1 ms                                                | 93.8 ms: 1.01x slower                                                  |
| sqlglot_parse           | 1.40 ms                                                | 1.41 ms: 1.01x slower                                                  |
| deepcopy_reduce         | 2.94 us                                                | 2.97 us: 1.01x slower                                                  |
| django_template         | 32.6 ms                                                | 32.9 ms: 1.01x slower                                                  |
| xml_etree_process       | 53.9 ms                                                | 54.4 ms: 1.01x slower                                                  |
| generators              | 73.5 ms                                                | 74.7 ms: 1.02x slower                                                  |
| async_tree_cpu_io_mixed | 739 ms                                                 | 755 ms: 1.02x slower                                                   |
| sqlite_synth            | 2.52 us                                                | 2.58 us: 1.02x slower                                                  |
| xml_etree_iterparse     | 104 ms                                                 | 106 ms: 1.03x slower                                                   |
| async_tree_io           | 1.30 sec                                               | 1.33 sec: 1.03x slower                                                 |
| genshi_text             | 21.6 ms                                                | 22.1 ms: 1.03x slower                                                  |
| pickle                  | 10.1 us                                                | 10.3 us: 1.03x slower                                                  |
| pickle_dict             | 31.1 us                                                | 32.2 us: 1.03x slower                                                  |
| unpickle_list           | 4.91 us                                                | 5.08 us: 1.04x slower                                                  |
| pickle_list             | 4.11 us                                                | 4.26 us: 1.04x slower                                                  |
| xml_etree_generate      | 76.2 ms                                                | 79.1 ms: 1.04x slower                                                  |
| python_startup          | 8.52 ms                                                | 8.96 ms: 1.05x slower                                                  |
| async_tree_memoization  | 627 ms                                                 | 666 ms: 1.06x slower                                                   |
| python_startup_no_site  | 6.01 ms                                                | 6.49 ms: 1.08x slower                                                  |
| dask                    | 360 ms                                                 | 495 ms: 1.38x slower                                                   |
| Geometric mean          | (ref)                                                  | 1.04x faster                                                           |

Benchmark hidden because not significant (6): unpickle, create_gc_cycles, bench_mp_pool, coroutines, sqlglot_transpile, async_tree_none
Ignored benchmarks (10) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, comprehensions, flaskblogging, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230123-3.12.0a4+-b724ac2/bm-20230123-linux-x86_64-python-b724ac2fe7fbb5a7a33d-3.12.0a4+-b724ac2.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x
