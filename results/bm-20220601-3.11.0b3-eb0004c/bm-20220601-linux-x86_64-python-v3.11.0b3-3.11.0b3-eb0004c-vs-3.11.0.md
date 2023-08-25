
# Results vs. 3.11.0

- fork: python
- ref: v3.11.0b3
- machine: linux-x86_64
- commit hash: eb0004c
- commit date: 2022-06-01
- overall geometric mean: 1.01x faster \*
- HPT reliability: 99.88%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220601-linux-x86_64-python-v3.11.0b3-3.11.0b3-eb0004c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 256 ms: 1.01x faster                                       |
| chameleon      | 6.47 ms                                                | 6.42 ms: 1.01x faster                                      |
| docutils       | 2.63 sec                                               | 2.56 sec: 1.03x faster                                     |
| html5lib       | 64.5 ms                                                | 62.8 ms: 1.03x faster                                      |
| tornado_http   | 96.3 ms                                                | 94.7 ms: 1.02x faster                                      |
| Geometric mean | (ref)                                                  | 1.02x faster                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220601-linux-x86_64-python-v3.11.0b3-3.11.0b3-eb0004c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| float          | 77.2 ms                                                | 73.9 ms: 1.05x faster                                      |
| pidigits       | 198 ms                                                 | 194 ms: 1.02x faster                                       |
| nbody          | 93.1 ms                                                | 94.9 ms: 1.02x slower                                      |
| Geometric mean | (ref)                                                  | 1.02x faster                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220601-linux-x86_64-python-v3.11.0b3-3.11.0b3-eb0004c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 2.92 ms: 1.37x faster                                      |
| regex_dna      | 204 ms                                                 | 194 ms: 1.05x faster                                       |
| regex_v8       | 22.0 ms                                                | 21.4 ms: 1.03x faster                                      |
| regex_compile  | 138 ms                                                 | 136 ms: 1.01x faster                                       |
| Geometric mean | (ref)                                                  | 1.11x faster                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220601-linux-x86_64-python-v3.11.0b3-3.11.0b3-eb0004c |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| pickle_dict          | 31.1 us                                                | 26.0 us: 1.20x faster                                      |
| pickle               | 10.1 us                                                | 9.37 us: 1.07x faster                                      |
| json_loads           | 26.5 us                                                | 24.9 us: 1.07x faster                                      |
| pickle_pure_python   | 306 us                                                 | 301 us: 1.02x faster                                       |
| xml_etree_process    | 53.9 ms                                                | 53.6 ms: 1.01x faster                                      |
| unpickle_pure_python | 228 us                                                 | 227 us: 1.00x faster                                       |
| json_dumps           | 12.6 ms                                                | 12.7 ms: 1.01x slower                                      |
| xml_etree_generate   | 76.2 ms                                                | 76.7 ms: 1.01x slower                                      |
| unpickle_list        | 4.91 us                                                | 4.96 us: 1.01x slower                                      |
| xml_etree_iterparse  | 104 ms                                                 | 108 ms: 1.04x slower                                       |
| pickle_list          | 4.11 us                                                | 4.27 us: 1.04x slower                                      |
| Geometric mean       | (ref)                                                  | 1.02x faster                                               |

