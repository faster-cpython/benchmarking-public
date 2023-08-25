
# Results vs. 3.11.0

- fork: faster-cpython
- ref: pep_669_incremental
- machine: linux-x86_64
- commit hash: 825f42a
- commit date: 2023-02-09
- overall geometric mean: 1.05x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230209-linux-x86_64-faster%2dcpython-pep_669_incremental-3.12.0a5+-825f42a |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 246 ms: 1.05x faster                                                            |
| chameleon      | 6.47 ms                                                | 6.23 ms: 1.04x faster                                                           |
| docutils       | 2.63 sec                                               | 2.49 sec: 1.06x faster                                                          |
| html5lib       | 64.5 ms                                                | 58.7 ms: 1.10x faster                                                           |
| tornado_http   | 96.3 ms                                                | 92.8 ms: 1.04x faster                                                           |
| Geometric mean | (ref)                                                  | 1.06x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230209-linux-x86_64-faster%2dcpython-pep_669_incremental-3.12.0a5+-825f42a |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 77.2 ms                                                | 71.4 ms: 1.08x faster                                                           |
| pidigits       | 198 ms                                                 | 192 ms: 1.03x faster                                                            |
| nbody          | 93.1 ms                                                | 90.7 ms: 1.03x faster                                                           |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230209-linux-x86_64-faster%2dcpython-pep_669_incremental-3.12.0a5+-825f42a |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.57 ms: 1.12x faster                                                           |
| regex_compile  | 138 ms                                                 | 124 ms: 1.11x faster                                                            |
| regex_dna      | 204 ms                                                 | 201 ms: 1.01x faster                                                            |
| regex_v8       | 22.0 ms                                                | 21.8 ms: 1.01x faster                                                           |
| Geometric mean | (ref)                                                  | 1.06x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230209-linux-x86_64-faster%2dcpython-pep_669_incremental-3.12.0a5+-825f42a |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.44 ms: 1.33x faster                                                           |
| unpickle_pure_python | 228 us                                                 | 194 us: 1.18x faster                                                            |
| json_loads           | 26.5 us                                                | 23.7 us: 1.12x faster                                                           |
| pickle_pure_python   | 306 us                                                 | 279 us: 1.10x faster                                                            |
| xml_etree_parse      | 158 ms                                                 | 148 ms: 1.07x faster                                                            |
| pickle_dict          | 31.1 us                                                | 29.4 us: 1.06x faster                                                           |
| xml_etree_iterparse  | 104 ms                                                 | 100 ms: 1.03x faster                                                            |
| pickle_list          | 4.11 us                                                | 4.04 us: 1.02x faster                                                           |
| xml_etree_process    | 53.9 ms                                                | 55.1 ms: 1.02x slower                                                           |
| xml_etree_generate   | 76.2 ms                                                | 79.6 ms: 1.04x slower                                                           |
| unpickle_list        | 4.91 us                                                | 5.15 us: 1.05x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                                    |

