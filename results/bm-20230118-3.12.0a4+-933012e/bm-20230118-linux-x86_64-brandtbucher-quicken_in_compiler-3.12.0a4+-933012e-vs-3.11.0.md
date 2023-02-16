
# Results vs. 3.11.0

- fork: brandtbucher
- ref: quicken_in_compiler
- machine: linux-x86_64
- commit hash: 933012e
- commit date: 2023-01-18
- overall geometric mean: 1.04x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-933012e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 249 ms: 1.04x faster                                                        |
| docutils       | 2.60 sec                                               | 2.48 sec: 1.05x faster                                                      |
| html5lib       | 64.8 ms                                                | 59.8 ms: 1.08x faster                                                       |
| tornado_http   | 96.5 ms                                                | 94.3 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                |

Benchmark hidden because not significant (1): chameleon

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-933012e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 76.8 ms                                                | 72.3 ms: 1.06x faster                                                       |
| pidigits       | 197 ms                                                 | 189 ms: 1.04x faster                                                        |
| nbody          | 90.0 ms                                                | 94.1 ms: 1.05x slower                                                       |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-933012e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 136 ms                                                 | 128 ms: 1.07x faster                                                        |
| regex_v8       | 22.2 ms                                                | 21.2 ms: 1.05x faster                                                       |
| regex_effbot   | 3.46 ms                                                | 3.51 ms: 1.02x slower                                                       |
| regex_dna      | 203 ms                                                 | 207 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-933012e |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 12.4 ms                                                | 9.32 ms: 1.33x faster                                                       |
| unpickle_pure_python | 227 us                                                 | 196 us: 1.16x faster                                                        |
| pickle_pure_python   | 308 us                                                 | 280 us: 1.10x faster                                                        |
| xml_etree_parse      | 160 ms                                                 | 148 ms: 1.08x faster                                                        |
| json_loads           | 26.1 us                                                | 24.1 us: 1.08x faster                                                       |
| xml_etree_iterparse  | 104 ms                                                 | 102 ms: 1.02x faster                                                        |
| xml_etree_process    | 53.7 ms                                                | 54.1 ms: 1.01x slower                                                       |
| pickle_dict          | 31.2 us                                                | 31.6 us: 1.02x slower                                                       |
| pickle_list          | 4.14 us                                                | 4.21 us: 1.02x slower                                                       |
| unpickle_list        | 4.99 us                                                | 5.09 us: 1.02x slower                                                       |
| pickle               | 9.90 us                                                | 10.2 us: 1.03x slower                                                       |
| xml_etree_generate   | 75.9 ms                                                | 78.5 ms: 1.03x slower                                                       |
| unpickle             | 13.3 us                                                | 14.0 us: 1.05x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-933012e |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 8.58 ms                                                | 8.85 ms: 1.03x slower                                                       |
| python_startup_no_site | 6.04 ms                                                | 6.39 ms: 1.06x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.05x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-933012e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml     | 51.4 ms                                                | 46.0 ms: 1.12x faster                                                       |
| genshi_text    | 21.5 ms                                                | 20.0 ms: 1.07x faster                                                       |
| mako           | 9.83 ms                                                | 9.50 ms: 1.04x faster                                                       |
| Geometric mean | (ref)                                                  | 1.06x faster                                                                |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-933012e |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| asyncio_tcp             | 883 ms                                                 | 497 ms: 1.78x faster                                                        |
| json_dumps              | 12.4 ms                                                | 9.32 ms: 1.33x faster                                                       |
| unpickle_pure_python    | 227 us                                                 | 196 us: 1.16x faster                                                        |
| scimark_sparse_mat_mult | 4.59 ms                                                | 3.96 ms: 1.16x faster                                                       |
| deltablue               | 3.66 ms                                                | 3.20 ms: 1.14x faster                                                       |
| genshi_xml              | 51.4 ms                                                | 46.0 ms: 1.12x faster                                                       |
| pickle_pure_python      | 308 us                                                 | 280 us: 1.10x faster                                                        |
| pycparser               | 1.19 sec                                               | 1.08 sec: 1.10x faster                                                      |
| scimark_sor             | 115 ms                                                 | 105 ms: 1.10x faster                                                        |
| richards                | 46.1 ms                                                | 42.2 ms: 1.09x faster                                                       |
| gc_traversal            | 3.82 ms                                                | 3.51 ms: 1.09x faster                                                       |
| nqueens                 | 83.8 ms                                                | 77.2 ms: 1.09x faster                                                       |
| chaos                   | 68.7 ms                                                | 63.3 ms: 1.09x faster                                                       |
| logging_silent          | 98.0 ns                                                | 90.4 ns: 1.08x faster                                                       |
| xml_etree_parse         | 160 ms                                                 | 148 ms: 1.08x faster                                                        |
| html5lib                | 64.8 ms                                                | 59.8 ms: 1.08x faster                                                       |
| json_loads              | 26.1 us                                                | 24.1 us: 1.08x faster                                                       |
| scimark_fft             | 325 ms                                                 | 301 ms: 1.08x faster                                                        |
| sympy_str               | 291 ms                                                 | 270 ms: 1.08x faster                                                        |
| mdp                     | 2.63 sec                                               | 2.44 sec: 1.08x faster                                                      |
| genshi_text             | 21.5 ms                                                | 20.0 ms: 1.07x faster                                                       |
| logging_simple          | 6.02 us                                                | 5.62 us: 1.07x faster                                                       |
| sympy_sum               | 166 ms                                                 | 155 ms: 1.07x faster                                                        |
| regex_compile           | 136 ms                                                 | 128 ms: 1.07x faster                                                        |
| sympy_integrate         | 21.0 ms                                                | 19.7 ms: 1.06x faster                                                       |
| hexiom                  | 6.34 ms                                                | 5.96 ms: 1.06x faster                                                       |
| float                   | 76.8 ms                                                | 72.3 ms: 1.06x faster                                                       |
| fannkuch                | 384 ms                                                 | 362 ms: 1.06x faster                                                        |
| pprint_pformat          | 1.46 sec                                               | 1.37 sec: 1.06x faster                                                      |
| aiohttp                 | 1.05 ms                                                | 991 us: 1.06x faster                                                        |
| pprint_safe_repr        | 706 ms                                                 | 670 ms: 1.05x faster                                                        |
| gunicorn                | 1.12 ms                                                | 1.06 ms: 1.05x faster                                                       |
| go                      | 140 ms                                                 | 134 ms: 1.05x faster                                                        |
| deepcopy                | 341 us                                                 | 325 us: 1.05x faster                                                        |
| pyflate                 | 419 ms                                                 | 399 ms: 1.05x faster                                                        |
| regex_v8                | 22.2 ms                                                | 21.2 ms: 1.05x faster                                                       |
| docutils                | 2.60 sec                                               | 2.48 sec: 1.05x faster                                                      |
| json                    | 4.87 ms                                                | 4.64 ms: 1.05x faster                                                       |
| sympy_expand            | 475 ms                                                 | 453 ms: 1.05x faster                                                        |
| logging_format          | 6.48 us                                                | 6.18 us: 1.05x faster                                                       |
| bench_thread_pool       | 817 us                                                 | 779 us: 1.05x faster                                                        |
| deepcopy_memo           | 35.8 us                                                | 34.4 us: 1.04x faster                                                       |
| 2to3                    | 259 ms                                                 | 249 ms: 1.04x faster                                                        |
| pidigits                | 197 ms                                                 | 189 ms: 1.04x faster                                                        |
| create_gc_cycles        | 1.52 ms                                                | 1.46 ms: 1.04x faster                                                       |
| mako                    | 9.83 ms                                                | 9.50 ms: 1.04x faster                                                       |
| deepcopy_reduce         | 3.02 us                                                | 2.92 us: 1.03x faster                                                       |
| coverage                | 99.3 ms                                                | 96.1 ms: 1.03x faster                                                       |
| scimark_monte_carlo     | 68.0 ms                                                | 65.9 ms: 1.03x faster                                                       |
| raytrace                | 291 ms                                                 | 283 ms: 1.03x faster                                                        |
| thrift                  | 760 us                                                 | 739 us: 1.03x faster                                                        |
| sqlglot_optimize        | 52.7 ms                                                | 51.4 ms: 1.02x faster                                                       |
| tornado_http            | 96.5 ms                                                | 94.3 ms: 1.02x faster                                                       |
| pathlib                 | 18.1 ms                                                | 17.7 ms: 1.02x faster                                                       |
| scimark_lu              | 108 ms                                                 | 106 ms: 1.02x faster                                                        |
| crypto_pyaes            | 75.7 ms                                                | 74.1 ms: 1.02x faster                                                       |
| async_generators        | 356 ms                                                 | 349 ms: 1.02x faster                                                        |
| xml_etree_iterparse     | 104 ms                                                 | 102 ms: 1.02x faster                                                        |
| dulwich_log             | 64.0 ms                                                | 62.9 ms: 1.02x faster                                                       |
| meteor_contest          | 104 ms                                                 | 103 ms: 1.01x faster                                                        |
| sqlglot_normalize       | 108 ms                                                 | 106 ms: 1.01x faster                                                        |
| unpack_sequence         | 44.5 ns                                                | 44.0 ns: 1.01x faster                                                       |
| spectral_norm           | 98.1 ms                                                | 97.4 ms: 1.01x faster                                                       |
| coroutines              | 26.2 ms                                                | 26.0 ms: 1.01x faster                                                       |
| xml_etree_process       | 53.7 ms                                                | 54.1 ms: 1.01x slower                                                       |
| pickle_dict             | 31.2 us                                                | 31.6 us: 1.02x slower                                                       |
| pickle_list             | 4.14 us                                                | 4.21 us: 1.02x slower                                                       |
| regex_effbot            | 3.46 ms                                                | 3.51 ms: 1.02x slower                                                       |
| regex_dna               | 203 ms                                                 | 207 ms: 1.02x slower                                                        |
| async_tree_io           | 1.30 sec                                               | 1.32 sec: 1.02x slower                                                      |
| async_tree_cpu_io_mixed | 736 ms                                                 | 751 ms: 1.02x slower                                                        |
| unpickle_list           | 4.99 us                                                | 5.09 us: 1.02x slower                                                       |
| async_tree_memoization  | 624 ms                                                 | 639 ms: 1.02x slower                                                        |
| sqlglot_transpile       | 1.65 ms                                                | 1.70 ms: 1.03x slower                                                       |
| python_startup          | 8.58 ms                                                | 8.85 ms: 1.03x slower                                                       |
| pickle                  | 9.90 us                                                | 10.2 us: 1.03x slower                                                       |
| sqlglot_parse           | 1.36 ms                                                | 1.41 ms: 1.03x slower                                                       |
| xml_etree_generate      | 75.9 ms                                                | 78.5 ms: 1.03x slower                                                       |
| generators              | 73.5 ms                                                | 76.0 ms: 1.03x slower                                                       |
| sqlite_synth            | 2.48 us                                                | 2.59 us: 1.04x slower                                                       |
| nbody                   | 90.0 ms                                                | 94.1 ms: 1.05x slower                                                       |
| unpickle                | 13.3 us                                                | 14.0 us: 1.05x slower                                                       |
| python_startup_no_site  | 6.04 ms                                                | 6.39 ms: 1.06x slower                                                       |
| dask                    | 365 ms                                                 | 496 ms: 1.36x slower                                                        |
| Geometric mean          | (ref)                                                  | 1.04x faster                                                                |

Benchmark hidden because not significant (6): djangocms, django_template, telco, chameleon, bench_mp_pool, async_tree_none
Ignored benchmarks (5) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230118-3.12.0a4+-933012e/bm-20230118-linux-x86_64-brandtbucher-quicken_in_compiler-3.12.0a4+-933012e.json: mypy