Benchmark hidden because not significant (2): unpickle, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220601-linux-x86_64-python-v3.11.0b3-3.11.0b3-eb0004c |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.51 ms: 1.00x faster                                      |
| python_startup_no_site | 6.01 ms                                                | 6.01 ms: 1.00x faster                                      |
| Geometric mean         | (ref)                                                  | 1.00x faster                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220601-linux-x86_64-python-v3.11.0b3-3.11.0b3-eb0004c |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| mako            | 10.1 ms                                                | 9.99 ms: 1.01x faster                                      |
| genshi_xml      | 51.8 ms                                                | 52.3 ms: 1.01x slower                                      |
| django_template | 32.6 ms                                                | 33.0 ms: 1.01x slower                                      |
| genshi_text     | 21.6 ms                                                | 22.0 ms: 1.02x slower                                      |
| Geometric mean  | (ref)                                                  | 1.01x slower                                               |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220601-linux-x86_64-python-v3.11.0b3-3.11.0b3-eb0004c |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------:|
| regex_effbot            | 3.99 ms                                                | 2.92 ms: 1.37x faster                                      |
| pickle_dict             | 31.1 us                                                | 26.0 us: 1.20x faster                                      |
| pickle                  | 10.1 us                                                | 9.37 us: 1.07x faster                                      |
| json_loads              | 26.5 us                                                | 24.9 us: 1.07x faster                                      |
| gc_traversal            | 4.02 ms                                                | 3.79 ms: 1.06x faster                                      |
| logging_format          | 6.68 us                                                | 6.35 us: 1.05x faster                                      |
| regex_dna               | 204 ms                                                 | 194 ms: 1.05x faster                                       |
| gunicorn                | 1.18 ms                                                | 1.12 ms: 1.05x faster                                      |
| float                   | 77.2 ms                                                | 73.9 ms: 1.05x faster                                      |
| json                    | 4.94 ms                                                | 4.74 ms: 1.04x faster                                      |
| asyncio_tcp             | 922 ms                                                 | 888 ms: 1.04x faster                                       |
| aiohttp                 | 1.10 ms                                                | 1.06 ms: 1.04x faster                                      |
| async_generators        | 368 ms                                                 | 356 ms: 1.04x faster                                       |
| logging_simple          | 6.03 us                                                | 5.82 us: 1.04x faster                                      |
| scimark_sor             | 118 ms                                                 | 114 ms: 1.03x faster                                       |
| sympy_sum               | 167 ms                                                 | 162 ms: 1.03x faster                                       |
| regex_v8                | 22.0 ms                                                | 21.4 ms: 1.03x faster                                      |
| html5lib                | 64.5 ms                                                | 62.8 ms: 1.03x faster                                      |
| docutils                | 2.63 sec                                               | 2.56 sec: 1.03x faster                                     |
| spectral_norm           | 100 ms                                                 | 97.5 ms: 1.03x faster                                      |
| pyflate                 | 418 ms                                                 | 409 ms: 1.02x faster                                       |
| scimark_monte_carlo     | 68.1 ms                                                | 66.6 ms: 1.02x faster                                      |
| scimark_lu              | 110 ms                                                 | 107 ms: 1.02x faster                                       |
| pidigits                | 198 ms                                                 | 194 ms: 1.02x faster                                       |
| meteor_contest          | 107 ms                                                 | 105 ms: 1.02x faster                                       |
| sympy_str               | 290 ms                                                 | 285 ms: 1.02x faster                                       |
| tornado_http            | 96.3 ms                                                | 94.7 ms: 1.02x faster                                      |
| pickle_pure_python      | 306 us                                                 | 301 us: 1.02x faster                                       |
| raytrace                | 297 ms                                                 | 292 ms: 1.02x faster                                       |
| chaos                   | 69.2 ms                                                | 68.2 ms: 1.01x faster                                      |
| crypto_pyaes            | 74.7 ms                                                | 73.6 ms: 1.01x faster                                      |
| regex_compile           | 138 ms                                                 | 136 ms: 1.01x faster                                       |
| sympy_integrate         | 21.0 ms                                                | 20.7 ms: 1.01x faster                                      |
| sympy_expand            | 475 ms                                                 | 469 ms: 1.01x faster                                       |
| flaskblogging           | 7.12 ms                                                | 7.04 ms: 1.01x faster                                      |
| pprint_safe_repr        | 701 ms                                                 | 694 ms: 1.01x faster                                       |
| dulwich_log             | 63.7 ms                                                | 63.0 ms: 1.01x faster                                      |
| 2to3                    | 259 ms                                                 | 256 ms: 1.01x faster                                       |
| sqlalchemy_declarative  | 138 ms                                                 | 137 ms: 1.01x faster                                       |
| mako                    | 10.1 ms                                                | 9.99 ms: 1.01x faster                                      |
| chameleon               | 6.47 ms                                                | 6.42 ms: 1.01x faster                                      |
| pprint_pformat          | 1.46 sec                                               | 1.45 sec: 1.01x faster                                     |
| deepcopy                | 342 us                                                 | 340 us: 1.01x faster                                       |
| pathlib                 | 18.2 ms                                                | 18.1 ms: 1.01x faster                                      |
| deltablue               | 3.67 ms                                                | 3.65 ms: 1.01x faster                                      |
| async_tree_cpu_io_mixed | 739 ms                                                 | 735 ms: 1.01x faster                                       |
| xml_etree_process       | 53.9 ms                                                | 53.6 ms: 1.01x faster                                      |
| go                      | 140 ms                                                 | 139 ms: 1.00x faster                                       |
| unpickle_pure_python    | 228 us                                                 | 227 us: 1.00x faster                                       |
| bench_thread_pool       | 819 us                                                 | 816 us: 1.00x faster                                       |
| python_startup          | 8.52 ms                                                | 8.51 ms: 1.00x faster                                      |
| python_startup_no_site  | 6.01 ms                                                | 6.01 ms: 1.00x faster                                      |
| generators              | 73.5 ms                                                | 73.8 ms: 1.00x slower                                      |
| async_tree_io           | 1.30 sec                                               | 1.30 sec: 1.00x slower                                     |
| json_dumps              | 12.6 ms                                                | 12.7 ms: 1.01x slower                                      |
| nqueens                 | 83.4 ms                                                | 83.8 ms: 1.01x slower                                      |
| xml_etree_generate      | 76.2 ms                                                | 76.7 ms: 1.01x slower                                      |
| thrift                  | 756 us                                                 | 763 us: 1.01x slower                                       |
| unpickle_list           | 4.91 us                                                | 4.96 us: 1.01x slower                                      |
| genshi_xml              | 51.8 ms                                                | 52.3 ms: 1.01x slower                                      |
| fannkuch                | 388 ms                                                 | 393 ms: 1.01x slower                                       |
| sqlglot_normalize       | 108 ms                                                 | 109 ms: 1.01x slower                                       |
| django_template         | 32.6 ms                                                | 33.0 ms: 1.01x slower                                      |
| async_tree_memoization  | 627 ms                                                 | 636 ms: 1.01x slower                                       |
| create_gc_cycles        | 1.49 ms                                                | 1.51 ms: 1.01x slower                                      |
| deepcopy_reduce         | 2.94 us                                                | 2.98 us: 1.02x slower                                      |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.57 ms: 1.02x slower                                      |
| sqlglot_optimize        | 53.1 ms                                                | 54.0 ms: 1.02x slower                                      |
| nbody                   | 93.1 ms                                                | 94.9 ms: 1.02x slower                                      |
| coroutines              | 25.5 ms                                                | 26.0 ms: 1.02x slower                                      |
| dask                    | 360 ms                                                 | 368 ms: 1.02x slower                                       |
| genshi_text             | 21.6 ms                                                | 22.0 ms: 1.02x slower                                      |
| djangocms               | 32.4 us                                                | 33.2 us: 1.02x slower                                      |
| mdp                     | 2.62 sec                                               | 2.69 sec: 1.03x slower                                     |
| xml_etree_iterparse     | 104 ms                                                 | 108 ms: 1.04x slower                                       |
| pickle_list             | 4.11 us                                                | 4.27 us: 1.04x slower                                      |
| unpack_sequence         | 43.1 ns                                                | 48.0 ns: 1.11x slower                                      |
| comprehensions          | 22.4 us                                                | 25.9 us: 1.16x slower                                      |
| sqlglot_transpile       | 1.70 ms                                                | 2.04 ms: 1.20x slower                                      |
| sqlglot_parse           | 1.40 ms                                                | 1.75 ms: 1.25x slower                                      |
| Geometric mean          | (ref)                                                  | 1.01x faster                                               |

Benchmark hidden because not significant (15): unpickle, richards, pycparser, sqlalchemy_imperative, deepcopy_memo, async_tree_none, mypy2, hexiom, xml_etree_parse, bench_mp_pool, scimark_fft, pylint, telco, logging_silent, sqlite_synth
Ignored benchmarks (5) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, coverage, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 99.88% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x
