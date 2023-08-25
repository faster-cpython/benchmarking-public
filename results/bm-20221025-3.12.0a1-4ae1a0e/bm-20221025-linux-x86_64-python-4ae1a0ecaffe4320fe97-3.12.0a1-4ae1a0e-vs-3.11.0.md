
# Results vs. 3.11.0

- fork: python
- ref: 4ae1a0ecaffe4320fe97
- machine: linux-x86_64
- commit hash: 4ae1a0e
- commit date: 2022-10-25
- overall geometric mean: 1.04x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221025-linux-x86_64-python-4ae1a0ecaffe4320fe97-3.12.0a1-4ae1a0e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 249 ms: 1.04x faster                                                  |
| chameleon      | 6.47 ms                                                | 6.51 ms: 1.01x slower                                                 |
| docutils       | 2.63 sec                                               | 2.52 sec: 1.04x faster                                                |
| html5lib       | 64.5 ms                                                | 59.9 ms: 1.08x faster                                                 |
| tornado_http   | 96.3 ms                                                | 93.7 ms: 1.03x faster                                                 |
| Geometric mean | (ref)                                                  | 1.04x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221025-linux-x86_64-python-4ae1a0ecaffe4320fe97-3.12.0a1-4ae1a0e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 77.2 ms                                                | 71.4 ms: 1.08x faster                                                 |
| pidigits       | 198 ms                                                 | 198 ms: 1.00x faster                                                  |
| nbody          | 93.1 ms                                                | 96.6 ms: 1.04x slower                                                 |
| Geometric mean | (ref)                                                  | 1.01x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221025-linux-x86_64-python-4ae1a0ecaffe4320fe97-3.12.0a1-4ae1a0e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.37 ms: 1.18x faster                                                 |
| regex_compile  | 138 ms                                                 | 127 ms: 1.08x faster                                                  |
| regex_v8       | 22.0 ms                                                | 21.4 ms: 1.03x faster                                                 |
| regex_dna      | 204 ms                                                 | 201 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.08x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221025-linux-x86_64-python-4ae1a0ecaffe4320fe97-3.12.0a1-4ae1a0e |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.36 ms: 1.34x faster                                                 |
| unpickle_pure_python | 228 us                                                 | 202 us: 1.13x faster                                                  |
| json_loads           | 26.5 us                                                | 23.5 us: 1.13x faster                                                 |
| xml_etree_parse      | 158 ms                                                 | 145 ms: 1.09x faster                                                  |
| pickle_pure_python   | 306 us                                                 | 285 us: 1.07x faster                                                  |
| unpickle             | 13.7 us                                                | 13.2 us: 1.04x faster                                                 |
| xml_etree_iterparse  | 104 ms                                                 | 101 ms: 1.03x faster                                                  |
| xml_etree_process    | 53.9 ms                                                | 53.4 ms: 1.01x faster                                                 |
| xml_etree_generate   | 76.2 ms                                                | 76.0 ms: 1.00x faster                                                 |
| pickle_list          | 4.11 us                                                | 4.19 us: 1.02x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                          |

