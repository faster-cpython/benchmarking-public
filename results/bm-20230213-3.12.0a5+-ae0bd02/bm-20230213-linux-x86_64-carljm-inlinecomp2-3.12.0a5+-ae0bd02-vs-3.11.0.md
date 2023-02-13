
# Results vs. 3.11.0

- fork: carljm
- ref: inlinecomp2
- machine: linux-x86_64
- commit hash: ae0bd02
- commit date: 2023-02-13
- overall geometric mean: 1.04x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230213-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-ae0bd02 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| 2to3           | 257 ms                                                 | 245 ms: 1.05x faster                                          |
| chameleon      | 6.41 ms                                                | 6.44 ms: 1.00x slower                                         |
| docutils       | 2.60 sec                                               | 2.54 sec: 1.02x faster                                        |
| html5lib       | 63.2 ms                                                | 60.8 ms: 1.04x faster                                         |
| tornado_http   | 96.6 ms                                                | 94.9 ms: 1.02x faster                                         |
| Geometric mean | (ref)                                                  | 1.02x faster                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230213-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-ae0bd02 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| pidigits       | 199 ms                                                 | 189 ms: 1.05x faster                                          |
| float          | 76.3 ms                                                | 72.7 ms: 1.05x faster                                         |
| nbody          | 95.0 ms                                                | 99.9 ms: 1.05x slower                                         |
| Geometric mean | (ref)                                                  | 1.02x faster                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230213-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-ae0bd02 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 129 ms: 1.06x faster                                          |
| regex_v8       | 22.3 ms                                                | 21.9 ms: 1.02x faster                                         |
| regex_dna      | 203 ms                                                 | 200 ms: 1.02x faster                                          |
| regex_effbot   | 3.36 ms                                                | 3.50 ms: 1.04x slower                                         |
| Geometric mean | (ref)                                                  | 1.01x faster                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230213-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-ae0bd02 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| json_dumps           | 12.7 ms                                                | 9.51 ms: 1.33x faster                                         |
| unpickle_pure_python | 225 us                                                 | 200 us: 1.13x faster                                          |
| json_loads           | 26.2 us                                                | 24.2 us: 1.09x faster                                         |
| xml_etree_parse      | 158 ms                                                 | 148 ms: 1.07x faster                                          |
| pickle_pure_python   | 304 us                                                 | 286 us: 1.06x faster                                          |
| xml_etree_iterparse  | 103 ms                                                 | 99.8 ms: 1.03x faster                                         |
| pickle_dict          | 31.4 us                                                | 30.7 us: 1.02x faster                                         |
| pickle_list          | 4.17 us                                                | 4.13 us: 1.01x faster                                         |
| unpickle_list        | 4.95 us                                                | 5.04 us: 1.02x slower                                         |
| pickle               | 9.79 us                                                | 10.0 us: 1.03x slower                                         |
| xml_etree_process    | 53.8 ms                                                | 55.2 ms: 1.03x slower                                         |
| xml_etree_generate   | 76.2 ms                                                | 80.4 ms: 1.06x slower                                         |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                  |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230213-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-ae0bd02 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup         | 8.36 ms                                                | 8.89 ms: 1.06x slower                                         |
| python_startup_no_site | 5.96 ms                                                | 6.45 ms: 1.08x slower                                         |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230213-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-ae0bd02 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| genshi_xml      | 52.1 ms                                                | 46.8 ms: 1.11x faster                                         |
| genshi_text     | 22.1 ms                                                | 20.8 ms: 1.06x faster                                         |
| mako            | 9.85 ms                                                | 10.0 ms: 1.02x slower                                         |
| django_template | 32.5 ms                                                | 33.3 ms: 1.03x slower                                         |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                  |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230213-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-ae0bd02 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| generators              | 72.2 ms                                                | 30.6 ms: 2.36x faster                                         |
| json_dumps              | 12.7 ms                                                | 9.51 ms: 1.33x faster                                         |
| deltablue               | 3.64 ms                                                | 3.18 ms: 1.15x faster                                         |
| coroutines              | 26.1 ms                                                | 22.9 ms: 1.14x faster                                         |
| unpickle_pure_python    | 225 us                                                 | 200 us: 1.13x faster                                          |
| genshi_xml              | 52.1 ms                                                | 46.8 ms: 1.11x faster                                         |
| scimark_fft             | 329 ms                                                 | 300 ms: 1.10x faster                                          |
| json_loads              | 26.2 us                                                | 24.2 us: 1.09x faster                                         |
| scimark_sparse_mat_mult | 4.40 ms                                                | 4.06 ms: 1.09x faster                                         |
| sqlglot_normalize       | 108 ms                                                 | 99.7 ms: 1.08x faster                                         |
| sympy_str               | 287 ms                                                 | 268 ms: 1.07x faster                                          |
| richards                | 46.2 ms                                                | 43.1 ms: 1.07x faster                                         |
| xml_etree_parse         | 158 ms                                                 | 148 ms: 1.07x faster                                          |
| spectral_norm           | 99.9 ms                                                | 93.5 ms: 1.07x faster                                         |
| scimark_sor             | 115 ms                                                 | 108 ms: 1.07x faster                                          |
| nqueens                 | 85.0 ms                                                | 79.7 ms: 1.07x faster                                         |
| sympy_integrate         | 20.9 ms                                                | 19.6 ms: 1.06x faster                                         |
| pickle_pure_python      | 304 us                                                 | 286 us: 1.06x faster                                          |
| genshi_text             | 22.1 ms                                                | 20.8 ms: 1.06x faster                                         |
| sqlglot_optimize        | 53.0 ms                                                | 49.9 ms: 1.06x faster                                         |
| sympy_sum               | 166 ms                                                 | 156 ms: 1.06x faster                                          |
| pycparser               | 1.17 sec                                               | 1.11 sec: 1.06x faster                                        |
| sympy_expand            | 472 ms                                                 | 446 ms: 1.06x faster                                          |
| regex_compile           | 136 ms                                                 | 129 ms: 1.06x faster                                          |
| chaos                   | 68.6 ms                                                | 65.2 ms: 1.05x faster                                         |
| pidigits                | 199 ms                                                 | 189 ms: 1.05x faster                                          |
| float                   | 76.3 ms                                                | 72.7 ms: 1.05x faster                                         |
| logging_silent          | 98.5 ns                                                | 93.8 ns: 1.05x faster                                         |
| 2to3                    | 257 ms                                                 | 245 ms: 1.05x faster                                          |
| telco                   | 6.62 ms                                                | 6.33 ms: 1.05x faster                                         |
| deepcopy_memo           | 36.4 us                                                | 34.9 us: 1.04x faster                                         |
| logging_format          | 6.62 us                                                | 6.34 us: 1.04x faster                                         |
| aiohttp                 | 1.05 ms                                                | 1.00 ms: 1.04x faster                                         |
| async_tree_none         | 529 ms                                                 | 507 ms: 1.04x faster                                          |
| scimark_monte_carlo     | 68.3 ms                                                | 65.5 ms: 1.04x faster                                         |
| logging_simple          | 6.06 us                                                | 5.82 us: 1.04x faster                                         |
| html5lib                | 63.2 ms                                                | 60.8 ms: 1.04x faster                                         |
| gunicorn                | 1.12 ms                                                | 1.08 ms: 1.04x faster                                         |
| pprint_pformat          | 1.44 sec                                               | 1.39 sec: 1.04x faster                                        |
| mdp                     | 2.62 sec                                               | 2.53 sec: 1.04x faster                                        |
| hexiom                  | 6.35 ms                                                | 6.12 ms: 1.04x faster                                         |
| pyflate                 | 417 ms                                                 | 402 ms: 1.04x faster                                          |
| sqlalchemy_imperative   | 18.0 ms                                                | 17.4 ms: 1.04x faster                                         |
| deepcopy                | 344 us                                                 | 332 us: 1.04x faster                                          |
| fannkuch                | 388 ms                                                 | 376 ms: 1.03x faster                                          |
| bench_thread_pool       | 810 us                                                 | 786 us: 1.03x faster                                          |
| xml_etree_iterparse     | 103 ms                                                 | 99.8 ms: 1.03x faster                                         |
| sqlalchemy_declarative  | 139 ms                                                 | 135 ms: 1.03x faster                                          |
| go                      | 143 ms                                                 | 139 ms: 1.03x faster                                          |
| async_tree_io           | 1.31 sec                                               | 1.27 sec: 1.03x faster                                        |
| coverage                | 101 ms                                                 | 98.2 ms: 1.02x faster                                         |
| pickle_dict             | 31.4 us                                                | 30.7 us: 1.02x faster                                         |
| raytrace                | 290 ms                                                 | 284 ms: 1.02x faster                                          |
| docutils                | 2.60 sec                                               | 2.54 sec: 1.02x faster                                        |
| json                    | 4.95 ms                                                | 4.85 ms: 1.02x faster                                         |
| tornado_http            | 96.6 ms                                                | 94.9 ms: 1.02x faster                                         |
| regex_v8                | 22.3 ms                                                | 21.9 ms: 1.02x faster                                         |
| pprint_safe_repr        | 691 ms                                                 | 679 ms: 1.02x faster                                          |
| dulwich_log             | 63.9 ms                                                | 62.9 ms: 1.02x faster                                         |
| regex_dna               | 203 ms                                                 | 200 ms: 1.02x faster                                          |
| async_tree_memoization  | 625 ms                                                 | 615 ms: 1.02x faster                                          |
| pathlib                 | 18.2 ms                                                | 17.9 ms: 1.01x faster                                         |
| pickle_list             | 4.17 us                                                | 4.13 us: 1.01x faster                                         |
| async_tree_cpu_io_mixed | 752 ms                                                 | 743 ms: 1.01x faster                                          |
| crypto_pyaes            | 73.9 ms                                                | 73.4 ms: 1.01x faster                                         |
| meteor_contest          | 105 ms                                                 | 104 ms: 1.01x faster                                          |
| chameleon               | 6.41 ms                                                | 6.44 ms: 1.00x slower                                         |
| scimark_lu              | 107 ms                                                 | 109 ms: 1.02x slower                                          |
| unpickle_list           | 4.95 us                                                | 5.04 us: 1.02x slower                                         |
| mako                    | 9.85 ms                                                | 10.0 ms: 1.02x slower                                         |
| deepcopy_reduce         | 2.97 us                                                | 3.03 us: 1.02x slower                                         |
| django_template         | 32.5 ms                                                | 33.3 ms: 1.03x slower                                         |
| pickle                  | 9.79 us                                                | 10.0 us: 1.03x slower                                         |
| xml_etree_process       | 53.8 ms                                                | 55.2 ms: 1.03x slower                                         |
| sqlglot_transpile       | 1.66 ms                                                | 1.72 ms: 1.03x slower                                         |
| sqlglot_parse           | 1.37 ms                                                | 1.42 ms: 1.04x slower                                         |
| regex_effbot            | 3.36 ms                                                | 3.50 ms: 1.04x slower                                         |
| unpack_sequence         | 43.4 ns                                                | 45.5 ns: 1.05x slower                                         |
| nbody                   | 95.0 ms                                                | 99.9 ms: 1.05x slower                                         |
| sqlite_synth            | 2.49 us                                                | 2.63 us: 1.05x slower                                         |
| xml_etree_generate      | 76.2 ms                                                | 80.4 ms: 1.06x slower                                         |
| python_startup          | 8.36 ms                                                | 8.89 ms: 1.06x slower                                         |
| python_startup_no_site  | 5.96 ms                                                | 6.45 ms: 1.08x slower                                         |
| async_generators        | 359 ms                                                 | 414 ms: 1.15x slower                                          |
| Geometric mean          | (ref)                                                  | 1.04x faster                                                  |

Benchmark hidden because not significant (3): unpickle, bench_mp_pool, thrift
Ignored benchmarks (3) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, mypy, pylint
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20230213-3.12.0a5+-ae0bd02/bm-20230213-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-ae0bd02.json: asyncio_tcp, create_gc_cycles, djangocms, gc_traversal, mypy2
