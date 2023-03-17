
# Results vs. base

- fork: brandtbucher
- ref: de_epfreeze
- machine: linux-x86_64
- commit hash: 034e2bf
- commit date: 2023-03-16
- overall geometric mean: 1.01x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230316-linux-x86_64-python-84e20c689a8b3b6cebfd-3.12.0a6+-84e20c6 | bm-20230316-linux-x86_64-brandtbucher-de_epfreeze-3.12.0a6+-034e2bf |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 250 ms                                                                 | 253 ms: 1.01x slower                                                |
| docutils       | 2.52 sec                                                               | 2.53 sec: 1.00x slower                                              |
| html5lib       | 60.7 ms                                                                | 59.6 ms: 1.02x faster                                               |
| tornado_http   | 91.0 ms                                                                | 91.7 ms: 1.01x slower                                               |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                        |

Benchmark hidden because not significant (1): chameleon

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230316-linux-x86_64-python-84e20c689a8b3b6cebfd-3.12.0a6+-84e20c6 | bm-20230316-linux-x86_64-brandtbucher-de_epfreeze-3.12.0a6+-034e2bf |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| pidigits       | 193 ms                                                                 | 189 ms: 1.02x faster                                                |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                        |

Benchmark hidden because not significant (2): float, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230316-linux-x86_64-python-84e20c689a8b3b6cebfd-3.12.0a6+-84e20c6 | bm-20230316-linux-x86_64-brandtbucher-de_epfreeze-3.12.0a6+-034e2bf |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_effbot   | 3.62 ms                                                                | 3.42 ms: 1.06x faster                                               |
| regex_compile  | 133 ms                                                                 | 135 ms: 1.01x slower                                                |
| regex_dna      | 200 ms                                                                 | 203 ms: 1.02x slower                                                |
| regex_v8       | 21.7 ms                                                                | 25.6 ms: 1.18x slower                                               |
| Geometric mean | (ref)                                                                  | 1.04x slower                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230316-linux-x86_64-python-84e20c689a8b3b6cebfd-3.12.0a6+-84e20c6 | bm-20230316-linux-x86_64-brandtbucher-de_epfreeze-3.12.0a6+-034e2bf |
|----------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| pickle               | 10.5 us                                                                | 10.2 us: 1.03x faster                                               |
| pickle_list          | 4.28 us                                                                | 4.16 us: 1.03x faster                                               |
| xml_etree_parse      | 148 ms                                                                 | 147 ms: 1.01x faster                                                |
| pickle_dict          | 31.0 us                                                                | 30.8 us: 1.01x faster                                               |
| pickle_pure_python   | 280 us                                                                 | 282 us: 1.01x slower                                                |
| xml_etree_generate   | 81.1 ms                                                                | 81.7 ms: 1.01x slower                                               |
| json_loads           | 24.0 us                                                                | 24.4 us: 1.01x slower                                               |
| unpickle_pure_python | 197 us                                                                 | 199 us: 1.01x slower                                                |
| xml_etree_iterparse  | 98.5 ms                                                                | 100 ms: 1.02x slower                                                |
| unpickle_list        | 5.08 us                                                                | 5.19 us: 1.02x slower                                               |
| unpickle             | 13.2 us                                                                | 13.7 us: 1.03x slower                                               |
| Geometric mean       | (ref)                                                                  | 1.00x slower                                                        |

Benchmark hidden because not significant (2): json_dumps, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230316-linux-x86_64-python-84e20c689a8b3b6cebfd-3.12.0a6+-84e20c6 | bm-20230316-linux-x86_64-brandtbucher-de_epfreeze-3.12.0a6+-034e2bf |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 6.52 ms                                                                | 6.47 ms: 1.01x faster                                               |
| python_startup         | 8.93 ms                                                                | 9.50 ms: 1.06x slower                                               |
| Geometric mean         | (ref)                                                                  | 1.03x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20230316-linux-x86_64-python-84e20c689a8b3b6cebfd-3.12.0a6+-84e20c6 | bm-20230316-linux-x86_64-brandtbucher-de_epfreeze-3.12.0a6+-034e2bf |
|-----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| django_template | 33.5 ms                                                                | 33.2 ms: 1.01x faster                                               |
| genshi_text     | 21.5 ms                                                                | 21.7 ms: 1.01x slower                                               |
| genshi_xml      | 47.5 ms                                                                | 48.4 ms: 1.02x slower                                               |
| mako            | 10.0 ms                                                                | 10.2 ms: 1.02x slower                                               |
| Geometric mean  | (ref)                                                                  | 1.01x slower                                                        |

