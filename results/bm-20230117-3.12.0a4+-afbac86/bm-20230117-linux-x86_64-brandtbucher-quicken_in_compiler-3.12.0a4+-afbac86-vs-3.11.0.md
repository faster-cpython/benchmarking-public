
# Results vs. 3.11.0

- fork: brandtbucher
- ref: quicken_in_compiler
- machine: linux-x86_64
- commit hash: afbac86
- commit date: 2023-01-17
- overall geometric mean: 1.03x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230117-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-afbac86 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 252 ms: 1.03x faster                                                        |
| docutils       | 2.60 sec                                               | 2.50 sec: 1.04x faster                                                      |
| html5lib       | 64.8 ms                                                | 60.3 ms: 1.08x faster                                                       |
| tornado_http   | 96.5 ms                                                | 93.8 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                |

Benchmark hidden because not significant (1): chameleon

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230117-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-afbac86 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 76.8 ms                                                | 73.0 ms: 1.05x faster                                                       |
| pidigits       | 197 ms                                                 | 189 ms: 1.04x faster                                                        |
| nbody          | 90.0 ms                                                | 94.5 ms: 1.05x slower                                                       |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230117-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-afbac86 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 129 ms: 1.06x faster                                                        |
| regex_effbot   | 3.46 ms                                                | 3.48 ms: 1.01x slower                                                       |
| regex_v8       | 22.2 ms                                                | 22.4 ms: 1.01x slower                                                       |
| regex_dna      | 203 ms                                                 | 207 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230117-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-afbac86 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.35 ms: 1.32x faster                                                       |
| unpickle_pure_python | 227 us                                                 | 204 us: 1.12x faster                                                        |
| json_loads           | 26.1 us                                                | 24.1 us: 1.08x faster                                                       |
| xml_etree_parse      | 160 ms                                                 | 149 ms: 1.07x faster                                                        |
| pickle_pure_python   | 308 us                                                 | 288 us: 1.07x faster                                                        |
| pickle_dict          | 31.2 us                                                | 29.9 us: 1.04x faster                                                       |
| pickle_list          | 4.14 us                                                | 4.00 us: 1.04x faster                                                       |
| pickle               | 9.90 us                                                | 9.93 us: 1.00x slower                                                       |
| unpickle_list        | 4.99 us                                                | 5.06 us: 1.01x slower                                                       |
| xml_etree_process    | 53.7 ms                                                | 54.4 ms: 1.01x slower                                                       |
| xml_etree_iterparse  | 104 ms                                                 | 106 ms: 1.02x slower                                                        |
| xml_etree_generate   | 75.9 ms                                                | 78.0 ms: 1.03x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                                |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230117-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-afbac86 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.89 ms: 1.04x slower                                                       |
| python_startup_no_site | 6.04 ms                                                | 6.42 ms: 1.06x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.05x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230117-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-afbac86 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 51.4 ms                                                | 47.4 ms: 1.08x faster                                                       |
| genshi_text     | 21.5 ms                                                | 20.9 ms: 1.03x faster                                                       |
| mako            | 9.83 ms                                                | 9.65 ms: 1.02x faster                                                       |
| django_template | 32.3 ms                                                | 32.0 ms: 1.01x faster                                                       |
| Geometric mean  | (ref)                                                  | 1.04x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230117-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-afbac86 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| asyncio_tcp             | 883 ms                                                 | 496 ms: 1.78x faster                                                        |
| json_dumps              | 12.4 ms                                                | 9.35 ms: 1.32x faster                                                       |
| scimark_sparse_mat_mult | 4.59 ms                                                | 4.00 ms: 1.15x faster                                                       |
| deltablue               | 3.66 ms                                                | 3.22 ms: 1.13x faster                                                       |
| unpickle_pure_python    | 227 us                                                 | 204 us: 1.12x faster                                                        |
| nqueens                 | 83.8 ms                                                | 76.6 ms: 1.09x faster                                                       |
| genshi_xml              | 51.4 ms                                                | 47.4 ms: 1.08x faster                                                       |
| json_loads              | 26.1 us                                                | 24.1 us: 1.08x faster                                                       |
| sympy_str               | 291 ms                                                 | 269 ms: 1.08x faster                                                        |
| scimark_sor             | 115 ms                                                 | 107 ms: 1.08x faster                                                        |
| html5lib                | 64.8 ms                                                | 60.3 ms: 1.08x faster                                                       |
| logging_silent          | 98.0 ns                                                | 91.2 ns: 1.07x faster                                                       |
| richards                | 46.1 ms                                                | 43.0 ms: 1.07x faster                                                       |
| xml_etree_parse         | 160 ms                                                 | 149 ms: 1.07x faster                                                        |
| unpack_sequence         | 44.5 ns                                                | 41.4 ns: 1.07x faster                                                       |
| pickle_pure_python      | 308 us                                                 | 288 us: 1.07x faster                                                        |
| chaos                   | 68.7 ms                                                | 64.3 ms: 1.07x faster                                                       |
| sympy_sum               | 166 ms                                                 | 155 ms: 1.07x faster                                                        |
| coverage                | 99.3 ms                                                | 93.1 ms: 1.07x faster                                                       |
| scimark_fft             | 325 ms                                                 | 306 ms: 1.06x faster                                                        |
| hexiom                  | 6.34 ms                                                | 5.98 ms: 1.06x faster                                                       |
| regex_compile           | 136 ms                                                 | 129 ms: 1.06x faster                                                        |
| sympy_integrate         | 21.0 ms                                                | 19.8 ms: 1.06x faster                                                       |
| pprint_pformat          | 1.46 sec                                               | 1.38 sec: 1.05x faster                                                      |
| coroutines              | 26.2 ms                                                | 24.8 ms: 1.05x faster                                                       |
| float                   | 76.8 ms                                                | 73.0 ms: 1.05x faster                                                       |
| pprint_safe_repr        | 706 ms                                                 | 671 ms: 1.05x faster                                                        |
| bench_thread_pool       | 817 us                                                 | 778 us: 1.05x faster                                                        |
| aiohttp                 | 1.05 ms                                                | 1.00 ms: 1.05x faster                                                       |
| sympy_expand            | 475 ms                                                 | 454 ms: 1.05x faster                                                        |
| spectral_norm           | 98.1 ms                                                | 93.8 ms: 1.05x faster                                                       |
| json                    | 4.87 ms                                                | 4.66 ms: 1.04x faster                                                       |
| scimark_monte_carlo     | 68.0 ms                                                | 65.2 ms: 1.04x faster                                                       |
| pidigits                | 197 ms                                                 | 189 ms: 1.04x faster                                                        |
| docutils                | 2.60 sec                                               | 2.50 sec: 1.04x faster                                                      |
| pickle_dict             | 31.2 us                                                | 29.9 us: 1.04x faster                                                       |
| gunicorn                | 1.12 ms                                                | 1.07 ms: 1.04x faster                                                       |
| deepcopy                | 341 us                                                 | 328 us: 1.04x faster                                                        |
| deepcopy_memo           | 35.8 us                                                | 34.5 us: 1.04x faster                                                       |
| pickle_list             | 4.14 us                                                | 4.00 us: 1.04x faster                                                       |
| pyflate                 | 419 ms                                                 | 404 ms: 1.04x faster                                                        |
| logging_simple          | 6.02 us                                                | 5.82 us: 1.03x faster                                                       |
| sqlglot_optimize        | 52.7 ms                                                | 51.0 ms: 1.03x faster                                                       |
| crypto_pyaes            | 75.7 ms                                                | 73.2 ms: 1.03x faster                                                       |
| genshi_text             | 21.5 ms                                                | 20.9 ms: 1.03x faster                                                       |
| pycparser               | 1.19 sec                                               | 1.15 sec: 1.03x faster                                                      |
| create_gc_cycles        | 1.52 ms                                                | 1.47 ms: 1.03x faster                                                       |
| tornado_http            | 96.5 ms                                                | 93.8 ms: 1.03x faster                                                       |
| dulwich_log             | 64.0 ms                                                | 62.2 ms: 1.03x faster                                                       |
| sqlglot_normalize       | 108 ms                                                 | 105 ms: 1.03x faster                                                        |
| 2to3                    | 259 ms                                                 | 252 ms: 1.03x faster                                                        |
| thrift                  | 760 us                                                 | 739 us: 1.03x faster                                                        |
| raytrace                | 291 ms                                                 | 284 ms: 1.02x faster                                                        |
| mdp                     | 2.63 sec                                               | 2.56 sec: 1.02x faster                                                      |
| deepcopy_reduce         | 3.02 us                                                | 2.95 us: 1.02x faster                                                       |
| fannkuch                | 384 ms                                                 | 376 ms: 1.02x faster                                                        |
| go                      | 140 ms                                                 | 138 ms: 1.02x faster                                                        |
| mako                    | 9.83 ms                                                | 9.65 ms: 1.02x faster                                                       |
| pathlib                 | 18.1 ms                                                | 17.7 ms: 1.02x faster                                                       |
| telco                   | 6.43 ms                                                | 6.35 ms: 1.01x faster                                                       |
| scimark_lu              | 108 ms                                                 | 107 ms: 1.01x faster                                                        |
| django_template         | 32.3 ms                                                | 32.0 ms: 1.01x faster                                                       |
| async_generators        | 356 ms                                                 | 354 ms: 1.00x faster                                                        |
| pickle                  | 9.90 us                                                | 9.93 us: 1.00x slower                                                       |
| regex_effbot            | 3.46 ms                                                | 3.48 ms: 1.01x slower                                                       |
| regex_v8                | 22.2 ms                                                | 22.4 ms: 1.01x slower                                                       |
| unpickle_list           | 4.99 us                                                | 5.06 us: 1.01x slower                                                       |
| xml_etree_process       | 53.7 ms                                                | 54.4 ms: 1.01x slower                                                       |
| async_tree_io           | 1.30 sec                                               | 1.32 sec: 1.02x slower                                                      |
| regex_dna               | 203 ms                                                 | 207 ms: 1.02x slower                                                        |
| xml_etree_iterparse     | 104 ms                                                 | 106 ms: 1.02x slower                                                        |
| async_tree_cpu_io_mixed | 736 ms                                                 | 752 ms: 1.02x slower                                                        |
| sqlglot_transpile       | 1.65 ms                                                | 1.70 ms: 1.03x slower                                                       |
| xml_etree_generate      | 75.9 ms                                                | 78.0 ms: 1.03x slower                                                       |
| sqlglot_parse           | 1.36 ms                                                | 1.40 ms: 1.03x slower                                                       |
| sqlite_synth            | 2.48 us                                                | 2.56 us: 1.03x slower                                                       |
| python_startup          | 8.58 ms                                                | 8.89 ms: 1.04x slower                                                       |
| generators              | 73.5 ms                                                | 76.6 ms: 1.04x slower                                                       |
| nbody                   | 90.0 ms                                                | 94.5 ms: 1.05x slower                                                       |
| async_tree_memoization  | 624 ms                                                 | 659 ms: 1.06x slower                                                        |
| python_startup_no_site  | 6.04 ms                                                | 6.42 ms: 1.06x slower                                                       |
| gc_traversal            | 3.82 ms                                                | 4.29 ms: 1.12x slower                                                       |
| dask                    | 365 ms                                                 | 497 ms: 1.36x slower                                                        |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                                |

Benchmark hidden because not significant (7): djangocms, unpickle, logging_format, async_tree_none, meteor_contest, bench_mp_pool, chameleon
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230117-3.12.0a4+-afbac86/bm-20230117-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-afbac86.json: mypy
