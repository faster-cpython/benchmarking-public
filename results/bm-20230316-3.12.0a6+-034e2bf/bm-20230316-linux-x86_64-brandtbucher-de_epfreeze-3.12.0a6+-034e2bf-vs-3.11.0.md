
# Results vs. 3.11.0

- fork: brandtbucher
- ref: de_epfreeze
- machine: linux-x86_64
- commit hash: 034e2bf
- commit date: 2023-03-16
- overall geometric mean: 1.03x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230316-linux-x86_64-brandtbucher-de_epfreeze-3.12.0a6+-034e2bf |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 253 ms: 1.02x faster                                                |
| chameleon      | 6.38 ms                                                | 6.43 ms: 1.01x slower                                               |
| docutils       | 2.60 sec                                               | 2.53 sec: 1.03x faster                                              |
| html5lib       | 64.8 ms                                                | 59.6 ms: 1.09x faster                                               |
| tornado_http   | 96.5 ms                                                | 91.7 ms: 1.05x faster                                               |
| Geometric mean | (ref)                                                  | 1.04x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230316-linux-x86_64-brandtbucher-de_epfreeze-3.12.0a6+-034e2bf |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 76.8 ms                                                | 73.6 ms: 1.04x faster                                               |
| pidigits       | 197 ms                                                 | 189 ms: 1.04x faster                                                |
| nbody          | 90.0 ms                                                | 89.3 ms: 1.01x faster                                               |
| Geometric mean | (ref)                                                  | 1.03x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230316-linux-x86_64-brandtbucher-de_epfreeze-3.12.0a6+-034e2bf |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 135 ms: 1.01x faster                                                |
| regex_effbot   | 3.46 ms                                                | 3.42 ms: 1.01x faster                                               |
| regex_v8       | 22.2 ms                                                | 25.6 ms: 1.15x slower                                               |
| Geometric mean | (ref)                                                  | 1.03x slower                                                        |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230316-linux-x86_64-brandtbucher-de_epfreeze-3.12.0a6+-034e2bf |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.41 ms: 1.31x faster                                               |
| unpickle_pure_python | 227 us                                                 | 199 us: 1.14x faster                                                |
| pickle_pure_python   | 308 us                                                 | 282 us: 1.09x faster                                                |
| xml_etree_parse      | 160 ms                                                 | 147 ms: 1.09x faster                                                |
| json_loads           | 26.1 us                                                | 24.4 us: 1.07x faster                                               |
| xml_etree_iterparse  | 104 ms                                                 | 100 ms: 1.04x faster                                                |
| pickle_dict          | 31.2 us                                                | 30.8 us: 1.01x faster                                               |
| unpickle             | 13.3 us                                                | 13.7 us: 1.03x slower                                               |
| pickle               | 9.90 us                                                | 10.2 us: 1.03x slower                                               |
| unpickle_list        | 4.99 us                                                | 5.19 us: 1.04x slower                                               |
| xml_etree_process    | 53.7 ms                                                | 56.3 ms: 1.05x slower                                               |
| xml_etree_generate   | 75.9 ms                                                | 81.7 ms: 1.08x slower                                               |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                        |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230316-linux-x86_64-brandtbucher-de_epfreeze-3.12.0a6+-034e2bf |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 6.04 ms                                                | 6.47 ms: 1.07x slower                                               |
| python_startup         | 8.58 ms                                                | 9.50 ms: 1.11x slower                                               |
| Geometric mean         | (ref)                                                  | 1.09x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230316-linux-x86_64-brandtbucher-de_epfreeze-3.12.0a6+-034e2bf |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 48.4 ms: 1.06x faster                                               |
| genshi_text     | 21.5 ms                                                | 21.7 ms: 1.01x slower                                               |
| django_template | 32.3 ms                                                | 33.2 ms: 1.03x slower                                               |
| mako            | 9.83 ms                                                | 10.2 ms: 1.04x slower                                               |
| Geometric mean  | (ref)                                                  | 1.00x slower                                                        |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230316-linux-x86_64-brandtbucher-de_epfreeze-3.12.0a6+-034e2bf |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 30.1 ms: 2.44x faster                                               |
| asyncio_tcp             | 883 ms                                                 | 508 ms: 1.74x faster                                                |
| json_dumps              | 12.4 ms                                                | 9.41 ms: 1.31x faster                                               |
| coroutines              | 26.2 ms                                                | 22.0 ms: 1.19x faster                                               |
| deltablue               | 3.66 ms                                                | 3.16 ms: 1.16x faster                                               |
| unpickle_pure_python    | 227 us                                                 | 199 us: 1.14x faster                                                |
| coverage                | 99.3 ms                                                | 90.3 ms: 1.10x faster                                               |
| mdp                     | 2.63 sec                                               | 2.39 sec: 1.10x faster                                              |
| pickle_pure_python      | 308 us                                                 | 282 us: 1.09x faster                                                |
| xml_etree_parse         | 160 ms                                                 | 147 ms: 1.09x faster                                                |
| html5lib                | 64.8 ms                                                | 59.6 ms: 1.09x faster                                               |
| spectral_norm           | 98.1 ms                                                | 90.3 ms: 1.09x faster                                               |
| scimark_sor             | 115 ms                                                 | 106 ms: 1.08x faster                                                |
| gc_traversal            | 3.82 ms                                                | 3.55 ms: 1.08x faster                                               |
| json_loads              | 26.1 us                                                | 24.4 us: 1.07x faster                                               |
| scimark_fft             | 325 ms                                                 | 306 ms: 1.06x faster                                                |
| genshi_xml              | 51.4 ms                                                | 48.4 ms: 1.06x faster                                               |
| tornado_http            | 96.5 ms                                                | 91.7 ms: 1.05x faster                                               |
| richards                | 46.1 ms                                                | 43.9 ms: 1.05x faster                                               |
| unpack_sequence         | 44.5 ns                                                | 42.4 ns: 1.05x faster                                               |
| deepcopy_memo           | 35.8 us                                                | 34.2 us: 1.05x faster                                               |
| scimark_sparse_mat_mult | 4.59 ms                                                | 4.39 ms: 1.05x faster                                               |
| aiohttp                 | 1.05 ms                                                | 1.00 ms: 1.05x faster                                               |
| float                   | 76.8 ms                                                | 73.6 ms: 1.04x faster                                               |
| pprint_pformat          | 1.46 sec                                               | 1.40 sec: 1.04x faster                                              |
| pidigits                | 197 ms                                                 | 189 ms: 1.04x faster                                                |
| xml_etree_iterparse     | 104 ms                                                 | 100 ms: 1.04x faster                                                |
| hexiom                  | 6.34 ms                                                | 6.10 ms: 1.04x faster                                               |
| json                    | 4.87 ms                                                | 4.69 ms: 1.04x faster                                               |
| pprint_safe_repr        | 706 ms                                                 | 685 ms: 1.03x faster                                                |
| deepcopy                | 341 us                                                 | 332 us: 1.03x faster                                                |
| sqlalchemy_imperative   | 18.1 ms                                                | 17.6 ms: 1.03x faster                                               |
| gunicorn                | 1.12 ms                                                | 1.09 ms: 1.03x faster                                               |
| raytrace                | 291 ms                                                 | 284 ms: 1.03x faster                                                |
| docutils                | 2.60 sec                                               | 2.53 sec: 1.03x faster                                              |
| bench_thread_pool       | 817 us                                                 | 796 us: 1.03x faster                                                |
| go                      | 140 ms                                                 | 137 ms: 1.03x faster                                                |
| async_tree_memoization  | 624 ms                                                 | 609 ms: 1.03x faster                                                |
| logging_simple          | 6.02 us                                                | 5.88 us: 1.02x faster                                               |
| 2to3                    | 259 ms                                                 | 253 ms: 1.02x faster                                                |
| sqlalchemy_declarative  | 138 ms                                                 | 135 ms: 1.02x faster                                                |
| sympy_integrate         | 21.0 ms                                                | 20.5 ms: 1.02x faster                                               |
| dulwich_log             | 64.0 ms                                                | 62.6 ms: 1.02x faster                                               |
| chaos                   | 68.7 ms                                                | 67.2 ms: 1.02x faster                                               |
| sqlglot_normalize       | 108 ms                                                 | 105 ms: 1.02x faster                                                |
| sympy_str               | 291 ms                                                 | 285 ms: 1.02x faster                                                |
| fannkuch                | 384 ms                                                 | 377 ms: 1.02x faster                                                |
| crypto_pyaes            | 75.7 ms                                                | 74.2 ms: 1.02x faster                                               |
| sqlglot_optimize        | 52.7 ms                                                | 51.7 ms: 1.02x faster                                               |
| logging_silent          | 98.0 ns                                                | 96.1 ns: 1.02x faster                                               |
| pathlib                 | 18.1 ms                                                | 17.7 ms: 1.02x faster                                               |
| sympy_expand            | 475 ms                                                 | 467 ms: 1.02x faster                                                |
| scimark_monte_carlo     | 68.0 ms                                                | 66.8 ms: 1.02x faster                                               |
| create_gc_cycles        | 1.52 ms                                                | 1.49 ms: 1.02x faster                                               |
| nqueens                 | 83.8 ms                                                | 82.3 ms: 1.02x faster                                               |
| deepcopy_reduce         | 3.02 us                                                | 2.97 us: 1.01x faster                                               |
| pickle_dict             | 31.2 us                                                | 30.8 us: 1.01x faster                                               |
| pycparser               | 1.19 sec                                               | 1.17 sec: 1.01x faster                                              |
| regex_compile           | 136 ms                                                 | 135 ms: 1.01x faster                                                |
| regex_effbot            | 3.46 ms                                                | 3.42 ms: 1.01x faster                                               |
| scimark_lu              | 108 ms                                                 | 107 ms: 1.01x faster                                                |
| nbody                   | 90.0 ms                                                | 89.3 ms: 1.01x faster                                               |
| chameleon               | 6.38 ms                                                | 6.43 ms: 1.01x slower                                               |
| logging_format          | 6.48 us                                                | 6.54 us: 1.01x slower                                               |
| genshi_text             | 21.5 ms                                                | 21.7 ms: 1.01x slower                                               |
| pyflate                 | 419 ms                                                 | 423 ms: 1.01x slower                                                |
| thrift                  | 760 us                                                 | 774 us: 1.02x slower                                                |
| telco                   | 6.43 ms                                                | 6.58 ms: 1.02x slower                                               |
| async_tree_none         | 526 ms                                                 | 539 ms: 1.02x slower                                                |
| django_template         | 32.3 ms                                                | 33.2 ms: 1.03x slower                                               |
| unpickle                | 13.3 us                                                | 13.7 us: 1.03x slower                                               |
| pickle                  | 9.90 us                                                | 10.2 us: 1.03x slower                                               |
| mako                    | 9.83 ms                                                | 10.2 ms: 1.04x slower                                               |
| unpickle_list           | 4.99 us                                                | 5.19 us: 1.04x slower                                               |
| xml_etree_process       | 53.7 ms                                                | 56.3 ms: 1.05x slower                                               |
| sqlglot_transpile       | 1.65 ms                                                | 1.73 ms: 1.05x slower                                               |
| sqlglot_parse           | 1.36 ms                                                | 1.44 ms: 1.06x slower                                               |
| async_tree_cpu_io_mixed | 736 ms                                                 | 782 ms: 1.06x slower                                                |
| sqlite_synth            | 2.48 us                                                | 2.64 us: 1.06x slower                                               |
| python_startup_no_site  | 6.04 ms                                                | 6.47 ms: 1.07x slower                                               |
| xml_etree_generate      | 75.9 ms                                                | 81.7 ms: 1.08x slower                                               |
| python_startup          | 8.58 ms                                                | 9.50 ms: 1.11x slower                                               |
| regex_v8                | 22.2 ms                                                | 25.6 ms: 1.15x slower                                               |
| async_generators        | 356 ms                                                 | 416 ms: 1.17x slower                                                |
| dask                    | 365 ms                                                 | 511 ms: 1.40x slower                                                |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                        |

Benchmark hidden because not significant (8): djangocms, regex_dna, meteor_contest, bench_mp_pool, async_tree_io, sympy_sum, pickle_list, mypy2
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, pylint
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230316-3.12.0a6+-034e2bf/bm-20230316-linux-x86_64-brandtbucher-de_epfreeze-3.12.0a6+-034e2bf.json: comprehensions