All benchmarks:
===============

| Benchmark               | bm-20230316-linux-x86_64-python-84e20c689a8b3b6cebfd-3.12.0a6+-84e20c6 | bm-20230316-linux-x86_64-brandtbucher-de_epfreeze-3.12.0a6+-034e2bf |
|-------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_effbot            | 3.62 ms                                                                | 3.42 ms: 1.06x faster                                               |
| coroutines              | 23.1 ms                                                                | 22.0 ms: 1.05x faster                                               |
| coverage                | 94.2 ms                                                                | 90.3 ms: 1.04x faster                                               |
| unpack_sequence         | 44.2 ns                                                                | 42.4 ns: 1.04x faster                                               |
| gc_traversal            | 3.67 ms                                                                | 3.55 ms: 1.03x faster                                               |
| pickle                  | 10.5 us                                                                | 10.2 us: 1.03x faster                                               |
| pickle_list             | 4.28 us                                                                | 4.16 us: 1.03x faster                                               |
| spectral_norm           | 92.3 ms                                                                | 90.3 ms: 1.02x faster                                               |
| html5lib                | 60.7 ms                                                                | 59.6 ms: 1.02x faster                                               |
| pidigits                | 193 ms                                                                 | 189 ms: 1.02x faster                                                |
| scimark_lu              | 109 ms                                                                 | 107 ms: 1.01x faster                                                |
| mdp                     | 2.43 sec                                                               | 2.39 sec: 1.01x faster                                              |
| crypto_pyaes            | 75.1 ms                                                                | 74.2 ms: 1.01x faster                                               |
| django_template         | 33.5 ms                                                                | 33.2 ms: 1.01x faster                                               |
| xml_etree_parse         | 148 ms                                                                 | 147 ms: 1.01x faster                                                |
| python_startup_no_site  | 6.52 ms                                                                | 6.47 ms: 1.01x faster                                               |
| pickle_dict             | 31.0 us                                                                | 30.8 us: 1.01x faster                                               |
| comprehensions          | 24.1 us                                                                | 23.9 us: 1.01x faster                                               |
| dulwich_log             | 62.9 ms                                                                | 62.6 ms: 1.01x faster                                               |
| pathlib                 | 17.8 ms                                                                | 17.7 ms: 1.00x faster                                               |
| aiohttp                 | 1.01 ms                                                                | 1.00 ms: 1.00x faster                                               |
| docutils                | 2.52 sec                                                               | 2.53 sec: 1.00x slower                                              |
| gunicorn                | 1.08 ms                                                                | 1.09 ms: 1.00x slower                                               |
| pprint_safe_repr        | 682 ms                                                                 | 685 ms: 1.00x slower                                                |
| sympy_integrate         | 20.4 ms                                                                | 20.5 ms: 1.00x slower                                               |
| deltablue               | 3.15 ms                                                                | 3.16 ms: 1.01x slower                                               |
| bench_thread_pool       | 791 us                                                                 | 796 us: 1.01x slower                                                |
| pickle_pure_python      | 280 us                                                                 | 282 us: 1.01x slower                                                |
| sympy_str               | 283 ms                                                                 | 285 ms: 1.01x slower                                                |
| xml_etree_generate      | 81.1 ms                                                                | 81.7 ms: 1.01x slower                                               |
| tornado_http            | 91.0 ms                                                                | 91.7 ms: 1.01x slower                                               |
| sqlite_synth            | 2.62 us                                                                | 2.64 us: 1.01x slower                                               |
| genshi_text             | 21.5 ms                                                                | 21.7 ms: 1.01x slower                                               |
| sqlglot_normalize       | 104 ms                                                                 | 105 ms: 1.01x slower                                                |
| create_gc_cycles        | 1.47 ms                                                                | 1.49 ms: 1.01x slower                                               |
| scimark_monte_carlo     | 66.0 ms                                                                | 66.8 ms: 1.01x slower                                               |
| regex_compile           | 133 ms                                                                 | 135 ms: 1.01x slower                                                |
| sqlglot_optimize        | 51.0 ms                                                                | 51.7 ms: 1.01x slower                                               |
| meteor_contest          | 103 ms                                                                 | 104 ms: 1.01x slower                                                |
| async_generators        | 410 ms                                                                 | 416 ms: 1.01x slower                                                |
| json_loads              | 24.0 us                                                                | 24.4 us: 1.01x slower                                               |
| unpickle_pure_python    | 197 us                                                                 | 199 us: 1.01x slower                                                |
| 2to3                    | 250 ms                                                                 | 253 ms: 1.01x slower                                                |
| xml_etree_iterparse     | 98.5 ms                                                                | 100 ms: 1.02x slower                                                |
| sympy_expand            | 459 ms                                                                 | 467 ms: 1.02x slower                                                |
| regex_dna               | 200 ms                                                                 | 203 ms: 1.02x slower                                                |
| telco                   | 6.46 ms                                                                | 6.58 ms: 1.02x slower                                               |
| generators              | 29.5 ms                                                                | 30.1 ms: 1.02x slower                                               |
| sqlglot_transpile       | 1.70 ms                                                                | 1.73 ms: 1.02x slower                                               |
| chaos                   | 66.0 ms                                                                | 67.2 ms: 1.02x slower                                               |
| genshi_xml              | 47.5 ms                                                                | 48.4 ms: 1.02x slower                                               |
| mako                    | 10.0 ms                                                                | 10.2 ms: 1.02x slower                                               |
| json                    | 4.59 ms                                                                | 4.69 ms: 1.02x slower                                               |
| unpickle_list           | 5.08 us                                                                | 5.19 us: 1.02x slower                                               |
| raytrace                | 278 ms                                                                 | 284 ms: 1.02x slower                                                |
| deepcopy_reduce         | 2.91 us                                                                | 2.97 us: 1.02x slower                                               |
| dask                    | 500 ms                                                                 | 511 ms: 1.02x slower                                                |
| deepcopy                | 324 us                                                                 | 332 us: 1.02x slower                                                |
| fannkuch                | 367 ms                                                                 | 377 ms: 1.03x slower                                                |
| async_tree_io           | 1.27 sec                                                               | 1.30 sec: 1.03x slower                                              |
| sqlglot_parse           | 1.40 ms                                                                | 1.44 ms: 1.03x slower                                               |
| pyflate                 | 412 ms                                                                 | 423 ms: 1.03x slower                                                |
| logging_silent          | 93.4 ns                                                                | 96.1 ns: 1.03x slower                                               |
| nqueens                 | 79.9 ms                                                                | 82.3 ms: 1.03x slower                                               |
| unpickle                | 13.2 us                                                                | 13.7 us: 1.03x slower                                               |
| go                      | 132 ms                                                                 | 137 ms: 1.03x slower                                                |
| deepcopy_memo           | 33.1 us                                                                | 34.2 us: 1.03x slower                                               |
| async_tree_none         | 518 ms                                                                 | 539 ms: 1.04x slower                                                |
| richards                | 42.0 ms                                                                | 43.9 ms: 1.04x slower                                               |
| logging_simple          | 5.62 us                                                                | 5.88 us: 1.04x slower                                               |
| logging_format          | 6.22 us                                                                | 6.54 us: 1.05x slower                                               |
| scimark_sparse_mat_mult | 4.17 ms                                                                | 4.39 ms: 1.05x slower                                               |
| async_tree_cpu_io_mixed | 736 ms                                                                 | 782 ms: 1.06x slower                                                |
| python_startup          | 8.93 ms                                                                | 9.50 ms: 1.06x slower                                               |
| pycparser               | 1.09 sec                                                               | 1.17 sec: 1.07x slower                                              |
| regex_v8                | 21.7 ms                                                                | 25.6 ms: 1.18x slower                                               |
| mypy2                   | 332 ms                                                                 | 446 ms: 1.34x slower                                                |
| Geometric mean          | (ref)                                                                  | 1.01x slower                                                        |

Benchmark hidden because not significant (17): async_tree_memoization, djangocms, chameleon, sqlalchemy_imperative, sqlalchemy_declarative, scimark_sor, float, bench_mp_pool, hexiom, pprint_pformat, json_dumps, scimark_fft, asyncio_tcp, sympy_sum, xml_etree_process, nbody, thrift
