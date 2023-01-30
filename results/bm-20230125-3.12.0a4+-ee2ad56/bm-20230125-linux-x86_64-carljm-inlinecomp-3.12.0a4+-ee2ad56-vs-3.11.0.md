
# Results vs. 3.11.0

- fork: carljm
- ref: inlinecomp
- machine: linux-x86_64
- commit hash: ee2ad56
- commit date: 2023-01-25
- overall geometric mean: 1.03x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230125-linux-x86_64-carljm-inlinecomp-3.12.0a4+-ee2ad56 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 257 ms                                                 | 249 ms: 1.03x faster                                         |
| chameleon      | 6.41 ms                                                | 6.35 ms: 1.01x faster                                        |
| docutils       | 2.60 sec                                               | 2.51 sec: 1.04x faster                                       |
| html5lib       | 63.2 ms                                                | 60.1 ms: 1.05x faster                                        |
| tornado_http   | 96.6 ms                                                | 94.5 ms: 1.02x faster                                        |
| Geometric mean | (ref)                                                  | 1.03x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230125-linux-x86_64-carljm-inlinecomp-3.12.0a4+-ee2ad56 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| float          | 76.3 ms                                                | 72.0 ms: 1.06x faster                                        |
| pidigits       | 199 ms                                                 | 190 ms: 1.05x faster                                         |
| nbody          | 95.0 ms                                                | 93.9 ms: 1.01x faster                                        |
| Geometric mean | (ref)                                                  | 1.04x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230125-linux-x86_64-carljm-inlinecomp-3.12.0a4+-ee2ad56 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 128 ms: 1.06x faster                                         |
| regex_v8       | 22.3 ms                                                | 21.3 ms: 1.05x faster                                        |
| regex_dna      | 203 ms                                                 | 201 ms: 1.01x faster                                         |
| regex_effbot   | 3.36 ms                                                | 3.42 ms: 1.02x slower                                        |
| Geometric mean | (ref)                                                  | 1.03x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230125-linux-x86_64-carljm-inlinecomp-3.12.0a4+-ee2ad56 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| json_dumps           | 12.7 ms                                                | 9.57 ms: 1.32x faster                                        |
| unpickle_pure_python | 225 us                                                 | 201 us: 1.12x faster                                         |
| json_loads           | 26.2 us                                                | 24.2 us: 1.08x faster                                        |
| xml_etree_parse      | 158 ms                                                 | 148 ms: 1.07x faster                                         |
| pickle_pure_python   | 304 us                                                 | 288 us: 1.05x faster                                         |
| unpickle_list        | 4.95 us                                                | 5.05 us: 1.02x slower                                        |
| xml_etree_generate   | 76.2 ms                                                | 78.2 ms: 1.03x slower                                        |
| pickle_list          | 4.17 us                                                | 4.29 us: 1.03x slower                                        |
| pickle_dict          | 31.4 us                                                | 32.4 us: 1.03x slower                                        |
| xml_etree_iterparse  | 103 ms                                                 | 106 ms: 1.04x slower                                         |
| pickle               | 9.79 us                                                | 10.2 us: 1.04x slower                                        |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                 |

