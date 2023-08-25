
# Results vs. 3.11.0

- fork: faster-cpython
- ref: long_rearrange_size_
- machine: linux-x86_64
- commit hash: ce6bfb2
- commit date: 2023-03-02
- overall geometric mean: 1.04x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230302-linux-x86_64-faster%2dcpython-long_rearrange_size_-3.12.0a5+-ce6bfb2 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 251 ms: 1.03x faster                                                             |
| chameleon      | 6.47 ms                                                | 6.43 ms: 1.01x faster                                                            |
| docutils       | 2.63 sec                                               | 2.55 sec: 1.03x faster                                                           |
| html5lib       | 64.5 ms                                                | 61.8 ms: 1.04x faster                                                            |
| tornado_http   | 96.3 ms                                                | 95.0 ms: 1.01x faster                                                            |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230302-linux-x86_64-faster%2dcpython-long_rearrange_size_-3.12.0a5+-ce6bfb2 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 198 ms                                                 | 188 ms: 1.05x faster                                                             |
| float          | 77.2 ms                                                | 74.6 ms: 1.04x faster                                                            |
| nbody          | 93.1 ms                                                | 91.6 ms: 1.02x faster                                                            |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230302-linux-x86_64-faster%2dcpython-long_rearrange_size_-3.12.0a5+-ce6bfb2 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.44 ms: 1.16x faster                                                            |
| regex_compile  | 138 ms                                                 | 134 ms: 1.03x faster                                                             |
| regex_v8       | 22.0 ms                                                | 21.5 ms: 1.03x faster                                                            |
| regex_dna      | 204 ms                                                 | 219 ms: 1.07x slower                                                             |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230302-linux-x86_64-faster%2dcpython-long_rearrange_size_-3.12.0a5+-ce6bfb2 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.41 ms: 1.34x faster                                                            |
| unpickle_pure_python | 228 us                                                 | 200 us: 1.14x faster                                                             |
| json_loads           | 26.5 us                                                | 23.9 us: 1.11x faster                                                            |
| xml_etree_parse      | 158 ms                                                 | 148 ms: 1.07x faster                                                             |
| pickle_pure_python   | 306 us                                                 | 285 us: 1.07x faster                                                             |
| xml_etree_iterparse  | 104 ms                                                 | 103 ms: 1.01x faster                                                             |
| pickle_dict          | 31.1 us                                                | 30.9 us: 1.01x faster                                                            |
| pickle_list          | 4.11 us                                                | 4.15 us: 1.01x slower                                                            |
| unpickle_list        | 4.91 us                                                | 5.00 us: 1.02x slower                                                            |
| xml_etree_process    | 53.9 ms                                                | 55.7 ms: 1.03x slower                                                            |
| xml_etree_generate   | 76.2 ms                                                | 80.8 ms: 1.06x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                                     |

