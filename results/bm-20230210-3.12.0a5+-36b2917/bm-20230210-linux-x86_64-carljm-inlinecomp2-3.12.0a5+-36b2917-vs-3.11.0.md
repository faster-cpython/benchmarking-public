
# Results vs. 3.11.0

- fork: carljm
- ref: inlinecomp2
- machine: linux-x86_64
- commit hash: 36b2917
- commit date: 2023-02-10
- overall geometric mean: 1.04x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230210-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-36b2917 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 251 ms: 1.03x faster                                          |
| chameleon      | 6.38 ms                                                | 6.47 ms: 1.01x slower                                         |
| docutils       | 2.60 sec                                               | 2.53 sec: 1.03x faster                                        |
| html5lib       | 64.8 ms                                                | 60.6 ms: 1.07x faster                                         |
| tornado_http   | 96.5 ms                                                | 94.1 ms: 1.03x faster                                         |
| Geometric mean | (ref)                                                  | 1.03x faster                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230210-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-36b2917 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| float          | 76.8 ms                                                | 72.8 ms: 1.05x faster                                         |
| pidigits       | 197 ms                                                 | 193 ms: 1.02x faster                                          |
| nbody          | 90.0 ms                                                | 94.0 ms: 1.04x slower                                         |
| Geometric mean | (ref)                                                  | 1.01x faster                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230210-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-36b2917 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 128 ms: 1.07x faster                                          |
| regex_v8       | 22.2 ms                                                | 21.6 ms: 1.03x faster                                         |
| regex_dna      | 203 ms                                                 | 205 ms: 1.01x slower                                          |
| regex_effbot   | 3.46 ms                                                | 3.66 ms: 1.06x slower                                         |
| Geometric mean | (ref)                                                  | 1.01x faster                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230210-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-36b2917 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.39 ms: 1.32x faster                                         |
| unpickle_pure_python | 227 us                                                 | 198 us: 1.14x faster                                          |
| json_loads           | 26.1 us                                                | 23.7 us: 1.10x faster                                         |
| xml_etree_parse      | 160 ms                                                 | 148 ms: 1.09x faster                                          |
| pickle_pure_python   | 308 us                                                 | 291 us: 1.06x faster                                          |
| xml_etree_iterparse  | 104 ms                                                 | 103 ms: 1.01x faster                                          |
| pickle_dict          | 31.2 us                                                | 30.9 us: 1.01x faster                                         |
| xml_etree_process    | 53.7 ms                                                | 54.8 ms: 1.02x slower                                         |
| pickle               | 9.90 us                                                | 10.1 us: 1.02x slower                                         |
| unpickle_list        | 4.99 us                                                | 5.13 us: 1.03x slower                                         |
| xml_etree_generate   | 75.9 ms                                                | 80.2 ms: 1.06x slower                                         |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                  |

