
# Results vs. 3.11.0

- fork: carljm
- ref: inlinecomp2
- machine: linux-x86_64
- commit hash: ae0bd02
- commit date: 2023-02-13
- overall geometric mean: 1.05x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230213-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-ae0bd02 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 245 ms: 1.06x faster                                          |
| chameleon      | 6.38 ms                                                | 6.44 ms: 1.01x slower                                         |
| docutils       | 2.60 sec                                               | 2.54 sec: 1.02x faster                                        |
| html5lib       | 64.8 ms                                                | 60.8 ms: 1.07x faster                                         |
| tornado_http   | 96.5 ms                                                | 94.9 ms: 1.02x faster                                         |
| Geometric mean | (ref)                                                  | 1.03x faster                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230213-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-ae0bd02 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| float          | 76.8 ms                                                | 72.7 ms: 1.06x faster                                         |
| pidigits       | 197 ms                                                 | 189 ms: 1.04x faster                                          |
| nbody          | 90.0 ms                                                | 99.9 ms: 1.11x slower                                         |
| Geometric mean | (ref)                                                  | 1.00x slower                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230213-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-ae0bd02 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 129 ms: 1.06x faster                                          |
| regex_dna      | 203 ms                                                 | 200 ms: 1.02x faster                                          |
| regex_v8       | 22.2 ms                                                | 21.9 ms: 1.01x faster                                         |
| regex_effbot   | 3.46 ms                                                | 3.50 ms: 1.01x slower                                         |
| Geometric mean | (ref)                                                  | 1.02x faster                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230213-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-ae0bd02 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.51 ms: 1.30x faster                                         |
| unpickle_pure_python | 227 us                                                 | 200 us: 1.14x faster                                          |
| xml_etree_parse      | 160 ms                                                 | 148 ms: 1.08x faster                                          |
| json_loads           | 26.1 us                                                | 24.2 us: 1.08x faster                                         |
| pickle_pure_python   | 308 us                                                 | 286 us: 1.08x faster                                          |
| xml_etree_iterparse  | 104 ms                                                 | 99.8 ms: 1.04x faster                                         |
| pickle_dict          | 31.2 us                                                | 30.7 us: 1.01x faster                                         |
| unpickle_list        | 4.99 us                                                | 5.04 us: 1.01x slower                                         |
| pickle               | 9.90 us                                                | 10.0 us: 1.01x slower                                         |
| xml_etree_process    | 53.7 ms                                                | 55.2 ms: 1.03x slower                                         |
| xml_etree_generate   | 75.9 ms                                                | 80.4 ms: 1.06x slower                                         |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                  |