Benchmark hidden because not significant (2): unpickle, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230302-linux-x86_64-faster%2dcpython-long_rearrange_size_-3.12.0a5+-ce6bfb2 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.02 ms: 1.06x slower                                                            |
| python_startup_no_site | 6.01 ms                                                | 6.53 ms: 1.09x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230302-linux-x86_64-faster%2dcpython-long_rearrange_size_-3.12.0a5+-ce6bfb2 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 48.2 ms: 1.07x faster                                                            |
| mako            | 10.1 ms                                                | 9.86 ms: 1.02x faster                                                            |
| genshi_text     | 21.6 ms                                                | 21.2 ms: 1.02x faster                                                            |
| django_template | 32.6 ms                                                | 32.7 ms: 1.00x slower                                                            |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                                     |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230302-linux-x86_64-faster%2dcpython-long_rearrange_size_-3.12.0a5+-ce6bfb2 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 31.0 ms: 2.37x faster                                                            |
| asyncio_tcp             | 922 ms                                                 | 509 ms: 1.81x faster                                                             |
| json_dumps              | 12.6 ms                                                | 9.41 ms: 1.34x faster                                                            |
| mypy2                   | 420 ms                                                 | 333 ms: 1.26x faster                                                             |
| regex_effbot            | 3.99 ms                                                | 3.44 ms: 1.16x faster                                                            |
| deltablue               | 3.67 ms                                                | 3.21 ms: 1.14x faster                                                            |
| unpickle_pure_python    | 228 us                                                 | 200 us: 1.14x faster                                                             |
| json_loads              | 26.5 us                                                | 23.9 us: 1.11x faster                                                            |
| coroutines              | 25.5 ms                                                | 23.1 ms: 1.11x faster                                                            |
| aiohttp                 | 1.10 ms                                                | 1.01 ms: 1.09x faster                                                            |
| json                    | 4.94 ms                                                | 4.57 ms: 1.08x faster                                                            |
| gunicorn                | 1.18 ms                                                | 1.09 ms: 1.08x faster                                                            |
| fannkuch                | 388 ms                                                 | 360 ms: 1.08x faster                                                             |
| scimark_sor             | 118 ms                                                 | 110 ms: 1.08x faster                                                             |
| deepcopy_memo           | 37.0 us                                                | 34.4 us: 1.08x faster                                                            |
| genshi_xml              | 51.8 ms                                                | 48.2 ms: 1.07x faster                                                            |
| xml_etree_parse         | 158 ms                                                 | 148 ms: 1.07x faster                                                             |
| logging_silent          | 101 ns                                                 | 94.3 ns: 1.07x faster                                                            |
| pickle_pure_python      | 306 us                                                 | 285 us: 1.07x faster                                                             |
| logging_format          | 6.68 us                                                | 6.30 us: 1.06x faster                                                            |
| pidigits                | 198 ms                                                 | 188 ms: 1.05x faster                                                             |
| pprint_pformat          | 1.46 sec                                               | 1.39 sec: 1.05x faster                                                           |
| coverage                | 100 ms                                                 | 95.7 ms: 1.05x faster                                                            |
| mdp                     | 2.62 sec                                               | 2.50 sec: 1.04x faster                                                           |
| html5lib                | 64.5 ms                                                | 61.8 ms: 1.04x faster                                                            |
| pprint_safe_repr        | 701 ms                                                 | 672 ms: 1.04x faster                                                             |
| logging_simple          | 6.03 us                                                | 5.78 us: 1.04x faster                                                            |
| richards                | 45.7 ms                                                | 43.9 ms: 1.04x faster                                                            |
| sqlglot_optimize        | 53.1 ms                                                | 51.2 ms: 1.04x faster                                                            |
| nqueens                 | 83.4 ms                                                | 80.4 ms: 1.04x faster                                                            |
| sqlglot_normalize       | 108 ms                                                 | 104 ms: 1.04x faster                                                             |
| meteor_contest          | 107 ms                                                 | 103 ms: 1.04x faster                                                             |
| pycparser               | 1.18 sec                                               | 1.14 sec: 1.04x faster                                                           |
| float                   | 77.2 ms                                                | 74.6 ms: 1.04x faster                                                            |
| 2to3                    | 259 ms                                                 | 251 ms: 1.03x faster                                                             |
| sympy_expand            | 475 ms                                                 | 460 ms: 1.03x faster                                                             |
| deepcopy                | 342 us                                                 | 331 us: 1.03x faster                                                             |
| go                      | 140 ms                                                 | 136 ms: 1.03x faster                                                             |
| docutils                | 2.63 sec                                               | 2.55 sec: 1.03x faster                                                           |
| unpack_sequence         | 43.1 ns                                                | 41.9 ns: 1.03x faster                                                            |
| regex_compile           | 138 ms                                                 | 134 ms: 1.03x faster                                                             |
| raytrace                | 297 ms                                                 | 289 ms: 1.03x faster                                                             |
| pathlib                 | 18.2 ms                                                | 17.8 ms: 1.03x faster                                                            |
| hexiom                  | 6.37 ms                                                | 6.21 ms: 1.03x faster                                                            |
| regex_v8                | 22.0 ms                                                | 21.5 ms: 1.03x faster                                                            |
| bench_thread_pool       | 819 us                                                 | 800 us: 1.02x faster                                                             |
| mako                    | 10.1 ms                                                | 9.86 ms: 1.02x faster                                                            |
| chaos                   | 69.2 ms                                                | 67.6 ms: 1.02x faster                                                            |
| pyflate                 | 418 ms                                                 | 409 ms: 1.02x faster                                                             |
| sympy_integrate         | 21.0 ms                                                | 20.6 ms: 1.02x faster                                                            |
| genshi_text             | 21.6 ms                                                | 21.2 ms: 1.02x faster                                                            |
| nbody                   | 93.1 ms                                                | 91.6 ms: 1.02x faster                                                            |
| spectral_norm           | 100 ms                                                 | 98.4 ms: 1.02x faster                                                            |
| scimark_fft             | 328 ms                                                 | 324 ms: 1.01x faster                                                             |
| sympy_str               | 290 ms                                                 | 286 ms: 1.01x faster                                                             |
| scimark_monte_carlo     | 68.1 ms                                                | 67.1 ms: 1.01x faster                                                            |
| telco                   | 6.58 ms                                                | 6.50 ms: 1.01x faster                                                            |
| tornado_http            | 96.3 ms                                                | 95.0 ms: 1.01x faster                                                            |
| xml_etree_iterparse     | 104 ms                                                 | 103 ms: 1.01x faster                                                             |
| create_gc_cycles        | 1.49 ms                                                | 1.47 ms: 1.01x faster                                                            |
| pickle_dict             | 31.1 us                                                | 30.9 us: 1.01x faster                                                            |
| chameleon               | 6.47 ms                                                | 6.43 ms: 1.01x faster                                                            |
| django_template         | 32.6 ms                                                | 32.7 ms: 1.00x slower                                                            |
| sympy_sum               | 167 ms                                                 | 167 ms: 1.00x slower                                                             |
| pickle_list             | 4.11 us                                                | 4.15 us: 1.01x slower                                                            |
| gc_traversal            | 4.02 ms                                                | 4.07 ms: 1.01x slower                                                            |
| scimark_lu              | 110 ms                                                 | 111 ms: 1.01x slower                                                             |
| sqlglot_transpile       | 1.70 ms                                                | 1.73 ms: 1.01x slower                                                            |
| unpickle_list           | 4.91 us                                                | 5.00 us: 1.02x slower                                                            |
| deepcopy_reduce         | 2.94 us                                                | 3.01 us: 1.02x slower                                                            |
| sqlglot_parse           | 1.40 ms                                                | 1.43 ms: 1.02x slower                                                            |
| thrift                  | 756 us                                                 | 781 us: 1.03x slower                                                             |
| xml_etree_process       | 53.9 ms                                                | 55.7 ms: 1.03x slower                                                            |
| sqlite_synth            | 2.52 us                                                | 2.62 us: 1.04x slower                                                            |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.71 ms: 1.05x slower                                                            |
| async_tree_memoization  | 627 ms                                                 | 661 ms: 1.05x slower                                                             |
| python_startup          | 8.52 ms                                                | 9.02 ms: 1.06x slower                                                            |
| xml_etree_generate      | 76.2 ms                                                | 80.8 ms: 1.06x slower                                                            |
| regex_dna               | 204 ms                                                 | 219 ms: 1.07x slower                                                             |
| comprehensions          | 22.4 us                                                | 24.1 us: 1.08x slower                                                            |
| python_startup_no_site  | 6.01 ms                                                | 6.53 ms: 1.09x slower                                                            |
| async_generators        | 368 ms                                                 | 421 ms: 1.14x slower                                                             |
| dask                    | 360 ms                                                 | 505 ms: 1.40x slower                                                             |
| Geometric mean          | (ref)                                                  | 1.04x faster                                                                     |

Benchmark hidden because not significant (11): crypto_pyaes, async_tree_none, unpickle, bench_mp_pool, sqlalchemy_declarative, sqlalchemy_imperative, async_tree_io, dulwich_log, djangocms, pickle, async_tree_cpu_io_mixed
Ignored benchmarks (6) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x