Benchmark hidden because not significant (2): pickle_list, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230210-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-36b2917 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.90 ms: 1.04x slower                                         |
| python_startup_no_site | 6.04 ms                                                | 6.46 ms: 1.07x slower                                         |
| Geometric mean         | (ref)                                                  | 1.05x slower                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230210-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-36b2917 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 47.8 ms: 1.08x faster                                         |
| genshi_text     | 21.5 ms                                                | 20.9 ms: 1.03x faster                                         |
| mako            | 9.83 ms                                                | 9.90 ms: 1.01x slower                                         |
| django_template | 32.3 ms                                                | 32.6 ms: 1.01x slower                                         |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                  |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230210-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-36b2917 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| asyncio_tcp             | 883 ms                                                 | 498 ms: 1.77x faster                                          |
| json_dumps              | 12.4 ms                                                | 9.39 ms: 1.32x faster                                         |
| mypy2                   | 420 ms                                                 | 322 ms: 1.30x faster                                          |
| deltablue               | 3.66 ms                                                | 3.13 ms: 1.17x faster                                         |
| scimark_sparse_mat_mult | 4.59 ms                                                | 3.94 ms: 1.16x faster                                         |
| unpickle_pure_python    | 227 us                                                 | 198 us: 1.14x faster                                          |
| nqueens                 | 83.8 ms                                                | 74.9 ms: 1.12x faster                                         |
| json_loads              | 26.1 us                                                | 23.7 us: 1.10x faster                                         |
| sympy_str               | 291 ms                                                 | 265 ms: 1.10x faster                                          |
| richards                | 46.1 ms                                                | 42.1 ms: 1.10x faster                                         |
| pycparser               | 1.19 sec                                               | 1.09 sec: 1.09x faster                                        |
| chaos                   | 68.7 ms                                                | 63.2 ms: 1.09x faster                                         |
| xml_etree_parse         | 160 ms                                                 | 148 ms: 1.09x faster                                          |
| sympy_expand            | 475 ms                                                 | 439 ms: 1.08x faster                                          |
| scimark_sor             | 115 ms                                                 | 106 ms: 1.08x faster                                          |
| hexiom                  | 6.34 ms                                                | 5.87 ms: 1.08x faster                                         |
| sympy_integrate         | 21.0 ms                                                | 19.5 ms: 1.08x faster                                         |
| genshi_xml              | 51.4 ms                                                | 47.8 ms: 1.08x faster                                         |
| html5lib                | 64.8 ms                                                | 60.6 ms: 1.07x faster                                         |
| json                    | 4.87 ms                                                | 4.55 ms: 1.07x faster                                         |
| regex_compile           | 136 ms                                                 | 128 ms: 1.07x faster                                          |
| sympy_sum               | 166 ms                                                 | 155 ms: 1.07x faster                                          |
| gc_traversal            | 3.82 ms                                                | 3.58 ms: 1.07x faster                                         |
| sqlglot_normalize       | 108 ms                                                 | 101 ms: 1.06x faster                                          |
| pprint_pformat          | 1.46 sec                                               | 1.37 sec: 1.06x faster                                        |
| scimark_fft             | 325 ms                                                 | 307 ms: 1.06x faster                                          |
| pickle_pure_python      | 308 us                                                 | 291 us: 1.06x faster                                          |
| async_tree_none         | 526 ms                                                 | 498 ms: 1.06x faster                                          |
| pprint_safe_repr        | 706 ms                                                 | 668 ms: 1.06x faster                                          |
| deepcopy                | 341 us                                                 | 324 us: 1.06x faster                                          |
| float                   | 76.8 ms                                                | 72.8 ms: 1.05x faster                                         |
| deepcopy_memo           | 35.8 us                                                | 34.1 us: 1.05x faster                                         |
| fannkuch                | 384 ms                                                 | 366 ms: 1.05x faster                                          |
| raytrace                | 291 ms                                                 | 279 ms: 1.05x faster                                          |
| spectral_norm           | 98.1 ms                                                | 93.9 ms: 1.05x faster                                         |
| sqlglot_optimize        | 52.7 ms                                                | 50.4 ms: 1.05x faster                                         |
| aiohttp                 | 1.05 ms                                                | 1.01 ms: 1.04x faster                                         |
| logging_silent          | 98.0 ns                                                | 94.1 ns: 1.04x faster                                         |
| deepcopy_reduce         | 3.02 us                                                | 2.90 us: 1.04x faster                                         |
| bench_thread_pool       | 817 us                                                 | 785 us: 1.04x faster                                          |
| gunicorn                | 1.12 ms                                                | 1.07 ms: 1.04x faster                                         |
| pyflate                 | 419 ms                                                 | 403 ms: 1.04x faster                                          |
| sqlalchemy_imperative   | 18.1 ms                                                | 17.4 ms: 1.04x faster                                         |
| scimark_monte_carlo     | 68.0 ms                                                | 65.5 ms: 1.04x faster                                         |
| crypto_pyaes            | 75.7 ms                                                | 73.3 ms: 1.03x faster                                         |
| logging_simple          | 6.02 us                                                | 5.83 us: 1.03x faster                                         |
| 2to3                    | 259 ms                                                 | 251 ms: 1.03x faster                                          |
| pathlib                 | 18.1 ms                                                | 17.5 ms: 1.03x faster                                         |
| regex_v8                | 22.2 ms                                                | 21.6 ms: 1.03x faster                                         |
| sqlalchemy_declarative  | 138 ms                                                 | 134 ms: 1.03x faster                                          |
| docutils                | 2.60 sec                                               | 2.53 sec: 1.03x faster                                        |
| genshi_text             | 21.5 ms                                                | 20.9 ms: 1.03x faster                                         |
| create_gc_cycles        | 1.52 ms                                                | 1.48 ms: 1.03x faster                                         |
| tornado_http            | 96.5 ms                                                | 94.1 ms: 1.03x faster                                         |
| pidigits                | 197 ms                                                 | 193 ms: 1.02x faster                                          |
| go                      | 140 ms                                                 | 137 ms: 1.02x faster                                          |
| dulwich_log             | 64.0 ms                                                | 62.6 ms: 1.02x faster                                         |
| async_tree_io           | 1.30 sec                                               | 1.27 sec: 1.02x faster                                        |
| async_tree_memoization  | 624 ms                                                 | 612 ms: 1.02x faster                                          |
| coroutines              | 26.2 ms                                                | 25.8 ms: 1.02x faster                                         |
| xml_etree_iterparse     | 104 ms                                                 | 103 ms: 1.01x faster                                          |
| logging_format          | 6.48 us                                                | 6.39 us: 1.01x faster                                         |
| pickle_dict             | 31.2 us                                                | 30.9 us: 1.01x faster                                         |
| mako                    | 9.83 ms                                                | 9.90 ms: 1.01x slower                                         |
| django_template         | 32.3 ms                                                | 32.6 ms: 1.01x slower                                         |
| regex_dna               | 203 ms                                                 | 205 ms: 1.01x slower                                          |
| mdp                     | 2.63 sec                                               | 2.66 sec: 1.01x slower                                        |
| chameleon               | 6.38 ms                                                | 6.47 ms: 1.01x slower                                         |
| async_tree_cpu_io_mixed | 736 ms                                                 | 747 ms: 1.02x slower                                          |
| xml_etree_process       | 53.7 ms                                                | 54.8 ms: 1.02x slower                                         |
| pickle                  | 9.90 us                                                | 10.1 us: 1.02x slower                                         |
| unpickle_list           | 4.99 us                                                | 5.13 us: 1.03x slower                                         |
| sqlglot_transpile       | 1.65 ms                                                | 1.71 ms: 1.03x slower                                         |
| python_startup          | 8.58 ms                                                | 8.90 ms: 1.04x slower                                         |
| sqlglot_parse           | 1.36 ms                                                | 1.41 ms: 1.04x slower                                         |
| sqlite_synth            | 2.48 us                                                | 2.58 us: 1.04x slower                                         |
| nbody                   | 90.0 ms                                                | 94.0 ms: 1.04x slower                                         |
| xml_etree_generate      | 75.9 ms                                                | 80.2 ms: 1.06x slower                                         |
| generators              | 73.5 ms                                                | 77.7 ms: 1.06x slower                                         |
| regex_effbot            | 3.46 ms                                                | 3.66 ms: 1.06x slower                                         |
| python_startup_no_site  | 6.04 ms                                                | 6.46 ms: 1.07x slower                                         |
| async_generators        | 356 ms                                                 | 427 ms: 1.20x slower                                          |
| Geometric mean          | (ref)                                                  | 1.04x faster                                                  |

Benchmark hidden because not significant (10): meteor_contest, telco, unpack_sequence, djangocms, bench_mp_pool, coverage, scimark_lu, thrift, pickle_list, unpickle
Ignored benchmarks (3) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: dask, flaskblogging, pylint