Benchmark hidden because not significant (2): unpickle, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230213-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-ae0bd02 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.89 ms: 1.04x slower                                         |
| python_startup_no_site | 6.04 ms                                                | 6.45 ms: 1.07x slower                                         |
| Geometric mean         | (ref)                                                  | 1.05x slower                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230213-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-ae0bd02 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 46.8 ms: 1.10x faster                                         |
| genshi_text     | 21.5 ms                                                | 20.8 ms: 1.03x faster                                         |
| mako            | 9.83 ms                                                | 10.0 ms: 1.02x slower                                         |
| django_template | 32.3 ms                                                | 33.3 ms: 1.03x slower                                         |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                  |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230213-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-ae0bd02 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 30.6 ms: 2.40x faster                                         |
| asyncio_tcp             | 883 ms                                                 | 502 ms: 1.76x faster                                          |
| json_dumps              | 12.4 ms                                                | 9.51 ms: 1.30x faster                                         |
| mypy2                   | 420 ms                                                 | 325 ms: 1.29x faster                                          |
| deltablue               | 3.66 ms                                                | 3.18 ms: 1.15x faster                                         |
| coroutines              | 26.2 ms                                                | 22.9 ms: 1.14x faster                                         |
| unpickle_pure_python    | 227 us                                                 | 200 us: 1.14x faster                                          |
| scimark_sparse_mat_mult | 4.59 ms                                                | 4.06 ms: 1.13x faster                                         |
| genshi_xml              | 51.4 ms                                                | 46.8 ms: 1.10x faster                                         |
| sympy_str               | 291 ms                                                 | 268 ms: 1.09x faster                                          |
| scimark_fft             | 325 ms                                                 | 300 ms: 1.08x faster                                          |
| xml_etree_parse         | 160 ms                                                 | 148 ms: 1.08x faster                                          |
| sqlglot_normalize       | 108 ms                                                 | 99.7 ms: 1.08x faster                                         |
| json_loads              | 26.1 us                                                | 24.2 us: 1.08x faster                                         |
| pickle_pure_python      | 308 us                                                 | 286 us: 1.08x faster                                          |
| pycparser               | 1.19 sec                                               | 1.11 sec: 1.07x faster                                        |
| richards                | 46.1 ms                                                | 43.1 ms: 1.07x faster                                         |
| sympy_integrate         | 21.0 ms                                                | 19.6 ms: 1.07x faster                                         |
| html5lib                | 64.8 ms                                                | 60.8 ms: 1.07x faster                                         |
| scimark_sor             | 115 ms                                                 | 108 ms: 1.07x faster                                          |
| sympy_expand            | 475 ms                                                 | 446 ms: 1.07x faster                                          |
| sympy_sum               | 166 ms                                                 | 156 ms: 1.06x faster                                          |
| regex_compile           | 136 ms                                                 | 129 ms: 1.06x faster                                          |
| 2to3                    | 259 ms                                                 | 245 ms: 1.06x faster                                          |
| float                   | 76.8 ms                                                | 72.7 ms: 1.06x faster                                         |
| sqlglot_optimize        | 52.7 ms                                                | 49.9 ms: 1.06x faster                                         |
| chaos                   | 68.7 ms                                                | 65.2 ms: 1.05x faster                                         |
| nqueens                 | 83.8 ms                                                | 79.7 ms: 1.05x faster                                         |
| spectral_norm           | 98.1 ms                                                | 93.5 ms: 1.05x faster                                         |
| create_gc_cycles        | 1.52 ms                                                | 1.44 ms: 1.05x faster                                         |
| pprint_pformat          | 1.46 sec                                               | 1.39 sec: 1.05x faster                                        |
| aiohttp                 | 1.05 ms                                                | 1.00 ms: 1.05x faster                                         |
| logging_silent          | 98.0 ns                                                | 93.8 ns: 1.04x faster                                         |
| xml_etree_iterparse     | 104 ms                                                 | 99.8 ms: 1.04x faster                                         |
| pidigits                | 197 ms                                                 | 189 ms: 1.04x faster                                          |
| pyflate                 | 419 ms                                                 | 402 ms: 1.04x faster                                          |
| mdp                     | 2.63 sec                                               | 2.53 sec: 1.04x faster                                        |
| sqlalchemy_imperative   | 18.1 ms                                                | 17.4 ms: 1.04x faster                                         |
| pprint_safe_repr        | 706 ms                                                 | 679 ms: 1.04x faster                                          |
| bench_thread_pool       | 817 us                                                 | 786 us: 1.04x faster                                          |
| scimark_monte_carlo     | 68.0 ms                                                | 65.5 ms: 1.04x faster                                         |
| async_tree_none         | 526 ms                                                 | 507 ms: 1.04x faster                                          |
| hexiom                  | 6.34 ms                                                | 6.12 ms: 1.04x faster                                         |
| genshi_text             | 21.5 ms                                                | 20.8 ms: 1.03x faster                                         |
| logging_simple          | 6.02 us                                                | 5.82 us: 1.03x faster                                         |
| gunicorn                | 1.12 ms                                                | 1.08 ms: 1.03x faster                                         |
| crypto_pyaes            | 75.7 ms                                                | 73.4 ms: 1.03x faster                                         |
| deepcopy                | 341 us                                                 | 332 us: 1.03x faster                                          |
| raytrace                | 291 ms                                                 | 284 ms: 1.03x faster                                          |
| deepcopy_memo           | 35.8 us                                                | 34.9 us: 1.03x faster                                         |
| sqlalchemy_declarative  | 138 ms                                                 | 135 ms: 1.03x faster                                          |
| docutils                | 2.60 sec                                               | 2.54 sec: 1.02x faster                                        |
| fannkuch                | 384 ms                                                 | 376 ms: 1.02x faster                                          |
| async_tree_io           | 1.30 sec                                               | 1.27 sec: 1.02x faster                                        |
| logging_format          | 6.48 us                                                | 6.34 us: 1.02x faster                                         |
| dulwich_log             | 64.0 ms                                                | 62.9 ms: 1.02x faster                                         |
| tornado_http            | 96.5 ms                                                | 94.9 ms: 1.02x faster                                         |
| regex_dna               | 203 ms                                                 | 200 ms: 1.02x faster                                          |
| regex_v8                | 22.2 ms                                                | 21.9 ms: 1.01x faster                                         |
| telco                   | 6.43 ms                                                | 6.33 ms: 1.01x faster                                         |
| pickle_dict             | 31.2 us                                                | 30.7 us: 1.01x faster                                         |
| async_tree_memoization  | 624 ms                                                 | 615 ms: 1.01x faster                                          |
| coverage                | 99.3 ms                                                | 98.2 ms: 1.01x faster                                         |
| pathlib                 | 18.1 ms                                                | 17.9 ms: 1.01x faster                                         |
| thrift                  | 760 us                                                 | 754 us: 1.01x faster                                          |
| go                      | 140 ms                                                 | 139 ms: 1.01x faster                                          |
| chameleon               | 6.38 ms                                                | 6.44 ms: 1.01x slower                                         |
| scimark_lu              | 108 ms                                                 | 109 ms: 1.01x slower                                          |
| unpickle_list           | 4.99 us                                                | 5.04 us: 1.01x slower                                         |
| regex_effbot            | 3.46 ms                                                | 3.50 ms: 1.01x slower                                         |
| pickle                  | 9.90 us                                                | 10.0 us: 1.01x slower                                         |
| mako                    | 9.83 ms                                                | 10.0 ms: 1.02x slower                                         |
| unpack_sequence         | 44.5 ns                                                | 45.5 ns: 1.02x slower                                         |
| xml_etree_process       | 53.7 ms                                                | 55.2 ms: 1.03x slower                                         |
| django_template         | 32.3 ms                                                | 33.3 ms: 1.03x slower                                         |
| python_startup          | 8.58 ms                                                | 8.89 ms: 1.04x slower                                         |
| sqlglot_transpile       | 1.65 ms                                                | 1.72 ms: 1.04x slower                                         |
| sqlglot_parse           | 1.36 ms                                                | 1.42 ms: 1.05x slower                                         |
| gc_traversal            | 3.82 ms                                                | 4.04 ms: 1.06x slower                                         |
| sqlite_synth            | 2.48 us                                                | 2.63 us: 1.06x slower                                         |
| xml_etree_generate      | 75.9 ms                                                | 80.4 ms: 1.06x slower                                         |
| python_startup_no_site  | 6.04 ms                                                | 6.45 ms: 1.07x slower                                         |
| nbody                   | 90.0 ms                                                | 99.9 ms: 1.11x slower                                         |
| async_generators        | 356 ms                                                 | 414 ms: 1.16x slower                                          |
| Geometric mean          | (ref)                                                  | 1.05x faster                                                  |

Benchmark hidden because not significant (8): unpickle, pickle_list, meteor_contest, json, djangocms, bench_mp_pool, deepcopy_reduce, async_tree_cpu_io_mixed
Ignored benchmarks (3) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: dask, flaskblogging, pylint
