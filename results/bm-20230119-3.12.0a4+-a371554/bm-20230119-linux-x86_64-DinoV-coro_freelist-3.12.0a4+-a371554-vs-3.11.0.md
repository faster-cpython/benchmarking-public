
# Results vs. 3.11.0

- fork: DinoV
- ref: coro_freelist
- machine: linux-x86_64
- commit hash: a371554
- commit date: 2023-01-19
- overall geometric mean: 1.04x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230119-linux-x86_64-DinoV-coro_freelist-3.12.0a4+-a371554 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 250 ms: 1.04x faster                                           |
| chameleon      | 6.47 ms                                                | 6.31 ms: 1.03x faster                                          |
| docutils       | 2.63 sec                                               | 2.47 sec: 1.06x faster                                         |
| html5lib       | 64.5 ms                                                | 59.7 ms: 1.08x faster                                          |
| tornado_http   | 96.3 ms                                                | 93.7 ms: 1.03x faster                                          |
| Geometric mean | (ref)                                                  | 1.05x faster                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230119-linux-x86_64-DinoV-coro_freelist-3.12.0a4+-a371554 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| float          | 77.2 ms                                                | 71.7 ms: 1.08x faster                                          |
| pidigits       | 198 ms                                                 | 190 ms: 1.04x faster                                           |
| nbody          | 93.1 ms                                                | 94.2 ms: 1.01x slower                                          |
| Geometric mean | (ref)                                                  | 1.04x faster                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230119-linux-x86_64-DinoV-coro_freelist-3.12.0a4+-a371554 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.36 ms: 1.19x faster                                          |
| regex_compile  | 138 ms                                                 | 129 ms: 1.07x faster                                           |
| regex_v8       | 22.0 ms                                                | 21.2 ms: 1.04x faster                                          |
| regex_dna      | 204 ms                                                 | 201 ms: 1.02x faster                                           |
| Geometric mean | (ref)                                                  | 1.08x faster                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230119-linux-x86_64-DinoV-coro_freelist-3.12.0a4+-a371554 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.39 ms: 1.34x faster                                          |
| unpickle_pure_python | 228 us                                                 | 198 us: 1.15x faster                                           |
| json_loads           | 26.5 us                                                | 24.0 us: 1.10x faster                                          |
| pickle_pure_python   | 306 us                                                 | 282 us: 1.08x faster                                           |
| xml_etree_parse      | 158 ms                                                 | 147 ms: 1.08x faster                                           |
| pickle_dict          | 31.1 us                                                | 29.7 us: 1.05x faster                                          |
| unpickle             | 13.7 us                                                | 13.2 us: 1.04x faster                                          |
| pickle_list          | 4.11 us                                                | 4.03 us: 1.02x faster                                          |
| xml_etree_iterparse  | 104 ms                                                 | 102 ms: 1.01x faster                                           |
| xml_etree_process    | 53.9 ms                                                | 53.6 ms: 1.01x faster                                          |
| unpickle_list        | 4.91 us                                                | 4.96 us: 1.01x slower                                          |
| xml_etree_generate   | 76.2 ms                                                | 77.1 ms: 1.01x slower                                          |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                   |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230119-linux-x86_64-DinoV-coro_freelist-3.12.0a4+-a371554 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.86 ms: 1.04x slower                                          |
| python_startup_no_site | 6.01 ms                                                | 6.42 ms: 1.07x slower                                          |
| Geometric mean         | (ref)                                                  | 1.05x slower                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230119-linux-x86_64-DinoV-coro_freelist-3.12.0a4+-a371554 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 47.3 ms: 1.09x faster                                          |
| mako            | 10.1 ms                                                | 9.59 ms: 1.05x faster                                          |
| genshi_text     | 21.6 ms                                                | 21.4 ms: 1.01x faster                                          |
| django_template | 32.6 ms                                                | 32.4 ms: 1.01x faster                                          |
| Geometric mean  | (ref)                                                  | 1.04x faster                                                   |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230119-linux-x86_64-DinoV-coro_freelist-3.12.0a4+-a371554 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------:|
| asyncio_tcp             | 922 ms                                                 | 501 ms: 1.84x faster                                           |
| json_dumps              | 12.6 ms                                                | 9.39 ms: 1.34x faster                                          |
| regex_effbot            | 3.99 ms                                                | 3.36 ms: 1.19x faster                                          |
| unpickle_pure_python    | 228 us                                                 | 198 us: 1.15x faster                                           |
| deltablue               | 3.67 ms                                                | 3.20 ms: 1.15x faster                                          |
| gunicorn                | 1.18 ms                                                | 1.06 ms: 1.11x faster                                          |
| deepcopy_memo           | 37.0 us                                                | 33.4 us: 1.11x faster                                          |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.06 ms: 1.11x faster                                          |
| aiohttp                 | 1.10 ms                                                | 993 us: 1.11x faster                                           |
| scimark_sor             | 118 ms                                                 | 107 ms: 1.10x faster                                           |
| logging_silent          | 101 ns                                                 | 91.6 ns: 1.10x faster                                          |
| json_loads              | 26.5 us                                                | 24.0 us: 1.10x faster                                          |
| coroutines              | 25.5 ms                                                | 23.2 ms: 1.10x faster                                          |
| genshi_xml              | 51.8 ms                                                | 47.3 ms: 1.09x faster                                          |
| pycparser               | 1.18 sec                                               | 1.08 sec: 1.09x faster                                         |
| pickle_pure_python      | 306 us                                                 | 282 us: 1.08x faster                                           |
| richards                | 45.7 ms                                                | 42.2 ms: 1.08x faster                                          |
| html5lib                | 64.5 ms                                                | 59.7 ms: 1.08x faster                                          |
| nqueens                 | 83.4 ms                                                | 77.1 ms: 1.08x faster                                          |
| float                   | 77.2 ms                                                | 71.7 ms: 1.08x faster                                          |
| json                    | 4.94 ms                                                | 4.59 ms: 1.08x faster                                          |
| xml_etree_parse         | 158 ms                                                 | 147 ms: 1.08x faster                                           |
| regex_compile           | 138 ms                                                 | 129 ms: 1.07x faster                                           |
| fannkuch                | 388 ms                                                 | 362 ms: 1.07x faster                                           |
| pprint_pformat          | 1.46 sec                                               | 1.36 sec: 1.07x faster                                         |
| spectral_norm           | 100 ms                                                 | 93.8 ms: 1.07x faster                                          |
| coverage                | 100 ms                                                 | 93.9 ms: 1.07x faster                                          |
| docutils                | 2.63 sec                                               | 2.47 sec: 1.06x faster                                         |
| pprint_safe_repr        | 701 ms                                                 | 663 ms: 1.06x faster                                           |
| hexiom                  | 6.37 ms                                                | 6.03 ms: 1.06x faster                                          |
| logging_format          | 6.68 us                                                | 6.34 us: 1.05x faster                                          |
| mako                    | 10.1 ms                                                | 9.59 ms: 1.05x faster                                          |
| logging_simple          | 6.03 us                                                | 5.74 us: 1.05x faster                                          |
| sqlglot_optimize        | 53.1 ms                                                | 50.6 ms: 1.05x faster                                          |
| sympy_expand            | 475 ms                                                 | 453 ms: 1.05x faster                                           |
| raytrace                | 297 ms                                                 | 283 ms: 1.05x faster                                           |
| pickle_dict             | 31.1 us                                                | 29.7 us: 1.05x faster                                          |
| bench_thread_pool       | 819 us                                                 | 783 us: 1.05x faster                                           |
| scimark_fft             | 328 ms                                                 | 314 ms: 1.05x faster                                           |
| pidigits                | 198 ms                                                 | 190 ms: 1.04x faster                                           |
| deepcopy                | 342 us                                                 | 328 us: 1.04x faster                                           |
| regex_v8                | 22.0 ms                                                | 21.2 ms: 1.04x faster                                          |
| sqlglot_normalize       | 108 ms                                                 | 104 ms: 1.04x faster                                           |
| telco                   | 6.58 ms                                                | 6.33 ms: 1.04x faster                                          |
| pyflate                 | 418 ms                                                 | 402 ms: 1.04x faster                                           |
| mdp                     | 2.62 sec                                               | 2.52 sec: 1.04x faster                                         |
| unpack_sequence         | 43.1 ns                                                | 41.5 ns: 1.04x faster                                          |
| 2to3                    | 259 ms                                                 | 250 ms: 1.04x faster                                           |
| unpickle                | 13.7 us                                                | 13.2 us: 1.04x faster                                          |
| sympy_str               | 290 ms                                                 | 280 ms: 1.04x faster                                           |
| sympy_integrate         | 21.0 ms                                                | 20.3 ms: 1.03x faster                                          |
| scimark_monte_carlo     | 68.1 ms                                                | 65.8 ms: 1.03x faster                                          |
| async_generators        | 368 ms                                                 | 357 ms: 1.03x faster                                           |
| create_gc_cycles        | 1.49 ms                                                | 1.44 ms: 1.03x faster                                          |
| tornado_http            | 96.3 ms                                                | 93.7 ms: 1.03x faster                                          |
| dulwich_log             | 63.7 ms                                                | 62.0 ms: 1.03x faster                                          |
| chameleon               | 6.47 ms                                                | 6.31 ms: 1.03x faster                                          |
| sympy_sum               | 167 ms                                                 | 163 ms: 1.02x faster                                           |
| pickle_list             | 4.11 us                                                | 4.03 us: 1.02x faster                                          |
| scimark_lu              | 110 ms                                                 | 108 ms: 1.02x faster                                           |
| chaos                   | 69.2 ms                                                | 67.9 ms: 1.02x faster                                          |
| regex_dna               | 204 ms                                                 | 201 ms: 1.02x faster                                           |
| xml_etree_iterparse     | 104 ms                                                 | 102 ms: 1.01x faster                                           |
| sqlglot_transpile       | 1.70 ms                                                | 1.68 ms: 1.01x faster                                          |
| pathlib                 | 18.2 ms                                                | 18.1 ms: 1.01x faster                                          |
| genshi_text             | 21.6 ms                                                | 21.4 ms: 1.01x faster                                          |
| thrift                  | 756 us                                                 | 751 us: 1.01x faster                                           |
| xml_etree_process       | 53.9 ms                                                | 53.6 ms: 1.01x faster                                          |
| django_template         | 32.6 ms                                                | 32.4 ms: 1.01x faster                                          |
| sqlglot_parse           | 1.40 ms                                                | 1.39 ms: 1.00x faster                                          |
| async_tree_cpu_io_mixed | 739 ms                                                 | 746 ms: 1.01x slower                                           |
| nbody                   | 93.1 ms                                                | 94.2 ms: 1.01x slower                                          |
| unpickle_list           | 4.91 us                                                | 4.96 us: 1.01x slower                                          |
| xml_etree_generate      | 76.2 ms                                                | 77.1 ms: 1.01x slower                                          |
| sqlite_synth            | 2.52 us                                                | 2.56 us: 1.02x slower                                          |
| async_tree_io           | 1.30 sec                                               | 1.32 sec: 1.02x slower                                         |
| async_tree_memoization  | 627 ms                                                 | 646 ms: 1.03x slower                                           |
| python_startup          | 8.52 ms                                                | 8.86 ms: 1.04x slower                                          |
| generators              | 73.5 ms                                                | 76.7 ms: 1.04x slower                                          |
| gc_traversal            | 4.02 ms                                                | 4.29 ms: 1.07x slower                                          |
| python_startup_no_site  | 6.01 ms                                                | 6.42 ms: 1.07x slower                                          |
| dask                    | 360 ms                                                 | 495 ms: 1.38x slower                                           |
| Geometric mean          | (ref)                                                  | 1.04x faster                                                   |

Benchmark hidden because not significant (8): meteor_contest, crypto_pyaes, bench_mp_pool, async_tree_none, deepcopy_reduce, go, pickle, djangocms
Ignored benchmarks (10) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, comprehensions, flaskblogging, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230119-3.12.0a4+-a371554/bm-20230119-linux-x86_64-DinoV-coro_freelist-3.12.0a4+-a371554.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x