Benchmark hidden because not significant (2): unpickle, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230125-linux-x86_64-carljm-inlinecomp-3.12.0a4+-ee2ad56 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 8.36 ms                                                | 8.89 ms: 1.06x slower                                        |
| python_startup_no_site | 5.96 ms                                                | 6.44 ms: 1.08x slower                                        |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230125-linux-x86_64-carljm-inlinecomp-3.12.0a4+-ee2ad56 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| genshi_xml      | 52.1 ms                                                | 46.8 ms: 1.11x faster                                        |
| genshi_text     | 22.1 ms                                                | 20.8 ms: 1.06x faster                                        |
| mako            | 9.85 ms                                                | 9.70 ms: 1.02x faster                                        |
| django_template | 32.5 ms                                                | 32.8 ms: 1.01x slower                                        |
| Geometric mean  | (ref)                                                  | 1.04x faster                                                 |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230125-linux-x86_64-carljm-inlinecomp-3.12.0a4+-ee2ad56 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| json_dumps              | 12.7 ms                                                | 9.57 ms: 1.32x faster                                        |
| deltablue               | 3.64 ms                                                | 3.20 ms: 1.14x faster                                        |
| unpickle_pure_python    | 225 us                                                 | 201 us: 1.12x faster                                         |
| genshi_xml              | 52.1 ms                                                | 46.8 ms: 1.11x faster                                        |
| nqueens                 | 85.0 ms                                                | 76.9 ms: 1.11x faster                                        |
| scimark_sparse_mat_mult | 4.40 ms                                                | 3.99 ms: 1.10x faster                                        |
| scimark_fft             | 329 ms                                                 | 303 ms: 1.09x faster                                         |
| scimark_sor             | 115 ms                                                 | 106 ms: 1.09x faster                                         |
| richards                | 46.2 ms                                                | 42.6 ms: 1.08x faster                                        |
| json_loads              | 26.2 us                                                | 24.2 us: 1.08x faster                                        |
| pycparser               | 1.17 sec                                               | 1.09 sec: 1.08x faster                                       |
| logging_silent          | 98.5 ns                                                | 91.7 ns: 1.07x faster                                        |
| sympy_sum               | 166 ms                                                 | 155 ms: 1.07x faster                                         |
| go                      | 143 ms                                                 | 134 ms: 1.07x faster                                         |
| xml_etree_parse         | 158 ms                                                 | 148 ms: 1.07x faster                                         |
| sympy_str               | 287 ms                                                 | 269 ms: 1.07x faster                                         |
| genshi_text             | 22.1 ms                                                | 20.8 ms: 1.06x faster                                        |
| chaos                   | 68.6 ms                                                | 64.6 ms: 1.06x faster                                        |
| sympy_integrate         | 20.9 ms                                                | 19.7 ms: 1.06x faster                                        |
| float                   | 76.3 ms                                                | 72.0 ms: 1.06x faster                                        |
| regex_compile           | 136 ms                                                 | 128 ms: 1.06x faster                                         |
| hexiom                  | 6.35 ms                                                | 5.99 ms: 1.06x faster                                        |
| gunicorn                | 1.12 ms                                                | 1.06 ms: 1.06x faster                                        |
| scimark_monte_carlo     | 68.3 ms                                                | 64.7 ms: 1.06x faster                                        |
| json                    | 4.95 ms                                                | 4.69 ms: 1.06x faster                                        |
| pickle_pure_python      | 304 us                                                 | 288 us: 1.05x faster                                         |
| deepcopy_memo           | 36.4 us                                                | 34.6 us: 1.05x faster                                        |
| pidigits                | 199 ms                                                 | 190 ms: 1.05x faster                                         |
| fannkuch                | 388 ms                                                 | 369 ms: 1.05x faster                                         |
| aiohttp                 | 1.05 ms                                                | 995 us: 1.05x faster                                         |
| html5lib                | 63.2 ms                                                | 60.1 ms: 1.05x faster                                        |
| logging_format          | 6.62 us                                                | 6.31 us: 1.05x faster                                        |
| regex_v8                | 22.3 ms                                                | 21.3 ms: 1.05x faster                                        |
| sympy_expand            | 472 ms                                                 | 450 ms: 1.05x faster                                         |
| sqlglot_optimize        | 53.0 ms                                                | 50.5 ms: 1.05x faster                                        |
| deepcopy                | 344 us                                                 | 328 us: 1.05x faster                                         |
| logging_simple          | 6.06 us                                                | 5.80 us: 1.05x faster                                        |
| mdp                     | 2.62 sec                                               | 2.51 sec: 1.04x faster                                       |
| sqlglot_normalize       | 108 ms                                                 | 103 ms: 1.04x faster                                         |
| pyflate                 | 417 ms                                                 | 400 ms: 1.04x faster                                         |
| spectral_norm           | 99.9 ms                                                | 96.2 ms: 1.04x faster                                        |
| bench_thread_pool       | 810 us                                                 | 781 us: 1.04x faster                                         |
| docutils                | 2.60 sec                                               | 2.51 sec: 1.04x faster                                       |
| pprint_pformat          | 1.44 sec                                               | 1.40 sec: 1.03x faster                                       |
| coverage                | 101 ms                                                 | 97.3 ms: 1.03x faster                                        |
| 2to3                    | 257 ms                                                 | 249 ms: 1.03x faster                                         |
| dulwich_log             | 63.9 ms                                                | 62.2 ms: 1.03x faster                                        |
| telco                   | 6.62 ms                                                | 6.46 ms: 1.03x faster                                        |
| raytrace                | 290 ms                                                 | 284 ms: 1.02x faster                                         |
| tornado_http            | 96.6 ms                                                | 94.5 ms: 1.02x faster                                        |
| coroutines              | 26.1 ms                                                | 25.6 ms: 1.02x faster                                        |
| async_tree_none         | 529 ms                                                 | 521 ms: 1.02x faster                                         |
| mako                    | 9.85 ms                                                | 9.70 ms: 1.02x faster                                        |
| pathlib                 | 18.2 ms                                                | 17.9 ms: 1.02x faster                                        |
| crypto_pyaes            | 73.9 ms                                                | 72.9 ms: 1.01x faster                                        |
| nbody                   | 95.0 ms                                                | 93.9 ms: 1.01x faster                                        |
| regex_dna               | 203 ms                                                 | 201 ms: 1.01x faster                                         |
| async_generators        | 359 ms                                                 | 355 ms: 1.01x faster                                         |
| pprint_safe_repr        | 691 ms                                                 | 684 ms: 1.01x faster                                         |
| chameleon               | 6.41 ms                                                | 6.35 ms: 1.01x faster                                        |
| thrift                  | 752 us                                                 | 748 us: 1.01x faster                                         |
| async_tree_io           | 1.31 sec                                               | 1.32 sec: 1.01x slower                                       |
| django_template         | 32.5 ms                                                | 32.8 ms: 1.01x slower                                        |
| regex_effbot            | 3.36 ms                                                | 3.42 ms: 1.02x slower                                        |
| unpickle_list           | 4.95 us                                                | 5.05 us: 1.02x slower                                        |
| unpack_sequence         | 43.4 ns                                                | 44.4 ns: 1.02x slower                                        |
| xml_etree_generate      | 76.2 ms                                                | 78.2 ms: 1.03x slower                                        |
| sqlglot_transpile       | 1.66 ms                                                | 1.70 ms: 1.03x slower                                        |
| pickle_list             | 4.17 us                                                | 4.29 us: 1.03x slower                                        |
| pickle_dict             | 31.4 us                                                | 32.4 us: 1.03x slower                                        |
| sqlglot_parse           | 1.37 ms                                                | 1.41 ms: 1.03x slower                                        |
| xml_etree_iterparse     | 103 ms                                                 | 106 ms: 1.04x slower                                         |
| sqlite_synth            | 2.49 us                                                | 2.58 us: 1.04x slower                                        |
| pickle                  | 9.79 us                                                | 10.2 us: 1.04x slower                                        |
| async_tree_memoization  | 625 ms                                                 | 656 ms: 1.05x slower                                         |
| generators              | 72.2 ms                                                | 75.9 ms: 1.05x slower                                        |
| python_startup          | 8.36 ms                                                | 8.89 ms: 1.06x slower                                        |
| python_startup_no_site  | 5.96 ms                                                | 6.44 ms: 1.08x slower                                        |
| mypy                    | 669 ms                                                 | 802 ms: 1.20x slower                                         |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                 |

Benchmark hidden because not significant (7): unpickle, scimark_lu, deepcopy_reduce, meteor_contest, bench_mp_pool, xml_etree_process, async_tree_cpu_io_mixed
Ignored benchmarks (4) of /home/mdboom/Work/builds/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of /home/mdboom/Work/builds/benchmarking/results/bm-20230125-3.12.0a4+-ee2ad56/bm-20230125-linux-x86_64-carljm-inlinecomp-3.12.0a4+-ee2ad56.json: asyncio_tcp, create_gc_cycles, dask, djangocms, gc_traversal