Benchmark hidden because not significant (2): unpickle, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230209-linux-x86_64-faster%2dcpython-pep_669_incremental-3.12.0a5+-825f42a |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.94 ms: 1.05x slower                                                           |
| python_startup_no_site | 6.01 ms                                                | 6.50 ms: 1.08x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230209-linux-x86_64-faster%2dcpython-pep_669_incremental-3.12.0a5+-825f42a |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 45.5 ms: 1.14x faster                                                           |
| genshi_text     | 21.6 ms                                                | 20.5 ms: 1.05x faster                                                           |
| mako            | 10.1 ms                                                | 9.79 ms: 1.03x faster                                                           |
| django_template | 32.6 ms                                                | 32.2 ms: 1.01x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.06x faster                                                                    |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230209-linux-x86_64-faster%2dcpython-pep_669_incremental-3.12.0a5+-825f42a |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| asyncio_tcp             | 922 ms                                                 | 504 ms: 1.83x faster                                                            |
| generators              | 73.5 ms                                                | 54.8 ms: 1.34x faster                                                           |
| json_dumps              | 12.6 ms                                                | 9.44 ms: 1.33x faster                                                           |
| mypy2                   | 420 ms                                                 | 322 ms: 1.31x faster                                                            |
| deltablue               | 3.67 ms                                                | 3.11 ms: 1.18x faster                                                           |
| unpickle_pure_python    | 228 us                                                 | 194 us: 1.18x faster                                                            |
| scimark_sor             | 118 ms                                                 | 102 ms: 1.16x faster                                                            |
| scimark_sparse_mat_mult | 4.50 ms                                                | 3.92 ms: 1.15x faster                                                           |
| genshi_xml              | 51.8 ms                                                | 45.5 ms: 1.14x faster                                                           |
| aiohttp                 | 1.10 ms                                                | 983 us: 1.12x faster                                                            |
| regex_effbot            | 3.99 ms                                                | 3.57 ms: 1.12x faster                                                           |
| gunicorn                | 1.18 ms                                                | 1.05 ms: 1.12x faster                                                           |
| json_loads              | 26.5 us                                                | 23.7 us: 1.12x faster                                                           |
| regex_compile           | 138 ms                                                 | 124 ms: 1.11x faster                                                            |
| deepcopy_memo           | 37.0 us                                                | 33.3 us: 1.11x faster                                                           |
| richards                | 45.7 ms                                                | 41.2 ms: 1.11x faster                                                           |
| chaos                   | 69.2 ms                                                | 62.6 ms: 1.11x faster                                                           |
| nqueens                 | 83.4 ms                                                | 75.5 ms: 1.10x faster                                                           |
| hexiom                  | 6.37 ms                                                | 5.79 ms: 1.10x faster                                                           |
| html5lib                | 64.5 ms                                                | 58.7 ms: 1.10x faster                                                           |
| scimark_fft             | 328 ms                                                 | 299 ms: 1.10x faster                                                            |
| pickle_pure_python      | 306 us                                                 | 279 us: 1.10x faster                                                            |
| pycparser               | 1.18 sec                                               | 1.08 sec: 1.09x faster                                                          |
| sympy_str               | 290 ms                                                 | 265 ms: 1.09x faster                                                            |
| go                      | 140 ms                                                 | 129 ms: 1.09x faster                                                            |
| logging_silent          | 101 ns                                                 | 93.1 ns: 1.09x faster                                                           |
| json                    | 4.94 ms                                                | 4.56 ms: 1.08x faster                                                           |
| float                   | 77.2 ms                                                | 71.4 ms: 1.08x faster                                                           |
| sympy_sum               | 167 ms                                                 | 155 ms: 1.08x faster                                                            |
| raytrace                | 297 ms                                                 | 276 ms: 1.08x faster                                                            |
| sympy_integrate         | 21.0 ms                                                | 19.5 ms: 1.08x faster                                                           |
| fannkuch                | 388 ms                                                 | 361 ms: 1.07x faster                                                            |
| spectral_norm           | 100 ms                                                 | 93.3 ms: 1.07x faster                                                           |
| scimark_lu              | 110 ms                                                 | 103 ms: 1.07x faster                                                            |
| xml_etree_parse         | 158 ms                                                 | 148 ms: 1.07x faster                                                            |
| logging_simple          | 6.03 us                                                | 5.65 us: 1.07x faster                                                           |
| logging_format          | 6.68 us                                                | 6.26 us: 1.07x faster                                                           |
| scimark_monte_carlo     | 68.1 ms                                                | 63.8 ms: 1.07x faster                                                           |
| sqlglot_optimize        | 53.1 ms                                                | 49.8 ms: 1.07x faster                                                           |
| deepcopy                | 342 us                                                 | 321 us: 1.07x faster                                                            |
| sympy_expand            | 475 ms                                                 | 446 ms: 1.06x faster                                                            |
| bench_thread_pool       | 819 us                                                 | 771 us: 1.06x faster                                                            |
| pickle_dict             | 31.1 us                                                | 29.4 us: 1.06x faster                                                           |
| pprint_pformat          | 1.46 sec                                               | 1.38 sec: 1.06x faster                                                          |
| gc_traversal            | 4.02 ms                                                | 3.80 ms: 1.06x faster                                                           |
| sqlglot_normalize       | 108 ms                                                 | 102 ms: 1.06x faster                                                            |
| docutils                | 2.63 sec                                               | 2.49 sec: 1.06x faster                                                          |
| 2to3                    | 259 ms                                                 | 246 ms: 1.05x faster                                                            |
| genshi_text             | 21.6 ms                                                | 20.5 ms: 1.05x faster                                                           |
| pprint_safe_repr        | 701 ms                                                 | 668 ms: 1.05x faster                                                            |
| chameleon               | 6.47 ms                                                | 6.23 ms: 1.04x faster                                                           |
| tornado_http            | 96.3 ms                                                | 92.8 ms: 1.04x faster                                                           |
| telco                   | 6.58 ms                                                | 6.35 ms: 1.04x faster                                                           |
| sqlalchemy_imperative   | 17.9 ms                                                | 17.3 ms: 1.04x faster                                                           |
| crypto_pyaes            | 74.7 ms                                                | 72.1 ms: 1.04x faster                                                           |
| dulwich_log             | 63.7 ms                                                | 61.5 ms: 1.03x faster                                                           |
| xml_etree_iterparse     | 104 ms                                                 | 100 ms: 1.03x faster                                                            |
| meteor_contest          | 107 ms                                                 | 103 ms: 1.03x faster                                                            |
| sqlalchemy_declarative  | 138 ms                                                 | 134 ms: 1.03x faster                                                            |
| unpack_sequence         | 43.1 ns                                                | 41.8 ns: 1.03x faster                                                           |
| mako                    | 10.1 ms                                                | 9.79 ms: 1.03x faster                                                           |
| deepcopy_reduce         | 2.94 us                                                | 2.86 us: 1.03x faster                                                           |
| pidigits                | 198 ms                                                 | 192 ms: 1.03x faster                                                            |
| nbody                   | 93.1 ms                                                | 90.7 ms: 1.03x faster                                                           |
| coverage                | 100 ms                                                 | 97.7 ms: 1.02x faster                                                           |
| pathlib                 | 18.2 ms                                                | 17.8 ms: 1.02x faster                                                           |
| pyflate                 | 418 ms                                                 | 410 ms: 1.02x faster                                                            |
| pickle_list             | 4.11 us                                                | 4.04 us: 1.02x faster                                                           |
| regex_dna               | 204 ms                                                 | 201 ms: 1.01x faster                                                            |
| django_template         | 32.6 ms                                                | 32.2 ms: 1.01x faster                                                           |
| create_gc_cycles        | 1.49 ms                                                | 1.47 ms: 1.01x faster                                                           |
| regex_v8                | 22.0 ms                                                | 21.8 ms: 1.01x faster                                                           |
| sqlglot_transpile       | 1.70 ms                                                | 1.69 ms: 1.01x faster                                                           |
| thrift                  | 756 us                                                 | 762 us: 1.01x slower                                                            |
| mdp                     | 2.62 sec                                               | 2.67 sec: 1.02x slower                                                          |
| xml_etree_process       | 53.9 ms                                                | 55.1 ms: 1.02x slower                                                           |
| sqlite_synth            | 2.52 us                                                | 2.58 us: 1.02x slower                                                           |
| async_tree_memoization  | 627 ms                                                 | 643 ms: 1.02x slower                                                            |
| async_tree_io           | 1.30 sec                                               | 1.34 sec: 1.03x slower                                                          |
| async_tree_cpu_io_mixed | 739 ms                                                 | 767 ms: 1.04x slower                                                            |
| xml_etree_generate      | 76.2 ms                                                | 79.6 ms: 1.04x slower                                                           |
| python_startup          | 8.52 ms                                                | 8.94 ms: 1.05x slower                                                           |
| unpickle_list           | 4.91 us                                                | 5.15 us: 1.05x slower                                                           |
| python_startup_no_site  | 6.01 ms                                                | 6.50 ms: 1.08x slower                                                           |
| async_generators        | 368 ms                                                 | 420 ms: 1.14x slower                                                            |
| coroutines              | 25.5 ms                                                | 54.8 ms: 2.15x slower                                                           |
| Geometric mean          | (ref)                                                  | 1.05x faster                                                                    |

Benchmark hidden because not significant (6): unpickle, djangocms, pickle, bench_mp_pool, sqlglot_parse, async_tree_none
Ignored benchmarks (8) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, comprehensions, dask, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.03x