Benchmark hidden because not significant (3): pickle_dict, unpickle_list, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221025-linux-x86_64-python-4ae1a0ecaffe4320fe97-3.12.0a1-4ae1a0e |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 6.01 ms                                                | 5.93 ms: 1.01x faster                                                 |
| python_startup         | 8.52 ms                                                | 8.42 ms: 1.01x faster                                                 |
| Geometric mean         | (ref)                                                  | 1.01x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221025-linux-x86_64-python-4ae1a0ecaffe4320fe97-3.12.0a1-4ae1a0e |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 10.1 ms                                                | 9.64 ms: 1.05x faster                                                 |
| genshi_xml      | 51.8 ms                                                | 50.0 ms: 1.04x faster                                                 |
| django_template | 32.6 ms                                                | 33.0 ms: 1.01x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                          |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221025-linux-x86_64-python-4ae1a0ecaffe4320fe97-3.12.0a1-4ae1a0e |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| json_dumps              | 12.6 ms                                                | 9.36 ms: 1.34x faster                                                 |
| mypy2                   | 420 ms                                                 | 328 ms: 1.28x faster                                                  |
| regex_effbot            | 3.99 ms                                                | 3.37 ms: 1.18x faster                                                 |
| gc_traversal            | 4.02 ms                                                | 3.55 ms: 1.13x faster                                                 |
| unpickle_pure_python    | 228 us                                                 | 202 us: 1.13x faster                                                  |
| json_loads              | 26.5 us                                                | 23.5 us: 1.13x faster                                                 |
| scimark_sor             | 118 ms                                                 | 106 ms: 1.12x faster                                                  |
| deltablue               | 3.67 ms                                                | 3.30 ms: 1.11x faster                                                 |
| logging_silent          | 101 ns                                                 | 91.6 ns: 1.10x faster                                                 |
| gunicorn                | 1.18 ms                                                | 1.07 ms: 1.10x faster                                                 |
| aiohttp                 | 1.10 ms                                                | 1.00 ms: 1.10x faster                                                 |
| xml_etree_parse         | 158 ms                                                 | 145 ms: 1.09x faster                                                  |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.13 ms: 1.09x faster                                                 |
| json                    | 4.94 ms                                                | 4.55 ms: 1.09x faster                                                 |
| regex_compile           | 138 ms                                                 | 127 ms: 1.08x faster                                                  |
| float                   | 77.2 ms                                                | 71.4 ms: 1.08x faster                                                 |
| richards                | 45.7 ms                                                | 42.4 ms: 1.08x faster                                                 |
| html5lib                | 64.5 ms                                                | 59.9 ms: 1.08x faster                                                 |
| deepcopy_memo           | 37.0 us                                                | 34.4 us: 1.08x faster                                                 |
| pickle_pure_python      | 306 us                                                 | 285 us: 1.07x faster                                                  |
| pprint_pformat          | 1.46 sec                                               | 1.38 sec: 1.06x faster                                                |
| pycparser               | 1.18 sec                                               | 1.12 sec: 1.06x faster                                                |
| async_generators        | 368 ms                                                 | 349 ms: 1.06x faster                                                  |
| pprint_safe_repr        | 701 ms                                                 | 665 ms: 1.06x faster                                                  |
| mdp                     | 2.62 sec                                               | 2.48 sec: 1.05x faster                                                |
| scimark_fft             | 328 ms                                                 | 312 ms: 1.05x faster                                                  |
| comprehensions          | 22.4 us                                                | 21.3 us: 1.05x faster                                                 |
| spectral_norm           | 100 ms                                                 | 95.2 ms: 1.05x faster                                                 |
| raytrace                | 297 ms                                                 | 282 ms: 1.05x faster                                                  |
| bench_thread_pool       | 819 us                                                 | 780 us: 1.05x faster                                                  |
| fannkuch                | 388 ms                                                 | 370 ms: 1.05x faster                                                  |
| logging_format          | 6.68 us                                                | 6.38 us: 1.05x faster                                                 |
| mako                    | 10.1 ms                                                | 9.64 ms: 1.05x faster                                                 |
| sqlglot_parse           | 1.40 ms                                                | 1.34 ms: 1.05x faster                                                 |
| docutils                | 2.63 sec                                               | 2.52 sec: 1.04x faster                                                |
| sympy_expand            | 475 ms                                                 | 455 ms: 1.04x faster                                                  |
| sqlglot_transpile       | 1.70 ms                                                | 1.63 ms: 1.04x faster                                                 |
| hexiom                  | 6.37 ms                                                | 6.11 ms: 1.04x faster                                                 |
| logging_simple          | 6.03 us                                                | 5.80 us: 1.04x faster                                                 |
| 2to3                    | 259 ms                                                 | 249 ms: 1.04x faster                                                  |
| unpickle                | 13.7 us                                                | 13.2 us: 1.04x faster                                                 |
| sqlglot_optimize        | 53.1 ms                                                | 51.2 ms: 1.04x faster                                                 |
| genshi_xml              | 51.8 ms                                                | 50.0 ms: 1.04x faster                                                 |
| asyncio_tcp             | 922 ms                                                 | 890 ms: 1.04x faster                                                  |
| go                      | 140 ms                                                 | 135 ms: 1.04x faster                                                  |
| coroutines              | 25.5 ms                                                | 24.7 ms: 1.03x faster                                                 |
| nqueens                 | 83.4 ms                                                | 80.7 ms: 1.03x faster                                                 |
| sqlglot_normalize       | 108 ms                                                 | 104 ms: 1.03x faster                                                  |
| xml_etree_iterparse     | 104 ms                                                 | 101 ms: 1.03x faster                                                  |
| regex_v8                | 22.0 ms                                                | 21.4 ms: 1.03x faster                                                 |
| chaos                   | 69.2 ms                                                | 67.1 ms: 1.03x faster                                                 |
| deepcopy                | 342 us                                                 | 333 us: 1.03x faster                                                  |
| pyflate                 | 418 ms                                                 | 407 ms: 1.03x faster                                                  |
| tornado_http            | 96.3 ms                                                | 93.7 ms: 1.03x faster                                                 |
| sympy_str               | 290 ms                                                 | 283 ms: 1.03x faster                                                  |
| sympy_integrate         | 21.0 ms                                                | 20.4 ms: 1.03x faster                                                 |
| meteor_contest          | 107 ms                                                 | 104 ms: 1.03x faster                                                  |
| scimark_monte_carlo     | 68.1 ms                                                | 66.6 ms: 1.02x faster                                                 |
| create_gc_cycles        | 1.49 ms                                                | 1.46 ms: 1.02x faster                                                 |
| dulwich_log             | 63.7 ms                                                | 62.4 ms: 1.02x faster                                                 |
| pathlib                 | 18.2 ms                                                | 17.9 ms: 1.02x faster                                                 |
| sympy_sum               | 167 ms                                                 | 164 ms: 1.02x faster                                                  |
| regex_dna               | 204 ms                                                 | 201 ms: 1.01x faster                                                  |
| thrift                  | 756 us                                                 | 746 us: 1.01x faster                                                  |
| python_startup_no_site  | 6.01 ms                                                | 5.93 ms: 1.01x faster                                                 |
| async_tree_cpu_io_mixed | 739 ms                                                 | 730 ms: 1.01x faster                                                  |
| python_startup          | 8.52 ms                                                | 8.42 ms: 1.01x faster                                                 |
| scimark_lu              | 110 ms                                                 | 108 ms: 1.01x faster                                                  |
| deepcopy_reduce         | 2.94 us                                                | 2.91 us: 1.01x faster                                                 |
| xml_etree_process       | 53.9 ms                                                | 53.4 ms: 1.01x faster                                                 |
| xml_etree_generate      | 76.2 ms                                                | 76.0 ms: 1.00x faster                                                 |
| pidigits                | 198 ms                                                 | 198 ms: 1.00x faster                                                  |
| chameleon               | 6.47 ms                                                | 6.51 ms: 1.01x slower                                                 |
| generators              | 73.5 ms                                                | 74.1 ms: 1.01x slower                                                 |
| django_template         | 32.6 ms                                                | 33.0 ms: 1.01x slower                                                 |
| coverage                | 100 ms                                                 | 102 ms: 1.01x slower                                                  |
| pickle_list             | 4.11 us                                                | 4.19 us: 1.02x slower                                                 |
| unpack_sequence         | 43.1 ns                                                | 44.1 ns: 1.02x slower                                                 |
| async_tree_io           | 1.30 sec                                               | 1.33 sec: 1.02x slower                                                |
| nbody                   | 93.1 ms                                                | 96.6 ms: 1.04x slower                                                 |
| sqlite_synth            | 2.52 us                                                | 2.62 us: 1.04x slower                                                 |
| async_tree_memoization  | 627 ms                                                 | 656 ms: 1.05x slower                                                  |
| Geometric mean          | (ref)                                                  | 1.04x faster                                                          |

Benchmark hidden because not significant (11): pylint, telco, genshi_text, pickle_dict, bench_mp_pool, dask, unpickle_list, crypto_pyaes, djangocms, async_tree_none, pickle
Ignored benchmarks (7) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, flaskblogging, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x
