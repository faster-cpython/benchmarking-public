
# Results vs. 3.11.0

- fork: carljm
- ref: inlinecomp2
- machine: linux-x86_64
- commit hash: 9f0fc5b
- commit date: 2023-02-20
- overall geometric mean: 1.05x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230220-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-9f0fc5b |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 248 ms: 1.05x faster                                          |
| chameleon      | 6.38 ms                                                | 6.32 ms: 1.01x faster                                         |
| docutils       | 2.60 sec                                               | 2.53 sec: 1.03x faster                                        |
| html5lib       | 64.8 ms                                                | 60.4 ms: 1.07x faster                                         |
| tornado_http   | 96.5 ms                                                | 94.3 ms: 1.02x faster                                         |
| Geometric mean | (ref)                                                  | 1.04x faster                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230220-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-9f0fc5b |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| float          | 76.8 ms                                                | 72.0 ms: 1.07x faster                                         |
| pidigits       | 197 ms                                                 | 189 ms: 1.04x faster                                          |
| nbody          | 90.0 ms                                                | 94.0 ms: 1.04x slower                                         |
| Geometric mean | (ref)                                                  | 1.02x faster                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230220-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-9f0fc5b |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 127 ms: 1.07x faster                                          |
| regex_v8       | 22.2 ms                                                | 21.8 ms: 1.02x faster                                         |
| regex_dna      | 203 ms                                                 | 207 ms: 1.02x slower                                          |
| regex_effbot   | 3.46 ms                                                | 3.69 ms: 1.07x slower                                         |
| Geometric mean | (ref)                                                  | 1.00x faster                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230220-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-9f0fc5b |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.49 ms: 1.30x faster                                         |
| unpickle_pure_python | 227 us                                                 | 197 us: 1.15x faster                                          |
| pickle_pure_python   | 308 us                                                 | 281 us: 1.10x faster                                          |
| xml_etree_parse      | 160 ms                                                 | 148 ms: 1.08x faster                                          |
| json_loads           | 26.1 us                                                | 24.1 us: 1.08x faster                                         |
| pickle_list          | 4.14 us                                                | 3.97 us: 1.04x faster                                         |
| pickle_dict          | 31.2 us                                                | 30.0 us: 1.04x faster                                         |
| xml_etree_iterparse  | 104 ms                                                 | 102 ms: 1.02x faster                                          |
| pickle               | 9.90 us                                                | 10.0 us: 1.01x slower                                         |
| unpickle_list        | 4.99 us                                                | 5.13 us: 1.03x slower                                         |
| xml_etree_process    | 53.7 ms                                                | 55.5 ms: 1.04x slower                                         |
| xml_etree_generate   | 75.9 ms                                                | 80.6 ms: 1.06x slower                                         |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                  |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230220-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-9f0fc5b |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.96 ms: 1.04x slower                                         |
| python_startup_no_site | 6.04 ms                                                | 6.50 ms: 1.08x slower                                         |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230220-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-9f0fc5b |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 47.9 ms: 1.07x faster                                         |
| genshi_text     | 21.5 ms                                                | 20.8 ms: 1.03x faster                                         |
| django_template | 32.3 ms                                                | 32.7 ms: 1.01x slower                                         |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                  |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230220-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-9f0fc5b |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 29.9 ms: 2.45x faster                                         |
| asyncio_tcp             | 883 ms                                                 | 502 ms: 1.76x faster                                          |
| json_dumps              | 12.4 ms                                                | 9.49 ms: 1.30x faster                                         |
| mypy2                   | 420 ms                                                 | 326 ms: 1.29x faster                                          |
| coroutines              | 26.2 ms                                                | 21.8 ms: 1.20x faster                                         |
| scimark_sparse_mat_mult | 4.59 ms                                                | 3.93 ms: 1.17x faster                                         |
| deltablue               | 3.66 ms                                                | 3.16 ms: 1.16x faster                                         |
| unpickle_pure_python    | 227 us                                                 | 197 us: 1.15x faster                                          |
| richards                | 46.1 ms                                                | 41.3 ms: 1.12x faster                                         |
| pickle_pure_python      | 308 us                                                 | 281 us: 1.10x faster                                          |
| xml_etree_parse         | 160 ms                                                 | 148 ms: 1.08x faster                                          |
| json_loads              | 26.1 us                                                | 24.1 us: 1.08x faster                                         |
| chaos                   | 68.7 ms                                                | 63.5 ms: 1.08x faster                                         |
| sqlglot_normalize       | 108 ms                                                 | 99.8 ms: 1.08x faster                                         |
| scimark_sor             | 115 ms                                                 | 107 ms: 1.07x faster                                          |
| genshi_xml              | 51.4 ms                                                | 47.9 ms: 1.07x faster                                         |
| regex_compile           | 136 ms                                                 | 127 ms: 1.07x faster                                          |
| html5lib                | 64.8 ms                                                | 60.4 ms: 1.07x faster                                         |
| sympy_expand            | 475 ms                                                 | 444 ms: 1.07x faster                                          |
| go                      | 140 ms                                                 | 131 ms: 1.07x faster                                          |
| logging_silent          | 98.0 ns                                                | 91.7 ns: 1.07x faster                                         |
| hexiom                  | 6.34 ms                                                | 5.94 ms: 1.07x faster                                         |
| float                   | 76.8 ms                                                | 72.0 ms: 1.07x faster                                         |
| pycparser               | 1.19 sec                                               | 1.11 sec: 1.07x faster                                        |
| sqlglot_optimize        | 52.7 ms                                                | 49.7 ms: 1.06x faster                                         |
| pprint_pformat          | 1.46 sec                                               | 1.37 sec: 1.06x faster                                        |
| mdp                     | 2.63 sec                                               | 2.48 sec: 1.06x faster                                        |
| json                    | 4.87 ms                                                | 4.61 ms: 1.06x faster                                         |
| scimark_fft             | 325 ms                                                 | 309 ms: 1.05x faster                                          |
| pprint_safe_repr        | 706 ms                                                 | 671 ms: 1.05x faster                                          |
| pyflate                 | 419 ms                                                 | 398 ms: 1.05x faster                                          |
| scimark_monte_carlo     | 68.0 ms                                                | 64.7 ms: 1.05x faster                                         |
| logging_simple          | 6.02 us                                                | 5.73 us: 1.05x faster                                         |
| deepcopy_memo           | 35.8 us                                                | 34.2 us: 1.05x faster                                         |
| sympy_str               | 291 ms                                                 | 278 ms: 1.05x faster                                          |
| 2to3                    | 259 ms                                                 | 248 ms: 1.05x faster                                          |
| aiohttp                 | 1.05 ms                                                | 1.00 ms: 1.05x faster                                         |
| fannkuch                | 384 ms                                                 | 368 ms: 1.05x faster                                          |
| sympy_integrate         | 21.0 ms                                                | 20.1 ms: 1.04x faster                                         |
| bench_thread_pool       | 817 us                                                 | 783 us: 1.04x faster                                          |
| nqueens                 | 83.8 ms                                                | 80.3 ms: 1.04x faster                                         |
| async_tree_none         | 526 ms                                                 | 505 ms: 1.04x faster                                          |
| pickle_list             | 4.14 us                                                | 3.97 us: 1.04x faster                                         |
| deepcopy                | 341 us                                                 | 328 us: 1.04x faster                                          |
| gunicorn                | 1.12 ms                                                | 1.07 ms: 1.04x faster                                         |
| pidigits                | 197 ms                                                 | 189 ms: 1.04x faster                                          |
| pickle_dict             | 31.2 us                                                | 30.0 us: 1.04x faster                                         |
| unpack_sequence         | 44.5 ns                                                | 42.9 ns: 1.04x faster                                         |
| raytrace                | 291 ms                                                 | 281 ms: 1.04x faster                                          |
| sqlalchemy_imperative   | 18.1 ms                                                | 17.5 ms: 1.03x faster                                         |
| genshi_text             | 21.5 ms                                                | 20.8 ms: 1.03x faster                                         |
| coverage                | 99.3 ms                                                | 96.1 ms: 1.03x faster                                         |
| async_tree_io           | 1.30 sec                                               | 1.26 sec: 1.03x faster                                        |
| create_gc_cycles        | 1.52 ms                                                | 1.47 ms: 1.03x faster                                         |
| docutils                | 2.60 sec                                               | 2.53 sec: 1.03x faster                                        |
| crypto_pyaes            | 75.7 ms                                                | 73.7 ms: 1.03x faster                                         |
| tornado_http            | 96.5 ms                                                | 94.3 ms: 1.02x faster                                         |
| thrift                  | 760 us                                                 | 742 us: 1.02x faster                                          |
| logging_format          | 6.48 us                                                | 6.33 us: 1.02x faster                                         |
| async_tree_memoization  | 624 ms                                                 | 611 ms: 1.02x faster                                          |
| deepcopy_reduce         | 3.02 us                                                | 2.96 us: 1.02x faster                                         |
| spectral_norm           | 98.1 ms                                                | 96.2 ms: 1.02x faster                                         |
| regex_v8                | 22.2 ms                                                | 21.8 ms: 1.02x faster                                         |
| xml_etree_iterparse     | 104 ms                                                 | 102 ms: 1.02x faster                                          |
| meteor_contest          | 104 ms                                                 | 103 ms: 1.02x faster                                          |
| sympy_sum               | 166 ms                                                 | 164 ms: 1.01x faster                                          |
| chameleon               | 6.38 ms                                                | 6.32 ms: 1.01x faster                                         |
| dulwich_log             | 64.0 ms                                                | 63.6 ms: 1.01x faster                                         |
| pathlib                 | 18.1 ms                                                | 18.3 ms: 1.01x slower                                         |
| django_template         | 32.3 ms                                                | 32.7 ms: 1.01x slower                                         |
| pickle                  | 9.90 us                                                | 10.0 us: 1.01x slower                                         |
| regex_dna               | 203 ms                                                 | 207 ms: 1.02x slower                                          |
| unpickle_list           | 4.99 us                                                | 5.13 us: 1.03x slower                                         |
| xml_etree_process       | 53.7 ms                                                | 55.5 ms: 1.04x slower                                         |
| nbody                   | 90.0 ms                                                | 94.0 ms: 1.04x slower                                         |
| python_startup          | 8.58 ms                                                | 8.96 ms: 1.04x slower                                         |
| sqlglot_transpile       | 1.65 ms                                                | 1.72 ms: 1.05x slower                                         |
| sqlglot_parse           | 1.36 ms                                                | 1.44 ms: 1.06x slower                                         |
| sqlite_synth            | 2.48 us                                                | 2.63 us: 1.06x slower                                         |
| xml_etree_generate      | 75.9 ms                                                | 80.6 ms: 1.06x slower                                         |
| regex_effbot            | 3.46 ms                                                | 3.69 ms: 1.07x slower                                         |
| python_startup_no_site  | 6.04 ms                                                | 6.50 ms: 1.08x slower                                         |
| gc_traversal            | 3.82 ms                                                | 4.18 ms: 1.09x slower                                         |
| async_generators        | 356 ms                                                 | 417 ms: 1.17x slower                                          |
| dask                    | 365 ms                                                 | 498 ms: 1.36x slower                                          |
| Geometric mean          | (ref)                                                  | 1.05x faster                                                  |

Benchmark hidden because not significant (8): sqlalchemy_declarative, scimark_lu, telco, mako, djangocms, bench_mp_pool, async_tree_cpu_io_mixed, unpickle
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, pylint
